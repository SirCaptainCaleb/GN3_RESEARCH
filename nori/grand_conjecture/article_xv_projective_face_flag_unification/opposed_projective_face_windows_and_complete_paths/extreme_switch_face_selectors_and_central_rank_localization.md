# Extreme-switch face selectors and central-rank localization

# Extreme-switch selectors and central-rank localization

Let \(P\) be a simple \(d\)-polytope, \(d\ge3\), and \(K\) the order complex of its proper nonempty faces. Then \(K\cong S^{d-1}\). Let \(X\) be its dual cell complex; its vertices are maximal face flags \(g=(F_0\subset\cdots\subset F_{d-1})\), and a dual edge of rank \(i\) exchanges \(F_i\). Write \(G=K^{(1)}\), the graph joining every comparable pair of proper faces.

Suppose \(g\) carries a binary complete-path word \(w(g)=(w_1,\ldots,w_m)\) with at least two switches. Let a free simplicial opposition \(J\) on \(K\) transform the words by complementation, either in place or after reversal. Require **rank coherence**: \(J\) carries the rank-\(j\) face in the flag to the rank assigned to switch position \(j\) after the word opposition. For the cube with edge windows, \(m=d\), both index maps are identity; for the simplex with ordered triple windows, \(m=d-1\), both send \(j\mapsto d-1-j\). This is a structural compatibility property, not an assumption that every arbitrary opposed polytope automatically satisfies it.

**Theorem 1 (an antipodal graph-valued selector).** Let \(a(g)\) and \(b(g)\) be the first and last switch indices of \(w(g)\). Then
\[
\boxed{L(g)=\operatorname{midpoint}\,[F_{a(g)},F_{b(g)}]\in G}
\tag{1}
\]
is well defined and satisfies \(L(Jg)=JL(g)\).

*Proof.* The indices are distinct and lie between \(1\) and \(m-1\), so the corresponding proper faces are nested and span an edge of \(K\). Complementation preserves every switch position; complemented reversal sends position \(j\) to \(m-j\) and exchanges the first and last switches. Rank coherence makes the unordered pair of chosen faces transform by \(J\), proving equivariance. For the simplex this holds even when the two opposed flags have identical binary words: their selected face vertices differ. \(\square\)

Choose a \(J\)-stable set \(R\) consisting of one central face rank, or two adjacent central ranks. For cubes, any one rank is stable. For simplices with \(d\) odd, choose \(R=\{(d-1)/2\}\); for simplices with \(d\) even, choose \(R=\{d/2-1,d/2\}\). Associate to each flag its *anchor* \(A(g)\in G\): the vertex \(F_r\) if \(R=\{r\}\), or the midpoint of \([F_r,F_{r+1}]\) if \(R=\{r,r+1\}\). Then \(A(Jg)=JA(g)\).

Let \(X_{\neg R}\) comprise all closed dual cells whose variable face ranks avoid \(R\). It is an opposition-invariant subcomplex, and every flag incident with one of its cells has the same anchor.

**Theorem 2 (equivariant anchored extension).** The selector (1) extends continuously and equivariantly to
\[
\boxed{L_R:X_{\neg R}\longrightarrow G.}
\tag{2}
\]

*Proof.* For each maximal flag \(g\), choose a path \(\gamma_g\) in \(G\) from \(L(g)\) to \(A(g)\), entirely inside the one-skeleton of the maximal simplex of \(K\) represented by \(g\). Such a path exists because all of the flag's proper faces are nested and pairwise adjacent in \(G\). Since opposition freely permutes maximal flags, choose paths on one representative of each antipodal pair and impose \(\gamma_{Jg}=J\gamma_g\).

For a directed dual edge \(g\to h\) changing a rank outside \(R\), the anchor is unchanged: \(A(g)=A(h)\). Define the image of the edge as \(\gamma_g\gamma_h^{-1}\). This is a path joining the prescribed vertex labels and is equivariant. Around a dual two-cell avoiding \(R\), these paths concatenate as \(\gamma_{g_0}\gamma_{g_1}^{-1}\gamma_{g_1}\gamma_{g_2}^{-1}\cdots\gamma_{g_q}\gamma_{g_0}^{-1}\), which freely reduces to the empty path. Hence the boundary admits a filling in the graph. Choose compatible fillings over antipodal cell pairs. For cells of dimension at least three, the higher homotopy groups of a graph vanish, allowing extension over each further cell, again in antipodal pairs. \(\square\)

**Theorem 3 (the unfilled cells must carry a topological obstruction).** No equivariant map from the full two-skeleton \(X^{(2)}\) to \(G\) exists. Hence, starting from (2), the only remaining obstruction to a full graph-valued map lies among dual edges and two-cells involving at least one rank in \(R\).

*Proof.* The covering class \(\alpha\in H^1(X/J;\mathbb F_2)\) of the free involution on the sphere satisfies \(\alpha^2\ne0\), also on the quotient two-skeleton. An equivariant map \(X^{(2)}\to G\) would induce a map into the one-dimensional quotient graph \(G/J\) that pulls back its covering class to \(\alpha\). The square of the class on \(G/J\) vanishes because the graph has no second cohomology. This contradicts \(\alpha^2\ne0\). \(\square\)

**Status.** Theorems 1–3 are unconditional structural statements once every flag has two switches. They apply to unrestricted NORI1 cube-edge colorings and unrestricted reversal-odd boundary tournaments. They do not establish a one-switch witness: central-rank exchange cells remain unfilled. The new proof target is to exploit the common projective-incidence descent to rule out the required central-rank obstruction under a hypothetical absence of favorable complete paths. Unlike the signed-second-switch method, this approach has a **one-dimensional equivariant target** and reduces the first obstruction to **rank-two residues in every ambient dimension**.
