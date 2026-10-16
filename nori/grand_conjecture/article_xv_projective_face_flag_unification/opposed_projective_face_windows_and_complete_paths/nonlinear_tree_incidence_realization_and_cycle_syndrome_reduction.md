# Nonlinear tree incidence realization and cycle-syndrome reduction

### Independent incidence realization on interaction trees

Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_d\). For each dimension \(i\), write \(f_i(x)\) for the color of the direction-\(i\) edge incident with \(x\); this is independent of \(x_i\). Its **interaction graph** \(G(f)\) joins \(i,j\) when either \(\partial_j f_i\) or \(\partial_i f_j\) is nonzero. Consequently \(f_i\) depends only on the bits of the neighboring directions \(N_G(i)\).

For every incident pair of graph vertices \(i,j\), regard \(a_{ij}\in\mathbb F_2\) as a prescribed value of bit \(j\) at the instant a full direction-simple path traverses dimension \(i\). Let \(\pi\) be the order of the traversed dimensions. The incidence equation is
\[
\boxed{a_{ij}=x_j+[\pi(j)<\pi(i)]\pmod2.}
\tag{1}
\]

**Lemma 1 (universal realization of prescribed incidences on trees).** Let \(T\) be any tree on a set of \(m\ge2\) directions. Prescribe the two incidence bits \(a_{ij},a_{ji}\) independently for every edge \(ij\) of \(T\). There exist an initial cube vertex \(x\) and a permutation \(\pi\) of the directions satisfying every equation (1). In fact, there are two antipodal choices of \(x\), with corresponding reverse orientations of \(T\). A suitable pair can be constructed in linear time from the incidence data.

*Proof.* Choose a tree root \(r\) and set \(x_r\) arbitrarily. Process the tree outward. When the parent \(p\) has known bit \(x_p\) and \(c\) is a new child, orient the edge \(p\to c\) if
\[
\varepsilon_{pc}=a_{cp}+x_p=1,
\]
and orient it \(c\to p\) otherwise. In either case define
\[
x_c=a_{pc}+1+\varepsilon_{pc}\pmod2.
\]
If \(p\) is earlier, its bit at the traversal of \(c\) is \(x_p+1=a_{cp}\); if it is later, the bit is \(x_p=a_{cp}\). The definition of \(x_c\) similarly makes the bit of \(c\) at traversal of \(p\) equal \(a_{pc}\). Thus the incidence equations hold on the new edge. Repeat for all edges. Every orientation of a tree is acyclic, so it extends to a total permutation \(\pi\). Changing \(x_r\) flips all inferred root bits and reverses every tree-edge orientation, giving the second solution. QED.

**Theorem 2 (admissible monochromatic targets on arbitrary nonlinear trees).** Suppose the interaction graph \(G(f)\) is a tree and choose a prescribed color \(t\in\{0,1\}\) **attained by every direction's local neighbor-bit function**:
\[
\boxed{t\in\bigcap_{i\in V(G)}\operatorname{im}(f_i).}
\]
Then there exists a full dimension-simple antipodal geodesic of constant color \(t\). The statement holds for arbitrary nonlinear local functions and is constructive.

*Proof.* For each \(i\), the displayed hypothesis permits an independent assignment \((a_{ij})_{j\in N(i)}\) satisfying \(f_i((a_{ij})_j)=t\). Lemma 1 realizes all chosen incidence bits simultaneously through a root and an acyclic orientation of the tree; topologically order its vertices to obtain a full antipodal geodesic. Every traversed edge has color \(t\). QED.

**Necessary qualification.** Connectedness of the *undirected* interaction graph alone does not imply that each \(f_i\) is nonconstant. An edge \(ij\) can arise solely from dependence of \(f_j\) on bit \(i\), while \(f_i\) is constant. For example on \(Q_3\) let \(f_1\equiv0\), \(f_3\equiv1\), and \(f_2(x)=x_1+x_3\). The interaction graph is the connected path \(1-2-3\), but no monochromatic full geodesic can exist, because every full geodesic uses direction 1 of color zero and direction 3 of color one. Thus the previously published unrestricted monochromatic-tree claim was false; the theorem above replaces it.

**Corollary 3 (paired roots in target-admissible interaction forests).** Suppose \(G(f)\) is a forest with \(c\) nontrivial connected tree components and \(r\) isolated vertices. Assume that in each nontrivial component \(C\), there is a bit \(t_C\) attained by **every** local color function in \(C\). Then
\[
\boxed{|P(f)|\ge 2^{c+r}.}
\]
In particular the condition holds when all local functions in each nontrivial component are nonconstant.

*Proof.* Theorem 2 produces a monochromatic color-\(t_C\) antipodal geodesic in each component; reversing it gives a second root at its antipode. An isolated direction has a constant color and allows either root bit. Select the roots independently in all components. To form a \(0^*1^*\) full geodesic, concatenate all component paths and singleton directions colored zero, followed by those colored one. For the reverse \(1^*0^*\) orientation, concatenate the same selected component paths in the opposite color-block order. Independence between interaction components preserves all edge colors and all dimensions are used once. The choices give at least \(2^{c+r}\) paired roots. QED.

**Corollary 4 (NORI1 over target-admissible forest facets).** An antipodally odd coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) whose lower-facet interaction forest satisfies the common-target condition of Corollary 3 admits at least \(2^{c+r}\) distinct directed monochromatic full antipodal geodesics, for arbitrary odd vertical bridge colors.

*Proof.* Apply Corollary 3 and the universal paired-root bridge equivalence. QED.

### Cycle-syndrome criterion for arbitrary interaction graphs

The tree realization proof extends to a graph with cycles, but now two precisely described obstructions arise.

For an arbitrary undirected graph \(G\) on the direction set and a full specification of the incident bits \(a_{ij}\) on its edges, set
\[
\lambda_{ij}=1+a_{ij}+a_{ji}\pmod2
\tag{3}
\]
for each edge \(ij\).

**Theorem 5 (cycle parity and acyclic orientation characterization).** The incidence prescription (1) is realizable by a root \(x\) and a total direction order \(\pi\) if and only if the following two conditions hold:

(i) for every cycle \(C\) of \(G\),
\[
\boxed{\sum_{ij\in E(C)}\lambda_{ij}=0\pmod2;}
\tag{4}
\]

(ii) choose either vertex potential \(x\) solving \(x_i+x_j=\lambda_{ij}\) on each connected component, and orient every graph edge \(j\to i\) when \(a_{ij}+x_j=1\); the resulting graph orientation is acyclic.

When (i) holds, the solutions for \(x\) are the two global-complement choices on each connected component. Replacing a potential by its complement reverses every edge orientation in that component, so condition (ii) is independent of which potential is chosen.

*Proof.* If (1) holds for some \(x,\pi\), summing the two incidence equations at the endpoints of an edge gives
\[
a_{ij}+a_{ji}=x_i+x_j+1.
\]
Thus the \(\lambda\)-values form a vertex coboundary, which is equivalent to (4). The induced edge orientations follow the total order \(\pi\) and hence are acyclic.

Conversely (4) makes the edge equations \(x_i+x_j=\lambda_{ij}\) solvable, uniquely up to one bit per connected component. Orient edge \(j\to i\) whenever \(a_{ij}+x_j=1\). Since
\[
(a_{ij}+x_j)+(a_{ji}+x_i)
=a_{ij}+a_{ji}+\lambda_{ij}=1,
\]
this assigns one direction to each undirected graph edge. If the orientation is acyclic, choose any of its topological total orders \(\pi\). The incidence equations (1) hold by construction. Replacing all \(x_i\) in one component by \(x_i+1\) reverses each orientation there; directed cycles exist in an orientation if and only if they exist in its reversal. QED.

**Corollary 6 (cyclomatic localization of a monochromatic obstruction).** If local neighbor-bit inputs making every direction color \(t\) can be chosen independently, then failure to realize those inputs as a monochromatic full geodesic can arise only from the cycle-parity constraints (4) and the acyclicity requirement in Theorem 5. A graph with cycle-space dimension
\[
\beta_1(G)=|E(G)|-|V(G)|+\#\text{components}
\]
has \(\beta_1(G)\) independent parity equations. On a forest there are none and the orientation condition is automatic. This gives a cycle-rank parameterization of the remaining difficulty, preserving all direction uses.

**Example 7 (a single even cycle already obstructs monochromaticity).** On \(Q_{2r}\), \(r\ge2\), index dimensions cyclically and define
\[
f_i(x)=x_{i-1}+x_{i+1}+a_i\pmod2,
\qquad \sum_i a_i=1\pmod2.
\tag{5}
\]
Its interaction graph is the even cycle \(C_{2r}\). Along any full antipodal dimension order, each graph edge contributes once to the sum of the traversed colors, while every starting bit appears twice. Therefore
\[
\sum_{\text{all }2r\text{ steps}}\text{color}
=\sum_i a_i+|E(C_{2r})|
=1\pmod2.
\]
A monochromatic word of even length has parity zero, so this coloring has **no monochromatic full antipodal geodesic from any root**. This shows that the tree monochromatic theorem does not extend unchanged to unicyclic interaction graphs. The paired-root conjecture remains a different and weaker assertion: existence of both monotone orientations from one root is not ruled out by this parity obstruction.

**Closure program.** Theorem 5 isolates the first obstruction after constructing admissible local tree prescriptions: nonzero syndrome around independent cycles and directed circuits of an induced orientation. To extend a closure proof toward general interactions, one should seek simultaneous prescribed input patterns supporting the two monotone orientations and show that a minimal incompatible cycle can be repaired by changing the seam placement or by an exchange of path orders. Unlike a bound based on small cube dimensions, the present realization and obstruction calculus applies to graphs of arbitrary order and arbitrary nonlinear local coloring functions.### Quantitative tree incidence paths

For a connected nontrivial interaction tree \(T\), let
\[
r_i(t)=|\{a\in\mathbb F_2^{N(i)}:f_i(a)=t\}|\ge1.
\]
Let \(G_t(f)\) be the number of directed rooted full antipodal geodesics of constant color \(t\).

**Theorem 8 (tree path census).** For each \(t\in\{0,1\}\),
\[
\boxed{G_t(f)\ge2\prod_i r_i(t).}
\tag{6}
\]
Indeed, if \(\mathcal A_t=\prod_i f_i^{-1}(t)\), and \(O(a)\) is the oriented tree resulting from the incidence-realization lemma with root bit fixed, while \(L(O)\) counts its topological total orders, then
\[
\boxed{G_t(f)=2\sum_{a\in\mathcal A_t}L(O(a)).}
\tag{7}
\]

