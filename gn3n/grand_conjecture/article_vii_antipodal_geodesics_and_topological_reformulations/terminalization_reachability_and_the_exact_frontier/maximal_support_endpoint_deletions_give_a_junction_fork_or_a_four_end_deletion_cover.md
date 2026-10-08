# Maximal-support endpoint deletions give a junction fork or a four-end deletion cover

## Composition

(none yet)

## Development

Let H be a minimum-order counterexample. Let S be a globally maximal proper Hamiltonian support and fix H-S=P|Q, with P=(p_1,...,p_m), Q=(q_1,...,q_t).

Let v be any exposed endpoint of P or Q and put G=H-S.

Exactly one of the following holds.

1. G-v is non-Hamiltonian. Since deleting the displayed endpoint v leaves a two-cover by inherited path intervals, the failed concatenation of those two intervals gives the corresponding audited second-layer junction fork by literal boundary reversal.

2. G-v is Hamiltonian. Then
   H-v = S | (G-v)
is a deletion cover of the minimum counterexample. The standard four-end deletion-cover theorem applies to the omitted vertex v: relative to displayed Hamilton orders on S and G-v, v reverses both exposed end edges of both paths.

Thus every exposed endpoint deletion of a maximal-support complement produces structured reversal data: either a second-layer rail fork or a full four-end deletion-cover reversal pattern.

In particular, the deletion-critical seam analysis is the non-Hamiltonian half of a more general minimum-counterexample endpoint dichotomy; the complementary Hamiltonian half is not featureless and enters the one-hole/four-end-reversal interface instead.

No cyclic rotation or path reversal is used.
