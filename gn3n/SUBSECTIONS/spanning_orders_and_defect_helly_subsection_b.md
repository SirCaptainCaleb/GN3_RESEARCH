# Exact inversion-window criterion

## Metadata

- ID: spanning_orders_and_defect_helly_subsection_b
- Parent Section: spanning_orders_and_defect_helly
- Position: 2
- Row version: 9
- Development version: 8
- Composition version: 2
- Composition stale: False

## Cold composition

### Inversion windows and deletion distance

For a spanning order \(\pi=(v_1,\ldots,v_n)\) with status word \(\epsilon_1,\ldots,\epsilon_m\), put
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
with \(p=m+1\) when there is no zero and \(q=0\) when there is no one.

**Theorem.**
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\quad q(\pi)\le p(\pi)+1.
\]
If \(q\le p+1\), a cut \(j\) with \(q\le j\le p+1\) gives the tight prefix \((v_1,\ldots,v_j)\) and, by boundary antisymmetry, the tight reversed suffix \((v_n,\ldots,v_{j+1})\). Conversely, a two-cover \(P\mid Q\), written as \((P,Q^{\rm rev})\), satisfies the displayed inequality.

Set
\[
d_2(\pi)=\max\{0,q(\pi)-p(\pi)-1\}
\]
and let \(\kappa_2(H)\) be the minimum number of deleted vertices required to obtain a two-cover. Then
\[
\boxed{\kappa_2(H)=\min_\pi d_2(\pi).}
\]
For positive deficiency the canonical paths are the prefix through \(v_{p+1}\) and the reversed suffix beginning at \(v_{q+1}\); the uncovered interval has exactly \(d_2(\pi)\) vertices.

If \(X\) is a minimum deletion set, \(|X|=\kappa_2(H)\), and \(H-X=P\mid Q\), then for every \(Y\subseteq X\),
\[
\boxed{\kappa_2\!\left(H-(X\setminus Y)\right)=|Y|.}
\]
Indeed, deleting \(Y\) gives the displayed two-cover, while a smaller deletion in the intermediate graph would produce fewer than \(|X|\) deletions in \(H\).

Consequently every nonempty \(Y\subseteq X\) is absolutely nonaugmentable relative to \(P\mid Q\): neither \(P\cup Y\) nor \(Q\cup Y\) is Hamiltonian, and no partition \(Y=Y_P\sqcup Y_Q\) makes both \(P\cup Y_P\) and \(Q\cup Y_Q\) Hamiltonian. This minimum-hole heredity will be used repeatedly below.

## Development

### Exact inversion-window criterion

There is a sharper order-relative formulation of the two-cover problem than the extreme-switch compression.

Let
\[
\pi=(v_1,\ldots,v_n),\qquad m=n-2,
\]
with status word \(\epsilon_1,\ldots,\epsilon_m\). Define
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
using the conventions \(p=m+1\) if there is no zero and \(q=0\) if there is no one.

**Theorem (exact inversion-window criterion).**
\[
\boxed{\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }q(\pi)\le p(\pi)+1.}
\]

**Proof.** Suppose first that \(q\le p+1\). Choose an integer cut \(j\) with
\[
q\le j\le p+1.
\]
Then every status wholly inside \(v_1,\ldots,v_j\), namely every \(\epsilon_i\) with \(i\le j-2\), equals \(1\), because \(j-2\le p-1\). Thus
\[
P=(v_1,\ldots,v_j)
\]
is tight. Every status wholly inside \(v_{j+1},\ldots,v_n\), namely every \(\epsilon_i\) with \(i\ge j+1\), equals \(0\), because \(j+1>q\). Boundary antisymmetry therefore makes
\[
Q=(v_n,\ldots,v_{j+1})
\]
tight. Hence \(P\mid Q\) is a spanning two-cover, with the evident empty-side convention at the ends.