*Proof.* For each local-successful incidence specification \(a\), the tree realization lemma supplies two antipodal initial vertices. Their tree orientations are reversals and have equal numbers of topological orders. Each topological order traverses every dimension once, realizing the specified neighbor-bit inputs and therefore constant edge color \(t\). Conversely each such rooted monochromatic path determines its local incidence specification, so paths from different specifications cannot coincide. Summation gives (7), and \(L(O)\ge1\) gives (6). QED.

**Corollary 9 (balanced nonlinear trees).** If each local color function gives color \(t\) on half of its neighbor assignments, then
\[
G_t(f)\ge2^{d-1},
\]
since \(\sum_i(\deg_T(i)-1)=d-2\). There is no linearity assumption.

### Affine parity colorings on one interaction cycle

Index the \(n\ge3\) directions cyclically. Define
\[
\boxed{f_i(x)=a_i+x_{i-1}+x_{i+1}\pmod2,}
\tag{8}
\]
and write \(A=\sum_i a_i\pmod2\). Fix a root \(x\) and let \(b_i=a_i+x_{i-1}+x_{i+1}\), so \(\sum_i b_i=A\). If a direction permutation orients each cycle edge from earlier to later, with \(p_i\) the parity of the number of earlier neighbors of \(i\), then its step color in direction \(i\) is \(b_i+p_i\).

**Lemma 10 (acyclic cycle indegree parity).** A vector \(p\in\mathbb F_2^n\) arises as the indegree-parity vector of an acyclic orientation of \(C_n\) if and only if
\[
\boxed{\sum_i p_i=n\pmod2,\qquad p\ne\mathbf1.}
\tag{9}
\]
When the parity equation holds there are two orientations having those parities, related by reversal of every cycle edge; they are both cyclic precisely for \(p=\mathbf1\).

*Proof.* Let \(u_i=1\) if \(i\) precedes \(i+1\) on their graph edge. Then
\(p_i=1+u_{i-1}+u_i\pmod2\).
Summing gives the parity condition. If it holds, choosing one \(u_i\) freely determines all the others around the cycle, with two complementary solutions. An orientation of a simple cycle is cyclic precisely when all its graph edges point around the cycle consistently; this makes \(p_i=1\) at every vertex. Every other orientation admits a total topological ordering. QED.

**Theorem 11 (full paired-root classification for cycle-neighbor parity colorings).**
\[
\boxed{|P(f)|=\begin{cases}2^n,&n\text{ even},\\2^n-2,&n\text{ odd}.\end{cases}}
\tag{10}
\]
More precisely:
(a) If \(n\) is even and \(A=0\), every root supports a monochromatic full geodesic.
(b) If \(n\) is even and \(A=1\), no root supports a monochromatic full geodesic, yet every root supports both color words \(0^{n-1}1\) and \(10^{n-1}\).
(c) If \(n\) is odd, every root except two antipodal roots supports a monochromatic full geodesic of color \(1+A\); those two exceptional roots admit no monotone full color word.

*Proof.* Suppose \(n\) is even. If \(A=0\), the parity vector \(p=b\) meets Lemma 10's sum condition. If \(b\ne\mathbf1\), its acyclic orientation gives all-zero traversed edge colors. If \(b=\mathbf1\), take \(p=\mathbf0\) instead, giving all-one traversed colors. Hence every root is paired.

If \(n\) is even and \(A=1\), then \(b\) has odd Hamming parity. Choose \(v\) with \(b_v=1\) and prescribe the traversed color of direction \(v\) to be one and all others zero. The required indegree parity is \(p=b+e_v\), whose total parity is zero and whose value at \(v\) is zero. The two opposite acyclic orientations from Lemma 10 make \(v\) respectively a source (indegree zero) and a sink (indegree two). Extend the first to a topological order with \(v\) first, and the second to one with \(v\) last. These give the two required words from the **same root**. No constant-color word is possible: every full path has total color parity
\(\sum_i b_i+\sum_i p_i=A+n=1\), while any constant word of even length has parity zero.

Now suppose \(n\) is odd. Let \(t=1+A\). To obtain a constant color-\(t\) path, the desired indegree parity is \(p=b+t\), with sum \(A+nt=A+t=1=n\pmod2\). Lemma 10 therefore gives a suitable acyclic orientation unless \(p=\mathbf1\), equivalently \(b_i=A\) at every direction. The exceptional roots solve
\[
x_{i-1}+x_{i+1}=A+a_i\pmod2
\quad\text{for all }i.
\]
The right side sums to zero; the linear map \(x\mapsto(x_{i-1}+x_{i+1})_i\) on an odd cycle has kernel consisting of the two constant binary strings, because kernel elements have period two and \(n\) is odd. Thus precisely two antipodal roots are exceptional.

At either exceptional root \(b_i=A\) for every \(i\). Along any full direction order the first step has no earlier graph neighbors and the last has two, so their colors both equal \(A\). A monotone binary word with equal first and last entries must be constant \(A\). But total step-color parity is \(\sum_i b_i+\sum_i p_i=A+1\), whereas the constant word \(A^n\) has parity \(A\). Thus no monotone full path exists from either exceptional root. This proves the theorem. QED.

**Closure implication.** The first cycle-parity obstruction to a monochromatic full geodesic is sometimes unavoidable: case (b) rules out such a path in every even dimension. Nevertheless the obstruction can be moved between the first and last directions by reversing a cycle orientation, yielding the paired paths NORI1 requires at every root. This identifies an induction motif beyond the tree-realization theorem but does not settle nonlinear cyclic interactions.

## Pendant direction elimination by a two-word insertion lemma

The tree realization theorem resolves interaction forests, but a stronger property is available: a responsive pendant direction can be removed from **any** interaction graph, regardless of the complexity of the remaining graph.

Let \(f\) color the edges of \(Q_{m+1}\), with a distinguished direction \(i\) and another direction \(j\ne i\). Assume
\[
f_i(x)=x_j+a\quad(a\in\mathbb F_2)
\tag{11}
\]
for every direction-\(i\) edge, and assume that for all directions \(k\notin\{i,j\}\), the color \(f_k\) is independent of bit \(x_i\). The color \(f_j\) may depend **arbitrarily** on \(x_i\) and all other permitted bits. These assumptions hold whenever \(i\) is a leaf of the undirected interaction graph and its own color function depends nontrivially on the bit of its neighbor \(j\). Let \(f^{(0)},f^{(1)}\) denote the facet colorings obtained by fixing \(x_i=0,1\).

**Theorem 12 (responsive-leaf paired-root lifting).** Under (11), every root \(x\in P(f^{(0)})\) has at least one lift among \((x,0),(x,1)\) belonging to \(P(f)\). The same conclusion holds with the facet \(x_i=1\) in place of \(x_i=0\). Consequently
\[
\boxed{|P(f)|\ge |P(f^{(0)})\cup P(f^{(1)})|
\ge\max(|P(f^{(0)})|,|P(f^{(1)})|).}
\tag{12}
\]
In particular, paired-root existence is preserved by adjoining a responsive pendant direction, even when the interaction between that leaf and its neighbor is bidirectional.

*Proof.* Fix \(x\in P(f^{(0)})\), and select complete facet geodesics \(P_\uparrow,P_\downarrow\) from \(x\) with color words \(0^*1^*\) and \(1^*0^*\). Let \(u\) be the color of direction \(j\) on \(P_\uparrow\), and \(v\) its color on \(P_\downarrow\). Put
\[
\alpha=x_j+a,\qquad\beta=1+\alpha.
\tag{13}
\]
If the new \(i\)-step is inserted **after** the \(j\)-step into either facet path, start the enlarged path with \(x_i=0\). All old step colors remain unchanged: direction \(j\) is traversed while \(x_i=0\), and the colors of all other old directions are independent of \(x_i\). The inserted \(i\)-edge then has color \(\beta\), because the \(j\)-bit has been toggled. Inserting a bit \(\beta\) after direction \(j\) preserves the nondecreasing word if \(\beta=1\) or \(u=0\); it preserves the nonincreasing word if \(\beta=0\) or \(v=1\). When \(\beta=1\), place the inserted step at the end of the nondecreasing path and immediately after \(j\) in the nonincreasing path (provided \(v=1\)). When \(\beta=0\), put it immediately after \(j\) in the nondecreasing path (provided \(u=0\)) and at the end of the nonincreasing path.

Alternatively, insert the new \(i\)-step **before** direction \(j\) and start at \(x_i=1\). Again all old colors are read from facet zero. The inserted step has color \(\alpha\), since \(j\) is still unused. Such insertion preserves the nondecreasing word when \(\alpha=0\) or \(u=1\), and preserves the nonincreasing word when \(\alpha=1\) or \(v=0\), placing the new step at the beginning or immediately before \(j\) as appropriate.

Now \(\alpha+\beta=1\). If \(\alpha=0,\beta=1\), the after-\(j\) construction works when \(v=1\), and the before-\(j\) construction works when \(v=0\). If \(\alpha=1,\beta=0\), the after-\(j\) construction works when \(u=0\), and the before-\(j\) construction works when \(u=1\). Thus one starting \(i\)-bit always supports both monotone words from the same enlarged root. All steps remain dimension-simple. This proves the first assertion; interchanging the two facets gives the same argument for \(f^{(1)}\).

For every \(x\) in the union of the two facet paired-root sets, choose one successful enlarged root in its two-element \(i\)-fiber. Different \(x\) give different roots, proving (12). QED.

**Corollary 13 (responsive-leaf pruning of irreducible obstructions).** Starting with any cube-edge coloring, repeatedly remove a leaf direction \(i\) of its undirected interaction graph whenever \(f_i\) depends nontrivially on its unique neighbor. At each removal restrict to either chosen facet of \(i\). If the final lower-dimensional coloring has a paired root, then the initial coloring also has a paired root. In particular the terminal coloring may be resolved by any previously proved criterion, including the corrected target-admissible forest theorem, the star theorem, or directed influence component seam lifting. Every hypothetical paired-root counterexample remains a counterexample under either facet restriction at every responsive pendant direction.

*Proof.* Theorem 12 lifts paired roots from either facet; contraposition and iteration prove the last assertion. QED.

**Proposition 14 (residual constant-source leaf obstruction).** Suppose instead the pendant direction \(i\) has constant edge color \(t\in\{0,1\}\), while its sole neighbor \(j\) may depend on bit \(i\), and all other old direction colors are independent of \(i\). Fix a paired root \(x\) of facet zero. If either of its two monotone witness paths traverses direction \(j\) with color \(t\), then at least one of \((x,0),(x,1)\) is paired in the full cube.

