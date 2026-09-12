# A canonical flat-return rebirth is an immediate P4 or lands back in the common spoke class

**Workspace:** D17
**State:** established
**Key:** `canonical-rebirth-opposite-orientation-p4-or-same-spoke-cell`

**Summary:** In the SV81686 canonical flat-return rebirth, the new head dimer is (c,t), head-signed by the chosen source spoke r, so (r,c,t) is tight and t is distinct from a,c,r and from the fossil middle y. Apply R3 to {a,t,c}. If (c,t,a) is tight, then on the same tested oriented dimer (c,t) there is a head certificate with witness r and a tail certificate with witness a, so R523 gives the literal P4 (r,c,t,a). Otherwise (a,t,c) is tight, placing t in the same outer orientation class as the retained source spokes. Since y and t are distinct same-orientation spokes, SV89302 makes {a,c,y,t} Hamiltonian. Thus the canonical non-source rebirth cannot occupy an unstructured fourth type: it is either already P4/PAYABLE-FOUR geometry or its new support endpoint belongs to the same-spoke Hamilton outer-four regime. This does not by itself forbid re-display of the same static birth after later flat returns.

### 1. Canonical rebirth packet
Retain the flat-return construction SV81686 at the old endpoint pair E={a,c}. The unused source sibling contributes the tail dimer (a,y), and the first controlled post-return c-incidence produces a head-signed dimer D=(c,t) with exact head witness r, so (r,c,t) is tight. In the genuinely new-support branch t is distinct from y and from the source witness r; all displayed vertices are outside E as in SV81686.

### 2. Opposite E-orientation gives a literal P4
Apply boundary antisymmetry R3 to the physical triple {a,t,c}, displayed with middle t. Exactly one of (a,t,c), (c,t,a) is tight. Suppose (c,t,a) is tight. Then the tested oriented dimer (c,t) carries a HEAD certificate with witness r from (r,c,t) and a TAIL certificate with witness a from (c,t,a). The witnesses are distinct. Accepted R523 therefore gives the literal tight P4 (r,c,t,a). Hence the opposite-orientation branch has already crossed the P4/PAYABLE-FOUR interface.

### 3. The only P4-free branch joins the common spoke class
Assume instead that no such immediate P4 is taken. Then necessarily (a,t,c) is tight. Thus t has the same outer E-orientation as every retained source spoke x,y,z. Because SV81686 gives t!=y, apply the pairwise spoke theorem SV89302 to the two same-orientation spokes y,t. It follows that the outer four-set {a,c,y,t} has a literal Hamilton P4.

Therefore every canonical flat-return rebirth has the dichotomy: (1) immediate literal P4 (r,c,t,a); or (2) t lies in the same spoke class and {a,c,y,t} is Hamiltonian. The second branch is not yet a contradiction because the complementary Hamilton rail needed for a spanning two-cover is not asserted current merely from the birth certificate. Its significance is structural: a recurrent canonical rebirth cannot introduce an arbitrary new endpoint type outside the spoke geometry.

### 4. Scope fence
This is a localization theorem, not a repeated-generation monotonicity theorem. The PAYABLE-FOUR certificate is graph-intrinsic once exhibited and may be redisplayed after later R1022 reentry. No generation count or lineage identity is treated as progress. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```