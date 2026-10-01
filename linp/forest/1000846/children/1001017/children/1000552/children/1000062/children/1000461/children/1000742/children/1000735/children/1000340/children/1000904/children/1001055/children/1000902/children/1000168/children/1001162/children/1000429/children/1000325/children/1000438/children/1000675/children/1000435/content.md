# Lens-free one-eighth local payment at low-defect misaligned centers

## Statement

Let v be an active misaligned vertex with p=phi(v)>=8, local defect eta_v, chosen maximum p-edge path P_v, and a maximum-rank ascending terminal anchor with edge rank q<p. Let F_v be the anchor-double / host-single switching family supplied by the lens-free dense switching theorem f3588b3a3bc7.

Restrict to switching contacts in the interior cells of P_v. Let D_v^cell be the number of doubly occupied interior cells and Y_v the number of paid occupied cells in the sense of the lens-free exact D+Y theorem 9a6be27912e0.

Then
  D_v^cell+Y_v >= p/8-eta_v-O(1).

More precisely,
  D_v^cell+Y_v
  >= beta(p)-eta_v-a(q)-ceil((p-3)/2)-O(1),
where beta(p)=floor((11p-16)/8) and a(q)=ceil((3q-4)/4).

Thus every low-defect active misaligned p-center carries at least p/8-o(p) selected local payment units, each represented by either a switcher triangle or a paid rotation-output cell.

## Body

By f3588b3a3bc7,
  |F_v|>=beta(p)-eta_v-a(q).
Only O(1) members can have their unique P_v-contact in the boundary positions outside the interior cells C_i, 1<=i<=p-3. Therefore
  s_int>=beta(p)-eta_v-a(q)-O(1).

Apply the exact D+Y payment theorem 9a6be27912e0:
  D_v^cell+Y_v
  >=s_int-ceil((p-3)/2)
  >=beta(p)-eta_v-a(q)-ceil((p-3)/2)-O(1).

Since v is misaligned, q<=p-1 and a is increasing. Hence
  D_v^cell+Y_v
  >=beta(p)-a(p-1)-ceil((p-3)/2)-eta_v-O(1).

Using
  beta(p)=(11/8)p+O(1),
  a(p-1)=(3/4)p+O(1),
  ceil((p-3)/2)=(1/2)p+O(1),
the coefficient is
  11/8-3/4-1/2 = 1/8,
so
  D_v^cell+Y_v>=p/8-eta_v-O(1).

The structural interpretation of D and Y is exactly that of 9a6be27912e0. No endpoint-lens assertion is used.
