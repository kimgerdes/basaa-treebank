# Basaa text corpora

Plain-text / parallel data for Basaa (`bas`). Raw material for lemma lists, frequency-based
"common word" selection, and parallel-projection of annotations.

## `opus/` — OPUS parallel & monolingual data

Downloaded via the OPUS API (<https://opus.nlpl.eu>). For Basaa, OPUS currently exposes **only two
corpora**, both small and both essentially Mozilla-project text:

| File | Pairs / lines | Description |
|---|---|---|
| `Mozilla-l10n_bas.mono.txt` | 843 lines (~770 markup-free) | Monolingual Basaa: Common Voice UI strings **and** sentence-collector prose. The prose lines are real, well-formed Basaa sentences with rich morphology — the most useful part. |
| `Mozilla-l10n_bas.freq` | 843 types | Word-frequency list. Basis for the "common words" selection in `../glossary/`. Caveat: inflated by UI tokens (`common`, `voice`, `hop`…). |
| `Mozilla-l10n_bas-fr.xml` | 933 links | Basaa↔French sentence alignment (`cesAlign`; text lives in the per-language docs, IDs referenced by `xtargets`). |
| `Mozilla-l10n_bas-en.xml` | 764 links | Basaa↔English alignment. |
| `translatewiki_bas-fr.xml` | 48 links | Tiny MediaWiki-interface translation set. |

**Note on JW300:** `docs/resources.md` claimed JW300 has "thousands of aligned Basaa sentences."
The live OPUS index does **not** list JW300 (or any Bible corpus) for `bas` — only the two Mozilla
sets above. Treat the JW300 claim as unverified. There is no large open Basaa parallel corpus.

## `crubadan/` — Crúbadán web crawl  ❌ UNAVAILABLE

The Crúbadán Basaa data (web-crawled text + word/char n-gram lists, `oai:crubadan.org:bas`) could
**not** be retrieved: `crubadan.org` is unreachable (DNS/host down, returns `000`), and the Wayback
Machine has **no capture of the data file** `crubadan.org/files/bas.zip` (only of the HTML landing
page). Folder kept as a placeholder. Retry later, or contact Kevin Scannell directly.

## Other lexical resources (not bulk-downloadable)

- **Webonary** — Njock (2019) *Dictionnaire ɓàsàa-français-anglais-allemand* (SIL), queryable at
  <https://webonary.org> (`oai:webonary.org:33`). No bulk export; would need scraping or an SIL request.
- **PanLex** — cross-lingual lexical translations incl. Basaa, downloadable as JSON/CSV from
  <https://panlex.org> (bulk database only; no per-language slice). Good source for seeding lemmas.
- **Lemb & de Gastines (1973)** *Dictionnaire basaá-français* — the reference dictionary; print only.
