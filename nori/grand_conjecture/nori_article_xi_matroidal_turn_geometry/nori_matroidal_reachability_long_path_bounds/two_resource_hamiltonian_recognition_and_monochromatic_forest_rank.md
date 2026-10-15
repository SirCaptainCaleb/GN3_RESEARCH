# Two-resource Hamiltonian recognition and monochromatic forest rank

# Two-resource Hamiltonian recognition and monochromatic forest rank

Let \(n\ge4\), let \(V=[n]\), and let \(\mathcal T_n\) denote reversal-orbits \([a,b,c]=[c,b,a]\) of ordered triples with pairwise distinct entries. As established in the boundary-cover construction, \(\mathcal T_n\) is the edge set of the line graph \(L(K_n)\): the turn \([a,b,c]\) joins its two **edge states** \(ab=\{a,b\}\) and \(bc=\{b,c\}\) and has **middle label** \(b\).

For a subset \(T\subseteq\mathcal T_n\), let \(J_T\) be the subgraph of \(L(K_n)\) with edge set \(T\), discarding isolated state vertices. Write \(S(T)\subseteq E(K_n)\) for its vertex support, i.e. the union of the two state edges activated by each triple. We say that \(T\) is **resource-feasible** if

* no two selected triples have the same middle label (independence in the middle-label partition matroid), and
* \(S(T)\) is independent in the graphic matroid \(M(K_n)\).

These conditions are intrinsic to the two resource systems, without presupposing a path or its orientation.

**Theorem 1 (automatic path-forest structure).** Every nonempty resource-feasible \(T\) has \(J_T\) equal to a vertex-disjoint union of \(c\ge1\) simple paths (each with at least one edge). Each such component lifts, in either direction, to a vertex-simple path in \(K_n\), and its line-graph edges are precisely the selected consecutive triple reversal-orbits of that path. If \(m=|T|\), then
\[
\boxed{|S(T)|=m+c\le n-1,\qquad c\le n-1-m.}\tag{1}
\]

*Proof.* A line-graph state \(e=\{a,b\}\) is incident with selected turns centered at \(a\) or \(b\). At most one selected turn has each middle label, so the degree of \(e\) in \(J_T\) is at most two. If a component of \(J_T\) were a cycle with turns centered at \(b_1,\ldots,b_r\), then consecutive turn centers would be distinct and its state edges would be \(\{b_1,b_2\},\{b_2,b_3\},\ldots,\{b_r,b_1\}\), forming a cycle in the underlying graph \(S(T)\), contrary to graphic independence. Thus \(J_T\) is a disjoint union of paths.

For one such path with state vertices \(e_1,\ldots,e_{\ell+1}\) and successive turn centers \(b_1,\ldots,b_\ell\), the middle-label independence gives \(b_i\ne b_{i+1}\), hence each intermediate state \(e_{i+1}\) has endpoints \(b_i,b_{i+1}\). Taking the other endpoints of the first and last states gives an edge trail in \(K_n\). As its state edges belong to the forest \(S(T)\), no original vertex repeats: otherwise the trail would contain a graph cycle. It is therefore a simple path whose consecutive triple windows are the selected turns. Summing \(\ell+1\) state vertices over its \(c\) disjoint line-graph components gives \(|S(T)|=|T|+c\). Graphic independence bounds this by \(n-1\), proving (1). \(\square\)

**Corollary 2 (complete Hamiltonian window recognition).** A \(0/1\) set \(T\subseteq\mathcal T_n\) is the family of consecutive triple reversal-orbits of a Hamiltonian vertex word if and only if
\[
\boxed{|T|=n-2,\quad\text{its middle labels are distinct},\quad
S(T)\in\mathcal I(M(K_n)).}\tag{2}
\]
No separate global cut-connectivity condition is needed at this integral maximal cardinality.

*Proof.* Necessity follows from a Hamiltonian word: the middle labels are its \(n-2\) internal vertices, and its \(n-1\) consecutive \(K_n\) edges form a spanning tree. For sufficiency, Theorem 1 gives \(n-2+c=|S(T)|\le n-1\), so \(c=1\). Thus \(J_T\) is one simple path on \(n-1\) edge states. Its lift is a simple \(K_n\) path with \(n-1\) edges, hence Hamiltonian. \(\square\)

This proves that a *full-rank* middle-partition selection with graphic-independent state support automatically satisfies the connectivity and incidence requirements absent from the bare Smith lattice and uniform-matroid base polytope. Both resource tests are necessary: several selected turns of the same center can form a line-graph star despite an underlying forest, while a repeated original vertex gives a graphic circuit despite distinct middle labels.

**Theorem 3 (complete single-turn augmentation test).** Let \(T\ne\varnothing\) be resource-feasible with \(|T|<n-2\), and let \(B=(V,S(T))\) be its underlying forest. There exists \(t\notin T\) such that \(T\cup\{t\}\) remains resource-feasible if and only if at least one of the following holds:

