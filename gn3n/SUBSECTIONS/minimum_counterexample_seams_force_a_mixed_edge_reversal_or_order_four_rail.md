# Minimum-counterexample seams force a mixed edge or positioned reversal

## Metadata

- ID: minimum_counterexample_seams_force_a_mixed_edge_reversal_or_order_four_rail
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 190
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let H be a minimum-order counterexample. Let S be a globally maximal Hamiltonian support and write
H-S=P|Q,
with P=(p_1,...,p_m), Q=(q_1,...,q_t).

Assume first m,t>=3.

Consider the oriented seam P->Q and put G=H-S.

If G-p_m or G-q_1 is Hamiltonian, the corresponding deletion cover
H-v = S | (G-v)
contains a Hamilton path on G-v meeting both nonempty inherited support classes from P and Q. Therefore that path has an ordinary edge joining the two classes: a direct mixed-edge comparison disturbance.

Assume both endpoint deletions are non-Hamiltonian. The audited second-layer seam theorem gives either:

1. a transversal Hamiltonian four-support, whose construction already contains a positioned external end-edge reversal; or

2. the pure rail four-support
K={p_{m-1},p_m,q_1,q_2}.

In case 2, minimum-counterexample minimality gives pc(H-K)=2. Deleting K leaves the two nonempty inherited residual rail intervals
C_P=(p_1,...,p_{m-2}),
C_Q=(q_3,...,q_t),
together with S.

By [[every_seam_reseed_is_support_preserving_or_exposes_a_cross_residual_reversal]], either a cross-residual positioned reversal occurs, or
H-K=S|R
where R is a Hamiltonian concatenation of C_P and C_Q.

In the latter case R necessarily contains an ordinary path edge with one endpoint in C_P and the other in C_Q, because both intervals are nonempty. Thus this is again a direct mixed edge between the original complementary supports P and Q.

Therefore, whenever m,t>=3:

> every oriented seam of a globally maximal-support state in a minimum counterexample yields either a direct mixed edge joining the two complementary support classes in a deletion/comparison cover, or a positioned external end-edge reversal.

The Q->P seam is symmetric.

If one complementary path has order two, the pure seam can consume that path completely; this remains a bounded short-rail interface and is the only exception to the displayed dichotomy.

This replaces development version 1: the former order-four-rail branch is absorbed into the direct mixed-edge disturbance whenever both residual intervals are nonempty.

## Frontier

- Development version when composed: None
- Development version now: 2
