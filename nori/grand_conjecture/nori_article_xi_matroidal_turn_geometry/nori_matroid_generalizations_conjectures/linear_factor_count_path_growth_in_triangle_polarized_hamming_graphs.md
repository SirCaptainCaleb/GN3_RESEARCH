# Linear factor-count path growth in triangle-polarized Hamming graphs

# Linear resource-independent path growth from square-flat turns

Let \(H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), and let \(N_{\rm sp}\) be its canonical spectral resource matroid of rank \(d=k(q-1)\). Let \(b(u,v,w)\in\mathbb F_2\) be defined on all nonbacktracking ordered turns, satisfying the mixed triangle/square axioms:

(i) if \(uw\in E(H)\), then \(b(u,v,w)+b(w,v,u)=1\);

(ii) there is one global edge coloring \(c:E(H)\to\mathbb F_2\) such that \(b(u,v,w)=c(uv)+c(vw)\) whenever \(uw\notin E(H)\).

A zero-turn path has \(b=0\) at every internal turn, and it is resource-independent when its edge vectors are independent in \(N_{\rm sp}\). The involution hypothesis at the cubical endpoint, when applicable, can be imposed additionally; it is unnecessary here.

**Theorem 1 (factor-count linear guarantee).** Every such mixed triangle/square turn system contains a zero-turn \(N_{\rm sp}\)-independent path with at least
\[
\boxed{\ell\ge \lceil k/2\rceil}
\tag{1}
\]
edges. The bound is uniform in \(q\) and valid for arbitrary triangular reversal-odd comparisons.

**Proof.** Choose any two symbols in each \(K_q\) factor and let \(C\subseteq H(k,q)\) be the induced copy of the hypercube \(Q_k\) on their \(2^k\) product vertices. Every two successive edges of a geodesic in \(C\) change distinct Cartesian factors. Therefore the two outer vertices of every such turn differ in two factors and are nonadjacent in the full Hamming graph. By (ii) its turn label is the sum of the colors of the two edges.

The restriction of \(c\) to \(C\) gives a binary edge coloring of \(Q_k\). Of its two monochromatic subgraphs, at least one has average degree at least \(k/2\), because \(Q_k\) is \(k\)-regular and the edge sets partition its edges. By the Leader–Long long-geodesic theorem (Imre Leader and Eoin Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33), any subgraph of a hypercube of average degree \(a\) contains a graph geodesic of at least \(a\) edges. Hence the denser color subgraph of \(C\) contains a monochromatic geodesic with at least \(\lceil k/2\rceil\) edges.

Such a geodesic changes each cube coordinate at most once. Its consecutive edge colors coincide; by (ii), all its turn labels are zero. The spectral resource vectors of its edges lie in distinct coordinate summands and are linearly independent. Thus it is an accepted zero-turn \(N_{\rm sp}\)-independent path of the required length. \(\square\)

In conjunction with the general mixed-turn terminal bound previously proved in Article XI, of order \(\sqrt{k(q-1)}\), this yields complementary, simultaneous guarantees of linear growth in factor count and square-root growth in resource rank:
\[
\ell_{\max}\ge \max\!\left\{\lceil k/2\rceil,\ \tfrac12\sqrt{k(q-1)}\right\}.
\tag{2}
\]
Formula (2) is a lower-bound combination; the stronger proposed unified conjecture asks for \(\ell\ge k\) in addition to the square-root term. The remaining gap is therefore a factor at most two in the factor-count branch.

**Lemma 2 (matroidal minimum-degree growth).** Let \(G\) be a finite simple graph with a matroid \(N\) on \(E(G)\) such that each vertex star is independent in \(N\) and every graph cycle is dependent in \(N\). If a subgraph \(F\subseteq G\) has minimum degree \(\delta\), then from every vertex of \(F\) there is an \(N\)-independent simple path with at least \(\delta\) edges.

**Proof.** Start at any vertex. If the current path has \(r<\delta\) edges, its edge set \(X\) is independent of rank \(r\). At the terminal vertex \(v\), the incident \(F\)-edges are independent in \(N\), so at most \(r\) of them can belong to \(\operatorname{cl}_N(X)\). Thus some incident edge \(e=vw\) is outside the closure, and \(X+e\) remains independent. If \(w\) were an earlier vertex of the path, \(X+e\) would contain a graph cycle and therefore be dependent, a contradiction. Hence the path can be extended. Continue until it has at least \(\delta\) edges. \(\square\)

**Corollary 3 (self-contained density bound).** Under the hypotheses of Lemma 2, every subgraph \(F\subseteq G\) of average degree \(a\) contains an \(N\)-independent simple path of length at least \(a/2\). Moreover, for every two-color edge coloring of a \(d\)-regular graph \(G\) under these hypotheses, some monochromatic \(N\)-independent path has length at least \(d/4\).

**Proof.** Iteratively delete vertices of current degree below \(a/2\). Such deletions strictly increase the average degree of the remaining nonempty graph, so a nonempty subgraph with minimum degree at least \(a/2\) remains. Apply Lemma 2. For a two-coloring, one color subgraph has average degree at least \(d/2\); apply the first assertion to it. \(\square\)

This corollary supplies a self-contained weaker version of (1), namely \(\ell\ge k/4\) on any induced \(Q_k\), without invoking the sharper Leader–Long theorem.

**Scope and asymmetry.** The rank-\(k\) root cube witness in Theorem 1 uses only cross-factor square-flat turns. Consequently it survives completely arbitrary and non-edge-orderable triangular comparisons. At the boundary endpoint \(k=1\), however, it supplies just one edge and does not replace the square-root boundary-tournament theorem. The mixed turn system combines the flat edge-potential geometry responsible for linear-in-\(k\) growth with freely oriented triangular comparisons responsible for the separate \(\sqrt{d}\) tournament bound.
