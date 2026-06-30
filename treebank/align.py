#!/usr/bin/env python
"""Forced-align the Basaa child sentences with torchaudio's MMS multilingual aligner.
Tokens come straight from basaa_aligned.sud.conllu so offsets map 1:1 onto treebank tokens.
Outputs: token offsets (TSV), Praat TextGrids, and an updated arborator conllu."""
import os, re, json, sys
os.environ.setdefault("TORCH_HOME", "/bigstorage/kim/tmp/torchhome")
import torch, torchaudio, soundfile as sf
import numpy as np
from torchaudio.pipelines import MMS_FA as bundle

def load_wav(path):
    data, sr = sf.read(path, dtype="float32")
    if data.ndim > 1: data = data.mean(axis=1)
    return torch.from_numpy(np.ascontiguousarray(data)).unsqueeze(0), sr

ALIGN_DIR = "/bigstorage/kim/basaa/recordings/aligned"
CONLLU    = "/bigstorage/kim/basaa/treebank/basaa_aligned.sud.conllu"
SR = bundle.sample_rate  # 16000

# --- parse conllu: sent_id -> (audio_filename, [tokens]) ---
def parse():
    sents=[]; sid=None; audio=None; toks=[]
    for line in open(CONLLU, encoding="utf-8"):
        line=line.rstrip("\n")
        if line.startswith("# sent_id"):
            if sid: sents.append((sid,audio,toks))
            sid=line.split("=")[1].strip(); audio=None; toks=[]
        elif line.startswith("# audio"): audio=line.split("=")[1].strip().split("/")[-1]
        elif line and not line.startswith("#"):
            c=line.split("\t")
            if c[0].isdigit(): toks.append(c[1])
    if sid: sents.append((sid,audio,toks))
    return [s for s in sents if s[1]]  # only sentences with audio

# romanize for the MMS dict: lowercase, keep a-z only per token
def norm(tok):
    t=re.sub(r"[^a-z]","", tok.lower())
    return t if t else "a"   # fallback for punctuation-only

def main():
    print("loading MMS_FA model (downloads ~1.2GB on first run)...", flush=True)
    model = bundle.get_model()
    tokenizer = bundle.get_tokenizer()
    aligner = bundle.get_aligner()
    rows=[]; offsets={}
    for sid,audio,toks in parse():
        path=os.path.join(ALIGN_DIR, audio)
        wav, sr = load_wav(path)
        if sr!=SR: wav=torchaudio.functional.resample(wav, sr, SR)
        transcript=[norm(t) for t in toks]
        with torch.inference_mode():
            emission,_=model(wav)
            spans=aligner(emission[0], tokenizer(transcript))
        ratio = wav.size(1)/emission.size(1)
        def f2ms(x): return int(round(x*ratio/SR*1000))
        tok_off=[]
        for tok, sp in zip(toks, spans):
            b,e=f2ms(sp[0].start), f2ms(sp[-1].end)
            tok_off.append((tok,b,e)); rows.append((sid,tok,b,e))
        offsets[sid]=tok_off
        print(f"{sid}: "+"  ".join(f"{t}[{b}-{e}]" for t,b,e in tok_off), flush=True)
    # write TSV
    with open(os.path.join(ALIGN_DIR,"forced_align_offsets.tsv"),"w") as f:
        f.write("sent_id\ttoken\tbegin_ms\tend_ms\n")
        for r in rows: f.write("\t".join(map(str,r))+"\n")
    json.dump(offsets, open("/bigstorage/kim/tmp/offsets.json","w"))
    # write Praat TextGrids (one per sentence)
    tg_dir=os.path.join(ALIGN_DIR,"textgrids"); os.makedirs(tg_dir, exist_ok=True)
    for sid,toks in offsets.items():
        xmax=toks[-1][2]/1000.0
        items=[]
        for t,b,e in toks:
            items.append((b/1000.0, e/1000.0, t))
        with open(os.path.join(tg_dir, sid+".TextGrid"),"w",encoding="utf-8") as f:
            f.write('File type = "ooTextFile"\nObject class = "TextGrid"\n\n')
            f.write(f"xmin = 0\nxmax = {xmax}\ntiers? <exists>\nsize = 1\nitem []:\n")
            f.write('    item [1]:\n        class = "IntervalTier"\n        name = "words"\n')
            f.write(f"        xmin = 0\n        xmax = {xmax}\n        intervals: size = {len(items)}\n")
            for i,(b,e,t) in enumerate(items,1):
                f.write(f"        intervals [{i}]:\n            xmin = {b}\n            xmax = {e}\n            text = \"{t}\"\n")
    print("\nwrote forced_align_offsets.tsv, textgrids/, offsets.json")

if __name__=="__main__": main()
