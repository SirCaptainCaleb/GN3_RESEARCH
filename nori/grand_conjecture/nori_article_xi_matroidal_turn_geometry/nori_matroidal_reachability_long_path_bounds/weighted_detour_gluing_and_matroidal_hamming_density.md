# Weighted detour gluing and matroidal Hamming density

Let \(D_F(u,v)\) be the greatest length of a vertex-simple path from \(u\) to \(v\) in a finite graph \(F\), with \(D_F(v,v)=0\) and \(D_F(u,v)=-\infty\) for vertices in different connected components. For connected \(F\), write
\[
S_F(z)=\sum_{v\in V(F)}D_F(z,v),\qquad
W_D(F)=\sum_{\{u,v\}\subseteq V(F)}D_F(u,v).
\]

**Lemma 1 (rooted detour bound).** For every connected graph \(F\) with \(m\) edges and root \(z\),
\[
\boxed{S_F(z)\ge m.}\tag{1}
\]
*Proof.* Run undirected depth-first search rooted at \(z\), obtaining a rooted tree \(T\). Every edge of \(F\) connects a vertex to an ancestor in \(T\). Assign the edge to its deeper endpoint \(v\). The number of edges so assigned is at most the depth \(d_T(z,v)\), because different assigned edges reach different ancestors of \(v\). Therefore
\[
m\le\sum_vd_T(z,v)\le\sum_vD_F(z,v)=S_F(z).
\]
Each tree path is a simple path of \(F\). \(\square\)

**Lemma 2 (one-vertex gluing).** Let connected graphs \(A,B\) meet at a single vertex \(z\), with no other connections, and have respective orders \(a,b\) and sizes \(m_A,m_B\). Then
\[
W_D(A\cup B)=W_D(A)+W_D(B)+(b-1)S_A(z)+(a-1)S_B(z).\tag{2}
\]
If each summand satisfies \(W_D(A)\ge(a-1)m_A\) and \(W_D(B)\ge(b-1)m_B\), then their union \(F\), of order \(a+b-1\) and size \(m_A+m_B\), satisfies
\[
\boxed{W_D(F)\ge(|V(F)|-1)|E(F)|.}\tag{3}
\]
*Proof.* A simple path between vertices in \(A\) cannot leave \(A\), because its return would repeat \(z\). For \(u\in A-\{z\}\), \(v\in B-\{z\}\), the longest simple \(u\)-to-\(v\) path concatenates a longest \(u\)-to-\(z\) path in \(A\) with a longest \(z\)-to-\(v\) path in \(B\). Thus \(D_F(u,v)=D_A(u,z)+D_B(z,v)\); summing the three pair types gives (2). Lemma 1 supplies \(S_A(z)\ge m_A\) and \(S_B(z)\ge m_B\). Substitution gives
\[
W_D(F)\ge(a-1)m_A+(b-1)m_B+(b-1)m_A+(a-1)m_B=(a+b-2)(m_A+m_B).
\]
\(\square\)

**Theorem 3 (natural detour-index classes).** Every block graph, every cactus graph, and every outerplanar graph \(F\) satisfies \(W_D(C)\ge(|V(C)|-1)|E(C)|\) in each connected component \(C\).

*Proof.* A complete graph \(K_s\) has \(D(u,v)=s-1\) for every distinct pair, giving equality \(W_D(K_s)=(s-1)\binom{s}{2}\). On a cycle \(C_s\), the longer arc between any pair is a simple path of length at least \(s/2\); for \(s\ge4\),
\[
W_D(C_s)\ge\tbinom{s}{2}\frac{s}{2}\ge s(s-1),
\]
and for \(s=3\) the cycle is a clique. Lemma 2 propagates the bound through cut vertices, proving the claims for block graphs (all blocks cliques) and cactus graphs (all blocks cycles or bridges).

For outerplanar graphs it suffices to consider a two-connected block of order \(s\). Such a block has a Hamiltonian outer-face boundary and at most \(2s-3\) edges. When \(s\ge6\), its cycle already guarantees
\[
W_D(F)\ge\tbinom{s}{2}\frac{s}{2}\ge(s-1)(2s-3)\ge(s-1)|E(F)|.
\]
For \(s=5\), the cycle provides detours of length at least three for all ten unordered pairs, so \(W_D(F)\ge30>4(2s-3)=28\). For \(s=4\), the four-cycle has detour index \(16>3(2s-3)=15\). For \(s=3\), the block is \(K_3\). Lemma 2 concludes the proof. \(\square\)

