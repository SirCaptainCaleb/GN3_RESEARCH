# Transitive-star terminal bounds for spectral-resource paths

**Theorem (transitive-star terminal bound).** Let \(G\) be a connected finite simple graph of average degree \(d\), and \(N\) a matroid on \(E(G)\) in which every vertex star is independent and every graph cycle is dependent. At each vertex equip the incident edges with a transitive tournament. An admissible path has an \(N\)-independent edge set and respects the tournaments at successive edges. If \(L\) is the maximum number of vertices of an admissible path, then
\[
\boxed{d\le L(L-1).}
\]
**Proof.** For each edge \(e\), choose a longest admissible path ending with \(e\) in either direction, orient \(e\) toward its witness terminal, and let \(r(e)\) be its witness order. Some vertex \(v\) receives at least \(d/2\) edges. Let \(U_r\) be the incoming edges with \(r(e)=r\). The transitive tournament on \(U_r\) has an edge \(uv\) beating all others. Let \(P\) be its \(r\)-vertex witness and \(X=E(P)\), independent of rank \(r-1\). Any other \(vw\in U_r\) outside \(\operatorname{cl}_N(X)\) extends \(P\): independence of \(X+vw\) precludes a repeated vertex because every graph cycle is \(N\)-dependent, and the terminal comparison is favorable. This contradicts \(r(vw)=r\). Thus \(U_r\subseteq E(v)\cap\operatorname{cl}_N(X)\). As the star is independent, \(|U_r|\le r-1\). Summing gives \(d/2\le\sum_{r=2}^L(r-1)=L(L-1)/2\). \(\square\)

**Corollary (binary cube-edge colors).** Every binary coloring of \(E(Q_n)\) has a coordinate-distinct geodesic with at most one color change and at least
\[
\boxed{\left\lceil(\sqrt{4n+1}-1)/2\right\rceil}
\]
edges. Use the coordinate-partition resource matroid and order each star by edge color, breaking ties arbitrarily. Every admissible path has distinct coordinates and a weakly increasing color word; the cube has average degree \(n\). Antipodal oddness is not needed.

**Corollary (locally transitive boundary tournaments).** If the comparison tournament at each middle vertex of a reversal-odd boundary \(3\)-tournament is transitive, there is a monochromatic vertex-simple tight path with at least \(1+(\sqrt{4n-3}-1)/2\) vertices. Use \(G=K_n\), \(N=M(K_n)\), and \(d=n-1\). The local orders may be mutually inconsistent.

**Interpolation.** If every induced subtournament on \(q\) edges of any star has a vertex beating at least \(\alpha(q-1)\) others, \(1/2\le\alpha\le1\), the same proof gives \(d/2\le (L-1)+(L-1)(L-2)/(2\alpha)\), since \(\alpha(|U_r|-1)\le r-2\). It specializes to the arbitrary-tournament bound at \(\alpha=1/2\) and the theorem at \(\alpha=1\).

An \(n\)-edge one-switch geodesic in the antipodally odd cube would settle NORI1 by odd-change rotation; the result here supplies a longer partial path.
