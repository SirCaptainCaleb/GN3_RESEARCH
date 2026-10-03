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
