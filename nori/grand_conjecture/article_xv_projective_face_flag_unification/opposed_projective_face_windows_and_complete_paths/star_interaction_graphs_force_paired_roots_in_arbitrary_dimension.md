# Star interaction graphs force paired roots in arbitrary dimension

### Arbitrary nonlinear star interactions force paired roots

Let \(f\) color the undirected edges of \(Q_d\), \(d\ge2\). Suppose its interaction graph is a star with center direction \(c\), including the possibility of isolated directions. Split the dimensions into leaves \(L=[d]\setminus\{c\}\) and center \(c\). An edge in leaf direction \(i\) has color \(a_i(s)\), where \(s\in\{0,1\}\) is the current center bit, while center edges have unrestricted color \(b(x)\) depending on the entire leaf configuration \(x\in Q_L\). There is no affine or oddness hypothesis.

Define \(A_0(f)\) and \(A_1(f)\) as roots with full dimension-simple geodesics of respective color words \(0^*1^*\) and \(1^*0^*\), and let \(P(f)=A_0(f)\cap A_1(f)\).

**Theorem (star paired-root closure).** Every star-interaction cube-edge coloring satisfies \(P(f)\ne\varnothing\). If any leaf configuration \(x\) obeys \(b(x)=b(\bar x)\), both roots \((x,0),(x,1)\) are paired. Otherwise a paired root can be constructed from any leaf-cube edge on which \(b\) changes.

*Proof.* From root \((x,s)\), leaf steps taken before the center edge have colors \(a_i(s)\), regardless of their order, and leaf steps afterward have colors \(a_i(1-s)\). Within each group the leaf steps may therefore be sorted by color.

Suppose \(b(x)=b(\bar x)=0\). Placing the center edge first gives a \(0^*1^*\) full geodesic: its center color is zero, then post-center leaf colors are sorted ascending. Placing it last gives a \(1^*0^*\) full geodesic: initial leaf colors are sorted descending, then the center has color zero. For \(b(x)=b(\bar x)=1\), exchange which orientation uses center first and which uses center last. This proves the assertion for both starting center bits.

Otherwise \(b(\bar x)=1-b(x)\) for all \(x\), so \(b\) is nonconstant. Choose a leaf direction \(j\) and adjacent configurations \(x,y=x\oplus e_j\) with \(b(x)=0,b(y)=1\). Choose \(s\in\{0,1\}\) such that \(a_j(s)=1\) or \(a_j(1-s)=0\). An admissible \(s\) exists: if neither condition holds for \(s=0\), then \(a_j(0)=0,a_j(1)=1\), making the first condition true for \(s=1\).

From \((x,s)\), placing the center first (color zero) and sorting all leaf steps ascending yields \(0^*1^*\).

For the reverse orientation there are two cases. If \(a_j(s)=1\), take direction \(j\) first (color one), then center at leaf configuration \(y\) (color one), followed by every other leaf direction sorted descending; this gives \(1^*0^*\). Otherwise \(a_j(1-s)=0\). Take all leaf steps except \(j\) first, sorted descending; then cross the center; then take \(j\) last. At the center crossing the leaf configuration equals \(\bar y\), so the center color is \(b(\bar y)=1-b(y)=0\); the final \(j\)-edge also has color zero. This again gives \(1^*0^*\). Both witnesses start at \((x,s)\) and traverse every dimension once. QED.

**Corollary.** An interaction-connected paired-root counterexample cannot have a star interaction graph, even when every dimension class is nonuniform. More generally, a counterexample under the Cartesian-product factorization must have some interaction component not governed by a single hub.

**Closure direction.** This proof supplies an all-dimensional leaf-exchange argument: an edge where the hub color changes permits relocating one leaf relative to the hub crossing to force the opposite monotone orientation. The next natural goal is to generalize such synchronization from stars to arbitrary interaction trees.

### Stronger theorem: paired roots in every hub fiber, without symmetry

