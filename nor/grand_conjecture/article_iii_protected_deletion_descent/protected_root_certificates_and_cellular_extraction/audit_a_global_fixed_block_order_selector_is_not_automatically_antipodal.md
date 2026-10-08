# Audit: a global fixed block-order selector is not automatically antipodal

## Composition

(none yet)

## Development

## Audit: a global fixed block-order selector is not automatically antipodal

Roots §§163-167 introduce a useful block-local selector: fix one NOR-good order g(S) for every proper subset S and label an ordered-partition face

F=B_1|...|B_s

using the full witness

pi_F=g(B_1)...g(B_s).

This gives excellent codimension-one locality, but it is NOT automatically compatible with the antipodal symmetry required by the symmetric Sperner carrier of roots §§155-156.

### The symmetry mismatch

Reversal sends F to

-F=B_s|...|B_1

and sends the witness pi_F to

pi_F^rev
=
g(B_s)^rev ... g(B_1)^rev.

The fixed-selector rule, however, assigns

pi_{-F}
=
g(B_s)...g(B_1).

These agree only if every selected block order satisfies

g(S)=g(S)^rev,

which is impossible for a nontrivial ordered set.

Since the consecutive-change defect is reversal-odd only under ACTUAL reversal of the coordinate order,

C(pi^rev)=-C(pi),

one cannot conclude

C(pi_{-F})=-C(pi_F)

for the fixed-selector witnesses.

Therefore the nonzero-degree antipodal boundary argument of §155 does not automatically apply to the global fixed-selector system of §§163-167.

### What remains valid

The following statements are still correct for any fixed selector g:
- codimension-one witness changes are block-local (§163);
- the transition-root identity for C(pi) (§164);
- Abel decomposition of convex combinations along a chosen flag (§165);
- bounded interface complexity of one merge (§166);
- disjoint merge squares and three-block associativity diamonds as face-poset/witness identities (§167).

What is not yet justified is that this particular selector can be used as the antipodal Sperner boundary carrier whose degree forces the zero.

### Repair target

One needs an EQUIVARIANT block-local selector or a replacement construction which retains both properties:

1. pi_{-F}=pi_F^rev, so labels are antipodal;
2. along a codimension-one face step, witnesses differ only in the merged block plus bounded boundary memory.

A choice of one global face-orientation sign on each antipodal pair gives (1) but can flip all block orders across adjacent faces and destroy (2). Hence the repair is nontrivial.

Possible safe alternatives are:
- work with the original independently antipodal witnesses of §155 and recover locality only after the topological zero selects one flag;
- use a two-valued/block-pair carrier and prove a degree statement for the resulting correspondence;
- construct orientations coherently only on the selected zero flag and its antipodal mate, where no global adjacent-face compatibility is required.

Until such a repair is proved, §§163-167 should not be cited as a complete symmetric Sperner extraction theorem.
