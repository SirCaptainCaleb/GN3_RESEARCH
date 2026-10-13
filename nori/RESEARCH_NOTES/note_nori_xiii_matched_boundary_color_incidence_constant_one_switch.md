# Matched boundary color-incidence graph with constant one-switch rainbow length

- Stable ID: note_nori_xiii_matched_boundary_color_incidence_constant_one_switch
- Author: independent research session
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: counterexample, minimum-color-degree, involution, structural-obstruction, boundary-tournaments
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7442_3
- Updated session: session_nori_r7442_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (matching the local color-color incidence of boundary-pair graphs while bounding one-switch rainbow paths).** For every odd integer \(n\ge5\), there exists a connected simple graph \(G\) with an edge coloring \(\lambda:E(G)\to[n]\), a binary edge labeling \(\chi\), and a fixed-point-free involutive automorphism \(\tau\), such that:

1. \(|V(G)|=n(n-1)\), every vertex has degree \(2(n-2)\), and each vertex sees \(n-1\) ordinary colors.
2. At every vertex, one ordinary color is absent, one other ordinary color occurs on \(n-2\) incident edges, and each of the remaining \(n-2\) colors occurs once.
3. For each color \(a\in[n]\), its color class is a disjoint union of \(n-1\) stars \(K_{1,n-2}\).
4. \(\lambda(\tau e)=\lambda(e)\) and \(\chi(\tau e)=1-\chi(e)\) for all edges.
5. Every vertex-simple rainbow path with at most one binary-label change has at most **three** edges, and there is such a path of length three.

All numerical and ordinary-color incidence assertions in (1)--(3) also hold for the ordered-pair overlap graph of the boundary \(3\)-tournament on \(n\) original vertices when an edge \((u,v)(v,w)\) is colored by the third vertex \(w\).

**Construction.** Let \(q=(n-1)/2\), \(I=\mathbb Z/n\mathbb Z\), \(S=\mathbb Z/q\mathbb Z\), and \(f(i)=i+1\pmod n\). Introduce vertices \(L_i^s,R_i^s\) for \(i\in I\), \(s\in S\). Represent indices \(i,j\) by integers \(0,\ldots,n-1\) when comparing their order. For every \(i\ne j\) and \(s\in S\), place the following edges, subject to the displayed admission conditions:
\[
\begin{array}{c|c|c|c}
\text{condition}&\text{edge}&\lambda&\chi\\
i\ne f(j)&L_i^sR_j^{s+d_0(i,j)}&i&0\\
j\ne f(i)&L_i^sR_j^{s+d_1(i,j)}&j&1,
\end{array}
\]
where
\[
d_0(i,j)=\begin{cases}0&i<j,\\-1&i>j,\end{cases}
\qquad
d_1(i,j)=d_0(i,j)+1.
\]
Sheet arithmetic is modulo \(q\). Since \(q\ge2\), the two edge types have distinct right endpoints for fixed \(i,j,s\), so this is a simple graph and \(\lambda,\chi\) are well-defined. Put \(\tau(L_i^s)=R_i^s\) and \(\tau(R_i^s)=L_i^s\).

**Degree and color incidence.** At \(L_i^s\), the label-\(0\) edges have ordinary color \(i\), with one edge for each \(j\notin\{i,f^{-1}(i)\}\), giving multiplicity \(n-2\). The label-\(1\) edges have ordinary colors \(j\in I\setminus\{i,f(i)\}\), each once. Thus \(L_i^s\) misses color \(f(i)\), sees \(i\) on \(n-2\) edges, and sees each remaining color once. The same computation at \(R_j^t\) gives \(n-2\) edges of ordinary color \(j\) and one edge for each color in \(I\setminus\{j,f(j)\}\). Hence the claimed degree and color degree hold at every vertex.

For color \(a\), all its label-\(0\) edges are centered at the \(q\) vertices \(L_a^s\), while all its label-\(1\) edges are centered at the \(q\) vertices \(R_a^t\). Each center has \(n-2\) neighbors of color \(a\). Every other vertex belongs to at most one such star, by the bijectivity of the sheet translations \(s\mapsto s+d_b(i,j)\). The centers and leaves are disjoint across the two types. Hence the color-\(a\) subgraph comprises \(2q=n-1\) disjoint \(K_{1,n-2}\)'s.

**Involution.** For \(i<j\), a label-\(0\) edge \(L_i^sR_j^s\) maps to the label-\(1\) edge \(L_j^sR_i^s\). A label-\(1\) edge \(L_i^sR_j^{s+1}\) maps to the label-\(0\) edge \(L_j^{s+1}R_i^s\), whose sheet offset is \(-1\). The reverse inequalities give the same identities. Admission conditions also transpose: the type-\(0\) condition \(i\ne f(j)\) becomes the type-\(1\) condition on \((j,i)\), and conversely. The ordinary color is \(i\) on the first pair and \(j\) on the second pair, on both members of each involution orbit. Thus \(\tau\) preserves \(\lambda\), complements \(\chi\), and fixes no vertex.

**Connectivity.** For each \(i\), choose \(j\notin\{i,f(i),f^{-1}(i)\}\). Both edge types are present between the \(i\)-th left fiber and the \(j\)-th right fiber, and their sheet offsets differ by one. Therefore, for each \(s\), a two-edge walk through a right vertex connects \(L_i^s\) to \(L_i^{s-1}\). Since \(S\) is cyclic, every left index fiber is connected within \(G\); applying \(\tau\), every right index fiber is likewise connected. Between fibers \(L_i\) and \(R_j\) with \(i\ne j\), at least one edge type is present because the permutation \(f\) has no \(2\)-cycles. Contracting each connected fiber therefore gives the connected graph \(K_{n,n}\) minus its index-matching. Consequently \(G\) is connected.