*Proof.* In the preceding insertion argument, now \(\alpha=\beta=t\). If \(t=0\) and the nondecreasing witness has its \(j\)-step colored zero, insert \(i\) after \(j\) when starting at \(i=0\); append \(i\) to the nonincreasing witness. If the nonincreasing witness has its \(j\)-step colored zero, insert \(i\) before \(j\) when starting at \(i=1\), and prepend it to the nondecreasing witness. The two cases for \(t=1\) follow by interchanging the colors and orientations. Old colors again remain unchanged because direction \(j\) is traversed in facet zero. QED.

Thus, for a constant-color pendant direction to obstruct this elementary lifting construction, **every** monotone facet witness at **every** paired root must traverse its neighboring direction with the opposite color. This gives a precise rigidity condition for the remaining source-leaf case, which is not settled by the responsive-leaf theorem.

**Connection to closure.** The directed SCC theorem removes one-way dependence blocks, while Theorem 12 eliminates bidirectionally interacting pendant directions with a nonconstant leaf function. Together they show that a minimal counterexample cannot be explained solely by a large strongly connected component with responsive trees attached to it. The unresolved leaf obstruction is asymmetric: a constant-colored leaf influencing its neighbor, rather than a leaf whose own color responds to that neighbor.

## Source-pendant directions and the one-class cross-favorability bottleneck

Let \(f\) be any binary coloring of \(Q_{m+1}=Q_m\times\{0,1\}\) whose edges in the added direction \(i\) all have the same color \(t\). No other hypothesis is imposed initially. Let \(h_0,h_1\) be the induced colorings of the two \(m\)-dimensional facets.

**Lemma 15 (constant-direction cross-seam gluing).** If either of the two intersections
\[
\boxed{A_0(h_0)\cap A_1(h_1),\qquad
A_0(h_1)\cap A_1(h_0)}
\tag{14}
\]
is nonempty, then the full coloring \(f\) has a paired root.

*Proof.* Suppose \(z\in A_0(h_0)\cap A_1(h_1)\). If \(t=0\), start at \((z,1)\). A nondecreasing full path traverses the new direction first (color zero) and then follows the chosen \(0^*1^*\) path in facet zero. A nonincreasing full path follows the chosen \(1^*0^*\) path in facet one and then traverses the new direction last (color zero). Both begin at the same root, are dimension-simple and monotone. If \(t=1\), start instead at \((z,0)\): the nondecreasing path follows its facet-zero path first and then uses the new direction last (color one), whereas the nonincreasing path uses the new direction first and then follows its facet-one path. The other intersection in (14) is handled by interchanging the two facets. QED.

**Corollary 16 (two-sided cross separation forced by a bad source leaf).** If \(f\) has no paired root and its direction-\(i\) edges have constant color, both intersections in (14) must be empty.

If, in addition, \(i\) is a leaf of the undirected interaction graph with sole neighbor \(j\), then \(h_0,h_1\) differ only in the colors of the edges of direction \(j\); every other direction has the same colors in both facets. Thus a bad constant-source pendant direction forces a pair of colorings with **one direction-class difference** whose opposite-orientation feasible-root sets are mutually disjoint.

**Theorem 17 (necessary structure of a minimum-dimension counterexample).** Suppose the paired-root conjecture fails and choose a counterexample \(f\) of least cube dimension \(d\). Then:

1. Every proper facet coloring has a paired root, by minimum-dimensional choice.
2. The undirected interaction graph is connected, by Cartesian product factorization.
3. The interaction graph cannot satisfy the common-local-target hypothesis of corrected Theorem 2, since such a coloring would have a monochromatic geodesic and hence a paired root. It is **not proved** that a connected interaction forest always has paired roots without that hypothesis.
4. Every pendant direction \(i\), if present, has a **constant** edge color. Otherwise responsive-leaf lifting would produce a paired root from a lower-dimensional facet.
5. For each constant-colored pendant direction with neighbor \(j\), the two lower-dimensional facet colorings differ only on direction \(j\); they each have paired roots but their two cross-orientation feasible-root intersections vanish.
6. Its directed influence graph has a strongly connected component of size at least four by seam lifting, or at least five using the separate computer-assisted four-cube certificate.

*Proof.* The cited factorization, conditional tree, pendant lifting, and seam theorems prove the assertions. The earlier statement that connectedness and badness force an undirected graph cycle depended on the incorrect unrestricted forest claim and has been withdrawn. QED.

**Proposed sufficient closure lemma (open).** Let \(g,h\) be two arbitrary binary colorings of \(Q_m\) that **agree on every edge outside one direction class**. Prove
\[
\boxed{A_0(g)\cap A_1(h)\ne\varnothing.}
\tag{15}
\]
This is considerably narrower than demanding cross-favorability for two completely unrelated colorings. If established for every \(m\), Lemma 15 and Theorem 12 would rule out all pendant directions in a least-dimension paired-root counterexample, leaving an undirected interaction graph of minimum degree at least two. Moreover the theorem would make *all* constant-source pendant directions safely removable, complementing the responsive-leaf elimination theorem.

**Additional implication.** If either facet coloring \(h_s\) of a constant-source leaf has a paired root with a monochromatic full path of the same color \(t\) as the leaf, that path lifts to a monochromatic full path of the full cube: start in facet \(s\), retain every old direction's edge colors by taking the constant new direction at the suitable end while the sole neighbor is read in facet \(s\), and append the same-color step. In particular the failure certificates above require careful attention to the one-switch witnesses, not merely the existence of independently monochromatic facet paths of the favorable color.

The unresolved source-leaf obstruction has thus been isolated as a one-direction cross-intersection problem, while responsive leaves have been removed unconditionally. This provides a focused next target for root-synchronization or path-exchange arguments.

## Local-incidence enumeration of arbitrary full geodesic color words

The cycle-syndrome theorem can be sharpened to describe *all* rooted full geodesics and both monotone orientations as local incidence constraints, with no restriction to trees, affine color functions, or special orders.

Let \(G=G(f)\) be a connected interaction graph on the \(d\) cube directions, and let
\[
f_i:\mathbb F_2^{N_G(i)}\to\mathbb F_2
\]
be its arbitrary local direction-color functions. Fix any prescribed direction-indexed step-color vector \(t=(t_i)_{i\in V(G)}\in\mathbb F_2^d\). Define the independently selectable local input patterns
\[
\mathcal A(t)=\prod_{i\in V(G)} f_i^{-1}(t_i).
\tag{16}
\]
For \(a\in\mathcal A(t)\), put \(\lambda_{ij}=1+a_{ij}+a_{ji}\) on each graph edge. If \(\lambda\) has zero sum around every cycle, choose either solution \(x\) of \(x_i+x_j=\lambda_{ij}\), orient graph edge \(j\to i\) when \(a_{ij}+x_j=1\), and denote the resulting orientation by \(O(a,x)\). The other root potential is \(\bar x\), which reverses the entire orientation.

Let \(L(O)\) be the number of topological total orders of an acyclic graph orientation \(O\), and zero when \(O\) has a directed cycle. Let \(L_\uparrow(O,t)\) count those topological total orders \(\pi\) that also satisfy
\[
t_{\pi_1}\le t_{\pi_2}\le\cdots\le t_{\pi_d},
\]
and define \(L_\downarrow(O,t)\) similarly with reversed inequality.

**Theorem 18 (local incidence path census).** The number of rooted directed full cube geodesics whose edge color in direction \(i\) is \(t_i\) equals
\[
\boxed{
N_t(f)=\sum_{\substack{a\in\mathcal A(t)\\
\lambda(a)\text{ has zero cycle periods}}}
\Bigl(L(O(a,x))+L(O(a,x)^{\rm rev})\Bigr).
}
\tag{17}
\]
The corresponding number whose *ordered* step colors are nondecreasing, respectively nonincreasing, is obtained by replacing \(L\) with \(L_\uparrow(O,t)\), respectively \(L_\downarrow(O,t)\), in both summands.

*Proof.* A rooted geodesic with root \(x\) and direction order \(\pi\) yields the incidence inputs
\(a_{ij}=x_j+[\pi(j)<\pi(i)]\).
Its color in direction \(i\) is \(f_i((a_{ij})_j)=t_i\), so its incidence specification lies in \(\mathcal A(t)\). As in Theorem 5, the resulting edge cochain \(\lambda\) is a vertex coboundary and the induced graph orientation is acyclic, with \(\pi\) among its topological extensions.

Conversely, for any \(a\) with zero cycle periods, the two root potentials \(x,\bar x\) give opposite graph orientations. Each topological extension of either orientation realizes the same prescribed incident bit values at all direction steps. Its color vector is therefore \(t\). Distinct incidence specifications cannot represent the same rooted order, because the latter determines every \(a_{ij}\). Summing counts every rooted geodesic once and gives (17). Restricting the counted topological extensions to color-sorted orders proves the monotone versions. QED.

**Corollary 19 (monotone path criterion by an oriented graph cut).** Given an incidence choice \(a\in\mathcal A(t)\) with vanishing cycle periods, a rooted full \(0^*1^*\) geodesic with step-color vector \(t\) is represented by one of its two potentials if and only if its induced orientation is acyclic **and every edge between a vertex with \(t_i=0\) and one with \(t_j=1\) points from the zero vertex toward the one vertex**. For a \(1^*0^*\) path, reverse the direction of all cross-color edges.

*Proof.* A topological order that first lists all vertices of color zero and then all of color one exists if and only if the orientation has no directed cycle and no edge pointing from a one-labeled vertex toward a zero-labeled vertex. Under these conditions, take a topological order of the zero-induced subgraph followed by one of the one-induced subgraph. The reverse-color assertion is analogous. QED.

**Corollary 20 (topological reduction of the paired-root requirement).** A root \(x\) is paired precisely when there are two locally successful incidence patterns \(a^\uparrow,a^\downarrow\) (possibly having different step-color vectors \(t^\uparrow,t^\downarrow\)), both inducing *the same root potential \(x\)*, whose graph orientations are acyclic and whose respective color cuts point in opposite monotone directions. This is a finite local-incidence formulation of the paired-root problem that retains the full one-use-per-dimension condition.

**Structural significance.** Tree interaction graphs have no cycle-period restrictions and every induced orientation is acyclic, explaining Theorem 2. A graph with cycles introduces a graphic-cohomology obstruction \(\lambda\notin B^1(G;\mathbb F_2)\), followed by acyclic-orientation restrictions. The cross-color cut criterion adds a further orientation constraint only when both colors occur. This exposes an intrinsic incidence/chamber object on which a deletion-contraction or cycle-exchange proof may operate, rather than testing small cube orders.

