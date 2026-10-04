# Article VII — antipodal geodesics, defect Helly theory, and topological compression

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


### Further developments



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

## Section — From topological recurrence to local GN3 structure

<!-- section_id: topological_recurrence_to_local_gn3_structure -->

### From balanced recurrence to local reversal structure

### Determining positions and positive face balance

Let \(F=B_1|\cdots|B_k\) be a proper permutahedral face, with its blocks occupying consecutive positions. Assume its chamber roots admit a circulation strictly positive on every occurring root, as provided by [[convex_root_balance_and_bourgin_yang]]. Then every coordinate occurring as a first switch also occurs as a reflected last switch in the same face. Every chamber belongs to a directed root cycle, unless it has a zero root and is already an exact diagonal.

This is stronger than choosing just one cycle. The following deductions explain what can be extracted without assuming that convex balance is already a two-cover.

### Block separation with explicit determining windows

A first switch at \(x\) is determined by the first \(x+1\) statuses and hence by vertex positions
\[
1,\ldots,x+3.
\]
A reflected last switch at \(x\) is determined by the last \(x+1\) statuses and hence by positions
\[
n-x-2,\ldots,n.
\]

**Lemma 7.1.** Suppose \(F\) has a chamber with first switch \(x\), a chamber with reflected last switch \(x\), and a block boundary after position \(j\) such that
\[
x+3\leq j\leq n-x-3.
\]
Then \(F\) contains a chamber with root zero.

**Proof.** Use the block orders from the first witness in every block up to the boundary, and those from the second witness after it. Both determining windows remain unchanged. The resulting chamber has \(a=\bar b=x\). \(\square\)

Consequently, if \(F\) contains no diagonal and the displayed interval of possible boundaries is nonempty, all positions
\[
x+3,\ldots,n-x-2
\]
lie in a single block. Its size is at least \(n-2x-4\).

**Corollary 7.2.** Under strictly positive face balance and absence of a diagonal, let \(r\) be the least switch coordinate occurring in any chamber root of \(F\). If \(n\geq2r+6\), one block contains positions \(r+3,\ldots,n-r-2\). It also contains every nonempty corridor of this form for any larger occurring coordinate.

**Proof.** Positive balance supplies both kinds of witness for \(r\), so Lemma 7.1 excludes all boundaries in its corridor. Corridors for larger coordinates are nested inside it. \(\square\)

This gives a single block for all occurring root coordinates, not only those of a selected cycle. If \(n<2r+6\), this separation lemma gives no block conclusion. Near-central coordinates must be treated by a separate argument; their numerical location alone does not prove a bounded-support descent.

### Cross-intersecting determining families

Fix the orders of all blocks other than a chosen block \(B\), and fix a coordinate \(x\) whose two determining windows are disjoint. Let \(\mathcal L_x\) consist of the sets of labels of \(B\) occupying its positions in the left window in some chamber with first switch \(x\). Define \(\mathcal R_x\) analogously for reflected last switch \(x\). Witness orders of these sets inside the corresponding positions are retained when combining them.

**Lemma 7.3.** If no chamber with these fixed outside orders has root zero, then every \(L\in\mathcal L_x\) intersects every \(R\in\mathcal R_x\).

**Proof.** If the sets were disjoint, place each in its own determining positions using its witness order, and fill the remaining positions of \(B\) arbitrarily. The disjoint windows and the fixed outside orders preserve both witnesses. This produces a diagonal. \(\square\)

The qualification about outside orders is essential: face balance supplies witnesses somewhere in \(F\), not automatically witnesses with every prescribed choice of outside block orders.

If both families are nonempty, any member of \(\mathcal L_x\) is a transversal of \(\mathcal R_x\). An inclusion-minimal transversal \(T\) contained in it has, for each \(v\in T\), a member of \(\mathcal R_x\) meeting \(T\) exactly at \(v\); otherwise \(v\) could be removed. This preserves the private-witness mechanism without asserting an absolute bound on \(|T|\). Such a bound would require a bound on the number of determining positions inside \(B\).

### Front motion with the witness hypotheses retained

**Lemma 7.4.** Fix all outside block orders. Suppose a permutation of \(B\) realizes first switch \(x\), another realizes reflected last switch \(x\), and no permutation of \(B\) realizes a diagonal. Then an adjacent transposition within \(B\) changes the first switch coordinate.

**Proof.** In the second witness, the first switch cannot equal \(x\). The adjacent-transposition graph of the permutations of \(B\) is connected. Along a path between the two witnesses, at least one swap changes the first switch. \(\square\)

