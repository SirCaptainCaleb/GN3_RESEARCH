# Canonical ternary switch packets split into forced flat and forced full descent types — preserved pre-item development

## Development

## Canonical ternary switch packets split into forced flat and forced full descent types

Work in the coboundary-flat alternating ternary sector. Let

O=(...,a,b,c,d,...)

be a one-change deletion witness whose old windows around the switch satisfy

alpha(a,b,c)=0,
alpha(b,c,d)=0,

and insert the omitted coordinate x between b and c. Write the three x-windows

A=alpha(a,b,x),
B=alpha(b,x,c),
C=alpha(x,c,d).

By the unique canonical descent theorem, a bad switch insertion has packet

ABC in {010,100,101,110}.

### Descent in AB: packets 100 and 101

Here

alpha(a,b,x)=1,
alpha(b,x,c)=0.

The transition tetrahedron is Q={a,b,x,c}. For a flat 1->0 transition, the last-pair endpoint repair would require

alpha(a,b,c)=1.

But the old deletion witness gives alpha(a,b,c)=0. Hence this repair criterion fails. In the coboundary-flat transition dichotomy, Q is therefore fully curved.

So every canonical descent of AB type is a forced FULL barrier.

### Descent in BC: packets 010 and 110

Here

alpha(b,x,c)=1,
alpha(x,c,d)=0.

The transition tetrahedron is Q'={b,x,c,d}. For a flat 1->0 transition, the first-pair endpoint repair criterion is

alpha(b,c,d)=0,

which is exactly the old deletion value. Coboundary flatness then forces the complementary endpoint-repair face as well. Hence Q' is flat.

So every canonical descent of BC type is a forced FLAT switch.

### Refined packet table

- 100: unique canonical 10 descent is AB and is fully curved.
- 101: canonical 10 descent AB is fully curved; the later 01 transition BC is also fully curved because flatness there would require alpha(b,c,d)=1, contrary to the old value 0.
- 010: the 01 transition AB is flat and the canonical 10 transition BC is flat.
- 110: the unique canonical 10 transition BC is flat.

### Consequence

The canonical ternary switch state already determines which branch of the Article III fiber/base geometry applies.

- AB-root packets 100,101 are born as transverse full barriers on the true normalized cut.
- BC-root packets 010,110 are born as mobile flat switches and must enter the audited endpoint-repair/threshold-band transport dynamics.

Thus a topology that forces a canonical switch state need not treat all root labels uniformly: the packet label itself supplies a discrete flat/full refinement. The missing canonical-to-terminal provenance bridge exists only for the BC/mobile branch; the AB branch is already a legitimate full barrier at the normalized switch.
