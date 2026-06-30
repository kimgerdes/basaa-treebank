# Stage 2 — Glossing rules

Apply these when adding the **morpheme gloss tier** (`MISC Gloss=` on each token) and UD features.
The goal is glosses **in Hamlaoui & Makasso's house style**, so the treebank reads like their examples
and can be checked against them. House style = Leipzig Glossing Rules + the conventions below.

Reference glosses to imitate (Hamlaoui, Gjersøe & Makasso 2014):

```
sógól           à-ǹ-téhé        á-ɓóóngé
1.grandfather   1.AGR-PST-see    2-children          'The grandfather saw the children.'   (ex. 7a/21)

bì-kwémbé       bí        á-ɓóóngé
8-boxes         8.CONN    2-children                 "The children's boxes."               (ex. 10)
```

---

## GL-1 — Class prefix on a noun → `n-stem` (class number + hyphen + stem gloss)
**Confidence: high · Source: Hamlaoui et al. 2014 (10, 11, 15…)**

Gloss an overt noun-class prefix as the **Bantu/Meinhof class number**: `2-children`, `1-child`,
`8-boxes`, `4-sheep`, `6-doughnuts`, `9.house`. Put the class on a UD feature too:
`NounClass=Bantu<n>`. Use the **augment-less class numbers**, not glosses like `CL1.child`.

> ⚠️ The project's `../glossary/` once used `CL1.child`; the house style is `1-child`. Already corrected
> in `../glossary/transcription_and_gloss_review.md`; keep new glosses in the `n-stem` form.

---

## GL-2 — Subject concord on the verb → `n.AGR`, never `SBJ`
**Confidence: high · Source: Hamlaoui et al. 2014 (7, 21, 22)**

The preverbal subject marker is **agreement/concord**, glossed `1.AGR`, `2.AGR`, `9.AGR` … by class.
It appears verb-bound (`à-ǹ-téhé` = `1.AGR-PST-see`) and, with a class-2 subject, becomes `áá-`
(`á-ór áá-ń-téhé` = `2-people 2.AGR-PST-see`). The **concord vowel's class = the subject's class**.

> ⚠️ **FLAG-4:** `../glossary/basaa_glosses.tsv` still glosses the standalone word `a` as `1.SBJ` while
> the prefix `a-` is `1.AGR`. Use **`1.AGR` everywhere** for consistency with the source.

---

## GL-3 — The homorganic nasal: gloss by host POS (class prefix on N, tense on V)
**Confidence: high · Source: Makasso & Lee 2015 (Syllabic nasals); Hamlaoui et al. 2014**

The *same* syllabic nasal (TR-3) is a **noun-class prefix** on nouns and a **tense morpheme** on verbs.
Disambiguate by the host's POS:

- on a **NOUN** → `CL<n>-` / `<n>-stem` (e.g. `m̀-pek` = `3-bag`).
- on a **VERB** → a tense gloss `PST` / `PRS` (e.g. `ǹ-sɔ́mb` = `PST-buy`, `ń-ʤɛ́` = `PRS-eat`).

A segmenter must therefore know POS before it labels the nasal.

---

## GL-4 — Do **not** read tense off the nasal's tone
**Confidence: flag · Source: Makasso & Lee 2015; Hamlaoui et al. 2014 (7)**

Assign `Tense=`/`Aspect=` from **translation + verified tone/segmental melody**, *not* from "H-nasal =
present, L-nasal = past." The sources give three non-aligned statements about the nasal's tone
(**FLAG-2**): syllabic nasals default to L (Makasso & Lee); present nasal is H + floating L (Makasso &
Lee, TR-9); the Past1 `{-n-}` is underlyingly toneless and copies the subject marker's tone via HTS
(Hamlaoui et al. 2014 ex. 7). Gloss tense from meaning; record the heard nasal tone only as an
observation (`MISC NasalTone=…(obs)`).

---

## GL-5 — Connective → `n.CONN`, agreeing with the **preceding** noun (NP1)
**Confidence: high · Source: Hamlaoui et al. 2014 §2.1 (10, 11)**

The connective ('of', and most modification) links **NP1 CONN NP2** and **agrees with NP1**:
`bì-kwémbé bí á-ɓóóngé` = `8-boxes 8.CONN 2-children`; `N-gwɔ́ ì m-ààngé` = `9-dog 9.CONN 1-child`
'the child's dog'. **Gloss the connective with NP1's class** + `.CONN`. (Attachment is a Stage-3
matter — see PA-3.)

---

## GL-6 — Pre-nominal vowel → `AUG` (augment)
**Confidence: high · Source: Hamlaoui et al. 2014 (16)**

A pre-nominal vowel before a noun is the **augment**, glossed `AUG`: `í ꜜndáp ì-ní` = `AUG 9.house 9-DEM`
'this house'. **FLAG-3 — RESOLVED:** the `í` in `ŋ́-kɛ̀ í ɓòm` 'going to market' is glossed **`LOC`** (a
locative particle, head of *market*), **not** `AUG`; the augment reading is set aside pending audio
verification (see `contradictions.md` FLAG-3). Use `AUG` for clear pre-nominal augments like ex. 16.

