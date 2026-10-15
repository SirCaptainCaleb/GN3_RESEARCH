# Universal positive-prefix collisions and global parity

# Universal positive-prefix collisions and global odd parity

Let \(n\ge3\), \(d=n-2\), and let \(P_n\) be the centered permutahedron in \(W=\{z\in\mathbb R^n:\sum z_i=0\}\), with antipodal boundary involution \(R\) reversing complete orders. For each order \(\pi\), suppose we choose two distinct proper prefix ranks
\[
1\le p(\pi)<q(\pi)\le n-1,\qquad
p(\pi^R)=n-q(\pi),\quad q(\pi^R)=n-p(\pi).
\tag{1}
\]
These include the first and last color-switch prefix ranks of reversal-complementary binary color words with at least two switches. This covers both fixed-root NORI1 geodesic words in a hypothetical counterexample and the reversal-odd boundary triple words in a hypothetical one-switch counterexample.

Define \(Z_j(\pi)=\sum_{h\le j}e_{\pi_h}-(j/n)\mathbf1\) and vertex labels \(X_\pi=Z_{p(\pi)}(\pi)\), \(Y_\pi=Z_{q(\pi)}(\pi)\). Interpolate affinely on a centrally symmetric triangulation of \(\partial P_n\), for instance by assigning each face barycenter the average of its vertex labels. Write the resulting continuous maps as \(X,Y:\partial P_n\to W\).

**Theorem 1 (positive-prefix symmetry and degree).** Let \(S=X+Y\), \(D=X-Y\). They satisfy
\[
\boxed{S(Rz)=-S(z),\qquad D(Rz)=D(z),\qquad S(z)\ne0.}
\tag{2}
\]
The normalized antipodal sphere map \(S/\|S\|:\partial P_n\to S(W)\) has integer degree \(+1\), with the usual orientation induced by the permutahedron. Moreover \(X(z)\) and \(Y(z)\) can never be negatively proportional.

*Proof.* For a proper nonempty first-block subset \(A\subset[n]\), the centered block vector \(T_A=\mathbf1_A-(|A|/n)\mathbf1\) satisfies, at every order refining its facet,
\[
\langle T_A,Z_j(\pi)\rangle
=\min(j,|A|)-j|A|/n>0
\quad(1\le j<n).
\tag{3}
\]
Positive affine interpolation retains this inequality throughout the facet. Every boundary point belongs to a facet, so X,Y,S are nowhere zero and X,Y are not negatively proportional. Prefix reversal gives \(Z_{n-j}(\pi^R)=-Z_j(\pi)\), which yields \(X(Rz)=-Y(z)\), \(Y(Rz)=-X(z)\), and (2). On every facet, both X and the source permutahedral position vector lie in the common strict open halfspace (3). Straight-line interpolation therefore homotopes normalized X to the identity radial map. The homotopy \(X+tY\) likewise never vanishes. Thus normalized S has degree \(+1\). \(\square\)

**Theorem 2 (odd parity of positive collinearity orbits).** The two interpolated prefix maps have a point where \(X\) and \(Y\) are *positively proportional*. After a small generic equivariant perturbation maintaining the strict facet inequalities, their positive-collinearity set is finite and contains an odd number of antipodal pairs:
\[
\boxed{\#\{[z]\in\partial P_n/R:X(z)\parallel Y(z)\}
\equiv1\pmod2.}
\tag{4}
\]

*Proof.* Put \(Q=\partial P_n/R\cong\mathbb RP^d\). The odd nonzero map S defines a real line subbundle \(L\subset Q\times W\), with \(w_1(L)=\alpha\), the generator of \(H^1(Q;\mathbb F_2)\). Its orthogonal complement \(E=L^\perp\) has rank d. Since \(L\oplus E\) is trivial,
\[
w(E)=(1+\alpha)^{-1}
=1+\alpha+\cdots+\alpha^d,\qquad
\boxed{w_d(E)=\alpha^d\ne0.}
\tag{5}
\]
The even vector D projects orthogonally to the section
\[
s([z])=D(z)-\frac{\langle D(z),S(z)\rangle}{\|S(z)\|^2}S(z)\in E_{[z]}.
\tag{6}
\]
The formula is unchanged under R. A zero means D and S are linearly dependent, which, since S is nonzero, is equivalent to X and Y being linearly dependent. By Theorem 1 this dependence is positive. The top Stiefel–Whitney class forces a zero; for a transverse section it counts zero points modulo two. Its Stiefel–Whitney number on \(Q\) equals \(\langle\alpha^d,[Q]\rangle=1\), proving (4). \(\square\)

