# Minimum-component repairs and Kleitman anticode corollaries

- Stable ID: note_nori_isolated_geodesic_tree_all_dimensions_20261016
- Author: Independent NORI1 critical-star researcher
- Primary home: subsection:curvature_realization_gauge_phases_and_rooted_square_defect_transport
- Labels: cube, geodesic, star, tree, obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 12
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_3
- Updated session: session_nori_r11254_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note


**Theorem (sharp isolated geodesic trees).** Fix \(n\ge4\). For every antipodally odd coloring of \(Q_n\), any red connected component containing a red full antipodal geodesic has at least \(2n-1\) vertices. This lower bound is sharp for every \(n\ge4\): a legal coloring can have a red component \(T\) that is a tree on \(2n-1\) vertices, contains one antipodal vertex pair, and has precisely one red full antipodal geodesic, up to reversal. Consequently, an alternative red full geodesic sharing any edge of the distinguished red geodesic need not exist, even though NORI1 succeeds in the full coloring.

**Classification for a fixed red geodesic.** Write vertices as subsets of \(D=[n]\), and set \(v_j=[j]\), \(j=0,\ldots,n\). Let \(P=v_0v_1\cdots v_n\). For each intermediate direction \(k=2,\ldots,n-1\), choose either \(s_k=\{k\}\), attaching a pendant edge at \(v_0\), or \(s_k=D\setminus\{k\}\), attaching a pendant edge at \(v_n\). Set \(S=\{v_0,\ldots,v_n\}\cup\{s_k:2\le k\le n-1\}\), and let \(T\) be \(P\) together with those \(n-2\) pendant edges.

There exists a legal coloring whose red component through \(v_0\) is precisely \(T\) if and only if
\[
s_2=\{2\},\qquad s_{n-1}=D\setminus\{n-1\}.
\tag{1}
\]
The two conditions are also necessary for the vertex set of *any* red component of order \(2n-1\) containing \(P\), without an a priori tree assumption. Accordingly, the number of possible minimum-order red-component vertex sets for this prescribed \(P\) is \(2^{n-4}\).

**Proof of lower bound.** For each intermediate direction \(k=2,\ldots,n-1\), the direction-\(k\) edges incident to \(v_0\) and \(v_n=\bar v_0\) are antipodal, so one is red. Its other endpoint is respectively \(\{k\}\) or \(D\setminus\{k\}\). These \(n-2\) vertices are distinct, outside \(P\), and connected to \(P\) by red edges. The component therefore contains at least \(n+1+n-2=2n-1\) vertices. Equality forces its vertex set to have the displayed form \(S\).

**Proof of necessity in (1).** If \(s_2=D\setminus\{2\}\), then \(v_2=\{1,2\}\) and \(s_2\) lie in \(S\) at Hamming distance \(n-1\); their antipodes lie outside \(S\). Both edges \(v_2\bar s_2\) and \(s_2\bar v_2\) therefore cross the component boundary. They are antipodal edges and would both be blue, a contradiction. Similarly, if \(s_{n-1}=\{n-1\}\), the vertices \(v_{n-2}\) and \(s_{n-1}\) have distance \(n-1\) and supply another forbidden antipodal pair of boundary edges. Thus (1) is necessary for every minimum-order component containing \(P\).

**Proof of sufficiency.** Fix any choices satisfying (1). All pairs of distinct non-endpoint vertices of \(S\) have distance at most \(n-2\). Indeed, proper nonempty prefixes \(v_j\) differ in at most \(n-2\) positions; singleton leaves differ in two positions, as do two complement leaves; a singleton leaf \(\{k\}\) and a complement leaf \(D\setminus\{\ell\}\), with \(k\ne\ell\), differ in \(n-2\) positions. For a singleton \(\{k\}\) and a proper prefix \(v_j\), their distance is \(j-1\) if \(k\le j\), and \(j+1\le k\le n-2\) if \(k>j\). For a complement leaf \(D\setminus\{k\}\) and a proper prefix \(v_j\), the distance is \(n-j+1\le n-2\) if \(k\le j\) (since \(k\ge3\)), and \(n-j-1\le n-2\) if \(k>j\).

Therefore \(S\cap\bar S=\{v_0,v_n\}\). Moreover no edge joins a non-endpoint of \(S\) to a non-endpoint of \(\bar S\), since that would correspond to two non-endpoints of \(S\) at Hamming distance \(n-1\). Every neighbor of \(v_0\) or \(v_n\) lies in \(S\cup\bar S\), and the edges from these two endpoints to \(S\cup\bar S\) are precisely the edges of \(T\cup\bar T\). Hence every cube edge having one endpoint in \(S\) and the other in \(\bar S\) belongs to \(T\cup\bar T\).

Prescribe color red on every edge of \(T\) and blue on every other edge incident with \(S\). These prescriptions are compatible with antipodal oddness. Two antipodal edges cannot both belong to \(T\), because their endpoints would lie in \(S\cap\bar S=\{v_0,v_n\}\), and those vertices are nonadjacent. If two antipodal edges were prescribed blue, each would touch \(S\); one of that pair would then join \(S\) to \(\bar S\), hence belong to \(T\cup\bar T\), contradicting the red-tree prescription and the opposite color forced on \(\bar T\). All remaining antipodal edge orbits can be colored arbitrarily with opposite colors on their two members.

