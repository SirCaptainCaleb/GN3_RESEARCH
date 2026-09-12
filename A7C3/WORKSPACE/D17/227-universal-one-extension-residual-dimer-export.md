# A dimer residual rail makes universal-extension endpoint surgery immediately nonterminal

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-residual-dimer-export`

**Summary:** Let S be a non-Hamilton universally one-extendable four-set and let Y=V(H)-S. If some exact residual cover is a dimer rail (r,s) plus a Hamilton rail V, accepted R157 at r and s gives exact singleton rows H-s=P_r|V and H-r=P_s|V, with r,s internal in the active Hamilton paths. Their active union A=S+r+s is non-Hamiltonian. Any R435-nonquiet comparison already exports: proper cycle gives the movable-break orbit, reverse trimer gives a fresh maximum forest by R4, and selected reversal lies in the INTERNAL branch of SV27136 because both exchanged labels are internal. If the comparison is quiet, SV26201 says the insertion slots are equal or adjacent. An adjacent-slot swap is itself a tight trimer on {r,s,u}; a same-gap one-sided fan also contains a tight trimer on {r,s,u} or {r,s,v}; pairing that trimer with a Hamilton trimer on the remaining three vertices of S and with V gives an actual spanning maximum three-forest. Opposite-side same-gap failures give a universal extension core. Hence the residual-dimer case is completely nonterminal; any surviving minimal-holonomy universal-extension configuration has residual rails of order at least three.

### 1. Non-Hamilton universal-extension setup with a residual dimer
Let H be a hypothetical smallest Strong Level-(1) counterexample. Let S be a non-Hamiltonian four-set and put

  Y=V(H)-S.

Assume every r in Y Hamilton-extends S. By accepted R156, pc(Y)=2 and every exact two-cover of Y has two nontrivial rails. Suppose one retained exact residual cover has a dimer rail

  Y=(r,s) | V,                                             (RD.1)

where V is a nonempty literal Hamilton path. The order of the dimer in (RD.1) is free because a two-vertex path has no turn constraint.

### 2. The two endpoint surgeries form a fixed-complement two-row cylinder
Apply accepted R157 at the two endpoints r,s of the dimer rail. Choose arbitrary Hamilton paths

  P_r on S+r,
  P_s on S+s.

Since S is non-Hamiltonian, R157 forces r internal in P_r and s internal in P_s. Moreover

  P_r | {s} | V,
  P_s | {r} | V                                           (RD.2)

are literal spanning minimum three-covers of H. Equivalently, deleting the singleton rails gives exact singleton-deletion covers

  H-s=P_r|V,
  H-r=P_s|V.                                               (RD.3)

Put

  A=S union {r,s}.

A is non-Hamiltonian: a Hamilton path on A together with V would be a spanning two-cover of H. Hence P_r and P_s are neighboring Hamilton puncture paths of the same non-Hamiltonian active support A, with common literal complement V. Both exchanged labels are internal in their own puncture paths.

### 3. Any nonquiet comparison already exports
Compare P_r and P_s by accepted R435.

If the comparison yields a proper tight cycle, the movable-break theorem SV25652 gives a closed family of actual maximum spanning three-forests.

If it yields a reverse trimer, that trimer is a proper graph-intrinsic tight path, so accepted R4 supplies an exact two-cover of its complement and hence an actual maximum spanning three-forest containing it.

If it yields an adjacent selected-state reversal, both exchanged labels r,s are internal by Section 2. Therefore the INTERNAL branch of SV27136 applies: after deleting r,s, an exact pair-deletion two-cover must cross the explicit three-cover trim, and the lifted dimer (r,s) together with that exact cover is an actual maximum spanning three-forest. In particular the selected reversal cannot recycle into the endpoint-endpoint fixed-complement residue.

Thus only the R435-quiet case remains.

### 4. Quiet adjacent-slot exchange is already a fresh trimer representative
Apply the quiet-neighbor normal form SV26201 to P_r,P_s on A. Their common S-vertices occur in one order K, and the insertion slots of r,s are equal or adjacent.

If the slots are adjacent across a common vertex u in S, SV26201 gives one of the tight swap trimers

  (s,u,r)  or  (r,u,s).                                   (RD.4)

The complementary three-set S-u always has a tight Hamilton trimer order by boundary antisymmetry, and V is a disjoint Hamilton path. Consequently

  (the certified trimer on {r,s,u}) | (a Hamilton trimer on S-u) | V  (RD.5)

is a literal spanning three-path cover of H, hence a maximum compatible spanning forest. So the adjacent-slot swap arrow is already an actual fresh representative.

### 5. Quiet same-gap one-sided fans are also fresh trimer representatives
Suppose r,s occupy the same insertion gap u|v of K. If the two double-insertion failures occur on opposite sides, SV26201 produces a universally one-extendable four-set, which is the small-core destination.

If both failures occur on the same side, SV26201 gives a SOURCE or SINK fan on the physical dimer {r,s}. In either orientation the fan contains a literal tight trimer on exactly

  {r,s,u}                                                  (RD.6)

for a left/source fan, or on exactly

  {r,s,v}                                                  (RD.7)

for a right/sink fan. Pair that certified trimer with a Hamilton trimer on the other three vertices of S and with the unchanged rail V. Again this is a literal spanning maximum three-forest of H.

Boundary same-gap cells cannot occur here because R157 places r and s internally in P_r and P_s, so their insertion slots in the common S-order are internal.

### 6. Residual-dimer extinction
Therefore a non-Hamilton universally one-extendable four-set with an exact residual dimer rail has no terminal local obstruction. Every comparison of the two endpoint-surgery representatives reaches

1. a universal one-extension four-set,
2. a fresh actual maximum spanning three-forest, or
3. a closed movable-break maximum-forest orbit.           (RD.8)

No endpoint-reversal residue survives, and no new one-sided-fan species remains. Thus in any minimal-holonomy counterexample to the G10 parent theorem, every exact residual two-cover Y=U|V associated with a non-Hamilton universal-extension core must have both rail orders at least three.

This is a routing/extinction theorem for the residual-dimer case, not global universal-core absorption.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R156"
    },
    {
        "relation": "dependency",
        "revision_id": "R157"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
