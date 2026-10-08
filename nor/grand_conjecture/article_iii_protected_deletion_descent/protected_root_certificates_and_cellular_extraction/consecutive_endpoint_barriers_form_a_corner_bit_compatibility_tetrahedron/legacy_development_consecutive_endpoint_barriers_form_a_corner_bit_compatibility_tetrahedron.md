# Consecutive endpoint barriers form a corner-bit compatibility tetrahedron — preserved pre-item development

## Composition

(none yet)

## Development

## Consecutive endpoint barriers form a corner-bit compatibility tetrahedron

Consider two consecutive edges of an actual endpoint-root cycle,

x -> y -> z.

Let A be the endpoint partner in a deletion witness omitting y and targeting z. Endpoint full curvature gives

alpha(y,A,z)=0.

Define

theta = alpha(x,A,y),

the missing-corner bit for trying to use A as a partner for the preceding physical edge x->y, and define

h = alpha(x,y,z),

the color of the consecutive physical-cycle triple.

Work on the four-set {x,y,A,z}.

### Coboundary identity

Use the ordered quadruple (x,y,A,z). Coboundary flatness gives

alpha(y,A,z)
xor alpha(x,A,z)
xor alpha(x,y,z)
xor alpha(x,y,A)
=0.

Since

alpha(y,A,z)=0

and

alpha(x,y,A)=1-theta

by alternation, one gets

alpha(x,A,z)=h xor (1-theta).

### Case theta=1: failed corner bit

Then

alpha(x,y,A)=0,
alpha(y,A,z)=0,

so the local order

(x,y,A,z)

has word

00.

Also

alpha(x,A,y)=1,
alpha(A,y,z)=1-alpha(y,A,z)=1,

so the adjacent order

(x,A,y,z)

has word

11.

Thus a failed missing-corner bit produces an exact local phase-toggle pair

00 <-> 11

by swapping the middle coordinates y,A.

The off-faces satisfy

alpha(x,A,z)=h,
alpha(x,y,z)=h.

Hence the same physical triple color is carried on both exterior faces of this toggle.

### Case theta=0: corner-compatible bit

Now

alpha(x,y,A)=1,
alpha(y,A,z)=0,

so

(x,y,A,z)

has a 10 transition.

The off-faces are

alpha(x,y,z)=h,
alpha(x,A,z)=1-h.

Therefore:

- if h=1, the off-faces are 1,0 and the transition tetrahedron is flat;
- if h=0, the off-faces are 0,1 and the transition tetrahedron is fully curved.

In the flat h=1 case, its two endpoint repairs give the constant local orders 00 and 11.

In the full h=0 case, the four-set carries a pinned 10 transition whose slide direction is x->z.

### Interpretation

The missing endpoint Johnson corner is not an unstructured yes/no event.

For two consecutive endpoint states it is encoded by one actual ternary face bit theta:

- theta=1 (corner-incompatible) gives a boundary-matched 00/11 phase toggle;
- theta=0 (corner-compatible) gives a 10 transition, flat or full according to the physical-cycle color h.

This theorem is purely local. It does NOT assert that theta=0 is sufficient to realize a new endpoint deletion witness with partner A, nor that the full theta=0,h=0 transition has the outside-order provenance needed to shorten an endpoint cycle.

Its value is to connect the endpoint square-lift problem to the same flat/full repair cells used by the Sperner/Tucker carrier. The obstruction to corner lifting already appears as a concrete four-coordinate phase-toggle cell rather than an abstract missing cut.
