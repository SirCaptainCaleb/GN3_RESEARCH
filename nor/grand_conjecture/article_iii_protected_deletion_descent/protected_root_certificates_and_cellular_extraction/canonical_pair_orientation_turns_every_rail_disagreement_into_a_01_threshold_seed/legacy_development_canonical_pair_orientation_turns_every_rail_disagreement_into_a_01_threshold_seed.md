# Canonical pair orientation turns every rail disagreement into a 01 threshold seed — preserved pre-item development

## Composition

(none yet)

## Development

## Canonical pair orientation turns every rail disagreement into a 01 threshold seed

Continue with the exact binary ladder
[
X_i=alpha(x,w_i,w_{i+1}),qquad
Z_i=alpha(z,w_i,w_{i+1}),qquad
R_i=alpha(x,z,w_i),
]
satisfying
[
R_{i+1}oplus R_i=X_ioplus Z_i.
]

Fix a gap between (w_i) and (w_{i+1}).

### Canonical orientation of the inserted pair

If
[
R_i=0,
]
insert the pair in the order
[
x,z.
]
Then the two central pair windows are
[
alpha(w_i,x,z)=R_i=0,
qquad
alpha(x,z,w_{i+1})=R_{i+1}.
]

If
[
R_i=1,
]
insert the pair in the reversed order
[
z,x.
]
By alternation and cyclic invariance,
[
alpha(w_i,z,x)=1-R_i=0,
qquad
alpha(z,x,w_{i+1})=1-R_{i+1}.
]

Thus in either case the first central pair window is (0).

For the second central window, the rung identity gives
[
R_{i+1}=R_ioplus X_ioplus Z_i.
]
Hence after the canonical orientation,
[
oxed{	ext{central pair word}=0,;X_ioplus Z_i.}
]

Therefore:

- if (X_i=Z_i), the canonical pair insertion contains a central (00) seed;
- if (X_i
e Z_i), the canonical pair insertion contains a central (01) seed.

### Corollary: every disagreement is a threshold seed

Every rail-disagreement index
[
i:quad X_i
e Z_i
]
canonically determines a full order with an exact (01) seed centered at the inserted pair ({x,z}).

Apply the terminating threshold-band construction to the one-change target with switch between these two central windows. Starting from the maximal target-compatible interval containing the (01) seed, outward flat repairs strictly enlarge the interval. Thus every rail disagreement yields either:

1. a spanning NOR-good order; or
2. one or two fully-curved terminal barriers bounding a nonempty matched interval containing the inserted pair.

All repairs occur at the boundary of the matched interval, so the ordered pair ((x,z)) or ((z,x)) used in the seed remains inside the protected central carrier.

### Hartman interpretation

The disagreement set
[
D={i:X_i
e Z_i}
]
is exactly the set of gaps where the canonical pair state changes from a monochromatic (00) seed to a threshold (01) seed.

Since the crossed shortcut residue has
[
X_1
e Z_1,qquad X_{m-1}
e Z_{m-1},
]
the set (D) is nonempty. Its least element is therefore a canonical “smallest obstruction” in the same spirit as Hartman's smallest unreachable label: before it, the canonically oriented pair sees only agreement rungs, while at it the rung flips and a threshold connector seed appears.

Unlike a merely formal label, this least disagreement already has a realized full-order consequence: a terminating threshold transport with the shortcut pair retained in the central provenance.

Hence the Hartman-style search on the crossed ladder can be reduced to studying the first/last rail-disagreement seeds and the protected barriers emitted by their threshold transports.
