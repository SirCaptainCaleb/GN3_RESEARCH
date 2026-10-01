# Two-gap behavior on both cores synchronizes one reverse-cross label pair

## Statement

In the all-three-split branch, suppose neither core exhibits relative-order disagreement among its three chosen Hamilton paths, and suppose on each core the three insertion positions occupy both of the two adjacent gaps from compatallgap23. Then there exist two special labels x,y that lie in different occupied gaps on both R and S. Consequently compatgaplocal24 supplies an explicit reverse cross triple on R involving x,y and the core vertex between its two occupied gaps, and another explicit reverse cross triple on S involving the same pair x,y and the core vertex between its two occupied gaps. Thus the genuinely two-gap/two-gap residue synchronizes one label pair across both disjoint cores.

## Body

# Proof

On R, the two occupied adjacent gaps partition the three labels {a,b,c} into two nonempty classes, hence into a singleton and a pair. Let sigma_R be the singleton label. Likewise the two occupied gaps on S determine a singleton sigma_S.

We claim there are two labels x,y separated by the R-gap partition and also by the S-gap partition.

If sigma_R=sigma_S, choose x=sigma_R and any other label y. Then x and y lie in different gap classes on both cores.

If sigma_R and sigma_S are different, take x=sigma_R and y=sigma_S. On R, x is the singleton while y belongs to the opposite two-label class, so they are separated. On S, y is the singleton while x belongs to the opposite class, so they are again separated.

Thus in all cases some pair x,y uses different adjacent gaps on both R and S.

Apply compatgaplocal24 on R to this pair. Simultaneous insertion of x,y would, together with the remaining special label on S, give a spanning two-cover, so the cross triple coupling the adjacent insertions is non-tight and its reverse is tight. Therefore there is a core vertex r in R such that one of the two orientations (y,r,x) or (x,r,y), specifically the reverse of the attempted simultaneous-insertion cross triple, is tight.

Apply the same argument on S. There is a core vertex s in S giving the analogous reverse cross triple on the same label pair x,y.

Hence the two-gap/two-gap all-split residue forces synchronized reverse-cross witnesses on both disjoint cores using one common pair of special labels.