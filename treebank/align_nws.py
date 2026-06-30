#!/usr/bin/env python
"""Align the North Wind & the Sun passage (one 52s file, 11 clause units) and emit
a SUD conllu where all units share the same sound_url with per-unit + per-token offsets.
TRANSCRIPTION IS PROVISIONAL (PDF IPA tier is mangled); parses are DRAFT. Refine in Arborator."""
import os, json
os.environ.setdefault("TORCH_HOME","/bigstorage/kim/tmp/torchhome")
import torch, torchaudio, soundfile as sf, numpy as np
from torchaudio.pipelines import MMS_FA as bundle
SR=bundle.sample_rate
WAV="/bigstorage/kim/basaa/recordings/aligned/bas_NWS_north_wind_and_sun.wav"
MP3="https://elizia.net/basaa/bas_NWS_north_wind_and_sun.mp3"
OUT_SRC="/bigstorage/kim/basaa/treebank/basaa_nws.sud.conllu"
OUT_ARB="/bigstorage/kim/basaa/treebank/basaa_nws.arborator.sud.conllu"

# (form, upos, gloss, head, deprel)  -- forms provisional, parse draft
NWS=[
 ("bas_nws01","The North Wind and the Sun were arguing.","La bise et le soleil se disputaient.",[
   ("mbebi","NOUN","wind",7,"subj"),("mabera","PROPN","north",1,"mod"),("ni","CCONJ","with",4,"cc"),
   ("hanga","NOUN","sun",1,"conj"),("ba","PRON","2.AGR",7,"dep"),("ba","AUX","be",7,"aux"),
   ("pehmba","VERB","argue",0,"root")]),
 ("bas_nws02","one day, about which of them was stronger,","un jour, à propos duquel était le plus fort,",[
   ("kel","NOUN","day",9,"mod"),("jada","NUM","one",1,"mod"),("inyu","ADP","for",4,"mark"),
   ("liji","VERB","know",9,"dep"),("nje","PRON","who",7,"subj"),("a","PRON","AGR",7,"dep"),
   ("gwee","VERB","have",9,"dep"),("nguy","NOUN","strength",7,"comp:obj"),("lo","VERB","surpass",0,"root"),
   ("nunu","PRON","this.one",9,"comp:obj")]),
 ("bas_nws03","when a traveler came along wrapped up in an overcoat,","quand un voyageur arriva enveloppé dans un manteau,",[
   ("hanyen","ADV","then",5,"mod"),("ngken","NOUN","stranger",3,"mod"),("mur","NOUN","man",5,"subj"),
   ("a","PRON","AGR",5,"dep"),("bitihi","VERB","arrive",0,"root"),("a","PRON","he",9,"subj"),
   ("ba","AUX","be",9,"aux"),("heeba","VERB","wear",5,"mod"),("kori","NOUN","coat",8,"comp:obj"),
   ("mbeng","NOUN","rain",9,"mod")]),
 ("bas_nws04","they agreed that the one who could make the traveler take off","ils convinrent que celui qui ferait ôter au voyageur",[
   ("ba","PRON","they",2,"subj"),("nogla","VERB","agree",0,"root"),("le","SCONJ","that",6,"mark"),
   ("i","PRON","the.one",6,"subj"),("a","PRON","AGR",6,"dep"),("mbong","VERB","make",2,"comp:obj"),
   ("ngken","NOUN","stranger",8,"mod"),("mur","NOUN","man",6,"comp:obj"),("le","SCONJ","that",11,"mark"),
   ("a","PRON","he",11,"subj"),("heja","VERB","take.off",6,"comp:obj")]),
 ("bas_nws05","his coat would be considered the stronger.","son manteau serait considéré le plus fort.",[
   ("kori","NOUN","coat",7,"subj"),("jee","PRON","his",1,"mod"),("nyen","PRON","the.one",1,"mod"),
   ("a","PRON","AGR",7,"dep"),("gwee","VERB","have",7,"dep"),("nguy","NOUN","strength",5,"comp:obj"),
   ("lo","VERB","surpass",0,"root"),("nunu","PRON","this.one",7,"comp:obj")]),
 ("bas_nws06","Then the wind blew as hard as he could,","Alors la bise souffla de toutes ses forces,",[
   ("we","ADV","then",4,"mod"),("mbebi","NOUN","wind",4,"subj"),("i","PRON","AGR",4,"dep"),
   ("bihong","VERB","blow",0,"root"),("ni","ADP","with",6,"case"),("nguy","NOUN","strength",4,"mod"),
   ("libim","NOUN","quantity",9,"mod"),("i","PRON","it",9,"dep"),("bela","VERB","be.able",4,"mod")]),
 ("bas_nws07","but the harder he blew, the tighter the man wrapped his coat;","mais plus il soufflait, plus l'homme serrait son manteau;",[
   ("ndi","CCONJ","but",7,"cc"),("kii","SCONJ","as",7,"mark"),("jo","PRON","him",7,"subj"),
   ("i","PRON","it",7,"dep"),("be","AUX","be",7,"aux"),("hongoh","VERB","blow",0,"root"),
   ("jah","ADV","also",6,"mod"),("mur","NOUN","man",10,"subj"),("a","PRON","AGR",10,"dep"),
   ("surge","VERB","tighten",7,"conj"),("kori","NOUN","coat",10,"comp:obj"),("jee","PRON","his",11,"mod")]),
 ("bas_nws08","and at last the wind gave up trying.","et finalement la bise renonça.",[
   ("ibol","SCONJ","till",6,"mark"),("le","SCONJ","that",6,"mark"),("te","SCONJ","till",6,"mark"),
   ("mbebi","NOUN","wind",6,"subj"),("i","PRON","AGR",6,"dep"),("bito","VERB","be.tired",0,"root"),
   ("i","PRON","it",8,"dep"),("waa","VERB","stop",6,"conj"),("hong","VERB","blow",8,"comp:obj")]),
 ("bas_nws09","Then the sun began to shine with strength,","Alors le soleil se mit à briller avec force,",[
   ("hanga","NOUN","sun",3,"subj"),("hi","PRON","9.AGR",3,"dep"),("boroo","VERB","start",0,"root"),
   ("baj","VERB","shine",3,"comp:obj"),("ni","ADP","with",4,"mod"),("nguy","NOUN","strength",5,"comp:obj")]),
 ("bas_nws10","and right away the traveler took off his coat.","et aussitôt le voyageur ôta son manteau.",[
   ("ibol","SCONJ","till",7,"mark"),("le","SCONJ","that",7,"mark"),("te","SCONJ","till",7,"mark"),
   ("ngken","NOUN","stranger",5,"mod"),("mur","NOUN","man",7,"subj"),("a","PRON","AGR",7,"dep"),
   ("heja","VERB","take.off",0,"root"),("kori","NOUN","coat",7,"comp:obj"),("jee","PRON","his",8,"mod")]),
 ("bas_nws11","And so the North Wind had to admit that the Sun was the stronger.","Et la bise dut reconnaître que le soleil était le plus fort.",[
   ("hanyen","ADV","then",5,"mod"),("mbebi","NOUN","wind",5,"subj"),("mabera","PROPN","north",2,"mod"),
   ("i","PRON","AGR",5,"dep"),("binea","VERB","accept",0,"root"),("le","SCONJ","that",9,"mark"),
   ("hanga","NOUN","sun",9,"subj"),("hi","PRON","9.AGR",9,"dep"),("nlel","VERB","surpass",5,"comp:obj"),
   ("jo","PRON","it",9,"dep"),("nguy","NOUN","strength",9,"comp:obj")]),
]

