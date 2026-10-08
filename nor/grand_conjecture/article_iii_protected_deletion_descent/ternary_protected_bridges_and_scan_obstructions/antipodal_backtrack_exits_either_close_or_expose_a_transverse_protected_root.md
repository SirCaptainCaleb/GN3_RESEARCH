# Antipodal backtrack exits either close or expose a transverse protected root

## Composition

(none yet)

## Development


In the audited flat d=e=3 antipodal backtrack, use local order ...q,r,a,b,y,c,d,e,f... with x omitted, old statuses 0,0,1,1,1,1,1, and x-bridge alpha(a,b,x)=alpha(b,x,c)=alpha(x,c,d)=0.

Left exit: ...q,r,x,a,b,y,c,d,e,f...
Its protected interior is 0,1,1,1,... . Let f=alpha(q,r,x), g=alpha(r,x,a). All coordinates to the right retain their order; only f,g are uncertain. If f=g=0, the full order is one-change. Otherwise there is a protected 10 descent. If g=1 it is g -> alpha(x,a,b)=0, with root e_r-e_b. If g=0 and f=1 it is f -> g, with root e_q-e_a. These roots use neither x nor y, so they are nonzero modulo the inert root line <e_x-e_y>.

Right exit: ...q,r,a,b,x,c,d,y,e,f...
Its protected interior is 0,0,0,1. Let h=alpha(d,y,e), k=alpha(y,e,f). All coordinates to the left retain their order; only h,k are uncertain. If h=k=1, the full order is one-change. Otherwise there is a protected 10 descent: if h=0, alpha(c,d,y)=1 -> h=0 gives root e_c-e_e; if h=1 and k=0, h -> k gives root e_d-e_f. Again the root survives modulo <e_x-e_y>. Under reversal this is the same strict protected-cut situation as the left exit.

Thus each canonical exit preserves the outside order on its protected side and either closes NOR or produces an explicit transverse protected root. In particular the g=1 branch canonically yields e_r-e_b while leaving the entire right suffix untouched.

The remaining flat-sector task is to show that a minimum protected-root carrier cannot indefinitely replace an antipodal root pair by such transverse exit roots without a strict carrier/codimension descent.
