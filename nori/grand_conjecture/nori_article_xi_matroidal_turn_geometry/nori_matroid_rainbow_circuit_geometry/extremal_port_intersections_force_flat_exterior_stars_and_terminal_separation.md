# Extremal port intersections force flat exterior stars and terminal separation

# Extremal port intersections and exterior-square signatures

Fix \(n\ge4\). Let \(D_n\) be the pointed binary matroid with port \(p\), and let \(X\in Z(D_n;\mathbb F_2)\) contain \(p\). Write \(d(t)=\mathbf1_{\{t\in X\}}\) for turns \(t\) of the folded cube line graph \(H_n\). Its shortest port-cocircuit intersection parameter is
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_n),\ p\in Y,\ |Y|=n+1\}.
\tag{1}
\]
The minimum switch count in full antipodal geodesics of the recovered cube-edge coloring equals \(I(X)-2\). We formulate the finite-face completion constraints of Article X entirely through turn chains and the port-cocircuit intersection parameter.

Let \(F\) be a coordinate face of codimension \(t\), with free-direction set \(D\), exterior-direction set \(T=[n]\setminus D\), and \(1\le|D|,|T|\). For a geodesic \(P=(e_1,\ldots,e_{|D|})\) spanning \(F\), let
\[
A(P)=\{\{[e_j],[e_{j+1}]\}:1\le j<|D|\}\subseteq E(H_n),\qquad
r_X(P)=|A(P)\cap X|.
\tag{2}
\]
Here the projected consecutive edge pairs are turns, and \(r_X(P)\) is their integer support weight. If \(P,Q\) terminate at the same cube vertex \(x\), let \(t_x(P,Q)\in E(H_n)\) be the turn joining their last edges.

**Theorem 1 (port intersection completion and terminal separation).** Let \(P\) span a codimension-\(t\) face, and put \(r=r_X(P)\). Then
\[
\boxed{I(X)\le2+2\left\lfloor\frac{r+t}{2}\right\rfloor.}
\tag{3}
\]
If \(P,Q\) span the same face, end at the same vertex, have \(r_X(P),r_X(Q)\le r\), and \(t_x(P,Q)\in X\), then
\[
\boxed{I(X)\le2+2\left\lfloor\frac{r+t-1}{2}\right\rfloor.}
\tag{4}
\]

*Proof.* The cochain \(d\) reconstructs an antipodally odd edge coloring \(c\), unique up to complementation. Its disagreements between consecutive edges are the labels \(d\), so \(r_X(P)\) is the number of switches along \(P\). Append the \(t\) exterior directions in any order; the resulting path is an antipodal geodesic of \(Q_n\), with at most \(r+t\) switches. The global minimum switch count is even, because cyclic root rotation removes one switch whenever that path has an odd number of switches. It is thus at most \(2\lfloor(r+t)/2\rfloor\). The identity \(I(X)=\mu(c)+2\) gives (3).

For (4), membership \(t_x(P,Q)\in X\) says that the terminal edges of \(P,Q\) have opposite colors. Fix one exterior geodesic \(W\) from \(x\). Its first edge matches the terminal color of one of \(P,Q\); append \(W\) to that path. The seam causes no switch, and the other exterior comparisons contribute at most \(t-1\) switches. Apply the even-minimum reduction and the intersection identity again. \(\square\)

For directions \(i\ne j\) incident at a cube vertex \(y\), write \(d_{ij}([y])\) for the label of their turn in the vertex-star clique of \(H_n=L(G_n)\). All such labels are invariant under replacing \(y\) by its antipode. For \(S\subseteq T\) put \(x^S=x\oplus\sum_{i\in S}e_i\).

**Theorem 2 (forced star-cut pattern on an exterior cube).** Suppose \(P\) spans \(F\), ends at \(x\in F\), and has \(r=r_X(P)\) internal labeled turns. If
\[
\boxed{I(X)\ge r+t+2,}
\tag{5}
\]
then \(r+t\) is even, every completion of \(P\) by an ordering of \(T\) has \(r+t\) switches, and for every \(S\subseteq T\) and distinct \(i,j\in T\),
\[
\boxed{d_{ij}([x^S])=\mathbf1_{\{i\in S\}}+\mathbf1_{\{j\in S\}}\pmod2.}
\tag{6}
\]
In particular, every coordinate square entirely contained in the exterior \(t\)-cube at \(x\) has zero coloring curvature:
\[
\boxed{d_{ij}([x^S])=d_{ij}([x^{S\triangle\{i,j\}}])\qquad
(i,j\in T,\ S\subseteq T).}
\tag{7}
\]

