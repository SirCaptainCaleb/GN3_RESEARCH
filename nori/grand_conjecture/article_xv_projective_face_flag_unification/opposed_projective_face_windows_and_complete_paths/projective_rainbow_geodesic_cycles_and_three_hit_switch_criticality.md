# Projective rainbow geodesic cycles and three-hit switch criticality

# Projective rainbow geodesic cycles and three-hit switch criticality

Let \(H_n=L(Q_n)/A\) be the antipodal quotient of the line graph of **undirected** cube edges, \(n\ge3\). Its vertices represent antipodal cube-edge pairs, labeled by their cube directions, and its edges represent antipodal orbits of unoriented two-edge turns. Let \(\alpha\in H^1(H_n;\mathbb F_2)\) classify the double cover. Call a simple cycle \(C\) a *rainbow projective n-cycle* when it has length n, uses every dimension label once, and obeys \(\langle\alpha,[C]\rangle=1\).

**Theorem 1 (rainbow projective lifting).** Every rainbow projective n-cycle lifts to a dimension-simple antipodal geodesic of \(Q_n\). Conversely, every such geodesic projects to a rainbow projective n-cycle.

*Proof.* Lift a quotient cycle to a sequence \(e_1,\ldots,e_n,Ae_1\) of undirected cube edges, with each successive pair incident. The final edge meets the antipodal image \(Ae_1\) because the cover monodromy of the quotient cycle is one. Since consecutive directions differ, their incidence point is unique. Write \(q_i=e_i\cap e_{i+1}\) for \(1\le i<n\), \(q_n=e_n\cap Ae_1\), and \(q_0=Aq_n\in e_1\). For each i, \(q_{i-1}\) and \(q_i\) are points on cube edge \(e_i\); they are either identical or joined by that edge. Thus the sequence \(q_0,\ldots,q_n\) is a possibly stationary walk in which each dimension can be used at most once. However, \(q_n=Aq_0\) differs from \(q_0\) in every dimension. It follows that none of the n steps is stationary and all n dimensions are traversed. The sequence is a full antipodal geodesic.

Conversely a full antipodal geodesic with edge sequence \(e_1,\ldots,e_n\) has \(e_n\) incident with \(Ae_1\) at its endpoint. Therefore its quotient edge sequence closes with monodromy one; the distinct direction labels give a simple rainbow n-cycle. \(\square\)

