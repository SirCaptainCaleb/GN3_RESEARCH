# Every low-defect misaligned center pays one-eighth into terminal retention or monotone output progress

## Statement

Let v be an active misaligned vertex with p=phi(v), and let F be a switching family from b032348c1a8a on the chosen maximum p-edge path P_v=(g_1,...,g_p). Restrict to interior blocker cells C_i={b_i,z_i}, 1<=i<=p-3, and let s_int be the number of F-edges whose unique P_v-contact lies in these cells.

Call a switcher X-type if its retained contact is its entrance, and U-type if its retained contact is its opposite terminal. Let U be the number of interior U-type switchers.

For each occupied cell C_i let h_i=g_{i+2} be the rotation-output edge. Call C_i flat if h_i is branch (3) of 6205fe95ecf8: phi(h_i)=p, h_i is nonspecial ascending, and its forward joint is the unique entrance of potential p-1. Let Y be the number of occupied cells that are not flat.

Then
  s_int <= ceil((p-3)/2)+U+2Y,
and hence
  U+2Y >= s_int-ceil((p-3)/2).

Since
  s_int >= (5/8)p-eta_v-O(1),
every low-defect misaligned center satisfies
  U+2Y >= (1/8)p-eta_v-O(1).

Every cell counted by Y yields one of the following monotone outputs:
(a) strict rank rise phi(h_i)>p;
(b) a special edge h_i of rank p;
(c) a nonspecial nonascending edge h_i of rank p whose three vertices all lie in the superlevel V_{>=p}={w:phi(w)>=p}.

Thus the only asymptotically unpaid switching behavior is the forward-flat ascending branch, and clean entrance-retained switchers can occupy that branch with density at most one half along the host path.

## Body

The proof is the same packing argument as 666bd06ca682, but 3c0ac5d646f1 removes the global-top hypothesis.

Let X_flat be the number of X-type switchers lying in flat occupied cells. By 3c0ac5d646f1, flat occupied cells form an independent set in the cell order.

A flat cell contains at most two switchers. If C_i contains two X-type switchers, their contacts are b_i and z_i, both clean entrances. By eac2e3da3eea, the joint entrance z_i forces the immediately preceding first-contact cell C_{i-1} to be empty.

Let f be the private-entrance switcher at b_i and put r=phi(f). Misalignment gives r<=p-1. If an earlier singleton blocker first contacts in C_j with j<=i-2, the quantitative separation theorem 65894e91ed50(a), applied with k=i, gives
  i-j >= p-r+3 >=4.
Therefore C_{i-2} and C_{i-3} are also empty.

Hence on the first n cells the maximum number W(n) of X-flat switchers obeys
  W(n)<=max{W(n-1),W(n-2)+1,W(n-4)+2},
so W(n)<=ceil(n/2). Thus
  X_flat<=ceil((p-3)/2).

Every interior switcher not counted by X_flat is either U-type or lies in a nonflat cell. A nonflat cell contains at most two switchers. Hence
  s_int<=X_flat+U+2Y
       <=ceil((p-3)/2)+U+2Y.

The switching theorem b032348c1a8a gives
  |F|>=(5/8)p-eta_v-O(1),
and only O(1) switchers lie outside the interior cell system, so
  s_int>=(5/8)p-eta_v-O(1).
This proves the one-eighth lower bound.

Finally 6205fe95ecf8 classifies every nonflat output. Branches (1),(2) are respectively strict rank rise and special rank-p output. In branch (4), h_i is nonspecial nonascending of rank p; its forward joint has potential at least p, while the two other vertices are last-vertex choices of the p-edge rotation supplied by 465568d6d8dc and therefore also have potential at least p. Hence all three vertices lie in V_{>=p}.
