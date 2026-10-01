# Equal-potential ascending terminal graph can contain a rainbow four-edge path

## Statement

The rainbow four-edge path in bdb1eac5484d already lies entirely in the equal-potential ascending terminal graph T_=; its five terminal vertices 9,2,11,10,5 all satisfy φ=5. Hence T_= need not be rainbow-P4-free.

## Body

Use the nine-edge linear 3-graph of bdb1eac5484d. The four ascending nonspecial hyperedges E_0={2,3,9}, E_7={2,7,11}, E_3={1,10,11}, E_1={0,5,10} give the rainbow terminal path 9-2-11-10-5 with distinct entrance colors 3,7,1,0. Each of the five path vertices is a terminal vertex of one of these rank-5 ascending edges, so each has endpoint potential at least 5. Exact induced-path enumeration for this nine-edge system gives global maximum linear-path length 5, hence every vertex has endpoint potential at most 5. Therefore φ(9)=φ(2)=φ(11)=φ(10)=φ(5)=5. Thus this same rainbow P4 is contained in T_=.
