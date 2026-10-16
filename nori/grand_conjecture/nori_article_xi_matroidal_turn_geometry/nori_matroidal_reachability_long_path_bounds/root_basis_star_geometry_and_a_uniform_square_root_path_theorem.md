# Root-basis star geometry and a uniform square-root path theorem

Let \(G=(V,E)\) be a finite simple graph. Let \(\mathsf R\) be a matroid of rank \(d\), represented by nonzero vectors \(\{a_\ell:\ell\in\Lambda\}\) over a field \(\mathbb F\). Suppose the edges of \(G\) carry labels \(\lambda:E\to\Lambda\) and there is an injective vertex potential \(\phi:V\to\mathbb F^N\), where the vectors \(a_\ell\) also lie in \(\mathbb F^N\), with the following properties:

1. For every oriented edge \(uv\), \(\phi(v)-\phi(u)\) is a nonzero scalar multiple of \(a_{\lambda(uv)}\).
2. At every vertex \(v\), the \(d\) labels on its incident edges form a basis of \(\mathsf R\).

The second condition makes \(G\) \(d\)-regular. We call this the **basis-star condition**. In this Subsection, a path is resource-independent if its edge-label multiset contains no repetitions and is independent in \(\mathsf R\). Equip each vertex \(v\) with an arbitrary tournament \(T_v\) on the edges incident with \(v\). A resource-independent path \(v_1,\ldots,v_\ell\) is admissible if \(v_{i-1}v_i\to v_iv_{i+1}\) in \(T_{v_i}\) at every internal vertex. The tournament data are entirely unrestricted.

**Lemma 1 (independent resources enforce vertex simplicity).** Every resource-independent walk in \(G\) is vertex-simple. Furthermore, two resource-independent walks terminating at the same vertex, whose combined edge-label multiset is independent, have no common vertex other than their terminal vertex.

*Proof.* A nonempty closed subwalk whose labels are independent would give, by telescoping the potential \(\phi\), a nontrivial linear relation among their representing vectors: every traversed edge contributes a nonzero scalar and no label occurs twice. This is impossible. Therefore an independent-resource walk has no repeated vertex. If two walks with a common terminal \(t\) met again at \(z\ne t\), their subwalks from \(t\) to \(z\) would give two representations of \(\phi(z)-\phi(t)\). Subtracting these expressions would produce a nontrivial dependence among their combined distinct labels. Hence their intersection consists only of \(t\). \(\square\)

**Theorem 2 (basis-star terminal-edge theorem).** In the preceding setting, there is an admissible resource-independent path with \(L\) vertices satisfying
\[
\boxed{\quad d/2\le (L-1)^2,\qquad L\ge 1+\sqrt{d/2}.\quad} \tag{1}
\]

*Proof.* For an undirected edge \(e\), let \(h(e)\) be the greatest order of an admissible resource-independent path with \(e\) as its last edge, in either orientation. A two-vertex path is admissible, so \(2\le h(e)\le d+1\). Orient \(e\) toward the terminal vertex of a path attaining \(h(e)\), resolving ties arbitrarily. Since \(G\) is \(d\)-regular, the average indegree in the resulting orientation is \(d/2\); choose a vertex \(v\) with at least this indegree.

For \(2\le k\le L:=\max_e h(e)\), let \(U_k\) consist of the edges oriented toward \(v\) for which \(h(e)=k\), and put \(q=|U_k|\). If \(q=0\) there is nothing to prove. The tournament on \(U_k\) has an edge \(uv\) beating at least \((q-1)/2\) other members \(vw\) of \(U_k\). By the choice of the orientation, there is an admissible resource-independent path \(P=(v_1,\ldots,v_{k-2},u,v)\) attaining \(h(uv)=k\).

Write \(S\) for the span of the \(k-1\) representing vectors corresponding to the labels of the edges of \(P\). Suppose that a beaten edge \(vw\in U_k\) has \(a_{\lambda(vw)}\notin S\). Then \(P\) followed by \(vw\) has independent labels, and it obeys the required tournament comparison at \(v\). Lemma 1 guarantees that the resulting walk has distinct vertices. It is therefore an admissible resource-independent \((k+1)\)-vertex path ending in \(vw\), contrary to \(h(vw)=k\).

