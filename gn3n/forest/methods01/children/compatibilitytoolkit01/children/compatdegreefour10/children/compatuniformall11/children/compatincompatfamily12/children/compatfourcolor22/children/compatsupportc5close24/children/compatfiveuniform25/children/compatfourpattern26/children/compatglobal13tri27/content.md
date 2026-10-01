# Thirteen deletion labels force endpoint structure, a uniform triple, or one of two four-cover patterns

## Statement

Let H be a minimum counterexample, let D be any set of m>=13 deletion labels, choose one deletion cover F_d of H-d for each d in D, and form the compatibility graph G. Then at least one of the following holds: (i) some label d has three compatibility neighbors on one path of F_d, so the synchronized endpoint conclusion of compatthreeoneside09 holds; (ii) there are three labels whose chosen deletion covers are pairwise incompatible and whose three pairwise incompatibilities all have the same broad type; or (iii) there are four pairwise incompatible chosen deletion covers whose support-compatibility graph is, up to relabeling, P_4 or 2K_2.

## Body

# Proof

Apply compatdegreefour10.

If the synchronized endpoint branch occurs, alternative (i) holds.

Otherwise Delta(G)<=4. By compatfourcolor22, the compatibility graph is 4-colorable, so it has an independent set I of size at least ceil(m/4). For m>=13 this gives |I|>=4. Thus the covers indexed by any four labels in I are pairwise incompatible.

If some three of these four covers have all three pairwise incompatibilities of the same broad type, then alternative (ii) holds.

Otherwise the four covers contain no uniform incompatibility triple. Apply compatfourpattern26. Their support-compatibility graph is P_4 or 2K_2, giving alternative (iii).

Hence every family of at least thirteen chosen deletion labels already enters either the synchronized endpoint branch, a uniform three-cover incompatibility branch, or one of two rigid four-cover mixed patterns.