**Theorem 4 (detour-index criterion for arbitrary endpoint weights).** Suppose every connected component \(C\) of a graph \(F\) of order \(s\ge2\) satisfies \(W_D(C)\ge(s-1)|E(C)|\). Then, for every real weight function \(w:V(F)\to\mathbb R\),
\[
\boxed{
\sum_{v\in V(F)}\max_{u\in V(F)}
\bigl(w(u)+D_F(u,v)\bigr)\ge\sum_{v\in V(F)}w(v)+2|E(F)|.
}\tag{4}
\]
*Proof.* For each nontrivial component \(C\) independently choose a uniform random derangement \(\pi_C\). The image \(\pi_C(v)\) is uniformly distributed over the other \(s-1\) vertices. Thus
\[
\mathbb E\sum_{v\in C}D_C(\pi_C(v),v)
=\frac{2W_D(C)}{s-1}\ge 2|E(C)|.
\]
Set \(\pi(v)=v\) for isolated vertices. Some component-preserving permutation \(\pi\) has \(\sum_vD_F(\pi(v),v)\ge2|E(F)|\). For arbitrary weights, the left side of (4) is at least
\[
\sum_v \bigl(w(\pi(v))+D_F(\pi(v),v)\bigr)
=\sum_v w(v)+\sum_vD_F(\pi(v),v),
\]
as required. \(\square\)

**Theorem 5 (matroidal Hamming-product density theorem).** Let
\[
G=\mathop{\square}_{j=1}^{t}K_{m_j},\quad
R=\bigoplus_{j=1}^{t} M(K_{m_j}),
\]
and label an edge changing coordinate \(j\) from symbol \(a\) to \(b\) by the graphic root resource \((j,\{a,b\})\). Let \(H\) be any edge-subgraph of \(G\), retaining all vertices. Assume that every graph of \(H\)-edges within every one-coordinate fiber satisfies the componentwise detour-index criterion of Theorem 4. Then \(H\) has a simple path with an \(R\)-independent set of edge labels and length at least
\[
\boxed{\left\lceil\frac{2|E(H)|}{|V(G)|}\right\rceil.}\tag{5}
\]
This holds whenever the fiber graphs are block graphs or outerplanar graphs.

*Proof.* Fix factor order \(1,\ldots,t\). Let \(L_0(x)=0\), and inductively let \(L_j(x)\) be the greatest length of a path of \(H\) ending at \(x\) that uses only factors \(1,\ldots,j\), in nondecreasing factor order, traversing within each factor a single simple path among that factor's symbols. Each such path has \(R\)-independent labels: in each factor the traversed roots form a simple graph path, a forest in \(M(K_{m_j})\), and distinct factors belong to different direct summands. These paths are vertex-simple because their potential \(\phi(x)=\oplus_i e_{x_i}\) is injective and a repeated vertex would produce a dependence among traversed root vectors.

Fix a \(j\)-coordinate fiber \(F\). Any preceding path using only the first \(j-1\) factors keeps coordinate \(j\) fixed at some \(u\). Extending it by a simple path along fiber \(F\) from \(u\) to \(v\) retains root independence and vertex simplicity. Hence the dynamic-programming recurrence is
\[
L_j(v)=\max_{u\in V(F)}\{L_{j-1}(u)+D_F(u,v)\}.\tag{6}
\]
Apply (4) to the weights \(L_{j-1}\) in every such fiber. Sum the resulting inequalities over fibers and successively over \(j\):
\[
\sum_{x\in V(G)}L_t(x)\ge 2|E(H)|.
\]
Some terminal \(x\) therefore has \(L_t(x)\ge 2|E(H)|/|V(G)|\); integrality proves (5). \(\square\)

**Corollary 6 (canonical models).** All edge-subgraphs of \(Q_n=(K_2)^{\square n}\) satisfy the hypothesis of Theorem 5, since their one-coordinate fibers are isolated vertices or \(K_2\). The conclusion recovers the Leader--Long density theorem for coordinate-distinct cube geodesics and yields monochromatic paths of at least \(n/2\) edges in each color for antipodally odd colorings. The other canonical source model \(U_{2,n}\) has rank-one reduction \(U_{1,n}\), with basis graph \(K_n\) and resource matroid \(M(K_n)\): here the full graph's fiber is a clique, so the theorem guarantees a graphic-independent length-\((n-1)\) path. Boundary coloring resides instead on oriented two-edge windows, so the earlier root-basis tournament path theorem controls its unrestricted monochromatic \(\Omega(\sqrt n)\) paths.

