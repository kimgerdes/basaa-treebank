# Basaa sound recordings

Spoken Basaa (Bàsàá, A43, ISO 639‑3 `bas`, Glottolog `basa1284`) audio collected for the
treebank project. All files here are openly downloadable. Provenance and licensing below.

## Contents

| Folder / file | Source | Genre | Tracks | Notes |
|---|---|---|---|---|
| `GRN_62699_Ngwin_Nlam_GoodNews_mp3/` | GlobalRecordings.net program 62699 "Ŋwìn Ňlam / Good News" | Narrated Bible-picture narration | 42 | Connected monologue, one speaker; matches a known picture script (good for forced alignment) |
| `GRN_62709_Songs_mp3/` | GRN program 62709 "Songs" | Sung Basaa | 8 | Music; lower value for syntax, useful for phonetics/prosody |
| `GRN_25370_Becoming_Friend_of_God_BassaMomo_mp3/` | GRN program 25370 | Narration | 2 | **Bassa "Momo" variety** — dialectal, flag separately |
| `GRN_Basaa_The_Two_Roads.mp3` | GRN GoKit | Short narration | 1 | Standalone clip |

Total: 53 MP3 files, ~178 MB of speech.

## Source details

**GlobalRecordings.net (GRN)** — <https://globalrecordings.net/en/language/bas>.
Religious narration/songs recorded for evangelism, freely streamable/downloadable.
Audio is © GRN; redistribution is restricted but personal/academic research use of the
downloads is permitted. Each track has an associated *script* (the narration text); the
English master script for "Good News" is at `/en/script/en/395` on the GRN site. Pulling the
Basaa-language script text would give a rough transcript to align against — a worthwhile next
step (see `../TREEBANK_PLAN.md`).

## ✅ IPA Illustration audio (Makasso & Lee 2015) — OBTAINED

`IPA_Makasso_Lee_2015/` — the supplementary sound files of the *JIPA* 45(1) Basaá illustration,
downloaded from Cambridge's static CDN (licensed for personal/research use). **This is the cleanest
sound+transcription material we have:** 226 single-word clips (each filename = its meaning; IPA in
`../docs/basaa.pdf`), **10 individually-aligned full sentences**, and the 52 s "North Wind and the
Sun" passage. The 10 sentences + NWS are extracted and paired with transcriptions in
[`aligned/`](aligned/) (see `aligned/README.md` and `aligned/manifest.tsv`).

## Known gaps (could not be auto-downloaded)

- **BULBasaa corpus (Hamlaoui et al. 2018)** — ~50 h speech, ~10 h phonetically transcribed +
  orally translated, Basaa–French. **Not a free download**; request via ELRA
  (<https://catalog.elra.info>). This is the single highest-value resource for a treebank and is
  worth requesting by email (the corpus paper is at `../docs/BULBasaa_corpus_Hamlaoui_et_al_2018_LREC.pdf`).
- **Mozilla Common Voice (bas)** — validated clips paired with orthographic transcripts; download
  is gated behind an email form / Hugging Face token. The matching *sentence text* is already here
  under `../corpora/opus/` (the Mozilla-l10n corpus is largely Common Voice UI + sentence-collector
  prompts).
- **SLDR/ORTOLANG "Bàsàa – oral spontané" (Makasso 2008)** — spontaneous speech, often openly
  accessible; OLAC id `oai:sldr.org:sldr000737`.
