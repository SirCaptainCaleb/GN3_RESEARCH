## Graphic and Boundary-Tournament Exchange Geometry

Let \(\widetilde G\to G\) be a connected regular two-sheeted cover of finite simple graphs, with deck displacement
\[
\delta=\min_{x\in V(\widetilde G)}\operatorname{dist}(x,\tau x)\ge3.
\]
Put \(H=L(G)\). Every simple cycle \(C\subseteq H\) of odd covering monodromy lifts to a cyclic sequence of edge states \(e_1,\ldots,e_r,e_{r+1}=\tau e_1\), with successive contact vertices \(u_i\), where \(u_0=\tau u_r\). Call \(e_i\) *stationary* when its preceding and following contacts coincide, \(u_{i-1}=u_i\), and *moving* otherwise. A **star-triangle pivot** replaces one edge of \(C\) by the other two edges of a triangle arising from three cover edges meeting at one vertex, or reverses this move, provided the new cycle remains simple and monodromy-odd.

**Theorem 1 (unique moving core and confluence).** For every odd-monodromy simple turn cycle \(C\), removing its stationary edge-state vertices by star-triangle contractions produces a simple odd-monodromy cycle \(C^\circ\) with no stationary contacts. The resulting cycle is independent of the order of these contractions: its cyclic edge-state sequence is obtained by deleting all stationary states from the original sequence. Every contraction preserves the ordered sequence of moving cover edges and their contact endpoints, and never increases integer turn cost for any deck-odd coloring.

*Proof.* If \(e_i\) is stationary, its two neighbors \(e_{i-1},e_{i+1}\) meet \(e_i\) at the same lifted vertex \(v\), so all three cover-edge states meet at \(v\). They define a star triangle in \(H\); shortcutting the two incident turn edges through the third deletes \(e_i\) and preserves simplicity, since \(C\) is simple and its length is at least \(\delta+1\ge4\) whenever a stationary state is present. A star triangle has covering monodromy zero, so odd monodromy survives. The two contact endpoints of every retained state remain unchanged under the shortcut, including at neighboring states. Thus their moving/stationary classifications are unchanged. Every deleted state was stationary before the deletion, and no new stationary state is created; induction proves that all removal orders delete the same set and leave the same cyclic moving-state order. The terminal cycle has at least \(\delta\ge3\) states, so it is a graph cycle. At a star triangle, the inequality \((a\oplus b)+(b\oplus c)\ge(a\oplus c)\) for binary edge-state colors proves the simultaneous nonincrease in integer cost. \(\square\)

**Theorem 2 (star-triangle exchange component theorem).** Form an undirected graph \(\mathscr E\) whose vertices are all simple odd-monodromy turn cycles of \(H\), joining two vertices when their edge-set symmetric difference is one balanced star triangle and both are simple. Then
\[
\boxed{C\text{ and }D\text{ lie in the same component of }\mathscr E
\iff C^\circ=D^\circ.}\tag{1}
\]
Every component has a unique minimum-length cycle, its stationary-free core. The core also minimizes every admissible integer turn cost over that entire component, simultaneously for all deck-odd edge colorings. The directed rewriting system obtained by orienting each pivot toward the shorter cycle is terminating and confluent.

*Proof.* Every stationary state can be deleted by a pivot, so every cycle is connected to its core. Conversely, a one-triangle expansion replaces a turn between states meeting at \(v\) by a two-turn detour through a previously unused edge state incident at \(v\). The inserted state has both contacts at \(v\), while the moving/stationary status and contacts of all original states are unchanged. Consequently both cycles have the same core. Induction along an exchange-graph path proves the forward implication of (1), while contracting both cycles to their common core proves the reverse implication. A stationary-free cycle admits no shortening pivot, every noncore cycle admits at least one, and Theorem 1 proves uniqueness and cost minimality. \(\square\)

**Corollary 3 (cube geodesic components and the directional-excess barrier).** In the folded cube turn graph \(H_n\), let \(q(C)\) denote the repeated-direction excess of Article XI. Star-triangle pivots preserve \(q(C)\) and the cyclic order of all moving coordinate directions. Among the monodromy-one cycles with \(q=0\), the exchange graph \(\mathscr E\) has
\[
\boxed{2^{n-2}(n-1)!}\tag{2}
\]
connected components, one for each antipodal-geodesic turn cycle. Every component is rooted at its distinguished length-\(n\) geodesic; its integer minimum turn cost equals the cost of that geodesic. No sequence of four-element curvature-port star-triangle cocircuit pivots can change the geodesic parent or decrease repeated-direction excess.

*Proof.* By the directional-excess identity, a stationary-free cycle with \(q=0\) has length \(n\) and is an antipodal geodesic. Theorem 2 identifies components with their stationary-free cores. The number of quotient geodesic turn cycles is \(2^{n-2}(n-1)!\), from the rooted directed count \(2^nn!\) divided by the \(4n\) choices of direction, sheet, and cyclic root representing the same turn cycle. Since the list of moving edge states is invariant under star-triangle pivots, so are their coordinate multiplicities and \(q\). \(\square\)

**Corollary 4 (constraint on a matroidal closure proof).** Let \(d\) be the turn cochain of an arbitrary antipodally odd cube-edge coloring. A strategy that starts with a minimum-cost monodromy-one cocircuit and uses only balanced four-element curvature-port cocircuits to simplify it will reach the stationary-free core of the *same moving walk*; it cannot reduce positive directional excess. Likewise, a strategy that starts from a geodesic cocircuit and makes only these local star-triangle pivots can never reach a different geodesic. Therefore any proof of unrestricted NORI1 by cocircuit exchange must additionally use an exchange relation that changes the moving direction word or its resource multiplicities. Adjacent square reroutings provide one candidate, but their turn weights need not decrease, as the strict exchange-local-minimum obstruction recorded in the generalizations research notes demonstrates.

The theorem also applies to the full-turn boundary-tournament cover, where it separates stationary contact removal from the remaining forward-polarity and vertex-injectivity defects.

### Hamilton path-forest overlaps and random boundary pattern universality

Let \(n\ge3\). Give each reversal-pair of distinct ordered triples an independent fair bit and its reverse the complementary bit. For a Hamilton vertex ordering \(\pi\), let \(W_b(\pi)\in\{0,1\}^{n-2}\) be its consecutive triple-color word. The \(n-2\) reversal-orbits along \(\pi\) are distinct, so \(W_b(\pi)\) is uniform.

**Theorem 1 (full-rank pattern second moment).** For any predetermined nonempty set \(A\subseteq\{0,1\}^{n-2}\), let \(Z\) count the Hamilton orders with word in \(A\), and put
\[
p=|A|2^{2-n},\qquad c_n=\frac{(e^2-1)(n-2)}{n(n-1)}.
\]
Then
\[
\boxed{\mathbb EZ=n!p,\quad\operatorname{Var}(Z)\le c_n(\mathbb EZ)^2,\quad
\Pr(Z>0)\ge(1+c_n)^{-1}.}
\tag{1}
\]
Moreover \(\Pr(Z<(1-\delta)\mathbb EZ)\le c_n/\delta^2\) for \(0<\delta<1\).

*Proof.* For two vertex permutations \(\pi,\sigma\), let \(K\) count the reversal-orbits of length-three windows they share. Their two color words together involve \(2(n-2)-K\) independent bits. Counting pairs of allowed words while disregarding compatibility on shared bits gives
\[
\Pr(W_b(\pi)\in A,\ W_b(\sigma)\in A)\le p^2 2^K.
\tag{2}
\]
Fix \(\pi\). Any \(k\) of its consecutive-triple windows contain a path forest of \(s\ge k+1\) edges of \(K_n\), with at most \(k\) nontrivial path components. For \(\sigma\) to contain all the selected triple-orbits, its consecutive adjacency edges must contain this forest. A path forest of \(s\) edges and \(c\) nontrivial components occurs in \(2^c(n-s)!\) permutations: orient each path component, contract it to one block, and permute all blocks. Thus
\[
\mathbb E_\sigma\binom Kk
\le\binom{n-2}k\frac{2^k(n-k-1)!}{n!}
=\frac{2^k(n-k-1)}{k!\,n(n-1)}.
\tag{3}
\]
Using \(2^K=\sum_{k=0}^K\binom Kk\), we obtain
\[
\mathbb E_\sigma 2^K\le1+
\frac{n-2}{n(n-1)}\sum_{k\ge1}\frac{2^k}{k!}
=1+c_n.
\tag{4}
\]
Sum (2) over all ordered permutation pairs to obtain
\(\mathbb E Z^2\le(1+c_n)(\mathbb EZ)^2\).
The variance estimate follows by subtraction, the positivity bound by Cauchy–Schwarz, and the lower-tail bound by Chebyshev. \(\square\)

**Corollary 2 (almost-all spanning one-turn boundary paths).** The number of binary words of length \(n-2\) with at most one color change is \(2(n-2)\). Therefore, if \(Z_{\le1}\) counts full spanning at-most-one-turn vertex-simple tight paths,
\[
\boxed{\mathbb EZ_{\le1}=n!(n-2)2^{3-n},\qquad
\Pr(Z_{\le1}=0)\le\frac{c_n}{1+c_n}=O(n^{-1}).}
\tag{5}
\]
With probability at least \(1-4c_n\), there are at least \(\frac12\mathbb EZ_{\le1}\) such paths. For any single prescribed color word, its realization by some Hamilton order has probability at least \(1/(1+c_n)\). Simultaneous realization of all color words is not claimed.

**Theorem 3 (fixed fractional Hamilton selector obstruction).** Let \(\lambda\) be an arbitrary distribution on Hamilton vertex paths selected independently of the tournament coloring, and let \(\operatorname{sw}_b(\pi)\) count the changes along its triple-color word. Then
\[
\boxed{\mathbb E_b\mathbb E_{\pi\sim\lambda}\operatorname{sw}_b(\pi)=\frac{n-3}{2}.}
\tag{6}
\]
In particular, for \(n\ge6\), some reversal-odd coloring has \(\mathbb E_{\pi\sim\lambda}\operatorname{sw}_b(\pi)>1\).

*Proof.* For any fixed \(\pi\), its two successive triple windows lie in distinct reversal-orbits and their colors are independent fair bits. Each of its \(n-3\) change indicators therefore has expectation \(1/2\). Average first over \(b\), then over \(\lambda\). Some coloring attains at least that mean. \(\square\)

**Graphic-matroid interpretation.** A Hamilton path's \(n-1\) edges form a basis of \(M(K_n)\), with the additional degree-two path condition. Each triple window is a two-edge flag of that basis. Any \(k\) common flags between two Hamilton words require at least \(k+1\) shared graphic basis edges. This additional edge gives the \(O(n^{-1})\) overlap-energy bound. The results are full-resource and all-dimensional, but do not close the worst-case spanning one-turn conjecture. Theorem 3 precludes a coloring-independent fractional basis mixture as a universal average-cost certificate; the missing witness must adapt to the coloring and preserve the integral path constraints.

Let \(n\ge4\), and let \(H_n=L(Q_n/\tau)\) be the folded-cube turn graph. Retain Article XI's monodromy and contact-curvature classes \((\alpha,\kappa)\), and the bipointed dual matroid \(D_n^{(2)}\) with ports \(p,q\), with orientation signature \(\lambda=\alpha+\kappa\). Write \(\mathcal G_n\) for the antipodal-geodesic turn cycles of \(H_n\).

**Theorem 1 (balanced hexagon exchange).** Let \(C\in\mathcal G_n\), and choose two consecutive coordinate directions \(a,b\) in its cyclic direction word. Exchanging their traversal order produces another geodesic turn cycle \(C'\in\mathcal G_n\) with
\[
\boxed{C\mathbin{\triangle}C'=Z,}
\tag{1}
\]
where \(Z\) is a simple six-edge cycle of \(H_n\) with
\[
\boxed{\alpha(Z)=\kappa(Z)=\lambda(Z)=0.}
\tag{2}
\]
Thus \(Z\) itself is a six-element cocircuit of \(D_n^{(2)}\) avoiding both distinguished ports, and the two geodesic cocircuits satisfy
\[
\boxed{(C\cup\{p,q\})\mathbin{\triangle}Z=C'\cup\{p,q\}.}
\tag{3}
\]
For every antipodally odd edge coloring with turn cochain \(d\),
\[
\boxed{w_d(C')-w_d(C)\in\{-2,0,2\}.}
\tag{4}
\]

*Proof.* Root the cyclic geodesic so the exchanged directions occur consecutively, and denote its corresponding four successive edge states (on the cyclic lift) by \(U,A,B,V\). The alternative route around the elementary cube square uses edge states \(B',A'\) instead of \(A,B\), with the same predecessor \(U\) and successor \(V\). Hence the affected turn paths are
\[
U-A-B-V,\qquad U-B'-A'-V.
\]
They are internally vertex-disjoint in \(H_n\). Indeed the edge-state directions of \(A,B\) are distinct and occur only once in a geodesic; the alternative edges \(A',B'\) are different cube edges of those same directions, neither antipodal translates of the original edges nor one another. For \(n\ge4\), the two unchanged neighboring states \(U,V\) are also different. Therefore the symmetric difference of the two geodesic cycles is the simple turn hexagon
\[
Z=U-A-B-V-A'-B'-U.
\]
Both geodesic cycles have covering monodromy one and have no stationary contacts, hence \((\alpha,\kappa)=(1,0)\); their symmetric difference has signatures \((0,0)\). A simple turn cycle with zero monodromy and zero orientation curvature is a circuit of the primal two-port incidence matrix without either port, hence is a cocircuit of \(D_n^{(2)}\). This proves (1)–(3).

Only the three consecutive turn costs along the two displayed paths differ. Since the admissible cochain \(d\) evaluates to zero on the balanced hexagon, the sums on the two three-edge paths have the same parity; each is between zero and three. Their difference must therefore be \(-2,0,\) or \(2\), proving (4). \(\square\)

**Theorem 2 (global connectivity by port-free hexagons).** The graph whose vertices are \(\mathcal G_n\), with edges joining pairs related by the balanced hexagon exchange of Theorem 1, is connected.

*Proof.* Represent a geodesic by a starting cube vertex \(x\in\mathbb F_2^n\) and a permutation \(\pi\) of the coordinate directions, modulo identifying representations of the same cyclic antipodal turn cycle. Adjacent coordinate transpositions generate the full symmetric group, so Theorem 1 connects every two direction orders at a fixed \(x\). Cyclically rerooting one geodesic after its first edge replaces \((x,(i,\pi_2,\ldots,\pi_n))\) by the representation
\[
(x+e_i,(\pi_2,\ldots,\pi_n,i))
\]
of the same turn cycle. Because transpositions can move any chosen coordinate \(i\) to the first position, this identification connects the directions' permutation classes at \(x\) and at \(x+e_i\). The edges \(x\leftrightarrow x+e_i\) generate the whole cube, so all starting vertices and all direction orders lie in one connected exchange graph. \(\square\)

**Corollary 3 (two-generator presentation of the zero-resource-excess exchange geometry).** Let \(\mathcal Z_0\) be the family of monodromy-one simple turn cycles of \(H_n\) with repeated-direction excess \(q(C)=0\). Equip \(\mathcal Z_0\) with two types of allowable symmetric-difference moves:

(i) a balanced star triangle, which toggles the curvature port in the bipointed matroid and inserts or removes one stationary edge state; and

(ii) a balanced turn hexagon as in Theorem 1, applied at a stationary-free geodesic, which changes the cyclic order of two neighboring coordinate directions while preserving both port sectors.

Then the resulting exchange graph on \(\mathcal Z_0\) is connected for every \(n\ge4\).

*Proof.* By the unique-core theorem in the preceding Subsection, every \(C\in\mathcal Z_0\) contracts using moves of type (i) to its unique stationary-free core. Since \(q(C)=0\), that core is a length-\(n\) antipodal geodesic cycle. Theorem 2 connects any two such cores by moves of type (ii). Reversing the star-triangle contractions of a chosen destination cycle then yields a path between any two cycles of \(\mathcal Z_0\). \(\square\)

**Corollary 4 (discrete intermediate-value property).** For any antipodally odd coloring, the set of integer cyclic turn weights attained by antipodal geodesics is an interval of odd integers:
\[
\boxed{\{w_d(C):C\in\mathcal G_n\}=
\{m,m+2,\ldots,M\}}
\tag{5}
\]
for some odd \(m\le M\). This statement does not assert \(m=1\).

*Proof.* The geodesic exchange graph is connected by Theorem 2. Along every exchange edge, the integer weight changes by at most two and preserves odd parity by Theorem 1. A path connecting a minimum-weight and a maximum-weight geodesic must therefore encounter every intermediate odd value. \(\square\)

The spanning one-turn boundary-tournament conjecture involves a different marked gallery language, so these cube-specific exchange generators do not by themselves supply the desired resource-independent directed tournament connector. Moreover, the nonoptimal strict exchange-local minima constructed for \(n\ge9\) in the research notes show why connectivity and the local two-unit cost bound cannot be strengthened to universal monotone descent.

Let \(G\) be a finite connected simple graph with at least two edges, and write \(H=L(G)\). A **turn** of \(G\) is a pair of distinct edges incident with a vertex \(v\); it is an edge of \(H\) and has a uniquely determined center \(v\). For each \(v\in V(G)\), the turns centered at \(v\) form the complete star clique \(K_v\cong K_{\deg_G(v)}\) inside \(H\). Their edge sets partition \(E(H)\).

For \(z\in Z(H)\), the binary cycle space of \(H\), define, for each original edge \(e=uv\in E(G)\),
\[
\Phi_G(z)_e
=\sum_{\substack{h\in E(K_u)\\ h\text{ incident with }e}}z_h
=\sum_{\substack{h\in E(K_v)\\ h\text{ incident with }e}}z_h
\pmod2.
\tag{1}
\]
The two sums agree because the full degree of the vertex \(e\) in the Eulerian turn set \(z\) is even.

**Theorem 1 (canonical line-graph cycle-space sequence).** The map \(\Phi_G\) is a well-defined surjective linear map \(Z(H)\to Z(G)\), and its kernel is the direct sum of the local star-clique cycle spaces:
\[
\boxed{
0\longrightarrow
\bigoplus_{v\in V(G)}Z(K_{\deg_G(v)})
\longrightarrow Z(L(G))
\xrightarrow{\ \Phi_G\ } Z(G)
\longrightarrow0.
}
\tag{2}
\]
In particular, \(\ker\Phi_G\) is generated by the star triangles of \(H\), and
\[
\boxed{\dim\ker\Phi_G
=\sum_{v\in V(G)}\binom{\deg_G(v)-1}{2}.}
\tag{3}
\]

*Proof.* Because \(z\in Z(H)\), the number of turns from \(z\) incident with each vertex \(e\) of \(H\) is even. The incident turns partition according to the two endpoints \(u,v\) of the original edge \(e\), making the two parity sums in (1) equal. At any original vertex \(u\in G\), summing the coefficients \(\Phi_G(z)_e\) over \(e\ni u\) counts every turn in \(K_u\) twice, and hence vanishes over \(\mathbb F_2\). Thus \(\Phi_G(z)\) is Eulerian in \(G\).

Every simple cycle \(e_1,\ldots,e_k\) of \(G\) lifts to the simple turn cycle \((e_1,e_2),\ldots,(e_k,e_1)\) of \(H\). Each original edge state then has one incident turn at each endpoint, so its image under \(\Phi_G\) is the original cycle. Simple cycles generate \(Z(G)\), proving surjectivity.

Now \(\Phi_G(z)=0\) precisely when every edge-state vertex \(e\) has even degree separately in each star clique \(K_u\) containing it. Since the turn edge sets of distinct star cliques are disjoint, this is equivalent to \(z|_{K_u}\in Z(K_u)\) for every original vertex \(u\). The kernel is therefore the asserted direct sum. Each complete-graph cycle space is generated by its triangles and has dimension \(\binom{\deg(u)-1}{2}\), proving (2) and (3). \(\square\)

If \(\widetilde G\to G\) is a connected two-sheeted graph covering with monodromy \(\beta:Z(G)\to\mathbb F_2\), its induced line-graph monodromy satisfies
\[
\boxed{\alpha=\beta\circ\Phi_G\quad\text{on }Z(H).}
\tag{4}
\]
Indeed any lifted turn cycle walks between contact vertices along the original edges counted by \(\Phi_G\), and stationary contacts contribute no moving edge. Hence the cover-sheet change depends only on the projected Eulerian base-graph cycle. Star triangles have zero monodromy and lie in the kernel of \(\Phi_G\).

Equation (2) is a canonical algebraic distinction between **local stationary-contact geometry**, carried by the kernel, and **global moving-walk homology**, carried by \(Z(G)\). It is independent of coloring and applies equally to the cube and ordered-pair boundary-tournament graph covers.

**Theorem 2 (cube triangle-square presentation).** For n>=3, put G_n=Q_n/tau and H_n=L(G_n). Let T denote all local star triangles in H_n and S the turn cycles corresponding to projected coordinate squares of Q_n. Then the binary cycle space of H_n has kernel of covering monodromy alpha equal to span(T union S). Together with any one antipodal-geodesic turn cycle C0, these generators span the entire cycle space. Thus the quotient by the star triangles and projected squares has dimension one, generated by C0.

*Proof.* First, the cycle space of the ordinary cube \(Q_n\) is generated by its coordinate squares. An elementary induction proves this: write \(Q_n\) as two copies of \(Q_{n-1}\) connected by matching edges of the last coordinate. Any Eulerian edge set has an even number of matching edges. Square boundaries involving the last coordinate let one transport those matching-edge incidences along paths within the lower-dimensional cube and eliminate them in pairs. What remains is a sum of Eulerian chains within the two copies of \(Q_{n-1}\), which are generated by squares by induction.

Next, if \(\pi:Q_n\to G_n\) is the two-cover, the image of the pushforward \(\pi_*:Z(Q_n)\to Z(G_n)\) is precisely the kernel of covering monodromy \(\beta\). Every closed lifted cycle has zero monodromy downstairs. Conversely, for an Eulerian base edge set \(z\) with \(\beta(z)=0\), traverse its Eulerian components, joining separate components by auxiliary paths traversed twice. The resulting closed base walk represents \(z\) modulo two and has zero monodromy, so it lifts to a closed walk upstairs. Its mod-two edge vector is a cycle of \(Q_n\) whose pushforward equals \(z\). Hence \(\ker\beta\) is generated by projections of cube squares.

For an even-monodromy turn cycle z, its moving-chain projection has zero base monodromy. It is therefore generated by projected coordinate squares. Subtract the associated turn cycles to land in the kernel of the line-graph projection, which Theorem 1 identifies with the span of star triangles. Conversely every listed generator has zero monodromy. One geodesic turn cycle has odd monodromy and supplies the remaining quotient generator. QED.

Let \(F\) be a connected finite simple graph, and define its *ordered-edge state graph* \(S(F)\) as follows: vertices are oriented edges \((u,v)\) of \(F\), and \((u,v)\) is adjacent to \((v,w)\) whenever \(u,v,w\) are pairwise distinct and \(\{u,v\},\{v,w\}\in E(F)\). The deck involution is reversal \(\tau(u,v)=(v,u)\), and the natural quotient map is
\[
\pi:S(F)\longrightarrow L(F),\qquad
(u,v)\longmapsto\{u,v\}.
\]
It is a regular two-sheeted graph covering; it need not be connected for an arbitrary \(F\). For \(F=K_n\), \(n\ge4\), the cover is connected.

Orient the edges of \(F\) arbitrarily. For each turn \(t\in E(L(F))\) between edges \(e,f\) incident at \(v\), let \(\kappa_F(t)=1\) if their reference orientations have equal incidence senses at \(v\), and let \(\kappa_F(t)=0\) otherwise. As in Article XI, the cohomology class of \(\kappa_F\) is independent of the reference edge orientations.

**Theorem 1 (ordered-edge covering classified by line-graph curvature).** The two-cover \(S(F)\to L(F)\) has covering-transition cochain \(\kappa_F\). In particular,
\[
\boxed{\beta_{S(F)/L(F)}=[\kappa_F]\in H^1(L(F);\mathbb F_2).}\tag{1}
\]

*Proof.* Represent a lifted state of an edge \(e\) by a sheet bit \(\varepsilon\), with zero indicating the chosen reference orientation and one indicating its reversal. Let \(h(e,v)\in\mathbb F_2\) be one if the reference orientation of \(e\) points into \(v\), and zero otherwise. The incidence sense of sheet \(\varepsilon\) at \(v\) is \(h(e,v)+\varepsilon\). Two lifted edge states representing incident edges \(e,f\) are adjacent in \(S(F)\) precisely when one points into their common vertex \(v\) and the other points out. Thus their sheet bits obey
\[
(h(e,v)+\varepsilon)+(h(f,v)+\varepsilon')=1,
\]
or
\[
\boxed{\varepsilon+\varepsilon'=1+h(e,v)+h(f,v)=\kappa_F(t).}
\]
This relation is the transition rule of the two-sheeted covering, proving (1). Reorienting reference edges adds a cut to the transition cochain and leaves its cohomology class unchanged. \(\square\)

**Corollary 2 (boundary monodromy is lower-level contact curvature).** Let \(n\ge4\), put \(F=K_n\), \(G=L(K_n)\), and \(H=L(G)=L^2(K_n)\). The connected double cover used for ordinary reversal-odd boundary tournaments is \(S(K_n)\to G\). Its induced line-graph covering \(L(S(K_n))\to H\) has monodromy
\[
\boxed{\alpha_{\mathrm{BT}}=\kappa_{K_n}\circ\Phi_{L(K_n)}
\quad\text{on }Z(L^2(K_n)),}\tag{2}
\]
where \(\Phi_{L(K_n)}:Z(L^2(K_n))\to Z(L(K_n))\) is the moving-cycle projection from the preceding Subsection.

*Proof.* Apply the naturality of covering monodromy under the moving-cycle projection, \(\alpha=\beta\circ\Phi_G\), from the preceding Theorem. Theorem 1 identifies \(\beta\) with the contact-curvature class \(\kappa_{K_n}\). \(\square\)

The cube and ordinary boundary-tournament pointed matroids thus have a shared signed-line-cover construction but different **origins of the monodromy port**: in the cube it records the global antipodal class of the folded cube; in the boundary construction it is the preceding line graph's local contact-curvature class. This explains the three-turn odd cycles in the boundary model and the dimension-growing odd girth in the cube, without claiming an automatic transfer of long resource-simple witnesses.

**Theorem 3 (three-level cycle-space generation for boundary tournaments).** Let \(n\ge4\), \(F=K_n\), \(G=L(F)\), and \(H=L(G)\). The two line-graph moving-cycle maps form a tower of surjections
\[
\boxed{Z(H)\xrightarrow{\Phi_G}Z(G)\xrightarrow{\Phi_F}Z(F),}\tag{3}
\]
whose kernels are the direct sums of their respective vertex-star clique cycle spaces. Consequently \(Z(H)\) is generated over \(\mathbb F_2\) by three classes:

(i) star triangles of \(H\), centered at the vertices of \(G\);

(ii) lifted turn cycles in \(H\) of star triangles of \(G=L(K_n)\), centered at original vertices of \(K_n\);

(iii) double-lifted turn cycles in \(H\) of ordinary triangles of \(K_n\).

On these three classes, the boundary covering monodromy \(\alpha_{\mathrm{BT}}\) takes the values \(0,1,0\), respectively.

*Proof.* The line-graph cycle-space sequence of the preceding Subsection applies first to \(G\), then to \(F\), giving the two maps and the stated kernels. An arbitrary cycle of \(H\) differs from a lift of its \(\Phi_G\)-image by a sum of type-(i) local star triangles. The \(\Phi_G\)-image in \(Z(G)\) differs from a lift of its image under \(\Phi_F\) by a sum of star triangles of \(G\); lifting those triangles to \(H\) gives type (ii). Finally \(F=K_n\), whose binary cycle space is generated by its ordinary triangles; twice lifting these gives type (iii). This proves spanning.

By Corollary 2, \(\alpha_{\mathrm{BT}}=\kappa_F\circ\Phi_G\). A top-level star triangle has \(\Phi_G=0\), so its monodromy is zero. A lifted type-(ii) triangle maps under \(\Phi_G\) to a star triangle of \(G\), and \(\kappa_F\) evaluates to one on every such triangle by the star-curvature identity. A type-(iii) double-lift projects to a simple cycle of \(F=K_n\), whose consecutive original edges contact distinct endpoints, so its contact-curvature is zero. These give the three claimed monodromy values. \(\square\)

**Corollary 4 (dimension and structural distinction).** The tower gives
\[
\boxed{\dim Z(L^2(K_n))=
\binom n2\binom{2n-5}{2}
+n\binom{n-2}{2}+\binom{n-1}{2}.}\tag{4}
\]
The first summand counts independent top-level star-clique cycles, the second independent lower-level star-clique cycles, and the third the dimension of the underlying complete-graph cycle space. Although the monodromy kernel in either canonical model has codimension one, the distinguished nonzero class is generated locally in the boundary model (a lifted lower-stage star triangle), but is generated by a global antipodal geodesic in the cube model after all star triangles and projected squares are factored out.

This tower is a useful test for prospective intrinsic matroid generalizations: cographic deletion and two-port signature algebra survive both constructions, yet the depth at which their nonzero covering class arises differs. A universal long-path theorem must therefore also control the marked coherent resource-independent galleries rather than merely the shortest cocircuit sector.

### Zero-turn contraction, pointed odd girth, and the cube geodesic distance defect

Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover, with induced connected turn cover over \(H=L(G)\). Let \(a\in C^1(H;\mathbb F_2)\) represent the covering-monodromy class. The pointed lift dual from Article XI is
\[
D=M\begin{pmatrix}B_H&0\\ a&1\end{pmatrix}^{*},
\tag{1}
\]
with distinguished port \(p\). Any deck-odd coloring gives \(d=a+\delta f\); its associated port-containing binary cycle is \(X_d=\operatorname{supp}(d)\cup\{p\}\).

The dependence on the coloring can be consolidated into a smaller **signed contraction graph**. This gives a full characterization of *unrestricted* port-cocircuit intersection and, in the cube, a metric distance defect whose vanishing is equivalent to NORI1.

#### 1. Zero-turn contraction and pointed odd girth

Define \(H_0(d)=(V(H),\{e:d(e)=0\})\), with all original vertices and only zero-turn edges. Contract each connected component of \(H_0(d)\) to one vertex; retain all edges \(e\) with \(d(e)=1\), including parallel edges and loops. Denote the resulting multigraph by \(K_d\). A loop has odd-girth contribution one. Let \(\operatorname{og}(K_d)\) denote the minimum edge count of an odd cycle, with \(+\infty\) if none exists.

**Theorem 1 (zero-turn odd-girth normal form).** For any deck-odd coloring and its pointed cycle \(X_d\),
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\p\in Y}}
|X_d\cap Y|
=1+\operatorname{og}(K_d).
}
\tag{2}
\]
The contracted graph \(K_d\) is nonbipartite (where loops count as odd cycles), so its odd girth is finite. More precisely, the contraction of the *primal* pointed matroid (1) by all zero-turn elements is represented, after elementary row operations, by
\[
\boxed{
\widehat M/H_0(d)\cong
M\begin{pmatrix}B_{K_d}&0\\ \mathbf1&1\end{pmatrix},
}
\tag{3}
\]
where \(\widehat M=D^*\), \(B_{K_d}\) is the incidence matrix of the contracted multigraph, and \(\mathbf1\) assigns one to each retained graph edge. The dual statement is deletion of the zero-turn elements from \(D\).

*Proof.* Replace the bottom row \(a\) in (1) by \(d=a+\delta f\) using vertex-incidence row operations. The columns corresponding to \(d=0\) then have bottom entry zero; contracting them identifies precisely the vertices in each connected component of \(H_0(d)\). The remaining columns represent \(B_{K_d}\) with bottom entry one, and the port still has bottom entry one, proving (3).

By the pointed covering representation, a port-containing cocircuit of \(D\) has the form \(Y_C=C\cup\{p\}\) for a simple cycle \(C\subseteq H\) with monodromy one, and
\[
|X_d\cap Y_C|=1+w_d(C),\qquad
w_d(C)=\sum_{e\in C}d(e),
\tag{4}
\]
where \(w_d\) is an integer. Since \(d\) represents monodromy, \(w_d(C)\) is odd.

Under the component contraction, \(C\) becomes a closed walk in \(K_d\) having \(w_d(C)\) edges: all zero turns have been contracted. Every odd closed walk contains an odd simple cycle, possibly a loop. Consequently
\(\operatorname{og}(K_d)\le w_d(C)\).

Conversely, take a shortest odd cycle of \(K_d\), of length \(g=\operatorname{og}(K_d)\). For each pair of its consecutive retained edges meeting at a contracted vertex, join their original endpoints by a path of zero turns inside the corresponding component of \(H_0(d)\). These zero paths and the \(g\) retained edges assemble a closed walk of \(H\) with odd monodromy and total integer turn weight \(g\). Split this closed walk into simple cycles, discarding paired traversals. Its mod-two turn sum is one, so at least one simple component has odd monodromy and weight at most \(g\). This gives a port cocircuit intersecting \(X_d\) in at most \(1+g\), proving (2).

Finally, if \(K_d\) were bipartite, its constant-one edge cochain would be a cut. Pulling that cut back through the zero-turn components would make \(d\) a cut of \(H\), contradicting the nonzero covering-monodromy class \(a\). Thus \(K_d\) has an odd cycle. \(\square\)

**Corollary 2 (single-disagreement loops).** A port cocircuit \(Y\) with \(|X_d\cap Y|=2\) exists if and only if \(K_d\) has a loop; equivalently, some positive-turn edge \(e=uv\) has both endpoints in the **same** connected component of \(H_0(d)\).

For the folded cube, the established nongeodesic monochromatic-antipodal-path theorem supplies this loop for every antipodally odd coloring. The open geodesic conjecture asks for a loop with a much stronger distance property.

#### 2. The cube zero-turn metric

Let \(n\ge4\), \(G_n=Q_n/\langle\tau\rangle\), \(H_n=L(G_n)\), and \(d\) be any deck-odd cube-edge coloring signature. Let
\[
\mathcal L_d=
\{\,e=uv\in E(H_n): d(e)=1,\ 
u,v\text{ lie in one component of }H_0(d)\,\}.
\tag{5}
\]
These are precisely the positive-turn edges that become loops of \(K_d\). For \(e=uv\in\mathcal L_d\), let \(\operatorname{dist}_{H_0(d)}(u,v)\) be their ordinary shortest-path distance using only zero-turn edges, and put
\[
\boxed{\ell_1(d)=
1+\min_{uv\in\mathcal L_d}
\operatorname{dist}_{H_0(d)}(u,v),}
\tag{6}
\]
taking \(+\infty\) when \(\mathcal L_d\) is empty.

**Theorem 3 (quantized geodesic distance defect).** When \(\mathcal L_d\ne\varnothing\), there exists an integer \(q_d\ge0\) such that
\[
\boxed{\ell_1(d)=n+2q_d.}
\tag{7}
\]
Moreover,
\[
\boxed{
\text{A full monochromatic antipodal geodesic exists}
\iff \ell_1(d)=n
\iff \min_{uv\in\mathcal L_d}\operatorname{dist}_{H_0(d)}(u,v)=n-1.
}
\tag{8}
\]
In particular, a hypothetical coloring refuting NORI1 must satisfy
\[
\boxed{
\operatorname{dist}_{H_0(d)}(u,v)\ge n+1
\quad\text{for EVERY }uv\in\mathcal L_d.
}
\tag{9}
\]

*Proof.* Every \(e=uv\in\mathcal L_d\), together with a shortest zero-turn path from \(u\) to \(v\), forms a simple turn cycle \(C_e\) with \(w_d(C_e)=1\). Thus \(\ell_1(d)\) is the minimum length of a simple odd-monodromy turn cycle containing precisely one positive-turn edge. Every odd-monodromy simple turn cycle in \(H_n\) has length at least \(n\), by the antipodal displacement bound of Article XI.

Choose such a cycle of minimum length, \(C\). If it contains a stationary edge state, the star-triangle shortening theorem permits deleting that state while retaining simplicity and odd monodromy. Its two incident turn labels are binary, and the shortcut label is their XOR. Since \(C\) contains only one positive-turn label, the integer turn cost of the shortened cycle is still one (it cannot be zero, by odd monodromy). This contradicts the minimum choice. Consequently \(C\) has no stationary contacts.

Its lifted edge-state sequence therefore represents a moving cube walk from \(x\) to \(x^*\), of length \(|C|=\ell_1(d)\). Each of the \(n\) coordinate directions appears an **odd positive** number of times in such a walk. Hence the length is \(n+2q_d\) for a nonnegative integer \(q_d\), proving (7).

If \(\ell_1(d)=n\), the lifted walk uses each coordinate once, so it is a full antipodal geodesic. Its cyclic turn word has one nonzero label; choose the root immediately after that turn, making all \(n-1\) internal turns zero. Conversely, a monochromatic full antipodal geodesic has precisely one cyclic nonzero turn (its closing seam, by reversal oddness); its turn cycle has length \(n\), showing \(\ell_1(d)\le n\). The antipodal lower bound forces equality. Formula (6) gives the remaining equivalence, and (7) gives (9) under the negation. \(\square\)

**Corollary 4 (explicit graph algorithm).** For a supplied cube coloring, the existence of a full monochromatic antipodal geodesic can be decided without enumerating \(n!\) coordinate permutations. Form \(H_0(d)\), find its connected components, and for every positive-turn edge \(uv\) internal to a zero component run a shortest-path search from \(u\) to \(v\) in \(H_0(d)\). A shortest path with \(n-1\) edges together with \(uv\) certifies a monochromatic antipodal geodesic. A direct implementation takes
\[
O\bigl(|E(H_n)|(|V(H_n)|+|E(H_n)|)\bigr)
\]
time and linear working space in the explicit turn graph. The method does not decide the all-dimensional conjecture uniformly; it decides the instance given by its complete edge coloring.

#### 3. What the contraction preserves and what it loses

Theorem 1 settles the **unrestricted minimum port-cocircuit intersection** as an odd-girth calculation after zero-turn contraction. But contraction discards both the number of zero turns used between positive turns and the moving-coordinate resources of the lift. A loop of \(K_d\) is therefore not necessarily a geodesic cocircuit: its shortest zero path can contain repeated moving directions, forcing a cycle of length \(n+2q_d\) with \(q_d>0\).

The distinction is now measured by the intrinsic nonnegative integer \(q_d\). Existing unrestricted port-two intersection results guarantee that \(q_d\) is finite for the cube. NORI1 is equivalent to \(q_d=0\). Any general matroid theorem proving that a point-loop of the zero-turn contraction can be **shortened to the covering-displacement distance** under the folded-cube exchange axioms would establish NORI1. The star-triangle shortening theorem removes stationary contacts but preserves moving-direction multiplicities; balanced hexagon exchanges alter the coordinate order but need not reduce the repeated-direction excess. Thus the remaining obstruction is a metric/resource defect, not a deficit of pointed-matroid parity.

#### 4. Intrinsic binary-matroid port-parallelism formulation

The graph contraction above is a special case of a matroid identity that does not assume a graph-cover representation.

**Lemma 5 (port-cocircuit intersection as a dual-minor circuit girth).** Let \(D\) be a finite matroid, \(p\in E(D)\), and \(X\subseteq E(D)\) with \(p\in X\). Put \(S=E(D)\setminus X\) and \(N=D^*/S\). Then
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\p\in Y}}
|X\cap Y|
=\min_{\substack{C\in\mathcal C(N)\\p\in C}}|C|.
}
\tag{10}
\]
Either minimum may be infinite if there is no relevant circuit or cocircuit.

