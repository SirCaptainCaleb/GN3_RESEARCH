# Flat preserving three step transport follows a forced distance four chord track — preserved pre-item development

## Development

## Flat-preserving three-step transport follows a forced distance-four chord track

Work in the coboundary-flat sector in Hamilton-normalized tournament coordinates. Let a flat isolated transition separate a left status color x from a right monochromatic run of color 1-x, and suppose a successful right endpoint repair transports that switch by distance three without meeting another transition.

Use consecutive vertices
[
a,b,c,d,q,r,s
]
so the old status packet is
[
x, 1-x, 1-x, 1-x, 1-x.
]
The central switch is flat.

The audited three-step transport law gives the repaired packet
[
x, x, x, V, S
]
with
[
V=x,qquad S=1-x,
]
so the new switch is three positions to the right.

Let
[
U=alpha(c,r,s).
]
Subsection 142 proves:
- the new switch is fully curved iff (U=V=x);
- the new switch is flat iff (U
e V), hence iff
  [
  U=1-x.
  ]

Now let
[
y=t^pi(c,s)
]
be the distance-four chord bit in the Hamilton-normalized tournament before the repair. The same local normalization gives
[
t^pi(c,r)=1
]
on this distance-three branch, and therefore
[
U=alpha(c,r,s)=1oplus y
]
with the established tournament convention.

Consequently the transported switch remains flat exactly when
[
1oplus y=1-x,
]
i.e.
[
oxed{y=x.}
]

### Dichotomy

Every isolated three-step transport of a flat switch has exactly one of two outcomes:

1. **curvature conversion:** the target switch is fully curved; or
2. **flat continuation:** the relevant skipped distance-four chord equals the departing run color.

Thus a mobile flat switch can survive a sequence of three-step transports only by following a prescribed binary track in the distance-four chord layer.

Two-step transports need no such extra bit and preserve flatness automatically.

### Significance

A closed repair component with one mobile switch now has a hierarchical but explicit structure:
- 2-step moves preserve flatness automatically;
- 3-step moves either terminate mobility by creating a full barrier or consume one forced distance-four chord condition.

Hence any indefinitely mobile component determines a constrained walk through the distance-four chord word. A no-cycle proof may now target the impossibility of satisfying these forced chord values around an odd-winding loop, rather than treating higher memory as unconstrained.
