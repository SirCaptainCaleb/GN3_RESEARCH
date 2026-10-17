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


## Cyclic Fourier discrepancy and high-distance affine closure

Continue with an antipodally odd affine coloring \(f_i(x)=\alpha_i+(Ax)_i\), where \(A_{ii}=0\) and \(A\mathbf1=\mathbf1\). Write \(V=\mathbb F_2^n/\operatorname{im}A\), \(k=\dim V\), and \(\sigma(\pi)=[\alpha+r_\pi]\). Let \(\mu\) be the probability distribution of \(\sigma(\pi)\) when \(\pi\) is uniformly sampled from all \(n!\) direction orders.

The dual space of \(V\) is \(W=\ker A^{\mathsf T}\). For \(z\in W\), let \(\widehat\mu(z)=\mathbb E_\pi(-1)^{z\cdot\sigma(\pi)}\), and write \(w(z)=|\operatorname{supp}z|\). Every \(z\in W\) has even weight since
\[
z\cdot\mathbf1=z^{\mathsf T}A\mathbf1=0. \tag{FD1}
\]

**Theorem 11 (cyclic Fourier discrepancy).** For every nonzero \(z\in W\), with positive even weight \(w=w(z)\),
\[
\boxed{|\widehat\mu(z)|
\le \sqrt{\frac{n-w}{n(w+1)}}.} \tag{FD2}
\]
The bound is uniform in the offset \(\alpha\) and the matrix entries of \(A\), subject to the stated antipodal and undirected-edge hypotheses.

*Proof.* Let \(\rho\) cyclically rotate a direction order. The root-slide identity (CR3) gives, for \(0\le t<n\),
\[
(-1)^{z\cdot\sigma(\rho^t\pi)}
=(-1)^{z\cdot\sigma(\pi)}
 (-1)^{\sum_{s=1}^t z_{\pi_s}}.
\]
Define \(S_z(\pi)=\sum_{t=0}^{n-1}(-1)^{\sum_{s=1}^t z_{\pi_s}}\). Uniform permutation sampling is invariant under each cyclic rotation, so
\[
|\widehat\mu(z)|
\le\frac1n\mathbb E_\pi |S_z(\pi)|
\le\frac1n\sqrt{\mathbb E_\pi S_z(\pi)^2}. \tag{FD3}
\]

We compute its second moment. Read the cyclic sequence \(z_{\pi_1},\ldots,z_{\pi_n}\), which has precisely \(w=2h\) entries equal to one. Its cyclic gaps between successive ones have positive lengths
\(\ell_1,\ldots,\ell_{2h}\) summing to \(n\). Since the number of ones is even, rotating the sequence changes \(S_z\) only by a global sign. Choosing one of the marked positions as a distinguished cyclic origin leaves \(S_z^2\) unchanged and makes the gap vector uniform among positive compositions of \(n\) into \(2h\) parts.

Put \(N=n-2h\), \(a_j=\ell_j-1\), and \(U=a_1+a_3+\cdots+a_{2h-1}\). Then \(a_j\ge0\), \(\sum a_j=N\), and the alternating-sign sum equals \(S_z=\pm(2U-N)\). Stars-and-bars gives
\[
\Pr(U=u)=
\frac{\binom{u+h-1}{h-1}
      \binom{N-u+h-1}{h-1}}
     {\binom{N+2h-1}{2h-1}}.
\]
This beta-binomial distribution has \(\mathbb E U=N/2\) and
\[
\operatorname{Var}(U)=\frac{N(N+2h)}{4(2h+1)}
=\frac{n(n-w)}{4(w+1)}.
\]
Thus
\[
\mathbb E_\pi S_z(\pi)^2
=4\operatorname{Var}(U)
=\frac{n(n-w)}{w+1}.
\]
Substitution into (FD3) proves (FD2). \(\square\)

**Corollary 12 (uniform favorable-order and path counts).** Put
\[
D(W)=\sum_{z\in W\setminus\{0\}}
 \sqrt{\frac{n-w(z)}{n(w(z)+1)}}. \tag{FD4}
\]
For every syndrome target \(v\in V\),
\[
\boxed{
\mu(v)\ge2^{-k}\bigl(1-D(W)\bigr).
} \tag{FD5}
\]
If \(D(W)<1\), every syndrome occurs, and therefore every affine offset \(\alpha\) has a monochromatic full antipodal geodesic. There are at least
\[
\boxed{n!\bigl(1-D(W)\bigr)} \tag{FD6}
\]
rooted, direction-ordered all-zero full geodesics, counted with their starting roots. The same lower bound holds for all-one rooted full geodesics.

*Proof.* Fourier inversion on \(V\) gives
\[
\mu(v)=2^{-k}\left(
1+\sum_{z\in W\setminus\{0\}}
 (-1)^{z\cdot v}\widehat\mu(z)\right).
\]
Use Theorem 11 term by term. For a successful order \(\pi\), the linear system \(Ax=\alpha+r_\pi\) has \(2^k\) solutions, all giving all-zero full paths. Hence the total all-zero rooted-path count is \(2^k n!\mu(0)\), bounded below by (FD6). Antipodal translation exchanges the zero and one colors. \(\square\)

**Corollary 13 (dual-distance sufficient condition).** Let \(d=\min_{z\in W\setminus\{0\}}w(z)\), with \(k\ge1\). If
\[
\boxed{(2^k-1)\sqrt{\frac{n-d}{n(d+1)}}<1,} \tag{FD7}
\]
then the affine coloring has a monochromatic full antipodal geodesic. In particular \(d\ge(2^k-1)^2\) suffices.

*Proof.* The function \(w\mapsto(n-w)/(n(w+1))\) is decreasing. Consequently (FD4) is bounded by the left side of (FD7). For the final sufficient inequality, \((n-d)/n<1\) and \(d+1>(2^k-1)^2\) establish the strict inequality. Apply Corollary 12. \(\square\)

**Closure significance and limitation.** The bound controls the distribution of *full dimension-order monochromatic solvability* by the weight distribution of the left-kernel code, rather than the cube's dimension or a feedback-graph size. It is especially effective when the cokernel is small and all nonzero codewords have large Hamming support. In contrast, short even kernel relations permit large Fourier biases, and the estimate alone cannot exclude a one-hole obstruction for arbitrary matrices. The general affine saturation lemma remains open.


## An abstract one-hole obstruction to star identities alone

