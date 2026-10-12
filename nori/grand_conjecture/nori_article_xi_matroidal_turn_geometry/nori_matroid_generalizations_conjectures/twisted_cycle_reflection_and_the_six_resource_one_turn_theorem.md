# Twisted-cycle reflection and the six-resource one-turn theorem

# Twisted-cycle reflection and the six-resource one-turn theorem

The preceding Subsection establishes that every induced six-vertex ordinary boundary 3-tournament admits at least 36 marked port cocircuits of size seven with port-cycle intersection at most four. We now prove a *re-rooting symmetry of the marked cocircuit itself* that converts this aggregate intersection bound into a **one-turn path theorem**. The symmetry works at every resource length; in larger dimensions it identifies the central-defect obstruction to the same conversion.

## Tail reflection of a resource-simple word

Fix \(m\ge6\), and let \(v=(v_1,\ldots,v_m)\) be an injective word on distinct original vertices. Put
\[
R(v)=(v_1,v_2,v_3,v_m,v_{m-1},\ldots,v_4).
\tag{1}
\]
The twisted closing construction associates to \(v\) a lifted state path
\[
\begin{split}
P_v:\quad
&(v_1,v_2,v_3),(v_2,v_3,v_4),\ldots,
(v_{m-2},v_{m-1},v_m),\\
&(v_{m-1},v_m,v_3),(v_m,v_3,v_2),(v_3,v_2,v_1).
\end{split}
\tag{2}
\]
It has \(m\) transition edges, the last state being the reversal \(J\) of the first. Its projection is a simple odd-monodromy cycle \(C_v\) and \(Y_v=C_v\cup\{p\}\) is a distinguished port cocircuit.

**Theorem 1 (twisted-cycle tail-reflection symmetry).** For every injective word \(v\) of length \(m\ge6\), the words \(v\) and \(R(v)\) define the **same** distinguished port cocircuit:
\[
\boxed{C_{R(v)}=C_v,\qquad Y_{R(v)}=Y_v.}
\tag{3}
\]
Their projected cyclic turn-edge sequences are traversed in opposite order. If \(e_1,\ldots,e_m\) are the successive turn edges of the cycle built from (2), then those of \(R(v)\) are
\[
\boxed{e_m,e_{m-1},\ldots,e_1.}
\tag{4}
\]

*Proof.* Write the nonterminal states of (2) as \(t_1,\ldots,t_{m-2},s_1,s_2\), where \(t_i=(v_i,v_{i+1},v_{i+2})\), \(s_1=(v_{m-1},v_m,v_3)\), and \(s_2=(v_m,v_3,v_2)\). Applying the twisted closing construction to (1) yields the lifted state sequence
\[
t_1,\ Js_2,\ Js_1,\ Jt_{m-2},\
Jt_{m-3},\ldots,Jt_2,\ Jt_1.
\tag{5}
\]
Every transition in (5) is the \(J\)-image of one of the transitions of (2), traversed backward. Applying the quotient map identifies each transition with its \(J\)-image, proving (3) and (4). The word \(R(v)\) is injective because it is a permutation of the same resource set; hence the second traversal is a legal boundary tight-path gallery, not merely an abstract reorientation of an inadmissible walk. \(\square\)

## The terminal-seam exchange identity

For any boundary coloring \(b\), let \(\omega_i=d_b(e_i)\in\{0,1\}\), with the sum of the \(\omega_i\) taken as an integer. The first \(m-3\) edges of (2) are the original tight-path turns, and the final three are closing-seam turns. Define
\[
L=\sum_{i=1}^3\omega_i,\qquad
Z=\sum_{i=4}^{m-3}\omega_i,\qquad
R_0=\sum_{i=m-2}^{m}\omega_i,
\tag{6}
\]
with an empty sum interpreted as zero. Put \(w=\sum_{i=1}^m\omega_i=L+Z+R_0=|X_b\cap Y_v|-1\).