Every edge of \(U_k\) beaten by \(uv\) consequently has its representing vector in \(S\). The vectors labeling the full star at \(v\) constitute a basis of \(\mathsf R\); at most \(\dim S=k-1\) of them can lie in \(S\). One of these vectors labels the incoming edge \(uv\), which does not beat itself. Therefore at most \(k-2\) other star edges can be beaten, and
\[
(q-1)/2\le k-2,\qquad q\le 2k-3.
\]
Summing over all terminal orders,
\[
d/2\le\deg^-(v)=\sum_{k=2}^{L}|U_k|
\le\sum_{k=2}^{L}(2k-3)=(L-1)^2.
\]
This proves (1). \(\square\)

The proof uses the matroid span to control both possible failures of extension: a repeated label and a repeated vertex. The vertex-potential identity in Lemma 1 makes the second failure automatically dependent on the first. This removes the second obstruction term in the proper-edge-label terminal theorem of Article VII, while allowing labels to recur at different vertices.

### Canonical realization on products of simplices

Let \(M=\bigoplus_{j=1}^t U_{r_j,E_j}\), where \(1\le r_j<|E_j|=:m_j\). Its connected-component partition is intrinsic to \(M\). Define the componentwise rank-one reduction
\[
M^\flat=\bigoplus_{j=1}^t U_{1,E_j},
\qquad
G_M=\Gamma(M^\flat)\cong \mathop{\square}_{j=1}^t K_{m_j}.
\tag{2}
\]
The vertices of \(G_M\) are tuples \(x=(x_1,\ldots,x_t)\), with \(x_j\in E_j\); an edge changes one component coordinate from \(a\) to \(b\).

Let
\[
\mathsf R_M=\bigoplus_{j=1}^t M(K_{E_j}),\qquad
d=\operatorname{rk}(\mathsf R_M)=\sum_{j=1}^t(m_j-1).
\tag{3}
\]
Represent the edge \(ab\) in the \(j\)-th clique by \(e_b-e_a\in\mathbb R^{E_j}\), and write \(\lambda(xy)=(j,\{a,b\})\) for the edge label when \(x,y\) differ in component \(j\). The vertex potential
\[
\phi(x)=\bigoplus_{j=1}^t e_{x_j}\in\bigoplus_{j=1}^t\mathbb R^{E_j}
\tag{4}
\]
is injective. Its derivative along \(xy\) is the root \(e_b-e_a\) with the appropriate orientation. At \(x\), the root vectors of its \(m_j-1\) incident edges in coordinate \(j\) are
\[
\{e_b-e_{x_j}:b\in E_j\setminus\{x_j\}\}.
\tag{5}
\]
These form a basis of the type-\(A_{m_j-1}\) root space. Taking their union over the different components gives a basis of \(\mathsf R_M\).

**Proposition (coordinatewise simple-path criterion).** Let
\[
G=\mathop{\square}_{j=1}^t K_{m_j},\qquad
R=\bigoplus_{j=1}^t M(K_{m_j}),
\]
with the canonical labels \(\lambda(xy)=(j,\{a,b\})\) on steps changing coordinate \(j\) from \(a\) to \(b\). For any finite walk \(P=(x^0,\ldots,x^\ell)\) in \(G\), let \(P_j\) be the sequence of coordinate-\(j\) values obtained from \(x_j^0,\ldots,x_j^\ell\) by suppressing consecutive repeats. Then the following are equivalent:

(a) the multiset of all step labels along \(P\) is independent in \(R\);

(b) for every \(j\), the entries of \(P_j\) are pairwise distinct.

Under either condition, \(P\) is a vertex-simple path and \(\ell\le\operatorname{rk}(R)=\sum_j(m_j-1)\). Equality holds if and only if \(P_j\) is a Hamiltonian path in the complete graph \(K_{m_j}\) for every coordinate \(j\).

*Proof.* The labels contributed by coordinate \(j\) are the consecutive edges of the walk \(P_j\) in \(K_{m_j}\). A multiset of edges is independent in the graphic matroid if and only if it has no repeated edge and its underlying graph is a forest. A walk using only edges of a forest, each at most once, cannot revisit a vertex: a segment between successive visits would be a nonempty closed trail, necessarily containing either a repeated edge or a cycle. Conversely, a walk with pairwise distinct vertices forms a simple path, whose edges are independent in the graphic matroid. Since \(R\) is the direct sum of its factor matroids, applying this equivalence in every coordinate proves (a)\(\Leftrightarrow\)(b).

