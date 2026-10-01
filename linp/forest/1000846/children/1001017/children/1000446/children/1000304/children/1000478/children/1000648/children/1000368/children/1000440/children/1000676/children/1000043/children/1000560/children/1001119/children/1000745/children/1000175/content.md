# Canonical p=5 entrance paths satisfy two simultaneous two-point transversals

## Statement

In the p=5 charged pattern (4,4,4,5), retain the notation
  f_b={b,v,u_b},  f_c={c,v,u_c},  e5={d,v,w}.
Let R_b be any canonical three-edge entrance path for f_b, so R_b ends at b and avoids v,u_b. Then R_b meets both
  e5 and f_c.
Consequently
  V(R_b)∩{d,w} != empty
and
  V(R_b)∩{c,u_c} != empty.

Symmetrically, every canonical entrance path R_c for f_c satisfies
  V(R_c)∩{d,w} != empty
and
  V(R_c)∩{b,u_b} != empty.

## Body

The intersection with e5 was proved in a6058546bd92.

It remains to prove that R_b meets f_c. Suppose instead that R_b is disjoint from f_c.

By definition of the canonical entrance path for f_b, the concatenation
  R_b,f_b
is a four-edge linear path ending in f_b through its unique entrance b, and R_b avoids the two terminals v,u_b. Thus f_b meets R_b only at b.

The distinct charged edges f_b and f_c both contain v, and by linearity
  f_b∩f_c={v}.
Since R_b is assumed disjoint from f_c, the concatenation
  R_b,f_b,f_c
is therefore a five-edge linear path.

But f_c has edge rank four. This five-edge path ends in f_c, contradicting phi(f_c)=4.

Hence R_b meets f_c. Since R_b avoids v, and
  f_c={c,v,u_c},
the contact lies in {c,u_c}.

Thus every R_b meets both {d,w}⊂e5 and {c,u_c}⊂f_c.

The argument with b and c interchanged proves the symmetric statement for every canonical R_c.