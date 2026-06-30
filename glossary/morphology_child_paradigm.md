# Morphological analysis — the *maàŋgɛ́* ('child') sentence paradigm

Word-by-word morphological analysis of the 10 aligned sentences in
`../recordings/aligned/` (manifest: `../recordings/aligned/manifest.tsv`; source: Makasso & Lee
2015). They share one frame, so they isolate Basaa verb and noun morphology cleanly.

> IPA is OCR-recovered from `../docs/basaa.pdf` and **must be verified against the audio + PDF**
> (esp. tone). The *analysis* (morpheme boundaries, features) is robust; some segmental/tone details
> are provisional.

## The shared frame

```
maàŋgɛ́            á-{m̀,ǹ,ŋ̀}-STEM          (OBJ)
m-aàŋgɛ́           a-     N-      V          …
1-child           1.AGR- TENSE-  verb       object
'the child'       (concord a- is bound onto the verb; NounClass=Bantu1)
```

> **Tokenisation note.** The preverbal concord `a-`/`hí-` is treated as **bound verb morphology** (a
> prefix; `NounClass=` on the verb), not a separate token — the agreed policy (`../rules/parsing.md`
> PA-2 option b). Glossed `1.AGR` (Hamlaoui & Makasso house style), **not** `1.SBJ`.

Three morphological systems are visible in this one frame:

### 1. Noun class + concord
- **maàŋgɛ́** 'child' is class 1 (the human singular class). Its class is not marked by an overt
  prefix here (`ma-` is lexicalized), but it **controls agreement**: the subject marker on the verb is
  the class-1 concord **á**. Change the subject's class and this vowel changes (cf. `á`/`áá` for cl.1/2
  in `../treebank/`). The concord, not word order alone, is what identifies the subject.

### 2. The homorganic nasal **tense prefix** (place assimilation)
Basaa marks tense with a **syllabic nasal prefixed to the verb stem**, and that nasal **assimilates in
place of articulation to the stem-initial consonant** (Makasso & Lee 2015: "syllabic nasals … as tense
morphemes"):

| nasal | appears before | example | stem |
|---|---|---|---|
| **m̀-/ḿ-** (bilabial) | p, ɓ | *m̀-pɔ́ɾɔ́* 'speak', *m̀-ɓíː* 'take' | pɔ́ɾɔ́, ɓíː |
| **ǹ-/ń-** (alveolar/palatal) | s, ʧ, ʤ, ɲ | *ǹ-sɔ́mb* 'buy', *ń-ʤɛ́* 'eat', *ǹ-ʧéʔ* 'die', *ǹ-ɲɔ́* 'drink' | sɔ́mb, ʤɛ́, ʧéʔ, ɲɔ́ |
| **ŋ̀-/ŋ́-** (velar) | k, vowel-initial | *ŋ́-kɛ̀* 'go', *ŋ̀-áŋ* 'read' | kɛ̀, áŋ |

This is the same syllabic-nasal that elsewhere is a **noun class prefix** (cl.1/cl.3: *m̀-pek*
'CL3-bag', *ŋ̀-kɔ̀ŋ* 'CL3-land') — so the segmenter must disambiguate **nasal = class-prefix** (on
nouns) vs **nasal = tense** (on verbs) by the host's POS.

### 3. Tense/aspect — and a caution about tone
The sentences contrast **present** ('speaks', 'eats', 'is going') with **perfect/recent-past** ('has
bought', 'has died', …). That much is clear from the translations. **How** the contrast is exponed is
**not** settled by this source, and an earlier draft over-claimed it:

> ⚠️ **Correction.** The illustration states *"syllabic nasals are assigned an L tone."* So the nasal is
> **not** straightforwardly H-for-present / L-for-past. The section is about *syllable structure* (the
> nasal is syllabic), not a tense paradigm. The observed nasal tone is recorded in the conllu as
> `NasalTone=…(obs)` — an **observation**, not an analysis. The real tense exponent (nasal tone vs.
> stem melody vs. a floating grammatical tone) must be checked against Hyman (2003), the BULB `basaa`
> morphology module, or Fatima directly. Full discussion: `transcription_and_gloss_review.md` §4.

What *is* robust: tone is lexically and grammatically active in Basaa, so a treebank that drops tone
risks mis-analyzing TAM (cf. `../TREEBANK_PLAN.md` §3B and Adda et al. 2022). The aligned audio now lets
each token's tone be checked by ear in Arborator.

## Per-sentence segmentation (interlinear)

(Concord `á-` is bound onto the verb; glossed `1.AGR`.)

```
s01  m-aàŋgɛ́       á-m̀-pɔ́ɾɔ́        ɓasáa
     1-child        1.AGR-PRS-speak   Basaa
     'the child speaks Basaa'

s03  m-aàŋgɛ́       á-ǹ-sɔ́mb         ma-kálà
     1-child        1.AGR-PST-buy     6-doughnut
     'the child has bought doughnuts'              ← object is class 6 (ma- plural)

s04  m-aàŋgɛ́       á-ń-ʤɛ́           ma-kálà
     1-child        1.AGR-PRS-eat     6-doughnut
     'the child eats doughnuts'                    ← s03/s04 contrast present vs perfect (exponent: see GL-4)

s06  m-aàŋgɛ́       á-ŋ́-kɛ̀          í        ɓòm
     1-child        1.AGR-PRS-go      LOC      market
     'the child is going to market'                ← í = locative head (comp:obl); see FLAG-3

s10  m-aàŋgɛ́       á-ŋ̀-áŋ           kâar
     1-child        1.AGR-PST-read    book
     'the child has read a book'                   ← ŋ̀- velar nasal before vowel-initial stem áŋ
```

(Full set in `../recordings/aligned/manifest.tsv`.)

## Feature bundle a morphological analyzer should output (UD-style)

For each finite verb token, e.g. *ǹ-sɔ́mb*:

```
FORM=ansɔmb  LEMMA=sɔmb  UPOS=VERB
FEATS = NounClass=Bantu1 (subj concord, bound á-) | Tense=Past | Aspect=Perf | VerbForm=Fin
MISC  = Morph=a-n-sɔmb | Gloss=1.AGR-PST-buy | NasalTone=L(obs)
```

These 10 sentences are enough to **seed and unit-test a Basaa morphological segmenter**: a finite-state
or neural model that, given an orthographic verb, returns `subject-concord + tense-nasal(+tone) + stem`
— the prerequisite called out in `../TREEBANK_PLAN.md` §3A.
