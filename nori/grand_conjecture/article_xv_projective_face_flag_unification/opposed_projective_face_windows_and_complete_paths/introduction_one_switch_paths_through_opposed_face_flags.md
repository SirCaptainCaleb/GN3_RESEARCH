# Introduction: one-switch paths through opposed face flags

# Introduction: one-switch paths through opposed face flags

## The mathematical objective

Two unresolved problems motivate a common intrinsic path-selection problem. The proposed extension to all opposed projective-window systems is refuted below by centrally symmetric permutahedral counterexamples.

**NORI1.** Color every undirected edge of the \(d\)-cube \(Q_d\) by an arbitrary binary function \(c\) satisfying \(c(\bar e)=1-c(e)\), where the bar complements all vertex bits. Conjecturally a full antipodal geodesic, traversing each dimension once, is monochromatic. A path of length \(d\) with at most one color change already suffices: sliding its root past the unique switch uses the antipodal oddness to produce a monochromatic full geodesic. The root and dimension order must both remain unrestricted.

**Ordinary boundary 3-tournaments.** Let \(V\) have \(d+1\) vertices and let \(b(a,h,c)\in\mathbb F_2\) be specified independently for every ordered triple of distinct vertices, subject only to \(b(c,h,a)=1-b(a,h,c)\). Conjecturally there is a permutation \(v_0,\ldots,v_d\) of *all* the vertices whose consecutive triple word \(b(v_0,v_1,v_2),\ldots,b(v_{d-2},v_{d-1},v_d)\) has at most one switch.

Neither a short nonspanning path nor an arbitrary path in an auxiliary state graph is an adequate witness. An earlier Coxeter-coset reformulation in Article XIV recovers both problems but its conjecture explicitly chooses the type-A and type-B cases; it therefore does not identify the desired common structural hypotheses.

## Complete paths from faces

A simple \(d\)-dimensional convex polytope \(P\) has maximal proper face flags \(F_0\subset\cdots\subset F_{d-1}\subset P\), with \(\dim F_i=i\). Starting at \(v_0=F_0\), traverse at rank \(i\) the unique edge of \(F_i\) that leaves \(F_{i-1}\) at \(v_{i-1}\). This constructs a canonical path \(v_0,\ldots,v_d\). Its successive displacement vectors are linearly independent: the first \(i+1\) vertices affinely span \(F_i\). Conversely every such face-graded basis path reconstructs its maximal flag.

For a simplex, these are all Hamilton vertex orderings. For a cube, these are all freely rooted full antipodal geodesics. In every simple polytope, complete-path witnesses are therefore encoded by the maximal simplices of the barycentrically subdivided boundary sphere. This is the essential dimension-simplicity condition required in a chain-level proof.

## Intrinsic observations of one or two steps

For an edge \(E=uv\), define the first-order observation \(\Xi_1=(E,[v-u])\), where \([a]=\mathbb Ra\) is an unoriented vector line.

For a nonbacktracking two-edge walk \(u,v,w\), its edges lie in one two-dimensional face \(F(u,v,w)\) of a simple polytope. Define its second-order *projective face observation*
\[
\boxed{\Xi_2(u,v,w)=\bigl(F(u,v,w),[v-u],[w-v]\bigr).}
\]
Let \(\mathscr I_k(P)\) be the set of such observations, \(k=1,2\). A coloring \(c:\mathscr I_k(P)\to\mathbb F_2\) descends to the specified local incidence: observations representing the same face and ordered unoriented directions share one color. A maximal face flag \(\mathcal F\) yields an observation word \(\mathsf w_k(\mathcal F)\) of length \(d+1-k\).

For cubes at \(k=1\), this is the entire unrestricted undirected-edge coloring problem. For simplices at \(k=2\), an ordered triple \((a,h,c)\) is recovered from its supporting triangular face and its two ordered edge direction lines; reversing the triple exchanges the lines. This retains every ordinary reversal-odd tournament coloring, not merely cyclically symmetric or globally representable subclasses.

## Opposition and the proposed common conjecture

Call \((P,k,J,\rho)\) an *opposed projective-window system* when \(P\) is a simple \(d\)-polytope, \(k\in\{1,2\}\), \(J\) is a free simplicial involution of the proper-face flag sphere, and \(\rho\) is a fixed-point-free involution of \(\mathscr I_k(P)\) such that the observation word on \(J\mathcal F\) is obtained from that on \(\mathcal F\) by applying \(\rho\) to every incidence, with either the original order of positions or its reversal. In particular, a \(\rho\)-odd coloring, \(c(\rho I)=1-c(I)\), has a complementary word on opposite flags, possibly reversed.

**Original opposed-window one-switch assertion (refuted).** Every such system with \(d\ge k\), and every \(\rho\)-odd coloring of its projective local incidences, admits a maximal face flag \(\mathcal F\) satisfying
\[
\boxed{\operatorname{sw}\bigl(\mathsf w_k(\mathcal F)\bigr)\le1.}
\]

For cube one-edge data, choose geometric central inversion for \(J\) and for \(\rho\) on edges. For simplex two-edge data, choose complement of proper nonempty vertex subsets for \(J\) and turn reversal for \(\rho\). These specializations recover both targets without mentioning either reflection family in the hypotheses. The enlarged assertion fails on other opposed systems.

**Status and proof obligations.** The face-flag path theorem, projective-incidence encoding, rank-flip rotation, and these two specializations are proved and developed in subsequent subsections. The universal one-switch assertion is false. The subsection “Centrally symmetric permutahedral counterexamples to the opposed-window conjecture” proves that for every \(d\ge5\) with \(d\equiv1,2\pmod4\), an opposed system satisfying all the stated hypotheses has \(d-2\) switches on every complete path. Its coloring descends to projective two-face observations. The original NORI1 and boundary-tournament targets remain open; a revised common statement requires further intrinsic hypotheses. Mere antipodality, a spherical flag carrier, and path-basis completeness are individually insufficient. In particular, changing colors on different paths representing the same projective two-face observation admits alternating-parity obstructions, so local incidence descent cannot be omitted.

The remaining proof search seeks an adaptation of the Wu–Yang chain-level Borsuk–Ulam obstruction from general monochromatic antipodal paths to complete face-flag paths. The obstacle is constructing equivariant color-sensitive fillings over rank exchanges while retaining both full-path decoding and the local observation identifications. This article tests that obstruction directly.
