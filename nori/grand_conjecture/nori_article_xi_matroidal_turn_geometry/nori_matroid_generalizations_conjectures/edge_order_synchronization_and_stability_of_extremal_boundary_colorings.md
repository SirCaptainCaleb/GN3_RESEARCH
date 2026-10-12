# Edge-order synchronization and stability of extremal boundary colorings

# Edge-order synchronization and stability of extremal boundary colorings

Let \(n\ge6\), and let \(V_n\) consist of real functions \(x(a,b,c)=-x(c,b,a)\) on ordered triples of distinct labels. Its dimension is \(N=n(n-1)(n-2)/2\). The legal-turn reversal quotient has \(E=N(n-3)\) edges. For sign-valued \(x\), let \(D(x)\) count disagreeing turns. Recall the signed adjacency operator
\[
(Ax)(a,b,c)=\sum_{d\notin\{a,b,c\}}[x(b,c,d)+x(d,a,b)]
\]
with spectrum contained in \(\{-(n-2),-2,0,1,n-2\}\). Its smallest eigenspace is
\[
\mathcal E_-=\{f_s(a,b,c)=s_{ab}-s_{bc}:s_{ab}=s_{ba},\ \sum_{b\ne a}s_{ab}=0\}.
\]
Let \(\mathcal G=\{f:f(a,b,c)=u_b(a)-u_b(c)\}\) be the direct sum of local gradient spaces; then \(\mathcal E_-\subseteq\mathcal G\).

**Theorem 1 (canonical symmetric edge potential).** For \(x\in V_n\) define
\[
d_b(a)=\sum_{c\notin\{a,b\}}x(a,b,c),\quad
h_{ab}=d_b(a)+d_a(b),\quad H_a=\sum_{b\ne a}h_{ab}.
\]
The symmetric weights
\[
\boxed{s_{ab}=\frac1{2(n-1)}
\left(h_{ab}-\frac{H_a+H_b}{n-2}\right)}
\tag{1}
\]
have zero row sums and determine the orthogonal projection
\(\Pi_-x=f_s\) onto \(\mathcal E_-\). The nonnegative global synchronization defect
\[
\Gamma(x)=\|\Pi_{\mathcal G}x-\Pi_-x\|^2
\]
has the explicit expression
\[
\boxed{\Gamma(x)=
\frac1{n-1}\sum_b\sum_{a\ne b}d_b(a)^2-
\frac1{2(n-1)}\sum_{a<b}
\left(h_{ab}-\frac{H_a+H_b}{n-2}\right)^2.}
\tag{2}
\]

*Proof.* Reversal skewness gives \(\sum_{a\ne b}d_b(a)=0\), hence \(\sum_aH_a=0\). Formula (1) has zero row sums. For any symmetric zero-row-sum array \(t\), define \(f_t(a,b,c)=t_{ab}-t_{bc}\). Expanding over outer pairs yields
\[
\langle x,f_t\rangle=\sum_{a<b}h_{ab}t_{ab},\qquad
\langle f_s,f_t\rangle=2(n-1)\sum_{a<b}s_{ab}t_{ab}.
\]
Their difference is zero because \(h_{ab}-2(n-1)s_{ab}=(H_a+H_b)/(n-2)\) is orthogonal to \(t\). This proves the projection claim. The local gradient projection has coordinates \((d_b(a)-d_b(c))/(n-1)\) and squared norm \((n-1)^{-1}\sum_{a\ne b}d_b(a)^2\). The norm of \(f_s\) is \(2(n-1)\sum_{a<b}s_{ab}^2\). Subtraction of the nested projection norms proves (2). \(\square\)

For each center \(b\), orient its tournament of outer labels by \(x(a,b,c)\), and let \(t_b\) count directed cyclic triangles, \(T(x)=\sum_b t_b\).

**Theorem 2 (joint curvature and synchronization penalty).** Every sign-valued reversal-skew \(x\) obeys
\[
\boxed{\frac{D(x)}E\le
\frac23+\frac{n-2}{2(n-3)(n-1)}
-\frac{2(n-4)T(x)}{(n-1)E}
-\frac{(n-4)\Gamma(x)}{4E}.}
\tag{3}
\]
*Proof.* The complete-graph Hodge identity yields
\(\|x-\Pi_{\mathcal G}x\|^2=n(n-2)(n-3)/6+8T(x)/(n-1)\).
Nested orthogonal projections add \(\Gamma(x)\) to this squared distance. The spectral gap between \(-(n-2)\) and the remaining eigenvalues, which are at least \(-2\), gives
\[
\langle x,Ax\rangle\ge-(n-2)N+
(n-4)\|x-\Pi_-x\|^2.
\]
Use \(\langle x,Ax\rangle=2E-4D(x)\) and simplify. \(\square\)

**Lemma 3 (elementary tournament stability).** A tournament on \(m\ge3\) vertices with \(t\) cyclic triangles can be made transitive by reversing at most \(8m^2(t/m^3)^{1/3}\) arcs, with zero changes when \(t=0\).