If positions \(j,j+1\) are swapped, only triple positions \(j-2,\ldots,j+1\) can change, clipped to \(1,\ldots,m\). Consequently only switch positions \(j-3,\ldots,j+1\) can change. If two resulting first-switch coordinates \(a<a'\) differ, the earlier coordinate \(a\) lies in this five-position interval; the word with first switch \(a'\) is constant through position \(a'\). Thus a long displacement has a monochromatic interval, while the cause of the displacement is local. The same statement holds for last switches by reversal.

### The conversion problem after face recurrence

Boundary antisymmetry turns each specified non-tight triple into its reversed tight triple. By itself, however, the preceding face geometry does not yet synchronize arbitrary left and right witnesses: a moved front need not already be one exterior vertex reversing two required end edges, and witnesses with different outside block orders need not have disjoint exposed edges.

The next subsection resolves precisely this issue without trying to synchronize two arbitrary chambers. Instead one minimizes switch span inside the carrier face and transports the **same physical carrier** to the two extreme fronts of a single chamber. The common-block conclusion above keeps both tests inside the face, while minimality prevents inward front motion. This produces the required local reversal structure and removes the formerly global synchronization problem.

The local path-cover mechanisms used after that compression are recorded in [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], [[endpoint_transport_and_small_support_gluing_the_remaining_lemma]], and [[defect_lines_and_spanning_order_compression_the_remaining_lemma]].


### Recurrent-face and minimum-span compression


### Compact switch span

For a spanning order
\[
\pi=(v_1,\ldots,v_n)
\]
whose status word has first switch \(a\) and last switch \(b\), put
\[
d(\pi)=b-a.
\]

**Lemma 7.5 (compact switch span).** If \(d(\pi)\le 2\), then \(H\) has a spanning two-cover.

**Proof.** Cut the order after \(v_{a+2}\). Every status internal to the left block has index at most \(a\), hence has the first-run color. Every status internal to the right block has index at least \(a+3>b\), hence has the last-run color. A monochromatic block is a tight path in its displayed orientation when its color is tight, and in the reverse orientation when its color is non-tight. Thus the two blocks can be oriented as tight paths. \(\square\)

The same cut calculation gives a useful next range.

**Lemma 7.6 (small middle from span at most five).** If
\[
3\le d(\pi)\le5,
\]
then \(H\) has a spanning three-cover
\[
L\mid M\mid R
\]
in which
\[
|M|=d(\pi)-2\le3.
\]

**Proof.** Put
\[
L=(v_1,\ldots,v_{a+2}),\qquad
M=\{v_{a+3},\ldots,v_b\},\qquad
R=(v_{b+1},\ldots,v_n).
\]
All internal statuses of \(L\) have the first-run color and all internal statuses of \(R\) have the last-run color, so each outer block has a tight orientation. The middle has order at most three and is therefore Hamiltonian: orders one and two are vacuous, and on three vertices one of the two reverse orders is tight by boundary antisymmetry. \(\square\)

### A recurrent carrier face has no large global residue

Let
\[
F=B_1|\cdots|B_k
\]
be a carrier face supplied by Theorem 6.1, so every chamber root occurring in \(F\) lies on a directed root cycle unless it is zero. Assume first that \(F\) contains no zero root.

Choose a chamber
\[
\pi=(v_1,\ldots,v_n)\in\mathcal V(F)
\]
for which \(d=b-a\) is minimum among the chambers of \(F\). Put
\[
m=n-2,\qquad c=m-b,
\]
so the root of \(\pi\) is the arc
\[
a\longrightarrow c.
\]

Because this arc lies on a directed root cycle, choose a simple such cycle and let \(r\) be its least coordinate. Every arc \(x\to y\) on the cycle comes from a chamber with
\[
x+y=m-d(\text{that chamber})\le m-1.
\]

If
\[
n<2r+6,
\]
then \(m\le2r+3\). For a neighbor \(s\) of \(r\) on the cycle,
\[
2r\le r+s\le m-1\le2r+2.
\]
There are no loops because \(F\) has no zero root, so \(s-r\in\{1,2\}\). The chamber realizing \(r\to s\) has switch span
\[
m-r-s\le2,
\]
and Lemma 7.5 gives a two-cover.

Hence, in a counterexample,
\[
n\ge2r+6.
\]
Corollary 7.2 then gives one block \(B\) of \(F\) containing the whole corridor
\[
r+3,\ldots,n-r-2=r+3,\ldots,m-r.
\]
Since \(a,c\ge r\), whenever \(d=b-a\ge6\) the position interval
\[
a+4,\ldots,b-1
\]
lies inside this same block.

This allows one physical vertex to be tested at both extreme fronts without leaving the face.

**Theorem 7.7 (one-carrier compression in a recurrent face).** Suppose \(H\) has no spanning two-cover. Suppose \(F\) has positive balance on every chamber and contains no zero root. Let \(\pi\in\mathcal V(F)\) minimize switch span in \(F\). If \(d(\pi)\ge6\), then \(H\) contains a Hamiltonian support of order four or five.

**Proof.** Let
\[
W=\{v_{a+4},\ldots,v_{b-1}\}.
\]
Then \(|W|=d-4\ge2\), and all these positions lie in the single face block \(B\).

Fix \(w\in W\). First permute only positions \(a+4,\ldots,b-1\) inside \(B\) so that \(w\) occupies position \(a+4\). This preserves both extreme switches: the first switch is determined through position \(a+3\), while the last switch \(b\) is determined by positions \(b,\ldots,n\). Now swap positions \(a+3,a+4\). No switch before \(a\) can be created, and \(b\) is outside the affected window. If the first switch moved to the right, the new chamber of \(F\) would have smaller switch span, contrary to the choice of \(\pi\). Therefore the first switch remains \(a\).

Let \(\alpha\) be the first-run color. If \(\alpha=1\), the preceding statement says that \(w\) reverses the terminal edge of the tight-oriented left outer block. If \(\alpha=0\), the left outer block is tight after reversal and the same statement says that \(w\) reverses its initial edge.

Independently restart from \(\pi\), place the same \(w\) at position \(b-1\), and swap positions \(b-1,b\). The first switch is now outside the affected window. If the last switch moved left, the switch span would decrease. Hence the last switch remains \(b\). Writing \(\omega\) for the last-run color, \(w\) reverses the terminal edge of the tight-oriented right outer block when \(\omega=0\), and its initial edge when \(\omega=1\).

The two exposed edges are vertex-disjoint because \(d\ge6\).

If \(\alpha\ne\omega\), the two reversals have the same endpoint type: terminal-terminal for \((\alpha,\omega)=(1,0)\), and initial-initial for \((0,1)\). A common reverser of two disjoint same-type end edges gives a Hamiltonian four-support. For completeness, in the terminal-terminal case, if the two tight paths end in \(x_0,x_1\) and \(y_0,y_1\), then
\[
(w,x_1,x_0),\qquad(w,y_1,y_0)
\]
are tight. Exactly one of
\[
(x_1,w,y_1),\qquad(y_1,w,x_1)
\]
is tight. In the first case
\[
(x_1,w,y_1,y_0)
\]
is a tight four-path; in the second
\[
(y_1,w,x_1,x_0)
\]
is. The initial-initial case is symmetric.

Suppose now that \(\alpha=\omega\). The two reversals have mixed endpoint type. Up to symmetry write the tight-oriented exposed edges as
\[
\ldots,a_0,a_1
\qquad\text{and}\qquad
p_1,p_2,\ldots
\]
so that
\[
(w,a_1,a_0),\qquad(p_2,p_1,w)
\]
are tight. Exactly one of
\[
(p_1,w,a_1),\qquad(a_1,w,p_1)
\]
is tight. The first alternative gives the Hamiltonian five-path
\[
(p_2,p_1,w,a_1,a_0).
\]
In the second alternative \(w\) is a parallel middle between \(a_1\) and \(p_1\).

There are at least two choices of \(w\in W\). If neither gives a Hamiltonian five-support, choose distinct \(w,w'\) with
\[
(a_1,w,p_1),\qquad(a_1,w',p_1)
\]
tight. Exactly one of
\[
(w,a_1,w'),\qquad(w',a_1,w)
\]
is tight. Accordingly
\[
(w,a_1,w',p_1)
\quad\text{or}\quad
(w',a_1,w,p_1)
\]
is a tight four-path. Thus a Hamiltonian support of order four or five always occurs. \(\square\)

The proof deliberately uses the same physical carrier and two exposed edges from one chamber. It therefore does not require the false implication that two distinct reversers of one common edge force a four-support, and it does not require exposed edges belonging to two different witness orders to be disjoint.

Combining Lemmas 7.5–7.6 with Theorem 7.7 gives the non-diagonal face conclusion:
\[
\boxed{
\begin{array}{c}
\text{positively balanced carrier face with no zero root}
\\[2mm]\Longrightarrow\\[2mm]
\text{two-cover}
\ \vee\
\text{spanning three-cover with a component of order }\le3
\ \vee\
\text{Hamiltonian support of order }4\text{ or }5.
\end{array}}
\]

Thus the coordinated face structure eliminates the genuinely global giant-block residue. A nonzero recurrent chamber cannot remain trapped in an unbounded front-motion configuration.

### The diagonal branch is absorbed by global minimum span

A zero root need not itself be a two-cover, so it must not be silently identified with the exact target. There is, however, a face-independent version of the preceding carrier argument which absorbs this branch as well.

**Theorem 7.8 (global minimum-span compression).** Let \(H\) be a boundary \(3\)-tournament with no spanning two-cover. Choose a spanning order \(\pi\) with globally minimum switch span \(d=b-a\). Then exactly one of the following local outcomes occurs:

1. \(3\le d\le5\), and \(H\) has the spanning three-cover of Lemma 7.6 with a component of order at most three;
2. \(d\ge6\), and \(H\) contains a Hamiltonian support of order four or five.

**Proof.** A counterexample has no order with at most one switch, because such an order already splits into two monochromatic tight orientations. Lemma 7.5 excludes \(d\le2\).

For \(3\le d\le5\), apply Lemma 7.6.

Assume \(d\ge6\). Now the interval
\[
a+4,\ldots,b-1
\]
may be permuted freely in the full permutation space, rather than merely inside one face block. Repeat verbatim the two carrier tests from Theorem 7.7. If either extreme front moved inward, the resulting spanning order would have smaller switch span, contradicting global minimality. Thus the same carrier reverses the two disjoint exposed end edges. The same-end and mixed-end arguments above give a Hamiltonian support of order four or five. \(\square\)

This theorem is stronger as a compression statement than the topology needs: once a counterexample is assumed, large switch span is already impossible as an independent geodesic obstruction.

### Closure of the geodesic/topological branch

The root topology and the global geodesic extremal argument now meet at one precise interface.

Theorem 6.1 upgrades a convex zero to recurrence for every chamber of a carrier face. Theorem 7.7 converts every nonzero recurrent branch into a two-cover or bounded local GN3 structure. A zero-root chamber is not itself declared solved; Theorem 7.8 instead shows that the diagonal branch cannot retain an independent global geodesic obstruction either.

Consequently Article VII has no remaining unbounded permutahedral or antipodal-geodesic residue. In a hypothetical counterexample the output of the entire geodesic program is already local:
\[
\boxed{
\text{small-middle spanning three-cover}
\quad\vee\quad
\text{Hamiltonian }4\text{- or }5\text{-support}.
}
\]

This is a handoff, not a proof of the grand conjecture. In particular it does not assert
\[
R\cap A(R)\ne\varnothing.
\]
What has been closed is the specifically geodesic/topological conversion problem: balanced recurrence no longer needs to be synchronized into a global reachability state. Its only surviving consequences are the bounded GN3 configurations handled by the local path-cover machinery.


### Exact-deficiency sharpening: the one-hole four-support handoff


### Exact deficiency one in a minimum counterexample

The exact inversion coordinates from [[spanning_orders_and_defect_helly]] sharpen the minimum-span conclusion further. For a spanning order \(\pi\), write
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
and
\[
\delta(\pi)=q(\pi)-p(\pi)-1.
\]
By the exact inversion-window criterion,
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }\delta(\pi)\le0.
\]
Thus every spanning order of a counterexample has \(\delta\ge1\).

**Theorem 7.9 (minimum exact deficiency is one).** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then
\[
\min_\pi\delta(\pi)=1.
\]
More precisely, for every \(x\in V(H)\) and every displayed two-cover
\[
H-x=P\mid Q
\]
with \(P=(p_1,\ldots,p_r)\) and \(Q=(q_1,\ldots,q_s)\), the spanning order
\[
\pi=(p_1,\ldots,p_r,x,q_s,\ldots,q_1)
\]
has \(\delta(\pi)=1\).

**Proof.** First \(r,s\ge3\). Indeed, if one deletion-cover component had order at most two, adjoining \(x\) would give a set of order at most three, hence a Hamiltonian tight path; together with the other displayed component this would two-cover \(H\).

In \(\pi\), every status wholly inside \(P\) is \(1\), while every status wholly inside \(Q^{\rm rev}\) is \(0\). Hence only the three junction statuses
\[
(p_{r-1},p_r,x),\qquad
(p_r,x,q_s),\qquad
(x,q_s,q_{s-1})
\]
can interrupt the pattern \(1^*0^*\). Consequently
\[
p(\pi)\ge r-1,\qquad q(\pi)\le r+1,
\]
so
\[
\delta(\pi)=q(\pi)-p(\pi)-1\le1.
\]
Since \(H\) is a counterexample, the exact inversion-window criterion gives \(\delta(\pi)\ge1\). Therefore \(\delta(\pi)=1\). \(\square\)

Equality forces
\[
p(\pi)=r-1,\qquad q(\pi)=r+1.
\]
Thus the first and third junction statuses are forced:
\[
(p_{r-1},p_r,x)\text{ is non-tight},
\qquad
(x,q_s,q_{s-1})\text{ is tight}.
\]
By boundary reversal,
\[
(x,p_r,p_{r-1})
\]
is tight as well. Hence the omitted vertex \(x\) reverses the displayed terminal edge of each deletion path:
\[
(x,p_r,p_{r-1}),\qquad
(x,q_s,q_{s-1})
\quad\text{are tight}.
\]

This is exactly the deficiency-one instance of the canonical partial-cover construction in [[convex_root_balance_and_bourgin_yang]]: the exact root carries a two-path cover with one missing vertex, and the missing vertex controls both exposed terminal edges.

### The exact geodesic handoff is a four-support

The preceding double reversal has an immediate bounded consequence.

**Corollary 7.10 (canonical four-support from exact deficiency one).** Let \(H\) be a minimum counterexample. For every deletion cover
\[
H-x=P\mid Q,
\]
the terminal edges of \(P\) and \(Q\), together with \(x\), contain a Hamiltonian four-support. Its complement is non-Hamiltonian and has path-cover number exactly two.

**Proof.** Write the terminal edges of the displayed tight paths as
\[
\ldots,a_0,a_1,
\qquad
\ldots,b_0,b_1.
\]
Theorem 7.9 gives
\[
(x,a_1,a_0),\qquad(x,b_1,b_0)
\]
tight. Exactly one of
\[
(a_1,x,b_1),\qquad(b_1,x,a_1)
\]
is tight. In the first case
\[
(a_1,x,b_1,b_0)
\]
is a tight Hamiltonian four-path; in the second,
\[
(b_1,x,a_1,a_0)
\]
is.

Let \(K\) be this four-set. It is proper, since otherwise \(H\) itself would be Hamiltonian. By minimality, \(H-K\) has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on \(H-K\) together with the displayed Hamilton path on \(K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2
\]
and \(H-K\) is non-Hamiltonian. \(\square\)

This sharpens the minimum-counterexample endpoint of the geodesic investigation. The width-three switch-span formulation remains useful for arbitrary counterexamples and for the recurrent-face compression, but after minimum-counterexample induction the exact inversion coordinate removes the mixed-end ambiguity entirely:
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support with non-Hamiltonian two-coverable complement}.
}
\]

Thus no synchronization of an entire directed root cycle is needed to finish Article VII's own task. The exact-root coordinate already reaches the bounded local interface. What remains after this point is the local four-support/path-cover analysis, not an antipodal-geodesic obstruction.


### Minimum-hole synchronization

Minimum deletion holes synchronize all omitted vertices as common reversers of the same two terminal edges; proof to follow.

Proof. Because X has minimum cardinality, H-X cannot be Hamiltonian: otherwise adding any one x in X as a singleton would two-cover H-(X minus {x}). Likewise neither P nor Q can have order at most two, because adjoining x to such a component produces a Hamiltonian set of order at most three and again yields a two-cover after deleting only X minus {x}. Hence both displayed paths have order at least three.

Fix x in X and put J=H-(X minus {x}). By minimality of X, pc(J)>2, while J-x=P|Q. Consider the order obtained by writing P, then x, then Q in reverse. All statuses internal to P are tight and all statuses internal to the reversed Q are non-tight. If r=|P|, the first non-tight status is no earlier than r-1 and the last tight status is no later than r+1. Therefore its exact deficiency is at most one. Since J has no two-cover, the inversion-window criterion forces the deficiency to be at least one. Equality follows.

Equality pins the first and last junction positions. Therefore every x in X reverses both terminal edges, as claimed. This completes the proof.

For each x in X, the middle triple on the two exposed endpoints has exactly one tight orientation. Combining it with the two reversal triples gives a Hamiltonian four-support through x. Removing that four-support and then deleting X without x leaves prefixes of P and Q as a two-cover. Hence the two-cover deletion distance of the complement drops by at least one.

### Bounded central blocks and short cycles in recurrent exact-root faces

### Exact roots and the hypotheses

For a spanning order \(\pi\) of a boundary \(3\)-tournament \(H\) on \(n\) vertices, write \(m=n-2\), let \(p(\pi)\) be the first non-tight status position, and let \(c(\pi)=m+1-q(\pi)\), where \(q(\pi)\) is the last tight status position. Thus \(c(\pi)=p(\pi^{\mathrm{rev}})\). The exact root is \(e_p-e_c\), and the exact deficiency is
\[
\delta(\pi)=m-p(\pi)-c(\pi).
\]
These conventions and the two-cover criterion are established in [[spanning_orders_and_defect_helly]].

Let \(F\) be an ordered-partition face of the permutahedron. Assume:

1. \(\delta(\pi)>0\) for every chamber \(\pi\) of \(F\);
2. every coordinate occurring as a tail of an exact root on \(F\) also occurs as a head, and conversely;
3. \(p(\pi)\ne c(\pi)\) for every chamber of \(F\).

Hypothesis 2 is weaker than positive root balance. In particular, the positive carrier theorem of [[convex_root_balance_and_bourgin_yang]] supplies it. No minimum-counterexample hypothesis is used.

**Theorem (bounded central block).** Put
\[
s=\min_{\pi\in\mathcal V(F)}\min\{p(\pi),c(\pi)\},
\qquad L=m-2s.
\]
There is a single face block \(B\), with \(b=|B|\le7\), such that the numbers \(\ell,r\) of positions before and after \(B\) satisfy
\[
\ell,r\in\{s,s+1\}.
\]
Every other face block has order at most two. More precisely:
\[
\begin{array}{c|c|c}
(\ell,r)& b\text{ in terms of }L&\text{upper bound on }b\\ \hline
(s,s)&L+2&7\\
(s,s+1)\text{ or }(s+1,s)&L+1&5\\
(s+1,s+1)&L&7.
\end{array}
\]
In particular \(2\le L\le7\), and every exact-root coordinate on \(F\) lies in
\[
\{s,s+1,\ldots,s+L-1\}\subseteq\{s,\ldots,s+6\}.
\]

