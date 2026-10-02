# An interior U_11 color-terminal collision forces adjacent edge-rank sum at least the colliding rank plus two

## Statement

In the setting of 3216d2e9afcd, every interior color-terminal collision x_i=v_j satisfies
  r_j >= ceil((r_i+1)/2),
  r_{j+1} >= ceil((2r_i+3)/4),
and therefore
  r_j+r_{j+1} >= r_i+2.

Equivalently,
  r_i-r_{j+1} <= r_j-2.

## Body

Apply the certified path-relative central-window packing theorem 220a14637b5f to the two distinct ascending nonspecial edges
  E_j,E_{j+1}
terminal at the common vertex x_i=v_j, using the chosen maximum path R_i with last vertex x_i.

The host path has length
  p=phi(x_i)=r_i-1.
By c9a012c1b82e both adjacent edge ranks are at most r_i-1=p, and by monotonicity
  r_j<=r_{j+1}.
The ordered-rank conclusion of 220a14637b5f for k=2 gives
  r_j >= ceil((2p+1+3)/4)
      = ceil((r_i+1)/2),
and
  r_{j+1} >= ceil((2p+2+3)/4)
            = ceil((2r_i+3)/4).

If r_i=2m, these lower bounds are m+1 and m+1; if r_i=2m+1, they are m+1 and m+2. In both cases their sum is at least r_i+2. Rearrangement gives the equivalent gap inequality.