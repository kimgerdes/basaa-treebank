# Playable audio in Arborator-Grew (spoken-language treebanks)

How to make a CoNLL-U treebank whose sound can be played, per token, inside
[arborator.grew.fr](https://arborator.grew.fr).

## How it works

Arborator-Grew builds its play controls from two things in the CoNLL-U:

1. **`# sound_url =` (sentence metadata)** — a URL to the audio for that sentence.
   It must be a publicly reachable `http(s)` URL; the browser fetches it directly,
   so a local file path will *not* play.
2. **`AlignBegin=` / `AlignEnd=` in the MISC column (token level)** — start/end
   offsets **in milliseconds** into that audio file. These make each token
   clickable (play just its slice) and highlight tokens in sync during playback.

When both are present, a play button appears; you can play the whole utterance or
click a single word to hear its span.

## Conventions (from UD_Naija-NSC, the reference spoken treebank)

- **`sound_url` is per sentence**, repeated in each sentence's metadata block.
  Several sentences may point into the *same* long recording — they just use
  different `AlignBegin`/`AlignEnd` ranges.
- **Every token carries `AlignBegin`/`AlignEnd`**, contiguous (one token's end ≈
  the next token's begin). Punctuation/pauses get their own spans; a zero-length
  span like `AlignBegin=3320|AlignEnd=3320` is fine.
- Values are millisecond integers, living in MISC as pipe-separated `Key=Value`
  pairs alongside everything else (e.g. `Gloss=…`).

### Real example

```conllu
# sent_id = ABJ_GWA_08_David-Lifestory_MG__1
# sound_url = https://naijasyncor.huma-num.fr/carte/mp3/ABJ_GWA_08_Davids-lifestory_MG.mp3
# text = ehm # di time wey I dey with ...
1   ehm    ehm    INTJ   _   _                  38  discourse  _   AlignBegin=1664|AlignEnd=1970|Gloss=ehm
2   #      #      PUNCT  _   _                   1  punct      _   AlignBegin=2000|AlignEnd=2210|Gloss=PUNCT
3   di     di     DET    _   Definite=Def        4  det        _   AlignBegin=2210|AlignEnd=2410|Gloss=DEF.ART
4   time   time   NOUN   _   _                  38  obl:mod    _   AlignBegin=2410|AlignEnd=2707|Gloss=time
```

## Applying it to this Basaa treebank

`basaa_sample.conllu` currently has no audio fields. To make it playable:

1. **Host the audio** at a stable public URL (Naija uses Huma-Num; GitHub raw, a
   project server, or any static host works). One file per sentence, or one long
   file indexed by offsets.
2. **Add `# sound_url = …`** to each sentence's metadata block, next to the
   existing `# text =` / `# source =` lines.
3. **Add `AlignBegin=…|AlignEnd=…`** (ms) to each token's MISC, prepended to what
   is already there, e.g.:

   ```conllu
   1   Sogol   sokol   NOUN   _   NounClass=Bantu1|Number=Sing   2   nsubj   _   AlignBegin=0|AlignEnd=540|Gloss=1.grandfather|Eng=grandfather
   ```

4. **Upload to arborator.grew.fr**: create/open a project and import the
   CoNLL-U. If `sound_url` is browser-reachable and the offsets are valid, the
   play controls appear automatically.

### Practical tips

- Keep MISC key order consistent across tokens.
- Make sure every offset stays within the file's duration.
- For many sentences in one recording, derive `AlignBegin`/`AlignEnd` from a
  forced-alignment tool (e.g. WebMAUS, or a Praat TextGrid → ms) rather than by
  hand.

## ✅ DEPLOYED & LIVE (2026-06-30)

The 10 child sentences are now fully playable in Arborator-Grew:
- **Audio:** MP3s at `https://elizia.net/basaa/bas_s*.mp3` (nginx `location ^~ /basaa/`, CORS `*`,
  byte-range enabled, `audio/mpeg`). NWS passage also there.
- **Offsets:** real **word-level** `AlignBegin/AlignEnd` from torchaudio MMS forced alignment
  (`recordings/aligned/forced_align_offsets.tsv`, Praat TextGrids in `recordings/aligned/textgrids/`).
- **Treebank:** `basaa_aligned.arborator.sud.conllu` has `# sound_url =` + offsets; also hosted at
  `https://elizia.net/basaa/basaa_aligned.arborator.sud.conllu`. Import it into Arborator-Grew → per-word
  play works immediately.

Remaining: the **NWS 52 s passage** still needs its 9-clause transcription fed to the aligner to be
split into sentence spans (the 10 child sentences are done).

## Status detail (checked 2026-06-30)

- **Trees only (no audio):** ready now. `basaa_sample.sud.conllu`, `basaa_aligned.sud.conllu`,
  `basaa_sample.conllu` are valid CoNLL-U and import straight into Arborator-Grew; `Gloss=` shows as a
  gloss tier. Nothing missing for the dependency/SUD view.
- **With playable audio:** `basaa_aligned.arborator.sud.conllu` is generated — it adds
  `# sound_url =` and per-token `AlignBegin/AlignEnd` (ms) to the 10 audio-aligned child sentences.
  **Two manual steps remain:**
  1. **Host the WAVs** (`../recordings/aligned/*.wav`) at a public http(s) URL and replace the
     `REPLACE_WITH_PUBLIC_HOST` base in that file. (The Cambridge source zip is public but not
     per-sentence; per Makasso & Lee's IPA/CUP licence the clips are for research use — check before
     re-hosting publicly.)
  2. Offsets are currently **sentence-level** (each token spans the whole clip → play button works,
     but no per-word highlight). For word-level highlighting, forced-align (MFA/WebMAUS/Praat → ms)
     and replace the spans. The 226 single-word clips in `../recordings/IPA_Makasso_Lee_2015/` give a
     ready pronunciation lexicon for the aligner.
- **NWS passage** (`bas_NWS`, one 52 s file, 9 sentences) is **not yet** offset-indexed — it needs
  forced alignment to split into clause spans before it is Arborator-playable.

## Sources

- [When Collaborative Treebank Curation Meets Graph Grammars (Arborator-Grew, LREC 2020)](https://aclanthology.org/2020.lrec-1.651/)
- [UD_Naija-NSC README — sound_url / AlignBegin / AlignEnd convention](https://github.com/UniversalDependencies/UD_Naija-NSC/blob/master/README.md)
- [UD_Naija-NSC treebank (live example of audio-aligned CoNLL-U)](https://github.com/UniversalDependencies/UD_Naija-NSC)
- [Arborator-Grew documentation repo](https://github.com/khansadaoudi/arboratordocs)
