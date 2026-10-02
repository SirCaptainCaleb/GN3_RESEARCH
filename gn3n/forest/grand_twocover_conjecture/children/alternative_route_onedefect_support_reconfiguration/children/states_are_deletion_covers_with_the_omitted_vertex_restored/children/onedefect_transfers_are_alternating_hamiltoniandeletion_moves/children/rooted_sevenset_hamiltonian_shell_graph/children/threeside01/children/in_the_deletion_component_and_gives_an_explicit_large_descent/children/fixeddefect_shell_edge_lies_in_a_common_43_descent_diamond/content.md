# Every fixed-defect shell edge lies in a common 4|3 descent diamond

## Statement

In any rooted seven-vertex shell W of threeside01, let Omega be its shell graph, let T be the complementary inherited tail, fix z in V(W), and suppose deg_Omega(z)>=4. For every edge {z,c} of Omega there exists c'!=c with {z,c'} in E(Omega) such that K=W-{z,c,c'} is Hamiltonian. Consequently the two spanning shell states (W-{z,c})|T|(z,c) and (W-{z,c'})|T|(z,c') have the common one-move descendant K|T|(z,c,c'), and each move lowers Phi by exactly 4.

## Body

Put S=W-{z} and N=N_Omega(z). Then |S|=6, |N|>=4, c belongs to N, and S-{c}=W-{z,c} is Hamiltonian.

We prove that some c' in N-{c} has
K=S-{c,c'}
Hamiltonian.

If |N|=4, put M=S-N, so |M|=2. The five-set S-{c} contains the prescribed pair M and the three vertices N-{c}. By independence_number_at_most_two_in_every_boundary_tournament, some Hamiltonian four-subset of S-{c} contains M. That four-subset omits a vertex c' of N-{c}, so it is exactly S-{c,c'}.

If |N|=5, the set M=S-N is a singleton. Again S-{c} is a five-set. By independence_number_at_most_two_in_every_boundary_tournament it has at least three Hamiltonian four-subsets. Only one four-subset can omit M, so some Hamiltonian four-subset contains M. Its omitted vertex c' lies in N-{c}, and the subset is S-{c,c'}.

If |N|=6, every vertex of S lies in N. The five-set S-{c} has a Hamiltonian four-subset by independence_number_at_most_two_in_every_boundary_tournament; its omitted vertex c' automatically lies in N-{c}. Again K=S-{c,c'} is Hamiltonian.

In every case c' lies in N, hence W-{z,c'}=S-{c'} is Hamiltonian and {z,c'} is an edge of Omega. Thus both
F_c=W-{z,c}
and
F_{c'}=W-{z,c'}
are Hamiltonian five-sets, and K is their four-vertex intersection after deleting the opposite shell label.

The three-set {z,c,c'} is Hamiltonian in every boundary tournament. Therefore the spanning shell cover
C_c=F_c | T | (z,c)
may repartition its first and third components, whose union is W, as
K | (z,c,c').
Likewise
C_{c'}=F_{c'} | T | (z,c')
repartitions to the same cover
D=K | T | (z,c,c').

Both arrows are legal one-step pairwise repartitions. The affected component orders change from 5 and 2 to 4 and 3, so
(5^2+2^2)-(4^2+3^2)=29-25=4.
Hence D is a common strict descendant of the two adjacent fixed-z shell states.

In particular, every prescribed fixed-z shell edge belongs to a strict descent diamond; no choice of a Hamilton-path endpoint on its five-set is needed.