*Proof.* A completion of \(P\) uses each exterior direction once. It has at most \(r+t\) switches, since only \(t\) additional comparisons are introduced. Condition (5), together with \(I(X)-2=\mu(c)\), forces every such completion to have at least \(r+t\) switches. Thus every newly introduced comparison must be a switch. As the minimum of full switch counts is even, \(r+t\) must be even.

Let \(q\in\mathbb F_2\) be the color of the final edge of \(P\). All exterior paths beginning at \(x\) therefore have successive edge colors
\[
1+q,\quad q,\quad1+q,\quad q,\quad\ldots
\tag{8}
\]
in their traversal order. Every exterior cube edge \(\{x^S,x^{S\cup\{i\}}\}\), with \(i\notin S\), occurs as the \((|S|+1)\)-st edge of some such path. Its color is
\[
1+q+|S|\pmod2.
\tag{9}
\]
At a vertex \(x^S\), the exterior direction-\(i\) edge has color \(1+q+|S|\) if \(i\notin S\), and \(q+|S|\) if \(i\in S\). Taking the difference of two such incident edge colors gives (6), independently of the choice of \(q\). Replacing \(S\) by \(S\triangle\{i,j\}\) flips both membership indicators, leaving their sum unchanged; this proves (7). \(\square\)

**Corollary 3 (flat exterior-square exclusions for hypothetical high intersection).** Suppose \(I(X)\ge6\).

(a) Every codimension-two face has no spanning geodesic \(P\) with \(r_X(P)\le1\). If such a face has a spanning geodesic with \(r_X(P)=2\), terminating at \(x\) with exterior directions \(a,b\), then
\[
d_{ab}([x])=d_{ab}([x^{ab}])=0,\qquad
d_{ab}([x^a])=d_{ab}([x^b])=1.
\tag{10}
\]
Consequently its exterior square has zero curvature. No two such low-cost terminal geodesics can have opposite terminal colors, equivalently their terminal-edge turn cannot lie in \(X\).

(b) Every codimension-three face has no monochromatic spanning geodesic. If it has a spanning geodesic with \(r_X(P)=1\) terminating at \(x\), then every exterior vertex star and every exterior square obeys (6)--(7), and no two one-turn terminal geodesics can have their terminal-edge turn in \(X\).

*Proof.* For codimension two, (3) with \(r\le1\) would give \(I(X)\le4\). With \(r=t=2\), Theorem 2 applies because \(I(X)\ge6=r+t+2\), yielding (10). For two such terminal paths, (4) gives \(I(X)\le4\) whenever their final-edge turn lies in \(X\), a contradiction. For codimension three, (3) with \(r=0\) gives \(I(X)\le4\); with \(r=1,t=3\), Theorem 2 gives (6)--(7). The same use of (4) excludes opposite terminal phases. \(\square\)

**Corollary 4 (curvature-positive squares cannot support two-turn terminals).** If \(I(X)\ge6\), fix distinct directions \(a,b\) and a coordinate square \(S\) parallel to them with
\[
d_{ab}([x])\ne d_{ab}([x^{ab}])
\tag{11}
\]
at opposite corners. No geodesic spanning the codimension-two face perpendicular to \(a,b\), terminating at the corresponding corner \(x\), can have only two turns in \(X\).

*Proof.* Such a path would satisfy Corollary 3(a), which forces equality of the two labels in (11). \(\square\)

Equations (6)--(7) transfer the face-completion rigidity of Article X into a phase-free condition on the cycle \(X\): a locally extremal partial turn chain forces the restriction of \(X\) to each exterior star to be the cut separating directions already flipped from directions not yet flipped. Theorem 1 supplies a complementary two-chain certificate for an intersection at most four. These assertions hold for arbitrary port-containing binary cycles, including those which decompose into several dual circuits.
