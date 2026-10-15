# Linear-threshold coset colorings admit one-switch full paths

# Linear-threshold one-switch theorem in both Coxeter models

We use the Coxeter parabolic-coset representation from the preceding subsection. Its two local-incidence spaces admit equivariant vector labels in the reflection representations, negated by their coset reversal involutions. A linear threshold of these vectors consequently defines a reversal-odd coloring. The theorem below produces a complete low-switch path in both types.

## The common threshold construction

Let \(G\) be either \(S_n\) (type \(A_{n-1}\)) or \(\mathbb F_2^n\rtimes S_n\) (type \(B_n\)), with \(K,\rho,t,m\) as in the preceding subsection. Let \(V\) be the real reflection representation, and choose the following \(K\)-fixed vector:
\[
q_A=e_1-e_3\in W=\{z\in\mathbb R^n:\sum_i z_i=0\},\qquad
q_B=\sum_{i=2}^n e_i\in\mathbb R^n.
\tag{1}
\]
In both cases \(\rho q=-q\). Hence
\[
R(gK)=gq
\tag{2}
\]
is a well-defined \(G\)-equivariant local-incidence vector satisfying \(R(g\rho K)=-R(gK)\). For any \(\theta\in V\) such that \(\langle\theta,gq\rangle\ne0\) for every \(g\in G\), put
\[
f_\theta(gK)=
\begin{cases}0,&\langle\theta,gq\rangle>0,\\1,&\langle\theta,gq\rangle<0.\end{cases}
\tag{3}
\]
It follows at once that this is an admissible reversal-odd coset coloring.

**Theorem 1 (constructive linear-threshold closure).** For either of the canonical type-A or type-B coset systems, every coloring of the form (3) has a complete Coxeter-orbit word with at most one switch. For type A, a suitable Hamilton ordering yields zero switches. For type B, a suitable cube root yields at most one switch for **every** dimension ordering; a root-slide rotation then produces a monochromatic full antipodal geodesic.

*Proof, type A.* Here \(gq_A=e_{g(1)}-e_{g(3)}\), so for the ordered triple \((a,h,c)\),
\[
b_\theta(a,h,c)=\mathbf1_{\{\theta_a-\theta_c<0\}}.
\]
The genericity assumption makes all \(\theta_a\) distinct. Take \(\pi\) listing the vertices in decreasing order of \(\theta\). Each triple \((\pi_j,\pi_{j+1},\pi_{j+2})\) satisfies \(\theta_{\pi_j}>\theta_{\pi_{j+2}}\); all its bits are zero. This is a Hamilton tight path and proves the claim.

*Proof, type B.* The signed-permutation action on \(\mathbb R^n\) is
\[
(a,\sigma)\cdot v=\operatorname{diag}((-1)^{a_1},\ldots,(-1)^{a_n})P_\sigma v.
\]
For an undirected cube edge \(E_i(y)=\{y,y\oplus e_i\}\), equation (2) becomes
\[
R(E_i(y))=\sum_{k\ne i}(-1)^{y_k}e_k,
\qquad
f_\theta(E_i(y))
=\mathbf1_{\{\sum_{k\ne i}(-1)^{y_k}\theta_k<0\}}.
\tag{4}
\]
The expression is independent of the endpoint chosen because its \(i\)-th term is absent. Complementing all cube bits negates the expression, so (4) is antipodally odd.

Choose a root \(x\in\mathbb F_2^n\) with \((-1)^{x_i}\theta_i=|\theta_i|\) for every \(i\); choose any dimension order \(\pi\). Immediately before the \(j\)-th step, dimensions \(\pi_1,\ldots,\pi_{j-1}\) have been flipped once, and all others have their starting signs. Thus the threshold quantity for the \(j\)-th traversed edge is
\[
M_j=\sum_{k>j}|\theta_{\pi_k}|-\sum_{k<j}|\theta_{\pi_k}|.
\tag{5}
\]
For adjacent positions,
\[
M_j-M_{j+1}=|\theta_{\pi_j}|+|\theta_{\pi_{j+1}}|\ge0.
\tag{6}
\]
All \(M_j\) are nonzero by genericity. Therefore the binary sign sequence \(\mathbf1_{\{M_j<0\}}\) is nondecreasing, and so has at most one switch. Every dimension occurs once, so the resulting path is a full antipodal geodesic. Root-slide rotation across its sole switch, when present, produces a monochromatic geodesic by the previously established NORI1 cyclic-rotation lemma. \(\square\)

## A monotone multi-threshold extension

**Corollary 2 (shared-chamber monotone aggregation).** Let \(f_{\theta^{(1)}},\ldots,f_{\theta^{(r)}}\) be threshold colorings in the same Coxeter model, and let
\[
\Phi:\{0,1\}^{r}\longrightarrow\{0,1\}
\]
be monotone in every argument and self-dual, meaning \(\Phi(\mathbf1-a)=1-\Phi(a)\). Define \(f=\Phi(f_{\theta^{(1)}},\ldots,f_{\theta^{(r)}})\) pointwise on local incidences.

In type A, if the weight vectors \(\theta^{(1)},\ldots,\theta^{(r)}\) induce one common strict ordering of the \(n\) vertices, then \(f\) has a monochromatic Hamilton tight path. In type B, if those weight vectors have a common entrywise sign pattern, then \(f\) has a one-switch full antipodal geodesic, and hence a monochromatic one.

*Proof.* Self-duality gives the required reversal oddness. In type A choose the common decreasing order: every constituent color word is constant zero, so the aggregate word is constant. In type B choose a root aligning the common sign pattern. For any dimension order, formula (6) applies to each constituent weight vector, making each constituent bit sequence nondecreasing. Monotonicity of \(\Phi\) makes their pointwise aggregate nondecreasing. The same root-slide completion applies. \(\square\)

For example, \(\Phi\) may be strict majority on an odd number of threshold colorings. The theorem establishes a common geometric subclass of the two open problems, including nonlinear combinations of compatible halfspaces. It does not establish one-switch existence for arbitrary reversal-odd coset colorings. The main unresolved issue is how to replace a globally consistent threshold vector by a topological obstruction when the coloring lacks a shared linear ordering or common sign pattern.