The full-affine spanning statement (CR9) leaves open a potential surjectivity argument using only symmetric pair weights and their star sums. Such an argument is impossible without further structural hypotheses.

**Proposition 14 (star-compliant, one-hole weighted inversion map).** Take \(V=\mathbb F_2^3\), four ordered labels \(0,1,2,3\), and symmetric pair weights encoded as binary integers
\[
(K_{01},K_{02},K_{03},K_{12},K_{13},K_{23})
=(0,1,2,3,4,4). \tag{OH1}
\]
Define \(v_i=\sum_{j\ne i}K_{ij}\). Then
\[
(v_0,v_1,v_2,v_3)=(3,7,6,2), \qquad
\operatorname{span}\{v_0,v_1,v_2,v_3\}=V, \tag{OH2}
\]
and \(\sum_i v_i=0\), but the weighted inversion sums over all 24 permutations take precisely seven values:
\[
\boxed{
\left\{\sum_{\substack{i<j\\\pi^{-1}(i)>\pi^{-1}(j)}}K_{ij}:
\pi\in\mathfrak S_4\right\}
=V\setminus\{5\}.} \tag{OH3}
\]
Thus star-curvature constraints and affine spanning are insufficient to eliminate the one-hole obstruction.

*Proof.* The star sums are computed directly from (OH1); for instance \(v_0=0+1+2=3\) and \(v_1=0+3+4=7\). The three values \(3,7,6\) are linearly independent over \(\mathbb F_2\), so the span is \(V\). To verify (OH3), the multiplicities of inversion sums \(0,1,\ldots,7\), in increasing binary-integer order, are
\[
\boxed{(6,2,4,4,4,0,2,2),} \tag{OH4}
\]
obtained by grouping the 24 permutations according to their inversion sets. These multiplicities sum to 24 and show that 5 alone is absent. \(\square\)

**Important limitation of the example.** The weights (OH1) are not of the matrix-compatible form \(K_{ij}=A_{ij}v_i+A_{ji}v_j\) for a zero-diagonal row-odd matrix with \(v_i=[e_i]\) in its cokernel. Indeed \(K_{13}=4\) is not in
\[
\operatorname{span}\{v_1,v_3\}
=\operatorname{span}\{7,2\}=\{0,7,2,5\}.
\]
Thus this proposition does not contradict affine corank-two closure or the proposed general affine theorem. It identifies the pairwise support identity, together with \(pA=0\) and \(A\mathbf1=\mathbf1\), as indispensable input for any general one-hole exclusion proof. The example is a finite refutation of an auxiliary overstrong lemma, not a counterexample to NORI1.


## Nonlinear triangular Boolean profiles

## Nonlinear triangular Boolean profiles force monochromatic full cube geodesics

Let \(n\ge2\) and \(c=(c_i)_{i=1}^n\) be the binary direction rules of an undirected-edge coloring of \(Q_n\): \(c_i(x+e_i)=c_i(x)\). Antipodal oddness, when required, is \(c_i(x+\mathbf1)=1+c_i(x)\), with addition in \(\mathbb F_2\). For each permutation \(\pi\), define the full-geodesic color profile \(\Phi_\pi(x)\in\mathbb F_2^n\) with its entries indexed by direction labels, so
\[
[\Phi_\pi(x)]_i=c_i(x+q_i(\pi)),\qquad
q_i(\pi)=\sum_{\pi^{-1}(j)<\pi^{-1}(i)}e_j.
\tag{TN1}
\]

**Theorem 1 (triangular nonlinear profile bijection).** Suppose there is an invertible binary matrix \(L\in\mathrm{GL}_n(\mathbb F_2)\) and Boolean functions \(h_i:\mathbb F_2^{i-1}\to\mathbb F_2\) such that, writing \(y=Lx\),
\[
\boxed{c_i(x)=y_i+h_i(y_1,\ldots,y_{i-1})\qquad (1\le i\le n).}
\tag{TN2}
\]
Then for *every* direction permutation \(\pi\), the map \(\Phi_\pi:Q_n\to Q_n\) is bijective. In particular, for every prescribed color word \(w\in Q_n\), each order \(\pi\) admits one and only one initial vertex with profile \(w\). If the coloring is antipodally odd, every order admits a monochromatic red and a monochromatic blue full antipodal geodesic, on antipodal initial vertices. There are \(n!\) oriented red full geodesics and \(n!/2\) unoriented red full geodesics.

*Proof.* Write \(y=Lx\), and put \(v_i=Lq_i(\pi)\), a vector depending on the chosen order but not on \(x\). Then
\[
[\Phi_\pi(x)]_i=y_i+(v_i)_i+
h_i(y_1+(v_i)_1,\ldots,y_{i-1}+(v_i)_{i-1}).
\tag{TN3}
\]
For prescribed profile \(w\), solve (TN3) in the order \(i=1,\ldots,n\): the first equation determines \(y_1\), the second determines \(y_2\), and so on. Each equation contains its newly introduced unknown \(y_i\) with coefficient one and depends otherwise only on already determined bits. Thus there is one solution \(y\), and \(L^{-1}y\) gives one initial vertex \(x\). This works for every \(\pi,w\). Antipodal oddness implies \(\Phi_\pi(x+\mathbf1)=\Phi_\pi(x)+\mathbf1\), so the red and blue roots are antipodal. For each of \(n!\) direction orders there is one oriented red geodesic; reversing its direction gives the opposite orientation of the same red path, proving the unoriented count. \(\square\)

**Equivalent derivative certificate.** Define \(f(y)=c(L^{-1}y)\) and Boolean differences \(\partial_j f_i(y)=f_i(y)+f_i(y+e_j)\). Condition (TN2) is equivalent to
\[
\boxed{\partial_i f_i\equiv1,\qquad \partial_j f_i\equiv0\quad(j>i).}
\tag{TN4}
\]
The first condition integrates to \(f_i=y_i+h_i(y_{<i})\), and the second makes \(h_i\) independent of every later variable. Therefore (TN4) is an order-independent, verifiable Boolean-Jacobian certificate for one-root solvability of every complete color profile.

