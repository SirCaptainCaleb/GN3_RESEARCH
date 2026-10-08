# The four-state holonomy gadget is transition-optimal for every boundary coloring — preserved pre-item development

## Development

## The four-state holonomy gadget is transition-optimal for every boundary coloring

Use the four local states of ternary subsection 50, all attached through the same ordered boundary pairs (x,a) and (c,e):

full states: 0000 and 1111,
deletion shadows: 001 and 100.

Because the exterior attachment data are identical, fix the binary status l immediately before the local word and r immediately after it. All farther exterior transition counts are common to the four states.

Compute the number of transitions contributed by the local word together with its two boundary adjacencies.

For 0000 the contribution is
[l != 0] + [0 != r].

For 1111 it is
[l != 1] + [1 != r].

For 001 it is
[l != 0] + 1 + [1 != r].

For 100 it is
[l != 1] + 1 + [0 != r].

There are four boundary cases:

- l=r=0: 0000 contributes 0, the other three contribute 2;
- l=r=1: 1111 contributes 0, the other three contribute 2;
- (l,r)=(0,1): 0000,1111,001 each contribute 1, while 100 contributes 3;
- (l,r)=(1,0): 0000,1111,100 each contribute 1, while 001 contributes 3.

Hence the gadget always realizes the minimum possible number of transitions compatible with its two boundary colors:

0 if l=r,
1 if l!=r.

### Consequence

The holonomy-flip six-set cannot itself force excess variation. For every fixed exterior boundary coloring, one of its four full/deletion states joins the two boundary bits with no superfluous color change.

Therefore any global obstruction surviving all four states must already contain its excess transitions in the common exterior reconnection packets. In particular, if deleting the interior of the gadget leaves an exterior status word with at most one required phase change between the two attachment sites, one of the four states produces a global one-change realization.

This gives a clean binary interface for the remaining proof: it is enough to show that the common exterior reconnection data inherited from the perfect-blocker tube have no independent extra oscillation. The internal six-coordinate geometry has been completely optimized away.
