# Modular complementary resource flats and opposite-terminal path gluing

Let \(N\) be a finite loopless matroid of rank \(r\), let \(I_0\) be an independent set spanning the **anchor flat** \(F_0=\operatorname{cl}_N(I_0)\), and let \(B_1,B_2\) be independent resource sets containing \(I_0\). Put \(F_i=\operatorname{cl}_N(B_i)\).

**Theorem 1 (modular complementary-flat gluing).** If
\[
\boxed{
F_1\wedge F_2=F_0,\qquad
F_1\vee F_2=E(N),\qquad
r(F_1)+r(F_2)=r(F_0)+r(N),}
\tag{1}
\]
then
\[
\boxed{B_1\cap B_2=I_0,\qquad B_1\cup B_2\text{ is a basis of }N.}\tag{2}
\]
Conversely, if \(B_1\cap B_2=I_0\) and \(B_1\cup B_2\) is a basis, all three relations in (1) hold. Thus (1) characterizes pairs of **complementary modular flats over \(F_0\)** whose bases glue to one full resource basis.

*Proof.* Since \(B_i\) is independent and contains a basis \(I_0\) of \(F_0\), it cannot contain any further element of \(F_0\). A common element of \(B_1,B_2\) belongs to \(F_1\cap F_2=F_0\); hence their intersection is \(I_0\). The union therefore has cardinality
\[
|B_1\cup B_2|=r(F_1)+r(F_2)-r(F_0)=r(N).
\]
It spans \(F_1\vee F_2=E(N)\). A spanning set of size \(r(N)\) is a basis, proving (2).

Conversely, assume \(B_1\cap B_2=I_0\) and their union is a basis. Their closures jointly span \(N\), so \(F_1\vee F_2=E(N)\). The basis cardinality gives \(r(F_1)+r(F_2)-r(F_0)=r(N)\). By submodularity,
\[
r(F_1\cap F_2)\le r(F_1)+r(F_2)-r(F_1\vee F_2)=r(F_0).
\]
But \(F_0\subseteq F_1\cap F_2\), so their ranks agree; since both are flats, \(F_1\cap F_2=F_0\). All conditions in (1) follow. \(\square\)

**Theorem 2 (colored opposite-terminal gluing).** Suppose \(B_1,B_2\) arise from two same-colored coherent paths in a deck-reversal-odd path system, and their distinguished terminal states are opposite and compatible: reversing and deck-translating the second path can be concatenated with the first along the shared anchor, without introducing any additional turn. If their resource flats satisfy (1), the concatenated path uses a full basis of resources and has at most one color change.

*Proof.* The reversal-deck operation complements the colors of the second arm. By terminal compatibility the two arms concatenate into one coherent path, with no extra interior transition beyond their joining seam. Theorem 1 says their combined resource set, counting the anchor once, is a full independent basis. Each arm was monochromatic, and the transformed second arm has the opposite color, so the concatenation has at most one color change. \(\square\)

The compatibility hypothesis in Theorem 2 is essential: complementary matroid flats alone do not encode the order in which directed path states can be joined. The theorem isolates resource-basis gluing as a modular-flat property and forward coherence as a separate signed-cover condition.

**Corollary 4 (boundary graphic flats form a Boolean sublattice).** Fix an unordered pair {u,v} and put A=V without {u,v}. Among flats of the graphic matroid M(K_V), consider only F_S=E(K_{S union {u,v}}), for S subset A. They are a Boolean sublattice: F_S meet F_T=F_(S intersect T), F_S join F_T=F_(S union T), with rank r(F_S)=|S|+1. Every pair is modular. The flat F_empty is the common anchor edge {u,v}, and F_A is the full resource flat. Therefore two terminal arms have complementary modular flats if and only if their sets of visited vertices outside {u,v} are complementary subsets of A.

**Theorem 5 (opposite-terminal complementary-family criterion).** For an ordinary reversal-odd boundary 3-tournament on \(V\), fix distinct \(u,v\) and a color \(\varepsilon\). Put \(A=V\setminus\{u,v\}\), and define
\[
\mathcal R^\varepsilon_{uv}
=\{S\subseteq A:\text{there is a vertex-simple monochromatic }\varepsilon
\text{ tight path ending at }(u,v)
\text{ whose vertex set is }S\cup\{u,v\}\}.
\tag{4}
\]
The vacuous two-vertex path is allowed. Then the boundary tournament has a spanning tight path with at most one internal color change if and only if
\[
\boxed{
\exists u\ne v,\ \varepsilon,\ S\subseteq A:
S\in\mathcal R^\varepsilon_{uv},\quad
A\setminus S\in\mathcal R^\varepsilon_{vu}.}
\tag{5}
\]
Consequently, if the spanning one-turn conjecture fails for a coloring, then for every unordered pair \(\{u,v\}\) and both colors \(\varepsilon\),
\[
\boxed{
|\mathcal R^\varepsilon_{uv}|+
|\mathcal R^\varepsilon_{vu}|\le2^{n-2}.}\tag{6}
\]

*Proof.* The resource footprints of the two paths in (5) have original vertex sets meeting only at \(u,v\) and covering \(V\). Their terminal ordered pairs are opposite and their triple colors coincide. The opposite-terminal packing theorem in Article XI (or Theorem 2 above) joins them into a vertex-simple spanning path with at most one color change. Conversely, any such path splits at its color-change seam into two same-colored terminal arms after reversal of the suffix; for a monochromatic word take one arm to be the vacuous two-vertex path. Their outside vertex sets are complementary, proving (5). In the absence of any such witness, \(\mathcal R^\varepsilon_{uv}\) and the complement image \(\{A\setminus T:T\in\mathcal R^\varepsilon_{vu}\}\) are disjoint subsets of \(2^A\). Since complementation is a bijection, their cardinalities sum to at most \(2^{|A|}=2^{n-2}\). \(\square\)

**Comparison with the cube.** In the free-matroid cube automaton, NORI1 is equivalent to a complementary pair inside one rooted color-zero reachable family \(R_x\subseteq2^{[n]}\); failure imposes \(|R_x|\le2^{n-1}\) for every root. In the boundary system the same Boolean-complement obstruction acts *between* the two opposite-terminal families \(\mathcal R^\varepsilon_{uv}\) and \(\mathcal R^\varepsilon_{vu}\). The shared proposed proof principle is therefore a **complementary reachable-flat intersection theorem** for compatible monochromatic arms, rather than an unrestricted short-cocircuit intersection theorem. The counting bounds are necessary conditions for failure, not proofs that failure is impossible.