If \(x^p=x^q\) for \(p<q\), some coordinate changes between those two times, and its suppressed coordinate sequence revisits its initial value, contradicting (b). Hence \(P\) is vertex-simple. In coordinate \(j\), pairwise distinct entries imply at most \(m_j-1\) changes. Summing gives \(\ell\le\sum_j(m_j-1)\). Equality holds precisely when every coordinate changes \(m_j-1\) times and thus visits all its \(m_j\) symbols. \(\square\)

**Canonical interpretations.** When all \(m_j=2\), a full-rank independent gallery changes each binary coordinate once; it is a cube antipodal geodesic. When \(t=1\) and \(m_1=n\), a full-rank independent gallery is a Hamiltonian vertex word in \(K_n\), and its successive two-edge windows are the ordered triples of the boundary tournament. For general \(t\), a full-rank gallery is a path whose projections onto every clique factor are Hamiltonian paths, with the factor moves interleaved arbitrarily. This is a common *geometric* witness language derived from the intrinsic direct-sum graphic-root matroid. Color-compatible existence is the additional problem.


**Corollary 3 (uniform Hamming-graph theorem).** For every Cartesian product of nontrivial cliques \(G=\square_{j=1}^t K_{m_j}\), endowed with arbitrary local tournaments on its incident edges, there is a vertex-simple tournament-admissible path whose labels are independent in \(\bigoplus_j M(K_{m_j})\) and which has at least
\[
\boxed{1+\sqrt{\tfrac12\sum_j(m_j-1)}} \tag{6}
\]
vertices.

This establishes one intrinsic root-matroid extension theorem for all rank-one partition-matroid basis graphs. The source matroid ranks \(r_j\) determine additional color-carrier geometry but play no role in the root-basis terminal inequality.

### Both canonical source models

For \(M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2}\), the reduction \(M_{\rm cub}^\flat=M_{\rm cub}\) has \(G_M=Q_n\) and \(\mathsf R_M\cong U_{n,n}\). Given any coloring of undirected cube edges, order the edges incident with each cube vertex first by increasing color and then by an arbitrary tie-break. Each local tournament is transitive. An admissible path has independent direction labels and therefore is a geodesic; its edge-color word is weakly increasing. Theorem 2 supplies a geodesic of at least
\[
\boxed{\sqrt{n/2}}\tag{7}
\]
edges and at most one color change. This applies, in particular, to every NORI1 antipodally odd coloring. It strengthens the partial-geodesic bound obtained by applying the proper-label estimate of Article VII directly.

For \(M_{\rm bd}=U_{2,n}\), the reduction is \(U_{1,n}\), so \(G_M=K_n\), \(\mathsf R_M=M(K_n)\), and
\[
\Gamma(M_{\rm bd})=J(n,2)=L(G_M).
\tag{8}
\]
Let \(b(a,v,c)\in\{0,1\}\) be an arbitrary reversal-odd boundary coloring. At vertex \(v\) of \(K_n\), orient the local comparison \(av\to vc\) precisely when \(b(a,v,c)=1\). Reversal oddness makes this a tournament. Theorem 2 produces a vertex-simple path of order at least
\[
\boxed{1+\sqrt{(n-1)/2}}\tag{9}
\]
on which every consecutive triple has color one. Reversal gives an equally long color-zero path. In this model the independent-root predicate is the original-vertex graphic independence: a simple tight path uses a forest of consecutive original edges.

Thus the same rank \(d\), the same star-basis hypothesis, and the same terminal-edge proof explain both square-root bounds. In the cube the resulting geodesic is only partial; neither Theorem 2 nor Corollary 3 promotes it to a monochromatic full antipodal geodesic. Such a promotion would require the global antipodal coloring law and the additional square-exchange geometry.

### Two-arm resource bases

The potential argument also supplies a common geometric gluing rule. Let \(P,Q\) be two paths ending at a common vertex \(t\), and suppose the multiset of labels of their combined edges is a basis of \(\mathsf R\). Lemma 1 makes their union a simple path, obtained by concatenating \(P\) with the reversal of \(Q\). For the two canonical color-carrier grades this has a common binary conclusion:

- For undirected edge colors, two same-colored monochromatic arms concatenate to a monochromatic path. On the cube, full root rank \(n\) forces every coordinate to occur once, hence the other endpoints are antipodes.
- For reversal-odd colors on oriented two-edge windows, two same-colored monochromatic arms concatenate to a path with at most one color change among successive windows. Windows in the reversed arm have the complementary color, and the one junction window can only extend one of these two color runs. On \(K_n\), full root rank \(n-1\) forces a Hamiltonian tight word.

