# An extremal width-two band forces the bad reconnection bit and a one-rank switch shift — preserved pre-item development

## Composition

(none yet)

## Development

## A lexicographically extremal width-two band forces the bad §226 reconnection bit

Work in the coboundary-flat alternating ternary sector. Let a lexicographically maximal two-change full order have global word
0^A 1^2 0^C, with A,C>=1, and suppose its two band boundaries are fully curved. In the rigid branch of §§221,257 normalize the active six coordinates as
(0,1,2,3,4,5)
with internal word 0,1,1,0.

Write the ambient order locally as
...,u,p,q,0,1,2,3,4,5,...
when the displayed left exterior coordinates exist. In the original global two-change word,
alpha(u,p,q)=alpha(p,q,0)=alpha(q,0,1)=alpha(0,1,2)=0.

### The stronger weave

Apply §226:
(0,1,2,3,4,5) -> (0,3,1,2,4,5).
Its internal word is 0,1,1,1, the ordered right pair (4,5) is preserved, and the only new immediate left bit is
r=alpha(q,0,3).

If r=0, the full status word retains the same leading zero run while the isolated 1-band grows from width two to width three. The right exterior is unchanged. This contradicts lexicographic maximality of (A,B).

Therefore every lexicographically extremal rigid width-two band has r=1.

By §226, (q,0,3,1,2) is then a double-full singleton with word 1,0,1.

### Exact one-sided resolution and switch shift

Use the double-full resolution preserving the ordered right pair:
(q,0,3,1,2) -> (0,q,3,1,2).
Its internal word becomes 0,1,1. Thus the ambient order is
...,u,p,0,q,3,1,2,4,5,...
and all statuses from alpha(0,q,3) through the right side of the rigid packet are
0,1,1,1,1.
The right exterior remains unchanged.

There are exactly two uncontrolled left crossing windows:
ell_0=alpha(u,p,0), ell_1=alpha(p,0,q),
with endpoint clipping.

Crucially, even when (ell_0,ell_1)=(0,0), the first 1 occurs one window rank earlier than in the original 0^A 1^2 0^C word. The clean resolved profile is
0^(A-1) 1^4 0^C
(up to endpoint clipping), not 0^A 1^4 0^C.

Hence lexicographic maximality of (A,B) does not exclude the clean resolved state: the primary coordinate A decreased by one.

### Correct theorem

For a lexicographically extremal rigid width-two full/full band:
1. the §226 reconnection bit equals 1;
2. the obstruction is canonically a double-full singleton;
3. its right-preserving resolution widens the local 1-band and confines all remaining uncertainty to two left crossing windows;
4. the resolution shifts the target switch one rank left.

Thus the width-two branch reduces to the tradeoff
(A,2) -> (A-1,4)
plus at most two exported left bits.

This identifies the missing global potential precisely: closure must compare the loss of one leading-phase unit against the gain of two 1-band units, or extract a strict improvement from the exported two-window defect. The ordinary lexicographic potential (A,B) alone is insufficient here.
