# Triangle-type classification of the Class-III nine-vertex residual obstruction

## Statement

In the residual obstruction R of 213f75e9692a, let A,B,C be the three degree-three vertices and let F_x,F_y,F_z be the off-star matchings induced by the three vertices x,y,z of e (so F_x omits A, F_y omits B, F_z omits C). At most one of F_x,F_y,F_z contains its available high-high pair. More precisely:

(i) If exactly one matching is high-high, then R has triangle-type counts (n_0,n_1,n_2,n_3)=(0,5,2,0), where n_i is the number of R-edges containing exactly i high vertices. Exactly four lows are external high-low mates, each has exactly two high neighbors in R, and the other two lows are adjacent in R to all three highs.

(ii) If no matching is high-high, then R has triangle-type counts either (0,6,0,1) or (1,3,3,0). Every low is the external mate of exactly one high and is adjacent in R to exactly the other two highs.

## Body

Every pair of residual vertices is in exactly one of four classes: it lies in an edge of R; it is an off-star pair in exactly one of F_x,F_y,F_z; or it is one of the three residual uncovered pairs among the six low vertices. Indeed R contributes 7*3=21 covered pairs, the three star matchings contribute 12 pairwise distinct pairs, and the residual leave contributes 3 pairs, totaling C(9,2)=36.

In particular, for any high vertex, its two nonneighbors in the 2-shadow of R are exactly its mates in the two star matchings that contain it.

Now suppose a star matching pairs a high t to a low o. By 213f75e9692a there is no three-edge path in R ending at t while avoiding o. Applying d9c5b28c09a0, o is adjacent in R to both of the other high vertices. Since the pair to t is external, o has exactly those two highs as its high neighbors in R.

It follows immediately that a low cannot be externally paired to two different highs: if o were externally paired to t and t', the first pairing would force o adjacent in R to t', contradiction.

Let h be the number of star matchings among F_x,F_y,F_z that use their available high-high pair. Then the number of external high-low pairs is 2(3-h). By the preceding paragraph these use distinct lows.

We now count the triangle types of R. Let n_i be the number of R-edges containing exactly i of A,B,C. We have
n_0+n_1+n_2+n_3=7,
n_1+2n_2+3n_3=9
from the total high degree 3+3+3=9, and
3n_0+2n_1+n_2=12
from the total low degree 6*2=12.

Also the number of high-high pairs covered in R is n_2+3n_3. Each of the three possible high-high pairs is either covered in R or is the unique high-high pair of the corresponding star matching, so
n_2+3n_3=3-h.

Solving the nonnegative integer equations, using 0<=3-h<=3, gives only:
- h=1: (n_0,n_1,n_2,n_3)=(0,5,2,0);
- h=0: either (0,6,0,1) or (1,3,3,0).
In particular h<=1, recovering and strengthening 9e8ff6352a95.

If h=1, there are four external high-low pairs, hence four distinct lows with exactly two high neighbors in R. The other two lows have no external high mate. Since their uncovered mates are low and every high-low pair not external lies in R, each of those two lows is adjacent in R to all three highs.

If h=0, there are six external high-low pairs on six distinct lows. Thus every low is externally paired to exactly one high and, by d9c5b28c09a0, is adjacent in R to exactly the other two highs.

This proves the classification.