### Locating the central block

Coordinate recurrence gives both a chamber with \(p=s\) and a chamber with \(c=s\). Since no root is zero, a chamber with \(p=s\) has \(c\ge s+1\). Its positive deficiency gives
\[
m\ge2s+2,
\]
so \(L\ge2\).

The event \(p=s\) is determined by positions \(1,\ldots,s+2\); the event \(c=s\) is determined by positions \(n-s-1,\ldots,n\). If a block boundary followed a position
\[
s+2\le j\le n-s-2,
\]
the independent block orders from the two witnesses could be combined, giving \(p=c=s\). Consequently one block \(B\) contains every position
\[
s+2,\ldots,n-s-1.
\]
Thus \(\ell,r\le s+1\).

Every chamber has \(p,c\ge s\). Hence all status positions \(1,\ldots,s-1\) are tight in every chamber, and all the corresponding statuses read inward from the right end are also tight in every chamber. If \(\ell\le s-2\), then \(B\) contains the three positions \(s-1,s,s+1\). Swapping the first and third vertices of this window stays in \(F\) and reverses its status, contradicting uniform tightness at \(s-1\). Therefore
\[
s-1\le\ell,r\le s+1.
\]

Set
\[
\alpha=s+2-\ell,\qquad\beta=s+2-r.
\]
These numbers belong to \(\{1,2,3\}\). A witness for \(p=s\) uses exactly the first \(\alpha\) vertices of \(B\), together with some orders of the blocks before \(B\). A witness for \(c=s\) uses exactly the first \(\beta\) vertices of \(B\) read inward from the right, together with some orders of the blocks after \(B\). In particular
\[
b=L+\alpha+\beta-2.
\]

Let \(\mathcal L,\mathcal R\) be the families of supports of these ordered witness tuples, allowing all outside block orders on the relevant side. Both families are nonempty. Every member of \(\mathcal L\) meets every member of \(\mathcal R\): disjoint witness tuples can be placed at opposite ends of \(B\), with their own left and right outside orders, and the remaining positions filled arbitrarily. This would give \(p=c=s\).

The independent choices of outside orders are legitimate here because the two determining windows are disjoint and involve disjoint collections of outside blocks. We are not combining two arbitrary witnesses that constrain the same outside block.

If \(\alpha=3\), the determining status at \(s\) is wholly inside \(B\). Every three-element subset of \(B\) therefore supports a left witness: one of the two reversed orders, for any fixed middle vertex, is non-tight. But a right witness uses \(\beta\) vertices, and
\[
b-\beta=L+1\ge3.
\]
A left witness can be chosen disjoint from it, a contradiction. The case \(\beta=3\) is symmetric. Thus \(\alpha,\beta\in\{1,2\}\), which proves \(\ell,r\in\{s,s+1\}\).

A block before \(B\) with three consecutive positions would contain a status window starting at most at \(\ell-2\le s-1\), where tightness is uniform. Boundary reversal rules this out. The same argument read inward from the right treats every block after \(B\). Thus all exterior blocks have order at most two.

### Bounding the central block by disjoint witnesses

We use inward orders on both sides: on the right these are the orders in \(\pi^{\mathrm{rev}}\). A first non-tight inward status on the right determines \(c\), exactly as one on the left determines \(p\). This makes the following arguments symmetric.

**Case \(\alpha=\beta=2\).** The families \(\mathcal L,\mathcal R\) consist of two-element sets and are cross-intersecting. Fix \(U\in\mathcal L\) and \(T\in\mathcal R\). Suppose \(b\ge8\). Choose a three-set \(C\subseteq B\setminus T\), and then a three-set
\[
D\subseteq B\setminus(U\cup C).
\]
The second choice is possible because \(|U\cup C|\le5\).

Place \(C\) first in \(B\), in an inward order with its internal triple non-tight. Its first pair avoids \(T\), so that pair is not a member of \(\mathcal L\), whatever left outside orders are used. Thus the status at \(s\) is tight, and the internal status at \(s+1\) is non-tight: \(p=s+1\). Place \(D\) at the right end, likewise with its inward internal triple non-tight. Its first inward pair avoids \(U\), so \(c=s+1\). The two placements are disjoint, producing a zero root. Hence \(b\le7\).

**Case \(\alpha=1,\beta=2\).** Let \(A\subseteq B\) be the nonempty set of singleton left witnesses and choose \(a\in A\). Every member of \(\mathcal R\) contains \(a\).

Suppose \(b\ge6\). Any three-set in \(B\setminus\{a\}\), placed inward at the right end with its internal triple non-tight, gives \(c=s+1\): its first pair cannot belong to \(\mathcal R\). Coordinate recurrence therefore supplies a chamber with \(p=s+1\).

Retain the first two \(B\)-vertices, in their order, and the left outside orders of this witness; denote their support by \(U\). They determine \(p=s+1\), because \(\ell=s+1\). Choose a three-set in
\[
B\setminus(U\cup\{a\}),
\]
which is possible for \(b\ge6\). Place it inward at the right end with non-tight internal triple. This again gives \(c=s+1\), independently of the left witness, a contradiction. Thus \(b\le5\). The case \(\alpha=2,\beta=1\) is symmetric.

**Case \(\alpha=\beta=1\).** Cross-intersection of the two nonempty singleton families implies that both are \(\{\{z\}\}\) for one vertex \(z\in B\). A witness for \(p=s\) must therefore start \(B\) with \(z\), and a witness for \(c=s\) must end \(B\) with \(z\). We do not assert that every choice of outside orders realizes either witness. Whenever the first \(B\)-vertex is different from \(z\), the status at \(s\) is tight for every outside order.

Define \(\mathcal L'\) to consist of supports of ordered pairs that occur as the first two \(B\)-vertices in some chamber with \(p=s+1\). Define \(\mathcal R'\) analogously for \(c=s+1\). Coordinate recurrence implies that either both families are empty or both are nonempty.

If both are empty and \(b\ge6\), choose disjoint three-sets at the two ends of \(B\). Order each inward so that its first vertex is not \(z\) and its internal triple is non-tight. This is always possible: if the set contains \(z\), put \(z\) in the middle and choose the appropriate order of the other two vertices. The statuses at \(s\) are tight; the statuses at \(s+1\) are tight because the pair families are empty; and the internal statuses at \(s+2\) are non-tight. Hence \(p=c=s+2\), a contradiction.

If both families are nonempty, they are cross-intersecting: disjoint ordered witnesses for \(p=c=s+1\) could again be combined with independent outside orders. Fix \(U\in\mathcal L'\) and \(T\in\mathcal R'\). If \(b\ge8\), choose disjoint three-sets
\[
C\subseteq B\setminus T,\qquad D\subseteq B\setminus U
\]
as in the first case. Order them inward with first vertex different from \(z\) and internal triple non-tight. The statuses at \(s\) are tight. Their first pairs avoid respectively \(T,U\), so cross-intersection excludes membership in \(\mathcal L',\mathcal R'\); the statuses at \(s+1\) are therefore tight for every outside order. Consequently \(p=c=s+2\), again a contradiction. Thus \(b\le7\).

This proves all three bounds in the table. Finally
\[
p+c\le m-1=2s+L-1,\qquad p,c\ge s
\]
gives \(p,c\le s+L-1\), completing the theorem.

### A finite reduction of the nonzero-cycle branch

Translate every coordinate by \(-s\). The exact-root digraph then uses at most seven coordinates, and every simple directed cycle has length at most seven.

There is also a bounded description in terms of actual vertices. Keep \(B\) and the complete outside blocks meeting the last two positions before \(B\) or the first two positions after it. Because exterior blocks have order at most two, at most three vertices are retained on either side. Thus at most
\[
7+3+3=13
\]
actual vertices affect the varying exact-root labels.

To verify this, the uniform statuses before \(s\) make those earlier tests irrelevant. The first potentially non-tight window on either side begins no earlier than two positions before \(B\). Moreover
\[
p\le n-s-3\le n-r-2,
\]
so the first non-tight window on the left ends within \(B\); the symmetric statement holds on the right. Hence all determining triples use the retained vertices. Orders of all other blocks may be fixed arbitrarily without changing the attainable root labels. Coordinate recurrence is preserved.

This is a uniform finite reduction of the nonzero exact-root face geometry. It does not identify the retained induced tournament as a counterexample, and it does not reduce the grand conjecture to tournaments of order thirteen.

If \(k=\kappa_2(H)>0\), a chamber with \(p=s\) satisfies
\[
k\le\delta(\pi)\le L-1\le6.
\]
Consequently a positive exact-root carrier in a tournament with \(k\ge7\) must contain a zero-root chamber.

### The remaining conversion

For a positively balanced exact-root face whose chambers all have positive deficiency, the proved alternative is now:
\[
\text{a chamber with }p=c
\quad\text{or}\quad
\text{the bounded central-block configuration above}.
\]
A zero root gives equally long canonical tight paths but may leave a nonempty hole. The bounded alternative likewise gives no spanning cover by itself. Neither branch can therefore be declared closed as a proof of the grand conjecture.

The new reduction uses the full ordered-partition freedom and coordinate recurrence. It repairs the earlier unjustified identification of the central block with its guaranteed corridor: their sizes need not be equal, but the exact determining windows restrict the surplus to zero, one, or two, and the case analysis bounds the entire block.


### Sharpening the central block bound to four

The preceding bound can be strengthened by using two-cover certificates as well as zero-root certificates. Keep its notation. Read the right side inward, so that its first non-tight coordinate is \(c\).

**Lemma (disjoint nonedges on five vertices).** Let \(E,F\) be nonempty families of two-element subsets of a five-element set, and suppose every member of \(E\) meets every member of \(F\). Then there are disjoint pairs \(e\notin E\), \(f\notin F\).

**Proof.** If not, for every two disjoint pairs \(e,f\), exactly one of \(e\in E\) and \(f\in F\) holds: both are excluded by cross-intersection, and neither is excluded by the supposition. Any two pairs sharing a vertex have a common disjoint pair, namely the remaining two vertices. Consequently membership in \(E\) is the same for any two pairs sharing a vertex. The line graph of the complete graph is connected, so \(E\) is either empty or all pairs. The first contradicts its nonemptiness, and the second forces \(F\) to be empty. \(\square\)

**Lemma (two triples on six vertices).** Let \(E,F\) be nonempty cross-intersecting families of pairs on a six-element set \(W\). Either there is a partition \(W=C\sqcup D\), with \(|C|=|D|=3\), such that
\[
|E\cap\binom C2|\le1,\qquad |F\cap\binom D2|\le1,
\]
or \(E\) and \(F\) are both the full star at the same vertex.

**Proof.** By symmetry, a family with at most two pairs may be taken to be \(F\). If \(F\) is one pair, put that pair in \(D\); its complement \(C\) contains no \(E\)-pair. If \(F\) consists of two disjoint pairs, every \(E\)-pair lies in their four-element union. Put the two remaining vertices and one vertex of that union in \(C\). If \(F=\{\{z,a\},\{z,b\}\}\), every \(E\)-pair either contains \(z\) or equals \(\{a,b\}\). Put \(z,a\) and one vertex outside \(\{z,a,b\}\) in \(D\). In each case the required inequalities follow.

Assume both families have at least three pairs. If one contains two disjoint pairs, the other is supported on their four-element union and is a subgraph of \(K_{2,2}\). With at least three edges it also contains disjoint pairs, so both families are supported on the same four vertices. Put two of those vertices and one exterior vertex in each triple.

Otherwise both families are pairwise intersecting. A pairwise-intersecting graph is a star or a triangle. If one is a triangle, the other must be that triangle, and splitting its vertices one versus two suffices. If both are stars, cross-intersection and their having at least three edges force a common center. Unless both stars are full, put the center and a missing neighbor in the triple assigned to a nonfull star, together with any other vertex. That triple contains at most one edge of its assigned star, while the other triple avoids the center. \(\square\)

