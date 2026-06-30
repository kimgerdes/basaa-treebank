# Basaa gloss lexicon

`basaa_glosses.tsv` — a seed lexicon of **common Basaa words and their glosses**, for bootstrapping
interlinear glossing and the treebank. Tab-separated; columns:

| column | meaning |
|---|---|
| `form` | Basaa form (tone-marked where the source has it; toneless otherwise). `-` marks affixes. |
| `pos` | Universal POS (UPOS) tag |
| `gloss` | Leipzig-style morpheme gloss (the label used in interlinear tier 2) |
| `english` / `french` | free-translation equivalents (the "translated" tier) |
| `features` | UD morphological features (esp. `NounClass=Bantu<n>`) |
| `conf` | confidence: `high` (literature-attested) / `med` (corpus-inferred, plausible) |
| `source` | `lit` = scientific articles in `../docs/`; `freq` = `../corpora/opus/*.freq`; `NWS`/`IPA`/`2014` = specific source |

It is deliberately small (~90 entries) and honest about confidence — it is a **starting point**, not
a dictionary. Items marked `med` need checking against Njock (2019) / Lemb & de Gastines (1973).

## Why agreement markers dominate

The most frequent tokens in real Basaa text are **one-letter concord markers** — `i, u, ma, li, mi,
bi, hi, di, a, ba`. This is the signature of a Bantu noun-class language: every noun belongs to a
class, and that class is echoed by agreement on verbs, demonstratives, the connective, and modifiers.
Getting these right is 80% of glossing Basaa. The classes pair into singular/plural genders:

| sg | pl | typical semantics | example (this lexicon) |
|---|---|---|---|
| 1 `mu-` | 2 `ɓa-` | persons | *mut* 'person' / *bôt* 'people' |
| 3 `mu-` | 4 `mi-` | plants, misc. | *nson* 'work' / *minson* |
| 5 `li-` | 6 `ma-` | paired things, langs | *hop* 'language' / *mahop* |
| 7 `hi-` | 8 `bi-` | things | *buk* 'word' / *bibuk* 'words' |
| 9 `N-` | 10 `N-` | animals, abstracts | *kiñ* 'voice', *haŋga* 'sun', *ŋguy* 'strength' |
| 19 `hi-` | 13 `di-` | diminutives | *nuni* 'bird', *hikékét/dikékét* 'small piece(s)' |

(Class numbering follows the Bantu/Meinhof convention used by Hyman 2003 and Hamlaoui & Makasso.)

## Gloss abbreviations used

`SBJ` subject marker · `AGR` agreement/concord · `CLn` noun class n · `CONN` connective/associative
('of') · `COMP` complementizer · `NEG` negation · `PST/PRS/FUT` tense · `PROG` progressive ·
`IMP` imperative · `DEM` demonstrative · `AUX` auxiliary · `1SG/2SG/1PL…` person-number.

These follow the **Leipzig Glossing Rules** and the abbreviation key in the Hamlaoui & Makasso
"Pronominal F-markers" paper (FUT2, GEN, INF, LOC, OBL, PASS, PRS, class numerals).

## A note on tone

Tone is **lexical and grammatical** in Basaa. The same segmental string can differ only in tone and
mean different tenses — e.g. (Adda et al. 2022) *M̀È nlÒ yani* 'I'll come tomorrow' vs *M̀È ǹlÔ yani*
'I came yesterday'. Where a form here is given toneless (from Common Voice / GRN text), its TAM gloss
is provisional until tone is restored. See `../TREEBANK_PLAN.md` §3B.
