# Antipodal incidence cocycles

# Rank-two cocycles and the antipodal cover

Let \(L_n\) be the line graph of \(Q_n\), \(n\ge2\): its vertices are the undirected cube edges, with adjacent vertices representing incident edges. It is connected. Antipodal complementation gives a free graph involution \(A\), and the quotient projection \(p:L_n\to L_n/A\) is a connected double cover.

For every antipodally odd binary edge coloring \(c\), define an \(A\)-invariant one-cochain on \(L_n\) by
\[
\epsilon_c(e,f)=c(e)+c(f)\pmod2
\]
for incident cube edges \(e,f\). This bit equals zero precisely when the two-step path through \(e,f\) is monochromatic, equivalently when its rooted Freudenthal triangle lies in the two-color prefix cone of Article XIV.

**Theorem 1 (covering class).** The descended cochain \(\bar\epsilon_c\) on the quotient graph represents the first Stiefel–Whitney class of the covering:
\[
\boxed{[\bar\epsilon_c]=w_1(p)\in H^1(L_n/A;\mathbb F_2).}
\]

*Proof.* A loop in \(L_n/A\) lifts to a path \(e_0,e_1,\ldots,e_r\) in \(L_n\), with \(e_r=A^h e_0\) for the covering-monodromy bit \(h\). The sum of the cochain around that loop telescopes:
\[
\sum_{j=1}^r\epsilon_c(e_{j-1},e_j)
=c(e_0)+c(e_r)=h
\]
by antipodal oddness. This is the defining evaluation of the double-cover class on the loop. \(\square\)

**Theorem 2 (complete rank-two encoding).** Sending \(c\) to its quotient cocycle induces a bijection
\[
\boxed{
\{\text{antipodally odd edge colorings}\}/(c\sim1-c)
\cong
\{\eta\in Z^1(L_n/A;\mathbb F_2):[\eta]=w_1(p)\}.
}
\]

*Proof.* Equality of local comparison cochains for two colorings makes their difference constant across all adjacent cube-edge pairs. Connectivity of \(L_n\) forces global constancy, proving uniqueness modulo complement. Conversely, if \([\eta]=w_1(p)\), the lifted cochain \(p^*\eta\) is a coboundary on \(L_n\), because the covering class pulls back to zero. Integrate \(p^*\eta\) to a function \(c\) on the vertices of \(L_n\), unique up to a constant. Along any path from \(e\) to \(Ae\), the integral equals the covering monodromy of its projected loop, which is one. Therefore \(c(Ae)=1-c(e)\), so \(c\) is a legal coloring inducing \(\eta\). \(\square\)

**Chain-level significance.** The rank-two prefix data remembers the entire unrestricted coloring up to a global color swap. Its cohomology *class*, however, is the fixed covering class and knows no coloring. A Wu–Yang-style full-geodesic proof must exploit the cocycle representative together with the Boolean constraint of disjoint dimension supports; oddness topology without this higher rank structure is insufficient.


## Cubical switch realizability, legal moves, and criticality

The preceding antipodal line-graph cocycle theorem has a fully intrinsic presentation on projective cube turns. It eliminates the original color bits while retaining the complete unrestricted NORI1 condition.

Write \(Y_n=\partial I^n/A\cong\mathbb RP^{n-1}\), \(G_n=Q_n/A\), \(n\ge3\), and \(m=|E(G_n)|=n2^{n-2}\). A switch system consists of symmetric bits \(s_{[v]}(i,j)\in\mathbb F_2\) for unordered distinct incident dimensions at each projective cube vertex \([v]\).

**Theorem 3 (triangle--square--period characterization).** The system is induced by an antipodally odd coloring of undirected cube edges if and only if:

