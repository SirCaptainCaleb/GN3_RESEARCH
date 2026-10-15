# Tournament interleaving and functional-dependency geodesics

# Full-rank monochromatic paths beyond threshold colorings

We establish constructive closure for reversal-odd boundary colorings obtained from an arbitrary tournament and for two affine classes of unrestricted antipodally odd cube-edge colorings. All paths in the proofs use each original vertex or each cube dimension once.

## Interleaving tournament Hamilton paths

**Theorem 1 (outer-pair tournament theorem).** Let \(T(a,c)\in\mathbb F_2\) satisfy \(T(c,a)=1-T(a,c)\) for all distinct \(a,c\in V\). Put
\[
b(a,h,c)=T(a,c)
\]
for pairwise distinct triples on \(V\), where \(|V|=n\ge3\). Then the boundary tournament \(b\) has a monochromatic Hamilton tight path, even if \(T\) is cyclic.

*Proof.* Split \(V=A\sqcup B\) with \(|A|=\lceil n/2\rceil\) and \(|B|=\lfloor n/2\rfloor\). Declare \(a\to c\) if \(T(a,c)=0\). Each induced tournament has a directed Hamilton path. For completeness, insert a new vertex \(v\) into a previously constructed directed path: place it first if it beats the first vertex, last if the last beats it, and otherwise at a place between consecutive vertices \(a_i,a_{i+1}\) with \(a_i\to v\to a_{i+1}\). This proves the tournament Hamilton-path lemma inductively. Let the resulting paths be \(a_1\to\cdots\to a_{|A|}\) and \(b_1\to\cdots\to b_{|B|}\), and interleave the two lists as \(a_1,b_1,a_2,b_2,\ldots\). Every consecutive ordered triple has two outer vertices that are consecutive along one of the directed Hamilton paths, so its bit is zero. The interleaving includes every vertex once. \(\square\)

**Corollary 2 (higher windows).** For \(k\ge1,n\ge k+1\), color ordered \((k+1)\)-tuples of distinct vertices by \(T(v_0,v_k)\), with \(T\) an arbitrary tournament. Then there is a Hamilton ordering of all \(n\) vertices whose consecutive \((k+1)\)-window bits are monochromatic.

*Proof.* Split vertices into \(k\) classes occupying positions congruent modulo \(k\) in the desired ordering. Choose a directed Hamilton path on every class, and interleave the paths in their corresponding residue positions. The first and last vertices of each consecutive \((k+1)\)-window are successive vertices of one class's directed path, giving bit zero. \(\square\)

## Affine cube-edge colorings

An affine coloring of the undirected direction-\(i\) edges has the form
\[
c_i(y)=\alpha_i+\sum_j A_{ij}y_j\pmod2,
\tag{1}
\]
where \(A_{ii}=0\) ensures endpoint invariance and \(A\mathbf1=\mathbf1\) ensures antipodal oddness.

**Theorem 3 (invertible dependency matrix).** If \(A\) is invertible over \(\mathbb F_2\), each dimension order \(\pi\) has precisely two starting roots giving monochromatic full antipodal geodesics: one root gives all zeros, and its antipode gives all ones. There are therefore \(2n!\) monochromatic rooted-and-ordered complete geodesics.

*Proof.* Before traversing direction \(\pi_i\), the path from \(x\) has flipped the preceding dimensions \(\pi_1,\ldots,\pi_{i-1}\). Its edge color is
\[
w_i=\alpha_{\pi_i}+(Ax)_{\pi_i}+
\sum_{k<i}A_{\pi_i,\pi_k}\pmod2.
\tag{2}
\]
The equations \(w_i=0\) for all \(i\) form the nonsingular system \(Ax=\alpha+r(\pi)\), where \(r(\pi)_{\pi_i}=\sum_{k<i}A_{\pi_i,\pi_k}\). It has one root solution. Since \(A\mathbf1=\mathbf1\), adding \(\mathbf1\) to the root complements every path bit, giving the unique all-one root. Every order uses every direction once, and there are \(n!\) orders. \(\square\)

**Theorem 4 (one dependency per dimension, allowing singular matrices).** Let \(p:[n]\to[n]\) satisfy \(p(i)\ne i\) and choose arbitrary bits \(\alpha_i\). Every coloring
\[
c_i(y)=y_{p(i)}+\alpha_i\pmod2
\tag{3}
\]
has a monochromatic full antipodal geodesic, whether or not \(p\) is injective.

