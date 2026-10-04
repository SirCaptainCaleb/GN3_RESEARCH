# Direct enumeration of two path covers by finite transfer matrices

Work with an arbitrary finite boundary 3-tournament. Encode vertex-simple tight paths in a finite commutative algebra with one square-zero variable per vertex. Seek a determinant, coefficient, or cancellation identity that forces the spanning two-path coefficient to be positive using boundary reversal. Develop the construction directly on H, with no minimum-counterexample hypothesis.

### Aim

Prove the two-cover statement directly for an arbitrary finite boundary \(3\)-tournament \(H\). The proposed mechanism is an identity for the number of spanning covers, obtained from the local tournament at each middle vertex. The argument uses every vertex of \(H\) together and makes no minimum-counterexample assumption.

The calculations below are finite symbolic derivations. They establish an encoding and a reversal identity; they do not yet establish the required positivity.

### A finite algebra records vertex disjointness

Let \(V(H)=V\), \(|V|=n\ge1\), and use
\[
\mathcal A=\mathbb Q[y_v:v\in V]/(y_v^2:v\in V).
\]
Its basis consists of the \(2^n\) squarefree monomials \(y_S=\prod_{v\in S}y_v\). Thus this is a finite-dimensional algebra. A product of path monomials vanishes whenever their supports intersect.

Let \(\mathcal P(H)\) be the set of all nonempty ordered tight paths, including one- and two-vertex paths, and define
\[
F_H=\sum_{P\in\mathcal P(H)}y_{V(P)}.
\]
Distinct path orders contribute separately.

Then
\[
G_H=F_H+\frac12F_H^2
\]
has nonnegative integer coefficients. Its coefficient at \(y_V\) counts spanning covers by one or two nonempty ordered tight paths, with the collection of paths unordered. Indeed, a surviving term in \(F_H^2\) is a pair of vertex-disjoint nonempty paths. Each unordered pair occurs exactly twice. The first summand counts Hamilton paths.

Consequently
\[
[y_V]G_H>0
\]
is equivalent to \(\operatorname{pc}(H)\le2\). This equivalence is an encoding of the target, not a proof of it.

### A transfer matrix for all tight paths

Index rows and columns by ordered pairs \((u,v)\) of distinct vertices. Put \(a_{uvw}=1\) when \((u,v,w)\) is tight, and \(a_{uvw}=0\) otherwise. Define
\[
T_{(u,v),(v,w)}=a_{uvw}y_v
\]
for pairwise distinct \(u,v,w\), and set all other entries to zero. Define the row \(\alpha\) and column \(\beta\) by
\[
\alpha_{(u,v)}=y_u,\qquad \beta_{(u,v)}=y_v.
\]

Every matrix entry of \(T\) has degree one. Hence \(T^{n+1}=0\), and
\[
(I-T)^{-1}=I+T+\cdots+T^n
\]
is a finite sum.

A term in \(\alpha T^k\beta\) follows a vertex sequence \((v_0,\ldots,v_{k+1})\), with a tight triple at every transition. Its weight is \(\prod_{i=0}^{k+1}y_{v_i}\). Repeated vertices make the weight zero, while every vertex-simple tight path of order \(k+2\) contributes exactly once. Therefore
\[
F_H=\sum_{v\in V}y_v+\alpha(I-T)^{-1}\beta.
\]
The formula also covers \(n=1\), when the ordered-pair index set is empty.

This construction retains original-vertex disjointness; an ordinary walk count on ordered-pair states alone would not do so.

### Boundary reversal becomes a matrix identity

Let \(J\) be the permutation matrix that exchanges \((u,v)\) and \((v,u)\). It satisfies \(J^2=I\) and \(J^{\mathsf T}=J\).

Let \(C\) have entry \(y_v\) at \(((u,v),(v,w))\) for pairwise distinct \(u,v,w\), and zero elsewhere. Boundary reversal gives
\[
T+JT^{\mathsf T}J=C.
\]
At a permitted transition the two entries are
\[
a_{uvw}y_v,\qquad a_{wvu}y_v,
\]
and \(a_{uvw}+a_{wvu}=1\).

More concretely, put \(K=JT\). After grouping states by their first coordinate \(v\), \(K\) is block diagonal. Its \(v\)-block has rows and columns \(u,w\in V-\{v\}\) and entries
\[
(K_v)_{u,w}=a_{uvw}y_v,\qquad u\ne w.
\]
Thus
\[
K_v=y_vA_v,
\qquad A_v+A_v^{\mathsf T}=\mathbf1\mathbf1^{\mathsf T}-I.
\]
The matrix \(A_v\) is the adjacency matrix of the ordinary tournament on \(V-\{v\}\) defined by \(u\to w\) when \((u,v,w)\) is tight. In particular \(K_v^2=0\), hence \(K^2=0\).

Also \(\beta=J\alpha^{\mathsf T}\) and \(T=JK\), so the nonsingleton path polynomial has the equivalent form
\[
q_H:=F_H-\sum_vy_v
=\alpha(J-K)^{-1}\alpha^{\mathsf T}.
\]
Here \(J-K=J(I-T)\) is invertible. The remaining difficulty is to turn these local tournament identities into a global statement about the squarefree coefficient of \(G_H\).

### First attempt: parity

The naive ordered-pair count gives no parity information. Over characteristic two,
\[
F_H^2=0,
\]
because distinct summands cancel in pairs and the square of every nonempty squarefree monomial is zero.

One must retain the unordered count \(\frac12F_H^2\) over the integers before reducing coefficients modulo two, or use an identity that controls its positive integer coefficients. The characteristic-two identity \(F_H^2=0\) neither disproves the conjecture nor supplies a positivity theorem.

### A determinant expression, and its limitation

The matrix determinant lemma, valid here because the coefficient algebra is commutative and \(I-T\) is invertible, gives
\[
q_H=\frac{\det(I-T+\beta\alpha)}{\det(I-T)}-1.
\]
The denominator has constant term one and is a unit in the finite algebra.

This offers a specific next route: seek a determinant expansion or cancellation identity using \(A_v+A_v^{\mathsf T}=\mathbf1\mathbf1^{\mathsf T}-I\) that leaves a positive contribution to \([y_V]G_H\). An expansion must retain the variables \(y_v\), since forgetting them admits walks that repeat original vertices.

No such positivity or cancellation identity has been proved in this pass. The transfer formula, local-tournament decomposition, and parity obstruction are recorded as the starting calculations for this direct counting route. No small-order classification or counterexample-minimality argument is used.


### The denominator enumerates signed tight-cycle families

Let \(\mathcal C(H)\) be the set of vertex-simple directed tight cycles of order at least three, with cyclic rotations identified. Reverse orders are distinct orientations. Define
\[
Z_H=\sum_{C\in\mathcal C(H)}y_{V(C)},\qquad D_H=\det(I-T).
\]

**Calculation.**
\[
D_H=\exp(-Z_H).
\]
All exponential and logarithmic series here terminate in the ideal generated by the \(y_v\).

**Proof.** For a commuting indeterminate \(z\), the determinant derivative identity gives
\[
\frac{d}{dz}\log\det(I-zT)
=-\operatorname{tr}((I-zT)^{-1}T).
\]
The inverse is a finite sum. Integrating coefficient by coefficient and using the constant term one gives
\[
\log\det(I-T)=-\sum_{k=1}^n\frac{\operatorname{tr}(T^k)}k.
\]
A term of the trace follows a closed walk of ordered-pair states. Its weight is the product of the variables for the middle vertices of its transitions. If an original vertex repeats in the corresponding cyclic sequence, the monomial vanishes. Surviving terms therefore correspond precisely to vertex-simple tight cycles. One- and two-step closed walks are excluded by the requirement that every transition triple have three distinct vertices. Each cyclic order of length \(k\ge3\) has \(k\) choices of initial state, so
\[
\frac{\operatorname{tr}(T^k)}k
=\sum_{\substack{C\in\mathcal C(H)\\|C|=k}}y_{V(C)}.
\]
Summing proves \(\log D_H=-Z_H\), hence the formula. \(\square\)

Expanding the exponential gives the concrete interpretation
\[
D_H=\sum_{\mathcal F}(-1)^{|\mathcal F|}y_{\bigcup_{C\in\mathcal F}V(C)},
\]
where \(\mathcal F\) ranges over unordered families of pairwise vertex-disjoint tight cycles, including the empty family. The factor \(1/k!\) in the exponential cancels the \(k!\) orderings of a disjoint family; products of intersecting cycle supports vanish.

Let
\[
N_H=\det(I-T+\beta\alpha).
\]
The previous determinant formula now says
\[
N_H=D_H(1+q_H).
\]
Thus its expansion consists of a disjoint tight-cycle family, optionally accompanied by one ordered tight path of order at least two, with sign \((-1)^{|\mathcal F|}\). This describes the cancellations introduced by the determinant. Invertibility of \(D_H\) provides the formal counting identity, but not positivity of the spanning two-cover coefficient.

### A direct polynomial for every number of paths

Define
\[
B_H(t)=[y_V]\exp(tF_H).
\]
Since \(F_H\) has zero constant term, the exponential is finite. Expanding it proves
\[
B_H(t)=\sum_{\mathcal P}t^{|\mathcal P|},
\]
where \(\mathcal P\) ranges over spanning covers by nonempty ordered tight paths, with the collection unordered. In particular its coefficients are nonnegative integers and its smallest exponent with nonzero coefficient is \(\operatorname{pc}(H)\).

The grand theorem asks for
\[
[t]B_H(t)+[t^2]B_H(t)>0.
\]
This expresses the direct counting target in one global polynomial, without choosing a deletion, a cover of a smaller tournament, or a minimum counterexample.

A tempting shortcut is to replace the exponential by a rank-one determinant perturbation. That cannot count arbitrary numbers of paths: for a scalar \(t\),
\[
\det(I-T+t\beta\alpha)=D_H(1+tq_H),
\]
which is affine in \(t\). The rank-one perturbation records at most one path together with signed cycles. Two-path terms require a further identity rather than the quadratic coefficient of this determinant.

### Using the local tournament symmetry in a quadratic identity

Retain \(K=JT\), set
\[
M=J-K,\qquad U=\alpha M^{-1},
\qquad h_v=\sum_{u\ne v}U_{(v,u)}.
\]
The inverse exists as above.

Since \(q_H=\alpha M^{-1}\alpha^{\mathsf T}\) is a scalar in a commutative algebra, transposition gives
\[
q_H=\alpha(M^{\mathsf T})^{-1}\alpha^{\mathsf T}.
\]
It follows that
\[
2q_H=U(M+M^{\mathsf T})U^{\mathsf T}.
\]
Indeed \(UMU^{\mathsf T}\) and \(UM^{\mathsf T}U^{\mathsf T}\) each equal \(q_H\).

Now
\[
M+M^{\mathsf T}=2J-(K+K^{\mathsf T}),
\]
and the \(v\)-block of \(K+K^{\mathsf T}\) is
\(y_v(\mathbf1\mathbf1^{\mathsf T}-I)\).
Moreover \(U=\alpha(I-T)^{-1}J\), so every nonzero monomial of \(U_{(v,u)}\) contains \(y_u\): it records a transition sequence ending at \((u,v)\), weighted at all vertices except its final \(v\). Hence \(U_{(v,u)}^2=0\). Substitution gives
\[
q_H=UJU^{\mathsf T}-\frac12\sum_{v\in V}y_vh_v^2.
\]

This is an explicit identity that uses boundary reversal, rather than only the path-counting definition. The entries of \(U\) have nonnegative integer coefficients, but the right-hand side is a difference of such contributions. A proof that the needed spanning coefficient remains positive has not emerged from this identity.

### Current direction

The next attempt is to relate the quadratic resolvent identity to the one- and two-path coefficients of \(B_H(t)\), or construct a cancellation rule on the signed path-and-cycle expansion that preserves a positive spanning contribution. Every cancellation must retain original-vertex disjointness.

The cycle expansion, the affine rank-one limitation, and the quadratic identity are established finite calculations. Positivity in degrees one or two remains the unproved step. These developments stay in this open Brainstorm.


### A two-state cut transfer counts all path covers directly

The exponential path-cover polynomial can be replaced by a single finite transfer matrix after adjoining one binary state recording whether the most recent cut is selected. This removes the rank-one determinant limitation at the level of enumeration.

For a spanning ordering
\[
\pi=(v_1,\ldots,v_n),
\]
let its defect line \(L_\pi\) have cut positions \(1,\ldots,n-1\) as vertices and edge \(\{i-1,i\}\) for each non-tight consecutive triple centered at \(v_i\). A subset \(C\subseteq[n-1]\) is a vertex cover of \(L_\pi\) exactly when cutting \(\pi\) at the positions in \(C\) leaves only tight path blocks.