**Relation to existing graph-orientation literature.** The parity part is closely related to the acyclic orientation with prescribed indegree parities problem: see Sylvain Gravier, Matthieu Petiteau, and Isabelle Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475 (March 2026), and the EGRES open problem on acyclic orientations with parity constraints. Acyclicity is essential and nontrivial on graphs with many cycles, as illustrated already by complete graphs. The added feature here is that the target parities and color cut can be chosen through the local color-function fibers and that two compatible root certificates are sought, rather than one prescribed parity vector.

## Unconditional paired-root theorem for arbitrary nonlinear interaction trees

The preceding target-admissible monochromatic-tree theorem is intentionally conditional: opposite constant-colored direction classes prevent monochromatic full paths. Nevertheless **every** tree-local coloring admits both monotone path orientations at one common root. This resolves the source-pendant obstruction for entire interaction trees without requiring monochromatic paths.

Let \(T\) be a tree on the direction set \(V(T)\), and let
\[
f_v:\{0,1\}^{N_T(v)}\to\{0,1\}
\]
be completely arbitrary local functions for the colors of the undirected direction-\(v\) cube edges. Fix a tree root \(r\) and orient the tree away from it. We construct one common initial cube vertex and two directed orientations of the tree edges, to be extended to full dimension orders.

For a nonroot vertex \(v\), denote its parent by \(p\) and its children by \(w_1,\ldots,w_k\). An *opposite-bit interface request* specifies:
- the starting bit \(s_p\in\{0,1\}\) of parent direction \(p\);
- the color \(U\) traversed at \(p\) in the required nondecreasing path and \(V\) traversed there in the nonincreasing path;
- two different bits \(a_\uparrow,a_\downarrow=1-a_\uparrow\), required as the observed value of bit \(v\) at the traversal of direction \(p\) in the respective paths.

The task is to choose the same starting bits for all vertices of the subtree rooted at \(v\), and to orient all its tree edges separately in the two paths, so that every oriented tree edge has nondecreasing colors in the first path and nonincreasing colors in the second. In particular the parent edge \(pv\) must satisfy its color comparison and interface request.

**Lemma 21 (universal opposite-bit subtree interface).** Every such request is feasible for every finite rooted tree and every collection of nonlinear local color functions. It can be realized recursively with two evaluations of \(f_v\) per processed direction.

*Proof.* Induct on the subtree size. At vertex \(v\), evaluate
\[
p_0=f_v(s_p+1,0,\ldots,0),\qquad
p_1=f_v(s_p,1,\ldots,1),
\tag{21}
\]
where the first argument is the parent bit and the remaining arguments are the children's bits seen when direction \(v\) is traversed.

**Case A:** If \(p_0\ge U\) and \(p_1\ge V\), choose the starting bit
\(s_v=a_\uparrow\).
Put \(p\) before \(v\) in the nondecreasing orientation and \(v\) before \(p\) in the nonincreasing orientation. Thus at the parent traversal the observed bit of \(v\) is respectively \(s_v=a_\uparrow\) and \(1-s_v=a_\downarrow\). Demand that every child bit seen at \(v\) be zero in the first orientation and one in the second. Under these requests the edge of direction \(v\) has colors \(p_0,p_1\), respectively. The required parent-edge comparisons are \(U\le p_0\) and \(p_1\ge V\), which hold.

**Case B:** Otherwise choose \(s_v=1-a_\uparrow\), put \(v\) before \(p\) in the nondecreasing orientation and \(p\) before \(v\) in the nonincreasing orientation. Demand that every child bit seen at \(v\) be one in the first orientation and zero in the second. The resulting colors of direction \(v\) are \(p_1,p_0\), respectively; the parent comparisons require \(p_1\le U\) and \(p_0\le V\).

Case B is always valid when A fails, because all four quantities are Boolean:
\[
\boxed{\neg(p_0\ge U\land p_1\ge V)
\quad\Longrightarrow\quad
(p_1\le U\land p_0\le V).}
\tag{22}
\]
To check (22), if \(U=V=0\), A always succeeds; if \(U=V=1\), the right side is automatic. When \((U,V)=(0,1)\), failure of A forces \(p_1=0\); when \((U,V)=(1,0)\), failure forces \(p_0=0\). Both give the desired inequalities.

In both cases the chosen parent-edge orientations and root bit \(s_v\) satisfy the interface request. Each child's required observed-bit pair is either \((0,1)\) or \((1,0)\). Apply the induction hypothesis independently to the child subtrees, taking their parent bit to be \(s_v\) and their parent color pair to be the constructed \((p_0,p_1)\) or \((p_1,p_0)\). The child realizations use mutually disjoint direction sets, so they combine into a single root assignment and two oriented trees. Every edge comparison holds. The base case of no children uses the same two schemes. QED.

**Theorem 22 (unrestricted nonlinear tree paired-root closure).** If the interaction graph of an arbitrary binary coloring of \(Q_d\) is a tree, then
\[
\boxed{P(f)\ne\varnothing.}
\tag{23}
\]
More strongly, for any specified direction \(r\) and either prescribed starting bit \(s_r\in\{0,1\}\), there is a paired root having that bit. Hence \(|P(f)|\ge2\) when \(d\ge1\).

*Proof.* Root the interaction tree at \(r\), and fix the starting bit \(s_r\) as prescribed. In the first desired orientation prescribe observed bit zero for every child of \(r\) at its traversal; in the second prescribe observed bit one. This makes the colors of direction \(r\)
\[
U=f_r(0,\ldots,0),\qquad V=f_r(1,\ldots,1).
\]
For each child of \(r\), use Lemma 21 with parent bit \(s_r\), parent color pair \((U,V)\), and interface request \((0,1)\). Combining these recursive subtree constructions gives one common starting cube vertex and two edge orientations of \(T\) such that every earlier-to-later oriented edge respects the nondecreasing, respectively nonincreasing, color order.

Because \(T\) is a tree, each orientation is acyclic. Since every cross-color edge is oriented from color zero to color one in the first orientation, a topological order of all zero-colored directions followed by one of all one-colored directions extends the entire first orientation. Similarly a topological order of one-colored directions followed by zero-colored directions extends the second. Each resulting full cube geodesic uses every direction once; the initial cube vertex is shared, because Lemma 21 uses common subtree starting bits for both orientations. Their color words are \(0^*1^*\) and \(1^*0^*\). Since either starting bit \(s_r\) may be prescribed independently, the theorem follows. QED.

**Corollary 23 (unrestricted nonlinear forest theorem).** If the interaction graph is a forest with \(c\) connected components, including isolated directions, then
\[
\boxed{|P(f)|\ge2^c.}
\tag{24}
\]
No target-admissibility, linearity, or symmetry condition is needed. The theorem follows by taking two paired roots in each component and using Cartesian factorization of the paired-root sets.

**Corollary 24 (NORI1 over arbitrary forest facets).** Let the edges of \(Q_{d+1}\) be antipodally oddly colored, with completely unrestricted odd vertical bridge colors. If the restriction to one \(Q_d\)-facet has an interaction forest with \(c\) connected components, then at least \(2^c\) directed monochromatic full antipodal geodesics cross that facet. This follows from the universal bridge equivalence and Corollary 23.

**Algorithmic form.** When the interaction forest and the local edge-color evaluation oracle are provided, the proof constructs a paired root and two full direction orders using at most two local color evaluations per direction, followed by two color-respecting topological sorts. Thus the paired-root and bridge-geodesic constructions take \(O(d)\) color queries and linear work on the forest representation.

**Audit.** An independent implementation assembled both orientations and their shared starting vertex, evaluated the traversed cube-edge colors rather than relying on the stored tree labels, and verified the monotone full color words on 4,200 randomized nonlinear tree cases in dimensions \(2\) through \(15\). Independent exhaustive checks on all \(4,096\) path-local colorings of \(Q_4\) and all \(65,536\) path-local colorings of \(Q_5\) found no paired-root-free instances. These finite audits supplement the unrestricted induction proof.

**Correction and closure interpretation.** The previously withdrawn claim that all tree-interaction colorings have *monochromatic* full paths remains false when constant directions of opposite colors occur. The new unconditional result instead guarantees the two monotone orientations from one root, which is the target needed for the bridge reduction. It eliminates all undirected interaction forests from a minimum counterexample without assuming local color targets. Thus a paired-root-free coloring must possess at least one cycle in its undirected interaction graph; its directed influence feedback components must also satisfy the independent restrictions of the SCC seam theorem. The next obstruction is cycle consistency, not pendant-tree structure.

## Full geodesic monotonicity on a cyclic interaction graph is a bounded-width constraint problem

The incidence-cycle syndrome theorem addressed monochromatic paths. For **monotone two-color paths**, the missing condition is that an acyclic orientation permit an ordering with every color-zero direction before every color-one direction. On a cycle this requirement is also local, and it yields an all-order transfer description of the paired-root conjecture.

Let the direction interaction graph be a subgraph of the cyclic graph on \(0,\ldots,n-1\), \(n\ge3\). The direction-i edge color therefore has the form \(f_i(x_{i-1},x_{i+1})\), with subscripts modulo n; all these functions may be nonlinear. Fix a root \(x\in\mathbb F_2^n\). For a cyclic edge \(i,i+1\), write \(u_i=1\) if i precedes i+1 in a dimension ordering, and \(u_i=0\) otherwise. Define
\[
\boxed{c_i(x,u)=f_i(x_{i-1}+u_{i-1},\,x_{i+1}+1-u_i).}
\tag{48}
\]
All additions to Boolean arguments are modulo two.

**Theorem (cyclic orientation criterion for monotone geodesics).** A full dimension-simple geodesic from x with word \(0^*1^*\) exists **if and only if** there is a nonconstant vector \(u\in\{0,1\}^n\) such that for each i modulo n,
\[
\boxed{
u_i=1\Longrightarrow c_i(x,u)\le c_{i+1}(x,u),\qquad
u_i=0\Longrightarrow c_{i+1}(x,u)\le c_i(x,u).
}
\tag{49}
\]
For word \(1^*0^*\), reverse both displayed inequalities. The criterion remains valid for any subgraph of the cyclic interaction graph, by allowing a local function to ignore a neighbor.

*Proof.* A direction ordering induces an orientation of each cycle edge by its earlier-to-later relation. In a consistently cyclic orientation all orientation bits u_i coincide. Conversely a nonconstant u gives an acyclic orientation of the undirected cycle and hence admits a topological ordering. Under the orientation u, the bit of predecessor i−1 seen when direction i is traversed is \(x_{i-1}+u_{i-1}\); the bit of successor i+1 is \(x_{i+1}+1-u_i\). Its traversed color is therefore c_i(x,u), independently of which topological order is chosen.

