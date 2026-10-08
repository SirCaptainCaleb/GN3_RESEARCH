# Minimum flat-sector endpoint runs have length at least four — preserved pre-item development

## Composition

(none yet)

## Development


Let O=(v_1,...,v_m) be a one-change deletion carrier of word 0^p1^q in a minimum coboundary-flat ternary counterexample, with omitted perfect blocker x and scan 1^(p+1)0^q.

The previous endpoint argument gives p,q>=3. We now exclude p=3.

For p=3, the first two blocker-tube tetrahedra

{x,v_1,v_2,v_3},
{x,v_2,v_3,v_4}

are fully curved.

Consider the full order

(v_3,v_1,v_2,x,v_4,v_5,...,v_m).

Its ternary statuses are:

1. alpha(v_3,v_1,v_2)=alpha(v_1,v_2,v_3)=0 by cyclic invariance.

2. alpha(v_1,v_2,x)=alpha(x,v_1,v_2)=1 by cyclic invariance of a ternary alternating orientation and the blocker scan.

3. alpha(v_2,x,v_4)=1. Indeed full curvature of {x,v_2,v_3,v_4} gives alpha(x,v_2,v_4)=0, and swapping the first two entries complements the value.

4. alpha(x,v_4,v_5)=1 because the blocker scan begins with p+1=4 ones.

Every later status is an untouched status of O beginning at w_4. Since p=3, all of these statuses lie in the 1-run.

Thus the full word is

0,1,1,...,1,

with one change, contradiction.

Therefore p cannot equal 3. Reversing the deletion carrier exchanges p and q, so q cannot equal 3 either.

Hence every minimum counterexample in the coboundary-flat ternary sector must satisfy

p,q>=4.

The p=3 closure is a boundary phenomenon: it uses only the first two fully-curved blocker-tube tetrahedra and does not by itself yield a uniform induction for longer p.
