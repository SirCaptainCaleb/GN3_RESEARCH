# A terminal width-two full-full corridor has a rigid three-rotation six-set — preserved pre-item development

## Composition

(none yet)

## Development

## Rigid classification of the width-two full-full corridor

Normalize a globally maximal-band width-two full-full corridor to six consecutive coordinates
(0,1,2,3,4,5)
with status word
0,1,1,0.
Assume the target transition on {0,1,2,3} and the unresolved boundary on {2,3,4,5} are fully curved.

Full curvature gives
alpha(0,1,3)=1, alpha(0,2,3)=0,
alpha(2,3,5)=0, alpha(2,4,5)=1.

On the middle four-set {1,2,3,4}, parity gives
alpha(1,2,4)=alpha(1,3,4)=t.

### The t=0 branch strictly improves the maximal band

Swap only coordinates 3 and 4:
(0,1,2,3,4,5) -> (0,1,2,4,3,5).

The four displayed statuses become
alpha(0,1,2)=0,
alpha(1,2,4)=t,
alpha(2,4,3)=0,
alpha(4,3,5)=1.

If t=0 this is
0,0,0,1.
Move the cut two ranks right, between the third and fourth displayed windows. The whole packet is then target-compatible. The swap preserves the ordered left prefix (0,1,2), so all old matched windows to the left are unchanged; any new right reconnection window lies strictly beyond the old first mismatch. Unlike endpoint relocation, no window rank is deleted. Therefore the maximal compatible band strictly enlarges, contradiction.

Hence every terminal width-two full-full corridor has
alpha(1,2,4)=alpha(1,3,4)=1.

### Rotate the right barrier

Move coordinate 3 across 4 and 5:
(0,1,2,3,4,5) -> (0,1,2,4,5,3).

Using the established values, the local status word is again exactly
0,1,1,0.
The first mismatch occurs at the same local rank, so this new state has exactly the same compatible-band length and the same distance-two right boundary. Its left exterior is unchanged because the prefix (0,1,2) is fixed.

The mixed flat/full distance-two theorem therefore forces the NEW target tetrahedron {0,1,2,4} to be fully curved; otherwise this equally extremal state would be an impossible flat/full corridor. Thus
alpha(0,1,4)=1,
alpha(0,2,4)=0.

Apply the t=0 exclusion to this rotated width-two state. Its middle bit is alpha(1,2,5), so
alpha(1,2,5)=1.

Rotate once more:
(0,1,2,4,5,3) -> (0,1,2,5,3,4).
Again the local word is 0,1,1,0 with unchanged left exterior and the same extremal band data. Its target tetrahedron {0,1,2,5} must be fully curved, giving
alpha(0,1,5)=1,
alpha(0,2,5)=0.

### Forced six-set table

Thus a genuinely terminal width-two residue satisfies, for x in {3,4,5},
alpha(0,1,x)=1,
alpha(0,2,x)=0,
alpha(1,2,x)=1,
in addition to
alpha(0,1,2)=0
and the fully-curved right-barrier data
alpha(2,3,4)=1,
alpha(2,3,5)=0,
alpha(2,4,5)=1,
alpha(3,4,5)=0.

Coboundary parity then determines the remaining increasing triples on the six-set:
alpha(0,3,4)=1,
alpha(0,3,5)=0,
alpha(0,4,5)=1,
alpha(1,3,4)=1,
alpha(1,3,5)=0,
alpha(1,4,5)=1.

So the terminal width-two obstruction is a single rigid six-coordinate alternating-flat pattern, up to relabeling, reversal, and color complement.

### Significance

Width two is not an arbitrary barrier reflection. Either it strictly enlarges the compatible band, or it collapses to this rigid three-rotation residue. The remaining closure problem can therefore target this exact six-set together with its two exterior ordered boundary pairs, rather than all full-full corridors.
