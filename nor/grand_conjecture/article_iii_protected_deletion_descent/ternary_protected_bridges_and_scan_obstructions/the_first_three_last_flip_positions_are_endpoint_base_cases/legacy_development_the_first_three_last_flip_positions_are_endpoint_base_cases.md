# The first three last-flip positions are endpoint base cases — preserved pre-item development

## The first three last-flip positions are endpoint base cases

Continue in the special perfect-blocker branch and choose j as the last index with h_j=1,h_{j+1}=0. Use the color-0 full-support last-flip order from subsection 54, whose six-set interior and entire right suffix are threshold-compatible.

### Case j=1

There is no old coordinate before a=v_1. The full order begins with the four internal zero windows of the phase-toggle gadget and then follows the clean right suffix. Hence its complete ternary word is of the form

0^*1^*.

So j=1 closes NOR directly.

### Case j=2

There is exactly one old prefix coordinate v_1 before the common pair (x,a), where a=v_2. The only new left crossing window is

alpha(v_1,x,v_2)=1-alpha(x,v_1,v_2)=0

by the special blocker scan. It is followed by the all-zero toggle interior and then the clean right suffix. Again the full order has word

0^*1^*.

So j=2 also closes NOR directly.

### Case j=3

Now the full order begins

(v_1,v_2,x,v_3,...).

Its first two statuses are

alpha(v_1,v_2,x)=alpha(x,v_1,v_2)=1

by cyclic invariance and the scan, and

alpha(v_2,x,v_3)=1-alpha(x,v_2,v_3)=0.

This is the left endpoint version of the 10 barrier, but there is no preceding old zero window.

Delete the first old coordinate v_1. The resulting deletion order begins

(v_2,x,v_3,...).

Its first status is 0, the toggle interior is all 0, and the entire right suffix is the clean one-change continuation from subsection 54. Therefore this is a genuine one-change deletion carrier.

### Endpoint conclusion

The last-flip descent has finite base cases:

- j=1 or 2: a spanning one-change full order exists;
- j=3: a genuine one-change replacement deletion carrier exists;
- j>=4: the middle-coordinate deletion of subsection 56 applies and reduces the obstruction to the earlier bit h_{j-4}.

Thus the only unresolved special-scan behavior is the j>=4 branch with h_{j-4}=1; the leftward reduction cannot run into an undefined endpoint without producing either NOR or another legitimate deletion witness.