An acyclic orientation admits a topological ordering in which every color-zero vertex precedes every color-one vertex **if and only if** it has no directed edge from a color-one vertex to a color-zero vertex. Necessity is immediate. For sufficiency, take topological orderings of the induced zero-color and one-color subgraphs separately, concatenating zero before one; the absence of one-to-zero arrows ensures the result respects every oriented edge. The absence condition is precisely (49). Such a topological ordering gives a full geodesic with color word \(0^*1^*\). Reversing color order proves the second assertion. \(\square\)

**Theorem (paired roots as a constant-width cyclic CSP).** Let f and g be two arbitrary binary edge colorings with interaction graphs contained in the same direction cycle. Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing}
\tag{50}
\]
holds if and only if one can choose a common root x and two nonconstant orientation words u,v satisfying (49) for f and the reversed version of (49) for g. Write the column symbol \(s_i=(x_i,u_i,v_i)\in\{0,1\}^3\). Every local constraint involves at most the four consecutive symbols
\[
\boxed{(s_{i-1},s_i,s_{i+1},s_{i+2}).}
\tag{51}
\]
Therefore (50) is decidable by a cyclic transfer algorithm of width three over an eight-symbol alphabet. Its underlying de Bruijn transfer graph has at most \(8^3=512\) boundary states; two additional two-bit masks can record whether both values occur in each of u and v, excluding cyclic orientations. The computation is **linear in n with a dimension-independent constant** (allowing enumeration of a fixed set of initial boundary states). When f=g, this tests the paired-root property.

*Proof.* Apply the first theorem to f using u and to g using v at the same root x. Each color \(c_i^u\) depends on \(x_{i-1},x_{i+1},u_{i-1},u_i\), and each neighboring color \(c_{i+1}^u\) depends on \(x_i,x_{i+2},u_i,u_{i+1}\); their comparison uses at most the four consecutive column symbols in (51). The same holds for v and g. A transfer state retains three consecutive symbols and appends one new symbol, rejecting any transition that violates the middle local condition. Recording occurrence of zero and one in each orientation word ensures neither is constant. Cyclic consistency is enforced by matching the final and initial column triples. Each valid closed walk of this transfer system gives a common root and two valid orientations, and every such triple yields a valid closed walk. The state space depends only on the eight-symbol alphabet and not on n. \(\square\)

**Corollary (finite-language closure reduction for unicyclic interactions).** Each local pair of edge-color functions \((f_i,g_i)\) belongs to an alphabet of \(16^2=256\) possibilities. The set of cyclic input words for which (50) holds is a regular language, recognized by the finite transfer system with cyclic boundary matching and nonconstant-orientation masks. Consequently the universal claim
\[
\forall n\ge3,\ \forall(f_i,g_i)_{i\in\mathbb Z_n},\
A_0(f)\cap A_1(g)\ne\varnothing
\tag{52}
\]
reduces to a finite automaton universality question. This is an **all-dimensional, finite-state proof target**, not an enumeration of a bounded set of cube dimensions. It is not asserted here that (52) is true or that its automaton universality has been decided. If proved, (52) combined with the previously established nonlinear pendant-tree elimination theorem would settle paired-root existence for every coloring whose undirected interaction graph is unicyclic, with arbitrary nonlinear pendant trees.

**Independent verification.** The orientation-CSP test was checked against an unrelated subset-reachability dynamic program for full nondecreasing and nonincreasing geodesics. All roots and both orientations were tested for 1000 random local colorings each at dimensions 3 and 4, 300 at dimension 5, and 60 at dimension 6; all results agreed. Exhaustive analysis of the 65536 possible four-direction local cycle colorings additionally gives, among those with all four cycle adjacencies present in the interaction graph, at least 12 favorable and at least 8 paired roots out of 16. This finite check is evidence only, and no all-dimensional favorable-density bound is inferred from it.

**Proof-closure significance.** The current arbitrary-cycle obstruction is not inherently factorial in the number of directions. It is represented by bounded-width local constraints, so a successful invariant of the transfer-state semigroup would establish the relevant universal intersection theorem in one argument for all cycle lengths. The next task is to find such an invariant or a counterexample to (52), not to extrapolate from small instances.

## Rigidity of nonlinear colorings on a cyclic direction-interaction graph

Let n>=3 and suppose the color of an undirected cube edge in direction i is \(f_i(x)=F_i(x_{i-1},x_{i+1})\), cyclic subscripts, where every two-input Boolean function \(F_i\) is nonconstant. An affine parity site is one of the form \(F_i(a,b)=\epsilon_i+a+b\).

**Lemma (cycle input repair).** Fix target bit t attained by every local function. Write \(S_i=F_i^{-1}(t)\subseteq\mathbb F_2^2\), with an input pair's parity being the sum of its two bits.

(a) If one site i admits two target-t inputs with equal parity and a different site j admits target-t inputs of both parities, then a full monochromatic color-t antipodal geodesic exists.

(b) If three distinct sites admit target-t inputs of both parities, the same conclusion holds.

*Proof.* Choose a permitted local input pair \(a_i=(a_i^-,a_i^+)\) for every site. The previously established cycle-incidence theorem shows these inputs can be realized by a cube root and a cycle-edge orientation whenever
\[
\boxed{\sum_i(a_i^-+a_i^++1)=0\pmod2.}
\tag{A}
\]
Such an orientation produces a full monochromatic geodesic unless all cycle edges point consistently around the cycle, because every other orientation is acyclic and has a topological direction ordering.

For (a), take one of the two equal-parity permitted inputs at i and choose the parity at j so that (A) holds, keeping all other permitted inputs arbitrary. If its orientation is cyclic, replace the input at i by the other permitted pair, which differs in both bits. Equation (A) persists; the new root is obtained by toggling bit x_i alone, while the new orientation reverses precisely the two cycle edges incident with i. Therefore it cannot also be cyclic, and gives the required full monochromatic geodesic.

For (b), use one flexible site to satisfy (A). If the resulting orientation is cyclic, choose three flexible sites. At each, an allowed single-bit input change is available, because inputs of opposite parity on two bits differ in one bit. Each selected input bit reads the starting vertex bit at one of the site's two neighboring directions. Since a starting vertex bit has only two neighboring sites, two of our three sites admit allowed changes reading *different* starting bits. Make both selected input changes, preserving (A).

These two changed entries cannot result in another cyclic orientation. Indeed every cyclic incidence prescription can be written, possibly after complementing its root, as
\[
\boxed{a_i^-=x_{i-1}+1,\qquad a_i^+=x_{i+1}.}
\tag{B}
\]
Under (B), toggling one root bit changes precisely the two incident inputs that read **that same root bit**. Toggling two or more root bits changes at least four input entries, with no cancellations, because each entry reads just one root bit. Our altered prescription changes only two entries, and they read different root bits. Thus it cannot be cyclic. Its acyclic orientation gives a full monochromatic geodesic. QED.

**Theorem (nonaffine cycle rigidity).** If every \(F_i\) is nonconstant, and at least one of the \(F_i\) is **not** an affine parity site \(F_i(a,b)=\epsilon_i+a+b\), then the coloring has a full monochromatic dimension-simple antipodal geodesic.

*Proof.* Every nonconstant Boolean function on two bits is either (i) parity or its complement, (ii) one-bit projection or its complement, or (iii) nonlinear with a quadratic term. A parity site's target-t preimage has two inputs of one parity, for either t. A projection site's target-t preimage has one input of each parity, for either t. A nonlinear site's three-input majority-color preimage has both types of flexibility.

If a parity site and a non-parity site occur, choose a target for which the non-parity site is parity-flexible. Apply Lemma (a), with the parity site furnishing the equal-parity pair.

If no parity site occurs but both a projection and a nonlinear site occur, take the nonlinear site's majority color. It furnishes the equal-parity pair and the projection site is parity-flexible. If all sites are nonlinear, among n>=3 sites two have the same majority color; again apply Lemma (a). Finally, if all sites are projections, at least three sites are flexible for either target; apply Lemma (b). These cases exhaust all nonconstant local functions. QED.

**Corollary (paired-root theorem for nonconstant cyclic locality).** Every such coloring has a paired root. The only potential exceptions to monochromaticity are the pure affine neighbor-parity colorings \(f_i(x)=\epsilon_i+x_{i-1}+x_{i+1}\) for all i; those are already handled by the all-dimensional affine-cycle theorem in this subsection, which gives all roots paired for even n and all but two antipodal roots paired for odd n. Therefore
\[
\boxed{P(f)\ne\varnothing\quad\text{for every cyclic-local coloring with no constant direction function.}}
\]
A monochromatic full path qualifies for both \(0^*1^*\) and \(1^*0^*\), proving paired-root membership whenever the first theorem applies.

**Boundaries and next target.** This theorem does not assert the result for sites with constant local color functions, where one target color may be unattainable. It also does not provide a **cross-fiber** root intersection for two unrelated cyclic colorings, which is required to apply the existing pendant-tree elimination theorem to all unicyclic interaction graphs with attached trees. That cross-intersection remains the closure target. The published bounded-width orientation-transfer system gives an all-dimensional finite-state formulation of it.

**Independent test.** Exhaustive enumeration of all \(14^4=38416\) cyclic-local Q4 colorings with nonconstant local functions found only eight without a monochromatic full geodesic. All eight belong to the pure affine parity family and match its predicted obstruction. The proof above holds in every dimension and does not rely on this finite test.

### Linear-time constructive paired roots on a nonconstant cyclic interaction graph

**Corollary (optimal constructive algorithm).** Under the hypotheses of the preceding nonlinear-cycle rigidity theorem, given the n local two-bit truth tables \(F_i\) of an arbitrary edge coloring with no constant direction function, a paired root and full monotone geodesic witnesses can be found in \(O(n)\) arithmetic operations.

*Proof.* Read each truth table and classify it as neighbor parity, one-input projection, or nonlinear. If all are neighbor parity, apply the constructive affine cycle orientation and root-classification algorithm already proved in this subsection; it performs a constant number of traversals around the cycle and constructs a root and two opposite monotone full paths.

Otherwise select target bit t and the permitted local incidence patterns using the case analysis in the preceding theorem. For the doubled-site case, choose local patterns with the required total parity; if the induced orientation is cyclic, change the two incidences at the doubled site and toggle the corresponding root bit. For the three-flexible-site case, if necessary change two permitted incidences reading different starting bits as in the parity-repair proof. Compute the root potential by propagating along the n equations \(x_i+x_{i+1}=1+a_{i,i+1}+a_{i+1,i}\); parity consistency ensures the closure equation. Orient the cycle edges according to the prescribed incidence patterns, and topologically order the resulting acyclic orientation using a queue of sources. Every stage requires only O(n) operations and yields a full monochromatic geodesic. A monochromatic path itself satisfies both monotone orientations and is therefore a paired-root witness.

