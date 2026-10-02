# Two persistent three-side defects share a shell neighbor in every rooted seven-set

## Statement

In the three-side fixed-defect transport setup of threeside01, let Z be the common defect set and let Ω_0,...,Ω_3 be the four rooted seven-set shell graphs, each of minimum degree at least four. Fix distinct z,z' in Z. For every j there exists c_j in V(Ω_j)-{z,z'} such that both zc_j and z'c_j are edges of Ω_j. Consequently the two five-sets W_j-{z,c_j} and W_j-{z',c_j} are Hamiltonian and share the four-core W_j-{z,z',c_j}. Writing U_j=W_j-{c_j}, the six-set U_j therefore satisfies the common-four-core dichotomy of yield_a_hamiltonian_sixset_or_fourgooddeletion_transport. Moreover the two complementary supports are the path-cover-two states T_j union {z,c_j} and T_j union {z',c_j}, with displayed covers T_j|(z,c_j) and T_j|(z',c_j). Thus the same two persistent three-side defects are coupled through a common shell neighbor in every shell, producing four valid six-set transport packages without any cyclic rotation of endpoint-barrier triples.

## Body

Let j be fixed and write W=W_j and Ω=Ω_j. By threeside01, Ω has seven vertices and minimum degree at least four. Fix distinct z,z' in Z.

Consider
A=N_Ω(z)-{z'} and B=N_Ω(z')-{z}.
Both A and B are subsets of the five-vertex set W-{z,z'}. Since deg_Ω(z),deg_Ω(z')>=4, removing the possible neighbor z' from N_Ω(z) and the possible neighbor z from N_Ω(z') leaves |A|>=3 and |B|>=3. Hence
|A intersect B|>=|A|+|B|-5>=1.
Choose c in A intersect B. Then zc and z'c are both edges of Ω.

By the definition of the shell graph in threeside01,
F_z=W-{z,c}
and
F_z'=W-{z',c}
are Hamiltonian five-sets. They share the four-vertex set
K=W-{z,z',c},
with F_z=K union {z'} and F_z'=K union {z}. Therefore yield_a_hamiltonian_sixset_or_fourgooddeletion_transport applies to the two Hamiltonian five-sets with common four-core K. Their union is
U=W-{c}.
Thus either U is Hamiltonian and H-U is non-Hamiltonian with path-cover number two, or U is non-Hamiltonian and carries the Hamiltonian-deletion and one-/two-label path-cover-two transport package stated in yield_a_hamiltonian_sixset_or_fourgooddeletion_transport.

Finally, threeside01 proves for every shell edge ab that the complementary support T_j union {a,b} is non-Hamiltonian with path-cover number two, with displayed cover T_j|(a,b). Applying this to zc and z'c gives the two coupled complementary states
T_j union {z,c}
and
T_j union {z',c}.

The argument is uniform for j=0,1,2,3. In particular, it couples any fixed pair of persistent defects from Z inside every shell using only shell-graph degree and the certified common-four-core theorem; no cyclic rotation of a tight triple is used.