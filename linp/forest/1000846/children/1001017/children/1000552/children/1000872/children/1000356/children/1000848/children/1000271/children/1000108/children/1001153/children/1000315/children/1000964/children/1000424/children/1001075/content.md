# The flat low-terminal branch is theta-or-terminal-central

## Statement

In the surviving one-low odd-boundary 0-1-1 state with flat opposite terminal phi(C)=phi(v)=2q-3, the reciprocal C-path has only two structural types. If its sole low-edge contact is the source x, then the C-path and the clean x-source rail share at least two vertices and hence contain a lens. Otherwise the sole contact is terminal v at the forced central joint r_{q-2}∩r_{q-1}. Thus the flat branch reduces to a theta branch and one symmetric terminal-terminal branch.

## Body

Retain the surviving one-low odd-boundary 0-1-1 state with
  e={x,v,C},
  phi(e)=q,
  phi(v)=phi(C)=p=2q-3,
where e is assigned at v, C is the sole contact of e on the chosen v-path, and the source incidence at x is clean.

Let
  Q_x
be the chosen maximum source path ending physically at x. Then |Q_x|=q-1 and, by source cleanness, Q_x avoids both terminals v,C.

Let
  R=(r_1,...,r_p)
be the chosen maximum C-ending path. By 436d55f14de2, because phi(C)=2q-3 and mu_C(e)=1, exactly one of the following holds:
(T) the sole e-contact on R is the terminal
      v=r_{q-2} cap r_{q-1},
    while x is absent;
(X) the sole e-contact is the source x, lying in one of
      r_{q-2} cap r_{q-1},
      private(r_{q-1}),
      r_{q-1} cap r_q,
    while v is absent.

In case (X), R and Q_x share at least two vertices.
Indeed x belongs to both paths and is the physical endpoint of Q_x. If x were their unique common vertex, the universal unique-intersection theorem 5854d853a44b would force x to be a path joint on Q_x. But a physical endpoint of Q_x is not a joint. Contradiction.

Therefore every source-contact reciprocal state (X) produces a genuine two-vertex overlap between the long C-path and the clean source rail Q_x. Choosing consecutive common vertices gives an elementary lens; if internal to both paths it is balanced by 390e818020e1.

The only reciprocal flat state not automatically producing such a theta is (T):
  v=r_{q-2} cap r_{q-1}
on the chosen C-path, with x absent.
