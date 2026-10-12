# Maximum rooted switch count forces rank-parity coloring

- Stable ID: note_article_x_maximal_alternation_root_rigidity_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_x_switch_induction
- Labels: rooted-switch-profile, endpoint-coincidence, rigidity
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6323_2
- Updated session: session_nori_r6323_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let \(m\ge3\) and let \(d\) be any binary coloring of the undirected edges of \(Q_m\). Write \(f_d(x)\) for the minimum number of changes among geodesics spanning \(Q_m\) from \(x\) to its antipode (equivalently, terminating at \(x\), by reversal).

**Theorem (rigidity of maximal rooted alternation).** A vertex \(x\) satisfies \(f_d(x)=m-1\) if and only if there is a bit \(b\) such that for every edge in direction \(i\),
\[
d_i(y)=b\oplus\bigoplus_{j\ne i}(y_j\oplus x_j).
\tag{1}
\]
If (1) holds, then the only vertices with \(f_d=m-1\) are \(x\) and \(\bar x\). Hence, for every arbitrary coloring \(d\), the set of roots \(x\) with \(f_d(x)=m-1\) is either empty or one antipodal pair. In particular
\[
\left|E_{m-2}(d)\right|\ge 2^m-2,
\qquad
\left|E_{m-2}(d)\cap E_{m-2}(e)\right|\ge 2^m-4
\tag{2}
\]
for any two arbitrary edge colorings \(d,e\). In dimension \(m=4\), this gives the unrestricted common-terminal assertion \(E_2(d)\cap E_2(e)\ne\varnothing\), with at least twelve common terminals.

*Proof.* If \(f_d(x)=m-1\), every spanning geodesic starting at \(x\) has its maximal possible \(m-1\) switches, so every color word alternates. For distinct directions \(i,j\), choose a third direction \(k\). Compare the two geodesics beginning with \((i,j,k)\) and \((j,i,k)\), followed by the same remaining directions. Their third edges coincide. In an alternating length-\(m\) word its third color equals its first, so the initial edges at \(x\) in directions \(i,j\) have the same color \(b\). This works for all \(i,j\). Every edge directed outward from \(x\), from rank \(r\) to rank \(r+1\), can be included as the \((r+1)\)-st edge of some spanning geodesic rooted at \(x\); alternation forces its color to be \(b\oplus(r\bmod2)\). For an undirected \(i\)-edge \(\{y,y^i\}\), the endpoint whose \(i\)-bit equals \(x_i\) is closer to \(x\); its rank is \(\sum_{j\ne i}(y_j\oplus x_j)\), proving (1). Conversely (1) makes the colors along every spanning geodesic rooted at \(x\) alternate.

For the remaining classification put \(t_j=y_j\oplus x_j\). If \(t\) contains both a zero and a one, select directions \(i,j\) with \(t_i=0,t_j=1\) and begin a spanning geodesic from \(y\) with \((i,j)\). Its first edge has color \(b\oplus\bigoplus_k t_k\). After flipping \(i\), its second edge in direction \(j\) has the same color, since the first flip adds one to the exterior parity and the excluded \(j\)-bit contributes one. Thus \(f_d(y)\le m-2\). At \(y=x\) and \(y=\bar x\), the color word alternates for every order, giving \(f_d=m-1\). This establishes the claimed dichotomy and (2). \(\square\)

This is a converse rigidity strengthening of the rooted switch formula for shifted rank-parity colorings in note \`note_article_x_signed_rank_parity_endpoint_sparsity_20261011\`. Its terminal-set intersection consequence is sharp in the near-maximum threshold \(m-2\), while it does not supply a dimension-independent two-switch bound when \(m\ge5\`.
