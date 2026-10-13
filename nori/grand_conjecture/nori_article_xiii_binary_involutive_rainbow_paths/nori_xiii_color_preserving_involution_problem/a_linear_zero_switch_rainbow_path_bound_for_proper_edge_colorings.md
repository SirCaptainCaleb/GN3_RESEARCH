# A linear zero-switch rainbow path bound for proper edge colorings

### Linear zero-switch paths for proper edge colorings

**Theorem.** Let \(G\) be a finite simple graph with a proper edge coloring \(\lambda\) and minimum degree \(k\geq 1\). For every binary edge labeling \(\chi:E(G)\to\{0,1\}\), there is a vertex-simple \(\lambda\)-rainbow path of at least \(k/8\) edges whose edges share the same \(\chi\)-label.

**Proof.** Write \(n=|V(G)|\), \(m=|E(G)|\). For some \(b\in\{0,1\}\), the spanning subgraph \(H\) comprising the edges with \(\chi=b\) has at least \(m/2\) edges, hence average degree
\[
D=\frac{2|E(H)|}{n}\geq \frac mn=\frac{\overline d(G)}2\geq \frac k2.
\]
There is a nonempty subgraph \(J\subseteq H\) of minimum degree at least \(D/2\). Indeed, if none existed, iterative deletion of vertices of current degree strictly less than \(D/2\) could delete the entire graph, removing fewer than \(nD/2=|E(H)|\) edges in total, an impossibility. Therefore \(\delta(J)\geq k/4\).

Let \(P=v_0v_1\ldots v_\ell\) be a longest vertex-simple \(\lambda\)-rainbow path in \(J\). At most \(\ell\) edges at the terminal vertex \(v_\ell\) lead to earlier vertices of \(P\). Among its edges to vertices outside \(P\), at most \(\ell\) carry colors used by \(P\), since the coloring is proper. Thus \(\deg_J(v_\ell)\leq 2\ell\), since otherwise \(P\) extends by an edge to a new vertex of a new color. Consequently
\[
\ell\geq\frac{\delta(J)}2\geq \frac k8.
\]
Every edge of \(J\) has binary label \(b\), so \(P\) has zero binary-label changes. \(\square\)

The bound requires no symmetry hypothesis on \(\lambda\) or \(\chi\); it also applies when an involutive vertex automorphism reverses \(\chi\) and changes ordinary edge colors.
