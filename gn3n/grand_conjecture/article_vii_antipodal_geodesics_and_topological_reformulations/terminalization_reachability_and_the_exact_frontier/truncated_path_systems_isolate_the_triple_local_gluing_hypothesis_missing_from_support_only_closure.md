# Truncated path systems isolate the triple-local gluing hypothesis missing from support-only closure

## Composition

(none yet)

## Development

This is an abstract countermodel to specified support-only hypotheses, NOT a counterexample boundary tournament. It explains why 276's relative detector does not itself supply a nonzero class.

CONSTRUCTION.
Fix r>=4 and n=2r+1, with vertices 1,...,n in their usual order.
Let H_0 be the genuine boundary tournament in which (u,v,w) is tight exactly when u<w. Each reversal pair has exactly one tight member.
Define an ABSTRACT admissible-path system A_r by declaring a vertex-simple word P admissible exactly when:
(1) |P|<=r;
(2) every consecutive triple (u,v,w) of P satisfies u<w.
Thus A_r agrees with the tight paths of H_0 up to order r, and imposes an extra length cap beyond r.

VERIFIED PROPERTIES.
(a) Its admissible words are closed under contiguous restriction, in particular under prefix and suffix restriction.
(b) Its three-vertex admissibility satisfies exactly the boundary reversal rule.
(c) A subset S is Hamiltonian in this abstract system if and only if |S|<=r. For the forward direction use the cap; for the reverse direction use the increasing vertex order of S.
(d) Every proper induced ground set W has a two-path cover: |W|<=2r, so partition W into at most two sets of size at most r and order each increasingly.
(e) The full ground set has path-cover number exactly three, since two admissible paths have at most 2r vertices, while three suffice.
(f) Its two-cover deletion distance is one.
(g) Every balanced deletion partition r|r is Hamiltonian, every one-vertex extension to an (r+1)-set is non-Hamiltonian, and its deletion interface is the complete odd middle layer.
(h) Every admissible support is accessible by Hamiltonian prefixes, so the prefix-chain conclusions of 272 apply at the support level.
(i) Its Hamiltonian-support poset is the nonempty face poset of the full (r-1)-skeleton of the (n-1)-simplex. This skeleton is (r-2)-connected, hence at least 2-connected. One proof uses simplicial approximation and cones: a j-sphere with j<=r-2 can be filled by coning its simplices to a vertex, and each cone simplex has dimension at most j+1<=r-1.
(j) Its signed downward complex is the middle Bier sphere, of equivariant index n-2. Its balanced complex has dimension n-3 and the relative top group in 276 is zero.
(k) For any fixed packet order b, choosing r>=max{4,b} makes the abstract system agree EXACTLY with the genuine boundary tournament H_0 on all words and induced sets of order at most b.

THE PRECISE FAILURE.
The increasing spanning word (1,2,...,n) has every consecutive triple tight in H_0, but is NOT admissible in A_r. Therefore A_r is not the tight-path system of any boundary tournament with those triples. It violates the sufficiency direction of triple locality:
a vertex-simple word whose every consecutive triple is tight must itself be a tight path.

Consequently the following collection of hypotheses is insufficient to derive a spanning two-cover:
proper-induced two-coverability, the exact support-rank identities, Hamiltonian prefix accessibility, low-dimensional Hamiltonian-support connectivity, the universal balanced deletion family, and the resulting antipodal support topology.
For every fixed b this remains true even after adjoining every statement confined to induced sets and admissible words of order at most b which holds in the genuine tournament H_0.

Scope of this conclusion.
It does NOT rule out a proof using a bounded local surgery and arbitrarily long inherited tails. Such a proof explicitly invokes triple locality when it checks the finitely many new seams and concatenates the long pieces. That is exactly the hypothesis the countermodel omits.
It also does NOT show that the odd middle-layer support family is realizable by a genuine boundary tournament.

STRATEGIC CONSEQUENCE.
The relative top-homology group in 276 correctly DETECTS a full-support cell; support-only data does not FORCE one.
A closure argument must retain enough ordered-path information to justify unbounded gluing, or prove a new support theorem using triple locality in its proof. Forgetting path orders and then applying only generic connectivity/index arguments loses this decisive implication.
The next genuine mathematical target is therefore an augmentation or composition theorem for displayed tight paths. No such theorem, and no nonzero relative top class, is established by this countermodel.