# --- bound-concord policy (rules/parsing.md PA-2 option b) -------------------
# The raw NWS list above keeps the preverbal subject-concord as a SEPARATE token
# (easy to re-transcribe by ear). At write time we FOLD each concord into its host
# verb: form -> concord+verb, FEATS NounClass=Bantu<n>, Gloss <n>.AGR-<stem>.
# Pronominal subjects / object pronouns (he/him/they/it/the.one) are LEFT as tokens.
# sid -> [(concord_idx, host_idx, flag_or_None)]  (1-based indices into the raw list)
FOLDS = {
 'bas_nws01': [(5,6,"concord 2.AGR attaches to AUX 'ba'(be), not main verb 'pehmba' — confirm host by ear")],
 'bas_nws02': [(6,7,None)],
 'bas_nws03': [(4,5,None)],
 'bas_nws04': [(5,6,None)],
 'bas_nws05': [(4,5,"draft attached 'a' to root 'lo'; refolded onto 'gwee' — confirm")],
 'bas_nws06': [(3,4,None),(8,9,"'i' was glossed 'it'; treated as cl.9 concord on 'bela' — confirm it is a subject marker, not a pronoun")],
 'bas_nws07': [(4,5,"'i'(it) folds onto AUX 'be'; sentence parse is rough — reparse by ear"),(9,10,None)],
 'bas_nws08': [(5,6,None),(7,8,"'i' was glossed 'it'; treated as concord on 'waa' — confirm")],
 'bas_nws09': [(2,3,None)],
 'bas_nws10': [(6,7,None)],
 'bas_nws11': [(4,5,None),(8,9,None)],
}
CLASS = {'a':1,'i':9,'hi':9,'ba':2}  # concord form -> Bantu class

