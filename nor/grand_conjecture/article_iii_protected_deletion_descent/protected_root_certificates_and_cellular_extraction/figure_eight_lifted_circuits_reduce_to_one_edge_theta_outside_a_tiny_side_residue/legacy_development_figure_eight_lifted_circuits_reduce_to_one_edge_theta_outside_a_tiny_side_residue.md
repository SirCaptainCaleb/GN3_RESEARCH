# Figure eight lifted circuits reduce to one edge theta outside a tiny side residue — preserved pre-item development

## Composition

(none yet)

## Development

## Figure-eight circuits reduce to one-edge theta pivots except for a tiny side-imbalance residue

Work in a full-support dimension-saturated honest lifted circuit whose physical support is a directed figure-eight.

Let the two directed cycles meet only at the articulation vertex v. Normalize their side imbalances as A>0 and B<0.

Let e=a->v be the incoming edge of the positive cycle at v, and f=b->v the incoming edge of the negative cycle. Write their side signs as s_e,s_f.

Connected full support forces all coordinates into one tied top carrier block, so the cross-splice windows below can be realized as honest violating states in the same product carrier cell.

### Positive-lobe cross splice

Realize the ternary window (a,v,b) on the threshold side on which it violates, with honest label (e_a-e_b,t_AB).

Replace in the positive cycle the final edge a->v by a->b->v, using the bypass and old edge f. The new directed cycle D_A has side imbalance

S(D_A)=A+delta_A,
delta_A=t_AB-s_e+s_f,

where delta_A is one of -3,-1,1,3.

If A+delta_A=0, D_A is a balanced simple cycle and is removable.

If A+delta_A>0, then D_A and the old negative cycle have opposite nonzero side imbalances. Their union is a theta graph whose common directed path is exactly the single edge b->v.

Thus this branch immediately enters the theta-shortening theorem with common-path length one.

This branch fails only if A+delta_A<0. Since A>=1, failure forces
A in {1,2} and delta_A=-3.
Hence
t_AB=-1, s_e=+1, s_f=-1.

### Negative-lobe cross splice

Similarly realize the honest window (b,v,a) with label (e_b-e_a,t_BA).

Replace b->v by b->a->v. The resulting cycle D_B has imbalance

S(D_B)=B+delta_B,
delta_B=t_BA-s_f+s_e,

again in {-3,-1,1,3}.

If B+delta_B=0, D_B is balanced and removable.

If B+delta_B<0, then the old positive cycle and D_B have opposite signs and form a theta whose common path is exactly the single edge a->v.

This branch fails only if B+delta_B>0. Since B<=-1, failure forces
B in {-1,-2} and delta_B=+3.
Hence
t_BA=+1, s_f=-1, s_e=+1.

### Rigid double-failure residue

Both direct figure-eight cross-splices can fail only when

A in {1,2},
B in {-1,-2},
s_e=+1,
s_f=-1,
t_AB=-1,
t_BA=+1.

Outside this tiny packet, at least one articulation cross-splice gives either a balanced removable cycle or a theta dependence with one-edge common path.

By the theta-shortening theorem, the theta case takes at most one shortening step to reach a balanced removable cycle or another figure-eight.

### Consequence

A terminal figure-eight cannot have arbitrary opposite side imbalance. If neither articulation predecessor splice enters the controlled balanced-cycle/theta mechanism, both lobe imbalances have absolute value at most two and the four articulation/bypass side signs are forced exactly as above.

Thus the remaining dimension-saturated honest-lift obstruction is reduced to a bounded side-arithmetic residue, independent of the physical lobe lengths.