**Theorem 3 (sharp fiberwise star theorem).** Under the star coloring hypotheses of Theorem 1, for every leaf configuration \(x\in Q_L\),
\[
\boxed{(x,0)\in P(f)\quad\text{or}\quad(x,1)\in P(f).}
\tag{3}
\]
Consequently \(|P(f)|\ge2^{d-1}\). This bound holds for arbitrary hub function \(b\), with no antipodal symmetry assumption, and is sharp even when the interaction star is connected.

*Proof.* Fix \(x\), and put \(q=b(x)\). Choose the leaf subset
\[
S=\{i\in L:a_i(0)=1-q\},\qquad y=x\oplus\bigoplus_{i\in S}e_i.
\tag{4}
\]
Set the starting hub bit to \(s=0\) when \(b(y)=1-q\), and to \(s=1\) when \(b(y)=q\).

We construct the two required monotone color words from root \((x,s)\).

The orientation beginning with color \(q\) is always obtained by traversing the hub direction first (color \(b(x)=q\)), followed by all leaf directions sorted by their post-hub colors \(a_i(1-s)\): increasing if \(q=0\), decreasing if \(q=1\). The full word has form \(q^*(1-q)^*\).

For the opposite orientation \((1-q)^*q^*\), distinguish the two choices of \(s\).

If \(s=0\), take all leaves of \(S\) first. By (4), their colors \(a_i(0)=1-q\); the hub crossing at \(y\) also has color \(b(y)=1-q\). Afterwards traverse the remaining leaves sorted toward final color \(q\). Thus the full word is \((1-q)^*q^*\).

If \(s=1\), first traverse the leaves in \(S\), sorted toward color \(q\), using their pre-hub colors \(a_i(1)\). Cross the hub at \(y\), where its color is \(b(y)=q\). Traverse the remaining leaves, whose post-hub colors are \(a_i(0)=q\), in any order. Again the full word has form \((1-q)^*q^*\).

Hence \((x,s)\) is a paired root. Every step uses a distinct direction. Since \(x\) was arbitrary, each hub fiber contains a paired root, proving (3).

For sharpness, take the product of the two-dimensional square coloring \(h\) from the Cartesian factorization theorem, which has two paired roots among four, with a one-direction monochromatic factor for every further dimension. This is a star-interaction coloring and its paired-root count is \(2^{d-1}\). To make the interaction star connected, one may instead take center color \(b(x)=0\) and leaf colors \(a_i(s)=s\) for every \(i\in L\). Then every leaf interacts with the hub, while direct evaluation of the two orientations shows precisely one of the two hub bits is paired for each leaf configuration, again attaining \(2^{d-1}\). QED.

**Corollary 4 (one-bit constructive selector).** A paired root can be found from any prescribed leaf configuration using one evaluation of \(b(x)\), one evaluation of \(b(y)\), and the list of leaf colors \(a_i(0),a_i(1)\). No search over permutations or over the full coloring space is required.

**Toward closure.** The star theorem now supplies a fiberwise lower bound of one half with arbitrarily many interacting directions. A leaf-elimination induction on more general interaction trees would be especially valuable if it preserved this fiberwise property on an appropriate separator.### Sharp favorable-root fractions for nonlinear star colorings

Let \(f\) be a coloring of \(Q_d\) with star interaction graph and central direction \(c\). Denote by \(A_0(f)\) and \(A_1(f)\) roots with full monotone words \(0^*1^*\) and \(1^*0^*\).

**Theorem 5.**
\[
\boxed{|A_0(f)|,\ |A_1(f)|\ge3\cdot2^{d-2}.}
\tag{5}
\]
The bounds are sharp, without any symmetry assumption on the central edge-color function.

*Proof.* Partition roots into four-element blocks \(\{(x,0),(x,1),(\bar x,0),(\bar x,1)\}\). If the center-edge colors satisfy \(b(x)=b(\bar x)\), Theorem 1 shows all four roots are paired.

