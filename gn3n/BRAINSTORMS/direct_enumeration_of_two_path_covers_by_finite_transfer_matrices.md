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


### Correction to the v34 four-unit near-diagonal claim

The v34 inference that both old and new first-switch positions must lie in the affected five-position window of an adjacent transposition is too strong.

Let W=[k-3,k+1] be the only switch positions whose indicators can change under swapping positions k,k+1. If the first switch changes from x' to an earlier x, then x is forced into W, but x' may lie arbitrarily far to the right: the swap can create a new early switch inside W while the old first switch remains unchanged farther out. Thus a rook-edge sign change does not by itself imply |x-y|<=4.

The same issue applies symmetrically to a last-switch jump. Therefore the constant-four near-diagonal conclusion of v34 is withdrawn. The exact diagonal and compact-window branches remain valid, and the later v35 face-balancing/root-cycle argument is independent of this correction.

What survives is a useful jump-corridor lemma.

**Jump-corridor lemma.**
Suppose adjacent orders pi,pi' differ only at positions k,k+1 and their first switches differ. If a(pi')=x lies in W and a(pi)=x'>max W, then:
1. x' remains a switch of pi';
2. pi' has no switch strictly between max W and x';
3. hence the triple-status word of pi' is monochromatic on that whole corridor.

Indeed all switch indicators outside W are unchanged, pi had no switch before x', and x' was itself a switch.

Thus a large extreme-switch jump creates a long monochromatic run with one end in the bounded splice window and the other at the old front. The symmetric statement holds for a last-switch jump.

Consequently, along a path inside the few-block faces isolated in v36, a change from x<y to x>y yields one of:
- an exact diagonal order;
- a bounded exceptional near-rook edge;
- a genuinely local crossing where both fronts are near the swap window;
- or a long monochromatic corridor exported from that window.

This corrected alternative interfaces naturally with the run-reversal certificate machinery: the topology can force a front crossing, while a large jump produces a long run rather than a spurious constant-distance conclusion.


### Block-separation completion forces an exact diagonal

Let F be one of the root-balanced few-block faces isolated above. Write its ordered partition as
B_1|...|B_t,
2<=t<=4,
so every vertex order of F is obtained by permuting independently inside these fixed contiguous blocks.

Suppose x is a coordinate on a directed extreme-switch cycle in F. Then there are orders pi,sigma in F with
a(pi)=x
and
m-b(sigma)=x.
Thus sigma has last switch
b(sigma)=m-x.

The first-switch condition a(pi)=x is determined entirely by the triple colors epsilon_1,...,epsilon_{x+1}, hence by the vertices in positions at most x+3. The last-switch condition b(sigma)=m-x is determined entirely by the suffix beginning at position m-x.

**Block-separation completion lemma.**
If F has a block boundary c satisfying
x+3 <= c < m-x,
then F contains an exact-diagonal order tau with
q(tau)=(x,x).

**Proof.**
Choose tau by taking the internal permutations of all blocks ending at or before c from pi and all blocks beginning after c from sigma. This is allowed by the Cartesian-product structure of F. Since positions through x+3 agree with pi, tau has first switch x. Since positions from m-x onward agree with sigma, tau has last switch m-x. Hence its reflected last coordinate is x. (square)

Consequently, in the branch where no exact diagonal order exists, every directed-cycle coordinate x satisfies:

> no face-block boundary lies in [x+3,m-x-1].

Whenever this interval is nonempty, the entire corridor between the local neighborhoods of the mirror switch fronts lies inside one permutation block.

This strongly sharpens the v36 few-block reduction. A genuinely global non-diagonal obstruction cannot keep the first and reflected-last switch fronts in independently permuting blocks; product independence would complete them to the forbidden diagonal. Instead, for every noncentral coordinate on the root cycle, one block must span the whole central corridor between the two mirror fronts.

Thus the remaining topology has a giant-block form: either the cycle coordinates are all within O(1) of the center, or a single large block reaches across a substantial central interval. The next target is to exploit internal permutations of that spanning block, together with the jump-corridor/run-reversal lemmas, to move one extreme front without disturbing the other.


### Color-sensitive face balancing and alternating switch-front cycles

The uncolored root map admits a stronger color-sensitive variant.

For a spanning order \(\pi\), put
\[
x=a(\pi),\qquad y=m-b(\pi),
\]
and let \(\alpha,\omega\in\{0,1\}\) be the first and last triple colors. Define
\[
\zeta(\pi)=(-1)^\alpha e_x+(-1)^\omega e_y
\in \mathbb R^{m-1}.
\]
Reversal swaps \(x,y\) and complements both outer colors, so
\[
\zeta(\pi^{\rm rev})=-\zeta(\pi).
\]

The only way \(\zeta(\pi)=0\) is
\[
x=y,\qquad \alpha\ne\omega,
\]
which is exactly the reflected odd-run diagonal singularity.

Assume no such singular order exists. If every permutahedron face had \(\zeta\)-convex hull avoiding \(0\), the barycentric face-average construction from version 35 would give an antipodal map
\[
S^m\longrightarrow S^{m-2},
\]
impossible by Borsuk--Ulam. Hence some actual ordered-partition face \(F\) satisfies
\[
0\in\operatorname{conv}\{\zeta(\pi):\pi\in V(F)\}.
\]

Interpret each order as an edge between the coordinate vertices \(x\) and \(y\), with half-edge signs \((-1)^\alpha\) at \(x\) and \((-1)^\omega\) at \(y\). A positive convex dependence at \(0\) says that, at every coordinate vertex, total positive half-edge weight equals total negative half-edge weight.

Such a balanced signed incidence flow decomposes into **alternating closed walks**: consecutive half-edges at each shared coordinate have opposite signs. Therefore there are orders
\[
\pi_1,\ldots,\pi_t\in V(F)
\]
whose extreme-switch coordinate edges form a closed walk and whose corresponding outer colors are opposite at every shared coordinate.

Orient every edge naturally from its first-switch coordinate \(a(\pi)\) to its reflected-last coordinate \(m-b(\pi)\). Then an alternating closed walk has one of two qualitative forms.

1. **Coherent winding.** All natural orientations run consistently around the walk. This is a color-compatible directed switch-front cycle.
2. **Source/sink collision.** At some shared coordinate the two incident natural edges both point out or both point in. In the first case, two orders in the same face have the same first-switch coordinate and opposite first colors. In the second, two orders have the same reflected-last coordinate and opposite last colors.

Thus color-sensitive Borsuk--Ulam produces more than the uncolored root cycle: either a coherent colored winding cycle or a same-front/opposite-color collision inside one few-block ordered-partition face.


### Non-diagonal few-block faces force cross-intersecting determining families

Let F=B_1|...|B_t, 2<=t<=4, be a few-block face carrying one of the directed switch-front coordinates supplied by the root-balanced or color-sensitive circulation. Fix a coordinate r that occurs both as a first-switch coordinate and as a reflected last-switch coordinate in F.

Define L_r to be the family of ordered vertex segments
(v_1,...,v_{r+3})
arising from orders pi in F with a(pi)=r. Define R_r to be the family of ordered suffix segments
(v_{m-r},...,v_n)
arising from orders sigma in F with m-b(sigma)=r. Their supports both have order r+3.

**Cross-intersection lemma.**
If F contains no exact-diagonal order q=(r,r), then every support from L_r intersects every support from R_r.

**Proof.**
Take L in L_r and R in R_r. If their supports were disjoint, use the Cartesian permutation freedom of F block by block. In every block, place the elements prescribed by L in their prescribed early positions and the elements prescribed by R in their prescribed late positions; disjointness makes these prescriptions compatible, and fill the remaining positions arbitrarily. The resulting order tau lies in F, agrees with the first witness through position r+3, and agrees with the second witness from position m-r onward. Hence a(tau)=r and m-b(tau)=r, giving q(tau)=(r,r), contradiction. (square)

In the v38 giant-central-block regime, all fixed outer blocks on the left and right are disjoint automatically. Therefore every forced intersection between L_r and R_r occurs inside the one block spanning the mirror-front corridor. The global topological obstruction is thus concentrated as a cross-intersection condition on two families of subsets of one permutation block.

Version 39 adds colors to this picture. In the coherent color-compatible circulation branch, each r comes with prescribed outer-run colors, so L_r and R_r become cross-intersecting families of colored tight-path determining segments. In the source/sink collision branch, the same coordinate r supports two determining families with opposite outer colors on the same side, giving a second local comparison problem.

This is the natural point to invoke the matching/intersection portion of the imported topology toolkit: either find disjoint representatives from the left and right determining families, which immediately completes to an exact diagonal order, or derive a structural common-intersection obstruction inside the giant block. No small-order enumeration is involved.


### Source/sink collisions force a bounded outer run

Consider the source branch from the color-sensitive alternating-walk theorem. Thus two orders \(\pi,\sigma\) in one permutahedron face have the same first-switch coordinate
\[
a(\pi)=a(\sigma)=x
\]
but opposite first triple colors.

