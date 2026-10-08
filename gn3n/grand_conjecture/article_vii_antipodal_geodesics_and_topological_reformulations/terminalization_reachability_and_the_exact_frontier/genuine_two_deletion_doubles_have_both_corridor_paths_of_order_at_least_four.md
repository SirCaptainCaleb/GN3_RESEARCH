# Genuine two-deletion doubles have both corridor paths of order at least four

## Composition

(none yet)

## Development

## A genuine two-deletion double has two substantial corridor paths

Retain the genuine two-deletion setup of [[genuine_two_deletion_doubles_reverse_all_four_corridor_ends]]:
[
J=Psqcup Qsqcup{x,y},qquad kappa_2(H[J])=2,
]
with P,Q tight paths.

For each exterior vertex e in {x,y}, neither P+e nor Q+e can be Hamiltonian. Indeed, if P+e were Hamiltonian, then
[
(P+e)mid Q
]
would two-cover J with the other exterior vertex deleted, contradicting the fact that each one-vertex deletion has path-cover number greater than two. The same argument applies to Q+e.

Now suppose |P|=2. Then P+e has order three and is Hamiltonian in every boundary tournament, contradiction. Hence |P|>=3.

Suppose |P|=3. Then P is a tight three-vertex path, while both four-sets
[
P+x,qquad P+y
]
are non-Hamiltonian. The two-bad-four-extension theorem in [[localextend01]] says that
[
P+x+y
]
has a Hamiltonian five-path. Therefore
[
(P+x+y)mid Q
]
is a two-cover of J, contradicting kappa_2(H[J])=2.

Thus
[
|P|ge4.
]
Symmetrically
[
|Q|ge4.
]

So the genuine two-deletion reflected-double residue occurs only in the mixed substantial-tail regime. All cases in which either corridor component has order at most three collapse directly to a two-cover.

This also means the remaining simultaneous four-end reversal configuration has at least ten vertices:
[
|J|=|P|+|Q|+2ge10.
]
The order-ten boundary case is the smallest genuine candidate and is covered by the established ten-vertex two-cover theorem; hence any actual kappa_2=2 residue must in fact satisfy
[
|J|ge11.
]
Thus the unresolved branch begins only beyond the finite ten-vertex theorem.
