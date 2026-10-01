# Matching deletions are exactly the minimum-degree-five deletions of STS(13)

## Statement

Let S be any Steiner triple system on 13 vertices, hence 6-regular. For a set M of deleted blocks, S\M has minimum degree at least 5 if and only if M is a matching. Moreover every such deletion is automatically P_7^(3)-free.

## Body

Every vertex of an STS(13) has degree (13-1)/2=6.

After deleting a block set M, the degree of a vertex v falls by exactly the number of deleted blocks containing v. Therefore the remaining minimum degree is at least 5 if and only if no vertex belongs to two deleted blocks. That condition is exactly that the deleted blocks are pairwise disjoint, i.e. M is a matching.

Finally, a seven-edge linear 3-uniform path uses 2*7+1=15 vertices. Every subhypergraph of S has only 13 vertices, so it contains no P_7^(3), independently of which blocks are deleted.

Thus, within STS(13), the admissible minimum-degree-5 deletion family is structurally exactly the matching-deletion family; no computation is needed for either the minimum-degree condition or P_7-freeness.
