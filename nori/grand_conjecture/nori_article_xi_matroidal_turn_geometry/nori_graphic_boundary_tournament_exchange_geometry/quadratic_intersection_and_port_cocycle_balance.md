# Quadratic intersection and port-cocycle balance

Let M be a finite binary matroid with distinguished port p, and let X be a binary cycle containing p. Every binary cocycle Y has even intersection with X by binary orthogonality. Define q_X(Y) to be half the intersection cardinality, reduced modulo two.

**Theorem 1 (quadratic intersection refinement).** The function q_X on the binary cocycle space W of M is quadratic. Its polar form is B_X(Y,Z)=|X intersect Y intersect Z| modulo two. This is an alternating bilinear form. If K is the port-free cocycle subspace and its polar restriction has rank 2r, then among all port-containing cocycles the fraction with intersection congruent to two modulo four differs from one half by at most 2^(-r-1). In particular, a positive polar rank forces at least one quarter of port-containing cocycles to have intersection congruent to two modulo four.

*Proof.* The identity |X intersect (Y symmetric-difference Z)|=|X intersect Y|+|X intersect Z|-2|X intersect Y intersect Z| establishes the polarization. Orthogonality makes its diagonal zero. The port-containing cocycles form an affine translate Y0+K. Their quadratic sign sum S=sum_{Z in K}(-1)^{q_X(Y0+Z)} obeys S^2=|K| times the character sum of the quadratic form on the radical of B_X restricted to K. That character sum is either zero or the cardinality of the radical. If the rank is 2r, its radical has codimension 2r, whence |S|<=|K|/2^r. Translating the sign sum into proportions proves the assertion. QED.

**Theorem 2 (local star-cut rank).** Let \(K_m\) be a complete graph with a binary coloring of its vertices, with \(a\) vertices of one color and \(b=m-a\) of the other. Put \(d(e)=1\) on edges joining different colors, and zero otherwise. On its binary graph cycle space \(Z(K_m)\), define
\[
B_d(U,V)=|U\cap V\cap\operatorname{supp}(d)|\pmod2.
\]
If \(a,b>0\), then
\[
\boxed{\operatorname{rank}B_d
=2\left\lfloor\frac{ab-1}{2}\right\rfloor.}\tag{4}
\]
If \(a=0\) or \(b=0\), the rank is zero.

*Proof.* Denote the two color classes by \(A,B\), so the changed-edge set is the cut \(\delta(A)\). A cycle \(U\) belongs to the radical of \(B_d\) precisely when its restriction \(U\cap\delta(A)\) is orthogonal to the entire cycle space of \(K_m\); thus this restriction is a cut of \(K_m\). Any cut supported wholly on the cross edges between \(A\) and \(B\) is either zero or all of \(\delta(A)\), since a vertex-partition cut containing no edge within either complete color class must be constant on each class.

If \(U\cap\delta(A)=0\), then \(U\) is a sum of cycles within \(K_a\) and \(K_b\), giving a radical subspace of dimension \(\binom{a-1}{2}+\binom{b-1}{2}\). A cycle \(U\) with \(U\cap\delta(A)=\delta(A)\) exists if and only if at least one of \(a,b\) is even: when both are odd, parity at each color class prevents completing the cut to an Eulerian set, while if either is even the odd-degree vertices of each color class occur in even numbers and can be paired by internal edges. Thus this second possibility contributes one additional radical dimension when \(ab\) is even.

Subtracting the radical dimension from
\[
\dim Z(K_m)=\binom{m-1}{2}
\]
gives rank \(ab-1\) when \(ab\) is odd and \(ab-2\) when \(ab\) is even, which is (4). \(\square\)

**Theorem 3 (universal modular balance in signed line-graph covers).** Let \(\widetilde G\to G\) be a connected regular two-sheeted graph covering with deck involution, where \(G\) is finite and simple with minimum degree \(m\ge4\). Let \(D\) be its associated pointed binary line-graph lift matroid and \(p\) its distinguished port. Fix any deck-odd edge coloring of \(\widetilde G\), with corresponding port cycle \(X_d\).

For each vertex \(v\in V(G)\), let the incident covering-edge states at either lift of \(v\) split into color classes of sizes \(a_v,b_v\) with \(a_v+b_v=\deg_G(v)\). Define
\[
R(d)=\sum_{\substack{v\in V(G)\\a_vb_v>0}}
2\left\lfloor\frac{a_vb_v-1}{2}\right\rfloor.
\]
Then the polar rank of \(q_{X_d}\) on the port-free binary cocycle space is at least \(R(d)\). In particular,
\[
\boxed{
\frac{|\{Y\in Z^*(D):p\in Y,\ |X_d\cap Y|\equiv2\pmod4\}|}
{|\{Y\in Z^*(D):p\in Y\}|}
\ge \frac12-2^{-R(d)/2-1}.}
\tag{5}
\]
Furthermore \(R(d)\ge2\lfloor(m-2)/2\rfloor\), so the right-hand side is at least
\[
\boxed{\frac12-2^{-\lfloor(m-2)/2\rfloor-1}.}\tag{6}
\]

