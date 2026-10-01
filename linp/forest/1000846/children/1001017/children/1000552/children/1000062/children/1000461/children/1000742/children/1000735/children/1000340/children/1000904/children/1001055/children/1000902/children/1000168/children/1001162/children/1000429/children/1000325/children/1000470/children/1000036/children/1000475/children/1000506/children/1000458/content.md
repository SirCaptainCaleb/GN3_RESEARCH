# One-eighth X/U-or-nonflat dichotomy at top-layer switching centers

## Statement

Let P=(g_1,...,g_L) be a globally longest L-edge path ending at v, and let F be a family of ascending nonspecial single blockers through v, all of rank at most L-1. Restrict to interior blocker cells
  C_i={b_i,z_i}, 1<=i<=L-3,
and let s_int be the number of F-edges whose unique precursor contact lies in these cells.

Call an F-edge X-type if its unique path contact is its entrance, and U-type if its contact is its opposite terminal. Let U be the number of interior U-type members.

For each occupied cell C_i let h_i=g_{i+2} be its rotation-output edge, and call C_i flat if h_i is in the forward-flat ascending branch of 09e3d5b2bd6b. Let Y be the number of occupied nonflat cells.

Then
  s_int <= ceil((L-3)/2) + U + 2Y,
and therefore
  U+2Y >= s_int-ceil((L-3)/2).

In particular, for the switching family at a global-top active misaligned center,
  U+2Y >= L/8-eta_v-O(1).

Thus a low-defect top center cannot hide its 5L/8 switching family inside clean entrance-retained flat rotations: linearly many switchers must either be terminal-retained, or lie in cells whose output is special or all-top nonspecial nonascending.

## Body

Count only X-type switchers lying in flat occupied cells; let X_flat denote their number.

By 699a1e79304b the flat occupied cells form an independent set in the cell order: no two consecutive cells are flat.

A flat cell contains at most two switchers. If it contains two X-type switchers, their contacts must be exactly the private vertex b_i and the joint z_i.

For the joint entrance z_i=g_i intersect g_{i+1}, the clean-joint exclusion eac2e3da3eea says the immediately preceding first-contact cell C_{i-1} contains no singleton blocker.

For the private entrance b_i, let f be its switcher and r=phi(f). Since v is misaligned, r<=L-1. Apply the quantitative separation theorem 65894e91ed50 to any earlier singleton blocker whose first-contact cell is C_j. If j<=i-2, its part (a) gives
  i-j >= L-r+3 >=4.
Hence C_{i-2} and C_{i-3} also contain no singleton blocker.

Therefore every flat cell carrying two X-type switchers has the preceding three cells empty. A flat cell carrying one X-type switcher merely obeys the flat-cell independence rule.

We now use the elementary one-dimensional packing recurrence. On the first n cells, the maximum possible number W(n) of X-type switchers carried by flat cells satisfies
  W(n)<=max{W(n-1), W(n-2)+1, W(n-4)+2}.
The three alternatives are: the last cell is unused by X-flat switchers; it carries one X-flat switcher, forcing the preceding flat cell absent; or it carries two X-flat switchers, forcing the preceding three cells empty. With W(0)=0, this recurrence gives
  W(n)<=ceil(n/2)+O(1),
and in fact W(n)<=ceil(n/2) with the natural boundary convention.
Thus
  X_flat<=ceil((L-3)/2).                              (1)

Every interior switcher not counted by X_flat is either U-type, or lies in a nonflat occupied cell. The U-type members contribute at most U of them, while each nonflat cell has at most two contact vertices and hence contains at most two switchers. Therefore
  s_int<=X_flat+U+2Y.
Combining with (1) proves the first inequality.

Finally b032348c1a8a gives, at a global-top active misaligned center,
  s_int>=(5/8)L-eta_v-O(1),
after discarding O(1) boundary contacts. Since ceil((L-3)/2)=L/2+O(1),
  U+2Y>=L/8-eta_v-O(1).

By 09e3d5b2bd6b and 57d5e4c71035, every nonflat output counted by Y is either special or a nonspecial nonascending all-top rank-L edge.