# The all-equal support triangle forces three synchronized reverse boundary triples

## Statement

Assume the all-equal {1,1,1} cube normalization A_i=(t_i,M_i), with antipodal paths (M_i,t_{i+1}), and write b_i for the first vertex of M_i and a_i for its last vertex. Then for every i modulo three the triple (b_i,t_i,a_{i-1}) is tight. Equivalently, the forward join (a_{i-1},t_i,b_i) is non-tight at all three transferred labels.

## Body

Fix i. The support S_{i-1} has Hamilton path (t_{i-1},M_{i-1},t_i), while M_i is a tight path. If (a_{i-1},t_i,b_i) were tight, concatenating these displayed orders would give a Hamilton path on S_{i-1} union V(M_i), because every other consecutive triple is inherited from S_{i-1} or M_i. But 4c049924257e proves that this enlargement is non-Hamiltonian. Hence (a_{i-1},t_i,b_i) is non-tight. Boundary antisymmetry therefore makes its reversal (b_i,t_i,a_{i-1}) tight. Applying this cyclically gives the three simultaneous reverse triples.