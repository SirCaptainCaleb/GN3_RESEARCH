# Tournament winner coloring: linear rainbow paths require linear binary switches

- Stable ID: note_tournament_winner_coloring_log_switch_obstruction
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: counterexample, obstruction, minimum-color-degree, switch-count
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7379_1
- Updated session: session_nori_r7379_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (unbounded minimum color degree with short bounded-switch rainbow paths).** For every integer \(m\ge1\) there is a connected simple graph \(G_m\), an ordinary edge coloring \(\lambda\), a binary edge labeling \(\chi\), and a vertex involution \(\tau\) with
\[
\lambda(\tau e)=\lambda(e),\qquad\chi(\tau e)=1-\chi(e),
\]
such that \(\delta(G_m)=2m\), \(\hat\delta(G_m,\lambda)=m+1\), but every vertex-simple rainbow path \(P\) satisfies
\[
|E(P)|\le 2(\operatorname{sw}_\chi(P)+1).
\]
Thus neither a positive linear-in-\(\hat\delta\) rainbow-path bound with \(O(\log\hat\delta)\) switches nor any \(o(\hat\delta)\) switch budget can guarantee linear length in the class of Article XIII.

**Construction and proof.** Put \(n=2m+1\) and choose a regular tournament \(T\) on \([n]\). Take a bipartite graph with vertices \(L_i,R_i\) for \(i\in[n]\), and all edges \(L_iR_j\) for \(i\ne j\) (the complete bipartite graph minus the index-matching). Define \(\tau(L_i)=R_i\) and \(\tau(R_i)=L_i\). For edge \(L_iR_j\), if \(i\to j\) in \(T\), assign \(\lambda=i\), \(\chi=0\); otherwise \(j\to i\), assign \(\lambda=j\), \(\chi=1\). The image of \(L_iR_j\) under \(\tau\) is \(L_jR_i\), which has the same winner and opposite binary bit. Since \(n\ge3\), the graph is connected, and every vertex has degree \(n-1=2m\). At vertex \(L_i\), the \(m\) tournament victories of \(i\) all contribute color \(i\), while its \(m\) defeats contribute \(m\) different winning-opponent colors. Thus the color degree is \(m+1\); symmetry gives the same value at \(R_i\).

Every \(\chi=0\) edge incident to \(L_i\) has ordinary color \(i\), and every \(\chi=1\) edge incident to \(R_i\) has ordinary color \(i\). A constant-\(0\) run of three consecutive edges in a bipartite path contains an internal \(L\)-vertex with two equal ordinary colors, and a constant-\(1\) run similarly contains an internal \(R\)-vertex. Neither can occur in a rainbow path. Therefore every maximal constant-bit run has at most two edges. A path with \(s\) binary switches has \(s+1\) runs, proving the bound.

This construction isolates the lack of local properness: it need not obstruct unrelated restricted classes with additional path-coherence structure.