Whenever a triple contains at most one forbidden pair, its two remaining pair edges have a common vertex. Use that vertex as the middle. Both reverse orders then have permitted first pairs, and boundary antisymmetry lets us choose either internal status.

**Theorem (four central vertices and the remaining cases).** Under the hypotheses of the bounded-central-block theorem, only the following cases can occur:
\[
\begin{array}{c|c|c}
(\ell,r)&|B|&L\\ \hline
(s+1,s+1)&2\text{ or }4&2\text{ or }4\\
(s+1,s)\text{ or }(s,s+1)&3&2.
\end{array}
\]
Thus the complete central block has at most four vertices. All varying root coordinates lie in \(\{s,s+1,s+2,s+3\}\), and at most ten actual vertices determine the root labels.

**Proof.** We give the exclusions in decreasing block size.

For \(\alpha=\beta=2\), use the pair families \(E=\mathcal L,F=\mathcal R\) at coordinate \(s\). For \(\alpha=\beta=1\), use \(E=\mathcal L',F=\mathcal R'\) at coordinate \(s+1\), with the distinguished singleton witness \(z\) from the preceding proof. In the latter case the two pair families are simultaneously empty or nonempty by coordinate recurrence. In either case, disjoint witnesses would give a zero root, so nonempty pair families are cross-intersecting.

**Seven vertices.** If the pair families are empty, two disjoint triples with non-tight internal status give a zero root, arranging \(z\) in the middle of its triple when necessary. Otherwise choose \(U\in E,T\in F\). If \(U\ne T\), they intersect in one vertex. There are disjoint triples \(C\subseteq B\setminus T\), \(D\subseteq B\setminus U\): put the unique vertex of \(U\setminus T\) in \(C\), the unique vertex of \(T\setminus U\) in \(D\), and split the four vertices outside \(U\cup T\) two and two. Their first pairs cannot be forbidden. Choose non-tight internal statuses to obtain \(p=c=s+1\) when \(\alpha=\beta=2\), or \(p=c=s+2\) when \(\alpha=\beta=1\). In the latter case make the first vertex different from \(z\), placing \(z\) in the middle if present.

If no unequal \(U,T\) exist, both families consist of the same single pair. Choose disjoint triples which separate the two vertices of that pair; each triple then has no forbidden pair. The same construction applies. Thus seven vertices are impossible.

**Six vertices.** Empty pair families again immediately give a zero root. Otherwise apply the six-vertex lemma. For \(\alpha=\beta=2\), a partition into two triples containing at most one forbidden pair each permits both internal statuses to be chosen non-tight; this gives \(p=c=s+1\).

For \(\alpha=\beta=1\), choose the permitted middle in each triple as explained after the lemma. In the triple containing \(z\), choose one of the two reverse orders whose first vertex is not \(z\). Choose the internal status of the other triple to match it. The earlier boundary tests on both sides are tight. If the matched status is non-tight, \(p=c=s+2\). If it is tight, append the two triples to the two inward outside paths. This is a spanning two-cover.

It remains to handle the common full star, at a vertex \(w\). For \(\alpha=\beta=2\), put \(w\) last in one inward triple. Its first pair avoids \(w\), and so do all pairs in the other triple. Match the internal status of the other triple to that of the first: a non-tight match gives a zero root, and a tight match gives a spanning two-cover.

For \(\alpha=\beta=1\), if \(w=z\), again put \(w\) last. If \(w\ne z\), use \((x,z,w)\) as the first inward triple, for any remaining vertex \(x\). Its first vertex is different from \(z\) and its first pair avoids \(w\). The other triple contains neither \(z\) nor \(w\), so both its reverse orders satisfy the boundary tests. Match its internal status to the first triple. The same zero-root or two-cover alternative follows. Thus six vertices are impossible.

**Five vertices, equal outside lengths.** Apply the five-vertex lemma to \(E,F\); if both are empty, simply choose any disjoint pairs. Put the resulting permitted pairs at the two inward ends of \(B\), filling the middle position arbitrarily.

If \(\alpha=\beta=2\), this gives \(p,c\ge s+1\). Here \(L=3\), so positive deficiency forces \(p+c\le2s+2\), and therefore \(p=c=s+1\).

If \(\alpha=\beta=1\), order each pair with first vertex different from \(z\). The tests at \(s\) and \(s+1\) are tight, giving \(p,c\ge s+2\). Here \(L=5\), and positive deficiency forces \(p+c\le2s+4\), so \(p=c=s+2\). Both conclusions contradict the absence of a zero root.

**Five vertices, unequal outside lengths.** By symmetry take \(\alpha=1,\beta=2\). Let \(A\) be the singleton left witness set. Every right witness pair contains all of \(A\), so \(1\le|A|\le2\).

Partition \(B=U\sqcup D\), with \(|U|=2,|D|=3\), so that \(U\) contains a vertex outside \(A\) and \(D\) contains no right witness pair. If \(A=\{z\}\), choose \(D\) avoiding \(z\). If \(A=\{z,w\}\), the right pair family is just \(\{\{z,w\}\}\); choose \(D\) with one of \(z,w\) and two of the three remaining vertices.

Read \(U\) from the left with its first vertex outside \(A\), so the status at \(s\) is tight. Fix any left outside orders and denote by \(\eta\) the status at \(s+1\). At the right, every order of \(D\) passes the boundary test at \(s\); choose its internal status to equal \(\eta\). If \(\eta=0\), the roots have \(p=c=s+1\). If \(\eta=1\), the outside paths extended by \(U,D\) form a spanning two-cover. Thus this case is impossible.

**Four vertices, unequal outside lengths.** Again take \(\alpha=1,\beta=2\). If \(A=\{z\}\), put two vertices other than \(z\) at the inward right end; put the remaining vertex other than \(z\) first at the left. If \(A=\{z,w\}\), put one vertex of \(A\) and one vertex outside \(A\) at the right, and start the remaining left pair with its vertex outside \(A\). In either case the first test on each side is tight, so \(p,c\ge s+1\). Since \(L=3\), positive deficiency forces \(p=c=s+1\), a contradiction.

**Four vertices with \(\alpha=\beta=2\).** Let \(E,F\) be the two boundary pair families. Any tight order of three \(B\)-vertices whose first pair is absent from \(E\) could be appended to the left outside path; the remaining \(B\)-vertex can be appended to the right outside path because all earlier statuses are uniformly tight. This would be a two-cover. The same argument applies with \(F\) on the right. Hence the first pair of every tight ordered triple of \(B\) belongs to
\[
G=E\cap F.
\]
For each middle vertex \(y\) and distinct endpoints \(x,z\), at least one of \(\{x,y\},\{y,z\}\) must therefore belong to \(G\), by boundary antisymmetry. The complement of \(G\) has maximum degree at most one, so \(G\) has at least four edges on the four vertices. But cross-intersection of \(E,F\) makes \(G\) pairwise intersecting, and a pairwise-intersecting graph on four vertices has at most three edges. This is a contradiction.

Since \(L\ge2\), these exclusions leave only \(b=3\) in the unequal-length case and \(b\in\{2,3,4\}\) when \(\alpha=\beta=1\).

**Three vertices with \(\alpha=\beta=1\).** Place the distinguished singleton witness \(z\) in the middle of \(B\). Both first tests are tight, so \(p,c\ge s+1\). Now \(L=3\); positive deficiency forces \(p=c=s+1\), a contradiction.

This proves the table. The coordinate bound follows from \(p,c\le s+L-1\). The earlier determining-block argument retains at most three exterior vertices on either side, so at most \(4+3+3=10\) actual vertices determine all varying roots. \(\square\)

### The distinguished vertex in the three-vertex case

In the unequal-length case, take \(\alpha=1,\beta=2\) by symmetry and retain the singleton witness set \(A\). It cannot have two vertices. If it did, let \(u\) be the third vertex of \(B\). The right pair family would be the unique pair \(A\). Choose a tight order of \(B\) with middle vertex \(u\); its first pair is not \(A\). The whole triple can then be appended to the right outside path, giving a two-cover together with the left outside path.

Hence \(A=\{z\}\). Both pairs incident with \(z\) must occur in the right witness family. Otherwise start \(B\) on the left with the remaining vertex different from \(z\), and put the missing right pair at the inward right end. This gives \(p,c\ge s+1\), incompatible with positive deficiency when \(L=2\). Thus the right pair family is the full star at \(z\).

Accordingly every remaining nonzero case has a distinguished actual vertex: in the two- and four-vertex cases both singleton witness families equal \(\{\{z\}\}\); in the three-vertex case one singleton family equals \(\{\{z\}\}\), and the opposite pair family is the full star at \(z\). These are statements about attainable witness supports, not assertions that every outside order realizes every witness.

Finally, if \(k=\kappa_2(H)>0\), a chamber with \(p=s\) has
\[
k\le\delta(\pi)\le L-1\le3.
\]
Thus for \(k\ge4\), every positively balanced exact-root carrier must contain a zero-root chamber. For general \(k\), the theorem reduces the nonzero branch to the three configurations in the table. Converting these configurations, or a zero-root chamber with a nonempty hole, into a spanning two-cover remains open.


### Only two- and three-cycles remain

Suppose in addition that every occurring exact root lies on a directed cycle, as it does under positive carrier balance. After subtracting \(s\) from the coordinates, every arc \(i\to j\) satisfies
\[
0\le i,j\le3,\qquad i\ne j,\qquad i+j\le3.
\]
Its underlying unordered pair is therefore one of
\[
\{0,1\},\ \{0,2\},\ \{0,3\},\ \{1,2\}.
\]
This graph is a triangle on \(0,1,2\) with one additional edge \(0\,3\). Consequently every simple directed cycle has length two or three, and every occurring arc lies on such a cycle. In particular, an arc using coordinate \(3\) forces its opposite arc. Thus the original coordinated-cycle question, away from zero roots, has no long-cycle case.


### Corollary: deletion distance at least two forces a zero exact root

Let
\[
k=\kappa_2(H)\ge2,
\]
and let \(F\) be a positively balanced exact-root carrier face. Then \(F\) contains a chamber with
\[
p=c.
\]

**Proof.**
Suppose not. Every chamber has positive deficiency, the occurring tail and head coordinate sets agree by positive exact-root circulation, and no chamber has zero root. The preceding four-central-vertices theorem therefore leaves only three possible nonzero configurations:
\[
(\ell,r,|B|,L)
=
(s+1,s+1,2,2),\quad
(s+1,s+1,4,4),
\]
or, up to left-right symmetry,
\[
(s+1,s,3,2).
\]

In either \(L=2\) case, a chamber with \(p=s\) has
\[
\delta\le L-1=1,
\]
contradicting the global lower bound
\[
\delta\ge\kappa_2(H)=k\ge2.
\]

It remains that
\[
\ell=r=s+1,\qquad |B|=L=4.
\]
The preceding distinguished-vertex conclusion gives one vertex \(z\in B\) such that every \(p=s\) witness starts \(B\) with \(z\), and every \(c=s\) witness ends \(B\) with \(z\). Choose a chamber whose first and last vertices of \(B\) are both different from \(z\). Then
\[
p,c\ge s+1.
\]
Since
\[
m=2s+4
\]
and every chamber has deficiency at least \(k\ge2\),
\[
2
\le
\delta
=
m-p-c
\le
(2s+4)-2(s+1)
=
2.
\]
Hence equality holds throughout:
\[
p=c=s+1,
\]
contradicting the assumption that \(F\) has no zero root. \(\square\)

Thus
\[
\boxed{
\kappa_2(H)\ge2
\quad\Longrightarrow\quad
\text{every positive exact-root carrier contains an actual balanced chamber }p=c.
}
\]

