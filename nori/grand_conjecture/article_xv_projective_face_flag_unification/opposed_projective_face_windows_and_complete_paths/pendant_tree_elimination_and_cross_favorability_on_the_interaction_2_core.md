# Pendant-tree elimination and cross-favorability on the interaction 2-core

### Eliminating all pendant trees while preserving paired-root certificates

Let \(f\) be an arbitrary binary coloring of the undirected edges of \(Q_d\), and let \(G(f)\) be its undirected direction-interaction graph. Let \(H\) be the **2-core** of \(G(f)\), obtained by iteratively deleting vertices of degree at most one. Every component of the deleted subgraph belonging to a connected component with nonempty 2-core is a tree joined to the core by a single edge. Thus the noncore directions form independent rooted pendant trees attached at core directions.

For each core direction \(v\in V(H)\), its edge-color function \(f_v\) depends on its neighboring core bits and on the bits of the immediately attached noncore children. Define two induced core colorings \(g^0,g^1\) by
\[
\boxed{
g^s_v(z)=f_v\bigl((z_w)_{w\in N_H(v)},\,
                  (s)_{w\in N_G(v)\setminus V(H)}\bigr),
\quad s\in\{0,1\}.
}
\tag{1}
\]
The bit of the traversed direction \(v\) is omitted, as it must be for an undirected cube-edge coloring. The two induced colorings are unrelated in general.

**Theorem 1 (nonlinear pendant-tree elimination).** Suppose \(G(f)\) is connected and its 2-core \(H\) is nonempty. Then
\[
\boxed{|P(f)|\ge |A_0(g^0)\cap A_1(g^1)|.}
\tag{2}
\]
Every root of the intersection on the right can be lifted constructively to a paired root of the full coloring, using the universal opposite-bit subtree-interface lemma of the preceding nonlinear-tree Subsection. If \(H\) is empty, \(G(f)\) is a tree and the unconditional tree theorem already gives at least two paired roots.

*Proof.* Choose a core root \(z\in A_0(g^0)\cap A_1(g^1)\). Let \(P_0,P_1\) be full dimension-simple core geodesics starting at \(z\), with color words \(0^*1^*\) in \(g^0\) and \(1^*0^*\) in \(g^1\). Their core direction orders may differ. For every core vertex \(v\), denote its prescribed traversal colors in the two paths by \(U_v,V_v\), and its common starting bit by \(z_v\).

Apply the universal opposite-bit subtree-interface lemma independently to each pendant branch rooted at a noncore neighbor \(w\) of \(v\). Give the branch parent starting bit \(z_v\), parent colors \((U_v,V_v)\), and prescribe that the parent sees bit \(w\) equal to zero in the first path and one in the second. The lemma supplies common initial bits for the entire branch and two sets of edge orientations, compatible with the required nondecreasing and nonincreasing color comparisons across every branch edge. Different branches have disjoint direction sets and may be constructed independently.

To form each full direction order, retain the selected order of all core directions as a directed chain, and adjoin the oriented edges of all pendant trees. This union is acyclic: each attached tree meets the core chain at one vertex. Moreover all its earlier-to-later edge comparisons respect the required monotone colors, because the core chain was already color sorted and every attached edge is by the interface lemma. Hence one can choose a topological order listing all color-zero directions before color-one directions in the first mode, and the reverse in the second. These topological orders retain the original relative core orders, so each core direction reads its core-neighbor bits as in \(P_0,P_1\). Each attached neighbor bit observed at a core traversal has the prescribed value zero or one, so its core edge color is \(g^0_v\) or \(g^1_v\), as required. The pendant direction colors agree with their inductively constructed interfaces. The two resulting full paths begin at the same root assignment, use each dimension once, and have opposite monotone words. Distinct core roots give distinct full roots. QED.

