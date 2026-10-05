# Article VII — antipodal geodesics, defect Helly theory, and topological compression

## Composition status

- Composition version: 1
- Stale: False
- Composed through revision: 1083

## Cold composition

---

## Section — Spanning orders and defect Helly theory

<!-- section_id: spanning_orders_and_defect_helly -->

### Defect intervals and the exact Helly criterion

### Spanning orders and status words

Let \(H\) be a boundary \(3\)-tournament on vertex set \(V\), and let
\[
\pi=(v_1,\ldots,v_n)
\]
be a spanning order. The cases \(n\leq1\) have path-cover number at most one. Throughout the cut formulation assume \(n\geq2\), and interpret the intersection of an empty defect family as the full cut set \(\{1,\ldots,n-1\}\). Write
\[
\epsilon_i(\pi)=
\begin{cases}
1,&(v_i,v_{i+1},v_{i+2})\text{ is tight},\\
0,&(v_i,v_{i+1},v_{i+2})\text{ is non-tight},
\end{cases}
\qquad 1\le i\le n-2.
\]
The word
\[
\epsilon_1(\pi)\cdots \epsilon_{n-2}(\pi)
\]
is the status word of \(\pi\).

The two-cover problem is already visible in one status word. Put a cut between \(v_j\) and \(v_{j+1}\), where \(1\le j\le n-1\). Every consecutive triple wholly contained in either side must be tight if the two inherited blocks are to be tight paths. A non-tight triple centered at status position \(i\) is harmless precisely when the cut separates one of its two adjacent vertex pairs.

It is convenient to encode this in the defect line from [[defect_lines_and_spanning_order_compression_the_defect_line_identity]]. Let the possible cuts be the vertices
\[
1,\ldots,n-1,
\]
and for every non-tight status position \(i\) put the defect edge
\[
I_i=\{i,i+1\}.
\]
Thus the defect family is an interval family on a line.

### The exact Helly theorem

**Theorem 1 (defect-interval Helly criterion).** A spanning order \(\pi\) yields a spanning two-cover by one cut if and only if
\[
\bigcap_{\epsilon_i(\pi)=0} I_i\ne\varnothing.
\]
Equivalently, the defect-line graph has vertex-cover number at most one.

**Proof.** A cut \(j\) leaves a non-tight triple inside one of the two inherited blocks exactly when \(j\notin I_i\). Hence both inherited blocks are tight exactly when \(j\) belongs to every defect interval. This is the asserted intersection condition. The graph formulation is the same statement, because the defect intervals are precisely the edges of the defect line. \(\square\)

The theorem is order-relative. Quantifying over all spanning orders gives the exact existence formulation
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ such that }\bigcap_{\epsilon_i(\pi)=0}I_i\ne\varnothing.
}
\]

Because intervals on a line are Helly, failure has an especially sharp witness.

**Corollary 2 (separated defect pair).** If \(\pi\) does not yield a two-cover, then there are two non-tight positions \(i<j\) with
\[
I_i\cap I_j=\varnothing.
\]
Equivalently,
\[
j\ge i+2.
\]

Thus every bad spanning order contains two separated defects. There is no need to retain the entire defect set merely to certify failure.

### Reversal and the antipodal defect pair

Let
\[
\pi^{\rm rev}=(v_n,\ldots,v_1).
\]
Boundary antisymmetry gives
\[
\epsilon_i(\pi^{\rm rev})
=
1-\epsilon_{n-1-i}(\pi).
\]
Thus reversal reflects the status positions and complements the colors.

Consequently a counterexample has two simultaneous interval statements. Every spanning order contains two separated non-tight defects, and its reverse contains two separated non-tight defects corresponding to two separated tight positions of the original order. In the Freudenthal language introduced in the next Section, every bad chamber therefore carries a separated defect pair, and the antipodal chamber carries the complementary pair.

This is the exact supported content of the earlier informal phrase that every bad Freudenthal simplex “contains a pair.” No stronger mysterious pair theorem is assumed.

### Extreme defects and switch coordinates

The separated pair can be compressed further by choosing extreme witnesses. When the status word contains both colors, let
\[
a(\pi)=\text{first switch position},
\qquad
b(\pi)=\text{last switch position}.
\]
Equivalently, \(a\) and \(b\) mark the first and last boundaries between monochromatic runs. The reflected terminal coordinate
\[
\bar b(\pi)=m-b(\pi),
\qquad m=n-2,
\]
is chosen so that reversal exchanges \(a\) and \(\bar b\).

These extreme coordinates lose information: they remember only the outermost failure of a one-run description, not the complete defect family. Their virtue is topological. They are the coordinates from which the later rook labels and root vectors are built.

This distinction will remain important throughout the article:

- the defect intervals encode the **exact two-cover condition**;
- extreme switch coordinates are a **compression** designed for topology.

The later topological argument is useful only if its compressed recurrence can ultimately be returned to the exact defect or support formulations.


### Exact inversion-window criterion

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

### Local forbidden patterns and witness handoff

The exact criterion
[
q(pi)le p(pi)+1
]
has a finite local form. A bad word has a zero followed by a one at distance at least two. Choose such a pair with minimum separation.

If the separation is two, the three-bit subword is (001) or (011). If the separation is at least three, minimality forces every position immediately after the first zero to be (1), and every position immediately before the last one to be (0). Separation at least four would force an overlap carrying both values, so the only remaining case has separation three and subword (0101).

Therefore
[
oxed{
qle p+1
iff
epsilon_1cdotsepsilon_m	ext{ avoids }001, 011, 0101.
}
]

Thus every failure of the exact two-cover criterion is witnessed on at most four consecutive status positions.

Under reverse-complement, (001) and (011) exchange, while the alternating pattern is the centered self-reflecting type. These local witnesses are the inputs to the fixed witness-path topology developed later in [[local_witness_topology_and_the_finite_terminal_theorem]].

Complementing all triple colors preserves path-cover number after reversing each path, so the opposite-polarity witnesses
[
110, 100, 1010
]
may be tracked simultaneously. This dual-polarity refinement is what removes the formerly unbounded symmetric-double witness branch.

---

## Section — The Norine–GN3 dictionary and Freudenthal geometry

<!-- section_id: norine_gn3_dictionary_and_freudenthal_geometry -->

### Geodesic chambers, memory, and the stronger general route

### Cube geodesics, permutations, and Freudenthal simplices

Let \(V\) be an \(n\)-element label set. Identify the vertices of the cube \([0,1]^V\) with subsets of \(V\). A monotone geodesic from \(\varnothing\) to \(V\) adds every label exactly once and is therefore specified by a permutation
\[
\pi=(v_1,\ldots,v_n),
\qquad
S_i=\{v_1,\ldots,v_i\}.
\]
The convex hull
\[
\Delta_\pi
=
\operatorname{conv}\{
\mathbf1_{S_0},\ldots,\mathbf1_{S_n}
\}
\]
is a maximal simplex of the standard staircase, or Freudenthal, triangulation of the cube. Conversely every maximal simplex arises in this way.

Thus
\[
\boxed{
\text{monotone antipodal cube geodesics}
\longleftrightarrow
\text{permutations}
\longleftrightarrow
\text{maximal Freudenthal simplices}.
}
\]

This is the basic dictionary behind the Norine analogy. It is an exact identification, not a metaphor.

Every maximal simplex contains the long diagonal
\[
[\mathbf0,\mathbf1].
\]
The link of that diagonal consists of chains of nonempty proper subsets of \(V\). It is the barycentric subdivision of the boundary of an \((n-1)\)-simplex and hence an \((n-2)\)-sphere. Cube complementation
\[
A(x)=\mathbf1-x
\]
sends \(\Delta_\pi\) to \(\Delta_{\pi^{\rm rev}}\); on the link it is fixed-point-free. This is the type-\(A\) Coxeter sphere on which the later antipodal topology lives.

### One-step data and two-step memory

The shared geometry should not obscure a crucial difference in the local data.

For an ordinary antipodal cube-edge coloring, the color encountered along a geodesic is attached to one cube edge. It depends on the present coordinate step. This is one-step data.

For a boundary tournament, the local status is
\[
h(u,v,w)=
\begin{cases}
1,&(u,v,w)\text{ is tight},\\
0,&(u,v,w)\text{ is non-tight},
\end{cases}
\]
and along
\[
\pi=(v_1,\ldots,v_n)
\]
the word is
\[
h(v_1,v_2,v_3),\ldots,h(v_{n-2},v_{n-1},v_n).
\]
The color therefore depends on three successive directions, or equivalently on two steps of memory.

Boundary antisymmetry is
\[
h(w,v,u)=1-h(u,v,w).
\]
Thus reversal of a geodesic complements the local word exactly as antipodality should, but the coloring is not an ordinary edge coloring of the bare cube.

Geometrically, \(h(u,v,w)\) is naturally attached to the monotone three-step flag
\[
S
\subset
S\cup\{u\}
\subset
S\cup\{u,v\}
\subset
S\cup\{u,v,w\},
\]
and is independent of the base set \(S\). This translation invariance is one of the strongest formal distinctions from an arbitrary cube coloring.

### The stronger conclusion and the class of inputs

A function on ordered triples of distinct labels satisfying
\[
h(w,v,u)=1-h(u,v,w)
\]
is exactly a boundary \(3\)-tournament: declare \((u,v,w)\) tight when \(h(u,v,w)=1\). Conversely every boundary tournament gives such a function. The local tournament at a middle vertex \(v\) has arc \(u\to w\) precisely when \(h(u,v,w)=1\). This structure follows from the displayed identity; it is not an additional hypothesis.

**Candidate one-change conjecture.** Every boundary \(3\)-tournament admits a spanning order whose consecutive-triple word changes color at most once.

This strengthens the desired conclusion on the same class of inputs. It is not a generalization to a larger class of triple colorings. The candidate implies a two-cover directly: split the order between its two monochromatic portions, then reverse any portion with non-tight triples. The memory lift below makes the candidate a precise geodesic assertion.

There are also two directed versions, requiring respectively \(1^a0^b\) and \(0^a1^b\). Reversal of the vertex order reverses and complements the word, so it preserves each directed type. One cannot change the direction of the switch merely by reversing the order. Auxiliary exactification uses specifically the first type.

### A genuinely larger memory class

To allow more general local data, one may let the color depend on the previously used set:
\[
g(S;u,v,w)\in\{0,1\},\qquad S\subseteq V\setminus\{u,v,w\},
\]
with antipodal identity
\[
g(V\setminus(S\cup\{u,v,w\});w,v,u)
=1-g(S;u,v,w).
\]
A permutation reads these colors with \(S\) equal to the prefix preceding its three displayed directions. Boundary tournaments are precisely the subclass independent of \(S\). An arbitrary reversal-complement assignment of words to whole permutations is broader still; it need not satisfy any consistency between permutations sharing a triple.

