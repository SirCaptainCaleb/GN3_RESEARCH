# Closed minimum-cover cores force uniform half-order Hamiltonicity and deletion-critical middle sets

## Metadata

- ID: closed_minimum_cover_cores_force_uniform_half_order_hamiltonicity_and_deletion_critical_middle_sets
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 262
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Closed cores of minimum-imbalance covers have only a middle-rank residue

Assume H has no spanning two-cover, on n vertices. For each hole, keep only deletion-cover support partitions minimizing Phi at that hole. Represent an oriented deletion facet by its dual cube edge A -> A-{x}, with x in A; its two Hamiltonian supports are A-{x} and V-A.

Let R be a nonempty antipodally invariant collection of these edges satisfying the square cocycle condition: every cube square contains an even number of R-edges. Such an R is exactly the kind of nonempty top core which can remain after the paired unique-face collapses of subsection 258, if those collapses are started on the minimum-imbalance facet family.

No monotonicity of a global Boolean potential is assumed.

### Theorem

If n=2r+1 is odd, R is the COMPLETE incidence layer between all (r+1)-sets and all r-sets. Hence:
1. every r-set is Hamiltonian;
2. every (r+1)-set is non-Hamiltonian and all its vertex deletions are Hamiltonian;
3. the maximum Hamiltonian support order is exactly r.

If n=2r is even, all R-edges lie in the two middle incidence layers, from r-sets to (r-1)-sets or from (r+1)-sets to r-sets. Moreover:
1. exactly one of S and V-S is Hamiltonian for every r-set S;
2. every non-Hamiltonian r-set has all its vertex deletions Hamiltonian;
3. no (r+1)-set is Hamiltonian, so the maximum Hamiltonian support order is exactly r.

Thus a nonempty closed minimum-cover core is far more rigid than an arbitrary self-antipodal Johnson component. In odd order it is the full middle layer; in even order it is a complementary choice on the middle rank, with deletion-critical non-Hamiltonian members.

### Proof: the only parallel-square exceptions are the middle ranks

Every nonisolated R-vertex is a pure source or pure sink under the natural cube orientation. Indeed, an outgoing edge at A certifies V-A Hamiltonian and an incoming edge at A certifies A Hamiltonian. Having both would two-cover H.

Take an edge A -> A-{x}, and put m=|A|.

For y outside A, consider the square with vertices
A-{x}, A, (A-{x})+y, A+y.
The edge A+y -> A is forbidden, since A is already a source. The opposite parallel edge A+y -> (A-{x})+y, if present, would be a same-hole transfer at hole x. The two endpoint deletion covers have potentials
(m-1)^2+(n-m)^2
and
m^2+(n-m-1)^2,
whose difference is 2(2m-n).
Both are minimum covers at the same hole, so equality is necessary. Unless 2m=n, that parallel edge is absent. Square parity then forces the remaining edge
(A-{x})+y -> A-{x}.
Thus upper-star propagation is forced unless m=n/2.

Similarly, for z in A-{x}, use the square obtained by also removing z. The edge leaving A-{x} downward is forbidden because A-{x} is a sink. The opposite parallel edge is a same-hole transfer whose potentials can be equal only when 2(m-1)=n. Unless m=n/2+1, parity forces
A -> A-{z}.
Thus lower-star propagation is forced except at the other middle rank.

If neither exception applies, every source in the component has every downward incidence, and every sink has every upward incidence. The bipartite incidence graph between all m-sets and all (m-1)-sets is connected: a one-element Johnson exchange between two m-sets passes through their common (m-1)-set, and all m-sets are connected by such exchanges. Consequently this component is the COMPLETE rank-m incidence layer.

A complete rank-m layer certifies every (m-1)-set Hamiltonian and, by taking complements of sources, every (n-m)-set Hamiltonian. Put k=max(m-1,n-m). If k>=ceil(n/2), choose a Hamilton path on any k-set and take a contiguous subpath on n-k vertices. Its complement is a k-set and hence Hamiltonian. These two supports give an ACTUAL spanning two-cover, contradiction.

For odd n=2r+1 there are no integer parallel-square exceptions. The only rank avoiding this last contradiction is m=r+1, for which k=r. Therefore every nonempty component is the entire middle layer. Its sources are every (r+1)-set, all non-Hamiltonian; its sinks are every r-set, all Hamiltonian. Every Hamilton path longer than r would contain a contiguous Hamiltonian (r+1)-set, impossible. This proves the odd statement.

For even n=2r, all non-middle components likewise propagate to a full layer and contradict no-two-cover. Only source ranks r and r+1 remain.

### Proof: the even middle-rank choice is self-dual and deletion-critical

Since R meets every cube square evenly, R=delta f for a Boolean function f on cube vertices. One elementary proof defines f(A) by counting R-edges along a path from the empty set to A; exchanging adjacent coordinate steps changes the count by one square boundary, hence by zero. Backtracking also has zero count. Thus the value is independent of the path.

All vertices of rank at most r-1 have one common f-value alpha, because their induced cube graph is connected and has no R-edges. All vertices of rank at least r+1 similarly have one common value beta.

If alpha=beta, any rank-r vertex whose value differs would have both all incoming and all outgoing incident edges in R, violating source/sink purity. If none differs, R is empty. Thus alpha!=beta.

Every r-set S is therefore nonisolated:
- if f(S)=alpha, all its edges from (r+1)-supersets lie in R, so S is a sink and Hamiltonian;
- if f(S)=beta, all its downward edges lie in R, so S is a source and non-Hamiltonian, while EVERY S-{x} is Hamiltonian.

Antipodal invariance implies delta(f(A)+f(V-A))=0, so f(A)+f(V-A) is constant. Evaluating in the lower and upper regions gives that constant as 1. Hence exactly one of each complementary pair of r-sets is a sink, equivalently Hamiltonian.

Finally suppose an (r+1)-set U were Hamiltonian. A Hamilton order of U supplies a Hamiltonian r-set S by deleting an endpoint. Such an S is a sink, so the edge U -> S belongs to R. But any source U of that edge is non-Hamiltonian, contradiction. Longer Hamilton paths are excluded by contiguous restriction. This proves the even statement. QED.

## A terminating normalization, with its limit stated

Start with all oriented minimum-imbalance deletion facets and their faces. Every codimension-one face has at most two cofacets, by the crossed-extension exclusion of subsection 257. Collapse a unique-incidence face and its top facet together with their antipodes. The two antipodal collapses cannot interfere: a signed face and its antipode have disjoint signed vertex sets. Every step removes two top facets, so the process terminates.

If the residue is nonempty and has no unique codimension-one face, its dual edges satisfy the square cocycle condition. The theorem above therefore classifies its entire possible nonempty residue.

If all top facets collapse, there is NO nonempty core to which the theorem applies. This branch is NOT a contradiction and is NOT closure. Nor is the classified half-order residue yet contradictory: the remaining tournament-specific problem is to exclude its universal critical family or produce a two-cover mixing its supports.

In particular a Hamiltonian support larger than floor(n/2) rules out a nonempty closed minimum-cover core; it forces the all-collapsed branch. This is a valid use of the largest-support lemmas, without mistakenly treating collapse alone as a spanning cover.

No small-order cutoff is used. The square calculation and propagation are valid at arbitrary order.

## Frontier

- Development version when composed: None
- Development version now: 1
