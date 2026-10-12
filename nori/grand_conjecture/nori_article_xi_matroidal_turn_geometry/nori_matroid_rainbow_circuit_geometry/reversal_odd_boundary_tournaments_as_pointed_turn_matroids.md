# Reversal-odd boundary tournaments as pointed turn matroids

# Reversal-odd boundary tournaments as pointed turn matroids

Let \(V\) be a set of \(n\ge5\) vertices. An ordinary boundary 3-tournament is a function
\[
b:V_{\neq}^{3}\longrightarrow\mathbb F_2,\qquad
b(c,b_0,a)=1+b(a,b_0,c),
\tag{1}
\]
where \(V_{\neq}^{3}\) is the set of triples with pairwise distinct entries; \(b_0\) denotes the middle entry, to distinguish it from the function \(b\). The long-path witness is an injective word \(v_1,\ldots,v_m\) for which all \(m-2\) triple values \(b(v_i,v_{i+1},v_{i+2})\) agree.

**Proposition 1 (line-graph orientation).** Boundary 3-tournaments on \(V\) are in bijection with orientations of the ordinary line graph \(L(K_V)\). The edge between \(\{a,b_0\}\) and \(\{b_0,c\}\) is directed from the former to the latter precisely when \(b(a,b_0,c)=0\). A positive tight path corresponds to a directed walk through the successive vertices
\[
\{v_1,v_2\},\{v_2,v_3\},\ldots,\{v_{m-1},v_m\}
\tag{2}
\]
of \(L(K_V)\), with consecutive incidences alternating endpoints of their common \(K_V\)-edge and with the symbols \(v_i\) pairwise distinct.

*Proof.* Every edge of \(L(K_V)\) has a unique middle vertex \(b_0\) of \(K_V\), and is represented by a reversal pair \((a,b_0,c),(c,b_0,a)\). Equation (1) chooses one of the two orientations. Conversely every orientation makes this choice and defines the reversal-odd function. In (2), consecutive edges of \(L(K_V)\) represent the triples \((v_i,v_{i+1},v_{i+2})\). A zero value means the traversal follows the prescribed orientation. The incidence and injectivity conditions are precisely the conditions that this walk comes from an injective word of original vertices. \(\square\)

Define the **triple-overlap graph** \(\widetilde T_V\) to have vertex set \(V_{\neq}^3\), with an undirected edge between
\[
(a,b_0,c)\quad\text{and}\quad(b_0,c,d)
\tag{3}
\]
whenever \(a,b_0,c,d\) are pairwise distinct. Reversal \(J(a,b_0,c)=(c,b_0,a)\) is a fixed-point-free involution of \(\widetilde T_V\), and it maps the edge in (3) to the edge between \((d,c,b_0)\) and \((c,b_0,a)\). Put
\[
T_V=\widetilde T_V/\langle J\rangle,\qquad
\pi:\widetilde T_V\longrightarrow T_V.
\tag{4}
\]

**Lemma 2 (connected double cover).** For \(n\ge5\), \(\widetilde T_V\) and \(T_V\) are connected, and \(\pi\) is a regular two-sheeted graph covering. Their orders are
\[
|V(T_V)|=\frac{(n)_3}{2},\qquad
|E(T_V)|=\frac{(n)_4}{2},\qquad
\deg_{T_V}(x)=2(n-3),
\tag{5}
\]
where \((n)_r=n(n-1)\cdots(n-r+1)\).

*Proof.* A triple \((a,b_0,c)\) has \(n-3\) neighbors of the form \((b_0,c,d)\) and \(n-3\) of the form \((d,a,b_0)\). These are distinct, and no pair consists of reversals of one another: the middle two symbols of the starting triple are distinct. Thus the free involution also acts freely on edges and gives a graph covering; counting vertices and edges gives (5).

For connectivity, fix the middle symbol \(b_0\). Any first entry \(a\) can be changed to \(e\notin\{b_0,c\}\) through
\[
(a,b_0,c)\ --\ (b_0,c,d)\ --\ (e,b_0,c),
\tag{6}
\]
choosing \(d\notin\{a,b_0,c,e\}\), possible because \(n\ge5\). A symmetrical two-step walk changes the last entry while fixing the first and middle entries. These operations connect all ordered triples having the same middle symbol: the graph of ordered pairs of distinct elements of \(V\setminus\{b_0\}\), with changes of one entry, is connected. Finally (3) changes the middle symbol from \(b_0\) to any chosen \(c\ne b_0\) by selecting \(a,d\) distinct from the two. Hence \(\widetilde T_V\) is connected. \(\square\)

