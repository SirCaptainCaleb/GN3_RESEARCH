# Odd Q7 coloring lacks every monochromatic six-direction facet but has three cyclic witnesses

**Theorem.** There is a coordinate-only reversal-odd ordered-three-face coloring of Q_7 with no monochromatic six-direction geodesic in any coordinate facet. It nevertheless admits a full one-change geodesic. Thus the six-direction monochromatic-five-facet theorem cannot be extended by requiring a monochromatic (n-1)-facet in every dimension.

**Exact construction.** Let V={0,1,2,3,4,5,6}. List the ordered triples (a,b,c) with a<c in lexicographic order, starting at index 0. There are 105 such triples. Let
M=0x1ace4c51f1eca17f4237e025d13.
For a<c, define h(a,b,c) to be bit i of M, where i is that triple's index. For a>c, put h(a,b,c)=1-h(c,b,a). Color each ordered face by h of its direction order, independently of its exterior bits. Reversal oddness follows immediately from the definition.

**Verification certificate.** The following complete finite enumeration reproduces the color-change counts. Its indexing convention fully specifies the example.

    from itertools import permutations
    from collections import Counter
    V = range(7)
    reps = [t for t in permutations(V,3) if t[0] < t[2]]
    index = {t:i for i,t in enumerate(reps)}
    M = int("1ace4c51f1eca17f4237e025d13",16)
    def h(t):
        if t[0] < t[2]:
            return (M >> index[t]) & 1
        return 1 - ((M >> index[t[::-1]]) & 1)
    for k in (5,6,7):
        counts = Counter()
        for p in permutations(V,k):
            w = [h(p[i:i+3]) for i in range(k-2)]
            counts[sum(x != y for x,y in zip(w,w[1:]))] += 1
        print(k, dict(sorted(counts.items())))

The exact output is:

| directions traversed | zero changes | one change | two changes | three changes | four changes |
|---|---:|---:|---:|---:|---:|
| 5 | 100 | 1168 | 1252 | 0 | 0 |
| 6 | 0 | 792 | 2520 | 1728 | 0 |
| 7 | 0 | 144 | 1332 | 2376 | 1188 |

Because colors ignore exterior bits, the zero in the six-direction row excludes every monochromatic six-direction path at every starting cube vertex. The example is a finite exact counterexample to the monochromatic-facet strengthening; the full one-change statement holds.

**Compatibility mechanism.** The cyclic direction order
(0,1,2,5,3,4,6)
has circular triple word 1101001. Three of its six-direction facet deletions are good:
(3,4,6,0,1,2), with word 0011;
(4,6,0,1,2,5), with word 0111;
(6,0,1,2,5,3), with word 1110.
The three-cyclic-facet theorem (Item nori_three_cyclic_facet_witnesses_dimension_independent_20261008) therefore applies. Explicitly, the full rotation
(3,4,6,0,1,2,5)
has word 00111.

**Research implication.** Retain one-change facet witnesses as the induction state. Their compatibility on a common cyclic direction order can force full closure even when every monochromatic facet is absent. This example supports the cyclic-witness target and identifies a strict limitation of demanding monochromatic facet transfer at every stage.
