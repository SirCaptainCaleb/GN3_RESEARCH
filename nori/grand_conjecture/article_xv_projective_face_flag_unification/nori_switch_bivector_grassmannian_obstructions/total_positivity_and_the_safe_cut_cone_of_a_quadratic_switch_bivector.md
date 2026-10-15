# Total positivity and the safe cut cone of a quadratic switch bivector

### Total positivity and the safe cone of cut directions

Fix an order \(\pi=(\pi_1,\ldots,\pi_n)\), \(n\ge4\), and the type-A reflection space \(W=\{x\in\mathbb R^n:\sum_i x_i=0\}\). Its centered prefix vectors are
\[
Z_j=\sum_{h=1}^j e_{\pi_h}-\frac jn\mathbf1,\qquad 1\le j<n.
\]
Their Gram kernel is \(G(i,j)=\langle Z_i,Z_j\rangle=\min(i,j)-ij/n\).

**Theorem 1 (strict total positivity of order two).** For all \(1\le i<j<n\) and \(1\le p<q<n\),
\[
\boxed{D(i,j;p,q):=G(i,p)G(j,q)-G(i,q)G(j,p)\ge0.}\tag{1}
\]
Equality holds precisely when the open real intervals \((i,j)\) and \((p,q)\) are disjoint; otherwise \(D(i,j;p,q)>0\).

*Proof.* Since \(G(i,p)>0\) for all interior ranks, fix \(i<j\) and consider
\[
R(t)=G(i,t)/G(j,t)
=\begin{cases}
(n-i)/(n-j),&t\le i,\\
i(n-t)/[t(n-j)],&i\le t\le j,\\
i/j,&t\ge j.
\end{cases}
\]
This is nonincreasing in \(t\), strictly decreasing precisely on \((i,j)\). Multiplying the inequality \(R(p)\ge R(q)\) by \(G(j,p)G(j,q)>0\) gives (1). Strictness occurs precisely if \((p,q)\) intersects \((i,j)\) in a nonempty open interval. QED.

**Theorem 2 (positive cone of safe contractions).** Let \(S\subseteq\{1,\ldots,n-1\}\) contain at least two ranks, with \(p=\min S<q=\max S\). Give every pair \(r<s\) in \(S\) a nonnegative weight \(w_{rs}\), with \(w_{pq}>0\), and set
\[
\mathcal B=\sum_{r<s,\ r,s\in S}w_{rs}\,Z_r\wedge Z_s.
\]
Then:
1. \(\langle \mathcal B,Z_i\wedge Z_j\rangle\ge0\) for every \(i<j\), strictly if some positive-weight interval \((r,s)\) overlaps \((i,j)\).
2. For every nonzero choice of coefficients \(\lambda_t\ge0\) over \(p\le t\le q\), the vector
\[
T=\sum_{t=p}^q\lambda_tZ_t
\quad\text{satisfies}\quad
\boxed{\iota_T\mathcal B\ne0.}\tag{2}
\]
Consequently every continuous interpolation of cut vectors within this positive cone produces a nonvanishing contracted switch-vector.

*Proof.* The bivector inner product identity
\[
\langle Z_r\wedge Z_s,Z_i\wedge Z_j\rangle=D(i,j;r,s)
\]
proves (1) by Theorem 1 and nonnegative weights. If some \(\lambda_t>0\) for \(t<q\), then
\[
\langle \mathcal B,T\wedge Z_q\rangle
=\sum_{t=p}^{q-1}\lambda_t\langle \mathcal B,Z_t\wedge Z_q\rangle>0,
\]
because the \((p,q)\)-summand has a strictly positive determinant whenever \(p\le t<q\). A zero contraction by \(T\) would make this scalar zero, a contradiction. If the only positive coefficient occurs at \(q\), use instead \(\langle\mathcal B,Z_p\wedge T\rangle>0\). QED.

**Corollary 3 (reversal-odd plane carrier of the full quadratic switch tensor).** Let a full Hamilton order carry at least two switches, at ranks \(S\), and let \(\mathcal B\) be its full unweighted quadratic switch bivector. Put
\[
T(\pi)=\sum_{t=p}^{q}Z_t(\pi),\qquad H(\pi)=\iota_{T(\pi)}\mathcal B(\pi).
\]
Then \(H(\pi)\ne0\) and \(H(\pi)\perp T(\pi)\). Hence the oriented plane
\[
\boxed{\Phi(\pi)=\bigl(\operatorname{span}\{T(\pi),H(\pi)\},\,T(\pi)\wedge H(\pi)\bigr)\in\widetilde{\mathrm{Gr}}_2(W)}
\tag{3}
\]
is well defined. Under complemented reversal of the order and color word,
\[
T(\pi^R)=-T(\pi),\quad \mathcal B(\pi^R)=-\mathcal B(\pi),\quad
H(\pi^R)=H(\pi),\quad \boxed{\Phi(\pi^R)=J\Phi(\pi),}
\]
where \(J\) reverses the plane orientation.

*Proof.* Reversal sends \(Z_{n-j}(\pi^R)=-Z_j(\pi)\) and the switch set \(S\) to \(n-S\); the first two identities follow by reindexing, and the other assertions by contraction and wedge orientation. Nonvanishing comes from (2) with all \(\lambda_t=1\). QED.

**Corollary 4 (safe adjacent-cut slides).** If two neighboring rank cuts \(a,a+1\) satisfy \(p\le a<a+1\le q\), every interpolated cut \(T(t)=(1-t)Z_a+tZ_{a+1}\), \(0\le t\le1\), contracts \(\mathcal B\) nontrivially. Thus local motion of the cut between consecutive ranks inside the first/last switch interval has a canonical zero-free homotopy, without discarding the intermediate switch contributions.

**Interpretation and limitation.** This identifies a substantial contractible family of admissible cut directions and a reversal-equivariant oriented-plane assignment depending on the *complete* switch bivector rather than solely the extreme two switches. It is valid in both the cube-edge and boundary-triple settings at the flag level, because only reversal of the centered prefix vectors and positivity of the switch-pair weights are used. It does not yet extend the map continuously across Coxeter flag exchanges: after a swap the centered-prefix configuration and the switch set may both change. Such cross-flag compatibility is the next color-sensitive question.
