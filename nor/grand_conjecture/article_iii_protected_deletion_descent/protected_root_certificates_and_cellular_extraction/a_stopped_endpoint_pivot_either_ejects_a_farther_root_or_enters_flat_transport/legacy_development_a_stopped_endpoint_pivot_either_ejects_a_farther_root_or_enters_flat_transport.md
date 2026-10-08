# A stopped endpoint pivot either ejects a farther root or enters flat transport — preserved pre-item development

## Composition

(none yet)

## Development

Continue with the arbitrary endpoint witness
O=(a,b,c,d,...)
omitting x, with word beginning 0,0,... and fully-curved endpoint tetrahedron (x,a,b,c). Thus
alpha(x,a,b)=1,
alpha(a,b,c)=0,
alpha(x,a,c)=0,
alpha(x,b,c)=1,
and alpha(b,c,d)=0.

Let
lambda=alpha(a,c,d).

If lambda=0, deleting b gives the good endpoint pivot witness described in root §113.

Assume instead lambda=1. Coboundary flatness on {a,b,c,d}, using
alpha(a,b,c)=alpha(b,c,d)=0,
forces
alpha(a,b,d)=1.

Put
r=alpha(x,a,d).
The remaining tetrahedral identities determine
alpha(x,b,d)=r,
alpha(x,c,d)=1-r.
Indeed these follow successively from the four-set parity identities on
{x,a,b,d}, {x,a,c,d}, and {x,b,c,d}.

Now delete b from the prepended endpoint state. The resulting order begins
(x,a,c,d,...)
and has first two statuses
alpha(x,a,c)=0,
alpha(a,c,d)=1.
So it carries a 0-to-1 transition on the ordered tetrahedron (x,a,c,d).

Its two endpoint-repair faces are precisely
alpha(x,a,d)=r,
alpha(x,c,d)=1-r.

Therefore:

1. If r=1, both endpoint repairs fail: the off-faces have the fully-curved pattern 1,0. The tetrahedron (x,a,c,d) is fully curved and emits the protected slide root
rho'=e_x-e_d.
This is a genuine farther successor root from the same endpoint coordinate x, skipping the old target c.

2. If r=0, both endpoint repairs are available: the tetrahedron is flat. Swapping c,d gives the local order
(x,a,d,c,...)
with central statuses
alpha(x,a,d)=0,
alpha(a,d,c)=1-alpha(a,c,d)=0.
Thus the local 01 defect is removed and any changed windows lie farther outward. With the inherited zero-phase target, this is exactly a one-sided flat boundary repair; the threshold-band potential either continues outward, reaches a good one-change deletion state, or stops at a later fully-curved protected root.

Hence a stopped first endpoint pivot has no fourth behavior:
- pivot bit 0: a new good deletion witness;
- pivot bit 1 and r=1: immediate farther protected root e_x-e_d;
- pivot bit 1 and r=0: audited outward flat transport.

The same statement applies after one successful pivot, with the corresponding relabeled coordinates. Therefore the endpoint-pivot dynamics either closes into the realized Johnson triangle of root §113, or exits into one of the two already-global Article III mechanisms: a protected root ejection or a monotone transport flag.

For a support-minimal physical endpoint-root cycle, the immediate-root branch is especially restrictive. If d lies on the cycle support and is not the old successor c, the new root e_x-e_d is a chord and combines with the appropriate directed segment of the old cycle to give a strictly shorter physical protected-root cycle. Thus any minimal cycle surviving this branch must eject d outside its support. In a Hamiltonian endpoint cycle there is no outside coordinate, so the r=1 stopped-pivot branch is impossible.
