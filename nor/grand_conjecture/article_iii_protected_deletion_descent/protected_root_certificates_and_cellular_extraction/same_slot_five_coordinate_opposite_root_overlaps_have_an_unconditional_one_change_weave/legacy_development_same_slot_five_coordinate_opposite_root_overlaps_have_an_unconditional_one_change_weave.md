# Same-slot five-coordinate opposite-root overlaps have an unconditional one-change weave — preserved pre-item development

## Composition

(none yet)

## Development

## Same-slot five-coordinate opposite-root overlaps have an unconditional one-change weave

Continue the two-root common-cell localization. Suppose
(a,b,c,d)
witnesses the protected 10 slide root
rho=e_a-e_d:
h(a,b,c)=1,
h(b,c,d)=0.

Suppose a second chamber witnesses the opposite root
-rho=e_d-e_a
on
(d,b',c',a):
h(d,b',c')=1,
h(b',c',a)=0.

Assume the two middle pairs share exactly one coordinate, so the union support has five coordinates.

There are two qualitatively different overlap types: the shared coordinate can occupy the same middle slot in the two packets, or opposite middle slots.

### Shared first-middle coordinate

Assume
b=b',
while c and c' are distinct.

By reversal oddness,
h(d,c,b)=1-h(b,c,d)=1.

The opposite-root witness gives
h(b,c',a)=0.

Therefore the five-coordinate order
(d,c,b,c',a)
has ternary word
1, z, 0,
where
z=h(c,b,c')
is arbitrary.

Both binary possibilities
100 and 110
have at most one change.

Hence this five-set has an unconditional NOR-good local order; no tetrahedral flatness, parity identity, or unknown-face classification is needed.

### Shared second-middle coordinate

Assume
c=c',
while b and b' are distinct.

The opposite-root witness gives
h(d,b',c)=1.

By reversal oddness of the first witness,
h(c,b,a)=1-h(a,b,c)=0.

Therefore
(d,b',c,b,a)
has word
1, z, 0,
with
z=h(b',c,b)
arbitrary, and again is automatically one-change.

### Theorem

A five-coordinate overlap of two opposite ternary window-slide certificates can be locally caged only if the shared middle coordinate occupies OPPOSITE middle slots in the two four-packets.

Equivalently, the same-slot overlap always admits an explicit one-change five-coordinate weave.

### Boundary provenance

The weave is a local active-block statement, not automatically a full ambient splice.

In the shared-first case, the order
(d,c,b,c',a)
retains the opposite-root packet's terminal ordered pair (c',a) but changes its initial pair. Thus all possible ambient reconnection risk is one-sided.

The reversed weave gives the mirrored one-sided statement. The shared-second case is symmetric.

Consequently same-slot A4 overlaps are already suitable for the one-sided boundary-transport machinery. A genuinely two-sided five-coordinate compatibility obstruction must be crossed-middle.

### Residual base cases

After the A3/two-term extraction and this lemma, a common-cell two-root protected zero has only:

1. crossed-middle five-coordinate overlap;
2. disjoint-middle six-coordinate overlap;

as genuinely new local support types.

This is a strict refinement of the six-coordinate localization and gives a concrete target for the remaining certificate-persistence theorem.
