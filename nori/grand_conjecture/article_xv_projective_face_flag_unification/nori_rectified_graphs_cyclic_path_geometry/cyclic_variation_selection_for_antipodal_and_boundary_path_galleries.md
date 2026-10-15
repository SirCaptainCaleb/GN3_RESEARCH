# Cyclic variation selection for antipodal and boundary path galleries

# Cyclic variation selection for antipodal and boundary path galleries

The two motivating conjectures have a uniform *orbitwise* description in terms of cyclic binary variation, including their distinct periodicity and observation widths. This separates the elementary root-selection problem from the difficult problem of finding a favorable orbit.

Let \(L\ge2\), let \(\epsilon\in\mathbb F_2\), and take an infinite binary sequence \(a_j\) satisfying the twisted periodicity
\[
a_{j+L}=a_j+\epsilon.
\]
Its adjacent comparison bits
\[
\delta_j=a_j+a_{j+1}
\]
are ordinarily \(L\)-periodic. Write \(D=\sum_{j=0}^{L-1}\delta_j\), as an integer, and for \(1\le m\le L\) consider every length-\(m\) window \(W_t=(a_t,\ldots,a_{t+m-1})\).

**Theorem 1 (twisted cyclic-window switch selection).** For every such sequence,
\[
\boxed{
D\equiv\epsilon\pmod2,\qquad
\min_{0\le t<L}\operatorname{sw}(W_t)
=D-\max_{0\le t<L}\sum_{j=0}^{L-m}\delta_{t+j}.
}
\tag{1}
\]
The omitted comparison block has length \(q=L-m+1\). Therefore an orbit has a window with at most \(r\) switches if and only if it has a cyclic block of \(q\) comparisons containing at least \(D-r\) changes.

*Proof.* The XOR of the \(L\) successive comparisons telescopes to \(a_0+a_L=\epsilon\). Each length-\(m\) window contains \(m-1\) successive comparisons, so it omits \(L-(m-1)=q\) consecutive comparisons from one period. Its switch count is \(D\) minus the number of ones in the complementary block, proving (1). \(\square\)

## NORI1: antiperiodic cycles, one omitted comparison

For every freely rooted full cube geodesic \(P(x;\pi)\), the canonical root slide
\[
T(x;\pi_1,\ldots,\pi_n)=(x+e_{\pi_1};\pi_2,\ldots,\pi_n,\pi_1)
\]
shifts the true edge-color word by one bit and appends the complement of the first bit. Consequently the orbit's color sequence has \(L=m=n\), twist \(\epsilon=1\), and omitted-block size \(q=1\). Formula (1) becomes
\[
\boxed{D\text{ odd},\qquad
\min_{0\le t<n}\operatorname{sw}(P(T^t(x;\pi)))=D-1.}
\tag{2}
\]
Thus an orbit contains a monochromatic full geodesic if and only if \(D=1\); an at-most-one-switch full geodesic exists on the orbit if and only if \(D=1\) as well. This recovers the cyclic defect criterion of the earlier chiral-turn subsection without reference to a chosen chirality gauge.

## Boundary tournaments: periodic cycles, three omitted comparisons

Let \(n\ge4\) and let \(b(a,h,c)\) be an arbitrary reversal-odd boundary tournament. For a cyclic vertex order \((v_0,\ldots,v_{n-1})\), set
\[
a_j=b(v_j,v_{j+1},v_{j+2}),\quad j\in\mathbb Z/n\mathbb Z.
\tag{3}
\]
Every Hamilton order obtained by cyclic rotation reads \(m=n-2\) consecutive entries \(a_t,\ldots,a_{t+n-3}\). Thus \(L=n,\epsilon=0\), and \(q=3\). Let \(\delta_j=a_j+a_{j+1}\), and let \(D=\sum_j\delta_j\). Theorem 1 yields
\[
\boxed{
D\text{ even},\qquad
\min_{\text{cyclic rotations}}\operatorname{sw}
=D-\max_t(\delta_t+\delta_{t+1}+\delta_{t+2}).
}
\tag{4}
\]

**Corollary 2 (complete orbitwise boundary one-switch criterion).** A cyclic vertex order has a rotation giving an at-most-one-switch Hamilton tight path if and only if one of the following holds:
\[
\boxed{
D\le2,\qquad\text{or}\qquad
D=4\ \text{and three successive cyclic comparisons are all one.}
}
\tag{5}
\]
No cyclic order with \(D\ge6\) has an at-most-one-switch Hamilton path among its rotations. Reversing the cyclic order preserves \(D\) and condition (5).

*Proof.* Since \(D\) is even, \(D=0\) gives all monochromatic windows. For \(D=2\), some three-comparison block contains at least one change, so (4) gives at most one. If \(D=4\), equation (4) gives at most one precisely when the maximum three-comparison block has all three changes. If \(D\ge6\), even omitting three changes leaves at least three. Reversing the order complements and reverses the cyclic triple-color word by reversal oddness, which reverses the cyclic comparison vector and preserves its total and its runs of length three. \(\square\)

**Corollary 3 (a sharp reduction of the unrestricted boundary conjecture).** The unrestricted boundary-tournament one-switch conjecture is equivalent to the following cyclic variation-selection assertion:

> For every reversal-odd binary coloring of ordered distinct triples, there is a cyclic ordering of all vertices whose cyclic triple-color comparison word satisfies (5).

This is an equivalent reformulation, not a proven existence claim. It reduces the desired bound to finding a cycle with either at most two transitions or four transitions containing a run of three consecutive changes. The second alternative must be retained; merely conjecturing the existence of a cycle with \(D\le2\) is a strictly stronger problem.

**Structural point.** Equation (1) is one common root-selection theorem, not a disjunction of two classes. The original systems differ only in intrinsic twist \(\epsilon\), orbit length \(L\), and observation width \(m\): NORI1 has \((\epsilon,L-m)=(1,0)\), while ordinary boundary tournaments have \((0,2)\). In both cases the unresolved mathematics is *inter-orbit selection*: using rank-two face exchanges, projective incidence, or equivariant topology to force an orbit of sufficiently low variation.

## Deletion of switches and minimal obstructions

Let \(H\) be a finite graph whose vertices are the objects read by path color words, and let \(R\) be a fixed-point-free involution of its vertex set which preserves adjacency. A permitted coloring is a function \(c:V(H)\to\mathbb F_2\) with \(c(Rv)=1+c(v)\). Write \(D(c)=\{uv\in E(H):c(u)\ne c(v)\}\). We allow a retained transition set \(S\subseteq D(c)\), without requiring equality. Throughout, transitions used by a complete path are distinct, including after identification under \(R\) when that identification is used.

**Theorem 4 (intrinsic description of the deletion-closed family).** For any set \(S\subseteq E(H)\), there exists a permitted coloring with \(S\subseteq D(c)\) if and only if
\[
K(S)=\bigl(V(H),\,S\cup\{\{v,Rv\}:v\in V(H)\}\bigr)
\]
is bipartite. If transitions are retained in \(R\)-orbits, replace \(S\) in this formula by the union of their lifts. Every connected component of \(K(S)\) has two possible colorings, independently of the other components.

*Proof.* Every edge displayed in \(K(S)\) requires its two endpoint bits to differ. A proper binary vertex coloring satisfies all these requirements, and the opposition edges give the required identity under \(R\). Conversely every permitted completion of \(S\) is a proper binary coloring of \(K(S)\). The usual alternating coloring along paths proves that such a coloring exists precisely when there is no odd cycle. In each connected bipartite component the coloring is determined by one vertex bit. \(\square\)

For cubes with \(n\ge3\), take \(H=L(Q_n)\), with cube edges as its vertices and cube antipodality as \(R\). For boundary tournaments on at least four vertices, the vertices of \(H\) are ordered distinct triples; its edges are the unordered pairs
\[
\{(a,b,c),(b,c,d)\},
\]
where \(a,b,c,d\) are distinct, and \(R(a,b,c)=(c,b,a)\). Thus an edge of \(H\) is a comparison of consecutive triple windows. In both models the original switch sets are \(R\)-invariant. A complete path uses each transition orbit at most once: on a cube path its turns occur at distinct antipodal vertex classes; in a Hamilton order distinct consecutive four-vertex windows cannot coincide up to reversal.

Theorem 4 gives an intrinsic hereditary condition for switch deletion. In particular, omitting a transition from \(S\) imposes no equality constraint on its endpoint colors.

**Proposition 5 (critical witnesses and the common threshold).** Let \(\mathcal P\) be a finite family of complete paths and let \(T(P)\) denote the set of transition orbits used by \(P\). If \(S\) is inclusion-minimal subject to
\[
|S\cap T(P)|\ge r+1\qquad(P\in\mathcal P),
\]
then for each \(s\in S\) there is a path \(P_s\) such that
\[
s\in T(P_s),\qquad |S\cap T(P_s)|=r+1.
\]
A counterexample to either motivating conjecture yields such a set with \(r=1\), satisfying the bipartiteness condition of Theorem 4.

*Proof.* By minimality some complete path has at most \(r\) retained transitions after deleting \(s\). Restoring \(s\) changes its count by at most one, whereas the original count is at least \(r+1\). Thus the path contains \(s\) and has count \(r+1\).

A boundary counterexample has at least two switches on every Hamilton order by definition. A cube coloring with no monochromatic full geodesic also has at least two switches on every full geodesic: the root-slide formula (2) turns any at-most-one-switch geodesic into a monochromatic one. Choose a minimal subset of transition orbits retaining this lower bound. Its lift is contained in the original switch set and hence satisfies Theorem 4. Conversely any such bipartite retained obstruction extends to a permitted coloring; that coloring has at least two switches on every complete path. \(\square\)

The reduction for cubes uses the one-switch threshold before deleting transitions. Root sliding need not turn a retained one-switch path into a retained zero-switch path after deletion.

### All rotations of a critical witness

The next lemma uses cyclic comparison positions without assuming they arise from a binary word. Fix integers \(r\ge0\) and \(q\ge1\). Let \(\mathcal C\) be a family of cycles of length greater than \(q\), each with distinct transition identifiers in cyclic order. A complete path consists of a cycle with a block of \(q\) consecutive transitions omitted. Let \(S\) be a set of identifiers. For a cycle \(C\), put
\[
d_S(C)=|S\cap C|,\qquad
M_S(C)=\max_{\substack{B\subset C\\B\text{ a cyclic }q\text{-block}}}|S\cap B|.
\]
The least retained count among its complete paths is \(d_S(C)-M_S(C)\).

**Theorem 6 (bounded cyclic witnesses).** Suppose \(S\) is inclusion-minimal with every complete path having at least \(r+1\) retained transitions. Each \(s\in S\) belongs to a cycle \(C_s\) and has an omitted block \(B_s\) avoiding \(s\), such that
\[
|S\cap(C_s\setminus B_s)|=r+1,\qquad
r+2\le d_S(C_s)\le r+q+1.
\]
Moreover every \(q\)-block \(B\) in this cycle satisfies
\[
|S\cap B|\le d_S(C_s)-(r+1),
\]
with equality for \(B_s\).

*Proof.* Proposition 5 supplies a complete witness containing \(s\), hence a cycle and omitted block avoiding \(s\). Its total retained count is \(r+1+|S\cap B_s|\), proving the upper bound. Every rotation is a complete path, so the displayed block inequality follows. Since the cycle contains a retained transition, some \(q\)-block contains at least one, and the inequality gives the lower bound. \(\square\)

**Corollary 7 (cube witnesses).** A hypothetical NORI1 counterexample has an antipodally invariant retained set \(S\), whose lift satisfies Theorem 4, with the following properties:

1. Every projective Petrie cycle contains at least three members of \(S\).
2. Every \(s\in S\) lies on a projective Petrie cycle containing precisely three members of \(S\).

These two properties are equivalent to minimality among retained sets for which every full geodesic has at least two retained transitions.

*Proof.* The projective Petrie cycle has \(n\) turns; its root slides omit each single turn in succession. Thus the least retained path count is \(\max\{0,d_S(C)-1\}\). Theorem 6 with \(q=1,r=1\) gives three retained turns on each critical witness cycle. Conversely a cycle with three retained turns becomes a cycle with two after deleting any one of them, and omitting one of the remaining two gives a complete path with one retained transition. \(\square\)

**Corollary 8 (boundary witness classification).** A hypothetical boundary counterexample has a reversal-invariant retained set satisfying Theorem 4. Each retained transition \(s\) has a cyclic Hamilton witness of one of these forms:

- Three retained positions, with cyclic distances between successive retained positions at least three.
- Four retained positions, with no block of three consecutive retained positions, and a three-position block avoiding \(s\) that contains two retained positions.
- Five retained positions, with a block of three consecutive retained positions avoiding \(s\).

