# Genuine two deletion obstructions have no small packet tail connectors

## Metadata

- ID: genuine_two_deletion_obstructions_have_no_small_packet_tail_connectors
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 85
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A one-path complement bound

Let R be any tight path in a boundary tournament H, and let E=V(H)-V(R). If deleting at most t vertices from H[E] makes E Hamiltonian, then kappa_2(H)<=t: use that Hamilton path together with R. This is an explicit cover construction, not a minimum-counterexample argument.

Every set E of order at most six becomes Hamiltonian after at most one deletion. For orders at most three it is already Hamiltonian. For order four, delete one vertex and order the remaining triple tightly. For order five, if E is Hamiltonian no deletion is needed; otherwise [[smallset01]] says that at most one of its five four-subsets is non-Hamiltonian, so some deletion leaves a Hamiltonian four-set. For order six, the four-of-six theorem in [[smallset01]] supplies a Hamiltonian five-subset.

It follows that
\[
\kappa_2(H)\ge2\quad\Longrightarrow\quad
|V(H)-V(R)|\ge7
\]
for every tight path R. Equivalently, every Hamiltonian support has order at most |V(H)|-7. For a hypothetical genuine reflected double of order twelve, this bounds every tight path by five vertices. This is a necessary condition, not a bounded-order reduction.

## The packet consequence

Suppose V(H)=S disjoint-union V(T) disjoint-union V(U), where T and U are tight paths, each of order at least two, and |S|<=7. Define a connector v in S to mean that either (T,v,U) or (U,v,T) is a tight path. Such a path covers all vertices outside S together with v, so its complement has order |S|-1<=6. The preceding construction proves kappa_2(H)<=1.

Therefore a genuine two-deletion obstruction admits **no** connector in any such packet decomposition. In particular, for each six-vertex packet and each of its complementary two-tail decompositions from [[mobile_corridor_cuts_give_a_twenty_vertex_tail_joining_certificate]], the connector set is empty. The earlier criterion with at least three connectors is a full two-cover certificate for arbitrary instances; it understates the restriction in the genuine kappa_2=2 branch.

The same observation applies to the common-packet and neighboring-cut constructions. A single connector already rules out kappa_2=2; repetition across neighboring cuts is not needed for that conclusion. It is still possible that the instance has kappa_2=1 rather than zero. Thus this strengthening does not replace the Hamiltonian-deletion test needed to produce an outward repair of the whole reflected span.

## Explicit residual inequalities

Write T=(t_1,...,t_p), U=(u_1,...,u_q), p,q>=2. For every v in S, genuineness forces
\[
h(t_{p-1},t_p,v)\,h(t_p,v,u_1)\,h(v,u_1,u_2)=0
\]
and
\[
h(u_{q-1},u_q,v)\,h(u_q,v,t_1)\,h(v,t_1,t_2)=0.
\]
These products express that each proposed joined order has at least one non-tight crossing triple. They must hold for every displayed complementary tail decomposition, including all legal mobile corridor cuts. They are stronger than saying a connector is confined to a non-Hamiltonian packet deletion.

No internal deletion of a tight path is assumed in this argument. The sole deletion occurs inside the separate complement of the newly constructed long path.
