# Every coordinate pair is clone-contractible or carries a common-A3 opposite-root cell — preserved pre-item development

## Composition

(none yet)

## Development

## Every coordinate pair is clone-contractible or carries a common-A3 opposite-root cell

Fix distinct coordinates x,z and let
O=(w_1,...,w_m)
be any coordinate order of W=V\{x,z}. Put
X_i=alpha(x,w_i,w_{i+1}),
Z_i=alpha(z,w_i,w_{i+1}).

### If the scans agree everywhere, x and z are clones

Let d(u)=alpha(x,z,u). Flatness on {x,z,u,v} gives
alpha(x,u,v) xor alpha(z,u,v)=d(u) xor d(v).

If X_i=Z_i for every consecutive pair of O, then d(w_i)=d(w_{i+1}) for every i. Since O is a spanning chain of W, d is constant on W. Hence
alpha(x,u,v)=alpha(z,u,v)
for every distinct u,v in W.

Thus x and z are genuine clones relative to all remaining coordinates.

Clone pairs contract. Take a NOR-good order of V\{z}, in which x occurs. Inserting z immediately after x creates two equal central statuses k,k; inserting z immediately before x creates the complementary pair 1-k,1-k. All exterior affected windows agree with the old windows by the clone identity. Choose the side whose duplicated value equals the old status through x. The old status word is unchanged except for duplicating one bit, so the lifted full order is NOR-good.

Therefore a minimum counterexample has no pair with identical scans along O.

### A disagreement gives opposite roots in one four-set

Choose i with X_i!=Z_i and normalize X_i=1,Z_i=0.

Then
(x,w_i,w_{i+1},z)
has status word 1,0, hence carries the physical transition root x->z.

The order
(z,w_{i+1},w_i,x)
also has word 1,0:
alpha(z,w_{i+1},w_i)=1-Z_i=1,
while
alpha(w_{i+1},w_i,x)=1-X_i=0.
It carries the opposite physical root z->x.

Both certificates use exactly the same four physical coordinates and lie in the same A3 permutahedral cell with any exterior order frozen.

Their curvature types agree. Thus every nonclone pair x,z has a common-A3 opposite-root cell, either:
1. fully curved in both orientations, giving a protected two-term A3 dependence; or
2. flat in both orientations, giving two opposite flat transition-removal chambers.

### Consequence

In a minimum counterexample EVERY coordinate pair is in the second alternative, since the clone alternative closes NOR. Hence the global shortcut problem can be reformulated locally:

For every x!=z there is a four-coordinate A3 cell carrying x<->z as an opposite transition pair. Fully-curved cells are already in the common-face protected A3 extraction theory. The only genuinely new pairwise compatibility object is a flat common-A3 opposite-root cell.

This removes the need to treat the crossed ladder as the primary pairwise existence mechanism; the ladder remains useful for boundary provenance, while existence of a compatible opposite-root cell follows directly from flatness plus clone exclusion.