Conversely, let \(P\mid Q\) be a spanning cover by at most two tight paths. Concatenate
\[
\pi=(P,Q^{\rm rev})
\]
and let \(j=|P|\). Every status with \(i\le j-2\) is \(1\), while every status with \(i\ge j+1\) is \(0\). Hence \(p\ge j-1\) and \(q\le j\), so \(q\le p+1\). \(\square\)

Thus a counterexample satisfies
\[
q(\pi)-p(\pi)\ge2
\]
for every spanning order. The quantity
\[
\delta(\pi)=q(\pi)-p(\pi)-1
\]
is an exact order-level two-cover deficiency: \(\delta\le0\) is already a certificate.

### Reversal coordinates for the exact obstruction

Put
\[
c(\pi)=m+1-q(\pi).
\]
Reversal-complement gives
\[
p(\pi^{\rm rev})=c(\pi),\qquad
c(\pi^{\rm rev})=p(\pi).
\]
Hence
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}
\]
is an odd type-\(A\) root label:
\[
\psi(\pi^{\rm rev})=-\psi(\pi).
\]

Moreover
\[
\delta(\pi)=m-\bigl(p(\pi)+c(\pi)\bigr).
\]
Therefore the exact two-cover threshold is the anti-diagonal
\[
p+c\ge m,
\]
while every chamber of a counterexample lies strictly below it:
\[
p+c\le m-1.
\]

This exact inversion root retains substantially more theorem-relevant information than the first/last-switch root. Its tail is the first actual non-tight status, its head is the reflected last actual tight status, and the sum of the two root coordinates measures the exact distance from the two-cover window. It is therefore the natural root for a second pass through the barycentric balance argument.

### Exact deficiency equals deletion distance to a two-cover

The order-level deficiency has an exact global interpretation.

For a spanning order \(\pi\), put
\[
d_2(\pi)=\max\{0,q(\pi)-p(\pi)-1\}.
\]
Define the **two-cover deletion distance**
\[
\kappa_2(H)
=
\min\{|X|:X\subseteq V(H),\ \operatorname{pc}(H-X)\le2\}.
\]

**Theorem (deletion-distance identity).**
\[
\boxed{\kappa_2(H)=\min_{\pi} d_2(\pi).}
\]

**Proof.** Fix a spanning order \(\pi=(v_1,\ldots,v_n)\).

If \(d_2(\pi)=0\), the exact inversion-window criterion already gives \(\operatorname{pc}(H)\le2\), so \(\kappa_2(H)=0\).

Assume \(d_2(\pi)>0\), and write
\[
p=p(\pi),\qquad q=q(\pi).
\]
Then
\[
P=(v_1,\ldots,v_{p+1})
\]
is tight, because every status before \(p\) is \(1\), and
\[
Q=(v_n,v_{n-1},\ldots,v_{q+1})
\]
is tight, because every status after \(q\) is \(0\) and boundary reversal makes the reversed suffix tight. The two paths are disjoint, and the uncovered set is
\[
X_\pi=\{v_{p+2},\ldots,v_q\},
\]
with
\[
|X_\pi|=q-p-1=d_2(\pi).
\]
Hence
\[
\kappa_2(H)\le d_2(\pi).
\]
Taking the minimum over \(\pi\) gives
\[
\kappa_2(H)\le\min_\pi d_2(\pi).
\]

Conversely, let \(X\subseteq V(H)\) have \(|X|=k\) and let
\[
H-X=P\mid Q
\]
be a two-cover. Write \(r=|P|\), choose any order \(x_1,\ldots,x_k\) of \(X\), and form
\[
\pi=(P,x_1,\ldots,x_k,Q^{\rm rev}).
\]
Every status wholly inside \(P\) is \(1\), so
\[
p(\pi)\ge r-1.
\]
Every status wholly inside \(Q^{\rm rev}\) is \(0\); in all cases this gives
\[
q(\pi)\le r+k.
\]
Therefore
\[
q(\pi)-p(\pi)-1\le k,
\]
and hence
\[
d_2(\pi)\le k.
\]
Minimizing first over \(\pi\) and then over such \(X\) gives
\[
\min_\pi d_2(\pi)\le\kappa_2(H).
\]
The two inequalities prove the identity. \(\square\)