Because the graph of every permutahedron face is connected, join \(\pi\) to \(\sigma\) by adjacent transpositions inside the face. Along this path the first triple color changes. Choose an edge \(\rho\rho'\) on which it changes.

An adjacent transposition at positions \(k,k+1\) can change the first triple color only when \(k\le3\). Consequently every triple-status position \(i\ge5\) is unchanged across \(\rho\rho'\).

If both \(a(\rho)>4\) and \(a(\rho')>4\), then in each order the status positions \(1,\ldots,5\) belong to the first monochromatic run. Since position \(5\) is unchanged across the edge, the first colors would be equal, contradiction. Hence
\[
\min\{a(\rho),a(\rho')\}\le4.
\]

Therefore a source collision forces some spanning order whose first monochromatic run has at most four triple positions. The corresponding vertex segment has order at most six and is Hamiltonian: if the run color is tight, use the displayed orientation; if it is non-tight, reverse that segment, which boundary reversal makes tight.

The sink branch is symmetric: two orders with the same reflected-last coordinate and opposite last colors force an order with
\[
m-b\le4,
\]
and hence a Hamiltonian terminal segment on at most six vertices.

Thus the color-sensitive topology splits more sharply:

1. a source/sink collision immediately produces a Hamiltonian support of order at most six;
2. only the coherently oriented alternating cycle remains genuinely global.

In a minimum counterexample, every such proper Hamiltonian support has non-Hamiltonian two-coverable complement. Hence the source/sink branch enters the existing four-/five-/six-support machinery, including the full two-label square available for Hamiltonian six-supports.


### One canonical giant block, or a three-coordinate central cycle

Let
\[
x_1\to x_2\to\cdots\to x_t\to x_1
\]
be a simple directed extreme-switch cycle in one few-block face \(F\), and assume \(F\) contains no exact diagonal order. Put
\[
r=\min_i x_i.
\]

Every arc \(x_i\to x_{i+1}\) comes from a spanning order with
\[
a=x_i,\qquad m-b=x_{i+1}.
\]
Since \(a<b\),
\[
x_i+x_{i+1}\le m-1.
\]
In particular, because every coordinate is at least \(r\),
\[
2r\le m-1.
\]

By the block-separation completion lemma, for every cycle coordinate \(x\), no face-block boundary lies in
\[
[x+3,m-x-1].
\]
When \(x\ge r\), this interval is contained in
\[
[r+3,m-r-1].
\]
Hence, if the latter interval is nonempty, it lies entirely inside one face block \(B\), and every nonempty mirror-front corridor belonging to every coordinate of the cycle lies inside this same block. Thus the giant central block is canonical: it is already determined by the minimum cycle coordinate.

There is a complementary near-central branch. If
\[
[r+3,m-r-1]
\]
is empty, then
\[
2r\ge m-3.
\]
For any cycle coordinate \(x_i\), choose one of its neighbors \(x_j\) on the directed cycle. Since \(x_j\ge r\) and
\[
x_i+x_j\le m-1,
\]
we have
\[
x_i\le m-1-r.
\]
Therefore
\[
0\le x_i-r\le m-1-2r\le2.
\]
So every cycle coordinate lies in
\[
\{r,r+1,r+2\}.
\]

Consequently the coherent-winding branch has the following exact structural dichotomy:

1. **canonical giant block:** one fixed permutation block contains every nonempty mirror-front corridor for the entire directed cycle;
2. **central three-coordinate regime:** every switch-front coordinate on a simple directed cycle belongs to three consecutive integers, so the simple cycle itself has length two or three.

This removes the ambiguity that different cycle coordinates might require different spanning blocks. The genuinely nonlocal branch is controlled by one common central permutation block; otherwise the topology has already collapsed to a two- or three-state extreme-front cycle.


### The central regime is always a two-cycle

In the central branch of version 42, let \(r\) be the minimum coordinate of a simple directed extreme-switch cycle. We know
\[
2r\ge m-3
\]
and every arc \(x\to y\) satisfies
\[
x+y\le m-1.
\]
Since some cycle coordinate is adjacent to \(r\) and is at least \(r\), also
\[
2r\le m-1.
\]
Put
\[
d=m-1-2r.
\]
Then
\[
d\in\{0,1,2\}.
\]

The case \(d=0\) is impossible: every coordinate is at least \(r\), while the arc inequality forces both endpoints of every arc to equal \(r\), giving the forbidden diagonal label \((r,r)\).

If \(d=1\), every coordinate lies in \(\{r,r+1\}\). Since diagonal arcs are excluded, the only possible simple directed cycle is
\[
r\longrightarrow r+1\longrightarrow r.
\]

If \(d=2\), every coordinate lies in \(\{r,r+1,r+2\}\). But
\[
(r+1)+(r+2)=2r+3>m-1=2r+2,
\]
so no arc can join \(r+1\) to \(r+2\) in either direction. Diagonal arcs are again excluded. Hence every simple directed cycle must use \(r\) as the intermediate vertex between any other coordinates. A simple cycle therefore has length two:
\[
r\longrightarrow s\longrightarrow r,
\qquad
s\in\{r+1,r+2\}.
\]

Thus the central coherent-winding residue consists of two spanning orders \(\pi,\sigma\) in one face with
\[
q(\pi)=(r,s),\qquad q(\sigma)=(s,r),
\qquad s-r\in\{1,2\}.
\]

In the color-compatible winding supplied by version 39, if \(\alpha_\pi,\omega_\pi\) and \(\alpha_\sigma,\omega_\sigma\) are their first and last colors, then alternation at the two shared coordinates gives
\[
\omega_\pi=1-\alpha_\sigma,
\qquad
\omega_\sigma=1-\alpha_\pi.
\]
So the near-central topology is reduced to a reciprocal pair of extreme fronts, with the two coordinates differing by at most two and with complementary cross-end colors.


### The reciprocal central pair collapses to one three-switch residue

Retain the central reciprocal pair from version 43:
\[
q(\pi)=(r,s),\qquad q(\sigma)=(s,r),
\qquad s-r\in\{1,2\}.
\]
For any order with label \(q=(x,y)\),
\[
b-a=m-x-y.
\]
Hence in the central pair
\[
b(\pi)-a(\pi)=b(\sigma)-a(\sigma)=m-r-s.
\]

The possibilities from version 43 give
\[
m-r-s\in\{1,2\}.
\]
Thus all switches of each order lie in an interval of at most three consecutive switch positions.

If \(m-r-s=1\), the first and last switches are consecutive, so the status word has exactly the form
\[
A^{r}\,\bar A\,A^{s}.
\]
Reverse the whole spanning order if necessary so that \(A\) is tight. There is then exactly one non-tight consecutive triple. Its defect line has one edge, hence matching number at most one, and the defect-line identity gives a spanning two-cover. Therefore this case is impossible in a counterexample.

Now suppose
\[
m-r-s=2.
\]
If the middle switch position is absent, the word is
\[
A^{r}\,\bar A^{\,2}\,A^{s}.
\]
Again reverse the whole order if necessary so \(A\) is tight. The two non-tight consecutive triples give two adjacent defect-line edges, whose matching number is one. Hence this case also yields a two-cover.

Therefore a counterexample can survive the central branch only when all three switch positions
\[
a,\ a+1,\ a+2
\]
are present.

This can happen only in the parameter case
\[
m-1=2r+2,\qquad s=r+1.
\]
For \(\pi\),
\[
a=r,\qquad b=r+2,
\]
and for \(\sigma\),
\[
a=r+1,\qquad b=r+3.
\]
The two status words are therefore
\[
A^{r}\,\bar A\,A\,\bar A^{\,r+1}
\]
and
\[
A'^{\,r+1}\,\bar A'\,A'\,\bar A'^{\,r}.
\]

The color-compatible alternation of version 39 forces
\[
\omega_\pi=1-\alpha_\sigma,
\qquad
\omega_\sigma=1-\alpha_\pi.
\]
Each displayed word has three switches, so its last color is the complement of its first. Substitution gives
\[
\alpha_\pi=\alpha_\sigma.
\]
Thus \(A'=A\).

So the entire near-central coherent-winding branch reduces to one exact reciprocal pattern:
\[
\boxed{
A^{r}\,\bar A\,A\,\bar A^{\,r+1}
\quad\text{and}\quad
A^{r+1}\,\bar A\,A\,\bar A^{\,r}
}
\]
on two spanning orders in one face, with the same outer starting color.

All other central reciprocal configurations already give a two-cover by the defect-line identity.


### The last central three-switch residue is also a two-cover

Version 44 left one possible near-central word:
\[
A^{r}\,\bar A\,A\,\bar A^{\,r+1},
\]
up to the reciprocal companion order.

Write the corresponding spanning order as
\[
(v_1,\ldots,v_n),
\qquad
m=n-2=2r+3.
\]
Cut the vertex order between
\[
v_{r+2}\quad\text{and}\quad v_{r+3}.
\]

The first block
\[
(v_1,\ldots,v_{r+2})
\]
has internal consecutive-triple status positions
\[
1,\ldots,r,
\]
all of color \(A\).

The second block
\[
(v_{r+3},\ldots,v_n)
\]
has internal status positions
\[
r+3,\ldots,m,
\]
all of color \(\bar A\).

The two exceptional middle status positions
\[
r+1,\qquad r+2
\]
straddle the cut and impose no condition on either path.

If \(A\) is tight, traverse the first block in the displayed direction and the second block in reverse. Every internal triple of both resulting paths is tight. If \(A\) is non-tight, reverse the first block and keep the second in the displayed direction. Again both are tight.

Thus this single order already gives a spanning two-cover.

Consequently **no near-central coherent-winding residue survives at all**. Combined with versions 42--44, every coherent winding in a counterexample must lie in the canonical giant-block branch, where the minimum switch-front coordinate has a nonempty mirror corridor and one fixed permutation block contains the mirror corridors for the entire cycle.


### Correction: the canonical giant-block reduction does not require a few-block face

Versions 38--45 were phrased as though the root-balanced face from version 35 had first been identified with the 2-, 3-, or 4-block obstruction cell from version 36. That identification has not been proved and should not be assumed.

Fortunately, the main reduction does not need it.

Let \(F\) be the arbitrary ordered-partition face supplied by version 35, and let
\[
x_1\to x_2\to\cdots\to x_t\to x_1
\]
be a simple directed cycle in its extreme-switch digraph. Write
\[
F=B_1|\cdots|B_k
\]
with no restriction on \(k\), and put
\[
r=\min_i x_i.
\]

The block-separation completion lemma uses only the Cartesian product structure of a permutahedron face: if a face-block boundary lies between the determining prefix for first switch \(x\) and the determining suffix for reflected last switch \(x\), the two witness orders can be combined blockwise to produce an exact diagonal order \(q=(x,x)\).

Therefore, in the no-diagonal branch, no block boundary lies in
\[
[x+3,m-x-1]
\]
for any cycle coordinate \(x\). In particular, if
\[
[r+3,m-r-1]\ne\varnothing,
\]
this entire interval lies inside one block \(B\). Since every other cycle coordinate satisfies \(x\ge r\),
\[
[x+3,m-x-1]\subseteq [r+3,m-r-1],
\]
so the same block \(B\) contains every nonempty mirror-front corridor on the entire cycle.

If the minimum corridor is empty, the arithmetic argument of versions 42--45 applies without any block-count hypothesis and produces a spanning two-cover.

Hence version 35 alone, together with block separation and the central-word analysis, gives the unconditional topology reduction:

> Every counterexample contains an ordered-partition face with a directed extreme-switch cycle whose minimum coordinate \(r\) has a nonempty mirror corridor, and one canonical permutation block contains every mirror-front corridor of that cycle.

The 2-, 3-, or 4-block statement of version 36 remains a separate observation about a particular cellular obstruction construction. It is not used in the canonical giant-block reduction.

Likewise, the cross-intersection lemma of version 40 is valid for an arbitrary ordered-partition face. Once the canonical block \(B\) contains the mirror corridor, the determining prefix and suffix supports can intersect only through the relevant portions of \(B\); no bound on the number of outer blocks is needed.


### Correct giant-block cross-intersection at the minimum winding coordinate

The cross-intersection statement of version 40 needs the determining position windows to be disjoint. That hypothesis is automatic for the minimum coordinate in the surviving giant-block branch.

Let
x_1 -> ... -> x_t -> x_1
be the simple directed extreme-switch cycle from the root-balanced face, and put
r=min_i x_i.
The near-central branch has been eliminated in versions 42--45, so the mirror corridor
[r+3,m-r-1]
is nonempty. Hence
2r<=m-4,
and the two determining position windows
P=[1,r+3],
Q=[m-r,n]
are disjoint.

Assume there is no exact diagonal order q=(r,r). By block separation, no face-block boundary lies between r+3 and m-r. Therefore positions r+3 and m-r belong to one common block B, the canonical giant block.

Write the position interval of B as [p,q]. Put
ell=r+4-p,
rho=q-(m-r)+1.
Thus ell is the number of B-positions lying in P and rho the number lying in Q. Both are positive, and the corresponding position bands in B are disjoint.

Let A_r be the family of supports inside B used by the prefix window P among orders with first switch r. Every member of A_r has size ell. Let C_r be the family of supports inside B used by the suffix window Q among orders with reflected last switch r. Every member of C_r has size rho.

**Uniform cross-intersection lemma.**
Every A in A_r meets every C in C_r.

**Proof.**
All blocks strictly before B lie entirely in P and all blocks strictly after B lie entirely in Q, so their vertex sets are disjoint and fixed. Suppose A and C were disjoint. Take witnesses for A and C. Inside B, prescribe the left witness on the ell positions B intersect P and the right witness on the rho positions B intersect Q. These position bands are disjoint, and A,C are disjoint, so the prescriptions are compatible. Fill the remaining positions of B arbitrarily and use arbitrary compatible orders in the other blocks. The resulting face vertex agrees with the first witness throughout P and with the second throughout Q. Hence its first switch is r and its reflected last switch is r, giving the forbidden exact diagonal. (square)

Thus the surviving global topology has a precise finite combinatorial core:
[
mathcal A_rsubseteq {Bchoose ell},
qquad
mathcal C_rsubseteq {Bchoose ho},
]
are nonempty uniform cross-intersecting families, with each set carrying an ordered determining segment and an outer-run color.

This is the correct matching-theoretic interface. Version 40's unrestricted formulation should be read only in this separated-window regime; near-central overlap is handled separately and has already been eliminated.

The next target is to exploit the extra structure beyond abstract cross-intersection: these families arise as first- and last-switch determining sets under the full symmetric permutation freedom of B, and the color-sensitive winding prescribes compatible outer colors. A disjoint pair gives an exact diagonal immediately; a genuine extremal cross-intersection must therefore impose a common-core or small-transversal phenomenon that can be converted into vertex transport or endpoint reversal.


### Boundary exchange in the giant block gives a star or a front jump

Retain the minimum winding coordinate r and the canonical block B from version 47. Let pi be an order in the root-balanced face with first switch r, and let A in A_r be the B-part of its determining prefix [1,r+3].

Let z be the vertex of B occupying position r+3 in pi. Put
K=A-{z}.
Because the first-switch condition is determined by positions at most r+3, the vertices of B strictly after position r+3 may be permuted arbitrarily without changing a(pi)=r.

Fix any
w in B-A.
First permute only positions after r+3 so that w occupies position r+4; this preserves first switch r. Then swap positions r+3 and r+4. Call the resulting order pi_w.

All triple-status positions strictly before r are unchanged, so
a(pi_w)>=r.
Exactly one of the following occurs.

1. **successful boundary exchange:** a(pi_w)=r. Then the new B-support in the determining prefix is
K union {w}.
Thus K union {w} belongs to A_r.

2. **front displacement:** a(pi_w)>r. The adjacent swap affects switch indicators only in
[r,r+4].
Hence either the new first switch lies in {r+1,...,r+4}, a bounded local-front event, or the whole interval of switch positions from r through r+4 becomes switch-free and the next first switch is an unchanged old switch farther to the right. In the latter case pi_w has the jump-corridor monochromatic run supplied by version 37.

This gives a useful extremal consequence. Suppose every choice
w in B-A
is a successful boundary exchange. Then
K union {u} in A_r
for every u in B-K
(including u=z from the original witness).

Since A_r and C_r are cross-intersecting, every
C in C_r
meets every set K union {u}. Therefore either
C meets K,
or C contains all of B-K.
Consequently, if
rho < |B|-|K| = |B|-ell+1,
then K is a transversal of C_r:
K meets every member of C_r.

Thus the giant-block branch has the following exchange dichotomy.

- A failed one-step replacement produces a bounded local-front event or a long monochromatic jump corridor.
- If every one-step replacement succeeds, one side of the cross-intersection contains a full one-vertex star, and the opposite family has a fixed transversal of size at most ell-1 unless its members occupy essentially all of B.

The symmetric statement holds at the right determining boundary, exchanging the vertex at position m-r with the preceding B-position. This is the first direct conversion of the topological cross-intersection residue into a matching-style small-transversal obstruction.


### Exact diagonal remains a separate branch

The topology reduction must retain the exact-diagonal alternative explicitly. Version 35 produces a root-balanced face only after excluding a spanning order with
\[
q(\pi)=(r,r),
\qquad
a(\pi)=r,\quad b(\pi)=m-r.
\]
Hence the unconditional topological frontier is:

1. an exact-diagonal spanning order; or
2. the canonical giant-block directed-cycle regime of versions 46--48.

The exact-diagonal branch has its own central freedom. Put
\[
d=b-a=m-2r.
\]
Fix the determining prefix through position \(r+3\) and the determining suffix from position \(b\) onward. Then every permutation of the vertices in the intermediate position interval
\[
r+4,\ldots,b-1
\]
preserves \(q=(r,r)\). Thus, when \(d\ge5\), the diagonal branch also contains a freely permutable central block of order \(d-4\).

There is a general compact-switch observation which removes the smallest diagonal gaps.

**Lemma.** If a spanning order has first and last switch positions \(a<b\) with
\[
b-a\le2,
\]
then \(H\) has a spanning two-cover.

**Proof.** Cut the vertex order between positions \(a+2\) and \(a+3\). The first block has internal status positions at most \(a\), hence all one color because \(a\) is the first switch. The second block has internal status positions at least \(a+3>b\), hence all one color because \(b\) is the last switch. Reverse either block if its common color is non-tight. Both resulting blocks are tight paths. \(\square\)

Consequently an exact diagonal can survive in a counterexample only when
\[
m-2r\ge3.
\]
For gap at least five it has a nonempty free central permutation block; gaps three and four are the remaining compact diagonal interface.

### Full boundary exchange gives an unconditional transversal

Retain the notation of version 48. The canonical block \(B\) contains \(\ell\) left-determining positions and \(\rho\) right-determining positions. Since the minimum mirror corridor is nonempty,
\[
2r\le m-4.
\]
A direct position count gives
\[
\ell+\rho
=
|B|+2r+4-m
\le |B|.
\]

Let \(A\in\mathcal A_r\), let \(z\) be its boundary vertex at position \(r+3\), and put
\[
K=A-\{z\}.
\]
Suppose every replacement of \(z\) by a vertex \(w\in B-A\) preserves first switch \(r\). Version 48 then gives
\[
K\cup\{u\}\in\mathcal A_r
\]
for every \(u\in B-K\).

For \(C\in\mathcal C_r\), cross-intersection with every \(K\cup\{u\}\) implies either \(C\cap K\ne\varnothing\), or \(C\) contains all of \(B-K\). The latter would require
\[
\rho\ge |B|-|K|=|B|-\ell+1.
\]
But \(\ell+\rho\le |B|\) gives
\[
\rho\le |B|-\ell<|B|-\ell+1.
\]
Therefore the second alternative is impossible.

Hence:

> If all left boundary exchanges succeed, \(K\) is a fixed \((\ell-1)\)-vertex transversal of the entire right family \(\mathcal C_r\).

The symmetric assertion holds with left and right interchanged.

Choose now an inclusion-minimal transversal
\[
T\subseteq K
\]
of \(\mathcal C_r\). For every \(x\in T\), minimality supplies a private witness
\[
C_x\in\mathcal C_r
\]
such that
\[
C_x\cap T=\{x\}.
\]
Thus the no-front-jump branch manufactures a family of right switch witnesses which transport individual vertices of one fixed left core to the far determining suffix while avoiding all the other transversal vertices.

This gives the sharpened giant-block trichotomy:

1. a left or right boundary exchange fails, producing a bounded local-front event or a long jump corridor;
2. all exchanges succeed on one side, producing a fixed small transversal and private opposite-side transport witnesses;
3. the symmetric structure occurs on both sides.

The next target is to combine two private witnesses with path-intersection / endpoint-reversal calculus, rather than treating the cross-intersecting families as arbitrary set systems.


### Giant-block cross-intersection forces a front-displacing adjacent swap

The matching/transversal structure can be simplified further.

Retain the canonical giant-block branch at the minimum cycle coordinate \(r\). Let
\[
b=m-r.
\]
Fix one order \(\sigma\) in the face with last switch \(b\), equivalently reflected last coordinate \(r\). Fix also one left determining support
\[
A\in\mathcal A_r
\]
of size \(\ell\) inside the canonical block \(B\). Let the right determining band inside \(B\) have size \(\rho\). As in version 49,
\[
\ell+\rho\le |B|.
\]

Freeze the internal orders of every face block other than \(B\), and consider the full adjacent-transposition graph of permutations of \(B\). This graph is connected.

Suppose, for contradiction, that every adjacent transposition inside \(B\), whenever applied to an order whose last switch is \(b\), preserves last switch \(b\). Starting from \(\sigma\), connectedness then implies that **every** permutation of \(B\), with the other blocks frozen as in \(\sigma\), has last switch \(b\).

Since
\[
\ell+\rho\le |B|,
\]
choose disjoint subsets
\[
A,\ C\subseteq B,
\qquad |A|=\ell,\quad |C|=\rho.
\]
Choose a permutation of \(B\) putting exactly \(C\) in the right determining band. By the preceding closure assumption, the resulting order still has reflected last coordinate \(r\).

Now independently replace the orders in all face blocks lying strictly before the right determining window by their orders from a witness for \(A\in\mathcal A_r\). This does not affect the last-switch condition, which is determined by the suffix beginning at position \(b\). Inside \(B\), choose the permutation so that the left determining band uses exactly \(A\) and the right determining band exactly \(C\); the bands are disjoint and so are \(A,C\). The resulting face vertex has
\[
a=r,\qquad m-b=r,
\]
an exact diagonal, contradiction.

Therefore:

> In the no-diagonal canonical giant-block branch, there exists an order \(\tau\) with last switch \(b=m-r\) and an adjacent transposition of two positions inside \(B\) after which the last switch is no longer \(b\).

The symmetric statement holds for the first switch.

This converts the whole giant-block cross-intersection problem into local front motion. If the transposition occurs well to the left of \(b\), it cannot affect any status at or after \(b\), so the last switch remains \(b\). Hence every front-displacing swap lies in or to the right of the bounded neighborhood of \(b\).

If it lies in the bounded neighborhood of \(b\), one obtains a bounded local-front event. If it lies farther to the right, the old order has no switches between \(b\) and the local swap window, because \(b\) was its last switch; the new order differs only in that local window. Thus one obtains a long monochromatic jump corridor between the old front and the new local disturbance.

Consequently the canonical giant-block topology has the unconditional reduction
\[
\boxed{
\text{exact diagonal}
\quad\text{or}\quad
\text{bounded local front displacement}
\quad\text{or}\quad
\text{long monochromatic jump corridor}.
}
\]

This bypasses the need to classify extremal cross-intersecting families. The transversal/private-witness machinery of versions 48--49 remains valid, but it is no longer necessary merely to escape the giant-block topology.


### Deterministic front pushing collapses the giant block to width three

Let pi=(v_1,...,v_n) be a spanning order in the surviving canonical giant-block branch. Let a be its first switch and b its last switch. Assume b-a>=4 and that positions a+3 and a+4 lie in the canonical permutation block B. Swap the vertices in positions a+3 and a+4, producing pi_prime.

Write A for the first-run color. The old boundary vertex z=v_(a+3) satisfies that the triple at status position a+1 has color 1-A. If after the swap the first switch remains a, then the replacement vertex w=v_(a+4) gives the same color 1-A at that same triple position. After orienting the monochromatic outer prefix as a tight path, both z and w are exterior reversers of the same exposed end edge. Hence the existing two-reverser lemma gives a Hamiltonian four-support.

Otherwise the first switch moves strictly right. No switch before a can be created by this swap, and when b>a+4 the last switch is untouched. Therefore the switch span b-a strictly decreases.

Starting from a cycle witness with first switch at the minimum winding coordinate r, the canonical block contains every position from r+3 through m-r. As long as b-a>=5, we have a>=r and a+4<=b-1<=m-r-1, so the required adjacent swap is always available inside B. Thus repeated failed exchanges strictly decrease b-a until either a Hamiltonian four-support appears or b-a<=4.

If b-a=4, the same swap still cannot move the last switch to the right: all switch indicators beyond a+4 are unchanged and were zero. Hence a failed exchange again decreases the span. Therefore the only compact residue has

b-a<=3.

If b-a<=2, cutting between the two middle vertices discards the two straddling status positions; the two remaining outer status blocks are monochromatic and can be oriented independently as tight paths. Hence H has a spanning two-cover.

Therefore the only unresolved front-motion residue is

b-a=3.

In this case a failed left boundary exchange either reduces the span to at most two, giving a two-cover, or produces a new order with first switch a+1 and last switch a+4. Thus the width-three switch window translates rigidly one position to the right. Repeating, either a second reverser appears, the span drops to the solved range, or the width-three window walks to the far end of the canonical block.

So the arbitrary-order giant-block obstruction has been reduced to one exact local dynamical pattern: a three-wide switch window translating through B under adjacent swaps.


### Universal front pushing and the width-three carrier
The adjacent swap at positions a+3,a+4 does not need to remain inside the topology face. For any spanning order with first switch a and last switch b, if b-a>=4 then either the first switch stays a, in which case the old and new boundary vertices are two exterior reversers of the same exposed end edge and give the known Hamiltonian four-support, or the first switch moves right. If b>a+4 the last switch is unchanged, so the span strictly decreases; if b=a+4 it cannot move right, so the span still decreases. Hence every spanning order reduces to a two-cover, a four-support, or switch span three.

In span three, regard the boundary vertex z as a carrier and delete it. All successive translations of the three-wide window induce the same order D of H-z. If z is at position j, D is monochromatic in the first-run color through status j-3 and in the last-run color from status j onward. Each surviving translation forces one more intervening status of D to equal the first-run color. Two translations make D monochromatic when the outer colors agree; three translations are impossible when they disagree. Thus a width-three walker cannot persist for more than two steps in either direction without producing a two-cover or the two-reverser four-support.


### Correction: two reversers of the same edge do not force a four-support

Versions 51--52 used the claim that if two exterior vertices z,w both reverse the same displayed edge xy, then {x,y,z,w} contains a Hamiltonian four-set. That claim is false.

The valid earlier lemma is different: one exterior vertex z reversing two distinct terminal edges gives a four-support because the two possible cross triples are genuine boundary flips of one another. With two different exterior vertices reversing one common edge, boundary antisymmetry gives no corresponding relation between z and w.

Concretely, from
(z,y,x) tight
and
(w,y,x) tight
there is no forced status among the additional triples needed to concatenate z and w into a four-path. An explicit four-vertex boundary tournament can satisfy both displayed triples while having no Hamilton path, so the implication fails even at order four.

Therefore the conclusions in versions 51--52 that a successful adjacent swap automatically yields a Hamiltonian four-support are withdrawn. In particular, the claimed universal reduction of every spanning order to switch span three is not established.

What remains valid from those versions is the local front-motion calculation:
- swapping positions a+3,a+4 affects only a bounded window of statuses/switches;
- if the first switch moves right while the last switch is outside that window, the switch span decreases;
- if it jumps past the local window, a long monochromatic corridor is created;
- if the first switch stays fixed, the old and replacement vertices have the same reversal/extension relation to the exposed ordered edge.

Thus a successful swap produces a **same-edge twin pair**, not a four-support. The corrected target is to understand how a large family of such same-edge twins interacts with the local tournament structure or with a second exposed edge; only a vertex that acquires reversal data at two distinct terminal edges triggers the valid common-exterior-reverser four-support lemma.


### Same-end common reversers: initial-initial is as good as terminal-terminal

The valid common-exterior-reverser lemma has a symmetric initial-edge form which is important for the color-sensitive topology.

Let A=(a_1,...,a_s) and P=(p_1,...,p_t) be vertex-disjoint tight paths, s,t>=2, and let w lie outside both.

If w reverses both terminal edges,
(w,a_s,a_{s-1}) and (w,p_t,p_{t-1})
tight,
the previously recorded lemma gives a Hamiltonian four-set.

The same conclusion holds if w reverses both initial edges:
(a_2,a_1,w) and (p_2,p_1,w)
tight.
Indeed exactly one of
(a_1,w,p_1), (p_1,w,a_1)
is tight. In the first case
(a_2,a_1,w,p_1)
is a tight four-path; in the second
(p_2,p_1,w,a_1)
is a tight four-path.

Thus a common reverser of two **same-type ends** (terminal-terminal or initial-initial) gives a Hamiltonian four-support. The mixed initial-terminal case is not asserted.

Now return to the coherent color-compatible winding at the minimum coordinate r. Let A in A_r be a left witness and C in C_r a right witness. Since A,C cross-intersect and |A|+|C|<=|B|, we have
|A union C|<=|B|-1.
Choose
w in B-(A union C).

Perform the left boundary exchange with w and the symmetric right boundary exchange with the same w.

If the left front moves, we obtain the bounded local-front/jump-corridor branch. If the right front moves, likewise.

Suppose both fronts remain fixed. Let alpha be the first outer color of the left witness and omega the last outer color of the right witness. Color-sensitive coherent winding gives
alpha != omega.

If alpha=1 and omega=0, after orienting the two monochromatic outer blocks as tight paths, w reverses their two terminal boundary edges.

If alpha=0 and omega=1, the tight orientations of both outer blocks are reversed relative to the displayed order, and w reverses their two initial boundary edges.

Hence in either color case the same-end common-reverser lemma gives a Hamiltonian four-support.

Therefore every pair of left/right witnesses at the minimum winding coordinate admits a vertex w producing the sharp trichotomy
[
oxed{
	ext{left front displacement}
quad	ext{or}quad
	ext{right front displacement}
quad	ext{or}quad
	ext{Hamiltonian four-support}.
}
]

This is the correct salvage of the front-pushing idea. The error in v51-v52 was using two vertices at one edge; topology supplies one vertex at two mirror edges, and the color alternation guarantees that the two reversals have the same endpoint type.



### Distance-two front swap: a deep boundary candidate acquires a second disjoint reversal

The corrected target from version 53 can be solved directly whenever the monochromatic run after the first switch has length at least three.

Let
\[
\pi=(v_1,\ldots,v_n)
\]
have first switch at \(a\). Reverse the whole order if necessary so that the first run is tight. Put
\[
x=v_{a+1},\quad y=v_{a+2},\quad z=v_{a+3},\quad
w=v_{a+4},\quad u=v_{a+5}.
\]
Then the triple at status \(a\) is tight and the triple
\[
(x,y,z)
\]
at status \(a+1\) is non-tight.

Assume the second run persists through status \(a+3\). In particular
\[
(z,w,u)
\]
is non-tight, so boundary reversal gives
\[
(u,w,z)
\]
tight. Thus \(u\) reverses the terminal edge \(zw\) of the two-vertex tight path \((z,w)\).

Now swap the vertices in positions \(a+3\) and \(a+5\), producing
\[
\pi'=(\ldots,x,y,u,w,z,\ldots).
\]
No status before \(a\) changes, and status \(a\) remains tight.

If the first switch of \(\pi'\) is still \(a\), then
\[
(x,y,u)
\]
is non-tight. Boundary reversal gives
\[
(u,y,x)
\]
tight. Hence the same vertex \(u\) reverses the terminal edges of the two vertex-disjoint tight paths
\[
(x,y)\qquad\text{and}\qquad(z,w).
\]
By the valid common-exterior-reverser lemma, these two terminal-edge reversals force a Hamiltonian four-support.

Otherwise the first switch moves strictly to the right. If the last switch lies beyond the bounded window affected by the transposition, the switch span strictly decreases. If the last switch lies inside that window, the whole switch pattern is already bounded.

Therefore a first-switch boundary followed by at least three statuses of the opposite color gives the trichotomy
\[
\boxed{
\text{front motion}
\quad\text{or}\quad
\text{bounded switch window}
\quad\text{or}\quad
\text{valid Hamiltonian four-support}.
}
\]

The key point is that the deep candidate \(u\) does not merely become a same-edge twin. Its original location in the opposite-color run already makes it a reverser of the disjoint edge \(zw\). If the boundary exchange also leaves the first switch fixed, \(u\) acquires the second reversal on \(xy\), exactly repairing the defect identified in version 53.


### The cyclic two-component strengthening is false in arbitrarily large orders

The self-contained Section [[balanced_cuts_obstruct_the_two_component_spanning_cycle_target]] constructs, for every s>=1, an edge-orderable boundary tournament on 4s vertices with path-cover number exactly two and a spanning one-change linear order, while the minimum number of monochromatic components of a spanning cycle is exactly four.

The construction uses four equal classes A,B,C,D. Order ordinary edges in levels: within classes; AB or CD; AC or BD; AD or BC. A cyclic edge sequence with only two color components has every upper rank set consecutive. The balanced cut AB|CD then forces every cycle edge into the top two levels, and the balanced cut AC|BD forces every cycle edge into the top level. That level is the disconnected union of the AD and BC complete bipartite graphs, a contradiction. Tie orders make alternating paths on A union D and B union C increasing; additional independent tie choices yield a spanning one-change linear order.

Thus the universal cyclic two-component target proposed in version 16 is refuted, and its asserted equivalence with the linear one-change target is withdrawn. The valid implication from a two-component cycle to a two-cover remains. The one-change linear target, the general two-cover conjecture, and the corrected linear switch arguments remain separate open questions.

For a cyclic formulation equivalent to the grand conjecture, let the cycle edges be vertices of a graph and join the two edges incident with each blue transition. A spanning two-cover exists exactly when some oriented cyclic order has a vertex cover of size at most two in this graph. This retains the freedom to cut at two positions even when the blue transitions form separated components. The complete proof is in the cited Section.


### Color-correct repair of the distance-two front swap

Version 55's distance-two swap used the phrase "reverse the whole order if necessary so that the first run is tight." That normalization is not legitimate: reversing the whole order replaces the first run by the complemented old last run, not by a recoloring of the same first run.

The local lemma nevertheless survives with a direct two-color proof.

Let the first run have color A in {0,1}, with 1=tight, and suppose the second run of color 1-A persists through statuses a+1,a+2,a+3. Write
x=v_{a+1}, y=v_{a+2}, z=v_{a+3}, w=v_{a+4}, u=v_{a+5}.
Swap z and u. If the first switch remains a, then both
(x,y,u)
and
(z,w,u)
have color 1-A.

If A=1, these two triples are non-tight, so boundary reversal gives
(u,y,x), (u,w,z)
tight. Thus u reverses the terminal edges of the tight two-paths (x,y) and (z,w), and the terminal-terminal common-reverser lemma gives a Hamiltonian four-support.

If A=0, the two displayed triples are already tight. Orient the vacuous tight two-paths as
(y,x) and (w,z).
Then
(x,y,u)
and
(z,w,u)
are precisely reversals of their two initial edges. The initial-initial common-reverser lemma from version 54 again gives a Hamiltonian four-support.

Therefore the distance-two trichotomy is color-symmetric and valid without reversing the spanning order:
[
oxed{
	ext{first-front displacement}
quad	ext{or}quad
	ext{bounded affected switch window}
quad	ext{or}quad
	ext{Hamiltonian four-support}.
}
]

The swap of positions a+3 and a+5 affects only triple starts a+1 through a+5, hence only a bounded switch neighborhood. If the old last switch lies beyond that neighborhood and the first front moves right, the switch span strictly decreases.

### Quantitative abundance of mirror carriers

In the coherent giant-block branch, for fixed left/right witnesses A,C at the minimum coordinate r, the carrier set
U=B-(A union C)
has size
[
|U|=m-2r-4+|Acap C|ge m-2r-3.
]
For each w in U, version 54 gives left front motion, right front motion, or a valid four-support.

Among any subset U_0 of carriers producing four-supports, the same-end common-reverser construction has only two possible cross orientations. Hence at least ceil(|U_0|/2) resulting Hamiltonian four-supports share one fixed three-vertex core and vary only in w.

Thus a large mirror gap forces either many front-moving carriers or many overlapping Hamiltonian four-supports with a common 3-core. In a minimum counterexample every such proper support has a two-coverable complement, producing many rooted 4|P|Q states. The remaining bridge is to link enough of those states in one repartition component, or use the abundance of front movers to compress the switch geometry.



### Three consecutive same-edge twins force a genuine second-edge reversal

The same-edge twin obstruction from version 53 cannot persist through three consecutive vertices of one monochromatic corridor.

Let the first-run color be \(A\in\{0,1\}\), and let \(x,y\) be the exposed ordered edge at the first front. Let
\[
z_0,z_1,z_2
\]
be three consecutive vertices in the following run, whose color is \(1-A\). Suppose all three are same-edge twins at the front, meaning that
\[
(x,y,z_i)
\]
has color \(1-A\) for \(i=0,1,2\).

Because \(z_0,z_1,z_2\) lie consecutively in that same run,
\[
(z_0,z_1,z_2)
\]
also has color \(1-A\).

If \(A=1\), all four displayed triples have color \(0\). Boundary reversal gives
\[
(z_i,y,x)\quad(i=0,1,2)
\]
tight and
\[
(z_2,z_1,z_0)
\]
tight. Thus \(z_2\) reverses the terminal edges of the two vertex-disjoint tight 2-paths
\[
(x,y),\qquad(z_0,z_1).
\]
The valid terminal-terminal common-reverser lemma gives a Hamiltonian four-support.

If \(A=0\), the displayed triples are themselves tight. Orient the two 2-paths as
\[
(y,x),\qquad(z_1,z_0).
\]
Then
\[
(x,y,z_2),\qquad(z_0,z_1,z_2)
\]
say exactly that \(z_2\) reverses both initial edges. The valid initial-initial common-reverser lemma again gives a Hamiltonian four-support.

Hence:

**Three-twin lemma.**
Three consecutive vertices of one opposite-color run cannot all be same-edge twins for a fixed exposed edge without producing a valid Hamiltonian four-support.

Therefore any front-pushing process in which the first front remains fixed can accumulate at most two consecutive same-edge twins inside one monochromatic corridor before one of three things happens:
- the front moves;
- the corridor color changes;
- a genuine common reverser of two disjoint same-type edges appears.


### Wide exact diagonals collapse to front motion or bounded Hamiltonian support

Return to the exact-diagonal branch
q(pi)=(r,r), with first switch a=r and last switch b=m-r, and put d=b-a=m-2r.

The cases d<=2 already give a two-cover. Assume d>=5, so positions r+4,...,b-1 contain d-4 freely permutable central vertices while preserving the two extreme switch coordinates.

Fix one central carrier w. Test it separately against the left and right boundary exchanges: place w at position r+4 and swap with r+3; place w at b-1 and swap with b.

If either exchange moves its extreme front, then for d>=5 the opposite extreme lies outside the local affected window, so the switch span strictly decreases.

Suppose both fronts remain fixed. Let alpha and omega be the first and last outer colors.

If alpha!=omega, version 54 applies: w is a same-end common reverser of the two tight-oriented outer blocks, and a Hamiltonian four-support follows.

Suppose alpha=omega. Then w is a mixed-end reverser. Up to the symmetric case, write the tight-oriented outer boundary edges as
...a_0,a_1
and
p_1,p_2,...
with
(w,a_1,a_0) and (p_2,p_1,w)
tight.

Exactly one of
(p_1,w,a_1), (a_1,w,p_1)
is tight.

If (p_1,w,a_1) is tight, then
(p_2,p_1,w,a_1,a_0)
is a tight Hamiltonian five-path.

Otherwise
(a_1,w,p_1)
is tight, so w is a parallel middle vertex between the fixed pair a_1,p_1.

Hence if two distinct central carriers w,w' both preserve both fronts and both fall into this second mixed-end orientation, then
(a_1,w,p_1), (a_1,w',p_1)
are tight. The toolkit lemma "Two parallel middle vertices force a Hamilton four-path" gives a Hamiltonian four-support on {a_1,p_1,w,w'}.

Therefore for d>=6, where at least two central carriers exist, the exact-diagonal branch satisfies
[
oxed{
	ext{strict switch-span decrease}
quad	ext{or}quad
	ext{Hamiltonian four-support}
quad	ext{or}quad
	ext{Hamiltonian five-support}.
}
]

For d=5 there is one central carrier; after excluding front motion and the immediate same-end/favorable mixed-end support outcomes, only one bounded mixed-end parallel-middle residue remains.

Thus wide exact diagonals are not a genuinely global topology obstruction. Repeated front motion reduces the diagonal gap, while failure of motion produces bounded Hamiltonian support. The unresolved exact-diagonal interface is confined to gap at most five.


### Compact exact diagonals are already small-component three-covers

Retain an exact-diagonal spanning order
\[
\pi=(v_1,\ldots,v_n),
\qquad
a=r,\quad b=m-r,
\]
and put
\[
d=b-a.
\]

The cases \(d\le2\) already give a spanning two-cover. Now suppose
\[
d\in\{3,4,5\}.
\]

Let
\[
L=(v_1,\ldots,v_{a+2}),
\qquad
R=(v_{b+1},\ldots,v_n),
\]
and let
\[
M=\{v_{a+3},\ldots,v_b\}.
\]
Then
\[
|M|=b-(a+3)+1=d-2\in\{1,2,3\}.
\]

Every internal status of \(L\) lies at a position at most \(a\), hence has the first outer color. Therefore one of the two orientations of \(L\) is a tight path. Every internal status of \(R\) lies at a position at least \(b+1\), hence has the last outer color, so one orientation of \(R\) is also a tight path.

The middle set \(M\) is Hamiltonian automatically:
- for \(|M|=1\) or \(2\), every ordering is a tight path vacuously;
- for \(|M|=3\), boundary antisymmetry guarantees that one of the two reverse orders is tight.

Hence every exact diagonal with gap \(3,4,\) or \(5\) gives a spanning three-cover
\[
L\mid M\mid R
\]
whose middle component has order \(1,2,\) or \(3\), respectively.

Thus in the minimum-counterexample architecture:
- gap \(3\) is exactly a singleton-lift/deletion-cover state;
- gap \(4\) is exactly a two-vertex middle-path state, so the existing endpoint-reversal pattern applies;
- gap \(5\) is a rooted three-support state, so the small-support quadratic-descent machinery applies.

Combined with version 59, the exact-diagonal branch is therefore completely absorbed into existing mainline interfaces: large gap gives strict front motion or a bounded Hamiltonian support, while gaps at most five give either a two-cover or a spanning three-cover with middle component of order at most three.

### One carrier-produced four-support already reaches Article III

The quantitative abundance statement of version 57 can also be simplified in the minimum-counterexample setting.

Suppose one mirror carrier produces a Hamiltonian four-support \(X\). Then
\[
H-X
\]
is non-Hamiltonian with path-cover number two; choose a displayed two-cover
\[
H-X=P\mid Q.
\]
Thus
\[
X\mid P\mid Q
\]
is a spanning three-cover with a displayed four-component.

The established rooted-four-support theorem in line_rooted_small_support_descent_from_deletion_cover_lifts already shows that such a state reaches the defect-compression interface immediately: either
- an endpoint of one complementary path reverses an end edge of the displayed four-path;
- \(H\) has a two-cover; or
- for each prescribed endpoint of a complementary path there is a Hamiltonian five-support containing that endpoint whose complement again has path-cover number two.

Therefore no linkage among many carrier-produced four-supports is needed merely to reconnect the topology route to the main line. A single four-support suffices.

Accordingly, in a minimum counterexample the only genuinely new carrier regime left by version 57 is:

> every available mirror carrier moves at least one front.

The same-core abundance of four-supports remains useful additional structure, but it is not itself a new bottleneck.


### Correction: mirror exposed edges need not be disjoint

Version 54, and the quantitative support conclusion in version 57 that depends on it, used the same-end common-reverser lemma on the exposed left and right boundary edges of two different witness orders. That lemma requires the two tight 2-paths to be vertex-disjoint.

The determining position windows are disjoint at the minimum giant-block coordinate, but the **vertex supports of two different face orders need not be disjoint**. Indeed the left and right determining support families are cross-intersecting. Therefore their exposed 2-edges can share one or even two physical vertices.

Hence the valid mirror-carrier conclusion is the following corrected trichotomy/quadrichotomy.

Let \(L\) be a left witness and \(R\) a right witness with complementary outer colors, and let \(w\) lie outside both determining supports. Perform the left and right boundary exchanges with \(w\).

- If the left front moves, record left front displacement.
- If the right front moves, record right front displacement.
- Suppose both fronts stay fixed. Then \(w\) reverses the two exposed tight-oriented boundary edges in the same endpoint sense: terminal-terminal or initial-initial.
  - If those two exposed edges are vertex-disjoint, the valid common-reverser lemma gives a Hamiltonian four-support.
  - If they intersect, one obtains an **exposed-edge collision** rather than an automatic four-support.

Thus
\[
\boxed{
\text{left motion}
\ \vee\
\text{right motion}
\ \vee\
\text{Hamiltonian four-support}
\ \vee\
\text{exposed-edge collision}.
}
\]

The support-abundance count of version 57 is valid only for carriers attached to witness pairs whose exposed boundary edges are disjoint. The distance-two swap, the three-twin lemma, and the exact-diagonal argument of versions 56--60 are unaffected, because there the two 2-edges occur in one displayed order and are visibly disjoint.

### Collision winding on physical vertices

The exposed-edge collision branch has a useful cyclic form along the color-compatible directed switch-front cycle.

Write the coherent winding orders cyclically as
\[
q(\pi_i)=(x_i,x_{i+1}).
\]
Let \(R_i\) be the exposed 2-edge of the tight-oriented last outer run of \(\pi_i\), and let \(L_i\) be the exposed 2-edge of the tight-oriented first outer run of \(\pi_i\).

For each \(i\), \(L_i\) and \(R_i\) are disjoint, because they occupy disjoint position windows in the same spanning order in the surviving noncentral branch.

At the shared switch coordinate \(x_{i+1}\), color alternation pairs \(R_i\) with \(L_{i+1}\). If a mirror carrier fixes both fronts and does not produce a four-support, then necessarily
\[
R_i\cap L_{i+1}\ne\varnothing.
\]

Therefore, if every coherent-winding link falls into the collision branch, choose
\[
c_i\in R_i\cap L_{i+1}.
\]
Because
\[
L_{i+1}\cap R_{i+1}=\varnothing,
\]
we automatically have
\[
c_i\ne c_{i+1}.
\]

So a complete failure of the disjoint-edge support mechanism converts the topological switch-front cycle into a cyclic sequence of **physical collision vertices**
\[
c_1,c_2,\ldots,c_t
\]
with consecutive labels distinct, where \(c_i\) lies simultaneously on the right exposed edge of \(\pi_i\) and the left exposed edge of \(\pi_{i+1}\).

This is the correct residual object for the mirror-carrier branch. The next task is to translate the same-end reversal triples through these shared endpoints; one should not use the common-reverser four-support lemma until disjointness has been established.



### A collision link has at most one stationary carrier outside bounded support

Retain one exposed-edge collision link from version 61. Let the two exposed 2-edges intersect, and let \(D\) be their three-vertex union.

Suppose two distinct mirror carriers \(w,w'\) both preserve the two fronts at this same link. The precise reversal orientation is irrelevant for the following reduction.

Every three-vertex boundary tournament is Hamiltonian, so choose a tight order \(T\) on \(D\).

If either \(D\cup\{w\}\) or \(D\cup\{w'\}\) is Hamiltonian, then a Hamiltonian four-support is already present.

Assume both four-sets are non-Hamiltonian. The bad-four-extension lemma in localextend01 applies to the tight three-path \(T\) and the two exterior vertices \(w,w'\): two non-Hamiltonian one-vertex extensions of the same tight three-path force
\[
D\cup\{w,w'\}
\]
to be Hamiltonian, with a Hamilton five-path whose endpoints lie in \(D\).

Hence a Hamiltonian five-support is present.

Therefore, in a minimum counterexample outside the already-developed bounded-support branch,
\[
\boxed{\text{each exposed-edge collision link has at most one stationary mirror carrier}.}
\]

All other available carriers at that link must move at least one front.

This sharpens the collision winding of version 61 from an arbitrary collision family to a uniquely carried one: every link can retain at most one carrier without immediately falling back into the four-/five-support mainline.



### A stationary carrier repeated across two consecutive collision links

Let \(w\) be the unique stationary carrier on collision link \(i\) and also on collision link \(i+1\). Then in the intermediate order \(\pi_{i+1}\), the same vertex \(w\) reverses the exposed left edge \(L_{i+1}\) and exposed right edge \(R_{i+1}\). These two edges are vertex-disjoint because they occur in disjoint outer position windows of the same spanning order.

Let \(\alpha\) and \(\omega\) be the first and last colors of \(\pi_{i+1}\).

If \(\alpha\ne\omega\), after orienting the two outer monochromatic blocks as tight paths, the two reversals have the same endpoint type: terminal-terminal when \((\alpha,\omega)=(1,0)\), and initial-initial when \((\alpha,\omega)=(0,1)\). The valid same-end common-reverser lemma therefore gives a Hamiltonian four-support.

If \(\alpha=\omega\), the reversals have mixed endpoint type. This is exactly the mixed-end configuration from the exact-diagonal carrier analysis. Writing the tight-oriented boundary edges as
\[
\ldots,a_0,a_1
\qquad\text{and}\qquad
p_1,p_2,\ldots
\]
one has, up to symmetry,
\[
(w,a_1,a_0),\qquad(p_2,p_1,w)
\]
tight. Exactly one of
\[
(p_1,w,a_1),\qquad(a_1,w,p_1)
\]
is tight. In the first case
\[
(p_2,p_1,w,a_1,a_0)
\]
is a Hamiltonian five-path. In the second case \(w\) is a parallel-middle vertex between \(a_1\) and \(p_1\).

Hence a stationary carrier can repeat on consecutive collision links only by immediately producing a Hamiltonian four-/five-support, or by entering one precise mixed-end parallel-middle residue in the intermediate order.



### Permutahedral geodesic dictionary with the cube problem

There is a precise analogy with strengthened forms of Norine's cube conjecture.

Fix antipodal vertices \(x,\bar x\) in \(Q_n\). An antipodal geodesic from \(x\) to \(\bar x\) uses each coordinate exactly once, so it is determined by a permutation of the \(n\) coordinate directions. Thus the space of such geodesics is a permutahedron.

Likewise, a spanning order of an \(n\)-vertex boundary tournament is a permutation of the \(n\) vertices.

In both settings one obtains a binary word from a permutation:
- for a cube geodesic, the edge colors along the path;
- for a boundary tournament order, the tight/non-tight colors of consecutive triples.

The reversal involution has the same form. In an antipodal cube coloring, reversing the coordinate permutation gives the reverse of the antipodal geodesic, hence
\[
c(\sigma^{\rm rev})=\overline{c(\sigma)}^{\rm rev}.
\]
For boundary tournaments,
\[
t(\pi^{\rm rev})=\overline{t(\pi)}^{\rm rev}
\]
by boundary antisymmetry.

Adjacent transpositions are local in both models. In the cube, swapping two consecutive coordinate directions changes only the corresponding two-edge square. In the boundary tournament, swapping adjacent vertices changes only a bounded window of consecutive triple statuses.

This explains why the first/last-switch rook labels and permutahedral topology arise naturally in both problems.

There is also an important difference in target strength. The geodesic one-change problem asks for a permutation whose color word has at most one switch. Our grand two-cover problem is already solved when the first and last switch positions differ by at most two: cutting across that bounded switch window leaves two monochromatic outer blocks, which orient as tight paths. Thus the GN3N target is a width-two front-compression statement rather than an exact one-switch statement.

Strategic consequence: a proof using only the abstract ingredients
\[
\text{permutations}+\text{reversal-complement symmetry}+\text{local adjacent-swap behavior}
\]
would be perilously close to proving the still-open geodesic cube conjecture. The extra leverage available in GN3N is the boundary-tournament structure absent from an arbitrary cube edge-coloring: overlapping triples, local tournaments, common-reverser forcing, parallel-middle lemmas, and Hamiltonian four-/five-support calculus.

Therefore the topology should be used to force a narrow collision/front configuration, and closure should then come from boundary-specific local structure rather than from a purely permutahedral obstruction.


### One-vertex prescribed-switch lift

Adjoin a new vertex infinity and declare (u,v,infinity) tight for every ordered pair of distinct old vertices u,v. Boundary reversal then forces (infinity,v,u) non-tight. Triples with middle vertex infinity are arbitrary.

Then pc(H)<=2 iff the extension has a spanning order P,infinity,Q^rev whose statuses are all tight strictly to the left of infinity and all non-tight strictly to the right. Indeed, if P,Q are a two-cover, the left outer junction through infinity is tight and the right outer junction is non-tight automatically; only the middle triple at infinity is free, so the word has one switch. Conversely such a centered order makes P and Q tight paths in H.

This is the exact dimension-lift analogue of the geodesic Norine formulations: the auxiliary element is the prescribed switch location. It is useful conceptually but also confirms the strategic warning of v64: proving an arbitrary one-switch permutation theorem would amount to attacking the still-open geodesic cube phenomenon. GN3N should exploit the stronger boundary-specific local structure instead.


### Global minimum switch span: one physical carrier reaches both fronts

The geodesic cube analogy suggests avoiding repeated local directions. In the present setting there is a direct extremal implementation that does not require a new topological theorem.

For a spanning order \(\pi\) with at least two switches, let
\[
a(\pi)=\text{first switch},\qquad
b(\pi)=\text{last switch},\qquad
d(\pi)=b(\pi)-a(\pi).
\]
Choose \(\pi=(v_1,\ldots,v_n)\) with \(d(\pi)\) globally minimum among all spanning orders having at least two switches.

If some spanning order has at most one switch, then cutting at that switch and orienting the two monochromatic blocks appropriately already gives a spanning two-cover. Hence in a counterexample the minimum is defined.

Write
\[
a=a(\pi),\qquad b=b(\pi),\qquad d=b-a.
\]

If \(d\le2\), the compact-switch cut gives a two-cover.

If \(3\le d\le5\), put
\[
L=(v_1,\ldots,v_{a+2}),\qquad
R=(v_{b+1},\ldots,v_n),
\]
and
\[
M=\{v_{a+3},\ldots,v_b\}.
\]
Then \(|M|=d-2\le3\). The internal statuses of \(L\) are all the first outer color and those of \(R\) all the last outer color, so each outer block has a tight orientation. The middle set \(M\) is Hamiltonian automatically. Thus
\[
L\mid M\mid R
\]
is a spanning three-cover with a component of order at most three.

Assume now
\[
d\ge6.
\]
Let
\[
W=\{v_{a+4},\ldots,v_{b-1}\},
\qquad |W|=d-4\ge2.
\]

Fix \(w\in W\).

#### Left test

Starting from \(\pi\), permute only the positions
\[
a+4,\ldots,b-1
\]
so that \(w\) occupies position \(a+4\). This does not change the first switch \(a\) or the last switch \(b\): the two extreme switch comparisons lie outside the permuted interval.

Now swap positions \(a+3,a+4\). This local swap cannot create a switch before \(a\), and because \(d\ge6\) it does not affect the last switch \(b\).

If the first switch moved strictly right, the new spanning order would have switch span smaller than \(d\), contradicting global minimality. If the resulting order had at most one switch, it would already give a two-cover. Hence in a counterexample the first switch remains exactly \(a\).

Therefore \(w\) has the fixed-front relation to the exposed left boundary edge. After orienting the first monochromatic outer block as a tight path, \(w\) reverses that exposed tight edge; the endpoint type is determined by the first outer color.

#### Right test

Independently restart from the original order \(\pi\). Permute only positions
\[
a+4,\ldots,b-1
\]
so that the same \(w\) occupies position \(b-1\), and swap positions \(b-1,b\).

Again the first switch \(a\) lies outside the affected window. The last switch cannot move strictly left, because that would decrease \(d\), and an order with at most one switch would already give a two-cover. Hence the last switch remains exactly \(b\).

Thus the same physical vertex \(w\) reverses the exposed tight-oriented right boundary edge as well.

The two exposed edges are physically disjoint: they lie at the two fixed outer boundaries of the same original spanning order and \(d\ge6\).

Let \(\alpha,\omega\) be the first and last outer colors.

- If \(\alpha\ne\omega\), the two reversal certificates have the same endpoint type after orienting the two outer monochromatic blocks as tight paths. The valid same-end common-reverser lemma therefore gives a Hamiltonian four-support.

- If \(\alpha=\omega\), the two certificates have mixed endpoint type. The mixed-end analysis gives, for each \(w\in W\), either a Hamiltonian five-support or a parallel-middle relation through one fixed pair of outer boundary vertices. Since \(|W|\ge2\), if no carrier gives the favorable five-support orientation, two distinct carriers are parallel middles for that same pair, and the parallel-middle lemma gives a Hamiltonian four-support.

Hence:

**Minimum-switch-span theorem.**
Let \(H\) be a boundary \(3\)-tournament with no spanning two-cover. A globally minimum-switch-span spanning order forces one of the following.

1. A spanning three-cover has a component of order at most three.
2. \(H\) contains a Hamiltonian support of order four or five.

In a minimum counterexample, outcome 1 is exactly the existing singleton/two-vertex/three-support descent interface, while outcome 2 has a non-Hamiltonian path-cover-two complement and therefore enters the rooted four-/five-support defect-compression machinery immediately.

This theorem is completely face-independent. It supersedes the need to close the all-movers or physical-collision topology branches merely to reach the established main line.

### Relation to the strengthened Norine geodesic analogy

For an antipodal cube geodesic, using each dimension exactly once is precisely the geodesic condition. In type \(A\), a reduced gallery from a permutation to its reversal crosses every unordered pair of labels exactly once.

The minimum-span carrier proof uses the same principle locally: one physical carrier is transported through the central permutation region and tested at each extreme without sacrificing the extremal front data. No abstract geodesic-Norine theorem is needed, because global switch-span minimality prevents an endpoint test from moving inward.

This suggests a sharper conceptual correspondence:

- cube coordinate used once \(\leftrightarrow\) physical carrier transported without reuse;
- antipodal geodesic \(\leftrightarrow\) reduced permutahedral gallery;
- two color components on the geodesic \(\leftrightarrow\) compressed first/last switch window;
- GN3N-specific closure comes from common-reverser, parallel-middle, and small-support lemmas, which have no analogue in a general antipodal cube coloring.

Thus the strengthened Norine conjecture is an excellent model for the geometry, but the actual proof leverage here comes from the extra boundary-tournament local structure.


### Minimum counterexamples have minimum switch span three

Let H be a minimum counterexample. For every vertex x, the smaller tournament H-x has a two-cover P|Q. Concatenating the displayed tight orders as P,x,Q leaves only the three junction triples as possible non-tight statuses. Hence some spanning order has first-to-last switch span at most three.

A spanning order whose first and last switch positions differ by at most two already gives a two-cover: cut between positions a+2 and a+3; each outer block is monochromatic and can be oriented as a tight path. An order with at most one switch also gives a two-cover. Therefore in a minimum counterexample the global minimum switch span is exactly three.

For every deletion order P,x,Q, the two outer junction triples are non-tight, since otherwise x appends to one of the two displayed paths and gives a two-cover. Thus the local five-bit pattern, including the adjacent inherited tight statuses, is exactly
1-0-0-0-1
or
1-0-1-0-1.

Equivalently,
(x,p_m,p_{m-1})
and
(q_2,q_1,x)
are tight, and only (p_m,x,q_1) is undetermined.

If (p_m,x,q_1) is non-tight, then (q_1,x,p_m) is tight and
(q_2,q_1,x,p_m,p_{m-1})
is a Hamiltonian five-path.

If (p_m,x,q_1) is tight, the junction is the alternating mixed-end/parallel-middle residue.

So the general problem is globally reduced to eliminating these two width-three deletion patterns. The strengthened Norine-geodesic analogy explains the permutation/switch geometry, but minimum-counterexample induction already performs the required global compression.


### Width-three equality makes the alternating junction deterministic

Let H be a minimum counterexample, let H-x=P|Q with P=(p_1,...,p_m), Q=(q_1,...,q_s), m,s>=3, and suppose the deletion junction has the alternating orientation (p_m,x,q_1) tight. Consider the spanning order

sigma=(p_1,...,p_{m-1},q_1,x,p_m,q_2,...,q_s).

All statuses outside the five local splice positions are inherited tight statuses. Write the local five statuses as

A=(p_{m-2},p_{m-1},q_1),
B=(p_{m-1},q_1,x),
C=(q_1,x,p_m),
D=(x,p_m,q_2),
E=(p_m,q_2,q_3).

The middle status C is non-tight by boundary reversal. Since the global minimum switch span in H is exactly three, if A and E are both tight then B and D must both be non-tight: otherwise the entire status word of sigma has first-to-last switch span at most two.

If B and D are both non-tight, boundary reversal gives
(x,q_1,p_{m-1}) and (q_2,p_m,x)
tight. Together with (p_m,x,q_1), these form the Hamiltonian five-path
(q_2,p_m,x,q_1,p_{m-1}).

If A is non-tight, its boundary flip
(q_1,p_{m-1},p_{m-2})
is tight, exporting a reversal one inherited edge outward on the P-side. If E is non-tight, its boundary flip
(q_3,q_2,p_m)
is tight, exporting a reversal one inherited edge outward on the Q-side.

Therefore the alternating width-three junction has the exact deterministic alternative

Hamiltonian five-support
or
external reversal one edge farther outward.

There is no independent local residue. This is the equality-strengthened form of the earlier bad-cross transport lemma.



### The alternating width-three junction forces a positioned four-support trichotomy

Let H be a minimum counterexample, let
\[
H-x=P\mid Q,\qquad
P=(p_1,\ldots,p_m),\qquad
Q=(q_1,\ldots,q_s),
\]
and suppose the deletion junction has the alternating width-three pattern
\[
1-0-1-0-1,
\]
so in particular
\[
(p_m,x,q_1)
\]
is tight, while
\[
(p_{m-1},p_m,x),\qquad (x,q_1,q_2)
\]
are non-tight.

Put
\[
a=p_{m-1},\quad b=p_m,\quad c=q_1,\quad d=q_2.
\]
Then
\[
(b,x,c)
\]
is tight. For the adjacent vertices a,d, boundary antisymmetry gives exactly one of
\[
(b,a,c),\ (c,a,b)
\]
tight, and exactly one of
\[
(b,d,c),\ (c,d,b)
\]
tight.

There are three possibilities.

1. If \((b,a,c)\) is tight, then a and x are two parallel middles from b to c. Hence
   \[
   K_P=\{a,b,c,x\}
   \]
   is Hamiltonian. Repartitioning the rooted three-cover
   \[
   (P-b)\mid(b,x,c)\mid(Q-c)
   \]
   on the union of its first two displayed components gives
   \[
   (P-\{a,b\})\mid K_P\mid(Q-c).
   \]
   The quadratic-potential change is
   \[
   10-2m.
   \]

2. If \((b,d,c)\) is tight, then d and x are two parallel middles from b to c. Hence
   \[
   K_Q=\{b,c,d,x\}
   \]
   is Hamiltonian, and the analogous repartition has potential change
   \[
   10-2s.
   \]

3. If neither of the preceding orientations is tight, then
   \[
   (c,a,b),\qquad(c,d,b)
   \]
   are both tight. Thus a and d are parallel middles from c to b, and
   \[
   K_0=\{a,b,c,d\}
   \]
   is Hamiltonian.

Therefore every alternating width-three deletion junction forces one of:
\[
\boxed{\text{rooted four-support on the P side}}
\]
or
\[
\boxed{\text{rooted four-support on the Q side}}
\]
or
\[
\boxed{\text{the endpoint cross four-set }\{p_{m-1},p_m,q_1,q_2\}\text{ is Hamiltonian}.}
\]

In the first two branches, if the corresponding deletion path has order at least six, the repartition is a strict Phi-descent. At order five it is Phi-neutral.

Hence a Phi-minimal alternating rooted state with both side lengths at least six is forced into the third, cross-four-set branch. More generally, every long side is forced to take the reverse orientation relative to x unless the state admits strict descent.


### Minimum span three propagates an endpoint reversal to the far side

Let H have global minimum switch span three. Let P,A,Q be three displayed tight paths in a spanning three-cover, and suppose z is an endpoint of P with

(z,a_r,a_{r-1})

tight, where A=(a_1,...,a_r). Thus z reverses the terminal edge of A. Consider a spanning order obtained by ending the P-block at z, then traversing A and Q in reverse vertex order. The internal status word on A^rev and Q^rev is entirely non-tight, while the displayed reversal supplies the tight status (z,a_r,a_{r-1}).

If both far A/Q junction triples

(a_2,a_1,q_t),   (a_1,q_t,q_{t-1})

were non-tight, then regardless of the other P/A junction status the complete spanning status word would have at most one switch or would have all of its switches within three consecutive switch positions, hence first-to-last switch span at most two. This contradicts the global minimum span three.

Therefore at least one of the two far triples is tight. The first says that q_t reverses the initial edge of A; the second says that a_1 reverses the terminal edge of Q. If both are tight then

(a_2,a_1,q_t,q_{t-1})

is a Hamiltonian four-path.

Hence, outside the bounded four-support branch, a displayed endpoint reversal propagates deterministically across the reversed path: exactly one far-end reversal survives. The initial-edge version is symmetric.

This is a boundary-specific analogue of geodesic direction transport: one local reversal cannot die in the interior because doing so would compress the status word below the globally minimal width.



### Two elementary middle-2 lifts force descent or an explicit cross four-path

Let \(H\) be a minimum counterexample and let
\[
H-x=P\mid Q,\qquad
P=(p_1,\ldots,p_m),\qquad
Q=(q_1,\ldots,q_s),
\]
with \(m,s\ge3\).

Consider first the spanning three-cover
\[
\mathcal D_P=(P-p_m)\mid(p_m,x)\mid Q.
\]
Write
\[
A=(p_1,\ldots,p_{m-1}),\qquad (u,v)=(p_m,x),\qquad C=Q.
\]
In the two-vertex-middle notation, \(u=p_m\) belongs to the left attachment set because
\[
(p_{m-2},p_{m-1},p_m)
\]
is inherited tight, while \(v=x\) does not belong to the right attachment set because
\[
(x,q_1,q_2)
\]
is non-tight in every deletion cover of a minimum counterexample.

If \(p_m\) belongs to the right attachment set, then the two-vertex-middle endpoint-reversal classification forces the mixed case with \(p_m\) as the unique attaching middle vertex and \(x\) reversing both exposed end edges. By the mixed two-vertex-middle descent theorem, \(\mathcal D_P\) admits a strict pairwise \(\Phi\)-descent.

Otherwise the right attachment set is empty. The same classification then gives
\[
(q_2,q_1,p_m),\qquad (q_2,q_1,x)
\]
tight. Thus \(p_m\) and \(x\) both reverse the displayed initial edge of \(Q\).

Now consider the symmetric middle-2 lift
\[
\mathcal D_Q=P\mid(x,q_1)\mid(Q-q_1).
\]
Here \(x\) does not attach to the terminal edge of \(P\), since
\[
(p_{m-1},p_m,x)
\]
is non-tight, while \(q_1\) attaches to the initial edge of \(Q-q_1\), since
\[
(q_1,q_2,q_3)
\]
is inherited tight.

If \(q_1\) also attaches to the terminal edge of \(P\), the two-vertex-middle classification again gives the mixed case and hence a strict \(\Phi\)-descent. Otherwise the left attachment set is empty, so
\[
(x,p_m,p_{m-1}),\qquad
(q_1,p_m,p_{m-1})
\]
are tight.

Consequently:

**Lemma.**
For every deletion cover \(H-x=P\mid Q\) with \(m,s\ge3\), at least one of the following holds.

1. One of the two elementary middle-2 lifts
   \[
   (P-p_m)\mid(p_m,x)\mid Q,\qquad
   P\mid(x,q_1)\mid(Q-q_1)
   \]
   admits a strict pairwise quadratic-potential descent.

2. The four vertices
   \[
   \{q_2,q_1,p_m,p_{m-1}\}
   \]
   have the explicit Hamiltonian order
   \[
   (q_2,q_1,p_m,p_{m-1}).
   \]

Indeed, if neither strict descent occurs, the first lift forces
\[
(q_2,q_1,p_m)
\]
tight and the second forces
\[
(q_1,p_m,p_{m-1})
\]
tight, so their concatenation is the displayed four-path.

This conclusion is independent of the central cross orientation \((p_m,x,q_1)\). In particular it simultaneously handles the \(1-0-0-0-1\) and \(1-0-1-0-1\) width-three patterns. It gives a simpler local interface: either immediate descent through a two-vertex middle, or a positioned cross four-support on the two exposed end edges.



### Four elementary middle-2 lifts isolate the double-alternating residue

Retain a minimum counterexample and a deletion cover
\[
H-x=P\mid Q,\qquad
P=(p_1,\ldots,p_m),\qquad
Q=(q_1,\ldots,q_s),
\]
with \(m,s\ge3\).

Apply the version-71 middle-2 lemma first to the ordered pair \(P,Q\). Either one of
\[
(P-p_m)\mid(p_m,x)\mid Q,\qquad
P\mid(x,q_1)\mid(Q-q_1)
\]
strictly descends in quadratic potential, or
\[
(q_2,q_1,p_m,p_{m-1})
\]
is a tight four-path.

Apply the same lemma after interchanging \(P\) and \(Q\). Either one of
\[
(Q-q_s)\mid(q_s,x)\mid P,\qquad
Q\mid(x,p_1)\mid(P-p_1)
\]
strictly descends, or
\[
(p_2,p_1,q_s,q_{s-1})
\]
is a tight four-path.

Hence, if none of the four elementary middle-2 lifts strictly descends, both opposite cross four-paths exist simultaneously:
\[
K_L=(q_2,q_1,p_m,p_{m-1}),
\qquad
K_R=(p_2,p_1,q_s,q_{s-1}).
\]

Now inspect the two central cross triples. If
\[
(p_m,x,q_1)
\]
is non-tight, boundary reversal gives
\[
(q_1,x,p_m)
\]
tight, and therefore
\[
(q_2,q_1,x,p_m,p_{m-1})
\]
is a tight five-path.

Likewise, if
\[
(q_s,x,p_1)
\]
is non-tight, then
\[
(p_1,x,q_s)
\]
is tight and
\[
(p_2,p_1,x,q_s,q_{s-1})
\]
is a tight five-path.

Therefore every deletion cover with \(m,s\ge3\) satisfies the trichotomy:

1. one of four explicit middle-2 lifts strictly descends in \(\Phi\);
2. there is an explicit positioned Hamiltonian five-support at one cross corner;
3. both central cross triples
   \[
   (p_m,x,q_1),\qquad(q_s,x,p_1)
   \]
   are tight, while both opposite cross four-paths \(K_L,K_R\) exist.

The third branch is the genuine double-alternating residue. All one-corner \(10001/10101\) ambiguity has disappeared: after excluding immediate descent and five-support, both opposite corners are simultaneously alternating and each carries a fixed cross four-path.



### General deletion covers reduce to the four-side regime

The version-72 trichotomy and the existing short-side descent tools combine into an arbitrary-order reduction.

First, no deletion cover of a minimum counterexample can have a component of order one or two. Indeed, if
\[
H-x=P\mid Q
\]
and \(|P|\le2\), then \(P\cup\{x\}\) has order at most three and is therefore Hamiltonian. A Hamilton path on \(P\cup\{x\}\) together with the displayed path \(Q\) would two-cover \(H\), contradiction. Hence every deletion-cover component has order at least three.

Now suppose one side, say \(P\), has order three. Since a minimum counterexample has order greater than ten,
\[
|Q|=|V(H)|-4\ge7.
\]
The three-side singleton-lift theorem applies directly to
\[
P\mid(x)\mid Q
\]
and gives a strict quadratic-potential descent within the same pairwise-repartition component.

It remains to consider deletion covers with both sides of order at least four.

Assume first that both sides have order at least five. Apply version 72. If one of the four elementary middle-2 lifts strictly descends, there is nothing to prove. Otherwise both cross four-paths exist. If either central cross triple is non-tight, version 72 gives an explicit Hamiltonian five-support.

Thus only the double-alternating branch remains. At the left corner put
\[
F=\{q_2,q_1,p_m,p_{m-1},x\}.
\]
The four-set
\[
F-x=\{q_2,q_1,p_m,p_{m-1}\}
\]
is Hamiltonian by version 72.

If \(F\) itself is Hamiltonian, again there is a positioned Hamiltonian five-support.

Suppose \(F\) is non-Hamiltonian. A non-Hamiltonian five-vertex boundary tournament has at most one non-Hamiltonian four-vertex induced subtournament. Therefore at least one of
\[
F-q_2=\{q_1,p_m,p_{m-1},x\},
\qquad
F-p_{m-1}=\{q_2,q_1,p_m,x\}
\]
is Hamiltonian.

If \(F-q_2\) is Hamiltonian, repartition
\[
P\mid(x,q_1)
\]
as
\[
(P-\{p_{m-1},p_m\})\mid(F-q_2).
\]
The affected component orders change from
\[
(m,2)\quad\text{to}\quad(m-2,4),
\]
so
\[
\Delta\Phi=16-4m<0
\]
because \(m\ge5\).

If \(F-p_{m-1}\) is Hamiltonian, repartition
\[
(p_m,x)\mid Q
\]
as
\[
(F-p_{m-1})\mid(Q-\{q_1,q_2\}).
\]
The affected orders change from
\[
(2,s)\quad\text{to}\quad(4,s-2),
\]
so
\[
\Delta\Phi=16-4s<0
\]
because \(s\ge5\).

Hence, whenever both deletion paths have order at least five, every deletion cover yields either a strict pairwise quadratic-potential descent or a positioned Hamiltonian five-support.

Combining the three observations gives:

**Four-side reduction.**
Let \(H\) be a minimum counterexample and let \(H-x=P\mid Q\) be any deletion cover. Then either

1. the associated singleton/middle-2 lift component admits a strict pairwise \(\Phi\)-descent;
2. \(H\) contains one of the positioned Hamiltonian five-supports produced above; or
3. one of \(P,Q\) has order exactly four.

Thus, after excluding immediate descent and the bounded five-support branch, the arbitrary-order deletion-cover problem reduces to the existing four-side regime. No small-order assumption is made: the side of order four is forced by the general argument.



### The forced four-side residue already gives descent or a five-support

Continue from the version-73 four-side reduction. Let
\[
H-x=X\mid Q
\]
be a surviving deletion cover with
\[
|X|=4,\qquad |Q|=s.
\]
Since a minimum counterexample has order greater than ten,
\[
s=|V(H)|-5\ge6.
\]

The singleton lift
\[
X\mid Q\mid(x)
\]
is a spanning three-cover. Apply the four-side endpoint-package theorem to the pair \(X\mid Q\).

Its first outcome is a legal pairwise repartition with affected component orders
\[
(4,s)\longrightarrow(5,s-1),
\]
whose potential change is
\[
\Delta\Phi=10-2s<0
\]
because \(s\ge6\). Hence this is a strict descent in the same three-cover component.

In the complementary endpoint-package branch, for every \(t\in X\) the five-set
\[
F_t=(X-\{t\})\cup\{q_1,q_s\}
\]
is Hamiltonian. Thus this branch already contains a positioned Hamiltonian five-support.

Combining this with version 73 yields:

**Deletion-to-five reduction.**
For every deletion cover
\[
H-x=P\mid Q
\]
of a minimum counterexample, the associated singleton/middle-support repartition component contains either

1. a spanning three-cover of strictly smaller quadratic potential than the displayed local lift; or
2. a positioned Hamiltonian five-support.

Indeed, sides of order at most two are impossible; a side of order three strictly descends by the three-side singleton-lift theorem; if both sides have order at least five, version 73 gives strict descent or a five-support; and the only remaining side order four is handled above.

Therefore the arbitrary-order deletion problem no longer has a separate three-side, four-side, balanced-long-side, or central-cross residue. All such branches feed the same two outcomes: strict descent or a Hamiltonian five-support.



### Large-order five-supports reduce to reversal or disturbance recurrence

Continue from the deletion-to-five reduction. Let \(X\) be a Hamiltonian five-support in a minimum counterexample, with
\[
H-X=P\mid Q
\]
a non-Hamiltonian two-cover of the complement. Let
\[
P=(p_1,\ldots,p_m)
\]
be the longer complementary path.

If \(|V(H)|\ge18\), then
\[
m\ge \left\lceil\frac{|V(H)|-5}{2}\right\rceil\ge7.
\]

Apply the five-side endpoint-core theorem to \(X\mid P\mid Q\).

If one endpoint of \(P\) extends \(X\) to a Hamiltonian six-set, the legal repartition
\[
(5,m)\longrightarrow(6,m-1)
\]
has
\[
\Delta\Phi=12-2m<0.
\]
Thus this branch is an immediate strict descent.

Otherwise both \(X\cup\{p_1\}\) and \(X\cup\{p_m\}\) are non-Hamiltonian, and there exists \(x\in X\) such that, with
\[
C=X-\{x\},
\]
both
\[
C\cup\{p_1\},\qquad C\cup\{p_m\}
\]
are Hamiltonian. Of course \(C\cup\{x\}=X\) is Hamiltonian as well, while
\[
C\cup\{x,p_1\}=X\cup\{p_1\},\qquad
C\cup\{x,p_m\}=X\cup\{p_m\}
\]
are non-Hamiltonian.

Therefore the root-exchange theorem applies to the four-core \(C\) with extenders \(x,p_1,p_m\). It yields one of four outcomes.

1. Two chosen Hamiltonian five-paths on
   \[
   C+x,\quad C+p_1,\quad C+p_m
   \]
   disagree on the relative order of \(C\). By the path-intersection calculus, such disagreement forces a reversed common edge, a tight triple reversing a displayed core edge, or a vertex-simple tight cycle.

2. There is a Hamiltonian four-set contained in
   \[
   C\cup\{x,p_1,p_m\}.
   \]
   In a minimum counterexample its complement has path-cover number two. If \(|V(H)|\ge15\), at least one path of that complement has order at least six, so the four-side endpoint package feeds this branch back into strict descent or a Hamiltonian five-support. Otherwise the total order is already bounded by fourteen.

3. A tight triple through a vertex of \(C\) reverses a displayed core edge between two of the extenders. This is already an explicit reversal certificate.

4. The six-set
   \[
   C\cup\{p_1,p_m\}
   \]
   is Hamiltonian. In a minimum counterexample its complement has path-cover number two. The rooted-six support theorem then yields either a one-label transfer back to a Hamiltonian five-support or a path disturbance: a split inherited edge of one complementary path, or a leave-and-return segment through exterior vertices.

Hence:

**Large-order five-support reduction.**
For \(|V(H)|\ge18\), every Hamiltonian five-support with path-cover-two complement yields either a strict quadratic-potential descent, or enters one of the already-established reversal/path-disturbance channels. The six-support outcome is not a new level of the hierarchy: it immediately returns to a five-support transfer or path disturbance.

Thus, after version 74, the remaining arbitrary-order obstruction is no longer a support-size case analysis. It is the compatibility and recurrence of reversal/order-disturbance data produced by the common four-core.



### Far-end reversal propagation is a one-vertex transfer theorem

Retain the version-70 setting. Let
\[
P\mid A\mid Q
\]
be a spanning three-cover,
\[
A=(a_1,\ldots,a_r),\qquad Q=(q_1,\ldots,q_t),
\]
and suppose an endpoint \(z\) of \(P\) reverses the terminal edge of \(A\):
\[
(z,a_r,a_{r-1})
\]
is tight.

Version 70 shows that at the far \(A/Q\) interface at least one of
\[
T_1=(a_2,a_1,q_t),\qquad
T_2=(a_1,q_t,q_{t-1})
\]
is tight.

If both are tight, then
\[
(a_2,a_1,q_t,q_{t-1})
\]
is a Hamiltonian four-path.

Suppose exactly \(T_1\) is tight. Then \(T_2\) is non-tight, so boundary reversal gives
\[
(q_{t-1},q_t,a_1)
\]
tight. Hence
\[
(q_1,\ldots,q_t,a_1)
\]
is a tight path, while
\[
(a_2,\ldots,a_r)
\]
is inherited tight. Thus \(A\mid Q\) admits the legal one-vertex transfer
\[
(A,Q)\longrightarrow(A-a_1,\;Q+a_1),
\]
with size change
\[
(r,t)\longrightarrow(r-1,t+1)
\]
and
\[
\Delta\Phi=2(t-r)+2.
\]

Suppose exactly \(T_2\) is tight. Then \(T_1\) is non-tight, so
\[
(q_t,a_1,a_2)
\]
is tight. Hence
\[
(q_t,a_1,\ldots,a_r)
\]
is a tight path and \(Q-q_t\) is inherited tight. Thus
\[
(A,Q)\longrightarrow(q_t+A,\;Q-q_t),
\]
with size change
\[
(r,t)\longrightarrow(r+1,t-1)
\]
and
\[
\Delta\Phi=2(r-t)+2.
\]

Therefore every propagated endpoint reversal gives either a Hamiltonian four-support or an explicit one-vertex transfer across the far interface.

At a quadratic-potential-minimal spanning three-cover this has a deterministic consequence.

- If \(r\ge t+2\), the transfer \(A\to Q\) would strictly decrease \(\Phi\), so the \(T_1\)-only branch is impossible. Outside the four-support branch, \(T_2\) alone survives; the new reversal is \(a_1\) reversing the terminal edge of the smaller path \(Q\).

- If \(t\ge r+2\), the transfer \(Q\to A\) would strictly decrease \(\Phi\), so the \(T_2\)-only branch is impossible. Outside the four-support branch, \(T_1\) alone survives; the new reversal targets the smaller path \(A\).

Thus whenever the two far component sizes differ by at least two, reversal propagation at a \(\Phi\)-minimum is directed toward the smaller component.

Iterating this observation over the three components gives a finite size-monotone picture: unless a Hamiltonian four-support appears or all relevant component sizes differ by at most one, an external reversal moves toward a component of minimum order. Once a minimum-order component is reached, propagation against any third component larger by at least two cannot leave it; instead an endpoint of that third component is forced to reverse the opposite displayed end edge of the same minimum component.

Hence the sole unbalanced recurrent residue is a **two-sided reversal trap on a minimum-order component**. This is the precise interface left after combining the bridge reductions with minimum-switch-span propagation.



### Any Phi-minimal size gap of at least two forces a Hamiltonian four-support

Let
\[
A\mid B\mid C
\]
be a spanning three-cover of a minimum counterexample that is \(\Phi\)-minimal in its pairwise-repartition component. Put
\[
a=|A|,\qquad b=|B|,
\]
and suppose
\[
b\ge a+2.
\]

Let \(y\) be either displayed endpoint of \(B\). Then
\[
H[V(A)\cup\{y\}]
\]
is non-Hamiltonian. Indeed, if it had a Hamilton path, deleting the endpoint \(y\) from \(B\) leaves an inherited tight path, so the pair \(A\mid B\) could be repartitioned with component orders
\[
(a,b)\longrightarrow(a+1,b-1).
\]
The potential change would be
\[
(a+1)^2+(b-1)^2-a^2-b^2
=2(a-b)+2<0,
\]
contradicting \(\Phi\)-minimality.

Apply the endpoint-replacement truncation dichotomy to the displayed path \(A\) and the exterior vertex \(y\). Since \(A+y\) is non-Hamiltonian, \(y\) is noninsertable at every position of the inherited displayed order of \(A\). In particular \(y\) cannot be prepended or appended. Hence boundary reversal gives
\[
(a_2,a_1,y),\qquad
(y,a_r,a_{r-1})
\]
tight, where
\[
A=(a_1,\ldots,a_r).
\]

The same conclusion holds for both displayed endpoints \(y_1,y_2\) of \(B\). Thus \(y_1,y_2\) are two distinct exterior reversers of each displayed end edge of \(A\).

By the two-common-reversers lemma, the exposed vertices contain a Hamiltonian four-set. Since a minimum counterexample has order greater than ten, this support is proper, and minimum-counterexample calculus gives its complement path-cover number exactly two.

Therefore:

**Size-gap four-support lemma.**
If a \(\Phi\)-minimal spanning three-cover has two component orders differing by at least two, then \(H\) contains a proper Hamiltonian four-support with non-Hamiltonian path-cover-two complement.

This conclusion does not require a pre-existing marked reversal. It is forced numerically by the size imbalance itself. In particular the unbalanced two-sided-reversal trap isolated in version 76 is not a new terminal geometry: the same size gap already creates a doubled reversal wall and hence a Hamiltonian four-support.



### Global funnel: bounded support or equitable external reversal

Version 77 has an immediate global consequence for quadratic minima.

Let
\[
P_1\mid P_2\mid P_3
\]
be a \(\Phi\)-minimal spanning three-cover of a minimum counterexample. If two component orders differ by at least two, version 77 forces a proper Hamiltonian four-support with non-Hamiltonian path-cover-two complement.

Therefore, in the absence of that bounded-support outcome,
\[
\max_i|P_i|-\min_i|P_i|\le1.
\]
Thus the size multiset is one of the three equitable profiles
\[
\{r,r,r\},\qquad
\{r+1,r,r\},\qquad
\{r+1,r+1,r\}.
\]

The quadratic-potential article already treats all three profiles.

- For \(\{r,r,r\}\), the comparison theorem yields order disagreement, at least two explicitly located mixed-support edges in a comparison cover, or a reverse tight triple at a displayed join.

- For \(\{r+1,r,r\}\), the profile theorem yields order disagreement, direct inter-support comparison edges, a split inherited edge, a leave-and-return block pattern, or a reverse tight triple at a displayed join.

- For \(\{r+1,r+1,r\}\), unless an equal-Phi move already gives a two-cover, strict descent, order disagreement, or a Hamiltonian four-/five-support, the neutral-transfer recurrence produces the structured three-core comparison configuration; every comparison two-cover then has order disagreement, at least three inter-core edges, a split inherited edge, or leave-and-return disturbance.

The current bridge/disturbance analysis absorbs these outputs as follows. Order disagreement produces a reversed common edge, a reversing tight triple, or a tight cycle by the path-intersection calculus. Direct mixing, split inherited edges, leave-and-return disturbance, and neutral omission swaps have all been reduced in the defect-line article to a two-cover, strict descent, a Hamiltonian four-support, or an external endpoint reversal.

Consequently:

**Global funnel theorem.**
At a quadratic-potential minimum in a minimum counterexample, every branch enters one of two geometric interfaces:

1. a proper Hamiltonian four- or five-support with non-Hamiltonian path-cover-two complement; or
2. an external tight triple reversing a displayed endpoint edge in an equitable three-cover.

No genuinely unbalanced \(\Phi\)-minimal profile remains outside the bounded-support architecture, and the comparison-disturbance branches of the equitable profiles introduce no third terminal residue.

This identifies the final large-order conversion problem cleanly: close external endpoint reversal in the equitable profiles, or show that it necessarily returns to the bounded four-/five-support architecture.



### Persistent one-crossing reversal recurrence has a six-state normal form

Let
\[
A=(a_1,\ldots,a_r),\qquad
B=(b_1,\ldots,b_s),\qquad
C=(c_1,\ldots,c_t)
\]
be a spanning three-cover with all three paths nontrivial. Suppose
\[
(b_1,a_r,a_{r-1})
\]
is tight, so the initial endpoint \(b_1\) of \(B\) reverses the terminal edge of \(A\).

Consider the recurrent branch in which, at every successive reversing endpoint, a chosen two-cover of the one-vertex deletion has exactly one cross-class edge relative to the three inherited support classes; all inherited block orders agree; and every direct two-cover, strict descent, neutral recurrence, bounded-support/reciprocal branch, and multi-crossing disturbance has been excluded.

Then the recurrence is forced, up to cyclic relabeling and simultaneous left-right reversal, through
\[
B_L\to A_R,\quad
C_R\to B_L,\quad
A_L\to C_R,\quad
B_R\to A_L,\quad
C_L\to B_R,\quad
A_R\to C_L,
\]
and then returns to \(B_L\to A_R\).

More explicitly, the six deletion covers have the forced mixed paths
\[
H-b_1:\quad A\mid C\,(B-b_1),
\]
\[
H-c_t:\quad B\mid (C-c_t)\,A,
\]
\[
H-a_1:\quad C\mid B\,(A-a_1),
\]
\[
H-b_s:\quad A\mid (B-b_s)\,C,
\]
\[
H-c_1:\quad B\mid A\,(C-c_1),
\]
\[
H-a_r:\quad C\mid (A-a_r)\,B.
\]

At each step, the residual carrier block cannot be isolated, since restoring its omitted endpoint would recover that displayed path and give a two-cover with the mixed component. In the present corner-turn branch it does not concatenate with the target component. It therefore concatenates with the third component. Of the two possible block orders, one permits direct restoration of the omitted endpoint and hence a two-cover; the opposite order is forced. Failure of restoration in that order is exactly the next endpoint reversal in the displayed six-state list.

Write
\[
A^\circ=(a_2,\ldots,a_{r-1}),\quad
B^\circ=(b_2,\ldots,b_{s-1}),\quad
C^\circ=(c_2,\ldots,c_{t-1}),
\]
when the relevant interiors are nonempty.

Opposite states force opposite tight concatenations on the same common support. Namely,
\[
C\,B^\circ\quad\text{and}\quad B^\circ\,C
\]
are both tight, as are
\[
C^\circ\,A\quad\text{and}\quad A\,C^\circ,
\]
and
\[
B\,A^\circ\quad\text{and}\quad A^\circ\,B.
\]
For example, the first pair is obtained by restricting the \(b_1\)-deletion cover at \(b_s\) and the \(b_s\)-deletion cover at \(b_1\); these are endpoint deletions of the displayed mixed paths and therefore preserve tightness.

Consequently the cyclic orders
\[
C\,B^\circ,\qquad A\,C^\circ,\qquad B\,A^\circ
\]
are tight cycles: one concatenation supplies all consecutive triples except the two wrap triples, and the opposite concatenation supplies exactly those wrap triples.

Thus, after all known exits are removed, a persistent one-crossing external-reversal recurrence is not diffuse. It consists of a six-state endpoint cycle together with three large overlapping tight cycles. The equitable external-reversal frontier of version 78 may therefore be refined further: either recurrence leaves the one-crossing regime, or it lands in this six-state/three-cycle normal form.



### The six-state one-crossing recurrence collapses to bounded support

The six-state normal form of version 79 is not a genuine terminal residue.

Retain its notation:
\[
A=(a_1,\ldots,a_r),\qquad
B=(b_1,\ldots,b_s),\qquad
C=(c_1,\ldots,c_t),
\]
and assume the six-state recurrence has been reached.

One of its deletion covers is
\[
H-a_1=C\mid B(A-a_1),
\]
where
\[
A-a_1=(a_2,\ldots,a_r)
\]
and the displayed concatenation
\[
B,a_2,\ldots,a_r
\]
is a tight path.

The induced set
\[
V(B)\cup(V(A)-\{a_1\})\cup\{a_1\}
=V(A)\cup V(B)
\]
is non-Hamiltonian. Otherwise a Hamilton path on \(A\cup B\), together with the displayed path \(C\), would two-cover \(H\).

Apply the endpoint-replacement truncation dichotomy to the displayed tight path
\[
B(A-a_1)
\]
and the exterior vertex \(a_1\). Since adjoining \(a_1\) does not Hamiltonize the support, \(a_1\) is noninsertable at every position of the displayed order. In particular it cannot be appended at the terminal end. Therefore
\[
(a_1,a_r,a_{r-1})
\]
is tight.

But the six-state recurrence already contains the reversal
\[
(a_1,c_t,c_{t-1})
\]
tight.

Thus the single carrier \(a_1\), which lies outside both displayed tight paths
\[
A-a_1=(a_2,\ldots,a_r)
\qquad\text{and}\qquad
C=(c_1,\ldots,c_t),
\]
simultaneously reverses their two terminal edges:
\[
(a_1,a_r,a_{r-1}),\qquad
(a_1,c_t,c_{t-1}).
\]

By the valid common-carrier lemma for two vertex-disjoint terminal edges, the exposed vertices contain a Hamiltonian four-support. In a minimum counterexample its complement is non-Hamiltonian with path-cover number two.

Hence:

**One-crossing recurrence collapse.**
A persistent one-crossing, order-compatible external-reversal recurrence cannot survive outside the bounded-support architecture. The six-state normal form of version 79 always produces a Hamiltonian four-support.

Therefore the equitable external-reversal frontier has no independent one-crossing terminal geometry. Any genuinely unresolved reversal recurrence must leave the one-crossing branch and enter a multi-crossing/split/leave-and-return comparison before returning to the existing bridge/disturbance machinery.



### Correction to versions 77--80: valid double-sided size-gap reduction

The proof of version 77 used the withdrawn same-edge-twins assertion. Two distinct exterior labels reversing one common displayed edge do not by themselves force a Hamiltonian four-set. Therefore the original version-77 proof and the unqualified version-78 funnel must be corrected.

The numerical part of version 77 remains valid and actually gives a stronger two-ended wall.

Let
\[
A\mid B\mid C
\]
be a \(\Phi\)-minimal spanning three-cover of a minimum counterexample, with
\[
a=|A|,\qquad b=|B|,\qquad b\ge a+2.
\]
For either displayed endpoint \(y\) of \(B\), the set \(A\cup\{y\}\) is non-Hamiltonian. Otherwise a Hamilton path on \(A+y\), together with the inherited path \(B-y\), gives a legal repartition
\[
(a,b)\longrightarrow(a+1,b-1)
\]
with
\[
\Delta\Phi=2(a-b)+2<0.
\]
Hence the endpoint-replacement dichotomy makes each endpoint \(y\) of \(B\) noninsertable at every position of the displayed path
\[
A=(a_1,\ldots,a_a).
\]
For both endpoints \(y_1,y_2\) of \(B\),
\[
(a_2,a_1,y_i),\qquad
(y_i,a_a,a_{a-1})
\]
are therefore tight. Thus the same two exterior labels reverse both exposed ends of \(A\).

If \(a\ge4\), the initial and terminal end edges of \(A\) are vertex-disjoint. Regard those edges as two disjoint tight paths of order two. The valid double-sided two-label reversal lemma in the defect-line article applies: two labels reversing both exposed sides force a Hamiltonian support of order four or five. In a minimum counterexample its complement is non-Hamiltonian with path-cover number two.

If \(a=3\), the existing theorem for a \(\Phi\)-minimum containing a three-path gives
\[
|V(H)|\le13.
\]
A \(\Phi\)-minimal three-cover has no component of order one or two.

Therefore:

**Corrected size-gap theorem.**
If a \(\Phi\)-minimal spanning three-cover has two component orders differing by at least two, then either
\[
|V(H)|\le13,
\]
or \(H\) contains a proper Hamiltonian support of order four or five whose complement has path-cover number two.

Consequently, for a minimum counterexample of order at least fourteen, absence of the bounded four-/five-support interface forces every \(\Phi\)-minimal profile to be equitable:
\[
\{r,r,r\},\qquad
\{r+1,r,r\},\qquad
\{r+1,r+1,r\}.
\]

This repairs the large-order funnel of version 78. Version 79's six-state normal form and version 80's collapse of that normal form use different local arguments and remain valid once interpreted inside this corrected large-order equitable frontier.


### The hard mixed bridge carries two rooted five-support probes

Retain the mixed universal pattern
\[
H-\{z,w\}=A\mid C,
\]
with
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s),
\]
and
\[
(a_{r-1},a_r,z),\quad (z,c_1,c_2),\quad
(w,a_r,a_{r-1}),\quad (c_2,c_1,w)
\]
tight. Assume the branch has not already returned to a bounded Hamiltonian support through the central four-set.

Lemma 44 gives that \(w\) is noninsertable into both \((A,z)\) and \((z,C)\). In particular
\[
(w,z,a_r),\qquad(c_1,z,w)
\]
are tight. Lemma 40 also gives
\[
(c_1,z,a_r)
\]
tight.

If
\[
(c_1,w,a_r)
\]
were tight, then \(z,w\) would be parallel middles between \(c_1\) and \(a_r\), so
\[
\{c_1,a_r,z,w\}
\]
would be Hamiltonian. Therefore outside the bounded-support branch,
\[
(a_r,w,c_1)
\]
is tight.

Now put
\[
U=\{a_{r-1},a_r,z,w,c_1,c_2\}.
\]
Apply the prescribed-pair six-set theorem to \(U\) with prescribed pair \(\{z,w\}\). With
\[
D=U-\{z,w\}=\{a_{r-1},a_r,c_1,c_2\},
\]
there are at least two distinct vertices \(d,e\in D\) such that
\[
U-\{d\},\qquad U-\{e\}
\]
are Hamiltonian five-sets. Both supports contain the bridge pair \(\{z,w\}\) and differ by one path-neighborhood vertex.

In a minimum counterexample, each of these proper Hamiltonian five-supports has a non-Hamiltonian complement of path-cover number two.

Hence every hard mixed bridge produces at least two overlapping rooted five-support probes preserving both bridge labels \(z,w\). The bridge-manufacture problem can therefore be reformulated as a comparison problem between the two complementary two-covers attached to these overlapping rooted probes. Any order disagreement, split inherited edge, leave-and-return disturbance, or external reversal in that comparison is already absorbed by the existing disturbance machinery; only a fully compatible overlap can remain quiet.


### Multi-crossing comparison has no quiet form

Let T be a genuine two-path cover of the union of three displayed connected path supports A,B,C, and assume that on each common support T preserves the inherited relative order. If no inherited displayed edge has endpoints in different T-components, connectedness of each displayed core forces the whole core to lie in one T-component. If, in addition, no T-component leaves a core through a nonempty block of another core and later returns, then each of A,B,C occurs as one contiguous T-block. Three nonempty blocks distributed among two nonempty comparison paths give exactly one inter-core T-edge. Therefore every comparison with at least two inter-core edges necessarily has a split inherited edge or a leave-and-return disturbance. In particular the >=3 crossing alternative in the equitable {r+1,r+1,r} profile is automatically absorbed by the existing disturbance machinery; the only quiet comparison geometry is one-crossing.

### Two overlapping bridge-pair probes cannot be locally featureless

Retain the v82 six-set U and choose distinct good deletion labels d,e outside the prescribed bridge pair {z,w}, so F_d=U-{d} and F_e=U-{e} are Hamiltonian five-supports. Put S=U-{d,e}; then {z,w} subset S and both S+d and S+e are Hamiltonian. If S is Hamiltonian, we already have a bridge-pair-rooted Hamiltonian four-support. Assume S is non-Hamiltonian. Compare Hamilton orders of S+d and S+e. If their induced orders on S disagree, the path-intersection calculus gives the existing reversal/order-disagreement interface. Otherwise both exceptional labels are inserted into one common order on S. Neither insertion can use an endpoint gap: deleting an endpoint-inserted label would leave that common order as a Hamilton path on S, contrary to non-Hamiltonicity. Hence both insertion slots are internal. The compatible one-vertex extension lemma now gives: separated slots => U=S+d+e is Hamiltonian; equal internal slots => a Hamiltonian four-set; adjacent slots => either U is Hamiltonian or the unique central triple fails and its boundary flip is a reversing tight triple. Thus the two rooted v82 probes cannot be locally quiet. The remaining issue is positional persistence: in the equal-slot four-support branch the new support need not retain both bridge labels, whereas the separated-slot six-support does retain them.


### The hard mixed-bridge central four-set is unique

Use the v82 notation and abbreviate a=a_r and c=c_1. Outside the bounded-support branch the central four-set X={a,z,w,c} is non-Hamiltonian, while the bridge/noninsertability relations give

(w,z,a), (c,z,w), (c,z,a), (a,w,c)

tight. Since a non-Hamiltonian four-set is edge-orderable with its three opposite-edge perfect matchings in strict blocks, write

M_1={aw,zc}, M_2={ac,zw}, M_3={az,wc}.

The four displayed triples translate to the incident-edge comparisons

zw<za,  zc<zw,  zc<za,  aw<wc.

Hence the matching blocks are forced in the unique order

M_1 < M_2 < M_3.

Because edges inside one opposite matching are disjoint, their relative order is irrelevant to every boundary triple. Thus the induced boundary tournament on {a,z,w,c} is uniquely determined. Equivalently its tight representatives are exactly

(w,a,z), (c,a,z), (w,a,c),
(w,z,a), (c,z,a), (c,z,w),
(a,w,z), (a,w,c), (z,w,c),
(z,c,a), (a,c,w), (z,c,w).

This removes the last local ambiguity in the hard bridge: every surviving mixed bridge contains the same oriented matching-block K4.

### Equal-slot loss of both bridge labels regenerates rooted probes

In the v83 equal-internal-slot branch, let K be the Hamiltonian four-set produced by the common slot of the two good probe roots d,e. If K contains neither z nor w, then necessarily K is exactly the four path-neighborhood vertices {a_{r-1},a_r,c_1,c_2}. The original two probe five-sets containing {z,w} remain available, so no positional information is actually lost. Moreover, if both K+z and K+w are non-Hamiltonian, the repeated-bad-extension theorem for a Hamiltonian four-set and two exterior vertices produces two Hamiltonian five-sets, each containing both z and w. Hence even replacing the probes by the equal-slot four-support cannot destroy bridge-pair-rooted support data permanently.


### Correction to the v83 non-Hamiltonian-core slot argument

The v83 paragraph beginning with two Hamiltonian five-probes \(S+d\) and \(S+e\) and a non-Hamiltonian common four-set \(S\) used an unjustified insertion model. A Hamiltonian path on \(S+d\) may have \(d\) internal; deleting \(d\) then leaves two path pieces rather than a Hamiltonian order on \(S\). Thus one cannot in general regard \(d,e\) as insertions into one common Hamilton order of a non-Hamiltonian \(S\).

The multi-crossing observation of v83 is unaffected. The six-set probe branch should instead be analyzed through the oriented six-set deletion graph.

### The oriented perfect-matching bridge exception strictly descends with the bridge pair retained

Retain the hard mixed bridge six-set
\[
U=\{u,t,z,w,c,d\},
\]
where
\[
u=a_{r-1},\qquad t=a_r,\qquad c=c_1,\qquad d=c_2,
\]
and
\[
H-\{z,w\}=A\mid C,
\qquad |A|=r,\quad |C|=s.
\]
Assume the central four-set
\[
X=\{z,w,t,c\}
\]
is non-Hamiltonian.

By v84, \(X\) is the unique oriented matching-block four-set with matching blocks
\[
\{tw,zc\}<\{tc,zw\}<\{tz,wc\}.
\]
In particular, relative to the fixed pair \((z,w)\),
\[
c\in C_+,\qquad t\in C_-,
\]
where
\[
C_+=\{y:(z,y,w)\text{ is tight}\},\qquad
C_-=\{y:(w,y,z)\text{ is tight}\}.
\]

Suppose the oriented six-set deletion graph is in its no-adjacent-edge perfect-matching exception. Then the four path-neighborhood labels
\[
D=\{u,t,c,d\}
\]
split into the two size-two orientation classes \(C_+,C_-\), and the two Hamiltonian fixed-pair four-supports are exactly
\[
\{z,w\}\cup C_+,\qquad
\{z,w\}\cup C_-.
\]

There are only two possibilities up to exchanging the class names.

#### Inherited-edge classes

Suppose
\[
C_-=\{u,t\},\qquad C_+=\{c,d\}.
\]
Then
\[
K_A=\{z,w,u,t\},
\qquad
K_C=\{z,w,c,d\}
\]
are Hamiltonian.

The first gives the legal pairwise repartition
\[
A\mid\{z,w\}
\longrightarrow
(A-\{u,t\})\mid K_A
\]
with
\[
\Delta\Phi=16-4r.
\]
The second symmetrically gives
\[
\Delta\Phi=16-4s.
\]
Since
\[
r+s=|V(H)|-2\ge9,
\]
at least one of \(r,s\) is at least five. Hence one of these two moves is a strict \(\Phi\)-descent, and the new Hamiltonian four-component still contains both bridge labels \(z,w\).

#### Crossed classes

Suppose
\[
C_+=\{c,u\},\qquad C_-=\{t,d\}.
\]
In the perfect-matching exception every five-set \(U-\{x\}\), \(x\in D\), is Hamiltonian.

Use
\[
F_u=U-\{u\}=\{t,z,w,c,d\}.
\]
First repartition \(A\mid\{z,w\}\) by moving the endpoint \(t\) into the two-set, obtaining
\[
(A-t)\mid\{t,z,w\}.
\]
Then repartition
\[
\{t,z,w\}\mid C
\]
as
\[
F_u\mid(C-\{c,d\}).
\]
Thus the original profile
\[
(r,2,s)
\]
reaches
\[
(r-1,5,s-2)
\]
within the same pairwise-repartition component, with
\[
\Delta_u
=26-2r-4s.
\]

Similarly let
\[
F_d=U-\{d\}=\{u,t,z,w,c\}.
\]
First move \(c\) into \(\{z,w\}\), and then repartition
\[
A\mid\{z,w,c\}
\]
as
\[
(A-\{u,t\})\mid F_d.
\]
This reaches profile
\[
(r-2,5,s-1)
\]
with
\[
\Delta_d
=26-4r-2s.
\]

If both changes were nonnegative, then
\[
r+2s\le13,\qquad 2r+s\le13.
\]
Adding gives
\[
3(r+s)\le26,
\]
contrary to \(r+s\ge9\).

Hence at least one move is a strict \(\Phi\)-descent. Again the new Hamiltonian five-component contains both bridge labels \(z,w\).

Therefore the oriented perfect-matching six-set exception is not a terminal bridge residue: it always admits a strict pairwise-repartition descent while retaining the full prescribed bridge pair.


### The mixed universal pattern is bridge-ready on one side

Retain the mixed universal pattern
\[
H-\{z,w\}=A\mid C,
\]
where
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s),
\]
and
\[
(a_{r-1},a_r,z),\qquad (z,c_1,c_2),
\]
\[
(w,a_r,a_{r-1}),\qquad(c_2,c_1,w)
\]
are tight. Put
\[
J_L=(a_{r-1},a_r,c_1),\qquad
J_R=(a_r,c_1,c_2).
\]

The two cross triples cannot both be tight, since then
\[
(a_1,\ldots,a_r,c_1,\ldots,c_s)
\]
would be Hamiltonian on \(H-\{z,w\}\), and together with the two-vertex path \(\{z,w\}\) would two-cover \(H\).

If both \(J_L,J_R\) are non-tight, their boundary reversals give
\[
(c_2,c_1,a_r,a_{r-1})
\]
as a Hamiltonian four-path. Thus, outside bounded support, exactly one of \(J_L,J_R\) is tight.

Suppose \(J_R\) is tight. Set
\[
L=(a_1,\ldots,a_{r-1}),\qquad R=C,\qquad
p=w,\ q=z,\ x=a_r.
\]
Then the three orders
\[
L,x,R,\qquad L,p,x,R,\qquad L,x,q,R
\]
have exactly the local defect form required by the abstract two-label one-defect bridge, except possibly for the predecessor triple
\[
(a_{r-2},a_{r-1},w)
\]
when \(r\ge3\). Hence, if that triple is tight or absent, the abstract bridge theorem yields a two-cover or a Hamiltonian four-/five-support with path-cover-two complement.

If it is non-tight, boundary antisymmetry gives
\[
(w,a_{r-1},a_{r-2})
\]
tight. Together with
\[
(w,a_r,a_{r-1})
\]
this says that \(w\) reverses the final two consecutive displayed edges of \(A\).

The case \(J_L\) tight is symmetric. Taking
\[
L=A,\qquad R=(c_2,\ldots,c_s),\qquad
p=z,\ q=w,\ x=c_1,
\]
the abstract bridge applies unless \(s\ge3\) and
\[
(w,c_2,c_3)
\]
is non-tight. In the exceptional case
\[
(c_3,c_2,w)
\]
is tight, so \(w\) reverses the first two consecutive displayed edges of \(C\).

Thus the mixed pattern reduces to
\[
\boxed{
\text{abstract one-defect bridge}
\ \vee\
\text{Hamiltonian four-support}
\ \vee\
\text{adjacent double reversal}.
}
\]

### Adjacent double reversal strictly descends while retaining the bridge pair

Treat the left-hand adjacent-double-reversal residue; the right-hand case is symmetric. Put
\[
u=a_{r-2},\qquad v=a_{r-1},\qquad t=a_r.
\]
Then
\[
(w,t,v),\qquad(w,v,u)
\]
are tight. The mixed pattern also gives
\[
(v,t,z),\qquad(w,z,t)
\]
tight. Define
\[
X=\{w,u,v,t\},\qquad
F=X\cup\{z\},\qquad
K=\{z,w,v,t\}.
\]

At least one of \(F,K\) is Hamiltonian.

Assume otherwise that \(F\) and \(K\) are both non-Hamiltonian. If \(X\) were also non-Hamiltonian, the non-Hamiltonian-five-set theorem would be violated, because a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Hence \(X\) is Hamiltonian.

Represent the non-Hamiltonian five-set \(F\) by an edge order. The restriction to the non-Hamiltonian four-set \(K\) is matching-block. The tight triples
\[
(v,t,z),\qquad(w,t,v),\qquad(w,z,t)
\]
force its matching blocks in the order
\[
\{wt,zv\}<\{wv,zt\}<\{wz,vt\}
\]
up to the corresponding relabeling; in particular they force
\[
vt<wv.
\]
But
\[
(w,v,u),\qquad(u,v,t)
\]
give
\[
wv<vu<vt,
\]
a contradiction. Hence at least one of \(F,K\) is Hamiltonian.

If \(F\) is Hamiltonian, repartition
\[
A\mid\{z,w\}
\longrightarrow
(a_1,\ldots,a_{r-3})\mid F.
\]
For \(r=3\) this is already a two-cover. Otherwise the affected size change is
\[
(r,2)\longrightarrow(r-3,5),
\qquad
\Delta\Phi=6(5-r).
\]
This is strict for \(r\ge6\), neutral for \(r=5\), and positive only for \(r=4\).

If \(K\) is Hamiltonian, repartition
\[
A\mid\{z,w\}
\longrightarrow
(a_1,\ldots,a_{r-2})\mid K,
\]
with
\[
(r,2)\longrightarrow(r-2,4),
\qquad
\Delta\Phi=4(4-r).
\]
This is strict for \(r\ge5\).

The remaining small values are strictly balanced using endpoints of the untouched path \(C\), without changing the Hamiltonian component containing \(z,w\).

- \(K,r=3\): after one endpoint transfer from \(C\) to the residual singleton, the total change is
  \[
  8-2s<0.
  \]
- \(K,r=4\): one endpoint transfer gives total change
  \[
  6-2s<0.
  \]
- \(F,r=5\): one endpoint transfer gives
  \[
  6-2s<0.
  \]
- \(F,r=4\): one endpoint transfer gives total change
  \[
  10-2s.
  \]
  This is strict for \(s\ge6\). If \(s=5\), it is neutral and a second endpoint transfer changes the profile \(5|2|4\) to \(5|3|3\), decreasing \(\Phi\) by \(2\).

The inequalities use only \(|V(H)|>10\).

Therefore every adjacent double reversal yields either a two-cover or a strict pairwise-repartition \(\Phi\)-descent, and throughout the descent the new Hamiltonian four- or five-component retains **both bridge labels \(z,w\)**.

Combining this with the completed abstract bridge gives:

\[
\boxed{
\text{mixed universal reversal pattern}
\Longrightarrow
\text{two-cover}
\ \vee\
\text{bounded support}
\ \vee\
\text{strict bridge-pair-preserving descent}.
}
\]

Thus the mixed pattern itself has no independent terminal geometry.


### Same-edge twins in the universal prescribed-pair pattern are bounded-support branches

Retain the universal prescribed-pair state
\[
H-\{u,v\}=A\mid C,
\qquad
A=(a_1,\ldots,a_r),\quad C=(c_1,\ldots,c_s),
\]
with \(r,s\ge2\).

Suppose the first endpoint-classification alternative holds:
\[
(u,a_r,a_{r-1}),\qquad
(v,a_r,a_{r-1})
\]
are tight. Thus \(u,v\) both reverse the displayed terminal edge of \(A\).

If, for one label, say \(u\),
\[
(c_{s-1},c_s,u)
\]
is non-tight, then boundary antisymmetry gives
\[
(u,c_s,c_{s-1})
\]
tight. The single carrier \(u\) then reverses the terminal edges of the two vertex-disjoint tight paths \(A\) and \(C\). The valid common-carrier lemma gives a Hamiltonian four-support with path-cover-two complement.

Hence, outside bounded support,
\[
(c_{s-1},c_s,u),\qquad
(c_{s-1},c_s,v)
\]
must both be tight: both labels append to \(C\).

If
\[
(u,a_1,a_2)
\]
were tight, then
\[
(u,a_1,\ldots,a_r)
\qquad\text{and}\qquad
(c_1,\ldots,c_s,v)
\]
would form a spanning two-cover. Therefore
\[
(u,a_1,a_2)
\]
is non-tight, and symmetrically so is
\[
(v,a_1,a_2).
\]
Thus
\[
(a_2,a_1,u),\qquad(a_2,a_1,v)
\]
are tight: both labels also reverse the displayed initial edge of \(A\).

If \(r\ge4\), the initial and terminal displayed end edges of \(A\) are vertex-disjoint. Regard them as two disjoint tight 2-paths. The two labels \(u,v\) reverse both exposed sides, so the valid double-sided two-label reversal lemma gives a Hamiltonian four- or five-support with path-cover-two complement.

If \(r=2\), both labels append to \(C\). The three-set \(A\cup\{u\}\) is Hamiltonian automatically, while
\[
C,v
\]
is a tight path. These two paths cover \(H\), contradiction.

If \(r=3\), apply the fixed-three-path extension theorem to the tight path \(A\) and the three exterior vertices
\[
u,\quad v,\quad c_s.
\]
At least one of
\[
A\cup\{u,v\},\qquad
A\cup\{u,c_s\},\qquad
A\cup\{v,c_s\}
\]
is Hamiltonian. In the first case that Hamiltonian five-set together with \(C\) two-covers \(H\). In the second case its complement is covered by
\[
\{v\}\mid(C-c_s),
\]
and in the third by
\[
\{u\}\mid(C-c_s).
\]
Thus the latter cases give a proper Hamiltonian five-support with non-Hamiltonian path-cover-two complement.

Therefore the same-terminal-edge twin alternative always yields a two-cover or bounded support. The same-initial-edge alternative is symmetric.

Consequently, in the universal prescribed-pair endpoint classification, the **only** alternative with genuinely new global content is the mixed pattern. By version 86 that mixed pattern itself reduces to a two-cover, bounded support, or strict bridge-pair-preserving \(\Phi\)-descent.


### Correction to the adjacent-double-reversal matching-block order

Version 86 wrote the three opposite-edge matching blocks of
\[
K=\{z,w,v,t\}
\]
in the wrong displayed order. The contradiction used there is nevertheless correct after fixing the block order.

The known tight triples are
\[
(v,t,z),\qquad(w,t,v),\qquad(w,z,t).
\]
In an edge-order representation they give
\[
vt<tz,\qquad wt<tv,\qquad wz<zt.
\]
The three opposite-edge matchings of \(K\) are
\[
M_1=\{zt,wv\},\qquad
M_2=\{zw,vt\},\qquad
M_3=\{zv,wt\}.
\]
Since \(K\) is non-Hamiltonian, these are strict blocks. The displayed inequalities force
\[
M_3<M_2<M_1.
\]
In particular
\[
vt<wv.
\]
The adjacent-double-reversal and inherited triples still give
\[
(w,v,u),\qquad(u,v,t)
\]
tight, hence
\[
wv<vu<vt,
\]
contradiction.

Thus the conclusion of version 86 is unchanged: at least one of the five-set \(F=\{z,w,u,v,t\}\) and the four-set \(K=\{z,w,v,t\}\) is Hamiltonian, and the subsequent strict-descent analysis remains valid.


### Every prescribed pair roots a clique of Hamiltonian four-supports

Let \(H\) be a minimum counterexample and fix any distinct vertices \(u,v\). Put
\[
X=V(H)-\{u,v\}.
\]
Partition \(X\) into the two fixed-pair orientation classes
\[
X_+=\{x:(u,x,v)\text{ is tight}\},
\qquad
X_-=\{x:(v,x,u)\text{ is tight}\}.
\]
Boundary antisymmetry gives \(X=X_+\dot\cup X_-\).

The fixed-pair bad-extension theorem in extremal01 says that if two vertices \(x,y\) lie in the same orientation class, then
\[
H[\{u,v,x,y\}]
\]
is Hamiltonian. Equivalently, all non-Hamiltonian pair-rooted four-sets use one vertex from each class.

Since a minimum counterexample has \(n>10\), one orientation class \(Y\) has
\[
|Y|\ge5.
\]
Therefore for every distinct \(x,y\in Y\),
\[
K_{xy}=\{u,v,x,y\}
\]
is a Hamiltonian four-support. Since \(K_{xy}\) is proper, minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K_{xy})=2.
\]

Thus every prescribed pair \(\{u,v\}\) is the common root of a complete graph on at least five exterior labels worth of Hamiltonian four-supports with non-Hamiltonian path-cover-two complements.

There is also a five-support density consequence. The fixed-pair density bound from extremal01 gives Hamiltonian-five density at least
\[
\frac{2(n-5)}{3(n-4)}
\]
among all five-sets containing \(\{u,v\}\). For \(n>10\), this exceeds the Erdős--Ko--Rado density
\[
\frac{3}{n-2}
\]
of an intersecting 3-uniform family on the remaining \(n-2\) vertices. Hence there exist two Hamiltonian five-supports
\[
\{u,v\}\cup A,\qquad \{u,v\}\cup B
\]
with
\[
|A|=|B|=3,\qquad A\cap B=\varnothing.
\]

So every possible bridge pair has both a large clique of rooted four-support probes and two rooted five-support wings meeting only in the bridge pair. This does not by itself complete bridge manufacture, but it shows that scarcity of pair-rooted Hamiltonian support is never the obstruction; the remaining issue is compatibility with the ambient displayed-path orders.
