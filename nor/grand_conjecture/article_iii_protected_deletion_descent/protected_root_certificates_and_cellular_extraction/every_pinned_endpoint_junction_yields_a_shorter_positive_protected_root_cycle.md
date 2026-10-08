# Every pinned endpoint junction yields a shorter positive protected-root cycle

## Composition

(none yet)

## Development

## Every pinned endpoint junction yields a shorter positive protected-root cycle

Assume the witness-preserving endpoint CORNER-LIFT property of Subsection 93.

By Subsection 114, after minimizing/pushing partner domains an endpoint-root cycle has the following alternative:

- all partners are constant, giving an exact constant-core Johnson cycle; or
- there is a pinned partner-change boundary.

We now show that every pinned boundary in the second case produces a strictly shorter positive physical root cycle. The shorter cycle may mix endpoint and flat-transport provenance; that is the intended handoff.

### Setup at a pinned boundary

Write three consecutive physical-cycle vertices as
a -> x -> c,
so the endpoint witness omitting x begins
O_x=(a,b,c,d,...)
with a the pinned partner and c the physical successor.

Thus a,b,c,d,x are distinct as required by the deletion witness, in particular d!=c.

The old positive physical cycle contains the two consecutive roots
a->x,
x->c.

Use the endpoint-pivot notation
lambda_0=alpha(a,c,d),
lambda_1=alpha(x,c,d).

### Case 1: lambda_0=lambda_1=0

By Subsection 113 the completed endpoint-pivot triangle produces an actual endpoint root
a->c.

Replacing
a->x->c
by
a->c
gives a strictly shorter positive protected-root cycle.

### Case 2: lambda_0=1

Delete b from the prepended endpoint state. Subsection 119 shows that the resulting order begins
(x,a,c,d,...)
and carries the actual transition on the tetrahedron (x,a,c,d).

Regardless of whether that transition tetrahedron is flat or fully curved, its physical first-to-fourth root is
x->d.

If fully curved, §119 retains it immediately as the farther protected root. If flat, it is the first actual root of the audited one-sided transport flag (§§82,104); flatness only says the transition can be repaired, not that the physical transition/root is fictitious.

Since d!=c, this root is NOT the old cycle edge x->c.

Let P be the directed segment of the old physical cycle from d back to x. Because the old cycle is simple on its support and d is a cycle vertex whenever d lies in the support, the chord x->d plus P gives a strictly shorter positive physical root cycle.

If d lies outside the old cycle support, then x->d is instead a genuine support-ejection root; this is already a strict enlargement/handoff rather than recurrence inside the old cycle.

Thus the first-stop case either gives a shorter positive protected-root cycle or exits the old support.

### Case 3: lambda_0=0, lambda_1=1

The first successful pivot of Subsection 113 gives the genuine endpoint witness omitting b, whose endpoint root is
b->c.

If b->c is not an edge of the old physical cycle, then:
- if b and c lie on the old cycle support, it is a directed chord and gives a strictly shorter positive cycle;
- if one endpoint lies outside the old support, it is a support-ejection handoff.

The only non-ejective non-shortening possibility is that b->c is already the old cycle edge leaving b.

Now apply Subsection 119 to the SECOND stopped pivot, with relabeling
omitted coordinate b,
current witness (x,a,c,d,...).

Its stopped transition is on
(b,x,c,d)
and has physical root
b->d.

But d!=c. Therefore b->d differs from the assumed old outgoing edge b->c, so it is again either a directed chord producing a strictly shorter positive cycle or a support-ejection root.

Hence the second-stop case also cannot recur inside the old physical circuit.

### Theorem

Under witness-preserving endpoint corner lifting, every endpoint-root cycle satisfies one of:

1. exact constant-core case:
   all attained rank-two cuts concatenate with one common partner;

2. cycle descent:
   there is a strictly shorter positive physical cycle of actual protected/transport roots;

3. support ejection:
   an actual protected root leaves the old cycle support.

In particular, if the endpoint cycle is Hamiltonian on the ambient coordinate set, support ejection is impossible. Since a Hamiltonian cycle cannot have a constant partner coordinate (the common partner is itself some ambient cycle vertex and would violate the endpoint exclusion on its incident edge), every corner-lift-normalized Hamiltonian endpoint cycle yields a strictly shorter positive protected-root cycle.

### Strategic consequence

The endpoint square/corner-lift theorem would therefore do substantially more than align cuts.

It would convert the direct endpoint cancellation of §84 into a well-founded dichotomy:

- exact constant-core Johnson chronology on a proper physical support; or
- strict descent in the length of a positive protected-root circuit.

The descended circuit may mix endpoint and flat-transport roots, so the next global theorem should be formulated for minimum positive protected-root circuits across ALL realized provenance classes, not only endpoint cycles.

This connects the endpoint route to §§104,109-110,116: a minimum mixed circuit cannot lie in one monotone transport flag, so it must pass through a genuine branching/repair-square/braid interaction.
