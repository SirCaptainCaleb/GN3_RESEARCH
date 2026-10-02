# Every interior U_11 color-terminal collision has rank-sum surplus, a local 3-cycle, or an explicit last-edge boundary cycle

## Statement

Retain the setting of 3216d2e9afcd. For an interior color-terminal collision x_i=v_j, let R_i=(g_1,...,g_p), p=r_i-1, be the chosen maximum source path and h=g_p its last edge. At least one of the following holds:

(1) r_j+r_{j+1}>=r_i+3;

(2) some edge g of R_i together with E_j,E_{j+1} forms a linear 3-cycle;

(3) one of E_j,E_{j+1} equals h. The other adjacent parent F has a genuine exact off-x_i contact and, together with the terminal host segment from that contact to x_i, forms the boundary cycle of 3216d2e9afcd.

If neither adjacent parent equals h, only (1) and (2) are possible. Hence away from the explicit last-edge boundary, the universal lower bound r_j+r_{j+1}>=r_i+2 can be tight only in the local-3-cycle case.

## Body

If one of E_j,E_{j+1} equals h, alternative (3) is exactly the boundary case of 3216d2e9afcd.

Assume neither adjacent parent equals h. By 608468bb403b both have genuine distinct exact contacts c_j,c_{j+1} on R_i. If their path-edge occurrence intervals are disjoint, order them from earlier to later and apply 2cc651f9fa5d on the maximum p-edge path R_i. Since p=r_i-1,
  r_j+r_{j+1}>=p+4=r_i+3.

If the occurrence intervals overlap, one path edge g contains both contacts. Exactness gives g∩E_j={c_j} and g∩E_{j+1}={c_{j+1}}, while E_j∩E_{j+1}={x_i}. These three intersection vertices are distinct, so g,E_j,E_{j+1} form a linear 3-cycle.

Thus the old two-way dichotomy remains valid exactly off the last-edge boundary, while the boundary itself is recorded as the controlled cycle alternative (3).