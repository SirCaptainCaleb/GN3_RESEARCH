# A clean high-rank terminal source gives a central contact capacity bound

## Statement

Let e={x,v,u} be ascending nonspecial of rank q, and S a clean maximum source path of length q-1 ending at x. Let F_R be any family of distinct other ascending nonspecial edges through terminal v, all of rank at most R<=q. Then
|F_R| <= max(0,4R-2q-1).
In particular no such edge has rank below (q+1)/2, and at the integer equality boundary there is at most one. This replaces the proposed repeated-halving mechanism, which does not yield a substantial low-rank family.

## Body

Fix f={a,v,b} of rank r<=R, with unique entrance a. If S avoids a,b, the linear path S,e,f has q+1 edges ending in f, contradicting r<=q. Thus S meets a or b.

If S contains a, use a as a contact. Both minimal S-segments from its ends to a are endpoint paths at a and have length at most phi(a)=r-1<=R-1.
If S avoids a, its only contact with f is b. Append f to either minimal S-segment ending at b. The path enters f through terminal b and may end at its nonterminal entrance a, so its length is at most r-1. Both S-segments therefore have length at most r-2<=R-1.

Every f supplies a vertex of S within R-1 edges of both ends, and different f supply different vertices by linearity at v. Put N=q-1. For R<=q-1 the allowed region, when nonempty, is the host segment between the junction after edge q-R and the junction after edge R-1. Its length is (R-1)-(q-R)=2R-q-1; zero length means the single common junction. It contains 4R-2q-1 vertices. If the difference is negative, no vertex satisfies both distance conditions. For R=q, use the full vertex count |V(S)|=2q-1, equal to the claimed expression. This also handles private vertices correctly: reaching a private vertex requires its host edge on both sides.

An optional sharper fact from the nonspecial cycle bound: if S meets f only in its entrance a, q<=2r-2; if only in the other terminal b, q<=2r-3. The S-tail from its contact to x, together with e,f, is a linear cycle, so its length plus two is <=r. The prefix bound is r-1 at a, or r-2 at b by the preceding nonterminal extension. The two segment lengths sum to at least q-1. These facts imply the stated sharper inequalities; they are not needed for the capacity bound.