# Compatibility components force a large canonical-state family or a large pairwise-incompatible deletion family

## Statement

Let H be a minimum counterexample, let D be a set of m deletion labels, and choose one two-cover F_v of H-v for every v in D. Form the compatibility graph G on D. For every integer t>=2, at least one of the following holds: (i) some connected component of G has at least t labels, and one trapped pairwise-repartition component contains the singleton lifts and canonical central-path states associated with all those labels; (ii) G has at least ceil(m/(t-1)) connected components, and choosing one label from each gives a family of at least ceil(m/(t-1)) pairwise incompatible chosen deletion covers. In particular, taking t=ceil(sqrt(m))+1 yields either more than sqrt(m) canonical central-path states in one trapped reconfiguration component or a pairwise-incompatible deletion family of order at least floor(sqrt(m)).

## Body

Let the connected components of the compatibility graph G have orders s_1,...,s_k, with sum m.

Fix t>=2. If some s_j>=t, then certified theorem eb169fd62ac1 applies to that compatibility component: all of its singleton lifts lie in one trapped pairwise-repartition component, and that same trapped component contains the canonical central-path states associated with every label of the compatibility component. This is alternative (i).

Otherwise every component has order at most t-1. Hence
m=s_1+...+s_k <= k(t-1),
so
k>=ceil(m/(t-1)).
Choose one label from each connected component. No two chosen labels are adjacent in G: an edge between two of them would put them in the same connected component. Thus the corresponding chosen deletion covers are pairwise incompatible. This is alternative (ii).

For the displayed square-root consequence, take
t=ceil(sqrt(m))+1.
Then alternative (i) supplies at least ceil(sqrt(m))+1 canonical central-path states in one trapped component. In alternative (ii),
ceil(m/(t-1))=ceil(m/ceil(sqrt(m)))
is at least floor(sqrt(m)).
∎
