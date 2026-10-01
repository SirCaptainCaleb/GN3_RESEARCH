# At least one Class-III terminal matching has two high-low pairs

## Statement

In the nine-vertex residual obstruction 213f75e9692a, the two terminal matchings F_y and F_z cannot both pair their two available degree-three vertices together. Consequently at least one of F_y,F_z contains two high-low pairs.

## Body

Write the three degree-three vertices of R as A=x*, B=y*, C=z*, and call the remaining six vertices low.

The matching F_y omits B, so its two available high vertices are A,C. If it pairs them together, then {A,C} is the off-y pair of a hyperedge through y, hence no edge of R contains both A and C.

Similarly, if F_z pairs its two available highs together, then {A,B} is covered by a z-edge and no edge of R contains both A and B.

Assume both events occur. Then A is nonadjacent in R to both B and C.

Since d_R(A)=3 and R is linear, the three edges through A have pairwise disjoint off-A pairs, giving six distinct neighbors of A. The only six available neighbors are precisely the six low vertices. Hence the three A-edges partition the six lows into three pairs; every low lies in exactly one A-edge.

Delete these three A-edges from R. Four edges remain. In the residual four-edge system, B and C retain degree three each, because no A-edge contains B or C. Thus the four remaining triples contain a total of six incidences with {B,C}.

But linearity allows at most one triple to contain both B and C. Therefore across four triples the total number of B/C incidences is at most 2+1+1+1=5, contradicting the required total six.

Hence F_y and F_z cannot both be high-high. Since each terminal matching either pairs its two available highs together or pairs each of them with a low, at least one terminal matching contains two high-low pairs.