# A common-tail deletion cycle cannot end in a singleton final run

## Metadata

- ID: a_common_tail_deletion_cycle_cannot_end_in_a_singleton_final_run
- Parent Section: higher_memory_norine_geodesics
- Position: 43
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Singleton final run is impossible

Work in the directed ternary sector. Suppose a reversal-antisymmetric coloring on the full ambient set V has no spanning one-change order.

Let T=(t_1,...,t_m) have word sigma^p(1-sigma), p>=1, and let V\V(T)={a,b,c}. Assume
(a,b,T), (b,c,T), (c,a,T)
are all one-change deletion orders.

Put w=t_m and eta=h(w,b,c).

Counterexamplehood on the full ambient set gives
h(a,t_1,t_2)=sigma,
h(c,a,t_1)=sigma,
h(b,c,a)=1-sigma,
and
h(t_{m-1},w,b)=sigma,
the last identity by appending b to the full deletion order (c,a,T).

Consider the cyclic order
C=(a,T,b,c).
Its cyclic ternary color list is
sigma^{p+1}, (1-sigma), sigma, eta, (1-sigma), sigma.

If eta=1-sigma, cut the cycle so that the two consecutive statuses immediately after the initial sigma-run are omitted. The resulting full linear order is
(w,b,c,a,t_1,...,t_{m-1})
and has word
(1-sigma)^2 sigma^{p+2},
hence one change. Contradiction.

Therefore eta=sigma. Cyclically,
h(w,a,b)=h(w,b,c)=h(w,c,a)=sigma.

Now
D=(w,a,b,t_1,...,t_{m-1})
is sigma-tight: the first three windows have color sigma and all remaining windows are tail windows before the unique final (1-sigma)-window.

D omits only c. Prepending c adds a single first color to a constant sigma word, so the resulting spanning order changes at most once. Contradiction.

Hence a common-tail deletion 3-cycle in a counterexample must have final run length at least two.

This proof uses only permutations of the full ambient set; no tail truncation or minimum-size inheritance is used.

## Frontier

- Development version when composed: None
- Development version now: 2
