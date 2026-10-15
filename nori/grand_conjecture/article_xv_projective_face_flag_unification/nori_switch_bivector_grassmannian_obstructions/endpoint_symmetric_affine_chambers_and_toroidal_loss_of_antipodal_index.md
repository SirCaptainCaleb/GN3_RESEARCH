# Endpoint-symmetric affine chambers and toroidal loss of antipodal index

### Endpoint-symmetric affine chambers and toroidal loss of antipodal index

The root-gluing obstruction from earlier in this Article suggests adjoining the exchange that changes a cube geodesic's starting vertex across its *last* dimension, in addition to the usual first-dimension root exchange. This gives a reflection-compatible chamber complex. The resulting topology can be computed: it is a torus, and its free path-reversal cover has vanishing Bockstein. Thus this natural repair eliminates the projective obstruction used in the spherical approach.

Fix \(n\ge3\). Let a cube complete-path chamber be \(g=(x;\pi_1,\ldots,\pi_n)\), with root \(x\in\mathbb F_2^n\) and a permutation \(\pi\) of the dimensions. Write
\[
r_0(x;\pi)=(x+e_{\pi_1};\pi),\qquad
r_n(x;\pi)=(x+e_{\pi_n};\pi),
\]
and, for \(1\le i<n\), let \(r_i\) exchange \(\pi_i\) and \(\pi_{i+1}\) without moving the root. The generators \(r_0,\ldots,r_{n-1}\) are the ordinary type-B chamber exchanges. The additional generator \(r_n\) changes the root across the last dimension. Every chamber still represents a full, dimension-simple antipodal cube geodesic.

**Theorem 1 (the endpoint-symmetric torus).** These \(n+1\) exchanges are the facet adjacencies of a finite regular cell decomposition of the \(n\)-torus
\[
\boxed{\mathbb T_n=(\mathbb R/2\mathbb Z)^n}\tag{1}
\]
into \(2^n n!\) full-dimensional simplicial chambers indexed by \((x;\pi)\). Their rank-two exchange relations are those of the affine Coxeter diagram \(\widetilde C_n\): orders four at the two terminal adjacent pairs, orders three at the internal adjacent pairs, and commuting relations for nonadjacent pairs. In particular the chamber graph is a finite quotient of an affine Coxeter chamber graph.

*Proof.* Represent a generic point of (1) by \(t_i\in(-1,1)\) with \(0<|t_i|<1\) and pairwise distinct absolute values. Record its signs by \(x_i=0\) for \(t_i>0\) and \(x_i=1\) for \(t_i<0\), and sort the magnitudes as
\[
0<|t_{\pi_1}|<|t_{\pi_2}|<\cdots<|t_{\pi_n}|<1.
\tag{2}
\]
For every \((x;\pi)\), the closure of the corresponding region is the image of the standard closed simplex \(0\le s_1\le\cdots\le s_n\le1\), under \(t_{\pi_j}=(-1)^{x_{\pi_j}}s_j\pmod2\). Distinct interior regions are disjoint, and their closures cover the torus, yielding a regular simplicial-cell decomposition. The interiors number \(2^n n!\).

Crossing \(s_1=0\) changes the sign of the smallest-magnitude entry, and hence gives \(r_0\). Crossing \(s_j=s_{j+1}\), \(1\le j<n\), exchanges the adjacent sorted entries and gives \(r_j\). Crossing \(s_n=1\) passes through the identified representatives \(+1\equiv-1\pmod2\), changing the sign of the largest-magnitude entry and giving \(r_n\). These are all the chamber facets.

At a codimension-two intersection of consecutive interior magnitude walls, six chambers meet, giving the braid relation of order three. At either end, a sign wall meets an adjacent magnitude wall with eight surrounding chambers, giving order four. Nonadjacent walls commute. These are the relations of the affine \(\widetilde C_n\) string diagram. \(\square\)

**Theorem 2 (reversal becomes geometric).** Define on the chamber set
\[
A(x;\pi)=(\bar x;\pi),\qquad
R(x;\pi)=(x;\pi^{\mathrm{rev}}),\qquad
J=AR.
\tag{3}
\]
On the torus (1), these are induced by
\[
\boxed{
A(t)=-t,\qquad R(t)=\mathbf1-t,\qquad
J(t)=t+\mathbf1\pmod{2\mathbb Z^n}.}\tag{4}
\]
Consequently \(R\) is a cellular involution, exchanges \(r_0\) with \(r_n\), and conjugates \(r_i\) with \(r_{n-i}\). It has \(2^n\) fixed points on \(\mathbb T_n\). The involution \(J\), which reverses each original full cube geodesic as an undirected path, is free on the entire torus.

