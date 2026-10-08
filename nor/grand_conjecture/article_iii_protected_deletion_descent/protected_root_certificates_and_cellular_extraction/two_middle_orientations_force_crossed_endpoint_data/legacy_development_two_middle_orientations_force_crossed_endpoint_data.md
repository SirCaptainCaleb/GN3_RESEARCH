# Two middle orientations force crossed endpoint data — preserved pre-item development

## Two orientations of the middle force crossed endpoint data

Fix distinct x,z and a NOR-good order O=(w_1,...,w_m) of V minus {x,z}, with internal word 0^p1^q.

Set
A=alpha(x,w_1,w_2),
C=alpha(z,w_1,w_2),
D=alpha(w_{m-1},w_m,x),
B=alpha(w_{m-1},w_m,z).

For x O z the full word is A,0^p1^q,B. Therefore this order either closes NOR, realizes the direct outermost root x->z, or has A=B.

Now reverse only the middle order. O^rev has normalized word 0^q1^p. The endpoint bits of x O^rev z are 1-D and 1-C. Hence this second order either closes NOR, realizes x->z, or has C=D.

Consequently, if neither middle orientation closes nor realizes x->z, then
A=B and C=D.

Equivalently, for insertion scans
s_i^x=alpha(x,w_i,w_{i+1}),
s_i^z=alpha(z,w_i,w_{i+1}),
the endpoint data are
s_1^x=A, s_{m-1}^x=C,
s_1^z=C, s_{m-1}^z=A.

Thus only two residual types exist:
- A=C, so all four endpoint bits agree;
- A differs from C, so the two scans have opposite endpoint directions.

In the second case, after normalization A=0,C=1, both xO and Ox are NOR-good orders of V minus {z}. The symmetric normalization gives the analogous statement with x,z exchanged.

Hence the three-block shortcut problem reduces exactly to an equal-ended or oppositely-directed two-exterior scan problem.