1. \(B\) is disconnected on \(V\); or
2. \(B\) is a spanning tree having a vertex \(b\) of degree at least two which is not yet used as the middle label of any turn in \(T\).

*Proof.* If \(B\) is disconnected, choose a leaf \(b\) in a nontrivial tree component, and let \(ab\in S(T)\) be its incident edge. Since \(\deg_B(b)=1\), no selected turn is centered at \(b\). Choose \(c\) in another component. The new turn \([a,b,c]\) has unused middle label \(b\), and its activated edge \(bc\) joins two forest components; adding it preserves graphic independence.

If \(B\) is a spanning tree and \(b\) is an unused center with two incident tree edges \(ab,bc\), the turn \([a,b,c]\) adds no new state edge to \(S(T)\), preserves middle-label independence, and is not already selected. It therefore augments \(T\).

Conversely, when \(B\) is a spanning tree no new underlying \(K_n\) edge can be activated without creating a cycle. Any added turn must use two edges already in \(B\), so its center must have tree degree at least two; distinct middle labels require it to be unused. \(\square\)

**Corollary 4 (failure of ordinary matroid augmentation).** The hereditary family of resource-feasible turn sets does not satisfy the matroid augmentation axiom. For every \(n\ge5\), consider the two simple \(K_n\) paths
\[
P_1=(0,1,2),\qquad P_2=(3,2,4,5,\ldots,n-1)
\]
and let \(T\) be the union of their respective triple-window orbit sets. Its middle centers are \(1,2,4,5,\ldots,n-2\), all distinct, and its state-edge support is the spanning tree
\[
01,\ 12,\ 23,\ 24,\ 45,\ 56,\ldots,(n-2)(n-1).
\]
It has \(n-3\) selected turns. The unused centers are precisely the three leaves \(0,3,n-1\), so by Theorem 3 it admits no single-turn augmentation, even though Hamiltonian triple sets of cardinality \(n-2\) exist. In dimension five the obstruction is simply \(T=\{[0,1,2],[3,2,4]\}\).

We next quantify how much of a resource-feasible turn forest can survive in one Hamiltonian vertex word. For a reversal-odd boundary coloring \(b\), let \(\operatorname{sw}_b(P)\) be the number of color changes between successive triple windows of a simple word \(P\). Reversing the word complements and reverses the triple-color sequence, so its switch count is unchanged. Accordingly every component of \(J_T\) has an unambiguous switch count \(s_b(Q)\), independent of which direction is used to read its corresponding simple \(K_n\) path.

**Theorem 5 (cost-controlled forest-to-Hamiltonian completion).** Let \(T\ne\varnothing\) be resource-feasible with \(m=|T|=n-2-\delta\), \(\delta\ge0\), and components \(Q_1,\ldots,Q_c\) of \(J_T\). There is a Hamiltonian vertex word \(P\) satisfying
\[
\boxed{\operatorname{sw}_b(P)
\le\sum_{i=1}^{c}s_b(Q_i)+6\delta.}\tag{3}
\]
Moreover, if each component is monochromatic (possibly with different colors before choosing its direction), there is a Hamiltonian word \(P\) with
\[
\boxed{\operatorname{sw}_b(P)\le4\delta.}\tag{4}
\]
The construction uses at most \(2\delta+1\) surviving vertex-disjoint path pieces; at least \(m-3\delta\) original turn windows remain as internal windows of those pieces, with a negative bound interpreted as vacuous.

*Proof.* Let \(h\) be the number of nontrivial connected components of the \(K_n\) forest \(B=(V,S(T))\), and let \(u\) count isolated vertices of \(B\). By Theorem 1, each line-graph component \(Q_i\) lifts to a simple \(K_n\) path \(P_i\), and the sum of the numbers of vertex occurrences across these \(c\) paths is \(m+2c\). The forest \(B\) has \(|S(T)|=m+c\) edges and \(m+c+h\) nonisolated vertices, so the number of repeated vertex occurrences among \(P_1,\ldots,P_c\), beyond one occurrence per original vertex, is
\[
r=(m+2c)-(m+c+h)=c-h.\tag{5}
\]
Assign every original vertex occurring in the paths to one owning occurrence and delete its other \(r\) occurrences. Deleting a vertex from a path word splits it into at most two contiguous subwords, increasing the number of pieces by at most one. After these deletions all surviving subwords are vertex-disjoint, and adding the \(u\) missing vertices as singleton words produces at most
\[
q\le c+r+u=2c-h+u=n-m+c-2h\tag{6}
\]
pieces which together use every original vertex precisely once. The bound \(m+c\le n-1\), combined with \(h\ge1\), gives \(c\le\delta+1\) and
\[
\boxed{q\le2\delta+1.}\tag{7}
\]
Each removed vertex occurrence belongs to at most three original triple windows, so at least \(m-3r\ge m-3\delta\) selected turn windows survive within the pieces.

