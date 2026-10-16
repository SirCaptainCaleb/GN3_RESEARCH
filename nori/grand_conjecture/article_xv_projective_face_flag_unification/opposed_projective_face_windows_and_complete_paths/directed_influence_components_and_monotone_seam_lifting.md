# Directed influence components and monotone seam lifting

### Directional influence components and monotone seam insertion

For an arbitrary binary coloring \(f\) of the undirected edges of \(Q_d\), write \(f_i(x)\) for the direction-\(i\) edge color, independent of the bit \(x_i\). Define the **directed influence graph** \(D(f)\) by placing an arc
\[
j\to i\quad\Longleftrightarrow\quad
\partial_jf_i(x)=f_i(x)+f_i(x\oplus e_j)
\]
is nonzero at some cube vertex. This records which direction changes can affect the colors of other directions. The undirected interaction graph forgets these arc directions.

Let \(A_0(f)\) and \(A_1(f)\) denote roots admitting full dimension-simple geodesics with color words \(0^*1^*\) and \(1^*0^*\), and put \(P(f)=A_0(f)\cap A_1(f)\). Define the cross-orientation intersection constant
\[
\kappa_k=\min_{g,h:E(Q_k)\to\{0,1\}}|A_0(g)\cap A_1(h)|.
\tag{1}
\]
The known dimension-one, square, and three-cube favorability results imply
\[
\boxed{\kappa_1=2,\qquad\kappa_2=2,\qquad\kappa_3=4.}
\tag{2}
\]
For \(k=3\), the lower bound follows from \(|A_0(g)|,|A_1(h)|\ge6\) and inclusion-exclusion among eight roots; equality is furnished by the product of an extremal colored square with a constant-colored one-cube. For \(k=4\), the previously recorded computer-assisted result \(m_4=9\) and the crossed-square construction give \(\kappa_4=2\), conditional on that finite computation.

**Theorem 1 (seam-lifting across a one-way dependence block).** Partition the directions as \(R\sqcup S\). Suppose all \(R\)-direction edge colors are independent of the \(S\)-bits, while the \(S\)-direction colors may depend arbitrarily on both their own bits and the \(R\)-bits. Denote the fixed induced \(R\)-coloring by \(f_R\), and the \(S\)-coloring at \(R\)-state \(y\) by \(g_y\). Then
\[
\boxed{|P(f)|\ge\kappa_{|S|}\,|P(f_R)|.}
\tag{3}
\]

*Proof.* Choose \(x\in P(f_R)\). Select an \(R\)-geodesic \(P_0\) from \(x\) with word \(0^a1^{|R|-a}\), and a second geodesic \(P_1\) from the same \(x\) with word \(1^b0^{|R|-b}\). Let \(y_0,y_1\) be the respective \(R\)-vertices immediately after the zero prefix and after the one prefix. Their locations may differ.

By (1), at least \(\kappa_{|S|}\) roots \(z\in Q_S\) belong to \(A_0(g_{y_0})\cap A_1(g_{y_1})\). From each such \(z\), insert a complete \(0^*1^*\) geodesic of the \(S\)-block at the seam of \(P_0\), and a complete \(1^*0^*\) \(S\)-geodesic at the seam of \(P_1\). During an inserted block the \(R\)-bits do not change, so its edge colors come from the stated induced coloring. The remaining \(R\)-steps retain their colors because no \(R\)-edge depends on the \(S\)-bits. Both enlarged paths start at \((x,z)\), use each dimension once, and have the desired opposite monotone words. Therefore every such \((x,z)\) is paired. Counting these distinct roots proves (3). QED.

**Theorem 2 (strongly connected component bound).** Let \(C_1,\ldots,C_t\) be the strongly connected components of \(D(f)\), in topological order of the condensation digraph. Then
\[
\boxed{|P(f)|\ge\prod_{\nu=1}^{t}\kappa_{|C_\nu|}}
\tag{4}
\]
whenever the factors on the right are positive.

*Proof.* For every topological prefix \(R=C_1\cup\cdots\cup C_{\nu-1}\), no edge-color function of a direction in \(R\) depends on a bit belonging to a later component. Such dependence would give a directed arc entering the prefix, contrary to the topological order. Therefore Theorem 1 applies when adjoining \(C_\nu\) to the prefix. Begin with the dimension-zero cube, whose empty root supports both empty monotone words, and multiply the estimates (3) along the component order. QED.

**Corollary 3 (unrestricted nonlinear closure for feedback components of size at most three).** If every strongly connected component of \(D(f)\) has size at most three, then \(P(f)\ne\varnothing\). If \(t_j\) is the number of components having \(j\) dimensions, then
\[
\boxed{|P(f)|\ge2^{t_1+t_2+2t_3}.}
\tag{5}
\]
In particular, when \(D(f)\) is acyclic, every cube vertex is paired, even if its underlying undirected interaction graph is complete.

*Proof.* Insert (2) into Theorem 2. In the acyclic case \(t_1=d\), and the lower bound equals all \(2^d\) roots. QED.

**Corollary 4 (computer-assisted component-size-four extension).** Assuming the previously reported integer-optimization certificate that every coloring of \(Q_4\) has at least nine nondecreasing feasible roots, Theorem 2 extends paired-root existence to all colorings with directed influence components of size at most four, with
\[
\boxed{|P(f)|\ge2^{t_1+t_2+2t_3+t_4}.}
\tag{6}
\]
This extension relies on that finite calculation; Corollary 3 has a noncomputational proof.

**Corollary 5 (feedback-size obstruction for a hypothetical counterexample).** Any paired-root-free coloring must possess a strongly connected directed influence component involving at least four dimensions. Subject to the computer-assisted four-cube bound, the size must be at least five. A directed cycle somewhere is therefore necessary but far from sufficient: feedback must organize into a large mutually dependent block.

**Corollary 6 (NORI1 for facets with small directed feedback components).** Suppose an antipodally odd edge coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) restricts on its lower facet to a coloring whose directed influence components have sizes at most three. Then at least \(2^{t_1+t_2+2t_3}\) distinct directed monochromatic full antipodal geodesics exist, each using a different vertical bridge. The bridge colors are otherwise arbitrary. The same conclusion extends to components of size four subject to the finite four-cube certificate.

*Proof.* Combine Corollary 3 with the universal free-bridge equivalence of the gauge-criticality Subsection. Each paired lower-facet root supplies a monochromatic geodesic across its designated vertical bridge. QED.

**Proof-closure perspective.** The seam-lifting theorem isolates the difficulty inside mutually dependent feedback blocks. Directed acyclic attachments may be absorbed in any dimension without losing dimension-simplicity, and small strongly connected blocks are handled by cross-orientation root intersection. A successful intersection theorem for arbitrary large feedback blocks would propagate automatically through all their directed attachments. The unrestricted NORI1 and ordinary boundary 3-tournament conjectures remain open.### Conditional cross profiles and hybrid feedback-block closure

The universal intersection constants \(\kappa_m\) consider all binary colorings of \(Q_m\). In the directed influence decomposition of one fixed coloring, the next strongly connected block usually encounters only a restricted family of conditional colorings, indexed by earlier-bit assignments. Cross-intersection for that family alone suffices.

For a component \(C_\nu\) following a topological prefix \(R_\nu\), denote the induced \(C_\nu\)-coloring at earlier state \(y\in Q_{R_\nu}\) by \(g_y^{(\nu)}\), and set
\[
\rho_\nu=\min_{y,y'\in Q_{R_\nu}}
|A_0(g_y^{(\nu)})\cap A_1(g_{y'}^{(\nu)})|.
\tag{8}
\]

**Theorem 7 (conditional component product theorem).**
\[
\boxed{|P(f)|\ge\prod_{\nu}\rho_\nu.}
\tag{9}
\]

*Proof.* Fix a paired root and two oppositely monotone full paths in the already constructed prefix. Their zero-to-one and one-to-zero seam vertices are possibly different prefix states \(y_0,y_1\). By the definition of \(\rho_\nu\), at least \(\rho_\nu\) roots of the next block admit both a nondecreasing full geodesic for coloring \(g_{y_0}^{(\nu)}\) and a nonincreasing full geodesic for \(g_{y_1}^{(\nu)}\). Insert these block geodesics into their respective prefix-path seams. All earlier-direction edge colors are independent of the later block bits, so the words remain monotone and the paths remain dimension-simple. Multiply the number of paired roots at each topological stage. QED.

**Corollary 8 (nonlinear star feedback blocks of any dimension).** If the conditional colorings on a component \(C_\nu\) of size \(m\ge2\) all have star interaction graphs, with hub directions and nonlinear functions allowed to vary with the preceding state, then
\[
\boxed{\rho_\nu\ge2^{m-1}.}
\tag{10}
\]
Indeed any two star colorings have at least \(3\cdot2^{m-2}\) roots in their respective required orientations; inclusion-exclusion forces at least \(2^{m-1}\) common roots.

**Corollary 9 (changing square matchings).** Let a component \(C_\nu\) have an even number \(m=2r\) of directions. Suppose each conditional coloring is a Cartesian product of arbitrary colored squares, but the perfect matching \(M_y\) of directions defining its product may depend on the earlier state \(y\). Then
\[
\boxed{\rho_\nu\ge\min_{y,y'}2^{c(M_y,M_{y'})}\ge2,}
\tag{11}
\]
by the all-dimensional crossed-matching intersection theorem. Here \(c(M,N)\) counts the alternating cycles in the multigraph formed by the two matchings.

**Corollary 10 (hybrid component closure).** Every binary edge coloring of \(Q_d\) has a paired root if every strongly connected component of its directed influence graph belongs to at least one of the following classes: a component of size at most three; a component whose conditional colorings are all star colorings; or an even-sized component whose conditional colorings all factor into colored squares, with the pairing permitted to vary between conditional states. The previous computer-assisted four-cube cross bound also permits arbitrary components of size four.

**Unbounded non-star feedback example.** Let \(c\) be one predecessor direction with constant edge color zero, followed by \(2r\) further directions. In the \(c=0\) facet color the further directions by Cartesian copies of a two-direction coloring \(h\) with both cross-dependencies nonzero, using matching \(M=(1,2),(3,4),\ldots,(2r-1,2r)\). In the \(c=1\) facet use the same square coloring along shifted matching \(N=(2,3),(4,5),\ldots,(2r,1)\). The directed influence graph on the later \(2r\) directions contains both orientations of every edge of \(M\cup N\), a connected even cycle. Thus it is one strongly connected feedback block of unbounded size, whose underlying interaction graph is non-star when \(r\ge2\). Still its two conditional colorings are square products, so (11) and (9) give at least four paired roots in the full cube.

**Closure interpretation.** The difficulty is not merely the existence or size of directed feedback, or the lack of a fixed square factorization. The remaining problem is to understand the cross-intersection behavior of conditional favorable-root families inside irreducible feedback components. Theorem 7 localizes the desired structural argument there, without unnecessarily demanding an intersection theorem for every possible coloring of a given order.

### Constructive algorithm for bounded directed feedback components

**Theorem 11 (linear-query paired-root construction).** Suppose the directed influence graph of an arbitrary binary edge coloring \(f\) of \(Q_d\) is supplied with its strongly connected components in topological order, each of size at most three. Then one paired root and full witnesses of both monotone orientations can be constructed using \(O(d)\) edge-color queries and \(O(d^2)\) elementary bit/list operations. The query estimate is conditional on being given the component decomposition; verifying the influence graph from an unrestricted black-box coloring may itself require exponentially many queries.

*Proof.* Start with the empty dimension prefix, its empty root, and the two empty witness paths. Process the components \(C_\nu\) in topological order. At each step, recover the zero-to-one seam vertex \(y_0\) of the current first witness and the one-to-zero seam vertex \(y_1\) of the second. Read the edge colors in the two induced colorings \(g_{y_0}^{(\nu)}\) and \(g_{y_1}^{(\nu)}\) of \(Q_{|C_\nu|}\).

For a component of size \(s\le3\), each induced \(s\)-cube has \(s2^{s-1}\le12\) edges, so both together require at most 24 color queries. Enumerate the at most \(2^s\le8\) possible new-block roots and the at most \(s!\le6\) direction orders. Test which roots support a \(0^*1^*\) path in the first induced coloring and a \(1^*0^*\) path in the second. The cross-intersection bounds \(\kappa_1=2,\kappa_2=2,\kappa_3=4\) guarantee a common root. Insert its two chosen block paths at the old seam vertices, preserving both monotone words and using each direction once by Theorem 1.

There are at most \(d\) components and each adds at most three dimensions, so at most \(24d\) color queries suffice, aside from the constant-size bookkeeping of the existing paths. Maintaining the two ordered lists of traversed directions and their seam positions costs \(O(d^2)\) elementary operations over all stages, with bit-vector representations of cube states. The final root and two full paths are explicit. QED.

**Corollary 12 (constructive monochromatic NORI1 path).** In an antipodally odd coloring of \(Q_{d+1}\) whose lower-facet directed influence components are all of size at most three, one can construct a monochromatic dimension-simple antipodal geodesic using the preceding paired-root algorithm and one additional vertical bridge-color query, again conditional on the supplied influence-component decomposition. The free-bridge path reconstruction is given in the star algorithm Subsection.

**Further computational extension.** Under the finite four-cube certificate \(\kappa_4=2\), the same procedure handles components of size four, still with a constant number of queries per component (at most 64 queries for two four-cube induced colorings). The analytical size-three algorithm requires no such certificate.

## Functional-dependency colorings: full root classification and Hall cross-root theorem

Call a cube-edge coloring f **functional** if each direction-i color depends on at most one other direction bit:
\[
f_i(x)=a_i+\lambda_i x_{p(i)},\qquad a_i,\lambda_i\in\mathbb F_2,
\]
where lambda_i=0 is a constant direction color, and p(i) differs from i whenever lambda_i=1. Direct an active dependency arrow p(i)->i. Its connected components are rooted outward trees or outward trees attached to a directed cycle; distinct dependency cycles have disjoint direction sets.

For any root x and any active i, put \(b_i=a_i+x_{p(i)}\). Write A0(f) and A1(f) for the starting roots of full dimension-simple geodesics whose edge-color words are respectively 0*1* and 1*0*.

**Theorem 1 (complete favorable-root classification).** For every functional coloring,
\[
\boxed{x\in A_0(f)\iff
\text{each directed dependency cycle }C\text{ has some }i\in C\text{ with }b_i=0.}
\tag{1}
\]
\[
\boxed{x\in A_1(f)\iff
\text{each directed dependency cycle }C\text{ has some }i\in C\text{ with }b_i=1.}
\tag{2}
\]
In particular, if \(\mathcal C(f)\) is its family of feedback cycles,
\[
\boxed{|A_0(f)|=|A_1(f)|
=2^n\prod_{C\in\mathcal C(f)}(1-2^{-|C|}).}
\tag{3}
\]

*Proof.* The color traversed in direction i is \(b_i+[p(i)\text{ before }i]\) modulo two. If every b_i=1 on a feedback cycle, the first cycle direction traversed has color one, while its last has color zero. This descent rules out a 0*1* full geodesic. Conversely, for a feedback cycle whose b-values contain both bits, orient each dependency comparison so that its traversed direction has color zero. The orientation is acyclic because the b-values are not constant, and gives an all-zero full cycle traversal. If every b_i=0 on a feedback cycle, traverse its directions in reverse dependency order, producing \(0^{|C|-1}1\).

For every direction i in a tree growing outward from such a cycle, or from a constant-colored tree root, orient its parent comparison so that direction i takes the **same color as its parent**:
\[
[p(i)\text{ before }i]=a_i+x_{p(i)}+c_{p(i)}.
\]
The tree edges introduce no directed cycles or color-descending comparisons. All comparison orientations therefore form an acyclic digraph, with no arrow from a color-one direction to a color-zero direction. Topologically sort all color-zero directions before all color-one directions to obtain the desired full geodesic. Color complementation proves (2).

A feedback cycle C forbids just one assignment to the starting bits whose indices lie in C, because the predecessor map permutes that set. These cycle sets are disjoint within one coloring. Multiplying the allowed assignments gives (3). QED.

**Theorem 2 (Hall's marriage theorem for two unrelated functional colorings).** For any two functional colorings f,g on the same Q_n,
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{4}
\]
If the two dependency digraphs contain respectively r and s directed feedback cycles, then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-r-s}.}
\tag{5}
\]
Their controlling predecessor maps and underlying interaction graphs can differ arbitrarily; the union interaction graph need not be a path, forest, or cycle.