**Remaining conjecture.** It remains to show whether \(W_D(F)\ge(|V(F)|-1)|E(F)|\) holds for every finite connected graph. The preceding results reduce any counterexample to a two-connected graph and prove the conjecture on natural families independent of either NORI construction. The full monochromatic antipodal cube geodesic requires further use of its global color-reversal polarity.

### Rooted strengthening and reduction to two-connected blocks

The preceding detour-index theorem has a stronger rooted version on these graph families. For a connected graph \(F\), define
\[
\Delta_F(z)=S_F(z)-2|E(F)|+\deg_F(z).
\]
The proposed unrestricted **rooted detour inequality** is \(\Delta_F(z)\ge0\) for every root \(z\).

**Lemma 8 (rooted inequality is preserved by one-sums).** Suppose connected graphs \(A,B\) meet in one cut vertex \(q\), and \(\Delta_A(x)\ge0\) and \(\Delta_B(y)\ge0\) for every respective root \(x,y\). Then \(\Delta_{A\cup B}(z)\ge0\) for every root \(z\) of their union.

*Proof.* At the shared root, \(S_{A\cup B}(q)=S_A(q)+S_B(q)\), and both edge counts and degrees add, so \(\Delta_{A\cup B}(q)=\Delta_A(q)+\Delta_B(q)\ge0\). For a root \(z\in A-\{q\}\), maximal simple paths from \(z\) to \(B-\{q\}\) pass through \(q\). Hence
\[
S_{A\cup B}(z)=S_A(z)+S_B(q)+(b-1)D_A(z,q),
\]
where \(b=|V(B)|\). Since \(\deg_{A\cup B}(z)=\deg_A(z)\), this gives
\[
\Delta_{A\cup B}(z)=\Delta_A(z)+\Delta_B(q)+(b-1)D_A(z,q)-\deg_B(q)\ge0.
\]
Here \(D_A(z,q)\ge1\) and \(\deg_B(q)\le b-1\). The other case is symmetric. \(\square\)

**Theorem 9 (rooted inequality for outerplanar, cactus, and block graphs).** Every graph belonging to any of these three classes satisfies, in each connected component and for every root \(z\),
\[
\boxed{\sum_{v\in V(F)}D_F(z,v)\ge2|E(F)|-\deg_F(z).}\tag{8}
\]

*Proof.* For a clique \(K_s\), every root-to-other-vertex detour has length \(s-1\), so \(S(z)=(s-1)^2=2\binom{s}{2}-(s-1)\). For a cycle \(C_s\), its two neighbors of \(z\) can each be reached around the opposite arc in \(s-1\) edges. Thus \(S(z)\ge 2(s-1)=2|E(C_s)|-\deg(z)\). Lemma 8 settles block graphs and cacti.

For a two-connected outerplanar graph \(F\) of order \(s\), the Hamiltonian outer-face cycle provides two root-to-neighbor detours of length \(s-1\), and each of the remaining \(s-3\) vertices is reachable along the longer of two cycle arcs, giving a detour of length at least \(s/2\). Therefore
\[
S_F(z)\ge 2(s-1)+(s-3)\frac{s}{2}
=\frac{s^2+s-4}{2}.
\]
For \(s\ge4\), this is at least \(4s-8\), since the difference is \((s-3)(s-4)/2\). Outerplanarity gives \(m\le2s-3\), and two-connectivity gives \(\deg_F(z)\ge2\), so
\[
2m-\deg_F(z)\le4s-8\le S_F(z).
\]
For \(s=3\), the block is \(K_3\). Lemma 8 extends the result from blocks to all outerplanar graphs. \(\square\)

**Corollary 10 (rooted inequality implies the conjectural unrestricted weighted theorem).** If the rooted inequality (8) holds for every connected graph \(F\), then the detour-index inequality \(W_D(F)\ge(|V(F)|-1)|E(F)|\), and hence Theorems 4--5 without fiber restrictions, follow.

