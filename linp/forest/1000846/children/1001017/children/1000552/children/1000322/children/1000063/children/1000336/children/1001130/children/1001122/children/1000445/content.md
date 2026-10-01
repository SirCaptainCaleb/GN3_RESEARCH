# Private-vertex ear surplus on a short linear cycle

## Statement

Let C be a linear cycle of c edges in a linear 3-graph H with minimum degree at least q. Let p be the private vertex of one cycle edge. Among edges f distinct from that cycle edge and containing p, let C_0,C_1,C_2 count those for which f minus {p} contains respectively 0,1,2 vertices of V(C). Then 2C_0+C_1 >= 2q-2c+1. In particular, if c<=q-1 then 2C_0+C_1>=3, and if c<=q-s then 2C_0+C_1>=2s+1.

## Body

The two cycle-joint vertices of the cycle edge containing p cannot occur in any other edge through p by linearity. Distinct edges through p have disjoint non-p vertex pairs. Therefore the cycle contacts made by the noncycle star at p are all distinct and lie among at most |V(C)|-3=2c-3 available cycle vertices, so C_1+2C_2<=2c-3. On the other hand C_0+C_1+C_2=d_H(p)-1>=q-1. Twice the latter inequality minus the former gives 2C_0+C_1>=2q-2-(2c-3)=2q-2c+1.
