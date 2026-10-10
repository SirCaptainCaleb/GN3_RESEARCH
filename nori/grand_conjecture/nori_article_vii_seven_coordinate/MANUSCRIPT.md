# Article VII — Seven-coordinate structural and tournament methods

## Article setting and orientation

Let c color physical ordered three-faces of Q_n. For a direction-distinct path (p_1,...,p_k) rooted at x, let w_j be the color of the actual ordered three-face traversed by (p_j,p_(j+1),p_(j+2)). Exterior-coordinate bits determine the root dependence of these colors.

For seven distinct directions (a,b,c,d,e,f,g), fix the initial root bits other than x_d=t. The five window colors have the form

*Full Article composition: [source manuscript](../nori_article_vii_seven_coordinate.md).*

## Seven-coordinate endpoint constraints and tournament structure

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
