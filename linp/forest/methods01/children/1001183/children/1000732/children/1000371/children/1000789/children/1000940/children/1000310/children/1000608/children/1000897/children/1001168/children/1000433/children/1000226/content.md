# Every interior U_11 color-terminal collision closes a local linear cycle, including the last-edge boundary

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path whose parent hyperedges E_s={x_s,v_{s-1},v_s} belong to U_11 and have nondecreasing edge ranks r_s=phi(E_s). Let x_i=v_j be an interior color-terminal collision. Let R_i=(g_1,...,g_p) be the chosen maximum source path ending at x_i, where p=r_i-1, and put h=g_p.

For every F in {E_j,E_{j+1}} with F!=h, let c_F be the exact off-x_i contact supplied by 608468bb403b.

If neither adjacent parent equals h, then E_j together with the R_i-segment between c_{E_j},c_{E_{j+1}} and E_{j+1} is a linear cycle; if that host segment has d edges, then d+2<=r_j.

If E_{j+1}=h, let b be the last index of an R_i-edge containing c_{E_j}. Then E_j,g_b,...,g_p is a linear cycle of length p-b+2<=r_j. If E_j=h, the symmetric statement holds with E_{j+1}.

Thus every interior U_11 color-terminal collision closes a local linear cycle; at the host-last-edge boundary the cycle is closed by the single adjacent parent having a genuine off-x_i contact.

## Body

By 608468bb403b, at most one of E_j,E_{j+1} equals h. Every adjacent parent F distinct from h has an exact intersection F∩V(R_i)={x_i,c_F}, with c_F outside h.

If neither adjacent parent is h, the two exact contacts are distinct by linearity. The host segment between them avoids x_i; each parent meets that segment only at its designated contact, while E_j∩E_{j+1}={x_i}. Hence E_j, the host segment, and E_{j+1} form a linear cycle. Since E_j and E_{j+1} are nonspecial, f2925a904b8e bounds the cycle length by both adjacent edge ranks, giving d+2<=r_j.

Suppose E_{j+1}=h. Then E_j!=h and has exact contact c=c_{E_j}. Let b be the last index of an R_i-edge containing c. Since E_j and h already meet at x_i, linearity implies c is not in h, so b<=p-1. The edge sequence g_b,...,g_p is a linear path whose endpoint vertices include c and x_i. Exactness gives that E_j meets this segment exactly at c and x_i. Therefore E_j,g_b,...,g_p is a linear cycle of length p-b+2. As E_j is nonspecial, f2925a904b8e gives p-b+2<=r_j.

The case E_j=h is symmetric, using the exact contact of E_{j+1}.