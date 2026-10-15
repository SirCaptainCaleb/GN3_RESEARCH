# Lie endpoint compression for filtered root wall variation

# Lie endpoint compression for filtered root-wall variation

The rank-lowering identity for the central-edge-changing type-D chamber wall in Article XIV contains an arity-\((n-2)\) right-normed Lie polynomial. We show that, even though individual Petrie-cycle switch grades depend on the complete direction ordering, their *difference under one initial square pivot* depends only on the first and last unused directions. The Lie coefficient sum of any such endpoint-dependent statistic collapses to at most four terms. In particular the signed first-order switch variation across a root wall uses only two of the remaining directions, for every unrestricted antipodally odd coloring.

Let \(n\ge4\). Fix a vertex \(g\) and distinct cube directions \(i,j\). Put \(\ell=n-2\) and let \(K=(k_1,\ldots,k_\ell)\) be a total order of the remaining directions. Write \(C(g;\tau)\) for the unoriented Petrie cycle whose first antipodal half starts at \(g\) and has dimension sequence \(\tau\). For a legal coloring \(c\), its twisted cyclic switch defect \(h_c(C)\) is defined by the antiperiodic switch word as in the previous subsections. It is invariant under root slides and reversal.

For \(\sigma\in S_K\), define the root-square switch increment
\[
\Delta_c(\sigma)=h_c(C(g;i,j,\sigma))-h_c(C(g;j,i,\sigma)).
\tag{1}
\]
Put
\[
a=c(g,g\oplus e_i),\quad b=c(g\oplus e_i,g\oplus e_i\oplus e_j),
\quad a'=c(g,g\oplus e_j),\quad b'=c(g\oplus e_j,g\oplus e_i\oplus e_j).
\tag{2}
\]
For each unused direction \(u\) and \(v\), write
\[
q_u=c(g\oplus e_i\oplus e_j,\ g\oplus e_i\oplus e_j\oplus e_u),\qquad
p_v=c(\bar g\oplus e_v,\bar g)=1-c(g,g\oplus e_v).
\tag{3}
\]
The final equality follows from antipodal oddness.

