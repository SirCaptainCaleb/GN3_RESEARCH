# Root-profile nerves and signed mixed-branch interfaces

# Root-profile nerves and signed mixed-branch interfaces

Label each cube root by its genuine monochromatic terminal-support possibilities, retaining the reversed terminal two-direction order used for NORI splicing. The profile nerve has opposite sign shores under antipodal reversal. Individual shores may be large simplices, but the mixed interface is controlled by the existence of paths long enough to support both complementary branches.

## Universal two-shore simplices in the exact signed-root reachability nerve and a canonical equivariant square

Let n>=5, d=n−2>=3, Ω={(J,U): J=(a,b) ordered distinct, ∅≠U⊊D_J=[n]\{a,b}}, with fixed-point-free involution τ(J,U)=(rev J,D_J\U). For each cube root x define the **actual color-free terminal memory profile**
L_x={(J,U) in Ω: U in R_J(x)},
where R_J(x) consists of supports witnessed by a MONOCHROMATIC directed physical ordered-three-face geodesic rooted at x and ending in ordered directions J. Let S_(x,+)=L_x and S_(x,−)=τ L_x. Define N as the nerve on signed roots (x,±) whose simplices are families of S_(x,±) with common label. This is the exact fixed-point carrier of item nori_reversed_tail_root_profile_nerve_tucker_label_reduction_20261008: an antipodal edge (x,+)(x,−) is equivalent to active NORI grand closure.

**Theorem 1 (unconditional two full shores).** All positive signed-root vertices together span a simplex Δ_+, and all negative signed-root vertices together span a simplex Δ_−, *independent of the coloring*. Indeed fix any ordered tail J and coordinate i∈D_J. The three-edge direction word (i,a,b) has exactly one ordered-three-face window, hence is automatically monochromatic, from EVERY starting cube root x. Therefore (J,{i}) belongs to L_x for ALL x. This one label witnesses the whole Δ_+. Its involution τ(J,{i}) witnesses the whole Δ_−.

**Theorem 2 (mixed edge and forced equivariant square).** A mixed edge (x,+)(y,−) exists iff some actual support U satisfies U∈R_J(x) and D_J\U∈R_revJ(y). If x=y this is grand closure. If x≠y, its τ partner (y,+)(x,−) also exists. Together with the universal shore edges (x,+)(y,+), (x,−)(y,−), these four vertices form a τ-invariant **induced four-cycle** in the no-closure hypothesis, namely
(x,+) -- (y,+) -- (x,−) -- (y,−) -- (x,+).
No other edges can occur inside this four-vertex set in a no-closure configuration, because the two missing diagonals are precisely the forbidden opposite-signed same-root pairs. Every triple of the four vertices contains one forbidden opposite pair, so no 2-simplex fills this square using only these four vertices. The induced cycle is an equivariant copy of the circle with antipodal involution. It follows that the free-Z2 cohomological index of N is >=1 whenever any cross-root mixed edge exists under no closure. This does **not** imply that the square is nonzero in the H_1 of all of N: other vertices and simplices could fill it.

**Theorem 3 (only genuinely long supports can couple the shores in a counterexample).** If the grand conjecture fails, no root has an admissible support U of size d−1 in ANY tail family: the complementary size-one label with reversed tail is automatically present at that same root and would give closure. Consequently every mixed signed-root nerve edge in a counterexample must be witnessed by a pair of support sizes s and d−s with BOTH s>=2 and d−s>=2. In particular, for d<=3 (n<=5) no mixed edge exists under the no-closure hypothesis, and the abstract hypothetical nerve is exactly Δ_+ disjoint union Δ_−. For n>=6 every mixed edge records genuinely longer path data not forced by one-window tautologies.

**Application and limit.** The signed root-profile nerve has a structural "two full shores plus constrained mixed faces" form. It is therefore especially amenable to Tucker/Bier-type equivariant arguments if one can control mixed high-dimensional simplices by genuine common witnessed labels. The unrestricted full shore simplices alone have equivariant index zero (their disjoint union is equivariantly S^0); a single cross-root mixed edge creates an invariant S^1 subcomplex, but no general high-index bound follows. Proving that a sufficiently high-index mixed-face configuration MUST appear (or an opposite edge occurs) remains the exact unsolved topological step.

## Color-preserving path carriers have trivial antipodal cover class

Inputs: nori_window_shift_monochromatic_edges_universal_cohomology_class_20261008 and literature_fixed_point_theorems. This gives a precise transport constraint for the new window parity class.

## 1. The monochromatic-shift subgraph splits the double cover
Let H be the graph of actual ordered three-face windows, with shifts realized by genuine four-edge geodesics. Let tau(F,pi)=(bar F,rev pi), and let c(tau v)=1-c(v). Let H_mono be the spanning subgraph retaining exactly edges uv with c(u)=c(v).