*Proof.* List vertices in increasing outdegree \(d_0\le\cdots\le d_{m-1}\). Counting transitive triples by their source gives
\(\sum_i i^2-\sum_i d_i^2=2t\).
For each \(k\), the \(k\) lowest-degree vertices have at least \(\binom{k}{2}\) internal wins, so \(\sum_{i<k}(d_i-i)\ge0\). Summation by parts against increasing \(d_i\) yields \(\sum_i(i-d_i)d_i\ge0\), hence
\[
\sum_i(i-d_i)^2\le2t. \tag{4}
\]
An inversion in the score order is an arc \(i\to j\) with \(i<j\). It belongs to at least \(d_j-d_i+1\) cyclic triangles, as follows by comparing the two endpoint outdegrees and partitioning their other neighbors into four orientation types.

Set \(\delta=t/m^3\), \(\eta=\delta^{1/3}\), \(\theta=\delta^{1/2}\), assuming \(t>0\). At most \(2t/(\eta^2m^2)\) vertices have \(|d_i-i|>\eta m\), so at most \(2t/(\eta^2m)\) inversion arcs touch such vertices. Among the remaining vertices, at most \((\theta+2\eta)m^2\) pairs have rank separation at most \((\theta+2\eta)m\). Every other inverted arc has outdegree gap greater than \(\theta m\), hence participates in at least \(\theta m\) cyclic triangles. Since each cyclic triangle has three arcs, there are at most \(3t/(\theta m)\) such inversions. The total is at most
\[
m^2\big(\theta+2\eta+2\delta/\eta^2+3\delta/\theta\big)
=m^2(4\delta^{1/3}+4\delta^{1/2})
\le8m^2\delta^{1/3}.
\]
Reversing the inversions gives a transitive order. \(\square\)


**Theorem 4 (near-extremal stability toward edge orderings).** Define
\[
\varepsilon=\max\{0,\,2/3-D(x)/E\},\qquad
z=\varepsilon+\frac{n-2}{2(n-3)(n-1)}.
\]
There exist pairwise distinct symmetric edge weights \(s_{ab}=s_{ba}\) such that the comparison coloring \(x_s(a,b,c)=\operatorname{sgn}(s_{ab}-s_{bc})\) differs from \(x\) on at most \(O(Nz^{1/9})\) reversal classes of triples, with an absolute implied constant. Consequently \(D(x_n)/E_n\ge2/3-o(1)\) forces agreement with an edge-ordered boundary coloring on \(1-o(1)\) of all triple classes.

*Proof.* The nonnegative penalties in (3) give
\[
\frac{2(n-4)T}{(n-1)E}+\frac{(n-4)\Gamma}{4E}\le z.
\]
Writing \(m=n-1\), we have \(T/(nm^3)\le3z/10\) and \(\Gamma/N\le6z\). Apply Lemma 3 to the \(n\) local tournaments. Jensen's inequality supplies a reversal-skew coloring \(y\), whose local tournaments are all transitive, with \(R\) altered triple classes satisfying
\[
R/N\le \frac{16m}{m-1}(T/(nm^3))^{1/3}
\le20z^{1/3}. \tag{5}
\]
Take the symmetric potential \(s\) computed by (1), so \(\Pi_-x=f_s\). Projection contractivity, \(\|x-y\|^2=4R\), and the definition of \(\Gamma\) give
\[
\|\Pi_{\mathcal G}y-f_s\|^2\le8R+2\Gamma. \tag{6}
\]
The signed outdegree scores of a transitive tournament on \(m\) vertices are \(-(m-1),-(m-3),\ldots,m-1\). Consequently the local gradient projection \((\Pi_{\mathcal G}y)(a,b,c)\) has the same sign as \(y(a,b,c)\) and magnitude \(2|i-j|/m\), where \(i,j\) are their local ranks.

For any \(0<\theta<1\), the fraction of outer pairs with rank separation smaller than \(\theta m\) is at most \(2m\theta/(m-1)\). Every other pair at which \(y\) and the sign of \(f_s\) disagree contributes at least \(4\theta^2\) to (6). Perturb the finitely many symmetric weights generically by sufficiently small amounts to eliminate ties while preserving all strict comparisons. Thus
\[
\frac{\operatorname{dist}(x,x_s)}N
\le\frac RN+\frac{2m}{m-1}\theta+
\frac{8R+2\Gamma}{4\theta^2N}. \tag{7}
\]
Taking \(\theta=z^{1/9}\) when \(z<1\), and applying (5) and the preceding bounds, proves the assertion. For \(z\ge1\) the bound is immediate after enlarging its absolute constant. \(\square\)

The theorem concerns unrestricted reversal-odd boundary tournaments; the edge-ordered subclass emerges quantitatively in the near-extremal density regime. Transferring long vertex-simple paths across exceptional triples requires a separate robustness argument.
