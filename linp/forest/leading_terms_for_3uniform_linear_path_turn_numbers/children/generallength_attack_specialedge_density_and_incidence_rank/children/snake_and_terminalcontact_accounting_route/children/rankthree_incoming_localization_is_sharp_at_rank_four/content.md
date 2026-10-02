# Rank-three incoming localization is sharp at rank four

## Statement


At any vertex z of a linear 3-graph, at most two nonspecial incoming snake edges of rank at most 3 can coexist. This threshold is sharp without additional hypotheses: there is a linear triple system with three distinct nonspecial incoming snake edges of rank exactly 4 at one vertex.


## Body


Suppose three distinct nonspecial incoming snake edges e,e_1,e_2 enter z and all have rank at most 3. Choose e of maximum rank q. Rank 1 is immediately special. If q=2, the two-edge path e_1,e enters e through z while (e,z) is already a snake incidence, giving two longest entrance labels and making e special. Thus q=3.

Take a longest realization P=(g,f,e) with last vertex z. Put S=(e_1 union e_2) minus {z}. If g meets S, say g meets e_i, then g,e_i,e is a three-edge path entering e through z, again making e special. Otherwise g is disjoint from S. Since each e_i has rank at most 3, it cannot be appended to P to form a four-edge path, so e_i minus {z} must meet V(P). By linearity it cannot meet e, and by assumption it cannot meet g; hence it must meet the unique private vertex of f relative to g,e. Both e_1 and e_2 would then contain z and that same vertex, contradicting linearity.

Sharpness at rank four is witnessed by the certified seven-edge system
  (0,1,2),(0,8,9),(0,4,6),(3,5,8),(2,6,7),(3,7,9),(2,4,10).
At the common vertex 0, the first three edges are all nonspecial snake-incoming edges of rank 4, with unique entrance labels 2,9,6. Thus the rank-three conclusion cannot be extended to rank four from bounded rank alone. In this witness only (0,8,9) is ascending, so it does not settle stronger minimum-degree or ascending-only variants.
