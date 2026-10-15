# Common-terminal monochromatic arm bases and rooted Boolean complement intersection

# Common-terminal monochromatic arm bases and rooted Boolean complement intersection

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

## Parallel-extension graphic matroid

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

## Rooted Boolean-lattice complement formulation

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

## Unification with NORI1

The cube's free-resource automaton already gives rooted color-zero reachability families \(R_x\subseteq2^{[n]}\), and Article XI proves NORI1 equivalent to the existence of a root \(x\) for which
\[
\boxed{\exists S:\quad S,\ [n]\setminus S\in R_x.}
\tag{7}
\]
Theorem 3 now places the ordinary boundary spanning one-turn conjecture in **the identical formal rooted complement-pair template**, but on original-vertex subsets \(V\setminus\{v\}\). The resource independence of two boundary arms is captured by the parallel-extension graphic matroid \(\mathsf R_n^{(2)}\), while cube coordinate resource independence is captured by the free matroid. This removes the two-vertex seam-matching constraint from the boundary selector and makes the common open question precise: **under which shared intrinsic polarized-exchange axioms must a rooted monochromatic reachable-set family intersect its Boolean complement image?**

These results are equivalences and sufficient criteria, not a proof of the required complementary intersection in every coloring.

## 5. Computational obstruction to the majority shortcut

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

## 6. The rooted path-basis polynomial and an integer counting identity

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

## 7. Canonical phase choice at the root and a symmetric-matrix cancellation

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
