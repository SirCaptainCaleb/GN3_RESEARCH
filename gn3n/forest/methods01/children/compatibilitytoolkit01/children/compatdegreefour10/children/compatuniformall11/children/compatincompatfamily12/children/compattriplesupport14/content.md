# A support-incompatible triple either disagrees on the common core or switches every deleted label between the two core classes

## Statement

Let a,b,c be deletion labels whose chosen covers F_a,F_b,F_c are pairwise support-incompatible. Put W=V(H)-{a,b,c}. Either two of the three induced support partitions on W differ, or all three induce one common two-class partition W=R disjoint-union S and, for each label x in {a,b,c}, the two covers among F_a,F_b,F_c that contain x place x in opposite classes relative to R|S.

## Body

# Proof

Restrict each deletion cover F_a,F_b,F_c to the common vertex set W=V(H)-{a,b,c}, retaining only the induced same-path equivalence relation.

If two restrictions induce different support partitions on W, the first alternative holds.

Assume therefore that all three induce the same partition R|S of W. Consider F_a and F_b. Their common domain is W union {c}. They are support-incompatible by hypothesis, while their support relations agree on every pair contained in W. Hence their support disagreement must involve c.

Since there are only two support classes extending the common partition R|S, this means c lies with R in one of F_a,F_b and with S in the other.

Apply the same argument to F_a,F_c. Their common extra label beyond W is b, so b belongs to opposite core classes in those two covers. Likewise, comparing F_b,F_c shows that a belongs to opposite core classes in those two covers.

Thus, when no support disagreement survives on the common core, all three pairwise support incompatibilities are concentrated in the deleted labels themselves: each label switches from one fixed core class to the other between its two surviving deletion covers.

No path-order information is used.
