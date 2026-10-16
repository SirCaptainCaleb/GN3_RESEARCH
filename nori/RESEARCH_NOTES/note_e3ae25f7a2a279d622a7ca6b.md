# Folded cubes have factorially many rainbow cycles: NORI1 is lift-color compatibility

- Stable ID: note_e3ae25f7a2a279d622a7ca6b
- Author: unspecified; session provenance retained
- Primary home: subsection:folded_cube_line_graphs_and_local_generation_of_binary_dependencies
- Labels: NORI1, folded-cube, rainbow-cycles, Alon-Pokrovskiy-Sudakov, monodromy, unrestricted
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10712_1
- Updated session: session_nori_r10712_1
- Disposition: none
- Successor: none

## Related references

- toolkit:literature_alon_pokrovskiy_sudakov_long_rainbow_cycles_2017

## Research note

Define the folded cube F_n=Q_n/<tau> where tau(x)=bar x and n>=3. Each quotient vertex is an antipodal orbit and each quotient edge has a direction label i in [n], giving a proper edge labeling of this n-regular graph on 2^(n-1) vertices.

THEOREM (rigid rainbow cycle length). Every direction-rainbow simple cycle of F_n uses all n direction labels, so has length n. Conversely, for each quotient root [x] and permutation pi of [n], traversing the labels pi generates a simple rainbow n-cycle: its lift starts at x, toggles every bit once, and ends at bar x; no proper intermediate portion can bring the lifted walk to either x or bar x because its used directions form a proper nonempty set. The number of undirected rainbow cycles of F_n is 2^(n-2)(n-1)!. Proof of count: there are 2^(n-1)n! rooted oriented cycles, one for each root orbit and ordered direction permutation; divide by n choices of cyclic root and by two orientations. Direct enumeration gives counts 4,24,192,1920 for n=3,4,5,6.

Let c be any antipodally odd binary coloring of Q_n. Every edge orbit of F_n has two lifted edges with opposite binary colors, so c cannot be assigned a well-defined binary edge color on the quotient. Call a rainbow cycle admissible in red if one of its two lifts is entirely red. Then NORI1 for c is equivalent to F_n having a red-admissible rainbow cycle. Because any rainbow quotient cycle has length n, the condition does not require a separate near-Hamilton or high-length rainbow conclusion.

More quantitatively define the lift frustration of a quotient rainbow cycle C to be the minimum number of blue edges in either one of its two lifts, and let f(c) be the minimum frustration over these cycles. Antipodal oddness makes the two lifted color words complementary, so 0<=f(c)<=n/2, and f(c)=0 iff NORI1 holds for c. The cycles are precisely projections of full antipodal geodesics, hence f(c) equals the previously defined minimum blue-edge defect r(c). Cartesian multiplication adds f, and a uniform f(c)=o(n) bound on balanced legal colorings along any unbounded even-dimensional sequence is therefore equivalent to unrestricted NORI1 by the existing product-amplification theorem.

APPLICATION TO ALON-POKROVSKIY-SUDAKOV. Their near-spanning rainbow cycle theorem concerns unlifted label distinctness in a complete graph. The folded cube already has factorially many full rainbow cycles without assumptions on c. What is missing is not label distinctness or a cycle but the common-sheet binary-color compatibility of its lift. Their rainbow path-forest exchange scheme would need to be strengthened to decrease signed-lift frustration, not merely to add previously unused edge labels. The edge-orbit red projection is all of F_n because precisely one of each orbit's lifted edges is red, but this does not make its red edges composable along a cycle: consecutive chosen red representatives can meet different sheets above the same quotient vertex.

RESERVE GRAPH DECOMPOSITION IN THE FOLDED CUBE. For a proper subset S of the n direction labels, let k=n-|S|>=1. The subgraph of F_n retaining precisely direction classes in S is the disjoint union of 2^(k-1) copies of Q_|S|. Indeed an antipodal orbit [x] has an invariant omitted-bit assignment x_D modulo complementation of every omitted bit; this gives 2^(k-1) components, and fixing one representative omitted assignment identifies a component with Q_S. Thus sampling o(n) direction classes as an APS-style sparse connecting reserve produces 2^(n-o(n)-1) separate components even after antipodal folding. If r=poly(n) endpoint orbit-vertices are independent uniform samples, the probability any two share a reserve component is at most binomial(r,2)*2^(-(k-1)), exponentially small when k=n-o(n). This quantifies why a random small-label reservoir cannot join globally distributed partial geodesics.

TWISTED ROOT-SLIDE HEIGHT. For any rooted lifted color word w=(w_1,...,w_n), shifting the starting orbit vertex once along its folded rainbow cycle replaces w with (w_2,...,w_n,1-w_1). Let b_j be the number of blue edges in the lift rooted after j steps, j=0,...,n. Then b_(j+1)-b_j=1-2w_(j+1), and b_n=n-b_0. Hence the range of the partial sums of the signed edge word measures how close some cyclic re-rooting gets to a monochromatic full geodesic. APS's edge-label-rainbow condition does not constrain this height. A NORI1-relevant rainbow-cycle theorem must drive some b_j to zero (or uniformly to o(n) defects), rather than merely ensuring color-label distinctness.