Conversely, a full monochromatic cube geodesic splits into two monochromatic arms with a basis union. The common-terminal two-arm theorem elsewhere in Article XI establishes the converse for boundary Hamiltonian words with at most one change, including its junction cases. In this way a single resource-basis packing predicate expresses both spanning conclusions; its universal existence remains conjectural. Theorem 2 supplies quantitative rank-growth toward that predicate without assuming it.

### Linear monochromatic paths from edge-density and root independence

The root-potential hypotheses strengthen the standard greedy rainbow-path argument for a properly edge-labelled graph. In particular, the independent-star property suffices without requiring the star to span all of \(\mathsf R\).

**Lemma 4 (minimum degree forces independent-root path length).** Suppose \(G\) has an injective vertex potential and a root representation as above, and the edge labels incident with each vertex are independent in \(\mathsf R\). Every nonempty edge-subgraph \(H\subseteq G\) of minimum degree \(\delta(H)\) contains a resource-independent path of at least \(\delta(H)\) edges.

*Proof.* Choose a resource-independent path \(P=(v_0,\ldots,v_\ell)\) in \(H\) with maximal length, and let \(S\) be the linear span of its \(\ell\) resource vectors. If an edge \(v_\ell w\) of \(H\) has label outside \(S\), then adding it preserves resource independence. Moreover \(w\) is new: for any \(w=v_i\) already on \(P\), the vector \(\phi(w)-\phi(v_\ell)\) is a linear combination of the root vectors labeling the terminal subpath of \(P\), hence the label of \(v_\ell w\) lies in \(S\). Thus maximality forces every \(H\)-edge incident with \(v_\ell\) to have its label in \(S\). The independent-star condition bounds their number by \(\dim S=\ell\). Therefore \(\ell\ge \deg_H(v_\ell)\ge\delta(H)\). \(\square\)

**Theorem 5 (density-to-resource-rank bound).** Under the conditions of Lemma 4, every nonempty edge-subgraph \(H=(V,E_H)\subseteq G\), including isolated vertices in \(V\), contains a resource-independent path of length at least
\[
\boxed{\left\lceil\frac{|E_H|}{|V|}\right\rceil .}\tag{10}
\]

*Proof.* Put \(a=|E_H|/|V|>0\). Iteratively delete a vertex whose degree in the remaining subgraph is strictly smaller than \(a\), if one exists. All vertices cannot be deleted: charge every edge to its endpoint deleted first. Were every vertex deleted, fewer than \(a|V|=|E_H|\) edge incidences would be charged, while each original edge is charged once. Hence a nonempty subgraph \(K\subseteq H\) survives with \(\delta(K)\ge a\). Lemma 4 gives a resource-independent path of at least \(\delta(K)\) edges, at least the ceiling in (10). \(\square\)

**Theorem 6 (free-resource rank potential).** Assume in addition that \(\mathsf R\) is free, and fix any total order on its edge-label ground set \(\Lambda\). For any edge-subgraph \(H=(V,E_H)\) with proper edge labelling and the same injective root potential, let \(L_H(v)\) be the greatest length of a path ending at \(v\) whose resource labels occur in strictly increasing order. Then
\[
\boxed{\sum_{v\in V} L_H(v)\ge 2|E_H|.}\tag{11}
\]
In particular \(H\) contains a resource-independent path of length at least \(2|E_H|/|V|\).

*Proof.* We argue by induction on \(|E_H|\). The assertion is immediate when \(E_H=\varnothing\). Choose an edge \(e=xy\) with maximal label and put \(H'=H-e\). By properness, the label of every last edge in a strictly increasing path of \(H'\) ending at \(x\) or \(y\) is smaller than \(\lambda(e)\): no other edge at either endpoint has this label. Since \(\mathsf R\) is free, appending \(e\) to either such path preserves resource independence; injectivity of the vertex potential ensures the new endpoint has not been visited. Write \(a=L_{H'}(x)\) and \(b=L_{H'}(y)\). If \(a=b\), appending \(e\) increases both endpoint maxima by at least one, and their sum increases by at least two. If, say, \(a\ge b+1\), appending \(e\) to a maximizing path ending at \(x\) increases the maximum at \(y\) by at least \(a+1-b\ge2\). In every case the sum of all endpoint maxima increases by at least two when \(e\) is restored. The induction hypothesis proves (11). \(\square\)