**Example with unbounded nonlinear directions.** Index directions and vertex bits by \(0,\ldots,n-1\), and take \(n\ge5\). Define the antipodally even, degree-two Boolean function
\[
H(x_1,x_2,x_3)=(x_1+x_2)(x_2+x_3),
\]
and let
\[
\boxed{c_i(x)=x_{(i+1)\bmod n}+[i\ge4]H(x_1,x_2,x_3)\quad(0\le i<n).}
\tag{TN5}
\]
Every rule ignores its own vertex bit: for \(i\le3\) the nonlinear term is absent, and for \(i\ge4\) the term depends only on \(x_1,x_2,x_3\). The cyclic reader index \((i+1)\bmod n\) never equals \(i\). Since \(H(x+\mathbf1)=H(x)\), every rule changes color under antipodality. Thus the coloring is legal and antipodally odd.

Let \(L\) be the cyclic permutation matrix \(y_i=x_{(i+1)\bmod n}\). For \(i\le3\) we have \(c_i=y_i\); for \(i\ge4\),
\[
c_i=y_i+(y_0+y_1)(y_1+y_2),
\]
which is triangular in the \(y\)-variables. Therefore Theorem 1 applies. There are \(n-4\) nonlinear rules, all of algebraic degree two, for arbitrarily large \(n\). Independent enumeration for \(n=5\) and \(n=7\) verified edge consistency, antipodal oddness, and bijectivity of the color-profile map for all \(5!=120\) and \(7!=5040\) direction orders, respectively.

*Placement and scope.* The invertible affine dependency-matrix theorem is the case \(h_i\) affine, after a suitable invertible linear transformation. The present theorem permits arbitrary nonlinear triangular transformations, with unboundedly many nonlinear direction rules. It forces NORI1 on this family by substitution, without using root-density bounds or cooperation between paths. It does not imply that every legal odd coloring possesses a triangular presentation.

### Order-wise bijectivity beyond first-level Fourier rank

**Corollary (profile bijections with singular linear Fourier matrix).** For every \(n\ge6\), define
\[
c_i(x)=x_{i+1}\quad(0\le i<n-1),\qquad
c_{n-1}(x)=x_0+H(x_1,x_2,x_3,x_4),
\tag{TN6}
\]
where
\[
H=\operatorname{Maj}(x_1+x_2,\ x_1+x_3,\ x_1+x_4)
\]
and \(\operatorname{Maj}(a,b,d)=ab+ad+bd\) is the three-input majority function over \(\mathbb F_2\). Because each difference \(x_1+x_j\) is invariant under complementing every vertex bit, \(H\) is antipodally even. Every rule ignores its own direction bit, so (TN6) is a legal antipodally odd coloring. With \(L\) the cyclic permutation \(y_i=x_{(i+1)\bmod n}\), the only nonlinear term is in the final output, and it depends on \(y_0,y_1,y_2,y_3\); Theorem 1 therefore makes \(\Phi_\pi\) bijective for every \(\pi\).

Let \(s_i(x)=(-1)^{c_i(x)}\), and let \(M_{ij}=\mathbb E_x s_i(x)(-1)^{x_j}\) be the matrix of first-level Walsh coefficients. The three differences \((x_1+x_2,x_1+x_3,x_1+x_4)\) are uniformly distributed on \(\mathbb F_2^3\), so their majority is a fair bit and \(\mathbb E(-1)^H=0\). Also \(H\) ignores \(x_0\). Consequently
\[
M_{n-1,0}=\mathbb E(-1)^H=0,\qquad
M_{n-1,j}=\mathbb E(-1)^{x_0+H+x_j}=0
\quad(j\ne0),
\tag{TN7}
\]
as the independent fair bit \(x_0\) forces cancellation. Thus the full \(n\)-entry last row of the first-level Fourier matrix is zero, even though all \(n!\) geodesic profile maps are bijections. For \(n=6\), enumeration verified the Walsh cancellation and all 720 color-profile bijections.

This example shows that full-color-profile solvability can be an entirely nonlinear triangular phenomenon not visible to first-order Walsh rank. It is not a counterexample to NORI1.

## Acyclic-orientation model for affine geodesic profiles

## Acyclic-orientation model for affine geodesic profiles

Let \(c_i(x)=\alpha_i+(Ax)_i\) be an affine binary edge coloring of \(Q_n\), with \(A\in M_n(\mathbb F_2)\), \(A_{ii}=0\), \(A\mathbf1=\mathbf1\). Thus the coloring is invariant on each undirected direction edge and is antipodally odd. Put
\[
V=\mathbb F_2^n/\operatorname{im}A,\qquad v_i=[e_i]\in V,\qquad
\gamma_{ij}=A_{ij}v_i+A_{ji}v_j\in V\quad(i\ne j).
\tag{FO1}
\]
Let \(H_A\) be the undirected graph on \([n]\) with edges \(ij\) for which \(\gamma_{ij}\ne0\). For a direction order \(\pi\), define \((r_\pi)_i=\sum_{j\text{ before }i}A_{ij}\), so that the direction-indexed color profile from root \(x\) is
\[
w(x,\pi)=\alpha+Ax+r_\pi.
\tag{FO2}
\]

**Theorem 1 (acyclic-orientation cokernel model).** Fix a reference total order \(\pi_0\) and orient every edge of \(H_A\) from earlier to later under \(\pi_0\). If \(O\) is any acyclic orientation of \(H_A\), let \(I(O)\) be its set of edges oriented opposite to this reference orientation. Then the attainable color-profile set is
\[
\boxed{\mathcal W(c)=
\bigcup_{O\text{ acyclic}}
\left(\alpha+r_{\pi_0}
+\sum_{ij\in I(O)}(A_{ij}e_i+A_{ji}e_j)
+\operatorname{im}A\right).}
\tag{FO3}
\]
In particular its number of profiles depends on \(A\), not on the affine constant \(\alpha\). The unrestricted affine profile-surjectivity question is equivalent to whether the images in \(V\) of the inversion-label sums of acyclic orientations of \(H_A\) exhaust \(V\).

*Proof.* Moving adjacent directions \(i,j\) past one another changes \(r_\pi\) by \(A_{ij}e_i+A_{ji}e_j\). For arbitrary orders \(\pi,\pi_0\), one can sort \(\pi\) into \(\pi_0\) by swapping each reversed pair once (a reduced word for their relative permutation). Thus \([r_\pi]+[r_{\pi_0}]\) is the sum of \(\gamma_{ij}\) over the pairs whose relative order differs. The pairs outside \(H_A\) contribute zero modulo \(\operatorname{im}A\). Restricting a total order to edges of \(H_A\) always gives an acyclic orientation; conversely every acyclic orientation of a finite graph has a total-order extension. Therefore the image of all \(r_\pi\) modulo \(\operatorname{im}A\) is precisely the finite set in (FO3). Equation (FO2) gives the asserted union of cosets. \(\square\)

