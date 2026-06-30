# Flags — contradictions & open questions

Conflicts found **between the sources**, **between the project's own files**, or **between a project file
and a source**, while extracting the rules in this folder. Each flag says what conflicts, why it matters,
and a recommended resolution. Resolve before scaling annotation. Severity: 🔴 blocks correct TAM/syntax ·
🟠 affects glossing consistency · 🟡 cosmetic/metadata.

---

## FLAG-1 🔴 — Which canonical orthography? IPA vs AGLC vs practical
**Sources: Makasso & Lee 2015; Nikitin et al. 2022; the corpus text itself**

- **Makasso & Lee 2015 deliberately give *no* orthographic spellings** ("there is no consensus about the
  writing system of Basaa … we decided not to provide spellings"), using **IPA only**.
- **Nikitin et al. 2022 treat the General Alphabet of Cameroon Languages (AGLC/ACALAN) as *the* official
  orthography** and build a model to convert missionary spellings *into* it.
- **Most running corpus text** (Common Voice, GRN) is in a **practical, largely toneless** Latin
  orthography that is **neither**.

**Why it matters:** the treebank's `form` field, the lemma index, and any tone-restoration step all
depend on a single canonical layer. **Recommendation:** adopt the **tone-marked AGLC/Hyman layer** as
canonical (consistent with `../TREEBANK_PLAN.md` §3B), store source spellings in `MISC Orig=`, and use
Nikitin et al.'s model to lift toneless text. Applies to TR-1, TR-2.

---

## FLAG-2 🔴 — The TAM nasal's tone is described three different ways
**Sources: Makasso & Lee 2015 (Syllabic nasals **and** Tone); Hamlaoui et al. 2014 (7)**

Three statements that do not align:

1. *"Syllabic nasals are assigned an L tone."* (Makasso & Lee 2015, Syllabic nasals — a general/phonetic
   default.)
2. *"The present tense is marked with a nasal **H** and a floating L tone."* (Makasso & Lee 2015, Tone.)
3. *The Past1 `{-n-}` is underlyingly **toneless** and surfaces L after a L subject marker, H after a H
   subject marker — its tone is copied via HTS, not by tense.* (Hamlaoui et al. 2014, ex. 7.)

**Why it matters:** an earlier project draft claimed "**H-nasal = present, L-nasal = past**." That is
**not supported** — the nasal's tone tracks the subject marker (HTS) and/or a floating melody, not tense
directly. **Resolution:** glossing rule **GL-4** — derive tense from translation + verified melody,
record nasal tone only as an observation. **Note:** the present-tense **downstep** (statement 2) *is* a
usable supporting cue (TR-9).

### FLAG-2b 🔴 — Internal contradiction the project must fix
[`../treebank/syntactic_analysis.md`](../treebank/syntactic_analysis.md) §6–10 still asserts
*"**tone = tense**, H present vs L past"* (around line 123). This **contradicts the correction** already
applied in [`../glossary/transcription_and_gloss_review.md`](../glossary/transcription_and_gloss_review.md)
§4 and [`../glossary/morphology_child_paradigm.md`](../glossary/morphology_child_paradigm.md). **Action:**
edit `syntactic_analysis.md` §6–10 to remove the "tone = tense" claim and point to GL-4 / FLAG-2.

---

## FLAG-3 🟠 — Is `í` in `ŋ́-kɛ̀ í ɓòm` 'go to market' an augment or a locative? — **RESOLVED: locative**
**Sources: Hamlaoui et al. 2014 (16); the project's own files disagreed**

- `../glossary/transcription_and_gloss_review.md` §5 floated `í` = **augment** (cf. ex. 16
  `í ndáp` `AUG 9.house`) → dependent of *market*.
- `../glossary/morphology_child_paradigm.md` (s06) and `../treebank/syntactic_analysis.md` §6–10 treat
  `í` as a **locative/allative particle** → head of *market*, `comp:obl` of 'go'.

**Why it matters:** changes the gloss (`AUG` vs `LOC`) **and** the tree (det-dependent vs prepositional
head). **Decision (this pass): keep `LOC`** — `í` is the locative head (`ADP`, `comp:obl`), uniformly
across all files. The augment reading is recorded but set aside **pending audio verification with
Makasso**. See GL-6, PA-6.

---

## FLAG-4 🟠 — Subject marker glossed `1.SBJ` in one place, `1.AGR` in another
**Source: `../glossary/basaa_glosses.tsv` vs Hamlaoui et al. 2014**

The lexicon glosses the standalone word `a` as **`1.SBJ`** but the prefix `a-` as **`1.AGR`**. The house
style (GL-2) is **`1.AGR` for both**. **Action:** change the `a = 1.SBJ` row to `1.AGR` (and any `*.SBJ`
to `*.AGR`) so the gloss tier is internally consistent.

---

## FLAG-5 🟠 — `hi-` is class 19, not "CL7/19"; class 7 prefix is Ø
**Sources: Janssens 1986 §1.4; Makasso & Lee 2015 vs `../glossary/`**

`../glossary/basaa_glosses.tsv` and `../glossary/README.md` give `hi-` as `CL7/19` and list classes 7 and
19 both as `hi-`. But **Janssens 1986 §1.4** states the **class-7 prefix is Ø (zero) before all
consonants** (`y-`/Ø before vowels), while **class 19 is `hi-`** (sg of the 19/13 diminutive gender,
e.g. `hi-nùní`→`rìnùní` 'bird'). **Action:** in the lexicon, assign `hi-` to **class 19** and mark
class 7 as **Ø-prefix**; keep the 19/13 pairing. (Low risk, but it mislabels diminutives.)

---

## FLAG-6 🟠 — The `-ak` imperative is contradicted by its own cited source
**Source: Makasso & Lee 2015 (Phonotactics, fn 4) vs `../glossary/basaa_glosses.tsv`**

The lexicon lists `-ak SUFF IMP` (source `lit`). But **Makasso & Lee 2015 fn 4 explicitly reject it**:
Greenberg's `-ak` imperative was checked and "there is no such imperative form in Basaa." Their
imperatives take a **`-V́χ` suffix with H tone** (`sɔ́mb-ɔ́χ` 'Buy!', `salꜜgá` 'Work!'). **Action:**
remove/re-flag the `-ak` entry; gloss attested imperatives with the `-V́χ` pattern. See GL-11.

---

## FLAG-7 🟡 — Consonant count: 22 vs 30
**Sources: Hyman 2003 / Janssens 1986 / Hamlaoui 2020 (22) vs Nikitin et al. 2022 (30)**

Hamlaoui 2020 and Janssens cite **22 consonants**; Nikitin et al. 2022 say **30**. This is a
**counting-convention** difference (whether prenasalised stops, labialised velars, and lenition
allophones are counted as separate phonemes), not a real disagreement about the inventory. Use the
**phonemic 22** for the lexicon; treat the extra surface units as allophones (TR-5). No action beyond a
note.

---

## FLAG-8 🟡 — `docs/Adda-etal_2022_…pdf` is misnamed
**Source: the PDF itself (arXiv 2210.06986)**

The tone-prediction paper is authored by **Ilya Nikitin, Brian O'Connor & Anastasia Safonova (2022)**;
**Gilles Adda is *cited* (via BULBasaa) but is not an author.** The filename and `../docs/SOURCES.md`
row imply Adda authorship. **Action:** cite it as **Nikitin, O'Connor & Safonova 2022** (optionally
rename the file); update `../docs/SOURCES.md`.

---

## Summary table

| Flag | Sev | One-line | Where to fix |
|---|---|---|---|
| FLAG-1 | 🔴 | Canonical orthography undecided (IPA / AGLC / practical) | `TREEBANK_PLAN.md`, TR-1 |
| FLAG-2 | 🔴 | Nasal tone ≠ tense (3 conflicting source statements) | GL-4; **edit `syntactic_analysis.md` §6–10** |
| FLAG-3 | 🟠 | `í` 'to market' = augment or locative? — **resolved: locative** (audio TBD) | applied across treebank |
| FLAG-4 | 🟠 | `1.SBJ` vs `1.AGR` inconsistency | `basaa_glosses.tsv` |
| FLAG-5 | 🟠 | `hi-` is cl.19, cl.7 prefix is Ø | `basaa_glosses.tsv`, glossary README |
| FLAG-6 | 🟠 | `-ak` imperative rejected by source | `basaa_glosses.tsv` |
| FLAG-7 | 🟡 | 22 vs 30 consonants (counting) | note only |
| FLAG-8 | 🟡 | Tone-prediction paper misattributed to Adda | filename, `SOURCES.md` |
