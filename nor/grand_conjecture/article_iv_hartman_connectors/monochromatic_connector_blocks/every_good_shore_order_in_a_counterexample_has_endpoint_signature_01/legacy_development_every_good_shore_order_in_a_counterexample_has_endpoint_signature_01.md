# Every good shore order in a counterexample has endpoint signature (0,1) — preserved pre-item development

## Composition

(none yet)

## Development

## Every good shore order in a counterexample has endpoint signature \(0,1\)

Work in the switching-normalized split
\[
B\to z\to A\to x.
\]
Let
\[
O=(a_1,\ldots,a_k)
\]
be any NOR-good order of \(A\), normalized with ternary word
\[
0^p1^q,\qquad p,q\ge1.
\]
Write
\[
e_i=1\iff a_i\to a_{i+1}
\]
in the fixed shore tournament.

If \(e_1=1\), then
\[
(x,z,a_1,\ldots,a_k)
\]
is spanning NOR-good on \(A\cup\{x,z\}\). Indeed
\[
\alpha(x,z,a_1)=0
\]
by the shore signature, while
\[
\alpha(z,a_1,a_2)=1\oplus e_1=0,
\]
and every later status is an old status of \(O\). Thus the new word is
\[
0^{p+2}1^q.
\]
Hence counterexamplehood forces
\[
e_1=0.
\]

If \(e_{k-1}=0\), then
\[
(a_1,\ldots,a_k,z,x)
\]
is spanning NOR-good. The old word is unchanged, and the two new final statuses are
\[
\alpha(a_{k-1},a_k,z)=e_{k-1}\oplus1=1,
\]
and
\[
\alpha(a_k,z,x)=1.
\]
Thus the new word is
\[
0^p1^{q+2}.
\]
Hence counterexamplehood forces
\[
e_{k-1}=1.
\]

Therefore every surviving good shore order satisfies
\[
\boxed{(e_1,e_{k-1})=(0,1).}
\]

The condition is invariant under reversal, since the endpoint bits of the reversed order are
\[
(1-e_{k-1},\,1-e_1)=(0,1).
\]

This is the unique residual endpoint signature. In particular the four-shore-vertex residual connector seed is universal across all good shore orders in a surviving switching split, rather than belonging to a special branch.

Elevation audit: the inferred endpoint signature is valid only if counterexamplehood concerns U=A∪{x,z}, or a separate extension theorem turns the displayed good U-orders into full-instance witnesses. In a counterexample on V=U∪B with B nonempty, U is proper and good U-orders are permitted. No such full-instance extension is established here. Retain the endpoint constructions but do not assume this signature universally in the full switching-split frontier.