*Proof.* Every circuit \(C\) of the contraction \(D^*/S\) lifts to a circuit \(Y\) of \(D^*\) with \(Y\setminus S=C\); this is the circuit description of matroid contraction. Hence the left-hand minimum is at most the right-hand minimum. Conversely, if \(Y\) is a circuit of \(D^*\) containing \(p\), then \(p\) lies in the closure of \(Y\setminus\{p\}\). After contracting \(S\), it still lies in the closure of \((Y\cap X)\setminus\{p\}\) in \(N\). Therefore a circuit \(C\) of \(N\) containing \(p\) exists inside \(Y\cap X\), and \(|C|\le|Y\cap X|\). This proves the reverse inequality. \(\square\)

**Corollary 6 (unrestricted two-intersection is parallelism).** If \(D\) is binary and \(X\in Z(D)\) contains \(p\), then \(p\) is **not a loop** of the contracted dual minor \(N=D^*/(E(D)\setminus X)\). Moreover
\[
\boxed{
\exists Y\in\mathcal C^*(D)\ (p\in Y,\ |X\cap Y|=2)
\iff
p\text{ belongs to a two-element parallel circuit of }N.
}
\tag{11}
\]
In the signed-cover representation, the parallel element is a positive-turn loop of \(K_d\): both its column and the port column of the contracted primal matrix (3) are \((0,\ldots,0,1)^\mathsf T\).

*Proof.* Binary cycle–cocircuit orthogonality forbids any one-element intersection of \(X\) with a cocircuit containing \(p\). Lemma 5 thus forbids a port loop in \(N\) and identifies intersection two with a two-element port circuit of \(N\). In (3), a positive graph loop has zero incidence column and bottom entry one, as does the port, proving the claimed correspondence. \(\square\)

This provides a fully matroid-intrinsic unrestricted two-intersection criterion, independent of shortest-cocircuit size. The remaining cube conjecture additionally asks that a corresponding lifted port cocircuit have size \(n+1\). The contraction minor forgets the lengths of its contracted zero-turn paths; Theorem 3 measures precisely that lost resource-length information by \(q_d\).

#### 5. Graphic-matroid fundamental circuits and a basis-selection form of NORI1

The distance defect of Theorem 3 can also be expressed using **basis exchange inside a graphic matroid**, without referencing a selected path. Let \(M_0=M(H_0(d))\), the cycle matroid of the zero-turn graph, and let \(\mathcal B_0\) be its set of spanning-forest bases. For \(T\in\mathcal B_0\) and a positive edge \(e=uv\in\mathcal L_d\), let \(C_T(e)\) be the unique fundamental circuit of \(e\) relative to \(T\) in the full graphic cycle matroid \(M(H_n)\). Equivalently, \(C_T(e)\) is \(e\) together with the unique tree path connecting its ends.

**Proposition 7 (basis-choice formula for the defect).** For any antipodally odd cube-edge coloring with \(\mathcal L_d\ne\varnothing\),
\[
\boxed{
\ell_1(d)=\min_{\substack{T\in\mathcal B_0\\e\in\mathcal L_d}}
|C_T(e)|,\qquad
q_d=\frac12\left(
\min_{\substack{T\in\mathcal B_0\\e\in\mathcal L_d}}|C_T(e)|-n
\right).
}
\tag{12}
\]
Consequently,
\[
\boxed{\text{NORI1 for this coloring}\iff
\exists\,T\in\mathcal B_0,\ e\in\mathcal L_d:\ |C_T(e)|=n.}
\tag{13}
\]

*Proof.* Every \(T\in\mathcal B_0\) joins the endpoints of every \(e\in\mathcal L_d\) by a zero-turn tree path, so \(|C_T(e)|-1\ge\operatorname{dist}_{H_0(d)}(u,v)\). Conversely, a shortest zero-turn path \(P\) from \(u\) to \(v\) is an independent set of the graphic matroid \(M_0\) and can be extended to a spanning-forest basis \(T\). Because \(T\) contains \(P\), its unique tree path between \(u,v\) is \(P\); thus \(|C_T(e)|=1+|P|\). Minimize over \(e\) and invoke Theorem 3. \(\square\)

This separates the proposed general matroid argument into two logically distinct steps. The unrestricted port intersection theorem supplies **parallelism after contracting all zero turns**, i.e. a positive \(e\) closing inside a zero component. The missing step is a compatible **basis selection** of that zero-turn component in which the mate \(e\) has a fundamental circuit of the covering-displacement length \(n\).

The latter property is stronger than ordinary matroid exchange or binary orthogonality: it compares a fundamental-circuit cardinality with the geometric displacement of the two-cover. Once that cardinality is \(n\), the cube's antipodal parity automatically forces each coordinate resource to occur once, so no further resource-independence hypothesis is needed in the cube model. For boundary tournaments, by contrast, a short port circuit need not use many original vertices, and the independent-resource path language must still be supplied separately.

#### 6. Chordless minimizers and simple moving cycles

The minimum-length one-disagreement cycle has a stronger structural property than the absence of stationary contacts.

**Theorem 8 (one-disagreement chord elimination).** Let \(H\) be a finite simple graph with a binary edge cochain \(d\). Among all simple cycles with integer turn weight
\[
w_d(C)=\sum_{e\in C}d(e)=1,
\]
choose a cycle \(C\) of minimum length. Then \(C\) is an **induced cycle of \(H\)**: there is no edge of \(H\) joining nonconsecutive vertices of \(C\). More generally, every one-disagreement simple cycle admits a sequence of strictly length-decreasing chord eliminations ending at an induced one-disagreement cycle.

*Proof.* Let \(h\) be a chord of a simple cycle \(C\) with \(w_d(C)=1\). The chord splits \(C\) into two strictly shorter simple cycles, using its two complementary arcs. Of the arcs, precisely one contains the unique positive-turn edge of \(C\). If \(d(h)=0\), choose the arc containing that edge; the resulting shorter cycle still has weight one. If \(d(h)=1\), choose the other arc, whose original edges all have cost zero; the chord contributes its unique positive edge. In both cases there is a shorter one-disagreement cycle. Iteration terminates and establishes the result. \(\square\)

**Corollary 9 (simple folded-cube core).** For the cube \(n\ge4\), a minimum-length monodromy-one cycle with one changed turn projects from \(H_n=L(G_n)\) to a **simple odd-monodromy cycle in \(G_n=Q_n/\tau\)**, whose lift is a self-avoiding path between antipodal vertices of \(Q_n\), with no two interior vertices related by the antipodal map. Its length is \(n+2q_d\).

*Proof.* Theorem 8 makes the turn cycle an induced cycle of \(L(G_n)\), of length at least \(n\ge4\). Any induced line-graph cycle of length at least four arises from a simple cycle of the base graph: consecutive edge-state vertices must meet at different endpoints of each base edge, else the preceding and following states are adjacent and create a chord. Moreover the contact vertices cannot repeat, since three or more selected edge states would then lie in the same base-vertex star clique, producing a chord of the induced cycle. Thus the moving walk is a simple base-graph cycle. Its monodromy is one, so its lifted path begins and ends at antipodal vertices, and no two distinct interior vertices project to the same base vertex. The direction-parity argument of Theorem 3 gives its length \(n+2q_d\). \(\square\)

**Example (why chordlessness alone does not close NORI1).** In every dimension \(n\ge4\), the following cube-vertex sequence, written as subsets of \([n]\), is a path from \(\varnothing\) to \([n]\):
\[
\varnothing,\ \{1\},\ \{1,2\},\ \{2\},\ \{2,3\},\
\{1,2,3\},\ \{1,2,3,4\},\ldots,[n].
\tag{14}
\]
Its direction sequence is \(1,2,1,3,1,4,5,\ldots,n\), of length \(n+2\). Its intermediate vertices have pairwise distinct antipodal orbits, so its projection is a simple monodromy-one cycle of length \(n+2\) in \(G_n\), corresponding to an induced turn cycle in \(H_n\). This is a geometric example, not an alleged NORI1 counterexample: prescribing one changed turn on this longer cycle does not rule out a monochromatic geodesic elsewhere.

Thus Theorem 8 removes all chord and stationary-contact defects from the shortest one-positive cocircuit, leaving **simple odd-voltage cycles of excess \(2q_d\)** as the sole geometric obstruction. A successful closure argument must exploit the cube's coordinate-square exchange structure to eliminate that positive excess; graph-theoretic chord shortening by itself is insufficient.

#### 7. Antipodal component-contact graph and port-parallel bundles

Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover with deck transformation \(\tau\), and let \(c:E(\widetilde G)\to\mathbb F_2\) be deck-odd, so \(c(\tau e)=1+c(e)\). Let \(R\) be the subgraph of color-zero covering edges, omitting isolated vertices; write \(R_1,\ldots,R_s\) for its edge-containing connected components. For a lifted vertex \(x\) incident with a red edge define \(\rho(x)=i\) by \(x\in R_i\), and put \(a_x=\deg_R(x)\), including \(a_x=0\) when no red edge is incident.

Construct the **antipodal component-contact multigraph** \(A_c\) with vertices \(R_1,\ldots,R_s\). For each pair \(\{x,\tau x\}\) with \(a_xa_{\tau x}>0\), place \(a_xa_{\tau x}\) parallel edges between \(R_{\rho(x)}\) and \(R_{\rho(\tau x)}\), allowing loops.

**Theorem 10 (component-contact realization).** Let \(K_d\) be the zero-turn contraction of the quotient line graph \(H=L(G)\) from Theorem 1. There is a canonical multigraph isomorphism
\[
\boxed{K_d\cong A_c.}\tag{15}
\]
In particular \(K_d\) is connected and nonbipartite. The entire contribution of a lifted vertex orbit is a single parallel edge bundle of cardinality
\[
\boxed{a_xa_{\tau x}=a_x(\deg_{\widetilde G}(x)-a_x).}\tag{16}
\]

*Proof.* Lift the zero-turn graph to \(L(\widetilde G)\). Its edges join incident covering edges of the same color, so its connected components are the line graphs of the monochromatic edge components. The deck transformation exchanges colors and pairs \(R_i\) with the color-one component \(\tau R_i\); the quotient zero-turn components are therefore indexed by red components \(R_i\). A positive turn at \(x\) joins a red covering edge at \(x\) to a blue covering edge at \(x\). The latter is the deck image of a red covering edge at \(\tau x\). Its two quotient components are \(R_{\rho(x)}\) and \(R_{\rho(\tau x)}\). Every choice of one red edge at each antipodal endpoint specifies one positive-turn orbit, and no orbit is counted twice since \(x,\tau x\) are one base vertex. This gives \(a_xa_{\tau x}\) parallel edges and exhausts the positive turns. Theorem 1 gives connectedness and nonbipartiteness. Deck oddness implies \(a_{\tau x}=\deg_{\widetilde G}(x)-a_x\). \(\square\)

**Corollary 11 (large parallel bundles).** If the covering graph has minimum degree \(m\ge3\), every edge of \(K_d\) belongs to a parallel bundle containing at least \(m-1\) elements. Every nonloop edge lies in a two-edge cycle; hence \(K_d\) has no bridges.

*Proof.* Both factors in a nonempty bundle are positive integers summing to a degree at least \(m\), so their product is at least \(m-1\). Each bundle consists of edges with the same two endpoints. \(\square\)

**Corollary 12 (loop characterization and port-parallel amplification).** The graph \(K_d\) has a loop if and only if some color-zero edge component \(R_i\) contains an antipodal pair \(x,\tau x\). More precisely, an edge contributed by the vertex orbit \(\{x,\tau x\}\) is a loop if and only if \(\rho(x)=\rho(\tau x)\). Such a vertex orbit contributes at least \(m-1\) distinct loops when the minimum degree is \(m\ge3\). In the primal pointed contraction of Theorem 1, these loop columns are all identical to the port column, so the port has at least \(m-1\) parallel mates.

*Proof.* The edge corresponding to \(\{x,\tau x\}\) is a loop if and only if \(\rho(x)=\rho(\tau x)\). In the contracted incidence-plus-monodromy matrix, a graph loop has zero incidence column and bottom entry one, as does the distinguished port. Apply Corollary 11. \(\square\)

**Lemma 13 (monochromatic antipodal metric).** In the cube cover,
\[
\boxed{
\ell_1(d)=
\min_{\substack{x\in Q_n,\ \varepsilon\in\{0,1\}\\
x,\tau x\text{ joined by an }\varepsilon\text{-colored path}}}
\operatorname{dist}_{G_\varepsilon}(x,\tau x),
}\tag{17}
\]
where \(G_\varepsilon\) is the spanning subgraph of cube edges of color \(\varepsilon\), and the distance is measured inside that monochromatic subgraph.

*Proof.* Any monochromatic antipodal path gives a turn walk of zero internal cost and one positive closing turn, hence an odd-monodromy turn walk of no larger length. Splitting it into simple cycles yields a one-positive simple cycle and proves \(\ell_1(d)\) is no larger than the monochromatic distance. Conversely, Theorem 3 shortens a minimum one-positive turn cycle to a moving stationary-free cycle, which lifts to a monochromatic cube path between antipodal vertices of length \(\ell_1(d)\). \(\square\)

**Proposition 14 (uniform near-short circuits within one loop bundle).** Suppose \(x,\tau x\) belong to the same color-zero component \(R_i\), and put \(L_x=\operatorname{dist}_{R_i}(x,\tau x)\). Every one of the \(a_xa_{\tau x}\) loop elements from the orbit \(\{x,\tau x\}\) belongs to a port cocircuit \(Y\) such that
\[
\boxed{|Y|\le L_x+3,\qquad |X_d\cap Y|=2.}\tag{18}
\]
These cocircuits are distinct for distinct loop edges. Consequently, for a cube coloring whose minimum monochromatic antipodal distance is \(\ell_1(d)=n+2q_d\), at least \(n-1\) distinct port cocircuits have intersection two and size at most \(n+2q_d+3\).

*Proof.* Let \(P\) be a shortest red \(x\)-to-\(\tau x\) path of length \(L_x\). Its edge states form a zero-turn path of length \(L_x-1\). Replace its initial edge by any other red edge incident at \(x\), and its terminal edge by any other red edge incident at \(\tau x\); these replacements add at most one zero turn each. Thus every pair of red incident edges at \(x,\tau x\) is joined by a zero-turn walk of length at most \(L_x+1\) in the quotient state graph. Close it by its associated positive-turn element (one of the loop bundle), and shorten the zero walk to a simple zero path. The result is a simple odd-monodromy cycle of length at most \(L_x+2\) with one positive turn. Adding the port gives (18); its positive-turn element identifies it uniquely. Take an antipodal pair attaining Lemma 13 and apply the cube degree \(m=n\) to obtain the multiplicity assertion. \(\square\)

The contact-graph structure is significantly more restrictive than an arbitrary nonbipartite multigraph: each edge belongs to a large parallel bundle, and a self-contact component yields many port-parallel elements with uniformly bounded circuit-length spread. Nevertheless, a loop is a certificate of monochromatic antipodal **connectivity**, not necessarily of a geodesic. The unresolved geometric condition is \(L_x=n\) for some self-contact, which would force zero directional excess and close NORI1.

#### 8. Eulerian conservation in the antipodal contact minor

Regularity of the covering graph imposes a second global constraint on \(K_d\), beyond the large parallel bundles in Corollary 11.

**Theorem 15 (Eulerian contact conservation).** Suppose \(\widetilde G\to G\) is a connected regular two-cover, \(\widetilde G\) is \(m\)-regular, and \(c(\tau e)=1-c(e)\). Then the contracted antipodal component-contact multigraph \(K_d\) of Theorem 10 is **Eulerian**:
\[
\boxed{\deg_{K_d}(R_i)\equiv0\pmod2\qquad
\text{for every color-zero edge component }R_i.}
\tag{19}
\]
More precisely,
\[
\boxed{
\deg_{K_d}(R_i)
=\sum_{x\in V(R_i)}a_x(m-a_x),\qquad
a_x=\deg_{R_i}(x).
}
\tag{20}
\]
Loops contribute two to the graph degree.

If \(m\) is odd, every *individual local parallel bundle* has even cardinality. If \(m\) is even, a local bundle has odd cardinality precisely when \(a_x\) is odd; the collection of odd-cardinality bundles, considered modulo two on the contact graph, forms an Eulerian subgraph.

*Proof.* A base vertex orbit \(\{x,\tau x\}\) contributes \(a_xa_{\tau x}\) edges between the red components containing \(x\) and \(\tau x\), by Theorem 10. Its contribution to the degree of a red component is \(a_xa_{\tau x}\) for each endpoint \(x\) of that orbit lying in the component; if both antipodal endpoints belong to it, the bundle is a loop and the contribution is counted twice. Summing the contributions over all vertices of \(R_i\) gives (20), since deck oddness and \(m\)-regularity yield \(a_{\tau x}=m-a_x\).

Working modulo two, \(a_x(m-a_x)\equiv(m-1)a_x\), because \(a_x^2\equiv a_x\pmod2\). The degree-sum identity inside \(R_i\) gives \(\sum_{x\in V(R_i)}a_x=2|E(R_i)|\equiv0\pmod2\). Therefore (20) is even, proving (19). For odd \(m\), the positive integers \(a_x\) and \(m-a_x\) have opposite parity and their product is even. For even \(m\), the product has the parity of \(a_x\); the already-proved even-degree condition says the odd-bundle edge set has even degree at every contact-graph vertex. \(\square\)

