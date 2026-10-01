# U_11 color-terminal collisions are confined to one factor-two edge-rank scale

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges with nondecreasing edge ranks r_1<=...<=r_k. Suppose x_i=v_j is a color-terminal collision. If F is either parent edge incident with v_j (that is, F=E_{j+1}, and also F=E_j when j>=1), then

ceil((r_i+1)/2) <= phi(F) <= r_i-1.

Equivalently, r_i <= 2phi(F)-1. Thus a color-terminal collision cannot jump backward to a path location whose incident parent-edge rank is less than half the colliding edge rank.

## Body

Because E_i is ascending with unique entrance x_i,
  phi(x_i)=r_i-1.
At the collision x_i=v_j this gives
  phi(v_j)=r_i-1.

Let F be a parent edge incident with v_j and put s=phi(F). The vertex v_j is a terminal of F. By the certified terminal-rank bound a7b7670e955a applied to the ascending nonspecial edge F,
  phi(v_j)<=2s-2.
Hence
  r_i-1<=2s-2,
so
  s>=ceil((r_i+1)/2),
equivalently r_i<=2s-1.

For the upper bound, c9a012c1b82e gives that every terminal-path edge incident with the hit vertex v_j has rank at most r_i-1. Therefore
  s<=r_i-1.

Combining the two inequalities proves the claim. No contact-multiplicity or exact-contact assertion is used.
