## Matroidal Reachability and Long-Path Bounds

Fix an antipodally odd binary edge coloring \(c\) of \(Q_n\), a root \(x\), and identify the directed resource-flat automaton with the Boolean lattice \(2^{[n]}\). Write \(\bar S=[n]\setminus S\). For the rooted edge \(S\to S\cup\{i\}\), deck oddness takes the form
\[
c_x(S,S+i)=1-c_x(\overline{S+i},\bar S).
\tag{1}
\]
Let \(U\subseteq2^{[n]}\) contain \(\varnothing\), avoid complementary pairs, and be forward-closed under color-zero arcs. Such a family is the dual reachability-cut certificate from the preceding flat-automaton Subsection.

**Theorem 1 (antipodal frontier separation).** No directed Boolean-lattice edge runs from \(U\) to its antipodal image \(\bar U=\{\bar T:T\in U\}\). Equivalently, there do not exist \(S,T\in U\) such that
\[
\boxed{S\cap T=\varnothing,\qquad |S|+|T|=n-1.}\tag{2}
\]

*Proof.* Suppose \(S\in U\) and \(S+i=\bar T\in\bar U\), with \(i\notin S\). Since \(U\cap\bar U=\varnothing\), this edge leaves \(U\), so its color is one. Reflection under complementation reverses this directed Boolean edge, producing
\[
T=\overline{S+i}\longrightarrow\bar S.
\]
Its initial point \(T\) lies in \(U\), while its terminal point \(\bar S\) lies in \(\bar U\), hence it also leaves \(U\) and must have color one. But the two reflected cube edges are antipodal and must have opposite colors by (1). Contradiction. A directed edge \(S\to\bar T\) exists if and only if \(S\cap T=\varnothing\) and \(|S|+|T|=n-1\), proving the equivalence. \(\square\)

**Theorem 2 (cross-level Hall inequalities).** Put \(U_s=U\cap\binom{[n]}s\). If \(s+t=n-1\) with \(s\ne t\), then
\[
\boxed{\frac{|U_s|}{\binom ns}+
\frac{|U_t|}{\binom nt}\le1.}\tag{3}
\]
In particular, since \(U_0=\{\varnothing\}\), it follows that \(U_{n-1}=\varnothing\).

*Proof.* Consider the bipartite disjointness graph between all \(s\)-subsets and all \(t\)-subsets. It is biregular: each \(s\)-set has \(n-s=t+1\) disjoint \(t\)-neighbors, and each \(t\)-set has \(n-t=s+1\) disjoint \(s\)-neighbors. Theorem 1 says that every neighbor of a member of \(U_s\) lies outside \(U_t\). Counting these edges by their two ends gives
\[
(t+1)|U_s|\le(s+1)(\binom nt-|U_t|).
\]
Use \((t+1)\binom ns=(s+1)\binom nt\) to obtain (3). Taking \(s=0,t=n-1\) proves the final statement. \(\square\)

**Corollary 3 (odd-dimensional Erdős–Ko–Rado obstruction).** For \(n=2k+1\), \(k\ge1\), the reachable middle family \(U_k\) is pairwise intersecting. Consequently,
\[
\boxed{|U_k|\le\binom{2k}{k-1}.}\tag{4}
\]
For \(k\ge2\), equality in the Erdős–Ko–Rado inequality forces \(U_k\) to be a full star (all \(k\)-subsets containing one distinguished coordinate).

*Proof.* Two disjoint \(k\)-sets would violate (2), since \(2k=n-1\). Apply the classical Erdős–Ko–Rado theorem to the intersecting \(k\)-uniform family on \(2k+1>2k\) elements. Its equality characterization for \(k\ge2\) gives the star structure. \(\square\)

**Consequence for NORI1.** In a hypothetical counterexample, the true color-zero reachable set \(R_x\) meets the hypotheses for every cube root \(x\). Thus (2)–(4) impose additional cross-rank constraints simultaneously on all rooted reachability families. The inequalities apply only under the complement-free hypothesis: colorings with a monochromatic full geodesic may violate them. They strengthen the SAT counterexample certificate, but do not independently prove that the certificate is impossible.

**Corollary 4 (near-complete monochromatic geodesics suffice).** For any \(n\ge3\), the following statements are equivalent under antipodally odd undirected cube-edge coloring:

(i) there exists a monochromatic full antipodal \(n\)-edge geodesic;

(ii) there exists a monochromatic geodesic of \(n-1\) edges, using all but one coordinate direction;

(iii) some rooted color-zero resource reachability family contains a subset of cardinality \(n-1\).

*Proof.* (i) implies (ii) by truncation. To see (ii) implies (i), take its two endpoints \(a,b\), which differ in all directions except \(j\). Appending the edge in direction \(j\) from either end gives an antipodal \(n\)-edge geodesic. These two extension edges are antipodal translates of one another and therefore have opposite colors. One of them has the color of the original \((n-1)\)-edge path, yielding a monochromatic full geodesic. For (iii), a rooted color-zero path using \(n-1\) resources is such a geodesic; conversely any monochromatic \((n-1)\)-edge geodesic can be deck-translated if needed to give a color-zero witness. \(\square\)

This shows that, in the free-coordinate matroid model, it would already suffice to force rank \(n-1\) in the color-zero flat automaton for **one** root, rather than force two complementary reachable flats directly. In a hypothetical counterexample, the accessible rank of every rooted color-zero automaton is at most \(n-2\), consistent with the conclusion \(U_{n-1}=\varnothing\) of Theorem 2.

**Corollary 5 (cross-level SAT strengthening).** The factorial-free counterexample SAT formulation in the flat-automaton Subsection can be strengthened, without changing satisfiability, by adding binary clauses
\[
\boxed{\neg r_{x,S}\vee\neg r_{x,T}
\quad\text{for every root }x,\ S\cap T=\varnothing,\ 
|S|+|T|=n-1.}\tag{5}
\]
These clauses are logical consequences of the original color-edge closure, antipodal oddness, and complementary exclusion constraints. In particular the clauses \(r_{x,\varnothing}\) force all membership variables \(r_{x,T}\) of cardinality \(n-1\) to be false.

*Proof.* Any satisfying assignment defines a complement-free outward color-zero-closed family \(U_x=\{S:r_{x,S}=1\}\). Apply Theorem 1 separately to each root. \(\square\)

For odd \(n=2k+1\), the clause family includes disjointness constraints between all reachable \(k\)-sets. By Corollary 3 these induce the Erdős–Ko–Rado bound \( |U_{x,k}|\le\binom{2k}{k-1}\). This gives a small, intrinsic collection of resource-level constraints that can be propagated by SAT or cutting-plane solvers. No large-dimensional conclusion is inferred from solver timeouts.

**Corollary 6 (Hilton–Milner stability of a hypothetical counterexample).** Suppose \(n=2k+1\) with \(k\ge2\), and suppose the antipodally odd coloring has no monochromatic antipodal geodesic. Then at every root \(x\), the middle-level reachable family
\[
\mathcal F_x=R_x\cap\binom{[n]}k
\]
obeys the following alternative:
\[
\boxed{
\bigcap_{S\in\mathcal F_x}S\ne\varnothing
\quad\text{or}\quad
|\mathcal F_x|\le\binom{2k}{k-1}-k+1.}
\tag{6}
\]
In particular, for \(Q_7\), if a counterexample had at least fourteen reachable triples at some root, all those triples would necessarily contain one common coordinate. If it had fifteen, they would form a full star on that coordinate.

*Proof.* By Corollary 3, \(\mathcal F_x\) is an intersecting \(k\)-uniform family on \(2k+1\) elements. If its total intersection is empty, the classical Hilton–Milner stability theorem for nontrivial intersecting families bounds its size by
\[
\binom{n-1}{k-1}-\binom{n-k-1}{k-1}+1
=\binom{2k}{k-1}-k+1.
\]
Otherwise it has a shared coordinate. The \(Q_7\) thresholds are \(15-3+1=13\) and the EKR maximum \(15\). \(\square\)

**Prospective proof route.** The missing global step can be sharpened to a root-coupling problem: if a hypothetical counterexample has many reachable rank-\(k\) flats, their common coordinate is nearly forced. One could seek a contradiction between the resulting root-dependent central-coordinate assignments, reversal symmetry, and the composition law
\[
S\in R_x,\quad T\in R_{x+\mathbf1_S},\quad S\cap T=\varnothing
\Longrightarrow S\cup T\in R_x.
\]
Theorem 1 and the Hilton–Milner bound are unconditional restrictions on the hypothetical counterexample, but do not establish the needed global counting lower bound.

### Common-terminal monochromatic arm bases and rooted Boolean complement intersection

The spanning at-most-one-turn conjecture for ordinary reversal-odd boundary 3-tournaments has a simpler equivalent form than opposite-ordered-pair terminal packing. It asks for two same-colored tight paths ending at the **same original vertex**, using complementary sets of other vertices. Their union is a basis of a doubled graphic matroid. No matching penultimate ordered pairs or prescribed bridging-triple color is required.

Fix a reversal-odd boundary coloring \(b(a,v,c)\in\mathbb F_2\) on a set \(V\) of order \(n\ge3\). Admit one-vertex and two-vertex tight paths as vacuously monochromatic in either color.

**Theorem 1 (single-terminal two-arm characterization).** The following assertions are equivalent:

(i) Some injective ordering \(W\) of all \(V\) has at most one change among its successive ordered-triple colors.

(ii) There are a vertex \(v\), a color \(\varepsilon\), and two vertex-simple \(\varepsilon\)-monochromatic tight paths \(P,Q\), **both ending at \(v\)**, with
\[
\boxed{V(P)\cap V(Q)=\{v\},\qquad V(P)\cup V(Q)=V.}
\tag{1}
\]

*Proof.* For (ii), write \(P=(p_1,\ldots,p_r,v)\), \(Q=(q_1,\ldots,q_s,v)\) and concatenate
\[
W=(p_1,\ldots,p_r,v,q_s,\ldots,q_1).
\]
This word is injective and spanning. All triples wholly inside \(P\) have color \(\varepsilon\), and all triples wholly inside the reverse of \(Q\) have color \(1-\varepsilon\). There is only one additional junction triple \((p_r,v,q_s)\), which has one of those two colors. Thus the full color word has at most one change. If either arm is a single vertex, the concatenation is the other monochromatic path.

Conversely, if the one change of \(W=(w_1,\ldots,w_n)\) occurs between its triple windows starting at indices \(i\) and \(i+1\), take \(v=w_{i+2}\), let \(P=(w_1,\ldots,w_{i+2})\), and take \(Q=(w_n,\ldots,w_{i+2})\), the reverse of the suffix beginning at \(v\). If the initial triple color is \(\varepsilon\), then \(P\) has all triple colors \(\varepsilon\), whereas the original suffix has triple colors \(1-\varepsilon\); reversal makes all triples of \(Q\) color \(\varepsilon\). Their vertex sets partition \(V\) around \(v\). The alternative pivot \(v=w_{i+1}\) works as well, giving **two adjacent seam-pivot choices**. If \(W\) is monochromatic, take \(P=W\) and \(Q=(w_n)\). \(\square\)

#### Parallel-extension graphic matroid

Let \(2K_n\) be the multigraph obtained by duplicating every edge of \(K_n\), giving each original edge a \(P\)-copy and a \(Q\)-copy, and let
\[
\boxed{\mathsf R_n^{(2)}=M(2K_n).}
\tag{2}
\]
For a path \(P\), write \(E_P(P)\) for its consecutive-original-vertex edges in the \(P\)-copy, and similarly \(E_Q(Q)\).

**Theorem 2 (rooted two-arm basis-packing equivalence).** If \(P,Q\) are vertex-simple tight words ending at the same original vertex \(v\), then
\[
\boxed{
E_P(P)\cup E_Q(Q)\in\mathcal I(\mathsf R_n^{(2)})
\iff
V(P)\cap V(Q)=\{v\}.
}
\tag{3}
\]
Such a union is a basis if and only if the two arms also cover \(V\). Hence the spanning one-turn conjecture is equivalent to the existence of a **same-color common-terminal arm pair whose union is a basis of the rank-\((n-1)\) graphic matroid \(\mathsf R_n^{(2)}\)**.

*Proof.* Each arm is a simple graph path. If their vertex sets meet only at \(v\), their doubled-edge union is a tree. Otherwise the two paths from \(v\) to any other common vertex form a graphic cycle, with doubled shared edges contributing two-element parallel cycles when necessary. Thus graphic independence is equivalent to intersection only at \(v\). An independent connected graph whose arms cover all \(n\) vertices has \(n-1\) edges, hence is a graphic-matroid basis; conversely a graphic basis requires all \(n\) vertices. Apply Theorem 1. \(\square\)

The parallel copies matter: in the simple graphic matroid \(M(K_n)\), two identical suffix edges collapse set-theoretically and might falsely appear independent. In \(M(2K_n)\) their repetition is a graphic two-cycle, so the basis condition alone enforces disjointness away from the root.

#### Rooted Boolean-lattice complement formulation

For each \(v\in V\) and color \(\varepsilon\), define
\[
\boxed{
\mathcal A_v^\varepsilon=
\{S\subseteq V\setminus\{v\}:
\exists\text{ an injective }\varepsilon\text{-monochromatic tight word}\\
\text{on }S\cup\{v\}\text{ ending at }v\}.
}
\tag{4}
\]
The singleton path \((v)\) witnesses the empty set, and all singleton subsets are witnessed by two-vertex paths. The complete family is the union of reachability states from the ordered-terminal resource automaton after forgetting the penultimate vertex.

**Theorem 3 (rooted complementary reachability).** A boundary tournament has a spanning at-most-one-turn tight path if and only if
\[
\boxed{
\exists\,v\in V,\ \varepsilon\in\mathbb F_2,\ S\subseteq V\setminus\{v\}:
\quad
S,\ (V\setminus\{v\})\setminus S\in\mathcal A_v^\varepsilon.
}
\tag{5}
\]

*Proof.* Two complementary reachable subsets give two same-color arms ending at \(v\) whose only shared original vertex is \(v\), and their union covers \(V\). Theorem 1 glues them into a one-turn spanning word. Conversely the two-arm decomposition in Theorem 1 yields precisely these complementary resource subsets. \(\square\)

**Corollary 4 (a sufficient rooted-majority criterion).** If some \(v,\varepsilon\) satisfies
\[
\boxed{|\mathcal A_v^\varepsilon|>2^{n-2},}
\tag{6}
\]
then a spanning one-turn tight path exists, by pigeonholing the \(2^{n-1}\) subsets into \(2^{n-2}\) complementary pairs. This inequality is a proposed proof route, **not** an established universal lower bound.

#### Unification with NORI1

The cube's free-resource automaton already gives rooted color-zero reachability families \(R_x\subseteq2^{[n]}\), and Article XI proves NORI1 equivalent to the existence of a root \(x\) for which
\[
\boxed{\exists S:\quad S,\ [n]\setminus S\in R_x.}
\tag{7}
\]
Theorem 3 now places the ordinary boundary spanning one-turn conjecture in **the identical formal rooted complement-pair template**, but on original-vertex subsets \(V\setminus\{v\}\). The resource independence of two boundary arms is captured by the parallel-extension graphic matroid \(\mathsf R_n^{(2)}\), while cube coordinate resource independence is captured by the free matroid. This removes the two-vertex seam-matching constraint from the boundary selector and makes the common open question precise: **under which shared intrinsic polarized-exchange axioms must a rooted monochromatic reachable-set family intersect its Boolean complement image?**

These results are equivalences and sufficient criteria, not a proof of the required complementary intersection in every coloring.

#### 5. Computational obstruction to the majority shortcut

The sufficient majority condition (6) is **not a universal consequence** of boundary reversal oddness. A reproducible order-eight reversal-odd coloring, stored in the research note *Eight-vertex obstruction to rooted-majority reachability*, has
\[
\boxed{\max_{v,\varepsilon}|\mathcal A_v^\varepsilon|=64=2^{8-2},}
\tag{8}
\]
with no root-color family larger than half the Boolean lattice. Yet it has the spanning one-turn tight word
\[
\boxed{(0,1,3,4,5,6,2,7),}
\tag{9}
\]
whose triple colors are \((0,0,0,1,1,1)\).

The complete representative-bit mask, the 16 rooted family sizes, and an independent standard-library enumeration certificate are preserved in that research note. The equivalence in Theorem 3 remains valid; this finite obstruction rules out only a proof relying on **strict rooted cardinality majority**. A universal theorem must force complementary reachability by more structural means, such as a linked exchange between the two monochromatic arms or a topological/intersection property stronger than set cardinality.

#### 6. The rooted path-basis polynomial and an integer counting identity

The same-terminal equivalence admits an all-dimensional **enumerative** refinement. It expresses the number of spanning at-most-one-turn words as a full-rank coefficient of squared monochromatic path-generating polynomials, and exposes a systematic characteristic-two cancellation in the corresponding doubled graphic-matroid basis count.

For each \(v\in V\) and \(\varepsilon\in\{0,1\}\), define the ordinary commuting-variable polynomial
\[
\boxed{
P_v^\varepsilon(\mathbf x)
=\sum_{\substack{P\text{ vertex-simple }\varepsilon\text{-monochromatic}\\
                   \text{tight word ending at }v}}
\prod_{u\in V(P)\setminus\{v\}}x_u.
}
\tag{10}
\]
Include singleton and two-vertex words, which are vacuously monochromatic in each color. The coefficient
\[
a_v^\varepsilon(S)=[x_S]P_v^\varepsilon
\]
is the number of monochromatic rooted paths using precisely \(S\cup\{v\}\). Thus the support of \(P_v^\varepsilon\) is the rooted family \(\mathcal A_v^\varepsilon\) defined above. Let \(H_0(b)\) and \(H_1(b)\) denote the respective numbers of ordered spanning tight words having zero and precisely one internal color change.

**Theorem 5 (rooted full-rank path-pair identity).** For every ordinary reversal-odd boundary coloring on \(n\ge3\) vertices,
\[
\boxed{
\sum_{v\in V}\sum_{\varepsilon=0}^1
\left[x_{V\setminus\{v\}}\right]
\bigl(P_v^\varepsilon(\mathbf x)\bigr)^2
=4H_0(b)+2H_1(b).
}
\tag{11}
\]
Equivalently, with \(U_v=V\setminus\{v\}\),
\[
\boxed{
\sum_{v,\varepsilon}\ \sum_{S\subseteq U_v}
a_v^\varepsilon(S)a_v^\varepsilon(U_v\setminus S)
=4H_0(b)+2H_1(b).
}
\tag{12}
\]

*Proof.* Each summand on the left counts an **ordered pair** of same-colored monochromatic tight words \(P,Q\) ending at one vertex \(v\), with disjoint other-vertex sets that together exhaust \(V\). Their union is a doubled-graphic-matroid basis by Theorem 2. Theorem 1 glues the ordered pair to the spanning word \(W=P+\operatorname{reverse}(Q)\), which has at most one internal color change.

Conversely, fix a spanning word \(W=(w_1,\ldots,w_n)\). A decomposition at a pivot \(v=w_j\) is forced by the word: \(P=(w_1,\ldots,w_j)\), \(Q=(w_n,\ldots,w_j)\). They have a common monochromatic color \(\varepsilon\) precisely when the prefix triples before the bridging position \(j-1\) all have color \(\varepsilon\), and the suffix triples after that bridging position all have color \(1-\varepsilon\).

If \(W\) has precisely one turn between the triple windows starting at positions \(i\) and \(i+1\), then there are precisely **two** admissible pivots \(j=i+1,i+2\), each with color \(\varepsilon\) equal to the initial run color. Thus \(W\) occurs twice on the left.

If \(W\) is monochromatic of color \(\eta\), two admissible pivots \(j=n-1,n\) use common arm color \(\eta\), while two pivots \(j=1,2\) use common arm color \(1-\eta\) (the short arm is vacuously monochromatic). Thus \(W\) occurs four times, including when \(n=3\), where the coincident middle pivot is counted once in each of the two different colors. Words with at least two changes admit no decomposition, since the only omitted crossing triple cannot suppress both changes. Summing multiplicities proves (11) and (12). \(\square\)

**Corollary 6 (basis-polynomial positivity certificate).** The spanning one-turn conjecture for a fixed boundary coloring is equivalent to strict positivity of the coefficient sum in (11). Each nonzero contributing monomial pair is a feasible full-rank basis in the doubled graphic matroid \(\mathsf R_n^{(2)}\), with both arms constrained to be monochromatic directed tight paths.

**Corollary 7 (parity cancellation).** For every \(v,\varepsilon\), and every \(n\ge2\),
\[
\boxed{
\left[x_{U_v}\right](P_v^\varepsilon)^2\equiv0\pmod2.
}
\tag{13}
\]
This holds regardless of the coloring and regardless of whether any complementary arm pair exists.

*Proof.* The coefficient is
\(\sum_{S\subseteq U_v}a(S)a(U_v\setminus S)\).
As \(U_v\ne\varnothing\), complementation has no fixed subset. Terms come in equal pairs indexed by \(S\) and \(U_v\setminus S\), so the sum is even. \(\square\)

Thus a direct **modulo-two full-rank coefficient** of the symmetric two-arm basis enumerator vanishes identically and cannot certify the desired intersection. This is consistent with, but conceptually distinct from, the binary pointed-matroid cycle–cocycle orthogonality: it reflects the exchange involution swapping the two arms. A proof using algebraic counting must retain asymmetry between the arms, richer integer coefficients, or geometric information about the reachability supports. The identity itself is an integral enumerative theorem, not an existence proof.

#### 7. Canonical phase choice at the root and a symmetric-matrix cancellation

The local tournament at a shared terminal vertex is not an additional feasibility constraint for two-arm gluing; it canonically selects **which of the two reversed Hamilton orders places the bridge on the first color run**.

**Proposition 8 (unique bridge-phase orientation).** Fix \(\varepsilon,v\), and let \(P,Q\) be two distinct vertex-simple color-\(\varepsilon\) tight words ending at \(v\), with disjoint nonterminal vertex sets, and suppose both arms have length at least two. Let \(u,w\) be their penultimate vertices. Then \(u\ne w\), and precisely one of the two Hamilton orders
\[
\boxed{P+\operatorname{rev}(Q),\qquad Q+\operatorname{rev}(P)}
\tag{14}
\]
has the joining triple of color \(\varepsilon\); the other has its joining triple of color \(1-\varepsilon\).

*Proof.* The two joining triples are \((u,v,w)\) and \((w,v,u)\), whose colors are complementary by reversal oddness. All remaining triples lie in the monochromatic first arm or the reversed second arm. The claimed phase choice follows. \(\square\)

Thus the orientation at a local tournament vertex is responsible for **selecting** the color-change position, but does not prevent the one-turn spanning path once the doubled-graphic-matroid basis pair exists. In particular, trying to impose a preselected junction color on *both* splicing orientations would introduce an unnecessary restriction.

For nontrivial arms define terminal refined polynomials
\[
P_{u,v}^{\varepsilon}(\mathbf x)=
\sum_{\substack{P\ \varepsilon\text{-monochromatic}\\
\operatorname{last2}(P)=(u,v)}}
\prod_{a\in V(P)\setminus\{v\}}x_a.
\tag{15}
\]
They give a local matrix representation of the full-rank complementary coefficient. Write
\(A^{\varepsilon}_v(u,w)=\mathbf1_{\{b(u,v,w)=\varepsilon\}}\) for distinct \(u,w\).
Then
\[
A_v^\varepsilon(u,w)+A_v^\varepsilon(w,u)=1,
\tag{16}
\]
and, because commuting polynomials multiply symmetrically,
\[
\boxed{
\sum_{u\ne w}
A_v^\varepsilon(u,w)
P_{u,v}^{\varepsilon}P_{w,v}^{\varepsilon}
=
\frac12\sum_{u\ne w}
P_{u,v}^{\varepsilon}P_{w,v}^{\varepsilon}.
}
\tag{17}
\]
All coefficients on the right are even before the division by two, by pairing \((u,w)\) and \((w,u)\). Taking the full-resource coefficient counts the unordered compatible rooted basis pairs with both arms nontrivial, each with its canonical bridge-color orientation. The remaining pairs involving a singleton arm contribute separately and correspond to monochromatic spanning paths.

Equation (17) shows the **skew-symmetric part of the local tournament adjacency matrix cancels** in this symmetric two-arm enumerator. Any future parity or Pfaffian argument must break the arm-swap symmetry before summing, rather than expect the local skew part to survive a symmetric quadratic form. This reinforces the integer-vs-binary distinction in Corollary 7 and points toward asymmetric terminal-root weights or a signed **two-arm linkage invariant** as a possible algebraic route.

### Random Hamiltonian absorption via transversal matroids

Let \(b_0\) be an arbitrary reversal-odd coloring of distinct ordered triples from an \(n\)-element vertex set \(V\). Independently for each reversal pair of triples, flip both colors with probability \(\rho\in(0,1/2]\), producing \(b\).

**Theorem 1 (noise-forced Hamiltonian tight paths).** If
\[
\boxed{\rho_n^3 n/\log n\to\infty,}\tag{1}
\]
then uniformly in \(b_0\), with probability \(1-o(1)\) **every** prescribed initial ordered pair \((u,v)\) and prescribed color \(\epsilon\in\{0,1\}\) extend to an \(\epsilon\)-monochromatic vertex-simple tight Hamiltonian path.

