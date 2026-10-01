# Repeated-label neutral cycles should force a canonical transport disturbance

## Statement

Let H be a minimum counterexample and let K be a Phi-minimal nonuniform equitable plateau in the pairwise-repartition graph. Suppose K contains a simple neutral-transfer cycle as in 8ca61ff768f5. Conjecture that the cycle exposes at least one canonical endpoint-transport / defect-compression input: relative-order disagreement between two overlapping displayed paths, an inherited displayed edge whose endpoints are separated by a comparison cover, a reversing tight triple through an inherited edge, a reversed displayed end-edge, or a bounded Hamiltonian four- or five-vertex support with path-cover-two complement. In particular a repeated-label neutral cycle cannot be completely transport-neutral.

## Body

Suggested first attack. Choose a transferred label v and two consecutive cycle edges carrying v. Between them v remains present in the evolving path supports and at the second occurrence is again a displayed endpoint. Locate the first intermediate state at which v becomes a displayed endpoint. If that exposure occurs by deleting the neighboring endpoint of its current inherited order, retain the adjacent inherited edge and compare the before/after pairwise repartition. If it occurs because the recipient path is replaced by a new Hamilton order having v at an end, compare that new order with the previous inherited order; try to invoke path-intersection/order-disagreement machinery unless the surviving old block is intact. In the intact-block branch, follow the common-middle/radius-two support-migration calculus. The aim is to show that a shortest repeated-label neutral cycle cannot return without producing one of the canonical disturbance witnesses.
