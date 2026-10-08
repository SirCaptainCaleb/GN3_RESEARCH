# Translation-invariant N_{r+1} at n=r+2 via an odd overlap cycle — preserved pre-item development


## Theorem

For every (rge 2), the directed tuple conjecture (N_k) holds when (n=r+2). In fact, reversal antisymmetry is unnecessary: every binary coloring of the injective ordered (r)-tuples of a ((r+2))-element set admits a permutation whose three sliding-window colors change at most once.

### Proof

Assume the contrary. Every permutation has a three-bit window word with more than one change, hence every such word is alternating:
[
010quad	ext{or}quad101.
]
Therefore, whenever
[
(x_1,ldots,x_k)
quad	ext{and}quad
(x_2,ldots,x_k,y)
]
are overlapping injective (r)-tuples, their colors differ. Indeed the (r+1) displayed coordinates are distinct, and the unique remaining coordinate extends them to a permutation of all (r+2) elements, where these are the first two windows.

Consider the overlap graph (Gamma_k) on injective ordered (r)-tuples, joining two tuples when one is obtained from the other by deleting the first coordinate and appending a new coordinate.

Choose (r+1) distinct coordinates in a cyclic order. Their cyclic consecutive length-(r) windows form a cycle of length (r+1) in (Gamma_k). Using all (r+2) coordinates cyclically likewise gives a cycle of length (r+2).

Our assumption forces the binary color to flip across every edge of both cycles. But (r+1) and (r+2) have opposite parity, so one of these cycles is odd, and no binary coloring can flip across every edge of an odd cycle. Contradiction.

Thus some permutation has at most one color change. (square)

### Audit

The proof uses only:
1. (n=r+2), so the window word has length three;
2. failure of the target, which forces both adjacent window pairs to disagree; and
3. the existence of the two cyclic overlap cycles.

It does not use reversal antisymmetry and therefore proves a strictly stronger first-nontrivial-dimension statement for directed NOR. The argument does not automatically extend to (nge r+3), because a bad longer word need not alternate at every adjacent pair.