*Proof.* Summing (8) over all \(n\) choices of root gives
\[
2W_D(F)=\sum_z S_F(z)\ge 2n|E(F)|-\sum_z\deg_F(z)
=2(n-1)|E(F)|.
\]
Apply the derangement argument of Theorem 4 to deduce the unrestricted weighted inequality. \(\square\)

The rooted inequality is presently a **conjecture** outside the proved graph families. Lemma 8 reduces its search for counterexamples to two-connected blocks. The rooted and unrooted assertions have been tested on all connected labeled graphs of order at most six and on samples of seven-vertex graphs, without yielding a counterexample; such finite checks are diagnostic only.

### Complete bipartite and complete split blocks

Two families with arbitrarily large non-outerplanar two-connected blocks also satisfy the rooted inequality, with explicit slack.

**Theorem 11 (complete bipartite blocks).** Let \(F=K_{a,b}\), where \(1\le a\le b\). For a root \(z\) in the part of size \(a\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg_F(z))=2(a-1)^2.}\tag{9}
\]
For a root \(z\) in the part of size \(b\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg_F(z))=
\begin{cases}
2(a-1)^2,&b=a,\\
2a(a-1),&b>a.
\end{cases}}\tag{10}
\]
In particular every complete bipartite graph satisfies the rooted detour inequality.

*Proof.* A simple path in a bipartite graph alternates the two parts. The greatest possible length of a path from a vertex of the smaller part to a vertex of the other part is \(2a-1\); between two vertices of the smaller part it is \(2(a-1)\). Between two vertices of the larger part it is \(2a\) when \(b>a\), and \(2(a-1)\) when \(b=a\). These maxima are attained by alternating paths using the allowed number of vertices in each part. Thus, for a root in the smaller part,
\[
S_F(z)=2(a-1)^2+b(2a-1),\quad
2|E(F)|-\deg(z)=2ab-b=b(2a-1),
\]
giving (9). For a root in the larger part and \(b>a\),
\[
S_F(z)=2a(b-1)+a(2a-1),\quad
2|E(F)|-\deg(z)=2ab-a.
\]
Subtracting yields \(2a(a-1)\). When \(a=b\), the two parts are symmetric and (9) applies. \(\square\)

**Theorem 12 (complete split blocks).** Let \(F=K_s\vee\overline{K_t}\), with \(s\ge1\) clique vertices and \(t\ge1\) independent vertices. Write \(C\) for the clique part and \(I\) for the independent part. For \(z\in C\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg(z))=
\begin{cases}
t(t-1),&t\le s-1,\\
(s-1)^2,&t\ge s.
\end{cases}}\tag{11}
\]
For \(z\in I\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg(z))=
\begin{cases}
(t-1)^2,&t\le s,\\
s(s-1),&t\ge s+1.
\end{cases}}\tag{12}
\]
In particular every complete split graph satisfies the rooted detour inequality.

*Proof.* Let \(L_{CC},L_{CI},L_{II}\) be the greatest simple-path lengths between two distinct vertices of the indicated types. In a path, independent vertices must be separated by clique vertices. Conversely any ordering of the required clique and independent vertices respecting that separation is a path in the join. Consequently
\[
L_{CC}=s+\min(t,s-1)-1,\quad
L_{CI}=s+\min(t,s)-1,\quad
L_{II}=s+\min(t,s+1)-1.
\]
(The \(CC\) and \(II\) expressions are used only if those endpoint types occur.) Therefore
\[
S_F(z)=
\begin{cases}
(s-1)L_{CC}+tL_{CI},& z\in C,\\
sL_{CI}+(t-1)L_{II},& z\in I.
\end{cases}
\]
The graph has \(m=\binom{s}{2}+st\) edges, a clique vertex has degree \(s-1+t\), and an independent vertex has degree \(s\). Substituting the three displayed path-length formulas and simplifying in the two threshold ranges gives (11) and (12). Every right-hand side is nonnegative. \(\square\)

**Corollary 13 (high-treewidth fiber family).** The rooted inequality (8), the detour-index hypothesis of Theorem 4, and the weighted endpoint inequality (4) hold on every connected graph whose blocks belong to the union of the following classes: outerplanar graphs, complete bipartite graphs, and complete split graphs. Consequently Theorem 5 holds for arbitrary Hamming-product edge-subgraphs all of whose one-coordinate fiber components have blocks of these types.

*Proof.* Theorems 9, 11, and 12 establish the rooted bound on each block, and Lemma 8 propagates it through the block-cut tree. Summing over roots and applying Theorem 4 establishes the weighted inequality. Theorem 5 then applies fiberwise. \(\square\)

