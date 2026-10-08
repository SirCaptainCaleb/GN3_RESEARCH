# Nested certified central cuts exclude every positive protected-root dependence

## Metadata

- ID: nested_certified_central_cuts_exclude_every_positive_protected_root_dependence
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 237
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Nested certified central cuts exclude every positive protected-root dependence

Work with any finite family of actual ternary protected roots
rho_i=e_{a_i}-e_{d_i}
equipped with certified central cuts C_i such that
a_i in C_i,qquad d_i notin C_i.

Assume the cuts form a chain under inclusion. After relabeling,
C_1 subseteq C_2 subseteq ... subseteq C_m.

We show that the roots lie in one open halfspace.

### Ordered difference blocks

Delete repeated cuts if necessary and write the distinct chain as
K_1 proper-subset K_2 proper-subset ... proper-subset K_r.

Partition the physical coordinates into ordered blocks
D_0=K_1,
D_j=K_{j+1} minus K_jquad(1<=j<r),
D_r=V minus K_r.

Choose real numbers
w_0<w_1<...<w_r
and define a coordinate potential w(v)=w_j for v in D_j.

Let rho=e_a-e_d be any protected root with certified cut K_q.

Since a in K_q, the coordinate a lies in one of D_0,...,D_{q-1}.
Since d notin K_q, the coordinate d lies in one of D_q,...,D_r.

Therefore
w(a)<w(d),
and hence
<w,rho>=w(a)-w(d)<0.

The inequality is strict for EVERY root in the family.

### Theorem

If the certified central cuts of a family of protected roots are totally ordered by inclusion, then the family admits no nontrivial positive dependence.

Indeed, if
sum_i lambda_i rho_i=0,qquad lambda_i>0,
then pairing with w gives
0=sum_i lambda_i <w,rho_i><0,
a contradiction.

### Consequence for Article III

Every positive protected-root dependence in a compatible carrier must contain at least two INCOMPARABLE certified central cuts.

Thus:
- arbitrary length along one monotone transport flag is irrelevant;
- more generally, mixing several roots from different trajectories still cannot cancel as long as their certified cuts remain laminar in one chain;
- the first genuinely possible cancellation occurs exactly when compatible repair trajectories branch into nonnested cut states or later rejoin after such a branch.

This localizes the remaining protected-root topology to branch/rejoin cells.

At a single flat ternary switch the two repair directions already form the realized boundary-separated square of §109/§110. At a fully-curved barrier the four same-cut exchange roots form the realized K_{2,2} Johnson square of §230. Hence the next closure target is precise:

> show that the first pair of incomparable certified cuts in a compatible protected carrier is contained in, or can be reduced to, one of these bounded rank-two gluing cells (commuting square or A2 braid residue).

No minimization in the unrestricted reversal-closed realized-root graph is used here.

## Frontier

- Development version when composed: None
- Development version now: 1
