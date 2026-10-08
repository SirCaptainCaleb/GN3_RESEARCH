# Audit: theta bypass descent has a degenerate single-edge return-path endpoint — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: theta bypass descent has a degenerate single-edge return-path endpoint

This audits root §196.

Write the directed theta support as three internally disjoint paths

P:u->v,
Q:v->u,
R:v->u,

with the two directed cycles C_Q=P union Q and C_R=P union R having opposite nonzero lifted side imbalances.

Root §196 shortens P by taking its last edge

e=p->v

and the first edges

f=v->q of Q,
g=v->r of R,

then using honest bypass roots p->q and p->r. When both q and r are distinct from p, its two-branch sign argument is valid: failure of the Q-bypass forces s_e=+1, while failure of the R-bypass forces s_e=-1, so at least one branch succeeds.

### Degenerate endpoint

If P has length one, then p=u.

If Q also has length one, its first edge is

f=v->u,

so q=u=p.

The claimed Q-bypass is then

p->q=u->u,

which is the zero vector and is NOT a physical type-A root or a ternary window label.

Hence the Q branch is unavailable. The contradiction between Q-failure and R-failure cannot be invoked, because there is only one genuine bypass branch.

The same issue occurs symmetrically if R has length one.

More generally, at any stage a return path of length one makes the corresponding branch bypass degenerate precisely when the last vertex p of P is the return endpoint u; this is the terminal P-length-one situation.

### Correct safe conclusion

The bypass descent of root §196 is valid while BOTH branch bypasses are nondegenerate.

It reduces every theta either to:
- a balanced removable cycle;
- a strictly shorter theta;
- or a terminal shared-edge configuration in which P has length one and at least one return path is also a single reverse edge.

The latter contains a directed 2-cycle

u->v->u

sharing the edge u->v with the second directed cycle. It is NOT yet justified that this state becomes a figure-eight.

If both return paths have length at least two when P reaches length one, both bypasses remain genuine and one can perform a final successful bypass to a figure-eight as claimed. The gap is exactly the single-edge-return degeneracy.

### New reduced theta frontier

The only theta residue not covered by the existing two-branch shortening proof is therefore bounded in topology, not in ambient order size:

one common directed edge plus a reverse single edge and one other return path.

Equivalently, a nonzero-side directed 2-cycle shares one of its physical root directions with the other cycle.

This is a much smaller target and should be handled together with two-root lifted/local-reversal geometry rather than by another long theta classification.
