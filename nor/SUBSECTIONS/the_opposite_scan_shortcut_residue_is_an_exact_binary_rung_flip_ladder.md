# The opposite-scan shortcut residue is an exact binary rung-flip ladder

## Metadata

- ID: the_opposite_scan_shortcut_residue_is_an_exact_binary_rung_flip_ladder
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 310
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The opposite-scan shortcut residue is an exact binary rung-flip ladder

Work in the sole unresolved two-sided shortcut residue of §§301,305. Let
[
O=(w_1,ldots,w_m)
]
be a NOR-good order of (Vsetminus{x,z}), and define the two exterior insertion scans
[
X_i=alpha(x,w_i,w_{i+1}),qquad
Z_i=alpha(z,w_i,w_{i+1}),
qquad 1le ile m-1.
]

After normalization, the crossed endpoint data are
[
X_1=0,quad Z_1=1,qquad
X_{m-1}=1,quad Z_{m-1}=0.
]

Define the rung bits
[
R_i:=alpha(x,z,w_i),qquad 1le ile m.
]

By the pair-insertion endpoint calculation of §305,
[
R_1=R_m=0.
]

### Exact square law

Apply tetrahedral parity to the four coordinates
[
{x,z,w_i,w_{i+1}}.
]
The four face values are precisely
[
R_i,quad R_{i+1},quad X_i,quad Z_i
]
up to even cyclic reorderings, so
[
R_ioplus R_{i+1}oplus X_ioplus Z_i=0.
]

Therefore
[
oxed{R_{i+1}oplus R_i=X_ioplus Z_i.}
]

Equivalently:

- if the two exterior scans agree at position (i), the rung state is unchanged;
- if the scans disagree, the rung state flips.

Since (R_1=R_m=0), the number of indices at which the two rails disagree is even.

### Pair-insertion interpretation

Insert the ordered pair (x,z) between (w_i) and (w_{i+1}). The four new local windows are
[
X_{i-1},quad R_i,quad R_{i+1},quad Z_{i+1}
]
with the obvious endpoint clipping.

Thus the same ladder square simultaneously records:

1. disagreement of the two one-vertex insertion scans;
2. change of the (x,z) pair-orientation rung;
3. the exact four-window packet created by pair insertion.

### Relation to the Hartman/Connector idea

This is a genuinely reversible local object, unlike the directed prefix automaton. The two rail states (X_i,Z_i) and the rung states (R_i) form a sequence of (mathbb F_2)-squares, and reversing an elementary pair/repair move stays inside the same local square.

Moreover §290 gives forbidden local rail patterns:
- no (010) centered strictly inside the zero phase;
- no (101) centered strictly inside the one phase,
for either rail.

Hence the surviving shortcut obstruction is a constrained two-row binary ladder with fixed crossed boundary data and a closed rung boundary (R_1=R_m=0).

A Hartman/Hex implementation should therefore be sought on this ladder (or its realized repair-square thickening), rather than on the acyclic prefix prism. The next concrete target is to prove that every such realized ladder contains either:
- a pair-insertion packet compatible with the one-change target;
- a rail-to-rail repair connector;
- or a fully-curved protected-root exit.

This is the first setting in which least-unreachable component labels have both reversibility and exact local square provenance.

## Frontier

- Development version when composed: None
- Development version now: 1
