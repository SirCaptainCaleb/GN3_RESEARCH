# Affine colorings, exterior-bit control, and lifting obstructions

# Affine face colorings and exterior-coordinate control

For an ordered three-face \((F,\pi)\), its exterior-bit vector consists of the coordinates fixed outside the free triple \(\pi\). This section isolates classes in which the dependence on those bits can be controlled algebraically, and explains why local lifting arguments must preserve their actual physical positions. The strongest general method is an explicit root-solving recurrence, which works even without antipodal oddness.

## Exact root count in the exterior-parity class

**Theorem (exterior-parity twist, arbitrary window length).** Fix integers 1≤k≤n, a coordinate order p=(p_1,…,p_n), and any binary function f of ordered k-tuples of distinct coordinates. For each ordered k-face (F,σ), let
c(F,σ)=f(σ) ⊕ (⊕_{u∉free(F)} b_u(F)),
where b_u(F) is the constant bit of coordinate u on F and ⊕ denotes addition in F_2. Then **exactly 2^k starting vertices** yield a monochromatic sequence of all n−k+1 ordered k-face windows along the antipodal geodesic with direction order p. In particular, for k=3 exactly eight starts work for **every fixed permutation**, for all n≥3, regardless of f.

**Proof.** Identify starting vertex bits in p-order by x_1,…,x_n and let X=⊕_{j=1}^n x_j. At window i, the first i−1 directions have been toggled. Its color is
w_i=f(p_i,…,p_{i+k−1}) ⊕ X ⊕ (⊕_{j=i}^{i+k−1}x_j) ⊕ ((i−1) mod 2).
We seek w_i=t for a single t∈F_2. Put q=X⊕t. Choose q and x_1,…,x_{k−1} freely, and successively define
x_{i+k−1}=f(p_i,…,p_{i+k−1}) ⊕ ((i−1) mod2) ⊕ q ⊕ (⊕_{j=i}^{i+k−2}x_j)
for i=1,…,n−k+1. Every x_k,…,x_n is determined, and setting t=X⊕q verifies w_i=t at every window. Conversely, any monochromatic starting vertex has its unique t and q=X⊕t and therefore appears exactly once in this construction. The choices are injective, since the first k−1 bits are freely specified and x_k determines q. Hence exactly 2^k starting vertices work. □

**Antipodal compatibility.** The coloring satisfies c(bar F,rev σ)=1⊕c(F,σ) exactly when f(rev σ)=f(σ)⊕(1+(n−k) mod2). Thus for k=3 this supplies a substantial NORI subclass, with reversal-even f in even n and reversal-odd f in odd n. The theorem also works without antipodal symmetry.

**Affine rank criterion (generalization).** Suppose more generally every ordered k-face color is affine over F_2 in the outside face bits. For a fixed coordinate order p the n−k+1 window colors form w(x)=A_p x⊕b_p. If the augmented matrix [A_p | 1] has full row rank n−k+1, a monochromatic window sequence exists: solve A_px⊕t1=b_p. The exterior-parity theorem above gives a constructive proof of this rank criterion for its special coefficient matrix, and proves the stronger exact count 2^k.

**Scope.** General Boolean dependence on outside face bits, and rank-deficient affine colorings, remain untreated. The grand NORI conjecture remains open.


## Universal flippers and affine change fibers

Say that a coordinate \(a\) is a *universal flipper* if toggling its exterior fixed bit complements every ordered-face color whenever \(a\) is outside the free triple. If \(V=A\sqcup B\) and every coordinate of \(A\) is such a flipper, the coloring has the factorization
\[
c(F,\pi)=\bigoplus_{a\in A\setminus\operatorname{free}(F)}x_a(F)
         \oplus g(\pi,x_{B\setminus\operatorname{free}(F)}).
\]
Put all \(A\)-directions first in the geodesic order, followed by an arbitrary \(B\)-order, and fix the \(B\)-starting bits. If \(A=(a_1,\ldots,a_r)\), shifting the three-window from position \(i\) to \(i+1\), for \(i\le r\), gives the change indicator
\[
d_i=G_i+G_{i+1}+1+z_i+\mathbf1_{i+3\le r}z_{i+3},
\]
where \(z_i\) is the initial \(a_i\)-bit and \(G_i\) is independent of every \(z_j\). Solve backward from \(i=r\) to \(1\). This triangular system makes the map from the \(r\) root bits to the first \(r\) change indicators a bijection. The remaining indicators are precisely those on the \(B\)-geodesic. Consequently, as \(A\)-bits range freely, the change-vector fiber is
\[
\{\,(u,\delta_B):u\in\mathbb F_2^r\,\}.
\]
If the residual \(B\)-geodesic has zero changes there are \(r+1\) full good lifts; if it has one there is exactly one; if it has at least two there are none. In particular, when \(|B|\le5\), the unrestricted five-dimensional theorem yields a full good lifted order. Under NORI oddness, removing an even number of flippers retains the antipodal-reversal axiom on the residual cube, furnishing a legitimate minimum-counterexample reduction.

