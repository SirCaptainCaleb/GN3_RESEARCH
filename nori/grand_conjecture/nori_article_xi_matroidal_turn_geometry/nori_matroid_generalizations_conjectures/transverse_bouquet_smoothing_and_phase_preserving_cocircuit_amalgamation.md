# Transverse bouquet smoothing and phase-preserving cocircuit amalgamation

Let \(G\) be a finite simple graph with a connected two-sheeted cover \(\widetilde G\to G\), and let \(H=L(G)\). Write \(\alpha\) for covering monodromy and \(\kappa\) for the intrinsic line-graph contact-curvature class of Article XI. A turn signature \(d\) is a binary cochain whose sum on every star triangle is zero; this includes every color signature \(d=a+\delta f\).

Fix a vertex \(v\) of \(H\), corresponding to an edge \(xy\) of \(G\). The neighbors of \(v\) split into two cliques \(K_x,K_y\), according to whether their corresponding \(G\)-edges meet \(xy\) at \(x\) or at \(y\). A cycle of \(H\) is *moving at \(v\)* when its two neighbors at \(v\) lie in different cliques.

**Theorem 1 (transverse bouquet smoothing).** Let \(C_1,\ldots,C_k\) be simple cycles of \(H\), \(k\ge2\), pairwise vertex-disjoint except at a single common vertex \(v\), and each moving at \(v\). Then one can construct a simple cycle \(C\) of \(H\), on their vertex union with \(v\) possibly omitted, such that
\[
\boxed{|C|=\sum_{i=1}^k|C_i|-2\lfloor k/2\rfloor,}\tag{1}
\]
\[
\boxed{\alpha(C)=\sum_i\alpha(C_i),\qquad
\kappa(C)=\sum_i\kappa(C_i)\pmod2,}\tag{2}
\]
and for every turn signature \(d\),
\[
\boxed{w_d(C)\le\sum_iw_d(C_i).}\tag{3}
\]
The reduction in (3) is an even nonnegative integer.

*Proof.* Write \(a_i\in K_x,b_i\in K_y\) for the neighbors of \(v\) on \(C_i\). Remove \(v\) from each \(C_i\), leaving mutually vertex-disjoint paths \(P_i\) from \(a_i\) to \(b_i\). All their endpoints are distinct.

When \(k\) is even, add the clique edges \(a_1a_2,a_3a_4,\ldots,a_{k-1}a_k\), and \(b_2b_3,b_4b_5,\ldots,b_kb_1\). The resulting graph is one simple cycle, alternating among the \(P_i\), with length \(\sum_i(|C_i|-2)+k\).

When \(k\) is odd, instead add \(a_1a_2,a_3a_4,\ldots,a_{k-2}a_{k-1}\), and \(b_2b_3,b_4b_5,\ldots,b_{k-1}b_k\), and retain the original edges \(va_k\) and \(vb_1\). These pieces again form one simple cycle, now through \(v\), with length \(\sum_i(|C_i|-2)+(k-1)+2\). Both cases give (1).

Each added edge \(a_ia_j\) replaces the pair \(va_i,va_j\) by the third edge of the star triangle \((v,a_i,a_j)\), and similarly on the \(b\)-side. The number of such triangles is \(k\) in the even case, and \(k-1\) in the odd case; it is even in both. Thus the mod-two sum of their indicators, added to the sum of the indicators of \(C_i\), yields \(C\). On every star triangle, covering monodromy is zero and contact curvature is one. Therefore both cohomology signatures in (2) follow.

Finally, on each replaced star triangle the cocycle condition gives \(d(a_ia_j)=d(va_i)\oplus d(va_j)\). Hence its integer turn cost cannot exceed the sum of the two removed turn costs, and the difference is either zero or two. The same argument applies to all paired neighbors in the other clique. All other edges are retained, giving (3). \(\square\)

**Corollary 2 (two-cycle phase addition).** When \(k=2\), the surgery amalgamates two cycles sharing only one moving contact into one cycle of length \(|C_1|+|C_2|-2\), with additive monodromy and contact-curvature phases, and with no greater total color-disagreement weight. In the two-port lift of Article XI, the \((\alpha,\lambda)\) port signatures therefore add. In particular a cycle of phase \((1,0)\) and one of phase \((0,1)\) can give a single cocircuit of phase \((1,1)\), whenever the required transverse shared-state contact holds.

