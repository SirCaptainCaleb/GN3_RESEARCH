# Article VII — Seven-coordinate structural and tournament methods

## Article setting and orientation

The target boundary-tournament problem concerns *every* ordinary reversal-odd ordered-triple orientation, without assuming that its incident-edge comparisons extend to one global total order of E(K_n). Such an order exists precisely when the comparison orientation of L(K_n) is acyclic; the edge-ordered subclass is an explicit fallback, never a substitute for the full target. NORI1's full class of arbitrary antipodally odd physical cube-edge colorings is the other equally primary research objective.

The current Section establishes genuine mathematical theorems about seven-direction endpoint and wing factorizations, admissible physical boundary-compatible three-face families, and edge-ordered/ac\-yclic boundary-tournament increasing paths under their precise hypotheses. Its chronological-saddle construction equates a full alternating increasing Hamilton path with adjacent-exchange extremality for a triangular edge-rank potential, and derives chain-prefix/minimax connector criteria. The full-class path/defect reduction measures the effect of bad ordered-triple windows on extracted monochromatic vertex-simple paths. These are useful affirmative structural statements, not a proof of the unrestricted conjecture.

*Full Article composition: [source manuscript](../nori_article_vii_seven_coordinate.md).*

## Seven-coordinate endpoint constraints and tournament structure

Two mathematical objectives must remain distinct: a long vertex-simple monochromatic tight path in every ordinary boundary 3-tournament, and unrestricted antipodally odd physical-edge NORI1 closure. A boundary 3-tournament assigns b(a,b,c) to each ordered triple of distinct original vertices with reversal oddness b(c,b,a)=1−b(a,b,c). No global edge order is assumed. Edge-order-realizable tournaments, characterized by an acyclic orientation of the line graph L(K_n), are a strict and useful fallback, not the full theorem.

The surviving Subsections develop exact seven-direction endpoint pivots and wing factorizations, boundary-tour\-nament monochromatic orders under stated additional hypotheses, physical sparse-exterior transfers, and positive generically full geodesic existence for restricted classes. The strongest chronological-saddle manuscript establishes an exact coupling of an alternating increasing Hamilton path with extremization of a triangular edge-rank potential; its threshold-chain and hereditary minimax connector lemmas and full-class path/defect reduction remain published. These statements retain original-vertex simplicity and state exactly where acyclic comparisons or exterior-bit restrictions enter.

*Full Section composition: [source manuscript](nori_seven_coordinate_structure.md).*

### Seven-coordinate shared-pivot endpoint constraints

## Endpoint pivots for ordered-face galleries

Let \(k\ge2\), and let \(c(F,\pi)\in\{0,1\}\) color ordered \(k\)-faces of a Boolean cube, independently of the traversal corner. On a geodesic segment with distinct direction order \(p_1,\ldots,p_m\), let \(w_i\) be its \(i\)-th consecutive ordered-\(k\)-face color. Fix all starting bits except those specified below.

**Theorem (endpoint-pivot dichotomy).** If \(m=2k\), varying \(u=x_{p_{k+1}}\) and \(v=x_{p_k}\) independently produces
\[
(w_1,\ldots,w_{k+1})=(A(u),M_1,\ldots,M_{k-1},E(v)).
\]
If \(m=2k+1\), varying the single bit \(t=x_{p_{k+1}}\) produces
\[
(w_1,\ldots,w_{k+2})=(A(t),M_1,\ldots,M_k,E(t)).
\]
In both formulas the interior colors \(M_i\) are independent of the varied bits.

**Proof.** A window is insensitive to the starting bits of its free directions, because these bits do not identify its underlying ordered face. For \(m=2k\), the free sets of windows \(2,\ldots,k\) have intersection \(\{p_k,p_{k+1}\}\). The first window contains \(p_k\) but excludes \(p_{k+1}\), while the last contains \(p_{k+1}\) but excludes \(p_k\). Hence the two pivots can affect only the respective endpoint colors. For \(m=2k+1\), the intersection of the free sets of windows \(2,\ldots,k+1\) is the singleton \(\{p_{k+1}\}\), and neither endpoint window contains it. \(\square\)

**Corollary (exact one-change criterion).** Let \(M=(M_1,\ldots,M_s)\) be the invariant middle word, and put \(q=\sum_{i=1}^{s-1}[M_i\ne M_{i+1}]\). A pivot choice achieves at most one change precisely when
\[
q+[A\ne M_1]+[E\ne M_s]\le1.
\]
In the shared-pivot case \(m=2k+1\), if \(q=0\) and neither \(t\) works, then \(A(0)=A(1)=E(0)=E(1)=1-M_1\). If \(q=1\) and both endpoint functions toggle with \(t\), neither choice works precisely when
\[
A(0)\oplus E(0)\ne M_1\oplus M_k.
\]

**Proof.** The color changes partition into the \(q\) changes inside \(M\) and the two boundary comparisons. For \(q=0\), failure under both choices forces both boundaries to disagree in both cases. For \(q=1\), success demands simultaneous agreement at both boundaries. Two endpoint functions that each toggle give complementary endpoint pairs, so one is the required pair exactly when their common XOR equals the target XOR. \(\square\)

When \(k=3\), the two cases are the six-move independent endpoint square and the seven-move shared endpoint obstruction. The statements require no antipodal symmetry. In a seven-dimensional NORI counterexample, they constrain every five-move interior whose color word has at most one change; compatibility of those constraints across different orders remains unresolved.

### Seven-coordinate wing factorization and exact obstruction

# A seven-coordinate wing decomposition

Fix a binary coloring \(c\) of ordered three-faces of \(Q_7\). No antipodal symmetry is required in this subsection. Consider the complete direction order \(p=(a,b,c,d,e,f,g)\), and denote its consecutive window colors by \(w_1,\ldots,w_5\).

**Lemma 1 (two independently controlled wings).** Fix the initial bits at \(a,b,d,f,g\). With \(u=x_e\) and \(v=x_c\), there are Boolean functions \(A,B,D,E\) and a constant \(M\) such that
\[
(w_1,w_2,w_3,w_4,w_5)=(A(u),B(u),M,D(v),E(v)).
\]
Put
\[
\ell(u)=[A(u)\ne B(u)]+[B(u)\ne M],\qquad
r(v)=[M\ne D(v)]+[D(v)\ne E(v)].
\]
Among these four initial vertices a geodesic with at most one color change exists if and only if
\[
\min_{u\in\mathbb F_2}\ell(u)+\min_{v\in\mathbb F_2}r(v)\le1.
\]
If both wing maps \(u\mapsto(A(u),B(u))\) and \(v\mapsto(D(v),E(v))\) are nonconstant, all four starts fail precisely when neither wing assumes the pair \((M,M)\).

**Proof.** The successive free triples are \(abc,bcd,cde,def,efg\). Direction \(e\) is exterior exactly to the first two faces, while \(c\) is exterior exactly to the last two; both are free in the middle face. This proves the displayed separation. The total number of changes is \(\ell(u)+r(v)\), and the independent minimization is exact. The left wing cost equals zero exactly for \((M,M)\) and two exactly for \((M,1-M)\). The right wing cost equals zero exactly for \((M,M)\) and two exactly for \((1-M,M)\). A nonconstant two-point wing map cannot always equal its unique cost-two pair, so each minimum is at most one; their sum is at most one exactly when at least one is zero. \(\square\)

**Theorem 2 (crossed sensitivity and pivot rigidity).** Fix just the four initial bits at \(a,b,f,g\) and vary \(u=x_e\), \(v=x_c\), and \(t=x_d\). Then the color word has the form
\[
(P(u,t),L(u),M,R(v),S(v,t)).
\]
Suppose \(L\) and \(R\) are each nonconstant. Let \(u_*,v_*\) be their respective unique arguments with \(L(u_*)=R(v_*)=M\). If either \(t\mapsto P(u_*,t)\) or \(t\mapsto S(v_*,t)\) is nonconstant, then a full antipodal geodesic in direction order \(p\) has at most one color change. More generally, failure for every one of the eight \((u,v,t)\) forces
\[
P(u_*,0)=P(u_*,1)=S(v_*,0)=S(v_*,1)=1-M.
\]

**Proof.** In addition to the dependencies proved above, the coordinate \(d\) is free in each of the three middle faces and exterior to the first and fifth faces. Hence the stated three-variable factorization holds. Choosing \(u_*,v_*\) makes the word
\[
(P(u_*,t),M,M,M,S(v_*,t)).
\]
Such a word has at most one change whenever either endpoint equals \(M\). Consequently, if both choices of \(t\) fail, both endpoints must equal \(1-M\) for both values of \(t\). The sensitivity conclusion follows. \(\square\)

Theorems 1–2 are local conclusions for unrestricted face colorings. They give a precise necessary condition on every seven-coordinate order in a hypothetical NORI counterexample. To prove dimension-seven closure, one must additionally use the antipodal-reversal relations between *different* orders to contradict the stipulated endpoint rigidity, or find an order whose wing minima sum to at most one.

## Recent consequences and compatibility conditions

# Four-core flat bridge: generalized seven-dimensional one-flipper closure

Let \(B=A\sqcup M\), \(|A|=4\), \(M=\{u,v\}\), and \(V=B\sqcup\{g\}\). Let \(c\) be an antipodal-reversal-odd ordered-three-face coloring of \(Q_7\), and suppose \(g\) is a universal exterior flipper. Write \(c(F,\pi)=x_g(F)\oplus h(F_B,\pi)\) on every ordered face avoiding \(g\), where \(h\) is an induced, completely arbitrary ordered-three-face coloring of \(Q_B\), satisfying antipodal-reversal *evenness* by the symmetry transfer. No position independence is assumed for \(h\).

**Theorem (four-core flat-bridge closure).** Suppose the residual coloring \(h\) has both properties:

(T) **Uniform good tails on the four-core.** For every pairwise distinct \(a,b,c\in A\) and every \(B\)-starting vertex \(x\in Q_B\), there is a permutation \((d,e,f)\) of \(B\setminus\{a,b,c\}\) such that the last three window colors of the six-direction geodesic with order \((a,b,c,d,e,f)\) and start \(x\) have at most one change.

(F) **One universally flat four-core prefix.** There is some permutation \((a,b,c,d)\) of \(A\) such that for every \(B\)-starting vertex \(x\), the first and second window colors of the six-direction geodesic with order \((a,b,c,d,u,v)\) agree. Their common value \(\lambda(x)\) may depend arbitrarily on \(x\).

Then \(c\) admits a full seven-coordinate antipodal geodesic with at most one color change. All colors on faces containing \(g\) may depend arbitrarily on their four fixed exterior bits.

**Proof.** Suppose every full \(Q_7\) geodesic has at least two changes.

First, the exact universal-flipper lifting lemma implies that every six-direction geodesic of \(h\) has at least two changes: a one-change residual geodesic would lift to a good full geodesic.

For distinct \(a,b,c\in A\), apply (T) and consider the full order \((a,g,b,c,d,e,f)\), with \((d,e,f)\) a good-tail completion. The first two window colors \(P=c(a,g,b)\) and \(Q=c(g,b,c)\), at the reached face positions, are independent of the initial \(g\)-bit. The last three windows avoid \(g\), so toggling that starting bit complements all three simultaneously, preserving their at-most-one changes. We may arrange for the third color to agree with \(Q\). Global failure therefore forces \(P\ne Q\) for every assignment of starting \(B\)-bits, every distinct \(a,b,c\in A\), and whichever completion (T) supplies.

For fixed \(a,b\), vary the initial bit \(x_c\): the \((g,b,c)\)-face has direction \(c\) free, so its color is independent of \(x_c\); the forced inequality implies the \((a,g,b)\)-color is also independent of \(x_c\). Taking both choices \(c\in A\setminus\{a,b\}\) shows that \((a,g,b)\) depends on no exterior \(A\)-bits. Write its value \(F_{ab}(m)\), where \(m=(x_u,x_v)\). Dually, varying \(a\in A\setminus\{b,c\}\) shows that \((g,b,c)\) depends on no exterior \(A\)-bits; write it \(G_{bc}(m)\). Thus
\[
F_{ab}(m)=1\oplus G_{bc}(m)\qquad(a,b,c\in A\text{ distinct}).
\tag{1}
\]
As \(|A|=4\), comparison through a common third direction shows that \(F_{ab}(m)=K_b(m)\) is independent of \(a\), and \(G_{bc}(m)=1\oplus K_b(m)\) is independent of \(c\). Applying oddness to the reversal of the \((a,g,b)\)-face gives
\[
K_a(\bar m)=1\oplus K_b(m)\quad(a\ne b).
\]
Comparing three distinct indices in \(A\) forces a common function \(K\) for all subscripts, with
\[
K(\bar m)=1\oplus K(m).
\tag{2}
\]
Hence, at the relevant face positions and for any distinct \(r,s\in A\),
\[
c(r,g,s)=K(m),\quad c(g,r,s)=1\oplus K(m),\quad c(r,s,g)=1\oplus K(m).
\tag{3}
\]
The final identity follows by antipodal reversal and (2). In all three formulas \(m\) is the marked exterior-bit pair *at that face*. These bits have not been traversed in any of the subsequent paths using (3).

Now choose the four-core order \((a,b,c,d)\) provided by (F), and fix arbitrary initial \(B\)-bits \(x\). Denote the common first-two residual colors in the order \((a,b,c,d,u,v)\) by \(\lambda(x)\). Because every complete residual \(h\)-geodesic is bad, its four-color word must be
\[
(\lambda,\lambda,1\oplus\lambda,\lambda);
\tag{4}
\]
indeed, when the first two entries agree, at least two changes require both remaining comparisons to change. Therefore the residual color of its final \((d,u,v)\)-window equals \(\lambda(x)\). The same holds for the complete residual order \((a,b,c,d,v,u)\): its first two window faces and their positions are unchanged, so its final \((d,v,u)\)-color also equals \(\lambda(x)\).

Consider next the full \(Q_7\) order
\[
(a,b,c,g,d,u,v).
\]
Its five-window word, with \(z=x_g\), is
\[
\bigl(z\oplus\lambda,\;1\oplus K(m),\;K(m),\;T_u,\;(1\oplus z)\oplus\lambda\bigr),
\tag{5}
\]
where \(T_u\) denotes the color of the fourth ordered face \((g,d,u)\), reached after the first three \(A\)-moves and the \(g\)-move. Formula (4) justifies the final entry of (5): the \(B\)-face \((d,u,v)\) is reached after precisely the same \(a,b,c\)-moves in both the residual path and the full path.

