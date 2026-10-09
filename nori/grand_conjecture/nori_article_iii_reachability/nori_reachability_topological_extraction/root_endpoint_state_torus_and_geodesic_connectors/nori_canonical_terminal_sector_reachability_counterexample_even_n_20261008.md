# Parity edge coloring defeats all canonical monochromatic terminal orthants

# Counterexample to extraction from canonical all-final-edge monochromatic sectors

Consider the **edge** analogue in even dimension n>=4. Define the undirected edge color in direction i by
c_i(x)=sum_{j!=i} x_j mod 2.
It is well-defined on the undirected edge because it is independent of x_i. Since n-1 is odd, c_i(bar x)=1-c_i(x), so the coloring is antipodally odd.

In the root-endpoint torus, for the antipodal endpoint state a_x=(x,bar x), the unique q-terminal orthant whose n final incoming cover edges all have color q has diagonal root
(z_q(x))_i=x_i XOR 1 XOR c_i(x) XOR q.
Writing P(x)=sum_j x_j mod2 gives
(z_q(x))_i=1 XOR P(x) XOR q
for every i. Thus z_q(x) is always **one of the two constant vertices** 0^n,1^n, regardless of x.

Every monochromatic geodesic starting at 0^n or 1^n has length at most one: at a constant vertex t^n its first edge has color t (since n-1 is odd), and after that first coordinate flip, every edge in a different direction has color 1-t. If q != t, it cannot even begin in color q.

A q-monochromatic path through diagonal root z_q(x) and joining antipodal endpoints x,bar x would require q-monochromatic geodesics from z_q(x) to **both** x and bar x. Their distances sum n>=4, so one branch has length>=2; this contradicts the previous paragraph. Hence for every antipodal pair and both colors, NEITHER canonical all-terminal-edge sector admits a monochromatic directed connector.

Nevertheless the coloring has monochromatic antipodal geodesics. For any permutation p, choose starting root x with x_(p_k)=(k-1) mod2 (alternating initial bits). Then each traversed edge at step k has color
P(x) XOR (k-1 mod2) XOR x_(p_k)=P(x),
constant. (The alternating root has n/2 ones.) This exhibits a full monochromatic geodesic.

**Conclusion.** Existence of a full monochromatic antipodal geodesic cannot be strengthened to existence inside one of the two uniquely selected top-rank orthants where *all* final cover colors agree. The local sphere and its complementary canonical terminal-root labels are genuine, but the implication from local monochromatic stars to jointly realizable directed geodesic connectors is false even for this highly structured affine parity coloring. Successful Tucker/Sperner extraction must retain multiple orthants and/or longer-prefix reachability information. The counterexample applies in all even dimensions n>=4, so additional small-order tests of this restricted canonical-sector principle are unnecessary. This does not refute the grand ordered-three-face NORI conjecture.