Orient each remaining piece consistently with its original \(P_i\), and concatenate all \(q\) pieces arbitrarily into a Hamiltonian word. A triple window wholly contained inside one piece retains its original color and any switch between consecutive such windows was already counted in \(\sum_i s_b(Q_i)\). Only windows crossing a piece boundary are new; at most two triple windows cross any given boundary. Every new switch comparison is incident to one of these crossing windows, and for each boundary at most three comparisons need to be counted. Thus at most \(3(q-1)\) new changes arise. This proves
\(\operatorname{sw}_b(P)\le\sum_i s_b(Q_i)+3(q-1)
\le\sum_i s_b(Q_i)+6\delta\), establishing (3).

If each original component \(Q_i\) has constant color, reverse individual paths before trimming them so all internal triple windows of all pieces have the same prescribed color \(\epsilon\); reversal-oddness makes this possible. All triple windows not crossing a join then have color \(\epsilon\). The crossing-window indices form a union of at most \(q-1\) intervals, each of length at most two. Any assignment of the other color to positions in a union of such intervals creates at most \(q-1\) maximal runs of non-\(\epsilon\) colors: an interval of length at most two can add at most one such run. Every run contributes at most two color changes. Hence \(\operatorname{sw}_b(P)\le2(q-1)\le4\delta\), proving (4). \(\square\)

**Theorem 6 (constant-factor matroidal rank-deficiency principle).** For every reversal-odd boundary 3-tournament \(b\), define
\[
R(b)=\max\{|T|: T\subseteq\mathcal T_n
\text{ resource-feasible, and each path component of }J_T
\text{ has constant triple color}\},
\]
and set
\[
\delta(b)=n-2-R(b),\qquad
\mu(b)=\min_{\pi\in S_n}\operatorname{sw}_b(\pi).
\]
Then for every \(n\ge4\),
\[
\boxed{\delta(b)\le\mu(b)\le4\delta(b).}\tag{8}
\]

*Proof.* Take a Hamiltonian word attaining \(s=\mu(b)\) switches and delete the right-hand triple window at each switch of its triple-color sequence. At most \(s\) windows are removed; the remaining selected turns form a resource-feasible subset of its original Hamiltonian line-graph path, and every surviving component has constant color. Thus \(R(b)\ge n-2-s\), or \(\delta(b)\le\mu(b)\).

Conversely, choose a maximizing \(T\) of size \(R(b)=n-2-\delta(b)\). By Theorem 5's monochromatic completion (4), there is a Hamiltonian word with at most \(4\delta(b)\) changes. Minimizing over all words yields \(\mu(b)\le4\delta(b)\). \(\square\)

**Interpretation.** The Hamiltonian switch minimization problem is, up to a universal factor four, equivalent to maximizing the rank of a *monochromatic forest of graphic-independent triple turns with distinct centers*. The two independence systems are necessary, but their intersection on the turn ground set is not itself a matroid: Theorem 3 supplies an obstruction to single-element augmentation. A promising stronger approach is to seek a **multi-exchange augmenting principle** for this resource system under the monochromatic-component constraint. An increase in \(R(b)\) immediately reduces the quantitative ceiling (8), and finding \(R(b)\ge n-2-o(\sqrt n)\) would produce a Hamiltonian word with \(o(\sqrt n)\) switches and hence a monochromatic tight subpath of length \(\omega(\sqrt n)\). This remains conjectural. The new theorems do not settle an unrestricted long-monochromatic-path conjecture, but reduce its asymptotic strengthening to a near-basis rank statement in a structured matroidal path-forest system.

**Independent finite check.** Enumerating every subset of \(n-2\) turn orbits and applying the two independence tests gives, in dimensions \(n=4,5,6\), respectively \(12,60,360\) feasible sets and no non-Hamiltonian sets. These counts agree with the \(n!/2\) unoriented Hamiltonian words; the proofs are dimension-independent and do not rely on the enumeration.

## A legal, cost-controlled augmenting exchange

Orient each edge of the turn graph \(L(K_n)\) according to the reversal-odd coloring \(b\). The turn from edge-state \(ab\) to \(bc\) is oriented in that direction when \(b(a,b,c)=1\), and the other direction otherwise.

**Lemma 7 (local orientation energy).** For any resource-feasible turn set \(T\), put \(d_b(e,T)=1\) if an edge-state \(e\in S(T)\) has two selected turns that both point into it or both point out of it, and zero otherwise. Then
\[
\boxed{K_b(T)=\sum_{e\in S(T)}d_b(e,T)
=\sum_{Q\text{ component of }J_T}\operatorname{sw}_b(Q).}\tag{9}
\]
*Proof.* Along a component path, consecutive triple colors differ precisely when both corresponding directed turn edges have the same incoming or outgoing incidence at their common state. Reversal of the path complements and reverses its color word, preserving this count. \(\square\)

