# All-split support switching forces order disagreement or adjacent-gap concentration on both cores

## Statement

Assume the all-three-split branch of compatsupportham22. For each x in {a,b,c}, choose the Hamilton path on R union {x} supplied by the corresponding deletion cover, and likewise on S union {x}. Then for each core K in {R,S}, either two of the three chosen Hamilton paths induce different relative orders on K, or all three induce one common linear order L_K and the insertion positions of a,b,c into L_K have diameter at most one. Equivalently, in the no-order-disagreement branch all three special labels occur in at most two adjacent gaps of one common order on R, and independently in at most two adjacent gaps of one common order on S.

## Body

# Proof

We prove the assertion for R; the proof for S is identical.

By compatsupportham22, R union {a}, R union {b}, and R union {c} are Hamiltonian. Choose Hamilton paths P_a,P_b,P_c on these three sets from the three original deletion covers.

If two paths induce different relative orders on their common R-vertices, the first alternative holds.

Assume therefore that P_a,P_b,P_c induce one common linear order

L=(r_1,...,r_k)

on R. Since P_x contains exactly the vertices of R together with x, and the R-vertices occur in the order L, the sequence P_x is obtained from L by inserting x into one of its k+1 gaps. Let i_x denote that insertion position.

Suppose two labels, say a,b, satisfy |i_a-i_b|>=2. We claim R union {a,b} is Hamiltonian.

Insert both a and b into L at their respective positions, preserving the common R-order. Because the two insertion positions are separated by at least one untouched R-gap, every consecutive triple of the resulting sequence occurs as a consecutive triple either in P_a or in P_b. Around the a-position the local triples are exactly those of P_a; around the b-position they are exactly those of P_b; away from both positions the consecutive triples consist only of R-vertices and occur unchanged in both P_a and P_b. Hence every consecutive triple is tight, so the combined sequence is a Hamilton tight path on R union {a,b}.

In the all-split support pattern, the remaining label c Hamiltonizes S. Therefore the two disjoint Hamiltonian sets

R union {a,b}   and   S union {c}

partition V(H), producing a spanning two-cover of H. This contradicts that H is a counterexample.

Thus no two of i_a,i_b,i_c differ by two or more, so

max{i_a,i_b,i_c}-min{i_a,i_b,i_c} <= 1.

Hence all three insertion positions lie in at most two adjacent gaps of L.

Applying the same argument to S proves the result on both cores.
