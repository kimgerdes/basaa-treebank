# Basaa annotation rules — extracted from the literature

Rules for building the Basaa (A43, ISO `bas`) glossed+translated treebank, **extracted from the
scientific articles in [`../docs/`](../docs/)** (especially Hamlaoui & Makasso). They are organised
**by the moment in the pipeline at which they apply**, so an annotator (or a script) can pick up the
right rule at the right stage.

| Stage | File | Applies when you are… |
|---|---|---|
| 1. Transcription | [`transcription.md`](transcription.md) | turning audio / a raw spelling into a canonical Basaa string (tone, segmentation, orthography) |
| 2. Glossing | [`glossing.md`](glossing.md) | adding the morpheme gloss tier (`MISC Gloss=`) + UD features |
| 3. Parsing | [`parsing.md`](parsing.md) | attaching dependencies (SUD/UD) |
| — Flags | [`contradictions.md`](contradictions.md) | **contradictions & open questions** to resolve before scaling |

These **supersede nothing** in [`../glossary/`](../glossary/) or [`../treebank/`](../treebank/); they
distil the *sources behind* those files into actionable rules and **flag where the project's own files
disagree with each other or with the literature** (see `contradictions.md`).

## ✅ Before the next annotation wave — read these

The full instruction set an annotator should review before extending the treebank, grouped by purpose.
**Settled policies** are marked so they are applied uniformly.

**Stage rules (this folder)**
- [`transcription.md`](transcription.md) — tone, syllabic nasal, length, lenition, borrowings (TR-1…9)
- [`glossing.md`](glossing.md) — Hamlaoui-style glosses, class numbers, AGR/CONN/AUG/DEM (GL-1…12)
- [`parsing.md`](parsing.md) — attachment rules incl. **settled: concord = bound morphology (PA-2)**,
  **settled: `í` = locative (PA-6)**, connective, focus-in-situ, HTS cue (PA-1…13)
- [`contradictions.md`](contradictions.md) — the 8 flags; check status before relying on any of them

**Worked analyses & lexicon**
- [`../treebank/syntactic_analysis.md`](../treebank/syntactic_analysis.md) — the SUD analysis, SUD↔UD
  mapping, and the **open annotation decisions** list (decision #1 now resolved)
- [`../treebank/nws_concord_review.md`](../treebank/nws_concord_review.md) — **NWS cases to confirm by
  ear** (concord-on-aux, expletive `i`, the rough nws07 parse, residual `aux`/`case` in SUD)
- [`../glossary/README.md`](../glossary/README.md) + [`basaa_glosses.tsv`](../glossary/basaa_glosses.tsv)
  — the seed lexicon (note FLAG-4/5/6 corrections still pending in the TSV)
- [`../glossary/morphology_child_paradigm.md`](../glossary/morphology_child_paradigm.md) — verb morphology
- [`../glossary/transcription_and_gloss_review.md`](../glossary/transcription_and_gloss_review.md) — house-style review

**Workflow & provenance**
- [`../treebank/ARBORATOR_UPLOAD.md`](../treebank/ARBORATOR_UPLOAD.md) — which files to upload, how audio works
- [`../treebank/audio_alignment.md`](../treebank/audio_alignment.md) — the alignment pipeline (`align.py`, `align_nws.py`)
- [`../TREEBANK_PLAN.md`](../TREEBANK_PLAN.md) — gap analysis & roadmap
- [`../docs/SOURCES.md`](../docs/SOURCES.md) — sources, and the 3 still to obtain (would settle several flags)

## Conventions used in every rule

- **ID** — `TR-n` (transcription), `GL-n` (glossing), `PA-n` (parsing), `FLAG-n` (contradiction).
- **Source** — the article each rule comes from, with the example/section number where possible.
- **Confidence** — `high` (explicitly stated in a source), `med` (inferred/partial), `flag` (sources conflict).
- A ⚠️ marks a rule that is contradicted somewhere; the detail is in `contradictions.md`.

## Sources cited (all in [`../docs/`](../docs/))

| Short cite | File | Type |
|---|---|---|
| **Makasso & Lee 2015** | `basaa.pdf` — *Basaá*, J. IPA 45(1) | IPA illustration; tone, syllable, segmental phonology, fully glossed *North Wind & Sun* |
| **Hamlaoui, Gjersøe & Makasso 2014** | `Hamlaoui_Makasso_2014_HighTone_PhonPhrases_Basaa.pdf` (TAL-2014) | glossed SVO/ditransitive/wh examples; HTS as a phrasing cue; connective syntax |
| **Hamlaoui et al. 2018** | `BULBasaa_corpus_Hamlaoui_et_al_2018_LREC.pdf` | corpus; transcription conventions; tone inventory |
| **Nikitin, O'Connor & Safonova 2022** | `Adda-etal_2022_Tone_prediction_orthographic_conversion_Basaa.pdf` (arXiv 2210.06986) | orthography conversion; tone restoration; tense-by-tone minimal pairs.  ⚠️ *filename is misleading — Adda is cited, not an author; see `contradictions.md` FLAG-8* |
| **Janssens 1986** | `aflin_2033-8732_1986_num_10_1_928.pdf`, *Africana Linguistica* X | historical-comparative; the fullest **noun-class prefix inventory** |
| **Hamlaoui 2020** | `Hamlaoui_2020_realisation_r_francais_basaaphones.pdf` | French of Basaa speakers — *peripheral*, no treebank rules drawn |

Still to obtain (would settle several flags): **Hamlaoui & Makasso 2015** (*Lingua* 154, focus/inversion),
the **"Pronominal F-markers in Basaá"** gloss-abbreviation key, and **Hyman 2003** (baseline morphology).
See [`../docs/SOURCES.md`](../docs/SOURCES.md).
