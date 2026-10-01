# Clean-retained switchers satisfy three-quarters cell packing

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v. Let X be a family of ascending nonspecial terminal edges e={x,v,u}, e!=g_p, such that each e has exactly one off-v contact with P and that contact is its unique entrance x.

For R<p let X_{\le R}={e in X: phi(e)<=R}. Then, whenever X_{\le R} is nonempty,
  |X_{\le R}| <= (3/4)(2R-p-1)+3/2.                    (1)

Hence, if the X-ranks are ordered rho_1<=...<=rho_a,
  rho_i >= ceil((3p+4i-3)/6),                          (2)
and therefore
  sum_{i=1}^a phi(x_i)
  >= (p/2)a + a^2/3 - 7a/6.                           (3)

In particular, if X comprises (5/8-o(1))p switchers, then
  sum_{f in X}phi(x_f) >= (85/192-o(1))p^2.

Moreover, near equality in (1) has the unique period-four cell pattern
  (private+joint), private, empty, empty
up to cyclic phase: if
  Delta = (3/4)(2R-p-1)+3/2-|X_{\le R}|,
then all but at most 4Delta cell transitions lie on the corresponding critical four-cycle.

## Body

Use the central-window cell notation. For every eligible index k let P_k denote the private slot of g_k and J_k=g_k∩g_{k+1} the joint slot. Let o_k=1 if at least one of P_k,J_k is occupied by an edge of X_{\le R}, and o_k=0 otherwise.

The joint rule eac2e3da3eea gives
  J_k occupied => o_{k-1}=0.                           (4)

The quantitative separation theorem 65894e91ed50 gives a stronger private rule than the one used in 7e047fd40dd7. Suppose P_k is occupied by an edge f of rank r<=R<p. If cell k-2 contained any earlier single contact e, then part (a) of 65894e91ed50, with j=k-2, would give
  2=k-j >= p-r+3.
But r<=p, so the right side is at least 3, impossible. Hence
  P_k occupied => o_{k-2}=0.                           (5)

Thus only the binary occupancies of the two preceding cells matter. Use states
  A=(0,0), B=(0,1), C=(1,0), D=(1,1),
where the coordinates are (o_{k-1},o_{k-2}). Give them potentials
  psi(A)=0,
  psi(B)=-3/4,
  psi(C)=-5/4,
  psi(D)=-3/2.

The allowed transitions and their cell weights w are:
  A --empty,0--> A,
  A --private,1--> C,
  A --joint,1--> C,
  A --private+joint,2--> C,
  B --empty,0--> A,
  B --joint,1--> C,
  C --empty,0--> B,
  C --private,1--> D,
  D --empty,0--> B.

For every allowed transition s->t,
  w <= 3/4 + psi(s)-psi(t).                            (6)
This is checked directly from the displayed list.

Summing (6) through the N=2R-p-1 eligible cells and using that the potential range is 3/2 gives
  |X_{\le R}| <= 3N/4+3/2,
which is (1).

Taking R=rho_i in (1),
  i <= (3/4)(2rho_i-p-1)+3/2
    = (3/2)rho_i-(3/4)p+3/4.
Therefore
  6rho_i >= 3p+4i-3,
which proves (2).

Since X-edges are ascending, phi(x_i)=rho_i-1. Dropping only ceiling gains,
  sum_i phi(x_i)
  >= sum_{i=1}^a [(3p+4i-3)/6-1]
  = (p/2)a + a^2/3 - 7a/6,
proving (3).

If a=(5/8-o(1))p, the quadratic coefficient is
  5/16 + (1/3)(25/64)
  = 60/192+25/192
  = 85/192.

Finally define transition slack in (6). Direct inspection shows zero slack exactly on
  A --(private+joint;2)--> C,
  C --(private;1)--> D,
  D --(empty;0)--> B,
  B --(empty;0)--> A.
Every other allowed transition has slack at least 1/4. Thus total deficit Delta permits at most 4Delta noncritical transitions, and between them the cell pattern is forced to repeat
  (private+joint), private, empty, empty
up to phase.
