# Adjacent-simple-root six-frames give balance, a six-seed, or local disturbance

## Composition

(none yet)

## Development

## Adjacent-simple-root minimum pairs have a sharp six-frame trichotomy

Let
[
X={x,y},qquad H-X=Pmid Q,
]
with
[
|P|=|Q|+1,
]
and write
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t),
qquad m=t+1.
]
Put
[
U={x,y,p_1,p_m,q_1,q_t}.
]

Then one of the following holds.

### 1. Balanced hole-preserving five-seed

At least one endpoint
[
qin{q_1,q_t}
]
is a good deletion of (U), so
[
U-{q}
]
is Hamiltonian.

Its complement is covered by the inherited intervals of orders
[
m-2=t-1,
qquad
t-1.
]
Thus the complementary two-cover is exactly balanced.

### 2. Hole-preserving Hamiltonian six-seed

Neither (q_1) nor (q_t) is a good deletion, but (U) itself is Hamiltonian.

Then (U) is a Hamiltonian six-support containing both holes, and
[
H-U
]
is covered by the two inherited interiors
[
P-{p_1,p_m},
qquad
Q-{q_1,q_t}.
]

### 3. Exact equality disturbance

Neither (q_1) nor (q_t) is a good deletion and (U) is non-Hamiltonian.

By [[minimum_pair_six_frames_have_bidirectional_five_seeds_or_an_exact_two_bad_endpoint_packet]], the other four deletion labels
[
p_1, p_m, x, y
]
are all good. Hence (U) is a non-Hamiltonian six-set with exactly four Hamiltonian five-deletions.

The four-good-deletion disagreement theorem used in [[four_of_six_equality_endpoints_force_local_order_disagreement]] gives Hamilton-order disagreement between two good deletion states. By [[bounded_order_disagreement_reduces_to_reversal_or_hamiltonian_support]], this yields either a positioned reversing tight triple or a Hamiltonian support contained in (U).

Therefore:

> **Adjacent-simple-root six-frame trichotomy.** A near-balanced minimum-pair state with component orders differing by one either rebases through a balanced hole-preserving five-seed, enters maximal-support theory through a hole-preserving six-seed with inherited two-coverable complement, or already carries a bounded local reversal/Hamiltonian disturbance on the six-frame.

In particular the adjacent-simple-root size profile has no featureless residual state at the exposed-endpoint level.

No cyclic rotation, path reversal, minimum-counterexample hypothesis, or finite computation is used.