**Corollary 16 (common Eulerian-port-minor axiom).** The cube cover \(Q_n\to Q_n/\tau\) is \(n\)-regular. The ordered-pair cover used for ordinary boundary 3-tournaments, \(S(K_n)\to L(K_n)\), is \(2(n-2)\)-regular. Thus **both** canonical Article XI signed turn models yield Eulerian zero-turn contractions for every reversal-odd coloring. The cube additionally has even local parallel multiplicities in odd dimensions; the boundary model always lies in the even-degree branch.

In matroid language, the entire positive-turn edge multiset of \(K_d\) is a cycle of its graphic matroid \(M(K_d)\). The parity reduction of local parallel bundles is itself an Eulerian cycle. Consequently a proposed abstract common class may require an Eulerian contact minor, quantitative parallel bundles, and a distinguished port-parallel loop whose lifted fundamental circuit has covering-displacement length. The first two properties are theorems for all regular two-covers; the last is the unresolved NORI1 selector.

**Limitation.** A connected nonbipartite Eulerian multigraph with all nonloop edges in large parallel classes need not have any loops: an odd cycle with each edge replaced by two parallel edges is a counterexample to that implication. Therefore regularity and Eulerian parity alone cannot replace the cube-specific antipodal connectivity theorem, much less guarantee a length-\(n\) loop lift. These restrictions nevertheless exclude most arbitrary pointed binary matroids and supply a useful common structural hypothesis for future matroid generalizations.

#### 9. Global contact-edge parity as a covering-cohomology evaluation

The Eulerian conservation law has a global counterpart. Let \(\beta\in H^1(G;\mathbb F_2)\) denote the monodromy class of a connected regular two-cover \(\widetilde G\to G\), where \(G\) is \(m\)-regular. The number of nonzero-turn edges is
\[
|E(K_d)|=\sum_{v\in V(G)}a_v(m-a_v),
\tag{21}
\]
with \(a_v\) the number of red covering edges incident with either selected lift of \(v\).

**Theorem 17 (covering-cohomology edge-parity identity).** If \(m\) is odd, then \(|E(K_d)|\) is even for every deck-odd coloring. If \(m\) is even, the all-edge set \(E(G)\) is a binary cycle of \(G\), and
\[
\boxed{
|E(K_d)|\equiv
\left\langle\beta,\ E(G)\right\rangle
\pmod2.
}
\tag{22}
\]
Thus for an even-regular quotient, the parity of the total changed-turn set depends only on the covering, **not** on the deck-odd coloring.

*Proof.* Fix one reference lift \(s(v)\) of every base vertex, and represent the covering by a binary edge-voltage cochain \(\alpha\): it is one on a base edge \(uv\) precisely when its lift from \(s(u)\) meets \(\tau s(v)\). Let \(a_v\) count red edges incident with \(s(v)\). Modulo two, \(a_v(m-a_v)\equiv(m-1)a_v\).

For each base edge \(uv\), the deck-odd coloring chooses one of its two covering-edge lifts to be red. If \(\alpha(uv)=0\), this chosen red lift is incident with either both reference endpoints \(s(u),s(v)\) or neither, and contributes zero modulo two to \(\sum_v a_v\). If \(\alpha(uv)=1\), it is incident with precisely one reference endpoint and contributes one, independently of which lift is red. Summing over all base edges gives
\[
\sum_{v\in V(G)}a_v\equiv\sum_{e\in E(G)}\alpha(e)\pmod2.
\]
If \(m\) is odd, the coefficient \(m-1\) vanishes modulo two. If \(m\) is even, the all-edge set is Eulerian; the right-hand sum is the well-defined pairing of covering cohomology with the all-edge cycle, proving (22). \(\square\)

**Corollary 18 (even contact-edge count for both canonical models).** For every antipodally odd \(n\)-cube edge coloring with \(n\ge3\), and for every ordinary reversal-odd boundary 3-tournament on \(n\ge4\) vertices,
\[
\boxed{|E(K_d)|\equiv0\pmod2.}
\tag{23}
\]

*Proof.* If the cube dimension \(n\) is odd, Theorem 17 applies immediately. If \(n\ge4\) is even, choose the sheet of the folded-cube covering whose first coordinate is zero. The voltage is one precisely on quotient edges of direction one; their number is \(2^{n-2}\), which is even. Thus the cohomology pairing in (22) vanishes.

For boundary tournaments the ordered-pair cover \(S(K_n)\to L(K_n)\) has degree \(m=2(n-2)\), and its covering class is the canonical contact-curvature class \(\kappa_{K_n}\), established in the monodromy-tower Subsection. Orient \(K_n\) transitively with vertices \(0,1,\ldots,n-1\). At vertex \(v\) there are \(v\) incoming and \(n-1-v\) outgoing edges, and curvature one occurs on pairs with the same incidence sense. Summing the curvature over all edges of \(L(K_n)\) therefore gives
\[
\sum_{v=0}^{n-1}\left[
\binom v2+\binom{n-1-v}2
\right]
=2\binom n3\equiv0\pmod2.
\]
Apply Theorem 17. \(\square\)

Theorems 15 and 17 identify a pair of common matroidal constraints: the entire positive-turn edge multiset is an Eulerian cycle in the graphic matroid of the contact graph, and it has even cardinality. Equivalently, its evaluation under the constant-one edge functional is zero. These conditions survive arbitrary deck-odd recoloring in both canonical systems. They do not force a length-\(n\) lift of a port-parallel loop; that additional metric selection is the remaining obstruction to NORI1.

#### 10. Endpoint-star tree certificate and rank amplification

The preceding results measure a hypothetical defect \(q_d>0\) by the length of a monochromatic antipodal path. The regular cubical endpoint stars force that metric defect to appear as **graphic rank** in the corresponding monochromatic component.

**Theorem 19 (endpoint-star independent-tree bound).** Let \(c\) be any antipodally odd two-coloring of \(E(Q_n)\), \(n\ge3\), and suppose \(x\) and \(x^*\) belong to one monochromatic component \(R\). Let \(P=(v_0=x,v_1,\ldots,v_L=x^*)\) be a *shortest* monochromatic path between these two endpoints, where \(L\ge n\). Then the union of \(P\) with **all monochromatic edges incident to either endpoint** is a tree having
\[
\boxed{L+n-2\text{ edges and }L+n-1\text{ vertices}.}
\tag{24}
\]
In particular, writing \(M(R)\) for the graphic cycle matroid of the monochromatic component,
\[
\boxed{\operatorname{rank}M(R)=|V(R)|-1\ge L+n-2.}
\tag{25}
\]

*Proof.* If a monochromatic edge joined \(v_0\) to a later path vertex \(v_j\) with \(j\ge2\), replacing the initial \(j\) path edges by this edge would shorten the monochromatic path from \(x\) to \(x^*\), contradicting minimality. The same argument at \(v_L\) shows that its only monochromatic neighbor on \(P\) is \(v_{L-1}\). By deck oddness, the monochromatic endpoint degrees satisfy
\[
\deg_c(x)+\deg_c(x^*)=n,
\]
because each coordinate-direction edge at \(x\) is paired with the oppositely colored edge at \(x^*\). The \(n\) endpoint-neighbor vertices are all distinct for \(n\ge3\): the neighbors of \(x\) and \(x^*\) belong to Hamming layers one and \(n-1\), respectively. Among those \(n\) monochromatic endpoint-neighbor vertices, only \(v_1\) and \(v_{L-1}\) belong to \(P\). Every other endpoint red edge therefore attaches a new leaf to \(P\), and there are \(n-2\) such edges. The resulting union is a tree with the asserted sizes. It is a graphic independent set in \(M(R)\), so the rank inequality follows. \(\square\)

**Corollary 20 (rank cost of cubical geodesic defect).** Let \(\ell_1(c)=n+2q_d\) be the shortest monochromatic antipodal-path length from Theorem 3, and let \(R\) be a monochromatic component containing a pair achieving this length. Then
\[
\boxed{
|V(R)|\ge 2n+2q_d-1,\qquad
\operatorname{rank}M(R)\ge2n+2q_d-2.
}
\tag{26}
\]
Consequently, **if every monochromatic component containing an antipodal pair has fewer than \(2n+1\) vertices, then NORI1 holds for that coloring.** Conversely, a hypothetical counterexample to NORI1 must have every such component of order at least \(2n+1\).

*Proof.* Substitute \(L=n+2q_d\) into Theorem 19; if \(q_d>0\), integrality makes \(q_d\ge1\), giving the threshold. For another self-contact component the same argument uses its own shortest antipodal distance, which is no smaller than \(\ell_1(c)\). \(\square\)

Theorem 19 is a useful graphic-matroid rank constraint on any port-parallel bundle: a self-contact loop with shortest lift of length \(n+2q\) can occur only in a monochromatic component carrying an independent tree of rank at least \(2n+2q-2\). The proof uses the combination of shortest-path chordlessness and complementary antipodal endpoint stars, not binary parity alone.

**Scope.** The rank bound by itself does not force \(q=0\). A partial monochromatic subgraph can contain a length-\(n+2\) antipodal path, both complementary endpoint stars, and no shorter path between its chosen endpoints, with \(2n+1\) vertices. Extending such a partial subgraph to a full deck-odd coloring may create additional monochromatic antipodal geodesics elsewhere. Thus Theorem 19 supplies a rigorous rank barrier for a hypothetical counterexample but not its exclusion.

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

Let \(W\subseteq\mathbb F_2^E\) be any binary linear code containing a vector of odd Hamming weight, with standard overlap pairing
\[
\langle x,y\rangle=|x\cap y|\pmod2.
\]
Put
\[
\beta=\dim W,\quad R=W\cap W^\perp,\quad b=\dim R,\quad
K=\{x\in W:|x|\equiv0\pmod2\}.
\]
Since \(W\) has an odd-weight vector, \(K\) is a hyperplane in \(W\); on \(K\) the overlap pairing is alternating.

**Theorem 1 (bicycle-rank formula for binary codes).** The rank of the alternating pairing restricted to \(K\) is
\[
\boxed{\operatorname{rank}\bigl(\langle\cdot,\cdot\rangle|_K\bigr)
=2\left\lfloor\frac{\beta-b-1}{2}\right\rfloor.}\tag{1}
\]
In particular, no further invariant of the binary code is needed to determine this rank.

*Proof.* Every \(r\in R\) has even weight, since \(\langle r,r\rangle=0\), so \(R\subseteq K\). Pass to \(\overline W=W/R\), whose induced symmetric bilinear pairing is nondegenerate and whose dimension is \(d=\beta-b\). Its diagonal map
\[
\ell(x)=\langle x,x\rangle=|x|\pmod2
\]
is a nonzero linear functional, and \(\overline K=K/R=\ker\ell\) has dimension \(d-1\).

By nondegeneracy there is a unique characteristic vector \(h\in\overline W\) satisfying \(\langle h,x\rangle=\ell(x)\) for every \(x\). A symmetric bilinear form over \(\mathbb F_2\) decomposes orthogonally into one-dimensional odd lines and hyperbolic alternating planes. In such a decomposition, \(h\) is the sum of the unit generators of the odd lines. Therefore
\[
\langle h,h\rangle=\dim\overline W=d\pmod2.
\]
The orthogonal complement of \(\overline K\) in \(\overline W\) is \(\langle h\rangle\). Hence the radical of the restriction to \(\overline K\) is zero if \(d\) is odd, and is \(\langle h\rangle\) of dimension one if \(d\) is even. Its rank is consequently \(d-1\) when \(d\) is odd, or \(d-2\) when \(d\) is even; both equal \(2\lfloor(d-1)/2\rfloor\). Since \(R\) is the radical of the pairing on \(W\), restricting from \(K\) to \(K/R\) does not change rank. Substituting \(d=\beta-b\) proves (1). \(\square\)

The dimension \(b\) is the **bicycle dimension** of the code: it measures the overlap of its linear subspace with its orthogonal complement. Theorem 1 applies to arbitrary binary matroid cycle spaces and not merely to graph-cover representations.

#### Application to the monochromatic-component quotient

Let \(H\) be the turn graph of a connected two-sheeted graph cover, and let \(d\) be an admissible deck-odd turn signature. As in the preceding Subsection, contract the zero-turn connected components of \(H\) to form the connected multigraph \(J=J_d\), whose edges are precisely the changed turns. Because its edge-count parity measures covering monodromy and the latter is nonzero, the graph \(J\) has an odd cycle. Put
\[
\beta(J)=|E(J)|-|V(J)|+1,\qquad
b(J)=\dim\bigl(Z(J)\cap Z(J)^\perp\bigr),
\]
where the orthogonal complement is the cut space of \(J\). Let \(r_d\) be half the polar rank of the quadratic half-intersection form on port-free cocycles of the pointed lift.

**Theorem 2 (Tutte–bicycle formula for port intersection).** With this notation,
\[
\boxed{
2r_d=2\left\lfloor\frac{\beta(J)-b(J)-1}{2}\right\rfloor.}\tag{2}
\]
Equivalently, the port-cocycle quadratic rank is determined by the graph cycle rank and the bicycle dimension of \(J\). By the Rosenstiehl–Read evaluation of the Tutte polynomial,
\[
\boxed{|T_J(-1,-1)|=2^{b(J)},}\tag{3}
\]
and therefore one can recover the polar rank from \(\beta(J)\) and \(T_J(-1,-1)\).

*Proof.* The preceding monochromatic-component quotient theorem identifies the port-free cocycle space, modulo cycles of zero-turn edges, with the even-cardinality subspace \(K\) of \(Z(J)\). Its polar form is precisely the standard binary edge-overlap pairing on \(K\), and the quotient kernel has zero polar pairing against the entire port-free space. Consequently the two polar ranks agree. Apply Theorem 1 to \(W=Z(J)\), which contains odd-weight vectors, with radical dimension \(b(J)\). Equation (3) is the classical Rosenstiehl–Read identity. \(\square\)

**Corollary 3 (three-value modular distribution).** Set
\[
r=\left\lfloor\frac{\beta(J)-b(J)-1}{2}\right\rfloor.
\]
For a uniformly sampled port-containing binary cocycle \(Y\), the probability that
\(|X_d\cap Y|\equiv2\pmod4\) belongs to the three-element set
\[
\boxed{
\left\{\frac12,\quad
\frac12-2^{-r-1},\quad
\frac12+2^{-r-1}\right\}.}\tag{4}
\]
It is not merely bounded by this interval.

*Proof.* In the affine coset of port-containing cocycles, the half-intersection function is quadratic with polar rank \(2r\). Its sign sum is zero when its affine-linear restriction to the radical is nontrivial; otherwise it has absolute value \(2^{-r}\) times the size of the affine coset. This is the standard quadratic Gauss-sum calculation, also proved by squaring the sign sum in the previous Subsection. Dividing by the coset size yields (4). \(\square\)

For a connected graph, the bicycle dimension can also be determined by the nullity of the binary graph Laplacian: \(b(J)=\dim\ker L_J-1\). Consequently the complete modular-distribution bound is computable by binary Gaussian elimination on the monochromatic-component quotient, without enumerating cocircuits or colorings.

#### Intrinsic pointed-matroid restriction theorem

Let \(M\) be a finite binary matroid, let \(p\) be a nonloop element, and let \(X\in Z(M)\) be a binary cycle containing \(p\). Put \(S=X\setminus\{p\}\) and let
\[
N=M|S
\]
be the restriction minor of \(M\) to \(S\). Define the binary bicycle dimension of \(N\) by
\[
b(N)=\dim\bigl(Z(N)\cap Z^*(N)\bigr),
\]
and write \(r(N)\) for the rank of \(N\).

**Theorem 4 (universal pointed intersection-rank formula).** On the port-free cocycle space
\[
K_p=\{Y\in Z^*(M):p\notin Y\},
\]
let
\[
B_X(Y,Z)=|X\cap Y\cap Z|\pmod2.
\]
Then
\[
\boxed{
\operatorname{rank}(B_X|_{K_p})
=2\left\lfloor\frac{r(N)-b(N)-1}{2}\right\rfloor.
}\tag{5}
\]
By the bicycle-space evaluation (Rosenstiehl–Read for graphs, extended to binary matroids by Jaeger, European J. Combin. 10 (1989), 247–255),
\[
\boxed{|T_N(-1,-1)|=2^{b(N)},}\tag{6}
\]
so the polar rank is determined solely by the rank and Tutte polynomial of the restriction minor \(N\). In particular, this quadratic invariant does not require a graph, a line-graph cover, a distinguished cocircuit length, or an admissible resource-path language.

*Proof.* Represent \(M\) over \(\mathbb F_2\) by a matrix \(A\). The binary cocycle space is the row space of \(A\), and coordinate restriction to \(S\) maps it surjectively onto the row space of \(A|S\), which is precisely \(Z^*(N)\). Denote this surjection by \(\rho\).

Because \(X\) is a binary cycle, cycle–cocycle orthogonality gives
\[
\mathbf1_Y(p)=|Y\cap S|\pmod2
\quad\text{for all }Y\in Z^*(M).
\tag{7}
\]
Thus \(\rho(K_p)\) equals the even-cardinality subspace
\[
K=\{z\in Z^*(N):|z|\equiv0\pmod2\}.
\]
Since \(p\) is a nonloop, some cocycle contains \(p\); by (7), \(Z^*(N)\) contains an odd-weight vector, and \(K\) is a hyperplane. The map \(\rho|_{K_p}\) is surjective onto \(K\), and its kernel has zero overlap pairing against every cocycle because all of its coordinates on \(S\) vanish. Therefore the polar rank on \(K_p\) equals the rank of the standard binary overlap form restricted to \(K\).

The full code \(W=Z^*(N)\) has dimension \(\beta=r(N)\), and its orthogonal complement is \(Z(N)\). Its radical hence has dimension \(b(N)\). Apply Theorem 1 to \(W\), giving precisely (5). The identity (6) is the classical bicycle-space evaluation of the Tutte polynomial, which holds for binary matroids. \(\square\)

**Corollary 5 (universal modular spectrum from a restriction minor).** Let
\[
r=\left\lfloor\frac{r(N)-b(N)-1}{2}\right\rfloor.
\]
Among all binary cocycles of \(M\) containing \(p\), the proportion meeting \(X\) in cardinality congruent to two modulo four belongs to
\[
\boxed{\left\{\frac12,\ \frac12-2^{-r-1},\
\frac12+2^{-r-1}\right\}.}\tag{8}
\]

*Proof.* The half-intersection quadratic function on the affine port-containing cocycles factors through the odd-weight coset of \(Z^*(N)\), by (7). Its polarization has rank \(2r\) by Theorem 4; the quadratic Gauss-sum dichotomy from Corollary 3 gives the stated three-value spectrum. \(\square\)

The theorem is a purely pointed-binary-matroid statement and is thus directly suitable for testing candidate intrinsic generalization classes. It also identifies a sharp limitation: modular intersection balance of *all* port-containing cocycles is governed by a restriction minor and need not impose any condition on minimum-size cocircuits or on the resource simplicity of their graph-cover witnesses.

**Corollary 6 (bicycle-corrected cycle-rank inequality).** In any signed line-graph cover with admissible turn cochain \(d\), put \(S=\operatorname{supp}(d)\), let \(r_0\) be the number of zero-turn connected components, and let \(J_d\) be the resulting connected multigraph on those components. If \(R(d)\) denotes the sum of the local star-cut polar ranks from the preceding Subsection, then
\[
\boxed{|S|-r_0\ge b(J_d)+R(d).}\tag{9}
\]
Thus the local quadratic mixing requires not merely global cycle rank but cycle rank *beyond the graph's bicycle space*.

*Proof.* The preceding local star theorem gives a lower bound \(R(d)\) for the polar rank of the port-free cocycle quadratic. By Theorem 2 this rank equals \(2\lfloor(\beta-b-1)/2\rfloor\), where \(\beta=|S|-r_0+1\) and \(b=b(J_d)\). Therefore
\[
R(d)\le 2\left\lfloor\frac{|S|-r_0-b}{2}\right\rfloor
\le |S|-r_0-b,
\]
which is (9). \(\square\)

**Corollary 7 (Laplace–Tutte computational interpretation).** For connected \(J_d\), its binary Laplacian satisfies
\[
b(J_d)=\dim\ker_{\mathbb F_2} L_{J_d}-1.
\]
Hence the quantity on the right side of (9) and the complete three-value modular spectrum can be computed by binary matrix rank calculations on the monochromatic-component quotient. When the number of spanning trees of \(J_d\) is odd, the bicycle dimension is zero; equivalently \(|T_{J_d}(-1,-1)|=1\).

*Proof.* A bicycle is a cut vector \(\partial^Tf\) that also lies in \(\ker\partial\); this is equivalent to \(L_{J_d}f=\partial\partial^Tf=0\). The map \(f\mapsto\partial^Tf\) has one-dimensional kernel for connected \(J_d\), yielding the displayed dimension identity. The matrix-tree theorem over \(\mathbb F_2\) identifies odd spanning-tree count with invertibility of a reduced Laplacian, which is equivalent to one-dimensional kernel of the full Laplacian and thus to \(b(J_d)=0\). \(\square\)

### Discrete Hodge stability and the asymptotically sharp two-thirds turn theorem

Let \(V_n\) denote the real functions on distinct ordered triples satisfying \(f(c,b,a)=-f(a,b,c)\). Use one representative of each reversal pair for the inner product, and write \(N=n\binom{n-1}{2}\), \(E=N(n-3)\). Recall from the preceding signed-adjacency theorem the self-adjoint operator
\[
(Af)(a,b,c)=\sum_{d\notin\{a,b,c\}}[f(b,c,d)+f(d,a,b)]
\]
with spectrum contained in \(\{-(n-2),-2,0,1,n-2\}\), for \(n\ge6\).

**Lemma 1 (minimum eigenspace).** The eigenspace at \(-(n-2)\) is
\[
\mathcal E_-=\{f_s(a,b,c)=s_{ab}-s_{bc}:s_{ab}=s_{ba},\quad
\sum_{b\ne a}s_{ab}=0\ \forall a\}. \tag{1}
\]
It has dimension \(n(n-3)/2\), and is contained in
\[
\mathcal G=\{f:f(a,b,c)=u_b(a)-u_b(c)\}, \tag{2}
\]
the direct sum of gradient spaces on the neighbor sets of the \(n\) centers.

*Proof.* For any \(f\in V_n\), set
\[
U_{ab}=\sum_{d\notin\{a,b\}}f(d,a,b),\quad
H_{ab}=\sum_{d\notin\{a,b\}}f(a,d,b),\quad
W_a=\sum_{c\ne a}U_{ca},
\quad \sigma(a,b,c)=f(a,b,c)+f(b,c,a)+f(c,a,b).
\]
Here \(H_{ba}=-H_{ab}\), \(\sigma\) is alternating, and \(\sum_{b\ne a}U_{ab}=0\). Rearrangement gives
\[
Af=f-\sigma+U_{ab}-U_{cb},\qquad
U(Af)_{ab}=W_a+H_{ab}-(n-2)U_{ba}. \tag{3}
\]
Suppose \(Af=-rf\), with \(r=n-2\). The second equation gives
\(H_{ab}=r(U_{ba}-U_{ab})-W_a\).
Antisymmetry of \(H\) forces \(W_a=-W_b\) for every \(a\ne b\), hence every \(W_a=0\).
From the first equation,
\[
(r+1)f(a,b,c)=\sigma(a,b,c)-U_{ab}+U_{cb}. \tag{4}
\]
Summing (4) over \(f(a,d,b)\), and using the zero row sums of \(U\) and
\(\sum_d\sigma(a,d,b)=-(U_{ab}-U_{ba}-H_{ab})\), yields
\((r+1)H_{ab}=H_{ab}\). Thus \(H=0\), so \(U\) is symmetric. Cyclically summing (4) then gives \((r+1)\sigma=3\sigma\). Since \(n\ge6\), \(\sigma=0\). Equation (4) becomes \(f(a,b,c)=(-U_{ab}+U_{bc})/(n-1)\), establishing (1) with \(s=-U/(n-1)\).
Conversely, the stated symmetric zero-row-sum \(s\) satisfies
\(U_{ab}=-(n-1)s_{ab}\), \(\sigma=0\), and consequently \(Af_s=-(n-2)f_s\) by (3). The \(n\) row-sum constraints on the \(\binom n2\) symmetric edge variables are independent, and \(s\mapsto f_s\) is injective, giving the dimension. \(\square\)

For an antisymmetric edge array \(z_{ac}\) on \(K_m\), write \(\operatorname{div}_a z=\sum_{c\ne a}z_{ac}\) and
\(\gamma_{acd}=z_{ac}+z_{cd}+z_{da}\).

**Lemma 2 (complete-graph Hodge identity).** Orthogonal projection onto the gradients \(z_{ac}=u_a-u_c\) satisfies
\[
(\Pi z)_{ac}=\frac{\operatorname{div}_a z-\operatorname{div}_c z}{m},\qquad
\sum_{\{a,c,d\}}\gamma_{acd}^{\,2}=m\|z-\Pi z\|^2. \tag{5}
\]
*Proof.* Expand the squares:
\(\sum_{\triangle}\gamma^2=m\sum_{\{a,c\}}z_{ac}^2-\sum_a(\operatorname{div}_a z)^2\).
The displayed projection has squared norm \(\frac1m\sum_a(\operatorname{div}_a z)^2\), proving (5). \(\square\)

**Theorem 3 (sharp asymptotic turn density with stability).**
Let \(b(a,b,c)\in\mathbb F_2\) satisfy \(b(c,b,a)=1-b(a,b,c)\). Among the \(E=n(n-1)(n-2)(n-3)/2\) legal-turn reversal orbits let \(D(b)\) be the number on which consecutive triple colors differ. At each center \(v\), interpret \(b(a,v,c)\) as a tournament orientation on the remaining \(n-1\) labels; let \(t_v\) be its number of directed cyclic triangles and \(T(b)=\sum_v t_v\). Then
\[
\boxed{\frac{D(b)}E\le
\frac23+\frac{n-2}{2(n-3)(n-1)}
-\frac{2(n-4)T(b)}{(n-1)E}.} \tag{6}
\]
In particular
\[
\boxed{\frac23\le\max_b\frac{D(b)}E
\le\frac23+\frac{n-2}{2(n-3)(n-1)},}
\qquad
\lim_{n\to\infty}\max_b\frac{D(b)}E=\frac23. \tag{7}
\]
The upper estimates apply to every induced \(m\)-label restriction with \(m\ge6\).

*Proof.* Put \(x(a,b,c)=(-1)^{b(a,b,c)}\). It is reversal-skew and \(\|x\|^2=N\). For every center \(v\), the triangle curl of the \(\{\pm1\}\)-edge array \(x(a,v,c)\) has square \(1\) on a transitive triangle and \(9\) on a cyclic triangle. Applying (5) with \(m=n-1\) separately at all centers yields
\[
\|x-\Pi_{\mathcal G}x\|^2
=\frac1{n-1}\left(n\binom{n-1}{3}+8T(b)\right)
=\frac{n(n-2)(n-3)}6+\frac{8T(b)}{n-1}. \tag{8}
\]
By Lemma 1, \(\mathcal E_-\subseteq\mathcal G\). Every eigenvalue of \(A\) other than \(-(n-2)\) is at least \(-2\). Thus
\[
\langle x,Ax\rangle\ge
-(n-2)N+(n-4)\|x-\Pi_{\mathcal G}x\|^2. \tag{9}
\]
Signed adjacency gives \(\langle x,Ax\rangle=2E-4D(b)\). Substituting (8) into (9) and simplifying proves (6) and the upper bound in (7).

For the matching lower bound, assign independent continuous real labels \(s_{uv}=s_{vu}\) to all edges of \(K_n\), and set
\[
(-1)^{b(a,b,c)}=\operatorname{sgn}(s_{ab}-s_{bc}).
\]
This is reversal-skew. For every legal quadruple \((a,b,c,d)\), the three labels \(s_{ab},s_{bc},s_{cd}\) are independent and identically distributed. The colors of the two overlapping triples differ precisely when the middle label is their minimum or maximum, an event of probability \(2/3\). Hence \(\mathbb E D(b)=2E/3\), so some edge ordering has \(D(b)\ge2E/3\). Finally every restriction retains reversal oddness and the argument applies with its own number of labels. \(\square\)

