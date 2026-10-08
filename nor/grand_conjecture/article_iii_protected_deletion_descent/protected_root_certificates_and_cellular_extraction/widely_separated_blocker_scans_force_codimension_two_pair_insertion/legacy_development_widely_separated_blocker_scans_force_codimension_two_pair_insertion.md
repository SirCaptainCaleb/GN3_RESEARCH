# Widely separated blocker scans force codimension-two pair insertion — preserved pre-item development

## Widely separated blocker scans force codimension-two pair insertion

Continue with the exact two-exterior scan formula of root §158.

Let

O=(v_1,...,v_m)

have word 0^p1^q with p,q>=3, and suppose BOTH exterior coordinates x,y block every single-coordinate insertion into this fixed carrier.

The arbitrary-scan blocking theorem gives, for each exterior coordinate z, the nonincreasing five-bit core

s_{p-1}^z >= s_p^z >= s_{p+1}^z >= s_{p+2}^z >= s_{p+3}^z.

Thus each core is a binary step function.

Assume the two cores are distinct. After swapping the names x,y if necessary, suppose x switches from 1 to 0 earlier than y. Then on their disagreement positions

s_i^x=0,
s_i^y=1.

The disagreement positions form one contiguous interval

I=[A,B] subset {p-1,p,p+1,p+2,p+3}.

Put d=|I|.

### Pair-potential alternation

For c_i=alpha(x,y,v_i), flatness gives

c_i xor c_{i+1}=s_i^x xor s_i^y.

Hence c toggles at EVERY i in I.

At a disagreement edge i, the ordered pair x,y has middle insertion bits

(c_i,c_{i+1}).

If these equal (0,1), the orientation x,y is the unique pair orientation whose two internal insertion windows are 01.

If they equal (1,0), the reversed orientation y,x is the unique orientation with internal 01.

Along consecutive disagreement edges these two orientation types alternate.

### Interior disagreement edges

If

A+1 <= i <= B-1,

then the outer scan bits are forced:

s_{i-1}^x=0,
s_{i+1}^y=1.

Therefore whenever such an interior edge has c_i,c_{i+1}=0,1, inserting x,y at gap i gives the exact four-window packet

0,0,1,1.

For the switch-core intervals above, every interior gap lies in

i in {p,p+1,p+2}.

At any such gap the untouched old windows before the insertion are still in the old 0-phase and the untouched suffix after the insertion is already in the old 1-phase. Hence packet 0011 gives a spanning one-change full order.

### Threshold separation at least four closes

If d>=4, there are at least two consecutive interior disagreement edges.

Their pair-potential orientations alternate, so one of them has middle orientation 01 for the ordered pair x,y.

At that edge the packet is 0011 and the full instance closes.

Therefore in a surviving counterexample two blocking scan cores can differ on at most three of the five switch-core positions.

### Exact distance-three residue

Suppose d=3. There is exactly one interior disagreement edge i=A+1.

If its pair-potential orientation is x,y, the packet is again 0011 and closes.

If not, the only orientation producing middle 01 is y,x. Its outer bits are now

s_{i-1}^y=1,
s_{i+1}^x=0.

So the exact four-window insertion packet is

1,0,1,0.

Thus a surviving scan-threshold separation of exactly three positions forces the universal local packet 1010.

### Consequence

For two insertion-blocking exterior coordinates on a common long-phase carrier:

- identical cores are handled by root §157;
- core threshold separation >=4 gives a spanning pair insertion;
- separation 3 gives either a spanning pair insertion or one exact 1010 residue;
- only separations 1,2 and the 1010 distance-three residue remain unconstrained.

This is a codimension-two local classification, independent of ambient order size.