Then c:|H_mono| -> {0,1} is continuous and equivariant (tau exchanges 0 and 1). The two color subgraphs are exchanged by tau. The quotient double cover
 H_mono -> H_mono/tau
is TRIVIAL: each quotient vertex and edge has a unique color-zero lift, and this defines a global continuous section. Thus its cover class w_mono vanishes, and all its positive powers vanish.

This holds even when the monochromatic shift graph has odd cycles and nonzero ordinary first cohomology.

## 2. The connector parity class is distinct from antipodal index
In the full quotient B=H/tau, the established classes satisfy
 alpha=[hbar]=[1_B]+w,
where hbar records same-color edges. Restrict to B_mono=H_mono/tau. Then
 w|B_mono=0,
 alpha|B_mono=[1_(B_mono)].
Hence an odd monochromatic cycle may detect alpha while detecting zero antipodal cover class.

The conclusion follows directly from the section in part 1 and the fact that hbar is one on every retained edge. In particular, the coloring-independent nonzero connector class provides genuine parity information; transporting it into a high-index carrier additionally requires the carrier's color-forgetting identifications or suitable edges between different colors.

## 3. General colored-state carrier theorem
Let Z be a finite simplicial complex whose vertices represent monochromatic path states, each with an actual binary witness color q(v). Suppose q is constant on every simplex and tau acts simplicially with q(tau v)=1-q(v). Then q extends to a continuous equivariant map |Z| -> S^0. Its quotient double cover has a global color-zero section. Consequently every positive power of its cover class vanishes.

Proof. Every simplex lies in one color class; the two resulting subcomplexes are disjoint and exchanged. The constant affine extension of q is continuous, and the section follows as above.

For r such carriers, their equivariant join maps to
 (S^0)^(join r)=S^(r-1),
by joining their color maps. Their product with the diagonal involution maps to S^0 by projecting to the first factor and then using its color map. Thus joins or products of separate color-preserving connector carriers have the stated index upper bounds, regardless of other ordinary cohomology classes.

## 4. Consequence for NORI's exact color-free carriers
The mixed root-profile interface and the initial/terminal physical witness-cone complexes forget witness color. Their points may identify states backed by distinct colored paths. Such identifications remove the hypothesis of part 3 and can carry nontrivial antipodal topology.

A proposed high-index construction should specify these identifications and verify that a face still retains a valid root/terminal-memory extraction. Keeping every monochromatic witness in a permanently separate colored component gives the explicit S^0 map above. The exact reversed-tail splice theorem allows either branch color, so color-free profile intersections are the appropriate extraction target.

No assertion of nonzero higher cover powers for the actual color-free interface is made here. Establishing such powers, or acyclicity of the interface, remains a forcing task toward grand closure.


## Sparse monochromatic reachability without large-volume guarantees

**Theorem (exact reachability count for an antipodally odd edge-colored family).** Let \(n=2m\) and partition the \(n\) directions into \(m\) ordered pairs \((a_t,b_t)\). Give each undirected edge in direction \(a_t\) the color of its fixed \(b_t\)-bit, and each edge in direction \(b_t\) the color of its fixed \(a_t\)-bit:
\[
c(\{z,z\oplus e_{a_t}\})=z_{b_t},\qquad
c(\{z,z\oplus e_{b_t}\})=z_{a_t}.
\]
This is a well-defined antipodally odd two-edge-coloring of \(Q_{2m}\): the partner bit remains fixed across its associated edge and toggles under antipodal complementation.

For root \(x\), let \(A,B,H\) be the numbers of coordinate pairs with starting bits \(00,11,\) and mixed \(01/10\), respectively; \(A+B+H=m\). Let \(R_i(x)\) be the vertices reachable from \(x\) by an edge-color-\(i\) monochromatic *geodesic*, including the zero-length path. Let \(R(x)=R_0(x)\cup R_1(x)\). Then
\[
|R_0(x)|=3^{A+H},\quad
|R_1(x)|=3^{B+H},\quad
|R_0(x)\cap R_1(x)|=2^H,
\]
and therefore
\[
\boxed{|R(x)|=3^{A+H}+3^{B+H}-2^H.}
\]
The maximum over roots is
\[
\boxed{\max_x |R(x)|=2\cdot3^m-2^m,}
\]
and the average over all \(2^{2m}\) roots is \(2(5/2)^m-(3/2)^m\).

