# A stationary equal recurrence forces a common cross-state after deleting both seam terminals

**Workspace:** D17
**State:** working
**Key:** `stationary-two-seam-common-cross`

**Summary:** In the support-stationary three-petal equal recurrence, deleting the two ancestral seam terminals produces two literal three-covers of the same residue. Every exact two-cover must contain a selected state crossing both decompositions. Otherwise the rigid hinge gives a singleton source with rail sizes 2k-1 and k+1, both below a=2k, contradicting subminimum-source saturation. The former R533/order-floor detour is unnecessary.


### Stationary setup
Retain the support-stationary high-a equal recurrence from `equal-recurrence-central-cut-exclusion`. Thus the three petals X,Y,Z have common size k, p is omitted, z lies in Z, and the two retained large-source orders have the literal forms

  X - z - (Z-z) | Y,
  Y - z - (Z-z) | X,

or the exact common dual orientation. Let u_X and u_Y be the final vertices of the displayed X and Y blocks immediately before z. The preceding section gives that u_X and u_Y are internal in every Hamilton path on X union Y.

Put

  A=X-{u_X},   B=Y-{u_Y}.

At the R953 three-petal fixed point, X+p and Y+p are non-Hamiltonian deletion-Hamiltonian. Therefore A+p and B+p are Hamiltonian. The retained petal orders also make A,B,Z Hamiltonian individually.

Delete both seam terminals and write

  W=H-{u_X,u_Y}=A disjoint-union B disjoint-union Z disjoint-union {p}.

W has path-cover number exactly two. Minimality gives pc(W)<=2; if W were Hamiltonian, its Hamilton path together with the vacuous dimer (u_X,u_Y) would two-cover H.

The residue W has TWO literal three-covers:

  R_X : (A+p) | B | Z,
  R_Y : (B+p) | A | Z.

### Simultaneous component-drop obligation
Let T be any exact two-cover of W. Relative to R_X, T must select a state between two distinct R_X components; otherwise two T rails cannot cover all three nonempty R_X components while reducing the component count from three to two. The same statement holds relative to R_Y.

Classify a selected interclass state by its endpoint classes among A,B,Z,{p}. The types

  A-B,  A-Z,  B-Z,  p-Z

cross BOTH three-cover decompositions. The type p-A crosses only R_Y, while p-B crosses only R_X.

Assume T contains no state of a common-cross type. Then satisfying both component-drop obligations forces T to select both a p-A state and a p-B state. Since p has degree at most two in a path cover, these are its only interclass incidences. There is no A-B, A-Z, B-Z, or p-Z transition. Hence every vertex of Z lies on one pure T rail, and the other T rail covers all of A union {p} union B. Necessarily A and B occur as complete contiguous blocks on the two sides of p. Thus, up to exact displayed reversal,

  T = (P_A - p - P_B) | P_Z,

where P_A,P_B,P_Z are actual Hamilton paths on A,B,Z. Call the mixed Hamilton support

  M=A union {p} union B.

### The hinge creates a forbidden sub-threshold source
The historical source seams give literal Hamilton paths on u_Y+Z and u_X+Z. Therefore the same mixed rail M produces two exact singleton sources

  H-u_X : M | (u_Y+Z),
  H-u_Y : M | (u_X+Z).

In the three-petal fixed point a=2k. Their rail sizes are

  |M|=(k-1)+1+(k-1)=2k-1,
  |u_Y+Z|=|u_X+Z|=k+1.

Both sizes are strictly below a=2k in the live three-petal regime. Equality between the two sizes at a small parameter is irrelevant: `subminimum-source-saturation` excludes every singleton source whose two rails are both below a, balanced or not. Hence either displayed source is impossible.

Therefore the hinge alternative is impossible.

### Surviving stationary residue
Every exact two-cover T of H-{u_X,u_Y} contains at least one ACTUAL selected state of one of the four common-cross types

  A-B,  A-Z,  B-Z,  p-Z.

That one state simultaneously crosses the two literal three-cover decompositions R_X and R_Y. It is therefore a common-shadow selected state to which accepted R176 may be applied relative to either decomposition while retaining the same physical state and the two omitted seam terminals as spare coordinates.

This is stronger than the earlier statement that the stationary orbit merely forces R435 activity on X+Y. The next consumer should distinguish the four common-cross types before paying R176, because generic balanced-pair descent would erase which of the two saturated puncture paths A+p or B+p supplied the old component at the selected endpoint.

Status: complete through the common-cross conclusion, conditional on the working movable-pivot/central-cut section that identifies u_X,u_Y as the stationary seam terminals. No absorption of the four surviving common-cross types is claimed here.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "related",
        "revision_id": "R176"
    }
]
```
