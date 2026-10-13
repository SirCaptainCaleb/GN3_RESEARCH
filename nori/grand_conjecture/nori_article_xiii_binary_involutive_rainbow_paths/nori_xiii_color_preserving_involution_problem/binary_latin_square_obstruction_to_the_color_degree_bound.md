# Binary Latin-square obstruction to the color-degree bound

### An infinite family of rainbow-path obstructions

**Lemma.** Let \(\tau\) be an involutive vertex automorphism of a graph \(G\). There exists a binary edge labeling \(\chi\) satisfying \(\chi(\tau e)=1-\chi(e)\) for all \(e\in E(G)\) if and only if \(\tau\) fixes no edge setwise.

**Proof.** A fixed edge would require \(\chi(e)=1-\chi(e)\). Conversely, when \(\tau\) acts without fixed edges, its edge orbits have size two. Label the two edges in each orbit \(0\) and \(1\). \(\square\)

**Theorem (binary Latin-square obstruction).** For every integer \(d\ge2\) there is a connected simple graph with a proper edge coloring \(\lambda\), binary edge labeling \(\chi\), and involutive automorphism \(\tau\) satisfying
\[
\lambda(\tau e)=\lambda(e),\qquad \chi(\tau e)=1-\chi(e),
\]
whose minimum color degree is \(2^d\), yet which has no rainbow path of length \(2^d\). In particular, Conjecture XIII.1 fails even if its condition on the number of \(\chi\)-changes is omitted.

**Proof.** Put \(A=\mathbb F_2^d\), \(q=|A|=2^d\), and let \(G=K_{q,q}\) have bipartition \(\{L_x:x\in A\}\) and \(\{R_y:y\in A\}\). Define
\[
\lambda(L_xR_y)=x+y.
\]
At every vertex the \(q\) incident edges receive all elements of \(A\) as distinct colors, so \(\hat\delta(G,\lambda)=q\).

Choose a nonzero \(t\in A\) and a linear functional \(h:A\to\mathbb F_2\) with \(h(t)=1\). Define
\[
\tau(L_x)=L_{x+t},\quad \tau(R_y)=R_{y+t},\qquad
\chi(L_xR_y)=h(x).
\]
Translation by \(t\) is an involutive automorphism. For every edge,
\[
\lambda(L_{x+t}R_{y+t})=x+y+2t=x+y,\qquad
\chi(L_{x+t}R_{y+t})=h(x)+1.
\]
Thus all the stipulated symmetries hold.

Suppose \(v_0v_1\cdots v_q\) were a rainbow path with \(q\) edges. Writing \(a(v)\in A\) for the index of either \(L_x\) or \(R_x\), we obtain
\[
a(v_0)+a(v_q)
=\sum_{i=1}^{q}\bigl(a(v_{i-1})+a(v_i)\bigr)
=\sum_{i=1}^{q}\lambda(v_{i-1}v_i)
=\sum_{x\in A}x=0.
\]
The last equality holds because \(d\ge2\). Hence the endpoints have equal indices. Since \(q\) is even, they lie in the same part of \(G\), and consequently \(v_0=v_q\), contrary to vertex-simplicity. There are only \(q\) colors in the graph, so a longer rainbow path is also impossible. \(\square\)

**Remark.** This obstruction distinguishes paths from cycles. When \(d=2\), choose a nonzero \(a\in\ker h\). The cycle
\[
L_0R_0L_aR_tL_0
\]
has colors \(0,a,a+t,t\), all distinct, and all four edges have \(\chi\)-label \(0\). Thus allowing rainbow cycles removes the obstruction in this four-color example.