The key deterministic construction is governed by a transversal matroid.

**Lemma 2 (separated-slot absorption).** Suppose \(P=(v_1,\ldots,v_\ell)\) is an injective \(\epsilon\)-monochromatic tight path and \(U=V\setminus V(P)\). Let \(I\subseteq\{2,\ldots,\ell-2\}\) be gap indices at pairwise distance at least five. Form a bipartite graph \(B\) with left vertices \(U\) and right vertices \(I\); declare \(z\in U\) adjacent to \(i\in I\) when
\[
b(v_{i-1},v_i,z)=b(v_i,z,v_{i+1})
=b(z,v_{i+1},v_{i+2})=\epsilon.\tag{2}
\]
If \(B\) has a matching saturating \(U\), then the original coloring has an \(\epsilon\)-monochromatic tight Hamiltonian path beginning with \((v_1,v_2)\).

*Proof.* For each matched pair \((z,i)\), insert \(z\) between \(v_i,v_{i+1}\). The insertion removes the two original triple windows meeting that gap and replaces them by the three windows in (2), all of the required color. Because selected gaps are separated by at least five positions, the changes at different gaps are disjoint. The resulting word uses all vertices once and retains its first two vertices. Matchable subsets of \(U\) are the independent sets of the transversal matroid determined by \(B\). \(\square\)

*Proof of Theorem 1.* Fix \(u,v,\epsilon\). Set
\[
t=\lceil12\rho^{-1}\log n\rceil,\qquad r=2t.
\]
Condition (1) implies \(t\log n=o(n)\), hence \(r=o(n)\). Beginning with \((u,v)\), repeatedly choose uniformly at random \(t\) of the unused vertices, expose the triples obtained by appending each candidate, and append one candidate with color \(\epsilon\), continuing until \(r\) vertices remain. At each step every newly queried reversal class has the current terminal vertex as its middle vertex. That vertex has never been the middle vertex of an earlier extension query, since the growing path is injective. Therefore the candidate colors are fresh independent random variables, each equal to \(\epsilon\) with probability at least \(\rho\). The chance that a step has no acceptable candidate is at most \((1-\rho)^t\le n^{-12}\). A union bound over fewer than \(n\) steps shows that, except with probability at most \(n^{-11}\), this process produces a monochromatic path \(P\) of length \(\ell=n-r\).

For each \(z\in V\), let \(Q_z\) be the number of stages whose random query set included \(z\). When \(k\) vertices are still unused, the conditional probability of such inclusion is at most \(t/k\), even given the entire earlier construction. Once \(z\) has been appended, its subsequent inclusion probability is zero. Therefore the moment-generating bound for adapted indicators gives
\[
\mathbb E e^{Q_z}
\le \exp\!\left((e-1)t\sum_{k=r+1}^{n-2}k^{-1}\right)
\le \exp((e-1)t(1+\log n)).
\]
By Markov's inequality,
\[
\Pr[Q_z>4t(1+\log n)]
\le\exp(-(5-e)t(1+\log n)).
\]
A union bound gives, with probability \(1-o(n^{-10})\),
\[
\boxed{\max_{z\in V}Q_z\le4t(1+\log n)=o(n).}\tag{3}
\]

Choose \(I=\{2,7,12,\ldots\}\cap\{2,\ldots,\ell-2\}\), so \(K=|I|=(1/5+o(1))n\). For any missing \(z\in U\), consider the three insertion comparisons at gap \(i\). The comparison centered at \(z\) has never been exposed, because \(z\) was never a terminal path vertex. The last comparison, centered at \(v_{i+1}\), also has not been exposed: when \(v_{i+1}\) was terminal during construction, every tested triple had \(v_i\) as one outer vertex, while \((z,v_{i+1},v_{i+2})\) has two different outer vertices. Only the first comparison, centered at \(v_i\), might have been exposed. This occurs at no more than \(Q_z\) gaps. Thus at least \(K-Q_z\) gap comparisons are fully fresh for each missing \(z\).

The reversal classes in the three comparisons for distinct eligible pairs \((z,i)\in U\times I\) are all different: the five-position gap spacing separates centers \(v_i,v_{i+1}\), the missing vertices \(z\) lie outside \(P\), and the remaining outer pairs identify the missing vertex and its gap. Conditional on the complete construction history, all eligible compatibility indicators are independent and have success probability at least \(\rho^3\).

We verify Hall's condition by a union bound. Let \(A\subseteq U\) be nonempty, with \(a=|A|\), and \(C\subseteq I\) have cardinality \(a-1\). If (3) holds, then for each \(z\in A\), at least
\[
K-Q_z-|C|\ge n/10
\]
gaps outside \(C\) retain three fresh comparisons, for all sufficiently large \(n\), since both \(r\) and the bound in (3) are \(o(n)\). The probability that no compatible edge joins \(A\) to \(I\setminus C\) is at most \(e^{-\rho^3 a n/10}\). The number of pairs \(A,C\) of these cardinalities is bounded by
\(\binom ra\binom K{a-1}\le n^{2a}\). Hence
\[
\Pr[\exists A\subseteq U:|N_B(A)|<|A|\mid\text{construction}]
\le\sum_{a=1}^{r}\exp\!\left(a(2\log n-\rho^3n/10)\right)
=n^{-\omega(1)}.\tag{4}
\]
By Hall's theorem, with overwhelming probability the bipartite compatibility graph has a matching saturating \(U\). Lemma 2 inserts every leftover vertex while preserving the complete monochromatic path. The error probabilities from the greedy stage, the exposure estimate, and Hall's estimate sum to \(o(n^{-3})\), allowing a final union bound over both colors and fewer than \(n^2\) ordered initial pairs. \(\square\)

**Scope and interpretation.** This proves a three-window, resource-preserving absorption theorem for ordinary boundary 3-tournaments and identifies its intrinsic transversal-matroid independence condition. The random perturbation assumption supplies the necessary compatible slots. It substantially strengthens near-spanning random smoothing, but it does not establish a deterministic spanning monochromatic path for arbitrary boundary colorings. For cube-edge colorings, inserting an unused coordinate at an interior position changes the edges along the entire remaining suffix, so an additional cubical exchange argument would be required for a parallel Hamiltonian result.

### Rooted random cube geodesics and permutation overlap moments

Fix a cube vertex \(x\), a prescribed color \(\epsilon\), and an arbitrary antipodally odd coloring \(c_0\) of \(Q_n\). Independently flip both colors in each antipodal edge orbit with probability \(\rho\in(0,1/2]\), producing \(c\).

**Theorem (optimal rootwise noise threshold).** If \(n\rho\to\infty\), the probability that there is an \(\epsilon\)-monochromatic geodesic from \(x\) to \(\tau x\) tends to one, uniformly over \(c_0\). Put \(h=3e(\rho^{-1}-1)/n\). If \(h<1\), the failure probability is at most \(h\). The growth assumption \(n\rho\to\infty\) is necessary for the uniform fixed-root, fixed-color assertion.

**Lemma (shared-edge moment).** Fix a coordinate permutation \(\pi\), take \(\sigma\in S_n\) uniformly, and let \(s\) be the number of cube edges common to the two root-to-antipode geodesics. For every \(z\ge1\),
\[
\mathbb E z^s\le\sum_{t=0}^n\frac{[3(z-1)]^t}{(n)_t}
\le\sum_{t=0}^n\left(\frac{3e(z-1)}n\right)^t.
\tag{1}
\]

*Proof.* Relabel so that \(\pi=(1,\ldots,n)\). The edge at rank \(k\) is common precisely when the first \(k\) symbols of \(\sigma\) are \([k]\) and its next symbol is \(k+1\). This is a singleton component of its direct-sum permutation decomposition. Prescribing \(t\) such positions divides the other \(n-t\) entries into \(t+1\) consecutive blocks of sizes \(a_0,\ldots,a_t\). The number of compatible permutations is \(\prod_j a_j!\). Expanding \(z^s=(1+z-1)^s\) gives
\[
\mathbb E z^s=\frac1{n!}\sum_{t=0}^n(z-1)^t
\sum_{\substack{a_0+\cdots+a_t=n-t\\a_j\ge0}}\prod_j a_j!.
\]
For all \(m\ge0\), \(\sum_{j=0}^m j!(m-j)!=m!\sum_j\binom mj^{-1}\le3m!\), since the two extreme reciprocals are one and each interior reciprocal is at most \(1/m\). Convolution induction bounds the inner sum by \(3^t(n-t)!\), giving the first inequality. The inequality \((n)_t\ge(n/e)^t\), obtained by comparing the geometric means of the largest \(t\) integers among \(1,\ldots,n\) with \((n!)^{1/n}\ge n/e\), proves the second. \(\square\)

*Proof of the theorem.* Let \(A_\pi\) be the event that the path of coordinate permutation \(\pi\) is all color \(\epsilon\), and \(q_\pi=\Pr(A_\pi)\). A geodesic uses each direction once, so its edges lie in distinct antipodal orbits, and \(q_\pi=\prod_{f\in P_\pi}p_f\), where \(p_f=\Pr(c(f)=\epsilon)\in[\rho,1-\rho]\). Define
\[
Z=\sum_{\pi\in S_n}\frac{\mathbf1_{A_\pi}}{q_\pi};
\qquad\mathbb EZ=n!.
\]
For two geodesics \(P_\pi,P_\sigma\), their simultaneous all-\(\epsilon\) event has probability zero if an edge of one is antipodal to an edge of the other. Otherwise all orbit variables are independent except for common edges, each contributing a joint-to-product factor \(1/p_f\le1/\rho\). Consequently
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{\pi,\sigma}\rho^{-|E(P_\pi)\cap E(P_\sigma)|}
\le\sum_{t=0}^n h^t\le(1-h)^{-1}.
\]
The second-moment inequality gives \(\Pr(Z>0)\ge1-h\), proving the quantitative claim and the limit. Conversely choose the initial coloring with all \(n\) edges at \(x\) colored \(1-\epsilon\), completing antipodal pairs consistently. With probability \((1-\rho)^n\), none of these root edges flips, so no \(\epsilon\)-monochromatic path starts at \(x\). This failure probability stays positive whenever \(n\rho\) is bounded. \(\square\)

The result concerns full geodesics under noise, and is uniform over the baseline coloring. The deterministic NORI1 conjecture remains open.

**Corollary (coordinate-face smoothing).** Let \(F\) be an \(m\)-dimensional coordinate face of \(Q_n\), \(2\le m\le n\), and fix \(x\in F\) and a color \(\epsilon\). Independently flip the colors on full-cube antipodal edge pairs with probability \(\rho\). Then, uniformly in the initial antipodally odd coloring,
\[
\Pr(\text{no \(\epsilon\)-monochromatic geodesic in \(F\) between opposite face corners})
\le\frac{3e(\rho^{-1}-1)}m
\]
whenever the right side is below one. In particular, the failure probability is \(o(1)\) if \(m\rho\to\infty\).

*Proof.* A face geodesic uses each of its \(m\) free coordinates once, and hence meets distinct full-cube antipodal edge orbits. If \(F\) is proper, the full-cube antipodal translate of any edge of \(F\) lies outside \(F\), so two face geodesics can share an orbit only by using the same edge. In the full-face case, opposite edges between different geodesics produce incompatible prescribed-color events and contribute zero to their joint probability. Thus the weighted second-moment calculation and the permutation singleton-block bound of the theorem apply in either case, with \(m\) in place of \(n\). \(\square\)

**Lemma (opposite-chain edge exclusion).** Let \(P_\pi\) be the root-to-antipode coordinate geodesic given by a permutation \(\pi=(i_1,\ldots,i_n)\), and let \(P_{\pi^R}\) use its reverse permutation. Every root-to-antipode coordinate geodesic \(P_\sigma\) shares an edge with at most one of \(P_\pi,P_{\pi^R}\).

*Proof.* In resource-set coordinates relative to the root, the first path has edges between its consecutive prefix sets
\[
A_k=\{i_1,\ldots,i_k\},\qquad 0\le k\le n,
\]
whereas the second has edges between consecutive suffix sets
\[
B_j=\{i_{n-j+1},\ldots,i_n\},\qquad 0\le j\le n.
\]
If a monotone resource chain contained an edge \(A_k\to A_{k+1}\) followed by an edge \(B_j\to B_{j+1}\), its sets would satisfy \(A_{k+1}\subseteq B_j\). But \(i_1\in A_{k+1}\) and \(i_1\notin B_j\), since \(j\le n-1\). If the suffix edge occurred first, the chain would require \(B_{j+1}\subseteq A_k\), contradicted by \(i_n\in B_{j+1}\) and \(i_n\notin A_k\). These exhaust the possible orders. \(\square\)

**Theorem (full edge-color profile universality).** Under the hypotheses of the rootwise smoothing theorem, fix an arbitrary predetermined word \(w=(w_1,\ldots,w_n)\in\{0,1\}^n\) and a root \(x\). There is a root-to-antipode geodesic whose consecutive edge colors form \(w\), with failure probability at most
\[
\boxed{\frac{2h}{1+h},\qquad
h=\frac{3e(\rho^{-1}-1)}n<1.}
\]
In particular this probability tends to one uniformly in the baseline coloring and prescribed word whenever \(n\rho\to\infty\). The growth condition is necessary for a uniform fixed-root, fixed-word assertion.

*Proof.* For every \(\pi\in S_n\), let \(A_\pi\) be the event that the sequence of colors along \(P_\pi\) is \(w\), let \(q_\pi=\Pr(A_\pi)>0\), and set \(Z=\sum_\pi\mathbf1_{A_\pi}/q_\pi\). Since each coordinate is used once, a single path visits distinct antipodal noise-variable orbits and \(\mathbb EZ=n!\).

A pair of paths may share a noise orbit through a common cube edge or through antipodal partner edges. When the two demands on a shared orbit conflict, their joint success probability is zero; otherwise that orbit contributes a joint-to-product factor at most \(\rho^{-1}\). Let \(K_+(\pi,\sigma)\) count edges common to \(P_\pi,P_\sigma\), and let \(K_-(\pi,\sigma)\) count edges common to \(P_{\pi^R},P_\sigma\). The antipodal image of the edge set of \(P_\pi\) is the edge set of \(P_{\pi^R}\), so \(K_++K_-\) counts shared noise orbits. By the opposite-chain exclusion lemma, \(K_+K_-=0\). Therefore, for \(z\ge1\),
\[
\begin{aligned}
\mathbb E_{\pi,\sigma}z^{K_++K_-}
&=1+\mathbb E(z^{K_+}-1)+\mathbb E(z^{K_-}-1)\\
&=2\mathbb E_{\pi,\sigma}z^{K_+}-1.
\end{aligned}
\]
The two overlap counts have identical marginal distributions under uniform permutations. Apply the singleton-block moment bound with \(z=\rho^{-1}\) to obtain
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le2(1-h)^{-1}-1=\frac{1+h}{1-h}.
\]
Cauchy--Schwarz now yields \(\Pr(Z>0)\ge(1-h)/(1+h)\), proving the failure estimate. For necessity, prescribe the first edge color \(w_1\) and choose the initial coloring with all \(n\) root-incident edges of color \(1-w_1\). The probability that none flips is \((1-\rho)^n\), bounded away from zero when \(n\rho\) stays bounded. \(\square\)

On a proper \(m\)-face, no two of its edges lie in the same full-cube antipodal orbit. Hence the face corollary also holds for every prescribed length-\(m\) color word with its original failure bound \(3e(\rho^{-1}-1)/m\). The new theorem establishes a common fixed-pattern smoothing principle with the rooted boundary Hamiltonian-window theorem.

### Rooted Hamiltonian windows and the sharp random perturbation threshold

Let \(V\) be an \(n\)-element set, \(n\ge4\), and let \(b_0:V_{\ne}^3\to\mathbb F_2\) satisfy \(b_0(c,v,a)=1-b_0(a,v,c)\). Independently flip both colors in each reversal orbit of ordered triples with probability \(\rho\in(0,1/2]\), obtaining \(b\). For an injective word \(P=(v_1,\dots,v_n)\), its windows are the ordered triples \((v_i,v_{i+1},v_{i+2})\), \(1\le i\le n-2\).

**Theorem 1 (optimal rooted Hamiltonian pattern universality).** Fix any ordered pair \((u,v)\) of distinct vertices and any predetermined binary word \(a=(a_1,\ldots,a_{n-2})\). Put
\[
h_n=\frac{e(1+2e)(\rho^{-1}-1)}{n-2}.
\]
If \(h_n<1\), then, uniformly over \(b_0\),
\[
\boxed{\Pr\bigl(\text{no Hamiltonian tight path starting with \(u,v\) has color word \(a\)}\bigr)\le h_n.}\tag{1}
\]
Consequently \(\rho_n n\to\infty\) implies that each preselected color word is realized from \((u,v)\) with probability \(1-o(1)\), uniformly in the word. Simultaneous realization of all color words is not asserted. Conversely, the assumption \(\rho_n n\to\infty\) is necessary for this assertion to hold uniformly over all baseline colorings.

The key input is a factorial-moment inequality for overlapping length-three windows.

**Lemma 2 (fixed-prefix window overlap).** Fix a permutation \(\pi=(1,\ldots,n)\), and choose \(\sigma\) uniformly among permutations beginning with \(1,2\). Let \(K(\pi,\sigma)\) count the reversal orbits of length-three windows appearing in both \(\pi\) and \(\sigma\). For \(z\ge1\), set \(y=z-1\). Then
\[
\boxed{\mathbb E_\sigma z^{K(\pi,\sigma)}
\le\sum_{t=0}^{n-2}\left(\frac{e(1+2e)y}{n-2}\right)^t.}\tag{2}
\]

*Proof.* Put \(N=n-2\). For a nonempty set \(S\subseteq[N]\), with \(|S|=t\), write \(c\) for its number of maximal runs of consecutive integers. Each selected triple window at rank \(i\) requires its two undirected path edges \(\{i,i+1\},\{i+1,i+2\}\) to occur as adjacent pairs in \(\sigma\). Their union is a path forest with \(t+c\) edges. Add the edge \(\{1,2\}\), which is already the prescribed first edge of \(\sigma\).

If \(1\in S\), the added edge is already present; the resulting forest has \(m=t+c\) edges and at most \(c\) nontrivial components. If \(1\notin S\), it has \(m=t+c+1\) edges and at most \(c+1\) components. For a forest with \(m\) edges and \(r\) nontrivial path components, one of which contains the required initial ordered edge \((1,2)\), the number of permutations beginning \(1,2\) that contain every forest edge as a consecutive adjacency is at most \(2^{r-1}(n-m-1)!\): the initial component has its order and position prescribed, each other path component admits two orientations, and the remaining blocks can be permuted. Dividing by the total \((n-2)!\) gives
\[
\Pr(S\text{ is contained in the common-window indices})\le
\begin{cases}
2^{c-1}/(N)_{t+c-1},&1\in S,\\
2^c/(N)_{t+c},&1\notin S,
\end{cases}\tag{3}
\]
where \((N)_j=N(N-1)\cdots(N-j+1)\). The bound holds because every shared triple imposes its two underlying path adjacencies.

The number of \(t\)-subsets of \([N]\) with \(c\) runs and containing \(1\) is
\[
\binom{t-1}{c-1}\binom{N-t}{c-1},
\]
and the number avoiding \(1\) is
\[
\binom{t-1}{c-1}\binom{N-t}{c}.
\]
Use \((N)_j\ge(N/e)^j\), \(\binom{N-t}{j}\le N^j/j!\), and \(1/j!\le1\). The sum of probabilities in (3) over all \(t\)-subsets is at most
\[
\begin{aligned}
&\left(\frac eN\right)^t
\sum_{c=1}^t\binom{t-1}{c-1}
\left(\frac{(2e)^{c-1}}{(c-1)!}
+\frac{(2e)^c}{c!}\right)\\
&\hspace{30mm}\le
\left(\frac eN\right)^t(1+2e)^t.\tag{4}
\end{aligned}
\]
Finally expand \(z^K=(1+y)^K=\sum_{S\subseteq\mathrm{CommonWindows}}y^{|S|}\), average, and insert (4), proving (2). \(\square\)

*Proof of Theorem 1.* Let \(\mathcal P\) be the \((n-2)!\) permutations of \(V\) starting with \(u,v\). Let \(A_P\) be the event that the consecutive triple-color word of \(P\) equals \(a\), and let \(q_P=\Pr(A_P)>0\). Their reversal orbits are distinct because their middle vertices are distinct, so
\[
q_P=\prod_{t\in\mathrm{Windows}(P)}p_t,\qquad p_t\in[\rho,1-\rho].
\]
Define
\[
Z=\sum_{P\in\mathcal P}\frac{\mathbf1_{A_P}}{q_P},
\qquad \mathbb E Z=(n-2)!.
\]
If two words \(P,Q\) require opposing colors on the same reversal orbit, their joint all-\(\epsilon\) event has probability zero. Otherwise independence of distinct orbit-noise variables shows that the ratio \(\Pr(A_P\cap A_Q)/(q_Pq_Q)\) is a product of \(p_t^{-1}\le\rho^{-1}\) over their shared window orbits. Hence
\[
\frac{\mathbb EZ^2}{(\mathbb EZ)^2}
\le\mathbb E_{P,Q}\rho^{-K(P,Q)}
\le\sum_{t=0}^{n-2}h_n^t
\le(1-h_n)^{-1}.
\]
By Cauchy--Schwarz, \(\Pr(Z>0)\ge(\mathbb EZ)^2/\mathbb EZ^2\ge1-h_n\), giving (1).

For necessity, choose \(b_0(u,v,w)=1-a_1\) for every \(w\in V\setminus\{u,v\}\), assign the reverse triples their complementary color, and fill the remaining reversal orbits arbitrarily. With probability \((1-\rho)^{n-2}\), no triple \((u,v,w)\) is flipped, and no Hamiltonian tight path starting with \(u,v\) can realize \(a\). This failure probability stays bounded away from zero if \(n\rho\) remains bounded. \(\square\)