Reading the n truth tables requires Omega(n), so the algorithm has optimal linear asymptotic complexity. This is a constructive **all-dimensional** theorem, not a fixed-dimension search or an average switch estimate.

The hypothesis that every local function is nonconstant is material. Extending the explicit construction to constant-color sites and, especially, to *two unrelated cyclic fiber colorings* is the remaining cross-intersection problem needed for the nonlinear pendant-tree 2-core reduction.


## Unary-reader dependency cycles admit paired monochromatic roots

Let \(d\ge2\) and let every direction-\(i\) edge have color
\[
f_i(x)=x_{r(i)}+a_i\pmod2,
\qquad r(i)\ne i.
\]
The functional digraph \(i\mapsto r(i)\) has disjoint directed reader cycles of lengths \(\ell_1,\ldots,\ell_c\ge2\), with attached trees.

**Theorem (monochromatic reversal-paired roots).** The number of starting cube vertices \(z\) for which some full dimension ordering \(\pi\) yields a zero-colored full geodesic, and the reverse ordering \(\pi^R\) from the same \(z\) yields a one-colored full geodesic, is
\[
\boxed{2^d\prod_{\nu=1}^c\left(1-2^{1-\ell_\nu}\right)
\ge2^{d-c}>0.}
\]
In particular every such coloring has paired roots, with no bound on the number of directed cycles or the sizes of their attached trees.

*Proof.* On the direction-\(i\) step of an ordering \(\pi\), the color equals
\[
a_i+z_{r(i)}+
[\pi^{-1}(r(i))<\pi^{-1}(i)].
\]
For every step to have color zero, the ordering must realize one precedence relation for every reader arrow. These relations define an orientation of the undirected reader graph. Tree edges never create an orientation cycle. On a reader cycle of length \(\ell\ge3\), the precedence relations are inconsistent only when all arrows orient consistently clockwise or consistently counterclockwise. The root bits of the readers on that cycle independently control the individual precedences, so two of its \(2^\ell\) patterns are bad. For a reciprocal-reader two-cycle, the two precedence relations must agree on the order of those two dimensions; two of four root patterns work. Different reader cycles use disjoint controlling bits, and bits of their attached trees are unrestricted, giving the stated multiplicative count.

For a permitted starting root, take a topological sort of the precedence graph. This orders every direction once and makes each direction color zero. Reversing that order reverses the relative order of each dimension and its distinct reader, so every direction color becomes one along the reverse path from the *same* root. Thus the root supports both monotone orientations. The count bound uses \(\ell_\nu\ge2\). \(\square\)

**Corollary (all unary edge-local colorings).** If every direction-edge bit depends on at most one other input bit, the coloring has a paired root. Its undirected dependency components are either cyclic unary-reader components covered above or dependency trees terminating at constant-colored directions. The latter are covered by the unconditional nonlinear-tree paired-root theorem in this Subsection. The Cartesian factorization theorem combines the paired roots across components.

Thus any least-dimensional paired-root counterexample must have a direction whose edge-color function depends essentially on at least two other input bits. Cyclic dependence alone, even across many functional cycles, cannot obstruct closure.


### Cyclic cross-fiber overlap theorem. Let f and g be binary edge colorings whose direction-i bits depend on the adjacent dimension bits. Suppose at each i at least two of the four possible neighboring-bit inputs make f_i=0 and g_i=1. Then some full antipodal geodesic has f-word 0*1* and g-word 1*0*. Proof: apply the established doubled/flexible incidence-repair lemma. Its exceptional case has allowed inputs forming fixed-parity antipodal pairs, with odd cyclic syndrome. The auxiliary affine cycle coloring h_i=p_i+x_(i-1)+x_(i+1) admits a full geodesic with h-word 0^(n-1)1 by the affine word-realization lemma. The first n-1 inputs meet both local requirements, making both original color words monotone. For three or more allowed pairs at every site, every prescribed dimension order has a starting root giving monochromatic f-zero and g-one paths, using composition of binary relations with at most one excluded pair.

**Affine word-realization lemma.** Write h_i(x)=p_i+x_(i-1)+x_(i+1), cyclic indices. If a prescribed bit b_i is desired as the traversed color in direction i and sum_i b_i=sum_i p_i+n modulo two, there exists a root and dimension order attaining all b_i with any chosen direction j last. To prove it, orient the cycle of dimension comparisons with u_i=1 if i is earlier than i+1. Require j to be a sink; this guarantees an acyclic orientation and a topological order ending in j. The parity of previously traversed neighbors at i is k_i=1+u_(i-1)+u_i. Let (Lx)_i=x_(i-1)+x_(i+1). The desired colors require Lx=p+b+k. For odd n, im(L) is the even-total-sum subspace, and the assumed parity equation ensures the right side lies there. For even n, im(L) requires zero sums on each cyclic parity class. In either class sum k_i=n/2+sum u_i modulo two. The assumed parity relation makes the two target sums equal, so one free u_i away from the edges fixed at the sink sets both to zero. Solve for x, then topologically sort the oriented cycle. In the exceptional overlap case set b_j=1 and all other b_i=0; the result gives a path with auxiliary word 0^(n-1)1.

**Proof of the doubled/flexible overlap dichotomy.** An allowed set D_i of two-bit neighbor inputs is doubled when it includes a complementary pair of the same input parity and flexible when it has allowed inputs of both parities. For a simultaneous monochromatic path, select one input per direction satisfying the cyclic incidence parity sum_i(1+a_i^-+a_i^+)=0 and a noncyclic orientation of the direction cycle. Distinct doubled and flexible sites permit parity correction at the flexible site. If the resulting orientation is cyclic, complement both bits at the doubled site. This keeps the incidence parity unchanged but reverses its two neighboring comparison edges, making the orientation acyclic. Any set of three permitted pairs is both doubled and flexible, so it can be combined with another site. If no doubled set occurs, each site is flexible; the earlier three-flexible-site repair lemma gives an acyclic input pattern. The sole remaining case is all allowed sets being size-two complementary pairs, with fixed input parities p_i. The incidence condition is then possible precisely if sum_i(1+p_i)=0. When the syndrome vanishes, complementing both inputs at one site removes a cyclic orientation. When it is nonzero, a simultaneous monochromatic path is impossible, but the affine one-defect lemma gives a simultaneous monotone path.

**Fixed-order three-input theorem proof.** For a fixed dimension order, the two neighbor bits seen at direction i differ from starting bits x_(i-1),x_(i+1) by flags determined by the order. Requiring membership in D_i therefore defines a binary relation on those two starting bits, containing at least three of four pairs. The constraint graph joins vertices i-1 and i+1, giving one cycle when n odd, two when n even, with parallel edges in the n=4 case. Such relations are closed under composition: a pair (a,c) can fail the composition only if the successor set of a and predecessor set of c are disjoint. In a relation omitting at most one pair, all but possibly one row or column have two possible entries, so the composition can omit at most one pair as well. Composing constraints around each cycle yields a relation containing at least three pairs, including some (t,t). Backtrack to assign each starting bit consistently along that cycle, and combine the assignments. All desired local simultaneous-success inputs are attained in the prescribed full order. The procedure is linear in n using constant-size relation tables. This theorem is stronger than merely finding a common root, but requires at least three permitted local inputs at every direction.

## Punctured-cycle incidence and one-flexible-site cross-fiber closure

Let n>=3 and prescribe, for each direction i other than j, a two-bit input pair a_i=(a_i^-,a_i^+) recording the neighbor bits that the direction-i edge must see. There exists a root and a full dimension order with j last realizing every prescribed pair **if and only if** a_(j-1)^+=a_(j+1)^-. Necessity: since direction j is last, both of its neighbors see the original starting bit x_j, so their prescribed entries must agree. Sufficiency: orient the comparison cycle so that j is a sink, writing u_i=1 when direction i precedes i+1. Set x_j equal to the common prescribed bit. Along the path j+1,...,j-1, recursively solve x_i+x_(i+1)=1+a_i^++a_(i+1)^-. These equations always admit a solution because that path has no cycle. On each internal comparison edge define u_i=a_(i+1)^-+x_i. The orientation has j as a sink and is acyclic; a topological direction order ending at j realizes every prescribed neighbor input. This is an all-dimensional necessary-and-sufficient lemma.

**Corollary (one flexible site suffices).** For cyclic-local colorings f,g, let D_i be the neighboring-bit inputs producing f_i=0 and g_i=1. Assume every D_i is nonempty and at least one D_k contains two or more input pairs. Then some single full antipodal geodesic has f-word 0*1* and g-word 1*0*. Proof: Since D_k has at least two inputs, either its left-bit projection or its right-bit projection contains both zero and one. In the first case choose final direction j=k-1; in the second choose j=k+1. The other direction neighboring j has a nonempty local set, so choose a permitted pair there; the two-bit projection at site k can match its required starting bit x_j. Choose arbitrary permitted pairs at the other n-3 directions. The punctured-cycle incidence lemma realizes all the chosen inputs with j last. The first n-1 edges have f=0,g=1; the final edge may have either bit, yielding the required monotone words. If all D_i are singleton, the same result holds whenever there is at least one j for which the right bit of the input at j-1 equals the left bit at j+1. Hence the **only** remaining pattern not covered by this method has D_i={a_i} at every site and a_(j-1)^+ differing from a_(j+1)^- for every j. Exhaustive checks of dimensions 3 through 5 confirm the punctured-incidence criterion; the theorem itself is constructive and dimension-independent.

## Odd-dimensional cyclic cross-fiber theorem under nonempty local overlap

Let f,g be cyclic-local colorings and D_i their local f-zero/g-one input sets. If every D_i is nonempty and n is odd, a common starting root exists for a nondecreasing f-geodesic and nonincreasing g-geodesic. Indeed one full geodesic can satisfy both.

*Proof.* The punctured-cycle theorem handles every case with a flexible D_i, and also singleton cases admitting a final direction j with a_(j-1)^+=a_(j+1)^-. The only remaining case has singleton inputs a_i=(l_i,r_i) with r_i=1+l_(i+2) everywhere. Put the reference root x_i=1+l_(i+1). For each cyclic rotation pi_j=(j,j+1,...,j-1) choose starting root y=x+e_(j-1). Direct substitution shows every direction except the final two j-2,j-1 sees its permitted input a_i; the final two see the permitted inputs with the right neighboring bit toggled. Consequently the first n-2 steps have paired colors (f,g)=(0,1), while the last two have values in the three-element set {(0,0),(1,1),(1,0)}. Order these values by increasing f and decreasing g. The only incomparable pair is (0,0) against (1,1). If no cyclic rotation gave a favorable path, every adjacent ordered pair of the last-two labels would have to be incomparable; thus the right-flip labels would alternate between (0,0) and (1,1) around the n-cycle. This cannot happen for odd n. Hence some rotation supplies a single geodesic monotone in both colorings. QED.