*Proof.* By (1), each directed feedback cycle C of f forbids a single assignment to all root bits indexed by its directions; by (2), each directed feedback cycle D of g forbids one such assignment on D. All cycles within f are pairwise disjoint, and likewise all cycles within g. Each forbidden-cycle condition involves at least two starting-bit indices, since self-influence is impossible; each starting-bit index participates in at most two conditions, at most one from each coloring.

Construct a bipartite incidence graph from the forbidden-cycle conditions to their participating starting-bit indices. For any subset S of the conditions, the number of incidences is at least 2|S| and at most 2|N(S)|, hence \(|N(S)|\ge|S|\). Hall's marriage theorem gives an injection assigning each forbidden-cycle condition its **own different starting-bit index**. Set that bit to disagree with the corner value forbidden by the assigned condition. All other bits may be chosen freely. Every forbidden corner is thereby avoided, so the root satisfies both (1) and (2). There are \(n-r-s\) unmatched bits, whose assignments are arbitrary; this gives at least \(2^{n-r-s}\) common roots. The constructive orientations of Theorem 1 recover both monotone full dimension orders. QED.

**Theorem 3 (t-coloring extension).** Let \(f^{(1)},\ldots,f^{(t)}\) be functional colorings, and prescribe independently one orientation A0 or A1 for each. If every directed feedback cycle of every coloring has length at least t, then
\[
\boxed{\bigcap_{h=1}^t A_{\epsilon_h}(f^{(h)})\ne\varnothing.}
\tag{6}
\]
Indeed each forbidden-cycle condition involves at least t starting-bit indices, while each such bit appears in at most t conditions. Hall's incidence criterion therefore applies again. If R is the total number of feedback cycles across the t colorings, the construction supplies at least \(2^{n-R}\) common roots.

**Closure implications.** The theorem covers projection/constant cyclic-local pairs even when the union of their interaction graphs forms a full cycle or multiple nontrivial components. It bypasses favorable-root density, parity-cycle repair, and finite-state path enumeration. A counterexample to unrestricted cyclic cross-favorability must contain a local direction rule that depends on **both** neighboring bits in at least one of the two colorings; two independent one-predecessor rules are insufficient. Theorem 3 gives a simultaneous multicoloring extension when feedback cycles are long.

**Audit.** An independent full-order enumeration compared (1),(2) with all starting roots for 250 random functional-dependency colorings per dimension n=2,3,4,5, with no disagreements. The argument itself is all-dimensional.

## Sharp two-root strengthening of the functional Hall theorem

**Corollary (two distinct common favorable roots).** Under the hypotheses of the preceding Hall theorem, for any two functional cube-edge colorings f,g on Q_n, n>=2,
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2.}
\tag{7}
\]
This is sharp, already for n=2.

*Proof.* By Theorem 2, at least one root x avoids every forbidden feedback-cycle corner. Let m be the total number of forbidden-cycle conditions from the two colorings. Since each condition has at least two participating root bits and every bit occurs in at most two conditions, m<=n.

A root bit j is **pivotal** at x if flipping it destroys one of the satisfied cycle conditions. This happens only when some cycle condition is satisfied by a **single** mismatching root bit, namely j. Each such cycle condition can make at most one bit pivotal. Thus there are at most m pivotal bits.

If m<n, some bit is not pivotal, so flipping it gives a second root satisfying all conditions.

If m=n, the incidence inequalities are tight: every cycle condition has length two, and every root bit belongs to two cycle conditions. Again, if some bit is not pivotal, flip it. Otherwise all n bits are pivotal and all n cycle conditions must each be satisfied by **precisely one** mismatching bit. Complement the whole root x. On each two-bit condition, the originally mismatching bit becomes matching and the originally matching bit becomes mismatching. Each condition still has one mismatch, so the antipodal root is also favorable in f and g. Since n>=2, it differs from x. This proves the bound.

For sharpness take n=2 with both f and g having reciprocal dependencies \(f_0=g_0=x_1,\ f_1=g_1=x_0\). The f-nondecreasing favorable roots exclude only 11; the g-nonincreasing roots exclude only 00; the intersection consists of 01 and 10. QED.

The argument is a combinatorial strengthening of Hall's matching certificate, not a density estimate. In the critical equality case, the antipodal map supplies a second solution automatically.

## Sharp obstruction to three-way cross-favorability with short feedback cycles

The t-coloring Hall extension above requires each feedback cycle to have length at least t. This cycle-size condition matters: even three **functional** colorings of Q4 need not possess a common favorable root, although every pair does.

**Proposition (a four-direction, three-coloring obstruction).** Let the four directions be 0,1,2,3. Define three functional colorings F,G,H by their controlling-predecessor maps:
\[
\begin{array}{l}
F_0=1+x_1,\ F_1=1+x_0,\ F_2=1+x_3,\ F_3=1+x_2;\\
G_0=1+x_2,\ G_2=1+x_0,\ G_1=1+x_3,\ G_3=1+x_1;\\
H_0=x_3,\ H_3=x_0,\ H_1=x_2,\ H_2=x_1.
\end{array}
\]
Then
\[
\boxed{A_0(F)\cap A_0(G)\cap A_0(H)=\varnothing.}
\tag{8}
\]
Nevertheless every two of these three favorable-root sets intersect, by the preceding universal two-coloring Hall theorem.

*Proof.* Each coloring consists of two reciprocal directed dependency pairs. Theorem 1 shows that F forbids the root-bit corner 00 on pairs {0,1},{2,3}, and G forbids 00 on {0,2},{1,3}. Thus the indices with starting bit zero cannot include both an index of A={0,3} and an index of B={1,2}, because the four cross pairs form precisely the edges of the complete bipartite graph K_(2,2).

But H forbids the corner 11 on the two within-group pairs {0,3} and {1,2}. Hence each of A and B must contain at least one zero starting bit. That contradicts the first two constraints. Therefore no common root exists. QED.

This shows why the unrestricted pairwise cross-root theorem cannot simply be strengthened to arbitrary finite families. The t-coloring extension with feedback-cycle sizes at least t remains valid; the example has three colorings but two-direction feedback cycles and violates that sufficient hypothesis.

## Antipodal double-failure formula and hybrid cross-root thresholds

Let f be any functional-dependency cube coloring. Let its directed feedback cycles have lengths \(\ell_1,\ldots,\ell_r\ge2\). Write
\[
B_f=V(Q_n)\setminus A_0(f),\quad
S_f=B_f\cap\overline{B_f}
\]
for roots where the f-nondecreasing orientation fails and where it fails at **both antipodal roots**, respectively.

**Theorem 4 (double-failure census).** With \(p_j=2^{-\ell_j}\),
\[
\boxed{
|S_f|=2^n\left[1-2\prod_{j=1}^r(1-p_j)
+\prod_{j=1}^r(1-2p_j)\right].
}
\tag{9}
\]
In particular S_f is empty whenever f has at most one feedback cycle.

*Proof.* On a feedback cycle C_j, the initial-color vector \((a_i+x_{p(i)})_{i\in C_j}\) runs over all binary strings uniformly as the starting root varies, because the predecessor map permutes the cycle directions. Distinct cycles use disjoint starting bits, so these vectors are independent. By Theorem 1, x fails A0(f) iff at least one cycle is all one. Its antipode fails A0(f) iff at least one cycle is all zero, since complementing x complements the initial-color vector on every active cycle. For cycle j, the all-one and all-zero events each have probability p_j and are disjoint. Inclusion-exclusion across the independent cycle events yields the displayed formula. \(\square\)

**Lemma 5 (antipodal transversal criterion).** Let g be any binary cube-edge coloring with paired-root set \(P(g)=A_0(g)\cap A_1(g)\). Then
\[
\boxed{|P(g)|>|S_f|\ \Longrightarrow\
A_0(f)\cap A_1(g)\ne\varnothing.}
\tag{10}
\]
In particular if f has at most one directed feedback cycle and g has even one paired root, the cross-root intersection is nonempty.

*Proof.* Reversing a full dimension-simple geodesic from x starts at its antipode and reverses its color word. Hence \(A_1(g)=\overline{A_0(g)}\) and P(g) is closed under antipodal complementation. If the cross intersection were empty, P(g) would be contained in B_f. Antipodal closure of P(g) would then imply \(P(g)\subseteq B_f\cap\overline{B_f}=S_f\), contradicting the cardinality inequality. \(\square\)

**Corollary 6 (functional with up to four cycles versus an arbitrary star).** If f is functional with at most **four** feedback cycles and g has a star direction-interaction graph, then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\]
The star center function may be any nonlinear Boolean function, and its leaf functions may be arbitrary one-bit functions.

*Proof.* Each p_j<=1/4. The probability that among r independent variables taking states all-one, all-zero, other with probabilities p_j,p_j,1−2p_j, both extreme states occur is increasing in every p_j and in r. Thus the bracket in (9) is at most its value with four p_j=1/4:
\[
1-2(3/4)^4+(1/2)^4
=\boxed{55/128}<1/2.
\]
The established nonlinear star theorem gives \(|P(g)|\ge2^{n-1}\). Apply Lemma 5. \(\square\)

**Corollary 7 (hybrid with the computer-assisted two-hub class).** Suppose f is functional and has at most two directed feedback cycles, not both of length two. Suppose g is any coloring covered by the sharp two-hub favorable-root theorem, so that \(|P(g)|\ge2^{n-3}\). Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}
\]
With two f-cycles the double-failure fraction in (9) equals \(2p_1p_2\), strictly less than 1/8 unless both lengths are two; with fewer than two cycles it is zero. Apply Lemma 5.

**Scope.** These are all-dimensional hybrid cross-orientation theorems that permit f and g to have unrelated interaction graphs, and allow nonlinear color behavior in g. The census also identifies where this direct antipodal-size method can fail: for five or more short feedback cycles the fraction of doubly excluded antipodal roots can exceed one-half, so merely knowing that g has half its roots paired no longer guarantees an intersection. Additional geometric information is needed there.

## Protected bit fiber and nonlinear star opponent

**Theorem.** Let f be functional and g an arbitrary nonlinear star coloring with center direction h. Then A0(f) intersects A1(g), independent of the number of feedback cycles in f.

**Proof.** For every feedback cycle C of f choose a starting bit index in C other than h (possible because each cycle has at least two directions). Different cycles use disjoint bits. Assign these chosen bits opposite to their forbidden f-corner values. Then BOTH completions of the remaining h bit are favorable for f, by the functional cycle classification. The earlier fiberwise star theorem says that for each fixed assignment of leaf bits, at least one of the two hub-bit completions is a paired root of g. Choose that completion. It is in A0(f) and A1(g). QED.

**Generalization.** If H is any direction set containing no entire f feedback cycle, one can assign the bits outside H to make the whole H-fiber favorable for f. If a second coloring g admits some paired root on each H-fiber, then the two colorings are cross-favorable. This is the protected bit-block gluing lemma. The earlier four-cycle counting threshold is superseded for nonlinear star opponents.

**Active rooted-tree variant.** The same result holds when g is a rooted active tree with arbitrary nonlinear hub color: compress each full rooted branch into a monochromatic macro-leaf. For each fixed nonhub assignment, the fiberwise star theorem supplies a paired hub-bit completion in the compressed star; expand both favorable macro-geodesics into full monochromatic tree-block traversals. Thus g has a paired root in every hub-bit fiber, and the protected bit lemma applies.

## Constructive Hall root extractor and independent full-geodesic audit

The Hall-based functional cross-favorability theorem admits an algorithm constructing the common root and both full dimension-simple geodesics. Find each directed feedback cycle of f and g by following the unique predecessor pointer from each dimension. For each f-cycle create its forbidden root-bit assignment with b_i=1 for all i; for each g-cycle use b_i=0 for all i. Build the cycle-to-root-bit incidence graph and use a bipartite matching to choose one distinct starting bit per forbidden cycle. Set the chosen bit opposite to the corner assignment forbidden by its matched cycle, leaving other bits free.

At the resulting root, orient every feedback cycle of f for a 0*1* path, and every feedback cycle of g for a 1*0* path. To orient a feedback cycle for 0*1*, if its initial colors b_i are mixed, make all traversed cycle colors zero by orienting each predecessor relation according to b_i; the mixed bits exclude a consistently cyclic order. If all initial colors are zero, traverse the directed feedback cycle in the reverse cyclic order, producing 0^(length-1)1. Every outward tree edge is then oriented so that the child direction traverses in its parent direction's color. The resulting comparison graph is acyclic and has no color-one to color-zero arrow. Topologically order all color-zero directions before color-one directions. For g reverse the target colors (equivalently complement its entire edge-coloring) and apply the same construction.

**Independent validator.** The source file nori_functional_hall_validator.py implements this procedure separately from the mathematical argument, and recomputes the full cube-edge color at each traversed step of each returned dimension order. It passed 100 independent random functional f/g pairs at each n=2,3,5,10,30,100 (600 tests), with no failures. Each test includes arbitrary active predecessor maps, constants, short or long feedback cycles, and outward branching. A separate root-by-root full-permutation enumeration through n=5 verified the favorable-root classification before the Hall extractor was implemented. The existence proof is combinatorial; finite checks are corroborative.

## Necessary local obstructions to cyclic cross-root closure

For cyclic-neighbor local colorings f,g, failure of A0(f) intersect A1(g) requires ALL of the following: (i) the union direction-interaction graph contains the entire cycle, because removing any common interaction edge reduces to the proved path theorem; (ii) no direction is constant in both f and g, because the cyclic constant-site corollary permits deletion and extreme reinsertion; (iii) at least one direction j has empty local success set D_j={neighbor inputs with f_j=0 and g_j=1}, because the all-dimensional nonempty-overlap theorem settles every pair without such a site; and (iv) at least one local direction rule in f or g depends on BOTH neighboring bits, because the new functional Hall theorem settles any pair of projection/constant local colorings, with at least two common roots. These necessary conditions are not sufficient for failure. They isolate overlapping two-parent feedback near locally deficient directions as the remaining proof target. The protected bit-selector theorem also works with the two colors swapped, solving any functional-versus-fiberwise-paired nonlinear star or active rooted feedback tree pair in either monotonicity orientation.

## One nonlinear hub versus arbitrary functional coloring

**Theorem.** Let f,g be edge colorings of Q_n. Every direction of g depends on at most one other direction bit, and every direction of f except h also depends on at most one other bit. The color of direction h in f may be an arbitrary Boolean function of all other bits. Then A0(f) intersects A1(g).

**Protected Hall lemma.** List the directed feedback cycles among the functional directions of f, excluding h, and all feedback cycles of g. Every f-cycle uses at least two direction bits distinct from h. Every g-cycle uses at least two bits; at most one g-cycle contains h, and even that cycle has another bit. For any set of m cycle conditions there are at least 2m-1 incidences with bits different from h, while each available bit participates in at most two conditions. Hence the set has at least m different neighbors. Hall's theorem assigns every cycle a different bit other than h. Fix each assigned bit opposite to the corner forbidden by its cycle, leaving the remaining bits free. All f-cycle conditions and g-cycle conditions are satisfied regardless of the h-bit.

**Proof.** Let B contain h and every direction reachable from h by the active functional dependency arrows of f, and A all other directions. An A-direction color cannot depend on a B-bit, else that direction would be reachable from h. Thus f on A is functional and independent of B; its directed feedback cycles are among those already satisfied by Hall. The root on A therefore supports a full nondecreasing geodesic, by the functional cycle classification. Choose its zero-to-one seam vertex y.

On the B-fiber over y, the directions below h form active outward rooted dependency trees, and the h-edge color is an unrestricted Boolean function of the other B-bits. The established fiberwise rooted-tree paired-selector theorem says that for the already prescribed starting bits B other than h, some h-bit gives a paired root of the fiber. Insert its nondecreasing full geodesic at the seam y of the A-geodesic. This gives an f-nondecreasing full geodesic from the chosen complete root. Hall also satisfied each forbidden all-zero cycle of functional g using a bit other than h. Consequently this same complete root admits a g-nonincreasing full geodesic by the functional cycle classification. QED.

