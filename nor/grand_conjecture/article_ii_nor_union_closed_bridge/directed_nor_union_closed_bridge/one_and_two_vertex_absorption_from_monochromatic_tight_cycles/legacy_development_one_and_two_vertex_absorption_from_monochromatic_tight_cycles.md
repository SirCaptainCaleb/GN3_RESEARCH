# One- and two-vertex absorption from monochromatic tight cycles — preserved pre-item development

## Composition

(none yet)

## Development

## One- and two-vertex absorption from a monochromatic tight cycle

Let C be a color-0 tight cyclic order with at least three vertices for a reversal-antisymmetric ternary label h. Fix c in C, with predecessor p and successor s, so h(p,c,s)=0. Let C_c^+ be C cut to end in (...,p,c), and let C_{c,start}^+ be C cut to start (c,s,...).

### Lemma 1: one exterior vertex
For x outside C, either h(p,c,x)=0 or h(x,c,s)=0 gives a monochromatic path on C union {x}: respectively append x to C_c^+, or prepend x to C_{c,start}^+.

Both possibilities fail precisely when the center tournament T_c contains the directed triangle
p -> s -> x -> p.
Hence if T_c restricted to {p,s,x} is transitive, at least one extension succeeds. In particular, locally transitive center tournaments let any exterior vertex be absorbed into a monochromatic path using any chosen cycle vertex c.

### Lemma 2: a middle vertex absorbs any second exterior vertex
Suppose x outside C satisfies both
h(p,c,x)=0 and h(x,c,s)=0.
Then for every y outside C union {x}, there is a color-0 tight path on C union {x,y}.

### Proof
The two one-vertex paths are
P_end=(C_c^+,x), ending in (...,c,x),
and
P_start=(x,C_{c,start}^+), starting (x,c,...).
If h(c,x,y)=0, append y to P_end. Otherwise reversal antisymmetry gives h(y,x,c)=0, so prepend y to P_start. In either case the new path is monochromatic and uses every vertex of C union {x,y} exactly once.

No local transitivity hypothesis is needed for Lemma 2. In a transitive T_c, its two premises say precisely that x lies strictly between p and s in the center order.

### Consequences for maximal monochromatic paths
If no monochromatic path exists on C together with any two distinct exterior vertices, no exterior vertex can lie between the cycle neighbors at any center c. Under local transitivity, every exterior vertex is therefore either before both neighbors or after both neighbors at every cycle center.

For a maximal monochromatic path, Lemma 1 does not by itself supply an iterated absorption procedure: the absorbed object is a path rather than a cycle. Lemma 2 supplies a genuine second absorption when its two local comparisons hold. The remaining before/after case is analyzed separately.

### Spanning consequences
A locally transitive instance with a monochromatic cycle omitting at most two coordinates satisfies directed N_4: absorb one omitted vertex monochromatically if necessary, then prepend the last omitted vertex, creating only one additional colored window.

More generally, if the cycle omits at most three coordinates and an exterior middle vertex exists, Lemma 2 produces a monochromatic path missing at most one coordinate, which similarly closes NOR. These are consequences of the general absorption constructions, not a dimension-cutoff strategy.

For a proper cycle in a general instance, every stated construction is on its indicated support. Unincorporated ambient coordinates remain part of the closure obligation.
