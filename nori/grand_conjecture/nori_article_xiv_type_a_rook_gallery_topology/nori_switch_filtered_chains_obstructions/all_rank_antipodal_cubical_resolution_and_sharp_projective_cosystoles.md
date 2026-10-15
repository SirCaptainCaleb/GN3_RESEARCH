# All-rank antipodal cubical resolution and sharp projective cosystoles

# All-rank antipodal cubical resolution and sharp projective cosystoles

The canonical exchange disks of Article XIV, Subsection 28, are the degree-two part of a uniform **all-rank cubical chain construction**. The construction preserves the set of free dimensions and realizes every nonzero projective cohomology class \(u^k\) by a fixed-dimension incidence cocycle with the minimum possible support. Its degree-one term is a full antipodal geodesic. No edge-color restriction is imposed.

Work with cubical cellular chains over \(\mathbb F_2\). Let \(Q_n=[0,1]^n\), with central antipodal involution \(\tau_n\). Put \(E_0^{(0)}=[*]\), and set \(E_k^{(n)}=0\) for \(k<0\) or \(k>n\). Recursively define
\[
E_0^{(n)}=E_0^{(n-1)}\times\{0\},
\]
\[
\boxed{E_k^{(n)}
=E_k^{(n-1)}\times\{0\}
+\tau_{n-1}E_{k-1}^{(n-1)}\times[0,1],
\qquad k\ge1.}
\tag{1}
\]

**Theorem 1 (antipodal chain resolution).** For every \(n\ge1\) and \(1\le k\le n\),
\[
\boxed{\partial E_k^{(n)}=(1+\tau_n)E_{k-1}^{(n)}.}
\tag{2}
\]
The chain \(E_k^{(n)}\) consists of \(\binom nk\) different \(k\)-faces, containing **one face for every \(k\)-element set of free dimensions**, each with coefficient one.

*Proof.* In (1), the first summand contributes the faces whose free sets omit dimension \(n\), while the second contributes those whose free sets contain \(n\); induction gives precisely one per \(k\)-subset. For the boundary identity, use the cubical product formula:
\[
\begin{aligned}
\partial E_k^{(n)}
={}&(1+\tau_{n-1})E_{k-1}^{(n-1)}\times0\\
&+\tau_{n-1}(1+\tau_{n-1})E_{k-2}^{(n-1)}\times[0,1]\\
&+\tau_{n-1}E_{k-1}^{(n-1)}\times(0+1)\\
={}&E_{k-1}^{(n-1)}\times0+
\tau_{n-1}E_{k-1}^{(n-1)}\times1\\
&+(1+\tau_{n-1})E_{k-2}^{(n-1)}\times[0,1]\\
={}&(1+\tau_n)E_{k-1}^{(n)}.
\end{aligned}
\]
For \(k=1\), replace \(\partial E_0\) by zero in the same calculation; its boundary is the sum of the origin and its antipode. \(\square\)

For any root \(x\) and permutation \(\pi\) of the \(n\) dimensions, transport \(E_k^{(n)}\) under the cube automorphism sending the standard origin to \(x\) and the standard dimension order to \(\pi\). Denote the resulting chain \(E_k(x,\pi)\). Central antipodality commutes with the transport, so (2) remains valid.

**Proposition 2 (recovering the geodesic and exchange disk).** The chain \(E_1(x,\pi)\) is the length-\(n\) antipodal geodesic \(P(x,\pi)\). The chain \(E_2(x,\pi)\) equals the canonical exchange disk
\[
\Sigma_P=\sum_{i<j} F_{\{d_i,d_j\}}
\left(x\oplus\bigoplus_{r=i}^{j-1}e_{d_r}\right)
\tag{3}
\]
from Subsection 28.

*Proof.* At \(k=1\), recursion (1) follows the first \(n-1\) dimensions, and then traverses the final dimension at the antipodal endpoint of the partial geodesic. At \(k=2\), its first summand supplies the squares of (3) not involving the final dimension, while its second is the antipodal image of the partial geodesic crossed with the final interval. These are precisely the squares in (3) involving the final dimension. Induct on \(n\). \(\square\)

## Theorem 3 (canonical generators in every projective rank)

For \(1\le k\le n-1\), all \(k\)-faces of \(E_k(x,\pi)\) lie on \(B_n=\partial Q_n\). Let \(Y_n=B_n/\tau_n\cong\mathbb{RP}^{n-1}\), with quotient map \(p\), and set
\[
Z_k(x,\pi)=p_*E_k(x,\pi).
\]
Equation (2) shows that \(Z_k\) is a \(k\)-cycle. For any \(I\subseteq[n]\), \(|I|=k\), let \(K_I\) be the invariant cubical \(k\)-cochain which evaluates to one on a \(k\)-face if its free dimension set is \(I\), and zero otherwise. It descends to a cocycle \(\bar K_I\) on \(Y_n\). If \(u\in H^1(Y_n;\mathbb F_2)\) is the canonical generator, then
\[
\boxed{
[\bar K_I]=u^k,\qquad
[Z_k(x,\pi)]\ne0\in H_k(Y_n;\mathbb F_2),\qquad
\langle\bar K_I,Z_k(x,\pi)\rangle=1.
}
\tag{4}
\]