**Corollary (cyclic single two-neighbor exception).** For two cyclic-local colorings f,g, if all g direction rules are constant or one-neighbor projections and at most one f direction depends on both cyclic neighbors, then A0(f) intersects A1(g). The statement with the roles and color orientations exchanged also holds. This is an all-dimensional induction step allowing unlimited nonlinear incoming dependencies into one f-direction; the first unresolved extension permits two independently nonfunctional direction rules.

## Density and feedback-cycle threshold for a pair of exceptional nonlinear hubs

For a coloring f with every direction except one hub h functional, let C_f consist of the directed feedback cycles on functional directions, none involving h. Define q_f as the product over these cycles C of (1−2^(−|C|)).

**Theorem.** Both favorable-root sets satisfy |A0(f)|>= (3/4) q_f 2^n and |A1(f)|>= (3/4) q_f 2^n.

*Proof.* Let B be the hub h and all functional descendants of h; let A be the remaining directions. A-direction edge colors are independent of B bits, and their induced functional coloring has favorable-root fraction q_f by the Hall cycle classification. For each favorable A-root choose a full nondecreasing A-geodesic and its zero-to-one seam vertex y. In the B-fiber above y every nonhub direction has one active predecessor on an outward tree rooted at h, while the hub color is unrestricted. The active rooted-tree nonlinear-hub theorem guarantees at least three quarters of the B-root choices are favorable. Insert those paths at y and sum over different starting roots. Color complementation proves the A1 estimate. QED.

**Corollary (two nonlinear hubs in two colorings).** If f and g separately satisfy this single-exception hypothesis, with products q_f,q_g, then |A0(f) intersect A1(g)| >= 2^n max(0,(3/4)(q_f+q_g)−1). In particular, if each coloring has at most ONE other functional feedback cycle, both products are at least 3/4, giving at least 2^(n−3) common roots. If f has no other feedback cycle and g has at most THREE, the same argument gives at least (17/256)2^n common roots. All these are dimension-uniform closure classes allowing unrelated exceptional hubs with arbitrary nonlinear color functions.

A counterexample within the two-exception class must therefore contain a more substantial collection of independent functional feedback cycles; one per coloring is insufficient. These are structural induction thresholds, not the unrestricted two-exception result.

## Two exceptional hubs: Hall deficiency at most one and checkerboard selector obstruction

Consider two colorings f,g each functional except for one unrestricted hub direction. Write h for f's hub and k for g's hub, and suppose h and k are different. Let C_f,C_g be all directed functional feedback cycles not containing their respective hubs. Their cycle sets are disjoint within each coloring and have size at least two.

**Lemma (two-hub protected Hall deficiency).** After deleting h and k from the available starting-bit indices, the cycle-to-bit incidence graph has maximum Hall deficiency at most one. Equivalently, there is a matching assigning distinct available bits to all but at most one of the feedback-cycle conditions.

*Proof.* For any m selected feedback cycles, at most one f-cycle contains k and at most one g-cycle contains h. No f-cycle contains h, and no g-cycle contains k. Consequently there are at least 2m−2 incidences with the bits outside {h,k}. Any available bit belongs to at most one f-cycle and one g-cycle, hence has incidence degree at most two. Therefore the m selected cycles touch at least m−1 available bits. This holds for every selected family; the deficiency form of Hall's theorem gives a matching missing at most one condition. QED.

**Lemma (only the checkerboard can defeat two selectors).** Let F,G be subsets of the four pairs (s,t) in {0,1}². Assume for every t there is an s with (s,t) in F, and for every s there is a t with (s,t) in G. If F and G are disjoint, they must each contain just two points and form complementary diagonals: either F={(0,0),(1,1)}, G={(0,1),(1,0)}, or vice versa.

*Proof.* Both sets have at least two points. If either has three points, its complement has at most one point and cannot support the other set's two independent row or column requirements. Thus both have two points and partition the square. To meet both columns F must choose one in each column. If its points share one row, its complement misses that row and cannot meet both rows for G. The only remaining possibilities are the two diagonals. QED.

**Conditional two-hub closure criterion.** Suppose the cycle-condition incidence graph has a complete matching outside {h,k}. Break every forbidden cycle corner by the selected nonhub bit and assign all other nonhub bits freely. For every fixed assignment obtained this way, the established rooted-tree hub-selector theorem implies: the favorable f-roots in the four-point (h,k) square meet both k-columns, while favorable g-roots of the opposite monotonicity meet both h-rows. Consequently, if the full cross-root intersection is empty, BOTH of these favorable-root restrictions must form complementary checkerboards. In particular, ruling out checkerboard patterns for one-exception favorable-root sets would prove the cross-root theorem in every two-hub instance with a complete protected Hall matching. The Hall-deficiency lemma shows that an arbitrary two-exception instance differs from this favorable matching situation by **at most one unresolved functional feedback-cycle condition**.

**Unproved local structural conjecture.** For a coloring with only one direction permitted a multi-bit Boolean color function and every other direction functional, its favorable-root set A0 contains no 2-dimensional square on the exceptional hub direction and any other direction in which just the two opposite corners are favorable. Color complementation gives the analogous claim for A1. Exhaustive direct geodesic reachability verified the exclusion for all 131072 Q4 colorings with hub fixed at direction zero, and all their 2-dimensional hub faces. Additional independent random checks of 30000 Q5 and 3000 Q6 colorings found no violation. This remains a conjecture in arbitrary dimension. Proving it would remove the checkerboard obstruction above; the single remaining functional-cycle condition would still need a separate repair lemma.

This identifies a two-part closure target: one missing Hall clause, and one sharply prescribed four-root checkerboard. Neither is a global geodesic counting problem.

## Acyclic-facet monochromatic confluence and strict-majority root theorem

Let f color undirected edges of Q_n. Fix a direction h and assume **both** induced facet colorings f^0 and f^1, obtained by fixing the h-bit to 0 or 1 and retaining all other directions T, have acyclic directed dependency graphs. The two facet graphs may use different topological orders; their union need not be acyclic. The color b(y) of the h-edge is an arbitrary Boolean function of the T-bits y.

**Lemma (acyclic monochromatic confluence).** In any binary edge coloring q with acyclic directed dependencies, for any starting roots u,v there are dimension-simple partial paths from u and v meeting at a common vertex w, one all color zero and the other all color one.

*Proof.* Process the direction bits in a topological order of their dependency digraph. At each direction i the two evolving vertices already agree in every earlier bit. If their ith bits differ, their two ith-direction incident edges have the same color, because the edge rule depends only on already matched predecessor bits. If that color is zero, flip i on the u-side; otherwise flip i on the v-side. The ith bits become equal. Continue. Each direction is used on at most one side, and the endpoints coincide after all directions. QED.

Write R0^q(u) and R1^q(v) for endpoints of such partial monochromatic paths, including empty paths.

**Lemma (constraints from an unfavorable full root).** If a full root (s,y) of f has no 0*1* dimension-simple antipodal geodesic, then
\[
\boxed{b(z)=1\text{ for every }z\in R0^{f^s}(y),\quad
b(z)=0\text{ for every }z\in R1^{f^{1-s}}(\bar y).}
\]
*Proof.* For z reached from y by an all-zero partial f^s path using directions U, if b(z)=0, cross h in color zero and then traverse the remaining directions T\U in the opposite facet along a 0*1* full path. This is possible because the induced dependency graph on any face of an acyclic coloring remains acyclic. The resulting full word is monotone, contradiction. Thus b(z)=1.

For z reached from bar y by an all-one partial f^(1-s) path using directions V, first traverse the complementary directions T\V from y to z in the initial facet along a 0*1* path, possible by acyclic dependencies. If b(z)=1, cross h in color one and reverse the previous all-one path from z to bar y. The complete direction order is again 0*1*, contradiction. Thus b(z)=0. QED.

**Theorem (one fully favorable starting half-cube).** There is a bit s such that **every** root (s,y) is in A0(f).

*Proof.* Otherwise choose unfavorable roots (0,y) and (1,y'). The preceding constraints force b=1 on R0^{f^0}(y) and b=0 on R1^{f^0}(bar y'). But the first lemma supplies a point in their intersection, impossible. Hence all unfavorable roots lie on at most one side of the h-bit partition. QED.

**Theorem (strict majority, sharp paired-root count).**
\[
\boxed{|A0(f)|\ge2^{n-1}+1,\qquad |P(f)|\ge2.}
\]
If b(y)=0 at any T-vertex y, both (0,y) and (1,y) are favorable: traverse h first in color zero, then use an acyclic-facet monotone path on all T-directions. At least one of those two roots lies outside the guaranteed favorable half-cube, giving the strict-majority bound. If b is identically one, every root is favorable by traversing an acyclic-facet monotone T-path first and h last in color one. Reversing antipodal full paths gives A1(f)=antipodal(A0(f)), so P=A0 intersect A1 has size at least twice |A0| minus 2^n, hence at least two. These bounds are sharp for Q2 reciprocal coloring f0=x1,f1=x0. QED.

**Cross-coloring theorem.** Let f,g be any two binary cube-edge colorings, each having some (possibly different) direction whose two opposite facets have acyclic directed dependencies. Then
\[
\boxed{|A0(f)\cap A1(g)|\ge2.}
\]
Indeed the theorem gives both favorable-root sets cardinality at least 2^(n-1)+1, so inclusion-exclusion proves the claim. If their distinguished directions differ, the two fully favorable half-cubes already meet in a codimension-two cube of size 2^(n-2).

**NORI1 closure.** A directed dependency graph with feedback vertex set of size at most one automatically meets the facet hypothesis. The hypothesis is broader, permitting different acyclic dependency orders in the two opposite facets even when the union digraph has cycles. Every such coloring has paired roots; by the established free-bridge correspondence the associated next-dimensional antipodally odd NORI1 instance has a monochromatic full antipodal geodesic without restrictions on the bridge-edge colors.

**Research path.** The greedy confluence lemma is a new dimension-uniform structural invariant and works for arbitrary acyclic Boolean dependency rules, not only functional directions. To extend beyond one hub, a candidate is two-dimensional confluence of four initial roots after deleting a two-bit feedback set. The present proof does not assert such a stronger property. Randomized independent full-path checks with differing facet topological orders passed 500 Q4, 250 Q5, and 80 Q6 instances.

## Universal gluing of an acyclic-facet coloring to any paired-root coloring

**Theorem (half-cube versus antipodal-pair intersection).** Let f be any binary cube-edge coloring satisfying the two-facet acyclicity hypothesis of the preceding confluence theorem in some direction h. Let g be ANY other binary cube-edge coloring with at least one antipodally paired root P(g)=A0(g) intersect A1(g). Then

A0(f) intersect P(g) is nonempty, and therefore A0(f) intersect A1(g) is nonempty.

More quantitatively |A0(f) intersect A1(g)| is at least |P(g)|/2. The orientation-swapped assertion also holds: A1(f) intersects P(g).

*Proof.* By the full-slice confluence theorem, A0(f) contains every root whose bit h equals some s. By reversing full dimension-simple geodesics, P(g) is invariant under antipodal complementation, so its roots occur in antipodal pairs. Each such pair contains one root with h-bit s, lying in A0(f). These |P(g)|/2 different roots also lie in A1(g). For the swapped orientation, apply the same reasoning to the coloring obtained from f by interchanging colors zero and one. QED.

**Corollary (unicyclic nonlinear pendant-tree closure).** Let F have a unicyclic undirected direction-interaction graph with arbitrary nonlinear rooted pendant trees. Let g0,g1 be its two induced core colorings in the established pendant-tree interface reduction. Each cyclic-local core coloring separately has paired roots by the proved nonlinear cycle paired-root theorem. Suppose EITHER g0 OR g1 has a cycle direction h such that both facets obtained by fixing its h-bit have acyclic directed dependencies on the remaining core directions. Then A0(g0) intersects A1(g1): use the full favorable half-cube of the acyclic-facet core and an antipodal pair of paired roots in the other core. The pendant-tree interface theorem lifts this common root to a paired root of F; the free-bridge correspondence supplies the associated NORI1 monochromatic antipodal geodesic. No joint constant-color site or nonempty local opposite-color overlap is required. Only ONE induced core needs the acyclic-facet property.

**Inductive significance.** A fully favorable starting half-cube is a universal transversal of every nonempty antipodally symmetric paired-root set. This converts any established one-coloring paired-root theorem into a two-coloring cross-root theorem whenever the opposite coloring has an acyclic-facet direction. It generalizes the earlier protected functional-hub gluing principle and does not require independent favorable-root density estimates.

## Sharp fiberwise paired selector and SCC gluing from acyclic opposite facets

**Theorem (paired-root selector in every hub fiber).** Under the two-facet acyclicity hypothesis of the preceding confluence theorem for distinguished direction h,
\[
\boxed{\forall y\in Q_{n-1}\ \exists s\in\{0,1\}:\ (s,y)\in P(f).}
\tag{CF7}
\]
Consequently \(|P(f)|\ge2^{n-1}\). The bound is sharp for reciprocal Q2 dependency coloring and its Cartesian products with independent monochromatic directions.

*Proof.* Let b(y) be the color of the h-edge between (0,y) and (1,y). The preceding full-slice theorem provides an h-bit value t for which every (t,z) is favorable, for all nonhub z.

For any y, if b(y)=0, both (0,y) and (1,y) are favorable: traverse h first in color zero, then use an acyclic-facet full nondecreasing path. The antipode of one of these two roots lies in the fully favorable t-slice; hence one of them is paired.

If b(y)=1 and b(bar y)=1, both hub completions of y are likewise favorable: traverse all nonhub directions first along an acyclic-facet full nondecreasing geodesic, then traverse h last in color one. Again one has its antipode in the fully favorable t-slice and is paired.

The remaining case is b(y)=1 and b(bar y)=0. Both hub completions of bar y are favorable by traversing h first at bar y. At least one completion (t,y) is favorable by the full-slice theorem, and its antipode is one of those two favorable roots at bar y. Thus (t,y) is paired.

All cases give a paired root over the prescribed y. Distinct y give distinct roots, yielding the count. QED.

