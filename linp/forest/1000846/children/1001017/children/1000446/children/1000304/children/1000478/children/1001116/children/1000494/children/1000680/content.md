# Five-edge deficit doubling implies logarithmic common-last-vertex degree

## Statement

Assume the five-edge deficit-doubling inequality 2q_4>=q_1+q_5+1 for every five ascending nonspecial edges with a common last vertex. If k such edges share a last vertex and p is the largest of their φ-values, then k<=3 floor(log_2 p)+4 for p>=1.

## Body

Order q_1<=...<=q_k=p and set d_i=p-q_i. For every i<=k-4, apply the five-edge inequality to e_i,e_{i+1},e_{i+2},e_{i+3},e_k. It gives 2q_{i+3}>=q_i+p+1, equivalently d_i>=2d_{i+3}+1. Let t=floor((k-2)/3). Iterating from i=1 along indices 1,4,7,... gives d_1>=2^t-1. Since q_1>=1, d_1<=p-1, hence 2^t<=p and t<=floor(log_2 p). Therefore k<=3 floor(log_2 p)+4.
