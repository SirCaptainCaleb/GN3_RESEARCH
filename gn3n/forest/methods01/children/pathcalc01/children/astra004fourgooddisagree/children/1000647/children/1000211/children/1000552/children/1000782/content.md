# A proper tight cycle forces a tight triple reversing a cycle or complement-path edge

## Statement

Let H be a minimum counterexample. Suppose C is a proper vertex-simple tight cycle that is the union of two internally vertex-disjoint tight paths P,Q sharing exactly two vertices u,v, with P running from u to v and Q from v to u. Then H-V(C) is non-Hamiltonian with path-cover number two, and H contains a tight triple reversing either a displayed cyclic edge of C or a displayed edge of a complementary two-cover path.

## Body

Opening the tight cycle C at any cyclic cut gives a Hamilton tight path on V(C). Since H is not Hamiltonian, C is proper. By minimum-counterexample calculus, H-V(C) has path-cover number at most two; it cannot be Hamiltonian, since a Hamilton path on H-V(C) together with an opened Hamilton path on C would two-cover H. Hence H-V(C) is non-Hamiltonian with path-cover number two. A non-Hamiltonian boundary tournament has at least four vertices, because every boundary tournament of order at most three is Hamiltonian. Therefore some component A=(a_0,...,a_m) of a displayed two-cover A|B of H-V(C) has order at least two, so m>=1. Apply f2bf5c6337c4 to A and C. For any cyclic cut indexed by i, its terminal-end conclusion gives at least one of (c_i,a_m,a_{m-1}) and (c_{i+1},c_i,a_m) tight. In the first case, the triple reverses the displayed ordered edge (a_{m-1},a_m) of A, because its final two entries are (a_m,a_{m-1}). In the second case, the triple reverses the displayed cyclic edge (c_i,c_{i+1}), because its first two entries are (c_{i+1},c_i). Thus a reversing tight triple exists. No cyclic rotation of an ordered triple is used.