The resulting red component is \(T\), because every tree edge is red and every other edge incident with \(S\) is blue. It is a tree on \(n+1+n-2=2n-1\) vertices. Since its only antipodal pair is \(\{v_0,v_n\}\), and a tree has a unique path between two vertices, its only red full antipodal geodesic (up to reversal) is \(P\). A red full geodesic sharing an edge with \(P\) must remain in the same component, so it equals \(P\).

**Reproducibility audit.** Enumerate the \(2^{n-2}\) possible endpoint-side choices. For each chosen \(S,T\), assign red to \(E(T)\) and blue to all other edges incident with \(S\); normalize each edge into its antipodal edge orbit and reject inconsistent prescriptions; complete other orbits in arbitrary opposite colors; finally BFS the red component from \(v_0\). For \(n=4,5,6,7,8,9\) the numbers of compatible minimum trees are \(1,2,4,8,16,32\), agreeing with \(2^{n-4}\). This finite audit is separate from the dimension-uniform proof.

**Implication and limitation.** The known endpoint-star lower bound and its \(Q_4\) attainment are thereby upgraded to all dimensions, with a classification of minimizing component vertex sets. Critical-star investigations cannot demand a monochromatic replacement inside the connected component of a selected witness: some such components contain only that full geodesic. Other monochromatic components may still contain avoiding paths; this is neither a critical-star counterexample nor a refutation of NORI1.


**Second theorem (two complementary halo geodesics; proved for every n>=4).** For every choice of minimum-tree endpoint sides admitted above, impose red on the tree T and blue on every other edge incident with S. Every antipodally odd completion then contains two red full antipodal geodesics A and B, both vertex-disjoint from S, whose visited antipodal vertex-pair classes along the original backbone P are disjoint. Hence, for every antipodal pair U meeting P, at least one of A and B avoids U. In particular the original red P cannot be part of a coloring in which a prescribed pair U meets every monochromatic full geodesic.

**Construction and proof.** Reindex directions by 0,...,n-1. Write D={0,...,n-1}, v_j={0,...,j-1}, beta_j=D\v_j, L={n-2}, H=D\{1}. The forced endpoint pendant choices mean L,H lie in bar S. Also beta_j lies in bar S for all j. Antipodal reversal implies *every* edge incident with bar S apart from an edge of bar T is red. Define A with root {0,n-2} and B with root {1,n-2}; concatenate the following ordered direction sequences (a pair-range is empty when its start is smaller than its end):

If n is odd:
A: (0,n-1), followed by pairs (k,k+1) for k=n-4,n-6,...,1, followed by (n-2).
B: (1,n-3,n-1), followed by pairs (k,k+1) for k=n-5,n-7,...,2, followed by (0,n-2).

If n is even:
A: (0,n-3,n-1), followed by pairs (k,k+1) for k=n-5,n-7,...,1, followed by (n-2).
B: (1,n-1), followed by pairs (k,k+1) for k=n-4,n-6,...,2, followed by (0,n-2).

Each sequence uses every direction once. After its first move, A reaches L; it next reaches beta_(n-2) when n is odd, or beta_(n-3) via two moves when n is even. The subsequent direction pairs trace two-edge jumps beta_j -> beta_(j-2), reaching beta_1. The last direction n-2 reaches the antipode of A's root.

After its first move B also reaches L; it next reaches beta_(n-2) when n is even, or beta_(n-3) via two moves when n is odd. Its following direction pairs trace jumps beta_j -> beta_(j-2), reaching beta_2. Direction 0 then reaches H, and direction n-2 reaches the antipode of B's root.

Every traversed edge touches L, H, or one of the beta_j, and hence touches bar S. None is in bar T: at a beta_j the path makes a two-level jump rather than moving to adjacent backbone vertices beta_(j-1) or beta_(j+1); its steps incident with L and H differ from the blue pendant edges of bar T. Thus every traversed edge is forced red without specifying colors on any other antipodal edge orbit.

Both paths avoid S: the vertices between the first and final moves (except for the special H on B) omit 0, contain n-2, and have at least two elements except L; they are neither prefixes v_j nor chosen endpoint leaves. Initial roots {0,n-2},{1,n-2} and their antipodes also avoid S; H is in bar S and outside S. Therefore A and B belong to other red connected components.

The antipodal backbone-pair classes U_j={v_j,beta_j} visited by A are the odd j in {1,...,n-1}; those visited by B are the even j in that range. Both avoid U_0={empty,D}. Thus for each U_j at least one of A,B avoids U_j. Any U meeting P is one of these U_j, finishing the proof.

**Finite independent audit.** The integer edge-orbit verifier enumerated all 2^(n-4) admissible trees for every 4<=n<=13, checked antipodal compatibility of the imposed colors, both full direction permutations, prescribed redness of every edge of A and B, disjointness from S, and complementary parity of their visited U_j. Audit counts for n=4,...,13: 1,2,4,8,16,32,64,128,256,512. The symbolic argument above is dimension-uniform.

