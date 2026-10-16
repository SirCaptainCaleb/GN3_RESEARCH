# Walsh residual moments and forced spectral clusters in balanced odd cube colorings

- Stable ID: note_nori_forced_neartop_walsh_spectrum_20261015
- Author: unspecified; session provenance retained
- Primary home: article:article_xv_projective_face_flag_unification
- Labels: spectral, balanced, closure_obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_4
- Updated session: session_nori_r9962_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let n=2m>=2 and let c be an antipodally odd vertex-balanced binary edge coloring of Q_n. Put r_i(x)=1-c_i(x), s_i(x)=2c_i(x)-1, so every s_i is in {-1,1}, s_i(bar x)=-s_i(x), and sum_i s_i(x)=0. Let R be the color-zero adjacency operator on functions with normalized inner product 2^(-n)sum_x u(x)v(x). For S subset [n], put chi_S(x)=(-1)^(sum_{i in S}x_i).

**Walsh residual identity.** For every S, with k=|S|,
(R-(m-k)I)chi_S = chi_S sum_{i in S}s_i.
Indeed, each color-zero direction contributes r_i(x)(-1)^[i in S]chi_S(x) to Rchi_S(x). In particular, for every singleton S={i},
|| (R-(m-1)I)chi_i ||^2 = 1,
and the residual chi_i s_i is antipodally even and orthogonal to the entire first Walsh level. Hence the compression of R to that n-dimensional level is (m-1)I. Vertex balance also gives R1=m1.

**Theorem (universal Walsh-level residual second moments).** For 1<=k<=n-1,
sum_{|S|=k} ||(R-(m-k)I)chi_S||^2
= binom(n,k) k(n-k)/(n-1).                                                     (1)
This identity uses only vertex balance, while antipodal oddness gives the stated parity-sector compression.

*Proof.* Fix x. From sum_i s_i(x)=0 and sum_i s_i(x)^2=n, we get sum_{i ne j}s_i(x)s_j(x)=-n. Averaging (sum_{i in S}s_i(x))^2 over uniformly selected k-subsets S yields
k+[k(k-1)/(n(n-1))](-n)=k(n-k)/(n-1).
Average over x and use the Walsh residual identity. QED.

**Corollary (forced spectral clustering).** Write v_k=k(n-k)/(n-1), N_k=binom(n,k). For every t>sqrt(v_k), R has at least ceil(N_k(1-v_k/t^2)) eigenvalues in [m-k-t,m-k+t], counted with multiplicity. They may be counted on 1-perp for k>=1. In particular, at least ceil(n/2) nonconstant eigenvalues lie in [m-1-sqrt(2),m-1+sqrt(2)]. By bipartiteness the same multiplicity lies in the reflected interval. Also Courant-Fischer on the first Walsh level gives at least n eigenvalues of R|1-perp at least m-1.

*Proof.* Let E be the spectral projector onto the stated interval, and W_k the Walsh-level k subspace. For each chi_S at level k, the spectral mass outside the interval is at most ||(R-(m-k)I)chi_S||^2/t^2. Summing, tr(E P_{W_k}) >= N_k(1-v_k/t^2). Since 0<=tr(E P_{W_k})<=rank(E), the bound follows. For k>=1, W_k is orthogonal to constants, so the same estimate holds after removing the constant eigenvector. At k=1 choose t=sqrt(2); the non-strict boundary version follows from the identical estimate. Conjugation by Hamming-parity sign sends R to -R. The final lower-tail inequality uses the first-level compression and minmax. QED.

These formulas apply to every vertex-balanced antipodally odd coloring, including all counterexample-preserving balanced reductions. They prohibit proof by ordinary n-step spectral-gap mixing alone. They leave the endpoint-specific geodesic trace positivity unresolved.
