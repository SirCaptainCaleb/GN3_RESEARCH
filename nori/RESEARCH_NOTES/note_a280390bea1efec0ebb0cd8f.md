# Affine four-cube holonomy trap and Cartesian amplification of defect local minima

- Stable ID: note_a280390bea1efec0ebb0cd8f
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, geodesic-bigon, holonomy, local-minimum, cartesian-product, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_2
- Updated session: session_nori_r10917_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note


Let \(\mathbb F_2\) denote the field of two elements. On \(Q_4\) with bit positions \(0,1,2,3\), define a legal antipodally odd coloring by
\[
c_0=x_2,\qquad c_1=1+x_3,\qquad
c_2=1+x_0+x_1+x_3,\qquad
c_3=1+x_0+x_1+x_2
\quad\text{in }\mathbb F_2.
\tag{LM1}
\]
Each \(c_i\) ignores bit \(i\) and is complemented by the full antipodal map.

For the red swap involutions \(U_i\), let
\[
\pi=(2,1,3,0),\quad A=\{1,0\},\quad x=13,\qquad
W(\pi,A)=(1,0,2,1,3,0,2,3).
\]
Starting at \(x=13\), the successive states along this word are
\[
13,15,15,11,9,1,0,0,0.
\]
Thus \(U_W(13)=0\), while \(\bar x=2\), and the antipodal defect equals one.

