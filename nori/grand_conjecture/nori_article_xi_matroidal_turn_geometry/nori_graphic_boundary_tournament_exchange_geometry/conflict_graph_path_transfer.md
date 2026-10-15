# Conflict graph path transfer

# Conflict-graph purification and robust transfer of monotone paths

Let \(V\) be an \(n\)-element set, \(n\ge3\). A *boundary coloring* is a map \(b:V_{\ne}^3\to\{0,1\}\) satisfying \(b(c,v,a)=1-b(a,v,c)\). Let \(\prec\) be a total ordering of \(E(K_V)\), and let
\[
b_\prec(a,v,c)=\mathbf 1_{\{av\prec vc\}}.
\]
Reversing a triple complements this value. Denote by
\[
m=m(b,\prec)=\bigl|\{\{(a,v,c),(c,v,a)\}:b(a,v,c)\ne b_\prec(a,v,c)\}\bigr|
\]
the number of erroneous reversal classes of ordered triples. Every such class represents an unordered pair of incident edges of \(K_V\).

**Theorem 1 (conflict-graph purification).** There is a spanning graph \(G\subseteq K_V\) satisfying
\[
\boxed{\quad
\frac{2|E(G)|}{n}\ \ge\
d_{n,m}:=\frac{n-1}{1+\frac{4m}{n(n-1)}} ,
\quad} \tag{1}
\]
such that for every ordered triple \((a,v,c)\) of distinct vertices with \(av,vc\in E(G)\),
\[
\boxed{b(a,v,c)=b_\prec(a,v,c).} \tag{2}
\]
Consequently, every path of strictly increasing edge labels in \(G\) is a vertex-simple monochromatic tight path of color \(1\) in \(b\). The same holds for decreasing edge labels, of color \(0\).

*Proof.* Form the conflict graph \(J\) with vertex set \(E(K_V)\). Join two vertices \(av,vc\in E(K_V)\) whenever their comparison is erroneous, namely when \(b(a,v,c)\ne b_\prec(a,v,c)\). The reversal identity makes this condition independent of ordering the pair. Thus
\[
|V(J)|=Q:=\binom n2,\qquad |E(J)|=m.
\]
For any finite graph \(J\), its independence number satisfies the Caro–Wei bound
\[
\alpha(J)\ge\sum_{e\in V(J)}\frac{1}{1+\deg_J(e)}
\ge\frac{Q^2}{Q+2m}. \tag{3}
\]
For completeness, randomly order \(V(J)\) and retain each vertex earlier than all its neighbors; the retained vertices are pairwise nonadjacent, and each is retained with probability \(1/(1+\deg_J(e))\). Taking expectations proves the first inequality; Cauchy–Schwarz proves the second.

Choose an independent vertex set \(F\subseteq V(J)\) attaining the lower bound (3), and take \(G=(V,F)\). Independence states precisely that no two incident edges of \(G\) give an erroneous triple, proving (2). Since \(Q=n(n-1)/2\), the lower bound (3) gives
\[
\frac{2|F|}{n}\ge\frac{2Q^2}{n(Q+2m)}
=\frac{n-1}{1+4m/[n(n-1)]},
\]
which proves (1). For a strictly increasing path \(v_0v_1\cdots v_\ell\) in \(G\), every consecutive pair of its edges has the comparison color \(1\) in \(b_\prec\), hence by (2) in \(b\). Since it is a graph path, the vertices are distinct. \(\square\)

Define the *altitude* \(f(G)\) to be the minimum, over all total orders of \(E(G)\), of the greatest length in edges of an increasing vertex-simple path. Then Theorem 1 immediately gives \(L(b)\ge f(G)\), where \(L(b)\) is the maximum number of edges in a monochromatic vertex-simple tight path. To quantify this, use the published theorem of Bucić, Kwan, Pokrovskiy, Sudakov, Tran and Wagner, *Nearly-linear monotone paths in edge-ordered graphs*, Israel J. Math. **238** (2020), 663–685, Theorem 1.2: for an \(n\)-vertex graph of average degree \(d\ge2\),
\[
f(G)\ge \frac{d}{2^{C\sqrt{\log_2 d\,\log_2\log_2 n}}} \tag{4}
\]
for an absolute constant \(C\). The classical lower bound of Rödl gives \(f(G)\ge c\sqrt d\) for a universal \(c>0\).

**Corollary 2 (robust monotone-path transfer).** Let \(d_{n,m}\) be given by (1). Whenever \(d_{n,m}\ge2\),
\[
\boxed{
L(b)\ge \max\left\{
c\sqrt{d_{n,m}},
\ \frac{d_{n,m}}{2^{C\sqrt{\log_2 d_{n,m}\,\log_2\log_2 n}}}
\right\}.} \tag{5}
\]
In particular, as \(n\to\infty\):

(a) If \(m=o(n^2)\), then \(L(b)\ge n^{1-o(1)}\).

(b) If \(m=O(n^{2+\delta})\) for fixed \(0<\delta<1\), then \(L(b)\ge n^{1-\delta-o(1)}\).

(c) If \(m=o(n^3)\), then \(L(b)\to\infty\), quantitatively \(L(b)=\Omega(\sqrt{\min\{n,n^3/m\}})\) when \(m>0\). In the equivalent normalized notation \(m=\eta n^3\), this is \(\Omega(\min\{\sqrt n,\eta^{-1/2}\})\). The zero-error case is covered by (a).

*Proof.* Both bounds of (5) apply to the purified graph from Theorem 1; each increasing path transfers by (2). Under (a), \(d_{n,m}=n(1-o(1))\). Under (b), \(d_{n,m}=\Omega(n^{1-\delta})\). The denominator of the second expression of (5) is \(n^{o(1)}\) whenever \(d_{n,m}\) is a positive power of \(n\), proving (a) and (b). Under (c), (1) implies \(d_{n,m}=\Omega(\min\{n,n^3/m\})\to\infty\), and the first expression in (5) applies. \(\square\)

**Corollary 3 (spectrally near-extremal boundary colorings).** Suppose \(b\) has legal-turn disagreement density \(D(b)/E_n\), and put
\[
z=\max\{0,2/3-D(b)/E_n\}+\frac{n-2}{2(n-3)(n-1)}.
\]
The preceding edge-order synchronization theorem supplies an ordering \(\prec\) for which
\[
m(b,\prec)\le C_0 n(n-1)(n-2)z^{1/9}
\]
for an absolute constant \(C_0\). Applying Theorem 1 gives a comparison-faithful graph of average degree at least
\[
\boxed{d\ge\frac{n-1}{1+4C_0(n-2)z^{1/9}}.} \tag{6}
\]
Corollary 2 now applies with this lower bound. In particular, a polynomially small synchronization error \(m=O(n^{2+\delta})\) yields a monochromatic path of length \(n^{1-\delta-o(1)}\).

The case \(m=o(n^3)\) gives an unbounded path but does not itself imply a path of length \(n^{1-o(1)}\). A stronger transfer would have to exploit path-wise avoidance of errors while retaining many adjacent edges of the ordered complete graph. The conflict-free subgraph in Theorem 1 is a graph-theoretic comparison certificate; the path's original-vertex simplicity is preserved by its graphic-matroid independence.
