# A relocated xz pair fills the unique bad adjacent-gap A2 residue

## Composition

The proposed relocated-pair filler preserves exterior pairs P,L and R,S and bypasses the bad mutual a,b edge when its old insertion windows are zero and fixed-representative L→a and M→b hold. Those two fixed edges do not follow from arbitrary path-normalized insertion collars. Removing x,z from their previous location also requires a legal collar check. With these conditions the filler gives the advertised rank-two union.

## Development

Use the bad adjacent-gap configuration P,L,M,R,S with uncovered vertices a and b. The insertion collars are P,L->a->M,R and L,M->b->R,S, and the bad mutual orientation is b->a. If the special pair x,z is relocated adjacent into this local cell, then the order P,L,a,x,z,M,b,R,S is monochromatic zero. The seven local windows are zero: P,L,a by the a-collar; L,a,x because L->a and shore vertices dominate x; a,x,z and x,z,M by the shore signature; z,M,b because M->b; M,b,R because M->b->R and M->R; and b,R,S by the b-collar. The exterior ordered pairs P,L and R,S are unchanged. Thus the unique rank-two adjacent-gap obstruction disappears completely once an adjacent xz pair is available locally. No outer incidences P->b or a->S are required.

Unification audit: the special-vertex signatures are in the fixed normalized split, whereas insertion collars may be certified in a path-normalizing gauge. The displayed filler is zero precisely when, in addition to its already certified old insertion windows, L→a and M→b hold in the fixed split representative: these verify α(L,a,x)=0 and α(z,M,b)=0. Arbitrary path-normalized collars do not imply those fixed edges. Removing x,z from their old location also requires a legal collar check. With these prerequisites the local filler preserves the exterior pairs P,L and R,S and eliminates the mutual a,b obstruction without the earlier outer-edge conditions.
