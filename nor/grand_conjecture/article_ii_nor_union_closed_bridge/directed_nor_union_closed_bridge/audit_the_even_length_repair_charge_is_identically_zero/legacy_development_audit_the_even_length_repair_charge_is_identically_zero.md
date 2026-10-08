# Audit: the even-length repair charge is identically zero — preserved pre-item development

## Development

## Audit: the proposed even-length Z2 charge is tautologically zero

Subsection 134 defined, for an even-length cyclic ternary status word with four changes,
I(C)=J2(C) xor P(C),
where J2 is the global distance-two tournament-chord parity and P is the parity of the sum of the four transition-slot indices. It was suggested that I might distinguish repair components.

In fact I(C)=0 identically.

### Step 1: J2 is just the parity of the cyclic status word

Fix a tournament representative t of the coboundary-flat orientation:
alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a).

For a cyclic coordinate order (v_1,...,v_n), xor all n cyclic ternary statuses. Each adjacent edge bit t(v_i,v_{i+1}) occurs twice and cancels. Also
t(v_{i+2},v_i)=1 xor t(v_i,v_{i+2}).
The n constant 1 terms cancel exactly with the n reversal constants. Therefore

xor_i alpha(v_i,v_{i+1},v_{i+2})
=
xor_i t(v_i,v_{i+2})
=
J2(C).

So J2 is switching-independent and equals the parity of the number of 1-statuses in the cyclic word.

### Step 2: transition-position parity equals the same quantity when n is even

Let the four cyclic run lengths be r1,r2,r3,r4, with colors alternating 0,1,0,1 after a global complement if necessary. Put the first transition at slot
r1,
then the next at
r1+r2,
then
r1+r2+r3,
and the fourth at n, identified with slot 0.

Hence
P
=
r1+(r1+r2)+(r1+r2+r3)
=
r1+r3 mod 2.

The parity of the number of 1-statuses is
r2+r4 mod 2.
Since n=r1+r2+r3+r4 is even,
r1+r3 = r2+r4 mod 2.

Thus
P=J2,
and therefore
I=J2 xor P=0.

### Consequence

Subsection 133 remains valid and useful:
Delta J2 equals the 2-versus-3 transport selector lambda, so every closed repair loop has even parity of distance-three transports.

But subsection 134 does not provide an additional component charge. Its proposed invariant is a tautological identity for even cyclic four-change words.

This correction sharpens the real target: one must prove odd distance-three parity for a hypothetical singleton-trap return loop directly from the geometry/holonomy of that loop; it cannot be obtained by comparing two pre-existing parity invariants on the same status word.
