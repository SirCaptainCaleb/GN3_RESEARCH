# Startup broadcasts

These persistent project directives remain in force until explicitly removed.

## Minimum-counterexample analysis is allowed

Project override: minimum-counterexample and minimum-order-counterexample arguments are allowed whenever they materially simplify, compress, or close the active proof branch. The previous bounded-order prerequisite is removed. Use minimality deliberately rather than reflexively: state what is minimized, verify any smaller object remains in the theorem class, and prefer minimality when it immediately kills a branch or turns hereditary descent into contradiction.

- ID: minimum_counterexample_allowed
- Scope: gn3n

## Bare bounded support is not a terminal outcome

Minimum-counterexample bookkeeping rule: do not treat the bare existence of a bounded Hamiltonian support K with pc(H-K)=2 as branch closure or substantive top-level progress. In a minimum-order counterexample every proper Hamiltonian support K automatically satisfies pc(H-K)=2; in particular every two-vertex set already has this property. A bounded 4/5/6-support is useful only when it retains additional structure needed downstream (specified endpoint/root, displayed edge, order disagreement, positioned reversal, split/leave-and-return incidence, protected seam, etc.). Statements of the form "either bounded support or X" may use the bounded branch as a handoff to a proved anchored conversion theorem, but may not simply discard it and infer X at the top level.

- ID: bounded_support_is_not_terminal_under_minimality
- Scope: gn3n

## Do not chase the small-order cutoff

Project methodological rule: minimum-counterexample arguments ARE allowed. What is banned is using minimum-counterexample reasoning merely to chase the current small-order verification cutoff. Do not present a branch as closed, substantially reduced, or at its true frontier just because minimality plus local moves imply |H|<=N, pc/combinatorial structure on orders <=N, or a finite list of orders immediately above the currently verified base range. Those thresholds are unstable: improving the verified small-order theorem merely moves the apparent frontier.

Use minimality for scale-independent structural consequences (for example: every proper induced subtournament satisfies the theorem; every proper Hamiltonian support has a two-coverable complement; hereditary descent is impossible in a minimum counterexample), and continue the argument structurally from those consequences.

A finite reduction is acceptable only when the bounded configuration is intrinsic to the mathematics of the branch—fixed local support, fixed-width interface, finite orientation type, etc.—rather than being bounded because it sits just beyond the present computational/small-order cutoff. Do not pivot to exhaustive small-order checking unless explicitly requested.

- ID: no_small_order_cutoff_chasing
- Scope: gn3n
