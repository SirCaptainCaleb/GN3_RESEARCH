# Counting and single-switch consequences

## Composition

Let k=\kappa_2(H)=1. The exact-root image lies in a linear space of dimension n-5, leaving three dimensions on the antipodal sphere S^{n-2}. For any prescribed triple S of actual vertices, augment the exact-root label by the three canonical role coordinates \rho_z\in\{+1,0,-1\} (left path, hole, right path), z\in S. Reversal negates the whole label, so Borsuk--Ulam gives a proper carrier face F with strictly positive weights, exact-root balance, and zero weighted role average for every z\in S.

Assume F has no zero exact root. Apply the four-central-vertices theorem. Every block strictly before the central block B is uniformly in the left canonical path and every block strictly after B is uniformly in the right canonical path. Hence a prescribed anchor with zero role average cannot lie outside B, so S\subseteq B. The two-vertex central case is impossible.

The three-vertex case is impossible as well. Up to left-right symmetry it has ell=s+1, r=s, |B|=3, L=2. The only nonzero roots are s->s+1 and s+1->s. Positive root balance gives positive total weight in both directions. For root s->s+1 the central role sum is -2; for root s+1->s it is 0. Thus the weighted average of the sum of the three central roles is strictly negative, contradicting the three zero anchor averages. The mirror case is strictly positive. Therefore every nonzero carrier of this augmented map has the unique form ell=r=s+1, |B|=L=4.

In that four-vertex case, the sum of the four central roles in a chamber equals p-c. Exact-root balance makes its weighted average zero. Since three central role averages are already zero, the fourth is zero too. Thus all four vertices of B are simultaneously balanced among left-path, hole, and right-path roles.

This leaves a finite four-vertex face conversion as the only nonzero exact-root branch when k=1.

There is also an equal-dimension Ky Fan alternative. For every proper face G define A(G)=intersection of the left canonical supports over its chambers and C(G)=intersection of the right canonical supports. If some face has A(G)=C(G)=empty, retain it as a unanimity-free carrier. Otherwise fix any total ordering of V(H) and label the barycentric vertex z_G by the signed element of A(G) union -C(G) having least absolute rank. Reversal negates the label. If G is contained in G', unanimity sets can only shrink, so comparable faces can never receive complementary labels. Ky Fan's antipodal lemma on S^{n-2}, with n available absolute labels, therefore gives an alternating maximal simplex with n-1 distinct absolute labels.

The bottom face of that chain is a chamber pi. Every signed label occurring higher in the chain is already unanimous in pi. Hence pi has at least n-1 vertices outside its canonical hole. Since k=1, it has exactly one hole vertex. Moreover, with respect to the prescribed total ordering, the left/right roles of the other n-1 vertices alternate in sign.

Consequently, for k=1 one has the structural dichotomy: either a proper face has no vertex unanimously on either canonical side, or for every prescribed ordering of V(H) there is a one-hole deletion cover whose two support roles alternate along that ordering after the hole label is removed. This uses no minimum-counterexample induction and no path-disturbance argument.

## Counting consequence of the alternating-cover branch

Suppose the unanimity-free-face outcome does not occur, so that for every prescribed total ordering of \(V(H)\) there is a one-hole deletion cover whose two support roles alternate after the hole label is removed.

Let \(n=|V(H)|\) and \(m=n-1\). Every such deletion cover is balanced:
\[
\{|P|,|Q|\}=\{\lfloor m/2\rfloor,\lceil m/2\rceil\}.
\]

Call \((x;\{P,Q\})\) a balanced deletion state when
\[
V(H)-\{x\}=P\sqcup Q
\]
and both supports are Hamiltonian.

**Proposition (many balanced deletion states).**
If \(N_{\rm bal}\) is the number of distinct balanced deletion states, then
\[
N_{\rm bal}\ge
\begin{cases}
\frac12\binom{m}{m/2},&m\text{ even},\\[2mm]
\binom{m}{\lfloor m/2\rfloor},&m\text{ odd}.
\end{cases}
\]

