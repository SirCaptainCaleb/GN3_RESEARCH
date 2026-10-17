# Rootwise commutator energy and sharp linear bigon-exchange activity

- Stable ID: note_8a7d1c151c6be956ffdde886
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, holonomy, root-activity, influence, bigon-exchange, unrestricted
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_1
- Updated session: session_nori_r10917_1
- Disposition: none
- Successor: none

## Related references

- note:note_63844857c6223f15944d26f9
- note:note_a674bfdfdd23faeef04d3cb8

## Research note

## Rootwise square curvature and bigon-exchange activity

Let \(n\ge4\), and let \(c\) be a legal antipodally odd coloring of \(Q_n\). Put \(U_i(x)=x\oplus(1-c_i(x))e_i\). For distinct \(i,j\), set \(D_{ij}=\partial_jc_i\), \(D_{ji}=\partial_ic_j\), and
\[
a_{ij}=\mathbb ED_{ij},\quad b_{ij}=\mathbb ED_{ji},\quad q_{ij}=\mathbb E(D_{ij}D_{ji}),\quad h_{ij}=a_{ij}+b_{ij}-q_{ij}.
\]
These derivatives are constant on each \((i,j)\)-face and invariant under antipodal translation. Let \(K_{ij}=(U_jU_i)^2\) and \(X\) be uniformly distributed on \(Q_n\).

**Theorem 1 (commutator root energy).**
\[
\boxed{\Pr(K_{ij}X\ne X)=\tfrac12(a_{ij}+b_{ij})-\tfrac14q_{ij},}
\tag{E1}
\]
\[
\boxed{\mathbb E d_H(K_{ij}X,X)=h_{ij},\qquad
\Pr([K_{ij}X\oplus X]_i=1)=\Pr([K_{ij}X\oplus X]_j=1)=\tfrac12h_{ij}.}
\tag{E2}
\]

*Proof.* Classify the two red-swap matchings on one \((i,j)\)-face by its derivative pair. If both derivatives vanish, the matchings commute. If both equal one, the red edges form an adjacent pair; the commutator is a three-cycle, moving three vertices with total Hamming displacement four, and changing each of the two relevant bits at two vertices. If only one derivative equals one, the face has one or three red edges; antipodal translation pairs these patterns and leaves both derivatives invariant. The one-red-face commutator is trivial. The three-red-face commutator takes each of the four face vertices to its opposite within that face, giving Hamming displacement two at each vertex. The averaged moved-vertex fraction, Hamming movement, and per-bit movement on an antipodal face pair are respectively \(1/2,1,1/2\). In the both-nonzero case they are \(3/4,1,1/2\). Averaging over faces proves (E1) and (E2). \(\square\)

**Theorem 2 (exchange activity independent of context).** Let \(W,W'\) be eligible embedded-bigon words with the same exterior restricted blocks and central words differing by one adjacent exchange of \(i\in A\), \(j\in B\):
\[
W=PijR,\qquad W'=PjiR.
\]
Then
\[
\boxed{\Pr_X(U_W(X)\ne U_{W'}(X))=\tfrac12(a_{ij}+b_{ij})-\tfrac14q_{ij},}
\tag{E3}
\]
\[
\boxed{\Pr_X([U_W(X)]_i\ne[U_{W'}(X)]_i)=\tfrac12h_{ij}.}
\tag{E4}
\]

*Proof.* Before the common suffix, the two maps take the uniform state \(Y=U_P(X)\) to \(U_jU_iY\) and \(U_iU_jY\). Their equality is equivalent, after a bijective change of variable, to \(K_{ij}Z=Z\) with \(Z\) uniform. A common suffix is a bijection, proving (E3). Since \(i\in A\), both appearances of \(i\) occur before the common suffix, so the suffix preserves bit \(i\). The same bijective change of variable transfers the difference in bit \(i\) to the bit-\(i\) displacement of \(K_{ij}\). Equation (E2) proves (E4). \(\square\)

**Corollary 3 (sharp linear exchange activity).** For each unordered pair \(\{i,j\}\), choose any eligible adjacent mixed-part exchange \(W_{ij}\leftrightarrow W'_{ij}\). Such exchanges exist for all \(n\ge4\), by placing two other distinct labels at the ends of the central permutation and \(i,j\) consecutively in its interior, with \(i\in A,j\in B\). Then
\[
\boxed{\sum_{i<j}\Pr_X(U_{W_{ij}}X\ne U_{W'_{ij}}X)\ge 3n/8,}
\tag{E5}
\]
\[
\boxed{\sum_{i<j}\mathbb E\,d_H(K_{ij}X,X)\ge n/2.}
\tag{E6}
\]
Both inequalities are sharp in arbitrarily large dimensions.

*Proof.* Let \(D=\sum_i\sum_{j\ne i}\operatorname{Inf}_j(c_i)\ge n\), by the Boolean Poincare inequality and the antipodally odd, mean-zero character of each signed rule. Since \(q_{ij}\le(a_{ij}+b_{ij})/2\), equation (E1) is at least \(3(a_{ij}+b_{ij})/8\), yielding (E5) on summation. Since \(h_{ij}\ge(a_{ij}+b_{ij})/2\), equation (E2) yields (E6). For the product of \(n/2\) reciprocal-reader squares, precisely \(n/2\) pairs have \(a=b=q=1\); all others have \(a=b=q=0\). Every active pair contributes \(3/4\) and \(1\) to the respective sums, attaining both inequalities. \(\square\)

The inequalities supply root-averaged curvature activity across the entire family of simple-bigon exchanges. They do not establish Hamming-defect descent: changes of multiple output bits can have competing signs, and improvements from distinct exchanges need not align at one starting fiber state.