**Theorem 2 (cyclic root rotation).** Let D be any subset of turn-orbits of \(H_n\), and let \(C(P)\) denote the rainbow projective cycle associated with a full antipodal geodesic P. The minimum switch count over its antipodal root rotations is
\[
\boxed{
\min_{P'\text{ a root rotation of }P}
|D\cap\operatorname{turns}(P')|
=
\max(0,|D\cap E(C(P))|-1).}
\tag{1}
\]

*Proof.* Start P at any intermediate vertex, first following its suffix and then the antipodal image of its prefix. The resulting walk remains a full geodesic, and its quotient turn sequence opens the same rainbow cycle at the selected turn. Every cycle turn can be chosen as the omitted turn, so the least number of marked turns equals the cycle's number of marked edges minus one if this number is positive, and zero otherwise. \(\square\)

For odd cube-edge colorings the realizable switch set S represents \(\alpha\), so \(|S\cap C|\) is odd on any rainbow projective n-cycle. Therefore NORI1 is equivalent to the one-hit cycle assertion
\[
\boxed{
\forall S,\ [\mathbf1_S]=\alpha,\quad
\exists\text{ rainbow projective n-cycle }C:
|S\cap C|=1.}
\tag{2}
\]
Using the hereditary switch-set theorem of the preceding subsection, it is also equivalent to
\[
\boxed{
\forall D\subseteq E(H_n),\
(\alpha+\ell)|_{H_n[D]}=0
\quad\Longrightarrow\quad
\exists\text{ rainbow projective n-cycle }C:
|D\cap C|\le2.}
\tag{3}
\]
Here \(\ell\) is the cycle-length-parity class.

**Theorem 3 (three-hit critical witnesses).** If (3) fails, choose an inclusion-minimal hereditary counterexample D. Then every rainbow projective n-cycle has at least three D-edges, and for every marked edge \(e\in D\) there exists a rainbow projective n-cycle \(C_e\) such that
\[
\boxed{e\in C_e,\qquad |D\cap C_e|=3.}
\tag{4}
\]

*Proof.* The first claim is the counterexample property. Deletion preserves the hereditary class; minimality means that \(D\setminus\{e\}\) permits a rainbow projective cycle with at most two hits. If this cycle avoided e, it would contradict the counterexample property for D. Thus it includes e, and its D-hit count is three. \(\square\)

**Scope and implications.** An arbitrary line-graph walk may execute an illegal transition by touching the middle edge twice at its same endpoint. The lift in Theorem 1 rules this out by using antipodal displacement and the one-use-per-dimension budget. This supplies a closed-cycle characterization that retains cube geodesicity and dimension-simplicity.

The common hereditary switch-class framework is not asserted to be a matroid. In the cube quotient, a triangle of turns among three cube edges meeting at one vertex has odd length and trivial cover monodromy. Hence the signed-graph restriction forbids D from containing all three turns. A minimal counterexample must simultaneously satisfy these local exclusions and cover every marked turn by a three-hit rainbow cycle. Exploiting the exchange and overlap geometry of those cycles is the next proof objective. Neither the lift theorem nor criticality proves NORI1.

## Uniform rainbow-cycle incidence and switch-density rigidity

The rainbow projective cycles admit a uniform incidence count that imposes numerical constraints on all hereditary switch obstructions.

**Theorem 4 (rainbow cycle census).** For every \(n\ge3\), the antipodal quotient line graph \(H_n=L(Q_n)/A\) has
\[
\boxed{|V(H_n)|=n\,2^{n-2},\qquad
|E(H_n)|=n(n-1)\,2^{n-2},}
\tag{5}
\]
and its number of undirected covering-odd, direction-rainbow n-cycles is
\[
\boxed{|\mathcal C_n|=2^{n-2}(n-1)!.}
\tag{6}
\]
Every turn-orbit of \(H_n\) lies on precisely
\[
\boxed{(n-2)!}
\tag{7}
\]
of these cycles.

*Proof.* The cube has \(n2^{n-1}\) undirected edges, paired by antipodality, giving the quotient vertex count. Each quotient state has \(2(n-1)\) turn neighbors, giving the edge count by the degree-sum rule.

There are \(2^n n!\) rooted directed full cube geodesics, one per root and direction permutation. By the lifting theorem, each undirected rainbow projective cycle yields \(2n\) distinct cyclically placed, oriented quotient edge sequences (n possible starts and two traversal directions). Every such quotient sequence has two antipodal lifts, giving \(4n\) rooted full geodesics per projective cycle. Dividing \(2^n n!\) by \(4n\) yields (6). The cube automorphism group acts transitively on turn-orbits and preserves the rainbow cycle family. Counting cycle-turn incidences gives the common turn multiplicity
\[
\frac{n|\mathcal C_n|}{|E(H_n)|}
=\frac{n2^{n-2}(n-1)!}{n(n-1)2^{n-2}}
=(n-2)!.
\]
\(\square\)

**Theorem 5 (critical switch-density lower bound).** If a hereditary set \(D\in\mathfrak H_\alpha\) meets *every* rainbow projective n-cycle in at least three turns, then
\[
\boxed{|D|\ge 3(n-1)2^{n-2}.}
\tag{8}
\]
This is three times the size of a quotient state's degree-one star multiplied by a factor of \(2^{n-3}\); more intrinsically, D occupies at least \(3/n\) of all quotient turn-orbits. The inequality applies in particular to every hypothetical deletion-minimal NORI1 counterexample D.

*Proof.* Count pairs \((e,C)\) with \(e\in D\cap C\). Each \(e\in D\) lies on \((n-2)!\) rainbow cycles by (7), while each rainbow cycle supplies at least three such pairs. Hence
\[
(n-2)!|D|\ge3|\mathcal C_n|
=3\,2^{n-2}(n-1)!,
\]
giving (8). \(\square\)

**Theorem 6 (local bipartite upper bound).** Every hereditary \(D\in\mathfrak H_\alpha\) satisfies
\[
\boxed{|D|\le 2^{n-1}\left\lfloor\frac{n^2}{4}\right\rfloor.}
\tag{9}
\]
Every legal odd switch set S obeys the same inequality. Equality requires that, at every antipodal pair of cube vertices, the marked turn graph on the n incident dimension edges be a complete bipartite graph with the two parts as balanced as possible.

*Proof.* At a cube vertex v, its n incident undirected edges form a clique \(K_n\) of turn edges in the line graph. The antipodal clique supplies the paired turn orbits. Every cycle in this clique lifts closed, so the covering class \(\alpha\) vanishes on it. The hereditary condition \((\alpha+\ell)|_{H_n[D]}=0\) thus requires the graph of marked turns within the clique to have only even cycles; in other words that local marked graph is bipartite. A bipartite graph on n vertices has at most \(\lfloor n^2/4\rfloor\) edges, with equality only for the balanced complete bipartite graph. Each quotient turn edge belongs to one antipodal pair of cube-vertex cliques, and there are \(2^{n-1}\) such pairs. Summing proves (9). \(\square\)

**Corollary 7 (all-dimensional mean switch bound and extremal rigidity).** For a uniformly random undirected rainbow projective cycle \(C\),
\[
\boxed{
\mathbb E|D\cap C|=\frac{|D|}{(n-1)2^{n-2}}
\le\frac{2\lfloor n^2/4\rfloor}{n-1}.}
\tag{10}
\]
Thus if \(2\lfloor n^2/4\rfloor<3(n-1)\), the hereditary two-hit conjecture follows without further work; this includes \(n=3,4\).

For \(n=5\), the upper bound in (9) and lower bound in (8) coincide. Any hypothetical hereditary counterexample must therefore be a **realizable** switch set S whose incident-edge colors split in sizes two and three at every cube vertex, and every rainbow projective 5-cycle must have three marked turns.

*Proof.* The expectation is the cycle-incidence census divided by the number of cycles. Apply (9). In dimension five, both inequalities read \(|D|=96\). The local inequality is therefore saturated at every cube-vertex orbit. Since D is a subset of some realizable legal switch set S and S satisfies the same local upper bound, S must coincide with D on every turn. Every rainbow 5-cycle has at least three hits, and the mean in (10) is three; therefore all such cycles have three hits. \(\square\)

**Research meaning.** The lower and upper density constraints force a substantial spread of marked turns in a critical hereditary obstruction. Local balance is stronger than merely forbidding fully marked incidence triangles: the entire marked graph at each cube vertex must be bipartite. The low-dimensional consequences are consistency checks, not a proposed approach of exhaustive small-order analysis. In higher dimensions, the still-open issue is to exploit the global compatibility of these local bipartitions with the forced three-hit cycles.

## Uniform near-monochromatic antipodal geodesics from the rainbow census

The incidence identity above yields an all-dimensional bound for every legal antipodally odd cube-edge coloring without requiring a topological chain transfer.

Let \(c\) be a legal coloring, and let \(S=S(c)\subseteq E(H_n)\) be its quotient switch set. At a cube vertex v, let \(a(v)\) be the number of color-one edges among the n incident cube edges. Then the number of switched unoriented turns based at v is \(a(v)(n-a(v))\). Antipodality sends \(a(v)\) to \(n-a(v)\), so each antipodal vertex pair contributes this same number to \(|S|\).

**Theorem 8 (mean projective switches and a universal even-switch bound).** For every legal odd coloring of \(Q_n\), \(n\ge3\),
\[
\boxed{\mathbb E_{C\in\mathcal C_n}|S\cap C|
=\frac1{(n-1)2^{n-1}}\sum_{v\in Q_n}a(v)(n-a(v))
\le\frac{2\lfloor n^2/4\rfloor}{n-1}.}
\tag{11}
\]
Every projective rainbow cycle has an odd number of S-edges. Consequently some full dimension-simple antipodal geodesic has at most
\[
\boxed{2\left\lfloor\frac{n-1}{4}\right\rfloor}
\tag{12}
\]
ordinary color switches.

*Proof.* Each turn orbit lies on \((n-2)!\) cycles by Theorem 4, so the expected S-hit count is \(|S|/((n-1)2^{n-2})\). Summing the local complete-bipartite turn counts gives \(|S|=\tfrac12\sum_v a(v)(n-a(v))\), and establishes (11). Every rainbow cycle evaluates \(\alpha\) to one, so its S-hit count is odd. Let \(h=2\lfloor(n-1)/4\rfloor+1\). Directly evaluating the displayed upper bound in each residue class of n modulo four shows it is strictly less than \(h+2\). If every rainbow cycle had at least \(h+2\) hits, its mean would violate (11). Thus some cycle has at most h odd hits. Root rotation deletes one marked turn, yielding a complete geodesic with at most \(h-1\) ordinary switches, which is (12). \(\square\)

**Corollary 9 (local imbalance improves the bound in dimensions \(4k+1\)).** Let \(n=4k+1\ge5\). If at least one cube vertex has other than \(2k\) or \(2k+1\) incident edges of color one, then there is a full antipodal geodesic with at most \(2k-2\) color switches. If an odd coloring in dimension \(4k+1\) has no geodesic with at most \(2k-2\) switches, then every vertex must have a locally balanced split \(2k\) versus \(2k+1\), and every rainbow projective cycle has \(2k+1\) switched turns.

*Proof.* In these dimensions, the right side of (11) equals \(2k+1\), an odd integer. Strict local imbalance reduces its mean below \(2k+1\); since every cycle count is odd, some cycle has at most \(2k-1\) hits, and root rotation gives the improved path. Conversely absence of such a path forces every cycle to have at least \(2k+1\) hits, so mean equality holds, implying equality in the local inequality at every vertex and equality of every cycle hit count with \(2k+1\). \(\square\)

The estimate applies only to realized odd switch sets, where the projective hit parity is odd. A hereditary subset D of a realizable switch set need not preserve this oddness; its universal mean and density estimates are instead Theorems 5–7. The strengthened result pinpoints a potential obstruction to improving average switch bounds: in dimensions \(4k+1\), only everywhere-balanced colorings can saturate the mean limit.

## Adjacent-exchange traps in rainbow projective cycles

**Theorem.** For every \(n\ge9\), an antipodally odd coloring of \(Q_n\) can have a three-switch projective rainbow geodesic cycle C for which every cyclic adjacent-dimension exchange produces a five-switch cycle. The coloring may also have a monochromatic full antipodal geodesic.

*Proof.* On the standard geodesic rooted at the zero vertex, with dimension order \(1,\ldots,n\), assign successive edge colors \(0001110^{n-6}\). The projective closing turn compares the final edge to the antipode of the first. Its only three switched turns lie after positions \(3,6,n\), separated cyclically by distances \(3,n-6,3\). Every three-turn window contains at most one switch.

Swapping two cyclically adjacent dimension edges changes just the three turns entering, between, and leaving the two-edge square route. Its parity is fixed by the colors a,b of the unchanged outer edges. If a=b, prescribe the alternate pair of square-edge colors as \((1-a,1-a)\), changing zero switches to two; if a differs from b, prescribe \((1-a,a)\), changing one switch to three. Every cyclic adjacent exchange thus adds two switches.

The n squares have distinct unordered direction pairs \(\{1,2\},\ldots,\{n-1,n\},\{n,1\}\). Their two alternate edges each are distinct from the standard path and the other alternate edges. No two specified edge orbits coincide under antipodality: opposite squares preserve the direction pair but are disjoint from the corresponding prescribed square for \(n\ge9\). The 3n edge-orbit prescriptions are consistent with antipodal oddness and extend freely to all other orbits.

There are \(n2^{n-2}\) antipodal orbits of cube edges. A uniformly random rooted full geodesic has n edges each marginally uniform on these orbits. Its expected number of encounters with the 3n prescribed orbits is \(3n/2^{n-2}<1\). Therefore some full geodesic misses them all. Color this additional geodesic monochromatically, enforce complementary antipodal colors, and fill remaining orbits arbitrarily. This preserves the frozen three-hit cycle. \(\square\)

**Implication.** The three-hit sublevel graph under cyclic adjacent exchanges may have isolated vertices even when a one-hit rainbow cycle exists elsewhere. Consequently neither one-step descent nor monotone three-hit plateau connectivity is a valid unconditional NORI1 proof mechanism. A critical-set closure argument must exploit relations among multiple tight witness cycles or allow temporary increases to five switches.

The construction extends to odd \(t\ge3\) when \(n\ge3t\), using t cyclic switches spaced at least three apart; every adjacent exchange can be prescribed to raise the switch count from t to t+2.

## Dimension-parity barrier for linear witness-cycle closure

Let \(H_n=L(Q_n)/A\) be the antipodal quotient line graph of undirected cube edges. Let \(\alpha\) be its covering class, let \(\ell\) be the class evaluating a cycle by its length modulo two, and put \(\beta=\alpha+\ell\). Let \(\mathcal C_n\) denote the covering-odd, dimension-rainbow projective n-cycles.

**Theorem (character separation).** Every \(C\in\mathcal C_n\) satisfies
\[
\boxed{\alpha(C)=1,\quad\ell(C)=n\bmod2,\quad
\beta(C)=n+1\bmod2.}
\tag{16}
\]
Every triangle T formed by three incident cube edges at one cube vertex satisfies \(\alpha(T)=0\), \(\ell(T)=1\), and \(\beta(T)=1\). Therefore:
- for odd n, the binary cycle-space span of the projective rainbow cycles lies in the proper hyperplane \(\ker\beta\), and a star triangle witnesses that the inclusion is strict;
- for even n, their span lies in the proper hyperplane \(\ker\ell\), again excluding each star triangle.

*Proof.* By definition a rainbow projective n-cycle has covering monodromy one and has n edges. A star triangle lifts to two closed triangles based at antipodal cube vertices, so its covering monodromy is zero, while its length is three. Linear extension to cycle-space spans gives the two separation statements. \(\square\)

**Corollary (necessary odd triangle flux for odd-dimensional linear certificates).** If n is odd, any binary sum of rainbow projective n-cycles and their adjacent-exchange symmetric differences evaluates to zero under \(\beta\). Thus no such sum alone can furnish a \(\beta\)-odd cycle supported inside a candidate hereditary switch set D. A contradiction to the hereditary criterion \(\beta|_{H[D]}=0\) must use at least one additional cycle with nonzero \(\beta\), such as a star triangle, or a nonlinear operation not captured by these binary cycle sums.

The local star triangles are therefore not merely a nuisance of the line-graph encoding: they represent homological information invisible to dimension-rainbow projective cycles in the sparse *odd* dimensions targeted by the Grassmannian proof program. A promising closure route must couple tight three-hit cycles to triangle-containing exchange chains and force their unmarked parts to cancel. This is a necessary structural observation, not a construction of the required certificate.

## Projective turn cycles are generated by rainbow cycles and star triangles

For \(n\ge3\), let \(G_n=Q_n/A\) and \(H_n=L(Q_n)/A\). Since G_n is simple, the quotient turn graph satisfies \(H_n\cong L(G_n)\).

**Theorem.** There is a short sequence of binary cycle spaces
\[
\boxed{0\to \bigoplus_{v\in V(G_n)}Z_1(K_n(v))
\to Z_1(H_n)\to Z_1(G_n)\to0,}
\]
where \(K_n(v)\) is the clique of the n edges incident with projective vertex v. The kernel has dimension \((n-1)(n-2)2^{n-2}\) and is spanned by local star triangles. Since the preceding Article XV Petrie theorem shows that full dimension-simple projective n-cycles span \(Z_1(G_n)\), it follows that **projective rainbow n-cycles and local star triangles together span \(Z_1(H_n)\)**.

*Proof.* Fill each star clique of H_n by a simplex. Distinct star simplices intersect in one vertex precisely when their centers in G_n are adjacent, and triple intersections are empty. Their nerve is G_n, hence their union has its homotopy type. Filling star simplices kills precisely the triangle-generated subspace, giving the short sequence. Different star cliques have disjoint graph-edge sets, so their cycle spaces sum directly. There are \(2^{n-1}\) stars, each of cycle rank \((n-1)(n-2)/2\). Finally rainbow cycles map to the Petrie generators of the quotient graph, proving the spanning claim. \(\square\)

**Triangle-flux invariant.** Write \(\alpha\) for covering monodromy on H_n and \(\ell\) for cycle-length parity. Let \(\chi_n=\ell+(n\bmod2)\alpha\). Every rainbow n-cycle has \(\chi_n=0\), while every star triangle has \(\chi_n=1\). Hence the parity of the number of star triangles in any rainbow-plus-triangle decomposition is independent of the decomposition.

In odd dimensions, \(\chi_n=\alpha+\ell=\beta\), the hereditary switch class. Therefore a parity-based contradiction for an alleged hereditary three-hit obstruction must retain odd star-triangle flux after canceling every unmarked turn. The theorem gives the complete cycle-space generators, but not the constrained cancellation needed to close NORI1.

## Local flatness and a modulo-four switch improvement

Let c be an antipodally odd edge coloring of Q_n, n>=5, and let h(C) be the number of switched turns on a covering-odd dimension-rainbow projective n-cycle.

**Lemma.** If a cube vertex x has at least two incident edges of each color, there exist two rainbow cycles differing by one adjacent dimension exchange whose switch counts are different.

*Proof.* Select incident dimensions i,j of opposite colors. Among remaining dimensions select p,p' of opposite colors and a third q distinct from both; n>=5 assures this is possible. For r=p or p', start at x toggled in r, traverse r,i,j,q, then all other dimensions; compare with the geodesic exchanging i,j. Denote the two colored routes across the square at x by (u,v) and (u',v'), where u differs from u'. Let a_r be the incoming r-edge color and b the outgoing q-edge color. The total switch-count change is

Delta_r=([a_r !=u]-[a_r !=u'])+([u!=v]-[u'!=v'])+([v!=b]-[v'!=b]).

The last two differences do not depend on r. Since a_p and a_p' are opposite and u,u' are opposite, Delta_p-Delta_p' is either +2 or -2. Both changes cannot vanish. The projective closing turn is unchanged by the adjacent exchange. QED.

**Theorem.** If h(C) is constant over all rainbow projective n-cycles, then that constant equals one.

*Proof.* The lemma implies that every cube vertex has at most one incident edge of its minority color. If its zero/one incident counts are a,n-a, its switched incident turns number a(n-a)<=n-1. There are 2^(n-1) antipodal vertex orbits, so the quotient switch set has size at most (n-1)2^(n-1). The proven uniform cycle-incidence identity gives mean h=|S|/((n-1)2^(n-2))<=2. Each cycle has positive odd h because its monodromy evaluates to one. The common value is consequently one. QED.

**Corollary.** For n=4k+1, k>=1, every antipodally odd coloring has a full antipodal dimension-simple geodesic with at most 2k-2 ordinary color switches.

*Proof.* The mean projective switch bound is at most 2 floor(n*n/4)/(n-1)=2k+1. If no cycle had at most 2k-1 turns switched, every cycle (which has odd switch count) would have at least 2k+1, forcing h(C)=2k+1 for all cycles. The theorem contradicts this constant value. Hence some cycle has at most 2k-1 switched turns. Root rotation omits a switched turn, yielding a full geodesic with at most 2k-2 switches. QED.

This gives monochromatic closure at n=5 and bounds of two, four, and six switches at n=9,13,17. Unlike the earlier critical-cycle approach, the proof uses just one square, two predecessor colors, and uniform counting; it is uniform in dimension.

## Quantitative exchange activity from a single vertex

For a vertex x let a(x),b(x) count its incident zero- and one-colored edges, with a+b=n. Choose a uniform rooted full cube geodesic, let H be the number of switched turns of its projective completion, and let H' be the count after exchanging its second and third dimensions. Both marginal distributions are uniform on rainbow projective cycles.

**Theorem (local exchange variance).** For n>=5 define
[
p_n(a,b)=\frac{2ab\bigl[(a-1)\min(a-2,b-1)+(b-1)\min(a-1,b-2)\bigr]}
{n(n-1)(n-2)(n-3)}
]
for a,b>=2 and put p_n=0 otherwise. Then
[
\boxed{\operatorname{Var}(H)\ge 2^{-n}\sum_{x\in Q_n}p_n(a(x),b(x)).}
	ag{24}
]

*Proof.* The initial four dimensions of a random rooted full geodesic have ordered roles (r,i,j,q), all distinct. Its square exchange takes place at x after direction r. For i,j of opposite incident colors at x, the swap effect Delta_r differs by two between predecessor colors zero and one, regardless of the square's other edge colors and the outgoing color in direction q. Among the possible r of the two colors, at least the size of the smaller group therefore produces nonzero Delta. There are 2ab choices of ordered opposite-colored i,j. After these are chosen, there are a-1 directions of color zero and b-1 of color one available. For a zero-colored q, the remaining predecessor groups have sizes a-2,b-1, while for a one-colored q they have sizes a-1,b-2. Counting the forced nonzero swaps gives the stated lower fraction p_n(a,b) among all n(n-1)(n-2)(n-3) ordered role choices at x.

Every nonzero swap change has absolute value at least two by three-turn parity. Thus E[(H-H')^2]>=4 E_x p_n(a(x),b(x)). Because H and H' have the same distribution, E[(H-H')^2]<=4 Var(H), proving (24). QED.

**Corollary (polynomial abundance in the balanced worst case).** Let n=4k+1, k>=1. If every cube vertex has incident colors split 2k versus 2k+1, then
[
\boxed{\operatorname{Var}(H)\ge
\frac{4k^2-1}{16k^2-1}.}
	ag{25}
]
Moreover, the proportion of rainbow projective cycles with at most 2k-1 switched turns is at least
[
\boxed{\frac{4k^2-1}{8k^2(16k^2-1)}.}
	ag{26}
]
Every such cycle has a root rotation giving at most 2k-2 ordinary switches.

*Proof.* Substitute a=2k,b=2k+1 in (24). The fraction simplifies to (4k^2-1)/(16k^2-1). The projective switch count H is odd, supported on [1,4k+1], and its mean under the local balance assumption is 2k+1. Let t=Pr(H<2k+1). Write A=2k for the maximum downward deviation and B=2k for the maximum upward deviation. Positive and negative deviations have the same expectation m<=tA. Their squares are bounded by B and A times their absolute magnitudes, so Var(H)<=m(A+B)<=8k^2t. Combine with (25) to obtain (26). QED.

This quantifies, rather than merely asserts, the obstruction to uniform projective switch count in locally balanced colorings. It provides polynomially many near-monochromatic geodesics in the extremal balancing regime, without coordinating a family of critical witness cycles.

### A low-turn Petrie cycle gives a full rainbow forest with one antipodal joining cycle

Let \(c\) be a legal antipodally odd coloring of \(Q_n\), \(n\ge2\). Take a full antipodal geodesic \(P\) with word \(w\), and follow it by its antipodal translate. The resulting simple Petrie cycle has length \(2n\) and cyclic word \(w\bar w\). Put
\[
q=\operatorname{sw}(w)+[w_1=w_n].
\]
This positive odd integer is its projective turn grade.

**Theorem (single-cycle forest certificate).** The red edges of this Petrie cycle form a vertex-disjoint linear forest \(F\) with \(n\) edges, using every direction once, and with \(q\) nonempty path components. Its \(2q\) endpoints are closed under antipodality. Joining each endpoint to its antipode by an auxiliary link turns \(F\) into one simple cycle, containing \(n\) cube edges and \(q\) auxiliary links.

*Proof.* Every direction occurs twice on the Petrie cycle, on antipodal edges with opposite colors. Thus precisely one occurrence belongs to \(F\). The number of cyclic color changes is \(2q\), so there are \(q\) red runs and \(q\) blue runs, all nonempty. The red runs are vertex-disjoint paths. Their endpoints are precisely the color-change vertices, which antipodality permutes.

For connectedness after adding the links, index the alternating runs cyclically by \(0,\ldots,2q-1\), with the red runs at even indices. Antipodality advances by \(q\) runs: it preserves their cyclic order, exchanges their colors, and has square equal to a full turn. The link at the end of red run \(2j\) therefore reaches the start of red run \(2j+q+1\). On the \(q\) red components this is the permutation
\[
j\longmapsto j+(q+1)/2\pmod q.
\]
Since \(\gcd(q,(q+1)/2)=1\), it is one cycle. Internal forest vertices have degree two, and the matching of endpoints gives degree two at every other vertex. Thus the joined graph is one cycle, with \(n+q\) vertices and edges. \(\square\)

The auxiliary links represent antipodal pairs, and are not cube edges. For \(q=1\), the forest itself is a monochromatic full antipodal geodesic. For larger \(q\), the theorem keeps the complete direction set while identifying precisely the \(q\) antipodal joins that obstruct a single cube path.

**Corollary (Hollom-to-rainbow transfer).** Every legal odd coloring has such a forest with
\[
q\le(\pi/2+o(1))\sqrt n.
\]
Indeed Hollom's geodesic theorem supplies \(P\) with at most \((\pi/2+o(1))\sqrt n\) internal switches, and the projective correction is at most one. Thus the initial rainbow-forest stage is available in the cube with every direction represented and only a square-root number of components. No density assumption on a monochromatic component is used.

### Eulerian completion of the forest transitions

**Lemma (prescribed unoriented forest transitions).** In a finite undirected graph of even degree at every vertex, every specified linear forest can be oriented as a union of directed paths within some Eulerian orientation of the whole graph.

*Proof.* At each internal vertex of a forest path, pair its two incident forest edges. Extend these disjoint partial pairings to pair all incident edges at every vertex; the remaining number is even. The transition pairings decompose the graph's edges into closed trails. Orient each trail cyclically. Every prescribed pair consists of one entering and one leaving edge, so each forest path is coherently directed. Every vertex has equal indegree and outdegree. \(\square\)

For a perfectly balanced cube with \(4\mid n\), each monochromatic graph has even degree \(n/2\). The red forest in the preceding theorem can therefore be retained as directed paths in an Eulerian orientation of the red graph. The orientation of each component is selected by the completed transitions. The lemma does not prescribe those orientations independently, and does not orient the auxiliary antipodal joining cycle as a directed cycle. That compatibility remains part of a prospective absorption argument.

### A quantitative absorption target sufficient for unrestricted closure

The three methods now supply a common object: a full-direction monochromatic forest with \(O(\sqrt n)\) components, one antipodal joining cycle, and an Eulerian orientation preserving its path transitions in the balanced dimensions divisible by four. A sufficient missing statement is the following.

**Conditional absorption statement.** In perfectly balanced legal odd cubes of dimension divisible by four, any forest certificate above with \(q=O(\sqrt n)\) can be replaced by a monochromatic direction-simple path of length \(n-o(n)\), uniformly over the coloring and certificate.

For example, a bound on the lost directions of \(Aq(\log n)^B\), with fixed constants \(A,B\), would suffice. The replacement may change the root, directions used, and all forest edges; no local extension or prescribed-endpoint assertion is required.

**Proposition (this absorption statement closes NORI1).** The conditional statement implies unrestricted NORI1.

*Proof.* Let \(L(c)\) be the largest length of a monochromatic geodesic in \(c\), allowing partial direction sets. For legal odd colorings,
\[
L(c\boxtimes d)=L(c)+L(d).
\]
Projection of a monochromatic geodesic to either Cartesian factor is a monochromatic geodesic, proving the upper bound. Antipodal translation interchanges colors, so longest monochromatic factor paths can be chosen with the same color and concatenated, proving the lower bound. Therefore the deficit \(\Delta(c)=\dim(c)-L(c)\) is additive.

Suppose a perfectly balanced legal odd coloring \(c\) in dimension \(n_0\), divisible by four, were bad. Its deficit is an integer at least one. Its \(t\)-fold Cartesian power is perfectly balanced and has deficit \(t\Delta(c)\). Hollom supplies a forest certificate with \(O(\sqrt{tn_0})\) components in that power. The conditional absorption statement would give deficit \(o(tn_0)\), contradicting additivity as \(t\to\infty\). Thus all balanced colorings in these dimensions satisfy NORI1. The established counterexample-preserving complementary balancing extension, followed if necessary by a Cartesian square, transfers every hypothetical unrestricted counterexample to this class. \(\square\)

This is a sufficient closure target, not a proved absorption theorem. The available Eulerian orientation gives closed walks with reusable directions; the absorption statement must retain distinct directions. The APS random-direction reserve does not directly provide the needed connections, because a cube subgraph restricted to a proper direction subset splits into faces. The preceding formulation isolates the global joining problem while allowing sublinear loss, instead of requiring a single local repair to preserve every direction.

**Finite audit.** For every binary word of lengths two through nine, direct construction verified the odd grade, the number of red forest components, antipodal pairing of endpoints, and connectedness of the degree-two graph obtained by adding the links. The argument above proves these assertions in all dimensions.