*Proof.* Negation flips each sign and preserves the ordering of absolute values, giving \(A\). For \(t_i\in(0,1)\), \(1-t_i\in(0,1)\); for \(t_i\in(-1,0)\), the representative of \(1-t_i\pmod2\) belongs to \((-1,0)\). In both cases its magnitude is \(1-|t_i|\), so the sign remains unchanged and the magnitude order reverses. This gives \(R\). The product is translation by \(-\mathbf1\equiv\mathbf1\pmod2\), giving \(J\).

The conjugation laws follow from the exchanges of the smallest and largest magnitude walls under \(s\mapsto1-s\). The equation \(t=\mathbf1-t\pmod2\) has solutions \(t_i\in\{1/2,3/2\}\) independently, hence \(2^n\) fixed points. Translation by \(\mathbf1\) has no fixed point modulo \(2\mathbb Z^n\), because \(\mathbf1\notin2\mathbb Z^n\). Finally, reversing a full cube geodesic changes its root to its antipode and reverses its dimension order, which is precisely \(J\). \(\square\)

The field transformation is significant. For any antipodally odd undirected cube-edge coloring \(c\), writing \(w(g)\) for its full edge-color word, the identities established earlier in this Article give
\[
w(Ag)=\mathbf1+w(g),\qquad
w(Rg)=\mathbf1+\operatorname{rev}w(g),\qquad
\boxed{w(Jg)=\operatorname{rev}w(g).}\tag{5}
\]
Thus the reflection \(R\), which complements and reverses the word, acquires fixed points in this enlarged source; the free geometric involution \(J\) merely reverses the undirected-edge word.

**Theorem 3 (vanishing primary cover obstruction).** The quotient of the endpoint-symmetric torus by its free involution \(J\) is another \(n\)-torus. Its double-cover class \(\alpha\in H^1(\mathbb T_n/J;\mathbb F_2)\) is the reduction of an integral class, so
\[
\boxed{\beta(\alpha)=0,\qquad \alpha^2=0.}\tag{6}
\]
More generally, \(\alpha^k=0\) for every \(k\ge2\). Hence the Bockstein and cup-power obstructions that force failures of equivariant fillings on the spherical type-B carrier do not force such failures on this free toroidal carrier.

*Proof.* Write \(\Lambda=2\mathbb Z^n+\mathbb Z\mathbf1\). Translation by \(\mathbf1\) defines the quotient
\[
\mathbb T_n/J\cong\mathbb R^n/\Lambda,
\]
which is a torus because \(\Lambda\) is a full-rank lattice. The vectors \(\mathbf1,2e_2,\ldots,2e_n\) form a basis of \(\Lambda\): indeed \(2e_1=2\mathbf1-\sum_{j=2}^n2e_j\). The double cover corresponds to the index-two sublattice \(2\mathbb Z^n\subset\Lambda\). Its covering homomorphism sends the \(\mathbf1\) basis vector to one in \(\mathbb F_2\) and all \(2e_j\) basis vectors to zero. It is the reduction modulo two of the integral homomorphism recording the integer coefficient of \(\mathbf1\). Hence \(\alpha\) lifts to \(H^1(\mathbb T_n/J;\mathbb Z)\), and the integral Bockstein vanishes. The mod-two cohomology ring of a torus is the exterior algebra on degree-one generators, in which every degree-one element squares to zero; this proves the remaining assertions. \(\square\)

**Consequence for a dimension-simple Wu--Yang argument.** Adjoining both endpoint root exchanges resolves the incompatibility of reversal with the ordinary type-B chamber adjacency while keeping every chamber a full dimension-simple geodesic. The natural completion replaces the sphere by a torus. The color-complementing reflection has fixed points, whereas the free path-reversal translation has a covering class with vanishing Bockstein and cup powers. Therefore the spherical equivariant obstruction cannot be transplanted unchanged to this endpoint-symmetric affine complex. A successful common proof requires additional color-sensitive incidence information or a different global source with a nonvanishing index.