def fold_sentence(sid, toks):
    """toks: [(form,upos,gloss,head,dep)] -> list of dicts with folded tokens.
    Each out token: oidx,form,lemma,upos,feats,head,dep,gloss,morph,flag,raw(0-based src idx)."""
    out=[{'oidx':i+1,'form':f,'lemma':f,'upos':u,'feats':'_','head':h,'dep':d,'gloss':g,
          'morph':None,'flag':None,'raw':[i]} for i,(f,u,g,h,d) in enumerate(toks)]
    remove=set()
    for cid,hid,flag in FOLDS.get(sid,[]):
        c=out[cid-1]; host=out[hid-1]
        assert c['upos']=='PRON', f"{sid}: tok {cid} not PRON"
        cls=CLASS[c['form']]
        host['lemma']=host['form']
        host['form']=c['form']+host['form']
        host['feats']=f"NounClass=Bantu{cls}"
        host['gloss']=f"{cls}.AGR-{host['gloss']}"
        host['morph']=f"{c['form']}-{host['lemma']}"
        host['flag']=flag
        host['raw']=sorted(c['raw']+host['raw'])
        remove.add(cid-1)
    survivors=[t for k,t in enumerate(out) if k not in remove]
    pos={t['oidx']:ni for ni,t in enumerate(survivors,1)}   # old 1-based -> new 1-based
    for cid,hid,_ in FOLDS.get(sid,[]):                     # removed concord -> host's new id
        pos[cid]=pos[out[hid-1]['oidx']]
    for t in survivors:
        t['head']=0 if t['head']==0 else pos[t['head']]
    return survivors

def norm(f):
    import re; t=re.sub(r"[^a-z]","",f.lower()); return t or "a"

def main():
    wav,sr=sf.read(WAV,dtype="float32")
    if wav.ndim>1: wav=wav.mean(1)
    wav=torch.from_numpy(np.ascontiguousarray(wav)).unsqueeze(0)
    if sr!=SR: wav=torchaudio.functional.resample(wav,sr,SR)
    model=bundle.get_model(); tok=bundle.get_tokenizer(); aln=bundle.get_aligner()
    allforms=[w[0] for s in NWS for w in s[3]]
    transcript=[norm(f) for f in allforms]
    print(f"aligning {len(transcript)} tokens over {wav.size(1)/SR:.1f}s ...",flush=True)
    with torch.inference_mode():
        emission,_=model(wav); spans=aln(emission[0],tok(transcript))
    ratio=wav.size(1)/emission.size(1)
    f2ms=lambda x:int(round(x*ratio/SR*1000))
    offs=[(f2ms(sp[0].start),f2ms(sp[-1].end)) for sp in spans]
    # write source + arborator
    src=open(OUT_SRC,"w",encoding="utf-8"); arb=open(OUT_ARB,"w",encoding="utf-8")
    hdr=("# === Basaa — North Wind & the Sun (SUD) ===\n"
         "# 11 clause units, one shared recording. TRANSCRIPTION PROVISIONAL, PARSE DRAFT —\n"
         "# refine by listening in Arborator (each token is clickable).\n"
         "# Subject-concord is BOUND onto the verb (NounClass feature); spaced form in # text_practical.\n"
         "# Flagged cases (MISC Flag=) are listed in nws_concord_review.md.\n\n")
    src.write(hdr); arb.write(hdr.replace("(SUD)","(SUD, audio for Arborator)"))
    k=0
    for sid,eng,fra,toks in NWS:
        # per-raw-token offsets for this sentence, then fold
        roff=offs[k:k+len(toks)]; k+=len(toks)
        s0=roff[0][0]; s1=roff[-1][1]
        fold=fold_sentence(sid, toks)
        forms=" ".join(t['form'] for t in fold)
        practical=" ".join(w[0] for w in toks)
        meta=(f"# sent_id = {sid}\n# text = {forms}\n"
              f"# text_practical = {practical}\n# text_eng = {eng}\n# text_fra = {fra}\n")
        src.write(meta)
        arb.write(meta+f"# sound_url = {MP3}\n# AlignBegin = {s0}\n# AlignEnd = {s1}\n")
        for i,t in enumerate(fold,1):
            b=min(roff[r][0] for r in t['raw']); e=max(roff[r][1] for r in t['raw'])
            misc=[f"Gloss={t['gloss']}"]
            if t['morph']: misc.append(f"Morph={t['morph']}")
            if t['flag']:  misc.append(f"Flag={t['flag']}")
            base=f"{i}\t{t['form']}\t{t['lemma']}\t{t['upos']}\t_\t{t['feats']}\t{t['head']}\t{t['dep']}\t_\t"
            src.write(base+"|".join(misc)+"\n")
            arb.write(base+f"AlignBegin={b}|AlignEnd={e}|"+"|".join(misc)+"\n")
        src.write("\n"); arb.write("\n")
        print(f"{sid}: [{s0}-{s1}ms] {forms}")
    src.close(); arb.close()
    print("\nwrote",OUT_SRC,"and",OUT_ARB)

if __name__=="__main__": main()