Write
\[
V_{L_\pi}(z)=\sum_{C\text{ vertex cover of }L_\pi}z^{|C|}.
\]
If
\[
B_H(t)=\sum_{k\ge1} c_k t^k
\]
counts spanning covers by \(k\) nonempty ordered tight paths, with the collection of paths unordered, then
\[
\boxed{\quad
Q_H(z):=\sum_{\pi}V_{L_\pi}(z)
      =\sum_{k\ge1} k!\,c_k z^{k-1}.
\quad}
\]
Indeed, a pair \((\pi,C)\) with \(|C|=k-1\) and \(C\) covering \(L_\pi\) is precisely an ordering of the \(k\) path blocks of a spanning \(k\)-cover, followed by concatenation. Each unordered \(k\)-cover has exactly \(k!\) block orders.

Consequently the grand theorem is equivalent to
\[
[z^0]Q_H(z)+\frac12[z^1]Q_H(z)>0.
\]

This polynomial has a direct resolvent representation. Retain the ordered-pair state space from the earlier transfer construction. Let
\[
T_{(u,v),(v,w)}=a_{uvw}y_v
\]
for pairwise distinct \(u,v,w\), and let
\[
C_{(u,v),(v,w)}=y_v
\]
on every such transition. Thus \(T\) is the tight-transition matrix and \(C\) is the complete transition matrix. Let
\[
\alpha_{(u,v)}=y_u,\qquad \beta_{(u,v)}=y_v.
\]

Double the state space by a bit \(c\in\{0,1\}\), where \(c=1\) means that the cut between the two vertices of the current ordered pair is selected. Define
\[
\mathbb T_H(z)=
\begin{pmatrix}
T & zC\\
C & zC
\end{pmatrix},
\qquad
\mathbb\alpha(z)=\begin{pmatrix}\alpha&z\alpha\end{pmatrix},
\qquad
\mathbb\beta=\begin{pmatrix}\beta\\ \beta\end{pmatrix}.
\]
Rows record the previous cut bit and columns the next cut bit.

A transition
\[
(u,v,c)\longrightarrow(v,w,d)
\]
is available exactly when either \((u,v,w)\) is tight or at least one of the two adjacent cuts is selected. Its weight is \(y_v z^d\). The initial row contributes \(y_u z^c\), and the terminal column contributes \(y_w\). Hence a surviving walk records an ordered vertex sequence together with a cut set covering every defect center; repeated original vertices vanish because \(y_v^2=0\).

Therefore, for \(|V|\ge2\),
\[
\boxed{\quad
Q_H(z)
=
[y_V]\,
\mathbb\alpha(z)(I-\mathbb T_H(z))^{-1}\mathbb\beta.
\quad}
\]
The inverse is a finite sum in the square-zero algebra. For \(|V|=1\), \(Q_H(z)=1\).

This gives a single finite transfer object for every path-cover number simultaneously. In particular, the constant and linear coefficients of the same resolvent are exactly the Hamilton-path count and twice the two-path-cover count. No exponential of \(F_H\), duplicated source-sink channels, or determinant perturbation is required.

### Boundary reversal inside the augmented transfer

The only block of \(\mathbb T_H(z)\) that depends on the orientation of \(H\) is the no-cut/no-cut block \(T\). The earlier boundary-reversal identity
\[
T+JT^{\mathsf T}J=C
\]
therefore remains visible without alteration:
\[
\mathbb T_H(z)=
\begin{pmatrix}
T & zC\\
C & zC
\end{pmatrix},
\qquad
T=C-JT^{\mathsf T}J.
\]
Thus all orientation dependence is confined to one block, while every transition touching a selected cut is universal.

There is also a defect-line form of the same symmetry. If \(\pi^{\mathrm{rev}}\) is the reversed ordering, then every consecutive triple changes from tight to non-tight or conversely. After reflecting cut positions,
\[
E(L_{\pi^{\mathrm{rev}}})
=
E(P_{n-1})\setminus E(L_\pi).
\]
Hence, if \(v_r(L)\) denotes the number of size-\(r\) vertex covers of \(L\),
\[
k!c_k
=
\frac12\sum_\pi
\left(
v_{k-1}(L_\pi)
+
v_{k-1}(P_{n-1}\setminus L_\pi)
\right).
\]
For \(k=1,2\), this symmetrizes the target entirely in terms of complementary edge-subsets of a path.

The next algebraic target is now sharper than the determinant-positivity problem: exploit
\[
T+JT^{\mathsf T}J=C
\]
inside the block resolvent for \(\mathbb T_H(z)\) to force a nonzero constant or linear spanning coefficient. Since the three cut-touching blocks are already universal, any cancellation argument only has to control the single oriented block \(T\).


### The linear cut coefficient factors through at most two complementary transitions

The augmented transfer permits an exact first-order expansion at \(z=0\), which is precisely the coefficient relevant to two-path covers.

Put
\[
R=(I-T)^{-1},
\qquad
T^\star=C-T=JT^{\mathsf T}J.
\]
The matrix \(T^\star\) has entry
\[
(T^\star)_{(u,v),(v,w)}=(1-a_{uvw})y_v=a_{wvu}y_v,
\]
so it records a non-tight forward transition, equivalently the reversed tight transition forced by boundary reversal.

Write
\[
\mathbb M(z)=I-\mathbb T_H(z)
=
\begin{pmatrix}
I-T & -zC\\
-C & I-zC
\end{pmatrix}.
\]
At \(z=0\),
\[
\mathbb M(0)^{-1}
=
\begin{pmatrix}
R&0\\
CR&I
\end{pmatrix}.
\]
Also
\[
\mathbb\alpha(0)=(\alpha,0),
\qquad
\mathbb\alpha'(0)=(0,\alpha),
\qquad
\mathbb T_H'(0)=
\begin{pmatrix}
0&C\\
0&C
\end{pmatrix}.
\]
Using
\[
\frac{d}{dz}(I-\mathbb T_H(z))^{-1}
=
(I-\mathbb T_H(z))^{-1}
\mathbb T_H'(z)
(I-\mathbb T_H(z))^{-1},
\]
a direct block multiplication yields
\[
Q_H'(0)
=
[y_V]\,
\alpha(I+RC)(I+CR)\beta.
\]
Now
\[
I+RC
=
R(I+T^\star),
\qquad
I+CR
=
(I+T^\star)R,
\]
because \(C=T+T^\star\) and \(RT=TR=R-I\). Therefore
\[
\boxed{\quad
Q_H'(0)
=
[y_V]\,
\alpha R(I+T^\star)^2R\beta.
\quad}
\]
Since \(Q_H(z)=\sum_{k\ge1}k!c_kz^{k-1}\),
\[
\boxed{\quad
2c_2
=
[y_V]\,
\alpha R(I+T^\star)^2R\beta.
\quad}
\]

Every coefficient in this expression is nonnegative. Expanding the middle factor,
\[
R(I+T^\star)^2R
=
R^2+2RT^\star R+R(T^\star)^2R.
\]
Thus the two-cover count is represented by spanning orderings consisting of a tight prefix and tight suffix separated by zero, one, or two consecutive complementary transitions. The two complementary transitions, when both occur, are consecutive because they are exactly the two triple centers adjacent to one selected cut.

This is the first expression in the route that simultaneously has all three desired features:

1. it counts the two-cover coefficient directly;
2. it uses boundary reversal explicitly through \(T^\star=JT^{\mathsf T}J\);
3. it has no cancellation or negative coefficients.

The grand theorem is therefore equivalent to showing
\[
[y_V]\left(
\alpha R\beta
+
\frac12\alpha R(I+T^\star)^2R\beta
\right)>0.
\]
Equivalently, some spanning ordering has no defect, one defect, or two adjacent defects.

The remaining problem is no longer algebraic sign control. It is a support-forcing statement for the positive transfer product
\[
\alpha R(I+T^\star)^2R\beta.
\]
A successful continuation should exploit the special relation
\[
T+T^\star=C
\]
to show that the supports of \(R\) and \(T^\star\) cannot avoid every spanning monomial in the three terms above.


### Eliminating the cut state gives a renewal formula for all cover numbers

The two-state augmented resolvent can be reduced to a one-state positive matrix. This gives an explicit formula for every coefficient of the path-cover polynomial and isolates the passage from a \(k\)-cover to a \((k+1)\)-cover.

Retain
\[
R=(I-T)^{-1},
\qquad
Q_H(z)
=
[y_V]\,
\mathbb\alpha(z)(I-\mathbb T_H(z))^{-1}\mathbb\beta,
\]
with
\[
\mathbb T_H(z)=
\begin{pmatrix}
T&zC\\
C&zC
\end{pmatrix}.
\]
Set
\[
A=I-T=R^{-1}.
\]
To compute the resolvent action, solve
\[
\begin{pmatrix}
A&-zC\\
-C&I-zC
\end{pmatrix}
\binom{x}{y}
=
\binom{\beta}{\beta}.
\]
The first row gives
\[
x=R\beta+zRCy.
\]
Substituting in the second row gives
\[
\bigl(I-zC-zCRC\bigr)y=(I+CR)\beta.
\]
Since
\[
C+CRC=C(I+RC),
\]
we obtain
\[
y=
\bigl(I-zC(I+RC)\bigr)^{-1}(I+CR)\beta.
\]
The output row is
\[
\alpha x+z\alpha y
=
\alpha R\beta+
z\alpha(I+RC)y.
\]
Therefore
\[
\boxed{
Q_H(z)
=
[y_V]\left[
\alpha R\beta+
z\alpha(I+RC)
\bigl(I-zC(I+RC)\bigr)^{-1}
(I+CR)\beta
\right].
}
\]

Define the nonnegative matrices
\[
L=I+RC,
\qquad
U=I+CR,
\qquad
K=CL=C(I+RC).
\]
Then
\[
\boxed{
Q_H(z)
=
[y_V]\left[
\alpha R\beta+
z\alpha L(I-zK)^{-1}U\beta
\right].
}
\]
All inverses are finite in the square-zero algebra.

Since
\[
Q_H(z)=\sum_{k\ge1}k!c_kz^{k-1},
\]
coefficient extraction gives, for every \(k\ge2\),
\[
\boxed{
k!c_k
=
[y_V]\,
\alpha L K^{k-2}U\beta.
}
\]
Equivalently,
\[
k!c_k
=
[y_V]\,
\alpha(I+RC)
\bigl[C(I+RC)\bigr]^{k-2}
(I+CR)\beta.
\]

Using \(T^\star=C-T\),
\[
L=R(I+T^\star),
\qquad
U=(I+T^\star)R,
\]
so the entire family may also be written
\[
k!c_k
=
[y_V]\,
\alpha R(I+T^\star)
\bigl[CR(I+T^\star)\bigr]^{k-2}
(I+T^\star)R\beta.
\]

For \(k=2\) this recovers
\[
2c_2
=
[y_V]\,
\alpha R(I+T^\star)^2R\beta.
\]

### The first nonzero cover coefficient in an arbitrary tournament

Let \(p=\operatorname{pc}(H)\ge2\), without any minimality hypothesis. Then the renewal formula gives
\[
[y_V]\alpha L K^{p-2}U\beta=p!c_p>0,
\]
while the analogous spanning coefficients for fewer than \(p\) paths vanish. In particular, when \(p=3\),
\[
[y_V]\alpha LU\beta=0,\qquad
[y_V]\alpha LKU\beta>0.
\]
These are identities for an arbitrary tournament of cover number three. They do not assert that all proper induced subtournaments have smaller cover number.

Here \(L,U,K\) are the matrices defined locally in the renewal calculation; the earlier quadratic identity uses the row \(U=\alpha(J-JT)^{-1}\) and the middle-vertex matrix \(K=JT\). Below that row is denoted \(W\) to distinguish it from the renewal matrices.



### Oriented line-graph formulation: the renewal step is a connector edge

There is a useful graph-theoretic model of the same transfer system.

Let \(K_V\) be the complete graph on \(V(H)\). Form a digraph \(D_H\) whose vertices are the ordinary edges of \(K_V\). Whenever
\[
e=\{u,v\},
\qquad
f=\{v,w\}
\]
are distinct incident edges, orient the adjacency
\[
e\longrightarrow f
\]
exactly when
\[
(u,v,w)
\]
is tight.

This is well-defined without choosing an orientation of either ordinary edge: reversing the ordered triple at the common middle vertex exchanges the two line-graph vertices, and the boundary-tournament axiom says exactly one direction occurs. Hence \(D_H\) is an orientation of the line graph
\[
L(K_V).
\]

A displayed tight path
\[
P=(v_0,v_1,\ldots,v_r)
\]
corresponds to the directed path
\[
v_0v_1
\longrightarrow
v_1v_2
\longrightarrow\cdots\longrightarrow
v_{r-1}v_r
\]
in \(D_H\), with the additional condition that the underlying ordinary edges form a vertex-simple path in \(K_V\). Conversely every such directed simple linear path in \(K_V\) gives a tight path of \(H\).

Therefore a path cover of \(H\) is equivalently a spanning linear forest \(F\) of \(K_V\), together with an orientation of each nontrivial component as a path, such that the ordinary edges of every component form a directed path in \(D_H\). Isolated vertices of \(F\) are the one-vertex path components.

