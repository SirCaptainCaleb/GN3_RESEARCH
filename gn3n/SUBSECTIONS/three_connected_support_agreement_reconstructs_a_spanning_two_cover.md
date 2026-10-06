# Three connected support agreement reconstructs a spanning two cover

## Metadata

- ID: three_connected_support_agreement_reconstructs_a_spanning_two_cover
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 210
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Three-connected support agreement reconstructs a spanning two-cover

Let H be a boundary tournament on a vertex set V with |V|>=4. For each x in V choose a cover F_x of H-x by at most two tight paths. Regard its supports as an unordered partition of V-{x}, allowing an empty part.

Define the support-agreement graph G on V: xy is an edge when the unordered support partitions of F_x and F_y restrict to the same partition of V-{x,y}. Orders inside the supports are not required to agree.

If G is 3-vertex-connected, then H has a spanning two-cover.

Proof. For distinct u,v in V and a hole x outside {u,v}, let R_x(u,v) mean that u and v lie in the same support of F_x. Along any edge xy of G with x,y outside {u,v}, support agreement gives R_x(u,v)=R_y(u,v). Since G-{u,v} is connected, this value is independent of the chosen hole x. Define u~v by this common value, and set u~u.

This relation is an equivalence relation. Symmetry is immediate. For three distinct labels u,v,w, choose a hole x outside {u,v,w}. All three pair relations are then computed in the same two-part partition F_x, which proves transitivity. The same argument shows that there are at most two equivalence classes: three representatives of distinct classes would all lie in different parts of F_x.

If there is only one class, every F_x has a single nonempty support V-{x}. Hence H-x is Hamiltonian, and a Hamilton path on H-x together with {x} two-covers H.

Otherwise let A,B be the two nonempty classes. Choose x in B. The support partition F_x is exactly A | (B-{x}), because every pair relation agrees with ~. Thus H[A] is Hamiltonian. Choosing y in A similarly shows H[B] Hamiltonian. Their two Hamilton paths cover H.

Consequently, in a minimum-order counterexample, every selection of one deletion cover F_x for each hole x has a support-agreement graph that is not 3-connected. In particular, if the graph is connected and has at least four vertices, there is a vertex set of size at most two whose removal disconnects it.

The argument is purely about support partitions and hereditary two-coverability; it requires no path reversal, finite-order verification cutoff, or assumption that local bounded Hamiltonian supports are terminal.

Relevance to Article VII. The compatible-deletion-cover analysis must confront a global separation phenomenon: local agreement cannot be organized into a 3-connected graph without closing the theorem outright. Conversely, a separator in this graph is not yet a separator of the tournament and is not itself closure. The next conversion must exploit the incompatible covers across it, or prove sufficient agreement to eliminate it.