**Theorem 3 (sum of local two-block contraction indices).** Let \(F_A\) be the top permutahedral facet of full orders whose first block is a nonempty proper \(A\subset[n]\). On it set
\[
H_A=\iota_{T_A}(X\wedge Y)
=\langle T_A,X\rangle Y-\langle T_A,Y\rangle X
\in T_A^\perp\cap W.
\tag{7}
\]
This vanishes if and only if X and Y are positively proportional. After generic equivariant perturbation avoiding zeros on the proper facet boundaries, define the local mod-two degree
\[
\delta_A=\deg_2(H_A/\|H_A\|:\partial F_A\to S^{d-1}).
\]
Then \(\delta_{A^c}=\delta_A\) and
\[
\boxed{\sum_{\{A,A^c\}}\delta_A=1\pmod2.}
\tag{8}
\]
The sum runs over antipodal pairs of proper nonempty block cuts.

*Proof.* Both scalar products in (7) are positive on F_A, and a linear dependence of X and Y implies H_A=0; conversely, H_A=0 forces their dependence since the coefficients are nonzero. A generic perturbation of the section in Theorem 2 is transverse and has no zeros on the union of boundaries of top facets, a codimension-one subset. On each top ball the mod-two zero count equals its boundary degree. R pairs facets F_A and F_{A^c}, and each zero orbit has one representative per paired facet; sum the local parities over one representative from each pair. Theorem 2 gives (8). \(\square\)

**Conditional odd-dimensional terminal leakage.** If n is odd and every nonterminal two-block facet (both block sizes at least two) has switches straddling the block boundary at every vertex order, the earlier variable-prefix top-cell degree theorem gives \(\delta_A=1\) on those facets. Their number of antipodal pairs is \(2^{n-1}-n-1\), which is even for odd n. Equation (8) therefore forces
\[
\sum_{\{A,A^c\}:\min(|A|,|A^c|)=1}\delta_A=1\pmod2.
\tag{9}
\]
This is conditional, and for ordinary boundary triple colorings the straddling requirement cannot hold for all two-element first blocks because their first switch rank is at least two. It must not be invoked as an unconditional terminal-cell statement.

**Relation to the recent positive-carrier transport theorem.** The new Article XV result on homotopy-constant prefix carriers shows that, while preserving positive-carrier fillings, a homotopy modification in a three-block cell can toggle the two neighboring top-facet obstruction degrees. The graph of antipodal top-facet pairs under these incidences is connected. Consequently these allowable changes generate all even-parity degree changes, whereas (8) fixes the total parity to one. The position of the odd local degrees is therefore not itself a positive-carrier invariant; only their total parity is. A coloring-specific contradiction must use conditions stronger than prefix positivity, rank reversal, and the associated carrier homotopy type.

**Scope.** Theorems 1–3 hold for every rank assignment satisfying (1), whether or not it comes from a coloring. They do not turn a positive-collinearity point of *averaged prefix vectors* into one monochromatic geodesic, and they do not settle NORI1 or the boundary 3-tournament one-switch conjecture. Their role is to identify the universal parity that any color-sensitive obstruction must strengthen.

## Integral Euler refinement and the dimension-parity dichotomy

The odd collision parity can be sharpened to an integral zero-count in even cube dimension. Retain the notation \(d=n-2\), \(Q=\mathbb RP^d\), the sign line bundle \(L\) and rank-\(d\) orthogonal complement \(E=L^\perp\) from Theorem 2. Let \(\mathbb Z_\alpha\) denote the integral local system with monodromy \(-1\) around the nontrivial loop in \(Q\).

