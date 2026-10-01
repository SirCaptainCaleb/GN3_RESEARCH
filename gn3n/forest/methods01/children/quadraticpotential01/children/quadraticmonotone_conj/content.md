# Quadratic-monotone three-cover reconfiguration

## Statement

For every finite boundary tournament H and every spanning three-cover C, there is a finite sequence of legal pairwise repartitions from C to a cover with at most two components such that, while three components remain, the quadratic component-size potential Phi=sum |P_i|^2 never increases. Equivalently, every connected component of the three-cover pairwise-repartition graph that contains no two-cover would have to contain a Phi-minimal plateau with no strict descent and no equal-Phi route to a merge; the conjecture asserts that no such trapped plateau exists.

## Body

This is a potential-level strengthening of ordinary three-cover no-trapping.

The point is not that every legal move must decrease Phi. Certified examples already show equal-Phi rotations and transports. The assertion is instead that an increase of Phi is never necessary on some route to a merge.

A proof can therefore split naturally into two layers:

1. STRICT DESCENT. Outside a structurally narrow plateau, find a legal pairwise repartition decreasing Phi.

2. PLATEAU TRANSPORT. At a Phi-minimal state, use equal-Phi moves and secondary support/order information until either a merge appears or a new strict descent becomes available.

The existing quadratic toolkit already supplies the well-foundedness and extremal normalization. Known route-specific results prove strict descent in several profiles and identify obstruction structure when descent fails. What remains is a general plateau theorem.

This conjecture is deliberately higher-level than any one Astra line: it can be attacked using pairwise repartition, balanced-cover improvement, endpoint transport, defect compression, or other move systems that realize legal pairwise repartitions.