**Theorem 2 (terminal-seam exchange).** The internal and closing switch counts of the two legal words are
\[
\boxed{
s(v)=L+Z,\quad h(v)=R_0,\qquad
s(R(v))=R_0+Z,\quad h(R(v))=L.
}
\tag{7}
\]
In particular,
\[
\boxed{\min\{s(v),s(R(v))\}=Z+\min\{L,R_0\}.}
\tag{8}
\]

*Proof.* The original traversal in Theorem 1 places its internal turn cut immediately after \(e_{m-3}\). The reversed traversal uses the turn order (4); its first \(m-3\) turns comprise old edges \(e_m,\ldots,e_4\), and its last three comprise \(e_3,e_2,e_1\). Counting the nonzero turn labels in these respective intervals gives (7), and taking the minimum gives (8). \(\square\)

When \(w\le3\), the right side of (8) is at most one unless (a) at least two changed turns lie in the central interval \(e_4,\ldots,e_{m-3}\), or (b) there is one central change and one changed turn in each three-edge terminal interval. Thus the sole obstruction to turning **a given low-intersection marked cocircuit** into a one-turn path using its two intrinsic orientations is a central-defect configuration. For \(m=7\) the central interval contains a single edge, so only the balanced pattern \((L,Z,R_0)=(1,1,1)\) remains at weight three.

## Universal six-resource one-turn theorem

**Theorem 3 (six-vertex one-turn path in every induced six-set).** Every ordinary reversal-odd boundary 3-tournament on \(n\ge6\) vertices has, in **each induced six-element subset** \(S\), a vertex-simple tight path on all six vertices of \(S\) with at most one change among its four ordered-triple colors.

More quantitatively, at least **18** of the 720 orderings of each \(S\) have at most one internal turn.

*Proof.* The preceding five-cycle density theorem produces at least 36 words \(v\) of each six-subset satisfying
\[
w(v)=|X_b\cap Y_v|-1\le3.
\tag{9}
\]
For \(m=6\), the central interval in (6) is empty, so \(Z=0\). Theorem 2 therefore gives
\[
s(v)=L,\qquad s(R(v))=R_0,\qquad
s(v)+s(R(v))=L+R_0=w(v)\le3.
\tag{10}
\]
Since the switch counts are nonnegative integers, at least one of \(v,R(v)\) has at most one internal turn. The map \(v\mapsto R(v)\) is a fixed-point-free involution on the six-vertex permutation set: it fixes the first three symbols and reverses the order of the last three distinct symbols. By Theorem 1, it preserves the set of words satisfying (9). Pairing the at least 36 favorable words under this involution, at least one word per pair is a one-turn word. Hence there are at least \(36/2=18\) such words. \(\square\)

**Corollary 4 (strengthening the canonical \(q=3\) conjecture in the known range).** For all \(6\le n\le36\), every ordinary boundary tournament has a resource-simple gallery on \(m\ge\max\{6,\lceil\sqrt n\rceil\}\) vertices with **at most one internal turn**. The proof chooses \(m=6\) inside an arbitrary induced six-set; it does not assert this bound for \(n>36\).

## Research consequence

The new reflection shows that the apparent freedom to place switches in the three closing seams is not arbitrary: a single marked cocircuit has two canonical, vertex-simple orientations of the same cycle, and the reflection exchanges its two terminal three-edge intervals. This is a structural property of the boundary gallery language beyond binary matroid orthogonality.

For a marked cocircuit with intersection four, the obstruction to one-turn conversion is now sharply localized to the *central defect* \(Z\) in (6). One can therefore seek a local, resource-preserving adjacent-transposition surgery that reduces \(Z\), or shifts a central changed turn to either terminal interval without increasing the total cyclic weight. A theorem eliminating those central-defect configurations in sufficiently long favorable galleries would strengthen the shared matroid intersection conjecture to produce long one-turn boundary paths. The present theorems prove this mechanism in length six and establish the reflection/central-defect identity in every length; the corresponding growing-length surgery remains open.
