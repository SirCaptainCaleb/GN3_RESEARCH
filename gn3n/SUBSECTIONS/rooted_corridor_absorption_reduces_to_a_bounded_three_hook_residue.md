# Rooted corridor absorption reduces to a bounded three-hook residue

## Metadata

- ID: rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 40
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["reflected_double_carriers_reduce_to_two_bounded_rooted_endpoint_interfaces", "localextend01", "correction_rooted_four_core_extension_is_not_automatic"]

## Cold composition

(none yet)

## Development

## Rooted corridor absorption reduces to a three-hook residue

The rooted endpoint problem from [[reflected_double_carriers_reduce_to_two_bounded_rooted_endpoint_interfaces]] admits a useful finite reduction using the prescribed-endpoint seven-set theorem in [[localextend01]].

Let
[
T=(x,y,z,ldots)
]
be a tight path forming the inward frozen corridor, so in particular
[
(x,y,z)
]
is tight. Let (A) be any six vertices disjoint from (T-{x}), and put
[
U=Acup{x}.
]

The seven-set prescribed-endpoint theorem gives a (4|3) two-cover
[
Kmid R
]
of (U) in which (K) has a Hamilton order ending at (x). Moreover, among all such covers at least three distinct vertices of (A) occur as the predecessor of (x).

Write one such path as
[
K=(k_1,k_2,t,x).
]

If
[
(t,x,y)
]
is tight, then
[
(k_1,k_2,t,x,y,z,ldots)
]
is a tight path, because the last old triple of (K), the bridge triple ((t,x,y)), and the first corridor triple ((x,y,z)) are tight. Consequently
[
(Kmathbin{aisebox{.15ex}{(smallfrown)}}(y,z,ldots))mid R
]
is a two-path cover of (Acup V(T)).

Therefore:

**Rooted absorption lemma.**
A six-vertex endpoint packet can be absorbed into a frozen tight corridor while retaining a two-cover unless every available predecessor (t) of the interface vertex (x) satisfies
[
(y,x,t)	ext{ tight}.
]
Since there are at least three distinct available predecessors, failure of direct absorption produces three distinct vertices
[
t_1,t_2,t_3in A
]
with
[
(y,x,t_i)
]
tight for all (i).

Thus the rooted endpoint obstruction is not an arbitrary seven-vertex configuration. It is a bounded **three wrong-way hooks** residue through the ordered pair ((y,x)).

The local-extension toolkit already gives additional structure in this residue: three common hooks through an ordered anchor pair force a Hamiltonian four- or five-support containing that pair. What is still needed is an ordered version strong enough either to expose the pair in the orientation required to concatenate with the corridor or to repartition the remaining endpoint packet simultaneously.

For reflected-double terminal surgery this is useful because each selected determining window uses at most six vertices. After adding the corridor interface vertex if necessary, every one-sided endpoint repair fits into the seven-set framework above. Hence the unbounded reflected-double branch reduces further to two bounded three-hook residues, one at each end, with the long positive-word-free corridor frozen between them.

This does not yet close the branch: support-level Hamiltonicity of the anchor-containing four/five-set does not automatically give the required endpoint order, as emphasized by [[correction_rooted_four_core_extension_is_not_automatic]]. The remaining theorem is an ordered three-hook absorption/repartition statement, not a new unbounded phenomenon.
