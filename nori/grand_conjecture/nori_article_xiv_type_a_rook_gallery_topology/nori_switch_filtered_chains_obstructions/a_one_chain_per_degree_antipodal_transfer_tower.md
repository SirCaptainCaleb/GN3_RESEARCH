# A one-chain-per-degree antipodal transfer tower

# A one-chain-per-degree antipodal transfer tower

Fix \(n\ge5\) and an antipodally odd coloring \(c:E(Q_n)\to\mathbb F_2\). Let \(K=K_0(c)\cup K_1(c)\) be the union of monochromatic geodesic endpoint-poset complexes, with the involution \(R(u,v)=(\bar v,\bar u)\) exchanging colors. Write \(C_j=C_j(K;\mathbb F_2)\), let \(\partial\) be simplicial boundary, and let \(\varepsilon:C_0\to\mathbb F_2\) be augmentation. Put \(q=\lfloor(n-1)/2\rfloor\).

**Definition.** An *antipodal chain tower of height \(q\)* consists of \(z_j\in C_j\), \(0\le j\le q\), with
\[
\boxed{\varepsilon z_0=1,\qquad
\partial z_j=(1+R)z_{j-1}\ (1\le j\le q).}
\tag{1}
\]
All chains have mod-two coefficients.

**Theorem 1 (cellular index detection).** If \(R\) acts freely on \(K\) and a tower (1) exists, then
\[
\boxed{w_1(K\to K/R)^q\ne0.}
\tag{2}
\]

*Proof.* The standard antipodal CW structure on \(S^q\), built by repeated suspension of \(S^0\), has one free \(\mathbb F_2[\mathbb Z_2]\)-generator \(e_j\) in each dimension \(0\le j\le q\), with cellular boundary \(\partial e_j=(1+R)e_{j-1}\). Sending \(e_j\mapsto z_j\), and extending equivariantly, defines an augmentation-preserving chain map into \(C_*(K)\). The Bockstein naturality theorem proved earlier in Article XIV shows that such a chain map preserves the powers of double-cover classes. Since the covering class on \(S^q/\mathbb Z_2=\mathbb RP^q\) has nonzero \(q\)-th power, (2) follows. \(\square\)

**Theorem 2 (equivalence with NORI1 existence).** For every legal antipodally odd coloring \(c\) of \(Q_n\), \(n\ge5\), the following are equivalent:

(i) There is a monochromatic full antipodal geodesic.

(ii) The endpoint complex \(K(c)\) admits a tower (1) of height \(q=\lfloor(n-1)/2\rfloor\).

*Proof.* If a monochromatic antipodal geodesic joins \(u\) to \(\bar u\), then the rank-\(n\) endpoint vertex \(p=(u,\bar u)\) belongs to \(K\) and satisfies \(Rp=p\). Take \(z_0=p\) and \(z_j=0\) for \(j\ge1\).

Conversely suppose (ii) holds and no such geodesic exists. Under this hypothesis \(R\) acts freely on \(K\): any fixed endpoint vertex has rank \(n\), and a simplex cannot be invariant without fixed vertices because ranks increase strictly within chains. The two-color endpoint rank-gap theorem, equivalently the seam-transgression corollary, gives
\[
w_1(K\to K/R)^{m+1}=0,\qquad m=\lfloor(n-3)/2\rfloor.
\]
But \(q=m+1\), contradicting Theorem 1. Thus (i) holds. \(\square\)

**Theorem 3 (homological continuation obstruction).** If \(z_0,\ldots,z_{j-1}\) satisfy the tower equations up to degree \(j-1\), define
\[
\boxed{\omega_{j-1}=(1+R)z_{j-1}.}
\tag{3}
\]
For \(j=1\), this is an augmentation-zero zero-cycle. For \(j\ge2\),
\[
\partial\omega_{j-1}=(1+R)\partial z_{j-1}
=(1+R)^2z_{j-2}=0.
\]
The tower extends through degree \(j\) if and only if the homology class of \(\omega_{j-1}\) vanishes (using reduced degree-zero homology for \(j=1\)). The obstruction may depend on prior chain choices.

**Corollary 4 (necessary homology of a hypothetical counterexample).** Suppose no monochromatic full antipodal geodesic exists. Then either \(K\) has no connected component preserved by \(R\), or every preserved connected component \(C\) has nonzero \(H_j(C;\mathbb F_2)\) for some \(1\le j\le q-1\).

*Proof.* In an \(R\)-preserved component, choose a vertex \(p=z_0\); connectedness supplies \(z_1\) with boundary \(p+Rp\). If all the stated homology groups vanish, the cycles (3) bound successively through degree \(q\), creating a tower forbidden by Theorem 2. \(\square\)

**Implication.** Instead of assigning exponentially many compatible target chains to Coxeter flags, one may seek just \(q+1\) mod-two chains satisfying (1), one per degree. The problem is not thereby solved: existence of a full tower is equivalent to the sought monochromatic complete geodesic, rather than established for every coloring. The advantage is a sequence of explicit homological obstructions at each degree, amenable to the dimension-support filtration and exchange relations already present in Article XIV.
