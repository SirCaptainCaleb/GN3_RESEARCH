# Exact two-window seam criterion for gluing directed monochromatic branches

# Exact ordered-three-face monochromatic connector gluing and two bridge windows

Let \(n\ge6\). Fix antipodes \(x,\bar x\), a meeting vertex \(z\), and two **directed** shortest paths
\[
A:x\to z,\qquad B:z\to\bar x
\]
of respective lengths \(a,b\ge3\), \(a+b=n\). Their direction sets are disjoint, since for each coordinate exactly one of the pairs \((x,z)\) and \((z,\bar x)\) differs. Thus \(A\cdot B\) is a complete antipodal geodesic. Let the direction words be \(A=(a_1,\ldots,a_a)\) and \(B=(b_1,\ldots,b_b)\).

Assume the ordered-three-face window colors within \(A\) are all \(q\) and those within \(B\) are all \(r\). Define the two cross-junction colors
\[
u=c(F(z;\{a_{a-1},a_a,b_1\}),(a_{a-1},a_a,b_1)),
\]
\[
v=c(F(z;\{a_a,b_1,b_2\}),(a_a,b_1,b_2)).
\]
The free sets in these two faces contain the indicated directions, and all their exterior bits are those of z, since z is a vertex of each cross window. (Thus the notation \(F(z;W)\) is exact.)

**Gluing theorem.** The full geodesic \(A\cdot B\) has color word exactly
\[
q^{a-2}\;u\,v\;r^{b-2}.
\]
If \(q=r\), the geodesic has at most one change exactly when \(u=v=q\). If \(q\ne r\), it has at most one change exactly when
\[
(u,v)\in\{(q,q),(q,r),(r,r)\};
\]
the sole forbidden bridge assignment is \((u,v)=(r,q)\).

**Proof.** Every three-edge window either lies wholly inside A, wholly inside B, or meets their seam. Since there are three consecutive edges per window, exactly two windows meet the seam and neither is contained in one branch: the triples of directions \((a_{a-1},a_a,b_1)\) and \((a_a,b_1,b_2)\). Both faces contain z, so their exterior bits agree with those of z. The asserted concatenated color word follows. Comparing successive symbols in the four blocks proves the binary criterion directly. \(\square\)

**Orientation guardrail.** In the NORI ordered-face setting, an outward monochromatic geodesic \(\bar x\to z\) cannot automatically serve as the directed branch \(B:z\to\bar x\), because reversing a segment reverses each ordered triple *on the same physical face*, whereas the NORI axiom relates reversed triples on the ANTIPODAL physical face. These are independent color values in general. Thus a valid common-target reachability labeling must pair forward reachability \(x\to z\) with directed **co-reachability** \(z\to\bar x\), retaining the last two directions of A and first two of B and their two bridge colors. For k=1 (undirected edge colors), there are no new cross-windows and reversing an edge path preserves color, recovering the standard easy common-vertex extraction. For k=3 the two bridge windows are the precise new obstacle.

**Topological closure target.** If some equivariant reachability/connector theorem forces an intersection of forward q-branch and co-reachable r-branch together with an admissible bridge pair, it immediately yields a one-switch NORI geodesic. When q≠r, three of the four bridge-color possibilities are admissible, giving a sharply specified candidate for a parity/topological obstruction to the remaining orientation (r,q). This is a conditional extraction lemma, not yet a forced compatible-connector existence theorem.
