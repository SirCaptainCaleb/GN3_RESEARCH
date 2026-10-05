# Rooted five-component endpoint synchronization is a closed bounded theorem

## Metadata

- ID: rooted_five_component_endpoint_synchronization_is_a_closed_bounded_theorem
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 80
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Rooted five-component endpoint synchronization is now a closed bounded theorem

Let
\[
Y\mid P\mid Q
\]
be a spanning three-cover with
\[
|Y|=5,
\]
where \(Y\) contains two distinguished labels \(x,y\). Assume both \(P,Q\) have order at least two.

For each of the four displayed endpoints \(e\) of \(P,Q\), consider the six-set
\[
U_e=Y\cup\{e\}.
\]

Then at least one of the following holds.

1. **Direct endpoint enlargement.** Some \(U_e\) is Hamiltonian. Then replacing \(Y\) by \(U_e\) and truncating the corresponding tail gives a larger Hamiltonian support with two-coverable complement.

2. **Bounded Hamiltonian disturbance.** For some exposed endpoint \(e\), the packet \(U_e\) contains a Hamiltonian support arising from the common-core/four-of-six analysis, of order at most six and with the explicit endpoint/core incidences supplied by that analysis.

3. **Positioned reversal.** For some exposed endpoint \(e\), the packet \(U_e\) contains a tight triple reversing an ordered edge of one of the Hamiltonian endpoint-core paths.

### Proof

Assume no \(U_e\) is Hamiltonian. For each endpoint define
\[
A_e
=
\{r\in Y-\{x,y\}:(Y-\{r\})\cup\{e\}\text{ is Hamiltonian}\}.
\]
Four-of-six gives \(A_e\ne\varnothing\).

The four-endpoint synchronization theorem [[the_four_endpoint_incidence_system_cannot_remain_featureless]] shows that these four endpoint tests cannot all remain featureless. Its outputs are order disagreement, positioned reversal, or bounded Hamiltonian support.

By [[bounded_order_disagreement_reduces_to_reversal_or_hamiltonian_support]], order disagreement itself reduces to positioned reversal or Hamiltonian support. The matching-block equality exception does not create a further branch: [[the_matching_block_one_edge_completion_branch_is_impossible]] returns it to bounded Hamiltonian support.

Hence only outcomes 2 and 3 remain when direct endpoint enlargement fails. ∎

### Frontier consequence

The rooted five-component endpoint problem is closed as a synchronization problem. There is no remaining label-incidence, equality, matching-block, or edge-order completion branch.

The next theorem needed by Article VII is therefore a **rooted disturbance conversion theorem**:

> Given a genuine two-deletion reflected-double state whose central/rooted five-component produces outcome 2 or 3 above, use the retained endpoint/root incidences to obtain either a spanning two-cover or an enlarged protected outward repair.

This is strictly narrower than the previous endpoint-handoff problem: the input is now a bounded six-label Hamiltonian/reversal certificate attached to the actual exposed corridor endpoints.
