# An explicit coherent alternating triangle orientation on eight coordinates has no monochromatic spanning path

# An eight-coordinate coherent triangle orientation with no monochromatic full geodesic

A coordinate-only NORI coloring h of ordered distinct coordinate triples is called *coherent* when h(b,c,a)=h(a,b,c) for every triple. Thus each unordered triangle receives an alternating orientation, and the defect-vertex field in Toolkit ternary_nor_decomposes_into_triangle_orientation_and_defect_vertex vanishes identically. Reversal oddness h(c,b,a)=1−h(a,b,c) holds automatically.

**THEOREM (explicit coherent obstruction in Q8).** There exists a coherent reversal-odd coordinate-only ordered-three-face coloring of Q8 for which EVERY full eight-edge antipodal geodesic has at least one color change. Thus a grand proof cannot begin by asserting that every coherent simplex-triangle orientation has a fully monochromatic Hamilton tight path. The constructed coloring still has exactly 2688 good full direction orders, at every cube root, and therefore is compatible with the one-switch NORI conjecture.

**Explicit 56-bit specification.** Let V={0,1,...,7}, enumerate its 56 unordered three-subsets T in lexicographic order (itertools.combinations(range(8),3)), indexed j=0,...,55. Set B_T to bit j of the integer
    M = 0x73adc517913474.
For any ordered distinct triple (a,b,c), let inv(a,b,c) be the parity of its three pairwise inversions and set
    h(a,b,c)=B_{sort(a,b,c)}+inv(a,b,c)   (mod 2).
Color every physical ordered three-face with free order (a,b,c) by h(a,b,c), independently of all exterior bits.

Cyclic permutations have even parity and preserve h; reversal has odd parity and complements h, so this is a genuine NORI coloring with fully coherent orientation on every coordinate triangle.

**Exhaustive, independently checkable proof certificate.** The following short Python checker exhausts all 8!=40320 genuine full antipodal direction orders, checks the orientation laws on all 336 ordered triples, and counts changes between consecutive ordered-three-face colors:

```python
from itertools import combinations, permutations
from collections import Counter

V=range(8)
M=int('73adc517913474',16)
ind={t:j for j,t in enumerate(combinations(V,3))}
def h(a,b,c):
    inv=(a>b)+(a>c)+(b>c)
    return ((M >> ind[tuple(sorted((a,b,c)))]) & 1) ^ (inv%2)

for a,b,c in permutations(V,3):
    assert h(a,b,c) == h(b,c,a)
    assert h(a,b,c) != h(c,b,a)

hist=Counter()
for p in permutations(V):
    w=[h(*p[i:i+3]) for i in range(6)]
    hist[sum(w[i]!=w[i+1] for i in range(5))]+=1
assert dict(sorted(hist.items())) == {
    1:2688, 2:10080, 3:14784, 4:10080, 5:2688
}
```

This directly verifies absence of any zero-switch spanning geodesic and the exact one-switch count. The verifier is deterministic and uses no SAT inference.

**Research implication.** The alternating triangle orientation itself, even with no distinguished defect vertex, can force a change in every spanning coordinate order. The actual grand target is therefore an orientation-and-defect selection theorem producing at most one change. It cannot be reduced to a universal monochromatic coherent-triangle path theorem. The example also distinguishes good full geodesics from monochromatic facet expectations.
