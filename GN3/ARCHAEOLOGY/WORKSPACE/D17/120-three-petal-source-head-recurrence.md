# The three-petal fixed point carries a forced source-head equal recurrence

**Workspace:** D17
**State:** established
**Key:** `three-petal-source-head-recurrence`

**Summary:** At the R953 same-size fixed point with historical order A=L-z-R and Z={z}+R, the p-isolated source (B+Z)|L is automatically universally crossed at z: (B+Z-z)+p cannot be Hamiltonian because it would pair with the literal path L-z to cover H. Thus the fixed point canonically restarts Arm A at the same minimum offending size with preserved source-head ancestry. In the DR17.55 globally quiet HHH cell, the puncture path on Z-z+p preserves the terminal dimer of Z, so no Hamilton B+Z order may consist of the literal Z block followed by a B block; such an order would splice to a spanning two-cover.

### 1. Fixed-point source rotation preserves a forced universal crossing

Retain the R953 same-size three-petal fixed point with the HISTORICAL critical-fork coordinates

  A=L-z-R,
  Z={z} union R,
  |L|=|B|=|Z|=k,

and common omitted label p. Thus L+p, B+p, Z+p are non-Hamiltonian deletion-Hamiltonian, while all three pair unions L+B, L+Z, B+Z are Hamiltonian. In particular choose any actual Hamilton path Q_BZ on B+Z. The p-isolated source is

  C_p^iso : (B+Z) | L

on H-p. Its large rail has size 2k, which is the same critical offending size a=2k.

The distinguished historical vertex z is automatically universal on the B+Z side of this source. Indeed consider

  (B+Z-{z}) union {p} = B union R union {p}.

If this support were Hamiltonian, choose a Hamilton path K on B+R+p. The old source order A=L-z-R has the literal prefix path L-z on L+{z}. These two supports are disjoint and partition V(H), so

  (L-z) | K

would be a spanning two-path cover of H, contradiction. Hence

  B+R+p is non-Hamiltonian.

By the support characterization of universal crossing from the universal-source development, this is exactly the statement that z is universally crossing relative to the actual p-isolated source (B+Z)|L.

Thus the three-petal fixed point is not a support-symmetric dead object. It comes with a canonical source rotation preserving the original distinguished source head:

  old source ancestry:       (L+Z) | B, with Z beginning at z after L;
  fixed-point p-isolated source: (B+Z) | L, universally crossed at the SAME z.

The recurrent offending rail has size |B+Z|=2k=a, so this is an exact equal-size recurrence, not a descent claim. What is new is the retained ancestry: the complement L+z is a literal Hamilton path, and the missing substitution (B+Z-z)+p is therefore certified non-Hamiltonian for a concrete cover-valued reason.

### 2. The next split is Hamilton deletion versus R942-compatible deletion

Because z is a physical endpoint of the retained petal order Z=(z,r_0,...), the old petal deletion Z-z=R is Hamiltonian. This does NOT imply B+R is Hamiltonian. Hence the new equal recurrence has a clean two-way continuation:

  (HAMILTON-DELETION) B+R is Hamiltonian;
  (NON-HAMILTON-DELETION) B+R is non-Hamiltonian.

In the second branch the accepted R942 arbitrary-fragmentation parent is legally applicable again to the minimum-size universal source C_p^iso with offending vertex z, because its offending-rail deletion (B+Z)-z=B+R is non-Hamiltonian. Any disconnected reduction, connected rainbow hinge, split-star weave, or later equal/larger recurrence must therefore retain this rotated source and the literal complementary path L-z.

In the first branch one has a universal crossing whose offending-rail deletion is Hamiltonian. This is precisely the branch in which a transition-one / endpoint-source consumer is potentially available, but no tau=1 representative is asserted here. The fixed point has therefore been reduced to a canonical equal recurrence with a sharper source-head certificate rather than merely being named as a symmetric terminal.

### 3. Quiet HHH forbids the Z-first block order on B+Z

Now additionally assume the source-anchored R961 comparison of DR17.55 on the saturated petal Omega=Z+p lies in its globally R435-quiet HHH cell. Write the literal petal order

  Z=(z,r_0,r_1,...,r_t),

where k>=4, hence t>=2. DR17.55 then gives the actual z-puncture Hamilton path

  K_z=(r_0,p,r_1,...,r_t)

on R+p. In particular K_z and Z have the SAME literal terminal dimer (r_{t-1},r_t).

Suppose there were a Hamilton path on B+Z having the literal whole Z block first, followed by one Hamilton B-block:

  Q = (z,r_0,...,r_t, b_0,b_1,...,b_{k-1}),

where (b_0,...,b_{k-1}) is some actual Hamilton order of B. The only turns of Q that meet the Z|B seam are

  (r_{t-1},r_t,b_0),
  (r_t,b_0,b_1).

Replacing the entire initial Z block by K_z leaves both seam turns literally unchanged because K_z has the same terminal dimer. Therefore

  (r_0,p,r_1,...,r_t,b_0,...,b_{k-1})

is a Hamilton tight path on R+p+B. Together with the disjoint literal source path L-z, it spans H by two tight paths, contradiction.

Hence in the globally quiet HHH cell NO Hamilton B+Z order can be obtained by putting the literal Z order as one complete leading block followed by a B-block. Equivalently, any retained B+Z Hamilton order must either expose explicit R435 geometry relative to the source orders, place B before the completion of Z, or genuinely interleave/split the petal contacts.

This is a one-sided block-order exclusion, not a full pair-union classification. The opposite B-then-Z block order is not eliminated by this argument because K_z changes the head of the Z block and therefore does not preserve its incoming seam.

### 4. Relation to the endpoint-row target

The first part supplies a concrete missing one-for-one substitution at the fixed point:

  (B+Z)-z+p is non-Hamiltonian.

Thus endpoint-exchange shortage on the p-isolated pair-union side is not anonymous. It is already tied to the old tau=1 ancestry and to the literal Hamilton complement L-z. If a chosen Hamilton order of B+Z exposes z as an endpoint, this missing substitution is an endpoint-row zero for exactly the R966 capacity framework; if z is not endpoint-accessible, that absence must be retained rather than silently replaced by a generic row count.

The quiet HHH clause further shows how a successful source-aligned pair-union boundary state would be consumed: a Z-leading block is immediately replaceable by the actual z-puncture path and closes H. The unresolved cases are therefore genuinely non-block/interleaved pair-union geometry, explicit R435 output, or the rotated equal recurrence described above.

Status: complete internal working deduction from accepted R953 plus the literal historical source order; section 3 additionally uses the working DR17.55 source-anchored quiet packet. No canonical review is claimed, and no global recurrence descent is asserted.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "related",
        "revision_id": "R942"
    },
    {
        "relation": "related",
        "revision_id": "R435"
    }
]
```
