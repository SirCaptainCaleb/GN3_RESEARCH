# An immediate t=1 full-flat blocker after the antipodal exit closes

## Composition

(none yet)

## Development


Work in the residual right exit of the exact d=e=3 antipodal braid. Use the audited local order

...,x,c,d,y,e,f,g,...

with threshold colors

alpha(x,c,d)=0,
alpha(c,d,y)=1,
alpha(d,y,e)=1,
alpha(y,e,f)=0,

and untouched old 1-suffix, in particular

alpha(c,d,e)=1.

Assume the singleton defect alpha(y,e,f)=0 is blocked immediately, before any successful rightward transport. Then the five-set

(d,y,e,f,g)

is the surviving t=1 full-flat packet (in the color-complemented normalization of subsection 27).

Use its target-color exit, which in the present color-1 normalization replaces

(d,y,e,f,g)

by

(y,e,d,f,g)

and is internally monochromatic 1 while preserving the ordered outward boundary pair (f,g).

It remains only to check the two left reconnection windows.

First, the exact antipodal pair-crossing data give

alpha(x,y,c)=0.

By alternation,

alpha(x,c,y)=1.

Second, the tetrahedron {c,d,y,e} lies in the coboundary-flat sector. Its known faces satisfy

alpha(c,d,y)=1,
alpha(d,y,e)=1,
alpha(c,d,e)=1.

The flat four-face XOR identity therefore forces

alpha(c,y,e)=1.

Hence after the target-color exit the full local connection is

alpha(x,c,y)=1,
alpha(c,y,e)=1,

followed by the internally monochromatic 1-block and the unchanged old 1-suffix.

The old prefix through alpha(x,c,d)=0 is unchanged. Therefore the resulting full spanning order has exactly one 0-to-1 transition.

Thus an immediate t=1 full-flat blocker cannot survive in a counterexample.

Equivalently, in the transport-count notation of subsection 31, the case m=0 is closed. Together with the late-blocker theorem, only m=1 and m=2 remain for the combinatorial flat-sector reflection problem.