**Common witness-overlap principle.** The theorem and the rootwise cube-geodesic theorem of the preceding Subsection both use a family of full-resource paths, with a distinct independent noise variable for each edge or window constraint within a path. For any such finite family \(\mathcal W\), let \(q_W>0\) be the probability that \(W\) satisfies its prescribed monochromatic constraints, and let \(K(W,W')\) count shared unoriented noise-variable orbits. With \(Z=\sum_W\mathbf1_{\{W\text{ succeeds}\}}/q_W\), the same argument gives
\[
\boxed{
\Pr(Z>0)\ge
\left(\mathbb E_{W,W'}\rho^{-K(W,W')}\right)^{-1}.}\tag{5}
\]
Oppositely oriented shared constraints make joint success impossible and only strengthen the estimate. In both canonical applications, the overlap sets form subforests of underlying path bases; their factorial moments decay sufficiently rapidly to produce the common optimal rootwise smoothing condition \(n\rho\to\infty\).

The theorem concerns independent random perturbations of arbitrary reversal-odd colorings and applies to each prescribed window pattern, including monochromatic, one-switch, and alternating words. It strengthens the earlier transversal-matroid absorption theorem, which supplies simultaneous guarantees for all ordered starting pairs under a larger perturbation rate. Neither theorem establishes a deterministic boundary-tournament selector or unrestricted NORI1.

### Two-resource Hamiltonian recognition and monochromatic forest rank

Let \(n\ge4\), let \(V=[n]\), and let \(\mathcal T_n\) denote reversal-orbits \([a,b,c]=[c,b,a]\) of ordered triples with pairwise distinct entries. As established in the boundary-cover construction, \(\mathcal T_n\) is the edge set of the line graph \(L(K_n)\): the turn \([a,b,c]\) joins its two **edge states** \(ab=\{a,b\}\) and \(bc=\{b,c\}\) and has **middle label** \(b\).

For a subset \(T\subseteq\mathcal T_n\), let \(J_T\) be the subgraph of \(L(K_n)\) with edge set \(T\), discarding isolated state vertices. Write \(S(T)\subseteq E(K_n)\) for its vertex support, i.e. the union of the two state edges activated by each triple. We say that \(T\) is **resource-feasible** if

* no two selected triples have the same middle label (independence in the middle-label partition matroid), and
* \(S(T)\) is independent in the graphic matroid \(M(K_n)\).

These conditions are intrinsic to the two resource systems, without presupposing a path or its orientation.

**Theorem 1 (automatic path-forest structure).** Every nonempty resource-feasible \(T\) has \(J_T\) equal to a vertex-disjoint union of \(c\ge1\) simple paths (each with at least one edge). Each such component lifts, in either direction, to a vertex-simple path in \(K_n\), and its line-graph edges are precisely the selected consecutive triple reversal-orbits of that path. If \(m=|T|\), then
\[
\boxed{|S(T)|=m+c\le n-1,\qquad c\le n-1-m.}\tag{1}
\]

*Proof.* A line-graph state \(e=\{a,b\}\) is incident with selected turns centered at \(a\) or \(b\). At most one selected turn has each middle label, so the degree of \(e\) in \(J_T\) is at most two. If a component of \(J_T\) were a cycle with turns centered at \(b_1,\ldots,b_r\), then consecutive turn centers would be distinct and its state edges would be \(\{b_1,b_2\},\{b_2,b_3\},\ldots,\{b_r,b_1\}\), forming a cycle in the underlying graph \(S(T)\), contrary to graphic independence. Thus \(J_T\) is a disjoint union of paths.

For one such path with state vertices \(e_1,\ldots,e_{\ell+1}\) and successive turn centers \(b_1,\ldots,b_\ell\), the middle-label independence gives \(b_i\ne b_{i+1}\), hence each intermediate state \(e_{i+1}\) has endpoints \(b_i,b_{i+1}\). Taking the other endpoints of the first and last states gives an edge trail in \(K_n\). As its state edges belong to the forest \(S(T)\), no original vertex repeats: otherwise the trail would contain a graph cycle. It is therefore a simple path whose consecutive triple windows are the selected turns. Summing \(\ell+1\) state vertices over its \(c\) disjoint line-graph components gives \(|S(T)|=|T|+c\). Graphic independence bounds this by \(n-1\), proving (1). \(\square\)

**Corollary 2 (complete Hamiltonian window recognition).** A \(0/1\) set \(T\subseteq\mathcal T_n\) is the family of consecutive triple reversal-orbits of a Hamiltonian vertex word if and only if
\[
\boxed{|T|=n-2,\quad\text{its middle labels are distinct},\quad
S(T)\in\mathcal I(M(K_n)).}\tag{2}
\]
No separate global cut-connectivity condition is needed at this integral maximal cardinality.

*Proof.* Necessity follows from a Hamiltonian word: the middle labels are its \(n-2\) internal vertices, and its \(n-1\) consecutive \(K_n\) edges form a spanning tree. For sufficiency, Theorem 1 gives \(n-2+c=|S(T)|\le n-1\), so \(c=1\). Thus \(J_T\) is one simple path on \(n-1\) edge states. Its lift is a simple \(K_n\) path with \(n-1\) edges, hence Hamiltonian. \(\square\)

This proves that a *full-rank* middle-partition selection with graphic-independent state support automatically satisfies the connectivity and incidence requirements absent from the bare Smith lattice and uniform-matroid base polytope. Both resource tests are necessary: several selected turns of the same center can form a line-graph star despite an underlying forest, while a repeated original vertex gives a graphic circuit despite distinct middle labels.

**Theorem 3 (complete single-turn augmentation test).** Let \(T\ne\varnothing\) be resource-feasible with \(|T|<n-2\), and let \(B=(V,S(T))\) be its underlying forest. There exists \(t\notin T\) such that \(T\cup\{t\}\) remains resource-feasible if and only if at least one of the following holds:

1. \(B\) is disconnected on \(V\); or
2. \(B\) is a spanning tree having a vertex \(b\) of degree at least two which is not yet used as the middle label of any turn in \(T\).

*Proof.* If \(B\) is disconnected, choose a leaf \(b\) in a nontrivial tree component, and let \(ab\in S(T)\) be its incident edge. Since \(\deg_B(b)=1\), no selected turn is centered at \(b\). Choose \(c\) in another component. The new turn \([a,b,c]\) has unused middle label \(b\), and its activated edge \(bc\) joins two forest components; adding it preserves graphic independence.

If \(B\) is a spanning tree and \(b\) is an unused center with two incident tree edges \(ab,bc\), the turn \([a,b,c]\) adds no new state edge to \(S(T)\), preserves middle-label independence, and is not already selected. It therefore augments \(T\).

Conversely, when \(B\) is a spanning tree no new underlying \(K_n\) edge can be activated without creating a cycle. Any added turn must use two edges already in \(B\), so its center must have tree degree at least two; distinct middle labels require it to be unused. \(\square\)

**Corollary 4 (failure of ordinary matroid augmentation).** The hereditary family of resource-feasible turn sets does not satisfy the matroid augmentation axiom. For every \(n\ge5\), consider the two simple \(K_n\) paths
\[
P_1=(0,1,2),\qquad P_2=(3,2,4,5,\ldots,n-1)
\]
and let \(T\) be the union of their respective triple-window orbit sets. Its middle centers are \(1,2,4,5,\ldots,n-2\), all distinct, and its state-edge support is the spanning tree
\[
01,\ 12,\ 23,\ 24,\ 45,\ 56,\ldots,(n-2)(n-1).
\]
It has \(n-3\) selected turns. The unused centers are precisely the three leaves \(0,3,n-1\), so by Theorem 3 it admits no single-turn augmentation, even though Hamiltonian triple sets of cardinality \(n-2\) exist. In dimension five the obstruction is simply \(T=\{[0,1,2],[3,2,4]\}\).

We next quantify how much of a resource-feasible turn forest can survive in one Hamiltonian vertex word. For a reversal-odd boundary coloring \(b\), let \(\operatorname{sw}_b(P)\) be the number of color changes between successive triple windows of a simple word \(P\). Reversing the word complements and reverses the triple-color sequence, so its switch count is unchanged. Accordingly every component of \(J_T\) has an unambiguous switch count \(s_b(Q)\), independent of which direction is used to read its corresponding simple \(K_n\) path.

**Theorem 5 (cost-controlled forest-to-Hamiltonian completion).** Let \(T\ne\varnothing\) be resource-feasible with \(m=|T|=n-2-\delta\), \(\delta\ge0\), and components \(Q_1,\ldots,Q_c\) of \(J_T\). There is a Hamiltonian vertex word \(P\) satisfying
\[
\boxed{\operatorname{sw}_b(P)
\le\sum_{i=1}^{c}s_b(Q_i)+6\delta.}\tag{3}
\]
Moreover, if each component is monochromatic (possibly with different colors before choosing its direction), there is a Hamiltonian word \(P\) with
\[
\boxed{\operatorname{sw}_b(P)\le4\delta.}\tag{4}
\]
The construction uses at most \(2\delta+1\) surviving vertex-disjoint path pieces; at least \(m-3\delta\) original turn windows remain as internal windows of those pieces, with a negative bound interpreted as vacuous.

*Proof.* Let \(h\) be the number of nontrivial connected components of the \(K_n\) forest \(B=(V,S(T))\), and let \(u\) count isolated vertices of \(B\). By Theorem 1, each line-graph component \(Q_i\) lifts to a simple \(K_n\) path \(P_i\), and the sum of the numbers of vertex occurrences across these \(c\) paths is \(m+2c\). The forest \(B\) has \(|S(T)|=m+c\) edges and \(m+c+h\) nonisolated vertices, so the number of repeated vertex occurrences among \(P_1,\ldots,P_c\), beyond one occurrence per original vertex, is
\[
r=(m+2c)-(m+c+h)=c-h.\tag{5}
\]
Assign every original vertex occurring in the paths to one owning occurrence and delete its other \(r\) occurrences. Deleting a vertex from a path word splits it into at most two contiguous subwords, increasing the number of pieces by at most one. After these deletions all surviving subwords are vertex-disjoint, and adding the \(u\) missing vertices as singleton words produces at most
\[
q\le c+r+u=2c-h+u=n-m+c-2h\tag{6}
\]
pieces which together use every original vertex precisely once. The bound \(m+c\le n-1\), combined with \(h\ge1\), gives \(c\le\delta+1\) and
\[
\boxed{q\le2\delta+1.}\tag{7}
\]
Each removed vertex occurrence belongs to at most three original triple windows, so at least \(m-3r\ge m-3\delta\) selected turn windows survive within the pieces.

Orient each remaining piece consistently with its original \(P_i\), and concatenate all \(q\) pieces arbitrarily into a Hamiltonian word. A triple window wholly contained inside one piece retains its original color and any switch between consecutive such windows was already counted in \(\sum_i s_b(Q_i)\). Only windows crossing a piece boundary are new; at most two triple windows cross any given boundary. Every new switch comparison is incident to one of these crossing windows, and for each boundary at most three comparisons need to be counted. Thus at most \(3(q-1)\) new changes arise. This proves
\(\operatorname{sw}_b(P)\le\sum_i s_b(Q_i)+3(q-1)
\le\sum_i s_b(Q_i)+6\delta\), establishing (3).

If each original component \(Q_i\) has constant color, reverse individual paths before trimming them so all internal triple windows of all pieces have the same prescribed color \(\epsilon\); reversal-oddness makes this possible. All triple windows not crossing a join then have color \(\epsilon\). The crossing-window indices form a union of at most \(q-1\) intervals, each of length at most two. Any assignment of the other color to positions in a union of such intervals creates at most \(q-1\) maximal runs of non-\(\epsilon\) colors: an interval of length at most two can add at most one such run. Every run contributes at most two color changes. Hence \(\operatorname{sw}_b(P)\le2(q-1)\le4\delta\), proving (4). \(\square\)

**Theorem 6 (constant-factor matroidal rank-deficiency principle).** For every reversal-odd boundary 3-tournament \(b\), define
\[
R(b)=\max\{|T|: T\subseteq\mathcal T_n
\text{ resource-feasible, and each path component of }J_T
\text{ has constant triple color}\},
\]
and set
\[
\delta(b)=n-2-R(b),\qquad
\mu(b)=\min_{\pi\in S_n}\operatorname{sw}_b(\pi).
\]
Then for every \(n\ge4\),
\[
\boxed{\delta(b)\le\mu(b)\le4\delta(b).}\tag{8}
\]

*Proof.* Take a Hamiltonian word attaining \(s=\mu(b)\) switches and delete the right-hand triple window at each switch of its triple-color sequence. At most \(s\) windows are removed; the remaining selected turns form a resource-feasible subset of its original Hamiltonian line-graph path, and every surviving component has constant color. Thus \(R(b)\ge n-2-s\), or \(\delta(b)\le\mu(b)\).

Conversely, choose a maximizing \(T\) of size \(R(b)=n-2-\delta(b)\). By Theorem 5's monochromatic completion (4), there is a Hamiltonian word with at most \(4\delta(b)\) changes. Minimizing over all words yields \(\mu(b)\le4\delta(b)\). \(\square\)

**Interpretation.** The Hamiltonian switch minimization problem is, up to a universal factor four, equivalent to maximizing the rank of a *monochromatic forest of graphic-independent triple turns with distinct centers*. The two independence systems are necessary, but their intersection on the turn ground set is not itself a matroid: Theorem 3 supplies an obstruction to single-element augmentation. A promising stronger approach is to seek a **multi-exchange augmenting principle** for this resource system under the monochromatic-component constraint. An increase in \(R(b)\) immediately reduces the quantitative ceiling (8), and finding \(R(b)\ge n-2-o(\sqrt n)\) would produce a Hamiltonian word with \(o(\sqrt n)\) switches and hence a monochromatic tight subpath of length \(\omega(\sqrt n)\). This remains conjectural. The new theorems do not settle an unrestricted long-monochromatic-path conjecture, but reduce its asymptotic strengthening to a near-basis rank statement in a structured matroidal path-forest system.

**Independent finite check.** Enumerating every subset of \(n-2\) turn orbits and applying the two independence tests gives, in dimensions \(n=4,5,6\), respectively \(12,60,360\) feasible sets and no non-Hamiltonian sets. These counts agree with the \(n!/2\) unoriented Hamiltonian words; the proofs are dimension-independent and do not rely on the enumeration.

#### A legal, cost-controlled augmenting exchange

Orient each edge of the turn graph \(L(K_n)\) according to the reversal-odd coloring \(b\). The turn from edge-state \(ab\) to \(bc\) is oriented in that direction when \(b(a,b,c)=1\), and the other direction otherwise.

**Lemma 7 (local orientation energy).** For any resource-feasible turn set \(T\), put \(d_b(e,T)=1\) if an edge-state \(e\in S(T)\) has two selected turns that both point into it or both point out of it, and zero otherwise. Then
\[
\boxed{K_b(T)=\sum_{e\in S(T)}d_b(e,T)
=\sum_{Q\text{ component of }J_T}\operatorname{sw}_b(Q).}\tag{9}
\]
*Proof.* Along a component path, consecutive triple colors differ precisely when both corresponding directed turn edges have the same incoming or outgoing incidence at their common state. Reversal of the path complements and reverses its color word, preserving this count. \(\square\)

**Theorem 8 (one-for-two augmentation with at most three new switches).** For \(n\ge5\), every nonempty resource-feasible \(T\) with \(|T|<n-2\) can be replaced by a resource-feasible \(T'\) satisfying
\[
\boxed{|T'|=|T|+1,\quad |T\setminus T'|\le1,\quad
|T'\setminus T|\le2,\quad K_b(T')\le K_b(T)+3.}\tag{10}
\]
The result holds for every reversal-odd boundary coloring \(b\).

*Proof.* Write \(B=(V,S(T))\) for the original-vertex forest. If \(B\) is disconnected, choose a leaf \(u\) in a nontrivial tree component, its neighbor \(a\), and a vertex \(w\) in another component. Add the turn \([a,u,w]\). This joins forest components through the new state-edge \(uw\), uses a fresh middle label \(u\), and creates at most one local orientation defect at the old edge-state \(au\).

If \(B\) is spanning and has an unused middle label \(u\) with tree degree at least two, add the turn between two tree edges incident with \(u\). State support is unchanged, middle independence persists, and at most two orientation defects are created, because neither of the two involved line-graph states had degree exceeding one.

Otherwise \(B\) is a spanning tree whose unused middle labels are all leaves. Since \(|T|<n-2\), the tree has a branching vertex \(v\) of degree at least three: if it were a Hamiltonian path, all its internal vertices would already be selected middle labels, giving \(|T|\ge n-2\). The unique turn centered at \(v\) involves two of its incident edges. Choose a third tree edge \(vc\), absent from that turn. This state-edge must belong to the unique turn \(t_c\) centered at \(c\), so \(c\) is an internal tree vertex and the line-graph degree of state \(vc\) is one.

Choose a leaf \(u\) in the branch of \(B-v\) containing \(c\), and a leaf \(w\) in another branch. Write \(a\) for the tree neighbor of \(u\) and \(d\) for that of \(w\). The edge \(vc\) belongs to the tree path from \(u\) to \(w\), away from their leaf edges. Define
\[
\boxed{T'=(T\setminus\{t_c\})\cup\{[a,u,w],[u,w,d]\}.}\tag{11}
\]
Both inserted centers \(u,w\) were previously unused. Deleting \(t_c\) removes state \(vc\), since no other selected turn uses it. Consequently
\[
S(T')\subseteq(S(T)\setminus\{vc\})\cup\{uw\}.\tag{12}
\]
The latter set is a tree: the new chord \(uw\) creates a fundamental cycle in \(B\), and \(vc\) lies on that cycle. Thus graphic independence holds, and the new middle labels are distinct. We removed one turn and inserted two, so the selected rank grew by one.

Removing \(t_c\) creates no orientation defect. Before inserting the two new turns, the old states \(au,dw\) each have line-graph degree at most one, because the leaves \(u,w\) were unused centers; the new state \(uw\) has degree zero. The two new turns can create at most one defect at each of \(au,dw,uw\), hence at most three in total. This proves the theorem. \(\square\)

**Corollary 9 (factor-three comparison).** With the maximum monochromatic feasible-forest rank \(R(b)\), rank deficit \(\delta(b)=n-2-R(b)\), and minimum Hamiltonian switch count \(\mu(b)\) defined earlier, every \(n\ge5\) satisfies
\[
\boxed{\delta(b)\le\mu(b)\le3\delta(b).}\tag{13}
\]
*Proof.* The lower inequality is Theorem 6: from an \(s\)-switch Hamiltonian word delete the right-hand triple at each switch, retaining at least \(n-2-s\) turns partitioned into monochromatic components. For the upper inequality, start from an optimal monochromatic feasible forest \(T\), with \(K_b(T)=0\). Apply Theorem 8 a total of \(\delta(b)\) times. The final turn set has \(n-2\) edges and is Hamiltonian by Corollary 2. Its cost rose by at most three per augmentation, giving \(\mu(b)\le3\delta(b)\). \(\square\)

**Corollary 10 (cost-stable full-rank extension).** Iterating the theorem \(n-2-|T|\) times extends any nonempty feasible set to a Hamiltonian turn set, deleting at most one and adding at most two turns per step, and gives
\[
\boxed{K_b(T_*)\le K_b(T)+3(n-2-|T|).}\tag{14}
\]

This proves a legal, rank-increasing and dimension-independent cost-Lipschitz exchange theorem for the two-resource gallery. Its bound does not force successive cost increases to cancel. The remaining open objective is to obtain a stronger color-compatible augmentation principle that keeps the final cost sublinear or bounded.

### Two-color Kneser stability and sharp middle-rank reachability bounds

#### 1. Uniform two-color Kneser upper bound

Let \(n=2k+1\), \(k\ge2\), and let \(\mathcal F\subseteq\binom{[n]}k\) be a vertex family whose induced disjointness graph in the Kneser graph \(KG(n,k)\) is bipartite.

**Theorem 1 (two-color Kneser bound).** Every such family satisfies
\[
\boxed{
|\mathcal F|\le
\max\left\{
\binom{2k}{k-1}+\binom{2k-1}{k-1},
\quad
2\binom{2k}{k-1}-2(k-1)
\right\}.
}
\tag{1}
\]
In particular the upper bound is \(7\) when \(n=5\), and \(26\) when \(n=7\).

*Proof.* A proper bipartition writes \(\mathcal F=\mathcal A\sqcup\mathcal B\), where \(\mathcal A\) and \(\mathcal B\) are disjoint intersecting families of \(k\)-subsets.

If \(\mathcal A\) has a common coordinate \(i\), it lies in the full star \(\mathcal S_i=\{S:i\in S\}\). Of the members of \(\mathcal B\), those also containing \(i\) lie in this star; those avoiding \(i\) form an intersecting family of \(k\)-subsets on \(2k\) points. Erdős–Ko–Rado bounds the latter by \(\binom{2k-1}{k-1}\). Thus
\[
|\mathcal F|\le|\mathcal S_i|+
|\{B\in\mathcal B:i\notin B\}|
\le\binom{2k}{k-1}+\binom{2k-1}{k-1}.
\]
The same argument applies with the classes reversed.

If neither color class has a common coordinate, the Hilton–Milner theorem bounds each by
\[
\binom{2k}{k-1}-\binom{k}{k-1}+1
=\binom{2k}{k-1}-k+1.
\]
Adding the two bounds proves (1). For empty classes, applying Erdős–Ko–Rado or Hilton–Milner to the nonempty class is no weaker. \(\square\)

**Corollary 2 (NORI1 middle-layer obstruction).** Let \(c\) be an antipodally odd undirected cube-edge coloring, and let \(R_x^\varepsilon\) be the coordinate subsets reachable from root \(x\) by a monochromatic geodesic of color \(\varepsilon\). If the coloring has no full monochromatic antipodal geodesic, then for every root \(x\),
\[
\mathcal F_x=(R_x^0\cup R_x^1)\cap\binom{[n]}k
\]
obeys (1). In particular \(|\mathcal F_x|\le7\) for \(Q_5\), and \(|\mathcal F_x|\le26\) for \(Q_7\).

*Proof.* Article VII's color-free reachability odd-cycle theorem shows that, absent a full monochromatic antipodal geodesic, the induced Kneser disjointness graph on \(\mathcal F_x\) must be bipartite: an edge joins two disjoint \(k\)-sets covering all but one coordinate, and two same-colored monochromatic arms at such endpoints would produce a monochromatic near-full geodesic, which extends to a full one by antipodal oddness. Every support incident to a disjointness edge then has a uniquely forced witness color, giving a proper bipartition. Apply Theorem 1. \(\square\)

The bound is necessary for a counterexample, not sufficient for a witness: a single rooted family may attain equality without any monochromatic geodesic of length \(n-1\) from that root.

#### 2. Sharpness and rigidity for dimensions five and seven

For \(n=5\), the union of the full stars of two distinct coordinates among two-element subsets has seven distinct members. Its disjointness graph is bipartite, assigning each support to one of the two stars, so the bound seven is sharp for the abstract Kneser problem.

For \(n=7\), partition the seven labels into a three-element set \(T\) and four-element set \(Q\), and fix \(q\in Q\). Put
\[
\begin{aligned}
\mathcal A&=\{S\in\tbinom{[7]}3:|S\cap T|\ge2\},\\
\mathcal B&=\{S\in\tbinom{[7]}3:q\in S,\ 
S\cap(Q\setminus\{q\})\ne\varnothing\}\cup\{Q\setminus\{q\}\}.
\end{aligned}
\tag{2}
\]
These are disjoint intersecting families, each of cardinality thirteen. Therefore their union realizes the upper bound twenty-six.

**Theorem 3 (classification of sharp seven-point Kneser families).** Every induced-bipartite family \(\mathcal F\subseteq\binom{[7]}3\) of size twenty-six admits a bipartition into two disjoint thirteen-element nontrivial intersecting families. Up to relabeling, there are precisely two possibilities:
\[
\begin{array}{ll}
\text{(I)}&J(T)\sqcup J(U),\quad T\cap U=\varnothing;\\
\text{(II)}&H(c;T)\sqcup J([7]\setminus(T\cup\{c\})),
\end{array}
\tag{3}
\]
where
\[
J(T)=\{S\in\tbinom{[7]}3:|S\cap T|\ge2\},\qquad
H(c;T)=\{T\}\cup\{\{c,a,b\}:\{a,b\}\cap T\ne\varnothing\},
\]
with \(|T|=3\) and \(c\notin T\). There are seventy labeled unordered pairs of type (I) and one hundred forty of type (II), for a total of
\[
\boxed{210\text{ labeled extremal pairs, in two permutation orbits}.}
\tag{4}
\]

*Proof.* The common-coordinate case in Theorem 1 gives at most \(15+10=25\), so a twenty-six-member family must have two nontrivial intersecting color classes. Hilton–Milner bounds each by thirteen, hence each attains equality.

The equality classification for nontrivial intersecting triple families on seven labels has two forms: the triangle-majority family \(J(T)\), or the canonical Hilton–Milner family \(H(c;T)\). Both have thirteen members, and there are respectively \(\binom73=35\) and \(7\binom63=140\) labeled families.

Two majority families \(J(T),J(U)\) are disjoint precisely when the indexing triples \(T,U\) are disjoint. Indeed, if \(T\cap U\ne\varnothing\), choose two points of \(T\) and two of \(U\), using their shared point so that the resulting three-element set has at least two in each. Conversely, no three-set can contain two elements from each of disjoint three-sets. Thus the number of unordered disjoint majority pairs is \(\binom73\binom43/2=70\).

A canonical family \(H(c;T)\) is disjoint from a majority family \(J(U)\) precisely when \(U=[7]\setminus(T\cup\{c\})\). If \(U\) avoids the four-point set \(T\cup\{c\}\), members of \(H(c;T)\) contain at most one point of \(U\). Conversely, if \(U\) contains two points of \(T\), it lies with a suitable third point in \(J(U)\cap H(c;T)\); if \(U\) contains \(c\) and any point of \(T\), choose a triple containing both and a further point of \(U\); the remaining configurations likewise supply a triple of \(H(c;T)\) with two members of \(U\). Hence there is one disjoint majority family for each of the \(140\) canonical families.

Two canonical families cannot be disjoint. If their centers coincide, a triple containing the center and meeting both exceptional triples belongs to both. If their centers \(c,d\) differ, a triple \(\{c,d,a\}\) belongs to both provided \(\{d,a\}\) meets the first exceptional triple and \(\{c,a\}\) meets the second. Such \(a\) exists unless both exceptional triples are disjoint and exclude both centers, which is impossible for distinct \(c,d\) on seven labels. This proves the two types and their counts. \(\square\)

The sharp configuration classification describes a **single root's** Kneser layer only. It does not imply the global existence of a counterexample to NORI1.

Let \(G=(V,E)\) be a finite simple graph with at least one edge, and let \(N\) be a matroid on \(E\). Assume
\[
\tag{1}
\mathcal I(N)\subseteq\mathcal I(M(G)),\qquad
\delta_G(v)\in\mathcal I(N)\quad(v\in V),
\]
where \(M(G)\) is the graphic matroid and \(\delta_G(v)\) is the star at \(v\). At each vertex \(v\), prescribe an arbitrary tournament \(T_v\) on \(\delta_G(v)\). A vertex word \(P=(v_1,\ldots,v_\ell)\) is an *independent tournament path* when its consecutive edges are pairwise distinct, their set is independent in \(N\), and
\[
v_{i-1}v_i\longrightarrow v_iv_{i+1}\quad\text{in }T_{v_i}
\qquad(2\le i<\ell).
\]
Condition (1) implies that an independent tournament path has distinct vertices. Indeed, a closed subwalk with pairwise distinct edges contains a graph cycle, contradicting independence in \(N\).

**Theorem (matroid terminal-growth bound).** Let \(L\) be the maximum number of vertices in an independent tournament path, and let \(\bar d=2|E|/|V|\). Then
\[
\boxed{\quad\frac{\bar d}{2}\le(L-1)^2,\qquad
L\ge1+\sqrt{\frac{\bar d}{2}}.\quad}\tag{2}
\]
The bound holds for arbitrary matroids \(N\), including nonrepresentable matroids.

*Proof.* For every \(e=uv\in E\), let \(r(e)\) be the maximum order of an independent tournament path ending in either \(u,v\) or \(v,u\). Orient \(e\) toward the last vertex of one maximizing path. Some vertex \(v\) receives at least \(\bar d/2\) oriented edges. For \(2\le r\le L\), write \(D_r(v)\) for the incoming edges with \(r(e)=r\), and let \(q=|D_r(v)|\).

For \(q>0\), choose \(e=uv\in D_r(v)\) which beats at least \((q-1)/2\) other members of \(D_r(v)\) in \(T_v\). Let \(P\) be an independent tournament path of order \(r\) ending in \(u,v\), and put \(A=E(P)\). Then \(r_N(A)=r-1\). If \(f=vw\in D_r(v)\) is beaten by \(e\) and \(f\notin\operatorname{cl}_N(A)\), the word obtained by appending \(w\) to \(P\) has independent edge set \(A\cup\{f\}\). By (1), this set is a forest; consequently \(w\) is new to \(P\). The tournament comparison at \(v\) is legal, so the new word is an independent tournament path of order \(r+1\), contradicting \(r(f)=r\).

Thus every member of \(D_r(v)\) beaten by \(e\) belongs to \(\operatorname{cl}_N(A)\). Since \(\delta_G(v)\) is independent in \(N\),
\[
\bigl|\delta_G(v)\cap\operatorname{cl}_N(A)\bigr|
\le r_N(A)=r-1.
\]
One of these edges is \(e\). Hence \((q-1)/2\le r-2\), giving \(q\le2r-3\). Summing over terminal ranks yields
\[
\frac{\bar d}{2}\le d^-(v)
=\sum_{r=2}^{L}|D_r(v)|
\le\sum_{r=2}^{L}(2r-3)
=(L-1)^2.
\]
This proves (2). \(\square\)

**Transitive refinement.** If every \(T_v\) is transitive, then
\[
\boxed{\quad \bar d\le L(L-1),\qquad
L-1\ge\frac{\sqrt{1+4\bar d}-1}{2}.\quad}\tag{3}
\]

*Proof.* In the preceding proof, the tournament induced on \(D_r(v)\) has a vertex beating all \(q-1\) others. Thus \(q-1\le r-2\), so \(q\le r-1\). Summing gives
\[
\bar d/2\le\sum_{r=2}^{L}(r-1)=L(L-1)/2.
\]
Solving this quadratic proves (3). \(\square\)

**Corollary 1 (ordinary reversal-odd boundary tournaments).** Let \(b(a,v,c)\in\{0,1\}\) satisfy \(b(c,v,a)=1-b(a,v,c)\) on distinct triples from an \(n\)-element set. Take \(G=K_n\), \(N=M(K_n)\), and orient the local tournament \(T_v\) by
\[
av\longrightarrow vc\quad\Longleftrightarrow\quad b(a,v,c)=1.
\]
Every independent tournament path is a vertex-simple monochromatic tight path of color one, and conversely. Thus there is such a path on at least
\[
\boxed{1+\sqrt{(n-1)/2}}\tag{4}
\]
vertices, with integer rounding understood.

*Proof.* Every vertex star of \(K_n\) is a forest, hence independent in its graphic matroid. The condition on \(b\) says precisely that the comparisons at each vertex form a tournament. Along an independent tournament path every triple color is one; ordinary graph paths have independent edge sets in \(M(K_n)\). Apply the theorem with \(\bar d=n-1\). \(\square\)

**Corollary 2 (cube geodesics with at most one switch).** For every binary coloring \(c\) of the edges of \(Q_n\), there exists a coordinate-distinct geodesic of length at least
\[
\boxed{\left\lceil\frac{\sqrt{4n+1}-1}{2}\right\rceil}\tag{5}
\]
whose edge-color word is weakly increasing. In particular it has at most one color change, and this applies to every NORI1 coloring.

*Proof.* On \(E(Q_n)\), let \(N\) be the partition matroid with capacity one in each parallel-coordinate class. Its independent edge sets use each direction at most once, hence contain no graph cycle. At each cube vertex, the \(n\) incident edges use distinct directions, so the whole star is independent. Order each local star with all color-zero edges preceding color-one edges, resolving ties arbitrarily, and let \(T_v\) be the resulting transitive tournament. A path independent in \(N\) uses distinct coordinate directions and is therefore a geodesic. Along every admissible path, the colors are weakly increasing. The chosen local tournaments are transitive, so apply (3) with \(\bar d=n\). \(\square\)

The common mechanism is a rank obstruction to extending a maximum terminal path: a rank-\((r-1)\) flat meets an independent vertex star in at most \(r-1\) edges. In the boundary model, the resource matroid is graphic. In the cube model, it is a coordinate partition matroid subordinate in independence to the graphic matroid of the cube. This supplies one intrinsic matroidal proof of the square-root scale in both models and improves the weaker proper-label cube estimate obtained by separately charging repeated vertices and directions. The passage from a partial low-switch cube geodesic to a full monochromatic antipodal geodesic remains open; (1) alone does not encode antipodal color polarization.

### Fundamental-circuit pivots, dual-basis sweeps, and faithful ordered exchanges

Let \(M\) be a finite loopless matroid on \(E\), and let \(\Gamma(M)\) denote its basis-exchange graph. For an oriented edge \(B\to B'=B-a+e\), let \(C_M(e,B)\) be the fundamental circuit of \(e\) with respect to \(B\). The circuit contains \(a,e\), since replacing \(a\) by \(e\) gives a basis.

**Theorem 1 (canonical pivot of a small fundamental circuit).** Suppose every circuit of \(M\) has cardinality at most three. Each oriented basis exchange \(B\to B-a+e\) admits a unique intrinsic label of one of the following types:
\[
\begin{array}{ll}
\text{parallel exchange:}& C_M(e,B)=\{a,e\};\\
\text{triangular exchange:}& C_M(e,B)=\{a,b,e\},\quad
b\in B\cap B'.
\end{array}
\tag{1}
\]
In the triangular case the ordered triple \((a,b,e)\) is determined by the oriented exchange and the matroid. Reversing the exchange changes it to \((e,b,a)\). The labels are preserved by every matroid isomorphism.

*Proof.* The element \(e\) is outside \(B\), and a fundamental circuit contains \(e\) together with at least one element of \(B\). Because \(B-a+e\) is independent, \(a\) is in this circuit. The size bound gives the two displayed possibilities; in the size-three case the third element \(b\) belongs to \(B\setminus\{a\}=B\cap B'\). Fundamental circuits are unique. For the reverse exchange \(B'\to B\), the fundamental circuit of \(a\) with respect to \(B'\) is the same circuit: its removal of \(e\) restores the basis, and its removal of \(b\) also yields a basis by the fundamental-circuit exchange criterion. The description is matroid-theoretic and therefore commutes with isomorphisms. \(\square\)

The theorem identifies the local middle element of a boundary triple as a *fundamental-circuit pivot*. It also identifies a cubical coordinate exchange with a two-element fundamental circuit. No auxiliary ordering of the retained basis elements is used in either case.

**Theorem 2 (faithfulness rigidity for uniform sliding windows).** Fix \(1\le r<n\). Map an injective ordered \((r+1)\)-tuple
\[
(a,x_1,\ldots,x_{r-1},e)
\]
to the oriented basis exchange
\[
\{a,x_1,\ldots,x_{r-1}\}
\longrightarrow
\{x_1,\ldots,x_{r-1},e\}
\tag{2}
\]
of \(U_{r,n}\). Every oriented edge of \(\Gamma(U_{r,n})=J(n,r)\) has precisely \((r-1)!\) preimages. Hence an oriented exchange determines its ordered sliding window if and only if \(r\le2\).

For \(r=2\), arbitrary reversal-odd boundary 3-tournaments on \([n]\) are in bijection with orientations of \(J(n,2)\): orient the edge
\[
\{a,b\}\longrightarrow\{b,e\}
\]
when \(b(a,b,e)=1\). Every orientation of \(J(n,2)\) arises. For \(r\ge3\), some reversal-odd ordered-\((r+1)\)-window colorings cannot descend to orientations of the basis-exchange graph.

*Proof.* The ordered source and target bases in (2) recover \(a\) as their deleted element, \(e\) as their inserted element, and the unordered set \(X=B\cap B'\) of their \(r-1\) retained elements. The preimages are precisely the permutations of \(X\). This gives the factorial and the characterization \(r\le2\). When \(r=2\), the sole retained element is \(b\), and reversing the graph edge reverses \((a,b,e)\). Thus the reversal-odd identity specifies one orientation of each undirected graph edge with no further compatibility conditions. When \(r\ge3\), choose two different permutations of \(X\) and give their windows different binary colors; assign the complementary colors to their reversed windows, then fill the remaining reversal orbits arbitrarily. The coloring is reversal-odd but assigns different colors to the same directed exchange, so it does not descend. \(\square\)

**Theorem 3 (dual-basis permutation sweeps).** In both canonical models the colored states along a complete path admit distinct intrinsic resource labels forming one basis of the dual matroid.

(i) Let \(M=\bigoplus_{i=1}^kU_{1,2}\). Every dual basis \(D\) has complementary primal basis \(B=E\setminus D\). For each permutation \(d_1,\ldots,d_k\) of \(D\), let \(B_j\) arise from \(B_{j-1}\) by exchanging its element parallel to \(d_j\) for \(d_j\). Then
\[
B=B_0,B_1,\ldots,B_k=D
\tag{3}
\]
is an antipodal geodesic of the \(k\)-cube. Its \(k=r(M^*)\) exchange edges have distinct two-element-circuit labels indexed by \(D\); every antipodal geodesic from \(B\) is obtained from one such permutation.

(ii) Let \(M=U_{2,n}\), \(n\ge3\). Every dual basis \(D\) has complementary primal basis \(\{s,t\}\). For each permutation \(d_1,\ldots,d_{n-2}\) of \(D\), the word
\[
(s,d_1,\ldots,d_{n-2},t)
\tag{4}
\]
defines a path in \(J(n,2)\) through its consecutive unordered pairs. Its \(n-2=r(M^*)\) oriented exchanges are labeled, in order, by the distinct triangular-circuit pivots \(d_1,\ldots,d_{n-2}\). Conversely, the original-element Hamiltonian tight words with endpoints \(s,t\) are precisely (4).

In both instances, the reversal operation on complete paths acts on the corresponding color words by
\[
w\longmapsto\overline{\operatorname{rev}(w)}.
\tag{5}
\]

*Proof.* The complement of a primal basis is a dual basis. In (i), each \(d_j\) belongs to a different parallel pair, so all exchanges are legal and no pair is toggled twice. A path from \(B\) to \(E\setminus B\) has length at least \(k\), and equality forces every pair to be toggled once. In (ii), consecutive unordered pairs of the displayed word intersect in the single middle element; every pair is a basis and every original vertex appears once. The ordered-triple labels are its successive windows, whose middle elements are precisely the members of \(D\). Conversely, a Hamiltonian tight word determines its two endpoints and the order of its interior elements. The reversal of a boundary word reverses and complements each triple label by reversal oddness. For the cube, reverse the geodesic and apply the canonical complementation map to every basis; the antipodal odd edge rule complements the reversed sequence of edge colors. This proves (5). \(\square\)

**Corollary 4 (the common resource parameter).** The natural number of primitive colored states of a complete gallery is
\[
\boxed{r(M^*)=|E(M)|-r(M)}
\tag{6}
\]
in both canonical models: \(k\) for the cube and \(n-2\) for the boundary tournament. The canonical exchange label is an inserted element in (i) and a retained fundamental-circuit pivot in (ii). For uniform rank \(r\ge3\), the underlying oriented basis-exchange graph alone loses \((r-1)!\)-fold ordered-window information.

This identifies a common matroidal resource budget and a choice-free source of its local exchange labels. It leaves two additional ingredients to a path-existence theorem: a compatible global polarity of colored exchange states, and a rank-increasing exchange rule that preserves a coherent path with distinct resources. In the cube the antipode acts on bases; in uniform rank two, reversal acts on directed exchanges. The two actions have different domains, and the colored signed-cover matroid requires the additional gallery information developed elsewhere in Article XI.

Let \(M\) be a finite matroid of rank \(r\ge1\) on a ground set \(E\), with \(N=|E|\). Write \(\mathcal B(M)\) for its bases and \(\mathcal I_{r-1}(M)\) for its independent \((r-1)\)-sets. For each \(1\le j\le N-r\), choose an arbitrary binary coloring \(\beta_j\) of the oriented edges of the basis-exchange graph, satisfying
\[
\beta_j(B',B)=1-\beta_j(B,B')\qquad(B,B'\text{ adjacent}).\tag{1}
\]
A **sliding-window gallery** of order \(m\) is an injective word \(v_1,\ldots,v_m\), \(m\ge r\), for which each consecutive \(r\)-set
\[
B_i=\{v_i,\ldots,v_{i+r-1}\},\qquad1\le i\le m-r+1,
\]
is a basis. The gallery is **positive** if \(\beta_i(B_i,B_{i+1})=1\) for \(1\le i\le m-r\). The stage colorings \(\beta_i\) may vary independently.

**Theorem (terminal-set growth).** Let \(L\) be the maximum order of a positive sliding-window gallery. Then
\[
\boxed{|\mathcal B(M)|\le|\mathcal I_{r-1}(M)|(L-r+1)^2,\qquad
L\ge r-1+\sqrt{\frac{|\mathcal B(M)|}{|\mathcal I_{r-1}(M)|}}.}\tag{2}
\]
The conclusion requires neither representability nor simplicity nor an edge ordering.

*Proof.* Every basis supports a gallery of order \(r\), with no colored transitions. For each basis \(B\), let \(\ell(B)\) be the maximum order of a positive gallery terminating with the \(r\)-set \(B\). Choose such a gallery with final word \(x,s_1,\ldots,s_{r-1}\), and assign \(B\) to the independent set \(S=\{s_1,\ldots,s_{r-1}\}\). 

Fix an independent \((r-1)\)-set \(S\), an integer \(s\in\{r,\ldots,L\}\), and put
\[
U_{S,s}=\{x\notin S:S\cup\{x\}\text{ was assigned to }S,\ \ell(S\cup\{x\})=s\},\qquad q=|U_{S,s}|.
\]
If \(s=N\), then \(q\le N-r+1\le 2(s-r)+1\), so (3) follows immediately. Suppose henceforth that \(s<N\). The bases \(S\cup\{x\}\), \(x\in U_{S,s}\), form a complete exchange clique. Equation (1) makes \(\beta_{s-r+1}\) a tournament on this clique. Choose \(x\) having at least \((q-1)/2\) outgoing comparisons of color one. The selected \(s\)-element gallery for \(S\cup\{x\}\) ends in \(x,s_1,\ldots,s_{r-1}\). If an outgoing neighbor \(y\in U_{S,s}\) did not already occur in the gallery, appending \(y\) would preserve distinctness, add the valid basis window \(S\cup\{y\}\), and fulfill the prescribed positive stage comparison. This would give \(\ell(S\cup\{y\})\ge s+1\), a contradiction. Thus all favorable neighbors occur among the earlier \(s-r\) vertices, and
\[
(q-1)/2\le s-r,\qquad |U_{S,s}|\le2(s-r)+1.\tag{3}
\]
The number of bases assigned to \(S\) is at most
\[
\sum_{s=r}^{L}(2(s-r)+1)=(L-r+1)^2.
\]
Summing over all \(S\in\mathcal I_{r-1}(M)\) gives (2). \(\square\)

**Corollary 1 (uniform matroids of every rank).** For \(1\le r<n\), every reversal-odd coloring of oriented exchanges of \(U_{r,n}\) admits a positive injective sliding-window gallery with
\[
\boxed{L\ge r-1+\sqrt{\frac{n-r+1}{r}}.}\tag{4}
\]
The assertion remains valid for independently chosen reversal-odd colorings at every stage.

*Proof.* In \(U_{r,n}\), all \(r\)-sets are bases and all \((r-1)\)-sets are independent, so
\[
|\mathcal B|/|\mathcal I_{r-1}|=\binom nr/\binom n{r-1}=(n-r+1)/r.
\]
Apply (2). \(\square\)

When \(r=2\), \(S=\{b\}\) and the oriented exchange \(S\cup\{a\}\to S\cup\{c\}\) is the ordered triple \((a,b,c)\). Thus (4) is \(L\ge1+\sqrt{(n-1)/2}\), recovering the Devine--Milans terminal-pair theorem for every ordinary reversal-odd boundary 3-tournament. Its stage-dependent version recovers the layered terminal-pair extension in Article VII. For every fixed \(r\), (4) is a square-root lower bound with distinct original resources. The complete exchange clique above a codimension-one independent set is the shared local mechanism.

**Corollary 2 (cubical specialization and its limitation).** Let \(M_n=\bigoplus_{i=1}^nU_{1,2}\), so its basis graph is \(Q_n\). Designate one element in each parallel pair as zero, and let \(\varepsilon(B)\) count the other selected elements modulo two. For an arbitrary undirected-edge coloring \(c\) of \(Q_n\), define the stage-dependent oriented coloring
\[
\boxed{\beta_j(B,B')=c(\{B,B'\})+\varepsilon(B)+(j-1)\pmod2.}\tag{5}
\]
Every positive sliding-window gallery for (5) induces a monochromatic cube geodesic, using \(m-n\) different directions if the gallery has order \(m\).

*Proof.* Each basis window of length \(n\) chooses one element of every parallel pair. When the window shifts, its entering element must be the parallel mate of the departing element. The injective word therefore exchanges every pair at most once, so the basis windows trace a geodesic. Every basis exchange changes \(\varepsilon\) by one, giving \(\beta_j(B',B)=1-\beta_j(B,B')\). Along the gallery, \(\varepsilon(B_j)=\varepsilon(B_1)+(j-1)\), whence
\[
\beta_j(B_j,B_{j+1})=c(\{B_j,B_{j+1}\})+\varepsilon(B_1).
\]
Positivity makes the traversed cube edges monochromatic. \(\square\)

For this cubical matroid, however,
\[
\frac{|\mathcal B(M_n)|}{|\mathcal I_{n-1}(M_n)|}
=\frac{2^n}{n2^{n-1}}=\frac2n.\tag{6}
\]
Therefore (2) offers no guaranteed positive exchange beyond the initial basis window, whereas a full antipodal geodesic requires gallery order \(2n\). In contrast, the ratio for \(U_{2,n}\) is \((n-1)/2\). The terminal-set method gives a common witness predicate and proves the tournament square-root estimate, while (6) pinpoints its inability to force the spanning cubical witness. A unified spanning theorem must supply an additional global exchange or antipodal-splicing principle beyond the terminal-set tournament comparison.

**Corollary 3 (parallel-factor law for terminal capacity).** For a loopless partition matroid \(M=\bigoplus_{j=1}^tU_{r_j,m_j}\) with \(r_j\ge1\), the terminal-set ratio in (2) obeys
\[
\boxed{\frac{|\mathcal B(M)|}{|\mathcal I_{r-1}(M)|}
=\left(\sum_{j=1}^{t}\frac{r_j}{m_j-r_j+1}\right)^{-1}.}\tag{7}
\]
*Proof.* An independent \((r-1)\)-set is obtained by choosing \(r_j-1\) elements in one summand \(j\) and bases in all others. Therefore
\[
|\mathcal I_{r-1}(M)|
=\sum_j \binom{m_j}{r_j-1}\prod_{\ell\ne j}\binom{m_\ell}{r_\ell}.
\]
Divide by \(|\mathcal B(M)|=\prod_\ell\binom{m_\ell}{r_\ell}\), and use \(\binom{m_j}{r_j-1}/\binom{m_j}{r_j}=r_j/(m_j-r_j+1)\). \(\square\)

The reciprocal terminal capacity is additive under direct sums. Thus the uniform rank-two model has one large rank-one contraction fiber, producing a square-root gain, whereas the cubical model has \(n\) small contraction fibers whose reciprocal contributions add to \(n/2\). This formula expresses quantitatively why terminal-fiber growth by itself cannot recover the cube's full antipodal geodesic.

### Intrinsic largest-clique incidence roots and a terminal-tournament path theorem

Let \(M\) be a finite matroid, let \(\Gamma(M)\) be its basis-exchange graph, and let \(\mathscr K(M)\) be the family of cliques of **maximum cardinality** in \(\Gamma(M)\). Construct the canonical bipartite incidence graph
\[
I(M)=\bigl(\mathcal B(M)\sqcup\mathscr K(M),\ \{BK:B\in K\}\bigr).
\]
An incidence side is called *thin* when every vertex on that side has degree two. Whenever \(I(M)\) is the edge-subdivision of a connected simple graph, denote the graph obtained by suppressing its thin side by \(G(M)\). This construction uses only the basis graph and its maximum cliques; it is invariant under matroid isomorphism.

#### Theorem 1 (three intrinsic root reconstructions)

For \(n\ge3\) and \(m\ge3\), the following matroids have thin incidence sides and root graphs:
\[
\begin{array}{c|c|c|c}
M&\Gamma(M)&\text{thin side}&G(M)\\ \hline
\bigoplus_{i=1}^n U_{1,2}&Q_n&\mathscr K(M)&Q_n\\
U_{2,n},\ n\ge5&J(n,2)&\mathcal B(M)&K_n\\
U_{1,m}\oplus U_{1,m}&K_m\square K_m&\mathcal B(M)&K_{m,m}.
\end{array}
\]

**Proof.** The first basis graph is the cube \(Q_n\). Because it is triangle-free, its largest cliques are its edges, each incident with two basis vertices. Thus \(I(M)\) is the edge subdivision of \(Q_n\), with the clique side thin.

For \(U_{2,n}\), bases are unordered pairs \(\{a,b\}\) and adjacent when they share a symbol. Its basis graph is \(J(n,2)=L(K_n)\). Every clique of size at least four consists of pairs sharing a single symbol; the other maximal cliques consist of the three edges of a triangle. For \(n\ge5\), the largest cliques are therefore the \(n\) stars
\[
K_a=\{\{a,b\}:b\ne a\},\qquad a\in[n].
\]
Each basis \(\{a,b\}\) lies in precisely \(K_a,K_b\). Suppressing the basis vertices of \(I(M)\) gives \(K_n\).

For \(U_{1,m}\oplus U_{1,m}\), bases are ordered pairs \((i,j)\in[m]^2\), and exchange replaces one coordinate. The basis graph is \(K_m\square K_m\). Its \(2m\) largest cliques are its rows and columns, and each basis lies in one of each. The incidence root is \(K_{m,m}\). \(\square\)

For any **basis-side thin** instance with a simple root \(G(M)\), the edge \(uv\) of \(G(M)\) is the unique basis \(B\) belonging to the two clique vertices \(u,v\). If two edges of \(G(M)\) meet at \(v\), their bases both lie in the clique \(v\), hence are adjacent in \(\Gamma(M)\). Thus every orientation of the corresponding basis-exchange edges induces a tournament on the incident root edges at \(v\). The restriction is canonical under basis-graph isomorphism and permits cyclic local tournaments.

#### Theorem 2 (terminal-tournament path transfer)

Suppose \(M\) has a basis-side thin incidence graph with connected simple root \(G=G(M)\). Orient the edges of \(\Gamma(M)\) arbitrarily. Then \(G\) admits a vertex-simple path \(v_1,\dots,v_L\) whose successive root edges are locally increasing at every common vertex:
\[
(v_iv_{i+1})\longrightarrow(v_{i+1}v_{i+2})
\]
in the induced tournament on the edges incident with \(v_{i+1}\), for every \(i\). Moreover
\[
\boxed{\ \frac{\overline d(G)}2\le (L-1)^2\ },\qquad
L\ge 1+\sqrt{\frac{\overline d(G)}2},
\]
where \(\overline d(G)=2|E(G)|/|V(G)|\). In particular, for \(M=U_{2,n}\), every arbitrary reversal-odd boundary \(3\)-tournament admits a monochromatic vertex-simple tight path on at least \(1+\sqrt{(n-1)/2}\) original vertices.

**Proof.** The root's tournament comparisons are induced by the given basis-graph orientation. Let \(L\) be the maximum order of a vertex-simple positively directed path. For each edge \(e\) of \(G\), let \(\ell(e)\) be the maximum order of a positively directed vertex-simple path ending with \(e\), in either direction. Choose a maximizing path and orient \(e\) toward its terminal vertex. Some root vertex \(v\) receives at least \(\overline d(G)/2\) such chosen orientations.

For \(2\le r\le L\), let \(S_r\) be the set of incoming edges \(uv\) with \(\ell(uv)=r\), and put \(s_r=|S_r|\). The tournament induced among the \(s_r\) edges has an edge with at least \((s_r-1)/2\) outneighbors. Choose its witness path of order \(r\) ending \(uv\). Every outneighbor edge \(vw\) with \(w\) outside that witness path would extend it to a positive vertex-simple path of order \(r+1\), contradicting \(\ell(vw)=r\). Apart from the previous vertex \(u\), at most \(r-2\) original vertices are unavailable. Hence
\[
(s_r-1)/2\le r-2,\qquad s_r\le 2r-3.
\]
Summing gives
\[
\frac{\overline d(G)}2\le\deg^-(v)=\sum_{r=2}^{L}s_r
\le\sum_{r=2}^{L}(2r-3)=(L-1)^2.
\]
For \(U_{2,n}\), the reconstruction gives \(G=K_n\) and \(\overline d(G)=n-1\); an arbitrary orientation of each Johnson star encodes an arbitrary reversal-odd middle-vertex tournament. Root vertex-simplicity is the distinct-symbol condition for the corresponding tight path. \(\square\)

#### Interpretation and limitation

Both initial matroids lie in the intrinsic class for which the largest-clique incidence graph is a subdivision of a simple graph. Their thin sides, however, differ. In the rank-two uniform family, bases become *edges* of the root and their overlapping exchanges define arbitrary local tournaments. In the cubical family, largest cliques become *edges* of the root; the original two-color antipodal condition belongs to the root-edge data, with the coordinate classes recoverable from opposite edges of its squares.

Thus Theorem 2 supplies the quantitative square-root mechanism for the boundary family, while the cubical instance instead falls under the properly resource-labeled terminal-path theorem already established in Article VII. The latter provides a coordinate-distinct increasing geodesic of order at least \((5+\sqrt{1+4n})/4\), after locally ordering the two edge colors, but does not yield a full monochromatic antipodal geodesic. The incidence reconstruction is a common intrinsic geometry, not yet a unified full-strength existence conjecture.

The condition alone also does not force one-switch spanning paths: the matroid \(U_{1,3}\oplus U_{1,3}\) lies in the class and has root \(K_{3,3}\); a nine-edge globally ordered tournament instance admits no Hamilton path with at most one change of turn-color (see the scoped research note 'Rook-graph counterexample to incidence-gallery one-switch spanning'). Any stronger common conjecture needs additional intrinsic assumptions encoding the relevant endpoint and resource conditions.

#### Theorem 3 (a root-basis filter excluding the rook family)

The property that \(G(M)\) is itself a matroid basis-exchange graph is invariant under matroid isomorphism. It holds in the first two rows of Theorem 1, since \(Q_n=\Gamma(\bigoplus U_{1,2})\) and \(K_n=\Gamma(U_{1,n})\). It fails in the third row for **every** \(m\ge3\): \(K_{m,m}\) cannot be a matroid basis graph.

**Proof.** In a matroid basis graph, suppose bases \(B,D\) are at distance two. Write \(B=S\cup\{a,b\}\) and \(D=S\cup\{c,d\}\), with the four indicated elements distinct. Every common neighbor of \(B\) and \(D\) is among
\[
S\cup\{a,c\},\quad S\cup\{a,d\},\quad
S\cup\{b,c\},\quad S\cup\{b,d\}.
\]
Those four possible common neighbors induce, when all are bases, a \(4\)-cycle: neighboring sets share three of the four displayed exchange elements; opposite sets differ by two. Thus a distance-two pair in a basis graph has at most four common neighbors, and no three of them can be pairwise nonadjacent. In \(K_{m,m}\), any two vertices from one part are at distance two and have \(m\) pairwise nonadjacent common neighbors. For \(m\ge5\), their number alone is impossible; for \(m=3,4\), their independence is impossible. \(\square\)

Consequently the class
\[
\mathcal C_{\mathrm{root}}=
\{M:I(M)\text{ is a simple connected edge subdivision with a thin side,
and }G(M)\text{ is itself a matroid basis graph}\}
\]
is defined from the matroid without reference to either target problem, contains both canonical families, and excludes the entire rook family. Theorems 1–2 remain valid within this refinement. No full-strength one-switch or antipodal-geodesic guarantee for this refined class has been established.

#### Theorem 4 (triangle-free matroid basis graphs are cubical)

If the basis-exchange graph of a finite matroid \(M\) is triangle-free, then, up to loops and coloops, \(M\) is a direct sum of copies of \(U_{1,2}\). Conversely, every such direct sum has triangle-free basis graph. In particular, a connected triangle-free basis-exchange graph is a hypercube.

**Proof.** Fix a basis \(B\). For any nonloop \(e\notin B\), its fundamental circuit \(C_B(e)\) must contain precisely one element \(b\in B\): if it contained two distinct basis elements \(b,b'\), then \(B-b+e\) and \(B-b'+e\) would both be bases adjacent to \(B\) and to one another, forming a triangle. Therefore each nonloop element outside \(B\) is parallel to a unique element of \(B\). Every nonloop belongs to one of the parallel classes indexed by \(B\), and \(M\) is the direct sum of rank-one uniform matroids on those classes. A class of three or more elements yields three pairwise adjacent bases by independently choosing one member, again forming a triangle. Each nontrivial parallel class consequently has size two. Conversely, replacing either member in any two-element parallel class independently gives the cube graph. \(\square\)

This classification shows that the triangle-free incidence branch has rigid intrinsic matroid structure. An extension claiming that the cube and the uniform rank-two models share a nontrivial self-dual *basis-vertex* polarity must still confront their distinct automorphism-equivariance properties, as recorded in the canonical-polarity obstruction note.

**A nonuniform member of the refined class.** Let \(M\) be the rank-two matroid on six elements with three parallel classes of size two. Its bases are the two-element sets meeting distinct parallel classes, and its basis graph is \(L(K_{2,2,2})\). Every vertex of \(K_{2,2,2}\) has degree four, so the largest cliques of this line graph are its stars (size four), exceeding its triangle cliques (size three). Consequently the largest-clique incidence root is \(G(M)=K_{2,2,2}\). This root is isomorphic to \(J(4,2)=\Gamma(U_{2,4})\): partition the six two-element subsets of a four-element set into three complementary pairs; precisely the complementary pairs are nonadjacent in \(J(4,2)\). Hence \(M\in\mathcal C_{\mathrm{root}}\), despite being neither a uniform rank-two matroid nor a direct sum of rank-one two-element matroids. This demonstrates that the filter defines a class broader than the two motivating matroids.

Let \(M=\bigoplus_{j=1}^{t}U_{r_j,m_j}\) be a loopless partition matroid decomposed into its connected matroid components, with \(1\le r_j<m_j\) or \(r_j=m_j=1\) (singleton coloops). Let its component ground sets be \(E_j\), and put \(r=\sum_jr_j\), \(N=\sum_jm_j\). A **resource-simple sliding-window gallery** of order \(m\) is an injective word \(w_1,\ldots,w_m\), \(m\ge r\), such that every consecutive length-\(r\) set \(B_i=\{w_i,\ldots,w_{i+r-1}\}\) is a basis. Its exchanged basis arcs are \(B_i\to B_{i+1}\).

**Theorem (periodic component strands).** A word of distinct ground elements with a basis as its initial length-\(r\) window is a resource-simple sliding-window gallery if and only if
\[
\boxed{w_i\text{ and }w_{i+r}\text{ belong to the same connected component of }M}
\quad(1\le i\le m-r).\tag{1}
\]
Thus every gallery decomposes into \(r\) strands indexed by positions modulo \(r\); each strand stays inside one connected component. Conversely every such component schedule can be realized by choosing distinct elements in the prescribed components, subject only to their cardinalities.

*Proof.* The \(i\)-th basis window contains \(r_j\) elements of block \(E_j\) for every \(j\). The next window deletes \(w_i\) and inserts \(w_{i+r}\). Since all block counts must be preserved, both belong to the same block. This proves necessity. Conversely, if the entering and departing elements always belong to the same block, each transition preserves the block counts \(r_j\). By induction every length-\(r\) window is a basis, proving sufficiency. Distinctness gives a resource-simple gallery. \(\square\)

**Theorem (resource-capacity formula).** Fix a nonnegative integer \(q\), the proposed number of successive basis exchanges, and write
\[
q=ar+s,\qquad a\ge0,\quad 0\le s<r.
\]
A resource-simple sliding-window gallery with \(q\) exchanges (word order \(r+q\)) exists if and only if both
\[
\boxed{m_j\ge(a+1)r_j\text{ for every }j,}\tag{2}
\]
and
\[
\boxed{\sum_{j=1}^{t}\min\{r_j,m_j-(a+1)r_j\}\ge s.}\tag{3}
\]
In particular, these conditions compute the maximum uncolored resource-simple gallery length for every partition matroid in all ranks.

*Proof.* Choose the initial length-\(r\) block schedule with \(r_j\) positions labeled \(j\). By (1) the block schedule repeats with period \(r\). In the first \(r+q=(a+1)r+s\) positions, each block \(j\) occurs \((a+1)r_j+t_j\) times, where \(t_j\) is the number of labels \(j\) among the first \(s\) positions of the initial period. We have \(0\le t_j\le r_j\), \(\sum_jt_j=s\). Distinct resources can be chosen if and only if \((a+1)r_j+t_j\le m_j\) for each \(j\). Such integers \(t_j\) exist precisely under (2) and (3). Indeed, (3) says the available nonnegative prefix capacities \(\min\{r_j,m_j-(a+1)r_j\}\) can be allocated to total \(s\); after choosing the \(t_j\), arrange the first \(s\) positions accordingly, fill the remaining \(r-s\) positions to reach initial counts \(r_j\), and populate the strands by distinct resources. \(\square\)

**Corollary (criterion for a full-resource word).** A resource-simple sliding-window gallery using every nonloop element of \(M\) exists if and only if, writing \(h=\lfloor N/r\rfloor\),
\[
\boxed{h r_j\le m_j\le(h+1)r_j\quad\text{for every }j.}\tag{4}
\]
*Proof.* Apply (2)--(3) with \(q=N-r=(h-1)r+(N-hr)\). The excess capacities \(u_j=m_j-h r_j\) sum to \(s=N-hr<r\). Feasibility requires \(u_j\ge0\) and \(\sum\min(r_j,u_j)\ge\sum u_j\), equivalently \(0\le u_j\le r_j\). \(\square\)

**Canonical cases.** For \(M=\bigoplus_{i=1}^nU_{1,2}\), one strand corresponds to each parallel pair and contains at most two elements. Consequently any maximal uncolored gallery has length \(2n\): its first \(n\) entries choose one representative from each pair, and its final \(n\) entries are the corresponding mates in the same order. The basis windows form a coordinate-distinct antipodal cube geodesic. For \(M=U_{2,n}\), all positions share one component; every injective word of length at least two is a gallery, giving ordinary vertex-simple tight paths of a boundary 3-tournament. More generally, for \(M=U_{r,n}\) the same one-component rule gives vertex-simple length-\(r\) window galleries.

**Geometric implication.** The periodic component-strand rule is a common intrinsic gallery geometry underlying both canonical models. Its capacity theorem separates **combinatorial admissibility** (which positions and resources may occur) from the **color feasibility** treated by terminal-set tournament growth. In particular, full-resource uncolored galleries exist for both models; their color existence problems have qualitatively different strength. The all-dimensional mixed example \(Q_k\square K_3\) constructed in the associated obstruction note satisfies (4), while its deck-odd reversal-odd coloring prohibits positive galleries of \(r\) exchanges. This proves that the periodicity and capacity axioms alone cannot supply the desired colored diameter bound.

### Cycle-dominating resource matroids and a unified tournament-extension bound

Let \(G=(V,E)\) be a finite connected simple graph with at least one edge. Let \(N\) be a matroid on the set \(E\). Assume

1. every vertex star \(E(v)\subseteq E\) is independent in \(N\);
2. every cycle of \(G\) is dependent in \(N\).

The second hypothesis implies that every \(N\)-independent edge set is a forest. In particular, a walk whose traversed edges form an independent family in \(N\) has no repeated vertex. At each \(v\), equip \(E(v)\) with an arbitrary tournament \(T_v\). A path \(v_1,\ldots,v_\ell\) is **admissible** if its successive edges are \(N\)-independent and
\[
(v_{i-1}v_i)\longrightarrow(v_iv_{i+1})\quad \text{in }T_{v_i}
\qquad(2\le i\le \ell-1).
\]
Let \(L\) be the maximum order of an admissible path.

**Theorem 1 (cycle-dominating matroid terminal bound).** Under these two matroid hypotheses,
\[
\boxed{\frac{\bar d(G)}2\le (L-1)^2,\qquad
L\ge 1+\sqrt{\frac{\bar d(G)}2},}
\qquad
\bar d(G)=\frac{2|E|}{|V|}.
\tag{1}
\]

**Proof.** For each root edge \(e\), let \(r(e)\) be the maximum order of an admissible path ending with \(e\) in either direction. Orient \(e\) toward the last vertex of a maximizing path. Some \(v\) receives at least \(\bar d(G)/2\) oriented edges. For \(2\le r\le L\), let
\[
U_r(v)=\{uv:u\to v,\ r(uv)=r\},\qquad q_r=|U_r(v)|.
\]
Select \(uv\in U_r(v)\) dominating at least \((q_r-1)/2\) members of \(U_r(v)\) under \(T_v\). Let \(P\) be an admissible \(r\)-vertex witness ending in \(u,v\), and write \(X=E(P)\), an independent set of rank \(r-1\) in \(N\).

For a dominated edge \(vw\in U_r(v)\setminus\{uv\}\), suppose that \(vw\notin\operatorname{cl}_N(X)\). Then \(X+vw\) is independent. Its edge set is a forest, so \(w\) cannot already belong to \(P\): otherwise \(X+vw\) would contain the cycle formed by the segment of \(P\) from \(w\) to \(v\) and \(vw\), contrary to hypothesis 2. The tournament comparison at \(v\) allows an admissible extension of \(P\) to \(w\), giving a path of order \(r+1\) ending with \(vw\). This contradicts \(r(vw)=r\). Thus **every dominated edge lies in** \(\operatorname{cl}_N(X)\).

Because \(E(v)\) is independent in \(N\), its subset \(E(v)\cap\operatorname{cl}_N(X)\) is independent and therefore has size at most
\[
\operatorname{rk}_N\operatorname{cl}_N(X)=r-1.
\]
One member is \(uv\), so at most \(r-2\) other members of \(U_r(v)\) can be dominated by \(uv\). Hence
\[
\frac{q_r-1}{2}\le r-2,\qquad q_r\le 2r-3.
\]
Summing over \(r\) at the chosen \(v\),
\[
\frac{\bar d(G)}2\le \deg^-(v)
=\sum_{r=2}^{L}q_r
\le\sum_{r=2}^{L}(2r-3)=(L-1)^2.
\]
This proves (1). \(\square\)

The statement strengthens the properly edge-labeled tournament theorem from Article VII whenever the associated color-partition resource matroid has the cycle-dependence property. That theorem counts a repeated vertex and a repeated resource separately, whereas here both obstructions are captured by a single matroid closure.

**Corollary 2 (proper colorings without rainbow cycles).** Let the edges of \(G\) be properly colored with arbitrary labels, and assume every graph cycle repeats at least one label. Give each vertex star an arbitrary tournament. Then there is a vertex-simple, rainbow, locally tournament-increasing path of order at least
\[
1+\sqrt{\bar d(G)/2}.
\tag{2}
\]

**Proof.** Let \(N\) be the partition matroid of edges grouped by label, of capacity one per class. Properness makes each star independent; the absence of rainbow cycles makes every graph cycle dependent in \(N\). Apply Theorem 1. \(\square\)

In particular the result applies to partial cubes, with their canonical edge labels given by the hypercube-coordinate classes: edges sharing a coordinate have the same label, each star has distinct coordinate labels, and every closed walk uses each coordinate an even number of times.

#### Intrinsic vector-difference resource quotients

Let \(\phi:V(G)\to\mathbb R^d\) be a map and represent an edge \(uv\) by \(d_{uv}=\phi(v)-\phi(u)\), with any choice of edge direction. Denote by \(N_\phi\) the linear matroid of these columns. Since every oriented graph-cycle sums to zero, every graph cycle is dependent in \(N_\phi\). If the vectors
\[
\{\phi(w)-\phi(v):w\in N_G(v)\}
\]
are linearly independent for each \(v\), then Theorem 1 applies. Equivalently, \(N_\phi\) is a representable quotient of the graphic matroid \(M(G)\), with independent vertex stars.

For the cube \(Q_n\), take \(\phi(x)=x\in\mathbb R^n\). Its edge vectors are \(\pm e_i\) and \(N_\phi\) is the coordinate-partition matroid. Independent edge sequences are precisely coordinate-distinct walks, and hence cube geodesics. Order incident cube edges locally by their arbitrary binary colors, breaking ties to form a tournament. Every admissible path has a weakly increasing color word and at most one switch. Since \(\bar d(Q_n)=n\), Theorem 1 yields

\[
\boxed{\text{a coordinate-distinct at-most-one-switch cube geodesic with at least }
\left\lceil\sqrt{n/2}\right\rceil\text{ edges}.}
\tag{3}
\]
No antipodal coloring hypothesis is required. This improves the general one-switch partial-geodesic constant in the Article VII terminal theorem. The statement is a partial-geodesic theorem; it does not establish a monochromatic antipodal geodesic.

For \(K_n\), take \(\phi(v)=e_v\in\mathbb R^n\). The edge vectors \(e_v-e_u\) represent \(M(K_n)\), since an edge set is independent precisely when it is a forest. Every star is independent. For any reversal-odd boundary coloring \(b(a,v,w)\), orient the tournament at \(v\) from \(av\) to \(vw\) when \(b(a,v,w)=1\). An admissible path is then a monochromatic, vertex-simple tight path, and (1) gives
\[
\boxed{L\ge1+\sqrt{(n-1)/2}.}
\tag{4}
\]

Thus the two witness constraints arise from one natural construction: vertex-difference matroids whose independent sets are forests and whose local stars are independent.

#### Canonical spectral construction

There is a representation-free way to obtain these resource matroids from the reconstructed graph. For any connected graph \(G\), let \(A\) be its real symmetric adjacency matrix and let \(\lambda_2\) denote its second largest **distinct** adjacency eigenvalue. Let \(P\) be the orthogonal projection onto the corresponding eigenspace and put
\[
\phi_G(v)=P\mathbf e_v,\qquad
N_{\mathrm{sp}}(G)=N_{\phi_G}.
\tag{5}
\]
The construction is invariant under every automorphism of \(G\): its defining projection is a polynomial in \(A\). It is a linear quotient of the graphic matroid. If each vertex star is independent in \(N_{\mathrm{sp}}(G)\), Theorem 1 applies without selecting a separate resource representation.

**Theorem 3 (spectral recovery of both canonical resources).** For \(n\ge3\),
\[
N_{\mathrm{sp}}(Q_n)=\bigoplus_{i=1}^n U_{1,2^{n-1}}
\quad\text{on the \(n\) direction classes of cube edges},
\tag{6}
\]
and
\[
N_{\mathrm{sp}}(K_n)=M(K_n).
\tag{7}
\]
The cube's \(\lambda_2=n-2\) eigenspace has dimension \(n\), and the complete graph's \(\lambda_2=-1\) eigenspace has dimension \(n-1\). In both graphs the vectors of any vertex star form a basis of the \(\lambda_2\) eigenspace.

**Proof.** For \(Q_n\), the functions \(\chi_i(x)=(-1)^{x_i}\), \(1\le i\le n\), are mutually orthogonal adjacency eigenvectors with eigenvalue \(n-2\); the Boolean-character decomposition gives the remaining eigenvalues \(n-2k\), so they span the eigenspace immediately below \(n\). Identifying that eigenspace with \(\mathbb R^n\), the projection of \(\mathbf e_x\) has coordinates proportional to \((\chi_1(x),\ldots,\chi_n(x))\). For adjacent \(x,x+e_i\), the difference is a nonzero multiple of \(e_i\). Thus its edge-column matroid is the direction-partition matroid; the \(n\) vectors at every vertex form a basis.

For \(K_n\), \(A=J-I\) has the constant eigenspace of eigenvalue \(n-1\) and its orthogonal complement, of eigenvalue \(-1\). Hence \(P=I-\frac1nJ\), and
\[
\phi_G(v)-\phi_G(u)=\mathbf e_v-\mathbf e_u.
\]
These columns represent \(M(K_n)\). Its \(n-1\) incident-edge vectors at any vertex form a basis of the standard zero-sum representation. \(\square\)

Define the **spectral root class** to consist of matroids \(M\) for which the largest-clique incidence graph is a subdivision of a connected simple graph \(G(M)\), the root \(G(M)\) is itself a matroid basis graph, and every root star is independent in \(N_{\mathrm{sp}}(G(M))\). These are intrinsic properties of \(M\). Theorem 3 and the earlier incidence reconstructions place both canonical target families in this class.

The rank-two matroid with three parallel classes of size two, which belongs to the broader root-basis class, does not satisfy the spectral-star condition: its incidence root is \(K_{2,2,2}\), regular of degree \(4\), whereas its second adjacency eigenspace has dimension \(3\), so no four incident spectral differences can be independent. Thus spectral-star independence makes a further structural distinction without referring to the desired path conclusion.

The spectral construction identifies the common resource geometry and proves the bound (1). The full NORI1 conclusion requires a separate rank-saturation mechanism compatible with antipodal color reversal.

#### The homogeneous Hamming interpolation

The canonical spectral-resource construction extends simultaneously to all Cartesian powers of complete graphs, providing an intermediate family between the cube and the complete graph.

**Theorem 4 (spectral resource geometry of Hamming graphs).** Let
\[
H(k,q)=\underbrace{K_q\square\cdots\square K_q}_{k\text{ factors}},
\qquad k\ge1,\ q\ge2.
\]
Then \(H(k,q)\) is a connected \(d=k(q-1)\)-regular matroid basis graph, namely the basis graph of \(\bigoplus_{i=1}^k U_{1,q}\). Its second adjacency eigenspace has eigenvalue
\[
\lambda_2=d-q
\]
and dimension \(d\). In a suitable orthogonal coordinate system, its canonical projection \(\phi_{H(k,q)}\) is proportional to
\[
(a_1,\ldots,a_k)\longmapsto
\bigl(\mathbf e_{a_1}-q^{-1}\mathbf1,\ldots,
\mathbf e_{a_k}-q^{-1}\mathbf1\bigr)
\in\bigoplus_{i=1}^k\mathbf1^\perp\subset(\mathbb R^q)^k.
\tag{8}
\]
Every vertex star represents a basis of the \(d\)-dimensional spectral resource matroid.

For each coordinate \(i\), the resource vectors of transitions changing \(a_i=a\) to \(b\) are proportional to \(\mathbf e_b-\mathbf e_a\) in the \(i\)th summand. Thus the canonical resource matroid is the direct sum of \(k\) copies of the type-\(A_{q-1}\) graphic matroid \(M(K_q)\), with parallel copies of each transition \(\{a,b\}\) across the different settings of the other \(k-1\) coordinates. A walk has an independent resource-edge sequence precisely when the transitions within every coordinate form an edge-simple forest in that coordinate's \(K_q\). Such a walk cannot revisit any coordinate value after leaving it, and is a vertex-simple path.

Moreover, through any specified initial vertex there exists an independent path with \(d\) edges, saturating the resource rank.

**Proof.** The eigenvalues of the \(K_q\) adjacency matrix on the constant and zero-sum spaces are respectively \(q-1\) and \(-1\), with multiplicities \(1\) and \(q-1\). The adjacency matrix of their Cartesian product is the sum of the adjacency operators on the \(k\) factors. Its leading eigenvalue is \(d\); replacing the constant space in precisely one factor by its zero-sum space produces the next eigenvalue \(d-q\), with total multiplicity \(k(q-1)=d\). Orthogonal projection of a vertex delta function to this eigenspace gives (8), up to a common nonzero normalization. An edge changes one coordinate, so its gradient is a single type-\(A_{q-1}\) root in one factor; all other blocks vanish. This proves the resource-matroid decomposition.

At a vertex \(a\), the \(q-1\) vectors \(\mathbf e_b-\mathbf e_{a_i}\) as \(b\) runs over the other symbols form a basis of the zero-sum space in factor \(i\). Over all coordinates they form a basis of the full spectral eigenspace. An independent edge sequence cannot contain a closed cycle among the transitions in any coordinate. The successive coordinate values form a trail in \(K_q\); a repeated coordinate value would produce a cycle in that trail. For rank saturation, fix any order of the \(k\) coordinates and, one coordinate at a time, change its value through all \(q\) symbols without repetition. The resulting \(k(q-1)\) transitions form a forest in each coordinate factor and are independent. \(\square\)

At the two extremes,
\[
H(n,2)=Q_n,\qquad H(1,n)=K_n,
\]
and their spectral resource matroids specialize respectively to coordinate independence and graphic independence. Theorem 1 therefore gives the uniform quantitative bound
\[
L\ge 1+\sqrt{k(q-1)/2}
\tag{9}
\]
for arbitrary local tournaments on every homogeneous Hamming graph, with spectral-resource-independent paths. The endpoint examples recover the cube one-switch partial-geodesic result (under local color ordering) and the ordinary boundary-tournament square-root result (under reversal-odd turn ordering).

The intermediate family is a statement about *resource-root graphs*; it does not assert that every \(H(k,q)\) appears as the maximum-clique incidence root of an input matroid \(M\) from the previous section. Its usefulness is that the two extremal resource matroids are specializations of the same automorphism-invariant spectral construction, with a common full-rank uncolored path geometry.

**Proposition 5 (spectral antipodes occur only at the cubical endpoint).** For \(k\ge1\), \(q\ge2\), the convex hull of the spectral vertex embedding \(\phi_{H(k,q)}(V)\) is centrally symmetric if and only if \(q=2\). When \(q=2\), its central reflection is the hypercube complement map \(a\mapsto\bar a\); when \(k=1\) and \(q>2\), the root is a simplex and has no centrally induced vertex antipode.

**Proof.** Formula (8) identifies the spectral convex hull, up to a common dilation, with a Cartesian product of \(k\) centered \((q-1)\)-simplices. For \(q=2\), each simplex is a segment, and their product is centrally symmetric. For \(q>2\), project onto any coordinate summand. A centrally symmetric convex body has centrally symmetric linear images, whereas the simplex with vertices \(\mathbf e_a-q^{-1}\mathbf1\), \(a\in[q]\), has no central symmetry: its centroid is the only possible center and the negative of \(\mathbf e_a-q^{-1}\mathbf1\) is not another vertex when \(q>2\). Hence the product is not centrally symmetric. \(\square\)

This proposition localizes a necessary distinction in the polarization problem: the spectral map produces the cube's vertex antipode intrinsically, while in the complete-graph endpoint the reversal-odd operation must be imposed on oriented exchanges or turns. In either case reversal of an oriented edge changes its spectral resource vector by a sign, but that common linear sign involution does not itself impose the original two-color constraints.

Let \(M\) be a finite matroid obtained as a direct sum of nontrivial uniform matroids
\[
M=\bigoplus_{j=1}^{t}U_{r_j,m_j},\qquad 1\le r_j<m_j,
\]
and let \(G=\Gamma(M)\) be its basis-exchange graph. Thus
\[
G=\mathop{\square}_{j=1}^{t}J(m_j,r_j),\qquad
d=\deg(G)=\sum_{j=1}^{t}r_j(m_j-r_j).
\]
Let \(A_G\) be its adjacency matrix, \(P_2\) the orthogonal projection onto the eigenspace \(W_2\) of its second largest distinct adjacency eigenvalue, and \(N_{\rm sp}(G)\) the linear matroid on graph edges \(uv\) represented by \(P_2({\bf e}_u-{\bf e}_v)\).

**Theorem (spectral-star rigidity).** The following are equivalent:

(i) The edge vectors in every vertex star of \(G\) are independent in \(N_{\rm sp}(G)\).

(ii) There is an integer \(q\ge2\) such that every summand has \(m_j=q\) and \(r_j\in\{1,q-1\}\).

(iii) \(G\cong H(t,q)=K_q^{\square t}\) for some \(q\ge2\).

Under these conditions,
\[
\dim W_2=d=t(q-1),\qquad
\operatorname{rk}N_{\rm sp}(G)=d;
\]
each vertex star is a basis of \(N_{\rm sp}(G)\), and \(N_{\rm sp}(G)\) has minimum possible rank among matroids on \(E(G)\) in which all vertex stars are independent.

*Proof.* The adjacency spectrum of a Johnson graph \(J(m,r)\), for \(1\le r<m\), consists of the distinct eigenvalues
\[
\theta_\ell=(r-\ell)(m-r-\ell)-\ell,\qquad 0\le\ell\le\min(r,m-r),
\]
with the second one \(\theta_1=r(m-r)-m\) of multiplicity \(m-1\). Thus its spectral gap between the largest and second-largest adjacency eigenvalues is \(m\).

The adjacency operator of a Cartesian product is the sum of the lifted factor adjacency operators. Put \(m_*=\min_jm_j\). The second-largest eigenvalue of \(G\) is therefore \(d-m_*\), and its multiplicity is
\[
D=\dim W_2=\sum_{\{j:m_j=m_*\}}(m_j-1).\tag{1}
\]
For every \(j\),
\[
r_j(m_j-r_j)\ge m_j-1,\tag{2}
\]
with equality if and only if \(r_j=1\) or \(r_j=m_j-1\). As each summand is nontrivial, (1)--(2) give \(d\ge D\), and equality holds if and only if all \(m_j=m_*\) and each rank is \(1\) or \(m_*-1\). Since the \(d\) incident edge vectors at a vertex lie in the \(D\)-dimensional space \(W_2\), condition (i) requires \(d\le D\). Hence (i) implies (ii).

Under (ii), every Johnson factor is \(J(q,1)\cong J(q,q-1)\cong K_q\), proving (iii). Conversely, every Johnson graph \(J(m,r)\), \(1\le r<m\), has triangle-connected edge set (the graph whose vertices are its edges and whose adjacencies join two edges belonging to one triangle is connected), unless it consists of a single edge. Indeed, two exchanges at the same basis are joined by a sequence of triangle moves that alternately hold the entering or departing element fixed; the line graph of the complete bipartite fundamental exchange graph \(K_{r,m-r}\) is connected. Connectedness of \(J(m,r)\) then joins the triangle chains across bases. In a Cartesian product, the edges of every triangle lie in one factor, so a triangle-connected Johnson factor cannot split across distinct Cartesian factors. Therefore if (iii) holds, each Johnson factor is one complete factor \(K_q\), and hence \(r_j\in\{1,m_j-1\}\) and \(m_j=q\).

To prove (iii) implies (i), identify the second eigenspace of \(H(t,q)\) with \(\bigoplus_{j=1}^t{\bf1}^{\perp}\subseteq(\mathbb R^q)^t\). The projected difference vector for an edge changing symbol \(a\) to \(b\) in factor \(j\) is, up to a common nonzero scalar, \({\bf e}_b-{\bf e}_a\) in the \(j\)-th summand and zero elsewhere. At any vertex, the \(q-1\) incident vectors in factor \(j\) form a basis of that summand. All incident vectors are therefore a basis of \(W_2\). Connectedness ensures that the projected differences of graph edges span all of \(W_2\), because edge differences span the coordinate hyperplane perpendicular to the all-ones vector, which contains \(W_2\). Hence the edge-column matroid has rank \(d\).

Finally, any matroid on \(E(G)\) with an independent vertex star has rank at least \(d\). The spectral resource matroid attains this lower bound. \(\square\)

**Corollary (intrinsic minimal resource geometry of the canonical roots).** For \(Q_n=H(n,2)\), the minimal-rank spectral resource matroid is the partition matroid on coordinate-direction edge classes, of rank \(n\). For \(K_n=H(1,n)\), it is the graphic matroid \(M(K_n)\), of rank \(n-1\). In both cases, every vertex star is a resource basis. These are two specializations of the same automorphism-invariant spectral projection, with the resource rank equal to the graph degree.

**Scope.** The theorem classifies the spectral-star condition *within partition-matroid basis graphs*. It does not classify all matroid basis graphs satisfying that condition. Its two extremal cases are the root graphs naturally associated with the NORI1 cube and the boundary 3-tournament Johnson basis graph, respectively: the boundary root is \(K_n\), recovered as the line-graph root of \(J(n,2)\) for \(n\ge4\). It provides a structural class and a minimum-rank resource representation but does not force full-rank positively oriented paths.

**Corollary (functorial polarization threshold).** Let \(X=V(H(t,q))\) with the natural action of \(\operatorname{Aut}(H(t,q))=S_q\wr S_t\). If \(q\ge3\), every equivariant self-map \(X\to X\) is the identity. If \(q=2\), the equivariant self-maps are the identity and simultaneous coordinate complementation.

*Proof.* The automorphism group acts transitively. An equivariant map is determined by the image of the all-zero vertex, which must be fixed by its stabilizer. For \(q\ge3\), the stabilizer contains an independent \(S_{q-1}\) permutation group on the unused alphabet symbols in every factor, and therefore fixes only the all-zero vertex. For \(q=2\), the stabilizer permutes the \(t\) factors and fixes the two constant binary words; the two resulting equivariant maps are identity and complementation. \(\square\)

Thus the canonical fixed-point-free antipode of \(Q_t\) disappears immediately upon passing to the next homogeneous Hamming interpolation \(H(t,3)\). Any formulation encompassing arbitrary complete-graph roots must locate its reversal structure on oriented exchange flags or another derived carrier.

Let \(G=(V,E)\) be a finite simple graph. Let \(\mathsf R\) be a matroid of rank \(d\), represented by nonzero vectors \(\{a_\ell:\ell\in\Lambda\}\) over a field \(\mathbb F\). Suppose the edges of \(G\) carry labels \(\lambda:E\to\Lambda\) and there is an injective vertex potential \(\phi:V\to\mathbb F^N\), where the vectors \(a_\ell\) also lie in \(\mathbb F^N\), with the following properties:

1. For every oriented edge \(uv\), \(\phi(v)-\phi(u)\) is a nonzero scalar multiple of \(a_{\lambda(uv)}\).
2. At every vertex \(v\), the \(d\) labels on its incident edges form a basis of \(\mathsf R\).

The second condition makes \(G\) \(d\)-regular. We call this the **basis-star condition**. In this Subsection, a path is resource-independent if its edge-label multiset contains no repetitions and is independent in \(\mathsf R\). Equip each vertex \(v\) with an arbitrary tournament \(T_v\) on the edges incident with \(v\). A resource-independent path \(v_1,\ldots,v_\ell\) is admissible if \(v_{i-1}v_i\to v_iv_{i+1}\) in \(T_{v_i}\) at every internal vertex. The tournament data are entirely unrestricted.

**Lemma 1 (independent resources enforce vertex simplicity).** Every resource-independent walk in \(G\) is vertex-simple. Furthermore, two resource-independent walks terminating at the same vertex, whose combined edge-label multiset is independent, have no common vertex other than their terminal vertex.

*Proof.* A nonempty closed subwalk whose labels are independent would give, by telescoping the potential \(\phi\), a nontrivial linear relation among their representing vectors: every traversed edge contributes a nonzero scalar and no label occurs twice. This is impossible. Therefore an independent-resource walk has no repeated vertex. If two walks with a common terminal \(t\) met again at \(z\ne t\), their subwalks from \(t\) to \(z\) would give two representations of \(\phi(z)-\phi(t)\). Subtracting these expressions would produce a nontrivial dependence among their combined distinct labels. Hence their intersection consists only of \(t\). \(\square\)

**Theorem 2 (basis-star terminal-edge theorem).** In the preceding setting, there is an admissible resource-independent path with \(L\) vertices satisfying
\[
\boxed{\quad d/2\le (L-1)^2,\qquad L\ge 1+\sqrt{d/2}.\quad} \tag{1}
\]

*Proof.* For an undirected edge \(e\), let \(h(e)\) be the greatest order of an admissible resource-independent path with \(e\) as its last edge, in either orientation. A two-vertex path is admissible, so \(2\le h(e)\le d+1\). Orient \(e\) toward the terminal vertex of a path attaining \(h(e)\), resolving ties arbitrarily. Since \(G\) is \(d\)-regular, the average indegree in the resulting orientation is \(d/2\); choose a vertex \(v\) with at least this indegree.

For \(2\le k\le L:=\max_e h(e)\), let \(U_k\) consist of the edges oriented toward \(v\) for which \(h(e)=k\), and put \(q=|U_k|\). If \(q=0\) there is nothing to prove. The tournament on \(U_k\) has an edge \(uv\) beating at least \((q-1)/2\) other members \(vw\) of \(U_k\). By the choice of the orientation, there is an admissible resource-independent path \(P=(v_1,\ldots,v_{k-2},u,v)\) attaining \(h(uv)=k\).

Write \(S\) for the span of the \(k-1\) representing vectors corresponding to the labels of the edges of \(P\). Suppose that a beaten edge \(vw\in U_k\) has \(a_{\lambda(vw)}\notin S\). Then \(P\) followed by \(vw\) has independent labels, and it obeys the required tournament comparison at \(v\). Lemma 1 guarantees that the resulting walk has distinct vertices. It is therefore an admissible resource-independent \((k+1)\)-vertex path ending in \(vw\), contrary to \(h(vw)=k\).

Every edge of \(U_k\) beaten by \(uv\) consequently has its representing vector in \(S\). The vectors labeling the full star at \(v\) constitute a basis of \(\mathsf R\); at most \(\dim S=k-1\) of them can lie in \(S\). One of these vectors labels the incoming edge \(uv\), which does not beat itself. Therefore at most \(k-2\) other star edges can be beaten, and
\[
(q-1)/2\le k-2,\qquad q\le 2k-3.
\]
Summing over all terminal orders,
\[
d/2\le\deg^-(v)=\sum_{k=2}^{L}|U_k|
\le\sum_{k=2}^{L}(2k-3)=(L-1)^2.
\]
This proves (1). \(\square\)

The proof uses the matroid span to control both possible failures of extension: a repeated label and a repeated vertex. The vertex-potential identity in Lemma 1 makes the second failure automatically dependent on the first. This removes the second obstruction term in the proper-edge-label terminal theorem of Article VII, while allowing labels to recur at different vertices.

##### Canonical realization on products of simplices

Let \(M=\bigoplus_{j=1}^t U_{r_j,E_j}\), where \(1\le r_j<|E_j|=:m_j\). Its connected-component partition is intrinsic to \(M\). Define the componentwise rank-one reduction
\[
M^\flat=\bigoplus_{j=1}^t U_{1,E_j},
\qquad
G_M=\Gamma(M^\flat)\cong \mathop{\square}_{j=1}^t K_{m_j}.
\tag{2}
\]
The vertices of \(G_M\) are tuples \(x=(x_1,\ldots,x_t)\), with \(x_j\in E_j\); an edge changes one component coordinate from \(a\) to \(b\).

Let
\[
\mathsf R_M=\bigoplus_{j=1}^t M(K_{E_j}),\qquad
d=\operatorname{rk}(\mathsf R_M)=\sum_{j=1}^t(m_j-1).
\tag{3}
\]
Represent the edge \(ab\) in the \(j\)-th clique by \(e_b-e_a\in\mathbb R^{E_j}\), and write \(\lambda(xy)=(j,\{a,b\})\) for the edge label when \(x,y\) differ in component \(j\). The vertex potential
\[
\phi(x)=\bigoplus_{j=1}^t e_{x_j}\in\bigoplus_{j=1}^t\mathbb R^{E_j}
\tag{4}
\]
is injective. Its derivative along \(xy\) is the root \(e_b-e_a\) with the appropriate orientation. At \(x\), the root vectors of its \(m_j-1\) incident edges in coordinate \(j\) are
\[
\{e_b-e_{x_j}:b\in E_j\setminus\{x_j\}\}.
\tag{5}
\]
These form a basis of the type-\(A_{m_j-1}\) root space. Taking their union over the different components gives a basis of \(\mathsf R_M\).

**Proposition (coordinatewise simple-path criterion).** Let
\[
G=\mathop{\square}_{j=1}^t K_{m_j},\qquad
R=\bigoplus_{j=1}^t M(K_{m_j}),
\]
with the canonical labels \(\lambda(xy)=(j,\{a,b\})\) on steps changing coordinate \(j\) from \(a\) to \(b\). For any finite walk \(P=(x^0,\ldots,x^\ell)\) in \(G\), let \(P_j\) be the sequence of coordinate-\(j\) values obtained from \(x_j^0,\ldots,x_j^\ell\) by suppressing consecutive repeats. Then the following are equivalent:

(a) the multiset of all step labels along \(P\) is independent in \(R\);

(b) for every \(j\), the entries of \(P_j\) are pairwise distinct.

Under either condition, \(P\) is a vertex-simple path and \(\ell\le\operatorname{rk}(R)=\sum_j(m_j-1)\). Equality holds if and only if \(P_j\) is a Hamiltonian path in the complete graph \(K_{m_j}\) for every coordinate \(j\).

*Proof.* The labels contributed by coordinate \(j\) are the consecutive edges of the walk \(P_j\) in \(K_{m_j}\). A multiset of edges is independent in the graphic matroid if and only if it has no repeated edge and its underlying graph is a forest. A walk using only edges of a forest, each at most once, cannot revisit a vertex: a segment between successive visits would be a nonempty closed trail, necessarily containing either a repeated edge or a cycle. Conversely, a walk with pairwise distinct vertices forms a simple path, whose edges are independent in the graphic matroid. Since \(R\) is the direct sum of its factor matroids, applying this equivalence in every coordinate proves (a)\(\Leftrightarrow\)(b).

If \(x^p=x^q\) for \(p<q\), some coordinate changes between those two times, and its suppressed coordinate sequence revisits its initial value, contradicting (b). Hence \(P\) is vertex-simple. In coordinate \(j\), pairwise distinct entries imply at most \(m_j-1\) changes. Summing gives \(\ell\le\sum_j(m_j-1)\). Equality holds precisely when every coordinate changes \(m_j-1\) times and thus visits all its \(m_j\) symbols. \(\square\)

**Canonical interpretations.** When all \(m_j=2\), a full-rank independent gallery changes each binary coordinate once; it is a cube antipodal geodesic. When \(t=1\) and \(m_1=n\), a full-rank independent gallery is a Hamiltonian vertex word in \(K_n\), and its successive two-edge windows are the ordered triples of the boundary tournament. For general \(t\), a full-rank gallery is a path whose projections onto every clique factor are Hamiltonian paths, with the factor moves interleaved arbitrarily. This is a common *geometric* witness language derived from the intrinsic direct-sum graphic-root matroid. Color-compatible existence is the additional problem.


**Corollary 3 (uniform Hamming-graph theorem).** For every Cartesian product of nontrivial cliques \(G=\square_{j=1}^t K_{m_j}\), endowed with arbitrary local tournaments on its incident edges, there is a vertex-simple tournament-admissible path whose labels are independent in \(\bigoplus_j M(K_{m_j})\) and which has at least
\[
\boxed{1+\sqrt{\tfrac12\sum_j(m_j-1)}} \tag{6}
\]
vertices.

This establishes one intrinsic root-matroid extension theorem for all rank-one partition-matroid basis graphs. The source matroid ranks \(r_j\) determine additional color-carrier geometry but play no role in the root-basis terminal inequality.

##### Both canonical source models

For \(M_{\rm cub}=\bigoplus_{i=1}^nU_{1,2}\), the reduction \(M_{\rm cub}^\flat=M_{\rm cub}\) has \(G_M=Q_n\) and \(\mathsf R_M\cong U_{n,n}\). Given any coloring of undirected cube edges, order the edges incident with each cube vertex first by increasing color and then by an arbitrary tie-break. Each local tournament is transitive. An admissible path has independent direction labels and therefore is a geodesic; its edge-color word is weakly increasing. Theorem 2 supplies a geodesic of at least
\[
\boxed{\sqrt{n/2}}\tag{7}
\]
edges and at most one color change. This applies, in particular, to every NORI1 antipodally odd coloring. It strengthens the partial-geodesic bound obtained by applying the proper-label estimate of Article VII directly.

For \(M_{\rm bd}=U_{2,n}\), the reduction is \(U_{1,n}\), so \(G_M=K_n\), \(\mathsf R_M=M(K_n)\), and
\[
\Gamma(M_{\rm bd})=J(n,2)=L(G_M).
\tag{8}
\]
Let \(b(a,v,c)\in\{0,1\}\) be an arbitrary reversal-odd boundary coloring. At vertex \(v\) of \(K_n\), orient the local comparison \(av\to vc\) precisely when \(b(a,v,c)=1\). Reversal oddness makes this a tournament. Theorem 2 produces a vertex-simple path of order at least
\[
\boxed{1+\sqrt{(n-1)/2}}\tag{9}
\]
on which every consecutive triple has color one. Reversal gives an equally long color-zero path. In this model the independent-root predicate is the original-vertex graphic independence: a simple tight path uses a forest of consecutive original edges.

Thus the same rank \(d\), the same star-basis hypothesis, and the same terminal-edge proof explain both square-root bounds. In the cube the resulting geodesic is only partial; neither Theorem 2 nor Corollary 3 promotes it to a monochromatic full antipodal geodesic. Such a promotion would require the global antipodal coloring law and the additional square-exchange geometry.

##### Two-arm resource bases

The potential argument also supplies a common geometric gluing rule. Let \(P,Q\) be two paths ending at a common vertex \(t\), and suppose the multiset of labels of their combined edges is a basis of \(\mathsf R\). Lemma 1 makes their union a simple path, obtained by concatenating \(P\) with the reversal of \(Q\). For the two canonical color-carrier grades this has a common binary conclusion:

- For undirected edge colors, two same-colored monochromatic arms concatenate to a monochromatic path. On the cube, full root rank \(n\) forces every coordinate to occur once, hence the other endpoints are antipodes.
- For reversal-odd colors on oriented two-edge windows, two same-colored monochromatic arms concatenate to a path with at most one color change among successive windows. Windows in the reversed arm have the complementary color, and the one junction window can only extend one of these two color runs. On \(K_n\), full root rank \(n-1\) forces a Hamiltonian tight word.

Conversely, a full monochromatic cube geodesic splits into two monochromatic arms with a basis union. The common-terminal two-arm theorem elsewhere in Article XI establishes the converse for boundary Hamiltonian words with at most one change, including its junction cases. In this way a single resource-basis packing predicate expresses both spanning conclusions; its universal existence remains conjectural. Theorem 2 supplies quantitative rank-growth toward that predicate without assuming it.

##### Linear monochromatic paths from edge-density and root independence

The root-potential hypotheses strengthen the standard greedy rainbow-path argument for a properly edge-labelled graph. In particular, the independent-star property suffices without requiring the star to span all of \(\mathsf R\).

**Lemma 4 (minimum degree forces independent-root path length).** Suppose \(G\) has an injective vertex potential and a root representation as above, and the edge labels incident with each vertex are independent in \(\mathsf R\). Every nonempty edge-subgraph \(H\subseteq G\) of minimum degree \(\delta(H)\) contains a resource-independent path of at least \(\delta(H)\) edges.

*Proof.* Choose a resource-independent path \(P=(v_0,\ldots,v_\ell)\) in \(H\) with maximal length, and let \(S\) be the linear span of its \(\ell\) resource vectors. If an edge \(v_\ell w\) of \(H\) has label outside \(S\), then adding it preserves resource independence. Moreover \(w\) is new: for any \(w=v_i\) already on \(P\), the vector \(\phi(w)-\phi(v_\ell)\) is a linear combination of the root vectors labeling the terminal subpath of \(P\), hence the label of \(v_\ell w\) lies in \(S\). Thus maximality forces every \(H\)-edge incident with \(v_\ell\) to have its label in \(S\). The independent-star condition bounds their number by \(\dim S=\ell\). Therefore \(\ell\ge \deg_H(v_\ell)\ge\delta(H)\). \(\square\)

**Theorem 5 (density-to-resource-rank bound).** Under the conditions of Lemma 4, every nonempty edge-subgraph \(H=(V,E_H)\subseteq G\), including isolated vertices in \(V\), contains a resource-independent path of length at least
\[
\boxed{\left\lceil\frac{|E_H|}{|V|}\right\rceil .}\tag{10}
\]

*Proof.* Put \(a=|E_H|/|V|>0\). Iteratively delete a vertex whose degree in the remaining subgraph is strictly smaller than \(a\), if one exists. All vertices cannot be deleted: charge every edge to its endpoint deleted first. Were every vertex deleted, fewer than \(a|V|=|E_H|\) edge incidences would be charged, while each original edge is charged once. Hence a nonempty subgraph \(K\subseteq H\) survives with \(\delta(K)\ge a\). Lemma 4 gives a resource-independent path of at least \(\delta(K)\) edges, at least the ceiling in (10). \(\square\)

**Theorem 6 (free-resource rank potential).** Assume in addition that \(\mathsf R\) is free, and fix any total order on its edge-label ground set \(\Lambda\). For any edge-subgraph \(H=(V,E_H)\) with proper edge labelling and the same injective root potential, let \(L_H(v)\) be the greatest length of a path ending at \(v\) whose resource labels occur in strictly increasing order. Then
\[
\boxed{\sum_{v\in V} L_H(v)\ge 2|E_H|.}\tag{11}
\]
In particular \(H\) contains a resource-independent path of length at least \(2|E_H|/|V|\).

*Proof.* We argue by induction on \(|E_H|\). The assertion is immediate when \(E_H=\varnothing\). Choose an edge \(e=xy\) with maximal label and put \(H'=H-e\). By properness, the label of every last edge in a strictly increasing path of \(H'\) ending at \(x\) or \(y\) is smaller than \(\lambda(e)\): no other edge at either endpoint has this label. Since \(\mathsf R\) is free, appending \(e\) to either such path preserves resource independence; injectivity of the vertex potential ensures the new endpoint has not been visited. Write \(a=L_{H'}(x)\) and \(b=L_{H'}(y)\). If \(a=b\), appending \(e\) increases both endpoint maxima by at least one, and their sum increases by at least two. If, say, \(a\ge b+1\), appending \(e\) to a maximizing path ending at \(x\) increases the maximum at \(y\) by at least \(a+1-b\ge2\). In every case the sum of all endpoint maxima increases by at least two when \(e\) is restored. The induction hypothesis proves (11). \(\square\)

The argument is the increasing-geodesic potential method of Leader and Long, *Long geodesics in subgraphs of the cube*, extended here to any faithful free-resource voltage graph with proper labelling. The representation-theoretic role of freeness is explicit: a newly largest label has no circuit dependence on previously used labels. The potential hypothesis makes an attempted endpoint repetition a consequence of precisely such a circuit.

**Corollary 7 (sharp known density bound for cube edge colors).** Every two-coloring of \(E(Q_n)\) has a monochromatic coordinate-distinct geodesic of length at least \(\lceil n/2\rceil\). For an antipodally odd coloring, each of the two colors admits such a geodesic.

*Proof.* The coordinate-root matroid \(U_{n,n}\) is free, the coordinate edge labelling is proper, and its natural vertex potential is injective. The cube has \(n2^{n-1}\) edges. Under any two-coloring, a color occurs on at least \(n2^{n-2}\) edges. Apply Theorem 6 with \(|V|=2^n\). Under antipodal oddness, each edge-color class contains \(n2^{n-2}\) edges, so the argument applies to both classes. \(\square\)

The first conclusion is the Leader--Long monochromatic-geodesic corollary, recovered through Theorem 6; the both-color formulation follows from antipodal balance. This result supersedes the weaker density-to-rank bound \(\lceil n/4\rceil\) that Theorem 5 supplies in the cube. Theorem 5 retains its independent significance for represented resource matroids with circuits.

**Proposition 8 (triangle obstruction to free-resource induction).** The induction proving (11) fails in general for graphic resource matroids, even on \(K_3\). Give the three edges the increasing order \(ab<bc<ac\) and use the incidence-root representation of \(M(K_3)\). In \(H'=K_3-ac\), a maximal increasing path ending at \(c\) is \(a,b,c\), using resources \(ab,bc\). The remaining largest root \(ac\) lies in their span and its addition would close a triangle and repeat \(a\). Restoring \(ac\) raises the sum of the three endpoint maxima by only one, whereas the free-resource proof requires an increment of two.

*Proof.* The incidence identity \(e_c-e_a=(e_b-e_a)+(e_c-e_b)\) is the graphic circuit relation. The lengths of maximal increasing paths ending at \(a,b,c\), respectively, are \((1,1,2)\) in \(H'\). In \(H\) they are \((2,1,2)\): the additional increasing path \(b,c,a\) increases the maximum at \(a\) by one, while the dependent edge cannot extend the two-edge path ending at \(c\). Thus the sum increases from four to five. \(\square\)

This circuit obstruction is independent of the second complication in ordinary boundary tournaments: arbitrary reversal-odd boundary data prescribe different local tournaments, which need not be restrictions of one globally ordered root set. The former prevents automatic independent extension; the latter prevents applying the global increasing-path induction. The root-basis terminal theorem permits both and retains the common square-root conclusion.

The different grades of the two original coloring systems also matter. In a cube, a monochromatic *edge* set is a dense graph whose average degree can be used in Theorem 6. In a boundary tournament, color is assigned to consecutive *turns*, and a color class does not determine an undirected edge-subgraph of comparable density. Together, freeness of the resource matroid and the carrier grade explain why a linear monochromatic *partial* cube geodesic is accessible by this method, whereas the common local-tournament proof only gives the square-root boundary estimate. A full monochromatic antipodal cube geodesic still requires the global opposition condition and additional exchange geometry.

Let \(M\) be a finite matroid on \(E\), and let \(\Gamma(M)\) be its basis-exchange graph. For a basis \(B\), the **fundamental exchange graph** \(F_B\) is the bipartite graph on \(B\sqcup(E\setminus B)\), with edge \(be\) precisely when \(B-b+e\) is a basis. Loops and coloops become isolated vertices; the remaining connected components correspond to the connected matroid components.

Define the canonical basis-incidence embedding
\[
\Phi:\mathcal B(M)\longrightarrow\mathbb R^E,\qquad
\Phi(B)=\sum_{b\in B}{\bf e}_b.
\]
An exchange edge \(B\to B-b+e\) has difference vector \({\bf e}_e-{\bf e}_b\).

**Theorem (exchange-forest rigidity).** The following conditions are equivalent.

(i) For every basis \(B\), the exchange-difference vectors of the edges incident with \(B\) are linearly independent.

(ii) For every basis \(B\), the fundamental exchange graph \(F_B\) is a forest.

(iii) Every connected component of \(M\) is a loop, a coloop, a uniform rank-one matroid \(U_{1,m}\), or its dual \(U_{m-1,m}\).

In particular, the canonical basis-incidence resource matroid has independent stars throughout the basis-exchange graph precisely for direct sums of rank-one or corank-one uniform matroids.

*Proof.* The difference vectors \({\bf e}_e-{\bf e}_b\) at a basis \(B\) are the oriented vertex-edge incidence columns of \(F_B\), viewed in \(\mathbb R^E\). Incidence columns are independent if and only if the corresponding graph has no cycle, so (i) and (ii) are equivalent.

We prove (ii) implies (iii). Suppose an induced path
\[
b_1-e_1-b_2-e_2\tag{1}
\]
occurs in \(F_B\), with \(b_1,b_2\in B\) and \(e_1,e_2\notin B\). Thus
\[
B-b_1+e_1,\quad B-b_2+e_1,\quad B-b_2+e_2
\]
are bases, whereas \(B-b_1+e_2\) is dependent. Put \(A=B\setminus\{b_1,b_2\}\), and contract \(A\). In the rank-two matroid \(M/A\), the pair \(\{b_2,e_2\}\) is dependent, while \(\{b_1,e_2\}\) and \(\{b_2,e_1\}\) are bases. Therefore \(b_2\) and \(e_2\) are nonloops in the same parallel class, and \(\{e_1,e_2\}\) is a basis. Lifting to \(M\) shows
\[
B-\{b_1,b_2\}+\{e_1,e_2\}\ \text{is a basis}.\tag{2}
\]

Pivot from \(B\) to the adjacent basis \(B'=B-b_2+e_1\). The four substitutions
\[
B'-b_1+b_2,\quad B'-e_1+b_2,\quad
B'-e_1+e_2,\quad B'-b_1+e_2
\]
are all bases, by the hypotheses and (2). Hence \(F_{B'}\) contains a four-cycle on bipartition \(\{b_1,e_1\}\sqcup\{b_2,e_2\}\), contradicting (ii). Thus **no** fundamental exchange graph can contain an induced four-vertex path.

We next recall why the connected components of \(F_B\) correspond to those of \(M\). Let \(S_1,\ldots,S_h\) be the vertex sets of the components of \(F_B\), and let \(B_j=B\cap S_j\). Every \(e\in S_j\setminus B_j\) belongs to the closure of \(B_j\), since its fundamental circuit relative to \(B\) is contained in \(S_j\). Therefore \(\operatorname{rk}_M(S_j)=|B_j|\). As \(\sum_j|B_j|=\operatorname{rk}(M)\), the rank-additivity criterion implies \(M=\bigoplus_jM|S_j\). Conversely each matroid direct-sum component induces no fundamental exchanges with other components. Thus a connected, nontrivial component of \(M\) yields a connected \(F_B\).

By (ii), each such graph is a tree, and by the preceding pivot argument it contains no induced four-vertex path. A connected tree with no four-vertex path is a star. Since the star spans every element of its connected matroid component, one side of its bipartition has a single vertex. Thus that component has rank one or corank one. A connected rank-one matroid is \(U_{1,m}\), and a connected corank-one matroid is its dual \(U_{m-1,m}\). Loops and coloops are harmless singleton components. This proves (iii).

Conversely, for \(U_{1,m}\) the graph \(F_B\) is \(K_{1,m-1}\), and for \(U_{m-1,m}\) it is \(K_{m-1,1}\). Direct sums give disjoint unions of these stars and isolated vertices, which are forests. Hence (iii) implies (ii). \(\square\)

**Application to the two canonical root graphs.** The basis graph \(Q_n\) of \(\bigoplus^nU_{1,2}\) has a canonical embedding \(\Phi\) whose incident differences are independent: its resources are the \(n\) parallel classes of coordinate directions. The original basis graph \(J(n,2)\) of \(U_{2,n}\), \(n\ge4\), fails this condition because \(F_B=K_{2,n-2}\) has cycles. Its intrinsic line-graph root \(K_n=\Gamma(U_{1,n})\), however, satisfies the condition, and its exchange-difference vectors represent the graphic matroid \(M(K_n)\). Thus the passage from the boundary model's Johnson basis graph to its complete-graph root is mathematically necessary for this common independent-star resource mechanism.

The theorem is an ordinary-matroid obstruction to using canonical basis-indicator gradients directly in both problems, and provides a structural reason for examining a derived root graph equipped with a graphic or spectral resource matroid.

**Theorem (transitive-star terminal bound).** Let \(G\) be a connected finite simple graph of average degree \(d\), and \(N\) a matroid on \(E(G)\) in which every vertex star is independent and every graph cycle is dependent. At each vertex equip the incident edges with a transitive tournament. An admissible path has an \(N\)-independent edge set and respects the tournaments at successive edges. If \(L\) is the maximum number of vertices of an admissible path, then
\[
\boxed{d\le L(L-1).}
\]
**Proof.** For each edge \(e\), choose a longest admissible path ending with \(e\) in either direction, orient \(e\) toward its witness terminal, and let \(r(e)\) be its witness order. Some vertex \(v\) receives at least \(d/2\) edges. Let \(U_r\) be the incoming edges with \(r(e)=r\). The transitive tournament on \(U_r\) has an edge \(uv\) beating all others. Let \(P\) be its \(r\)-vertex witness and \(X=E(P)\), independent of rank \(r-1\). Any other \(vw\in U_r\) outside \(\operatorname{cl}_N(X)\) extends \(P\): independence of \(X+vw\) precludes a repeated vertex because every graph cycle is \(N\)-dependent, and the terminal comparison is favorable. This contradicts \(r(vw)=r\). Thus \(U_r\subseteq E(v)\cap\operatorname{cl}_N(X)\). As the star is independent, \(|U_r|\le r-1\). Summing gives \(d/2\le\sum_{r=2}^L(r-1)=L(L-1)/2\). \(\square\)

**Corollary (binary cube-edge colors).** Every binary coloring of \(E(Q_n)\) has a coordinate-distinct geodesic with at most one color change and at least
\[
\boxed{\left\lceil(\sqrt{4n+1}-1)/2\right\rceil}
\]
edges. Use the coordinate-partition resource matroid and order each star by edge color, breaking ties arbitrarily. Every admissible path has distinct coordinates and a weakly increasing color word; the cube has average degree \(n\). Antipodal oddness is not needed.

**Corollary (locally transitive boundary tournaments).** If the comparison tournament at each middle vertex of a reversal-odd boundary \(3\)-tournament is transitive, there is a monochromatic vertex-simple tight path with at least \(1+(\sqrt{4n-3}-1)/2\) vertices. Use \(G=K_n\), \(N=M(K_n)\), and \(d=n-1\). The local orders may be mutually inconsistent.

**Interpolation.** If every induced subtournament on \(q\) edges of any star has a vertex beating at least \(\alpha(q-1)\) others, \(1/2\le\alpha\le1\), the same proof gives \(d/2\le (L-1)+(L-1)(L-2)/(2\alpha)\), since \(\alpha(|U_r|-1)\le r-2\). It specializes to the arbitrary-tournament bound at \(\alpha=1/2\) and the theorem at \(\alpha=1\).

An \(n\)-edge one-switch geodesic in the antipodally odd cube would settle NORI1 by odd-change rotation; the result here supplies a longer partial path.

Let \(G=(V,E)\) be a finite connected simple graph and let \(N\) be a matroid on \(E\) such that
\[
\text{each vertex star }E(v)\text{ is independent in }N,
\qquad
\text{every graph cycle is dependent in }N.\tag{1}
\]
Let \(c:E\to\mathbb F_2\) be an arbitrary edge coloring. Give each nonbacktracking oriented two-edge walk \((u,v,w)\), with \(u\ne w\), a bit \(b(u,v,w)\). Assume
\[
b(u,v,w)=c(uv)+c(vw)\pmod2\qquad\text{if }uw\notin E,\tag{2}
\]
and
\[
b(u,v,w)+b(w,v,u)=1\pmod2\qquad\text{if }uw\in E.\tag{3}
\]
Thus a turn with nonadjacent outside vertices tests agreement of its incident edge colors, whereas a turn belonging to a triangle has an arbitrarily oriented comparison. The two conditions are equivalent to a reversal law
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E\}},
\]
together with the potential condition (2) on nontriangular turns.

Call a vertex-simple path \(P=(v_0,\ldots,v_\ell)\) **accepted** if \(\{v_{i-1}v_i:1\le i\le\ell\}\) is independent in \(N\) and \(b(v_{i-1},v_i,v_{i+1})=0\) for every internal turn.

**Theorem (two-color triangular-turn terminal bound).** Under (1)--(3), there exists an accepted path of at least
\[
\boxed{\ell\ge\frac12\sqrt{\bar d(G)},\qquad \bar d(G)=\frac{2|E|}{|V|}}\tag{4}
\]
edges. Its edge set can be chosen monochromatic under \(c\).

*Proof.* Partition \(E=E_0\sqcup E_1\) by the edge coloring \(c\). At least one color class, say \(E_s\), has at least \(|E|/2\) edges. Hence the spanning monochromatic subgraph \(G_s=(V,E_s)\) has average degree at least \(\bar d(G)/2\). Some nontrivial connected component \(H\) of \(G_s\) has average degree at least \(\bar d(G)/2\).

For every vertex \(v\in V(H)\), define a tournament on the incident edges of \(H\). Given two incident edges \(uv\), \(vw\), if \(u,w\) are adjacent in \(G\), orient their tournament comparison from \(uv\) to \(vw\) when \(b(u,v,w)=0\), and in the opposite direction otherwise. Condition (3) ensures that one orientation is accepted. If \(u,w\) are nonadjacent in \(G\), both edges have color \(s\), so (2) gives
\[
b(u,v,w)=c(uv)+c(vw)=0,
\]
and the reversed turn also has value zero. Either orientation may be chosen in the tournament. Thus **every forward comparison of these vertex-star tournaments is an accepted turn**.

The restriction \(N|E(H)\) has independent vertex stars and dependent graph cycles, by (1). Apply the cycle-dominating resource-matroid terminal-path theorem to \(H\) with the constructed local tournaments. It gives a path with \(N\)-independent edge set, all its turns accepted, and at least
\[
\sqrt{\bar d(H)/2}\ge\sqrt{\bar d(G)/4}
\]
edges. Since the path lies in \(H\subseteq G_s\), all its edges also have color \(s\). \(\square\)

**Corollary (common spectral-root bound).** Let \(G=H(k,q)=K_q^{\square k}\), \(k\ge1,q\ge2\), and let \(N=N_{\rm sp}(G)\) be its canonical second-adjacency-eigenspace edge-difference matroid. Then (1) holds, \(\bar d(G)=k(q-1)\), and every turn system (2)--(3) admits an accepted \(N\)-independent path of at least
\[
\boxed{\frac12\sqrt{k(q-1)}}\tag{5}
\]
edges.

*Proof.* The second-eigenspace difference vectors are supported within individual Cartesian factors, representing a direct sum of \(k\) copies of \(M(K_q)\). The vectors in every vertex star form a basis of \(N\). Graph cycles are dependent because their oriented edge differences telescope to zero. The graph is \(k(q-1)\)-regular. Apply (4). \(\square\)

**Canonical specializations.** For \(G=Q_n=H(n,2)\), every nonbacktracking turn has nonadjacent outside vertices, so the turn condition (2) reduces to \(b(u,v,w)=c(uv)+c(vw)\). An accepted resource-independent path is a monochromatic coordinate-distinct cube geodesic. Consequently **every** binary coloring of the edges of \(Q_n\), without any antipodal condition, admits such a geodesic of at least \(\frac12\sqrt n\) edges.

For \(G=K_n=H(1,n)\), every turn has adjacent outside vertices; (3) is the reversal-odd boundary 3-tournament rule, and condition (2) is vacuous. Here the auxiliary edge coloring \(c\) may be chosen constant. Applying the terminal-path theorem directly to the full \(K_n\) recovers the stronger boundary estimate
\[
\ell\ge\sqrt{(n-1)/2}.\tag{6}
\]
The spectral resource matroid is \(M(K_n)\), so independence is equivalent to vertex simplicity along a path.

These instances share a single accepted-turn predicate, a single star-independent cycle-dominating resource matroid hypothesis, and a common terminal-set counting proof. To force the full \(n\)-edge cubical geodesic, an additional global condition must strengthen the square-root estimate (5).

Let \(D_F(u,v)\) be the greatest length of a vertex-simple path from \(u\) to \(v\) in a finite graph \(F\), with \(D_F(v,v)=0\) and \(D_F(u,v)=-\infty\) for vertices in different connected components. For connected \(F\), write
\[
S_F(z)=\sum_{v\in V(F)}D_F(z,v),\qquad
W_D(F)=\sum_{\{u,v\}\subseteq V(F)}D_F(u,v).
\]

**Lemma 1 (rooted detour bound).** For every connected graph \(F\) with \(m\) edges and root \(z\),
\[
\boxed{S_F(z)\ge m.}\tag{1}
\]
*Proof.* Run undirected depth-first search rooted at \(z\), obtaining a rooted tree \(T\). Every edge of \(F\) connects a vertex to an ancestor in \(T\). Assign the edge to its deeper endpoint \(v\). The number of edges so assigned is at most the depth \(d_T(z,v)\), because different assigned edges reach different ancestors of \(v\). Therefore
\[
m\le\sum_vd_T(z,v)\le\sum_vD_F(z,v)=S_F(z).
\]
Each tree path is a simple path of \(F\). \(\square\)

**Lemma 2 (one-vertex gluing).** Let connected graphs \(A,B\) meet at a single vertex \(z\), with no other connections, and have respective orders \(a,b\) and sizes \(m_A,m_B\). Then
\[
W_D(A\cup B)=W_D(A)+W_D(B)+(b-1)S_A(z)+(a-1)S_B(z).\tag{2}
\]
If each summand satisfies \(W_D(A)\ge(a-1)m_A\) and \(W_D(B)\ge(b-1)m_B\), then their union \(F\), of order \(a+b-1\) and size \(m_A+m_B\), satisfies
\[
\boxed{W_D(F)\ge(|V(F)|-1)|E(F)|.}\tag{3}
\]
*Proof.* A simple path between vertices in \(A\) cannot leave \(A\), because its return would repeat \(z\). For \(u\in A-\{z\}\), \(v\in B-\{z\}\), the longest simple \(u\)-to-\(v\) path concatenates a longest \(u\)-to-\(z\) path in \(A\) with a longest \(z\)-to-\(v\) path in \(B\). Thus \(D_F(u,v)=D_A(u,z)+D_B(z,v)\); summing the three pair types gives (2). Lemma 1 supplies \(S_A(z)\ge m_A\) and \(S_B(z)\ge m_B\). Substitution gives
\[
W_D(F)\ge(a-1)m_A+(b-1)m_B+(b-1)m_A+(a-1)m_B=(a+b-2)(m_A+m_B).
\]
\(\square\)

**Theorem 3 (natural detour-index classes).** Every block graph, every cactus graph, and every outerplanar graph \(F\) satisfies \(W_D(C)\ge(|V(C)|-1)|E(C)|\) in each connected component \(C\).

*Proof.* A complete graph \(K_s\) has \(D(u,v)=s-1\) for every distinct pair, giving equality \(W_D(K_s)=(s-1)\binom{s}{2}\). On a cycle \(C_s\), the longer arc between any pair is a simple path of length at least \(s/2\); for \(s\ge4\),
\[
W_D(C_s)\ge\tbinom{s}{2}\frac{s}{2}\ge s(s-1),
\]
and for \(s=3\) the cycle is a clique. Lemma 2 propagates the bound through cut vertices, proving the claims for block graphs (all blocks cliques) and cactus graphs (all blocks cycles or bridges).

For outerplanar graphs it suffices to consider a two-connected block of order \(s\). Such a block has a Hamiltonian outer-face boundary and at most \(2s-3\) edges. When \(s\ge6\), its cycle already guarantees
\[
W_D(F)\ge\tbinom{s}{2}\frac{s}{2}\ge(s-1)(2s-3)\ge(s-1)|E(F)|.
\]
For \(s=5\), the cycle provides detours of length at least three for all ten unordered pairs, so \(W_D(F)\ge30>4(2s-3)=28\). For \(s=4\), the four-cycle has detour index \(16>3(2s-3)=15\). For \(s=3\), the block is \(K_3\). Lemma 2 concludes the proof. \(\square\)

**Theorem 4 (detour-index criterion for arbitrary endpoint weights).** Suppose every connected component \(C\) of a graph \(F\) of order \(s\ge2\) satisfies \(W_D(C)\ge(s-1)|E(C)|\). Then, for every real weight function \(w:V(F)\to\mathbb R\),
\[
\boxed{
\sum_{v\in V(F)}\max_{u\in V(F)}
\bigl(w(u)+D_F(u,v)\bigr)\ge\sum_{v\in V(F)}w(v)+2|E(F)|.
}\tag{4}
\]
*Proof.* For each nontrivial component \(C\) independently choose a uniform random derangement \(\pi_C\). The image \(\pi_C(v)\) is uniformly distributed over the other \(s-1\) vertices. Thus
\[
\mathbb E\sum_{v\in C}D_C(\pi_C(v),v)
=\frac{2W_D(C)}{s-1}\ge 2|E(C)|.
\]
Set \(\pi(v)=v\) for isolated vertices. Some component-preserving permutation \(\pi\) has \(\sum_vD_F(\pi(v),v)\ge2|E(F)|\). For arbitrary weights, the left side of (4) is at least
\[
\sum_v \bigl(w(\pi(v))+D_F(\pi(v),v)\bigr)
=\sum_v w(v)+\sum_vD_F(\pi(v),v),
\]
as required. \(\square\)

**Theorem 5 (matroidal Hamming-product density theorem).** Let
\[
G=\mathop{\square}_{j=1}^{t}K_{m_j},\quad
R=\bigoplus_{j=1}^{t} M(K_{m_j}),
\]
and label an edge changing coordinate \(j\) from symbol \(a\) to \(b\) by the graphic root resource \((j,\{a,b\})\). Let \(H\) be any edge-subgraph of \(G\), retaining all vertices. Assume that every graph of \(H\)-edges within every one-coordinate fiber satisfies the componentwise detour-index criterion of Theorem 4. Then \(H\) has a simple path with an \(R\)-independent set of edge labels and length at least
\[
\boxed{\left\lceil\frac{2|E(H)|}{|V(G)|}\right\rceil.}\tag{5}
\]
This holds whenever the fiber graphs are block graphs or outerplanar graphs.

*Proof.* Fix factor order \(1,\ldots,t\). Let \(L_0(x)=0\), and inductively let \(L_j(x)\) be the greatest length of a path of \(H\) ending at \(x\) that uses only factors \(1,\ldots,j\), in nondecreasing factor order, traversing within each factor a single simple path among that factor's symbols. Each such path has \(R\)-independent labels: in each factor the traversed roots form a simple graph path, a forest in \(M(K_{m_j})\), and distinct factors belong to different direct summands. These paths are vertex-simple because their potential \(\phi(x)=\oplus_i e_{x_i}\) is injective and a repeated vertex would produce a dependence among traversed root vectors.

Fix a \(j\)-coordinate fiber \(F\). Any preceding path using only the first \(j-1\) factors keeps coordinate \(j\) fixed at some \(u\). Extending it by a simple path along fiber \(F\) from \(u\) to \(v\) retains root independence and vertex simplicity. Hence the dynamic-programming recurrence is
\[
L_j(v)=\max_{u\in V(F)}\{L_{j-1}(u)+D_F(u,v)\}.\tag{6}
\]
Apply (4) to the weights \(L_{j-1}\) in every such fiber. Sum the resulting inequalities over fibers and successively over \(j\):
\[
\sum_{x\in V(G)}L_t(x)\ge 2|E(H)|.
\]
Some terminal \(x\) therefore has \(L_t(x)\ge 2|E(H)|/|V(G)|\); integrality proves (5). \(\square\)

**Corollary 6 (canonical models).** All edge-subgraphs of \(Q_n=(K_2)^{\square n}\) satisfy the hypothesis of Theorem 5, since their one-coordinate fibers are isolated vertices or \(K_2\). The conclusion recovers the Leader--Long density theorem for coordinate-distinct cube geodesics and yields monochromatic paths of at least \(n/2\) edges in each color for antipodally odd colorings. The other canonical source model \(U_{2,n}\) has rank-one reduction \(U_{1,n}\), with basis graph \(K_n\) and resource matroid \(M(K_n)\): here the full graph's fiber is a clique, so the theorem guarantees a graphic-independent length-\((n-1)\) path. Boundary coloring resides instead on oriented two-edge windows, so the earlier root-basis tournament path theorem controls its unrestricted monochromatic \(\Omega(\sqrt n)\) paths.

**Remaining conjecture.** It remains to show whether \(W_D(F)\ge(|V(F)|-1)|E(F)|\) holds for every finite connected graph. The preceding results reduce any counterexample to a two-connected graph and prove the conjecture on natural families independent of either NORI construction. The full monochromatic antipodal cube geodesic requires further use of its global color-reversal polarity.

##### Rooted strengthening and reduction to two-connected blocks

The preceding detour-index theorem has a stronger rooted version on these graph families. For a connected graph \(F\), define
\[
\Delta_F(z)=S_F(z)-2|E(F)|+\deg_F(z).
\]
The proposed unrestricted **rooted detour inequality** is \(\Delta_F(z)\ge0\) for every root \(z\).

**Lemma 8 (rooted inequality is preserved by one-sums).** Suppose connected graphs \(A,B\) meet in one cut vertex \(q\), and \(\Delta_A(x)\ge0\) and \(\Delta_B(y)\ge0\) for every respective root \(x,y\). Then \(\Delta_{A\cup B}(z)\ge0\) for every root \(z\) of their union.

*Proof.* At the shared root, \(S_{A\cup B}(q)=S_A(q)+S_B(q)\), and both edge counts and degrees add, so \(\Delta_{A\cup B}(q)=\Delta_A(q)+\Delta_B(q)\ge0\). For a root \(z\in A-\{q\}\), maximal simple paths from \(z\) to \(B-\{q\}\) pass through \(q\). Hence
\[
S_{A\cup B}(z)=S_A(z)+S_B(q)+(b-1)D_A(z,q),
\]
where \(b=|V(B)|\). Since \(\deg_{A\cup B}(z)=\deg_A(z)\), this gives
\[
\Delta_{A\cup B}(z)=\Delta_A(z)+\Delta_B(q)+(b-1)D_A(z,q)-\deg_B(q)\ge0.
\]
Here \(D_A(z,q)\ge1\) and \(\deg_B(q)\le b-1\). The other case is symmetric. \(\square\)

**Theorem 9 (rooted inequality for outerplanar, cactus, and block graphs).** Every graph belonging to any of these three classes satisfies, in each connected component and for every root \(z\),
\[
\boxed{\sum_{v\in V(F)}D_F(z,v)\ge2|E(F)|-\deg_F(z).}\tag{8}
\]

*Proof.* For a clique \(K_s\), every root-to-other-vertex detour has length \(s-1\), so \(S(z)=(s-1)^2=2\binom{s}{2}-(s-1)\). For a cycle \(C_s\), its two neighbors of \(z\) can each be reached around the opposite arc in \(s-1\) edges. Thus \(S(z)\ge 2(s-1)=2|E(C_s)|-\deg(z)\). Lemma 8 settles block graphs and cacti.

For a two-connected outerplanar graph \(F\) of order \(s\), the Hamiltonian outer-face cycle provides two root-to-neighbor detours of length \(s-1\), and each of the remaining \(s-3\) vertices is reachable along the longer of two cycle arcs, giving a detour of length at least \(s/2\). Therefore
\[
S_F(z)\ge 2(s-1)+(s-3)\frac{s}{2}
=\frac{s^2+s-4}{2}.
\]
For \(s\ge4\), this is at least \(4s-8\), since the difference is \((s-3)(s-4)/2\). Outerplanarity gives \(m\le2s-3\), and two-connectivity gives \(\deg_F(z)\ge2\), so
\[
2m-\deg_F(z)\le4s-8\le S_F(z).
\]
For \(s=3\), the block is \(K_3\). Lemma 8 extends the result from blocks to all outerplanar graphs. \(\square\)

**Corollary 10 (rooted inequality implies the conjectural unrestricted weighted theorem).** If the rooted inequality (8) holds for every connected graph \(F\), then the detour-index inequality \(W_D(F)\ge(|V(F)|-1)|E(F)|\), and hence Theorems 4--5 without fiber restrictions, follow.

*Proof.* Summing (8) over all \(n\) choices of root gives
\[
2W_D(F)=\sum_z S_F(z)\ge 2n|E(F)|-\sum_z\deg_F(z)
=2(n-1)|E(F)|.
\]
Apply the derangement argument of Theorem 4 to deduce the unrestricted weighted inequality. \(\square\)

The rooted inequality is presently a **conjecture** outside the proved graph families. Lemma 8 reduces its search for counterexamples to two-connected blocks. The rooted and unrooted assertions have been tested on all connected labeled graphs of order at most six and on samples of seven-vertex graphs, without yielding a counterexample; such finite checks are diagnostic only.

##### Complete bipartite and complete split blocks

Two families with arbitrarily large non-outerplanar two-connected blocks also satisfy the rooted inequality, with explicit slack.

**Theorem 11 (complete bipartite blocks).** Let \(F=K_{a,b}\), where \(1\le a\le b\). For a root \(z\) in the part of size \(a\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg_F(z))=2(a-1)^2.}\tag{9}
\]
For a root \(z\) in the part of size \(b\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg_F(z))=
\begin{cases}
2(a-1)^2,&b=a,\\
2a(a-1),&b>a.
\end{cases}}\tag{10}
\]
In particular every complete bipartite graph satisfies the rooted detour inequality.

*Proof.* A simple path in a bipartite graph alternates the two parts. The greatest possible length of a path from a vertex of the smaller part to a vertex of the other part is \(2a-1\); between two vertices of the smaller part it is \(2(a-1)\). Between two vertices of the larger part it is \(2a\) when \(b>a\), and \(2(a-1)\) when \(b=a\). These maxima are attained by alternating paths using the allowed number of vertices in each part. Thus, for a root in the smaller part,
\[
S_F(z)=2(a-1)^2+b(2a-1),\quad
2|E(F)|-\deg(z)=2ab-b=b(2a-1),
\]
giving (9). For a root in the larger part and \(b>a\),
\[
S_F(z)=2a(b-1)+a(2a-1),\quad
2|E(F)|-\deg(z)=2ab-a.
\]
Subtracting yields \(2a(a-1)\). When \(a=b\), the two parts are symmetric and (9) applies. \(\square\)

**Theorem 12 (complete split blocks).** Let \(F=K_s\vee\overline{K_t}\), with \(s\ge1\) clique vertices and \(t\ge1\) independent vertices. Write \(C\) for the clique part and \(I\) for the independent part. For \(z\in C\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg(z))=
\begin{cases}
t(t-1),&t\le s-1,\\
(s-1)^2,&t\ge s.
\end{cases}}\tag{11}
\]
For \(z\in I\),
\[
\boxed{S_F(z)-(2|E(F)|-\deg(z))=
\begin{cases}
(t-1)^2,&t\le s,\\
s(s-1),&t\ge s+1.
\end{cases}}\tag{12}
\]
In particular every complete split graph satisfies the rooted detour inequality.

*Proof.* Let \(L_{CC},L_{CI},L_{II}\) be the greatest simple-path lengths between two distinct vertices of the indicated types. In a path, independent vertices must be separated by clique vertices. Conversely any ordering of the required clique and independent vertices respecting that separation is a path in the join. Consequently
\[
L_{CC}=s+\min(t,s-1)-1,\quad
L_{CI}=s+\min(t,s)-1,\quad
L_{II}=s+\min(t,s+1)-1.
\]
(The \(CC\) and \(II\) expressions are used only if those endpoint types occur.) Therefore
\[
S_F(z)=
\begin{cases}
(s-1)L_{CC}+tL_{CI},& z\in C,\\
sL_{CI}+(t-1)L_{II},& z\in I.
\end{cases}
\]
The graph has \(m=\binom{s}{2}+st\) edges, a clique vertex has degree \(s-1+t\), and an independent vertex has degree \(s\). Substituting the three displayed path-length formulas and simplifying in the two threshold ranges gives (11) and (12). Every right-hand side is nonnegative. \(\square\)

**Corollary 13 (high-treewidth fiber family).** The rooted inequality (8), the detour-index hypothesis of Theorem 4, and the weighted endpoint inequality (4) hold on every connected graph whose blocks belong to the union of the following classes: outerplanar graphs, complete bipartite graphs, and complete split graphs. Consequently Theorem 5 holds for arbitrary Hamming-product edge-subgraphs all of whose one-coordinate fiber components have blocks of these types.

*Proof.* Theorems 9, 11, and 12 establish the rooted bound on each block, and Lemma 8 propagates it through the block-cut tree. Summing over roots and applying Theorem 4 establishes the weighted inequality. Theorem 5 then applies fiberwise. \(\square\)

These new block families include two-connected graphs of arbitrarily large treewidth (complete bipartite graphs with both part sizes increasing, and dense complete split graphs). They extend the preceding result beyond sparse planar exchange geometries. The stronger unrestricted rooted inequality remains open.

##### Dominant independent parts and complete multipartite graphs

We extend the rooted-detour inequality to graphs containing a complete bipartite spanning subgraph with a sufficiently large independent side, and thence to all complete multipartite graphs. The proofs use the preceding complete-bipartite slack formulas and the classical Ore Hamiltonian-connectedness theorem.

**Theorem 14 (stability under filling the smaller side of a biclique).** Let \(a\ge b\ge1\) be integers. Let \(A,B\) be disjoint vertex sets of cardinalities \(a,b\). Define
\[
G=\overline{K_a}\vee H,
\]
where \(H\) is an arbitrary simple graph on \(B\); thus \(A\) is independent and all \(ab\) edges between \(A,B\) belong to \(G\). Then for every root \(z\in V(G)\),
\[
\boxed{S_G(z)\ge 2|E(G)|-\deg_G(z).}\tag{13}
\]
For \(b\ge2\), a uniform lower bound for the rooted slack is
\[
\Delta_G(z):=S_G(z)-2|E(G)|+\deg_G(z)
\ge(b-1)(b-2).
\tag{14}
\]

*Proof.* Let \(G_0=K_{a,b}\subseteq G\), and let \(e=|E(H)|\le\binom b2\). Since adding edges does not reduce any longest simple-path length, \(S_G(z)\ge S_{G_0}(z)\). Also
\[
|E(G)|=ab+e,\qquad
\deg_G(z)=\deg_{G_0}(z)+\deg_H(z),
\]
where \(\deg_H(z)=0\) for \(z\in A\). Therefore
\[
\Delta_G(z)\ge\Delta_{G_0}(z)-2e+\deg_H(z)
\ge\Delta_{G_0}(z)-2e.
\tag{15}
\]
The complete-bipartite formulas in Theorem 11 give \(\Delta_{G_0}(z)\ge 2(b-1)^2\) for every root: the smaller part of \(K_{a,b}\) has order \(b\), and the displayed root slack on either side has this lower bound. Thus
\[
\Delta_G(z)\ge2(b-1)^2-b(b-1)=(b-1)(b-2)\ge0
\]
when \(b\ge2\). If \(b=1\), the only possible \(H\) has no edges and \(G=K_{a,1}\), already covered by Theorem 11. \(\square\)

The theorem allows an arbitrary pattern of up to \(\binom b2\) internal edges on \(B\), independent of whether the resulting graph is chordal, planar, or multipartite. The hypothesis is intrinsic: \(G\) contains an independent set of size at least half its order, every vertex of which is adjacent to every vertex outside that set.

**Theorem 15 (all complete multipartite graphs).** Every connected complete multipartite graph \(G=K_{a_1,\ldots,a_t}\) satisfies the rooted-detour inequality (13) for every root.

*Proof.* Let \(n=\sum_i a_i\) and \(a=\max_i a_i\). If \(a\ge n/2\), choose a part \(A\) of order \(a\) and let \(B=V(G)\setminus A\) have size \(b=n-a\le a\). All edges between \(A\) and \(B\) occur and \(A\) is independent. Theorem 14 applies, regardless of the internal multipartite graph on \(B\).

Now suppose \(a<n/2\). Since \(a\) is integral, \(a\le(n-1)/2\). Every nonadjacent pair \(u,v\) belongs to one common part of cardinality \(s\le a\), so
\[
\deg_G(u)+\deg_G(v)=2(n-s)\ge n+1.
\]
By Ore's Hamiltonian-connectedness theorem (Ore's degree-sum criterion for Hamiltonian-connected graphs, as recalled in Gould–Yu, *On hamiltonian-connected graphs*, J. Graph Theory 18 (1994), 841–860), \(G\) has a Hamiltonian path between every pair of distinct vertices. Hence \(D_G(z,v)=n-1\) for every \(v\ne z\), and
\[
S_G(z)=(n-1)^2\ge\sum_{v\ne z}\deg_G(v)=2|E(G)|-\deg_G(z),
\]
since every degree is at most \(n-1\). For orders \(n\le2\) the claim follows by direct inspection. \(\square\)

**Corollary 16 (weighted detours and Hamming products).** The weighted endpoint inequality (4) holds for every graph whose connected components are complete multipartite, or whose blocks are complete multipartite, outerplanar, complete bipartite, or complete split graphs. The matroidal Hamming-product density theorem (Theorem 5) therefore applies whenever all one-coordinate fiber components have blocks from this enlarged list.

*Proof.* Theorem 15 and Lemma 8 verify the rooted inequality through one-sum gluing. Summation over roots yields the detour-index inequality; Theorem 4 supplies arbitrary endpoint weights, which Theorem 5 propagates factor by factor. \(\square\)

The complete-multipartite result covers high-connectivity and arbitrarily large graphic circuits without requiring a bounded treewidth or chordal graph structure. It leaves the unrestricted rooted-detour and vertex-deletion conjectures open.


##### Augmentation from a Hamiltonian-connected core

**Theorem 17 (sharp vertex-deletion inequality).** Let \(G\) be connected and \(H=G-v\) Hamiltonian-connected. Write \(N=|V(H)|\), \(K=N_G(v)\), and \(k=|K|\). Then for every \(z\in V(H)\),
\[
\boxed{S_G(z)-S_H(z)\ge 2k-\mathbf1_{\{z\in K\}}.}\tag{16}
\]
Consequently the rooted-detour inequality holds at every root of \(G\).

*Proof.* For \(N=1\) the graph is \(K_2\). Suppose \(N\ge2\). If \(K=\{z\}\), then \(D_G(z,v)=1=2k-\mathbf1_{\{z\in K\}}\) and every old endpoint detour can only increase. In every other case there is a neighbor \(u\in K-\{z\}\). A Hamiltonian \(z\)-to-\(u\) path in \(H\), followed by \(uv\), shows \(D_G(z,v)=N\). Every existing endpoint \(w\ne z\) has \(D_H(z,w)=N-1\), and its new detour length is either \(N-1\) or \(N\). The latter occurs whenever a Hamiltonian \(z\)-to-\(w\) path in \(H\) has two consecutive vertices in \(K\): insert \(v\) between them.

If \(2k-\mathbf1_{\{z\in K\}}\le N\), the newly available endpoint \(v\) supplies the claimed increase. If \(k>\lceil N/2\rceil\), any Hamiltonian path in \(H\) has two consecutive vertices in \(K\), since at most \(\lceil N/2\rceil\) positions of a path can be chosen without consecutive positions. All \(N-1\) old endpoints therefore gain one, and \(S_G(z)-S_H(z)=2N-1\ge2k-\mathbf1_{\{z\in K\}}\). The sole remaining possibility is \(N=2m-1\), \(k=m\), \(z\notin K\). Choose \(w\in K\) and a Hamiltonian \(z\)-to-\(w\) path in \(H\). An alternating placement of \(m\) marked \(K\)-vertices among \(2m-1\) positions with no adjacent marks must start with a marked position; since \(z\notin K\), a consecutive \(K\)-pair must occur. Inserting \(v\) gives a gain of one at endpoint \(w\), producing the required increment \(N+1=2m=2k\). This proves (16).

Because \(H\) is Hamiltonian-connected, \(S_H(z)=(N-1)^2\ge 2|E(H)|-\deg_H(z)\); adding (16) proves the rooted inequality on \(H\)'s vertices. At root \(v\) there are two cases. If \(k\ge2\), for each \(w\in H\) choose \(u\in K-\{w\}\), traverse a Hamiltonian \(u\)-to-\(w\) path of \(H\) after the initial edge \(vu\), and obtain \(D_G(v,w)=N\). Thus \(S_G(v)=N^2\ge 2|E(H)|+k=2|E(G)|-\deg_G(v)\). If \(k=1\), let \(u\) be the sole neighbor; then
\[
S_G(v)=N+S_H(u)=N+(N-1)^2
\ge2|E(H)|+1=2|E(G)|-\deg_G(v).
\]
This completes the proof. \(\square\)

The result is an unconditional one-vertex extension theorem for *arbitrary attachment neighborhoods*, provided the core is Hamiltonian-connected. Its proof isolates the failure mechanism for general vertex deletion: the desired detour increment is available by inserting a vertex between adjacent neighbors on a long endpoint path. It remains open whether an aggregate version of this argument works for arbitrary connected deletion cores.


Let \(G=H(k,3)=K_3^{\square k}\), \(k\ge1\), with canonical edge-resource matroid \(N=N_{\mathrm{sp}}(G)\cong\bigoplus_{j=1}^kM(K_3)\). Let \(c:E(G)\to\mathbb F_2\) and let \(b(u,v,w)\) label ordered two-edge turns under the intrinsic rules
\[
b(u,v,w)+b(w,v,u)=\mathbf1_{\{uw\in E(G)\}}\pmod2,\qquad
b(u,v,w)=c(uv)+c(vw)\quad\text{if }uw\notin E(G).\tag{1}
\]
A path is **accepted** if all internal \(b\)-turns are zero and its edge resources are independent in \(N\).

A **coordinate triangle** arises by fixing all but one coordinate. If its three edges are monochromatic, its three unoriented two-edge walks have one accepted orientation apiece. These orientations induce a tournament on their endpoint pairs. Call the triangle **defective** if this tournament is transitive; let \(B\) be the total number of defective coordinate triangles.

**Theorem (ternary turn conservation).** There exists an accepted monochromatic \(N\)-independent path of length
\[
\boxed{\ell\ge\left\lceil k-\frac{B}{2\cdot3^k}\right\rceil\ge\left\lceil\frac{5k}{6}\right\rceil.}\tag{2}
\]
Consequently the Hamming-root factor-count conjecture \(\ell\ge k\) holds for all \(k\le5\); it also holds for arbitrary \(k\) whenever no coordinate triangle is defective. In particular, it holds whenever every coordinate triangle is bichromatic.

*Proof.* Let \(F\) be any subgraph of a coordinate \(K_3\) whose edges have one fixed color. Let \(D_F(u,v)\) denote the greatest length of an accepted simple \(u\)-to-\(v\) path within \(F\), taking \(D_F(u,u)=0\) and \(-\infty\) for unreachable pairs. Every single edge is accepted. Put \(\delta(F)=1\) if \(F=K_3\) and its accepted two-step endpoint tournament is transitive; put \(\delta(F)=0\) otherwise.

**Local permutation lemma.** There exists a permutation \(\pi\) of the three vertices of \(F\), using only reachable source-target pairs, for which
\[
\sum_v D_F(\pi(v),v)\ge 2|E(F)|-\delta(F).\tag{3}
\]
For zero edges choose the identity; for one edge transpose its endpoints to obtain total length two. For two edges \(F=a-b-c\), reversal oddness on its triangular turn accepts one of \(a-b-c\), \(c-b-a\). If the former is accepted, use the cyclic source-target assignment \(a\to c,\ c\to b,\ b\to a\), giving total length \(2+1+1=4\); reverse it in the other case. For three edges, each ordered pair has a direct path of length one, and one orientation of each two-edge path is accepted. These longer path orientations constitute a tournament on three vertices. Its cyclic case admits a cyclic permutation with three length-two paths, total six. Its transitive case admits a cyclic permutation with two forward arcs of length two and one reverse arc of length one, total five. This establishes (3).

For any real weight function \(w\) on the three vertices, put \(T_F(w)(v)=\max_u\{w(u)+D_F(u,v)\}\). The permutation lemma implies
\[
\sum_v T_F(w)(v)\ge\sum_v w(v)+2|E(F)|-\delta(F),\tag{4}
\]
because \(\sum_vw(\pi(v))=\sum_vw(v)\).

Now choose one edge color \(s\). Process coordinates in order \(1,\ldots,k\), and define \(L_j(x)\) as the largest length of a color-\(s\) accepted path ending at \(x\), whose coordinate indices are nondecreasing and whose successive moves within one coordinate visit distinct symbols. Set \(L_0(x)=0\). For each \(j\)-coordinate triangle fiber, with color-\(s\) edge subgraph \(F\), the dynamic-programming recurrence is
\[
L_j(v)=\max_u\{L_{j-1}(u)+D_F(u,v)\}.\tag{5}
\]
The concatenated path is accepted: turns internal to one coordinate segment are accepted by definition of \(D_F\); turns joining different factors have nonadjacent outer vertices, and their label is \(s+s=0\) by (1). Its edge-resource family is independent because within each coordinate factor it is a simple path in the root \(K_3\), hence a forest in the corresponding direct-sum factor \(M(K_3)\). Nondecreasing factor order also makes the full vertex path simple.

Apply (4) to weights \(L_{j-1}\) in every fiber of coordinate \(j\), and sum over the \(3^{k-1}\) fibers. Then
\[
\sum_{x\in V(G)}L_j(x)\ge\sum_xL_{j-1}(x)+2|E_s^{(j)}|-B_s^{(j)},
\]
where \(E_s^{(j)}\) comprises the color-\(s\) edges of the \(j\)-factor and \(B_s^{(j)}\) its defective monochromatic triangles. Summing across coordinates gives
\[
\sum_x L_k^{(s)}(x)\ge 2|E_s|-B_s.\tag{6}
\]
Summing (6) over the two colors gives
\[
\sum_x\bigl(L_k^{(0)}(x)+L_k^{(1)}(x)\bigr)
\ge 2|E(G)|-B=2k3^k-B.
\]
Thus some color and some terminal vertex satisfy
\[
L_k^{(s)}(x)\ge k-\frac B{2\cdot3^k}.
\]
There are \(k3^{k-1}\) coordinate triangles, so \(B\le k3^{k-1}\), and (2) follows. For \(k\le5\), \(\lceil5k/6\rceil=k\); if \(B=0\), the first inequality gives \(\ell\ge k\). \(\square\)

**Interpretation.** The local weighted transfer contribution equals \(2|E(F)|\) except for a transitive monochromatic coordinate triangle, which can lose one unit. Every other fiber, including a bichromatic triangle, conserves the full weighted transfer budget. This gives the first linear-in-\(k\) bound for arbitrary polarized ternary Hamming systems, establishes the full factor-count guarantee in dimensions \(k\le5\), and reduces the unrestricted ternary gap to controlling global compensation for transitive monochromatic triangles. The binary endpoint remains the NORI1 antipodal spanning problem.

**Corollary (critical six-factor rigidity).** If a triangular-turn system on \(H(6,3)\) has no accepted monochromatic resource-independent path of length six, then (i) all \(6\cdot3^5=2\cdot3^6\) coordinate triangles are defective, hence monochromatic with transitive accepted-turn tournaments; (ii) there are \(3^6\) defective triangles of each color; and (iii) for every permutation \(\sigma\) of the six factor indices, each color \(s\), and each terminal vertex \(x\), the longest accepted color-\(s\) path whose coordinate segments occur in order \(\sigma\) and do not revisit a symbol within one segment has length five.

*Proof.* Put \(V=3^6\). The bound (2) forces \(B\ge2V\) if no length-six path exists, while the total number of coordinate triangles equals \(2V\). Thus every coordinate triangle is defective. Let \(B_s\) count the defective triangles of color \(s\). Every edge of color \(s\) lies in one of these monochromatic coordinate triangles, so \(|E_s|=3B_s\). The transfer inequality (6) gives
\[
\sum_x L_6^{(s)}(x)\ge2|E_s|-B_s=5B_s.
\]
Since every terminal length is at most five, the sum is at most \(5V\), hence \(B_s\le V\). As \(B_0+B_1=2V\), equality holds: \(B_0=B_1=V\). Therefore \(\sum_xL_6^{(s)}(x)\ge5V\) while each summand is at most five, so every \(L_6^{(s)}(x)=5\). The dynamic-programming proof is invariant under permutations of the coordinate order, giving the terminal conclusion for every \(\sigma\). \(\square\)

This isolates the equality case: a perfectly balanced system of transitive monochromatic coordinate triangles with flat five-edge terminal profiles under all \(6!\) factor orders.

**Lemma (forced predecessor profile in the critical case).** In the hypothetical six-factor counterexample of the preceding corollary, fix any order of factors, its final factor \(j\), and a coordinate-\(j\) fiber. If the fiber is monochromatic in color \(s\), then the three values of \(L_5^{(s)}\) just before processing that fiber are, in some order,
\[
\boxed{(3,3,4),}\tag{7}
\]
with the value four located at the sink of the fiber's accepted two-step endpoint tournament. For the other color, whose fiber edge subgraph is empty, all three predecessor values are five.

*Proof.* By the corollary, for both colors and every terminal vertex, \(L_6^{(s)}=5\). Equality also holds in every summed local transfer inequality (4): the two colors' total transfer lower bounds sum to the maximum possible \(10\cdot3^6\), and each of their terminal outputs is at most five. Thus on a defective color-\(s\) triangle, with input weights \(w\), the transfer output \(T_F(w)\) is the constant vector \((5,5,5)\) and \(\sum w=10\).

Relabel the triangle so its accepted length-two endpoint tournament is transitive \(a\to b\), \(a\to c\), \(b\to c\). Every direct edge has length one; the accepted length-two arcs have length two. Therefore
\[
T_F(w)(a)=\max\{w_a,w_b+1,w_c+1\},\quad
T_F(w)(b)=\max\{w_b,w_a+2,w_c+1\},\quad
T_F(w)(c)=\max\{w_c,w_a+2,w_b+2\}.
\]
To reach output five at \(a\), some predecessor other than \(a\) must have weight four (the possibility \(w_a=5\) would force the output at \(b\) to be at least seven). Weight four at \(b\) would force output at \(c\) to be at least six. Hence \(w_c=4\). The output constraints at \(b,c\) give \(w_a,w_b\le3\), and the sum \(\sum w=10\) forces \(w_a=w_b=3\). When the fiber has no edges of color \(1-s\), its transfer map is the identity, so the opposite-color predecessor vector is \((5,5,5)\). \(\square\)

Thus a six-factor counterexample would force a specific \((3,3,4)\) profile around every last-factor monochromatic triangle, in every permutation of the six factors.