These are the complete possibilities for a cycle to certify that deleting \(s\) destroys the lower bound of two on some rotation, while all rotations originally satisfy that bound.

*Proof.* Hamilton orders omit three cyclic comparisons, so apply Theorem 6 with \(q=3,r=1\). The total \(d\) is three, four, or five. If \(d=3\), every three-position block contains at most one retained position, which is equivalent to the spacing condition; a block containing one of the other retained positions avoids \(s\). If \(d=4\), every block has at most two retained positions, and the witness block must have two and avoid \(s\). If \(d=5\), the lower bound on every rotation is automatic, and a witness block has three retained positions and avoids \(s\). These conditions are also sufficient, by restoring the omitted block and counting the two retained positions outside it. \(\square\)

In particular the first boundary case requires at least nine vertices. Neither the odd cube count nor the even boundary count of the original switch word can be imposed on a retained set after deletion.

### Exchange inequalities and odd-cycle certificates

**Theorem 9 (replacement demand).** Let \(S\) meet every complete path in at least \(k\) transitions, and let \(P\) be a complete path meeting it in precisely \(k\). For every complete path \(Q\),
\[
|S\cap(T(Q)\setminus T(P))|
\ \ge\
|S\cap(T(P)\setminus T(Q))|.
\]
Equality makes \(Q\) another path meeting \(S\) in precisely \(k\). The same statement holds for any family of cycles with a uniform lower bound \(k\), in particular the three-turn cube witnesses of Corollary 7.

*Proof.* Subtract the counts on \(P\) and \(Q\). Their common transitions cancel, and the resulting difference is nonnegative. \(\square\)

This inequality retains the complete-path constraint in every exchange. An adjacent dimension exchange changes at most three turn positions of a cube path or projective Petrie cycle. An adjacent vertex exchange changes at most five comparison positions of a boundary Hamilton path. Thus removing \(a\) retained transitions in one such exchange requires at least \(a\) of at most three, respectively five, replacement transitions to be retained. The bounds remain valid for deleted sets; they do not use the parity of a completed color word.

**Corollary 10 (bipartite exclusion in an exchange).** Suppose \(F\subseteq S\) is known, and form \(K(F)\) as in Theorem 4. A transition whose endpoints are joined by an even-length path in \(K(F)\) cannot belong to \(S\). Consequently, in an exchange from Theorem 9 that removes \(a\) retained transitions, at least \(a\) replacement transitions must avoid this exclusion. If fewer than \(a\) do so, the assumed obstruction has no permitted completion. If precisely \(a\) do so, every one of them is forced into \(S\).

*Proof.* Adding an edge between the endpoints of an even-length path gives an odd closed walk and hence an odd cycle. This contradicts bipartiteness of \(K(S)\). Apply this exclusion to the replacement demand. \(\square\)

For an orbit transition the exclusion may be tested on either lift; opposition edges ensure that the tests agree. Repeatedly adjoining forced transitions to \(F\) can therefore yield an odd-cycle certificate of inconsistency. This is a sufficient contradiction mechanism. A theorem forcing it to terminate in an odd cycle for every critical obstruction in either path geometry remains open.

The conclusions above reduce both original problems to exclusion of bipartite critical transition sets with complete two-transition path witnesses. Cube root slides strengthen those witnesses to three-transition Petrie cycles, while Hamilton rotations restrict them to the three configurations of Corollary 8. Establishing a global exchange argument from these constrained witnesses is the remaining existence step.


## Hereditary containers and the structure of tight witnesses

The containing transition set may be fixed before any deletion. If \(\mathcal B\) is any collection of transition sets, its downward closure
\[
\mathcal D(\mathcal B)=\{S:S\subseteq B\text{ for some }B\in\mathcal B\}
\]
is hereditary. For any complete-path family, the assertion that every \(S\in\mathcal D(\mathcal B)\) has a path of retained count at most one is equivalent to the same assertion restricted to \(B\in\mathcal B\). Indeed a favorable path for the containing set remains favorable after deletion; conversely the containing sets themselves belong to the downward closure. Critical witness arguments therefore require no symmetry or coloring condition beyond membership in the chosen hereditary class.

### An oddness-free cube formulation

For a cube \(Q_n\), let \(S\) be a set of its unoriented two-edge turns. Regard \(S\) as an edge set in the line graph \(L(Q_n)\), and let \(\sigma_S(P)\) count the turns of a geodesic \(P\) belonging to \(S\).

**Theorem 11 (bipartite turn reformulation).** The following all-dimensional assertions are equivalent:

1. Every antipodally odd binary cube-edge coloring has a monochromatic full antipodal geodesic.
2. Every binary cube-edge coloring has a full antipodal geodesic with at most one color change.
3. For every \(n\) and every \(S\subseteq E(L(Q_n))\) such that the graph \((V(L(Q_n)),S)\) is bipartite, some full antipodal geodesic \(P\) satisfies \(\sigma_S(P)\le1\).

The equivalence of the first two assertions is the established Leader–Long dimension-shift equivalence, recorded previously in the project's doubling treatment. The third is its hereditary switch formulation.

*Proof.* A binary cube-edge coloring is a binary vertex coloring of \(L(Q_n)\). Its switch set is a cut in that line graph. A set \(S\) is contained in such a cut if and only if \((V(L(Q_n)),S)\) is bipartite, by assigning either side of each bipartite component color zero. Thus assertion 2 supplies the favorable path in assertion 3. Assertion 3 applied to the full switch set gives assertion 2.

For completeness, write \(A_n\) and \(B_n\) for assertions 1 and 2 in dimension \(n\). Then \(B_n\) implies \(A_n\): if an antipodally odd coloring has a one-change geodesic, write it as \(L:x\to y\) of color \(a\), followed by \(R:y\to\bar x\) of color \(1-a\). The concatenation
\[
L^{-1}:y\to x,\qquad \bar R^{-1}:x\to\bar y
\]
is monochromatic of color \(a\) and uses each dimension once. A path already monochromatic requires no change.

Conversely, for an arbitrary coloring \(c\) on \(Q_n\), construct a coloring \(C\) on \(Q_n\times\{0,1\}\) by giving the lower copy of an edge \(e\) color \(c(e)\), the upper copy color \(1-c(\bar e)\), and the vertical edge at \(x\) color \(x_1\). This is an antipodally odd coloring. Under \(A_{n+1}\), take a monochromatic full geodesic and orient it so its vertical crossing is from layer zero to layer one. Its lower portion \(L:x\to y\) and upper portion \(R:y\to\bar x\) use complementary dimension sets. If the common color is \(a\), then \(L^{-1}\) is colored \(a\) in the original cube, whereas the antipodal image of the upper portion, reversed, is colored \(1-a\). Their concatenation goes from \(y\) to \(\bar y\), uses each original dimension once, and has at most one change. Hence \(A_{n+1}\) implies \(B_n\), proving the all-dimensional equivalence. The one-dimensional assertion \(B_1\) is immediate. \(\square\)

Here bipartiteness is imposed on the retained turn set alone; there are no opposition edges. Deletion is ordinary single-turn deletion. If assertion 3 fails, an inclusion-minimal failing set is bipartite and every retained turn belongs to a full geodesic with precisely two retained turns. This reformulation removes antipodal oddness from the switch hypothesis while preserving equivalence to the full NORI1 problem.

The three-turn Petrie conclusion of Corollary 7 concerns antipodally invariant transition-orbit sets. It is a separate, stronger conclusion available in that symmetric formulation; it is not asserted for arbitrary sets from Theorem 11.

### Uncrossing two-switch witnesses

Let \(S\) be any retained transition set for which every complete path has at least two retained transitions. Call a complete path *tight* in this paragraph when it has precisely two retained transitions. The adjective refers only to equality in this lower bound; for boundary tournaments the underlying paths are also tight paths in the usual hypergraph sense.

**Theorem 12 (prefix agreement under admissible tail exchange).** Suppose two tight complete paths \(P,Q\) share an observation at which both exchanges of their suffixes give admissible complete paths, with no new comparison at the join. Let \(a\) and \(b\) be their retained counts before the common observation, including comparisons ending at it. Then
\[
a=b.
\]
Both exchanged paths are tight. The conclusion depends only on the path family and \(S\); no binary coloring or opposition relation is needed.

*Proof.* The two hybrid paths have retained counts
\[
a+(2-b),\qquad b+(2-a).
\]
Each is at least two. The first inequality gives \(a\ge b\), and the second gives \(b\ge a\). Thus both counts are two. \(\square\)

The common observation and completeness conditions can be expressed directly in the two geometries.

**Corollary 13 (coherent prefix levels on cube witnesses).** Fix a root \(x\) in \(Q_n\). Orient each cube edge away from \(x\), according to increasing Hamming distance. Let \(E_x\) be the set of edges occurring on two-switch full geodesics rooted at \(x\). For every \(e\in E_x\), the number of retained turns before and through the observation \(e\) is independent of the chosen two-switch geodesic containing it. Denote it by
\[
h_x(e)\in\{0,1,2\}.
\]
If consecutive edges \(e,f\) occur on such a geodesic, then
\[
h_x(f)-h_x(e)=\mathbf1_{\{\{e,f\}\in S\}}.
\]
Initial edges have level zero and terminal edges level two. Any full rooted geodesic each of whose consecutive turns occurs on some two-switch rooted geodesic has precisely two retained turns.

If \(S\) is antipodally invariant, then \(E_x\) is antipodally invariant and
\[
h_x(\bar e)=2-h_x(e).
\]

*Proof.* Two full geodesics from \(x\) containing the same edge traverse it in the same direction. Their dimension sets before that edge agree: they are the dimensions in which its initial vertex differs from \(x\). Exchanging their suffixes at the common edge therefore preserves every dimension precisely once. No new comparison is created because the edge observation itself is shared. Theorem 12 proves independence of \(h_x\), and the increment formula follows on each witness.

For a full geodesic assembled from witness turns, the increment formula telescopes. Its first edge occurs as a first edge on every rooted geodesic containing it, so has level zero; its last edge has level two. The retained count is consequently two.

When \(S\) is antipodally invariant, reversing a full geodesic and complementing all its vertices gives another full geodesic from the same root \(x\), with the same retained count. The prefix ending at \(\bar e\) in the transformed path corresponds to the suffix beginning at \(e\) in the original. Those two counts sum to two. \(\square\)

Thus the union of rooted witnesses has three coherent edge regions. Each retained turn on a witness crosses from level zero to one, or from level one to two. In the symmetric formulation, antipodality exchanges these two kinds of crossings.

**Corollary 14 (coherent prefix levels on Hamilton witnesses).** Let \(V\) be the vertex set of a boundary path problem with an arbitrary retained comparison set \(S\). For a prefix of a two-switch Hamilton order, retain its used vertex set \(U\) and its final ordered triple \(t\). The prefix switch count is determined by \((U,t)\), independently of the witness order. In particular two witnesses with the same used set and final ordered triple can exchange their suffixes, producing two further two-switch Hamilton orders.

*Proof.* Both suffixes use precisely the vertices of \(V\setminus U\). The common final triple supplies the same preceding observation for the first comparison of either suffix. Both exchanges therefore preserve distinct vertices and create no new comparison. Apply Theorem 12. \(\square\)

Repeated admissible tail exchanges preserve the prefix levels and generate further complete witnesses. These conclusions use the support required by geodesicity or Hamilton completeness explicitly. Equality of terminal observations alone is sufficient for rooted cube witnesses, because the root determines their used dimensions; for Hamilton witnesses the used vertex set remains necessary.

### The graph of two-switch witness pairs

For a retained set \(S\), define a graph \(W_S\) on vertex set \(S\) by
\[
st\in E(W_S)
\quad\Longleftrightarrow\quad
S\cap T(P)=\{s,t\}
\text{ for some complete path }P.
\]
Criticality says that \(W_S\) has no isolated vertices. Rotational closure supplies stronger conclusions.

**Theorem 15 (certified witness triangles on the cube).** In the antipodally invariant critical cube formulation of Corollary 7, every vertex and every edge of \(W_S\) lies in a triangle supplied by a projective Petrie cycle containing precisely three retained turns.

*Proof.* For any tight geodesic \(P\), its projective Petrie cycle \(C\) has all the turns of \(P\) and one closing turn. Thus \(|S\cap C|\le3\). Every cycle has at least three retained turns by Corollary 7, so its count is three. Root slides can omit each of these three turns in succession, producing all three pairs as two-switch complete witnesses. Every edge of \(W_S\) therefore lies in the corresponding triangle. Criticality covers every vertex by an edge. \(\square\)

