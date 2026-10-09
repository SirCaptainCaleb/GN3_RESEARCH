# Doubling, complementary reachability, and geodesic splicing

# Complementary monochromatic reachability and two-window splicing

Write \(c(F,\pi)\in\mathbb F_2\) for an antipodal-reversal-odd coloring of physical ordered three-faces of \(Q_n\), so \(c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi)\). Any directed geodesic has its actual consecutive three-face colors. A monochromatic directed geodesic is one whose entire window word has a constant bit, of either color. The difficulty with joining arbitrary monochromatic branches is that their junction creates two new ordered-three-face windows.

## The exact two-tail extraction theorem

For two distinct directions \(a,b\), let \(D=[n]\setminus\{a,b\}\). Define the *color-free terminal reachability family*
\[
\mathcal R_{(a,b)}(x)=\left\{U\subseteq D,\ |U|\ge1:
\begin{array}{l}
\exists\text{ a monochromatic directed geodesic from }x\\
\text{with direction order }(u_1,\ldots,u_s,a,b),\\
\{u_1,\ldots,u_s\}=U
\end{array}\right\}.
\]
The monochromatic bit is deliberately forgotten; the ordered two-direction terminal memory is retained.

**Theorem 1 (exact grand equivalence).** A full antipodal geodesic with at most one ordered-three-face color change exists if and only if for some common root \(x\), some ordered pair \((a,b)\), and nonempty complementary supports \(U,V\subseteq D\),
\[
U\sqcup V=D,\qquad
U\in\mathcal R_{(a,b)}(x),\quad
V\in\mathcal R_{(b,a)}(x).
\tag{1}
\]

**Proof.** Suppose (1) holds, and choose two monochromatic \(x\)-rooted witnesses with direction words
\[
A=(u_1,\ldots,u_s,a,b),\qquad
B=(v_1,\ldots,v_t,b,a),
\]
of colors \(q,r\), respectively. Antipodal reversal of \(B\) begins at
\[
\overline{x\oplus(V\cup\{a,b\})}=x\oplus U,
\]
has direction word \((a,b,v_t,\ldots,v_1)\), and has all window colors \(1+r\). Retain the first \(s\) moves of \(A\), ending at \(x\oplus U\), and then follow this reversed \(B\). The concatenation is a full path changing each coordinate once. Its first \(s\) ordered-face windows are precisely those of \(A\), and its last \(t\) are precisely those of the reversed \(B\). Since \(s+t=n-2\), these blocks exhaust every window and have word \(q^s(1+r)^t\), containing at most one change.

Conversely, let \(P\) be a good full order \((p_1,\ldots,p_n)\) from root \(x\). Choose a cut between positions \(s\) and \(s+1\) in the \(n-2\) window word where both nonempty sides are constant; if \(P\) is monochromatic any interior cut works. Set \(a=p_{s+1},b=p_{s+2}\), \(U=\{p_1,\ldots,p_s\}\), and \(V=\{p_{s+3},\ldots,p_n\}\). The initial \((s+2)\)-move subpath with terminal directions \((a,b)\) is monochromatic, witnessing \(U\in\mathcal R_{(a,b)}(x)\). Reversing and antipodally complementing the terminal subpath gives an \(x\)-rooted monochromatic witness ending in \((b,a)\) with support \(V\). These supports are nonempty, disjoint, and complementary. \(\square\)

The proof works for ordered \(k\)-faces with a common terminal memory of \(k-1\) directions. The two-tail overlap (1) is therefore a faithful, color-free target for a topological or combinatorial proof of NORI.

## Why direct cube doubling requires care

Let \(b\) be any binary coloring of ordered three-faces of \(Q_n\), and introduce a new coordinate \(g\). On faces omitting \(g\), color the lower facet by \(b(F,\pi)\) and the upper by
\[
1+b(\bar F,\operatorname{rev}\pi).
\]
Choose values on \(g\)-containing faces in complementary antipodal-reversal pairs. This defines a legal NORI coloring of \(Q_{n+1}\). The reversal and physical complementation in the upper formula are both necessary.

Suppose \(b\) is reversal-blind, \(b(F,\operatorname{rev}\pi)=b(F,\pi)\), and a monochromatic full doubled geodesic crosses \(g\) once. After decoding its lower and upper portions into a full path in \(Q_n\), the windows lying completely on the two sides have constant complementary colors. At their splice exactly two three-direction windows remain uncontrolled. With long flanks the resulting word may be
\[
(1+q)^{\,t},z_1,z_2,q^{\,s},
\]
which can have three changes, for example when \((z_1,z_2)=(q,1+q)\). Without reversal-blindness even the decoded upper-flank colors need not be controlled. Thus the direct edge-color doubling argument does not automatically establish the ordered-three-face NORI conjecture. This is a precise two-window obstruction, not a counterexample to the grand assertion.

## Codimension-two cap rigidity

Fix a set \(U\) of \(n-2\) directions, with omitted directions \(a,b\), and a projected root \(r\) on \(U\). For \(i\in U\) define physical cap bits
\[
A_i=c(F(r;\{a,b,i\}),(a,b,i)),\qquad
B_i=c(F(r;\{a,b,i\}),(b,a,i)).
\]
Because \(a,b\) are free on those physical faces, these bits are the same across the four parallel \(U\)-facets.

If a monochromatic \(U\)-spanning geodesic of color \(q\) begins with direction \(i\) and ends with \(j\), inspect completions by placing the two missing directions in either order at the beginning or end. Under hypothetical failure of grand closure, all these completions must fail. The first cap must then be stable and agree with \(q\): \(A_i=B_i=q\); the terminal cap must be stable and opposite: \(A_j=B_j=1+q\). Otherwise one of the full completions has at most one change. Accordingly, the *color-free* graph on \(U\) whose edges join witnessed first and last directions in any of the four facets must be bipartite across the stable cap classes. An odd cycle or an unstable incident direction certifies grand closure.

This cap criterion is a positive extraction theorem conditional on near-spanning monochromatic witnesses. Such witnesses need not exist in a prescribed \(U\)-facet; valid NORI colorings can make the whole four-facet near-spanning memory graph empty. Hence a global proof must force either the complementary two-tail reachability coincidence (1) or sufficiently rich compatible near-spanning cores. Current local cap rigidity does not furnish that existence theorem.\n\n## Refined physical reachability\n\nThe exact two-tail closure criterion requires a common root, complementary used-direction supports, and reversed terminal two-direction memories. Monochromatic basin convexity or a Tucker label collision without those witnesses is insufficient. The new subsections establish maximal support bounds, barycentric carrier obstructions, root-profile interface conditions, and exact codimension-two cap compatibilities under this same physical extraction requirement.