For even n, the same proof reduces the hard singleton case to an alternating right-flip label sequence. The reversed orientation yields a second alternating left-flip sequence. These alternating patterns are necessary for a counterexample, not sufficient. A full all-dimensional even-case proof is still open.

## Full cyclic cross-fiber theorem under nonempty local overlap

Let f,g be two cyclic-local cube-edge colorings, and D_i the two-bit inputs where f_i=0 and g_i=1. **Theorem.** If every D_i is nonempty, then A_0(f) intersects A_1(g) for every n>=3. The paths may use different dimension orders. The theorem has no favorable-root density hypothesis.

Proof part I: If some D_i has two inputs, the punctured-cycle theorem supplies one common monotone full geodesic. If all D_i are singleton inputs a_i=(l_i,r_i) and some final direction j has r_(j-1)=l_(j+1), the same punctured-cycle theorem applies. Otherwise the mismatch equation r_i=1+l_(i+2) holds for all i. Set reference root x_i=1+l_(i+1). Every desired pair then has form a_i=(x_(i-1)+1,x_(i+1)), corresponding to the cyclic clockwise orientation of direction comparisons, which is the sole obstruction to using all desired inputs at once. For a cyclic order j,j+1,...,j-1, start instead at x+e_(j-1). Every edge except the final two sees its desired local input a_i; the last two directions j-2,j-1 see the pair obtained from a_i by flipping its right bit. Their f/g output pairs belong to {(0,0),(1,1),(1,0)}, with (0,1) occurring only at the desired input. A two-bit output pair is ordered by increasing f and decreasing g, with (0,1) least and (1,0) greatest. Thus unless every consecutive pair of right-flipped output labels is incomparable, one of these paths is favorable for both. Incomparability occurs only between (0,0) and (1,1), forcing those right-flipped labels to alternate around the entire cycle. This is impossible for odd n, proving the theorem in odd dimensions.

Proof part II (even n): Reverse the cyclic order of direction traversals, beginning at the complementary reference root (bar x)+e_(j+1). The same local incidence calculation gives all desired pairs except at the final two directions j+2,j+1, where the *left* input bit is flipped. If the left-flipped labels ever give a comparable consecutive pair in the output order, this again supplies one full path favorable in both colorings. Otherwise the left-flipped labels also alternate between (0,0) and (1,1). Since n is even, both right-flipped and left-flipped labels now have a constant value on each direction-parity class, with opposite values on opposite parity classes.

At the original reference root x, place all even-indexed directions before all odd-indexed directions. Each even direction is a source in the undirected interaction cycle, so its neighbor input is the left-flipped pair, and each odd direction is a sink, so its input is the right-flipped pair. The resulting f/g output word has two constant blocks, each either (0,0) or (1,1). Reverse the parity-block order: all odd directions before all even. Its first output block is the complement of the preceding first block, and its second is the complement of the preceding second block, because both left- and right-flipped labels alternate. Since (0,0) and (1,1) have equal first and second bits, one of these two orders has its f-bit nondecreasing, and one (possibly different) has its g-bit nonincreasing. Both full geodesics start at the SAME root x. Therefore x lies in A_0(f) intersect A_1(g), closing the even-dimensional case. The proof uses only local input patterns and the bipartition of an even cycle, not root-density estimates or case enumeration.

## Even-cycle overlap can require two different full direction orders

The odd-dimensional nonempty-overlap theorem produces one order monotone in both colorings. In even dimensions that stronger objective has an all-dimensional obstruction, while the desired cross-root conclusion can hold at every root.

Let \(n\ge4\) be even. For neighboring bits \(a=x_{i-1},b=x_{i+1}\), put \(I(a,b)=a(1-b)\), and define
\[
\boxed{
\begin{array}{c|cc}
 &f_i&g_i\\ \hline
i\text{ even}&0&I(a,b)\\
i\text{ odd}&1-I(a,b)&1.
\end{array}}
\tag{EO1}
\]
These are ordinary undirected cube-edge colorings with cyclic-neighbor dependence. At every direction the simultaneous \(f=0,g=1\) input set is the singleton
\[
\boxed{D_i=\{(1,0)\}.}
\]
Both left-flip and right-flip labels alternate between \((0,0)\) at even directions and \((1,1)\) at odd directions, realizing the remaining pattern of the preceding even-case discussion.

**Theorem (all roots cross-favorable, no common monotone order).** For (EO1),
\[
\boxed{A_0(f)=A_1(g)=V(Q_n),}
\tag{EO2}
\]
while no starting root and no single full direction order give both an \(f\)-word \(0^*1^*\) and a \(g\)-word \(1^*0^*\).

*Proof of cross-favorability.* From any root, traverse all even directions first. Their \(f\)-colors are zero. Every odd direction then sees its final even-neighbor bits, independently of the order among odd directions. Traverse the odd directions of \(f\)-color zero and then those of color one. This gives a full nondecreasing \(f\)-path.

For \(g\), traverse all odd directions first, each of color one. The even direction colors are then independent of their relative order. Traverse the even directions of color one and then those of color zero. This gives a full nonincreasing \(g\)-path from the same prescribed root. Thus (EO2) holds.

*Proof of the common-order obstruction.* The only traversed color pairs are \((0,1)\), \((0,0)\), and \((1,1)\). Under the joint monotonicity requirement, \((0,1)\) precedes both other pairs, and \((0,0),(1,1)\) are incomparable. A successful pair word therefore cannot contain both incomparable values.

Suppose it contains no \((1,1)\). Every odd direction must then see input \((1,0)\). Each even direction is read with opposite requested bits by its two odd neighbors: its left odd neighbor requests zero and its right odd neighbor requests one. Since a bit is flipped once, the even direction must be traversed strictly between those two neighbors. If that even direction has pair \((0,0)\), its later odd neighbor has \((0,1)\), violating the nonincreasing \(g\)-word. Thus every even direction must also see input \((1,0)\).

If the pair word contains no \((0,0)\), reverse the parity classes. Every even direction sees \((1,0)\), every odd direction lies between its neighboring even directions, and any odd pair \((1,1)\) precedes a later \((0,1)\), violating the nondecreasing \(f\)-word. Again all directions must see \((1,0)\).

Finally, realizing \((1,0)\) at every direction would require every direction to be traversed between its two neighbors. The first direction in a total order cannot satisfy that condition. This rules out the common order. \(\square\)

**Closure consequence.** Nonempty local overlap supports the desired two-order cross-favorability problem beyond the single-order method. The theorem above supplies a sharp obstruction to extending the preceding odd-dimensional common-order theorem unchanged to all even dimensions. It simultaneously demonstrates that alternating left/right-flip labels can coexist with maximal cross-favorability. The preceding full cyclic nonempty-overlap theorem closes this case using two orders at one root, as the pendant-tree interface and the paired-root implication formula also permit. Earlier statements leaving the even nonempty-overlap case open are superseded by that theorem. General cyclic cross-favorability with empty local overlap sets remains unresolved.

Independent exhaustive checks in dimensions four and six confirmed the common-order obstruction for the displayed family. The proof above covers every even dimension at least four.


**Deficient-direction corollary (one missing local overlap).** Suppose a pair of cyclic-local colorings has a direction j with D_j empty, and every other D_i nonempty. Put R=the set of right-neighbor bits appearing in D_(j-1) and L=the set of left-neighbor bits appearing in D_(j+1). If R intersects L, then the cross-favorable root intersection is nonempty. More strongly, there is one full geodesic with j last for which all previous edges satisfy f=0 and g=1. Proof: choose compatible bits and permitted pairs at the two neighbors of j, choose arbitrary permitted pairs at every other direction, and apply the punctured-cycle incidence criterion. This also covers any local D_j of size zero or one when at least one of the two bordering permitted sets has the relevant bit projection equal to {0,1}. Any obstruction in the single-empty-site regime must therefore impose opposite fixed values of the starting bit x_j at the two adjacent sites. Those contradictory local prescriptions, rather than the absence of overlap at j by itself, are the structural defect to analyze next. The result is a direct corollary of the preceding all-dimensional incidence lemma.### One exceptional reversed-color site in cyclic cross-favorability

Let F_i,G_i be two binary cyclic-neighbor edge-color functions on Q_n, n>=4. Define D_i={(a,b):F_i(a,b)=0,G_i(a,b)=1} and E_i={(a,b):F_i(a,b)=1,G_i(a,b)=0}.

**Theorem.** If |D_i|>=3 for every i distinct from j, and D_j union E_j is nonempty, then there is ONE full dimension-simple path whose F-colors are nondecreasing and G-colors nonincreasing. If D_j is nonempty the path has respective constant words 0^n and 1^n. Otherwise it has 0^(n-1)1 and 1^(n-1)0.

*Proof.* Put direction j last, and at that step prescribe an input from D_j if available, otherwise E_j. This fixes the starting bits x_(j-1),x_(j+1), since both neighbor directions precede j. Every other site's requirement D_i becomes a binary relation R_i on starting bits x_(i-1),x_(i+1), with at most one forbidden pair. The incidence graph of these relations is one cycle for odd n, two parity cycles for even n. Removing R_j opens a path whose endpoints are the just-prescribed bits.

Two binary relations omitting at most one pair compose to the FULL relation when their omitted values on their shared bit agree. Indeed the only obstruction to an intermediate value is a pair of disjoint singleton permitted sets, which requires different omitted middle values. FULL composed with a relation omitting at most one pair is again FULL.

If n is odd and at least five, choose site relations j+1 and j+3, sharing starting bit x_(j+2). If n is even and at least six, choose j+2 and j+4, sharing x_(j+3). None of these three directions equals j. By placing the shared direction before or after each of its two neighboring site directions, independently, ensure that their forbidden shared-bit values agree (or use that a relation is already full). This is compatible with j last. The two relations compose to FULL; further composition with the other at-least-three-pair relations leaves the whole opened path FULL. Any specified endpoint pair is therefore realizable. In the even case the remaining parity cycle has only at-least-three-pair relations; its composition contains a diagonal pair, so it too is satisfiable.

At n=4 the opened component has only site j+2. Its two neighbor directions can be placed independently before or after that site while j remains last, moving a possible forbidden pair to any of four starting-bit values. Avoid the prescribed endpoint pair. The other parity component consists of two at-least-three-pair relations on the same two bits, so their intersection is nonempty.

