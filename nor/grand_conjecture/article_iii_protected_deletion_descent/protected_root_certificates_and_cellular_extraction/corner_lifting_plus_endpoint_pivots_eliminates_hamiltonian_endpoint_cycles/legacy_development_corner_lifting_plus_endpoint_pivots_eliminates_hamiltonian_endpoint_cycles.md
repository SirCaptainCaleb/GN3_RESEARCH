# Corner lifting plus endpoint pivots eliminates Hamiltonian endpoint cycles — preserved pre-item development

## Development

Assume the witness-preserving endpoint CORNER-LIFT property of roots §§93/114. Choose an actual endpoint-root cycle
rho_i=e_{x_i}-e_{x_{i+1}}
of minimum possible length, and suppose its support is Hamiltonian, i.e. it contains every ambient coordinate.

Normalize its partner word by the corner-copy dynamics of root §114. Then it decomposes into constant-core arcs joined at pinned boundaries. At a pinned boundary beginning at s,
a=x_{s-1},
x=x_s,
c=x_{s+1},
and the endpoint witness omitting x begins
(a,b,c,d,...),
with b,d distinct from a,x,c.

We show that ANY pinned boundary contradicts minimum cycle length.

Let
lambda_0=alpha(a,c,d).

### Case 1: lambda_0=0

Root §113 gives a genuine one-change endpoint-pivot witness omitting b, with endpoint root
rho'=e_b-e_c.

Because the physical cycle is Hamiltonian, b is one of its vertices. The unique cycle vertex whose old outgoing root targets c=x_{s+1} is x=x_s. But b is distinct from x. Therefore rho' is not the existing cycle edge into c: it is a genuine directed chord b->c.

Adding this chord to the directed segment of the old physical cycle from c back to b gives a strictly shorter positive physical root cycle of actual endpoint roots. Contradiction.

Hence lambda_0 cannot be 0 at a pinned boundary of a minimum Hamiltonian cycle.

### Case 2: lambda_0=1

Use the stopped-pivot calculation of root §119. Put
lambda_1=alpha(x,c,d).

If lambda_1=1, the order obtained by deleting b contains a fully-curved transition on (x,a,c,d) and emits
rho'=e_x-e_d.
The old successor of x on the physical cycle is c, while d is distinct from c. Since d is on the Hamiltonian cycle support, rho' is a genuine chord x->d and gives a shorter cycle.

If lambda_1=0, root §117 gives the face packet
alpha(a,x,c)=1,
alpha(a,x,d)=0,
alpha(a,c,d)=1,
alpha(x,c,d)=0.
Thus the ordered tetrahedron
(a,x,c,d)
has a fully-curved 1-to-0 transition and emits
rho'=e_a-e_d.
The old successor of a=x_{s-1} is x=x_s, while d is distinct from x. Again rho' is a genuine chord on the Hamiltonian support and shortens the cycle.

Therefore lambda_0=1 is also impossible.

So NO pinned partner-change boundary can occur.

By the copy-lift normalization of root §114, absence of boundaries means the partner word is constant:
a_i=a
for all i.

But the physical cycle is Hamiltonian, so a=x_t for some cycle vertex. At edge t the endpoint exclusion requires a_t not equal x_t, contradiction.

Hence:

> Assuming only the witness-preserving endpoint CORNER-LIFT property of §93, no minimum counterexample can have a Hamiltonian endpoint-root cycle.

This avoids the stronger unproved partner-SWAP lift used in §§108/111. The proof needs only:
1. backward partner copying to normalize defects into pinned boundaries;
2. the endpoint pivot theorem;
3. the stopped-pivot full/flat face calculation;
4. minimum physical-cycle length.

More generally, for a proper-support minimum endpoint cycle, the same proof shows that every pinned boundary must eject an exterior coordinate: in the lambda_0=0 branch the pivot coordinate b must lie outside the cycle support; in the lambda_0=1 branches the farther coordinate d must lie outside the support. Thus pinned boundaries are literal support-expansion certificates.
