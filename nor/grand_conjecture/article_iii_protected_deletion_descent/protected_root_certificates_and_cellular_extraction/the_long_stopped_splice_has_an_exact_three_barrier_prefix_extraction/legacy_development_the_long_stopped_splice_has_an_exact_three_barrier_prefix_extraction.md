# The long stopped splice has an exact three-barrier prefix extraction — preserved pre-item development

Continue with the long stopped splice state of root §133:
O_c=(x,b,a,d,e,f,...)
omitting c, with target 0^p1^q and exact prefix statuses
0,0,1,0,...
The only initial mismatch is rank 3.

Write
r=alpha(x,b,d).
From the first-stop tetrahedral identities this equals alpha(x,a,d).

### First boundary: rank 3

The rank-3 transition is the 1-to-0 tetrahedron
Q_3=(a,d,e,f).

If Q_3 is fully curved, stop with its protected physical root
e_a-e_f.

Assume Q_3 is flat. The inward first-pair repair swaps a,d and turns the two boundary statuses 1,0 into 0,0. The order becomes
(x,b,d,a,e,f,...).

The four changed prefix statuses are:
w_1'=alpha(x,b,d)=r,
w_2'=alpha(b,d,a)=alpha(a,b,d)=1,
w_3'=0,
w_4'=0.
Here alpha(a,b,d)=1 is forced by the original first-stop identity.

Thus the new prefix is
r,1,0,0,...
and the target-compatible band now begins at rank 3.

### Second boundary: rank 2

The rank-2 transition is
Q_2=(b,d,a,e)
with statuses 1,0.

If Q_2 is fully curved, stop with protected root
e_b-e_e.

Assume Q_2 is flat. Its inward first-pair repair swaps b,d, giving
(x,d,b,a,e,f,...).

The prefix statuses become
w_1''=alpha(x,d,b)=1-alpha(x,b,d)=1-r,
w_2''=0,
w_3''=0,
w_4''=0.
Hence the entire word now agrees with the target except possibly at rank 1.

If r=1, then w_1''=0 and the resulting order is already a genuine one-change deletion witness omitting c.

### Third boundary: rank 1

It remains only r=0. Then the order
(x,d,b,a,e,f,...)
has exact prefix
1,0,0,0,...
against the zero target.

Its endpoint transition tetrahedron is
Q_1=(x,d,b,a).

If Q_1 is fully curved, it emits the protected endpoint root
e_x-e_a
inside the fixed deletion instance V minus {c}.

If Q_1 is flat, its first-pair endpoint repair swaps x,d. Since
alpha(x,d,b)=1
and
alpha(x,b,a)=0,
the repaired first two statuses are 0,0. No earlier window exists, and every later rank was already matched. Therefore the resulting deletion order is exactly 0^p1^q.

### Exact theorem

The long stopped branch lambda=mu=1 has exactly the following finite extraction:

1. a fully-curved rank-3 barrier with root e_a-e_f; or
2. after one flat repair, a fully-curved rank-2 barrier with root e_b-e_e; or
3. after two flat repairs, a genuine one-change deletion witness; or
4. after two flat repairs with r=0, either a fully-curved endpoint barrier with root e_x-e_a or one final flat repair giving a genuine one-change deletion witness.

Thus no generic transport theorem is needed here. At most three explicit adjacent swaps suffice, and every non-closing outcome is one of THREE nested protected root directions
a->f, b->e, x->a
supported on the first six coordinates of the fixed-omission deletion state.

All suffix coordinates and the omitted coordinate c remain unchanged throughout. This is a witness-preserving finite extraction theorem for the last long-phase branch left open by root §128.