This conclusion is global and structural. It uses neither minimum-counterexample induction nor disturbance analysis. The remaining problem in the \(k\ge2\) branch is no longer recurrence without a diagonal; it is to exploit a balanced canonical partial two-cover
\[
P_\pi\mid X_\pi\mid Q_\pi,
\qquad
|P_\pi|=|Q_\pi|,
\qquad
|X_\pi|=\delta(\pi)\ge k,
\]
and, ideally, force one with \(|X_\pi|=k\).


---

## Section — Antipodal reachability and the neutral corridor

<!-- section_id: antipodal_reachability_and_neutral_corridor -->

### Exact reachability and the neutral corridor

### Reachability in the exactified memory lift

Return now to the auxiliary extension \(H^+\) from the fourth Section and work in the single memory-lift copy whose source color is \(1\). Orient every edge from lower rank to higher rank.

Let \(R\) be the set of states reachable from the source pole \(s\) by an increasing path using only color \(1\).

Because the antipodal involution reverses rank and complements color, the antipodal image \(A(R)\) has an exact dual interpretation.

**Proposition 6.** A state \(x\) lies in \(A(R)\) if and only if there is an increasing color-\(0\) path from \(x\) to the target pole \(t\).

**Proof.** A color-\(1\) increasing path from \(s\) to \(y\) maps under \(A\) to a color-\(0\) decreasing path from \(t\) to \(A(y)\). Reversing that path gives a color-\(0\) increasing path from \(A(y)\) to \(t\). The converse is the same argument reversed. \(\square\)

Hence
\[
\boxed{
R\cap A(R)\ne\varnothing
\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}.
}
\]

If
\[
x\in R\cap A(R),
\]
concatenate a color-\(1\) increasing path from \(s\) to \(x\) with a color-\(0\) increasing path from \(x\) to \(t\). Rank increases at every step, so the concatenation has pole distance and is automatically geodesic.

Together with auxiliary exactification,
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
R\cap A(R)\ne\varnothing.
}
\]

This is an exact state-space formulation of the original theorem.

### The neutral corridor

Assume
\[
R\cap A(R)=\varnothing
\]
and put
\[
N
=
V(\Gamma)\setminus\bigl(R\cup A(R)\bigr).
\]
Then
\[
A(N)=N.
\]

There is no increasing edge directly from \(R\) to \(A(R)\). Such an edge cannot have color \(1\), since its upper endpoint would then lie in \(R\). It cannot have color \(0\), since its lower endpoint would then have a color-\(0\) route through the upper endpoint to \(t\), placing it in \(A(R)\).

Every increasing pole-to-pole path starts in \(R\), ends in \(A(R)\), and therefore must meet \(N\). Such paths exist from the permutation construction, so \(N\ne\varnothing\). This is separation for increasing paths; the argument does not exclude an undirected edge whose lower endpoint is in \(A(R)\) and upper endpoint in \(R\).

The interface colors are forced:

- every increasing edge from \(R\) to \(N\) has color \(0\);
- every increasing edge from \(N\) to \(A(R)\) has color \(1\).

The antipode exchanges these two frontiers.

Thus failure produces an antipodally invariant set separating every increasing pole geodesic, with prescribed colors at the two directed interfaces. Conversely, disjointness of these particular reachability regions is exactly failure of the directed one-change target.

### Convex balance and actual intersection are different zeros

This distinction is the sharpest way to state the present frontier.

The root construction asks for a convex zero:
\[
0\in\operatorname{conv}\{\phi(\pi):\pi\in\mathcal C\}.
\]
Such a zero says that compressed extreme-defect vectors balance. Through the circulation criterion, it produces recurrence among switch fronts.

Reachability asks for an actual state-space intersection:
\[
x\in R\cap A(R).
\]
Such a point is not an average. It is one concrete memory state simultaneously reachable from the source by one color and from which the target is reachable by the other.

Therefore
\[
\boxed{
\text{root balance}
\neq
\text{reachability self-intersection}
}
\]
without an additional conversion theorem.

The unresolved topological problem may be phrased precisely as:

> Convert the multiplicity or recurrence forced by antipodal root topology into one actual state of the exactified memory lift lying in \(R\cap A(R)\), or into GN3-specific local structure that Articles III–VI can close.

This is more precise than asking vaguely for “a Borsuk–Ulam proof.”

### What a purely topological closure must preserve

Any theorem acting directly on the exactified memory lift must preserve three features simultaneously:

1. **distinguished poles:** the relevant antipodal pair is \(s,t\);
2. **geodesicity:** rank increases at every step, so no original label is reused;
3. **memory:** edge color records three successive cube directions.

A theorem producing an arbitrary antipodal path may fail the first two conditions. A theorem on ordinary cube-edge colorings may fail the third.

A universal directed one-change theorem for boundary tournaments would apply to the auxiliary extension. The undirected one-change conjecture permits either switch direction; it implies the grand conjecture by application to H itself and the cut-and-reverse construction. It does not automatically select the directed target in an individual extension.

Alternatively, work only with the auxiliary extensions and exploit their special vertex together with the consistent triple rule. Antipodal symmetry of arbitrary chamber words alone does not encode that rule.

### How the older topology fits

The earlier Tucker, root, and Bourgin–Yang programs should now be interpreted as candidate mechanisms for attacking the corridor.

- Tucker sought a local complementary state.
- Cellular root topology replaced one complementary edge by balanced recurrence.
- Bourgin–Yang sought enough balanced recurrence to make avoidance impossible.
- GN3-specific compression seeks to turn recurrence into a local reversal or support.

The reachability picture supplies the exact endpoint of that program: all of those mechanisms are useful only insofar as they force
\[
R\cap A(R)\ne\varnothing
\]
or a combinatorial contradiction to the existence of \(N\).

This is the exact topological frontier.


### Further developments

### Nearest-violation Tucker labeling

Work in the auxiliary extension (H^+) with distinguished vertex (r). Assume there is no directed one-change spanning order. For a spanning order (pi), let (x_d(pi),y_d(pi)) denote the left-zero and right-one violation indicators at equal distance (d) from (r), as in [[auxiliary_violation_vector_has_exact_chamber_zeros]]. Fix distinct original vertices (a,b) and use the antipodal gauge
[
g_{ab}(pi)=
egin{cases}
+1,&a	ext{ precedes }b,\
-1,&b	ext{ precedes }a.
end{cases}
]
Set
[
F_d(pi)=x_d(pi)-y_d(pi)+g_{ab}(pi)x_d(pi)y_d(pi).
]
Then (F(pi^{m rev})=-F(pi)), and (F(pi)
e0) for every chamber under the present assumption.

Let
[
d(pi)=min{d:F_d(pi)
e0}
]
and define the signed-basis label
[
ell(pi)=operatorname{sgn}(F_{d(pi)}(pi)),e_{d(pi)}.
]
Reversal preserves the distance index and negates the sign, so
[
ell(pi^{m rev})=-ell(pi).
]

If (H) has (n) original vertices, then (H^+) has (n+1) vertices. The centered permutahedron of (H^+) has boundary (S^{n-1}). There are at most (n-2) nontrivial violation distances, so the labels lie in (mathbb R^{n-2}).

For each nonempty proper permutahedron face (C), assign its barycenter the average
[
L(z_C)=rac1{|mathcal V(C)|}sum_{piinmathcal V(C)}ell(pi),
]
and extend affinely over the barycentric subdivision. This gives a continuous odd map
[
L:S^{n-1}	omathbb R^{n-2}.
]
Bourgin--Yang therefore gives
[
dim L^{-1}(0)ge1.
]

Exactly as in the positive-carrier argument for the root maps, every zero has a carrier face (C) and strictly positive coefficients
[
lambda_pi>0qquad(piinmathcal V(C))
]
with
[
sum_{piinmathcal V(C)}lambda_piell(pi)=0.
]

Because the labels are signed basis vectors, coordinate balance is completely explicit.

**Proposition.** For every distance (d) that occurs among the labels of chambers of (C), both (+e_d) and (-e_d) occur among the chamber labels of (C).

**Proof.** In coordinate (d), the positive relation reads
[
sum_{ell(pi)=+e_d}lambda_pi
=
sum_{ell(pi)=-e_d}lambda_pi.
]
If one sign occurs, the corresponding side is positive, so the other side is positive as well. (square)

Let
[
d_0=min{d(pi):piinmathcal V(C)}.
]
Then every chamber of (C) has no violation at any distance (<d_0), while (C) contains chambers labeled (+e_{d_0}) and (-e_{d_0}).

Thus the topological output is no longer a diffuse convex recurrence. It is one ordered-partition face on which all chambers share a common protected radius around (r), and at the first distance where any violation can occur both left and right signs are realized.

### Protected windows force thin blocks

Write the carrier face as an ordered partition
[
C=B_1|cdots|B_k,
]
and let (B_j) be the block containing (r).

For every chamber of (C), every left or right status window at distance (<d_0) from (r) has its prescribed one-change color. Therefore none of those three-position windows can lie wholly in one block of (C): if such a window lay in one block, swapping its first and third vertices would stay in (C) and boundary antisymmetry would flip its status, producing a closer violation in one of the two chambers.

In particular:

**Corollary.** If (d_0ge2), then
[
|B_j|le3.
]

**Proof.** If (|B_j|ge4), choose a chamber in which (r) is last inside (B_j) and three other vertices of (B_j) occupy the three positions immediately preceding (r). Those three positions form the left status window at distance (1<d_0). It is required to be tight in every chamber of (C). Swapping its first and third vertices produces another chamber of (C) in which that triple is its boundary flip and hence non-tight, contradiction. (square)

More generally, every protected three-position window within distance (d_0-1) from (r) must straddle a block boundary of (C). Thus a large protected radius forces a dense sequence of ordered-partition boundaries near (r).

This gives a new global structural alternative:

- either a directed one-change chamber exists, hence a two-cover of (H);
- or there is a proper permutahedron face with a common protected radius, paired opposite nearest-violation labels at the first bad distance, and locally thin ordered-partition blocks around the auxiliary vertex.

The conclusion uses no minimum-counterexample hypothesis and no disturbance analysis.

---

## Section — Synthesis and the exact topological frontier

<!-- section_id: article_vii_synthesis_and_exact_frontier -->

### Exact formulations and the pre-compression frontier

### The exact equivalence chain

The purpose of Article VII is not to replace the local GN3 theory of Articles I–VI. It is to identify the global obstruction geometrically and to translate the original conjecture into exact antipodal models.

The exact chain is
\[
\boxed{
\begin{aligned}
\operatorname{pc}(H)\le2
&\iff
\exists\pi\text{ whose defect intervals admit one common cut}\\
&\iff
H^+\text{ has a directed one-change spanning order}\\
&\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}\\
&\iff
\text{the rooted complementary-support condition holds}\\
&\iff
R\cap A(R)\ne\varnothing.
\end{aligned}}
\]

The first line is the quantified defect-Helly theorem. The second is auxiliary exactification. The third is the memory lift. The fourth is the opposite-edge/common-terminal support dictionary normalized at \(r\). The fifth is the reachability criterion.

Every arrow in this chain is exact.

### What topology currently supplies

The root-topological route does not yet prove one of these exact conditions directly. What it supplies is structure:

- the Coxeter sphere of spanning orders;
- antipodal extreme-switch labels;
- cellular square and braid-hexagon constraints;
- the odd root map
  \[
  \phi(\pi)=e_a-e_{\bar b};
  \]
- balanced faces and directed root circulations;
- potentially positive-dimensional balanced loci via Bourgin–Yang;
- block separation, giant-block recurrence, cross-intersection, and front motion.

These are genuine mathematical outputs. They should not be discarded merely because they stop one step short of the theorem.

But they are compressed outputs. The exact target remains one concrete intersection or one exact complementary-support state.

### Route A: prove the stronger one-change conclusion

The candidate from the second Section asks whether every boundary tournament has a spanning order with at most one color change. A reversal-complement function on ordered triples is exactly a boundary tournament, so the candidate concerns the same input class with a stronger desired conclusion.

If this candidate holds, apply it to \(H\) itself and split into monochromatic blocks, reversing the non-tight block. This gives a two-cover. A universal theorem specifically producing \(1^a0^b\) could instead be applied to \(H^+\) and Theorem 3. Reversal preserves the direction of the switch, so these two reductions must be distinguished.