Otherwise one of \(x,\bar x\) has center color zero; placing the center direction first gives a nondecreasing path from both roots over that configuration. The other has center color one; placing center first gives a nonincreasing path from both of those roots. The fiberwise Theorem 3 guarantees at least one paired root above *each* configuration. Hence each four-root block contributes at least three roots to each orientation's favorable set. There are \(2^{d-2}\) blocks.

For equality, take the Cartesian product of the extremal colored square \(h\), with three favorable roots in each orientation, and a monochromatic factor for every remaining direction. QED.

**Corollary 6 (two independent star colorings).** Suppose arbitrary colorings \(f,g\) of \(Q_d\) each have star interaction graphs, possibly with different hub directions and unrelated nonlinear edge functions. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{d-1}.}
\tag{6}
\]
This follows from the preceding lower bounds by inclusion-exclusion. It verifies the stronger two-coloring favorable-root intersection statement for two unrelated stars in all dimensions.

**Scope.** The interaction-star assumption is essential to the present proof; no claim is made for general interaction graphs.### Erratum: connected-star sharpness

The earlier constant-hub example following Theorem 3 does not attain the stated half-root bound: it has paired roots everywhere.

A valid connected-star extremizer is
\[
b(x)=x_j,\qquad a_i(s)=1-s\quad(i\in L),
\]
where (j\in L) is one selected leaf. Every leaf interacts with the center. Fix any leaf configuration (x), and consider initial center bit (s=1-x_j). Every leaf step before the center has color (x_j), every leaf step after the center has color (1-x_j), and the center edge has color (x_j) when leaf (j) precedes it, and (1-x_j) when leaf (j) follows it. Consequently every full geodesic from that root has both colors and the single monotone orientation (x_j^*(1-x_j)^*). No geodesic realizes the opposite orientation, so this root is unpaired. The fiberwise theorem guarantees the other root ((x,x_j)) is paired. Thus every hub fiber has one paired root, and the lower bound \(|P(f)|=2^{d-1}\) is attained with connected interaction graph. This corrects only the equality example; preceding theorems are unaffected.

### Star forests and interaction-prime reduction

**Corollary 7 (quantitative star-forest theorem).** Suppose the interaction graph \(\Gamma(f)\) is a disjoint union of components, each either isolated or a star. Let \(c\) denote the number of nontrivial components (those containing at least two dimensions). Then
\[
\boxed{|P(f)|\ge2^{d-c}.}
\tag{8}
\]
The bound is sharp for every such component-size partition.

*Proof.* By the Cartesian factorization theorem, \(f\) is the product of its component colorings, and \(P(f)\) is the Cartesian product of their paired-root sets. An isolated direction, whose edge color is constant, has both roots paired. A nontrivial star component of dimension \(m\) has at least \(2^{m-1}\) paired roots by Theorem 3. Multiplication over components gives \(2^{d-c}\). Equality follows by using the connected-star extremizer \(b(x)=x_j,\ a_i(s)=1-s\) in every nontrivial component and any constant edge color in the isolated components. QED.

**Corollary 8 (star-or-small reduction for potential counterexamples).** Suppose every connected component of \(\Gamma(f)\) is either a star or has at most four dimensions. Then \(P(f)\ne\varnothing\). Consequently any hypothetical paired-root-free coloring has an interaction component of size at least five that is not a star; in particular a minimum-dimension counterexample must have a connected, non-star interaction graph on at least five directions.

*Proof.* Star components have paired roots by Theorem 1. Every coloring on at most four dimensions has a paired root by the previously established finite-dimensional paired-root theorem. Apply Cartesian factorization of \(P(f)\). QED.

**Corollary 9 (independent star factors and two-coloring cross-intersection).** Suppose \(f\) and \(g\) share a decomposition of their dimension set into \(c\) nontrivial component blocks and any number of singleton blocks, such that on each nontrivial block both factor colorings have star interaction graphs, with their hubs and edge rules allowed to differ. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge2^{d-c}.}
\tag{9}
\]
This follows from the product factorization and Corollary 6 applied independently on every component, while a singleton factor permits either monotone orientation at both roots.