(i) At each projective vertex, every three distinct directions satisfy
\[
\boxed{s_{[v]}(i,j)+s_{[v]}(j,k)+s_{[v]}(i,k)=0.}
\tag{3}
\]
(ii) On every cube square \(F\) with directions \(i,j\), the four corner switches sum to zero:
\[
\boxed{\sum_{v\in V(F)}s_{[v]}(i,j)=0.}
\tag{4}
\]
(iii) The sum of switch bits along one projective Petrie loop is odd.

If (i)--(ii) hold, all projective Petrie loops have the same switch-sum parity \(p\). Such a system is realized by an edge coloring satisfying \(c(Ae)=c(e)+p\), unique up to global complementation. Thus NORI1 is equivalent to the assertion that every system satisfying (3)--(4) and odd period admits a full dimension-simple Petrie loop with just one active switch.

*Proof.* Comparing three incident edge colors gives (3) by cancellation; summing corner comparisons around a square counts each edge color twice, proving (4). A projected antipodal full geodesic has odd switch sum because the color of its final lifted edge is complemented at the seam.

Conversely choose a reference direction \(r\), and put \(\lambda_r([v])=0\), \(\lambda_i([v])=s_{[v]}(r,i)\). By (3),
\(s_{[v]}(i,j)=\lambda_i([v])+\lambda_j([v])\).
For a projective edge of direction \(i\), define
\[
a([v],[v\oplus e_i])=\lambda_i([v])+\lambda_i([v\oplus e_i]).
\tag{5}
\]
The coboundary of \(a\) on an \(ij\)-square is the four-corner sum (4), so \(a\) is a cocycle on \(Y_n\). Pull it back to \(S^{n-1}=\partial I^n\); its cohomology class vanishes since \(n\ge3\). Consequently there exists a vertex function \(f\) with
\(f(v)+f(v\oplus e_i)=a([v],[v\oplus e_i])\).
Define the undirected edge color
\[
c(\{v,v\oplus e_i\})=f(v)+\lambda_i([v]).
\tag{6}
\]
Equation (5) proves independence of the chosen endpoint, and its local switches recover the prescribed system. Because \(a\) is antipodally invariant, \(p=f(v)+f(\bar v)\) is constant across \(v\); hence \(c(Ae)=c(e)+p\).

For an antipodal path \(v_0,\ldots,v_n=\bar v_0\) using directions \(i_1,\ldots,i_n\), the integral of \(a\) around its projective Petrie loop equals
\[
p=\sum_{j=1}^{n-1}s_{[v_j]}(i_j,i_{j+1})
+s_{[v_0]}(i_n,i_1).
\tag{7}
\]
This is obtained by grouping the endpoint \(\lambda\) terms in the edge sum; the two endpoint contributions meet at one projective vertex. Every Petrie loop represents the nonzero class in \(H_1(Y_n;\mathbb F_2)\), so all its periods agree. Condition (iii) gives \(p=1\). If two colorings realize the same system, their edge-color difference is constant on all edges incident to each vertex, hence constant over the connected cube. They differ by global complementation. A one-switch projective Petrie loop can be cyclically rooted at its unique switch, giving a monochromatic antipodal geodesic, and the converse holds. \(\square\)

**Corollary 4 (linear dimensions).** The switch assignments satisfying just (3)--(4) form a binary vector space of dimension \(m\). The odd-period assignments form an affine subspace of dimension \(m-1\), hence there are \(2^{m-1}\) realizable odd switch systems.

*Proof.* Colorings of both uniform antipodal parities \(p\) have \(m\) independent orbit-edge bits plus \(p\), giving dimension \(m+1\). The linear switch map is onto the triangle--square solution space by Theorem 3. Its kernel is the globally constant color flip, of dimension one. Odd period imposes one nontrivial linear equation. \(\square\)

For each projective edge \(e\in E(G_n)\), let \(T_e\) be the legal operation of flipping the colors on its antipodal pair of cube edges. It toggles the \(n-1\) comparisons involving its direction at either projective endpoint.