Thus the useful distinction is between antipodal symmetry alone and a consistent, base-independent rule on ordered triples. Local reversals, endpoint transport, and repartitions exploit that consistency. They do not distinguish boundary tournaments from the function \(h\) already displayed above.

A theorem for the larger class would require its own statement and proof, including the prescribed poles and the desired switch direction. No such theorem is asserted here.

### A cochain viewpoint

There is a useful algebraic way to summarize the difference.

An ordinary cube-edge coloring may be treated as degree-\(1\) local data on oriented cube edges. The GN3 status behaves instead as a translation-invariant degree-\(3\) local datum on monotone three-edge flags: translating the base subset \(S\) does not change the value attached to the direction triple \(u,v,w\).

Along one chamber, the discrete derivative
\[
\epsilon_{i+1}-\epsilon_i
\]
records switch positions. Thus the switch pattern is the one-dimensional coboundary of the local color word along that chamber, while the underlying color itself comes from a higher-memory translation-invariant rule.

This language is not needed for the proofs below, but it deserves a numbered place because future topology may need to distinguish exactly these two levels: arbitrary antipodal edge data versus translation-invariant higher-memory data.

### Working principle

The chamber geometry is shared with cube-geodesic problems. The local data differ. We may seek the stronger one-change conclusion for boundary tournaments, or work only in the auxiliary extensions for which directed one-change existence is equivalent to a two-cover. A broader theorem for base-dependent memory is a separate possible generalization. These distinctions concern respectively the conclusion, the input subclass, and the input class.


### Proof-transfer meta-conjecture

The present GN3 problem and Norine-type antipodal cube-geodesic problems share the same global Freudenthal/Coxeter chamber geometry but differ in their local data.

For GN3, the geodesic status comes from a base-independent two-memory rule
[
h(u,v,w)in{0,1},
qquad
h(w,v,u)=1-h(u,v,w).
]
A broader bounded-memory cube model may allow
[
g(S;u,v,w)
]
to depend on the current base set (S), subject to the corresponding antipodal reversal-complement identity. Ordinary Norine edge colorings belong naturally to the lower-memory side of that broader class.

This motivates an independent meta-conjecture:

> Whatever arguments ultimately close the boundary-tournament conjecture should contain a substantial portable core which, after suitable reformulation, seeds a proof of a generalized Norine geodesic conjecture.

The most plausible portable ingredients are the chamber topology, antipodal symmetry, local witness-tree compression, carrier recurrence, and a relative-index/terminalization argument. The steps most likely to remain GN3-specific are the strong face-permutation arguments that use translation invariance of (h(u,v,w)), especially endpoint swaps and blockwise splicing.

Accordingly the final proof should be decomposed after closure into:
1. purely chamber-topological arguments;
2. bounded-memory local arguments;
3. genuinely GN3-specific translation-invariant arguments.

The independent brainstorm [[meta_conjecture_gn3_closure_should_seed_generalized_norine]] records this research program. It is not required for the present conjecture, but it should remain visible while the terminalization theorem is developed.

---

## Section — The memory lift and exact antipodal geodesics

<!-- section_id: memory_lift_and_exact_antipodal_geodesics -->

### The memory lift, antipodality, and zero detour


### The memory-lift graph

The staircase triangulation identifies spanning orders with cube geodesics, but the GN3 color at one step depends on three successive directions. Introduce a ranked graph \(\Gamma_n\) that stores precisely this missing memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and
\[
S\subseteq V\setminus\{u,v\}.
\]
Give such a state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\).

Join \(s\) to every state
\[
(\sigma,\varnothing,u,v).
\]
Join
\[
(\sigma,S,u,v)
\longrightarrow
(\sigma,S\cup\{u\},v,w)
\]
whenever
\[
w\notin S\cup\{u,v\},
\]
and join every rank-\((n-1)\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by
\[
h(u,v,w),
\]
and a terminal edge by \(1-\sigma\).

The underlying graph depends only on \(n\). The boundary tournament enters only through the internal edge colors.

### Antipodal involution and cube projection

Define
\[
A(s)=t,\qquad A(t)=s,
\]
and
\[
A(\sigma,S,u,v)
=
\bigl(
\sigma,\,
V\setminus(S\cup\{u,v\}),\,
v,u
\bigr).
\]
This is fixed-point-free.

An internal edge carrying \(u,v,w\), when mapped by \(A\) and read in increasing-rank direction, carries \(w,v,u\). Hence its color is complemented by
\[
h(w,v,u)=1-h(u,v,w).
\]
Source and terminal colors are also complementary.

There is an antipodal projection to the cube,
\[
p(s)=\varnothing,\qquad
p(t)=V,\qquad
p(\sigma,S,u,v)=S\cup\{u\}.
\]
Every edge projects to a cube edge and
\[
p(Ax)=V\setminus p(x).
\]

Thus \(\Gamma_n\) is a finite two-step-memory lift of the cube.

### Pole geodesics are spanning orders

Every edge changes rank by one, so
\[
d(s,t)\ge n.
\]
Given
\[
\pi=(v_1,\ldots,v_n)
\]
and \(\sigma\in\{0,1\}\), there is a length-\(n\) path
\[
s,\,
(\sigma,S_0,v_1,v_2),\,
(\sigma,S_1,v_2,v_3),\ldots,t,
\]
with the obvious indexing
\[
S_i=\{v_1,\ldots,v_i\}.
\]

Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and therefore determines a unique permutation and copy index.

Hence pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\,
h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\,
1-\sigma.
\]

Therefore a spanning order whose internal word changes color at most once is exactly a pole geodesic with at most one internal change after choosing the appropriate copy.

### Geodesicity is the no-reuse condition

The strengthened Norine analogy becomes exact at this point.

For an arbitrary \(s\)-\(t\) walk \(W\), let \(m_v\) be the number of projected cube edges using coordinate \(v\). Since the projection joins antipodal cube vertices, every \(m_v\) is odd. Thus
\[
|W|
=
\sum_{v\in V}m_v
=
n+
2\sum_{v\in V}\frac{m_v-1}{2}.
\]

Consequently
\[
\boxed{
W\text{ is geodesic}
\iff
m_v=1\text{ for every }v.
}
\]

Zero detour is exactly the requirement that each original vertex, or each cube dimension, be used once.

This is the sharp distinction between the desired theorem and a generic antipodal-path theorem. A one-change antipodal walk that repeats a coordinate does not encode a spanning order. A theorem whose antipodal endpoints are allowed to vary likewise does not solve the distinguished-pole problem.

The topology must preserve simultaneously:

1. the prescribed poles;
2. geodesicity;
3. the two-step memory carried by the state.

### The stronger problem represented exactly

The memory lift gives an exact graph formulation of the stronger one-change spanning-order target:

\[
\boxed{
H\text{ has a one-change spanning order}
\iff
\Gamma_n(H)\text{ has a one-change pole geodesic}.
}
\]

This equivalence is useful but must not be confused with the original two-cover conjecture. A two-cover need not itself appear as a one-change spanning order of \(H\).

That distinction is the point at which the next Section begins.

> **Transition.** The memory lift makes one-change spanning orders into genuine one-change antipodal geodesics, but on \(H\) this remains potentially stronger than the two-cover conjecture. We now remove that discrepancy.


---

## Section — Auxiliary exactification and complementary path supports

<!-- section_id: auxiliary_exactification_and_complementary_supports -->

### Exactification before support-family development

### One-change orders and opposite-edge supports

Before exactifying the theorem, it is useful to record the support meaning of a one-change order.

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets
\[
X\subseteq V\setminus\{u,v\}
\]
for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word
\[
1^a0^b
\]
exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},
\qquad
Y\in\mathcal F_{vu}
\]
with
\[
X\sqcup Y=V\setminus\{u,v\}.
\]
Indeed, the tight prefix ends in \(u,v\), while reversing the non-tight suffix turns it into a tight path ending in \(v,u\). Conversely the two tight paths splice to a one-change order.

Equivalently, one may use two tight paths having one common terminal vertex. If
\[
P=(p_1,\ldots,p_\ell,v),
\qquad
Q=(q_1,\ldots,q_m,v),
\]
then
\[
(p_1,\ldots,p_\ell,v,q_m,\ldots,q_1)
\]
has at most one change. Conversely splitting a one-change order and reversing the non-tight side gives such a common-terminal pair.

These formulations concern the directed word \(1^a0^b\). The other direction uses opposite initial edges or a common initial vertex. Either common-terminal path may be a singleton.

One useful quantitative consequence is retained from [[antipodal_geodesics_and_complementary_path_supports]]: a one-change order on \(N\geq2\) vertices yields two tight paths sharing an edge, so their orders sum to \(N+2\). Hence at least one has
\[
\left\lceil\frac{N+2}{2}\right\rceil
\]
vertices. This helps explain why the one-change target on the original vertices may be stronger than a two-cover.

We now exactify the original theorem before developing these support formulations further.

### Auxiliary-vertex exactification

Adjoin a new vertex \(r\) to \(H\). Retain every old triple and impose
\[
h(u,v,r)=1,
\qquad
h(r,v,u)=0
\]
for distinct \(u,v\in V(H)\). Values of
\[
h(u,r,v)
\]
may be chosen arbitrarily subject to boundary reversal.

Every spanning order of the extension is uniquely
\[
(L,r,R).
\]

**Theorem 3 (exact one-change extension).**
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
H^+\text{ has a spanning order of directed form }1^a0^b.
}
\]

Assume \(V(H)\ne\varnothing\). More precisely, directed one-change orders of \(H^+\) occur in reversal pairs and map two-to-one onto two-covers of \(H\). A cover is an unordered collection of individually ordered paths.

**Proof.** Suppose
\[
(L,r,R)
\]
has directed form \(1^a0^b\). If \(|L|\ge2\), the last two vertices of \(L\) followed by \(r\) form a tight triple by construction. Hence every earlier triple on the left belongs to the initial tight run, so \(L\) is a tight path. Likewise a triple beginning at \(r\) is non-tight, forcing the entire right side into the non-tight run; therefore \(R^{\rm rev}\) is a tight path. Removing \(r\) gives
\[
L\mid R^{\rm rev}.
\]

Conversely, from a two-cover
\[
P\mid Q
\]
the two orders
\[
(P,r,Q^{\rm rev}),
\qquad
(Q,r,P^{\rm rev})
\]
have directed form \(1^a0^b\). The possible triple with \(r\) in the middle may have either value without creating a second switch. For a one-path cover \(P\), the two orders are \((P,r)\) and \((r,P^{\rm rev})\); when deleting \(r\), discard an empty side. The two side orders are recoverable from the spanning order, proving the two-to-one assertion. \(\square\)

This theorem is the conceptual pivot of the article. From here onward the geodesic and support formulations model the **actual conjecture**, not merely a stronger surrogate.

### Exact geodesic form

