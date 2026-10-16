# Mykkeltveit's de Bruijn cycle-transversal theorem via the first Fourier mode

**Summary:** One Fourier-selected representative of each length-n necklace intersects every directed cycle in the q-ary de Bruijn graph; this minimum size equals the number of necklaces.

## Statement

The minimum feedback vertex set of the directed de Bruijn graph B(q,n) has size (1/n) sum_{d|n} phi(d) q^{n/d}, the necklace count. A Fourier root-of-unity construction selects one word per rotation class and meets every directed cycle.

## Body

# Mykkeltveit's minimum directed-cycle transversal of a de Bruijn graph

**Literature.** Johannes Mykkeltveit, "A proof of Golomb's conjecture for the de Bruijn graph," *Journal of Combinatorial Theory, Series B* 13 (1972), 40–45, DOI: 10.1016/0095-8956(72)90006-8. Expository sources: Zheng–Kingsford–Marçais, "Lower Density Selection Schemes via Small Universal Hitting Sets with Short Remaining Path Length," *Journal of Computational Biology* (2021), DOI: 10.1089/cmb.2020.0432; Pellow et al., "Efficient minimizer orders for large values of k using minimum decycling sets," *Genome Research* (2023), DOI: 10.1101/gr.277644.123.

**Statement (minimum feedback vertex set / cycle transversal).** Let B(q,n) have vertex set {0,...,q-1}^n and arcs
x=(x_0,...,x_{n-1}) -> (x_1,...,x_{n-1},a) for every alphabet symbol a. Let tau be the least number of vertices whose deletion destroys every directed cycle (loops count as cycles). Then for all integers q>=2 and n>=1,
\[
\boxed{\tau(B(q,n))=N(q,n)=\frac{1}{n}\sum_{d\mid n}\varphi(d)\,q^{n/d}.}
\]
Moreover, an optimal transversal contains precisely one representative of each orbit of the pure rotation R(x_0,...,x_{n-1})=(x_1,...,x_{n-1},x_0). The number N(q,n) is the number of length-n necklaces under cyclic rotation. This also bounds the maximum number of pairwise vertex-disjoint directed cycles by N(q,n), attained by the pure-rotation cycles.

**Fourier construction for n>=3.** Set zeta=exp(2 pi i/n) and define the first discrete Fourier mode
\[
P(x)=\sum_{j=0}^{n-1} x_j\zeta^{j+1}\in\mathbb C.
\]
Then
\[
P(Rx)=\zeta^{-1}P(x),\qquad
P(x_1,\ldots,x_{n-1},a)=\zeta^{-1}P(x)+(a-x_0). \tag{D1}
\]
The appended-symbol correction is real. Consequently, for every arc x->y,
\[
\operatorname{Im}P(y)=\operatorname{Im}P(Rx). \tag{D2}
\]
For each rotation orbit with P nonzero, select its unique x satisfying
\[
\operatorname{Im}P(x)\le0<\operatorname{Im}P(Rx). \tag{D3}
\]
The uniqueness follows because the orbit points P(R^t x)=zeta^{-t}P(x) lie at equally spaced angles on a nonzero circle, and exactly one oriented rotation step crosses from the closed lower semicircle to the open upper semicircle. (The orbit of words may have a proper period dividing n, but the same uniqueness holds: P nonzero implies its rotation orbit has full length n, since a shorter word period would force zeta^{-t}P=P for 0<t<n.) From every orbit with P=0 select any one representative, for example the lexicographically least word. Let M be the resulting set, so |M|=N(q,n).

**Self-contained proof that B(q,n)-M is acyclic.** Suppose a directed cycle x^(0)->...->x^(m-1)->x^(0) survives. Its cyclic words arise from a periodic bi-infinite sequence of symbols a_t of period m: x^(t)=(a_t,...,a_(t+n-1)). Summing the Fourier positions around the cycle,
\[
\sum_{t=0}^{m-1}P(x^{(t)})
=\sum_{j=0}^{n-1}\zeta^{j+1}\sum_{t=0}^{m-1}a_{t+j}=0, \tag{D4}
\]
because each inner sum is the same and \(\sum_{j=0}^{n-1}\zeta^{j+1}=0\).

If some imaginary part is nonzero, their sum zero implies that along the cycle some edge crosses from Im P<=0 to Im P>0. By (D2) its tail satisfies (D3), hence belongs to M, a contradiction. Otherwise Im P(x^(t))=0 throughout. Equation (D2) and Im(zeta^{-1}r)=-sin(2 pi/n)r for real r, where n>=3, imply Re P(x^(t))=0 for every t. Thus every P is zero. By (D1), each step of the cycle must then have a=x_0, i.e. each step is a pure rotation. The cycle is therefore a rotation orbit with P=0, from which M contains a vertex, again a contradiction.

The lower bound is immediate: the pure-rotation orbits partition the vertices into N(q,n) vertex-disjoint directed cycles, so every directed-cycle transversal must meet each orbit. This proves the theorem for n>=3.

**Small orders.** For n=1, every vertex has a loop; remove all q vertices. For n=2, select M={(a,b):a<=b}; this selects one vertex per rotation orbit, has q(q+1)/2=N(q,2) members, and its complement permits only transitions (a,b)->(b,c) with a>b>c, which cannot form a directed cycle. The one-mode imaginary-part construction must NOT be applied for n=2, since zeta=-1 has zero imaginary part.

**Transfer mechanism and scope.** The useful pattern is (i) partition by a cyclic symmetry into disjoint base cycles, (ii) represent their rotation by multiplication by one complex Fourier character, (iii) ensure all non-rotation arcs perturb that character only in one real direction, (iv) select one phase-crossing representative per orbit, and (v) use zero Fourier mean on every directed cycle to force a crossing or a degenerate rotation orbit. This is a robust *cycle-cutting* result on shift-overlap graphs; it does **not** by itself produce a monochromatic antipodal cube geodesic or a boundary-tournament tight path. To invoke it for NORI1, a rigorous encoding must preserve directed cycles and supply the special real-increment identity (D1), not merely an abstract cyclic action. This is distinct from Boolean Fourier/syndrome estimates used in the affine NORI1 analysis.

## Metadata

- ID: literature_mykkeltveit_de_bruijn_fourier_cycle_transversal
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
