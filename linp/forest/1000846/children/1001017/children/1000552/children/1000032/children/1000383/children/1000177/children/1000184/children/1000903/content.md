# Right-side high entrances obey a conditional left-prefix recoil and unconditional low-rail crossing

## Statement

In the top-boundary q,(q+1)^3 setting of 28445330afcc, let P=(g_1,...,g_{2q-2}) end at v with last vertex v, let e={x,v,u} be the rank-q edge with x=g_{q-1}∩g_q, and let h={y,v,z} be a rank-(q+1) charged competitor whose selected witness is a right slot y∈{c,d}. Then y is the unique entrance of h and phi(y)=q.

Moreover, if the low edge e has no second contact with the prefix P^-=(g_1,...,g_{q-1}) besides x, then z lies in V(P^-). Unconditionally, h meets every canonical (q-1)-edge entrance rail for e; on any such rail avoiding y, the forced contact is z.

## Body

The first assertion is 28445330afcc: right-slot witnesses c,d can only be unique entrances. Since h has rank q+1 and is ascending, phi(y)=q.

Assume now that e meets the prefix P^- only at x. If z were also absent from P^-, then
  g_1,...,g_{q-1},e,h
would be a (q+1)-edge linear path. Indeed e meets the prefix only at x, e∩h={v}, the entrance y of h lies to the right of the central cut and hence outside P^-, and z is absent by assumption. The last edge h can have y as a last vertex, giving phi(y)>=q+1, contradiction. Hence z lies in P^-.

For the unconditional rail statement, let R be any canonical (q-1)-edge entrance path for e, ending at x and avoiding the terminals v,u. By 7c02145677de every rank-(q+1) nonspecial competitor h through terminal v meets R. If y is absent from R, then the only possible non-v contact of h with R is z, so z∈V(R). If y lies on R, no conclusion about z follows from this argument.

Thus the displayed-prefix recoil requires the explicit clean-prefix hypothesis; the canonical-rail crossing is unconditional.