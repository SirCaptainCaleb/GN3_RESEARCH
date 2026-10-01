# Charged four-edge spacing implies logarithmic charged degree and the 2/3 leading coefficient

## Statement

Assume the charged four-edge spacing conjecture above. For every vertex v with p=φ(v)>=1, the number c_+(v) of ascending nonspecial edges e={x,v,u} with v terminal and φ(u)>=p is at most 3+ceil(log_2 p). Consequently every n-vertex P_ell^(3)-free linear 3-graph satisfies |E(H)| <= ((2ell + ceil(log_2(ell-1)))/3)n for ell>=2, and in particular has leading coefficient 2/3.

## Body

Order the c_+(v)=k charged edge ranks as q_1<=...<=q_k. If k<=3 there is nothing to prove. Put d_i=q_k-q_i. For each i<=k-3, apply charged spacing to e_i,e_{i+1},e_{k-1},e_k. This gives 2q_{i+1}>=q_i+q_k+1, equivalently d_i>=2d_{i+1}+1. Iterating yields d_1>=2^{k-3}-1. Since q_1>=1, d_1<=q_k-1, hence 2^{k-3}<=q_k. Because every incident ascending edge terminal at v has edge rank at most φ(v)=p, q_k<=p, so k<=3+log_2 p and the displayed ceiling bound follows. Now assign every ascending edge to one terminal endpoint having no larger potential than the other, breaking equal-potential ties arbitrarily. Each edge is assigned exactly once and an edge assigned to v is counted by c_+(v). Thus A<=Σ_v c_+(v)<=n(3+ceil(log_2(ell-1))), since φ(v)<=ell-1. Apply 3m-A<=(2ell-3)n from 419519f0efa5 to obtain 3m<=(2ell+ceil(log_2(ell-1)))n.