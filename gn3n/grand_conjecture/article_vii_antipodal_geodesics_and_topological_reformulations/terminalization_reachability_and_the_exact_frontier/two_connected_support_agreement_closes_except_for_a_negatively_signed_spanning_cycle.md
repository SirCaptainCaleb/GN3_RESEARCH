# Two connected support agreement closes except for a negatively signed spanning cycle

## Composition

(none yet)

## Development

## A two-connected support-agreement graph closes unless it is one negatively signed spanning cycle

Retain the deletion covers F_x and the support-agreement graph G from [[three_connected_support_agreement_reconstructs_a_spanning_two_cover]], with |V|>=4.

If G is 2-vertex-connected, then either H has a spanning two-cover, or G is exactly a spanning cycle and the support identifications around that cycle exchange the two sides.

Proof. Temporarily name the two support parts of each F_x by signs +1,-1; an empty part is allowed. Write chi_x(v) for the sign of v in F_x. Each agreement edge xy has a unique sign epsilon_xy in {+1,-1} such that
chi_x(v)=epsilon_xy chi_y(v) for every v outside {x,y}.
Uniqueness follows from the nonempty common domain, and existence from agreement of the unordered partitions.

For any cycle in G omitting a vertex v, multiply these equations at v around the cycle. The product of the edge signs is +1.

If a cycle visits every vertex and G has an additional edge, that edge is a chord of the cycle. Splitting along the chord gives two cycles, each omitting at least one vertex. Their sign products are +1, and multiplying cancels the chord sign twice. Thus the spanning cycle also has positive product.

Consequently, if G is not exactly one spanning cycle, every cycle has positive product. Choose a base vertex and multiply edge signs along paths to obtain signs tau_x; the positive-cycle property makes this independent of the chosen path. Renaming the parts of F_x using tau_x makes chi_x(v)=chi_y(v) along every edge xy whenever v is in the common domain.

Since G-v is connected for every vertex v, the sign assigned to v is then independent of the hole x!=v. Hence all deletion partitions are restrictions of one global bipartition of V. As in the preceding reconstruction theorem, if both classes are nonempty, choose a hole in the opposite class to see each full class Hamiltonian; if only one class is nonempty, H-x is Hamiltonian and {x}|(H-x) is a two-cover.

If G is exactly a spanning cycle but its edge-sign product is positive, the same path-product argument applies and again gives a spanning two-cover. The only remaining possibility is the spanning cycle with negative product.

Thus every selected family of deletion covers in a minimum counterexample satisfies a sharper global alternative:
G is disconnected, G has a cut vertex, or G is exactly a negatively signed spanning cycle.
In particular, a support-agreement graph containing a spanning cycle and even one additional agreement edge already closes the grand two-cover statement for that H.

No internal Hamilton order agreement is assumed. The exceptional cycle records genuine failure to name the two sides consistently around all holes; it is not a bare bounded-support handoff. This identifies the precise global obstruction left by support-level coherence, independently of tournament order.
