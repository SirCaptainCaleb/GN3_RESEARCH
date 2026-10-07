# Audit minimum middle run needs a rooted extremality lemma

## Metadata

- ID: audit_minimum_middle_run_needs_a_rooted_extremality_lemma
- Parent Section: directed_nor_union_closed_bridge
- Position: 50
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The minimum-middle-run shortcut is not valid without an additional rooted-extremality lemma. Minimum counterexample deletion yields rooted two-change sandwiches, but a globally minimum-middle two-change order need not have a singleton outer run, while minimizing only among rooted sandwiches does not survive the first swap. Therefore the claimed exclusion of the repeated outer-color case and the resulting dichotomy cannot be used until rooted extremality is proved.

## Development

The subsection claiming that a minimum-middle-run spanning two-change order may be written in prepended-deletion form has a gap. Minimum counterexample deletion plus endpoint blocking guarantees the existence of rooted sandwiches of the form tau,sigma^p,tau^q with singleton first run, but does not show that a globally minimum middle-run two-change order has a singleton outer run. Conversely, if p is minimized only among rooted sandwiches, swapping the first two coordinates and obtaining tau^2 sigma^(p-1) tau^q does not contradict that rooted minimality because the new order is not rooted by a one-change deletion order in the same evident way. Therefore the exclusions of the (tau,tau) case and the resulting two-circuit-or-crossed-pattern dichotomy require an additional rooted-extremality lemma. The p=1 shifted-two-circuit theorem remains valid because it uses only counterexamplehood, not this extremality step. A correct continuation should either prove that some global minimum-middle two-change order has a singleton outer run, or use the middle-run reversal blockers for the case where both outer runs have length at least two.