**Corollary 2 (nonlinear unicyclic triangles in all dimensions).** If a connected interaction graph has a triangle as its 2-core, with arbitrary attached trees, then
\[
\boxed{|P(f)|\ge4.}
\tag{3}
\]
Indeed every arbitrary three-dimensional edge coloring has at least six nondecreasing and six nonincreasing favorable roots, so any two such colorings have at least four roots in their cross-orientation intersection. No restriction is imposed on the nonlinear local functions along the triangle or trees. In particular a minimum counterexample cannot have a triangular unicyclic interaction graph.

**Corollary 3 (2-core order at most four).** If a connected interaction graph has nonempty 2-core on at most three dimensions, it has paired roots by Corollary 2 and the \(\kappa_m\) bounds. With the separately recorded computer-assisted four-cube minimum favorable-root count \(m_4=9\), the same conclusion holds for any 2-core on four dimensions, with at least two paired roots. The order-four part depends on the finite optimization certificate; the order-three result is analytic.

**Corollary 4 (large cores with cross-favorable induced colorings).** Let the 2-core have \(m\) dimensions. If both \(g^0,g^1\) have star interaction graphs (their hubs may differ), then
\[
\boxed{|P(f)|\ge 2^{m-1}.}
\tag{4}
\]
If \(m=2r\) and both induced core colorings factor into arbitrarily colored squares along possibly different perfect matchings \(M,N\), then
\[
\boxed{|P(f)|\ge2^{c(M,N)}\ge2.}
\tag{5}
\]
These follow by applying the existing all-dimensional cross-star and crossed-matching intersection theorems to (2). Thus arbitrarily large feedback cores can be favorable despite nonlinear attached trees and changing square decompositions.

**Corollary 5 (forest and multiple-component extension).** If the whole interaction graph has connected components \(G_1,\ldots,G_s\), apply the unconditional tree theorem to each acyclic component and Theorem 1 to each cyclic component, then multiply paired-root counts using Cartesian factorization. In particular, for an interaction forest with \(s\) components the lower bound is \(2^s\), with no target-admissibility assumption.

**Corollary 6 (NORI1 with eliminable interaction cores).** Every antipodally odd coloring of \(Q_{d+1}\) whose lower facet satisfies a positive cross-intersection hypothesis from Theorem 1 or its corollaries admits monochromatic full antipodal geodesics, for arbitrary odd vertical bridge colors. The number of directed geodesics distinguished by their vertical crossing edge is at least the paired-root lower bound in the corresponding corollary, by the universal free-bridge equivalence.

**Independent reconstruction check.** A separate implementation generated arbitrary nonlinear color functions on interaction graphs whose 2-core was a triangle with randomly attached trees, in dimensions \(4,6,9,12,15\). For 80 independent cases per dimension it selected cross-favorable core paths, reconstructed both full paths using the subtree-interface recursion, and evaluated every original cube-edge color along the two geodesics. All 400 tests produced a common root and monotone full words.

**Closure perspective.** The earlier monochromatic-tree argument failed because of opposing constant-colored directions. The opposite-bit interface succeeds despite them. Therefore every pendant tree may be pruned without losing the paired-root objective, at the cost of replacing its core by two induced colorings \(g^0,g^1\). The remaining unrestricted obstruction lives in the 2-core cross-favorability problem. On a unicyclic graph this becomes a problem about two independent colorings of the cycle, a significantly smaller and geometrically constrained target than arbitrary colorings of the full high-dimensional cube.### Exhaustive cross-favorability for four- and five-cycle cores

Consider arbitrary binary edge colorings on \(Q_m\) with cyclic-neighbor dependence,
\[
f_i(x)=F_i(x_{i-1},x_{i+1}),\qquad F_i:\{0,1\}^2\to\{0,1\},
\]
with cyclic indices. Each of the \(m\) local truth tables has four free bits, so there are \(2^{4m}\) such colorings, including cases with inactive interaction edges. Write \(A_0(f)\) for roots admitting a full nondecreasing geodesic and \(A_1(f)=\overline{A_0(f)}\).

