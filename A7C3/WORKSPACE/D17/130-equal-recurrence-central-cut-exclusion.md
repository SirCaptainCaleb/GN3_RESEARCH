# Equal recurrence forbids Hamilton deletion of the central-cut neighbor

**Workspace:** D17
**State:** working
**Key:** `equal-recurrence-central-cut-exclusion`

**Summary:** In the high-a three-petal regime, every equal R942 disconnected recurrence step cuts the retained minimum source at a central position. The source neighbor transferred to the new small petal Hamilton-extends that petal, so the movable-pivot parent forces its deletion from the new large mixed support to be non-Hamiltonian. Hence that named seam vertex is internal in every Hamilton path on the new large support. In a support-stationary two-step recurrence, the two retained pre-z neighbors from the alternating source orders are both forbidden Hamilton endpoints of the same third pair-union, forcing every Hamilton order of that pair-union to be R435-active against at least one retained petal order. This is a terminal-state restriction, not yet a consumer of the recurrence orbit.

### Setup and one-step exclusion
Retain the high-a equal-recurrence regime arising from the R953 three-petal fixed point. Thus |H|=3k+1, the globally minimum universal offending size is a=2k, so |H|<2a and the movable-pivot parent in `three-petal-hamilton-deletion-closure` forbids every legal one-vertex transfer inside every singleton-deletion fiber.

Consider one equal disconnected R942 step. Write the retained actual minimum-source order as

  A = U - z - V,

with |A|=2k and opposite Hamilton source rail B of order k. Suppose the disconnected common-residue cover isolates V; the U-isolated case is the exact dual. The equal recurrence produces an actual Hamilton mixed support

  M=U union B

of order 2k and the new small Hamilton support

  Z'={z} union V

of order k, giving the literal exact source

  H-p : M | Z'.

Equality |M|=2k and |B|=k forces |U|=k; hence |V|=k-1. Thus z occurs at the central cut of the retained actual source order. Let u be the final vertex of the literal U block, i.e. the physical source neighbor immediately before z.

The literal contiguous source suffix beginning at u is

  u - z - V,

so Z'+u is Hamiltonian in this retained order. If M-u were Hamiltonian, then the same deletion fiber H-p would contain both exact Hamilton support partitions

  M | Z'
  and
  (M-u) | (Z'+u).

These differ by the legal one-vertex transfer of u. This is impossible because |H|<2a by the movable-pivot parent. Therefore

  M-u is non-Hamiltonian.

In particular u is not an endpoint of any Hamilton path on M: deleting an endpoint from such a Hamilton path would Hamiltonize M-u. The U-isolated dual says that the physical source neighbor immediately after z is non-Hamilton-deletable from the corresponding new large mixed support.

This conclusion is stronger than a generic endpoint-row zero. It identifies the forbidden Hamilton endpoint with the ACTUAL source seam used by the equal recurrence.

### General transfer-to-terminal-state corollary
More generally in any regime with a>|H|/2, let H-p have an exact Hamilton cover X|Y. If x in X satisfies Y+x Hamiltonian, then X-x is non-Hamiltonian. Otherwise X|Y and (X-x)|(Y+x) would be a forbidden legal one-vertex transfer. Consequently every endpoint of every Hamilton path on X lies outside the extension set

  G_Y={x in X : Y+x is Hamiltonian}.

This is a support-level terminal-state restriction derived from realizable cover change; it does not synchronize Hamilton orders.

### Stationary equal recurrence forces a named third-pair order conflict
Suppose now that an equal recurrence orbit is support-stationary on three k-petals X,Y,Z with z in Z and omitted label p: the alternating minimum sources use the same petal partition and have retained block-source forms

  X - z - (Z-z) | Y,
  Y - z - (Z-z) | X,

or the exact common dual orientation. Let u_X and u_Y be the final vertices of the retained X and Y blocks immediately before z. Applying the one-step exclusion to the two equal steps shows

  (X union Y)-u_X is non-Hamiltonian,
  (X union Y)-u_Y is non-Hamiltonian.

Hence u_X and u_Y are internal in every Hamilton path Q on the Hamilton pair-union X+Y.

Compare any such Q with the retained Hamilton orders on X and Y. If both comparisons are R435-quiet, the X-contacts of Q occur in increasing retained X-order and the Y-contacts occur in increasing retained Y-order. Therefore Q is a shuffle preserving both retained orders. The final vertex of such a shuffle must be the final retained X vertex u_X or the final retained Y vertex u_Y. Both are forbidden Hamilton endpoints, contradiction. Thus every Hamilton path on X+Y has explicit R435 Reverse-Ear geometry against at least one of the two retained petal orders.

In particular neither retained-order block concatenation X followed by Y nor Y followed by X can be Hamiltonian on X+Y, because those orders end at u_Y and u_X respectively. Any stationary survivor requires genuine interleaving/order conflict on the third pair-union.

This does NOT close the stationary orbit: R483 forbids treating the resulting R435 event family as absorption, and no R561 boundary-reversed Hamilton dimer has yet been extracted. The value of the lemma is that every equal step creates a named terminal exclusion on its actual changed seam, so a complete recurrence orbit carries terminal-state data that a future legal-transfer/R561 consumer must preserve.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R942"
    },
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "related",
        "revision_id": "R435"
    },
    {
        "relation": "related",
        "revision_id": "R561"
    }
]
```
