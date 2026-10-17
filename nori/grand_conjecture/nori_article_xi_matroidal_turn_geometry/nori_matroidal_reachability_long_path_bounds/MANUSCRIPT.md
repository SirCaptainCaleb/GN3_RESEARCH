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

**Lemma (shared-edge moment).** Fix a direction permutation \(\pi\), take \(\sigma\in S_n\) uniformly, and let \(s\) be the number of cube edges common to the two root-to-antipode geodesics. For every \(z\ge1\),
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

*Proof of the theorem.* Let \(A_\pi\) be the event that the path of direction permutation \(\pi\) is all color \(\epsilon\), and \(q_\pi=\Pr(A_\pi)\). A geodesic uses each direction once, so its edges lie in distinct antipodal orbits, and \(q_\pi=\prod_{f\in P_\pi}p_f\), where \(p_f=\Pr(c(f)=\epsilon)\in[\rho,1-\rho]\). Define
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

**Corollary (face smoothing).** Let \(F\) be an \(m\)-dimensional face of \(Q_n\), \(2\le m\le n\), and fix \(x\in F\) and a color \(\epsilon\). Independently flip the colors on full-cube antipodal edge pairs with probability \(\rho\). Then, uniformly in the initial antipodally odd coloring,
\[
\Pr(\text{no \(\epsilon\)-monochromatic geodesic in \(F\) between opposite face corners})
\le\frac{3e(\rho^{-1}-1)}m
\]
whenever the right side is below one. In particular, the failure probability is \(o(1)\) if \(m\rho\to\infty\).

*Proof.* A face geodesic uses each of its \(m\) free directions once, and hence meets distinct full-cube antipodal edge orbits. If \(F\) is proper, the full-cube antipodal translate of any edge of \(F\) lies outside \(F\), so two face geodesics can share an orbit only by using the same edge. In the full-face case, opposite edges between different geodesics produce incompatible prescribed-color events and contribute zero to their joint probability. Thus the weighted second-moment calculation and the permutation singleton-block bound of the theorem apply in either case, with \(m\) in place of \(n\). \(\square\)

**Lemma (opposite-chain edge exclusion).** Let \(P_\pi\) be the root-to-antipode geodesic given by a permutation \(\pi=(i_1,\ldots,i_n)\), and let \(P_{\pi^R}\) use its reverse permutation. Every root-to-antipode geodesic \(P_\sigma\) shares an edge with at most one of \(P_\pi,P_{\pi^R}\).

*Proof.* In used-direction-set notation relative to the root, the first path has edges between its consecutive prefix sets
\[
A_k=\{i_1,\ldots,i_k\},\qquad 0\le k\le n,
\]
whereas the second has edges between consecutive suffix sets
\[
B_j=\{i_{n-j+1},\ldots,i_n\},\qquad 0\le j\le n.
\]
If a nested direction-set chain contained an edge \(A_k\to A_{k+1}\) followed by an edge \(B_j\to B_{j+1}\), its sets would satisfy \(A_{k+1}\subseteq B_j\). But \(i_1\in A_{k+1}\) and \(i_1\notin B_j\), since \(j\le n-1\). If the suffix edge occurred first, the chain would require \(B_{j+1}\subseteq A_k\), contradicted by \(i_n\in B_{j+1}\) and \(i_n\notin A_k\). These exhaust the possible orders. \(\square\)

**Theorem (full edge-color profile universality).** Under the hypotheses of the rootwise smoothing theorem, fix an arbitrary predetermined word \(w=(w_1,\ldots,w_n)\in\{0,1\}^n\) and a root \(x\). There is a root-to-antipode geodesic whose consecutive edge colors form \(w\), with failure probability at most
\[
\boxed{\frac{2h}{1+h},\qquad
h=\frac{3e(\rho^{-1}-1)}n<1.}
\]
In particular this probability tends to one uniformly in the baseline coloring and prescribed word whenever \(n\rho\to\infty\). The growth condition is necessary for a uniform fixed-root, fixed-word assertion.

*Proof.* For every \(\pi\in S_n\), let \(A_\pi\) be the event that the sequence of colors along \(P_\pi\) is \(w\), let \(q_\pi=\Pr(A_\pi)>0\), and set \(Z=\sum_\pi\mathbf1_{A_\pi}/q_\pi\). Since each direction is used once, a single path visits distinct antipodal noise-variable orbits and \(\mathbb EZ=n!\).

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

#### Translated block networks amplify global smoothing

The face smoothing estimate can be amplified over many edge-orbit-disjoint networks. This permits a bounded value of \(n\rho\) for a global existence conclusion.

Fix a legal baseline coloring of \(Q_n\) and the same independent antipodal edge-orbit noise of rate \(0<\rho\le1/2\). Put
\[
C_\rho=3e(\rho^{-1}-1).
\]
Partition the directions into \(r\ge2\) nonempty blocks of sizes \(k_1,\ldots,k_r\), each greater than \(C_\rho\), and put \(K=\max_jk_j\). Starting at \(x\), traverse the blocks consecutively, using a full geodesic inside each block face, from its initial corner to its opposite corner. These faces form a network joining \(x\) to \(\bar x\).

**Theorem (global block smoothing).** Uniformly over the baseline,
\[
\boxed{
\Pr(\text{no zero full antipodal geodesic anywhere})
\le
\exp\!\left[
-\frac{2^n}{2\sum_{j=1}^r2^{k_j}}
\prod_{j=1}^r\left(1-\frac{C_\rho}{k_j}\right)
\right].
}\tag{GB1}
\]

*Proof.* Every block face is proper. Its zero connection has probability at least \(1-C_\rho/k_j\), by the preceding face corollary. Different faces in a network use disjoint direction sets, and hence disjoint noise orbits, so their success events are independent. A network therefore succeeds with probability at least
\[
p=\prod_j(1-C_\rho/k_j).
\]
A successful network concatenates to a zero full antipodal geodesic.

Consider all \(2^n\) translations of this network. Two translates can share a noise orbit only through faces belonging to the same direction block. For that block \(I_j\), the translation difference must lie in its binary span or in the antipodal translate of that span: outside \(I_j\), the two faces must have identical or complementary fixed bits. There are at most \(2\sum_j2^{k_j}\) such translation differences.

Greedy packing supplies at least \(2^n/(2\sum_j2^{k_j})\) networks with pairwise disjoint noise-orbit sets. Their success events are independent, each of probability at least \(p\). Global failure implies that all packed networks fail. Use \((1-p)^t\le e^{-pt}\) to obtain (GB1). \(\square\)

**Corollary (global smoothing at a bounded reciprocal-dimension rate).** For every fixed \(A>6e\), if \(\rho=A/n\) for sufficiently large \(n\), then for some \(c_A>0\),
\[
\boxed{
\Pr(\text{no zero full antipodal geodesic anywhere})
\le\exp(-c_A2^{n/2}).
}\tag{GB2}
\]
The same conclusion holds whenever \(\liminf n\rho>6e\).

*Proof.* Use two blocks of sizes \(\lfloor n/2\rfloor,\lceil n/2\rceil\). Their failure bounds have limits at most \(6e/A<1\), so their joint success probability is uniformly bounded below by a positive constant. The packing size is at least \(2^{\lfloor n/2\rfloor-2}\). The same argument uses any fixed lower bound \(A>6e\) for \(n\rho\). \(\square\)

The root and direction order may depend on the perturbed coloring. The fixed-root threshold proved earlier remains \(n\rho\to\infty\); (GB2) is a global statement with a freely selected root. The constant \(6e\) is a sufficient bound from this calculation, with no optimality claim.

**Corollary (uniform random odd colorings have doubly exponentially small bad probability).** Under the uniform distribution on legal odd cube-edge colorings,
\[
\boxed{
\Pr(\text{no monochromatic full antipodal geodesic})
\le
\exp\!\left(-2^{\,n-O(n^{1/3})}\right).
}\tag{GB3}
\]

*Proof.* Take \(\rho=1/2\), so \(C_\rho=3e\) and the perturbed coloring is uniform over all legal colorings. Partition the directions into \(r=\lfloor n^{2/3}\rfloor\) blocks whose sizes differ by at most one. Then \(K=O(n^{1/3})\), while their minimum size tends to infinity. Using \(\log(1-u)\ge-2u\) for \(0\le u\le1/2\) gives
\[
p=\prod_j(1-3e/k_j)\ge \exp(-O(n^{1/3})).
\]
The packing size is at least \(2^{n-K-1}/r\). Their product is \(2^{n-O(n^{1/3})}\), proving (GB3). Legal antipodal oddness interchanges zero and one geodesics by antipodal translation, so absence of a zero full geodesic is equivalent to absence of both colors. \(\square\)

**Encoding interpretation.** The packed networks use disjoint edge-orbit bits. Given a bad coloring, retain the bits outside them and encode each network's assignment by its index among its failing local assignments, with a single mixed-radix code for the tuple. The baseline, supports and ordered local failure lists determine a decoder. At \(\rho=1/2\), this is an injective encoding saving \(2^{n-O(n^{1/3})}\) bits in logarithmic code-space size. The global entropy-amplification criterion (EA7) requires a saving proportional to \(n2^{n-2}\); that stronger bound remains open.

The corresponding fixed-gauge-phase theorem in the curvature manuscript uses odd block sizes to solve correlated vertex-gauge seam equations. It proves a bad fraction at most \(\exp(-2^{n-O(\sqrt n)})\) inside every individual invariant vertex-gauge orbit. The different exponents reflect the different independence structures of edge-orbit noise and vertex gauges.


#### Independent sparse rounds give exponential face smoothing

Put \(B=3e^2\). The following amplification uses only the proved face second-moment estimate.

**Lemma (independent-round amplification).** Consider an ordinary \(k\)-cube whose edges are independently occupied with probabilities at least \(p\), where \(0<p\le1/2\). Fix opposite corners. The probability that no occupied geodesic joins them is at most
\[
\boxed{q_k(p)=\exp\!\left(-\left\lfloor\frac{kp}{B}\right\rfloor\right).}\tag{SR1}
\]
The assertion also applies when occupancy means matching a prescribed direction-indexed profile or a prescribed positional color word on paths between these corners.

*Proof.* If \(t=\lfloor kp/B\rfloor=0\), the bound is immediate. Otherwise \(k\ge B/p\ge2B\). Generate \(t\) independent edge-percolation rounds, each with occupation probability \(p_0=B/k\le1/2\). In each round, the earlier ordinary-face second-moment bound gives failure probability at most
\[
\frac{3e(p_0^{-1}-1)}{k}\le\frac{3e}{B}=\frac1e.
\]
Consequently all rounds fail with probability at most \(e^{-t}\). Their union has independent edge indicators, with common occupation probability
\[
1-(1-B/k)^t\le tB/k\le p.
\]
Couple this union below the given independent occupation field, adding occupied edges separately as necessary. Connection is increasing in the occupation field, which proves (SR1).

For a direction-indexed profile, the required color of each edge is fixed by its direction. For a positional word, orient the face from its chosen initial corner; an edge joining ranks \(j-1,j\) has required color equal to the \(j\)-th word entry. Thus in both cases matching the prescription defines independent edge indicators of probabilities at least \(p\). \(\square\)

**Theorem (exponential fixed-root smoothing).** In the antipodal edge-orbit noise model, fix a root and either a positional length-\(n\) word or a direction-indexed binary profile. Uniformly over every legal baseline, the probability that no full geodesic from that root realizes the prescription is at most
\[
\boxed{
\exp\!\left(-\left\lfloor\frac{\lfloor n/2\rfloor\rho}{B}\right\rfloor\right)
+
\exp\!\left(-\left\lfloor\frac{\lceil n/2\rceil\rho}{B}\right\rfloor\right).
}\tag{SR2}
\]
In particular it is \(O(\exp[-n\rho/(2B)])\). For the fixed-root monochromatic assertion, the exponential order \(n\rho\) is optimal up to absolute constants.

*Proof.* Fix a partition into two nonempty direction blocks of sizes \(\lfloor n/2\rfloor,\lceil n/2\rceil\). Follow their two series faces from the prescribed root to its antipode. Both faces are proper, so within either face every edge uses a distinct full-cube antipodal noise orbit. Its prescribed-color occupation indicators are independent and each has probability at least \(\rho\). Apply (SR1) and a union bound. The positional prescription restricts to the corresponding consecutive segment in each face; a direction-indexed prescription restricts to its block. Successful face paths concatenate to the required full geodesic.

For the lower bound on the uniform monochromatic failure probability, take a baseline whose root-incident edges all have the opposite color. With probability \((1-\rho)^n\) none flips, preventing the first step. Since \(-\log(1-\rho)\) lies between \(\rho\) and \(2\rho\) for \(0<\rho\le1/2\), this obstruction has probability \(\exp[-\Theta(n\rho)]\). \(\square\)

Splitting into proper faces is essential to the argument: the occupation field on the whole cube has complementary values on antipodal edges. The independent-round construction is performed inside each proper face.

**Theorem (amplified global smoothing and polynomial-loss entropy bound).** For any partition into \(r\ge2\) nonempty blocks of sizes \(k_j\), put
\[
p_*=\prod_{j=1}^r(1-q_{k_j}(\rho)).
\]
Then
\[
\boxed{
\Pr(\text{no zero full antipodal geodesic anywhere})
\le
\exp\!\left[-\frac{2^n}{2\sum_j2^{k_j}}\,p_*\right].
}\tag{SR3}
\]
If \(n\rho\to\infty\), this implies, uniformly over the baseline,
\[
\boxed{
\Pr(\text{global failure})
\le
\exp\!\left[-2^{\,n-O(\rho^{-1}\log(n\rho)+\log n)}\right]
=
\exp[-2^{\,n-o(n)}].
}\tag{SR4}
\]
For uniform legal odd colorings, taking \(\rho=1/2\) improves (GB3) to
\[
\boxed{
\Pr(\text{NORI1 failure})
\le \exp[-2^{\,n-O(\log n)}]
=\exp[-2^n/n^{O(1)}].
}\tag{SR5}
\]

*Proof.* In the translated block-network proof of (GB1), replace each face-success lower bound by \(1-q_{k_j}(\rho)\) from (SR1). The faces of one network use disjoint direction sets and hence disjoint noise orbits. The same packing supplies at least \(2^n/(2\sum_j2^{k_j})\) mutually independent networks, proving (SR3).

Write \(a=n\rho\to\infty\) and choose
\[
k=\left\lceil\frac{2B\log a}{\rho}\right\rceil,\qquad r=\lfloor n/k\rfloor.
\]
For sufficiently large \(a\), one has \(k=o(n)\) and \(r\ge2\). Partition into \(r\) blocks with sizes differing by at most one. Their minimum size is at least \(k\), and maximum size \(K\le2k\). Hence
\[
q_{k_j}(\rho)\le e\,a^{-2},\qquad
\sum_jq_{k_j}(\rho)\le \frac{e}{2B\,a\log a}=o(1).
\]
The product bound \(p_*\ge1-\sum_jq_{k_j}(\rho)\) gives \(p_*\ge1/2\) eventually. Also \(\sum_j2^{k_j}\le r2^K\), so the exponent in (SR3) is at least \(2^{n-K-2}/r\). This proves (SR4), and its specialization gives (SR5). \(\square\)

**Simultaneous global profile universality.** Under the assumptions of (SR4), with probability at least
\[
1-2^{n+1}\exp\!\left[-2^{\,n-O(\rho^{-1}\log(n\rho)+\log n)}\right],
\]
every direction-indexed binary profile occurs on some full geodesic, and every positional binary word occurs on some full geodesic. Roots and orders may vary with the prescription. Indeed (SR3) applies to each prescribed profile or word by using its induced edge demands on every translated face network; a union bound covers the two lists, each of size \(2^n\).

**Closure status.** At \(\rho=1/2\), the disjoint-network failure-list encoder now saves \(2^{n-O(\log n)}\) edge-orbit bits in logarithmic code-space size. This is a polynomial-loss improvement on the earlier \(2^{n-O(n^{1/3})}\) saving. The entropy-amplification closure criterion requires a saving \(\varepsilon n2^{n-2}\) for some fixed \(\varepsilon>0\). That remaining step asks for additional compatibility among overlapping failed networks. Independent sparse rounds settle the sharp exponential order of fixed-root noise smoothing; they do not establish deterministic NORI1.


#### A limitation of marginal entropy bounds on orbit-simple supports

Call a cube-edge subgraph \(K\) *orbit-simple* if it contains at most one edge from each full-cube antipodal edge pair. It need not be connected, induced, or a series of faces. Let \(S(K)\) be its set of edge orbits and \(s=|S(K)|\). For uniform legal odd colorings, let \(F_K\) be the set of assignments on these \(s\) independent bits for which \(K\) contains no zero full antipodal geodesic, allowing every root and direction order in \(K\). Define its local entropy deficit by
\[
D_K=s-\log_2|F_K|.
\]

**Theorem (direction-blocking bound).** For every orbit-simple \(K\),
\[
\boxed{D_K\le \min_i|E_i(K)|\le s/n.}\tag{SR6}
\]

*Proof.* Choose any direction \(i\). Set every direction-\(i\) edge of \(K\) to color one. These are \(|E_i(K)|\) independent conditions, because \(K\) contains no antipodal partner edges. They admit \(2^{s-|E_i(K)|}\) assignments, all belonging to \(F_K\): a zero full geodesic would need a direction-\(i\) edge. Hence \(D_K\le |E_i(K)|\). Minimize and use \(\sum_i|E_i(K)|=s\). If a direction is missing, the deficit is zero. \(\square\)

The same argument applies to any chosen smaller family of candidate full geodesics in \(K\), and to a fixed direction-indexed profile after whole-direction color complements.

**Corollary (marginal failure-list compression cannot supply a fixed entropy deficit).** Put \(L=n2^{n-2}\). Suppose one bounds global bad colorings using only local failure-list cardinalities for orbit-simple supports. Neither disjoint-support coding nor the weighted Shearer bound can certify a saving greater than \(L/n\) bits.

*Proof.* For disjoint supports, retain the outside bits and index each local assignment in its failure list. The logarithmic code-space saving is \(\sum_KD_K\le\sum_K|S(K)|/n\le L/n\).

For a weighted Shearer argument, assign nonnegative weights \(w_K\) whose supports cover each of the \(L\) edge-orbit variables with total weight at least one. The resulting upper bound on logarithmic bad-set cardinality is
\[
U=\sum_K w_K\log_2|F_K|.
\]
By (SR6),
\[
U\ge(1-1/n)\sum_Kw_K|S(K)|\ge(1-1/n)L.
\]
Thus this upper-bound expression cannot certify a larger saving. If the constraints are indexed by smaller candidate path families, their failure lists are larger and the conclusion persists. \(\square\)

Every translated series-face network used above is orbit-simple. Within one face this follows from properness; different block faces have disjoint direction sets. The corollary therefore limits this entire marginal-counting architecture even if all face probabilities and packing constants were improved. It is a limitation of these entropy estimates, rather than a lower bound on the cardinality of their joint failure set. Joint reconstruction from overlapping constraints may yield further savings.

**Implication for closure.** The fixed entropy-deficit criterion requires \(\varepsilon L\) saved bits for a dimension-independent \(\varepsilon>0\). A proof through local constraints must therefore exploit their joint compatibility more strongly than marginal failure-list counting, or use supports containing both representatives of some antipodal edge pairs. The antipodal dependence that disappears on proper faces must enter the closing argument.


#### Sparse global noise simultaneously realizes every direction profile and every positional color word

Fix any legal antipodally odd coloring \(c_0\) of the undirected edges of \(Q_n\). Flip each antipodal edge-pair variable independently with probability \(\rho=A/n\), where \(A>6e\) is fixed and \(n\) is sufficiently large that \(\rho\le1/2\). Write \(c\) for the resulting legal coloring. Let \(\mathcal W_{\rm dir}(c)\) be the set of full-geodesic edge-color vectors indexed by coordinate direction, and \(\mathcal W_{\rm pos}(c)\) the set of consecutive edge-color words, both ranging over all roots and full direction permutations.

**Theorem (sparse-noise simultaneous profile universality).** For each fixed \(A>6e\) there is \(b_A>0\) such that, uniformly in the baseline \(c_0\),
\[
\boxed{
\Pr\!\left(
\mathcal W_{\rm dir}(c)\ne\mathbb F_2^n
\text{ or }
\mathcal W_{\rm pos}(c)\ne\mathbb F_2^n
\right)
\le 2^{n+1}\exp\!\bigl(-b_A 2^{\lfloor n/2\rfloor}\bigr).
}
\tag{SPU1}
\]
One can take
\[
b_A=\tfrac14\left(\frac{1-6e/A}{2}\right)^2
\]
for all sufficiently large \(n\). Thus at an edge-orbit flip probability of order \(1/n\), the perturbation simultaneously realizes *every* prescribed direction-indexed color profile and *every* prescribed chronological color word, with probability tending to one uniformly in \(c_0\).

*Proof.* Split the \(n\) dimensions into two nonempty blocks \(I_1,I_2\) of sizes \(k_1=\lfloor n/2\rfloor\) and \(k_2=\lceil n/2\rceil\). Put
\[
C_\rho=3e(\rho^{-1}-1)=3e(n/A-1),\qquad
\beta_A=\frac{1-6e/A}{2}>0.
\]
The previously proved face-smoothing theorem applies on any proper \(k_j\)-face, for a prescribed direction-indexed profile on its free directions or a prescribed chronological word of length \(k_j\). It gives failure probability at most \(C_\rho/k_j\), which is at most \(1-\beta_A\) for all sufficiently large \(n\). In either case, therefore, every block face succeeds with probability at least \(\beta_A\), uniformly in the baseline coloring, face location and prescribed profile or word. The argument is legitimate under antipodal orbit noise because a proper face contains at most one edge from each full-cube antipodal edge orbit, and the desired color for each direction-indexed (respectively rank-indexed) face edge is predetermined independently of the noise.

Choose any root and traverse the two direction blocks consecutively, allowing arbitrary order *within* each block. For a prescribed direction-indexed word \(w\), require the first block's geodesic to realize \(w|_{I_1}\) and the second to realize \(w|_{I_2}\). For a prescribed positional word \(w\), require respectively its first \(k_1\) and last \(k_2\) entries. In either case successful face geodesics concatenate to a full geodesic realizing \(w\). The two face events are independent because their edge-orbit variables belong to disjoint direction blocks, so each two-block network succeeds with probability at least \(\beta_A^2\).

Now translate this fixed two-face network by each of the \(2^n\) cube translations. Two translated networks can share an antipodal edge-pair orbit only if the corresponding faces belong to the *same* direction block \(I_j\); their translation difference must be zero or all-one outside \(I_j\). For each \(j\) there are at most \(2^{k_j+1}\) such translation differences. Greedy packing therefore gives at least
\[
M\ge\frac{2^n}{2(2^{k_1}+2^{k_2})}
\ge 2^{\lfloor n/2\rfloor-2}
\]
translated networks using pairwise disjoint collections of noise variables. Their success events are independent. Consequently, for any fixed prescribed word \(w\), of either type,
\[
\Pr(w\text{ is not realized})
\le (1-\beta_A^2)^M
\le \exp\!\left[-\frac{\beta_A^2}{4}2^{\lfloor n/2\rfloor}\right].
\]
A union bound over the \(2^n\) direction-indexed words and \(2^n\) chronological words yields (SPU1), with \(b_A=\beta_A^2/4\). \(\square\)

**Corollary (vanishing-relative-distance full-profile completion).** For every legal \(c_0\) on \(Q_n\), there exists a legal coloring \(c_1\) that realizes every direction-indexed and every positional color word on a full antipodal geodesic and differs from \(c_0\) on at most
\[
\boxed{
(6e+o(1))\,2^{n-2}
}
\tag{SPU2}
\]
antipodal edge-pair variables, uniformly in \(c_0\) as \(n\to\infty\). Since there are \(n2^{n-2}\) such variables, this is at most a \((6e+o(1))/n\) fraction of the legal-coloring variables.

*Proof.* Take \(A_n=6e+1/\log n\) and \(\rho_n=A_n/n\). The above proof remains valid with \(\beta_n=\Theta(1/\log n)\): its failure estimate is at most
\[
2^{n+1}\exp\!\left[-\Omega\!\left(2^{\lfloor n/2\rfloor}/(\log n)^2\right)\right]=o(1).
\]
The total number \(X\) of flipped antipodal edge-pair variables is binomial with parameters \(n2^{n-2}\) and \(A_n/n\), hence mean \(\mu_n=A_n2^{n-2}\). A standard binomial Chernoff bound with relative error \(1/\log n\) shows
\[
\Pr\{X>(1+1/\log n)\mu_n\}=o(1),
\]
since \(\mu_n/(\log n)^2\to\infty\). Both full-profile universality and this flip-count bound therefore occur simultaneously with positive probability, giving (SPU2). \(\square\)

**Scope and limitation.** The result is valid for arbitrary nonlinear direction functions and any initial legal coloring. It is a deterministic metric-density consequence of the existing random-face and translated-block theorems, strengthened to simultaneous *full* profile surjectivity. The \(o(1)\) relative perturbation does **not** prove unrestricted NORI1: a bad coloring, if one exists, could lie immediately adjacent to successful colorings in edge-pair Hamming distance. The theorem instead establishes that the full-profile-surjective legal colorings form a vanishing-relative-radius covering family in the ambient legal-coloring Boolean cube.


#### Hereditary profile universality on every moderately large face

The preceding sparse-noise theorem can be made simultaneous over exponentially many faces. For a face \(F\subseteq Q_n\), let \(m=\dim F\). Regard the restriction of a full-cube legal coloring to \(F\) as an ordinary binary coloring of the \(m\)-cube; it need not be antipodally odd relative to the face's own antipodal map. Let \(\mathcal W_{\rm dir}(F)\subseteq\mathbb F_2^{\operatorname{free}(F)}\) be its full face-geodesic profiles indexed by free directions, and \(\mathcal W_{\rm pos}(F)\subseteq\mathbb F_2^m\) its consecutive face-geodesic color words, with arbitrary starting face corner and free direction order.

**Theorem (simultaneous universality on all large faces).** Fix \(A>6e\). Let \(m_0=m_0(n)\) be integers with \(m_0\to\infty\), \(m_0\le n\), and set \(\rho=A/m_0\le1/2\) for large \(n\). From any legal antipodally odd coloring \(c_0\) of \(Q_n\), independently flip each full-cube antipodal edge-pair color variable with probability \(\rho\), producing \(c\). There exists \(b_A>0\) such that
\[
\boxed{
\Pr\!\left(
\exists\,F\subseteq Q_n,\ \dim F\ge m_0:
\ \mathcal W_{\rm dir}(F)\ne\mathbb F_2^{\operatorname{free}(F)}
\text{ or }\mathcal W_{\rm pos}(F)\ne\mathbb F_2^{\dim F}
\right)
\le
2\cdot6^n\exp\!\bigl(-b_A\,2^{\lfloor m_0/2\rfloor}\bigr).
}
\tag{HPS1}
\]
The estimate is uniform in \(c_0\).

*Proof.* Fix a face \(F\) of dimension \(m\ge m_0\) and one prescribed free-direction-indexed profile or chronological word of length \(m\). Divide the \(m\) free directions into two blocks of sizes \(\lfloor m/2\rfloor,\lceil m/2\rceil\). The existing arbitrary-face smoothing estimate applies to each block face. For each required color pattern, the event that any particular edge matches its assigned color has probability at least \(\rho\). The pertinent noise variables on a proper subface are independent because no two edges of a proper full-cube face can be antipodal. The block success probability is at least \(1-3e(\rho^{-1}-1)/\lfloor m/2\rfloor\), which for all sufficiently large \(m_0\) is bounded below by a fixed \(\beta_A>0\), since \(\rho m\ge A>6e\). (For example take \(\beta_A=(1-6e/A)/2\).) Different direction blocks use disjoint edge-orbit variables and their geodesics concatenate into the prescribed full face profile or word.

Translate the two-block network by all \(2^m\) translations within \(F\). Two translated networks can share an antipodal edge orbit only through the same direction block \(I_j\), and then their translation difference must be all-zero or all-one outside \(I_j\). There are at most \(2^{|I_j|+1}\) such differences. Greedy packing therefore supplies at least \(2^{\lfloor m/2\rfloor-2}\) networks using pairwise disjoint full-cube edge-orbit variables. Their successes are independent, each with probability at least \(\beta_A^2\). Thus the prescribed profile or word is absent from \(F\) with probability at most
\[
\exp\!\left(-\frac{\beta_A^2}{4}2^{\lfloor m/2\rfloor}\right)
\le \exp\!\left(-b_A2^{\lfloor m_0/2\rfloor}\right),
\]
where \(b_A=\beta_A^2/4\). Union-bound over at most \(2^{m+1}\le2^{n+1}\) prescribed profile and positional words for each face. The number of all nonempty cube faces is \(\sum_{m=0}^n\binom nm2^{n-m}=3^n\). The resulting estimate is (HPS1). \(\square\)

**Corollary (logarithmic face-size saturation under vanishing-density perturbation).** Fix \(\epsilon>0\) and \(A>6e\), put
\[
m_0=\left\lceil(2+\epsilon)\log_2 n\right\rceil,\qquad \rho=A/m_0.
\]
Then with probability \(1-o(1)\), **every face of dimension at least \(m_0\)** realizes every free-direction color profile and every positional color word on some full face-geodesic, uniformly in the baseline coloring. Only an \(O(1/\log n)\) fraction of the full-cube edge-pair variables are changed in expectation, and with high probability their fraction is \((A+o(1))/m_0\).

*Proof.* With this \(m_0\), \(2^{\lfloor m_0/2\rfloor}=\Omega(n^{1+\epsilon/2})\), so (HPS1) tends to zero. The number of independent edge-pair variables is \(n2^{n-2}\), and the flip count is binomial of mean \(\rho n2^{n-2}\); Chernoff concentration gives the stated fraction. \(\square\)

**Corollary (macroscopic face saturation after \(O(1/n)\) noise).** Fix \(\alpha\in(0,1]\) and \(B>6e/\alpha\). Under full-cube noise rate \(\rho=B/n\), with probability \(1-\exp[-\Omega(2^{\alpha n/2})]\), every face of dimension at least \(\alpha n\) realizes all its direction-indexed full-geodesic profiles and all its chronological color words.

*Proof.* Set \(m_0=\lceil\alpha n\rceil\) and \(A=\rho m_0\), bounded away from \(6e\) for large \(n\). Apply (HPS1), absorbing the factor \(2\cdot6^n\) into the doubly exponential failure bound. \(\square\)

These are *free-root* statements: for each face and each pattern the starting corner may depend on the face, pattern and perturbed coloring. They do not assert rooted profile surjectivity for every corner, which is obstructed at bounded \(\rho m\) by the sharp rooted noise threshold. In particular hereditary random smoothing does not establish the zero-perturbation deterministic NORI1 conjecture.


#### Robust simultaneous profile certificates after sparse noise

The preceding independent translated block networks provide a packing theorem, not merely existence. Two geodesics are *edge-orbit-disjoint* if no undirected edge of one equals an edge of the other or its full-cube antipodal translate. The witnesses below may depend on the prescribed direction profile or chronological word.

**Theorem (exponentially robust full-profile surjectivity).** Fix \(A>6e\), and set \(\rho=A/n\) in the antipodal edge-orbit noise model on \(Q_n\), starting from any legal coloring \(c_0\). There exist constants \(\gamma_A,b_A>0\), depending only on \(A\), such that with probability at least
\[
\boxed{1-2^{n+1}\exp(-b_A2^{\lfloor n/2\rfloor})}
\tag{RPC1}
\]
the perturbed legal coloring \(c\) has the following property *simultaneously* for every \(w\in\mathbb F_2^n\):

- at least \(\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) pairwise edge-orbit-disjoint full antipodal geodesics have **direction-indexed** color profile \(w\);
- at least the same number of pairwise edge-orbit-disjoint full antipodal geodesics have **chronological** color word \(w\).

Consequently the full direction-profile set and the full chronological-word set both remain all of \(\mathbb F_2^n\) after **any** further modification of fewer than \(\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) antipodal edge-pair variables.

For instance put \(\beta_A=(1-6e/A)/2>0\). For all sufficiently large \(n\) one can take
\[
\gamma_A=\beta_A^2/8,\qquad b_A=\beta_A^2/32.
\tag{RPC2}
\]

*Proof.* Use the same two direction blocks and greedily packed translated networks as in (SPU1). There are at least \(M=2^{\lfloor n/2\rfloor-2}\) networks with pairwise disjoint underlying edge-orbit-variable sets. For any fixed target \(w\), whether direction-indexed or chronological, each network succeeds with probability at least \(p=\beta_A^2\). These Bernoulli events are independent because their underlying variable sets are disjoint. Their sum stochastically dominates \(\operatorname{Bin}(M,p)\). The lower-tail Chernoff inequality gives
\[
\Pr\{\text{fewer than }pM/2\text{ successful networks}\}
\le \exp(-pM/8)
\le\exp\!\left[-(\beta_A^2/32)\,2^{\lfloor n/2\rfloor}\right].
\]
Every successful network supplies a full antipodal geodesic with the prescribed profile or word. Since the underlying network orbit supports are pairwise disjoint, these geodesics are edge-orbit-disjoint. The bound \(pM/2\ge\gamma_A2^{\lfloor n/2\rfloor}\) proves the packing claim. Apply a union bound over \(2^n\) targets of each of the two types to get (RPC1).

Now alter fewer than \(K=\lfloor\gamma_A2^{\lfloor n/2\rfloor}\rfloor\) antipodal edge-pair variables arbitrarily. For any fixed target, at most that many of its \(K\) orbit-disjoint geodesics can have an edge affected; hence at least one geodesic of each target type and each word survives. The same set of adversarial alterations is permitted for every word simultaneously. \(\square\)

**Theorem (robust hereditary face saturation).** Fix \(A>6e\) and integers \(m_0=m_0(n)\to\infty\), \(m_0\le n\), and perturb with \(\rho=A/m_0\). With probability at least
\[
\boxed{1-2\cdot6^n\exp(-b_A2^{\lfloor m_0/2\rfloor})}
\tag{RPC3}
\]
every face \(F\subseteq Q_n\) of dimension \(m\ge m_0\) simultaneously possesses, for every prescribed free-direction profile and every positional color word, at least
\[
\boxed{K_m=\left\lfloor\gamma_A2^{\lfloor m/2\rfloor}\right\rfloor}
\tag{RPC4}
\]
pairwise full-cube-edge-orbit-disjoint full geodesics *inside \(F\)* realizing the target. The property for all such faces persists after arbitrary modifications of fewer than
\[
\boxed{K_{m_0}=\left\lfloor\gamma_A2^{\lfloor m_0/2\rfloor}\right\rfloor}
\tag{RPC5}
\]
full-cube antipodal edge-pair variables.

*Proof.* For each face \(F\) of dimension \(m\ge m_0\), apply the preceding two-block packing and binomial lower-tail argument using translations only within \(F\). The proper block faces have the requisite independent edge-orbit variables, and each block-face success probability is at least \(\beta_A\) because \(\rho m\ge A>6e\). This provides at least \(K_m\) orbit-disjoint witnesses for each of its \(2^{m+1}\) target conditions, except with probability at most \(2^{m+1}\exp(-b_A2^{\lfloor m/2\rfloor})\). Sum over the at most \(3^n\) faces of \(Q_n\) and use \(m\le n\) and \(m\ge m_0\), obtaining (RPC3). Any \(K_{m_0}-1\) adversarial orbit flips can destroy at most that number of the disjoint witness geodesics for any particular face and target; at least one remains for every condition. \(\square\)

**Corollary (robust logarithmic-scale universality).** For each fixed \(\epsilon>0\), take \(m_0=\lceil(2+\epsilon)\log_2n\rceil\) and perturb with \(\rho=A/m_0\), \(A>6e\). With probability \(1-o(1)\), every face of dimension at least \(m_0\) is direction-profile and positional-word universal, and this remains true after any additional \(o(n^{1+\epsilon/2})\) edge-pair flips bounded by \(K_{m_0}-1=\Theta(n^{1+\epsilon/2})\). The initial perturbation changes an \(O(1/\log n)\) fraction of all legal edge-pair variables with high probability.

*Proof.* The hereditary failure bound tends to zero because \(2^{m_0/2}=\Omega(n^{1+\epsilon/2})\gg n\). The packing lower bound is of order \(2^{m_0/2}\), and the perturbation size follows from binomial concentration. \(\square\)

This converts sparse-noise **existence** into simultaneous quantitative *adversarial robustness*, directly linking random face smoothing to the orbit-disjoint path-packing program. The deterministic conjecture at zero noise remains open; this result cannot be specialized to \(\rho=0\).


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


##### Equality rigidity and a strict antipodal density bound

**Lemma (regular geodesic rigidity).** Let \(1\le k\le n\), and let \(H\) be a \(k\)-regular spanning edge-subgraph of \(Q_n\). If \(H\) contains no geodesic of length \(k+1\), every connected component of \(H\) is a \(k\)-dimensional face of \(Q_n\).

*Proof.* Let \(S(x)\subseteq[n]\) be the \(k\) directions of the edges of \(H\) incident with \(x\). Every direction-distinct \(H\)-path of length \(r<k\) can be extended at its last vertex: of its \(k\) incident directions, at most \(r\) have already been used. Thus every such path extends to length \(k\).

Every length-\(k\) geodesic beginning at \(x\) uses precisely the directions \(S(x)\). Indeed, if its direction set omitted \(j\in S(x)\), prepending the edge \(x+e_j,x\) would give a direction-distinct \(H\)-path of length \(k+1\), contrary to hypothesis.

Let \(xy\) be an edge of \(H\), in direction \(i\). If \(k=1\), then \(S(x)=S(y)=\{i\}\). Suppose \(k\ge2\). If some \(j\in S(y)\setminus S(x)\) existed, the two-edge path \(x,y,y+e_j\) would have distinct directions \(i,j\); extend it to length \(k\). Its direction set would contain \(j\notin S(x)\), contradicting the preceding paragraph. Therefore \(S(y)\subseteq S(x)\), and cardinality \(k\) gives \(S(y)=S(x)\). Hence \(S\) is constant along every \(H\)-edge. The component containing \(x\) contains every vertex obtained by toggling arbitrary directions from \(S(x)\), since these edges remain present, and contains no other vertex, since all its edges have directions in \(S(x)\). It is the \(k\)-face through \(x\). \(\square\)

**Theorem (equality classification in the Leader–Long bound).** Let \(1\le k\le n\) and \(H\subseteq Q_n\) be a spanning edge-subgraph with
\[
|E(H)|=k2^{n-1}.
\tag{12}
\]
Then \(H\) has a geodesic of length \(k+1\), unless its connected components are \(k\)-dimensional faces. Conversely, a partition into \(k\)-faces attains (12) and has no geodesic longer than \(k\).

*Proof.* Suppose no geodesic has length \(k+1\). For any total order \(\pi\) of the directions, let \(L_\pi(x)\) be the longest geodesic ending at \(x\) whose directions are strictly increasing in \(\pi\). The increasing-geodesic inequality (11) gives
\[
\sum_x L_\pi(x)\ge2|E(H)|=k2^n.
\]
As every \(L_\pi(x)\le k\), equality holds and \(L_\pi(x)=k\) for every vertex and every order. Fix \(x\) and choose \(\pi\) placing the \(d_H(x)\) incident directions of \(H\) before all other directions. Every increasing geodesic ending at \(x\) has its final direction among these first \(d_H(x)\) directions, so its length is at most \(d_H(x)\). Thus \(d_H(x)\ge k\). The average degree of \(H\) is \(k\) by (12), hence \(d_H(x)=k\) at every vertex. Apply the preceding lemma. Conversely, paths inside a \(k\)-face use at most its \(k\) free directions, and a spanning partition into such faces has \(2^{n-k}\cdot k2^{k-1}=k2^{n-1}\) edges. \(\square\)

**Theorem (unique two-color extremizer at half dimension).** Let \(n=2m\ge2\). In every binary edge-coloring of \(Q_n\), either a color class contains a geodesic of length \(m+1\), or there is a fixed \(m\)-element set \(S\subseteq[n]\) such that precisely the edges in directions \(S\) have color zero. Conversely, this constant direction split has no monochromatic geodesic longer than \(m\).

*Proof.* Suppose neither color has a geodesic of length \(m+1\). The increasing-geodesic inequality (11) bounds the edges in each color class by \(m2^{n-1}\). Their total is \(n2^{n-1}=2m2^{n-1}\), so both bounds are attained. The equality-classification theorem above shows that each monochromatic component is an \(m\)-face. Let \(S(x)\) be the color-zero directions incident with \(x\). Across a zero-colored edge, \(S\) stays constant because the endpoints are in the same zero-colored \(m\)-face. Across a one-colored edge, its complement \([n]\setminus S\) stays constant because the endpoints are in the same one-colored \(m\)-face. Connectivity of \(Q_n\) makes \(S(x)\) independent of \(x\). This gives the fixed direction split. In that split each monochromatic component is an \(m\)-face, so each geodesic has length at most \(m\). \(\square\)

**Corollary (strict half-dimensional geodesic bound).** For every \(m\ge1\), every antipodally odd binary edge-coloring of \(Q_{2m}\) has, in **each** color, a geodesic of length at least \(m+1\).

*Proof.* A fixed direction split is invariant under antipodal inversion, while an antipodally odd coloring reverses the colors of every antipodal edge pair. The theorem therefore supplies a monochromatic geodesic of length \(m+1\). Antipodal inversion carries any such geodesic to one of the other color, completing the proof. \(\square\)

This strict bound improves the general density-only lower bound (Corollary 7) by one in every even dimension. The uniqueness theorem classifies all two-colorings attaining the density bound, independently of antipodal oddness. Obtaining a full antipodal geodesic of length \(2m\) remains open.

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

### Paired-direction involutions and monochromatic geodesic endpoint matchings

Let \(Q_{2m}\) have a binary undirected-edge coloring whose dimensions are partitioned into pairs \(\{a_j,b_j\}\), \(1\le j\le m\), such that
\[
c_{a_j}(v)+c_{b_j}(v)=1 \quad(v\in Q_{2m}).
\tag{1}
\]
Here \(c_i(v)=c_i(v\oplus e_i)\) is the color of the edge in dimension \(i\). Antipodal oddness is unnecessary for the first theorem.

**Lemma 1 (pair invariance).** Each of \(c_{a_j},c_{b_j}\) is invariant under flipping either bit \(a_j,b_j\).

*Proof.* Edge consistency makes \(c_{a_j}\) independent of bit \(a_j\), and \(c_{b_j}\) independent of bit \(b_j\). The identity \(c_{a_j}=1-c_{b_j}\) implies independence from the other bit as well. \(\square\)

For \(t\in\{0,1\}\), let \(T_j^t\) flip whichever member of pair \(j\) has incident color \(t\). Lemma 1 gives \((T_j^t)^2=\mathrm{id}\), with no fixed vertices.

**Theorem 2 (all-rank perfect matchings).** For every \(0\le k\le m\), either color \(t\), and any distinct pair indices \(j_1,\ldots,j_k\), the map
\[
F^t_{j_1,\ldots,j_k}=T^t_{j_k}\circ\cdots\circ T^t_{j_1}
\tag{2}
\]
is a permutation of the cube vertices, with every vertex sent to the endpoint of a color-\(t\) geodesic of length \(k\). The bipartite relation joining roots to endpoints of color-\(t\) \(k\)-geodesics therefore contains a perfect matching for every \(k\le m\).

*Proof.* Every factor in (2) is an involution, so the composition is a bijection. Its \(k\) edges all have color \(t\), and each is chosen from a different pair. The traversed dimensions are distinct, hence the paths are geodesics. The permutation graph is the promised perfect matching; at \(k=0\), use the identity. \(\square\)

**Corollary 3 (counterexample-preserving paired lift).** Let \(c\) be any antipodally odd edge coloring of \(Q_m\). The coloring on \(Q_{2m}\) defined by
\[
\widetilde c_i(x,y)=c_i(x),\qquad
\widetilde c_{m+i}(x,y)=1-c_i(x)\quad(1\le i\le m)
\tag{3}
\]
is antipodally odd and balanced, satisfies (1) for the pairs \(\{i,m+i\}\), and admits the matchings of Theorem 2 in every rank \(k\le m\). It has a monochromatic full antipodal geodesic if and only if the original coloring has one.

*Proof.* The color equations give balance and antipodal oddness, and Theorem 2 gives the matchings. Every monochromatic full geodesic of the lift projects, after deleting its dummy-dimension steps, to a monochromatic full geodesic of \(c\). Conversely, let a color-\(t\) full geodesic of \(c\) run from \(x\) to \(\bar x\). Dummy dimension \(m+i\) has color \(1-c_i(x)\) at the starting old vertex and color \(c_i(x)\) at the terminal old vertex. One of these two values is \(t\). Traverse first those dummy dimensions colored \(t\) at \(x\); follow the original geodesic; then traverse the remaining dummy dimensions at \(\bar x\). Since dummy steps do not alter \(x\), this is a color-\(t\) full geodesic of the lift. \(\square\)

Thus all-rank endpoint matchings are guaranteed throughout a counterexample-preserving family. The unresolved issue is compatibility of half-geodesics chosen at antipodal roots.

#### Reversible sweeps and an unrestricted closure criterion

For a coloring \(c\) of \(Q_m\), define the color-zero edge-swap involution
\[
U_i(v)=
\begin{cases}
v\oplus e_i,&c_i(v)=0,\\
v,&c_i(v)=1.
\end{cases}
\tag{4}
\]
For a dimension permutation \(\pi=(i_1,\ldots,i_m)\), set \(U_\pi=U_{i_m}\circ\cdots\circ U_{i_1}\). Each sweep crosses color-zero edges only, using any given dimension at most once.

**Proposition 4 (two-sweep sufficient condition).** If \(U_\pi^2(x)=\bar x\) for some root \(x\) and some dimension order \(\pi\), then a color-zero full antipodal geodesic exists.

*Proof.* Apply the same ordered sweep twice. Each dimension is encountered twice and traversed zero, one, or two times. The antipodal endpoint forces an odd number of traversals in every dimension, hence one traversal per dimension. Remove the stationary updates to obtain a color-zero full geodesic. \(\square\)

**Proposition 5 (paired midpoint and reverse sweep).** More generally, if \(U_\pi(x)=U_\sigma(\bar x)\) for orders \(\pi,\sigma\), then a color-zero full antipodal geodesic exists. For the lift (3), its paired-direction half-geodesic permutation \(F_\pi^0\) projects to \(U_\pi\), and equality of the projected endpoints from antipodal roots is equivalent to equality of their full lifted midpoints. Taking \(\sigma=\operatorname{rev}\pi\) recovers Proposition 4.

*Proof.* The two projected sweep paths use dimension sets \(S,T\). Since their roots are antipodal and their endpoints equal, \(T=[m]\setminus S\). Concatenating the first path with the reversal of the second is a monochromatic full geodesic. In each lifted pair, a sweep flips one member, so the dummy flip set complements the original flip set. With antipodal lifted starts, equality of the original endpoints forces equality of the dummy endpoints. Finally each \(U_i\) is an involution, giving \(U_{\operatorname{rev}\pi}=U_\pi^{-1}\). Thus \(U_\pi(x)=U_{\operatorname{rev}\pi}(\bar x)\) is equivalent to \(U_\pi^2(x)=\bar x\). \(\square\)

The assertion that every antipodally odd cube coloring has \(x,\pi\) with \(U_\pi^2(x)=\bar x\) is an open dimension-uniform strengthening sufficient to prove unrestricted NORI1.

#### Antipodal square-root identity

Let \(P(v)=\bar v\), \(E_i(v)=v\oplus e_i\), and let \(U_i\) be the red edge-swap map (4) of a legal antipodally odd coloring. Write \(V_i\) for the analogous blue edge-swap map. Then
\[
P U_i P=V_i,\qquad U_iV_i=V_iU_i=E_i,
\]
and therefore
\[
\boxed{(U_iP)^2=E_i.}
\tag{7}
\]
*Proof.* At the antipodal vertex, the edge in direction \(i\) has the complementary color. Thus conjugating the red swap by \(P\) produces the blue swap. The red and blue swaps act on disjoint edges within direction \(i\), are individually involutive, and together flip that dimension at every vertex. Substitution gives (7). \(\square\)

Consequently each \(U_iP\) has order four and decomposes the vertex set into four-cycles (for dimensions \(m\ge2\)); the group generated by \(P,U_1,\ldots,U_m\) contains every standard cube bit flip \(E_i\), and hence acts transitively on vertices. Equation (7) is an unrestricted algebraic constraint potentially useful in attacking the two-sweep assertion; the subgroup transitivity itself does not establish a geodesic witness.

**Proposition 6 (reversal pairing of two-sweep witnesses).** For every dimension \(m\ge2\), the total number of pairs \((x,\pi)\) satisfying (5) is even. More precisely, the map
\[
(x,\pi)\longmapsto(\bar x,\operatorname{rev}\pi)
\tag{8}
\]
pairs such witnesses without fixed points.

*Proof.* Write \(F=U_\pi\). The reversed sequence of involutive edge swaps gives \(U_{\operatorname{rev}\pi}=F^{-1}\). If \(F^2(x)=\bar x\), then \(F^{-2}(\bar x)=x=\overline{\bar x}\); thus the partner also satisfies (5). For \(m\ge2\), a permutation of distinct dimensions differs from its reversal, so the pairing has no fixed points. \(\square\)

In particular a direct odd-parity counting proof on the unweighted set of two-sweep witnesses is unavailable; any successful topological degree argument must carry additional structure.

#### Opposed-sweep mismatch and tensor-power closure

Let \(U_i\) be the color-zero involutions (4), and \(F_\pi=U_\pi\). Since \(F_{\mathrm{rev}\pi}=F_\pi^{-1}\), define
\[
\boxed{\Delta(c)=\min_{x,\pi} d_H(F_\pi(x),F_\pi^{-1}(\bar x)).}
\tag{9}
\]
If \(\Delta(c)=0\), the two opposed zero sweeps meet, and their used direction sets are complementary. Concatenating them gives a zero full antipodal geodesic by Proposition 5. The condition is also equivalent to \(F_\pi^2(x)=\bar x\) for some \(x,\pi\).

**Theorem 7 (Cartesian additivity).** For legal antipodally odd colorings \(c\) on \(Q_a\) and \(d\) on \(Q_b\), define the independent Cartesian coloring \(c\boxtimes d\) by using \(c\) on the first block's edges and \(d\) on the second block's edges. Then
\[
\boxed{\Delta(c\boxtimes d)=\Delta(c)+\Delta(d).}
\tag{10}
\]
*Proof.* Updates from different factors commute. Any combined order \(\pi\) induces orders \(\pi_c,\pi_d\), and
\[
F_\pi^{c\boxtimes d}(x,y)=(F_{\pi_c}^c(x),F_{\pi_d}^d(y)),
\quad
(F_\pi^{c\boxtimes d})^{-1}(\bar x,\bar y)
=((F_{\pi_c}^c)^{-1}(\bar x),(F_{\pi_d}^d)^{-1}(\bar y)).
\]
Hamming distances add on disjoint bit sets. Every pair of factor orders extends to a combined order, so the minima separate. \(\square\)

**Theorem 8 (sublinear mismatch criterion for unrestricted NORI1).** If \(f(n)=o(n)\) and \(\Delta(c)\le f(n)\) for every vertex-balanced antipodally odd coloring of \(Q_n\) in every even dimension, unrestricted NORI1 follows.

*Proof.* If a bad coloring \(b\) of \(Q_d\) existed, its paired-direction lift (3) would give a vertex-balanced bad coloring \(c\) of \(Q_{2d}\), by Corollary 3. Since \(\Delta(c)=0\) implies a monochromatic full antipodal geodesic, \(\Delta(c)\ge1\). Every independent tensor power \(c^{\boxtimes h}\) is balanced and antipodally odd. Equation (10) gives
\[
h\le h\Delta(c)=\Delta(c^{\boxtimes h})\le f(2dh)=o(h),
\]
a contradiction. \(\square\)

**Counterexample to universal two-sweep and sublinear mismatch hypotheses.** Number the bits of Q6 from 0 to 5, and let rho_i(x) delete bit i from x. Define c_i(x) as bit rho_i(x) of T_i, where the six unsigned 32-bit tables are (d7aaaa14,eb555528,4f0f0f0d,b0f0f0f2,d99d4664,d99d4664), in hexadecimal. Every table ignores its direction bit and reverses under complementation. Direct enumeration of all 64 roots and 720 orders gives no pair with U_pi^2(x)=bar x; the histogram of Hamming discrepancies 0 through 6 is (0,3120,10080,13968,12864,6048,0). Yet root 2 with order (1,5,3,2,0,4) is a color-zero antipodal geodesic. Its paired lift C on Q12 is balanced and remains without a two-sweep witness, since every lifted sweep projects onto an original six-direction sweep. The full zero path in C from integer root 2 with order (8,10,11,1,5,3,2,0,4,6,7,9) verifies that C is good. Therefore Delta(C)>=1, and Cartesian powers yield balanced good cubes of dimension 12h with Delta>=h by Theorem 7. The uniform o(n) hypothesis of Theorem 8 and the existential two-sweep conjecture are refuted. Proposition 4 and the implication of Theorem 8 remain valid. See verified note_a16c9ca04fb509fefb7004e3.

**Lemma 9 (fixed-order mean sweep displacement).** For every antipodally odd coloring and every order \(\pi\),
\[
\boxed{\sum_{x\in Q_n}d_H(x,F_\pi(x))=n2^{n-1}.}
\tag{11}
\]
*Proof.* Every \(U_i\) is a permutation, so the intermediate vertex before the direction-\(i\) update runs bijectively over all vertices as the root varies. The incident direction-\(i\) edge is zero at \(2^{n-1}\) vertices by antipodal oddness. Thus each of the \(n\) updates fires for \(2^{n-1}\) roots. A direction is visited once, so each fired update contributes one to the final Hamming displacement. Summing proves (11). \(\square\)

The mean displacement of one zero sweep is \(n/2\); it does not constrain the mismatch between opposed sweeps in (9).

#### Sparse common readers with asymptotically independent direction samples

For a legal antipodally odd edge coloring \(c\) of \(Q_d\), let \(c^{\boxtimes h}\) be the independent Cartesian product of \(h\) copies. Write \(L(c)\) for the paired lift of Corollary 3, and let
\[
C_{h,r}=L^r(c^{\boxtimes h}),\qquad N=2^rhd,\qquad h\ge1,\quad r\ge1.
\]
A Boolean direction rule has *reader support* \(T\) if it depends only on vertex bits indexed by \(T\). Fourier degree refers to its signed form \((-1)^{c_i}\) on \(\mathbb F_2^N\). A pair of directions \(i,j\) is *square-flat* if both \(c_i(x+e_j)=c_i(x)\) and \(c_j(x+e_i)=c_j(x)\) for every vertex \(x\).

**Theorem 10 (simultaneous sparse-reader and local-uniformity counterexample reduction).** Every \(C_{h,r}\) has the following properties.

1. \(C_{h,r}\) is vertex-balanced and antipodally odd. It admits a monochromatic full antipodal geodesic if and only if \(c\) admits one.
2. All \(N\) direction rules have a common reader support of size \(hd=N/2^r\). Each signed direction rule has Fourier degree at most \(d-1\).
3. Choose \(k\) distinct directions uniformly without replacement, then choose a uniform cube vertex \(X\). The total-variation distance between their \(k\) incident color bits and \(k\) independent fair bits is at most
\[
\boxed{\binom{k}{2}\frac{2^rd-1}{N-1}\le\frac{\binom{k}{2}}h.}\tag{12}
\]
4. At least a fraction \(1-(2^rd-1)/(N-1)\ge1-1/h\) of unordered direction pairs are square-flat.

*Proof.* The product coloring reads only the original factor of the direction being traversed. Its antipodal oddness follows factorwise. Projection of a monochromatic full path to each factor gives a monochromatic full geodesic there; conversely, antipodal oddness supplies either color of full path whenever one exists, and same-colored factor paths concatenate. Thus the product has a full monochromatic geodesic precisely when \(c\) does.

The paired lift is antipodally odd and balanced because each new direction rule is the complement of the corresponding old rule. Projection of a monochromatic full lifted path onto the old bits gives an old full path. Conversely, for an old monochromatic full path from \(x\) to \(\bar x\), traverse before it the new directions having its color at \(x\), then traverse the old path, and finally traverse the remaining new directions, which have the desired color at \(\bar x\). Iterating gives assertion 1.

After any number of lifts, every direction rule is an original rule from one of the \(h\) base factors, or its complement. The first \(hd\) input bits therefore form a common reader support. An original rule ignores its own direction bit, so it depends on at most \(d-1\) bits, giving the Fourier bound.

Assign each lifted direction to the unique original factor whose rule it reads. Each factor contributes \(2^rd\) direction indices. The probability that two sampled distinct directions belong to the same factor is \((2^rd-1)/(N-1)\); the union bound gives (12). Conditional on all \(k\) factors being distinct, the sampled color bits are independent, since their rules read disjoint groups of vertex bits. Each bit is fair by antipodal oddness. Coupling with independent fair bits proves the total-variation bound. If two directions belong to distinct factors, neither rule reads the other's vertex bit, proving square-flatness and assertion 4. \(\square\)

**Corollary 11 (a low-complexity, locally uniform class sufficient for unrestricted NORI1).** For sufficiently large even \(N\), consider balanced antipodally odd colorings whose direction rules share a reader support of size at most \(\sqrt{\log_2 N}\), whose signed rules have Fourier degree at most \(\sqrt{\log_2 N}\), and which satisfy
\[
d_{\rm TV}\bigl((c_{I_1}(X),\ldots,c_{I_k}(X)),\operatorname{Ber}(1/2)^{\otimes k}\bigr)
\le \binom{k}{2}(\log_2 N)^{-1/4}
\]
for every \(1\le k\le N\), where \(I_1,\ldots,I_k\) are distinct uniformly sampled directions and \(X\) is a uniform vertex. Suppose NORI1 holds for all such colorings, for all sufficiently large even \(N\). Then unrestricted NORI1 holds.

*Proof.* Suppose \(c\) were a counterexample in some fixed dimension \(d\). In Theorem 10 take \(h=\max\{1,\lfloor r^{1/3}\rfloor\}\) and let \(r\to\infty\). Then \(N=2^rhd\), so \(\log_2N=r+O(\log r)\). Its common reader support has size \(hd=O(r^{1/3})=o(\sqrt{\log_2N})\), and its signed Fourier degree is bounded by \(d-1\). The bound (12) is \(O(\binom{k}{2}r^{-1/3})\), at most the displayed threshold uniformly in \(k\) for all sufficiently large \(r\). All lifted colorings remain balanced counterexamples, contradicting the assumed class theorem. \(\square\)

This reduction leaves the unrestricted conclusion unchanged while locating hypothetical counterexamples among colorings with simultaneously bounded Fourier complexity, sublinear common reader support, and asymptotically independent fixed-size direction samples. These are properties of the *entire coloring*, not an assumption on any chosen path. The result supplies a closure-equivalent target, without asserting positivity of its monochromatic full-path count.


##### Reader-core deletion preserves every successful starting root

**Proposition 12 (one-way reader-core factorization).** Let \(S\subsetneq[n]\) be nonempty. Suppose \(c\) is a legal antipodally odd coloring of \(Q_n\), and every direction rule \(c_i\), including those with \(i\notin S\), depends only on the vertex bits in \(S\). Write \(f\) for the coloring of \(Q_S\) consisting of the \(S\)-direction rules. For either color \(t\), let \(W_t(c)\) and \(W_t(f)\) be the sets of roots admitting a color-\(t\) full antipodal geodesic. Then, under \(Q_n=Q_S\times Q_{[n]\setminus S}\),
\[
\boxed{W_t(c)=W_t(f)\times Q_{[n]\setminus S}.}\tag{13}
\]
In particular, \(c\) has a monochromatic full antipodal geodesic if and only if \(f\) has one, and the fraction of successful roots is unchanged.

*Proof.* Project a color-\(t\) full geodesic of \(c\) onto \(S\). Since each \(S\)-direction rule is independent of the remaining vertex bits, deleting the other-direction steps yields a color-\(t\) full geodesic of \(f\). Conversely, fix a color-\(t\) geodesic of \(f\) from \(x\) to \(\bar x\), and fix any initial outside bits \(y\). For each outside direction \(j\), its rule \(g_j\) satisfies \(g_j(\bar x)=1-g_j(x)\) and is independent of all outside bits. Traverse before the \(S\)-path all outside directions with \(g_j(x)=t\); traverse after the \(S\)-path all remaining outside directions, which have \(g_j(\bar x)=t\). All steps have color \(t\), and each direction occurs once. This works for every \(y\), proving (13). \(\square\)

Applied to Theorem 10, this factorization identifies the successful-root fraction of \(C_{h,r}\) with the \(h\)-th power of that of the base coloring \(c\). It also shows that the low-reader closure-equivalent class retains the full complexity of the arbitrary coloring on its reader core: the reduction is an alternative closure target, without an approximation theorem for the reduced core.


#### Reader-core profile factorization and its obstruction to sparse-reader entropy methods

Retain the reader-core setting of Proposition 12: every direction rule of a legal antipodally odd edge coloring \(c\) on \(Q_n\) reads only the vertex bits in a fixed nonempty set \(S\subseteq[n]\). Write \(E=[n]\setminus S\), and let \(f\) be the induced legal coloring on \(Q_S\). For a fixed starting root \(a\in Q_S\) write \(\mathcal W_a(f)\) for the set of direction-indexed color words of full geodesics starting at \(a\). For a full root \((a,y)\), use \(\mathcal W_{(a,y)}(c)\).

**Proposition 13 (rootwise profile fibration).** For every \(a\in Q_S\) and every outside root \(y\in Q_E\),
\[
\boxed{\mathcal W_{(a,y)}(c)=\mathcal W_a(f)\times\mathbb F_2^E.}\tag{14}
\]
Consequently,
\[
\boxed{\mathcal W(c)=\mathcal W(f)\times\mathbb F_2^E,\qquad
|\mathcal W(c)|=2^{|E|}|\mathcal W(f)|.}\tag{15}
\]

*Proof.* Delete all steps in directions \(E\) from a full geodesic of \(c\). Because every rule in directions \(S\) ignores the outside bits, the remaining steps form a full geodesic of \(f\) from \(a\) to \(\bar a\), with the same color bits in directions \(S\). This proves the inclusion from left to right.

Conversely choose any full \(f\)-geodesic from \(a\) with desired direction profile \(w\in\mathcal W_a(f)\). Fix arbitrary outside target bits \(b\in\mathbb F_2^E\). For each \(j\in E\), let \(g_j(a)\) be its edge color when the core is at \(a\). Antipodal oddness and outside-bit independence give \(g_j(\bar a)=1-g_j(a)\). Traverse before the entire core geodesic all outside directions with \(g_j(a)=b_j\), then follow the core geodesic, then traverse all remaining outside directions. The latter have color \(g_j(\bar a)=b_j\). Since outside steps never modify a core bit, every core edge retains its assigned profile \(w\); all outside colors equal \(b\). Every direction is used once, and this works from any exterior root \(y\). Hence the other inclusion holds. \(\square\)

Write \(\Delta(c)=n-\log_2|\mathcal W(c)|\) for the logarithmic profile-support deficit, and \(v(c)\) for the maximum number of direction indices whose profile projection is surjective. Proposition 13 gives
\[
\boxed{\Delta(c)=\Delta(f),\qquad v(c)=v(f)+|E|.}\tag{16}
\]
The latter follows because a set \(T=T_S\sqcup T_E\) is shattered by a Cartesian profile product precisely when \(T_S\) is shattered by its core factor.

**Corollary 14 (paired lifts preserve absolute profile-support deficit).** If \(L\) is the paired lift of Corollary 3 and \(c\) is any legal antipodally odd coloring on \(Q_d\), then
\[
\boxed{\mathcal W(L(c))=\mathcal W(c)\times\mathbb F_2^d,\quad
\Delta(L(c))=\Delta(c),\quad v(L(c))=v(c)+d.}\tag{17}
\]
For the previously defined balanced, locally uniform counterexample-preserving family \(C_{h,r}=L^r(c^{\boxtimes h})\) of dimension \(N=2^rhd\),
\[
\boxed{\Delta(C_{h,r})=h\Delta(c),\qquad
v(C_{h,r})=h\,v(c)+(2^r-1)hd.}\tag{18}
\]
*Proof.* Apply (15)--(16) to each paired lift, and the established Cartesian profile product and shattered-set laws to tensor powers. \(\square\)

**Proof-strategy caution (a logical separation).** If \(|S|=o(n)\), (15) automatically gives \(\Delta(c)\le|S|=o(n)\), irrespective of whether its reader-core coloring \(f\) has a monochromatic full geodesic. In particular, if NORI1 were false, repeated paired lifts of a fixed counterexample would be balanced counterexamples satisfying
\[
\Delta(L^r(c))/\dim(L^r(c))=\Delta(c)/(2^r d)\longrightarrow0.
\]
Thus a sublinear profile-support deficit bound restricted to the sparse-reader class is automatic and cannot establish NORI1. The previously proved **global** sublinear-deficit criterion remains equivalent to NORI1 because it covers all legal colorings, including unpadded Cartesian powers. The reader-core family remains sufficient for grand closure when the target is full-profile surjectivity or a monochromatic full path, rather than an asymptotic scalar support bound.


#### Canonical paired-sweep conjugacy and rootwise preservation

Let c be any binary undirected-edge coloring of Q_n, with direction functions c_i(x)=c_i(x+e_i), and let L(c) be the paired lift on Q_n x Q_n defined by \(\tilde c_i(x,y)=c_i(x)\) and \(\tilde c_{n+i}(x,y)=1-c_i(x)\). For a direction order pi=(i_1,...,i_n), denote the composition of the red edge-swap involutions by \(F_\pi=U_{i_n}\cdots U_{i_1}\). Let rho list the corresponding pairs (i_j,n+i_j) consecutively in pi order, allowing either orientation within every pair; write \(\tilde F_\rho\) for the lifted red swap sweep.

**Theorem (canonical paired-sweep conjugacy).** Under the bijection \(T(x,y)=(x,z=x+y)\), every such paired sweep obeys
\[
\boxed{T\tilde F_\rho T^{-1}(x,z)=(F_\pi(x),z+\mathbf1).}\tag{1}
\]
Consequently
\[
\boxed{\tilde F_\rho^2(x,y)=(F_\pi^2(x),y+x+F_\pi^2(x)),}\tag{2}
\]
and
\[
\boxed{d_H(\tilde F_\rho^2(x,y),(\bar x,\bar y))=2d_H(F_\pi^2(x),\bar x).}\tag{3}
\]

*Proof.* At each adjacent direction pair i,n+i, evaluate a=c_i at the current original vertex x. The original i-swap flips x_i precisely when a=0, while the dummy (n+i)-swap flips y_i precisely when a=1. Their evaluations coincide regardless of their internal order: dummy moves do not alter x, while c_i ignores bit x_i. Thus the pair flips precisely one of the two bits x_i,y_i and toggles z_i=x_i+y_i once. The original x-updates follow the sweep F_pi and do not read y. After all pairs, x'=F_pi(x) and z'=z+one, proving (1). Two iterations return z to its old value and send x to F_pi^2(x); rewriting y=z+x proves (2). In (2), the net flip parity of dummy bit i equals the net flip parity of original bit i, so the two antipodal mismatch indicators coincide, giving (3). QED.

For an arbitrary lifted order sigma, its projection onto the original n bits is F_(pi_sigma) where pi_sigma is the order of its original directions: dummy swaps never affect x and the original rules never read y. This also holds for two sweeps.

**Corollary (rootwise and quantitative preservation).** Define \(W_2(c)=\{x:\exists\pi,F_\pi^2(x)=\bar x\}\), \(\Delta(c)=\min_{x,\pi}d_H(F_\pi^2(x),\bar x)\), and \(Z(c)=\#\{(x,\pi):F_\pi^2(x)=\bar x\}\). Then
\[
\boxed{W_2(L(c))=W_2(c)\times Q_n,\qquad
\Delta(c)\le\Delta(L(c))\le2\Delta(c),\qquad
Z(L(c))\ge2^{2n}Z(c).}\tag{4}
\]
*Proof.* Every lifted witness projects to an original witness and every lifted mismatch includes the original mismatch, proving one inclusion and the lower bound. Conversely (2) lifts every witness at x to one at (x,y) for all y, and (3) gives the upper bound. For each original root-order witness, the 2^n dummy roots and the 2^n orientations of the adjacent pairs yield distinct lifted root-order witnesses; this gives the count. QED.

When c is antipodally odd, its lift is balanced and antipodally odd. Hence the assertion that every legal coloring has a reversible two-sweep witness is equivalent to the same assertion restricted to vertex-balanced colorings possessing complementary direction pairs. The equivalence preserves the permitted original roots and iterates through repeated paired lifts. The existential two-sweep conjecture is refuted by the six-dimensional coloring above, including after its balanced paired lift.

##### Opposed sweeps with unrelated orders

For any undirected-edge coloring c of Q_n, write \(H_c(x)=\{F_\pi(x):\pi\in S_n\}\) and \(W_{\rm pair}(c)=\{x:H_c(x)\cap H_c(\bar x)\ne\varnothing\}\). Two sweeps from antipodal roots meeting at a common endpoint yield a monochromatic full antipodal geodesic: each sweep uses any direction at most once, and equality of endpoints forces the two used direction sets to be complementary.

**Proposition (rootwise paired-midpoint preservation under balanced lifts).** For the paired lift L(c) defined above,
\[
\boxed{W_{\rm pair}(L(c))=W_{\rm pair}(c)\times Q_n.}\tag{PS7}
\]
For independent Cartesian products,
\[
\boxed{H_{c\boxtimes d}(x,y)=H_c(x)\times H_d(y),\quad
W_{\rm pair}(c\boxtimes d)=W_{\rm pair}(c)\times W_{\rm pair}(d).}\tag{PS8}
\]

*Proof.* Every lifted sweep projects to an original sweep, giving the inclusion from left to right in (PS7). Conversely, if orders pi,sigma give a common endpoint \(F_\pi(x)=F_\sigma(\bar x)\), lift them by adjacent original/dummy pairs. Formula (PS1) maps \((x,z)\) to \((F_\pi(x),\bar z)\), and maps \((\bar x,z)\) to \((F_\sigma(\bar x),\bar z)\); the antipodal lift of \((x,y)\) has the same \(z=x+y\). The lifted endpoints therefore agree, proving the other inclusion. For (PS8), updates acting on disjoint Cartesian factors commute, and every pair of factor orders has an interleaving. Hence the set of sweep endpoints is the Cartesian product of the factor endpoint sets, and antipodal intersection separates factorwise. QED.

The rootwise implication from a color-zero full geodesic to a paired-sweep midpoint can fail, even with antipodal oddness. A five-dimensional edge-table certificate and its balanced-product amplification appear in the associated research note. The existential paired-midpoint assertion remains a sufficient condition for unrestricted NORI1.

#### Directed-influence pruning: feedback-core factorization

For a legal antipodally odd edge coloring \(c\) of \(Q_n\), let \(D(c)\) be the directed influence graph: \(j\to i\), \(i\ne j\), precisely when \(c_i(x+e_j)+c_i(x)\) is nonzero for some vertex \(x\). Each direction rule is nonconstant by antipodal oddness and ignores its own bit, so all vertices have positive indegree.

Iteratively delete any vertex \(j\) of outdegree zero **within the surviving direction set**, dropping rule \(c_j\). All other surviving rules ignore bit \(j\), so they define a legal antipodally odd coloring on the smaller cube. Write \(K\) for the surviving direction set and \(c_K\) for its coloring.

**Theorem (canonical directed-feedback core and rootwise profile fibration).** The final set \(K\) is independent of the deletion order and is the set of vertices from which some directed influence cycle is reachable. It is nonempty, and every vertex in its induced influence graph has positive outdegree. For every root \(x=(a,y)\) indexed by \(K\) and its complement,
\[
\boxed{\mathcal W_{(a,y)}(c)=\mathcal W_a(c_K)\times\mathbb F_2^{[n]\setminus K},\qquad
W_t(c)=W_t(c_K)\times Q_{[n]\setminus K}\quad(t=0,1).}\tag{FC1}
\]
Consequently \(c\) is a NORI1 counterexample precisely when \(c_K\) is, and
\[
\boxed{\Delta_0(c)=\Delta_0(c_K),\qquad v(c)=v(c_K)+n-|K|.}\tag{FC2}
\]
Here \(\Delta_0\) is the logarithmic profile-support deficit and \(v\) the profile-shattering number.

*Proof.* At one deletion, every retained rule disregards the deleted bit \(j\). Delete the \(j\)-step of any full geodesic to obtain a full geodesic in the retained cube with the same retained direction colors. Conversely, take any full retained geodesic from \(a\) with prescribed retained profile \(w\), and prescribe either value \(b\) for its deleted-direction color. The deleted rule disregards bit \(j\); its color at the two antipodal endpoints of the retained geodesic is complementary by antipodal oddness. Insert the \(j\)-step before the retained geodesic if it has color \(b\) there, and after otherwise. The other colors are unchanged. This establishes the rooted profile product by a free bit, independent of the deleted starting bit. Iteration yields the first equation of (FC1); specializing to constant words yields the successful-root equation. Scalar formulas (FC2) follow from the Cartesian profile product and shattering laws.

No directed cycle can lose a vertex under sink deletion, because its successor remains. Every vertex with a directed path to a cycle therefore survives. Conversely the subgraph induced by vertices without a directed path to any cycle is acyclic and is exhausted by iterative sink deletion. This gives the intrinsic characterization and deletion-order independence. Positive initial indegrees imply the existence of a directed cycle, so \(K\) is nonempty. Termination forces positive outdegree within \(K\). \(\square\)

**Corollary (minimal-bad feedback restriction).** A hypothetical legal counterexample of least dimension has directed influence outdegree at least one at every vertex, in addition to the automatic positive indegree. Any terminal acyclic dependency fringe may be removed without changing counterexample status or the core's color-profile deficit. This extends the earlier common-reader-core factorization: the deleted direction rules may depend on one another, so long as their directed subgraph has no feedback cycle and they do not influence the surviving core. The remaining feedback-core problem retains the full unrestricted conjectural difficulty.


##### Nonlinear reader-degree gap

Let \(r_i\) count the essential input bits of direction rule \(c_i\), and let \(M(c)=\sum_i r_i\) be the number of directed influence arcs.

**Lemma.** Each \(r_i\) equals one or is at least three. Indeed, a Boolean function of at most two bits \(u,v\) satisfying \(f(1-u,1-v)=1-f(u,v)\) has one of four possible truth tables: \(u,1-u,v,1-v\). This follows by prescribing its values at 00 and 01 and using antipodal oddness at 11 and 10.

**Corollary.** Any hypothetical NORI1 counterexample in dimension \(n\) satisfies \(M(c)\ge n+2\). Otherwise every rule would have one reader, and the all-dimensional one-reader theorem in Article XIV supplies a monochromatic full geodesic.

**Balanced corollary.** Any hypothetical vertex-balanced counterexample in even dimension \(n\) satisfies
\[
\boxed{M(c)\ge n+4.}\tag{FC3}
\]

*Proof.* Set \(s_i(x)=(-1)^{c_i(x)}\). Balance imposes \(\sum_i s_i(x)=0\) pointwise. If at most one rule depended on three or more input bits, all other signed rules would be signed singleton Walsh characters. The remaining signed rule would also belong to their real linear span. A function \(s=\sum_j a_j\chi_j\) taking only values \(\{\pm1\}\) is a signed singleton character: the identity \(s^2=1\) yields \(a_ja_k=0\) for all distinct \(j,k\) by comparing the two-element Walsh coefficients, and \(\sum_j a_j^2=1\) from the constant coefficient. Thus every rule would have one reader, and the known one-reader theorem again constructs a monochromatic full geodesic. At least two rules therefore require at least three input bits, and every other rule requires at least one, giving \(M(c)\ge(n-2)+2\cdot3=n+4\). \(\square\)

These necessary bounds supplement directed feedback-core pruning. They leave unrestricted nonlinear feedback systems as the closure target.


#### Adjacent-pair sweep trace transfer

Let c be an arbitrary undirected binary edge coloring of Q_n, n>=1, and U_i its color-zero i-edge swap involution. For a direction order pi write F_pi=U_(pi_n)...U_(pi_1), and let K=sum_(pi in S_n) F_pi denote the permutation-matrix sum. Let L(c) be the paired lift on Q_(2n), with original colors c_i(x) and dummy colors 1-c_i(x). Define K_adj as the sum of permutation matrices for all 2^n n! lifted full-sweep orders in which each original direction i occurs adjacent to its dummy partner n+i. The n pairs may occur in any order, with either internal order. Let P_n be antipodal translation on Q_n, and P_tilde that on Q_(2n).

**Theorem (even-moment trace transfer).** Under the vertex bijection T(x,y)=(x,z=x xor y),
\[
\boxed{T K_{\rm adj}T^{-1}=2^n(K\otimes P_n),\qquad
T\widetilde P T^{-1}=P_n\otimes I_{2^n}.}\tag{1}
\]
Consequently, for every integer j>=1,
\[
\boxed{\operatorname{tr}(\widetilde P K_{\rm adj}^{\,j})=
\begin{cases}
0,&j\ {\rm odd},\\
2^{n(j+1)}\operatorname{tr}(P_nK^j),&j\ {\rm even}.
\end{cases}}\tag{2}
\]
In particular,
\[
\boxed{\operatorname{tr}(\widetilde P K_{\rm adj}^{\,2})
=2^{3n}\operatorname{tr}(P_nK^2).}\tag{3}
\]

*Proof.* In each adjacent original/dummy pair, the original bit i is toggled iff its incident edge is zero, while dummy bit i is toggled iff that same original edge is one. The tests agree regardless of the order within the pair because c_i ignores bit i and dummy moves do not change x. Thus each pair toggles z_i=x_i xor y_i once. When the pairs follow pi, the update on x is F_pi, and z is complemented. Each pi admits 2^n internal pair orientations, proving the first formula (1). Under total antipodal translation (x,y)->(bar x,bar y), z is unchanged, proving the second. Taking the j-th power and tracing gives 2^(nj) tr(P_n K^j) tr(P_n^j). Since tr(P_n)=0 and tr(I)=2^n, (2) and (3) follow. QED.

K is symmetric because F_pi^(-1)=F_(rev pi). Therefore tr(P_nK^2)=sum_(x,v) K(x,v)K(bar x,v)>=0, positive precisely when two color-zero sweeps from antipodal roots share an endpoint. Formula (3) transfers this global midpoint intersection test to the balanced lift. Every odd antipodal moment of K_adj vanishes. A single adjacent-pair lifted sweep always complements z, whereas full antipodal translation leaves z fixed; consequently no such single sweep connects antipodal lifted vertices.

**Finite check.** For n=3 and the legal coloring c_i(x)=x_(i+1 mod 3), exhaustive evaluation of all original rooted orders gives tr(P_nK^2)=18. Enumeration of the 48 adjacent-pair orders on Q_6 gives tr(P_tilde K_adj^2)=9216=2^9*18, confirming (3).

#### Lazy paired-sweep trace rigidity

Let c be an undirected binary edge coloring of Q_n and L(c) its paired lift to Q_(2n). Denote by K the sum of original zero-edge full-sweep permutation matrices. Let H(t) sum all lazy lifted full sweeps with adjacent original/dummy direction pairs, each update being tI+(1-t)U_i. Then tr(Ptilde H(t)^2)=2^(3n)(1-t)^(2n) tr(PK^2) for 0<=t<=1, and tr(Ptilde H(t))=0. Proof: in each paired position precisely one zero-edge swap changes its bit. Thus the product of the two lazy factors equals tI+(1-t)U_i U_(n+i). Under (x,y)->(x,x xor y), the active paired factor acts by U_i on x and flips the corresponding second-block bit. The lifted antipode complements x and fixes the second block. Across two sweeps, each pair must be active twice: zero activations leave x_i unchanged and one activation changes the second-block bit. Thus every contributing term activates all n pairs in both sweeps and has weight (1-t)^(2n). The deterministic trace transfer gives the factor 2^(3n). QED. For c_i(x)=x_((i+1) mod 3), direct enumeration gives original trace 18, lifted t=0 trace 9216 and lifted t=1/2 trace 144.

#### Few-exception profile prescription and two-nonlinear balance rigidity

A direction rule is called *unary* if its signed value is a single signed Walsh character \(\varepsilon\chi_j(x)\), where \(\chi_j(x)=(-1)^{x_j}\), \(\varepsilon\in\{\pm1\}\), and \(j\) differs from the edge direction. An antipodally odd rule that is not unary has at least three essential input bits, by the two-reader gap proved above.

**Theorem (near-spanning profile prescription with t exceptional rules).** Let \(c\) be any legal antipodally odd coloring of \(Q_n\), and let \(T\subseteq[n]\) contain all nonunary directions. Every binary assignment to the remaining \(n-|T|\) direction colors occurs on some full antipodal geodesic. Consequently,
\[
\boxed{v(c)\ge n-|T|,\qquad
|\mathcal W(c)|\ge 2^{n-|T|},\qquad
\Delta_0(c)\le |T|.}\tag{NR1}
\]
In particular, balanced colorings with precisely two nonunary direction rules shatter their other \(n-2\) directions.

*Proof.* Choose for each \(i\in T\) any legal unary odd rule, obtaining an all-unary coloring \(c'\) that agrees with \(c\) in every direction outside \(T\). To prescribe a binary vector \(b\) on \([n]\setminus T\), complement the corresponding whole-direction edge colors of \(c'\). This preserves the unary form. The all-dimensional one-reader full-geodesic theorem of Article XIV supplies a monochromatic full antipodal geodesic in the modified coloring. If its color is one, move its starting root to its antipode while retaining its direction order, thereby complementing all traversed colors. Undoing the whole-direction color complements gives a full geodesic of \(c'\) realizing the assignment \(b\) outside \(T\). Traversing this same root and order in \(c\) leaves every edge color outside \(T\) unchanged. Thus the projection of \(\mathcal W(c)\) onto \([n]\setminus T\) is all of \(\mathbb F_2^{[n]\setminus T}\). The displayed inequalities follow. \(\square\)

**Theorem (classification of the two-nonlinear balanced interface).** Let \(n\ge4\) be even and suppose a balanced legal coloring \(c\) has precisely two nonunary directions \(a,b\); all other signed rules have the form
\[
s_i(x)=(-1)^{c_i(x)}=\varepsilon_i\chi_{p(i)}(x)
\qquad(i\notin\{a,b\}).
\]
Then both \(s_a\) and \(s_b\) disregard **both** bits \(x_a,x_b\), and precisely one of the following possibilities holds:

(A) \(s_b=-s_a\), where \(s_a\) is an arbitrary antipodally odd signed function of the remaining \(n-2\) bits. The unary signed characters sum to zero, reader by reader.

(B) There are distinct reader indices \(p,q\notin\{a,b\}\), signs \(\varepsilon,\eta\in\{\pm1\}\), and an antipodally even signed Boolean function \(h\) disregarding \(a,b\), such that, with \(X=\varepsilon\chi_p\) and \(Y=\eta\chi_q\),
\[
\boxed{s_a=\frac{X+Y+(X-Y)h}{2},\qquad
s_b=\frac{X+Y-(X-Y)h}{2}.}\tag{NR2}
\]
The sum of the unary signed rules equals \(-X-Y\). On the locus \(X=Y\), both exceptional functions are forced to equal \(X\); on \(X=-Y\), they are opposite, with their assignment controlled by \(h\).

*Proof.* Balance says \(\sum_i s_i=0\). Hence
\[
L(x):=s_a(x)+s_b(x)
=-\sum_{i\ne a,b}\varepsilon_i\chi_{p(i)}(x)
=\sum_j m_j\chi_j(x),
\]
where every \(m_j\) is an integer. Since \(s_a,s_b\) each take values \(\pm1\), \(L\) takes values in \(\{-2,0,2\}\). The independent choices of the signs \(\chi_j(x)\) give \(\max_x|L(x)|=\sum_j|m_j|\le2\). Also \(\sum_jm_j\equiv n-2\equiv0\pmod2\), so the integer coefficient vector has even \(\ell_1\) norm. The possibilities are \(L=0\), \(L=\pm2\chi_p\), or \(L=\varepsilon\chi_p+\eta\chi_q\) for distinct \(p,q\). The term \(\pm2\chi_p\) forces \(s_a=s_b=\pm\chi_p\), contradicting nonunarity.

If \(L=\varepsilon\chi_p+\eta\chi_q\) and \(p=a\), fix every vertex bit other than \(x_a\). At the setting where \(X=Y\), both \(s_a,s_b\) equal \(Y\). Because \(s_a\) ignores its own bit \(a\), it equals \(Y\) also at the other setting, where \(X=-Y\); the sum identity then makes \(s_b=X\). Thus both rules are unary, a contradiction. The same argument excludes \(q=a\), and interchanging \(a,b\) excludes \(p=b\) and \(q=b\). Therefore \(L\) disregards both bits \(a,b\), also in the case \(L=0\).

Now fix all remaining vertex bits. Since \(s_a\) ignores \(a\), \(s_b\) ignores \(b\), and their sum \(L\) ignores both, varying \(x_b\) forces \(s_a\) to be independent of \(b\); varying \(x_a\) forces \(s_b\) to be independent of \(a\). This proves the joint independence. Case \(L=0\) gives (A). In case \(L=X+Y\), where \(X,Y\) are signed singleton characters outside the exceptional pair, set \(h=Xs_a\) on the set \(X=-Y\) and put \(h=1\) on \(X=Y\). This defines a signed Boolean function independent of \(a,b\). Antipodal oddness of \(X,s_a\) makes \(h\) even under complementation; the set \(X=Y\) is also preserved under complementation. The identities (NR2) follow separately on the two loci. The unary-sum conclusions are the balance equation. \(\square\)

**Sharpness of the nonlinear influence count.** The balanced lower bound \(M(c)\ge n+4\) for a potential bad coloring cannot be improved solely by excluding one-nonlinear-rule colorings. In \(Q_6\), signed functions
\[
s_0=f(x_2,x_3,x_4),\quad s_1=-f(x_2,x_3,x_4),\quad
(s_2,s_3,s_4,s_5)=(\chi_0,-\chi_0,\chi_1,-\chi_1)
\]
are balanced and legal for any odd three-reader signed Boolean \(f\), such as the three-variable majority sign. Both exceptional directions have three essential readers, giving \(M(c)=6+4=10\). The switching type (B) also occurs with three essential readers per exceptional rule, using
\[
X=\chi_2,\quad Y=\chi_3,\quad h=\chi_2\chi_4,\quad
(s_2,s_3,s_4,s_5)=(\chi_5,-\chi_5,-\chi_2,-\chi_3).
\]
In both examples the coloring has a monochromatic full path by the established small-dimensional theorem. The classification leaves the all-dimensional two-exception closure question open.

**Global-proof target.** By (NR1), arbitrary fixed-size nonlinear exceptions force a near-spanning shattered direction set. The missing lemma is the extension of one such prescribed near-monochromatic full path across the exceptional directions. In the balanced two-exception branch, (NR2) reduces this extension problem to a complementary pair or an even switching selector, while the other direction rules remain unary. This is a single global structural branch rather than a sequence of individual dimensions.


#### All-dimensional one-exception closure via functional-cycle pivots

Let \(c\) be a legal antipodally odd edge coloring. Say direction \(i\) is unary when \(c_i(x)=x_{p(i)}+\alpha_i\) with \(p(i)\ne i\).

**Theorem (unrestricted one-exception closure).** If all but at most one direction rule of \(c\) are unary, then \(c\) admits a monochromatic full antipodal geodesic in every dimension.

*Proof.* Designate the exceptional direction \(a\), and put \(R=[n]\setminus\{a\}\). Each \(i\in R\) has one reader \(p(i)\in R\cup\{a\}\). The reader multigraph with edges \(\{i,p(i)\}\), \(i\in R\), consists of a rooted tree containing \(a\) and zero or more unicyclic components, each a functional directed cycle of length at least two with attached rooted trees.

We construct an antipodal pair \(\{y,\bar y\}\subseteq Q_R\) such that either prescribed state can occur at the \(a\)-step of a full path with **all R-direction edges zero**.

In the tree containing \(a\), every assignment \(y\) to the other bits is possible. Start with the one-letter word \(a\) and choose its initial bit \(x_a\). Add vertices in parent-first order. When parent \(j=p(i)\) has been placed, its initial bit \(x_j\) is known. Insert child \(i\) immediately before or after \(j\), whichever satisfies
\[
[j\text{ before }i]=x_j+\alpha_i.
\]
If \(i\in R\), set \(x_i=y_i+[i\text{ before }a]\) after insertion. The insertion preserves all previously fixed comparisons, gives zero color on the new direction, and ensures state \(y\) at \(a\). Thus both \(y\) and \(\bar y\) are freely realizable in this rooted component.

For any unicyclic component, place all its direction steps after \(a\). Then its starting bits are its state \(y\) at \(a\). The desired zero-color conditions orient its reader edges by
\[
[p(i)\text{ before }i]=y_{p(i)}+\alpha_i.
\]
An orientation of a functional pseudoforest is acyclic unless its unique cycle is directed consistently around itself. If the directed cycle has length \(\ell\ge2\), precisely two assignments to the \(\ell\) cycle-parent bits yield these two inconsistent orientations; they are antipodal, since complementing all the parent bits reverses every cycle edge. The other \(2^\ell-2\) assignments contain at least one antipodal pair. Choose such a pair, extend with arbitrary complementary assignments on attached tree bits, and take a topological order for each of the two resulting acyclic precedence orientations. Inserting all these component orders after the \(a\)-step preserves zero colors. Distinct components have no mutual reader constraints.

Taking the Cartesian product of the selected antipodal state pairs across components yields global \(y,\bar y\) realizable at the exceptional step, both with all unary R-edges zero. Since \(c_a\) ignores its own bit and is antipodally odd, \(c_a(\bar y)=1-c_a(y)\). Choose the one of the two states at which \(c_a=0\). Every edge of the constructed full antipodal geodesic is then zero. \(\square\)

**Corollary (sharper general nonlinear-influence threshold).** Every hypothetical NORI1 counterexample has at least two nonunary direction rules. Each nonunary odd rule has at least three essential input bits by the two-reader gap, while every unary rule has one. Therefore the directed influence-arc count of any hypothetical counterexample satisfies
\[
\boxed{M(c)\ge n+4.}\tag{OF1}
\]
This sharpens the earlier \(n+2\) unrestricted necessary bound. The one-exception global branch is eliminated without balance or other extra assumptions.


##### Absorbing an acyclic unary fringe around a monochromatic core

**Lemma (functional rooted-forest block absorption).** Partition the directions into nonempty core \(T\) and fringe \(R\). Assume each \(i\in R\) has unary rule \(c_i(x)=x_{p(i)}+\alpha_i\), and every parent chain beginning in \(R\) eventually reaches a direction of \(T\). Let \(y\in Q_R\). If the \(T\)-subcube obtained by freezing the R-bits at \(y\) has a color-\(t\) full direction-simple geodesic, then \(c\) has a color-\(t\) full antipodal geodesic on all \(n\) directions.

*Proof.* Begin with the chosen \(T\)-geodesic as one consecutive block, using its prescribed initial T-bits \(x_T\). Insert the fringe directions in parent-first order. For a fringe direction \(i\) with reader \(j\in T\), insert \(i\) before or after the entire T-block according as its initial edge color \(x_j+\alpha_i\) equals \(t\) or \(1-t\); the T-block toggles bit \(j\) once. For a fringe direction \(i\) with reader \(j\in R\), the previously inserted parent has a known initial bit \(x_j\). Insert \(i\) immediately before or after \(j\), whichever makes
\[
x_j+\alpha_i+[j\text{ before }i]=t.
\]
No insertion enters the interior of the core block, and all previously established reader comparisons remain valid. Upon inserting each fringe direction \(i\), prescribe its initial bit to be
\[
x_i=y_i+[i\text{ before the core block}].
\]
All fringe edges now have color \(t\). The R-state is \(y\) throughout the core block, so its T-direction edges retain color \(t\). Every direction is used once, proving the full antipodal geodesic. \(\square\)

**Corollary (two-nonlinear balanced switching branch).** Let \(c\) be balanced and legal with precisely two nonunary directions \(a,b\). Suppose its signed exceptional functions belong to switching case (B) of (NR2):
\[
s_a+s_b=X+Y,\qquad X=\varepsilon\chi_p,\quad Y=\eta\chi_q,
\]
with distinct \(p,q\notin\{a,b\}\). If the unary reader map on \(R=[n]\setminus\{a,b\}\) has no parent cycle contained entirely in \(R\), then \(c\) has a monochromatic full antipodal geodesic.

*Proof.* The two-nonlinear balance classification proves that \(s_a,s_b\) both disregard bits \(a,b\). Choose frozen R-state \(y\) with \(X(y)=Y(y)=1\), possible since the reader indices are distinct. Their sum is then two, forcing \(s_a(y)=s_b(y)=1\), so the consecutive core steps \(a,b\) both have color zero. All fringe parent chains reach \(\{a,b\}\); apply the block-absorption lemma to this monochromatic two-step core geodesic. \(\square\)

**Scope.** The one-exception closure theorem covers arbitrary unary parent cycles. The block-absorption lemma closes larger exceptional-core classes under an acyclic fringe hypothesis, including the balanced two-nonlinear switching case. A complementary nonlinear pair with \(s_a=-s_b\) cannot form a monochromatic adjacent two-step core at any frozen R-state; closing that class requires a separated exceptional-step construction. Switching systems with cyclic unary parent components are also unresolved by this lemma. The unrestricted conjecture remains open.


##### Cyclic-unary switching closure except a two-reader 2-cycle

Retain the balanced two-nonlinear switching setting of (NR2), with exceptional directions \(a,b\), remaining unary directions \(R\), and \(s_a+s_b=X+Y\), where \(X=\varepsilon\chi_p\), \(Y=\eta\chi_q\) for distinct \(p,q\in R\). Let \(j\mapsto p(j)\) denote the reader assigned to each unary direction \(j\in R\). To distinguish the two distinguished readers, write \(u,v\) for the indices in \(X,Y\) in this result.

**Theorem (all cyclic fringes except a mutual-reader obstruction).** If \(u,v\) do not form a directed two-cycle under the unary reader map, i.e. if it is not the case that \(p(u)=v\) and \(p(v)=u\), then \(c\) admits a monochromatic full antipodal geodesic. The conclusion also holds in the mutual-reader case whenever the zero-state bits forced by \(X=Y=1\) satisfy
\[
\boxed{y_u+y_v+\alpha_u+\alpha_v=1,}\tag{UC1}
\]
where \(c_u=x_v+\alpha_u\), \(c_v=x_u+\alpha_v\).

*Proof.* Use the adjacent core block \((a,b)\). Choose R-state \(y\) satisfying \(X(y)=Y(y)=1\), which forces both exceptional edges to have color zero by \(s_a+s_b=X+Y\). Apart from the two prescribed bits \(y_u,y_v\), all R-bits remain free.

The unary reader graph on R decomposes into rooted trees ending at \(a\) or \(b\), and unicyclic components. In rooted components, apply the parent-first insertion construction of the previous block-absorption lemma; every assignment of their R-bits at the core block is realizable. Put each unicyclic component entirely after the core block. If its reader cycle has length \(\ell\ge2\), two antipodal assignments to its cycle-reader bits orient that cycle as a directed loop; every other assignment makes the precedence constraints acyclic, and all attached trees can then be placed in topological order.

Within one cycle, at most two bits are prescribed by \(X(y)=Y(y)=1\). With no fixed bits there are \(2^\ell-2\) feasible assignments. With one fixed bit, at most one of the two antipodal forbidden assignments has that bit, leaving a feasible assignment, since \(\ell\ge2\). With two fixed bits and \(\ell\ge3\), at least two extensions exist, and at most one can be forbidden, since the two forbidden assignments are complementary on the fixed bits. Thus an assignment respecting both distinguished reader bits exists in every unicyclic component, except potentially a cycle of length two consisting precisely of \(u,v\).

If \(p(u)=v\) and \(p(v)=u\), the two unary edge requirements, with the whole core block before this component, are
\[
[v\text{ before }u]=y_v+\alpha_u,\quad
[u\text{ before }v]=y_u+\alpha_v.
\]
They are consistent precisely when (UC1) holds. In that case choose the corresponding order. All other components have compatible states and orders by the preceding argument. Assemble the rooted components around the core block, then concatenate the unicyclic component orders after it. Every unary edge is zero, both exceptional edges are zero, and every direction occurs once. \(\square\)

**Remaining switching obstruction.** A balanced switching coloring with no monochromatic full geodesic must have the two distinguished singleton readers \(u,v\) form a mutual unary-reader pair, and their forced zero-state bits must satisfy \(y_u+y_v+\alpha_u+\alpha_v=0\). This is a necessary condition on a hypothetical counterexample, not a claim that any such coloring is bad. The theorem eliminates the switching branch for arbitrary unary cycles outside this narrowly specified two-reader interaction.


##### Full profile universality and a constructive one-query algorithm for one-exception colorings

**Corollary (full support).** Every antipodally odd legal coloring with at most one nonunary direction rule realizes **every** binary direction-indexed color profile on a full antipodal geodesic:
\[
\boxed{\mathcal W(c)=\mathbb F_2^n,\qquad \Delta_0(c)=0,\qquad v(c)=n.}\tag{OF3}
\]

*Proof.* Given target \(b\in\mathbb F_2^n\), complement the entire edge-color class in each direction \(i\) with \(b_i=1\). This gauge operation preserves legality and the property of having at most one nonunary direction. Apply the one-exception theorem to find a monochromatic full geodesic. If its color is one, antipodally translate the starting root while retaining the direction order, so every edge color is zero. Undo the whole-direction complements; the corresponding original-color profile is \(b\). \(\square\)

**Algorithmic strengthening.** The one-exception theorem admits a construction requiring only one evaluation of its arbitrary nonlinear exceptional rule after its antipodal oddness has been specified. In every functional cycle of the unary reader graph, choose an orientation with at least one edge in each cyclic direction; equivalently choose cycle-reader bits \(y_j\) to enforce that orientation using equation (OF1) of the preceding theorem. This assignment and its antipode both give acyclic precedence relations. Assign arbitrary bits to attached trees and their complements, and arbitrary complementary bits in the rooted component containing the exception. Query the exceptional rule at the assembled R-state \(y\). Choose \(y\) if its exceptional color is zero, and otherwise choose \(\bar y\), whose exceptional color is zero by oddness. The rooted-tree insertion procedure and topological sorting of the unicyclic components then construct the monochromatic full geodesic. Finding the functional components, cycle orientation, and precedence orders uses a number of elementary graph operations polynomial in \(n\) (linear-time graph traversal and sorting, plus word insertion). This is an oracle-polynomial constructive proof, independent of the truth-table complexity of the exceptional nonlinear rule.


##### Twin-reader rigidity and single-four-block matching normal form

Retain the balanced two-nonunary classification (A)--(B) above. Let \(D_i=\{j:c_i(x+e_j)\ne c_i(x)\text{ for some }x\}\) be the essential reader set of direction \(i\).

**Theorem (exceptional directions are reader twins).** If a vertex-balanced antipodally odd coloring has precisely two nonunary direction rules \(a,b\), then
\[
\boxed{D_a=D_b\subseteq[n]\setminus\{a,b\},\qquad |D_a|=|D_b|\ge3.}\tag{TW1}
\]
Thus its two nonlinear vertices have identical in-neighborhoods in the directed influence graph; its total arc count is
\[
\boxed{M(c)=n-2+2|D_a|.}\tag{TW2}
\]

*Proof.* In classification (A), \(s_b=-s_a\) and both signed rules disregard \(a,b\), so equality is immediate. In classification (B), write \(X=\varepsilon\chi_p\), \(Y=\eta\chi_q\), with distinct \(p,q\notin\{a,b\}\), and put \(D=\{x:X(x)=-Y(x)\}\). The classified signed functions equal \(X=Y\) on \(D^c\). On \(D\) they obey
\[
s_a=Xh,\qquad s_b=-Xh,
\]
where \(h\) is antipodally even. The selector \(h\) takes **both** signs on \(D\): if it were constantly \(+1\), then \((s_a,s_b)=(X,Y)\) everywhere, whereas constant \(-1\) gives \((Y,X)\); both would make the exceptions unary.

Both \(p\) and \(q\) are essential for each exceptional rule. To see this for \(p\), hold all bits other than \(p\) fixed, choosing a point of \(D\) with \(h=+1\) for \(s_a\), or \(h=-1\) for \(s_b\). Flipping \(p\) moves that point from \(D\) to \(D^c\), where both exceptional functions equal \(Y\); the chosen function changes sign. To see essentiality of \(q\), use a point of \(D\) with \(h=-1\) for \(s_a\), or \(h=+1\) for \(s_b\), and flip \(q\). For any other bit \(j\notin\{a,b,p,q\}\), flipping \(j\) preserves \(D\) and \(X,Y\); the two exceptional rules agree on \(D^c\), while on \(D\) they are negatives. Therefore the derivative in bit \(j\) is nonzero for one precisely when it is nonzero for the other. The classification already shows both ignore \(a,b\). This proves (TW1), and (TW2) follows because every remaining direction has one reader. \(\square\)

**Theorem (single-four-block matching normal form).** Under the same assumptions, the \(n\) direction rules can be organized into complementary pairs as follows.

(A) If \(s_a=-s_b\), pair \(a\) with \(b\). Every unary direction can be paired with another unary direction carrying its opposite signed character; this gives a fixed partition of all \(n\) directions into pointwise complementary pairs.

(B) If \(s_a+s_b=X+Y\) with \(X=\varepsilon\chi_p\), \(Y=\eta\chi_q\), then two distinct unary directions \(u,v\) carry signed rules \(s_u=-X\) and \(s_v=-Y\). The other \(n-4\) unary directions can be partitioned into fixed complementary pairs. On the four remaining directions \(a,b,u,v\), both matchings
\[
\{\{a,u\},\{b,v\}\},\qquad
\{\{a,v\},\{b,u\}\}
\]
are pointwise complementary whenever \(X=Y\). When \(X=-Y\), the first matching is complementary for \(h=+1\), and the second for \(h=-1\).

*Proof.* In case (A), balance and \(s_a+s_b=0\) force the signed unary functions to sum to zero. Distinct Walsh singleton characters are independent; hence for each reader index the number of positive and negative copies agrees, permitting the asserted fixed pairings. In case (B), the sum of the unary functions is \(-X-Y\). Thus the signed-character coefficient for \(X\) and \(Y\) is \(-1\) and all other coefficients vanish. We can remove one unary \(-X\) and one unary \(-Y\), after which all remaining signed unary characters cancel in opposite pairs. The displayed switching formula (NR2) gives the two complementary matchings by direct substitution. \(\square\)

**Global relevance.** The balanced two-exception problem therefore has only a fixed complementary pairing or one four-direction partner switch, and both exceptional rules read the same nonlinear support. This strengthening follows from balance alone; it imposes no bound on the size or complexity of their common nonlinear reader set. Closing the fixed-pair and the single-switch configurations under all dependency patterns would eliminate the entire balanced two-nonunary branch, while higher-nonlinearity systems remain part of unrestricted NORI1.


##### Parallel alternating-square normal form for balanced two-nonlinear colorings

**Theorem.** Every vertex-balanced antipodally odd coloring with at most two nonunary direction rules is obtained from an all-unary balanced legal coloring by simultaneously reversing a collection of pairwise edge-disjoint alternating square faces, all parallel to one pair of directions \(\{a,b\}\), with the chosen squares invariant under antipodal translation. When two exceptional directions exist, they are \(a,b\).

*Proof.* The existing balanced nonunary-multiplicity lemma excludes precisely one exceptional rule. With no exceptions take the empty collection. Suppose \(a,b\) are both nonunary; use the previously proved two-rule classification, writing \(s_i=(-1)^{c_i}\).

In complementary case (A), \(s_b=-s_a\) and all remaining unary signed rules sum to zero. Choose a signed one-bit character \(X=\chi_p\), where \(p\notin\{a,b\}\), and take reference rules \(s_a^*=X\), \(s_b^*=-X\), leaving every other rule unchanged. The reference is all-unary, odd, legal and balanced. At every frozen assignment \(y\) to the remaining bits, its two exceptional direction colors are complementary, so the \((a,b)\)-square is alternating. Reverse this square when \(s_a(y)\ne X(y)\), which also changes \(-X(y)\) to \(s_b(y)\). The selection is antipodally invariant because \(s_a\) and \(X\) are odd.

In switching case (B), the classification supplies distinct signed singleton characters \(X=\varepsilon\chi_p\), \(Y=\eta\chi_q\), both independent of bits \(a,b\), with \(s_a+s_b=X+Y\). Take all-unary reference rules \(s_a^*=X\), \(s_b^*=Y\) and retain the other rules. The reference is balanced because their signed sum is unchanged. On \(X=Y\) the exceptional rules already agree with the reference. On \(X=-Y\) the reference squares are alternating, and the selector \(h\) of (NR2) gives \((s_a,s_b)=(X,Y)\) when \(h=+1\), or \((-X,-Y)\) when \(h=-1\). Reverse precisely the squares in the latter set. It is antipodally invariant because \(X=-Y\) and the even function \(h\) are antipodally invariant. Distinct parallel squares are edge-disjoint. This reconstructs \(c\) in either case. \(\square\)

**Corollary (one-layer trade-preservation equivalence).** The following conditions are equivalent: (i) NORI1 holds for every balanced coloring having at most two nonunary direction rules; (ii) every coloring produced by one antipodally paired family of parallel alternating-square reversals from an all-unary balanced legal coloring satisfies NORI1. The theorem proves (ii) implies (i). Conversely, such reversals change only the two chosen direction rules, preserve balance and oddness, and leave all other rules unary; thus (i) implies (ii).

This reframes a whole dimension-uniform structural branch as one constrained trade-stability question. The unrestricted NORI1 conjecture still includes colorings with more nonlinear direction rules.


##### Codimension-one prescriptions omitting either exceptional rule

**Theorem (two-exception profile-neighbor theorem).** Let \(c\) be a legal antipodally odd coloring of \(Q_n\) with precisely two nonunary direction rules \(a,b\). Then
\[
\boxed{\operatorname{proj}_{[n]\setminus\{a\}}\mathcal W(c)
=\mathbb F_2^{n-1}
=\operatorname{proj}_{[n]\setminus\{b\}}\mathcal W(c).}\tag{NP1}
\]
Consequently \(v(c)\ge n-1\), \(|\mathcal W(c)|\ge 2^{n-1}\), and \(\Delta_0(c)\le1\). If \(z\notin\mathcal W(c)\), then
\[
\boxed{z+e_a\in\mathcal W(c),\qquad z+e_b\in\mathcal W(c).}\tag{NP2}
\]
These conclusions do not require balance and do not assert that deleting an arbitrary unary direction gives a surjective projection.

*Proof.* Replace rule \(c_a\) by any legal unary odd rule \(c'_a(x)=x_p\), where \(p\ne a\), keeping all other rules. The modified coloring has only one nonunary rule, so the proved one-exception full-profile theorem gives \(\mathcal W(c')=\mathbb F_2^n\). For any desired assignment to directions other than \(a\), take a full path of \(c'\) realizing it. The identical starting root and dimension order in \(c\) retain all those colors, since only the \(a\)-rule changed. This proves surjectivity of the projection omitting \(a\); repeat with \(b\). Either projection has \(2^{n-1}\) distinct values, proving the cardinality, shattering, and logarithmic deficit bounds. If \(z\) is absent, the fiber over its pattern outside \(a\) must contain \(z+e_a\), and likewise outside \(b\). \(\square\)

**Implication for grand closure.** A bad two-nonunary coloring must admit full geodesics of profile \(e_a\) and \(e_b\), as well as their complements \(\mathbf1+e_a,\mathbf1+e_b\). These are two independently placed single-error certificates; a global exchange or gluing argument between them would close the entire two-exception branch. A formal support set lacking \(0^n,\mathbf1\) can still satisfy (NP1)--(NP2), so profile combinatorics alone do not supply that exchange.


#### Rootwise metric preservation under antipodally odd reader extensions

**Theorem (rootwise shortest antipodal path length under reader-core extension).** Let c be an antipodally odd undirected-edge coloring of Q_n, and let g_1,...,g_k be antipodally odd Boolean functions on Q_n. Extend c to Q_(n+k) by retaining its old-direction rules c_i(x) and setting each new-direction color to g_j(x), independent of all new bits. Let d_t(c,x) be the shortest color-t antipodal path length from x to bar x, taking infinity if no such path exists. For every root (x,y),

d_t(tilde c,(x,y))=d_t(c,x)+k.

Proof: Every antipodal extension path crosses each new direction an odd positive number of times, giving at least k new moves, and projection onto old bits is a color-t antipodal walk, giving at least d_t(c,x) old moves. For the reverse bound, take a shortest old path. Each g_j has complementary values at x and bar x. Traverse before the old path all new directions with g_j(x)=t, and after it all remaining new directions, with g_j(bar x)=t. Thus all moves have color t and length is d_t(c,x)+k. This also proves equality in the disconnected case. Equality forces every new direction to be used once and the old projection to be a shortest old path; conversely every shortest old path admits a shortest extension. QED.

For the standard complementary balanced lift L(c), put k=n and g_i=1-c_i. Then d_t(L(c),(x,y))=d_t(c,x)+n. Iterating r times gives dimension 2^r*n and d_t(L^r(c),root)=d_t(c,x)+(2^r-1)*n. Hence the additive excess over dimension is invariant under arbitrarily many balanced lifts. Also d_0(c,x)=d_1(c,x) by antipodal translation followed by reversing the path.

Independent computation: breadth-first search of all sixteen original roots of the legal Q4 coloring c_0=1-x_2, c_1=majority(x_0,1-x_2,x_3), c_2=majority(1-x_0,1-x_1,x_3), c_3=x_2, and all 256 roots of its Q8 lift verifies this relation. Root x=2 has old red antipodal distance eight and lifted distance twelve for all y. This strengthens the existing reader-core rootwise geodesic-preservation theorem to a shortest-path metric identity, without settling NORI1.

#### Complementary two-nonlinear rules: antipodal implication-SCC equivalence

**Complementary-pair 2-SAT theorem.** Fix directions a,b and R=[n]\{a,b}; fix arbitrary unary edge rules c_i(x)=x_{p(i)}+alpha_i (i in R), p(i)!=i. Define directed transport graph G on Q_R: u->v iff a full direction order with a before b and some root traverses all R-direction edges in color zero, reading R-state u at a and v at b. Form graph H by including v->u and bar(u)->bar(v) for each G arc u->v.

**Theorem.** The following are equivalent: (1) for EVERY odd Boolean f on Q_R, the coloring with exceptional rules c_a=f, c_b=1-f possesses a monochromatic full antipodal geodesic; (2) an SCC of H contains an antipodal pair u,bar(u). If (2) fails, ordinary 2-SAT extracts an odd f whose coloring lacks any monochromatic full antipodal geodesic.

**Proof.** In an odd coloring every monochromatic-one full geodesic antipodally translates to a monochromatic-zero one. A full zero path can be reversed to put a before b without altering the edge-state values. Thus the extension has a zero full path iff G has an arc u->v with f(u)=0,f(v)=1. A failed extension is an odd assignment satisfying clauses f(u)=1 OR f(v)=0 for all G arcs. Treat assertion f(w)=1 as Boolean variable w and its negation as the variable at bar(w), because f(bar(w))=1-f(w). Each clause yields implications v->u and bar(u)->bar(v), precisely H. Standard 2-SAT gives satisfiability iff no variable and its negation share an SCC. Negation of satisfiability establishes the equivalence.

A stronger sufficient condition is an antipodal SCC already in G, since H contains all reversed G arcs. Independently enumerating all 192 balanced pair-parameter presentations (representing 180 distinct unary interfaces) on Q6 with exceptional directions 0,1 and four unary directions 2,3,4,5 finds an antipodal SCC already in G in every case. There are three pair matchings, four permitted readers per pair, and two signs per pair, yielding 192 presentations, with 12 duplicate presentations when both pairs share their reader. The enumeration verifies only dimension six.

This is a grand-branch reduction: for balanced complementary two-exception colorings, arbitrary nonlinear f is eliminated from the proof target and replaced by one antipodal SCC condition on the unary transport graph, independent of f. Failure would explicitly produce a balanced legal NORI1 counterexample.

#### Free color-profile factors under reader-core extension

**Theorem (rootwise profile-support factorization under antipodally odd reader extensions).** Let c be any undirected binary edge coloring of Q_n, not necessarily antipodally odd. Let g_1,...,g_k be Boolean functions of the old n vertex bits satisfying g_j(bar x)=1-g_j(x). Define a coloring tilde c on Q_(n+k) by retaining c_i(x) for old directions i<=n and assigning g_j(x) to the new direction n+j; all new-direction rules ignore every new bit. For a fixed root x, let W_c(x) be the set of n-bit direction-indexed color profiles of full antipodal geodesics rooted at x. Then for every root (x,y),

  W_(tilde c)(x,y) = W_c(x) x F_2^k.

Proof: Projecting any full geodesic from (x,y) onto the old n directions gives a full old geodesic from x to bar x, whose old color profile is unchanged by all new-bit moves. Thus the left set is contained in the right set. Conversely choose any full old geodesic from x to bar x with profile w and any prescribed k-bit new-direction profile t. For each j, if g_j(x)=t_j, traverse new direction j before the old geodesic; otherwise traverse it afterwards, when g_j(bar x)=1-g_j(x)=t_j. New-direction steps leave old bits unchanged, so every old color remains w and every new color is t. All directions occur once. This proves the reverse inclusion independently of y. QED.

Taking the union over starting roots gives W(tilde c)=W(c) x F_2^k, hence |W(tilde c)|=2^k|W(c)|, the VC shattering dimension increases by k, and the Hartley profile-support deficit (ambient dimension minus log_2 support cardinality) is unchanged. The set of forbidden old profiles is preserved and simply repeated over all 2^k new profiles. These statements apply to the standard complementary balanced lift L(c) of an antipodally odd c, with k=n and g_i=1-c_i. Iterating r balanced lifts of an original Q_n yields dimension 2^r*n and profile support W(c) x F_2^((2^r-1)*n).

Rootwise profile covering distances also factor: for any target (a,b), min_(w in W_(tilde c)(x,y)) HammingDistance(w,(a,b)) = min_(u in W_c(x)) HammingDistance(u,a). The new profile bits create no additional obstruction to prescribed-color full geodesics.

Independent finite checks: an odd cyclic color rule c_i(x)=x_((i+1) mod n) in Q2 and Q3 was extended by two odd readers; enumeration of all roots and direction orders in Q4 and Q5 confirmed the full-product support law. An additional nonodd Q2 coloring with fixed direction colors (0,1) has singleton original support and four-element extended support, also verifying the law. This is a structural identity for all reader-core extensions, not a solution of NORI1.

##### One retained nonlinear rule: general profile shattering improvement

**One retained exceptional reader theorem.** Let c be any legal antipodally odd coloring of Q_n, with k nonunary direction rules forming set E. For each j in E, the direction-profile projection onto T_j=([n] minus E) union {j} is surjective. Hence for k>=1 the maximal shattered dimension v(c)>=n-k+1, the attainable profile set has size at least 2^(n-k+1), and the logarithmic profile-support deficit is at most k-1. If k<=1, full profile surjectivity holds.

Proof. Fix j in E and replace every other nonunary rule i in E without j by any unary legal odd rule c_i'(x)=x_{p(i)} for p(i)!=i. The modified coloring c' has at most one nonunary rule and therefore realizes every full color profile by the previously proved one-exception theorem. The same root and direction order in original c preserve every color on T_j, since none of those rules changed. Thus T_j is shattered. The cardinality and deficit bounds follow. This improves the preceding n-k unary-only shattering theorem and includes the two-exception one-error profile-neighbor theorem as k=2.

#### Acyclic paired-reader closure via antipodal transport

Suppose a balanced legal coloring has precisely two nonunary directions \(a,b\), with complementary rules \(c_a(x)=f(x_R)\), \(c_b(x)=1+f(x_R)\), where \(R=[n]\setminus\{a,b\}\) and \(f\) is an arbitrary odd Boolean function. Balance pairs the unary rules on \(R\) into opposing-reader pairs \(P=\{i,i'\}\), with rules \(c_i=x_{p(P)}+\alpha_P\), \(c_{i'}=x_{p(P)}+\alpha_P+1\). Draw \(P\to Q\) if \(p(P)\in Q\), and otherwise direct it to its terminal reader \(a\) or \(b\).

Define a directed transport graph \(G\) on \(Q_R\): \(u\to v\) when some rooted full direction order, with \(a\) preceding \(b\), has zero edges in every unary direction, has R-state \(u\) at its \(a\)-step, and has R-state \(v\) at its \(b\)-step. Exceptional-edge colors are disregarded here.

**Lemma 1 (antipodal SCC suffices).** If one strongly connected component of \(G\) contains \(u,\bar u\), every odd choice of \(f\) admits a zero full geodesic. Indeed, follow a directed path inside that component from a vertex where \(f=0\) to one where \(f=1\). Some arc \(s\to t\) crosses from \(f(s)=0\) to \(f(t)=1\). Its unary edges are zero by definition; the \(a\)-edge has color \(f(s)=0\) and the \(b\)-edge color \(1+f(t)=0\).

**Lemma 2 (paired-leaf SCC extension).** Suppose an existing unary interface on \(R_0\) has transport graph \(G_0\) with an SCC \(C\) containing an antipodal pair. Add new unary directions \(r,s\), ignored by all old edge rules, with complementary rules \(c_r=x_j+\alpha\), \(c_s=x_j+\alpha+1\) reading some old \(j\in R_0\). Then the enlarged transport graph has an SCC containing \(C\times\mathbb F_2^{\{r,s\}}\), hence an antipodal pair.

*Proof.* Every old transport arc \(u\to v\) lifts to \((u,w)\to(v,w)\) for every two-bit state \(w\): insert the newly added zero-before-\(j\) edge before both \(j\) and \(a\), and the zero-after-\(j\) edge after both \(j\) and \(b\). Their zero colors follow from complementarity and the one flip of \(j\); they do not alter the old edge colors. Their initial bits can be chosen to realize any \(w\) at \(a\).

As \(C\) contains \(u,\bar u\) and is strongly connected, for the selected old direction \(j\) some arc \(u_0\to v_0\) of \(C\) has \((u_0)_j\ne(v_0)_j\); otherwise \(j\)'s bit would be constant on \(C\). Every witness of this arc crosses \(j\) between \(a,b\). Either chosen new member \(k\in\{r,s\}\) can be made the only new direction traversed in that interval: if its color is zero before \(j\), place \(k\) between \(a,j\) and its partner after \(b\); otherwise put its partner before \(a\) and \(k\) between \(j,b\). These are zero edges, yielding additional arcs \((u_0,w)\to(v_0,w+e_r)\) and \((u_0,w)\to(v_0,w+e_s)\), for all \(w\). Combine each with a no-flip lifted return path in \(C\) from \(v_0\) to \(u_0\), and paths in \(C\) from any root to \(u_0\). This independently flips either new state bit within one SCC, so all of \(C\times\mathbb F_2^2\) are strongly connected. \(\square\)

**Theorem (acyclic paired-reader full closure).** If the paired reader digraph has no directed cycle among pair vertices, i.e. every reader chain eventually enters \(\{a,b\}\), then this complementary two-nonunary coloring satisfies NORI1 in every dimension.

*Proof.* Start with all unary pairs reading \(a\) or \(b\). Their transport graph contains **every directed one-bit cube edge** \(u\to u+e_i\). For a chosen unary direction \(i\), fix the initial bit of its exceptional reader so \(i\) has zero color between \(a,b\), and put its complementary pair member outside this interval on the appropriate side of that reader. In every other pair, put the member zero before its exceptional reader before \(a\), and the other member zero after that reader after \(b\). The initial R-bits can be chosen freely to give state \(u\) at \(a\); only the selected \(i\) flips between \(a,b\). Hence this base graph is bidirectionally connected and contains antipodal vertices.

The acyclic paired reader digraph permits insertion of the remaining pairs in parent-before-child order. Every inserted pair reads an old unary direction, and all old rules ignore its new bits, so Lemma 2 preserves an antipodal SCC at each step. Apply Lemma 1. \(\square\)

The unresolved complementary branch therefore requires at least one directed cycle **among paired unary reader blocks**. This theorem eliminates every forest-of-pairs dependency pattern, of arbitrary depth, with no restriction on the nonlinear function \(f\). It strengthens the previously closed switching-forest branch without resolving unrestricted NORI1.


##### Cyclic paired-reader components close the complementary two-nonunary branch

Continue the antipodal transport construction of the preceding theorem. Every unary direction belongs to a complementary pair \(P\), and its reader \(p(P)\) belongs either to \(a,b\) or to another unary pair. The functional paired reader digraph therefore decomposes into (i) a *rooted portion*, consisting of pairs whose reader chains reach \(a,b\), and (ii) disjoint *cyclic portions*, each consisting of a directed reader cycle among pairs together with all trees feeding into that cycle. No rule in a cyclic portion reads a bit outside its portion; no rooted rule reads a bit in a cyclic portion.

**Lemma (autonomous unary component transports antipodally).** Let \(H\) be any nonempty set of unary directions whose reader rules are all internal to \(H\), and assume these rules form a legal antipodally odd coloring of \(Q_H\). Define its *free-cut transport graph* on \(Q_H\): an arc \(u\to v\) means a zero-colored full antipodal H-geodesic can be partitioned into a prefix, middle, and suffix whose states after the prefix and after the middle are respectively \(u,v\). Then this graph has a strongly connected component containing an antipodal pair, and every vertex of that component has a loop.

*Proof.* The established all-dimensional one-reader theorem supplies a zero-colored full geodesic \(z_0,z_1,\ldots,z_h=\bar z_0\). For every \(t\), cutting both times at \(z_t\) gives a loop \(z_t\to z_t\). Cutting immediately before and after any of its individual edges gives \(z_t\to z_{t+1}\). Reverse the whole zero-colored geodesic to obtain \(z_{t+1}\to z_t\). Hence all the path vertices form a bidirectionally connected subgraph with loops, containing \(z_0,\bar z_0\). \(\square\)

**Lemma (independent transport product).** Let an interface with distinguished directions \(a,b\) have a rooted transport graph \(G_0\) on \(Q_{R_0}\). Add an independent internally read unary component \(H\) whose rules ignore all directions outside \(H\), while every original unary rule ignores \(H\). If \(G_H\) is the free-cut transport graph just defined, the enlarged transport graph satisfies
\[
\boxed{G=G_0\times G_H}\tag{CT1}
\]
as a directed relational product: an arc \((u,z)\to(v,w)\) occurs if and only if \(u\to v\) belongs to \(G_0\) and \(z\to w\) belongs to \(G_H\).

*Proof.* Project an enlarged witness direction order onto the original directions and onto \(H\). The first projection preserves the two exceptional steps and all old unary colors; the second is a zero-colored full H-geodesic cut at the same exceptional steps. Conversely, select both witnesses and interleave their direction words independently within each of the three successive regions *before \(a\)*, *between \(a,b\)*, and *after \(b\)*. All rules in either portion ignore the other portion's bits, so all unary edges remain zero and the requested states are preserved. \(\square\)

If \(G_0\) has a strongly connected component \(C_0\) containing an antipodal pair, and a loop at every vertex of \(C_0\), while \(G_H\) contains the bidirectional path-with-loops \(C_H\) from the first lemma, then \(G_0\times G_H\) contains the strongly connected set \(C_0\times C_H\). The loops allow paths to change one factor while fixing the other. This set contains a pair of antipodal vertices. In dimension zero take the trivial one-vertex transport graph with its loop as \(G_0\).

**Theorem (complete balanced complementary two-nonlinear closure).** Every vertex-balanced antipodally odd coloring of \(Q_n\) with precisely two nonunary direction rules \(a,b\) satisfying
\[
\boxed{c_b(x)=1+c_a(x)}
\]
has a monochromatic full antipodal geodesic, in every dimension. No restriction on the nonlinear odd rule, its reader set, or the cyclic structure of the remaining unary rules is required.

*Proof.* By the two-nonlinear balance classification, the exceptional rules disregard \(a,b\), all other unary rules split into pointwise complementary same-reader pairs, and each such pair reads one direction outside itself. Partition these pairs by their reader-chain attractors. For pairs whose chains reach \(a\) or \(b\), the earlier acyclic paired-reader theorem constructs a transport graph with an antipodal strongly connected component **and loops at every vertex**: its base graph permits a zero unary path with no step between \(a,b\) at every R-state, and the paired-leaf construction lifts every loop to arbitrary new pair-state bits. If this rooted portion is empty, use the trivial singleton with its loop.

Each remaining reader-chain component contains a directed cycle and is closed under taking unary readers. Its rules therefore form an independent legal antipodally odd all-unary coloring on its own cube. By the first lemma, its free-cut transport graph has an antipodal strongly connected path with loops. Successively apply the independent transport product lemma to adjoin all such components. The resulting full transport graph contains an antipodal strongly connected component with loops. Apply the preceding antipodal-SCC criterion: every odd exceptional function admits a directed arc crossing from its zero side to its one side, yielding a full zero-colored geodesic. \(\square\)

**Consequence for the two-exception program.** Complementary exceptional rules, previously the main unresolved branch of the balanced two-nonlinear classification, are now entirely closed. Under that classification the remaining balanced two-nonlinear case is the *switching* type (B), and the preceding switching theorems already exclude every such case except their narrowly specified incompatible mutual-reader two-cycle. The unrestricted grand conjecture still includes arbitrary colorings with three or more nonunary rules, so the result is a complete dimension-uniform closure of one substantial global structural branch, not the unrestricted NORI1 theorem.


##### Uniform frozen-core closure, including cyclic unary fringes

**Theorem (uniformly soluble core absorbs every unary fringe).** Partition the directions into a nonempty core \(T\) and outside set \(R\). Assume every direction \(i\in R\) has a unary odd rule \(c_i=x_{p(i)}+\alpha_i\), \(p(i)\ne i\). Assume that **for every frozen outside state** \(y\in Q_R\), the coloring of the \(T\)-subcube at exterior state \(y\) admits a zero-colored full antipodal \(T\)-geodesic. Then \(c\) admits a zero-colored full antipodal geodesic on all directions, with no assumption that the unary parent graph on \(R\) is acyclic.

*Proof.* Partition \(R=A\sqcup U\) by forward iteration of the parent map: \(A\) consists of indices whose parent chains reach \(T\), while \(U\) consists of those eventually entering a cycle entirely inside \(R\). Every parent of a vertex of \(A\) lies in \(A\cup T\); every parent of a vertex of \(U\) lies in \(U\). The coloring induced by the unary rules on \(Q_U\) is therefore a legal antipodally odd all-unary coloring, independent of \(A,T\). The previously proved one-reader theorem gives a zero full geodesic of this coloring, starting at some \(y_U\). Choose any \(y_A\in Q_A\). By the hypothesis, the frozen \(T\)-subcube at \(y=(y_A,y_U)\) has a zero full geodesic. Apply the established functional rooted-forest block absorption lemma to insert all \(A\)-directions around this \(T\)-geodesic while holding the \(U\)-bits fixed at \(y_U\). All \(A\)-edges remain zero and the core's exterior state is \(y\). Now append the previously chosen zero full geodesic in the \(U\)-directions. Its rules depend only on the \(U\)-bits, so neither the preceding core nor the \(A\)-steps affect its colors. Every direction is used once, and every traversed edge is zero. \(\square\)

##### The remaining switching two-cycle has a precise frozen-gadget criterion

In the balanced two-nonunary switching case (NR2), suppose the two singled-out unary directions \(u,v\) form the mutual-reader two-cycle left by the earlier switching theorem. In the negative mutual-reader configuration, their signed rules on the four-direction core \(T=\{a,b,u,v\}\) have the form
\[
X=\varepsilon(-1)^{x_u},\quad Y=\eta(-1)^{x_v},\qquad
s_u=-Y,\quad s_v=-X,
\]
\[
s_a=\tfrac12[X+Y+(X-Y)h],\qquad
s_b=\tfrac12[X+Y-(X-Y)h],
\tag{SG1}
\]
where \(h(x_u,x_v,y)\in\{\pm1\}\) is the switching selector and \(y\) collects all other frozen vertex bits. Let \(\xi_+,\xi_-\) be the two complementary assignments of \(x_u,x_v\) satisfying \(X=-Y\).

**Lemma (four-direction frozen switching gadget).** For any fixed outside state \(y\), the four-direction core coloring (SG1) has a zero full antipodal geodesic if and only if
\[
\boxed{h(\xi_+,y)=h(\xi_-,y).}\tag{SG2}
\]

*Proof.* At \(X=Y=+1\), both exceptional directions \(a,b\) have zero color and both unary directions \(u,v\) have one color. At \(X=Y=-1\), both unary directions are zero and both exceptional directions are one. Thus no all-zero complete core path can start at an equal-sign state: after traversing any initially available direction, the other kind remains forbidden, and traversing both initially available directions does not change this. A successful path must start at a mismatch state \(X=-Y\). When \(X=1,Y=-1\), only the \(u\)-direction among \(u,v\) is zero; after it, the state is \((-1,-1)\), where \(v\) is zero; after \(v\), the state is the opposite mismatch \((-1,1)\). The reverse mismatch requires \(v\) then \(u\). In either case, the two exceptional directions must be traversed one before and one after this consecutive unary pair, because at any mismatch state their colors are opposite. The exceptional edge available first is selected by \(h(\xi_+,y)\); the other exceptional edge is zero at the opposite mismatch precisely when its selector value agrees, \(h(\xi_-,y)=h(\xi_+,y)\). This proves both necessity and sufficiency. \(\square\)

**Corollary (a complete dimension-uniform switching subbranch).** If the switching selector in (SG1) satisfies
\[
\boxed{h(\xi_+,y)=h(\xi_-,y)\quad\text{for every }y\in Q_{[n]\setminus T},}\tag{SG3}
\]
then the full balanced coloring satisfies NORI1 regardless of the unary fringe's dependency cycles. Indeed (SG2) supplies a zero core path for every frozen exterior state, and the uniform frozen-core theorem absorbs all other unary directions. In particular the conclusion holds whenever \(h\) is independent of the two mutual-reader bits \(u,v\).

If a balanced two-nonunary coloring still resists the existing complementary and switching closure theorems, its selector must violate (SG3), and the residual forcing argument must use paths whose outside states move between exceptional steps. This is a necessary structural obstruction, not a construction of a NORI1 counterexample.


#### Full closure of the balanced two-nonunary switching branch

Retain the balanced two-nonunary classification (NR2). The complementary case (A) is closed in the preceding theorem. In switching case (B), the earlier cyclic-fringe theorem closes every instance except one where the distinguished singleton-reader directions form a mutual reader two-cycle. We prove that remaining case here.

There are two mutual-reader sign configurations, displayed in (SW1) below. The positive configuration is closed by the positive mutual-reader configuration lemma below. In this section treat the negative configuration. Label the two exceptional directions \(a,b\) and the distinguished mutual-reader directions \(u,v\), so
\[
X=\varepsilon(-1)^{x_u},\quad Y=\eta(-1)^{x_v},
\qquad s_u=-Y,\quad s_v=-X,
\tag{ST1}
\]
and
\[
s_a=\tfrac12(X+Y+(X-Y)h),\qquad
s_b=\tfrac12(X+Y-(X-Y)h).
\tag{ST2}
\]
The switching selector \(h\) is independent of \(a,b\) and is even under full antipodal complementation. Removing \(a,b,u,v\) leaves a collection \(W\) of unary rules whose signed sum vanishes, so their directions can be paired into opposing same-reader pairs, each reading a direction in \(\{a,b,u,v\}\cup W\).

Choose the initial \(u,v\) bits so \(X=+1,Y=-1\). Traversing \(u\) and then \(v\) gives two zero unary edges, passing through the sign states
\[
(+1,-1)\xrightarrow{u}(-1,-1)\xrightarrow{v}(-1,+1).
\tag{ST3}
\]
Write \(\xi_+,\xi_-\) for the two endpoint assignments of these bits, and define \(g(y)=h(\xi_+,y)\), \(y\in Q_W\). Evenness of \(h\) gives
\[
\boxed{h(\xi_-,z)=g(\bar z).}\tag{ST4}
\]

**Definition (common four-pivot transport).** Let \(K\) be the directed graph on \(Q_W\) in which \(y\to z\) means that both of the following full direction-order patterns admit roots with **all unary edges zero**, initial signs \(X=+1,Y=-1\), W-state \(y\) at the first exceptional step, and W-state \(z\) at the last exceptional step:
\[
a,\ u,\ v,\ b\qquad\text{and}\qquad b,\ u,\ v,\ a.
\]
Other W-direction steps may be inserted anywhere, without changing the displayed relative order. Exceptional edges are not required to be zero while constructing \(K\).

**Lemma 1 (twisted antipodal SCC forcing).** Let a directed graph on \(Q_W\) have a strongly connected component \(C\) containing an antipodal pair and a loop at every vertex of \(C\). Then for every function \(g:Q_W\to\{\pm1\}\), some arc \(y\to z\) within \(C\) satisfies
\[
\boxed{g(y)=g(\bar z).}\tag{ST5}
\]

*Proof.* If some \(y\in C\) has \(g(y)=g(\bar y)\), use its loop. Otherwise \(g(y)=-g(\bar y)\) at every vertex of \(C\). Choose antipodal vertices \(w,\bar w\in C\). They have opposite \(g\)-values. Along a directed path in \(C\) from \(w\) to \(\bar w\), some arc \(y\to z\) changes the \(g\)-value, so \(g(y)=-g(z)=g(\bar z)\). \(\square\)

**Lemma 2 (common four-pivot transport has an antipodal SCC with loops).** For every collection of opposing unary pairs on \(W\) described above, the common transport graph \(K\) has a strongly connected component containing an antipodal pair and loops at all its vertices.

*Proof.* Compress the opposing unary pairs into nodes \(P=\{i,i'\}\), each with one reader \(p(P)\notin P\). As in the complementary transport theorem, their functional reader graph splits into a rooted portion whose chains enter one of \(a,b,u,v\), and internally read cyclic portions.

First take every pair reading one of the four pivots. The common transport graph then contains loops at every W-state and **both orientations of every one-bit edge** \(y\leftrightarrow y+e_i\). To realize a loop, place the pair member with zero color before its reader before the first pivot, and its complementary member with zero color after its reader after the last pivot. This works simultaneously for either displayed pivot order. To realize \(y\to y+e_i\), choose the \(i\)-step as the only W-step between the first and last pivots and position it on the side of its reader where its color is zero; place its partner on the other exterior side. For reader \(u\) or \(v\), the pivot lies strictly inside the interval and its initial bit is already fixed by (ST3), but either member can be positioned on its required side. For reader \(a\) or \(b\), choose that exceptional starting bit so the selected member is zero on the interior side of its pivot; exceptional starting bits are free because the four special direction rules disregard \(a,b\). Position every other pair wholly outside the interval as in the loop construction. W-starting bits can be chosen to give any desired \(y\) at the first pivot because these base unary rules read only pivot bits. Both exceptional orders admit these constructions. The resulting common graph contains the bidirected W-cube with loops.

Next add any pair \(r,s\) whose reader \(j\) belongs to a previously installed W-pair. If the old common transport graph has a looped SCC \(C\) containing an antipodal pair, all its old arcs lift to common no-flip arcs
\[
(y,w)\longrightarrow(z,w)
\tag{ST6}
\]
for arbitrary two-bit new state \(w\): put the newly added zero-before-\(j\) member before the first pivot, and its complementary zero-after-\(j\) member after the last pivot, in **both** exceptional orders. Because \(C\) contains antipodal states and is strongly connected, for every old reader bit \(j\) some common arc \(y_0\to z_0\) in \(C\) changes \(j\). Every witness of this arc in either exceptional order crosses \(j\) strictly between its first and last exceptional steps. Thus either chosen member \(r\) or \(s\) can be placed as the only new W-step inside that interval, on the side of \(j\) where it is zero, with its partner on the opposite exterior side. Both pivot orders thereby have common arcs
\[
(y_0,w)\longrightarrow(z_0,w+e_r),\qquad
(y_0,w)\longrightarrow(z_0,w+e_s).
\tag{ST7}
\]
The no-flip lifted paths inside \(C\) allow both new state bits to be toggled independently and reversed. Hence all of \(C\times\mathbb F_2^2\) belong to one looped SCC containing an antipodal pair. Induct over the rooted paired-reader forest.

For a cyclic portion \(H\), all its unary rules read bits within \(H\). By the one-reader theorem it has a zero full antipodal H-geodesic. Splitting that path at freely selected positions relative to the first and last exceptional steps gives a free-cut H-transport graph with a looped bidirected path joining antipodal H-states, as proved in the preceding cyclic-component lemma. Such paths can be interleaved independently with any old common transport witness, in each region before, between, or after the exceptional steps, irrespective of whether their four-pivot order is \(a,u,v,b\) or \(b,u,v,a\). Thus the enlarged common graph contains the relational product of the old SCC with the free-cut H-component. Loops permit one factor to advance while the other stays fixed, so the product is strongly connected and contains an antipodal pair. Adjoin all cyclic portions to finish the proof. If \(W\) is empty, the one-state graph with its loop supplies the base case. \(\square\)

**Theorem (balanced two-nonunary switching closure).** Every vertex-balanced antipodally odd coloring with precisely two nonunary direction rules in switching case (B) of (NR2) has a monochromatic full antipodal geodesic, with no restriction on dimension or nonlinear selector \(h\).

*Proof.* The prior cyclic-unary theorem handles the instances without a distinguished mutual-reader two-cycle and the compatible mutual-reader instances. The positive remaining sign configuration is closed by the positive mutual-reader configuration lemma below. In the negative configuration use (ST1)--(ST2). Lemmas 1 and 2 furnish a common transport arc \(y\to z\) such that \(g(y)=g(\bar z)=\sigma\in\{\pm1\}\). By (ST4), the selector at the two exceptional steps agrees and equals \(\sigma\). If \(\sigma=+1\), use the witness with pivot order \(a,u,v,b\): its exceptional signed colors are respectively \(s_a=+h(\xi_+,y)=1\) and \(s_b=+h(\xi_-,z)=1\). If \(\sigma=-1\), use the common arc's witness with order \(b,u,v,a\): its exceptional signed colors are \(s_b=-h(\xi_+,y)=1\) and \(s_a=-h(\xi_-,z)=1\). In both cases the mutual-reader \(u,v\) edges are zero by (ST3), and every remaining unary edge is zero by the transport witness. Hence all \(n\) edges of this full antipodal geodesic have color zero. \(\square\)

**Corollary (complete all-dimensional balanced two-nonunary closure).** Every vertex-balanced antipodally odd coloring of \(Q_n\) with at most two nonunary direction rules has a monochromatic full antipodal geodesic. The zero- and one-exception cases were closed by the functional-cycle pivot theorem, the complementary two-exception case by the cyclic transport theorem, and the switching two-exception case by the theorem above.

Consequently, any hypothetical balanced minimal counterexample to unrestricted NORI1 must have **at least three nonunary direction rules**. The established even-dimensional balanced reduction makes this a dimension-uniform structural restriction on the grand conjecture, but does not by itself settle unrestricted NORI1.


##### Sharpened nonlinear influence threshold after two-exception closure

**Corollary.** If a vertex-balanced antipodally odd coloring of \(Q_n\) is a hypothetical counterexample to NORI1, it has at least three nonunary direction rules, and its directed influence graph has at least
\[
\boxed{M(c)=\sum_i |\operatorname{Read}(c_i)|\ge n+6}\tag{NL3}
\]
arcs.

*Proof.* The one-exception theorem and the complete balanced two-exception theorem exclude zero, one, and two nonunary rules. Antipodal oddness forces every edge rule to have at least one essential reader and, by the two-reader gap, every nonunary rule has at least three. If there are \(k\ge3\) nonunary rules, then \(M(c)\ge(n-k)+3k=n+2k\ge n+6\). \(\square\)

This is a necessary condition in the balanced reduction class sufficient for unrestricted NORI1. It does not assert that an arbitrary unbalanced coloring with two nonunary rules is already closed; its standard paired lift can contain four nonunary rules, so the balanced two-exception theorem alone does not imply such a statement. The outstanding balanced proof frontier begins with three nonlinear direction rules and their joint higher-order Fourier cancellation.


#### Bounded unpaired unary defect for k nonlinear direction rules

Let \(c\) be any vertex-balanced antipodally odd coloring in even dimension \(n\). Let \(E\) be its set of \(k\) nonunary direction rules, and \(U=[n]\setminus E\). For each \(i\in U\), the signed rule is \(s_i=\varepsilon_i\chi_{p(i)}\), where \(\chi_j(x)=(-1)^{x_j}\) and \(p(i)\ne i\). Put
\[
L(x)=\sum_{i\in E}s_i(x)
=-\sum_{i\in U}\varepsilon_i\chi_{p(i)}(x)
=\sum_{j=1}^n m_j\chi_j(x),\qquad m_j\in\mathbb Z.
\tag{UD1}
\]

**Theorem (bounded unary balancing defect).** The integer signed singleton coefficients in (UD1) satisfy
\[
\boxed{r:=\sum_{j=1}^n|m_j|\le k,\qquad r\equiv k\pmod2.}\tag{UD2}
\]
Consequently all unary direction rules except for precisely \(r\) of them can be organized into pointwise complementary pairs having the same reader bit. Here \(r\) may be zero, and the unmatched \(r\) rules, together with the \(k\) nonlinear rules, form a bounded family of at most \(2k\) unpaired directions. No assumption is made that their reader supports stay within this bounded family.

*Proof.* The signed sum \(L=\sum_{i\in E}s_i\) has values between \(-k\) and \(k\), hence \(\max_x|L(x)|\le k\). Because all singleton Walsh characters \(\chi_j(x)\) can be chosen independently by selecting \(x\), the linear expansion of (UD1) obeys
\[
\max_x\left|\sum_jm_j\chi_j(x)\right|=\sum_j|m_j|.
\]
This gives the inequality. For each reader \(j\), let \(N_j^+\) and \(N_j^-\) be the number of unary rules with signed values \(+\chi_j\) and \(-\chi_j\). The balance relation makes \(m_j=N_j^- -N_j^+\). Pair \(\min(N_j^+,N_j^-)\) opposite unary rules, leaving \(|m_j|\) rules of the majority sign. Summing over \(j\) leaves \(r\). Since \(|m_j|\equiv N_j^++N_j^-\pmod2\),
\[
r\equiv\sum_j(N_j^++N_j^-)=n-k\equiv k\pmod2
\]
because \(n\) is even. \(\square\)

**Corollary (first open balanced branch: three nonlinear rules).** If \(k=3\), the number of unpaired unary rules after maximal same-reader cancellation is
\[
\boxed{r\in\{1,3\}.}\tag{UD3}
\]
Thus every balanced coloring with three nonlinear rules consists of these three exceptional rules, one or three unmatched unary rules, and arbitrarily many pointwise complementary unary pairs. If \(r=3\), the integer coefficient vector \(m\) has \(\ell_1\)-norm three; the case \(L=\pm3\chi_p\) cannot occur with three nonunary exceptional functions, because it forces all three signed exceptional functions to be the same unary character. The remaining possibilities include one coefficient of magnitude two and a distinct singleton coefficient, or three singleton coefficients with unit magnitude (possibly after consolidating repeated readers).

This is a dimension-uniform structural reduction to bounded unpaired *rules*, not to a bounded-dimensional reader core. The complementary-pair transport methods established for \(k=2\) now face a core of four or six unpaired directions, with arbitrary nonlinear dependence on the full cube. Establishing the required joint path compatibility on this bounded unpaired family would advance unrestricted NORI1 beyond the closed two-exception branch.


#### Independent mixed-state transport proof and the positive mutual-reader configuration

Retain switching type (B), with exceptional directions \(a,b\), distinguished unary reader directions \(u,v\), and signed rules
\[
s_a+s_b=X+Y,\qquad X=\varepsilon\chi_u,\quad Y=\eta\chi_v.
\]
Both exceptional rules disregard \(a,b\). The preceding cyclic-unary theorem already proves closure unless \(u,v\) read each other and their forced state \(X=Y=1\) violates (UC1).

Write \(s_u=\delta_u\chi_v,\ s_v=\delta_v\chi_u\). In that remaining case,
\(\varepsilon\eta\delta_u\delta_v=1\), so there is a common sign \(\mu\) with
\[
\boxed{s_u=\mu Y,\qquad s_v=\mu X.}\tag{SW1}
\]
This leaves two configurations.

**Lemma 1 (positive mutual-reader configuration).** If \(\mu=1\), the switching coloring has a zero full antipodal geodesic.

*Proof.* The two unary directions \(u,v\) have a zero two-step geodesic whose successive \((X,Y)\)-states are
\[
(1,-1)\longrightarrow(1,1)\longrightarrow(-1,1),
\]
using first \(v\), then \(u\). At the middle state, both exceptional signed rules equal one, independently of every other bit and of the selector. Insert \(a,b\) consecutively there. This gives a zero full geodesic on the four-direction core \(T=\{a,b,u,v\}\), for every frozen assignment of the other bits.

In the functional unary reader graph outside \(T\), separate the directions whose parent chains reach \(T\) from the autonomous unicyclic components. Choose a zero full geodesic in each autonomous component by the one-reader theorem, and freeze its bits at that path's starting state. Choose arbitrary frozen bits on the rooted portion. The four-step core path exists at this combined frozen state. Apply the rooted-forest block-absorption lemma to insert all directions whose parent chains reach \(T\), keeping the autonomous bits fixed. Finally append the chosen zero paths of the autonomous components. Their rules ignore the other portions, while no rooted unary rule reads an autonomous component. All directions occur once and all edges are zero. \(\square\)

For the remaining sign \(\mu=-1\), put
\[
Z=\{z\in Q_R:X(z)=-Y(z)\},\qquad R=[n]\setminus\{a,b\}.
\]
At every state in \(Z\), the exceptional signed rules are complementary:
\(s_b=-s_a\).
Let \(G_Z\) be the directed unary transport graph restricted to \(Z\): an arc \(z\to w\) is witnessed by a full order with \(a\) before \(b\), every unary edge zero, and R-states \(z,w\) at the exceptional steps. Internal states between those steps are unrestricted.

**Lemma 2 (restricted mixed-state transport).** If \(s_u=-Y,\ s_v=-X\), then \(G_Z\) has a strongly connected set containing an antipodal pair, with a loop at every vertex of that set.

*Proof.* The total unary signed sum is \(-X-Y\), and \(u,v\) already contribute precisely \(-X-Y\). Hence the remaining unary signed rules sum to zero. Pair them into opposite signed singleton characters, reader by reader. Each pair has a common reader outside that pair.

The pair-reader graph decomposes into pairs whose reader chains reach \(\{a,b,u,v\}\), and autonomous cyclic portions. We construct the required restricted transport set.

First take \(u,v\), together with all unary pairs reading \(a\) or \(b\) directly. On the two mixed \((X,Y)\)-states, the zero \(u,v\)-path runs
\[
(1,-1)\longrightarrow(-1,-1)\longrightarrow(-1,1).
\tag{SW2}
\]
Its reversal is also zero. Placing \(a,b\) before or after that two-step path supplies a loop at either mixed state. Placing them on opposite sides supplies a directed arc between the mixed states, in either direction. Thus their restricted free-cut transport graph is the two-vertex bidirectional graph with loops.

For the pairs reading \(a\) or \(b\), the earlier base-interface construction supplies every directed one-bit state change and a loop at every state. To change one chosen member between the exceptional steps, choose the initial bit of its reader to make that member zero in the interval, and put its partner on the required exterior side. Put the two members of every other pair before \(a\) and after \(b\), respectively, according to their zero side of the reader. Initial bits of pair members realize any requested state at \(a\). These base directions and the \(u,v\)-component ignore each other, so their transport relations combine by independently interleaving the three regions before \(a\), between \(a,b\), and after \(b\). The product contains a strongly connected set with loops and an antipodal pair, all of whose endpoints lie in \(Z\).

Insert all other pairs in the rooted portion in parent-before-child order. The paired-leaf SCC extension remains valid with the mixed-state restriction: its lifted arcs retain the old states of \(u,v\) at both exceptional steps. For completeness, every old arc lifts with both new steps outside the interval, preserving any chosen new pair-state. Since the old strongly connected set contains antipodal states, each old reader bit changes on some arc within it. On such an arc the reader step occurs between \(a,b\); either new pair member can be placed on its zero side of that reader inside the interval, with its partner outside. This lifts the arc while toggling either selected new state bit. Lifted return paths then connect all four new pair-states over the old strongly connected set. Exterior insertions lift its loops. Thus induction preserves the required restricted set.

Each autonomous cyclic portion is an independent legal all-unary coloring. Choose a zero full geodesic in it. Cutting that path before and after any of its edges, and also reversing it, supplies a bidirectional path of state transitions from a vertex to its antipode, with loops at all path vertices. The independent transport product adjoins this component to the constructed set; loops permit one factor to change while the other remains fixed. Repeat for all autonomous portions. The resulting set in \(G_Z\) is strongly connected, has loops, and contains an antipodal pair. \(\square\)

**Theorem (complete switching closure).** Every balanced legal coloring of switching type (B) with precisely two nonunary rules has a monochromatic full antipodal geodesic, in every dimension.

*Proof.* The earlier cyclic-unary theorem covers the cases where the distinguished readers are not a mutual pair, and the mutual-reader cases satisfying (UC1). Otherwise use (SW1). Lemma 1 covers \(\mu=1\).

For \(\mu=-1\), Lemma 2 supplies a strongly connected set \(C\subseteq Z\) containing \(z,\bar z\). Oddness gives \(s_a(\bar z)=-s_a(z)\). Follow a directed path in \(C\) from a state with \(s_a=1\) to one with \(s_a=-1\). It contains an arc \(r\to s\) with these respective signs. Its unary witness has all unary edges zero; its \(a\)-edge is zero because \(s_a(r)=1\), and its \(b\)-edge is zero because \(s_b(s)=-s_a(s)=1\) on \(Z\). This is a zero full antipodal geodesic. \(\square\)

**Corollary (balanced two-nonlinear theorem).** Every vertex-balanced antipodally odd coloring with at most two nonunary direction rules satisfies NORI1. The all-unary and one-exception theorems cover at most one exception; the two-rule classification leaves the complementary and switching cases; the preceding complementary closure and the present theorem cover both.

The switching selector may be an arbitrary antipodally even Boolean function on its full reader set. The proof uses its forced equal values at \(X=Y=1\), or its complementary exceptional values on \(X=-Y\), together with oddness and restricted transport. It places no bound on dimension or reader complexity.

**Finite audit.** The mixed-state transport construction for \(\mu=-1\) was checked independently by enumerating full orders and solving the unary root-bit constraints. In \(Q_6\), all eight interfaces obtained by choosing the one remaining complementary pair's reader in \(\{a,b,u,v\}\) and either sign have an antipodal SCC on all eight mixed states. In \(Q_8\), four sign choices were checked for each of three interface patterns: two pairs reading \(a,b\); a pair reading \(u\) with a child pair reading one of its members; and an autonomous two-pair reader cycle. The first two patterns have all 32 mixed states in an antipodal SCC. The autonomous-cycle pattern has 16 states in antipodal SCCs, with loops on those states. The dimension-uniform proof uses the SCC extension and product lemmas, independently of this audit.



#### Three-exception minority selectors and fiberwise two-label rigidity

The complete balanced two-nonlinear theorem above motivates a finite-interface description of the first unresolved balanced branch \(k=3\). Throughout let \(n\) be even, \(E=\{a,b,c\}\subset[n]\) be precisely the three nonunary directions, and write signed color rules \(s_i=(-1)^{c_i}\). For \(i\notin E\), write \(s_i=\varepsilon_i\chi_{p(i)}\), with \(p(i)\ne i\). Vertex balance gives the signed singleton expansion
\[
\boxed{L:=s_a+s_b+s_c=\sum_{j=1}^n m_j\chi_j,\qquad
r:=\sum_j|m_j|\in\{1,3\}.}\tag{TS1}
\]
The parity and upper bound for \(r\) were proved in (UD2).

**Theorem (minority-selector normal form).** Let \(M(x)=\operatorname{sgn}L(x)\), an odd signed Boolean function, and \(A=\{x:|L(x)|=1\}\), an antipodally invariant set. There is a unique selector \(J:A\to E\) such that
\[
\boxed{
s_i(x)=M(x)(1-2\beta_i(x)),\quad
\beta_i(x)=\mathbf1_{\{x\in A,\ J(x)=i\}},\qquad
\sum_{i\in E}\beta_i=\mathbf1_A.
}\tag{TS2}
\]
Each \(\beta_i\) is antipodally even. If \(M(x)=(-1)^{q(x)}\), the undirected-edge condition for the three exceptional rules is **equivalent** to the three Boolean equations
\[
\boxed{\beta_i(x+e_i)+\beta_i(x)=q(x+e_i)+q(x)
\pmod2,\qquad i\in E.}\tag{TS3}
\]
Conversely, any signed singleton sum \(L\) of the form (TS1), together with an even selector \(J\) supported on \(A\) satisfying (TS3), defines antipodally odd undirected exceptional rules with signed sum \(L\); together with the compatible prescribed unary rules they form a balanced legal coloring. The condition that all three exceptional rules are substantively nonunary remains a separate hypothesis.

Up to writing signs into the unary characters, the possibilities for \(L\) are
\[
\boxed{
\begin{array}{c|c|c}
r&L&M,\ A\\
1&X&X,\quad A=Q_n\\
3&2X+Y\ (X,Y\text{ distinct readers})&
X,\quad A=\{X=-Y\}\\
3&X+Y+Z\ (X,Y,Z\text{ distinct readers})&
\operatorname{majority}(X,Y,Z),\quad A=\{|X+Y+Z|=1\}.
\end{array}}\tag{TS4}
\]
The remaining possibility \(L=3X\) is excluded when all three exceptional rules are nonunary: it would force each \(s_i=X\), making at least two of them unary.

*Proof.* For three signed bits with sum \(L=\pm1\), precisely one bit differs from \(\operatorname{sgn}L\); for sum \(L=\pm3\), none does. This gives uniqueness and (TS2). Antipodal oddness of each \(s_i\) and \(M\) makes their ratio \(1-2\beta_i\) antipodally even. Writing \(s_i=(-1)^{q+\beta_i}\), its invariance under flipping its own bit is precisely (TS3). Conversely (TS2) gives signed sum \(M(3-2\mathbf1_A)=L\), oddness, and, by (TS3), undirectedness. The possible coefficient vectors in (TS4) exhaust integral odd singleton sums with \(\ell_1\) norm one or three, except \(3X\). For \(2X+Y\), the coefficient of \(X\) dominates, yielding the table; for three distinct readers, the sign is their majority. \(\square\)

The case \(r=1\) has a particularly strong local restriction. Write \(L=X=\varepsilon\chi_p\), so \(M=X\), \(A=Q_n\), and for \(i\in E\),
\[
\boxed{\beta_i(x+e_i)+\beta_i(x)=\mathbf1_{\{p=i\}}.}\tag{TS5}
\]
Freeze all vertex bits outside \(E\) at any state \(y\). The restricted selector \(J_y:Q_E\to E\) satisfies the following classification.

**Theorem (fiberwise two-label rigidity).** On every frozen three-cube \(Q_E\), the selector \(J_y\) uses at most two of its three labels.

- If \(p\notin E\), then \(J_y\) is either constant, or there exist distinct \(i,j,k\in E\) such that it uses precisely the two labels \(i,j\) and selects between them according to the single remaining bit \(x_k\), possibly complemented:
  \[
  \boxed{J_y(x_E)\in\{i,j\},\quad
  \mathbf1_{\{J_y=i\}}=x_k+\alpha(y)\pmod2.}\tag{TS6}
  \]
- If \(p\in E\), then \(J_y\) uses precisely the two labels \(p,j\), for one \(j\in E\setminus\{p\}\). Writing \(k=E\setminus\{p,j\}\), its membership rule has the form
  \[
  \boxed{\mathbf1_{\{J_y=p\}}=x_p+t_y(x_k)\pmod2,}\tag{TS7}
  \]
  where \(t_y\) is any Boolean function of the single bit \(x_k\) (hence one of four possible unary/constant functions on this fiber).

*Proof when \(p\notin E\).* Put \(S_i=\{x_E:J_y(x_E)=i\}\). By (TS5), \(S_i\) is a union of \(i\)-direction edges. For any \(i\in E\), its intersection with the half-cube \(x_i=0\) has \(|S_i|/2\) vertices. For \(j\ne i\), \(S_j\) is a union of \(j\)-edges that stay inside this half-cube, so \(|S_j\cap\{x_i=0\}|\) is even. Since the half-cube has four vertices, \(|S_i|/2\) is even; thus every nonempty color class has at least four vertices. As \(|Q_E|=8\), at most two classes occur. If precisely \(i,j\) occur, \(\mathbf1_{\{J_y=i\}}\) ignores both bits \(i\) and \(j\), because it is invariant in direction \(i\) while its complement \(\mathbf1_{\{J_y=j\}}\) is invariant in direction \(j\). Therefore it is a nonconstant Boolean function of the sole remaining bit \(k\), giving (TS6).

*Proof when \(p\in E\).* Denote the other two indices by \(b,c\). By (TS5), the membership indicator of \(p\) changes on every \(p\)-edge, so its class contains precisely four vertices of the three-cube. The remaining four vertices are partitioned into classes \(b,c\), each tiled by edges in its matching direction. Suppose both classes occur. Then each comprises precisely one two-vertex edge, one in direction \(b\), one in direction \(c\). Those two differently directed edges cannot lie in the same \(p\)-face: any two perpendicular edges of a two-cube meet. Nor can they lie in opposite \(p\)-faces, because the complement of the \(p\)-class contains precisely one endpoint of each \(p\)-edge, so their projections onto the remaining \(b,c\) square must be disjoint, whereas perpendicular edges in that square always meet. This contradiction proves that all four non-\(p\) vertices have the same label \(j\), and the two labels present are precisely \(p,j\). The \(p\)-membership indicator flips along direction \(p\), and its complement (the \(j\)-class) is invariant in direction \(j\), so the indicator ignores \(j\). With \(k\) the third direction, it must equal \(x_p+t_y(x_k)\), proving (TS7). \(\square\)

**Why this helps the switching program.** The first open balanced branch with three exceptional rules is not an arbitrary triple of nonlinear Boolean functions. Balance reduces it to one antipodally even *minority-label selector* on an explicitly prescribed active set, with the local derivative equations (TS3). In the \(r=1\) branch each frozen three-cube has only a **two-way** switch, never an intrinsically three-way switch. The pair of active labels, and its controlling bit, may vary with the outside state; this cross-fiber compatibility is the next obstacle. The theorem is structural and does not assert NORI1 closure for the three-nonlinear branch.



##### Exterior-reader necessity in the three-exception one-defect branch

**Corollary (two indispensable outside selector variables).** In the \(r=1\) case of (TS1), suppose all three exceptional direction rules are substantively nonunary. Then the minority selector \(J:Q_n\to E\) has at least **two essential input directions outside \(E\)**:
\[
\boxed{|\operatorname{Read}(J)\setminus E|\ge2.}\tag{TS8}
\]

*Proof.* Suppose \(J\) depends on no outside bit or on at most one outside bit \(j\). Freeze the other outside bits, which do not affect \(J\). If there is one remaining outside bit, the antipodally even identity
\[
J(\bar x_E,1-t)=J(x_E,t)
\]
shows that the two frozen sections \(t=0,1\) have the same image set of labels. By fiberwise two-label rigidity (TS6)--(TS7), each section uses at most two labels, hence the global selector uses at most two labels. The zero-outside-bit case follows directly from the same rigidity. Some \(i\in E\) is therefore never the minority, so \(s_i=M=X=\varepsilon\chi_p\) everywhere. If \(p=i\) this contradicts edge consistency (the rule would read its own bit); if \(p\ne i\) it is unary, contradicting the three-exception hypothesis. Thus at least two outside bits are essential to \(J\). \(\square\)

**Finite-interface audit.** Exhaustively list maps \(J:Q_3\to\{a,b,c\}\), and test the own-direction derivative constraints (TS5). If \(p\notin E\), precisely **nine** maps pass: three constant selectors and six two-label single-reader switches. If \(p\in E\), precisely **eight** maps pass: for each of the two possible other labels \(j\), four choices of \(t_y(x_k)\) in (TS7). All valid maps use at most two labels. These numbers independently check the local classification; the proofs of (TS6)--(TS8) are dimension-uniform and do not depend on this finite audit.

**Audit of the solved two-exception switching branch.** Independently of the recent two all-dimensional transport proofs, exhaustive subset-free full-order enumeration verified the mutual-reader common-four-pivot graph of (ST1)--(ST7) in dimension eight for **all 144 legal interface parameter presentations** with two additional opposing unary pairs: each pair reads one of the six directions outside itself, with either sign. The two four-pivot orders \(a,u,v,b\) and \(b,u,v,a\) were checked separately, fixing \(X=1,Y=-1\) and allowing all consistent root and direction orders. Their common transport graphs had between 84 and 256 directed arcs on sixteen \(W\)-states. Every one contained a strongly connected component with an antipodal state pair and a loop at every vertex. This verifies an entire finite interface rank rather than a sample of reader patterns, but the all-dimensional closure relies on the published induction proof.



**Sharp six-dimensional example for (TS8).** The two-outside-reader necessity cannot be strengthened merely by counting the selector's outside essential bits. On \(Q_6\), take \(E=\{0,1,2\}\), \(X=(-1)^{x_3}\), and define an antipodally even ternary selector by \(z=x_4+x_5\pmod2\):
\[
\boxed{
J(x)=
\begin{cases}
0,&z=0,\ x_2+x_4=0,\\
1,&z=0,\ x_2+x_4=1,\\
1,&z=1,\ x_0+x_4=0,\\
2,&z=1,\ x_0+x_4=1,
\end{cases}
\qquad
s_i=X\bigl(1-2\mathbf1_{\{J=i\}}\bigr)\quad(i=0,1,2).
}\tag{TS9}
\]
For the three remaining directions put
\[
\boxed{s_3=(-1)^{x_0},\qquad s_4=-X,\qquad
s_5=-(-1)^{x_0}.}\tag{TS10}
\]
Then \(\sum_{i=0}^2s_i=X\) and \(s_3+s_4+s_5=-X\), giving vertex balance. The selector uses only the two outside bits \(x_4,x_5\), and is even under global antipodal complementation because it depends on the parities \(x_4+x_5,\ x_2+x_4,\ x_0+x_4\). Each exceptional membership indicator ignores its own bit, so all signed rules define undirected edges; their antipodal oddness follows from odd \(X\) and even \(J\).

The essential reader sets, found directly from these formulas, are
\[
\boxed{
\operatorname{Read}(s_0)=\{2,3,4,5\},\quad
\operatorname{Read}(s_1)=\{0,2,3,4,5\},\quad
\operatorname{Read}(s_2)=\{0,3,4,5\}.
}\tag{TS11}
\]
Thus precisely three rules are nonunary, and (TS8) is attained with equality. A separate enumeration of all \(64\) roots and \(6!\) orders finds \(224\) zero-colored rooted full antipodal geodesics. This example confirms that the \(r=1\) three-exception switching interface is nonempty and substantively nonlinear; it is a successful coloring and does **not** counterexample NORI1.


#### Saturated balance: autonomous unary components with one marked reader

Let E be the k nonunary directions of a balanced legal coloring, U its unary directions, and s_i=(-1)^{c_i}. The balance identity gives
\[
\sum_{i\in E}s_i(x)=L(x)=\sum_{j=1}^n m_j\chi_j(x),
\qquad \chi_j(x)=(-1)^{x_j},\quad m_j\in\mathbb Z,\quad
\sum_j|m_j|\le k. \tag{SB1}
\]
For i in U, write c_i=x_{p(i)}+\alpha_i, where p(i)\ne i. Split U into A, the unary directions whose parent chains reach E, and disjoint autonomous components H_1,...,H_t, whose parent chains enter a cycle contained in U. All rules in A read only bits of A∪E; each H_l reads only its own bits.

**Theorem (saturated balancing-sum closure).** Suppose (i) \(\sum_j|m_j|=k\), (ii) every nonzero m_j has j in U, and (iii) each autonomous H_l contains at most one index j with m_j nonzero. Then c has a monochromatic full antipodal geodesic, in every dimension and for arbitrarily complicated nonunary Boolean rules.

*Proof.* At any exterior state y satisfying \(\chi_j(y)=\operatorname{sgn}(m_j)\) at every marked reader j, the balance sum is L(y)=k. All k signed exceptional rules must therefore be +1, or color zero, at **every** E-vertex when the U-bits are frozen at y. Thus any E-direction full geodesic is zero in that frozen face.

Choose bits of A arbitrarily, respecting its marked reader signs. In each H_l, the one-reader theorem supplies a zero full antipodal geodesic. Its vertex sequence visits both values of any selected marked bit, because it traverses that direction once. Choose a cut along this geodesic at a state having the required sign for its sole marked reader, if one exists, or choose any cut otherwise. Let y_H be the tuple of cut states and y the concatenation with the chosen A-bits.

Start with any zero full geodesic of the frozen E-face at y. Apply the previously proved rooted-forest block-absorption lemma to insert all A-directions around it, retaining all zero edges and the frozen U-state throughout the E-block. For every H_l, concatenate the prefix of its chosen zero geodesic before this E∪A path and its suffix afterwards. Its direction rules read no E∪A bits and the A-rules read no H_l bits. Thus all colors remain zero, and every direction is traversed once, giving the required full antipodal geodesic. \(\square\)

**Corollary (three-nonunary saturated branch).** For k=3 and unary balancing defect r=3, if the residual signed-singleton reader indices are all in U and no autonomous unary component contains two distinct residual readers, NORI1 holds for that coloring. It suffices in particular that all residual readers lie in the rooted fringe A.

The obstruction left by this theorem is a joint marked-reader prescription inside a single autonomous unary component, or a nonsaturated signed sum, or marked readers among the exceptional directions. These are explicit dimension-uniform extension targets, rather than a finite-cube verification.


#### Antipodal exposure and arbitrary odd feedforward extension

The unary paired-leaf argument admits an extension to arbitrary odd Boolean rules. The useful invariant records full cube states exposed between exceptional steps; it can be weaker than requiring loops for all assignments of the exceptional bits.

Let \(a,b\) be two distinguished directions, and let \(R\) be all remaining directions. Specify the edge rules in \(R\), allowing dependence on \(a,b\); disregard the two exceptional edge colors while defining transport. An arc \(u\to v\) of \(G\) is witnessed by a full direction order with \(a\) before \(b\), all R-edges zero, and R-states \(u,v\) at those two steps.

For a nonempty strongly connected set \(C\) in \(G\), define its *interior exposure set*
\[
\mathcal E(C)\subseteq Q_{\{a,b\}\cup R}
\]
to consist of every full old cube state visited after the \(a\)-step and before the \(b\)-step, including the state immediately after \(a\) and immediately before \(b\), in every witness of an arc with both endpoints in \(C\). Interior R-states need not belong to \(C\).

Adjoin a new direction \(r\) with rule
\[
c_r=g(x_{\{a,b\}\cup R}),
\]
where \(g\) is any odd Boolean function of the old bits, \(g(\bar x)=1+g(x)\). Every old R-rule ignores the new bit. Let \(G^g\) be the enlarged transport graph.

**Theorem (sharp odd-reader extension criterion).** The subgraph of \(G^g\) induced by \(C\times\mathbb F_2\) is strongly connected if and only if
\[
\boxed{g(x)=0\text{ for some }x\in\mathcal E(C).}\tag{OE1}
\]
Consequently it is strongly connected for **every** odd \(g\) if and only if \(\mathcal E(C)\) contains two antipodal full cube states.

*Proof.* Every old transport arc \(u\to v\) lifts to
\[
(u,w)\longrightarrow(v,w),\qquad w\in\mathbb F_2.
\tag{OE2}
\]
Indeed its full old witness starts and ends at antipodal vertices. The new rule has complementary values at those endpoints, so insert its zero edge before or after the entire old witness. Choose its initial bit to realize the desired \(w\) at both exceptional steps. Old edge colors are unchanged.

Suppose \(g(x)=0\) at an exposed state of an old arc \(u\to v\), with \(u,v\in C\). Insert the new step at that interior state. For either initial new state this supplies
\[
(u,w)\longrightarrow(v,w+1).
\tag{OE3}
\]
Combine (OE3) with a no-flip lifted return path in \(C\). It toggles the new bit in either direction while returning to the old state. The lifted old paths then connect all of \(C\times\mathbb F_2\).

Conversely, if \(g=1\) throughout \(\mathcal E(C)\), no enlarged transport arc with endpoints projecting into \(C\) can traverse \(r\) between the exceptional steps. Removing the new step from any enlarged witness leaves an old transport witness; an interior new step would occur at a state of \(\mathcal E(C)\), where its color is one. Thus every such arc preserves the new state bit, and the induced subgraph cannot be strongly connected.

An odd function takes both values on any antipodal pair. If \(\mathcal E(C)\) contains no antipodal pair, assign \(g=1\) there and \(g=0\) on its antipodal image, extending arbitrarily and oddly to the remaining pairs. This proves the final equivalence. \(\square\)

**Theorem (exposure propagates under extension).** Whenever (OE1) holds, put \(C'=C\times\mathbb F_2\). Then
\[
\boxed{\mathcal E(C')\supseteq\mathcal E(C)\times\mathbb F_2.}\tag{OE4}
\]
In particular, if both \(C\) and \(\mathcal E(C)\) contain antipodal states, these two properties survive every odd feedforward extension.

*Proof.* Lift an old witnessing arc by placing the new step outside the entire old word, as in (OE2). Its new bit can have either prescribed value throughout the old exceptional interval, and every old exposed state persists there. Strong connectivity follows from (OE1); antipodal pairs in \(C\) and in its exposure lift by choosing complementary new bits. \(\square\)

Thus the appropriate robust induction state is an antipodal strongly connected transport set with antipodal interior exposure. A sufficient stronger condition is a loop at each \(z\in C\) for every assignment \(\zeta\in Q_{\{a,b\}}\) of the exceptional bits between their steps: then \(\mathcal E(C)\) contains \(Q_{\{a,b\}}\times C\). An old loop necessarily has the exceptional steps consecutive, since no R-bit changes between them.

##### Modules with arbitrarily many nonlinear feedforward rules

**Corollary (complementary-core feedforward closure).** Begin with an autonomous legal coloring on \(R_0\) having a zero full antipodal geodesic, and two distinguished directions \(a,b\). Repeatedly add a new direction whose edge rule is any odd Boolean function of \(a,b\) and the previously installed directions. Previously installed nonexceptional rules ignore later directions. At the end assign the exceptional rules
\[
c_a=f(x_R),\qquad c_b=1+f(x_R)
\]
for an arbitrary odd Boolean \(f\) on all installed nonexceptional bits. The resulting coloring has a zero full antipodal geodesic.

*Proof.* The chosen autonomous zero path and its reversal supply a bidirectional path of free-cut transport states from a vertex to its antipode, with loops at all those states. Exceptional bits are free, so its exposure contains all four exceptional-bit assignments over every path state, including antipodal full states. Apply (OE1)--(OE4) at every insertion. In the final strongly connected set choose a directed path from a state with \(f=0\) to one with \(f=1\), which exists by oddness and its antipodal pair. An arc crossing these values supplies zero exceptional edges at \(a,b\), together with all the zero nonexceptional edges. The empty initial \(R_0\) is allowed, using its one state and loop. \(\square\)

Balance is preserved when the initial autonomous coloring is balanced and new directions are added in complementary pairs \(g,1+g\) reading the earlier bits. This gives a closure class with arbitrarily many nonunary rules, arbitrary reader-set sizes, and nonlinear dependencies on both exceptional bits. The final exceptional function may depend on every inserted direction.

**Corollary (switching-core feedforward closure).** Start with the negative mutual-reader switching core
\[
s_u=-Y,\qquad s_v=-X,\qquad
s_a+s_b=X+Y,
\]
where the exceptional rules have form (NR2), and their even selector may depend on all subsequently installed nonexceptional bits. Add arbitrarily many complementary pairs of odd reader rules, each reading only \(a,b,u,v\) and earlier pairs. Then the resulting balanced legal coloring satisfies NORI1.

*Proof.* Restrict transport endpoints to the two mixed states \(X=-Y\). The zero \(u,v\)-path (SW2), its reversal, and its free cuts give a bidirectional two-state transport set with loops. The exceptional bits are free, so its interior exposure contains antipodal full states. Every odd feedforward insertion preserves this invariant and the mixed-state restriction on the original \(u,v\) bits. On that restriction the final exceptional signed rules remain complementary. Oddness and a sign-changing transport arc give the full zero geodesic, as in the switching closure proof. Pairwise cancellation preserves vertex balance. \(\square\)

These corollaries extend the transport mechanism through an unbounded number of nonlinear rules. Their ordering hypothesis concerns dependencies among the added rules; the exceptional functions themselves can read all of them.

##### Uniform exceptional-bit loops can fail in a successful balanced cube

The stronger universal-loop condition above is sufficient for exposed transport, but it cannot serve as a universal invariant for all cyclic paired interfaces.

Take \(a=0,b=1,u=2,v=3,r=4,s=5\), and give the four nonexceptional directions the rules
\[
c_u=x_s,\quad c_v=1+x_s,\quad
c_r=x_a+x_b+x_v,\quad c_s=1+x_a+x_b+x_v.
\tag{OE5}
\]
They form two pointwise complementary pairs, have legal odd rules, and depend cyclically between the pairs.

For a loop with the exceptional steps consecutive, let \(q=x_a+x_b\) on the nonexceptional steps. Both exceptional bits flip in their consecutive block, so this \(q\) has the same value before and after that block. The autonomous two-direction cycle on \(v,s\) has rules
\[
c_v=1+x_s,\qquad c_s=1+q+x_v.
\]
For \(q=0\), its zero full two-step paths visit every \((x_v,x_s)\)-state except \((0,0)\). For \(q=1\), they visit every state except \((1,0)\). The attached leaf directions \(u,r\) can be inserted with arbitrary prescribed bits at the cut, by the rooted-tree insertion construction.

It follows that a nonexceptional state supports a loop for **every** exceptional-bit assignment precisely when
\[
\boxed{x_s=1.}\tag{OE6}
\]
This set has no antipodal pair. Thus no antipodal transport set in this interface can satisfy the stronger universal-loop requirement.

For a complete successful balanced coloring, set \(c_a=x_u,\ c_b=1+x_u\). Root zero and order
\[
(0,2,5,1,4,3)
\]
give a zero full antipodal geodesic. Direct enumeration also verifies that the unrestricted transport graph of (OE5) is strongly connected on all sixteen nonexceptional states and its interior exposure comprises all 64 old cube states. Therefore it satisfies the weaker exposed-SCC invariant despite the universal-loop obstruction.

**Audit.** Every odd function on four old bits was tested as a new complementary pair after the elementary unary interface whose old pair reads either exceptional direction, with either sign: all \(4\cdot256\) resulting six-direction transport interfaces are strongly connected. In a fixed-seed sample of 300 cyclic six-direction two-pair interfaces, each transport graph was strongly connected on its sixteen states; its exposure had size 64 in 291 cases and 60 in nine cases, and always contained antipodal states. These finite checks support the exposure invariant as a useful target. Its validity for arbitrary cyclic paired interfaces remains unproved.

**Grand closure target.** Every legal cube coloring has a balanced counterexample-preserving lift with fixed complementary direction pairs. In that class, selecting one pair as \(a,b\) reduces success to a complementary exceptional-core transport problem. Proving the existence of an antipodal strongly connected transport set for arbitrary cyclic paired interfaces would settle unrestricted NORI1. The exposure criterion identifies the additional condition that makes such a set stable under every odd feedforward extension. The unresolved step is a cyclic-block transport theorem retaining this compatibility.


#### Three-nonlinear minority-selector theorem

Suppose a balanced antipodally odd coloring has three exceptional signed rules s_a,s_b,s_c and the other unary rules sum to -q, where q=epsilon*(-1)^x_p. Balance gives s_a+s_b+s_c=q. Define minority selector J in {a,b,c}: s_i=q*(1-2*1_[J=i]). The selector is invariant under antipodal complementation. On every Q3 face obtained by fixing bits outside {a,b,c}, J assumes at most two labels. If p is outside the triple, there are nine possible patterns obeying own-bit invariance: three constant labels, and six binary switches J=i for x_k=t, J=j otherwise, with {i,j,k}={a,b,c}. Proof: every label class A_i is invariant under flipping its corresponding bit. If all three were nonempty, their even cardinalities would be 2,2,4. The two size-two classes would be an a-edge and b-edge. Their union, complement of a c-invariant size-four class, is c-invariant. Translating the a-edge by c would give a disjoint a-edge equal to the b-edge, impossible. With only two labels, J ignores their two bits and depends on the remaining bit. If p=a, membership J=a toggles on every a-edge and membership J=b,J=c is invariant under its own bit. Thus A_a contains four vertices. If both other classes were nonempty they would be b- and c-edges whose projections would partition Q2, impossible since such edges intersect. Hence one of b,c is absent. The eight possibilities are J=a iff x_a=psi(x_k), J=j otherwise, where j is one of b,c, k is the other, and psi is one of four one-bit Boolean functions. In all cases one exceptional signed rule equals q throughout the frozen three-face. The missing label can vary between faces, so this is not a full NORI1 proof.

##### A frozen-core obstruction in Q6

Let Q6 have bits x0,...,x5. Define m=majority(x3,x4,x5), b=x4 xor x5, and J=0 if x0=m, else J=1+b. Set q=(-1)^x0 and signed edge-color rules s_i=q*(1-2*1_[J=i]) for i=0,1,2, and (s3,s4,s5)=(-q,q,-q). The first three signs sum to q and the final three to -q, proving balance. Every rule ignores its own bit: s0=-(-1)^m depends only on x3,x4,x5, s1 and s2 ignore bits 1 and 2, and the final three depend only on x0. The selector J is invariant under global complementation because m and x0 reverse together and b remains fixed, while q changes sign. Hence the coloring is antipodally odd. Its first three essential-reader sets are {3,4,5}, {0,4,5}, and {0,3,4,5}; these are the only nonunary rules. On the frozen four-face x4=x5=0, one has m=0,b=0, and s0=-1, s1=+1 throughout, so there is no monochromatic full geodesic in directions {0,1,2,3}, regardless of starting vertex. But the full Q6 coloring has a red antipodal geodesic with vertices 1,3,11,43,42,58,62, direction order (1,3,5,0,4,2); each signed color along the path is +1. Thus a frozen-core theorem cannot close the balanced three-nonlinear residual-one branch; movement in the complementary unary directions may be indispensable. The coloring axioms and the path were independently verified by full 64-vertex enumeration.

#### Unary functional cycles: a complete cut-state theorem

Let H be a connected set of unary directions, \(c_i(x)=x_{p(i)}+\alpha_i\), with every reader \(p(i)\in H\), \(p(i)\ne i\). Its functional reader graph has one cycle \(C\) and trees attached. Call \(y\in Q_H\) *zero-cut admissible* if some zero-colored full antipodal H-geodesic visits y, possibly at either endpoint.

**Theorem (one forbidden cycle state).**
\[
\boxed{y\text{ is zero-cut admissible}\iff
\exists i\in C:\ c_i(y)=0.}\tag{UC1}
\]
The excluded y are precisely those satisfying \(y_{p(i)}=1+\alpha_i\) for every cycle direction i. Because p permutes the cycle, these equations determine one assignment to the cycle bits and leave every attached-tree bit free.

*Proof.* Project a full zero H-geodesic onto C. The projected path uses every cycle direction once. At any cycle-bit state y_C having all its incident cycle-direction edges colored one, a zero cycle path cannot enter or leave; hence it cannot visit y_C. This proves necessity even when y occurs during attached-tree steps.

For sufficiency first ignore the trees. If the list of cycle-edge colors c_i(y) contains both zero and one, impose precedence conditions
\[
[p(i)\text{ precedes }i]=c_i(y).
\]
Each condition orients the reader-cycle edge. A directed precedence cycle is possible only when all the comparisons point around the cycle in one direction, hence only when all c_i(y) agree. Thus the mixed case admits a topological order, and the full cycle geodesic beginning at y and traversing this order has every color zero.

If every cycle-edge color at y is zero, choose any cycle direction i. Start at y+e_i and traverse \(i,p(i),p^2(i),\dots,p^{|C|-1}(i)\). The first step enters y and reads an unaffected parent bit. Each subsequent step reads a parent not yet flipped, except the final step, which reads bit i already returned to its value at y. Every edge therefore has color zero. This handles all admissible cycle-bit states.

Now insert the attached-tree directions in parent-first order. Keep a cut marker at the occurrence of y_C. When inserting a child j, its parent has already been positioned and has a known initial bit. Put j immediately before or after the parent to make \(x_{p(j)}+\alpha_j+[p(j)\text{ precedes }j]=0\), and choose its initial bit so its value at the cut marker is the prescribed y_j. Insertion does not affect any existing edge color because no previously placed rule reads the new child bit. The resulting zero full H-geodesic visits the complete y. \(\square\)

**Corollary (simultaneous marked readers).** Prescribed values on any subset S of H-bits can be realized at a cut of a zero full H-geodesic if and only if they do not force all cycle bits to the unique forbidden assignment \(y_{p(i)}=1+\alpha_i\). Tree-bit prescriptions impose no further restriction. In particular, fewer than |C| prescribed cycle bits always permit a zero-cut state.

**Strengthening of saturated-balance closure.** In the saturated balancing-sum theorem (SB1)--(SB2), the former requirement of at most one marked reader per autonomous unary component can be replaced by the weaker requirement that its prescribed marked-reader signs do not force that component's forbidden cycle assignment. Choose a zero full component geodesic through the jointly prescribed cut by the corollary, then apply the same rooted-forest absorption and prefix/suffix concatenation argument. The grand conjecture remains open when the residual signs force a forbidden cycle state or the balancing sum is nonsaturated.


#### Three-nonlinear triple-reader cycle-rigidity closure

THEOREM (all-dimensional closure of a balanced three-nonunary branch). Let c be an antipodally odd vertex-balanced binary cube edge coloring, with at most three nonunary signed rules s_a,s_b,s_c. Assume the remaining unary rules have signed sum -X_a-X_b-X_c, where X_i=epsilon_i*(-1)^x_i for i in {a,b,c} and epsilon_i in {+1,-1}. Then c admits a monochromatic full antipodal geodesic in every dimension, regardless of the nonlinear dependence of the exceptional rules on exterior bits or the cycles in the unary reader graph.

RIGIDITY LEMMA. For every fixed exterior bit assignment y, the triple of exceptional signed rules is either (s_a,s_b,s_c)=(X_b,X_c,X_a) or (X_c,X_a,X_b), identically on the exceptional three-cube.

PROOF OF LEMMA. Fix y and regard X_a,X_b,X_c as independent {+1,-1} variables. The balance relation becomes s_a+s_b+s_c=X_a+X_b+X_c. Each s_i ignores X_i. Expand each as a real Fourier polynomial in its two permitted variables. The coefficient of the quadratic term X_b X_c occurs only in s_a, and is zero because the sum on the right has degree one. Similarly all three quadratic coefficients vanish. Therefore each s_i is an affine-linear Boolean {+1,-1} function of its two input signs. Such a function is a constant sign or a signed singleton character: if both linear coefficients were nonzero, the four possible input values could not all be in {+1,-1}. At X_a=X_b=X_c=+1, the sum is 3, forcing all three signed rules to be +1 there. Thus any constant function is +1 and any nonconstant is precisely one of the positive characters X_j. The constant Fourier coefficients of the three s_i sum to zero, hence no constant rule occurs. Comparing the three singleton Fourier coefficients now shows that each X_a,X_b,X_c appears once among the outputs. Since s_i ignores X_i, the resulting permutation has no fixed point. There are only two such permutations, the two displayed three-cycles. QED.

PROOF OF CLOSURE. Every frozen exceptional three-cube has an all-unary legal antipodally odd coloring of one of these two cyclic types, and hence has a red full antipodal geodesic. More explicitly, start at exceptional signs (X_a,X_b,X_c)=(-1,+1,+1). In the first type traverse exceptional directions (a,b,c), and in the second traverse (a,c,b). Each of these three edges has signed color +1, and each direction occurs once. The rooted starting signs are the same for both types. All exterior direction rules are unary by hypothesis. Apply the established uniform frozen-core closure theorem, which absorbs every unary reader tree and every internally cyclic unary component without assuming an acyclic fringe. It gives a red full geodesic of the entire cube. QED.

The exceptional triple may switch between the two directed three-cycles as the exterior bits change; antipodal oddness forces the orientation selector to be invariant under exterior complementation. The proof does not restrict that selector. A Q6 check, with three unmatched unary rules (-X_a,-X_b,-X_c), exhaustively tested all sixteen antipodally even selectors on three exterior bits. All admitted red full geodesics, confirming the algebraic theorem. This closes one dimension-uniform subbranch of the first open balanced three-nonunary case; it does not settle the residual-one branch or the residual-three cases whose reader indices are not the exceptional triple.

#### Universal frozen three-exception Fourier linearization

THEOREM (three-exception Fourier rigidity). Let c be an undirected vertex-balanced binary coloring of Q_n, and let E={a,b,c} be three directions such that every rule outside E is constant or unary. Fix any assignment y of all vertex bits outside E. For each i in E, its signed edge rule s_i=(-1)^(c_i), viewed as a function on the exceptional Q3 with outside state y, is either a constant sign +1 or -1, or a signed singleton character +chi_j or -chi_j for some j in E distinct from i. In particular no exceptional rule has quadratic internal interaction on any frozen exceptional three-face. This assertion does not require antipodal oddness.

PROOF. Balance gives s_a+s_b+s_c equal to the negative sum of the exterior signed rules. Each exterior unary rule restricts to a constant or a signed singleton character on E, and constants remain constant. Therefore the sum of the three exceptional rules has Fourier degree at most one in the three independent signs chi_a,chi_b,chi_c. Each s_i ignores its own bit i and thus is a Boolean function of only the other two exceptional bits on this frozen face. Its possible quadratic Fourier term is the product of those other two characters. This particular quadratic character cannot appear in either of the other two exceptional rules, because each of them ignores one of the two constituent bits. Its coefficient must therefore vanish individually. Hence each s_i is affine-linear over the reals in its two permitted signs. An affine-linear function of two independent signs with values only in {+1,-1} is constant or a signed singleton character: if one slope is nonzero, the two outputs under that input flip differ by two, which forces the other slope and the constant term to vanish. This completes the proof.

COROLLARY (mandatory external readers). Suppose in addition that c is antipodally odd and all three exceptional rules are globally nonunary. Then each of these three rules has at least one essential reader outside E. Otherwise that rule would be independent of y, hence equal globally to one of its frozen templates. An antipodally odd rule cannot be constant, so it would be unary, a contradiction. Thus any hypothetical balanced NORI1 counterexample with just three nonunary rules has at least three directed influence arcs from these exceptions to the unary fringe.

FINITE-STATE CONSEQUENCE. For every exterior state y, the triple (s_a,s_b,s_c) belongs to an alphabet of at most 6^3=216 signed unary-or-constant templates (six per exceptional rule: two constants and four signed readers). Vertex balance filters these templates to those whose signed sum equals the exterior unary imbalance. Arbitrarily high Boolean complexity in the three exceptional rules arises only by switching among these finite templates as the exterior state changes, not by internal quadratic dependence within the exceptional triple. This supplies a bounded local-state formulation for the first open three-nonlinear branch; global compatibility of the templates along unary-direction paths remains to be proved.

#### Uniformly active three-exception faces force a full geodesic

Suppose a balanced antipodally odd Q_n coloring has three nonunary rules on E={a,b,c}, and every other rule is unary. Assume that, for every outside state y, each exceptional rule is nonconstant on the frozen Q_E face. The three-exception Fourier rigidity theorem makes each of those frozen rules a signed singleton character reading another direction in E. Thus every frozen Q_E is an all-unary antipodally odd coloring and has a red full geodesic by the one-reader theorem. The established uniform frozen-core theorem then inserts the full unary fringe, including cyclic reader components, producing a red full antipodal geodesic in Q_n. Consequently, any balanced three-exception NORI1 counterexample must possess a frozen exceptional face on which at least one exceptional rule is constant. Antipodal oddness supplies a second face with the opposite constant color. In the residual-one case with s_a+s_b+s_c=epsilon*chi_a, the minority-selector classification shows that the exceptional rules are all unary on a frozen face when the selector psi depends on its permitted reader bit. When psi is constant, two exceptional directions have opposing fixed colors. Therefore the residual-one subbranch in which psi is nonconstant on every frozen face is closed in all dimensions.

#### Feedback SCC absorption by arbitrary-color one-change paths

Let D(c) have arc j->i when the direction-i rule depends essentially on bit j. Order its strongly connected components K_1,...,K_r topologically, so rules in K_t read only bits in K_1∪...∪K_t. Let B_m mean that every arbitrary binary coloring of Q_m has a full antipodal geodesic with at most one color change, as defined and established through m=7 in Article VIII.

**Lemma (one-change feedforward block extension).** Suppose an antipodally odd edge coloring on a direction set I already has a zero full antipodal geodesic P from x to bar x. Adjoin a set J of m directions, with arbitrary new legal odd rules that may read I∪J, while all old rules ignore J. If B_m holds, the enlarged coloring has a zero full antipodal geodesic.

*Proof.* Freeze the I-bits at x and form the unrestricted binary J-edge coloring d_j(z)=c_j(x,z). By B_m choose a full J-geodesic \(u_0\to u_*\to\bar u_0\) with a zero prefix U and one suffix V, reversing the geodesic if required. Starting at (x,u_*), traverse U in reverse from u_* to u_0, then P on the I-bits, then the reverse of the J-antipodal image of V from u_0 to bar u_* with the I-bits fixed at bar x. Every first-block edge is zero by reversal, and every last-block edge is zero because oddness gives \(c_j(\bar x,z)=1-c_j(x,\bar z)\), while every edge of V was one. The old edges remain zero because old rules ignore J. Every direction appears once, giving a zero full antipodal geodesic. \(\square\)

**Theorem (small strongly connected feedback components cannot obstruct NORI1).** If B_m holds for all \(1\le m\le M\), then every legal antipodally odd coloring whose influence graph has all strongly connected components of cardinality at most M admits a monochromatic full antipodal geodesic.

*Proof.* Begin with the zero-length path on the empty cube. Install the SCCs in topological order, using the lemma at each stage. New rules read only installed directions and their own SCC, and earlier rules ignore newly installed directions by the SCC ordering. The existing zero full path extends through each component, completing the induction. \(\square\)

**Corollary (feedback size at least eight in any hypothetical bad coloring).** Article VIII records the established Leader–Long arbitrary-color one-change theorem B_m for all m≤7, deduced from the geodesic Norin theorem proved through Q_8. Consequently, without assuming balance or limiting the number of nonunary rules,
\[
\boxed{\text{every NORI1 counterexample has an influence SCC of size at least eight}.}\tag{SC8}
\]
This is a dimension-uniform global restriction, not a finite-dimensional exhaustion. The module extension construction was independently checked on 500 randomly generated legal colorings with dependency block patterns (2,3,2), (2,4,1), (3,3), (2,2,3), (2,3,3), finding a zero full antipodal geodesic in each and checking all its edges.


#### Unrestricted NORI1 reduces to strongly connected influence graphs

Let \(A_n\) denote the NORI1 assertion for every legal antipodally odd coloring of \(Q_n\), and \(B_m\) the arbitrary binary edge-color one-change full-geodesic assertion on \(Q_m\). Article VIII gives the dimensionwise bridge implication
\[
\boxed{A_{m+1}\ \Longrightarrow\ B_m.}\tag{SC9}
\]
Its contrapositive says that any arbitrary \(Q_m\) coloring lacking a full \(0^*1^*\) geodesic yields a legal antipodally odd NORI1 counterexample in dimension \(m+1\). This holds whether or not \(B_m\) is known for that dimension.

**Theorem (strong-connectivity reduction).** If unrestricted NORI1 is false, there exists a counterexample of least dimension \(n\) whose directed influence graph \(D(c)\) is strongly connected. Equivalently, proving NORI1 for every legal odd coloring with strongly connected directed influence graph would settle the unrestricted grand conjecture.

*Proof.* Suppose \(c\) is a counterexample of minimum dimension \(n\), and its influence graph has more than one strongly connected component. Order these components topologically and let \(J\) be the last component, \(I=[n]\setminus J\), with \(m=|J|\). Every rule indexed by \(I\) ignores the bits of \(J\), so its restriction to \(Q_I\) is a legal antipodally odd coloring. By minimality of \(n\), this coloring has a color-zero full antipodal geodesic P from some root x to bar x.

The first strongly connected component has at least two vertices: a singleton source would have neither a self-input (forbidden by undirectedness) nor an incoming reader, making its rule constant, contrary to antipodal oddness. Thus \(|I|\ge2\), so \(m+1\le n-1<n\). By minimality, \(A_{m+1}\) holds, hence \(B_m\) holds by (SC9).

The preceding one-change module-absorption lemma now extends P through the final component J, irrespective of its internal dependencies. This gives a color-zero full antipodal geodesic of c, contradicting the choice of c. Therefore \(D(c)\) has only one strongly connected component. \(\square\)

**Corollary (localization of the grand obstruction).** Any minimal-dimensional bad legal coloring has a strongly connected influence graph spanning **all** its directions. In addition, the known NORI1 cases through dimension eight force \(n\ge9\); the prior feedback-component theorem gives the analogous necessary bound of eight for any bad coloring without minimality. Strong connectivity is an unrestricted counterexample-preserving *existence reduction*, not an assertion that the balanced paired lift of a minimal counterexample remains strongly connected.

**Proof-strategy implication.** The grand conjecture can be attacked on one irreducible directed feedback component, rather than on arbitrary arrangements of modules. A proof that every strongly connected odd edge-coloring of the cube admits a monochromatic antipodal geodesic would immediately imply the full theorem by this reduction; no separate gluing hypothesis would remain.


#### Balanced lifts, even tangent vector fields, and the central-fiber zero

Let an antipodally odd balanced Q_(2m) coloring have signed incident-edge colors s_i(v)=(-1)^c_i(v), with centered vertices v in {+1,-1}^(2m). The vector V(v)=(v_i s_i(v)) is tangent to the radial sphere because V(v) dot v=sum_i s_i(v)=0, and is even under inversion because s_i(-v)=-s_i(v). Every continuous even tangent field on S^(2m-1) has a zero: otherwise its normalization w is homotopic to the identity by cos(t)v+sin(t)w(v), implying degree one, but w factors through the double cover S^(2m-1)->RP^(2m-1), so its degree is even. The absence of zeros is impossible.

For the paired balanced lift of odd coloring c on Q_m, signed rules are (s_i(x),-s_i(x)), independent of the dummy bits y. In centered real variables (x,y) in [-1,1]^m times [-1,1]^m, the multilinear extension of the vertex displacement field is (x_i S_i(x),-y_i S_i(x)), where S_i is the multilinear interpolation of s_i. The antipodal oddness implies S_i(0)=0. Thus the vector field vanishes on the central fiber x=0 for EVERY y, including boundary points with y on the dummy cube boundary. Radial tangent projection preserves those zeros. Therefore an unqualified Borsuk-Ulam or Tucker argument applied solely to this canonical local color field cannot reveal a monochromatic full geodesic: its required zeros exist for every input coloring and are unrelated to reachability. To be effective, a new equivariant field must encode nonlocal path support and exclude this zero fiber.

The paired lift is pointwise balanced on subfaces whose free directions are unions of original/dummy pairs, not on arbitrary subfaces. Every binary coloring of dimension >=3 fails to balance some two-dimensional face, since at a common vertex three incident edges cannot have pairwise opposite binary colors.

#### Eight-pivot closure with a paired residual reader

THEOREM. Let c be a vertex-balanced antipodally odd cube edge coloring with precisely three exceptional nonunary directions a,b,c and every other direction unary. Suppose the signed exceptional sum is s_a+s_b+s_c=X_a+X_b+X_p, with X_j=epsilon_j*(-1)^x_j, p outside {a,b,c}. Cancel opposite unary rules sharing a reader. Let the three unmatched unary directions u_a,u_b,u_p have signed rules -X_a,-X_b,-X_p. Assume p belongs to a remaining complementary unary pair {p,p'} whose common reader is a or b. Then the coloring admits a zero full antipodal geodesic in every dimension, regardless of its nonlinear exceptional rules and all remaining unary reader cycles.

PROOF. Normalize bit signs so X_a,X_b,X_p act as independent signed bit characters. The pair p,p' has rules s_p=delta*X_r and s_p'=-delta*X_r, with r=a or b and delta=+1 or -1. Take the eight-direction core T={a,b,c,u_a,u_b,u_p,p,p'}. Fix arbitrary exterior bits. Balance gives s_a+s_b+s_c=X_a+X_b+X_p at every core vertex. If X_a=X_b=X_p=+1, all three exceptional signed rules are +1. Since s_a ignores its own bit a, its sign is therefore + whenever X_b=X_p=+; similarly s_b is + whenever X_a=X_p=+. The c edge is + whenever all three characters are +. These are selector-independent forcing rules.

By symmetry suppose r=a. If delta=+1, choose initial (X_a,X_b,X_p)=(-1,+1,+1) and traverse directions (u_a,p',a,c,b,u_b,p,u_p). The first two steps are red because s_(u_a)=-X_a and s_p'=-X_a. Direction a is red because X_b=X_p=+; afterward X_a=+. Then c is red since all three X signs are +. Direction b is red because X_a=X_p=+; afterward X_b=-. Direction u_b is red because s_(u_b)=-X_b. Direction p is red because s_p=X_a=+; afterward X_p=-. Finally u_p is red because s_(u_p)=-X_p.

If delta=-1, choose initial (X_a,X_b,X_p)=(+1,-1,+1) and traverse (u_b,b,c,p',a,u_a,p,u_p). Direction u_b is red because X_b=-. Direction b is red since X_a=X_p=+, making X_b=+. Direction c is now red at the all-positive sign state. Direction p' has signed value X_a=+. Direction a is red since X_b=X_p=+, leaving X_a=-. Direction u_a is then red. Direction p has signed value -X_a=+, leaving X_p=-, after which u_p is red. For r=b swap a and b and their unmatched partners in these constructions. All eight directions occur once; neither construction uses any information about the exceptional selector or the frozen exterior bits. Hence every frozen core T has a zero full antipodal geodesic. Apply the established uniform frozen-core absorption theorem to the remaining unary directions, including cyclic components. QED.

An independent exhaustive subset-reachability check on the eight-bit core confirms a selector-robust path for each of the four (reader r, sign delta) cases. This closes another dimension-uniform three-nonunary subbranch beyond the earlier result where p equals one of the unmatched unary directions u_a,u_b.

#### Feedback vertex sets of size at most two: unrestricted closure

For a legal antipodally odd edge coloring c, let D(c) be its directed influence graph. Fix a nonempty set F of directions, and let U=[n]\setminus F. Assume the induced digraph D(c)[U] is acyclic, but permit arbitrary nonlinear edge rules and unrestricted dependencies from F into U or U into F.

**Lemma (arbitrary acyclic-fringe absorption).** If for some fixed U-bit state y the induced coloring of the F-dimensional face with U-bits frozen at y has a monochromatic full antipodal F-geodesic, then c has a monochromatic full antipodal geodesic on all n directions.

*Proof.* If the frozen face path has color one, antipodally translate the full cube bits: its image is a zero F-face path at outside assignment bar y, since the global coloring is odd. Thus start with a zero F-geodesic P at some frozen outside state y.

Topologically order U as i_1,...,i_|U| so every U-bit read by the rule of i_t belongs to an earlier index. Build a path word beginning with P as a contiguous F-block. At stage t the new rule c_(i_t) depends only on F and the already installed U-bits, and ignores its own bit. The current path traverses each installed direction once, hence its endpoint is antipodal to its starting root on the installed bits. The new rule is odd under simultaneous complementation of those bits, because it ignores all uninstalled bits. Its values at the endpoints of the current path are therefore complementary. Insert direction i_t before the entire current word if its edge color at the current root is zero, or after the word otherwise. All previously installed rules ignore this new bit by the topological order, so their zero edges are preserved. The new rule ignores its own bit; choose its initial bit to give the prescribed value y_(i_t) during the F-block, which remains contiguous. Induction inserts all U-directions, leaves the exterior state y frozen throughout the F-block, and gives every edge color zero. \(\square\)

**Theorem (one-feedback-vertex closure).** If deleting one direction a makes D(c) acyclic, c satisfies NORI1 in every dimension. Indeed c_a ignores its own bit and is odd in the remaining bits, so some frozen one-dimensional a-face has its edge colored zero. Apply the acyclic-fringe absorption lemma with F={a}.

**Theorem (two-feedback-vertex closure).** If deleting two directions a,b makes D(c) acyclic, c satisfies NORI1 in every dimension.

*Proof.* By the absorption lemma, there is nothing to prove if any frozen \(\{a,b\}\)-square has a monochromatic two-edge antipodal geodesic. Assume no such square exists at any exterior state y. In a two-colored square, any pair of same-color incident edges would form a monochromatic full Q2-geodesic. Thus each vertex must have its two incident edge colors opposite. These conditions around the four-cycle force all a-edges in that square to share one color and all b-edges to have the other color. Consequently, for every y,
\[
\boxed{c_a(x_a,x_b,y)=f(y),\qquad
c_b(x_a,x_b,y)=1+f(y),} \tag{FV2}
\]
independent of both exceptional bits. Antipodal oddness forces f(bar y)=1+f(y).

Order U topologically. Each rule indexed by U is an arbitrary odd Boolean function of a,b and its earlier U-directions; earlier U-rules ignore later U-bits. Thus the entire coloring has the form of the **complementary-core feedforward closure theorem** already proved in this Subsection using the exposed-SCC invariant (OE1)--(OE4), with the initial autonomous R_0 empty and arbitrary final odd complementary exceptional function f. That theorem supplies a zero full antipodal geodesic, contradicting failure. \(\square\)

**Corollary (feedback vertex number at least three in a hypothetical counterexample).** Every legal antipodally odd counterexample to NORI1 has a directed influence graph whose minimum feedback vertex set contains at least three directions. This requires no balance assumption and permits arbitrarily many nonunary rules. In conjunction with the SCC localization theorem, a minimum-dimensional bad coloring has one strongly connected dependency graph of dimension at least nine **and feedback vertex number at least three**.

**Verification.** The single-feedback-vertex greedy insertion was independently tested on 1,600 random legal odd colorings of dimensions 3 through 10, with arbitrary odd nonlinear feedforward rules on every other direction; every produced path was checked edge by edge and ended at the antipode. The two-feedback-vertex result is a composition of the new general absorption lemma with the previously verified complementary-core feedforward theorem, not an assumption that frozen two-faces are always solvable.


#### Full eight-pivot closure for all internal paired readers

THEOREM (selector-robust eight-pivot closure, arbitrary internal unary reader). Let c be a balanced antipodally odd cube coloring whose only nonunary directions are a,b,c. Suppose s_a+s_b+s_c=X_a+X_b+X_p, where X_i=epsilon_i*(-1)^(x_i), the reader p is distinct from a,b,c, and after cancellation of opposing same-reader unary rules the three unmatched unary directions u_a,u_b,u_p have signed values -X_a,-X_b,-X_p. Suppose direction p is a member of a complementary unary pair {p,p'} whose common reader r is ANY member of {a,b,c,u_a,u_b,u_p}. Then c contains a monochromatic full antipodal geodesic in every dimension, for every allowed nonlinear selector and every remaining unary fringe.

PROOF. Normalize the signs of relevant bits so X_a=(-1)^(x_a), X_b=(-1)^(x_b), X_p=(-1)^(x_p), and the paired rules become s_p=delta*(-1)^(x_r), s_p'=-delta*(-1)^(x_r), delta=+1 or -1. Take the eight-direction core T={a,b,c,u_a,u_b,u_p,p,p'}. At EVERY vertex, the sum of exceptional signs equals X_a+X_b+X_p. Therefore s_a is positive whenever X_b=X_p=+1: set X_a=+1 while keeping all other bits fixed, obtain sum three so every exceptional sign is positive, then toggle a back using that s_a ignores a. Similarly s_b is positive whenever X_a=X_p=+1. Finally s_c is positive whenever X_a=X_b=X_p=+1. These three guarantees do not depend on the nonlinear selector or other bits.

The following finite path certificate covers all twelve cases. Number the eight core directions 0=a,1=b,2=c,3=u_a,4=u_b,5=u_p,6=p,7=p'. The displayed root is an eight-bit integer in this normalized labeling; the right-hand tuple is the direction order. For each row, begin at that root and flip the listed bits in order. The exceptional edges satisfy the preceding three forced-red conditions, and the five unary edges have positive signed color by their reader rules.
reader r=0, delta=-1: root 2, order (4,1,2,7,0,3,6,5).
reader r=0, delta=+1: root 1, order (3,7,0,2,1,4,6,5).
reader r=1, delta=-1: root 1, order (3,0,2,7,1,4,6,5).
reader r=1, delta=+1: root 2, order (4,7,1,2,0,3,6,5).
reader r=2, delta=-1: root 1, order (3,0,7,2,1,4,6,5).
reader r=2, delta=+1: root 5, order (3,0,7,2,1,4,6,5).
reader r=3, delta=-1: root 1, order (7,3,0,2,1,4,6,5).
reader r=3, delta=+1: root 2, order (4,1,2,0,6,3,5,7).
reader r=4, delta=-1: root 1, order (3,0,2,1,7,4,6,5).
reader r=4, delta=+1: root 1, order (3,0,2,1,6,4,5,7).
reader r=5, delta=-1: root 33, order (3,0,2,1,4,6,5,7).
reader r=5, delta=+1: root 1, order (3,0,2,1,4,6,5,7).

Every displayed order uses every one of the eight core directions once, so its endpoint is antipodal to its root. The table constitutes a direct finite proof for EVERY frozen exterior state, without fixing the nonlinear selector. The established uniform frozen-core absorption theorem adds all remaining unary directions, regardless of reader cycles, to yield a monochromatic full antipodal geodesic on Q_n. QED.

This extends the previous paired-reader theorem from r in {a,b} to all six internal readers, including r=u_p, where the unary rules of p and u_p form a reciprocal dependency. A direct subset dynamic program checked all twelve rows against the selector-independent forced-red edge conditions. It also extends a concurrent six-pivot closure theorem dealing with the case p=u_a or p=u_b. The residual-three cases in which p's unary pair reads a direction outside this eight-direction core remain open by this method.

#### Rooted paired-reader chains via subdivision

THEOREM (arbitrary-depth rooted reader-chain closure). Let c be a balanced antipodally odd cube coloring with exceptional nonunary directions E={a,b,c} and every other direction unary. Suppose s_a+s_b+s_c=X_a+X_b+X_p, where X_i=epsilon_i*(-1)^x_i, p is outside E, and the three unmatched unary directions u_a,u_b,u_p have signed rules -X_a,-X_b,-X_p after cancelling opposing same-reader pairs. Let T0={a,b,c,u_a,u_b,u_p}. Suppose p belongs to a complementary same-reader unary pair P0, and repeatedly following the common reader of each pair through the containing paired vertex reaches T0, without first entering a reader cycle. Then c has a monochromatic full antipodal geodesic in every dimension, regardless of the nonlinear selector or all other unary reader cycles.

PROOF. We use the previously proved eight-pivot theorem, which gives for any r in T0 and any sign delta a full zero core geodesic on T0 union P0 if P0 reads r. The exceptional edges in its twelve explicit witnesses are guaranteed positive solely by the balance saturation conditions: s_a is positive when X_b=X_p=+, s_b when X_a=X_p=+, and s_c when X_a=X_b=X_p=+. These guarantees hold under arbitrary changes of the other vertex bits, so all such paths are selector-robust.

READER-SUBDIVISION LEMMA. Suppose a selector-robust red full path includes a complementary unary pair {v,w} whose opposite signed rules read a direction r already used by the path. Since both pair edges are red and their signed functions are opposite, the unique r-step lies strictly between the v- and w-steps. Introduce a new complementary unary pair {j,j'} with signed rules eta*chi_r and -eta*chi_r, and replace the old pair rules by opposite signed unary characters reading j instead of r. Insert j and j' on opposite sides immediately adjacent to the r-step, choosing the side for j where eta*chi_r is positive and the opposite side for j'. Both insertions occur between v and w because r is between them. Choose the initial bit j so that the first of v,w has positive signed color; its complement is then positive after j is crossed. The other old unary rules are unaffected. The selector-robust exceptional edges remain positive because the inserted moves do not alter X_a,X_b,X_p and their positivity criteria ignore arbitrary additional bits. Thus the new longer core also has a selector-robust red full path, with the pair {j,j'} straddling its reader r.

Let the chain of paired nodes be P0 -> P1 -> ... -> Pm -> T0, with Pk reading a member of P(k+1) and Pm reading a direction r in T0. Begin with the eight-pivot witness for P0 artificially reading r. Apply the subdivision lemma to P0, introducing P1 with reader r and redirecting P0 to its required reader inside P1. Apply it next to P1, introducing P2 with reader r and redirecting P1 to its required reader, and continue. After the last insertion, every paired node in the chain has its required unary reader, including Pm reading r. All exceptional steps remain positive independently of their nonlinear selector and the frozen bits outside this core. The construction therefore gives a red full geodesic on the enlarged core for EVERY frozen exterior assignment. The uniform frozen-core theorem then absorbs all other unary directions, including internally cyclic components, and yields a red full antipodal geodesic on the whole Q_n. QED.

The statement extends the finite eight-pivot reader theorem to arbitrarily long functional reader chains, without bounding the cube dimension or the selector complexity. In the two-internal/one-external reader pattern, the remaining paired-reader configuration outside this theorem is one where the reader chain of p enters a cycle disjoint from the six-pivot core (along with configurations where p is itself unmatched, addressed separately by a concurrent six-pivot result). No claim is made here for the internally cyclic reader-chain case.


#### Autonomous-reader closure for the residual-three balanced pivot

Retain the balanced three-exception setting of the eight-pivot and rooted reader-chain theorems. Let the three nonunary directions be \(a,b,c\), and suppose after canceling pointwise complementary unary pairs there remain three unmatched unary directions \(u_a,u_b,u_p\) with signed rules
\[
\boxed{s_{u_a}=-X_a,\quad s_{u_b}=-X_b,\quad s_{u_p}=-X_p,
\qquad s_a+s_b+s_c=X_a+X_b+X_p,}\tag{AR1}
\]
where \(X_a=\varepsilon_a(-1)^{x_a}\), \(X_b=\varepsilon_b(-1)^{x_b}\), and \(X_p=\varepsilon_p(-1)^{x_p}\), with \(p\) different from all six displayed directions. The exceptional rules are undirected and hence \(s_a,s_b,s_c\) ignore their own respective bits.

**Lemma (saturation-forced pivot word with autonomous reader module).** Suppose \(H\) is a set of directions containing \(p\) and disjoint from
\(T_0=\{a,b,c,u_a,u_b,u_p\}\), such that all rules indexed by \(H\) ignore every vertex bit outside \(H\), and the induced coloring on \(Q_H\) has a signed-positive full antipodal geodesic. Then the coloring on the \(T_0\cup H\) face, with all other bits frozen arbitrarily, has a signed-positive full antipodal geodesic, regardless of the values and nonlinearity of the exceptional rules.

*Proof.* Let \(P_H\) be a signed-positive full antipodal geodesic for the autonomous \(H\)-coloring. Reverse it if necessary so that \(X_p=+1\) at its initial vertex. This is possible since \(P_H\) traverses the \(p\)-direction once, so its endpoints have opposite \(X_p\)-values, and reversing preserves undirected edge colors.

Set initially \(X_a=-1,\ X_b=+1\); take the \(H\)-initial state from \(P_H\), so \(X_p=+1\). All other initial bits, including frozen exterior bits and the bit \(c\), may be arbitrary. Traverse the direction word
\[
\boxed{u_a,\ a,\ c,\ b,\ u_b,\quad P_H,\quad u_p.}\tag{AR2}
\]
The first edge has \(s_{u_a}=-X_a=+1\). For the \(a\)-edge, \(X_b=X_p=+1\). At the neighboring state obtained by changing just bit \(a\), the three signs \(X_a,X_b,X_p\) are all \(+1\); (AR1) forces \(s_a=s_b=s_c=+1\) there. Since \(s_a\) ignores bit \(a\), its value is also \(+1\) at the current \(a\)-step. After that step \(X_a=X_b=X_p=+1\), so the \(c\)-edge has sign \(+1\). The \(c\)-step leaves \(X_a,X_b,X_p\) unchanged. Hence the \(b\)-edge has sign \(+1\), regardless of the exceptional selector; afterward \(X_b=-1\) and \(s_{u_b}=-X_b=+1\).

The entire path \(P_H\) remains positive because its rules depend only on \(H\). It traverses \(p\), changing \(X_p\) from \(+1\) to \(-1\). Thus the final \(u_p\)-edge has sign \(s_{u_p}=-X_p=+1\). No direction occurs twice. The concatenated word traverses all directions of \(T_0\cup H\) once, ends at the antipode in those directions, and is monochromatic positive. The exceptional saturation argument is independent of all other frozen bits. \(\square\)

**Theorem (complete autonomous-cycle reader-chain subbranch).** In the setting (AR1), assume that \(p\) belongs to one of the canceled complementary unary pairs and that the functional reader chain of this pair, followed through the other complementary pairs, enters an internally read directed cycle of paired nodes **without meeting \(T_0\)**. Then the full coloring has a monochromatic full antipodal geodesic in every dimension, with no restriction on the nonlinear exceptional selector or the remaining unary dependency components.

*Proof.* Let \(H\) be the union of all directions in the paired nodes along the chain from the pair containing \(p\) through the entered reader cycle. Every paired rule in this union reads another direction in the same union. Thus the induced coloring on \(Q_H\) is autonomous, legal, antipodally odd, and all-unary. By the established one-reader theorem, it admits a signed-positive full antipodal geodesic. (If that theorem supplies a monochromatic-negative path, apply antipodal translation of its root to obtain a positive one.) The lemma gives a positive full antipodal geodesic on \(T_0\cup H\), for **every** assignment of the remaining frozen bits. Every direction outside \(T_0\cup H\) is unary. Apply the previously proved uniform frozen-core absorption theorem, including its cyclic-fringe case, to obtain a positive full antipodal geodesic in the whole cube. \(\square\)

**Consequences.** The earlier rooted reader-chain theorem closes the case where the pair containing \(p\) reaches \(T_0\); the theorem above closes the complementary case where it reaches an autonomous paired cycle. These are all possible eventual behaviors of that pair's functional reader chain. Therefore the entire balanced three-exception residual-three subbranch (AR1), with \(p\) outside the six-pivot core and belonging to a canceled complementary unary pair, is now closed **regardless of its reader-chain topology**. This does not cover configurations where \(p\) itself is an unmatched unary direction or where the three singleton reader indices occupy other positions; it also does not prove unrestricted NORI1.

**Independent witness check.** On \(Q_{10}\), take \(a=0,b=1,c=2,u_a=3,u_b=4,u_p=5,p=6\), an autonomous paired module \(H=\{6,7,8,9\}\) with
\[
s_6=\chi_8,\ s_7=-\chi_8,\ s_8=\chi_6,\ s_9=-\chi_6,
\]
and the permitted saturated exceptional template
\(s_0=\chi_1,s_1=\chi_6,s_2=\chi_0\).
The \(H\)-path with root bits \(x_8=1\) and \(x_6=x_7=x_9=0\), in order \((7,8,6,9)\), has every signed color positive and starts with \(X_p=+1\). Set \(x_0=1,x_1=0\), then traverse
\[
(3,0,2,1,4,\ 7,8,6,9,\ 5).
\]
All ten edges have signed color \(+1\) and the endpoint is antipodal. This small witness illustrates the selector-independent construction; the dimension-uniform proof does not depend on the check.



**Corollary (complete two-internal-reader, one-external-reader branch).** Suppose a legal vertex-balanced antipodally odd coloring has precisely three nonunary directions \(a,b,c\), and its exceptional signed sum is
\[
\boxed{s_a+s_b+s_c=X_a+X_b+X_p,\qquad p\notin\{a,b,c\},}\tag{AR3}
\]
with \(X_a=\varepsilon_a\chi_a,\ X_b=\varepsilon_b\chi_b,\ X_p=\varepsilon_p\chi_p\). Then the coloring has a monochromatic full antipodal geodesic in every dimension.

*Proof.* By balance, the unary signed-character sum is \(-X_a-X_b-X_p\). Select one unmatched unary direction \(u_a,u_b,u_p\) with rules \(-X_a,-X_b,-X_p\), respectively; these three directions are distinct. All other unary rules form pointwise complementary same-reader pairs. Since a rule cannot read its own bit, \(p\ne u_p\). If \(p=u_a\) or \(p=u_b\), invoke the already established six-pivot saturated-core theorem, which gives a monochromatic geodesic for every frozen exterior assignment and absorbs the other unary directions. Otherwise \(p\) belongs to one of the complementary pairs. Follow the reader of that pair through the functional paired-reader graph. Since the graph is finite, the chain either encounters \(T_0=\{a,b,c,u_a,u_b,u_p\}\), or enters an internally read cycle of paired nodes without encountering \(T_0\). In the first case apply the previously established arbitrary-depth rooted reader-chain theorem. In the second apply the autonomous-cycle reader-chain theorem above. All cases are closed. \(\square\)

The result handles arbitrary nonunary selector functions and arbitrary other unary dependency cycles, and makes no restriction on dimension. It advances the established three-exception classification beyond separate rooted and cyclic reader-chain special cases. The remaining \(r=3\) branches are those with fewer than two exceptional-direction reader indices among the three distinct singleton terms, or with a repeated-reader coefficient \(2X+Y\); the \(r=1\) minority-selector branch also remains open. None of these unsolved branches is being declared closed.



#### Repeated-reader elimination in the three-nonlinear balanced branch

The bounded unary balancing defect (UD2)--(UD3) permits the residual-three signed sum \(L=s_a+s_b+s_c\) to be of the form \(2X+Y\), with \(X=\varepsilon\chi_p\), \(Y=\eta\chi_q\), \(p\ne q\). The undirected-edge identities eliminate an entire class of internal readers.

**Theorem (no exceptional reader in a repeated-singleton sum).** Let \(E=\{a,b,c\}\) consist of three substantively nonunary signed rules in a vertex-balanced legal coloring and suppose
\[
\boxed{s_a+s_b+s_c=2X+Y,\quad X=\varepsilon\chi_p,\quad Y=\eta\chi_q,\quad p\ne q.}\tag{RR1}
\]
Then
\[
\boxed{\{p,q\}\cap E=\varnothing.}\tag{RR2}
\]
This assertion uses undirectedness and the signed-sum equation only; antipodal oddness is not separately needed for the elimination.

*Proof.* Whenever \(X=Y\), the sum in (RR1) is \(3X\), so necessarily
\[
s_a=s_b=s_c=X=Y.
\]
Suppose \(p=i\in E\). Fix all bits other than \(i\). precisely one of the two values of bit \(i\) gives \(X=Y\), because \(X\) changes when \(i\) changes and \(Y\) does not. At that value \(s_i=Y\). Since an undirected direction-\(i\) edge rule ignores its own bit \(i\), its value at the other setting is also \(Y\). This holds for every assignment of the other bits, proving \(s_i=Y\) globally. Since \(q\ne i\), this is a signed unary character, contradicting the assumption that \(i\) is nonunary.

Similarly if \(q=i\in E\), fix the other bits and choose the unique value of bit \(i\) where \(X=Y\). Then \(s_i=X\) there, and own-bit independence forces \(s_i=X\) at the other setting, making direction \(i\) unary. These contradictions prove (RR2). \(\square\)

**Implications for the first open balanced branch.** In the three-exception classification, an \(r=3\) repeated-reader term \(2X+Y\) cannot have *either* singleton reader inside \(E\). The full \(r=3\) three-distinct-reader case with at least two internal reader indices is closed by the triple-reader rigidity and the complete two-internal-one-external theorem (AR3). Thus a remaining three-exception counterexample must lie in one of the following substantively global configurations: (i) the residual-one minority selector (TS1)--(TS8); (ii) three distinct residual singleton readers with at most one internal reader; or (iii) the repeated-reader configuration (RR1) with both readers exterior. This is a dimension-uniform exhaustion of the *algebraic* residual-three cases, not a claim that any surviving configuration yields a counterexample.



##### Autonomous two-reader saturation and the only forbidden unary cut

Continue in the repeated-reader case (RR1), where (RR2) places the two singleton readers \(p,q\) outside the exceptional directions \(E=\{a,b,c\}\). By signed-character cancellation there are three distinct unmatched unary directions \(u,v,w\) with
\[
\boxed{s_u=s_v=-X,\qquad s_w=-Y,\qquad s_a+s_b+s_c=2X+Y.}\tag{RA1}
\]
The remaining unary directions form opposite same-reader pairs. Note \(p\ne u,v\) and \(q\ne w\) by undirectedness.

**Lemma (two-reader saturation cut).** Let \(H\subset[n]\setminus(E\cup\{u,v,w\})\) contain both \(p,q\). Suppose every rule indexed by \(H\) depends only on the \(H\)-bits and the induced \(H\)-coloring has a signed-positive full antipodal geodesic \(P_H\) visiting a vertex \(z\) at which
\[
\boxed{X(z)=Y(z)=+1.}\tag{RA2}
\]
Then for *every* frozen assignment of the remaining direction bits, the coloring induced on the \((E\cup\{u,v,w\})\cup H\) face has a signed-positive full antipodal geodesic, regardless of the exceptional nonlinear selector. Thus, if all directions outside this core are unary, the full coloring satisfies NORI1.

*Proof.* At any state with \(X=Y=+1\), (RA1) gives \(s_a+s_b+s_c=3\), hence every exceptional edge direction has signed color \(+1\), independent of all other bits, including the exceptional bits themselves. Split the positive \(H\)-geodesic at the occurrence of \(z\), and insert the three exceptional steps \(a,b,c\) consecutively at that cut. Each is positive since all its steps retain \(X=Y=+1\).

For each of the unmatched directions \(u,v,w\), insert its unique step at a point of \(P_H\) where its reader sign is negative: \(X=-1\) for \(u,v\) and \(Y=-1\) for \(w\). Such points exist because the \(H\)-geodesic traverses directions \(p,q\) once each and therefore changes the sign of each from its value \(+1\) at \(z\). The unmatched steps do not change the \(H\)-bits, and their rules read only \(p\) or \(q\); all are positive at their selected insertion points. The \(H\)-edges remain positive because the \(H\)-coloring is autonomous. Inserting the unmatched steps also cannot change the three exceptional colors at the saturation cut, which are forced to \(+1\) at every state with \(X=Y=+1\). The resulting word traverses every core direction once and is positive. It works for arbitrary exterior frozen states, so the existing uniform frozen-core absorption theorem inserts the remaining unary directions. \(\square\)

**Corollary (unary-cycle sufficient criterion).** Suppose \(H\) above is autonomous and all-unary. Decompose its functional reader graph into connected unicyclic components, each with directed cycle \(C\). Let \(z_p,z_q\) denote the required bit values making \(X=Y=+1\). If no component containing the prescribed readers \(p,q\) is forced by those prescriptions to have *all* its cycle bits at its unique zero-cut-forbidden assignment from the unary functional-cycle cut theorem (UC1), then the coloring satisfies NORI1.

In particular this criterion automatically holds when \(p,q\) lie in different unary functional components, or lie in a common component with a reader cycle of length at least three, or when at least one of \(p,q\) lies off that component's cycle. The only possible obstruction under this criterion is when \(p,q\) are the two directions of one reader two-cycle and the required \(X=Y=+1\) assignment coincides with that cycle's forbidden cut state.

*Proof.* By the previously proved complete cut-state theorem (UC1), a zero full geodesic through any prescribed state exists in each connected autonomous unary component unless the prescription forces all cycle bits to the forbidden assignment. Tree bits impose no constraint. Choose such a zero path in each component, passing through states with the prescribed \(p,q\) bits wherever those readers occur. Interleave their prefixes up to the designated states, then their suffixes, producing a zero full \(H\)-geodesic visiting a joint state \(z\) with \(X=Y=+1\). The lemma applies. With at most two prescribed bits, all cycle bits can be forced only for a cycle of length two whose two members are both \(p,q\). \(\square\)

This theorem closes a dimension-uniform repeated-reader three-exception subbranch without assuming the exceptional selector is simple. The sharply isolated two-reader-cycle cut obstruction is a gap in this particular saturation-cut method, not a candidate NORI1 counterexample: other successful geodesics may exist without visiting an \(X=Y=+1\) state of the autonomous unary module.


#### Strongly connected nonunary kernel of a dimension-minimal obstruction

Let D(c) have arc j->i if rule i essentially reads input bit j; let E consist of nonunary rules and U of unary rules.

**Lemma.** If D(c) is strongly connected and E is nonempty, then D(c)[U] is acyclic. For any directed cycle in U, each vertex already receives its sole incoming influence arc from its predecessor on that cycle. The cycle has no incoming arcs from outside, contradicting strong connectivity because E is outside it.

**Theorem.** If unrestricted NORI1 fails, a dimension-minimal legal odd counterexample c has:
(i) a strongly connected influence graph;
(ii) an acyclic U subgraph, with every unary parent chain reaching E, so E is a feedback vertex set and every unary direction belongs to a directed cycle meeting E;
(iii) at least three nonunary rules, giving
\[
\boxed{M(c)=\sum_i|\operatorname{Read}(c_i)|\ge n+2|E|\ge n+6,}\tag{NK1}
\]
without balance;
(iv) **no** monochromatic full antipodal E-geodesic in **any** face obtained by freezing the U bits;
(v) the opposite frozen faces linked by
\[
\boxed{d_{\bar y,i}(\bar x)=1+d_{y,i}(x)\pmod2,\quad i\in E.}\tag{NK2}
\]

*Proof.* (i) is the published dimension-minimal SCC theorem. The lemma gives (ii), and the previously proved feedback-vertex-two theorem excludes |E|≤2. Antipodal oddness forces every unary rule to read one bit and each nonunary rule to read at least three, giving (iii). For (iv), any monochromatic E-face geodesic would extend to the full cube by the published acyclic-fringe absorption theorem. Finally (v) is the antipodal oddness identity with vertex bits split into E and U. \(\square\)

A minimum-dimensional obstruction therefore contains one nonlinear-feedback kernel E and a completely acyclic unary fringe, while **every frozen E-face is a bad arbitrary-color E-cube**. The face colorings need not themselves be odd. This is a dimension-uniform irreducible normal form, not a NORI1 proof.


#### Three-nonlinear all-face core obstruction and eight local types

For every even N>=8, there is a balanced antipodally odd cube coloring with only three nonunary direction rules such that every four-face retaining these three exceptional directions and their unmatched unary reader has no monochromatic antipodal full geodesic, although the whole cube DOES have one. Base Q8: index bits a,b,c,u,w0,w1,w2,w3 as 0,..,7. Put chi_i=(-1)^x_i, lambda=2*majority(w0,w1,w2)-1, k=w0 XOR w1. Set signed rule s_a=lambda; if k=0 let (s_b,s_c)=(chi_a,-lambda), otherwise (-lambda,chi_a). Set s_u=-chi_a and (s_w0,s_w1,s_w2,s_w3)=(chi_a,-chi_a,chi_a,-chi_a). Here signed +1 means color zero. Every rule ignores its own bit. Global complementation flips lambda and chi_a but preserves k, proving oddness. Sum of the signed rules is zero, proving balance. Directions a,b,c have at least three essential readers; all remaining rules are unary. At every frozen exterior w state, s_a=lambda and one of s_b,s_c=-lambda are opposing constant signs throughout the four-face on a,b,c,u; no monochromatic full four-face path is possible in either color. Yet the full red geodesic from root zero in order (6,1,4,2,0,7,5,3) visits vertices 0,64,66,82,86,87,215,247,255. All eight edges have signed value +1. Add any number of opposite unary direction pairs with signs (chi_a,-chi_a). These preserve oddness, balance, the same three nonlinear rules and all frozen four-face obstructions; inserting the new first-member edges before direction a and second-member edges after direction a extends the full red path. Thus the construction works in Q_(8+2r) for all r>=0. The theorem shows that no argument requiring a monochromatic geodesic inside some frozen four-direction core can close the first balanced three-nonlinear branch, even with antipodal symmetry; motion through exterior directions is essential.

LOCAL EIGHT-TYPE CLASSIFICATION. In the balanced three-nonlinear residue-one case s_a+s_b+s_c=chi_a, with unmatched unary rule s_u=-chi_a, fix all bits except a,b,c,u. At either frozen u-layer, the signed triple (s_a,s_b,s_c) is one of eight types: T0=(-1,chi_a,+1), T1=(-1,+1,chi_a), T2=(chi_c,-chi_c,chi_a), T3=(chi_b,chi_a,-chi_b), T4=(-chi_b,chi_a,chi_b), T5=(-chi_c,chi_c,chi_a), T6=(+1,-1,chi_a), T7=(+1,chi_a,-1). Proof: each signed exceptional rule ignores its own bit; applying mixed discrete differences to the signed sum shows each is a constant or signed singleton character on the other two exceptional bits. One of s_b,s_c must equal chi_a, and the remaining two functions cancel, giving the eight cases. For any ordered pair of u-layer types, red full four-face geodesics exist in 52 out of 64 cases. The twelve failures, indexed by layer types (i,j), are (0,0),(0,1),(0,6),(1,0),(1,1),(1,7),(6,0),(6,6),(6,7),(7,1),(7,6),(7,7). A finite exhaustive certificate tests 16 roots and 24 direction orders per case. All 52 successful cases have a witness with one of four direction orders: (b,a,u,c), (b,c,a,u), (b,u,a,c), (c,b,a,u). Therefore one u-layer having a type among T2,T3,T4,T5 guarantees a red four-face geodesic, regardless of the other layer. For corner types 0,1,6,7, the only successful pairs are (0,7),(1,6),(6,1),(7,0). The Q8 construction above has identical corner types in both u layers, ensuring failure. Antipodal complement sends types 0<->7,1<->6 and fixes 2,3,4,5, while exchanging the two layers. Its action preserves the twelve-pair failure relation. Thus local antipodal parity alone cannot force a successful frozen core.

##### Three-state twisted transport and the chromatic obstruction

Let K be a directed graph with fixed-point-free involution J. Define T(K) as the undirected graph with edges {y,J(z)} for every arc y->z, including loops. For a selector g with q possible values, an arc y->z satisfying g(y)=g(J(z)) is forced for all g if and only if the chromatic number chi(T(K)) exceeds q. Indeed a selector avoiding all such arcs is just a proper q-coloring of T(K).

A looped strongly connected component with antipodal vertices is insufficient for q=3. In Q3 set (v0,...,v5)=(000,001,011,111,110,100). Let K have directed cycle v0->v1->v2->v3->v4->v5->v0 and a loop at each vertex. The involution is J(v_i)=v_(i+3 mod 6). Color these vertices around the cycle (A,A,B,B,C,C). For each loop i->i, g(v_i) differs from g(v_(i+3)); for each directed edge i->i+1, g(v_i) differs from g(v_(i+4)). Thus no matching-selector arc exists. The twisted graph contains triangles on even and odd indices joined by a perfect matching, the triangular prism, which is 3-chromatic. This is a sharp counterexample to the naive ternary generalization of the binary antipodal-SCC forcing lemma, not a NORI1 counterexample and not a construction of a unary-pair transport graph from a cube coloring. A general finite-alphabet exchange theorem must prove chromatic number at least q+1 using added cubical structure.

#### Nonunary feedback-kernel quotient

Let D be a strongly connected directed influence graph with nonempty nonunary direction set E and unary direction set U. The induced graph on U is acyclic by the earlier unary-cycle exclusion lemma. Every unary direction u has one parent p(u); iterating p reaches a unique root \(\rho(u)\in E\). Set \(\rho(e)=e\) for e in E.

Form a multigraph H on E by including an arc \(\rho(j)\to i\) for each essential reader j of every nonunary rule i. Loops and parallel arcs are allowed.

**Theorem (feedback-transversal preservation).** For every subset T of E,
\[
\boxed{D\setminus T\text{ is acyclic}\iff H\setminus T\text{ is acyclic},\qquad \tau(D)=\tau(H),}\tag{FK1}
\]
where tau is the minimum cardinality of a directed feedback vertex set.

*Proof.* Each D-cycle must meet E, since U is acyclic. Between successive E vertices on a D-cycle are unary chains, each necessarily rooted at the preceding E vertex because each unary vertex has only one incoming reader arc. Contracting these chains gives a positive-length closed H-walk avoiding T, and hence an H-cycle. Conversely each H-arc is realized by the corresponding root-to-reader unary chain, followed by the reader's influence edge into its nonunary target. An H-cycle lifts to a closed D-walk, and thus a D-cycle, with no intermediate nonunary directions. This proves the equivalence for T⊂E.

For arbitrary feedback vertex set F⊂V(D), replace each unary u∈F by its root \(\rho(u)\), retaining the nonunary elements of F. The resulting T⊂E has |T|≤|F|. Every directed cycle through a unary u must also contain \(\rho(u)\), by backward iteration along that vertex's unique incoming reader arcs. Thus a D-cycle avoiding T would also avoid F, a contradiction. Therefore T is a feedback vertex set of D and H. Any feedback set of H likewise breaks D-cycles by the first assertion, proving equality of minimum sizes. \(\square\)

**Corollary (three disjoint private feedback cycles).** If c is a minimum-dimensional bad NORI1 coloring with E={a,b,d}, then \(\tau(D)\ge3\) by feedback-two closure. Thus \(\tau(H)=3\). Deleting any two vertices of the three-vertex H must leave a directed cycle, forcing a loop at each of a,b,d. Each loop corresponds to an essential reader of that exceptional rule lying in its own unary descendant tree, yielding a directed cycle from that exceptional vertex through unary directions back to itself. Since unary-parent roots are unique, the three resulting feedback cycles are vertex-disjoint.

Therefore a dimension-minimal counterexample with three nonunary rules requires each of those rules to read a descendant of itself. It contains three disjoint directed cycles, one through each exceptional vertex, notwithstanding the strong connectivity of the entire influence graph. This quotients the feedback structure to the nonunary kernel in every dimension.


#### Self-feedback forest closure with arbitrary nonunary Boolean functions

Let \(E\) be a nonempty set of directions and \(U=[n]\setminus E\). Assume:
1. Every rule on \(E\) depends **only** on bits in \(U\), and is antipodally odd in those bits; it may have arbitrarily many essential readers and need not be unary or affine.
2. Each direction \(u\in U\) has a unary rule \(c_u(x)=x_{p(u)}+\alpha_u\), with \(p(u)\in E\cup U\), and the induced dependency graph on U is acyclic.
3. For each \(e\in E\), the offsets \(\alpha_u\) of all unary children \(u\in U\) with \(p(u)=e\) agree whenever such children exist. Equivalently, there is a choice of frozen core bits \(\beta\in Q_E\) satisfying
\[
\boxed{\beta_{p(u)}=\alpha_u\quad\text{whenever }u\in U,\ p(u)\in E.}\tag{SF1}
\]

**Theorem (root-sign-coherent self-feedback closure).** Every coloring satisfying these conditions admits a color-zero full antipodal geodesic, in any dimension. No vertex-balance assumption is required. In particular, condition 3 always holds when every core direction has at most one unary child.

*Proof.* Freeze E at a choice \(\beta\) satisfying (SF1). The unary rules on U then admit a zero full U-geodesic \(P\), running from some y to \(\bar y\). Construct it in parent-first order on the acyclic U graph. A root unary direction with parent in E has its edge constantly zero by (SF1). When adding a unary child u whose parent j already appears in the developing word, insert u immediately before or after j according to the red-edge equation
\[
x_j+\alpha_u+[j\text{ precedes }u]=0.
\]
Choose its initial bit freely for the benefit of later children. Previous rules ignore the newly inserted bit, so their red edges are retained. Once all U directions are inserted, P is a zero full U-geodesic at frozen E-state \(\beta\).

For each \(e\in E\), let \(f_e(y)\) be the color of its edge at U-state y. Because these rules depend only on U and are odd, \(f_e(\bar y)=1+f_e(y)\) modulo two. Traverse before P every core direction e with \(f_e(y)=0\). Traverse after P every remaining core direction e, which has \(f_e(\bar y)=0\). No E-step changes U-bits, and the E-rule colors are independent of all E-bits, so these are all zero edges. Choose the starting E-bits so that their state throughout the middle U-path equals the prescribed \(\beta\); namely start with bit \(\beta_e+1\) if e precedes P, and \(\beta_e\) otherwise. Thus every U-edge of P retains color zero. Every direction is traversed once, and the endpoint is antipodal to the start. \(\square\)

**Corollary (unbounded, strongly connected feedback complexity is soluble).** For any odd \(k\ge3\), on directions \(E=\{a_1,\dots,a_k\}\), \(U=\{u_1,\dots,u_k\}\), put
\[
c_{u_i}(x)=x_{a_i},\qquad
c_{a_i}(x)=\bigoplus_{j=1}^k x_{u_j}.
\tag{SF2}
\]
This is a legal antipodally odd coloring with k nonunary rules. Its influence graph is strongly connected, and its directed feedback vertex number is k: there are k vertex-disjoint directed two-cycles \(a_i\to u_i\to a_i\), while deleting E leaves no cycle. Yet the theorem gives a zero full antipodal geodesic. Replacing the parity rules by **any** odd Boolean functions of U preserves the theorem; when each function essentially reads every U-bit the influence graph remains strongly connected. Thus neither arbitrarily large feedback vertex number nor strongly connected nonlinear feedback by itself provides a NORI1 obstruction.

This theorem admits directed feedback through E and hence strictly extends the prior no-feedback block construction. It does not cover unary children of one E direction with incompatible offsets, or exceptional rules that also read other exceptional bits. These are the remaining compatibility mechanisms to analyze.


#### Rootwise half-geodesic theorem for switched three-exception reader stars

Let n=4+2r, r>=1, with directions a,b,c,u and W=P disjoint-union N, |P|=|N|=r. Put chi=(-1)^x_a. Choose ANY odd signed function L of exterior bits with L(bar w)=-L(w), and ANY even bit function k with k(bar w)=k(w). Set signed color rules s_a=L, (s_b,s_c)=(chi,-L) if k=0 and (-L,chi) if k=1, s_u=-chi, s_i=chi for i in P and s_i=-chi for i in N. The rules are independent of their own bits, antipodally odd and balanced. Up to three rules can be nonunary.

THEOREM. A zero full antipodal geodesic starts from root with a-bit t and W-state w if and only if L(w*)=+1, where w*=w xor P if t=0 and w*=w xor N if t=1. Consequently half of all roots are successful, independent of the nonlinear selector k. This closes the entire all-dimensions switched singleton-reader fringe class.

Proof of necessity: all P-directions have signed color chi and must occur while a=0; all N-directions and u have signed color -chi and must occur while a=1. Since a occurs once, at the a-step W must equal w*; hence its edge requires L(w*)=+1.

Proof of sufficiency when t=0: place P before a and N,u after a. If L(w)=-1, then at the starting root chi=+1 and -L=+1, so both b and c are red; traverse them first, then P,a,N,u. If L(w)=+1, traverse first whichever of b,c is assigned signed color chi under k(w), then P,a,N. At the final exterior state bar w, oddness gives L(bar w)=-1 and evenness preserves k, so the other exceptional edge has signed color -L=+1; traverse it, then u. In both cases the a-step is red because L(w*)=+1.

When t=1: place u,N before a, P after a. If L(w)=+1, then at the final exterior state bar w, L=-1 and chi=+1, so both b and c are red; place them after u,N,a,P. If L(w)=-1, first traverse whichever exceptional edge has signed color -L=+1; then u,N,a,P; at bar w oddness gives L=+1 and evenness preserves k, so the other exceptional edge, assigned chi=+1, is red and can be traversed last. All directions are used once, and all used edges have color zero. The root characterization is necessary and sufficient. As L is odd, it is positive on half the exterior states, giving half the roots.

Independent finite audit: all 256 odd L functions and all 256 even k functions on four exterior bits (65,536 Q8 colorings) obey the predicted root count 16 of 32 compressed root states; a separate program checked the rootwise equivalence in full Q8 on randomized functions. The theorem includes balanced three-nonlinear colorings for which every frozen four-face on a,b,c,u lacks a monochromatic full geodesic. Its mechanism is an antipodal endpoint transport, with L reversing and k preserved.

##### Complementary-root fork is mandatory when the nonunary kernel reads only unary bits

**Corollary (necessary opposing-child fork).** Let c be a minimum-dimensional NORI1 counterexample. Let E be its nonunary directions and U its unary directions. Assume every E-rule disregards every E-bit, so the E-rules are arbitrary odd functions solely of U. Then some exceptional direction e has two distinct unary children u,v reading e with opposite offsets:
\[
\boxed{c_u=x_e+\alpha,\qquad c_v=x_e+\alpha+1.}\tag{SF3}
\]
The two children thus have pointwise complementary incident edge colors. Each lies on a directed dependency path leading back into the exceptional kernel E.

*Proof.* Minimum-dimensional badness forces D(c) to be strongly connected, and the induced graph on U to be acyclic. Each U rule is unary. If all children of every e∈E had equal offsets, including when there are zero or one children, the root-sign-coherent self-feedback closure theorem would produce a zero full antipodal geodesic, contradicting badness. Therefore two children reading one e must have opposite offsets. Strong connectivity gives a directed path from each of these unary vertices to some member of E, establishing the feedback-fork assertion. \(\square\)

This locates a specific pointwise complementary unary fork in any hypothetical minimum bad coloring whose nonunary rules do not read each other's bits. The remaining all-dimensional proof obstacle is to absorb such opposing forks without requiring a common frozen core state; arbitrarily many and arbitrarily complicated nonunary rules are allowed.


#### Complete three-nonlinear single-reader-star closure via exterior antipodal transport

THEOREM (uniform NORI1 closure of the balanced three-nonunary single-reader-star branch). Let c be a balanced antipodally odd edge coloring of Q_n, n even. Suppose its only nonunary directions are a,b,c, the signed exceptional sum is s_a+s_b+s_c=chi_a where chi_a=(-1)^x_a, and EVERY other unary direction reads bit a (its signed rule is either chi_a or -chi_a). Then c admits a monochromatic full antipodal geodesic, without any restriction on dimension or on the nonlinear dependence of its three exceptional rules.

Proof. Balance forces the unary signed-rule sum to -chi_a. Designate one unary direction u whose signed rule is -chi_a, and pair all remaining unary rules with opposite signs: W=P disjoint union N, with |P|=|N|, signed rules s_i=chi_a on P and s_i=-chi_a on N. Put T={a,b,c,u}.

DICHOTOMY: If some four-face retaining T, with all W bits frozen at w, has a zero full antipodal T-geodesic, extend it to Q_n. Place each W-direction whose sign chi_a or -chi_a is positive at the T-path starting a-bit before the entire T-path; put every other W-direction after the entire T-path. Because a is traversed once within T, those opposite signs are then positive. Choose the initial W-bits to give the specified frozen state w throughout the T block. No inserted step changes any T-direction color, and all inserted unary edges have sign +1. Therefore a full zero geodesic exists.

Otherwise EVERY frozen T-four-face lacks a zero full geodesic. At a fixed W-state and either fixed u-bit, the exceptional signed rules (s_a,s_b,s_c), as functions of a,b,c, satisfy s_a+s_b+s_c=chi_a and each ignores its own bit. A real mixed-difference argument gives precisely eight possible triples:
T0=(-1,chi_a,+1), T1=(-1,+1,chi_a), T2=(chi_c,-chi_c,chi_a), T3=(chi_b,chi_a,-chi_b), T4=(-chi_b,chi_a,chi_b), T5=(-chi_c,chi_c,chi_a), T6=(+1,-1,chi_a), T7=(+1,chi_a,-1).
For the two u-layers of the frozen T-face, direct four-dimensional exhaustive root-and-order checking (16 roots times 24 orders per type pair) establishes that if either layer is of type T2,T3,T4,T5, a zero full four-face geodesic exists, regardless of the other layer. Because every frozen face is assumed unsuccessful, every layer at every W-state must belong to corner types T0,T1,T6,T7.

Consequently s_a is independent of b,c globally. Define lambda(z)=s_a at z=(u,W), independent also of a. By antipodal oddness lambda(bar z)=-lambda(z). In all four corner types the other exceptional rules equal chi_a and -lambda(z) in some order. Define k(z)=0 if (s_b,s_c)=(chi_a,-lambda) and k(z)=1 for the reverse order. The two assignments are distinct as functions of a, so k is well defined. Because both chi_a and lambda change sign under antipodal translation, while s_b,s_c also change sign, k(bar z)=k(z). Thus lambda is an arbitrary odd sign and k an arbitrary even selector on z=(u,W).

It remains to give a full zero geodesic. Let t be the starting a-bit and z the starting (u,W)-state. If t=0, put every P-direction before a and every N-direction and u after a; at a the z-state is z*=z xor P. If t=1, put u and every N-direction before a and every P-direction after a; at a the state is z*=z xor (N union {u}). Choose a starting z for which lambda(z*)=+1. Such choices exist (indeed half of z), because lambda is odd.

Place b,c as follows. When t=0, if lambda(z)=-1 then both b,c are positive at the start (chi_a=+1 and -lambda=+1), so traverse both before P. If lambda(z)=+1, traverse first the one of b,c carrying chi_a. At the final z-state bar z, antipodal oddness gives lambda=-1 and evenness gives k(bar z)=k(z); after a the OTHER exceptional direction carries -lambda=+1 and may be traversed at the end. When t=1, if lambda(z)=+1, both b,c are positive at the end since lambda(bar z)=-1 and chi_a=+1 after a. If lambda(z)=-1, traverse first the exceptional member carrying -lambda=+1; at the end lambda(bar z)=+1 and k is unchanged, so the other exceptional member carries chi_a=+1. In every case, the a-edge is positive by lambda(z*)=+1, and every unary edge is positive by its placement. This constructs a zero full antipodal geodesic, contrary to the assumption that the frozen four-faces failed globally.

Thus either outcome of the dichotomy supplies a full zero geodesic. This proves the claimed all-dimensional closure. The proof makes exterior antipodal transport essential precisely when ALL frozen four-faces fail, overcoming the frozen-core obstruction seen in the Q8 example.

ROOTWISE STRENGTHENING IN THE SECOND CASE. If no frozen T-face contains a zero full T-geodesic, then from any root the zero full geodesic exists if and only if lambda(z*)=+1. Necessity follows because every unary rule constrains its step to one side of a; the value z* at the a-step is forced. Sufficiency was proved constructively. Hence half of all cube roots admit a zero full antipodal geodesic in this case. The local-type enumeration was independently checked in all 64 ordered layer pairs, with precisely twelve frozen four-face failures.

##### Analytic mobile-type closure certificates
For mobile types T2,T3,T4,T5, the following exceptional three-direction red paths have starting a-bit zero: T2 root 4 order (b,c,a), T3 root 2 order (c,b,a), T4 root 0 order (c,b,a), T5 root 0 order (b,c,a), with little-endian vertex bits (a,b,c). In every case the final a-bit is one, so appending the unmatched unary u-edge with signed rule -chi_a gives a red full four-direction geodesic, independently of the other u-layer. Thus the analytic eight-type classification and these four certificates suffice for the full dimension-uniform three-nonlinear reader-star closure. Finite enumeration is only an independent audit.

##### Simplified deletion proof for the three-exception reader-star closure
If some frozen T={a,b,c,u} face has a red full geodesic, all exterior unary directions reading a can be inserted outside the four-step core by placing each where its signed singleton character is positive. If every frozen T-face fails, the local eight-type classification and the four analytic mobile-type certificates show that all exceptional rules globally ignore b and c. All other unary rules read only a, so b and c are independent reader-extension directions. Delete both: the remaining antipodally odd cube has at most one nonunary rule. The existing one-exception theorem gives a red full geodesic there, and the free-reader extension lemma inserts b and c before or after that path, according to their antipodally opposite endpoint colors. Thus the entire reader-star branch closes alternatively without the new endpoint-transport count. The half-root theorem still gives a stronger characterization of every root in the all-frozen-failure subcase.

#### Balanced feedback branching for independent nonunary direction rules

Let c be a vertex-balanced antipodally odd coloring of Q_n with strongly connected direction-influence graph D. Let E be the nonempty set of nonunary directions and U the set of unary directions. Assume every E-rule ignores every E-bit, but may depend on arbitrarily many U-bits. The earlier unary-cycle lemma makes D[U] acyclic, and the parent map of unary directions partitions U into forests rooted in E. Put \(R=\bigcup_{e\in E}\operatorname{Read}(c_e)\subseteq U\).

**Theorem (two external readers per exceptional root).** Each e∈E has at least two immediate unary children of opposite signed colors. Each child branch contains a vertex of R, so
\[
\boxed{|R\cap\rho^{-1}(e)|\ge2\quad(e\in E),\qquad |R|\ge2|E|.}\tag{BR1}
\]
Here rho(u) is the unique E-root reached by repeatedly following the reader parent of u. Furthermore, any unary vertex u∉R that has at least one unary child has at least two unary children of opposite signs.

*Proof.* Put \(s_i=(-1)^{c_i}\), \(\chi_j=(-1)^{x_j}\). Balance gives \(\sum_i s_i=0\). Since each exceptional rule disregards all E-bits, its singleton Walsh coefficient at e∈E is zero. Each unary rule reading e contributes +chi_e or -chi_e, so the number of children of e carrying each sign agrees. Strong connectivity gives an outgoing influence edge from e. No E-rule reads e, so this edge leads to a unary child; hence e has at least two children with opposite signed rules.

For each child u of e, strong connectivity gives a directed path to E. Stop at its first entry into E. Every earlier vertex lies in the descendant subtree of u because unary directions each receive one incoming reader arc. The last unary vertex j of this path is an essential reader of some E-rule and belongs to R. Branches rooted at distinct children are disjoint. Thus each e has at least two R-bits in its rooted unary tree, and different E roots have disjoint trees, proving (BR1).

If u∈U\R, every exceptional rule disregards u, so its singleton Walsh coefficient at u vanishes. The signed unary children reading u must sum to zero by balance. Therefore if any child is present, at least two children of opposite sign are present. \(\square\)

**Corollary (cubic minimal-influence configuration cannot be strongly connected).** No strongly connected balanced antipodally odd coloring with precisely three nonunary rules has \(M(c)=n+6\). The previously proved cubic cancellation theorem shows that in this influence class all three E-rules share a single three-element reader set R disjoint from E. The branching theorem forces \(|R|\ge2|E|=6\), a contradiction.

If a counterexample of least dimension among ALL legal NORI1 colorings happens to be vertex-balanced, then \(M(c)\ge n+7\): the minimal-counterexample SCC reduction forces strong connectivity, the first two nonunary cases have been closed, and the above corollary excludes the equality \(M=n+6\) at three nonunary rules. This is deliberately not claimed as a lower bound for arbitrary balanced counterexamples, whose influence graphs may be reducible.

The theorem reveals a balance-forced bifurcation of every nonunary feedback root, followed by reconvergence into E via its disjoint unary descendant branches. It applies with arbitrarily many nonlinear rules and arbitrarily large feedback vertex number.


##### Antipodal edge-orbit Hamming scaling in paired lifts

For legal colorings \(c,d\) of the same cube \(Q_m\), define \(d_{\mathrm{orb}}(c,d)\) as the number of antipodal edge orbits \(\{e,\bar e\}\) on which their binary edge colors differ. This is the Hamming metric on the independent legal-coloring variables.

**Theorem (paired lift as a repetition embedding).** Let \(B(c)\) be the standard balanced complementary paired lift of a legal coloring \(c\) of \(Q_m\), \(m\ge2\), defined by
\[
B(c)_i(x,y)=c_i(x),\qquad
B(c)_{m+i}(x,y)=1\oplus c_i(x),\qquad 1\le i\le m.
\]
Then for any legal \(c,d\),
\[
\boxed{d_{\mathrm{orb}}(B(c),B(d))=2^{m+1}d_{\mathrm{orb}}(c,d).}\tag{HE1}
\]

*Proof.* Fix a base edge orbit \(\{e,\bar e\}\) of direction \(i\). Changing its base color variable changes the lifted original-direction edges over every spectator vector \(y\in Q_m\). These form \(2^m\) distinct antipodal edge orbits (each consists of the edge \(e\) over \(y\) paired with \(\bar e\) over \(\bar y\)). In the complementary dummy direction \(m+i\), the change occurs at the four distinct base vertices incident with \(e,\bar e\), for each of the \(2^{m-1}\) choices of the other spectator bits. Thus the \(4\cdot2^{m-1}\) changed dummy edges form another \(2^m\) antipodal edge orbits. Dummy directions differ from original directions, so these classes are disjoint. Distinct base edge orbits control disjoint lifted original and dummy edge-orbit variables, so the contributions sum without overlap. This gives (HE1). \(\square\)

**Corollary (balanced lifts admit exponentially many orbit-disjoint certificates).** If \(c\) has a monochromatic full antipodal geodesic, then \(B(c)\) has at least \(2^{m-1}\) monochromatic full geodesics of the same color whose antipodal edge-orbit supports are pairwise disjoint. Consequently any legal coloring differing from \(B(c)\) in fewer than \(2^{m-1}\) edge orbits still has a monochromatic full geodesic.

*Proof.* Apply the spectator parity-code packing theorem in the Cartesian-factorization Subsection to the \(m\) dummy directions of \(B(c)\). At most one path in the orbit-disjoint family can be destroyed by changing any single edge-pair variable. \(\square\)

Combining (HE1) with the rooted metric identity \(D_\varepsilon(B(c);(x,y))=D_\varepsilon(c;x)+m\), balanced lifting preserves every original detour while multiplying coloring-space Hamming distances by \(2^{m+1}\). This separates the reachability metric from the edge-variable geometry of counterexample-preserving lifts.


#### Eulerian ice orientations, paired directed squares and antipodal square-flip calculus

For a legal antipodally odd perfectly balanced coloring c on Q_(2m), let p(v)=Hamming parity(v). Orient every red edge even->odd and every blue edge odd->even. Then outdegree(v)=indegree(v)=m. Every directed walk alternates colors. Since antipodal complementation preserves vertex parity but changes edge color, it reverses every arrow: u->v iff bar(v)->bar(u). Conversely any Eulerian orientation of Q_(2m) with this antipodal arrow-reversing symmetry produces a unique balanced legal coloring by coloring even->odd arrows red and odd->even arrows blue.

At any vertex of rank k relative to an arbitrary root, let a be the number of directed edges upward to rank k+1 and b the number entering from rank k-1. Eulerian degree gives a-b=m-k, since outgoing downward edges are k-b. Thus greedy increasing directed paths from every root continue at least to rank m+1 (at rank m, a=b>=1 if reached).

For the standard complementary paired lift C on Q_(2d), its direction pairs (i,d+i) have complementary rules c_i(x) and 1-c_i(x), both invariant on flips of these two bits. Every such two-face is a directed red-blue 4-cycle in the canonical orientation, and these faces partition every cube edge. From any root, traverse each direction pair in either its currently outward-first order followed by its mate. Both steps are directed; any permutation of the d pairs gives a directed full antipodal geodesic. Hence there are at least d! rooted directed full antipodal geodesics, all alternating red-blue.

NORI1 asks for a monochromatic full antipodal geodesic, which corresponds instead to a zigzag path: successive edges alternate between traversing with and against the canonical arrows. Directed Euler tours alternate colors and do NOT directly provide the desired zigzag.

If 4 divides the cube dimension N, each monochromatic subgraph is regular of even degree N/2. Orient each red component by an Euler circuit; obtain blue orientations by taking antipodal reversed images. Then every vertex has N/4 incoming and N/4 outgoing edges of each color, and antipodality still reverses arrows. For N=2 mod 4, no orientation balances incoming and outgoing degrees separately within either color because the monochromatic degree N/2 is odd.

Theorem of Levit, Chandran, Cheriyan (Operations Research Letters 46 (2018), 553-556): every Eulerian orientation of Q_(2m) is strongly m-vertex-connected. This supplies abundant alternating directed paths but, without a new zigzag-selection principle, not a monochromatic full geodesic.

### Forced directed-square circulation in every balanced cube

Let c be a two-color edge coloring of Q_N, N even, with N/2 edges of each color incident at every vertex. For a square face, count its cyclic color switches. That count is 0, 2, or 4. Let A_0,A_2,A_4 denote the numbers of faces of each type. A_0 is the number of monochromatic squares; A_4 counts squares with alternating boundary colors. Under the canonical Eulerian orientation (red even->odd, blue odd->even), the A_4 squares are precisely the directed 4-cycles.

**Theorem (square-switch excess identity).**
\[
\boxed{A_4-A_0=N\,2^{N-3}.}
\tag{EO1}
\]
In particular there are at least N*2^(N-3) directed squares, even without antipodal oddness.

*Proof.* At every vertex, the number of unordered pairs of incident edges with different colors is (N/2)^2. Such a pair lies in a unique 2-face. Counting bichromatic turns by vertex and by face gives
\[
4A_4+2A_2 = 2^N(N/2)^2.
\]
The total number of faces is A_0+A_2+A_4=binom(N,2)2^(N-2). Subtract twice this equation from the turn equation to obtain 2(A_4-A_0)=N2^(N-2), proving (EO1). \(\square\)

More generally, for any binary coloring with red degrees r(v), not necessarily balanced,
\[
\boxed{A_4-A_0=\tfrac12\sum_v r(v)(N-r(v))-\binom N2 2^{N-2}.}
\tag{EO2}
\]
This follows by the same count and recovers (EO1) at r(v)=N/2.

**Corollary (antipodal square swaps).** Suppose in addition c is antipodally odd and N>=4. The antipodal image of every directed square is a distinct directed square, giving at least N2^(N-4) antipodal pairs. Choose any such pair, and reverse the colors of all eight edges in its two disjoint faces. The resulting edge coloring remains vertex-balanced and antipodally odd; equivalently, the canonical Eulerian digraph undergoes simultaneous reversal of the two directed 4-cycles.

*Proof.* At each vertex of an alternating-colored square one red and one blue incident face edge are toggled, leaving its red and blue degrees unchanged. The opposite face is vertex-disjoint for N>=4, and toggling both antipodal edge orbits preserves the relation c(tau e)=1-c(e). In the canonical orientation toggling the color of an edge reverses its arrow, so the directed cycles are reversed. The lower bound on pairs is half that in (EO1). \(\square\)

**Corollary (square account for the paired balanced lift).** If C is the standard complementary paired lift of a legal Q_m coloring to Q_(2m), every 2-face spanned by a paired original/dummy direction is a directed square. There are m*2^(2m-2) such faces, precisely the universal lower bound in (EO1). Hence
\[
\boxed{\#\text{directed squares outside the paired faces}
=\#\text{monochromatic squares}.}
\tag{EO3}
\]
The paired directed squares are edge-disjoint and cover every cube edge.

*Proof.* Both rules in a pair are complementary and ignore the two paired bits. Their face boundary alternates red and blue. Every edge belongs to its unique pair-face. Since the number of these faces is (2m)2^(2m-3), subtract them from (EO1) to obtain (EO3). \(\square\)

**Computational check.** Exhaustive enumeration of antipodally odd, vertex-balanced Q_4 colorings gives 48 colorings. Each has A_4=10 and A_0=2, satisfying (EO1). The graph generated by simultaneous antipodal directed-square flips is connected and 5-regular on these 48 colorings. These finite enumerations are checks and do not assert any general connectivity of the square-flip graph.

This furnishes a dimension-uniform supply of local, antipodally symmetric Eulerian-preserving exchanges. The limitation for NORI1 is that square flips change the coloring, and need not preserve a preselected monochromatic geodesic or counterexample status. Any extremal argument using them must control that change rather than assume invariance.

##### An explicit two-orbit geodesic gate defeats the universal factor-four packing threshold

For a legal successful coloring \(c\) of \(Q_m\), let \(\tau_{\rm geo}(c)\) be the smallest number of antipodal edge-pair orbits that meet every **red** full antipodal geodesic. By antipodal translation, a set of edge orbits meets all red full geodesics if and only if it meets all blue full geodesics; thus \(\tau_{\rm geo}(c)\) is a color-independent geodesic hitting number. Let \(p(c)\) be the maximum size of a family of full monochromatic antipodal geodesics (of either color) whose edge-orbit supports are pairwise disjoint.

**Proposition (lifted geodesic-transversal upper bound).** For the complementary paired lift \(B(c)\) on \(Q_{2m}\),
\[
\boxed{p(B(c))\le\tau_{\rm geo}(c)\,2^m.}\tag{GATE1}
\]
More generally, for an extension by \(k\) spectator directions whose rules depend only on the \(m\) original bits, the corresponding packing number is at most \(\tau_{\rm geo}(c)\,2^k\).

*Proof.* Choose \(\tau_{\rm geo}(c)\) base edge-pair orbits meeting every red full geodesic. Every red full geodesic in the spectator extension projects to a red full geodesic in the base cube: each original direction is traversed precisely once, and all original edge colors ignore the spectator bits. Consequently it traverses one original-direction lifted edge over one of the chosen base edge-pair orbits. Each chosen base orbit contributes precisely \(2^k\) distinct antipodal edge-pair orbits in the original directions of the extension, one for every spectator vector at a chosen representative red edge. These form an orbit-transversal meeting every red full geodesic in the extension. Antipodal translation maps all blue full geodesics to red ones without changing their edge-orbit supports; hence the same transversal meets all monochromatic geodesics. A family with pairwise disjoint orbit supports uses distinct members of this transversal, so its size is at most \(\tau_{\rm geo}(c)2^k\). Apply \(k=m\) to \(B(c)\). \(\square\)

**Theorem (four-dimensional obstruction to the factor-four closure premise).** On \(Q_4\), with directions indexed \(0,1,2,3\), consider the legal affine coloring
\[
\boxed{c_0(x)=1\oplus x_2,\quad c_1(x)=x_3,\quad c_2(x)=x_3,\quad c_3(x)=x_2.}\tag{GATE2}
\]
It admits red full antipodal geodesics but satisfies
\[
\boxed{\tau_{\rm geo}(c)=2,\qquad p(B(c))\le 32=2^{4+1}.}\tag{GATE3}
\]
Thus the universally quantified strengthening \(p(B(c))>2^{m+1}\) for all successful legal \(Q_m\) colorings with \(m\ge4\), previously identified as *sufficient* for NORI1, is already **false in dimension four**. The conditional implication remains valid, but its hypothesis is not.

*Proof.* All rules in (GATE2) ignore their own bits and contain one foreign direction with coefficient one, hence are undirected edge rules and flip under global antipodal complementation. At the root \((x_0,x_1,x_2,x_3)=(0,0,1,0)\), the direction order \((0,1,2,3)\) traverses four red edges and ends at its antipode.

On any red full geodesic, a direction-\(2\) step is red only while \(x_3=0\), and a direction-\(3\) step is red only while \(x_2=0\). Since these two directions are each flipped once, their initial pair must be either \((x_2,x_3)=(1,0)\), with the \(2\)-step before the \(3\)-step, or \((0,1)\), with the \(3\)-step before the \(2\)-step. In the first case, the state \((x_2,x_3)=(1,0)\) occurs only before the \(2\)-step; in the second it occurs only after the \(2\)-step. Since the direction-\(0\) edge is red precisely when \(x_2=1\), **every red full geodesic crosses direction \(0\) at \(x_2=1,x_3=0\)**. There are only two possible undirected red direction-\(0\) edges with these fixed directions, according to \(x_1=0\) or \(1\). These are the edges with integer-mask endpoints \(\{4,5\}\) and \(\{6,7\}\), with antipodal mates \(\{10,11\}\) and \(\{8,9\}\). Therefore \(\tau_{\rm geo}(c)\le2\).

There are two orbit-disjoint red full geodesics with the common direction order \((0,1,2,3)\), rooted respectively at \((0,0,1,0)\) and \((1,1,1,0)\). Their traversed edges have distinct antipodal edge-pair orbits: the paths differ in both spectator bits \(x_0,x_1\), while their common original two-direction path uses directions \(2,3\). Thus no single orbit meets both, so \(\tau_{\rm geo}(c)\ge2\). Hence \(\tau_{\rm geo}(c)=2\). Proposition (GATE1) with \(m=4\) gives \(p(B(c))\le 2\cdot 16=32\). \(\square\)

**Interpretation.** This example is successful and has multiple orbit-disjoint monochromatic geodesics, but all of them cross one of two prescribed edge-pair orbits. The paired lift makes the coloring perfectly vertex-balanced and amplifies the two-orbit gate to a transversal of size only \(2^{m+1}\). Consequently the earlier factor-four packing target is not an appropriate universal closure premise, even though its implication to NORI1 was logically correct. The example constrains the deterministic exchange program: an argument must exploit path geometry beyond the number of orbit-disjoint full geodesics in a balanced paired lift.


##### Balanced monochromatic components are bridgeless; Eulerian orientations and robust antipodal reachability

**Proposition (balanced two-route theorem).** Let \(c\) be any antipodally odd vertex-balanced coloring of \(Q_{2d}\), with \(d\ge2\): every cube vertex is incident with precisely \(d\) red and \(d\) blue edges. Then both monochromatic spanning graphs are \(d\)-regular and bipartite, and every connected component is bridgeless. Hence for any two vertices \(u,v\) connected by a red (respectively blue) path, there exist at least two *edge-disjoint* red (respectively blue) paths between them. In particular, every root supporting a monochromatic antipodal path has two edge-disjoint such paths of **each** color. Moreover, after changing the colors of any one antipodal edge pair, every previously existing monochromatic antipodal root remains connected to its antipode in both original colors, although the shortest path lengths and geodesic status may change.

*Proof.* The cube is bipartite by Hamming-weight parity, and vertex balance makes each color graph \(d\)-regular. Let \(S\) be one side of a proposed bridge in a monochromatic connected component, with \(a\) even-parity and \(b\) odd-parity vertices. Counting incident monochromatic edges from each parity class gives
\[
d(a-b)=|\partial_R S\cap\{\text{even endpoint in }S\}|-
|\partial_R S\cap\{\text{odd endpoint in }S\}|.
\]
If \(\partial_R S\) were a single edge, the right side would be \(+1\) or \(-1\), impossible for \(d\ge2\). Thus there are no bridges. For any two distinct vertices of a connected bridgeless graph, every separating edge cut has size at least two, so the edge version of Menger's theorem supplies two edge-disjoint paths. Antipodal reflection and reversal transform red paths between a fixed root and its antipode into blue paths with the same endpoints, establishing both-color certification.

A single legal edge-orbit flip removes at most one red edge (the originally red edge of the orbit) and adds its antipodal mate as red; analogously for blue. Since neither monochromatic graph has bridges, deleting that one edge does not destroy any monochromatic connectivity relation. Thus all existing antipodal root connections persist in their original colors. \(\square\)

**Corollary (antipodally compatible Eulerian orientations when \(4\mid n\)).** For a vertex-balanced legal coloring of \(Q_{4k}\), each monochromatic component is Eulerian with all degrees \(2k\). One may orient every red component along Euler tours, producing a directed red graph with in-degree and out-degree \(k\) at every vertex and strong connectivity inside each component. Orient each blue edge by reversing the orientation of its red antipodal mate. Then the blue graph is also Eulerian, strongly connected on each component, and has in-degree and out-degree \(k\) at every vertex; the antipodal involution exchanges red and blue edges while reversing orientations. Splitting each original vertex into independent red and blue states yields two families of directed Eulerian monochromatic circuits, with no need for nonlinear assumptions.

*Proof.* Every even-regular connected graph admits an Euler tour, and directing its edges along an Euler tour gives equal in/out degrees and a strongly connected digraph. Antipodal translation is a graph isomorphism between the red and blue subgraphs. Reversing the transported red orientation preserves strong connectivity and the equal in/out counts. \(\square\)

**Essential limitation.** The two-route theorem concerns *arbitrary-length monochromatic paths*, not full direction-simple antipodal geodesics. A red graph can be bridgeless while every red full geodesic crosses a small set of edge orbits, as illustrated by the explicit gate (GATE2). Consequently Eulerian orientation and cycle bypass are not by themselves a proof of NORI1; any successful cycle-exchange potential must quantitatively control repeated direction directions.


#### Signed edge orders, antipodal greedy commutators, and balanced circulation

THEOREM (signed-rank greedy antipodal obstruction). In an antipodally odd binary edge coloring of Q_n, for each direction i let R_i swap its red i-edges and fix all blue i-edges, and let B_i swap its blue i-edges and fix red i-edges. These permutations are involutions, and antipodal translation P obeys B_i=P R_i P. Fix any ranking pi=(i_1,...,i_n) of the directions, and assign blue edges signed rank -rank_pi(i) and red edges signed rank +rank_pi(i). Scan the ranks increasingly, at every rank traversing the incident edge if it has the indicated color, and otherwise remaining stationary. Put F_pi=R_(i_n)...R_(i_1). Because the blue scan has direction order i_n,...,i_1 and the red scan has direction order i_1,...,i_n, the resulting full greedy scan H_pi satisfies H_pi=F_pi P F_pi^(-1)P. Consequently H_pi P=F_pi P F_pi^(-1), a conjugate of the fixed-point-free antipodal permutation. Thus H_pi(x) never equals bar x for any root and any pi. The result needs antipodal oddness only, with no balance assumption. It forbids the mandatory greedy rank scan, and does not preclude non-greedy increasing full geodesics.

THEOREM (balanced affine obstruction to a preassigned signed direction order). On Q4, with binary bits indexed 0,...,3, put c_0=x_1, c_1=x_0, c_2=1-x_0, c_3=1-x_1. Each rule ignores its own bit, changes under antipodal inversion, and their sum equals two at each vertex, giving vertex balance. Fix direction rank 0<1<2<3. No full direction-simple geodesic has increasing signed edge ranks (blue indices descending, then red indices ascending). Proof: direction 2 comes before direction 0 if and only if its color is blue, since it has the greater rank. Its rule 1-x_0 forces the starting x_0 to be zero in either case (blue before direction 0 requires x_0=0; red afterward reads the flipped x_0 and likewise requires starting x_0=0). Direction 3 relative to direction 1 similarly forces starting x_1=0. Direction 0 reads x_1, so it is blue precisely when it follows direction 1, and red when it precedes direction 1. In the signed increasing schedule, this forces directions 0 and 1 to share a color. If both are blue, direction 1 precedes 0 and reads x_0=0, contradicting its blue status; if both are red, direction 0 precedes 1 and direction 1 reads x_0=1, contradicting red. Thus no full signed-increasing geodesic exists. Renaming directions furnishes a counterexample to every predetermined ranking, even among balanced antipodally odd colorings.

COROLLARY (linear loss for a fixed ranking). The h-fold independent Cartesian product of the Q4 example has dimension 4h and is balanced and antipodally odd. Order each four-direction factor as above, with arbitrary interleaving of the factor ranks. Any strictly signed-increasing direction-simple path restricts to a signed-increasing path in every factor. It can traverse at most three of that factor's four directions, so its total length is at most 3h. The cube nonetheless has monochromatic full geodesics; it is the imposed rank ordering that creates a linear deficiency.

THEOREM (balanced colors form a signed circulation). For any balanced two-coloring of Q_(2m), orient each edge temporarily from its even-parity endpoint to its odd-parity endpoint, with coefficient s_e=+1 for red and -1 for blue. Balance makes the incidence divergence zero at every vertex. Discrete summation by parts therefore gives, for every real height function f on vertices,
sum_(e even->odd) s_e[f(odd(e))-f(even(e))]=0.
Thus no strict height can increase across all red even-to-odd edges and decrease across all blue even-to-odd edges, since that would make every summand positive. Orienting red edges even-to-odd and blue edges odd-to-even gives an Eulerian orientation, which necessarily contains directed cycles. For even dimensions, antipodal oddness reverses that Eulerian orientation. Thus local balance provides a divergence-free current rather than a gradient of a globally monotone potential.

Together these results distinguish three hypotheses: a two-level edge ranking encodes at most one color switch; a strict prescribed within-color ranking may forbid full paths; and a deterministic greedy scan has an algebraic antipodal obstruction. An effective edge-order route must retain non-greedy choice of steps and control repeated directions.

UNIVERSAL EXPECTATION IDENTITY. For any order pi and uniform starting root X, let T_pi(X) count the traversed edges of the full greedy signed-rank scan. Antipodal oddness makes half the edges in every direction red and half blue. Each partial greedy sweep permutes the cube vertices and therefore preserves the uniform distribution. Each of the 2n signed slots moves with probability 1/2, so E[T_pi]=n. If M0 is the number of omitted directions and M2 the number traversed twice, then T_pi=n+M2-M0. Consequently E[M0]=E[M2]. The proved antipodal commutator identity prevents traversing all n directions once, so M0+M2>=1 for every starting vertex. Hence E[M0]=E[M2]>=1/2, in every dimension and for every antipodally odd coloring, independent of balance. Thus the greedy rank scan has mean length n while necessarily producing direction omissions or repetitions.

SHARP PRODUCT EXAMPLE. In the affine balanced Q4 coloring of the preceding theorem, strict increasing signed-rank paths with no direction repeated have maximum length three under pi=(0,1,2,3). For example, root 0 allows blue direction 3, then blue direction 2, then red direction 0. Exhaustive checking of the 16 roots and subsets of the four directions confirms that no length-four path exists, independently also proved analytically above. Taking h independent Cartesian copies and preserving the rank order 0<1<2<3 within each factor gives a longest strictly signed-increasing direction-simple path of length 3h in Q_(4h). The lower bound follows by concatenating factor paths with all blue portions before all red portions; the upper bound follows by projecting any candidate into its independent factors. This is a linear loss despite balance, antipodal oddness and existing monochromatic full geodesics.

INTERPRETATION. Ordering all blue edges before red edges makes every increasing path have at most one color switch. Giving each direction one rank in each color adds a partial direction-use condition, but cannot prevent traversal of the same direction once in each color. The greedy scan is obstructed algebraically, and the fixed within-color ranking is obstructed by the balanced affine family. An edge-order approach to NORI1 therefore needs nongreedy choices, adaptive rankings and a separate mechanism preventing direction repetition.

#### Edge-ordered monotone trails and full-geodesic threshold

For a legal antipodally odd binary edge coloring c of Q_n and any direction permutation pi, order all cube edges with zero-colored edges first, grouped by direction in pi order, followed by one-colored edges grouped by direction in pi order; break ties within groups arbitrarily. Denote this order phi_pi. Let T(c) be the maximum increasing edge TRAIL length over choices of pi. A trail may revisit vertices but cannot reuse an edge.

THEOREM. Each phi_pi-increasing trail is a zero-star-one-star walk, and each single-color phase is a direction-simple cube path. Indeed, all edges in any fixed (binary color, cube direction) class form a matching and occur in one interval of the total order. Two such edges cannot be consecutive in a trail; hence a trail can take at most one edge in each class. Each color phase thus has length at most n and is a monochromatic cube geodesic. In particular T(c)<=2n, and a trail of length 2n-k contains in each color phase a monochromatic direction-simple path of length at least n-k.

The condition T(c)=2n is equivalent to the existence of a monochromatic full antipodal geodesic. A 2n-long increasing trail has a zero phase of n steps, hence a zero full geodesic. Conversely take a zero full antipodal geodesic from x to bar x using directions in order pi. Antipodal translation produces a one-colored full geodesic from bar x to x traversing the same directions in order pi. Concatenate the zero path and the one path. They share no edge because all first-path edges have color zero and all second-path edges have color one. The concatenation is a 2n-long phi_pi-increasing trail. If the original geodesic is one-colored, antipodally translate it first.

If c is bad for NORI1, its longest monochromatic direction-simple path has length <=n-2: a monochromatic path of length n-1 missing direction i has its two endpoint i-edges antipodal and oppositely colored, so one endpoint permits extending to length n. Therefore every phi_pi-increasing trail has length <=2n-4 in a hypothetical NORI1 counterexample. A general guarantee T(c)>=2n-3 would suffice to prove NORI1.

The Graham-Kleitman increasing-trail theorem provides a trail of length >= average degree n of Q_n for EVERY edge ordering. Applied to phi_pi it yields only a monochromatic direction-simple path of length >=n/2, far below the near-2n trail length required by sublinear-defect amplification. The 2020 Bucić-Kwan-Pokrovskiy-Sudakov-Tran-Wagner result N^(1-o(1)) is for edge-ordered complete graph K_N; neither the graph density nor the additive near-spanning scale match this cube reduction. The 2016 De Silva-Molla-Pfender-Retter-Tait bound f(Q_n)>=n/log n is for increasing vertex-simple paths under arbitrary edge orderings. A successful theorem in the current setup must exploit its special two-color grouping and antipodal relations, or add rainbow support constraints to increasing paths. This is a dimension-uniform equivalent reformulation and methodological bridge, not a proof of NORI1.

##### Two-sided Hamming shells force antipodal balanced components to double their size

Let \(n=2d\), \(d\ge2\), and \(G\) be any \(d\)-regular subgraph of \(Q_{2d}\), such as either monochromatic graph in a vertex-balanced legal coloring. Let \(H\) be a connected component containing antipodal vertices \(x,\bar x\). Put \(a_k=|V(H)\cap\{v:d_H(x,v)=k\}|\). Then
\[
\boxed{a_k\ge\binom dk,\quad a_{2d-k}\ge\binom dk\ (0\le k<d),\qquad a_d\ge2.}
\tag{LB1}
\]
Consequently
\[
\boxed{|V(H)|\ge2^{d+1}.}\tag{LB2}
\]

*Proof.* At distance \(k<d\) from \(x\), a vertex has at most \(k\) cube neighbors in the previous Hamming layer and monochromatic degree \(d\), so it has at least \(d-k\) neighbors in the next layer. A vertex in layer \(k+1\) has at most \(k+1\) neighbors in layer \(k\). Double counting edges gives
\[
a_{k+1}\ge \frac{d-k}{k+1}a_k.
\]
Starting with \(a_0=1\), this yields \(a_k\ge\binom dk\) up to the middle layer. Apply the same argument from \(\bar x\) to obtain the upper-shell bounds. Thus \(a_{d-1}\ge d\) and \(a_{d+1}\ge d\). Every vertex in either of these two layers has at least one edge toward the middle, so there are at least \(2d\) edges incident with vertices in layer \(d\). Since every middle-layer vertex has degree \(d\), \(da_d\ge2d\), so \(a_d\ge2\). Summing all shell bounds yields
\[
|V(H)|\ge2\sum_{k=0}^{d-1}\binom dk+2=2^{d+1}.
\]
\(\square\)

**Component isoperimetry.** Every component \(K\) of a \(d\)-regular subgraph of \(Q_{2d}\) has at least \(2^d\) vertices: it spans at least \(d|K|/2\) cube edges, whereas the cube edge-isoperimetric bound gives at most \((|K|/2)\log_2|K|\). Equality forces \(K\) to be a \(d\)-dimensional face with all its internal edges present, which cannot contain a full-cube antipodal pair.

**Corollary.** If a vertex-balanced legal \(Q_{2d}\) coloring has \(t\) red components containing antipodal vertex pairs, then its total number of red components is at most \(2^d-t\). The analogous assertion holds for blue. Indeed, these \(t\) components require at least \(2^{d+1}\) vertices each, and the others at least \(2^d\), out of a total of \(2^{2d}\) vertices. By Wu--Yang and antipodal translation, each color has at least one component containing an antipodal pair, so each color has at most \(2^d-1\) components.

The component-size gap is universal and needs only vertex balance and cube geometry; it does not assert full geodesic reachability.


##### Monotone half-geodesic growth and singleton-midpoint rigidity

Fix \(n=2d\), \(d\ge2\), and a vertex-balanced legal antipodally odd coloring \(c\) of \(Q_{2d}\). For a root \(x\) and color \(\epsilon\in\{0,1\}\), define \(M^\epsilon_k(x)\) to be the set of vertices reachable from \(x\) by a color-\(\epsilon\) geodesic of precisely \(k\) steps, using \(k\) distinct directions. In particular \(M^\epsilon_d(x)\) is the half-geodesic midpoint reachability set.

**Theorem (monotone growth and rigidity of the equality case).** For every color, root and \(0\le k\le d\),
\[
\boxed{|M^\epsilon_k(x)|\ge\binom dk.}\tag{MG1}
\]
Moreover, the following are equivalent:

1. \(|M^\epsilon_d(x)|=1\);
2. the monochromatic connected component of \(x\) is a \(d\)-dimensional face of \(Q_{2d}\), with all its internal edges of color \(\epsilon\);
3. all half-geodesics of color \(\epsilon\) from \(x\) lie in the face spanned by the \(d\) directions of color \(\epsilon\) incident with \(x\).

In the singleton case, writing \(A\) for the incident color-\(\epsilon\) directions at \(x\), one has, for every \(0\le k\le d\),
\[
\boxed{M^\epsilon_k(x)=\{x\oplus S:S\subseteq A,\ |S|=k\},\qquad
M^\epsilon_d(x)=\{x\oplus A\}.}\tag{MG2}
\]

*Proof.* The color-\(\epsilon\) graph is \(d\)-regular. Every vertex of \(M^\epsilon_k(x)\), \(k<d\), has at most \(k\) neighbors in directions already used along a geodesic from \(x\), because its difference from \(x\) has weight \(k\). It therefore has at least \(d-k\) color-\(\epsilon\) neighbors in the next Hamming layer, all reached by extending a geodesic. Every next-layer vertex has at most \(k+1\) cube neighbors in the preceding layer. Thus
\[
|M^\epsilon_{k+1}(x)|\ge\frac{d-k}{k+1}|M^\epsilon_k(x)|.
\]
Starting at one root gives (MG1).

Suppose \(|M^\epsilon_d(x)|=1\). Applying the same inequalities backward from \(k=d-1\) to zero, and comparing with (MG1), forces equality at every layer:
\[
|M^\epsilon_k(x)|=\binom dk\quad(0\le k\le d).
\]
Let \(A\) be the \(d\) initial color-\(\epsilon\) directions. We prove (MG2) by induction. It holds at levels zero and one. If the reachable level \(k\) consists of all \(k\)-subsets of \(A\), then its vertices send at least
\[
(d-k)\binom dk=(k+1)\binom d{k+1}
\]
color-\(\epsilon\) edges toward the next layer. Since that next layer contains precisely \(\binom d{k+1}\) reachable vertices, each having at most \(k+1\) possible predecessors, equality holds throughout. Every reachable next-layer vertex therefore has all \(k+1\) of its predecessors among the \(k\)-subsets of \(A\); hence it is itself a subset of \(A\). This proves (MG2). Every forward cube edge within the face on \(A\) must have color \(\epsilon\), because equality forces each \(k\)-subset vertex to use all \(d-k\) of its forward edges inside the face. Thus all edges of that \(d\)-face are monochromatic. At each of its vertices, these \(d\) edges saturate the color-\(\epsilon\) degree, so no color-\(\epsilon\) edge exits the face. The face is precisely the connected component of \(x\).

Conversely, if the color-\(\epsilon\) component of \(x\) is a \(d\)-face, the only vertex at distance \(d\) in that face is its opposite corner, so \(|M^\epsilon_d(x)|=1\). The stated face description directly gives condition 3 and its converse under the growth equality. \(\square\)

**Corollary (no singleton midpoint on an antipodally reachable root).** If \(x\) and \(\bar x\) are connected by any monochromatic color-\(\epsilon\) path, then
\[
\boxed{|M^\epsilon_d(x)|\ge2,\qquad |M^\epsilon_d(\bar x)|\ge2.}\tag{MG3}
\]
Indeed, a singleton midpoint forces the component of that root to be a proper \(d\)-face, which cannot contain an ambient antipodal pair. This conclusion applies to arbitrary-length antipodal paths, not only full geodesics.

**Theorem (two-color midpoint branching at every vertex).** For every root \(x\) of every vertex-balanced legal coloring of \(Q_{2d}\),
\[
\boxed{|M^0_d(x)|+|M^1_d(x)|\ge3.}\tag{MG4}
\]
Equivalently, no vertex belongs simultaneously to a minimum-size red component and a minimum-size blue component.

*Proof.* Suppose both midpoint sets are singletons. The rigidity theorem forces a monochromatic red \(d\)-face \(F_A\) and a monochromatic blue \(d\)-face \(F_B\), both containing \(x\). At \(x\), the red and blue incident direction sets partition \([2d]\) into complementary size-\(d\) sets \(A,B\), so these are precisely the free directions of \(F_A,F_B\). Antipodal oddness makes the full-cube antipodal translate \(\bar F_A\) a monochromatic blue \(d\)-face. But \(F_B\) and \(\bar F_A\) meet at the vertex obtained by flipping precisely the \(B\)-directions of \(x\): \(x\oplus B\) belongs to \(F_B\), and its \(B\)-bits equal those fixed on \(\bar F_A\), while its \(A\)-bits are permitted to vary. Their union would therefore belong to a single blue component. Each face has all its vertices' blue degrees saturated within itself, so they would have to be the same blue component, impossible because their free direction sets \(B\) and \(A\) are disjoint. Thus at least one midpoint set has size at least two. \(\square\)

**Corollary (at most half the vertices lie in minimum-size components of one color).** Let \(F_R\) be the union of vertex sets of all red components that are \(d\)-faces. By antipodal oddness the union of blue \(d\)-face components is \(\overline{F_R}\). The two-color branching theorem gives \(F_R\cap\overline{F_R}=\varnothing\), hence \(|F_R|\le2^{2d-1}\). The same estimate holds for blue. Thus at least half of all cube vertices have at least two red half-geodesic endpoints, and likewise at least half have at least two blue half-geodesic endpoints.

These are unrestricted, dimension-uniform *monotone reachability* results. They supply a rigidity characterization for the minimal possible halfway endpoint count and show that antipodal oddness forces branching in at least one color at every root. They do not establish the intersection of opposite-root midpoint sets required for a monochromatic full antipodal geodesic.


##### A quantitative midpoint-overlap certificate for full antipodal geodesics

Retain the notation for vertex-balanced legal \(Q_{2d}\) colorings, \(d\ge2\), and for red half-geodesic endpoint sets \(M_d^R(x)\). Suppose \(x,\bar x\) belong to the same red connected component \(H\). Let
\[
r_x=|M_d^R(x)|,\qquad r_{\bar x}=|M_d^R(\bar x)|,\qquad
q_x=|M_d^R(x)\cap M_d^R(\bar x)|.
\]
The half-geodesic midpoint rigidity theorem shows \(r_x,r_{\bar x}\ge2\).

**Theorem (component volume controls midpoint overlap).** For every such red component,
\[
\boxed{|V(H)|\ge 2^{d+1}+2\bigl(r_x+r_{\bar x}-q_x-2\bigr).}\tag{MO1}
\]
Equivalently,
\[
\boxed{q_x\ge r_x+r_{\bar x}-2-\frac{|V(H)|-2^{d+1}}2.}\tag{MO2}
\]
In particular, if
\[
\boxed{|V(H)|<2^{d+1}+2(r_x+r_{\bar x}-2),}\tag{MO3}
\]
then \(q_x\ge1\), and a red *full antipodal geodesic from \(x\) to \(\bar x\)* exists.

*Proof.* Let \(a_k=|H\cap\{v:d_H(x,v)=k\}|\). The established two-sided growth inequalities (LB1) give
\[
a_k\ge\binom dk\ (k<d),\qquad
a_{2d-k}\ge\binom dk\ (k<d).
\]
At middle rank \(d\), the union of the two red half-geodesic endpoint sets is contained in \(H\), so
\[
a_d\ge|M_d^R(x)\cup M_d^R(\bar x)|
=r_x+r_{\bar x}-q_x.
\]
Use the baseline layer-count vector \(b_k=\binom dk\) for \(k<d\), \(b_{2d-k}=\binom dk\) for \(k<d\), and \(b_d=2\), whose total is \(2^{d+1}\). Its counts in the even- and odd-parity cube classes are equal, as follows from \(\sum_{k=0}^d(-1)^k\binom dk=0\).

Every component of the \(d\)-regular bipartite red graph also has the same number of even- and odd-parity vertices, by counting red edges between the two classes. Therefore, if \(a_d\) exceeds \(b_d=2\) by \(s\ge0\), the other-parity layers must contribute at least another \(s\) vertices beyond their baseline bounds. Thus
\[
|H|\ge2^{d+1}+2s
\ge2^{d+1}+2(r_x+r_{\bar x}-q_x-2).
\]
This proves (MO1)--(MO2). A vertex \(y\) in the intersection of the two midpoint sets is reachable by a red geodesic of length \(d\) from \(x\) and from \(\bar x\). The two direction sets of these geodesics are complementary, because \(y\) lies at Hamming distance \(d\) from each antipodal root. Reverse one half and concatenate; the resulting red path uses all \(2d\) directions precisely once and joins \(x\) to \(\bar x\). This proves (MO3). \(\square\)

**Corollary (counterexample component threshold).** Suppose \(c\) is a legal, vertex-balanced coloring of \(Q_{2d}\), and \(x,\bar x\) are red connected but possess **no red full antipodal geodesic**. Then
\[
\boxed{|V(H)|\ge2^{d+1}+4.}\tag{MO4}
\]
Consequently every red component of size strictly less than \(2^{d+1}+4\) that contains an antipodal vertex pair necessarily contains a red full geodesic joining that particular pair.

*Proof.* The absence of a red full geodesic means the two red midpoint endpoint sets are disjoint, so \(q_x=0\). Since their common red component contains an antipodal pair, the singleton-midpoint theorem gives \(r_x,r_{\bar x}\ge2\). Substitute into (MO1). \(\square\)

**Corollary (unrestricted counterexample obstruction).** If unrestricted NORI1 fails, then the previously established paired-balanced counterexample-preserving lift and the Wu--Yang monochromatic antipodal-path theorem produce a vertex-balanced counterexample on \(Q_{2d}\) containing both a red and a blue antipodal-connected component of size at least \(2^{d+1}+4\). For the antipodal roots in those components, the two respective color-specific half-geodesic endpoint sets must each contain at least two vertices and be disjoint.

This is a dimension-uniform *sufficient certificate* for monochromatic full antipodal geodesicity that uses component volume together with local half-geodesic branching, and a necessary component-size obstruction for hypothetical failures. Neither the volume constraint alone nor the branching constraint alone forces the required midpoint intersection for arbitrary components.


##### Central-hub exchange dichotomy for minimal half-geodesic frontiers

Let \(n=2d\), \(d\ge2\), and \(c\) be any vertex-balanced antipodally odd legal coloring of \(Q_{2d}\). Fix a color \(\epsilon\) and antipodal roots \(x,\bar x\) lying in one monochromatic color-\(\epsilon\) component \(H\). Let \(A\subset[2d]\) be the \(d\) directions of color \(\epsilon\) at \(x\). By antipodal oddness, the \(\epsilon\)-directions at \(\bar x\) are the complementary set \(B=[2d]\setminus A\). Put \(h=x\oplus A=\bar x\oplus B\).

**Theorem (minimal-frontier hub dichotomy).** Assume
\[
\boxed{|M_{d-1}^\epsilon(x)|=|M_{d-1}^\epsilon(\bar x)|=d.}\tag{HX1}
\]
Then both \((d-1)\)-step frontier sets are forced:
\[
\boxed{
M_{d-1}^\epsilon(x)=\{x\oplus(A\setminus\{a\}):a\in A\},\quad
M_{d-1}^\epsilon(\bar x)=\{\bar x\oplus(B\setminus\{b\}):b\in B\}.
}\tag{HX2}
\]
For either of the two poles \(u\in\{x,\bar x\}\), if the common central vertex \(h\) is **not** reachable by a color-\(\epsilon\) geodesic of length \(d\) from \(u\), then
\[
\boxed{|M_d^\epsilon(u)|=d.}\tag{HX3}
\]
If no full monochromatic geodesic joins \(x,\bar x\), at least one pole misses \(h\), and hence one has \(d\) midpoint endpoints while the other has at least two. Therefore
\[
\boxed{
\text{(HX1) and no color-\(\epsilon\) full antipodal geodesic}
\quad\Longrightarrow\quad
|H|\ge2^{d+1}+2d.
}\tag{HX4}
\]
Equivalently, if (HX1) holds and \(|H|<2^{d+1}+2d\), a color-\(\epsilon\) full antipodal geodesic joins \(x\) to \(\bar x\).

*Proof.* The binomial monotone-reachability bound gives \(|M_k^\epsilon(u)|\ge\binom dk\) for \(k\le d\) and the growth inequality \(|M_{k+1}^\epsilon(u)|\ge(d-k)|M_k^\epsilon(u)|/(k+1)\). Equality \(|M_{d-1}^\epsilon(u)|=d=\binom d{d-1}\) forces equality at every earlier rank by backward induction. Let \(A_u\) be the \(d\) initial \(\epsilon\)-directions at \(u\). The equality case of the backward-counting argument inductively yields
\[
M_k^\epsilon(u)=\{u\oplus S:S\subseteq A_u,\ |S|=k\}
\quad(0\le k\le d-1);
\]
all cube edges within the corresponding first \(d-1\) ranks of this \(d\)-face have color \(\epsilon\). Applying this to \(u=x\), \(A_u=A\), and to \(u=\bar x\), \(A_u=B\) gives (HX2).

Each of the \(d\) last-shell vertices \(x\oplus(A\setminus\{a\})\) has \(d-1\) color-\(\epsilon\) edges to its previous-layer predecessors, one for each element of \(A\setminus\{a\}\). As its monochromatic degree is \(d\), it has precisely one remaining color-\(\epsilon\) edge, going outward to layer \(d\). The candidate \(h=x\oplus A\) is a neighbor of *all* \(d\) last-shell vertices. Any alternative forward neighbor of \(x\oplus(A\setminus\{a\})\) has support \((A\setminus\{a\})\cup\{b\}\) for some \(b\in B\), and its missing element \(a\) is uniquely determined by that support. Consequently the alternatives from different \(a\)'s are distinct. If none of the remaining edges goes to \(h\), they yield precisely \(d\) distinct middle-layer endpoints, proving (HX3). The same argument applies at the other pole, where its initial set is \(B\) and its central candidate is again \(h\).

If both poles can reach \(h\) by monochromatic half-geodesics, reversing and concatenating the two halves produces a full antipodal monochromatic geodesic. Thus if the full geodesic is absent, at least one pole has \(d\) distinct middle endpoints by (HX3). The other has at least two midpoint endpoints because it is monochromatically connected to its antipode and the singleton-midpoint rigidity theorem applies. Since there is no full geodesic, the two midpoint endpoint sets are disjoint. Hence their union has at least \(d+2\) vertices in the middle layer. Substitute this into the proved volume-overlap theorem (MO1), with \(r_x+r_{\bar x}\ge d+2\) and overlap zero:
\[
|H|\ge 2^{d+1}+2((d+2)-2)=2^{d+1}+2d.
\]
This proves (HX4). \(\square\)

The theorem converts a local equality assumption one rank before the middle into a sharp *branching-or-meeting* alternative. It is a deterministic result for unrestricted nonlinear vertex-balanced legal colorings and directly constrains geodesic failure. It is distinct from size-only component bounds: the hypothesis is an extremal half-geodesic frontier, not a bound on component size.


##### Six-dimensional sharp-scale witness for antipodal component volume

The general component-volume obstruction (MO4) has the numerical scale \(2^{d+1}+4\). At \(d=3\), there is an explicitly checkable **successful** balanced legal \(Q_6\) coloring with a red antipodal component of precisely \(20=2^{4}+4\) vertices. Thus the volume \(20\) is attainable by an antipodal component, although this example does not show sharpness of (MO4) *under the additional absence-of-full-geodesic hypothesis*.

Index directions by \(i=0,\ldots,5\). For a cube vertex \(x\in\{0,1\}^6\), let \(r_i(x)\in\{0,\ldots,31\}\) be the integer whose binary bits are those of \(x\) in all positions other than \(i\), in increasing direction order. Define the color rule
\[
c_i(x)=\bigl(H_i\mathbin{\mathrm{shr}}r_i(x)\bigr)\ \&\ 1
\]
with 32-bit constants
\[
\boxed{
(H_0,H_1,H_2,H_3,H_4,H_5)=
(\texttt{0xFCC0FCC0},\texttt{0xE7669918},\texttt{0xFAA0FAA0},
\texttt{0x00FF00FF},\texttt{0x05A55A5F},\texttt{0x005F05FF}).
}\tag{Q6W1}
\]
These six rules ignore their own direction bits. Directly comparing the opposite indices \(r,31-r\) in each 32-bit mask proves \(c_i(\bar x)=1\oplus c_i(x)\). Direct summation at the \(64\) vertices gives \(\sum_i c_i(x)=3\) for each vertex, so every vertex has three incident edges of each color.

The red connected-component sizes are \(20\) and \(44\). The smaller component has vertices, in standard six-bit integer labels,
\[
\boxed{
H=\{0,1,2,3,4,5,6,7,13,15,21,23,29,31,45,47,53,55,61,63\}.
}\tag{Q6W2}
\]
Its antipodal vertex pairs are \(\{0,63\}\) and \(\{2,61\}\). It contains a red full antipodal geodesic from both \(0\) and \(2\), with common direction order
\[
\boxed{(0,1,2,4,3,5).}\tag{Q6W3}
\]
Every assertion can be checked by evaluating just 384 direction incidences and taking the connected components of the 192 cube edges; the existence certificate needs only the six indicated direction steps.

**Restricted affine contrast (finite diagnostic only).** For a vertex-balanced affine legal \(Q_6\) coloring, the six sign functions \((-1)^{c_i(x)}\) are signed odd Walsh characters independent of their own direction bits. Their sum is identically zero. Orthogonality of Walsh characters forces equal positive/negative multiplicities for each character, so the six directions can be paired into three character-opposite pairs. Exhausting the 15 perfect matchings of six directions, the eight admissible odd character supports on the remaining four bits for each pair, and the two sign choices for each pair gives \(15\cdot8^3\cdot2^3=61{,}440\) parametrizations (some can coincide). In this entire affine paired family, the only red-component size partitions are
\[
(64),\ (56,8),\ (48,16),\ (48,8,8),\ (32,32),
\]
and no antipodal-containing red component has \(24\) vertices or fewer. Thus the 20-vertex witness necessarily lies outside the affine class. This diagnostic is subordinate to the unrestricted midpoint theorems and is not used to prove them.

The finite witness supplies a sharp-scale test instance for any proposed size-only improvement of the midpoint-overlap argument. It also shows why treating the affine subclass as representative can miss small, antipodally connected monochromatic components.


#### Implication exposure characterizes stability under arbitrary feedforward additions

The transport graph can be replaced by its implication completion. This yields a necessary and sufficient criterion for a fixed interface to remain successful after every finite odd feedforward addition. The criterion allows arbitrary cyclic dependence among the existing nonexceptional rules.

Fix two distinguished directions \(a,b\) and a nonempty remaining set \(R\). Specify legal antipodally odd rules in directions \(R\), allowing arbitrary dependence on \(a,b\), and leave the rules in directions \(a,b\) unassigned. Let \(G\) be the transport graph defined above. Define \(H\) by putting
\[
v\longrightarrow u,\qquad \bar u\longrightarrow\bar v
\quad\hbox{for every arc }u\longrightarrow v\hbox{ of }G.
\tag{IE1}
\]
Bars in \(G,H\) complement the \(R\)-state; bars on full exposed states also complement \(a,b\).

**Lemma (implication completion for arbitrary interfaces).** There is an odd Boolean function \(f\) on \(Q_R\) for which the completion
\[
c_a=f(x_R),\qquad c_b=1+f(x_R)
\]
has no monochromatic full antipodal geodesic if and only if no SCC of \(H\) contains an antipodal pair.

*Proof.* The earlier complementary-pair 2-SAT argument does not use the unary hypothesis on the rules in \(R\). A zero full path, reversed if necessary to put \(a\) before \(b\), is precisely a transport arc \(u\to v\) with \(f(u)=0,f(v)=1\). Avoiding these arcs imposes the clauses \(f(u)\lor\neg f(v)\); oddness identifies the assertion at \(\bar u\) with the negation of the assertion at \(u\). Their two implications are (IE1). The SCC criterion for satisfiability gives the assertion. Oddness of the completed cube makes existence of a monochromatic-one full path equivalent to existence of a zero one. \(\square\)

Complementation reverses arcs of \(H\). Consequently, if an SCC \(C\) contains \(u,\bar u\), then
\[
\bar C=C:
\tag{IE2}
\]
its complemented SCC meets it and hence equals it. For such a \(C\), let \(\mathcal E_G(C)\) contain all full old cube states exposed between the exceptional steps in witnesses of \(G\)-arcs whose endpoints lie in \(C\). This definition refers to witnesses in \(G\), even though \(C\) is an SCC of \(H\).

**Theorem (sharp implication-exposure extension).** Adjoin a direction \(r\) whose rule is any odd Boolean function \(g\) of the full old state. The old rules ignore \(r\). Write \(H^g\) for the enlarged implication graph. For an antipodally invariant SCC \(C\) of \(H\), the subgraph induced on \(C\times\mathbb F_2\) is strongly connected if and only if
\[
g(x)=0\quad\hbox{at some }x\in\mathcal E_G(C).
\tag{IE3}
\]
When this holds, the enlarged exposure contains
\[
\mathcal E_{G^g}(C\times\mathbb F_2)
\supseteq \mathcal E_G(C)\times\mathbb F_2.
\tag{IE4}
\]
Thus an antipodal SCC with antipodal full-state exposure survives every odd feedforward addition.

*Proof.* Each old \(G\)-arc lifts with the new bit fixed at either prescribed value between the markers: insert the new zero edge outside the entire old witness, using oddness at its antipodal endpoints. Taking the two implications lifts every \(H\)-arc inside each new-bit layer.

A zero of \(g\) at an exposed state permits insertion between the markers. For both new-bit values this gives a \(G^g\)-arc changing that bit and therefore an \(H^g\)-arc changing it. The strongly connected copies of \(C\) in the two layers and these two bit-changing arcs connect the whole product.

Conversely, if \(g=1\) throughout the exposure, a \(G^g\)-arc projecting to endpoints in \(C\) cannot change the new bit between the markers. Every \(H^g\)-arc projecting inside \(C\) comes either from such a \(G^g\)-arc by reversal, or from one with endpoints in \(\bar C=C\) by complementation. It therefore preserves the new bit. The induced product is not strongly connected.

Outside insertion also preserves every old exposed state with either new-bit value, proving (IE4). If the old exposure contains antipodal full states, every odd \(g\) has a zero on it, and the enlarged exposure again contains antipodal full states. \(\square\)

**Theorem (complete feedforward-stability criterion).** The following are equivalent for a fixed interface.

1. \(H\) has an SCC \(C\) containing antipodal \(R\)-states, and \(\mathcal E_G(C)\) contains antipodal full old cube states.
2. After every finite succession of odd feedforward additions, every odd complementary completion in the two distinguished directions has a monochromatic full antipodal geodesic.
3. The conclusion in item 2 holds when additions are restricted to independent complementary pairs \(g,1+g\), each reading only the original full old state.

If item 1 fails, let \(k\) be the number of antipodal SCCs of \(H\). At most \(k\) independent complementary reader pairs suffice to produce an interface admitting a bad odd complementary completion. If the original nonexceptional rules occur in complementary pairs, the constructed bad cube is perfectly balanced.

*Proof.* Item 1 implies item 2 by repeated applications of (IE3)--(IE4), followed by the implication-SCC lemma. In particular it implies item 3.

Suppose item 1 fails. List the antipodal SCCs as \(C_1,\ldots,C_k\). Each is invariant under complementation by (IE2), and each exposure \(\mathcal E_G(C_j)\) contains no antipodal pair. Choose an odd Boolean function \(g_j\) that equals one throughout that exposure: assign zero on its antipodal image and extend oddly to the remaining pairs of full old states. Adjoin independent directions \(r_j,s_j\) with rules
\[
c_{r_j}=g_j,\qquad c_{s_j}=1+g_j.
\tag{IE5}
\]
All these rules ignore every added bit. They are legal and odd, and each pair preserves balance.

Let \(\widehat H\) be the enlarged implication graph. Deleting the added steps from any enlarged transport witness gives an old transport witness. Hence every \(\widehat H\)-arc projects to an \(H\)-arc, and every SCC of \(\widehat H\) projects inside one old SCC.

Over \(C_j\), the bit \(r_j\) is preserved by every \(\widehat H\)-arc. Indeed a transport witness with projected endpoints in \(C_j\) cannot traverse \(r_j\) between the markers: its projected full old state there would lie in \(\mathcal E_G(C_j)\), where \(g_j=1\). The same conclusion holds for the two kinds of implication arcs because \(\bar C_j=C_j\).

An antipodal SCC of \(\widehat H\) would project into an antipodal old SCC, say \(C_j\). It would then contain complementary values of \(r_j\), contradicting this preserved bit. Thus \(\widehat H\) has no antipodal SCC. The implication-SCC lemma constructs an odd exceptional function \(f\) yielding a bad completion. If \(k=0\), no additions are needed. This contradicts item 3 and proves the equivalence. \(\square\)

This dichotomy makes implication exposure a closure-equivalent target. Unrestricted NORI1 holds if and only if every legal interface with complementary pairs in \(R\) has an antipodal implication SCC with antipodal exposure. One implication follows from the preceding counterexample construction. For the other, the criterion supplies a full geodesic in every fixed-pair balanced cube, and the counterexample-preserving paired lift reduces every legal coloring to that class. Failure of the criterion produces a counterexample; failure of the stronger requirement of an antipodal SCC already in \(G\) would not by itself do so.

#### Cyclic cores with even dependence on the exceptional pair

The exposure seed need not be autonomous of both exceptional bits.

Partition the nonexceptional directions as \(R=K\sqcup J\). Suppose every rule indexed by \(K\) ignores \(J\), and
\[
c_i(x+e_a+e_b)=c_i(x)\qquad(i\in K).
\tag{EC1}
\]
Thus the rules of this possibly cyclic core may depend on the exceptional bits through \(x_a+x_b\). Suppose the directions of \(J\) have an ordering in which each rule reads only \(a,b,K\) and earlier directions of \(J\). Finally let
\[
c_a=f(x_R),\qquad c_b=1+f(x_R)
\]
for any odd \(f\).

**Theorem (even-marker cyclic-core absorption).** If one fixed exceptional-bit fiber of the \(K\)-coloring has a zero full \(K\)-geodesic, the entire coloring has a zero full antipodal geodesic. Every such fiber is a legal odd coloring of \(Q_K\). In particular, an already established NORI1 theorem for that core suffices, irrespective of its cyclic dependence, the number of feedforward additions, and the final exceptional function.

*Proof.* Write \(h_\zeta\) for the core coloring at exceptional assignment \(\zeta\in Q_{\{a,b\}}\). Condition (EC1) gives \(h_{\bar\zeta}=h_\zeta\). Combining this with oddness on the full old cube gives
\[
h_\zeta(\bar z)=1+h_\zeta(z)
\]
on each core edge, proving the fiber assertion.

Let \(P\) be a zero full core geodesic from \(u\) to \(\bar u\) in a chosen fiber \(\zeta\). The same path is zero in fiber \(\bar\zeta\). Place \(a\) first and \(b\) last, choosing the initial exceptional bits so that their value throughout \(P\) is \(\zeta\). This is a transport arc \(u\to\bar u\). Reversing \(P\), while retaining \(a\) first and \(b\) last, supplies \(\bar u\to u\). Repeat at \(\bar\zeta\). The strongly connected transport set \(C=\{u,\bar u\}\) has exposure containing both
\[
\{\zeta\}\times V(P),\qquad \{\bar\zeta\}\times V(P).
\]
In particular, \((\zeta,u)\) and \((\bar\zeta,\bar u)\) are exposed antipodal full states. This remains valid for an empty core, using its single state and the two marker steps.

Apply the odd-reader extension theorem successively through \(J\). The resulting transport set contains antipodal \(R\)-states. Oddness of \(f\) gives both function values on this strongly connected set; a directed path from an \(f=0\) state to an \(f=1\) state has a transport arc crossing those values. Its two exceptional edges and all its other edges are zero. \(\square\)

Here only a common zero full core geodesic in the opposite fibers \(\zeta,\bar\zeta\) was used to seed exposure. Condition (EC1) is a convenient sufficient hypothesis guaranteeing that a zero geodesic in one fiber is common to both.

**Corollary (joint sensitivity must reach surviving pair feedback).** Assume a bad fixed-pair balanced coloring of minimum dimension among all bad fixed-pair balanced colorings exists. Form its pair influence graph: vertices are complementary direction pairs, and \(P\to Q\) when the common rule of \(Q\) essentially reads a bit of \(P\). Fix any pair \(P=\{a,b\}\). In the graph with \(P\) deleted, let \(K\) comprise all pairs from which a directed cycle is reachable. Then some pair \(Q\in K\) has a nonzero joint derivative
\[
c_i(x+e_a+e_b)+c_i(x)\not\equiv0,\qquad i\in Q.
\tag{EC2}
\]
Equivalently, joint sensitivity to \(P\) reaches a cycle without revisiting \(P\).

*Proof.* The union of direction pairs in \(K\) is source-closed in the residual pair graph. Its complement \(J\) is acyclic; topologically ordering its pairs orders its directions as feedforward additions, because the two rules in a pair ignore both of that pair's bits. If (EC2) failed for every pair in \(K\), the core would satisfy (EC1). Each fixed exceptional-bit core fiber is then a legal odd fixed-pair balanced coloring in smaller dimension. Minimality supplies its monochromatic full geodesic, and oddness supplies a zero one. The preceding theorem absorbs \(J\) and closes the exceptional pair, a contradiction. An empty \(K\) uses the empty-core seed directly. \(\square\)

This necessity concerns sensitivity to flipping both bits of a pair and ancestry of surviving cycles. Ordinary essential dependence on either bit alone does not imply that joint sensitivity.

**Finite audit of the stronger transport target.** Full rooted direction orders were enumerated for 1,000 independent random eight-direction interfaces with three nonexceptional complementary pairs. Each pair rule was independently uniform among the odd functions on its six permitted input bits. All 1,000 transport graphs were strongly connected on their 64 states and had antipodal exposure. A further 2,000 interfaces were sampled by perturbing the autonomous cyclic unary interface \(c_2=x_4,\ c_4=x_6,\ c_6=x_2\), with the rules in directions \(3,5,7\) their respective complements, flipping each antipodal input-table pair independently with probability \(0.03\); each had at least one antipodal transport SCC with antipodal exposure. Seed 9314 was used. These are finite checks supporting the stronger \(G\)-based target; the implication-exposure dichotomy and cyclic-core absorption above are proved independently of them.


#### One-marker cyclic interfaces: exposure is automatic

A further absorption theorem allows arbitrary cyclic rules in the old core that read one distinguished bit. Its conclusion is a counterexample reduction, with no restriction on the number or complexity of feedforward additions.

Assume the rules in \(R\) ignore \(b\), while retaining arbitrary dependence on \(a\) and the other \(R\)-bits. Let \(G,H\) be the transport and implication graphs. For \(a=0\), write \(F\) for the ordinary coloring on \(Q_R\). The \(a=1\) fiber is
\[
\widetilde F(z)=1+F(\bar z)
\tag{OM1}
\]
on corresponding edges. No oddness within either fiber is assumed.

**Lemma (full marker exposure at every transport tail).** If \(u\) is the tail of any \(G\)-arc, then \(G\) has a loop at \(u\) with every prescribed assignment of the two marker bits between their steps. In particular, for any \(C\) containing \(u\),
\[
Q_{\{a,b\}}\times\{u\}\subseteq \mathcal E_G(C).
\tag{OM2}
\]

*Proof.* Since the \(R\)-rules ignore \(b\), deleting the \(b\)-step from a transport witness leaves a full \(R\cup\{a\}\)-path whose \(R\)-edges are zero and whose state at \(a\) is \(u\).

For initial \(a=0\), existence of such a path is equivalent to \(u\in A_0(F)\). Indeed, write its initial \(R\)-state as \(z\). Its prefix is a zero \(F\)-path \(z\to u\), while its suffix is a zero \(\widetilde F\)-path \(u\to\bar z\). Reverse the prefix and complement and reverse the suffix. Their concatenation is a full \(F\)-geodesic
\[
u\longrightarrow z\longrightarrow\bar u
\]
with color word \(0^*1^*\). These operations are reversible.

For initial \(a=1\), the same argument gives \(u\in A_0(\widetilde F)\). But
\[
A_0(\widetilde F)=\bar A_1(F)=A_0(F),
\tag{OM3}
\]
using complementation of vertices, complementation of colors, and geodesic reversal. Thus either initial value of \(a\) can be used at the same state \(u\). Insert \(b\) immediately after \(a\), choosing its bit arbitrarily. The \(R\)-rules ignore it, so this gives the required loop with both choices of the interior \(a\)-bit and both choices of the interior \(b\)-bit. Its exposed state is the specified marker assignment over \(u\), proving (OM2). \(\square\)

**Theorem (automatic implication exposure).** In a one-marker interface, every antipodal SCC \(C\) of \(H\) has antipodal full-state exposure.

*Proof.* Let \(T\) and \(U\) be the respective tails and heads of \(G\)-arcs with both endpoints in \(C\). They are nonempty: the strongly connected set \(C\), which contains two antipodal states, has an internal implication edge; by \(\bar C=C\), its underlying \(G\)-arc also has endpoints in \(C\).

There is a state \(u\in T\) with \(\bar u\in T\cup U\). Otherwise \(T\cap\bar T=T\cap\bar U=\varnothing\). Every internal \(H\)-arc leaving \(T\) is then of the reversed-\(G\) kind and lands in \(T\); the complemented-\(G\) kind starts in \(\bar T\) and cannot start in \(T\). Thus \(T\) is nonempty and forward-closed inside the strongly connected \(C\), forcing \(T=C\). This contradicts \(\bar C=C\) and \(T\cap\bar T=\varnothing\).

The endpoint \(\bar u\in T\cup U\) occurs as the \(R\)-projection of an exposed full state, say \((\zeta,\bar u)\). By (OM2), \((\bar\zeta,u)\) is also exposed. These states are antipodal. \(\square\)

**Corollary (success transfers to every odd feedforward addition).** For a one-marker interface, the following are equivalent:
- Every odd complementary exceptional completion of the original interface has a monochromatic full antipodal geodesic.
- The same holds after every finite succession of arbitrary odd feedforward additions.

The statement also holds with additions restricted to complementary pairs. It follows from the implication-SCC lemma, automatic exposure, and the complete feedforward-stability criterion.

**Theorem (one-marker feedback-core counterexample reduction).** Consider a completed coloring with exceptional pair \(c_a=f(x_R),c_b=1+f(x_R)\), and partition \(R=K\sqcup J\). Assume:
- Every \(K\)-rule ignores \(b\) and \(J\), and may depend arbitrarily on \(a\) and the other \(K\)-bits.
- The directions in \(J\) can be ordered so that each rule reads only \(a,b,K\) and earlier directions in \(J\).

If this coloring is bad, there exists a bad legal odd coloring on \(Q_{K\cup\{a\}}\). Consequently, NORI1 in dimension \(|K|+1\) closes every coloring in this class, with arbitrarily many nonlinear feedforward additions and arbitrary final odd \(f\).

*Proof.* Disregard the final exceptional rules and form the one-marker core interface on \(a,b,K\). If it had an antipodal implication SCC, automatic exposure would make it stable through all additions in \(J\), and the final completion would be good. Hence it has none. The implication-SCC lemma supplies an odd Boolean function \(f_0\) on \(K\) for which
\[
c_a=f_0(x_K),\qquad c_b=1+f_0(x_K)
\]
gives a bad completed core.

Delete direction \(b\). The resulting coloring on \(K\cup\{a\}\) is legal and odd. If it had a monochromatic full antipodal geodesic, choose its color to be zero by oddness. The two endpoint \(K\)-states are antipodal, so the incident \(b\)-edge has color zero at one of them. Append that edge before or after the geodesic. Every retained rule ignores \(b\), yielding a zero full geodesic in the completed core, a contradiction. The smaller coloring is therefore bad.

An empty \(K\) cannot occur in a bad coloring under these hypotheses: the empty transport seed has full marker exposure, and the feedforward theorem applies directly. \(\square\)

This reduction permits feedback of arbitrary complexity inside \(K\cup\{a\}\), as well as return dependence through the final exceptional function. The smaller exceptional function \(f_0\) is extracted by the implication clauses; it need not be a fiber of the final \(f\). The conclusion is an existence-preserving counterexample reduction. It does not prescribe roots or preserve perfect balance in the smaller cube.


##### Colorwise Eulerian splitting and optimal Euler tour switches

#### Optimal color-change Euler circuits in balanced cubes

Let c color Q_(2m) with m red and m blue edges incident at every vertex. Let k_R,k_B be the numbers of red and blue connected components. Count switches in an Euler circuit cyclically, including last-to-first.

**Theorem.** The minimum number of cyclic color switches is
\[
\boxed{s(c)=2^{2m}\ (m\ {\rm odd}),\qquad s(c)=2(k_R+k_B-1)\ (m\ {\rm even}).}
\]
Both constructions work for arbitrary balanced colorings. Under antipodal oddness the underlying directed-edge orientations can additionally be chosen so antipodality reverses each arrow.

*Odd case, lower bound.* At any vertex v an Euler tour pairs its incident red and blue half-edges into transitions. If t(v) is the number of bichromatic pairs, then t(v)=m (mod 2), since the red-red pairs consume the other red half-edges two at a time. When m is odd t(v)>=1, so total switches s=sum_v t(v)>=2^(2m).

*Odd case, sharp construction.* Every color subgraph is m-regular bipartite, so has a perfect matching. Choose a red matching M_R and a blue matching M_B. If c is antipodally odd choose M_B=antipode(M_R). After removing these matchings each monochromatic subgraph has even degree m-1=2q. Euler-orient the remaining red components and, in the antipodal case, orient remaining blue components as the reversed antipodal image of red. Orient the red matching even-to-odd and the blue matching odd-to-even. Split each original cube vertex into a red and a blue state, attaching each colored edge to its state. Add a zero-length color-change portal blue->red at every even vertex and red->blue at every odd vertex. Each split state has equal indegree and outdegree: its matching creates a deficit of one, canceled by its portal. The underlying undirected split graph is connected, since the cube is connected and the portal joins the color states of every vertex. Hence the split digraph has one Euler tour. Project away the portals: this gives a closed Euler tour of every cube edge with one switch at each original vertex, attaining 2^(2m). The antipodal map swaps red and blue states and reverses every arrow, including each portal, when the coloring is odd.

*Even case, lower bound.* Now all monochromatic components have even degree m, hence Euler circuits. Form a bipartite multigraph J whose vertices are the k_R red and k_B blue components, with one edge for each original cube vertex v joining the red and blue components containing v. J is connected because Q_(2m) is connected. In any Euler tour, t(v) is even. The original vertices at which t(v)>0 correspond to a connected spanning collection of incidence edges in J, since a tour can leave one color component for another only through a color switch. There must be at least k_R+k_B-1 such vertices, each with at least two switches. Thus s>=2(k_R+k_B-1).

*Even case, construction.* Choose a spanning tree T of J and an Euler circuit for each monochromatic component. Begin with a root-component circuit; for every tree edge, insert the circuit of the as-yet-unvisited neighboring component at its associated original vertex v, which belongs to both components. Each insertion joins closed tours of opposite colors and creates two switches. Tree edges are distinct original cube vertices, so previous splices are unaffected. The result is a single Euler tour of the entire cube, with precisely 2(k_R+k_B-1) switches. In an antipodally odd coloring the separate red and blue component circuits can be given antipodally reversing orientations before splicing.

**Corollary.** If m is odd, the optimal Euler tour splits at its one portal per vertex into 2^(2m-1) red trails from distinct even vertices to distinct odd vertices, and equally many blue trails in the reverse parity direction. Their average length is m, since each color has m*2^(2m-1) edges. Their endpoints have opposite parity, so none individually joins antipodal vertices in Q_(2m). This identifies a parity obstacle to deriving NORI1 from color-switch-optimal Euler tours alone.

**Finite verification.** Exhaustive enumeration of all 2^16 legal antipodally odd Q4 edge assignments gives 48 vertex-balanced colorings. Each has two red connected components and two blue connected components; the theorem therefore yields a six-switch optimal Euler tour in each case.

The theorem is independent of bounds on nonlinear direction rules. It upgrades arbitrary Euler-tour existence to the least possible number of transitions while retaining the original cubical edge set.

##### Two antipodally paired directed Euler tours and folded-cube transversals

#### Antipodally paired Euler tours in balanced cubes

Let \(D\) be an Eulerian orientation of a connected graph \(G\), equipped with a fixed-point-free involution \(\tau\) on its geometric realization such that \(\tau\) takes every directed edge \(u\to v\) to a directed edge \(\tau v\to\tau u\). Assume \(\tau\) fixes no geometric edge or point.

**Theorem (two-tour decomposition).** The edge set of \(D\) admits a partition into two directed closed Euler trails \(T,\tau(T)^{\mathrm{rev}}\), each using every edge in its part once, exchanged by antipodal reversal. A \(\tau\)-equivariant local transition system cannot have a single Euler circuit, so two tours is best possible among symmetry-preserving Euler decompositions.

*Proof.* At each vertex \(v\), choose a bijection \(f_v\) from its incoming arcs to outgoing arcs. On one member of each vertex pair \(\{v,\tau v\}\) choose this bijection arbitrarily, and prescribe on the other vertex
\[
f_{\tau v}(\tau f_v(e))=\tau e
\]
for every incoming arc \(e\) of \(v\). This is consistent because \(\tau\) reverses arrow directions and \(v\ne\tau v\). The resulting local pairing decomposes the arcs into directed closed Euler trails, and \(\tau\) carries each trail, with its cyclic order reversed, onto another trail.

No trail is preserved by this involution. If a trail were preserved, the induced involution on its cyclic abstract edge-occurrence circle would reverse the cyclic orientation. Every orientation-reversing involution of a circle has a fixed point, which would correspond to a point of \(G\) fixed by \(\tau\) (at a vertex occurrence or inside an edge). This contradicts the assumption.

Thus the trails occur in disjoint antipodal pairs. If there are at least two such pairs, connectedness of \(G\) ensures some vertex \(v\) is incident with edges belonging to trails \(A,B\) from two different pairs: otherwise edge sets of distinct pairs would have disjoint vertex sets and disconnect \(G\). At \(v\), interchange the successors of an incoming arc from \(A\) and one from \(B\), merging these two directed trails into one. At \(\tau v\), make the conjugate successor interchange, merging their two antipodal mates. The two vertex locations differ, the four original trails are distinct, and the paired changes maintain the \(\tau\)-equivariance of the transition system. They replace two antipodal pairs of trails by one pair. Iterate until precisely one pair remains. Since every arc occurs in one trail, the two remaining trails partition \(E(D)\), and \(\tau\) exchanges them with reversal. \(\square\)

**Corollary (uniform direction counts in balanced NORI1 cubes).** Suppose \(N=2m\ge4\) and \(c\) is a perfectly balanced antipodally odd coloring of \(Q_N\). Orient red edges even-to-odd and blue edges odd-to-even. This is an Eulerian orientation on which \(\tau(x)=\bar x\) reverses every arrow. The theorem gives two antipodally paired directed Euler tours \(T,T^\tau\) with
\[
\boxed{|E(T)|=N2^{N-2},\quad
\#\{\text{direction }i\text{ edges in }T\}=2^{N-2}
\quad(i=1,\ldots,N).}
\]
Each tour alternates red and blue, and therefore contains \(N2^{N-3}\) edges of each color. The formulas also hold for its antipodal partner.

*Proof.* Antipodal reflection preserves edge direction classes and bijects the two tours. The full cube has \(2^{N-1}\) edges of each direction, so each tour contains half of that class. Directed edges alternate colors under the parity-defined orientation. \(\square\)

**Finite audit.** For a representative antipodally odd vertex-balanced coloring of \(Q_4\), all \(2^8\) involution-equivariant choices of local incoming-to-outgoing pairings at the eight antipodal vertex pairs were enumerated. A choice with precisely two directed tours was found. Their lengths were 16 and 16; each uses four edges in every direction, and the antipodal map exchanges the two tours. The theorem is combinatorial and does not depend on this finite check.

This is a symmetry-preserving half-Euler decomposition, not yet a NORI1 proof: its directed tours alternate colors, and the direction repetition within them is large. Any attempt to obtain a monochromatic full antipodal geodesic must extract an \(N\)-step zigzag using each direction once rather than merely a directed subtrail.

**Antipodal-edge transversal corollary.** In the two-tour decomposition, each tour contains one edge from every antipodal pair \(\{e,\tau(e)\}\): if \(e\) belongs to the first tour, \(\tau(e)\) belongs to its disjoint second tour. Therefore the projection of either tour to the folded cube \(Q_N/\langle\tau\rangle\) is an Euler circuit of the entire folded cube graph, and the first tour is a closed directed lift of that Euler circuit. This lift alternates red and blue and uses one representative from every antipodal edge orbit. In particular, the quotient Euler tour traverses \(2^{N-2}\) edges of each direction and its lift has trivial antipodal monodromy. The second closed lift contains all antipodal mate edges in reversed traversal order. This is a much stronger property than merely splitting an Euler tour into two circuits of equal length.


##### Switch-optimal antipodally paired Euler tours

#### Switch-optimal antipodally paired two-tour decompositions

Let \(c\) be antipodally odd and perfectly balanced on \(Q_N\), \(N=2m\ge4\). The antipode \(\tau\) exchanges red and blue subgraphs, so their numbers of components agree: write \(k=\kappa_R=\kappa_B\).

**Theorem (symmetric two-tour switch optimum).** There is an Eulerian orientation of the whole cube that reverses under \(\tau\) and a pair of edge-disjoint directed closed tours \(T,\tau(T)^{\rm rev}\) partitioning the cube edges, such that each tour contains one edge from every antipodal edge orbit and the total number of cyclic red/blue switches across the two tours is
\[
\boxed{
\begin{cases}
2^N,&m\text{ odd},\\
4(k-1),&m\text{ even}.
\end{cases}}
\tag{ST1}
\]
These switch counts are minimal among antipodally equivariant two-tour transition systems. In the even-\(m\) case, each tour has \(2(k-1)\) switches. In the odd-\(m\) case, each has \(2^{N-1}\) switches, occurring at complementary representatives of the antipodal vertex pairs.

*Proof, odd \(m\).* Both monochromatic graphs are odd-regular and bipartite. Choose a red perfect matching and take its antipodal blue matching. Euler-orient the residual even-degree monochromatic graphs in antipodally reversed pairs. Orient the red matching even-to-odd and the blue matching odd-to-even. Split each cube vertex into red and blue states and insert one portal blue-to-red at even vertices, and red-to-blue at odd vertices. The resulting directed split graph is connected and Eulerian, with a free arrow-reversing involution swapping colors and antipodal vertices. Apply the two-tour decomposition theorem for such oriented graphs: choose incoming-to-outgoing pairings equivariantly, then splice different pairs at antipodal vertex locations until precisely two tours remain. All original cube edges and portals are partitioned, and the tours are antipodal reversals. Each of the \(2^N\) portals represents one red/blue switch, so the total is \(2^N\). The antipode pairs the portals without fixed points and exchanges the two tours, so each tour traverses \(2^{N-1}\) portals. The half-edge parity argument forces at least one color switch per vertex in every decomposition when \(m\) is odd, proving optimality.

*Proof, even \(m\): construction.* Every red component has even degree and an Eulerian orientation; orient each blue antipodal mate by reversing the red orientation. Initially these give \(k\) pairs of antipodally exchanged monochromatic Euler circuits, with no switches. Their union is the full edge set. If more than one pair remains, connectedness of the original cube guarantees a vertex \(v\) incident with two tours \(A,B\) from different antipodal pairs. Those two incident tours must have different colors at \(v\): all red edges at \(v\) belong to its unique red component, which remains entirely in one tour under the merging process, and likewise for blue edges. Swap the outgoing successors at the selected traversal of \(v\), merging the two tours and creating two color changes; perform the conjugate swap at \(\tau v\), merging the antipodal mates and creating two further changes. The two sites are distinct, and the four tours were in distinct pairs. Each operation reduces the number of pairs by one and introduces four switches. After \(k-1\) operations precisely two tours remain, with \(4(k-1)\) switches, exchanged by antipodal reversal. Every individual antipodal edge orbit is split between the tours, since they partition all edges and the antipode swaps tours.

*Even case: lower bound.* In any \(\tau\)-equivariant transition system with just two tours, the set of original vertices where some colors switch must connect the \(k\) antipodal *pairs* of original monochromatic connected components. Each antipodal pair of switch sites can join at most two previously disconnected component-pair groups. At least \(k-1\) antipodal pairs of switch sites are needed. Because \(m\) is even, the number of red-blue transitions at each vertex is even, hence at least two at a switch site. Such sites are antipodally paired, giving at least four switches per pair and at least \(4(k-1)\) switches overall. \(\square\)

**Corollary (folded-cube half-Euler tours).** Each of the two directed tours uses one representative of every antipodal edge orbit and hence projects to a single Euler circuit of the folded cube \(Q_N/\tau\). Each tour traverses \(2^{N-2}\) edges in each direction. For \(m\) even, the resulting directed folded-cube Euler tour changes the original red/blue color only \(2(k-1)\) times, although its edge colors are not intrinsic to the quotient: each quotient edge has two oppositely colored lifts.

This is a global structural theorem for balanced antipodal colorings, including nonlinear rules. It does not imply a monochromatic full geodesic: the Euler tours may repeat directions, and the red/blue blocks need not be geodesic. The issue for NORI1 is to extract a direction-simple monochromatic segment or splice without losing antipodal endpoint control.

##### Direction-uniform monochromatic Eulerian cycles can avoid every full rainbow segment

The following construction tests direct extraction from monochromatic Eulerian cycles. It applies in perfectly balanced odd cubes, including dimensions divisible by four.

**Theorem.** For every \(t\ge1\), there is a perfectly balanced antipodally odd coloring of \(Q_N\), \(N=12t\), and a simple red cycle \(C\) of length \(2N\) such that:
1. Every direction occurs twice on \(C\).
2. \(V(C)\cap\overline{V(C)}=\varnothing\).
3. No contiguous segment of \(C\) is a full rainbow geodesic.
4. Some colorwise Eulerian orientation and circuit decomposition contains \(C\) as a directed red circuit; its antipodal blue circuit can be oriented in reverse.

Thus even the smallest possible positive, uniform direction multiplicity on a cube circuit can coexist with complete avoidance of antipodal vertex pairs. Direct extraction requires exchanges involving edges outside the selected circuit.

*Construction in dimension twelve.* For \(0\le i<6\), let \(f_i(x)\) be bit \(x\), with bit zero least significant, of the following 64-bit hexadecimal word; vertices of \(Q_6\) are encoded by \(x=\sum_i2^ix_i\):
\[
\begin{array}{c|c}
i&H_i\\\hline
0&\texttt{CFFFFFFF0000000C}\\
1&\texttt{0FFFFFF0F000000F}\\
2&\texttt{77FFFFFF00000011}\\
3&\texttt{F7F7FFFF00001010}\\
4&\texttt{FFFFFFFF00000000}\\
5&\texttt{BFF71002BFF71002}
\end{array}
\]
For every \(i,x\), these finite tables satisfy
\[
f_i(x+e_i)=f_i(x),\qquad f_i(x+\mathbf1)=1-f_i(x).
\]
On \(Q_{12}\), with old bits \(x\in Q_6\) and new bits \(y\in Q_6\), set
\[
c_i(x,y)=f_i(x),\qquad c_{i+6}(x,y)=1-f_i(x).
\]
Take color one to be red. The rules are legal and antipodally odd, and each pair contributes one red incident edge, proving perfect balance.

The old direction word
\[
w=(1,0,1,5,0,4,3,4,2,5,3,2)
\]
from root zero gives the twelve distinct vertices
\[
(0,2,3,1,33,32,48,56,40,44,12,4)
\]
before returning to zero. Every traversed edge has color one. This vertex set is disjoint from its complement under \(x\mapsto63-x\). The numbers of distinct labels in its twelve cyclic windows of length six are
\[
(4,5,5,5,5,4,4,5,5,5,5,4).
\]
In particular no such window is rainbow.

Insert the two occurrences of new direction \(i+6\) immediately before the old steps with the following zero-based positions:
\[
(0,3),\ (4,5),\ (1,2),\ (0,1),\ (0,1),\ (0,1)
\quad(i=0,\ldots,5).
\]
At each indicated old vertex, \(f_i=0\), so each new step is red. Order simultaneous inserted steps increasingly. The resulting direction word is
\[
\begin{split}
W={}&(6,9,10,11,1,8,9,10,11,0,8,1,\\
&6,5,7,0,7,4,3,4,2,5,3,2).
\end{split}
\]
Every label occurs twice, so the walk closes. Old vertices at distinct old-step positions are distinct; within an insertion block, distinct new bits are flipped once each. Hence the 24 vertices before closure are distinct. Projection to the old bits proves antipodal avoidance. A hypothetical rainbow twelve-step segment would project to a cyclic six-step segment of \(w\) using all six old directions, contradicting the displayed window counts.

*Passage to all \(N=12t\).* Take the Cartesian product of \(t\) copies of this coloring. It is perfectly balanced and antipodally odd. In factor \(j\), write its cycle as a path \(P_j\) consisting of the first 23 edges, followed by its closing edge \(e_j\). Traverse
\[
P_1P_2\cdots P_t e_1e_2\cdots e_t
\]
in the product. This is a simple cycle: during the initial phase the factors successively move from their roots to their respective neighbors of the roots along simple paths, and during the closing phase those factors return to their roots one at a time. Comparing the factors already entered and already returned excludes any repeated vertex before final closure. All edges are red, and every direction appears twice. Each factor projection stays in its antipodal-free cycle vertex set, proving antipodal avoidance. This also excludes a full rainbow segment, whose endpoints would be antipodal.

Finally the red graph has degree \(N/2=6t\), which is even. Delete the edges of the displayed simple cycle. Every remaining red degree is even, so each remaining component has an Eulerian orientation. Orient the selected cycle cyclically and combine these orientations. Orient blue edges as the reversed antipodal image of red edges. This gives the claimed colorwise Eulerian realization. \(\square\)

**Verification and scope.** All 384 old table entries were checked for direction invariance and antipodal oddness; all prescribed old and inserted edges and all cyclic windows were checked directly. The product and Eulerian arguments above establish the dimension-uniform family. These colorings are successful instances of NORI1: the theorem concerns the specified circuits. The resulting research target is a global circuit exchange that uses the surrounding red edges and antipodal blue structure while controlling repeated directions.


For completeness, the twelve-dimensional coloring in the last theorem has a red full geodesic from root zero in direction order \(6,9,2,3,7,8,10,5,0,1,11,4)\). Substitution in the displayed tables verifies all twelve colors. Concatenating these witnesses in the Cartesian factors proves success for every member of the family.


#### Reconfiguration by antipodal directed-cycle reversal

##### Antipodal directed-cycle reconfiguration of balanced legal colorings

Let \(\mathscr B_N\) denote antipodally odd vertex-balanced binary edge colorings of \(Q_N\), for even \(N\ge4\). For \(c\in\mathscr B_N\), orient red edges from even to odd and blue edges from odd to even, obtaining the Eulerian digraph \(D(c)\). The antipode \(\tau(x)=\bar x\) reverses every arrow.

**Theorem (monotone cycle-flip connectivity).** Given \(c,d\in\mathscr B_N\), their disagreeing-edge subgraph
\[
F=\{e:c(e)\ne d(e)\}
\]
is directed Eulerian under \(D(c)\), invariant under antipodal arrow reversal, and admits an edge partition into distinct pairs of antipodal directed simple cycles \(C,\tau C\). Reversing the colors of every edge of such a pair preserves balance and antipodal oddness and decreases the number of disagreements with \(d\) by \(2|C|\). Repeating transforms \(c\) into \(d\) in at most \(|F|/8\) paired flips.

*Proof.* At a vertex \(v\), the number of incident formerly red edges that become blue equals the number of formerly blue edges that become red, because the two colorings have the same red degree \(N/2\). At even vertices, changed red edges point outward in \(D(c)\) and changed blue edges point inward; at odd vertices the roles reverse. Thus \(D(c)[F]\) has equal incoming and outgoing degrees. Both colorings are antipodally odd, so \(F\) is invariant under \(\tau\), which reverses the ambient arrows.

Choose at one vertex of each antipodal vertex pair a bijection from incoming \(F\)-arcs to outgoing \(F\)-arcs, then define the matching at its antipode by reversing and antipodally translating this bijection. The resulting transition system decomposes \(F\) into directed simple cycles exchanged by \(\tau\) with reversal (split any repeated-vertex closed trails if necessary, respecting the paired transitions). No directed cycle is fixed by this involution: reversal of its cyclic parameter would have a fixed point, whereas the antipodal map fixes no vertex or interior point of an edge of the cube. Thus cycles occur in distinct antipodal pairs.

Flipping one pair reverses two directed cycles, preserving the Eulerian condition at every vertex. The simultaneous antipodal flip preserves legality. Since all their edges are disagreements, flipping them makes those edges agree with \(d\) and changes no other edge. Each cycle has length at least four, so each pair removes at least eight disagreements. \(\square\)

**Corollary (per-direction four-divisibility).** For every direction \(i\), the number of \(i\)-edges on which two members of \(\mathscr B_N\) disagree is divisible by four; the total disagreement is divisible by four, and distinct members differ on at least eight edges.

*Proof.* A closed cube walk traverses each direction an even number of times. Its antipodal partner traverses the same number, doubling an even number. Add over paired directed cycles. \(\square\)

**Corollary (first failing cycle flip).** If a counterexample to NORI1 exists, there is a good balanced legal coloring \(g\) and an antipodal pair of directed cycles \(C,\tau C\) in \(D(g)\) such that flipping these cycles gives a bad legal coloring. Every monochromatic full antipodal geodesic in \(g\) intersects \(E(C)\cup E(\tau C)\).

*Proof.* Choose a fixed known good balanced coloring of the same dimension and use the theorem to connect it to a balanced bad counterexample, supplied if necessary by the standard counterexample-preserving paired lift. Take the first good-to-bad step. A monochromatic full geodesic of \(g\) avoiding the flipped edges would survive in the bad coloring, which is impossible. \(\square\)

This places every balanced legal coloring in one cycle-flip reconfiguration component, with a strictly decreasing disagreement potential toward any chosen reference. The first-failure corollary identifies a possible cycle transversal of all full monochromatic geodesics; exclusion of such a transversal is a stronger problem not proved here.

#### Directed matching-pair 2-factorization

##### Antipodally paired directed 2-factorization

Let \(c\) be a perfectly balanced antipodally odd coloring on \(Q_N\) with \(N=2m\ge4\). The red edge graph \(R\) is \(m\)-regular and bipartite. By the bipartite one-factorization theorem, its edge set partitions into \(m\) perfect matchings,
\[
E(R)=M_1\sqcup\cdots\sqcup M_m.
\tag{EF1}
\]
Antipodal translation \(\tau(x)=\bar x\) maps the red edge graph bijectively to the blue edge graph. Therefore the blue edges split into perfect matchings \(\tau(M_j)\).

**Theorem.** For each \(j\), the spanning 2-regular subgraph
\[
F_j=M_j\cup\tau(M_j)
\]
is a union of alternating-color directed cycles under the canonical Eulerian orientation. Its directed cycles occur in distinct antipodal-reversal pairs. Moreover
\[
\boxed{E(Q_N)=F_1\sqcup\cdots\sqcup F_m.}
\tag{EF2}
\]
Thus every balanced legal coloring admits a decomposition into \(m\) antipodally invariant directed cycle covers, each with one incoming and one outgoing arc at every vertex.

*Proof.* Every vertex meets one red matching edge and one blue matching edge of \(F_j\). The canonical orientation points the red edge outward at even vertices and the blue edge inward there, reversing those roles at odd vertices. So each vertex has one incoming and one outgoing \(F_j\)-arc and each connected component is a directed cycle alternating colors. Antipodality maps \(F_j\) to itself, reverses every arc, and acts without fixed points on the geometric realization of the cube. A self-antipodal directed component would yield an orientation-reversing involution of its traversal circle with a fixed point; hence the directed cycles come in distinct antipodal pairs. The perfect matchings partition all red and blue edges, proving (EF2). \(\square\)

**Paired-lift specialization.** For the complementary paired lift \(C_i(x,y)=c_i(x)\), \(C_{m+i}(x,y)=1-c_i(x)\), the set of red edges in the two directions \(\{i,m+i\}\) is a perfect matching \(M_i\). Its blue antipodal mate is the set of blue edges in the same two directions, and \(M_i\cup\tau(M_i)\) partitions into directed four-cycles of those pair-faces. Thus (EF2) generalizes the edge-disjoint directed-square decomposition of the standard lift to arbitrary balanced colorings, with longer cycles replacing squares.

**Algebraic permutation form.** Treat each perfect matching \(M_j\) as a fixed-point-free involution \(r_j\) on cube vertices, taking each vertex to its red matching neighbor. Its blue matching involution is \(b_j=\tau r_j\tau\). On even-parity vertices, two successive directed steps of \(F_j\) act as
\[
T_j=b_jr_j=\tau r_j\tau r_j,\qquad
\tau T_j\tau=T_j^{-1}.
\tag{EF3}
\]
Thus the oriented 2-factors provide an ensemble of reversible permutations of the even-parity vertex set, whose cycles are the even-vertex halves of the directed alternating cycles. This is a potential entry point for permutation/rainbow-path methods; no direction-simple antipodal path is asserted.

#### Complementary cube covers and lifted Euler-tour monodromy

COVERING THEOREM. Let c be any binary undirected-edge coloring of Q_m. On the paired lift Q_(2m), original direction i has signed color c_i(x), and dummy direction m+i has complementary color 1-c_i(x). Write z=x XOR y. The projection pi(x,y)=z maps the red subgraph R onto the smaller cube Q_m as a 2^m-sheeted graph cover: at every lifted vertex, for each base direction i, one and only one incident red edge lies in paired directions {i,m+i}, and it projects to base direction i. The blue graph B is another covering of Q_m of the same fiber cardinality. If c is antipodally odd, tau(x,y)=(bar x,bar y) maps red to blue and fixes z, giving a fiber-preserving isomorphism between R and B. These graph covers need not be connected or normal.

EULER-TOUR LIFT DECOMPOSITION. If m is even, choose an Euler tour W of Q_m, length L=m*2^(m-1), beginning and ending at a base vertex z0. Unique path lifting defines a return permutation sigma_R of the 2^m red fiber states over z0. Each orbit of length k of sigma_R gives a red closed TRAIL of length kL by concatenating the k successive lifts of W. These orbit trails are edge-disjoint and partition every red edge. For proof, W traverses each base edge e once and its 2^m lifted edges are reached bijectively as the starting fiber state varies; splitting starting states into return-permutation orbits partitions these lifts into trails. Thus every red closed trail in this decomposition has length at least m*2^(m-1), and there are at most 2^m trails. The blue return permutation is conjugate to sigma_R via tau when c is odd, so blue trails can be chosen as antipodal images of red trails, projecting onto the same W in Q_m. These trails need not be simple cycles because one orbit trail can revisit lifted vertices.

SWEEP IDENTIFICATION. The red lift of a base direction i updates its x part as U_i(x)=x XOR e_i if c_i(x)=0, otherwise U_i(x)=x. These are the original cube red edge-swap involutions. Thus sigma_R is their product in the direction word of the base Euler tour. Its orbit structure determines the Euler-lift trail lengths and counts, supplying a direct link between paired balance, Eulerian decomposition, and edge-swap monodromy. Eoin Long's separate minimum-degree theorem guarantees SIMPLE red and blue cycles of length at least 2^m, while the Euler lift construction guarantees an entire decomposition into potentially nonsimple closed trails of length at least m*2^(m-1). Neither statement alone yields a near-spanning direction-simple monochromatic path.

#### Folded-cube voltage obstruction to directed-cycle extraction

##### Folded-cube monodromy separates directed cycles from NORI1 rainbow cycles

Fix even \(N\ge4\) and write \(\widehat Q_N=Q_N/\langle\tau\rangle\), where \(\tau(v)=\bar v\). The quotient is an \(N\)-regular graph on \(2^{N-1}\) antipodal vertex pairs, with each edge marked by its original direction. A closed quotient walk \(W\) has a binary monodromy \(\nu(W)\): starting from a lift vertex \(x\), its lifted walk ends at \(x\) if \(\nu=0\), and at \(\bar x\) if \(\nu=1\).

**Theorem (rainbow-cycle voltage).** If a closed quotient walk uses every direction once, then it has length \(N\) and
\[
\boxed{\nu(W)=1.}
\tag{VM1}
\]
It lifts to a full antipodal geodesic in \(Q_N\). Conversely every full antipodal geodesic projects to such a direction-rainbow closed quotient walk. In a legal antipodally odd coloring, NORI1 asks for one whose lift from a suitable sheet is monochromatic.

*Proof.* Along a lifted quotient walk, taking an edge in direction \(i\) toggles bit \(i\). The product of its \(N\) distinct flips toggles all bits, sending \(x\) to \(\bar x\). Conversely an antipodal full geodesic uses every direction once and projects to a closed quotient walk. \(\square\)

**Theorem (zero voltage for directed 2-factor cycles).** For the antipodally paired directed 2-factorization (EF2), each constituent directed cycle projects to a closed quotient walk of monodromy zero. Paired directed cycles project onto the same zero-voltage quotient cycle. Thus no cycle lying wholly in a single canonical directed 2-factor can project to a direction-rainbow \(N\)-cycle.

*Proof.* The constituent directed cycles are already closed in \(Q_N\), so their projections have closed lifts and voltage zero. The antipodal mate projects onto the same quotient edge sequence, with reverse cyclic order. A rainbow \(N\)-cycle has voltage one by (VM1), precluding coincidence. \(\square\)

This is a topological obstruction to extracting NORI1 merely by choosing cycles inside the Eulerian 2-factorization. Obtaining a direction-rainbow antipodal loop requires altering the directed transition system, allowing a path to pass with and against arrows in alternation. The obstruction concerns constituent directed cycles, not arbitrary directed antipodal *open* paths: such open paths may project to voltage-one loops and are abundant in paired lifts.

#### Translation geodesic packing and short-cycle flip resilience

##### Exponential edge-transversal robustness of successful spectator lifts

Let \(c\) be any antipodally odd coloring of \(Q_m\) that has a monochromatic full antipodal geodesic. Let \(C\) be a legal spectator extension on \(Q_{m+k}\):
\[
C_i(x,y)=c_i(x)\quad(1\le i\le m),\qquad
C_{m+j}(x,y)=g_j(x)\quad(1\le j\le k),
\]
where each \(g_j(\bar x)=1\oplus g_j(x)\). As in the spectator-extension theorem, \(C\) has a monochromatic full antipodal geodesic \(P\), of some color \(\varepsilon\).

**Theorem (edge-transversal lower bound).** Let \(\mathcal P=\{P+t:t\in\mathbb F_2^k\}\) be its \(2^k\) dummy-bit translations. Then every original-direction edge belongs to at most one member of \(\mathcal P\), and every added-direction edge belongs to at most two members. Consequently:
\[
\boxed{\#\{Q\in\mathcal P:E(Q)\cap F\ne\varnothing\}\le2|F|}
\tag{ER1}
\]
for every edge set \(F\). If \(F\) is invariant under the antipodal involution, then
\[
\boxed{\#\{Q\in\mathcal P:E(Q)\cap F\ne\varnothing\}\le|F|.}
\tag{ER2}
\]
Thus any edge perturbation changing fewer than \(2^{k-1}\) edges preserves a monochromatic full geodesic of \(C\), whether or not it preserves legal oddness. Any *antipodally symmetric* perturbation changing fewer than \(2^k\) edges also preserves a monochromatic full geodesic.

*Proof.* Every rule of the extension ignores the new bits, so translating those bits preserves edge colors. A full geodesic uses each direction once. Translating an original-direction edge through all \(2^k\) added-bit states produces \(2^k\) distinct undirected edges, so a fixed old-direction edge lies on at most one translated path. Translating an added-direction \(j\)-edge has stabilizer \(\{0,e_j\}\), so a fixed added-direction edge lies on at most two translated paths. This proves (ER1).

If \(F\) is antipodally invariant, then every antipodal edge orbit inside \(F\) consists of one \(C\)-color-\(\varepsilon\) edge and one \(C\)-color-\((1-\varepsilon)\) edge. All paths in \(\mathcal P\) use only color \(\varepsilon\), so only \(|F|/2\) edges of \(F\) can meet them. Each such edge meets at most two paths, proving (ER2). If the right-hand count is smaller than \(2^k\), some translated monochromatic full geodesic avoids \(F\) and survives the perturbation. \(\square\)

**Corollary (paired-lift resistance to legal recoloring).** Let \(B(c)\) be the standard complementary paired lift of a successful legal \(Q_m\) coloring to the balanced \(Q_{2m}\). If \(d\) is any other legal antipodally odd coloring on \(Q_{2m}\) whose edge colors differ from \(B(c)\) on fewer than \(2^m\) edges, then \(d\) still satisfies NORI1. In particular every *balanced* counterexample would differ from \(B(c)\) on at least \(2^m\) edges, if such a counterexample existed.

**Corollary (short Eulerian cycle flips preserve success near a paired lift).** In the canonical Eulerian orientation of a successful paired lift \(B(c)\), reverse any directed simple cycle \(A\) and its antipodal mate, of common length \(\ell\). If
\[
\boxed{2\ell<2^m,}
\tag{ER3}
\]
then the flipped balanced legal coloring still has a monochromatic full antipodal geodesic.

*Proof.* The paired cycle flip changes \(2\ell\) edges and is antipodally symmetric; apply (ER2). \(\square\)

These results are conditional on success of the original base coloring, not a proof of unrestricted NORI1. Their significance for the Eulerian cycle-reconfiguration theorem is that a potential first counterexample cannot occur within an exponentially sized edge-Hamming neighborhood of any successful paired lift, and no individual short paired-cycle flip starting at such a lift can be the first failure.

**Theorem (translation-orbit intersection graph).** For the family \(\mathcal P=\{P+t:t\in\mathbb F_2^k\}\) from the preceding theorem, the intersection graph in which two distinct paths are adjacent when they share an undirected cube edge is precisely the standard \(k\)-cube: \(P+t\) and \(P+t'\) have a common edge if and only if
\[
\boxed{t\oplus t'=e_j\quad\text{for some }j\le k.}
\tag{ER4}
\]
In that case they share one edge, the one in new direction \(m+j\). Consequently the \(2^{k-1}\) paths indexed by even-parity translation vectors are pairwise edge-disjoint, and so are those indexed by odd-parity vectors. The antipodal images of either packing form a further \(2^{k-1}\) edge-disjoint full geodesics of the opposite color, disjoint from all paths of the chosen original-color packing. Hence a successful spectator extension contains an antipodally paired collection of
\[
\boxed{2^k\text{ pairwise edge-disjoint monochromatic full geodesics}}
\tag{ER5}
\]
when both colors are counted.

*Proof.* Paths with different translations cannot share an original-direction edge: its whole new-bit state changes with the translation vector. A new-direction \(j\)-edge has stabilizer consisting of the identity and the translation \(e_j\), and each full geodesic contains just one such edge. Thus two different paths intersect precisely when their translation vectors differ in that single bit, proving (ER4). No two vectors of the same parity differ in one bit, yielding the two edge-disjoint packings. All paths in the chosen packing are of the same color, whereas their antipodal images are of the opposite color; opposite-color paths cannot share edges. The antipodal map preserves disjointness within the second packing, yielding (ER5). \(\square\)

**Corollary (exponential distance in the Eulerian square-flip reconfiguration graph).** Let \(B(c)\) be a successful complementary paired lift on \(Q_{2m}\), where \(m\ge4\). Any sequence of antipodal directed-square flips starting at \(B(c)\) that ends in a legal counterexample, if such a sequence exists, requires at least
\[
\boxed{2^{m-3}}
\tag{ER6}
\]
flips. More generally, if each allowed flip consists of two antipodal directed cycles of at most \(\lambda\) edges each, at least \(\lceil2^{m-1}/\lambda\rceil\) such flips are needed.

*Proof.* The paired square flip changes eight edges. After \(t\) flips, the final coloring disagrees with the starting lift on at most \(8t\) edges, irrespective of cancellations. The preceding antipodal robustness theorem requires at least \(2^m\) changed edges for a bad final coloring. Hence \(8t\ge2^m\). The same reasoning applies to paired cycles of length at most \(\lambda\), for which one flip changes at most \(2\lambda\) edges. \(\square\)

The packing formulation makes the robustness theorem a direct edge-disjoint-path statement rather than just a probability calculation. The exponential lower bound concerns local reconfiguration from a successful paired lift; it does not claim that counterexamples exist or that a square-flip path to them exists.


#### Six-cycle barrier to square-only monotone descent

##### Antipodal directed hexagons give strict local minima for square-only descent

Work in \(Q_6\), with original bits \(x_0,x_1,x_2\), dummy bits \(y_0,y_1,y_2\), and direction indices \(0,1,2,3,4,5\). Define the legal balanced coloring \(a\) by
\[
a_i(x,y)=x_{i+1\pmod3},\qquad
a_{3+i}(x,y)=1\oplus x_{i+1\pmod3}\quad(0\le i<3).
\tag{HX1}
\]
This is the complementary paired lift of the unary cycle \(c_i=x_{i+1\pmod3}\) on \(Q_3\).

**Theorem (six-cycle obstruction to monotone square descent).** Let \(C\) be the directed six-cycle in the canonical orientation of \(a\), beginning at \(v=(x,y)=(001,000)\) when \(x_0\) is the low-order bit, with direction word
\[
\boxed{(2,0,1,2,0,1).}
\tag{HX2}
\]
Let \(b\) be obtained from \(a\) by reversing the edge colors on the twelve-edge set \(F=E(C)\cup E(\tau C)\), where \(\tau(x,y)=(\bar x,\bar y)\). Then \(b\) remains perfectly balanced and antipodally odd and differs from \(a\) on twelve edges, four in each original direction and none in dummy directions. However, every legal antipodal directed-square flip of \(a\) increases its edge-disagreement distance to \(b\) from twelve to at least sixteen. Consequently the strictly decreasing paired-cycle descent theorem cannot in general be implemented using directed square flips alone.

*Proof.* Vertex balance and antipodal oddness of \(a\) follow from the complementary paired rules (HX1). Starting at integer \(x=1\) with \(y=0\), the cycle (HX2) runs through the distinct old vertices
\[
1\to5\to4\to6\to2\to3\to1,
\]
all with dummy state \(y=000\). Its edge colors are \(1,0,1,0,1,0\), respectively. The starting vertex has odd parity, so these colors are precisely the outward arrows of the canonical orientation at their successive tails; \(C\) is directed. Its antipodal mate lies in the disjoint face \(y=111\) and is directed with reversed cyclic order. Flipping the two directed cycles preserves indegree and outdegree at all vertices and maintains the antipodal relation, so \(b\) is balanced and legal. Each of directions \(0,1,2\) occurs twice in \(C\) and twice in \(\tau C\), proving the disagreement counts.

There are no directed squares using only two original directions. Indeed, among any two distinct original indices \(i,j\), one is the cyclic successor of the other; hence one of the edge rules \(a_i=x_{i+1}\), \(a_j=x_{j+1}\) changes when the other bit is flipped. Its two opposite edges around that square have different colors. A directed square in the canonical orientation would instead need its two opposite edges to have the same color (the square colors must alternate cyclically). Thus each directed square uses at least one dummy direction.

The disagreement set \(F\) consists solely of original-direction edges contained in the two opposite fixed-dummy facets \(y=000\) and \(y=111\). A square involving a dummy direction contains at most one original-direction edge in either one of these facets, and it cannot meet both facets, whose dummy states differ in three bits. Hence every directed square shares at most one edge with \(F\), and every antipodal pair of directed squares shares at most two edges with \(F\).

Each permitted paired-square flip toggles eight distinct edges. If \(h\le2\) of them already disagree with \(b\), the new disagreement count is
\[
12+8-2h\ge16.
\]
Therefore no such flip decreases, or even preserves, the disagreement potential. Reversing the antipodal pair of directed hexagons transforms \(a\) into \(b\) in one legal cycle operation. \(\square\)

**Scope.** Both colorings are legal balanced cubes of dimension six; neither is asserted to be bad for NORI1. This is a rigorous barrier to a specific proof strategy: monotone descent toward an arbitrary balanced target under *square-only* directed-cycle flips. The general antipodal directed-cycle reconfiguration theorem remains valid.

**Extension to every even dimension at least six.** Let \(N=2m\ge6\). On \(Q_m\) take the legal coloring \(c_0=x_1,c_1=x_2,c_2=x_0\), and \(c_i=x_0\) for \(3\le i<m\). Let \(a\) be its standard complementary paired lift to \(Q_{2m}\). In the three-face where all bits except original dimensions \(0,1,2\) are zero, the closed word \((2,0,1,2,0,1)\) from the vertex with \(x_0=1\) is a directed hexagon. Recolor that hexagon and its antipodal directed mate to obtain \(b\). It is balanced and odd and differs from \(a\) on twelve edges.

Every original pair of directions from \(\{0,1,2\}\) includes a rule that reads the other bit, so no square using two such directions is directed. All changed edges lie in the selected three-face and its antipodal face, whose fixed exterior bits differ in \(N-3\ge3\) positions. Any other square has at least one exterior direction, intersects either of these three-faces in at most one core edge, and cannot meet both. Thus an antipodal directed-square pair intersects the disagreement set in at most two edges. Flipping any such square pair changes eight edges and increases disagreement from twelve to at least sixteen. This proves the strict monotone-square-descent obstruction in every even dimension \(N\ge6\), while reversing the hexagon pair reaches \(b\) in one step.

#### Gray-monodromy parity and quarter-fiber fixed-point theorem

PARITY OBSTRUCTION TO A SINGLE LIFTED HAMILTON CYCLE. Let H be ANY Hamilton cycle in the base Q_m, with direction word w. Every base direction occurs an even number of times in this closed walk. The return permutation sigma_R equals the word in red edge-swap involutions U_i acting on the 2^m possible x-states. A product of involutions in which each generator occurs an even number of times has even permutation sign. Hence sigma_R belongs to the alternating group A_(2^m). For m>=2, 2^m is even; a permutation on 2^m points is even if and only if it has an even number of permutation cycles. Therefore the red preimage 2-factor of ANY base Hamilton cycle has an even number of constituent simple cycles, in particular at least two. The blue one has the same count. A Hamilton cycle in the upstairs red subgraph cannot arise by lifting just one Hamilton cycle of the base.

QUARTER-FIBER FIXED POINT THEOREM FOR THE REFLECTED GRAY CYCLE. Assume c is antipodally odd and m>=2. Take the standard cyclic binary-reflected Gray Hamilton cycle H_m in Q_m, with direction word (A,m-1,A,m-1), where A is the palindromic direction word of the binary-reflected Gray Hamilton PATH in Q_(m-1). The return permutation has the form sigma_R=(U_(m-1) P)^2, where P is the word of edge-swap involutions U_i given by A. Since A is an odd-length palindrome, P is conjugate to its central single-letter involution U_(m-2). Each U_i exchanges the 2^(m-2) red edges of direction i in the input odd Q_m coloring; it is therefore a product of q=2^(m-2) disjoint transpositions and fixes the other 2q of the 4q=2^m vertices. The same is true of P by conjugacy.

TWO-MATCHING LEMMA. If U,V are involutions on 4q points, each consisting of q disjoint transpositions, then (UV)^2 fixes at least q points. To prove this, take the multigraph whose edges are the transpositions of U and V, retaining duplicates. It has 4q vertices and 2q edges, with every component a path or a cycle (parallel edges permitted). Components on one or two vertices are fixed pointwise by (UV)^2: there both involutions are either the identity or the same transposition. Every connected component with v>=3 vertices has at least v-1>=2v/3 edges. Thus all components with at least three vertices contain together at most (3/2)*2q=3q vertices. The remaining at least q vertices lie in size-one or size-two components, where (UV)^2 is the identity.

Apply this to U=U_(m-1) and V=P. Thus sigma_R has at least 2^(m-2) fixed points. Each fixed point over a selected base root produces a simple red cycle in the lifted 2-factor projecting ONCE around H_m, of length 2^m. Such cycles are vertex-disjoint. Their total vertex count is at least 2^(m-2)*2^m=2^(2m-2), one quarter of the entire Q_(2m). The blue 2-factor contains their antipodal images, also simple cycles of length 2^m. This is valid for EVERY antipodally odd input coloring, with arbitrary nonlinear rules and no fixed-point or geodesic hypothesis.

FINITE AUDIT. For the Gray direction words m=2,3,4,5, random antipodally odd input colorings were checked by composing the red U_i permutations on every fiber state; in sample sizes 40,5000,5000,500 respectively, all return permutations had even numbers of cycles and at least 2^(m-2) fixed points. For m=2 the orbit partition was always 1+3; for m=3 the observed types were 1+1+1+1+2+2 and 1+1+3+3. The analytic proof does not rely on these samples.

#### The Gray cycle-factor rainbow obstruction and doubled-direction loops

GRAY 2-FACTOR GEODESIC INVISIBILITY. Assume m>=3, hence 2m<2^m. Every monochromatic full antipodal geodesic of the paired lift traverses both members of each direction pair. Its projection pi(x,y)=x XOR y therefore is a CLOSED 2m-edge walk in Q_m, with each base direction used twice. But every simple path in the red 2-factor obtained by pulling back a Hamilton cycle H of Q_m projects to a nonbacktracking arc along H. An arc of 2m<2^m edges cannot return to its initial base vertex. Therefore this red 2-factor, despite covering every vertex by cycles of length >=2^m, contains NO full monochromatic antipodal geodesic; the same applies to its blue antipodal partner.

UNIFORM FIVE-STEP RAINBOW LIMIT FOR THE REFLECTED GRAY FACTOR. In the standard binary-reflected Gray Hamilton cycle H_m, base direction 0 occurs every other step. Any six consecutive lifted red edges therefore include THREE steps from paired directions {0,m}. There are only two possible lifted directions in this pair, forcing repetition. Thus every direction-simple contiguous arc of every red Gray-factor cycle, and similarly blue, has length at most FIVE, independently of m. This is compatible with all cycles having lengths >=2^m and with at least 2^(m-2) of them each having length 2^m. Exponential simple cycle lengths alone give no nontrivial lower bound on longest rainbow arc inside these particular cycle factors.

DOUBLE-RAINBOW BASE LOOP CHARACTERIZATION. Full red antipodal geodesics in the paired lift correspond precisely to red lifts of closed 2m-edge base walks whose direction words use each of the m base directions twice, with the two corresponding lifted edges drawn from opposite members of each paired direction. Forward direction is projection. Conversely, such a lifted walk uses all 2m distinct cube directions once and hence joins antipodes. A successful Eulerian method needs to create these SHORT doubled-direction base loops with consistent red lifts, rather than only long cyclic tours of the base.

##### Directed hexagon traps with exponentially many changed edges

**Exponentially extensive trap for square-only descent.** For every even \(N=6+2k\ge8\) there are perfectly balanced antipodally odd colorings \(a,b\) with
\[
\boxed{|\{e:a(e)\ne b(e)\}|=12\cdot2^{2k-1}=6\cdot2^{N-6}}
\tag{HX3}
\]
such that every antipodal directed-square flip of \(a\) increases its edge-disagreement distance to \(b\) by at least four.

*Construction and proof.* Start from the six-dimensional coloring \(a^{(6)}\) in (HX1). Adjoin \(2k\) spectator directions in complementary pairs, with rules
\[
a_{6+2j}(x,y,z)=x_0,\qquad
a_{7+2j}(x,y,z)=1\oplus x_0\quad(0\le j<k).
\]
The old six edge rules ignore the new \(z\)-bits. The enlarged coloring remains legal and balanced because each added pair contributes one edge of each color at every vertex.

Let \(C\) and \(\tau_6 C\) be the two directed hexagons from the six-cube construction, regarded in the \(Q_6\) factor. For each spectator state \(z\in Q_{2k}\) of even Hamming parity, include *both* six-cycles \(C\times\{z\}\) and \(\tau_6 C\times\{z\}\) in a set \(F\). They are directed because the spectator parity is even, and no two cycles share an edge. Since \(2k\) is even, antipodal complementation preserves the parity of the spectator state, and exchanges the two hexagon types; thus \(F\) is antipodally invariant. There are \(2^{2k-1}\) selected states and twelve edges per state, giving (HX3). Flip all edges of \(F\) to obtain \(b\); each flipped directed cycle preserves balance, and antipodal invariance preserves legal oddness.

Every directed square of the original \(Q_6\) coloring intersects \(E(C)\cup E(\tau_6 C)\) in at most one edge, as proved above. Thus a directed square entirely in old directions meets \(F\) in at most one edge, occurring only at an even spectator state. A square using one old and one spectator direction has two old parallel edges at spectator states of opposite parity; at most one lies in \(F\). A square in two spectator directions meets no changed edge. Therefore *every* directed square in the enlarged cube meets \(F\) in at most one edge, and its antipodal partner in at most one additional edge. A paired-square flip toggles eight edges with at most two already disagreeing, so changes distance by \(8-2h\ge4\).

The construction provides strict local minima for the square-flip disagreement potential at exponentially large disagreement distance. It does not imply any of the constructed colorings is bad for NORI1; it is a method obstruction for monotone square-only reconfiguration.

Finite checks for \(N=8,10\) verified both legal balanced colorings and the bound of one disagreement edge per directed square, with disagreement counts \(24\) and \(96\), respectively.

##### Red swap commutators and influence-curvature identity

##### Red edge-swap commutators are the undirected influence graph

Let \(c\) be a legal antipodally odd edge coloring on \(Q_m\). Define \(U_i(x)=x+e_i\) when \(c_i(x)=0\), and \(U_i(x)=x\) when \(c_i(x)=1\). Each \(U_i\) is an involution. The directed influence graph has arc \(j\to i\) when \(\partial_j c_i\) is nonzero somewhere.

**Theorem (commutator-influence identity).** For all different directions \(i,j\),
\[
\boxed{U_iU_j=U_jU_i
\iff \partial_j c_i\equiv0\ \text{and}\ \partial_i c_j\equiv0.}
\tag{CM1}
\]
Hence the undirected noncommutation graph of the red edge-swap involutions is obtained by forgetting arc orientations in the directed influence graph. It has no isolated vertices.

*Proof.* If the two derivatives vanish, swapping along a red edge of direction \(i\) cannot change the red/blue status of direction \(j\), and conversely. The conditional flips consequently commute.

If \(\partial_j c_i\) is nonzero, choose a direction-\(j\) edge across which the \(i\)-edge color changes. One of that edge and its antipodal mate is red, and the derivative is nonzero on both mates by antipodal oddness. Let \(u,u+e_j\) be the red member. Then \(U_j(u)=u+e_j\), while one of \(U_i(u)\), \(U_i(u+e_j)\) is the identity operation at its argument and the other flips bit \(i\). It follows immediately by comparing the \(i\)-th output bit of \(U_iU_j(u)\) and \(U_jU_i(u)\) that these two compositions differ. If instead \(\partial_i c_j\) is nonzero, interchange the roles of \(i,j\). This proves (CM1). Every direction rule \(c_i\) is independent of bit \(i\) but changes under the full antipodal flip, so it depends on at least one other bit \(j\). The associated edge-swap pair does not commute, proving that every vertex has a noncommuting neighbor. \(\square\)

**Corollary (nonflat covering curvature).** In the red covering \(\pi(x,y)=x+y\) of \(Q_m\) furnished by the complementary paired lift, the fiber return permutation for a base square with direction word \((i,j,i,j)\) is
\[
\boxed{K_{ij}=(U_jU_i)^2.}
\tag{CM2}
\]
Since both swaps are involutions, \(K_{ij}\ne\mathrm{id}\) if and only if at least one of \(i\to j\) and \(j\to i\) belongs to the influence graph. Every legal odd coloring therefore produces nontrivial red-cover holonomy around some base square.

*Proof.* Each red lift of a base direction \(i\) updates the old-bit fiber by \(U_i\); compose the four updates. The product squared is the identity if and only if the two involutions commute. Apply (CM1). \(\square\)

Nontrivial curvature is automatic, but it does not force the antipodal fiber monodromy along a direction-double-occurrence loop required for NORI1.

#### Fourier energy counts local square holonomy

##### Fourier energy identity for square holonomy

Let \(n\ge3\) and \(c\) be any legal antipodally odd edge coloring of \(Q_n\). Let \(A_2\) denote the number of square faces whose cyclic edge colors have two transitions, and let \(T\) denote the number of square faces containing two *adjacent* red edges. Define \(H\) as the number of square faces on which the red edge-swap involutions \(U_i,U_j\), restricted to that face, do not commute. Write \(\operatorname{Inf}_j(c_i)=\Pr_x[c_i(x)\ne c_i(x\oplus e_j)]\).

**Theorem (square holonomy and Fourier influence).**
\[
\boxed{A_2+T=2^{n-2}\sum_{i}\sum_{j\ne i}\operatorname{Inf}_j(c_i),\qquad
H=\frac{A_2+T}{2}=2^{n-3}\sum_i\sum_{j\ne i}\operatorname{Inf}_j(c_i).}
\tag{HE1}
\]
Thus
\[
\boxed{A_2\ge n2^{n-3},\qquad H\ge n2^{n-3}.}
\tag{HE2}
\]
If \(s_i(x)=(-1)^{c_i(x)}\), and \(\widehat s_i(S)\) denotes its Walsh-Fourier coefficients, then
\[
\boxed{H-n2^{n-3}
=2^{n-3}\sum_i\sum_{\substack{S\subseteq[n]\setminus\{i\}\\ |S|\ge3\ {\rm odd}}}(|S|-1)\widehat s_i(S)^2.}
\tag{HE3}
\]

*Proof.* Fix a square in directions \(i,j\), and let \(a=\partial_jc_i\) and \(b=\partial_ic_j\) there. Because each rule ignores its own direction bit, these derivative indicators are constant on the square. If \(a=b=0\), the boundary has zero or four cyclic color transitions. If one of \(a,b\) is one, the boundary has two transitions with one or three red edges. If both are one, the boundary has two transitions with two adjacent red edges. Thus each face contributes \(a+b\) to \(A_2+T\). Averaging over its \(2^{n-2}\) possible translates and summing direction pairs gives the first identity.

The restricted red swaps commute when the square red graph has zero, one, four or two opposite edges. They fail to commute when it is a two-edge path (red pair adjacent; product of swaps a 3-cycle) or a three-edge path (product of swaps a 4-cycle). Antipodal translation sends each face to a different face and complements all four colors. In particular, it pairs every one-red face with a three-red face, while adjacent-two-red faces pair with the same type. Therefore \(H=T+(A_2-T)/2\), proving the second identity.

Each signed rule \(s_i\) has mean zero by antipodal oddness, ignores bit \(i\), and has Fourier support only on odd-size sets. Parseval and the Boolean total-influence formula give
\[
\sum_{j\ne i}\operatorname{Inf}_j(c_i)=\sum_{S\ {\rm odd}}|S|\widehat s_i(S)^2\ge\sum_S\widehat s_i(S)^2=1.
\]
Substitute into (HE1) to obtain the \(H\)-bound. Since \(T\le A_2\), the \(A_2\)-bound follows. Subtract the degree-one Fourier contribution from the \(H\)-formula to get (HE3). \(\square\)

**Equality cases.** Equality \(H=n2^{n-3}\) holds if and only if every direction rule is unary: \(c_i=x_{r(i)}\oplus\epsilon_i\), with \(r(i)\ne i\). Indeed equality in the Fourier influence bound forces all Fourier mass onto singletons; a Boolean-valued linear combination of singleton characters can have only one nonzero coefficient, by squaring and comparing cross terms. Equality \(A_2=n2^{n-3}\) further forces \(r(i)=j\) if and only if \(r(j)=i\), so \(r\) is a fixed-point-free involution and the directions split into mutual-reader pairs. Such a coloring cannot be vertex-balanced: flipping any input bit changes just one of the incident edge colors. Consequently a perfectly balanced legal coloring satisfies \(A_2>n2^{n-3}\).

**Audit.** Independent random legal odd colorings in dimensions 3 through 7 were checked by enumerating all squares and their restricted red-swap commutators. Their counts satisfied (HE1). The proof is dimension-uniform and imposes no bounds on nonlinear rules.

#### Chord interlacement and factorization of doubled-direction holonomy

##### Crossing-commutator factorization for doubled-direction holonomy

Let \(U_i\) be the red edge-swap involutions of a legal antipodally odd coloring of \(Q_n\), and let \(w\) be any word of length \(2n\) in which each direction occurs twice. Define its chord-interlacement graph \(J(w)\) by joining \(i,j\) if their occurrences alternate \(i\,j\,i\,j\) or \(j\,i\,j\,i\). Let \(r_c(w)\) be the number of such crossing pairs for which the two red involutions fail to commute. By the commutator-influence theorem above, these are crossing pairs linked by at least one directed influence arc.

**Theorem (holonomy is transported square curvature).** The red return permutation
\[
U_w=U_{w_{2n}}\cdots U_{w_1}
\]
is a product of at most \(r_c(w)\) conjugates of square commutators
\[
K_{ij}=(U_jU_i)^2.
\tag{CW1}
\]
In particular
\[
\boxed{r_c(w)=0\implies U_w=\mathrm{id}.}
\tag{CW2}
\]
When \(r_c(w)=1\), the entire return permutation is conjugate to a single square commutator or its inverse.

*Proof.* Choose in a nonempty double-occurrence word a letter \(i\) whose two appearances are closest together. Every intervening letter \(j\) appears once between these two copies: if it appeared twice, its appearances would have smaller separation. Therefore each intervening \(j\) crosses \(i\) in the chord diagram. Move the later \(i\) across all the intervening letters to make the two \(i\)'s adjacent, then cancel them by \(U_i^2=\mathrm{id}\). This uses one adjacent swap for each current interlacement neighbor of \(i\). The relative order and interlacement relations among all remaining letters are unchanged by deleting both copies of \(i\). Repeating reduces the word to empty and uses one swap for every interlacement edge of the original chord graph, with no swaps of noncrossing pairs.

For two involutions \(A,B\) one has \(AB=(AB)^2BA\). Hence replacing an adjacent \(AB\) by \(BA\) introduces a conjugated commutator factor \((AB)^2\) in the full word product. If \(A,B\) commute, this factor is the identity. Tracking the described reductions proves the claimed product of at most \(r_c(w)\) nontrivial commutator conjugates. \(\square\)

**Corollary (crossing curvature is necessary).** A doubled-direction word whose red lift is a monochromatic antipodal geodesic must have a crossing pair \(i,j\) with noncommuting red swaps: otherwise its return map is the identity and cannot take a fiber state \(x\) to \(\bar x\).

**Theorem (independent-component crossing lower bound).** If the undirected influence graph of \(c\) has \(h\) connected components, every red doubled-direction word with antipodal return has
\[
\boxed{r_c(w)\ge h.}
\tag{CW3}
\]

*Proof.* Every direction rule depends only on vertex bits in its own undirected influence component. Thus the red swaps act independently on the corresponding blocks. Restrict the word to the letters in one block; each block letter still appears twice. If there is no noncommuting crossing inside this subword, the factorization theorem makes its return map the identity on that block, whereas antipodal return must flip every bit of the block. Each block therefore contributes at least one distinct noncommuting crossing. \(\square\)

**Sharpness in arbitrarily many components.** For \(n=2h\), take the Cartesian product of \(h\) legal odd \(Q_2\) colorings
\[
c_{2a}(x)=x_{2a+1},\qquad c_{2a+1}(x)=x_{2a},
\quad 0\le a<h.
\tag{CW4}
\]
The influence graph has \(h\) disjoint two-vertex components. Each four-letter word \((2a,2a+1,2a,2a+1)\) has antipodal red return on its two-bit block from the root whose bits in those directions are \((0,1)\). Concatenating the \(h\) words yields an antipodal doubled-direction red return with \(h\) crossing pairs, attaining (CW3). The standard paired lift of this legal coloring produces a perfectly balanced cube on \(Q_{4h}\).

**Finite audit.** Exhaustive enumeration of the 64 legal odd \(Q_3\) colorings found 16 that have no antipodal-return word with a single interlacing pair. Exhausting all 65,536 legal odd \(Q_4\) colorings found 3,856 without such a word. The complete double-occurrence holonomy criterion remains satisfied in these dimensions. The enumeration shows that a single transported square commutator is not universally sufficient, and the independent-product theorem shows no fixed bound on the number of required square commutators can suffice in all dimensions.

The factorization locates the algebraic source of every successful doubled-direction return in transported square curvature. What remains open is how to combine enough such local factors to move a fiber state antipodally while traversing every base direction only twice.

##### Influence cones of chord-diagram square curvature

##### Directed influence cones of interlacement curvature

Continue with the doubled-direction word \(w\), red swaps \(U_i\), its set \(C(w)\) of directions appearing in a noncommuting interlacement pair, and the directed influence graph \(D(c)\), whose arc \(i\to j\) means that the rule \(c_j\) reads bit \(i\). Define the forward influence closure \(A=\operatorname{Reach}^+_{D(c)}(C(w))\).

**Theorem (influence-cone necessary condition).** For every starting fiber state \(x\in Q_n\), the red return map \(U_w\) preserves every bit outside \(A\):
\[
\boxed{\pi_{[n]\setminus A}U_w(x)=\pi_{[n]\setminus A}(x).}
\tag{IC1}
\]
Consequently any doubled-direction word with antipodal return \(U_w(x)=\bar x\) must satisfy
\[
\boxed{\operatorname{Reach}^+_{D(c)}(C(w))=[n].}
\tag{IC2}
\]

*Proof.* By the crossing-commutator factorization, \(U_w\) is a product of conjugates of commutators \(K_{ij}=(U_jU_i)^2\), each with both \(i,j\in C(w)\subseteq A\). Write \(T=[n]\setminus A\). As \(A\) is forward-closed under directed influence, no rule indexed by \(T\) reads a vertex bit belonging to \(A\). Therefore projection onto \(T\) intertwines every full red swap \(U_k\) with the corresponding swap on \(Q_T\) when \(k\in T\), and with the identity when \(k\in A\). This property extends to their inverses, products and conjugates. In particular each square commutator \(K_{ij}\) with \(i,j\in A\) and every conjugate of it acts trivially after projection onto \(T\). So does their product \(U_w\). This proves (IC1), and (IC2) follows because an antipodal displacement changes every vertex bit. \(\square\)

**Theorem (source-component curvature requirement).** Let \(S_1,\ldots,S_h\) be the source strongly connected components of \(D(c)\). If \(U_w(x)=\bar x\), then for every \(a\), the chord diagram \(J(w)\) has a crossing edge \(\{i,j\}\) lying entirely in \(S_a\) and satisfying \(U_iU_j\ne U_jU_i\). Consequently
\[
\boxed{r_c(w)\ge h.}
\tag{IC3}
\]

*Proof.* A source SCC \(S_a\) receives no influence arcs from outside, so each rule indexed in \(S_a\) depends only on its own SCC bits. Projecting the red swap sequence onto \(S_a\) deletes all letters outside \(S_a\) and preserves the original action on its bits. The projected double-occurrence word must send the projected start state to its bitwise complement. If it had no noncommuting interlacement pair, the crossing factorization theorem would make its return the identity, a contradiction. Different source SCCs are disjoint, and crossing status of pairs within one SCC is not affected by deleting the other labels. Thus the required crossings are distinct, proving (IC3). \(\square\)

**Sharpness.** The direct product of \(h\) legal reciprocal-reader two-cubes in (CW4) has \(h\) source SCCs and admits an antipodal doubled-direction return with \(h\) crossing pairs. Thus (IC3) is tight for arbitrarily large \(n=2h\), and the standard paired lift gives balanced examples on \(Q_{4h}\).

This improves the earlier weak-component lower bound to the source-SCC count and gives a geometric necessary coverage criterion (IC2). It is compatible with a strongly connected influence graph having a single interlacement-curvature seed; such a seed being sufficient is not claimed.

##### A single crossing requires simultaneous mutual square sensitivity

##### Single-crossing antipodal holonomy requires a mutual square bridge

Let \(c\) be a legal odd coloring of \(Q_n\), \(n\ge3\), and let \(w\) use every direction twice with just one pair \(i,j\) whose occurrences interlace. If the red return \(U_w\) sends some \(x\) to \(\bar x\), then
\[
\boxed{w=(v,i,j,i,j,\operatorname{rev}v)}
\tag{OC1}
\]
after possibly exchanging \(i,j\), where \(v\) is a permutation of the remaining \(n-2\) directions.

*Proof.* Every other chord avoids crossing the two core chords and all other noncore chords. A noncore chord is therefore either nested around the entire crossing core or confined to a gap between core appearances. All gap-confined chords form noncrossing subwords and cancel by successive adjacent double-letter cancellations, using \(U_k^2=1\). A canceled direction \(k\) can never be changed by the total return map, since only \(U_k\) updates bit \(k\), contradicting antipodal return. All noncore chords must therefore surround the core, nested in reverse order. This proves (OC1). \(\square\)

Let \(S=U_{v_{n-2}}\cdots U_{v_1}\) be the red sweep of those exterior directions, and \(K_{ij}=(U_jU_i)^2\). Then \(U_w=S^{-1}K_{ij}S\).

**Theorem (two-direction bridge and synchronized exterior).** The word (OC1) sends \(x\) to \(\bar x\) if and only if
\[
\boxed{K_{ij}(S(x))=S(\bar x).}
\tag{OC2}
\]
When (OC2) holds, the two states \(S(x),S(\bar x)\) have the same bits in all \(n-2\) exterior directions and opposite bits in \(i,j\). Each of the \(n-2\) swap operations constituting \(S\), applied simultaneously to the two initially antipodal states, must decrease their Hamming separation by one. The visited \(i,j\) face has simultaneous directional sensitivity
\[
\boxed{\partial_jc_i=\partial_ic_j=1,}
\tag{OC3}
\]
and the restricted red commutator is a three-cycle taking the indicated opposite corners into one another.

*Proof.* The equivalence (OC2) follows by rearranging \(U_w=S^{-1}K_{ij}S\). The commutator only affects bits \(i,j\), while the sweep \(S\) touches neither, so (OC2) forces the stated final Hamming separation to be two. Every \(U_k\) changes just bit \(k\), and therefore changes the distance between any two inputs by at most one. The initial pair has distance \(n\); after \(n-2\) swaps it has distance two. Every swap must decrease the distance by one, synchronizing the corresponding exterior bit. A square commutator that takes two opposite corners into one another can only occur on a square with two adjacent red edges. With three red edges its commutator flips at most one bit; with zero, one, four or two opposite red edges it is trivial. The two-adjacent-red case has both transverse derivatives one and yields the stated three-cycle. \(\square\)

**Corollary.** If the directed influence graph has no reciprocal pair \(i\leftrightarrow j\), no double-occurrence antipodal-return word has only one crossing pair. This includes arbitrarily large strongly connected directed reader cycles with unary rules. In fact a single-crossing return requires two simultaneous nonzero derivatives on one square, a stronger requirement than mutual influence somewhere in the cube.

The condition does not exclude successful words with several crossing pairs. It shows that one transported square commutator cannot serve as a universal holonomy proof: beyond the mutual-curvature face, its exterior sweep must synchronize every other bit of an antipodal pair.

#### Even-generator holonomy and the antipodal-path metric

Let \(c\) be an antipodally odd edge coloring of \(Q_n\), \(n\ge2\), and \(U_i\) its red edge-swap involutions. A word in these involutions is *even* if each direction occurs an even number of times. Define \(\ell_R(x)\) as the minimum length of a red path from \(x\) to \(\bar x\), and \(\mu_R(x)\) as the minimum length of an even word \(w\) with \(U_w(x)=\bar x\). Use value \(\infty\) when the corresponding set is empty.

**Theorem (rootwise even-holonomy metric).** For every \(x\),
\[
\boxed{\mu_R(x)=n+\ell_R(x).}\tag{EH1}
\]
If \(\ell_R(x)<\infty\), an attaining word exists whose moving updates follow a shortest red antipodal path and whose \(n\) stationary updates occur only at the initial or terminal vertex, once per direction. Its length is at least \(2n\); equality holds precisely when it uses every direction twice and its moving updates form a red antipodal geodesic.

*Proof.* In an even word sending \(x\) to \(\bar x\), let \(a_i\) and \(b_i\) count moving and stationary occurrences of \(U_i\). The endpoint condition implies \(a_i\equiv1\pmod2\), and evenness gives \(b_i\equiv1\pmod2\), hence \(b_i\ge1\). Deleting stationary updates leaves a red antipodal walk, so
\[
|w|=\sum_i(a_i+b_i)\ge\ell_R(x)+n.
\]
If no red antipodal path exists, no even antipodal-return word exists.

Conversely take a shortest red antipodal path \(P\) starting at \(x\). Every direction occurs an odd number of times on \(P\). Antipodal oddness implies \(c_i(\bar x)=1-c_i(x)\), so \(U_i\) fixes precisely one of the two vertices \(x,\bar x\). Insert one stationary \(U_i\) at the beginning of \(P\) if it fixes \(x\), and at the end otherwise. Multiple inserted updates at an endpoint remain stationary. This yields an even word of length \(\ell_R(x)+n\). Finally every antipodal walk has at least \(n\) moving steps; when the total even-word length is \(2n\), each \(a_i=b_i=1\), proving the remaining assertions. \(\square\)

Let \(G_c=\langle U_1,\ldots,U_n\rangle\le\operatorname{Sym}(Q_n)\), with commutator subgroup \(G_c'\).

**Corollary (transported square curvature has an antipodal orbit).** For every root \(x\),
\[
\boxed{\bar x\in G_c'x\iff x,\bar x\text{ belong to one red connected component}.}\tag{EH2}
\]
In particular, for every antipodally odd coloring there is some \(x\) and some product of conjugates of square commutators \(K_{ij}=(U_jU_i)^2\) taking \(x\) to \(\bar x\).

*Proof.* In the free product \(F=*_{i=1}^n C_2\), abelianization records generator-occurrence parity. Hence its derived group \(F'\) consists of even words. The map \(s_i\mapsto U_i\) sends \(F'\) onto \(G_c'\); (EH1) now proves the equivalence. The normal closure in \(F\) of the elementary commutators \([s_i,s_j]=(s_is_j)^2\) is \(F'\), so \(G_c'\) is normally generated by the \(K_{ij}\). The established monochromatic antipodal-path theorem of Wu and Yang gives a monochromatic antipodal path for every legal coloring, and antipodal reflection changes its color; hence some red antipodal path exists. \(\square\)

**Sharp metric obstruction.** Set \(\ell_R=\min_x\ell_R(x)\), finite by the antipodal-path theorem, and \(\delta_R=(\ell_R-n)/2\). Then
\[
\boxed{\min_x\mu_R(x)=2n+2\delta_R.}\tag{EH3}
\]
Consequently global transported square curvature always admits an antipodal orbit. The unrestricted NORI1 problem is the removal of the nonnegative length surplus \(2\delta_R\), equivalently obtaining an even return word with two uses of every direction. No bound on the surplus follows from the group-orbit assertion alone.


#### Derived-group orbits and the optimal even-return budget

Let \(c\) be an undirected binary coloring of \(Q_n\), \(U_i\) its red edge-swap involutions, \(G=\langle U_1,\ldots,U_n\rangle\), and \(G'=[G,G]\). For a red connected component \(C\), set
\[
I(C)=\{i:\exists v\in C,\ c_i(v)=1\}.
\]

**Theorem (commutator-orbit classification).** If \(x,y\in C\), then
\[
\boxed{y\in G'x\ \Longleftrightarrow\
\operatorname{supp}(x\oplus y)\subseteq I(C).}\tag{DG1}
\]
In particular, if the coloring is antipodally odd and \(C\) contains antipodal vertices, then \(G'\) acts transitively on \(C\).

*Proof.* Let \(F=\ast_{i=1}^n\mathbb Z_2\) act via generators \(s_i\mapsto U_i\), and let \(\varepsilon:F\to\mathbb F_2^n\) record each generator's occurrence parity. Its kernel is \(F'\), and the image of \(F'\) is \(G'\). A word taking \(x\) to \(y\) traces a walk in \(C\). Each \(s_i\) either traverses a red \(i\)-edge, flipping bit \(i\), or fixes the current vertex at a blue \(i\)-edge. Therefore
\[
\varepsilon(w)=x\oplus y\oplus b(w),\qquad
\operatorname{supp}b(w)\subseteq I(C),
\]
where \(b(w)\) records the parity of stationary occurrences. If \(w\in F'\), this proves necessity.

Conversely, for each \(i\in I(C)\) choose \(v_i\in C\) fixed by \(U_i\). Starting at \(x\), travel by red swaps to \(v_i\), apply \(U_i\) there, and retrace the same swap word backward. This is a stabilizer word at \(x\) with occurrence-parity vector \(e_i\). Thus all vectors supported in \(I(C)\) are attainable by words fixing \(x\). If \(\operatorname{supp}(x\oplus y)\subseteq I(C)\), the displayed identity shows that the occurrence parity of any word taking \(x\) to \(y\) belongs to this span. Correct that parity with a stabilizer word. The resulting word belongs to \(F'\) and takes \(x\) to \(y\), proving sufficiency. If \(x,\bar x\in C\) and \(c\) is antipodally odd, for each \(i\) one of \(c_i(x),c_i(\bar x)\) is blue, so \(I(C)=[n]\) and the action is transitive. \(\square\)

Because the commutator subgroup of an involution-generated group is normally generated by its pairwise commutators, \(G'\) is generated by conjugates of \(K_{ij}=(U_jU_i)^2\). Thus arbitrary products of transported square curvatures act transitively on every red component containing antipodal vertices.

Now suppose \(c\) is legal and antipodally odd. Let \(L_R(c)\) be the minimum length of a red antipodal walk, finite by the monochromatic antipodal-path theorem. A word in the \(U_i\) is *even* when every direction appears an even number of times. Define
\[
\Lambda_R(c)=\min\{|w|:\ w\text{ even},\
U_w(x)=\bar x\text{ for some }x\}.
\]

**Theorem (optimal even-return budget).**
\[
\boxed{\Lambda_R(c)=n+L_R(c).}\tag{DG2}
\]
Consequently, writing \(L_R(c)=n+2\delta(c)\),
\[
\boxed{\Lambda_R(c)=2n+2\delta(c).}\tag{DG3}
\]

*Proof.* In an even word carrying \(x\) to \(\bar x\), each direction has an odd number of moving occurrences, because its bit changes. It consequently also has an odd number of stationary occurrences, hence at least one. Deleting stationary steps leaves a red antipodal walk of length at most \(|w|-n\), proving \(\Lambda_R(c)\ge n+L_R(c)\).

For the reverse inequality, choose a shortest red antipodal path \(P:x\to\bar x\) with direction word \(p\). Let \(A=\{i:c_i(x)=1\}\) and \(B=[n]\setminus A\). First apply \(U_i\) for \(i\in A\) at \(x\), where they are stationary. Traverse \(P\). Finally apply \(U_i\) for \(i\in B\) at \(\bar x\), where they are stationary by antipodal oddness. The resulting word \(w=(A,p,B)\) carries \(x\) to \(\bar x\), has length \(n+L_R(c)\), and uses each generator evenly, since each direction occurs oddly along every antipodal walk and once among the stationary steps. Equality in the lower bound forces every shortest even-return word to have one stationary occurrence per direction and its moving steps to form a shortest red antipodal walk. \(\square\)

For \(\delta(c)=0\), minimal even-return words have two occurrences of every direction, and the simple-bigon theorem selects a base-simple representative. Formula (DG3) quantifies the additional direction repetitions required for unrestricted commutator holonomy when the shortest red antipodal walk has detours. The remaining NORI1 problem is to force this length to be \(2n\), rather than merely establishing antipodal reachability within \(G'\).


#### Marked-influence feedback and directed-girth interlacement

Fix a legal antipodally odd edge coloring \(c\) of \(Q_n\), red swap involutions \(U_i\), and a double-occurrence word \(w\). Let \(p_i^-<p_i^+\) be the two positions of direction \(i\), \(J(w)\) its chord-interlacement graph, and \(r(w)=|E(J(w))|\). The directed influence graph \(D(c)\) has an arc \(j\to i\) when \(\partial_jc_i\not\equiv0\).

**Closed-span lemma.** For any connected component \(A\) of \(J(w)\), the consecutive subword between the earliest and latest appearances of letters in \(A\) contains full pairs of every letter it meets. In particular, a disconnected \(J(w)\) has a nonempty proper consecutive subword made of complete occurrence pairs.

*Proof.* Associate \(I_i=[p_i^-,p_i^+]\subseteq\mathbb R\) to each letter. Crossing chords give intersecting intervals, hence connectivity makes \(\bigcup_{i\in A}I_i=[a,b]\). If another letter \(j\) had one endpoint inside \([a,b]\) and the other outside, an interval \(I_i\), \(i\in A\), containing the inside endpoint would have alternating endpoints with \(I_j\). Then \(j\) would belong to \(A\), contradiction. Thus the span is closed under occurrence pairing. For disconnected \(J(w)\), choose a component not containing the first letter of \(w\); its span is proper. \(\square\)

**Marked-influence lemma.** If \(U_w(x)=\bar x\), each direction \(j\) moves at one of its two occurrences, denoted \(q_j\). For every \(i\) there is an arc \(j\to i\) of \(D(c)\) for which
\[
p_i^-<q_j<p_i^+.
\tag{MI1}
\]
When \(i\) is in a source strongly connected component \(S\), \(j\) may be chosen in \(S\).

*Proof.* Antipodal displacement with two uses of each swap requires one moving and one stationary use in each direction. The two evaluations of \(c_i\) therefore differ. Between them, only moving swaps change the state; at least one such swap must flip a bit on which \(c_i\) depends. Its direction supplies \(j\). The source property excludes influences into \(S\) from outside. \(\square\)

**Theorem (source-SCC directed girth).** Let \(S_1,\ldots,S_h\) be the source strongly connected components of \(D(c)\), and let \(g_a\) denote the length of a shortest directed cycle in \(D(c)[S_a]\). Then every successful double-occurrence word satisfies
\[
\boxed{r(w)\ge\sum_{a=1}^{h}(g_a-1).}
\tag{MI2}
\]
Each \(g_a\) is finite and at least two.

*Proof.* For each \(i\in S_a\) choose an incoming influence \(j_i\to i\) satisfying (MI1). The chosen arcs form a directed graph with indegree one at every vertex, so it contains a simple directed cycle \(C\subseteq S_a\) of length \(k\ge g_a\). Restrict the word to \(C\). Were there a nonempty proper consecutive subword formed from complete pairs on \(B\subsetneq C\), some \(i\in B\) would have its predecessor \(j_i\) on the selected cycle outside \(B\). Its marked occurrence \(q_{j_i}\) could not then be between the two occurrences of \(i\), contradicting (MI1). By the closed-span lemma, \(J(w)[C]\) is connected and has at least \(k-1\) crossings. Distinct source components are disjoint, so these crossing counts add. Each rule \(c_i\) ignores bit \(i\) but changes under the full antipodal flip, hence depends on some other bit; a source component therefore has an internal directed cycle, and no self-loop is possible. \(\square\)

The bound (MI2) counts all crossings, including commuting pairs. The noncommuting crossing count can remain bounded even when the directed girth grows.

##### A root-count formula and two-commutator propagation

Suppose
\[
c_i(x)=x_{r(i)}\oplus\varepsilon_i,
\quad r\in S_n,\ r(i)\ne i,\ \varepsilon_i\in\mathbb F_2,
\tag{MI3}
\]
so every rule has a unique reader and every bit is read by a unique rule. For each reader \(j\), put \(i=r^{-1}(j)\) and define
\[
a_j(w)=\#\{t\in\{-,+\}:p_i^-<p_j^t<p_i^+\}.
\]

**Theorem (reader-permutation return count).** For (MI3), the number of starting states with \(U_w(x)=\bar x\) is
\[
\boxed{\#\{x:U_w(x)=\bar x\}=\prod_{j=1}^{n}a_j(w).}
\tag{MI4}
\]
It is zero or a power of two, independently of the constants \(\varepsilon_i\).

*Proof.* If the return is antipodal, reader \(j=r(i)\) must move between the two appearances of \(i\), since the value of its rule must change. Its moving occurrence \(q_j\) is one of the \(a_j(w)\) admissible positions.

Conversely select one admissible \(q_j\) for each \(j\). Let \(b_i=0\) if \(q_i=p_i^-\), and \(b_i=1\) otherwise. Set the initial bits by
\[
x_j=\varepsilon_i\oplus b_i\oplus\mathbf1_{\{q_j<p_i^-\}},
\qquad i=r^{-1}(j).
\tag{MI5}
\]
Induct over the successive occurrences, assuming earlier moves agree with their selected positions. At the first appearance of \(i\), its reader bit is \(x_j\oplus\mathbf1_{\{q_j<p_i^-\}}\), so \(c_i=b_i\) and the swap moves if \(b_i=0\). Reader \(j\) moves between the two appearances of \(i\), complementing \(c_i\); the second swap moves if \(b_i=1\). Thus every direction moves once and the endpoint is antipodal. Two different selections cannot yield one root because the deterministic swaps determine their moving positions. This gives (MI4). \(\square\)

**Corollary (sharp crossings for reader permutations).** If \(r\) has \(h\) cycles, then
\[
\boxed{\min_{w:\,\exists x,\ U_w(x)=\bar x}r(w)=n-h.}
\tag{MI6}
\]
Moreover for a directed reader cycle on arbitrarily many directions \(m\ge3\), a successful word can have \(m-1\) crossings, only two of them noncommuting.

*Proof.* Each cycle of \(r\) is a source SCC with girth equal to its size; (MI2) gives the lower bound. On a cycle of length \(m\ge2\), relabel so that \(r(i)=i-1\pmod m\) and take
\[
v_m=(m-1,m-2,\ldots,1,0,1,2,\ldots,m-1,0).
\tag{MI7}
\]
Its chord crossings are precisely \(\{0,j\}\) for \(1\le j<m\), a star with \(m-1\) edges. In (MI4) one has \(a_0=a_{m-1}=1\) and \(a_j=2\) for \(1\le j\le m-2\). Thus \(v_m\) succeeds from \(2^{m-2}\) roots for every sign choice. Since the only influence pairs are consecutive directions on the reader cycle, for \(m\ge3\) only the crossings \(\{0,1\}\) and \(\{0,m-1\}\) are noncommuting. For \(m=2\) the sole crossing is noncommuting. Concatenate (MI7) for the disjoint cycles of \(r\); no crossing joins the cycles, and successful roots combine, attaining \(n-h\). \(\square\)

The star words (MI7) exhibit dimension-uniform antipodal displacement assembled from just two essential transported square commutators on a long one-way influence cycle. The girth bound detects an unbounded number of geometric crossings while permitting these two commutators to propagate through arbitrarily many reader bits. For unrestricted colorings, (MI1) is a necessary condition; a compatible choice of marked moves and starting state remains the missing step.


#### Directionwise crossing flux in paired-cover geodesic bigons

**Theorem (crossing-flux identity and sharp linear curvature necessity for geodesic bigons).** Let \(c\) be a legal antipodally odd binary edge coloring of \(Q_n\), with red swaps \(U_i\), and let \(W=W(\pi,A)=(\pi|_A)\pi(\pi|_{A^c})\) for an arbitrary subset \(A\). Write \(J(W)\) for the chord-interlacement graph. Between the two occurrences of each \(i\) in \(W\), the intervening word \(W_i\) consists of every neighbor \(j\in N_{J(W)}(i)\) once, and no other letters. For a trajectory of \(U_W\) from \(x\), let \(z_i\) be the state just after the first \(i\)-operation, and \(z_{ij}\) the state just before the intervening \(j\)-operation. With \(r_j=1-c_j\) and \(\partial_jc_i(v)=c_i(v)\oplus c_i(v\oplus e_j)\), the displacement of bit \(i\) obeys
\[
\boxed{[U_W(x)\oplus x]_i
=c_i(z_i)\oplus c_i(U_{W_i}(z_i))
=\bigoplus_{j\in N_{J(W)}(i)}r_j(z_{ij})\,\partial_j c_i(z_{ij}).}
\tag{1}
\]
Let the directed influence graph have arc \(j\to i\) when \(\partial_jc_i\not\equiv0\). Let \(a_c(W)\) be the number of such directed arcs crossing in \(J(W)\), and \(r_c(W)\) the number of noncommuting crossing swap pairs. Then
\[
\boxed{d_H(U_W(x),\bar x)\ge n-a_c(W)\ge n-2r_c(W).}
\tag{2}
\]
Indeed every displaced bit \(i\) has an incoming crossed directed-influence arc. Thus a successful bigon demands minimum indegree at least one in the crossed directed-influence graph, \(a_c(W)\ge n\), and
\[
\boxed{r_c(W)\ge\lceil n/2\rceil.}
\tag{3}
\]
This strengthens the source-SCC curvature lower bound for the geodesic-bigon family.

*Proof.* For \(i\in A\), the interval separating its occurrences contains each other \(A\)-letter once and each \(B\)-letter preceding \(i\) in \(\pi\) once. For \(i\in B\), it contains each other \(B\)-letter once and each \(A\)-letter following \(i\) once. These are the interlacement neighbors, with no repeated intervening directions. Both \(i\)-operations change only bit \(i\), and \(c_i\) is invariant under bit \(i\). Hence the parity of the two \(i\)-flips equals the change in \(c_i\) across the intervening trajectory. Telescoping this change across its distinct direction operations yields (1). If bit \(i\) changes, one summand of (1) is nonzero, furnishing a directed influence arc \(j\to i\) whose letters cross. Counting displaced bits against crossed arcs yields the first inequality in (2). The existing commutator-influence identity says a crossed pair carries at least one influence arc if and only if its swaps do not commute; each such pair carries at most two arcs. This proves (2) and (3).

*Sharpness.* Let \(n=2h\). For each \(0\le t<h\), set \(c_{2t}(x)=x_{2t+1}\) and \(c_{2t+1}(x)=x_{2t}\), independently of all other bits. Each two-bit factor admits a red antipodal geodesic from a root with mixed bits, and concatenating those geodesics gives a red full geodesic. The simple-bigon normal form supplies a word \(W(\pi,A)\) with antipodal return. The only noncommuting swap pairs are the \(h\) reciprocal-reader pairs, so the lower bound forces all \(h\) to cross and \(r_c(W)=h=n/2\).

*Scope.* The gap property (1) is specific to the bigon family. For arbitrary doubled words, a nested pair may lie twice between two occurrences of another label, transmitting curvature without an incident crossing. Thus (3) is a bigon-only statement. The curvature requirement is necessary and does not establish antipodal return.

#### Root-averaged bigon holonomy as transported color autocorrelation

Fix a legal coloring \(c\) of \(Q_n\), a word \(w\) in which every direction occurs twice, and the red swaps \(U_i\). For each \(i\), let \(m_i(w)\) be the subword strictly between its two occurrences, and let \(M_i\) be the induced permutation of \(Q_n\). Define \(f_i(x)=(-1)^{c_i(x)}\) and the uniform inner product \(\langle f,g\rangle=2^{-n}\sum_x f(x)g(x)\).

**Theorem (gap-transport identity).** For every such word,
\[
\boxed{\frac1{2^n}\sum_x d_H(x,U_w(x))
=\frac12\sum_{i=1}^n\bigl(1-\langle f_i,f_i\circ M_i\rangle\bigr).}
\tag{GT1}
\]
Equivalently, its mean antipodal holonomy defect is
\[
\boxed{\frac1{2^n}\sum_x d_H(U_w(x),\bar x)
=\frac12\sum_{i=1}^n\bigl(1+\langle f_i,f_i\circ M_i\rangle\bigr).}
\tag{GT2}
\]

*Proof.* Before the first occurrence of \(U_i\), the state \(z\) is uniformly distributed when the initial state \(x\) is uniform, since the preceding swaps are permutations. Put \(u=U_i(z)\). Since \(c_i\) ignores bit \(i\), \(c_i(z)=c_i(u)\), and \(u\) is uniform. The state before the second occurrence is \(M_i(u)\). Because only \(U_i\) changes bit \(i\), the final state differs from its initial state in that bit if and only if
\[
c_i(u)\ne c_i(M_i(u)).
\]
Averaging over uniform \(u\) gives the \(i\)-th term \((1-\langle f_i,f_i\circ M_i\rangle)/2\). Sum over \(i\) to obtain (GT1). For binary vectors, \(d_H(v,\bar x)=n-d_H(v,x)\), proving (GT2). \(\square\)

**Bigon specialization.** Suppose \(w=(\pi|_A,\pi,\pi|_B)\), \(B=[n]\setminus A\), and write \(\pi_{<i}\), \(\pi_{>i}\) for the labels preceding and following \(i\) in \(\pi\). Then
\[
m_i(w)=
\begin{cases}
(\pi_{>i}|_A)\,\pi_{<i},&i\in A,\\
\pi_{>i}\,(\pi_{<i}|_B),&i\in B.
\end{cases}
\tag{GT3}
\]
Each \(m_i(w)\) uses every one of its directions once, so every term of (GT2) is a color autocorrelation under a direction-simple red swap sweep. In particular, the first and last labels of a simple bigon have intervening sweeps using all remaining \(n-1\) directions.

The identities distinguish endpoint forcing at a selected root from mixing in the uniform root distribution. The minimum antipodal defect is bounded above by the mean in (GT2), but the two quantities can be far apart even for legal colorings satisfying NORI1.


#### Median shuffle exchange geometry of simple antipodal bigons

**Theorem (median shuffle strata and transported-square exchange).** Fix a nonempty proper partition \([n]=A\sqcup B\), and fix the internal orders \(a_1,\ldots,a_k\) on \(A\) and \(b_1,\ldots,b_l\) on \(B\), with \(k,l\ge1\). Let \(\mathcal S(A,B)\) consist of all shuffles \(\pi\) of these two internally ordered lists with first letter \(b_1\) and last letter \(a_k\). Associate the embedded antipodal bigon word \(W_\pi=(\pi|_A)\pi(\pi|_B)\). Join two shuffles by an edge when one is obtained from the other by transposing adjacent letters from opposite parts in interior positions.

Then this exchange graph is the cover graph of the distributive lattice of order ideals of a \((k-1)\times(l-1)\) rectangular grid. It is connected, is a median graph, and has \(\binom{n-2}{k-1}\) vertices. Its graph distance between \(\pi,\sigma\) equals the number of mixed pairs \((a,b)\in A\times B\) whose relative order differs between \(\pi\) and \(\sigma\).

The interlacement graph \(J(W_\pi)\) determines the shuffle uniquely within the stratum. Adjacent shuffles have interlacement graphs differing by one mixed edge \(\{a,b\}\). For a legal coloring with red swaps \(U_i\), suppose the two central words are \(W=P\,a\,b\,R\) and \(W'=P\,b\,a\,R\), where \(a\in A,b\in B\) are adjacent and the words are written in traversal order. With \(S=U_R\) and \(H=U_W,H'=U_{W'}\), one has
\[
\boxed{H'H^{-1}=S\,(U_aU_b)^2\,S^{-1}.}\tag{1}
\]
Thus an elementary exchange toggles one chord crossing and changes holonomy by one transported square commutator. In particular, if \(U_a,U_b\) commute, the return permutation is unchanged by that exchange.

*Proof.* All shuffles have forced first letter \(b_1\) and last letter \(a_k\). Their remaining \(k-1\) A-letters and \(l-1\) B-letters form arbitrary order-preserving interleavings. The inversion sets of pairs \((b_j,a_i)\), \(2\le j\le l,1\le i<k\), with \(b_j\) preceding \(a_i\), are precisely the order ideals of a rectangle poset (choose the grid orientation so inversion sets are downward closed). Adjacent cross-part transpositions insert or delete one allowable inversion, yielding the distributive-lattice cover graph. Such graphs are median, and the inversion-vector embedding is isometric, proving connectedness and the distance formula.

For the bigon word, all pairs within A and within B cross; a mixed pair \((a,b)\) crosses precisely when \(b\) precedes \(a\) in the central shuffle. Hence the crossing graph records every mixed inversion and is injective within the stratum. A cross-part adjacent swap changes only the order of that pair, leaving all other pair orders and the two exterior restricted words unchanged. Therefore \(W,W'\) differ at only the displayed central adjacent positions. Applying the sequences right-to-left as permutations yields \(H=S U_bU_a U_P\), \(H'=S U_aU_b U_P\). Since the swaps are involutions, \(H'H^{-1}=S U_aU_bU_aU_b S^{-1}\), proving (1).

*Application.* In the published six-direction counterexample to repeated identical sweeps, the successful bigon has A-order (5,2,4), B-order (1,3,0), and central shuffle (1,5,3,2,0,4). Its stratum is the six-vertex lattice of a \(2\times2\) rectangle. Its mixed optional inversion rank is one and its interlacement graph has twelve of the fifteen pairs. The maximal shuffle in the same stratum corresponds to a repeated sweep and has fifteen crossing pairs but no antipodal root for that coloring.

*Scope.* The theorem determines each fixed-partition, fixed-internal-order stratum, not connectivity under moves changing A or the internal orders. Nor does a sequence of curvature exchanges necessarily decrease the Hamming holonomy defect.

#### Derived swap-group orbits inside red components

Let \(c\) be any binary edge coloring of \(Q_n\), \(n\ge2\), with red swaps \(U_i(x)=x\oplus e_i\) when \(c_i(x)=0\), and \(U_i(x)=x\) otherwise. Put \(G=\langle U_1,\ldots,U_n\rangle\) and write \(G'\) for its derived subgroup. For a red connected component \(C\), define
\[
B(C)=\{i:\exists z\in C,\ c_i(z)=1\},\qquad R(C)=[n]\setminus B(C).
\]
Thus \(i\in R(C)\) means that the direction-\(i\) edge is red at every vertex of \(C\).

**Theorem (derived-orbit classification).** For every \(x\in C\),
\[
\boxed{G'x=\{y\in C:y_i=x_i\ \text{for all }i\in R(C)\}.}\tag{DO1}
\]
Moreover, \(C\) is invariant under toggling any subset of the directions in \(R(C)\), and the \(G'\)-orbits on \(C\) are its \(2^{|R(C)|}\) nonempty slices obtained by fixing those bit values. Each orbit has cardinality \(|C|/2^{|R(C)|}\).

*Proof.* Every swap preserves each red connected component. In the free product \(F=*_{i=1}^n C_2\), the kernel of the generator-parity map \(F\to\mathbb F_2^n\) is the derived group \(F'\); its image under the substitution of generators by \(U_i\) is \(G'\). Thus \(G'\)-orbits are precisely the endpoints of words using every direction an even number of times.

For \(i\in R(C)\), \(U_i\) flips bit \(i\) at every state in \(C\); no other swap changes this bit. Consequently an even word preserves the \(i\)-th bit, proving inclusion from left to right in (DO1).

Conversely, take \(x,y\in C\) agreeing in all directions of \(R(C)\). Choose any red path \(P\) from \(x\) to \(y\). Since every step of \(P\) moves, its generator-parity vector is \(x\oplus y\). For each \(i\in B(C)\), choose \(z_i\in C\) with \(c_i(z_i)=1\) and a red path \(T_i\) from \(x\) to \(z_i\). The word \(T_i U_i T_i^{-1}\), interpreted in traversal order, fixes \(x\) and has generator-parity vector \(e_i\): the inserted \(U_i\) is stationary, and the outward and return paths use each direction equally often. Prepend these loops for all \(i\) where \(x_i\ne y_i\). Their combined parity is \(x\oplus y\), so the resulting word has even multiplicities and takes \(x\) to \(y\). This proves (DO1).

For \(i\in R(C)\), the \(i\)-edge at every vertex in \(C\) is red; hence toggling bit \(i\) preserves \(C\). These toggles commute, so the \(2^{|R(C)|}\) rigid-bit assignments occur equally often in \(C\). The orbit-size assertion follows from (DO1). \(\square\)

**Corollary (transitivity in antipodal-bearing components).** If \(c\) is antipodally odd and a red component \(C\) contains some pair \(a,\bar a\), then \(B(C)=[n]\), and hence
\[
\boxed{G'x=C\qquad\text{for every }x\in C.}\tag{DO2}
\]
Indeed \(c_i(\bar a)=1-c_i(a)\), so at least one of \(a,\bar a\) has a blue direction-\(i\) edge for every \(i\). Therefore every element of \(C\) can be reached from every other by an even-generator word, equivalently by a product of conjugates of the square commutators \((U_iU_j)^2\).

This transitivity is a group-orbit statement without a word-length bound. The existing full-coloring \(Q_6\) certificate with a red tree component containing the sole antipodal pair \((0,63)\) at red distance eight shows that a transitive derived action on an antipodal-bearing component does not imply a red antipodal geodesic within that component.


#### Paired-lift component geometry and red distance

Let \(c\) be an antipodally odd binary edge coloring of \(Q_m\), and let \(C\) be its complementary paired coloring on \(Q_{2m}\), written at vertices \((x,y)\in Q_m\times Q_m\):
\[
C_i(x,y)=c_i(x),\qquad C_{m+i}(x,y)=1-c_i(x).
\]
Let \(T\) be a red connected component of the original coloring, and put \(B(T)=\{i:\exists x\in T,\ c_i(x)=1\}\), \(R(T)=[m]\setminus B(T)\).

**Theorem (red component decomposition of the paired lift).** The red components of the paired coloring lying above \(T\) are
\[
\boxed{T\times\{y\in Q_m:y|_{R(T)}=t\},
\qquad t\in\mathbb F_2^{R(T)}.}\tag{PL1}
\]
Each has \(|T|\,2^{|B(T)|}\) vertices. If \(T\) contains an antipodal pair, then \(B(T)=[m]\), so the entire \(T\times Q_m\) is one red component. For any \(x,\bar x\in T\) and any \(y\in Q_m\),
\[
\boxed{
d_{C,\mathrm{red}}\bigl((x,y),(\bar x,\bar y)\bigr)
=m+d_{c,\mathrm{red}}(x,\bar x).
}\tag{PL2}
\]

*Proof.* A red move in one of the first \(m\) directions changes \(x\) along a red edge of \(c\) and leaves \(y\) fixed. A red move in direction \(m+i\) changes only \(y_i\), and is available precisely at those base vertices where \(c_i(x)=1\). Thus no red path leaves \(T\) in its base state and the bits \(y_i\) with \(i\in R(T)\) remain fixed. Conversely, any two base vertices in \(T\) are joined by a red path, and for every \(i\in B(T)\), one can travel within \(T\) to a vertex with \(c_i=1\), toggle \(y_i\), and return. This proves (PL1). If \(x,\bar x\in T\), antipodal oddness ensures one of them has \(c_i=1\) for every \(i\), so \(B(T)=[m]\).

For (PL2), projection onto the first factor sends every red lifted path joining the indicated antipodal endpoints to a red walk from \(x\) to \(\bar x\); it therefore uses at least \(d_{c,\mathrm{red}}(x,\bar x)\) first-factor moves. The lifted path also changes each \(y_i\) an odd number of times, requiring at least \(m\) second-factor moves. This is the lower bound. For equality, lift a shortest base red antipodal path with \(y\) initially fixed. For each \(i\), perform its single \(y_i\)-toggle at whichever endpoint \(x\) or \(\bar x\) has \(c_i=1\). The toggles commute when the base state is fixed, and every lifted move is red. This yields a red antipodal path of length \(m+d_{c,\mathrm{red}}(x,\bar x)\). \(\square\)

**Eulerian component obstruction.** Let \(T\subset Q_6\) be the previously certified red tree component with 13 vertices, unique antipodal pair \(0,63\), and red distance eight. Its paired lift is a balanced legal coloring of \(Q_{12}\) with red component \(T\times Q_6\) containing \(13\cdot64=832\) vertices. This component is six-regular, hence Eulerian, and every antipodal pair in it has red distance \(8+6=14\), exceeding the cube geodesic length twelve. More generally, taking \(k\) independent copies of the six-dimensional base coloring before pairing yields balanced colorings of \(Q_{12k}\) with an Eulerian red component of size \(13^k2^{6k}\), all of whose antipodal pairs have red distance \(14k=12k+2k\). The resulting Eulerian red component and its transported square-holonomy group exhibit linear antipodal distance excess. Hence neither red regularity nor the existence of colorwise Euler tours nor transitivity of transported square holonomy within an antipodal-bearing component forces a red full antipodal geodesic in that component.


#### Connected simple-bigon exchanges and curvature transport

Let \(c\) be a legal antipodally odd coloring of \(Q_n\), let \(U_i\) be its red edge-swap involutions, and write \(H_w=U_w\) for the permutation induced by executing a word \(w\) from left to right. The simple-bigon parameters are a permutation \(\pi\) and a subset \(A\subset[n]\) with \(B=[n]\setminus A\), the first letter of \(\pi\) in \(B\), and the last letter in \(A\). The associated word is \(W(\pi,A)=(\pi|_A)\pi(\pi|_B)\).

Define the *simple-bigon exchange graph* to have these parameter pairs as vertices, with two types of edge: (i) an adjacent transposition in \(\pi\) that preserves the first/last membership conditions, with \(A\) unchanged; (ii) changing the membership of an interior letter of \(\pi\) between \(A\) and \(B\), with \(\pi\) unchanged.

**Theorem (connected exchange graph).** For every \(n\ge3\), the simple-bigon exchange graph is connected and has diameter \(O(n^2)\).

*Proof.* Take two admissible parameter pairs. An arbitrary adjacent transposition of a permutation can be made admissible by at most one preliminary membership change: for a transposition in the first two positions, make the second letter belong to \(B\); for a transposition in the final two positions, make the penultimate letter belong to \(A\). The adjusted letter is interior before the transposition. All other adjacent transpositions preserve admissibility directly. Transform the first permutation into the second by at most \(\binom n2\) adjacent transpositions, using these preliminary changes when necessary. With the target permutation fixed, alter the membership of each interior letter to match the target subset; the first and last memberships are forced. This gives at most \(2\binom n2+n-2\) exchanges. \(\square\)

The holonomy variation is controlled by square commutators \(K_{ij}=(U_jU_i)^2\).

**Proposition (exchange transport).**
(a) If adjacent letters \(a,b\) of \(\pi\) belong to opposite membership classes, their transposition changes the doubled word from \(PabS\) to \(PbaS\), for common subwords \(P,S\), and
\[
\boxed{H_{W'}H_W^{-1}=H_S(U_aU_b)^2H_S^{-1}.}\tag{BE1}
\]
(b) If they belong to the same class, both their occurrences change relative order, and \(H_{W'}H_W^{-1}\) is a product of at most two conjugates of \(K_{ab}^{\pm1}\).
(c) For a membership exchange moving an interior letter \(i\) from \(A\) to \(B\), there are common subwords \(P,H,S\) such that \(W=PiHS\), \(W'=PHiS\), and
\[
\boxed{H_{W'}H_W^{-1}=H_S[U_i,H_H]H_S^{-1},}\tag{BE2}
\]
where \([g,h]=ghg^{-1}h^{-1}\). Reversing the exchange gives the inverse relation. The commutator in (BE2) expands into transported pairwise square commutators \(K_{ij}^{\pm1}\).

*Proof.* For (a), since only the central permutation swaps \(a,b\), the prefix and suffix subwords are common. With left-to-right execution, \(H_{PabS}=H_SU_bU_aH_P\) and \(H_{PbaS}=H_SU_aU_bH_P\). Multiply the second expression by the inverse of the first. In (b) there are two adjacent-letter interchanges, one in the central permutation and one in the outer restriction, and applying (a)'s group calculation to each gives the product. For (c), moving \(i\) from the restricted prefix to the restricted suffix preserves the order of the other letters and transports its outer occurrence across the subword \(H\). Hence \(H_{PiHS}=H_SH_HU_iH_P\) and \(H_{PHiS}=H_SU_iH_HH_P\), proving (BE2). Expanding a commutator with a product by \([g,hk]=[g,h]h[g,k]h^{-1}\), and using the involutivity of the letters, expresses it in conjugates of pairwise commutators. \(\square\)

Write \(i\to j\) in the directed influence graph \(D(c)\) when \(c_j\) depends on vertex bit \(i\), and \(\operatorname{Reach}^+(I)\) for the smallest forward-closed set containing \(I\).

**Theorem (causal localization of bigon exchanges).** If \(W,W'\) differ by an admissible adjacent transposition of letters \(a,b\), then for every root \(x\),
\[
\boxed{\operatorname{supp}\bigl(H_{W'}(x)\oplus H_W(x)\bigr)
\subseteq\operatorname{Reach}^+(\{a,b\}).}\tag{BE3}
\]
If \(W,W'\) differ by changing the membership of \(i\), the same inclusion holds with \(\operatorname{Reach}^+(\{i\})\) on the right. Consequently, for the defect \(d_W(x)=d_H(H_W(x),\bar x)\),
\[
|d_{W'}(x)-d_W(x)|\le |\operatorname{Reach}^+(I)|,\tag{BE4}
\]
where \(I=\{a,b\}\) or \(I=\{i\}\), respectively.

*Proof.* Let \(T=\operatorname{Reach}^+(I)\). Forward closure implies that no color rule \(c_j\) with \(j\notin T\) depends on bits in \(T\). Projecting onto the complementary dimensions \([n]\setminus T\) therefore maps every \(U_j\) with \(j\in T\) to the identity, and every \(U_j\) with \(j\notin T\) to a well-defined edge swap on that smaller cube. The two words \(W,W'\) have identical subsequences after removing all letters in \(T\): their only reordered or relocated occurrences lie in \(I\subseteq T\). Therefore their induced projections coincide for every root. This proves (BE3), including the membership-exchange version. The Hamming-distance inequality (BE4) follows from the triangle inequality. \(\square\)

The localization includes propagated nonlinear dependencies, since the reachability set is computed from all directed influences. It supplies a pointwise restriction on the changes available to local exchanges; it does not assert that a defect-minimizing bigon admits a decreasing exchange.


#### Marked-reader interval containment and essential commutator cost

Let \(c\) be a legal antipodally odd edge coloring, \(w\) a word using each direction twice, and \(I_i=[p_i^-,p_i^+]\) the interval between its two appearances. Write \(r_c(w)\) for the number of interlaced unordered pairs \(\{i,j\}\) with noncommuting swaps \(U_i,U_j\). For an antipodal return, let \(q_j\) denote the unique moving occurrence of \(j\).

**Lemma (uncrossed readers are nested).** If \(p_i^-<q_j<p_i^+\), either chords \(i,j\) cross or \(I_j\subsetneq I_i\).

*Proof.* One endpoint of \(I_j\) is in the interior of \(I_i\). If the other is outside, the endpoints alternate and the chords cross; otherwise both lie inside \(I_i\). \(\square\)

**Theorem (essential crossing lower bound from source directed girth).** Let \(S_1,\ldots,S_h\) be the source strongly connected components of the directed influence graph \(D(c)\), and let \(g_a\) be the directed girth of \(D(c)[S_a]\). Every doubled-direction word admitting an antipodal red return satisfies
\[
\boxed{r_c(w)\ge\sum_{a=1}^h\kappa(g_a),
\qquad
\kappa(2)=1,\quad\kappa(g)=2\ (g\ge3).}
\tag{EC1}
\]

*Proof.* For each \(i\) in a source component \(S_a\), select an incoming influence arc \(j_i\to i\) such that the moving occurrence \(q_{j_i}\) lies between the two occurrences of \(i\), as guaranteed by the marked-influence lemma (MI1). The selected arcs contain a directed simple cycle \(C=(v_0,\ldots,v_{k-1})\) with \(k\ge g_a\), and \(v_t\to v_{t+1}\) cyclically. An arc of \(C\) whose chords do not cross forces \(I_{v_t}\subsetneq I_{v_{t+1}}\) by the lemma. If \(k\ge3\) and at most one arc crossed, the remaining strict inclusions would either form a cycle of strict containments, or concatenate to show that the endpoints of the purported crossing arc were nested. Both are impossible. Thus at least two distinct unordered pairs corresponding to arcs of \(C\) cross. Their swaps do not commute, because the chosen arcs are influences. If \(k=2\), the two opposite influence arcs refer to one unordered pair, which must cross since otherwise each interval would strictly contain the other. Distinct source components contribute disjoint pairs, proving (EC1). \(\square\)

**Theorem (optimal essential crossings for permutation readers).** Suppose
\[
c_i(x)=x_{r(i)}\oplus\varepsilon_i,\qquad
r\in S_n,\quad r(i)\ne i.
\tag{EC2}
\]
Let \(a\) be the number of cycles of \(r\) of length at least three and \(b\) the number of its two-cycles. Then
\[
\boxed{\min_{w:\,\exists x,\ U_w(x)=\bar x}r_c(w)=2a+b.}
\tag{EC3}
\]
For every simple geodesic-bigon word \(W=(\pi|_A)\pi(\pi|_{A^c})\), the number of antipodal roots is zero or one; when nonzero,
\[
\boxed{r_c(W)=n-b.}
\tag{EC4}
\]
For every permutation \(\pi\), the repeated-sweep bigon \(W=\pi\pi\) has one antipodal root and attains (EC4).

*Proof.* Every reader cycle is a source component, so (EC1) gives \(r_c(w)\ge2a+b\). For a cycle of length \(m\ge3\), the word \(v_m=(m-1,\ldots,1,0,1,\ldots,m-1,0)\) from (MI7) has two noncommuting chord crossings and succeeds from \(2^{m-2}\) roots; for \(m=2\) it has one noncommuting crossing. Concatenating these words on disjoint reader cycles attains \(2a+b\).

For a simple bigon, the subword between the two appearances of direction \(i\) contains any other direction \(j\) once if their chords cross and zero times otherwise. By the root-count formula (MI4), its \(a_j(W)\) factor is the indicator that the chord of \(j\) crosses the chord of its child \(r^{-1}(j)\). Thus an antipodal root exists if and only if every reader-child pair crosses, and then (MI4) yields one root. A reader cycle of length \(m\ge3\) contributes \(m\) distinct unordered influence pairs; a two-cycle contributes one. All must cross, giving \(r_c(W)=n-b\). Every pair crosses in \(W=\pi\pi\), so (MI4) proves the final statement. \(\square\)

For a single directed reader cycle of length \(n\ge3\), general doubled words need just two essential commutator crossings, whereas every successful simple bigon needs \(n\). The star word \(v_n\) has \(2^{n-2}\) antipodal roots, whereas every successful simple bigon has one. This gives an unbounded separation between transported square-curvature cost and geodesic-bigon curvature cost even within one strongly connected influence component.


#### Prime-degree symmetric holonomy in an antipodal-deficient red tree

**Theorem.** In the published six-dimensional legal coloring with red component \(T=\{0,1,4,8,9,13,29,31,41,45,47,61,63\}\), one has \(\langle U_i|_T:0\le i<6\rangle=S_{13}\) and its commutator subgroup is \(A_{13}\), although the unique red antipodal pair \(0,63\) has red distance eight rather than six.

*Proof.* The red tree is connected, so its directional swaps act transitively on thirteen vertices. The direction-one swap restricted to \(T\) is precisely the transposition \((61\ 63)\); it is the sole red direction-one edge in the component. A transitive permutation group of prime degree thirteen is primitive. The graph whose edges correspond to conjugates of this transposition has connected components forming invariant blocks of the group. Thus this graph is connected, and its edge transpositions generate all of \(S_{13}\). The derived group is \(A_{13}\), which is eleven-transitive. The distance-eight assertion is certified by the component's tree edges. \(\square\)


#### Wreath-product lift holonomy

**Theorem (paired-lift wreath structure).** Suppose a red connected component \(T\) of a legal coloring of \(Q_m\) contains an antipodal pair, has \(q\ge3\) vertices, and the restricted swap group equals \(S_q\). Put \(E_q=\{f:T\to\mathbb F_2:\sum_{t\in T}f(t)=0\}\). The red swap group of the complementary paired lift, restricted to its component \(D=T\times Q_m\), is
\[
\widetilde G_D=\begin{cases}
(\mathbb F_2^T)^m\rtimes S_q,&q\text{ odd},\\
(E_q)^m\rtimes S_q,&q\text{ even}.
\end{cases}
\tag{WP1}
\]
Here the normal factor translates the second block \(y\) at each fiber over \(t\in T\), and \(S_q\) permutes those fibers.

*Proof.* The first \(m\) swaps act as \(S_q\) on the first block and fix \(y\). Vertical swap \(m+i\) flips \(y_i\) at base vertices in \(S_i=\{t:c_i(t)=1\}\). Its support size is \(q-2r_i\), where \(r_i\) is the number of red direction-\(i\) edges in \(T\). An antipodal red path in \(T\) traverses direction \(i\), so \(r_i\ge1\); antipodal oddness ensures \(S_i\ne\varnothing\). Thus \(0<|S_i|<q\), with support parity \(q\bmod2\). Conjugation by \(S_q\) generates the characteristic vectors of all subsets of \(T\) of size \(|S_i|\). Their binary span is \(E_q\) if the size is even and \(\mathbb F_2^T\) if odd: differences between supports related by a single-element exchange generate all \(e_a+e_b\). Independent vertical swaps commute, giving the asserted semidirect product. \(\square\)


**Corollary (derived wreath group and Eulerian obstruction).** In the preceding theorem,
\[
\boxed{\widetilde G_D'=(E_q)^m\rtimes A_q.}\tag{WP2}
\]
The derived group is transitive on \(D\). Indeed the vertical normal factor is abelian; its commutators with \(S_q\) generate even-support flips \(E_q\) independently in every direction, and \(S_q'=A_q\). The latter acts transitively on \(T\), and an even-support flip can modify any selected bit at any selected base vertex, compensating at another base vertex. This proves both conclusions.

For the certified 13-vertex red tree \(T\subset Q_6\) whose restricted swap group is \(S_{13}\), its balanced paired lift has a red component \(D=T\times Q_6\) with 832 vertices, all of red degree six. Every antipodal pair in \(D\) has red distance fourteen by the established paired-lift distance identity, exceeding the geodesic length twelve. Yet
\[
\boxed{\widetilde G_D=(C_2^6)^{13}\rtimes S_{13},\qquad
\widetilde G_D'=(E_{13})^6\rtimes A_{13}.}\tag{WP3}
\]
Their orders are \(2^{78}13!\) and \(2^{72}13!/2\). Thus a regular Eulerian monochromatic component may have full symmetric base monodromy, unrestricted vertical translation group, and transitive square-commutator group while containing no monochromatic antipodal geodesic. Independent products give balanced \(Q_{12k}\) instances with deficient component \(D^k\), red antipodal distance \(14k\), and restricted swap group the direct product of \(k\) such wreath groups.


##### Time-ordered influence bounds and defect balance

For a swap word \(S=(s_1,\ldots,s_m)\) and a set \(I\) of vertex-bit indices, define \(T_0=I\) and
\[
T_t=T_{t-1}\cup\{s_t:\text{some }k\in T_{t-1}\text{ influences }c_{s_t}\},
\qquad T_S(I)=T_m. \tag{BT1}
\]
Then for any two vertices \(u,v\) differing only within \(I\),
\[
\operatorname{supp}(H_S(u)\oplus H_S(v))\subseteq T_S(I).
\tag{BT2}
\]
Indeed a swap in dimension \(s_t\) can create a disagreement only in that bit, and only if its color rule reads a bit on which the two current states disagree. Induction proves (BT2).

If a cross-class adjacent transposition changes \(W=PabS\) to \(W'=PbaS\), the states just before the common suffix \(S\) differ only in bits \(a,b\). Therefore
\[
\operatorname{supp}(H_W(x)\oplus H_{W'}(x))
\subseteq T_S(\{a,b\})\subseteq\operatorname{Reach}^+(\{a,b\}).
\tag{BT3}
\]
The first inclusion records causal timing even when the influence digraph is strongly connected.

For a fixed root \(x\) let \(D=\operatorname{supp}(H_W(x)\oplus\bar x)\). Under a word exchange set \(P=\operatorname{supp}(H_W(x)\oplus H_{W'}(x))\). Under a root move \(x\to x\oplus e_i\), instead set
\[
P=\operatorname{supp}\bigl(e_i\oplus H_W(x)\oplus H_W(x\oplus e_i)\bigr)
\subseteq T_W(\{i\}).
\]
In either case the new Hamming defect minus the old one is
\[
\boxed{|P|-2|P\cap D|.}\tag{BT4}
\]
This follows by toggling precisely the defect indicators indexed by \(P\). Hence every rooted simple-bigon local minimum satisfies \(2|P\cap D|\le |P|\) for every admissible elementary exchange and every one-bit root move. In particular an exchange pulse supported in the nonempty set of defective bits strictly improves the defect. The affine four-cube local-minimum note supplies a positive-defect example satisfying all these inequalities.


#### Bigon square spanning and normal generation of full curvature

Let \(n\ge4\). Recall the admissible simple-bigon word \(W(\pi,A)=(\pi|_A)\pi(\pi|_B)\), where the first letter of \(\pi\) belongs to \(B=[n]\setminus A\) and its last letter belongs to \(A\). Regard \(W\) as a length-\(2n\) cycle in the uncolored cube based at an arbitrary vertex \(z\).

**Theorem (two bigons span any square).** Every square-face cycle \(S\) of \(Q_n\) is the symmetric difference of the edge sets of two translated simple-bigon cycles of this family:
\[
\boxed{S=C(W(\pi,A),z)\mathbin{\triangle} C(W(\pi',A),z).}\tag{BS1}
\]
Moreover, \(\pi'\) differs from \(\pi\) by one adjacent transposition of two interior labels belonging to opposite classes \(A,B\). Consequently the simple-bigon cycles, allowing arbitrary base vertices, span the full binary cycle space of \(Q_n\).

*Proof.* Let the two directions of the prescribed square be \(i,j\). Choose two further distinct directions \(k,l\notin\{i,j\}\). Order the remaining labels arbitrarily as \(R\), and put
\[
\pi=(k,i,j,R,l),\quad
\pi'=(k,j,i,R,l),\quad
A=\{i,l\}.
\]
The first direction \(k\) belongs to \(B\), the last \(l\) to \(A\), and both parameter pairs satisfy the simple-bigon admissibility condition. Swapping \(i,j\) changes neither restricted outer word: \(\pi|_A=\pi'|_A=(i,l)\) and \(\pi|_B=\pi'|_B=(k,j,R)\). Thus
\[
W(\pi,A)=P\,i\,j\,S,\qquad
W(\pi',A)=P\,j\,i\,S
\]
with common prefix \(P=(i,l,k)\) and common suffix \(S\). The two projected cycles share all edges except for the two alternative length-two routes across the \(ij\)-square whose initial vertex is \(z\oplus e_i\oplus e_l\oplus e_k\). Choose \(z\) so that this equals any prescribed square corner. Their symmetric difference is the four-edge square (BS1). Because square-face boundaries generate the binary cycle space of \(Q_n\), the spanning conclusion follows. \(\square\)

**Theorem (bigon holonomies normally generate the derived swap group).** For any involutions \(U_1,\ldots,U_n\) on a common set, \(n\ge4\), let \(G=\langle U_i\rangle\) and let \(N\) be the normal subgroup of \(G\) generated by all simple-bigon holonomies \(H_{W(\pi,A)}\). Then
\[
\boxed{N=G'=[G,G].}\tag{BS2}
\]
In particular, this holds for all legal nonlinear red-swap systems of NORI1.

*Proof.* Every word \(W(\pi,A)\) uses each involution twice, so its image lies in \(G'\), hence \(N\subseteq G'\). For any distinct \(i,j\), the two admissible words from (BS1) differ only by the central interchange \(ij\leftrightarrow ji\). The exchange transport identity therefore gives
\[
H_{W'}H_W^{-1}=H_S(U_iU_j)^2H_S^{-1}.
\]
Both holonomies belong to \(N\), and \(N\) is normal, so \((U_iU_j)^2\in N\). Pairwise commutators \([U_i,U_j]=(U_iU_j)^2\) normally generate the derived subgroup of an involution-generated group. Thus \(G'\subseteq N\). \(\square\)

**Low-dimensional boundary.** The preceding construction requires two interior positions and therefore dimension at least four. In dimension three, simple-bigon word cycles, even after arbitrary translations, have only four distinct edge supports: each is the six-cycle obtained by deleting an antipodal pair of vertices from \(Q_3\). Their binary span has dimension three (their sum is zero), whereas the cube cycle space has dimension \(12-8+1=5\). Thus the square-spanning statement fails for this restricted bigon family in dimension three. Dimension two has its single square, itself a bigon.

**Scope.** (BS2) establishes full *normal generation* and, together with the commutator-orbit theorem, permits arbitrary products of conjugated simple-bigon holonomies to reach every vertex in an antipodal-containing red component. It does not force one length-\(2n\) holonomy map to have an antipodal value. The resulting problem is a bounded-word concentration of normally generated curvature rather than an absence of available curvature generators.


#### Rootwise square curvature and bigon-exchange activity

#### Rootwise square curvature and bigon-exchange activity

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

#### Normal generation by embedded antipodal bigon loops

#### Normal generation by embedded antipodal bigon loops

Let \(F_n=*_{i=1}^n C_2=\langle s_1,\ldots,s_n\mid s_i^2=1\rangle\), and let \(F_n'\) be its derived subgroup. Let \(\mathscr B_n\) consist of direction words \(W(\pi,A)=(\pi|_A)\pi(\pi|_B)\), \(B=[n]\setminus A\), where \(\pi\) is a permutation, \(A\) contains its last letter and omits its first, and both parts are nonempty.

**Theorem 1 (normal-generation threshold).** For \(n=2\) and \(n\ge4\),
\[
\boxed{\langle\!\langle s_W:W\in\mathscr B_n\rangle\!\rangle_{F_n}=F_n'.}
\]
For \(n\ge4\), a family of at most \(2\binom n2\) embedded bigon words suffices. In dimension three the normal closure of the eligible bigon elements is a proper subgroup of \(F_3'\).

*Proof.* Each \(W\) uses every generator twice, so lies in \(F_n'\). Fix \(i\ne j\) with \(n\ge4\) and choose distinct other labels \(a,b\). Choose \(\pi\) beginning at \(b\), ending at \(a\), and having \(i,j\) adjacent in its interior. Put \(A=\{i,a\}\); all remaining labels are in \(B\). Exchanging adjacent interior \(i,j\) preserves the two exterior restrictions, so two eligible words have the forms \(W=PijR,\ W'=PjiR\). Their elements satisfy
\[
s_{W'}s_W^{-1}=s_R(s_is_j)^2s_R^{-1}.
\]
A normal subgroup containing both \(s_W,s_{W'}\) therefore contains \((s_is_j)^2=[s_i,s_j]\). All pairwise commutators normally generate \(F_n'\). For \(n=2\), the word \(ijij\) generates the infinite cyclic subgroup \(F_2'\). For \(n=3\), each eligible word is the square of a permutation of all three letters (up to cyclic ordering). Send the three involutions to the three distinct transpositions of \(S_3\); every such square maps to the identity, whereas a pairwise commutator maps to a nontrivial 3-cycle. Thus the normal closure is proper. \(\square\)

**Theorem 2 (cubical cycle-space spanning).** For \(n\ge4\), the mod-two edge cycles of eligible bigons, allowing all base-cube starting vertices, span \(Z_1(Q_n;\mathbb F_2)\). Every elementary \((i,j)\)-square is the symmetric difference of two eligible bigon cycles. In \(Q_3\) the eligible-bigon cycle span has rank three, while the full cycle space has rank five.

*Proof.* Use \(W=PijR\), \(W'=PjiR\) above, and start both walks at the same cube vertex. Their prefixes and suffixes agree, while the two central two-edge walks use opposite sides of a single square, so the mod-two difference is that square's boundary. Translation of the root realizes every \((i,j)\)-square; direction squares span the cube cycle space. In \(Q_3\), the eligible bigons are translated Petrie hexagons, four in total. Each edge is in two of them, giving one relation; their span has rank three because the omitted antipodal vertex pairs distinguish every other binary linear combination. \(\square\)

**Corollary.** For \(n\ge4\), the derived subgroup of any involution-generated red-swap group \(G_c=\langle U_1,\ldots,U_n\rangle\) is normally generated by eligible simple-bigon holonomies. Together with the established red-antipodal connectivity and derived-orbit theorems, a product of conjugates of eligible simple-bigon returns sends some state to its antipode. This does not require any one factor to do so.

**Algebraic obstruction.** On \(\mathbb Z_{12}\), take \(r(v)=v+1,\ t(v)=-v\) and involutions \(s_1=rt,\ s_i=t\) for \(i\ge2\). The derived subgroup of the generated dihedral group contains \(r^6\), which sends each state to its paired opposite. Yet every double-occurrence word acts as \(r^{-2},1\), or \(r^2\) and never as \(r^6\). Hence normal generation plus derived-orbit antipodal transitivity alone cannot force one successful doubled word. This representation is not a legal cube coloring.

*Scope.* The new rooted-curvature exchange-energy theorem supplies local quantitative information unavailable to this abstract dihedral model. Single-word extraction remains open.

#### Antipodal spectral coupling and signed zero modes

Let \(c\) be a legal antipodally odd coloring of \(Q_d\). Write \(A\), \(B\), and \(Q\) for the red, blue, and uncolored adjacency operators; let \(Jf(x)=f(\bar x)\), \(s_i(x)=(-1)^{c_i(x)}\), and \(S=A-B=2A-Q\), so \((Sf)(x)=\sum_i s_i(x)f(x\oplus e_i)\).

**Theorem (fixed antipodal compressions and geodesic trace).** The operators satisfy
\[
A+JAJ=Q,\qquad JSJ=-S.
\tag{SA1}
\]
For \(P_\pm=(I\pm J)/2\),
\[
\boxed{P_\pm A P_\pm=\tfrac12 QP_\pm.}\tag{SA2}
\]
Furthermore,
\[
\boxed{\operatorname{Tr}(JA^d)=2N_R(c),}\tag{SA3}
\]
where \(N_R(c)\) counts undirected red full antipodal geodesics.

*Proof.* Antipodality exchanges red and blue edges; hence \(JAJ=B=Q-A\). Since \(JQ=QJ\), compression to either eigenspace gives (SA2). The entry \((A^d)_{x,\bar x}\) counts red length-\(d\) walks from \(x\) to its antipode. Every such walk traverses all \(d\) directions once, so is a geodesic. The trace sums over roots, counting each unoriented geodesic twice. \(\square\)

**Theorem (balanced signed zero modes).** Let \(d=2m\ge4\) and suppose every vertex has \(m\) incident edges of each color. Then
\[
\boxed{\dim\ker S\ge4,\qquad
\dim\{f:Sf=0,\ Jf=-f\}\ge2.}\tag{SA4}
\]
Equivalently there are at least two linearly independent antipodally odd functions satisfying
\[
\sum_{i:c_i(x)=0}f(x\oplus e_i)=
\sum_{i:c_i(x)=1}f(x\oplus e_i)
\quad\text{for all }x.
\tag{SA5}
\]

*Proof.* Let \(Pf(x)=(-1)^{|x|}f(x)\). Bipartiteness gives \(PSP=-S\), while (SA1) gives \(JSJ=-S\). Because \(d\) is even, \(J\) and \(P\) commute; their four joint eigenspaces \(H_{\varepsilon,\eta}\), indexed by eigenvalue signs \(\varepsilon,\eta\), have dimension \(2^{d-2}\). The symmetric operator \(S\) pairs \(H_{+,+}\) with \(H_{-,-}\), and \(H_{+,-}\) with \(H_{-,+}\). Every such connecting block is square and its transpose governs the reverse map. Balance gives \(S\mathbf1=0\), and the two parity-supported constant functions are separately in \(\ker S\), one in each antipodally even sector. By rank-nullity their opposite antipodally odd sectors each have a zero mode, proving (SA4). \(\square\)

**Theorem (exponential paired-lift nullspace).** Let \(c\) be any legal coloring on \(Q_m\), \(m\ge2\), and let \(C\) be its complementary paired lift on \(Q_{2m}\). Then
\[
\boxed{\dim(\ker S_C\cap\ker(J-I))=
\dim(\ker S_C\cap\ker(J+I))\ge2^m,}
\tag{SA6}
\]
so \(\dim\ker S_C\ge2^{m+1}\).

*Proof.* The horizontal signed weight in direction \(i\) is \(s_i(x)\), and the paired vertical weight is \(-s_i(x)\). For any function \(g:Q_m\to\mathbb R\), put \(f_g(x,y)=g(x\oplus y)\). The horizontal and vertical moves both send \(x\oplus y\) to \((x\oplus y)\oplus e_i\), and their contributions to \(S_C f_g\) cancel. These form \(2^m\) independent zero modes fixed by full antipodality. Since \(S_C\) is symmetric, anticommutes with \(J\), and the two \(J\)-eigenspaces have equal dimension, its off-diagonal blocks are transposes of square matrices. Their nullities coincide, giving at least \(2^m\) antipodally odd zero modes as well. \(\square\)

**Signed curvature versus swap curvature.** Define signed flip involutions \(D_i=\operatorname{diag}(s_i)T_i\), where \(T_i f(x)=f(x\oplus e_i)\). Because \(c_i\) ignores bit \(i\), \(D_i^2=I\), and
\[
\boxed{(D_iD_j)^2f(x)=
(-1)^{\partial_jc_i(x)+\partial_ic_j(x)}f(x).}\tag{SA7}
\]
For reciprocal readers \(c_i=x_j,c_j=x_i\), both derivatives equal one; (SA7) is trivial although the red swaps \(U_i,U_j\) do not commute. Thus signed face flux may cancel mutual red-swap holonomy. The paired-lift zero modes furnish global linear potentials, without a geodesic-length conclusion.


**Corollary (simply connected bigon 2-cell complex).** For \(n\ge4\), form a two-dimensional complex \(X_n\) whose one-skeleton is \(Q_n\), with one disk attached along every translated admissible simple-bigon cycle \(C(W(\pi,A),z)\). Then \(\pi_1(X_n)=1\). For \(n=3\), the analogous complex has binary first-homology dimension two.

*Proof.* Each square is the symmetric difference of two bigon cycles sharing a common prefix and suffix, whose intervening passages are \(ij\) and \(ji\). When both bigon cycles bound disks, concatenating one with the inverse of the other cancels the common suffix, leaving a conjugate of the square loop. Thus every square bounds a nullhomotopic loop in \(X_n\). The ordinary cubical two-skeleton obtained by attaching all squares is simply connected, so \(X_n\) is simply connected. In dimension three the translated bigon cycles have binary rank three inside the cube cycle space of rank five, leaving first-homology dimension two. \(\square\)

This topological completeness does not establish a short antipodal lift: a bigon disk in the added base complex may carry a nontrivial red holonomy, and products of normally generated holonomies remain longer than a single admissible doubled word.


**Theorem (quadratic bigon synthesis for arbitrary even words).** Assume \(n\ge4\), and let \(w\) be any word of length \(L\) in the involutions \(U_1,\ldots,U_n\), with each label occurring an even number of times. Then \(H_w\) can be expressed as a product of at most
\[
\boxed{\binom L2}\tag{BS4}
\]
conjugates of quotients \(H_{W'}H_W^{-1}\), where \(W,W'\) are admissible simple-bigon words differing by one cross-class adjacent transposition. Each quotient itself is a conjugate of one pairwise square commutator. Equivalently, every closed length-\(L\) cube walk is the binary sum of at most \(L(L-1)\) translated admissible bigon cycles.

*Proof.* Sort the \(L\) labels of \(w\) by a fixed direction order, interchanging adjacent unequal labels. At most \(\binom L2\) interchanges are necessary. Once sorted, the associated group word equals the identity, since each generator appears evenly and squares to the identity. Each adjacent interchange replaces \(PijS\) by \(PjiS\), changing its group action by a conjugate of \((U_iU_j)^2\). The two-bigon square realization (BS1) and exchange identity (BS2's proof) express this commutator as a conjugate of a quotient of two admissible bigon holonomies. Telescope across the sorting sequence to obtain the asserted product bound. For the edge-chain formulation, each adjacent interchange changes the closed walk chain by the four-edge boundary of its traversed square, and each such square is the symmetric difference of two translated bigons. The final sorted word consists entirely of immediate backtracks and contributes zero to the binary cycle chain. Thus at most twice the number of interchanges suffices. \(\square\)

In particular, an antipodal-reaching even word of optimal length \(2n+2\delta\) admits such a decomposition with at most \(\binom{2n+2\delta}{2}\) transported bigon quotients. The statement supplies a bounded algebraic synthesis certificate and retains the original word-length obstruction for realizing antipodal displacement with one bigon.


**Corollary (color-independent quotient spectrum and residual antipodal trace).** For the complementary paired lift \(C\) of a legal \(Q_m\) coloring, put \(d=2m\) and let \(\mathcal L=\{f(x,y)=g(x\oplus y):g:Q_m\to\mathbb R\}\). This is an invariant subspace of the red adjacency \(A_C\) and of antipodality \(J\), with \(J|_{\mathcal L}=I\). Under the natural identification \(\mathcal L\simeq\mathbb R^{Q_m}\), one has
\[
\boxed{A_C|_{\mathcal L}=A(Q_m).}\tag{SA8}
\]
Consequently the characteristic polynomial of \(A_C\) is divisible by
\[
\boxed{\prod_{k=0}^{m}(\lambda-m+2k)^{\binom mk}.}\tag{SA9}
\]
Furthermore,
\[
\boxed{\operatorname{Tr}(JA_C^{2m})
=\sum_{k=0}^m\binom mk(m-2k)^{2m}
+\operatorname{Tr}\bigl((JA_C^{2m})|_{\mathcal L^\perp}\bigr).}\tag{SA10}
\]
Since the left side counts rooted red antipodal geodesics, NORI1 for arbitrary legal base colorings is equivalent to the dimension-uniform residual inequality
\[
\boxed{\operatorname{Tr}\bigl((JA_C^{2m})|_{\mathcal L^\perp}\bigr)>
-\sum_{k=0}^m\binom mk(m-2k)^{2m}.}\tag{SA11}
\]

*Proof.* At \((x,y)\), precisely one of the two red directions \(i,m+i\) is available. Both send \(z=x\oplus y\) to \(z\oplus e_i\), so
\[
(A_C f)(x,y)=\sum_{i=1}^{m}g(z\oplus e_i)
\]
when \(f(x,y)=g(z)\). This proves (SA8). The Walsh characters of \(Q_m\) are eigenvectors of \(A(Q_m)\) with eigenvalue \(m-2k\) at Hamming weight \(k\), yielding (SA9). Self-adjointness makes \(\mathcal L^\perp\) invariant under \(A_C\); it is also invariant under \(J\), which fixes \(\mathcal L\). Splitting the trace into these two invariant spaces gives (SA10). The geodesic trace identity (SA3) and preservation of existence of full antipodal geodesics under complementary paired lifting yield (SA11). \(\square\)

The universal positive summand in (SA10) is \(2^m(2m)![t^{2m}](\cosh t)^m\). At \(m=2\) it equals \(32\); for the paired lift of the reciprocal-reader coloring \(c_0=x_1,c_1=x_0\), the antipodal trace is \(8\), so the residual is \(-24\). Thus the invariant quotient spectrum supplies a strictly positive trace contribution, but cancellation from the orthogonal spectral sector is substantial even in a legal coloring. A proof of (SA11) must use the cubical support and antipodal oddness constraints on that sector.


#### Odd-dimensional Pfaffian rigidity of the signed cube operator

**Theorem (odd signed determinant and antipodal Pfaffian).** Let \(d=2m+1\ge3\). For every assignment of real edge weights equal to \(+1\) or \(-1\) on \(Q_d\), its symmetric signed adjacency matrix \(S\) is nonsingular, and \(\det S\) is odd when the weights are integers. If the signs arise from an antipodally odd coloring, then there is an integer \(p(c)\), necessarily odd, such that
\[
\boxed{\det S=p(c)^4>0.}\tag{PF1}
\]
Thus all odd-dimensional legal colorings have invertible signed adjacency, in contrast to the signed zero modes forced by balance in even dimensions.

*Proof.* Over \(\mathbb F_2\), all edge weights reduce to one, so \(S\) reduces to the uncolored cube adjacency \(Q=\sum_{i=1}^dT_i\), where \(T_i\) are commuting bit-flip permutations. Therefore
\[
Q^2=\sum_iT_i^2+2\sum_{i<j}T_iT_j=dI=I
\quad\text{over }\mathbb F_2.
\]
Hence \(\det S\equiv1\pmod2\), proving nonsingularity.

Now assume antipodal oddness. Let \(E\) be the even-parity vertices of \(Q_d\), with \(|E|=2^{d-1}\). Because \(d\) is odd, \(x\mapsto\bar x\) identifies \(E\) with the odd-parity vertices. Index the even vertices by \(u,v\in E\), and put \(M_{uv}=S_{u,\bar v}\). Symmetry of signed adjacency and antipodal reversal of each sign give
\[
M_{vu}=S_{v,\bar u}=S_{\bar u,v}=-S_{u,\bar v}=-M_{uv}.
\]
Thus \(M\) is skew-symmetric. Ordering the full cube vertices as \(E,\bar E\) writes
\[
S=\begin{pmatrix}0&M\\M^\top&0\end{pmatrix}.
\]
Since \(q=|E|=2^{d-1}\) is even, the block determinant gives
\[
\det S=(-1)^q\det(M)^2=\det(M)^2.
\]
The Pfaffian identity \(\det M=\operatorname{Pf}(M)^2\) now yields (PF1) with \(p(c)=\operatorname{Pf}(M)\in\mathbb Z\). The first part shows \(\det S\) odd, hence \(p(c)\) odd. \(\square\)

**Folded-cube parity interpretation.** The matrix \(M\) modulo two is the adjacency of the folded cube \(Q_d/\langle x\mapsto\bar x\rangle\), represented on the even-parity vertices. Its neighbors are \(u\oplus(\mathbf1\oplus e_i)\). These are commuting involutive translations, hence the folded adjacency \(F\) obeys \(F^2=dI=I\) over \(\mathbb F_2\). In particular the number of perfect matchings of the folded cube is odd: its parity equals the Pfaffian of \(M\) modulo two, independently of the legal orientation. The nonzero integer Pfaffian counts these matchings with orientation-dependent signs.

For \(d=3\), enumerating all \(2^6=64\) legal colorings gives \(\operatorname{Pf}(M)\in\{-3,-1,1,3\}\), with frequencies \(8,24,24,8\), respectively. This finite check illustrates the theorem and is not used in its proof.

The invertibility assertion is an integer-parity property of odd cubes, while the fourth-power factorization uses antipodal oddness. It supplies a global spectral invariant without identifying a monochromatic antipodal geodesic.


**Theorem (odd matching cofactors and Pfaffian variation).** Let \(d\ge3\) be odd and \(F_d=Q_d/\langle x\mapsto\bar x\rangle\) its folded cube. The total number of perfect matchings of \(F_d\) is odd, and for each edge \(e\) the number of perfect matchings containing \(e\) is also odd. If \(c\) is a legal antipodally odd coloring and \(p(c)\) the signed Pfaffian defined in (PF1), flipping the color of one antipodal pair of edges changes \(p(c)\) by an integer congruent to \(2\) modulo \(4\). Hence, for a fixed reference coloring \(c_0\),
\[
\boxed{p(c)\equiv p(c_0)+2\,h(c,c_0)\pmod4,}\tag{PF2}
\]
where \(h(c,c_0)\) is the number of antipodal edge orbits on which the colorings differ.

*Proof.* Let \(F\) be the adjacency matrix of the folded cube over \(\mathbb F_2\). As shown above, \(F^2=I\). Let \(M\) be any integer skew-symmetric orientation matrix with \(M_{uv}=\pm1\) on edges and zero elsewhere. Then \(M\bmod2=F\), and \(\operatorname{Pf}(M)\) is odd. Its reduction modulo two is the number of perfect matchings, proving the first assertion. For distinct vertices \(u,v\), the Pfaffian minor obtained by deleting them counts matchings of the remaining graph modulo two. The Pfaffian cofactor identity gives this minor, modulo two, as \(\operatorname{Pf}(M)(M^{-1})_{uv}=F_{uv}\), because \(M^{-1}\bmod2=F^{-1}=F\). In particular the count is odd when \(uv\) is an edge. Adding that edge to a matching of the remaining vertices proves the edge-specific assertion.

Flipping one antipodal color pair reverses the sign of the corresponding skew entry \(M_{uv}=-M_{vu}\). Pfaffian multilinearity implies
\[
p(c')-p(c)=\pm2\operatorname{Pf}(M_{\widehat u,\widehat v}).
\]
The minor Pfaffian is odd for every edge, so this change is congruent to two modulo four. Summing changes along any sequence of flipped edge orbits proves (PF2). \(\square\)

The result supplies an orientation-sensitive parity phase on the space of all legal odd-dimensional colorings. It does not assign a geodesic to a matching and by itself does not imply NORI1.


#### Rook-label invariance versus antipodal-geodesic distance

**Theorem.** For every \(n\ge6\), two legal antipodally odd colorings \(c,d\) of \(Q_n\) can have the same red connected-component partition (hence the same blue partition and the same Wu--Yang rook labels \(v\mapsto(p(v),p(\bar v))\)), yet a common red component \(C\) satisfies, for every antipodal pair \(x,\bar x\) in \(C\),
\[
\boxed{\operatorname{dist}_{R(c)}(x,\bar x)=n+2\lfloor n/6\rfloor,\quad
\operatorname{dist}_{R(d)}(x,\bar x)=n.}\tag{RI1}
\]
The two colorings can also have the same restricted permutation group \(S_{13}\) on their distinguished six-dimensional component.

*Proof.* Use the already certified \(Q_6\) coloring \(c_*\) of antipodal-edge-orbit mask \(\texttt{0x6228f060010108000780d}\). Its red tree component
\[
T=\{0,1,4,8,9,13,29,31,41,45,47,61,63\}
\]
has the unique antipodal pair \(0,63\), at red distance eight. The other red components have sizes \(45,1,1,1,1,1,1,1\). Form \(d_*\) by reversing the colors of the antipodal direction-four edges \((2,18)\) and \((45,61)\): the first becomes blue and the second red. This preserves legality.

The added red edge \((45,61)\) lies within \(T\). The deleted red edge \((2,18)\) lies in the 45-vertex component and has the alternative red route
\[
2,6,22,20,16,18.
\]
Thus every red component retains its vertex set. The newly added red edge yields the six-step full geodesic
\[
0,8,9,41,45,61,63,
\]
whose directions are \(3,0,5,2,4,1\). The old component \(T\) remains a red tree of antipodal distance eight, so the distinguished component has different antipodal-geodesic behavior. Both restricted swap groups on \(T\) are transitive, and in both the direction-one swap is the sole transposition \((61\ 63)\). Since \(|T|=13\) is prime, the same prime-degree argument proves both restricted groups equal the embedded \(S_{13}\).

For \(n=6k+r\), \(k\ge1\), \(0\le r<6\), take \(k\) independent copies of \(c_*\), respectively \(d_*\), and assign each of the final \(r\) directions the rule \(c_j(x)=x_0\), with bit zero belonging to the first six-dimensional block. Each resulting rule ignores its own direction bit and reverses under complementation. Independent products preserve equality of the red component partitions. The added directions permit arbitrary changes of the final \(r\) bits above a base component precisely when the first factor's component contains a vertex with bit zero equal to zero; this criterion depends only on its vertex set and is the same for the two colorings. Their full red component partitions therefore agree.

Both have the distinguished component \(C=T^k\times Q_r\). Each antipodal pair in \(C\) has base endpoints \(0,63\) in every six-dimensional factor. Every red path between such antipodes has at least eight moves per block under \(c\), or six under \(d\), plus \(r\) additional moves. Equality is attained by concatenating shortest red paths in the factors and flipping all added bits while the first block equals vertex zero. This gives distances \(8k+r=n+2k\) and \(6k+r=n\). The blue graph is the antipodal image of the red graph, so the blue component partitions agree; the rook labelings consequently agree. \(\square\)

A component-level invariant (including the red-blue component-incidence matrix and the rook labeling) cannot determine which antipodal-bearing red components contain full antipodal geodesics.


#### Identical global swap groups with distinct geodesic-root sets

**Theorem (group-action indeterminacy).** The two six-dimensional colorings \(c_*,d_*\) in (RI1) have the same subgroup of \(\operatorname{Sym}(Q_6)\) generated by their red swaps. Let \(T\) be the common 13-vertex red component and \(B\) the common 45-vertex component. Their common group is
\[
\boxed{G_{c_*}=G_{d_*}=\{(\sigma,\rho)\in S_T\times S_B:
\operatorname{sgn}\sigma=\operatorname{sgn}\rho\},}\tag{GI1}
\]
acting trivially on the other six vertices. Nonetheless, the numbers of vertices from which a red full antipodal geodesic exists are \(28\) and \(30\), respectively. Taking \(k\) independent products gives, in \(Q_{6k}\), colorings with the same full red swap group and respective red-geodesic root counts
\[
\boxed{28^k\quad\text{and}\quad30^k.}\tag{GI2}
\]
The added-direction extension used in (RI1) preserves the equality of full generated swap groups for every \(n\ge6\).

*Proof.* On \(T\), both restricted swap groups are \(S_{13}\) by the prime-degree single-transposition argument. On \(B\), finite Schreier--Sims computations of the six red swap permutations, constructed from the antipodal-edge-orbit bit mask \(\texttt{0x6228f060010108000780d}\) and the mask with bit 14 reversed, give group order \(45!\) in both cases. This establishes that each restricted group equals \(S_{45}\). The full permutation generators preserve the two components and fix six isolated vertices, so both full groups are subdirect products of \(S_{13}\times S_{45}\). By Goursat's lemma, the only possibilities are the full direct product and its common-sign subgroup: the only nontrivial proper quotients of either symmetric group are their sign quotients \(C_2\), while \(S_{13}\) and \(S_{45}\) are not isomorphic. Every red direction swap on \(Q_6\) is the product of sixteen transpositions and hence is even globally. Therefore its signs on \(T\) and \(B\) agree, and both full groups are contained in the common-sign subgroup. Surjectivity on both factors now forces equality (GI1).

The original red component \(T\) has its unique antipodal pair at red distance eight, while the modified component has the red full antipodal geodesic displayed in (RI1). In the common 45-vertex component \(B\), there are 28 vertices whose antipodes lie in \(B\). Each has a red full antipodal geodesic shared by both colorings; it suffices to exhibit one for each of the fourteen unordered antipodal pairs. The following six-step paths (one per pair) are red in both colorings:
\[
\begin{gathered}
(3,2,6,22,20,52,60),\ (6,22,20,52,60,56,57),\\
(10,2,6,22,20,52,53),\ (17,49,57,59,58,62,46),\\
(19,51,59,58,62,60,44),\ (20,52,60,62,58,59,43),\\
(21,53,55,51,59,58,42),\ (23,55,53,52,60,56,40),\\
(24,56,60,62,54,38,39),\ (25,57,59,58,62,54,38),\\
(26,58,62,60,52,53,37),\ (27,59,58,62,60,52,36),\\
(28,60,62,58,59,51,35),\ (30,62,60,56,57,49,33).
\end{gathered}
\]
All paths use the six directions once; their reversals account for all 28 antipodal roots in \(B\). The isolated components contain no antipodal pairs, and the distinguished component contributes respectively zero and two geodesic roots. This proves the root counts \(28\) and \(30\).

For an independent product of colorings on disjoint sets of directions, the swap group is the direct product of the factor groups. A full red antipodal geodesic exists from a product root precisely if one exists from its root in each factor: necessity follows by projection onto each factor; sufficiency follows by concatenating the factor geodesics. Hence the generated groups remain the same and the numbers of roots multiply, proving (GI2). For the \(r\) added directions in (RI1), the corresponding swaps are identical in both colorings, since their common gate function is \(x_0\), and their base swaps generate the same subgroup on each of the first \(k\) blocks. Adding the same generators preserves the equality of the full groups. \(\square\)

*Finite computation certificate.* The bit-mask convention scans unoriented edges \((u,u\oplus e_i)\) with \(u<u\oplus e_i\), in increasing \(u\), then \(i\). It selects one member of each antipodal orbit upon first encounter; a set mask bit colors that representative red and its opposite blue. Under this convention orbit index 14 is the pair \(((2,18),(45,61))\). For each of the two masks, form the six permutations on \(B\) by interchanging endpoints of each red direction-\(i\) edge and fixing the remaining vertices. Schreier--Sims gives order
\[
45!=119622220865480194561963161495657715064383733760000000000
\]
in both cases. The same computation yields \(13!\) on \(T\). The explicit components, shortest-path checks, and fourteen witnesses above provide independent combinatorial verification of the geometric statements.

Thus the entire generated permutation group and its derived subgroup, even as embedded actions on every cube vertex, do not determine whether a specified antipodal-bearing red component contains a red full geodesic. The labeled generators and their bounded word metric retain information absent from the abstract or embedded group action.


**Corollary (balanced Eulerian twins with common local holonomy groups).** Let \(c_*,d_*\) be the preceding two colorings of \(Q_6\), and take their complementary paired lifts \(C_*,D_*\) on \(Q_{12}\). Both are antipodally odd with six incident red edges and six blue edges at every vertex. Their red and blue connected-component partitions coincide, and the red swaps generate the same restricted permutation group on every one of their common red components.

In particular the common component \(T\times Q_6\), of cardinality \(13\cdot64=832\), satisfies
\[
\boxed{\operatorname{dist}_{R(C_*)}((x,y),(\bar x,\bar y))=14,\qquad
\operatorname{dist}_{R(D_*)}((x,y),(\bar x,\bar y))=12}
\]
for every antipodal pair in it, while in both cases its red swap group is
\[
\boxed{(\mathbb F_2^T)^6\rtimes S_{13},\qquad
\text{derived group }(E_{13})^6\rtimes A_{13}.}
\tag{GI3}
\]
The total numbers of red full-antipodal-geodesic roots in the two \(Q_{12}\) colorings are respectively \(28\cdot64=1792\) and \(30\cdot64=1920\).

*Proof.* For each base red component \(B\) of either coloring, every direction \(i\) is blue at some vertex of \(B\): if \(B\) has an antipodal pair, this follows from antipodal oddness; if \(B\) is a singleton, all its incident edges are blue. The original red components have cardinalities \(13,45,1,1,1,1,1,1\), and each of the two non-singleton components contains antipodal pairs. By the paired-lift component theorem (PL1), the red components of both lifts are the sets \(B\times Q_6\), giving the same partition. The blue partitions are their antipodal images. The paired-lift distance formula (PL2) adds six to every antipodal red distance, proving the displayed distances. By the full symmetric restriction computations in (GI1), both base colorings generate \(S_{13}\) on \(T\), \(S_{45}\) on the other large component, and the trivial group on the singletons. The wreath-product theorem (WP1) therefore gives the same embedded restricted group on each lifted red component: \((\mathbb F_2^B)^6\rtimes S_{|B|}\) for either odd-size large component, and \(C_2^6\) for a singleton. Formula (WP2) gives the derived group on \(T\times Q_6\). A lifted red antipodal geodesic based at \((x,y)\) exists precisely when the base coloring has one rooted at \(x\), and this is independent of \(y\); this follows directly from the two-factor length identity. Multiplying the base root counts by \(2^6\) gives the asserted numbers. \(\square\)

Independent products followed by complementary pairing give, in every dimension \(12k\), perfectly balanced legal colorings with identical red and blue component partitions, identical restricted swap-group actions on each component, and a common regular Eulerian component whose antipodal distances are \(14k\) and \(12k\). The corresponding red-geodesic root counts are \(2^{6k}28^k\) and \(2^{6k}30^k\).


#### Guard lift spectral theorem

### Majority guard lifts: red graph spectrum, antipodal connectivity and rare geodesics

Let \(c\) be any legal antipodally odd binary edge coloring of \(Q_n\) and let \(R_c\) denote its red adjacency matrix. Add bits \(u,v\) and define \(G(c)\) on \(Q_{n+2}\) by
\[
g_u(x,u,v)=1-v,\qquad g_v(x,u,v)=u,\qquad
g_i(x,u,v)=\operatorname{Maj}(1-u,v,c_i(x))\quad(i\in[n]).
\tag{G1}
\]
Here \(\operatorname{Maj}\) is three-input Boolean majority.

**Theorem 1 (graph and spectral decomposition).** The coloring \(G(c)\) is legal and antipodally odd. Its red graph is the disjoint union of an all-red \(n\)-cube on guard layer \(10\), and three layers \(00,01,11\) with red adjacency
\[
\begin{pmatrix}R_c&I&0\\ I&0&I\\0&I&R_c\end{pmatrix}.
\tag{G2}
\]
Consequently, writing \(\mu_\pm(\lambda)=(\lambda\pm\sqrt{\lambda^2+8})/2\), with eigenvalue multiplicities respected,
\[
\boxed{\operatorname{Spec}(R_{G(c)})=
\{n-2j\text{ with multiplicity }\binom nj:0\le j\le n\}
\cup\operatorname{Spec}(R_c)
\cup\!\!\bigcup_{\lambda\in\operatorname{Spec}(R_c)}\!\!\{\mu_+(\lambda),\mu_-(\lambda)\}.}
\tag{G3}
\]
In particular, \(\rho(R_{G(c)})\ge n\).

*Proof.* At guard states \(00,11\), the old-direction red edges are those of \(c\); at \(01\) they are all blue, and at \(10\) all red. Red guard edges form corridors \(00-01-11\), with no red guard edge incident to \(10\). This proves (G2). The antisymmetric combination of layers \(00,11\) carries a copy of \(R_c\). The symmetric combination, together with layer \(01\), yields \(\begin{pmatrix}R_c&\sqrt2 I\\\sqrt2 I&0\end{pmatrix}\). On an eigenvector of \(R_c\) with eigenvalue \(\lambda\), its two eigenvalues solve \(z^2-\lambda z-2=0\). The isolated \(10\) layer is a standard \(Q_n\) with spectrum \(n-2j\). \(\square\)

Write \(\mathcal A(c)=\{x:x\text{ and }\bar x\text{ lie in the same connected component of }R(c)\}\), and \(\mathcal S(c)=\{x:\text{a red full antipodal geodesic starts at }x\}\). Let \(P(c)\) denote the number of unoriented red full antipodal geodesics.

**Theorem 2 (antipodal metric and root sets).**
\[
\boxed{
\mathcal A(G(c))=\mathcal A(c)\times\{00,11\},\quad
\mathcal S(G(c))=\mathcal S(c)\times\{00,11\},\quad
P(G(c))=2(n+1)P(c).
}
\tag{G4}
\]
Moreover, for \(a,b\in\{0,1\}\), the red distance between \((x,a,a)\) and \((y,b,b)\) equals \(d_{R(c)}(x,y)+2[a\ne b]\), allowing infinite distances. Every red full geodesic of \(G(c)\) traverses \(u,v\) consecutively, and deleting them yields a red full geodesic of \(c\). Thus NORI1 holds for \(G(c)\) if and only if it holds for \(c\), and the shortest red antipodal distance surplus is preserved.

*Proof.* Antipodality sends \(00\leftrightarrow11\) and \(01\leftrightarrow10\). The latter states lie in different red connected components. Within the three-layer component, projecting a red path to \(x\) and deleting guard edges gives a red walk in \(c\), and crossing between \(00,11\) takes at least two guard steps. A base red path with one corridor insertion attains the lower bound. A full red geodesic uses each guard direction once, so the two guard edges pass through state \(01\), where every old-direction edge is blue. They must therefore be consecutive. Conversely one can insert the red guard pair in any of \(n+1\) slots of a red base geodesic, in either of the two initial equal guard states. Counting orientations and dividing by two proves (G4). \(\square\)

**Corollary 3 (simultaneously near-maximal spectral radius and sparse antipodal roots).** Let \(\beta\) on \(Q_4\) have rules \(\beta_0=x_1,\ \beta_1=x_0,\ \beta_2=1-x_0,\ \beta_3=1-x_1\). A direct four-label order calculation gives \(P(\beta)=4\), \(|\mathcal S(\beta)|=8\), and the red connected components have sizes 12 and 4, so \(|\mathcal A(\beta)|=8\). For \(h\ge0\) set \(c_h=G^h(\beta)\) and \(N=4+2h\). Then
\[
\boxed{\rho(R_{c_h})\ge N-2,\qquad
\frac{|\mathcal A(c_h)|}{2^N}
=\frac{|\mathcal S(c_h)|}{2^N}=2^{-h-1}=2^{1-N/2},}
\tag{G5}
\]
\[
\boxed{P(c_h)=\frac{N!}{3(h+2)!}.}
\tag{G6}
\]
For a uniformly random legal odd coloring of \(Q_N\), the mean unoriented red-geodesic count is \(N!/2\), since every full geodesic uses \(N\) distinct antipodal edge-orbit variables. Thus
\[
\boxed{\frac{P(c_h)}{N!/2}=\frac{2}{3(h+2)!}.}
\tag{G7}
\]
All these colorings possess monochromatic full geodesics.

*Proof.* Iterating (G3) provides a red isolated \((N-2)\)-cube, hence the spectral-radius bound. Iterating (G4) doubles both root counts at each increase in dimension by two. The recurrence \(P(G(c))=2(n+1)P(c)\) from \(P(\beta)=4\) gives (G6). The counting mean and ratio then follow. \(\square\)

This family disproves any universal assertion that red spectral radius \((1-o(1))N\) entails a positive asymptotic density of red antipodal-connected roots, or that the fraction of all-red geodesics is within an exponential factor of its random-coloring mean. It does not disprove NORI1.

#### Recursive guard-pair order languages and universal test lower bounds

#### Recursive guard-pair order languages and factorial lower bounds for universal path tests

A legal antipodally odd coloring of Q_n has undirected edge rules c_i(x)=c_i(x+e_i), c_i(bar x)=1-c_i(x). A red full geodesic rooted at x with direction order pi has every traversed edge red. Define the majority extension G(c) on Q_(n+2), with new bits u,v, by
\[
g_u(x,u,v)=1-v,\quad g_v(x,u,v)=u,\quad g_i(x,u,v)=\operatorname{Maj}(1-u,v,c_i(x)).
\tag{A1}
\]
At guard states 00,11 the old-direction rules equal c. At state 01 all old directions are blue; and the guard transitions 00 -> 01 -> 11 and 11 -> 01 -> 00 are red. Thus a red full geodesic of G(c) necessarily uses the two guard directions consecutively, and deletion of that pair gives a red full geodesic of c. Conversely, every red geodesic of c lifts by inserting the two guard directions, in either order, into any gap; for a specified root and direction order of c, each insertion and chosen pair order determines a unique guard-root state.

For n=2, use the legal coloring c^2 with rules c^2_1=1-x_2, c^2_2=x_1. Both direction orders admit precisely one red root. For n=3, use the cyclic unary-reader coloring c^3_i=x_(i+1 mod 3); for each direction order the red equations determine every root bit independently, so all six orders admit precisely one red root. For any n>=2, start with c^2 for even n and c^3 for odd n and add h=(n-m)/2 guard pairs, where m is 2 or 3, respectively. Arbitrarily relabel all directions. The chronological sequence of guard pairs will be denoted D_1,...,D_h, with the m base directions forming a terminal set D_0.

**Theorem 1 (recursive order-language theorem).** A direction permutation pi supports a red full geodesic if and only if the newest guard pair D_h is adjacent in pi, and after deleting its two members the reduced permutation supports a red full geodesic at the previous stage. Recursively deleting all h pairs leaves an arbitrary permutation of the m base directions. For every admitted pi there is precisely one red initial vertex. The set L_n of admitted direction orders has cardinality
\[
\boxed{|L_n|=m!\prod_{j=1}^h 2(m+2j-1)
=\frac{n!\,2^h m!!}{n!!},}
\tag{A2}
\]
where !! denotes the double factorial. Equivalently, for even n=2k, \(|L_n|=n!/k!\); for odd n=2k+3, \(|L_n|=n!\,3\,2^k/n!!\).

*Proof.* The majority-gate layer decomposition proves the adjacent-pair deletion characterization. The base coloring has one red root per order, and a new adjacent pair in the extended order has a unique permitted initial guard state determined by its orientation. Thus the unique-root assertion is inherited. For each admitted order of length d, a fresh consecutive pair can be inserted in d+1 positions and in two orientations, so \(|L_{d+2}|=2(d+1)|L_d|\), with \(|L_m|=m!\), yielding (A2). \(\square\)

**Theorem 2 (universal order-list lower bound).** Choose a uniform random assignment of n direction names to the m base positions and h chronological guard pairs. For any fixed direction permutation pi,
\[
\boxed{\Pr(\pi\in L_n)=p_n=\frac{2^h m!!}{n!!}.}
\tag{A3}
\]
Hence any predetermined family F of direction permutations of size strictly less than \(p_n^{-1}\) can be avoided by some legal antipodally odd coloring: no monochromatic full geodesic has an order in F. In particular, for every even n=2k,
\[
\boxed{|F|\ge k!}
\tag{A4}
\]
is necessary for F to contain a monochromatic-geodesic direction order for every legal coloring. In odd dimension n=2k+3, the corresponding lower bound is \(|F|\ge n!!/(3\,2^k)\).

*Proof.* The newest pair under uniform relabeling is a uniform two-element subset of [n]. Among \(\binom n2\) possible pairs, n-1 are adjacent in a fixed pi, giving probability \(2/n\). Conditional on adjacency, deleting the pair leaves uniform assignments of all earlier names; induction gives \(p_n=(2/n)p_{n-2}\), with \(p_m=1\). A union bound gives \(\Pr(F\cap L_n\ne\varnothing)\le |F|p_n<1\). Thus some labeled guard coloring excludes every order in F. Blue full geodesics have the same admitted orders as red ones, because antipodal translation complements the color of every traversed edge without changing the direction order. \(\square\)

**Theorem 3 (rooted-geodesic test lower bound).** Independently translate the labeled guard coloring by a uniform cube translation. Every admitted direction permutation then has a unique red root uniformly distributed over all \(2^n\) roots, and its sole blue root is the antipode. Hence a fixed rooted full geodesic is monochromatic with probability
\[
\boxed{\frac{p_n}{2^{n-1}}.}
\tag{A5}
\]
Consequently, any fixed collection of fewer than \(2^{n-1}/p_n\) full geodesics can be made entirely nonmonochromatic by one legal antipodally odd coloring. For even n=2k the lower bound on the size of a universal full-geodesic test collection is
\[
\boxed{2^{n-1} k!.}
\tag{A6}
\]
The same assertion holds for unoriented geodesics, since path reversal preserves monochromaticity.

*Proof.* Translation preserves both legal edge consistency and antipodal oddness. Conditional on pi being admitted, the root unique to its red geodesic is uniform, as translation acts transitively on Q_n; the unique blue root is antipodal to it. Thus red and blue events are disjoint and each has probability \(p_n/2^n\). Apply a union bound to any prescribed family of paths. \(\square\)

**Examples and finite audit.** Direct enumeration of the even-dimensional canonical guards gives, for n=2,4,6, respectively: admitted-order counts 2,12,120; favorable-root counts 2,4,8; and red unoriented full-geodesic counts 1,6,60. Every admitted order had one red root. The odd-dimensional base at n=3 admits six orders with one root per order, and its n=5 extension admits 48 orders with one red root per order.

**Scope.** The theorem obstructs universal nonadaptive lists of preselected directions or rooted geodesics. It does not obstruct methods that choose paths adaptively from the coloring, and it does not imply the existence or failure of a monochromatic full geodesic in an arbitrary legal coloring.

#### Free-facet fork reduction and bridge selectors

### Free-facet fork reduction and bridge-selector formula for NORI1

Let m>=1. An unrestricted binary edge coloring a of Q_m has undirected edge values a_i(x)=a_i(x+e_i), with no antipodal condition. Red denotes value 0, blue value 1. Write bar x for bitwise complement. For y in Q_m define f_a(y) to be the number of triples (x,P,Q) in which P is a red monotone geodesic from x to y using some direction set S, and Q is a blue monotone geodesic from x to bar y using precisely the complementary direction set [m]\S. Either path may have length zero. The direction subsets are determined by x,y, while different orderings of the same subsets are counted separately. Define F(a)={y:f_a(y)>0}.

For any antipodally odd Boolean vertex labeling d:Q_m->{0,1}, d(bar x)=1-d(x), build a coloring C(a,d) of Q_(m+1), with layer bit t, by
\[
 c_i(x,0)=a_i(x),\qquad c_i(x,1)=1-a_i(\bar x)\quad(1\le i\le m),\qquad
 c_{m+1}(x,t)=d(x).
\tag{F1}
\]
This defines a legal antipodally odd undirected-edge coloring. Conversely, every legal antipodally odd coloring of Q_(m+1) is uniquely of form (F1) after fixing one direction as the last bit.

**Theorem 1 (fork-selector bijection and red path count).** Let P_R(C) denote the number of unoriented red full antipodal geodesics in C, each undirected path counted once. Then
\[
\boxed{P_R(C(a,d))=\sum_{y:d(y)=0}f_a(y).}
\tag{F2}
\]
*Proof.* Orient each red antipodal geodesic from layer t=0 to t=1; every such geodesic crosses the last direction precisely once, say at vertex y. Before this crossing the path is red in the lower facet a, from some x to y using S. The final upper-facet portion from (y,1) to (bar x,1) becomes, after applying the m-dimensional antipodal map and reversing the path, a blue geodesic in a from x to bar y using [m]\S. The bridge at y is red if and only if d(y)=0. Conversely, any fork counted by f_a(y), with d(y)=0, determines one red full antipodal geodesic in C(a,d) by crossing the bridge and reflecting/reversing the blue arm. These constructions are mutually inverse. Reversal of a red full antipodal geodesic uniquely determines its orientation from layer zero to layer one, so the paths counted are unoriented. \(\square\)

**Theorem 2 (minimum, generating polynomial, and equivalent arbitrary-facet conjecture).** Choose one representative y of each antipodal pair of vertices of Q_m, and write \(\mathcal P_m\) for the resulting family of pairs. As d ranges over all antipodally odd vertex labelings, the red geodesic-count generating polynomial is
\[
\boxed{\sum_{d\mathrm{\ odd}}t^{P_R(C(a,d))}
=\prod_{\{y,\bar y\}\in\mathcal P_m}
\left(t^{f_a(y)}+t^{f_a(\bar y)}\right).}
\tag{F3}
\]
In particular,
\[
\boxed{\min_{d\mathrm{\ odd}}P_R(C(a,d))
=\sum_{\{y,\bar y\}}\min(f_a(y),f_a(\bar y)).}
\tag{F4}
\]
Thus the unrestricted NORI1 conjecture in dimension m+1 is equivalent to the following assertion about **all** undirected binary edge colorings a of Q_m, without any antipodal constraint:
\[
\boxed{\exists y\in Q_m:\quad f_a(y)>0\quad\text{and}\quad f_a(\bar y)>0.}
\tag{F5}
\]
Equivalently, \(F(a)\cap\overline{F(a)}\ne\varnothing\). Indeed, an odd labeling d selects precisely one of y,bar y to have value zero, independently for each pair. Equations (F3)-(F4) follow from (F2). All eligible odd colorings arise from (F1), and any monochromatic antipodal geodesic can be taken red by antipodal translation, so positivity of (F4) is equivalent to the unrestricted conjecture at the stated dimension. \(\square\)

**Theorem 3 (Cartesian product).** For arbitrary edge colorings a of Q_m and b of Q_l, define their Cartesian product a boxplus b on Q_(m+l) by taking each factor rule independently. Then
\[
\boxed{F(a\boxplus b)=F(a)\times F(b).}
\tag{F6}
\]
Indeed, restricting the two arms of any fork to each block produces a fork in that block. Conversely, forks of both factors combine, with the two red arms interleaved and the two blue arms interleaved, to form a fork of the product. Therefore
\[
F(a\boxplus b)\cap\overline{F(a\boxplus b)}
=(F(a)\cap\overline{F(a)})\times(F(b)\cap\overline{F(b)}).
\tag{F7}
\]

**Corollary 4 (exponentially sparse forks with surviving antipodal pairs).** On Q_2 let a_1(x)=x_2 and a_2(x)=x_1. Direct enumeration gives
\(F(a)=\{00,01,10\}\), whereas \(F(a)\cap\overline{F(a)}=\{01,10\}\). For the Cartesian h-fold product a_h on Q_(2h), (F6)-(F7) give
\[
\boxed{|F(a_h)|=3^h,\quad |F(a_h)\cap\overline{F(a_h)}|=2^h.}
\tag{F8}
\]
Thus fork endpoints can occupy only a fraction \((3/4)^h\) of the cube, even though the pair assertion (F5) holds. In particular, a proof of (F5) based merely on \(|F(a)|>2^{m-1}\) cannot work dimension-uniformly. A hypothetical fork-antipodal-free coloring remains so after Cartesian product with any other arbitrarily colored cube.

**Computational audit.** Independently implemented fork counts and full-geodesic dynamic programs agreed with (F2) for ten random unrestricted facet colorings in each dimension m=1,...,5. The Cartesian product formula was also checked directly for h=1,2,3. These tests are ancillary to the proofs.

*Scope.* (F5) is equivalent to NORI1, not a proof of it. The value is the elimination of antipodal oddness from the input lower-dimensional coloring and the reduction of every possible legal bridge extension to one vertex-pair support condition, without assuming root abundance, exchange descent, or joint improvement.

#### Universal paired-diamond synchronization

Let \(n\ge2\). For any legal antipodally odd coloring \(c=(c_i)_{i\in[n]}\) of \(Q_n\), and functions \(p_i:\mathbb F_2^n\to\mathbb F_2\) satisfying
\[
p_i(\bar z)=p_i(z),\qquad p_i(z\oplus e_i)=1-p_i(z),\tag{PD1}
\]
color the two direction blocks \(A_i,B_i\) of \(Q_{2n}\), with vertices \((x,y)\), by
\[
C_{A_i}(x,y)=c_i(x)+p_i(y),\qquad
C_{B_i}(x,y)=c_i(y)+p_i(x)\pmod2.\tag{PD2}
\]
Such \(p_i\) exist for every \(n\ge2\): fix \(j(i)\ne i\) and put \(p_i(z)=z_i+z_{j(i)}\).

**Theorem (paired-diamond synchronization and word universality).** The coloring \(C\) is legal and antipodally odd. For every root \(x\), direction permutation \(\pi=(i_1,\ldots,i_n)\), and target bits \(t_1,\ldots,t_n\), there is a unique word among
\[
(A_{i_1}B_{i_1}\text{ or }B_{i_1}A_{i_1})\cdots
(A_{i_n}B_{i_n}\text{ or }B_{i_n}A_{i_n})
\]
whose color sequence from \((x,\bar x)\) is
\[
(t_1,t_1,t_2,t_2,\ldots,t_n,t_n).\tag{PD3}
\]
The resulting path is a full antipodal geodesic. In particular, \(C\) has at least \(2^n n!\) oriented rooted red full geodesics and the same number of blue ones.

*Proof.* The \(A_i\)-rule in (PD2) ignores vertex bit \(x_i\), and the \(B_i\)-rule ignores bit \(y_i\), so they define colors of undirected edges. Complementing all \(2n\) vertex bits complements \(c_i\) and preserves \(p_i\), giving antipodal oddness.

Before the pair \(A_i,B_i\) is traversed, suppose the two block states are \((z,\bar z)\). Put \(r=c_i(z)+p_i(z)\). Traversing \(A_i\) then \(B_i\) gives colors
\[
c_i(z)+p_i(\bar z)=r,\qquad
c_i(\bar z)+p_i(z\oplus e_i)
=(1-c_i(z))+(1-p_i(z))=r.
\]
Traversing \(B_i\) then \(A_i\) instead gives colors \(1-r,1-r\). Thus precisely one of the two orders realizes any prescribed common color \(t\). Both orders terminate at \((z\oplus e_i,\overline{z\oplus e_i})\), allowing induction over the selected permutation. All \(2n\) directions occur once and the final state is \((\bar x,x)\), antipodal to the initial vertex.

For the count, fix target \(t=(0,\ldots,0)\). Every one of the \(2^n\) roots \((x,\bar x)\) and \(n!\) permutations gives a distinct oriented full direction word; injectivity follows by reading the root and the consecutive pair labels. The blue count is identical. \(\square\)

**Sharp local criterion in the separable coupling.** If \(c\) is legal and antipodally odd and the \(p_i\) are antipodally even, then, for every vertex \((z,\bar z)\), the two length-two routes using \(A_i,B_i\) have opposite monochromatic colors if and only if \(p_i(z\oplus e_i)=1-p_i(z)\). This follows from the displayed two-route calculation and also proves that (PD1)'s bit-flip condition is necessary for pairwise word universality in this separable form.

These paired-diamond channels admit unrestricted nonlinear base rules \(c_i\), as well as nonlinear coupling rules \(p_i(z)=z_i+h_i(z_{-i})\) for any antipodally odd Boolean \(h_i\). Their construction supplies a monochromatic full geodesic without a counting or averaging argument. It is a sufficient family, not a deduction of a geodesic in the original base coloring: the chosen pair orders encode and can compensate for an arbitrary underlying geodesic color word.


**Corollary (simultaneous red and blue geodesically isometric cubical subdivisions).** Under the hypotheses of (PD1)-(PD2), put \(D_z=(z,\bar z)\) for \(z\in Q_n\). For each cube edge \(zz'\) in direction \(i\), the two different length-two \(Q_{2n}\)-paths between \(D_z,D_{z'}\), with intermediate vertices \((z\oplus e_i,\bar z)\) and \((z,\bar z\oplus e_i)\), are monochromatic of opposite colors. Choose the red path for each edge, and separately choose the blue path. Then each collection is an embedded one-subdivision of \(Q_n\), with common branch set \(\{D_z:z\in Q_n\}\); the sets of internal vertices for the red and blue subdivisions are disjoint.

*Proof.* The two-color statement is the route calculation in the preceding theorem. An intermediate vertex \((u,v)\) of either route satisfies \(u\oplus\bar v=e_i\), identifying the virtual direction \(i\). Moreover it is incident to precisely the two branch vertices \(D_u,D_{u\oplus e_i}\), so distinct virtual edges yield distinct intermediate vertices. Each virtual edge uses its two possible intermediate vertices for the opposite-colored routes. Thus each fixed-color family embeds the subdivision of \(Q_n\), with no internal collisions, and the two families have disjoint internal vertex sets. \(\square\)

In particular, for any \(u,v\in Q_n\) and \(\varepsilon\in\{0,1\}\), the monochromatic graph of color \(\varepsilon\) has
\[
\boxed{\operatorname{dist}_{C,\varepsilon}(D_u,D_v)=2d_H(u,v)
=\operatorname{dist}_{Q_{2n}}(D_u,D_v).}\tag{PD4}
\]
Indeed every shortest \(u\)-to-\(v\) path of \(Q_n\) lifts along its chosen color subdivision to a path of length \(2d_H(u,v)\). This meets the ambient distance lower bound, so the monochromatic distance is equal to it. Moreover at least \(d_H(u,v)!\) distinct shortest monochromatic paths exist between the two branch vertices, obtained by permuting the differing virtual directions. Thus both colors simultaneously realize every ambient geodesic distance on the anti-diagonal branch set. The conclusion is independent of all nonlinear details of \(c\) and of the choices of \(p_i\) within (PD1).


##### Sparse diagonal-diamond certificate and full realization count

Fix \(n\ge2\), group the \(2n\) directions into \(A_i,B_i\) for \(i\in[n]\), and put \(D_z=(z,\bar z)\in Q_{2n}\). For each virtual edge \(\{z,z\oplus e_i\}\) in \(Q_n\), its *diagonal diamond* is the square in directions \(A_i,B_i\) connecting \(D_z\) and \(D_{z\oplus e_i}\). All the edges of distinct diagonal diamonds are disjoint: any nonbranch intermediate vertex \((u,v)\) satisfies \(u\oplus\bar v=e_i\), identifying the virtual direction, and is incident within the diamonds only to \(D_u,D_{u\oplus e_i}\).

**Theorem (intrinsic diamond criterion).** For any binary undirected-edge coloring \(C\) of \(Q_{2n}\), assume that each diagonal diamond has two opposite-colored monochromatic length-two routes between its diagonal branch vertices. Then the red and blue graphs each contain an internally disjoint one-subdivision of \(Q_n\) with shared branch set \(\{D_z\}\), and every branch-vertex pair is connected in each color by an ambient shortest path. In particular,
\[
N_R(C)\ge2^n n!,\qquad N_B(C)\ge2^n n!,
\]
where these counts refer to oriented rooted full antipodal geodesics. Neither antipodal oddness nor a separable formula for \(C\) is required for this implication.

*Proof.* Select the red length-two route in each virtual edge's diamond, and separately its blue counterpart. The disjointness of intermediate vertices proves both are one-subdivisions. A dimension-simple path in the virtual \(Q_n\) lifts in either color to a path using both corresponding directions \(A_i,B_i\) for each virtual direction it traverses. Between \(D_u,D_v\), its length is \(2d_H(u,v)\), equal to the ambient Hamming distance. In particular each root \(D_x\) and each virtual permutation provide distinct red and blue antipodal full geodesics, proving the counts. \(\square\)

**Theorem (all legal odd diamond certificates).** Let \(C\) additionally satisfy antipodal oddness on \(Q_{2n}\), and define the diagonal departure bit
\[
r_i(z)=C_{A_i}(D_z).
\]
Every diamond has the two opposite monochromatic routes if and only if
\[
\boxed{r_i(z\oplus e_i)=1-r_i(z),\qquad
r_i(\bar z)=1-r_i(z)}\tag{PD5}
\]
and its four edge colors agree with
\[
\begin{array}{c|cc}
\text{two-step route from }D_z&\text{first edge}&\text{second edge}\\
A_i B_i&r_i(z)&r_i(z)\\
B_i A_i&1-r_i(z)&1-r_i(z).
\end{array}\tag{PD6}
\]
Conversely, every family of functions \(r_i\) satisfying (PD5) prescribes a consistent coloring on all diagonal diamonds by (PD6), and extends to a legal odd coloring of the entire \(Q_{2n}\) by independently coloring every antipodal edge pair outside those diamonds.

*Proof.* Under the diamond property, the \(A_i\)-departure at \(D_{z\oplus e_i}\) is the last \(A_i\)-edge of the opposite \(B_iA_i\) route based at \(D_z\), proving the first condition. Antipodal oddness gives the second. Conversely the first relation makes (PD6) agree whether an edge is described from \(D_z\) or \(D_{z\oplus e_i}\), while the second makes its antipodal mate complementary. Distinct diamond edge sets are disjoint, so no other compatibility condition is needed. The complement of their union is stable under the ambient antipodal involution, permitting independent extension. \(\square\)

Each \(r_i\) has the form \(r_i(z)=z_i+q_i(z_{-i})\), where \(q_i\) is antipodally even on the remaining \(n-1\) bits. Thus there are \(n2^{n-2}\) free diagonal-channel bits. The ribbon comprises \(n2^{n+1}\) ordinary edges, or \(n2^n\) antipodal edge orbits, while \(Q_{2n}\) has \(n2^{2n-1}\) antipodal edge orbits altogether. Consequently the number of legal odd colorings satisfying this fixed diamond certificate is
\[
\boxed{2^{\,n2^{2n-1}-n2^n+n2^{n-2}}.}\tag{PD7}
\]
The certificate constrains only a fraction \(2^{1-n}\) of all antipodal edge orbits; every other edge-orbit bit may be assigned arbitrarily. For \(n=2\), exhaustive enumeration of all \(2^{16}\) legal \(Q_4\) colorings confirms the value \(2^{10}=1024\).

In the separable construction (PD2), the correspondence is \(r_i(z)=c_i(z)+p_i(z)\). Because \(p_i\) is antipodally even and flips under \(e_i\), this is a bijection between legal base rules \(c_i\) and all permissible diagonal-channel rules \(r_i\) for each fixed \(p_i\). Hence the intrinsic diamond certificate retains the full nonlinear freedom of every legal \(Q_n\) edge coloring on its channel data while freely allowing perturbation on all remaining ambient edge orbits.


##### Universal ordered two-direction connector and sharp pivotal support

Let \(n\ge2\), and let \(c_i(x)=c_i(x+e_i)\in\mathbb F_2\) be an arbitrary antipodally odd coloring of the undirected edges of \(Q_n\). No bound on nonlinear dependence or influence feedback is imposed.

**Theorem (ordered-pair three-edge connector).** For every ordered pair of distinct directions \((i,j)\) and each color \(b\in\mathbb F_2\), there is a monochromatic \(b\)-colored direction-simple path of length two or three which uses direction \(i\) before direction \(j\). If no monochromatic two-edge path of color \(b\) has order \(i,j\), then
\[
c_i(x)=g(x_I),\qquad c_j(x)=1+g(x_I),\qquad I=[n]\setminus\{i,j\},
\tag{OP1}
\]
for an antipodally odd function \(g:Q_I\to\mathbb F_2\). Moreover, under (OP1), a direction \(k\in I\) supports a red path with word \(i,k,j\) if and only if \(\partial_k g\) is nonzero at some input. The analogous assertion holds for blue.

*Proof.* It suffices to treat red. Suppose no red two-step path has direction order \(i,j\). Applying the antipodal involution to any blue path of that direction order would produce a red one, so no blue two-step path of that order exists either.

Fix the other direction bits \(y\in Q_I\), and consider the square in directions \(i,j\). Its two \(i\)-edges have colors \(A_0,A_1\), indexed by the \(j\)-bit, and its two \(j\)-edges have colors \(B_0,B_1\), indexed by the \(i\)-bit. Every choice of an \(i\)-edge color \(A_\alpha\) and a \(j\)-edge color \(B_\beta\) is realized by an ordered two-step path \(i,j\) from a suitable square corner. Since none of these four paths is monochromatic, \(A_\alpha\ne B_\beta\) for all \(\alpha,\beta\). Thus \(A_0=A_1=g(y)\) and \(B_0=B_1=1+g(y)\). Varying \(y\) proves (OP1). Antipodal oddness of \(c_i\) makes \(g(\bar y)=1+g(y)\); therefore \(I\ne\varnothing\) and \(g\) is nonconstant.

Choose any edge \(y,z=y+e_k\) with \(g(y)=0,g(z)=1\). At any fixed \(i,j\) bits, the two \(k\)-edges along this edge and its antipodal mate have opposite colors. Select the red one and orient it from its \(g=0\) endpoint to its \(g=1\) endpoint. At the first endpoint we can prepend a red \(i\)-edge, and at the second append a red \(j\)-edge, since the two edge rules ignore both the \(i\)- and \(j\)-bits. This gives the required red word \(i,k,j\). Conversely a red word \(i,k,j\) under (OP1) starts with \(g=0\) and ends with \(g=1\), so \(\partial_k g\) must be nonzero somewhere. Taking the antipodal image gives the corresponding statement in blue. \(\square\)

**Sharpness.** Three edges can be necessary: on \(Q_3\) take \(c_i=x_k,\ c_j=1+x_k,\ c_k=x_i\), for distinct directions \(i,j,k\). These are legal and odd; no monochromatic two-step path uses both \(i,j\), while a red path ordered \(i,k,j\) exists. Prescribing three consecutive direction labels in a monochromatic path is not always possible: the legal odd rules \(c_0=x_1,\ c_1=x_0,\ c_2=1+x_0\) forbid a red full three-edge path with order \(0,1,2\), because its \(1\)- and \(2\)-direction edges necessarily have opposite colors.

**Algorithm.** Given oracle access to the edge rules and an ordered pair \((i,j)\), test the \(ij\)-faces at \(y=0^I\) and \(y=1^I\) for a red ordered two-step path. If neither admits one, antipodal oddness shows both faces have the opposite constant-direction coloring of the proof, with \(g(0^I)\ne g(1^I)\). Repeatedly test the face at the Hamming midpoint of two such unfavorable faces, and retain the half-interval with differing \(g\)-values unless a red two-step route is found. After at most \(\lceil\log_2|I|\rceil\) bisections there are adjacent unfavorable faces where \(g\) changes, and the antipodal red pivotal \(k\)-edge yields \(i,k,j\). Thus a witness is constructed with \(O(\log n)\) edge-color evaluations for \(n\ge3\), and a constant number for \(n=2\). This procedure uses no influence-graph information.


**Sharp oracle-query complexity.** The \(O(\log n)\) algorithm for a prescribed ordered pair \((i,j)\) has optimal deterministic query order in \(n\). Fix a hidden direction \(k\) from the set \(I=[n]\setminus\{i,j\}\), and define
\[
c_i(x)=x_k,\qquad c_j(x)=1+x_k,\qquad c_\ell(x)=x_i\quad(\ell\in I).
\tag{OP2}
\]
Every choice of \(k\) gives a legal antipodally odd coloring. No red two-edge ordered path \(i,j\) exists, and by the pivotal-support characterization a red direction-simple path with ordered word \(i,\ell,j\) exists if and only if \(\ell=k\). Thus the direction sequence of any correct output path of length at most three uniquely identifies the hidden index \(k\). All edge-color queries outside directions \(i,j\) are independent of \(k\); each query within \(i,j\) returns only one bit of information about \(k\). A deterministic decision tree identifying one of \(n-2\) possibilities has depth at least \(\lceil\log_2(n-2)\rceil\). Together with the antipodal-bisection upper bound, constructing a prescribed-order red connector of length at most three has worst-case deterministic edge-query complexity \(\Theta(\log n)\) for \(n\ge4\), with edge-color oracle access and the two direction labels supplied.

**Finite audit.** Enumerating every one of the \(2^{16}=65536\) legal odd colorings of \(Q_4\) confirmed that directions \(0,1\), in that prescribed order, occur in a red direction-simple path of length two or three. The proof above applies in every dimension without any computational assumption.


##### Ordered-connector counting: a cut identity and threshold suppression

Fix an ordered direction pair \((i,j)\) in a legal antipodally odd coloring \(c\) of \(Q_n\). Let \(U=\{z:c_i(z)=0\}\), \(V=\{z:c_j(z)=0\}\); each is antipodally complemented. Let \(N_2(i,j)\) count rooted red two-edge paths with direction word \(ij\), and \(N_3(i,j)\) count rooted red three-edge paths with word \(ikj\) for any \(k\notin\{i,j\}\). These are oriented rooted path counts.

**Proposition (two-edge count and antipodal crossing lower bound).** Define \(A=U\setminus V\) and \(B=V\setminus U=\bar A\). Let \(E_\times\) be the number of undirected cube edges with directions outside \(\{i,j\}\) joining \(A\) to \(B\). Then
\[
\boxed{N_2(i,j)=|U\cap V|,\qquad N_3(i,j)\ge \tfrac12 E_\times.}\tag{OC1}
\]
The second bound follows independently of all colors on directions outside \(\{i,j\}\).

*Proof.* A red \(ij\)-path starts at \(z+e_i\), uses its red \(i\)-edge to reach \(z\), then crosses the red \(j\)-edge from \(z\); it exists precisely when \(z\in U\cap V\). This gives the first identity. For each undirected \(k\)-edge joining \(A\) to \(B\), orient it from \(A\) to \(B\). Its color is red or blue. The antipodal edge also joins \(A\) to \(B\) and has opposite color, because antipodal translation exchanges \(A,B\). The red edge in each such antipodal pair, preceded by its red \(i\)-edge and followed by its red \(j\)-edge, gives one red word \(ikj\). There are \(E_\times/2\) antipodal pairs, proving the lower bound. \(\square\)

**Theorem (sharp obstructed-case connector count).** Suppose no red \(ij\)-path of length two exists. Then the same is true in blue. The two edge rules are \(c_i=g(y)\), \(c_j=1+g(y)\), where \(y\) consists of the \(m=n-2\) remaining bits and \(g(\bar y)=1+g(y)\). Let \(\partial g\) be the undirected edge boundary between \(g^{-1}(0)\) and \(g^{-1}(1)\) in \(Q_m\). Then
\[
\boxed{N_3(i,j)=2|\partial g|\ge2^{n-2}.}\tag{OC2}
\]
Equality holds if and only if \(g\) is one remaining input bit or its complement.

*Proof.* A red word \(ikj\) crosses a \(k\)-edge from a \(g=0\) state to a \(g=1\) state. For every undirected crossing edge of \(g\) there are four choices of the \(i,j\)-bits along the pivot; the antipodal symmetry pairs the resulting four edges so that two are red and two blue, counting over all boundary edges. Each red middle edge gives one red rooted \(ikj\)-path, proving the identity. Since \(g\) is antipodally odd, it is balanced. The binary edge-isoperimetric inequality gives \(|\partial g|\ge2^{m-1}\). Equality for a balanced Boolean subset holds only for a codimension-one face, or its complement, so \(g\) must be a dictator or its complement. \(\square\)

**Theorem (threshold suppression when direct connectors are present).** For every odd \(n=m+2\ge5\), put \(m=2t-1\), and let \(w=\sum_{k=2}^{n-1}x_k\) be the Hamming weight of the remaining \(m\) bits. Define
\[
\boxed{
c_0(x)=\mathbf1_{\{w<t\}},\qquad
c_1(x)=
\begin{cases}
\mathbf1_{\{w\ge t+1\}},&x_0=0,\\
\mathbf1_{\{w\ge t-1\}},&x_0=1,
\end{cases}\qquad
c_k(x)=1+x_0\quad(2\le k<n).}\tag{OC3}
\]
This coloring is legal, antipodally odd and nonlinear (for \(m\ge3\)). For the prescribed red ordered pair \((0,1)\),
\[
\boxed{N_2(0,1)=2\binom{m}{t},\qquad N_3(0,1)=0.}\tag{OC4}
\]
In particular,
\[
N_2(0,1)+N_3(0,1)=\Theta(2^n/\sqrt n),
\]
which is smaller than \(2^{n-2}\) for all odd \(n\ge5\) and is an \(O(n^{-1/2})\) fraction of that obstructed-case lower bound. Hence (OC2) cannot be extended to all colorings without its failure-of-length-two hypothesis.

*Proof.* Direction zero reads only \(w\) and ignores bit zero; direction one reads \(w,x_0\) and ignores bit one; other directions read only bit zero, so all rules are consistent with undirected edges. Under antipodal complementation \(w\mapsto m-w\). Since \(m=2t-1\), the threshold at \(w<t\) becomes its complement. For direction one, the two branches interchange under complementation, and the threshold inequalities are complementary; the other rules are plainly odd. Thus the coloring is legal and antipodally odd.

After direction zero is traversed, write \(u=x_0+1\) for the current zero-bit. Its edge is red precisely when \(w\ge t\). The following direction-one edge is red, if \(u=0\), precisely when \(w\le t\), and if \(u=1\), precisely when \(w\le t-2\). Therefore a red \(01\)-path exists only when \(u=0\) and \(w=t\). There are \(\binom mt\) choices of the remaining bits and two free choices of \(x_1\), proving the first identity in (OC4).

For a three-step path \(0,k,1\), the initial red direction-zero step requires \(w\ge t\). If \(u=1\), a single \(k\)-step cannot reduce the weight below \(t-1\), so the final direction-one edge cannot be red. If \(u=0\), the \(k\)-edge color is \(c_k=1\), so it cannot be red. Hence \(N_3=0\). Finally the central binomial coefficient asymptotics yield the last assertion. Direct evaluation in dimensions \(5,7,9\) gives the count pairs \((N_2,N_3)=(6,0),(20,0),(70,0)\), as predicted. \(\square\)

The forcing dichotomy remains valid: if a red \(ij\)-connector of length two is absent, many red three-step connectors must appear. However, the presence of some red two-step connectors can entirely suppress the three-step family while leaving substantially fewer than \(2^{n-2}\) short connectors in total. These are universal and all-dimensional statements, rather than conclusions about bounded-degree or affine subclasses. They expose a bottleneck in extending local connector counts toward NORI1.


**Even dimensions and explicit full red witnesses for the threshold family.** The suppression phenomenon in (OC3)--(OC4) holds for every dimension \(n\ge5\), not only odd dimensions. Let \(m\ge3\) be odd, put \(t=(m+1)/2\), and adjoin \(d\ge0\) extra directions, so \(n=m+d+2\). Define \(w=\sum_{k=2}^{m+1}x_k\). Keep the rules \(c_0,c_1\) from (OC3), and set
\[
c_k(x)=1+x_0\qquad(2\le k<n),
\tag{OC5}
\]
including the \(d\) extra directions. All edge rules ignore their own bits and remain antipodally odd, since the distinguished block of \(m\) bits flips its Hamming weight from \(w\) to \(m-w\), while the extra bits do not enter the first two rules. Then
\[
\boxed{N_2(0,1)=2^{d+1}\binom mt,\qquad N_3(0,1)=0.}\tag{OC6}
\]
Indeed all added root bits are free in a red \(01\)-path; no added direction can serve as a red intermediate step because its red edge requires the zero-bit after direction zero to equal one, whereas at that value the direction-one rule cannot be red after just one remaining-direction flip. Taking \(d=0\) when \(n\) is odd and \(d=1\) when \(n\) is even gives an explicit example in every \(n\ge5\) with \(N_2+N_3=\Theta(2^n/\sqrt n)\) and no red three-step connector of the prescribed direction order.

These colorings nevertheless have full red antipodal geodesics. Choose initial \(x_0=0\) and a Hamming-weight-\(t\) pattern on the distinguished \(m\) bits. Traverse direction zero first, then two directions whose distinguished bits initially equal one, then direction one, and finally all remaining directions in any order. Direction zero is red because the starting weight is \(t\); after flipping it, the other-direction rules are all red since \(x_0=1\). The first two distinguished flips lower the Hamming weight to \(t-2\), so direction one is red. All remaining directions retain red color. Hence this threshold obstruction lives inside legal colorings fully satisfying NORI1 and does not suggest a counterexample to the grand conjecture.


##### Antipodal isodiametric lower bound for ordered short connectors

Let n>=3 and fix ordered directions i,j of an arbitrary legal odd coloring. Let N2 count rooted red paths ij and N3 count rooted red paths ikj, summed over k distinct from i,j. Then

N2+N3 >= binom(n,n/2)/2 for n even, and >= binom(n-1,(n-1)/2) for n odd.

Proof. Let U={x:c_i(x)=0}, V={x:c_j(x)=0}, and A=U minus V. Since U,V each have 2^(n-1) members and bar(A)=V minus U, N2=|U intersect V|=2^(n-1)-|A|. Let E be the number of cube edges joining A and bar(A). By edge consistency none of these is in direction i or j. Antipodal oddness pairs these crossing edges into red-blue pairs. The red member in each pair, oriented from A toward bar(A), together with its red i-edge at the start and red j-edge at the end, forms one rooted red path ikj. Thus N3>=E/2. Each crossing-edge antipodal pair is given by a pair of vertices a,b in A and edges {a,bar(b)} and {b,bar(a)}. Delete at most one of a,b per pair. The surviving set A' has |A'|>=|A|-E/2 and no edge to its antipodal image. Since A' and bar(A') are disjoint, its Hamming diameter is at most n-2. Kleitman's sharp cube isodiametric theorem gives |A'|<=M_n, where M_n=sum_(r=0)^(m-1) binom(2m,r) for n=2m and M_n=2sum_(r=0)^(m-1) binom(2m,r) for n=2m+1. Consequently N2+N3 >=2^(n-1)-M_n, the asserted values. The odd-dimensional threshold construction of (OC3) attains the odd bound: for n=2m+1>=5, N2=2binom(2m-1,m)=binom(2m,m) and N3=0. The theorem applies to any prescribed color target for each direction of the short path by flipping direction-color labels before the proof. Exhaustive Q4 enumeration gives minimum N2+N3=4, whereas this general theorem gives three; no even-dimensional sharpness is claimed.


##### Robust three-step connector abundance near the obstructed branch

For a legal odd coloring of Q_n, n>=3, fix ordered directions i,j and let q=N2(i,j) be the number of rooted red two-edge paths ij. Then

N3(i,j) >= max(0, 2^(n-2)-4(n-2)q).

Proof. Put m=n-2 and index ij-squares by their remaining bit pattern y in Q_m. Let q_y count red ordered ij paths inside square y, so sum_y q_y=q. Call y good when q_y=q_(bar y)=0. Since each face with positive q_y makes at most two members of its antipodal pair bad, the set B of non-good faces has |B|<=2q and is antipodally invariant. Each good square has neither a red nor a blue ij-route: a blue route would become red in its antipodal mate. Hence the two i-edges of square y have one common color g(y), while its two j-edges have color 1+g(y). The function g on the good faces obeys g(bar y)=1+g(y).

Extend g arbitrarily to an antipodally odd Boolean function on all Q_m, choosing complementary values on each missing antipodal pair. This extension is balanced, so the edge-isoperimetric inequality of Q_m gives at least 2^(m-1) undirected edges across which its value changes. At most m|B|<=2mq of these edges touch a bad face. Thus at least 2^(m-1)-2mq boundary edges have both endpoints good. Their collection is invariant under antipodal translation. Each antipodal pair of such boundary edges in Q_m lifts to eight middle-direction edges in Q_n across the two ij-fibers; the eight split into four complementary antipodal color pairs, furnishing four red ordered three-edge connectors ikj. Hence each good-good boundary edge contributes on average two red three-step connectors, and N3>=2(2^(m-1)-2mq)=2^m-4mq. Negative lower bounds may be replaced by zero. When q=0, the bound recovers the sharp N3>=2^(n-2) theorem; when q is small, it proves robustness under exceptional direct paths. Combining this with the isodiametric estimate in the preceding result gives N3>=max(0,2^(n-2)-4(n-2)q,T_n-q), where T_n is the parity-dependent central-binomial connector bound.
