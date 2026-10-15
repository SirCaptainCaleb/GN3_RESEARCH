# Complete cycle-extension criterion for colorings on projected geodesic subgraphs

# Relative cycle-extension theorem for projected geodesic colorings

This establishes the full system of **linear compatibility constraints** on any collection of observed cube edges when the square curvature of an unrestricted antipodally odd coloring is fixed. It shows precisely why a single complete dimension-simple geodesic has arbitrary color-word freedom, while overlapping complete paths have constraints from their shared projective incidence cycles.

Fix \(n\ge3\), and write \(Y=\partial[0,1]^n/\tau\cong\mathbb{RP}^{n-1}\), with quotient edge graph \(G=Y^{(1)}\). It has \(V=2^{n-1}\) vertices. Fix a realizable projective square-curvature cocycle \(\eta\) and a legal reference edge coloring \(c_*\) with that curvature. Every other legal coloring with the same curvature is
\[
c_*+\pi^*d,\qquad d\in Z^1(Y;\mathbb F_2).
\tag{1}
\]
The vector space \(Z^1(Y)\) has dimension \(V\): the quotient one-skeleton is connected, so \(\dim B^1(Y)=V-1\), while \(H^1(Y;\mathbb F_2)\cong\mathbb F_2\).

Let \(H\subseteq G\) be an arbitrary edge subgraph. Prescribe a modification \(v\in C^1(H;\mathbb F_2)\) of the coloring of its quotient edges, relative to \(c_*\). Write
\[
\phi_H:H_1(H;\mathbb F_2)\to H_1(Y;\mathbb F_2)\cong\mathbb F_2
\tag{2}
\]
for the inclusion-induced homomorphism. Put \(\epsilon_H=\operatorname{rank}\phi_H\in\{0,1\}\), \(v_H=|V(H)|\), and \(c_H=\text{number of connected components of }H\).

**Theorem 1 (relative cycle-extension criterion).** The prescribed modification \(v\) extends to a legal coloring of the entire cube with the same curvature \(\eta\) **if and only if**
\[
\boxed{\langle v,z\rangle=0
\quad\text{for every }z\in\ker\phi_H.}
\tag{3}
\]
Whenever an extension exists, the number of legal extensions is
\[
\boxed{2^{\,2^{n-1}-v_H+c_H-\epsilon_H}.}
\tag{4}
\]
In particular, no compatibility equations beyond the nullhomologous cycles of the selected edge subgraph are imposed by holding the entire square curvature fixed.

*Proof.* If \(v\) extends, then by (1) it is the restriction of a closed quotient cochain \(d\). A cocycle vanishes on every cycle representing zero homology in \(Y\), proving necessity.

Conversely, let \(u_1\in Z^1(Y)\) represent the nonzero class in \(H^1(Y)\). If \(\phi_H=0\), equation (3) says \(v\) vanishes on every cycle of \(H\), so it is a graph coboundary \(\delta h_H\). If \(\phi_H\ne0\), choose a cycle \(z_0\) with \(\phi_H(z_0)=1\), and put \(\lambda=\langle v,z_0\rangle\). Any cycle \(z\) with \(\phi_H(z)=0\) has evaluation zero by (3). If \(\phi_H(z)=1\), then \(z+z_0\in\ker\phi_H\), so \(\langle v,z\rangle=\lambda\). Thus in either case
\[
v+\lambda u_1|_H
\]
has zero evaluation on every graph cycle and equals \(\delta h_H\) for some vertex function \(h_H\) on \(H\). Extend \(h_H\) arbitrarily to all quotient vertices, define \(d=\delta h+\lambda u_1\), and use (1). This gives an extension.

For counting, restrictions of vertex gauges to \(H\) form its graph coboundary space of dimension \(v_H-c_H\). The class \(u_1\) adds one independent direction precisely if \(\phi_H\ne0\). Hence the image of the restriction map \(Z^1(Y)\to C^1(H)\) has dimension \(v_H-c_H+\epsilon_H\), and its kernel has dimension \(2^{n-1}-v_H+c_H-\epsilon_H\). Each attainable assignment has the number of preimages in (4). \(\square\)

**Corollary 2 (forest freedom).** If \(H\) contains no graph cycles, then every assignment \(v\) to its edges extends, at any fixed realizable curvature. More generally, a projectively nontrivial cycle contributes a freely selectable common phase, whereas a cycle representing zero projective homology imposes one linear compatibility relation (possibly dependent on other such relations).

**Corollary 3 (one complete geodesic).** The projection of a full antipodal dimension-simple geodesic is a simple \(n\)-cycle in \(G\) representing the nonzero class of \(H_1(Y)\). Thus \(v_H=n\), \(c_H=1\), \(\epsilon_H=1\), and the kernel of (2) is zero. All \(2^n\) possible complete edge-color words are feasible at fixed curvature, each in
\[
\boxed{2^{\,2^{n-1}-n}}
\tag{5}
\]
legal colorings, recovering the uniform one-path theorem of Subsection 31.

**Corollary 4 (arbitrary overlapping galleries).** Let \(H\) be the union of the projections of any family of complete dimension-simple antipodal geodesics, identifying their shared quotient edges. A simultaneous prescription of their edge colors is feasible at fixed projective curvature if and only if its differences from a reference coloring vanish on all cycles in \(H\) bounding two-chains in \(Y\). These are all the imposed linear conditions.

**Proof-search relevance.** This is an intrinsic classification of how the original unrestricted cube-edge coloring couples distinct complete geodesics. Square curvature places no restriction on a single chosen full color word, but it enforces compatibility across overlapping paths through their nullhomologous incidence cycles. The theorem therefore identifies a natural color-sensitive ingredient for the higher Coxeter homotopies of Subsections 34–35. It is not itself a proof of the existence of a monochromatic full geodesic; a successful Wu–Yang adaptation must use these path-to-path constraints to control the second-switch obstruction, rather than replacing the coloring by its curvature alone.
