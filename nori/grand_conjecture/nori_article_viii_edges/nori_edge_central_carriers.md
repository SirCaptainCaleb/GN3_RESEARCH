# Central edge carriers and antipodal topology

## Exact seven-direction universality via multifacet bridging

For every integer k>=2 and every larger dimension n>k, the following are equivalent: (B_k) every arbitrary physical edge 2-coloring of Q_k has a full antipodal geodesic with at most one color change; and (P_n,k) every legal antipodally odd physical-edge coloring of Q_n realizes each prescribed assignment on any fixed k selected directions along a full n-direction antipodal geodesic. The new Subsection "Antipodal multifacet bridge and seven-coordinate universality" proves both implications by an exact physical multifacet bridge and a reversed doubling.

Leader--Long proved that geodesic odd closure A_(k+1) implies B_k. Kirchweger, Peitl, Subercaseaux and Szeider (2025, arXiv:2511.08386, Theorem 1) verified the geodesic statement A_8 by SAT; smaller dimensions were known. Hence any seven prescribed direction colors are simultaneously realizable for all n>7, with no restriction on nonlinear exterior dependence. For n<=8 every full target vector is attainable by known finite-dimensional odd-geodesic closure and directionwise reweighting. Eight prescribed coordinates in dimension at least nine remain open, equivalent under the bridge to B_8. This exact reduction is restricted to physical edges: ordered three-face paths have two uncontrolled splice windows.

## Universal three-coordinate prescription (unrestricted NORI1)

**New theorem.** In *every* antipodally odd binary coloring of genuine undirected cube edges, for any three distinct directions \(i,j,k\) and any three desired color bits, a full antipodal geodesic realizes all three prescribed edge colors simultaneously. Thus the direction-indexed full-geodesic color-profile set projects onto \(\mathbb F_2^3\) on every three-coordinate set, including for arbitrary nonlinear, exterior-dependent edge colors.

The proof, given in the Subsection *Universal three-direction edge-color prescription*, assumes an absent triple, applies a directionwise color normalization and global antipodal complementation to forbid \(000,111\), then cyclically root-rotates a genuine full geodesic starting \((i,j,k)\). The four profiles trace a full three-cube geodesic avoiding both antipodal corners, which forces the selected first three edge colors to alternate. Swapping the first two directions from the same root preserves the third *physical* edge, forcing the first two direction-edge colors to agree at every root. Undirected physicality then contradicts their required alternation. This gives an all-dimensional result stronger than the earlier two-coordinate corollary of the full-affine-span theorem: any missing complete target requires a genuinely at-least-four-direction compatibility failure. Monochromatic full-geodesic closure remains open.

## Unrestricted edge-color profiles: a full-affine-span theorem

**Theorem (all legal NORI1, with no affine hypothesis).** For any physical antipodally odd coloring of the cube's undirected edges, the set of color vectors indexed by *original direction* and realized along all full antipodal geodesics has affine span all of \(\mathbb F_2^n\). Consequently every prescribed pair of colors on any two selected coordinate directions occurs along a genuine full geodesic. This is a new universal theorem for the **entire** still-open NORI1 class.

The proof considers a hypothetical constant parity functional on the realized vectors. Swapping the first two steps of a full geodesic forces the corresponding weighted physical-edge cochain to have zero mod-two curvature on every cube square. The cochain must then be a gradient \(\delta\phi\); its full-path parity telescopes to \(\phi(x)\oplus\phi(\bar x)\). Antipodal edge oddness gives coordinate derivative \(y_i\) of this endpoint potential, contradicting its constancy for nonzero functional \(y\). Antipodal root complementation closes realized pair-profiles under simultaneous bit complement; their full affine span then forces all four possible pairs.

This identifies a stronger unrestricted edge-geodesic invariant than local curvature counts: **every linear parity obstruction to full color-profile variation vanishes.** The essential open step is simultaneous attainment of one prescribed vector, especially a constant vector; affine span and pair prescription alone do not establish full monochromatic closure. Full statement, local swap/root-flip dichotomy, exact physical-edge proof, and scope are in *Full-geodesic color profiles span the entire binary space* (Subsection 2).

# Middle-rank Johnson carriers and tight-path obstructions

The antipodally odd physical edge problem admits a central-rank formulation in even dimension n=2k. A monotone antipodal geodesic corresponds to a permutation of all n coordinates; its intermediate cube vertices correspond to the nested sets of directions already used.

## The middle carrier

At rank k, these vertices are k-subsets. Exchanges of one direction produce Johnson adjacency, and a chain of consecutive k-subsets with overlap k−1 is a tight path. For the central-vertex-gated coloring models, the proved exact transfer identifies monochromatic middle-belt cube geodesics with tight k-uniform hypergraph paths through 2k−1 distinct coordinate directions. The requirement of distinct directions guarantees geodesicity in the cube. The complement-odd tight-path completion theorem shows that a qualifying path through 2k−2 distinct directions can be extended using one of the two remaining coordinates.

This is an exact reduction for the specified central carrier. It is not an unrestricted equivalent of the original edge conjecture: legal antipodally odd edge colorings can obstruct all monochromatic paths confined to particular central belts, while still leaving other root choices available.

## Curvature and flat central realizations

Define curvature of each physical square as the parity of its four edge colors. In odd dimension the antipodal parity law forces at least 2^(n−2) odd-curvature squares, and a matching class of constructions attains the bound. In even dimension, arbitrary complement-odd middle-layer hypergraph labeling can be realized by a globally flat odd edge coloring. Hence square curvature and middle-layer labeling retain distinct degrees of freedom.

The Johnson picture offers an exact combinatorial carrier with verifiable caps; the curvature results constrain possible global lifts and show why a single middle slice is insufficient. The remaining forcing task is to select a globally compatible rooted path while retaining its actual physical edge colors.