**Theorem (one-feedback-vertex SCC closure).** Let f be an arbitrary binary cube-edge coloring, with directed dependency graph D(f). Suppose that in EVERY strongly connected component B of D(f), one can delete at most one direction vertex h_B so that the induced dependency digraph on B\{h_B} is acyclic. (Singleton components qualify.) Then
\[
\boxed{P(f)\ne\varnothing,\quad
|P(f)|\ge2^{\,\#\operatorname{SCC}(D(f))}.}
\tag{CF8}
\]

*Proof.* Select a terminal strongly connected component B in the condensation DAG and write A for the remaining directions. No B-bit influences any A-direction edge color, so A-direction colors are independent of B. For each fixed outside assignment x, the induced B-fiber coloring has the same internal dependency graph or a subgraph thereof; by assumption its two facets after fixing h_B have acyclic dependencies. The strict-majority theorem above gives at least \(2^{|B|-1}+1\) favorable roots in each such fiber, for |B|>=2. Hence for any two outside assignments x,y, inclusion-exclusion gives
\[
|A_0(g_x)\cap\overline{A_0(g_y)}|
\ge 2(2^{|B|-1}+1)-2^{|B|}=2.
\]
For a singleton B both possible roots are favorable and the same overlap bound two holds. The established paired-root seam-gluing theorem therefore removes B while multiplying the lower bound for the number of paired roots by at least two. Apply induction to the remaining SCCs of the condensation DAG, starting from one paired root of the empty cube. This yields at least two roots per SCC and proves (CF8). QED.

**Structural obstruction corollary.** Any paired-root counterexample must contain a terminal strongly connected dependency component whose directed feedback vertex set has size **at least two**: deleting any single direction from that component still leaves a directed feedback cycle. This excludes feedback cores with arbitrarily many branching vertices when all directed cycles pass through one hub. The result is independent of any upper bound on internal indegrees or nonlinear Boolean complexity.

The theorem strengthens the earlier active rooted-tree feedback, fan-cycle, nonlinear star, and one-exception results, while complementing the separate computer-assisted two-hub theorem for SCCs with at most two branching-indegree vertices. It does not settle SCCs that require at least two directions to hit all internal feedback cycles.

### Correction to the SCC obstruction statement

The preceding SCC theorem proves that any counterexample must contain **some** strongly connected dependency component whose internal feedback vertex set requires at least two directions. It does NOT prove that every counterexample has such a component among the terminal SCCs: a nonterminal hard SCC can feed a removable terminal SCC.

The stronger terminal assertion is valid only for a **least-dimensional** counterexample. Indeed, if a terminal SCC B of a least-dimensional counterexample admitted an internal feedback vertex set of size at most one, the paired-root seam-gluing equivalence would imply that deleting B leaves a smaller paired-root counterexample, contradicting minimality. Thus every terminal SCC in a least-dimensional counterexample requires deletion of at least two internal direction vertices to destroy all directed feedback cycles. This qualification supersedes the unqualified terminal-SCC sentence in the prior theorem while leaving its proof and quantitative paired-root bound unchanged.

## Mixed-facet confluence: one confluent facet and one hereditarily favorable facet

For a binary cube-edge coloring q of Q_m, define \(R^q_0(u)\) as endpoints of dimension-simple partial paths starting at u using only edges of color zero, and \(R^q_1(v)\) analogously for color one; empty paths are permitted.

Call q **monochromatically confluent** if
\[
\boxed{R^q_0(u)\cap R^q_1(v)\ne\varnothing\quad\text{for all }u,v\in Q_m.}
\tag{MC1}
\]
Call q **hereditarily favorable** if every root of every nonempty subface of q admits a full dimension-simple \(0^*1^*\) geodesic in that subface. An acyclic dependency coloring has both properties by the published greedy confluence lemma and sink-direction seam insertion; hereditary favorability is a weaker hypothesis than acyclic dependencies.

**Theorem (mixed-facet selector).** Let F color the edges of Q_(m+1), with distinguished hub bit h. Write q^0,q^1 for its two opposite m-dimensional facet colorings and b(y) for its arbitrary h-edge color at nonhub vertex y. Suppose q^0 is monochromatically confluent and q^1 is hereditarily favorable. No dependency relationship between q^0 and q^1 is required. Then
\[
\boxed{\exists s\in\{0,1\}:\{(s,y):y\in Q_m\}\subseteq A_0(F),}
\tag{MC2}
\]
\[
\boxed{|A_0(F)|\ge2^m+1,\qquad
\forall y\in Q_m\ \exists s:(s,y)\in P(F).}
\tag{MC3}
\]
Consequently \(|P(F)|\ge2^m\), sharply.

*Proof.* Confluence of q^0 implies every root u of q^0 admits a full \(0^*1^*\) geodesic: apply (MC1) to \(u,\bar u\), join the all-zero path from u to a meeting point with the reverse all-one path from \(\bar u\), which use complementary direction sets. Hereditary favorability of q^1 supplies full monotone paths from every root in all its faces.

Suppose (0,y) is unfavorable in F. For each \(z\in R^{q^0}_0(y)\), if b(z)=0, traverse the zero path from y to z, cross h in color zero, then traverse all remaining dimensions in the q^1 subface starting at z along a full monotone path. This contradicts unfavorability. Thus
\[
b=1\text{ throughout }R^{q^0}_0(y).
\tag{MC4}
\]

Suppose (1,y') is unfavorable. For every \(z\in R^{q^0}_1(\bar y')\), let V be the directions of a monochromatic-one q^0 path from \(\bar y'\) to z. Starting at y', traverse the complementary directions T\V inside the appropriate q^1 subface along a full monotone geodesic, ending at z. If b(z)=1, cross h in color one and then reverse the q^0 one-path from z to \(\bar y'\). This is a complete monotone geodesic from (1,y'), a contradiction. Therefore
\[
b=0\text{ throughout }R^{q^0}_1(\bar y').
\tag{MC5}
\]

Confluence (MC1) supplies a meeting point of the two reachable sets in (MC4),(MC5), forcing b to be both one and zero. Thus unfavorable roots cannot occur in both hub-bit slices. This proves (MC2).

If b(y)=0 for some y, both hub-bit completions of y are favorable by crossing h first in color zero and following a monotone full path in the opposite facet. If b is identically one, all roots are favorable by following a monotone full path in the initial facet and crossing h last in color one. Hence (MC2) always extends to at least \(2^m+1\) favorable roots.

For each nonhub y, if b(y)=0, both completions at y are favorable, so one has its antipode in the fully favorable hub slice (MC2) and is paired. If b(y)=1=b(\bar y), both completions at y are favorable by traversing the initial facet first and crossing h last at \(\bar y\); again one is paired. Otherwise b(y)=1 and b(\bar y)=0. Both completions at \(\bar y\) are favorable by crossing h first, and (MC2) supplies at least one favorable completion at y whose antipode is among them. Therefore one completion at y is paired in every case. Distinct nonhub assignments y give distinct paired roots, establishing (MC3). \(\square\)

**New feedback-two application.** On three directions 0,1,2 define
\[
q_0(x)=x_1x_2,\qquad q_1(x)=x_0(1-x_2),\qquad q_2(x)=0.
\tag{MC6}
\]
Its global dependency digraph contains both 0->1 and 1->0. Nevertheless q is hereditarily favorable: each proper subface has an acyclic dependency digraph (the two reciprocal arrows cannot be simultaneously active after fixing x_2), and every full root even admits an all-zero geodesic. From x_2=1, traverse direction 2 first in color zero; with x_2=0, if x_0=1 traverse 0 then 1, otherwise traverse 1 then 0; all traversed edges have color zero. Finish with direction 2 when starting x_2=0.

Construct a Q4 coloring F with hub h=3: the h=0 facet is identically zero in directions 0,1,2; the h=1 facet is q of (MC6); and the h-direction color is \(b(x)=x_0+x_1\) modulo two. The full dependency digraph has directed cycles after deletion of **any single** direction, but deletion of {0,1} leaves an acyclic digraph; hence its directed feedback vertex set has size two. Nevertheless the mixed-facet theorem gives \(|P(F)|\ge8\). The result thus goes beyond the previously proved one-feedback-vertex theorem, allowing a nonlinear two-feedback core on one side of the hub.

**Structural scope.** The mixed-facet theorem isolates the real ingredients of the acyclic-facet proof: monochromatic confluence is needed on only one facet, while the other facet needs monotone geodesics in every restricted face. Confluence is not generally preserved when adding a hub, so this is a sufficient induction rule rather than a universal closure of NORI1.

## Hereditary favorability under constant-control grafting, with arbitrarily dense global feedback

Call a cube-edge coloring **hereditarily favorable** if every root in every subface admits a full \(0^*1^*\) geodesic within that face (including zero-dimensional faces).

**Theorem (constant-control grafting).** Let q^0,q^1 be any two hereditarily favorable colorings of Q_m, possibly with entirely unrelated dependency digraphs. Construct a coloring q on Q_(m+1) whose restrictions to the two facets of a new direction z are respectively q^0,q^1, and whose z-direction edges all have the same constant color c in {0,1}. Then q is hereditarily favorable.

*Proof.* Take an arbitrary subface S of Q_(m+1) and a starting root in it. If z is fixed throughout S, the induced coloring belongs to a subface of q^0 or q^1 and is favorable by hypothesis. If z is free, consider its two facet subfaces S^0,S^1; their colorings are hereditarily favorable. When c=0, traverse z first in color zero, entering the opposite z-facet, and then take a full \(0^*1^*\) geodesic there. When c=1, first traverse all other free directions along a \(0^*1^*\) path in the initial z-facet, then traverse z last in color one. Both constructions use every free direction once and yield the desired monotone word. Since S and its starting root were arbitrary, hereditary favorability follows. \(\square\)

**Corollary (hierarchical conditional-facet closure).** Begin with any collection of hereditarily favorable base colorings, including every coloring with an acyclic dependency graph. Repeatedly adjoin a new constant-color control direction, choosing *independently* arbitrary previously constructed colorings on its two opposite facets. Every coloring produced in this recursive class remains hereditarily favorable. Finally adjoin one more hub direction h with **arbitrary** edge-color Boolean function of all other bits, placing an acyclic monochromatically confluent coloring on its h=0 facet and any recursively produced hereditary coloring on its h=1 facet. By the mixed-facet confluence theorem, the resulting cube has
\[
\boxed{|A_0|\ge2^{n-1}+1,\qquad
|P|\ge2^{n-1}}
\]
and has a paired root over every assignment of its nonhub starting bits.

**Example (unbounded feedback vertex number).** Fix m>=2 ordinary directions 1,...,m and a control direction z. Let its z-edge color be constant zero, and define ordinary direction-i colors by
\[
q_i(x,z=0)=\bigoplus_{j<i}x_j,\qquad
q_i(x,z=1)=\bigoplus_{j>i}x_j.
\tag{HG1}
\]
For each fixed z, the direction-dependency graph on the ordinary directions is a DAG: the natural total order when z=0, and its reversal when z=1. Hence both facets and all their subfaces are hereditarily favorable. The constant-control theorem shows that q is hereditarily favorable.

But in the *global* dependency graph, for every distinct ordinary directions i,j, **both** arrows i->j and j->i occur: the first is active in one control facet and the reverse in the other. Thus the m ordinary directions induce a complete bidirected graph. At least m−1 direction vertices must be deleted to make the global dependency digraph acyclic, so the directed feedback vertex number grows without bound with m.

Add one final hub direction h whose h=0 facet is an arbitrary acyclic edge coloring of Q_(m+1), whose h=1 facet is q, and whose h-edge color is an **arbitrary nonlinear Boolean function** of the m+1 nonhub bits. The mixed-facet theorem gives a paired-root selector along h and at least \(2^{m+1}\) paired roots. The resulting global dependency digraph still contains the complete bidirected graph on the ordinary directions and can include additional hub feedback cycles.

**Proof-closure lesson.** The global directed dependency graph can be highly cyclic even when the coloring is built from a sequence of completely tractable conditional facets. Feedback vertex number is therefore not a sufficient measure of local proof complexity. A structurally natural induction should track monochromatic confluence and hereditary monotone-path solvability **after fixing control bits**, allowing different dependency orders in different facets. The mixed-facet theorem supplies a nonconstant final-hub operation above this hereditary class; extending this operation to multiple mutually interacting arbitrary hub layers remains open.

## Canonical seam permutations for acyclic dependency colorings

Let q color cube edges in dimension m, with an acyclic directed dependency graph. Let \(c_q(w)=(q_i(w))_{i=1}^m\) denote the vector of the m incident direction-edge colors at a cube vertex w.

**Theorem (triangular seam bijection).** The map
\[
\boxed{T_q(w)=w\oplus\mathbf1\oplus c_q(w)}
\tag{S1}
\]
is a bijection of the m-cube. For every root y, the unique solution \(w=T_q^{-1}(y)\) is the transition seam of a full dimension-simple antipodal geodesic from y with color word \(0^*1^*\). Its zero phase traverses all directions with q_i(w)=0 in a dependency-topological order; its one phase traverses all directions with q_i(w)=1 in reverse dependency-topological order. The seam w is independent of the chosen topological order.

*Proof.* Fix a topological order i_1,...,i_m of the dependency DAG. Each q_(i_j)(w) depends only on earlier listed bits and not on w_(i_j). Thus (S1) is triangular with a bijective one-bit diagonal map at each stage. Solve \(w_{i_j}=y_{i_j}\oplus1\oplus q_{i_j}(w)\) successively; every starting root y determines precisely one w.

Put Z={i:q_i(w)=0} and O={i:q_i(w)=1}. Equation (S1) says y differs from w on Z, and w differs from the antipode of y on O. Starting at y, traverse Z in topological order. Each predecessor bit of a traversed direction i already equals its value at w, whether previously changed in Z or unchanged in O. Hence every edge has color q_i(w)=0. From w traverse O in reverse topological order. Each predecessor bit of direction i remains at w when i is traversed, so every remaining edge has color q_i(w)=1. All directions are used once. \(\square\)

**Corollary (seam distribution).** The canonical monotone paths from all \(2^m\) roots have all \(2^m\) different transition seams. For any prescribed set U of seam vertices, precisely |U| starting roots have a canonical seam in U.

**Corollary (two acyclic colorings).** Let q,r be any two acyclic-dependency colorings on Q_m, allowing unrelated topological orders. Their canonical monotone paths from the *same root* can share a seam vertex w if and only if
\[
\boxed{c_q(w)=c_r(w)\quad\text{in every direction}.}
\tag{S2}
\]
Indeed the common-root condition T_q(w)=T_r(w) reduces immediately to (S2). Such alignment is not automatic, even when both colorings have every root favorable, because their incident direction-color vectors may disagree at every vertex.

**Theorem (canonical two-source gate).** For any two starts u,v, their greedy acyclic monochromatic confluence construction has one canonical meeting point w in their smallest common face. With directions processed in a dependency-topological order, the meeting bits satisfy
\[
\boxed{
w_i=u_i=v_i\quad\text{if }u_i=v_i;\qquad
w_i=u_i\oplus1\oplus q_i(w)\quad\text{if }u_i\ne v_i.
}
\tag{S3}
\]
These equations are triangular and define one w independent of the topological order. The path from u to w is all zero, the path from v to w is all one, and their disjoint direction sets partition the bit positions where u and v differ.

**Relevance to two-feedback restoration.** A cube coloring that becomes acyclic after fixing two exceptional direction bits has four canonical seam permutations T_00,T_01,T_10,T_11. The alignment criterion (S2) converts common canonical-seam questions into local equalities of direction-color vectors. Requiring all four seam maps to agree is not a valid general induction invariant, since even two acyclic facet colorings may lack any shared canonical seam. The new maps give an algebraic language for controlled exchanges of the two exceptional directions; unrestricted two-feedback closure remains open.

## Bipolar square restoration for two-feedback-direction cube colorings

Let F be a binary edge coloring of Q_(m+2), with two distinguished hub directions h,k and m other directions T. For each fixed assignment (s,t) of the hub bits, suppose the induced T-direction facet coloring has an **acyclic directed dependency graph**. The facet dependency orders may depend arbitrarily on (s,t). Hub-edge colors can depend on every ordinary bit and on the other hub bit.

Fix an ordinary starting assignment y in Q_T. The four hub edges with ordinary bits y form a colored square. Write their colors as
\[
F_h(s,t,y)=a+t,\qquad F_k(s,t,y)=b+s
\tag{BS1}
\]
for a,b in F2, if both hub directions depend nontrivially on the *other* hub bit at this y.

**Lemma (two bipolar roots of a reciprocal hub square).** Under (BS1), the two opposite hub corners
\[
\boxed{(s,t)=(1+b,a)\quad\text{and}\quad(s,t)=(b,1+a)}
\tag{BS2}
\]
each admit both a full all-zero hub-square geodesic and a full all-one hub-square geodesic, using the two different hub orders.

*Proof.* From corner (1+b,a), traverse h then k. The h-edge has color a+a=0; after flipping h, the k-edge has color b+b=0. For the opposite hub order k then h, the k-edge has color b+(1+b)=1 and the subsequent h-edge has color a+(1+a)=1. Interchanging starting corner and hub orders gives the same property for the other opposite corner. \(\square\)

**Theorem (local reciprocal-square paired-root restoration).** If (BS1) holds for even **one** ordinary assignment y, then F has a paired root. In fact both complete starting roots whose ordinary bits equal y and whose hub bits are the corners (BS2) belong to P(F). If m>=1, antipodal symmetry gives at least four distinct paired roots.

*Proof.* Choose either hub corner sigma of (BS2). For the full F-geodesic of word 0*1*, first traverse both hub directions along the all-zero hub-square path at ordinary vertex y. This reaches the opposite hub corner bar sigma, without changing any ordinary bit. Inside the fixed-bar-sigma T-facet, start at ordinary y and traverse a complete 0*1* antipodal geodesic. Such a path exists from EVERY T-root since its dependency graph is acyclic. Concatenating the two paths gives a full dimension-simple nondecreasing geodesic starting at (sigma,y).

For the opposite word 1*0* from the SAME root (sigma,y), traverse the two hub directions first along the all-one square path (in the other order), then traverse a complete 1*0* geodesic in that same opposite T-facet from ordinary y. Color complementation of the acyclic-facet theorem gives this path. The resulting full path uses every original direction once, proving (sigma,y) paired. Do the same for the other hub corner. Antipodal closure of P(F) supplies the additional roots stated. \(\square\)

**Corollary (necessary obstruction for a two-vertex feedback set).** Suppose deleting two designated directions h,k from the global directed dependency graph of F leaves an acyclic digraph. Then every fixed-hub T-facet is acyclic, so the theorem applies. If F is a paired-root counterexample, for **every** ordinary vertex y the restricted colored hub square must fail reciprocal dependence. Equivalently at each y at least one of the two restricted hub-direction color functions is constant with respect to the other hub bit. In particular the two directed hub-to-hub dependencies can never both be simultaneously active on the same ordinary square.

This excludes a broad nonlinear feedback configuration by a two-edge-order exchange, without any enumeration of high-dimensional paths. It is a sufficient paired-root restoration lemma, not a proof for all colorings with a two-vertex directed feedback set.

## Two-hub sandwich restoration and bounded square interface

Let F be an edge coloring of Q_(m+2), with two special hub directions 0,1 and m ordinary directions T. Assume each of the four T-facet colorings, obtained after fixing both hub bits, has acyclic directed dependencies. Hub edge colors can depend arbitrarily on all ordinary bits and the other hub bit.

For a fixed ordinary starting root y, denote by a the hub-square coloring at y and by b the hub-square coloring at its antipode bar y. For hub starting state sigma and a hub order (i,j), write tau=sigma+e_i. For epsilon=0 or 1, define three possible local certificates:

(Early) a_i(sigma)=epsilon and a_j(tau)=epsilon.
(Late) b_i(sigma)=1-epsilon and b_j(tau)=1-epsilon.
(Split) a_i(sigma)=epsilon and b_j(tau)=1-epsilon.

**Theorem (sandwich lifting).** If at least one of these conditions holds for some hub order (i,j), then (sigma,y) supports a full dimension-simple antipodal geodesic with word epsilon*(1-epsilon)*. If conditions hold for epsilon=0 and epsilon=1 from the same root (possibly using different orders), the root is paired.

*Proof.* In the early case traverse the two hub edges first, in color epsilon, then traverse all m ordinary directions in the opposite hub facet along a monotone full geodesic. In the late case first traverse all ordinary directions in the initial hub facet, arriving at bar y, and then both hub edges in color 1-epsilon. In the split case traverse one hub edge at y in color epsilon, then all ordinary directions in the intermediate hub facet along a monotone full geodesic from y to bar y, and then the final hub edge at bar y in color 1-epsilon. Each fixed-hub T facet admits the required complete monotone path from every starting root by the acyclic dependency theorem. Each construction traverses every original direction once and has the required monotone word. QED.

**Uniform finite classification.** A hub square coloring is encoded by a 4-bit integer a, in which bits 0 and 1 give the direction-0 color when hub bit 1 is zero and one, while bits 2 and 3 give the direction-1 color when hub bit 0 is zero and one. There are 16 choices for a and 16 for b. Direct evaluation of the three certificates across both hub orders, both target orientations, and all four starting hub corners gives:
- 196 of the 256 ordered pairs (a,b) admit a common hub corner with both polarity certificates and hence a paired root for **every** acyclic four-fiber extension.
- 60 ordered pairs do not admit a paired root through these restricted sandwich constructions. This does NOT assert that the full coloring lacks paired roots.
- If a is any of {5,6,9,10}, the two hub directions are mutually active on the square at y, and both polarity certificates hold for two opposite starting hub corners regardless of b. This is the previously proved bipolar-square restoration theorem.
- Only the ordered pairs (3,12) and (12,3) fail to provide an orientation-zero sandwich certificate at every hub root above both y and bar y.

The finite check uses the following formulas, evaluated for each a,b in {0,...,15}, sigma in {0,...,3}, epsilon in {0,1}, and order (i,j) in {(0,1),(1,0)}. Define edge(c,0,sigma)=bit_(sigma_1)(c), edge(c,1,sigma)=bit_(2+sigma_0)(c), tau=sigma XOR (1<<i), and evaluate Early, Late, Split with the above formulas. A pair passes the paired test if some sigma passes one test for epsilon zero and one for epsilon one. Reversing full geodesics gives paired(b,a) = antipodal(paired(a,b)), so the paired test is symmetric upon exchanging a and b. No SAT or unbounded search is involved: the classification has 256 inputs **after** the dimension-uniform sandwich lifting theorem.

**Proof-closure target.** The hard cases are not failures of the original cube theorem; they require paths that interleave ordinary dimensions with the hub crossings more flexibly. The two pairs (3,12),(12,3) isolate a particularly rigid special form: at ordinary y one hub direction is uniformly zero and the other uniformly one, whereas at bar y these two values reverse. A full two-feedback-direction restoration theorem must be able to move an ordinary direction through the hub crossings when this polarity changes.

## Hereditary favorability implies monochromatic confluence

**Lemma (interval confluence).** Let q be a hereditarily favorable coloring of Q_m, meaning that every starting vertex of every subface has a full \(0^*1^*\) geodesic inside that subface. Then q is monochromatically confluent: for any two vertices u,v, a partial dimension-simple all-zero path from u and a partial dimension-simple all-one path from v meet at a common vertex inside their smallest containing subface.

*Proof.* Let I be the set of directions in which u and v differ, and let C be the |I|-dimensional face obtained by fixing all other bits. Inside C, the two vertices u and v are antipodal. By hereditary favorability there is a complete nondecreasing q-geodesic in C from u to v. Split it at its zero-to-one color transition seam w. Its first part is an all-zero path u to w, and reversing its second part gives an all-one path v to w. The two paths are dimension-simple, use disjoint direction sets partitioning I, and lie entirely in C. QED.

**Corollary (two arbitrary hereditary facets).** Let F color cube edges in Q_(m+1). Suppose the two opposite m-dimensional facet colorings at a chosen direction h are BOTH hereditarily favorable, with no requirement that their dependency digraphs share any structure. The h-edge colors may be arbitrary. Then F has one entire favorable hub-bit half-cube and a paired-root selector over every assignment of the other m bits:
\[
\boxed{|A_0(F)|\ge2^m+1,\qquad |P(F)|\ge2^m.}
\]
Indeed the lemma supplies monochromatic confluence for either facet, while both supply hereditary favorability. Apply the mixed-facet restoration theorem. The class is stable under repeated constant-colored control grafts, but an arbitrary-color final hub generally yields only the paired-selector conclusion, not hereditary favorability; a repeated arbitrary-hub step needs an additional restoration principle.

**Closure relevance.** The abstract property driving one-hub restoration is interval monochromatic confluence, rather than directed graph acyclicity. The hereditary class is much larger than the DAG class: opposite conditional acyclic orders can generate complete bidirected dependency graphs of arbitrary order while remaining hereditarily favorable. The next two-feedback-direction problem concerns the weaker *paired-selector* outputs of one hub restoration, which need not themselves be hereditarily favorable.

## Seven symmetry orbits of the residual two-hub sandwich interface

In the preceding dimension-uniform two-hub sandwich restoration theorem, encode a hub-square coloring by four bits: the two direction-0 edge colors indexed by the other hub bit (positions 0,1), followed by the two direction-1 colors indexed by the first hub bit (positions 2,3). Let \(R(a,b)\) be the subset of the four starting hub corners at ordinary root y for which the three sandwich alternatives certify BOTH monotone polarities, using a at y and b at its antipode.

The preceding bounded 16-by-16 interface census found \(R(a,b)\ne\varnothing\) for 196 square pairs and \(R(a,b)=\varnothing\) for the remaining 60. The latter are **failures only of the restricted sandwich witness**, not refutations of paired-root existence.

**Theorem (seven residual orbit types).** Under the operations
(a) independently translate either hub bit in the labels of both square colorings;
(b) interchange the two hub directions in both colorings;
(c) complement all eight hub-edge color bits in both squares;
(d) interchange the two squares a and b, corresponding to reversing antipodal full witnesses;
the sixty noncertified pairs split into precisely **seven symmetry orbits**:
\[
\boxed{
\begin{array}{c|rrrrrrr}
\text{representative }(a,b)&(0,3)&(0,7)&(0,15)&(1,12)&(1,13)&(1,14)&(3,12)\\
\text{orbit size}&8&16&2&16&8&8&2
\end{array}}
\tag{SO1}
\]
The sizes sum to 60.

*Proof.* Each listed operation preserves paired-root existence under the sandwich alternatives. Bit translations merely relabel the starting hub corner and its two possible orders. Hub interchange relabels the two orders. Complementing both edge colors exchanges the two monotonicity polarities. Exchanging a and b reverses the complete full geodesics, replacing a root with its antipode and swapping the two polarities, so \(R(b,a)=\overline{R(a,b)}\). Thus the collection of failing pairs is stable under all four operations.

The orbit classification is a bounded sixteen-square computation. To reproduce it, evaluate for every pair a,b in 0,...,15 and every starting hub corner sigma and the two hub orders the three Early/Late/Split tests of the previous theorem for epsilon=0 and epsilon=1. Retain the sixty pairs for which no corner passes both tests. Generate each symmetry orbit by repeatedly applying: the four hub translations, the swap of the two two-bit square-code halves, simultaneous code complements (a,b)->(15-a,15-b), and (a,b)->(b,a). The seven representatives above generate disjoint sets of the displayed sizes, whose union has sixty members. These finite assertions follow by direct examination of at most 256 ordered square pairs, **after** the dimension-uniform mathematical lifting reduction. No unbounded cube enumeration or optimization is involved. \(\square\)

**Interpretation.** One of the seven types, represented by (3,12), is the antipodally odd opposite-hub-polarity obstruction: at y one hub direction is uniformly one and the other uniformly zero, while at bar y their colors reverse. The other six types include fully monochromatic hub squares opposite asymmetric hub squares. The classification replaces 60 local configurations by seven structural boundary patterns, but does not establish that every such pattern can be restored in the full cube.

**Next closure direction.** A full two-feedback-direction theorem could arise from a single dimension-simple exchange rule permitting an ordinary direction to be traversed before one hub crossing and another ordinary direction after it. Such a rule needs to repair the seven residual types, while the sandwich theorem already handles the other 196 interface configurations. The one-feedback confluence permutations offer a controlled way to choose those ordinary directions without laddering through successive cube dimensions.

## Antipodally matching hub squares force paired roots

Let F be a binary cube-edge coloring with two hubs h,k such that all four induced T-direction facet colorings obtained after fixing both hub bits have acyclic directed dependency graphs. For each ordinary starting vertex y let H_y denote the coloring of the four hub-square edges over y.

**Theorem (opposite-square equality).** If for some ordinary root y the four hub-edge colors at y equal their corresponding colors at bar y, then F has at least two paired roots.

*Proof.* Every binary edge coloring of Q2 has at least two paired hub starting corners. Choose any such corner sigma in H_y. It supports both a full 0*1* hub geodesic and a full 1*0* hub geodesic. Lift either path as follows. If its two hub edges are monochromatic in the initial phase (zero for the nondecreasing order, one for the nonincreasing order), traverse the two hubs first at ordinary y, then traverse all T directions in the final hub facet. If both hub edges have the terminal phase color, traverse all T directions first in the initial hub facet, arriving at bar y, then traverse the two hub edges there. If its hub colors are initial-phase then terminal-phase, traverse the first hub at y, all T directions in the intermediate hub facet, then the second hub at bar y. The required hub-edge colors agree at y and bar y by hypothesis, and the needed full T geodesic of either orientation exists from every root in every fixed-hub facet because its dependency digraph is acyclic. Both hub geodesics therefore lift to complete dimension-simple monotone geodesics from the SAME full starting root (sigma,y). The other paired hub corner lifts in the same way. QED.

**Corollary (necessary two-feedback obstruction).** If deleting two designated hubs h,k from the global directed dependency graph makes its remaining digraph acyclic, but F has no paired root, then at every ordinary vertex y both restrictions hold:
(i) the two hub directions are not mutually dependent in the four-edge hub square over y, by the previous bipolar square theorem;
(ii) the square-coloring vector H_y is different from H_(bar y), by the theorem above.
These local constraints are necessary but are not asserted sufficient for failure. They sharpen the next two-feedback closure target without restricting the nonlinear Boolean rules on ordinary directions or requiring their four facet dependency orders to agree.


### Cross-favorability under the combined directed influence decomposition

Let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_d\), and let \(D=D(f)\cup D(g)\) record each dependence arc \(j\to i\) of either coloring. List the strongly connected components in topological order \(C_1,\ldots,C_t\), and put \(R_\nu=\bigcup_{\mu<\nu}C_\mu\). For \(y\in\{0,1\}^{R_\nu}\), let \(f^{(\nu)}_y,g^{(\nu)}_y\) be the induced colorings on \(C_\nu\), with the bits in \(R_\nu\) fixed to \(y\). Later bits do not influence these colorings. Set
\[
\rho_\nu=
\min_{y,z\in\{0,1\}^{R_\nu}}
\bigl|A_0(f^{(\nu)}_y)\cap A_1(g^{(\nu)}_z)\bigr|.
\]

**Theorem (two-coloring directed-component product).** For every pair \(f,g\),
\[
\boxed{\bigl|A_0(f)\cap A_1(g)\bigr|
\ge \prod_{\nu=1}^{t}\rho_\nu
\ge \prod_{\nu=1}^{t}\kappa_{|C_\nu|},}
\]
where \(\kappa_m=\min_{u,v:E(Q_m)\to\{0,1\}}
|A_0(u)\cap A_1(v)|\). Empty products are one.

*Proof.* Induct over the ordered components. Suppose \(x\) supports an \(f\)-geodesic with word \(0^*1^*\) and a \(g\)-geodesic with word \(1^*0^*\) in the earlier directions. Let \(y\) be the first path's vertex after its zero prefix, and \(z\) the second path's vertex after its one prefix; these states may differ. Choose
\[
w\in A_0(f^{(\nu)}_y)\cap A_1(g^{(\nu)}_z).
\]
Insert a full \(f^{(\nu)}_y\)-geodesic from \(w\) at the first seam and a full \(g^{(\nu)}_z\)-geodesic from \(w\) at the second seam. Both resulting words retain their monotonicity. Every earlier direction's edge colors are independent of the bits in \(C_\nu\); otherwise \(D\) would contain an arc from \(C_\nu\) into an earlier component, contradicting the topological order. Thus the old steps retain their colors, and both enlarged paths start at the same root \((x,w)\) and traverse every processed direction once. For each earlier common root there are at least \(\rho_\nu\) distinct choices of \(w\). Multiplication gives the first inequality, and the definition of \(\kappa_m\) gives the second. \(\square\)

**Corollary (jointly acyclic influences).** If \(D(f)\cup D(g)\) is acyclic, then
\[
\boxed{A_0(f)=A_1(g)=V(Q_d).}
\]
Indeed every component is a singleton, whose two induced colorings are constant; thus \(\rho_\nu=\kappa_1=2\), and the lower bound is \(2^d\).

**Corollary (joint feedback blocks).** If every strongly connected component of \(D(f)\cup D(g)\) has size at most three, then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{t_1+t_2+2t_3},}
\]
where \(t_j\) is the number of components of size \(j\). This follows analytically from \(\kappa_1=\kappa_2=2\) and \(\kappa_3=4\). The separately certified four-cube result \(\kappa_4=2\) also gives a factor \(2^{t_4}\) when four-direction components occur.

