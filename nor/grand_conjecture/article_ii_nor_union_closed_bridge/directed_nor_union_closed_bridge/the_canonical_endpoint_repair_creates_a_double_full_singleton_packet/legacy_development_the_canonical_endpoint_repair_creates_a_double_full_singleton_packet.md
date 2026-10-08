# The canonical endpoint repair creates a double-full singleton packet — preserved pre-item development


Continue with the canonical minimum-counterexample cyclic carrier

1,p,q,2

obtained from a one-change deletion order O=(v_1,...,v_m) of word 0^p1^q and its omitted perfect blocker x. Assume q>=3.

The perfect-blocker scan is

s_i=alpha(x,v_i,v_{i+1})=1^(p+1)0^q.

The wrap transition from the final length-two 0-run into the initial singleton 1-run is flat. Perform its left endpoint repair, swapping the cyclicly adjacent pair v_m,x.

A distance-two transport would land on the occupied q|2 transition and lower cyclic variation from four to two, so counterexamplehood forces the distance-three equality branch. The repaired cyclic order has run profile

1,3,p,q-1

up to rotation.

More importantly, its new singleton run is bracketed by two fully-curved tetrahedra.

Indeed, in the repaired local cyclic sequence

...,v_{m-3},v_{m-2},v_{m-1},x,v_m,v_1,...,

the singleton status is

alpha(v_{m-2},v_{m-1},x)=s_{m-2}=0.

Its left neighboring status is

alpha(v_{m-3},v_{m-2},v_{m-1})=1

because q>=3, and its right neighboring status is

alpha(v_{m-1},x,v_m)=1-s_{m-1}=1.

For the left transition tetrahedron

Q_L={v_{m-3},v_{m-2},v_{m-1},x},

the consecutive statuses are 1,0 and the third relevant face is

alpha(v_{m-3},v_{m-2},x)=s_{m-3}=0.

Since q>=3, s_{m-3}=0. Coboundary flatness therefore gives the fully-curved face pattern.

For the right transition tetrahedron

Q_R={v_{m-2},v_{m-1},x,v_m},

the consecutive statuses are 0,1 and

alpha(v_{m-2},v_{m-1},v_m)=1

from the tail of the q-run. Again the flat-sector parity identity forces the fully-curved pattern.

Thus one legal repair of the canonical perfect-blocker endpoint converts the minimum-counterexample witness into a double-full singleton gadget.

If p and q are not both 2, reverse the deletion order if necessary so that q>=3. Hence the only minimum-counterexample case not covered by this reduction is the exact symmetric residue p=q=2.

This connects minimum-counterexample threshold defect one directly to the previously developed five-set holonomy and double-full cancellation machinery.