**Lemma 2 (automatic span of all exchange labels).** Without any acyclicity hypothesis,
\[
\boxed{\sum_{j\ne i}\gamma_{ij}=v_i,\qquad
\operatorname{span}_{\mathbb F_2}\{\gamma_{ij}:ij\in E(H_A)\}=V.}
\tag{FO4}
\]
*Proof.* Since \(\sum_{j\ne i}A_{ij}=1\) and \(\sum_{j\ne i}A_{ji}v_j=[Ae_i]=0\), the first identity follows. The vectors \(v_i\) span \(V\), hence so do the exchange labels. \(\square\)

**Theorem 3 (forest criterion and polynomial-time construction).** If \(H_A\) is a forest, then
\[
\boxed{\mathcal W(c)=\mathbb F_2^n}
\tag{FO5}
\]
for every affine constant \(\alpha\). Given any desired profile \(w\), a full antipodal geodesic with profile \(w\) can be constructed by Gaussian elimination and topological sorting in polynomial time.

*Proof.* A forest has no directed cycles under any orientation, so every subset \(T\subseteq E(H_A)\) can be realized as the reversed-edge set \(I(O)\) of some acyclic orientation \(O\). Thus (FO3) realizes every subset sum of \(\gamma_{ij}\). By (FO4) those sums cover \(V\), giving (FO5). Constructively, solve in \(V\) for coefficients \(t_{ij}\) such that \(\sum t_{ij}\gamma_{ij}=[w+\alpha+r_{\pi_0}]\). Reverse the reference orientation on the selected forest edges and topologically sort the resulting directed forest, obtaining an order \(\pi\). Equations (FO3)-(FO4) then ensure \(w+\alpha+r_\pi\in\operatorname{im}A\), so solve \(Ax=w+\alpha+r_\pi\) by Gaussian elimination. Equation (FO2) proves that the resulting geodesic has profile \(w\). \(\square\)

**Corollary 4 (odd-degree forest dependency graphs).** If \(T\) is any forest in which every vertex has odd degree, let \(A\) be its binary adjacency matrix. The legal antipodally odd coloring
\[
c_i(x)=\alpha_i+\sum_{j:\{i,j\}\in E(T)}x_j
\]
has complete direction-indexed color-profile support, for every \(\alpha\). Indeed \(A_{ii}=0\), \(A\mathbf1=\mathbf1\), and \(\gamma_{ij}=0\) outside \(E(T)\); hence \(H_A\subseteq T\).

**Corollary 5 (simultaneously unbounded cokernel and nonunary dependence).** For any odd \(h\ge3\), let \(T_h\) have vertices consisting of a hub \(o\), branch vertices \(b_1,\ldots,b_h\), and two private leaves \(a_j,d_j\) for each branch. Its edges are \(ob_j,b_ja_j,b_jd_j\). Then \(n=3h+1\), every vertex has odd degree, the binary adjacency matrix \(A_h\) has rank \(2h\), and its cokernel has dimension \(h+1\). The hub and all \(h\) branch vertices have at least three readers, so the number of nonunary direction rules is \(h+1\). By Corollary 4 every direction-indexed profile occurs, even though both the cokernel dimension and number of nonunary rows diverge with \(n\).

*Rank proof.* Each leaf column is \(e_{b_j}\), so the leaf columns span the \(h\)-dimensional branch subspace. The column of branch vertex \(b_j\) is \(e_o+e_{a_j}+e_{d_j}\). These \(h\) columns are independent modulo the branch subspace, because their disjoint private-leaf supports are nonzero. The hub column is \(\sum_{j=1}^h e_{b_j}\) and is already in the branch subspace. Hence \(\operatorname{rank}A_h=2h\). The number of branch readers is three; the hub degree \(h\) is odd, so all row sums equal one. \(\square\)

**Audit.** A Gaussian-elimination and topological-sort implementation constructed geodesics with prescribed independently randomized color profiles in the \(T_h\) families for \(h=3,5,7,9\) (dimensions \(10,16,22,28\)); 200 target profiles were tested per instance. The computed ranks were \(6,10,14,18\), respectively, agreeing with \(2h\). Separately, all 32,768 legal affine five-direction dependency matrices were checked for full profile support, as were 10,000 sampled legal affine six-direction matrices. These finite checks support, but do not establish, surjectivity for arbitrary affine matrices; only the forest theorem and its corollaries are proved.

*Scope.* The acyclic-orientation description (FO3) is valid for all legal affine colorings, not just forests. In general a cyclic exchange-support graph need not admit arbitrary choices of inverted edges; the full affine profile-surjectivity conjecture remains open beyond established classes. The forest theorem does not assert the unrestricted nonlinear NORI1 conjecture.

## Universal local cycle transparency and one-cycle affine profiles

## Universal local cycle transparency and one-cycle affine profile surjectivity

Let \(c_i(x)=\alpha_i+(Ax)_i\) be an affine antipodally odd edge coloring of \(Q_n\), where \(A_{ii}=0\) and \(A\mathbf1=\mathbf1\). Put \(V=\mathbb F_2^n/\operatorname{im}A\), \(v_i=[e_i]\in V\), and \(\gamma_{ij}=A_{ij}v_i+A_{ji}v_j\in V\). Let \(H_A\) be the undirected graph with edges \(ij\) precisely when \(\gamma_{ij}\ne0\). Every orientation of \(H_A\) induced by a total order is acyclic, and every acyclic orientation arises from some total order. Fixing a reference orientation, its reversed-edge sum determines the class of the color-profile offset modulo \(\operatorname{im}A\).

**Lemma 1 (universal vertex-star identity).** For every direction \(i\),
\[
\boxed{v_i=\sum_{j\ne i}\gamma_{ij}.}\tag{CL1}
\]
*Proof.* The first contribution is \((\sum_{j\ne i}A_{ij})v_i=v_i\), because row \(i\) has odd sum. The second is \([\sum_j A_{ji}e_j]=[Ae_i]=0\). \(\square\)

