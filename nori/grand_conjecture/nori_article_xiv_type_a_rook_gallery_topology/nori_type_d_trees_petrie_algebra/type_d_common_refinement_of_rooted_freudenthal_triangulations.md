# Type-D common refinement of rooted Freudenthal triangulations

# The type-D Coxeter complex simultaneously refines all rooted Freudenthal triangulations

Work in \(I^n=[0,1]^n\), \(n\ge3\), and write \(t_i=2z_i-1\). The Freudenthal triangulation \(T_x\) rooted at any corner \(x\in\{0,1\}^n\) sorts the \(n\) quantities
\[
d_i^x(z)=|z_i-x_i|=\frac{1+(-1)^{x_i}t_i}{2}.
\tag{1}
\]
Every maximal simplex records a permutation of these signed distances.

**Theorem 1 (simultaneous root refinement).** The union of separating hyperplanes of all rooted Freudenthal triangulations is
\[
\boxed{\mathcal A_D=
\bigcup_{i<j}\{t_i=t_j\}\cup\bigcup_{i<j}\{t_i=-t_j\},}
\tag{2}
\]
the type-\(D_n\) root arrangement. Its induced polyhedral decomposition of the cube, and of the cube boundary, is a common refinement of all \(2^n\) rooted Freudenthal triangulations. It is minimal among common refinements obtained by superimposing entire separating hyperplanes.

*Proof.* A wall of \(T_x\) has \(d_i^x=d_j^x\), equivalent by (1) to \((-1)^{x_i}t_i=(-1)^{x_j}t_j\). When \(x_i=x_j\) this gives \(t_i=t_j\), and otherwise \(t_i=-t_j\). Varying the roots realizes both signs for every pair. Each cell of (2) lies on fixed sides of every wall of every \(T_x\), so refines all such simplices. Every listed hyperplane occurs in one of those triangulations. \(\square\)

**Theorem 2 (first-edge chamber pairing).** The type-\(B_n\) arrangement is obtained from (2) by adding the sign hyperplanes \(t_i=0\). Each type-D chamber fuses two type-B chambers across the sign wall for the entry of smallest absolute value. In the standard type-B flag notation
\[
0<|t_{\pi_1}|<\cdots<|t_{\pi_n}|,\qquad
\operatorname{sgn}(t_i)=(-1)^{x_i},
\]
the fused flags are
\[
\boxed{(x,\pi)\quad\text{and}\quad(x\oplus e_{\pi_1},\pi).}
\tag{3}
\]
Their two complete cube geodesics traverse the same undirected edge in their first step.

*Proof.* A sign can change without crossing any hyperplane \(t_i=\pm t_j\) only if its absolute value is the smallest: if another entry had smaller absolute value, a sign change would cross an equality wall. Conversely changing the sign of a unique smallest entry preserves all inequalities \(t_i\pm t_j\), proving the fusion. The two root choices in (3) differ only at the dimension first traversed, so that first edge is shared as an undirected edge. \(\square\)

**Corollary 3 (fixed source complex for all prefix cones).** Every rooted monochromatic geodesic-prefix complex \(K_x^a\), its two-color union \(C_x\), and its switch-filtered extension \(K_x^{[r]}\), can be subdivided inside the same type-D polyhedral cube complex. Geometric intersections of these root-dependent complexes become ordinary intersections of subcomplexes in one common subdivision. Antipodal inversion preserves this common refinement. The underlying path witnesses and their distinct-dimension supports are unchanged.

*Proof.* Each prefix complex is a subcomplex of its rooted \(T_x\). Refining every \(T_x\) by (2) refines all prefix complexes and their intersections. Antipodality preserves the collection of hyperplanes in (2). Subdivision does not alter admissibility or path certificates. \(\square\)

**Research consequence.** The type-D complex provides a canonical, root-independent source for a Wu–Yang-style chain map while retaining the original full-rank rooted geodesic certificates as labels on the pieces. The two fused type-B flags in (3) need not have the same suffix color word, so they must not be identified in a color-sensitive target map. This theorem settles common-source compatibility, not the remaining higher-dimensional chain cancellation on mixed-color square carriers.