**Proof-search consequence.** Arbitrarily large interaction systems assembled from nonlinear hubs cannot obstruct NORI1. The first interaction-graph shapes outside this theorem arise by connecting hubs together or introducing cycles. Establishing a similar root-selector property for an interaction tree with two adjacent hubs would extend the theorem from star forests toward arbitrary forests, while retaining the same dimension-simple path geometry.### Free-bridge NORI1 closure and abundance

**Corollary 10 (odd cube colorings with star lower facet).** Let \(n=d+1\ge3\). Suppose the undirected edges of \(Q_n=Q_d\times\{0,1\}\) are colored antipodally oddly, and the induced coloring \(f\) on its lower \(Q_d\) facet has a star interaction graph. The vertical bridge colors are unrestricted except for antipodal oddness. Then there are at least
\[
\boxed{2^{n-2}}
\]
distinct directed monochromatic full antipodal geodesics oriented from the lower facet to the upper facet.

*Proof.* Every such odd coloring is the universal bridge extension \(C(f,h)\) of the earlier paired-root Subsection, where \(h(\bar z)=1-h(z)\). The bridge equivalence assigns to every paired root \(z\in P(f)\) a monochromatic full antipodal geodesic whose unique vertical step uses the bridge at \(z\). Theorem 3 proves \(|P(f)|\ge2^{d-1}=2^{n-2}\). Paths coming from different roots \(z\) traverse different vertical bridges, so they are distinct. QED.

**Corollary 11 (star-forest extension).** If the lower-facet interaction graph is a disjoint union of stars with \(c\) nontrivial components, the same argument gives at least \(2^{d-c}\) distinct directed monochromatic full antipodal geodesics.

This closes an all-dimensional class of NORI1 instances with nonlinear hub functions and unrestricted odd bridge assignments. It makes no claim about unrestricted facets or the boundary tournament conjecture.

### A linear-query monochromatic-path algorithm for star facets

**Theorem 12 (constructive oracle bound).** Given an antipodally odd coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) whose lower facet has star interaction graph with known hub direction, one can construct a monochromatic full antipodal geodesic with \(O(d)\) color queries and \(O(d)\) elementary operations. The vertical bridge colors remain arbitrary subject to oddness.

*Proof.* Fix any leaf configuration \(x\), for example the all-zero string. Read the leaf edge colors \(a_i(0),a_i(1)\) for every leaf direction \(i\), and read the lower-facet hub color \(q=b(x)\). Form
\[
S=\{i:a_i(0)=1-q\},\qquad y=x\oplus\bigoplus_{i\in S}e_i.
\]
Read the hub-edge color \(b(y)\), and set the starting hub bit \(s=0\) if \(b(y)=1-q\), otherwise \(s=1\). Theorem 3 explicitly constructs from \(z=(x,s)\) a full lower-facet path \(P_q\) of word \(q^*(1-q)^*\) and a full path \(P_{1-q}\) of word \((1-q)^*q^*\). Both are obtained by sorting leaf directions into their two color classes and positioning the hub first or between those classes, without any path search.

Read the vertical bridge color \(h(z)\) in \(Q_{d+1}\), and choose the lower-facet witness \(P_{h(z)}\). Write its vertices as \(z=z_0,z_1,\ldots,z_d=\bar z\), with color change after edge \(k\), and let \(w=z_k\). Construct a full geodesic starting at lower vertex \((w,0)\): first traverse the prefix of \(P\) in reverse from \(w\) to \(z\), then use the vertical bridge at \(z\), then traverse in the upper facet the antipodal image of the suffix of \(P\), reversed, from \(z\) to \(\bar w\). Its lower edges have color \(h(z)\), its vertical edge also has color \(h(z)\), and its upper edges have color \(1-(1-h(z))=h(z)\) by antipodal oddness. Its horizontal directions are the disjoint dimension sets from the original prefix and suffix, and the new vertical dimension is used once. Therefore the resulting path is dimension-simple, monochromatic, and antipodal, as claimed. QED.

