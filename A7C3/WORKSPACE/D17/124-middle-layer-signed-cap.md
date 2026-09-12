# Uniform signed-cap lemma consumes large outer/outer families

**Workspace:** D17
**State:** established
**Key:** `middle-layer-signed-cap`

**Summary:** In the uniform middle-layer residue, let O be the exterior labels admitting both literal OUT endpoint replacements relative to one Hamilton order P. For every ordered distinct x,y in O, nonextension forces (p_1,x,y) and (x,y,p_{k-2}) tight. More generally, if fixed h,t satisfy (h,x,y),(x,y,t) for every ordered pair in O, then any Hamilton path on U+h with |U|>=3 places h first or second and therefore extends by t. Uniformity on a (k-1)-subset U of O yields a forbidden P_{k+1}, so |O|<=k-2.


### Abstract signed-cap lemma

Let H be an exact-reversal tight-turn system. Let h,t be distinct vertices outside a set O, and assume

  (h,x,y) and (x,y,t)

are tight for every ordered pair of distinct x,y in O.

Let U be a subset of O with |U|>=3, and let W be any Hamilton tight path on {h} union U. Then h is one of the first two vertices of W. Indeed, if h occurred later, its two immediate predecessors u,v would lie in U and W would certify (u,v,h) tight. But the hypothesis applied to the ordered pair (v,u) certifies (h,v,u) tight, which is the complete reversal of (u,v,h), contradicting exact reversal.

Since |W|>=4 and h is first or second, the final two vertices x,y of W both lie in U. The hypothesis gives (x,y,t) tight. Appending t therefore creates only this one new consecutive turn and yields a Hamilton tight path on {h,t} union U.

No Hamilton path on U itself is assumed or used.

### Uniform middle-layer application

Assume the surviving uniform residue has |V(H)|=2k+1 with k>=6, every k-set Hamiltonian, and no (k+1)-set Hamiltonian. Fix a literal Hamilton order

  P=(p_0,p_1,...,p_{k-1})

and let O consist of exterior labels x for which both literal OUT endpoint replacements are actual Hamilton paths:

  EL(x)=(x,p_1,p_2,...,p_{k-1}),
  ER(x)=(p_0,...,p_{k-2},x).

Put h=p_1 and t=p_{k-2}; these are distinct because k>=6.

For distinct x,y in O, prepend y to EL(x). Every inherited turn remains tight. If (y,x,p_1) were tight, this would be a tight path on k+1 vertices, forbidden in the uniform residue. Thus (y,x,p_1) is bad, and exact reversal gives

  (p_1,x,y) tight.

Likewise append x to ER(y). The forbidden (k+1)-path forces (p_{k-2},y,x) bad, hence

  (x,y,p_{k-2}) tight.

These hold for every ordered distinct x,y in O, so the abstract signed-cap lemma applies with h=p_1 and t=p_{k-2}.

If |O|>=k-1, choose any U subset O with |U|=k-1. The k-set U union {h} is Hamiltonian by uniformity. Apply the signed-cap lemma to one Hamilton path W on this support. It extends by t to a tight path on k+1 vertices, contradiction. Equivalently its k-vertex complement is Hamiltonian and the extension would also provide an explicit spanning two-cover.

Therefore every surviving uniform residue satisfies

  |O| <= k-2.

### Scope and limitation

This consumes only the large outer/outer subbranch. It does not prove that O is large, eliminate two-label outer nuclei, consume the synchronized K4-e residue, or turn the support-wide active R435 family into a cover. It does not infer Hamiltonicity of arbitrary (k-1)-sets. The input OUT orders must be actual literal Hamilton paths; no path reversal or representative synchronization is implicit.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R927"
    },
    {
        "relation": "conditional_dependency",
        "revision_id": "R966"
    }
]
```
