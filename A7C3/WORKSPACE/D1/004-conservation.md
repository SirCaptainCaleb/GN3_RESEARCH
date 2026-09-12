# One conservation law controls the fragmented excess budget

**Workspace:** D1
**State:** established
**Key:** `conservation`

**Summary:** For every exact two-cover, r_Y+p+delta_X=6. In the bounded branch its slack records exactly extra X-X edges and extra X rail-end occupancy.

General counting reference: D13/selected-forest-counting proves c(F-K)=k+|K|-e_F(K)-delta_F(K) for any selected k-path forest. Taking F=T, k=2, and K=X with |X|=4 gives the conservation identity below. The geometric LOW/MAX deductions remain specific to this section.

Let X=G_3 union G_4 and Y=G_0 union G_1 union G_2. For an arbitrary exact two-cover T put p=e_T(X), q=e_T(X,Y), r_Y=c(T[Y]), and delta_X=sum_{x in X}(2-d_T(x)). Because T is a spanning forest of exactly two paths, it has |W|-2 edges. The induced Y-forest has |Y|-r_Y edges, so counting the remaining selected edges gives p+q=r_Y+2. Summing selected degrees over the four X vertices gives 2p+q, hence delta_X=8-(2p+q). Eliminating q yields the unconditional identity
 r_Y+p+delta_X=6.
The total endpoint deficiency of a two-path forest is four, so delta_X is literally the number of its four rail-end slots occupied by X, with an isolated X vertex occupying two.

Now assume the BOUNDED branch of R885, and let f be the number of fragmented X cells. Every unfragmented X cell contributes its internal selected edge, so p>=2-f, and its forced initial/terminal placement contributes an X endpoint slot, so delta_X>=2-f. Define
 s=(p-(2-f))+(delta_X-(2-f))>=0.
Substitution into the conservation identity gives
 r_Y=2+2f-s.
Thus MAX is exactly s=0, namely p=2-f, delta_X=2-f, r_Y=2+2f, and q=2+3f. Each fragmented marker then has d_Y=2 and c=1+2f; in each unfragmented cell the inner vertex has d_Y=1,c=2+2f and the outer endpoint has d_Y=0,c=3+2f. The three specializations are f=0: (p,q,r_Y)=(2,2,2), c multiset {2,2,3,3}; f=1: (1,5,4), d_Y multiset {2,2,1,0}, c={3,3,4,5}; f=2: (0,8,6), all c=5.

LOW is exactly s>=1, so it has a physical meaning: either an extra selected X-X edge beyond the forced internal edges of unfragmented cells, or an extra X rail-end slot beyond the forced outer endpoints. At f=2 there is no forced contribution, so LOW4 iff p+delta_X>=1. Any selected X-X edge must then be cross-cell, one of ab,az,cb,cz, because both native dimers are fragmented; the other alternative is an X rail endpoint. Moreover 5-r_Y=p+delta_X-1. This is the complete R901 conservation proof and physical LOW4 normal form. It unifies the numerical faces, but does not imply the M/N skeletons or endpoint labels proved separately.
