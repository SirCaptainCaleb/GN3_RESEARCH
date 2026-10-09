# Maximal uncolored reachability blocker-incidence components must be antipodally exchanged

# Antipodal self-connection obstruction in the maximal-reachability blocker graph

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. Let m denote the largest possible length of a monochromatic geodesic; if m=n, the conjectured monochromatic antipodal geodesic already exists. Suppose therefore \(m<n\), and hence \(m\le n-2\) by the one-coordinate end-extension lemma.

Form the set \(\mathcal T_m\) of unordered endpoint pairs \(\{x,y\}\) at Hamming distance m that are related by the uncolored reachability relation y∈R(x). Each \(P=\{x,y\}\in\mathcal T_m\) has an intrinsic *terminal blocker edge set*
\[
B(P)=\bigl\{\{x,x\oplus e_i\},\{y,y\oplus e_i\}:i\in[n],\ x_i=y_i\bigr\}.
\]
The definitions of \(\mathcal T_m\), B(P), and the following graph do not mention either edge color.

Define the undirected **blocker-incidence graph** \(J_m\) on vertex set \(\mathcal T_m\) by
\[
P\sim P'\quad\Longleftrightarrow\quad B(P)\cap B(P')\ne\varnothing.
\]
The cube-antipodal map \(\tau(P)=\{\bar x,\bar y\}\) preserves \(\mathcal T_m\) and J_m.

**Theorem (color-free terminal connector criterion).** There is a unique monochromatic witness color \(q(P)\in\mathbb F_2\) for each \(P\in\mathcal T_m\). It satisfies
\[
q(P')=q(P)\quad(P\sim P'),\qquad q(\tau P)=1-q(P).
\]
Thus every connected component of \(J_m\) is assigned a single witness color, and the antipodal involution acts *freely on the set of components*: no connected component contains both P and \(\tau P\). Equivalently, if one can force an antipodally self-connected component of this *uncolored reachability-defined incidence graph*, a full monochromatic antipodal geodesic exists.

**Proof.** A monochromatic witness of length m cannot be extended at either endpoint through any coordinate unused by it. Therefore each physical edge in B(P) has color \(1-q(P)\). Because m<n, B(P) is nonempty, so two opposite-color witnesses for the SAME pair P are impossible: one physical blocker edge would have to have both colors. If B(P) and B(P') share an edge e, then c(e)=1-q(P)=1-q(P'), proving edge-coherence and thus component-constancy. Cube antipodality sends each monochromatic witness to a complementary-color witness for \(\tau P\), yielding \(q(\tau P)=1-q(P)\). If a component contained P and \(\tau P\), constancy and antipodal oddness would give q(P)=1-q(P), contradiction. QED.

**Consequences.**
1. The obstruction depends only on the support of R(x) at its *global maximum Hamming rank m*, not on the complete lower-rank reachability relation or any chosen witness paths.
2. For all terminal pairs starting at a fixed root x, if their omitted coordinate sets intersect, they share the blocker edge at x and lie in one J_m-component. Thus terminal witnesses of opposite colors from x must have disjoint omitted sets, forcing \(m\ge n/2\) whenever both witness colors occur at one root.
3. The condition is geometric and root-mobile: a chain of pairs P_0,...,P_t linking P_t=\tau(P_0) may shift endpoints and support sets freely, provided consecutive terminal blocker sets share a physical edge. Each step is witnessed by uncolored reachability.

**Research obligation.** Derive an antipodal self-connection from the coverage and incidence constraints on the collection of all globally maximal reachable pairs. A purely combinatorial theorem about arbitrary antipodally invariant subsets of endpoint pairs would be too strong; the proof must exploit the additional fact that their blockers came from actual maximal monochromatic-geodesic reachability. This precisely separates the topological forcing half from the proven extraction half.
