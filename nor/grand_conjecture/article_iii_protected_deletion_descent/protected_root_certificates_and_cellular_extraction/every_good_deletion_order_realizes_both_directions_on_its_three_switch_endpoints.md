# Every good deletion order realizes both directions on its three switch endpoints

## Composition

(none yet)

## Development

## Every good deletion order realizes both directions on its three switch endpoints

Assume a minimum counterexample and fix x. Let O_x=(a_1,...,a_{n-1}) be a NOR-good deletion order of V without x, with normalized word 0^p 1^q. Let its unique switch use (a_p,a_{p+1},a_{p+2},a_{p+3}), and put l=a_p and r=a_{p+3}.

By §285:
- x O_x has outermost root x -> r;
- O_x x has outermost root l -> x;
- the deletion switch has physical root l -> r.

Now reverse O_x. Reversal preserves goodness and reverses the switch-support quadruple, so its switch endpoints are r and l.

Applying §285 to O_x reversed gives:
- x O_x^rev has outermost root x -> l;
- O_x^rev x has outermost root r -> x;
- the reversed deletion switch has physical root r -> l.

Therefore the same good deletion order and its reversal realize both directions between every pair of the three coordinates x,l,r:

x <-> l,
x <-> r,
l <-> r.

The four roots incident with x are outermost roots of singleton or co-singleton facet witnesses. The two l-r roots are the deletion-switch root and its reversal. All six have explicit witness provenance.

Consequently the singleton-facet cycle of §283 carries much more local structure than a bare root cycle: every edge x -> r(x) belongs to a three-coordinate two-way root cell completed by l(x).

The unresolved issue is therefore order-level compatibility between consecutive such cells, rather than existence of physical root cancellation.
