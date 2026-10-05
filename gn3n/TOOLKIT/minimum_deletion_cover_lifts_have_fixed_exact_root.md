# Minimum deletion-cover lifts have a fixed exact root

**Summary:** For a minimum deletion set X and any two-cover H-X=P|Q, every lift obtained by inserting the vertices of X between P and reverse(Q) has exact deficiency |X| and root determined only by |P| and |Q|.

## Statement

Let |X|=kappa_2(H)=k and let H-X=P|Q with |P|=r, |Q|=s. For every ordering x_1,...,x_k of X, put pi=(P,x_1,...,x_k,Q^rev). Then p(pi)=r-1, q(pi)=r+k, c(pi)=s-1, and delta(pi)=k. Hence psi(pi)=e_{r-1}-e_{s-1}, independent of the ordering of X.

## Body

The deletion-distance identity gives delta(pi)<=k for every such lift: statuses wholly inside P are tight, so p(pi)>=r-1, while statuses wholly inside Q^rev are non-tight, so q(pi)<=r+k. Since k=kappa_2(H) is the global minimum deletion distance, every spanning order has delta(pi)>=k. Therefore equality holds throughout q-p-1<=k, forcing p=r-1 and q=r+k. Since m+1=n-1=r+s+k-1, c=m+1-q=s-1. Thus the exact root is e_{r-1}-e_{s-1} and is independent of the internal ordering of the minimum deleted set.

## Metadata

- ID: minimum_deletion_cover_lifts_have_fixed_exact_root
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