Choose \(z=1\oplus K(m)\oplus\lambda\). Then (5) becomes
\[
(1\oplus K,\;1\oplus K,\;K,\;T_u,\;K).
\tag{6}
\]
If \(T_u=K(m)\), the word has exactly one change. Thus global failure forces \(T_u=1\oplus K(m)\) for every \(x\). Since \(u\) is *free* in \((g,d,u)\), changing the initial bit \(x_u\) leaves \(T_u\) unchanged, and all the other exterior face bits are unchanged. Therefore \(K(x_u,x_v)\) is independent of \(x_u\).

Repeating the same argument with the order \((a,b,c,g,d,v,u)\), using the second consequence of (4), forces \(K(x_u,x_v)\) independent of \(x_v\). Thus \(K\) is constant, contradicting (2). This proves closure. \(\square\)

**Scope and significance.** Conditions (T) and (F) are structural hypotheses on the six-dimensional reversal-even residual. The theorem tolerates arbitrary nonlinear dependence on all exterior bits in that residual, provided (T) and (F) hold, and *complete* arbitrary dependence on exterior bits for every \(g\)-containing face. It strengthens the earlier prescribed sparse two-mark template: that template has a four-core \(A\) with its AAA-prefix colors both zero, and the explicit marked-tail pattern makes (T) hold. In an unresolved one-flipper counterexample, for every four-set \(A\) satisfying (T), **every** permutation of \(A\) must have at least one residual start whose two first-window colors differ; otherwise (F) would hold and the counterexample would collapse. This leaves an explicit residual dichotomy to attack.

# One universal flipper with coordinate-only residual: full Q7 closure

Let \(V=B\sqcup\{g\}\), \(|B|=6\), and let \(c\) be an antipodal-reversal-odd binary coloring of ordered three-faces of \(Q_7\). Assume

1. \(g\) is a universal exterior flipper: complementing the fixed \(g\)-bit complements the color whenever the free triple avoids \(g\).
2. The induced six-coordinate residual on faces avoiding \(g\) is *position-independent*: for some ternary label \(H\),
\[
c(F,(a,b,d))=x_g(F)\oplus H(a,b,d)
\qquad(a,b,d\in B\text{ pairwise distinct}).
\]

There is **no restriction** on colors of ordered faces *containing* \(g\), beyond the global antipodal-reversal oddness condition. Those colors may be arbitrary functions of their four fixed exterior face bits.

**Theorem.** Every such \(c\) admits a full seven-coordinate antipodal geodesic with at most one color change.

**Proof.** For a free triple avoiding \(g\), antipodal complementation toggles \(x_g(F)\), and reversal of its ordered triple toggles the full \(c\)-color by oddness. Cancelling these two toggles gives
\[
H(d,b,a)=H(a,b,d),
\]
so the residual \(H\) is reversal-even.

If the six-direction residual \(H\) has a complete direction order with at most one color change, the exact universal-flipper lifting theorem applies: choose that \(B\)-order and place \(g\) first, selecting its starting bit so that the new first seam contributes zero changes. This yields a good full \(Q_7\) geodesic.

Otherwise *every* complete six-direction order of \(H\) has at least two changes. The exact finite classification in Item nori_reversal_even_coordinate_triple_q6_exact_classification_20261008 now forces
\[
H(a,b,d)=\varepsilon\oplus
\mathbf1_{\{b\notin M,\ \{a,d\}\cap M\ne\varnothing\}}
\]
for some marked two-set \(M\subset B\) and a global bit \(\varepsilon\). Complementing *all* colors of \(c\), if needed, removes \(\varepsilon\) without changing the NORI oddness axiom or the number of changes along any path.

Thus \(B\) splits into four unmarked and two marked directions, and the \(g\)-free face colors satisfy exactly the prescribed sparse two-mark template (AAA=0, AAM=MAA=1, AMM=MMA=0). The already proved *sparse-template seven-dimensional forcing theorem*, Item nori_sparse_two_mark_template_seven, applies even when all \(g\)-containing faces have arbitrary exterior dependence. It produces a good full seven-direction geodesic. Undo the global color complement if one was made. \(\square\)

**All-dimensional extension (six-coordinate residual).** Let \(c\) be an antipodal-reversal-odd coloring of \(Q_n\) with a set \(A\) of universal exterior flippers, leaving exactly six other directions \(B\). Suppose its induced ordered-three-face coloring on \(B\) is position-independent. Then \(c\) admits a one-change full antipodal geodesic in *every* dimension \(n\ge6\).

Indeed, write \(r=|A|\). If \(r\) is even, the symmetry-transfer theorem makes the six-coordinate residual antipodal-reversal odd, and the established full \(Q_6\) NORI closure lifts through the \(r\) flippers. If \(r\) is odd, choose a single flipper \(g\) and strip off the remaining \(r-1\) flippers, an even number; the seven-dimensional induced coloring is antipodal-reversal odd and has a universal \(g\)-flipper and the same position-independent six-coordinate residual. Apply the preceding \(Q_7\) theorem, then lift through the \(r-1\) stripped flippers by exact backward elimination.

**Research frontier.** The odd-flipper six-residual case has now been solved whenever the residual is position-independent. The remaining six-residual bottleneck is *genuine dependence on the fixed exterior face bits*. The finite classification explicitly isolates this distinction: reversal-even *coordinate-triple* obstructions are all two-mark, and every one of them lifts successfully. This does not prove arbitrary NORI in dimension seven or higher.

### Endpoint-tournament factorization and monochromatic orders

# Endpoint-tournament factorization and monochromatic orders

## Arbitrary middle-sign twists: a spanning theorem from oriented Hamilton paths

Let \(V\) be a set of \(n\) coordinate directions, \(T\) an arbitrary tournament on \(V\), and \(s:V\to\{0,1\}\) *any* binary function. Set
\[
t(a,c)=\begin{cases}0&a\to c\text{ in }T,\\1&c\to a\text{ in }T,\end{cases}
\qquad
b(a,v,c)=t(a,c)\oplus s(v)
\]
for pairwise distinct \(a,v,c\). Thus the local comparison tournament at a middle vertex \(v\) is either \(T[V\setminus\{v\}]\) or its complete reversal, with the choice allowed to vary at *every* middle vertex.

**Theorem (arbitrary middle-sign spanning tight path).** For every \(n\ge3\), every such \(b\) has a vertex-simple **spanning positive tight path**. Its direction-only realization \(c(F,(a,v,c))=b(a,v,c)\) on the *physical ordered three-faces* of \(Q_n\) obeys both same-face reversal oddness and antipodal invariance, and admits a **monochromatic full antipodal cube geodesic from every starting root**.

