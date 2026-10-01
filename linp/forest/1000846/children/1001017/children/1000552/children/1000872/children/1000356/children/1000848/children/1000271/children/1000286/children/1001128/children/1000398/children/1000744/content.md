# Source-hit imbalance exactly measures excess distinguished rail overlap

## Statement

For four source-clean 0-1-1 edges e_j={x_j,v,u_j} and their four maximum source rails Q_i, let s_j be the number of foreign rails Q_i, i!=j, that meet e_j at the source x_j. Let a_ik be the number of distinguished vertices among {x_j,u_j:1<=j<=4} shared by Q_i and Q_k. Then sum_{i<k} a_ik = 8 + sum_{j=1}^4 (s_j-1)^2. In particular the distinguished overlap mass is exactly 8 iff every source x_j lies on exactly one foreign rail.

## Body

Fix j. The own rail Q_j contains x_j and not u_j. Among the other three rails, exactly s_j contain x_j and the remaining 3-s_j contain u_j, because each foreign rail meets e_j in exactly one of its two non-v vertices. Hence, among the four rails, the number of rail pairs agreeing in the j-th distinguished pair is C(1+s_j,2)+C(3-s_j,2). A direct simplification gives C(1+s,2)+C(3-s,2)=2+(s-1)^2 for s=0,1,2,3. Summing over j counts every shared distinguished vertex once and yields sum_{i<k} a_ik = sum_j [2+(s_j-1)^2] = 8 + sum_j (s_j-1)^2. Thus overlap beyond the universal mass eight is precisely the quadratic imbalance of foreign source hits.