**Scope.** This applies to the constructed tree-with-blue-chords coloring family. An arbitrary minimum-order red component may contain additional red chords within S; their antipodal blue mates may block a halo path. The unrestricted critical-star obstruction remains open.

**Third theorem (complete shape classification of minimum-order red components, proved for every n>=4).** Let C be a red connected component of order 2n-1 containing the red full geodesic P=(v_0,...,v_n) with 0-based direction order 0,...,n-1, vertex v_j={0,...,j-1}, D={0,...,n-1}. Its vertex set S is necessarily a permitted endpoint-choice set described above. The cube subgraph induced on S consists of the backbone-and-pendant tree T and at most two further edges
\[
 e_L=\{\{1\},\{0,1\}\},\qquad
 e_R=\{\{0,\ldots,n-3\},D\setminus\{n-2\}\}.
\]
Every red edge of C is in T or one of e_L,e_R. Both chord colors can be selected independently, and every choice extends to a legal antipodally odd coloring having C as its red component. Writing a,b for the indicators of red chords e_L,e_R, the number of red full antipodal geodesics in C, up to reversal, is
\[
 \boxed{(1+a)(1+b)\in\{1,2,4\}.}
\]
All these geodesics arise by independently switching the first two and the last two direction steps of P when the corresponding chord is red.

**Proof.** The vertex-set classification forces S to consist of the prefixes v_j and one endpoint leaf for each intermediate direction. Different leaves are never adjacent: leaves at the same endpoint have Hamming distance 2; leaves at opposite endpoints have distance n-2>=2. The prefix-induced cube graph is the backbone P. For a singleton leaf {k}, the only adjacent prefix besides v_0 occurs for k=1, at v_2={0,1}; for a complementary leaf D\{k}, the only adjacent prefix besides v_n occurs for k=n-2, at v_(n-2)={0,...,n-3}. These produce e_L,e_R and exhaust the additional induced edges. Their antipodal mates have both endpoints outside S. Consequently, the existing red-T/blue-boundary construction allows either color on each chord independently, and the rest of the edge orbits can be completed legally. C has one antipodal vertex pair, its two backbone endpoints. The chord e_L adds a four-cycle using the first two directions, and e_R adds a four-cycle using the last two. The tree connecting those end squares has a unique route; a full red geodesic chooses either direction order in an end square when its closing chord is red. There are (1+a)(1+b) such choices.

**Finite refutation of a stronger halo claim.** The earlier two forced-red halo paths require both extra chords blue. A red chord forces its antipodal halo edge blue. In n=5, both chords red produce a partial coloring (all edges incident S prescribed, all other orbits free) in which no monochromatic full geodesic avoiding the backbone endpoint antipodal pair uses only prescribed-color edges. Exhaustive search over full direction permutations and starting roots establishes this finite statement. It refutes a universal *forced-boundary-only* avoidance theorem for arbitrary minimum-order red components. It does not exclude an avoiding geodesic that uses unconstrained edges after completion, and has no bearing on the truth of unrestricted NORI1.

**Audit.** Every endpoint-side choice and four chord states for n=4,...,10 were checked with antipodal edge-orbit assignments and red-component BFS, verifying the component shape and full-path counts. The numbers of checked configurations are 4,8,16,32,64,128,256 by dimension. The algebraic proof is dimension-uniform.

**Research consequence.** The only internal freedom in a minimum-size red component is the color of its two end-square chords. These two bits already obstruct the unconditional forced-boundary halo construction. The next necessary mechanism must account for outside edge orbits instead of assuming the two companion halo paths survive all chord states.

**Fourth theorem (odd-dimensional antipodal-carrier parity obstruction, proved for all odd n>=5).** Fix any permitted minimum-order component vertex set S described above. Prescribe all edges in the cube graph induced by S **red** (the tree T and both end-square chords), and prescribe all edges leaving S **blue**. These prescriptions extend to antipodally odd full cube colorings. Write U_0={v_0,v_n} for the backbone endpoint antipodal pair. Consider the *partially colored* graph containing only edge colors determined by these prescriptions and antipodal reversal; edges outside this determined set remain absent. Then the partially colored graph contains **no** monochromatic full antipodal geodesic avoiding U_0.

In particular, for any fully colored legal completion, a monochromatic full antipodal geodesic avoiding U_0 must traverse an edge that was not determined by the original component and its antipodal color image. This is an unconditional obstruction to proving arbitrary critical-star avoidance by a proof that uses only the edges forced by a minimizing component.

**Proof.** Let \(\bar S=\{\bar x:x\in S\}\), and set \(W=V(Q_n)\setminus(S\cup\bar S)\). The vertex-set classification proves \(S\cap\bar S=U_0\), and, after deleting U_0, there are no cube edges between S and \(\bar S\). Every edge with both endpoints in S is red by hypothesis, hence every edge with both endpoints in \(\bar S\) is blue. Every edge from S to W is blue, hence every edge from \(\bar S\) to W is red. No edge with both endpoints in W has yet been prescribed.

