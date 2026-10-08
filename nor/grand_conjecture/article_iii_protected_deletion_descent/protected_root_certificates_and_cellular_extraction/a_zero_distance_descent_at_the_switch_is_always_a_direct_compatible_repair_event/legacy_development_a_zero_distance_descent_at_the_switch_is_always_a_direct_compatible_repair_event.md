# A zero-distance descent at the switch is always a direct compatible repair event — preserved pre-item development

## Composition

(none yet)

## Development

## A zero-distance descent at the switch is always a direct compatible repair event

Work in the coboundary-flat alternating ternary sector with a proposed switch cut whose target colors are

0 on the pre side,
1 on the post side.

Suppose an actual 10 descent occurs at signed transition distance zero, i.e. exactly between the last pre-side window and the first post-side window.

Write the four consecutive coordinates supporting this descent as

(a,b,c,d),

with

alpha(a,b,c)=1,
alpha(b,c,d)=0.

Thus BOTH central windows violate the 0|1 target.

### Flat case

If the transition tetrahedron is flat, then

alpha(a,b,d)=1,
alpha(a,c,d)=0.

The two endpoint repairs are both legal.

Applying the first-pair swap a<->b gives local word

0,0.

Applying the last-pair swap c<->d gives local word

1,1.

Because these swaps are disjoint, applying BOTH gives

(b,a,d,c).

Its two central statuses are

alpha(b,a,d)=1-alpha(a,b,d)=0,

alpha(a,d,c)=1-alpha(a,c,d)=1.

Hence the local word is exactly

0,1,

matching the switch target on both sides.

### Fully-curved case

If the transition tetrahedron is fully curved, then

alpha(a,b,d)=0,
alpha(a,c,d)=1.

Now either single endpoint swap already produces the target pair.

First-pair swap:

(b,a,c,d)

has statuses

alpha(b,a,c)=0,
alpha(a,c,d)=1.

Last-pair swap:

(a,b,d,c)

has statuses

alpha(a,b,d)=0,
alpha(b,d,c)=1-alpha(b,c,d)=1.

So either adjacent swap converts the central 10 into the desired 01.

### Theorem

An actual 10 descent exactly at the proposed switch is never a terminal topological obstruction.

- flat transition: the two commuting endpoint swaps jointly produce the target 01;
- fully-curved transition: either endpoint swap alone produces the target 01.

In every case the two central threshold defects are eliminated by actual adjacent transpositions on the full coordinate order.

Only the outer windows changed by those swaps remain to be audited.

### Relation to the distance-lifted carrier

In the all-descent distance-lifted switch-prism carrier, an occurrence at signed distance zero is therefore already a controlled switch-compatible repair event, not merely a root label.

Hence any support-minimal topological zero with no extractable repair must avoid zero-distance descents entirely. Its scalar balance must be achieved by genuinely opposite-side descents with nonzero signed distances.

This sharpens the large-block frontier: after the small-block zero-free theorem, a remaining zero lives in a block of size at least six and, if unresolved, its positive support contains descents strictly on both sides of the cut but none exactly at it.

The next extraction target is therefore a pair or chain of opposite-side descents whose signed distances straddle zero; use repair transport to reduce their separation or force a compatible gluing event.
