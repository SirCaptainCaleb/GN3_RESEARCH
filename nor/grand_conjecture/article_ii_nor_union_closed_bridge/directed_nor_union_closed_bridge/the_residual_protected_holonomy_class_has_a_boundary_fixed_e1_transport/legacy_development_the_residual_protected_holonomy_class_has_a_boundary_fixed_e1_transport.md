# The residual protected holonomy class has a boundary-fixed E=1 transport — preserved pre-item development


Continue the protected switch-insertion setup. Use consecutive coordinates

y,r,a,b,c,x,e,f

with the canonical full-support word

0,0,0,1,0,1

on the six displayed ternary windows. Thus the unique threshold defect is the 0 immediately after the 0-to-1 cut.

Assume the residual protected class u=t=0 from the previous subsection. In fact only u=0 is needed below:

alpha(r,a,c)=alpha(r,b,c)=0.

The two blocker tetrahedra

{x,a,b,c},
{x,b,c,e}

are fully curved.

Perform the adjacent transposition b,c:

(y,r,a,b,c,x,e,f)
->
(y,r,a,c,b,x,e,f).

The ordered left boundary pair (r,a) and ordered right boundary pair (x,e) are unchanged. Hence every ternary window outside the displayed packet is unchanged.

Now compute the six displayed new statuses.

1. alpha(y,r,a)=0, unchanged.

2. alpha(r,a,c)=u=0.

3. alpha(a,c,b)=1-alpha(a,b,c)=1.

4. alpha(c,b,x)=1-alpha(x,b,c)=0, because reversal of the ordered triple (x,b,c) gives (c,b,x), and the blocker scan has alpha(x,b,c)=1.

5. alpha(b,x,e)=1. Indeed in the fully-curved tetrahedron {x,b,c,e}, the ordering (x,b,c,e) has consecutive statuses 1,0, so its remaining predecessor face satisfies alpha(b,x,e)=1.

6. alpha(x,e,f)=1 from the blocker scan.

Thus the local word is exactly

0,0,1,0,1,1.

Relative to the same polarity 0-to-1, this word again has threshold defect exactly one: choose the cut after the second displayed window. The sole defect is then the fourth displayed 0.

Before the surgery the unique optimal local cut is after the third displayed window. Therefore the move preserves E=1 and the threshold polarity while shifting the cut strictly one rank to the left.

Because both ordered boundary pairs are fixed, no hidden outer window changes. This is a genuinely protected full-support surgery.

Consequently the previously residual u=t=0 holonomy class is not locally closed. The canonical switch-insertion state always admits one of the following:
- a suffix-protected repair exporting at most one defect leftward (the earlier u=1 or u=0,t=1 branches);
- or, in the remaining class, this boundary-fixed E=1 transport with a strict cut-position shift.

No deletion witness, omitted vertex, or protected boundary pair is reset in this argument.