**Proof.**
There are \(n!\) prescribed total orders. Fix one balanced deletion state with support orders \(a,b\), \(a+b=m\). Choose the position of the hole in \(n\) ways. If \(a=b\), the alternating support word may start with either side and the vertices inside the two supports may be permuted arbitrarily, so this state certifies at most
\[
2n\,a!\,b!
\]
prescribed orders. If \(|a-b|=1\), the larger support must occupy both ends of the alternating word, so the corresponding number is
\[
n\,a!\,b!.
\]
The certified order sets of all balanced deletion states cover all \(n!\) orders. Comparing the total number of orders with the maximum number certified by one state gives the claimed lower bounds. \(\square\)

By pigeonhole, some actual vertex \(x\) is the hole in at least \(N_{\rm bal}/n\) distinct balanced deletion states. Thus one fixed subtournament \(H-x\) admits exponentially many complementary Hamiltonian bipartitions.

### Single-switch support interpretation

Let \(V(H)=A\sqcup B\) be a bipartition with sizes differing by at most one, and prescribe an order \(\sigma=(v_1,\ldots,v_n)\) whose parity classes are \(A,B\). If the alternating Ky Fan chamber has hole \(v_i\), deleting that position shifts the parity of every later position. Up to exchanging the two path supports, the support sets are therefore
\[
(A\cap\{v_1,\ldots,v_{i-1}\})
\cup
(B\cap\{v_{i+1},\ldots,v_n\})
\]
and
\[
(B\cap\{v_1,\ldots,v_{i-1}\})
\cup
(A\cap\{v_{i+1},\ldots,v_n\}).
\]

Hence the alternating-cover branch says that every balanced target bipartition, when written in alternating order, admits a deletion cover obtained by one support-color phase switch. When the prescribed order interleaves two displayed path supports, these are set-theoretic complementary splices of the two supports. This is the support geometry sought by complementary-splice arguments, obtained globally rather than by disturbance.


## Fixed-hole extremal target

The counting consequence does not itself contradict counterexamplehood: a fixed deletion \(H-x\) could in principle admit many balanced Hamiltonian bipartitions.

However, in a counterexample every balanced deletion state
\[
(x;\{P,Q\})
\]
has the additional property that neither one-vertex extension
\[
H[P\cup\{x\}],
\qquad
H[Q\cup\{x\}]
\]
is Hamiltonian. Indeed, if \(P\cup\{x\}\) were Hamiltonian, then
\[
(P\cup\{x\})\mid Q
\]
would be a spanning two-cover of \(H\), and similarly on the other side.

Therefore, in the alternating-cover branch, there exists a vertex \(x\) for which \(H-x\) has exponentially many complementary balanced bipartitions
\[
V(H)-\{x\}=P\sqcup Q
\]
such that

1. \(H[P]\) and \(H[Q]\) are Hamiltonian;
2. \(H[P\cup\{x\}]\) and \(H[Q\cup\{x\}]\) are both non-Hamiltonian.

This is the current sharp extremal target suggested by the Ky Fan route.