Delete the two vertices U_0. The *determined-red* graph is therefore the disjoint union of a graph induced inside \(S\setminus U_0\) and a bipartite graph with edges from \(\bar S\setminus U_0\) to W (possibly several connected components). The *determined-blue* graph is the disjoint union of a graph induced inside \(\bar S\setminus U_0\) and a bipartite graph with edges from \(S\setminus U_0\) to W.

No antipodal pair lies wholly inside S or wholly inside \(\bar S\), apart from the deleted pair U_0. Thus an antipodal path avoiding U_0 cannot lie in either of the two induced internal graphs. For a path lying in either bipartite graph, an odd number n of edges forces its endpoints to lie on opposite sides of the bipartition. One endpoint would belong to S or to \(\bar S\), and its antipode would belong to the *other* of S and \(\bar S\), outside the bipartite component in question. Hence a length-n antipodal path is impossible in these determined-color bipartite graphs as well. This excludes monochromatic full antipodal geodesics avoiding U_0 in the determined graph.

**Independent numerical audit.** Every permitted endpoint-side configuration in dimensions n=5,7,9,11 was inspected using integer bit masks. For both chord colors red, after deleting U_0 all prescribed red edges lie either within S or across the cut \((\bar S,W)\), all prescribed blue edges lie either within \(\bar S\) or across \((S,W)\), and no W-W edge is prescribed. Counts checked in these dimensions: 2,8,32,128. The proof covers every odd dimension n>=5.

**Strategic disposition.** This dimension-uniform, adversarial family falsifies forced-boundary-only critical-star repair. Even the full induced red component and its antipodal forced colors contain insufficient information to produce an avoiding full monochromatic geodesic. Any further mechanism must exploit edges outside the component and its antipode, or pivot to a structurally different global invariant.

**Theorem (the antipodal endpoint pair of a minimum red geodesic component is avoidable).** Let n>=4, let c be an antipodally odd coloring of Q_n, and suppose a red full antipodal geodesic P has a red component C of minimum possible order 2n-1. Then c contains a red full geodesic avoiding the antipodal endpoint pair of P. The conclusion holds for all endpoint-leaf choices, both internal chord colors, and every assignment of the remaining antipodal edge orbits.

**Proof.** Label directions D={0,...,n-1}, let v_j={0,...,j-1}, beta_j=D\v_j, and translate P to the prefix path v_0,...,v_n. By the minimum component theorem, its vertex set S is the backbone together with one pendant leaf in each intermediate direction k=1,...,n-2, with {1} and D\{n-2} the compulsory outer leaves. The red edges inside S are the backbone-and-pendant tree, plus either or both optional square-closing chords {1}--{0,1} and v_(n-2)--(D\{n-2}). Every edge from S to W=Q_n\(S union bar S) is blue, and by antipodal oddness every edge from bar S to W is red. An edge inside bar S is blue only when its antipodal mate belongs to the red tree or a red chord.

For even n, set r={0,n-2}. Starting from r, traverse
\[
 (0,n-3,n-1)\ \Vert\ \mathop{\Vert}_{k=n-5,n-7,\ldots,1}(k,k+1)\ \Vert\ (n-2).
\]
Every direction appears once; the path ends at bar r and avoids the backbone endpoint pair. It begins in W, enters L={n-2} in bar S, and subsequently visits beta_(n-3),beta_(n-5),...,beta_1 in bar S, interspersed with W vertices. Every edge touches bar S and none is in the blue complementary backbone or complementary pendant tree: the moves at beta_j are two-level jumps and at L avoid its blue pendant edge. The blue antipodes of the optional chords are H--beta_2 and L--beta_(n-2), with H=D\{1}; the displayed path uses neither, since its beta indices are odd and n-2 is even. Thus all of its edges are red regardless of chord colors.

For odd n>=5, let a={0} union {2,3,...,n-3}, and b=a union {n-2}. These two vertices and their antipodes belong to W. Let rho be the direction sequence
\[
 (n-1,2,0,4,3,6,5,\ldots,n-3,n-4,1),
\]
where the intervening pairs are (4,3),(6,5),...,(n-3,n-4). It lists each direction except n-2 once. The path R from b following rho terminates at bar a. It alternates vertices of W with anchors in bar S: first H=D\{1}, then beta_3,beta_5,...,beta_(n-2), finally returning to W at bar a. Every edge joins W to bar S, and avoids the antipodes of the red tree and both possible chords. At H its incident directions are n-1,2, avoiding the complementary pendant direction 1 and left-chord direction 0; at beta_j its incident directions avoid the adjacent complementary backbone directions j-1,j; and the final beta_(n-2) departs via direction 1, avoiding the right-chord direction n-1. Hence every edge of R is forced red.

The remaining direction-(n-2) edges e=a--b and bar e=bar a--bar b form an antipodal pair of edges wholly inside W, so they have opposite colors. If e is red, prepend it to R to obtain a red full geodesic from a to bar a. Otherwise bar e is red, and appending it to R gives a red full geodesic from b to bar b. Both avoid the original endpoint pair. This proves the theorem.