The query bound uses at most \(2(d-1)+3\) lower/vertical edge-color evaluations, with constant-work sorting into two binary color classes. The hub-direction identity may be part of the input promise; discovering it from a completely unrestricted black-box coloring is a separate task.

## Uniform Hamming robustness of nonlinear star selectors

For any binary edge coloring \(f\) of \(Q_d\), write \(P(f)\) for the paired-root set. The star selector of Theorem 3 chooses one paired root \(z(x)=(x,s(x))\) above each leaf configuration \(x\in Q_{d-1}\), and constructs two full geodesics from that same root, of color words \(0^*1^*\) and \(1^*0^*\).

**Lemma 13 (fixed-order edge incidence).** Fix a permutation \(\pi\) of the \(d\) cube directions. Every undirected cube edge \(e\) belongs to precisely two full directed antipodal geodesics \(P(z,\pi)\), as the root \(z\) ranges over \(Q_d\).

*Proof.* Let \(i\) be the direction of \(e\), and let \(S\) be the set of directions preceding \(i\) in \(\pi\). The direction-\(i\) step of the path rooted at \(z\) joins \(z\oplus S\) to \(z\oplus S\oplus e_i\). It equals the prescribed undirected edge \(e\) for precisely the two values of \(z\) obtained by translating the two endpoints of \(e\) by \(S\). QED.

**Lemma 14 (bounded permutation certificate).** For every star-interaction coloring \(f\), the \(2^{{d-1}}\) distinct paired roots \(z(x)\) furnished by the fiberwise selector have orientation witnesses drawn from at most **eight fixed permutations** of the \(d\) directions, independently of the hub function and of \(d\).

*Proof.* Recall the explicit algorithm of Theorem 3. For each leaf configuration \(x\), put \(q=b(x)\), define \(S(q)=\{i:a_i(0)=1-q\}\), and select \(s\in\{0,1\}\) from the hub-color value \(b(x\oplus S(q))\). The witness of word \(q^*(1-q)^*\) places the hub first and sorts the remaining leaf directions by their post-hub colors \(a_i(1-s)\). The witness of word \((1-q)^*q^*\) has a fixed ordering of \(S(q)\) before the hub and its complement afterward, with the two groups sorted by their known leaf colors as required. Once the pair \((q,s)\in\{0,1\}^2\) is specified, **both direction orders are fixed**, independently of \(x\). Thus four values of \((q,s)\) produce at most eight dimension orders. QED.

**Theorem 15 (Hamming stability around arbitrary stars).** Let \(f\) be any binary coloring of \(Q_d\) whose interaction graph is a star, with arbitrary nonlinear hub-edge colors. Let \(g\) differ from \(f\) on \(k\) undirected edges. Then
\[
\boxed{|P(g)|\ge\max\{0,\ 2^{d-1}-16k\}.}
\tag{11}
\]
In particular, when \(k<2^{d-5}\), the coloring \(g\) has a paired root.

*Proof.* Choose the \(2^{d-1}\) pairwise distinct roots \(z(x)\) and their two star-selector witness paths. Theorem 3 certifies both monotone orientations for \(f\) at every selected root. Under recoloring \(k\) edges, a selected root remains paired for \(g\) if neither of its witness paths contains a changed edge. By Lemmas 13-14, a prescribed changed edge belongs to at most \(2\cdot8=16\) of the witness paths indexed by all selected roots. It can therefore invalidate at most 16 root certificates. The union bound over \(k\) changed edges leaves at least \(2^{d-1}-16k\) unaffected roots, proving (11). QED.

**Corollary 16 (stability of NORI1 over star-like facets).** Let an antipodally odd coloring of \(Q_{d+1}=Q_d\times\{0,1\}\) have lower-facet coloring \(g\) at Hamming distance \(k\) from some star-interaction coloring \(f\) of \(Q_d\). The vertical bridge colors are arbitrary subject to oddness. Then at least
\[
\boxed{\max\{0,\,2^{d-1}-16k\}}
\tag{12}
\]
distinct directed monochromatic dimension-simple antipodal geodesics, oriented from the lower to the upper facet, exist.

