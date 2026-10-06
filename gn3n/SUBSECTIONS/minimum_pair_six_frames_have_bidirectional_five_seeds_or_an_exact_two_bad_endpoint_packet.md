# Minimum-pair six-frames have bidirectional five-seeds or an exact two-bad endpoint packet

## Metadata

- ID: minimum_pair_six_frames_have_bidirectional_five_seeds_or_an_exact_two_bad_endpoint_packet
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 176
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Endpoint-deletion dichotomy in the minimum-pair six-frame

Let
[
X={x,y},qquad H-X=Pmid Q,
]
with
[
P=(p_1,ldots,p_m),qquad Q=(q_1,ldots,q_t),
qquad m,tge2.
]
Put
[
U={x,y,p_1,p_m,q_1,q_t}.
]

Call an exposed endpoint (e) **good** if
[
U-{e}
]
is Hamiltonian.

By the four-of-six theorem at least four one-vertex deletions of (U) are Hamiltonian. Since only two deletion labels are the holes (x,y), at least two exposed endpoints are good.

Exactly one of the following holds.

### 1. Bidirectional endpoint goodness

There is a good endpoint of (P) and a good endpoint of (Q).

Then there are Hamiltonian five-supports of both truncation types:
- for good (ein{p_1,p_m}), the support (U-{e}) has inherited complementary path orders
  [
  (m-1)mid(t-2);
  ]
- for good (fin{q_1,q_t}), the support (U-{f}) has inherited complementary path orders
  [
  (m-2)mid(t-1).
  ]

Both supports contain the entire minimum pair.

### 2. Exact two-bad endpoint packet

All good exposed endpoints lie on one complementary path. Since at least two are good and a path has only two exposed endpoints, both endpoints of that path are good and both endpoints of the other path are bad.

Moreover the four-of-six lower bound then forces both hole deletions
[
U-{x},qquad U-{y}
]
to be Hamiltonian. Thus the six-frame has exactly four certified good deletions and the two bad endpoint deletions are the opposite path's two endpoints.

Therefore:

> **Minimum-pair six-frame dichotomy.** The six labels formed by the minimum pair and the four exposed endpoints either provide hole-preserving five-supports truncating from both sides, or form an exact two-bad endpoint packet in which the two holes and the two opposite-path endpoints are the four good deletion labels.

If (m=t+1), a good endpoint of the shorter path produces a five-support whose inherited complement is balanced:
[
(m-2)mid(t-1)=(t-1)mid(t-1).
]
Hence in the adjacent-simple-root size profile, failure to reach a balanced complementary cover through this five-seed forces the exact two-bad endpoint packet above.

No path reversal, cyclic rotation, minimum-counterexample hypothesis, or computation is used.