These choices give a root and total direction order realizing pair (F_i,G_i)=(0,1) at all i other than j, and at j either (0,1) or (1,0). Thus both ordered color words have the claimed monotonicities. QED.

The result extends the previously established nonempty-overlap theorem to one site with *empty* D_j, provided its reverse-color set E_j is nonempty and all other sites have three permitted joint inputs. Binary relation propagation constructs the witness in O(n) time.

## Terminal-block incidence realization on a cyclic direction graph

Let f,g be cyclic-neighbor cube edge colorings on Q_n, n>=3. Let B be a consecutive interval of m directions in the cyclic direction graph, with 2<=m<n; let A be its nonempty complementary path. For each i in A prescribe an arbitrary two-bit neighbor input a_i=(a_i^-,a_i^+). Then there exists a cube starting root and a total order of all n directions such that every A direction is traversed before every B direction and sees its prescribed input a_i. The order within B is arbitrary. This is a structural incidence theorem and imposes NO restrictions on the prescribed inputs.

Proof. For each internal edge (i,i+1) of the A path, impose the binary equation x_i+x_(i+1)=1+a_i^++a_(i+1)^-. Because A is a path these equations have two solutions differing by complementing all A bits. Fix either one, and orient each internal A edge so that u_i=a_(i+1)^-+x_i is the bit indicating i is traversed before i+1. With that orientation, the local neighbor bit read at each end of the internal edge agrees with the prescribed values. Choose any topological order of this oriented path. Its two endpoints abut distinct B directions because B has at least two consecutive members. Since every B direction is traversed after A, its bit is not yet toggled when read by the adjacent endpoint of A. Choose the two boundary B starting bits equal to the respective prescribed endpoint input bits. The remaining m-2 B starting bits may be chosen freely. Append all B directions after the A topological order. Every A direction reads its desired two neighbor inputs. QED.

Corollary (many compatible-prefix roots). If each i in A has at least one neighbor input where f_i=0 and g_i=1, then there are at least 2^(m-1) distinct starting roots supporting full geodesics whose first n-m edge pairs all equal (f_i,g_i)=(0,1), with the m consecutive B directions last. This follows by fixing allowed a_i and an internal A orientation, choosing either of the two A-root solutions and freely choosing the m-2 interior B bits.

For a terminal block B of size two, the remaining question is a finite two-step interface: among the two possible orders of the last two directions and the two compatible-prefix starting roots, does one order yield a sequence of f/g output pairs that is nondecreasing under the partial order (a,b)<=(c,d) iff a<=c and b>=d? If so the same full path is favorable in f and g. Failure of this two-edge test is not asserted to imply cross-root failure, since different orders in f and g can still succeed. The lemma avoids path-family complexity by localizing all failure to the terminal interval. It does not prove unrestricted cyclic cross-favorability.


### Simultaneous incidence parity and the three signed leaf ports

Let \(f,g\) be arbitrary binary edge colorings of \(Q_d\), and let \(G\) be the union of their undirected direction-interaction graphs. At every directed incidence \((i,j)\) of \(G\), prescribe two bits \(a_{ij},b_{ij}\), interpreted as the bit of \(j\) observed when the first and second full paths traverse \(i\). Put
\[
u_i=f_i((a_{ij})_{j\in N_G(i)}),\qquad
v_i=g_i((b_{ij})_{j\in N_G(i)}).
\]
All additions of incidence bits are modulo two.

**Theorem (simultaneous incidence realization).** These prescribed inputs are realized by two dimension-simple full geodesics from one common root, with the first \(f\)-color word nondecreasing and the second \(g\)-color word nonincreasing, if and only if the following conditions hold:

(i) Every edge \(ij\) satisfies
\[
\boxed{a_{ij}+b_{ij}=a_{ji}+b_{ji}.}\tag{SI1}
\]
(ii) With \(\lambda_{ij}=1+a_{ij}+a_{ji}=1+b_{ij}+b_{ji}\), every cycle \(C\) of \(G\) has \(\sum_{ij\in E(C)}\lambda_{ij}=0\). Equivalently, a potential \(x\) exists with \(x_i+x_j=\lambda_{ij}\) for every edge.
(iii) For at least one such potential, orient \(j\to i\) in \(O_f\) when \(a_{ij}+x_j=1\), and in \(O_g\) when \(b_{ij}+x_j=1\). Both orientations are acyclic. Every \(j\to i\) in \(O_f\) has \(u_j\le u_i\); every \(j\to i\) in \(O_g\) has \(v_j\ge v_i\).

*Proof.* Along two paths from a common root \(x\), the incidence equations are
\[
a_{ij}=x_j+[\text{\(j\) precedes \(i\) in the first order}],\qquad
b_{ij}=x_j+[\text{\(j\) precedes \(i\) in the second order}].
\]
On every edge, one end precedes the other in each order. Comparing the two equations at both ends proves (SI1), and adding either path's equations on an edge gives \(x_i+x_j=\lambda_{ij}\). The orders supply the acyclic orientations and monotone color inequalities.

Conversely the cycle conditions supply \(x\). For an edge \(ij\),
\[
(a_{ij}+x_j)+(a_{ji}+x_i)=1,
\]
and likewise for \(b\); therefore the orientation prescriptions choose one direction per edge. Since \(O_f\) is acyclic and contains no arrow from a color-one direction to a color-zero direction, topologically order its color-zero vertices and then its color-one vertices. For \(O_g\) topologically order the color-one vertices and then the color-zero vertices. Both total orders recover the incidence assignments from \(x\), so they yield the required full paths. \(\square\)

For an interaction forest, the cycle condition and the acyclicity tests are automatic. Condition (SI1) provides the shared parity constraint on each edge. The possible potentials form two complementary choices per connected nontrivial tree, and free starting bits at isolated directions. The color-order tests thus depend on one global binary sign per tree component, after the local incidence data are selected.

**Lemma (signed leaf-port classification).** Let \(w\) be a leaf of \(G\) with neighbor \(v\). Fix the common starting bit \(x_v=s\) and two *candidate* traversal colors \(U,V\) at \(v\). Consider the leaf-edge comparison constraints before imposing the equations defining the traversal colors at \(v\). Write \(p=0\) for traversing \(w\) before \(v\) and \(p=1\) for traversing \(v\) before \(w\). The allowable choices are
\[
B_f=\{0:f_w(s)\le U\}\cup\{1:U\le f_w(1-s)\},
\]
\[
B_g=\{0:g_w(s)\ge V\}\cup\{1:V\ge g_w(1-s)\}.\tag{SI2}
\]
Both sets are nonempty. If \(r_f,r_g\) denote the bits of \(w\) observed at the two traversals of \(v\), then, as its **common** initial bit \(x_w\) varies, the relation allowed by these leaf-edge comparisons, **before testing the parent-color equations**, is one of
\[
\boxed{\{00,11\},\qquad \{01,10\},\qquad \{00,01,10,11\}.}\tag{SI3}
\]
The diagonal relation occurs if all pairs in \(B_f\times B_g\) have equal precedences, the antidiagonal if all have unequal precedences, and the full relation if both types occur.

*Proof.* The first set is nonempty because \(U=1\) always permits \(p=0\), while \(U=0\) always permits \(p=1\). Likewise \(V=0\) always permits \(p=0\), while \(V=1\) always permits \(p=1\) in the second set. For \(p_f\in B_f,p_g\in B_g\),
\[
r_f=x_w+1-p_f,\qquad r_g=x_w+1-p_g.
\]
Hence \(r_f+r_g=p_f+p_g\), and the two choices of \(x_w\) realize both pairs of the permitted parity. Taking the union over allowed precedences gives precisely (SI3). \(\square\)

All three cases occur on a two-direction tree with constant colors at \(v\). For the diagonal, choose \((U,V)=(1,0)\) and \(f_w=0,g_w=1\). For the antidiagonal, choose \((U,V)=(1,1)\) and \(f_w=g_w=0\). For the full relation, take \(s=0,(U,V)=(1,0)\) and \(f_w(x_v)=x_v,\ g_w(x_v)=1-x_v\).

**Consequence for induction.** When the two paths belong to unrelated colorings, deleting a leaf must retain whether its two observations at the parent agree, disagree, or are unrestricted, together with the parent root bit and traversal colors. Replacing all leaf interfaces by opposite-bit observations loses admissible pairs already in dimension two. The unconditional opposite-bit interface for two paths in a *single* coloring uses the common-coloring hypothesis essentially. The parity relation (SI1) and the three-way relation (SI3), subsequently intersected with the parent-local color equations, describe the boundary information needed by a simultaneous-root induction on trees.


## Quantitative gluing across a constant direction

Let F be any binary coloring of Q_(m+1) in which all edges in one direction i have common color t. Let g_0 and g_1 be its two induced Q_m facet colorings, and write A_0,A_1 for the respective rising and falling starting-root sets.

**Theorem (sharp cross-seam multiplicity).**
\[
\boxed{|P(F)|\ge 2\,|A_0(g_0)\cap A_1(g_1)|.}\tag{CG1}
\]
Furthermore the two cross intersections \(A_0(g_0)\cap A_1(g_1)\) and \(A_0(g_1)\cap A_1(g_0)\) have equal size. The coefficient two is sharp.

*Proof.* Reversing a full path identifies \(A_1(g_s)=\overline{A_0(g_s)}\). The antipodal map therefore bijects the two cross intersections; denote their common size by K.

If t=0, any starting root (s,y) with y in \(A_0(g_{1-s})\cap A_1(g_s)\) is paired: for the rising witness traverse i first and then a rising path in facet 1-s; for the falling witness traverse a falling path in facet s and then i last. If t=1, any (s,y) with y in \(A_0(g_s)\cap A_1(g_{1-s})\) is paired: place i last on the rising path and first on the falling path. Thus each of the two i-facets contains at least K paired roots, proving (CG1).

When g_0=g_1=g and other edge colors are independent of bit i, F is the Cartesian product of g with a single constant-colored direction. Projecting full paths and inserting the constant-colored step at the appropriate phase seam gives \(P(F)=P(g)\times\{0,1\}\), hence equality in (CG1). \(\square\)

**Corollary.** If both facet colorings each have a one-vertex directed feedback set, the existing two-color cross-root theorem implies \(|P(F)|\ge2^m\). If both are two-hub stars (possibly with unrelated hub functions and leaf templates), the established cross-root bound implies \(|P(F)|\ge2^{m-2}\).

The quantitative statement makes the source-direction induction bottleneck explicit. A strengthened two-hub cross-root lower bound \(2^{m-2}\) would give \(|P(F)|\ge2^{m-1}\), matching the proposed feedback-number-two paired-root multiplicity. Such a cross-root improvement is not proved here.
