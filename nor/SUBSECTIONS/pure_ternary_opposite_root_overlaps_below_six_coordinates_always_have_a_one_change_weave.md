# Pure ternary opposite-root overlaps below six coordinates always have a one-change weave

## Metadata

- ID: pure_ternary_opposite_root_overlaps_below_six_coordinates_always_have_a_one_change_weave
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 175
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## In pure ternary orientation every five-coordinate opposite-root overlap has a one-change weave

Continue with opposite protected ternary slide roots

(a,b,c,d): 10,
(d,b',c',a): 10.

Root 171 handled the five-coordinate cases in which the shared middle coordinate occupies the same middle slot, using only reversal oddness.

Now assume alpha is a pure alternating ternary orientation. Cyclic permutations of an ordered triple preserve alpha, while a transposition complements it. This removes the two crossed-middle cases as well.

### Crossed case b=c'

Write
b=c'=m,
c=u,
b'=v.

The two root packets are

(a,m,u,d): 10,
(d,v,m,a): 10.

Thus
alpha(m,u,d)=0,
so reversal gives
alpha(d,u,m)=1.

Also
alpha(v,m,a)=0.
The cyclic permutation
(v,m,a) -> (m,a,v)
is even, hence
alpha(m,a,v)=0.

Finally reversal of
alpha(a,m,u)=1
gives
alpha(u,m,a)=0.

Therefore the five-coordinate order

(d,u,m,a,v)

has word

1,0,0.

It is NOR-good on the active five-set.

### Crossed case c=b'

Write
c=b'=m,
b=u,
c'=v.

The packets are

(a,u,m,d): 10,
(d,m,v,a): 10.

This is the reversal/relabeling of the previous crossed pattern. Explicitly,

alpha(a,u,m)=1,
alpha(u,m,d)=0,

and the second packet gives
alpha(d,m,v)=1.

The order

(a,u,m,d,v)

has:
alpha(a,u,m)=1,
alpha(u,m,d)=0,
alpha(m,d,v)=0,

because (d,m,v) -> (m,d,v) is one transposition.

Hence its word is again 100.

### Theorem

For a pure alternating ternary orientation, every five-coordinate overlap of two opposite actual window-slide 10 certificates admits an explicit one-change ordering of the five active coordinates.

Combining with the four-coordinate A3 extraction, a two-root protected cancellation in one carrier cell can be genuinely new only if the two middle pairs are disjoint.

Equivalently, its active support must be exactly six distinct coordinates:

(a,b,c,d)
and
(d,e,f,a),

with {b,c} disjoint from {e,f}.

### Significance

This uses only alternation and the two certified 10 packets; no tetrahedral coboundary-flatness is used.

Thus two independent localization routes now meet at the same scale:

1. common-cell certificate persistence reduces any two-root zero to at most six active coordinates;
2. in pure ternary orientation all support sizes four and five admit local extraction/weaving;
3. the distance-lifted fixed-point carrier independently excludes forced zeros on faces whose blocks have size at most five.

The exact six-coordinate disjoint-middle packet is therefore the first genuinely new local two-root obstruction in the pure ternary sector.

As before, a local good active-set weave is not automatically a full ambient splice; boundary-collar compatibility remains to be checked.

## Frontier

- Development version when composed: None
- Development version now: 1
