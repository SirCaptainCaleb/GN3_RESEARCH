# Audit: strong-imbalance Hall descent still lacks transfer-direction control — preserved pre-item development

## Composition

(none yet)

## Development

## Audit correction

This proposed repair depended on the now-withdrawn assertion that an isolated Hall block forces opposite transfer polarities.

The quadratic calculation remains correct **conditional on direction**: moving one endpoint from a component of order \(c\) to a component of order \(d\) changes
\[
\Phi
\]
by
\[
2(d-c+1),
\]
so an outward move from a component at least two larger is a strict decrease.

However, the Hall obstruction alone does not currently force the transfer to leave the dominant component when both receiving components are nontrivial. Therefore this subsection does not prove strong-imbalance descent. See [[audit_same_hall_transfer_polarity_is_not_excluded_by_boundary_antisymmetry]] and the corrected current version of [[hall_endpoint_transfers_give_terminating_quadratic_descent_from_strongly_imbalanced_three_covers]].
