# Twisted and periodic gallery cut calculus for cubes and boundary tournaments

# Cyclic switch calculus for cube galleries and arbitrary boundary tournaments

## A binary local system and its cut identity

Let \(m\ge3\), \(h\in\{1,\ldots,m\}\), and \(w_i\in\mathbb F_2\), indexed by integers, satisfy
\[
w_{i+m}=w_i+\eta,\qquad\eta\in\mathbb F_2.
\]
Put \(d_i=w_i+w_{i+1}\pmod2\), and let \(D=\sum_{i=0}^{m-1}d_i\) be an integer sum. Then \(d\) is \(m\)-periodic and
\[
D\equiv\eta\pmod2.
\]
A retained switch-window with seam width \(h\) has cost
\[
J_s=D-\sum_{j=s}^{s+h-1}d_j.
\]
**Lemma 1 (cyclic cut transfer).** The cut costs obey
\[
\boxed{\sum_{s=0}^{m-1}J_s=(m-h)D,\qquad
\sum_{s=0}^{m-1}z^{J_s}
=\sum_{s=0}^{m-1}z^{D-\sum_{j=s}^{s+h-1}d_j}.}
\]
In particular, a cut with cost at most one exists if and only if one block of \(h\) consecutive comparisons contains at least \(D-1\) changes.

*Proof.* The switch sequence is periodic because the twist cancels when taking adjacent differences. Its cyclic XOR telescopes to \(\eta\), proving parity. Each comparison belongs to \(h\) deleted blocks and \(m-h\) retained blocks, proving the sum formula. The generating-function identity is termwise. \(\square\)

## Cubical odd-monodromy specialization

Let \(c:E(Q_n)\to\mathbb F_2\) be arbitrary except for \(c(\bar e)=1-c(e)\). Moving the first step of a rooted full geodesic to its end, while shifting the root over that edge, transforms its color word by
\[
(w_0,\ldots,w_{n-1})\mapsto(w_1,\ldots,w_{n-1},1-w_0).
\]
Therefore \(m=n,\eta=1,h=1\). A rooted rotation orbit has \(2n\) members and contains two lifts of each cyclic cut. If its odd cyclic switch count is \(D\), the orbit has \(2D\) paths with \(D-1\) ordinary switches and \(2(n-D)\) paths with \(D\) switches. The universal switch-spectrum identity from the preceding subsection follows. The presence of a monochromatic full geodesic is equivalent to existence of a rooted cyclic gallery with \(D=1\).

## Boundary even-monodromy specialization

Let \(V\) be an \(n\)-vertex set, \(n\ge4\), and let \(b(a,v,c)\) be an arbitrary reversal-odd boundary coloring:
\[
b(c,v,a)=1-b(a,v,c).
\]
Take any oriented Hamiltonian cycle \(C=(v_0,\ldots,v_{n-1})\), modulo rotations but not reversal, and define, with subscripts modulo \(n\),
\[
t_i=b(v_{i-1},v_i,v_{i+1}),\qquad
d_i=t_i+t_{i+1}\pmod2,\qquad D(C)=\sum_i d_i.
\]
The word \(t\) is \(n\)-periodic, so \(D(C)\) is even. Open the cycle into the Hamiltonian path
\(P_s=(v_s,v_{s+1},\ldots,v_{s+n-1})\).
The path's turn colors are \(t_{s+1},\ldots,t_{s+n-2}\); their switch count is
\[
\boxed{\sigma(P_s)=D(C)-(d_{s-2}+d_{s-1}+d_s).}
\tag{1}
\]
Thus the seam width is \(h=3\), rather than the cubical \(h=1\).

**Theorem 2 (boundary Hamiltonian cycle-window theorem).** Each oriented Hamiltonian cycle supplies \(n\) distinct Hamiltonian paths, and
\[
\boxed{\sum_{s=0}^{n-1}\sigma(P_s)=(n-3)D(C).}
\tag{2}
\]
The number of cyclic cuts with at most one switch equals the number of cyclic length-three blocks of \(d(C)\) containing at least \(D(C)-1\) ones. Hence:

- For \(D(C)=0\), all \(n\) cuts give monochromatic Hamiltonian paths.
- For \(D(C)=2\), at least four cuts give Hamiltonian paths with at most one switch.
- For \(D(C)=4\), some cut works if and only if three consecutive entries of \(d(C)\) are one.
- For \(D(C)\ge6\), no cyclic cut works.

The spanning one-switch Hamiltonian boundary conjecture is consequently equivalent to the existence of a Hamiltonian cycle with \(D(C)\le2\), or one with \(D(C)=4\) and three consecutive changes.