The stability term in (6) penalizes cyclic triangles in the local tournaments. The upper bound covers all reversal-odd boundary 3-tournaments, while the asymptotically extremal construction belongs to the edge-ordered subclass. The theorem is a global constraint on coloring-cycle support in the pointed binary turn matroid. Extracting a resource-simple long path still requires a cocircuit selector.

**Corollary 5 (abundance of six-resource low-intersection port cocircuits).**
Let \(n\ge6\), and consider the six-resource twisted-cycle construction in the preceding Subsection. For every injective ordered six-vertex word \(v=(v_1,\ldots,v_6)\), let \(Y_v=C_v\cup\{p\}\) be its seven-element marked port cocircuit and put
\[
w(v)=|X_b\cap Y_v|-1.
\]
The six-turn odd-monodromy construction gives \(w(v)\in\{1,3,5\}\). Then the proportion \(q_n(b)\) of injective words satisfying \(|X_b\cap Y_v|\le4\) obeys
\[
\boxed{
q_n(b)\ge
\frac14-\frac{3(n-2)}{4(n-3)(n-1)}
+\frac{3(n-4)T(b)}{(n-1)E_n}.
}\tag{16}
\]
In particular
\[
q_n(b)\ge\frac14-\frac{3(n-2)}{4(n-3)(n-1)}
=\frac14-O(n^{-1}).
\]
At \(n=6\) this recovers the established \(36/720=1/20\) uniform six-resource guarantee; as \(n\to\infty\) it gives a lower bound approaching one quarter of all ordered six-vertex words, independently of the coloring.

*Proof.* Each of the six edges of the marked turn cycle is uniformly distributed over the \(E_n\) legal-turn reversal orbits when \(v\) is uniformly distributed over injective ordered six-tuples. Hence
\[
\mathbb E_v w(v)=6D_n(b)/E_n.
\]
Writing \(q=\Pr(w\le3)\), the parity restriction \(w\in\{1,3,5\}\) gives
\[
\mathbb E_v w(v)\ge q\cdot1+(1-q)\cdot5=5-4q.
\]
Thus \(q\ge(5-6D_n(b)/E_n)/4\). Substitution of the stability bound (11) proves (16). \(\square\)

This is a global marked-cocircuit counting statement; the stronger assertion that every prescribed six-element resource set has at least one such cocircuit follows separately from the five-cycle averaging theorem.

Let \(H\) be a finite connected graph, let \(B_H\) be its binary incidence matrix, and let \(a\in\mathbb F_2^{E(H)}\) represent a nonzero graph cohomology class. Form the pointed binary matroid
\[
D(H,a)=M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*
\]
with port \(p\). For an admissible signature \(d=a+\delta f\), put
\[
S=\operatorname{supp}(d),
\]
and let \(J_d\) be the multigraph obtained by contracting every connected component of the spanning zero-signature subgraph \(H_0=(V(H),E(H)\setminus S)\). Its labeled edges are precisely the elements of \(S\), including possible loops. Write \(B_J\) for its binary incidence matrix and \(\mathbf1_S\) for the all-ones row on \(S\).

**Theorem 1 (canonical pointed cographic restriction minor).** There are canonical labeled binary-matroid isomorphisms
\[
\boxed{
D(H,a)|(S\cup\{p\})\cong
M\!\left(\begin{array}{c|c}B_J&0\\
\mathbf1_S&1\end{array}\right)^*,}
\tag{1}
\]
and
\[
\boxed{D(H,a)|S\cong M(J_d)^*.}\tag{2}
\]
The first restriction is a pointed parity coextension of the cographic matroid of \(J_d\). It depends only on the monochromatic-component quotient \(J_d\), not on the full turn graph or the chosen representative of the cohomology class.

*Proof.* The binary cocycle space of the dual \(D(H,a)\) is the kernel of its displayed primal representation:
\[
Z^*(D)=\left\{(z,t):B_Hz=0,\ 
t=\langle a,z\rangle\right\}.
\]
Since \(a=d+\delta f\) and every graph cycle is orthogonal to cuts, \(\langle a,z\rangle=\langle d,z\rangle=|z\cap S|\pmod2\). Thus
\[
Z^*(D)=\left\{\bigl(z,|z\cap S|\bmod2\bigr):
z\in Z(H)\right\}.\tag{3}
\]
Coordinate projection from \(Z(H)\) onto \(S\) is surjective onto \(Z(J_d)\), with kernel \(Z(H_0)\). For surjectivity, given an Eulerian set of changed edges of \(J_d\), pair its incident endpoints within each contracted zero-signature component and join each pair by zero-signature paths; the resulting mod-two union is Eulerian in \(H\). Consequently restriction of (3) to \(S\cup\{p\}\) gives
\[
\boxed{
Z^*(D|(S\cup\{p\}))
=\{(w,|w|\bmod2):w\in Z(J_d)\}.}\tag{4}
\]
The right-hand side of (4) is the kernel of the augmented matrix in (1), and hence is the binary cocycle space of its dual. A binary matroid is determined by its cocycle space, proving (1). Deleting the port coordinate from (4) gives \(Z(J_d)\), the cocycle space of the cographic matroid \(M(J_d)^*\), proving (2). \(\square\)

**Corollary 2 (port cocircuits are odd cycles of the quotient).** The cocircuits of \(D(H,a)|(S\cup\{p\})\) containing \(p\) are precisely the sets
\[
\boxed{C\cup\{p\},\quad
C\text{ a simple odd-length cycle of }J_d.}\tag{5}
\]
Loops count as odd cycles of length one. Therefore the shortest port-cocircuit size of the restriction minor is \(1+g_{\mathrm{odd}}(J_d)\).

*Proof.* An odd cycle \(C\) gives a cocycle \(C\cup\{p\}\) by (4). It is support-minimal because no nonzero Eulerian edge set lies in a proper subset of a simple graph cycle. Conversely, a cocycle containing \(p\) projects to an odd-cardinality Eulerian edge set of \(J_d\). Decompose it into edge-disjoint simple cycles. At least one constituent is odd, and the associated cocycle \(C\cup\{p\}\) lies inside the original cocycle. Support minimality therefore forces equality. \(\square\)

The theorem is valid for arbitrary binary graph-cover pointed lifts, including the folded cube and the boundary-tournament full-turn matroid. The restriction minor makes the quotient odd-cycle obstruction intrinsic to the matroid, but—because all unchanged turns have been deleted—it does not retain the length or resource-independence of a lift of an odd cycle to the original graph.

Let \(H\) be a finite connected graph with a nontrivial covering-monodromy cochain \(a\), let
\[
D=M\!\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*
\]
be the corresponding pointed binary lift with port \(p\), and fix an admissible signature \(d=a+\delta f\). Let \(S=\operatorname{supp}(d)\), \(X_d=S\cup\{p\}\in Z(D)\), and \(H_0=(V(H),E(H)\setminus S)\). Define
\[
\mathscr L(d)=\left\{e=uv\in S:
u,v\text{ belong to the same connected component of }H_0\right\}.
\]
For \(e\in\mathscr L(d)\), write \(\ell_e=\operatorname{dist}_{H_0}(u,v)\), and put \(\ell_*(d)=\min_{e\in\mathscr L(d)}\ell_e\). As usual the minimum of an empty family is infinite.

**Theorem 1 (metric loop-lifting identity).** The minimum cardinality of a port cocircuit intersecting \(X_d\) in two elements is
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\
p\in Y,\ |X_d\cap Y|=2}}|Y|
=\ell_*(d)+2.}
\tag{1}
\]
In particular, a two-point-intersection port cocircuit exists if and only if the monochromatic-component quotient \(J_d\) has a loop. Its minimum size is determined by the shortest zero-disagreement path connecting the endpoints of a changed turn that becomes a loop in \(J_d\).

*Proof.* Given \(e=uv\in\mathscr L(d)\), take a shortest \(u\)-to-\(v\) path \(P\) in \(H_0\). Since \(P\) is simple and does not use \(e\), the edge set \(C=P\cup\{e\}\) is a simple cycle in \(H\), with precisely one changed turn. Its covering monodromy is
\[
\alpha(C)=\langle a,C\rangle
=\langle d,C\rangle=1.
\]
Consequently \(Y=C\cup\{p\}\) is a port cocircuit of \(D\) meeting \(X_d\) precisely in \(\{e,p\}\), and \(|Y|=\ell_e+2\).

Conversely, every cocircuit \(Y\) containing \(p\) corresponds to a simple monodromy-one cycle \(C=Y\setminus\{p\}\) of \(H\). If \(|X_d\cap Y|=2\), the cycle \(C\) contains precisely one edge \(e=uv\) from \(S\), and every other edge is in \(H_0\). Thus \(C\setminus\{e\}\) is a zero-turn path joining \(u\) to \(v\), of length at least \(\ell_e\). Therefore \(|Y|\ge\ell_*(d)+2\). Both inequalities establish (1). \(\square\)

For the cube, the existence of at least one such loop follows from the known unrestricted monochromatic antipodal-path theorem (Wu–Yang, 2026), as already recorded in Article XI. The nontrivial question is the distance of the corresponding lifted loop.

#### Cube geodesicity as a zero-turn distance equality

For \(n\ge3\), put \(H_n=L(Q_n/\tau)\) and retain the notation of Theorem 1. Write
\[
g_{p,2}(d)=\min\{|Y|:Y\in\mathcal C^*(D_n),\
p\in Y,\ |X_d\cap Y|=2\}.
\]

**Theorem 2 (even resource-excess distance theorem).** For every antipodally odd edge coloring of \(Q_n\), the minimum \(g_{p,2}(d)\) is finite and satisfies
\[
\boxed{g_{p,2}(d)=n+1+2q_*(d),\qquad
\ell_*(d)=n-1+2q_*(d)}
\tag{2}
\]
for a nonnegative integer \(q_*(d)\). Every minimum-cardinality port cocircuit with two-point intersection is represented by a stationary-free odd-monodromy turn cycle whose lifted moving walk travels each cube coordinate an odd number of times. Its repeated-direction excess is \(q_*(d)\).

In particular, the monochromatic NORI1 conjecture is equivalent to the metric condition
\[
\boxed{
\forall d\text{ admissible on }H_n,\quad
\ell_*(d)=n-1.}\tag{3}
\]
A counterexample, if one exists, must satisfy \(\ell_*(d)\ge n+1\). Equivalently, every changed turn whose endpoints lie in one zero-turn component would have zero-turn distance at least \(n+1\).

*Proof.* The unrestricted monochromatic antipodal-path theorem, together with Article XI's odd-girth duality, guarantees the existence of an odd-monodromy turn cycle of integer turn cost one. Thus Theorem 1 makes \(g_{p,2}(d)\) finite. Choose such a simple cycle \(C\) of the least possible length \(r\).

If \(C\) has a stationary contact, the balanced star-triangle shortcut removes the corresponding stationary edge-state vertex, yields a shorter simple odd-monodromy cycle, and does not increase integer turn cost. The new cost is still a positive odd integer, so it must equal one, contrary to minimality. Therefore \(C\) has no stationary contacts.

Its cyclic edge-state lift is consequently a walk of \(r\) cube edges from a vertex \(x\) to its antipode \(\tau x\). Each coordinate direction occurs an odd number of times; writing its multiplicity as \(1+2k_i\) gives
\[
r=\sum_{i=1}^n(1+2k_i)=n+2\sum_i k_i.
\]
Set \(q_*(d)=\sum_i k_i\). Since \(r=g_{p,2}(d)-1\), Theorem 1 yields (2). If \(q_*=0\), the walk changes each coordinate once and hence is an antipodal geodesic. Its cyclic turn cost is one; place the unique changed turn at the closing seam to obtain a monochromatic full geodesic. Conversely, every monochromatic full antipodal geodesic has a cyclic turn cycle of length \(n\), cost one, and produces \(g_{p,2}\le n+1\). Since the deck displacement is \(n\), no odd-monodromy turn cycle has fewer than \(n\) turns, so equality follows. This proves (3). \(\square\)

**Corollary 3 (a graph-distance sufficient condition).** Suppose a deck-odd cube coloring has at least one changed turn whose endpoints lie in a common zero-turn component of \(H_n\) of graph diameter at most \(n-1\). Then it has a monochromatic antipodal geodesic.

*Proof.* Such a turn has \(\ell_e\le n-1\); Theorem 2 forces \(\ell_*\ge n-1\), so \(\ell_*=n-1\), and (3) applies. \(\square\)

This metric reformulation isolates the full remaining obstruction as the presence of repeated coordinate directions in a shortest zero-turn lift of a changed-turn loop. The pointed cographic restriction minor records which loops exist, while the distances \(\ell_e\) require the zero-turn component geometry discarded by that minor. A universal short-port result therefore needs a hypothesis controlling these **loop-lifting distances**, rather than only its circuit and cocircuit incidence algebra.

Let A be a directed graph whose arcs carry labels in a loopless resource matroid N. Starting from a vertex v and the closure F of an independent resource set, construct a flat-graded automaton with states (v,F). For an arc from v to w labeled e outside F, advance to (w,cl(F union {e})). Every transition increases matroid rank by one. The resulting automaton paths are in bijection with coherent directed walks whose resource labels, together with the initial independent set, remain independent. The automaton is acyclic. This follows immediately from the matroid independence exchange criterion: appending e preserves independence if and only if e is outside the closure of the previously chosen elements.

**Corollary 2 (canonical specializations).** For the cube, take the bidirected Q_n and the free matroid on n coordinate directions; label each cube edge by its direction and begin with the empty flat. From root x a state is (x XOR S,S) with S a subset of directions. Rank n forces every coordinate to be used once, producing an antipodal geodesic.

For ordinary boundary 3-tournaments, take directed ordered-pair states (u,v) and transitions (u,v) to (v,w) for three distinct letters. Use the graphic matroid of K_V. Label each transition by the new resource edge {v,w}, and begin at (u,v) with the flat of {u,v}. After a forward prefix the selected graphic edges form a connected vertex path; its closure contains all edges between previously visited vertices. Thus the next resource {v,w} increases rank if and only if w is new. This automaton recognizes precisely forward vertex-injective tight paths. Reaching graphic rank h means the underlying word uses h+1 original vertices and h-1 ordered triples.

*Proof.* In the cube, free-matroid independence is nonrepetition of coordinate directions. In the boundary model, the graphic closure of a connected tree on a visited vertex set is the set of all complete-graph edges internal to that set. Rank-increasing ordered-pair transitions therefore append a fresh vertex, and the converse holds for every injective tight-path word. QED.

**Theorem 3 (antipodal Boolean reachability criterion for NORI1).** Fix an antipodally odd coloring \(c\) of \(Q_n\) and a root \(x\). Identify its free-resource automaton with the Boolean lattice \(2^{[n]}\), where the directed arc \(S\to S\cup\{i\}\) has the color of the cube edge from \(x+\mathbf1_S\) in direction \(i\). Define
\[
R_x=\{S\subseteq[n]:\text{a color-zero directed path runs from }\varnothing\text{ to }S\}.
\tag{1}
\]
Then, for every \(S\subseteq[n]\), the rooted cube has a geodesic whose edge colors are first zero and then one, with the switch at the vertex \(x+\mathbf1_S\), if and only if
\[
\boxed{S\in R_x\ \text{and}\ [n]\setminus S\in R_x.}\tag{2}
\]
Empty initial or terminal color blocks are allowed. Consequently unrestricted NORI1 is equivalent to
\[
\boxed{\exists x\in Q_n:\ R_x\text{ contains a complementary pair of subsets}.}\tag{3}
\]
A hypothetical NORI1 counterexample would have \(R_x\cap\{[n]\setminus S:S\in R_x\}=\varnothing\) for every root, and hence \(|R_x|\le2^{n-1}\) for every root.

*Proof.* Antipodal oddness makes the arc
\[
S\to S\cup\{i\}
\]
opposite in color to its complemented reverse
\[
[n]\setminus(S\cup\{i\})\to[n]\setminus S.
\]
Therefore reversing and complementing a color-zero path from \(\varnothing\) to \([n]\setminus S\) yields a color-one path from \(S\) to \([n]\). Concatenate with the zero path from \(\varnothing\) to \(S\) to obtain the specified one-switch geodesic. The converse follows by reversing and complementing the color-one suffix. A geodesic with one linear color switch has precisely one cyclic turn disagreement: its closing turn compares the terminal color with the deck complement of the initial color. Cyclically rerooting at the changed turn therefore gives a monochromatic antipodal geodesic. Conversely any monochromatic geodesic, after deck reversal if necessary, is a color-zero geodesic rooted at some \(x\), and gives the complementary pair \(\varnothing,[n]\). Finally a family of subsets avoiding complementary pairs has size at most \(2^{n-1}\), by pairing every subset with its complement. \(\square\)

**Theorem 4 (antipodal cut duality).** For a fixed rooted cube \(x\), let \(R_x\) be as in Theorem 3. The absence of a color-zero-then-color-one antipodal geodesic rooted at \(x\) is equivalent to the existence of a set \(\mathcal U_x\subseteq2^{[n]}\) satisfying all three conditions:
\[
\varnothing\in\mathcal U_x,\qquad
\mathcal U_x\cap\{\bar S:S\in\mathcal U_x\}=\varnothing,\qquad
\text{every outward Boolean-lattice arc of }\mathcal U_x\text{ has color one.}
\tag{4}
\]
Here \(\bar S=[n]\setminus S\). Accordingly, failure of unrestricted NORI1 is equivalent to the existence of such a family \(\mathcal U_x\) for every root \(x\), all arising from the same antipodally odd cube-edge coloring.

*Proof.* If no one-switch geodesic exists from \(x\), Theorem 3 shows that \(R_x\) contains no complementary pair; it contains the empty set, and any outward arc of \(R_x\) must have color one by the definition of color-zero reachability. Thus \(\mathcal U_x=R_x\) works. Conversely, if \(\mathcal U_x\) satisfies (4), no color-zero directed path from the empty set can leave \(\mathcal U_x\), because its first outward arc would have color one. Hence \(R_x\subseteq\mathcal U_x\) and is complement-free, so Theorem 3 excludes the rooted one-switch witness. Apply this for all roots, using Theorem 3's equivalence with global NORI1. \(\square\)

The families in (4) need not be order ideals: directed monochromatic reachability can omit a subset even while reaching some of its supersets by another coordinate order. This is an antipodal-cut certificate, not an ordinary monotone Boolean-lattice ideal.

**Corollary 5 (resource-flat groupoid constraints).** For every root \(x\), the reachability families also satisfy:
\[
\begin{aligned}
&S\in R_x\Longrightarrow S\in R_{x+\mathbf1_S},\\
&S\in R_x,\quad T\in R_{x+\mathbf1_S},\quad S\cap T=\varnothing
\Longrightarrow S\cup T\in R_x .
\end{aligned}
\tag{5}
\]
The first property comes from reversing a color-zero geodesic, and the second from concatenating two coordinate-disjoint color-zero geodesics. Thus the root-indexed antipodal cuts of a hypothetical counterexample cannot be chosen independently: their reachable families obey the symmetric partial-composition laws (5).

The formulation supplies a precise target for Tucker-, Sperner-, or KKM-type arguments. To prove unrestricted NORI1 it suffices to show that no deck-odd cube-edge coloring supports a compatible system of complement-free, color-one-boundary families as in (4) and (5). Theorem 4 does not establish that impossibility.

**Theorem 6 (factorial-free SAT obstruction certificate).** For \(n\ge3\), introduce one Boolean coloring variable per antipodal orbit of cube edges, and one Boolean membership variable \(r_{x,S}\) for every cube root \(x\) and coordinate subset \(S\subseteq[n]\). Let \(\gamma_{x,S,i}\) denote the color-one Boolean expression of the edge from \(x+\mathbf1_S\) in unused coordinate direction \(i\). Consider the clauses
\[
\begin{array}{ll}
r_{x,\varnothing},&\text{all }x,\\
\neg r_{x,S}\vee\gamma_{x,S,i}\vee r_{x,S\cup\{i\}},&
\text{all }x,S,i\notin S,\\
\neg r_{x,S}\vee\neg r_{x,\bar S},&
\text{all }x,\text{ one representative per complement pair }S,\bar S.
\end{array}
\tag{6}
\]
This formula is satisfiable if and only if an antipodally odd coloring of \(Q_n\) exists with no monochromatic antipodal geodesic. Its size is
\[
\boxed{n2^{n-2}+4^n\text{ variables},\qquad
(n+1)2^{2n-1}+2^n\text{ clauses}.}\tag{7}
\]

*Proof.* The coloring variables determine one deck-odd coloring by giving opposite colors to paired antipodal edges. For each root, the first two clause families make \(U_x=\{S:r_{x,S}=1\}\) contain the empty subset and be closed under every color-zero forward transition. The third clause family makes it free of complementary pairs. By Theorem 4 this excludes a NORI1 witness. Conversely, if a counterexample coloring exists, take \(U_x\) to be the true zero-reachable family \(R_x\). Theorem 4 guarantees every clause. There are \(n2^{n-2}\) edge orbits and \(4^n\) root-subset memberships; the forward transitions number \(n2^{2n-1}\), complement pairs \(2^{2n-1}\), and initial-root clauses \(2^n\). \(\square\)

**Corollary 7 (resource-groupoid strengthening).** Adding
\[
r_{x,S}\Longrightarrow r_{x+\mathbf1_S,S},\qquad
r_{x,S}\wedge r_{x+\mathbf1_S,T}
\Longrightarrow r_{x,S\cup T}\quad(S\cap T=\varnothing)
\tag{8}
\]
does not change satisfiability. Indeed the true reachable sets satisfy these implications by path reversal and disjoint-resource concatenation, so they still witness the converse direction.

This gives a finite resource-sensitive dual certificate of a potential counterexample, with a clause count growing as \(O(n4^n)\) instead of the factorial number of rooted geodesics. It is not a uniform proof of unsatisfiability.

**Corollary 8 (antipodal root reduction).** In Theorem 6 the rooted membership variables and clauses may be imposed only for a transversal \(T\) of antipodal vertex pairs. The smaller formula is satisfiable if and only if a counterexample coloring exists. Its size is
\[
\boxed{n2^{n-2}+2^{2n-1}\text{ Boolean variables},\qquad
(n+1)2^{2n-2}+2^{n-1}\text{ clauses}.}\tag{9}
\]
For \(n=7\), this is 224 coloring variables, 8192 rooted variables, and 32,832 clauses before symmetry constraints.

*Proof.* Any counterexample coloring has complement-free true reachable families at every root, so restrict to \(T\). Conversely, if a monochromatic antipodal geodesic existed, reversing it and translating by the deck involution would give geodesics of both colors rooted at both antipodal endpoints. One endpoint lies in \(T\), and its color-zero path forces both the empty set and its complement into that root's SAT membership family, contradicting the complementary-pair clauses. Thus the restricted formula excludes all counterexample witnesses if unsatisfiable. Halving the roots halves the reachability variables and clauses. \(\square\)

This is an equivalent finite-dimensional decision procedure, not a uniform proof over all dimensions.

### Edge-order synchronization and stability of extremal boundary colorings

Let \(n\ge6\), and let \(V_n\) consist of real functions \(x(a,b,c)=-x(c,b,a)\) on ordered triples of distinct labels. Its dimension is \(N=n(n-1)(n-2)/2\). The legal-turn reversal quotient has \(E=N(n-3)\) edges. For sign-valued \(x\), let \(D(x)\) count disagreeing turns. Recall the signed adjacency operator
\[
(Ax)(a,b,c)=\sum_{d\notin\{a,b,c\}}[x(b,c,d)+x(d,a,b)]
\]
with spectrum contained in \(\{-(n-2),-2,0,1,n-2\}\). Its smallest eigenspace is
\[
\mathcal E_-=\{f_s(a,b,c)=s_{ab}-s_{bc}:s_{ab}=s_{ba},\ \sum_{b\ne a}s_{ab}=0\}.
\]
Let \(\mathcal G=\{f:f(a,b,c)=u_b(a)-u_b(c)\}\) be the direct sum of local gradient spaces; then \(\mathcal E_-\subseteq\mathcal G\).

**Theorem 1 (canonical symmetric edge potential).** For \(x\in V_n\) define
\[
d_b(a)=\sum_{c\notin\{a,b\}}x(a,b,c),\quad
h_{ab}=d_b(a)+d_a(b),\quad H_a=\sum_{b\ne a}h_{ab}.
\]
The symmetric weights
\[
\boxed{s_{ab}=\frac1{2(n-1)}
\left(h_{ab}-\frac{H_a+H_b}{n-2}\right)}
\tag{1}
\]
have zero row sums and determine the orthogonal projection
\(\Pi_-x=f_s\) onto \(\mathcal E_-\). The nonnegative global synchronization defect
\[
\Gamma(x)=\|\Pi_{\mathcal G}x-\Pi_-x\|^2
\]
has the explicit expression
\[
\boxed{\Gamma(x)=
\frac1{n-1}\sum_b\sum_{a\ne b}d_b(a)^2-
\frac1{2(n-1)}\sum_{a<b}
\left(h_{ab}-\frac{H_a+H_b}{n-2}\right)^2.}
\tag{2}
\]

*Proof.* Reversal skewness gives \(\sum_{a\ne b}d_b(a)=0\), hence \(\sum_aH_a=0\). Formula (1) has zero row sums. For any symmetric zero-row-sum array \(t\), define \(f_t(a,b,c)=t_{ab}-t_{bc}\). Expanding over outer pairs yields
\[
\langle x,f_t\rangle=\sum_{a<b}h_{ab}t_{ab},\qquad
\langle f_s,f_t\rangle=2(n-1)\sum_{a<b}s_{ab}t_{ab}.
\]
Their difference is zero because \(h_{ab}-2(n-1)s_{ab}=(H_a+H_b)/(n-2)\) is orthogonal to \(t\). This proves the projection claim. The local gradient projection has coordinates \((d_b(a)-d_b(c))/(n-1)\) and squared norm \((n-1)^{-1}\sum_{a\ne b}d_b(a)^2\). The norm of \(f_s\) is \(2(n-1)\sum_{a<b}s_{ab}^2\). Subtraction of the nested projection norms proves (2). \(\square\)

For each center \(b\), orient its tournament of outer labels by \(x(a,b,c)\), and let \(t_b\) count directed cyclic triangles, \(T(x)=\sum_b t_b\).

**Theorem 2 (joint curvature and synchronization penalty).** Every sign-valued reversal-skew \(x\) obeys
\[
\boxed{\frac{D(x)}E\le
\frac23+\frac{n-2}{2(n-3)(n-1)}
-\frac{2(n-4)T(x)}{(n-1)E}
-\frac{(n-4)\Gamma(x)}{4E}.}
\tag{3}
\]
*Proof.* The complete-graph Hodge identity yields
\(\|x-\Pi_{\mathcal G}x\|^2=n(n-2)(n-3)/6+8T(x)/(n-1)\).
Nested orthogonal projections add \(\Gamma(x)\) to this squared distance. The spectral gap between \(-(n-2)\) and the remaining eigenvalues, which are at least \(-2\), gives
\[
\langle x,Ax\rangle\ge-(n-2)N+
(n-4)\|x-\Pi_-x\|^2.
\]
Use \(\langle x,Ax\rangle=2E-4D(x)\) and simplify. \(\square\)

**Lemma 3 (elementary tournament stability).** A tournament on \(m\ge3\) vertices with \(t\) cyclic triangles can be made transitive by reversing at most \(8m^2(t/m^3)^{1/3}\) arcs, with zero changes when \(t=0\).

*Proof.* List vertices in increasing outdegree \(d_0\le\cdots\le d_{m-1}\). Counting transitive triples by their source gives
\(\sum_i i^2-\sum_i d_i^2=2t\).
For each \(k\), the \(k\) lowest-degree vertices have at least \(\binom{k}{2}\) internal wins, so \(\sum_{i<k}(d_i-i)\ge0\). Summation by parts against increasing \(d_i\) yields \(\sum_i(i-d_i)d_i\ge0\), hence
\[
\sum_i(i-d_i)^2\le2t. \tag{4}
\]
An inversion in the score order is an arc \(i\to j\) with \(i<j\). It belongs to at least \(d_j-d_i+1\) cyclic triangles, as follows by comparing the two endpoint outdegrees and partitioning their other neighbors into four orientation types.

