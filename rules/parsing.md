# Stage 3 — Parsing (dependency attachment) rules

Apply these when attaching **dependencies** (SUD primarily; UD mapping noted). The treebank uses **SUD**
(function words are heads) — see [`../treebank/syntactic_analysis.md`](../treebank/syntactic_analysis.md).
Every rule below is grounded in a glossed example from the literature.

---

## PA-1 — Basic order is SVO; the lexical verb is the root
**Confidence: high · Source: Hamlaoui et al. 2014 (20, 21)**

`[TP [NP mùr] [T à-ń-sèbél [VP <sèbél> [NP m-áángé]]]]` — subject, verb, object. Attach `subj` and
`comp:obj` (UD `nsubj`/`obj`) to the inflected verb as root.

---

## PA-2 — The subject is identified by **concord**, not by word order
**Confidence: high · Source: Hamlaoui et al. 2014 (1–2, 7)**

The preverbal agreement vowel matches the subject's noun class (cl.1 → `à-`, cl.2 → `áá-`). When a
lexical subject NP and its concord co-occur, **the concord doubles the subject**. Two questions follow:

- **Treatment of the preverbal concord (`a`, `hí`): RESOLVED — option (b).** It is **bound verb
  morphology**: written as the verb prefix `a-`/`hi-` with `NounClass=Bantu<n>` on the verb, **no
  separate token**. (Rejected: (a) separate `dep` token; (c) `subj` + `dislocated` NP.) Applied across
  `../treebank/*.conllu`; the spaced practical spelling is kept in `# text_practical`, and in the audio
  file the verb's `AlignBegin` spans back over the concord's slice.
- Agreement, not position, is the surface diagnostic for subjecthood — rely on it.

---

## PA-3 — Connective construction: head-initial ConnP (possessor, modifier, relative — all one pattern)
**Confidence: high · Source: Hamlaoui et al. 2014 §2.1 (10)**

Their own constituency: `[ConnP [NP bì-kwémbé] [Conn bí [NP á-ɓóóngé]]]` 'the children's boxes'.

```
SUD:  bì-kwémbé (root) ──mod──▶ bí (CONN) ──comp:obj──▶ á-ɓóóngé
UD:   bì-kwémbé (root) ──nmod:poss──▶ á-ɓóóngé ;  bí = case
```

- **SUD makes the connective `bí` the head of NP2**, and the whole linker phrase attaches to NP1 as
  `mod`. This is the project's chosen analysis and **mirrors Hamlaoui et al.'s ConnP** — solid ground.
- The connective agrees with **NP1** (GL-5). This **one pattern covers possessives, qualification,
  classification, adjectival-noun modification, and relatives** — keep it uniform.

---

## PA-4 — Adjective attachment: connective vs. true post-nominal adjective
**Confidence: high · Source: Hamlaoui et al. 2014 §2.2 (14, 15)**

- **Adjectival noun + connective** (the common case) → parse exactly like PA-3 (CONN heads, attaches
  as `mod`): `áà-lám áá á-ɓóóngé` 'beautiful children'.
- **True post-nominal adjective** (agrees, no connective) → adjoined to the noun: `mìn-tómbá mìn-kéní`
  '4-sheep 4-big'. Attach as `mod` (UD `amod`) directly on the noun.

---

## PA-5 — Demonstratives adjoin to the noun; either side; no special head
**Confidence: high · Source: Hamlaoui et al. 2014 §2.3 (16, 17); Jenks, Makasso & Hyman**

Demonstratives are adjoined to a functional projection over the noun and **may precede or follow** it
(`í ꜜndáp ì-ní` 'this house'; `míí mɔ̀ní` 'that money'). Attach as `det`/`mod` on the noun, position
permitting.

---

## PA-6 — Augment: a det-like dependent of its noun
**Confidence: med · Source: Hamlaoui et al. 2014 (16)**

The pre-nominal augment (`í ndáp` `AUG 9.house`) attaches **as a det-like dependent of the noun**
(not as a clause-level head). **FLAG-3 — RESOLVED:** the `í` in `ŋ́-kɛ̀ í ɓòm` 'go to market' is kept as a
**locative preposition** (head of *market*, `comp:obl` of the verb), **not** the augment. The augment
reading is recorded but set aside pending audio verification with Makasso (see `contradictions.md` FLAG-3).

---

## PA-7 — Ditransitives are asymmetric: V — Recipient — Theme
**Confidence: high · Source: Hamlaoui et al. 2014 §3.2 (34–38), fn 6**