**Theorem 1 (finite computer-assisted census).** Exhaustive enumeration yields
\[
\begin{array}{c|r|r|r|r}
m&\text{colorings}&\text{distinct }A_0\text{ masks}&
\min_f|A_0(f)|&\min_{f,g}|A_0(f)\cap A_1(g)|\\
4&65,536&193&9&2\\
5&1,048,576&2,723&18&6.
\end{array}
\tag{1}
\]
In particular two arbitrary cyclic-neighbor colorings of either \(Q_4\) or \(Q_5\) have common roots for opposite monotone path orientations.

*Reproducible enumeration.* Encode the four truth-table bits \(F_i(0,0),F_i(0,1),F_i(1,0),F_i(1,1)\) in positions \(4i,\ldots,4i+3\), with direction zero least significant. For every integer code \(c\) from zero to \(2^{4m}-1\), run through all roots \(r\in\{0,1\}^m\) and all \(m!\) permutations of the directions. At each step \(i\), read \(F_i\) on the two neighbor bits at the current cube vertex, then toggle bit \(i\). Mark root \(r\) favorable if at least one such word is nondecreasing, thereby producing a \(2^m\)-bit root mask \(M_c\). Deduplicate all masks. The nonincreasing root mask of any coloring is its antipodal translate, obtained by replacing root index \(r\) with \(r\oplus(2^m-1)\). Minimize the population count of the bitwise intersection of \(M_c\) with that antipodal translate over all pairs of *distinct masks*, also including equality pairs. This deterministic finite algorithm gives the entries in (1); a separate direct evaluator independently checked the equality witnesses.

For \(m=5\), equality for the last column is attained at the two truth-table codes
\[
c=0{\rm x}53ad3,\qquad c'=0{\rm x}c5a35,
\]
whose nondecreasing root masks are respectively \(0{\rm x}f0ffa0aa\) and \(0{\rm x}eeee00ee\), each with 18 favorable roots. The cross-orientation intersection is the six roots \(1,5,13,28,29,30\). For \(m=4\), the two root masks \(0{\rm x}eee0\), \(0{\rm x}fca8\) give cross-orientation intersection \(\{5,10\}\).

**Corollary 2 (unicyclic closure up to pentagonal cores).** Let the undirected interaction graph of an arbitrary binary edge coloring be connected and unicyclic, with its unique cycle of length \(m\in\{3,4,5\}\). Arbitrary nonlinear trees may be attached to the cycle. Then the coloring has paired roots. Lower bounds on their number are 4, 2, and 6 for \(m=3,4,5\), respectively.

*Proof.* The preceding pendant-tree elimination theorem lifts each root in \(A_0(g^0)\cap A_1(g^1)\) to a paired root of the full coloring. The induced core colorings \(g^0,g^1\) have cyclic-neighbor dependence, so apply Theorem 1 when \(m=4,5\); for \(m=3\), use the analytic three-dimensional cross-root bound of four. QED.

The universal free-bridge theorem consequently establishes NORI1 for any antipodally odd coloring whose chosen lower facet has one of these interaction graphs; the number of distinct directed monochromatic geodesics is at least the same paired-root bound.

**Closure boundary.** At order six, the product of three colored squares has just \(27\) favorable roots among \(64\), so a purely cardinality-based cross-intersection proof no longer applies. The crossed-square theorem still gives two common roots for two shifted matching products. Arbitrary cycle-local colorings in dimension six and higher remain unresolved; an additional compatibility mechanism is required.### Square templates, alternating constraint paths, and a potential cycle closure

For a matching \(M\) of the cube direction set, covering all but at most one direction, choose a forbidden bit pair \(q_{ij}\in\{0,1\}^2\) for every edge \(ij\in M\). The corresponding **square template** is
\[
T(M,q)=\{x:(x_i,x_j)\ne q_{ij}\text{ for every }ij\in M\}.
\tag{5}
\]
It contains \(3^{\lfloor d/2\rfloor}2^{d\bmod2}\) roots. Taking antipodes of every root produces another template with the same matching.