**One-orbit completion lemma (unrestricted fixed-coloring mechanism).** If a color-q dimension-simple path R has length n-1 from b to bar a, where b=a xor e_i, and R uses all directions except i, then one of a--b+R and R+bar a--bar b is a color-q full antipodal geodesic. This is because the two possible closing edges are antipodal, so one has color q. If all vertices of both candidates avoid a prescribed antipodal pair U, the resulting color-q geodesic avoids U. This lemma requires no minimal-component assumptions.

**Finite verification.** The standalone integer-orbit verifier nori_minimum_component_endpoint_avoidance.py tested all 2^(n-4) admissible endpoint choices and all four chord assignments for each 4<=n<=15: 4,8,16,...,8192 cases. It checks legality of imposed colors, redness of the even path, odd shared path and complementarity of the two closing edges, endpoint avoidance, and use of all directions once. The proof is dimension-uniform.

**Consequences.** Any critical-star transversal associated with a minimum-order monochromatic geodesic component must meet that geodesic internally. The odd-dimensional proof resolves the earlier forced-boundary-only obstruction by using one formerly unrestricted antipodal edge orbit; it constructs a red avoiding witness inside the original coloring for either color of that orbit. The result does not assert avoidance at interior pairs or for larger components.

**Theorem (odd-dimensional minimum red components admit avoidance of every backbone antipodal pair).** Let n>=5 be odd, and suppose a red full geodesic P belongs to a red component of minimum possible order 2n-1 in an arbitrary antipodally odd coloring of Q_n. For each antipodal vertex pair U meeting P, there is a red full geodesic avoiding U.

**Proof.** Translate and permute directions to write the original red path as v_j={0,...,j-1}, j=0,...,n; let beta_j=[n]\v_j. Denote its minimum-component vertex set by S. The prior classification gives the red backbone and endpoint pendants, compulsory leaves {1} and [n]\{n-2}, arbitrary colors of the two end-square chords, and blue boundary edges. Hence each edge between bar S and W=V(Q_n)\(S union bar S) is red. Blue edges of the graph induced on bar S are the antipodes of the red backbone/pendant edges and possibly the two end-square chords.

First zipper: let a={0} union {2,...,n-3}, b=a union {n-2}. The shared (n-1)-step path from b to bar a, with direction list
\[
 \rho_1=(n-1,2,0,4,3,6,5,\ldots,n-3,n-4,1),
\]
uses every direction except n-2 once. It alternates W vertices with bar-S anchors H=[n]\{1},beta_3,beta_5,...,beta_(n-2). Every edge is red because its ends lie across the (bar S,W) cut and none coincides with a complementary red-tree or end-chord edge; the moves at H avoid directions 1,0 and the moves at beta_j avoid the complementary backbone directions j-1,j, while the final move avoids the right-chord direction n-1. The two possible direction-(n-2) closing edges a--b and bar a--bar b are antipodal. One is red, giving a red full geodesic P_1 by prepending or appending the red closing edge to rho_1. The endpoints and interior of either completion avoid U_0,U_1 and every even-indexed backbone antipodal pair U_j={v_j,beta_j}.

Second zipper: let a'={0,n-2}, b'={0,1,n-2}. From a' follow
\[
 \rho_2=(0,n-3,n-1)\ \Vert\ \mathop{\Vert}_{k=n-5,n-7,\ldots,2}(k,k+1)\ \Vert\ (n-2).
\]
The path has length n-1, terminates at bar b', and uses every direction except 1 once. It alternates W vertices with bar-S anchors L={n-2},beta_(n-3),beta_(n-5),...,beta_2. Every traversed edge is red: at L the used directions avoid its complementary pendant/chord edges in directions n-2,n-1; at beta_j the used directions differ from the complementary-backbone directions j-1,j; and at beta_2 the path leaves in direction n-2, avoiding the left-chord direction 0. This is independent of the endpoint-side choices and both chord colors. The closing direction-1 edges a'--b' and bar a'--bar b' are antipodal, with one red. Prepending or appending the red edge gives a red full geodesic P_2. Each possible completion avoids U_0,U_1 and every odd-indexed backbone pair U_j.

The visited backbone-pair classes of P_1 are contained in {U_3,U_5,...,U_(n-2)}, while those of P_2 lie in {U_2,U_4,...,U_(n-3)}. These sets are disjoint. Therefore each pair U meeting the original P is avoided by P_1 or P_2. This is a fixed-coloring result and requires no assumption on the colors of edges outside the minimum component. QED.

**Independent verification.** Script nori_two_zippers_odd.py exhausts all permitted endpoint-side configurations and four chord states for each odd n=5,7,9,11,13,15 (8,32,128,512,2048,8192 models), checking both forced-red (n-1)-edge bridges, two antipodal closing-edge orbits, distinct direction use, and disjoint visited backbone-pair sets. The proof applies to every odd n>=5.

