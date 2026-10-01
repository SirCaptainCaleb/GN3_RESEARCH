# A 0-1-1 low edge at the odd boundary is reciprocally central on its other terminal path

## Statement

Let e={x,v,u} be a 0-1-1 ascending edge of rank q>=4, assigned to terminal v with phi(v)=2q-3 and phi(u)>=phi(v). Then phi(u) is 2q-3 or 2q-2. On the chosen maximum u-ending path, if phi(u)=2q-2 the sole e-contact is necessarily x at the unique central joint. If phi(u)=2q-3, either the sole contact is v at joint r_{q-2}∩r_{q-1}, or it is x in one of the three central slots around r_{q-1}.

## Body

Let e={x,v,u} be a 0-1-1 ascending nonspecial edge of rank q>=4, with unique entrance x. Assume
  phi(v)=2q-3
and e is assigned to v as a minimum-potential terminal. Suppose, as in the surviving one-low odd-boundary state, that the opposite terminal u satisfies phi(u)>=phi(v).

By the 0-1-1 terminal-potential bound ceef20074f6f,
  q <= phi(u) <= 2q-2.
Since phi(u)>=2q-3,
  phi(u) in {2q-3,2q-2}.                              (1)

Let
  R=(r_1,...,r_s),  s=phi(u),
be the globally chosen maximum endpoint path ending physically at u. Because mu_u(e)=1 and s>q, e cannot be the last edge of R. Hence exactly one of x,v lies in V(R) outside its last edge.

Case A: the unique e-contact on R is the terminal v, so x is absent.

If v is private to r_i, terminal-tail localization gives
  i>=s-q+2,
while the wrong-entrance prefix
  r_1,...,r_i,e
must have length at most q-1, so i<=q-2.
For s>=2q-3 this is impossible.

If v=r_i cap r_{i+1} is a joint, terminal-tail localization gives
  i>=s-q+1,
and the same wrong-entrance prefix through r_i gives i<=q-2.
Thus:
- if s=2q-2, i>=q-1, impossible;
- if s=2q-3, necessarily i=q-2.
So terminal-only contact is possible only when
  s=2q-3
and
  v=r_{q-2} cap r_{q-1}.                              (2)

Case B: the unique e-contact is the entrance x, so v is absent.

First-contact localization 813f5b668319 gives first-index at most q-1.
Terminal-tail localization at terminal u forces the unique {x,v}-contact into the final q-2 precursor band.

If x is private to r_i, the tail bound gives
  i>=s-q+2.
Thus:
- for s=2q-2, i>=q, contradicting i<=q-1;
- for s=2q-3, i=q-1.

If x=r_i cap r_{i+1} is a joint, the tail bound gives
  i>=s-q+1,
while first-contact localization gives i<=q-1.
Thus:
- for s=2q-2, i=q-1;
- for s=2q-3, i in {q-2,q-1}.

Combining:
- if phi(u)=2q-2, the unique contact is necessarily the entrance
    x=r_{q-1} cap r_q;
- if phi(u)=2q-3, either
    v=r_{q-2} cap r_{q-1},
  or x is one of
    r_{q-2} cap r_{q-1},
    private(r_{q-1}),
    r_{q-1} cap r_q.

This is a reciprocal central normal form forced solely by the 0-1-1 signature.
