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
