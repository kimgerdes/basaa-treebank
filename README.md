# Basaa (A43) treebank

Materials toward **the first glossed, translated and audio-aligned dependency treebank of Basaa**
(Bàsàá, ISO 639‑3 `bas`, Glottolog `basa1284`, Guthrie **A43** / group A.40, Cameroon).

- 🌳 **Browse & annotate (with playable audio):** the *Bàsàá* project on Arborator-Grew —
  <https://arborator.grew.fr/#/projects/B%C3%A0s%C3%A0%C3%A1>
- 🔊 **Demo / data hub:** <https://elizia.net/basaa/> (sentence list with in-browser audio players)
- The treebank is annotated in **SUD** (Surface-syntactic Universal Dependencies), with a UD copy of
  the literature sample for comparison.

## What's here

| Path | What |
|---|---|
| [`treebank/`](treebank/) | The treebank: **`basaa_audio.arborator.sud.conllu`** (21 audio-aligned sentences), SUD/UD samples, the forced-alignment scripts, and the syntactic analysis + upload notes |
| [`glossary/`](glossary/) | [`basaa_glosses.tsv`](glossary/basaa_glosses.tsv) (~90 common words, glosses, noun classes); the *child*-paradigm morphology; the transcription & gloss review |
| [`rules/`](rules/) | Annotation rules extracted from the literature, by pipeline stage — [transcription](rules/transcription.md), [glossing](rules/glossing.md), [parsing](rules/parsing.md), and flagged [contradictions](rules/contradictions.md) |
| [`recordings/`](recordings/) | **Metadata only** (manifests, forced-alignment offsets, Praat TextGrids, provenance READMEs). Audio is **not** in this repo — see §Copyright |
| [`corpora/`](corpora/) | Provenance/README for the text & parallel data (OPUS); raw dumps not bundled |
| [`docs/`](docs/) | [`SOURCES.md`](docs/SOURCES.md) + `resources.md` (annotated bibliography). The PDFs themselves are **not** redistributed |
| [`TREEBANK_PLAN.md`](TREEBANK_PLAN.md) | Gap analysis & roadmap to scale beyond this seed |
| [`treebank/index.html`](treebank/index.html) | The demo page deployed at elizia.net/basaa |

## Status

- **21 audio-aligned sentences**: 10 isolated "child" utterances (clean — transcription, Hamlaoui-style
  glosses, SUD parse, **word-level** forced alignment) + 11 *North Wind & the Sun* clause units
  (sentence-level timing reliable; word forms & parse **draft**, to re-transcribe by ear).
- Audio time-aligned with **torchaudio's MMS** multilingual forced aligner; each token is clickable in
  Arborator-Grew.
- A separate 5-sentence **literature sample** (SUD + UD) showcases the core constructions
  (concord, the connective, copula).

## Highest-leverage next step

Obtain the **BULBasaa** corpus (Hamlaoui et al. 2018; ELRA) — ~50 h speech with a transcribed +
orally-translated subset. It supplies most of a treebank's substrate; this repo's format is ready to
receive it.

---

## Copyright, licences & attribution

This project deliberately separates **our own scholarly contributions** (freely licensed below) from
**third-party material that we do not have the right to redistribute** (excluded from the repo, cited
and linked instead).

### Our contributions — freely licensed

The **treebank annotations, glosses, lexicon, morphological/syntactic analyses, rules and prose** in
this repository are © the project authors (Kim Gerdes and collaborators) and released under
**[Creative Commons Attribution 4.0 International (CC‑BY‑4.0)](LICENSE)**.
The **scripts** (`treebank/*.py`) are additionally available under the **MIT License**.
If you use the treebank, please cite it (see *Citation* below) and attribute the underlying sources.

### Third-party material — NOT redistributed here

| Material | Rights holder / source | Why it's excluded · how to get it |
|---|---|---|
| **Speech recordings** (the audio behind every `# sound_url`) | **Makasso, E.-M. & Lee, S. J. (2015). "Basaá." *JIPA* 45(1): 71–79** — Illustration of the IPA. Audio © **International Phonetic Association / Cambridge University Press**. | The CUP terms permit download **for personal/research use** but state the files "may **not** be incorporated in another product without the permission of Cambridge University Press." We therefore **do not bundle them**. The treebank instead **references** them by URL. Download the original `Basaa.zip` from the article's supplementary materials on Cambridge Core. |
| **Scientific articles** (`docs/*.pdf`) | Respective authors/publishers (Hamlaoui, Makasso, Hyman, Adda et al., …) | Copyrighted. **Not redistributed.** Full citations and where to obtain each: [`docs/SOURCES.md`](docs/SOURCES.md). |
| **GlobalRecordings.net audio** (other spoken Basaa) | © GlobalRecordings.net | Evangelism recordings, redistribution restricted. Not in repo; see `recordings/README.md`. |
| **OPUS text/parallel data** (Mozilla‑l10n, translatewiki) | OPUS · Mozilla · translatewiki contributors | Licences vary by corpus. Not bundled; re-fetch per [`corpora/README.md`](corpora/README.md). |
| **Forced-alignment model** (MMS) | Meta AI, `torchaudio` | Used only to compute timing offsets; the model is **not** redistributed. The resulting millisecond timestamps (factual data) are included. |

The audio is currently **hosted for research use** at `https://elizia.net/basaa/`, which the
`# sound_url` fields point to, so the treebank is usable without bundling the media. **Re-hosting the
IPA recordings elsewhere requires permission from Cambridge University Press.**

### Language-data acknowledgement

The Basaa language data was produced by a native-speaker consultant for Makasso & Lee (2015). We thank
**Emmanuel-Moselly Makasso** and **Fatima Hamlaoui**, whose published descriptions of Bàsàá (A43)
underpin the glossing and syntactic analysis here.

## Citation

> Gerdes, K. and collaborators (2026). *Basaa (A43) audio-aligned SUD treebank* (v0.1).
> Annotations CC‑BY‑4.0. Speech © IPA/CUP (Makasso & Lee 2015), used by reference.

Underlying linguistic sources to cite alongside: Makasso & Lee (2015); Hamlaoui & Makasso (2014, 2015);
Hyman (2003). See [`docs/SOURCES.md`](docs/SOURCES.md).