Apply the memory lift to \(H^+\) and keep the copy with source color \(1\). Its pole-geodesic words begin in \(1\) and end in \(0\). Therefore
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}.
}
\]

The switch is normalized near \(r\). If
\[
P=(p_1,\ldots,p_k),
\qquad
Q=(q_1,\ldots,q_\ell),
\]
then the order
\[
(P,r,Q^{\rm rev})
\]
changes in the junction containing \(r\). There is no separate search for the switch position.

Similarly, in the opposite-edge support formulation for \(H^+\), the shared oppositely directed edge necessarily contains \(r\). In the common-terminal formulation, the endpoint-moving involution has a unique representative whose common endpoint is \(r\). Deleting \(r\) from that normalized state recovers the two-cover.

### Complementary tails in the exactified problem

The support-family language can now be read without ambiguity.

A directed one-change order of \(H^+\) is equivalent to two tight paths
\[
P=(X,u,v),
\qquad
Q=(Y,v,u)
\]
whose union is \(V(H^+)\), whose intersection is the ordinary edge \(uv\), and whose remaining supports are complementary.

Because the exactification forces
\[
r\in\{u,v\},
\]
this is an exact support encoding of a two-cover of \(H\).

Equivalently, normalize the paired common-terminal state so that both paths end at \(r\):
\[
P=(P_H,r),
\qquad
Q=(Q_H,r).
\]
Then
\[
P_H\mid Q_H
\]
is a two-cover of \(H\).

Thus the unresolved support problem may be stated as a complementary-tail problem **with a distinguished root** rather than as an arbitrary opposite-endpoint problem. This positional normalization is important: many topological arguments naturally produce support abundance, but the theorem needs the correct root and the correct endpoint order.

### The endpoint-moving involution

For completeness, common-terminal pairs on a fixed support carry a fixed-point-free involution.

Suppose
\[
P=(A,u,v),
\qquad
Q=(B,w,v).
\]
Exactly one of
\[
(u,v,w),
\qquad
(w,v,u)
\]
is tight. If the first is tight, replace the pair by
\[
(A,u,v,w),
\qquad
(B,w).
\]
The common endpoint moves from \(v\) to \(w\). If \(B\) is nonempty with last vertex \(z\), tightness of the old second path gives \((z,w,v)\) tight, so the same rule returns to \(v\). The other orientation is symmetric.

If one path is the singleton \((v)\), write the other as \((A,u,v)\) and replace the pair by \((A,u)\) and \((v,u)\). These are tight, and the preceding rule returns to the old pair when \(A\) is nonempty; when \(A\) is empty the singleton rule itself returns. Thus the involution is defined on every common-terminal pair whose union has at least two vertices.

The involution explains why common-terminal states naturally occur in pairs. In \(H^+\), exactly one member of such a pair has common endpoint \(r\), which is another form of the exactification.

### The common-terminal counting identity

One useful identity from the earlier positive enumeration has a direct combinatorial proof. For a boundary tournament \(J\) on at least two vertices, let \(A(J)\) count spanning orders of directed form \(1^a0^b\), and let \(h(J)\) count ordered tight Hamilton paths. Let \(b(J)\) count a choice of vertex \(v\) and an unordered pair of nonempty tight paths partitioning \(V(J)\setminus\{v\}\), such that appending \(v\) to either path remains tight. Then
\[
\boxed{A(J)=h(J)+b(J).}
\]

**Proof.** Common-terminal pairs with a singleton member correspond to the \(h(J)\) Hamilton paths; pairs with both members nontrivial correspond to the \(b(J)\) certificates. The endpoint-moving involution groups all these pairs into two-element orbits, one for each unordered opposite-terminal-edge pair. Such an edge pair also gives exactly two directed one-change orders, exchanged by reversal. Conversely a directed word has a uniquely specified shared edge: if it contains \(a\) tight triples, use its vertices in positions \(a+1,a+2\). Thus both sides count twice the number of opposite-terminal-edge pairs. \(\square\)

This identity retains the earlier square-zero calculation's positive combinatorial content without requiring its transfer matrices. It concerns the directed one-change target on \(J\); it does not assert that an arbitrary two-cover of \(J\) gives such an order.

### Positive factorization

Work in the square-zero algebra
\[
\mathcal A
=
\mathbb Q[x_v:v\in V]/(x_v^2:v\in V).
\]
Let
\[
F_H
=
\sum_{P\text{ nonempty tight in }H}x_{V(P)},
\]
counting distinct path orders separately.

For \(S\subseteq V\), let \(m_r(S)\) be the number of directed one-change orders on \(S\cup\{r\}\). Applying the exact extension to every induced subtournament gives
\[
\boxed{
\sum_{S\subseteq V}m_r(S)x_S
=
(1+F_H)^2.
}
\]

The constant term is the singleton order \(r\); the term \(2F_H\) places one nonempty tight path on either side of \(r\); and \(F_H^2\) records two disjoint nonempty tight paths. Square-zero multiplication removes intersecting supports with no cancellation.

In particular
\[
m_r(V)
=
2[x_V]\left(F_H+\frac12F_H^2\right).
\]

This factorization does not itself prove positivity. Its value is conceptual: it confirms that the auxiliary one-change model counts exactly the original one- and two-path covers.

The first half of Article VII is therefore exact:
\[
\text{two-cover}
\longleftrightarrow
\text{rooted one-change order}
\longleftrightarrow
\text{rooted one-change geodesic}
\longleftrightarrow
\text{rooted complementary supports}.
\]
The second half asks what antipodal topology can force inside these exact models.


### Further developments



---

## Section — From antipodal labels to cellular root topology

<!-- section_id: antipodal_labels_and_cellular_root_topology -->

### From rook labels to cellular roots

### Extreme-switch labels

Return first to the unexactified permutation sphere, where the local topology is easiest to see. For a spanning order whose status word contains at least two runs, let
\[
a(\pi)=\text{first switch position},
\qquad
b(\pi)=\text{last switch position},
\]
and put
\[
m=n-2,
\qquad
\bar b(\pi)=m-b(\pi).
\]

Reversal exchanges the two extreme coordinates:
\[
a(\pi^{\rm rev})=\bar b(\pi),
\qquad
\bar b(\pi^{\rm rev})=a(\pi).
\]

A natural first label is therefore the ordered pair
\[
q(\pi)=\bigl(a(\pi),\bar b(\pi)\bigr).
\]
Adjacent transpositions change only a bounded neighborhood of the status word. In particular, away from singular cases the two coordinates behave like a rook move: one coordinate is retained while the other changes locally.

This was the source of the Tucker and Ky Fan attempts.

### Why graph-level Tucker is insufficient

The temptation is to seek a theorem saying that an antipodal rook labeling of the permutahedron graph must contain a complementary edge or a diagonal label. That statement is false in this generality.

Indeed, for a permutation
\[
\pi=(v_1,\ldots,v_n)
\]
consider the purely combinatorial label
\[
Q(\pi)=(v_1,v_n).
\]
Reversal swaps the two coordinates:
\[
Q(\pi^{\rm rev})=(v_n,v_1).
\]
An adjacent transposition either occurs internally, leaving \(Q\) unchanged, or touches one endpoint and changes only one coordinate. Thus adjacent labels share a coordinate exactly as a rook condition would require.

Therefore antipodality plus rook adjacency on the \(1\)-skeleton is not enough to force a contradiction.

The same lesson persists for signed variants. One can build antipodal signed labels with very few magnitudes that avoid complementary labels on every permutahedron edge. Any successful Tucker argument must therefore use higher-dimensional consistency, not merely the graph.

This negative result is worth preserving. It explains why the later cellular topology is necessary.

### Tucker and Ky Fan as guides

A Tucker-style conclusion would ideally produce two compatible chambers carrying complementary extreme data. A Ky Fan-style conclusion would be stronger: an alternating simplex or chain could carry several coordinated switch-front witnesses at once.

The difficulty is not the absence of powerful antipodal theorems. The difficulty is representing the chamber data on a dimension-correct antipodal triangulation while preserving the positional meaning of the labels.

A naive triangulation of the permutahedron introduces diagonals between chambers that need not differ by adjacent transpositions. The local status word can then change in ways not controlled by the rook calculation. Conversely, a labeling confined to chamber vertices remembers the correct local swaps but does not satisfy the hypotheses of the simplicial theorem.

This is the reason Tucker and Ky Fan remain in the article as diagnostic tools rather than claimed closure theorems.

### Rank-two cells: squares and hexagons

The Coxeter complex supplies a canonical cellular repair.

Two independent adjacent transpositions commute. Their four chambers form a square. Adjacent transpositions at neighboring positions satisfy the braid relation
\[
s_is_{i+1}s_i=s_{i+1}s_is_{i+1},
\]
and their six chambers form a hexagon.

These are the rank-two cells controlling all local ambiguity in the chamber graph.

These rank-two cells describe the local relations of adjacent swaps. A proposed graph-level extension must check what the actual status labels do on these cells; their combinatorial shape alone does not prove that every square is harmless or that every exceptional hexagon produces a directed root cycle.

The explicit barycentric extension in the next Section avoids this extension problem: it averages all chamber roots on every face and is defined on all nested face chains. Squares and hexagons remain useful for local combinatorial analysis, but no unproved assertion about their label patterns is needed to define the odd map.

### The extreme-switch root

Replace the ordered pair \(q(\pi)\) by the vector
\[
\phi(\pi)
=
e_{a(\pi)}-e_{\bar b(\pi)}.
\]
This vector lies in the type-\(A\) root space. Reversal is odd:
\[
\phi(\pi^{\rm rev})
=
-\phi(\pi).
\]

The vector is zero exactly at an exact diagonal
\[
a(\pi)=\bar b(\pi).
\]
Otherwise it is an oriented edge of the complete directed graph on the switch-coordinate set.

The root has two advantages over the rook pair.

First, convex combinations make sense. A family of chamber labels may balance at the origin even when no single chamber is diagonal.

Second, the rank-two cellular relations become algebraic relations among roots. A square expresses commuting local changes; an exceptional braid hexagon can support a directed root cycle.

This is the point at which the topology stops asking for one complementary edge and starts asking for **balanced recurrence**.

### From the Helly witnesses to the root

The root coordinates should be read back through the first Section.

The exact two-cover obstruction is a family of defect intervals. The root discards almost all of that family and remembers only the first and reflected-last switch fronts. It is therefore a topological compression of the Helly failure.

This compression is useful because it produces an odd map into a linear representation. It is dangerous because a zero of the compressed data need not itself be the exact two-cover state.

The rest of Article VII is devoted to that gap:
\[
\text{topological balance of extreme witnesses}
\quad\Longrightarrow?\quad
\text{exact combinatorial intersection}.
\]

### Ky Fan forces a hole-sweeping face

### Ky Fan forces a hole-sweeping face

