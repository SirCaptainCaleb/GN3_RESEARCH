# All but two consecutive pairs in a large one-gap corridor force Hamiltonian windows unless disturbance already occurs

## Statement

Let H be a minimum counterexample, let A be a globally longest tight path of order lambda, and let C be an A-order-preserving tight path of order lambda-1 agreeing with A outside one gap. Write the C-only vertices in that gap in displayed order as E=(x_1,...,x_r), r>=2. Then either there is explicit order disagreement or a reversed tight splice-junction triple, or all but at most two indices i in {1,...,r-1} have the following property: H contains a Hamiltonian four- or five-vertex set W_i supplied by the paired-noninsertion theorem for {x_i,x_{i+1}}. The exceptional indices, if two exist, are consecutive. Every such W_i is proper and H-W_i is non-Hamiltonian with path-cover number two.

## Body

Fix an index i. The vertices x_i,x_{i+1} lie outside the globally longest path A, hence the certified longest-path paired-noninsertion menu 6839f08d0cf8 applies. If it gives a Hamiltonian four- or five-set, record i as a window index. Otherwise its remaining possibilities are a direct interval connector or a tight cross triple through A.

For consecutive corridor vertices, a connector whose A-interval contains at least two vertices is consumed by 435125d4ab86: it gives order disagreement or a reversed splice-junction triple. If the connector contains only one A-vertex z, it is itself a tight cross triple and is handled by d63d3042d1ad. Likewise any cross-triple alternative from the paired-noninsertion menu is consumed by d63d3042d1ad: it gives one of those disturbances, or a successful insertion of some z_i in V(A)-V(C) between x_i and x_{i+1}. In the successful case the resulting path has order lambda and every new junction triple is tight.

Assume henceforth that no stated disturbance occurs. Then every non-window index i carries such a successful insertion label z_i. Two distinct non-window indices cannot use the same label. Indeed, inserting one fixed z at two distinct edges of the displayed path C gives two tight paths on the same support V(C) union {z}; the position of z relative to a C-vertex lying between the two insertion positions differs, so the two paths have order disagreement. For adjacent insertion positions the shared corridor vertex itself changes side of z.

Now suppose i<j are two non-window indices with j>=i+2. Their insertion labels z_i,z_j are distinct. Perform both insertions simultaneously in the displayed sequence C. Because the two replaced edges x_i x_{i+1} and x_j x_{j+1} are nonadjacent, every consecutive triple of the doubly modified sequence is one already certified by one of the two successful single insertions or inherited from C. Hence the doubly modified sequence is tight. It has order |C|+2=lambda+1, contradicting the global maximality of A.

Therefore any two non-window indices differ by at most one. A subset of {1,...,r-1} with this property has size at most two, and if it has two elements they are consecutive. Thus all but at most two indices are window indices. Finally each Hamiltonian four- or five-set W_i is proper because a minimum counterexample has more than ten vertices. If H-W_i were Hamiltonian, W_i together with H-W_i would two-cover H. Hence H-W_i is non-Hamiltonian; minimality gives path-cover number two.