Thus the exact inversion coordinate measures a genuine edit distance:
\[
\boxed{\text{minimum exact deficiency}
=
\text{minimum number of vertices whose deletion makes the tournament two-coverable}.}
\]

For a counterexample, the minimum deficiency is positive. For a minimum counterexample, every one-vertex deletion is two-coverable, so
\[
\kappa_2(H)=1
\qquad\Longrightarrow\qquad
\min_\pi d_2(\pi)=1.
\]
This recovers the exact-deficiency-one conclusion of Section 7 conceptually, without any separate junction calculation. The junction calculation remains useful because it shows more: every chosen deletion cover of a minimum counterexample yields a deficiency-one order and identifies the omitted vertex as the common terminal-edge reverser.


### Size-profile dictionary

For an order with positive exact deficiency, the canonical partial cover has
\[
|P_\pi|=p(\pi)+1,
\qquad
|Q_\pi|=c(\pi)+1,
\qquad
|X_\pi|=\delta(\pi).
\]
Hence
\[
n=(p+1)+(c+1)+\delta.
\]
Thus the exact inversion root \(e_p-e_c\) records the signed imbalance of the two canonical path orders, while the anti-diagonal deficit \(m-(p+c)\) is exactly the number of uncovered vertices. Reversal swaps the two path orders and negates the root. In particular, on a minimum-hole order arising from a two-cover \(P|Q\) of \(H-X\), the root is
\[
e_{|P|-1}-e_{|Q|-1}.
\]
This identifies the exact-root topology as a topology of partial two-cover size profiles rather than merely of abstract switch coordinates.

### Canonical side labels cannot flip across one swap when the exact hole is at least two

Assume
\[
\kappa_2(H)=k\ge2.
\]
For a spanning order \(\pi\), give each actual vertex its canonical role
\[
\sigma_\pi(v)=
\begin{cases}
+,&v\in P_\pi,\\
0,&v\in X_\pi,\\
-,&v\in Q_\pi.
\end{cases}
\]
Reversal negates the signs and preserves the zero set.

