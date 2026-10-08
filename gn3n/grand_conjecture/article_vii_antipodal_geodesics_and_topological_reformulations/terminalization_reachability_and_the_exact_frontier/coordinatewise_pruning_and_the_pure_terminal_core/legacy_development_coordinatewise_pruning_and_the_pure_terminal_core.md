# Coordinatewise pruning and the pure terminal core — preserved pre-item development

## Coordinatewise pruning reduces terminalization to pure one-edge carriers

The fixed-path local-witness labels are signed basis vectors:
[
ell(pi)in{pm e_1,ldots,pm e_d}.
]
This gives a useful reduction that is independent of the separator construction.

Let (F) be a proper carrier face with a strictly positive balancing relation
[
sum_{piinmathcal V(F)}lambda_piell(pi)=0,
qquad
lambda_pi>0,
]
and let (e_r) be the innermost edge occurring among its labels. Split the chambers into
[
E_r={pi:ell(pi)=pm e_r},
qquad
O_r={pi:ho(pi)>r}.
]
Because the witness-edge vectors are linearly independent coordinates, the balance equation separates coordinatewise. Hence
[
sum_{piin O_r}lambda_piell(pi)=0
]
and independently the total positive weight on (+e_r) equals the total positive weight on (-e_r).

Therefore, whenever (O_r
eqarnothing), the same proper face (F) already contains a positive balanced **subconfiguration** supported strictly farther outward. No terminal finite analysis is needed to obtain this algebraic balance.

What is not automatic is that this outward subconfiguration is itself the full chamber set of a smaller permutahedron face with strictly positive weight on every chamber. Taking the smallest face containing its support can reintroduce depth-(r) chambers. Thus coordinatewise pruning does not by itself prove the carrier-to-carrier statement used by the local protected-band machinery.

It does, however, isolate the genuine hard case:

**Pure one-edge reduction.** The only case in which terminalization cannot even algebraically discard the innermost edge is a positive carrier face (F) for which every chamber label is one of
[
+e_r,quad -e_r.
]
Such a face is globally protected from all closer witnesses and contains both orientations of (e_r).

For a pure one-edge carrier, the audited paired-witness lemma immediately excludes the separable branch: if a face-block boundary separates the two determining windows, blockwise splicing stays in (F) and produces an outward-labeled chamber, contradicting purity. The audited dual-polarity terminal lemmas also eliminate every disjoint single-sided terminal branch. Hence a pure carrier can only lie in the centered/overlapping reflected terminal geometry, supported on at most ten determining vertices.

Accordingly the remaining carrier-level theorem may be sharpened to:

> **Pure terminal core.** A proper protected face all of whose selected labels are (pm e_r), with both signs present, cannot realize a centered/overlapping terminal configuration in a counterexample; equivalently it either contains an outward chamber or the bounded terminal support extends to a spanning two-cover.

This is strictly narrower than arbitrary mixed-cell completion. It separates the algebraic issue (already solved by coordinatewise pruning) from the face-coherence issue (pure centered/overlapping cells only).
