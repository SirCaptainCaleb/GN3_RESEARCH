# Auxiliary inversion graphs and Fourier criteria for affine NORI1

- Stable ID: note_nori_affine_profile_fourier_inversion_graphs_20261017_r11401
- Author: session_nori_r11401_1
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, affine, Fourier, inversion-graph, acyclic-orientations, Hall, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11401_1
- Updated session: session_nori_r11401_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Quotient Fourier coefficients of affine geodesic profiles are signed graph-ordering sums

Let A in F2^(n x n) have zero diagonal and A*1=1. For each direction order pi let
b_i(pi)=sum_(j preceding i in pi) A_ij,
and let B(A)={b(pi):pi in S_n}. The legal affine coloring c_i(x)=a_i+(Ax)_i has full profiles a+Ax+b(pi). Write K=ker(A^T), with dimension q, and let pi be a uniformly random permutation.

**Theorem 1 (graphical Walsh representation).** For lambda in K define a simple undirected graph H_lambda on the direction set E=[n] whose ij edge, i<j, is present precisely when
h_ij=lambda_i A_ij+lambda_j A_ji=1.
Let alpha_lambda=sum_(i<j)lambda_j A_ji, and define inv_H(pi) as the number of edges ij of H with i<j but j preceding i in pi. Then
lambda dot b(pi)=alpha_lambda+inv_(H_lambda)(pi) (mod 2).
Moreover
deg_(H_lambda)(i) mod 2=lambda_i, and |E(H_lambda)| mod 2=0.
Thus H_lambda is nonempty whenever lambda is nonzero.

*Proof.* For i<j, the contribution of the unordered pair {i,j} to lambda dot b equals lambda_j A_ji when i precedes j and equals lambda_i A_ij when j precedes i. Switching its order changes this contribution by h_ij. Summing gives the inversion formula. At vertex i the sum of h_ij over neighbors j is
lambda_i sum_(j != i)A_ij+sum_(j != i)lambda_j A_ji
=lambda_i+(A^T lambda)_i=lambda_i.
The edge parity is sum_(i<j)h_ij=sum_i lambda_i sum_(j != i)A_ij=lambda dot 1, which vanishes because 1=A1 and A^T lambda=0. A nonzero lambda yields an odd-degree vertex, so H_lambda is nonempty.

**Theorem 2 (component factorization and zero coefficients).** Define the quotient Walsh coefficient
mu_hat(lambda)=E_pi[(-1)^(lambda dot b(pi))].
If H_lambda has connected components C_1,...,C_t, then
mu_hat(lambda)=(-1)^alpha_lambda product_(j=1)^t Z(H_lambda[C_j]),
where Z(H)=E_sigma[(-1)^inv_H(sigma)] for a uniformly random order of the vertices of H. If any component has an odd number of edges, mu_hat(lambda)=0.

*Proof.* For a uniformly random ordering of E, the induced relative permutations on disjoint vertex subsets are independent and uniform. The inversion sign for H is the product of inversion signs for its components, proving factorization. Reversing the induced order on a component toggles each edge inversion, so Z(C)=(-1)^|E(C)|Z(C). It vanishes when the edge count is odd. Isolated vertices contribute one.

**Theorem 3 (explicit analytic coverage criterion).** For each coset t+im A, let P_A(t) be the probability that b(pi) belongs to it. Walsh inversion on the q-dimensional quotient gives
P_A(t)=2^(-q) sum_(lambda in K)(-1)^(lambda dot t) mu_hat(lambda).
If sum_(0 != lambda in K)|mu_hat(lambda)|<1, every quotient coset has positive probability. Consequently all complete profiles are attained globally for every constant vector a, and the root-profile incidence graph admits a perfect matching by the established affine matching-transversal theorem. It suffices, in particular, that for every nonzero lambda in K some component of H_lambda has an odd edge count: then all nontrivial coefficients vanish and the quotient profiles are uniformly distributed.

*Proof.* The characters of F2^n/im A are precisely lambda in ker A^T, giving the Fourier inversion formula. The stated strict inequality bounds P_A(t) below by 2^(-q)(1-sum_(lambda !=0)|mu_hat(lambda)|)>0. Full quotient coverage implies full affine profile realization, and affine quotient selectors give a bijective root-profile matching.

**Small certificates.** For A with row bit masks (2,1,1) in n=3, lambda=110 in binary lies in K, H_lambda is the two-edge path 1-0-2, and mu_hat(lambda)=1/3 (up to the reference-order sign). Indeed the two leaf-order indicators, conditional on the center's independent uniform priority U, have expectation (2U-1)^2; integrating gives 1/3. For A with row masks (2,13,8,7) in n=4, K={0,1111}, and H_1111 consists of the two isolated edges {0,3},{1,2}. Both components have odd edge count; hence mu_hat(1111)=0 and the two affine quotient classes receive the same number of permutation witnesses.

**Open auxiliary inequality (not used in the proofs).** Exhaustive Walsh-transform enumeration of all undirected graphs on up to six vertices found |Z(H)|<=1/3 for every graph with at least one edge, with equality for a two-edge path. No dimension-uniform proof is claimed. If such a bound holds, it yields a sharp uniform bound on the bias of nontrivial affine quotient characters and quantitative Fourier criteria for arbitrary corank. The current theorems require neither this inequality nor symmetric-exchange conjectures.

The construction applies to every legal affine matrix A, with no rank, balance, or interaction-graph sparsity restriction. The underlying symmetric-exchange question and unrestricted NORI1 remain open.
