# A triangulated portal wheel is globally support-coherent or exposes a current common-residue crossing

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-johnson-triangle-coherence-quotient`

**Summary:** For any three pair-deletion fibers on a Johnson triangle {x,a,b}, inspect the surviving third vertex in each exact cover. If one is internal, deleting it gives a literal three-cover of the common triple-deletion residue and hence a current component-drop crossing against an exact two-cover. If all are endpoints, the trims are exact two-covers of the same residue; differing support partitions give an R410 current crossing, while equality defines a support-commuting triangle. Apply this around a G23 portal-wheel rim. If every triangle commutes, the spoke partitions glue to one bipartition P of V(H)-{x}. Each rim partition then has only one remaining binary choice, the side containing the hub x. A change of this hub-side bit between adjacent rim fibers again gives either an internal-trim component drop or two exact common-residue covers with differing partitions, hence an R410 crossing. Therefore outside current crossing/component-drop geometry all hub bits are constant and every spoke/rim support partition is the restriction of one global bipartition P* of V(H). This is a coherent-wheel gluing theorem, not yet a spanning two-cover.

### 1. Pair-deletion Johnson triangle compiler
Let H be a hypothetical smallest Strong Level-(1) counterexample. Fix three distinct physical vertices x,a,b and choose literal exact pair-deletion covers

  C_xa of H-{x,a},
  C_xb of H-{x,b},
  C_ab of H-{a,b}.

Accepted R429 makes every rail of every chosen cover nontrivial.

Put W=H-{x,a,b}. First note that pc(W)=2. Accepted minimality R4 gives pc(W)<=2. If W were Hamiltonian, R3 supplies a tight Hamilton ordering of the deleted triple {x,a,b}, and those two disjoint paths would two-cover H. Hence pc(W) is not one.

Now inspect the surviving third triangle vertex in each pair-deletion cover.

- In C_xa inspect b.
- In C_xb inspect a.
- In C_ab inspect x.

If one inspected vertex is internal on its rail, deleting it splits that rail into two nonempty intervals while the other rail survives, giving a literal three-cover of W. Since pc(W)=2, choose an exact two-cover of W. The component count drop supplies a physical selected cross-state between two components of the three-cover, and accepted R159 gives the corresponding component-drop pair certificate. Retain the actual three-cover, exact two-cover and selected crossing as CURRENT common-residue data.

Suppose instead that all three inspected vertices are rail endpoints. Trimming them leaves three literal two-nonempty-path covers of W. Since pc(W)=2, all three are exact. Compare their unordered support partitions. If two differ, the proof mechanism of accepted R410 supplies a selected state of one exact cover crossing the support partition of the other; retain that selected state before any payment. If all three support partitions agree, call the Johnson triangle SUPPORT-COMMUTING.

Thus every actual pair-deletion Johnson triangle has the exact dichotomy

  CURRENT common-residue crossing/component-drop,
  or three endpoint trims with one common support partition.       (JW.1)

No payment or historical reentry is needed for the first branch.

### 2. Apply the compiler around a portal-wheel rim
Retain a G23 hub-and-rim wheel with physical hub x and a shortest root-capture rim

  d_0 -> d_1 -> ... -> d_{r-1} -> d_0,   2<=r<=5,

with distinct rim labels. For each spoke pair {x,d_i}, choose one literal exact pair-deletion cover S_i. For each rim arc choose one literal exact pair-deletion cover R_i on the pair {d_i,d_{i+1}}; in the r=2 case the two directed rim arcs may retain two different exact representatives of the same deleted pair. Such exact covers exist by R429 and may be chosen from the same-pair currentization data of SV60333 whenever that branch already supplies one.

Apply Section 1 to every Johnson triangle

  {x,d_i,d_{i+1}}.                                      (JW.2)

If any triangle takes the first branch of (JW.1), the wheel already exposes a current common-residue crossing/component-drop and we stop. Hence assume every triangle is SUPPORT-COMMUTING.

### 3. The spoke partitions glue on V(H)-{x}
Write pi_i for the support partition of S_i on V(H)-{x,d_i}. For each consecutive pair i,i+1, support-commutation says that pi_i and pi_{i+1} have identical restrictions to

  W_i=V(H)-{x,d_i,d_{i+1}}.                              (JW.3)

The trimmed covers on W_i have two nonempty rails, so the two blocks can be aligned uniquely across each adjacency, up to one initial global swap. Propagate this naming around the rim.

For r>=3, fix any physical vertex v!=x. If v is not a rim label, it occurs in every pi_i. If v=d_j, it occurs in every pi_i except pi_j; the index set C_r-{j} is connected. Along every adjacency on which v survives, (JW.3) preserves its named block. Hence v receives one well-defined global block label. The final rim adjacency is compatible with the initial naming because its common restriction has both blocks nonempty. For r=2, pi_0 and pi_1 agree on V(H)-{x,d_0,d_1}; align those two nonempty blocks directly, then assign d_0 from pi_1 and d_1 from pi_0.

Consequently there is one unordered bipartition

  P = A | B  of V(H)-{x}                                 (JW.4)

such that every spoke partition pi_i is exactly P restricted to V(H)-{x,d_i}.

### 4. Every rim partition has only one remaining bit: the hub side
Fix a rim edge i. Its cover R_i lives on V(H)-{d_i,d_{i+1}} and, by support-commutation of triangle i, trimming the endpoint x gives exactly P restricted to W_i. Therefore the full support partition of R_i is obtained from P merely by choosing which of the two P-blocks receives x.

Write

  c_i in {A,B}                                            (JW.5)

for this HUB-SIDE bit. All nonhub vertices of R_i already have their global P-side; c_i is the only support-partition freedom left on that rim fiber.

### 5. A change of hub-side bit is itself a current portal
Assume first r>=3 and c_i!=c_{i+1}. Compare the adjacent rim covers R_i on H-{d_i,d_{i+1}} and R_{i+1} on H-{d_{i+1},d_{i+2}} on their common triple-deletion shadow

  Z_i=H-{d_i,d_{i+1},d_{i+2}}.

Inspect d_{i+2} in R_i and d_i in R_{i+1}. If either is internal, deleting it gives a literal three-cover of Z_i, while minimality gives an exact two-cover; retain the resulting current component-drop crossing exactly as in Section 1.

If both are endpoints, trim them. Both trims are exact two-covers of Z_i. Their nonhub vertices inherit the same P-partition, but x lies in opposite blocks because c_i!=c_{i+1}. Hence their support partitions differ. Accepted R410 then supplies a physical selected cross-state between these two actual common-residue covers. Thus

  c_i != c_{i+1}
    => CURRENT crossing/component-drop.                  (JW.6)

For r=2, the two rim representatives R_0,R_1 already live on the same residue H-{d_0,d_1}. If c_0!=c_1 their support partitions differ directly, so R410 gives the same current crossing conclusion.

Therefore, outside current common-residue geometry, all hub-side bits are equal:

  c_0=c_1=...=c_{r-1}.                                   (JW.7)

### 6. Coherent-wheel gluing
When (JW.7) holds, extend P by placing x in that common side. Call the resulting bipartition

  P^* = A^* | B^*  of V(H).                              (JW.8)

Every spoke cover S_i and every rim cover R_i has support partition exactly equal to the restriction of P^* to its deleted-pair residue. Hence a portal wheel has the parent dichotomy

  INCOHERENT WHEEL:
    a visible current common-residue crossing/component-drop occurs on one Johnson triangle or one adjacent-rim comparison;

  COHERENT WHEEL:
    all chosen spoke/rim pair-deletion support partitions are restrictions of one global bipartition P^* of V(H).             (JW.9)

This is a support-level gluing theorem for the whole bounded wheel. It reduces all quiet Johnson-triangle freedom to one hub-side bit and then proves that even that bit cannot vary without producing current geometry.

### 7. Scope fence
The coherent branch is not yet a two-cover. A global support bipartition on only the wheel deletion fibers does not by itself certify Hamilton paths on both full blocks. Nor does (JW.9) assert that the alternative spoke/rim descendants coexist as one current state; it compares actual literal covers that are individually available in the reconstruction-closed family. The gain is the exact G23 quotient: a triangulated portal wheel cannot remain quietly incoherent. Any surviving quiet wheel is supportwise the restriction of one global partition, so the next theorem may attack that coherent partition directly rather than another portal taxonomy.

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
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```