# NWS concord-fold — review checklist (for your ear)

When the preverbal subject-concord was folded into its verb (bound-morphology policy,
[`../rules/parsing.md`](../rules/parsing.md) PA-2), most cases were clean. The cases below need a
listen + judgement. Each is also flagged **inline** in the CoNLL-U via `MISC Flag=...` on the token, so
it shows in Arborator when you click it. Audio: the shared NWS file
`https://elizia.net/basaa/bas_NWS_north_wind_and_sun.mp3`, seek to the offset given.

The fold spec lives in [`align_nws.py`](align_nws.py) (`FOLDS`), so fixes belong **there** (re-running the
script regenerates all three files); editing the `.conllu` directly will be overwritten on the next run.

## Cases to confirm

| sent | token | seek (ms) | issue |
|---|---|---|---|
| bas_nws01 | `baba` | 6823 | concord `2.AGR` folded onto the **auxiliary** `ba` (be), not the main verb `pehmba`. Is the SM on the aux (likely) or should it bind the lexical verb? |
| bas_nws05 | `agwee` | 24211 | the draft attached `a` to the root `lo`; refolded onto `gwee` 'have' (the verb it actually marks, in the relative 'which has…'). Confirm host. |
| bas_nws06 | `ibela` | 28612 | `i` was glossed `it`; treated as a class-9 concord on `bela` 'be.able'. Confirm it's a subject marker, not a pronoun/expletive argument. |
| bas_nws07 | `ibe` | 30793 | `i`(it) folded onto the **auxiliary** `be`; this whole clause's parse is rough (see corrections below). Re-transcribe + reparse. |
| bas_nws08 | `iwaa` | 38157 | `i` (glossed `it`) treated as a concord on `waa` 'stop'. Confirm. |

## Policy point to confirm — pronominal subjects were NOT folded

Where the preverbal `a`/`jo`/`ba` is the **sole** expression of the subject (no lexical subject NP), the
draft glossed it as a pronoun (`he`/`him`/`they`/`it`/`the.one`) and it was **left as a separate `subj`/
`dep` token**, not folded:

- `bas_nws03` tok `a` 'he'; `bas_nws04` tok `ba` 'they', tok `a` 'he'; `bas_nws07` tok `jo` 'him';
  `bas_nws11` tok `jo` 'it' (post-verbal — an **object** pronoun, not a subject marker).

Decision needed: under strict bound-morphology these pronominal subjects would also be verb prefixes
(pro-drop, `NounClass` on the verb). Keeping them as tokens is the alternative. They're consistent with
PA-8 (object pronouns are genuine arguments) for the post-verbal ones; the **pre-verbal** ones are the
open question.

## Corrections already applied (verify they match the audio)

- **bas_nws07** `jah` 'also' had a head **self-loop** (head = itself) → repointed to the verb `hongoh`.
  The clause is still a rough parse; reparse by ear.
- **bas_nws09** `ni` and `nguy` pointed at **each other** (a cycle) → `ni` 'with' now heads `nguy`
  'strength' and attaches to `baj` 'shine' as `mod` (matching the curated sample's NWS-sun analysis).

## Also worth a pass (not concord-related)

- The NWS files still carry a few **UD-style relations** (`aux`, `case`) mixed into SUD trees. For pure
  SUD, the auxiliary (`ba`/`be`) and the adposition (`ni`) should be heads. Clean up when reparsing.
- `bas_nws11` tok `jo` 'it' is `dep`; as a post-verbal object pronoun it's likely `comp:obj`.
