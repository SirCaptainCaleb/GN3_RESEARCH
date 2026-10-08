# A width-two full-full corridor is an exact barrier-reflection gadget — preserved pre-item development

## Composition

(none yet)

## Development

Work in the coboundary-flat alternating ternary sector. Let six consecutive coordinates (a,b,c,d,e,f) have status word A,B,B,A with B=1-A. Assume both end transitions A->B on {a,b,c,d} and B->A on {c,d,e,f} are fully curved.

Swap only the two central coordinates c,d, obtaining (a,b,d,c,e,f). Exactly four ternary windows change, all inside this six-coordinate packet; exterior windows are untouched.

Full curvature of the first transition gives alpha(a,b,d)=B. Alternation gives alpha(b,d,c)=1-alpha(b,c,d)=A and alpha(d,c,e)=1-alpha(c,d,e)=A. Full curvature of the second transition gives the remaining off-face alpha(c,e,f)=B. Therefore the new four-window word is exactly B,A,A,B.

Thus the central swap implements the involution
A B B A  <->  B A A B
while preserving the entire exterior order and every exterior ternary window.

If the old target switch is between the first and second displayed ranks, then A,B,B are matched and the final A is the first right-side defect. After the swap, move the target switch two ranks to the right, between the third and fourth displayed ranks. Then A,A,B are matched and the initial B is the sole displayed left-side defect.

Hence a width-two corridor bounded by two fully-curved transitions is an exact barrier-reflection gadget: it transfers the local mismatch from one side of the switch to the other and translates the switch by two window ranks, without any exterior spill.

This does not by itself improve total band length, because the matched exterior run may be longer on one side than the other. But it removes all local uncertainty from the first genuine full-full corridor identified in root 216. Any recurrence of such a terminal obstruction is therefore a one-dimensional reflection/translation process, not a new six-coordinate pattern. A global closure argument may seek a monotone potential for successive reflections or combine a reflection with the asymmetric exterior run lengths.