The argument is the increasing-geodesic potential method of Leader and Long, *Long geodesics in subgraphs of the cube*, extended here to any faithful free-resource voltage graph with proper labelling. The representation-theoretic role of freeness is explicit: a newly largest label has no circuit dependence on previously used labels. The potential hypothesis makes an attempted endpoint repetition a consequence of precisely such a circuit.

**Corollary 7 (sharp known density bound for cube edge colors).** Every two-coloring of \(E(Q_n)\) has a monochromatic coordinate-distinct geodesic of length at least \(\lceil n/2\rceil\). For an antipodally odd coloring, each of the two colors admits such a geodesic.

*Proof.* The coordinate-root matroid \(U_{n,n}\) is free, the coordinate edge labelling is proper, and its natural vertex potential is injective. The cube has \(n2^{n-1}\) edges. Under any two-coloring, a color occurs on at least \(n2^{n-2}\) edges. Apply Theorem 6 with \(|V|=2^n\). Under antipodal oddness, each edge-color class contains \(n2^{n-2}\) edges, so the argument applies to both classes. \(\square\)

The first conclusion is the Leader--Long monochromatic-geodesic corollary, recovered through Theorem 6; the both-color formulation follows from antipodal balance. This result supersedes the weaker density-to-rank bound \(\lceil n/4\rceil\) that Theorem 5 supplies in the cube. Theorem 5 retains its independent significance for represented resource matroids with circuits.


### Equality rigidity and a strict antipodal density bound

**Lemma (regular geodesic rigidity).** Let \(1\le k\le n\), and let \(H\) be a \(k\)-regular spanning edge-subgraph of \(Q_n\). If \(H\) contains no geodesic of length \(k+1\), every connected component of \(H\) is a \(k\)-dimensional face of \(Q_n\).

*Proof.* Let \(S(x)\subseteq[n]\) be the \(k\) directions of the edges of \(H\) incident with \(x\). Every direction-distinct \(H\)-path of length \(r<k\) can be extended at its last vertex: of its \(k\) incident directions, at most \(r\) have already been used. Thus every such path extends to length \(k\).

Every length-\(k\) geodesic beginning at \(x\) uses precisely the directions \(S(x)\). Indeed, if its direction set omitted \(j\in S(x)\), prepending the edge \(x+e_j,x\) would give a direction-distinct \(H\)-path of length \(k+1\), contrary to hypothesis.

Let \(xy\) be an edge of \(H\), in direction \(i\). If \(k=1\), then \(S(x)=S(y)=\{i\}\). Suppose \(k\ge2\). If some \(j\in S(y)\setminus S(x)\) existed, the two-edge path \(x,y,y+e_j\) would have distinct directions \(i,j\); extend it to length \(k\). Its direction set would contain \(j\notin S(x)\), contradicting the preceding paragraph. Therefore \(S(y)\subseteq S(x)\), and cardinality \(k\) gives \(S(y)=S(x)\). Hence \(S\) is constant along every \(H\)-edge. The component containing \(x\) contains every vertex obtained by toggling arbitrary directions from \(S(x)\), since these edges remain present, and contains no other vertex, since all its edges have directions in \(S(x)\). It is the \(k\)-face through \(x\). \(\square\)

**Theorem (equality classification in the Leader–Long bound).** Let \(1\le k\le n\) and \(H\subseteq Q_n\) be a spanning edge-subgraph with
\[
|E(H)|=k2^{n-1}.
\tag{12}
\]
Then \(H\) has a geodesic of length \(k+1\), unless its connected components are \(k\)-dimensional faces. Conversely, a partition into \(k\)-faces attains (12) and has no geodesic longer than \(k\).

*Proof.* Suppose no geodesic has length \(k+1\). For any total order \(\pi\) of the directions, let \(L_\pi(x)\) be the longest geodesic ending at \(x\) whose directions are strictly increasing in \(\pi\). The increasing-geodesic inequality (11) gives
\[
\sum_x L_\pi(x)\ge2|E(H)|=k2^n.
\]
As every \(L_\pi(x)\le k\), equality holds and \(L_\pi(x)=k\) for every vertex and every order. Fix \(x\) and choose \(\pi\) placing the \(d_H(x)\) incident directions of \(H\) before all other directions. Every increasing geodesic ending at \(x\) has its final direction among these first \(d_H(x)\) directions, so its length is at most \(d_H(x)\). Thus \(d_H(x)\ge k\). The average degree of \(H\) is \(k\) by (12), hence \(d_H(x)=k\) at every vertex. Apply the preceding lemma. Conversely, paths inside a \(k\)-face use at most its \(k\) free directions, and a spanning partition into such faces has \(2^{n-k}\cdot k2^{k-1}=k2^{n-1}\) edges. \(\square\)