`sógól à-ǹ-tí á-ɓóóngé mà-kàlà` `1.grandfather 1.AGR-PST-give 2-children 6-doughnuts`
'the grandfather gave the children doughnuts'. The **recipient is closer to the verb** than the theme.
Attach recipient as `iobj` (UD) / `comp:obj` and theme as the second object. Order holds under
pronominalisation (`…tí áɓó mà-kàlà` 'gave them doughnuts').

---

## PA-8 — Postverbal pronouns are arguments, not agreement
**Confidence: high · Source: Hamlaoui et al. 2014 fn 6**

"Basaá has genuine object pronouns rather than object agreement markers." A postverbal pronoun fills
the object slot — attach it as `comp:obj`/`obj` (or `iobj`), **not** as a clitic/agreement on the verb.
(Contrast the *subject* concord, PA-2, which *is* agreement.)

---

## PA-9 — Wh-words stay in situ and cliticise to the verb
**Confidence: high · Source: Hamlaoui et al. 2014 §3 (39–41), Discussion**

Wh-pronouns — `nɟɛ́ɛ́` 'who', `kíí` 'what', `láá` 'how', `hɛ́ɛ́` 'where' — appear **in their canonical
postverbal position** (no wh-movement) and **form a prosodic word with the verb** (V-wh clitic; vowel
long phrase-finally, short medially). Attach the wh-word **low, next to the verb** in its argument/adjunct
slot; do not raise it to a clause-initial position.

---

## PA-10 — Focus is in situ; no inversion; apparent ex-situ focus keeps the grammatical subject
**Confidence: med · Source: Hamlaoui et al. 2014 Discussion; Hamlaoui & Makasso 2015 (to obtain)**

There is **no dedicated postverbal focus position** (no IAV focus position): focused phrases surface in
their **canonical position** with no change to phrasing. Hamlaoui & Makasso 2015 further argue **apparent
ex-situ focus keeps the subject as the grammatical subject** and that inversion structures are
unavailable. **Rule:** a fronted/focused constituent attaches **high as `dislocated`** while the
canonical `subj` relation is preserved — it does **not** become the subject. ⚠️ Confirm against
Hamlaoui & Makasso 2015 before annotating focus at scale (it is not yet in `../docs/`).

---

## PA-11 — Use High Tone Spreading as a constituency cue — with one hard caveat
**Confidence: high · Source: Hamlaoui et al. 2014 (whole paper)**

HTS (a H spreading rightward) is **blocked at the right edge of a syntactic XP / phonological phrase**.
When tone is marked, HTS tells you where phrase edges are:

| Boundary | HTS applies? | Constituency reading |
|---|---|---|
| Subject — Verb | **no** | subject is its own φ → separate constituent: `(S)φ (V O)φ` |
| Verb — first complement/adjunct | **yes** | they phrase together (binary φ) |
| between O1 and O2 (ditransitive) | **no** | the two objects do **not** phrase together |
| Noun — true adjective | **no** | the connective/φ edge blocks it (PA-4) |
| Verb — wh-pronoun | **yes** | wh is a clitic on the verb (PA-9) |

⚠️ **Hard caveat:** in the postverbal domain the **complement/adjunct distinction is prosodically
neutralised** — the first phrase after the verb phrases with it *whether it is an argument or an
adjunct*. So **HTS cannot decide `comp:obj` vs `mod`**; use it only for **edge detection**, and decide
argument-hood from valency/meaning.

---

## PA-12 — Phasal/inceptive verbs are full verbs, not auxiliaries
**Confidence: high · Source: Makasso & Lee 2015 (NWS: ɓoroo ɓaj); `../treebank/` open decision #3**

`ɓoroo` 'begin' inflects for tense and concord like a main verb, so keep it as the **head** with its
verbal complement as `comp:obj` (UD `xcomp`): `haŋga hí ɓoroo ɓaj ni ŋguy` 'the sun began to shine
with strength'. Do **not** demote it to an auxiliary.

---

## PA-13 — Copula is the head in SUD
**Confidence: med · Source: Common Voice example in `../treebank/syntactic_analysis.md` §4**

`Bés bo njé?` 'Who are we?' → SUD root = copula `bo`; `Bés` = `subj`, predicate `njé` = `comp:pred`.
(UD inverts: predicate `njé` is root, `bo` is `cop`.) Apply consistently for identificational/predicative
clauses.
