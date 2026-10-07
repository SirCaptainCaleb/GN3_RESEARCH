# Canonical ternary switch packets split exactly into full and flat descent types

## Metadata

- ID: canonical_ternary_switch_packets_split_exactly_into_full_and_flat_descent_types
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 105
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Canonical ternary switch packets split exactly into full and flat descent types

Let a ternary one-change deletion witness have old local coordinates

...,a,b,c,d,...

around its normalized switch, with

alpha(a,b,c)=0,
alpha(b,c,d)=0.

Insert the omitted coordinate x between b and c. Write the three x-packet colors

A=alpha(a,b,x),
B=alpha(b,x,c),
C=alpha(x,c,d).

By the unique canonical-descent theorem, counterexamplehood forces

ABC in {010,100,101,110},

with exactly one internal 10 descent.

### Left-pair descent packets: 100 and 101

Here the unique descent is

A B = 1 0

on the transition tetrahedron {a,b,x,c}, in the ordered packet (a,b,x,c).

A flat 10 transition would admit the last-pair repair and therefore require

alpha(a,b,c)=alpha(a,b,x)=1.

But the old deletion witness gives alpha(a,b,c)=0.

Hence the last-pair repair fails. In the coboundary-flat ternary sector every transition tetrahedron is either flat with both endpoint repairs available or fully curved with neither available. Therefore {a,b,x,c} is fully curved.

Thus packets 100 and 101 produce an immediate fully-curved canonical barrier at the true normalized switch.

### Right-pair descent packets: 010 and 110

Here the unique descent is

B C = 1 0

on {b,x,c,d}, ordered as (b,x,c,d).

For a flat 10 transition, the first-pair repair requires

alpha(b,c,d)=0.

This is exactly the old deletion-witness value.

In the coboundary-flat sector the endpoint-repair classification therefore forces {b,x,c,d} to be flat: the repair criterion on this side is satisfied, so the tetrahedron cannot be fully curved.

Hence packets 010 and 110 enter the audited flat transport mechanism immediately.

### Dichotomy

At the ternary canonical switch insertion there is no third local curvature regime:

- 100 or 101: unique canonical root and immediate fully-curved barrier;
- 010 or 110: unique canonical root and immediate flat transport.

Therefore the canonical-switch stage feeds directly into the two global Article III architectures:

1. fully-curved canonical roots remain on the genuine minimum-first Johnson layer and are eligible for separation/exchange-realization arguments;
2. flat canonical roots generate a one-sided transport flag in the graded central-cut Boolean simplex, whose roots are zero-free along each individual trajectory by root §104.

This removes any need to choose a canonical root or guess its first curvature type in ternary arity.

## Frontier

- Development version when composed: None
- Development version now: 1
