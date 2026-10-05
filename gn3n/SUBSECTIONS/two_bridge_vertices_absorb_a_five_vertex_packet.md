# Two bridge vertices absorb a five-vertex packet

## Metadata

- ID: two_bridge_vertices_absorb_a_five_vertex_packet
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 56
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Lemma. Let S be any five-vertex set and Q=(q_1,...,q_t), t>=2, a disjoint tight path in a boundary tournament. Put
G={u in S:h(q_{t-1},q_t,u)=1}.
If |G|>=2, then S union V(Q) has a two-path cover. More precisely, either S is Hamiltonian and the cover is S|Q, or there is u in G such that S-u is Hamiltonian and the cover is (S-u)|(Q,u), of orders 4,t+1.

Proof. If S is Hamiltonian, the first cover suffices. Otherwise the non-Hamiltonian-five-set theorem in [[smallset01]], Section 7, says that at most one four-subset of S is non-Hamiltonian. Thus at least four of the five vertex deletions are Hamiltonian. Since G has at least two vertices, one u in G has S-u Hamiltonian. The bridge makes (Q,u) tight. No prescribed endpoint theorem or reversal of a tight path is used. QED.

There is a symmetric initial-bridge version: replace the bridge test by h(u,q_1,q_2)=1 and prepend u. This is a new proof with the initial ordered pair, not a reversal of Q.

Exact failure description for this procedure. It can fail only when S is non-Hamiltonian and either G is empty, or G consists of a single vertex u with S-u non-Hamiltonian. This follows because any bridge with a Hamiltonian deletion already supplies the cover. Such failure does not establish that no other two-cover exists.

This improves the four-reversed-bridge criterion of [[four_reversed_bridge_vertices_give_a_protected_packet_corridor_repair]] when component sizes are allowed to vary: there S=A union {y}, Q=Z^{rev}, and a zero h(u,z_1,z_2) supplies a terminal bridge h(z_2,z_1,u)=1. Two such vertices already suffice for a two-cover, of orders 5,d or 4,d+1. Four bridges are still a convenient sufficient condition for the specific 4|(d+1) partition proved there.

Application to a same-word positive span-two double. In the 001/001 case of [[complete_positive_span_two_double_corridor_classification]], the short corridor path has order two and the left exterior vertex is absorbed into a tight three-path R=(p_2,p_1,x). The remaining data are a long tight path Q and one exterior vertex y. If |Q|>=3, remove its terminal vertex q_t and set
S=V(R) union {y,q_t},  Q'= (q_1,...,q_{t-1}).
This is a five-packet and a tight path. The packet vertex q_t is a bridge to Q' by the original path triple. Therefore either of the following suffices:
(1) S is Hamiltonian;
(2) V(R) union {y}=S-q_t is Hamiltonian;
(3) some u in V(R) union {y} satisfies h(q_{t-2},q_{t-1},u)=1.
In (1) use S|Q'; in (2) use (S-q_t)|Q; in (3) the two-bridge lemma applies. If |Q|=2, the complete span has at most six vertices and the elementary two-cover bound applies.

If all three tests fail, the residual conditions are explicit: S and S-q_t are non-Hamiltonian, q_t is the unique terminal bridge from S to Q', and every u in V(R) union {y} satisfies the reverse triple h(u,q_{t-1},q_{t-2})=1. This is a finite packet plus one ordered tail-pair obstruction, not a proof that the branch is impossible.

The 011/011 case is the counterpart obtained by applying the same argument to the other short path and its actual tight orientation. A two-cover of the complete determining span can be inserted as a positive-word-free order and yields an outward chamber, with frozen inherited-mask carriers on a fixed ambient source face. General mixed doubles and compatibility across ambient faces remain open.
