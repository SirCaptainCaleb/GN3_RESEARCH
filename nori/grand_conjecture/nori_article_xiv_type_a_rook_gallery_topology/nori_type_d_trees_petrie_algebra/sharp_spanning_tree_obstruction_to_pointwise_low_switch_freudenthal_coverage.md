# Sharp spanning-tree obstruction to pointwise low-switch Freudenthal coverage

# Sharp spanning-tree obstruction to pointwise low-switch Freudenthal coverage

This subsection gives an all-dimensional obstruction to a pointwise version of the multi-root Freudenthal chain strategy. The construction applies to unrestricted antipodally odd colorings, simultaneously handles every cube root, and has a sharp parity distinction. It does not obstruct the existence of a favorable complete path at some other simplex.

Identify the vertices of \(Q_n\) with subsets \(S\subseteq[n]\), \(n\ge3\), and work in the geometric cube \(I^n\). A point \(z\in(0,1)^n\) is *generic for all rooted Freudenthal triangulations* if
\[
t_i=2z_i-1\ne0,\qquad |t_i|\ne|t_j|\quad(i\ne j).
\]
For each root \(x\subseteq[n]\), the point \(z\) belongs to the relative interior of a unique maximal simplex of the rooted Freudenthal triangulation \(T_x\). Let \(P_x(z)\) be the corresponding full dimension-simple antipodal geodesic, starting at \(x\). For a legal edge coloring \(c\), define
\[
M_z(c)=\min_{x\subseteq[n]}\operatorname{sw}_c(P_x(z)).
\tag{1}
\]

**Theorem 1 (sharp maximal pointwise minimum).** For every generic interior point \(z\) and every \(n\ge3\),
\[
\boxed{\max_{\substack{c:E(Q_n)\to\mathbb F_2\\c(Ae)=1+c(e)}}M_z(c)=
\begin{cases}n-1,&n\ {\rm odd},\\n-2,&n\ {\rm even}.\end{cases}}
\tag{2}
\]
For odd \(n\), one legal coloring makes every one of the \(2^n\) selected geodesics fully alternating. For even \(n\), one legal coloring makes each selected geodesic fully alternating except possibly at one comparison; every legal coloring has at least one selected geodesic with at most \(n-2\) switches.

*Proof.* The signed permutation group of the cube acts transitively on the open chambers defined by the hyperplanes \(t_i=0\) and \(t_i=\pm t_j\). It preserves antipodal oddness, rooted Freudenthal simplices, and switch counts. It therefore suffices to choose a generic \(z\) with
\[
-1<t_n<t_{n-1}<\cdots<t_1<0,\quad
|t_1|<\cdots<|t_n|.
\tag{3}
\]
For any root \(x\), the rooted signed distances are
\(d_i^x(z)=(1+(-1)^{x_i}t_i)/2\). The decreasing-distance order first takes the indices with \(x_i=1\), in decreasing order, and then the indices with \(x_i=0\), in increasing order. Accordingly,
\[
\boxed{P_x(z):\quad x\longrightarrow\varnothing\longrightarrow[n]\setminus x}
\tag{4}
\]
where the first segment deletes elements of \(x\) in decreasing order and the second adds elements of its complement in increasing order. The notation \([n]\setminus x\) is intended for the terminal vertex. The concatenation is a full antipodal geodesic.

Define the spanning tree \(T\) on all subsets \(S\subseteq[n]\) by the edges
\[
\boxed{\{S\setminus\{\max S\},S\},\quad\varnothing\ne S\subseteq[n].}
\tag{5}
\]
Its parent map removes the largest element, so every nonempty vertex has one parent and every path to \(\varnothing\) is unique. Each path (4) lies entirely in \(T\). The graph distance from \(\varnothing\) to \(S\) in this tree is \(|S|\).

Assign a preliminary edge bit \(b\) to a tree edge with upper vertex \(S\ne\varnothing\) by
\[
\boxed{b(S\setminus\{\max S\},S)
=|S|-1+[1\notin S]\pmod2.}
\tag{6}
\]
On a tree branch from \(\varnothing\) whose first edge is in dimension \(i\), the minimum element of every nonempty visited subset remains \(i\), so (6) alternates with depth. Its initial edge bit is zero if \(i=1\) and one if \(i>1\). If \(x\) and its complement are both nonempty, precisely one contains \(1\); therefore the two tree branches through \(\varnothing\) have different incident-edge colors there. Consequently the complete path (4), including its joining comparison at \(\varnothing\), has an alternating color word. If either branch is empty, the other branch alone alternates. Thus
\[
\operatorname{sw}_b(P_x(z))=n-1
\quad\text{for every }x.
\tag{7}
\]