*Proof.* Apply Theorem 15 to \(g\) and invoke the universal free-bridge correspondence for each surviving paired root, as in Corollary 10. Distinct paired roots correspond to distinct vertical bridges and hence distinct full geodesics. QED.

**Prospective closure use.** Minimal hypothetical paired-root-free colorings must be separated by at least \(2^{d-5}\) edge changes from every star interaction coloring. This extends the earlier Hamming obstruction around direction-uniform templates to arbitrarily nonlinear hub functions. It does not yet prove that a critical bad coloring lies near a star, but yields a uniform stability barrier should a structural reduction or interaction-tree decomposition produce such proximity.### Six-order witnesses and robust cross-favorability near stars

**Lemma 17 (six-order orientation certificates).** For every binary coloring \(f\) of \(Q_d\) whose interaction graph is a star, there are at least \(3\cdot2^{d-2}\) roots with \(0^*1^*\) full geodesics whose dimension orders belong to a fixed family of at most six permutations. The same holds for \(1^*0^*\).

*Proof.* Write a root as \((x,s)\), where \(x\) comprises all leaf bits and \(s\) the hub bit. Partition the roots into four-element groups over antipodal leaf pairs \(\{x,\bar x\}\).

If \(b(x)=b(\bar x)=0\), all four roots have \(0^*1^*\) paths obtained by hub first and leaves sorted by their post-hub colors. If both hub colors are one, all four have \(0^*1^*\) paths obtained by hub last and leaves sorted by their pre-hub colors. If the hub colors differ, the two roots over the zero-colored leaf configuration have hub-first \(0^*1^*\) paths, and the star fiberwise selector supplies at least one root over the one-colored configuration with a \(0^*1^*\) path. In every group at least three roots are thus certified.

The three possible path constructions have respectively two dimension orders, one for each starting hub bit: hub first with leaves ascending; hub last with leaves ascending; and the \(q=1\) selector's opposite-orientation path as in Theorem 3. For each fixed construction and starting hub bit the order of the leaf dimensions depends only on the given star's functions \(a_i(0),a_i(1)\), not on \(x\). Hence at most six permutations suffice. Interchanging the two colors proves the other orientation. QED.

**Theorem 18 (favorable-root stability around any star).** If a coloring \(g\) differs from some star-interaction coloring of \(Q_d\) on \(k\) undirected edges, then
\[
\boxed{|A_0(g)|,\ |A_1(g)|\ge \max\{0,\ 3\cdot2^{d-2}-12k\}.}
\tag{13}
\]

*Proof.* Lemma 17 supplies at least \(3\cdot2^{d-2}\) rooted paths in each monotone orientation, drawn from six fixed dimension orders. For one given order, each undirected cube edge belongs to two rooted full geodesics, by Lemma 13. Each altered edge can therefore spoil at most twelve of the chosen certificates. Union bounding over \(k\) changed edges proves the inequalities. QED.

**Corollary 19 (robust cross-orientation intersection for unrelated stars).** Suppose \(g,h\) have respective Hamming distances \(k,\ell\) from two star-interaction colorings, whose hubs and edge-color rules need not agree. Then
\[
\boxed{|A_0(g)\cap A_1(h)|\ge\max\{0,\ 2^{d-1}-12(k+\ell)\}.}
\tag{14}
\]
In particular, the stronger two-coloring intersection conjecture holds whenever \(k+\ell<2^d/24\).

*Proof.* Apply Theorem 18 to the two colorings and use inclusion-exclusion in the \(2^d\) cube vertices. QED.

**Implication.** Abundant root certificates supported on finitely many dimension orders admit quantitative stability under arbitrary edge recoloring, even if the base coloring has nonlinear dependence on arbitrarily many leaf bits. Controlling the number of such orders under interaction-tree gluing is a possible induction target toward unrestricted paired-root existence.

## Transverse square-variation obstruction to paired-root failure