The triangle vertices are switches, not colored observations. This assertion imposes no odd-cycle contradiction on the transition constraint graph from Theorem 4.

**Theorem 16 (boundary rotational witness graphs).** Let \(C\) be a cyclic Hamilton order whose every rotation has retained count at least two, and suppose some rotation has count two. Define \(W_C\) on the retained positions in \(C\), with an edge for each retained pair left by a two-switch rotation. Then:

1. If \(C\) has three retained positions, \(W_C=K_3\).
2. If \(C\) has four retained positions, \(W_C\) is bipartite.
3. If \(C\) has five retained positions and the cycle has length greater than five, the nonisolated part of \(W_C\) is a path with one, two, or three edges.
4. If the cycle has length five and all its positions are retained, \(W_C=C_5\).

These exhaust the possibilities.

*Proof.* Theorem 6 restricts the number of retained positions to three, four, or five.

For three, the spacing condition ensures that a three-position block can omit any one retained position while leaving the other two, giving \(K_3\).

For four, let \(J_C\) be the graph on the four retained positions joining a pair when both can be contained in a three-position cyclic block. No such block contains three retained positions. Consequently \(W_C\) has the edge complementary to each edge of \(J_C\), where complementation means taking the other two vertices among the four. The degree of \(J_C\) is at most two: the possible neighbors of a marked position have offsets \(-2,-1,1,2\), and choosing any three of these would produce three consecutive marked positions, which is forbidden. A triangle in \(W_C\) would correspond to three edges of \(J_C\) with a common endpoint, contrary to that degree bound. A graph on four vertices is nonbipartite only if it contains a triangle. Hence \(W_C\) is bipartite.

For five on a longer cycle, an unretained position exists, so the retained positions split into runs. A two-switch rotation must omit a block of three consecutive retained positions. Since there are only five retained positions in total, at most one run has length at least three. If its length is three, four, or five, its consecutive triple blocks leave respectively one, two, or three distinct retained pairs. Naming a length-five run \(a,b,c,d,e\), these pairs are \(de,ae,ab\), which form a three-edge path; shortening the run gives the shorter paths. Remaining retained positions are isolated where applicable.

On a five-cycle with all positions retained, omitting a cyclic block of three leaves two consecutive positions. The five possible pairs form \(C_5\). \(\square\)

Theorem 16 requires no binary parity condition and therefore includes the pentagon case. In the original completed boundary coloring, a five-cycle cannot have all five comparisons switched because a periodic binary word has even cyclic variation. An arbitrary hereditary container need not enforce that restriction.

Theorems 12–16 supply structure beyond individual private witnesses: coherent switch counts at admissible joins, closure under complete-path recombination, and certified small witness-pair graphs. A proof of existence must still compare prefix levels across different supports or roots, or derive a contradiction from the containing set and these witness configurations. No such global comparison is established here.


## Coupling deletion witnesses

Retain the antipodally invariant cube formulation: \(S\) is a set of projective turn orbits, contained in the switch set of some antipodally odd cube-edge coloring, and every full geodesic has retained count at least two. Assume \(S\) is inclusion-minimal for this lower bound. A full geodesic uses any given turn orbit at most once.

**Proposition 17 (complete description after one deletion).** For every \(s\in S\), put \(S_s=S\setminus\{s\}\). Then
\[
\min_P\sigma_{S_s}(P)=1.
\]
Its one-switch geodesics are precisely the original two-switch geodesics containing \(s\). Their projective Petrie cycles contain three original retained turns, one of which is \(s\). After deletion those cycles have two retained turns. Among the \(n\) cyclic cuts of each such projective cycle, precisely two have retained count one; the other \(n-2\) have count two.

*Proof.* Deleting \(s\) reduces the count on any complete path by at most one, so every path still has count at least one. Criticality supplies one of count one. If a path has count one after deletion, its original count is at least two and differs by at most one, so its original count is two and it contains \(s\). The converse is immediate. Theorem 15 identifies its original cyclic count as three. Removing \(s\) leaves two active cyclic comparisons. A cut omits one comparison, giving count one precisely when that comparison is one of the remaining two. \(\square\)

Thus the two optimal rotations after deletion supply two cuts of the same two-switch period. Coupling them to other witnesses requires comparisons between their supports or roots.

### Deletion fixes the position of a switch at shared prefixes

The following statement does not require a coloring or an opposition relation. It applies to cube turns, boundary comparisons, or another complete-path family with the stated exchange property.

**Theorem 18 (uniform intersections at shared prefixes).** Let \(k\ge1\), and let \(S\) be a transition set for which every complete path has retained count at least \(k\). Suppose no complete path repeats a transition identifier. Fix prefix data \(q\) such that any two complete paths through \(q\) may exchange their suffixes in both directions, preserving completeness and creating no new comparison. Consider all paths through \(q\) having retained count \(k\).

Their prefix count has one common value \(h(q)\). For each retained transition \(s\) used by any such path, whether \(s\) occurs in the prefix is independent of the chosen path through \(q\) containing \(s\). Write this indicator as \(b_q(s)\in\{0,1\}\). Every retained \(k\)-set \(A\) realized by a path through \(q\) satisfies
\[
\boxed{\sum_{s\in A}b_q(s)=h(q).}
\]
In particular, all realized \(k\)-sets meet the subset \(\{s:b_q(s)=1\}\) in the same number of elements.

*Proof.* If two paths have prefix counts \(a,b\), their exchanged paths have counts \(a+k-b\) and \(b+k-a\). Both are at least \(k\), so \(a=b\). This defines \(h(q)\).

Fix \(s\), and restrict to paths through \(q\) using \(s\). After deleting \(s\), all these paths have count \(k-1\). Every complete path has count at least \(k-1\), because no path repeats \(s\). Applying the same tail-exchange argument to \(S\setminus\{s\}\), the deleted prefix count has a common value \(h_s(q)\). Therefore
\[
b_q(s)=h(q)-h_s(q)
\]
is independent of the path and equals the indicator that its prefix used \(s\). Summing these indicators on a path proves the displayed formula. \(\square\)

For cube geodesics, fix a root and take \(q\) to be an edge observation. The root determines its orientation and the dimensions used before it. For Hamilton orders, take \(q=(U,t)\), where \(U\) is the used vertex set and \(t\) the final ordered triple. These are the exchange data verified in Corollaries 13–14.

**Corollary 19 (bipartite witness pairs at a middle observation).** In the case \(k=2\), let \(W_q\) be the graph on retained switches occurring in two-switch complete paths through \(q\), with an edge for each pair realized by such a path. If \(h(q)=1\), then
\[
\boxed{W_q\text{ is bipartite},}
\]
with the sides given by \(b_q(s)=0\) and \(b_q(s)=1\).

Consequently, witnesses for the pairs
\[
\{s_0,s_1\},\ \{s_1,s_2\},\ \ldots,\
\{s_{2r},s_0\}
\]
cannot all share compatible prefix data at which each path has one retained switch before the join. In particular, the three pairs of a certified witness triangle cannot all have a common compatible middle observation.

*Proof.* Theorem 18 gives \(b_q(s)+b_q(t)=1\) on every witness edge. This is a proper binary vertex coloring of \(W_q\). Around an odd cycle the roles would alternate and return to their complement, which is impossible. \(\square\)

This is a coupling criterion on the switch witnesses themselves. It applies to every hereditary containing-set hypothesis. Criticality is used to ensure that every switch has witnesses; the exclusion at a common prefix follows from the lower bound and admissible recombination.

### Two antipodally odd binary labels after deletion

Fix a cube root \(x\). Let \(E_x^s\) be the edges occurring in the one-switch \(S_s\)-geodesics from \(x\), equivalently in the original two-switch geodesics from \(x\) containing \(s\). Define
\[
u_x^s(e)=\text{the }S_s\text{-prefix count through }e,
\qquad
b_x^s(e)=\text{the indicator that }s\text{ has occurred through }e.
\]

**Theorem 20 (binary labels and antipodal complementation).** Both functions are well defined on \(E_x^s\), have values in \(\{0,1\}\), and satisfy
\[
h_x(e)=u_x^s(e)+b_x^s(e),
\]
where \(h_x\) is the original two-switch prefix level. Moreover \(E_x^s\) is antipodally invariant, and
\[
\boxed{
u_x^s(\bar e)=1-u_x^s(e),\qquad
b_x^s(\bar e)=1-b_x^s(e).
}
\]
Along any consecutive edge pair appearing in one of these witnesses, \(b_x^s\) changes precisely at \(s\), and \(u_x^s\) changes precisely at the other retained switch. Their disagreement set is the middle edge region \(h_x=1\).

*Proof.* Proposition 17 gives the family of one-switch paths. Theorem 18 with \(k=2\) proves that their deleted prefix counts and indicators of \(s\) are well defined at each shared edge. Both are zero or one, and their sum is the original prefix count.

Reverse a witness and complement all its vertices. Antipodal invariance of \(S_s\) makes this another one-switch geodesic from \(x\), and it still contains \(s\) in the original set. The prefix count through \(\bar e\) in the transformed path is the suffix count after \(e\) in the original path, so its deleted count is \(1-u_x^s(e)\). The original path uses \(s\) once, and the transformed prefix contains it precisely when the original suffix does, giving \(1-b_x^s(e)\). The increment statements follow by counting on each witness. Finally two binary values have sum one precisely when they differ. \(\square\)

The retained set need not itself be the switch set of a binary coloring. Nevertheless, each critical deletion canonically produces two antipodally odd binary labels on its witness domain. One label records the deleted transition, and the other records its witness partner. At a compatible middle edge these labels determine the consistent switch roles of Corollary 19.

### A component condition for coupling rooted witnesses

Let \(E_x\) be the union of all two-switch rooted geodesic edges. Form a graph \(J_x\) on \(E_x\), retaining the adjacency \(\{e,f\}\) precisely when that turn belongs to \(S\) and occurs consecutively on some two-switch geodesic from \(x\). This graph records only retained transitions, while preserving their rooted complete-path certificates.

**Proposition 21 (paired retained-transition components).** If \(S\) is contained in a NORI1 switch set, no connected component of \(J_x\) contains both \(e\) and \(\bar e\). Equivalently, antipodality pairs the connected components of \(J_x\) without fixing a component.

*Proof.* By Corollary 13, the integer prefix level \(h_x\) changes by one across every edge of \(J_x\). Hence \(h_x\bmod2\) is a proper binary coloring of \(J_x\). Antipodality sends \(h_x(e)\) to \(2-h_x(e)\), preserving this parity.

Let \(c\) be any antipodally odd cube-edge coloring whose switch set contains \(S\). On every edge of \(J_x\), both \(c\) and \(h_x\bmod2\) change, so their sum is constant on each connected component. Were \(e\) and \(\bar e\) in the same component, this constant would have equal values at them. Antipodality complements \(c\) and preserves \(h_x\bmod2\), making those values different. This is a contradiction.

The graph \(J_x\) is antipodally invariant by the witness reversal used in Corollary 13. A component is fixed by antipodality precisely when it contains an antipodal vertex pair, proving the equivalent statement. \(\square\)

This gives another sufficient contradiction certificate: a chain of retained transitions, each lying in a rooted two-switch witness, that joins an edge observation to its antipode. It uses ordinary connectivity only to contradict the containing coloring; the constituent transitions retain their complete geodesic certificates.

The other switch-matroid treatment identifies legal signature changes on the folded line graph with its binary cut space, whose minimal nonzero supports are cographic circuits. This describes changes of a completed coloring. The deletion arguments here concern subsets of a fixed containing signature; Theorems 18–20 remain valid before a completion is chosen. Coupling must therefore supply either a compatible middle observation for an odd cycle of witness pairs, or an antipodally invariant component forbidden by Proposition 21, or another contradiction using the containing set. Criticality alone has not yet been shown to force any of these global configurations.


## Root transport, independent arms, and cographic bond moves

The deletion witnesses admit a factorization into independent geodesic arms. This makes root transport a finite-dimensional comparison of two minimum switch counts and gives a family of legal bond moves.

Let \(s=([v],\{i,j\})\in S\) be a retained projective turn. Fix a lift \(v\), and a root \(x\) for which
\[
D=\{d:x_d\ne v_d\}
\]
contains \(i\) and excludes \(j\). A full geodesic from \(x\) containing this lift of \(s\) arrives at \(v\) in direction \(i\) and leaves in direction \(j\). Define
\[
\begin{aligned}
p_s(x,v)&=\min\{\sigma_S(A):
 A:x\to v\text{ uses }D,\text{ with final direction }i\},\\
q_s(x,v)&=\min\{\sigma_S(B):
 B:v\to\bar x\text{ uses }[n]\setminus D,\text{ with first direction }j\}.
\end{aligned}
\]
The costs here count only the internal turns of each arm. No turn at the join \(v\) is included. Both families of arms are nonempty. For the other eligible roots interchange the names \(i,j\). Eligibility is the affine condition
\[
x_i+x_j=1+v_i+v_j\pmod2.
\]