Assume
\[
k=\kappa_2(H)\ge2.
\]
For a proper permutahedron face \(F\), call an actual vertex \(v\in V(H)\)

- **uniformly positive on \(F\)** if \(v\in P_\pi\) for every chamber \(\pi\in\mathcal V(F)\);
- **uniformly negative on \(F\)** if \(v\in Q_\pi\) for every chamber \(\pi\in\mathcal V(F)\).

Uniformity is inherited by subfaces. Reversal exchanges the two signs.

**Theorem 5.1 (hole-sweeping face).** There exists a proper permutahedron face \(F\) having no uniformly positive and no uniformly negative actual vertex. Consequently, for every \(v\in V(H)\), some chamber \(\pi\in\mathcal V(F)\) has
\[
v\in X_\pi.
\]

**Proof.** Suppose every proper face has a uniformly signed actual vertex. Fix an arbitrary total order of \(V(H)\). Label the barycentric-subdivision vertex corresponding to \(F\) by the least actual vertex that is uniformly signed on \(F\), with sign \(+\) or \(-\) according to its uniform role.

This is an antipodal labeling: the candidate set is unchanged by reversal and every sign is reversed. Moreover a barycentric edge joins nested faces \(F\subset G\), and its endpoint labels cannot be complementary in one absolute label. Indeed, if \(v\) is uniformly positive on \(F\) and uniformly negative on \(G\), then uniform negativity on \(G\) is inherited by \(F\), impossible. The other orientation is symmetric.

The barycentric subdivision of the boundary of the \((n-1)\)-dimensional permutahedron is an antipodal triangulation of \(S^{n-2}\). Ky Fan's lemma therefore gives a top-dimensional simplex whose \(n-1\) labels have distinct absolute values. Such a simplex is a maximal chain
\[
F_0\subsetneq F_1\subsetneq\cdots\subsetneq F_{n-2}
\]
of proper faces. The bottom face \(F_0\) is one chamber \(\pi\). Every sign attached to a larger face is inherited by this chamber. Hence \(n-1\) distinct actual vertices of \(H\) lie in \(P_\pi\cup Q_\pi\). Therefore
\[
|X_\pi|\le1,
\]
contradicting
\[
|X_\pi|=\delta(\pi)\ge\kappa_2(H)=k\ge2.
\]
Thus some proper face \(F\) has no uniformly signed vertex.

Now fix \(v\in V(H)\). If \(v\) never belonged to \(X_\pi\) on this face, then it would take only the roles \(P\) and \(Q\). The chamber graph of a permutahedron face is connected. By the no-direct-side-flip lemma of [[spanning_orders_and_defect_helly]], one adjacent transposition cannot change \(v\) directly from \(P\) to \(Q\) or conversely. Hence its role would be constant on the whole face, making \(v\) uniformly signed, a contradiction. Therefore \(v\) occurs in the exact hole in some chamber of \(F\). \(\square\)

Call such an \(F\) a **hole-sweeping face**. Its significance is global: one fixed ordered-partition face supports canonical partial two-covers whose holes collectively sweep the entire vertex set.

Two immediate consequences are worth recording. The first face block has order at least three, because the first two positions of every chamber always lie in \(P_\pi\); a block of order at most two would make one of its vertices uniformly positive. Symmetrically the last face block has order at least three.

This theorem supplies the higher-dimensional consistency missing from the earlier graph-level Tucker attempt. The labels are actual vertices rather than switch positions, the exact deletion gap \(k\ge2\) forbids complementary labels across chamber edges, and Ky Fan forces failure of uniform signed labeling on one genuine permutahedral face.

---

## Section — Convex root balance and Bourgin–Yang multiplicity

<!-- section_id: convex_root_balance_and_bourgin_yang -->

### Balance, circulation, and multiplicity of zeros

### Convex balance is directed circulation

Let \(I\) be a finite coordinate set and let
\[
E\subseteq I\times I
\]
be a directed graph, allowing loops and regarding a loop as a cycle of length one. Set \(\operatorname{conv}(\varnothing)=\varnothing\). Associate to an arc \(i\to j\) the type-\(A\) root
\[
\rho_{ij}=e_i-e_j.
\]

**Proposition 4 (root-balance criterion).**
\[
\boxed{
0\in\operatorname{conv}\{\rho_{ij}:(i,j)\in E\}
\iff
E\text{ contains a directed cycle}.
}
\]

**Proof.** If
\[
i_1\to i_2\to\cdots\to i_k\to i_1
\]
is a directed cycle, then
\[
\sum_{\ell=1}^k
(e_{i_\ell}-e_{i_{\ell+1}})
=
0,
\]
so the origin lies in the convex hull after dividing by \(k\).

Conversely, suppose
\[
\sum_{(i,j)\in E}\lambda_{ij}(e_i-e_j)=0,
\qquad
\lambda_{ij}\ge0,
\qquad
\sum\lambda_{ij}=1.
\]
The coefficients form a nonzero nonnegative circulation: at every coordinate, total outgoing weight equals total incoming weight. Any finite nonzero circulation contains a directed cycle. \(\square\)

Thus a convex zero of the extreme-switch root map is not merely an analytic event. It is a finite directed recurrence among switch-front coordinates.

### Balanced faces of the Coxeter complex

A face of the permutahedron is an ordered partition
\[
B_1|\cdots|B_k.
\]
Its chamber vertices are the permutations obtained by ordering the vertices inside each block while retaining the block order.

Suppose a set of chambers in one such face has root labels whose convex hull contains the origin. By Proposition 4, after discarding zero coefficients the support contains a directed switch-front cycle
\[
x_1\to x_2\to\cdots\to x_t\to x_1.
\]

This is the basic combinatorial output of root topology.

The converse viewpoint is equally useful: a directed cycle is already a balanced convex configuration. Hence later arguments can work directly with a finite cycle rather than with a continuous map once a balanced face has been obtained.

### Borsuk–Ulam as the baseline

Let \(S^d\) be the antipodal Coxeter sphere or an antipodal subdivision of it. An odd continuous map
\[
f:S^d\to\mathbb R^q
\]
satisfies
\[
f(-x)=-f(x).
\]

When \(q\le d\), the Borsuk–Ulam theorem forces
\[
f^{-1}(0)\ne\varnothing.
\]

For the root program, one constructs such a map by assigning root data to chambers or face barycenters and extending over an antipodal cellular or barycentric subdivision. A zero means that the root labels of one carrier face balance at the origin.

This is already stronger than seeking a complementary edge on the chamber graph: a zero may be supported by several chambers around a cell.

But ordinary Borsuk–Ulam says only that at least one zero exists. The later program needed multiplicity.

### The Bourgin–Yang strengthening

We use the standard Bourgin–Yang dimension principle in the following form.

**Theorem 5 (Bourgin–Yang, dimension form).** Let
\[
f:S^d\to\mathbb R^q
\]
be continuous and odd, with \(q\le d\). Then the zero set
\[
Z=f^{-1}(0)
\]
has topological dimension at least
\[
d-q.
\]

The relevant feature is the lower bound on the **whole zero locus**, not merely nonemptiness.

Consequently, whenever the GN3 root construction is shown to take values in a \(q\)-dimensional linear subspace of a \(d\)-dimensional antipodal sphere, one obtains
\[
\dim Z\ge d-q.
\]

This is the rigorous span–multiplicity principle needed here. Any more specific numerical statement must come from a separately proved bound on \(q\).

### Switch span and dimension saving

Large first-to-last switch separation can force many root coordinates to be absent from the image. This is the source of the dimension saving contemplated in the brainstorm work.

The logical chain must be kept explicit:

1. prove a coordinate-subspace bound
   \[
   \phi(\mathcal C)\subseteq W,
   \qquad
   \dim W=q;
   \]
2. construct the odd continuous root map
   \[
   f:S^d\to W;
   \]
3. apply Bourgin–Yang to obtain
   \[
   \dim f^{-1}(0)\ge d-q;
   \]
4. separately convert this zero-set dimension into a statement about balanced faces or independent root circulations.

The next subsection supplies an explicit equivariant extension and a precise switch-span bound. The zero-set bound must still be distinguished from any assertion about the number of independent directed cycles.

### Why multiplicity matters

One balanced face may be accidental. A positive-dimensional balanced locus is qualitatively different.

A positive-dimensional zero set contains a family of balanced points. This does not by itself force multiple independent switch-front cycles, or even different cycle supports: many convex representations can use the same roots. Converting topological dimension into distinct combinatorial recurrences requires an additional argument.

That is the point at which topology becomes potentially useful to Articles III–VI. Those articles are strong at converting **repeated local obstruction** into:

- endpoint reversals;
- common carriers;
- parallel middles;
- bounded Hamiltonian supports;
- strict potential descent.

Bourgin–Yang is therefore not a replacement for the GN3 machinery. Its intended role is to supply enough recurrence for that machinery to act.

### The remaining conversion problem

Root balance and the exact theorem still live at different levels.

A balanced root face says that a convex combination of compressed extreme-defect vectors vanishes. It does not yet say that one actual spanning order has intersecting defect intervals, nor that one actual state lies in both reachability regions of the exactified memory lift.

The next Section records the strongest combinatorial consequences that can be extracted from a balanced face before invoking the GN3-specific local structure.


### Positive balance on every chamber and the switch-separation bound

### Explicit odd root maps and positive carrier balance

Assume \(H\) has no spanning two-cover and put \(m=n-2\).

For the extreme-switch coordinates \(a(\pi)<b(\pi)\), put
\[
\bar b(\pi)=m-b(\pi),\qquad
\phi(\pi)=e_{a(\pi)}-e_{\bar b(\pi)}.
\]
Reversal gives
\[
\phi(\pi^{\rm rev})=-\phi(\pi).
\]

Realize the centered permutahedron \(P\) equivariantly, and for every nonempty proper face \(F\) assign its barycenter the average of \(\phi\) over the permutation vertices of \(F\). Extend affinely on the barycentric subdivision.

**Theorem 6.1 (positive carrier balance).** The resulting map
\[
\Phi:\partial P\cong S^{n-2}\to\mathbb R^m
\]
is continuous and odd. For every zero \(x\), if \(F\) is the unique face whose relative interior contains \(x\), there are
\[
\lambda_\pi>0\quad(\pi\in\mathcal V(F)),\qquad \sum_\pi\lambda_\pi=1,
\]
with
\[
\sum_\pi\lambda_\pi\phi(\pi)=0.
\]
After grouping equal roots, these coefficients form a strictly positive circulation, so every occurring root lies on a directed return cycle.

The proof is the standard smallest-barycentric-simplex expansion: the top face of the chain contributes positive weight to every chamber of \(F\).

