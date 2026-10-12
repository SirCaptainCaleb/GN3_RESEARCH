# Sparse low-switch endpoint sets and exact paired alignment in signed rank-parity colorings

- Stable ID: note_article_x_signed_rank_parity_endpoint_sparsity_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_x_switch_induction
- Labels: obstruction, endpoint_geometry, exact_formula, partial_positive
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6298_2
- Updated session: session_nori_r6298_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_x_switch_induction, exact version 2

## Research note

# Endpoint sparsity and paired alignment for signed rank-parity edge colorings

Fix m≥2. For t∈{0,1}^m define an edge coloring of Q_m by

\[
d_t(\{u,u\oplus e_i\})=\bigoplus_{j\ne i}(u_j\oplus t_j).
\]

This is well-defined on undirected edges. For x∈Q_m let f_t(x) be the smallest number of changes among spanning geodesics ending at x, and let E_r(d_t)={x:f_t(x)≤r}.

**Proposition 1 (rooted switch formula).**
\[
f_t(x)=\max\{0,\ |2\,\mathrm{wt}(x\oplus t)-m|-1\}.
\tag{1}
\]

*Proof.* A spanning path beginning at u traverses a permutation π_1,…,π_m. Put b_i=u_i⊕t_i. Its color in position k is
\[
w_k=\left(\bigoplus_i b_i\right)\oplus(k-1\bmod2)\oplus b_{\pi_k}.
\]
Therefore w_k≠w_{k+1} precisely when b_{\pi_k}=b_{\pi_{k+1}}. Among binary words with h ones and m−h zeros, the minimum number of adjacent equal pairs is \(\max\{0,|2h-m|-1\}\): alternating arrangements attain this bound, and the more frequent symbol requires at least \(|2h-m|-1\) same-symbol adjacencies. The initial vertex u is the complement of the terminal vertex x; complementing all b_i preserves |2h−m|. This proves (1).

**Corollary 2 (sparse endpoints).** If m is even,
\[
|E_2(d_t)|=\binom m{m/2}+2\binom m{m/2-1}.
\]
If m≥3 is odd,
\[
|E_2(d_t)|=2\binom m{(m-1)/2}+2\binom m{(m-3)/2}.
\]
Consequently \(|E_2(d_t)|/2^m=O(m^{-1/2})\), tending to zero. Hence a universal endpoint-intersection proof cannot rely on each arbitrary edge coloring having a positive constant fraction of eligible endpoints, or on an endpoint-set majority argument.

**Proposition 3 (paired alignment despite sparsity).** For any s,t∈{0,1}^m,
\[
\min_{x\in Q_m}\max\{f_t(x),f_s(x)\}=
\begin{cases}
1,&m\text{ even and }\mathrm{wt}(s\oplus t)\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\tag{2}
\]
Thus these two arbitrary face colorings always have corresponding endpoints of spanning paths with at most one switch each. However, for even m and odd \(\mathrm{wt}(s\oplus t)\), their monochromatic endpoint sets \(E_0(d_t)\) and \(E_0(d_s)\) are disjoint.

*Proof.* Partition the coordinates into I={i:s_i=t_i} and J={i:s_i≠t_i}. For any x define \(\epsilon_i=1-2(x_i\oplus t_i)\), \(A=\sum_{i\in I}\epsilon_i\), \(B=\sum_{i\in J}\epsilon_i\). The two imbalance quantities in (1) are |A+B| and |A−B|, with maximum |A|+|B|. We may choose x independently on I,J to minimize |A| and |B| to |I| mod 2 and |J| mod 2 respectively. Applying (1) gives
\[
\min_x\max(f_t(x),f_s(x))
=\max\{0,(|I|\bmod2)+(|J|\bmod2)-1\}.
\]
Both cardinalities are odd precisely when m is even and |J| is odd, proving (2). In that case one of |A+B|,|A−B| must be at least 2 for every x, so no endpoint is monochromatically attainable in both colorings.

**Scope.** Proposition 1 gives a quantitative obstruction to density-based approaches to the Article X endpoint-coincidence conjecture. Proposition 3 establishes paired endpoint coincidence for the entire signed rank-parity family, including instances in which either endpoint set occupies a vanishing proportion of the cube. The general arbitrary-pair endpoint intersection remains open.

**Proposition 4 (failure of multiway endpoint intersection).** For every power of two m≥8, there are m signed rank-parity colorings \(d_{t_1},\ldots,d_{t_m}\) of \(Q_m\) such that every pair has a common endpoint admitting a spanning path with at most one switch in each coloring, yet
\[
\bigcap_{j=1}^m E_2(d_{t_j})=\varnothing.
\]
More generally, if \(m>(r+1)^2\) is a power of two, then \(\bigcap_j E_r(d_{t_j})=\varnothing\).

*Proof.* Let H be an m×m Walsh–Hadamard matrix with entries ±1, so \(H^{\mathsf T}H=mI\). Choose \(t_j\) so the jth row of H is \(((-1)^{t_{j,i}})_i\). For any x put \(z_i=(-1)^{x_i}\). By orthogonality,
\[
\sum_{j=1}^m\left(\sum_{i=1}^m(-1)^{x_i\oplus t_{j,i}}\right)^2
=\|Hz\|_2^2=m^2.
\]
Thus for some j the imbalance has absolute value at least \(\sqrt m\). For m≥8, the imbalance is an even integer, so it is at least 4 and formula (1) gives \(f_{t_j}(x)\ge3\). The same formula gives \(f_{t_j}(x)\ge\sqrt m-1>r\) when \(m>(r+1)^2\). Since x was arbitrary, the full intersection is empty. Every pair satisfies Proposition 3.

This disproves any multiway Helly deduction based only on pairwise low-switch endpoint intersection, even inside the signed rank-parity family.

**Antipodal-odd specialization.** When m is even, \(d_t(\bar e)=1-d_t(e)\), since each edge color is the parity of m−1 exterior bits. Thus the vanishing endpoint density of Corollary 2 occurs even under the NORI1 antipodal law. In particular \(m=20\) gives \(|E_2|=520676<2^{19}\). For even m and \(\mathrm{wt}(s\oplus t)\) odd, the two colorings are individually antipodally odd yet have disjoint monochromatic endpoint sets by Proposition 3.