More generally, the theorem applies if every conditional pair \((f^{(\nu)}_y,g^{(\nu)}_z)\) has intersecting opposite-orientation favorable-root sets. The interaction-path, nonlinear-star, and crossed-square-factorization theorems supply arbitrarily large eligible components. Any counterexample to unrestricted two-coloring cross-favorability therefore has a strongly connected component of at least four directions in its **combined** influence digraph, or at least five subject to the four-cube certificate.

This extension of the one-coloring component theorem allows the two colorings and their seam states to differ. It leaves open the case of an unrestricted large feedback component, including the unresolved cyclic-neighbor cross-favorability conjecture.


### Abundant paired roots need not share a phase seam

For a full \(0^*1^*\) direction-simple geodesic define its *rising seam* to be the vertex reached after its zero-colored prefix. For a full \(1^*0^*\) geodesic define its *falling seam* to be the vertex reached after its one-colored prefix. The seams are well defined also for monochromatic words: an all-zero rising path has seam at its endpoint, while an all-zero falling path has seam at its starting root.

**Theorem (complete influence with no common-seam root).** For every \(n\ge3\), there is an arbitrary undirected binary edge coloring \(h\) of \(Q_n\) such that
\[
\boxed{D(h)\text{ is the complete bidirected influence graph},\qquad
P(h)=Q_n\setminus\{0^n,1^n\},}
\tag{CS1}
\]
yet for **no** starting root do a rising full geodesic and a falling full geodesic have the same seam vertex.

