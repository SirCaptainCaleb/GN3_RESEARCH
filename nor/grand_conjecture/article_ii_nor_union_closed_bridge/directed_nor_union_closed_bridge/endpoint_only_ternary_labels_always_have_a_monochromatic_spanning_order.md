# Endpoint-only ternary labels always have a monochromatic spanning order

## Composition

(none yet)

## Development

Adversarial pruning lemma for ternary NOR. Suppose h(a,b,c)=T(a,c), where T is any tournament on V, with T(c,a)=1-T(a,c). Then h always has a monochromatic spanning order. Partition V arbitrarily into A and B with sizes differing by at most one. By the tournament Hamilton-path theorem, choose directed Hamilton paths a1,...,ar in T[A] and b1,...,bs in T[B], oriented so T(ai,ai+1)=0 and T(bj,bj+1)=0 after fixing the bit convention. Interleave a1,b1,a2,b2,... (ending with the extra A vertex if needed). Every ternary window compares vertices two positions apart, hence lies entirely within one of the two directed paths and has color 0. Thus endpoint-only reversal-odd labels cannot be counterexamples. Any false ternary NOR example must depend essentially on the middle coordinate, equivalently on the triangle defect field in the orientation-plus-defect decomposition.