Set \(\delta=t/m^3\), \(\eta=\delta^{1/3}\), \(\theta=\delta^{1/2}\), assuming \(t>0\). At most \(2t/(\eta^2m^2)\) vertices have \(|d_i-i|>\eta m\), so at most \(2t/(\eta^2m)\) inversion arcs touch such vertices. Among the remaining vertices, at most \((\theta+2\eta)m^2\) pairs have rank separation at most \((\theta+2\eta)m\). Every other inverted arc has outdegree gap greater than \(\theta m\), hence participates in at least \(\theta m\) cyclic triangles. Since each cyclic triangle has three arcs, there are at most \(3t/(\theta m)\) such inversions. The total is at most
\[
m^2\big(\theta+2\eta+2\delta/\eta^2+3\delta/\theta\big)
=m^2(4\delta^{1/3}+4\delta^{1/2})
\le8m^2\delta^{1/3}.
\]
Reversing the inversions gives a transitive order. \(\square\)


**Theorem 4 (near-extremal stability toward edge orderings).** Define
\[
\varepsilon=\max\{0,\,2/3-D(x)/E\},\qquad
z=\varepsilon+\frac{n-2}{2(n-3)(n-1)}.
\]
There exist pairwise distinct symmetric edge weights \(s_{ab}=s_{ba}\) such that the comparison coloring \(x_s(a,b,c)=\operatorname{sgn}(s_{ab}-s_{bc})\) differs from \(x\) on at most \(O(Nz^{1/9})\) reversal classes of triples, with an absolute implied constant. Consequently \(D(x_n)/E_n\ge2/3-o(1)\) forces agreement with an edge-ordered boundary coloring on \(1-o(1)\) of all triple classes.

*Proof.* The nonnegative penalties in (3) give
\[
\frac{2(n-4)T}{(n-1)E}+\frac{(n-4)\Gamma}{4E}\le z.
\]
Writing \(m=n-1\), we have \(T/(nm^3)\le3z/10\) and \(\Gamma/N\le6z\). Apply Lemma 3 to the \(n\) local tournaments. Jensen's inequality supplies a reversal-skew coloring \(y\), whose local tournaments are all transitive, with \(R\) altered triple classes satisfying
\[
R/N\le \frac{16m}{m-1}(T/(nm^3))^{1/3}
\le20z^{1/3}. \tag{5}
\]
Take the symmetric potential \(s\) computed by (1), so \(\Pi_-x=f_s\). Projection contractivity, \(\|x-y\|^2=4R\), and the definition of \(\Gamma\) give
\[
\|\Pi_{\mathcal G}y-f_s\|^2\le8R+2\Gamma. \tag{6}
\]
The signed outdegree scores of a transitive tournament on \(m\) vertices are \(-(m-1),-(m-3),\ldots,m-1\). Consequently the local gradient projection \((\Pi_{\mathcal G}y)(a,b,c)\) has the same sign as \(y(a,b,c)\) and magnitude \(2|i-j|/m\), where \(i,j\) are their local ranks.

For any \(0<\theta<1\), the fraction of outer pairs with rank separation smaller than \(\theta m\) is at most \(2m\theta/(m-1)\). Every other pair at which \(y\) and the sign of \(f_s\) disagree contributes at least \(4\theta^2\) to (6). Perturb the finitely many symmetric weights generically by sufficiently small amounts to eliminate ties while preserving all strict comparisons. Thus
\[
\frac{\operatorname{dist}(x,x_s)}N
\le\frac RN+\frac{2m}{m-1}\theta+
\frac{8R+2\Gamma}{4\theta^2N}. \tag{7}
\]
Taking \(\theta=z^{1/9}\) when \(z<1\), and applying (5) and the preceding bounds, proves the assertion. For \(z\ge1\) the bound is immediate after enlarging its absolute constant. \(\square\)

The theorem concerns unrestricted reversal-odd boundary tournaments; the edge-ordered subclass emerges quantitatively in the near-extremal density regime. Transferring long vertex-simple paths across exceptional triples requires a separate robustness argument.


### NORI Article XI — precise Smith form for boundary-tournament tight windows

**Theorem (proved, n >= 5).** Let T_n be the reversal-orbits of distinct ordered triples (a,b,c)~(c,b,a), N=n(n-1)(n-2)/2. Let h_pi be the 0/1 incidence vector of the n-2 consecutive triple windows in any Hamiltonian word pi. Then

  span_Z{h_pi: pi in S_n}
    = {z in Z^N: sum(z) = 0 mod (n-2)}.

Thus Z^N/span_Z{h_pi} = Z/(n-2), and the Smith normal form has N-1 ones and one n-2. This proves the earlier Smith-form conjecture, not merely the n=5,6,7 computations.

**Local swaps.** If a Hamiltonian word ends u,a,b,c, exchanging b,c gives the identity for an annihilating triple weighting w_{abc}=w_{cba}:

  w_{uab}+w_{abc}-w_{uac}-w_{acb}=0. (E)

For characteristic different from two, fix middle symbol a. Equation (E) says the differences of the symmetric matrix M_a(u,b)=w_{uab} between columns b,c do not depend on row u. The standard complete-graph additive lemma (solve three pair equations and extend by column differences) gives M_a(u,b)=s_a(u)+s_a(b). Set P_ab=s_a(b)+s_b(a). Substitution in E shows P_ab-P_ac=s_c(b)-s_b(c), independent of a, so another application of the lemma gives P_ab=gamma_a+gamma_b. Adding/subtracting these two identities gives s_a(b)=gamma_b, hence w_{abc}=gamma_a+gamma_c.

The Hamiltonian sum is 2 sum gamma_i minus the gamma values at the four end positions. Swapping an interior-position label with an end-position label forces all gamma_i equal. So w is constant, and the word constraint is (n-2)w=0. This proves the claimed annihilator dimension for all fields of odd characteristic and for characteristic zero.

For characteristic two, each relation (E) is a four-cycle in F=L(K_n) with vertices ua,ab,bc,ac. These squares generate the even-length subspace of Z_1(F;F2): the cycle space is generated by star triangles (three K_n edges at a vertex) and edge triangles (three K_n edges forming a triangle). An E square is the symmetric difference of an edge triangle on ab,ac,bc and a star triangle on ua,ab,ac. Two K_n edge triangles sharing an original K_n edge are congruent via the same star triangle; the adjacency graph of K_n triangles is connected. Thus all generating triangles are congruent modulo E squares, and their common odd parity proves the square span is precisely the even-cycle subspace.

Therefore every F2 annihilating weighting of (E) has the form
  w_{abc}=u_{ab}+u_{bc}+z,
a cut cochain on F plus a constant. Summing over a Hamiltonian word telescopes the cut, yielding u_{v1v2}+u_{v(n-1)vn}+(n-2)z=0. Any two disjoint edges of K_n can be the first and last. For two edges sharing a vertex, a third edge disjoint from both exists since n>=5; comparing these pairs forces their u-values equal. Connectivity of L(K_n) forces u constant. Thus w=z constant and (n-2)z=0. Hence over *every* field the annihilator has dimension one precise when its characteristic divides n-2; otherwise it is zero.

**Integral step.** The Hamiltonian incidence matrix has full rational rank, so C=Z^N/L is finite. In every characteristic its corank is <=1, making C cyclic. For each prime dividing |C|, the unique modular annihilator is the all-one cochain, nonzero on every basis vector e_t; therefore every e_t generates C. S_n acts on C by relabeling. Since Aut(C) is abelian, conjugate transpositions induce the same automorphism. A transposition of two labels outside a fixed triple exists (n>=5) and fixes the generator e_t; it therefore acts trivially. Thus all transpositions, hence all permutations, act trivially, and every e_t is the same element e of C. Each Hamiltonian row has n-2 windows, giving (n-2)e=0. Conversely total coordinate sum modulo n-2 gives a surjection C -> Z/(n-2). Hence C is precise Z/(n-2).

**Significance.** The cube's geodesic unsigned incidence lattice was proved saturated for n>=5. The boundary-tournament Hamiltonian triple-window lattice has precisely one length-based torsion factor n-2, and no other hidden integrality defects. The theorem concerns unsigned triple-window incidence, not the entire pointed two-port cocircuit incidence matrix. It does not yield positivity, a monochromatic tight path, or unrestricted NORI1; the nonlinear low-cost gallery selector remains open.


#### Signed Hamiltonian tight-window incidence: complete Smith form

Choose one oriented representative of every reversal class \(t=[a,b,c]=[c,b,a]\). Each Hamiltonian word \(\pi\) determines a signed incidence vector \(s_\pi\in\mathbb Z^{\mathcal T_n}\), in which a triple window contributes \(+1\) if it agrees with the chosen orientation of its reversal orbit, and \(-1\) if it is reversed. Write \(\Lambda_n^\pm=\operatorname{span}_{\mathbb Z}\{s_\pi\}\).

**Theorem 2 (signed Smith form).** For all \(n\ge5\),
\[
\boxed{\mathbb Z^{\mathcal T_n}/\Lambda_n^\pm\cong
\begin{cases}
0,&n\ \text{odd},\\
\mathbb Z/2\mathbb Z,&n\ \text{even}.
\end{cases}}
\]
Thus the signed Hamiltonian incidence matrix has full rational column rank. All nonzero Smith invariant factors are one in odd orders, and there is a single factor two in even orders.

*Proof.* We first compute its linear annihilator over fields. For characteristic different from two, represent an annihilating weighting by \(z_{abc}=-z_{cba}\). The terminal adjacent-swap comparison gives, for pairwise distinct \(u,a,b,c\),
\[
z_{uab}+z_{abc}-z_{uac}-z_{acb}=0.\tag{S}
\]
Interpret triple reversal orbits as oriented edges of \(F=L(K_n)\), where \((u,a,b)\) is the edge from \(\{u,a\}\) to \(\{a,b\}\).

Fix \(a\) and put \(M_a(u,b)=z_{uab}\); this is antisymmetric in \(u,b\). The relation (S) says \(M_a(u,b)-M_a(u,c)\) is independent of \(u\) outside \(\{a,b,c\}\). It follows that the triangular circulation
\[
T_a(u,b,c)=M_a(u,b)+M_a(b,c)+M_a(c,u)
\]
does not change if any one of the three arguments is replaced by a fourth distinct label. Comparing such replacements on four labels shows \(T_a(u,b,c)=-T_a(u,b,c)\); since the field characteristic is not two, \(T_a=0\). Thus there are potentials \(r_a(b)\) with
\[
z_{uab}=r_a(b)-r_a(u).
\]
Substituting this form in (S), the skew function \(P_{ab}=r_a(b)-r_b(a)\) has zero triangular circulation on \(K_n\); hence \(P_{ab}=\gamma_b-\gamma_a\) for some \(\gamma\). The potentials
\[
v_{\{a,b\}}=r_a(b)+\gamma_a
\]
are symmetric, since \(r_a(b)-r_b(a)=\gamma_b-\gamma_a\), and yield
\[
\boxed{z_{uab}=v_{\{a,b\}}-v_{\{u,a\}}.}
\]
This is a graph coboundary on \(F\). In a Hamiltonian tight-window sequence it telescopes to the potential of the final unordered edge minus that of the initial unordered edge. Any two disjoint \(K_n\) edges can occur as these endpoints. If two edges intersect, a third edge disjoint from both exists for \(n\ge5\), so comparison through that edge forces their potentials to agree as well. Therefore every \(v_{\{a,b\}}\) is equal and \(z=0\). The signed incidence matrix has full column rank over every field of characteristic other than two.

Over characteristic two, the orientation signs disappear. The unsigned Smith-form theorem above says that its nullity is zero when \(n\) is odd and one when \(n\) is even; in the latter case the unique annihilator is the constant triple-orbit weighting.

The integral cokernel \(C^\pm=\mathbb Z^{\mathcal T_n}/\Lambda_n^\pm\) is finite because of rational full column rank. It has no odd-primary torsion and its reduction modulo two has dimension zero for odd \(n\), one for even \(n\). Therefore it is trivial for odd \(n\) and a cyclic \(2\)-group for even \(n\). In the even case, each coordinate class \(e_t\) generates \(C^\pm\), since the unique modular annihilator is constant and nonzero at every triple orbit.

Relabeling gives an action of \(S_n\) on the cokernel. Since a cyclic group has abelian automorphism group, conjugate transpositions induce the same automorphism. For any fixed oriented triple, two unused labels exist when \(n\ge5\). Their transposition fixes its generating coordinate class and must act as identity. Thus every transposition acts trivially. But exchanging the first and third labels of a triple sends its signed coordinate class \(e_t\) to \(-e_t\). Consequently \(2e_t=0\), so the cokernel has exponent two. It is nonzero in even orders by its mod-two deficiency; hence \(C^\pm=\mathbb Z/2\mathbb Z\). \(\square\)

**Scope.** These two Smith-form results concern unsigned and reversal-signed Hamiltonian triple-window incidences. They are not statements about all pointed dual-matroid cocircuits. The unsigned length congruence and residual signed parity describe linear integer obstructions; they do not produce nonnegative path representations, low-switch geodesics, or long monochromatic boundary-tournament tight paths.

#### Nonnegative cones and the missing connectivity constraints

The integral lattice identities above admit a sharp positivity analysis.

**Theorem 3 (the signed Hamiltonian semigroup has no convex restriction).** Let
\[
\mathsf S_n^\pm=\left\{\sum_{\pi\in S_n}m_\pi s_\pi:
m_\pi\in\mathbb Z_{\ge0}\right\}
\]
be the nonnegative integral semigroup generated by the signed Hamiltonian triple-window incidence vectors. For every \(n\ge5\),
\[
\boxed{
\mathsf S_n^\pm=\Lambda_n^\pm
=\begin{cases}
\mathbb Z^{\mathcal T_n},&n\text{ odd},\\
\{z\in\mathbb Z^{\mathcal T_n}:\sum_tz_t\equiv0\pmod2\},
&n\text{ even}.
\end{cases}}
\tag{16}
\]
The real cone generated by these signed vectors is the entire real space \(\mathbb R^{\mathcal T_n}\).

*Proof.* Reversing a Hamiltonian vertex word reverses all of its triple windows, so
\[
s_{\pi^R}=-s_\pi.
\]
Every integer linear combination of signed path vectors can therefore be rewritten as a nonnegative integer combination, by replacing a negatively weighted path with its reversal. Hence the signed semigroup equals its generated integer lattice. The signed Smith theorem gives this lattice as the entire space in odd orders and a subgroup of index two in even orders. For even \(n\), each signed row has even coordinate sum, and the parity-even subgroup itself has index two, identifying the lattice. Full rational column rank and the availability of both \(s_\pi\) and \(-s_\pi\) make the real cone equal to the whole space. \(\square\)

This theorem warns against treating nonnegative coefficients in a **signed** incidence expansion as a positive witness: reversal provides a negative representative for every path, so the semigroup has no pointed-cone geometry. The relevant convex constraints must instead retain orientation-specific feasibility or use unsigned incidences.

For unsigned windows let
\[
P_n=\operatorname{conv}\{h_\pi:\pi\in S_n\}
\subseteq\mathbb R^{\mathcal T_n},
\tag{17}
\]
and define the middle-resource projection
\[
(Mz)_v=\sum_{\substack{a,c\in[n]\setminus\{v\}\\a<c}}
z_{[a,v,c]},\qquad v\in[n].
\tag{18}
\]

**Theorem 4 (uniform-matroid base projection).** For \(n\ge5\),
\[
\boxed{
M(P_n)=\left\{y\in[0,1]^n:
\sum_{v=1}^n y_v=n-2\right\}
=B(U_{n-2,n}),
}
\tag{19}
\]
the base polytope of the uniform matroid of rank \(n-2\).

*Proof.* A Hamiltonian word uses each vertex as a middle vertex of a triple window precisely when that vertex is neither its first nor its last label. Hence
\[
Mh_\pi=\mathbf1-e_{v_1}-e_{v_n}.
\]
Every unordered pair of possible endpoints occurs in a Hamiltonian word, so the images of path vectors are all \(0/1\) vectors with \(n-2\) ones. Their convex hull is the hypersimplex \(B(U_{n-2,n})\). \(\square\)

The base-polytope projection captures the resource independence used by Hamiltonian words, but it does not capture their connectedness.

**Theorem 5 (cut inequalities and disconnected lattice certificates).** For every nonempty proper vertex set \(S\subsetneq[n]\), define
\[
q_S([a,b,c])=
\mathbf1\bigl(\{a,b\}\in\delta_{K_n}(S)
\text{ or }\{b,c\}\in\delta_{K_n}(S)\bigr).
\tag{20}
\]
Every unsigned Hamiltonian path-incidence vector satisfies
\[
\boxed{\langle q_S,h_\pi\rangle\ge1,}
\tag{21}
\]
and therefore so does every \(z\in P_n\). For every \(n\ge6\), however, there exists a \(0/1\) vector \(z\in\mathbb Z^{\mathcal T_n}\) satisfying all of the following:
\[
\boxed{
\begin{gathered}
z\ge0,\quad\sum_tz_t=n-2,\quad
z\in\Lambda_n,\quad
Mz=\mathbf1-e_u-e_v\in B(U_{n-2,n}),\\
\langle q_S,z\rangle=0\text{ for some nontrivial }S.
\end{gathered}}
\tag{22}
\]
In particular, the complete Smith congruence plus nonnegativity and the uniform-matroid resource-base constraints are insufficient to characterize a Hamiltonian path or its convex hull.

*Proof.* Every Hamiltonian word visits vertices in both \(S\) and its complement, so at least one of its consecutive \(K_n\) edges crosses \(\delta(S)\). That edge belongs to at least one of the \(n-2\) consecutive triple windows, proving (21).

For (22), partition the vertex set into \(S\dot\cup S^c\) with \(|S|,|S^c|\ge3\). Choose one omitted middle vertex \(u\in S\) and \(v\in S^c\). For every other center \(b\), choose distinct \(a,c\) from the same side as \(b\) and different from \(b\); put a single one in the coordinate \([a,b,c]\), with all other coordinates zero. Different centers give different triple-orbit coordinates, so the resulting \(z\) is \(0/1\), has \(n-2\) ones, and has middle-resource projection \(\mathbf1-e_u-e_v\). The unsigned Smith theorem puts it in \(\Lambda_n\), because its coordinate sum equals \(n-2\). But no chosen triple crosses the partition, giving \(\langle q_S,z\rangle=0\), contrary to (21). \(\square\)

**Implication for the unification program.** The two lattice theorems eliminate divisibility ambiguity but do not replace coherent resource-independent path geometry. Signed cones are non-pointed because reversal negates generators; unsigned convex path incidence has additional global connectivity inequalities invisible to both the Smith lattice and its uniform-matroid middle-resource projection. A common matroidal low-switch selector must preserve **graphic connectivity across cuts**, in addition to linear incidence and resource independence. The new conclusions are polyhedral obstructions to a proposed shortcut, not proofs of the unrestricted cube or boundary-tournament existence conjectures.

#### Complete local-exchange generation for signed Hamiltonian windows

Keep \(n\ge5\), and write \(s_\pi\in\mathbb Z^{\mathcal T_n}\) for the signed triple-window incidence vector of a Hamiltonian word \(\pi\). Let
\[
E_n^\pm=\operatorname{span}_{\mathbb Z}
\{s_\pi-s_{\pi'}:\ \pi'\text{ is obtained from }\pi
\text{ by one adjacent transposition}\}.
\tag{23}
\]

**Theorem 6 (all signed adjacent-swap differences generate the parity lattice).** For every \(n\ge5\),
\[
\boxed{
E_n^\pm=
\left\{z\in\mathbb Z^{\mathcal T_n}:
\sum_t z_t\equiv0\pmod2\right\}.
}
\tag{24}
\]
Equivalently, the integer matrix of all signed adjacent-swap differences has full rational column rank and a Smith normal form with \(|\mathcal T_n|-1\) unit factors and one factor two. This holds in both odd and even orders.

*Proof.* Adjacent transpositions generate the connected Cayley graph of the permutation group, so \(E_n^\pm\) also equals the lattice of all pairwise differences \(s_\pi-s_\sigma\).

First classify annihilators over fields. Let \(z\) be a linear functional vanishing on these differences. Then \(\langle z,s_\pi\rangle=K\) is constant over all Hamiltonian words \(\pi\). Comparing terminal adjacent swaps gives the same four-cycle relation (S) used in Theorem 2.

For a field of characteristic different from two, Theorem 2's local-potential argument turns any solution of (S) into an oriented graph cut
\[
z_{uab}=v_{\{a,b\}}-v_{\{u,a\}}
\]
on \(F=L(K_n)\). Its Hamiltonian sum is the potential of the final unordered edge minus that of the first. Since any ordered pair of disjoint original \(K_n\)-edges occurs as these endpoints, constant value \(K\) forces all potentials to agree (compare through a third edge disjoint from any intersecting pair), giving \(z=0\). Thus the swap-difference matrix has full rank over every field of characteristic different from two, including \(\mathbb Q\).

In characteristic two, the unsigned four-cycle classification from Theorem 1 applies: every solution of (S) is
\[
z_{abc}=u_{\{a,b\}}+u_{\{b,c\}}+\zeta.
\]
Its Hamiltonian evaluation is
\[
u_{\{v_1,v_2\}}+u_{\{v_{n-1},v_n\}}+(n-2)\zeta=K.
\]
Constancy over arbitrary disjoint endpoint pairs again forces \(u\) to be constant. Hence the only annihilating weightings are the constant triple-orbit cochains \(z_{abc}=\zeta\), a one-dimensional space over \(\mathbb F_2\). Therefore the integral cokernel
\[
C=\mathbb Z^{\mathcal T_n}/E_n^\pm
\]
is finite with no odd-primary torsion, and \(\dim_{\mathbb F_2}(C/2C)=1\). It is a nonzero cyclic 2-group. Its unique nonzero modular annihilator is the all-one cochain, which evaluates to one on every coordinate vector, so every standard coordinate class \(e_t\) generates \(C\).

The symmetric group acts on \(C\) by relabeling oriented triples. Every transposition is conjugate, while automorphisms of a cyclic group commute. A transposition of two labels outside a fixed triple fixes its coordinate generator, so it acts trivially; hence every transposition acts trivially. But transposing the first and last labels of the fixed triple reverses its orientation and sends \(e_t\) to \(-e_t\). Thus \(2e_t=0\), forcing \(C\cong\mathbb Z/2\mathbb Z\).

Every signed Hamiltonian incidence vector has coordinate sum congruent to \(n-2\pmod2\), independent of its orientation signs. Accordingly every difference \(s_\pi-s_\sigma\) has even coordinate sum. The even-sum lattice has index two in \(\mathbb Z^{\mathcal T_n}\), as does \(E_n^\pm\); inclusion implies equality and proves (24). \(\square\)

**Corollary 7 (difference-only versus full signed path lattices).** For \(n\ge5\),
\[
\boxed{
\Lambda_n^\pm/E_n^\pm\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}}
\tag{25}
\]
Thus in even orders the entire signed Hamiltonian path incidence lattice is generated by adjacent-swap differences. In odd orders a single signed Hamiltonian path vector supplies the remaining parity-odd class.

*Proof.* Combine Theorem 6 with Theorem 2 and note that the coordinate sum of each signed Hamiltonian incidence vector has parity \(n-2\). \(\square\)

**Interpretation for the matroidal unification project.** The signed Hamiltonian *resource-incidence* exchange system is integrally complete up to a single unavoidable parity class; it has no residual affine resource charge analogous to the \(n-1\)-dimensional charge space of cube geodesic six-turn exchanges. Yet this does not imply low color cost or long monochromatic tight paths. Differences between signed Hamiltonian vectors are formal integer relations, and their all-dimensional generation need not yield a sequence of legal, monotone-cost, resource-independent galleries. The remaining common problem is nonlinear **accessibility and positivity**, not generation of the integral incidence lattice.

### Antipodal cut-pair separation and four-sector cocycle geometry

The component-contact minor records the intersections of monochromatic components with their deck images. Here we recover additional information lost under zero-turn contraction: the *boundaries of a monochromatic component and its deck image are disjoint graphic-matroid cocycles*. This yields a canonical four-sector quotient with prescribed boundary colors, and a matroid-intersection characterization of which vertex sets can occur as monochromatic components under a deck-odd coloring.

Let \(G\) be a finite connected graph with a fixed-point-free involution \(\tau\) that acts freely on edges, and let \(c:E(G)\to\mathbb F_2\) obey \(c(\tau e)=1+c(e)\). The antipodal cube \(Q_n\), \(n\ge3\), is the principal example. The graph cuts \(\delta_G(S)\) form the cocycle space of the graphic matroid \(M(G)\).

#### 1. Disjoint antipodal cut cocycles

**Theorem 1 (component-cut disjointness).** Let \(R\subseteq V(G)\) be the vertex set of one connected color-zero component, excluding isolated zero-degree vertices. Then
\[
\boxed{\delta_G(R)\subseteq c^{-1}(1),\qquad
\delta_G(\tau R)=\tau\delta_G(R)\subseteq c^{-1}(0),}
\tag{1}
\]
and therefore
\[
\boxed{\delta_G(R)\cap\delta_G(\tau R)=\varnothing.}
\tag{2}
\]

*Proof.* An edge leaving a full color-zero connected component cannot itself have color zero, since its exterior endpoint would belong to the same component. Thus \(\delta_G(R)\) is blue. Applying \(\tau\) converts those edges to red and gives the boundary of \(\tau R\), proving (1) and (2). \(\square\)

**Corollary 2 (antipodal cocycle pair).** The two graphic-matroid cocycles \(\delta_G(R)\) and \(\delta_G(\tau R)\) have disjoint supports, are exchanged by \(\tau\), and have the same cardinality. Their union is the cocycle
\[
\boxed{
\delta_G(R)\sqcup\delta_G(\tau R)
=\delta_G(R\mathbin{\triangle}\tau R).
}
\tag{3}
\]
If \(R\) contains an antipodal pair, then \(R\cap\tau R\ne\varnothing\), and this pair of separated cuts coexists with a port-parallel loop in the pointed component-contact minor.

*Proof.* Binary cut addition obeys \(\delta(A)\triangle\delta(B)=\delta(A\triangle B)\). The supports are disjoint by (2), and \(\tau\) exchanges them. \(\square\)

#### 2. Canonical four-sector geometry

Define a partition of \(V(G)\):
\[
\boxed{
I=R\cap\tau R,\quad
A=R\setminus\tau R,\quad
B=\tau R\setminus R=\tau A,\quad
O=V(G)\setminus(R\cup\tau R).
}
\tag{4}
\]
The sectors \(I,O\) are \(\tau\)-invariant; \(\tau\) exchanges \(A\) and \(B\).

**Theorem 3 (four-sector forbidden diagonals and forced colors).** No edge joins \(I\) to \(O\), and no edge joins \(A\) to \(B\):
\[
\boxed{E_G(I,O)=E_G(A,B)=\varnothing.}
\tag{5}
\]
Every edge between distinct sectors belongs to one of the four other cross-sector classes. Its color is forced:
\[
\boxed{
c(E_G(I,A))=0,\quad
c(E_G(B,O))=0,\quad
c(E_G(I,B))=1,\quad
c(E_G(A,O))=1.
}
\tag{6}
\]
Edges contained within an individual sector are not assigned a color by (5)–(6).

*Proof.* An edge between \(I\) and \(O\) crosses both boundaries \(\delta(R)\) and \(\delta(\tau R)\); so does an edge between \(A\) and \(B\). Theorem 1 forbids such edges. An \(I\)-to-\(A\) edge crosses \(\delta(\tau R)\), hence is red. An \(I\)-to-\(B\) edge crosses \(\delta(R)\), hence is blue. The other two cases are symmetric and give (6). \(\square\)

Equivalently, the sector label defines a \(\tau\)-equivariant graph map to a four-cycle with cyclic sectors \(I,A,O,B\), allowing stationary steps, and with the two opposite diagonals forbidden. Red and blue boundary edges alternate around this four-cycle. The quotient is a global compatibility constraint between the color-zero component \(R\), the color-one component \(\tau R\), and their interface \(I\), not merely a statement about one component in isolation.

#### 3. Which sets can be monochromatic components?

Let \(G\) be any finite connected graph with a fixed-point-free involution acting freely on edges, as at the start of this Subsection. A deck edge orbit is the two-element pair \(\{e,\tau e\}\). For a vertex set \(R\), let \(G_R=G[R]\) be its induced graph. The edge orbits partition \(E(G_R)\) into classes of size one or two. Let \(P_\tau(R)\) be the partition matroid on \(E(G_R)\) permitting at most one selected edge from each antipodal orbit. Let \(M(G_R)\) be the graphic cycle matroid of the induced graph.

