# Universal red Fourier compression obstructs spectral-gap forcing

- Stable ID: note_5b24eda311cbf6f4b8e9120a
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, nonlinear, fourier, spectrum, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11945_1
- Updated session: session_nori_r11945_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Fourier compression and the spectral-gap obstruction to red antipodal forcing

Let n=2m>=6 and R be the symmetric red adjacency matrix of an arbitrary antipodally odd paired-flat coloring of Q_n. Write b_j(x) in {0,1} for whether direction j is red at vertex x. Legality gives b_j(x+e_j)=b_j(x); antipodal oddness gives b_j(x+1)=1-b_j(x); paired balance gives sum_j b_j(x)=m. Write normalized Walsh modes chi_S(x)=2^(-n/2)(-1)^(sum_(j in S)x_j) and hat(b_j)(H)=2^(-n)sum_x b_j(x)(-1)^(sum_(k in H)x_k).

THEOREM (universal Fourier interaction law). For any S,T subsets of [n],

<chi_S,R chi_T>=(m-|T|)[S=T]-2[S!=T]sum_(j in S intersect T)hat(b_j)(S symmetric_difference T).

Thus every Fourier diagonal entry is m-|S|. An off-diagonal coefficient vanishes when S and T are disjoint or when their symmetric difference has even cardinality. No affine, bounded-feedback, or restricted nonlinear hypothesis is imposed.

PROOF. A red step in direction j multiplies chi_T by -1 if j belongs to T and by +1 otherwise. Hence R chi_T=chi_T(m-2sum_(j in T)b_j). Taking its inner product with chi_S proves the displayed identity once the following three observations are made: the mean of each b_j is 1/2; its Fourier coefficient at any set containing j vanishes by own-direction independence; and every nonconstant coefficient at an even-cardinality set vanishes by antipodal oddness. QED.

THEOREM (fixed singleton compression and near-extremal spectrum). If L denotes the n-dimensional span of the singleton Walsh modes, then the compression of R to L is (m-1)I_n. For every singleton chi_j, the residual norm satisfies ||R chi_j-(m-1)chi_j||_2=1. There are at least n eigenvalues >=m-1 on the subspace perpendicular to the constant eigenvector; by bipartite symmetry there are at least n eigenvalues <=-(m-1).

PROOF. The compression follows from the universal Fourier interaction law. Directly R chi_j=(m-2b_j)chi_j, so the residual is (1-2b_j)chi_j and its squared norm is one. Minmax on L proves the lower spectral band. Multiplication by the all-bit parity character conjugates R to -R and proves the negative spectral band. QED.

SPECTRAL MIXING OBSTRUCTION. Suppose the red graph is connected and write Lambda for the largest absolute nonextremal eigenvalue. The elementary Perron contribution bound for red full antipodal paths is Z(R)=tr(P R^(2m))>=2m^(2m)-(2^(2m)-2)Lambda^(2m). This bound certifies positivity only if Lambda/m<(2/(2^(2m)-2))^(1/(2m)). Since Lambda>=m-1, the required inequality is impossible for every m>=3. In a disconnected graph the simplifying Perron assumption already fails. More refined spectral-signature or four-point return-kernel arguments are not ruled out.

AUDIT. nori_fourier_spectral_audit.py tests independently sampled legal nonlinear Q6 and Q8 gates, checking the Fourier interaction law for all Fourier-mode pairs, singleton residual norms, and the predicted near-extremal eigenvalue bands.

SCOPE. This is an unrestricted paired-flat operator identity and a method obstruction to generic spectral-gap amplification. It does not prove NORI1 or critical-square preservation. It implies that any useful rank-four switch return-kernel inequality must exploit higher-order common-gate constraints rather than a strong red-graph spectral gap.

PERRON-MODE DECOUPLING OF A SQUARE SWITCH. For n=2m even, let phi_const=2^(-n/2)1 and phi_parity=2^(-n/2)(-1)^(sum_j x_j). Both are red adjacency eigenvectors with eigenvalues m and -m, respectively, and P acts by +1 on each. Every face Walsh vector in the four-column switch matrix U is orthogonal to both. Hence the rank-four perturbation E=U C U^T annihilates these two modes, and R and R'=R+E coincide on their two-dimensional span. On its invariant orthogonal complement V,
Z(R)=2m^(2m)+tr(P|_V R_V^(2m)).
The same identity holds for R', so the entire change of the red full-geodesic count comes from V. If the red graph is connected, its eigenvalues +/-m are simple and the four-point return kernel K(z) has no poles at z=+/-1/m. This decoupling further explains why Perron dominance does not settle critical-square positivity: the switch lives entirely in the slow nontrivial modes of the red graph. It does not show that complete cancellation is possible or impossible.
