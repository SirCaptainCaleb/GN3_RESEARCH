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