The one-change sufficient condition also gives a tight path on at least \(\lceil(n+2)/2\rceil\) vertices. This quantitative consequence, the endpoint involution including singleton paths, and the positive square-zero enumeration remain part of the support formulation.

A genuinely broader input class is provided by the base-dependent memory rule in the second Section. Any theorem about that class would need a separate proof and a precise reduction.

### Route B: prove only the exact auxiliary target

The alternative is to prove directed one-change existence only for the extensions \(H^+\). This is exactly equivalent to the grand conjecture. One may use the forced endpoint behavior of the auxiliary vertex and the local tournament structure supplied by the triple rule.

Articles I–VI develop deletion-cover compatibility, quadratic-potential descent, defect-line compression, endpoint transport, longest-path reversal structure, and equal-potential recurrence. Article VII seeks to turn topological balance into hypotheses to which those arguments apply. Neither balanced roots nor a moved switch front alone establishes that the full hypotheses of a closing repartition are satisfied.

These are two routes distinguished by the strength of the conclusion and by whether the auxiliary vertex is used, not by a nonexistent distinction between boundary tournaments and reversal-complement triple functions.

### The apparent exact-reachability conversion

Before the minimum-span compression of Section 7, the natural missing implication was
\[
\boxed{
\text{balanced or recurrent extreme-switch data}
\quad\Longrightarrow?\quad
R\cap A(R)\ne\varnothing.
}
\]

That implication is still not proved, and proving it directly would prove the grand conjecture. The neutral-corridor formulation therefore remains a valid optional route to the theorem.

It is no longer, however, the frontier of Article VII. Section 7 shows combinatorially that the recurrence needed to support the balanced face already collapses to bounded local GN3 structure: one minimizes switch span and transports one physical carrier to both extreme fronts. The explicit Bourgin--Yang dimension bound remains a genuine topological statement, but no further conversion of its zero set into a reachability intersection is required for the geodesic investigation itself.

### A cyclic guardrail

One attractive strengthening should be recorded only as a warning.

It is sufficient to find a spanning cyclic order whose transition-color word has at most two monochromatic components, but this is not necessary for a two-cover. There are edge-orderable boundary tournaments with
\[
\operatorname{pc}(H)=2
\]
for which every spanning cycle has at least four monochromatic transition components.

The correct cyclic invariant is not the number of runs.

For an oriented Hamilton cycle
\[
Z=(v_1,\ldots,v_n,v_1),
\]
let the cycle-edge positions be
\[
e_i=\{v_i,v_{i+1}\}.
\]
Construct a defect graph \(D_Z\) on these positions by joining
\[
e_{i-1},e_i
\]
exactly when
\[
(v_{i-1},v_i,v_{i+1})
\]
is non-tight.

A set of cut edges turns the cycle into tight inherited paths exactly when it meets every edge of \(D_Z\). Therefore
\[
\operatorname{pc}(H)
=
\min_Z\max\{1,\tau(D_Z)\}.
\]

In particular,
\[
\operatorname{pc}(H)\le2
\iff
\exists Z\text{ with }\tau(D_Z)\le2.
\]

This exact cyclic formulation may still be useful, but the false two-component-cycle strengthening is not part of the main route.

### Article thesis

Article VII retains the exact Helly, auxiliary-geodesic, complementary-support, and directed-reachability formulations, together with the Coxeter geometry, the failure of graph-only labeling arguments, the explicit barycentric root construction, Bourgin--Yang multiplicity, and carrier-face recurrence.

Its specifically geodesic contribution is now complete at the correct level: recurrent nonzero face geometry and global minimum switch span eliminate every unbounded permutahedral obstruction and hand the problem to bounded local GN3 structure. The article does **not** prove the grand two-cover conjecture, and it does not claim the exact intersection \(R\cap A(R)\ne\varnothing\). Those stronger statements remain equivalent or sufficient routes to the global theorem, while the false cyclic two-component strengthening stays excluded by the balanced-cut obstruction above.


### Closure: width-three mixed-end handoff


### Article VII closure theorem

The exact formulations established earlier remain unchanged:
\[
\operatorname{pc}(H)\le2
\]
is equivalent to the defect-Helly cut condition, to a directed \(1^*0^*\) order in the auxiliary exactification, to the corresponding directed one-change pole geodesic, to the complementary-support formulation, and to
\[
R\cap A(R)\ne\varnothing
\]
in the exact memory lift.

The new compression in Section 7 changes the role of the topological route. It is no longer necessary to synchronize an arbitrary collection of balanced face witnesses into one global reachability state.

**Theorem 9.1 (geodesic compression to a local GN3 interface).** If a boundary \(3\)-tournament \(H\) has no spanning two-cover, then a globally minimum-switch-span spanning order has one of the following forms:

1. its switch span \(d\) satisfies \(3\le d\le5\), and it yields a spanning three-cover with a middle component of order \(d-2\le3\);
2. \(d\ge6\), and \(H\) contains a Hamiltonian support of order four or five.

Moreover, for the positively balanced carrier face of Theorem 6.1, the same conclusion already holds on every non-diagonal recurrent branch: minimum span within the face and one physical carrier eliminate the giant-block/front-motion residue.

Thus all unbounded permutahedral behavior has disappeared. The exact reachability formulation remains mathematically equivalent to the conjecture, but the topology no longer carries an independent unresolved global obstruction.

### Minimum counterexamples have exact width three

There is a sharper consequence in the setting relevant to the grand conjecture.

**Corollary 9.2.** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then the minimum switch span over all spanning orders of \(H\) is exactly three.

**Proof.** Fix \(x\in V(H)\). By minimality,
\[
H-x=P\mid Q
\]
for two tight paths \(P,Q\). Insert \(x\) between their displayed orders:
\[
P,\ x,\ Q.
\]
Every status except the three junction statuses meeting \(x\) is inherited from \(P\) or \(Q\) and is tight. Hence all switches lie across a window of three consecutive variable statuses, so the first-to-last switch span is at most three.

A counterexample has no spanning order with at most one switch, and Lemma 7.5 excludes switch span at most two. Therefore the global minimum is exactly three. \(\square\)

For a minimum-span order with
\[
b=a+3,
\]
Lemma 7.6 becomes especially concrete:
\[
L\mid\{z\}\mid R,
\qquad
z=v_{a+3},
\]
where \(L\) and \(R\) have tight orientations.

The first-switch condition says that \(z\) reverses one exposed end edge of the tight-oriented \(L\); the last-switch condition says that the same \(z\) reverses one exposed end edge of the tight-oriented \(R\). Let \(\alpha,\omega\) be the first and last status colors.

- If \(\alpha\ne\omega\), the two reversals have the same endpoint type. Since the two exposed edges are disjoint, the common-reverser argument gives a Hamiltonian four-support.
- If \(\alpha=\omega\), the reversals have mixed endpoint type. Writing the tight-oriented exposed edges, up to symmetry, as
  \[
  \ldots,a_0,a_1
  \qquad\text{and}\qquad
  p_1,p_2,\ldots
  \]
  gives
  \[
  (z,a_1,a_0),\qquad(p_2,p_1,z)
  \]
  tight. Exactly one of
  \[
  (p_1,z,a_1),\qquad(a_1,z,p_1)
  \]
  is tight. The first gives the Hamiltonian five-path
  \[
  (p_2,p_1,z,a_1,a_0),
  \]
  while the second is the parallel-middle relation
  \[
  (a_1,z,p_1)\ \text{tight}.
  \]

Therefore the geodesic route has a single genuinely local terminal form after bounded Hamiltonian supports are separated off:

\[
\boxed{
\text{width-three singleton carrier with mixed-end parallel-middle data}.
}
\]

This is precisely a local GN3 configuration, not an antipodal-topology problem.

### Final status of the two topological formulations

The root-space formulation and the exact reachability formulation now have different roles.

The root-space topology is **closed as a compression mechanism**: positive balance on every chamber, block separation, and minimum-span carrier transport reduce every nonzero recurrent branch to a two-cover or bounded local structure, while global minimum span absorbs the diagonal branch.

The exact reachability statement
\[
R\cap A(R)\ne\varnothing
\]
remains an exact reformulation of the grand conjecture, not an independently proved theorem. A direct topological proof of that intersection would still solve the conjecture, but Article VII no longer needs such a proof in order to finish its own geodesic investigation. Any hypothetical failure is already compressed to the width-three local interface above.

Accordingly, no further continuation of the antipodal-geodesic, carrier-face, Tucker/Ky Fan, Bourgin--Yang, or neutral-corridor machinery is presently justified. The unresolved mathematics lies in the local GN3 handoff, which belongs to the other articles' path-cover and small-support arguments rather than to Article VII.


### Exact-deficiency sharpening of the terminal handoff


### Exact-deficiency sharpening of the terminal handoff

The exact inversion-window coordinates sharpen the minimum-counterexample conclusion one final step. For
\[
\delta(\pi)=q(\pi)-p(\pi)-1,
\]
the exact criterion of Section 1 says that \(\delta\le0\) is already a two-cover certificate. If \(H\) is a minimum counterexample and
\[
H-x=P\mid Q,
\]
then the order
\[
(P,x,Q^{\rm rev})
\]
has all statuses away from the three \(x\)-junctions equal to \(1\) on the left and \(0\) on the right. Hence \(\delta\le1\); counterexamplehood forces
\[
\delta=1.
\]

The deficiency-one canonical partial cover from Section 6 therefore has a single hole, namely \(x\). Its two displayed tight paths are exactly \(P\) and \(Q\), and \(x\) reverses the terminal edge of both. A common terminal-edge reverser of two disjoint tight paths gives a Hamiltonian four-support. By minimum-counterexample induction its complement is non-Hamiltonian with path-cover number exactly two.

Accordingly the sharp terminal statement of Article VII is
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support }K
\text{ with }\operatorname{pc}(H-K)=2
\text{ and }H-K\text{ non-Hamiltonian}.
}
\]

This strictly sharpens the earlier width-three \(4/5\)-support or mixed-end description. The width-three and recurrent-face theorems remain the correct global compression statements for an arbitrary no-two-cover boundary tournament; the exact-deficiency argument is the stronger endpoint available after minimum-counterexample induction.

It also resolves the specific synchronization question raised by the coordinated-face program at the level needed by this article. One may still study directed cycles of exact roots, but Article VII does not need to turn a whole cycle into one reachability intersection. The exact inversion coordinate collapses a minimum counterexample to a one-hole deletion cover before that synchronization is necessary, and the one hole already forces the canonical four-support handoff.

The direct reachability assertion
\[
R\cap A(R)\ne\varnothing
\]
remains equivalent to the grand conjecture and is not proved here. Article VII is closed more modestly and more sharply: the global geodesic/topological obstruction has been eliminated, and the surviving minimum-counterexample state is a single bounded four-support interface.


### The remaining face-to-cover conversion

### Current status of the face-to-cover conversion

The earlier descriptions in this Section of Article VII as closed, and the assertion that no further topological continuation is justified, are superseded by the following precise status. The small-support compression results do not prove a two-cover and do not prove that every obstruction to the grand conjecture has been eliminated. The exact reachability intersection remains unproved.

The bounded-central-block theorem in [[topological_recurrence_to_local_gn3_structure]] gives a uniform reduction within Article VII itself. For a positively balanced exact-root carrier whose chambers all have positive deficiency, either a zero-root chamber occurs or its nonzero-root geometry has one central block of order at most four, exterior blocks of order at most two, at most four consecutive root coordinates, and at most ten actual vertices determining the varying root labels after irrelevant exterior block orders are fixed. The proof uses ordered-partition block freedom and boundary antisymmetry, not minimum-counterexample or disturbance arguments.

This is a finite reduction of one face-geometric branch, not a reduction of the grand conjecture to order ten. Two conversion problems remain. In the diagonal branch, p=c gives equal canonical path lengths but can leave a nonempty hole. In the non-diagonal branch, bounded determining data still have to produce a spanning cover or force a useful change of face.