**Theorem 1 (endpoint locality of a root-square switch increment).** If \(\sigma\) begins in direction \(u\) and ends in direction \(v\), then
\[
\boxed{
2\Delta_c(\sigma)
=[p_v=a]-[p_v=a']+[a\ne b]-[a'\ne b']
+[b\ne q_u]-[b'\ne q_u].
}
\tag{4}
\]
In particular, \(\Delta_c(\sigma)\in\{-1,0,1\}\) and depends on \(\sigma\) only through \(\sigma_1=u\) and \(\sigma_\ell=v\). This holds for all legal colorings, without any flatness condition.

*Proof.* The two full geodesics have color words
\[
(a,b,t_1,\ldots,t_\ell),\qquad(a',b',t_1,\ldots,t_\ell),
\]
because they reach the same vertex after their first two edges and then traverse the same remaining directions. Their shared first tail bit is \(t_1=q_u\), and their shared last bit is \(t_\ell=p_v\). The twisted cyclic comparison count consists of successive unequal-color comparisons, together with the closing equality comparison between the final and initial colors. All comparisons strictly inside the common tail cancel when subtracting the two counts. The three remaining comparisons give the right side of (4). Both twisted counts are positive odd integers; their difference is even. Changing only the first two edge colors changes the twisted half-switch defect by at most one, by the established adjacent-dimension exchange law in Article XIV. \(\square\)

Let \(D_\ell(K)=[k_1,[k_2,[\cdots,[k_{\ell-1},k_\ell]]\cdots]]\) be the right-normed multilinear commutator, expanded into associative words with integer coefficients \(\epsilon_K(\sigma)\in\{0,\pm1\}\). Let \(\mathcal U(K)\) be its support of unimodal permutations.

**Theorem 2 (four-endpoint Dynkin compression).** For every \(\ell\ge3\) and every function \(\Phi\) of the first and last letters of a permutation,
\[
\boxed{
\begin{aligned}
\sum_{\sigma\in\mathcal U(K)}\epsilon_K(\sigma)\Phi(\sigma_1,\sigma_\ell)
={}&\Phi(k_1,k_\ell)-\Phi(k_1,k_{\ell-1})\\
&+(-1)^\ell\Phi(k_{\ell-1},k_1)
+(-1)^{\ell-1}\Phi(k_\ell,k_1).
\end{aligned}}
\tag{5}
\]
For \(\ell=2\), the right side is replaced by \(\Phi(k_1,k_2)-\Phi(k_2,k_1)\). The identities hold over every coefficient group for which integer scalar multiplication is defined.

*Proof.* Expand the right-normed bracket by successively inserting \(k_{\ell-1},k_{\ell-2},\ldots,k_1\) at the left or right end of the existing word, with a minus sign for right insertion. Fix the first and last letters in the resulting word and sum its coefficients. Inductively these two-end marginal sums vanish except for four ordered pairs:
\[
(k_1,k_\ell)\mapsto1,\quad
(k_1,k_{\ell-1})\mapsto-1,\quad
(k_{\ell-1},k_1)\mapsto(-1)^\ell,\quad
(k_\ell,k_1)\mapsto(-1)^{\ell-1}.
\tag{6}
\]
To verify the induction, use \(D_\ell(K)=k_1D_{\ell-1}(K')-D_{\ell-1}(K')k_1\), where \(K'=(k_2,\ldots,k_\ell)\). The first summand fixes the first letter at \(k_1\), so its last-letter marginals are those of \(D_{\ell-1}\); the second fixes the last letter at \(k_1\), so its first-letter marginals are the negatives of those of \(D_{\ell-1}\). These one-end marginals follow from the same recurrence, or directly from the endpoint insertion rule: the last-letter marginals are \(+1\) at \(k_\ell\), \(-1\) at \(k_{\ell-1}\), and zero otherwise; the first-letter marginals are \((-1)^{\ell-1}\) at \(k_\ell\), \((-1)^\ell\) at \(k_{\ell-1}\), and zero otherwise. This proves (6) for all \(\ell\ge3\), beginning with the four terms of \(D_3\). Summing the endpoint function against (6) gives (5). The two terms of \(D_2\) give the remaining case. \(\square\)

Define the half-integer-valued functions
\[
F(v)=\frac{[p_v=a]-[p_v=a']}{2},
\qquad
G(u)=\frac{[b\ne q_u]-[b'\ne q_u]}{2}.
\tag{7}
\]

**Theorem 3 (four-edge formula for the signed first-order switch wall defect).** For every \(n\ge4\),
\[
\boxed{
\begin{aligned}
\mathfrak d_c(i,j;K)
&:=\sum_{\sigma\in\mathcal U(K)}
\epsilon_K(\sigma)\Delta_c(\sigma)\\
&=F(k_\ell)-F(k_{\ell-1})
+(-1)^\ell\bigl(G(k_{\ell-1})-G(k_\ell)\bigr).
\end{aligned}}
\tag{8}
\]
In particular, the right side is an integer, lies between \(-2\) and \(2\), and is independent of \(k_1,\ldots,k_{\ell-2}\) and their order. It depends on the root-square colors and on the four endpoint-star edge colors belonging to only the two greatest-ranked remaining directions.

*Proof.* Theorem 1 gives
\[
\Delta_c(\sigma)=
\frac{[a\ne b]-[a'\ne b']}{2}
+F(\sigma_\ell)+G(\sigma_1).
\]
For \(\ell\ge2\), the sum of the coefficients of \(D_\ell\) is zero, as every commutator has zero augmentation. The last-letter signed marginals are \(+1\) at \(k_\ell\) and \(-1\) at \(k_{\ell-1}\). The first-letter signed marginals are \((-1)^{\ell-1}\) at \(k_\ell\) and \((-1)^\ell\) at \(k_{\ell-1}\). Substituting these marginals gives (8). Although \(F,G\) may be half-integral, the left side is an integer. Each difference of \(F\) or \(G\) has absolute value at most one, proving the bound. \(\square\)

**Corollary 4 (all signed grade-crossing event counts have four-endpoint compression).** Define \(N_+\) and \(N_-\) to be the Lie-signed sums of the indicators of \(\Delta_c(\sigma)=+1\) and \(\Delta_c(\sigma)=-1\), respectively, and \(N_{\times}=N_++N_-\). For every \(\ell\ge3\), all three are determined by the four endpoint pairs in (6) through
\[
N_{\times}=
\sum_\sigma\epsilon_K(\sigma)\Delta_c(\sigma)^2,
\qquad
N_\pm=\frac12\bigl(N_{\times}\pm\mathfrak d_c(i,j;K)\bigr).
\tag{9}
\]
For \(\ell=2\), only the two endpoint pairs of the base case are needed.

*Proof.* The values of \(\Delta_c\) are \(-1,0,1\), so the indicators of nonzero, positive, and negative increments are the indicated polynomials in \(\Delta_c\). By Theorem 1, each is an endpoint function. Apply Theorem 2 to each. \(\square\)

**Scope for a switch-filtered Wu--Yang construction.** A central-edge wall exchanges \(i,j\) and produces a rank-lowered multilinear Lie defect. Theorem 3 shows that its first moment in twisted switch grade is supported on the root square plus the two greatest-ranked residual directions: all lower-ranked directions cancel algebraically, without a coloring restriction. Corollary 4 compresses signed totals of upward and downward grade changes as well. These are not statements about a fixed switch level; the indicator that a cycle lies below a given switch threshold depends on its full interior color word and need not be an endpoint function. A proof of unrestricted NORI1 would still need a filtered higher-order cancellation or an obstruction class that retains this interior information.