**Theorem 8 (one-for-two augmentation with at most three new switches).** For \(n\ge5\), every nonempty resource-feasible \(T\) with \(|T|<n-2\) can be replaced by a resource-feasible \(T'\) satisfying
\[
\boxed{|T'|=|T|+1,\quad |T\setminus T'|\le1,\quad
|T'\setminus T|\le2,\quad K_b(T')\le K_b(T)+3.}\tag{10}
\]
The result holds for every reversal-odd boundary coloring \(b\).

*Proof.* Write \(B=(V,S(T))\) for the original-vertex forest. If \(B\) is disconnected, choose a leaf \(u\) in a nontrivial tree component, its neighbor \(a\), and a vertex \(w\) in another component. Add the turn \([a,u,w]\). This joins forest components through the new state-edge \(uw\), uses a fresh middle label \(u\), and creates at most one local orientation defect at the old edge-state \(au\).

If \(B\) is spanning and has an unused middle label \(u\) with tree degree at least two, add the turn between two tree edges incident with \(u\). State support is unchanged, middle independence persists, and at most two orientation defects are created, because neither of the two involved line-graph states had degree exceeding one.

Otherwise \(B\) is a spanning tree whose unused middle labels are all leaves. Since \(|T|<n-2\), the tree has a branching vertex \(v\) of degree at least three: if it were a Hamiltonian path, all its internal vertices would already be selected middle labels, giving \(|T|\ge n-2\). The unique turn centered at \(v\) involves two of its incident edges. Choose a third tree edge \(vc\), absent from that turn. This state-edge must belong to the unique turn \(t_c\) centered at \(c\), so \(c\) is an internal tree vertex and the line-graph degree of state \(vc\) is one.

Choose a leaf \(u\) in the branch of \(B-v\) containing \(c\), and a leaf \(w\) in another branch. Write \(a\) for the tree neighbor of \(u\) and \(d\) for that of \(w\). The edge \(vc\) belongs to the tree path from \(u\) to \(w\), away from their leaf edges. Define
\[
\boxed{T'=(T\setminus\{t_c\})\cup\{[a,u,w],[u,w,d]\}.}\tag{11}
\]
Both inserted centers \(u,w\) were previously unused. Deleting \(t_c\) removes state \(vc\), since no other selected turn uses it. Consequently
\[
S(T')\subseteq(S(T)\setminus\{vc\})\cup\{uw\}.\tag{12}
\]
The latter set is a tree: the new chord \(uw\) creates a fundamental cycle in \(B\), and \(vc\) lies on that cycle. Thus graphic independence holds, and the new middle labels are distinct. We removed one turn and inserted two, so the selected rank grew by one.

Removing \(t_c\) creates no orientation defect. Before inserting the two new turns, the old states \(au,dw\) each have line-graph degree at most one, because the leaves \(u,w\) were unused centers; the new state \(uw\) has degree zero. The two new turns can create at most one defect at each of \(au,dw,uw\), hence at most three in total. This proves the theorem. \(\square\)

**Corollary 9 (factor-three comparison).** With the maximum monochromatic feasible-forest rank \(R(b)\), rank deficit \(\delta(b)=n-2-R(b)\), and minimum Hamiltonian switch count \(\mu(b)\) defined earlier, every \(n\ge5\) satisfies
\[
\boxed{\delta(b)\le\mu(b)\le3\delta(b).}\tag{13}
\]
*Proof.* The lower inequality is Theorem 6: from an \(s\)-switch Hamiltonian word delete the right-hand triple at each switch, retaining at least \(n-2-s\) turns partitioned into monochromatic components. For the upper inequality, start from an optimal monochromatic feasible forest \(T\), with \(K_b(T)=0\). Apply Theorem 8 a total of \(\delta(b)\) times. The final turn set has \(n-2\) edges and is Hamiltonian by Corollary 2. Its cost rose by at most three per augmentation, giving \(\mu(b)\le3\delta(b)\). \(\square\)

**Corollary 10 (cost-stable full-rank extension).** Iterating the theorem \(n-2-|T|\) times extends any nonempty feasible set to a Hamiltonian turn set, deleting at most one and adding at most two turns per step, and gives
\[
\boxed{K_b(T_*)\le K_b(T)+3(n-2-|T|).}\tag{14}
\]

This proves a legal, rank-increasing and dimension-independent cost-Lipschitz exchange theorem for the two-resource gallery. Its bound does not force successive cost increases to cancel. The remaining open objective is to obtain a stronger color-compatible augmentation principle that keeps the final cost sublinear or bounded.
