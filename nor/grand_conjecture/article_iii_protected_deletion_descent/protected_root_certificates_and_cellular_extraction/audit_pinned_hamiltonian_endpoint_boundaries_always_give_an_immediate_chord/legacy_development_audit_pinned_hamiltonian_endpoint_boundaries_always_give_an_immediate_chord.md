# Audit: pinned Hamiltonian endpoint boundaries always give an immediate chord — preserved pre-item development

## Audit and simplification: a pinned boundary in a Hamiltonian endpoint cycle always gives an immediate chord

Subsection 121 has the correct strategic conclusion but its stopped-pivot case conflates two bits.

In the notation of Subsection 119, after the first pivot stops with
lambda_0=alpha(a,c,d)=1,
the curvature of the transition tetrahedron (x,a,c,d) is controlled by
r=alpha(x,a,d),
not by
lambda_1=alpha(x,c,d).
Indeed flatness gives alpha(x,c,d)=1-r.

Fortunately no curvature split is needed for the Hamiltonian-cycle argument.

Assume the endpoint CORNER-LIFT property and choose an actual endpoint-root cycle of minimum length whose physical support is Hamiltonian.

Normalize its partner word as in Subsection 114. Suppose there is a pinned boundary with
a -> x -> c
on the physical cycle and endpoint witness
O_x=(a,b,c,d,...),
where a is the pinned partner. The coordinates a,b,c,d,x are distinct.

Put
lambda_0=alpha(a,c,d).

### If lambda_0=0

Subsection 113 gives the genuine endpoint-pivot deletion witness omitting b. Its endpoint root is
b->c.

On the Hamiltonian directed cycle, the unique old edge entering c is
x->c.
Since b!=x, the root b->c is not an old cycle edge.

Hence b->c is a directed chord. Together with the directed old-cycle segment from c back to b it gives a strictly shorter positive cycle of actual endpoint roots.

This contradicts minimum cycle length.

### If lambda_0=1

Deleting b from the prepended endpoint state produces the actual transition on the ordered tetrahedron
(x,a,c,d),
as in Subsection 119.

Its physical slide root is
x->d.

If the tetrahedron is fully curved, this root is retained immediately as the farther protected root.

If the tetrahedron is flat, the same root is the first actual root of the audited one-sided flat transport trajectory of Subsections 82 and 104. Flatness changes its repairability, not its physical root vector or its realized transition provenance.

The old outgoing cycle edge from x is
x->c.
Since d!=c, x->d is a directed chord of the Hamiltonian physical cycle.

Again, x->d together with the old directed segment from d back to x gives a strictly shorter positive protected-root cycle.

Contradiction.

### Corrected theorem

Therefore no pinned partner-change boundary can occur in a minimum-length Hamiltonian endpoint-root cycle.

Under corner-lift normalization, the partner word must then be constant.

But on a Hamiltonian cycle every ambient coordinate occurs as some x_t. A constant partner a is one of these coordinates, say a=x_t, and the endpoint exclusion at edge t forbids a_t=x_t. Contradiction.

Hence:

> Assuming only the witness-preserving endpoint CORNER-LIFT property of Subsection 93, no minimum counterexample admits a Hamiltonian endpoint-root cycle.

This proof does not require:
- the stronger partner-swap lift of Subsections 108/111;
- the second pivot bit lambda_1;
- classification of the stopped transition as flat versus full;
- terminalization of the flat transport.

It uses only the first pivot bit and the existence of the actual transition root at the stopped state.

For proper-support endpoint cycles the same local argument gives the exact alternative:
- lambda_0=0: if b lies in the old support, b->c shortens the cycle; otherwise b is a support-ejection coordinate;
- lambda_0=1: if d lies in the old support, x->d shortens the cycle; otherwise d is a support-ejection coordinate.

Thus every pinned boundary of a minimum proper-support endpoint cycle certifies support expansion.