*Proof.* Give color one to precisely the \(n\) cube edges incident with \(0^n\), and color zero to every other edge. Equivalently, the direction-\(i\) edge-color function is
\[
h_i(x)=\prod_{j\ne i}(1+x_j)\pmod2.
\tag{CS2}
\]
For each distinct \(i,j\), flipping bit \(j\) changes \(h_i\) when all other arguments vanish, so every influence arc \(j\to i\) occurs.

From \(0^n\), the first edge of every complete geodesic is colored one and all subsequent edges zero. Thus the rising orientation is impossible there. The reversed statement holds from \(1^n\), where every complete geodesic ends with a color-one edge, preventing the falling orientation.

Take now a root \(x\) with Hamming weight \(1\le k\le n-1\). Traverse first every bit that is initially zero, then every bit initially one. The resulting full geodesic never visits \(0^n\), so every edge has color zero. It supports both monotone orientations, proving the paired-root assertion of (CS1).

Every full geodesic from such a root either avoids \(0^n\), and has word \(0^n\), or visits \(0^n\) after the \(k\) initially-one bits have been flipped and before any initially-zero bit is flipped. In the second case its edge word is
\[
\boxed{0^{k-1}11\,0^{n-k-1}.}
\tag{CS3}
\]
(The two color-one edges enter and leave the origin.) If \(1<k<n-1\), word (CS3) has two switches, so every favorable full geodesic is all zero. Its rising seam is \(\bar x\), while its falling seam is \(x\), distinct vertices.

If \(k=1\), the rising full geodesics must again have all-zero words, so their seam is \(\bar x\), of Hamming weight \(n-1\). Every falling geodesic has seam of Hamming weight one: either its root \(x\) in the all-zero case, or the vertex reached immediately after the two one-colored steps in (CS3). These seam sets are disjoint for \(n\ge3\).

If \(k=n-1\), the argument reverses. Every falling geodesic is all zero and has seam \(x\), of weight \(n-1\), while every rising seam has Hamming weight one, whether the word is all zero or of the form (CS3). The seam sets again are disjoint. The endpoint roots \(0^n,1^n\) have only one monotone orientation. Hence no root admits a shared rising/falling seam. \(\square\)

**Implication for source-block gluing.** A proposed induction deleting arbitrary source strongly connected components cannot rely on choosing opposite monotone paths with a common seam. This construction has maximum possible off-diagonal influence and paired-root density \(1-2^{1-n}\to1\), but its two phase-seam sets remain disjoint at every root. Therefore a source-block induction must exploit two distinct seam slices through cross-favorability, or use an insertion mechanism such as periodic-block restoration that does not require seam coincidence.



### Strong connectivity is necessary for a cyclic-local cross-root obstruction

**Theorem (cyclic feedback irreducibility).** Let \(n\ge3\), and let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_n\) whose local edge-color functions depend only on the two cyclically neighboring direction bits. If the **union directed influence graph**
\[
D=D(f)\cup D(g)
\]
is not strongly connected, then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{CF1}
\]
Consequently, a counterexample to the shared-site cyclic cross-favorability conjecture can occur only when the combined directed influence graph is strongly connected on the entire cycle. The assertion places no restriction on the local truth tables, and applies to two unrelated cyclic-local colorings even without a common site.

*Proof.* Let \(C_1,\ldots,C_t\) be the strongly connected components of \(D\). Since \(D\) is not strongly connected, \(t\ge2\), and every \(C_\nu\) is a proper subset of the \(n\) direction indices. The union **undirected** interaction graph of \(f,g\) is contained in the simple cycle on those indices. Therefore the interaction graph induced on \(C_\nu\) is a disjoint union of paths and isolated vertices. Fix arbitrary assignments of the bits in all earlier components. Because the SCCs are topologically ordered, neither induced coloring on \(C_\nu\) depends on bits in later components. The two resulting conditional colorings have a combined interaction graph contained in a path forest. The established all-dimensional path cross-favorability theorem gives
\[
A_0(f^{(\nu)}_y)\cap A_1(g^{(\nu)}_z)\ne\varnothing
\quad\text{for every earlier-state pair }(y,z).
\]
Thus \(\rho_\nu\ge1\) for every component in the combined directed-component product theorem. Their product is positive, proving (CF1). \(\square\)

**Degree-two extension.** Suppose the union undirected interaction graph of \(f,g\) has maximum degree at most two. Each connected component is a path, a cycle, or a singleton. A path component is settled by universal path cross-favorability. A cyclic component is settled by the theorem above unless its entire vertex set is one strongly connected component of the union directed influence graph. Cartesian factorization across independent interaction components then shows that any cross-root failure requires at least one cyclic interaction component that is strongly connected under the union directed influence graph. This statement makes no claim about branched trees or general pseudoforests.

The theorem isolates **irreducible global feedback**, rather than deficient overlap sites, as a necessary obstruction for arbitrary cyclic pairs. It combines two distinct all-dimensional tools: componentwise phase-seam insertion and path-local cross-favorability.



**Corollary (directed Hamilton feedback forced by a shared projection site).** In the preceding cyclic-local setting, suppose that at some site \(j\) the two local functions agree and are the projection \(f_j=g_j=x_{j-1}\), with cyclic indices. If
\[
A_0(f)\cap A_1(g)=\varnothing,
\]
then the combined directed influence graph contains the consistently oriented directed Hamilton cycle
\[
\boxed{j\longrightarrow j+1\longrightarrow j+2
\longrightarrow\cdots\longrightarrow j-1\longrightarrow j.}
\tag{CF2}
\]

*Proof.* The shared projection gives the arc \(j-1\to j\), and ensures the reverse-neighbor arc \(j+1\to j\) is absent. By the previous theorem, a hypothetical cross-root failure forces the union influence graph to be strongly connected. Moreover the union undirected interaction graph must use the edge \(j,j+1\): if that edge were absent, the entire interaction graph would lie in a path, where cross-favorability has already been proved. As \(j+1\to j\) is absent, the arc \(j\to j+1\) must therefore occur.

Strong connectivity supplies a directed simple path from \(j+1\) to \(j\). Since its first vertex is \(j+1\), it cannot use the nonexistent direct arc \(j+1\to j\). Every arc follows an edge of the undirected cycle \(C_n\), and the only simple path in \(C_n\) from \(j+1\) to \(j\) avoiding their direct edge is
\[
j+1,j+2,\ldots,j-1,j.
\]
Hence every successive forward arc occurs. Joining the already established \(j\to j+1\) gives (CF2). \(\square\)

In particular, if the union pair has no directed Hamilton cycle of this orientation, the shared-projection cross-root assertion holds in every dimension. The other unresolved shared-site prototype, \(H(a,b)=a\land b\), has two incoming neighbor influences and requires a different structural argument.


## Root-diagonal transport and cross-favorability under one feedback vertex

For any binary coloring f of undirected edges of Q_n, let D(f) contain an arrow j->i when a direction-i edge color depends on bit j. Let A_0(f), A_1(f) be roots of full dimension-simple geodesics with words 0^*1^*, 1^*0^* respectively. We assume n>=2. A direction h is a feedback vertex when D(f)-h is acyclic.

**Lemma 1 (all-root acyclic geodesics).** An edge coloring with acyclic directed influence graph has a rising full geodesic from every root. The assertion remains true after restricting to any set of directions and fixing the remaining bits.

*Proof.* Choose a sink direction i: its bit influences no other edge color. By induction take a rising geodesic on the other directions. Insert i at its zero-to-one seam, putting its step in the appropriate color block. The original steps retain their colors, giving a rising complete geodesic. Induced dependency subgraphs of a DAG remain acyclic. QED.

**Theorem 2 (hub fiber and diagonal transport).** Suppose D(f)-h is acyclic. Write x=(s,y), separating the h-bit s from the remaining bits y. Then

\[
\boxed{x\in A_0(f)\ \text{or}\ x\oplus e_h\in A_0(f).}\tag{HD1}
\]

For every j distinct from h,

\[
\boxed{x\in A_0(f)\ \text{or}\ x\oplus e_h\oplus e_j\in A_0(f).}\tag{HD2}
\]

Furthermore each fixed-h-bit face meets A_0(f). The same assertions hold with A_1(f) in place of A_0(f).

*Proof.* Fix s,y. In the facet h=s choose, by Lemma 1, a rising complete geodesic over a set T of nonhub directions, leaving all other bits fixed. Write B for its zero-prefix directions and z=y xor 1_B for the endpoint of that prefix. All edges in the remaining suffix T\B have color one.

For (HD1), take T to be all nonhub directions. If the hub edge over z has color zero, start at x, traverse B, cross the hub edge, then take a rising full geodesic on the remaining directions in h=1-s. If the hub edge has color one, start at x xor e_h, take a rising geodesic over B in the facet h=1-s, cross the same hub edge, and follow the original color-one suffix T\B in h=s. All restricted remaining colorings are acyclic, so the required rising insertions exist and both resulting routes traverse each dimension once.

For (HD2), take T=[n]\{h,j}, with bit j held at its value in y. If the hub edge over z has color zero, use B from x, cross the hub edge, and finish by a rising geodesic over all remaining nonhub directions, including j, in h=1-s. If the hub edge has color one, start at x xor e_h xor e_j, traverse B union {j} by a rising geodesic in h=1-s, and arrive at leaf state z. Cross the hub edge and follow the original color-one suffix T\B in h=s. The original suffix has the same edge colors because the state at its beginning is z in both paths. These are rising full geodesics.

To prove the fixed-face assertion, choose any nonhub vertex z and fixed hub bit s. If the hub edge over z is zero, take it first from (s,z) and follow a rising nonhub geodesic in h=1-s. If its color is one, begin at (s,bar z), follow a rising nonhub geodesic in h=s ending at (s,z), and take the hub edge last. Either way the starting hub bit is s. Applying the proof to the complementary coloring 1-f proves the falling variants. QED.

**Corollary 3 (square restriction).** On any root square spanned by h and another direction j, at most two roots fail A_0(f). If two fail, they share the same h-bit. The same holds for A_1(f).

*Proof.* The fiber property HD1 permits at most one failure for each fixed j-bit. If two failures had different h-bits they would form the forbidden diagonal in HD2. QED.

**Theorem 4 (two-coloring one-feedback-vertex closure).** Suppose f and g are arbitrary edge colorings of Q_n, and there exist h,k for which D(f)-h and D(g)-k are acyclic. Then

\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{HD3}
\]

When h and k are distinct,

\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-2}.}\tag{HD4}
\]

*Proof.* Suppose first h and k are distinct. Fix all root bits outside {h,k}, giving a four-root square. By Corollary 3, the roots in this square outside A_0(f) number at most two; if two, they form a pair with common h-bit. Likewise roots outside A_1(g) number at most two; if two, they form a pair with common k-bit. A two-point h-row and a two-point k-column intersect. Hence the union of these two unfavorable sets occupies at most three of the four roots. The square contains a cross-favorable root, and all 2^{n-2} disjoint squares give HD4.

Now let h=k. For each nonhub bit vector y, HD1 supplies at least one of (0,y),(1,y) in A_0(f), and at least one in A_1(g). Suppose their intersection were empty. Every such hub fiber would then have one favorable root of each type, at opposite hub bits. Thus its unfavorable A_0(f)-root would have the form (s(y),y). Applying HD2 to neighboring nonhub states y,y xor e_j forces s(y)=s(y xor e_j). Connectivity of Q_{n-1} makes s constant. One fixed-h-bit face would then have no A_0(f)-root, contradicting Theorem 2. QED.

**Corollary 5 (combined influence components).** Let D=D(f) union D(g). If every strongly connected component of D has a feedback vertex, then A_0(f) intersects A_1(g).

*Proof.* In the directed-component seam-insertion theorem, each conditional pair on a strongly connected component has influence graphs contained in the induced digraph of D on that component. Its feedback vertex works for both conditional colorings, so Theorem 4 gives cross-favorability for each component. The component product is positive. Singleton components follow from Lemma 1. QED.

Theorem 4 allows arbitrary nonlinear dependence at the exceptional directions and different dependency structures for f,g. A hypothetical failure of unrestricted two-color cross-favorability must therefore contain a strongly connected component of the combined influence graph requiring at least two vertex deletions to become acyclic. The checkerboard obstruction conjectured for one multi-input direction is eliminated when deleting that direction leaves an acyclic influence digraph.


## Arbitrary-subset hub transport and sharp half-cube cross-root bound

The preceding diagonal transfer admits a stronger form, with a subset of nonhub directions replacing the single direction j.

**Theorem 6 (arbitrary-subset transport).** If D(f)-h is acyclic, then for every root x=(s,y) and every subset J of nonhub directions,

\[
\boxed{(s,y)\in A_0(f)\quad\text{or}\quad
(1-s,y\oplus\mathbf1_J)\in A_0(f).}\tag{HT1}
\]

The same holds for A_1(f). Consequently, one of the two full (n-1)-dimensional faces h=0 or h=1 lies entirely inside A_0(f), and one of them lies entirely inside A_1(f).

*Proof.* Fix J and set T=[n]\setminus(\{h\}\cup J). In the facet h=s, with all J-bits frozen at their values in y, use the acyclic all-root lemma to find a rising geodesic over T. Write B for its zero-prefix directions and z=y xor 1_B for the prefix endpoint. Every edge in the remaining T\B suffix has color one.

If the hub edge over z has color zero, from (s,y) traverse B along its color-zero prefix, cross the hub edge, and traverse all unread nonhub directions in a rising order in the facet h=1-s. This is possible because the induced influence digraph is acyclic.

If the hub edge over z has color one, start at (1-s,y xor 1_J), traverse B union J in a rising order in the facet h=1-s, cross the hub edge at z, and traverse the original all-one suffix T\B in the facet h=s. Both constructions use every direction once. This proves HT1.

Fix s. If any root (s,y) is unfavorable, HT1, as J ranges through all subsets of the nonhub directions, places every root (1-s,y') in A_0(f). If the h=s face has no unfavorable root, it is already fully favorable. Applying the argument to 1-f gives the A_1 conclusion. QED.

**Lemma 7 (antipodal-pair coverage within each hub facet).** For each fixed hub bit s, at least 2^(n-2) starting roots of that facet lie in A_0(f), and at least 2^(n-2) lie in A_1(f).

*Proof.* For each nonhub bit vector y, inspect the color t of the hub edge over y. If t=0, the root (s,y) is rising-favorable: cross h first, then take an acyclic rising full geodesic in the opposite facet. If t=1, the root (s,bar y) is rising-favorable: take an acyclic rising full geodesic in the facet h=s from bar y to y, and cross h last. Thus every antipodal pair {y,bar y} of nonhub starting vectors contains at least one rising-favorable root in the fixed hub facet. There are 2^(n-2) such pairs. Color complementation gives the falling assertion. QED.

**Theorem 8 (sharp favorable-root and two-color intersection bounds).** If D(f)-h is acyclic, then

\[
\boxed{|A_0(f)|\ge3\cdot2^{n-2},\qquad
|A_1(f)|\ge3\cdot2^{n-2}.}\tag{HT2}
\]

If f,g have possibly different feedback vertices, with D(f)-h and D(g)-k acyclic, then

\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-1}.}\tag{HT3}
\]

Both numerical bounds are sharp for every n>=2.

*Proof.* By Theorem 6, one hub facet is entirely contained in A_0(f), contributing 2^(n-1) roots; by Lemma 7 the other contributes at least 2^(n-2). The argument applies also to A_1. For two colorings, inclusion-exclusion and HT2 yield

\[
|A_0(f)\cap A_1(g)|
\ge |A_0(f)|+|A_1(g)|-2^n
\ge 2^{n-1}.
\]

For sharpness, take the reciprocal two-direction readers f_1(x)=x_2 and f_2(x)=x_1, and give all other directions constant edge colors independent of the first two bits and of one another. On Q_2 the rising favorable-root set has three vertices and the paired-root set has two. Cartesian factorization with the independent constant directions gives |A_0(f)|=3·2^(n-2) and |A_0(f) intersect A_1(f)|=2^(n-1). The dependency digraph consists of a two-cycle and isolated vertices, so deleting either cycle direction makes it acyclic. QED.

