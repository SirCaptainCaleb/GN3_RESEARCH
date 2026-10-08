# Canonical shared-wall gauges force a dominance cut among blocked vertices

## Composition

# Canonical wall normalization and blocker dominance

Let \(T\) be a tournament, let \(t(u,v)=1\) mean \(u\to v\), and put \(\alpha(u,v,w)=t(u,v)\oplus t(v,w)\oplus t(w,u)\). Switching a vertex reverses all its incident edges and preserves \(\alpha\). An \(\alpha\)-zero order \(C=(c_1,\ldots,c_m)\) is **compatible** when its first and last ordered pairs point forward in the fixed tournament. Assume \(C\) is support-maximal among compatible zero orders containing the designated special vertices.

There is a unique switching of the vertices of \(C\), up to simultaneously complementing all switching bits, making each \(c_j\to c_{j+1}\). The zero equations then imply \(c_j\to c_{j+2}\). Fix an internal gap \(c_i\mid c_{i+1}\) with \(2\le i\le m-2\). Each omitted vertex \(v\) for which \(\alpha(c_i,v,c_{i+1})=0\) has a unique switching state satisfying \(c_i\to v\to c_{i+1}\). Switch **all eligible vertices simultaneously** to their respective states. Let \(W_i\) be the set of eligible vertices and define
\[
L_i=\{v\in W_i:c_{i-1}\to v\},\qquad
R_i=\{v\in W_i:v\to c_{i+2}\}.
\]

**Theorem (wall-dominance).** \(L_i\cap R_i=\varnothing\), and every vertex of \(R_i\) dominates every vertex of \(L_i\) in this jointly wall-normalized tournament.

**Proof.** Any \(v\in L_i\cap R_i\) satisfies all four distance-one/two incidences necessary to insert \(v\) at the internal gap. The resulting directed square-path remains compatible and grows support, contradicting maximality. For \(a\in L_i\), \(b\in R_i\), the proposed block insertion
\[
(\ldots,c_{i-1},c_i,a,b,c_{i+1},c_{i+2},\ldots)
\]
satisfies the six exterior required incidences
\[
c_{i-1}\to a,\quad c_i\to a,\quad c_i\to b,\quad
a\to c_{i+1},\quad b\to c_{i+1},\quad b\to c_{i+2}.
\]
Its only additional required edge is \(a\to b\). Maximality forbids this support-increasing insertion, hence \(b\to a\). Reversing every connector switching bit forces each omitted vertex's canonical wall switching bit to reverse as well, leaving the mutual orientations of omitted vertices unchanged. \(\square\)

**Corollary (two-sided obstruction).** For \(a\in L_i\) and \(b\in R_i\), their incidence words \((t(c_{i-1},v),t(c_i,v),t(c_{i+1},v),t(c_{i+2},v))\) are \(1101\) and \(0100\), respectively. The block \(a,b\) fails at its mutual orientation \(a\to b\); the reverse block \(b,a\) fails at both \(c_{i-1}\to b\) and \(a\to c_{i+2}\). The induced bipartite orientation is a homogeneous cut \(R_i\to L_i\) **in this wall gauge**.

**Corollary (cross-wall parity).** Fix a path-normalizing gauge on \(C\) and arbitrary initial switching states of omitted vertices. Write \(u_k(v)=t(c_k,v)\). For any gap \(k\) where \(a,b\) lie in opposite thickness classes, define \(\varepsilon_k(a,b)=0\) when \(a\in L_k,b\in R_k\), and \(1\) for the opposite assignment. Switching a vertex \(v\) into the down-wall state at \(k\) uses bit \(1\oplus u_k(v)\). Accordingly,
\[
\varepsilon_k(a,b)=t(a,b)\oplus u_k(a)\oplus u_k(b).
\]
For two such gaps \(i,j\),
\[
\varepsilon_i(a,b)\oplus\varepsilon_j(a,b)
=u_i(a)\oplus u_i(b)\oplus u_j(a)\oplus u_j(b).
\]
An opposite-thickness pair at wall \(i\) cannot simultaneously be opposite-thickness at walls \(i-1\) or \(i+1\). If it recurs at wall \(i+2\), its roles are reversed. Indeed its incidence words at \(i\) agree, while those at \(i+2\) disagree.

**Scope and closure frontier.** This repairs the shared-wall normalization gap in the earlier conditional blocker claim and imposes an orientation and parity constraint on the state space of support-maximal connectors. The missing step is a legal support-increasing exchange, or a well-founded reversible repair path, preserving both endpoint ports across several such walls. The parity constraint alone does not provide that exchange.

## Development

Fix a monochromatic-zero connector C=(c_1,...,c_m) in the flat tournament split, with both exposed endpoint pairs forward. Switch its vertices to the path-normalized gauge in which c_j→c_{j+1} and c_j→c_{j+2} whenever defined. Fix an internal gap c_i|c_{i+1}, 2≤i≤m−2. For each omitted vertex a with α(c_i,a,c_{i+1})=0, there is a unique switching state of a for which c_i→a→c_{i+1}. Define L_i and R_i by the left and right outer incidences c_{i−1}→a and a→c_{i+2}, respectively. The main result proves that in a support-maximal connector L_i and R_i are disjoint, and all edges between them point R_i→L_i in these jointly chosen wall-normalized switching states. This replaces the earlier unsupported claim that opposite thicknesses can never coexist. They may coexist, but then their mutual orientations are forced. The corollary identifies the two-sided adjacent-collar obstruction to either two-vertex ordering.
