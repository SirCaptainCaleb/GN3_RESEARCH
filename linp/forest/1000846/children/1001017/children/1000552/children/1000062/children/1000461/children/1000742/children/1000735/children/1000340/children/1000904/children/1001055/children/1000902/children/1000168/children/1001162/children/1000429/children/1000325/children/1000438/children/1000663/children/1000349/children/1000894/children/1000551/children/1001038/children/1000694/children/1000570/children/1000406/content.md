# Minimum-terminal rank-gap families force a disjoint two-tier rank packet

## Statement

Let v be a vertex with phi(v)=p, and let
  e_i={x_i,v,u_i},  i=1,...,k,
be distinct ascending nonspecial edges through v, where x_i is the unique entrance, v is terminal at e_i, phi(u_i)>=p, and phi(e_i)<p. Order the edge ranks
  q_1<=...<=q_k,  q_i=phi(e_i).
Then all 2k vertices x_1,...,x_k,u_1,...,u_k are distinct, and
  q_i >= ceil((2p+i+3)/4).
Consequently
  sum_{i=1}^k phi(x_i) >= (p/2)k + k(k-1)/8,
and
  sum_{i=1}^k [phi(x_i)+phi(u_i)]
    >= (3p/2)k + k(k-1)/8.
In particular the family forces k distinct vertices of vertex rank at least p outside v, together with a disjoint unique-entrance packet of the displayed total vertex rank.

## Body

Because all e_i contain v and H is linear, two distinct e_i,e_j cannot share any other vertex. Hence the pairs {x_i,u_i} are pairwise disjoint, so the 2k displayed vertices are all distinct.

Apply the certified path-relative central-window packing theorem 220a14637b5f to a maximum p-edge path ending at v. Its hypotheses are exactly that the e_i are distinct ascending nonspecial edges terminal at v and have rank at most p. Since every q_i<p, after ordering by edge rank the theorem gives
  q_i >= ceil((2p+i+3)/4).
Each e_i is ascending nonspecial with unique entrance x_i, so
  phi(x_i)=q_i-1
          >= (2p+i-1)/4
          = p/2+(i-1)/4.
Summing over i=1,...,k yields
  sum_i phi(x_i)
    >= (p/2)k + (1/4)sum_{i=1}^k(i-1)
    = (p/2)k + k(k-1)/8.
The assumption phi(u_i)>=p gives
  sum_i phi(u_i)>=pk.
The two packets are vertex-disjoint by linearity, and adding the last two inequalities proves
  sum_i[phi(x_i)+phi(u_i)]
    >= (3p/2)k+k(k-1)/8.