If \(F\) has \(k\) components, then
\[
|E(F)|=n-k.
\]
Consequently
\[
\boxed{
\operatorname{pc}(H)
=
n-
\max\{|E(F)|:F\text{ is a spanning }D_H\text{-directed linear forest}\}.
}
\]
In particular the grand theorem is equivalent to
\[
\boxed{
\text{every orientation }D_H\text{ of }L(K_n)\text{ arising above admits such a spanning linear forest with at least }n-2\text{ edges}.
}
\]

This formulation clarifies the renewal matrix. For two displayed components
\[
P=(\ldots,a,b),
\qquad
Q=(c,d,\ldots),
\]
the ordinary edge
\[
e=bc
\]
is a connector between the two linear-forest components. The merged path \(PQ\) is tight exactly when
\[
ab\longrightarrow bc\longrightarrow cd
\]
is a directed two-step path in \(D_H\). If the merge fails, at least one of these two line-graph adjacencies points backward. These are precisely the complementary transitions recorded by \(T^\star\).

Thus the positive two-cover factor
\[
\alpha R(I+T^\star)^2R\beta
\]
says: take two directed linear-path pieces and insert one connector ordinary edge; the connector is allowed to point backward at neither, one, or both of its two endpoint incidences. A selected cut absorbs those at most two consecutive backward incidences.

Likewise, in
\[
\alpha L C L U\beta,
\]
the central complete transition \(C\) is exactly the free connector edge needed to pass from a three-component directed linear forest to the next component. For any tournament of path-cover number three, a spanning three-component directed linear forest exists and no spanning admissible forest with fewer components exists. This observation requires no counterexample-minimality hypothesis.

This suggests a concrete optimization version of the remaining problem:

> Choose a spanning admissible directed linear forest with the maximum number of ordinary edges, and among those optimize a secondary endpoint potential. If it has three components, every connector between two component endpoints is forced to point backward at at least one adjacent component edge. Use the resulting endpoint ownership pattern, together with boundary reversal in the incident-edge tournaments of \(D_H\), to perform an edge exchange that preserves cardinality but improves the secondary potential, or to add a connector and reduce the component count.

The line-graph formulation does not itself prove the exchange theorem, but it identifies the exact combinatorial content of the algebraic shortening problem and removes the matrix notation from that step.


### The quadratic identity counts an ordering with one change of triple status

Assume \(n\ge2\), and set
\[
R^\star=(I-T^\star)^{-1}=JR^{\mathsf T}J.
\]
Let \(a_H\) count pairs \((\pi,t)\), where \(\pi=(v_1,\ldots,v_n)\) is a spanning ordering and \(0\le t\le n-2\), such that its first \(t\) consecutive triples are tight and its remaining \(n-2-t\) consecutive triples are non-tight. Thus the list of triple statuses changes at most once, from tight to non-tight. The parameter \(t\) is included in the count.

Let \(h_H\) be the number of Hamilton tight path orders. Let \(b_H\) count pairs
\[
(v,\{P,Q\}),
\]
where \(v\in V\), the unordered collection \(\{P,Q\}\) consists of two nonempty vertex-disjoint ordered tight paths partitioning \(V-\{v\}\), and both \(Pv\) and \(Qv\) are tight paths. Appending \(v\) to a one-vertex path is allowed and is vacuously tight.

**Proposition.**
\[
\boxed{a_H=h_H+b_H.}
\]

**Proof.** Expanding \(R=\sum_{i\ge0}T^i\) and \(R^\star=\sum_{j\ge0}(T^\star)^j\), with both sums finite, gives
\[
a_H=[y_V]\alpha RR^\star\beta.
\]
The first \(i\) transitions are tight and the following \(j\) are non-tight. The square-zero variables require a spanning sequence of distinct original vertices, so \(i+j=n-2\).

Now use the earlier row, with its name distinguished from the renewal matrices:
\[
W=\alpha(J-JT)^{-1}=\alpha RJ,\qquad
g_v=\sum_{u\ne v}W_{(v,u)}.
\]
Since \(\beta=J\alpha^{\mathsf T}\),
\[
\alpha RR^\star\beta
=\alpha RJ R^{\mathsf T}\alpha^{\mathsf T}
=WJW^{\mathsf T}.
\]
The quadratic identity already derived in this Brainstorm is
\[
q_H=WJW^{\mathsf T}-\frac12\sum_v y_vg_v^2.
\]
Taking the spanning coefficient gives
\[
a_H=h_H+\frac12\sum_v[y_V]y_vg_v^2.
\]

To identify the last term, \(W_{(v,u)}\) enumerates transition sequences ending with the ordered pair \((u,v)\), with weights at all vertices except the final \(v\). Multiplication by \(y_v\) kills every sequence in which \(v\) already occurred. Thus \(y_vg_v\) enumerates tight paths of order at least two ending at \(v\), with the final vertex weighted once.

A surviving term of \(y_vg_v^2\) corresponds to two such paths sharing only their final vertex \(v\). Deleting their common final vertex gives nonempty disjoint paths \(P,Q\); their union must be \(V-\{v\}\) when the spanning coefficient is taken. Both \(Pv\) and \(Qv\) are tight by construction. Conversely every pair counted by \(b_H\) contributes two terms, from the two orders of its paths in the square. Division by two yields precisely \(b_H\). \(\square\)

### A direct sufficient condition for a two-cover

Every ordering counted by \(a_H\) yields a two-cover. If its parameter is \(t\), the prefix
\[
(v_1,\ldots,v_t)
\]
is tight whenever nonempty, and
\[
(v_n,v_{n-1},\ldots,v_{t+1})
\]
is tight. Indeed the forward order \((v_{t+1},\ldots,v_n)\) contains only the non-tight triples following the status change, and reversal replaces each by its tight boundary flip. For \(t=0\), the reversed sequence alone is a Hamilton path. These sequences partition \(V\).

A pair counted by \(b_H\) also gives a two-cover directly: append \(v\) to either \(P\) or \(Q\) and leave the other path unchanged.

The proposition therefore supplies a positive combinatorial interpretation of the quadratic identity. The expression \(WJW^{\mathsf T}\) counts orderings with one change of triple status; its correction term counts pairs of paths that both accept the same exterior vertex at their terminal ends.

The next sufficient statement is now concrete:

**Open target.** Every finite boundary \(3\)-tournament of order at least two has a spanning ordering whose triple statuses change at most once, from tight to non-tight.

By the proposition, this asks for \(h_H+b_H>0\), and it would imply the grand two-cover conjecture by the displayed construction. The converse implication from the grand conjecture to this stronger ordering statement has not been proved. In particular, the existence of an arbitrary two-cover is not being identified with the existence of this special ordering.

The universal existence assertion remains open. The exact identity and its two-cover construction hold for arbitrary \(H\); they use no counterexample-minimality hypothesis.


### Compatible neutral omission swaps are not an independent obstruction

The current Article III architecture isolates a compatible Phi-neutral omission swap as the only coherent residue left after direct mixing and split-support comparisons. In the explicit normal form of
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]],
this residue collapses to the already-central external-reversal interface.

Use the notation of that theorem:
\[
H-y=R\mid Q,qquad
R=(r_0,\ldots,r_m),qquad
z=r_0,qquad
B=(r_1,\ldots,r_m),
\]
and let
\[
T=C\mid D
\]
be a deletion cover of \(H-z\). In the no-disturbance branch, the surviving vertices of \(R-z\) occur as one inherited-order block \(B\) in
\[
C=L,B,K.
\]

There are only two neutral geometries.

#### Nonempty suffix

Assume \(K\ne\varnothing\). Neutrality forces \(|L|=1\); write \(L=(w)\). Then
\[
T=(w,B,K)\mid D
\]
is a deletion cover of \(H-z\), while endpoint restoration gives
\[
G_w=(z,B,K)\mid D
\]
as a deletion cover of \(H-w\).

This is exactly the same-slot root-exchange configuration of Lemma 11 in
[[defect_lines_and_spanning_order_compression_the_remaining_lemma]]:
the common ordered core is \((B,K)\), the fixed path is \(D\), and the omitted labels \(z,w\) occupy the same initial endpoint slot.

Lemma 11 therefore gives a two-cover, a direct mixed edge, an order disagreement, or an external reversal at the opposite endpoint. Under the current Article III reductions, direct mixing feeds split/leave-and-return unless a two-cover already exists; order disagreement yields a reversing triple by path-intersection calculus; and split/leave-and-return returns to external reversal. Hence this neutral branch produces either a two-cover or an external reversal.

#### Terminal inherited block

Assume \(K=\varnothing\). Write
\[
L=L',w.
\]
Neutrality forces \(|L'|=1\); write \(L'=(u)\). Then
\[
T=(u,w,B)\mid D
\]
is a deletion cover of \(H-z\), and the restoration calculation gives
\[
(w,z,B)
\]
as a tight path. Omitting \(u\) produces the compatible deletion cover
\[
G_u=(w,z,B)\mid D
\]
of \(H-u\).

Now the common ordered core is
\[
(w,B)=(w,r_1,\ldots,r_m).
\]
The root \(u\) occupies the endpoint gap immediately before \(w\), while \(z\) occupies the adjacent gap immediately after \(w\).

If
\[
(u,w,z)
\]
is tight, then
\[
(u,w,z,B)
\]
is a tight path, because \((w,z,r_1)\) is supplied by the restoration branch and every later triple is inherited from \(B\). Thus
\[
(u,w,z,B)\mid D
\]
is a two-cover of \(H\).

Therefore in a counterexample \((u,w,z)\) is non-tight. Boundary reversal gives
\[
(z,w,u)
\]
tight. Since \((u,w)\) is the displayed initial edge of \((u,w,B)\) in \(T\), this is an external tight triple reversing a displayed endpoint edge.

Hence:

**Neutral omission-swap absorption lemma.**
Every Phi-neutral omission swap arising from
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]]
produces either a two-cover of \(H\) or, after the already-established disturbance reductions, an external tight triple reversing a displayed endpoint edge.

So the compatible neutral omission swap is not an independent bridge-manufacture obstruction.

### Line-graph meaning

The two cases are precisely the two cardinality-preserving endpoint exchanges of a maximum admissible directed linear forest.

In the first case one root edge is replaced by another in the same endpoint slot while the directed core is unchanged. Lemma 11 says this same-slot exchange cannot remain invisible at the opposite end.

In the second case the two roots occupy adjacent gaps around the common vertex \(w\). The only new adjacency needed to merge them is encoded by \((u,w,z)\). If it points forward, one connector is added and the component count drops. If it points backward, its boundary orientation is exactly the external reversal \((z,w,u)\).

Thus the renewal/line-graph route and the updated main architecture now converge on one recurrent geometric obstruction: external endpoint reversal.


### Exact junction obstruction for a displayed two-cover

Let (P=(p_1,ldots,p_r)) and (Q=(q_1,ldots,q_s)) be disjoint tight paths, with (r,sge2). In the ordering
[
P,Q^{m rev}=(p_1,ldots,p_r,q_s,q_{s-1},ldots,q_1),
]
all triples internal to (P) are tight and all triples internal to (Q^{m rev}) are non-tight. Thus the ordering fails to have a single change from tight to non-tight only when the two junction triples have statuses
[
	ext{non-tight}, 	ext{tight}.
]
Equivalently,
[
(p_{r-1},p_r,q_s)	ext{ is non-tight},
qquad
(p_r,q_s,q_{s-1})	ext{ is tight}.
]
By boundary reversal the first condition is equivalent to
[
(q_s,p_r,p_{r-1})	ext{ tight}.
]
Hence failure is exactly the condition that the chosen terminal endpoints (p_r,q_s) each reverse the terminal edge of the opposite path.

Therefore (P Q^{m rev}) is a one-change ordering unless those two endpoint reversals occur simultaneously.

If the same failure occurs after every independent reversal of (P) and (Q), then every endpoint of (P) reverses both end edges of (Q), and every endpoint of (Q) reverses both end edges of (P). Thus absence of a one-change ordering from a displayed two-cover forces a complete endpoint reversal grid.

In a minimum counterexample every proper deletion has a two-cover. Each deletion cover therefore yields either a one-change ordering of the deletion or this rigid endpoint grid. The latter feeds the existing simultaneous-reversal and bounded-support machinery.

### Three-arm hub forced by transport

Suppose a spanning three-cover (Amid Pmid Q) is in the current longest-path normal form and (q_t), an endpoint of (Q), reverses the terminal edges of both (A) and (P):
[
(q_t,a_r,a_{r-1}),qquad(q_t,p_m,p_{m-1})
]
are tight.

Apply the preceding junction calculation to transport the reversal across the third component. Unless a spanning one-change ordering or the existing two-reverser bounded-support conclusion appears, one is forced to have
[
(a_r,q_t,q_{t-1}),qquad
(p_m,q_t,q_{t-1})
]
tight as well.

Thus outside immediate compression or bounded support, the endpoint (q_t) mutually reverses the terminal edges of both large paths, while both terminal vertices (a_r,p_m) reverse the terminal edge of (Q).

For the central triple on ({a_r,p_m,q_t}), exactly one of
[
(a_r,q_t,p_m),qquad(p_m,q_t,a_r)
]
is tight. In the first case
[
(a_r,q_t,p_m,p_{m-1})
]
is a tight four-path; in the second
[
(p_m,q_t,a_r,a_{r-1})
]
is a tight four-path. Hence the three-arm hub always contains an anchored Hamiltonian four-support using the common reversal center and terminal data from both large paths.