*Proof.* For a root \(x\), the direction-\(i\) step of a full dimension ordering has bit zero if and only if
\[
\mathbf1_{\{p(i)\ \text{precedes }i\}}=x_{p(i)}+\alpha_i.
\tag{4}
\]
Give each edge \(\{p(i),i\}\) of a multigraph the direction \(p(i)\to i\) when the right side is one, and \(i\to p(i)\) otherwise. A topological ordering of this directed multigraph satisfies all equations (4).

Because each vertex chooses one parent \(p(i)\), the undirected dependency multigraph is a pseudoforest: every component consists of one cycle (including a pair of parallel edges when a cycle has two vertices) with attached trees. Fix an arbitrary linear ordering of the vertices on each cycle. Every cycle vertex \(v\) is the parent of one other cycle vertex \(i\), so the choice of \(x_v\) controls the direction of its corresponding cycle edge. Set \(x_v\) so each cycle edge points forward in the chosen linear ordering. Choose the remaining root bits arbitrarily. The resulting directed multigraph has no directed cycle: the edges in its only undirected cycle are aligned with an acyclic order, while the attached trees contain no cycles. Choose a topological ordering of its vertices and use it as the cube dimension order. Equation (4) makes every traversed cube edge color zero. Antipodal translation gives a full geodesic of color one. \(\square\)

These results prove the monochromatic full-path conclusion for nonlinear outer-pair tournament colorings and for two affine cube families. They supply additional tests for a proposed common selection theorem on locally consistent Coxeter coset words; unrestricted one-switch existence remains open.

## Cokernel root-slide transport and affine corank-two closure

Retain the affine antipodally odd cube-edge coloring
\[
f_i(x)=\alpha_i+(Ax)_i,\qquad A_{ii}=0,\quad A\mathbf1=\mathbf1
\]
over \(\mathbb F_2\). The matrix need not be symmetric or have an acyclic dependency graph. Let \(V=\mathbb F_2^n/\operatorname{im}A\), \(k=\dim V=n-\operatorname{rank}A\), and \(v_i=[e_i]\in V\). The \(v_i\) span \(V\), and
\[
\sum_i v_i=[\mathbf1]=[A\mathbf1]=0. \tag{CR1}
\]
For a permutation \(\pi=(\pi_1,\ldots,\pi_n)\) put
\[
(r_\pi)_{\pi_t}=\sum_{s<t}A_{\pi_t,\pi_s},
\qquad \sigma(\pi)=[\alpha+r_\pi]\in V. \tag{CR2}
\]

**Lemma 5 (monochromatic solvability and cyclic transport).** A full all-zero geodesic with dimension order \(\pi\) exists if and only if \(\sigma(\pi)=0\). Every successful order admits \(2^k\) all-zero starting roots; their antipodes give \(2^k\) all-one starting roots. For cyclic rotation \(\rho\pi=(\pi_2,\ldots,\pi_n,\pi_1)\),
\[
\boxed{\sigma(\rho\pi)=\sigma(\pi)+v_{\pi_1}.} \tag{CR3}
\]
Consequently the obstructions of the \(n\) cyclic rotations are
\[
\sigma(\pi)+\sum_{s=1}^t v_{\pi_s},\qquad 0\le t<n. \tag{CR4}
\]

*Proof.* The color on the \(t\)-th step from starting root \(x\) is \(\alpha_{\pi_t}+(Ax)_{\pi_t}+(r_\pi)_{\pi_t}\). Thus all colors vanish precisely when \(Ax=\alpha+r_\pi\), solvable if and only if its quotient class vanishes. The solution fiber has cardinality \(|\ker A|=2^k\). Since \(A\mathbf1=\mathbf1\), translating the root antipodally changes every color from zero to one.

Let \(i=\pi_1\). Under cyclic rotation, every other predecessor sum changes by \(A_{ji}\), while the predecessor sum in row \(i\) changes from zero to \(\sum_{j\ne i}A_{ij}=1\). Therefore \(r_{\rho\pi}+r_\pi=Ae_i+e_i\). Project into \(V\) to obtain (CR3) and iterate. \(\square\)

**Corollary 6 (quotient prefix-cover criterion).** If some order satisfies
\[
\left\{\sum_{s=1}^t v_{\pi_s}:0\le t<n\right\}=V, \tag{CR5}
\]
then for every constant vector \(\alpha\), one of its cyclic rotations supplies a monochromatic full antipodal geodesic.

*Proof.* Equation (CR4) translates all of \(V\) and therefore contains zero. Apply Lemma 5. \(\square\)

**Theorem 7 (all-dimensional affine corank-two closure).** Every affine antipodally odd cube-edge coloring as above satisfies
\[
\boxed{\operatorname{rank}_{\mathbb F_2}A\ge n-2
\ \Longrightarrow\
\text{a monochromatic dimension-simple full antipodal geodesic exists}.} \tag{CR6}
\]

