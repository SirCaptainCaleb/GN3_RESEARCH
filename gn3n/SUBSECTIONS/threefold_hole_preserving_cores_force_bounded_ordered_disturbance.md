# Threefold hole-preserving cores force bounded ordered disturbance

## Metadata

- ID: threefold_hole_preserving_cores_force_bounded_ordered_disturbance
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 62
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Threefold hole-preserving cores already force bounded ordered structure

Retain branch (1) of [[four_endpoints_force_a_threefold_core_or_two_double_hole_equality_endpoints]]. Thus
\[
Y\mid P\mid Q
\]
is a spanning three-cover with
\[
Y=C\cup\{r\},\qquad |C|=4,
\]
where \(C\) contains the two distinguished hole labels, and there are three distinct exposed tail endpoints
\[
e_1,e_2,e_3
\]
such that
\[
C\cup\{e_i\}
\]
is Hamiltonian for \(i=1,2,3\).

The ordered common-core analysis following Lemma 6 of [[longest_paths_and_reversal_structure_a_common_four_vertex_core]] depends only on these three Hamiltonian five-extensions, not on the separate minimum-counterexample argument used there to obtain two-coverable complements. Apply that local analysis to
\[
C,\ e_1,e_2,e_3.
\]

Choose Hamilton orders on the three five-sets \(C+e_i\). If two induce different relative orders on \(C\), there is an order disagreement on the common four-label support.

Otherwise all three roots occur as insertions into gaps of one common relative order on \(C\). The gap analysis gives one of the following:

1. two roots occupy separated gaps, yielding a Hamiltonian six-set;
2. two roots occupy adjacent gaps, yielding either a Hamiltonian six-set or a tight triple reversing the intervening core edge;
3. two roots occupy one common internal gap, yielding a Hamiltonian four-set;
4. all three roots occupy one endpoint gap, and boundary antisymmetry among the roots yields a Hamiltonian four-set.

Hence:

> **Threefold-core disturbance theorem.** A hole-preserving four-core accepting three exposed endpoints cannot remain featureless. It forces a Hamiltonian support of order four or six, an order disagreement on the core, or a positioned reversing tight triple through a core edge.

This conclusion is purely local. It does not require the complements of the five-extensions to be two-coverable.

Consequently branch (1) of [[four_endpoints_force_a_threefold_core_or_two_double_hole_equality_endpoints]] already lies in the bounded-support/order-disagreement/reversal interfaces developed in Articles III--V. Together with [[four_of_six_equality_endpoints_force_local_order_disagreement]], the entire four-endpoint hard rooted-five-component dichotomy feeds existing disturbance machinery: the threefold-core branch gives a bounded support, disagreement, or reversal, while the equality branch gives disagreement directly.

Thus the unresolved five-component endpoint handoff has been reduced one level further. No new unbounded endpoint configuration survives the four-endpoint analysis; what remains is to convert these bounded disturbances into the protected outward-carrier conclusion or into a two-cover.

## Frontier

- Development version when composed: None
- Development version now: 1
