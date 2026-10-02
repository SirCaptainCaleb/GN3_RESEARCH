# Signed carrier-chain identity for a spanning path

## Statement

In the t=1 signed-projective normal form dd9129917320, suppose a spanning linear path exists. Let Q=PG(n-2,2) be the quotient on the carrier pairs G_x. Let y in F_2^{Lines(Q)} record, for each quotient line L, the parity of the number of selected cross blocks of the path supported on L. Let p in F_2^{Points(Q)} record, for each x, the parity of the number of path joints lying in G_x. Then A_Q y=p, where A_Q is the point-line incidence matrix of Q. If sigma is the line-signing and j_infinity is 1 when infinity is a path joint and 0 otherwise, then <sigma,y> = j_infinity + sum b over all path joints (x,b), modulo 2.

## Body

For a carrier pair G_x={(x,0),(x,1)}, let v_x be 1 if the vertical block {infinity,(x,0),(x,1)} is selected by the path and 0 otherwise. Each actual point (x,b) is incident with exactly 1+j_{x,b} selected path edges, where j_{x,b} is its joint indicator. Removing the vertical contribution, the parity of the number of selected cross-block incidences at G_x is
(1+j_{x,0}-v_x)+(1+j_{x,1}-v_x) = j_{x,0}+j_{x,1} (mod 2).
On the other hand this is exactly the x-coordinate of A_Q y, since every selected cross block on a quotient line through x contributes one incidence and y records line multiplicity mod 2. Hence A_Q y=p.

For the signed identity, every selected cross block on a quotient line L={x_1,x_2,x_3} satisfies b_1+b_2+b_3=sigma(L). Summing over all selected cross blocks gives <sigma,y> on the left. On the right, summing the b-coordinates of cross incidences group by group leaves, modulo 2, 1+j_{x,1}-v_x from G_x. Since Q has 2^{n-1}-1 points, its number of points is odd, so summing the constant 1 gives 1. Thus
<sigma,y> = 1 + sum_x j_{x,1} + sum_x v_x.
Only vertical blocks contain infinity, so sum_x v_x is the number of selected path edges through infinity, namely 1+j_infinity. Therefore the two constants cancel and
<sigma,y> = j_infinity + sum_x j_{x,1}.

Under swapping the bit labels in any carrier pair G_x, sigma is toggled on every quotient line through x while the bit of every joint in G_x is toggled; because A_Q y=p, both sides change by the same amount. Hence the identity is switching-invariant.