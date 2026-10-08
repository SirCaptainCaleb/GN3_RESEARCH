# The degenerate theta endpoint still has a successful surviving bypass — preserved pre-item development

## The degenerate theta endpoint still has a successful surviving bypass

This repairs the endpoint gap identified in root §198.

Use the notation of root §196:
P:u->v, Q:v->u, R:v->u,
with cycle imbalances
A=S(P)+S(Q)>0,
B=S(P)+S(R)<0.

Assume the descent has reached the degenerate endpoint where P is the single edge e=u->v and Q is the single reverse edge f=v->u. Then the Q-bypass is indeed degenerate, as root §198 notes.

However the 2-cycle C_Q={e,f} has positive side imbalance A=s_e+s_f>0. Since s_e,s_f are each plus or minus one, this forces
s_e=s_f=+1
and A=2.

Now inspect the still genuine R-bypass from root §196. Its failure condition was proved there exactly: R-bypass failure can occur only when
delta_R=+3
and
B in {-1,-2},
and delta_R=+3 requires
s_e=s_g=-1,
where g is the first edge of R.

But the positive 2-cycle already forces s_e=+1. Contradiction.

Therefore the genuine R-bypass CANNOT fail.

Hence at the degenerate theta endpoint the surviving bypass necessarily yields one of:
1. a side-balanced simple cycle, removable by the one-cycle parity-transversality theorem; or
2. a new positive lifted dependence in which the common path has disappeared, i.e. a figure-eight support.

The symmetric case where R is the single reverse edge is identical.

### Corrected theta theorem

Root §196 together with this endpoint repair gives a complete finite descent:
- while both branch bypasses are nondegenerate, the two-branch sign argument shortens the common path or gives a balanced removable cycle;
- if one branch degenerates at the final common edge, the nonzero side imbalance of that 2-cycle fixes the shared-edge sign and forces the other bypass to succeed.

Thus every full-support theta honest-lifted circuit reduces to either a removable one-cycle zero or a figure-eight circuit.

No terminal shared-edge theta residue remains.
