# Minimum-blue faces, face-cut obstruction, and critical-boundary scope

- Stable ID: note_nori_xvii_minority_minimizer_face_saturation_r12176
- Author: session_nori_r12181_1
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, global-minimality, face-exchange, critical-boundary
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12176_1
- Updated session: session_nori_r12181_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Full-face saturation at a minimum-color geodesic

Session session_nori_r12176_1. Let c be a binary coloring of the undirected edges of Q_n. For a full direction-simple antipodal geodesic P, let b(P) be its number of color-1 edges and let delta=min_P b(P).

**Theorem (monochromatic face saturation).** If P attains delta, every maximal consecutive color-1 run of P with free-direction set S and endpoints u,v=u xor 1_S spans an entire S-face F all of whose original edges have color 1. Every permutation of this run's directions is again a delta-minimizing full geodesic, retaining both its direction-indexed color profile and its oriented selector q(P)_i=x_i+c_i(e_i(P)), where x is its root.

*Proof.* Swap any two consecutive color-1 directions in P. The new route replaces only the two edges of their square; its new pair has at most two color-1 edges. Global minimum blue count forces both replacements to be color 1. The resulting path retains delta. Transpositions generate every order on S; induction preserves all colors on the run and all edges outside it. Every edge of F appears in some direction-once u-to-v order, hence is color 1. The profile and selector remain constant. QED.

Suppose further that c is antipodally odd: c_i(bar x)=1+c_i(x). The antipodal face bar F is entirely color 0. A true cyclic root-slide of a full path replaces the first edge color w_1 by 1-w_1 as its last edge, changing b by 1-2w_1. The reverse root-slide changes b by 1-2w_n. Thus every global delta-minimizer has first and last edges of color 0 (when delta>0), and each blue run has two adjacent red cap edges.