### Rooted omission vectors

For a spanning order (pi=(L,r,R)) of the auxiliary extension, let (P_pi) be the longest suffix of (L), followed by (r), that is a tight path. Let (Q_pi) be the corresponding rooted path on the right, obtained from the longest initial segment of (R) whose reversal followed by (r) is tight. Define
[
A(pi)=V(L)setminus V(P_pi),qquad
B(pi)=V(R)setminus V(Q_pi),
]
and
[
D(pi)=mathbf 1_{A(pi)}-mathbf 1_{B(pi)}.
]
Reversal exchanges (A) and (B), so (D(pi^{m rev})=-D(pi)). Also (D(pi)=0) exactly when the two rooted tight tails cover every original vertex, which by auxiliary exactification is exactly a spanning two-cover of (H).

Along the chamber order every (D(pi)) has signed threshold form
[
+cdots+,0cdots0, -cdots-.
]
It is never identically positive or identically negative, because an original vertex adjacent to (r) belongs to a two-vertex tight path with (r).

### A dimension-tight quotient map

Let (n=|V(H)|). The boundary of the centered permutahedron on (H^+) is (S^{n-1}). Project the omission vector to
[
mathbb R^{V(H)}/langlemathbf1angle,
]
which also has dimension (n-1). Averaging projected omission vectors on every proper face and extending affinely over the barycentric subdivision gives a continuous odd map. Borsuk--Ulam therefore gives a zero. Its carrier face (F) has strictly positive chamber weights satisfying
[
sum_{piinmathcal V(F)}lambda_pi D(pi)=c,mathbf1
]
for some scalar (c).

This yields a sharper structural frontier:

**Facewise omission-balance problem.** If a proper permutahedral face admits a strictly positive convex combination of rooted omission vectors equal to a constant vector, must it contain a chamber with (D(pi)=0)?

A positive answer proves the two-cover conjecture directly through auxiliary exactification, without minimum-counterexample or disturbance arguments. The extra structure is that each chamber label is a signed prefix/suffix threshold vector of actual omitted vertices and all chambers of (F) arise by independent permutations inside ordered face blocks. The remaining task is therefore an uncrossing or face-convexity problem for threshold omissions inside one ordered partition, not a generic convex-cancellation problem.

The sharper theorem leaves only a two- or four-vertex central block with two singleton witness families supported on the same vertex \(z\), or a three-vertex block with a singleton witness \(\{z\}\) on one side and the full star at \(z\) as the opposite pair family. Moreover, every simple directed root cycle has length two or three. The proof of these sharper bounds sometimes converts a matched pair of tight triples directly into a spanning two-cover; it is therefore stronger than a zero-root argument alone.

The remaining nonzero cases have global deletion distance at most three. This is a consequence under the no-zero-root face hypothesis, not a universal bound on \(\kappa_2(H)\).


### Localization of omission balance and the two exceptional facets

The facewise omission-balance question above has a precise exception. Let the auxiliary vertex be \(r\), let \(V=V(H)\), and use the rooted omission vectors \(D(\pi)\) just defined. In the chamber order their entries on original vertices have the form
\[
+\cdots+,\,0\cdots0,\,-\cdots-.
\]
In particular, if original vertices \(u,v\) lie in distinct ordered face blocks with the block of \(u\) earlier, then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber of that face.

**Proposition (localization to the two exceptional facets).** Let \(F\) be a proper face of the permutahedron on \(V\cup\{r\}\). Suppose
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi D(\pi)=c\mathbf1,
\qquad \lambda_\pi>0,\quad \sum_\pi\lambda_\pi=1.
\]
If \(F\) is neither \(\{r\}\mid V\) nor \(V\mid\{r\}\), then \(D(\pi)=0\) for every chamber of \(F\).

**Proof.** If original vertices occur in at least two face blocks, the displayed coordinate inequality and equality of coordinate averages imply
\[
D(\pi)_u=D(\pi)_v
\]
for every chamber and every pair in different original-vertex blocks. Positivity of every coefficient is essential here. Using any vertex in a second block also equates two coordinates in the same block. Thus every chamber vector is constant on all original vertices.

At least one original vertex is adjacent to \(r\) in each chamber and belongs to a rooted tight path of order two. Its omission coordinate is zero. Therefore the constant vector is zero.

If all original vertices occur in one block, a proper face can have only that block and the singleton block \(\{r\}\), in either order. These are exactly the two excluded facets. \(\square\)

Thus, under the assumption that \(H\) has no two-cover, every zero of the projected omission map must have one of the two exceptional facets as its carrier. The Borsuk--Ulam conclusion by itself does not exclude this possibility.

**Example (the exceptional facets really can balance).** Identify four original vertices with \(\mathbb F_2^2\). Order the three nonzero differences as \(d_1<d_2<d_3\), and give the ordinary edge \(\{x,y\}\) the class of \(x+y\). Declare
\[
(x,y,z)\text{ tight}\quad\Longleftrightarrow\quad
\operatorname{class}(x+y)<\operatorname{class}(y+z).
\]
The two classes are different, so boundary reversal complements tightness. This is the matching-block boundary tournament.

It has no tight Hamilton path. Such a path would have three successive, strictly increasing edge classes, hence differences \(d_1,d_2,d_3\). Their sum is zero in \(\mathbb F_2^2\), so its final vertex would equal its initial vertex. This contradicts distinctness. It does, of course, have a two-cover by two pairs.

On the facet \(\{r\}\mid V\), the left rooted path is the singleton \(r\). The right rooted path covers either two or three original vertices; it never covers four because that would give a tight Hamilton path of \(H\). Hence no chamber of this facet has \(D=0\).

Translations of \(\mathbb F_2^2\) preserve edge classes and act transitively on original vertices. The uniform average of \(D\) over all chambers of this facet is therefore a constant vector. Exactly half the orders have a non-tight first original triple, allowing the reversed rooted prefix to cover three original vertices; the other half cover only two. Thus the average number omitted is \(3/2\), and
\[
\frac1{4!}\sum_{\pi\in\mathcal V(\{r\}\mid V)}D(\pi)
=-\frac38\mathbf1.
\]
All weights are strictly positive. Reversal gives the opposite constant on \(V\mid\{r\}\).

This refutes the universal facewise implication proposed above: strictly positive projected omission balance need not yield a zero chamber in the same face. It does not refute the grand conjecture. The viable strengthened target is to force a projected zero outside the two exceptional facets, or to extract a two-cover directly from balance on an exceptional facet. The localization proposition proves the first target sufficient; the example shows why the second cannot demand a Hamilton path.


### Facewise omission balance collapses to the two extreme auxiliary facets

Retain the rooted omission notation
\[
D(\pi)={\bf1}_{A(\pi)}-{\bf1}_{B(\pi)}
\]
on spanning orders \(\pi=(L,r,R)\) of \(H^+\). Thus \(A(\pi)\) is a prefix of \(L\), \(B(\pi)\) is a suffix of \(R\), and \(D(\pi)=0\) is exactly a two-cover certificate for \(H\).

Let
\[
F=C_1|\cdots|C_t
\]
be a nonempty proper permutahedron face, and suppose \(r\in C_j\). Assume there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(F)),\qquad
\sum_\pi\lambda_\pi=1,
\]
such that
\[
\sum_\pi\lambda_\pi D(\pi)=c\,{\bf1}
\]
for some scalar \(c\).

**Theorem (facewise omission reduction).**
If \(F\) is not one of the two extreme facets
\[
\{r\}|V(H),
\qquad
V(H)|\{r\},
\]
then \(F\) contains a chamber \(\pi\) with
\[
D(\pi)=0.
\]
In fact, except for a terminal two-block configuration with the auxiliary block containing original vertices, the argument forces \(D=0\) in every chamber of \(F\); that remaining terminal configuration also collapses by the probability argument below.

**Proof.**

First suppose
\[
1<j<t.
\]
Every original vertex in a block before \(C_j\) is always left of \(r\), hence its \(D\)-coordinate is in \(\{0,1\}\). Every original vertex in a block after \(C_j\) has coordinate in \(\{0,-1\}\). Since all weighted coordinate averages equal \(c\), both sides force
\[
c=0.
\]
Strict positivity of all \(\lambda_\pi\) then implies that every original vertex outside \(C_j\) has \(D\)-coordinate \(0\) in every chamber.

If some chamber had \(A(\pi)\ne\varnothing\), then, because \(A(\pi)\) is a prefix of \(L\) and there is a whole face block before \(C_j\), the first original vertex of the chamber would lie in \(A(\pi)\), contradicting its identically zero coordinate. Hence \(A(\pi)=\varnothing\) for every chamber. The symmetric suffix argument gives \(B(\pi)=\varnothing\). Thus every chamber has \(D=0\).

Now suppose \(j=1\); the case \(j=t\) is symmetric. Every original vertex outside \(C_1\) has coordinate in \(\{0,-1\}\), so
\[
c\le0.
\]
If \(c=0\), strict positivity makes every outside coordinate identically zero. A nonempty suffix \(B(\pi)\) would contain the last original vertex of the chamber, which lies outside \(C_1\), a contradiction. Thus \(B(\pi)=\varnothing\) for every chamber. The remaining coordinates are then nonnegative, have average zero, and hence \(A(\pi)=\varnothing\) as well.

Assume therefore
\[
c=-W<0.
\]

If \(C_1\ne\{r\}\), choose
\[
x\in C_1-\{r\}.
\]
Let \(E\) be the event, under the positive weights \(\lambda\), that every original vertex outside \(C_1\) belongs to \(B(\pi)\), and write its total weight as \(e\).

For every outside vertex \(y\),
\[
D_y=-{\bf1}_{\{y\in B\}},
\]
so its average \(-W\) gives
\[
\Pr_\lambda(y\in B)=W.
\]
Since \(E\subseteq\{y\in B\}\),
\[
e\le W.
\]

Write
\[
a_x=\Pr_\lambda(x\in A),
\qquad
b_x=\Pr_\lambda(x\in B).
\]
If \(x\in B(\pi)\), the suffix property forces every later outside vertex into \(B(\pi)\), hence
\[
\{x\in B\}\subseteq E
\]
and therefore
\[
b_x\le e.
\]
The balance equation at coordinate \(x\) is
\[
a_x-b_x=-W,
\]
so
\[
b_x=a_x+W\ge W.
\]
Consequently
\[
W\le b_x\le e\le W.
\]
Thus
\[
a_x=0,\qquad b_x=e=W.
\]

The same argument holds for every \(x\in C_1-\{r\}\). Hence on every chamber in \(E\), all original vertices of \(C_1\) and all outside vertices belong to \(B(\pi)\): every original vertex of \(H\) is omitted on the right. This is impossible, because whenever \(R\ne\varnothing\), the first vertex of \(R\) together with \(r\) is a two-vertex tight path, so the rooted right path \(Q_\pi\) always contains at least that vertex.

Thus \(c<0\) is impossible whenever \(C_1\ne\{r\}\).

It remains only
\[
C_1=\{r\}.
\]
If \(t\ge3\), choose vertices \(u\in C_i\), \(v\in C_j\) with
\[
2\le i<j\le t.
\]
Because \(B(\pi)\) is a suffix of \(R\),
\[
{\bf1}_{\{u\in B\}}\le{\bf1}_{\{v\in B\}}
\]
in every chamber. Their weighted expectations are both \(W\), so strict positivity forces equality chamberwise. Varying \(u,v\) shows that in every chamber either every original vertex is in \(B\) or none is. The former is impossible by the immediate-neighbor observation, while the latter contradicts \(W>0\).

Therefore the only unresolved case with \(j=1\) is
\[
F=\{r\}|V(H).
\]
The symmetric argument leaves only
\[
F=V(H)|\{r\}.
\]
This proves the theorem. \(\square\)

### The reduction is sharp at the level of convex cancellation