**Theorem 4 (graphic–partition matroid component characterization).** For a nonempty \(R\subseteq V(G)\), there exists a deck-odd edge coloring of the full covering graph for which \(R\) is precisely one connected red component if and only if
\[
\boxed{
\delta_G(R)\cap\tau\delta_G(R)=\varnothing
}
\tag{7}
\]
and
\[
\boxed{
\max\{|T|:T\in\mathcal I(M(G_R))\cap\mathcal I(P_\tau(R))\}
=|R|-1.
}
\tag{8}
\]
The second condition says that \(G_R\) has a spanning tree containing no antipodal pair of edges.

*Proof.* For necessity, let \(R\) be a red component of a deck-odd coloring. Condition (7) is Theorem 1. Choose a red spanning tree of \(R\). It is independent in \(M(G_R)\), has \(|R|-1\) edges, and cannot contain both members of an antipodal edge pair because they have complementary colors. Thus (8) holds.

For sufficiency, choose a spanning tree \(T\subseteq E(G_R)\) meeting each edge orbit at most once. For each orbit that meets \(\delta(R)\), color its unique boundary member blue and its antipode red; this prescription is consistent because (7) forbids both orbit members from lying in \(\delta(R)\). On every still-uncolored edge orbit meeting \(T\), declare its member in \(T\) red and its antipode blue; there is no conflict because the orbit contains at most one tree edge, and any tree edge whose antipode was a boundary edge has already been colored red. Color the remaining orbits arbitrarily with complementary bits. All boundary edges of \(R\) are blue, so no red path exits \(R\); every edge of \(T\) is red, so \(R\) is red connected. Hence \(R\) is one full red component. \(\square\)

**Corollary 5 (intrinsic partition-cut test).** Condition (8) holds if and only if for every partition
\(\mathcal P=\{R_1,\ldots,R_k\}\) of the vertex set \(R\) into \(k\ge2\) nonempty parts,
\[
\boxed{
\#\left\{\text{antipodal edge orbits containing an edge of }
G_R\text{ crossing }\mathcal P\right\}\ge k-1.
}
\tag{9}
\]
Thus (7) together with (9) gives a criterion expressed entirely by **disjoint antipodal graphic cocycles and edge-orbit matroid rank**, without quantification over edge colorings.

*Proof.* Apply the matroid-intersection min–max theorem to \(M(G_R)\) and \(P_\tau(R)\). For any edge subset \(F\subseteq E(G_R)\), the graphic rank is \(|R|-\kappa(F)\), where \(\kappa(F)\) is the number of connected components of \((R,F)\). The partition rank on \(E(G_R)\setminus F\) is the number of antipodal edge orbits represented there. Therefore the intersection has a common independent set of size \(|R|-1\) precisely when, for all \(F\),
\[
\#\{\text{orbits represented in }E(G_R)\setminus F\}
\ge\kappa(F)-1.
\]
The crossing edges of the component partition of \(F\) lie outside \(F\), so (9) implies the inequalities. Conversely, for an arbitrary partition \(\mathcal P\), take \(F\) to contain all edges internal to its parts. The remaining edges are its crossing edges and \(\kappa(F)\ge k\), proving (9). \(\square\)

#### 4. Consequences for the spanning-geodesic selector

For a cube coloring \(c\), take a red component \(R\) containing an antipodal pair. The component is subject simultaneously to (i) the graphic-rank amplification bound from the preceding Subsection, (ii) the antipodal cocycle separation (7), and (iii) the orbit-rainbow connectivity condition (8). The induced four-sector partition constrains every edge leaving \(R\) and every edge leaving its antipodal blue mate \(\tau R\).

These conditions provide an intrinsic matroidal class of admissible **monochromatic component supports**, not merely of signed turn graphs. Nevertheless, they characterize which supports are possible under *some* deck-odd coloring, not which edges inside such a support are red under a previously fixed coloring. A vertex-simple antipodal geodesic lying in \(Q_n[R]\) need not be red. Therefore the characterization alone does not establish NORI1.

The next closure problem is to combine the two-cut sector geometry with resource-simple fundamental-circuit exchange. It would suffice to prove that in every admissible fixed coloring, some self-antipodal red component contains a **red** shortest antipodal path. Disjoint graphic cocycle pairs and the partition-cut criterion are additional constraints that any purported counterexample must satisfy; in isolation they do not imply the desired distance equality.

#### 5. Shared specialization to both canonical systems

**Corollary 6 (common component-support structure).** Theorems 1–4 and Corollary 5 apply to both canonical Article XI graph coverings:

(i) the \(n\)-regular antipodal cube cover \(Q_n\to Q_n/\tau\), whose covering edges are cube edges; and

(ii) the \(2(n-2)\)-regular ordered-pair cover \(S(K_n)\to L(K_n)\) used for ordinary reversal-odd boundary 3-tournaments, whose covering edges are ordered triples \((a,b,c)\), with deck reversal \((c,b,a)\).

For both systems, every monochromatic component \(R\) and its opposite-colored deck image \(\tau R\) determine disjoint antipodal cut cocycles and the same four-sector constraints. A candidate monochromatic component support is realizable by a deck-odd coloring if and only if its antipodal cut pair is disjoint and its induced graph has an edge-orbit-rainbow spanning tree, equivalently the partition-cut inequalities (9).

*Proof.* In either cover, the deck involution acts freely on vertices and edges and complements edge-state colors. The proofs above use only those conditions and the graphic–partition matroid intersection theorem. \(\square\)

In the boundary model, the vertices of \(S(K_n)\) are ordered pairs of original vertices. Thus red connectivity of an ordered-pair component does not ensure a forward vertex-simple tight path. The shared cocycle and component-realizability structures are independent of, but compatible with, the additional original-resource matroid required for the spanning one-turn conjecture.

Let \(Q_n\) be the \(n\)-cube, \(n\ge3\), \(\tau(x)=x+\mathbf1_{[n]}\), and \(H_n=L(Q_n/\tau)\), whose \(n2^{n-2}\) vertices correspond to antipodal orbits of cube edges. Fix any order \(\pi=(1,\ldots,n)\) of coordinate directions. For a starting vertex \(x\), let \(C_x^\pi\subseteq H_n\) be the simple length-\(n\) turn cycle of the antipodal geodesic starting at \(x\) and visiting coordinates in order \(\pi\).

**Theorem 1 (geodesic vertex-disjoint packing).** For even \(n\ge4\), choose one representative \(x\) from each antipodal pair of even-parity cube vertices. The family of cycles \(C_x^\pi\), indexed by those \(2^{n-2}\) roots, partitions \(V(H_n)\) into pairwise vertex-disjoint cycles of length \(n\). In particular it is a 2-factor of \(H_n\), all of whose components are shortest odd-monodromy turn cycles.

For odd \(n\ge3\), choose every even-parity cube vertex \(x\) whose first two coordinates are zero. The resulting \(2^{n-3}\) cycles \(C_x^\pi\) are pairwise vertex-disjoint.

*Proof.* Along a fixed order \(\pi\), the state corresponding to direction \(i\) on the path from \(x\) is the cube edge starting at \(x\) translated by the fixed preceding-coordinate prefix. Suppose the projected edge states in direction \(i\) from roots \(x,y\) coincide. Two unoriented cube edges lie in the same antipodal orbit precisely when one is the other, its endpoint reversal, its antipodal translate, or the endpoint reversal of that translate. Translating away the common coordinate prefix gives
\[
\boxed{y\in\{x,\ x+e_i,\ \tau x,\ \tau x+e_i\}.}\tag{1}
\]
For even \(n\), both selected roots have even parity, excluding \(x+e_i\) and \(\tau x+e_i\). The two remaining possibilities are the same selected root or its antipode, and the latter is excluded by choosing one representative from each pair. Thus the cycles are vertex-disjoint. Their number times \(n\) equals \(|V(H_n)|\), proving the partition assertion.

For odd \(n\), \(x+e_i\) and \(\tau x\) have odd parity, so neither is selected. The point \(\tau x+e_i\) has at least one of its first two coordinates equal to one, whether \(i\) belongs to those two directions or not. Since all selected roots have both coordinates zero, this final possibility is also excluded. Their number is \(2^{n-3}\), proving the second assertion. \(\square\)

**Corollary 2 (pointed-cocircuit sunflower).** Let \(D_n\) be the pointed binary turn matroid and \(p\) its distinguished port. Each cycle \(C_x^\pi\) determines a shortest port cocircuit \(Y_x=E(C_x^\pi)\cup\{p\}\). The family of such cocircuits satisfies
\[
\boxed{Y_x\cap Y_y=\{p\}\quad(x\ne y),}\tag{2}
\]
and has cardinality \(2^{n-2}\) when \(n\) is even, and \(2^{n-3}\) when \(n\) is odd.

*Proof.* Disjoint turn-cycle vertex sets give disjoint turn-edge sets, while each port cocircuit contains \(p\). \(\square\)

**Theorem 3 (exponential-probability monochromatic NORI1).** Color each antipodal orbit of cube edges independently with an unbiased bit, giving its antipodal mate the complementary bit. Then the probability that the coloring has a monochromatic full antipodal geodesic obeys
\[
\boxed{
\Pr(\mathrm{NORI1\ witness})
\ge
\begin{cases}
1-\left(1-\dfrac{n}{2^{n-1}}\right)^{2^{n-2}}
\ge1-e^{-n/2},&n\text{ even},\\[6pt]
1-\left(1-\dfrac{n}{2^{n-1}}\right)^{2^{n-3}}
\ge1-e^{-n/4},&n\text{ odd}.
\end{cases}}\tag{3}
\]

*Proof.* For one fixed antipodal-geodesic turn cycle, the \(n\) cube-edge states belong to distinct antipodal edge orbits. Their edge colors are therefore independent unbiased bits. The cyclic comparison of consecutive states uses the deck complement of the first bit at the closing seam. The cyclic number of disagreements is one precisely when the linear color word is constant, or changes once between two constant blocks. There are \(2\) constant words and \(2(n-1)\) one-change words, among \(2^n\) equally likely words. Thus
\[
\Pr(w_d(C)=1)=\frac{2n}{2^n}=\frac{n}{2^{n-1}}.
\]
A cycle of cyclic turn weight one can be rerooted at its changed turn to give a monochromatic full antipodal geodesic. By Theorem 1, the cycles in the selected packing have disjoint edge-state orbit sets. Thus their weight-one events are independent. The complement of the event that at least one succeeds has probability \((1-n/2^{n-1})^k\), where \(k\) is the size of the packing. Substituting the two values of \(k\) gives (3); the exponential estimates follow from \(1-z\le e^{-z}\). \(\square\)

**Proposition 4 (why the full 2-factor is restricted to even dimension).** For odd \(n\), the turn graph \(H_n\) cannot have a partition of its vertices into antipodal-geodesic turn cycles, regardless of coordinate ordering.

*Proof.* Such a partition would cover every edge of the folded cube \(G_n=Q_n/\tau\) by edge-disjoint closed geodesic walks. Each component is a graph cycle, so their union would give every vertex of \(G_n\) even degree. But \(G_n\) is \(n\)-regular with \(n\) odd. This is impossible. \(\square\)

The two-factor theorem produces many independently testable shortest port cocircuits, and the probability bound quantifies how unlikely a counterexample is under an unbiased deck-odd coloring. It does not prove the worst-case conjecture: an adversarial coloring could make all members of one packing have at least three disagreements. Relations between different packings, rather than independence within a single packing, would be needed for a deterministic closure.

Let \(N\) be a finite loopless matroid of rank \(r\), let \(I_0\) be an independent set spanning the **anchor flat** \(F_0=\operatorname{cl}_N(I_0)\), and let \(B_1,B_2\) be independent resource sets containing \(I_0\). Put \(F_i=\operatorname{cl}_N(B_i)\).

**Theorem 1 (modular complementary-flat gluing).** If
\[
\boxed{
F_1\wedge F_2=F_0,\qquad
F_1\vee F_2=E(N),\qquad
r(F_1)+r(F_2)=r(F_0)+r(N),}
\tag{1}
\]
then
\[
\boxed{B_1\cap B_2=I_0,\qquad B_1\cup B_2\text{ is a basis of }N.}\tag{2}
\]
Conversely, if \(B_1\cap B_2=I_0\) and \(B_1\cup B_2\) is a basis, all three relations in (1) hold. Thus (1) characterizes pairs of **complementary modular flats over \(F_0\)** whose bases glue to one full resource basis.

*Proof.* Since \(B_i\) is independent and contains a basis \(I_0\) of \(F_0\), it cannot contain any further element of \(F_0\). A common element of \(B_1,B_2\) belongs to \(F_1\cap F_2=F_0\); hence their intersection is \(I_0\). The union therefore has cardinality
\[
|B_1\cup B_2|=r(F_1)+r(F_2)-r(F_0)=r(N).
\]
It spans \(F_1\vee F_2=E(N)\). A spanning set of size \(r(N)\) is a basis, proving (2).

Conversely, assume \(B_1\cap B_2=I_0\) and their union is a basis. Their closures jointly span \(N\), so \(F_1\vee F_2=E(N)\). The basis cardinality gives \(r(F_1)+r(F_2)-r(F_0)=r(N)\). By submodularity,
\[
r(F_1\cap F_2)\le r(F_1)+r(F_2)-r(F_1\vee F_2)=r(F_0).
\]
But \(F_0\subseteq F_1\cap F_2\), so their ranks agree; since both are flats, \(F_1\cap F_2=F_0\). All conditions in (1) follow. \(\square\)

**Theorem 2 (colored opposite-terminal gluing).** Suppose \(B_1,B_2\) arise from two same-colored coherent paths in a deck-reversal-odd path system, and their distinguished terminal states are opposite and compatible: reversing and deck-translating the second path can be concatenated with the first along the shared anchor, without introducing any additional turn. If their resource flats satisfy (1), the concatenated path uses a full basis of resources and has at most one color change.

*Proof.* The reversal-deck operation complements the colors of the second arm. By terminal compatibility the two arms concatenate into one coherent path, with no extra interior transition beyond their joining seam. Theorem 1 says their combined resource set, counting the anchor once, is a full independent basis. Each arm was monochromatic, and the transformed second arm has the opposite color, so the concatenation has at most one color change. \(\square\)

The compatibility hypothesis in Theorem 2 is essential: complementary matroid flats alone do not encode the order in which directed path states can be joined. The theorem isolates resource-basis gluing as a modular-flat property and forward coherence as a separate signed-cover condition.

**Corollary 4 (boundary graphic flats form a Boolean sublattice).** Fix an unordered pair {u,v} and put A=V without {u,v}. Among flats of the graphic matroid M(K_V), consider only F_S=E(K_{S union {u,v}}), for S subset A. They are a Boolean sublattice: F_S meet F_T=F_(S intersect T), F_S join F_T=F_(S union T), with rank r(F_S)=|S|+1. Every pair is modular. The flat F_empty is the common anchor edge {u,v}, and F_A is the full resource flat. Therefore two terminal arms have complementary modular flats if and only if their sets of visited vertices outside {u,v} are complementary subsets of A.

**Theorem 5 (opposite-terminal complementary-family criterion).** For an ordinary reversal-odd boundary 3-tournament on \(V\), fix distinct \(u,v\) and a color \(\varepsilon\). Put \(A=V\setminus\{u,v\}\), and define
\[
\mathcal R^\varepsilon_{uv}
=\{S\subseteq A:\text{there is a vertex-simple monochromatic }\varepsilon
\text{ tight path ending at }(u,v)
\text{ whose vertex set is }S\cup\{u,v\}\}.
\tag{4}
\]
The vacuous two-vertex path is allowed. Then the boundary tournament has a spanning tight path with at most one internal color change if and only if
\[
\boxed{
\exists u\ne v,\ \varepsilon,\ S\subseteq A:
S\in\mathcal R^\varepsilon_{uv},\quad
A\setminus S\in\mathcal R^\varepsilon_{vu}.}
\tag{5}
\]
Consequently, if the spanning one-turn conjecture fails for a coloring, then for every unordered pair \(\{u,v\}\) and both colors \(\varepsilon\),
\[
\boxed{
|\mathcal R^\varepsilon_{uv}|+
|\mathcal R^\varepsilon_{vu}|\le2^{n-2}.}\tag{6}
\]

*Proof.* The resource footprints of the two paths in (5) have original vertex sets meeting only at \(u,v\) and covering \(V\). Their terminal ordered pairs are opposite and their triple colors coincide. The opposite-terminal packing theorem in Article XI (or Theorem 2 above) joins them into a vertex-simple spanning path with at most one color change. Conversely, any such path splits at its color-change seam into two same-colored terminal arms after reversal of the suffix; for a monochromatic word take one arm to be the vacuous two-vertex path. Their outside vertex sets are complementary, proving (5). In the absence of any such witness, \(\mathcal R^\varepsilon_{uv}\) and the complement image \(\{A\setminus T:T\in\mathcal R^\varepsilon_{vu}\}\) are disjoint subsets of \(2^A\). Since complementation is a bijection, their cardinalities sum to at most \(2^{|A|}=2^{n-2}\). \(\square\)

**Comparison with the cube.** In the free-matroid cube automaton, NORI1 is equivalent to a complementary pair inside one rooted color-zero reachable family \(R_x\subseteq2^{[n]}\); failure imposes \(|R_x|\le2^{n-1}\) for every root. In the boundary system the same Boolean-complement obstruction acts *between* the two opposite-terminal families \(\mathcal R^\varepsilon_{uv}\) and \(\mathcal R^\varepsilon_{vu}\). The shared proposed proof principle is therefore a **complementary reachable-flat intersection theorem** for compatible monochromatic arms, rather than an unrestricted short-cocircuit intersection theorem. The counting bounds are necessary conditions for failure, not proofs that failure is impossible.

### Global antipodal graphic-flat covers and rainbow spanning-forest chambers

The preceding four-sector theorem describes one monochromatic component and its opposite-colored deck image. The following characterization instead controls the **entire partition of the covering graph into monochromatic components at once**. Its hypotheses and conclusions are intrinsic to a graphic matroid, an edge-free involutive automorphism, and the corresponding partition matroid on deck edge orbits. It applies to both the cube and the ordered-pair cover of ordinary boundary 3-tournaments.

Let \(G=(V,E)\) be a finite connected graph with a fixed-point-free involutive automorphism \(\tau\) acting freely on edges, and let \(M=M(G)\) be its graphic cycle matroid. For a partition \(\Pi\) of \(V\) into nonempty parts, define its graphic flat
\[
\boxed{
F_\Pi=\{uv\in E:u,v\text{ lie in the same part of }\Pi\}.
}
\tag{1}
\]
This is a flat of \(M\); its rank is \(r_M(F_\Pi)=|V|-|\Pi|\). The deck image \(\tau F_\Pi\) is the flat for the partition \(\tau\Pi\).

Call a forest \(T\subseteq F_\Pi\) **orbit-rainbow** if it contains at most one element from each two-element edge orbit \(\{e,\tau e\}\). Call it a **spanning forest of \(\Pi\)** if the connected components of \((V,T)\) are precisely the parts of \(\Pi\).

#### 1. Global flat-cover characterization

**Theorem 1 (antipodal flat-cover realization).** The partition \(\Pi\) is the partition of all vertices into color-zero connected components of some deck-odd edge coloring \(c:E(G)\to\mathbb F_2\) if and only if both conditions hold:
\[
\boxed{F_\Pi\cup\tau F_\Pi=E(G),}
\tag{2}
\]
and
\[
\boxed{\text{there exists an orbit-rainbow spanning forest }T
\text{ of }\Pi.}
\tag{3}
\]
Equivalently, with \(P_\tau\) the orbit partition matroid on \(E\),
\[
\boxed{
\max\{|T|:T\subseteq F_\Pi,\ 
T\in\mathcal I(M)\cap\mathcal I(P_\tau)\}
=r_M(F_\Pi)=|V|-|\Pi|.
}
\tag{4}
\]

*Proof.* Suppose \(c\) is deck-odd with red component partition \(\Pi\). Choose a spanning forest \(T\) in the red-edge subgraph. Every red edge has both endpoints in the same red component, so it belongs to \(F_\Pi\). The deck image of every blue edge is red and therefore lies in \(F_\Pi\), so every blue edge lies in \(\tau F_\Pi\). Thus \(E=F_\Pi\cup\tau F_\Pi\). The red forest \(T\) is independent in \(M\) and cannot contain both members of a deck edge orbit, since their colors are opposite; it spans all parts of \(\Pi\), proving (3).

Conversely, suppose (2) and (3). For each edge orbit \(\{e,\tau e\}\), at least one member belongs to \(F_\Pi\). If the orbit meets \(T\), declare its unique tree edge red and its mate blue. Otherwise select any member of the orbit lying in \(F_\Pi\) to be red, and its mate blue. These prescriptions are consistent because \(T\) is orbit-rainbow. They define a deck-odd coloring in which **every red edge lies in** \(F_\Pi\) and **every tree edge lies among the red edges**. Therefore no red edge joins two different parts of \(\Pi\), while \(T\) red-connects each part. The red component partition is \(\Pi\). \(\square\)

**Corollary 2 (all-component cut separation).** If \(\Pi\) is realizable, no graph edge simultaneously crosses a part boundary of \(\Pi\) and the corresponding boundary of \(\tau\Pi\). In other words, for every \(e=uv\),
\[
\boxed{
u\not\sim_\Pi v\ \Longrightarrow\ \tau u\sim_\Pi\tau v.
}
\tag{5}
\]
Here \(\sim_\Pi\) means belonging to the same part. For a specified red component \(R\in\Pi\), this implies the disjoint cocycles \(\delta(R)\cap\tau\delta(R)=\varnothing\) of the preceding Subsection.

*Proof.* Equation (2) says every edge is internal to \(\Pi\) or internal to \(\tau\Pi\). The two formulations are equivalent. If an edge leaves \(R\), it crosses \(\Pi\), so its deck image is internal to \(\Pi\), and cannot leave the corresponding deck image component. \(\square\)

This is stronger organizational information than imposing antipodal boundary separation on one red component at a time: it specifies a pair of **graphic-matroid flats that cover all covering edges simultaneously**.

#### 2. A global matroid-intersection cut test

**Theorem 3 (refinement-partition criterion).** Given a vertex partition \(\Pi\), the orbit-rainbow forest condition (3) is equivalent to the following inequalities. For every partition \(\mathcal Q\) of \(V\) that refines \(\Pi\),
\[
\boxed{
\#\bigl\{\{e,\tau e\}:
e\in F_\Pi\text{ joins distinct parts of }\mathcal Q\bigr\}
\ge |\mathcal Q|-|\Pi|.
}
\tag{6}
\]
Thus a proposed component partition is realizable precisely when its two antipodal graphic flats cover \(E\) and all inequalities (6) hold.

*Proof.* If an orbit-rainbow spanning forest \(T\) exists, then contracting each part of \(\mathcal Q\) within its containing \(\Pi\)-part requires at least \(|\mathcal Q|-|\Pi|\) forest edges crossing \(\mathcal Q\). Those forest edges belong to different deck orbits, proving (6).

For sufficiency, apply the matroid-intersection min–max theorem to the restrictions of \(M\) and \(P_\tau\) to \(F_\Pi\). For any \(A\subseteq F_\Pi\), let \(\mathcal Q\) be the partition of \(V\) into connected components of \((V,A)\). It refines \(\Pi\), with
\[
r_M(A)=|V|-|\mathcal Q|,\quad
r_M(F_\Pi)=|V|-|\Pi|.
\]
Every edge of \(F_\Pi\) crossing \(\mathcal Q\) lies in \(F_\Pi\setminus A\). Thus (6) gives
\[
r_{P_\tau}(F_\Pi\setminus A)
\ge|\mathcal Q|-|\Pi|
=r_M(F_\Pi)-r_M(A).
\]
This is the matroid-intersection min–max criterion for a common independent subset of \(F_\Pi\) of size \(r_M(F_\Pi)\). Such a common independent set is the required orbit-rainbow spanning forest of \(\Pi\). \(\square\)

#### 3. Boolean chambers of compatible colorings

For fixed \(\Pi\) satisfying (2) and any orbit-rainbow spanning forest \(T\) of \(\Pi\), let
\[
\mathcal O_{\rm amb}(\Pi)
=\{\{e,\tau e\}: e,\tau e\in F_\Pi\}
\tag{7}
\]
be the set of **ambiguous edge orbits**, whose two members are both internal to red components. Let \(\mathcal O(T)\) be the edge orbits represented by \(T\).

**Proposition 4 (basis chambers).** The family of all deck-odd colorings in which \(T\) is red and no red edge leaves a part of \(\Pi\) is an affine Boolean cube of dimension
\[
\boxed{
|\mathcal O_{\rm amb}(\Pi)\setminus\mathcal O(T)|.
}
\tag{8}
\]
In every such coloring, each edge in \(F_\Pi\setminus\tau F_\Pi\) is **forced red**, each edge in \(\tau F_\Pi\setminus F_\Pi\) is **forced blue**, and the remaining choices occur independently on the ambiguous orbits not constrained by \(T\). Every compatible coloring with red component partition \(\Pi\) belongs to at least one of these spanning-forest chambers.

*Proof.* For a deck orbit with only one member in \(F_\Pi\), that member must be red so red edges cannot leave the components; the other member is blue. For an orbit with both members in \(F_\Pi\), either orientation is permitted unless the orbit meets \(T\), in which case its tree member is forced red. The choices on distinct unconstrained orbits are independent. Each resulting coloring contains \(T\) and has red edges only in \(F_\Pi\), so its red components are the parts of \(\Pi\). Conversely, any coloring giving \(\Pi\) has a red spanning forest \(T\), belongs to the associated chamber, and meets the stated conditions. \(\square\)

**Corollary 5 (a forced-edge geodesic certificate).** In the antipodal cube, suppose a realizable partition \(\Pi\) has a monochromatic antipodal geodesic using only edges from the forced-red set \(F_\Pi\setminus\tau F_\Pi\). Then **every** deck-odd coloring with red component partition \(\Pi\) satisfies NORI1.

*Proof.* The edges of such a geodesic are red by Proposition 4 for every compatible coloring, so the path is a monochromatic full antipodal geodesic. \(\square\)

The certificate is sufficient, not asserted to hold in every realizable partition. In particular, when \(F_\Pi=E\), the forced-red set is empty, and the certificate does not apply.

#### 4. Relationship to both canonical pointed matroids

In the cube, the graphic matroid is \(M(Q_n)\) and \(\tau\) is coordinate complementation. In the ordinary boundary-tournament covering, use \(M(S(K_n))\), whose edge states are reversal-paired ordered triples. Both have the same full component-partition characterization (2), (4) and the refinement cut test (6).

This theorem coordinates *all* monochromatic components across the two sheets of their regular covering, beyond the Eulerian zero-turn contact graph and the local four-sector pair for a single component. It also exposes the coloring choices not fixed by component connectivity as independent ambiguous edge-orbit variables. Nevertheless, it does not alone prove the deterministic spanning-path targets. In the cube, geodesicity must still be certified by a red resource-simple antipodal path in at least one component; in the boundary model, the original-vertex graphic-resource independence and forward ordered-pair coherence remain additional requirements. The global flat-cover constraints give an intrinsic common class within which a future geodesic or one-turn selector theorem must operate.

#### 5. Global cycle-rank conservation

The flat-cover theorem gives a common partition-based representation; regularity imposes an additional **global graphic-matroid nullity budget** that cannot be detected inside a single component.

**Theorem 6 (fixed red cycle-rank budget).** Let \(G\) be a finite \(d\)-regular graph on \(N\) vertices with a free vertex-and-edge involution \(\tau\), and let \(c\) be any deck-odd edge coloring. Let \(\Pi_c\) be its partition into color-zero connected components, including isolated vertices, with \(\kappa=|\Pi_c|\). Then the nullity of its color-zero edge set in the graphic matroid \(M(G)\) is
\[
\boxed{
\dim Z(G_{\rm red})
=|E_{\rm red}|-r_M(E_{\rm red})
=\frac{(d-4)N}{4}+\kappa.
}
\tag{9}
\]
In particular,
\[
\boxed{
\sum_{R\in\Pi_c}
\left(|E_{\rm red}(R)|-|R|+1\right)
=\frac{(d-4)N}{4}+\kappa.
}
\tag{10}
\]

