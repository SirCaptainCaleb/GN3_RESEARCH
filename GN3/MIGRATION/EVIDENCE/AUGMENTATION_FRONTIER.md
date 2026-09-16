# GN3 augmentation frontier

This note records research directions and migration correspondence that are intentionally excluded from the canonical proof spine. The canonical proof currently ends with Proposition 6.2 of `GN3/PROOF_SPINE/TWO_TIGHT_PATHS.md`.

## 1. Exact missing augmentation statement

Let `H` be a smallest counterexample and let `F` be a spanning three-path cover for which no endpoint transfer from one component to a component of at least equal order is possible. Write

`lambda(F)=(ell_1,ell_2,ell_3)`, `ell_1>=ell_2>=ell_3`,

for the component orders in decreasing order.

A sufficient next lemma would be:

> Either `H` has a spanning two-path cover, or there is a spanning three-path cover `F'` with `lambda(F')` lexicographically larger than `lambda(F)`.

For the lexicographically maximal cover chosen in Section 6 of the proof spine, this statement would give a contradiction. It is weaker than requiring the largest component to increase at every step, because it permits the largest order to remain fixed while the second component increases.

## 2. Why the proved local statements do not yet give the augmentation

The current proof supplies explicit local tight paths and crossing triples, but not yet the required replacement spanning cover.

- A three-vertex contact from the fixed-pair or deletion arguments specifies actual ordered edges and a tight triple, but it does not by itself enlarge the longest component or improve the sorted component-order triple.
- Completing a newly found proper path by the complement lemma can discard the former long component; endpoint improvement controls the new cover only after that completion.
- The fixed-pair section now supplies two distinct layers. Theorem 4.2 gives static restriction facts at every vertex outside the fixed pair. Theorem 4.5 additionally gives one lawful continuation on which all but at most one such vertex actually undergo both historical source reductions. Theorem 4.8 then localizes any later two-vertex return through a historically reduced vertex: a new endpoint outside the fixed pair forces a larger path or an explicit reversed/crossing triple (with the general contact lemma also allowing a proper cycle), leaving only the two old fixed-pair supports as exact recurrence residues. None of these conclusions by itself constructs a spanning replacement cover.

Any proposed replacement `F'` must explicitly specify every retained subpath, every inserted ordinary edge, every tight triple required at a join, pairwise vertex-disjointness of the resulting components, and the disposition of every vertex of `H`.

The component formula

`comp(F-S)=comp(F)+sum_{v in S}(deg_F(v)-1)-e_F(S)`

is useful for checking these constructions. For example, deleting one internal vertex from an exact two-path cover creates three path components. Adding a separate three-vertex path on that deleted vertex and a fixed pair therefore creates four components unless additional joins are proved. A crossing edge and its associated tight triple cannot be counted as those missing joins without an explicit splice.

## 3. Most promising current data

For the lexicographically maximal cover `A|B|C`, choose a nontrivial component `X_0=(x_0,...,x_m)` outside `A` and put `a=x_0`, `c=x_m`. Proposition 6.2 gives

`(a,v_{ell-1},v_{ell-2})`, `(v_1,v_0,c)`

at the two ends of `A`. Theorem 4.2 gives both static fixed-pair restrictions at each of the four end vertices

`v_{ell-1}, v_{ell-2}, v_1, v_0`,

for this same fixed pair `a,c`. Theorem 4.5 gives a lawful continuation for this pair on which at least three of those four vertices have both historical source reductions. Proposition 4.7 gives the explicit static three-vertex contact alternatives, and Theorem 4.8 converts any later new-endpoint return through one of the historically reduced vertices into recurrence-localized geometry. Proposition 5.2 gives a separate deletion-crossing mechanism with exact adjacent edges from two compared covers.

The next target is to combine one of these data sets into a literal spanning two-path cover or a literal lexicographically improved three-path cover.

## 4. Historical endpoint-selection machinery

The immediately preceding audited GN3 fixed-pair branch did define lawful continuations by explicit endpoint-selection and singleton-replacement operations, with a strict distinction between current path components and older extended paths or restriction facts retained for later use. The first streamlined single-document reauthoring intentionally omitted that continuation layer and kept only the static extended-path restrictions. That omission lost mathematical strength: the static facts alone do not certify that a singleton reduction was actually reached along a legal continuation before a later return through the same vertex.

The canonical proof spine now restores the minimal continuation structure needed for that distinction. Section 4 states the two accepted operations precisely, defines lawful finite continuations as sequences generated only by those operations (together with non-changing restriction-recording steps), proves the simultaneous all-but-one historical reduction theorem, and isolates the exact recurrence residue to the old supports `{a,s}` and `{s,c}`. The broader legacy payment/capture ontology remains outside the canonical exposition unless a future theorem requires additional information not present in this restored interface.

## 5. Reauthoring correspondence

The single-document spine was reauthored from the earlier GN3 proof files after commit `9ae9f366b69ebb3d394a57708e76bfd4ce77e9cf`. The main correspondence is:

| Earlier material | Current location or disposition |
| --- | --- |
| minimal counterexample, complement and pair deletion | Section 1 |
| small-order local lemmas and order `>10` | Section 2, now proved internally |
| terminal longest path and endpoint transfers | Section 3 |
| fixed-pair restrictions and lawful continuation/history | Section 4: static restrictions in Theorem 4.2; lawful all-but-one historical reductions in Theorem 4.5; recurrence localization in Theorem 4.8 |
| four same-orientation vertices | Lemma 4.9 |
| deletion component formula and crossing | Section 5 |
| three same-orientation internal vertices and eight induced subgraphs | Propositions 5.3–5.4 |
| lexicographic extremal choice, fixed-pair end data, and recurrence control | Section 6 |
| order-sensitive path intersection arguments | Appendix A |
| proposed augmentation lemma and reasons it is still missing | this note |

This note is research context, not part of the proof.