# Odd balanced-cover failures force half-family deletion incompatibility

## Statement

Let H be a minimum-order counterexample to the balanced two-cover conjecture of odd order n=2k+1, and choose one balanced deletion cover F_v of H-v for each vertex v. Let G be their pair-state compatibility graph. For n>=7, e(G)<=floor(n^2/4)+2. Consequently the number of incompatible pairs is at least binom(n,2)-floor(n^2/4)-2=k^2-2. In particular, if k>=4 (n>=9), some chosen balanced deletion cover is incompatible with at least k=(n-1)/2 of the other chosen covers.

## Body

By astra002oddgapgeom03, the compatibility graph has the two graph-theoretic properties used in the abstract near-Mantel lemma:

1. every compatibility edge lies in at most two triangles;
2. every compatibility triangle contains an edge lying in no other triangle (all three edges in the cyclic case, and the source-sink edge in the transitive case).

The abstract graph lemma proved in compatdensityplus2 therefore applies directly and gives

e(G)<=floor(n^2/4)+2

for n>=7.

Now n=2k+1, so

binom(n,2)=k(2k+1)=2k^2+k

and

floor(n^2/4)=k^2+k.

Hence the number of incompatible pairs is at least

(2k^2+k)-(k^2+k)-2
= k^2-2.

The average incompatible degree is therefore at least

2(k^2-2)/(2k+1).

For k>=4,

2(k^2-2) > (k-1)(2k+1),

so this average is strictly greater than k-1. Since incompatible degrees are integers, some vertex has incompatible degree at least k.

Thus in every odd minimum balanced-cover failure of order at least nine, and for every arbitrary selection of balanced deletion covers, one deletion state disagrees in pair-state compatibility with at least half of the other labels.

This is an arbitrary-order consequence of balance plus compatibility geometry; it uses no fixed-order classification.