*Proof.* The covering graph has \(dN/2\) edges. Since every antipodal edge orbit consists of one red and one blue edge, \(|E_{\rm red}|=dN/4\), independently of the coloring. The graphic rank of the red subgraph is \(N-\kappa\), because its connected components are the parts of \(\Pi_c\), including isolated vertices. Subtracting rank from edge count proves (9); summing the component cyclomatic numbers proves (10). \(\square\)

**Corollary 7 (the two canonical budgets).** For an antipodally odd edge coloring of \(Q_n\), whose \(2^n\) vertices have degree \(n\),
\[
\boxed{\dim Z((Q_n)_{\rm red})=(n-4)2^{n-2}+\kappa.}
\tag{11}
\]
For an ordinary reversal-odd boundary coloring on the ordered-pair covering graph \(S(K_n)\), which has \(N=n(n-1)\) vertices and degree \(d=2(n-2)\),
\[
\boxed{
\dim Z((S(K_n))_{\rm red})
=\frac{n(n-1)(n-4)}2+\kappa.
}
\tag{12}
\]

The budget is global: it does **not** assert that every self-antipodal red component contains a red circuit. Research-note constructions in Q4–Q6 exhibit self-antipodal components that are trees, including one with a two-unit geodesicity defect. Such tree components contribute zero to (10), forcing the total cycle-rank budget to reside elsewhere. This is a rigorous indication that a successful matroid closure argument may need to compare distinct monochromatic components and their graphic cycles through the shared antipodal flat-cover constraints, rather than optimizing only one port-loop component.

### Boundary tournaments, antipodal graphic-flat matroids, and resource-basis packing

We verify that *every* ordinary reversal-odd boundary 3-tournament produces the antipodal graphic-flat and edge-orbit partition-matroid structure of Article XI. We also establish a distinction between the **basis-exchange quotient** and its covering graph, and reduce the spanning one-turn conjecture to the existence of a two-arm basis of the **separate** original-vertex graphic matroid.

#### 1. Cover and matroid construction

For \(n\ge4\), define \(\mathscr S_n\) to have vertices \((a,b)\), \(a\ne b\), and undirected edges
\[
\boxed{\{(a,b),(b,c)\}\quad(a,b,c\text{ distinct}).}
\tag{1}
\]
Each covering edge is indexed by its ordered triple \((a,b,c)\). Reversal \(\tau(a,b)=(b,a)\) exchanges the edges of \((a,b,c)\) and \((c,b,a)\). Thus
\[
\boxed{\mathscr S_n/\tau\cong L(K_n)=\Gamma(U_{2,n}),}
\tag{2}
\]
with a connected regular two-cover \(\mathscr S_n\to L(K_n)\). The cover is \(2(n-2)\)-regular, has \(N=n(n-1)\) vertices, and has \(N(n-2)\) edges.

Write \(\mathsf G_n=M(\mathscr S_n)\) for its graphic cycle matroid. Let \(\mathsf P_n\) be the partition matroid on covering edges with one two-element part \(\{e,\tau e\}\) per triple reversal-orbit, each of capacity one. Its rank is \(N(n-2)/2\).

**Theorem 1 (unrestricted boundary representation).** Reversal-odd boundary 3-tournaments are in bijection with the bases \(B\) of \(\mathsf P_n\): their zero-colored covering edges. For any such \(B\), let \(\Pi_B\) be the partition into connected components of \((V(\mathscr S_n),B)\) and let \(F_B=\operatorname{cl}_{\mathsf G_n}(B)\). Then
\[
\boxed{
F_B\cup\tau F_B=E(\mathscr S_n),\qquad
r_{\mathsf G_n}(B)=N-|\Pi_B|,
}
\tag{3}
\]
and
\[
\boxed{
|B|-r_{\mathsf G_n}(B)
=\frac{n(n-1)(n-4)}2+|\Pi_B|.
}
\tag{4}
\]
Conversely, a partition \(\Pi\) is the full zero-colored component partition of some reversal-odd boundary coloring if and only if its graphic flat \(F_\Pi\) covers \(E(\mathscr S_n)\) together with \(\tau F_\Pi\), and \(F_\Pi\) contains an orbit-rainbow spanning forest. By the graphic–partition matroid intersection theorem, the latter is equivalent to the refinement-partition cut inequalities already proved in the global flat-cover Subsection.

*Proof.* Each reversal-odd coloring selects one edge from every reversal-orbit as zero-colored; that is a basis of the orbit partition matroid, and every such basis gives a coloring. Every zero edge lies in its connected component, and the reversal of any one-colored edge is a zero edge, which proves the flat covering. The graphic rank is \(N\) minus the number of connected components, giving (3) and (4). The converse is the all-cover flat and rainbow-forest characterization from the preceding Subsection, applied to \(\mathscr S_n\). \(\square\)

It follows that **all** the shared antipodal cut, Eulerian contact-graph, global even-edge and graphic-flat results of Article XI apply to every boundary coloring. The pointed binary matroid from the induced cover of the turn graph \(L(L(K_n))\) is a second, compatible construction. No special coloring subclass is needed.

#### 2. The covering graph itself is not generally a basis graph

**Theorem 2 (basis-graph obstruction in unbounded orders).** The graph \(\mathscr S_n\) is not the basis-exchange graph of any matroid when \(n=4\) or \(n\ge8\).

*Proof.* Choose distinct original symbols \(a,b,c\) and vertices \(u=(a,b)\), \(v=(a,c)\) in \(\mathscr S_n\). They are not adjacent, and their common neighbors are
\[
\boxed{N(u)\cap N(v)=\{(x,a):x\notin\{a,b,c\}\}.}
\tag{5}
\]
Thus these two vertices are at distance two and possess \(n-3\) common neighbors. In every matroid basis graph, two vertices at distance two correspond to bases differing by two elements in each direction. All common neighbors exchange one of two elements for one of two others, giving at most four possibilities. Symmetric basis exchange supplies at least two distinct common neighbors. The number \(n-3\) violates the lower bound for \(n=4\) and the upper bound for \(n\ge8\). \(\square\)

Therefore the relevant **basis graph** is the quotient \(\Gamma(U_{2,n})=L(K_n)\); the covering graph has its own *graphic matroid*. Identifying these two layers would lead to an invalid universal basis-exchange argument.

#### 3. A second graphic matroid supplies the Hamilton resource constraint

The original-vertex resource matroid is
\[
\boxed{\mathsf R_n=M(K_n),}
\tag{6}
\]
distinct from \(\mathsf G_n=M(\mathscr S_n)\). A forward tight word \(P=(v_1,\ldots,v_k)\) is a directed-overlap path \((v_1,v_2)\to(v_2,v_3)\to\cdots\) in the covering graph, with resource edges
\[
E(P)=\{\{v_i,v_{i+1}\}:1\le i<k\}.
\tag{7}
\]
Starting from one original edge, requiring each appended resource edge to increase graphic rank in \(\mathsf R_n\) forces every appended original vertex to be new. An undirected same-color path in \(\mathscr S_n\) need not be a legal forward tight path because it may switch the overlap direction and revisit original vertices. Thus covering-graph connectivity, even between reversal-related oriented pairs, does not alone produce the desired tournament path.

**Theorem 3 (opposite-terminal basis packing).** Let \(P,Q\) be vertex-simple \(\varepsilon\)-monochromatic forward tight paths for the same color, ending in ordered pairs \((u,v)\) and \((v,u)\) respectively. A two-vertex arm is allowed. Then
\[
\boxed{
E(P)\cup E(Q)\in\mathcal I(\mathsf R_n)
\iff
V(P)\cap V(Q)=\{u,v\}.
}
\tag{8}
\]
Consequently,
\[
\boxed{
\text{A spanning one-turn boundary tight path exists}
\iff
\exists\,u,v,\varepsilon,P,Q:
E(P)\cup E(Q)\in\mathcal B(\mathsf R_n).
}
\tag{9}
\]
In this formulation, graphic independence automatically enforces disjoint interiors and the Hamilton path degree bound.

*Proof.* Delete the shared last edge \(\{u,v\}\). The remaining edges of \(P\) form one path attached to \(u\), and those of \(Q\) another path attached to \(v\). If the paths have no common additional vertex, their union with \(\{u,v\}\) is a simple path, hence graphic-independent. If they meet at some other original vertex, choose the first common meeting point from the two rooted ends. The two initial subpaths from \(u\) and \(v\), together with \(\{u,v\}\), form a graph cycle; hence their union is graphic-dependent. This proves (8). If the independent union is a graphic basis, its simple path contains all \(n\) original vertices. Reverse \(Q\), which reverses all its triple colors under boundary oddness, and splice it to \(P\) at the terminal pair to obtain a spanning path with at most one color change. Conversely, split a spanning one-turn path at its switch, reverse its second arm and use the two same-colored arms. When the path is monochromatic, use a vacuous two-vertex arm and the full reversed path. \(\square\)

The criterion (9) is the natural **integral matroid basis-packing target**. The difficult part is finding the two forward, color-compatible arms; their families do not satisfy ordinary greedoid augmentation in general, as shown by earlier Article XI research-note counterexamples. Generic matroid intersection on the covering graph \(\mathsf G_n\) is therefore insufficient without the directed resource-language constraint.

#### 4. Why a cube-specific port-loop axiom must be excluded

The cube's pointed contact graph always has a port-parallel loop by the known existence of a monochromatic antipodal path. The corresponding loop property fails for boundary tournaments: on four original vertices, the reversal-odd coloring with representative mask \(\mathrm{0x555}\), indexed by increasing middle symbol and then lexicographic outer pair \(a<c\), has a red covering graph consisting of four disjoint oriented three-cycles, one on each three-element original-vertex subset. No component contains both \((a,b)\) and \((b,a)\). The contact graph is \(K_4\) with four parallel copies of every edge. It is Eulerian, nonbipartite, even-sized, and loop-free. Hence its shortest unrestricted port intersection is four, rather than two. This example and an exhaustive enumeration of the 4096 order-four colorings are retained as a research note.

The **shared** matroid class is therefore the antipodal graph-cover, graphic-flat, orbit-partition, and pointed-binary construction. The **distinct admissible selectors** are (i) a displacement-minimal lifted fundamental circuit for the cube and (ii) an opposite-terminal union that is a basis of \(\mathsf R_n=M(K_n)\) for boundary tournaments. A unification theorem must preserve this second level of independent resources rather than replacing it by port parallelism.

#### 5. A pulled-back original-resource matroid on covering transitions

Fix the initial ordered pair \((u,v)\). For each covering edge
\[
e_{abc}=\{(a,b),(b,c)\}\in E(\mathscr S_n),
\]
label its original resource by \(\lambda(e_{abc})=\{b,c\}\in E(K_n)\). This is well-defined because an undirected covering edge has a unique ordered-triple index. Define the parallel-extension pullback matroid
\[
\boxed{\mathsf N_{uv}=\lambda^*(M(K_n)/\{u,v\})}
\tag{10}
\]
on the same covering-transition ground set as \(\mathsf G_n=M(\mathscr S_n)\). Thus \(A\subseteq E(\mathscr S_n)\) is independent in \(\mathsf N_{uv}\) if the resource labels \(\lambda(A)\) are distinct and
\[
\{\{u,v\}\}\cup\lambda(A)\in\mathcal I(M(K_n)).
\tag{11}
\]

**Theorem 4 (resource independence of coherent forward words).** A coherent forward covering-state path starting at \((u,v)\) with no repeated covering edge decodes to an injective original-vertex word if and only if its edge set is independent in \(\mathsf N_{uv}\). When these conditions hold, its edge set is also independent in the covering graphic matroid \(\mathsf G_n\).

*Proof.* The initial original edge \(\{u,v\}\) followed by the labels of the successive forward covering edges is the entire original edge sequence of the decoded word. An injective word traces a graph path with pairwise distinct original resource labels, so (11) holds. Conversely, revisiting an original vertex yields a closed nonbacktracking segment, because consecutive triples use three distinct original vertices. That segment either repeats a resource edge or contains a graph cycle, contradicting the label distinctness or original graphic independence in (11). For an injective word, its oriented-pair covering states are distinct, so the covering edges form a graph path and are independent in \(\mathsf G_n\). \(\square\)

**Proposition 5 (plain matroid intersection does not enforce coherent paths).** On five original vertices there exists a reversal-odd boundary coloring whose red covering edge set contains a common independent set of size \(n-2=3\) in \(\mathsf G_5\) and \(\mathsf N_{01}\), yet no red or blue spanning tight path exists.

*Proof.* Use the representative bit mask \(\mathrm{0x3ed25058}\), with representatives ordered by increasing middle vertex followed by increasing outer pair \(a<c\). The full \(5!=120\) word enumeration in the five-cycle sharpness Subsection establishes that all spanning words have at least one turn, so no monochromatic spanning word exists. Nevertheless, the three covering edges indexed by
\[
\boxed{(0,1,3),\ (0,1,4),\ (0,2,3)}
\tag{12}
\]
are red. They form a covering graph forest (two share only state \((0,1)\), and the third is disjoint). Their original resource labels are \(\{1,3\},\{1,4\},\{2,3\}\). Adding the initial resource \(\{0,1\}\) gives a spanning tree of \(K_5\). Hence the three covering edges are independent in both matroids, attaining resource rank \(3\), but they are not a single forward coherent state path. \(\square\)

This yields two graphic-derived matroids on the same boundary covering-edge set, plus the antipodal orbit partition matroid that parametrizes all reversal-odd colorings. Theorem 4 proves resource independence is an ordinary matroid constraint on directed forward paths. Proposition 5 shows a common independent set of full resource rank need not be a forward path: its **directed adjacency and route connectedness** must be retained as a separate admissibility condition. Thus a matroid-based spanning one-turn proof needs an exchange principle compatible with the coherent directed path language, not plain matroid intersection alone.

#### 6. Near-complete resource support in every boundary coloring

There is a strong universal abundance theorem for the original-resource labels of a **fixed** color, independent of any randomization or exchange choices.

Fix one color \(\varepsilon\), and let \(B_\varepsilon\) consist of covering edges of that color. Using the resource labeling \(\lambda(e_{abc})=\{b,c\}\), put
\[
\boxed{
\Lambda_\varepsilon=\lambda(B_\varepsilon)
\subseteq E(K_n).
}
\tag{13}
\]

**Theorem 6 (missing resources form a matching).** For every ordinary reversal-odd boundary 3-tournament on \(n\ge3\) vertices, and for each \(\varepsilon\in\{0,1\}\),
\[
\boxed{
E(K_n)\setminus\Lambda_\varepsilon
\text{ is a matching}.
}
\tag{14}
\]
In particular,
\[
\boxed{
|\Lambda_\varepsilon|\ge\binom n2-\left\lfloor\frac n2\right\rfloor,
\qquad r_{M(K_n)}(\Lambda_\varepsilon)=n-1.
}
\tag{15}
\]
Thus every fixed color appears on a collection of forward covering transitions whose **original-resource labels already span the full graphic resource matroid**.

*Proof.* For each middle vertex \(b\), restrict the boundary coloring to the ordered triples \((a,b,c)\) with \(a,c\ne b\). Reversal oddness makes the color-\(\varepsilon\) triples into the arcs of a tournament \(T_b^\varepsilon\) on \(V\setminus\{b\}\), oriented \(a\to c\) when \(b(a,b,c)=\varepsilon\). The resource edge \(\{b,c\}\) occurs as \(\lambda(e_{abc})\) for some color-\(\varepsilon\) triple with middle \(b\) if and only if \(c\) has positive indegree in \(T_b^\varepsilon\).

Suppose two missing resource edges \(\{b,c\}\) and \(\{b,d\}\) share the same vertex \(b\). Their absence implies both \(c\) and \(d\) have indegree zero in \(T_b^\varepsilon\). But a tournament has at most one vertex of indegree zero, because the edge between any two proposed sources must enter one of them. This is impossible. Hence the missing-edge graph has maximum degree at most one, proving (14). The stated cardinality bound follows. The complement of a matching in \(K_n\) is connected for \(n\ge3\); its graphic rank is \(n-1\). \(\square\)

**Corollary 7 (two forced outgoing fans).** If a resource edge \(\{b,c\}\) is absent from \(\Lambda_\varepsilon\), then for every \(a\notin\{b,c\}\),
\[
\boxed{
b(c,b,a)=\varepsilon,\qquad b(b,c,a)=\varepsilon.
}
\tag{16}
\]
Equivalently, both ordered-pair states \((c,b)\) and \((b,c)\) have all \(n-2\) possible **outgoing forward transitions** of color \(\varepsilon\).

*Proof.* Absence of resource \(\{b,c\}\) means each triple \((a,b,c)\) and \((a,c,b)\) has the opposite color \(1-\varepsilon\). Reverse both triples and apply reversal oddness. \(\square\)

The matching bound is attainable: the missing resource sets for the five-vertex mask \(\mathrm{0x3ed25058}\) in Proposition 5 are the two disjoint edges \(\{1,2\}\) and \(\{3,4\}\). More generally the independent local tournament choices at each middle vertex permit any prescribed matching as the missing color-\(\varepsilon\) resource support for \(n\ge4\): make the designated partner a zero-indegree source at each matched vertex, and choose source-free local tournaments at unmatched vertices.

This theorem clarifies why ordinary graphic rank arguments on \(\mathsf R_n\) alone cannot settle the spanning conjecture. Every color already has an almost-complete **resource support graph**, and therefore abundant spanning trees. The obstruction must occur in the directed overlap constraints coupling **successive** resource edges, not in the ability to select independent resources individually. The forced outgoing fans (16) may supply useful local rerouting operations for an eventual rank-preserving opposite-terminal exchange theorem.

#### 7. Missing resource edges are forced color-change gates

The outgoing-fan phenomenon in Corollary 7 has a dual incoming constraint. Let \(e=\{b,c\}\) be an original resource edge absent from the color-\(\varepsilon\) support \(\Lambda_\varepsilon\).

**Theorem 8 (forced phase gate at a missing resource).** For every \(a\notin\{b,c\}\),
\[
\boxed{
\begin{aligned}
b(a,b,c)&=1-\varepsilon,&
b(b,c,a)&=\varepsilon,\\
b(a,c,b)&=1-\varepsilon,&
b(c,b,a)&=\varepsilon.
\end{aligned}}
\tag{17}
\]
Consequently **every** coherent forward tight path that passes through either ordered-pair state \((b,c)\) or \((c,b)\) as an interior state makes a color change from \(1-\varepsilon\) to \(\varepsilon\) at that state. All incoming transitions to either state have color \(1-\varepsilon\), and all outgoing transitions have color \(\varepsilon\).

*Proof.* The first and third displayed triples have resource label \(\{b,c\}\) in the color-\(\varepsilon\) resource map. Since this label is absent, both triples have color \(1-\varepsilon\). The second and fourth triples are their reversal pairs, so reversal oddness forces color \(\varepsilon\). The incoming and outgoing transition description follows from the ordered-pair covering graph. \(\square\)

**Corollary 9 (forced-gate packing restriction).** Let \(F_\varepsilon=E(K_n)\setminus\Lambda_\varepsilon\), a matching by Theorem 6. In any spanning tight word with at most one internal color change, there is at most one consecutive original pair from \(F_\varepsilon\) occurring as an interior ordered-pair state; if such a pair occurs, the unique change is from \(1-\varepsilon\) to \(\varepsilon\) at that pair. A monochromatic spanning tight word cannot contain any missing-resource pair as an interior state. The endpoints of the word may contain such a pair without triggering an internal comparison.

Theorem 8 converts a missing resource into a **deterministic two-color switching interface**. In particular, instead of treating missing labels solely as rank defects, a proposed spanning one-turn proof may use one as its intended seam and seek two independent monochromatic arms attaching on opposite sides. The missing edges themselves form a matching, so there can be no overlapping gate constraints based at the same original vertex. This is a structural lead, not a completed spanning one-turn theorem.

#### 8. A common full-rank resource-cocircuit axiom for cube and boundary models

The resource-support theorem has a direct counterpart in NORI1 and therefore supplies another **intrinsic hypothesis shared by the two canonical models**.

Let \(\mathsf R\) denote the original-resource matroid of a polarized exchange-gallery system and \(\Lambda_\varepsilon\) the set of resource labels occurring on primitive states or forward transitions of color \(\varepsilon\). Consider the matroid property
\[
\boxed{
r_{\mathsf R}(\Lambda_0)
=r_{\mathsf R}(\Lambda_1)
=r(\mathsf R).
}
\tag{18}
\]
Equivalently, **each color support meets every cocircuit of the original-resource matroid**. This equivalence is standard: a set spans a matroid if and only if it intersects every cocircuit.

**Theorem 10 (common cocircuit-hitting resource supports).** Both canonical Article XI models satisfy (18) for every permitted reversal-odd coloring, with the following refinements.

(a) For the antipodal \(n\)-cube, \(\mathsf R\) is the free matroid on the \(n\) coordinate directions. Each color occurs on precisely \(2^{n-2}\) edges of each coordinate direction, for \(n\ge2\). In particular, \(\Lambda_0=\Lambda_1=[n]\), and each color meets every singleton cocircuit.

(b) For the ordinary boundary 3-tournament, \(\mathsf R=M(K_n)\), and for every nonempty proper \(S\subset[n]\),
\[
\boxed{
|\Lambda_\varepsilon\cap\delta_{K_n}(S)|
\ge |S|(n-|S|)-\min(|S|,n-|S|).
}
\tag{19}
\]
Consequently the resource-support graph \(([n],\Lambda_\varepsilon)\) is \((n-2)\)-edge-connected for every \(n\ge3\), and it contains a Hamilton cycle whenever \(n\ge4\).

*Proof.* For (a), the \(2^{n-1}\) cube edges of any coordinate direction split into \(2^{n-2}\) antipodal edge pairs, and reversal oddness selects one edge of each color in each pair. For (b), Theorem 6 says the missing resource-edge graph is a matching. At most \(\min(|S|,n-|S|)\) edges of that matching cross a cut \(\delta(S)\), proving (19). Its minimum over nontrivial \(S\) is at least \(n-2\) for \(n\ge3\), giving the edge-connectivity bound. Since the support graph has minimum degree at least \(n-2\ge n/2\) for \(n\ge4\), Dirac's Hamilton-cycle theorem applies. \(\square\)

The common full-rank cocircuit-hitting condition (18) is a natural addition to the proposed abstract class of **polarized resource-exchange matroids**. It is an all-color, all-dimensional restriction stronger than merely saying that the uncolored gallery system admits every resource permutation. But it is still not a path selector: the five-vertex counterexample in Proposition 5 has almost-complete full-rank red resource support and even a Hamilton resource cycle, without any coherent monochromatic spanning tight path. A closure proof must exploit **how** these abundant resource labels are realized by adjacent colored covering transitions.

#### 9. Matroid base-packing abundance for each color

The cocircuit-hitting theorem also yields a quantitative **spanning-basis packing** result for the color-specific resource supports. This survives in arbitrarily large order and can be useful for future exchange arguments that must avoid a bounded set of resource labels.

**Theorem 11 (boundary spanning-tree packing).** For an ordinary reversal-odd boundary 3-tournament on \(n\ge4\) vertices, let \(B_\varepsilon\) be the colored covering edges and let \(\Lambda_\varepsilon=\lambda(B_\varepsilon)\). Then \(\Lambda_\varepsilon\) contains at least
\[
\boxed{k_n=\left\lfloor\frac{n-2}{2}\right\rfloor}
\tag{20}
\]
pairwise edge-disjoint spanning trees of \(K_n\). Equivalently, the pullback resource matroid
\[
\lambda^*M(K_n)
\]
on the covering-transition ground set contains \(k_n\) pairwise disjoint bases comprised entirely of color-\(\varepsilon\) transitions.

*Proof.* By Theorem 10(b), the resource-support graph \(([n],\Lambda_\varepsilon)\) is \((n-2)\)-edge-connected, hence \(2k_n\)-edge-connected. For every partition of its vertex set into \(t\ge2\) nonempty parts, each part has at least \(2k_n\) crossing incidences. Counting edges crossing between parts twice gives at least \(k_n t\ge k_n(t-1)\) such edges. The Nash-Williams–Tutte spanning-tree packing criterion therefore supplies \(k_n\) edge-disjoint spanning trees. For each tree edge choose one color-\(\varepsilon\) covering transition with that resource label. Since the trees have disjoint resource-edge sets, these choices give disjoint bases of the parallel-extension pullback matroid. \(\square\)

**Proposition 12 (cube analogue).** For the antipodally odd \(n\)-cube, \(n\ge2\), let \(\lambda\) label each colored cube edge by its coordinate direction and let \(\mathsf R\) be the free matroid on \([n]\). For either fixed color, the parallel-extension pullback \(\lambda^*\mathsf R\) on the cube-edge set contains
\[
\boxed{2^{n-2}}
\tag{21}
\]
pairwise disjoint full-rank bases, and no larger number is possible.

*Proof.* In each direction there are precisely \(2^{n-2}\) edges of each color, by Theorem 10(a). A basis of the parallel-extension free matroid chooses one edge in every direction. Pair the direction-\(i\) edges arbitrarily with the indices \(1,\ldots,2^{n-2}\); selecting the edges with the same index across all directions gives \(2^{n-2}\) disjoint bases. Conversely every such basis consumes one colored edge of each direction, and only \(2^{n-2}\) are available. \(\square\)

Hence **both canonical models have many single-color full-rank resource bases**, in addition to the covering graphic-flat and pointed binary matroid structure. The quantitative base-packing property is still weaker than the spanning-path conjectures, because independent resource representatives chosen from different covering states need not be geometrically adjacent or coherently directed. The challenge is to turn this substantial matroid-rank redundancy into a **coherent basis-path selector** using covering monodromy and the antipodal path language.

#### 10. Common two-color resource bases and the rarity of forced gates

The preceding full-rank and base-packing statements concern each color separately. The two colors also share a substantial **common** graphic resource support, even in worst-case tournaments.

Let \(F_\varepsilon=E(K_n)\setminus\Lambda_\varepsilon\) denote the color-\(\varepsilon\) missing-resource matching, and define
\[
\boxed{
H_b=([n],\Lambda_0\cap\Lambda_1)
=K_n-(F_0\cup F_1).
}
\tag{22}
\]

**Theorem 13 (simultaneous full rank and Hamiltonian common support).** For every ordinary reversal-odd boundary tournament:
\[
\boxed{
F_0\cap F_1=\varnothing,\quad
\Delta(F_0\cup F_1)\le2,\quad
\delta(H_b)\ge n-3.
}
\tag{23}
\]
Consequently, for \(n\ge5\),
\[
\boxed{r_{M(K_n)}(\Lambda_0\cap\Lambda_1)=n-1;}
\tag{24}
\]
for \(n\ge6\), \(H_b\) has a Hamiltonian cycle; and for \(n\ge7\), \(H_b\) is Hamilton-connected.

*Proof.* A resource edge \(\{u,v\}\) cannot be absent from both color supports, since each ordered triple entering the state \((u,v)\) has one of the two colors and would represent that same resource edge. Thus \(F_0\cap F_1=\varnothing\). By Theorem 6 each \(F_\varepsilon\) is a matching, so their union has maximum degree at most two, proving (23). For \(n\ge5\), each component of \(H_b\) contains at least \(\delta(H_b)+1\ge n-2\) vertices. Two components would require at least \(2(n-2)>n\) vertices, impossible; thus \(H_b\) is connected and its original graphic resource rank is \(n-1\). For \(n\ge6\), \(\delta(H_b)\ge n-3\ge n/2\), so Dirac's theorem gives a Hamiltonian cycle. For \(n\ge7\), every pair of nonadjacent vertices has degree sum at least \(2(n-3)\ge n+1\); Ore's Hamilton-connectedness theorem gives a Hamilton path between any prescribed pair of vertices. \(\square\)

The common-support graph omits a graph of maximum degree two whose components are isolated vertices, alternating paths, and even alternating cycles (the two omitted matchings alternate in any nontrivial cycle). In particular, **the same original resource basis can be represented by transitions of either color**, though the two representations need not be coherently adjacent or have compatible roots.

**Corollary 14 (any designated gate can occupy the unique unsupported position).** Let \(n\ge7\), and let \(e=\{u,v\}\in F_0\cup F_1\) be any missing-resource edge. There exists a Hamiltonian vertex order \(w\) containing \(u,v\) consecutively in an *interior* position, such that
\[
\boxed{
E(w)\setminus\{e\}\subseteq\Lambda_0\cap\Lambda_1.
}
\tag{25}
\]

