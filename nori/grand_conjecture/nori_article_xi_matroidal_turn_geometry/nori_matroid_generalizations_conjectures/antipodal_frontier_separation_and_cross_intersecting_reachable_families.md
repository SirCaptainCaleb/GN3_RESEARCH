# Antipodal frontier separation and cross-intersecting reachable families

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