**Theorem 22 (arm factorization and opposite branches).** Suppose every full geodesic has retained count at least two. Then
\[
p_s(x,v)+q_s(x,v)\ge1.
\]
There is a two-switch geodesic from \(x\) through this lift of \(s\) if and only if \(p_s(x,v)+q_s(x,v)=1\). In that case the family of all such geodesics is the Cartesian product of the minimizing prefix-arm family and the minimizing suffix-arm family.

If \(S\) is antipodally invariant, then
\[
p_s(x,\bar v)=q_s(x,v),\qquad
q_s(x,\bar v)=p_s(x,v).
\]
The families through \(v\) and \(\bar v\) are internally vertex-disjoint: their only possible common vertices are \(x,\bar x\). Within one branch all two-switch witnesses encounter \(s\) in the same position among their retained switches; in the other branch that position is reversed.

*Proof.* Any prefix arm \(A\) and suffix arm \(B\) use complementary dimension sets. Their concatenation is therefore a full geodesic, with cost
\[
\sigma_S(A)+1+\sigma_S(B),
\]
since the joining turn is \(s\). The two minima can be attained independently, proving the lower bound and the criterion. If their sum is one, a two-switch concatenation must attain both minima, and every pair of minimizing arms gives such a concatenation.

Antipodal reversal converts a suffix through \(v\) to a prefix through \(\bar v\) from the same root, and conversely, proving the two identities. For disjointness, identify cube vertices with their flip sets from \(x\). A chain through \(v\) consists of sets comparable with \(D\); a chain through \(\bar v\) consists of sets comparable with \([n]\setminus D\). Since these two sets are disjoint and both nonempty, a set comparable with both is either empty or all of \([n]\). Thus the paths have no common internal vertex. Finally \((p_s,q_s)\) is either \((0,1)\) or \((1,0)\), determining whether \(s\) is the first or second retained turn; antipodal reversal swaps these types. \(\square\)

In particular, the two branches created by a fixed critical deletion do not need to be coupled through a common middle edge. The arm factorization instead describes how their roots and dimension sets can change.

### Opposite arm types supplied by each critical cycle

**Theorem 23 (root transport along the intervening arc).** Let a projective Petrie cycle contain precisely the three retained turns \(s,a,b\). Choose a lift \(v\) of the center of \(s\), and orient a half-cycle from \(v\) to \(\bar v\). Its dimension order is
\[
(j,d_1,\ldots,d_{n-2},i).
\]
Let \(x\) and \(y\) be the centers of the lifted turns \(a,b\), in that order along this half-cycle. Then \(x,y\) lie in the same \((n-2)\)-face of root choices, fixing
\[
x_i=y_i=v_i,\qquad x_j=y_j=1-v_j.
\]
At the lift \(v\), their arm types are
\[
(p_s(x,v),q_s(x,v))=(0,1),\qquad
(p_s(y,v),q_s(y,v))=(1,0).
\]
Along the segment from \(x\) to \(y\) inherited from the half-cycle, every intermediate root \(z\) satisfies
\[
(p_s(z,v),q_s(z,v))
\in\{(0,1),(1,0),(1,1)\}.
\]
The connecting segment uses only the exterior dimensions \(d_1,\ldots,d_{n-2}\), each once, and has no retained internal turn.

*Proof.* The centers \(x,y\) occur after the first move \(j\) and before the last move \(i\), establishing the fixed root bits. Rotating the complete path to start at \(x\) omits the turn \(a\); its two retained turns are \(b\) and the lift of \(s\) at \(\bar v\), in that order. Antipodal reversal gives a path from the same root through \(v\) on which \(s\) is first. It therefore supplies a zero-cost prefix and a one-cost suffix. Theorem 22 proves that their minima are \((0,1)\). Rotating to \(y\) omits \(b\) and reverses the retained order, giving \((1,0)\) at \(v\).

At any root strictly between these two centers, the inherited rotated path encounters one retained turn on each side of the lift of \(s\). Antipodal reversal therefore supplies arms of cost one on each side of \(v\). The minima are each at most one, while Theorem 22 excludes \((0,0)\). Finally the segment between \(x,y\) contains neither \(s\) nor the endpoint turns \(a,b\) internally, so all its internal retained turn indicators are zero. \(\square\)

Thus every critical cycle supplies opposite arm types in one connected cube of eligible roots. The intermediate type \((1,1)\) accounts for loss of two-switch witnesses during transport; the inherited paths then have three retained switches.

### A common connector produces a whole witness family

**Theorem 24 (zero-cost arms joined by a zero-cost connector).** Let \(x,y\) be eligible roots for the same lift \(v\), and suppose their flip sets from \(v\) satisfy
\[
D_x\subsetneq D_y,
\qquad
K=D_y\setminus D_x\subseteq[n]\setminus\{i,j\}.
\]
Let \(R:x\to y\) be a geodesic using \(K\) with no retained internal turn. Suppose \(p_s(x,v)=0\) and \(q_s(y,v)=0\).

For every zero-cost prefix \(A:x\to v\) ending in the incoming direction of \(s\), and every zero-cost suffix \(B:v\to\bar y\) starting in its outgoing direction, the concatenation
\[
P=A^{-1}\,R\,\bar B^{-1}
\]
is a full antipodal geodesic from \(v\) to \(\bar v\). It has precisely two retained turns, at the two ends of \(R\). Its projective cyclic completion has precisely those two retained turns and \(s\).

*Proof.* The three segments use, respectively,
\[
D_x,\qquad K,\qquad[n]\setminus D_y,
\]
which partition \([n]\). They concatenate at \(x,y\) and hence form a full geodesic. Antipodal invariance makes \(\bar B^{-1}\) zero-cost. All three segments have zero internal retained count; the only possible retained turns are their two joins. The global lower bound of two therefore forces both joining turns to belong to \(S\). The first direction of \(P\) is the incoming direction of \(s\), and its last is the outgoing direction, so its cyclic closing turn is \(s\). \(\square\)

Theorem 23 supplies the hypotheses of Theorem 24 for every critical three-turn cycle. The connector can be fixed while all zero-cost arms vary independently. When \(R\) has length one, the two forced turns occur at opposite ends of one cube edge.

### A cographic bond lowers the completed variation

Write \(G=Q_n/A\) and \(H=L(G)\), where vertices of \(H\) are projective cube-edge orbits. For the fixed connector \(R\) from Theorem 24, let \(U\subseteq V(H)\) consist of its edge orbits, and put
\[
\mathcal B_R=\delta_H(U).
\]

