# Endpoint pivots either stop on one splice bit or realize a Johnson triangle — preserved pre-item development

Let an arbitrary-scan endpoint witness in the coboundary-flat alternating ternary sector be
O_x=(a,b,c,d,...)
omitting x, with word 0^p1^q and p>=3. Prepending x gives the endpoint-defect word 1,0^p,1^q, and the endpoint tetrahedron (x,a,b,c) is fully curved. Hence
alpha(x,a,b)=1,
alpha(a,b,c)=0,
alpha(x,a,c)=0,
alpha(x,b,c)=1.

Put
lambda_0=alpha(a,c,d).

Delete b from the prepended endpoint order. The resulting deletion order is
O_b=(x,a,c,d,...)
omitting b. Its first two statuses are
alpha(x,a,c)=0,
alpha(a,c,d)=lambda_0,
and every later status from (c,d,...) onward is the untouched suffix of O_x.

Therefore, if lambda_0=0, O_b is a genuine one-change deletion witness with the SAME phase profile 0^p1^q.

Now put
lambda_1=alpha(x,c,d).
Apply the same endpoint pivot to O_b. If lambda_1=0, deleting its second coordinate a from the prepended b-state gives
O_a=(b,x,c,d,...)
omitting a, again with the same word 0^p1^q.

For O_a the next pivot condition is alpha(b,c,d), which is the second old window of O_x and equals 0 because p>=2. Hence the third pivot returns exactly to O_x.

Thus, when lambda_0=lambda_1=0, there is an exact three-state endpoint recurrence:
omit x: (a,b,c,d,...)
 -> omit b: (x,a,c,d,...)
 -> omit a: (b,x,c,d,...)
 -> omit x: (a,b,c,d,...).

Every state is a genuine one-change deletion witness with identical outside suffix and identical phase profile.

Its cut geometry is exact. The attained rank-two endpoint cuts are
C_x={x,a},
C_b={b,x},
C_a={a,b},
the three vertices of the Johnson triangle on {x,a,b}. The endpoint roots are
rho_x=e_x-e_c,
rho_b=e_b-e_c,
rho_a=e_a-e_c.
Thus all three roots point transversely from that realized Johnson face toward the same fourth coordinate c. Their forced successor cuts are
{a,c}, {x,c}, {b,c},
respectively.

Consequently the endpoint pivot recurrence realizes one triangular face of Delta(4,2) together with the three canonical outward exchange directions toward the opposite c-face.

If either lambda_0 or lambda_1 equals 1, the pivot recurrence stops at a single explicit splice bit. Hence the arbitrary endpoint local problem has the sharp alternative:
1. a one-bit stopped pivot, or
2. a fully realized three-witness Johnson triangle with common target c.

This is the endpoint analogue of the interior A2 recurrence, but with stronger chronology: the three deletion witnesses share the entire suffix starting at c and differ only in the first two coordinates and the omitted member of {x,a,b}. It is therefore a promising finite cell on which to prove the endpoint square/triangle-lift theorem without comparing unrelated global witnesses.
