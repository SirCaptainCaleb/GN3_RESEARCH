# Strengthened frozen-support fences at component order six

## Statement

Frozen Hamiltonian six-supports remain locally consistent under two natural strengthenings: the explicit frozen seven-set from humanfrozen01 realizes all four endpoint hooks for its Hamilton path, and one Hamiltonian six-set can be frozen simultaneously against two distinct exterior roots. Hence neither endpoint-hook forcing nor same-base multi-root comparison can by itself rule out one-defect trapping at the first order-six shell.

## Body

# Strengthened frozen-support fences at component order six

Both local consistency statements follow from the explicit frozen seven-set certified by `humanfrozen01`; no exhaustive check of replacement supports is needed.

Let `J` be that boundary tournament on
`A union {x}`, where `A={0,1,2,3,4,5}` and `x=6`, represented by the edge order

`46 < 01 < 26 < 15 < 03 < 04 < 06 < 35 < 13 < 05 < 56 < 12 < 23 < 34 < 14 < 02 < 16 < 24 < 36 < 25 < 45`.

By `humanfrozen01`, `J[A]` is Hamiltonian, `J` is non-Hamiltonian, and for every `a in A` the six-set `(A-{a}) union {x}` is non-Hamiltonian. Thus `x` is the unique vertex whose deletion from `J` leaves a Hamiltonian six-set.

## 1. The explicit frozen seven-set realizes all four endpoint hooks

Take the Hamilton tight path
`P=(0,1,2,3,4,5)`
of `J[A]`.

The four endpoint hooks are verified directly in the displayed edge order:

- `(1,0,6)` is tight because `01 < 06`;
- `(2,6,0)` is tight because `26 < 06`;
- `(6,5,4)` is tight because `56 < 45`;
- `(5,6,3)` is tight because `56 < 36`.

These are exactly
`(p_1,p_0,x)`,
`(p_2,x,p_0)`,
`(x,p_5,p_4)`, and
`(p_5,x,p_3)`
for the displayed Hamilton path `P`.

Hence a frozen Hamiltonian six-set can occur together with all four endpoint hooks. The complete hook pattern itself therefore cannot rule out freezing at component order six.

## 2. One Hamiltonian six-set can be frozen against two roots

Take two copies `J_r` and `J_s` of this same explicit `J`, rename the exterior vertex `x` as `r` and `s` respectively, and identify their six-vertex Hamiltonian parts vertex-for-vertex with the same labeled set `A`.

The two prescribed boundary-tournament structures agree on their intersection `A`. A reversal pair involving `r` is prescribed only by `J_r`, and a reversal pair involving `s` only by `J_s`; triples involving both `r` and `s` remain free. Hence the prescriptions are compatible. Orient every still-undetermined reversal pair arbitrarily to obtain a boundary tournament `K` on `A union {r,s}`.

The induced subtournaments `K[A union {r}]` and `K[A union {s}]` are unchanged copies of `J`. Consequently `K[A]` is Hamiltonian, both seven-sets `A union {r}` and `A union {s}` are non-Hamiltonian, and for every `a in A`, both
`K[(A-{a}) union {r}]`
and
`K[(A-{a}) union {s}]`
are non-Hamiltonian.

Thus the same Hamiltonian six-set `A` is frozen simultaneously against two distinct exterior roots.

## Consequence

At component order six, neither the complete four-hook endpoint pattern nor the presence of two distinct exterior roots over one Hamiltonian six-set forces a nontrivial one-for-one replacement. Any no-trapping argument must therefore use additional information coupling the opposite support, an actual support/order disagreement between deletion covers, or another global consequence of the counterexample hypothesis.