*Proof.* The turn graph \(H=L(G)\) has one complete star clique at every base vertex, and these cliques have disjoint turn-edge sets. The cycle spaces of these star cliques are subspaces of the port-free cocycle space of \(D\): their turn cycles have zero covering monodromy. The local turn cochain \(d\) is the cut between the two classes of incident covering-edge colors. Theorem 2 therefore gives rank \(2\lfloor(a_vb_v-1)/2\rfloor\) on the corresponding local subspace. Disjoint supports make these subspaces mutually orthogonal for the polar form, giving total rank at least \(R(d)\). Apply Theorem 1 to obtain (5).

If no vertex star had both colors, all incident edges at every covering vertex would have a common color. Since the covering graph is connected, this would force every edge of the cover to have one color, contradicting deck oddness. Thus at least one base vertex has \(a_vb_v>0\). There \(a_vb_v\ge\deg_G(v)-1\ge m-1\); monotonicity of the local rank formula gives \(R(d)\ge2\lfloor(m-2)/2\rfloor\). This proves (6). \(\square\)

For the antipodal \(n\)-cube, \(m=n\) and the bound is \(1/2-2^{-\lfloor(n-2)/2\rfloor-1}\) for every \(n\ge4\). For the full-turn ordinary boundary-tournament double cover, \(m=2(n-2)\), and the bound is \(1/2-2^{-(n-2)}\) for \(n\ge4\).

These are quantitative statements about all port-containing cocycles. Converting them into intersection two with a shortest **port cocircuit** requires an additional length- and simplicity-preserving selection theorem; the modular balance alone does not close NORI1 or the boundary-tournament conjecture.

**Corollary 4 (four-cocycle modular switch).** Suppose a changed turn e belongs to a base star clique of size at least four. Choose two star triangles T1,T2 sharing only e. For any binary cocycle Y containing the distinguished port, the four port-containing cocycles Y, Y triangle T1, Y triangle T2 and Y triangle T1 triangle T2 include both an intersection congruent to two modulo four and an intersection congruent to zero modulo four. Every one differs from Y on at most four turn elements.

*Proof.* Each local triangle has zero covering monodromy and avoids the port, while the quadratic polar pairing of T1,T2 is the color-change indicator d(e)=1. Hence the quadratic intersection form cannot be constant on the four-element affine plane spanned by these triangles. Their symmetric difference has four turn edges. QED.

**Cocircuit extraction caution.** When Y is a geodesic cocircuit and e a changed turn, its two one-triangle extensions are simple stationary-contact cocircuits with unchanged cost, while the double-triangle extension has the opposite quadratic residue but forms a turn subgraph with local degree four at both endpoints of e. It need not be one simple cocircuit. Thus modular freedom at the cocycle level does not imply the shortest simple witness demanded by NORI1.

**Theorem 5 (component quotient cycle-space compression).** If H0 is the subgraph of zero-disagreement turns and J is obtained by contracting its components, restriction from Z(H) to Z(J) is surjective with kernel Z(H0). On the port-free cocycle quotient, the half-intersection quadratic form becomes q(t)=|t|/2 modulo two on the even-cardinality graph cycles t of J, with polar B(t,u)=|t intersect u| modulo two.

*Proof.* Any Eulerian set of changed edges of the quotient J has an even number of incidences at each contracted zero-turn component. Pair the incident endpoints inside that connected component and join each pair with zero-turn paths. Their mod-two sum together with the changed edges is an Eulerian set upstairs, proving the restriction map is surjective. Its kernel contains precisely those Eulerian sets using zero-turn edges alone. Covering monodromy is the parity of the changed edges because the coloring-turn cochain represents the covering class. Therefore the port-free binary cocycle sector projects onto the even-cardinality cycle subspace of J. The definitions of quadratic half-intersection and its polar form depend only on the changed-edge coordinates, proving the identities. QED.

**Corollary 6 (quotient cycle-rank bound).** Let R(d) be the sum of local star-cut polar ranks from Theorem 3. The even-cardinality binary cycle subspace of J has dimension at least R(d). Since J admits a cycle with odd cardinality, dim Z(J)>=R(d)+1. Writing r0 for the number of zero-turn components and D for the changed-turn set yields |D|-r0>=R(d). This constraint does not ensure a shortest port cocircuit with small intersection.
