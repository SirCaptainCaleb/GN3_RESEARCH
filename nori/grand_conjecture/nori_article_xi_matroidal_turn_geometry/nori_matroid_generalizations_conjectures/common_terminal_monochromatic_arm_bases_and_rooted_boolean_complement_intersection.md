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