**One-switch path bound.** Every binary-\(0\) edge incident to a left vertex \(L_i^s\) has ordinary color \(i\). Every binary-\(1\) edge incident to a right vertex \(R_j^t\) has ordinary color \(j\). In a bipartite path with three consecutive \(0\)-edges, an internal vertex lies on the left and is incident to two \(0\)-edges of the same ordinary color; thus a rainbow path has no three consecutive \(0\)-edges. Dually it has no three consecutive \(1\)-edges. A four-edge path with at most one switch would consequently have binary word \(0011\) or \(1100\). For \(0011\), the middle vertex of the first two edges must be a right vertex (otherwise the two \(0\)-colors agree), while the middle vertex of the final two edges must be a left vertex (otherwise the two \(1\)-colors agree). These two vertices occupy positions one and three in a bipartite four-edge path and therefore belong to the same part, a contradiction. The argument for \(1100\) is symmetric. Hence \(L_1\le3\).

For the reverse bound, choose successive index pairs \((0,1)\), \((3,1)\), \((3,2)\) and binary labels \(0,0,1\). They are admitted because \(0,3\ne f(1)=2\) and \(2\ne f(3)=4\). Starting at any \(L_0^s\), use the uniquely determined sheet endpoints to obtain a path \(L_0^s,R_1^t,L_3^u,R_2^v\). Its ordinary colors are \(0,3,2\), so it is a vertex-simple rainbow path of length three and one binary change. Thus \(L_1=3\).

**Comparison with the boundary overlap graph.** Let \(B_n\) have vertices ordered pairs \((u,v)\) of distinct elements of \(I\), and one undirected edge between \((u,v)\) and \((v,w)\) for each ordered triple of pairwise distinct colors. Color that edge by \(w\). At \((u,v)\), the \(n-2\) incoming overlap edges all have color \(v\), while the \(n-2\) outgoing edges receive every color in \(I\setminus\{u,v\}\) once. Thus color \(u\) is missing; color \(v\) occurs \(n-2\) times; the other \(n-2\) colors occur once. For each fixed color \(a\), the centers \((v,a)\), \(v\ne a\), each support a star with \(n-2\) leaves \((u,v)\), \(u\notin\{v,a\}\), and these \(n-1\) stars are vertex-disjoint. This proves the matching incidence properties.

**Consequence.** Numerical regularity, a palette of size only one greater than minimum color degree, the full local color-multiplicity vector, and the complete star-component profile of every color class cannot alone yield a bound \(L_1\ge c\widehat\delta\) with any fixed \(c>0\). The boundary graph must be distinguished through the incidence *wiring* of the color-class stars or through other global exchange/coherence laws. This construction makes no assertion about the corresponding restricted boundary-tournament conjecture.

## Additional theorem: vertex-regular abelian Cayley symmetry and color transitivity

The graph G_n already constructed above is a Cayley graph of an abelian group, and its ordinary color classes form a single orbit under automorphisms. Set q=(n-1)/2, I=Z/nZ, and S=Z/qZ as in the construction, with every index represented by an integer 0,...,n-1. Define the permutation sigma on the vertices by
sigma(L_i^s)=L_{i+1}^{s-[i=n-1]}, sigma(R_i^s)=R_{i+1}^{s-[i=n-1]},
with index arithmetic mod n and sheet arithmetic mod q. Write d0(i,j)=0 if i<j and -1 if i>j, and d1(i,j)=d0(i,j)+1. For all i!=j,
d_b(i+1,j+1)-d_b(i,j)=[i=n-1]-[j=n-1] (mod q), b in {0,1}.
Consequently the sheet-offset correction in sigma maps each type-b edge L_i^s R_j^{s+d_b(i,j)} to an edge L_{i+1}^{s'} R_{j+1}^{s'+d_b(i+1,j+1)} of the same binary label b. The admission conditions i!=f(j), j!=f(i) are invariant because f(i)=i+1 modulo n. The ordinary edge color advances by +1 modulo n whether it is i or j. Thus sigma is a graph automorphism that preserves chi and cyclically permutes all n ordinary colors.

The vertex involution tau(L_i^s)=R_i^s, tau(R_i^s)=L_i^s commutes with sigma, preserves ordinary colors, and complements chi. The n-th power sigma^n sends every L_i^s and R_i^s to its counterpart with sheet s-1. Thus sigma has order nq and acts transitively on the nq left vertices and separately on the nq right vertices. The commuting group <sigma,tau> has order 2nq and acts transitively, hence regularly, on V(G_n), with |V(G_n)|=2nq=n(n-1). Therefore G_n is a connected Cayley graph of the abelian group Z/(nq)Z x Z/2Z. When q is odd, equivalently n=3 mod 4, this group is cyclic, and G_n is a circulant graph.

All the conclusions of the previously proved construction remain: k=n-1, the ordinary palette has n=k+1 colors, degree 2(n-2), each local ordinary color multiplicity pattern and color-class star decomposition agrees with the boundary ordered-pair model, tau is a fixed-point-free vertex automorphism with chi(tau{u,v})=1-chi({u,v}), and L_1(G_n)=3. In particular vertex transitivity, transitivity on ordinary edge colors, a central involution, and abelian Cayley geometry do not imply linear one-switch rainbow paths. No requirement on lambda under general involutions is used; this particular counterexample satisfies lambda(tau e)=lambda(e).