**Theorem 4 (Euler class of the positive-prefix collision bundle).** The Euler class with its orientation local system satisfies
\[
e(E)\in H^d(Q;\mathbb Z_\alpha),\qquad
\boxed{
H^d(Q;\mathbb Z_\alpha)\cong
\begin{cases}
\mathbb Z,&d\text{ even},\\
\mathbb Z/2,&d\text{ odd}.
\end{cases}}
\tag{10}
\]
For even \(d\), \(e(E)\) is a generator of the integer group and its signed evaluation on the twisted fundamental class is \(+1\) with the orientation induced by the degree-\(+1\) sum map of Theorem 1. For odd \(d\), \(e(E)\) is the unique nonzero element of \(\mathbb Z/2\). In both cases its mod-two reduction is the class \(\alpha^d\).

*Proof.* The bundle E has \(w_1(E)=\alpha\), because \(L\oplus E\) is trivial and \(w_1(L)=\alpha\). Its orientation local system is therefore \(\mathbb Z_\alpha\). By Poincare duality with local systems,
\[
H^d(Q;\mathbb Z_\alpha)
\cong H_0(Q;\mathbb Z_\alpha\otimes\mathcal O_Q).
\]
The orientation system of \(Q=\mathbb RP^d\) is the sign system when d is even and trivial when d is odd. The right-hand side is therefore \(\mathbb Z\) for even d and the sign coinvariants \(\mathbb Z/2\) for odd d, proving (10).

Let \(\rho:S^d\to Q\) be the antipodal two-sheeted covering and \(f=S/\|S\|:S^d\to S(W)\cong S^d\) the odd degree-\(+1\) map from Theorem 1. The lifted bundle \(\rho^*E\) is the orthogonal complement of the line spanned by \(f(z)\) in W, and hence
\[
\boxed{\rho^*E\cong f^*(TS^d).}
\tag{11}
\]
When d is even, \(e(TS^d)\) evaluates to \(\chi(S^d)=2\); the degree-one map f therefore gives \(\langle\rho^*e(E),[S^d]\rangle=2\). Pullback of a generator of \(H^d(Q;\mathbb Z_\alpha)\cong\mathbb Z\) to the sphere multiplies its top pairing by two, because \(\rho\) has twisted covering degree two. Thus \(e(E)\) evaluates to \(+1\) with compatible orientations.

When d is odd, the mod-two reduction of the twisted Euler class equals \(w_d(E)=\alpha^d\ne0\). The reduction map from \(H^d(Q;\mathbb Z_\alpha)\cong\mathbb Z/2\) onto top mod-two cohomology is an isomorphism in this degree, so \(e(E)\) is its unique nontrivial element. \(\square\)

**Corollary 5 (signed positive-collision index in even cube dimensions).** For even \(n\ge4\), a transverse equivariant perturbation of the positive-prefix difference section has finitely many antipodal collision orbits, carrying coherent local *integer* indices. The signed sum is
\[
\boxed{\sum_{\text{collision orbits}}\operatorname{ind}([z])=+1.}
\tag{12}
\]
For odd n, the corresponding signed local indices have orientation monodromy, and the canonical global total is their odd parity rather than an integer.

*Proof.* When n is even, \(d=n-2\) is even, and the orientation systems of E and the base Q agree. Therefore every transverse section zero carries an index in a globally consistent orientation convention, and the sum evaluates \(e(E)\) on the twisted fundamental class. Theorem 4 gives +1. When n is odd, the Euler group is \(\mathbb Z/2\); its nonzero class yields the odd parity in Theorem 2. \(\square\)

