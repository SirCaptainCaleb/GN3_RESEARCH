# Failed rooted corridor absorption supplies three zero-exit carrier labels

## Metadata

- ID: failed_rooted_corridor_absorption_supplies_three_zero_exit_carrier_labels
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 164
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Failed rooted corridor absorption automatically supplies three zero-exit carrier labels

Retain the rooted corridor setup of [[rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue]]:
\[
T=(x,y,z,\ldots)
\]
is a tight inward corridor, and failure of every direct packet absorption produces three distinct labels
\[
t_1,t_2,t_3
\]
satisfying
\[
h(y,x,t_i)=1
\qquad(i=1,2,3).
\]

Now view the oriented interface edge
\[
(x,y)
\]
as the exit edge of a protected terminal-pair enlargement. For a movable label \(t\), define its exit status relative to this edge by
\[
\delta(t)=h(t,x,y).
\]

Boundary antisymmetry gives
\[
h(t,x,y)+h(y,x,t)=1.
\]
Therefore the three wrong-way hooks satisfy
\[
\boxed{\delta(t_i)=0\qquad(i=1,2,3).}
\]

Hence:

> **Rooted hook / zero-exit bridge.** Failure of direct rooted corridor absorption automatically produces three distinct zero-exit labels for the same oriented interface edge.

This is exactly the combinatorial resource required by the protected-cycle replacement theorems
[[a_four_cycle_has_an_exact_six_label_repair_classification_with_one_exterior_label]]
and
[[sequential_zero_exit_vertex_replacement_fills_protected_pair_cycles]].

No orientation conversion is involved: the equivalence is the literal boundary flip, so it is unaffected by [[audit_cyclic_rotation_invalidates_the_new_descent_and_second_layer_claims]].

### Remaining condition

The carrier replacement theorem requires more than zero exit. If a nonzero-exit cycle vertex \(v\) has current cycle neighbors \(\ell,r\), a replacement label \(t_i\) must also be mutually admissible before the carrier following label with
\[
\ell,\quad v,\quad r.
\]

Thus the combinatorial and topological interfaces now coincide in one coordinate and differ in only one:
- rooted absorption failure supplies **three zero-exit candidates automatically**;
- the unresolved bridge is the **three-neighbor mutual-adjacency** condition for at least one candidate, or an alternative sequence of such replacements.

This identifies the precise remaining information that an ordered packet-repartition theorem must produce.