For an arbitrary cube-edge coloring \(f\) of \(Q_d\), let \(f_i(x)\) denote the color of the direction-\(i\) edge incident with \(x\). It is independent of \(x_i\). Define the directed square-influence
\[
I_{ij}(f)=\Pr_{x\in Q_d}[f_i(x)\ne f_i(x\oplus e_j)],\qquad i\ne j.
\]
For a designated potential hub \(c\in[d]\), set
\[
D_c(f)=\sum_{\substack{i,j\ne c\\i\ne j}}I_{ij}(f).
\tag{15}
\]
This records only square variation *among the leaves*, discarding every term incident with \(c\).

**Lemma 20 (projection onto a nonlinear star by leaf Poincare).** For every binary edge coloring \(f\) of \(Q_d\) and every proposed center \(c\), there exists a star-interaction coloring \(g\) with center \(c\), agreeing with \(f\) on every center-direction edge, such that
\[
\boxed{\operatorname{dist}(f,g)\le2^{d-2}D_c(f).}
\tag{16}
\]

*Proof.* Keep the center-direction edge colors \(g_c=f_c\), which may depend arbitrarily on every leaf bit. For each leaf direction \(i\ne c\) and each fixed hub bit \(s\in\{0,1\}\), choose \(g_i\) to be the majority color of \(f_i\) over all \(2^{d-2}\) undirected direction-\(i\) edges in the hub-\(s\) facet. This produces a star coloring: each \(g_i\) depends only on the hub bit.

Let \(p_{i,s}\) be the fraction of these leaf-direction edges colored one. The number of altered edges in this slice is \(2^{d-2}\min(p_{i,s},1-p_{i,s})\). The Boolean-cube Poincare inequality for the \(d-2\) leaf bits other than \(i,c\) gives
\[
p_{i,s}(1-p_{i,s})
\le\frac14\sum_{j\notin\{i,c\}}
\Pr[\partial_j f_i=1\mid x_c=s].
\]
Since \(\min(p,1-p)\le2p(1-p)\), summing over \(i\ne c\) and both hub bits yields
\[
\operatorname{dist}(f,g)
\le2^{d-3}\sum_{i\ne c}\sum_{j\notin\{i,c\}}\sum_{s=0}^1
\Pr[\partial_j f_i=1\mid x_c=s]
=2^{d-2}D_c(f).
\]
QED.

**Theorem 21 (transverse curvature sufficient condition).** Every arbitrary cube-edge coloring \(f\) satisfies
\[
\boxed{|P(f)|\ge\max\{0,\ 2^{d-1}(1-8D_c(f))\}}
\quad\text{for every }c\in[d].
\tag{17}
\]
In particular, if some \(c\) has \(D_c(f)<1/8\), then \(f\) has a paired root.

*Proof.* Let \(g\) be the star approximation from Lemma 20. Theorem 15 gives
\[
|P(f)|\ge2^{d-1}-16\operatorname{dist}(f,g)
\ge2^{d-1}-16\cdot2^{d-2}D_c(f)
=2^{d-1}(1-8D_c(f)).
\]
QED.

**Corollary 22 (hereditary spread of transverse interactions in every putative counterexample).** If \(P(f)=\varnothing\), then
\[
\boxed{\sum_{\substack{i,j\ne c\\i\ne j}}\Pr_x[\partial_j f_i(x)=1]\ge\tfrac18
\qquad\text{for every }c\in[d].}
\tag{18}
\]
Thus no dimension can serve as an approximate hub with total leaf-leaf square variation below \(1/8\), even if all \(d\) directions have nonuniform colors. Equivalently, every putative paired-root-free coloring is quantitatively separated in square-influence from the entire nonlinear star class.

**Closure interpretation.** The new obstruction is localized by *deleting one candidate hub* from the directed square-influence sum, rather than by counting global switch support. A proof that switch-criticality forces some dimension with \(D_c<1/8\) would establish NORI1 through the existing free-bridge equivalence. No such implication is presently known; arbitrary random colorings typically have much larger variation, so an induction must exploit the criticality or full-path witness geometry rather than treat (18) as an immediate contradiction.