This does not yet close the theorem: deleting that four-support leaves three inherited path pieces in general. The remaining task is to exploit the anchor information, rather than merely the existence of the bounded support, to merge two of those complementary pieces.


### Global noninsertability forces an alternating transitive bridge core

Retain the mixed bridge pattern of Article III Lemmas 40 and 44:
[
H-{z,w}=Amid C,
quad
A=(ldots,a',a),
quad
C=(c,c_2,ldots),
]
with
[
(a',a,z),quad (z,c,c_2),quad
(w,a,a'),quad (c_2,c,w)
]
tight. Lemma 40 also gives
[
(c,z,a)
]
tight.

Lemma 44 says that (w) is noninsertable not only in (A,C), but also in the enlarged displayed paths
[
(A,z),qquad (z,C).
]
Testing the new endpoint gaps gives two additional forced triples. Since (w) cannot be appended to ((A,z)),
[
(a,z,w)
]
is non-tight, hence
[
(w,z,a)
]
is tight. Since (w) cannot be prepended to ((z,C)),
[
(w,z,c)
]
is non-tight, hence
[
(c,z,w)
]
is tight.

Thus the local tournament with middle (z) on the three outer vertices ({c,w,a}) is transitive:
[
c	o w	o a,qquad c	o a.
]

Now inspect the local tournament with middle (w) on ({a,z,c}).

- If ((z,w,a)) is tight, then
  [
  (c,z,w,a,a')
  ]
  is a Hamiltonian five-path, using ((c,z,w)) and ((w,a,a')).

- If ((c,w,a)) is tight, then
  [
  (c_2,c,w,a,a')
  ]
  is a Hamiltonian five-path.

- If ((c,w,z)) is tight, then
  [
  (c_2,c,w,z,a)
  ]
  is a Hamiltonian five-path, using ((w,z,a)).

Hence, unless a Hamiltonian five-support already appears, all three displayed triples are non-tight. Boundary reversal then forces
[
(a,w,z),qquad (a,w,c),qquad (z,w,c)
]
tight. Therefore the local tournament at middle (w) is the opposite transitive order
[
a	o z	o c,qquad a	o c.
]

Consequently the mixed bridge has the following sharp local alternative:

1. a Hamiltonian four- or five-support occurs; or
2. on the four-set
   [
   X={a,z,w,c},
   ]
   the local tournaments at the two bridge vertices are opposite transitive chains:
   [
   c	o w	o aquad	ext{at middle }z,
   ]
   [
   a	o z	o cquad	ext{at middle }w.
   ]
   If (X) itself is Hamiltonian, this is again a Hamiltonian four-support. If not, the four-set classification in [[smallset01]] identifies (X) as the non-Hamiltonian matching-block four-set.

Thus, after the global noninsertability update, the genuinely coherent mixed-bridge residue is not an arbitrary external reversal. It is an anchored matching-block four-set whose two bridge vertices carry opposite transitive local orders, with (a') and (c_2) attached by the inherited/reversal triples above.

This produces a natural six-vertex interface
[
{a',a,z,w,c,c_2}
]
to which the prescribed-pair six-set transport theorem [[sixset_prescribed_pair_menu01]] applies with prescribed pair ({a',c_2}). The next step is to exploit that menu while retaining the inherited tails of (A) and (C).


### Reversing the canonical five-defect island transports the obstruction to the outer splice boundaries

Let
[
H-x=Pmid Q,
qquad
P=(p_1,ldots,p_m),
qquad
Q=(q_1,ldots,q_s)
]
be a deletion cover of a minimum counterexample, with (m,sge3).

The standard spanning order
[
P,x,Q
]
has exactly the three possible central defect triples
[
(p_{m-1},p_m,x),qquad
(p_m,x,q_1),qquad
(x,q_1,q_2).
]
In a counterexample all three are non-tight: the two outer ones are the endpoint-insertion failures, while the middle one is forced by the failure of the spanning concatenation.

Article IV Lemma 21 gives the reverse tight five-path
[
F=(q_2,q_1,x,p_m,p_{m-1}).
]

Write
[
P^-=(p_1,ldots,p_{m-2}),
qquad
Q^+=(q_3,ldots,q_s).
]
Replacing the central five-vertex order by (F) gives the spanning three-cover
[
P^-mid Fmid Q^+.
]

Every triple internal to these three displayed blocks is tight. Therefore:

- (P^-F) fails to be tight only through the two present splice triples
  [
  (p_{m-3},p_{m-2},q_2),
  qquad
  (p_{m-2},q_2,q_1);
  ]
- (FQ^+) fails to be tight only through
  [
  (p_m,p_{m-1},q_3),
  qquad
  (p_{m-1},q_3,q_4).
  ]

If either concatenation were tight, the other untouched block would give a spanning two-cover of (H). Hence in a counterexample both splice attempts fail.

Boundary reversal therefore gives at least one tight reversal certificate on each side:

left:
[
(q_2,p_{m-2},p_{m-3})
quad	ext{or}quad
(q_1,q_2,p_{m-2});
]

right:
[
(q_3,p_{m-1},p_m)
quad	ext{or}quad
(q_4,q_3,p_{m-1}),
]
with nonexistent boundary terms omitted in the short cases.

Thus reversing the central three-defect island does not merely produce a bounded Hamiltonian support. It **pushes the obstruction outward** from the deleted label (x) to the two splice boundaries. The original three adjacent failures are replaced by two separated two-triple interfaces, and each interface supplies a concrete external reversal.

The symmetric canonical five-path
[
(p_2,p_1,x,q_s,q_{s-1})
]
does the same thing from the opposite ends. Hence every deletion cover carries two opposite obstruction-transport operations.

This gives a direct transport interpretation of the current architecture:

1. the deletion ordering concentrates the obstruction into a length-three defect island;
2. reversing its canonical five-vertex core makes that island tight;
3. failure to reduce the component count forces new reversal certificates farther out;
4. applying the construction from both ends creates two opposing reversal fronts along the displayed paths.

A closure proof can therefore target collision of these two fronts rather than arbitrary external reversals. The useful invariant is the distance, measured in inherited path edges, between the two forced splice interfaces.


### Endpoint peeling shows that the one-change target is exactly the two-cover target

Call a spanning ordering **one-change** if its consecutive triple statuses consist of a possibly empty block of tight triples followed by a possibly empty block of non-tight triples.

The sufficient condition above is in fact equivalent to the grand two-cover statement.

**Proposition.** A finite boundary \(3\)-tournament \(H\) has path-cover number at most two if and only if \(H\) has a spanning one-change ordering.

**Proof.** The implication from a one-change ordering to a two-cover was established above.

Conversely, suppose
\[
H=P\mid Q
\]
is a spanning cover by at most two nonempty tight paths. If there is only one path, its Hamilton order is one-change. Thus assume there are two paths and write
\[
P=(p_1,\ldots,p_r),\qquad Q=(q_1,\ldots,q_s).
\]

If one component is a singleton, say \(Q=\{q_1\}\), then
\[
(p_1,\ldots,p_r,q_1)
\]
is one-change: all triples internal to \(P\) are tight and there is at most one additional terminal triple. This also covers the cases \(r\le2\).

Assume now \(r,s\ge2\). For each independent choice of displayed orientation of \(P\) and \(Q\), consider the ordering
\[
P\,Q^{\rm rev}.
\]
By the exact junction calculation above, this ordering is one-change unless its two junction triples have statuses
\[
\text{non-tight},\ \text{tight}.
\]

If any of the four orientation choices succeeds, we are done. Suppose all four fail. Keep \(Q\) in the displayed orientation above but orient \(P\) as
\[
(p_r,\ldots,p_1).
\]
The terminal endpoint of this oriented copy of \(P\) is \(p_1\), with terminal edge \(p_2p_1\), while the chosen terminal endpoint of \(Q\) is \(q_s\). Failure of the corresponding junction forces
\[
(q_s,p_1,p_2)
\]
to be tight. Hence
\[
P'=(q_s,p_1,\ldots,p_r)
\]
is a tight path, while
\[
Q'=(q_1,\ldots,q_{s-1})
\]
is an inherited tight path. Thus
\[
H=P'\mid Q'
\]
is another two-cover in which the second component has lost one vertex.

Repeat with \(P'\mid Q'\). At each stage either one of the four junction orderings is one-change, or an endpoint of the second path peels off and prepends to the first path. The second component strictly decreases in order. Eventually it is a singleton, where the preceding base case gives a one-change spanning ordering. \(\square\)

The complete endpoint-reversal grid is therefore not a terminal obstruction. Its reversal at the initial edge of one path is exactly the tight triple needed to transfer an endpoint of the other path across that initial edge.

Consequently the earlier open target is not stronger than the grand conjecture. In the notation of the quadratic identity,
\[
a_H>0
\quad\Longleftrightarrow\quad
\operatorname{pc}(H)\le2.
\]
Since
\[
a_H=h_H+b_H,
\]
the identity becomes the exact reformulation
\[
\boxed{\operatorname{pc}(H)\le2\iff h_H+b_H>0.}
\]

Thus the direct-counting route loses no strength by targeting the one-change coefficient. In particular, endpoint-reversal grids should be used as transfer moves: repeated failure of the naive junction shortens one component of a displayed two-cover until a one-change ordering appears.


### Correction to versions 10, 12, and 13

Three recent extensions used orientation moves that are not available in a boundary (3)-tournament.

First, if
[
P=(p_1,ldots,p_r)
]
is a tight path, its formal reversal
[
P^{m rev}=(p_r,ldots,p_1)
]
is not in general another tight path. For every internal displayed triple, boundary antisymmetry makes the reversed triple non-tight. Therefore the exact junction calculation for
[
P,Q^{m rev}
]
is valid for the displayed tight orders (P,Q), but one cannot independently reverse (P) or (Q) and reapply it as though those reversed orders were alternative Hamilton orders.

Accordingly, the version-10 claim that failure for four independent path orientations forces a complete endpoint-reversal grid is withdrawn. The reciprocal transport assertions in the subsequent three-arm paragraph do not follow from the junction calculation alone.

Second, the version-12 “canonical five-defect island” relied on the former Article IV claim that, for every deletion cover
[
H-x=Pmid Q,
]
the cross triples
[
(q_1,x,p_m),qquad (p_1,x,q_s)
]
are forced tight. That claim has now been corrected in
[
[[endpoint_transport_and_small_support_gluing_the_remaining_lemma]].
]
The spanning order (P,x,Q) introduces three triples around (x); the endpoint-insertion failures determine the two outer ones but do not determine the middle triple ((p_m,x,q_1)). Thus the canonical five-paths, and the obstruction-front transport built from them, are conditional rather than universal. The version-12 transport branch is withdrawn as a general assertion.

Third, version 13 again treats the reversed displayed order of (P) as a tight orientation when performing endpoint peeling. Hence its proof that every two-cover yields a one-change ordering is invalid. The converse implication
[
operatorname{pc}(H)le2Longrightarrow a_H>0
]
is open again. The already-proved implication
[
a_H>0Longrightarrow operatorname{pc}(H)le2
]
and the exact identity
[
a_H=h_H+b_H
]
remain valid.

### A common exterior reverser of two terminal edges already gives a four-support

The useful local conclusion sought by the three-arm discussion survives without any reciprocal transport.

**Lemma.** Let
[
A=(a_1,ldots,a_r),qquad P=(p_1,ldots,p_m)
]
be vertex-disjoint tight paths with (r,mge2), and let (z) lie outside both supports. If
[
(z,a_r,a_{r-1}),qquad (z,p_m,p_{m-1})
]
are tight, then the set
[
{z,a_r,p_m,a_{r-1},p_{m-1}}
]
contains a Hamiltonian four-set. More precisely, exactly one of
[
(a_r,z,p_m),qquad (p_m,z,a_r)
]
is tight. In the first case
[
(a_r,z,p_m,p_{m-1})
]
is a tight four-path; in the second
[
(p_m,z,a_r,a_{r-1})
]
is a tight four-path.

**Proof.** The two central triples are boundary flips of one another, so exactly one is tight. Concatenate the tight choice with the corresponding assumed terminal-edge reversal. (square)

Thus a vertex which simultaneously reverses two displayed terminal edges already produces the anchored four-support; no “reversal back” through a third path is needed.

### Correct cross-corner dichotomy for a deletion cover

Let
[
H-x=Pmid Q,qquad
P=(p_1,ldots,p_m),qquad
Q=(q_1,ldots,q_s)
]
be a deletion cover of a minimum counterexample. Article IV Lemma 14 gives the four genuine endpoint reversals
[
(p_2,p_1,x),quad (x,p_m,p_{m-1}),quad
(q_2,q_1,x),quad (x,q_s,q_{s-1}).
]

At the cross pair ((p_m,q_1)), exactly one of
[
(q_1,x,p_m),qquad (p_m,x,q_1)
]
is tight. If the first orientation is tight, then
[
(q_2,q_1,x,p_m,p_{m-1})
]
is a tight five-path. If the second orientation is tight, this five-path is unavailable and the tight cross triple
[
(p_m,x,q_1)
]
must be retained as the branch datum.

Symmetrically, at the other cross pair ((p_1,q_s)), either
[
(p_2,p_1,x,q_s,q_{s-1})
]
is a tight five-path, or the opposite cross triple
[
(q_s,x,p_1)
]
is tight.

Hence every deletion cover falls into an exact four-case menu according to the two cross-corner bits:

1. two favorable cross orientations, giving two opposite five-supports;
2. one favorable orientation and one opposite cross triple;
3. the symmetric mixed case;
4. two opposite cross triples
   [
   (p_m,x,q_1),qquad(q_s,x,p_1).
   ]

No orientation in this menu is inferred beyond a genuine boundary-flip pair.

The fourth case is the clean corrected residue. In the local tournament at middle (x), the two cross arcs form the matching
[
p_m	o q_1,qquad q_s	o p_1.
]
Meanwhile the same-end pairs ((p_1,q_1)) and ((p_m,q_s)) still yield the unconditional rooted four-support probes of Article IV Lemma 18. This gives a concrete next target: exploit the interaction between the cross matching and those two same-end four-supports, or feed the resulting rooted three-square of Article IV Lemma 19 into the renewal/line-graph exchange formulation.

### Current corrected direction

The direct transfer identities, the renewal formula, the line-graph formulation, the quadratic identity (a_H=h_H+b_H), the neutral omission-swap absorption, and the version-11 alternating bridge-core analysis remain available.

The most promising direct combinatorial target is now the two-cross-triple residue
[
(p_m,x,q_1),qquad(q_s,x,p_1)
]
together with the four endpoint-pair rooted three-cover states
[
(P-p)mid T_{p,q}mid(Q-q).
]
Unlike formal reversal of a displayed path, these are genuine tight-path states connected by actual pairwise repartitions. A closure argument should seek a monotone transfer on this neutral square, or a cancellation identity on the full spanning transfer object whose combinatorial fixed points are precisely these cross-matching configurations.


### A favorable cross corner is a strict potential descent above order twelve

The corrected cross-corner menu still has a strong monotonic consequence.

Let
\[
H-x=P\mid Q,\qquad
P=(p_1,\ldots,p_m),\qquad
Q=(q_1,\ldots,q_s),
\]
with \(m,s\ge3\). Consider the rooted endpoint-pair state at the cross corner \((p_m,q_1)\):
\[
\mathcal C_{R,L}
=(p_1,\ldots,p_{m-1})
\mid T_{p_m,q_1}\mid
(q_2,\ldots,q_s),
\]
whose profile is
\[
(m-1,3,s-1).
\]

Suppose the favorable cross orientation
\[
(q_1,x,p_m)
\]
is tight. By the genuine endpoint reversals
\[
(q_2,q_1,x),\qquad (x,p_m,p_{m-1}),
\]
the five-path
\[
F=(q_2,q_1,x,p_m,p_{m-1})
\]
is tight. Hence
\[
\mathcal F_{R,L}
=(p_1,\ldots,p_{m-2})
\mid F\mid
(q_3,\ldots,q_s)
\]
is a spanning three-cover, of profile
\[
(m-2,5,s-2).
\]

Moreover \(\mathcal F_{R,L}\) lies in the same pairwise-repartition component as \(\mathcal C_{R,L}\). Starting from \(\mathcal C_{R,L}\), first move \(p_{m-1}\) from the \(P\)-remainder into the middle component, using the tight four-path
\[
(q_1,x,p_m,p_{m-1}),
\]
and then move \(q_2\) from the \(Q\)-remainder into that component, using \(F\). Both moves repartition only two components.

The potential change is therefore
\[
\begin{aligned}
\Phi(\mathcal F_{R,L})-\Phi(\mathcal C_{R,L})
&=(m-2)^2+5^2+(s-2)^2\\
&\qquad-\bigl((m-1)^2+3^2+(s-1)^2\bigr)\\
&=22-2(m+s)\\
&=2(12-|V(H)|).
\end{aligned}
\]

Thus, whenever \(|V(H)|\ge13\), the favorable cross orientation gives a **strict** \(\Phi\)-decrease. For \(|V(H)|=12\) the move is neutral.

The symmetric statement holds at the opposite cross corner \((p_1,q_s)\).

Consequently, for order at least thirteen, any state in the endpoint-pair square that is locally blocked from strict \(\Phi\)-descent must have the two opposite cross orientations
\[
(p_m,x,q_1),\qquad
(q_s,x,p_1)
\]
tight. In other words, after the correction to the former canonical-five-path claim, the cross-matching residue is not merely one case among four: it is the **only** cross-corner orientation pattern compatible with local potential minimality at arbitrary large order.

This gives a cleaner continuation target. Work directly with the genuine cross matching
\[
p_m\to q_1,\qquad q_s\to p_1
\]
in the local tournament at middle \(x\), together with the unconditional same-end four-support probes and the neutral endpoint-pair square. A successful exchange only has to show that this cross matching cannot persist at a true pairwise-repartition minimum without producing either a lower-potential cover, a one-defect spanning ordering, or a two-cover.


### Cyclic two-run reformulation and a Norine--Coxeter route

There is a global red/blue reformulation of the surviving one-change sufficient condition.

For an oriented spanning cycle
\[
C=(v_1,\ldots,v_n)
\]
with indices read cyclically, color the cyclic window at \(i\) red when
\[
(v_i,v_{i+1},v_{i+2})
\]
is tight and blue when it is non-tight. Let \(\rho(C)\) be the number of monochromatic components of this cyclic red/blue word.

**Cyclic two-run lemma.** If some spanning cycle \(C\) has \(\rho(C)\le 2\), then
\[
\operatorname{pc}(H)\le2.
\]

If the cyclic word is monochromatic, break the cycle to obtain a Hamilton tight path after choosing the appropriate orientation. If it has exactly two monochromatic components, break the cyclic order at one color change. The resulting spanning linear order has a consecutive-triple status word with at most one color change. Reversing the entire linear order if needed makes the status pattern tight followed by non-tight. The already-valid one-change construction then gives a two-cover by taking the tight prefix and the reversal of the non-tight suffix.

Boundary reversal gives an exact antipodal symmetry. Reversing \(C\) sends every cyclic window
\[
(v_i,v_{i+1},v_{i+2})
\]
to its boundary flip
\[
(v_{i+2},v_{i+1},v_i),
\]
so every red window becomes blue and every blue window becomes red. Thus cycle reversal globally complements the local coloring while preserving \(\rho(C)\).

This is closely analogous to Norine's antipodal-coloring problem. Wu and Yang, *A Chain-Level Borsuk--Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture*, arXiv:2607.19276 (2026), prove that every antipodal red/blue edge-coloring of a hypercube has a monochromatic path between antipodal vertices. Their contradiction labels each cube vertex by the red component containing the vertex and the red component containing its antipode; red edges preserve one coordinate and blue edges preserve the other, producing an antipodal rook labeling ruled out by a chain-level Borsuk--Ulam obstruction.

The formally closer cube statement is the Feder--Subi one-switch conjecture: every arbitrary red/blue cube coloring has an antipodal path with at most one color change. That stronger statement remains open. The present boundary-tournament problem is intermediate: the target is likewise a one-switch/two-run traversal, but the local colors satisfy a built-in antipodal law under reversal.

There is a natural topological source space for this symmetry. The type-\(A_{n-1}\) Coxeter complex is the barycentric subdivision of the boundary of an \((n-1)\)-simplex, hence an \((n-2)\)-sphere, and its chambers are the permutations of \(V(H)\). Under the subset-flag model, the antipodal complement map sends the chamber
\[
(v_1,\ldots,v_n)
\]
to
\[
(v_n,\ldots,v_1).
\]
Thus the geometric antipode is exactly spanning-order reversal.

Each consecutive triple in a chamber is local rank-two data. On the six orders of any three fixed labels, boundary reversal pairs each order with its reverse, and the boundary-tournament axiom gives opposite tight/non-tight colors to each such pair. Hence \(H\) can be viewed as a system of antipodal binary data on the rank-two \(A_2\) residues of the type-\(A\) Coxeter sphere.

This suggests a route genuinely different from endpoint transport:

> **Norine--Coxeter target.** Use the antipodal type-\(A\) Coxeter sphere and its local rank-two tight/non-tight data to force a chamber whose consecutive-triple status word has at most one linear color change, equivalently a spanning cyclic order whose window coloring has at most two monochromatic components.

A direct application of Wu--Yang is not yet available: their coloring lives on cube edges, while the present coloring lives on consecutive-triple windows/rank-two chamber data. The concrete next problem is to find the analogue of their component-pair labeling. Ideally, failure of every two-run cycle should assign two labels to each antipodal state so that local red data preserves one coordinate and local blue data preserves the other. The type-\(A\) Coxeter complex is the natural source because its antipode is exactly order reversal.


### A bad cross corner either descends or pushes a reversal outward

The version-15 potential calculation has a complementary statement for the surviving cross-matching orientation. This recovers a valid form of the obstruction-front idea without using a formally reversed tight path.

Let
[
H-x=Pmid Q,qquad
P=(p_1,ldots,p_m),qquad
Q=(q_1,ldots,q_s),
]
with (m,sge2), and suppose the cross corner ((p_m,q_1)) has the bad orientation
[
(p_m,x,q_1)
]
tight. Then its boundary flip
[
(q_1,x,p_m)
]
is non-tight. The corresponding rooted endpoint-pair state is
[
mathcal C_{R,L}
=
(p_1,ldots,p_{m-1})
mid
(p_m,x,q_1)
mid
(q_2,ldots,q_s).
]

Consider instead the spanning linear order
[
sigma=
(p_1,ldots,p_{m-1},q_1,x,p_m,q_2,ldots,q_s).
]
All triples of (sigma) are inherited tight triples except possibly
[
(p_{m-2},p_{m-1},q_1),
qquad
(p_{m-1},q_1,x),
qquad
(q_1,x,p_m),
qquad
(x,p_m,q_2),
qquad
(p_m,q_2,q_3),
]
with the two outer terms omitted when (m=2) or (s=2). The middle triple ((q_1,x,p_m)) is definitely non-tight.

**Lemma (one-step bad-cross transport).** If (H) has no two-cover, then at least one of the following holds:

1. both inner splice triples
   [
   (p_{m-1},q_1,x),
   qquad
   (x,p_m,q_2)
   ]
   are non-tight;

2. a present outer splice triple
   [
   (p_{m-2},p_{m-1},q_1)
   quad	ext{or}quad
   (p_m,q_2,q_3)
   ]
   is non-tight.

**Proof.** Suppose every present outer splice triple is tight and at least one inner splice triple is tight. Then the defect line of (sigma) has the mandatory central defect and at most one defect on an adjacent triple. Hence all defect edges are incident with a single cut position, so
[

u(L_sigma)le1.
]
By the defect-line identity, (sigma) yields a spanning cover by at most two tight paths, contradiction. (square)

The two alternatives both have concrete positive interpretations.

If both inner splice triples are non-tight, boundary reversal gives
[
(x,q_1,p_{m-1}),
qquad
(q_2,p_m,x)
]
tight. Together with the bad cross triple ((p_m,x,q_1)), this gives the tight five-path
[
F_{m bad}
=
(q_2,p_m,x,q_1,p_{m-1}).
]
Thus
[
mathcal F_{m bad}
=
(p_1,ldots,p_{m-2})
mid
F_{m bad}
mid
(q_3,ldots,q_s)
]
is a spanning three-cover of profile
[
(m-2,5,s-2).
]
It lies in the same pairwise-repartition component as (mathcal C_{R,L}): first absorb (p_{m-1}) into the middle path using
[
(p_m,x,q_1,p_{m-1}),
]
then prepend (q_2) using (F_{m bad}).

Consequently
[
Phi(mathcal F_{m bad})-Phi(mathcal C_{R,L})
=
2(12-|V(H)|),
]
exactly as in the favorable-cross five-path calculation. Hence for (|V(H)|ge13), the first alternative is a strict potential descent.

If an outer splice triple is non-tight, its boundary flip is a genuine reversal farther from the original cross corner:
[
(q_1,p_{m-1},p_{m-2})
]
on the (P)-side, or
[
(q_3,q_2,p_m)
]
on the (Q)-side. Thus the obstruction has moved one inherited edge outward.

Therefore:

**Corollary.** Let (|V(H)|ge13), and suppose the rooted endpoint-pair state (mathcal C_{R,L}) is (Phi)-minimal in its pairwise-repartition component. If the cross orientation is bad,
[
(p_m,x,q_1) 	ext{tight},
]
then at least one present outer splice triple is non-tight, and hence an external reversal is forced one edge farther out along (P) or (Q).

Combined with version 15, every cross corner of a (Phi)-minimal rooted square at order at least thirteen has a monotone interpretation:

- favorable orientation (Rightarrow) strict descent;
- bad orientation (Rightarrow) outward reversal transport.

Thus a genuine minimum cannot absorb the cross-corner information locally. It must export reversal data away from the deleted label. This is the first valid obstruction-front step after the correction of the former canonical-five-path argument.

The next target is to iterate this exported reversal while preserving a monotone quantity—most naturally distance from the deleted label along the inherited path, with (Phi) as the primary potential—until two fronts collide or an endpoint is reached.


### Switch-minimal orders export a certificate from the last color run

The Norine-style formulation admits a purely local descent move that does not use counterexample minimality.

For a spanning linear order
\[
\pi=(v_1,\ldots,v_n),
\]
write
\[
\epsilon_i\in\{0,1\},\qquad 1\le i\le n-2,
\]
for the tightness indicator of
\[
(v_i,v_{i+1},v_{i+2}),
\]
with \(1\) meaning tight. Define its switch number by
\[
s(\pi)=
\left|\{\,i:1\le i\le n-3,\ \epsilon_i\ne\epsilon_{i+1}\,\}\right|.
\]
Thus \(s(\pi)\le1\) is already sufficient for a two-cover: if the word is tight then non-tight, use the tight prefix and reverse the non-tight suffix; if it is non-tight then tight, reverse the non-tight prefix and keep the tight suffix.

Boundary reversal gives
\[
\epsilon_i(\pi^{\rm rev})
=
1-\epsilon_{n-1-i}(\pi),
\]
and hence
\[
s(\pi^{\rm rev})=s(\pi).
\]

There is also a useful locality statement. Reverse any terminal vertex interval
\[
(v_{k+1},\ldots,v_n).
\]
Every triple wholly before the cut keeps its color, while every triple wholly inside the reversed suffix has its color complemented and its order reflected. Consequently every switch wholly inside either region is preserved. The change in \(s\) is concentrated at the join between the unchanged prefix and the reversed suffix.

This becomes especially sharp for the final monochromatic run. Suppose
\[
r\le n-2,\qquad
\epsilon_r=\epsilon_{r+1}=\cdots=\epsilon_{n-2}=\beta,
\]
and, when \(r>1\),
\[
\epsilon_{r-1}=1-\beta.
\]
Assume \(r\ge3\) so that the displayed boundary vertices below exist. Reverse the terminal vertex interval
\[
(v_r,v_{r+1},\ldots,v_n)
\]
and call the new order \(\pi'\).

Every new triple beginning at position \(i\ge r\) is the boundary flip of an old triple in the final run. Hence all of those new triples have color
\[
1-\beta.
\]
Only the two new triples immediately before them are not predetermined:
\[
A=(v_{r-2},v_{r-1},v_n),\qquad
B=(v_{r-1},v_n,v_{n-1}).
\]

**Last-run reversal lemma.**
If both \(A\) and \(B\) have color \(1-\beta\), then
\[
s(\pi')<s(\pi).
\]

**Proof.**
After the reversal, every triple from position \(r-2\) through the end has color \(1-\beta\). Hence no switch remains at or after position \(r-2\). Before that position the triple-color word is unchanged. In the original order there was at least the switch
\[
\epsilon_{r-1}\ne\epsilon_r
\]
at the beginning of the final run. Thus at least one switch is deleted and none is created earlier. \(\square\)

Therefore, if \(\pi\) minimizes \(s\) among all spanning orders, at least one of \(A,B\) must have the final-run color \(\beta\).

Equivalently, every switch-minimal order with \(s(\pi)\ge2\) exports a concrete tight-triple certificate from its final monochromatic run:

- if \(\beta=1\), then at least one of
  \[
  (v_{r-2},v_{r-1},v_n),\qquad
  (v_{r-1},v_n,v_{n-1})
  \]
  is tight;

- if \(\beta=0\), boundary reversal gives at least one of
  \[
  (v_n,v_{r-1},v_{r-2}),\qquad
  (v_{n-1},v_n,v_{r-1})
  \]
  tight.

Thus failure of the one-switch target cannot remain purely global. At the end of every switch-minimal order it forces a tight triple joining the terminal end of the order to the boundary immediately preceding the last monochromatic run.

The symmetric statement holds at the first run by reversing the whole order first.

This gives a direct bridge between the Norine-style color-word picture and the existing endpoint-transport architecture: minimizing the global number of color changes automatically produces endpoint reversal/extension data at the outermost run boundaries. The next target is to choose, among switch-minimal orders, a secondary extremal criterion on the lengths of the first and last runs and show that the two exported certificates either extend one outer run, move its boundary inward, or meet to produce a one-switch order.


### Comparison-digraph formulation of the two-color cycle

The cyclic red/blue perspective has a direct graph-theoretic formulation in the comparison digraph.

Let
\[
C=(v_1,v_2,\ldots,v_n,v_1)
\]
be an oriented Hamilton cycle of the complete graph on \(V(H)\), and let
\[
e_i=\{v_i,v_{i+1}\}
\]
with indices modulo \(n\). The edge sequence
\[
e_1,e_2,\ldots,e_n,e_1
\]
is a cycle in the underlying line graph \(L(K_{V(H)})\) of the comparison digraph \(\Gamma(H)\).

Color the transition from \(e_{i-1}\) to \(e_i\) red when
\[
e_{i-1}\longrightarrow e_i
\]
is an arc of \(\Gamma(H)\), and blue when the comparison arc points in the opposite direction. Equivalently, the transition at \(v_i\) is red exactly when
\[
(v_{i-1},v_i,v_{i+1})
\]
is tight.

A consecutive red segment of the edge sequence is therefore a directed path of \(\Gamma(H)\), and the corresponding vertex segment of \(C\) is a tight path in the displayed direction. A consecutive blue segment becomes a directed path after reversing its edge order, and the corresponding vertex segment of \(C\) is a tight path in the reverse direction.

Hence:

**Two-component cycle lemma.**
If some Hamilton cycle \(C\) has at most two monochromatic components in this red/blue transition coloring, then
\[
\operatorname{pc}(H)\le2.
\]

**Proof.**
If all transitions have one color, orient \(C\) in the direction that makes them red and break it at any ordinary edge; the resulting spanning vertex path is tight.

Otherwise there are exactly two color changes. Cut \(C\) at the two ordinary cycle edges lying between the two monochromatic transition components. This partitions \(V(H)\) into two ordinary vertex paths. Traverse the red component in the displayed direction and the blue component in the reverse direction. Every internal consecutive triple in each resulting path is tight, so the two paths form a two-cover. \(\square\)

Thus the Norine-style target can be stated without reference to triple-color words:

> Find a Hamilton cycle of \(K_{V(H)}\) whose induced cycle in the oriented line graph \(\Gamma(H)\) has at most two maximal directed segments, allowing the two segments to be traversed in opposite directions.

This is precisely the user's red-edge/blue-nonedge picture: along the induced line-graph cycle, red means that the required comparison arc is present in the traversal direction and blue means that it is present only in the reverse direction.

There is also a natural local move. Choose two nonadjacent ordinary edges of \(C\) and perform the usual two-edge exchange that reverses the vertex interval between them. On the induced line-graph cycle:

- every transition strictly outside the reversed interval keeps its color;
- every transition strictly inside the reversed interval has its color complemented;
- only the four transition positions at the two splice ends are not determined from the old coloring.

Therefore every color change strictly inside either unaffected region is preserved. Any change in the number of monochromatic components is controlled entirely by the four splice transition positions.

This is the cycle analogue of the last-run reversal lemma. It suggests an extremal strategy: choose a Hamilton cycle minimizing the number of monochromatic components, then analyze a two-edge exchange whose cuts lie at two color-change boundaries. The interior components merely reverse color; failure to reduce the global component count is witnessed at the four splice positions. In a boundary tournament those four positions are governed by four local comparison tournaments, so the global obstruction is forced into bounded endpoint data.

The useful distinction from the earlier endpoint route is that the Hamilton cycle itself supplies both fronts simultaneously. A successful two-edge exchange lowers the number of color components globally; an unsuccessful exchange records local comparison data at both chosen run boundaries. The next target is to determine whether two suitably separated color-change boundaries can always be paired so that the four splice comparisons reduce the component count, or else force one of the already-known Hamiltonian four-/five-support configurations.


### Universal marking removes certificate-preservation bookkeeping

Article V now contains the following general fact.

**Universal marking lemma.** If \(\operatorname{pc}(H)\ge3\), then every spanning three-cover of \(H\) already carries an external tight triple reversing a displayed end edge.

Indeed, two singleton components would combine into a tight two-vertex path and give a two-cover with the third component. Hence two displayed components \(A,B\) are nontrivial. Their union is non-Hamiltonian, so one of the two junction triples of the displayed concatenation \(AB\) is non-tight; its boundary flip reverses the terminal edge of \(A\) or the initial edge of \(B\).

Consequently a global \(\Phi\)-minimum among all spanning three-covers is automatically a global marked-reversal minimum. Strict \(\Phi\)-descent never needs to preserve a chosen reversal certificate: the destination three-cover supplies another certificate automatically.

This simplifies the interpretation of the explicit cross-corner moves. Their value is to produce concrete descent or positioned geometry, not to carry a particular mark all the way to the global minimum.

### Correction to the version-17 minimum language

Article IV Corollary 20 already shows that an endpoint-pair rooted square can be componentwise \(\Phi\)-minimal only in profile
\[
3\mid4\mid4,
\]
and hence only at order eleven. Therefore the version-17 corollary stated for a componentwise-minimal rooted square of order at least thirteen is vacuous.

The one-step bad-cross transport lemma itself remains valid. What is withdrawn is only the claim that such an order-\(\ge13\) minimum must export a reversal front. At order at least thirteen the rooted square is known *not* to be terminal somewhere in its repartition component.

Moreover, an exported reversal from the one-step lemma no longer has the special deleted-label cross form, so literal iteration of that same lemma is not justified. The cycle/switch-minimal route of versions 18--19 is the more natural place for an actual distance-type monotone.

### Consequence for the cycle route

The universal marking lemma and the comparison-cycle formulation complement one another cleanly:

- the three-cover architecture may descend freely in \(\Phi\), since every intermediate state remains marked automatically;
- the Hamilton-cycle architecture keeps one global carrier fixed and measures monochromatic components directly, so local two-edge exchanges retain the positional information needed for a front argument.

Thus the live direct target should remain the version-19 two-edge-exchange problem: choose a Hamilton cycle minimizing its number of red/blue transition components, pair two color-change boundaries, and show that either the exchange lowers the component count or the four exceptional splice comparisons force one of the already-developed bounded-support configurations.


### Exact junction obstruction inside the cycle route

Let \(P=(p_1,\ldots,p_r)\) and \(Q=(q_1,\ldots,q_s)\) be disjoint tight paths with \(r,s\ge3\). Consider the cyclic vertex order
\[
(p_1,\ldots,p_r,q_s,\ldots,q_1).
\]
Windows internal to \(P\) are tight; windows internal to the reversed displayed order of \(Q\) are non-tight.

Only four junction windows are uncontrolled:
\[
A=(p_{r-1},p_r,q_s),\quad B=(p_r,q_s,q_{s-1}),
\]
\[
C=(q_2,q_1,p_1),\quad D=(q_1,p_1,p_2).
\]
Writing tight as \(1\) and non-tight as \(0\), the first junction is the word \(1,A,B,0\), so it is monotone exactly unless \((A,B)=(0,1)\). The second is \(0,C,D,1\), so it is monotone exactly unless \((C,D)=(1,0)\).

Hence this cycle has at most two monochromatic components unless at least one end is a reciprocal endpoint obstruction. At the terminal end the forbidden pattern is equivalent to
\[
(q_s,p_r,p_{r-1}),\qquad (p_r,q_s,q_{s-1})
\]
both tight. At the initial end it is equivalent to
\[
(q_2,q_1,p_1),\qquad (p_2,p_1,q_1)
\]
both tight. The equivalence is just boundary reversal of the non-tight member of the corresponding junction pair.

Therefore every displayed two-cover with both sides of order at least three satisfies
\[
\boxed{\text{two cyclic runs, or a reciprocal endpoint square}.}
\]

The reversed copy of \(Q\) is used only as a cyclic ordering for the red/blue transition word, not as a tight path. Thus this avoids the invalid orientation move corrected in version 14.

For a deletion cover \(H-x=P\mid Q\), the omitted vertex \(x\) already reverses every displayed end edge of \(P\) and \(Q\). In the reciprocal-square branch, each of the two end edges at that junction therefore has two distinct exterior reversers: \(x\) and the opposite path endpoint. This gives a canonical five-vertex double-reverser interface and connects the cycle obstruction directly to the established four-support machinery.



### Run-reversal certificate in a component-minimal Hamilton cycle

Let
\[
C=(v_0,v_1,\ldots,v_{n-1},v_0)
\]
be a Hamilton cycle whose tight/non-tight transition coloring has the minimum possible number of monochromatic components. Assume this minimum is greater than two.

Let the transitions centered at
\[
v_a,v_{a+1},\ldots,v_b
\]
form one maximal monochromatic run of color \(\beta\), and suppose \(b-a+1\ge3\). The neighboring transition components therefore have color \(1-\beta\).

Reverse the vertex interval
\[
(v_a,v_{a+1},\ldots,v_b).
\]
Locally the new cycle is
\[
\ldots,v_{a-2},v_{a-1},v_b,v_{b-1},\ldots,v_a,v_{b+1},v_{b+2},\ldots.
\]

For every \(a<j<b\), the new transition centered at \(v_j\) is the boundary reversal of the old transition centered at \(v_j\), so its color changes from \(\beta\) to \(1-\beta\).

Only four new transitions are not determined by the old run:
\[
(v_{a-2},v_{a-1},v_b),\qquad
(v_{a-1},v_b,v_{b-1}),
\]
\[
(v_{a+1},v_a,v_{b+1}),\qquad
(v_a,v_{b+1},v_{b+2}).
\]

If all four had color \(1-\beta\), then after the interval reversal the entire old \(\beta\)-run, together with its two splice neighborhoods, would have color \(1-\beta\). The two neighboring \(1-\beta\) components would merge and the \(\beta\)-component would disappear. Thus the number of monochromatic components would decrease by two, contradicting minimality.

Hence at least one of the four displayed splice transitions has color \(\beta\).

Equivalently, every monochromatic run of length at least three in a component-minimal cycle with more than two runs carries a four-position certificate preventing its elimination by the natural two-edge exchange. If \(\beta=1\), the certificate is itself a tight crossing triple. If \(\beta=0\), boundary reversal converts the certified non-tight triple into a tight crossing triple in the reverse direction.

This gives the exact bounded obstruction sought in the two-edge-exchange program. The next target is to compare the certificates carried by adjacent runs. A pair that is simultaneously compatible with the corresponding two interval reversals should lower the component count; failure should force a bounded reciprocal-reversal configuration.


### Permutahedral near-rook labeling from first and last switches

The combinatorial-topology toolkit suggests encoding a hypothetical failure of the one-switch target directly on the permutahedron.

Let
\[
\pi=(v_1,\ldots,v_n)
\]
be a spanning order and put \(m=n-2\). Write
\[
\epsilon_i(\pi)\in\{0,1\},\qquad 1\le i\le m,
\]
for the tightness indicator of the consecutive triple beginning at \(v_i\). Let
\[
S(\pi)=\{\,j:1\le j\le m-1,\ \epsilon_j(\pi)\ne\epsilon_{j+1}(\pi)\,\}
\]
be its switch set.

Assume throughout this subsection that no spanning order has at most one switch. Then
\[
|S(\pi)|\ge2
\]
for every \(\pi\). Define
\[
a(\pi)=\min S(\pi),\qquad b(\pi)=\max S(\pi),
\]
and the transformed pair label
\[
q(\pi)=\bigl(a(\pi),\,m-b(\pi)\bigr).
\]

#### Exact antipodal rule

Let \(A\pi=\pi^{\rm rev}\). Boundary reversal gives
\[
\epsilon_i(A\pi)=1-\epsilon_{m+1-i}(\pi).
\]
Therefore
\[
S(A\pi)=\{\,m-j:j\in S(\pi)\,\},
\]
so
\[
a(A\pi)=m-b(\pi),\qquad b(A\pi)=m-a(\pi).
\]
Consequently
\[
\boxed{q(A\pi)=\tau q(\pi),}
\]
where \(\tau(x,y)=(y,x)\).

This is exactly the antipodal coordinate-swap rule appearing in the Wu--Yang rook-labeling reduction.

The label is diagonal precisely when
\[
a(\pi)+b(\pi)=m.
\]
Thus a diagonally labeled order is a concrete singular configuration: its first and last switch positions are mirror images about the center of the triple-status word.

#### The source sphere is the permutahedron

Represent an ordering \(\pi\) by its position vector
\[
p_\pi:V(H)\to\{1,\ldots,n\},
\qquad
p_\pi(v_i)=i.
\]
These vectors are the vertices of the standard \((n-1)\)-dimensional permutahedron. Its edges join orders that differ by an adjacent transposition. After centering, the central symmetry
\[
p(v)\mapsto n+1-p(v)
\]
is exactly order reversal. Hence the boundary of the permutahedron is an antipodal \((n-2)\)-sphere whose vertices are precisely the spanning orders.

#### Adjacent transpositions satisfy a near-rook condition

Suppose \(\pi'\) is obtained from \(\pi\) by swapping the vertices in positions \(k,k+1\).

Only consecutive triples whose starting positions lie in
\[
[k-2,k+1]
\]
can change their tightness status. Therefore switch indicators can change only at positions
\[
W_k=[k-3,k+1]\cap[1,m-1].
\]

It follows that if \(S(\pi)\) contains a switch strictly to the left of \(W_k\), then
\[
a(\pi')=a(\pi),
\]
while if \(S(\pi)\) contains a switch strictly to the right of \(W_k\), then
\[
b(\pi')=b(\pi).
\]

Hence:

**Near-rook lemma.**
For every edge \(\pi\pi'\) of the permutahedron, either the labels \(q(\pi),q(\pi')\) share their first coordinate, or they share their second coordinate, or
\[
S(\pi)\cup S(\pi')\subseteq W_k.
\]

**Proof.**
If the first coordinates differ, there can be no switch of \(\pi\) left of \(W_k\), since all switch indicators there are unchanged. If the second coordinates differ, then \(b(\pi')\ne b(\pi)\), so there can be no switch of \(\pi\) right of \(W_k\). Thus if both coordinates change, all switches of \(\pi\) lie in \(W_k\). Since switch indicators outside \(W_k\) are identical in \(\pi,\pi'\), the same holds for \(\pi'\). \(\square\)

The exceptional window contains at most five switch positions. Therefore all color changes in both adjacent orders are confined to at most six consecutive triple positions, hence to at most eight consecutive vertices of the order.

So failure of the exact rook condition is not diffuse: it is an eight-vertex local obstruction.

#### Topological trichotomy

The preceding construction reduces the topology route to three sharply separated possibilities.

1. **Diagonal singularity.**
   Some spanning order satisfies
   \[
   a(\pi)+b(\pi)=m.
   \]
   The transformed root label
   \[
   e_{a(\pi)}-e_{m-b(\pi)}
   \]
   vanishes.

2. **Compact switch window.**
   Some permutahedron edge changes both rook coordinates. Then all switches in both endpoint orders lie inside five consecutive switch positions, supported on at most eight consecutive vertices.

3. **Genuine off-diagonal rook data.**
   Every label is off-diagonal and every permutahedron edge preserves one coordinate. Then
   \[
   q:V(\operatorname{Perm}_n)\to\Omega_{n-3}
   \]
   is an antipodal rook labeling of the permutahedron graph.

The Wu--Yang proof architecture is directly relevant to case 3. Their algebraic Borsuk--Ulam obstruction itself only asks for an augmented exact source chain complex with a free involution; the boundary chains of the centrally symmetric permutahedron satisfy the analogous source-side topological hypotheses. The cube-specific part is the **chain realization** of a rook labeling: Freudenthal subdivision produces gallery simplices, and the rook-gallery root labels define radial polyhedral chains.

Thus the precise topology problem is now:

> **Permutahedral rook-chain target.**
> Construct, from an antipodal rook labeling of the vertices of the permutahedron boundary, an equivariant augmentation-preserving chain map into the Wu--Yang root-sphere polyhedral chain complex.

A natural candidate is a triangulation or cellular gallery decomposition of permutahedral faces in which the relevant simplex vertices can be ordered through adjacent-transposition edges. Existing \(W\)-permutahedron triangulations are plausible candidates, but the required gallery/rank property must be verified rather than assumed.

If this chain-realization target is established, the chain-level Borsuk--Ulam obstruction eliminates case 3. The route would then reduce the grand problem to the two explicit singular configurations above: a centrally balanced first/last switch pair or an at-most-eight-vertex compact switch window.

This is the concrete content supplied by the topology toolkit: one precise missing chain construction, while every failure of the rook hypotheses is already localized into bounded combinatorial geometry.



### Universal run certificate, including isolated runs

The run-reversal certificate can be made uniform over all run lengths.

Let
\[
C=(v_0,v_1,\ldots,v_{n-1},v_0)
\]
be a Hamilton cycle minimizing the number of monochromatic transition components, and suppose this minimum exceeds two. Let
\[
v_a,v_{a+1},\ldots,v_b
\]
be the transition centers of an arbitrary maximal monochromatic run of color \(\beta\). The neighboring transitions centered at \(v_{a-1}\) and \(v_{b+1}\) have color \(1-\beta\).

Reverse the enlarged vertex interval
\[
(v_{a-1},v_a,\ldots,v_b,v_{b+1}).
\]
The new local order is
\[
\ldots,v_{a-2},v_{b+1},v_b,\ldots,v_a,v_{a-1},v_{b+2},\ldots.
\]

For every \(a\le j\le b\), the new transition centered at \(v_j\) is the boundary flip of the old transition centered at \(v_j\). Hence the whole old \(\beta\)-run changes to color \(1-\beta\), even when \(a=b\).

Only four splice transitions are uncontrolled:
\[
(v_{a-3},v_{a-2},v_{b+1}),\qquad
(v_{a-2},v_{b+1},v_b),
\]
\[
(v_a,v_{a-1},v_{b+2}),\qquad
(v_{a-1},v_{b+2},v_{b+3}),
\]
with indices read cyclically.

If all four had color \(1-\beta\), the old \(\beta\)-component would disappear and the two neighboring \(1-\beta\) components would merge through the complemented interval. Thus the total number of monochromatic components would drop by two, contradicting minimality.

Therefore at least one of the four displayed splice transitions has color \(\beta\).

So every monochromatic run, including an isolated one-transition run, carries a four-position certificate of its own color. For a red run this certificate is directly a tight crossing triple; for a blue run, boundary reversal converts the certified blue triple into a tight crossing triple in the reverse direction.

There is consequently no short-run residue in the Hamilton-cycle program. A hypothetical component-minimal cycle with more than two runs assigns bounded crossing data to every run around the full cyclic run decomposition. This is the natural combinatorial object to compare with the permutahedral near-rook labels of version 23.



### Certificate-orientation dichotomy on the cyclic run decomposition

Retain a component-minimal Hamilton cycle with more than two monochromatic runs. For each run \(R\), the universal run-certificate lemma gives at least one certified splice on the left side of the reversed interval or on the right side. Call \(R\) left-certified or right-certified accordingly; a run may be certified on both sides.

Consider a boundary shared by consecutive runs \(R_i,R_{i+1}\). Call it a **facing boundary** if \(R_i\) is right-certified and \(R_{i+1}\) is left-certified.

**Lemma.** Either some run boundary is facing, or all runs are certified coherently in one cyclic direction: every run is right-certified and no run is left-certified, or every run is left-certified and no run is right-certified.

**Proof.** Suppose no boundary is facing. If some run \(R_i\) is right-certified, then \(R_{i+1}\) cannot be left-certified. Since \(R_{i+1}\) has at least one certified side, it must be right-certified. Iterating around the cyclic sequence of runs shows that every run is right-certified. Returning to \(R_i\), its predecessor is right-certified, so \(R_i\) cannot be left-certified; the same argument at every boundary shows that no run is left-certified.

If no run is right-certified, then every run is left-certified. \(\square\)

Thus the global obstruction has only two qualitative forms:

1. **certificate collision:** two adjacent runs have certificates directed across their common boundary;
2. **coherent winding:** every run certificate points in the same cyclic direction.

The first branch is a local combinatorial collision problem. The second branch is a genuinely global oriented winding pattern and is the natural branch to compare with the antipodal permutahedral near-rook labeling.


### Color-refined near-rook label

Retain the first and last switch positions a(pi), b(pi), put m=n-2, and let alpha(pi) and omega(pi) be the first and last triple colors. Define
Q(pi)=((a(pi),alpha(pi)),(m-b(pi),1-omega(pi))).

Reversal swaps these two coordinates exactly. Across an adjacent-transposition edge of the permutahedron, one full coordinate is preserved unless every switch of both endpoint orders lies in the same five consecutive switch positions; the proof is the same locality calculation as for the uncolored near-rook label, with the outer colors unchanged whenever the corresponding extreme switch lies outside the exceptional window.

The label is diagonal exactly when
a(pi)+b(pi)=m
and alpha(pi)=1-omega(pi).
Equivalently, the two outer monochromatic runs have equal length and the total number of switches is odd.

Thus the topology branch sharpens to three cases: a reflected odd-run singularity, a compact at-most-eight-vertex switch window, or a genuine antipodal color-refined rook labeling on the permutahedron graph.

This meshes with the run-certificate dichotomy: local certificate collision belongs to the bounded branch, while coherent cyclic winding is the natural regime for the antipodal rook-chain obstruction.



### A recent permutahedron triangulation does not by itself realize the rook labels

A natural possible shortcut for the version-23/28 topology branch is to use the recent Brady--Delucchi--Watt triangulation of the permutahedron (arXiv:2607.07567).

That shortcut does not automatically work. Their special top-dimensional simplices have ordered vertices
\[
w_0(v_0),w_1(v_0),\ldots,w_n(v_0)
\]
with
\[
w_i=w_{i-1}R(\theta_i)
\]
and with standard Coxeter length increasing by one at each step. Thus consecutive simplex vertices are Bruhat covers obtained by arbitrary reflections. They need not differ by a simple reflection, hence need not be joined by an edge of the permutahedron.

Our near-rook condition is proved only for genuine permutahedron edges, namely adjacent transpositions of the spanning order. Therefore the color/switch label cannot simply be propagated along the edges of those special simplices.

So the recent triangulation supplies a useful geometric model but does not close the chain-realization target without an additional lemma converting its Bruhat-cover edges into sequences on which rook-coordinate preservation is controlled.

Reference: Brady, Delucchi, Watt, "Triangulating the Permutahedron", arXiv:2607.07567, especially Definition 3.2 and Proposition 3.1.

### Coxeter 2-faces: squares fill; singular hexagons localize

Return to the uncolored rook label q(pi)=(a(pi),m-b(pi)), whose root vector is
phi(pi)=e_a-e_{m-b}
in the sum-zero hyperplane on coordinates {1,...,m-1}. Reversal sends phi to -phi. This uncolored target has the right dimension for Borsuk--Ulam; the color-refined label remains diagnostic only.

Assume the compact-window edge singularity does not occur, so every permutahedron edge is a genuine rook move.

For a Coxeter square, an irreducible label loop has the form
(a,b),(a,c),(d,c),(d,b).
All four labels are off-diagonal, so {a,d} is disjoint from {b,c}. Hence the convex hull of the four roots is separated from 0 by the linear functional summing coordinates in {a,d}; it takes value 1 on every vertex. Thus every square label loop fills in the punctured root space.

For a braid hexagon, after removing reducible row/column shortcuts, an irreducible rook loop has labels
(r1,c1),(r1,c2),(r2,c2),(r2,c3),(r3,c3),(r3,c1).
If the row set and column set do not form the cyclic identification
r1=c3, r2=c1, r3=c2
(up to cyclic relabeling), the convex hull of the six roots avoids 0. Indeed 0 in the convex hull is equivalent to a nonzero balanced circulation in the directed label graph with arcs r_i->c_i and r_i->c_{i+1}; off-diagonality allows each r_i to coincide only with c_{i-1}, so a circulation forces all three cyclic identifications. In the exceptional case the three roots e_{r1}-e_{c1}, e_{r2}-e_{c2}, e_{r3}-e_{c3} sum to 0.

Moreover an irreducible braid hexagon alternates which rook coordinate changes on the two generators s_k,s_{k+1}. A first-coordinate change forbids switches left of the corresponding exceptional window W, and a second-coordinate change forbids switches right of W. Since W_k union W_{k+1} consists of at most six consecutive switch positions, every switch in all six chamber orders is confined there. Hence the singular braid hexagon is supported on at most nine consecutive vertices.

Therefore, unless a bounded nine-vertex switch-window singularity occurs, the odd root map on the permutahedron 1-skeleton extends equivariantly over the entire 2-skeleton.

Since the target root sphere has dimension m-3, it is (m-4)-connected. Consequently this 2-skeleton map extends automatically, cell by cell, through the (m-3)-skeleton. Only the top three cellular dimensions remain capable of carrying a genuine obstruction. This sharply isolates where the Wu--Yang-type chain machinery is actually needed.


### Cellular Tucker reduction to a fully sign-paired permutahedron face

Let X be the boundary CW complex of the n-permutahedron, so |X| is an m-sphere with m=n-2 and antipode given by order reversal. Assume the version-30 signed chamber label lambda takes values in {+-1,...,+-(m-1)} and satisfies lambda(A pi)=-lambda(pi).

Call a nonempty face F of X sign-paired if, for every magnitude i that occurs among labels of vertices of F, both +i and -i occur on F.

Lemma. Some face of X is sign-paired.

Proof. Suppose not. For each nonempty face F choose the smallest magnitude i for which labels of magnitude i occur on F with only one sign, and label the barycentric vertex [F] by that signed i. This is well-defined by the assumption that F is not sign-paired. Antipodality of lambda gives mu(-F)=-mu(F). If F is contained in G and |mu(F)|=|mu(G)|=i, the signs must agree: F contains a vertex carrying the sign chosen on F, and G contains F, while i occurs with only one sign on G. Hence an edge [F][G] of the barycentric subdivision can never be complementary. Therefore mu is an antipodal Tucker labeling of an antipodal triangulation of S^m using only m-1 absolute labels and with no complementary edge. Ky Fan/Tucker forbids this. Contradiction.

Thus the topological obstruction can be realized inside one actual permutahedron face: every signed magnitude visible on that face is represented in both orientations. This bypasses the unresolved top-three-dimensional extension problem from version 31.

A face of the permutahedron is an ordered set partition; its vertices are exactly the spanning orders obtained by permuting entries within the fixed contiguous blocks. Hence the next combinatorial target is concrete: analyze an inclusion-minimal sign-paired ordered-partition face and show that complementary signed switch labels inside one block-product either force a compact switch window or a two-run spanning cycle.


### Convex-root cycle criterion inside a Tucker face

For any collection E of off-diagonal uncolored rook labels (i,j), let
R(E)={e_i-e_j:(i,j) in E}
and let D(E) be the directed graph with arc i->j for each label.

**Lemma.** The origin lies in conv R(E) if and only if D(E) contains a directed cycle.

A directed cycle gives roots summing to zero. Conversely, a convex combination summing to zero is a nonzero nonnegative balanced circulation on D(E), and every finite nonzero circulation contains a directed cycle. Equivalently, if D(E) is acyclic, a topological ordering h gives h(i)>h(j) on every arc and the functional sum h(i)x_i strictly separates all roots from zero.

Therefore any permutahedron face F whose chamber labels q(pi)=(a(pi),m-b(pi)) form an acyclic extreme-switch digraph can be filled in the punctured root space using any vertex triangulation of F; diagonals need no separate rook control because the entire convex hull already avoids zero.

So every genuinely root-topological face contains a directed switch-front cycle
x_1 -> x_2 -> ... -> x_t -> x_1,
meaning that for orders pi_i in one ordered-partition face,
a(pi_i)=x_i and m-b(pi_i)=x_{i+1}.

This complements the cellular Tucker reduction. Tucker supplies an actual sign-paired face without solving the full chain-extension problem; the convex-root lemma supplies an independent structural test inside such a face. If its uncolored label digraph is acyclic, that face is root-harmless despite being sign-paired under the compressed signed labels. Hence an inclusion-minimal Tucker face should next be split into the acyclic compressed-label phenomenon versus a genuine directed extreme-switch cycle.

The directed-cycle interpretation also explains the coherent-winding branch of the Hamilton-cycle certificates: both are literal cyclic transport of an outer switch front rather than merely an analogy.


### Tucker plus near-rook gives a four-unit near-diagonal order

Put m=n-2 and, for a spanning order pi with at least two switches, let x=a(pi) be its first switch position and y=m-b(pi) its reflected last-switch coordinate. Since a<b,

x+y <= m-1.

If x=y, then a(pi)+b(pi)=m, the exact diagonal singularity already isolated earlier. Assume no such order exists. Define a signed label

lambda_0(pi)=+x if x<y, and lambda_0(pi)=-y if y<x.

Then reversal swaps x and y, so lambda_0(pi^rev)=-lambda_0(pi). Moreover |lambda_0|=min{x,y}<=floor((m-1)/2), giving far fewer than m absolute labels on the antipodal m-sphere. Apply the cellular Tucker face lemma of version 32 to lambda_0. Some permutahedron face is sign-paired. Its graph is connected, so there is an edge pi pi_prime on a path between vertices of opposite sign at which the sign changes.

If this edge is one of the exceptional near-rook failures, all switches of its endpoint orders lie in the known five-position switch window, hence on at most eight consecutive vertices.

Otherwise the edge is a genuine rook move for q=(x,y): one coordinate is fixed. Suppose y is fixed and the first coordinate changes from x to x_prime. A sign change means, after interchanging the endpoints if necessary,

x<y<x_prime.

Because the first coordinates differ across the adjacent transposition, the near-rook proof says neither order has a switch strictly left of the exceptional window W_k=[k-3,k+1]. Hence both first-switch positions x,x_prime belong to W_k. Since W_k is an interval and y lies between them, y also belongs to W_k. Therefore

|x-y|<=4 and |x_prime-y|<=4.

The case in which x is fixed and y changes is symmetric.

Consequently every hypothetical failure of the one-switch target satisfies at least one of:

1. exact diagonal: a(pi)+b(pi)=m for some spanning order;
2. compact window: all switches of some order lie in at most five consecutive switch positions;
3. near diagonal: for some spanning order,
   1<=|a(pi)+b(pi)-m|<=4.

Thus the cellular Tucker obstruction can be converted from a whole-face statement into a single spanning order whose two outer switch fronts are mirror-symmetric to within four positions, unless the obstruction is already supported on at most eight consecutive vertices.



### Direct face balancing by root averages

The full uncolored root labels give a stronger face-localization than the compressed Tucker labels.

Assume every spanning order has at least two switches. Put \(m=n-2\), and for a spanning order \(\pi\) set
\[
q(\pi)=(a(\pi),m-b(\pi)),\qquad
\phi(\pi)=e_{a(\pi)}-e_{m-b(\pi)}
\]
in the sum-zero subspace of \(\mathbb R^{m-1}\). Reversal gives
\[
\phi(\pi^{\rm rev})=-\phi(\pi).
\]

If some \(\phi(\pi)=0\), then \(a(\pi)+b(\pi)=m\), giving the exact diagonal branch. Hence assume all chamber roots are nonzero.

**Face-balancing lemma.**
Some nonempty proper face \(F\) of the permutahedron satisfies
\[
0\in\operatorname{conv}\{\phi(\pi):\pi\in V(F)\}.
\]

**Proof.**
Suppose every face-root convex hull avoids \(0\). For each nonempty proper face \(F\), define
\[
z_F=\frac1{|V(F)|}\sum_{\pi\in V(F)}\phi(\pi).
\]
Then \(z_F\ne0\), and \(z_{-F}=-z_F\).

Use \(z_F\) as the value at the barycentric vertex corresponding to \(F\), and extend affinely over the barycentric subdivision of the permutahedron boundary. Consider a barycentric simplex
\[
F_0\subset F_1\subset\cdots\subset F_k.
\]
Because \(0\) is outside the convex hull of the chamber roots of \(F_k\), strict separation gives a linear functional \(L\) that is positive on every \(\phi(\pi)\) for \(\pi\in V(F_k)\). Since \(F_i\subseteq F_k\),
\[
L(z_{F_i})>0
\]
for every \(i\). Hence the affine image of the whole barycentric simplex avoids \(0\).

This gives a continuous antipodal map
\[
S^m\longrightarrow
\mathbb R^{m-2}\setminus\{0\}\simeq S^{m-3},
\]
contradicting Borsuk--Ulam. \(\square\)

By the convex-root cycle criterion, such a balanced face contains a directed cycle in its extreme-switch digraph. Thus there are chamber orders
\[
\pi_1,\ldots,\pi_t
\]
in one ordered-partition face and coordinate symbols \(x_1,\ldots,x_t\) such that cyclically
\[
q(\pi_i)=(x_i,x_{i+1}),
\]
equivalently
\[
a(\pi_i)=x_i,\qquad m-b(\pi_i)=x_{i+1}.
\]

So the topology branch admits a direct reduction, independent of the compressed Tucker label and independent of a global chain realization:

> one actual ordered-partition face contains a directed cycle of first-switch to reflected-last-switch fronts.

The next target is an inclusion-minimal root-balanced face. Versions 31 and 34 already show that dimension-one and nonsingular dimension-two behavior is harmless or bounded, so a minimal higher-dimensional balanced face is the genuinely global residue.


### Any genuine topological obstruction lives on at most four ordered blocks

Assume the bounded singular branches from the Coxeter 2-face analysis do not occur. Version 31 then gives an equivariant root map on the permutahedron boundary that extends through the entire (m-3)-skeleton, where m=n-2. Since an antipodal map S^m -> S^{m-3} cannot exist, extension must fail on some cell F of dimension d at least m-2.

A face of the n-permutahedron corresponding to an ordered set partition into t blocks has dimension n-t. Since n=m+2 and d>=m-2,

t=n-d <= (m+2)-(m-2)=4.

Because F is a proper boundary face, t>=2. Therefore the first genuinely topological obstruction may be chosen on a face with exactly 2, 3, or 4 ordered blocks. Equivalently, after excluding the bounded nine-vertex braid singularity, the global topology is supported on a product

Perm(B_1) x ... x Perm(B_t),  2<=t<=4,

where the blocks occur as fixed contiguous intervals in every spanning order belonging to F.

Thus the topological branch has a concrete macrostructure: either a compact bounded switch window occurs, or all remaining obstruction is already visible while only two, three, or four contiguous vertex blocks are allowed to permute internally. The next target is to determine which block can control the first switch and which can control the reflected last switch; if these controls lie in independent end blocks, the product structure should permit a filling, so a genuine obstruction should force both switch fronts into one common block or adjacent blocks.
