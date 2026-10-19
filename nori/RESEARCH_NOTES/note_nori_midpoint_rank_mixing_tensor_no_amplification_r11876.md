# Tensor no-amplification for midpoint permutation rank and mixing

- Stable ID: note_nori_midpoint_rank_mixing_tensor_no_amplification_r11876
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, rank, tensor-product, method-obstruction, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11858_2
- Updated session: session_nori_r11858_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Tensor obstruction for midpoint rank and mixing certificates

Let c be any legal paired-flat Q_(2m) coloring and p a pair-parity fiber. Set N=2^m. Let P_pi be the N-by-N permutation matrix of the red half-sweep with pair order pi. Define r(c,p)=dim_R span{P_pi}, d(c,p)=r(c,p)-1, and K(c,p)=(1/m!)sum_pi P_pi.

**Theorem (product identities).** For arbitrary independent paired-flat colorings c,h with initial parity fibers p,q and M=2^k fiber states in h,

r(c box h,(p,q))=r(c,p)r(h,q),
d(c box h,(p,q))+1=(d(c,p)+1)(d(h,q)+1),
K(c box h,(p,q))=K(c,p) tensor K(h,q).

**Proof.** Pair matching operations in disjoint blocks commute. Restricting a combined pair order to each block yields endpoint matrix P_pi(c,p) tensor P_sigma(h,q), and every pair of restricted orders occurs among combined orders. Their linear spans therefore form the tensor product of the factor spans. All permutation matrices have the same positive sum of entries, hence the difference-span dimension equals the linear span dimension minus one. Each prescribed pair of factor orders admits binomial(m+k,m) interleavings, which proves the uniform-average identity.

**Theorem (no rank amplification).** Let T(N)=(N-1)(N-2)/2. If d(c,p)<=T(N), then for every independent h and any q,

d(c box h,(p,q))<=T(NM).

Thus the previously established sufficient rank-forcing certificate cannot be created by tensoring a factor that fails it with independent spectator directions.

**Proof.** Doubly stochastic N-by-N matrices form an affine space of dimension (N-1)^2, so r(h,q)<=(M-1)^2+1. The hypothesis gives r(c,p)<=T(N)+1. The tensor formula and the integer identity

T(NM)+1-(T(N)+1)((M-1)^2+1)
=(M-1)(2N^2+3NM-6N-4M+4)/2 >0

for N,M>=4 complete the proof.

**Corollary (no Frobenius mixing amplification).** Let mu(c,p)=||K(c,p)||_F^2. Then mu(c box h,(p,q))=mu(c,p)mu(h,q), and mu(h,q)>=1 by doubly stochasticity. Therefore if mu(c,p)>=2, no independent factor makes the criterion mu<2 hold. For every fixed c, r(c^box s)=r(c)^s while r(c)<N^2; its difference-span ratio against T(N^s) tends to zero as s grows.

The paired-flat Q4 gates f_(2j)=t_(2j+1)+a_j, f_(2j+1)=t_(2j)+b_j yield ranks 2,4,8 for products on Q4,Q8,Q12, although the pair-order counts are 2,24,720. The checker nori_permutation_span_tensor_audit.py independently reproduces these ranks. The result concerns all legal paired-flat colorings; no affine assumption enters the theorems. The explicit gates serve only as an illustration. This closes tensor padding as a means of forcing the rank or mixing hypothesis, without ruling out a forcing mechanism involving coupled nonlinear direction interactions.
