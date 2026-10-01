# Seventeen deletion labels force endpoint structure or a uniform incompatibility triple

## Statement

Let H be a minimum counterexample, let D be any set of m>=17 deletion labels, choose one deletion cover F_d of H-d for each d in D, and form the compatibility graph G. Then at least one of the following holds: (i) some label d has three compatibility neighbors on one path of F_d, so the synchronized endpoint conclusion of compatthreeoneside09 holds; or (ii) there exist three labels a,b,c whose chosen deletion covers are pairwise incompatible and whose three pairwise incompatibilities are all support-incompatible, or are all support-compatible but order-incompatible.

## Body

# Proof

Apply compatdegreefour10.

If its synchronized endpoint branch occurs, then some label d has three compatibility neighbors on one path of F_d, and compatthreeoneside09 gives alternative (i).

Otherwise Delta(G)<=4. By compatfourcolor22, G is 4-colorable and therefore contains an independent set of size at least ceil(m/4). Since m>=17, this independent set has size at least five.

Choose five labels in it. Their chosen deletion covers are pairwise incompatible. Since H has at least m>=17 vertices, there is certainly a vertex outside these five labels. Therefore compatfiveuniform25 applies and gives three covers whose three pairwise incompatibilities all have one broad type: all support-incompatible, or all support-compatible but order-incompatible. This is alternative (ii).

Thus seventeen chosen deletion labels already force either synchronized endpoint structure or a uniform three-cover incompatibility pattern.