For every \(m\ge5\), **no** starting vertex has a monochromatic reachability set comprising more than half the cube:
\[
|R(x)|\le2\cdot3^m-2^m<2^{2m-1}.
\]
Nevertheless, the coloring admits a full **monochromatic antipodal geodesic**.

**Proof.** A geodesic changes each coordinate at most once. In a starting \(00\) pair, an edge-color-0 geodesic may traverse neither coordinate or exactly one of the pair (three choices) but cannot traverse both, since the second move would see partner bit 1; edge-color-1 traversal permits only the empty support. For a starting \(11\) pair the roles of the colors reverse. In a mixed pair \(01/10\), each color separately permits exactly three supports: the empty support, one of the two singleton supports, and the two-coordinate support. The two color-specific local support sets intersect precisely in the empty and full-pair supports (two choices).

Coloring interactions between distinct pairs are independent: colors within a pair depend only on that pair's coordinates, so every selection of independently realizable per-pair support witnesses can be concatenated to a globally monochromatic geodesic of the same selected color. Counting the possible global supports, which correspond bijectively to endpoints, gives the two powers of 3; the intersection has one support choice in each homogeneous pair and two in each mixed pair, giving \(2^H\). Inclusion-exclusion yields the formula.

Converting one homogeneous pair to a mixed pair strictly increases the union size: for \(00\to\text{mixed}\), \(3^{A+H}\) stays fixed, \(3^{B+H}\) is tripled and \(2^H\) doubled, so the net increment is \(2\cdot3^{B+H}-2^H>0\); the \(11\to\text{mixed}\) case is symmetric. Thus the maximum occurs when \(A=B=0,H=m\), giving \(2\cdot3^m-2^m\). For a uniformly random root, pairs are independently \(00,11,01,10\) with probability \(1/4\) each. Taking expectations of \(3^{A+H}\), \(3^{B+H}\), and \(2^H\) gives the stated average by multiplying the respective per-pair expectations \(5/2,5/2,3/2\).

For \(m=5\), \(2\cdot3^5-2^5=454<512=2^{9}\). The ratio \((2\cdot3^m-2^m)/2^{2m-1}=4(3/4)^m-2(1/2)^m\) decreases with \(m\ge5\), proving the strict half-volume inequality for all later \(m\).

For the full antipodal geodesic, take a root whose bits in every pair are mixed. For each pair choose the order of its two moves so that both edges have a preselected common color 0 (or analogously color 1); this is possible because one order traverses both directions in color 0 and the other in color 1. Concatenate the resulting monochromatic two-move paths across all pairs. Each direction is used exactly once, yielding a full monochromatic antipodal geodesic. \(\square\)

**Verified checks.** A direct monotone-subset dynamic program enumerated *all roots* in \(n=2,4,6,8\), with no discrepancies between computed monochromatic reachable-endpoint counts and the formula. The independent \(Q_4\) square-face obstruction example in Item \`nori_edge_reachability_nerve_square_face_nonfilling_and_support_symmetries_20261008\` uses the same family.

**Implication for topological NORI strategy.** A proposed proof based solely on universal largeness \(|R(x)|>2^{n-1}\) (and therefore pigeonhole overlap with its antipode) cannot work. The goal must use geometry, support structure, local face incidence, or equivariant topology of the *actual certified reachability family*, rather than a large-volume bound. This theorem is about the simpler edge-colored proving ground; it is NOT by itself a proof or disproof of ordered-three-face NORI.

### Elevation pass I: antipodal invariance at vanishing density

For a root \(x\) with **all \(m\) coordinate pairs mixed** (one 0 and one 1 in each pair), the same family satisfies the stronger identity
\[
\overline{R(x)}=R(x),
\]
even though
\[
\frac{|R(x)|}{|Q_{2m}|}=\frac{2\cdot3^m-2^m}{4^m}\longrightarrow0
\]
exponentially. Indeed, within a mixed pair the color-0 supports are exactly \(\varnothing,\{b\},\{a,b\}\) after a suitable naming of the directions, whereas the color-1 supports are \(\varnothing,\{a\},\{a,b\}\). Complementation of that two-element coordinate support interchanges these lists. Since distinct pairs contribute independent choices, global support complementation interchanges the full color-0 and color-1 reachable families. Thus every endpoint \(x\oplus S\) monochromatically reachable from this particular root has its physical antipode \(x\oplus(V\setminus S)\) monochromatically reachable as well. This demonstrates a much sharper limitation on purely volumetric fixed-point methods: **complete antipodal closure of a reachable set can coexist with arbitrarily small density**. Its arrangement and certified support involution, not its size, contain the relevant obstruction.


A topological coincidence in this nerve implies grand closure only when it realizes complementary supports with compatible endpoint memories at the same root. The interface, not the separate large shores, is the active topological target.
