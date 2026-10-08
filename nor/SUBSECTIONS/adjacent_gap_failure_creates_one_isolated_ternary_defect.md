# Adjacent-gap failure creates one isolated ternary defect

## Metadata

- ID: adjacent_gap_failure_creates_one_isolated_ternary_defect
- Parent Section: hartman_least_unreachable_connectors
- Position: 10
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The bad adjacent-gap interleaving has exactly one nonzero internal triple, a directed triangle, while the other new windows remain zero. Its elimination must preserve the outside zero tails and both endpoint ports. An unrestricted good local order does not establish this relative repair.

## Development

In path-normalized gauge, let a and b be individually insertable at adjacent gaps with the bad mutual orientation. Insert both in the natural interleaving. All new windows are zero except the middle triple consisting of a, the shared connector vertex, and b; that triple is a directed triangle and has color one. Hence the enlarged order differs from a compatible zero connector by exactly one isolated ternary one. The remaining rank-two union-closure problem is therefore a relative singleton-elimination theorem that preserves the outside zero tails and the two connector endpoint ports.
