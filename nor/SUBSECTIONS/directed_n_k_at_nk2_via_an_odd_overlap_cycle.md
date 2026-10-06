# Directed N_k at n=k+2 via an odd overlap cycle

## Metadata

- ID: directed_n_k_at_nk2_via_an_odd_overlap_cycle
- Parent Section: higher_memory_norine_geodesics
- Position: 9
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


## Theorem

For every (kge 2), the directed tuple conjecture (N_k) holds when (n=k+2). In fact, reversal antisymmetry is unnecessary: every binary coloring of the injective ordered (k)-tuples of a ((k+2))-element set admits a permutation whose three sliding-window colors change at most once.

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
are overlapping injective (k)-tuples, their colors differ. Indeed the (k+1) displayed coordinates are distinct, and the unique remaining coordinate extends them to a permutation of all (k+2) elements, where these are the first two windows.

Consider the overlap graph (Gamma_k) on injective ordered (k)-tuples, joining two tuples when one is obtained from the other by deleting the first coordinate and appending a new coordinate.

Choose (k+1) distinct coordinates in a cyclic order. Their cyclic consecutive length-(k) windows form a cycle of length (k+1) in (Gamma_k). Using all (k+2) coordinates cyclically likewise gives a cycle of length (k+2).

Our assumption forces the binary color to flip across every edge of both cycles. But (k+1) and (k+2) have opposite parity, so one of these cycles is odd, and no binary coloring can flip across every edge of an odd cycle. Contradiction.

Thus some permutation has at most one color change. (square)

### Audit

The proof uses only:
1. (n=k+2), so the window word has length three;
2. failure of the target, which forces both adjacent window pairs to disagree; and
3. the existence of the two cyclic overlap cycles.

It does not use reversal antisymmetry and therefore proves a strictly stronger first-nontrivial-dimension statement for directed NOR. The argument does not automatically extend to (nge k+3), because a bad longer word need not alternate at every adjacent pair.
