# A factor-two edge-rank jump is a barrier to U_11 color-terminal collisions

## Statement

Let
v_0v_1...v_k
be a rainbow path in the terminal-pair graph whose parent hyperedges are ascending nonspecial edges in U_11, with nondecreasing edge ranks
r_1<=...<=r_k.

If for some t
r_{t+1}>=2r_t,
then no color-terminal collision x_i=v_j satisfies
j<t<i.
Equivalently, no collision interval crosses the cut between E_t and E_{t+1}.

## Body

Suppose x_i=v_j crossed the cut, so j<t<i. By monotonicity,
  r_{j+1}<=r_t
and
  r_i>=r_{t+1}.
By 5ba61d0a77eb, a U_11 collision satisfies
  r_i<=2r_{j+1}-1<=2r_t-1.
But r_{t+1}>=2r_t gives
  r_i>=2r_t,
a contradiction.