**Theorem 25 (bond descent on the connector witness family).** Let \(1\le\ell=|E(R)|\le n-2\). Then \(\mathcal B_R\) is a bond of \(H\), hence a circuit of its cographic matroid, and
\[
\boxed{|\mathcal B_R|=2\ell(n-2)+2.}
\]
Let \(c\) be any antipodally odd coloring whose switch set contains \(S\). Flip the colors of all cube-edge orbits in \(U\), obtaining another antipodally odd coloring \(c'\). On every projective Petrie cycle \(C\) supplied by Theorem 24,
\[
\boxed{D_{c'}(C)=D_c(C)-2.}
\]
Thus one legal bond move decreases completed cyclic variation simultaneously throughout this Cartesian product of zero-cost arm choices.

*Proof.* The projective connector edge orbits induce a path with \(\ell\) vertices in \(H\): nonconsecutive connector edges cannot share an endpoint, and their lifts cannot meet antipodally because the connector has length less than \(n\). Hence \(H[U]\) is connected and has \(\ell-1\) edges.

To see that \(H[V(H)\setminus U]\) is connected, remove the \(\ell\) connector edges from \(G\). The folded cube contains a spanning \((n-1)\)-cube, obtained by choosing one representative with a fixed vertex bit and using the other \(n-1\) dimensions. A \(d\)-cube remains connected after deletion of fewer than \(d\) edges; its edge connectivity is \(d\), as follows by induction from its two \((d-1)\)-cube halves and their perfect matching. Since \(\ell\le n-2\), the spanning cube remains connected after the removals. Consequently \(G\setminus E(R)\) and its line graph are connected. Both shores of \(\delta_H(U)\) therefore induce connected graphs, making it a bond.

Every vertex of \(H\) has degree \(2(n-1)\). Subtracting twice the \(\ell-1\) internal edges of \(H[U]\) gives
\[
|\delta_H(U)|=2\ell(n-1)-2(\ell-1)=2\ell(n-2)+2.
\]

Flipping the orbit colors in \(U\) toggles precisely the comparisons in \(\delta_H(U)\), which is the legal cut-space move identified by the cographic switch-change theorem. On each cycle in the witness family, the connector is one contiguous block of edge observations. No observation in either arm belongs to \(U\), because its dimension is outside \(K\). The bond therefore meets this cycle in precisely its two connector-end turns. Both are retained and hence are switches of the containing coloring \(c\); the flip changes both from one to zero and leaves every other cyclic comparison unchanged. This proves the decrease by two. \(\square\)

If \(D_c(C)=3+2r\), the moved coloring has cyclic count \(1+2r\), and its best rotation has \(2r\) color changes. In particular, \(r=0\) gives a monochromatic full geodesic for the moved coloring. This is a legal variation-descent statement; a conclusion for the original coloring still requires controlling restoration of the connector colors or coupling this descent with another witness family.

The root-arm analysis therefore ties the hereditary criticality argument to the existing cographic matroid through a specified bond and a batch of complete geodesic witnesses. A single-cycle argument permits a \((1,1)\) transport region; the linked research note gives a realizable example. The global critical witness distribution remains the additional ingredient needed for a universal existence theorem.


## Global sensitivity of a connector bond

The bond in Theorem 25 has controlled effects even on Petrie cycles outside its certified witness family. The control comes from dimension simplicity, rather than from the size of the bond.

**Theorem 26 (connector intersection rigidity and sharp run bound).** Let \(R\) be any cube geodesic of length \(1\le\ell\le n-2\), and let \(U\) be its projective edge observations. For a projective Petrie cycle \(C\), mark the edges of \(R\) whose orbits belong to \(C\). The resulting binary word has no occurrence of \(101\). Its runs of ones are precisely the connected portions of \(C\cap U\) in the observation cycle. Consequently, if \(r_R(C)\) denotes their number,
\[
\boxed{r_R(C)\le\left\lceil\frac{\ell}{3}\right\rceil.}
\]
The bound is attained for every permitted \(\ell\).

*Proof.* Suppose \(C\) contains the outer edges of three consecutive connector edges, in dimensions \(a,b,c\). Delete those outer edges from \(C\). The two remaining arcs use neither \(a\) nor \(c\). Their endpoints must therefore be paired so that their projective differences have representatives avoiding both dimensions. A cross pairing of an inner connector endpoint with the opposite outer endpoint has difference \(a+b\) or \(b+c\); its complement contains the other forbidden dimension. Such pairings are impossible. Hence the two inner endpoints are paired. Their difference is \(b\), whereas its complement contains both \(a,c\). Dimension simplicity forces their connecting arc to be the single \(b\)-edge. The middle connector edge therefore belongs to \(C\), excluding \(101\).

The induced graph \(H[U]\) is the connector observation path, as established in Theorem 25. Consecutive selected connector edges are consecutive observations of \(C\), since they meet at their common cube vertex. Conversely, observations from different runs cannot be adjacent in \(C\), since they are not adjacent in \(H[U]\). Thus the two run counts agree. Between runs there are at least two zero entries, so \(r\) runs require at least \(r+2(r-1)=3r-2\) entries. This proves the bound.

For sharpness take \(R\) to be the first \(\ell\) edges of the full geodesic with dimension order \(1,\ldots,n\). Put \(r=\lceil\ell/3\rceil\). Starting at the same root, interchange dimensions at positions \(2,3\), then \(5,6\), and so on through the first \(r-1\) such pairs. Each interchange replaces precisely those two cube edges and returns to the same vertex after the pair. The unchanged connector edges have \(r\) runs, separated by the replaced pairs; their projective orbits do not acquire additional coincidences. Indeed every observation retains its direction, and each replaced edge differs from the original edge of that direction in one other vertex bit, rather than in all \(n-1\) other vertex bits. The completed Petrie cycle attains the bound. \(\square\)

**Corollary 27 (global switch-grade sensitivity).** For an antipodally odd coloring define its Petrie grade by
\[
g_c(C)=\frac{D_c(C)-1}{2}.
\]
Flip the edge orbits of a connector \(R\), obtaining \(c'\). Let \(a_R(C)\) count the original switched comparisons in \(\delta_H(U)\cap C\). Then
\[
\boxed{g_{c'}(C)-g_c(C)=r_R(C)-a_R(C),\qquad
|g_{c'}(C)-g_c(C)|\le\left\lceil\frac{\ell}{3}\right\rceil.}
\]
In particular every connector of length at most three induces a legal move changing every Petrie grade by at most one. On the complete witness family of Theorem 24 the grade decreases by one.

*Proof.* Each observation run has two boundary comparisons, giving \(|\delta_H(U)\cap C|=2r_R(C)\). Toggling these comparisons changes \(D_c(C)\) by \(2r_R(C)-2a_R(C)\). Since \(0\le a_R(C)\le2r_R(C)\), Theorem 26 gives the bound. On a certified cycle there is one run and both boundary comparisons are switches. \(\square\)

**Corollary 28 (short connector choice at a critical cycle).** Every three-turn retained witness cycle has a connector bond which decreases its completed grade by one, together with its associated independent-arm witness family, and satisfies
\[
|g_{c'}(C')-g_c(C')|
\le
\left\lceil\frac{\lfloor n/3\rfloor}{3}\right\rceil
\]
for every Petrie cycle \(C'\).

*Proof.* The three edge distances between consecutive retained turn centers are positive integers summing to \(n\). Choose the shortest, of length \(\ell\le\lfloor n/3\rfloor\), as the connector. Use the third retained turn as \(s\) in Theorems 23–25. Corollary 27 supplies the global bound. \(\square\)

These bounds quantify the compensation required outside a descending witness family. They permit increases on other cycles, so a simultaneous descent principle remains to be proved.

## Shared one-switch Fourier law for both complete-path problems

Fix \(m\ge2\), and write a binary color word as spins \(t_j=(-1)^{w_j}\). Let \(G_m(t)\) be the indicator that the word has at most one adjacent color change.

**Theorem (universal Fourier formula).**
\[
G_m(t)=2^{-m}\sum_{k=0}^{m-1}\left[
\prod_{j<k}(1-t_j)\prod_{j\ge k}(1+t_j)
+\prod_{j<k}(1+t_j)\prod_{j\ge k}(1-t_j)\right].
\tag{UF1}
\]
Its coefficient at the squarefree monomial \(\prod_{j\in S}t_j\) is zero for odd \(|S|\), and for even \(|S|\) equals
\[
\boxed{2^{1-m}\sum_{k=0}^{m-1}(-1)^{|S\cap\{0,\ldots,k-1\}|}.}
\tag{UF2}
\]
Consequently \(\deg G_m\le d_m=2\lfloor(m-1)/2\rfloor\).

*Proof.* The first summand at \(k=0\) lists the two constant words, and the summands indexed \(1\le k<m\) list the two complementary two-block words with a single switch at \(k\). Each listed word occurs once, and no other word occurs. This proves (UF1). In its multilinear expansion, each complementary pair cancels on odd-degree monomials. For even \(S\), the common monomial sign in the \(k\)-th pair is \((-1)^{|S\cap[0,k)|}\), proving (UF2). If \(m\) is odd, degree \(m\) vanishes by parity. For even \(m\), the degree-\(m\) coefficient is proportional to \(\sum_{k=0}^{m-1}(-1)^k=0\). The largest remaining possible degree is \(d_m\). \(\square\)

**Theorem (common restoration identity).** Let \(\Omega\) carry a free involution \(J\), and let legal colorings satisfy \(c(Jo)=1-c(o)\). Suppose every member \(P\) of a family \(\mathscr P\) reads \(m\) observations from distinct \(J\)-orbits. Put
\[
H(c)=\sum_{P\in\mathscr P}G_m((-1)^{w(P)_0},\ldots,(-1)^{w(P)_{m-1}}).
\]
As a function of one independent spin per observation orbit, \(H\) has Fourier degree at most \(d_m\). For any \(r>d_m\) distinct orbits \(q_1,\ldots,q_r\), and writing \(c^U\) for the legal coloring with orbits indexed by \(U\) flipped,
\[
\boxed{\sum_{U\subseteq[r]}(-1)^{r-|U|}H(c^U)=0.}
\tag{UF3}
\]

*Proof.* Distinct observation orbits on each path make (UF1) a multilinear polynomial in distinct global variables, up to fixed signs from the choice of lifts. The degree bound survives summation. Iterated Boolean finite differences in more than \(d_m\) variables annihilate every monomial, giving (UF3). \(\square\)

**NORI1 encoding.** Take \(\Omega=E(Q_n)\), \(J(e)=\bar e\), and all undirected antipodal geodesics, each reading \(m=n\) distinct direction orbits. Root sliding converts an at-most-one-switch word into a monochromatic geodesic. If \(F_n(c)\) counts monochromatic-zero unoriented antipodal geodesics, then
\[
\boxed{H_{Q_n}(c)=2nF_n(c).}
\tag{UF4}
\]
Indeed each projective Petrie cycle of twisted variation one has \(2n\) full geodesic windows, all with at most one switch, and one monochromatic-zero window. A cycle with higher odd variation has neither.

**Boundary-tournament encoding.** Take \(\Omega\) to be ordered triples of distinct vertices, \(J(abc)=cba\), and \(\mathscr P=S_n\), the Hamilton vertex orders. Their \(m=n-2\) consecutive triple windows have distinct middle vertices, preserved by reversal, so they lie in distinct \(J\)-orbits. Consequently
\[
\boxed{H_{\mathrm{BT},n}(c)=\sum_{\pi\in S_n}G_{n-2}(w(\pi)),\quad
\deg H_{\mathrm{BT},n}\le d_{n-2},}
\tag{UF5}
\]
and (UF3) governs its legal triple-pair recolorings. Both original existence problems are therefore nonvanishing assertions for the *same one-switch polynomial* on two path-incidence systems.

**Switch-bound distinction and closure scope.** The at-most-two-switch indicator need not share this degree drop: on four bits, its top Fourier coefficient is \(-1/8\), because its only excluded words are \(0101\) and \(1010\). This distinguishes the former higher-face two-switch objective algebraically. The common Fourier law remains an incidence-blind necessary structure; an unrestricted nonvanishing theorem requires further hypotheses linking overlapping paths, thereby excluding the higher-face obstructions.

### Even-repair compensation at a zero of the path-count polynomial

**Corollary (cross-orbit compensation).** In the setting of the shared low-degree theorem, suppose \(H(c)=0\). Take any \(r>d_m\) distinct observation orbits \(R=\{q_1,\ldots,q_r\}\). Then
\[
\boxed{
\sum_{\substack{U\subseteq R\\|U|\ {\rm even}\\|U|\ge2}}H(c^U)
=
\sum_{\substack{U\subseteq R\\|U|\ {\rm odd}}}H(c^U)
\ge\sum_{q\in R}H(c^{\{q\}}).
}
\tag{UF7}
\]
Consequently if at least one singleton flip in \(R\) creates a favorable complete path, some even-cardinality collection of at least two flips in \(R\) also creates one. Moreover at least one such collection has path-count at least
\[
\frac{\sum_{q\in R}H(c^{\{q\}})}{2^{r-1}-1}.
\tag{UF8}
\]

*Proof.* Equation (UF3) states that the sum over even \(U\) equals the sum over odd \(U\), irrespective of the parity of \(r\). The empty even subset contributes \(H(c)=0\), and every other path count is nonnegative. The odd sum includes all singleton subsets, proving (UF7). There are \(2^{r-1}-1\) nonempty even subsets. Averaging gives (UF8). \(\square\)

For NORI1 one may select \(r=n-1\) distinct edge orbits when \(n\) is even, or \(r=n\) when \(n\) is odd; choosing distinct directions avoids automatic same-direction affinity. For boundary tournaments the same statement holds with \(r>d_{n-2}\) distinct ordered-triple reversal orbits. This gives a shared higher-order compensation mechanism among legal repairs. It does not prescribe which even subset heals, nor guarantee a two-pair repair: the cancellation may be distributed among larger subsets.

## Quadratic Fourier overlap law for boundary 3-tournaments

Let \(n\ge5\), \(m=n-2\). An ordinary boundary 3-tournament colors ordered triples of distinct vertices, with \(c(c,b,a)=1-c(a,b,c)\). Choose a representative from each reversal pair of triples \(q\) and let \(s_q=(-1)^{c(q)}\). The number
\[
H_n(c)=\sum_{\pi\in S_n}\mathbf1\{\text{the }m\text{ consecutive triple colors along }\pi
\text{ have at most one switch}\}
\]
is a multilinear polynomial in these independent spins. Its Fourier degree is at most \(2\lfloor(m-1)/2\rfloor\).

Two reversal pairs \(q,r\) form a *four-chain* if they admit orientations \((a,b,c),(b,c,d)\) on four distinct original vertices. They form a *five-chain* if they admit orientations \((a,b,c),(c,d,e)\) on five distinct original vertices. Either chain comes with the signed product \(\varepsilon_{q,r}\) of the two orientation signs relative to the selected representatives. Simultaneous reversal of the entire chain negates both signs, so their product is well defined.

**Theorem (signed two-triple kernel).** The constant coefficient of \(H_n\) is \(n!m/2^{m-1}\), its odd Fourier degrees vanish, and the quadratic coefficient of two distinct reversal orbits is
\[
\boxed{
\widehat H_n(\{q,r\})=
\begin{cases}
\varepsilon_{q,r}\,2^{2-m}(m-1)(m-2)(n-4)!,&\text{four-chain},\\
\varepsilon_{q,r}\,2^{2-m}(m-2)(m-4)(n-5)!,&\text{five-chain},\\
0,&\text{all other pairs}.
\end{cases}}
\tag{BTK1}
\]
The two chain cases have different numbers of shared original vertices and are mutually exclusive. In particular, disjoint triple supports have zero quadratic coefficient.

*Proof.* The universal one-change word indicator has constant Fourier coefficient \(m/2^{m-1}\) and two-position coefficient
\(2^{1-m}(m-2(q-p))\) at positions \(p<q\). Sum these over the \(n!\) Hamilton vertex orders; odd degrees cancel under global color complementation.

Two triple windows in one Hamilton order overlap in two original vertices if their starting positions differ by one, in one endpoint if those positions differ by two, and in none if they differ by at least three. Hence two reversal orbits sharing two vertices can co-occur only if they form a four-chain. Each such chain has \(m-1\) possible starting positions and \((n-4)!\) orders of the remaining vertices. Its reversed chain has the same spin-product sign. The gap-one coefficient \(2^{1-m}(m-2)\) times this twofold count yields the first case.

Two orbits sharing a single original vertex can co-occur only when that vertex is an endpoint of both triples, giving a five-chain at position gap two. There are \(m-2\) starting positions, \((n-5)!\) residual permutations, and two reversed chain orientations with the same spin-product sign. The gap-two coefficient is \(2^{1-m}(m-4)\), giving the second case.

Two different reversal orbits supported on the same three vertices cannot both appear in a Hamilton order, since two distinct overlapping windows use at least four vertices. Incompatible one- or two-vertex overlaps likewise cannot co-occur. For disjoint triple supports, at every permitted pair of positions all four independently chosen triple orientations have equal multiplicity, and their spin-product signs sum to zero. This proves the remaining case. \(\square\)

**Corollary (six-vertex polynomial).** At \(n=6\) the word length is \(m=4\). The five-chain coefficient is zero and the polynomial has degree at most two. With \(t_{abc}=(-1)^{c(a,b,c)}=-t_{cba}\),
\[
\boxed{H_6(c)=360+\frac32\sum_{\substack{a,b,c,d\\\text{pairwise distinct}}}t_{abc}t_{bcd}.}
\tag{BTK2}
\]
Each four-chain pair appears in the ordered quadruple sum twice, via reversal. For \(n=5,6,7,8\), the unsigned four-chain coefficients are \(1,3,9,30\), respectively, and the five-chain coefficients are \(-1/2,0,3/4,3\), before their orientation signs. Independent exhaustive enumeration of Hamilton orders through eight vertices verifies these values and the zero cases.

**Interpretation.** This gives the boundary-tournament counterpart of the cube's factorial quadratic Fourier kernel. Both arise from the same one-change word polynomial. The cube kernel measures signed Hamming separation between direction-distinct edges; the boundary kernel records the four-vertex and five-vertex overlaps of ordered triple windows. The resulting support difference is a constraint on any shared positive-certificate strategy. Higher even Fourier degrees remain when the word length exceeds four.


## Two usage-class completion and the missing interleaving clauses

The shared one-switch polynomial and the restoration fans have a Boolean counterpart retaining complete-path incidence. It gives a precise closure target and clarifies the role of Article XIV's local joining-square constraints.

**Theorem (two-class avoidance is 2-SAT).** Let complete paths read at most one observation orbit from each of two selected usage classes. Fix all other orbit colors, and let the selected colors vary freely, respecting the involution's coloring relation. For any specified success predicate on full color words, the legal completions avoiding successful complete paths are the solutions of a 2-CNF formula.

*Proof.* A given path depends on at most two adjustable Boolean variables. List its successful assignments, at most four. Forbid each such assignment with a clause asserting that at least one accessed variable differs. The clause has at most two Boolean tests. A successful path with no adjustable variables gives an empty clause; one adjustable variable gives a unary clause. Conjoining over complete paths is equivalent to avoidance. \(\square\)

**Cube specialization.** Select two distinct directions \(a,b\) of \(Q_n\), \(n\ge3\), and fix a legal antipodally odd coloring of all other directions. Give the antipodal edge orbits of direction \(a\) variables \(X_e\), and those of direction \(b\) variables \(Y_f\), choosing one lift of each as representative.

For a full geodesic, its \(n-2\) fixed observations must all have a common color \(t\) to permit a monochromatic completion. When they do, let its two adjustable colors be \(X_e+\epsilon_e\) and \(Y_f+\epsilon_f\), where the lift signs \(\epsilon_e,\epsilon_f\) are fixed. Its avoidance clause is
\[
\boxed{
(X_e\ne t+\epsilon_e)\ \lor\
(Y_f\ne t+\epsilon_f).
}
\tag{TC1}
\]
If the fixed observations have both colors, that path gives no clause. The resulting formula \(\Psi_{a,b}\) has only binary clauses between the two direction classes. A completion is a NORI1 counterexample precisely when it satisfies \(\Psi_{a,b}\).

Therefore NORI1 is equivalent to universal unsatisfiability of these formulas for every legal partial coloring. In implication-graph language this requires a signed variable and its negation to lie in one strongly connected component. The underlying variable classes alternate along every implication path.

**Boundary specialization.** Select two middle symbols \(a,b\) of an ordinary reversal-odd boundary tournament, and vary the reversal-orbit colors of triples centered at those symbols. A Hamilton ordering reads at most one triple from each selected class. Apply the theorem with the success predicate “at most one switch.” Its avoidance formula has clause width at most two; unary and empty clauses can occur because a selected symbol may be an endpoint of the ordering. Universal unsatisfiability is equivalent to the full boundary one-switch conjecture.

These are complete-incidence reductions. The usage-class property alone does not prove unsatisfiability: the geometry of the path-generated clauses remains essential.

### What the two-polarity folding contributes

Let \(f\) be a hypothetical least-dimensional odd cube counterexample. For two omitted dimensions \(a,b\), the preceding dimension's NORI1 theorem gives paired roots in every arbitrary opposing face coloring, by the folding equivalence of Article XIV.

At a given corner \(u\), a face certificate of polarity \(t\) excludes a color-\(t\) monochromatic two-step route across its residual \(\{a,b\}\)-square. Thus every such route gives a clause forbidding \(tt\). A paired face root supplies both clauses, requiring the two route colors to differ.

This implies the following four-corner rule:
- A residual square of curvature one has no corner whose parallel complementary face is paired at that root.
- A flat gate permits paired face roots only at its two opposing gate corners. Its adjacent corners have monochromatic diagonal routes and therefore cannot be paired.
- A stripe has bichromatic diagonal routes at all four corners.
- A monochromatic residual square has no paired face root at any corner.

*Proof.* The face-certificate gluing is the two-polarity folding construction. Curvature one means the two diagonal routes from any corner have different color parities, so one is monochromatic. A gate's adjacent-corner diagonals are monochromatic; a stripe's diagonals are all bichromatic. \(\square\)

These clauses concern paths in which \(a,b\) are consecutive. They form only a subformula of \(\Psi_{a,b}\); interleaved placements generate additional clauses.

**Proposition (consecutive-direction avoidance can remain satisfiable in every dimension).** Fix \(n\ge3\), choose \(j\notin\{a,b\}\), and put
\[
\boxed{
c_a(x)=x_j,\qquad c_b(x)=1-x_j,\qquad
c_i(x)=x_a\quad(i\notin\{a,b\}).
}
\tag{TC2}
\]
This coloring is legal and antipodally odd. No monochromatic full geodesic has \(a,b\) consecutive. Nevertheless it has a monochromatic-zero full geodesic.

*Proof.* Without a \(j\)-step between \(a,b\), their colors are opposite, so a monochromatic path cannot traverse them consecutively. Start with \(x_a=1,x_j=0\) and traverse \(a,j,b\), followed by all remaining directions. The first edge is zero, flipping \(a\) makes every fixed-direction color zero, and the \(j\)-step changes \(x_j\) to one, making the \(b\)-edge zero. All remaining colors are zero. \(\square\)

Thus a contradiction obtained solely from residual-square gates cannot be universal. The missing clauses can already be supplied by a third interleaving direction. This agrees with Article XIV's need for full dimension-simple exchange geometry and higher coherence.

### Four-clause inconsistent kernels

**Theorem (two robust orientation paths force a four-clause contradiction).** Fix a partial odd coloring with free directions \(a,b\). In the \(a=0\) facet, suppose a root \(z\) has one full path order of each monotone orientation which succeeds for either value of the color of its traversed \(b\)-edge. All other colors on those paths are fixed. Let \(Y_0,Y_1\) be the two adjustable \(b\)-edge colors read by these orders, and let \(X\) be the color of the \(a\)-bridge over \(z\), after choosing the representative sign accordingly.

Then the full completion formula contains the four clauses
\[
\boxed{
(X\lor Y_0),\quad(X\lor\neg Y_0),\quad
(\neg X\lor Y_1),\quad(\neg X\lor\neg Y_1).
}
\tag{TC3}
\]
They form an inconsistent kernel. Equivalently, they give implication paths
\[
\boxed{\neg X\longrightarrow Y_0\longrightarrow X,
\qquad X\longrightarrow Y_1\longrightarrow\neg X.}
\]

*Proof.* For \(t=0,1\), use the robust facet order of word \(t^*(1-t)^*\). For either value \(q=0,1\) of its \(b\)-edge, split the path at its monotone seam and apply the odd bridge gluing. If the bridge color is \(X=t\), the result is a monochromatic color-\(t\) full geodesic in the original cube. Its two adjustable observations are precisely \(X\) and \(Y_t\); when the \(b\)-step lies in the antipodally moved suffix, its lift sign changes, but its original variable requirement remains \(Y_t=q\).

Avoiding these two paths requires
\[
(X\ne t)\lor(Y_t\ne0),\qquad
(X\ne t)\lor(Y_t\ne1).
\]
For \(t=0,1\) these are the displayed four clauses. The first two force \(X=1\), and the second two force \(X=0\). \(\square\)

**Corollary (common-reader fixed directions force full completion inconsistency).** Fix \(a,b\), and suppose every other direction has color
\[
\boxed{c_i(x)=x_a+\eta_i,\qquad \eta_i\in\mathbb F_2.}
\tag{TC4}
\]
The free directions \(a,b\) may have arbitrary legal antipodally odd colors depending on all permitted bits. Every completion has a monochromatic full geodesic. More strongly, its completion formula has a four-clause inconsistent kernel for every lower-facet root.

*Proof.* On \(a=0\), all directions other than \(b\) have constant colors \(\eta_i\). From any root, traverse the zero-colored directions, then \(b\), then the one-colored directions. This order is nondecreasing for either color of the \(b\)-edge. The order taking the one-colored directions, then \(b\), then the zero-colored directions is nonincreasing for either color. Apply the theorem. \(\square\)

An alternative proof compresses the two offset groups into macro-directions within antipodally stable cosets, reducing to an odd cube of dimension at most four and expanding its monochromatic path. The four-clause proof identifies the contradictory implication kernel directly and uses no finite-dimensional existence input.

An independent completion check found zero full-avoidance solutions among all 16 legal compressed \(Q_3\) completions and all 256 legal compressed \(Q_4\) completions with these prescribed fixed directions. Their consecutive-direction relaxations had respectively two and four solutions. The all-dimensional proof is the four-clause construction.

**Assessment and next closure task.** Article XV now gives critical repairs, directional selector incompatibility, and full completion clauses. Article XIV provides faithful root/order geometry, paired-face gate clauses, curvature-strip constraints, and a sharp chain-tower obstruction calculus. The tower nonvanishing and universal contradictory implication cycle remain unproved.

The four-clause kernel shows how to close a completion formula through interleaving paths. Its robust fixed root is a sufficient certificate; it is unavailable in general, as the one-direction completion Subsection's adaptive-root example demonstrates. The next structural task is therefore to link clauses at different roots into the same pair of opposite implication paths, using criticality and the direction-changing incidence geometry. Local gates supply only part of the formula, and a high topological index cannot be inferred merely from their presence.

## Critical repair intervals and terminal implication blocks

The preceding completion reduction lets us state the consequence of hereditary repair criticality without assuming that it already supplies an inconsistent implication cycle. The distinction between legal orbit recolorings and deletion of retained switches remains important.

Let \(c^0\) be a legal coloring and \(D\) a finite set of observation orbits. For \(S\subseteq D\), write \(c^S\) for the coloring obtained by flipping the orbits in \(S\). Assume
\[
c^D\text{ has no successful complete path},\qquad
c^S\text{ has one whenever }S\subsetneq D.
\tag{CR1}
\]
This is an inclusion-minimal bad interval based at \(c^0\). Such an interval can be selected from a hypothetical bad coloring and any good legal reference: minimize the bad subsets of their difference set.

Choose two usage classes and let \(V\subseteq D\) be the orbits in those classes. Keep all other orbits in their \(c^D\) state. Put \(p_u=1\) when orbit \(u\in V\) is kept in that state and \(p_u=0\) when it is repaired toward \(c^0\). The two-class avoidance formula \(\Phi_V\) has the unique satisfying assignment
\[
\boxed{p_u=1\quad(u\in V).}
\tag{CR2}
\]
Indeed every other assignment corresponds to a proper subset of \(D\). This statement uses only hereditary interval criticality and the two-usage property.

**Theorem (terminal-block characterization of criticality).** A 2-CNF formula satisfied by its all-one assignment has that assignment as its sole model if and only if the following condition holds.

After removing tautologies and repeated Boolean tests, its clauses have the forms
\[
p_u,\qquad p_u\lor p_v,\qquad p_u\lor\neg p_v.
\tag{CR3}
\]
Make a directed graph on the variables by placing an arc \(u\to v\) for every mixed clause \(p_u\lor\neg p_v\). Call \(u\) anchored if \(p_u\) is a unary clause, and mark the pair \(\{u,v\}\) for each positive clause \(p_u\lor p_v\). Then every sink strongly connected component contains an anchor or contains both ends of a marked pair.

*Proof.* A set \(T\) of variables changed to zero satisfies all mixed clauses precisely when it is closed under the directed arcs. It satisfies the remaining clauses precisely when it contains no anchor and contains no marked pair in full.

If a sink component has neither kind of obstruction, changing that component to zero gives another model. Conversely, every nonempty arc-closed set contains a sink component of the whole graph: follow outgoing arcs in the finite condensation graph, which remains inside the set. Under the stated condition that component contains an anchor or a marked pair, so the proposed zero set violates a clause. Hence no nonempty zero set is allowed. \(\square\)

**Corollary (one-sided implication certificates).** Under (CR1), every \(u\in V\) has an implication path
\[
\boxed{\neg p_u\longrightarrow p_u.}
\tag{CR4}
\]
A certificate can be chosen using at most \(2|V|-1\) clause implications.

*Proof.* Follow deletion arcs from \(u\) to a sink component. For a mixed clause \(p_i\lor\neg p_j\), the signed implication graph contains \(\neg p_i\to\neg p_j\) and \(p_j\to p_i\). If the sink has an anchor \(i\), choose a path from \(u\) to \(i\), use the unary implication \(\neg p_i\to p_i\), and reverse the path in positive signs.

Otherwise choose a marked pair \(\{i,j\}\) within the sink. There are directed paths from \(u\) to both \(i\) and \(j\). Use the first path in negative signs, the positive-clause implication \(\neg p_i\to p_j\), and the second path backwards in positive signs. Simple paths have at most \(|V|-1\) arcs each, giving the bound. \(\square\)

### Full-geodesic meaning of the terminal blocks

For the cube, take success to mean a monochromatic full antipodal geodesic. The three clause types have direct witness meanings.

A unary anchor is a full geodesic that becomes monochromatic after repairing one orbit; its other selected-direction orbit is fixed outside \(V\). A mixed clause \(p_u\lor\neg p_v\) records a geodesic becoming monochromatic when \(u\) is repaired and \(v\) is retained. A positive clause \(p_u\lor p_v\) records a geodesic becoming monochromatic when both \(u,v\) are repaired. All its other observations already have the target color.

Thus a terminal component without anchors contains a two-repair witness and chains of one-repair witnesses returning between its repaired orbits. When \(V\) consists of two direction classes, every binary clause joins the classes and every deletion-arc path alternates between them. In particular an unanchored sink has at least two vertices and a directed alternating cycle.

The path supplying a mixed clause has one exceptional edge in the original coloring. In a NORI1 counterexample that edge must be internal: an endpoint exception gives an at-most-one-switch full word and hence a monochromatic root slide. The two-repair witness has two exceptional edges in the original coloring. Its existence does not prescribe their adjacency or the compatibility of its direction order with the one-repair witness orders.

For boundary tournaments, the same terminal-block theorem applies to the at-most-one-switch avoidance formula. Its witness meanings refer to repaired observations making the full word successful, rather than necessarily making it monochromatic.

### Why a return block is not yet a contradiction

**Proposition (criticality and two-class incidence permit arbitrarily long consistent return blocks).** For any even \(r\ge2\), alternate variables \(p_0,\ldots,p_{r-1}\) between two classes and consider
\[
\boxed{
\bigwedge_{i=0}^{r-1}(p_i\lor\neg p_{i+1\bmod r})
\ \land\ (p_0\lor p_1).
}
\tag{CR5}
\]
All clauses join different classes. The formula has no anchors and its sole model is the all-one assignment.

*Proof.* The mixed clauses give one directed cycle. Their implication requirements force every variable to have the same value. The positive clause excludes the all-zero value. \(\square\)

Every nonempty deletion therefore restores a successful assignment pattern for some clause, and every variable participates in a one-deletion witness pattern. Nonetheless the original assignment satisfies the formula. This is an obstruction to a graph-only closure argument, not a claimed realization by cube geodesics or Hamilton orders.

In a consistent critical interval, (CR4) cannot be accompanied by \(p_u\to\neg p_u\): that would contradict its all-one model. Consequently criticality provides the first half of the desired inconsistent cycle, while complete-path geometry must force the other half.

**Revised closure task.** Select an unanchored terminal block, its internal two-repair path, and the alternating chains of one-repair paths. Use their full direction orders, antipodal lifts, and interleaving exchanges to produce a reverse signed implication or a monochromatic path before repair. Anchored blocks require coupling their one-repair paths to other roots instead. Article XIV's joining-square clauses constrain those exchanges but do not by themselves exclude (CR5); its higher chain obstruction also still requires a nonvanishing argument.

This reduction makes the needed coupling finite and dimension-independent in form. It proves neither universal inconsistency nor a switch-matroid exchange axiom. Independent enumeration checked the terminal-block criterion against all 4096 three-variable formulas assembled from the clause types (CR3); the proof above does not rely on that check.


### Endpoint saturation removes a class of binary clauses

Antipodal root sliding gives a clause operation beyond the abstract terminal-block theorem.

**Lemma (endpoint sign saturation).** In the cube's full two-direction completion formula, suppose a clause comes from a full path whose free \(a\)-edge is its first or last edge. Write its mono-completion requirement as \(X=\alpha,\ Y=\beta\). Then the formula also contains the clause with requirement \(X=1-\alpha,\ Y=\beta\). These two clauses together impose the unary constraint \(Y\ne\beta\).

*Proof.* If the path starts with its \(a\)-edge, slide the root one step forward. The new full path removes that first edge and appends its antipodal mate. Its other \(n-1\) edges remain the same, in the same order, and the new \(a\)-edge has the complemented color. The fixed observations retain their common target color, and the \(b\)-edge retains its color. The representative variable for the \(a\)-orbit is unchanged while its required value is complemented. If the \(a\)-edge is last, use the reverse root slide.

The avoidance clauses are
\[
(X\ne\alpha)\lor(Y\ne\beta),\qquad
(X\ne1-\alpha)\lor(Y\ne\beta).
\]
Their conjunction is equivalent to \(Y\ne\beta\). \(\square\)

**Corollary (internal-edge completion core).** The full avoidance formula can be written as
\[
\boxed{\Psi_{a,b}\equiv U_{a,b}\land I_{a,b},}
\tag{CR6}
\]
where \(U_{a,b}\) is a conjunction of unary constraints generated by paths having at least one selected-direction edge at an endpoint, and \(I_{a,b}\) uses paths whose two selected-direction edges are both internal.

*Proof.* Pair each endpoint path with its root slide. Every resulting unary constraint is entailed by the endpoint-path formula, and every endpoint clause is entailed by the corresponding unary constraint. Paths with mixed fixed observations give no clause on either side. Retain all remaining clauses. \(\square\)

If the endpoint constraints force opposite values of one variable, completion closes immediately. Otherwise propagate them through the internal clauses. A surviving unanchored terminal block in a critical repair interval is then generated by internal/internal witnesses. Its two-repair witness and alternating one-repair chains must be coupled in that interior geometry.

This is stronger than observing that a critical defect cannot sit at an endpoint: it removes every clause having either free observation at an endpoint. For \(n=3\) there is no internal/internal path, so the full formula is equivalent to unary constraints alone. For \(n\ge4\), interior interleavings remain. Article XIV's face-gate information constrains consecutive internal placements, while (TC2) continues to show why the full interleaving system must be retained.


### A five-clause closure through two different readers

The endpoint reduction yields a second bounded certificate, without the common-reader hypothesis (TC4).

**Theorem (two uniform reader groups admit arbitrary nonlinear hubs).** Partition the remaining directions into nonempty sets \(J,K\), and prescribe
\[
\boxed{
c_j(x)=1-x_a\quad(j\in J),\qquad
c_k(x)=1-x_b\quad(k\in K).
}
\tag{CR7}
\]
Allow arbitrary legal antipodally odd colors in directions \(a,b\). Every completion has a monochromatic full geodesic. Its full completion formula has an inconsistent kernel of at most five clauses.

*Proof.* Fix any direction-\(a\) edge and let \(B\) be its \(b\)-bit. Construct a full path of order
\[
J,\ a,\ K,\ b
\]
passing through that prescribed edge. Choose its initial \(a\)-bit to be \(B\); choose all other initial bits so that the prescribed edge is read after the \(J\)-steps. Every \(J\)-edge then has color \(1-B\), and every \(K\)-edge has color \(1-B\), since \(b\) has not yet been traversed. The \(b\)-edge is last. Endpoint sign saturation forces the prescribed \(a\)-edge to avoid color \(1-B\). Thus every completion avoiding monochromatic full paths must satisfy
\[
c_a(x)=x_b.
\]
The symmetric construction with order \(K,b,J,a\), and initial \(b\)-bit equal to the prescribed \(b\)-edge's \(a\)-bit, forces
\[
c_b(x)=x_a.
\]

These forced colors already give a monochromatic-zero full path. Start with \(x_a=1,x_b=0\), traverse \(J,a,b,K\), and use any orders within the two groups. Before \(a\), the \(J\)-colors are zero; the \(a\)-color is \(x_b=0\); crossing \(a\) makes the \(b\)-color \(x_a=0\); crossing \(b\) makes all \(K\)-colors zero.

To obtain the bounded kernel, retain this internal path's clause and the two endpoint path pairs forcing its \(a\)- and \(b\)-observations. With representative signs chosen so those observations are \(X,Y\), the five clauses have the form
\[
\boxed{
(\neg X\lor Z),\quad(\neg X\lor\neg Z),\quad
(\neg Y\lor W),\quad(\neg Y\lor\neg W),\quad
(X\lor Y).
}
\tag{CR8}
\]
The first two force \(X=0\), the next two force \(Y=0\), and the last excludes that assignment. Variable coincidences can only shorten the certificate. \(\square\)

**Proposition (the endpoint relaxation can be consistent in every dimension \(n\ge4\)).** In (CR7), set
\[
c_a(x)=x_b,\qquad c_b(x)=x_a.
\tag{CR9}
\]
Every monochromatic full geodesic has one of the orders
\[
\boxed{J,a,b,K\qquad\text{or}\qquad K,b,a,J,}
\tag{CR10}
\]
with arbitrary orders within the groups. Hence both selected directions are internal, and the endpoint-only formula is satisfied by (CR9).

*Proof.* Suppose a monochromatic path of color \(t\) traverses \(a\) before \(b\). Its \(a\)-color forces the initial \(b\)-bit to be \(t\); its later \(b\)-color forces the initial \(a\)-bit to be \(1-t\). A \(J\)-edge has color \(t\) only before \(a\), and a \(K\)-edge has color \(t\) only after \(b\). This gives the first order. The opposite relative order gives the second. Since \(J,K\) are nonempty, neither selected direction is an endpoint. \(\square\)

This provides a dimension-uniform model of the closure step: endpoint paths at different roots force colors, and a full internal path couples those forces. The four-clause common-reader certificate and the five-clause two-reader certificate therefore realize two distinct ways to contradict the completion formula. Arbitrary fixed colorings need not admit either certificate; their remaining internal implication blocks still require a general coupling theorem.


## Bridge-variable resolution couples the two implication reductions

The one-direction paired-root formula and the two-direction odd-cube formula are linked by eliminating a complete class of bridge variables. This supplies a dimension-uniform correspondence between their implication certificates.

Fix arbitrary colors on all directions of \(Q_d\) except direction \(i\), whose edge colors are variables \(X\). Write \(f_X\) for this ordinary facet coloring. Form its odd bridge extension on \(Q_{d+1}\): the lower facet has \(f_X\), the upper facet has edge color \(1-f_X(\bar e)\), and the joining edge above \(u\) has color \(h(u)\), with \(h(\bar u)=1-h(u)\). Choose one representative \(u\) from each antipodal root pair and write \(Y_u=h(u)\).

For a full nondecreasing facet path \(P\) starting at \(u\), let \(L_P(X)\) be its success predicate. Since it uses one direction-\(i\) edge, this predicate is false, true, or a one-variable Boolean test. Put
\[
A_u(X)=\bigvee_{P\text{ full nondecreasing from }u}L_P(X).
\]

**Lemma (bridge-port identity).** A monochromatic full path crosses the bridge above \(u\) precisely when the facet admits a full path from \(u\) of orientation \(h(u)^*(1-h(u))^*\).

*Proof.* For a facet path of that orientation, split at its monotone seam. Reverse the initial segment, traverse the bridge at \(u\), and use the antipodally translated reversed final segment in the upper facet. Its edges all have the bridge's color and its endpoints are antipodal.

Conversely, cut a monochromatic full path at its unique bridge. Reversing its lower horizontal segment and then applying antipodal translation and reversal to its upper segment produces a full facet path from the bridge root. The first segment has color \(h(u)\), the second color \(1-h(u)\). Paths starting in the upper facet give the same conclusion after reversal. \(\square\)

Reversal of an ordinary full facet path exchanges nondecreasing paths from \(\bar u\) with nonincreasing paths from \(u\). Thus the odd completion formula has the equivalent root-pair factorization
\[
\boxed{
\Psi(X,Y)=
\bigwedge_{[u]}
\left[(Y_u\lor\neg A_u(X))
\land(\neg Y_u\lor\neg A_{\bar u}(X))\right].
}
\tag{BR1}
\]
Expanding each \(\neg A\) produces the full two-class clauses associated with the corresponding complete paths.

**Theorem (bridge elimination is paired-root avoidance).** Eliminating all bridge variables gives
\[
\boxed{
\exists Y\,\Psi(X,Y)
\ \Longleftrightarrow\
\bigwedge_{[u]}(\neg A_u(X)\lor\neg A_{\bar u}(X))
\ \Longleftrightarrow\
P(f_X)=\varnothing.
}
\tag{BR2}
\]
After expansion, the middle formula is the one-direction paired-root 2-CNF.

*Proof.* For one root pair, some \(Y_u\) satisfies its two factors if and only if \(A_u,A_{\bar u}\) are not both true. The bridge variables for different root pairs are independent. Both predicates true mean that the same root has opposite monotone witnesses, by reversal. Expanding the middle factor over every pair of successful-path predicates gives
\[
\neg L_P(X)\lor\neg L_Q(X),
\]
where \(P\) starts at \(u\) and \(Q\) starts at \(\bar u\), both nondecreasing. Reverse \(Q\) to recover the ordinary paired-root clause at \(u\). \(\square\)

**Corollary (two-step lifting of every resolved implication).** Suppose a paired-root clause comes from success predicates \(L_P,L_Q\) at the antipodal roots \(u,\bar u\). Its two bridge clauses are
\[
(Y_u\lor\neg L_P),\qquad
(\neg Y_u\lor\neg L_Q).
\]
The resolved implication \(L_P\to\neg L_Q\) lifts to
\[
\boxed{L_P\longrightarrow Y_u\longrightarrow\neg L_Q,}
\tag{BR3}
\]
and the reverse implication lifts through \(\neg Y_u\). Consequently a contradictory implication cycle in the facet formula gives one in the odd-cube formula with at most twice as many steps. Constant success predicates give the corresponding unary or empty clauses.

This correspondence permits the root pair to change at every resolved implication. It therefore requires neither a universally robust root nor a shared direction order across the certificate. In a critical repair interval, the bounded one-sided forcing paths already obtained can be interpreted as chains of paired-root witness clauses and lifted through their individual bridge ports. The missing reverse forcing path remains a geometric obligation.

**Assessment alongside the current updates.** The tree interfaces allow two orders at a shared root; the cyclic overlap results sometimes construct one order for both colorings. Bridge resolution retains the more general two-order structure. The affine twin reduction and rank-three verification close their stated matrix class, while the general paired-root implication formula remains unresolved. The current proof target is a contradictory resolved chain in that formula, using antipodal reversal and full-order exchange to couple different root pairs.

Independent direct enumeration checked the bridge-port identity for 36 unrelated ordinary facet colorings and odd extensions in facet dimensions three and four. The proof and the Boolean elimination above apply in every dimension.


## Non-reader support thresholds from rooted-tree and two-hub closure

The current proof tools imply a stronger necessary condition on an arbitrary NORI1 counterexample than the one-unrestricted-direction theorem alone gives. This is a support reduction valid for unrestricted dependency graphs and arbitrarily large cube dimension.

Call a direction of an ordinary cube coloring a partial-reader direction when its edge-color function is constant or is \(a_i+x_{r(i)}\), \(r(i)\ne i\). A legal odd coloring has no constant direction, so its reader directions are precisely the signed one-bit readers.

**Lemma (one unrestricted ordinary direction).** Let \(f\) color the edges of \(Q_d\). Suppose all but at most one direction are partial readers. If \(k\) is the number of its nontrivial dependency strongly connected components, then
\[
\boxed{|P(f)|\ge2^{d-k}\ge2^{\lceil d/2\rceil}.}
\tag{NS1}
\]

*Proof.* Every partial-reader direction has dependency indegree at most one. Thus every nontrivial strongly connected component has at most one internal branching target. The unique-predecessor graph lemma identifies each such component as a directed cycle or an outward rooted tree with feedback into its root. The rooted-tree feedback theorem makes every fixed-outer fiber at least three quarters favorable. Paired-root fiber gluing contributes a factor \(2^{s-1}\) when a component has \(s\ge2\) directions, and a factor two for a singleton. Multiply over the condensation graph to obtain \(2^{d-k}\). Nontrivial components have at least two vertices, so \(k\le\lfloor d/2\rfloor\). \(\square\)

**Lemma (two unrestricted ordinary directions; computer-assisted).** If all but at most two directions of \(f\) are partial readers, then \(P(f)\ne\varnothing\).

*Proof.* Every component has at most two internal branching targets. Components with at most one are removed using (NS1)'s fiber argument. For a terminal component with two branching targets, the unique-predecessor forest compression reduces each fixed-outer fiber to a two-hub star. Its hub functions may be arbitrary. The published two-hub finite certificate proves that every fiber is at least nine sixteenths favorable. Two such favorable sets intersect after antipodal complementation in at least \(2^{s-3}\) roots. The sink-component gluing lemma therefore removes that component as well. Induct over the condensation graph.

This uses the computer-assisted two-hub majority theorem. The paired-root bound used in the argument is valid; its numerical sharpness is not needed. \(\square\)

**Theorem (two unrestricted odd directions; analytic).** A legal antipodally odd coloring of \(Q_n\), \(n\ge2\), has a monochromatic full antipodal geodesic whenever all but at most two directions are signed one-bit readers. Moreover,
\[
\boxed{F_n(c)\ge2^{\lceil(n-1)/2\rceil-1},}
\tag{NS2}
\]
where \(F_n\) counts unoriented monochromatic-zero full geodesics.

*Proof.* Choose an unrestricted direction \(h\), or any direction if all are readers, and restrict to its lower facet. A reader pointing to \(h\) becomes constant. All other reader directions remain partial readers, and the facet has at most one unrestricted direction. Apply (NS1). The odd bridge-splice theorem gives a monochromatic-zero full path from each antipodal pair of paired facet roots, choosing the unique zero bridge in that pair. Different pairs give different crossing edges. Hence \(F_n(c)\ge|P(f)|/2\), proving (NS2). \(\square\)

**Theorem (three unrestricted odd directions; computer-assisted).** A legal odd coloring with all but at most three directions signed one-bit readers has a monochromatic full antipodal geodesic.

*Proof.* Restrict along one unrestricted direction. Its ordinary facet has at most two unrestricted directions, and the preceding two-target lemma gives paired roots. Apply the free-bridge equivalence. The only computer-assisted input is the existing sharp favorable-root theorem for two-hub stars. \(\square\)

### Consequences for the critical implication search

Let \(s_i(x)=(-1)^{c_i(x)}\) be the direction spin, regarded as an odd Boolean function on the other \(n-1\) bits. Define
\[
E(c)=\left\{i:\sum_{|T|\ge3}\widehat s_i(T)^2>0\right\}.
\]
Oddness removes even Walsh degrees. A Boolean function supported only on singleton Walsh characters is a signed single character, since the degree-two coefficients of its square force all but one linear coefficient to vanish. Thus \(E(c)\) is precisely the set of non-reader directions.

**Corollary (four-direction obstruction threshold).** Every hypothetical NORI1 counterexample satisfies
\[
\boxed{|E(c)|\ge4.}
\tag{NS3}
\]
The threshold three is analytic; excluding three non-reader directions uses the two-hub finite certificate.

Equivalently, arbitrary legal recolorings confined to any three direction classes of any one-reader odd coloring preserve a monochromatic full geodesic. The number of recolored antipodal edge orbits within those classes is unrestricted. A critical bad interval based at a reader coloring must therefore use at least four direction classes.

In the full two-direction formula \(\Psi_{a,b}\), a signed-reader background forces universal inconsistency analytically. A background with at most one additional non-reader direction forces universal inconsistency through the computer-assisted theorem. Any satisfiable two-direction completion formula must consequently have at least two non-reader directions among its fixed observations.

These conclusions strengthen the earlier four- and five-clause families: the controlling reader graph can be arbitrary, with many cycles, incoming trees, and readers pointing to either selected direction. A robust fixed root and a constant-size inconsistent kernel are not assumed.

### Updated path toward closure

The general formula remains unsolved. The proved elimination rules remove singleton, cyclic, rooted-tree, and two-target terminal components. A least-dimensional paired-root obstruction therefore contains a terminal component with at least three internal branching targets. The remaining task is a cross-fiber intersection certificate for such a component, compatible with two different hub tables at the outside seam vertices.

A strict favorable-root majority cannot be the universal certificate: a product of three sharp three-dimensional stars has favorable fraction \((3/4)^3=27/64\) and nevertheless has paired roots. The safe-check and crossed-factor theorems already provide intersections below the majority threshold when suitable root constraints are present. The next closure attempt should extract analogous compatible root constraints from the critical repair witnesses in the three-target component, then use bridge resolution to assemble the resulting root-changing implications.

This is the current proof plan: retain the hereditary repair interval, localize its unresolved implications to a multi-target terminal fiber, and couple its witness orders through root constraints that survive a change of fiber. The new support threshold records how much feedback such an obstruction must contain before that step is needed.


**Independent support-threshold check.** A separate subset-reachability evaluator verified (NS1) for 80 partial-reader colorings with one arbitrary direction in dimensions three through six, including constant directions and multiple dependency components. It computed the dependency components from essential inputs and checked the bound (2^{d-k}) against directly obtained paired-root sets. The support-threshold theorems rest on the analytic component arguments and the stated two-hub certificate, rather than on this sample.


## Dimension induction with boundary parity and interior seams

A dimension induction on paired roots must retain where the deleted direction can be inserted. The lower-dimensional existence statement by itself supplies no control of that insertion port. The following general endpoint criterion identifies one part of the induction that does close.

Let \(f\) be an ordinary edge coloring of \(Q_{d+1}\), split across direction \(h\). Denote its facet colorings by \(g_0,g_1\), and write \(H(y)\) for the edge color in direction \(h\) above the remaining-bit root \(y\). The function \(H\) is arbitrary. Set
\[
C=A_0(g_1)\cap A_1(g_0).
\]

**Theorem (even boundary pair closes an inductive step).** If \(y\in C\) and
\[
\boxed{H(y)=H(\bar y),}
\tag{DI1}
\]
then \(f\) has a paired root. Both witnesses can put direction \(h\) at an endpoint.

*Proof.* If both values are zero, start at \((y,0)\). For the nondecreasing path, cross the zero \(h\)-edge first and then use the \(g_1\) nondecreasing path from \(y\). For the nonincreasing path, use the \(g_0\) nonincreasing path and then cross the zero \(h\)-edge at its endpoint \(\bar y\). The two full words are monotone.

If both values are one, reversal gives \(\bar y\in A_0(g_0)\cap A_1(g_1)\). Start at \((\bar y,0)\). Use the \(g_0\) nondecreasing path followed by its terminal one-colored \(h\)-edge, and the initial one-colored \(h\)-edge followed by the \(g_1\) nonincreasing path. \(\square\)

**Corollary (boundary oddness on cross-favorable roots).** In any paired-root-free ordinary coloring,
\[
\boxed{y\in C\Longrightarrow H(y)\ne H(\bar y).}
\tag{DI2}
\]
Thus an attempted endpoint induction leaves a specified odd boundary profile over its cross-root set.

**Example (interior insertion is necessary even with complete facet profiles).** Take three directions \(a,b,h\) with
\[
f_a=0,\qquad f_b=1,\qquad f_h=x_a.
\tag{DI3}
\]
Both \(h\)-facets have every root paired, and \(C\) is their whole root set. Their horizontal full paths have no monochromatic word. The joining values \(H(y),H(\bar y)\) are opposite.

No root has both orientations witnessed with \(h\) at an endpoint. For a root with initial \(x_a=0\), an endpoint-\(h\) path cannot be nonincreasing: \(h\) first has color zero before the required one-colored \(b\)-edge, and \(h\) last has color one after the required zero-colored \(a\)-edge. With initial \(x_a=1\), the nondecreasing endpoint case fails for the reversed reasons.

Every root of the full cube is nevertheless paired. The orders \(a,h,b\) and \(b,h,a\) produce opposite monotone words from every root. Thus the lifting construction needs an interior seam even when the two smaller paired-root profiles are complete.

### Structural return from the induction attempt

The new adjacent-face result in Article XIV makes the residual boundary condition much stronger in an odd cube. For omitted directions \(a,b\), let \(g_{\alpha\beta}\) be the codimension-two face colorings. If a root belongs to
\[
A_0(g_{01})\cap A_1(g_{00})
\]
or its reverse-orientation counterpart, the residual joining square must be a stripe in a bad coloring. Both transverse direction derivatives vanish there and the two incident direction colors differ.

At a gate, an adjacent face root supports neither orientation. In particular every vertex of Article XIV's monochromatic face corridor becomes a completely empty root in each neighboring translated face. The rooted-tree rootwise coverage theorem therefore constrains those neighboring fibers at the prescribed corridor vertices, rather than only supplying paired roots somewhere else.

The induction has consequently reached a usable obstruction: cross-root ports carry stripe constraints; gate ports force empty adjacent profiles. Critical repair witnesses can be tested against both conditions. A closing exchange must carry a witness through an interior seam, preserve its direction set, and either create a nonstripe cross-root port or assemble opposite implication paths through several bridge ports.

The local cross-interface graph of Article XIV records the first possibility: an odd cycle among its direction pairs produces a monochromatic full path. Full two-direction completion retains the interleaving clauses needed for the second. Neither universal odd-cycle production nor universal opposite-path coupling has been proved.

**Current strategy.** Continue the hereditary repair induction using full direction orders and seam positions. Whenever a proposed witness transport crosses a gate, apply the empty-root rule to the neighboring face; whenever it creates opposite face polarities, apply the stripe rule. The earlier endpoint transport obstruction shows why these positions must remain in the inductive state. This returns the closure search to structural analysis at the first point where the smaller certificates fail to align.
