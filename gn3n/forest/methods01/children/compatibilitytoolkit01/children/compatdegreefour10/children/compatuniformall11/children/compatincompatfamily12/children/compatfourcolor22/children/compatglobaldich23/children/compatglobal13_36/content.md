# Thirteen deletion labels force endpoint structure, a uniform triple, or one of two mixed four-cover corridors

## Statement

Let H be a minimum counterexample, let D be any set of m>=13 deletion labels, choose one deletion cover F_d of H-d for each d in D, and form the compatibility graph G. Then at least one of the following holds: (i) the synchronized endpoint conclusion of compatthreeoneside09; (ii) three chosen covers whose three pairwise incompatibilities are uniformly support-incompatible or uniformly support-compatible but order-incompatible; (iii) four pairwise-incompatible covers whose support-compatibility graph is P4 and hence have the two-switch corridor normal form of compatp4switch35; or (iv) four pairwise-incompatible covers whose support-compatibility graph is 2K2 and hence have the core-disagreement / paired-switch normal form of compat2k2switch29.

## Body

# Proof

Apply compatdegreefour10.

If its high-compatibility synchronized endpoint branch occurs, alternative (i) holds.

Otherwise Delta(G)<=4. By compatfourcolor22, G is 4-colorable. Since m>=13,

ceil(m/4) >= 4,

so one color class contains four labels. The corresponding four chosen deletion covers are pairwise incompatible.

If some three of those four covers have all three pairwise incompatibilities of one broad type, alternative (ii) holds.

Assume no such uniform triple exists. Then compatfourpattern26 applies: the support-compatibility graph on the four covers is, up to relabeling, either P4 or 2K2.

In the P4 case, compatp4switch35 gives a common core partition with support-stable endpoint labels and exactly two internal labels switching class across opposite ends of the support-compatible path. This is alternative (iii).

In the 2K2 case, compat2k2switch29 says either the two blue matched pairs already induce different partitions on the common core, or all four covers induce one common core partition and at least one matched side contributes a paired two-label support switch. This is alternative (iv).

Thus thirteen deletion labels suffice to force one of the four explicit structural interfaces.
