# Canonical source rails of arbitrary common-terminal ascending edges are pairwise intersecting

## Statement

Let e_i={x_i,v,u_i} and e_j={x_j,v,u_j} be distinct ascending nonspecial edges terminal at the same vertex v, with ranks r_i<=r_j. Let R_i,R_j be canonical maximum source rails ending at x_i,x_j, of lengths r_i-1,r_j-1, each avoiding the two terminals of its own edge. Then V(R_i)∩V(R_j) is nonempty. Thus the source rails of any finite family of ascending nonspecial edges sharing a terminal form a pairwise-intersecting family, with no restriction on the rank gaps.

## Body

By downward-completeness 1c8aac8aa4dd, the higher rail R_j meets e_i. If x_i lies on R_j, then x_i is also the endpoint of R_i, so the rails intersect. Otherwise the R_j-contact with e_i uses the opposite terminal u_i. Suppose for contradiction that R_i and R_j are vertex-disjoint. Then x_i is absent from R_j, so e_i meets R_j only at u_i because v is absent from every canonical source rail. Let a,b be the first and last edge indices of R_j containing u_i; thus b is a or a+1. First-contact localization 813f5b668319 applied to the rank-r_i nonspecial edge e_i and the path R_j gives a<=r_i-2 because u_i is a terminal label. Hence b<=r_i-1. Start the suffix of R_j at its last edge containing u_i. Its length is at least
(r_j-1)-b+1 = r_j-b >= r_j-r_i+1.
Now concatenate R_i, then e_i, then this suffix of R_j. Under the disjoint-rail assumption this is linear: R_i ends at x_i, e_i joins x_i to u_i, and the chosen suffix begins at the last occurrence of u_i; e_i has no other R_j-contact and v is absent from both rails. Its length is at least
(r_i-1)+1+(r_j-r_i+1)=r_j+1.
It ends at x_j, contradicting phi(x_j)=r_j-1. Therefore R_i and R_j intersect.