---

## GL-7 — Demonstratives, possessives, independent & object pronouns
**Confidence: high · Source: Hamlaoui et al. 2014 (12,13,16,17,19,35–38)**

| Element | Gloss | Example |
|---|---|---|
| demonstrative | `n-DEM` / `n.DEM` | `ì-ní` `9-DEM` 'this'; `míí` `4.DEM` 'that' |
| possessive | `n-POSS` | `gw-éé bí-támb` `8-POSS 8-shoes` 'her shoes' |
| independent pronoun | `n.PRO` | `ñɛ́` `1.PRO` 'he/she'; `áɓó` `2.PRO` 'them' |
| **object** pronoun | `n.PRO` (a real argument) | `…à-ǹ-tí áɓó mà-kàlà` `1.AGR-PST-give 2.PRO 6-doughnuts` |

**Object pronouns are genuine pronouns, not object-agreement markers** (Hamlaoui et al. 2014 fn 6) — so
gloss them as the argument they are (contrast the **subject** marker, which *is* agreement, GL-2).

---

## GL-8 — Adjectives are mostly adjectival nouns linked by a connective
**Confidence: high · Source: Hamlaoui et al. 2014 §2.2 (14, 15); Hyman, Jenks & Makasso 2013**

Most "adjectives" are **adjectival nouns** and modify via a **connective construction** (gloss like a
possessive): `áà-lám áá á-ɓóóngé` = `2-beautiful 2.CONN 2-children` 'beautiful children'. A smaller set
of **true adjectives** are **post-nominal and agree** directly: `mìn-tómbá mìn-kéní` = `4-sheep 4-big`
'big sheep'. **Rule:** if a modifier is linked by a CONN-like element, gloss/parse it as a connective
construction; only the bare post-nominal agreeing kind is a "true" adjective.

---

## GL-9 — Verbal derivation: gloss the extension, keep the base lemma
**Confidence: med · Source: Makasso & Lee 2015 (Vowel raising); Voorhoeve 1980 (cited)**

Verbal extensions (causative, applicative…) attach to the root and **trigger vowel-raising of the stem**
(TR-6). Gloss the extension morpheme (e.g. `-Vl` `APPL`, causative `CAUS`) and keep `LEMMA` = the
**un-raised base verb**. E.g. `sel-êl` 'work with' → `LEMMA=sal`, `Gloss=work-APPL`.

---

## GL-10 — Class 15 (infinitive) has **no prefix** in Basaa; plural in class 6
**Confidence: high · Source: Janssens 1986 §1.4 (kùù/màkùù; an, èè, ôk)**

The infinitive (class 15) **takes a Ø prefix even before vowels** (`an` 'to count', `èè` 'to cry',
`ôk` 'to curse'); its plural is in **class 6**. **Rule:** gloss an infinitive `INF` with no class
prefix; do not invent a `15-` prefix on the form.

---

## GL-11 — Imperative: the `-ak` suffix is **not** Basaa
**Confidence: flag · Source: Makasso & Lee 2015 (Phonotactics, fn 4)**

> Greenberg's reported imperative `-ak` ("Wish!" `[tam-aŋ]`) — "Our speaker confirmed that **there is no
> such imperative form in Basaa.**"

Imperatives in Makasso & Lee's own data take a **`-V́χ` suffix with H tone**: `sɔ́mb-ɔ́χ` 'Buy!',
`salꜜgá` 'Work!', `tıŋ-lá` 'Detach!'. ⚠️ **FLAG-6:** `../glossary/basaa_glosses.tsv` still lists
`-ak SUFF IMP` — that source-cited gloss is contradicted; re-check before using.

---

## GL-12 — Gloss-abbreviation inventory to adopt verbatim
**Confidence: med · Source: Hamlaoui & Makasso "Pronominal F-markers" key (still to obtain); usage in docs**

Use these labels (extend from the F-markers key once obtained — see `../docs/SOURCES.md`):

`AGR` concord/agreement · `AUG` augment · `CONN` connective · `DEM` demonstrative · `POSS` possessive ·
`PRO` (independent/object) pronoun · `PST` past · `PRS` present · `FUT2` future-2 · `INF` infinitive ·
`PASS` passive · `OBL` oblique · `GEN` genitive · `LOC` locative · `NEG` negation · `APPL` applicative ·
`CAUS` causative · `COMP`/quotative complementizer · class numerals `1,2,3,4,5,6,7,8,9,10,13,15,19`.

Genders (sg/pl pairings), per Janssens 1986 §1.4 and the project glossary:
**1/2, 3/4, 5/6, 7/8, 9/10, 19/13**, plus **15 (infinitive) → 6**. ⚠️ Class-7 prefix is **Ø**, class-19
is **hi-**; do not conflate them (**FLAG-5**).