We now enforce legal antipodal oddness. A tree edge whose direction is \(i<n\) has all dimensions above \(i\) absent at both endpoints. Its antipodal edge has all those dimensions present, and hence does not lie in \(T\). A dimension-\(n\) edge, by contrast, always lies in \(T\), as does its antipodal mate. Write its upper endpoint \(S=R\cup\{n\}\), where \(R\subseteq[n-1]\). The mate has upper endpoint \(S'=([n-1]\setminus R)\cup\{n\}\). Formula (6) gives
\[
\begin{aligned}
b(S)+b(S')
&=|R|+|[n-1]\setminus R|+
 [1\notin R]+[1\in R]\\
&=n\pmod2 .
\end{aligned}
\tag{8}
\]
For odd \(n\), the tree labeling is already antipodally odd on all pairs lying within \(T\). Extend it to the other edge orbits by giving each non-tree mate the complementary bit, and choose arbitrary complementary bits on pairs outside the tree. This gives a legal coloring realizing \(M_z(c)=n-1\).

For even \(n\), the top-direction pairs in the tree initially have equal bits. In each such pair, flip the bit of precisely one edge. All other preliminary tree bits can be retained and extended antipodally as above. For every selected path (4), direction \(n\) is traversed as its first edge when \(n\in x\), and as its last edge when \(n\notin x\). Thus the repair changes at most the first or last word bit. Starting from an alternating word, this can destroy at most one switch, so every selected path has at least \(n-2\) switches. It follows that \(M_z(c)\ge n-2\) for this legal coloring.

It remains to show that in even dimensions every legal coloring has a selected path with at most \(n-2\) switches. Suppose instead that all paths (4) have \(n-1\) switches. Put \(a_i=c(\{\varnothing,\{i\}\})\). Every ascending tree branch \(\varnothing\to S\), \(S\ne\varnothing\), is the terminal segment of the selected path with root \([n]\setminus S\); therefore its edge colors alternate. Every tree edge with upper endpoint \(S\) is consequently forced to have
\[
c(S\setminus\{\max S\},S)
=a_{\min S}+|S|-1\pmod2.
\tag{9}
\]
For each \(i>1\), the selected path with root \(\{i\}\) passes through \(\varnothing\), then begins the complementary branch with first direction \(1\). Alternation at this join forces \(a_i\ne a_1\). Hence \(a_i=a_1+1\) for all \(i>1\). Applied to antipodal top-direction edges, formula (9) now gives
\[
c(e)+c(Ae)=n\pmod2=0
\]
for even \(n\), contradicting antipodal oddness. Thus some selected path has at most \(n-2\) switches. Combining the bounds proves (2). \(\square\)

**Corollary 2 (unbounded failure of pointwise low-switch coverage).** For a legal coloring \(c\), let \(K_x^{[r]}\) be the switch-filtered rooted prefix complexes of Article XIV and set
\[
U^{[r]}=\bigcup_{x\in Q_n}|K_x^{[r]}|.
\]
For every generic \(z\), one can choose \(c\) so that
\[
\boxed{z\notin U^{[r]}\quad\text{whenever}\quad
\begin{cases}
r<n-1,&n\text{ odd},\\
r<n-2,&n\text{ even}.
\end{cases}}
\tag{10}
\]
In particular a fixed switch allowance, independent of dimension, cannot make these complexes cover every interior chamber, even when all roots are included.

*Proof.* Every generating prefix of length less than \(n\) belongs to the boundary of the geometric cube, since some dimension remains fixed. For a generic interior point \(z\), the only maximal rooted Freudenthal simplex containing it is the one encoded by \(P_x(z)\). Hence \(z\in K_x^{[r]}\) if and only if \(P_x(z)\) has at most \(r\) switches. Apply Theorem 1. \(\square\)

**Consequences for the chain-level proof search.** The type-\(B_n\) chamber geometry does not admit a pointwise low-switch root selector, even for an unrestricted *legal* edge coloring with all roots available. One must therefore avoid any proposed Wu--Yang chain map whose existence requires an everywhere-defined, bounded-switch Freudenthal simplex containing the source point. The theorem leaves open the desired global existence of some favorable complete geodesic, and remains compatible with the dimension-simple prefix and multi-root Čech constructions that use relative rather than pointwise coverage. The tree (5) is the intrinsic explanation of this sharp obstruction; no auxiliary graph-class conjecture is introduced.
