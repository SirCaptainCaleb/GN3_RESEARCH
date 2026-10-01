# One-eighth payment is exactly internal superlevel edges or switcher triangles

## Statement

In the setting of 9586a4d2317f, put
  V_p={w:phi(w)>=p}.
For each occupied interior cell C_i let h_i=g_{i+2} be its rotation-output edge, and let I_p be the number of occupied cells for which
  V(h_i) subset V_p.
Let D be the number of doubly occupied cells.

Then
  D+I_p >= s_int-ceil((p-3)/2).

For the switching family at an active misaligned p-center,
  D+I_p >= p/8-eta_v-O(1).

Thus the arbitrary-p one-eighth payment theorem has an exact potential-cut form: every dangerous center forces either a switcher triangle or a distinct output edge lying wholly inside its own potential superlevel H[V_p].

## Body

Every rotation output h_i has rank at least p by 6205fe95ecf8.

Apply the potential-cut classification 321022a601f7 at threshold p. If phi(h_i)>p then every vertex of h_i lies in V_p. If phi(h_i)=p, then h_i fails to lie wholly in V_p exactly when it is ascending nonspecial with unique entrance of potential p-1. This is precisely the unpaid branch (3) of 6205fe95ecf8. Therefore
  h_i subset V_p
if and only if C_i is paid in the terminology of 9586a4d2317f.

Hence I_p equals the paid-cell count Y in that theorem. Its exact cell inequality gives
  D+I_p=D+Y>=s_int-ceil((p-3)/2).

For the switching family from b032348c1a8a,
  s_int>=(5/8)p-eta_v-O(1),
so
  D+I_p>=p/8-eta_v-O(1).
Distinct occupied cells have distinct output edges, so the I_p term counts genuinely distinct edges of the induced superlevel hypergraph H[V_p] on the chosen host path.
