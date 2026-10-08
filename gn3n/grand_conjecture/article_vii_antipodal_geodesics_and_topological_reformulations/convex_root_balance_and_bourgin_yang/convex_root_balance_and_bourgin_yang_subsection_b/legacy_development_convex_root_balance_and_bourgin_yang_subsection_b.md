# Positive balance on every chamber and the switch-separation bound — preserved pre-item development

## Composition

(none yet)

## Development

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
