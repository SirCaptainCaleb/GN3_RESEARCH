# Three-cube chain homotopy for every adjacent geodesic exchange

# Three-cube chain homotopy for adjacent dimension exchanges

Work over \(\mathbb F_2\) on the cubical boundary \(B_n=\partial[0,1]^n\), \(n\ge4\). For a set of free dimensions \(I\), let \(F_I(y)\) denote the cubical face containing the corner \(y\); changing bits of \(y\) inside \(I\) leaves this face unchanged.

For a full geodesic \(P=P(x;d_1,\ldots,d_n)\), Article XIV, Subsection 28, defines
\[
\Sigma_P=\sum_{i<j}F_{\{d_i,d_j\}}\left(x\oplus\bigoplus_{r=i}^{j-1}e_{d_r}\right),
\quad \partial\Sigma_P=P+\tau P.
\tag{1}
\]

**Theorem (adjacent-swap three-chain).** Suppose \(P'\) differs from \(P\) by swapping the adjacent dimensions \(a=d_k\), \(b=d_{k+1}\), where \(1\le k<n\). Put
\[
y=x\oplus\bigoplus_{r<k}e_{d_r},\quad F=F_{\{a,b\}}(y).
\]
Define a three-chain with \(n-2\) terms:
\[
\boxed{
\begin{aligned}
T_k={}&\sum_{r<k}F_{\{d_r,a,b\}}\left(x\oplus\bigoplus_{j=r+1}^{k-1}e_{d_j}\right)\\
&+\sum_{r>k+1}F_{\{a,b,d_r\}}\left(x\oplus\bigoplus_{j=k+2}^{r-1}e_{d_j}\right).
\end{aligned}}
\tag{2}
\]
Then
\[
\boxed{\Sigma_P+\Sigma_{P'}=F+\tau F+\partial T_k.}
\tag{3}
\]

*Proof.* Squares involving neither \(a\) nor \(b\), as well as the common \(\{a,b\}\) square, cancel between \(\Sigma_P\) and \(\Sigma_{P'}\). For every dimension \(d_r\) occurring before the swapped pair, the four surviving squares of types \(\{d_r,a\}\) and \(\{d_r,b\}\) are precisely the four side faces of the corresponding first-sum three-cube in (2). The analogous statement holds for every \(d_r\) occurring after the pair and its second-sum three-cube. These exhaust the difference of the two exchange disks.

Every three-cube also has two faces of type \(\{a,b\}\). In the first sum these extra faces telescope from the square at \(x\) to the square \(F\) at \(y\). In the second sum they telescope from the square at \(x\) to the square at \(x\oplus\bigoplus_{j=k+2}^ne_{d_j}\). The two squares at \(x\) cancel, and the remaining second endpoint is the antipode of \(F\), since its corner differs from \(\tau y\) only in the free bits \(a,b\). The cases with either sum empty follow by the same endpoint cancellation. This proves (3). \(\square\)

**Corollary (projective chain homotopy).** On the antipodal quotient \(\pi_B:B_n\to\mathbb{RP}^{n-1}\), the two squares \(F,\tau F\) project to the same cell and cancel. Therefore
\[
\boxed{\pi_{B*}\Sigma_P+\pi_{B*}\Sigma_{P'}=\partial(\pi_{B*}T_k).}
\tag{4}
\]
For any two-cocycle \(\eta\) on the quotient, its evaluations on these two projected exchange disks agree.

The formula was checked independently by cubical boundary expansion on 150 random root-and-order choices for every \(4\le n\le7\), at each adjacent swap position. The proof is uniform for all dimensions.

**Relation to the dimension-simple Wu–Yang adaptation.** Equation (3) supplies a prescribed three-dimensional correction for each Coxeter adjacent transposition, using only ordinary cube faces and an antipodal pair of the two-dimensional exchange squares. The uncolored exchange-disk homotopy is therefore already explicit. The remaining mathematical difficulty is lifting these corrections through the color-sensitive, dimension-preserving reachability records, including coherence for Coxeter braid and commuting relations. No monochromatic-path existence claim follows from (3) alone.