**Lemma 3 (sharp path constraint bound).** If a path on \(p\ge1\) Boolean variables has one constraint on each neighboring pair, forbidding at most one of the four possible pairs, then it has at least \(p+1\) satisfying assignments.

*Proof.* For one vertex there are two choices. When a new endpoint is appended, each old satisfying assignment extends at least once. At least one old assignment ends with the bit that permits *both* values of the new endpoint: construct it backward greedily from that desired terminal bit, avoiding the sole forbidden pair at each earlier edge. Thus every extension adds at least one to the solution count. Induction gives \(p+1\). Equality is attained by forbidding \(10\) at every step, leaving just the \(p+1\) nondecreasing words. QED.

**Theorem 4 (matching-template intersection).** Given two matchings \(M,N\), each leaving at most one unmatched direction, the union multigraph consists of alternating paths and even cycles, with parallel-edge cycles allowed. If its path components have \(p_1,\ldots,p_s\) vertices and there are \(c\) cycle components, then for arbitrary forbidden bit pairs,
\[
\boxed{|T(M,q)\cap T(N,q')|
\ge2^c\prod_{\nu=1}^s(p_\nu+1)>0.}
\tag{6}
\]
The path estimate is Lemma 3; every binary constraint cycle has at least two solutions by the crossed-square Subsection. Independence of the components gives their product. QED.

**Corollary 5 (sharp odd-cycle bound).** On the odd cycle \(C_d\), \(d=2r+1\), restrict \(M,N\) to adjacent almost-perfect matchings, each missing one vertex. Then
\[
\boxed{|T(M,q)\cap T(N,q')|\ge d+1.}
\tag{7}
\]
The bound is sharp. For an even cycle, adjacent perfect matching templates always intersect in at least two roots, and this is sharp.

*Proof.* The union of the odd-cycle matchings contains one alternating path with odd vertex count \(p\) and \(k=(d-p)/2\) parallel-edge cycles. Formula (6) gives \((p+1)2^k\ge d+1\), since \(2^k\ge k+1\) and \(p\ge1\). Choose matchings with a spanning alternating path and forbid \(10\) along that path to attain \(d+1\) solutions. For an even cycle choose the two distinct adjacent perfect matchings; their union is one even cycle. Forbid \(00\) on one matching and \(11\) on the other to leave precisely the two alternating bit strings. QED.

**Corollary 6 (root-template sufficient criterion).** If the nondecreasing favorable-root sets \(A_0(f),A_0(g)\) of two arbitrary cube colorings each contain a square template, then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{8}
\]
Indeed \(A_1(g)=\overline{A_0(g)}\) contains the antipodal translate of its template, and Theorem 4 supplies a common root.

The open statement that would complete the **unicyclic interaction-graph case** is:

**Square-template containment conjecture (open).** For every chordless cycle \(C_d\), \(d\ge4\), and arbitrary binary local edge-color functions \(f_i(x)=F_i(x_{i-1},x_{i+1})\), the set \(A_0(f)\) contains a template from *some* matching of the \(d\) directions. The matching may include nonadjacent pairs.

If proved, Corollary 6 would show cross-favorability for every pair of cyclic-neighbor colorings, and pendant-tree elimination would resolve every unicyclic interaction graph with arbitrary nonlinear attachments. For odd cycle order an even stronger version may hold with an adjacent almost-perfect matching. The complete \(C_4,C_5\) enumerations verify containment in these dimensions, and the odd-cycle matching bound explains their cross-intersection minima 2 and 6. Additional sampling found suitable matchings in 100,000 \(C_6\) cases, 25,000 \(C_7\) cases, 10,000 perturbed \(C_8\) cases and 1,000 perturbed \(C_9\) cases. This is evidence, not a general proof.

**Nonadjacent pairs cannot be excluded.** A coloring with all six cyclic-neighbor interactions active, encoded by its six four-bit local truth tables as hexadecimal \(0{\rm x}ca83ad\), has favorable-root mask \(0{\rm x}cfcfcfcfcfcf\). It contains no template built from either neighboring-direction perfect matching of the six-cycle. It does contain a template for the nonlocal matching \(\{(0,3),(1,2),(4,5)\}\), with forbidden two-bit values \((0,1,3)\). Independent direct path enumeration verified this mask.

**The conjecture must remain restricted to chordless cycles of order at least four.** In the odd three-cycle parity coloring \(f_i(x)=x_{i-1}+x_{i+1}\) the unfavorable roots are \(000,111\). Multiply by a one-dimensional factor of constant edge color. Its unfavorable set in four dimensions becomes \(\{000,111\}\times\{0,1\}\). No two forbidden square faces on disjoint matched direction pairs can cover these four roots: a face fixing the fourth bit covers at most one, and a face fixing two of the first three bits covers at most two. Thus the favorable set has 12 roots but contains no square template. This interaction graph is a triangle plus an isolated direction and has maximum degree two, showing that the proposed containment is not an unrestricted low-degree theorem.

The remaining problem is the template-containment conjecture, not compatibility of templates. Its proof would turn the cycle's nonlinear path constraints into a system of forbidden binary pairs whose union graph has maximum degree two.

## Unicyclic NORI1 closure from local opposite-fiber overlap

Let F be a binary cube-edge coloring whose undirected direction-interaction graph is connected and unicyclic. The cycle H consists of m directions, and the other directions form rooted pendant trees. Define induced core colorings g0,g1 by assigning every pendant-child bit zero or one respectively when evaluating a core-direction color. Assume that for every cycle direction i some pair of its two cyclic neighbor bits yields g0_i=0 and g1_i=1. Thus each local simultaneous-success set D_i is nonempty.

**Theorem.** Under this condition, F has an antipodally paired root. By the established free-bridge correspondence, the one-higher-dimensional antipodally odd NORI1 instance has a monochromatic full antipodal geodesic.

*Proof.* The all-dimensional cyclic cross-fiber theorem in the nonlinear tree-incidence subsection supplies z in A0(g0) intersect A1(g1), possibly using two different cycle direction orders. The previously proved pendant-tree interface theorem lifts those two monotone core paths to two full monotone geodesics from one cube root, establishing P(F) nonempty. Apply the free-bridge equivalence. The attached trees and their nonlinear color functions have unrestricted depth and size, subject only to the interaction graph and local crossing condition. This is a new all-dimensional sufficient closure class, not the unrestricted unicyclic assertion.### Adaptive polarization closes responsive unicyclic interactions

Let a connected direction-interaction graph have unique cycle C_n, n>=3, with arbitrary pendant trees. At a cycle direction i, denote by L_i its immediate attached children and write its arbitrary local edge-color function as F_i(a,b;y), where a,b are the neighboring cycle bits and y is the L_i-bit vector.

Call i **antipodally responsive** if there exists y_i such that F_i(.;y_i) and F_i(.;complement(y_i)) differ at some cycle-neighbor input (a,b).

**Theorem.** If every cycle direction is antipodally responsive through its pendant children, then the full cube-edge coloring has a paired root, without any restrictions on the nonlinear color functions elsewhere in the pendant trees.

*Proof.* Choose for every cycle site i one y_i for which the two opposite attachment slices differ. If at some input their values are (0,1), retain y_i for the nondecreasing witness and its complement for the nonincreasing witness. If their values are (1,0), swap those choices. Distinct cycle sites have disjoint pendant branches, so all polarities can be chosen independently. This gives two induced cyclic-neighbor colorings g0,g1 on the same C_n satisfying, at every site i, at least one input with g0_i=0 and g1_i=1.

Apply the previously established all-dimensional cyclic nonempty-overlap theorem in the nonlinear-tree incidence Subsection: any pair of cyclic-neighbor colorings satisfying this local overlap has a common root supporting a nondecreasing full g0-geodesic and a nonincreasing full g1-geodesic, possibly with distinct dimension orders. Record the resulting core traversal colors U_i,V_i.

At each pendant child w of site i prescribe its observed bit at traversal of i to equal y_i(w) in the first path and its complement in the second. The unconditional opposite-bit subtree interface theorem supplies common starting bits and two oriented traversal trees compatible with parent colors U_i,V_i. Attach these separately to the two core orders. Since every pendant tree meets the core at one site, the joined precedence graphs remain acyclic, and sorting their two color phases gives two full dimension-simple geodesics from the same root with words 0*1* and 1*0*. The resulting root is paired. QED.

**Corollary (responsive sun graphs).** If every cycle direction i has a single pendant leaf w_i and its edge-color function depends nontrivially on bit w_i at some cycle-neighbor input, then the theorem applies. Arbitrary further trees may be attached below these leaves. The free-bridge equivalence therefore proves NORI1 for antipodally odd extensions of all these facets, with unrestricted odd bridge colors.

**Induction lesson.** The appropriate interface carried by the pendant-tree proof is an adaptively selected opposite-bit polarization, rather than a fixed square template. The remaining cycle sites for this method are those whose attachment-complement slices coincide for every attached-bit assignment; they require the terminal-defect or checkerboard analysis.

## Full unicyclic closure with a jointly constant core direction

Consider an arbitrary binary cube-edge coloring F whose undirected direction-interaction graph has a unique cycle H and arbitrary rooted pendant trees. Define the two induced cycle colorings g0,g1 by assigning all attached child bits zero or one in the manner of the established pendant-tree interface theorem. Suppose some cycle direction j has a constant color in g0 AND a constant color in g1, with the two constants allowed to differ. Then the original coloring F has an antipodally paired root. Indeed, fixing bit j leaves a pair of path-local colorings; by the new 66-core finite induction theorem in the subsection universal_path_local_cross_favorability_66_core_finite_induction, any such pair has a common root for an f-nondecreasing and a g-nonincreasing full path. Insert direction j first or last in either path according to the two constant colors, using the appropriate fixed-bit fibers. This gives A0(g0) intersection A1(g1) nonempty. The published nonlinear pendant-tree interface theorem lifts the two monotone core paths to full monotone paths with one common original root. Under the free-bridge equivalence, the associated antipodally odd one-higher-dimensional NORI1 instance has a monochromatic full geodesic.

All four pairs of constant core colors are covered: (0,1) prepend j to both paths; (1,0) append j to both; (0,0) prepend to the nondecreasing path and append to the nonincreasing path; (1,1) do the reverse. No opposite-color local-overlap assumption is required, and all attached tree color functions may be nonlinear. The path theorem is computer-assisted through an independently checked 66-mask inductive invariant. This result is an all-dimensional sufficient closure class, not the unrestricted unicyclic theorem.

### Shared-site cyclic cross-favorability is sufficient for all unicyclic interaction graphs

For a unicyclic direction-interaction graph with arbitrary pendant trees, write the edge color of a core direction \(i\) as \(F_i(a,b;y)\), with \(a,b\) its two cycle-neighbor bits and \(y\) the immediate attached-child bits.

Call a site *responsive* when some complementary choices \(y,\bar y\) produce distinct two-input functions \(F_i(\cdot;y)\ne F_i(\cdot;\bar y)\). Call it *nonresponsive* otherwise.

**Reduction theorem.** The following proposed statement is sufficient to establish paired-root existence for every binary coloring with a unicyclic interaction graph:

> Any pair of arbitrary cyclic-neighbor colorings \(g,h\) whose local functions agree at at least one cycle direction satisfies \(A_0(g)\cap A_1(h)\ne\varnothing\).

*Proof of sufficiency.* If every core site is responsive, the adaptive pendant-polarization theorem in this Subsection already constructs two conditional cycle colorings with a common local \((0,1)\) input at every site. The established cyclic nonempty-overlap theorem then supplies compatible core geodesics and the opposite-bit interfaces restore all pendant trees.

Otherwise choose a nonresponsive site \(j\). By definition, for every attached-bit assignment \(y_j\), the two conditional functions \(F_j(\cdot;y_j)\) and \(F_j(\cdot;\bar y_j)\) agree on all four cycle-neighbor inputs. Choose arbitrary complementary polarizations at the other core sites. The two conditional cycle colorings therefore share their entire direction-\(j\) truth table. The proposed shared-site statement supplies a common opposite-orientation core root; the pendant-tree interface restores its two full geodesics. Hence the full coloring has a paired root. QED.

**Proved constant-site case.** If at the shared site \(j\) both conditional local functions are constants (possibly different), the new 66-state path cross-favorability theorem already supplies the needed core intersection. Therefore any unresolved unicyclic example under this reduction must have at least one nonresponsive core site whose common local two-input function is **nonconstant**.

**Focused remaining cases.** Nonconstant binary functions on two inputs fall into the one-input projection/complement class, the neighbor-parity/complement class, and the eight unbalanced nonlinear truth-table types. Proving the shared-site cross statement for these classes would close every unicyclic interaction coloring in all dimensions, with arbitrary nonlinear attached trees, without requiring unrestricted cross-favorability for every pair of unrelated cyclic colorings.

This is a sufficient proof target, not a claim that the shared-site statement is established.

## Unicyclic paired-root closure with independently functional induced core colorings

Let F color cube edges with a unicyclic undirected direction-interaction graph and arbitrary nonlinear rooted pendant trees. Denote its two induced cycle colorings by g0,g1, obtained by fixing every immediately attached noncore child bit to zero or one respectively. Suppose that at every cycle direction each of the two induced local edge-color functions depends on at most one of its two cyclic-neighbor bits; the controlling neighbor may be different for g0 and g1, and constant functions are permitted.

**Theorem.** Under these hypotheses F has at least two paired roots. Indeed g0 and g1 are unrelated functional-dependency colorings. By the Hall cross-root theorem and its sharp two-root strengthening, |A0(g0) intersect A1(g1)|>=2. The already proved pendant-tree interface lifts each different core root to a different paired root of F. By the free-bridge equivalence, the corresponding next-dimensional antipodally odd NORI1 coloring has monochromatic antipodal geodesics. This allows arbitrary nonlinear functions on all pendant trees; only the two induced core-local functions are restricted. The result does not require nonempty local opposite-color overlap or a jointly constant core direction.

## Unicyclic paired-root closure with one acyclic-facet conditional core

Let F be any binary cube-edge coloring whose undirected direction-interaction graph has one cycle H with arbitrary nonlinear rooted pendant trees. Let g0,g1 be the two induced cycle-core colorings obtained by assigning the immediate pendant-child bits zero or one in the established nonlinear pendant-tree interface theorem. The previously established cyclic-local single-coloring theorem guarantees P(g0) and P(g1) nonempty.

**Theorem.** If either induced core coloring, say g0, has a cycle direction h such that its two fixed-h facet colorings have acyclic directed dependencies, then F has a paired root; likewise if g1 has such a direction. Indeed the new monochromatic confluence theorem says A0(g0) contains a full starting half-cube on one h-bit value. Since P(g1) is antipodally closed and nonempty, one root of an antipodal pair in P(g1) lies in that half-cube. Hence A0(g0) intersect A1(g1) is nonempty. If g1 is the acyclic-facet core instead, use the full half-cube in A1(g1) and a paired antipodal pair in P(g0). In either case the nonlinear pendant-tree interface lifts the common core root to a paired root of F, and the free-bridge equivalence supplies the associated NORI1 monochromatic full antipodal geodesic.

This sufficient all-dimensional closure hypothesis is distinct from a jointly constant core direction, functional core rules, or nonempty local opposite-color input sets. Only ONE of the two conditional core colorings needs an acyclic-facet direction; the other may have arbitrary cyclic-local nonlinear rules. Tree depth, branching, and internal Boolean edge-color functions are unrestricted.
