# Hamilton-normalized distance-two and distance-three chords encode status and curvature — preserved pre-item development

## Composition

(none yet)

## Development

## Hamilton-normalized chord coordinates encode both status and curvature

Work in the coboundary-flat pure-orientation sector with a tournament representative t. Fix a linear coordinate order
pi=(v_1,...,v_n).
Vertex-switch t uniquely up to global complement so that every adjacent edge v_i v_{i+1} is oriented forward along pi. Write the switched tournament as t^pi.

Define
x_i = t^pi(v_i,v_{i+2})
for distance-two chords, and
z_i = t^pi(v_i,v_{i+3})
for distance-three chords.

### Status theorem
For every i,
alpha(v_i,v_{i+1},v_{i+2}) = x_i.
Indeed both adjacent tournament edges are forward in the normalized representative, so the alternating triangle formula reduces to the distance-two chord bit.

Thus the ternary status word is exactly the distance-two chord word.

### Curvature theorem
For four consecutive coordinates
a=v_i,b=v_{i+1},c=v_{i+2},d=v_{i+3},
put
d_i=x_i xor x_{i+1}.
Let
kappa_i
=
alpha(a,b,d) xor alpha(a,b,c),
so that at a transition d_i=1, kappa_i=1 is the fully-curved case and kappa_i=0 is the flat case.

In the Hamilton-normalized tournament,
alpha(a,b,d)
=
x_{i+1} xor z_i.
Therefore
kappa_i
=
x_i xor x_{i+1} xor z_i
=
d_i xor z_i.

Consequently, at an actual transition d_i=1,
- fully curved iff z_i=0;
- flat iff z_i=1.

### Significance
The flat-sector repair problem can be encoded by two binary chord layers:
- x is the observable ternary status word;
- z marks the curvature type of every switch.

The canonical extremal profile 1,p,q,2 with three forced fully-curved transitions therefore has three switch positions where z=0; the remaining possible mobile switch has z=1.

This representation is switching-class exact and avoids repeatedly expanding tetrahedral face tables. The next target is the local update rule for z under an endpoint repair. If the z-update is sufficiently local, the closed-component problem becomes a finite binary transport system on the coupled (x,z) words.
