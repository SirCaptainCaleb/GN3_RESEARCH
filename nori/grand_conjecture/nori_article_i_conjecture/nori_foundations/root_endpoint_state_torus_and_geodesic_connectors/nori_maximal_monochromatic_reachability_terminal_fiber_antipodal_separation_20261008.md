# Maximum-length monochromatic reachability fibers split into antipodally exchanged components

# Terminal reachability rigidity and an antipodal separator on parallel facet fibers

Let \(Q_n\) carry an antipodally odd binary UNDIRECTED edge coloring: \(c(\bar e)=1-c(e)\). Let \(m\) be the maximum length of any monochromatic cube geodesic, over all roots and colors. Suppose no monochromatic full antipodal geodesic exists. The top-rank extension lemma gives \(m\le n-2\). Define \(d=n-m\ge2\).

**Theorem 1 (terminal-edge rigidity).** Let \(P:x\to x\oplus S\) be any monochromatic geodesic of length \(m\), color \(q\), with \(|S|=m\). For every \(i\notin S\), the two exposed edges
\[
\{x,x\oplus e_i\},\qquad
\{x\oplus S,x\oplus S\oplus e_i\}
\]
both have color \(1-q\). Furthermore the color \(q\) is uniquely determined by the *uncolored reachable endpoint pair* \(\{x,x\oplus S\}\): two monochromatic geodesics realizing the same endpoints cannot have opposite colors.

**Proof.** Either exposed edge of color \(q\) could be prepended/appended to P, producing a monochromatic geodesic of length \(m+1\), contradicting maximality. Both therefore have color \(1-q\). Since \(d\ge1\), an exposed edge exists, and its fixed color determines q for all monochromatic witnesses of the endpoint pair. QED.

**Theorem 2 (common-unused-coordinate coherence).** Suppose \(S,T\) are size-\(m\) supports such that \(x\oplus S\) and \(x\oplus T\) belong to the *color-free* monochromatic-geodesic reachability set \(R(x)\). If
\[
([n]\setminus S)\cap([n]\setminus T)\ne\varnothing,
\]
then the monochromatic witnesses from x to the two endpoints have the SAME (uniquely determined) color. Equivalently, maximal-length reachable supports of opposite witness colors have DISJOINT omitted-coordinate sets.

**Proof.** For a shared omitted coordinate i, the single physical edge \(\{x,x\oplus e_i\}\) is terminal for both paths. By Theorem 1 its color is simultaneously the complement of each path color, making those colors equal. QED.

**Theorem 3 (facet-fiber antipodal separation).** Fix a support \(U\subset[n]\) of size m, an unordered projected antipodal pair \(\{r,r\oplus U\}\subseteq Q_U\), and the remaining coordinate set \(D=[n]\setminus U\) of size d. For each exterior assignment \(t\in Q_D\), let
\[
t\in\mathcal C(U,r)
\iff
\text{the \(U\)-parallel facet with exterior bits \(t\) admits a monochromatic \(U\)-geodesic joining \(r\) to \(r\oplus U\)}.
\]
Then \(\mathcal C(U,r)\subseteq Q_D\) is invariant under exterior antipodality \(t\mapsto\bar t\). Its occupied vertices have a uniquely determined monochromatic witness color \(q(t)\), satisfying
\[
q(\bar t)=1-q(t),\qquad
q(t\oplus e_i)=q(t)\ \text{whenever }t,t\oplus e_i\in\mathcal C(U,r).
\]
In particular, NO connected component of the cube graph induced by \(\mathcal C(U,r)\) contains an antipodal pair. When d=2, the occupied set is contained in one of the two antipodal pairs \(\{00,11\}\) and \(\{01,10\}\).

**Proof.** Global antipodality maps the pair of projected endpoints to itself (as an unordered pair), complements exterior t and all edge colors, proving invariance and \(q(\bar t)=1-q(t)\). Witness color uniqueness follows from Theorem 1. For adjacent occupied exterior t,t⊕e_i, orient their monochromatic U-geodesics to start at the same projected r. Their physical starting vertices x,y are adjacent along i, which is an unused direction in BOTH maximum-length paths. The common edge \(\{x,y\}\) has color \(1-q(t)\) and \(1-q(t\oplus e_i)\), so the colors agree. Hence q is constant on every occupied component and flips under antipodality. An occupied antipodal pair in one component would require q=1-q, impossible. For d=2, every two vertices of Q_2 not mutually antipodal are adjacent, so an antipodally invariant occupied set containing representatives of both antipodal pairs would have adjacent occupied vertices and thereby one component with an antipodal pair. Thus at most one exterior antipodal pair is occupied. QED.

**Topological meaning.** The occupied facet-fiber \(\mathcal C(U,r)\), defined entirely from COLOR-FREE reachability R, admits a locally constant binary function q which is globally antipodal-odd. It must be a disconnected antipodal separator. Thus a theorem forcing even ONE occupied path from t to \(\bar t\) in some maximal-support fiber would immediately prove geodesic closure. Unlike a balanced single ridge, such a path can involve arbitrary roots and lies naturally in the user's root-coupled 2n-bit space.

**Exact outstanding obligation.** Find a dimension-independent reason, perhaps using Sperner/Hex/connector topology across several supports U and endpoint pairs r, why all maximal-support fibers cannot simultaneously admit these antipodal separators. The theorem alone does not force connectivity: e.g. a pair of isolated antipodal exterior vertices is a valid disconnected pattern.