*Proof.* By Theorem 13, the common-support graph \(H_b\) has a Hamiltonian path with prescribed endpoints \(u,v\). Adding the missing edge \(e=uv\) closes this path into a Hamiltonian cycle in which \(e\) is the sole edge outside \(H_b\). Delete a cycle edge not incident with \(e\) to obtain a spanning Hamiltonian path in which \(e\) is an interior resource edge and all other resource edges belong to both color supports. \(\square\)

This is a **resource-geometric**, not a colored-forward-path, statement: the color-\(\varepsilon\) representative of each common resource edge may occur at a completely different ordered-pair state. The theorem shows that the *placement* of a forced switching gate is never obstructed by ordinary graphic basis availability in orders \(n\ge7\). Forward path coherence remains the difficulty.

**Proposition 15 (forced gates are exponentially rare under random coloring).** Under the uniform probability measure on reversal-odd boundary 3-tournaments,
\[
\boxed{
\mathbb E|F_\varepsilon|
=\binom n2\,2^{-2(n-2)},\qquad
\Pr(F_0\cup F_1\ne\varnothing)
\le n(n-1)\,2^{-2(n-2)}.
}
\tag{26}
\]
In particular, with probability \(1-O(n^2 4^{-n})\), the **two** resource supports both equal the entire edge set \(E(K_n)\); no forced switching gate exists.

*Proof.* For a given edge \(\{u,v\}\), its absence from \(\Lambda_\varepsilon\) requires that all \(n-2\) ordered triples entering \((u,v)\) have color \(1-\varepsilon\), and likewise all \(n-2\) triples entering \((v,u)\). These are \(2(n-2)\) distinct reversal-pair bits: the first group has middle vertex \(u\), the second middle vertex \(v\), and no pair is the reversal of another in the same group or across groups. They are independent fair bits, so the absence event has probability \(2^{-2(n-2)}\). Sum over the \(\binom n2\) possible edges and use Markov's inequality and a union bound over both colors to obtain (26). \(\square\)

**Research limitation and next target.** The missing-resource matching and its phase gates are valuable *conditional* rerouting devices, but Proposition 15 rules out any universal proof that requires at least one missing resource: nearly all colorings have none. The stronger shared full-rank property (24) remains available even then. The natural missing theorem is therefore a **coherent basis-path synchronization principle**, converting the two full-color representatives of a common resource basis into oppositely rooted monochromatic arms whose union is independent, with at most one phase seam. Neither ordinary graphic matroid intersection nor uncolored Hamiltonicity implies that synchronization, as the preceding finite obstructions demonstrate.

### Conflict-graph purification and robust transfer of monotone paths

Let \(V\) be an \(n\)-element set, \(n\ge3\). A *boundary coloring* is a map \(b:V_{\ne}^3\to\{0,1\}\) satisfying \(b(c,v,a)=1-b(a,v,c)\). Let \(\prec\) be a total ordering of \(E(K_V)\), and let
\[
b_\prec(a,v,c)=\mathbf 1_{\{av\prec vc\}}.
\]
Reversing a triple complements this value. Denote by
\[
m=m(b,\prec)=\bigl|\{\{(a,v,c),(c,v,a)\}:b(a,v,c)\ne b_\prec(a,v,c)\}\bigr|
\]
the number of erroneous reversal classes of ordered triples. Every such class represents an unordered pair of incident edges of \(K_V\).

**Theorem 1 (conflict-graph purification).** There is a spanning graph \(G\subseteq K_V\) satisfying
\[
\boxed{\quad
\frac{2|E(G)|}{n}\ \ge\
d_{n,m}:=\frac{n-1}{1+\frac{4m}{n(n-1)}} ,
\quad} \tag{1}
\]
such that for every ordered triple \((a,v,c)\) of distinct vertices with \(av,vc\in E(G)\),
\[
\boxed{b(a,v,c)=b_\prec(a,v,c).} \tag{2}
\]
Consequently, every path of strictly increasing edge labels in \(G\) is a vertex-simple monochromatic tight path of color \(1\) in \(b\). The same holds for decreasing edge labels, of color \(0\).

*Proof.* Form the conflict graph \(J\) with vertex set \(E(K_V)\). Join two vertices \(av,vc\in E(K_V)\) whenever their comparison is erroneous, namely when \(b(a,v,c)\ne b_\prec(a,v,c)\). The reversal identity makes this condition independent of ordering the pair. Thus
\[
|V(J)|=Q:=\binom n2,\qquad |E(J)|=m.
\]
For any finite graph \(J\), its independence number satisfies the Caro–Wei bound
\[
\alpha(J)\ge\sum_{e\in V(J)}\frac{1}{1+\deg_J(e)}
\ge\frac{Q^2}{Q+2m}. \tag{3}
\]
For completeness, randomly order \(V(J)\) and retain each vertex earlier than all its neighbors; the retained vertices are pairwise nonadjacent, and each is retained with probability \(1/(1+\deg_J(e))\). Taking expectations proves the first inequality; Cauchy–Schwarz proves the second.

Choose an independent vertex set \(F\subseteq V(J)\) attaining the lower bound (3), and take \(G=(V,F)\). Independence states precisely that no two incident edges of \(G\) give an erroneous triple, proving (2). Since \(Q=n(n-1)/2\), the lower bound (3) gives
\[
\frac{2|F|}{n}\ge\frac{2Q^2}{n(Q+2m)}
=\frac{n-1}{1+4m/[n(n-1)]},
\]
which proves (1). For a strictly increasing path \(v_0v_1\cdots v_\ell\) in \(G\), every consecutive pair of its edges has the comparison color \(1\) in \(b_\prec\), hence by (2) in \(b\). Since it is a graph path, the vertices are distinct. \(\square\)

Define the *altitude* \(f(G)\) to be the minimum, over all total orders of \(E(G)\), of the greatest length in edges of an increasing vertex-simple path. Then Theorem 1 immediately gives \(L(b)\ge f(G)\), where \(L(b)\) is the maximum number of edges in a monochromatic vertex-simple tight path. To quantify this, use the published theorem of Bucić, Kwan, Pokrovskiy, Sudakov, Tran and Wagner, *Nearly-linear monotone paths in edge-ordered graphs*, Israel J. Math. **238** (2020), 663–685, Theorem 1.2: for an \(n\)-vertex graph of average degree \(d\ge2\),
\[
f(G)\ge \frac{d}{2^{C\sqrt{\log_2 d\,\log_2\log_2 n}}} \tag{4}
\]
for an absolute constant \(C\). The classical lower bound of Rödl gives \(f(G)\ge c\sqrt d\) for a universal \(c>0\).

**Corollary 2 (robust monotone-path transfer).** Let \(d_{n,m}\) be given by (1). Whenever \(d_{n,m}\ge2\),
\[
\boxed{
L(b)\ge \max\left\{
c\sqrt{d_{n,m}},
\ \frac{d_{n,m}}{2^{C\sqrt{\log_2 d_{n,m}\,\log_2\log_2 n}}}
\right\}.} \tag{5}
\]
In particular, as \(n\to\infty\):

(a) If \(m=o(n^2)\), then \(L(b)\ge n^{1-o(1)}\).

(b) If \(m=O(n^{2+\delta})\) for fixed \(0<\delta<1\), then \(L(b)\ge n^{1-\delta-o(1)}\).

(c) If \(m=o(n^3)\), then \(L(b)\to\infty\), quantitatively \(L(b)=\Omega(\sqrt{\min\{n,n^3/m\}})\) when \(m>0\). In the equivalent normalized notation \(m=\eta n^3\), this is \(\Omega(\min\{\sqrt n,\eta^{-1/2}\})\). The zero-error case is covered by (a).

*Proof.* Both bounds of (5) apply to the purified graph from Theorem 1; each increasing path transfers by (2). Under (a), \(d_{n,m}=n(1-o(1))\). Under (b), \(d_{n,m}=\Omega(n^{1-\delta})\). The denominator of the second expression of (5) is \(n^{o(1)}\) whenever \(d_{n,m}\) is a positive power of \(n\), proving (a) and (b). Under (c), (1) implies \(d_{n,m}=\Omega(\min\{n,n^3/m\})\to\infty\), and the first expression in (5) applies. \(\square\)

**Corollary 3 (spectrally near-extremal boundary colorings).** Suppose \(b\) has legal-turn disagreement density \(D(b)/E_n\), and put
\[
z=\max\{0,2/3-D(b)/E_n\}+\frac{n-2}{2(n-3)(n-1)}.
\]
The preceding edge-order synchronization theorem supplies an ordering \(\prec\) for which
\[
m(b,\prec)\le C_0 n(n-1)(n-2)z^{1/9}
\]
for an absolute constant \(C_0\). Applying Theorem 1 gives a comparison-faithful graph of average degree at least
\[
\boxed{d\ge\frac{n-1}{1+4C_0(n-2)z^{1/9}}.} \tag{6}
\]
Corollary 2 now applies with this lower bound. In particular, a polynomially small synchronization error \(m=O(n^{2+\delta})\) yields a monochromatic path of length \(n^{1-\delta-o(1)}\).

The case \(m=o(n^3)\) gives an unbounded path but does not itself imply a path of length \(n^{1-o(1)}\). A stronger transfer would have to exploit path-wise avoidance of errors while retaining many adjacent edges of the ordered complete graph. The conflict-free subgraph in Theorem 1 is a graph-theoretic comparison certificate; the path's original-vertex simplicity is preserved by its graphic-matroid independence.

### Random smoothing and the failure of global edge-order purification

Let \(V\) be a set of \(n\) vertices, \(n\ge3\). A reversal-odd coloring is a map \(b_0:V_{\ne}^3\to\{0,1\}\) satisfying \(b_0(c,v,a)=1-b_0(a,v,c)\). Fix \(0<\rho\le1/2\). Independently for each reversal class \(\{(a,v,c),(c,v,a)\}\), choose a Bernoulli random variable \(Z_{\{a,v,c\}}\) of parameter \(\rho\), and define
\[
b(a,v,c)=b_0(a,v,c)\oplus Z_{\{a,v,c\}}.
\tag{1}
\]
Thus \(b\) is again reversal-odd.

**Theorem 1 (near-spanning paths after independent perturbation).**
Fix an ordered pair \(u,v\) of distinct vertices, a color \(\epsilon\in\{0,1\}\), and \(0<\delta<1\). Put
\[
r=\left\lceil \rho^{-1}\log(n/\delta)\right\rceil .
\]
If \(r\le n-2\), then with probability at least \(1-\delta\), the coloring \(b\) admits a vertex-simple \(\epsilon\)-monochromatic tight path beginning with \(u,v\), using at least \(n-r\) vertices. In particular, when \(\rho n/\log n\to\infty\), with probability tending to one every ordered starting pair and each prescribed color admits such a path on \(n-O(\rho^{-1}\log n)\) vertices.

*Proof.* Build a sequence \(v_1=u,v_2=v,\ldots\) by greedily appending any unused \(w\) for which \(b(v_{i-1},v_i,w)=\epsilon\). To decide whether the next extension exists, reveal the colors of the triples \((v_{i-1},v_i,w)\) for unused \(w\). Every one of their reversal classes has middle vertex \(v_i\). The vertices \(v_i\) used as centers at successive stages are distinct, hence none of these classes has been queried at an earlier stage. Conditional on the complete past of the algorithm, the new bits are independent and each has probability at least \(\rho\) of yielding the desired color, whatever the deterministic values of \(b_0\). If \(k\) vertices remain unused, the conditional probability of failure is at most
\[
(1-\rho)^k\le e^{-\rho k}.
\]
Before \(n-r\) vertices have been used, \(k\ge r\), and there are at most \(n\) opportunities to fail. A union bound gives probability of failure at most \(ne^{-\rho r}\le\delta\). For the uniform assertion choose \(r=\lceil6\rho^{-1}\log n\rceil\), giving failure probability at most \(n^{-5}\) for each of fewer than \(2n^2\) starting-pair/color choices. A final union bound completes the proof. \(\square\)

A spanning subgraph \(G\subseteq K_V\) is called *comparison-orderable for \(b\)* if some strict total ordering of \(E(G)\) induces \(b(a,v,c)\) on every pair of incident edges \(av,vc\in E(G)\). Such a graph has a transitive induced subtournament on \(N_G(v)\) for every vertex \(v\): its local arc \(a\to c\) is defined by \(b(a,v,c)\), and a single ordering of the incident edges at \(v\) determines all its arcs.

**Lemma 2 (edge-disjoint triangle packing).** For any integer \(d\ge3\), the complete graph \(K_d\) contains at least \(d(d-1)/18\) triangles with pairwise disjoint edge sets.

*Proof.* Greedily select a triangle and remove every triangle sharing one of its three edges. Each selection removes at most \(3(d-2)\) triangles, while \(K_d\) originally contains \(\binom d3\) triangles. At least \(\binom d3/[3(d-2)]=d(d-1)/18\) selections are possible. \(\square\)

**Theorem 3 (uniform obstruction to comparison-orderable subgraphs).**
For every deterministic baseline \(b_0\), with probability tending to one as \(n\to\infty\), every comparison-orderable spanning subgraph \(G\subseteq K_V\), even allowing its edge ordering to depend on \(b\) and \(G\), satisfies
\[
\boxed{\quad
\Delta(G)<\left\lceil\frac{200\log n}{\rho}\right\rceil
\quad\text{whenever the right side is at most }n-1.\quad}
\tag{2}
\]
Consequently all such \(G\) satisfy
\[
\boxed{\quad |E(G)|=O\!\left(\frac{n\log n}{\rho}\right). \quad}
\tag{3}
\]
The implicit constant is absolute, independent of \(b_0\).

*Proof.* Fix a center \(v\) and a \(d\)-set \(S\subseteq V\setminus\{v\}\), where \(d=\lceil200(\log n)/\rho\rceil\le n-1\). For a triple \(\{a,c,e\}\subseteq S\), the restriction of the tournament \(b(\cdot,v,\cdot)\) to those three vertices is cyclic with probability at least \(\rho/4\). Indeed, if it is transitive in \(b_0\), flipping just the comparison between the first and last vertices in its transitive order produces a directed cycle, with probability \(\rho(1-\rho)^2\ge\rho/4\). If it is initially cyclic, keeping all three comparisons unchanged has probability \((1-\rho)^3\ge1/8\ge\rho/4\).

Choose the edge-disjoint triangle packing of Lemma 2 on \(S\). The corresponding cyclic-triangle events involve disjoint comparison variables and are therefore independent. Since there are at least \(d(d-1)/18\) such triangles,
\[
\Pr\bigl(b(\cdot,v,\cdot)|_S\text{ is transitive}\bigr)
\le\left(1-\frac{\rho}{4}\right)^{d(d-1)/18}
\le \exp\left(-\frac{\rho d(d-1)}{72}\right).
\]
The probability that some \(v\) and \(d\)-set \(S\) have a transitive induced local tournament is at most
\[
n\binom{n-1}{d}\exp\left(-\frac{\rho d(d-1)}{72}\right)
\le n\exp\left(d\log n-\frac{\rho d(d-1)}{72}\right)=o(1).
\tag{4}
\]
The last relation follows from \(d\ge200(\log n)/\rho\). On the complementary event, no comparison-orderable graph can have a vertex of degree at least \(d\), since that vertex's neighbor set contains such a transitive \(d\)-set. This proves (2). If \(d>n-1\), (3) is trivial from \(|E(G)|\le\binom n2\); otherwise use the degree bound. \(\square\)

**Corollary 4 (near-extremal coloring with almost-spanning paths but no dense orderable subgraph).**
There exist reversal-odd boundary colorings \(b_n\) on \(n\) vertices for which simultaneously
\[
\boxed{\frac{D(b_n)}{E_n}\ge \frac23-O(n^{-1/3}),}\tag{5}
\]
every ordered pair and both colors initiate a monochromatic tight path on \(n-O(n^{1/3}\log n)\) vertices, and every comparison-orderable subgraph \(G\subseteq K_n\) satisfies
\[
\boxed{|E(G)|=O(n^{4/3}\log n),\qquad
\Delta(G)=O(n^{1/3}\log n).}\tag{6}
\]
Here \(D(b)\) counts disagreeing edges of the legal-turn reversal quotient and \(E_n=n(n-1)(n-2)(n-3)/2\).

*Proof.* Randomly assign distinct real labels to \(E(K_n)\), and let \(b_0\) compare consecutive edge labels. Each legal turn \((a,b,c,d)\) involves three distinct edges with independent labels, so the probability of a changed comparison is \(2/3\). By averaging, there exists a deterministic edge order with \(D(b_0)/E_n\ge2/3\). Perturb this \(b_0\) as in (1) with \(\rho=n^{-1/3}\).

The two reversal classes involved in each legal turn are distinct, so their flips are independent. Write \(h=2\rho(1-\rho)\). The perturbed turn disagrees with probability \(h+(1-2h)d_0\), where \(d_0\in\{0,1\}\) is its original disagreement bit. Since \(1-2h=(1-2\rho)^2\ge0\),
\[
\frac{\mathbb E D(b)}{E_n}
=h+(1-2h)\frac{D(b_0)}{E_n}
\ge\frac23-\frac h3\ge\frac23-\frac23\rho.
\tag{7}
\]
There are \(N_n=n\binom{n-1}{2}\) independently perturbed reversal classes, and changing one flip changes \(D\) by at most \(2(n-3)\). The bounded-differences inequality therefore gives, for any \(t>0\),
\[
\Pr\left(\frac{D(b)}{E_n}<\frac{\mathbb E D(b)}{E_n}-t\right)
\le \exp(-t^2N_n/2).
\tag{8}
\]
Taking \(t=\rho\) proves (5) with probability tending to one. Theorem 1, with \(\delta=n^{-5}\) and a union bound over all starting ordered pairs and colors, gives the claimed paths. Theorem 3 gives (6). All three events occur simultaneously with probability tending to one, proving existence. \(\square\)

The contrast is structural: even when an unrestricted boundary coloring is arbitrarily close in normalized disagreement density to the extremal value \(2/3\), and supports near-spanning monochromatic paths, a subgraph on which *any* total edge ordering realizes all its local comparisons may have only \(O(n^{4/3}\log n)\) edges. Resource-simple paths can navigate mutually incompatible comparisons globally, so an exchange theorem seeking long paths must retain only the comparisons used by the evolving witness rather than insist upon one global edge-order representation.

**Theorem 5 (near-geodesic smoothing of antipodally odd cube colorings).**
Let \(Q_n\) be the \(n\)-dimensional cube, let \(c_0:E(Q_n)\to\{0,1\}\) satisfy \(c_0(\tau e)=1-c_0(e)\), where \(\tau\) is antipodal reversal, and fix a root vertex \(x\) and color \(\epsilon\). Independently for each antipodal pair of cube edges \(\{e,\tau e\}\), flip both assigned colors with probability \(\rho\), where \(0<\rho\le1/2\). Put \(r=\lceil\rho^{-1}\log(n/\delta)\rceil\) for \(0<\delta<1\). If \(2\le r\le n-1\), with probability at least \(1-\delta\) there is an \(\epsilon\)-monochromatic path beginning at \(x\) that uses \(n-r\) distinct coordinate directions, and hence is a geodesic of length \(n-r\). If \(\rho n/\log n\to\infty\), such a path has length \(n-o(n)\) with probability tending to one, for each prescribed root and color.

*Proof.* Identify vertices relative to \(x\) with subsets \(S\subseteq[n]\), and regard the directed edge \(e(S,i)\) from \(x^S\) to \(x^{S\cup\{i\}}\), \(i\notin S\), as a possible increasing-resource move. Greedily select an unused coordinate \(i\) whenever \(c(e(S,i))=\epsilon\). We show that, as long as \(|S|\le n-2\), all candidate antipodal edge orbits at the current step are distinct and have never been queried at an earlier step.

Indeed, let \(T\subsetneq S\) be a previously visited coordinate set, and let \(e(T,j)\) have been queried at that step. The current edge \(e(S,i)\) cannot equal \(e(T,j)\), since these two edges have different lower endpoints. If \(e(S,i)=\tau e(T,j)\), comparison of the endpoints with their ranks in the Boolean lattice gives
\[
S=[n]\setminus(T\cup\{j\}),\qquad
S\cup\{i\}=[n]\setminus T.
\]
Thus \(i=j\) and \(S\cap T=\varnothing\). Since \(T\subseteq S\), we have \(T=\varnothing\), and then \(S=[n]\setminus\{i\}\), contradicting \(|S|\le n-2\). Distinct current candidate coordinates also represent distinct antipodal edge orbits. This proves freshness until the final coordinate.

Consequently, conditional on all previously queried colors, when \(k=n-|S|\ge2\) unused coordinates remain, the candidate colors are independent, each with probability at least \(\rho\) of equaling \(\epsilon\). The conditional chance that all \(k\) extensions fail is at most \(e^{-\rho k}\). Until length \(n-r\) has been reached, at least \(r\ge2\) coordinates remain. At most \(n\) stages are tested, so the total failure probability is at most \(ne^{-\rho r}\le\delta\). Each selected coordinate is used once, so the resulting path is a geodesic. \(\square\)

**Common probabilistic mechanism.** Theorem 1 and Theorem 5 both exploit a graded extension system in which each extension consumes a new resource and its local candidates belong to noise variables unexposed at previous stages. For boundary tournaments the new resource is the next terminal vertex, giving a previously unused middle vertex for every new triple comparison. For cube geodesics the new resource is the next coordinate, and antipodal edge-orbit collisions are excluded until the final step by the Boolean-lattice complement relation. This common mechanism gives near-full-length single-color paths under independent perturbations, while the deterministic problem demands a zero-defect selection under arbitrary signatures; the cube theorem makes no claim about extending the last \(r\) coordinates in the prescribed color.


### Three-matroid Hamiltonian galleries and bounded-cost block reversal

Let \(n\ge4\) and let \(b(a,v,c)\in\{0,1\}\) be a reversal-odd boundary 3-tournament:
\[
b(c,v,a)=1-b(a,v,c)
\]
for pairwise distinct letters. For an injective word \(P=(v_1,\ldots,v_m)\), write its triple-color sequence \(c_P(i)=b(v_i,v_{i+1},v_{i+2})\), and let \(\mathrm{sw}(P)=\sum_{i=1}^{m-3}\mathbf1_{\{c_P(i)\ne c_P(i+1)\}}\).

**Theorem 1 (Hamiltonian words as three-matroid common independent sets).** Let \(A=\{(u,v):u,v\in[n],u\ne v\}\) be the directed arcs of the complete graph. On this common ground set define the graphic matroid \(M_{\rm gr}\) of \(K_n\), treating both directions of an undirected edge as parallel elements; the indegree partition matroid \(M_{\rm in}\), allowing at most one arc entering each vertex; and the outdegree partition matroid \(M_{\rm out}\), allowing at most one arc leaving each vertex. The common independent sets of cardinality \(n-1\) are precisely the directed Hamiltonian paths:
\[
\boxed{\{B\subseteq A:|B|=n-1,\ B\in\mathcal I(M_{\rm gr})\cap\mathcal I(M_{\rm in})\cap\mathcal I(M_{\rm out})\}.}
\tag{1}
\]

*Proof.* A graphic-independent set of \(n-1\) arcs has an underlying spanning tree in \(K_n\). The two partition matroid bounds give each vertex total degree at most two. Every degree-two spanning tree is an undirected Hamiltonian path. Its internal vertices each have one incoming and one outgoing arc, ensuring a consistently directed Hamiltonian path. Conversely such a path satisfies all three conditions. \(\square\)

**Proposition 2 (a single matroid does not encode the paths).** For every \(n\ge4\), the undirected edge sets of Hamiltonian paths of \(K_n\) do not form the bases of any matroid on \(E(K_n)\).

*Proof.* Let \(P=(0,1,2,3,\ldots,n-1)\) and \(Q=(0,2,1,3,\ldots,n-1)\). The differences between their edge sets are
\[
E(P)\setminus E(Q)=\{\{0,1\},\{2,3\}\},\quad
E(Q)\setminus E(P)=\{\{0,2\},\{1,3\}\}.
\]
Remove \(e=\{0,1\}\) from \(P\). Adding \(\{0,2\}\) gives degree three at vertex 2 and is not a path. Adding \(\{1,3\}\) creates triangle \(1,2,3,1\) and leaves vertex 0 isolated. No element of \(E(Q)\setminus E(P)\) provides the required basis exchange, so the axiom fails. \(\square\)

**Theorem 3 (uniformly bounded cost for nonlocal block reversal).** For any injective word \(P=(v_1,\ldots,v_m)\), \(m\ge4\), and any \(1\le a<b\le m\), let \(P^{[a,b]}\) be obtained by reversing the contiguous block \(v_a,\ldots,v_b\). Then
\[
\boxed{\bigl|\mathrm{sw}(P^{[a,b]})-\mathrm{sw}(P)\bigr|\le6.}
\tag{2}
\]
The bound is independent of \(m\) and the number of reversed vertices. For Hamiltonian words the operation preserves all three matroid independence conditions from Theorem 1, and modifies at most two edges of the underlying undirected Hamiltonian spanning tree.

*Proof.* Every triple window fully inside the reversed block becomes, after reindexing, the reversal of its corresponding former triple. Reversal-oddness complements every such color while reversing their order. Comparing consecutive triple colors strictly within this block therefore yields the same number of changes before and after reversal. Triple windows fully outside the block are unchanged. Only windows crossing its boundaries can change nontrivially: their possible start indices are \(a-2,a-1\) on the left and \(b-1,b\) on the right. Each pair of boundary-crossing windows belongs to at most three switch comparisons; every other comparison is either unchanged or belongs to the reversed-and-complemented interior, where the total is preserved. Thus no more than six switch indicators can change, proving (2).

Reversing a block preserves the vertex set and injectivity of the word, so the resulting Hamiltonian path is again a common independent set of cardinality \(n-1\). At the undirected graph level, every interior edge of the reversed block remains present. Only the two external boundary edges, if present, are replaced:
\[
\{v_{a-1},v_a\}\mapsto\{v_{a-1},v_b\},\qquad
\{v_b,v_{b+1}\}\mapsto\{v_a,v_{b+1}\}.
\]
Thus at most two graphic-basis edges change. \(\square\)

**Proposition 4 (the constant six is sharp).** For \(n=14\), consider
\[
P=(0,1,2,3,4,5,6,7,8,9,10,11,12,13)
\]
and the block reversal of positions 8 through 11 (one-based),
\[
P'=(0,1,2,3,4,5,6,10,9,8,7,11,12,13).
\]
The following triple-color words are simultaneously realizable by a reversal-odd tournament:
\[
c_P=011000000000,\qquad c_{P'}=011001011010.
\tag{3}
\]
Every triple reversal-orbit occurring in both words receives consistent complementary labels upon orientation reversal; assign colors on all other triple orbits freely. The two words have switch counts two and eight. Hence equality is achieved in (2). \(\square\)

**Corollary 5 (connected nonlocal gallery with bounded edge and cost changes).** The graph of directed Hamiltonian paths joined by contiguous-block reversals is connected. Any two such words can be joined by at most \(n-1\) reversals, each changing at most two underlying graphic-basis edges and at most six color switches.

*Proof.* Reversing an adjacent pair swaps two consecutive symbols, and adjacent transpositions generate all permutations. For the quantitative bound, repeatedly locate the desired next symbol of a target word and reverse the block from its current position to the current target position, fixing one additional prefix symbol at each step. At most \(n-1\) reversals suffice. Apply Theorem 3 to each operation. \(\square\)

**Implications and limitations.** This is an admissibility-preserving *nonlocal* exchange on Hamiltonian paths, with a dimension-independent cost Lipschitz constant. It differs from formal binary hexagon reductions or signed-incidence lattice generation because every intermediate object is a connected, resource-simple directed path. The theorem does not guarantee a descending reversal from each nonoptimal Hamiltonian path; it gives no universal upper bound on the minimum switch count. Arbitrary antipodally odd cube-edge colorings do not acquire the same block-reversal property on proper coordinate subcubes: complementarity is imposed only by the full antipodal involution. A future shared theorem needs the analogous globally legal move in each model, not an unqualified transfer of this tournament-specific operation.

A prospective approach is to combine the nonlocal reversal graph with cut-connectivity constraints and a low-cost witness principle. The difficult remaining step is to prove that this connected family must contain a path with a long constant-color run, rather than merely controlling how much one move can change the cost.
