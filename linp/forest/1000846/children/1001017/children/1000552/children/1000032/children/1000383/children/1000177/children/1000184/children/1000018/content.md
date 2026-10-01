# At the half-rank top boundary every high competitor has a visible entrance

## Statement

Assume the top-boundary q,(q+1)^3 configuration of 28445330afcc:
  phi(v)=2q-2,
  P=(g_1,...,g_{2q-2})
is a maximum path ending physically at v,
  e={x,v,u}
has rank q with universal entrance
  x=g_{q-1}∩g_q,
and h is one of the rank-(q+1) charged competitors through v.

Then the unique entrance of h lies on P. Consequently the three high-edge entrances are three distinct vertices among
  a=g_{q-2}∩g_{q-1},
  b=private(g_{q-1}),
  c=private(g_q),
  d=g_q∩g_{q+1}.
In particular each of these three selected witnesses has endpoint potential exactly q.

## Body

Suppose the entrance y of h={y,v,z} is absent from P. By 28445330afcc the selected path-relative witness z is then the opposite terminal and must equal a or b.

Consider the reversed suffix
  h,g_{2q-2},g_{2q-3},...,g_q.
The edge h meets g_{2q-2} at v. Its only other vertex on P is z, but z lies in g_{q-2}∪g_{q-1}, outside the retained suffix g_q,...,g_{2q-2}; the entrance y is absent from P. Hence h has no other contact with the retained suffix. The reversed suffix itself is a linear path.

The displayed sequence therefore is a linear path of length
  1+[(2q-2)-q+1]=q.
Its last edge is g_q. Since g_{q-1} has been omitted, the central joint
  x=g_{q-1}∩g_q
occurs only in the last edge of the displayed path and is a physical last vertex. Thus
  phi(x)>=q.

But e is ascending of rank q with unique entrance x, so
  phi(x)=q-1,
a contradiction.

Therefore every high competitor has its entrance on P. The four-slot localization and distinctness from 28445330afcc then show that the three entrances occupy three distinct elements of {a,b,c,d}. Ascendingness of each rank-(q+1) edge gives entrance potential q.