**Theorem 6.2 (switch-separation multiplicity).** If every spanning order satisfies
\[
b(\pi)-a(\pi)\ge L\ge1,
\]
then
\[
\dim\Phi^{-1}(0)\ge L+2.
\]
Indeed
\[
a+\bar b=m-(b-a)\le m-L,
\]
so every root lies in the sum-zero subspace on coordinates
\[
1,\ldots,m-L-1,
\]
of dimension \(n-L-4\); Bourgin--Yang gives the result. The target rank can be sharpened to the rank of the undirected support graph of the occurring roots.

**Proposition 6.3.** In a genuine counterexample,
\[
b(\pi)-a(\pi)\ge3
\]
for every spanning order. If the first-to-last switch span were at most two, a cut immediately after the short middle run would split the order into two monochromatic blocks, each of which has a tight orientation. Hence
\[
\dim\Phi^{-1}(0)\ge5.
\]

### Exact inversion roots

For a spanning order \(\pi\), define
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
and
\[
c(\pi)=m+1-q(\pi),\qquad
\delta(\pi)=q(\pi)-p(\pi)-1=m-p(\pi)-c(\pi).
\]
The exact inversion-window criterion in [[spanning_orders_and_defect_helly]] gives
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi:\delta(\pi)\le0.
\]

Define
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}.
\]
Reversal exchanges \(p\) and \(c\), so
\[
\psi(\pi^{\rm rev})=-\psi(\pi).
\]

Use the same barycentric face-average extension.

**Theorem 6.4 (positive exact-root balance).** The resulting odd map
\[
\Psi:\partial P\to\mathbb R^m
\]
has a zero whose carrier face \(F\) admits strictly positive coefficients on every chamber:
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi\psi(\pi)=0,
\qquad \lambda_\pi>0.
\]
Thus every occurring exact root lies on a directed cycle of exact roots in \(F\).

**Theorem 6.5 (exact-deficiency multiplicity).** If
\[
\delta(\pi)\ge D\ge1
\]
for every spanning order, then
\[
\dim\Psi^{-1}(0)\ge D+2.
\]
Indeed
\[
p+c\le m-D,
\]
so the image lies in the sum-zero subspace on
\[
1,\ldots,m-D-1,
\]
of dimension \(n-D-4\).

By the deletion-distance identity,
\[
\kappa_2(H)=\min_\pi\max\{0,\delta(\pi)\}.
\]
Hence, writing
\[
k=\kappa_2(H)>0,
\]
one has
\[
\dim\Psi^{-1}(0)\ge k+2.
\]

### Canonical partial two-covers

For a chamber \(\pi=(v_1,\ldots,v_n)\) with positive deficiency, define
\[
P_\pi=(v_1,\ldots,v_{p+1}),
\qquad
Q_\pi=(v_n,v_{n-1},\ldots,v_{q+1}),
\]
and
\[
X_\pi=\{v_{p+2},\ldots,v_q\}.
\]
Then \(P_\pi,Q_\pi\) are tight, disjoint, and
\[
|P_\pi|=p+1,\qquad
|Q_\pi|=c+1,\qquad
|X_\pi|=\delta.
\]
Thus
\[
n=(p+1)+(c+1)+\delta.
\]

So the exact root records a partial two-cover:
\[
\boxed{\psi=e_p-e_c
\quad\Longleftrightarrow\quad
P_\pi\mid X_\pi\mid Q_\pi.}
\]
Its anti-diagonal deficit is literally the hole size.

At deficiency one, \(X_\pi=\{x\}\), and
\[
(x,v_{p+1},v_p),\qquad
(x,v_{q+1},v_{q+2})
\]
are tight. Thus the unique hole vertex reverses the exposed terminal edge of both canonical paths.

### Minimum-hole faces

Let \(X\) be a minimum deletion set,
\[
|X|=k=\kappa_2(H),
\qquad
H-X=P\mid Q,
\]
with \(|P|=r\), \(|Q|=s\). For every ordering \(\sigma\) of \(X\),
\[
\pi_\sigma=(P,\sigma,Q^{\rm rev})
\]
has exact deficiency at most \(k\), hence exactly \(k\). Therefore
\[
p(\pi_\sigma)=r-1,\qquad
q(\pi_\sigma)=r+k,\qquad
c(\pi_\sigma)=s-1
\]
for every \(\sigma\).

Consequently the entire \((k-1)\)-dimensional face obtained by freely permuting \(X\) has constant exact root
\[
e_{r-1}-e_{s-1}.
\]

In particular every \(x\in X\) may be placed first or last in the hole, forcing
\[
(x,p_r,p_{r-1}),
\qquad
(x,q_s,q_{s-1})
\]
tight. Thus a minimum hole is a synchronized family of common reversers of the same two exposed terminal edges. This uses only minimum deletion distance inside the fixed graph, not minimum-counterexample induction.

### High-dimensional exact carriers

Because \(\Psi^{-1}(0)\) is a finite polyhedral complex of dimension at least \(k+2\), some zero lies in a cell of dimension at least \(k+2\).

**Proposition 6.6.** There is a zero whose carrier face \(F\) satisfies
\[
\dim F\ge k+2
\]
and has strictly positive exact-root balance on every chamber.

### Exact determining-window splice

The condition \(p=r\) is determined by positions
\[
1,\ldots,r+2,
\]
while \(c=r\) is determined by positions
\[
n-1-r,\ldots,n.
\]

**Lemma 6.7 (exact face splice).** Suppose a permutahedron face \(F\) contains a chamber with \(p=r\), a chamber with \(c=r\), and has a block boundary after a position \(j\) satisfying
\[
r+2\le j\le n-r-2.
\]
Then \(F\) contains a chamber with
\[
p=c=r.
\]
Take block orders from the \(p=r\) witness through that boundary and from the \(c=r\) witness afterward; the two determining windows are preserved.

### Balanced hole or a large free corridor

Let \(F\) have positive exact-root balance, and let
\[
s=\min\{p(\pi),c(\pi):\pi\in\mathcal V(F)\}.
\]
Positive circulation supplies both a \(p=s\) witness and a \(c=s\) witness.

**Corollary 6.8.** At least one of the following holds.

1. \(F\) contains a zero exact root \(p=c=r\), hence a canonical partial two-cover with equal path orders and hole size
   \[
   m-2r\ge k.
   \]

2. One block of \(F\) contains every position
   \[
   s+2,\ldots,n-1-s.
   \]
   The guaranteed central corridor has length
   \[
   L:=m-2s.
   \]
   If no zero root occurs, an arc \(s\to t\) with \(t>s\) occurs, and
   \[
   L
   =\delta+(t-s)
   \ge k+1.
   \]

Thus a nonzero recurrent branch contains a freely permutable central corridor longer than a minimum hole.

### Independent internal status bits

**Lemma 6.9.** Let \(F\) be a permutahedron face. Choose pairwise disjoint three-position windows, each wholly inside a single face block. As the chamber ranges uniformly over \(\mathcal V(F)\), the corresponding status signs are uniform on the full cube
\[
\{-1,+1\}^t.
\]

For each selected window, swap its first and third positions. The swaps are disjoint and commute; each flips exactly its selected status by boundary antisymmetry.

Hence any face block of order \(b\) contains an independently flippable status cube of dimension at least
\[
\left\lfloor b/3\right\rfloor.
\]

### Guardrail on the central block size

The proved conclusion is that one block **contains** the \(L=m-2s\) central corridor. It does not by itself imply
\[
|B|=m-2s.
\]
Therefore any refinement using equality of the whole block size with the corridor length requires an additional argument.

In particular, the earlier draft of a “unique bottleneck vertex / exact \(+3\) surplus block” used that equality without proof. That refinement is not retained here. A repaired version must work with the actual determining positions inside the containing block, which may extend beyond the corridor.

### Anchored three-state balance

Fix an actual vertex \(z\). For every chamber, write
\[
P_\pi\mid X_\pi\mid Q_\pi.
\]
Define
\[
\omega_z(\pi)=
\begin{cases}
 |X_\pi|^{-1}{\bf1}_{X_\pi}-|Q_\pi|^{-1}{\bf1}_{Q_\pi},
   &z\in P_\pi,\\
 |Q_\pi|^{-1}{\bf1}_{Q_\pi}-|P_\pi|^{-1}{\bf1}_{P_\pi},
   &z\in X_\pi,\\
 |P_\pi|^{-1}{\bf1}_{P_\pi}-|X_\pi|^{-1}{\bf1}_{X_\pi},
   &z\in Q_\pi.
\end{cases}
\]
This lies in
\[
W_z=\{x:\sum_vx_v=0,\ x_z=0\},
\qquad \dim W_z=n-2,
\]
and reversal negates it.

Averaging on face barycenters and extending affinely gives an odd map
\[
\Omega_z:S^{n-2}\to W_z.
\]

**Theorem 6.10 (anchored three-state balance).** \(\Omega_z\) has a zero with strictly positive carrier weights on every chamber.

Each chamber vector is the divergence of a complete bipartite role transport:
\[
Q_\pi\to X_\pi \ (z\in P_\pi),\qquad
P_\pi\to Q_\pi \ (z\in X_\pi),\qquad
X_\pi\to P_\pi \ (z\in Q_\pi).
\]
At a zero these transports form a nonzero circulation on \(V(H)-\{z\}\), so every contributed actual-vertex arc lies on a directed role-transfer cycle.

### Uniform-anchor terminal block collapse

Let
\[
F=B_1|\cdots|B_t
\]
be an anchored carrier face with positive role-transfer circulation.

**Proposition 6.11.**

- If \(z\in P_\pi\) for every chamber, then
  \[
  X_\pi\cup Q_\pi\subseteq B_t
  \]
  for every chamber.

- If \(z\in Q_\pi\) for every chamber, then
  \[
  P_\pi\cup X_\pi\subseteq B_1
  \]
  for every chamber.

- The role \(z\in X_\pi\) cannot be uniform on a proper carrier face.

For the first case all transport arcs are \(Q\to X\). Face-block index is nonincreasing along every such arc, but every arc lies on a directed cycle, so block index is constant along every arc. Complete bipartite transport forces \(Q\cup X\) into one block, necessarily the final block. The other cases are symmetric.

Hence a uniform side role forces a terminal block of order at least
\[
k+2,
\]
while a nonuniform anchor enters the hole somewhere once \(k\ge2\).

### Canonical side labels cannot flip in one adjacent swap

Assume
\[
k=\kappa_2(H)\ge2.
\]
Give each actual vertex its role
\[
+\ (P),\qquad 0\ (X),\qquad -\ (Q).
\]

**Lemma 6.12 (no direct side flip).** One adjacent transposition cannot move any actual vertex directly from \(+\) to \(-\) or conversely.