*Proof.* Put \(k=\dim V\le2\). For \(k=0\), every \(\sigma(\pi)\) vanishes. For \(k=1\), some \(v_i\ne0\), because the classes span \(V\). Beginning an order with \(i\) makes the two prefix sums \(0,v_i\) exhaust \(V\), proving the result by Corollary 6.

Suppose \(k=2\). If two distinct directions \(i,\ell\) have equal nonzero classes \(v_i=v_\ell=a\), choose \(j\) with \(v_j=b\) independent of \(a\) and begin an ordering with \(i,j,\ell\). The first four prefix sums \(0,a,a+b,b\) exhaust \(V\), again giving (CR5).

It remains to consider the case in which every nonzero quotient class occurs at most once among the \(v_i\). As these classes span \(V\) and sum to zero by (CR1), three distinguished directions \(i,j,\ell\) have
\[
v_i=a,\qquad v_j=b,\qquad v_\ell=a+b,
\]
where \(a,b\) are independent, and all remaining \(v_h=0\).

Assume contrariwise that every dimension ordering \(\pi\) has nonzero syndrome \(\sigma(\pi)\). Choose an order \(\pi=(i,j,\ldots)\). Its first three rotation syndromes are \(\sigma(\pi),\,\sigma(\pi)+a,\,\sigma(\pi)+a+b\). All must be nonzero. As \(V=\{0,a,b,a+b\}\), this forces \(\sigma(\pi)=b\). Swapping the first two directions gives \(\pi'=(j,i,\ldots)\), for which the same reasoning forces \(\sigma(\pi')=a\).