**Implication.** In odd dimensions any hypothetical critical-star witness must have a monochromatic full geodesic lying in a component with strictly more than 2n-1 vertices. The two independent single-orbit repairs resolve the previous apparent obstruction at the endpoint and at every interior antipodal pair of a minimizing path. For even dimensions, only the endpoint-pair case has been proved; interior pairs remain unresolved.

**Dimension-uniform parity law for red geodesics outside a minimum component.** Let c be an antipodally odd coloring of Q_n (n>=4), and let a red connected component C of size 2n-1 contain a full red antipodal geodesic. Its vertex set S contains one antipodal pair U_0, and the induced cube graph on S consists of a forced red backbone-and-pendant tree plus two optional end-square chords. Put B=bar S\U_0 and W=V(Q_n)\(S union bar S). Every red full antipodal geodesic R avoiding U_0 lies in B union W, has both endpoints in W, and obeys
\[
 N_{WW}(R)+N_{BB}(R)\equiv n\pmod2.
\]
Here N_XY counts the edges of R crossing the designated sets, and N_BB can count only the antipodal images of the two optional end-square chords whose originals in S are blue. If both chords are red, N_BB=0 and N_WW(R) has the parity of n.

**Proof.** Every edge leaving S is blue, so a red path outside C cannot enter S. A red antipodal path avoiding U_0 has both endpoints outside S, and cannot have an endpoint in B because its antipode would then belong to S. Both endpoints therefore belong to W. The antipodes of the red tree edges are blue; the only red edges with both endpoints in B are antipodes of blue optional chords. Every B--W edge is red, by applying antipodal oddness to the blue boundary edges of S. Thus R decomposes into B--W crossings, W--W edges, and the stated internal B--B chord-antipode edges. It starts and ends in W, so the number of B--W crossings is even. Reducing the total edge count n modulo two gives the formula. The proof works for every n>=4 and all unspecified edge colors.

**Sharp finite Q8 repair threshold (verified).** In Q8 write v_j={0,...,j-1} and take S to consist of the backbone vertices v_0,...,v_8 together with leaves {1},{2},{3},{4},{5},D\{6}. Declare all edges induced inside S red, including both end-square chords, and all boundary edges blue. Put U_3={v_3,bar v_3}={7,248}. Among all legal completions of these partial prescriptions, the maximum of the minimum number of W--W edges on a red full antipodal geodesic avoiding U_3 is four.

To establish the lower bound, the standalone nori_twofree_q8_countermodel.py enumerates the 352 possible red avoiding paths with at most two W--W edge orbits, constructs a 66-variable 2-SAT assignment that falsifies all these candidate paths, and extends it to a legal full coloring. The parity law excludes paths with one or three W--W edges. Therefore that coloring requires at least four.

For the upper bound, a finite family of 35 red-geodesic candidate paths, each avoiding U_3, uses 21 formerly unspecified antipodal edge-orbit variables. All other edges of each candidate are forced red. Nine candidates require two free edges and 26 require four. Their corresponding 35 Boolean clauses have no common satisfying assignment, as certified by a direct truth-table check of all 2^21 assignments. The standard-library script verify_q8_35path.py with data q8_35path_certificate.json checks all 35 root and direction-order witnesses, antipodal edge-orbit color equations, and all 2^21 cases without invoking a SAT solver. Therefore every completion has some red avoiding geodesic with at most four W--W edges. This proves the sharp value four for the specified Q8 partial coloring.

**Consequences.** The parity law isolates the source of the odd/even difference in one-orbit geodesic completion. The Q8 certificate rules out a two-free-edge universal repair mechanism even with a minimum-size red component, while preserving a four-free-edge conclusion in that finite instance. This is a structural method obstruction and a finite sharpness theorem, neither a NORI1 counterexample nor a dimension-uniform full repair theorem.

**Theorem (even-dimensional forbidden locations for critical antipodal pairs).** Let n>=6 be even and c a legal antipodally odd coloring of Q_n. Suppose a red full antipodal geodesic P lies in a red component of minimum order 2n-1. Number the path P=(v_0,...,v_n) by direction order 0,...,n-1, with v_j={0,...,j-1}. Then c contains a red full geodesic B satisfying
\[
 \{j:B\text{ meets }\{v_j,\bar v_j\}\}=\{3,5,\ldots,n-3\}.
\]
Therefore a critical antipodal pair U meeting P must be one of the inner odd-indexed pairs U_3,U_5,...,U_(n-3). This restriction holds for all optional end-square chord colors and all choices of the other endpoint leaves.

**Proof.** By the minimum-component classification, its vertex set S consists of the prefix path and one endpoint pendant leaf for each direction k=1,...,n-2, including compulsory leaves {1} and D\{n-2} (D={0,...,n-1}). All edges from S into W=V(Q_n)\(S union bar S) are blue; antipodal reversal makes all edges from bar S into W red. Set beta_j=D\v_j, L={n-2}, H=D\{1}. Start at r={1,n-2}, and follow the permutation of all n directions
\[
 (1,n-3,n-1)\ \Vert\ \mathop{\Vert}_{k=n-5,n-7,\ldots,3}(k,k+1)\ \Vert\ (0,2,n-2).
\]
The pair concatenation is empty in n=6. Its first step enters L in bar S. The next two reach beta_(n-3). The descending pairs move successively from beta_(k+2) through W to beta_k for odd k, ending at beta_3. The last three steps pass through W, then H, and then end at the antipode of r in W. Every traversed edge lies across bar S and W: at the anchors L,H,beta_j none of the incident moves uses an edge internal to bar S. Hence all edges are red, independent of the two optional internal chord colors; no appeal to an unprescribed edge orbit is needed.

