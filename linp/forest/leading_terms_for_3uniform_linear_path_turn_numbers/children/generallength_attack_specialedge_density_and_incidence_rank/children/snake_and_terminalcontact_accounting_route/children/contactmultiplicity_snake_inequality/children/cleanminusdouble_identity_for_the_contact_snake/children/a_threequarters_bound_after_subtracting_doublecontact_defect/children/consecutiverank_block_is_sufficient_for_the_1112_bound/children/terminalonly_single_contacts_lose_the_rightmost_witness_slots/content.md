# At the odd central boundary terminal-only single contacts lose the rightmost witness slots

## Statement

Let v have p=phi(v)=2q-3, q>=3, and let
  P=(g_1,...,g_p)
be a maximum path ending at v.

Let e={x,v,u} be a potential-charged ascending nonspecial edge assigned to v, assume e is not double on P, and suppose its unique P-contact outside the last edge is the opposite terminal u while its entrance x is absent.

If phi(e)=q, then
  u=g_{q-2}∩g_{q-1}.

If phi(e)=q+1, then:
- if u is private to g_i, q-2<=i<=q-1;
- if u=g_i∩g_{i+1}, q-3<=i<=q-1.

In particular a terminal-only rank-(q+1) single contact cannot occupy private(g_q) or the joint g_q∩g_{q+1}; those rightmost witness slots are entrance-only.

## Body

Let s=phi(e). Since x is absent, the terminal-tail localization gives the usual lower bounds:
- if u is private to g_i, then i>=p-s+2;
- if u is the joint g_i∩g_{i+1}, then i>=p-s+1.

For the upper bound, truncate P at the first edge containing u. If u is private to g_i, then
  g_1,...,g_i,e
is a linear path of length i+1 ending in e through terminal u. Since e is nonspecial with unique longest entrance x, a path entering e through u cannot have length s: length s would give a second longest entrance label, while a larger length would exceed phi(e)=s. Hence
  i+1<=s-1,
so
  i<=s-2.

If u is the joint g_i∩g_{i+1}, use the prefix only through g_i; again
  g_1,...,g_i,e
is linear, has length i+1, and enters e through terminal u. Thus the same argument gives
  i<=s-2.

Now substitute p=2q-3.

For s=q:
- private contacts would require
    i>=p-q+2=q-1
  and
    i<=q-2,
  impossible;
- joint contacts require
    i>=p-q+1=q-2
  and
    i<=q-2.
Thus the unique possibility is
  u=g_{q-2}∩g_{q-1}.

For s=q+1:
- private contacts satisfy
    i>=p-(q+1)+2=q-2
  and
    i<=q-1;
- joint contacts satisfy
    i>=p-(q+1)+1=q-3
  and
    i<=q-1.
This is exactly the asserted window.