**Theorem 2 (local cycle transparency in arbitrary affine exchange graphs).** Let \(C\) be any simple undirected cycle of length \(\ell\ge3\) in \(H_A\), and let \(W_C\subseteq V\) be the span of all exchange labels from edges not belonging to \(C\). In the quotient \(\widetilde V=V/W_C\), there exists a nonempty proper subset \(D\subsetneq E(C)\) satisfying
\[
\boxed{\sum_{e\in D}\widetilde\gamma_e=0.}\tag{CL2}
\]
Consequently, every attainable class in \(\widetilde V\) of an orientation of \(C\) is also attained by an orientation in which \(C\) is not directed. This conclusion imposes no assumptions on other cycles elsewhere in \(H_A\).

*Proof.* All directions outside \(C\) have \(\widetilde v_j=0\), by the vertex-star identity: every edge incident to such \(j\) lies outside \(C\). For a vertex \(i\) on \(C\), denote its two incident cycle labels by \(\gamma_{i-}\), \(\gamma_{i+}\), giving \(\widetilde v_i=\widetilde\gamma_{i-}+\widetilde\gamma_{i+}\). Fix an edge \(e=ij\) on the cycle, with predecessor edge \(e_-\) at \(i\) and successor edge \(e_+\) at \(j\), following an arbitrary cyclic order. Put \(a=A_{ij}\), \(b=A_{ji}\), with \((a,b)\ne(0,0)\) because \(\gamma_e\ne0\). The definition of \(\gamma_e\) gives
\[
(1+a+b)\widetilde\gamma_e+
a\widetilde\gamma_{e_-}+
b\widetilde\gamma_{e_+}=0.
\tag{CL3}
\]
If \((a,b)=(1,0)\), the predecessor label vanishes; if \((a,b)=(0,1)\), the successor label vanishes. If both equal one, the sum of the predecessor, central, and successor labels vanishes. For \(\ell\ge4\), these are nonempty proper edge subsets, proving (CL2).

It remains to treat a triangle on which every cycle edge has \(a=b=1\). At each of its three vertices, the two internal readers give even parity. Since every row of \(A\) has odd sum, each triangle vertex \(i\) has some reader \(j\) outside the triangle with \(A_{ij}=1\). In \(\widetilde V\), both \(\widetilde v_j=0\) and \(\widetilde\gamma_{ij}=0\), whether \(ij\) lies outside \(C\) as an edge of \(H_A\) or has label zero. The equation \(\widetilde\gamma_{ij}=A_{ij}\widetilde v_i+A_{ji}\widetilde v_j\) therefore yields \(\widetilde v_i=0\). Thus all triangle labels \(\widetilde\gamma_{ij}\) vanish, and any singleton triangle edge establishes (CL2). If at least one triangle edge is asymmetric, the first two cases of (CL3) already apply.

The two directed orientations of \(C\) differ by reversing every cycle edge. Let \(D\) be the proper nonempty zero-sum subset supplied above. Reversing the edges in \(D\) changes no class in \(\widetilde V\), and sends either directed orientation to a nondirected orientation. \(\square\)

**Theorem 3 (one-cycle affine closure with constructive witnesses).** If \(H_A\) contains at most one undirected cycle in total, then every direction-indexed full-geodesic color profile is realized:
\[
\boxed{\mathcal W(c)=\mathbb F_2^n.}\tag{CL4}
\]
For a prescribed profile, a starting root and direction order can be constructed in polynomial time by binary Gaussian elimination, cycle repair, and a topological sort.

*Proof.* If \(H_A\) is a forest, this is the previously proved forest theorem. Otherwise let \(C\) be its unique cycle and put \(W=W_C\). The noncycle edges induce a forest. For a desired target offset class \(t\in V\), first choose a subset of cycle-edge reversals whose labels have image \(t+W\) in \(V/W\). This is possible because all exchange labels together span \(V\). If these reversals make the cycle directed, change them on a nonempty proper subset from Theorem 2; the quotient class is unchanged, but the cycle becomes nondirected. The remaining difference in \(V\) lies in \(W\), so choose orientations of noncycle edges to match it, using their spanning definition. Regardless of those tree-edge orientations, the full orientation of \(H_A\) remains acyclic because its only possible undirected cycle is not directed. Topologically sort to obtain a total direction order \(\pi\), then solve \(Ax=w+\alpha+r_\pi\). The prescribed profile follows. All operations are polynomial-time linear algebra or graph algorithms. \(\square\)

**Nonforest example.** In dimension five, take the binary row masks
\[
(A_0,A_1,A_2,A_3,A_4)=(2,13,2,7,8),
\]
meaning
\[
c_0=x_1+\alpha_0,\quad c_1=x_0+x_2+x_3+\alpha_1,\quad
c_2=x_1+\alpha_2,\quad c_3=x_0+x_1+x_2+\alpha_3,\quad
c_4=x_3+\alpha_4.
\]
Every row has odd weight and zero diagonal. The cokernel has dimension two, with representatives \(v=(1,2,3,2,2)\) in a fixed two-bit basis. Its nonzero exchange-label graph has edges \(01,03,12,23,34\), containing the four-cycle \(0-1-2-3-0\) and a pendant edge \(34\). Independent dynamic programming confirms all four cokernel classes occur. Theorem 3 proves this directly and for all affine constants.

**Scope and methodological caution.** The cycle-transparency theorem holds for *every* legal affine matrix and identifies a universal forced relation near each cycle. The full-surjectivity corollary requires at most one cycle. For graphs with multiple interacting cycles, repairing one directed cycle may change other cycles, so Theorem 2 must not be interpreted as a global acyclic-orientation selection theorem. Neither result proves unrestricted affine or nonlinear NORI1.

## Odd paired-block nonlinear profile universality

# Odd paired-block profile universality with nonlinear later-bit gates

All sums are in F2. For a subset S of direction labels, write p_S(x)=sum_(i in S)x_i. A full-geodesic profile records the edge colors indexed by direction.

Lemma 1 (odd bipartite four-run ordering). Let U,V be disjoint nonempty direction sets of odd sizes, and define the cube-edge colors c_i(x)=beta_i+p_V(x) for i in U, c_j(x)=beta_j+p_U(x) for j in V, where beta_i are arbitrary constants. Fix any starting root x. A profile w is attained by some full direction order from x if and only if
sum_(i in U union V)(w_i+beta_i)=1+p_U(x)+p_V(x). (L1)
Consequently the rootwise profile image contains 2^(|U|+|V|-1) words and each prescribed word is attained from 2^(|U|+|V|-1) roots.

