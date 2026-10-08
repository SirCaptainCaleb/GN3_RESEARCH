# Every lexicographically extremal width-two type forces the same left double-full kernel

## Metadata

- ID: every_lexicographically_extremal_width_two_type_forces_the_same_left_double_full_kernel
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 272
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

The strong weave (a,d,b,c,e,f) has word 0111 for every exact width-two six-set type. It preserves the first coordinate and final ordered pair. In a lexicographic extremum its one left crossing bit is forced to one, producing a double-full 101 packet. The right-preserving resolution gives 01111 and the exact left export ell_0,1, with the second bit forced by alternation. Thus every width-two type shares one left split-band normal form. Realized elimination of that exported kernel remains open.

## Development

## Every lexicographically extremal width-two type forces the same left double-full kernel

Work in the coboundary-flat alternating ternary sector. Let a lexicographically maximal global two-change order contain six consecutive coordinates
(a,b,c,d,e,f)
with local word
0,1,1,0
and both bounding transitions fully curved.

By §257,
alpha(b,c,e)=1.
From the original word and full curvature at the left boundary,
alpha(b,c,d)=1, alpha(a,b,d)=1.
From full curvature at the right boundary,
alpha(c,e,f)=1.

These values are independent of the two free six-set bits r=alpha(a,b,f) and s=alpha(b,c,f) of §264.

### Uniform strong weave

Replace
(a,b,c,d,e,f)
by
(a,d,b,c,e,f).

Its four internal statuses are
alpha(a,d,b)=1-alpha(a,b,d)=0,
alpha(d,b,c)=alpha(b,c,d)=1
by cyclic invariance,
alpha(b,c,e)=1,
alpha(c,e,f)=1.

Hence every one of the four lexicographic six-set types admits the SAME internal weave
0,1,1,1.

The weave preserves:
- the first coordinate a;
- the ordered final pair (e,f).

Therefore the whole right exterior is unchanged, and on the left only the immediate crossing bit can change.

Write the old ambient prefix as
...,p,q,a,b,c,d,e,f,...
when the displayed coordinates exist. The old leading zero phase gives
alpha(p,q,a)=0,
alpha(q,a,b)=0.
Put
z=alpha(q,a,d).

If z=0, the new full order remains in the global two-change class with exactly the same leading zero run and with its 1-band widened from width two to width at least three. This contradicts lexicographic maximality.

Therefore
z=1.

### The induced 101 packet is double-full

The five consecutive coordinates
(q,a,d,b,c)
have status word
1,0,1:
alpha(q,a,d)=1,
alpha(a,d,b)=0,
alpha(d,b,c)=1.

The right transition is carried by the tetrahedron {a,b,c,d}, which is fully curved by hypothesis.

For the left transition, use tetrahedral parity on {q,a,b,d}. We know
alpha(q,a,b)=0,
alpha(q,a,d)=1,
alpha(a,b,d)=1.
Hence
alpha(q,b,d)=0.
By alternation,
alpha(q,d,b)=1.

Thus for the ordered transition
(q,a,d,b)
with colors 1->0, the two off-face values are
alpha(q,a,b)=0,
alpha(q,d,b)=1,
which is exactly the fully-curved pattern.

Hence (q,a,d,b,c) is a double-full isolated singleton.

### Right-preserving resolution and exact exported kernel

Apply the one-sided double-full resolution preserving the ordered right pair:
(q,a,d,b,c) -> (a,q,d,b,c).

Its internal word becomes
0,1,1.
Together with the unchanged continuation through e,f, the resolved packet has
0,1,1,1,1.

The entire right exterior remains unchanged.

On the left, exactly two crossing windows may differ. If the old prefix is
...,u,p,q,a,...,
write them as
ell_0=alpha(u,p,a),
ell_1=alpha(p,a,q).

The second one is forced:
alpha(p,q,a)=0
in the old zero phase, so alternation gives
ell_1=alpha(p,a,q)=1.

Therefore every lexicographically extremal width-two full/full state, regardless of its six-set type (r,s), reduces to the SAME one-bit exported kernel
old zero prefix | ell_0,1,0,1,1,1,1 | old zero suffix,
with only ell_0 undetermined.

### Consequence

The four symbolic six-set types of §264 need not be treated separately for the strong-weave handoff. Their common forced data already imply the same double-full left export.

Thus the entire width-two lexicographic frontier has one universal local normal form:
- one free exported left bit;
- one forced intervening 1;
- a one-window zero valley;
- a protected 1-band of length at least four;
- the old right zero suffix unchanged.

The remaining issue is global progress for this one-bit kernel. In particular, ordinary lexicographic (A,B) extremality is insufficient because the right-preserving singleton resolution shifts the target switch one rank left.
