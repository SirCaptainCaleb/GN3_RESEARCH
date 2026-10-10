# Article VII — Seven-coordinate structural and tournament methods

## Article setting and orientation

All-dimensional boundary-tournament altitude transfer: any direction-only boundary 3-tournament with an acyclic line-graph comparison orientation has a monochromatic cube geodesic using n/2^{O(sqrt(log n loglog n))} distinct coordinates, via a global edge order and the Bucić et al. 2020 nearly-linear increasing-path theorem. The transfer exactly preserves original-vertex simplicity and physical face colors. Directed comparison cycles are therefore necessary for shorter-path obstructions in this subclass. See the new Section Subsection; exterior dependence remains unresolved.

Let c color physical ordered three-faces of Q_n. For a direction-distinct path (p_1,...,p_k) rooted at x, let w_j be the color of the actual ordered three-face traversed by (p_j,p_(j+1),p_(j+2)). Exterior-coordinate bits determine the root dependence of these colors.

*Full Article composition: [source manuscript](../nori_article_vii_seven_coordinate.md).*

## Seven-coordinate endpoint constraints and tournament structure

Acyclic boundary-tournament transfer (all dimensions): a direction-only reversal-odd triple coloring whose comparison orientation of L(K_n) is acyclic inherits an edge order on K_n. The Bucić-Kwan-Pokrovskiy-Sudakov-Tran-Wagner increasing-path theorem then yields a monochromatic coordinate geodesic of length n/2^{O(sqrt(log n loglog n))}. The graph path is original-vertex-simple, so every cube direction is distinct. This exact transfer is proved in the new Subsection on nearly-linear monochromatic geodesics. Exterior-dependent comparison orders require a separate coherence principle.

A directed geodesic with direction word \(p_1,\ldots,p_m\) produces a binary word \(w_1,\ldots,w_{m-2}\) of colors of its consecutive physical ordered three-faces. The dependence of \(w_i\) on the initial cube vertex is confined to the coordinates exterior to that face. We exploit this locality to separate endpoint choices from an invariant middle block.

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

# Endpoint-tournament factorization yields monochromatic antipodal geodesics

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
