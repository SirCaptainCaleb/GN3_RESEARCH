# A balanced full-Z rail forces a P4 or a two-witness reverse-boundary packet

**Workspace:** D17
**State:** working
**Key:** `stationary-z-entry-insertion-barrier`

**Summary:** In the stationary c=2 residue, suppose Z is one full block on a T rail R of size m<=2k-2. Outside same-support R435 disagreement, the Z block has its retained order beginning at z. If Z is the rail source, either omitted seam terminal prepends and immediately gives a forbidden subminimum singleton source. Otherwise let q immediately precede z. If q has predecessor r, insertion of u_X or u_Y between q and z requires exactly the two turns (r,q,u) and (q,u,z); threshold saturation forces at least one failure for each u. Two left failures give an R542 two-witness packet on reverse boundary dimer (q,r) of selected trimer (r,q,z). A mixed pair forces a Hamilton P4 by incompatible R516 alignment bits and R522, while two right failures force a P4 directly from R516. If q is the rail source, the two right failures likewise force a P4. Thus every balanced full-Z survivor exports an actual selected-entry P4 or R542 packet, with all seam ancestry retained.

### Setup and the exact size window
Retain the stationary c(T)=2 residue. Thus W=H-{u_X,u_Y}, |H|=3k+1, a=2k, and the retained stationary source seams give literal tight paths

  u_X - z - (Z-z),
  u_Y - z - (Z-z),

up to the exact common dual orientation. Let T be an exact two-cover of W in which Z occurs as one full maximal block on a rail R. Write m=|R|.

Compare the Hamilton order of this full Z-block with the retained Hamilton order Z=(z,z_2,...,z_k). If the comparison has explicit R435 reversal/reverse-trimer/cycle geometry, retain that order-valued output. Otherwise R435 monotonicity on equal supports forces the block order to be exactly

  z,z_2,...,z_k.

Assume from now on this quiet order and

  m <= 2k-2.

Since the rail contains all k vertices of Z, m>=k. If one omitted seam terminal u is inserted into R while the other T rail is unchanged, the resulting singleton-deletion cover has rail sizes

  m+1  and  (3k-1)-m.

The first is at most 2k-1; the second is also at most 2k-1 because m>=k. Hence both are strictly below a=2k. By `subminimum-source-saturation`, NO such insertion may succeed for either u_X or u_Y.

### Source Z-block closes immediately
If Z is the first block of R, prepend either u in {u_X,u_Y}. The only new turn is

  (u,z,z_2),

which is an ancestral stationary seam turn. Thus the insertion succeeds, contradicting the preceding size argument. Therefore every balanced survivor has some selected predecessor q immediately before z on R.

### Complete two-window insertion obstruction
First suppose q is not the rail source, and let r be its selected predecessor. Then T contains the tight selected trimer

  C=(r,q,z).

Replacing the local segment r,q,z by r,q,u,z changes exactly two turns:

  (r,q,u),   (q,u,z).

The following turn (u,z,z_2) is ancestral and tight, and every other turn of R is unchanged. Therefore for each u in {u_X,u_Y}, at least one of the two displayed turns is bad. By exact reversal, every u has at least one of the labelled failure certificates

  L_u : (u,q,r) tight,
  R_u : (z,u,q) tight.

These certificates retain the same actual selected entry q-z and, in the L case, the same selected predecessor state r-q.

### LL is exactly a short-carrier two-witness packet
If L_{u_X} and L_{u_Y} both hold, then the tested oriented dimer

  S=(q,r)

is the reverse left boundary dimer of the tight selected trimer C=(r,q,z), and u_X,u_Y are two distinct head witnesses on that SAME tested orientation:

  (u_X,q,r),   (u_Y,q,r).

Accepted R542 therefore applies with the full selected-trimer ancestry retained. This is a genuine short-carrier capture/payment packet, not an anonymous R435 event.

### A mixed failure pair forces a Hamilton P4
Suppose, for example, L_{u_X} and R_{u_Y} hold. Apply the accepted R516 no-P4 signature classification to the common tight trimer C=(a,b,c)=(r,q,z).

If C+u_X had no Hamilton P4, the turn

  (u_X,q,r)=(y,b,a)

is the exact reversal of (a,b,y), so the R516 alignment bit A=[(a,b,y) tight] must be 0.

If C+u_Y had no Hamilton P4, the turn

  (z,u_Y,q)=(c,y,b)
occurs only in the R516 rows with the same alignment bit A equal to 1.

But accepted R522 says that two distinct no-P4 extensions of one tight trimer have the same R516 signature, in particular the same A bit. Contradiction. Hence at least one of C+u_X or C+u_Y supports a tight Hamilton P4. The L/R-dual mixed pattern is identical.

### RR forces a Hamilton P4 even without r
Assume R_{u_X} and R_{u_Y}:

  (z,u_X,q),   (z,u_Y,q)

are tight. Regard C'=(z,u_X,q) as a tight trimer and u_Y as fourth vertex. If this four-set had no Hamilton P4, inspect any of the four exact R516 no-P4 rows. In every row the turn

  (q,u_Y,z)

is tight. It is the complete reversal of the already tight turn (z,u_Y,q), impossible. Therefore {z,q,u_X,u_Y} supports a Hamilton P4.

The same argument covers the endpoint degeneration where q itself is the rail source. There the insertion q,u,z needs only (q,u,z) in addition to the ancestral (u,z,z_2), so threshold saturation forces R_{u_X} and R_{u_Y}, and the preceding four-set P4 follows.

### Output
Thus a stationary c=2 cover whose full retained-order Z-block lies on a rail of size at most 2k-2 cannot remain locally featureless. It yields one of:

1. explicit same-support R435 geometry on the Z block;
2. a tight Hamilton P4 in a labelled cell meeting the selected Z-entry and one or both omitted seam terminals;
3. the exact R542 two-witness packet on reverse boundary dimer (q,r) of the selected trimer (r,q,z).

No claim is made that the P4 branch alone closes H. Its value is currentization: the P4 is born at the actual selected Z-entry of the common-residue cover, while the R542 branch retains the same carrier and both omitted seam terminals as witnesses. The remaining stationary work is to consume these labelled outputs and to handle the oversized-Z-rail and exceptional fragmented-Z cells.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R516"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    },
    {
        "relation": "dependency",
        "revision_id": "R542"
    },
    {
        "relation": "dependency",
        "revision_id": "R953"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```
