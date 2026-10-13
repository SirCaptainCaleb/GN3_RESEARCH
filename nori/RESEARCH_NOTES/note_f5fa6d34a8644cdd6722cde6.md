# Multiplicity and permutation-order richness of half-spanning monochromatic cube geodesics

- Stable ID: note_f5fa6d34a8644cdd6722cde6
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: cube, leader-long, density, multiplicity, monochromatic-geodesics
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_6
- Updated session: session_nori_r7130_6
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Theorem (exponentially many half-spanning monochromatic geodesics).** Let \(n\ge2\), \(N=2^n\), and let \(c:E(Q_n)\to\{0,1\}\) be any binary coloring of undirected cube edges. Fix **any** permutation \(\pi\) of the \(n\) coordinate directions. Put \(h=\lceil n/2\rceil\). Then there exists a color \(s\) such that at least
\[
\boxed{
A_n=
\begin{cases}
\left\lceil {2N}/{(n+2)}\right\rceil,&n\text{ even},\\[2pt]
\left\lceil N/{(n+1)}\right\rceil,&n\text{ odd}
\end{cases}
}\tag{1}
\]
distinct terminal vertices \(x\in Q_n\) admit a monochromatic color-\(s\) geodesic of length at least \(h\), whose edge-coordinate sequence is a subsequence of \(\pi\) (so no coordinate is repeated). In particular, any coloring has at least \(A_n=\Omega(2^n/n)\) oriented color-monochromatic geodesics of length at least \(h\), with pairwise distinct chosen terminal vertices. If the coloring is antipodally odd, (1) holds **separately for each color**.

*Proof.* Take a color \(s\) and let \(H_s\) be its spanning edge subgraph. For a fixed order \(\pi=(i_1,\ldots,i_n)\), let \(L_j^s(x)\) be the greatest number of edges in a color-\(s\) geodesic ending at \(x\) whose coordinate directions form a subsequence of \((i_1,\ldots,i_j)\). In particular \(L_0^s(x)=0\) and \(0\le L_n^s(x)\le n\). At stage \(j\), each \(i_j\)-coordinate pair of vertices \(x,y=x\oplus e_{i_j}\) has the same previously considered coordinate sets. If \(xy\notin E(H_s)\), retain the two previous terminal labels. If \(xy\in E(H_s)\), update
\[
L_j^s(x)=\max\{L_{j-1}^s(x),\,L_{j-1}^s(y)+1\},\qquad
L_j^s(y)=\max\{L_{j-1}^s(y),\,L_{j-1}^s(x)+1\}.
\]
For all real \(a,b\),
\[
\max\{a,b+1\}+\max\{b,a+1\}\ge a+b+2.
\]
Consequently summing over all coordinate-\(i_j\) pairs and all stages gives
\[
\sum_{x\in Q_n}L_n^s(x)\ge2|E(H_s)|.\tag{2}
\]
Choose the majority color, with \(|E(H_s)|\ge|E(Q_n)|/2=nN/4\). Then \(\sum_x L_n^s(x)\ge nN/2\). Let \(A\) be the number of terminals with \(L_n^s(x)\ge h\). Each of the other \(N-A\) terminals has label at most \(h-1\), and every terminal has label at most \(n\). Hence
\[
\frac{nN}{2}\le\sum_xL_n^s(x)
\le (N-A)(h-1)+An,
\]
giving
\[
A\ge \frac{N(n/2-h+1)}{n-h+1}.
\]
If \(n=2m\), this is \(N/(m+1)=2N/(n+2)\); if \(n=2m+1\), this is \(N/[2(m+1)]=N/(n+1)\). Integrality gives (1). Distinct terminals yield distinct oriented witnesses by selecting a maximal path for each counted terminal.

For an antipodally odd edge coloring, antipodal complementation bijects the edges of the two colors, so \(|E(H_0)|=|E(H_1)|=nN/4\). Apply the same proof to either color independently. \(\square\)

**Relation to the published manuscript and literature.** The key aggregate inequality (2) is the cube specialization of Article XI, Subsection \`weighted_detour_gluing_and_matroidal_hamming_density\`, Theorem 5, which recovers Leader–Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29–33 (arXiv:1301.2195). Its stated Corollary 6 asserts the existence of a monochromatic geodesic of length at least \(\lceil n/2\rceil\); the present elementary counting consequence strengthens the statement to exponentially many terminally distinguished geodesics for every fixed factor ordering. The bounds (1) are not asserted to be optimal.

## Sharp ordered-direction richness for arbitrary cube subgraphs

**Theorem.** Let \(H\subseteq Q_n\) be an edge-subgraph on \(N=2^n\) vertices, average degree \(d=2|E(H)|/N\), and \(h=\lceil d\rceil\ge1\). Define \(\mathcal W_h(H)\) as the set of ordered \(h\)-tuples of distinct coordinate directions realized by directed \(h\)-edge geodesics in \(H\). Then **every permutation of all \(n\) directions contains a member of \(\mathcal W_h(H)\) as a subsequence**, and
\[
\boxed{|\mathcal W_h(H)|\ge h!.}\tag{O}
\]

*Proof.* Fix an arbitrary permutation \(\pi\) of the coordinate directions. The factor-ordered dynamic program from the preceding theorem provides terminal values \(L_n(x)\) with \(\sum_x L_n(x)\ge2|E(H)|=dN\), so some terminal has a witnessing coordinate-distinct path of length at least \(h\), whose direction word is a subsequence of \(\pi\). Take its last \(h\) edges to obtain a word in \(\mathcal W_h(H)\) contained in \(\pi\). This applies to every \(\pi\). Each fixed \(h\)-word of pairwise distinct directions occurs as a subsequence of precisely \(n!/h!\) full permutations. Covering all \(n!\) permutations thus requires \(|\mathcal W_h(H)|\ge h!\). \(\square\)

**Two-colored consequence.** In every binary edge coloring of \(Q_n\), put \(h=\lceil n/2\rceil\). A fixed majority edge color supports at least \(h!\) distinct relative direction words of monochromatic \(h\)-edge geodesics, and its word family hits *every* full coordinate permutation by subsequences. For antipodally odd colorings the theorem applies **separately to each color**, since both color subgraphs have average degree \(n/2\).

**Sharpness.** For a prescribed \(h\)-element coordinate set \(S\), let \(H\) contain every cube edge in the directions \(S\) and no others. Its average degree is \(h\), and its length-\(h\) path words consist of the \(h!\) permutations of \(S\). This also gives equality for the majority color of an arbitrary 2-edge coloring when \(h=\lceil n/2\rceil\). The example is not antipodally odd, so support-richness beyond the factorial word count remains a research direction in NORI1.

**Distinct oriented path multiplicity.** The preceding theorem supplies \(A_n\) terminal vertices for each permutation, where \(A_n=\lceil2N/(n+2)\rceil\) for even \(n\) and \(A_n=\lceil N/(n+1)\rceil\) for odd \(n\). Select one \(h\)-edge suffix for every such permutation-terminal pair. Every fixed oriented \(h\)-edge geodesic fits at most \(n!/h!\) full coordinate orders. Double-counting proves there are at least \(A_nh!\) distinct directed geodesic instances in the majority color, and in each color under antipodal oddness.

**Limitation.** Many relative orders do not necessarily imply many different coordinate supports: the sharpness example uses one fixed support \(S\). Exploiting polarity to force support diversity or complementary-root compatibility remains the key challenge for NORI1.
