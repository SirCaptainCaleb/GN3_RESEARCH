# Four-edge spacing implies logarithmic common-last-vertex degree

## Statement

Assume the four-edge spacing inequality 2q_2>=q_1+q_4+1 holds whenever four ascending nonspecial edges share a last vertex. Then if k ascending edges share a last vertex v and p is the largest of their φ-values, k<=3+ceil(log_2(p+1)).

## Body

Order q_1<=...<=q_k=p and put d_i=p-q_i. For each i<=k-3, apply the four-edge spacing inequality to e_i,e_{i+1},e_{k-1},e_k. Since q_k=p, 2q_{i+1}>=q_i+p+1, equivalently d_i>=2d_{i+1}+1. Iteration gives d_1>=2^{k-3}-1. Since d_1<=p-1, 2^{k-3}<=p, hence the claimed logarithmic bound.