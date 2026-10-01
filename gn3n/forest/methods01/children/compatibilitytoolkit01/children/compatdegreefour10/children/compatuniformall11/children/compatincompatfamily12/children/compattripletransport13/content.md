# A support-compatible order-incompatible triple either disagrees on the common core or moves every deleted label between two gaps

## Statement

Let a,b,c be deletion labels whose chosen covers F_a,F_b,F_c are pairwise support-compatible but pairwise order-incompatible. Then there is a partition V(H)=X disjoint-union Q with {a,b,c} subseteq X, a fixed Hamilton path on Q, and Hamilton paths P_a,P_b,P_c on X-{a},X-{b},X-{c}, respectively. Put R=X-{a,b,c}. Either two of the restrictions P_a|R,P_b|R,P_c|R have different relative orders, or all three induce one common order on R and, for each label x in {a,b,c}, the two paths among P_a,P_b,P_c that contain x place x in two distinct insertion gaps of that common R-order.

## Body

# Proof

Pairwise support compatibility of F_a,F_b,F_c gives the standard support localization: there are exactly two support classes X,Q, all three deletion labels lie in X, every F_d has support partition (X-{d})|Q, and the Q-path may be chosen with one fixed Hamilton order. Let P_a,P_b,P_c denote the corresponding Hamilton paths on X-{a},X-{b},X-{c}. Put R=X-{a,b,c}.

If the restrictions of the three P-paths to R do not all have the same relative order, the first alternative holds.

Assume therefore that all three restrictions induce one common linear order on R.

Consider the pair P_a,P_b. Their common vertex set is R union {c}. Since F_a,F_b are support-compatible, their incompatibility is purely order-theoretic on this common X-support. The vertices of R already occur in the same relative order in both paths. Hence the only possible source of order incompatibility is the position of c relative to R. Therefore c must occupy two different insertion gaps of the common R-order in P_a and P_b.

Apply the same argument cyclically. For P_a,P_c, the only extra common label beyond R is b, so b occupies different insertion gaps in those two paths. For P_b,P_c, the only extra common label beyond R is a, so a occupies different insertion gaps there.

Thus in the common-core-order branch every deletion label is transported between two distinct gaps of one fixed R-order across the two deletion paths that contain it.

This is a three-state transport normal form: either disagreement survives on the common core after all three deletion labels are removed, or all disagreement is concentrated into three labels each changing insertion gap.