**Lemma.** If \(\pi'\) is obtained from \(\pi\) by one adjacent transposition, then no vertex changes directly from \(+\) to \(-\), or from \(-\) to \(+\).

**Proof.** Let \(p,q\) and \(p',q'\) be the exact inversion coordinates, and suppose that a vertex \(v\) is \(+\) in \(\pi\) and \(-\) in \(\pi'\). Write \(t,t'\) for its two positions, so \(|t-t'|\le1\). Since \(v\in P_\pi\),
\[
t\le p+1,
\qquad
q-p-1\ge k,
\]
hence
\[
q\ge t+k.
\]
Since \(v\in Q_{\pi'}\),
\[
t'\ge q'+1,
\qquad
q'-p'-1\ge k,
\]
so
\[
p'\le t-k-1.
\]
Thus \(p'<p\) and \(q'<q\).

An adjacent transposition changes only four consecutive status positions, say a set \(J\) of diameter at most three. Because the first zero moved left, the new first-zero position \(p'\) must lie in \(J\). Because the last one moved left, the old last-one position \(q\) must also lie in \(J\). Hence
\[
q-p'\le3.
\]
But the two displayed bounds give
\[
q-p'\ge2k+1\ge5,
\]
a contradiction. The reverse sign change is symmetric. \(\square\)

Therefore, when \(k\ge2\), canonical roles change along the permutahedron graph only through the hole:
\[
+\longleftrightarrow0\longleftrightarrow-.
\]
This is the missing local compatibility for a signed-partition Tucker formulation; it is stronger than the old rook condition because it is attached to actual vertices and the exact two-cover deficiency.

### Minimum-hole faces have constant exact root

Let \(X\) be a minimum deletion set of order \(k=\kappa_2(H)>0\), and fix
\[
H-X=P\mid Q,\qquad |P|=r,\quad |Q|=s.
\]
For every ordering \(\sigma\) of \(X\), the spanning order
\[
\pi_\sigma=(P,\sigma,Q^{\rm rev})
\]
has exact deficiency at most \(k\). The deletion-distance identity makes \(k\) the global minimum, so equality holds. Consequently
\[
p(\pi_\sigma)=r-1,\qquad
q(\pi_\sigma)=r+k,\qquad
c(\pi_\sigma)=s-1
\]
for every \(\sigma\). Hence the whole \((k-1)\)-dimensional permutahedral face obtained by freely permuting \(X\) carries the constant exact root
\[
e_{r-1}-e_{s-1}.
\]
In particular the exact-root geometry records minimum deletion states as honest faces rather than isolated chamber labels.

### The Boolean cube generated by a minimum hole

Let
\[
X\subseteq V(H),\qquad |X|=k=\kappa_2(H),
\]
be a minimum deletion set, and fix a two-cover
\[
H-X=P\mid Q.
\]

For every subset \(Y\subseteq X\), put
\[
H_Y:=H-(X\setminus Y).
\]

**Theorem (hereditary exactness of a minimum hole).**
For every \(Y\subseteq X\),
\[
\boxed{\kappa_2(H_Y)=|Y|.}
\]

**Proof.** Deleting \(Y\) from \(H_Y\) leaves \(H-X=P\mid Q\), so
\[
\kappa_2(H_Y)\le |Y|.
\]
If \(\kappa_2(H_Y)<|Y|\), choose \(Z\subseteq V(H_Y)\) with
\[
|Z|<|Y|,\qquad \operatorname{pc}(H_Y-Z)\le2.
\]
Then deleting
\[
(X\setminus Y)\cup Z
\]
from \(H\) leaves the same two-coverable graph, while
\[
|(X\setminus Y)\cup Z|
\le k-|Y|+|Z|
<k,
\]
contradicting the definition of \(X\). \(\square\)

Thus a minimum hole carries an entire Boolean cube of exact deletion distances.

Write
\[
P=(p_1,\ldots,p_r),\qquad Q=(q_1,\ldots,q_s).
\]
For every nonempty \(Y\subseteq X\) and every ordering
\[
\sigma=(y_1,\ldots,y_t),\qquad t=|Y|,
\]
the spanning order of \(H_Y\)
\[
(P,\sigma,Q^{\rm rev})
\]
has exact deficiency at most \(t\). The theorem makes \(t\) the global minimum deficiency of \(H_Y\), so equality holds. Consequently
\[
p=r-1,\qquad q=r+t,\qquad c=s-1
\]
for every such \(Y\) and every ordering of \(Y\).

In particular every \(x\in X\) satisfies the same two terminal reversal relations
\[
(x,p_r,p_{r-1}),
\qquad
(x,q_s,q_{s-1})
\]
tight.

### Absolute nonaugmentability of the complementary paths

The Boolean-cube identity gives a stronger global obstruction than failure of insertion into one displayed order.

**Corollary (absolute nonaugmentability).**
Let \(Y\subseteq X\) be nonempty.

1. The induced boundary tournament on \(V(P)\cup Y\) is non-Hamiltonian.
2. The induced boundary tournament on \(V(Q)\cup Y\) is non-Hamiltonian.
3. More generally, for no partition
   \[
   Y=Y_P\sqcup Y_Q
   \]
   can both \(H[V(P)\cup Y_P]\) and \(H[V(Q)\cup Y_Q]\) be Hamiltonian.

**Proof.**
If \(P\cup Y\) had a Hamilton tight path, then deleting only \(X\setminus Y\) from \(H\) would leave a two-cover consisting of that Hamilton path and \(Q\), using fewer than \(k\) deletions. The statement for \(Q\) is symmetric.

For the third statement, Hamilton paths on the two displayed enlarged supports would two-cover
\[
H-(X\setminus Y),
\]
again contradicting
\[
\kappa_2(H_Y)=|Y|>0.
\]
\(\square\)

Hence a minimum exact hole is a synchronized family of common terminal-edge reversers that is simultaneously **unabsorbable in every nonempty subfamily and under every split between the two complementary paths**. This is a global structural constraint on one fixed graph, not a minimum-counterexample or disturbance hypothesis.

### Exact classification of direct side flips at deletion distance one

Assume
\[
\kappa_2(H)=1.
\]
Let \(\pi'\) be obtained from \(\pi\) by one adjacent transposition. Suppose an actual vertex \(v\) changes directly from the canonical left path to the canonical right path:
\[
v\in P_\pi,\qquad v\in Q_{\pi'}.
\]

Write \(t\) for the position of \(v\) in \(\pi\), and let
\[
p,q,\delta
\quad\text{and}\quad
p',q',\delta'
\]
be the exact inversion data of \(\pi,\pi'\).

**Proposition (rigid direct side flip).**
Then \(v\) moves one place to the right, and necessarily
\[
p=t-1,\qquad q=t+1,\qquad \delta=1,
\]
while
\[
p'=t-2,\qquad q'=t,\qquad \delta'=1.
\]
If \(w\) is the vertex swapped with \(v\), then \(w\) is the unique canonical hole vertex in **both** chambers.

The reverse transition \(Q\to P\) is symmetric.

**Proof.**
Since \(v\in P_\pi\),
\[
t\le p+1.
\]
Because every order has deficiency at least one,
\[
q\ge p+2\ge t+1.
\]

Let \(t'\) be the position of \(v\) in \(\pi'\). Since \(v\in Q_{\pi'}\),
\[
t'\ge q'+1,
\]
and
\[
q'\ge p'+2.
\]
Hence
\[
p'\le q'-2\le t'-3.
\]
Because one adjacent transposition moves \(v\) by at most one place,
\[
t'\le t+1,
\]
so
\[
p'\le t-2.
\]
Therefore
\[
q-p'\ge3.
\]

A direct \(P\to Q\) transition forces both the first-zero coordinate and the last-one coordinate to move left. An adjacent transposition changes only the four consecutive status positions whose windows meet the swapped pair; these positions have diameter at most three. Thus the new first zero \(p'\) and the old last one \(q\) both lie in that affected set, so
\[
q-p'\le3.
\]
Hence equality holds throughout:
\[
q-p'=3.
\]

The preceding inequalities must all be equalities. Thus
\[
q=t+1,\qquad p'=t-2,\qquad t'=t+1.
\]
Now
\[
q\ge p+2,\qquad p\ge t-1
\]
forces
\[
p=t-1,
\]
and similarly
\[
q'\ge p'+2,\qquad q'\le t'-1=t
\]
forces
\[
q'=t.
\]
Therefore
\[
\delta=q-p-1=1,\qquad
\delta'=q'-p'-1=1.
\]

Let \(w\) be the vertex adjacent to \(v\) that is swapped past it. In \(\pi\), the unique hole position is
\[
p+2=t+1,
\]
which is occupied by \(w\). In \(\pi'\), the unique hole position is
\[
p'+2=t,
\]
again occupied by \(w\). Thus the hole label is conserved across the direct side flip. \(\square\)

Consequently, when \(\kappa_2(H)=1\), all direct side changes in the chamber graph are confined to deficiency-one edges and carry a canonical conserved decoration:
\[
\boxed{
P\leftrightarrow Q
\text{ across one swap}
\Longrightarrow
\text{the same vertex is the unique hole on both endpoints}.
}
\]
This replaces the \(k\ge2\) no-direct-side-flip rule by an exact description of the only possible exception.