Direct substitution into (LM1) gives the following complete single-edit neighborhood, with all values equal to
\(d_H(U_{W'}(x'),\overline{x'})\):

| single edit | resulting defects |
|---|---|
| change the root from \(13\) to \(13\oplus e_i\), \(i=0,1,2,3\) | \(4,4,3,3\) |
| change membership of \(i=0,1,2,3\) in \(A\), keeping \(\pi,x\) fixed | \(2,3,1,2\) |
| transpose adjacent positions \(1,2\), \(2,3\), \(3,4\) of \(\pi\), keeping \(A,x\) fixed | \(4,2,2\) |

In the simple-bigon parameter graph, only the interior membership changes at \(i=1,3\) and the middle transposition \((1,3)\) are admissible. Their defects are \(3,2,2\), respectively; all four one-bit root changes give defects at least three. Consequently **this is a strict positive-defect local minimum under every admissible elementary bigon exchange and every single-bit root change**. The two inadmissible boundary transpositions and the two inadmissible membership changes do not decrease the defect either.

The same coloring has a zero-defect simple bigon:
\[
\pi_*=(0,1,2,3),\quad A_*=\{3\},\quad x_*=5,\qquad
W_*=(3,0,1,2,3,0,1,2),\quad U_{W_*}(5)=10=\bar5.
\tag{LM2}
\]

**Theorem (Cartesian amplification of positive-defect local minima).** For every \(h\ge1\), the Cartesian product of \(h\) copies of (LM1) is a legal antipodally odd coloring on \(Q_{4h}\) with \(\eta_{\mathrm{hol}}=0\). Nevertheless it has an admissible simple-bigon/root pair with defect \(h\) such that changing one fiber bit, exchanging the class membership of one direction, or transposing two adjacent directions of the middle permutation never decreases the defect.

*Proof.* In each four-bit factor choose the trap parameters above; concatenate the orders \(\pi\), take the union of their membership sets \(A\), and root each factor at \(13\). The full word restricts to (LM1)'s trap word in every factor, and independent factor swaps commute, so its defect is \(h\). A single-bit root change modifies only one factor, where the defect increases. A membership change modifies one factor, where the displayed table shows that defect does not decrease. An adjacent transposition within a factor modifies one local order, increasing that factor's defect. An adjacent transposition across two factor boundaries preserves each factor's restricted word, hence preserves the full holonomy. The global parameters are admissible: the first direction in the concatenated permutation belongs to \(B\) and its final direction belongs to \(A\). Finally, concatenate \(\pi_*\) and combine \(A_*\) and roots \(x_*=5\) across the factors. The restriction of the resulting doubled word to each factor is \(W_*\), so its return is antipodal by (LM2). \(\square\)

Thus a local improvement theorem requiring an immediate strict decrease in Hamming defect under these elementary moves fails for arbitrarily large \(n\), even among affine legal colorings satisfying NORI1. Exchanges with temporary deterioration, plateau travel, or simultaneous coordinated edits remain possible.


**A three-edit minimax bypass.** The strict four-cube local minimum can be escaped along admissible bigon/root moves with defect sequence
\[
1\longrightarrow2\longrightarrow1\longrightarrow0.
\]
A certificate is
\[
\begin{array}{c|c|c|c|c}
\text{operation}&\pi&A&x& (U_W(x),\,d_H(U_W(x),\bar x))\\\hline
\text{start}&(2,1,3,0)&\{1,0\}&13&(0,1)\\
\text{swap middle }(1,3)&(2,3,1,0)&\{1,0\}&13&(4,2)\\
\text{flip root bit }3&(2,3,1,0)&\{1,0\}&5&(2,1)\\
\text{move }3\text{ into }A&(2,3,1,0)&\{3,1,0\}&5&(10,0).
\end{array}
\]
Every row satisfies the simple-bigon first/last membership conditions. The neighbor table above proves that any path from the initial parameter/root pair to a zero-defect pair must first reach defect at least two, so the displayed path minimizes its maximum defect.

In the \(h\)-fold Cartesian power, apply these three edits successively inside each factor while leaving the others untouched. Each factor changes its contribution \(1\to2\to1\to0\), so there exists a path from defect \(h\) to defect zero whose largest defect is \(h+1\). Hence the amplified examples obstruct strict one-step descent, while admitting a dimension-independent uphill allowance of one.


## A stronger four-cube minimax barrier

Take the affine legal antipodally odd coloring of \(Q_4\), with bits \(0,1,2,3\),
\[
c_0=x_1,\qquad c_1=1+x_3,\qquad c_2=x_1,\qquad c_3=x_0+x_1+x_2.
\tag{LM3}
\]
Choose the rooted simple bigon \(\pi=(1,0,2,3)\), \(A=\{0,2,3\}\), \(x=0\). Its word is \(W=(0,2,3,1,0,2,3,1)\), and its trajectory is
\[
0,1,5,13,15,15,15,15,13.
\]
Thus its antipodal defect is one.

**Theorem (sharp height-three minimax escape).** In the graph of admissible adjacent-permutation transpositions, interior membership flips, and single-bit root flips, the smallest possible maximum defect along a path from the displayed rooted bigon to any zero-defect rooted bigon equals three.

*Proof and finite certificate.* At \(x=0\), the sole admissible one-edit move with defect at most two is the swap of the two middle permutation entries, giving \(\pi'=(1,2,0,3)\), still with \(A=\{0,2,3\}\), and defect one. At either of the two resulting states, the four root-bit flips produce defects \((4,4,4,3)\); the two interior membership flips produce defects \((4,4)\). The other admissible adjacent transposition (the last two permutation entries) has defect four, while the middle transposition returns to the other state with defect one. Consequently the connected component of the sublevel set \(\{d\le2\}\) containing the chosen rooted bigon has just these two states and no zero-defect state. Hence every escaping path reaches defect at least three. Conversely, holding \(\pi,A\) fixed, the root sequence \(0\to8\to9\) has successive defects \(1,3,0\), proving equality. \(\square\)

**Product caveat and countercertificate.** The isolated four-cube height-three theorem above is valid. Its earlier asserted Cartesian minimax lower bound \(h+2\) is withdrawn. In a product coloring, the projection of an admissible global bigon to one factor may fail the first/last membership conditions for a simple local bigon. Those additional moves can defeat the local barrier.

For two copies, take \(\pi=(1,0,2,3,5,4,6,7)\), \(A=\{0,2,3,4,6,7\}\), and root zero, with each four-bit block using (LM3). Its global defect is two. Move letter \(5\) left past \(3,2,0,1\), producing \(\pi'=(5,1,0,2,3,4,6,7)\), with global defect remaining two throughout, because inter-factor transpositions preserve each factor's restricted word. The first direction \(1\) of the first block is now an interior global label; moving it into \(A\) is admissible and reduces global defect to one. Finally flip fiber bits \(7\) and \(4\) successively, giving defects three and zero. This is an admissible global exchange path with defect sequence \(2,2,2,2,2,1,3,0\). Thus the claimed \(h+2=4\) lower bound already fails at \(h=2\); moreover, for \(h\ge2\), the concatenated initial product state is not a local minimum because its second block's first label can be moved into \(A\), lowering the defect immediately. The general minimax barrier of product constructions requires new analysis and must not be inferred from the isolated factor.

The original four-cube height-three obstruction and its two-state sublevel certificate stand independently.