This strengthens Theorem 4 above: the cross-root conclusion has a sharp half-cube lower bound for both coincident and distinct feedback vertices. It extends the previously established nonlinear-star root bound to arbitrary nonlinear acyclic dependence among all nonhub directions.


**Corollary 9 (universal antipodal transversal).** If D(f)-h is acyclic and g is any edge coloring of the same cube, then

\[
\boxed{|A_0(f)\cap P(g)|\ge\tfrac12|P(g)|.}\tag{HT4}
\]

In particular, every coloring g with a paired root is cross-favorable against f, even if g has unrestricted nonlinear influence. The analogous inequality holds for A_1(f).

*Proof.* The paired-root set P(g)=A_0(g)\cap A_1(g) is invariant under antipodal complementation, because reversing a full geodesic changes its monotonic orientation. Every antipodal pair in P(g) has one endpoint in each fixed-h-bit face. Theorem 6 puts one whole fixed-h-bit face in A_0(f). Therefore that face contains |P(g)|/2 paired roots of g, proving HT4. Complementing the coloring f proves the falling version. QED.

This extends the functional-cycle antipodal-transversal criterion to every coloring admitting a one-direction feedback vertex, without restrictions on its nonlinear edge functions away from the feedback vertex beyond acyclicity of their induced influence digraph.


**Corollary 10 (sharp componentwise paired-root multiplicity).** Let D=D(f) union D(g), and suppose every nontrivial strongly connected component C of D has a vertex whose deletion makes D[C] acyclic. If s is the number of strongly connected components of D having at least two vertices, then

\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{n-s}.}\tag{HT5}
\]

In particular, if f=g, then |P(f)|>=2^(n-s). The bound is attained when f=g is a Cartesian product of reciprocal two-direction readers, with any number of independent constant directions.

*Proof.* The directed-component product theorem inserts separate monotone paths at their respective seams and multiplies cross-root counts. A nontrivial component of order m has at least 2^(m-1) compatible roots by Theorem 8, uniformly over earlier-facet assignments in the two colorings. Every singleton component has two compatible root bits because its edge color is constant after the earlier bits are fixed. Multiplying the component bounds gives 2^(n-s). For sharpness each reciprocal-reader pair contributes two paired roots on two dimensions and each isolated constant direction contributes two; Cartesian factorization gives the claimed equality. QED.


## Fiberwise paired roots and antipodal diagonal squares

Let \(f\) be any binary coloring of the undirected edges of \(Q_n\), with directed influence digraph \(D(f)\). Assume \(D(f)-h\) is acyclic. Write a cube root as \((s,y)\), separating its bit \(s\) in direction \(h\) from its remaining bit vector \(y\), and put \(P(f)=A_0(f)\cap A_1(f)\).

**Theorem (paired-root fiber property).** For every nonhub vector \(y\), at least one of \((0,y),(1,y)\) belongs to \(P(f)\). Consequently \(|P(f)|\ge2^{n-1}\). There is an antipodally equivariant Boolean selector \(s(y)\) satisfying
\[
\boxed{(s(y),y)\in P(f),\qquad s(\bar y)=1-s(y).}\tag{PF1}
\]

*Proof.* The preceding hub-fiber transport theorem gives at least one point of \(A_0(f)\) in each two-vertex hub fiber. By complementing every edge color, the same holds for \(A_1(f)\). If these two favorable sets were disjoint on a particular fiber, there would be an \(s\) for which \((s,y)\notin A_0(f)\) and \((1-s,y)\notin A_1(f)\). Reversing a full geodesic shows \(A_1(f)=\overline{A_0(f)}\), so \((s,\bar y)\notin A_0(f)\). This contradicts the earlier antipodal-pair coverage lemma, which guarantees that either \((s,y)\) or \((s,\bar y)\) belongs to \(A_0(f)\) for every fixed hub bit \(s\). Thus each hub fiber meets \(P(f)\). Since \(P(f)\) is invariant under full antipodal complementation, choose a paired-root hub bit on each pair of complementary nonhub states, and choose the complementary hub bit at the complementary state. This yields (PF1). \(\square\)

**Theorem (many diagonal paired-root squares).** If \(n\ge2\), at least \(2^{n-2}\) distinct cubical squares involving direction \(h\) have a pair of opposite vertices in \(P(f)\). The bound is sharp.

*Proof.* Fix the selector \(s\) in (PF1), and let \(\partial s\) be the edges of \(Q_{n-1}\) whose endpoint selector values differ. Follow a uniformly random full antipodal geodesic in \(Q_{n-1}\), choosing its root uniformly and its direction permutation uniformly. Because \(s(\bar y)=1-s(y)\), the number of selector changes is odd and at least one. The traversed edge of any specified direction is uniformly distributed among the \(2^{n-2}\) edges of that direction. Consequently,
\[
1\le\mathbb E[\text{selector changes}]
=\frac{|\partial s|}{2^{n-2}},
\]
so \(|\partial s|\ge2^{n-2}\).

For each edge \(\{y,y\oplus e_j\}\in\partial s\), the vertices \((s(y),y)\) and \((s(y\oplus e_j),y\oplus e_j)\) are opposite corners of the cubical square with directions \(h,j\), and both belong to \(P(f)\). Different nonhub edges give different squares. For equality take reciprocal readers in directions \(h,j\), with all other direction colors constant and independent. Then each hub fiber has a unique paired root, whose hub bit is \(1-y_j\); the selector changes only on the \(2^{n-2}\) edges of direction \(j\). \(\square\)

These conclusions hold for unrestricted nonlinear edge functions at the feedback vertex and arbitrary acyclic interactions among the remaining direction classes. The diagonal squares provide a family of paired-root path-exchange certificates for attempts to restore a second feedback direction.


### Equality rigidity and spectral surplus of paired-root diagonal squares

Let s:Q_d -> F_2 be any antipodally odd Boolean selector, s(bar y)=1-s(y), including those obtained from the one-feedback-vertex paired-root fiber theorem. Let B(s) be the number of its bichromatic cube edges. Put sigma(y)=(-1)^{s(y)}, and use the normalized Walsh expansion
\[
\sigma(y)=\sum_{S\subseteq[d]}\widehat\sigma(S)\chi_S(y),\qquad
\chi_S(y)=(-1)^{\sum_{i\in S}y_i}.
\]

**Theorem (sharp rigidity and surplus identity).** The Fourier coefficients of sigma vanish for all even-size S, and
\[
\boxed{
\frac{B(s)}{2^{d-1}}-1
=\sum_{\substack{S\subseteq[d]\\ |S|\ge3,\ |S|\ {\rm odd}}}
(|S|-1)\widehat\sigma(S)^2.}\tag{FS1}
\]
In particular B(s)>=2^(d-1), with equality if and only if
\[
\boxed{s(y)=y_j+\epsilon\pmod2}
\]
for some direction j and bit epsilon. Moreover
\[
\boxed{
\sum_{\substack{|S|\ge3\\ |S|\ {\rm odd}}}
\widehat\sigma(S)^2
\le \frac{B(s)-2^{d-1}}{2^d}.}\tag{FS2}
\]

*Proof.* The antipodal identity sigma(bar y)=-sigma(y) implies
\(\widehat\sigma(S)=(-1)^{|S|+1}\widehat\sigma(S)\); hence every even-level coefficient vanishes. Parseval gives \(\sum_S\widehat\sigma(S)^2=1\).

For direction i, the normalized probability of a selector change under bit i is
\[
\Pr[\sigma(y)\ne\sigma(y\oplus e_i)]
=\frac14\mathbb E[(\sigma(y)-\sigma(y\oplus e_i))^2]
=\sum_{S\ni i}\widehat\sigma(S)^2.
\]
There are 2^(d-1) undirected edges in each direction. Summing gives
\[
B(s)=2^{d-1}\sum_S|S|\widehat\sigma(S)^2.
\]
Subtract the Parseval identity and use the vanishing of even-level coefficients to obtain (FS1). Since every surviving term with |S|>=3 has |S|-1>=2, (FS2) follows.

If equality holds, sigma has only level-one coefficients, so
\(\sigma(y)=\sum_i a_i(-1)^{y_i}\). The Boolean identity \(\sigma(y)^2=1\) implies \(\sum_i a_i^2=1\) and \(a_i a_j=0\) for all i distinct from j, by comparing the independent Walsh coefficients on pairs. Thus a single a_j equals +1 or -1, and sigma is a signed single-bit character. This is equivalent to the displayed form for s. Conversely, such a selector changes only on the 2^(d-1) edges of direction j. \(\square\)

When d=n-1, the theorem classifies every minimum-size family of paired-root diagonal squares arising from a feedback-vertex selector. For an extremal choice of selector, either the section is a signed one-bit reader, or a strictly positive cut surplus is forced; FS2 quantitatively controls the non-reader spectral mass.


## Componentwise closure with owner-local hub dependence

The former version of the multi-hub strongly connected component theorem (CH2) omitted a necessary hypothesis. Its proof invoked the unconditional hub-lifting assertion MH1, disproved by the four-dimensional counterexample in the two-hub selector Subsection. The original proof does not establish its stated conclusion when a leaf can influence more than one hub. The following corrected statement supplies a rigorous dimension-uniform component theorem.

Let \(D(f)\) be the directed influence digraph of an arbitrary binary edge coloring \(f\) of \(Q_N\). Order its strongly connected components \(C_1,\ldots,C_t\) so that the colors of directions in \(C_j\) may depend on preceding components but are independent of all later components. Suppose that for each \(C_j\) there is a nonempty designated hub set \(H_j\subseteq C_j\), with \(h_j=|H_j|\le4\), such that:

1. Every direction \(i\in C_j\setminus H_j\) has a globally fixed unary rule
\[
f_i(x)=a_i+\lambda_i x_{p(i)},\qquad
a_i,\lambda_i\in\mathbb F_2,\quad p(i)\in H_j.
\tag{CH-C1}
\]
In particular these leaf rules do not vary with assignments to preceding components.

2. For each such \(i\), all hub-direction edge-color functions \(f_h\), \(h\in H_j\setminus\{p(i)\}\), are independent of \(x_i\). A hub can depend arbitrarily on its own leaves, other hub bits, and earlier-component bits. No hub may read a leaf assigned to another hub.

Put \(\beta_1=\beta_2=2\), \(\beta_3=4\), and \(\beta_4=2\).

**Theorem (owner-local SCC cross-seam lifting).** Under these hypotheses,
\[
\boxed{|P(f)|\ge\prod_{j=1}^{t}\beta_{h_j}>0.}
\tag{CH-C2}
\]
For components with four hubs the theorem uses the previously certified unrestricted \(Q_4\) favorable-root minimum of nine; for up to three hubs it uses the corresponding \(Q_1,Q_2,Q_3\) bounds. It is enough that conditions (CH-C1) and (2) hold componentwise; the hub functions may change arbitrarily with preceding bits.

*Proof.* Suppose we have selected a paired starting root on the previously processed components and its rising and falling full witness paths. They have possibly different zero-to-one seam states in earlier directions. Condition on these two earlier seam states to obtain two colorings of the next component. Their hub functions may differ, but by (CH-C1) their leaf functions agree and remain unary in their designated reader hub. Condition (2) gives owner-local independence in both conditional colorings.

Apply the corrected owner-local cross-hub lifting theorem to these two conditional colorings. The rising hub coloring with all leaves fixed to zero and the falling hub coloring with all leaves fixed to one each have at least \(a_h\) favorable hub roots, where \(a_1=2,\ a_2=3,\ a_3=6,\ a_4=9\). By inclusion-exclusion their opposite-orientation root sets intersect in at least \(2a_h-2^h\) hub roots: respectively \(2,2,4,2\). Each such hub root extends to one common starting root of the two component paths.

Insert the rising component path at the zero-to-one seam of the earlier rising witness and the falling component path at that of the earlier falling witness. Colors of earlier directions are independent of later bits by the condensation ordering, and the component paths use the new directions once each. Hence the full resulting paths remain monotone and share the same combined starting root. Distinct hub roots produce distinct extensions, and extensions of distinct earlier roots remain distinct. Inducting over the component order proves (CH-C2). \(\square\)

**Construction.** With the SCC decomposition and designated owner-local unary rules supplied, one paired root and two witness orders can be found using \(O(N)\) direction-edge evaluations and \(O(N^2)\) elementary operations. Tabulate the hub colorings on at most four bits at the two earlier seam states, enumerate hub roots and orders to find a cross-favorable hub root, choose each leaf's starting bit by the two-case owner-local lemma, and topologically sort the monotone phase-compatible precedence constraints. Only a bounded number of hub-edge evaluations is needed per component and at most two unary leaf evaluations per nonhub direction. Updating explicit witness orders by insertion takes \(O(N^2)\) list operations. This construction does not include discovery of the influence digraph from an oracle.

**Scope and correction.** The theorem does not cover arbitrary three- or four-hub stars. In particular merely having globally fixed unary reader rules for nonhubs, or only three branching vertices in a strongly connected component, is insufficient for the owner-local proof: nonlinear hub functions might read a leaf assigned to a different hub. The previous unrestricted CH2 statement and its unrestricted constructive corollary are withdrawn as unsupported by that argument. This qualification leaves the separately proved one-feedback and two-hub-star results intact.


## Permutation-reader SCC closure with variable predecessor conditions

**Theorem.** Let F color the undirected edges of Q_N. Assume every strongly connected component C of the directed influence graph either satisfies a previously proved positive cross-favorable criterion, or has three hubs h_0,h_1,h_2 and three fixed disjoint nonhub groups L_0,L_1,L_2, with arbitrary multiplicities. At each fixed assignment y of preceding-component bits, require that all leaves w in L_i obey
\[
F^y_w(z)=z_{h_{\sigma_y(i)}}+a_{i,y}\pmod2,
\tag{CPS1}
\]
where the reader assignment \(\sigma_y\) is **any permutation** of the three hubs and the offsets \(a_{i,y}\) are arbitrary. Both the permutation and offsets may change with y. Hub edge functions are unrestricted nonlinear functions of every other internal bit and may also change with y.

Then F has a paired root. In particular every antipodally odd coloring on Q_(N+1) with such a lower-facet coloring has a monochromatic full antipodal geodesic, regardless of bridge-edge colors.

*Proof.* Process the directed SCCs in topological order. At any step choose rising and falling geodesics from a common root in the processed prefix, with seam states y_0 and y_1. The next block's conditional colorings F^{y_0} and F^{y_1} satisfy the full permutation-reader cross theorem (PRH2), even when their reader permutations, offsets, and nonlinear hub tables differ. They therefore admit rising and falling full block geodesics from a common block root. Insert each block path into the respective prior seam. Previous edge colors ignore future block bits, so neither path's earlier colors change. Each enlarged path remains monotone and uses all directions once. Repeat for all components; the other allowed component classes use their previously established cross-root lemmas. Apply the free-bridge equivalence to obtain the final statement. \(\square\)

**Constructive form.** Given the SCC decomposition and reader assignments, each three-hub block can be solved using at most 192 evaluations of the two conditional hub-edge truth tables: clone-contract its leaf groups to one representative each, add any absent dummy groups, enumerate roots and orders in the resulting Q_6 core, and lift the chosen paths by consecutive leaf duplication. Across all components this gives O(N) edge-color evaluations and O(N^2) elementary list operations, exclusive of finding the SCC decomposition from an arbitrary black-box coloring.

**Boundary.** Reader maps with repeated hub assignments, or leaf offsets varying within a fixed group, are not covered. This all-dimensional component theorem uses a computer-assisted six-cube core but does not invoke the earlier refuted unrestricted hub-to-leaf polarization lemma.

## Paired-root enumeration of unary functional influence

Let f be a binary edge coloring of Q_n in which each direction i is constant or of the form \(f_i=x_{p(i)}+\epsilon_i\pmod2\), with p(i) different from i. Its directed influence graph has indegree at most one. Let the directed cycles have lengths \(\ell_1,\ldots,\ell_t\). For a starting root x put \(\alpha_i=x_{p(i)}+\epsilon_i\) on each cycle.

