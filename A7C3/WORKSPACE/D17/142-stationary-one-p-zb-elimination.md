# The Z-to-B incoming placement already two-covers H

**Workspace:** D17
**State:** established
**Key:** `stationary-one-p-zb-elimination`

**Summary:** In the quiet c=2,d=1,tau_Z=1 incoming one-p cell, suppose B enters the non-p A block V and the remaining Z-cross is incident with B. The quotient orientation is necessarily Z-B-V | U-p. The current Z-B seam, together with the two historical stationary source ends u_X-Z and B-u_Y, gives the literal tight path u_X-Z-B-u_Y. Its vertex complement is exactly A+p, Hamiltonian in the final-gap order K_A. Hence K_A | (u_X-Z-B-u_Y) is a spanning two-cover of H. Combined with the preceding incoming reductions, the unique direct quiet survivor is B-V-Z | U-p.


### Setup
Retain `stationary-one-p-incoming-partial-consumer`. Thus, outside its explicit R435/R542 alternatives and the eliminated Z-U placement, p is terminal in the current A block U, B enters the other A block V, and the lone remaining Z-cross is incident with either B or V. The full B and Z blocks have their retained quiet orders, and

  K_A=(a_1,...,a_{k-2},p,a_{k-1})

is Hamiltonian on A union {p}.

### The Z-B orientation is forced
Assume the remaining Z-cross is incident with B. Since the unique A-B seam is oriented B -> V, B already uses its outgoing interclass incidence toward V. A path component cannot give the full B block a second outgoing interclass incidence. Therefore the Z-B cross enters B, and the quotient rail is

  Z -> B -> V,

while the other current rail is U -> p.

### Historical ends complete the Z-B rail
The two stationary source orders retain literal tight paths

  u_X -> Z,
  B -> u_Y.

The current cover supplies the complete Z-to-B junction window because the full retained-order Z and B blocks are consecutive on one actual tight rail. Consequently

  Q=(u_X, Z, B, u_Y)

is a tight path. More explicitly, prepending u_X changes only the initial Z turn, already certified by the historical X-source; appending u_Y changes only the terminal B turn, already certified by the historical Y-source; every turn internal to Z or B is retained; and the two turns straddling the Z-B junction are selected turns of the current cover.

The path Q uses exactly u_X, all of Z, all of B, and u_Y. Its vertex complement in H is A union {p}, which is exactly the support of K_A. Hence

  K_A | Q

is a spanning two-path cover of H, contradiction.

### Consequence
The Z-B incoming placement is impossible outright. Combining this with `stationary-one-p-incoming-partial-consumer`, the only direct quiet `c=2,d=1,tau_Z=1` one-fragmented-petal survivor is the exact oriented block skeleton

  B -> V -> Z  |  U -> p.

Its Z-bearing rail has order

  |B|+|V|+|Z| = 2k+|V|-1 >= 2k,

so it is precisely the oversized-Z cell not covered by the balanced full-Z insertion argument. This reduction uses an actual spanning two-cover and no packet payment.

Status: complete internal deduction, unreviewed exposition. It does not consume the final B-V-Z | U-p skeleton and does not alter the separate exceptional fragmented-Z, tau_Z=2, c>2, R435, R542, or nonstationary recurrence branches.

