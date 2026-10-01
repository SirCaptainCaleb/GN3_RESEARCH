# A cycle-free flat terminal-retained state forces a rank-p edge common to both host paths

## Statement

Retain a flat state from 7312b3378d20. Thus e={x,v,u} has edge rank below p, its unique contact on the maximum p-edge path P ending at v is u, and a maximum p-edge path Q ending at u has last edge h, where h is an internal edge of P, h is nonspecial ascending of edge rank p, and Q enters h through the forward joint of P.

Assume additionally that e belongs to a selected common-precursor family: there is a maximum endpoint path R of length L<p that avoids v and contains both x and u.

Then either
  Q union R
contains a linear cycle, or
  h belongs to E(P) intersect E(R).

In the second case, either h is the last edge of R, or h is internal on R. If h is internal and the propagation process of 678901b48360 starting from h produces no linear cycle, the position of h on R is at most
  2L+1-p.

For a family of such flat states using one fixed precursor R, the boundary alternative h=last(R) can occur for at most two target edges.

## Body

The endpoint u of Q lies on R. Since Q and R are maximum endpoint paths ending at distinct vertices u and last(R), they cannot have u as their unique common vertex: by 5854d853a44b, a unique common vertex of two maximum endpoint paths is an internal joint on both paths, whereas u is the last vertex of Q. Hence Q and R have at least two common vertices.

Apply 41100a9882dd to Q and R, with endpoint u of Q lying on R. Either their union contains a linear cycle, or the last edge h of Q is an edge of R. The latter gives
  h in E(P) intersect E(R)
because h already belongs to P in the flat state.

If h is internal on R, then phi(h)=p>L and the cycle-free position bound of 678901b48360 applies, giving position at most 2L+1-p.

If h is the last edge of R, no internal-edge conclusion is asserted. However one fixed last edge h of R is a flat rank-p nonspecial edge and has exactly two terminal vertices. Every target state using h has its distinct last vertex u among those two terminals. Therefore at most two target edges can use this boundary alternative.