**Proof.** We have \(t(c,a)=1\oplus t(a,c)\), hence \(b(c,v,a)=1\oplus b(a,v,c)\). Direction-only physical-face coloring therefore has \(c(F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\) and \(c(\bar F,\pi)=c(F,\pi)\), giving the legal combined NORI antipodal-reversal law.

Put \(m=\lceil n/2\rceil\ge2\) and \(k=\lfloor n/2\rfloor\). By pigeonhole, some bit \(\varepsilon\) occurs at least \(m\) times among the values \(s(v)\). We choose an \(m\)-element set \(O\subseteq s^{-1}(\varepsilon)\), and put \(E=V\setminus O\), so \(|E|=k\). For \(m\notin\{3,5,7\}\), any \(O\) will work. If \(m\in\{3,5,7\}\) and \(|s^{-1}(\varepsilon)|\ge m+1\), choose \(O\) so that \(T[O]\) is **not regular**. Such a set exists by the following elementary observation.

**Nonregular-subtournament observation.** In a tournament on at least \(m+1\) vertices, with \(m\ge3\) odd, some induced subtournament of order \(m\) is nonregular. Indeed, otherwise fix any set \(U\) of \(m+1\) vertices. Every \(U\setminus\{u\}\) would be regular of degree \((m-1)/2\). Fix \(v\in U\). Comparing its degrees in \(U\setminus\{u\}\) for the various \(u\ne v\) shows that the indicators \(\mathbf1_{\{v\to u\}}\) are equal for every \(u\ne v\), so \(v\) either dominates or loses to every other vertex of \(U\). Its degree in \(U\setminus\{u\}\) would then be \(m-1\) or zero, contradicting regularity since \(0<(m-1)/2<m-1\). This proves the observation.

Finally, if \(m\in\{3,5,7\}\) and the majority sign class has size exactly \(m\), take that entire class for \(O\). Then all members of \(E\) have the opposite sign \(1\oplus\varepsilon\).

Every tournament has a directed Hamilton path. Choose an order \(e_1,\ldots,e_k\) on \(E\) such that
\[
t(e_j,e_{j+1})=\varepsilon\quad(1\le j<k).
\]
For \(\varepsilon=0\), use an ordinary directed Hamilton path in \(T[E]\); for \(\varepsilon=1\), reverse one.

Now prescribe an orientation of the *abstract* path on \(m\) consecutively numbered vertices: its \(j\)-th edge points forward precisely when \(s(e_j)=0\), and backward precisely when \(s(e_j)=1\), for \(1\le j<m\). These \(m-1\) bits are defined because \(k\ge m-1\) in both parities. Havet and Thomassé's exact theorem states that every tournament contains every orientation of a Hamilton path of the same order **except** for an antidirected path in one of three regular tournaments: the directed \(3\)-cycle, the regular \(5\)-vertex tournament, and the Paley \(7\)-vertex tournament. If \(m\notin\{3,5,7\}\), there is no exception (this includes \(m=2\)). If \(m\in\{3,5,7\}\) and the majority class has size at least \(m+1\), our nonregular choice of \(T[O]\) avoids all exceptions. In the remaining case, \(E\) has constant sign \(1\oplus\varepsilon\), so the prescribed abstract path is uniformly directed (or uniformly reversed), and the elementary tournament Hamilton-path theorem applies even if \(T[O]\) is exceptional. Thus in **every dimension \(n\ge3\)** we can realize the prescribed orientation inside \(T[O]\). We obtain an ordering \(o_1,\ldots,o_m\) of all \(O\), with
\[
t(o_j,o_{j+1})=s(e_j)\quad(1\le j<m).
\]

Interleave the two orders, beginning with the \(O\)-order:
\[
p=(o_1,e_1,o_2,e_2,\ldots,o_k,e_k)
\]
when \(n=2k\), and
\[
p=(o_1,e_1,o_2,e_2,\ldots,o_k,e_k,o_{k+1})
\]
when \(n=2k+1\). All \(n\) entries of \(p\) are distinct.

The consecutive triples starting at odd positions have the form \((o_j,e_j,o_{j+1})\); their color is
\[
b(o_j,e_j,o_{j+1})
=t(o_j,o_{j+1})\oplus s(e_j)=0.
\]
Those starting at even positions have the form \((e_j,o_{j+1},e_{j+1})\); their color is
\[
b(e_j,o_{j+1},e_{j+1})
=t(e_j,e_{j+1})\oplus s(o_{j+1})
=\varepsilon\oplus\varepsilon=0.
\]
Thus \(p\) is a spanning positive tight path. The physical cube path traversing the coordinates in the order \(p\) uses each coordinate once and is therefore a full antipodal geodesic. Its consecutive physical ordered-three-face windows all have color zero because the coloring depends only on the ordered coordinate triple, so **every starting cube vertex works**. \(\square\)

**Corollary (large induced factorized chart).** Let \(b\) be an arbitrary ordinary boundary 3-tournament on \(V\). If some \(X\subseteq V\), \(|X|\ge3\), has an induced triple coloring of the above factorized form, then \(b\) has a positive vertex-simple tight path on all \(|X|\) vertices of \(X\), hence a genuine monochromatic cube geodesic of \(|X|\) moves. More generally, the same conclusion holds for physical ordered-three-face colorings on a fixed cube fiber whenever every triple on \(X\) is insensitive to changing the coordinates of \(X\) outside its free set and, on that common fiber, agrees with the factorized rule. This fiber hypothesis ensures that all windows share the *same* direction-only chart.

**Interpretation and exact limitation.** The earlier all-dimensional theorem below permits one exceptional value of \(s\) and uses elementary tournament Hamilton paths. The new theorem permits **arbitrary sign patterns at all \(n\) middle directions**, replacing the required second parity-path orientation by the universal oriented-Hamilton-path theorem; the three exceptional oriented-Hamilton-path instances of orders \(3,5,7\) are avoided by choosing a nonregular majority subtournament or, when the majority class has exactly the required size, by observing that the prescribed orientation pattern is constant. Thus the theorem holds in every dimension \(n\ge3\). This does not assert the same result for a general boundary 3-tournament: there the local middle tournaments \(T_v\) can vary independently, rather than being restrictions of one tournament or its reverse. Handling a chronologically *prescribed sequence of different tournaments* on one parity class is the missing transfer. The familiar theorem on transversal Hamilton paths through a family of tournaments does not automatically supply this ordered requirement. The arbitrary exterior-dependent physical NORI3 case and the separate unrestricted NORI1 full-geodesic conjecture also remain unresolved.

**External theorem used.** F. Havet and S. Thomassé, *Oriented Hamiltonian Paths in Tournaments: A Proof of Rosenfeld's Conjecture*, Journal of Combinatorial Theory, Series B **78** (2000), 243–273, DOI 10.1006/jctb.1999.1945. The published theorem has three small antidirected-path exceptions on 3, 5, and 7 vertices; there are no exceptions on at least eight vertices.

## Two arbitrary middle-local tournament types: a linear guarantee

The preceding theorem assumes all middle-vertex comparison tournaments are a single tournament or its reverse. A different parity argument retains *two completely unrelated* comparison tournaments.

**Theorem (two-type boundary tournaments).** Let \(b\) be an ordinary boundary 3-tournament on \(n\ge3\) vertices. Suppose there are arbitrary tournaments \(T_0,T_1\) on \(V\) and an assignment \(s:V\to\{0,1\}\) such that
\[
b(a,v,c)=t_{s(v)}(a,c),\qquad
t_j(a,c)=\begin{cases}0&a\to c\text{ in }T_j,\\1&c\to a\text{ in }T_j.\end{cases}
\]
Then \(b\) contains a vertex-simple positive tight path of order at least
\[
\boxed{\lceil 2n/3\rceil}.
\]
If the two middle-vertex classes \(A=s^{-1}(0)\) and \(B=s^{-1}(1)\) differ in cardinality by at most one, \(b\) contains a **spanning positive tight path**. Both conclusions give monochromatic genuine coordinate-distinct cube geodesics of the same move lengths for the corresponding direction-only physical face coloring.

**Proof.** For any vertex set \(X\) all of whose middle vertices have the same type \(j\), its induced triple coloring is \(b(a,v,c)=t_j(a,c)\). Split \(X\) into two parity classes with cardinalities differing by at most one. Choose a directed Hamilton path in \(T_j\) restricted to each parity class, and interleave their vertices. Every consecutive ordered triple has its outer vertices consecutive within one of those directed paths and hence has color zero. Thus \(X\) admits a spanning positive tight path.

Write \(a=\max(|A|,|B|)\), \(b_0=\min(|A|,|B|)\), so \(a+b_0=n\). The preceding observation gives a positive tight path of order \(a\) inside a largest type class. Also select \(b_0\) vertices from each class, obtaining sets \(A'\subseteq A\) and \(B'\subseteq B\) of equal order \(b_0\). Choose a directed Hamilton path through \(A'\) in the tournament corresponding to the **middle type of \(B'\)**, and a directed Hamilton path through \(B'\) in the tournament corresponding to the **middle type of \(A'\)**. Interleave these two Hamilton paths. Windows centered at \(B'\) compare consecutive vertices of the \(A'\)-path, and windows centered at \(A'\) compare consecutive vertices of the \(B'\)-path. Every window has color zero, yielding a positive tight path of order \(2b_0\).

Consequently the longest positive path has order at least \(\max(a,2b_0)\). As \(a+b_0=n\),
\[
\max(a,2b_0)\ge 2n/3,
\]
so integer path order is at least \(\lceil2n/3\rceil\).

If \(a=b_0\), the equal-size interleaving already spans \(V\). If \(a=b_0+1\), instead choose a directed Hamilton path of order \(a\) in the tournament of the other class, a directed Hamilton path of order \(b_0\) in the tournament of the first class, and interleave beginning and ending with a vertex from the larger class. Every window is again positive, and all \(n\) vertices occur. The physical realization is exact because the direction-only colors depend exclusively on these ordered triples and all directions are distinct. \(\square\)

**Scope.** The balanced conclusion permits independent and arbitrarily cyclic local tournaments \(T_0,T_1\), with no common global edge order and no reversal relationship between them. The \(\lceil 2n/3\rceil\) result is a genuinely linear guarantee even for unbalanced classes; the arbitrary-middle-sign theorem above strengthens it to full spanning when \(T_1\) is the reverse of \(T_0\) and \(n\ge3\). For a general boundary 3-tournament, the number of distinct local tournament types can grow with \(n\), so neither result asserts a universal linear bound. A promising precise next obstacle is a **chronologically prescribed** Hamilton path through two or more varying tournaments, rather than an unordered transversal that can assign its colors to positions after the path is chosen.

---

## Elementary all-dimensional theorem with one exceptional middle sign

Let \(V\) be a set of \(n\ge3\) coordinate directions, \(T\) an arbitrary tournament on \(V\), and \(s:V\to\mathbb F_2\) a function constant on \(V\setminus\{v\}\) for some \(v\in V\). Let \(t(a,c)\in\mathbb F_2\) be 0 when \(a\to c\) in \(T\) and 1 when \(c\to a\). Define the position-independent ordered-face coloring
\[
c(F,(a,b,c'))=t(a,c')\oplus s(b).
\]
(Here \(c'\) names the third direction, to distinguish it from the coloring \(c\).)

**Theorem (monochromatic tournament-factorized NORI).** This coloring satisfies antipodal-reversal oddness and admits a monochromatic full antipodal geodesic, for every \(n\ge3\).

**Balanced two-path lemma.** For every tournament \(T\) on \(n\ge3\) vertices and any distinguished vertex \(v\), there is an ordering \(p=(p_1,\dots,p_n)\) such that \(p_i\to p_{i+2}\) for all \(1\le i\le n-2\) and \(v\in\{p_1,p_n\}\).

**Proof of the lemma.** Every tournament has a directed Hamilton path: inductively insert a new vertex immediately before the first existing path vertex it dominates, or append it if it dominates none. Choose such a path \(q=(q_1,\ldots,q_n)\), with \(v=q_j\).

If \(n=2k\), at least one of the numbers \(j-1,n-j\) is at least \(k-1\). If \(n-j\ge k-1\), take the consecutive directed path \(q_j,\ldots,q_{j+k-1}\) as the odd-position subsequence \(p_1,p_3,\ldots,p_{2k-1}\). Then \(p_1=v\). If \(j-1\ge k-1\), take \(q_{j-k+1},\ldots,q_j\) as the even-position subsequence \(p_2,p_4,\ldots,p_{2k}\). Then \(p_n=v\). In either case, order the other \(k\) vertices by any directed Hamilton path in their induced tournament and place them in the vacant parity positions.

If \(n=2k+1\), at least one of \(j-1,n-j\) is at least \(k\). Take a directed consecutive \(q\)-segment of \(k+1\) vertices beginning or ending at \(v\), and place it in the odd positions \(p_1,p_3,\ldots,p_{2k+1}\); place a directed Hamilton path on the other \(k\) vertices in the even positions. Then \(v=p_1\) or \(v=p_n\), respectively.

In every case, each parity subsequence is a directed path, hence \(p_i\to p_{i+2}\) for all \(i\). \(\square\)

**Proof of the theorem.** Reversing an ordered triple swaps its outer directions; since \(t(c',a)=1\oplus t(a,c')\), we have
\[
c(\bar F,(c',b,a))=t(c',a)\oplus s(b)=1\oplus c(F,(a,b,c')).
\]
Apply the balanced two-path lemma to \(T\) with distinguished vertex \(v\). Along the resulting full coordinate order \(p\), the window at index \(i\) has color
\[
t(p_i,p_{i+2})\oplus s(p_{i+1})=s(p_{i+1}).
\]
All middle positions \(p_2,\ldots,p_{n-1}\) avoid \(v\), so this value is constant. Since the face coloring ignores exterior fixed bits, the starting cube vertex is arbitrary; every such starting vertex yields a monochromatic antipodal geodesic. \(\square\)

**Scope.** This solves a nontrivial all-dimensional subclass of coordinate-only, reversal-odd ternary colorings, including every endpoint-tournament labeling \(t(a,c)\) and every perturbation by a single exceptional middle direction. It does not treat general triangle-dependent ternary colorings or exterior-face-dependent NORI. The proof exhibits the potential usefulness of balanced two-path covers with prescribed extreme vertices as a replacement for one-switch endpoint repairs.

# Facet monochromatic lifting and a face-dependent tournament-factorized class

**Lemma (monochromatic facet lifting).** Let \(n\ge4\), \(g\in[n]\), and let \(c\) be any binary coloring of ordered three-faces of \(Q_n\), without a symmetry assumption. If one facet \(H=\{x:x_g=\varepsilon\}\cong Q_{n-1}\) contains a full \((n-1)\)-direction geodesic all of whose ordered-three-face windows have the same color, then the full \(Q_n\) has an antipodal geodesic with at most one color change.

**Proof.** Let \(p=(p_1,\ldots,p_{n-1})\) be the direction order of the monochromatic geodesic in \(H\), starting from \(y\in H\). In \(Q_n\), start at the vertex whose \(g\)-bit is \(1-\varepsilon\) and whose other coordinates agree with \(y\), and traverse directions \((g,p_1,\ldots,p_{n-1})\). Its first ordered-three-face window contains \(g\) and has arbitrary color \(b\); after the first move the path is in \(H\), and its remaining \(n-3\) windows agree exactly with those of the given monochromatic path in \(H\), so each has color \(q\). The full word is \(b,q,\ldots,q\), with at most one change. \(\square\)

**Corollary (one-facet tournament factorization).** Fix \(g\) and one facet \(x_g=\varepsilon\). Suppose that on all ordered three-faces lying entirely within this single facet, the coloring is position-independent and is of the form
\[
c(F,(a,b,d))=t(a,d)\oplus s(b),
\]
where \(t(a,d)=0\) for \(a\to d\) in some tournament on \([n]\setminus\{g\}\), \(t(d,a)=1\oplus t(a,d)\), and \(s\) is constant except possibly at one direction. Then \(Q_n\) admits a one-change antipodal geodesic. The coloring of every face containing \(g\), and every face in the opposite facet, is arbitrary; antipodal-reversal oddness is unnecessary.

**Proof.** The balanced two-path tournament lemma proved above supplies a monochromatic full geodesic in the specified \((n-1)\)-facet. Apply the lemma above. \(\square\)

**Research role.** A single suitably structured facet suffices for full one-change closure. In particular, face-dependent behavior outside that facet and across the entering ordered-three-face window cannot spoil the construction. This is a route for extending monochromatic coordinate-only theorems to genuine face-dependent NORI families.

## Recent consequences and compatibility conditions

**Theorem.** There is a coordinate-only reversal-odd ordered-three-face coloring of Q_7 with no monochromatic six-direction geodesic in any coordinate facet. It nevertheless admits a full one-change geodesic. Thus the six-direction monochromatic-five-facet theorem cannot be extended by requiring a monochromatic (n-1)-facet in every dimension.

**Exact construction.** Let V={0,1,2,3,4,5,6}. List the ordered triples (a,b,c) with a<c in lexicographic order, starting at index 0. There are 105 such triples. Let
M=0x1ace4c51f1eca17f4237e025d13.
For a<c, define h(a,b,c) to be bit i of M, where i is that triple's index. For a>c, put h(a,b,c)=1-h(c,b,a). Color each ordered face by h of its direction order, independently of its exterior bits. Reversal oddness follows immediately from the definition.

**Verification certificate.** The following complete finite enumeration reproduces the color-change counts. Its indexing convention fully specifies the example.

    from itertools import permutations
    from collections import Counter
    V = range(7)
    reps = [t for t in permutations(V,3) if t[0] < t[2]]
    index = {t:i for i,t in enumerate(reps)}
    M = int("1ace4c51f1eca17f4237e025d13",16)
    def h(t):
        if t[0] < t[2]:
            return (M >> index[t]) & 1
        return 1 - ((M >> index[t[::-1]]) & 1)
    for k in (5,6,7):
        counts = Counter()
        for p in permutations(V,k):
            w = [h(p[i:i+3]) for i in range(k-2)]
            counts[sum(x != y for x,y in zip(w,w[1:]))] += 1
        print(k, dict(sorted(counts.items())))

The exact output is:

| directions traversed | zero changes | one change | two changes | three changes | four changes |
|---|---:|---:|---:|---:|---:|
| 5 | 100 | 1168 | 1252 | 0 | 0 |
| 6 | 0 | 792 | 2520 | 1728 | 0 |
| 7 | 0 | 144 | 1332 | 2376 | 1188 |

Because colors ignore exterior bits, the zero in the six-direction row excludes every monochromatic six-direction path at every starting cube vertex. The example is a finite exact counterexample to the monochromatic-facet strengthening; the full one-change statement holds.

**Compatibility mechanism.** The cyclic direction order
(0,1,2,5,3,4,6)
has circular triple word 1101001. Three of its six-direction facet deletions are good:
(3,4,6,0,1,2), with word 0011;
(4,6,0,1,2,5), with word 0111;
(6,0,1,2,5,3), with word 1110.
The three-cyclic-facet theorem (Item nori_three_cyclic_facet_witnesses_dimension_independent_20261008) therefore applies. Explicitly, the full rotation
(3,4,6,0,1,2,5)
has word 00111.

**Research implication.** Retain one-change facet witnesses as the induction state. Their compatibility on a common cyclic direction order can force full closure even when every monochromatic facet is absent. This example supports the cyclic-witness target and identifies a strict limitation of demanding monochromatic facet transfer at every stage.

# Dimension-independent adjacent-order exchange law

Let \(n\ge4\), \(x\in Q_n\), and \(p=(p_1,\ldots,p_n)\) be a permutation of the coordinate directions. For \(1\le i\le n-2\), let \(W_i(x,p)\) be the *actual* ordered three-face window of the full geodesic from \(x\) following \(p\), and let \(w_i(x,p)=c(W_i(x,p))\) for an arbitrary binary ordered-face coloring \(c\). For \(1\le i\le n-3\), write \(d_i(x,p)=w_i(x,p)\oplus w_{i+1}(x,p)\). Let \(\tau_kp\) interchange adjacent directions \(p_k,p_{k+1}\), where \(1\le k\le n-1\).

**Theorem (four-window locality).** For every \(x,p,k\),
\[
W_i(x,\tau_kp)=W_i(x,p)
\quad\text{for }i\notin [k-2,k+1]\cap[1,n-2],
\tag{1}
\]
and therefore
\[
d_i(x,\tau_kp)=d_i(x,p)
\quad\text{for }i\notin[k-3,k+1]\cap[1,n-3].
\tag{2}
\]
In particular, a single adjacent swap can modify **at most four consecutive window colors** and **at most five consecutive seams**, independently of \(n\) and irrespective of exterior-face dependence.

For the two central potentially affected windows \(i=k-1\) and \(i=k\), whenever these indices exist, the underlying geometric three-face is unchanged by the swap, and only the ordering of its free directions changes. Explicitly, writing \(a=p_{k-1}\), \(b=p_k\), \(c=p_{k+1}\), \(d=p_{k+2}\), these central free-direction orders are
\[
(a,b,c)\longleftrightarrow(a,c,b),\qquad
(b,c,d)\longleftrightarrow(c,b,d),
\tag{3}
\]
at **identical exterior face positions**. The other potentially affected windows are the two neighboring positions \(k-2,k+1\), where the geometric free triple changes.

**Proof.** Before the swapped pair is reached, the two full geodesics traverse exactly the same ordered directions. After the pair is completed, they have traversed exactly the same *set* of directions and agree on the current cube vertex. Thus for every window whose three free positions avoid both swap positions, its ordered free triple and all previously traversed directions are the same for both paths. The two corresponding ordered faces coincide. A length-three interval intersects positions \(k,k+1\) exactly when its starting position belongs to \(\{k-2,k-1,k,k+1\}\), proving (1). Each change indicator is the XOR of two consecutive window colors, so it can change only if either endpoint window does, giving (2). For \(i=k-1\) and \(i=k\), both exchanged directions lie within the same free triple; the prefix preceding each such window is the same in both geodesics, so their exterior face positions coincide. The displayed direction orders follow immediately. \(\square\)

**Interaction with NORI antipodal reversal.** If \(c\) satisfies \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\), the established root-coupled reversal involution
\[
J(x,p)=(x,\operatorname{rev}p)
\]
obeys \(w_i(x,\operatorname{rev}p)=1\oplus w_{n-1-i}(x,p)\) and \(d_i(x,\operatorname{rev}p)=d_{n-2-i}(x,p)\). Adjacent swaps transform equivariantly under this involution:
\[
\operatorname{rev}(\tau_k p)=\tau_{n-k}(\operatorname{rev}p).
\tag{4}
\]
Thus the graph of full orders, with edges given by adjacent swaps, is the **permutohedron**, equipped with a free reversal involution and an antipodally equivariant, locally constrained word label. The NORI conjecture asks for some root and vertex in this coupled family of permutohedra whose word has at most one change.

**Research obligation.** This lemma gives a dimension-independent local move for a possible minimal-defect exchange/descent argument. It is not itself a decreasing-move theorem. A closure proof must show that the no-good-geodesic hypothesis, together with cross-root face-fiber incidence and antipodal reversal, forces either a strictly improving local exchange (possibly following a finite sequence of nonincreasing exchanges) or a topological obstruction to all local minima. Such a proof would apply uniformly to every dimension, unlike further Q7 subclass classifications.

## Chronologically prescribed transitive tournaments: a rank-potential theorem and the coupled-parity obstruction

A tempting strengthening of the two-parity factorization method is to replace one fixed comparison tournament by a tournament that varies with the *position* in a path. The correct transitive case has a simple exact solution. It still does not synchronize the two interleaved parity paths.

**Theorem (chronological transitive Hamilton paths).** Let \(X\) be a set of \(m\ge 2\) vertices, and for each \(1\le i<m\) let \(T_i\) be a transitive tournament on \(X\). There is an ordering \(x_1,\ldots,x_m\) of all of \(X\) such that
\[
 x_i\longrightarrow x_{i+1}\quad\text{in }T_i
 \qquad(1\le i<m).
\]
More generally, for arbitrary injective real rank functions \(\rho_i:X\to\mathbb R\), one can require \(\rho_i(x_i)<\rho_i(x_{i+1})\) simultaneously.

**Proof.** Give \(T_i\) its unique increasing rank order \(\rho_i\). For every permutation \(p=(p_1,\ldots,p_m)\), define the scalar potential
\[
 \Phi(p)=\sum_{j=1}^m\ \sum_{i=j}^{m-1}\rho_i(p_j).
\]
Choose a permutation minimizing \(\Phi\). If \(p_j=a,p_{j+1}=b\) and \(\rho_j(a)>\rho_j(b)\), swapping those adjacent entries changes the potential by
\[
 \Phi(p\circ(j\ j+1))-\Phi(p)=\rho_j(b)-\rho_j(a)<0,
\]
contradicting minimality. Thus every prescribed comparison is positive. The proof is constructive through a finite linear assignment minimization followed, equivalently, by descent along improving adjacent swaps. \(\square\)

**Boundary-tournament half-window consequence.** Let \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_{m-1}\}\) be disjoint vertex sets of an ordinary boundary 3-tournament, with the sequence \(b_1,\ldots,b_{m-1}\) already fixed. Suppose that for each \(i\) the middle-local tournament \(T_{b_i}[A]\), defined by \(u\to v\) iff \(h(u,b_i,v)=1\), is transitive. The theorem orders \(A\) so that
\[
 h(a_i,b_i,a_{i+1})=1\qquad (1\le i<m).
\]
Consequently the vertex-simple interleaving
\[
 a_1,b_1,a_2,b_2,\ldots,b_{m-1},a_m
\]
has **every triple centered in \(B\)** positive. Its remaining windows, centered in \(A\), are not prescribed by this argument. In a boundary tournament with all middle-local tournaments transitive, one may choose either parity's center order arbitrarily and satisfy all windows of that parity by reordering the other class.

**First obstruction: transitivity really matters for prescribed chronology.** Take \(X=\{0,1,2\}\). Let \(T_1\) be the directed triangle \(0\to1\to2\to0\), and \(T_2\) its reversal. There is no ordering \(a,b,c\) of the three distinct vertices with \(a\to b\) in \(T_1\) and \(b\to c\) in \(T_2\): the latter would give \(c\to b\) in \(T_1\), but \(b\) has exactly one inneighbor in \(T_1\), namely \(a\). Thus a chronologically prescribed Hamilton path need not exist for arbitrary tournaments, even though ordinary transversal tournament-path results can freely permute the assignments of tournaments to edge positions.

**Second obstruction: transitive local centers still need not synchronize the two parities.** On \(V=\{0,1,2,3\}\), partition the six edges of \(K_4\) into its three perfect matchings:
\[
 M_0=\{\{0,3\},\{1,2\}\},\quad
 M_1=\{\{0,1\},\{2,3\}\},\quad
 M_2=\{\{0,2\},\{1,3\}\}.
\]
Give every edge in \(M_j\) weight \(j\), and for pairwise distinct \(a,b,c\) put
\[
 h(a,b,c)=\mathbf1_{\{w(ab)<w(bc)\}}.
\]
At each middle vertex \(b\), the three incident edge weights are \(0,1,2\) in some order. Hence \(T_b\) is transitive, and \(h(c,b,a)=1-h(a,b,c)\). For any vertex-simple spanning tight path \(p_1,p_2,p_3,p_4\), its first and last graph edges \(\{p_1,p_2\}\) and \(\{p_3,p_4\}\) are disjoint; they therefore belong to the **same** perfect matching and have the same weight. The two successive triple comparisons cannot both be increasing (or both decreasing). Indeed, since the middle edge shares a vertex with each outer edge, its matching is different, so the two triple colors are opposite for **every** spanning order. Thus this ordinary boundary 3-tournament has no monochromatic spanning tight path, despite all four local comparison tournaments being transitive. This example is even induced by a global edge weighting; ties occur only between disjoint edges and can be broken arbitrarily to obtain a strict edge order. Its direction-only physical cube realization is legal under antipodal-reversal oddness and fails the monochromatic *full* geodesic property in dimension four.

**Exact scope.** The rank-potential theorem settles the chronological path problem for transitive time-indexed tournaments and proves a valid half-window realization theorem. The \(K_4\) example blocks the inference from *separate* chronological solvability on the two parity classes to simultaneous spanning tight-path solvability, even for globally edge-ordered boundary tournaments. It does not challenge the established \(\Omega(\sqrt n)\) lower bound for ordinary boundary tournaments, the nearly-linear edge-ordered altitude bound, or the separate unrestricted NORI1 physical-edge conjecture. Any successful use of time-indexed orders for the full boundary problem needs a joint coupling mechanism stronger than the one-parity rank potential.


### Nearly-linear monochromatic geodesics for acyclic boundary 3-tournaments

# Nearly-linear monochromatic geodesics for acyclic boundary 3-tournaments

## Scope and principal transfer theorem

Let \(V\) be an \(n\)-element coordinate set, \(n\ge3\). A **boundary 3-tournament** is a function \(b(a,b,c)\in\{0,1\}\) on ordered triples of distinct coordinates obeying \(b(c,b,a)=1-b(a,b,c)\). The corresponding direction-only coloring of genuine physical ordered 3-faces is
\[
 c(F,(a,b,c)):=b(a,b,c).
 \tag{1}
\]
This satisfies both \(c(F,\operatorname{rev}\pi)=1-c(F,\pi)\) and \(c(\bar F,\pi)=c(F,\pi)\), hence the combined NORI antipodal-reversal oddness condition.

Associate to \(b\) an orientation \(\vec L\) of the line graph \(L(K_V)\), whose vertices are unordered edges of \(K_V\), by orienting
\[
 \{a,b\}\longrightarrow\{b,c\}
 \quad\Longleftrightarrow\quad b(a,b,c)=1.
 \tag{2}
\]
The reversal identity makes (2) well defined.

**Theorem (acyclic transfer, using the edge-ordered-graph altitude theorem).** If \(\vec L\) is acyclic, the coloring (1) has a monochromatic geodesic traversing at least
\[
 \frac{n}{2^{C\sqrt{(\log n)(\log\log n)}}}
 \tag{3}
\]
distinct coordinate directions, for some absolute constant \(C>0\) and all sufficiently large \(n\). In particular its longest monochromatic geodesic has length \(n^{1-o(1)}\).

The count in (3) is of **edges of the original simple path in \(K_V\)**, equivalently of coordinate moves in the cube. It is not a count of vertices of \(L(K_V)\) without an incidence-consistent lift. The resulting cube geodesic may be partial; (3) makes no spanning assertion.

**Proof.** Since the finite orientation \(\vec L\) is acyclic, take a topological order \(\prec\) of its vertices. These vertices are precisely the unordered edges of \(K_V\), so \(\prec\) is one strict ordering of the edges of \(K_V\). Every comparison (2) is respected:
\[
 b(a,b,c)=1\quad\Longleftrightarrow\quad \{a,b\}\prec\{b,c\}. \tag{4}
\]
For the converse direction in (4), note that the two line-graph vertices are adjacent and their edge is oriented exactly one way; topological order must respect that orientation.

Apply the theorem of M. Bucić, M. Kwan, A. Pokrovskiy, B. Sudakov, T. Tran and A. Z. Wagner (*Nearly-linear monotone paths in edge-ordered graphs*, Israel J. Math. 238 (2020), 663–685, Theorem 1.1; DOI 10.1007/s11856-020-2035-7) to the edge-ordered complete graph \((K_V,\prec)\). This gives a **vertex-simple** original-graph path
\[
 v_0,v_1,\ldots,v_\ell,\quad
 \{v_0,v_1\}\prec\{v_1,v_2\}\prec\cdots
 \prec\{v_{\ell-1},v_\ell\},
 \tag{5}
\]
with \(\ell\) at least the quantity in (3).

Choose any cube starting vertex \(x\) and traverse distinct coordinate directions \(v_0,v_1,\ldots,v_\ell\) in this order. Because no coordinate is repeated, this is a genuine geodesic of length \(\ell+1\) if we traverse every \(v_i\), or \(\ell\) if we traverse \(v_0,\ldots,v_{\ell-1}\). In either case, all its consecutive ordered 3-face windows have color 1 by (4)–(5), using the direction-only rule (1). Choosing all \(\ell+1\) vertices of the original graph path as distinct coordinate moves yields a cube geodesic of length \(\ell+1\), with exactly \(\ell-1\) windows, each colored 1. Thus (3) follows (indeed with one extra coordinate move). The start \(x\) is arbitrary because the coloring ignores fixed exterior bits. \(\square\)

**Length convention.** The edge-ordered increasing path has \(\ell\) edges and \(\ell+1\) distinct original vertices. These \(\ell+1\) distinct vertices become \(\ell+1\) cube coordinate directions. Thus there is no hidden loss through repeated original vertices, and there is no appeal to an arbitrary directed path of \(L(K_V)\).

## What directed cycles can obstruct

**Corollary.** Any sequence of direction-only boundary 3-tournaments \(b_n\) whose longest monochromatic cube geodesic has \(o(n^{1-o(1)})\) length (in particular \(O(\sqrt n)\)) must have a **directed cycle in its line-graph comparison orientation** for all sufficiently large \(n\).

More quantitatively, if a direction-only boundary tournament on \(n\) directions has no monochromatic geodesic of length at least the explicit lower bound (3), then its line-graph orientation contains a directed cycle.

This is the contrapositive of the theorem. It gives a precise requirement for a prospective short-path boundary obstruction: the local comparisons cannot all arise from one global edge ordering.

The converse is false: presence of a directed cycle says nothing by itself about the largest monochromatic simple path. It only obstructs an exact edge-order realization. The orientation and realizability correspondence are proved independently in the sibling manuscript *Scope of the distinguished-coordinate counterexamples and edge-order realizability*.

## Exact limitation: exterior dependence

The theorem applies to the **direction-only** coloring (1), and in particular to every edge-ordered complete graph. For a general physical coloring \(c(F,(a,b,c))\), even assuming
\[
 c(F,(c,b,a))=1-c(F,(a,b,c)),\qquad
 c(\bar F,(a,b,c))=c(F,(a,b,c)),
 \tag{6}
\]
the comparison assigned to adjacent edges \(\{a,b\}\) and \(\{b,c\}\) can depend on the exterior coordinate bits of the physical face \(F\). Different windows along a cube path generally belong to different exterior fibers. Even if each fiber separately admits an acyclic comparison orientation, its topological order may depend on the fiber and therefore need not supply a common monotone original-graph path.

A sufficient **global-flatness hypothesis** for the proof is that one total edge order \(\prec\) of \(K_V\) realizes every comparison uniformly:
\[
 c(F,(a,b,c))=\mathbf1_{\{\{a,b\}\prec\{b,c\}\}}\quad
 \text{for every physical face }F.
 \tag{7}
\]
This is stronger than separate fiberwise acyclicity. Identifying a weaker coherent-transport hypothesis under which (3) persists is an explicit structural problem with a clear mathematical payoff.

## Relation to NORI-k switch amplification

The unbounded-switch multilevel coloring of ordered physical 3-faces uses the reversal-even rule \(h(a,b,c)=h(c,b,a)\), so it violates the extra boundary symmetry (6). The present theorem gives a strong lower bound on **long monochromatic paths** for an acyclic subclass of the reversal-odd boundary-compatible colorings; it makes no assertion for boundary tournaments with directed cycles, and no assertion for arbitrary exterior-dependent colorings satisfying (6).

In particular, the old NORI3 obstruction does not imply an edge-ordered increasing-path obstruction. The near-linear bound (3) is an application of the published Bucić–Kwan–Pokrovskiy–Sudakov–Tran–Wagner theorem, **not** a new lower bound for altitude. The contribution here is the exact incidence- and face-consistent transfer and its explicit boundary on possible counterexamples.

## References

M. Bucić, M. Kwan, A. Pokrovskiy, B. Sudakov, T. Tran, A. Z. Wagner, *Nearly-linear monotone paths in edge-ordered graphs*, Israel Journal of Mathematics **238** (2020), 663–685. DOI: 10.1007/s11856-020-2035-7. arXiv:1809.01468.

See also the companion NORI research manuscript *Scope of the distinguished-coordinate counterexamples and edge-order realizability* for the exact correspondence between boundary 3-tournaments and orientations of \(L(K_n)\).

## Directed-pair rank rigidity and quantitative boundary defects

The following rigidity result closes a natural attempt to enlarge the edge-ordered boundary-tournament class by assigning asymmetric scores to *ordered* pairs.

**Theorem (directed-pair score symmetrization).** Let \(V\) be a finite set, and let \(\lambda(a,b)\) take values in an arbitrary totally ordered set for all distinct \(a,b\in V\). Define
\[
h(a,b,c)=\mathbf 1\{\lambda(a,b)<\lambda(b,c)\},\qquad a,b,c\ \text{distinct}.
\tag{8}
\]
If \(h(c,b,a)=1-h(a,b,c)\) for every ordered triple, then there exists one total order \(\prec\) of the undirected edges of \(K_V\) for which
\[
h(a,b,c)=1\quad\Longleftrightarrow\quad\{a,b\}\prec\{b,c\}.
\tag{9}
\]
Conversely, every boundary tournament induced by a global edge order admits the representation (8).

**Proof.** Because \(V\) is finite, replace each \(\lambda\)-value by its rank among the \(m\) distinct values attained by \(\lambda\). This preserves all strict and weak comparisons. Write \(\rho(a,b)\in\{1,\ldots,m\}\) for the resulting rank and put
\[
s(\{a,b\})=\rho(a,b)+\rho(b,a).
\tag{10}
\]
If \(h(a,b,c)=1\), then \(\rho(a,b)<\rho(b,c)\). The reversal identity gives \(h(c,b,a)=0\), so \(\rho(c,b)\ge\rho(b,a)\). Adding yields
\[
s(\{a,b\})<s(\{b,c\}).
\]
If \(h(a,b,c)=0\), apply the previous argument to the reversed triple, for which \(h(c,b,a)=1\), to obtain the reverse *strict* score inequality. Consequently every pair of incident edges has distinct \(s\)-scores and the strict inequalities induced by \(h\) coincide with their comparisons under \(s\). Sort undirected edges by \(s\), breaking possible ties only between disjoint edges. This produces the total edge order (9). Conversely, assign to both directed copies \((a,b)\) and \((b,a)\) the rank of \(\{a,b\}\) in any prescribed total edge order. Formula (8) reproduces its adjacent-edge comparisons. \(\square\)

**Corollary (nearly-linear positive tight paths).** Every reversal-odd boundary tournament represented by directed-pair strict comparisons (8) admits a positive vertex-simple tight path on \(n/2^{O(\sqrt{\log n\log\log n})}\) vertices, by the preceding acyclic-transfer theorem and the Bucić–Kwan–Pokrovskiy–Sudakov–Tran–Wagner monotone-path theorem. The original graph vertices are distinct; their labels provide distinct cube directions in the corresponding direction-only physical coloring.

The rigidity admits a quantitative form *without assuming reversal oddness*. For each unordered triple \(\{a,b,c\}\), say it is **defective** if at least one of its three possible middle vertices violates \(h(c,b,a)=1-h(a,b,c)\), with \(h\) still defined by (8). Let \(B\) be the number of defective unordered triples.

**Theorem (rank-height/defect tradeoff).** If the directed score \(\lambda\) takes \(m\) distinct values, then
\[
\boxed{B\ \ge\ \frac n6\left(\frac{(n-1)^2}{2m-1}-(n-1)\right)_+.}
\tag{11}
\]
In particular, if there are no defective triples then
\[
\boxed{m\ge \lceil n/2\rceil;}
\tag{12}
\]
if \(m=O(\log n)\) along a family with \(n\to\infty\), then \(B=\Omega(n^3/\log n)\).

**Proof.** Normalize all distinct \(\lambda\)-values to consecutive ranks \(1,\ldots,m\) as in the preceding theorem and use the same symmetric integer scores (10), which range from \(2\) to \(2m\). If two incident edges \(\{a,b\},\{b,c\}\) have equal symmetric score, reversal oddness at middle vertex \(b\) is impossible: otherwise the first theorem's strict-inequality argument, which uses only reversal oddness at that triple, would force one of the two unequal strict orders. Fix \(b\), and let \(d_t(b)\) count its \(n-1\) incident edges with score \(t\in\{2,\ldots,2m\}\). Every colliding pair of edges produces a reversal violation with middle \(b\). By Cauchy–Schwarz,
\[
\begin{aligned}
\sum_{t=2}^{2m}\binom{d_t(b)}2
&=\frac12\left(\sum_t d_t(b)^2-(n-1)\right)\\
&\ge\frac12\left(\frac{(n-1)^2}{2m-1}-(n-1)\right).
\end{aligned}
\]
Summing over \(b\) counts at most three violating middle-vertex choices for each defective unordered triple. Dividing by three and taking the nonnegative part gives (11). If \(B=0\), every star has \(n-1\) pairwise distinct symmetric integer scores in a set of size \(2m-1\), implying (12). The asymptotic defect bound follows by substituting \(m=O(\log n)\) into (11). \(\square\)

**Scope and consequence.** The proof holds for arbitrary asymmetric ordered-pair scores, arbitrary discrete ranking/tie patterns, and (by rank normalization) every totally ordered score set, including lexicographically ordered tuples. It is an exact no-go for transferring an \(O(\log n)\)-height *directed-pair strict-comparison* construction to an ordinary boundary 3-tournament. It does **not** imply global edge-orderability for arbitrary boundary 3-tournaments, because their line-graph comparison orientations can contain directed cycles. It makes no assertion about unrestricted exterior-dependent physical 3-face colorings or unrestricted NORI1. A full ordinary boundary theorem must exploit mechanisms beyond strict comparisons of directed-pair potentials.


### Polynomial monochromatic geodesics from sparse triplewise exterior support

# Long monochromatic NORI3 geodesics under sparse triplewise exterior dependence

## Theorem

Let \(V\) be the \(n\) coordinate directions of \(Q_n\). Let \(c(F,(a,b,c))\in\{0,1\}\) color *physical ordered three-faces*. Assume **same-face reversal oddness**
\[
c(F,(a,b,c))=1-c(F,(c,b,a))
\tag{R}
\]
for every ordered physical face. For each unordered triple \(T\subset V\), suppose there exists a set of exterior coordinates \(S_T\subset V\setminus T\) of size at most \(d\), such that all six ordered-face colors with free set \(T\) depend only on their free-direction order and the fixed bits on \(S_T\). These support sets are allowed to vary arbitrarily with \(T\).

**Theorem (sparse exterior-support boundary-snake transfer).** For \(1\le d\le n-3\), as \(n/d\to\infty\), the coloring has a monochromatic *genuine coordinate-distinct geodesic* of length
\[
\boxed{\Omega((n/d)^{1/3})}.
\tag{1}
\]
The explicit estimate \(L_{\max}(c)\ge1+(n/d)^{1/3}/2100\) holds whenever \(n/d\ge32^{3/2}\).

If \(d=0\), then \(c\) is direction-only, and the full Devine–Milans boundary-tournament snake theorem gives
\[
L_{\max}(c)\ge1+\sqrt{(n-1)/2}.
\tag{2}
\]
If all ordinary triples outside a *common* set \(S\) of \(t\) directions depend only on their exterior bits in \(S\), the same theorem directly yields
\[
L_{\max}(c)\ge1+\sqrt{(n-t-1)/2}\quad(n-t\ge3).
\tag{3}
\]

Condition (R) is exactly the additional same-face reversal symmetry proposed for **boundary-compatible NORI3**. When the ordinary NORI law \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\) also holds, (R) is equivalent to the additional antipodal invariance \(c(\bar F,\pi)=c(F,\pi)\). No antipodal hypothesis beyond (R) is needed for the theorem.

## Lemma: robust boundary snake with selectively discarded terminal pairs

A **partial boundary 3-tournament** on \(N\) vertices has a set of available unordered triples. For every available triple, exactly one ordering of each same-middle reversal pair is a positive directed triple; unavailable triples have no positive orderings. For an unordered pair \(e=\{u,v\}\), let \(b(e)\) be the number of unavailable triples containing \(e\). Fix \(b\ge0\), call \(e\) *clean* when \(b(e)\le b\), and let
\[
\alpha=\frac{\#\{\mathrm{clean\ unordered\ pairs}\}}{\binom N2}.
\]
If \(L\ge2\) is the maximum vertex order of a vertex-simple positive directed tight path, then
\[
\boxed{\alpha\frac{N-1}{2}\le(L-1)^2+b(L-1).}
\tag{4}
\]

**Proof.** For each *clean* unordered pair \(\{u,v\}\), find a longest positive directed tight path ending either in \(uv\) or in \(vu\), giving a terminal order \(r(\{u,v\})\in[2,L]\). Orient the pair toward the endpoint of the chosen path, breaking ties arbitrarily. Orienting only the clean pairs produces a partial tournament on the \(N\) vertices with \(\alpha\binom N2\) arcs. Hence some vertex \(v\) has at least \(\alpha(N-1)/2\) incoming clean pairs.

For \(r=2,\ldots,L\), let \(U_r\) be its incoming clean neighbors having terminal order \(r\), and put \(q=|U_r|\). For distinct \(u,w\in U_r\), whenever \(\{u,v,w\}\) is available, direct the comparison \(u\to w\) precisely when \((u,v,w)\) is positive. Same-middle reversal oddness makes this a partial tournament. Since the terminal pair \(\{u,v\}\) is clean for every \(u\in U_r\), each \(u\) participates in at most \(b\) missing comparisons. The induced comparison tournament therefore has at most \(bq/2\) missing edges, and some \(u\in U_r\) has outdegree at least \((q-1-b)/2\).

Take a longest positive \(r\)-vertex path \(P\) ending \(uv\). Each outneighbor \(w\) in the comparison tournament must already belong to \(P\), or \((u,v,w)\) extends \(P\) to a positive \((r+1)\)-vertex path ending \(vw\), contradicting that the clean pair \(\{v,w\}\) is oriented \(w\to v\) and has terminal order exactly \(r\). There are at most \(r-2\) such outneighbors. Thus \(q\le2r+b-3\), and
\[
\alpha(N-1)/2\le\sum_{r=2}^L|U_r|
\le \sum_{r=2}^L(2r+b-3)
=(L-1)^2+b(L-1).
\]
This proves (4). The positive tight path is *vertex-simple in the original \(N\)-vertex hypergraph*, not merely a directed path in a line graph. \(\square\)

When \(b=0,\alpha=1\), (4) recovers the scrapbook's \(L\ge1+\sqrt{(N-1)/2}\). This robust version is useful even when many triples are unavailable, provided most terminal pairs have few unavailable extensions.

## Random extraction: retain good triples and clean pairs

Assume \(d\ge1\). Choose each original direction independently with probability
\[
p=(d^2n)^{-1/3},\qquad \mu=np=(n/d)^{2/3}.
\]
Let \(X\) be the selected direction set, of size \(N\). Call \(T\subseteq X\) **bad** if \(S_T\cap X\ne\varnothing\), and let \(B(X)\) count bad unordered triples. Every bad triple is witnessed by a four-element inclusion \(T\cup\{u\}\subseteq X\) for some \(u\in S_T\). By linearity of expectation,
\[
\mathbb E B(X)\le d\binom n3p^4
\le\frac16\mu^{5/2}.
\tag{5}
\]
Markov gives \(\Pr(B(X)>\mu^{5/2})\le1/6\), and Chernoff gives \(\Pr(N<\mu/2)\le e^{-\mu/8}<1/6\) whenever \(\mu\ge32\). Consequently some \(X\) satisfies
\[
N\ge\mu/2,\qquad B(X)\le\mu^{5/2}.
\tag{6}
\]

Construct a partial boundary tournament on \(X\) by declaring each *good* unordered triple \(T\) (those with \(S_T\cap X=\varnothing\)) available. Define its orientations using one fixed exterior cube root \(x_0\), as explained below; (R) guarantees exactly one orientation in each reversal pair. For each unordered pair \(\{u,v\}\subseteq X\), let \(b(\{u,v\})\) count bad triples containing it. Since each bad triple contributes to exactly three unordered pairs,
\[
\sum_{\{u,v\}\subset X}b(\{u,v\})=3B(X).
\]
Choose the clean-pair threshold \(b=128\sqrt\mu\). There are at most \(3\mu^2/128\) dirty pairs. Because \(N\ge\mu/2\ge16\),
\[
\binom N2\ge N^2/4\ge\mu^2/16.
\]
Therefore dirty pairs constitute at most \(3/8\) of all pairs, and the clean proportion obeys \(\alpha\ge5/8\). Lemma (4) implies
\[
\frac{N-1}{4}\le(L-1)^2+128\sqrt\mu(L-1).
\tag{7}
\]
Put \(z=L-1\). If \(z\ge\sqrt\mu\), the claimed bound follows. Otherwise \(z^2\le z\sqrt\mu\), and \(N\ge\mu/2\), \(\mu\ge32\) imply
\[
\mu/16\le(N-1)/4\le129z\sqrt\mu,
\qquad z\ge\sqrt\mu/2064>\sqrt\mu/2100.
\]
Since \(\sqrt\mu=(n/d)^{1/3}\), this proves the explicit estimate in (1).

## Exact physical-fiber realization and root consistency

Fix a single cube vertex \(x_0\in Q_n\) BEFORE orienting any available triple. For every good triple \(T\subseteq X\), the support \(S_T\) lies outside \(X\), so none of its influential fixed exterior bits ever changes along *any* cube path using directions from \(X\). Thus for every ordering \(\pi\) of \(T\), all actual physical faces with free directions \(T\) encountered by such paths have exactly the color determined by \(\pi\) and \(x_0|_{S_T}\), regardless of other exterior-coordinate bits. This defines one direction-only same-face reversal-odd tournament chart on the good triples. Omit the bad triples altogether.

By the robust snake lemma, there is a positive directed tight path \(u_1,\ldots,u_L\) of DISTINCT vertices/directions using only good triples. Starting at \(x_0\), traverse the actual cube coordinates in this order. The resulting cube path is a genuine direction-distinct geodesic; its successive physical ordered 3-faces have the precisely matched good-triple colors and are all positive. There is no incompatible-root transfer, no abstract physical-face substitution, and no repeated cube direction.

For \(d=0\), take \(X=V\) and apply the complete Devine–Milans snake theorem. For a common exterior support \(S\), choose \(X=V\setminus S\), freeze \(S\)-bits at \(x_0\), and apply the complete theorem on \(n-t\) directions. This proves (2)–(3). \(\square\)

## Consequences, prior improvements, and boundary of applicability

This resolves a nontrivial intermediate structural class: **polynomial-length monochromatic paths survive both same-face reversal oddness and arbitrary triple-specific exterior interactions of bounded support**, even though no global exterior support is available. The earlier hypergraph-independent-set proof supplied only exponent \(1/6\). A first robust snake bound controlling missing triples per vertex improved it to \(1/4\). The selective-terminal-pair lemma above gives the current strongest exponent \(1/3\), making the earlier arguments valid but superseded.

For legal boundary-compatible NORI3, complement invariance implies that a face color depending on at most ONE exterior bit cannot genuinely depend on that bit; such colorings are direction-only, so (2) holds for \(d\le1\). Genuine nonconstant complement-invariant dependencies first appear with \(d\ge2\). In unrestricted boundary-compatible NORI3, a triple can depend on \(\Theta(n)\) exterior bits, where (1) gives no growing bound. Likewise this does not settle unrestricted NORI3's universal \(\Omega(\log n)\) question: the antichain and self-dual constructions avoiding that structural hypothesis have \(O(\log n)\) maximum monochromatic geodesics. The problem of improving the exponent \(1/3\) within the sparse-support class is separately open; no sharpness claim is made.

**Source attribution.** The complete boundary-tournament \(1+\sqrt{(N-1)/2}\) terminal-pair bound is from R. C. Devine and K. G. Milans, *Tight paths in fully directed hypergraphs*, the supplied scrapbook, sections “Antisymmetric Tournaments” and “Boundary Tournaments.” The partial-tournament clean-pair lemma, probabilistic extraction, and physical-face transfer giving exponent \(1/3\) above are new to this manuscript.

### Layered boundary snakes and a dense rank-sensitivity barrier

# Layered boundary snakes and the dense rank-sensitivity barrier

## Main abstract theorem: one boundary tournament per step

Let \(V\) be an \(n\)-element set. For every \(j\ge0\), choose **arbitrary**, possibly unrelated functions \(h_j(a,b,c)\in\{0,1\}\) on distinct ordered triples satisfying same-middle reversal oddness \(h_j(c,b,a)=1-h_j(a,b,c)\). Then there exist \(L\ge1+\sqrt{(n-1)/2}\) **distinct** vertices \(v_1,\ldots,v_L\) with \(h_{i-1}(v_i,v_{i+1},v_{i+2})=1\) for all \(1\le i\le L-2\).

**Proof (correct step indexing).** Define a positive \(r\)-vertex path by requiring its triple at starting position \(i\) to be positive in \(h_{i-1}\). A two-vertex path is positive vacuously. For every unordered pair \(e=\{u,v\}\), select a longest such simple path ending either \(u,v\) or \(v,u\); write \(r(e)\in[2,L]\) for its maximum order and orient \(e\) toward its selected terminal vertex. This makes a tournament on \(V\). Choose \(v\) with incoming degree at least \((n-1)/2\). Let \(U_r\) be its incoming neighbors \(u\to v\) with \(r(\{u,v\})=r\), and put \(q=|U_r|\).

For \(u,w\in U_r\), orient \(u\to w\) iff \(h_{r-2}(u,v,w)=1\). (Appending to an \(r\)-vertex path creates the triple at window **position \(r-1\)**, which is evaluated by \(h_{r-2}\), not \(h_{r-1}\).) Reversal oddness makes this a tournament. Pick \(u\) with at least \((q-1)/2\) outneighbors, and a positive longest path ending \(u,v\) of order \(r\). Every such outneighbor \(w\) is already among the first \(r-2\) vertices of that path: otherwise append \(w\), obtaining an \((r+1)\)-vertex positive path ending \(v,w\), contradicting \(r(\{v,w\})=r\) with selected orientation \(w\to v\). Therefore \(q\le 2r-3\). Summing over \(r=2,\ldots,L\),
\[
(n-1)/2\le \sum_r |U_r|\le\sum_{r=2}^{L}(2r-3)=(L-1)^2.
\]
This proves the theorem; the resulting path is vertex-simple in \(V\), not merely a walk in the terminal-pair graph.

## Physical face transfer: all exterior bits may matter

Let \(c(F,\pi)\) color physical ordered 3-faces of \(Q_n\), obeying \(c(F,\operatorname{rev}\pi)=1-c(F,\pi)\). Suppose for each ordered triple \(\pi\) the color depends on the fixed exterior vector only through its **Hamming weight**:
\[
c(F,\pi)=h_{|z(F)|}(\pi).
\tag{1}
\]
The \(h_j\) are arbitrary and reversal-odd, with no bound on exterior support or linearity. Starting a direction-distinct cube geodesic at \(0^n\), its \(i\)-th 3-face window has precisely \(i-1\) exterior 1-bits (its earlier traversed directions). Its actual physical color is therefore \(h_{i-1}(p_i,p_{i+1},p_{i+2})\). The abstract theorem produces a **genuine monochromatic cube geodesic** with at least \(1+\sqrt{(n-1)/2}\) coordinate moves, all directions distinct, using one fixed root. There is no identification of nonmatching physical faces.

For legal NORI3, the combined antipodal-reversal law and separate same-face reversal oddness amount to antipodal invariance \(c(\bar F,\pi)=c(F,\pi)\). In (1) this holds precisely when \(h_j(\pi)=h_{n-3-j}(\pi)\). This defines a substantial subclass of boundary-compatible NORI3 allowing arbitrary nonlinear dependence on all \(n-3\) exterior coordinates. The sparse-triplewise-support theorem cannot address this subclass when the essential exterior support is full.

## Partial layered tournament and selective terminal-pair robustness

For \(j\in\{0,\ldots,n-3\}\), call an unordered direction triple \(T\) *rank-flat at layer \(j\)* if, for all six orderings of \(T\), the physical ordered-face color is identical over all exterior assignments with exactly \(j\) ones. Write \(B_j\) for the family of triples that are **not** rank-flat at layer \(j\). On rank-flat triples, define the constant chart \(h_j\); due to same-face reversal oddness this is a partial boundary tournament. Unavailable triples receive no orientations. For formal use beyond physical layer \(n-3\), extend charts arbitrarily to complete reversal-odd tournaments; no geodesic with distinct directions uses these extra layers.

For an unordered direction pair \(e\), define its maximal *rank-nonflat codegree*
\[
\beta(e)=\max_{0\le j\le n-3}\bigl|\{w\notin e:e\cup\{w\}\in B_j\}\bigr|.
\]
Fix \(b\ge0\). Call \(e\) *clean* if \(\beta(e)\le b\), and let \(\alpha\) be the proportion of clean pairs among all \(\binom n2\) unordered pairs.

**Theorem (selectively pruned layered snake).** If \(L_{\max}(c)\) is the maximum length of a monochromatic direction-distinct cube geodesic, then
\[
\boxed{\alpha\frac{n-1}{2}\le (L_{\max}(c)-1)^2+b(L_{\max}(c)-1).}
\tag{2}
\]
The estimate remains true without imposing antipodal invariance, but requires same-face reversal oddness.

**Proof.** Define positive paths by their consecutive *rank-flat* triples, using chart \(h_{i-1}\) at window starting position \(i\). Every such distinct-direction path is a genuine physical monochromatic cube geodesic when traversed from \(0^n\), because its \(i\)-th window has exterior Hamming weight \(i-1\). Let \(L_+\le L_{\max}(c)\) be their maximum order.

For **clean** unordered terminal pairs \(e\), orient \(e\) by its maximum positive simple terminal-path order \(r(e)\), as in the abstract proof (paths may use dirty pairs elsewhere). The clean-pair graph has \(\alpha\binom n2\) oriented edges, so some vertex \(v\) has at least \(\alpha(n-1)/2\) incoming clean edges. Partition these neighbors into \(U_r\), with \(q=|U_r|\), by maximum terminal-path order \(r\).

For \(u,w\in U_r\), use rank-\(r-2\) chart \(h_{r-2}(u,v,w)\) to orient \(u\to w\) whenever the triple \(\{u,v,w\}\) is rank-flat at that layer. Since each pair \(\{u,v\}\) is clean, it is incident to at most \(b\) missing comparisons at this layer. Thus this partial tournament on \(U_r\) has at least \(q(q-1-b)/2\) arcs, and some \(u\) has outdegree at least \((q-1-b)/2\). As before, each comparison outneighbor must already occur on a longest \(r\)-vertex positive path ending \(u,v\), or appending it contradicts the maximal terminal order of the **clean** pair \(\{v,w\}\). Therefore \(q\le2r+b-3\). Summation yields
\[
\alpha(n-1)/2\le (L_+-1)^2+b(L_+-1)
\le (L_{\max}(c)-1)^2+b(L_{\max}(c)-1).
\]
This proves (2). Setting \(\alpha=1\) yields the explicit robust bound
\[
L_{\max}(c)\ge1+\frac{\sqrt{b^2+2(n-1)}-b}{2}.
\]
In particular \(b=O(\sqrt n)\) still forces \(L_{\max}=\Omega(\sqrt n)\), with arbitrary physical exterior dependence on the exceptional triple faces.

## Consequential obstruction for hypothetical logarithmic boundary-compatible colorings

Rearrange (2):
\[
\boxed{\frac{\#\{e:\beta(e)\le b\}}{\binom n2}
\le \frac{2((L_{\max}-1)^2+b(L_{\max}-1))}{n-1}.}
\tag{3}
\]
If a family of *boundary-compatible* legal physical NORI3 colorings has \(L_{\max}=O(\log n)\), then for **every** threshold \(b(n)=o(n/\log n)\), (3) implies
\[
\#\{e:\beta(e)\le b(n)\}=o(n^2).
\]
In words: for all but \(o(n^2)\) unordered direction pairs \(e\), there must be **some exterior Hamming-weight layer**, potentially depending on \(e\), at which more than \(b(n)\) choices of third direction yield genuinely rank-nonflat physical triples. For instance one may take \(b(n)=n/(\log n\log\log n)\). Thus any logarithmic obstruction preserving boundary tournaments must have **widely distributed identity-sensitive exterior dependence**, rather than merely global dependence on the number of exterior ones or sensitivity concentrated around a few pairs. This necessity does NOT construct such an obstruction or resolve unrestricted boundary-compatible NORI3.

## Several exterior coordinate types

If the directions are partitioned into \(t\) classes and the colors of faces with three free directions in each class depend on exterior bits only through **counts of ones per class**, choose the largest class \(D\), with \(m\ge\lceil n/t\rceil\). A cube geodesic starting at \(0^n\) using only \(D\) leaves other classes at exterior count zero and increases the active class exterior count by one at every triple window. The abstract layer theorem applied to \(D\) gives a genuine monochromatic path of length
\[
\boxed{1+\sqrt{(\lceil n/t\rceil-1)/2}}.
\]
This again permits dependence on arbitrarily many exterior bits.

**Attribution and scope.** The complete boundary-tournament terminal-pair snake bound is the Devine–Milans scrapbook result. The layer-varying extension, the physical rank-homogeneous transfer, the selectively pruned layer-defect inequality, and the dense rank-nonflatness necessity are proved here. The independent sparse-support \(\Omega((n/d)^{1/3})\) result covers a different class. No claim of a universal square-root bound for fully arbitrary physical boundary-compatible NORI3 is made.

### Generic full geodesics in physical boundary-compatible NORI3 and affine smoothing

# Generic full monochromatic geodesics in physical boundary-compatible NORI3

## Statement and distinction from the deterministic conjecture

A boundary-compatible NORI3 coloring on physical ordered 3-faces of Q_n satisfies BOTH
\[
c(F,(w,v,u))=1-c(F,(u,v,w)),\qquad c(\bar F,(u,v,w))=c(F,(u,v,w)).
\tag{BC}
\]
These imply the ordinary antipodal-reversal NORI law; colors are functions of genuine physical exterior fixed bits, independent of traversing corners.

**Theorem A (uniform nonlinear model).** Sample uniformly from ALL legal boundary-compatible physical ordered-three-face colorings (BC): for each unordered free triple T, each of its three reversal pairs of orders, and each antipodal pair of exterior bit assignments, choose one independent fair bit, extending by BC. For n>=20 and every FIXED prescribed binary word w of length n-2,
\[
\Pr[\exists\text{ full antipodal geodesic of window word }w]\ge1-2^{-\varphi(n)/2}.
\tag{A1}
\]
A stronger bound, where \(D_n=\binom n1+\binom n2+\binom n3\), is
\[
\Pr[\text{no full geodesic has word }w]
\le\exp\{-\varphi(n)[1-\tfrac14D_n2^{6-n}]\}.
\tag{A2}
\]
Thus a uniformly random legal boundary-compatible physical coloring has a COMPLETELY MONOCHROMATIC FULL geodesic with probability 1-o(1), allowing arbitrary nonlinear dependence on every exterior coordinate.

**Corollary A3 (all-word universality for prime n).** For prime n tending to infinity, a uniformly random legal boundary-compatible physical coloring, with probability \(1-o(1)\), realizes EVERY one of the \(2^{n-2}\) possible binary window words on full antipodal geodesics. The realizing direction order and starting root may depend on the word.

**Theorem B (adversarial-base affine smoothing).** Fix ANY direction-only boundary 3-tournament \(b(u,v,w)=1-b(w,v,u)\). For every unordered direction triple T and reversal pair of orders choose independently a uniform even-parity vector \(A_{T,\mathrm{orbit}}\) supported on exterior coordinates \(V\setminus T\), using the same vector on reversed orders. Define the real physical face color
\[
c(F,\pi)=b(\pi)\oplus\langle A_{T,\mathrm{orbit}(\pi)},z(F)\rangle.
\tag{B1}
\]
This is legal BC for every choice of the vectors. For n>=15, with probability at least \(1-(0.55)^{\varphi(n)/2}\), there exists ONE complete direction order p such that as the initial cube root x varies, its actual ordered three-face word attains every one of the \(2^{n-2}\) binary words, each by EXACTLY FOUR initial vertices (two antipodal root pairs). This remains true for every adversarial choice of the base boundary tournament b.

No theorem here claims the deterministic square-root lower bound for EVERY exterior-dependent boundary-compatible coloring. The Devine–Milans terminal-pair snake guarantees the square-root bound for ordinary direction-only boundary tournaments; our new results establish that generic exterior dependence, however global, is not itself an obstruction.

## Lemma: independent arithmetic-progression full direction orders

Let n>=5, and for each unit a of Z/nZ set
\[
p^{(a)}=(0,a,2a,\ldots,(n-1)a)\pmod n.
\]
This is a permutation of ALL n cube coordinate directions. Its n-2 consecutive unordered triple windows are three-term arithmetic progressions \(\{j a,(j+1)a,(j+2)a\}\), whose common step is \(\pm a\). Such a three-element set has a UNIQUE middle vertex for a unit a: if a second vertex were its arithmetic midpoint, then \(3a=0\pmod n\), impossible for n>3 when a is a unit. Thus progressions arising from \(p^{(a)}\) and \(p^{(b)}\) can coincide as unordered triples only when \(a=\pm b\pmod n\). Choose one representative a from each pair \(\{a,-a\}\) of units. We obtain \(K=\varphi(n)/2\) FULL direction orders whose unordered consecutive-triple sets are PAIRWISE DISJOINT. In either of our random models, events depending on the face data of these respective orders are consequently independent.

## Proof of Theorem A: complete physical-face second moment and Janson bound

Fix one full direction order p and one target word w of m=n-2 bits. Starting at a cube vertex x and traversing the n distinct directions in p order gives a true full antipodal geodesic. Because of BC antipodal invariance, starts x and \(\bar x\) give IDENTICAL window words in the same order p. Select one representative x from each of the \(M=2^{n-1}\) antipodal root pairs.

For each such x, let \(I_x\) indicate that its full geodesic has word w. Distinct window positions use distinct unordered triples, so their sampled physical face-orbit bits are independent. Therefore
\[
\Pr(I_x=1)=2^{-m},\qquad Z=\sum_xI_x,\qquad \mathbb EZ=M2^{-m}=2.
\tag{A4}
\]
For two different root orbits x,y, write \(\delta=x\oplus y\). At window T_i, both roots query the SAME independent underlying face-orbit bit exactly when their exterior assignments agree or are complementary:
\[
\operatorname{supp}(\delta)\subseteq T_i
\quad\text{or}\quad
\operatorname{supp}(\bar\delta)\subseteq T_i.
\tag{A5}
\]
Let t(delta) count such windows. Since the two roots request the same prescribed word w, all shared requirements agree. Independence over distinct free triples yields
\[
\Pr(I_x=I_y=1)=2^{-2m+t(\delta)}.
\tag{A6}
\]
For distinct antipodal root pairs neither delta nor its complement is empty. If both supports have size >=4, t=0; otherwise only triple windows containing the support of at most three directions can match. Any one, two, or three fixed distinct coordinate directions belong together to at most three, two, or one sliding triple windows, respectively. Hence t<=3. For any x, there are at most \(D_n=\sum_{j=1}^{3}\binom nj\) other antipodal root pairs with t>0.

Thus
\[
\mathbb EZ^2
\le2+M(M-1)2^{-2m}+7MD_n2^{-2m}
<6+7D_n2^{3-n}<8\quad(n\ge20).
\tag{A7}
\]
By the second-moment inequality \(\Pr(Z>0)\ge(\mathbb EZ)^2/\mathbb EZ^2\ge1/2\). For each of the K arithmetic-progression orders above, this event uses an entirely disjoint collection of independent random triple variables. The K success events are independent, giving
\[
\Pr[\text{word w not realized by any of them}]\le(1/2)^K,
\]
proving (A1).

For the stronger bound, for this fixed order p and target w, recode each orbit bit as a Bernoulli SUCCESS variable for receiving the corresponding target w_i. This is well defined because each unordered triple appears at only one window, and different orbit bits are independent. The root event \(I_x\) is the increasing event that a specified subset of m independent fair success variables are ALL 1. Apply the standard Janson inequality for increasing subgraph/cylinder events: \(\Pr(Z=0)\le\exp(-\mu+\Delta/2)\), where \(\mu=\mathbb EZ=2\) and \(\Delta\) is the sum over ordered distinct dependent root pairs of their joint probabilities. Using (A5)–(A6), the at-most-D_n dependencies per root pair and t<=3 give
\[
\Delta\le M D_n2^{-2m+3}=D_n2^{6-n}.
\tag{A8}
\]
Consequently
\[
\Pr(Z=0)\le\exp[-2+\tfrac12D_n2^{6-n}].
\]
Raise this bound to the K independent full-order trials to obtain (A2). If n is prime, \(\varphi(n)=n-1\). The union bound over ALL \(2^{n-2}\) prescribed words gives
\[
\Pr[\exists\text{ unrealized word}]
\le 2^{n-2}\exp[-(n-1)(1-o(1))]
=\exp[-(1-\ln2-o(1))n]\to0,
\]
proving Corollary A3. All root and face comparisons here use ACTUAL physical exterior assignments and their precise antipodal identifications; the paths always use n distinct coordinates.

## Proof of Theorem B: root-map surjectivity and generic affine row rank

For each ordered face, reversing its free tuple flips the boundary-tournament base bit b but preserves the affine coefficient vector, and complementing its exterior bits leaves the affine correction unchanged because the vector has even parity. Hence (B1) satisfies BC on every physical ordered face.

Fix a full direction permutation \(p_1,\ldots,p_n\), with m=n-2 windows. Let \(T_i=\{p_i,p_{i+1},p_{i+2}\}\). Extend the random exterior coefficient vector for its ordered window by zero coordinates on T_i and call it \(A_i\in\mathbb F_2^n\). Its physical face exterior at step i is \(x\oplus1_{\{p_1,\ldots,p_{i-1}\}}\) outside T_i, when starting at cube root x. Therefore the COMPLETE actual ordered-face word equals
\[
W_p(x)=Ax\oplus\gamma,\quad A=(A_1;\ldots;A_m),\quad
\gamma_i=b(p_i,p_{i+1},p_{i+2})\oplus\langle A_i,1_{\{p_1,\ldots,p_{i-1}\}}\rangle.
\tag{B2}
\]
If A has row rank m, the map \(x\mapsto W_p(x)\) is surjective onto \(\mathbb F_2^m\), so EVERY target word is obtained at exactly \(2^{n-m}=4\) roots. Since A has even-weight rows, those roots form two antipodal pairs. This property does not depend on the chosen base tournament b.

For fixed p, the m independent rows \(A_i\) are uniform on subspaces
\[
H_i=\{u\in\mathbb F_2^n:u|_{T_i}=0,\ \sum_j u_j=0\},\quad\dim H_i=n-4.
\]
Let E be the even-parity hyperplane, \(\dim E=n-1\). For \(|i-j|\ge3\), the sliding triples T_i,T_j are disjoint, and for n>=7 a coordinate remains outside their union. Duality yields \(H_i+H_j=E\): indeed \(H_i^\perp=\operatorname{span}(1,e_{p_i},e_{p_{i+1}},e_{p_{i+2}})\), and the orthogonal spaces for two disjoint triples intersect precisely in \(\operatorname{span}(1)\).

For nonempty J⊆{1,...,m}, the XOR \(\bigoplus_{i\in J}A_i\) is uniform on \(\sum_{i\in J}H_i\). If J has two indices distance >=3, the sum is uniform on E, so the probability of zero is \(2^{-(n-1)}\). Otherwise J lies in some three consecutive index positions; there are at most 4m such J, and their probability of zero is at most \(2^{-(n-4)}\) since at least one \(H_i\) is present. Taking a union bound over all possible nontrivial row dependencies gives
\[
\Pr(\operatorname{rank}A<m)
\le2^m2^{-(n-1)}+4m2^{-(n-4)}
=\tfrac12+4(n-2)2^{-(n-4)}<0.55\quad(n\ge15).
\tag{B3}
\]
So the full-rank probability for ANY fixed full direction order is greater than 0.45. The K=φ(n)/2 arithmetic-progression orders above use disjoint unordered triples and hence independent coefficient vectors. Their row-full-rank events are independent. All fail with probability less than \(0.55^K\). On the complementary event, at least one order realizes ALL window words with exactly four roots each by (B2). This proves Theorem B.

## Relation to established work and open frontier

The deterministic affine change-vector and syndrome framework, including exact root counts and a corank-at-most-one guarantee for one-switch words, already appears in the earlier NORI Subsection *Exact change-vector fibers and affine obstruction certificates*. It is NOT claimed as an original theorem here. This manuscript's distinct contributions are the independent arithmetic-progression full-order packing, the physical antipodal-orbit second moment/Janson results for arbitrary nonlinear BC colorings, and the quantitative adversarial-base random-affine smoothing theorem.

Devine–Milans (supplied *Scrapbook*, “Antisymmetric Tournaments”) proves EVERY ordinary direction-only boundary 3-tournament has a simple positive tight path of order at least \(1+\sqrt{(n-1)/2}\). The fully exterior-dependent physical BC class is larger, and its universal deterministic square-root guarantee is not established by the present results. In particular, random full-geodesic existence does NOT imply existence in adversarial colorings. The theorems show that generic independent global exterior variation promotes rather than obstructs long paths, so any deterministic counterexample must rely on globally correlated exterior behavior.

**Verification.** Independent GF(2) rank simulations verified the order-packing triple disjointness and generic full-row-rank rates on n=9,11,13,15,17,19,21,25 (300 trials each). Independent face-orbit sampling checked the full physical nonlinear model in n=7,8,9,10 (500 trials each). A further exhaustive-root linear-algebra implementation verified the previously known corank-to-switch consequence for 500 random face-affine matrices in every n=5,...,11. These tests supplement, rather than replace, the exact proofs above.

### Endpoint-density snakes and bounded algebraic degree

# Endpoint-density snakes and bounded-degree physical NORI3

Let V be the n>=3 coordinate directions. Assume a binary coloring c(F,(u,v,w)) of genuine ordered physical three-faces satisfies **separate same-face reversal oddness** c(F,(w,v,u))=1-c(F,(u,v,w)). Combined with ordinary NORI antipodal-reversal oddness, this is exactly the boundary-compatible class with antipodal invariance. Antipodal invariance is not needed in our proof.

## Theorem 1: endpoint-density terminal-pair snake

Call an r-direction-distinct rooted cube geodesic *positive* when all r-2 consecutive ordered-three-face windows have color 1. Paths of length two are positive vacuously. A negative geodesic reverses to a positive one along the **same physical faces** under same-face reversal oddness; thus the maximal positive length L is the maximal monochromatic length.

For each unordered pair e={u,v}, define r(e) as the maximum number of coordinate moves in a positive geodesic ending in either ordered terminal pair uv or vu, over all possible starting roots and endpoints. Choose ONE maximizing orientation u_e,v_e. Let G_e be the set of cube endpoints y at which some positive r(e)-move geodesic ends with those ordered directions. Define the average maximizing-terminal endpoint density
\[
\delta=\binom n2^{-1}\sum_{e\in\binom V2}|G_e|/2^n.
\]
Then
\[
\boxed{\delta\,(n-1)/2\le(L-1)^2.}\tag{1}
\]
In particular, if a coloring has a longest monochromatic geodesic of order o(sqrt(n)), then its globally maximizing terminal-pair paths occupy o(1) of endpoint fibers **on average**, for every choice of maximizing orientations.

**Proof.** Orient each unordered coordinate pair e from u_e to v_e. For any cube endpoint y, retain only those arcs e for which y is in G_e. Averaging shows that some y retains at least delta*binom(n,2) arcs, and hence at that y some coordinate v has at least delta*(n-1)/2 incoming arcs. Group these incoming arcs u->v by their GLOBAL terminal maximum r(e)=r, defining U_r.

For u,w in U_r, both their chosen maximal positive geodesics (one ending uv and the other wv) can be realized at the SAME endpoint y. Consider the **single physical face** F_y whose free directions are {u,v,w}, and whose other exterior bits are those at y. Extending the uv path by w creates F_y with free-direction ordering (u,v,w); extending the wv path by u creates EXACTLY THE SAME physical F_y with reversed ordering (w,v,u). By same-face reversal oddness, precisely one of these extensions has color 1. Thus comparisons u->w iff c(F_y,(u,v,w))=1 form an ordinary tournament on U_r.

Choose u of outdegree at least (|U_r|-1)/2 in this tournament, and a positive maximal r-move path ending uv at y. Every outneighbor w MUST already occur among the first r-2 directions of this path; otherwise appending w produces an (r+1)-move positive geodesic ending in pair (v,w) at endpoint y XOR e_w, contradicting the GLOBAL maximum r({v,w})=r. Hence (|U_r|-1)/2<=r-2, or |U_r|<=2r-3. Summing from r=2 to L yields delta*(n-1)/2 <= sum_{r=2}^L(2r-3)=(L-1)^2. Every extension and comparison takes place on actual physical faces; no root or face identification is omitted. QED.

The same observation gives the classical Devine--Milans sqrt(n) snake theorem when colors are direction-only: each maximizing terminal sequence then works at EVERY cube endpoint and delta=1.

## Lemma: root multiplicity for low-degree Boolean equations

If f_1,...,f_t are Boolean polynomial functions on F_2^n of algebraic normal form degree <=d and have one simultaneous root with f_i=1 for all i, then they have at least 2^{max(n-dt,0)} such roots.

**Proof.** The simultaneous-satisfaction indicator P(x)=product_i f_i(x) is a nonzero multilinear Boolean polynomial of degree at most dt (reducing x_i^2=x_i). The classical Reed--Muller minimum-weight lemma asserts that a nonzero degree-at-most-D polynomial on n Boolean variables is nonzero at least 2^{n-D} times when D<=n, and at least once otherwise. An elementary proof writes P(x',x_n)=x_n Q(x')+R(x'). If Q=0 the support is twice the support of nonzero R; if Q!=0, for every x' with Q(x')=1 exactly one of P(x',0),P(x',1) is 1, and deg Q<=D-1. Induction supplies at least 2^{n-1-(D-1)}=2^{n-D} such x'. QED.

## Theorem 2: logarithmic geodesics under arbitrarily dense bounded algebraic degree

Suppose additionally that, for every ordered free triple pi, the color c(F,pi) is a Boolean polynomial of degree at most d in the actual n-3 fixed exterior coordinates of F, with no restriction on WHICH exterior bits appear and no support bound. Then the maximum monochromatic cube geodesic length L satisfies
\[
\boxed{2^{d(L-2)}(L-1)^2\ge(n-1)/2.}\tag{2}
\]
In particular, if d=0 the full sqrt(n) boundary-snake estimate holds; if d>=1 is fixed, then
\[
\boxed{L\ge\big(\log_2n-2\log_2\log_2n-O_d(1)\big)/d.}\tag{3}
\]
Thus arbitrary (possibly dense) affine exterior dependence d=1 forces an (1-o(1))*log_2(n) monochromatic geodesic for EVERY boundary-compatible physical NORI3 coloring. Degree two forces at least (1/2-o(1))*log_2(n). These are lower guarantees only, NOT matching examples; the universal sqrt(n) target remains open.

**Proof.** For every unordered pair e, choose ONE positive maximal r(e)-move direction sequence with the selected terminal orientation, along with one starting cube vertex where it is positive. Keep the direction order FIXED and vary its initial cube vertex x over Q_n. Its r(e)-2 actual physical ordered windows are Boolean functions of x of degree <=d: each exterior face state is x XOR a fixed previously traversed mask, restricted to the face's exterior directions, preserving degree. Their all-positive indicator is nonzero because of the selected successful root, and has degree at most d(r(e)-2). By the lemma, at least 2^{max(n-d(r(e)-2),0)} starting roots make ALL its windows positive. Translating the start x to its endpoint x XOR {all traversed directions} is a bijection. Therefore
\[
|G_e|/2^n\ge2^{-d(r(e)-2)}\ge2^{-d(L-2)}
\]
for EVERY pair e, whence delta>=2^{-d(L-2)}. Substitution in Theorem 1 yields (2). Taking base-two logarithms gives
d(L-2)+2log_2(L-1)>=log_2((n-1)/2),
and (3) follows by bounding the log(L-1) term with 2log log n+O(1), unless L is already greater than 2log n. QED.

## Structural fallout and precise limits

Equation (1) is an all-dimensional physical-root coherence criterion: if globally maximal positive terminal-pair paths have a constant-average density of possible cube endpoints, the Devine--Milans sqrt(n) path bound survives in full physical boundary-compatible NORI3. Failure of such a long-path bound requires significant localization of maximal terminal paths in the endpoint cube, not merely variation of local face colors.

Equation (2) yields a new algebraic-degree obstruction: if an adversarial boundary-compatible family had L=o(log n), its minimal maximum exterior algebraic degree would necessarily diverge. Quantitatively, for L>=3,
\[
d\ge\frac{\log_2((n-1)/2)-2\log_2(L-1)}{L-2}.
\]
This is logically independent of the existing near-linear **essential exterior support** barrier: a degree-1 Boolean function can depend essentially on n-3 exterior variables. The earlier sparse-support results give stronger polynomial paths if few variables are influential, whereas (2) gives nontrivial logarithmic paths when nearly all exterior variables participate but algebraic degree is bounded.

The result uses same-face reversal oddness essentially. It does not establish a universal logarithmic bound for unrestricted NORI3, nor a universal sqrt(n) bound for all boundary-compatible physical NORI3; a counterexample to the latter might already have degree one unless some further argument excludes it. The theorem provides a rigorous quantitative target for such an argument.

**Attribution:** The original complete boundary-tournament square-root terminal-pair count is due to Devine--Milans (supplied Scrapbook). The Boolean minimum-weight lemma is the classical Reed--Muller fact. The new mathematics is the endpoint-density lift to actual cube faces and its root-multiplicity transfer to globally supported low-degree exterior colorings.

**Checks:** Direct exhaustive evaluation of randomly generated legal affine boundary-compatible physical colorings in dimensions n=4,5,6 verified the endpoint-density inequality and the root-multiplicity claim, using actual physical exterior-bit evaluation. The proofs do not depend on these computations.

## Corollary: cube-translation symmetry and global coefficient rank restore square-root paths

Let H be a subgroup of the F_2^n translation group acting on Q_n. Suppose c(F+h,pi)=c(F,pi) for EVERY actual physical ordered face and h in H. Translating a globally maximizing positive terminal-path witness for any unordered pair e by all h in H preserves its positive colors and terminal order, while producing |H| DISTINCT ending cube vertices. Consequently the maximizing-endpoint density obeys delta>=|H|/2^n. The endpoint-density theorem gives
\[
\boxed{L\ge1+\sqrt{|H|(n-1)/2^{n+1}}.}
\]
If H has codimension at most t, this becomes
\[
\boxed{L\ge1+\sqrt{(n-1)/2^{t+1}}.}
\]
The coloring may be nonlinear and dependent on all exterior bits, provided its action under H is precisely invariant.

For a boundary-compatible affine physical coloring, express each ordered three-face color as b_pi+<A_pi,z(F)> with the coefficient vector A_pi extended by zero on the three free directions. If the linear span of ALL A_pi over every free triple and order has dimension t, take H=(span{A_pi})^perp. Every h in H preserves all physical face colors under translation, since <A_pi,h>=0. Thus the bound above applies: bounded GLOBAL exterior coefficient rank forces Omega(sqrt n) geodesics, even if individual coefficient vectors are dense and there is no bounded common coordinate support. This is a distinct condition from the support-size hypothesis; the general affine-degree-one guarantee remains logarithmic when the global coefficient rank is unbounded.

Proof uses exactly the same physical-fiber translation for every window, not just the abstract ordered direction triples. It does not settle square-root paths for arbitrary affine or nonlinear boundary-compatible colorings.


### Coupled chronological saddle potentials and checkerboard obstructions

# Coupled chronological saddle potentials and checkerboard obstructions

## 1. An exact simultaneous-compatibility criterion

Let \(A=\{a_1,\dots,a_p\}\) and \(B=\{b_1,\dots,b_q\}\) be the parts of an edge-ordered complete bipartite graph, with \(p=q\) or \(p=q+1\). Write \(w(a,b)\) for the distinct numerical ranks of its edges. For an ordering \(A^\ast=(a_1,\dots,a_p)\) and \(B^\ast=(b_1,\dots,b_q)\), define
\[
F(A^\ast,B^\ast)=\sum_{j=1}^{q}\sum_{i=1}^{j}w(a_i,b_j).
\tag{1}
\]

**Theorem 1 (coupled chronological saddle).** The interleaved spanning path
\[
a_1,b_1,a_2,b_2,\dots,a_q,b_q
\quad (p=q),
\qquad
a_1,b_1,\dots,a_q,b_q,a_{q+1}
\quad (p=q+1)
\]
has strictly increasing edge ranks if and only if \(A^\ast\) is an adjacent-transposition local **minimum** of \(F(\cdot,B^\ast)\) and \(B^\ast\) is an adjacent-transposition local **maximum** of \(F(A^\ast,\cdot)\).

**Proof.** Swapping \(a_i,a_{i+1}\), \(1\le i<p\), changes (1) by
\[
\Delta_{A_i}F=w(a_{i+1},b_i)-w(a_i,b_i).
\tag{2}
\]
For \(p=q\), the relevant indices end at \(q-1\); for \(p=q+1\) they end at \(q\). Swapping \(b_i,b_{i+1}\), \(1\le i<q\), changes (1) by
\[
\Delta_{B_i}F=w(a_{i+1},b_i)-w(a_{i+1},b_{i+1}).
\tag{3}
\]
Because all edge weights are distinct, the first local-optimality requirement is precisely \(w(a_i,b_i)<w(a_{i+1},b_i)\), and the second is precisely \(w(a_{i+1},b_i)<w(a_{i+1},b_{i+1})\). Together they are *all* consecutive edge inequalities for the displayed interleaving, with the correct endpoint convention in either parity. \(\square\)

Thus the two chronological tournament constraints admit an exact **pure local saddle** formulation on two permutation spaces. The existing chronological theorem for transitive tournaments guarantees the minimizing half for each fixed \(B^\ast\); the simultaneous maximizing half is the missing coupling. The four-vertex example in *Endpoint-tournament factorization and monochromatic orders* shows that an arbitrary edge order need not possess such a local saddle for a spanning interleaving.

The criterion uses only ranks of edges between \(A\) and \(B\) and makes no assumption on edges within the two parts. It therefore transfers directly to the edge-order-generated ordinary boundary 3-tournament on an interleaving of those directions. For physical cube three-faces the transfer is valid for direction-only colors, where every exterior fiber has the same chart.

## 2. Threshold chain graphs and the two-by-two obstruction

Call a \(2\times2\) submatrix of the weight matrix **checkerboard-obstructed** when the two entries on one diagonal are both smaller than the entries on the other diagonal. This includes the symmetric case with the roles of the diagonals reversed. Equivalently, its two smallest edges are disjoint. An initial edge segment is its set of smallest \(t\) edges, and a **chain graph** means a bipartite graph with nested neighborhoods on either side, equivalently no induced \(2K_2\).

**Proposition 2 (chain-prefix equivalence).** An edge ordering of a complete bipartite graph has no checkerboard-obstructed \(2\times2\) rectangle if and only if every initial edge segment is a chain graph.

**Proof.** If such a rectangle exists, take the initial segment ending with the larger of its two smaller, disjoint edges. On the four selected vertices the prefix induces exactly two disjoint edges. Conversely, an induced \(2K_2\) in any prefix consists of the two diagonal edges of a \(2\times2\) rectangle, both preceding its crossed edges; the rectangle is obstructed. \(\square\)

On an obstructed \(K_{2,2}\), no alternating spanning path has strictly increasing ranks: the first and last edges in any three-edge path are disjoint, hence constitute one diagonal; its middle edge belongs to the other diagonal.

## 3. A hereditary minimax connector lemma

**Theorem 3 (row-maximum / column-minimum pivot).** Let \(M\) be a real matrix whose every \(2\times2\) submatrix is checkerboard-free. There exists an entry \(M_{ab}\) which is simultaneously a maximum in row \(a\) and a minimum in column \(b\). The same conclusion holds in every nonempty submatrix.

**Proof.** Put
\[
\alpha=\min_a\max_b M_{ab},
\qquad
\beta=\max_b\min_a M_{ab}.
\]
The elementary minimax inequality gives \(\beta\le\alpha\). Suppose \(\beta<\alpha\), and choose \(\beta<t<\alpha\). Make a bipartite graph of entries \(M_{ab}\le t\). Every column has at least one neighbor, because its minimum is at most \(\beta\), whereas every row has at least one nonneighbor, because its maximum is at least \(\alpha\). By Proposition 2 this graph is \(2K_2\)-free. Its column neighborhoods are nested; their smallest member is nonempty, so any row in that neighborhood belongs to *every* column neighborhood. This contradicts the nonneighbor in every row. Thus \(\alpha=\beta\). A row attaining its row maximum \(\alpha\) and a column attaining its column minimum \(\beta\) intersect in an entry that is both. Heredity of the forbidden-rectangle hypothesis proves the same statement for every submatrix. \(\square\)

With distinct edge ranks this pivot \((a,b)\) gives, for any remaining \(a'\ne a,b'\ne b\), an increasing three-edge connector
\[
b' \;-\; a \;-\; b \;-\; a',
\qquad
w(a,b')<w(a,b)<w(a',b).
\tag{4}
\]
The missing step is **global compatibility**: choosing successive pivots and their connectors without reusing vertices or reversing the chronology of earlier edges. The following open problem is a natural exact test of the mechanism.

**Chain-prefix Hamilton conjecture (OPEN).** Every edge ordering of \(K_{m,m}\) in which every initial edge segment is a chain graph has a strictly increasing alternating Hamilton path. The assertion concerns the complete spanning path; Theorem 3 proves only the hereditary local pivot property.

As finite evidence, exhaustive enumeration of all \(6!\) orders of \(K_{3,2}\) identifies exactly 264 checkerboard-free orders; all have an increasing alternating spanning path beginning and ending in the larger part. Enumeration of all \(9!\) orders of \(K_{3,3}\) identifies exactly 30,240 checkerboard-free orders; all have an increasing alternating spanning path. These finite checks establish **no** general Hamilton theorem.



## 6. A full-class path/defect reduction

Let \(h\) be any ordinary boundary 3-tournament on \(N\) vertices (with no global-edge-order hypothesis), and let \(p=(p_1,\dots,p_N)\) be a permutation. Define the number of bad windows relative to the target color 1 by
\[
D(p)=\#\{1\le i\le N-2: h(p_i,p_{i+1},p_{i+2})\ne1\}.
\tag{8}
\]

**Lemma 6 (extracting one long path).** If \(D(p)=D\), and \(N-2-D>0\), a positive vertex-simple tight path has order at least
\[
2+\left\lceil\frac{N-2-D}{D+1}\right\rceil.
\tag{9}
\]
**Proof.** The \(N-2-D\) positive windows form at most \(D+1\) consecutive runs. A longest run has at least the displayed number of windows minus two, and a run of \(r\) windows uses exactly \(r+2\) vertices. \(\square\)

**Lemma 7 (packing paths into a low-defect spanning order).** Suppose a hereditary class of ordinary boundary tournaments has a constant \(c>0\) such that every induced instance on \(s\ge1\) vertices admits a positive vertex-simple path on at least \(c\sqrt{s}\) vertices (with one- and two-vertex paths regarded as trivially positive). Then every instance on \(N\) vertices has a permutation \(p\) with
\[
D(p)\le 4\sqrt N/c.
\tag{10}
\]
**Proof.** Greedily remove a positive path from the remaining \(s\) vertices. If its vertex count is \(r\ge c\sqrt s\), then
\[
\sqrt s-\sqrt{s-r}=\frac{r}{\sqrt s+\sqrt{s-r}}\ge c/2.
\]
Consequently at most \(2\sqrt N/c\) blocks are removed. Concatenate their vertex sequences. Every window internal to a block is positive; at most two windows cross each block boundary. Thus \(D\le2(\#\text{blocks}-1)\le4\sqrt N/c\). \(\square\)

**Implication for the full grand-conjecture boundary goal.** The established hereditary square-root path guarantee supplies a spanning permutation with \(D=O(\sqrt N)\). A universal bound \(D=o(\sqrt N)\) for **every** ordinary boundary tournament would, by Lemma 6, force a positive path on \(\omega(\sqrt N)\) vertices, improving the universal square-root baseline. Conversely, improving path bounds can be leveraged back into stronger defect bounds by the same greedy packing argument.

The triangular potential (1) applies specifically to globally edge-ordered instances, whereas the defect variable (8) is meaningful in the **full** ordinary boundary class. Their relationship is a candidate direction for research, not an asserted transfer to unrestricted NORI1: the latter requires independent physical-edge and root-fiber compatibility.

## Status and significance

Theorems 1, 3, 4, Propositions 2, 5 and Lemmas 6–7 are proved with exact hypotheses; the chain-prefix Hamilton conjecture remains OPEN. This package isolates a joint local-saddle mechanism, a genuine four-local obstruction, a probabilistic barrier to extracting clean submatrices, and a quantitative route by which stronger coupling could improve the full ordinary-boundary lower bound. No theorem here settles unrestricted NORI1 or the Hamilton/long-path problem for every ordinary boundary 3-tournament.
