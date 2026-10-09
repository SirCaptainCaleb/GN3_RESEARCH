# Actual opposite-endpoint full geodesics form a free antipodal high-index permutohedral face nerve; at least 2n−4 exist per root

# An honest high-index carrier made only of actual endpoint-opposed full geodesics

Let \(n\ge7\), fix ANY cube root \(x\), and consider the standard \((n-1)\)-dimensional permutohedron \(P_n\). Its vertices \(v_\pi\) index all full cube geodesics \((x,\pi)\); central inversion sends \(v_\pi\) to \(v_{\operatorname{rev}\pi}\). For each direction permutation \(\pi\), write its actual ordered-three-face word as \(w_1(x,\pi),\ldots,w_{n-2}(x,\pi)\), and define
\[
q_x(\pi)=w_1(x,\pi)+w_{n-2}(x,\pi)-1\in\{-1,0,1\}.
\tag{1}
\]
The existing permutohedral theorem proves \(q_x(\operatorname{rev}\pi)=-q_x(\pi)\) and \(|q_x(\pi)-q_x(\pi')|\le1\) on each permutohedral 1-skeleton edge (an adjacent transposition), because the first and last triple windows cannot both be affected when \(n\ge7\).

Let \(F_x:\partial P_n\to\mathbb R\) be the odd PL function obtained by assigning at every face barycenter the arithmetic mean of \(q_x\) on that face's permutation vertices and extending linearly on its barycentric subdivision. Let \(Z_x=F_x^{-1}(0)\). By the previously proved odd-map zero-carrier index theorem, the free antipodal quotient satisfies
\[
w_1(Z_x/\tau)^{n-3}\ne0.
\tag{2}
\]

Define the set \(\mathcal B_x=\{\pi:q_x(\pi)=0\}\), consisting of **ACTUAL FULL ANTIPODAL GEODESICS whose first and last ordered-face colors are opposite**. Define a finite abstract simplicial complex \(K_x\) with vertex set \(\mathcal B_x\) by declaring \(\sigma=\{\pi_0,\ldots,\pi_k\}\) a simplex if the corresponding permutation vertices \(v_{\pi_i}\) all lie in **some common proper face** of the permutohedron. The involution \(\pi\mapsto\operatorname{rev}\pi\) is simplicial on \(K_x\).

**Theorem 1 (every interpolated zero has a true path in its carrier face).** If \(z\in Z_x\) and \(H\) is the unique minimal permutohedral face whose relative interior contains \(z\), then \(H\) contains at least one vertex \(v_\pi\) with \(q_x(\pi)=0\).

**Proof.** Suppose no original permutation vertex of \(H\) has \(q=0\). Its 1-skeleton is connected (as the graph of a convex polytope), and adjacent vertices cannot have opposite \(q\) signs because \(q\in\{\pm1\}\) on all vertices of \(H\) and the edge difference is at most one. Consequently EVERY vertex of \(H\) has the SAME sign \(s\in\{\pm1\}\). Every nonempty subface of \(H\) has only vertices of this sign, so all their barycentric means equal \(s\). The barycentric PL extension therefore satisfies \(F_x\equiv s\) on the entire face \(H\), contradicting \(z\in Z_x\). \(\square\)

**Theorem 2 (path-only high-index nerve).** The genuine-geodesic complex \(K_x\) is a FREE antipodal simplicial complex and
\[
\boxed{w_1(K_x/\tau)^{n-3}\ne0.}
\tag{3}
\]
Thus \(\operatorname{ind}_{\mathbb Z_2}(K_x)\ge n-3\), with no interpolated points serving as vertices or fictitious full geodesics.

**Proof.** For every \(v_\pi\) with \(\pi\in\mathcal B_x\), let \(U_\pi\subseteq\partial P_n\) be its *open polyhedral star*: the union of relative interiors of all nonempty proper faces containing \(v_\pi\). These are open in the boundary face-complex topology: a point in a face's relative interior has a neighborhood only among that face and its cofaces. By Theorem 1, the open sets \(U_\pi\cap Z_x\) cover \(Z_x\). They are interchanged by the central antipodal involution, since \(U_{\operatorname{rev}\pi}=-U_\pi\).

A family of such open stars intersects if and only if all their vertices belong to some common proper face \(H\) (a point of the intersection lies in the relative interior of a face containing all the vertices; conversely the relative interior of \(H\) lies in all these stars). Hence the **nerve of the ambient open-star cover** is exactly \(K_x\). The nerve of the restricted cover of \(Z_x\) is a subcomplex of \(K_x\).

Choose a continuous partition of unity subordinate to the finite open cover of compact \(Z_x\). Average it under the antipodal involution to make the weights satisfy \(\lambda_{\operatorname{rev}\pi}(-z)=\lambda_\pi(z)\). The standard nerve map
\[
f:Z_x\longrightarrow |K_x|,\qquad
f(z)=\sum_{\pi\in\mathcal B_x}\lambda_\pi(z)e_\pi
\]
is continuous and antipodally equivariant. No proper face of a centrally symmetric polytope contains both a vertex \(v\) and its opposite \(-v\): otherwise its convexity would include the polytope center, which lies in the interior. Thus NO simplex of \(K_x\) contains both \(\pi\) and \(\operatorname{rev}\pi\). This makes the geometric simplicial involution on \(K_x\) free.

An equivariant map between free involution spaces pulls the antipodal quotient double-cover class back to that of the source. Therefore nonvanishing of \(w_1(Z_x/\tau)^{n-3}\) from (2) implies nonvanishing of \(w_1(K_x/\tau)^{n-3}\), proving (3). \(\square\)

**Corollary 3 (improved number of ACTUAL endpoint-opposed full geodesics at EVERY root).** For any active NORI coloring and every root \(x\) in \(Q_n\), \(n\ge7\),
\[
\boxed{\#\mathcal B_x\ge 2(n-2).}
\tag{4}
\]
These are \(2(n-2)\) DISTINCT physical rooted full geodesics with opposite first/last ordered-face window colors. In a hypothetical grand counterexample, every one of these has at least three color changes.

**Proof.** The free involution on the finite vertex set of \(K_x\) partitions it into \(N=\#\mathcal B_x/2\) pairs \(\{\pi_i,\operatorname{rev}\pi_i\}\). Assign its paired vertices the vectors \(\pm e_i\) in \(\mathbb R^N\). No simplex contains both members of a pair, so on any simplex the PL extension of these signed-coordinate vertices has at most one signed unit vector in each coordinate: its convex combination is never zero. Normalize to give a continuous antipodally equivariant map \(K_x\to S^{N-1}\). Thus \(w_1(K_x/\tau)^N=0\). Theorem 2 gives its \((n-3)\)-rd power nonzero, forcing \(N>n-3\), or \(N\ge n-2\). Hence (4). \(\square\)

**The exact higher-dimensional extraction obligation.** The crucial improvement is that the topological carrier's vertices are **real endpoint-opposed full paths**, and its simplices mean those paths' coordinate orders lie in one common **proper face of the true permutohedron**, not convex hulls of imaginary geodesics. Under hypothetical grand failure every such vertex has an ODD number of changes \(\ge3\). If one can construct from this genuine order-face incidence a simplicial antipodal map \(K_x\to S^{n-4}\) using the internal switch positions, it will contradict (3) and force NORI closure. For a valid map, a cell's assigned labels must avoid zero in every simplex, with the actual face/order incidence checked. Counting switch positions alone is not an extension theorem. Fixed-root NORI strengthening is false, so a uniformly valid low-sphere map cannot arise merely from no-good paths at one fixed root without using actual cross-root face constraints (or else it would contradict known rooted counterexamples). The theorem isolates the high-index **physical path complex**, without claiming that its topology alone settles grand closure.

**Status:** Theorem 1–2 and Corollary 3 are all-dimensional proved consequences of the established 1-Lipschitz endpoint imbalance and odd PL zero-index theorem. They require neither affine-exterior dependence nor a low-dimensional classification.