*Proof.* Each permutation of the \(n\) original vertices opens a unique oriented Hamiltonian cycle, obtained by appending its closing edge. Formula (1) omits three consecutive circular comparisons and retains the \(n-3\) internal comparisons. Apply Lemma 1 to obtain (2) and the cut condition. Since \(D\) is even, the four listed cases exhaust the possibilities. For \(D=2\), each of the two changed comparisons belongs to three deleted three-blocks; their combined set contains at least four different blocks. At \(D=4\), deleting at least three changed comparisons requires an all-one three-block; at \(D\ge6\), three deletions cannot leave fewer than three changes. \(\square\)

**Corollary 3 (unconditional spanning one-switch path on five vertices).** Every binary coloring of ordered triples on \(n\le5\) distinct vertices, even without reversal oddness, has a Hamiltonian vertex ordering whose consecutive triple-color word has at most one switch.

*Proof.* For \(n\le4\) there are at most two successive triple colors. At \(n=5\), any cyclic binary five-term turn word has \(D\in\{0,2,4\}\). The first two cases are covered by Theorem 2. In the last case, the cyclic comparison word has four ones and one zero, and therefore three consecutive ones. Theorem 2 applies. \(\square\)

**Theorem 4 (boundary quartet-discrepancy moment).** Let
\[
\beta(b)=\frac1{n(n-1)(n-2)(n-3)}
\sum_{\substack{a,u,v,d\in V\\\mathrm{distinct}}}
\mathbf1_{\{b(a,u,v)\ne b(u,v,d)\}}.
\]
For uniform oriented Hamiltonian cycle \(C\) and uniform Hamiltonian path \(P\),
\[
\boxed{\mathbb E D(C)=n\beta(b),\qquad
\mathbb E\sigma(P)=(n-3)\beta(b).}
\tag{3}
\]
In particular, if \(\beta(b)<4/n\), there is a Hamiltonian path with at most one switch.

*Proof.* Four consecutive vertices in a uniformly random oriented Hamiltonian cycle form a uniformly random ordered quadruple of distinct vertices. Thus each cyclic turn comparison changes color with probability \(\beta(b)\), giving the first equality. Averaging (2) over cycles, whose cuts partition the permutations, gives the second. If the mean cyclic count is below four, some cycle has even count zero or two; apply Theorem 2. \(\square\)

## Mathematical distinction

Both models encode the turn defects of full-resource galleries as cyclic \(\mathbb F_2\)-differences. An existence witness is a cut whose deleted seam contains nearly all defects. This is a shared statement valid for all legal colorings; no affinity, local transitivity, or special edge order is involved.

The cube has odd monodromy and a one-comparison seam; the boundary has even monodromy and a three-comparison seam. For the former, existence is governed solely by the smallest cyclic change count \(D=1\). For the latter, the relative positions of up to four cyclic changes also matter. Consequently a proof of the boundary conjecture must control clustering or reductions of cyclic turn defects, not just their total. The results give a common analytic mechanism but do not assert that a general unifying existence theorem has been proved.

## 5. Quantized local exchange curvature

**Lemma 5 (adjacent-exchange Lipschitz bounds).** On the graph of full-resource galleries related by transposing adjacent steps, the cyclic switch count \(D\) changes as follows:

(a) For arbitrary antipodally odd cubical edge colors, transposing two consecutive directions changes \(D\) by an even integer of absolute value at most two.

(b) For arbitrary boundary triple colors, transposing two consecutive vertices in a cyclic Hamiltonian ordering changes \(D\) by an even integer of absolute value at most four.

Both statements hold without assuming the target conjectures.

**Proof.** The cyclic switch count of a binary color word is the number of unequal adjacent colors, including the twisted closing comparison in (a) and the periodic closing comparison in (b). In both cases its parity is preserved under gallery transpositions: odd in (a), even in (b).

In (a), exchanging two consecutive coordinate steps replaces two edges of a single coordinate square; all the other path edges stay unchanged. Thus only two neighboring entries of the length-\(n\) edge-color word can change, affecting at most three consecutive cyclic comparisons. The integer difference of switch counts is even, so its magnitude is at most two.

In (b), swapping two consecutive vertices in the Hamiltonian cycle changes only the four consecutive triple colors whose centers are the swapped vertices or their two immediate neighbors. All other turn colors are unchanged. Therefore at most five cyclic comparisons are affected. The integer difference is even, hence of magnitude at most four. \(\square\)

**Variational consequence.** A gallery minimizing the cyclic switch count is automatically stable under every adjacent exchange. In the cube its local energy increments belong to \(\{0,2\}\), and for boundary Hamiltonian cycles they belong to \(\{0,2,4\}\). To prove the target from such a minimum, one must show that an odd local minimum with \(D\ge3\) (cube), respectively a boundary local minimum outside the \(D\le2\)/clustered-\(D=4\) extraction classes, is impossible or can be escaped by a coordinated sequence of zero-cost exchanges. The support bounds make this a finite-neighborhood curvature problem, not a solution in themselves.


## Switch signatures as the prescribed covering class

