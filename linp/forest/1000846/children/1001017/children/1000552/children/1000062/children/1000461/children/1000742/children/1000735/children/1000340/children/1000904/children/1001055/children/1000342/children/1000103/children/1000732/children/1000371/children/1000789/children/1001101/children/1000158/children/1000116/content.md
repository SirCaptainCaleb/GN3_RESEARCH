# Lens-free global one-eighth paid switching mass

## Statement

Let (H_j) satisfy
  S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
  |E(H_j)| >= (43/48)S_j-o(S_j).
For every active misaligned vertex v use the lens-free common-anchor switching family from f3588b3a3bc7 and let D_v^cell,Y_v be the corresponding local certificate counts from 614c7d2d181a.

Then
  sum_v (D_v^cell+Y_v) >= (1/8-o(1))S_j.

Every D-unit is represented by a doubly occupied switching cell and hence a linear switcher triangle. Every Y-unit is represented by a paid switching cell whose output is in one of the nonflat progress branches of 6205fe95ecf8.

Thus the global one-eighth paid progress-or-obstruction mass survives on a lens-free dependency chain.

## Body

By the lens-free near-extremal stability theorem 223efeb00c7b,
  sum_v eta_v=o(S),
and active misaligned vertices carry total endpoint-potential mass
  S-o(S).
Bounded-p vertices contribute O(n_+)=o(S).

For every remaining active misaligned vertex v, the local payment theorem 614c7d2d181a gives
  D_v^cell+Y_v >= p_v/8-eta_v-O(1).
Summing,
  sum_v(D_v^cell+Y_v)
  >= (1/8)sum_{v active misaligned} p_v
       -sum_v eta_v-O(n_+)
  =(1/8-o(1))S.

The triangle and paid-output interpretations are inherited from the exact lens-free D+Y theorem 9a6be27912e0.