**Corollary 6 (contrast with the local oriented Grassmannian obstruction).** In dimensions \(n\ge6\), the top-cell homotopy obstruction in the *oriented two-plane Grassmannian* obeys
\[
\pi_{n-3}(\widetilde{\operatorname{Gr}}_2(\mathbb R^{n-1}))
\cong \mathbb Z/\chi(S^{n-2})\mathbb Z
=
\begin{cases}
\mathbb Z/2,&n\text{ even},\\
\mathbb Z,&n\text{ odd}.
\end{cases}
\]
This has the opposite dimension-parity pattern from (10). Thus the integer signed collision number in even dimensions is finer than the mod-two class retained by the local Grassmannian projection; preserving it requires a suitable framed or orthogonal-section lift. Conversely, in odd dimensions, local integer cell degrees can be moved by three-block carrier surgery, while the global collision obstruction records only their total parity.

**Scope.** This is an integral strengthening of the universal topological obstruction, not yet a coloring-specific contradiction. The signed count is determined already by the odd prefix-sum map and is therefore compatible with colorings that possess many monochromatic antipodal paths. Any intended use in NORI1 needs a new theorem tying the local indices to constraints imposed by edge colors and their root changes.

## Sharpness benchmark: every top facet can have degree one without coloring

The universal hypotheses (1) contain a distinguished *color-independent* rank selection,
\[
\boxed{p(\pi)=1,\qquad q(\pi)=n-1\quad\text{for every full order }\pi.}
\tag{13}
\]
It obeys the reversal rule for all \(n\ge3\). This model realizes the parity obstruction on every top two-block facet simultaneously.

**Theorem 7 (universal facet-barycenter coincidences).** For the ranks (13), every top permutahedral facet \(F_A\), indexed by a nonempty proper \(A\subset[n]\), has a positive-prefix collision at its barycenter \(b_A\). More precisely, with \(a=|A|\), \(b=n-a\) and \(T_A=\mathbf1_A-(a/n)\mathbf1\),
\[
\boxed{X(b_A)=\frac1aT_A,\qquad
Y(b_A)=\frac1bT_A.}
\tag{14}
\]
Moreover, every local two-block contraction degree satisfies
\[
\boxed{\delta_A=1\pmod2.}
\tag{15}
\]
Hence the collision parity from Theorem 3 is already witnessed by the odd count of top-facet pairs
\[
\boxed{\#\{F_A,F_{A^c}\}=2^{n-1}-1\equiv1\pmod2.}
\tag{16}
\]

*Proof.* On F_A, the first member of an ordering is uniformly distributed among the a members of A, while the final member is uniformly distributed among the b members of its complement B. Because \(Z_1(\pi)=e_{\pi_1}-(1/n)\mathbf1\) and \(Z_{n-1}(\pi)=(1/n)\mathbf1-e_{\pi_n}\), averaging the vertex labels gives
\[
X(b_A)=\frac1a\mathbf1_A-\frac1n\mathbf1
=\frac1aT_A,
\]
\[
Y(b_A)=\frac1n\mathbf1-\frac1b\mathbf1_B
=\frac1bT_A.
\]
This proves (14).

If \(2\le a,b\), the selected ranks satisfy \(1<a<n-1\). The established variable-prefix two-block product degree theorem therefore gives \(\delta_A=1\). If a=1, the first-prefix vector X is constant on F_A, equal to T_A, and the contracted map H_A is a positive multiple of the B-part of \(Y=Z_{n-1}\), the centered last-prefix vector on the permutahedron \(P_B\). Its normalized boundary map has degree \(\pm1\) by the standard permutahedral prefix degree theorem. If b=1, the symmetric argument uses the A-part of \(X=Z_1\), again obtaining degree \(\pm1\). Thus every cut has degree one modulo two. There are \(2^n-2\) proper nonempty subset-indexed facets, paired without fixed facets by complementation, giving (16). \(\square\)

**Consequences for proof strategy.** The universal odd collision count, even accompanied by a nonzero local obstruction on *every* top cell, cannot force a monochromatic geodesic without additional coloring identities: model (13) provides all these topological features without reference to edge or triple colors. For ordinary boundary triple colorings, first/last switch ranks must lie in \(\{2,\ldots,n-2\}\), so this illustrative selection is excluded by the switch window; additional restrictions like these, adjacent-exchange coloring constraints, and coherent root changes must be central in any closure argument.
