# A one-p stationary cover either balances at the A-B cut or exposes a consecutive source edge across the split petal

**Workspace:** D17
**State:** working
**Key:** `stationary-one-p-cut-or-cross`

**Summary:** Corrected one-p cut-or-cross interface. In the quiet c=2,d=1,tau_Z=1 cell, branch explicitly on R435 not only for the full B,Z blocks but also for each fragmented A-block path. Outside those order-conflict branches each A block is an increasing retained-A subsequence, so the balancing splice is valid: failure pins a literal consecutive retained A edge across the two current A blocks at the unique A-B interface. The earlier incoming-seam monotonicity assumption is now explicit.

### Setup
Retain the corrected quiet stationary c=2 cell and the d>=1 conclusion of `stationary-isolated-p-consumer`. Assume d=1. Up to A/B duality, p has one selected incidence with A and none with B. Then the corrected block identity gives

  b_A=2,  b_B=b_Z=1.

Thus A is the unique fragmented petal, while B and Z are full current blocks. Branch explicitly if either full B or Z block order has R435 geometry relative to its retained order. ALSO branch explicitly if either current A-block path has R435 reversal/reverse-trimer/cycle geometry relative to the retained A order. Outside these branches, B and Z equal their retained orders and every current A block is an increasing retained-A subsequence. This A-block monotonicity is required below; the earlier DR17.84 wording used it silently in the incoming-seam paragraph. Write

  A=(a_1,...,a_{k-1}),  B=(b_1,...,b_{k-1})

for the retained orders and let

  K_A=(a_1,...,a_{k-2},p,a_{k-1}),
  K_B=(b_1,...,b_{k-2},p,b_{k-1})

be the quiet final-gap puncture paths supplied by `terminal-puncture-last-gap` and the source-anchored packet.

Let tau_Z be the number of the two common-cross transitions incident with Z. Since p-Z is impossible, tau_Z=1 means exactly one common cross is Z-incident and the other common cross is an A-B transition. Hence there is a UNIQUE current A-B seam.

### Outgoing A-to-B seam: an aligned retained cut gives the desired balanced source
Suppose the actual A-B transition is from an A block into the full B block. Let its A endpoint be x=a_j. Since x is the final A vertex of that current A block, the T seam certifies

  (x,b_1,b_2)

and, when the immediate retained predecessor a_{j-1} lies in the same current A block, also

  (a_{j-1},x,b_1).

For j=1 the latter turn is absent and no predecessor is needed. In either case construct

  P_1=(a_1,...,a_j,b_1,...,b_{k-2},p,b_{k-1}),
  P_2=(a_{j+1},...,a_{k-1},u_X,z,...)

with the empty A suffix omitted when j=k-1. The first path is tight by the retained A prefix, the two selected A-B seam turns, and K_B. The second is the literal suffix of the historical stationary source A-u_X-Z. They partition H-u_Y. Their orders are

  |P_1|=j+k,
  |P_2|=2k-j.

Because 1<=j<=k-1, both are strictly below 2k. This contradicts `subminimum-source-saturation`.

Therefore, in any surviving outgoing A-to-B seam with j>1, the immediate retained predecessor a_{j-1} does NOT lie in the same current A block as a_j. Since the two A blocks partition A, the literal retained source edge

  a_{j-1} a_j

crosses the two current A blocks. For j=1 the balanced construction already closes the cell.

### Incoming B-to-A seam: only a head-aligned entry can avoid an immediate split-source edge, and that head entry closes
Suppose instead the actual A-B transition runs from the full B block into an A block, with first A vertex x=a_j. If j>1, the retained predecessor a_{j-1} cannot lie in this same A block: the block is an increasing A-subsequence beginning at a_j, so any retained predecessor present in it would have to occur before a_j. Hence the consecutive retained edge a_{j-1}a_j already crosses the two A blocks.

It remains j=1. If a_2 lies in the same current A block, the selected seam certifies

  (b_{k-2},b_{k-1},a_1),
  (b_{k-1},a_1,a_2).

Since K_A begins with a_1,a_2, replacing the entered A block and the other A/p material by the full puncture K_A gives the Hamilton path

  B followed by K_A

on M=A+B+p. Pairing it with the literal u_X+Z path gives the exact singleton cover

  H-u_Y : M | (u_X+Z)

of sizes 2k-1 and k+1, again contradicting the subthreshold theorem. Therefore a surviving head entry j=1 must have a_2 in the other A block, so the literal retained edge a_1a_2 crosses the two current A blocks.

### Exact surviving tau_Z=1 interface
Thus every surviving quiet c=2,d=1,tau_Z=1 cover has a graph-intrinsic consecutive retained A adjacency whose endpoints lie in the two distinct current A blocks, and this adjacency is pinned immediately beside the unique A-B seam in the retained source order. The B-dual statement holds when p is incident with B.

This is stronger than arbitrary two-block fragmentation: failure of the balancing splice identifies one exact source edge crossing the split petal. The next consumer should combine that source edge with the unique p-A incidence and the remaining Z-cross, retaining their actual rail locations. No claim is made yet that the cross-block source edge itself closes the branch.

Status: complete working deduction inside the corrected stationary c=2,d=1,tau_Z=1 quiet cell. Explicit R435 block-order outputs remain separate live alternatives.