These new block families include two-connected graphs of arbitrarily large treewidth (complete bipartite graphs with both part sizes increasing, and dense complete split graphs). They extend the preceding result beyond sparse planar exchange geometries. The stronger unrestricted rooted inequality remains open.

### Dominant independent parts and complete multipartite graphs

We extend the rooted-detour inequality to graphs containing a complete bipartite spanning subgraph with a sufficiently large independent side, and thence to all complete multipartite graphs. The proofs use the preceding complete-bipartite slack formulas and the classical Ore Hamiltonian-connectedness theorem.

**Theorem 14 (stability under filling the smaller side of a biclique).** Let \(a\ge b\ge1\) be integers. Let \(A,B\) be disjoint vertex sets of cardinalities \(a,b\). Define
\[
G=\overline{K_a}\vee H,
\]
where \(H\) is an arbitrary simple graph on \(B\); thus \(A\) is independent and all \(ab\) edges between \(A,B\) belong to \(G\). Then for every root \(z\in V(G)\),
\[
\boxed{S_G(z)\ge 2|E(G)|-\deg_G(z).}\tag{13}
\]
For \(b\ge2\), a uniform lower bound for the rooted slack is
\[
\Delta_G(z):=S_G(z)-2|E(G)|+\deg_G(z)
\ge(b-1)(b-2).
\tag{14}
\]

*Proof.* Let \(G_0=K_{a,b}\subseteq G\), and let \(e=|E(H)|\le\binom b2\). Since adding edges does not reduce any longest simple-path length, \(S_G(z)\ge S_{G_0}(z)\). Also
\[
|E(G)|=ab+e,\qquad
\deg_G(z)=\deg_{G_0}(z)+\deg_H(z),
\]
where \(\deg_H(z)=0\) for \(z\in A\). Therefore
\[
\Delta_G(z)\ge\Delta_{G_0}(z)-2e+\deg_H(z)
\ge\Delta_{G_0}(z)-2e.
\tag{15}
\]
The complete-bipartite formulas in Theorem 11 give \(\Delta_{G_0}(z)\ge 2(b-1)^2\) for every root: the smaller part of \(K_{a,b}\) has order \(b\), and the displayed root slack on either side has this lower bound. Thus
\[
\Delta_G(z)\ge2(b-1)^2-b(b-1)=(b-1)(b-2)\ge0
\]
when \(b\ge2\). If \(b=1\), the only possible \(H\) has no edges and \(G=K_{a,1}\), already covered by Theorem 11. \(\square\)

The theorem allows an arbitrary pattern of up to \(\binom b2\) internal edges on \(B\), independent of whether the resulting graph is chordal, planar, or multipartite. The hypothesis is intrinsic: \(G\) contains an independent set of size at least half its order, every vertex of which is adjacent to every vertex outside that set.

**Theorem 15 (all complete multipartite graphs).** Every connected complete multipartite graph \(G=K_{a_1,\ldots,a_t}\) satisfies the rooted-detour inequality (13) for every root.

*Proof.* Let \(n=\sum_i a_i\) and \(a=\max_i a_i\). If \(a\ge n/2\), choose a part \(A\) of order \(a\) and let \(B=V(G)\setminus A\) have size \(b=n-a\le a\). All edges between \(A\) and \(B\) occur and \(A\) is independent. Theorem 14 applies, regardless of the internal multipartite graph on \(B\).

Now suppose \(a<n/2\). Since \(a\) is integral, \(a\le(n-1)/2\). Every nonadjacent pair \(u,v\) belongs to one common part of cardinality \(s\le a\), so
\[
\deg_G(u)+\deg_G(v)=2(n-s)\ge n+1.
\]
By Ore's Hamiltonian-connectedness theorem (Ore's degree-sum criterion for Hamiltonian-connected graphs, as recalled in Gould–Yu, *On hamiltonian-connected graphs*, J. Graph Theory 18 (1994), 841–860), \(G\) has a Hamiltonian path between every pair of distinct vertices. Hence \(D_G(z,v)=n-1\) for every \(v\ne z\), and
\[
S_G(z)=(n-1)^2\ge\sum_{v\ne z}\deg_G(v)=2|E(G)|-\deg_G(z),
\]
since every degree is at most \(n-1\). For orders \(n\le2\) the claim follows by direct inspection. \(\square\)

