# Two exterior scans give an exact pair-insertion four-window formula

## Composition

(none yet)

## Development

## Two exterior scans give an exact pair-insertion four-window formula

Let

O=(v_1,...,v_m)

be a one-change carrier in the coboundary-flat alternating ternary sector. Let x,y be two exterior coordinates.

Define their insertion scans

s_i^x=alpha(x,v_i,v_{i+1}),
s_i^y=alpha(y,v_i,v_{i+1}),

and define the pair-potential bits

c_i=alpha(x,y,v_i).

### Coboundary transport identity

Flatness on the four-set {x,y,v_i,v_{i+1}} gives

alpha(x,y,v_i)
xor alpha(x,y,v_{i+1})
xor alpha(x,v_i,v_{i+1})
xor alpha(y,v_i,v_{i+1})
=0.

Hence

c_i xor c_{i+1}
=
s_i^x xor s_i^y.

Therefore the two scans agree on edge i exactly when c_i=c_{i+1}, and disagree exactly when c toggles.

### Consecutive insertion packet

Insert the ordered pair x,y between v_i and v_{i+1}.

The four new ternary windows meeting the insertion are

(v_{i-1},v_i,x),
(v_i,x,y),
(x,y,v_{i+1}),
(y,v_{i+1},v_{i+2}),

with endpoint clipping as usual.

By cyclic invariance,

alpha(v_{i-1},v_i,x)=s_{i-1}^x,
alpha(v_i,x,y)=c_i,

while directly

alpha(x,y,v_{i+1})=c_{i+1},
alpha(y,v_{i+1},v_{i+2})=s_{i+1}^y.

Thus the exact packet is

(s_{i-1}^x, c_i, c_{i+1}, s_{i+1}^y).

If instead the inserted order is y,x, alternation gives the exact packet

(s_{i-1}^y, 1-c_i, 1-c_{i+1}, s_{i+1}^x).

### Disagreement-edge normalization

Suppose the scans disagree at edge i:

s_i^x != s_i^y.

Then c_i != c_{i+1}. Exactly one of the two pair orientations has middle bits

0,1.

Therefore every scan-disagreement edge supplies a canonical orientation of the inserted pair for which the two INTERNAL insertion windows already have the desired one-change direction 0->1.

Only the two outer scan bits remain:

left outer = the scan of the first inserted coordinate at edge i-1,
right outer = the scan of the second inserted coordinate at edge i+1.

### Pair-insertion closure criterion

If the carrier switch is oriented 0^p1^q and the pair is inserted at a gap where the untouched prefix requires color 0 and the untouched suffix requires color 1, then a scan-disagreement edge closes by full pair insertion whenever, in the orientation with middle packet 01,

left outer =0,
right outer=1.

The resulting four-window insertion packet is then

0,0,1,1

or a clipped subpacket, and it splices monotonically into the untouched one-change carrier.

### Relation to identical scans

If the scans are identical, c_i is constant and root §157 handles the pair by switch insertion or an explicit replacement omission.

If the scans differ, the present formula localizes the entire codimension-two obstruction to the TWO outer scan bits adjacent to one disagreement edge.

Thus arbitrary two-blocker interaction is reduced to:

- identical scans: explicit augmentation theorem;
- differing scans: a canonical 01 middle pair plus two outer reconnection bits.

This is a natural interface for endpoint corner lifting and for a Sperner/IVT argument on scan disagreement positions.