**Theorem.** The root x belongs to \(P(f)\) if and only if the bits alpha_i are nonuniform on every directed reader cycle. Consequently
\[
\boxed{|P(f)|=2^{n-\sum_j\ell_j}\prod_{j=1}^t(2^{\ell_j}-2)
\ge2^{n-\tau(D(f))}.}\tag{UF1}
\]
Equality in the feedback multiplicity inequality holds precisely when every directed cycle has length two. If all directions are readers, a paired root supports monochromatic full geodesics of both colors.

*Proof.* If alpha is constant, say a, on one reader cycle, the earliest cycle step in any order sees its parent unflipped and has color a, while the latest sees its parent flipped and has color 1-a. Thus a=0 rules out falling geodesics and a=1 rules out rising geodesics. Such a root cannot be paired.

Otherwise, for either chosen color b impose that p(i) precede i in each cycle precisely when alpha_i+b=1. Nonuniform alpha guarantees that these constraints are not a directed cycle. A topological order makes every cycle step color b. Combine separate reader-cycle components, choosing color zero on all cycles for rising paths and color one for falling paths. Constant-source components are inserted in the appropriate monotone color phase. Attach every noncycle reader direction outward from its parent: because its edge color toggles when the parent is crossed, insert its direction immediately before or after the parent's step to match the parent step color. This does not modify previous direction colors; each initial new bit is arbitrary. Therefore both monotone paths start from the same root and the criterion is sufficient. When every component contains a reader cycle, choose the same monochromatic color throughout to obtain two monochromatic witnesses.

Each reader cycle admits 2^ell initial assignments, just two of which yield uniform alpha; all noncycle bits are free. This gives (UF1). The cycles are disjoint, so their number is tau(D). Each factor 2^ell-2 is at least 2^(ell-1), with equality only for ell=2. QED.

Independently verified over every signed-reader Q3 and Q4 coloring, every mixed constant/reader Q2--Q4 coloring, and random Q5--Q6 colorings (nori_signed_reader_roots_audit.py and nori_mixed_functional_roots_audit.py).


## Conditional three-hub SCC closure for arbitrary reader maps

The three-group cross-root theorem (NM5) removes the bijectivity requirement from the earlier conditional permutation-reader SCC argument.

**Theorem (unrestricted map selection at every seam).** Let F be an ordinary binary coloring of Q_N, and order the strongly connected components of its directed influence graph topologically. Suppose each component is either already covered by a previously established positive conditional cross-root theorem, or has three hubs \(h_0,h_1,h_2\) and three fixed disjoint nonhub groups \(L_0,L_1,L_2\), of arbitrary sizes, with the following property. For every assignment \(y\) of earlier-component bits, all leaves \(w\in L_i\) satisfy
\[
\boxed{F^y_w(z)=z_{h_{\rho_y(i)}}+a_{i,y}\pmod2,}\tag{RSC1}
\]
where \(\rho_y:\{0,1,2\}\to\{0,1,2\}\) is **any** map, not necessarily injective, and \(a_{i,y}\) are arbitrary signs uniform within each group. The three hub-edge functions of each conditional coloring may depend nonlinearly on all other component bits and arbitrarily on preceding bits.

Then F has a paired root. In particular every antipodally odd coloring of Q_(N+1) whose selected N-facet satisfies this hypothesis has a monochromatic full antipodal geodesic, for any legal perpendicular bridge coloring.

*Proof.* Maintain rising and falling full geodesics from a common root on the already processed SCC prefix. Their monotone phase seams may be at different prefix vertices y_0,y_1. The conditional colorings F^{y_0},F^{y_1} on the next component have the same fixed leaf groups, but can have entirely different maps \(\rho_{y_0},\rho_{y_1}\), offsets, and nonlinear hub functions. By (NM5), they have a common starting component root supporting rising and falling full component geodesics. Insert those geodesics into the two prefix seams. Earlier-direction edge colors are independent of later-component bits by the topological order, so the resulting full paths preserve their colors and use each direction once. Induction yields a paired root. Other allowed component types use their previously proved cross-root criteria. The free-bridge equivalence transfers the paired root to a monochromatic antipodal geodesic in the larger odd coloring. \(\square\)

**Constructive consequence.** With the decomposition, three group assignments, and conditional reader rules supplied, a root and both witnessing direction orders can be constructed using O(N) edge-color evaluations and O(N^2) order-list operations. At each stage contract a representative leaf of each nonempty group (add dummy leaves for absent groups), tabulate both six-dimensional conditional hub models using at most 192 hub-edge evaluations, and enumerate 64 roots and 720 orders to locate a cross-root. Expand each selected leaf step consecutively across its group and insert the two component orders into the previous seams. The constant six-dimensional search is warranted by the computer-assisted theorem. Discovering the influence graph from unrestricted black-box data is excluded from the stated query complexity.

**Limit.** This settles the global SCC branch with any three-group signed reader maps, even if all three groups read the same hub at one seam and three different hubs at the other. It does not handle arbitrarily many distinct joint leaf types or nonlinear multi-hub leaf rules, and it does not close unrestricted NORI1.


## Rooted phase signatures and omission rigidity under one-way extensions

Let c be any binary undirected-edge coloring of Q_n. Adjoin r dummy directions y, retaining original colors c_i(x) independently of y, and assign each dummy direction j an arbitrary color f_j(x) depending only on the original vertex x, independently of all dummy bits. For a root x and integer k>=1, let M_k(c,x) be the greatest length of a direction-simple path beginning at x with at most k color changes. Let O_k(c,x) be the family of sets of omitted original directions for paths attaining M_k(c,x). Then for every dummy root y, M_k(C,(x,y))=r+M_k(c,x), and O_k(C,(x,y))=O_k(c,x). In particular every maximum path in C traverses all r dummy directions, and the old-direction omission spectrum is unchanged. The same holds separately for path words with colors 0-star-1-star and 1-star-0-star. Proof: projecting away dummy steps gives the upper bound and shows every maximum extension projects to a maximum source path. Conversely choose any source maximum path. If it has a color change, pause at one such transition vertex v, traverse all dummy edges of the old color and then all dummy edges of the next color; the dummy colors f_j(v) remain fixed because dummy steps do not change x. This inserts every dummy edge without adding a change. For a monochromatic path, insert dummy edges at its beginning or end, grouped by color, requiring at most one change. Both groups retain the prescribed monotone color-word orientation as appropriate. Thus every source maximal omission set lifts and no additional omission set arises. For r=1 this holds for every undirected coloring of the new edges, because such a color is necessarily independent of its own new bit. Rootwise favorable full-geodesic sets of a single dummy extension consequently factor as the source favorable-root set times Q_1. If a hypothetical minimum-dimension coloring of Q_n had no full one-change geodesic, every codimension-one facet would have a full one-change path by minimality, so its maximum one-change paths would omit each of the n directions in some example. Therefore changing which single dummy direction survives in an independent double cannot give an obstruction based solely on globally omitted direction sets; an additional constraint relating roots or opposite facets would be needed.

MINIMAL-COUNTEREXAMPLE SATURATION. Suppose c is a hypothetical minimum-dimensional arbitrary binary cube-edge coloring of Q_n with no full one-change antipodal geodesic. Every restriction of c to either facet omitting direction i is then a coloring of Q_(n-1) with a full one-change geodesic. Thus L_1(c)=n-1 and every singleton {i}, i in [n], occurs as the omission set of some maximum one-change path of c. In its independent double c box c, maximum length equals 2n-2. Every cross-block pair {i,n+j} occurs as the omission set of a maximum one-change path, by choosing paths in a facet omitting i in the first factor and in a facet omitting j in the second, reversing path orientations as needed and interleaving their zero and one portions. Conversely the factor projection bounds demand that every maximum product path omit one direction in each block, so the complete omission family of global maxima is { {i,n+j} : i,j in [n] }, of cardinality n^2. Every (2n-1)-face of the product contains a maximum product path as well. Therefore even complete coverage of every admissible two-direction omission pair across longest paths does not imply a one-change spanning geodesic. A dimension-deletion strategy must exploit rooted endpoint, phase-seam or inter-layer color dependence, not omission supports alone.

ROOTED PHASE-SIGNATURE FACTORIZATION. For root x in c and an oriented word 0-star-1-star, define S(c;x) as the family of ordered disjoint direction sets (A,B) for which there exists a direction-simple path rooted at x, traversing precisely A during its zero phase and B during its one phase. Empty phases are allowed. The transition vertex is x xor A and the endpoint is x xor A xor B. For independent product colorings c box d, with disjoint direction labels, the entire rooted signature family factorizes: S(c box d;(x,y)) = { (A union A', B union B') : (A,B) in S(c;x), (A',B') in S(d;y) }. Necessity follows by projecting any global 0-star-1-star path onto the two blocks; sufficiency follows by interleaving both zero prefixes first and both one suffixes afterward. The analogous formula holds with colors reversed. Hence rooted oriented maximum lengths satisfy M_up(c box d;(x,y)) = M_up(c;x)+M_up(d;y), and likewise for M_down. Unoriented rooted maximum length is the maximum of these two phasewise sums; unlike global maximum lengths it need not equal the sum of the two unoriented rooted maxima. The sets of attainable transition vertices and attainable omitted direction sets likewise factor under a fixed oriented phase and fixed optimal length. This proves that the full switch-vertex signature information in an independent product carries no cross-block correlation: deletion based only on its two phase direction sets cannot enforce an exchange between factors.

SMALL-DIMENSION AUDIT. For randomized undirected edge colorings on factor cubes of dimensions (1,2),(2,2),(2,3),(3,3), rooted feasible signature families were enumerated by exhaustive direction-subset dynamic programming and agreed with their Cartesian products at every root. Separate randomized checks verified the rooted one-way extension identity and its omission spectrum for source dimensions through five and several multi-dummy extensions.

## Minimal-counterexample feedback and axis-face restrictions

STRONGLY CONNECTED MINIMAL-COUNTEREXAMPLE REDUCTION. In a binary edge coloring c of Q_n, draw a directed influence arc j->i when the i-edge color function changes under toggling bit j at some vertex. Suppose a nonempty proper set R has no incoming influence from its complement S, so all R-edge colors are independent of S-bits. If the R-coloring admits a full 0-star-1-star geodesic and every induced S-coloring at a frozen R-vertex admits some full 0-star-1-star geodesic, then c admits a full 0-star-1-star geodesic: run the R zero prefix, insert a full S zero-then-one path at its transition vertex, and finish the R one suffix. The S root can be chosen after the R transition vertex is fixed, and R steps do not read S-bits. In particular, a hypothetical minimum-dimensional counterexample to existence of an unrestricted full one-change geodesic must have a strongly connected directed influence graph. Otherwise choose a source strongly connected component R and use the minimality hypothesis on R and each conditional S-coloring, both lower-dimensional, to construct the full geodesic. This strengthens the elementary fact that a minimal counterexample cannot have a dummy-like sink direction. It is a reduction for the auxiliary arbitrary-coloring one-change problem, not by itself a proof of NORI1 or its universal paired-root condition.

AXIS-FACE NO-GO. Every axis-aligned face of an independent product c box d is itself the independent product of faces of c and d. For a fixed global phase orientation, its rooted phase-signature family therefore remains a Cartesian product, even when that face is selected adaptively according to a prior switch vertex. Thus deletion of axis directions within independently copied colorings cannot generate cross-factor phase constraints. Coupling via nonproduct color dependence, or additional antipodal/root information, would be required for the proposed amplification-then-restriction contradiction.

## Cyclic sink-component elimination

Let c be antipodally odd on Q_n, K a proper nonempty set of at most seven directions, R its complement. Assume that no direction in K influences an edge rule in R. Then c_R is a legal antipodally odd coloring on Q_R. The full-geodesic profile support and shortest monochromatic antipodal length satisfy W(c)=W(c_R) times F_2^K and ell(c)=ell(c_R)+|K|.

Proof. The established arbitrary-color at-most-one-switch geodesic theorem B_k holds for each k<=7. Fix any antipodal walk P in Q_R from z to bar z and target bits t_i on K. On the lower K-face at exterior vertex z let d_i(u)=c_i(u,z) xor t_i. Choose a K-geodesic with d-word zero^a one^(k-a); reverse the traversal first if necessary. If its zero-block U runs u0 to ua and its one-block is V, the following Q_n antipodal walk has each K-step of color t_i: start at (ua,z), traverse reverse U, follow P with K vertex fixed at u0, and traverse reverse of the full antipodal image of V in the upper K-face. The original zero-block gives c-color t; antipodal complementation makes the one-block give c-color t too. This walk preserves the complete ordered exterior projection P; if P is a full geodesic, the result is a full geodesic.

All R-rules ignore bits in K. Consequently every full c-geodesic projects to one of c_R, and any prescribed profile of c_R together with any K profile is realized by the above construction. Hence W(c)=W(c_R) times F_2^K. Likewise, any monochromatic antipodal c-path projects to a monochromatic antipodal walk of c_R with at least ell(c_R) exterior steps, and it has at least |K| new steps. For the reverse bound, choose a shortest monochromatic c_R-antipodal path as P and prescribe all K colors equal to its color. The constructed antipodal c-walk is monochromatic of length ell(c_R)+|K|. Loop-erasure and the lower bound prove the length identity. Minority defect, profile-support deficit and detour thus persist.

If every strongly connected component in the directed influence graph has size <=7, repeatedly remove a sink SCC by the theorem. The final SCC has size <=7, where the established finite NORI theorem implies all direction-profile targets are realized: recolor any direction according to a prescribed target and take a monochromatic path; antipodal reflection provides both constant colors. Back-substituting the profile cylinders gives W(c)=F_2^n for the original coloring. In particular, every NORI1 counterexample has an SCC of size >=8. Every sink SCC of a minimum-dimensional counterexample has size >=8, because otherwise deletion produces a smaller counterexample.

### Branching-sparse sink sets of unbounded size

Let c be legal and K a nonempty sink set in its directed influence graph, with R=[n]\K nonempty. Put H={i in K: i influences at least two different direction rules}, L=K\H. Assume |H|<=7; no bound on |K|. Then W(c)=W(c_R) times F_2^K and ell(c)=ell(c_R)+|K|.

Single-edge repair lemma: If an antipodal walk uses direction i once and every out-neighbor of i also occurs at most once, and i has at most one out-neighbor j, its i-step can be assigned either color while retaining all other traversed edge colors. If j precedes i, move i to the last step, otherwise to the first. This crosses no direction whose color rule depends on bit i. For first i, replace root x, order (i,sigma) by root bar(x+e_i), order (i,reverse sigma); only the first edge becomes antipodal, the remainder is traversed backwards. For last i, replace root x, order (sigma,i) by root bar x+e_i, order (reverse sigma,i). This toggles only the last edge. Both manipulations preserve antipodality even when exterior directions repeat.

Profile factorization: Start with any full c_R geodesic realizing arbitrary exterior profile w, append each L direction once, and use the established B_k antipodal two-phase bridge on H (size<=7) to prescribe all H edge colors while retaining the ordered exterior skeleton. All R colors stay w, since K has no arcs into R. For each i in L, the only possible out-neighbor lies in K and is traversed once. Apply the single-edge repair lemma to set its profile bit, preserving all previous profile bits. Every (w,t_K) therefore occurs. Conversely every full c-geodesic projects to a full c_R geodesic with unchanged R colors.

Metric identity: The projection lower bound gives ell(c)>=ell(c_R)+|K|. Start from a shortest monochromatic R antipodal path, append the L steps once, prescribe color zero on H by the B_k bridge (allowing repeated R directions), then set each L step to zero using the same individual repair. R-edge colors are unchanged. This yields a monochromatic antipodal walk of length ell(c_R)+|K|, and loop-erasure proves equality.

Corollary: Every sink strongly connected component in a minimum-dimensional NORI1 counterexample must have at least eight directions with at least two outgoing influence neighbors. Otherwise this theorem deletes it and yields a smaller counterexample. A directed cycle of any length is therefore an eliminable sink component.

**Whole-graph case.** If the influence graph has a single strongly connected component, the sink set is not proper and cannot be deleted. The earlier low-outdegree profile-cylinder theorem and seven-direction prescription theorem nonetheless force at least eight branching directions in any bad coloring. The corollary for every sink SCC of a minimum counterexample uses this separate argument in the one-component case.