**Corollary 16 (weighted detours and Hamming products).** The weighted endpoint inequality (4) holds for every graph whose connected components are complete multipartite, or whose blocks are complete multipartite, outerplanar, complete bipartite, or complete split graphs. The matroidal Hamming-product density theorem (Theorem 5) therefore applies whenever all one-coordinate fiber components have blocks from this enlarged list.

*Proof.* Theorem 15 and Lemma 8 verify the rooted inequality through one-sum gluing. Summation over roots yields the detour-index inequality; Theorem 4 supplies arbitrary endpoint weights, which Theorem 5 propagates factor by factor. \(\square\)

The complete-multipartite result covers high-connectivity and arbitrarily large graphic circuits without requiring a bounded treewidth or chordal graph structure. It leaves the unrestricted rooted-detour and vertex-deletion conjectures open.


### Augmentation from a Hamiltonian-connected core

**Theorem 17 (sharp vertex-deletion inequality).** Let \(G\) be connected and \(H=G-v\) Hamiltonian-connected. Write \(N=|V(H)|\), \(K=N_G(v)\), and \(k=|K|\). Then for every \(z\in V(H)\),
\[
\boxed{S_G(z)-S_H(z)\ge 2k-\mathbf1_{\{z\in K\}}.}\tag{16}
\]
Consequently the rooted-detour inequality holds at every root of \(G\).

*Proof.* For \(N=1\) the graph is \(K_2\). Suppose \(N\ge2\). If \(K=\{z\}\), then \(D_G(z,v)=1=2k-\mathbf1_{\{z\in K\}}\) and every old endpoint detour can only increase. In every other case there is a neighbor \(u\in K-\{z\}\). A Hamiltonian \(z\)-to-\(u\) path in \(H\), followed by \(uv\), shows \(D_G(z,v)=N\). Every existing endpoint \(w\ne z\) has \(D_H(z,w)=N-1\), and its new detour length is either \(N-1\) or \(N\). The latter occurs whenever a Hamiltonian \(z\)-to-\(w\) path in \(H\) has two consecutive vertices in \(K\): insert \(v\) between them.

If \(2k-\mathbf1_{\{z\in K\}}\le N\), the newly available endpoint \(v\) supplies the claimed increase. If \(k>\lceil N/2\rceil\), any Hamiltonian path in \(H\) has two consecutive vertices in \(K\), since at most \(\lceil N/2\rceil\) positions of a path can be chosen without consecutive positions. All \(N-1\) old endpoints therefore gain one, and \(S_G(z)-S_H(z)=2N-1\ge2k-\mathbf1_{\{z\in K\}}\). The sole remaining possibility is \(N=2m-1\), \(k=m\), \(z\notin K\). Choose \(w\in K\) and a Hamiltonian \(z\)-to-\(w\) path in \(H\). An alternating placement of \(m\) marked \(K\)-vertices among \(2m-1\) positions with no adjacent marks must start with a marked position; since \(z\notin K\), a consecutive \(K\)-pair must occur. Inserting \(v\) gives a gain of one at endpoint \(w\), producing the required increment \(N+1=2m=2k\). This proves (16).

Because \(H\) is Hamiltonian-connected, \(S_H(z)=(N-1)^2\ge 2|E(H)|-\deg_H(z)\); adding (16) proves the rooted inequality on \(H\)'s vertices. At root \(v\) there are two cases. If \(k\ge2\), for each \(w\in H\) choose \(u\in K-\{w\}\), traverse a Hamiltonian \(u\)-to-\(w\) path of \(H\) after the initial edge \(vu\), and obtain \(D_G(v,w)=N\). Thus \(S_G(v)=N^2\ge 2|E(H)|+k=2|E(G)|-\deg_G(v)\). If \(k=1\), let \(u\) be the sole neighbor; then
\[
S_G(v)=N+S_H(u)=N+(N-1)^2
\ge2|E(H)|+1=2|E(G)|-\deg_G(v).
\]
This completes the proof. \(\square\)

The result is an unconditional one-vertex extension theorem for *arbitrary attachment neighborhoods*, provided the core is Hamiltonian-connected. Its proof isolates the failure mechanism for general vertex deletion: the desired detour increment is available by inserting a vertex between adjacent neighbors on a long endpoint path. It remains open whether an aggregate version of this argument works for arbitrary connected deletion cores.