Proof. The vertex function Q(x)=p_U(x)p_V(x) has derivative Q(x)+Q(x+e_i) equal to the partner-block parity for any i. Along a full geodesic, the sum of these derivatives telescopes to Q(x)+Q(bar x)=1+p_U(x)+p_V(x), since both block sizes are odd. This proves necessity. For sufficiency, put z_i=w_i+beta_i+p_V(x) on U and z_i=w_i+beta_i+p_U(x) on V; (L1) makes the total number of ones in z odd. Write U0,U1,V0,V1 for the four lists partitioned by z value, and a=|U1|, b=|V1|. When a is odd and b even, take the direction order U0,V0,U1,V1. The number of preceding V-moves has parity zero on U0 and one on U1 because |V0| is odd; the number of preceding U-moves is even on V0 because |U0| is even, and odd on V1 because |U| is odd. This realizes z, hence w. When a is even and b odd, use V0,U0,V1,U1, with the symmetric verification. For any prescribed w, condition (L1) is one nonzero root-bit parity equation, giving the root count. QED.

Theorem 2 (arbitrary nonlinear one-way gates). Partition all n dimensions into r ordered pairs of odd-sized nonempty blocks (U_t,V_t), 1<=t<=r. Set L_t=union_(s>t)(U_s union V_s). For every individual direction i in U_t union V_t choose alpha_i in F2 and an arbitrary Boolean function f_i on the L_t bits satisfying f_i(bar z)=f_i(z). Define c_i(x)=alpha_i+p_(V_t)(x)+f_i(x_(L_t)) for i in U_t, and c_i(x)=alpha_i+p_(U_t)(x)+f_i(x_(L_t)) for i in V_t. Then c is a legal antipodally odd edge coloring, and every binary direction-indexed profile is attained by a full antipodal geodesic. All witnesses can use orders that traverse the block pairs in sequence, with at most four runs inside each pair.

More strongly, for any fixed starting vertex x, the profiles attained by these pair-consecutive direction orders are precisely the solutions w to the r parity equations
sum_(i in U_t union V_t)(w_i+alpha_i+f_i(x_(L_t)))=1+p_(U_t)(x)+p_(V_t)(x), 1<=t<=r. (L2)
They form an affine subspace of codimension r and size 2^(n-r). For each prescribed w, the number of roots satisfying (L2) is 2^(n-r), and all such roots admit a pair-consecutive geodesic with profile w.

Proof. An old-direction rule is unchanged on its undirected edge because it reads only its opposite block and later blocks. Under global antipodal translation the parity of its opposite odd block flips and the even gate f_i does not, establishing legality. During traversal of the t-th pair, later bits remain fixed and earlier bits do not occur in that pair's rules. The frozen pair coloring therefore has the form of Lemma 1, with constants beta_i=alpha_i+f_i(x_(L_t)). Lemma 1 establishes (L2), including the sufficiency by four-run order for each pair. The r conditions involve disjoint target-bit sets and hence have rank r for fixed x. To prescribe w and choose a starting root, process pairs from r backwards to 1. Once the later root bits are chosen, the t-th equation requires only one parity on the current pair's root bits and permits 2^(|U_t|+|V_t|-1) assignments. Their product is 2^(n-r). For every resulting root, concatenate the four-run direction orders supplied by Lemma 1. QED.

The gates may have unbounded Boolean degree and vary independently with i. For instance, if there are r>=3 pairs, take f_i(x)=product_(s>t)(x_(u_s)+x_(v_s)) for all i in U_t with t<=r-2, where u_s in U_s and v_s in V_s are fixed representatives. Each factor is antipodally even; the earliest gate has degree r-1. Taking |U_t|=|V_t|=3 gives 3(r-2) nonlinear rows of degree at least two.

Theorem 3 (affine odd-clone lift with matched invertible core). Let m be even and B in GL_m(F2) satisfy B_aa=0, B*1=1, and B_(2t-1,2t)=B_(2t,2t-1)=1 for each matching pair. Partition [n] into odd-sized nonempty blocks D_1,...,D_m. For i in D_a set
c_i(x)=alpha_i+sum_(b=1)^m B_ab p_(D_b)(x). (L3)
Then c is legal and antipodally odd, its affine reader matrix has rank m, and every full direction-indexed color profile occurs.

Proof. Let p_b be the initial parity of D_b. When the pair (D_(2t-1),D_(2t)) is traversed after all earlier pairs, the frozen part of the color in D_a equals alpha_i+(Bp)_a+sum_(b<2t-1)B_ab, and every preceding direction of its matched block toggles that color once. For any prescribed profile, Lemma 1 allows choosing arbitrary effective phases for each matched pair subject only to one selectable odd parity condition; choose them to support a four-run order. This determines the desired vector q=Bp, because the earlier-completed-block correction is known for every a. Invert B to obtain p, select root bits with those block parities, and concatenate the matched-pair four-run orders. The reader matrix is the composition of the surjective block-parity map, invertible B, and injective block-repetition map, proving rank m. QED.

Corollary. For any odd p,q>=1, the complete bipartite reader graph K_(p,q) gives a legal affine coloring of rank 2 and corank p+q-2 whose exchange graph has (p-1)(q-1) independent cycles; its complete profile support follows from Theorem 3. For any even m, B=I+J (J the all-one matrix) satisfies B^2=I and has reciprocal pairs; all complete multipartite reader graphs with m odd-sized classes therefore satisfy the same full-profile conclusion with rank m, regardless of their many interacting cycles.

Independent tests used randomly generated antipodally even truth-table gates separately for every direction in Q_10, Q_12 and Q_14, constructing 1,000 prescribed profiles per instance and checking legality. The affine matched-core construction was checked on 250-300 prescribed targets in dimensions 6, 10 and 16. These are finite audits of the dimension-uniform proofs. The result covers unrestricted nonlinear complexity inside one-way gated paired-block systems but does not establish NORI1 for arbitrary legal colorings.

## Cyclic paired-gate feedback and Boolean fixed-point obstructions

## Cyclic paired-gate feedback encodes Boolean fixed points

