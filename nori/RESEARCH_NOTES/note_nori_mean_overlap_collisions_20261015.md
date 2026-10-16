# Reciprocal-binomial mean of overlap-root collisions

- Stable ID: note_nori_mean_overlap_collisions_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:global_petrie_switch_moment_and_local_turn_counting
- Labels: proved, distribution, overlap
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9580_1
- Updated session: session_nori_r9580_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

## Mean overlap-root collisions

With the projective root forest H_pi associated to a fixed canonical full geodesic P and a uniform second direction order pi, put C2(H_pi)=sum_v binom(deg_H_pi(v),2).

**Theorem (reciprocal-binomial collision identity).** For every n>=3,
\[
\boxed{E_{\pi} C2(H_\pi)=2\sum_{r=0}^{n-2}\binom{n-1}{r}^{-1}\le10/3.}
\tag{SM4}
\]
The expectation tends to two as n increases.

*Proof.* Choose two reference edges of distinct directions at path positions i<j, with r=j-i-1 directions strictly between them. The two-edge incidence formula gives N(e_i,e_j)=r!(n-1-r)! and N(e_i,bar e_j)=(n-2-r)!(r+1)!. The number of unoriented geodesics using both antipodal orbit classes is therefore 2[N(e_i,e_j)+N(e_i,bar e_j)]=2n r!(n-2-r)!. For a fixed permutation pi, its two projective root edges E_i,E_j can meet in at most one projective root. When they meet, the two antipodal root lifts give two rooted paths of order pi using both orbits. Each unoriented geodesic has two rooted descriptions as order and root vary, so the number of pi where E_i,E_j meet equals the number of unoriented geodesics just counted. Dividing by n! yields probability 2r!(n-2-r)!/(n-1)! for this pair. There are n-1-r pairs of positions with separation r. Summing gives SM4.

For m>=2 let S_m=sum_{r=0}^{m-1}1/binom(m,r). Directly S_2=3/2 and S_3=S_4=5/3. The difference S_(m+1)-S_m equals (1-sum_{r=1}^{m-1}r/binom(m,r))/(m+1), which is nonpositive: the first and last summands total one. Thus S_m<=5/3 for every m>=2. The interior reciprocal-binomial sum is O(1/m), hence S_m approaches one. QED.

**Corollary.** For every k>=2, the probability that H_pi has a projective root incident to at least k of its n edges is at most (10/3)/binom(k,2), by Markov's inequality. Hence the expected number of pairwise overlap collisions remains bounded independently of dimension, even though rare orders permit a star on all n edges. Controlling high-degree overlap stars is a potential next step in sharpening the random-coloring theorem; it does not settle existence for every coloring.
