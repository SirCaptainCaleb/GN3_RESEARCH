# The Hamilton-deletion source-head branch is impossible by a smaller pivot source

**Workspace:** D17
**State:** established
**Key:** `three-petal-hamilton-deletion-closure`

**Summary:** At the R953 same-size three-petal fixed point, if S=(B+Z)-z were Hamiltonian then H-p would have two exact Hamilton covers (S+z)|L and S|(L+z). The second places z on a rail of size k+1<2k=a. Global minimality makes z non-universal there; a quiet H-z cover with no L|S adjacency then forces L+p or S+p Hamiltonian, and either possibility two-covers H. Hence S is non-Hamiltonian and the DR17.58 recurrence always re-enters R942. A general movable-pivot lemma now shows that two adjacent singleton-cover support partitions force universal crossing at the transferred vertex on both sides; hence |H|>=2a. If a>|H|/2, every legal one-vertex rebalancing of any singleton cover is forbidden. This parent is a new internal deduction pending review.

### Setup
Retain the R953 same-size three-petal fixed point and the accepted DR17.58 source-head recurrence. Thus |L|=|B|=|Z|=k, Z={z} union R, the historical source order is the literal tight path L-z-R, X=B union Z is Hamiltonian, C=L union {p} is non-Hamiltonian deletion-Hamiltonian, and the p-isolated exact source H-p : X | L is universally crossed at z with globally minimum offending-rail size a=|X|=2k. Also S+p=((B union Z)-z) union {p} is non-Hamiltonian, since otherwise it would pair with the literal tight path L-z and two-cover H.

Assume for contradiction the Hamilton-deletion branch S:=X-z=B union R is Hamiltonian.

### A second exact source in the same deletion fiber
The literal historical prefix L-z is a tight Hamilton path on L union {z}. Since S is Hamiltonian, H-p has a second exact two-cover C_p^small : S | (L union {z}). The rail containing z now has size k+1. We have k>=2: if k=1 then |H|=3k+1=4, and two disjoint dimers already give a spanning two-cover. Hence k+1<2k=a.

By the global choice of a, z cannot be universally crossed relative to C_p^small. Thus there exists a literal exact two-cover T of H-z selecting no adjacency between L and S.

### The quiet pivot source forces one forbidden extension
Now V(H-z)=L disjoint-union S disjoint-union {p}. The only vertex outside L and S is p. Let T_0 be the rail of T not containing p. Since T has no selected L|S adjacency, T_0 lies wholly in one of L,S.

If T_0 is contained in L, then every vertex of S lies on the p-containing rail. That rail cannot move between S and L except through the single vertex p, so all of S occurs as one contiguous block adjacent to p. The corresponding contiguous subpath is a Hamilton tight path on S union {p}. Thus S+p is Hamiltonian. Dually, if T_0 is contained in S, then L+p is Hamiltonian. The case where {p} itself is a rail is impossible, because the other single rail could not cover both nonempty classes L,S without an L|S adjacency. Therefore every quiet witness forces S+p Hamiltonian or L+p Hamiltonian.

Both alternatives contradict pc(H)>2. The first would pair with L+z; the second contradicts the fixed-point non-Hamiltonicity of L+p and would pair with X=S+z. Hence the Hamilton-deletion assumption is impossible.

### Consequence for Arm A
At every R953 same-size three-petal fixed point, the DR17.58 distinguished recurrence satisfies (B union Z)-z=B union R non-Hamiltonian. Therefore the p-isolated minimum source (B+Z)|L, universally crossed at the same physical z, always meets the non-Hamiltonian-deletion hypothesis of accepted R942 and legally re-enters that theorem at the same offending size. The formerly separate Hamilton-deletion branch is eliminated.
### Parent: a movable pivot forces two universal sources

This is a new complete internal deduction, pending independent canonical review. It uses the quiet-cut argument of R927/P999, not R24.

Let H admit no spanning two-cover, and let V(H)={p,z} disjoint-union S disjoint-union T with S,T nonempty. Suppose S,T,S+z,T+z are all Hamiltonian. Thus H-p has two literal exact sources
  (S+z)|T,    S|(T+z).
Every exact H-z two-cover must select an S|T adjacency. Indeed, if one did not, the rail avoiding p would be monochromatic, and the p-containing rail would contain the whole opposite class as a contiguous block adjacent to p. It would certify S+p or T+p Hamiltonian. The former pairs with T+z and the latter with S+z to cover H, impossible. This proves that z is universally crossed in BOTH displayed sources, with precisely the SAME target cut S|T.

If a is the globally minimum offending-rail size among all universal singleton sources, it follows that
  a <= min(|S|+1, |T|+1),
and therefore |H|=|S|+|T|+2 >= 2a.

Equivalently, when a>|H|/2, NO singleton-deletion cover can admit a one-vertex support transfer that leaves both rails Hamiltonian: such a transfer is exactly the displayed pair of sources. This forbids transfer in every singleton fiber, not only the original minimizing one. Actual path orders on the two transferred supports may be completely different.

The three-petal application above is immediate: S=B+R, T=L, n=3k+1, a=2k, and the historical prefix certifies T+z. Since n<2a for k>=2, S cannot be Hamiltonian. More generally the conclusion is a precise constructive target: in this high-a regime it suffices to exhibit ONE legal one-vertex transfer anywhere in the singleton-cover family. This does not assert such a transfer exists, does not make an equal recurrence strict, and does not address the regime a<=|H|/2.


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
        "revision_id": "R942"
    }
]
```