**Theorem (unique two-color extremizer at half dimension).** Let \(n=2m\ge2\). In every binary edge-coloring of \(Q_n\), either a color class contains a geodesic of length \(m+1\), or there is a fixed \(m\)-element set \(S\subseteq[n]\) such that precisely the edges in directions \(S\) have color zero. Conversely, this constant direction split has no monochromatic geodesic longer than \(m\).

*Proof.* Suppose neither color has a geodesic of length \(m+1\). The increasing-geodesic inequality (11) bounds the edges in each color class by \(m2^{n-1}\). Their total is \(n2^{n-1}=2m2^{n-1}\), so both bounds are attained. The equality-classification theorem above shows that each monochromatic component is an \(m\)-face. Let \(S(x)\) be the color-zero directions incident with \(x\). Across a zero-colored edge, \(S\) stays constant because the endpoints are in the same zero-colored \(m\)-face. Across a one-colored edge, its complement \([n]\setminus S\) stays constant because the endpoints are in the same one-colored \(m\)-face. Connectivity of \(Q_n\) makes \(S(x)\) independent of \(x\). This gives the fixed direction split. In that split each monochromatic component is an \(m\)-face, so each geodesic has length at most \(m\). \(\square\)

**Corollary (strict half-dimensional geodesic bound).** For every \(m\ge1\), every antipodally odd binary edge-coloring of \(Q_{2m}\) has, in **each** color, a geodesic of length at least \(m+1\).

*Proof.* A fixed direction split is invariant under antipodal inversion, while an antipodally odd coloring reverses the colors of every antipodal edge pair. The theorem therefore supplies a monochromatic geodesic of length \(m+1\). Antipodal inversion carries any such geodesic to one of the other color, completing the proof. \(\square\)

This strict bound improves the general density-only lower bound (Corollary 7) by one in every even dimension. The uniqueness theorem classifies all two-colorings attaining the density bound, independently of antipodal oddness. Obtaining a full antipodal geodesic of length \(2m\) remains open.

**Proposition 8 (triangle obstruction to free-resource induction).** The induction proving (11) fails in general for graphic resource matroids, even on \(K_3\). Give the three edges the increasing order \(ab<bc<ac\) and use the incidence-root representation of \(M(K_3)\). In \(H'=K_3-ac\), a maximal increasing path ending at \(c\) is \(a,b,c\), using resources \(ab,bc\). The remaining largest root \(ac\) lies in their span and its addition would close a triangle and repeat \(a\). Restoring \(ac\) raises the sum of the three endpoint maxima by only one, whereas the free-resource proof requires an increment of two.

*Proof.* The incidence identity \(e_c-e_a=(e_b-e_a)+(e_c-e_b)\) is the graphic circuit relation. The lengths of maximal increasing paths ending at \(a,b,c\), respectively, are \((1,1,2)\) in \(H'\). In \(H\) they are \((2,1,2)\): the additional increasing path \(b,c,a\) increases the maximum at \(a\) by one, while the dependent edge cannot extend the two-edge path ending at \(c\). Thus the sum increases from four to five. \(\square\)

This circuit obstruction is independent of the second complication in ordinary boundary tournaments: arbitrary reversal-odd boundary data prescribe different local tournaments, which need not be restrictions of one globally ordered root set. The former prevents automatic independent extension; the latter prevents applying the global increasing-path induction. The root-basis terminal theorem permits both and retains the common square-root conclusion.

The different grades of the two original coloring systems also matter. In a cube, a monochromatic *edge* set is a dense graph whose average degree can be used in Theorem 6. In a boundary tournament, color is assigned to consecutive *turns*, and a color class does not determine an undirected edge-subgraph of comparable density. Together, freeness of the resource matroid and the carrier grade explain why a linear monochromatic *partial* cube geodesic is accessible by this method, whereas the common local-tournament proof only gives the square-root boundary estimate. A full monochromatic antipodal cube geodesic still requires the global opposition condition and additional exchange geometry.