**Theorem 6 (odd vertex labels versus switch cohomology).** Let \(H\) be a finite graph with a fixed-point-free involution \(R\) on vertices and edges, let \(G=H/R\), and let \(\alpha=w_1(H\to G)\in H^1(G;\mathbb F_2)\). An edge signature \(s:E(G)\to\mathbb F_2\) arises from an odd vertex coloring \(c(Rv)=1+c(v)\) by
\[
s([uv])=c(u)+c(v)
\]
if and only if
\[
\boxed{[s]=\alpha.}\tag{6}
\]
For connected \(G\), the coloring is unique up to simultaneous complementation; in general it has one binary choice on each quotient component.

*Proof.* Select one lift \(\widetilde v\) of each quotient vertex. Put \(\eta(vw)=0\) if the lift of \(vw\) from \(\widetilde v\) reaches \(\widetilde w\), and \(\eta(vw)=1\) if it reaches \(R\widetilde w\). This cochain represents \(\alpha\). Writing \(b(v)=c(\widetilde v)\), oddness gives \(s(vw)=\eta(vw)+b(v)+b(w)\), so \([s]=\alpha\). Conversely, if \(s+\eta=\delta b\), assign \(c(\widetilde v)=b(v)\) and \(c(R\widetilde v)=1+b(v)\). These assignments induce \(s\) on every edge orbit. Any two potential choices differ by a locally constant function on \(G\). \(\square\)

**Corollary 7 (legal perturbations are graph cuts).** Two legal signatures on \(G\) differ by a coboundary \(\delta f\), i.e. by toggling all signature edges crossing a vertex cut. Changing just one switch while leaving all others unchanged is legal precisely when the selected edge of \(G\) is a bridge.

*Proof.* Theorem 6 says both signatures lie in the same affine coset \(\alpha+B^1(G;\mathbb F_2)\). A one-edge indicator is a graph coboundary if and only if that edge lies on no graph cycle. \(\square\)

**Theorem 8 (common switch-only encoding for both unrestricted gallery problems).** There are native graphs \(H_\square,H_\partial\) on which the two original reversal-odd bit colorings become odd vertex colorings, and the switches become representatives of the corresponding covering class.

For NORI1, take \(H_\square=L(Q_n)\), whose vertices are cube edges and whose adjacencies are incident pairs of distinct cube edges. Antipodal inversion acts freely. The quotient \(G_\square=L(Q_n)/A\cong L(Q_n/A)\) has vertices representing antipodal pairs of cube edges and edges representing projective turns. The NORI1 conclusion is equivalent to: every edge signature on \(G_\square\) in the class \(\alpha_\square\) admits a dimension-simple projective Petrie loop with precisely **one** active turn.

For ordinary reversal-odd boundary 3-tournaments, take \(H_\partial\) whose vertices are ordered triples \((a,b,c)\) of distinct symbols, with an undirected edge joining \((a,b,c)\) to \((b,c,d)\) for every ordered quadruple of distinct symbols. The involution \(R(a,b,c)=(c,b,a)\) preserves adjacency and reverses transition orientations. The quotient \(G_\partial=H_\partial/R\) has one edge for each reversal-orbit of four-symbol transitions. Every unrestricted odd triple coloring becomes an odd vertex coloring of \(H_\partial\). The boundary conclusion is equivalent to: every signature representing \(\alpha_\partial\) admits a vertex-simple Hamilton triple-overlap path with **at most one** active transition.

Neither \(G_\square\) nor \(G_\partial\) has bridges. In \(G_\square\), each turn belongs to a triangle formed by three edges incident at one projective cube vertex, since \(n\ge3\). In \(G_\partial\), every transition belongs to the four-cycle obtained by rotating its four distinct symbols:
\[
(a,b,c)\to(b,c,d)\to(c,d,a)\to(d,a,b)\to(a,b,c).
\]
Its quotient remains a cycle. Thus no single-switch deletion is legal in either unrestricted class.

*Proof.* Apply Theorem 6 to the graphs and involutions defined above. Cube edge bits become vertex bits of the line graph and their changes occur on turn edges. The closed projective Petrie path represents a nontrivial lift and has an odd number of changes; one change is equivalent, by cyclic root sliding, to a monochromatic antipodal half-geodesic. Consecutive ordered triples of a Hamilton vertex order trace a path in \(H_\partial\), and its changes are the transition signature. The graph-cycle assertions prove the bridge claim. \(\square\)

**Research consequence.** This is one common structural encoding of the two full unrestricted coloring classes; it does **not** yet prove one substantive shared path-existence theorem. Their distinguished complete path families differ. It does correct the natural switch-criticality induction: legal perturbations are whole graph cuts, not deletion of arbitrary isolated turns. The signed-graph class \(\alpha+B^1\), together with the prescribed dimension-simple or vertex-simple path family, is the proper object for cut-critical investigations.
