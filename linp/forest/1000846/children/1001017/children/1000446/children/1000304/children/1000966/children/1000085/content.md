# Increasing ordered-shadow paths have nondecreasing parent ranks and lift unless they close a linear cycle

## Statement

Let Z be the ordered shadow from d7bc6f5ad804. Let z_0z_1,...,z_{t-1}z_t be a simple rainbow path in Z with strictly increasing order labels lambda_1<...<lambda_t, and let E_i be the distinct parent hyperedge of z_{i-1}z_i, with q_i=phi(E_i). Then q_1<=...<=q_t. Moreover either E_1,...,E_t is a linear hypergraph path, or there exist i<j-1 such that E_i,...,E_j is a linear cycle.

## Body

For each i, the auxiliary edge z_{i-1}z_i belongs to an ascending parent E_i of rank q_i and therefore has label lambda_i in {q_i-1,q_i}. Hence q_i<=lambda_i+1. Strict integrality gives lambda_{i+1}>=lambda_i+1, while lambda_{i+1}<=q_{i+1}. Thus q_i<=lambda_i+1<=lambda_{i+1}<=q_{i+1}, proving nondecreasing parent ranks. Because the Z-path is rainbow, the parents E_i are distinct. Consecutive parents E_i,E_{i+1} both contain z_i; by linearity of H they intersect in exactly z_i. Since the Z-path is simple, these prescribed consecutive joints are distinct. If no nonconsecutive pair of parents intersects, the parent sequence is a linear hypergraph path. Otherwise choose a nonconsecutive intersecting pair E_i,E_j with j-i minimal. By minimality, among E_i,...,E_j there are no nonconsecutive intersections except E_i∩E_j, while every consecutive pair intersects in its prescribed Z-joint. Therefore E_i,...,E_j is a linear cycle.