**Boundary-gate inequalities and full-face migration.** Let a be the red direction immediately preceding an all-blue S-run, y the run's entry vertex, and i any direction in S. Reorder S to place i first, preserving delta. Swapping a and i yields replacement colors c_i(y^a),c_a(y^i) for the old (0,1) pair. Minimality forces
c_i(y^a)+c_a(y^i)>=1.                                        (FG1)
If c_i(y^a)=0 and c_a(y^i)=1, the swap preserves delta and yields a new consecutive blue run with free directions S'=(S\{i}) union {a}. The new S'-face F' is entirely blue, and F,F' meet in one common (|S|-1)-face. The original-color agreement on their overlap is automatic; the oriented selectors satisfy
q(P')=q(P) xor e_a xor e_i.                                 (FG2)
There is an analogous right-cap exchange replacing the final direction i of the blue run by its succeeding red direction b when the corresponding swapped two-edge word is (1,0).

*Proof.* The old path follows a red edge y^a->y, then the blue i-edge y->y^i. The exchanged path first uses red i from y^a, then blue a into y^i, followed by the other |S|-1 blue directions. Apply the saturation theorem to the new minimizing path. Its face frees S' and fixes i at the value after the new first step, whereas the old face frees S and fixes a at the value after the old first step; their intersection frees precisely S\{i}. All unchanged directions retain their edge colors, and directions i,a exchange their colors 1,0, proving (FG2). The right-cap argument is symmetric. QED.

**Scope and forcing obligation.** For a hypothetical bad antipodally odd coloring, delta>0. Hence the family of *globally minimum-blue* full geodesics supplies monochromatic cubical faces with contractible order-permutation fibers and legal facet-to-facet transports preserving the minimum and original edge consistency. The OR condition (FG1) still permits an increasing-cost boundary exchange; it does not ensure enough facet transports to force a projectively essential direction-once red loop. The missing argument must produce those transports using simultaneous constraints from the same coloring, or derive a separate global contradiction. This result supplies integral path carriers and a precise exchange, without asserting unrestricted NORI1.

## Whole-face cap transport and its Boolean cut

Continue with the minimum-blue full geodesic P and an all-blue consecutive run with free-direction set S, entry vertex y, and immediately preceding red edge in direction a from y^a to y. Let F^a denote the parallel S-face based at y^a. For T subset S and a direction-simple monotone path H in F^a from y^a to y^(a xor T), let r(H) be the number of red edges of H, with colors 0=red, 1=blue.

**Theorem (all-prefix gate inequality).** For every T and H,
\[
\boxed{r(H)\le c_a(y^T)\le1.}\tag{PF1}
\]
*Proof.* By minimum-blue run saturation, rearrange the original blue run so that its first |T| directions follow H's order. Replace the segment consisting of the preceding red a-edge and those |T| original blue edges by H, then the a-edge at y^T. The endpoints, support, all remaining segments, and original prescribed edge colors agree with a full direction-once antipodal path. Its blue count minus that of P is c_a(y^T)-r(H). Minimality gives PF1. QED.

Define U to be the upward closure in 2^S of the heads (rank-increasing endpoints) of all red edges in F^a. Then
\[
\boxed{U\subseteq\{T\subseteq S:c_a(y^T)=1\}.}\tag{PF2}
\]
Every red edge of F^a crosses from the lower ideal 2^S\U into U; every edge with both endpoints in either region is blue. Indeed any monotone path in F^a has at most one red edge by PF1 with T=S. If a red edge had its lower endpoint in U, one could precede it by another red edge along a monotone path, contradiction; membership of its upper endpoint in U is automatic. If T belongs to U, choose a monotone path to T containing the relevant red edge, then PF1 forces c_a(y^T)=1. This is an integral upper-cut/gate compatibility derived from all prefix exchanges, strengthening the earlier two-edge square inequality. The analogous right-cap argument produces a downward-closed cut in the parallel face on the other side of the blue run.

If U is nonempty then the opposite a-edge at y^S is blue, and moving the red cap past a monotone prefix H containing one red edge gives another minimum-blue full path (the difference in blue counts vanishes). Such an exchange need not preserve the number of blue runs. If U is empty, F^a is itself all blue; PF1 need not supply any nontrivial equality exchange. This dichotomy is the precise information available from the entire adjacent face, without an unsupported assumption about the other faces or minimizers.

## Why minimum-color faces alone cannot carry the antipodal index

Let X be the dual all-root Freudenthal chamber complex, with a vertex for each rooted full geodesic P, and J the free antipodal chamber involution. Put b(P)=the blue-edge count, delta=min_P b(P). Antipodal oddness implies b(JP)=n-b(P). Thus delta<=n/2. Equality would force every rooted full path to have b=n/2. Yet cyclically moving the first direction of any path to the last position while sliding its root replaces its first edge by its antipodal mate and changes b by 1-2w_1, which is either +1 or -1. Therefore
\[
\boxed{\delta<n/2.}\tag{PF3}
\]

For any integer t<n/2, let L_t be the full subcomplex of X on the chamber vertices with b(P)<=t. Its antipodal image J L_t consists of vertices with b(P)>=n-t>t. The two subcomplexes have disjoint vertex sets and are disjoint as polyhedra. Hence
\[
L_t\sqcup J L_t \longrightarrow (L_t\sqcup J L_t)/J\simeq L_t
\]
is a trivial double cover, with a continuous section choosing L_t. In particular the first Stiefel-Whitney class of this cover and all its powers vanish.

**Research implication.** The low-blue and high-blue extrema—even with all monochromatic-face fibers and their min-preserving facet transports—have no antipodal cohomological index until additional intermediate-color chambers are included. The forced topology of the full Freudenthal sphere does not automatically restrict to global minority minimizers. A plausible global approach must couple a middle-level equivariant obstruction to the endpoint face-cut data by a justified direction-simple path exchange or a relative obstruction. Further refinements of one face's gate inequalities alone cannot supply that link.

## Critical-boundary scope: why full-face cuts are insufficient for closure

The legal coloring space in dimension n is a finite hypercube, one binary choice per antipodal unoriented-edge orbit, and is connected. It contains a coloring with a red full geodesic, e.g. \(c_i(x)=x_{i+1}\) for indices modulo n, using direction order \(1,\ldots,n\) from root \(x_1=1,\ x_2=\cdots=x_n=0\). If any bad coloring exists, choose a path through the coloring hypercube from a good coloring to it and its first good-to-bad single-orbit flip \(c^+\to c^-\). Every red full geodesic P in \(c^+\) traverses the red member e of the flipped orbit: if it avoided this orbit, it would remain red in \(c^-\). A direction-once path uses at most one edge from a given orbit. Therefore that P acquires precisely one blue edge after the flip, while no all-red geodesic exists in \(c^-\). Thus
\[
\boxed{\text{NORI1 failure implies a bad coloring with global minimum blue-edge count }\delta=1.}
\tag{CB1}
\]
This is the established critical-orbit reduction in Article XVI, here included to delimit the applicability of the new face-cut theorems.

In this sufficient critical case, every minimum-blue full path has only one blue edge. Its saturated blue-run face has dimension one; the all-prefix gate inequality PF1 reduces to its original single-square version FG1. Therefore higher-dimensional face saturation and its Boolean cut cannot by themselves settle unrestricted NORI1. The critical flip, on the other hand, forces a common original red edge in every red full path of \(c^+\), while \(c^-\) has no successful full path. These simultaneous, same-coloring constraints were absent from the original minimum-blue face argument.

**Decision.** Treat the face-cut theorem as a supporting structural result, and shift the central forcing target to the whole one-defect family at a good-to-bad coloring-space boundary. The missing implication is a compatible integral exchange or relative topological obstruction ruling out this critical configuration, with root freedom, shared-edge consistency, and one use of each original direction retained. Scalar level-set topology on global blue-count minima alone cannot do so, by PF3 and the trivial-cover argument.