**Theorem 5 (sharp affine switch code).** The \(m\) moves \(T_e\) generate all differences between legal odd switch systems. Their only linear relation is
\[
\boxed{\sum_{e\in E(G_n)}T_e=0.}
\tag{8}
\]
The Hamming distance between any two distinct legal odd switch systems is at least \(2(n-1)\). Equality holds if and only if one is obtained from the other by one move \(T_e\) (equivalently, the complementary set of all other moves). The minimum-distance adjacency graph on legal switch systems is the folded \(m\)-cube \(Q_m/A\), of degree \(m\).

*Proof.* The difference of two odd edge colorings is an antipodally even function, so it is represented by a subset \(B\subseteq E(G_n)\). The resulting switch difference is \(\sum_{e\in B}T_e\), and vanishes if and only if the edge-bit difference is constant across all incident edge pairs. Connectedness forces \(B=\varnothing\) or \(B=E(G_n)\), establishing (8).

Let \(d_B(v)\) denote the number of selected edges incident to a projective vertex \(v\). A local turn changes when precisely one of its incident edges is selected; thus
\[
\boxed{d_H(s,s')=\sum_{v\in V(G_n)}d_B(v)(n-d_B(v)).}
\tag{9}
\]
Call \(v\) mixed when \(0<d_B(v)<n\). Every mixed vertex contributes at least \(n-1\). If none is mixed, connectivity forces the change to vanish. Just one mixed vertex is impossible: deleting it leaves a connected graph, so all remaining vertices have the same unmixed state and force it to have that state as well. Therefore a nonzero change has at least two mixed vertices and weight at least \(2(n-1)\).

At equality there are two mixed vertices, while all others are unmixed. The graph \(G_n\) stays connected after deletion of any two vertices: \(G_3=K_4\), and when \(n\ge4\) it has a spanning \((n-1)\)-cube whose vertex connectivity is \(n-1\ge3\). Thus all the remaining vertices have the same unmixed state. Up to replacing \(B\) by its complement, none of their edges is selected. Any selected edge must then join the two mixed vertices, giving just one selected projective edge. Conversely one such edge changes \(2(n-1)\) turn bits. The orbit-edge coloring cube modulo global color complement is \(Q_m/A\), and its minimum-distance adjacency is induced by the \(T_e\). \(\square\)

**Proposition 6 (dimension-simple criticality under legal moves).** A projective edge belongs to \((n-1)!\) Petrie cycles. Flipping its antipodal edge orbit changes only the two switches adjacent to that edge on any containing Petrie loop, and hence changes its grade \(h=(w-1)/2\) by at most one. A grade-one cycle is repaired to grade zero if and only if both adjacent switches were active before the flip.

For \(n\ge4\), if a coloring has no grade-zero cycles and \(H\subseteq E(G_n)\) consists of edges whose atomic flip creates a grade-zero cycle, then
\[
\boxed{|H|\le2Z_1(c),}
\tag{10}
\]
where \(Z_1(c)\) is the number of grade-one Petrie cycles. In particular, a hypothetical bad coloring for which every atomic move creates a monochromatic geodesic must contain at least \(m/2\) grade-one cycles. No claim is made that all bad colorings have this critical property.

*Proof.* Count loop-edge incidences to obtain \(n|\mathcal P_n|/m=(n-1)!\). The local flip toggles two adjacent turn bits and changes their number by \(-2,0,\) or \(2\). To reach grade zero from a coloring having no grade-zero loop, the original loop must have grade one and both toggled turns must be active. Three active turns on an \(n\)-cycle with \(n\ge4\) form at most two adjacent active pairs. Each grade-one cycle therefore witnesses the healability of at most two projective edges, proving (10). \(\square\)

**Research significance.** This presentation is equivalent to the preceding line-graph covering-class reconstruction, but adds native triangle and square constraints, a sharp switch-code distance, and a canonical legal perturbation geometry. One-turn deletion is never a realizable operation for \(n\ge3\); criticality and induction must use the paired edge-star moves or their combinations. These moves preserve the full dimension-simple path family and change each individual witness grade by at most one.



## The cographic matroid underlying legal switch changes

The preceding cubical presentation admits a succinct graphic-matroid interpretation. Unlike a hypothetical matroid whose bases are full Petrie turn sets, this matroid is intrinsic and exists in every dimension.

Let \(G=Q_n/A\), \(n\ge3\), and \(H=L(G)\). Thus the vertices of \(H\) are the \(m=n2^{n-2}\) projective edge orbits of the cube, and its edges are the
\[
t=2^{n-1}\binom n2
\tag{11}
\]
projective turns, one for each unordered incident pair of distinct projective edge orbits. The graph \(H\) is connected and regular of degree \(2(n-1)\). Write \(\operatorname{Cut}(H)=\operatorname{im}(\delta:C^0(H;\mathbb F_2)\to C^1(H;\mathbb F_2))\).

**Theorem 8 (affine cut-space description and a cycle presentation).** Fix one legal odd coloring and its turn signature \(s_0\). The space of turn signatures of **all** legal odd colorings is
\[
\boxed{s_0+\operatorname{Cut}(H).}
\tag{12}
\]
Its differences are cocycles of the graphic matroid \(M(H)\), or equivalently vectors of the cycle space of the cographic matroid \(M^*(H)\).

Moreover, the entire binary cycle space \(Z_1(H;\mathbb F_2)\) is generated by the following three families of cycles of \(H\):

(a) triangles formed by three projective edges incident with one vertex of \(G\);

(b) four-cycles formed by the four successive projective edges of each cubical square of \(G\);

(c) any one cycle formed by the sequence of projective edges of a complete Petrie loop of \(G\).

The local triangle cycles are linearly independent across projective vertices up to the usual local \(K_n\) triangle dependencies; their span has rank
\[
\boxed{2^{n-1}\binom{n-1}{2}.}
\tag{13}
\]
Modulo this span, the square cycles have rank \((n-2)2^{n-2}\), and one Petrie cycle contributes the last independent relation. In particular, these families collectively have cycle rank
\[
\boxed{\dim Z_1(H;\mathbb F_2)=t-m+1.}
\tag{14}
\]

*Proof.* Relative to the fixed coloring \(c_0\), the difference of any other odd coloring \(c\) descends to a bit \(b_e=c(e)+c_0(e)\) for each projective edge orbit \(e\), i.e. a vertex function \(b\) on \(H\). The comparison at a turn between orbit-edges \(e,f\) changes by \(b_e+b_f=(\delta b)(ef)\). Conversely, every vertex labeling \(b\) can be implemented by flipping the indicated antipodal edge orbits. This proves (12).

The turn comparison sum around a triangle in a local \(K_n\) is condition (3). The comparison sum around the four-cycle in \(H\) corresponding to a cubical square is condition (4). The sum around a Petrie line-graph cycle is its global projective switch period. By Theorem 3, a cochain \(z\in C^1(H;\mathbb F_2)\) has zero sum on all triangles, squares and the chosen Petrie cycle if and only if its local reconstruction has period zero, i.e. if and only if \(z=\delta b\) for some vertex function on \(H\). Therefore the orthogonal complement of the span of those cycles is \(\operatorname{Cut}(H)\). By cut--cycle orthogonality for connected graphs, that span is the full cycle space \(Z_1(H;\mathbb F_2)\).

For each vertex \(v\) of \(G\), the \(n\) orbit-edges incident with \(v\) form a clique \(K_n\) in \(H\). Its triangle cycles span a space of rank \(\binom{n-1}{2}\). Distinct projective vertices give disjoint sets of turn edges in \(H\), because two distinct edges of the simple graph \(G\) share at most one endpoint. Hence the local triangle spaces form a direct sum, proving (13).

Contracting the local triangle-cycle relations leaves the ordinary cycle space of \(G\). The projective cubical squares generate \(B_1(Y_n;\mathbb F_2)\), whose dimension is
\[
|E(G)|-|V(G)|+1-\dim H_1(Y_n;\mathbb F_2)
=m-2^{n-1}.
\]
Since \(H_1(Y_n;\mathbb F_2)\cong\mathbb F_2\) and every Petrie loop represents its nonzero element, the squares and any one Petrie cycle generate the remaining graph-cycle relations, contributing \((n-2)2^{n-2}\) and one dimension. Summing with (13) gives \(t-m+1\). \(\square\)

**Corollary 9 (the relevant matroid and its bonds).** The set of all legal switch *differences* is the cocycle space of the graphic matroid \(M(H)\). The elementary support-minimal nonzero differences are the bonds of \(H\), the circuits of the cographic matroid \(M^*(H)\). Its shortest bonds have size \(2(n-1)\), and Theorem 5 shows they are precisely the stars of individual vertices of \(H\), corresponding to flips of one projective cube edge orbit.

The natural switch-criticality induction should therefore use **cographic bonds and unions of bonds**, with the shortest bond acting on both endpoints of a projective cube edge. This is compatible with the earlier non-matroid theorem for complete Petrie turn sets: the cographic matroid governs *legal color-switch changes*, not which collections of turns constitute complete paths.

*Proof.* In a graph, nonzero cut vectors decompose into bonds, and bonds are the cocircuits of its graphic matroid, equivalently circuits of the dual. Theorem 5 identifies all minimum-size cut vectors and their support. \(\square\)

**Consequence for the covering obstruction.** The global antipodal twist appears here as the value one on the chosen Petrie cycle in the cycle-space presentation. All local triangle and cubical-square periods vanish; one distinguished noncontractible projective cycle detects the parity class. This is an explicit finite presentation of the projective covering class on \(H\), while the cographic bond structure describes every legal perturbation of its representative.


Atomic switch energy. Write m=n*2^(n-2) for the projective cube edge count, N for the total number of active projective turns, and d(e) for the active turns incident to the projective edge e. Flipping the antipodal edge orbit e gives N(new)-N(old)=2(n-1)-2d(e). Summing over e gives 2m(n-1)-4N, since every active turn is incident to two projective edges. Consequently N>m(n-1)/2 forces some legal atomic flip to decrease the switch support. This identity is valid for all antipodally odd colorings and uses only the intrinsic line-graph cut structure.

**Theorem (critical near-good witness bound).** Assume \(n\ge4\), a NORI1 counterexample exists, and \(c\) minimizes its projective switch support \(N\) among counterexamples. Let \(Z_1\) be its number of grade-one Petrie cycles. Set \(F=\{e:d(e)>n-1\}\), with \(d(e)\) the number of active turn comparisons incident to the projective edge \(e\). Then
\[
\boxed{2Z_1\ge |F|\ge
\max\{0,(2N-m(n-1))/(n-1)\}.}
\]
In particular the earlier universal necessary bound \(N\ge3\cdot2^{n-2}(n-1)\) for any counterexample gives
\[
\boxed{Z_1\ge2^{n-3}\max(0,6-n).}
\]

*Proof.* An edge \(e\in F\) has a support-decreasing legal flip by the atomic energy identity. The flipped coloring cannot remain bad, since \(c\) minimizes support among bad colorings. Hence that flip creates a grade-zero Petrie loop. Before the flip this loop must have grade one, with both turns adjacent to \(e\) active. Three active turns on a cyclic word of length \(n\ge4\) contain at most two adjacent active pairs, so any single grade-one loop can witness at most two such edges. This gives \(|F|\le2Z_1\). Every \(e\notin F\) has \(d(e)\le n-1\); every \(e\in F\) has \(d(e)\le2(n-1)\). Since \(\sum_e d(e)=2N\), we have \(2N\le m(n-1)+|F|(n-1)\), giving the lower bound on \(|F|\). Substitute the necessary bad-coloring density to obtain the last inequality. \(\square\)

The bound becomes vacuous at dimension six, exposing the limit of one-edge first-variation arguments. This is a conditional criticality theorem; it does not presume existence of counterexamples.

Atomic stationarity classification (proved). If every projective edge-orbit flip preserves total switch support, then n is even and every direction-i edge has color sum_{j!=i} x_j + a_i modulo two. Conversely all these affine odd colorings are stationary. The proof sums the endpoint switch-degree equations to obtain (A+(n-2)I)(s-n/2)=0 for the cube adjacency A and s(x)=number of incident one-edges. The Walsh eigenvalue -(n-2) forces s-n/2 to be a combination of size-(n-1) Walsh characters. Adding at neighboring vertices isolates each coefficient, which must be plus or minus one half; this reconstructs the asserted edge colors. For even n the reader matrix I+J squares to I over F2, so the affine Petrie distribution theorem gives n!/2 favorable Petrie loops. Therefore every bad coloring at or above the average atomic energy has some support-decreasing legal flip.

**Detailed spectral proof and full path certificate.** Write \(s(x)=\sum_{i=1}^n c_i(x)\) as an ordinary integer, and let \(d(e)\) denote the number of active turn comparisons involving the projective edge \(e\). If the color of \(e=\{x,y=x\oplus e_i\}\) is \(b\), then \(d(e)=s(x)+s(y)\) when \(b=0\), and \(d(e)=2n-s(x)-s(y)\) when \(b=1\). Stationarity sets \(d(e)=n-1\), so
\[
s(x)+s(x\oplus e_i)=n-1+2c_i(x).
\]
Summing over \(i\) gives \((A+(n-2)I)(s-n/2)=0\), with \(A\) the cube adjacency operator. Its eigencharacters are \(\chi_S(x)=(-1)^{\sum_{j\in S}x_j}\) of eigenvalue \(n-2|S|\). Therefore
\[
s(x)-n/2=\sum_i b_i\chi_{[n]\setminus\{i\}}(x).
\]
Add this expression at \(x\) and at \(x\oplus e_i\). Every term cancels except that indexed by \(i\). Comparing with the edge equation yields
\[
2b_i\chi_{[n]\setminus\{i\}}(x)=2c_i(x)-1\in\{-1,1\}.
\]
Hence each \(b_i=\pm1/2\), and each edge color is the parity of all input bits other than \(i\), possibly complemented. For odd \(n\), such a function is antipodally even and cannot be a legal odd coloring. For even \(n\), substitution verifies stationarity.

A direct monochromatic path certificate is available without the affine distribution theorem. For any dimension ordering \(\pi=(\pi_1,\ldots,\pi_n)\), put
\[
x_{\pi_t}=t-1+a_{\pi_t}+B\pmod2,\qquad B\in\mathbb F_2.
\]
Before the \(t\)-th step, the vertex parity is \(\sum_i x_i+t-1\), while the bit in dimension \(\pi_t\) is still \(x_{\pi_t}\). Thus the edge color is
\(\sum_i x_i+t-1+x_{\pi_t}+a_{\pi_t}=\sum_i x_i+B\), independent of \(t\). Every dimension ordering therefore has a monochromatic realization at two antipodal roots. The reader matrix \(I+J\) is invertible for even \(n\), giving the complete binomial Petrie count and \(Z_0=n!/2\).

At dimension six, the necessary bad-coloring switch support satisfies \(N\ge3\cdot2^{n-2}(n-1)=m(n-1)/2\). If \(N\) is larger, the summed atomic variation is negative, so some edge flip lowers \(N\). At equality, the absence of a lowering flip forces all variations to vanish, contradicting the favorable-path certificate. Hence any hypothetical bad \(Q_6\) coloring has a support-decreasing legal flip, although this alone does not prove that the original coloring has a good path.
