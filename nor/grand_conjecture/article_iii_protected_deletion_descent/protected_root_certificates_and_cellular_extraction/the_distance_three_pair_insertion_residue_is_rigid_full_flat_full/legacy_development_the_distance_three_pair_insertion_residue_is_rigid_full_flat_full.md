# The distance-three pair-insertion residue is rigid full-flat-full — preserved pre-item development

## Development

## The distance-three pair-insertion residue is rigid full-flat-full

Continue with root §159 in the only nonclosing scan-threshold-separation-three branch.

Let the disagreement interval be

i-1,i,i+1,

with x the earlier-switching blocker and y the later-switching blocker. Then

s_{i-1}^x=s_i^x=s_{i+1}^x=0,
s_{i-1}^y=s_i^y=s_{i+1}^y=1.

The bad pair-potential parity has

c_{i-1}=0,
c_i=1,
c_{i+1}=0,
c_{i+2}=1.

Insert the canonically oriented pair y,x at gap i. On the six consecutive coordinates

(A,B,y,x,C,D)
=
(v_{i-1},v_i,y,x,v_{i+1},v_{i+2})

the exact four-window word is

1,0,1,0.

### Left transition is fully curved

The left 10 tetrahedron is

(A,B,y,x).

Its off-faces are

alpha(A,B,x)=s_{i-1}^x=0,

and

alpha(A,y,x)=1.

For a 10 transition, the full pattern has off-faces 0,1. Hence the left tetrahedron is fully curved.

### Middle transition is flat

The middle 01 tetrahedron is

(B,y,x,C).

Its off-faces are

alpha(B,y,C)=0

because alpha(y,B,C)=s_i^y=1,

and

alpha(B,x,C)=1

because alpha(x,B,C)=s_i^x=0.

For a 01 transition, the flat pattern has off-faces 0,1. Hence the middle tetrahedron is flat.

### Right transition is fully curved

The right 10 tetrahedron is

(y,x,C,D).

Its off-faces are

alpha(y,x,D)=0

because alpha(x,y,D)=c_{i+2}=1,

and

alpha(y,C,D)=s_{i+1}^y=1.

Thus it again has the full 10 off-face pattern 0,1 and is fully curved.

Therefore the exact curvature word is

FULL - FLAT - FULL.

### Middle flat repair reduces variation

Repair the middle flat 01 transition by swapping its first pair B,y.

The local six-coordinate order becomes

(A,y,B,x,C,D).

The four ternary statuses are forced to be

0,1,1,0.

Indeed the repaired middle pair is 11, while the first status flips from 1 to 0 and the last status remains 0.

The other endpoint repair gives the mirror local word 1101.

In the codimension-two insertion setting, the untouched carrier immediately before this packet lies in color 0 and the untouched suffix immediately after it lies in color 1.

Hence the full word changes from the five-transition pattern

...0 | 1010 | 1...

to a three-transition one-band pattern such as

...0 | 0110 | 1....

So the 1010 residue is never a terminal primitive obstruction.

### Consequence

A scan-threshold separation-three pair of blockers has only two outcomes:

1. direct 0011 pair insertion closes the full instance; or
2. the rigid 1010 packet appears, with curvature FULL-FLAT-FULL, and one middle flat repair reduces it to a single isolated monochromatic band bounded by the opposite color.

That resulting one-band state is exactly in the threshold-band / double-full transport architecture: flat boundaries move finitely; full boundaries emit protected roots.

Thus codimension-two scan separation three has been reduced to the existing one-band extraction frontier rather than introducing a new recurrence.
