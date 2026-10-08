# Favorable shore endpoint orientations give an immediate spanning one-change order — preserved pre-item development

## Favorable shore endpoint orientations give an immediate spanning one-change order

Work in the switching-normalized split
\[
B\to z\to A\to x.
\]

Let
\[
O=(a_1,\ldots,a_k)
\]
be a NOR-good order of the shore \(A\), normalized with word
\[
0^p1^q,\qquad p,q\ge1.
\]
Write
\[
e_i=1\iff a_i\to a_{i+1}
\]
in the fixed shore tournament.

Assume
\[
e_1=1,\qquad e_{k-1}=0.
\]

Consider the full shore-plus-special order
\[
C=(z,a_1,\ldots,a_k,x).
\]

Every old internal window is unchanged, so the middle word is still
\[
0^p1^q.
\]

The new left endpoint window is
\[
\alpha(z,a_1,a_2)
=
t(z,a_1)\oplus t(a_1,a_2)\oplus t(a_2,z)
=
1\oplus e_1\oplus0
=
0.
\]

The new right endpoint window is
\[
\alpha(a_{k-1},a_k,x)
=
t(a_{k-1},a_k)\oplus t(a_k,x)\oplus t(x,a_{k-1})
=
e_{k-1}\oplus1\oplus0
=
1.
\]

Therefore
\[
C
\]
has word exactly
\[
0^{p+1}1^{q+1}.
\]

Hence it is a spanning NOR-good order on
\[
A\cup\{x,z\}.
\]

### Consequence

The endpoint orientation type
\[
(e_1,e_{k-1})=(1,0)
\]
requires no connector construction, no switch-local splice, and no port analysis at all.

By full reversal, the same conclusion holds for the reversed normalized presentation of the corresponding complementary endpoint type.

Thus every unresolved shore-order branch may be assumed to avoid this immediate endpoint closure. The whole-shore connector program is needed only for the remaining endpoint signatures.

Elevation audit: spanning here means A∪{x,z}. When B is nonempty this is a proper subset of the ambient instance; a bichromatic good order on it is not the compatible monochromatic connector used by homogeneous-cut gluing. Consequently it cannot alone eliminate this endpoint type from a full-instance counterexample.
