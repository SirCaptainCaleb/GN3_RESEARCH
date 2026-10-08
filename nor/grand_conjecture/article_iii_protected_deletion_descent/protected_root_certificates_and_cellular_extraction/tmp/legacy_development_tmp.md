# Hamiltonian regular cut designs have defect at least n — preserved pre-item development

## Development

Assume the surviving single-cycle zero of the irrational two-moment perturbation. Thus the physical roots form a Hamiltonian cycle v_1,...,v_n, all barrier sides agree, and the protected p-cuts C_i are p-regular with v_i notin C_i and v_{i+1} in C_i.

Define B_i=C_i minus {v_{i+1}}. Then |B_i|=p-1 and B_i avoids both v_i and v_{i+1}. Because the successor matching uses every coordinate once and the C_i incidence design is p-regular, every coordinate belongs to exactly p-1 of the n sets B_i.

The canonical predecessor cut predicted by rho_i is B_i union {v_i}, whereas C_{i-1}=B_{i-1} union {v_i}. Hence the i-th cut defect is exactly
Delta_i=d_J(B_{i-1},B_i),
and the total defect is the Johnson variation
Delta=sum_i d_J(B_{i-1},B_i).

For a coordinate x let b_i(x)=1_{x in B_i}. Since 0<p-1<n, the cyclic binary word b_1(x),...,b_n(x) is nonconstant and therefore has at least two transitions. Also
2 Delta = sum_i |B_{i-1} triangle B_i| = sum_x (# cyclic transitions of b_i(x)).
Consequently Delta >= n.

Equality holds exactly when every coordinate-membership word has exactly two transitions, equivalently the indices i with x in B_i form one cyclic interval of length p-1. In that case the individual element exchanges between consecutive B_i form a balanced directed multigraph with n exchange edges and indegree=outdegree=1 at every coordinate, hence a directed cycle cover of the physical coordinates.

Therefore the irreducible equality case is extremely rigid: either the secondary defect cycle cover has a proper component, yielding a strictly smaller-support zero-sum defect circulation, or it is itself Hamiltonian. Any surviving single-cycle topological obstruction has positive cut defect at least n; the minimum-defect case consists of a Hamiltonian physical root cycle together with a cyclic-interval regular cut design and a secondary directed cycle cover.
