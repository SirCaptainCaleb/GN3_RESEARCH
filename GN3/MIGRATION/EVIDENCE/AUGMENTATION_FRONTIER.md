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
- The fixed-pair restrictions are static graph-theoretic tuples specifying the original extended path, intersecting singleton, surviving singleton, extension vertex, and side. Their existence does not prohibit the same source paths from appearing again in later constructions.

Any proposed replacement `F'` must explicitly specify every retained subpath, every inserted ordinary edge, every tight triple required at a join, pairwise vertex-disjointness of the resulting components, and the disposition of every vertex of `H`.

The component formula

`comp(F-S)=comp(F)+sum_{v in S}(deg_F(v)-1)-e_F(S)`

is useful for checking these constructions. For example, deleting one internal vertex from an exact two-path cover creates three path components. Adding a separate three-vertex path on that deleted vertex and a fixed pair therefore creates four components unless additional joins are proved. A crossing edge and its associated tight triple cannot be counted as those missing joins without an explicit splice.

## 3. Most promising current data

For the lexicographically maximal cover `A|B|C`, choose a nontrivial component `X_0=(x_0,...,x_m)` outside `A` and put `a=x_0`, `c=x_m`. Proposition 6.2 gives

`(a,v_{ell-1},v_{ell-2})`, `(v_1,v_0,c)`

at the two ends of `A`. Theorem 4.2 gives both fixed-pair restriction statements at each of the four end vertices

`v_{ell-1}, v_{ell-2}, v_1, v_0`,

for this same fixed pair `a,c`. Proposition 4.3 gives explicit three-vertex contact alternatives through each of those vertices, and Proposition 5.2 gives a separate deletion-crossing mechanism with exact adjacent edges from two compared covers.

The next target is to combine one of these data sets into a literal spanning two-path cover or a literal lexicographically improved three-path cover.

## 4. Historical endpoint-selection machinery

Earlier versions of the spine represented endpoint selection by a sequence of “current path systems” carrying historical certificates. That language was removed from the canonical proof because, without a separately defined transition relation, it is proof-process semantics rather than a graph-theoretic object. The reauthored fixed-pair deductions used in the present spine are direct consequences about extended paths and therefore need no such state space.

The older endpoint-selection/payment theorems remain part of project provenance and may still be useful for future research if a genuinely lineage-sensitive argument is needed. They should be reintroduced into the canonical proof only if a later theorem requires information that cannot be expressed as a fixed collection of paths, witnesses, sides, and incidence relations in `H`.

## 5. Reauthoring correspondence

The single-document spine was reauthored from the earlier GN3 proof files after commit `9ae9f366b69ebb3d394a57708e76bfd4ce77e9cf`. The main correspondence is:

| Earlier material | Current location or disposition |
| --- | --- |
| minimal counterexample, complement and pair deletion | Section 1 |
| small-order local lemmas and order `>10` | Section 2, now proved internally |
| terminal longest path and endpoint transfers | Section 3 |
| fixed-pair restrictions | Section 4, rewritten as direct statements about extended paths and their restrictions |
| four same-orientation vertices | Lemma 4.4 |
| deletion component formula and crossing | Section 5 |
| three same-orientation internal vertices and eight induced subgraphs | Propositions 5.3–5.4 |
| lexicographic extremal choice and fixed-pair end data | Section 6 |
| order-sensitive path intersection arguments | Appendix A |
| proposed augmentation lemma and reasons it is still missing | this note |

This note is research context, not part of the proof.