An adjacent transposition changes only four consecutive status positions, a set of diameter at most three. If a vertex at position \(t\) changed from \(P\) to \(Q\), then the old last-one coordinate \(q\) and the new first-zero coordinate \(p'\) would both have to lie in that four-position set. But the two deficiency inequalities give
\[
q-p'\ge2k+1\ge5,
\]
a contradiction.

Thus roles change along the chamber graph only through
\[
+\longleftrightarrow0\longleftrightarrow-.
\]

### Multi-anchor role balance

For \(S\subseteq V(H)\), define
\[
\rho_S(\pi)=(\rho_z(\pi))_{z\in S},
\qquad
\rho_z=
\begin{cases}
+1,&z\in P,\\
0,&z\in X,\\
-1,&z\in Q.
\end{cases}
\]
Reversal negates \(\rho_S\). Average on face barycenters and extend affinely.

**Theorem 6.13 (multi-anchor balance).** For every
\[
1\le |S|=t\le n-2,
\]
the zero set has dimension at least
\[
n-2-t.
\]
Hence there is a carrier face \(F\) with
\[
\dim F\ge n-2-t,
\qquad
\#\{\text{blocks of }F\}\le t+2,
\]
such that every anchor \(z\in S\) enters a canonical hole in some chamber of \(F\). More precisely, either \(z\) is in the hole in every chamber, or all three roles \(P,X,Q\) occur for \(z\).

The last assertion uses positive carrier weights and the no-direct-side-flip lemma.

### Octahedral unanimity collapse

Assume again \(k\ge2\). For every nonempty proper face \(F\), define
\[
A(F)=\bigcap_{\pi\in\mathcal V(F)}P_\pi,
\qquad
B(F)=\bigcap_{\pi\in\mathcal V(F)}Q_\pi.
\]
Then
\[
|A(F)|+|B(F)|\le n-k,
\]
and reversal exchanges \(A\) and \(B\).

**Theorem 6.14 (unanimity collapse).** There is a nonempty proper face \(F\) with
\[
A(F)=B(F)=\varnothing.
\]

If not, \(F\mapsto(A(F),B(F))\) gives an antipodal simplicial map from the barycentric subdivision of the permutahedron boundary to the barycentric subdivision of the \((n-k-1)\)-skeleton of the \(n\)-cross-polytope boundary. Any free antipodal complex of dimension \(r\) maps equivariantly to \(S^r\) by a generic antipodal linear realization. Therefore one would obtain
\[
S^{n-2}\to S^{n-k-1}
\]
equivariantly, impossible for \(k\ge2\).

**Corollary 6.15 (universal hole carrier).** There is one nonempty proper face \(F\) such that for every actual vertex
\[
v\in V(H)
\]
some chamber of \(F\) has
\[
v\in X_\pi.
\]

Indeed \(A(F)=B(F)=\varnothing\). If a vertex never entered a hole, it would take both side roles somewhere in the connected chamber graph of \(F\), forcing a forbidden direct side flip along an adjacent-transposition path.

Thus a hypothetical graph with
\[
\kappa_2(H)\ge2
\]
has a single proper ordered-partition face through whose exact holes **every vertex of \(H\) can pass**. This is the strongest current Tucker-type structural output and uses neither minimum-counterexample induction nor path disturbance.

### Spending the exact topological surplus on actual vertices

Let
\[
k=\kappa_2(H)\ge2.
\]
The exact-root map has a built-in dimension saving of \(k+2\): every exact root uses coordinates
\[
I_k=\{1,\ldots,m-k-1\},
\]
so its span has dimension
\[
|I_k|-1=n-k-4.
\]
This leaves exactly \(k+2\) dimensions before reaching the sphere dimension \(n-2\).

Fix any prescribed set
\[
S\subseteq V(H),\qquad |S|=k+2,
\]
and for \(z\in S\) let
\[
\rho_z(\pi)=
\begin{cases}
+1,&z\in P_\pi,\\
0,&z\in X_\pi,\\
-1,&z\in Q_\pi.
\end{cases}
\]
Consider the direct-sum chamber label
\[
\Theta_S(\pi)
=
\bigl(\psi(\pi),(\rho_z(\pi))_{z\in S}\bigr).
\]
Average this label on every proper face barycenter and extend over the barycentric subdivision. Reversal negates both parts. The target dimension is
\[
(n-k-4)+(k+2)=n-2.
\]

**Theorem (exact-root balance with \(k+2\) prescribed role anchors).**
For every \(S\subseteq V(H)\) of order \(k+2\), there is a proper permutahedron face \(F\) and coefficients
\[
\lambda_\pi>0\quad(\pi\in\mathcal V(F)),\qquad
\sum_\pi\lambda_\pi=1,
\]
such that simultaneously
\[
\sum_\pi\lambda_\pi\psi(\pi)=0
\]
and
\[
\sum_\pi\lambda_\pi\rho_z(\pi)=0
\qquad(z\in S).
\]
Consequently every prescribed anchor \(z\in S\) occurs in the exact hole of some chamber of \(F\).

Moreover, at least one of the following holds.

1. \(F\) contains a chamber with zero exact root
   \[
   p=c=r,
   \]
   hence an equal-side canonical partial two-cover with hole size
   \[
   m-2r\ge k.
   \]

2. There is one block \(B\) of \(F\) containing all of \(S\) and containing the complete central corridor
   \[
   s+2,\ldots,n-1-s,
   \]
   where \(s\) is the least coordinate occurring as a tail or head of an exact root on \(F\).

**Proof.** Borsuk--Ulam applied to the direct-sum odd map gives a zero. Expanding that zero through its smallest barycentric face chain gives strictly positive weight to every chamber of the top carrier face \(F\), exactly as for the previous root maps.

Fix \(z\in S\). Its weighted role average is zero. If all chamber roles of \(z\) are zero, then \(z\) is already in every hole. Otherwise both signs \(+1\) and \(-1\) must occur because all coefficients are positive. The chamber graph of \(F\) is connected, and when \(k\ge2\) the no-direct-side-flip lemma forbids an adjacent \(P\leftrightarrow Q\) transition. Hence a path between the two signs passes through role zero. Thus \(z\) enters some canonical hole.

Now use the positive exact-root balance. If a zero exact root occurs, we are in (1). Otherwise let \(s\) be the least occurring exact coordinate. Positive circulation supplies both a \(p=s\) witness and a \(c=s\) witness. Exact determining-window splicing shows that no face-block boundary can lie between positions
\[
s+2\quad\text{and}\quad n-s-2;
\]
hence one block \(B\) contains the whole displayed central corridor.

Every block strictly before \(B\) lies entirely among the first \(s+1\) positions. Since every chamber has \(p\ge s\), all of its vertices lie in \(P_\pi\) for every chamber and are uniformly positive. Similarly every block strictly after \(B\) is uniformly negative because every chamber has \(c\ge s\). A prescribed anchor \(z\in S\) has weighted role average zero, so it cannot lie in a uniformly positive or uniformly negative block. Therefore
\[
S\subseteq B.
\]
This proves (2). \(\square\)

Thus the full Bourgin--Yang surplus has a concrete meaning: it can be spent to force **any chosen \(k+2\) actual vertices** to participate in role balance on the very same exact-root carrier. Unless an equal-side exact hole appears, all \(k+2\) prescribed vertices are trapped in one freely permutable central block.

### The universal-hole locus has dimension at least \(k-2\)

Continue to assume
\[
k=\kappa_2(H)\ge2.
\]
Call a nonempty proper permutahedron face \(F\) **unanimity-free** if
\[
A(F)=B(F)=\varnothing.
\]
By Corollary 6.15, every unanimity-free face is a universal-hole carrier.

Unanimity-free faces form an upper order ideal:
\[
F\subseteq G,\quad A(F)=B(F)=\varnothing
\quad\Longrightarrow\quad
A(G)=B(G)=\varnothing,
\]
because unanimous side sets can only shrink when a face is enlarged.

Let \(K\) be the \((n-k-1)\)-skeleton of the \(n\)-cross-polytope boundary. Choose an equivariant generic linear realization
\[
g:|\operatorname{sd}K|\longrightarrow \mathbb R^{\,n-k}\setminus\{0\}
\]
such that the convex hull of the images of the vertices of every simplex avoids the origin.

Define a PL map \(U\) on the barycentric subdivision of the permutahedron boundary as follows. At the vertex corresponding to a face \(F\),
\[
U(z_F)=
\begin{cases}
g(A(F),B(F)),&A(F)\cup B(F)\ne\varnothing,\\
0,&A(F)=B(F)=\varnothing.
\end{cases}
\]
Extend affinely over face chains. Reversal negates \(U\).

In a chain
\[
F_0\subsetneq\cdots\subsetneq F_t,
\]
the nonempty unanimous labels form an initial segment, because emptiness is upward closed; those nonempty signed faces are nested, so their \(g\)-images lie in one simplex of \(\operatorname{sd}K\), whose convex hull avoids zero. It follows that an affine point of the chain maps to zero exactly when all its positive barycentric weight is supported on unanimity-free faces.

Therefore
\[
U^{-1}(0)
\]
is precisely the order complex of the unanimity-free proper faces.

**Theorem 6.16 (dimension of the universal-hole locus).**
\[
\boxed{\dim U^{-1}(0)\ge k-2.}
\]

**Proof.** The map
\[
U:S^{n-2}\to\mathbb R^{n-k}
\]
is continuous and odd. Bourgin--Yang gives
\[
\dim U^{-1}(0)
\ge
(n-2)-(n-k)
=
k-2.
\]
\(\square\)

Hence there is a chain of at least \(k-1\) nested unanimity-free faces,
\[
F_0\subsetneq F_1\subsetneq\cdots\subsetneq F_{k-2}.
\]
Every \(F_i\) is a universal-hole carrier: every actual vertex of \(H\) enters the exact hole in some chamber of that same face.

Because strict inclusion of permutahedron faces coarsens the ordered partition and decreases the number of blocks by at least one, the smallest face in such a chain has at least \(k\) ordered blocks. Thus a hypothetical obstruction with deletion distance \(k\ge2\) forces not merely one universal-hole carrier but a positive-dimensional nested family of them.

### The normalized side-balance map has odd degree

The two canonical tight paths themselves define a global map with no zeros.

For every chamber put
\[
u(\pi)
=
\frac{{\bf1}_{P_\pi}}{|P_\pi|}
-
\frac{{\bf1}_{Q_\pi}}{|Q_\pi|}.
\]
This lies in the sum-zero subspace
\[
W=\{x\in\mathbb R^{V(H)}:\sum_vx_v=0\},
\qquad \dim W=n-1,
\]
and reversal exchanges \(P_\pi,Q_\pi\), so
\[
u(\pi^{\rm rev})=-u(\pi).
\]
Average \(u\) on every proper face barycenter and extend affinely over the barycentric subdivision; call the resulting odd map
\[
U:\partial P\cong S^{n-2}\longrightarrow W.
\]

**Theorem (nonvanishing side balance).**
The map \(U\) never vanishes.

**Proof.** Suppose \(U(x)=0\), and let
\[
F=B_1|\cdots|B_t
\]
be the carrier face of \(x\). The usual carrier expansion gives strictly positive coefficients \(\lambda_\pi\) on every chamber of \(F\) with
\[
\sum_\pi\lambda_\pi u(\pi)=0.
\]
Interpret each \(u(\pi)\) as the divergence of unit complete-bipartite flow
\[
Q_\pi\longrightarrow P_\pi,
\]
putting weight \(1/(|P_\pi||Q_\pi|)\) on every arc \(q\to p\). The weighted sum is a nonzero circulation, so every contributed arc lies on a directed cycle.

Let \(\beta(v)\) be the face-block index of \(v\). Every \(P_\pi\)-vertex precedes every \(Q_\pi\)-vertex, hence every arc \(q\to p\) satisfies
\[
\beta(q)\ge\beta(p).
\]
A nonincreasing integer potential must be constant around a directed cycle. Thus every contributed arc has equal block indices at its ends. Since each chamber contribution is complete bipartite, all vertices of \(P_\pi\cup Q_\pi\) lie in one block.

But \(P_\pi\) contains the first chamber vertex, in \(B_1\), and \(Q_\pi\) contains the last chamber vertex, in \(B_t\). Hence
\[
B_1=B_t,
\]
so \(t=1\), contradicting that a carrier face on the boundary of the permutahedron is proper. \(\square\)

Therefore
\[
\widehat U(x)=\frac{U(x)}{\|U(x)\|}
\]
is a continuous odd self-map
\[
\widehat U:S^{n-2}\longrightarrow S(W)\cong S^{n-2}.
\]
Every odd self-map of a sphere has odd degree. In particular \(\widehat U\) is surjective.

### Prescribed source--sink side balance

Fix distinct actual vertices \(a,b\). By surjectivity, some point has
\[
\widehat U(x)
=
\frac{e_a-e_b}{\sqrt2}.
\]
For its carrier face \(F\) there are positive chamber weights and a scalar \(\tau>0\) such that
\[
\sum_\pi\lambda_\pi u(\pi)
=
\tau(e_a-e_b).
\]
Equivalently, the associated positive \(Q\to P\) flow has net divergence \(+\tau\) at \(a\), \(-\tau\) at \(b\), and zero at every other actual vertex.

Let
\[
F=B_1|\cdots|B_t.
\]
For every cut after block \(B_j\), all flow crossing the cut goes from the suffix to the prefix. Hence the total divergence of the prefix is nonnegative and equals
\[
\tau\bigl({\bf1}_{a\in B_1\cup\cdots\cup B_j}
-
{\bf1}_{b\in B_1\cup\cdots\cup B_j}\bigr).
\]
Because every chamber has a \(P\)-vertex in \(B_1\) and a \(Q\)-vertex in \(B_t\), positive flow crosses every proper face-block cut. It follows that
\[
a\in B_1,
\qquad
b\in B_t.
\]

If \(k=\kappa_2(H)\ge2\), then for every other vertex
\[
v\notin\{a,b\}
\]
the weighted \(v\)-coordinate is zero. Either \(v\) is in the hole in every chamber, or it occurs on both path sides; in the latter case connectedness of the chamber graph and the no-direct-side-flip lemma force a hole occurrence between the two side roles. Thus:

**Corollary (two-exception hole-sweeping carrier).**
For every ordered pair of distinct vertices \((a,b)\) in a hypothetical counterexample with \(k\ge2\), there is a proper face
\[
F=B_1|\cdots|B_t
\]
such that
\[
a\in B_1,\qquad b\in B_t,
\]
and every vertex of
\[
V(H)-\{a,b\}
\]
belongs to the canonical exact hole in some chamber of \(F\).

This is a degree-level strengthening of the Tucker/Ky Fan output: not only does one universal hole-sweeping face exist, but the two possible exceptions can be prescribed arbitrarily and forced to opposite ends of the ordered-partition carrier.

### Universal-hole facets and a nested flag of global cuts

Continue to assume
\[
k=\kappa_2(H)\ge2.
\]
A proper face \(F\) is **unanimity-free** when
\[
A(F)=\bigcap_{\pi\in\mathcal V(F)}P_\pi=\varnothing,
\qquad
B(F)=\bigcap_{\pi\in\mathcal V(F)}Q_\pi=\varnothing.
\]
Such faces are upward closed in the face poset: if \(F\subseteq G\), then
\[
A(G)\subseteq A(F),\qquad B(G)\subseteq B(F).
\]

**Corollary 6.17 (universal-hole facet).**
There is a two-block facet
\[
A\mid B
\]
of the permutahedron such that every actual vertex of \(H\) belongs to \(X_\pi\) for some chamber \(\pi\) of that facet.

**Proof.** By Theorem 6.14 there is an unanimity-free proper face \(F\). Coarsen its ordered partition by merging consecutive blocks until only two nonempty blocks remain. The resulting facet \(G=A\mid B\) contains \(F\), so upward closure gives
\[
A(G)=B(G)=\varnothing.
\]
By the no-direct-side-flip lemma, a vertex that never enters a canonical hole on the connected chamber graph of \(G\) would have one constant nonzero side role and hence would belong to \(A(G)\cup B(G)\), impossible. Thus every vertex enters a hole in some chamber of \(G\). \(\square\)

Necessarily
\[
|A|,|B|\ge3.
\]
Indeed the first two positions of every chamber always belong to \(P_\pi\). If \(|A|\le2\), at least the first vertex block would contain a vertex that remains in \(P_\pi\) for every chamber of the facet. Symmetrically \(|B|\ge3\).

The positive-dimensional unanimity-free locus gives more.

**Corollary 6.18 (nested universal-hole cuts).**
There is an ordered partition
\[
C_1|\cdots|C_r,
\qquad r\ge k,
\]
which is unanimity-free, and hence for every
\[
1\le j<r
\]
the two-block coarsening
\[
(C_1\cup\cdots\cup C_j)
\mid
(C_{j+1}\cup\cdots\cup C_r)
\]
is a universal-hole facet.

**Proof.** Theorem 6.16 gives a chain of \(k-1\) strictly nested unanimity-free proper faces
\[
F_0\subsetneq\cdots\subsetneq F_{k-2}.
\]
If the smallest face \(F_0\) has \(r\) ordered blocks, then each strict coarsening reduces the block count by at least one. Since \(F_{k-2}\) is still proper and therefore has at least two blocks,
\[
r-(k-2)\ge2,
\]
so \(r\ge k\). Every two-block coarsening along a cut of \(F_0\) contains \(F_0\), hence remains unanimity-free by upward closure and is universal-hole by Corollary 6.17. \(\square\)

Thus a hypothetical obstruction of deletion distance \(k\ge2\) carries not merely one global cut but a flag of at least \(k-1\) nested global cuts, each of which supports holes sweeping the entire vertex set.

---

## Section — Exact-root compression and bounded central structure

<!-- section_id: exact_root_compression_and_bounded_central_structure -->

### Exact-root compression and bounded central structure

The exact status coordinates from [[spanning_orders_and_defect_helly]] are
[
p(pi)=min{i:epsilon_i=0},qquad
q(pi)=max{i:epsilon_i=1},qquad
c(pi)=m+1-q(pi),
]
with exact deficiency
[
delta(pi)=q-p-1=m-(p+c).
]
The exact root
[
psi(pi)=e_{p(pi)}-e_{c(pi)}
]
is odd under reversal. Unlike the older switch-root compression, its anti-diagonal displacement is exactly the order-level distance from a two-cover.

### Positive root balance

The barycentric odd-map construction of [[convex_root_balance_and_bourgin_yang]] yields a proper permutahedron face (F) and strictly positive chamber weights satisfying
[
sum_{piinmathcal V(F)}lambda_pipsi(pi)=0.
]
Interpreting (e_i-e_j) as the directed root (i	o j), every occurring nonzero root lies on a directed return cycle inside the same carrier face. The common-face condition is essential: all witnessing orders vary only by permutations within one ordered block partition.

### Bounded central block theorem

The facewise endpoint-transport and block-separation arguments developed in the former recurrence Section imply the following canonical compression.

**Theorem.** Suppose a positive exact-root carrier has positive deficiency in every chamber and contains no zero root. Then all varying exact-root data are controlled by a central face block (B) with
[
|B|le4.
]
Moreover at most ten actual vertices are needed to determine all varying exact-root labels in the carrier, and every simple directed root cycle has length two or three.

Thus the nonzero exact-root branch has no unbounded permutahedral residue. The only root-level recurrence left is a bounded interaction among opposite roots and, before the final moment reduction, directed triangles.

### Cubic moment and pairwise root symmetry

After translation to the four-coordinate model, every occurring nonzero root lies on the graph
[
01,quad02,quad03,quad12.
]
Append the odd cubic coordinate
[
sigma(i,j)=(j-i)^3.
]
Root balance makes the antisymmetric edge weights a circulation. The bridge (03) carries no circulation; the remaining triangle has one-dimensional cycle space. Cubic balance evaluates that triangle as
[
1^3+1^3-2^3=-6,
]
forcing its circulation coefficient to vanish. Hence
[
w_{ij}=w_{ji}
]
for every occurring root pair. No further odd scalar depending only on the ordered root can distinguish the carrier: root-only topology is exhausted at pairwise opposite-root balance.

### Deletion distance and the zero-root branch

The deletion-distance identity gives
[
kappa_2(H)=min_pimax(0,delta(pi)).
]
For
[
k=kappa_2(H)ge2,
]
the bounded-central-block analysis forces every positive exact-root carrier to contain a chamber with
[
p=c.
]
This is a genuinely balanced canonical partial two-cover:
[
P_pimid X_pimid Q_pi,qquad |P_pi|=|Q_pi|,
]
but (X_pi) may still be nonempty. A zero root is therefore not itself the grand-theorem conclusion.

For (k=1), the nonzero branch is already confined to the same bounded four-coordinate/four-vertex central geometry. Thus the exact-root theory separates the problem cleanly:

- nonzero recurrence is finite and bounded;
- for (kge2), topology forces the diagonal (p=c);
- further progress must use actual vertices, hole supports, or local status data rather than more root moments.

### Relation to the local-witness route

The local-witness compression developed next reaches the same numerical scale from a different invariant. This agreement is structural: root recurrence compresses the *extreme inversion coordinates*, whereas local witnesses compress the *nearest actual forbidden pattern*. The two routes should be regarded as complementary descriptions of the same finite central geometry, not independent grand-theorem obligations.

---

## Section — Local-witness topology and the finite terminal theorem

<!-- section_id: local_witness_topology_and_the_finite_terminal_theorem -->

### Local-witness topology and the finite terminal theorem

The exact inversion-window criterion admits a local language that is better suited to chamber topology than the extreme-root coordinates.

### Exact forbidden words

For a status word
[
epsilon_1cdotsepsilon_m,
]
the two-cover condition
[
qle p+1
]
is equivalent to the absence of a zero followed by a one at distance at least two. A minimal such inversion has span two or three. Hence:

**Forbidden-pattern theorem.**
[
oxed{
qle p+1
iff
epsilon	ext{ avoids }001, 011, 0101.
}
]

Thus every bad spanning order has a local witness on at most four consecutive status positions, equivalently on at most six consecutive vertices. Complementing all triple colors preserves path-cover number, so the opposite-polarity witnesses
[
110, 100, 1010
]
are available as well.

### The fixed witness path

The reflected locations of the three basic witnesses are generated by the two reflections
[
imapsto m-1-i,qquad imapsto m-2-i.
]
Their nontrivial pairs interlace to form a single path (T_m) on witness-location coordinates, with one pendant treatment for the unique centered self-reflecting case. Fix an external antipodal sign on spanning orders, for example the relative-order sign of two fixed vertices. Then every bad spanning order receives a nonzero oriented edge label
[
ell(pi)in E(T_m)
]
such that
[
ell(pi^{m rev})=-ell(pi).
]

Because (T_m) is a tree, its edge-incidence vectors are linearly independent. Positive convex cancellation is therefore edgewise: every used witness edge must occur in both orientations.

### Bourgin--Yang and protected central bands

For (m=n-2), the permutahedron boundary is (S^m), while the witness-edge space has dimension (m-2). Averaging the labels at face barycenters and extending over the barycentric subdivision gives an odd map
[
S^mlongrightarrow mathbb R^{m-2}.
]
Bourgin--Yang yields a zero set of dimension at least two.

Let (F) be a positive carrier of such a zero and let (e) be the innermost witness edge occurring among its chamber labels. Then every chamber of (F) avoids all witness edges closer to the center, while both orientations of (e) occur. Hence every chamber shares a protected central band free of
[
001, 011, 0101.
]
Inside that band every chamber has the local two-cover form
[
1^*0^*
quad	ext{or}quad
1^*010^*.
]

Using both inversion polarities sharpens this further: an interval avoiding all six local witnesses
[
001, 011, 0101, 110, 100, 1010
]
is monochromatic once its length is at least four. Consequently reflected double witnesses selected nearest the center are automatically bounded near the center; there is no unbounded symmetric-double branch.

### Face cancellation and Boolean cubes

For an ordered-partition face
[
F=B_1|cdots|B_k,
]
the average status at any three-position window contained in one block is zero: swap the first and third vertices of the window. For pairwise disjoint internal windows these involutions commute, so the selected status coordinates realize a full Boolean cube over the chamber family.

This forces strong thinness in a protected band. Two disjoint internal triple windows would allow one to prescribe an earlier zero and a later one, creating a forbidden pattern. In particular, five protected consecutive vertex positions cannot lie in one face block. The stronger finite argument rules out such a five-position block directly from boundary antisymmetry.

### Terminal block compression

Suppose the nearest-witness reduction reaches a terminal single-sided configuration with disjoint reflected determining windows. Let (B) be the unique face block coupling the two windows, and let (alpha,eta) be the numbers of (B)-positions used on the two sides.

The ordered-tuple disjointness graph gives
[
|B|lealpha+eta.
]
Simultaneous occupation gives the reverse inequality, so
[
|B|=alpha+eta.
]
Boundary antisymmetry inside a fixed support partition then forces
[
alpha,etale2,
qquad |B|le4.
]

The alternating branch (0101/1010) is impossible: nearestness fixes the inward statuses strongly enough that the two terminal witness indicators collapse to unary functions of the first and last block vertices, and the identity that exactly one side occurs forces both functions to be constant.

The span-two branch is even sharper in the dual-polarity formulation. A purported terminal disjoint witness of type
[
001, 011, 110, 100
]
immediately creates a strictly closer witness of one of the six dual-polarity types. Therefore no disjoint single-sided terminal configuration survives.

### Finite terminal theorem

Only centered or overlapping reflected witnesses remain. Their determining support is bounded:

- centered span-two witnesses use at most five vertices;
- centered alternating witnesses use at most six;
- reflected double span-two supports use at most eight;
- reflected alternating supports use at most ten.

Each finite terminal support is two-coverable. The small centered cases split into two sets of order at most three; the reflected cases are covered by the established eight- and ten-vertex boundary-tournament theorems.

Therefore:

[
oxed{
	ext{every terminal local-witness support has path-cover number at most }2.
}
]

The local finite line is closed. The only remaining issue is global: prove that every balanced witness carrier can be terminalized, or use its escape geometry directly to build a spanning two-cover.

---

## Section — Terminalization, reachability, and the exact frontier

<!-- section_id: terminalization_reachability_and_the_exact_frontier -->

### Current closure frontier

The geodesic program now has a sharply separated finite and global structure.

### What is already closed

The exact status-word theory gives local forbidden witnesses. The witness-path topology gives positive balanced carrier faces. The finite classification in [[local_witness_topology_and_the_finite_terminal_theorem]] proves:
[
oxed{	ext{every terminal local-witness support is two-coverable}.}
]

Thus there is no remaining finite terminal obstruction to classify. Centered witnesses, overlapping reflected witnesses, double witnesses, and disjoint single-sided branches have all been reduced to explicit finite supports and closed.

The exact-root route independently reaches the same bounded scale: nonzero recurrent carriers have a central block of order at most four and at most ten determining vertices.

### The missing global implication

Let (C) be a positive balanced carrier for the fixed-path local-witness map, and let (e) be the innermost witness edge appearing among chamber labels. Then all chambers are protected from witness edges closer to the center, both orientations (+e) and (-e) occur, and face-product splicing may produce chambers in which (e) disappears and the selected witness moves farther outward.

The missing point is that an improved chamber is not automatically an improved **balanced carrier**. Convex cancellation may still use other chambers labeled by (e).

**Terminalization theorem.** From a positive balanced carrier with innermost witness edge (e), either obtain a spanning two-cover directly, obtain one of the already classified terminal finite supports, or construct a new positive balanced carrier whose chamber labels all lie strictly farther outward than (e).

Iteration would terminate because the witness path is finite. Together with the finite terminal theorem, this would prove the grand conjecture.

### Relative-index formulation

The natural topological model is a relative separator problem. The (+e) and (-e) chamber regions are separated by configurations in which the (e)-witness is absent. On that (e)-free locus, the remaining witness coordinates lie on the outer subpath.

The desired mechanism is a relative (mathbb Z_2)-index or Bourgin--Yang recursion:
[
	ext{balanced carrier index}
longrightarrow
	ext{index retained on the }e	ext{-free separator}
longrightarrow
	ext{zero of the outer witness map}.
]

The technical issue is that an individual carrier face need not be antipodally invariant, and a barycentric zero may cancel (+e) and (-e) contributions without containing an actual chamber where (e) is absent. The finite mixed-cell classification should be used precisely here: if cancellation across (e) occurs without a genuine separator chamber, the responsible cell should already fall into one of the closed finite support types.

This is now the principal research target.

### Relation to antipodal reachability

The earlier exact reachability formulation remains valid:
[
operatorname{pc}(H)le2
quadLongleftrightarrowquad
Rcap A(R)	ext{ is nonempty}
]
in the auxiliary memory lift. Its neutral corridor is best viewed as a global analogue of the witness-carrier separator.

The current witness topology is more economical because it compresses the obstruction before attempting reachability intersection. A successful terminalization theorem would effectively resolve the relevant neutral-corridor obstruction without proving a separate reachability theorem.

Thus antipodal reachability is no longer an independent branch that must be closed after terminalization; it is an alternate language for the same global separator phenomenon.

### Exact status of the grand conjecture

The proof architecture is
[
	ext{counterexample}
Longrightarrow
	ext{balanced local-witness carrier}
Longrightarrow
egin{cases}
	ext{terminal finite support},\
	ext{or an outward escape}.
end{cases}
]

The first branch is closed by the finite terminal theorem. The second branch is what terminalization must convert into a new balanced carrier or a direct two-cover. Accordingly
[
oxed{
	ext{terminalization}
+
	ext{the proved finite terminal theorem}
Longrightarrow
operatorname{pc}(H)le2.
}
]

No separate solution of the old omission-facet, zero-root, neutral-corridor, or disturbance branches would then be required.

### Proof-transfer program toward generalized Norine

The eventual terminalization proof should be audited for portability. The chamber topology, antipodal symmetry, witness-tree compression, and relative-index recursion appear substantially less dependent on GN3 translation invariance than the block-swap and splicing lemmas.

This motivates the independent meta-conjecture recorded in [[meta_conjecture_gn3_closure_should_seed_generalized_norine]]: a substantial core of the eventual boundary-tournament proof should seed a generalized bounded-memory Norine geodesic theorem. That program is deliberately kept separate from the proof of the present conjecture, but the distinction between portable topology and GN3-specific face combinatorics should be tracked as the terminalization argument is developed.

## Contained Sections

- 1. [Spanning orders and defect Helly theory](../SECTIONS/spanning_orders_and_defect_helly.md) (\`spanning_orders_and_defect_helly\`; composition v1; stale=False)
- 2. [The Norine–GN3 dictionary and Freudenthal geometry](../SECTIONS/norine_gn3_dictionary_and_freudenthal_geometry.md) (\`norine_gn3_dictionary_and_freudenthal_geometry\`; composition v1; stale=False)
- 3. [The memory lift and exact antipodal geodesics](../SECTIONS/memory_lift_and_exact_antipodal_geodesics.md) (\`memory_lift_and_exact_antipodal_geodesics\`; composition v1; stale=False)
- 4. [Auxiliary exactification and complementary path supports](../SECTIONS/auxiliary_exactification_and_complementary_supports.md) (\`auxiliary_exactification_and_complementary_supports\`; composition v1; stale=False)
- 5. [From antipodal labels to cellular root topology](../SECTIONS/antipodal_labels_and_cellular_root_topology.md) (\`antipodal_labels_and_cellular_root_topology\`; composition v1; stale=False)
- 6. [Convex root balance and Bourgin–Yang multiplicity](../SECTIONS/convex_root_balance_and_bourgin_yang.md) (\`convex_root_balance_and_bourgin_yang\`; composition v1; stale=False)
- 7. [Exact-root compression and bounded central structure](../SECTIONS/exact_root_compression_and_bounded_central_structure.md) (\`exact_root_compression_and_bounded_central_structure\`; composition v1; stale=False)
- 8. [Local-witness topology and the finite terminal theorem](../SECTIONS/local_witness_topology_and_the_finite_terminal_theorem.md) (\`local_witness_topology_and_the_finite_terminal_theorem\`; composition v1; stale=False)
- 9. [Terminalization, reachability, and the exact frontier](../SECTIONS/terminalization_reachability_and_the_exact_frontier.md) (\`terminalization_reachability_and_the_exact_frontier\`; composition v1; stale=False)