The two exceptional facets cannot be discarded by a generic convexity argument. On the facet
\[
\{r\}|V(H),
\]
one has
\[
D(\pi)=-{\bf1}_{B(\pi)},
\]
where \(B(\pi)\) is the suffix omitted after the maximal rooted right path.

For a standard non-Hamiltonian four-vertex matching-block boundary tournament, the uniform distribution on all \(24\) permutations gives
\[
\Pr(v\in B)=\frac38
\]
for every vertex \(v\), while no permutation has \(B=\varnothing\). Thus
\[
\frac1{24}\sum_\pi D(\pi)
=
-\frac38\,{\bf1}
\]
is a genuine full-support constant balance with no zero chamber.

Accordingly, the facewise omission theorem is sharp:
\[
\boxed{
\text{all non-extreme carrier faces close;}
\quad
\text{the only genuine convex-cancellation residue is the pair of extreme facets.}
}
\]

The remaining global topological question is therefore whether an odd zero of the quotient omission map can be supported entirely by those two antipodal extreme facets when the whole tournament has no two-cover. Local averaging alone cannot answer this.

### The exceptional facets carry essential degree

The matching-block example above shows that the two exceptional facets can support projected omission balance without a zero chamber. In a hypothetical counterexample, the limitation is stronger: the projected omission map is topologically forced to have a zero in the interior of each exceptional facet.

Let
\[
F^-=\{r\}\mid V(H)
\]
be the left exceptional facet. It is canonically a copy of the centered permutahedron \(P_V\) on the original vertex set, of dimension \(n-1\). Its boundary is therefore an \((n-2)\)-sphere.

On \(F^-\), every omission vector has the form
\[
D(\pi)=-\mathbf 1_{B(\pi)},
\]
where \(B(\pi)\) is a suffix of the original-vertex order. Hence, if
\[
G=B_1|\cdots|B_t
\]
is any proper face of \(P_V\), and \(u\in B_i,\ v\in B_j\) with \(i<j\), then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber \(\pi\) of \(G\). The same inequalities hold for the face-average omission vector assigned to the barycenter of \(G\), and therefore throughout every barycentric simplex whose largest face is \(G\).

Write
\[
Q=\mathbb R^{V(H)}/\langle\mathbf 1\rangle
\]
and, for an ordered partition \(G\), let
\[
C_G=
\left\{
[y]\in Q:
y_u\ge y_v
\text{ whenever }
u\in B_i,\ v\in B_j,\ i<j
\right\}.
\]
Thus the projected omission map on the barycentric subdivision of \(\partial P_V\) is carried by the spherical carrier
\[
K_G=(C_G\setminus\{0\})/\mathbb R_{>0}.
\]

Assume now that \(H\) has no spanning two-cover. By the facewise omission theorem above, the projected omission map has no zero on \(\partial F^-\): any zero there would have a proper nonexceptional carrier face in the full auxiliary permutahedron and would force an actual chamber with \(D=0\).

Each \(K_G\) is contractible. Indeed \(C_G\) is a proper convex cone; after quotienting its lineality space, the pointed part has a spherically convex section, and \(K_G\) is the join of that section with the sphere of the lineality space.

Compare the normalized omission map on \(\partial P_V\) with
\[
h(x)=-\frac{x}{\|x\|}.
\]
If \(x\) lies in the permutahedron face \(G\), then the coordinates of \(x\) increase from earlier to later blocks, so the coordinates of \(-x\) decrease from earlier to later blocks. Therefore
\[
h(G)\subseteq K_G.
\]
The normalized omission map is carried by the same acyclic carrier. The acyclic carrier theorem makes the two maps homotopic.

Consequently
\[
\deg(\widehat D|_{\partial F^-})
=
\deg(h)
=
(-1)^{n-1},
\]
up to the harmless orientation convention for \(Q\). In particular the degree has absolute value one.

Every continuous extension of this boundary map over the exceptional facet \(F^-\) must therefore hit the origin. The barycentric omission map is such an extension, so \(F^-\) contains an interior projected omission zero. Reversal gives the same conclusion for
\[
F^+=V(H)\mid\{r\}.
\]

Thus in a hypothetical counterexample the two exceptional facets do not merely permit topological cancellation:
\[
\boxed{
\text{each exceptional facet carries an essential degree-one omission zero.}
}
\]

This sharpens the limitation of the rooted omission projection. The global Borsuk--Ulam zero can be absorbed by the two extreme facets for a structural degree reason. Therefore a continuation that uses only the same projected omission map and the same quotient target cannot force a useful nonexceptional zero; additional information or a genuinely different target is required.


### The exact violation map escapes the exceptional omission facets

The omission projection fails for a topologically structural reason on the two extreme auxiliary facets, but the exact auxiliary violation vector behaves differently.

Let \(n=|V(H)|\), so the auxiliary tournament \(H^+\) has \(n+1\) vertices and the boundary of its centered permutahedron is
\[
S^{n-1}.
\]
Use the odd violation vector
\[
F(\pi)=(F_d(\pi))_{1\le d\le n-2}
\]
from [[auxiliary_violation_vector_has_exact_chamber_zeros]], where
\[
F_d=x_d-y_d+g\,x_dy_d.
\]
Its chamber zeros are exactly directed one-change orders and therefore exactly two-cover certificates for \(H\).

Average \(F\) over every proper face and extend affinely on the barycentric subdivision. This gives a continuous odd map
\[
\mathcal F:S^{n-1}\longrightarrow\mathbb R^{n-2}.
\]
Bourgin--Yang therefore gives
\[
\dim \mathcal F^{-1}(0)\ge1.
\]
Every zero has the usual positive carrier-face expansion:
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi F(\pi)=0,
\qquad
\lambda_\pi>0.
\]

Now consider the exceptional facet
\[
C^-=\{r\}\mid V(H).
\]
Here \(r\) is first in every chamber. There are no left violations, so
\[
x_d=0,\qquad F_d=-y_d\in\{0,-1\}
\]
for every chamber and every distance \(d\). If a positive convex combination of these vectors were zero, every coordinate of every chamber vector would have to vanish. Thus every chamber in the carrier would satisfy
\[
F(\pi)=0,
\]
which is already a directed one-change order and hence a two-cover of \(H\).

Therefore, under the counterexample hypothesis,
\[
\mathcal F^{-1}(0)\cap C^-=\varnothing.
\]
By reversal,
\[
\mathcal F^{-1}(0)\cap C^+=\varnothing,
\qquad
C^+=V(H)\mid\{r\}.
\]

Hence:
\[
\boxed{
\text{if }H\text{ has no two-cover, every zero carrier of the exact violation map is nonexceptional.}
}
\]

This contrasts sharply with the projected omission map, whose two exceptional facets carry essential degree-one zeros. The violation map therefore genuinely escapes Astra's exceptional-facet obstruction.

The remaining gap is different: positive balance of the violation vectors on a nonexceptional face does not yet imply that one chamber has \(F=0\). The next structural target is a facewise conversion theorem for these positional violation vectors, ideally using fixed-center intermediate value and the fact that the zero locus has positive dimension.


### A side-set gauge and exact closure on singleton-\(r\) carrier faces

The coordinatewise gauge in the exact violation vector can be replaced by one global double-violation coordinate in a way that is better adapted to faces.

Let the original vertex set be \(V\), let \(r\) be the auxiliary vertex, and for a spanning order \(\pi\) write
\[
L_r(\pi)=\{v\in V:v\text{ occurs left of }r\},
\qquad
R_r(\pi)=V\setminus L_r(\pi).
\]
Fix once and for all a total order \(\prec\) on subsets of \(V\). Define an antipodal sign \(g_{\rm set}\) by
\[
g_{\rm set}(\pi)=
\begin{cases}
+1,&|L_r(\pi)|<|R_r(\pi)|,\\
-1,&|L_r(\pi)|>|R_r(\pi)|,\\
+1,&|L_r|=|R_r|\text{ and }L_r\prec R_r,\\
-1,&|L_r|=|R_r|\text{ and }R_r\prec L_r.
\end{cases}
\]
Reversal exchanges \(L_r\) and \(R_r\), hence
\[
g_{\rm set}(\pi^{\rm rev})=-g_{\rm set}(\pi).
\]

For the left/right violation bits \(x_d,y_d\) of [[auxiliary_violation_vector_has_exact_chamber_zeros]], define
\[
A_d(\pi)=x_d(\pi)-y_d(\pi),
\]
and choose arbitrary positive weights \(w_d>0\). Put
\[
B(\pi)
=
g_{\rm set}(\pi)\sum_d w_d x_d(\pi)y_d(\pi).
\]
Then
\[
\Theta(\pi)=\bigl((A_d(\pi))_d,B(\pi)\bigr)
\]
is odd. Its target has dimension \(n-1\), equal to the dimension of the auxiliary Coxeter sphere.

Moreover
\[
\Theta(\pi)=0
\]
if and only if \(\pi\) has no violations. Indeed \(A_d=0\) gives \(x_d=y_d\) at every distance, while \(B=0\), since \(g_{\rm set}=\pm1\) and all \(w_d>0\), forces
\[
x_dy_d=0
\]
for every \(d\). Thus \(x_d=y_d=0\) for all \(d\).

Average \(\Theta\) on proper face barycenters and extend affinely. Borsuk--Ulam gives a zero and the usual strictly positive expansion over every chamber of its carrier face.

The key advantage of \(g_{\rm set}\) is the following.

**Theorem (singleton-\(r\) carrier conversion).**
Let
\[
C=C_1|\cdots|C_t
\]
be a proper permutahedron face in which
\[
C_j=\{r\}.
\]
Suppose there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(C))
\]
with
\[
\sum_\pi\lambda_\pi\Theta(\pi)=0.
\]
Then every chamber of \(C\) is violation-free. In particular \(H\) has a spanning two-cover.

**Proof.**
Because \(r\) is a singleton block, the set of original vertices left of \(r\) and the set right of \(r\) are fixed throughout \(C\). Hence
\[
g_{\rm set}(\pi)=g_0\in\{\pm1\}
\]
is constant on all chambers of \(C\).

The last coordinate of the positive balance is therefore
\[
0
=
g_0\sum_\pi\lambda_\pi\sum_d w_dx_d(\pi)y_d(\pi).
\]
Every summand inside the last sum is nonnegative, every \(w_d\) is positive, and every \(\lambda_\pi\) is positive. Hence
\[
x_d(\pi)y_d(\pi)=0
\]
for every chamber \(\pi\) and every distance \(d\).

Now fix \(d\). Since \(r\) is a singleton block, the chamber set factors as
\[
\mathcal V(C)
=
\mathcal L\times\mathcal R,
\]
where \(\mathcal L\) consists of the independent permutations in blocks left of \(r\), and \(\mathcal R\) those right of \(r\). The bit \(x_d\) depends only on the left factor and \(y_d\) only on the right factor.

If some left factor had \(x_d=1\) and some right factor had \(y_d=1\), their product chamber would satisfy
\[
x_dy_d=1,
\]
contrary to the preceding paragraph. Therefore at least one of the two functions is identically zero on its factor.

But the \(A_d\)-coordinate of the positive balance says
\[
\sum_\pi\lambda_\pi x_d(\pi)
=
\sum_\pi\lambda_\pi y_d(\pi).
\]
If one side is identically zero, positivity forces the other side to be identically zero as well. Hence
\[
x_d(\pi)=y_d(\pi)=0
\]
for every chamber. Since \(d\) was arbitrary, every chamber of \(C\) is violation-free. \(\square\)

Thus the exact violation map has no unresolved singleton-\(r\) carrier geometry at all:
\[
\boxed{
\text{positive }\Theta\text{-balance on a face with }\{r\}\text{ as a block}
\Longrightarrow
\text{an actual two-cover certificate}.
}
\]

Consequently, under the counterexample hypothesis, every zero carrier of the \(\Theta\)-map must place \(r\) in a block containing at least one original vertex. This eliminates the central singleton case as well as the two extreme singleton facets; the only remaining face-to-cover obstruction is genuinely the geometry of a nontrivial \(r\)-block.