Equivalently, for one fixed \(x\), define
\[
\mathcal F_x
=
\left\{
P\subseteq V(H)-\{x\}:
|P|\in\{\lfloor(n-1)/2\rfloor,\lceil(n-1)/2\rceil\},
\ H[P]\text{ Hamiltonian},
\ H[P\cup\{x\}]\text{ non-Hamiltonian},
\right.
\]
\[
\left.
\phantom{\mathcal F_x=\{}
H[(V(H)-\{x\})\setminus P]\text{ Hamiltonian},
\ H[((V(H)-\{x\})\setminus P)\cup\{x\}]\text{ non-Hamiltonian}
\right\}.
\]

The alternating-cover branch forces \(\mathcal F_x\) to be exponentially large for some \(x\). Closing the branch can therefore be reduced to an upper bound on such a fixed-hole family, preferably through Johnson-graph adjacency, one-vertex-extension density, or complementary-pair restrictions.

This target is materially different from the earlier disturbance/minimal-hole program: the vertex \(x\) is fixed, while the complementary Hamiltonian supports vary through a very large family.


## Development

Let k=\kappa_2(H)=1. The exact-root image lies in a linear space of dimension n-5, leaving three dimensions on the antipodal sphere S^{n-2}. For any prescribed triple S of actual vertices, augment the exact-root label by the three canonical role coordinates \rho_z\in\{+1,0,-1\} (left path, hole, right path), z\in S. Reversal negates the whole label, so Borsuk--Ulam gives a proper carrier face F with strictly positive weights, exact-root balance, and zero weighted role average for every z\in S.

Assume F has no zero exact root. Apply the four-central-vertices theorem. Every block strictly before the central block B is uniformly in the left canonical path and every block strictly after B is uniformly in the right canonical path. Hence a prescribed anchor with zero role average cannot lie outside B, so S\subseteq B. The two-vertex central case is impossible.

The three-vertex case is impossible as well. Up to left-right symmetry it has ell=s+1, r=s, |B|=3, L=2. The only nonzero roots are s->s+1 and s+1->s. Positive root balance gives positive total weight in both directions. For root s->s+1 the central role sum is -2; for root s+1->s it is 0. Thus the weighted average of the sum of the three central roles is strictly negative, contradicting the three zero anchor averages. The mirror case is strictly positive. Therefore every nonzero carrier of this augmented map has the unique form ell=r=s+1, |B|=L=4.

In that four-vertex case, the sum of the four central roles in a chamber equals p-c. Exact-root balance makes its weighted average zero. Since three central role averages are already zero, the fourth is zero too. Thus all four vertices of B are simultaneously balanced among left-path, hole, and right-path roles.

This leaves a finite four-vertex face conversion as the only nonzero exact-root branch when k=1.

There is also an equal-dimension Ky Fan alternative. For every proper face G define A(G)=intersection of the left canonical supports over its chambers and C(G)=intersection of the right canonical supports. If some face has A(G)=C(G)=empty, retain it as a unanimity-free carrier. Otherwise fix any total ordering of V(H) and label the barycentric vertex z_G by the signed element of A(G) union -C(G) having least absolute rank. Reversal negates the label. If G is contained in G', unanimity sets can only shrink, so comparable faces can never receive complementary labels. Ky Fan's antipodal lemma on S^{n-2}, with n available absolute labels, therefore gives an alternating maximal simplex with n-1 distinct absolute labels.

The bottom face of that chain is a chamber pi. Every signed label occurring higher in the chain is already unanimous in pi. Hence pi has at least n-1 vertices outside its canonical hole. Since k=1, it has exactly one hole vertex. Moreover, with respect to the prescribed total ordering, the left/right roles of the other n-1 vertices alternate in sign.

Consequently, for k=1 one has the structural dichotomy: either a proper face has no vertex unanimously on either canonical side, or for every prescribed ordering of V(H) there is a one-hole deletion cover whose two support roles alternate along that ordering after the hole label is removed. This uses no minimum-counterexample induction and no path-disturbance argument.

## Counting consequence of the alternating-cover branch

Suppose the unanimity-free-face outcome does not occur, so that for every prescribed total ordering of \(V(H)\) there is a one-hole deletion cover whose two support roles alternate after the hole label is removed.

Let \(n=|V(H)|\) and \(m=n-1\). Every such deletion cover is balanced:
\[
\{|P|,|Q|\}=\{\lfloor m/2\rfloor,\lceil m/2\rceil\}.
\]

Call \((x;\{P,Q\})\) a balanced deletion state when
\[
V(H)-\{x\}=P\sqcup Q
\]
and both supports are Hamiltonian.

**Proposition (many balanced deletion states).**
If \(N_{\rm bal}\) is the number of distinct balanced deletion states, then
\[
N_{\rm bal}\ge
\begin{cases}
\frac12\binom{m}{m/2},&m\text{ even},\\[2mm]
\binom{m}{\lfloor m/2\rfloor},&m\text{ odd}.
\end{cases}
\]

**Proof.**
There are \(n!\) prescribed total orders. Fix one balanced deletion state with support orders \(a,b\), \(a+b=m\). Choose the position of the hole in \(n\) ways. If \(a=b\), the alternating support word may start with either side and the vertices inside the two supports may be permuted arbitrarily, so this state certifies at most
\[
2n\,a!\,b!
\]
prescribed orders. If \(|a-b|=1\), the larger support must occupy both ends of the alternating word, so the corresponding number is
\[
n\,a!\,b!.
\]
The certified order sets of all balanced deletion states cover all \(n!\) orders. Comparing the total number of orders with the maximum number certified by one state gives the claimed lower bounds. \(\square\)

By pigeonhole, some actual vertex \(x\) is the hole in at least \(N_{\rm bal}/n\) distinct balanced deletion states. Thus one fixed subtournament \(H-x\) admits exponentially many complementary Hamiltonian bipartitions.

### Single-switch support interpretation

Let \(V(H)=A\sqcup B\) be a bipartition with sizes differing by at most one, and prescribe an order \(\sigma=(v_1,\ldots,v_n)\) whose parity classes are \(A,B\). If the alternating Ky Fan chamber has hole \(v_i\), deleting that position shifts the parity of every later position. Up to exchanging the two path supports, the support sets are therefore
\[
(A\cap\{v_1,\ldots,v_{i-1}\})
\cup
(B\cap\{v_{i+1},\ldots,v_n\})
\]
and
\[
(B\cap\{v_1,\ldots,v_{i-1}\})
\cup
(A\cap\{v_{i+1},\ldots,v_n\}).
\]

Hence the alternating-cover branch says that every balanced target bipartition, when written in alternating order, admits a deletion cover obtained by one support-color phase switch. When the prescribed order interleaves two displayed path supports, these are set-theoretic complementary splices of the two supports. This is the support geometry sought by complementary-splice arguments, obtained globally rather than by disturbance.


## Fixed-hole extremal target

The counting consequence does not itself contradict counterexamplehood: a fixed deletion \(H-x\) could in principle admit many balanced Hamiltonian bipartitions.

However, in a counterexample every balanced deletion state
\[
(x;\{P,Q\})
\]
has the additional property that neither one-vertex extension
\[
H[P\cup\{x\}],
\qquad
H[Q\cup\{x\}]
\]
is Hamiltonian. Indeed, if \(P\cup\{x\}\) were Hamiltonian, then
\[
(P\cup\{x\})\mid Q
\]
would be a spanning two-cover of \(H\), and similarly on the other side.

Therefore, in the alternating-cover branch, there exists a vertex \(x\) for which \(H-x\) has exponentially many complementary balanced bipartitions
\[
V(H)-\{x\}=P\sqcup Q
\]
such that

1. \(H[P]\) and \(H[Q]\) are Hamiltonian;
2. \(H[P\cup\{x\}]\) and \(H[Q\cup\{x\}]\) are both non-Hamiltonian.

This is the current sharp extremal target suggested by the Ky Fan route.

Equivalently, for one fixed \(x\), define
\[
\mathcal F_x
=
\left\{
P\subseteq V(H)-\{x\}:
|P|\in\{\lfloor(n-1)/2\rfloor,\lceil(n-1)/2\rceil\},
\ H[P]\text{ Hamiltonian},
\ H[P\cup\{x\}]\text{ non-Hamiltonian},
\right.
\]
\[
\left.
\phantom{\mathcal F_x=\{}
H[(V(H)-\{x\})\setminus P]\text{ Hamiltonian},
\ H[((V(H)-\{x\})\setminus P)\cup\{x\}]\text{ non-Hamiltonian}
\right\}.
\]

The alternating-cover branch forces \(\mathcal F_x\) to be exponentially large for some \(x\). Closing the branch can therefore be reduced to an upper bound on such a fixed-hole family, preferably through Johnson-graph adjacency, one-vertex-extension density, or complementary-pair restrictions.

This target is materially different from the earlier disturbance/minimal-hole program: the vertex \(x\) is fixed, while the complementary Hamiltonian supports vary through a very large family.
