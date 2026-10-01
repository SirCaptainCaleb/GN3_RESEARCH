# High 0-1-1 edges at the odd boundary have reciprocal central-gate normal forms

## Statement

Let h={y,v,z} be a 0-1-1 ascending edge of rank q+1 with q>=5, phi(v)=2q-3 and phi(z)>=phi(v). Then phi(z) is one of 2q-3,2q-2,2q-1,2q. On the chosen maximum z-path, the sole h-contact is forced into an explicit central window. At phi(z)=2q the source y is the unique central joint; at 2q-1 either y lies in the three central slots or v is the central joint; at 2q-2 and 2q-3 the contact lies in the corresponding five- or seven-slot central window.

## Body

Let h={y,v,z} be a 0-1-1 ascending nonspecial edge of rank q+1, q>=5, with
  phi(y)=q,
  phi(v)=2q-3,
  phi(z)=t>=2q-3,
and suppose h is assigned to v, so phi(z)>=phi(v).

By the 0-1-1 terminal-potential bound,
  t<=2(q+1)-2=2q,
hence
  t in {2q-3,2q-2,2q-1,2q}.

Let R=(r_1,...,r_t) be the chosen maximum path ending physically at z.
Since q>=5,
  t>=2q-3>q+1=phi(h),
so h is not the last edge of R. Because mu_z(h)=1, exactly one of {y,v} occurs in V(R) outside its last edge.

CASE 1: y is absent, so v is the unique h-contact.
Let j,j' be the first and last indices of path edges containing v. The prefix
  r_1,...,r_j,h
ends in h through terminal v, hence has length at most q (length q+1 would be a longest h-path through a wrong entrance). Thus j<=q-1.
Likewise the reversed suffix
  r_{t-1},...,r_{j'},h
has length t-j'+1<=q, so j'>=t-q+1.
Since a path vertex lies in one edge or two consecutive edges,
  j'<=j+1<=q.
Thus t<=2q-1.

If t=2q-1, equality forces
  j=q-1, j'=q,
so v=r_{q-1} cap r_q.

If t=2q-2, the possibilities are:
- v private in r_{q-1};
- v=r_{q-2} cap r_{q-1};
- v=r_{q-1} cap r_q.

If t=2q-3, v is confined to the five central positions:
- private in r_{q-2} or r_{q-1};
- one of r_{q-3} cap r_{q-2}, r_{q-2} cap r_{q-1}, r_{q-1} cap r_q.

CASE 2: v is absent, so y is the unique h-contact.
Use the certified position-sensitive endpoint-potential bound 8b1790d79d74 and phi(y)=q.

If y is private in r_i, then
  max{i,t-i+1}<=q,
so
  t-q+1<=i<=q.

If y=r_i cap r_{i+1}, then
  max{i,t-i}<=q,
so
  t-q<=i<=q.

Consequently:
- t=2q: y is uniquely r_q cap r_{q+1};
- t=2q-1: y is private in r_q or one of joints r_{q-1} cap r_q, r_q cap r_{q+1};
- t=2q-2: y lies in the five-slot central window with private indices q-1,q or joint indices q-2,q-1,q;
- t=2q-3: y lies in the seven-slot central window with private indices q-2,q-1,q or joint indices q-3,q-2,q-1,q.

Thus every high 0-1-1 terminal at the odd boundary has a reciprocal central-gate normal form on its opposite-terminal path.
