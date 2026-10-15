# Explicit higher coherences for every rank-two type-B Coxeter relation

# Higher coherences for all rank-two type-B Coxeter relations

Continue the antipodal cubical chains \(E_k(g)\) and the generator homotopies \(H_k(g,s)\) from Article XIV, Subsections 33–34. We prove that every rank-two Coxeter relation, including the four-braid involving the initial root, admits an explicit *homotopy of homotopies* in every rank. No assumptions on the edge-coloring class are made.

Let \(g=(x;d_0,\ldots,d_{n-1})\) be a complete geodesic flag. The generator \(s_0\) flips the initial root in dimension \(d_0\), and \(s_i\) for \(1\le i<n\) interchanges the dimensions in positions \(i-1,i\). Put \(N=1+\tau\). For a set \(U\) of dimension positions and a bit assignment \(q\) on its complement, write \([U;q]_x\) for the cubical face with free dimensions \(\{d_j:j\in U\}\) and fixed bits \(x_{d_j}+q(j)\).

For any two generators \(s,t\), let \(m=m(s,t)\) be their Coxeter exponent, which is \(2,3\), or \(4\). Traverse the relation polygon, a cycle of \(2m\) flag edges with alternating generators:
\[
g_0=g\xrightarrow{a_0}g_1\xrightarrow{a_1}\cdots
\xrightarrow{a_{2m-1}}g_{2m}=g,
\qquad a_j\in\{s,t\}.
\]
The corresponding degree-\((k+1)\) correction chain is
\[
B_k(g;s,t)=\sum_{j=0}^{2m-1}H_k(g_j,a_j).
\tag{1}
\]
The first-order homotopy identity from Subsection 34 implies
\[
\boxed{\partial B_k=NB_{k-1},}
\tag{2}
\]
since every \(E_k(g_j)\) appears twice when summed around a closed polygon.

## The four uniform formulas

Define a core set \(C\) of positions and a base bit function \(q_0\), using the following table. The variable \(r\) is the position at which the bit function is evaluated.

| Relation | Core \(C\) | \(q_0(r)\) outside \(C\) | Initial \(k_0\) |
|---|---|---|---|
| Four-braid \(s_0,s_1\) | \(\{0,1\}\) | \(0\) | \(0\) |
| Ordinary braid \(s_i,s_{i+1}\), \(i\ge1\) | \(\{i-1,i,i+1\}\) | \(\mathbf1_{\{r<i-1\}}\) | \(1\) |
| Root commuting \(s_0,s_j\), \(j\ge2\) | \(\{0,j-1,j\}\) | \(\mathbf1_{\{0<r<j-1\}}\) | \(1\) |
| Disjoint commuting \(s_i,s_j\), \(1\le i<j-1\) | \(\{i-1,i,j-1,j\}\) | \(\mathbf1_{\{i\le r<j-1\}}\) | \(2\) |

In all cases \(k_0=|C|-2\). For \(k_0\le k\le n-2\), define
\[
\boxed{
K_k(g;s,t)=
\sum_{\substack{R\subseteq\{0,\ldots,n-1\}\setminus C\\|R|=k-k_0}}
[C\cup R;q_R]_x,\qquad
q_R(r)=q_0(r)+|\{v\in R:v>r\}|\pmod2.
}
\tag{3}
\]
Set \(K_k=0\) outside that range. Each nonzero \(K_k\) is a \((k+2)\)-chain supported on
\[
\boxed{\binom{n-|C|}{k-k_0}}
\tag{4}
\]
cubical faces, one per admissible additional free dimension set \(R\).

**Theorem 1 (second-level Coxeter coherence in all ranks).** For every \(n\), every full geodesic flag \(g\), every rank-two type-B Coxeter relation and every \(0\le k\le n-1\),
\[
\boxed{
B_k(g;s,t)=\partial K_k(g;s,t)+N K_{k-1}(g;s,t).
}
\tag{5}
\]
Thus the root-flip and adjacent-swap homotopies satisfy the Coxeter braid and commuting identities *up to explicitly prescribed higher cubical chains*.

*Proof.* Separate the dimensions into the core \(C\) of the rank-two relation and all other, spectator, dimensions. When no spectator dimension is free, the relation gives one of four elementary cubical identities.

For the \(s_0,s_1\) four-braid, the four root-edge corrections \(H_0\) traverse the four edges bounding the square in dimensions \(d_0,d_1\), giving \(B_0=\partial K_0\).

For the ordinary braid \(s_i,s_{i+1}\), its six generator-swap square corrections \(H_1\) are the six two-faces bounding the three-cube on its three consecutive dimensions, giving \(B_1=\partial K_1\).

For root commuting \(s_0,s_j\), the root-edge corrections \(H_0\) cancel pairwise; its six noncancelling rank-one square corrections are the boundary of the three-cube on \(\{d_0,d_{j-1},d_j\}\), giving \(B_1=\partial K_1\).

For the commuting pair \(s_i,s_j\) with \(|i-j|\ge2\), the four rank-one corrections cancel in pairs; its eight surviving rank-two three-cube corrections bound the four-cube on \(\{d_{i-1},d_i,d_{j-1},d_j\}\), giving \(B_2=\partial K_2\).

For a fixed nonempty spectator set \(R\), every face of \([C\cup R;q_R]_x\) obtained by fixing a core dimension reproduces the appropriate remaining term in the generator-homotopy sum \(B_k\); the listed \(q_0\) offsets encode the portions of the complete geodesic traversed before the relation's core. The other boundary facets arise by fixing one \(r\in R\). Hold \(R'=R\setminus\{r\}\) fixed and sum over the possible \(r\). Those facets concatenate into a monotone path in the still-fixed spectator dimensions, traversed in increasing position order, whose two ends are \([C\cup R';q_{R'}]_x\) and its full antipodal mate. All intermediate facets cancel over \(\mathbb F_2\). The resulting boundary contribution is \(N K_{k-1}\). Summing over all \(R,R'\) establishes (5). \(\square\)

**Theorem 2 (top-rank location).** For \(k\le n-3\), every \(K_k\) consists of proper cube faces and lies on \(B_n=\partial[0,1]^n\). For \(k=n-2\) and every relation,
\[
\boxed{K_{n-2}(g;s,t)=Q_n,}
\quad\text{hence}\quad
\boxed{B_{n-2}+NK_{n-3}=[B_n].}
\tag{6}
\]
Here \([B_n]\) is the nonzero fundamental mod-two cycle of the cubical boundary sphere.

*Proof.* Each \(K_k\) has dimension \(k+2\). When \(k=n-2\), the only choice of \(R\) in (3) is the full complement of \(C\), so every dimension is free and the term is the full cube. Equation (6) follows from (5) and \(\partial Q_n=[B_n]\). \(\square\)

**Verification and scope.** Equations (3)–(5) were independently checked by explicitly expanding cubical boundaries on every rank-two type-B relation, with arbitrary dimension orders, for \(n\le7\). The proof uses the same cancellation in arbitrary dimension. The theorem constructs the complete set of **rank-two coherence fillers** for this uncolored chain resolution; it does not establish coherence on higher Coxeter residues or a color-compatible chain map. The root- and dimension-order constraints remain visible throughout, and no arbitrary graph-gallery class is introduced. The next step toward Wu–Yang is to lift these second-level homotopies through the monochromatic edge-incidence filtration, then analyze rank-three coherence.