Let \(\alpha:Z_1(T_V;\mathbb F_2)\to\mathbb F_2\) denote the covering-monodromy functional: a closed walk has \(\alpha=0\) when its lift closes, and \(\alpha=1\) when its lift ends at the reversed triple. Choose any binary edge cochain \(a\in C^1(T_V;\mathbb F_2)\) representing \(\alpha\). Let \(B\) be the binary vertex-edge incidence matrix of \(T_V\), and introduce a distinguished element \(p\). Set
\[
\widehat A_V=
\begin{pmatrix}B&0\\a&1\end{pmatrix},
\qquad D_V^{\mathrm{BT}}=M(\widehat A_V)^*.
\tag{7}
\]
The pointed binary matroid depends only on \(V\) and the overlap/reversal structure, independently of a tournament coloring.

**Theorem 3 (boundary tournament–port-cycle correspondence).** A boundary tournament \(b\) defines a turn cochain on \(T_V\) by
\[
d_b(\pi\{t,s\})=b(t)+b(s).
\tag{8}
\]
It obeys
\[
\boxed{d_b=a+\delta f,\qquad f\in C^0(T_V;\mathbb F_2),}
\tag{9}
\]
and the binary cycles of \(D_V^{\mathrm{BT}}\) containing \(p\) are precisely
\[
\boxed{X_b=\operatorname{supp}(d_b)\cup\{p\}.}
\tag{10}
\]
Every port-containing binary cycle of \(D_V^{\mathrm{BT}}\) is of this form. The two boundary tournaments inducing a given port cycle are complementary: \(b\) and \(1+b\). Furthermore,
\[
\boxed{
\mathcal C^*(D_V^{\mathrm{BT}})\cap\{Y:p\in Y\}
=\{\,C\cup\{p\}: C\subseteq T_V\text{ a simple cycle with }\alpha(C)=1\,\}.
}
\tag{11}
\]
For such a cocircuit and a port cycle,
\[
\boxed{|X_b\cap(C\cup\{p\})|=1+|\operatorname{supp}(d_b)\cap C|
\quad\text{is a positive even integer}.}
\tag{12}
\]

*Proof.* Because \(b(Jt)=b(t)+1\), the sum \(b(t)+b(s)\) is unchanged on applying \(J\) to an overlap edge, so (8) is well-defined. Lift a closed walk \(C\) of \(T_V\), starting at \(t\). Telescoping (8) along the lift gives \(d_b(C)=b(t)+b(J^{\alpha(C)}t)=\alpha(C)\). Since \(a\) represents the same functional on cycles, \(d_b+a\) annihilates every graphic cycle. The cut-cycle orthogonality of a connected graph implies \(d_b+a=\delta f\).

Conversely any cochain \(d=a+\delta f\) pulls back to a coboundary on the connected graph \(\widetilde T_V\), since its sum on every lifted closed cycle vanishes. Integrate from one triple \(t_0\) to obtain \(b\). Because the covering involution preserves the pullback cochain, \(b(Jt)+b(t)\) is constant on the connected covering graph; evaluating on an odd-monodromy lifted walk gives the constant one. Thus (1) holds. The integration is unique up to a global constant, producing the two complementary colorings.

The row space of (7) is the binary cycle space of its dual and consists of \((\delta f,0)\) and \((a+\delta f,1)\), proving (10). A port-containing circuit of \(M(\widehat A_V)\), equivalently a port-containing cocircuit of \(D_V^{\mathrm{BT}}\), has a graphic Eulerian part with monodromy one. Its minimality forces this part to be a single simple odd-monodromy cycle, proving (11). Finally \(d_b(C)=\alpha(C)=1\), so its integer support weight on \(C\) is odd; adjoining the common port proves (12). \(\square\)

Since \(|V(T_V)|=(n)_3/2\) and \(|E(T_V)|=(n)_4/2\), the dual matroid has rank
\[
\operatorname{rank}D_V^{\mathrm{BT}}
=\frac{(n)_4-(n)_3}{2}+1.
\tag{13}
\]