This supplies a phase-coherent local repair mechanism for splitting port sectors under cocircuit contraction. It does not apply when the cycles fail the transverse intersection condition, and it does not enforce a long forward resource-independent gallery.

**Theorem 3 (mixed-contact splice).** Suppose two simple cycles C1,C2 of H=L(G) meet only at v, with C1 moving and C2 stationary there. Then there exists a simple cycle C with length |C1|+|C2|-1, monodromy alpha(C)=alpha(C1)+alpha(C2), contact curvature kappa(C)=kappa(C1)+kappa(C2)+1 modulo two, and cost w_d(C)<=w_d(C1)+w_d(C2) for every admissible turn signature d. The reduction in cost is zero or two.

*Proof.* Let C1 meet v through neighbors a in the x-clique and b in the y-clique, and let C2 meet v through c,d in the x-clique, relabeling endpoints when necessary. Delete v to leave mutually disjoint paths P1 from a to b and P2 from c to d. Replace the two original incident edges va and vd by the clique edge ad, retaining vb and vc. The resulting walk v-b-P1-a-d-P2-c-v is a simple cycle, with the stated length. Its mod-two edge vector is the sum of those for C1,C2 and the star triangle v,a,d. That triangle has monodromy zero and contact curvature one. Its turn colors satisfy d(ad)=d(va) XOR d(vd), so the cost never increases; the improvement is even. QED.

This is a phase-flipping counterpart to the transverse bouquet theorem: a single balanced star-triangle surgery toggles the curvature port while preserving monodromy, whereas the even number of surgeries in a moving bouquet preserves both port phases.