Let \(r\ge1\), with \(2r\) directions named \(a_t,b_t\) for \(1\le t\le r\). Write \(u_t=x_{a_t}\), \(v_t=x_{b_t}\), and \(p_t=u_t+v_t\), with arithmetic in \(\mathbb F_2\). Choose arbitrary Boolean functions \(f_t:\mathbb F_2^{r-1}\to\mathbb F_2\), each acting on the list of parities \(p_s\), \(s\ne t\), and define
\[
\boxed{c_{a_t}(x)=v_t+f_t(p_{-t}),\qquad c_{b_t}(x)=u_t.}\tag{FB1}
\]
Every direction rule is constant along its own undirected edge. Antipodal translation changes \(u_t,v_t\) individually but preserves every parity \(p_s\), so (FB1) is a legal antipodally odd coloring in every dimension \(2r\).

Let a *pair-consecutive* direction order be one in which the two directions \(a_t,b_t\) of each pair are adjacent, while the \(r\) pairs may be permuted and oriented internally. For a target direction-indexed profile \(w\), define \(b_t=1+w_{a_t}+w_{b_t}\) and the Boolean map \(T_f(p)=(p_t+f_t(p_{-t}))_{t=1}^r\).

**Theorem 1 (feedback-profile fiber formula).** The number of rooted oriented full antipodal geodesics of (FB1) with profile \(w\) and a pair-consecutive order is
\[
\boxed{N_w^{\mathrm{pc}}=2^r\,r!\,|\{p\in\mathbb F_2^r:T_f(p)=b\}|.}\tag{FB2}
\]
In particular, a red pair-consecutive full geodesic exists if and only if \(T_f(p)=\mathbf1\) is solvable.

*Proof.* When the two directions of pair \(t\) are consecutive, every other pair is either entirely untouched or entirely traversed. Thus its parity \(p_s\) has its starting value during the two steps of pair \(t\). If \(a_t\) is followed by \(b_t\), the corresponding profile bits are \(w_{a_t}=v_t+f_t(p_{-t})\), \(w_{b_t}=u_t+1\). If \(b_t\) is followed by \(a_t\), they are \(w_{b_t}=u_t\), \(w_{a_t}=v_t+1+f_t(p_{-t})\). In both orders,
\[
w_{a_t}+w_{b_t}=1+p_t+f_t(p_{-t}).\tag{FB3}
\]
Conversely, if (FB3) matches the target pair-bit sum, then for a fixed root precisely one of the two internal orders yields the two individually prescribed colors: switching the internal order complements both profile bits. For each admissible parity vector \(p\) there are \(2^r\) starting roots realizing it, each pair has one forced internal order, and the \(r\) pairs can be permuted in \(r!\) ways without changing their parity inputs. This proves (FB2). \(\square\)

**Theorem 2 (arbitrary Boolean fixed-point realization).** Let \(F:\mathbb F_2^r\to\mathbb F_2^r\) be an arbitrary Boolean map, represented by a Boolean circuit. Construct a legal odd coloring of \(Q_{4r}\) with \(2r\) named pairs, \(P_i=(a_i,b_i)\) and \(Q_i=(c_i,d_i)\). Define the pair parities \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{c_i}+x_{d_i}\), and direction-color rules
\[
\begin{array}{ll}
c_{a_i}=x_{b_i}+q_i, & c_{b_i}=x_{a_i},\\
c_{c_i}=x_{d_i}+F_i(p), & c_{d_i}=x_{c_i}.
\end{array}\tag{FB4}
\]
All gates read only other pairs' parities, so this belongs to the cyclic paired-gate family (FB1). The rooted oriented red full-geodesic count among orders keeping every \(P_i\) and \(Q_i\) consecutive is
\[
\boxed{2^{2r}(2r)!\,|\operatorname{Fix}(F)|.}\tag{FB5}
\]
In particular, such a red geodesic exists if and only if \(F\) has a fixed point.

*Proof.* Applying (FB3) with target profile zero to the \(P_i\) pair yields \(p_i+q_i=1\); applying it to \(Q_i\) yields \(q_i+F_i(p)=1\). Eliminating \(q\) gives \(F_i(p)=p_i\) for all \(i\). Each fixed point \(p\) determines \(q=\mathbf1+p\); the \(2r\) pair parities admit \(2^{2r}\) starting roots, each has a unique red orientation within each pair, and all \((2r)!\) orders of the pairs succeed. \(\square\)

**Corollary 3 (SAT universality of static pair schedules).** For a Boolean formula \(\psi(z_1,\ldots,z_r)\), set \(F_1(z)=z_1+1+\psi(z)\) and \(F_i(z)=z_i\) for \(i>1\). Then \(\operatorname{Fix}(F)=\{z:\psi(z)=1\}\), so the legal odd edge-coloring in (FB4) has a red pair-consecutive full geodesic if and only if \(\psi\) is satisfiable. With Boolean-circuit encodings of the color rules, existence of a red pair-consecutive antipodal geodesic is NP-complete even for the family (FB4), and counting such rooted ordered red geodesics determines the number of satisfying assignments after division by \(2^{2r}(2r)!\). This is a restricted scheduling problem; it does not claim NP-hardness or failure of unrestricted monochromatic geodesic existence.

**Four-dimensional obstruction repaired by interleaving.** Let \(r=2\), \(f_1(p_2)=p_2\), and \(f_2(p_1)=p_1+1\). Then the pair-consecutive all-red conditions are \(p_1+p_2=1\) and \(p_1+p_2=0\), so no such path exists. Nevertheless, from root \((u_1,v_1,u_2,v_2)=(0,0,0,0)\), the order
\[
\boxed{b_1,\ b_2,\ a_1,\ a_2}\tag{FB6}
\]
has four red edges and terminates at the antipode. The second pair's parity is temporarily toggled when the first \(a\)-direction is evaluated; this defeats the inconsistent static parity constraints.

**Finite feedback audit, not a universal theorem.** For \(r=3\), all \(16^3=4096\) choices of the functions \(f_t:\mathbb F_2^2\to\mathbb F_2\) were enumerated. Each corresponding legal odd \(Q_6\) coloring attained all 64 direction-indexed profiles using direction orders with at most two simultaneously open pairs (a pair is open after its first and before its second step). In 816 instances pair-consecutive orders already attained all profiles; in the other 3280 some profile required interleaving. Random samples for \(r=4\) likewise had width-two profile witnesses. These finite observations do not establish a dimension-uniform width-two theorem.