An adjacent swap changes only the two predecessor entries involved:
\[
r_{\pi'}+r_\pi=A_{ij}e_i+A_{ji}e_j,
\]
hence
\[
a+b=\sigma(\pi')+\sigma(\pi)=A_{ij}a+A_{ji}b.
\]
Independence yields \(A_{ij}=A_{ji}=1\). Since any two of the three distinct nonzero vectors of \(V\) are independent, the same argument applied to the other two pairs forces all six off-diagonal entries in the distinguished \(3\times3\) submatrix to equal one. In particular, \(A_{ji}=A_{\ell i}=1\).

But the \(i\)-th column lies in \(\operatorname{im}A\), so
\[
0=[Ae_i]=\sum_h A_{hi}v_h=v_j+v_\ell=b+(a+b)=a,
\]
a contradiction. Here \(A_{ii}=0\), and every unlisted \(v_h\) vanishes. Therefore some \(\sigma(\pi)=0\), and Lemma 5 supplies a monochromatic full antipodal geodesic. \(\square\)

**Proof-closure perspective.** The quotient root-slide identity (CR3) translates monochromatic existence into locating the zero syndrome in a permutation gallery. The prefix-cover criterion gives an order-independent sufficient condition, while the exceptional corank-two proof extracts additional compatibility from adjacent-order exchanges. In higher corank the identity
\[
\sigma(\pi')+\sigma(\pi)=A_{ij}v_i+A_{ji}v_j
\]
for exchanging adjacent directions is a candidate global invariant. Establishing that these relations force zero for arbitrary affine \(A\) with \(A\mathbf1=\mathbf1\) would close the antipodally odd affine class, which is strictly narrower than unrestricted NORI1. The present theorem makes no assertion about arbitrary nonlinear edge colorings or arbitrary reversal-odd boundary 3-tournaments.


## Weighted-inversion curvature normal form

Retain \(V,v_i,r_\pi,\sigma(\pi)\) from the preceding results. For distinct direction indices \(i,j\), define the symmetric quotient-valued pair weight
\[
K_{ij}:=A_{ij}v_i+A_{ji}v_j=K_{ji}\in V. \tag{CR7}
\]
For permutations \(\pi,\tau\), let \(I(\pi,\tau)\) comprise the unordered direction pairs whose relative order differs between \(\pi\) and \(\tau\).

**Proposition 8 (inversion formula and star-curvature identity).** For every antipodally odd affine cube-edge coloring,
\[
\boxed{\sigma(\pi)+\sigma(\tau)
=\sum_{\{i,j\}\in I(\pi,\tau)}K_{ij}.} \tag{CR8}
\]
Moreover,
\[
\boxed{\sum_{j\ne i}K_{ij}=v_i\qquad(i\in[n]).} \tag{CR9}
\]
Consequently the affine span of the attainable syndrome set \(\{\sigma(\pi):\pi\in\mathfrak S_n\}\) is the whole quotient \(V\), for *every* matrix rank. The set contains at least \(k+1\) values, where \(k=\dim V\), and no proper affine hyperplane contains it.

*Proof.* The \(i\)-th entry of \(r_\pi+r_\tau\) is the sum of \(A_{ij}\) over the indices \(j\) whose relative precedence changes. Hence
\[
r_\pi+r_\tau
=\sum_{\{i,j\}\in I(\pi,\tau)}
(A_{ij}e_i+A_{ji}e_j).
\]
Projecting to \(V\) gives (CR8). Summing the pair weights incident to \(i\) gives
\[
\sum_{j\ne i}K_{ij}
=\Bigl(\sum_{j\ne i}A_{ij}\Bigr)v_i
 +\sum_{j\ne i}A_{ji}v_j
=v_i+[Ae_i]=v_i,
\]
using \(A_{ii}=0\), \(A\mathbf1=\mathbf1\), and \([Ae_i]=0\). This proves (CR9).

Every pair \(i,j\) can be made adjacent in some permutation and then interchanged. By (CR8), the two resulting syndrome values differ by \(K_{ij}\). Thus the linear span of all differences of attained values contains each \(K_{ij}\), hence by (CR9) every \(v_i\). The \(v_i\) span \(V\), so the attained values affinely span \(V\). A spanning set in a \(k\)-dimensional affine space has at least \(k+1\) elements. \(\square\)

**Reduction to a global saturation lemma (open).** For any reference order \(\pi_0\), the statement that *every* choice of offset \(\alpha\) has a monochromatic full geodesic is equivalent to the weighted inversion map
\[
\pi\longmapsto\sum_{\{i,j\}\in I(\pi,\pi_0)}K_{ij} \tag{CR10}
\]
being surjective onto \(V\). Indeed (CR8) expresses the attainable syndromes as a translate of this image, and varying \(\alpha\) varies the translating coset arbitrarily. Proposition 8 proves that the image affinely spans \(V\); Theorem 7 proves surjectivity when \(\dim V\le2\). General surjectivity remains conjectural.

The needed further ingredient is therefore a global saturation principle for the permutation inversion weights, using both their pairwise form (CR7) and their star relations (CR9). This formulation preserves full dimension-simple paths and avoids reasoning through successively larger cube orders.


## Quotient induction and the one-hole obstruction

The preceding affine results remain valid if the quotient \(V\) is replaced by *any* vector space equipped with a surjective linear map \(p:\mathbb F_2^n\to V\) satisfying \(pA=0\). In this generality let \(v_i=p(e_i)\) and \(\sigma_p(\pi)=p(\alpha+r_\pi)\). The cyclic-rotation and adjacent-interchange formulas, the star-curvature identity, and the corank-at-most-two surjectivity proof require only
\[
A_{ii}=0,\quad A\mathbf1=\mathbf1,\quad pA=0,\quad
\operatorname{span}\{v_i\}=V.
\]
In particular, any further linear quotient of \(V\) is again admissible.

**Proposition 9 (missing-syndrome descent).** Let \(S_p=\{\sigma_p(\pi):\pi\in\mathfrak S_n\}\subseteq V\). If \(S_p\) omits two distinct elements \(a,b\), then the induced syndrome set in the quotient \(V/\langle a+b\rangle\) also omits a point.

*Proof.* The two-element coset \(a+\langle a+b\rangle=\{a,b\}\) is disjoint from \(S_p\). Its image is therefore absent from the projection of \(S_p\). The quotient map composed with \(p\) still annihilates \(A\) and is surjective, so it gives admissible lower-dimensional data. \(\square\)

**Corollary 10 (one-hole reduction for universal affine closure).** Suppose that syndrome surjectivity is established for all admissible quotients of dimension strictly less than \(k\), where \(k\ge3\). For any admissible \(k\)-dimensional quotient, either its syndrome image is all of \(V\), or it is \(V\setminus\{a\}\) for a single element \(a\). In particular any minimal-dimensional failure of universal surjectivity has precisely one missing syndrome.

*Proof.* If two values were missing, Proposition 9 would exhibit a nonsurjective quotient of dimension \(k-1\), contrary to the hypothesis. \(\square\)

**Proof-closure target.** A general theorem excluding the *punctured full image* \(V\setminus\{a\}\), among admissible weighted-inversion maps, would imply universal affine syndrome surjectivity by induction from the corank-two theorem. The extra fact that every nonzero quotient syndrome would have to be attained in a minimal obstruction is available for exploiting rank-two exchanges, cyclic root slides, or parity counts. This is a conditional reduction; it does not establish the exclusion itself.

The reduction uses affine invariance and full direction permutations throughout. It makes no claim that nonlinear cube-edge colorings, or boundary-tournament colorings, admit analogous linear quotient syndromes.