**Theorem 4 (zero-cost one-triangle curvature extension).** Let \(C\) be a simple cycle of the turn graph \(H=L(G)\), with an edge \(va\) lying inside a vertex-star clique of \(H\). Let \(b\) be another vertex of this clique, not in \(V(C)\). Suppose a prescribed admissible binary turn signature \(d\) satisfies
\[
\boxed{d(vb)=0.}\tag{6}
\]
Replace \(va\) in \(C\) by the two-edge detour \(v-b-a\), obtaining \(C'\). Then \(C'\) is a simple cycle with
\[
\boxed{|C'|=|C|+1,\quad
\alpha(C')=\alpha(C),\quad
\kappa(C')=\kappa(C)+1\pmod2,\quad
w_d(C')=w_d(C).}\tag{7}
\]
Equivalently, the orientation-curvature port membership toggles while covering-monodromy port membership and integer color-intersection cost are unchanged.

*Proof.* The vertex \(b\notin V(C)\), so replacing the edge \(va\) with \(v-b-a\) preserves simplicity and increases length by one. The symmetric difference of the edge sets of \(C,C'\) is the star triangle \((v,a,b)\), on which covering monodromy is zero and canonical contact curvature is one. Consequently the two cohomology phases behave as stated. The turn-signature relation on the star triangle gives
\[
d(ab)=d(va)\oplus d(vb)=d(va)
\]
because \(d(vb)=0\). The removed edge \(va\) has the same cost as the new edge \(ab\), while \(vb\) costs zero, proving equality of integer weights. \(\square\)

**Proposition 5 (monochromatic curvature triangles at high-degree stars).** Suppose the base graph \(G\) has degree at least five at a vertex \(x\). For every deck-odd binary coloring of cover edges, the star clique in \(H=L(G)\) corresponding to the edges incident with \(x\) contains a triangle \(T\) with
\[
\boxed{w_d(T)=0,\qquad(\alpha(T),\kappa(T))=(0,1).}\tag{8}
\]

*Proof.* At either lift of \(x\), among its at least five incident edges, at least three have the same color. Their three pairwise turns form a star triangle downstairs. Every turn joins edges of the same color and therefore has zero cost. Star triangles lift to closed triangles, giving monodromy zero, and the intrinsic line-graph curvature evaluates to one on them. \(\square\)

For \(n\ge5\), the folded cube has degree \(n\), and the graph \(L(K_n)\) underlying ordinary boundary tournaments has degree \(2(n-2)\). Hence both canonical models have such zero-cost curvature triangles at every base vertex. **This alone does not guarantee Theorem 4's extension for a prescribed cycle:** an available zero-cost triangle must meet that cycle in the specified way, and the detour vertex must be unused. The distinction prevents conflating abundant local curvature supply with a global phase-switch selector.

**Theorem 6 (free curvature conjugation at a changed turn).** Let \(G\) be a finite simple graph with a connected two-sheeted cover, let \(H=L(G)\), and let \(d\) be a deck-odd turn signature. Let \(C\) be any simple odd-monodromy cycle in \(H\). Assume that at some changed turn \(va\in E(C)\), there is a third vertex \(b\) of the same star clique with \(b\notin V(C)\). Then replacing \(va\) by \(v-b-a\) gives a simple cycle \(C'\) satisfying
\[
\boxed{|C'|=|C|+1,\quad
\alpha(C')=\alpha(C),\quad
\kappa(C')=\kappa(C)+1\pmod2,\quad
w_d(C')=w_d(C).}\tag{9}
\]
In particular, if every base-graph vertex has degree at least \(s+1\) and every star clique meets \(V(C)\) in at most \(s\) vertices, such a companion cycle exists.

*Proof.* Since \(d(C)=\alpha(C)=1\pmod2\), at least one turn edge \(va\) of \(C\) is changed: \(d(va)=1\). The stated unused vertex \(b\) makes the detour simple. The mod-two edge difference is the star triangle \((v,a,b)\), which has monodromy zero and contact curvature one. On that triangle,
\[
d(vb)\oplus d(ba)=d(va)=1.
\]
Thus the two new turn indicators sum to one as ordinary integers, precisely matching the cost of the deleted turn \(va\). For the degree condition, the star clique has at least \(s+1\) vertices, of which at most \(s\) belong to \(C\); hence such an unused \(b\) is available at every changed turn. \(\square\)

**Corollary 7 (unconditional adjacent-sector pairing for cube geodesics).** For every \(n\ge3\), every antipodally odd coloring of cube edges, and every antipodal-geodesic turn cycle \(C\) of length \(n\) in \(H_n=L(Q_n/\tau)\), there is a simple odd-monodromy turn cycle \(C'\) of length \(n+1\) such that
\[
\boxed{w_d(C')=w_d(C),\qquad
(\alpha(C),\kappa(C))=(1,0),\quad
(\alpha(C'),\kappa(C'))=(1,1).}\tag{10}
\]

*Proof.* The folded cube has degree \(n\). The geodesic uses one edge per direction and visits each antipodal vertex pair at most once, except for the identified initial and terminal vertices. Consequently the star clique of any folded-cube vertex contains at most two geodesic edge-state orbits. (At an internal vertex these are its entering and departing edges; at the terminal seam they are the first and last edge orbits.) Apply Theorem 6 with \(s=2\) and \(n\ge3\). The geodesic has no stationary contact, so \(\kappa(C)=0\); the detour toggles that parity. \(\square\)

**Theorem 8 (equality of adjacent two-port minimum spectra).** Let \(\mathcal G_n\) be the odd-monodromy simple turn cycles of length \(n\) in \(H_n\), and let \(\mathcal S_n\) be those of length \(n+1\). For every \(n\ge3\) and every admissible turn signature \(d\),
\[
\boxed{
\min_{C\in\mathcal G_n}w_d(C)
=
\min_{C'\in\mathcal S_n}w_d(C').}\tag{11}
\]
Every member of \(\mathcal G_n\) has \((\alpha,\kappa)=(1,0)\), and every member of \(\mathcal S_n\) has \((\alpha,\kappa)=(1,1)\). Hence the two-port matroid has equal minimum port-cycle intersection weights over these two distinguished consecutive-length cocircuit sectors.

*Proof.* By the established directional-excess formula from Article XI, every odd-monodromy simple turn cycle of length \(r\) satisfies
\[
r=n+s(C)+2q(C),
\]
where \(s(C)\) is its stationary-contact count and \(q(C)\) its nonnegative repeated-direction excess. If \(r=n\), necessarily \(s=q=0\), so the cycle lifts to an antipodal geodesic. If \(r=n+1\), necessarily \(s=1,q=0\). The unique stationary contact admits the established star-triangle contraction, producing a simple odd-monodromy cycle of length \(n\) whose turn weight does not exceed that of the original length-\(n+1\) cycle. Thus the left minimum is no larger than the right one. Conversely Corollary 7 extends every length-\(n\) geodesic cycle to a length-\(n+1\) odd-monodromy cycle at the same cost, giving the reverse inequality. The curvature phases follow from \(\kappa(C)\equiv s(C)\pmod2\). \(\square\)

**Consequence for the conjecture.** In the cube, the monochromatic-geodesic assertion can equivalently be tested in the opposite curvature sector one turn above the port cogirth:
\[
\min_{C'\in\mathcal S_n}w_d(C')=1
\quad\Longleftrightarrow\quad
\min_{C\in\mathcal G_n}w_d(C)=1.
\tag{12}
\]
The additional turn does not weaken this minimization problem. It changes the two-port cocircuit sector while preserving the minimum integer overlap, and may permit alternative geometric or dual-matroid arguments.

**Theorem 9 (equal-weight cube-extension ladder).** For n>=3, every antipodal-geodesic turn cycle C of the folded cube, for every antipodally odd edge coloring and every 0<=t<=n-2, has at least binomial(n-2,t) distinct simple odd-monodromy cycle extensions C_t of length n+t. Their turn weights are all w(C), and their contact curvature is t modulo two. In particular the minimum turn weight among odd-monodromy cycles of length n+t cannot exceed the minimum weight of full geodesic cycles; the adjacent length n+1 case is an equality by Theorem 8.

*Proof.* Covering monodromy is odd on C, so at least one cyclic turn va has color difference one. The vertex va belongs to an incident-edge star clique K_x of the folded cube quotient. At every star the geodesic uses only two edge-state orbits, v and a, leaving n-2 unused clique vertices. Choose any t of those unused states. Order them with all states colored like v followed by all those colored like a. The detour v,b_1,...,b_t,a stays inside K_x and has one color change, just as va did. All inserted vertices were outside C, so the enlarged cycle is simple and retains the same integer turn cost. The symmetric difference with C is the star-clique cycle v,b_1,...,b_t,a,v; it has zero covering monodromy, and its contact curvature is t modulo two, because it triangulates into t star triangles, each with curvature one. The original geodesic has zero contact curvature. Different choices of the t inserted vertices give different enlarged-cycle vertex sets. This proves the binomial lower bound and the asserted weight and phase relations. QED.

**Corollary 10 (stationary-only spectral plateau).** For n>=3, every integer t with 0<=t<=n-2, and every admissible turn signature d, the minimum integer weight of an odd-monodromy simple turn cycle with length n+t and directional excess q=0 equals the minimum weight among antipodal-geodesic turn cycles of length n. Moreover all cycles in the binomial extension family of Theorem 9 have q=0 and stationary-contact count s=t.

*Proof.* The inserted edge states in the star-clique detour of Theorem 9 all have both contact vertices equal to the same cube vertex, so they are stationary; the original n geodesic edge states retain their distinct moving coordinates. Hence s=t and q=0 for every extension, establishing that the left minimum is no greater than the geodesic minimum. Conversely, the monotone stationary-contact contraction theorem already established in the first section of Article XI takes any odd-monodromy cycle with q=0 to a geodesic cycle while never increasing its integer turn weight. Therefore the left minimum is at least the geodesic minimum. QED.

The plateau applies to the q=0 sector only. For t>=2, unrestricted cycles of length n+t may have positive repeated-direction excess, and no equality for that larger family is asserted.

**Theorem 11 (equal-cardinality two-port cocircuit sector exchange).** Let D_n^(2) be the canonical bipointed binary matroid for the n-dimensional cube, with monodromy port p and orientation-curvature port q. Define A_n to be its cocircuits containing p and q of size n+2, and B_n to be its cocircuits containing p but not q of size n+2. For every binary cycle X of D_n^(2) containing p and avoiding q, the two families are nonempty and satisfy

min{|X intersect Y|:Y in A_n}=min{|X intersect Y|:Y in B_n}.

In particular, the unrestricted monochromatic NORI1 conjecture is equivalent to the assertion that for every such X there is a cocircuit Y in B_n with |X intersect Y|=2. This is a size-n+2 cocircuit condition in a single bipointed binary matroid, with port sector (p present, q absent).

*Proof.* By the canonical two-port construction in Article XI, every simple turn cycle C contributes a cocircuit comprising its turn edges and those ports prescribed by (alpha(C),lambda(C)), where lambda=alpha+kappa. An odd-monodromy cycle of length n is a geodesic with stationary count zero, so lambda=1 and its cocircuit belongs to A_n. An odd-monodromy cycle of length n+1 has one stationary contact, so lambda=0 and its cocircuit belongs to B_n. Conversely a cocircuit in either family arises from the indicated turn-cycle length and sector. For X containing p and avoiding q, intersection with either cocircuit is 1+w_d(C). The adjacent-length minimum-spectrum equality of Theorem 8 therefore gives the claimed equality of minimum intersections. Cyclic rotation converts turn weight one in a geodesic cycle to a monochromatic antipodal geodesic, proving the final equivalence. QED.

**Theorem 12 (four-element curvature-port cocircuit pivot).** In the canonical bipointed cube turn matroid D_n^(2), for every star triangle T of H_n the set Q_T=T union {q} is a four-element cocircuit containing curvature port q and not monodromy port p. Let Y=C union {p,q} be any full-geodesic cocircuit. Suppose T contains a changed turn e of C and its third star vertex lies outside C. Then the symmetric difference Y' = Y triangle Q_T is a cocircuit containing p but not q, has the same cardinality n+2 as Y, and for every admissible port cycle X with d(e)=1 satisfies |X intersect Y'|=|X intersect Y|. Conversely, every size-n+2 p-only cocircuit Y' has a unique stationary edge-state, and contraction at that state reverses such a four-element cocircuit pivot, producing a both-port cocircuit Y of size n+2 whose intersection with X does not exceed that of Y'.

*Proof.* A star triangle has monodromy zero and orientation curvature one, so adjoining q yields a cocircuit of the two-port lift. For the forward pivot, Y and Q_T intersect in q and the one old turn e, hence their symmetric difference replaces e by the other two sides of the triangle while deleting q. The third triangle vertex was unused in C, so the turn cycle remains simple. It has one additional turn and the same total cocircuit cardinality. The star turn signature has even parity on T; since d(e)=1, precisely one of its other two sides has label one, hence the X-intersection is unchanged. Conversely, the directional-excess identity forces a size-n+2 p-only cocircuit to have a length-n+1 monodromy-one turn cycle with one stationary contact and no repeated-direction excess. Its stationary state belongs to a unique local star triangle with the two neighboring states; shortcutting via the third side contracts it to a geodesic and adds q. The star-triangle cost inequality guarantees that intersection cannot increase. QED.

This identifies a local q-port cocircuit exchange realizing the adjacent-sector equality, rather than merely a numerical equality of optima.

**Theorem 13 (regular parent map between equal-size cocircuit sectors).** With A_n and B_n as in Theorem 11, for every n>=3 the stationary-contact contraction defines a canonical map pi:B_n -> A_n. Every fiber of pi has cardinality n(n-2), and

|A_n| = 2^(n-2) (n-1)!,     |B_n| = n(n-2) 2^(n-2) (n-1)!.

For a fixed admissible coloring turn cochain d, each B_n-child of a geodesic parent C has integer turn weight either w_d(C) or w_d(C)+2. At least (n-2)w_d(C) of the n(n-2) children retain precisely the parent's turn weight.

*Proof.* The directional-excess identity forces every odd-monodromy cycle of length n+1 to have one stationary contact and no repeated-direction excess. Its stationary edge-state has a unique pair of neighboring states, and replacing its two incident turns by the shortcut uniquely recovers a length-n geodesic cycle. Conversely, a geodesic has n cyclic turn edges, each lying in a folded-cube vertex-star clique containing n edge-state orbits, only two of which belong to that geodesic. Choosing any of the n-2 unused states and inserting it between the endpoints of the selected turn produces a unique simple length-(n+1) odd-monodromy cycle. These n(n-2) extensions are distinct and all contract back to their parent, proving the fiber count.

There are 2^n n! rooted directed full antipodal geodesics in the cube. Each undirected quotient geodesic turn cycle corresponds to 2n choices of oriented starting turn and two deck sheets, or 4n rooted directed geodesics. Hence |A_n|=2^n n!/(4n)=2^(n-2)(n-1)! and the B_n count follows.

For a triangle expansion replacing turn va through a new star state b, the two new turn labels have binary sum d(va). If d(va)=1, one new label is one and the other zero, so the integer weight is preserved for every one of the n-2 choices of b. If d(va)=0, the two new labels agree: their integer sum is either zero or two. Summing the n-2 neutral options for each of the w_d(C) changed turns yields the stated bound. QED.

This yields an uncolored regular cocircuit exchange map and a coloring-dependent lower bound on its cost-preserving outgoing degree. The structure is intrinsic to the canonical two-port representation together with its star-triangle family; ordinary cocircuit elimination alone does not imply such regular fibers.