The reduction identifies a limitation of any argument that assumes the parity equations of cyclically dependent interfaces can always be solved simultaneously: such equations represent arbitrary Boolean fixed-point problems. Allowing interleaving introduces intermediate-state changes absent from those static equations. The existence of full monochromatic geodesics without pair-consecutive restriction remains a separate question.

## Three-phase parity reset eliminates arbitrary nonlinear feedback

## Three-phase reset theorem: arbitrary cyclic pair-feedback gates are profile-universal

Let \(r\ge1\) and index \(2r\) cube directions by \(a_i,b_i\) (\(i\in[r]\)). Write \(u_i=x_{a_i}\), \(v_i=x_{b_i}\) and \(p_i=u_i+v_i\). For every \(i\), let \(f_i:\mathbb F_2^{[r]\setminus\{i\}}\to\mathbb F_2\) be an unrestricted Boolean function (there is no acyclicity, locality, degree, or rank hypothesis), and define
\[
\boxed{c_{a_i}(x)=v_i+f_i(p_{-i}),\qquad c_{b_i}(x)=u_i.}\tag{TR1}
\]
Every rule ignores its own direction bit. Global antipodal translation complements \(u_i,v_i\), but preserves each \(p_j\), so the coloring is legal and antipodally odd.

**Theorem 1 (unrestricted feedback profile universality).** For every coloring (TR1), every prescribed direction-indexed binary profile \(w\in\mathbb F_2^{2r}\) occurs on a full antipodal geodesic. In symbols,
\[
\boxed{\mathcal W(c)=\mathbb F_2^{2r}.}\tag{TR2}
\]
More strongly, fix any order \(\sigma\in S_r\) of the \(a_i\)-directions. There is a constructive full geodesic with profile \(w\), using the following three-phase form: an initial group of selected \(b\)-directions, then the \(a\)-directions in order \(\sigma\), then the remaining \(b\)-directions. Its initial vertex and the membership of the two \(b\)-groups are obtained with precisely \(r\) evaluations of the Boolean gates.

*Proof.* For \(i\ne j\) define \(k_{ij}=[a_j\text{ precedes }a_i\text{ in }\sigma]\), and regard \(k_{i,-i}\in\mathbb F_2^{r-1}\) as a fixed input for the \(i\)-th gate. For the desired profile \(w\), set
\[
\boxed{p_i=1+w_{a_i}+w_{b_i}+f_i(k_{i,-i}),}\tag{TR3}
\]
\[
\boxed{u_i=w_{b_i}+1+p_i,\qquad v_i=u_i+p_i.}\tag{TR4}
\]
Start at the vertex with the indicated \(u_i,v_i\). First traverse every direction \(b_i\) for which \(p_i=1\), in arbitrary order. Second traverse all \(a_i\) in order \(\sigma\). Third traverse all \(b_i\) with \(p_i=0\), in arbitrary order.

After phase one, \(v_i\) has become \(u_i\) for every \(i\), since the initial \(b_i\)-bit differs from \(u_i\) by \(p_i\) and \(b_i\) is flipped once precisely when \(p_i=1\). Thus every pair parity is zero before phase two. During phase two, just before \(a_i\), the current pair-parity vector outside \(i\) is precisely \(k_{i,-i}\), independently of the starting vertex. Furthermore \(v_i=u_i\) before \(a_i\), so
\[
c_{a_i}=u_i+f_i(k_{i,-i})=w_{a_i}
\]
by (TR3)-(TR4). For the direction \(b_i\), if \(p_i=1\), it was traversed in phase one and its color was \(u_i=w_{b_i}\). If \(p_i=0\), it is traversed in phase three, after \(a_i\) has flipped \(u_i\), so its color is \(u_i+1=w_{b_i}\). Every direction is used once. Therefore the path is a full antipodal geodesic and has all prescribed colors. \(\square\)

**Corollary 2 (many constructive witnesses and oracle complexity).** For every target \(w\), each one of the \(r!\) orders \(\sigma\) gives a rooted, ordered full geodesic of profile \(w\), with different orders on the \(a_i\). Consequently
\[
\boxed{G_c(w)\ge r!\qquad\text{for all }w.}\tag{TR5}
\]
For a fixed \(\sigma\), only the \(r\) Boolean values \(f_i(k_{i,-i})\) are queried. The root and path are constructed with \(O(r^2)\) elementary operations, apart from those queries, regardless of the functions' Boolean degree or circuit complexity. For fixed \(\sigma\) and \(w\), the root and partition of \(b\)-steps in this particular three-phase scheme are uniquely determined by (TR3)-(TR4).

**Corollary 3 (static SAT-hardness versus unrestricted constructive solvability).** The earlier fixed-point encoding remains valid: restricting (TR1) to pair-consecutive orders makes existence of a red full geodesic equivalent to a Boolean fixed-point equation and is NP-complete under circuit input. Removing that restriction yields the explicit algorithm of Theorem 1. Thus the SAT obstruction is solely an artifact of forbidding dynamic interleaving; arbitrary Boolean feedback does not obstruct full profiles in this entire family. The theorem supersedes the previous uncertainty about unrestricted profile attainment for (TR1); whether two simultaneously open pairs always suffice is a separate bounded-width scheduling question and is not needed for NORI1 closure within this family.

**Gauge-reset interpretation.** Phase one moves the root onto the diagonal subcube \(\{x_{a_i}=x_{b_i}\ \forall i\}\); phase two evaluates all nonlinear feedback gates on a completely predetermined chain of pair-parity states \(0,e_{\sigma_1},e_{\sigma_1}+e_{\sigma_2},\ldots\); phase three completes the antipodal traversal. This temporary reset breaks every apparent feedback cycle without solving any fixed-point equation.

**Independent audit.** Implemented the construction with independently sampled unrestricted Boolean truth tables for each gate, random profiles and random \(\sigma\). Verified legality by symbolic inspection and directly simulated 300 target profiles per sample in dimensions \(4,6,8,10,16,24\), all successful. These finite tests supplement the dimension-uniform proof.

*Scope.* The theorem covers cyclic dependence of arbitrary complexity through other pairs' XOR parities, with the private \(b_i\)-directions serving as resettable auxiliary bits. It does not establish a comparable reset mechanism for an arbitrary legal odd coloring of \(Q_n\); in particular a counterexample-preserving paired lift need not possess these programmable scratch-bit rules.
