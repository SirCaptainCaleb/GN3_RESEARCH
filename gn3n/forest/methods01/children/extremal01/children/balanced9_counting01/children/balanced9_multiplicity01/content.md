# Every nine-vertex boundary tournament has at least twelve balanced four-five partitions

## Statement

Every boundary tournament on nine vertices has at least twelve distinct partitions into a Hamiltonian four-set and a Hamiltonian five-set.

## Body

Let H5 be the family of Hamiltonian five-subsets and H4 the family of Hamiltonian four-subsets. By balanced9_density84_54_01, |H5|>=84 and |H4|>=54. Let C4={V-F:F in H4}, a family of five-subsets with |C4|=|H4|>=54. Since there are C(9,5)=126 five-subsets in total, inclusion-exclusion gives |H5 intersect C4| >=84+54-126=12. Each five-set S in this intersection is Hamiltonian and has Hamiltonian four-set complement V-S, hence determines a balanced 5|4 partition. Distinct five-sets give distinct partitions because the five-side is uniquely determined.