The only visited complementary-prefix vertices are beta_3,beta_5,...,beta_(n-3); the vertices L,H are complementary endpoint leaves and do not belong to a backbone antipodal class. All other vertices lie in W and no prefix vertex in S is visited. Consequently the backbone pair classes met by B are precisely U_3,U_5,...,U_(n-3). Every other backbone pair is avoided, proving the theorem.

**Verification.** Reproducible script nori_even_universal_spine.py checks legality and forced redness of this path, its n distinct direction flips, endpoint antipodality, and its visited backbone-pair classes for every admissible endpoint-side choice and all four chord assignments. Cases exhaustively checked: n=6 (16), n=8 (64), n=10 (256), n=12 (1024). The argument above is independent of dimension.

**Consequences.** Combining this theorem with the existing odd-dimensional two-zipper exclusion, a critical pair on a geodesic contained in a minimum-order red component can occur only in even dimension n>=6, and only at an inner odd backbone level. The existence of such critical pairs remains unresolved.



**Cube-specific anticode corollaries of the previously published four-sector theorem.** Article XI, Subsection "Antipodal cut-pair separation and four-sector cocycle geometry" already proves the general four-sector restrictions and the graphic/partition-matroid component-support characterization. The new deductions here concern the Hamming diameter and cardinality of the unpaired vertices, and the resulting geometry-only criterion when the paired core has at most two vertices.

**Hamming anticode and size theorem for the unpaired sector.** Let n>=2, c be an antipodally odd red/blue edge coloring of Q_n, and S the vertex set of a red connected component. Put
\[
 P=S\cap\bar S,\quad T=S\setminus\bar S,\quad \bar T=\{\bar t:t\in T\},\quad W=V(Q_n)\setminus(S\cup\bar S).
\]
Then P and W are antipodally invariant, while T and bar T are exchanged by antipodality. The four sets partition the vertices. The following properties hold:

(i) There are no cube edges joining P to W, nor T to bar T.

(ii) Every edge from P to T is red and every edge from P to bar T is blue. Every edge from T to W is blue and every edge from bar T to W is red.

(iii) The Hamming diameter of T is at most n-2. In particular, using Kleitman's isodiametric theorem for the Boolean cube, writing p=|P|, one has
\[
 |T|\le D_n:=
 \begin{cases}
 2^{n-1}-\frac12\binom{n}{n/2},&n\text{ even},\\
 2^{n-1}-\binom{n-1}{(n-1)/2},&n\text{ odd},
 \end{cases}
\]
and consequently
\[
 |W|=2^n-p-2|T|\ge
 \begin{cases}
 \binom n{n/2}-p,&n\text{ even},\\
 2\binom{n-1}{(n-1)/2}-p,&n\text{ odd}.
 \end{cases}
\]
This applies to EVERY red connected component, regardless of how many antipodal vertex pairs it contains. It is a component result and does not assert the corresponding diameter inequality for monotone rooted reachability sets (the latter has a known Q5 counterexample in the archive).

**Proof of (i)--(iii).** Every edge leaving S is blue. If p in P and w in W were adjacent, both p--w and its antipode bar p--bar w would leave S and hence be blue, violating the opposite-color rule. Similarly, if t in T and bar s in bar T were adjacent, the edges t--bar s and bar t--s would both leave S and be blue. This proves (i). The antipode of any edge joining P to T joins P to bar T and leaves S, so the former edge is red and the latter blue. Every edge joining T to W leaves S and is blue, and its antipode joins bar T to W and is red; this proves (ii). Since T is disjoint from its antipode, no two members of T are at Hamming distance n. If t,s in T had distance n-1, then t and bar s would be adjacent, contrary to (i). Thus diam(T)<=n-2. Kleitman's bound for a diameter-(n-2) subset yields the formula for D_n, and the formula for |W| follows by cardinality of the four-part partition.



**Purely geometric component realizability for zero or one antipodal pair.** Let S be any nonempty subset of V(Q_n), n>=2, and set P=S intersect bar S, T=S\bar S and W=V(Q_n)\(S union bar S). Assume |P|<=2. Then S is a red connected-component vertex set of some legal antipodally odd coloring if and only if: (a) Q_n[S] is connected; (b) no cube edges join P to W; and (c) no cube edges join T to bar T.

When P is empty, conditions (b),(c) reduce to the single numerical condition diam(S)<=n-2. When P is the antipodal pair U, the conditions reduce to connectedness, diam(S\U)<=n-2, and N(U) subset S union bar S.