For another affine approach, fix a full direction order \(p\) and let \(\Delta_p:\mathbb F_2^n\to\mathbb F_2^{n-3}\) be the vector of successive window-color changes as the root varies. If every window color is affine and the linear part of \(\Delta_p\) has rank at least \(n-4\), the affine image has codimension at most one. Any affine hyperplane \(\lambda\cdot z=b\) contains either \(0\) (when \(b=0\)) or a unit vector \(e_j\) with \(\lambda_j=1\) (when \(b=1\)). Thus the fixed order has a root with at most one change. A fixed bad order requires strictly lower rank.

## Two independently adjustable endpoint bits

For six distinct directions \(a,b,c,d,e,f\), hold all initial bits except \(u=x_d\), \(v=x_c\). The four-window word has the exact form
\[
(A(u),B,C,D(v)),
\]
because \(d\) is free in both interior windows and exterior to the first, while \(c\) is free in both interior windows and exterior to the last. If both endpoint functions toggle, independently select \(u,v\) to produce \((B,B,C,C)\), a good six-move block. In dimension six, sensitivity of the first \(abc\)-face to exterior bit \(d\) and sensitivity of the last \(def\)-face to exterior bit \(c\) can be realized simultaneously: their remaining exterior controls are disjoint. This proves the crossed-sensitivity closure criterion and yields complementary influence sparsity constraints under hypothetical failure. In larger cubes it produces a local block, with extension across other coordinates requiring additional control.

## Exterior-bit holonomy

Let \(S=\{a,b,c,d,e,f\}\subsetneq V\), and suppose \(g\in V\setminus S\). Consider attempting to reuse the six-geodesic forcing certificate of the dimension-six theorem inside an \(S\)-coordinate block of \(Q_V\), with the \(g\)-coordinate untraversed throughout the four consecutive length-three windows associated with each of the six orders. Each window in one such geodesic has the same fixed \(g\)-bit \(z_i\), determined by the starting vertex and by whether \(g\) occurs before or after the entire \(S\)-block.

**Lemma (exterior-bit parity obstruction).** There is no choice of bits \(z_1,z_2,z_4\in\mathbb F_2\) for the first, second, and fourth rows of the dimension-six forcing table that simultaneously preserves all three face identifications used in that proof:
(i) row 2's first \(dcb\)-window is the antipodal reversal of row 1's second \(bcd\)-window;
(ii) row 4's first \(dcb\)-window is likewise the antipodal reversal of row 1's second \(bcd\)-window;
(iii) row 4's last \(fea\)-window is the antipodal reversal of row 2's last \(aef\)-window.

**Proof.** To be antipodal reversals in the ambient cube, the fixed exterior \(g\)-bits of two compared faces must be complements. Relation (i) forces \(z_2=1\oplus z_1\), relation (ii) forces \(z_4=1\oplus z_1\), and relation (iii) forces \(z_4=1\oplus z_2=z_1\). Thus \(z_1=1\oplus z_1\), impossible. \(\square\)

**General parity principle.** Build a graph whose vertices are windows or blocks with a fixed value of a chosen outside coordinate \(g\); mark an identification edge 0 when the two windows are required to be the same ordered face, and mark it 1 when the two windows are required to be antipodal reversals. Existence of consistent \(g\)-bit assignments is equivalent to the parity label being a coboundary: every cycle must contain an even number of edges marked 1. The equivalence follows by propagating one chosen root bit along edges; consistency on cycles is necessary and sufficient. In the six-path forcing gadget, rows 1,2,4 form a triangle with three marked-1 edges, giving odd holonomy.

**Precise extension obligation.** A dimension-raising use of this six-path gadget must (a) traverse at least one additional coordinate between selected comparison windows in some path, so the exterior bit changes within that path, or (b) replace at least one of the three antipodal comparisons by another valid forcing relation. Simply appending or prepending all additional coordinates to contiguous six-coordinate blocks cannot preserve the proof's face identifications. This is a limitation of this particular forcing certificate; it does not assert any obstruction to the grand conjecture for \(n\ge7\).

The parity contradiction in the six-path extension is sharply local. It applies to a fixed contiguous block whose extra exterior coordinates remain untraversed. A dimension-independent proof must move such coordinates between the compared physical windows or replace some of the required antipodal face comparisons. The exact exterior-parity and universal-flipper theorems furnish broad all-dimensional positive subclasses; the holonomy obstruction diagnoses one failure of a naive induction rather than an obstruction to the NORI conjecture itself.\n\n## Affine syndromes and nonlinear exceptions\n\nFor a fixed order the change vector is affine in the root when each ordered face color is affine in exterior bits. A codimension-one image meets the radius-one Hamming ball, and the full exterior-parity recurrence gives eight monochromatic roots per order. The separate nonlinear-fault theorems allow a small exceptional coordinate set while preserving parity on all clean triples. Their scope is strictly conditional on that clean-triple hypothesis.
