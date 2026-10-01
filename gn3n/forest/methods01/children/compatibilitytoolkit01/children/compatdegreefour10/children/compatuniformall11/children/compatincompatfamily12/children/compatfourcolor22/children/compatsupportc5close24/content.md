# Every support-compatible cycle closes to a clique

## Statement

Let a_1,...,a_k be distinct deletion labels with k>=4 in a boundary tournament H, assume V(H)-{a_1,...,a_k} is nonempty, and let F_i be a two-cover of H-a_i. If, cyclically modulo k, F_i and F_{i+1} are support-compatible on their common domain, then all k covers are pairwise support-compatible. Equivalently, every cycle in the support-compatibility graph of such a deletion-cover family spans a clique.

## Body

# Proof

Put A={a_1,...,a_k} and W=V(H)-A. By hypothesis W is nonempty; fix r in W.

For each i, let ~_i be the same-support equivalence relation induced by F_i on V(H)-{a_i}. Support compatibility of consecutive covers means that ~_i and ~_{i+1} agree on V(H)-{a_i,a_{i+1}}.

First consider vertices x,y in W. They survive in every cover. Agreement therefore propagates around the compatibility cycle, so all k covers induce the same support relation on W.

Now fix one special label a_j. It occurs in every cover except F_j. For i!=j, define epsilon_i(j)=1 if a_j ~_i r and 0 otherwise. Whenever i and i+1 are both different from j, support compatibility of F_i,F_{i+1} gives epsilon_i(j)=epsilon_{i+1}(j).

Deleting vertex j from the cycle C_k leaves a connected path through all other k-1 indices. Hence epsilon_i(j) is independent of i!=j. Thus every cover containing a_j places a_j in the same one of the two common W-support classes.

Take arbitrary p,q. On the common domain V(H)-{a_p,a_q}, every vertex of W has the same support class in F_p and F_q. Every surviving special label a_j, j not in {p,q}, also has the same class relative to r in the two covers by the preceding paragraph. Because each cover has exactly two support classes, equality of the class relative to r for every surviving vertex determines the same support partition. Hence F_p and F_q are support-compatible.

Since p,q were arbitrary, all k covers are pairwise support-compatible.

Therefore every cycle in the support-compatibility graph closes to a clique on the same vertex set.