**Proof.** Necessity is the four-sector cut theorem from Article XI. Conversely, since P has zero or two vertices and its two possible vertices are antipodal at distance n>=2, no cube edge with both endpoints in S has its antipodal mate also inside S. The absence of edges P--W and T--bar T is equivalent to the absence of a pair of antipodal boundary edges. We may therefore color every edge induced by S red and every edge leaving S blue without prescribing both colors to any one edge or assigning the same color to antipodal mates. Complete all remaining edge orbits with opposite colors. The red graph induced on S is the connected graph Q_n[S], and no red edge leaves S, so S is one red component. Finally, T and bar T are disjoint, and T--bar T adjacency is equivalent to the existence of two members of T at Hamming distance n-1, yielding diam(T)<=n-2. This proves the numerical reformulations.

**Verification.** Direct enumeration of all 64 legal Q3 colorings produces 40 different red-component vertex sets. Independent enumeration of all 255 nonempty subsets S of Q3 against conditions (A),(B), with each P--P antipodal orbit tested for a rainbow spanning tree, produces the same 40 sets. For the zero/one paired-core subcase, the geometry-only criterion predicts the 20 observed sets, without missing or spurious candidates. Random legal colorings in Q3 through Q8 were also checked for (i)--(iii). These computations audit the theorem; the proof is valid in every dimension n>=2.

**Relevance to critical-star geometry.** The theorem supplies restrictions on *arbitrary* monochromatic connected components, including those much larger than the 2n-1 minimal examples. Their unpaired vertices form a diameter-(n-2) anticode; their paired vertices cannot touch the doubly exterior region W; the four interfaces have forced colors. When the paired set is one antipodal pair, admissible component vertex sets have a geometric characterization with no edge-color variables. These facts constrain possible components of a critical coloring, but they do not by themselves produce a full avoiding geodesic, so unrestricted NORI1 remains open.

**Four-geodesic branching theorem (proved for even n>=8).** Let P be a red full antipodal geodesic contained in a red connected component S of minimum order 2n-1. Normalize P to the prefix path v_j={0,...,j-1}. Let s_k=0 when the red direction-k pendant leaf is {k}, and s_k=1 when it is D\{k}, 1<=k<=n-2. Beyond mandatory s_1=0,s_(n-2)=1, suppose s_2=1,s_(n-4)=1,s_(n-3)=0. Then the original coloring contains a red full geodesic avoiding U_3={v_3,bar v_3}, for arbitrary remaining pendant-side choices and arbitrary colors of both optional internal chords.

**Constructive proof.** Identify vertices with bit masks, put q=2^(n-4)+2^(n-3), and write J(a,b) for the ordered concatenation (a,a+1),(a-2,a-1),...,(b,b+1), empty when a<b. The following four rooted paths are full antipodal geodesics (root: ordered direction flips):
A0: 29: (4,3,0,n-2,2,n-3,n-1) || J(n-5,5) || (1).
A1: 13: (3,0,n-2,2,n-3,n-1) || J(n-5,5) || (1,4).
B0: 5: (0,n-4,2,n-3,n-2,n-1) || J(n-6,4) || (1,3).
B1: q+2^(n-2): (n-1) || J(n-6,4) || (1,3,2,n-3,0,n-4,n-2).

All path vertices outside the exterior region W=V(Q_n)\(S union bar S) lie in bar S, and the bar-S vertices visited are:
A0,A1: {2},{n-2},beta_(n-3),beta_(n-5),...,beta_5;
B0: {2},{n-4},beta_(n-4),beta_(n-6),...,beta_4;
B1: beta_(n-4),beta_(n-6),...,beta_4,beta_1,D\{n-3},
where beta_j=D\v_j. These membership lists follow by successively applying the displayed bit flips. The indicated singleton/complement anchors belong to bar S by the five pendant-side constraints; every other path vertex is neither a prefix, a complementary prefix, a singleton, nor a complementary singleton, and is therefore in W independently of the other leaves. In particular none meets U_3.

Every traversed edge apart from three unprescribed antipodal edge orbits joins bar S to W and is forced red, since its antipode is a blue boundary edge of S. Name the three remaining orbits xi=[5--13], eta=[13--29], and theta=[q--(q+2^(n-2))]. The two A paths both require xi itself red, and require opposite representatives of eta red. The B paths both require the antipode of xi red, and require opposite representatives of theta red. If xi is red, one A path succeeds depending on eta; if xi is blue, one B path succeeds depending on theta. One of these four U3-avoiding paths is therefore red for every legal completion. This is a fixed-coloring, two-stage binary completion involving only three unrestricted edge orbits.

**Independent audit.** The accompanying script nori_even_u3_four_branch.py verifies all edge-orbit signatures, path direction permutations, forced red edges and U3 avoidance for every permitted other leaf attachment and all four end-chord states for even n=8,10,12,14,16: 8,32,128,512,2048 cases. The proof works for all even n>=8.

**Boundary.** This excludes the inner pair U3 under explicit geometric side conditions. It does not exclude the remaining inner odd-indexed critical pairs for arbitrary red components, nor prove NORI1.