*Proof.* Each \((k+1)\)-face contains either no \(k\)-facets with free dimensions \(I\), or a pair of opposite such facets. Thus \(\delta\bar K_I=0\). By Theorem 1, each \(E_k(x,\pi)\) has one \(k\)-face with free set \(I\), so its pairing with \(K_I\), and hence the downstairs pairing in (4), is one. Both homology and cohomology in degree \(k\) of \(\mathbb{RP}^{n-1}\) are one-dimensional over \(\mathbb F_2\); their nonzero classes are the desired generators. \(\square\)

## Theorem 4 (sharp projective cocycle support in all degrees)

For every \(1\le k\le n-1\), a cubical \(k\)-cocycle \(\eta\) representing \(u^k\) on \(Y_n\) must have nonzero values on at least
\[
\boxed{2^{n-k-1}}
\tag{5}
\]
antipodal orbits of \(k\)-faces. This bound is sharp, attained by every fixed-free-set indicator \(\bar K_I\).

*Proof.* Every projected chain \(Z_k(x,\pi)\) is a nonzero homology generator, so its pairing with \(\eta\) is one. Hence every lifted chain \(E_k(x,\pi)\) contains at least one face in the lifted support of \(\eta\). There are \(2^nn!\) rooted dimension permutations and \(\binom nk\) faces in each \(E_k\). The cube automorphism group acts transitively on the \(\binom nk2^{n-k}\) \(k\)-faces and permutes the canonical chains. Thus every fixed \(k\)-face occurs in
\[
\frac{(2^nn!)\binom nk}{\binom nk2^{n-k}}=2^kn!
\]
canonical chains, counting root-and-order choices. If the lifted support contains \(M\) faces, double counting gives
\[
2^nn!\le M\,2^kn!,\qquad M\ge2^{n-k}.
\]
All proper cube faces occur in free antipodal pairs, so downstairs there are at least \(M/2\ge2^{n-k-1}\) supported orbits. The indicator \(K_I\) is supported on the \(2^{n-k}\) faces with one prescribed free dimension set \(I\); it attains the bound. \(\square\)

**Corollary 5 (primary obstruction admits a sparse projective representative).** The primary obstruction for the signed-second-switch map in Article XIV, Subsection 25, has cohomology class \(u^{n-2}\). In the antipodal cubical cellulation, the same cohomology class has a representative \(\bar K_I\), \(|I|=n-2\), supported on only **two antipodal orbits** of \((n-2)\)-faces. This is a statement about cohomology classes in different cellulations; it does not assert that the color-dependent obstruction degrees themselves concentrate on those cells.

**Connection to the Wu–Yang adaptation.** The boundary relation (2) realizes the antipodal two-periodic free chain resolution through all dimensions on ordinary cubical faces, retaining a distinct \(k\)-dimensional support for each \(k\)-subset of dimensions. The previously identified antipodal geodesics, canonical exchange disks, and adjacent-swap three-cube corrections belong to this same chain geometry. We no longer need to invent an uncolored, rank-preserving antipodal chain system: the one in (1) is explicit. The remaining research problem is to lift its boundary relation through color-sensitive reachability and ordered-path incidence data while preserving the topological obstruction. None of the results here assumes a specialized coloring or proves the NORI1 existence conjecture.


## Rigidity of minimum degree-one support

**Theorem 6.** A projective cubical one-cocycle representing the generator \(u\in H^1(\mathbb RP^{n-1};\mathbb F_2)\), \(n\ge3\), has at least \(2^{n-2}\) supported projective edges. Equality holds only for a whole cube-dimension edge class. More precisely, its pullback is the edge boundary of an antipodally odd sign function \(f:Q_n\to\{\pm1\}\), and
\[
|B|=2^{n-2}\left(1+\sum_{\substack{|S|\ge3\\|S|\text{ odd}}}(|S|-1)\widehat f(S)^2\right).
\]
*Proof.* The pullback is a coboundary because \(H^1(S^{n-1};\mathbb F_2)=0\). The nonzero projective period forces \(f(\bar x)=-f(x)\), so its Walsh spectrum contains only odd levels. Counting the lifted boundary edges by Boolean influence, and using Parseval, yields the formula. Equality means that \(f\) has Fourier degree one. The Boolean identity \(f^2=1\) forces at most one linear Fourier coefficient to be nonzero, making \(f=\pm(-1)^{x_i}\). Its boundary is the full dimension-\(i\) edge class. \(\square\)

**Theorem 7 (transversal equality).** A set of projective edges meeting every complete dimension-simple Petrie cycle has at least \(2^{n-2}\) members. At equality it must be one complete dimension class.
*Proof.* Each projective edge occurs in \((n-1)!\) Petrie cycles, and there are \(2^{n-2}(n-1)!\) cycles. Equality in double counting means every cycle meets the set once. The symmetric difference of two cycles obtained by adjacent-dimension exchange is a projective square boundary, so the edge set has zero square coboundary. It has odd period along every Petrie cycle, hence represents \(u\). Apply Theorem 6. \(\square\)

The Fourier identity also gives spectral stability: support at most \((1+\varepsilon)2^{n-2}\) implies total Fourier mass above degree one at most \(\varepsilon/2\).
