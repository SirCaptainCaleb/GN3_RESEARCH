# Every singleton source reaches the global offending-size threshold

**Workspace:** D17
**State:** established
**Key:** `subminimum-source-saturation`

**Summary:** If a universal crossing exists and a is its globally minimum offending-rail size, every exact singleton cover has a rail of size at least a. Otherwise localized R927 exchanges saturate both size layers; unequal sizes close H, while equal sizes force every singleton cover to have both rails of size r<a, contradicting the definition of a. The balanced-case exclusion is new unreviewed exposition.


### Statement
Let H be a hypothetical smallest counterexample and assume at least one universal singleton-source crossing exists. Let

  a = minimum offending-rail size

over all literal singleton-deletion sources and all universally crossing vertices on either rail.

Suppose there is an exact singleton source

  C_x = A | B

of H-x with

  r=|A|<a,   s=|B|<a.

Such a source is impossible. The exchange argument first forces r=s and the uniform middle-layer residue; the balanced case then contradicts the assumed existence of a universal crossing with global minimum offending size a. Consequently EVERY exact singleton source has maximum rail size at least a.

### Localizing the accepted R927 exchange proof
The proof is the accepted P999/R927 argument with its global-quiet hypothesis replaced by the numerical threshold.

Fix any exact singleton source whose rail sizes are r,s. No vertex on either rail can be universally crossing relative to that source: such a vertex would exhibit an offending rail of size r or s, both strictly below a. Therefore every deleted-label substitution required in P999 is quiet.

For a in A and b in B, perform the same three literal substitutions as P999:

  H-a : (A-a+x) | B,
  H-b : (A-a+x) | (B-b+a),
  H-x : (A-a+b) | (B-b+a).

Every intermediate source still has rail sizes r,s, so the threshold argument applies again. Thus any one-for-one exchange across the two support classes is realizable. Connectivity of the Johnson graph saturates every r|s support partition of H-x.

Exactly as in P999, one quiet substitution produces an r|s source at every other deletion label y; repeating the exchange saturation there realizes every r|s partition of H-y. Hence every r-set and every s-set of H is Hamiltonian.

### Unequal sizes close H
If r<s, choose any Hamilton s-set and one actual Hamilton order on it. Since s>=r+1, take a contiguous tight subpath on r+1 vertices. Its complement has

  (r+s+1)-(r+1)=s

vertices and is Hamiltonian by the preceding saturation. These two disjoint Hamilton paths span H, contradiction. The case s<r is dual. Hence r=s.

Now |H|=2r+1 and every r-set is Hamiltonian. No (r+1)-set is Hamiltonian, because its r-vertex complement is Hamiltonian and the two paths would two-cover H. This is exactly the uniform middle-layer residue.

### The balanced case also contradicts the threshold
In the remaining case r=s, no tight path has more than r vertices: any longer path contains a contiguous Hamilton (r+1)-set, which the previous paragraph excludes. Every singleton-deletion exact two-cover spans 2r vertices with two paths, so BOTH rails in EVERY such cover have size r. In particular, the universal crossing whose existence defines a occurs on a rail of size r. This forces a=r, contrary to r<a.

Thus no singleton source can have both rails smaller than a. The earlier suggestion that universal crossings might survive elsewhere in the balanced outcome is withdrawn; the uniform path-length bound excludes it.

### Status and use
The saturation argument is complete internal exposition from accepted R927/P999 and smallest-counterexample noncoverability. The final balanced-case exclusion is a new unreviewed deduction; this section has no exact-unit certification. In the three-petal regime a=2k, it suffices to construct ANY exact singleton cover with both rails below 2k, allowing arbitrary reordering and simultaneous multi-vertex redistribution. Neither unequal sizes nor adjacency to the historical cover is required.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```