**Theorem 4 (tight-path decoding).** Let \(3\le m\le n\). For an injective word \(v=(v_1,\ldots,v_m)\), define the forward overlap path \(\gamma_v\) in \(\widetilde T_V\) through
\[
t_i=(v_i,v_{i+1},v_{i+2}),\qquad 1\le i\le m-2,
\tag{14}
\]
and let \(\pi\gamma_v\) denote its projected path in \(T_V\). Then
\[
\boxed{
\sum_{i=1}^{m-3}
[b(v_i,v_{i+1},v_{i+2})\ne b(v_{i+1},v_{i+2},v_{i+3})]
=|\operatorname{supp}(d_b)\cap E(\pi\gamma_v)|.
}
\tag{15}
\]
Consequently \(b\) has a vertex-simple monochromatic tight path on \(m\) original vertices if and only if
\[
\boxed{
\min_{\substack{v_1,\ldots,v_m\in V\\\text{pairwise distinct}}}
|X_b\cap E(\pi\gamma_v)|=0.
}
\tag{16}
\]
The same condition characterizes the existence of a positive tight path, since reversing an injective word complements and reverses its color word.

*Proof.* Each edge of \(\gamma_v\) is the overlap of the consecutive triples in (14). By (8), it is labeled one precisely when their colors differ. Pairwise distinct symbols imply that the projected vertices and edges of \(\gamma_v\) are not repeated, so the right side of (15) counts each transition once. Vanishing means the triple-color word is constant, proving (16). The reversal identity (1) changes a constant-one word into a constant-zero word. \(\square\)

**Proposition 5 (bounded odd-girth).** For every \(n\ge5\), the least size of a port-containing cocircuit of \(D_V^{\mathrm{BT}}\) is seven. Equivalently, the least length of a cycle of \(T_V\) with monodromy one is six.

*Proof.* Choose five distinct symbols \(a,b_0,c,d,e\). The following is a six-edge path in \(\widetilde T_V\):
\[
\begin{split}
(a,b_0,c)&\;--\;(b_0,c,e)\;--\;(d,b_0,c)\;--\;(e,d,b_0)\\
&\;--\;(d,b_0,a)\;--\;(b_0,a,e)\;--\;(c,b_0,a).
\end{split}
\tag{17}
\]
Its endpoints are reversals, and its six intermediate reversal-orbits are distinct. Its projection is therefore a simple six-cycle with monodromy one.

To verify minimality uniformly in \(n\), a path of length at most five from a triple to its reverse uses at most eight symbols: each overlap step retains two existing symbols and introduces at most one. Relabel those symbols into \(\{0,\ldots,7\}\). It is enough to verify in the graph on the \(336\) ordered triples of eight symbols that \((2,1,0)\) lies outside the radius-five ball around \((0,1,2)\). The following exhaustive finite check uses precisely the adjacency definition (3):
\[
\begin{array}{l}
R=\{(0,1,2)\};\\
\text{repeat five times: }\;
R\leftarrow R\cup\bigcup_{(a,b_0,c)\in R}
\{(b_0,c,d),(d,a,b_0):d\notin\{a,b_0,c\}\};\\
(2,1,0)\notin R.
\end{array}
\tag{18}
\]
For reproducibility, the respective distance-layer cardinalities through radius five are \(1,10,55,162,97,10\); a sixth step reaches the reversed triple. This computation covers every possible path of length at most five in any order \(n\), because of the eight-symbol cutoff. Thus the least odd-monodromy cycle has length six, and (11) gives cocircuit size seven. \(\square\)

**Witness distinction.** In the cube case of Article XI, shortest odd-monodromy cycles themselves encode full antipodal geodesics. In the boundary-tournament matroid, port cocircuits of size seven exist uniformly in \(n\), while the long-path target in (16) is a *forward*, symbol-injective overlap path that need not be closed. Accordingly (16) is the pertinent cycle–path zero-intersection problem; the short port cocircuits of (11) encode local reversal monodromy and do not themselves encode long tight paths. This distinction also records both endpoint-seam constraints implicitly in the ordered overlap path: concatenations must preserve directed pair overlaps and the injectivity of the underlying word.
