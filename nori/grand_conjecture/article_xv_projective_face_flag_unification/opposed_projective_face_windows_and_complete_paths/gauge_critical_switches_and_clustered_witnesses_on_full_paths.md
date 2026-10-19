# Gauge critical switches and clustered witnesses on full paths

### Gauge-critical switch cochains and clustered near-good paths

The shared antipodal incidence-cover theorem represents both unrestricted colorings by a switch cochain \(\sigma\) in the prescribed cohomology class \(\alpha\in H^1(H;\mathbb F_2)\) of a connected two-cover \(T\to H=T/J\). The cube case has \(T=L(Q_n)\), where vertices represent cube edges and \(J\) acts antipodally. The boundary-tournament case has \(T=O_n\), where vertices are ordered distinct triples, adjacent if they overlap in two successive symbols, and \(J(abc)=cba\). An admissible complete path never visits both lifts of one quotient vertex: otherwise a cube dimension or a tournament symbol would repeat.

**Theorem 1 (isolated switch deletion is not integrable).** Every quotient edge of either incidence graph \(H\) lies on a cycle. Thus deleting only one switch from a legal switch assignment changes its cohomology class and cannot arise from another legal reversal-odd coloring.

*Proof.* A cube transition between incident edges belongs to the four-edge cycle around a cube square; it projects to a cycle in the quotient line graph (for \(n=2\), two parallel quotient edges form a cycle). An ordered-triple transition \(abc\sim bcd\) belongs to \(abc\sim bcd\sim cda\sim dab\sim abc\), disjoint from its reversed cycle and projecting to a cycle. Hence the quotient graph has no bridges. A single-edge cochain has nonzero integral on a cycle containing that edge, and so cannot be a coboundary. Adding it changes the prescribed class \(\alpha\). QED.

**Theorem 2 (legal gauge cuts and critical witnesses).** Flipping a binary color simultaneously at \(v\) and \(Jv\), leaving other elementary states unchanged, is legal. It modifies the quotient switch cochain by the star coboundary \(\delta\mathbf1_{\{[v]\}}\). Such moves generate all legal representatives of \(\alpha\), modulo overall color complementation.

Fix a switch bound \(t\ge0\). Suppose a coloring minimizes \(|S|\), the support size of its quotient switch cochain, among colorings for which all admissible complete paths have more than \(t\) switches. For any \(U\subseteq V(H)\) satisfying
\[
|S\cap\delta U|>\tfrac12|\delta U|,
\tag{1}
\]
there must be a complete path \(P\) whose switch data in the original coloring satisfies
\[
\boxed{2|S\cap E(P)\cap\delta U|\ \ge\
|S\cap E(P)|+|E(P)\cap\delta U|-t.}
\tag{2}
\]

*Proof.* Two reversal-odd colorings differ by a \(J\)-invariant zero-cochain, which descends to \(H\), so every legal change is a quotient coboundary. Flipping the lifts of \(U\) replaces \(S\) by \(S\triangle\delta U\), reducing the support by (1). By minimizing among bad colorings, the new coloring has some full path \(P\) with at most \(t\) switches. The new switch count along \(P\) equals \(|S\cap E(P)|+|E(P)\cap\delta U|-2|S\cap E(P)\cap\delta U|\), proving (2). QED.

**Corollary 3 (clustered local witnesses).** Suppose a quotient vertex \(z\) has more than half of its incident comparisons marked as switches in such a support-minimal bad coloring. The original coloring has a full path of one of two types:
(i) a path with \(t+1\) switches, including a switch at the path endpoint \(z\);
(ii) a path with \(t+1\) or \(t+2\) switches, including two consecutive switches incident to the internal state \(z\). The case \(t+1\) in (ii) requires \(t\ge1\).

*Proof.* Apply Theorem 2 to \(U=\{z\}\). A complete path visits that quotient state at most once, hence toggling \(z\) alters at most one comparison when \(z\) is an endpoint, or at most two consecutive comparisons when it is internal. Only removal of one switched endpoint comparison or both switched internal comparisons can lower the original count to at most \(t\), producing the stated alternatives. QED.

For NORI1 (\(t=0\)), the witness is a one-switch full geodesic with its switch at an endpoint, or a two-switch full geodesic with adjacent switches around one state. For the boundary one-switch target (\(t=1\)), it is a two-switch Hamilton order with one endpoint switch, or a two-/three-switch Hamilton order with two adjacent switches. The state degrees are \(2(n-1)\) and \(2(n-3)\), so the strict majority thresholds are \(n-1\) and \(n-3\).

**Interpretation.** Critical switch sets must be treated as cohomologically constrained path multitransversals. Isolated switch deletion violates integrability; the legitimate local operations are vertex-star gauges and general cuts. Formula (2) supplies a shared necessary condition that distributes nearly favorable complete paths across any cut with a strict majority of switches. This sharpens the proposed induction-on-switch-count framework without proving either conjecture.

**Theorem 4 (linear versus bounded monodromy length).** In the antipodally folded cube line graph \(H_Q=L(Q_n)/J\), \(n\ge2\), the shortest loop with nonzero double-cover monodromy has length \(n\). In the reversal quotient \(H_B=O_n/R\) of the ordered triple-overlap graph on \(n\ge5\) symbols, such a loop has length at most six.

*Proof.* In any connected graph double cover \(T\to T/J\), the shortest nontrivial-monodromy loop has length \(\min_v d_T(v,Jv)\). For cube edges \(e=\{x,x\oplus e_i\}\) and \(Je=\{\bar x,\bar x\oplus e_i\}\), the closest pair of endpoints has Hamming distance \(n-1\). The distance of distinct edges in the line graph is one more than the minimum distance of their endpoints, giving \(d_{L(Q_n)}(e,Je)=n\). For five distinct symbols \(a,b,c,d,e\), the path
\[
abc\sim bcd\sim cda\sim dae\sim aec\sim ecb\sim cba
\]
uses six valid triple-overlap transitions and ends at the reversal of its first state. Its projected loop has nontrivial monodromy and length six. QED.

**Limitation.** The common switch cohomology class does not retain the full-length condition: cube monodromy loops must grow with dimension, but tournament triple-overlap monodromy loops can use only five symbols in any dimension. The Hamilton vertex-usage and cube dimension-usage restrictions must therefore remain visible in any shared unification.

## Antipodal edge-pair restoration and universal internal pivots

Let \(n\ge2\), let \(\tau\) complement cube vertices, and call an undirected-edge coloring \(c\) legal when \(c(\tau e)=1-c(e)\). Define \(c^{[e]}\) by reversing colors on the two edges \(e,\tau e\). Say that a coloring is *good* if some antipodal geodesic is monochromatic, and *bad* otherwise.

**Lemma (one-change surgery).** If a legal coloring has an antipodal geodesic with at most one color change, it is good.

*Proof.* For a geodesic \(a\to v\to\tau a\) consisting of a color-zero segment followed by a color-one segment, reverse the first segment to run \(v\to a\). Reverse and apply \(\tau\) to the second, obtaining a color-zero segment \(a\to\tau v\). Their concatenation is monochromatic, joins antipodes, and uses each direction once. The opposite color order is symmetric; a constant color word already suffices. \(\square\)

**Theorem (universal internal pivot for a critical antipodal pair).** Suppose \(c\) is legal and bad, while \(d=c^{[e]}\) is good. For each \(b\in\mathbb F_2\), write \(f_b\) for the unique member of \(\{e,\tau e\}\) colored \(b\) by \(d\). Every color-\(b\) monochromatic antipodal geodesic in \(d\) contains \(f_b\) strictly internally. Both colors have such geodesics.

*Proof.* Antipodal complementation maps any monochromatic geodesic to one of the opposite color. Fix a color-\(b\) geodesic \(P\). It uses the direction of \(e\) once and so cannot contain both members of the flipped pair. It also cannot contain the member colored \(1-b\) by \(d\). If \(P\) avoided \(f_b\), then it would still be monochromatic in \(c\), contrary to badness. If \(f_b\) were first or last, the coloring \(c\) would give \(P\) a single color change; the lemma would again contradict badness. Hence \(f_b\) occurs internally in every such \(P\). \(\square\)

**Corollary (critical good–bad boundary).** If a bad legal coloring exists, then there is a good legal coloring \(d\) and a pair \(\{e,\tau e\}\) with the preceding internal-pivot property for both colors.

*Proof.* Legal colorings form a connected hypercube under flips of antipodal edge pairs. A good legal coloring exists: color a selected full geodesic zero, its edge-disjoint antipodal image one, and extend over the remaining edge pairs. Along any pair-flip sequence from this good coloring to a bad one, take the first good-to-bad transition and apply the theorem. \(\square\)

Consequently NORI1 would follow from the *internal-bottleneck exclusion*: every good legal coloring \(d\), for each edge \(f\) of color \(b\), admits some color-\(b\) monochromatic antipodal geodesic that avoids \(f\) or has \(f\) at an endpoint. This is a sufficient condition and is not established here. The argument uses undirected cube-edge colors; it asserts no transfer to boundary tournaments.

## Boolean restoration fans and internal bottlenecks

Fix direction \(i\) of a legal antipodally odd edge coloring of \(Q_{m+1}\). Identify its lower facet with \(Q_m\), with unrestricted coloring \(g\); the upper horizontal coloring is its complemented antipodal image. Let \(S\) be the set of lower endpoints of zero-colored \(i\)-edges. Legality makes \(S\) a selector of antipodal vertex pairs. Put
\[
A(g)=\{y:\exists\text{ a full }y\to\bar y\text{ geodesic with word }0^*1^*\},\qquad P(g)=A(g)\cap\bar A(g),
\]
and let \(M(g)\) denote roots of monochromatic full geodesics.

**Theorem (restoration fan).** A zero-colored antipodal geodesic crossing the \(i\)-edge above \(y\) exists precisely for \(y\in S\cap A(g)\). Such a geodesic can have that edge first or last precisely when \(y\in S\cap M(g)\). In particular the entire legal coloring is good if and only if \(S\cap A(g)\ne\varnothing\).

If the coloring is bad, then \(P(g)=M(g)=\varnothing\) and \(S\cap A(g)=\varnothing\). Of all antipodal edge-pair flips in direction \(i\), precisely \(|A(g)|\) single flips heal it. Denote this set of healing flips by \(H_i\). For any collection \(F\) of flips in direction \(i\), the resulting coloring is good if and only if \(F\cap H_i\ne\varnothing\). Every member of \(F\cap H_i\) contributes a monochromatic full geodesic crossing its distinct restored \(i\)-edge. For a single healing flip, all monochromatic full geodesics in the repaired coloring use the changed pair strictly internally.

*Proof.* Orient a zero-colored full geodesic from the lower to upper facet and let it cross above \(y\). Reverse its lower zero arm and antipodally complement the reversal of its upper zero arm. These form a \(0^*1^*\) full geodesic from \(y\) to \(\bar y\) in the lower facet. Conversely, split any such lower-facet path at the change, reverse its zero arm, cross vertically, and append the antipodal image of the reversed one arm. The two arms use disjoint directions. A vertical endpoint corresponds to an empty arm and thus a constant word. Antipodal symmetry handles paths of the other color. If the legal coloring is bad, the selector avoids \(A(g)\). An antipodal pair wholly inside \(A(g)\) would meet every selector, hence \(P(g)=\varnothing\). Monochromatic full geodesics place both their endpoints in \(A(g)\), hence \(M(g)=\varnothing\). Every member \(y\in A(g)\) is presently excluded from \(S\), while its antipode is selected. Its pair flip introduces precisely that favorable bridge; independent flips of other pairs cannot affect it. This proves the healing formula and the multi-flip statement. With only one healing pair, it is the sole available favorable bridge; since \(M(g)\) is empty, its use is internal. \(\square\)

**Proposition (internal-bottleneck profile).** Within the bridge colorings above a fixed arbitrary \(g\), a good coloring can possess an \(i\)-edge strictly internal to every monochromatic full geodesic of its color if and only if either (i) \(P(g)=\varnothing\) and \(A(g)\ne\varnothing\), or (ii) \(P(g)\) is one antipodal vertex pair and \(g\) has no monochromatic full geodesic.

*Proof.* A common internal zero-edge means there is a selector \(S\) with \(S\cap A(g)=\{y\}\) and \(y\notin M(g)\). Every antipodal pair contained in \(A(g)\) forces a member into the intersection, so there are at most one such pair. If none exists, select one \(y\in A(g)\) and avoid all remaining favorable members; \(M(g)\subseteq P(g)\) ensures the pivot is internal. If there is one such pair, select one of its members and avoid the others. A monochromatic full geodesic, if present, has both endpoints in that unique pair, and conversely its absence makes the chosen witness strictly mixed. Two or more paired-root orbits prohibit a singleton intersection. \(\square\)

This locates the additional obligation in the proposed universal internal-pivot exclusion: paired-root existence alone does not ensure it. The stronger exclusion would also require a monochromatic antipodal geodesic whenever the paired-root set consists of a single antipodal pair.
## Weighted restoration and a bridge generating polynomial

Fix a direction of \(Q_{m+1}\), put an arbitrary two-coloring \(g\) on its lower \(Q_m\)-facet, and put the antipodally complemented coloring on the upper facet. Let \(S\) choose one vertex from each antipodal pair \(\{y,\bar y\}\). Give the vertical edge above \(y\) color zero if and only if \(y\in S\). Write \(C(g,S)\) for the resulting legal coloring, and
\[
W_g(y)=\#\{y=v_0,\ldots,v_m=\bar y:
\text{each direction is used once and the color word lies in }0^*1^*\}.
\]
Let \(N_b(c)\) count unoriented monochromatic antipodal geodesics of color \(b\). Antipodal complementation gives \(N_0(c)=N_1(c)\).

**Theorem (weighted bridge enumeration).** For every \(g,S\),
\[
\boxed{N_0(C(g,S))=\sum_{y\in S} W_g(y).}\tag{WB1}
\]
Consequently, with the product over antipodal vertex pairs in the lower facet,
\[
\boxed{\sum_{S}t^{N_0(C(g,S))}
 =\prod_{\{y,\bar y\}}\bigl(t^{W_g(y)}+t^{W_g(\bar y)}\bigr).}\tag{WB2}
\]
The minimum over legal bridge assignments equals
\[
\boxed{\min_S N_0(C(g,S))
=\sum_{\{y,\bar y\}}\min\{W_g(y),W_g(\bar y)\},}\tag{WB3}
\]
and the maximum has \(\max\) in place of \(\min\). Under independent uniformly random selector choices,
\[
\mathbb E_S N_0=\frac12\sum_y W_g(y),\qquad
\operatorname{Var}_S N_0=\frac14\sum_{\{y,\bar y\}}(W_g(y)-W_g(\bar y))^2.
\tag{WB4}
\]

*Proof.* Orient an unoriented monochromatic-zero full geodesic from the lower facet to the upper facet. It crosses one vertical edge above \(y\in S\). Reverse its lower zero arm, obtaining a zero path starting at \(y\). Reverse and antipodally complement its upper zero arm, obtaining a one path ending at \(\bar y\). They concatenate to a full \(0^*1^*\) geodesic rooted at \(y\). Conversely split any such lower-facet geodesic at the zero/one division, reverse the zero arm, cross above \(y\), and append the antipodally complemented reversal of the one arm upstairs. These constructions are inverse. Constant words use the division at the beginning or end, as appropriate. This proves (WB1). Every antipodal bridge pair makes an independent binary choice of one of its two weights. Multiplying the two-term factors gives (WB2); optimizing each choice gives (WB3). The expectation and variance of an independent choice between weights \(a,b\) are \((a+b)/2\) and \((a-b)^2/4\); summation gives (WB4). \(\square\)

**Corollary (additive repair multiplicity).** If \(C(g,S)\) is bad, then \(W_g(y)=0\) for every \(y\in S\). Let \(F\) be any collection of antipodal vertical edge pairs to flip, and identify a flipped pair by its currently unselected root \(y\). Then
\[
\boxed{N_0(C(g,S)^F)=\sum_{y\in F}W_g(y).}\tag{WB5}
\]
Each summand counts full paths whose sole one-colored edge in the original bad coloring is the edge restored at \(y\). By the one-change surgery lemma this edge is internal. Thus the healing neighbors of a bad coloring carry additive, integer path multiplicities, not just a binary repair indicator.

**Common structure and closure limitation.** Both NORI1 and ordinary boundary tournaments have a free involution on local colored observations and a partition into usage classes such that a complete path reads at most one observation from each class: cube directions in NORI1 and the middle symbol of ordered triples in tournaments. Thus complete-path color-word indicator polynomials are separately affine in the coloring variables of each usage class. The cube identity (WB1) is stronger because its fixed-direction observations separate into two opposite facets. Higher-face counterexamples also retain separate affinity, so it alone cannot force the desired path. The outstanding mathematical step is a nonvanishing relation across *different* usage classes, imposed by their joint local incidence geometry.
## Counterexamples nearest to a perfect cube coloring

Reference distance supplies a different criticality criterion. It is available for any hypothetical NORI1 counterexample, and places no local majority condition on the switch signature.

Fix distinct dimensions \(a,b\) in \(Q_n\), \(n\ge3\). For an edge in direction \(d\), define
\[
(c_0)_d(x)=
\begin{cases}
x_b,&d=a,\\
x_a,&d\ne a.
\end{cases}
\]
This is well-defined on unoriented edges and antipodally odd. It has one switched comparison on every projective Petrie cycle: turns not involving \(a\) compare equal bits, while the two turns at the ends of the unique \(a\)-edge have complementary switch bits \(x_a+x_b\). Thus every Petrie cycle has a monochromatic rotation under \(c_0\).

Write \(V\) for the \(n2^{n-2}\) projective cube-edge observations. Every legal coloring has the form
\[
c_U=c_0+\mathbf1_U,\qquad U\subseteq V,
\]
where both lifts of an observation are flipped. Call \(c_U\) bad if it has no monochromatic full geodesic.

**Theorem 5 (minimum reference distance forces clustered witnesses).** If a bad coloring exists, choose one minimizing \(|U|\). Every proper subset of \(U\) gives a good coloring. More generally, flipping any set \(Q\subseteq V\) satisfying
\[
2|Q\cap U|>|Q|
\]
gives a good coloring.

For each \(e\in U\), there is a full geodesic \(P_e\) on which \(e\) is internal and is the sole edge whose original color differs from the other edge colors. Those other edges all have color \(c_0(e)\). Consequently the original geodesic has two adjacent switches around \(e\), and its projective completion \(C_e\) has three switched comparisons.

*Proof.* A proper subset has smaller reference distance, as does \(U\triangle Q\) under the displayed inequality. Minimality makes both colorings good. In particular restore the observation \(e\) to its reference color and choose a monochromatic full geodesic in the restored coloring. It must contain \(e\), since otherwise it was already monochromatic. Its common color is \(c_0(e)\). In the original coloring only \(e\) on this path has the opposite color.

If \(e\) were an endpoint observation, the original path would have one switch. The antipodal root-slide formula then yields a monochromatic full geodesic in the original coloring, contradicting badness. Thus \(e\) is internal and its two adjacent comparisons are switches. The cyclic completion has the two internal switches plus at most one closing switch; its total is odd and at least three in a bad coloring. Its total is therefore three. \(\square\)

This reduction covers the unrestricted existence problem: any counterexample supplies a counterexample with these witnesses at every changed observation. It does not assert that every bad coloring has this stronger property.

**Proposition 6 (anchored interval structure of each witness).** Cut the observation cycle \(C_e\) at its unique reference switch. In this linear order of its \(n\) observations,
\[
U\cap V(C_e)=I\ \dot\cup\ \{e\},
\]
where \(I\) is a prefix or suffix, possibly empty. If \(I\) is nonempty, at least one unselected observation separates \(e\) from \(I\). If \(I\) is empty, \(e\) is neither endpoint of the linear order.

*Proof.* The reference color word is constant along the chosen linear order. The restored coloring \(c_{U\setminus\{e\}}\) has cyclic variation one on \(C_e\), because the path used in Theorem 5 is monochromatic. Hence the membership word of \(U\setminus\{e\}\) along this order has at most one internal transition. Its ones form a prefix or suffix, including the empty or full possibilities. The full possibility is excluded because \(e\) is not selected after restoration.

If adding \(e\) merely extends that interval, the original membership word still has at most one transition and the original completed variation is one. The same occurs when the interval is empty and \(e\) is an endpoint. Each would contradict badness. This proves both remaining restrictions. \(\square\)

**Proposition 7 (switch compensation under subset repair).** Let \(R\) be a nonempty subset of the minimum-distance set \(U\). Some Petrie cycle \(C\) has variation one after restoring \(R\). Let \(t\) be its unique switched comparison in the restored coloring, and let \(r\) count the cyclic runs of observations in \(R\cap V(C)\). Then
\[
D_{c_U}(C)=
\begin{cases}
2r+1,&t\notin\delta_H(R),\\
2r-1,&t\in\delta_H(R).
\end{cases}
\]
The first case requires \(r\ge1\), and the second requires \(r\ge2\). The original switch set on \(C\) is the symmetric difference of its repair-boundary comparisons with \(\{t\}\).

*Proof.* The repaired coloring is good by Theorem 5, so choose the completion of a monochromatic full geodesic. Its switch set consists of \(\{t\}\). Repair toggles the \(2r\) boundary comparisons of the selected observation runs. Taking the symmetric difference proves the formulas. The original variation is at least three, giving the two lower bounds. The selected observations cannot be empty or the whole cycle, since either gives no boundary comparisons and would leave original variation one. \(\square\)

For a singleton repair the second case is impossible. Thus the two adjacent original switches are forced by completed parity as well as by the monochromatic path witness.

**Corollary 8 (many grade-one cycles in the reduced obstruction).** Let \(Z_1(c_U)\) count distinct projective Petrie cycles with three switched comparisons. For \(n\ge4\),
\[
Z_1(c_U)\ge\frac{|U|}{2}\ge2^{n-3}.
\]

*Proof.* Every observation of \(U\) is healed by its singleton restoration on a grade-one cycle, by Theorem 5. A cycle with three marked comparisons can heal an observation only when both comparisons adjacent to that observation are marked. On an observation cycle of length at least four, three marked comparisons supply at most two such observations. Counting the witness incidences gives \(|U|\le2Z_1(c_U)\).

Furthermore \(U\) meets every Petrie cycle: one disjoint from \(U\) would retain reference variation one. Cube symmetry makes the number of Petrie cycles through each observation constant. Each cycle has \(n\) observations, so double counting incidences with this transversal gives \(|U|\ge |V|/n=2^{n-2}\). \(\square\)

The strict transversal bound established in “Dimension-simple Petrie presentation of the full projective cycle space” further strengthens this to \(Z_1(c_U)>2^{n-3}\). That refinement uses the classification of equality transversals.

### Coupling reference minimality to connector bonds

**Corollary 9 (short reference-improving connectors force a second descent witness).** Let \(c_U\) be the minimum-distance bad coloring above. Let \(Q\) be the projective observations of a geodesic connector of length at most three, with length also at most \(n-2\), and suppose \(2|Q\cap U|>|Q|\). Flipping \(Q\) produces a good coloring. There is an original grade-one Petrie cycle \(C\) such that \(Q\cap V(C)\) is a single nonempty proper observation interval, and both of its boundary comparisons are original switches.

*Proof.* Reference minimality makes the moved coloring good. Choose a cycle whose moved grade is zero. The connector sensitivity theorem in “Cyclic variation selection for antipodal and boundary path galleries” bounds every grade change by one. Original badness makes the original grade at least one, so it is precisely one and decreases by one. The connector intersection has at most one run. It must have one run, and the identity
\[
g_{\mathrm{moved}}(C)-g_{c_U}(C)=r_Q(C)-a_Q(C)
\]
then forces both boundary comparisons to be original switches. \(\square\)

Thus a short connector certified by retained criticality can lower its independent-arm family; when it also improves reference distance, minimality forces a completed grade-one witness somewhere in the Petrie family. Coupling these two witness families, or ruling out their required compensation, remains the unresolved step.
## Connected zero-switch skeletons and the cographic deletion matroid

Let \(p:T\to H\) be either of the connected incidence double covers of Article XV, and let \(\eta\in C^1(H;\mathbb F_2)\) be a legal switch cochain, representing \(w_1(p)\), with support \(S\). Write \(Z=(V(H),E(H)\setminus S)\), and let \(V_1,\ldots,V_c\) denote its connected components. Form a multigraph \(F\) by contracting the \(V_i\) in \(H\), retaining the switched intercomponent edges as links and any switched intracomponent edges as loops.

**Theorem 10 (all legal deletions are cocircuit cuts).** For every \(D\subseteq S\), the following statements are equivalent:
(i) toggling every switch in \(D\) to nonswitch, without adding switches elsewhere, is realizable by another legal odd coloring;
(ii) \(\mathbf1_D=\delta_H f\) for a quotient-vertex function \(f:V(H)\to\mathbb F_2\);
(iii) \(D=\delta_H U\), where \(U\) is a union of connected components of \(Z\);
(iv) \(D\) is the inverse image of a cut of \(F\).

The legal deletion masks form the binary cut space of \(F\), with dimension \(c-1\). Their inclusion-minimal nonempty members are the **bonds**, or graphic-matroid cocircuits, of \(F\). The least size of a nonempty legal deletion is \(\lambda(F)\), the edge-connectivity of \(F\), with no nonempty deletion when \(c=1\).

*Proof.* Removing \(D\) changes \(\eta\) to \(\eta+\mathbf1_D\). Both switch cochains represent \(w_1(p)\) if and only if their difference \(\mathbf1_D\) is a coboundary, proving (i)\(\Leftrightarrow\)(ii). Every graph coboundary is a cut \(\delta_H U\). Requiring \(\delta_H U\subseteq S\) means no nonswitch edge crosses the partition \(U|U^c\), so \(U\) is a union of connected components of \(Z\). This proves equivalence with (iii), and contracting those components proves equivalence with (iv). The graph \(F\) is connected because \(H\) is connected. Standard graphic matroid theory gives the dimension, bond characterization and minimum cut size. QED.

**Corollary 11 (connected monochromatic normal form).** The switch set \(S\) is inclusion-minimal among all legal supports representing \(w_1(p)\) if and only if \(Z\) is connected. Every legal coloring is gauge equivalent to one whose zero-switch graph is connected: choose a spanning tree in \(H\) and apply vertex color-pair flips that cancel every switch along it.

*Proof.* A disconnected \(Z\) gives a nonempty cut \(D\subseteq S\) by Theorem 10; conversely a connected \(Z\) forbids such a cut, so no proper support subset is legal. A gauge potential may be integrated along any spanning tree to make its edges all nonswitching, giving the claimed representative. QED.

**Corollary 12 (monochromatic elementary-state components).** The two induced color-class graphs upstairs in \(T\) are both isomorphic, via \(p\), to the zero-switch quotient graph \(Z\). Hence \(Z\) is connected if and only if both of those color-class graphs are connected.

*Proof.* Above every quotient vertex there is one elementary state of each color. An edge of \(Z\) lifts to an adjacency of states having equal colors, and no switched comparison joins two same-color states. The restrictions of \(p\) identify the two color-class graphs separately with \(Z\). QED.

**Short-cycle deletion certificate.** By the local integration theorem, condition (ii) is equivalent to the vanishing of the parity of \(D\) on every required local motif and on the one covering-odd loop: for cubes these are incidence triangles and cubical squares; for boundary triples at least six symbols these are alternating crown squares and directed sliding quadrilaterals and pentagons, with the crown six-cycles also included at five symbols.

**Limitation.** Inclusion-minimality here is among *all legal odd colorings*, not only bad colorings without favorable complete paths. A gauge-equivalent coloring may acquire such a path. Therefore the theorem identifies the matroid of permissible deletions for any proposed switch-critical induction, but does not assert that a hypothetical minimum bad coloring has connected \(Z\).

## Quotient frustration index and monotone reduction to a connected skeleton

Retain the zero-switch component contraction \(q:H\to F\) from Theorem 10, with all the original switched edges represented in \(F\). Write \(\mathbf1_F\) for the cochain taking value one on every edge of \(F\), including loops.

**Theorem 13 (signed quotient and unavoidable odd cycle).** The canonical covering class satisfies
\[
\boxed{w_1(p)=q^*[\mathbf1_F].}
\tag{15}
\]
Consequently the connected component multigraph \(F\) is nonbipartite, where a loop counts as an odd cycle.

*Proof.* Along any closed walk in \(H\), the original switch cochain \(\eta\) counts each switched edge and ignores each zero-switch edge. Contracting the zero-switch components gives a closed walk in \(F\), whose edge-length parity is the same. This proves (15). The covering class is nonzero since the incidence double cover is connected. If \(F\) were bipartite, \(\mathbf1_F\) would be the cut cochain of its bipartition, hence cohomologically zero, contradicting (15). QED.

**Theorem 14 (maximum-cut optimization of all monotone deletions).** Let \(F\) have \(m\) edges counted with multiplicity and loops. Starting from the given legal coloring, the largest number of switches that can be deleted without creating any new switch is \(\operatorname{MaxCut}(F)\). The smallest remaining number of switches reachable by such monotone deletion is therefore
\[
\boxed{m-\operatorname{MaxCut}(F),}
\tag{16}
\]
the frustration index (minimum edge-bipartization number) of the all-negative signed multigraph \(F\). Every maximum-cut deletion produces a connected zero-switch graph, so its support is inclusion-minimal among *all* legal signatures.

*Proof.* Every monotone legal deletion is, by Theorem 10, a quotient cut \(\delta_F U\); it removes \(|\delta_F U|\) switches and changes no other comparisons. Maximizing the number removed is precisely the maximum-cut problem, proving (16).

To show connectivity, let \(K\) be the spanning subgraph of \(F\) consisting of the edges crossing a fixed maximum cut. Suppose \(K\) is disconnected. Since \(F\) is connected, some edge of \(F\) joins distinct components of \(K\). Such an edge cannot cross the cut, for every crossing edge belongs to \(K\). Flip the cut side of all vertices in one connected component of \(K\). Every crossing edge of \(K\) remains crossing, since both of its ends lie in that component or neither does; every edge joining that component to another was previously noncrossing and now becomes crossing. At least one such edge exists, so the cut size strictly increases, contradicting maximality. Thus \(K\) is connected. The new zero-switch graph is the union of the previous zero-switch components with the crossing edges of \(K\); its contraction is \(K\), so it is connected. By Corollary 11 the remaining signature is inclusion-minimal. QED.

**Implication for criticality.** The matroid of deletion masks has a global optimization interpretation: the entire set of legal monotone deletions is the cut space of \(F\), minimal clusters are its bonds, and the maximal total deletion is a maximum cut. The residual switch count is positive because \(F\) is nonbipartite. For a coloring selected as a minimum-size counterexample *among bad colorings*, these deletions need not remain bad; their resulting favorable full paths are precisely the witnesses constrained by the earlier critical-cut inequality.

## Root-slide sharpening of critical cut witnesses for NORI1

Let \(H=L(Q_n)/J\) be the antipodally folded cube-edge incidence graph, with the canonical switch cochain \(\eta\) of an odd coloring \(c\). Let \(D=\delta_H U\) be a cut whose support lies inside the switches \(S=\operatorname{supp}\eta\). Deleting \(D\) produces a legal odd coloring \(c'\), obtained from \(c\) by complementing the colors of the two antipodal edge states over every quotient vertex of \(U\).

**Lemma 15 (one-switch root-slide elimination).** A full antipodal dimension-simple geodesic with one interior color switch yields a monochromatic full antipodal geodesic for the same coloring.

*Proof.* Write the direction order \(\pi=(i_1,\ldots,i_n)\) and its color word as \(b,\ldots,b,1-b,\ldots,1-b\), changing after position \(j\), where \(1\le j<n\). Let \(y\) be the vertex reached after those first \(j\) steps. The new full dimension order \((i_{j+1},\ldots,i_n,i_1,\ldots,i_j)\), starting from \(y\), traverses the final \(n-j\) edges of the former path and then antipodal copies of its first \(j\) edges. Those copied edges have color \(1-b\) by oddness, so the whole new path is monochromatic. All dimensions are used once. QED.

**Theorem 16 (two-crossing necessity for every legal monotone deletion).** Suppose \(c\) is a hypothetical NORI1 counterexample. Let \(D\subseteq S\) be any nonempty legal deletion cut and let \(c'\) be obtained by deleting it. If \(P\) is a monochromatic full geodesic of \(c'\), then
\[
\boxed{|D\cap E_{\mathrm{turn}}(P)|\ge2,}
\tag{17}
\]
where the intersection counts consecutive elementary-state comparisons along \(P\). Equivalently, the binary gauge membership of the \(n\) consecutive cube-edge states along \(P\) must change at least twice.

*Proof.* Since \(D\subseteq S\), deleting it changes the comparison bit at precisely those turns in \(D\), and nowhere else. The color word of \(P\) in \(c'\) is constant, so the number of switches on the same path in \(c\) is \(|D\cap E_{\mathrm{turn}}(P)|\). If this number is zero, \(P\) is monochromatic for \(c\), a contradiction. If it is one, Lemma 15 supplies a monochromatic root-slide of \(P\) for \(c\), also a contradiction. QED.

**Theorem 17 (the interior-defect witness in a support-minimal bad coloring).** Suppose a hypothetical NORI1 counterexample \(c\) minimizes the total support size \(|S|\) among all bad legal odd colorings. If a quotient elementary-state vertex \(z\in V(H)\) has more than half of its incident comparisons switched, then there is a complete antipodal geodesic \(P\) under \(c\) whose color word is constant except for one **interior** edge with the opposite color, and that exceptional edge represents \(z\). Consequently \(P\) has two consecutive switches in the linear word and its projective Petrie cycle has three switches in total.

*Proof.* Flipping the antipodal elementary-edge pair corresponding to \(z\) modifies the switch support by its vertex-star cut \(\delta\{z\}\). The strict-majority hypothesis makes the support smaller, so by minimal bad-support choice the flipped coloring \(c'\) admits a monochromatic full geodesic \(P\). A full dimension-simple geodesic traverses each quotient elementary state at most once (each dimension occurs once). Thus the vertex gauge at \(z\) changes the color of at most one edge on \(P\), and changes at most two successive comparisons. If that edge is absent, or occurs at either endpoint, \(P\) has zero or one switch for the original coloring \(c\), contradicting Lemma 15 and badness. Therefore the flipped elementary edge occurs strictly inside \(P\); under \(c\) its color differs from that of all other edges of \(P\), producing two neighboring switches.

The projective Petrie cycle formed by the complete path has an additional closure comparison, joining its last edge to the antipodal copy of its first. Since the two endpoint colors of \(P\) in \(c\) are equal, this closure comparison switches, giving three cyclic switches. QED.

**Corollary 18 (local minimality or three-switch Petrie obstruction).** A support-minimal hypothetical NORI1 counterexample has one of two properties: either every quotient elementary-state vertex has switched degree at most half its total degree, or it has a dimension-simple Petrie cycle with precisely three switches, two consecutive and enclosing a single exceptional elementary edge. This dichotomy holds independently of dimension and does not require choosing a special small subcube.

**Boundary distinction.** The root-slide lemma depends on antipodal cube geometry and is unavailable for general boundary ordered-triple colorings. Their one-switch target has the ordinary star-flip witness classification from the preceding part of this Subsection. Therefore the two-crossing principle is a strengthened cube-specific consequence of the common cographic deletion framework, not an assertion that every one-switch boundary Hamilton word can be made monochromatic by cyclic rotation.

## Free bridge colors and a closure route through paired roots

The reference family can be enlarged by freeing one whole dimension. This strengthens repair criticality from one favorable path to a coupled pair in an ordinary cube.

Write \(Q_{d+1}=Q_d\times\{0,1\}\), and let \(f:E(Q_d)\to\mathbb F_2\) be arbitrary. Color a lower edge \(e\) by \(f(e)\) and an upper edge \(e\) by \(1-f(\bar e)\). Color the vertical edge at \(z\in Q_d\) by \(h(z)\), where \(h(\bar z)=1-h(z)\). The resulting edge coloring \(C(f,h)\) is antipodally odd.

For \(b\in\{0,1\}\), let \(A_b(f)\) be the set of roots \(z\) admitting a full geodesic to \(\bar z\) with color word
\[
b^k(1-b)^{d-k}\qquad(0\le k\le d).
\]
Empty blocks are allowed, so a monochromatic path qualifies for both values of \(b\). Reversal gives \(A_1(f)=\overline{A_0(f)}\). Call a root in \(A_0(f)\cap A_1(f)\) a paired root.

**Theorem 19 (universal bridge criterion and fixed-dimension equivalence).** The coloring \(C(f,h)\) has a monochromatic full geodesic if and only if
\[
h(z)=b\quad\text{for some }z\in A_b(f).
\]
Consequently the following are equivalent:
(i) every legal bridge assignment \(h\) gives a monochromatic full geodesic;
(ii) \(f\) has a paired root.
In particular, NORI1 in dimension \(d+1\) is equivalent to the assertion that every binary edge coloring of \(Q_d\) has a paired root.

*Proof.* A full geodesic uses precisely one vertical edge. Orient it from the lower to the upper layer, and suppose this crossing occurs at \(z\), with color \(b=h(z)\). Let \(x\) be its lower starting root. Its lower arm \(x\to z\) has color \(b\). Antipodal reflection of its upper arm gives a lower path \(z'\!:=\bar z\to x\) of color \(1-b\). Reverse both arms and concatenate them as \(z\to x\to\bar z\). They use complementary dimension sets, giving the required word. Reversing this construction proves the converse.

The permitted bridge-color set at \(z\) is therefore \(\{b:z\in A_b(f)\}\). At \(\bar z\) this set is its bitwise complement. If a paired root exists, every choice of its bridge color is permitted. If none exists, choose a bridge color outside the permitted set independently at one vertex from each antipodal pair, and extend by oddness. The complementary-set identity makes both choices forbidden, so this legal \(h\) gives no monochromatic full geodesic.

Finally every antipodally odd coloring of \(Q_{d+1}\) is of the displayed form: its lower layer determines \(f\), its upper layer follows by oddness, and its vertical colors determine \(h\). This proves the fixed-dimension equivalence. \(\square\)

**Lemma 20 (a free-direction perfect reference family).** For every legal \(h\), the coloring \(C(0,h)\) has completed switch count one on every Petrie cycle. Thus all vertical colors can be chosen freely within the perfect reference family.

*Proof.* Root the full geodesic immediately before its vertical edge and cross upward. The vertical edge has color \(h(z)\), and all subsequent upper horizontal edges have color one. The linear comparisons contribute \(1-h(z)\). The closing comparison joins the last upper edge, of color one, to the antipodal vertical edge, of color \(1-h(z)\), contributing \(h(z)\). Their sum is one. \(\square\)

The edge orbits where \(C(f,h)\) differs from \(C(0,h)\) correspond precisely to the one-colored edges of \(f\); no vertical edge is changed. Hence minimum distance from this enlarged family is minimum one-edge count for a coloring without a paired root.

**Theorem 21 (bridge-independent critical repairs).** Suppose NORI1 fails in dimension \(d+1\). Choose \(f\) without a paired root minimizing
\[
m=|\{e:f(e)=1\}|.
\]
For every nonempty subset \(R\) of its one-colored edges, changing all edges of \(R\) to zero yields a coloring \(f_R\) with a paired root. Equivalently, every bridge assignment \(h\) makes \(C(f_R,h)\) good.

*Proof.* Theorem 19 converts a counterexample into a coloring without a paired root. A nonempty repair lowers \(m\), so minimality supplies a paired root. Apply the universal bridge criterion. \(\square\)

This quantifier is stronger than choosing a monochromatic witness after one fixed bridge assignment. The two opposite path orientations occur at one common root, using the same repaired horizontal coloring.

**Proposition 22 (normal form of a singleton critical repair).** Let \(e\) be one-colored in the minimum coloring of Theorem 21, and choose a paired root \(z\) of \(f_e\). At least one of its two orientation witnesses fails when \(e\) is restored to one. One may choose the witnesses so that one of the following holds:

1. A full geodesic from \(z\) is zero-colored in \(f_e\) and has \(e\) as its sole one-colored edge in \(f\). If \(e\) is internal, both orientation witnesses can be chosen as this same path, and both fail after restoration.
2. There is no zero-colored full geodesic from \(z\) in \(f_e\). Precisely one witness contains \(e\); the other avoids it and already supplies the opposite orientation in \(f\).

If both initially chosen witnesses fail upon restoration, the first alternative holds with \(e\) internal.

*Proof.* A pair surviving restoration would make \(z\) paired in \(f\), contradicting its choice. Thus a failing witness contains \(e\). If a zero-colored full geodesic exists from \(z\) in \(f_e\), it contains \(e\), since \(f\) has no monochromatic full geodesic: such a path would make its root paired. This gives alternative 1, including its internal-edge assertion.

Otherwise choose witnesses \(P_0,P_1\) of the two types. If both contain \(e\), both read it as zero. Every path from the same root traverses a given cube edge in the same orientation and with the same set of preceding dimensions. Splice the zero prefix of \(P_0\), through \(e\), with the zero suffix of \(P_1\), after \(e\). Their dimension sets partition \([d]\), giving a zero-colored full geodesic in \(f_e\), a contradiction. Hence precisely the failing witness contains \(e\), proving alternative 2.

For the final assertion, restoring a zero entry in a \(0^*1^*\) word destroys that form only if another zero occurs later. Restoring a zero entry in a \(1^*0^*\) word destroys that form only if another zero occurs earlier. Thus failure of both witnesses forces the common edge \(e\) to be internal. The same splice proves the first alternative. \(\square\)

### Locating the remaining obstruction in directed zero arms

For a root \(z\), direct every edge away from \(z\) by increasing Hamming distance. Let \(F_z(f)\) be the vertices reachable from \(z\) by zero-colored directed paths, and let \(B_z(f)\) be the vertices from which \(\bar z\) is reachable by zero-colored directed paths. Directed paths use each dimension at most once.

**Proposition 23 (zero-arm separation and repair factorization).** In a coloring without paired roots,
\[
F_z(f)\cap B_z(f)=\varnothing\qquad\text{for every }z.
\]
For a repaired edge oriented \(u\to v\), let \(R_0(v)\) be the vertices reachable from \(v\) by original zero-colored directed paths, and let \(L_0(u)\) be the vertices that can reach \(u\) by such paths. Then
\[
F_z(f_e)=F_z(f)\cup
\begin{cases}
R_0(v),&u\in F_z(f),\\
\varnothing,&u\notin F_z(f),
\end{cases}
\]
and
\[
B_z(f_e)=B_z(f)\cup
\begin{cases}
L_0(u),&v\in B_z(f),\\
\varnothing,&v\notin B_z(f).
\end{cases}
\]
In particular, if both opposite orientation types are newly created at \(z\), then \(u\in F_z(f)\), \(v\in B_z(f)\), and repair joins these original zero arms into a zero-colored full geodesic.

*Proof.* A vertex in both sets splices two zero paths into a full zero geodesic, whose root is paired. A new zero path after repair must use \(e\) once. Its prefix ending at \(u\) and its suffix starting at \(v\) use original zero edges. Conversely any such concatenation is directed, and therefore dimension-simple; this proves the formulas.

A newly created \(0^*1^*\) witness must use \(e\) in its zero prefix, since a path avoiding \(e\) survives restoration. Hence \(u\in F_z(f)\). A newly created \(1^*0^*\) witness similarly forces \(v\in B_z(f)\). Joining those arms across \(e\) gives the final conclusion. \(\square\)

**Closure target.** By Theorems 19 and 21, it suffices to exclude a binary cube-edge coloring with disjoint sets \(A_0,A_1\) for which every one-edge repair creates a paired root. Propositions 22–23 divide its critical witnesses into isolated-edge exceptions and a new orientation coupled to an existing opposite orientation. A successful exchange argument must force compatible original zero arms or a surviving opposite path pair at one root. The directed support keeps every splice dimension-simple.

The bridge criterion and its direct doubled-cube interpretation were exhaustively compared for all \(2\), \(16\), and \(4096\) edge colorings of \(Q_1,Q_2,Q_3\), including every legal bridge assignment. The general statements above are proved by the arm decomposition; the universal paired-root assertion remains the closure step.


## Counting counterexample bridge fibers via antipodal root profiles

Use the universal bridge family \(C(f,h)\) of Theorem 19: arbitrary horizontal coloring \(f\) of \(Q_d\), upper-layer antipodal complement, and vertical bits \(h(\bar z)=1-h(z)\). Let \(A_0(f)\) be the roots admitting a complete \(0^*1^*\) geodesic in \(f\). Reversing a full path gives \(A_1(f)=\bar A_0(f)\).

For each antipodal root pair \(P=\{z,\bar z\}\), put \(a(P)=|P\cap A_0(f)|\in\{0,1,2\}\), and let \(N_j\) count pairs with \(a(P)=j\).

**Theorem 24 (bridge-fiber enumeration).** Of the \(2^{2^{d-1}}\) legal assignments of vertical bridge colors, the number producing a cube coloring with no monochromatic full antipodal geodesic is
\[
\boxed{
\#\{h:C(f,h)\text{ is bad}\}=
\begin{cases}
0,&N_2>0,\\
2^{N_0},&N_2=0.
\end{cases}}
\tag{18}
\]
If \(N_2=0\), this count equals \(2^{2^{d-1}-|A_0(f)|}\).

*Proof.* For a representative \(z\) of each antipodal root pair, Theorem 19 permits a favorable full geodesic through its bridge whenever
\[
h(z)\in B_z=\{0:z\in A_0(f)\}\cup\{1:\bar z\in A_0(f)\}.
\]
The set \(B_z\) has size \(a(P)\). If \(a(P)=2\), either legal bridge bit gives a favorable path, eliminating all bad assignments. If \(a(P)=1\), precisely one bit choice forbids a favorable path through that root pair. If \(a(P)=0\), both bit choices forbid it. The bridge bits on different antipodal pairs are independent, so multiplying their numbers of forbidden choices gives the displayed count. If no pair contains two members of \(A_0\), each element of \(A_0\) belongs to a different antipodal pair, proving \(N_1=|A_0|\) and \(N_0=2^{d-1}-|A_0|\). QED.

**Corollary 25 (probability and root-density reformulation).** For uniformly random legal bridge bits \(h\), the probability that \(C(f,h)\) is bad is zero when \(A_0(f)\) contains an antipodal pair, and otherwise
\[
\boxed{\Pr_h[C(f,h)\text{ bad}]=2^{-|A_0(f)|}.}
\]
Thus a hypothetical lower-dimensional coloring with no paired root and larger \(A_0\) creates fewer bad bridge assignments; one with every antipodal pair meeting \(A_0\) on one side gives only one bad assignment. This is a counting refinement of the paired-root criterion, not a proof that a paired root must exist.

## Bridge input supports and minimal influence criticality

Let \(f\) be an arbitrary binary edge coloring of \(Q_d\), \(d\ge1\), and set \(B=A_0(f)\). In its odd bridge extension \(C(f,q)\), the lower facet is \(f\), the upper facet has the complemented antipodal coloring, and the bridge color \(q:Q_d\to\mathbb F_2\) satisfies \(q(\bar x)=1-q(x)\).

For \(x,y\in B\), put
\[
E(x,y)=\{i\in[d]:x_i=y_i\},\qquad
\mathcal E(B)=\{E(x,y):x,y\in B\}.
\tag{BS1}
\]
A set \(S\subseteq[d]\) is a transversal of \(\mathcal E(B)\) if it meets every member. An empty member prevents a transversal. Let \(\pi_S\) denote projection onto the bits indexed by \(S\). Saying that \(q\) depends only on \(S\) permits some bits of \(S\) to be inessential.

**Theorem (bridge input-support criterion).** For every nonempty \(S\subseteq[d]\), the following conditions are equivalent:
1. Some odd bridge function depending only on \(S\) makes \(C(f,q)\) bad.
2. The sets \(\pi_S(B)\) and \(\overline{\pi_S(B)}\) are disjoint.
3. \(S\) is a transversal of \(\mathcal E(B)\).

If these conditions hold, the number of such bridge functions is
\[
\boxed{
2^{\,2^{|S|-1}-|\pi_S(B)|}.
}
\tag{BS2}
\]
If they fail, this number is zero.

*Proof.* The bridge correspondence says that a monochromatic full path through the bridge above \(x\) exists when the facet has a full path of orientation \(q(x)^*(1-q(x))^*\) rooted at \(x\). Reversal gives \(A_1(f)=\bar B\). Therefore badness is equivalent to
\[
q=1\ \hbox{on }B,\qquad q=0\ \hbox{on }\bar B.
\tag{BS3}
\]
For a function depending only on \(S\), these prescriptions descend to \(\pi_S(B)\) and its antipodal image. An odd function on \(Q_S\) extends the prescriptions if and only if those sets are disjoint: assign the forced values there and choose opposite values arbitrarily on every unprescribed antipodal pair. This proves equivalence of the first two conditions.

A projection collision means \(\pi_S(x)=\pi_S(\bar y)\) for some \(x,y\in B\). This holds precisely when \(x_i\ne y_i\) for every \(i\in S\), or \(S\cap E(x,y)=\varnothing\). Its exclusion is the transversal condition. Finally, disjointness makes every member of \(\pi_S(B)\) prescribe one distinct antipodal pair. There are \(2^{|S|-1}\) pairs in total. The remaining pairs have two independent choices each, proving (BS2). \(\square\)

This criterion distinguishes the existence of an odd separating bridge function from the essential input set of a specified function. The latter can contain redundant inputs. Replacing it by a separator on a smaller transversal changes only its direction class.

**Theorem (private agreement witnesses at minimum influence).** Suppose bad legal odd colorings exist in dimension \(n\), and choose one, \(c\), minimizing the number of arcs of its directed influence graph. For a direction \(j\), let
\[
N_j=\{i\ne j:\partial_i c_j\not\equiv0\}
\]
be the essential input set of its edge-color function, and let \(f\) be the ordinary coloring in the facet \(j=0\). Then \(N_j\) is inclusion-minimal among the nonempty transversals of \(\mathcal E(A_0(f))\).

If \(|N_j|\ge2\), then for every \(h\in N_j\) there are roots \(x,y\in A_0(f)\), with full nondecreasing witness paths, satisfying
\[
\boxed{x_h=y_h,\qquad x_i=1-y_i\quad(i\in N_j\setminus\{h\}).}
\tag{BS4}
\]
For \(z=\bar y\), this gives
\[
\boxed{
x\in A_0(f),\quad z\in A_1(f),\quad
x_h\ne z_h,\quad
x_i=z_i\quad(i\in N_j\setminus\{h\}).
}
\tag{BS5}
\]
Moreover,
\[
\boxed{\partial_hc_j(x)=1.}
\tag{BS6}
\]

*Proof.* The coloring \(c\) is the bridge extension of its facet \(f\), with bridge function \(q=c_j\). Oddness makes \(N_j\) nonempty. The preceding theorem makes \(N_j\) a transversal. If a proper nonempty subset were a transversal, replacing \(c_j\) by an odd bad separator depending only on that subset would preserve badness and remove at least one influence arc. No other direction function changes. This contradicts minimality.

For \(|N_j|\ge2\), the nonempty set \(N_j\setminus\{h\}\) is not a transversal. Choose \(E(x,y)\) disjoint from it. Since \(N_j\) itself meets this edge, its intersection with \(N_j\) is precisely \(\{h\}\), proving (BS4). Reversing the nondecreasing full witness from \(y\) gives a nonincreasing full witness from \(z=\bar y\), proving (BS5).

Badness and (BS3) give \(c_j(x)=1\) and \(c_j(z)=0\). Their assignments on \(N_j\) differ only at \(h\). Since \(c_j\) ignores every bit outside \(N_j\), the values at \(x\oplus e_h\) and \(z\) agree. Hence \(\partial_hc_j(x)=1\). \(\square\)

There are no essential input sets of size two for an odd Boolean function: on two bits, its two antipodal values determine one signed bit reader. Thus the second theorem applies in particular to every non-reader direction, whose essential input set has at least three members.

**Corollary (affine rank of the favorable-root projection).** Under minimum influence, let \(N=N_j\), \(k=|N|\ge2\), and \(C=\pi_N(A_0(f))\subseteq\mathbb F_2^N\). Then
\[
\boxed{
\dim\operatorname{aff}_{\mathbb F_2} C
\ge
\begin{cases}
k,&k\ \mathrm{even},\\
k-1,&k\ \mathrm{odd}.
\end{cases}
}
\tag{BS7}
\]
Consequently \(|C|\ge k+1\) for even \(k\), and \(|C|\ge k\) for odd \(k\). When \(k\) is odd, the affine hull is either the full input cube or one of its two total-parity hyperplanes. In particular every nonconstant linear form other than total parity takes both values on \(C\).

*Proof.* Formula (BS4) puts the vectors
\[
w_h=\mathbf1_N+e_h\quad(h\in N)
\]
in the difference span of \(C\). For \(\lambda\in\mathbb F_2^N\),
\[
\sum_h\lambda_hw_h
=\lambda+\left(\sum_h\lambda_h\right)\mathbf1_N.
\]
When \(k\) is even, these vectors are linearly independent. When \(k\) is odd, their sole nonzero linear dependence uses all \(k\) vectors, and their span is the even-weight hyperplane. This proves the rank bounds and the alternatives for the affine hull. A set with affine dimension \(r\) has at least \(r+1\) members. The final assertion follows because the annihilator of the even-weight subspace consists of zero and the total-parity linear form. \(\square\)

**Corollary (non-affine directions force full affine span).** Among bad colorings minimizing the number of influence arcs, further minimize the number of direction-edge functions that are non-affine over \(\mathbb F_2\). Then, for every such non-affine direction \(j\), the projection
\[
\boxed{\pi_{N_j}(A_0(f))}
\]
affinely spans the whole input cube \(\mathbb F_2^{N_j}\). Here affineness concerns the Boolean algebraic normal form; parity on several inputs is affine.

*Proof.* A non-affine odd function has at least three essential inputs. Write \(N=N_j\), \(k=|N|\), and \(C=\pi_N(A_0(f))\). If \(k\) is even, (BS7) gives full affine span. If \(k\) is odd and the affine hull is proper, (BS7) makes it a total-parity hyperplane. Replace \(c_j\) by the affine parity function taking value one on that hyperplane. Since \(k\) is odd, the replacement is odd. It takes value one on \(C\), zero on \(\bar C\), and thus preserves badness by (BS3). Its essential input set is still \(N\), so the number of influence arcs is unchanged. The number of non-affine direction functions decreases, contradicting secondary minimality. \(\square\)

For comparison, if \(c_j=a+\sum_{i\in N_j}x_i\) is affine and \(|N_j|\ge3\), oddness makes \(|N_j|\) odd. Badness places \(C\) in the value-one parity hyperplane, and (BS7) makes its affine hull the whole hyperplane. Thus the rank alternative isolates where affine parity transport can apply and where a non-affine obstruction must carry fully spanning favorable-root data.

**Equivalent elimination rule.** Fix \(h\in N_j\) with \(|N_j|\ge2\). If there are no two nondecreasing facet witnesses satisfying (BS4), then the support criterion constructs a bad odd coloring with direction-\(j\) colors independent of bit \(h\), without adding any influence arc. Consequently a minimal obstruction must supply the private witness pair for every essential input of every non-reader direction simultaneously.

**Scope of the witnesses.** Formula (BS5) prescribes agreement on the other inputs read by \(j\). The roots may differ on bits outside \(N_j\), and their path orders and phase seams can differ. Even when \(N_j=[n]\setminus\{j\}\), so these two roots are adjacent, opposite exclusive orientations alone do not yield paired roots; the neighboring-root obstruction proved below already excludes that inference. The new requirement is their simultaneous occurrence at every essential input under a legitimate minimum-influence choice of the full bad coloring. Coupling these retained paths to the square-flatness witnesses remains a closure problem.

The support criterion and count were independently checked for every antipodal-pair-free subset of \(Q_d\), \(1\le d\le3\), and every nonempty support. All 597 support-count comparisons agreed with (BS2); all 54 private-input incidences for nonsingleton minimal supports in dimension three had witnesses (BS4). These checks support the statements; their proofs are dimension-uniform.


## Root-profile barriers and the middle ranks of a critical pair

The paired-root route requires the paths' color arms and dimension supports. Two simpler closure proposals, based on root density and neighboring root labels, have explicit obstructions.

**Theorem 26 (complete root profile of the parity-reader coloring).** Let \(d=2r\ge2\), and color a direction-\(i\) edge by
\[
f_i(x)=\sum_{j\ne i}x_j\pmod2.
\]
Writing \(|x|\) for Hamming weight, its root sets are
\[
\boxed{
A_0(f)=\{x:|x|=r\text{ or }r+(-1)^r\},\qquad
A_1(f)=\{x:|x|=r\text{ or }r-(-1)^r\}.
}
\]
Their intersection is precisely the middle layer. Hence
\[
|A_0|=\binom{2r}{r}+\binom{2r}{r+1},\qquad
|A_0\cap A_1|=\binom{2r}{r}.
\]
Both densities tend to zero as \(r\) grows. In particular \(|A_0|<2^{d-1}\) for every even \(d\ge8\).

*Proof.* For a dimension order \(\pi\) rooted at \(x\), let \(p=|x|\bmod2\). Its edge-color word is
\[
a_t=p+(t-1)+x_{\pi_t}\pmod2,\qquad1\le t\le d.
\]
To obtain \(0^k1^{d-k}\), the ordered root bits must therefore read \(p+(t-1)\) before the switch and its complement afterwards. If \(k\) is even, both blocks have even length, and precisely \(r\) root bits are one. If \(k\) is odd, both blocks have odd length and each begins with bit \(p\). Thus the weight is \(r-1\) when \(p=0\) and \(r+1\) when \(p=1\). Consistency with the parity of the root weight leaves precisely \(r+(-1)^r\). Conversely, any root with one of these weights supplies the required bit sequence by ordering its zero-bit and one-bit dimensions appropriately. This proves \(A_0\); antipodal reversal proves \(A_1\).

The two binomial densities tend to zero by the central-binomial estimate. More explicitly, put \(s_r=2^{-2r}(\binom{2r}{r}+\binom{2r}{r+1})\). Then \(s_4=126/256<1/2\) and \(s_{r+1}/s_r=(2r+3)/(2r+4)<1\), proving the final assertion. \(\square\)

This is the atomic-stationary family classified in the incidence-cocycle subsection, now with its complete paired-root profile. It has paired roots and monochromatic full paths while most roots eventually have neither one-switch orientation. A universal positive-density lower bound for paired roots, or a greater-than-half bound for \(A_0\), cannot establish closure.

**Lemma 27 (constant-direction extension of root profiles).** Extend any coloring \(f\) of \(Q_d\) to \(Q_{d+k}\) by making its old edge colors independent of the new bits and coloring every new direction by a fixed bit \(c\). Then
\[
A_b(f^{\mathrm{ext}})=A_b(f)\times Q_k\qquad(b=0,1).
\]

*Proof.* Projecting a full geodesic to its old directions deletes entries from its color word, preserving each of the forms \(0^*1^*\) and \(1^*0^*\). Conversely, insert the new constant-colored directions into the appropriate constant block of any old witness, including at an endpoint if that block was empty. This gives a full witness from every root in the corresponding fiber. \(\square\)

**Proposition 28 (adjacent exclusive orientations in every dimension at least four).** For every \(d\ge4\), there is a binary edge coloring with adjacent roots
\[
z\in A_0\setminus A_1,\qquad w\in A_1\setminus A_0.
\]

*Proof.* Begin in \(Q_4\) with the parity-reader coloring of Theorem 26, using bit indices \(0,1,2,3\). Change just the edge \(\{e_0,e_0+e_1\}\) from one to zero. Take \(z=0\) and \(w=e_1\).

At \(z\), every unmodified dimension order has word \(0101\). A full path uses the changed edge precisely when its first two dimensions are \(0,1\), in that order; its new word is \(0001\). Thus \(z\in A_0\setminus A_1\).

Originally \(w\), of weight one, belongs to \(A_1\setminus A_0\) by Theorem 26. A full path from \(w\) uses the changed edge precisely when its first two dimensions are again \(0,1\). Its new word is \(1010\), which creates no \(0^*1^*\) witness. The dimension order \((2,1,0,3)\) avoids that edge and retains word \(1110\), so \(w\in A_1\setminus A_0\). The two roots are adjacent. Apply Lemma 27 for every larger dimension. \(\square\)

This example has many paired roots elsewhere. Its role is to exclude a local rule that adjacent exclusive opposite orientations must already yield a pair at one of those two roots. A closure argument must retain the path witnesses.

**Proposition 29 (separation throughout the middle ranks of a critical repair).** Let \(f\) be the minimum obstruction of Theorem 21. Suppose repairing \(e\) creates a paired root \(z\), with no zero-colored full geodesic from \(z\) in \(f_e\). Let the two witnesses have words
\[
P_0:0^{k_0}1^{d-k_0},\qquad
P_1:1^{k_1}0^{d-k_1}.
\]
Then \(1\le k_0,k_1<d\). At every rank
\[
\min(k_0,k_1)\le t\le\max(k_0,k_1),
\]
their vertices are different. Precisely one witness uses \(e\), and restoring it destroys that witness's orientation.

*Proof.* A one-colored full geodesic in \(f_e\) would also be one-colored in \(f\), since repair only changes one to zero; this would give a paired root in \(f\). By hypothesis there is no zero-colored full geodesic from \(z\). Thus both color blocks in each witness are nonempty.

Suppose the two paths share a vertex of rank \(t\). If \(k_1\le t\le k_0\), splice the zero prefix of \(P_0\) to the zero suffix of \(P_1\). If \(k_0\le t\le k_1\), splice the one prefix of \(P_1\) to the one suffix of \(P_0\). Each splice uses complementary dimension sets, so it gives a monochromatic full geodesic from \(z\). Both possibilities were excluded. Proposition 22 supplies the last assertion. \(\square\)

The critical paired witnesses therefore carry a separated interval of Boolean ranks, together with the single edge whose restoration breaks one orientation and an opposite companion path that avoids it. An intersection at a rank with \(k_0\le t\le k_1\) would give an original one-colored full geodesic and contradict the obstruction. An intersection in the opposite rank order gives a zero-colored repaired geodesic and reduces to the isolated-edge case. The root-profile barriers above show why this requires arm and support data rather than only the roots' labels or their cardinalities.



## Rooted monotone-witness intersection and a spectral closure target

The universal bridge criterion in Theorem 19 converts NORI1 for \(Q_{d+1}\) into a paired-root assertion for an *arbitrary* binary coloring \(f\) of \(Q_d\). This section records a positive integral intersection formula, its Walsh spectral form, and a calibration showing why root density or the first two aggregate moments cannot be a proof invariant.

For a root \(z\), let
\[
P_f(z)=\#\{\pi\in S_d:
\text{the full path from }z\text{ in dimension order }\pi
\text{ has word }0^*1^*\}.
\]
Define
\[
\mathcal I(f)=\sum_{\{z,\bar z\}}P_f(z)P_f(\bar z),
\tag{19}
\]
with the sum over unordered antipodal vertex pairs. Reversing a \(0^*1^*\) full path from \(\bar z\) gives a \(1^*0^*\) full path from \(z\). Consequently
\[
\boxed{\mathcal I(f)>0
\quad\Longleftrightarrow\quad
f\text{ has a paired root}.}
\tag{20}
\]
This is the integral intersection number that the closure route must force to be positive.

**Theorem 30 (antipodal Walsh intersection identity).** Write the normalized Walsh coefficients
\[
\widehat P_f(S)=2^{-d}\sum_{z\in Q_d}
P_f(z)(-1)^{\sum_{i\in S}z_i}.
\]
Then
\[
\boxed{\mathcal I(f)=2^{d-1}
\left(
\sum_{|S|\text{ even}}\widehat P_f(S)^2
-
\sum_{|S|\text{ odd}}\widehat P_f(S)^2
\right).}
\tag{21}
\]
Thus the universal paired-root assertion, and hence NORI1 one dimension higher, is equivalent to strict dominance of the even Walsh energy of the *rooted monotone-witness count* over its odd Walsh energy for every arbitrary \(f\).

*Proof.* The Walsh characters diagonalize the antipodal translation \(z\mapsto\bar z\), with eigenvalue \((-1)^{|S|}\). Parseval applied to the inner product of \(P_f(z)\) and \(P_f(\bar z)\) gives
\[
2^{-d}\sum_zP_f(z)P_f(\bar z)
=\sum_S(-1)^{|S|}\widehat P_f(S)^2.
\]
The unordered antipodal sum in (19) is half the full sum. This proves (21); the positivity criterion (20) proves the equivalence. \(\square\)

The crude sufficient condition \(\operatorname{Var}_zP_f(z)<(\mathbb E_zP_f(z))^2\) would follow by keeping only the constant Walsh term and discarding the positive even nonconstant terms. It is *not* universally valid, even when many paired roots exist.

**Theorem 31 (full rooted multiplicity for the parity-reader coloring).** Let \(d=2r\ge2\), and let
\[
f_i(x)=\sum_{j\ne i}x_j\pmod2.
\]
Put \(q_r=(r+1)(r!)^2\). Then
\[
\boxed{
P_f(z)=
\begin{cases}
q_r,&|z|=r\text{ or }r+(-1)^r,\\
0,&\text{otherwise}.
\end{cases}}
\tag{22}
\]
Therefore
\[
\boxed{
\mathcal I(f)=\frac12\binom{2r}{r}q_r^2>0.}
\tag{23}
\]
If \(p_r=2^{-2r}\bigl(\binom{2r}{r}+\binom{2r}{r+1}\bigr)\) is the fraction of roots having \(P_f(z)>0\), then
\[
\boxed{
\frac{\operatorname{Var}P_f}{(\mathbb EP_f)^2}
=\frac{1-p_r}{p_r}\longrightarrow\infty.
}
\tag{24}
\]

*Proof.* Along an order \(\pi\), the edge colors from a root of weight \(w\), with parity \(p=w\bmod2\), are
\(a_t=p+(t-1)+z_{\pi_t}\pmod2\). To obtain a prescribed monotone word \(0^k1^{d-k}\), the root bits in that permutation must be \(p+(t-1)\) for \(t\le k\) and \(p+t\) for \(t>k\). For an even cut \(k\), the required bit string has weight \(r\), with \(r+1\) possible even cuts. For an odd cut, it has weight \(r-1\) if \(p=0\) and weight \(r+1\) if \(p=1\), giving the permitted other weight \(r+(-1)^r\), with \(r\) possible cuts. Each prescribed bit string of root weight \(w\) occurs under \(w!(d-w)!\) permutations. Therefore \(P_f=(r+1)(r!)^2\) on the middle layer and
\(P_f=r(r+1)!(r-1)!=(r+1)(r!)^2\) on the other permitted layer. Every other root has no witness.

The antipode preserves weight \(r\) and interchanges the other permitted weight with the excluded weight \(r-(-1)^r\). Thus only the \(\binom{2r}{r}/2\) antipodal middle-layer pairs contribute to (19), giving (23). Since \(P_f\) is \(q_r\) times the indicator of a set of density \(p_r\), its squared coefficient of variation is \((1-p_r)/p_r\). The central-binomial estimate gives \(p_r\to0\), proving (24). \(\square\)

**Proposition 32 (unweighted paired-path parity is not a recoloring invariant).** Already for arbitrary binary colorings of \(Q_4\), \(\mathcal I(f)\bmod2\) can change after recoloring. For all-zero \(f\), every root has \(P_f(z)=24\), giving \(\mathcal I(f)=4608\), even. If only the three edges
\[
\{0000,0001\},\quad
\{0000,0010\},\quad
\{0100,0101\}
\tag{25}
\]
have bit one (with bit positions read from the least significant end), direct enumeration of the 24 dimension orders at each root gives
\[
(P_f(0),\ldots,P_f(15))
=(10,16,17,18,14,16,19,18,18,19,21,20,18,22,22,22)
\]
and hence
\[
\boxed{\mathcal I(f)=2571,\quad\text{odd}.}
\tag{26}
\]
Thus a direct mod-two degree based only on unweighted path-pair counts cannot be preserved by arbitrary edge recoloring, even though both colorings have abundant paired roots. A successful topological intersection proof must use supported chains, refined orientations, or a different equivariant index.

**Closure objective.** The bridge criterion reduces the conjecture to proving strict positivity in (21) for every coloring \(f\). The parity-reader family shows that a proof cannot rely on any fixed positive density of good roots or on \(\operatorname{Var}P_f<(\mathbb EP_f)^2\); the nonconstant *even* Walsh levels are essential. The critical-repair separation of Proposition 29 supplies geometric information not represented by the raw overlap (19). A possible next proof is a supported chain lift of this overlap whose nonzero index survives edge recoloring and whose intersections splice into dimension-simple paired roots.



## Transfer determinants for one-edge critical repairs

The preceding spectral overlap formula counts paired-root witnesses globally. We now obtain an edge-local factorization of its underlying rooted monotone path counts. It is valid for every arbitrary edge coloring of \(Q_d\), not merely those satisfying an antipodal relation, and uses only dimension-simple directed paths.

Fix a root \(z\) and orient each cube edge from smaller to larger Hamming distance from \(z\). For vertices \(u,v\), let \(F_{0,z}(u)\) and \(F_{01,z}(u)\) count directed paths from \(z\) to \(u\) whose color words are respectively all zero and \(0^*1^*\). Let \(B_{1,z}(v)\) and \(B_{01,z}(v)\) count directed paths from \(v\) to \(\bar z\) whose words are all one and \(0^*1^*\). Empty paths count once. Define \(F_{1,z},F_{10,z},B_{0,z},B_{10,z}\) similarly for the other word orientation.

**Theorem 33 (signed transfer determinants).** Let \(e=uv\) be an edge of color one, oriented \(u\to v\) away from \(z\), and let \(f_e\) be the coloring obtained by changing only \(e\) to zero. With \(P_f(z)\) the number of rooted \(0^*1^*\) full geodesics and \(Q_f(z)\) the number of \(1^*0^*\) geodesics, one has
\[
\boxed{
P_{f_e}(z)-P_f(z)=
F_{0,z}(u)B_{01,z}(v)
-F_{01,z}(u)B_{1,z}(v),
}
\tag{27}
\]
\[
\boxed{
Q_{f_e}(z)-Q_f(z)=
F_{10,z}(u)B_{0,z}(v)
-F_{1,z}(u)B_{10,z}(v).
}
\tag{28}
\]
The right side of (27) is the determinant of the two path-count vectors
\((F_{0,z}(u),F_{01,z}(u))\) and \((B_{1,z}(v),B_{01,z}(v))\), with the latter's entries ordered as displayed.

*Proof.* All rooted geodesics avoiding \(e\) contribute identically before and after repair. A full geodesic using \(e\) in the original coloring, with \(f(e)=1\), has a \(0^*1^*\) word if and only if its prefix up to \(u\) is \(0^*1^*\) and its suffix after \(v\) is entirely one. Such paths are counted by \(F_{01,z}(u)B_{1,z}(v)\). In the repaired coloring, \(e\) has color zero, so the entire prefix up to \(u\) must be all zero and the suffix after \(v\) may be \(0^*1^*\), giving \(F_{0,z}(u)B_{01,z}(v)\). Every such concatenation is a dimension-simple full geodesic because all pieces increase Hamming distance from \(z\); their traversed dimension sets are disjoint. Subtracting yields (27). The same argument for \(1^*0^*\) words gives (28): the original one-colored edge requires an all-one prefix and a \(1^*0^*\) suffix, whereas after repair the prefix may be \(1^*0^*\) and the suffix must be all zero. \(\square\)

**Corollary 34 (critical empty-root repair and monochromatic arm splice).** Suppose \(P_f(z)=Q_f(z)=0\), but a single repair \(f_e\) makes both positive at \(z\). Then, orienting \(e=u\to v\) away from \(z\),
\[
\boxed{F_{0,z}(u)>0,\qquad B_{0,z}(v)>0.}
\tag{29}
\]
Thus \(f_e\) has a monochromatic zero full geodesic from \(z\) passing through \(e\). In particular, if a critical repair \(e\) produces a paired root but no repaired zero geodesic, that root had at least one monotone orientation already before repair.

*Proof.* Since \(P_f(z)=0\), equation (27) and the positivity of \(P_{f_e}(z)\) imply
\(F_{0,z}(u)B_{01,z}(v)>0\), so its first factor is positive. Similarly (28), \(Q_f(z)=0\), and \(Q_{f_e}(z)>0\) imply \(F_{10,z}(u)B_{0,z}(v)>0\), so its second factor is positive. Concatenate the original all-zero prefix ending at \(u\), the repaired zero edge \(uv\), and the original all-zero suffix from \(v\) to \(\bar z\). All pieces are directed away from \(z\), so each dimension is used once. \(\square\)

**Lemma 35 (the path-count influence kernel).** For any edge \(e\) in direction \(i\), every root \(z\) gives an orientation \(u\to v\) of \(e\) away from \(z\), with \(k=d_{Q_d}(z,u)\). Precisely
\[
\boxed{k!(d-1-k)!}
\tag{30}
\]
complete dimension-simple rooted geodesics from \(z\) contain \(e\). Hence
\[
\boxed{|P_{f_e}(z)-P_f(z)|\le k!(d-1-k)!},
\tag{31}
\]
and summing the influence envelope over all roots gives
\[
\boxed{\sum_{z\in Q_d} k_z!(d-1-k_z)!=2d!.}
\tag{32}
\]

*Proof.* To use \(e\) in a full geodesic from \(z\), the path must first traverse the \(k\) dimensions on which \(z\) and \(u\) differ, then direction \(i\), then the other \(d-1-k\) dimensions. The two outer blocks may be ordered arbitrarily, proving (30). Recoloring \(e\) cannot affect paths avoiding it, giving (31). For a fixed edge and each \(k\), precisely \(2\binom{d-1}{k}\) roots have nearer endpoint distance \(k\). Sum (30) over these roots to obtain \(2\sum_{k=0}^{d-1}(d-1)!=2d!\). \(\square\)

**Closure significance.** In the minimal-one-edge obstruction of Theorem 21, every one-colored edge \(e\) must create a paired root when deleted. Equations (27)--(28) now express the creation of each missing orientation as strict positivity of a **signed rank-two prefix/suffix determinant**. Corollary 34 isolates the only two kinds of critical repair: a new zero full geodesic across \(e\), or a newly repaired orientation paired with an orientation already present in the original coloring. A proof of the unrestricted paired-root lemma would follow from a global coherence/cancellation identity forcing a contradiction among these determinants over all critical edges. Unlike unweighted root-pair parity, the determinants retain direction support and the relative location of the two color blocks; establishing their square-exchange and antipodal coherence is the remaining substantive task.



## Two-state transfer algebra and curvature-twisted square coherence

The rooted transfer determinants above arise from a two-state path automaton. Its rank-two finite differences obey an explicit square-exchange law that keeps every intermediate path dimension-simple.

For a color bit \(b\in\{0,1\}\), put
\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\quad T_1=\begin{pmatrix}0&0\\1&1\end{pmatrix},
\quad B=T_0-T_1=
\begin{pmatrix}1&0\\-1&-1\end{pmatrix}.
\tag{33}
\]
If the successive bits of a directed path are \(b_1,\ldots,b_k\), the scalar
\[
\boxed{(1,1)T_{b_k}\cdots T_{b_1}(1,0)^T}
\tag{34}
\]
equals one precisely when the path word has type \(0^*1^*\), and zero otherwise. In particular
\[
\boxed{T_0^2=T_0,\quad T_1^2=T_1,\quad
T_0T_1=0,\quad B^2=I.}
\tag{35}
\]
The difference of the zero-edge and one-edge transition operators is an involution.

Fix a root \(z\), orient every cube edge away from \(z\), and write \(a\preceq_z b\) when \(b\) is reachable from \(a\) by such a directed path. Define \(\mathscr T_f(a,b)\) as the sum of \(T_{b_k}\cdots T_{b_1}\) over every dimension-simple directed path \(a\to b\), and set \(\mathscr T_f(a,a)=I\). The number of full \(0^*1^*\) geodesics from \(z\) is
\[
P_f(z)=(1,1)\mathscr T_f(z,\bar z)(1,0)^T.
\]

**Theorem 36 (factorized first variation).** For a directed edge \(e=u\to v\), let \(D_e\) denote the formal difference between setting its bit to zero and setting it to one, holding all other edge bits fixed. Then
\[
\boxed{D_e\mathscr T_f(z,\bar z)
=\mathscr T_f(v,\bar z)\,B\,\mathscr T_f(z,u).}
\tag{36}
\]

*Proof.* All paths avoiding \(e\) cancel. Any path containing \(e\) uniquely decomposes into a prefix \(z\to u\), edge \(e\), and suffix \(v\to\bar z\). Its matrix product is suffix times edge times prefix, and the two transition matrices differ by \(B\). Every concatenation is still dimension-simple because its Hamming-distance rank strictly increases. Summing independently over the prefix and suffix families proves (36). \(\square\)

**Theorem 37 (curvature-twisted second variation on every square).** Let \(F\) be any cube square, with bottom \(u\), top \(w\), and intermediate vertices \(v_i=u\oplus e_i,v_j=u\oplus e_j\) under the ordering directed away from \(z\). Denote its two ascending routes by
\[
a=(u,v_i),\ b=(v_i,w),\qquad
a'=(u,v_j),\ b'=(v_j,w).
\]
The *formal* second variations satisfy
\[
\boxed{D_aD_b\mathscr T_f(z,\bar z)
=D_{a'}D_{b'}\mathscr T_f(z,\bar z)
=\mathscr T_f(w,\bar z)\mathscr T_f(z,u).}
\tag{37}
\]
Let \(\Delta_e\) instead denote toggling the original bit of \(e\). Then
\[
\boxed{
\Delta_a\Delta_b P_f(z)
=(-1)^{\kappa_f(F)}\Delta_{a'}\Delta_{b'}P_f(z),
\qquad
\kappa_f(F)=f(a)+f(b)+f(a')+f(b')\pmod2.
}
\tag{38}
\]
The two second variations have the same nonnegative magnitude
\[
\boxed{
K_z(F)=(1,1)\mathscr T_f(w,\bar z)
\mathscr T_f(z,u)(1,0)^T.
}
\tag{39}
\]
Every identity holds for arbitrary cube-edge colorings and every root, with no antipodal hypothesis.

*Proof.* A directed full geodesic containing both edges of a given route must traverse those edges consecutively: after entering the intermediate vertex it cannot return there. The rest of the path consists of an independent prefix \(z\to u\) and suffix \(w\to\bar z\). Two formal bit differences insert \(B^2=I\) between the outer matrix sums, giving the last expression of (37). The alternate square route has the same start, end, prefix and suffix, so gives the same expression. Applying the accepting row and initial column vector yields (39), which is nonnegative since the transfer matrices have nonnegative entries.

For original bit \(b_e\), toggling rather than setting gives
\(\Delta_e=(2b_e-1)D_e\). The two-bit toggle multiplier on one route is therefore \((2b_a-1)(2b_b-1)=(-1)^{b_a+b_b}\). Comparing it with the alternate route gives the ratio \((-1)^{\kappa_f(F)}\), proving (38). \(\square\)

**Corollary 38 (rooted rank-two consistency).** The integer \(K_z(F)\) counts complete dimension-simple geodesics whose colored prefix before \(u\) and colored suffix after \(w\), concatenated while omitting the square's two edge bits, form a \(0^*1^*\) word. It is independent of the two square routes and all four square edge bits. The sole sign discrepancy between the two edge-pair toggle variations is the ordinary square curvature. Since \(\kappa_f=\delta f\), the sign twist obeys the three-cube identity \(\delta\kappa_f=0\). This verifies coherence of the *local signs*, not a root-changing equivariant homotopy.

**Remaining closure task.** The bridge theorem reduces NORI1 to paired-root existence for arbitrary lower-cube colorings. The preceding first-variation determinant describes the repair of each missing path orientation, while Theorem 37 provides the signed rank-two compatibility of those repairs along cubical squares. The missing step is to assemble these rooted matrices with antipodal root reversal into a global chain operation having nonzero Smith-transfer index. Unlike unweighted path-pair parity, the matrices retain both direction support and the two color phases.



## Antipodal anti-involution and quantitative bridge witness counts

The two-state transfer algebra above has a natural reverse-complement symmetry. Combining it with the universal free-bridge construction of Theorem 19 yields the full number of monochromatic witnesses for every bridge assignment, not just a yes/no criterion.

Keep
\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad T_1=\begin{pmatrix}0&0\\1&1\end{pmatrix}.
\]
Define
\[
R=\begin{pmatrix}0&1\\1&-1\end{pmatrix},
\quad
R^{-1}=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\qquad \Theta(M)=R M^T R^{-1}.
\tag{41}
\]

**Theorem 39 (reverse-complement duality of monotone transfer).** The map \(\Theta\) is an involutive anti-automorphism of the two-state matrix algebra, and
\[
\boxed{\Theta(T_0)=T_1,\quad \Theta(T_1)=T_0,\quad
\Theta(T_0-T_1)=-(T_0-T_1).}
\tag{42}
\]
For any binary word \(w\), writing \(w^\sharp\) for its reverse followed by bitwise complementation,
\[
\boxed{T(w^\sharp)=\Theta(T(w)).}
\tag{43}
\]
For any arbitrary coloring \(f\) of \(Q_d\), let \(1-f\) complement all its edge bits. Then its full transfer matrices obey
\[
\boxed{
\mathscr T_{1-f}(\bar z,z)
=\Theta(\mathscr T_f(z,\bar z)).
}
\tag{44}
\]
For an antipodally odd coloring \(c\) of \(Q_d\), its rooted transfer matrix is fixed under \(\Theta\):
\[
\boxed{\Theta(\mathscr T_c(z,\bar z))
=\mathscr T_c(z,\bar z).}
\tag{45}
\]
The sign reversal of \(B=T_0-T_1\) under \(\Theta\), together with \(B^2=I\), gives an algebraic explanation for the odd first variation and even square second variation.

*Proof.* Direct multiplication gives the three relations in (42). The symmetry \(R^T=R\) and \(R^{-T}=R^{-1}\) implies that \(\Theta^2\) is the identity, while transposition reverses product order. Applying \(\Theta\) to the matrix product of a word therefore reverses its order and exchanges the two colors, proving (43). Reversing a directed geodesic from \(z\) to \(\bar z\) produces a directed geodesic from \(\bar z\) to \(z\); complementing the coloring complements each edge bit. This is a bijection of all full dimension orders, proving (44). If \(c(Ae)=1-c(e)\), the coloring \(1-c\) is the antipodal pullback of \(c\), and inversion identifies the two corresponding full path families. This gives (45). \(\square\)

Fix an *arbitrary* coloring \(f\) of \(Q_d\). Let \(P_f(z)\) be its rooted \(0^*1^*\) full-geodesic count as defined above; by path reversal, the rooted \(1^*0^*\) count is \(P_f(\bar z)\). For an odd bridge assignment \(h(\bar z)=1-h(z)\), form the antipodally odd coloring \(C(f,h)\) of \(Q_{d+1}\) from Theorem 19. Let \(X_f(h)\) count **oriented monochromatic full geodesics directed from the lower face to the upper face** (each such path crosses a vertical bridge once).

**Theorem 40 (full quantitative bridge formula).** Choose a representative \(z_P\) from each antipodal root pair \(P=\{z,\bar z\}\). Then
\[
\boxed{
X_f(h)=2\sum_{P}
\begin{cases}
P_f(z_P),&h(z_P)=0,\\
P_f(\bar z_P),&h(z_P)=1.
\end{cases}}
\tag{46}
\]
In particular,
\[
\boxed{
\min_hX_f(h)=2\sum_P\min(P_f(z),P_f(\bar z)),
}
\tag{47}
\]
\[
\boxed{
\max_hX_f(h)=2\sum_P\max(P_f(z),P_f(\bar z)).
}
\tag{48}
\]
If \(h\) is chosen uniformly among all legal odd bridge assignments, then
\[
\boxed{
\mathbb E_hX_f(h)=\sum_{z\in Q_d}P_f(z),\qquad
\operatorname{Var}_hX_f(h)=
\sum_P(P_f(z)-P_f(\bar z))^2.
}
\tag{49}
\]
Furthermore, with \(\mathcal I(f)=\sum_PP_f(z)P_f(\bar z)\), the uniform lower bound
\[
\boxed{\min_hX_f(h)\ge\frac{2}{d!}\mathcal I(f)}
\tag{50}
\]
holds. Therefore the universal bridge condition is equivalent to the strict positivity of the minimum in (47), or of the Walsh overlap in (21).

*Proof.* Orient a monochromatic full geodesic from the lower cube face to the upper face and let \(z\) be the lower endpoint of its vertical bridge, with bit \(b=h(z)\). As in Theorem 19, reversing its lower horizontal arm and reflecting its upper horizontal arm gives a full directed geodesic of \(f\) from \(z\) to \(\bar z\) whose color word is \(b^* (1-b)^*\). Conversely this construction is reversible and uniquely reconstructs the lower-to-upper monochromatic geodesic, including its split position. The number of such paths using the bridge at \(z\) is therefore \(P_f(z)\) when \(b=0\), and \(P_f(\bar z)\) when \(b=1\).

Now pair \(z\) and \(\bar z\). If \(h(z)=0\), then \(h(\bar z)=1\), and the respective contributions at the two bridge endpoints are both \(P_f(z)\); if \(h(z)=1\), they are both \(P_f(\bar z)\). Summing proves (46). Distinct antipodal root pairs carry independent bridge choices, giving (47)--(48). For a pair with values \(a,b\), its random contribution is \(2a\) or \(2b\) with equal probabilities, having mean \(a+b\) and variance \((a-b)^2\). Independence proves (49).

Finally \(0\le P_f(z)\le d!\), so \(\min(a,b)\ge ab/d!\) for every pair. Summing in (47) proves (50). \(\square\)

**Corollary 41 (rooted \(L^1\) closure formulation).** The universal paired-root lemma, hence NORI1 in dimension \(d+1\), is equivalent to the strict inequality
\[
\boxed{
\sum_{z\in Q_d}P_f(z)>
\sum_{\{z,\bar z\}}
|P_f(z)-P_f(\bar z)|
\quad\text{for every arbitrary }f.
}
\tag{51}
\]
Both sides are intrinsic to monotone full geodesics in the lower cube. Unlike a density-greater-than-one-half proposal, (51) remains meaningful for the sparse parity-reader root profiles of Theorem 31.

*Proof.* Equations (47) and (49) give
\[
\min_hX_f(h)=
\sum_zP_f(z)-\sum_P|P_f(z)-P_f(\bar z)|.
\]
It is positive precisely when some antipodal root pair has two positive rooted path counts, by (47). Apply the bridge equivalence of Theorem 19. \(\square\)

**Proof-search implication.** The two-state path matrices now supply an explicit involutive antipodal duality and a curvature-twisted square second-variation identity. The quantitative bridge formula converts their rooted counts into a minimax intersection inequality (51). The remaining full proof would establish (51) for arbitrary lower-cube colorings, preferably by a supported equivariant chain index preserved under single-edge recolorings. The unweighted parity counterexample in Proposition 32 explains why a direct mod-two count is inadequate, while the transfer involution and square relation identify the additional algebraic structure available for such an index.


## Root-reversal duality and antipodal seam certificates

The two-state transfer algebra has a support-preserving duality under root reversal and color complementation. It also suggests a geometric certificate in which the opposite path orientations have antipodal switch vertices.

**Theorem 42 (transfer duality under reversal).** Put
\[
J=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
K=JB=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
For each bit \(b\),
\[
\boxed{T_b^T J=J T_{1-b},\qquad B^T J=-JB.}
\]
If \(a\preceq_z b\), and the reverse interval is ordered away from \(\bar z\), then
\[
\boxed{\mathscr T_f(b,a)^T J
       =J\mathscr T_{1-f}(a,b).}
\]
Thus this duality reverses each geodesic's dimension order and preserves its dimension support. The full-root scalar identity is
\[
P_f(\bar z)=P_{1-f}(z)=Q_f(z).
\]

*Proof.* Multiply the two displayed transition matrices to verify the local identity. For a path with bits \(b_1,\ldots,b_k\), the reversed transfer product is \(T_{b_1}\cdots T_{b_k}\). Transposing and moving \(J\) through its factors gives \(J T_{1-b_k}\cdots T_{1-b_1}\), the complemented forward product. Reversal is a bijection on the interval's directed geodesics, so sum the identity over those paths. Finally \(J(1,0)^T=(1,1)^T\), which converts the terminal scalar on the reversed interval into the accepting scalar on the complemented interval. \(\square\)

**Corollary 43 (positive-cone form of a critical determinant).** For an edge \(u\to v\), put
\[
p=\mathscr T_f(z,u)(1,0)^T,\qquad
q=J^{-1}\mathscr T_f(v,\bar z)^T(1,1)^T.
\]
Both vectors have nonnegative integer entries, and
\[
\boxed{D_e P_f(z)=q^T Kp=p_0q_1-p_1q_0.}
\]
More explicitly, \(p_0\) counts zero prefixes and \(p_1\) counts prefixes with a monotone word ending in one. The entry \(q_0\) counts one suffixes, while \(q_1\) counts monotone suffixes with an initial zero. The entries at empty intervals are defined by the matrix formula.

*Proof.* Every nonempty accepted word is all zero, all one, or of type \(0^+1^+\), with transfer matrix respectively \(T_0,T_1,T_1T_0\). Thus an interval transfer sum has form
\[
\begin{pmatrix}Z&0\\H+O&O\end{pmatrix},
\]
where \(Z,O,H\) count these three kinds of words. This proves the prefix description, while application of \(J^{-1}\) gives suffix vector \((O,Z+H)^T\). Empty intervals give \(p=(1,0)^T\) or \(q=(1,0)^T\), directly. The factorized first variation from Theorem 36 is
\[
(1,1)\mathscr T_f(v,\bar z)B\mathscr T_f(z,u)(1,0)^T
=q^T JBp,
\]
proving the determinant. \(\square\)

The matrix \(J\) has determinant \(-1\), so its symmetric form is indefinite. The duality gives an algebraic compatibility of root reversal with supported transfers. A global supported homotopy and a nonzero index remain to be established.

### A quadrilateral certificate with antipodal switches

For any cube vertices \(a,b\), let \(Z_f(a,b)\) and \(O_f(a,b)\) count respectively zero-colored and one-colored geodesics using precisely the dimensions on which \(a,b\) differ. Empty paths count once. Define
\[
\mathcal R_f(z)=
\sum_{w\in Q_d}
Z_f(z,w)O_f(w,\bar z)
O_f(z,\bar w)Z_f(\bar w,\bar z).
\]
Let \(S(f)=\{z:\mathcal R_f(z)>0\}\).

**Theorem 44 (antipodal seam equivalence).** A root belongs to \(S(f)\) precisely when its two opposite-orientation witnesses can have switch vertices \(w,\bar w\), respectively. Therefore
\[
\boxed{S(f)\subseteq P(f),\qquad S(f)=\bar S(f).}
\]
A positive summand specifies a monochromatic geodesic quadrilateral: zero arms join \(z\) to \(w\) and \(\bar w\) to \(\bar z\), while one arms join \(w\) to \(\bar z\) and \(z\) to \(\bar w\). If neither color block is empty, its union is a simple \(2d\)-cycle; each of its two diagonals joins antipodal vertices.

*Proof.* Put \(U=\{i:z_i\ne w_i\}\). The zero arms use \(U\), and the one arms use \(U^c\). Concatenating the indicated zero and one arms gives a full \(0^*1^*\) path from \(z\); concatenating the one and zero arms gives a full \(1^*0^*\) path from the same root, with complementary switch vertices. Conversely such paths supply the four factors of a positive summand. Antipodal reversal of both witnesses preserves this condition, proving symmetry.

The two zero arms occupy opposite parallel \(U\)-faces, and the two one arms occupy opposite parallel \(U^c\)-faces. Any two adjacent arms meet only at their prescribed corner, because their varying dimension sets are disjoint. Opposite arms lie in disjoint faces. This proves the simple-cycle statement when both blocks are nonempty. \(\square\)

**Theorem 45 (antipodal seam preservation under a free new direction).** Extend \(f\) from \(Q_d\) to \(Q_d\times Q_1\) by keeping every old-direction edge color independent of the new bit, and assigning arbitrary colors \(h(x)\) to the new-direction edges. Then
\[
\boxed{S(f^{\mathrm{ext}})=S(f)\times Q_1.}
\]

*Proof.* Projection of an extended certificate erases the new direction from both witnesses. The resulting words retain their opposite monotone orientations, and their switch vertices remain antipodal after projection. Hence every extended root projects into \(S(f)\).

For the converse take a certificate with corners \(z,w,\bar z,\bar w\), and start in either new layer. Suppose each of the two zero arms has a corner where \(h=0\). Insert the new edge at one such corner of each zero arm. This puts the new direction in the zero dimension block, while the old one arms remain in their prescribed layers. The two new switch vertices are antipodal, so this gives an extended certificate.

If that condition fails, both corners of one zero arm have \(h=1\): either \(h(z)=h(w)=1\), or \(h(\bar w)=h(\bar z)=1\). Each of the two opposite one arms therefore has a corner where \(h=1\). Insert the new edge at these corners instead, putting the new direction in the one dimension block. Again the switch vertices are antipodal. This four-corner argument also covers an empty color block. \(\square\)

**Corollary 46 (Cartesian seam factorization).** For independent Cartesian factors,
\[
\boxed{S(f\boxtimes g)=S(f)\times S(g).}
\]

*Proof.* Project the two witnesses and their antipodal seams into each factor for one inclusion. Conversely concatenate the factors' zero prefixes, then their one suffixes, to make the first witness; concatenate their one prefixes, then zero suffixes, to make the other. Their switch vertices are the product of the first seams and its antipode. Every dimension is used once. \(\square\)

### A local limitation of seam normalization

**Proposition 47 (a paired root can lack antipodal seams).** In \(Q_3\), color precisely the edges indexed by
\[
(x,i)\in\{(0,1),(0,2),(1,1),(1,2),(2,2)\}
\]
one, where \(x\) is the integer encoding of the endpoint with bit \(i\) zero; all other edges have color zero. Then \(z=1\) is paired and belongs to \(P(f)\setminus S(f)\).

*Proof.* In lexicographic dimension-permutation order, the six words from \(z=1\) are
\[
011,\ 010,\ 101,\ 100,\ 100,\ 100.
\]
The only \(0^*1^*\) switch vertex is \(0\). The \(1^*0^*\) switch vertices are \(3,5\). The antipode of \(0\) is \(7\), so none of these two opposite witnesses has an antipodal seam partner. The root is paired because both orientations occur. \(\square\)

**Closure proposal and status.** The assertion \(S(f)\ne\varnothing\) for every binary cube-edge coloring would imply the paired-root theorem and NORI1 one dimension higher. Theorems 45--46 show that this stronger certificate respects free-direction insertion and Cartesian decomposition. Proposition 47 shows that deriving it from a paired witness requires control of rerooting. The unrestricted certificate assertion and its implication from ordinary paired-root existence are unproved.

For validation, all \(1920\) distinct quadrilateral and monochromatic certificates in \(Q_4\) were encoded as Boolean forbidden-pattern inequalities on its \(32\) edge bits. The integer feasibility solver reported the joint avoidance system infeasible. This is a finite computational consistency check of the stronger proposal, rather than an all-dimensional proof.


## Restoring an endpoint defect in an antipodal quadrilateral

An antipodal seam certificate permits restoration to be coupled with rerooting. This gives a contradiction rule stronger than the arbitrary paired-root repair classification.

**Theorem 48 (endpoint restoration forces an original paired root).** Let \(f\) have no paired root, let \(e\) have color one, and let \(f_e\) change its color to zero. Suppose \(f_e\) has a nondegenerate antipodal geodesic quadrilateral, with zero dimension block \(U\) and one dimension block \(U^c\), both nonempty. Then \(e\) lies strictly inside one of its zero arms. In particular
\[
\boxed{3\le |U|\le d-1.}
\]

*Proof.* If the quadrilateral avoided \(e\), it would already certify a paired root in \(f\). Since \(e\) has repaired color zero, it belongs to a zero arm. The two zero arms lie in disjoint parallel \(U\)-faces, so only one contains \(e\). All other arms retain their colors after restoration.

Name the affected zero arm \(z\to w\); the other is \(\bar w\to\bar z\), and the one arms are \(z\to\bar w\) and \(w\to\bar z\). Put \(k=|U|\).

If \(e\) is the final edge of \(z\to w\), its original word is \(0^{k-1}1\). Append the one arm \(w\to\bar z\), obtaining an original \(0^*1^*\) full geodesic from \(z\). The unaffected one arm \(z\to\bar w\), followed by the unaffected zero arm, gives the opposite orientation from the same root. Thus \(z\) was paired.

If \(e\) is the first edge, reverse the affected arm. From \(w\) its original word is \(0^{k-1}1\); append the one arm \(z\to\bar w\) to obtain \(0^*1^*\). The one arm \(w\to\bar z\), followed by the reverse of the unaffected zero arm, gives \(1^*0^*\) from \(w\). Thus \(w\) was paired. The same argument applies to the other zero arm after relabeling the corners. Both endpoint cases contradict the hypothesis. An internal edge requires \(k\ge3\), and nondegeneracy gives \(k\le d-1\). \(\square\)

**Corollary 49 (an empty antipodal root pair in the affected face).** Under Theorem 48, let the affected zero arm run from \(z\) to \(w\), and let \(H\) be its \(U\)-face. In the original restricted coloring \(f|_H\), neither \(z\) nor \(w\) admits either monotone orientation to the other. Repair makes them joined by a zero-colored full \(H\)-geodesic. Moreover, every zero-colored \(z\)-to-\(w\) geodesic in \(f_e|_H\) must contain \(e\) internally.

*Proof.* An original \(0^*1^*\) geodesic from \(z\) to \(w\), followed by the unaffected one arm to \(\bar z\), would give that orientation at the full root \(z\). Its unaffected opposite witness would then make \(z\) paired in \(f\). An original \(0^*1^*\) geodesic from \(w\) to \(z\) gives the same contradiction at \(w\). Reversal excludes the other orientation at each face root.

Repair supplies the prescribed zero arm. Any repaired zero arm avoiding \(e\) would yield an original quadrilateral; any with \(e\) at an endpoint would contradict Theorem 48. This proves the last assertion. \(\square\)

**Inductive closure implication.** Choose a hypothetical paired-root counterexample in the least dimension, and then minimize its one-edge count. Every repaired coloring has a paired root. If a repair supplies a nondegenerate antipodal seam certificate, Theorem 48 confines its defect to a proper face of at least three dimensions. That face has an empty antipodal pair at the certificate's corners by Corollary 49, while the least-dimension hypothesis supplies paired roots elsewhere in the same face. Thus closure can proceed by transporting a lower-dimensional paired root to the quadrilateral interface, or by showing that a critical repair must admit an endpoint-defect certificate. These transport assertions remain unproved.



## Reciprocal doubling gives a unimodular self-dual positive transfer module

The positive \(q\)-deformation of rooted monotone-geodesic transfer introduces reciprocal parameters \(q\) and \(q^{-1}\) under reversal-complementation. A two-state bilinear duality cannot identify these at one fixed \(q\ne1\), but a four-state direct-sum module does. Importantly the doubled model has **entrywise nonnegative** transition matrices and an **integral unimodular** reversal pairing, with no need to invert \(q\) in its coefficients.

Let
\[
T_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
T_1=\begin{pmatrix}0&0\\1&1\end{pmatrix},\quad
R=\begin{pmatrix}0&1\\1&-1\end{pmatrix},
\quad S=R^{-1}=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
For an indeterminate \(q\) (or any positive real specialization), define four-state operators
\[
V_0(q)=\operatorname{diag}(qT_0,T_0),\quad
V_1(q)=\operatorname{diag}(T_1,qT_1),\quad
\mathcal J=\begin{pmatrix}0&S\\S&0\end{pmatrix}.
\tag{52}
\]
The first channel is the weighted automaton \(U_b(q)\); the second is the automaton \(q U_b(q^{-1})\), so a length-\(k\) path has channel matrices \(U_q(P)\) and \(q^kU_{q^{-1}}(P)\). No negative powers of \(q\) occur in the four-state edge operators.

**Theorem (fixed-parameter reciprocal bilinear duality).** Over \(\mathbb Z[q]\),
\[
\boxed{V_b(q)^T\mathcal J=\mathcal J V_{1-b}(q)
\quad(b=0,1).}
\tag{53}
\]
The matrix \(\mathcal J\) is symmetric, nondegenerate and unimodular, with determinant \(1\), and has real signature \((2,2)\). Writing \(D(q)=V_0(q)-V_1(q)\), one has
\[
\boxed{D(q)^T\mathcal J=-\mathcal J D(q),\qquad
(D(q)^k)^T\mathcal J=(-1)^k\mathcal J D(q)^k.}
\tag{54}
\]
For any full dimension-simple path \(P\) with bit word \(w\), if \(w^\sharp\) is the reversal of its bitwise complement, then
\[
\boxed{V(w)^T\mathcal J=\mathcal J V(w^\sharp),}
\tag{55}
\]
where \(V(w)=V_{w_{|w|}}\cdots V_{w_1}\). Thus root reversal with antipodal color complementation is represented by **one fixed unimodular bilinear pairing** on a four-state module.

*Proof.* The two-state reciprocity identity \(U_b(q)^TS=qS U_{1-b}(q^{-1})\) follows from \(T_b^TS=S T_{1-b}\). The off-diagonal blocks of \(V_b^T\mathcal J\) are therefore \(U_b(q)^TS\) and \(qU_b(q^{-1})^TS\), respectively equal to the off-diagonal blocks of \(\mathcal J V_{1-b}\), proving (53). The determinant of \(S\) is \(-1\), and \(\det\mathcal J=\det(S)^2=1\). The symmetric off-diagonal form has equal positive and negative inertia. Subtract (53) for the two colors to obtain the first identity of (54); raise it to successive powers for the second. Applying (53) to each factor of the transfer product, with transpose reversing factor order, proves (55). \(\square\)

**Proposition (two-state and positive-metric obstructions).** For \(q\ne1\), there is no invertible two-by-two matrix \(J\) with
\[
U_0(q)^T J=J U_1(q),\quad U_1(q)^T J=J U_0(q).
\tag{56}
\]
Nor can the doubled operators in (52) satisfy the corresponding exchange relation for a positive-definite real symmetric \(J\), for any \(q>0\).

*Proof.* An invertible two-state \(J\) in (56) would make \(U_0(q)^T\) similar to \(U_1(q)\), whose traces are \(q\) and \(1\), forcing \(q=1\). For any dimension and a positive-definite \(J\), the adjoint relation gives \(V_1=J^{-1}V_0^TJ\). But \(V_0V_1=0\), since \(T_0T_1=0\) in both blocks. Therefore \(V_0J^{-1}V_0^TJ=0\). Multiplying by \(J^{-1}\) and taking the associated positive quadratic form forces \(V_0=0\), a contradiction. \(\square\)

**Scope for equivariant chains.** The four-state model reconciles positive transfer operators with *integral* reversal duality at fixed \(q\). Its skew-adjoint color difference gives coherent odd/even signs under all-rank face variations. Nevertheless the bilinear pairing is necessarily indefinite. Its existence supplies a compatible local coefficient system, not a nonvanishing global Smith index. Moreover reduction of path-count coefficients modulo two may cancel all witnesses at a root (for example, an all-zero \(d\)-cube has \(d!\) accepted full paths, an even number for \(d\ge2\)). A support-sensitive chain lift must retain individual path incidences or higher cells rather than relying on the parity of the scalar transfer sum.



## Faithful path tags versus square-flat scalar transport

The reciprocal four-state module is self-dual, but characteristic-two scalar path summation may cancel all existing witnesses. The following gives a rigorous obstruction and a minimal higher-chain replacement.

Fix a root \(z\) of \(Q_d\), \(d\ge2\), and put an independent commuting indeterminate \(t_e\) on each undirected cube edge. Work over \(\mathcal R=\mathbb F_2[q,\{t_e\}]\). For an arbitrary coloring \(f\), define
\[
\boxed{\mathscr P_{f,q}(z;\mathbf t)
=\sum_{\substack{\pi\in S_d\\f(P(z,\pi))=0^k1^{d-k}}}
q^k\prod_{e\in P(z,\pi)}t_e.}
\tag{57}
\]

**Theorem 50 (faithful support and paired-root polynomial).** For every \(f,z\), the polynomial \(\mathscr P_{f,q}(z;\mathbf t)\) is nonzero if and only if a full \(0^*1^*\) geodesic from \(z\) exists. If \(r_{\{z,\bar z\}}\) are distinct indeterminates indexed by antipodal root pairs, then
\[
\boxed{\mathscr I_{f,q}=
\sum_{\{z,\bar z\}}r_{\{z,\bar z\}}
\mathscr P_{f,q}(z;\mathbf t)
\mathscr P_{f,q}(\bar z;\mathbf t)}
\tag{58}
\]
is nonzero if and only if a paired root exists.

*Proof.* Two different full geodesics from a fixed root have different edge sets: a simple path edge set and its initial vertex determine its entire order. Their tagged monomials therefore differ, so their sum cannot cancel in \(\mathcal R\). This proves the first assertion. The polynomial ring has no zero divisors, so a product of the two root polynomials is nonzero precisely when both are nonzero. Distinct variables \(r_{\{z,\bar z\}}\) prevent cancellation between different antipodal pairs. \(\square\)

**Theorem 51 (flat scalar tags necessarily lose support).** Let \(\mathcal K\) be any commutative ring of characteristic two with edge weights \(w_e\), satisfying on every directed square
\[
\boxed{w_{uv_i}w_{v_iw}=w_{uv_j}w_{v_jw}.}
\tag{59}
\]
Every full root-to-antiroot geodesic has the same weight \(W\). In the all-zero coloring its weighted monotone count is
\[
\boxed{\sum_{\pi\in S_d}q^d\prod_{e\in P(z,\pi)}w_e
=d!\,q^d W=0.}
\tag{60}
\]
Thus scalar multiplicative square-flatness is incompatible with detecting every rooted witness by nonvanishing of a characteristic-two transfer count.

*Proof.* Adjacent transpositions generate \(S_d\). Each replaces one square route by its other route, leaving prefix and suffix unchanged; (59) preserves its product weight. Therefore all full path products agree. The integer \(d!\) is even for \(d\ge2\), so the sum vanishes although all geodesics are admissible. \(\square\)

Let \(\mathscr U_{f,q}^{\mathbf t}(a,b)\) be the two-state matrix transfer weighted by the monomial \(\prod_{e\in P}t_e\) along each directed dimension-simple path \(P:a\to b\). For a monotone route \(\rho\) through a \(k\)-face \(F=[u,w]\), put \(t_\rho=\prod_{e\in\rho}t_e\) and \(B_q=U_0(q)-U_1(q)\).

**Theorem 52 (tagged higher-face exchange defect).** The formal color differences along \(\rho\) obey
\[
\boxed{D_\rho\mathscr U_{f,q}^{\mathbf t}(z,\bar z)
=t_\rho\,
\mathscr U_{f,q}^{\mathbf t}(w,\bar z)
B_q^k\mathscr U_{f,q}^{\mathbf t}(z,u).}
\tag{61}
\]
For any two routes \(\rho,\rho'\) across the same face, their difference is
\[
\boxed{(t_\rho-t_{\rho'})
\mathscr U_{f,q}^{\mathbf t}(w,\bar z)
B_q^k\mathscr U_{f,q}^{\mathbf t}(z,u).}
\tag{62}
\]

*Proof.* Taking formal differences removes paths avoiding any prescribed route edge. Every remaining path is the concatenation of a prefix, the full prescribed route, and a suffix. The route matrices become \(B_q^k\), while its tag monomial factors as \(t_\rho\). Prefix and suffix sums multiply as displayed. Subtract the formulas for the two routes. \(\square\)

**Closure implication.** Independent path tags are support-faithful, but they replace scalar square equality by the nonzero difference \(t_\rho-t_{\rho'}\). A viable dimension-simple equivariant construction must retain **higher square-exchange chains whose boundary is this difference**, not collapse them to scalar equalities. The natural uncolored framework is the permutohedron of full dimension orders, with neighboring vertices related by adjacent swaps and two-faces encoding commutation and braid relations. Whether the colored accepted-path carriers inside this framework have the necessary antipodal Smith index remains unproved.


## Localizing restoration defects after dimension removal

The endpoint restoration theorem forces both opposite corners of the affected zero face to admit neither monotone orientation. The repaired zero arm nevertheless gives a full geodesic with a single one-colored edge in the original face. These two facts constrain which dependencies can contain that edge.

**Theorem 53 (a defect cannot lie in a root-universally removable block).** Let \(g\) color \(Q_k\), let a root \(z\) admit neither \(0^*1^*\) nor \(1^*0^*\), and suppose a full geodesic from \(z\) has precisely one one-colored edge \(e\). Split the directions into \(A,B\), with every \(A\)-edge color independent of the \(B\)-bits. Suppose every fixed-\(A\) fiber on \(B\) has all roots favorable. Then the direction of \(e\) lies in \(A\).

*Proof.* If it lay in \(B\), projection of the exceptional path onto \(A\) would give a zero-colored full outer geodesic from \(z_A\). Traverse this path first, then a favorable \(B\)-geodesic from \(z_B\) in the terminal fiber. The resulting full word has type \(0^*1^*\), contradicting the root hypothesis. All outer colors are preserved because they are independent of \(B\). \(\square\)

In particular the defect direction survives every successive sink deletion in the directed dependency graph. A sink variable affects no other direction's edge color; its one-dimensional fibers are root-universally favorable. Favorability of each orientation at the projected root is preserved by insertion at its phase change.

**Theorem 54 (the surviving defect requires branching in its component).** Under Theorem 53's root and path hypotheses, strip all sink directions and let \(C\) be the interaction component of the surviving defect direction. Then:

1. The projected root in \(C\) admits neither monotone orientation.
2. The projected exceptional path has its sole one-colored edge strictly internally in \(C\).
3. The interaction graph on \(C\) is not a star.
4. Some direction in \(C\) has at least two incoming dependency arcs.

Consequently these restrictions hold inside every affected face of a nondegenerate critical-repair quadrilateral.

*Proof.* Sink insertion preserves both orientation sets after projection, while Theorem 53 prevents removal of the defect. In the retained cube, the coloring factors over its interaction components. Projection of the exceptional path onto every component other than \(C\) gives a zero-colored full geodesic. If the root in \(C\) admitted either orientation, combine that witness with these zero factor paths, placing the additional zeros before the one block for \(0^*1^*\), or after it for \(1^*0^*\). This would give the corresponding orientation in the retained cube, and hence at the original root. Thus assertion 1 holds. The exceptional path projects to a one-edge exception in \(C\); an endpoint exception would itself have a monotone word, proving assertion 2.

Every root of a star-interaction coloring admits at least one orientation: traverse the hub first, read its color \(b\), and sort the remaining leaf steps from color \(b\) toward color \(1-b\). Their colors depend only on the now-fixed hub bit. This contradicts assertion 1 and proves assertion 3.

Suppose all indegrees in \(C\) were at most one. The sink-stripped graph has outdegree at least one everywhere. Its total indegree and outdegree agree, forcing both degrees to equal one at every vertex of \(C\). The weakly connected component is therefore a directed cycle. Each edge-color function has form \(a_i+x_{p(i)}\), where \(p(i)\) is its cycle predecessor.

At a root \(y\), put \(b_i=a_i+y_{p(i)}\). Nonconstant \(b_i\) orient the cycle precedence constraints for a zero-colored path acyclically, giving a monochromatic zero full geodesic. If all \(b_i=0\), a reverse cyclic dimension order gives word \(0^{|C|-1}1\). If all \(b_i=1\), a forward cyclic order gives \(10^{|C|-1}\). Thus every root admits an orientation, contradicting assertion 1. This proves assertion 4. \(\square\)

The hypothesis is stronger than merely having an empty root: it includes a full path with one isolated color exception. The defect must remain in the retained dependency system, and the branching obstruction is localized to its own factor. This prevents removal of the exceptional direction by the existing all-root fiber reductions.

A scoped counterexample recorded as research note \(\texttt{note_0ef014a49eca70c6785725e2}\) shows that the surviving interaction graph can still be an undirected path. In that example, two overlapping three-direction constraints force a rise and a descent in every order at the selected root, while one order has only an internal single-edge exception. Hence cycle-freeness of the interaction graph alone cannot transport a paired root to the quadrilateral corner.

**Closure assessment.** The recent repair-fan theorem identifies all free bridge flips within one direction; the variable-matching and star-fiber results give structural rules for gluing across selected terminal blocks. Theorems 53--54 confine a restoration defect beyond the root-universal removal rules. The remaining step must couple a paired root elsewhere in this surviving component to the outside one-colored arms, or force an endpoint certificate. Existence of paired roots in a proper face supplies the starting witness; preserving the outside arm colors during root transport remains unproved.


## Rooted-tree exclusion at the restoration corners

The rootwise rooted-tree theorem in “Cartesian factorization of paired roots and interaction-prime reduction” strengthens the local obstruction in Theorem 54.

**Corollary 55 (two branching targets in a strongly connected defect factor).** Let \(C\) be the surviving defect factor of Theorem 54. Its coloring cannot have an outward rooted-tree dependency structure with arbitrary feedback into its root, including inactive parent links. If the directed dependency graph on \(C\) is strongly connected, it has at least two distinct vertices of indegree at least two.

*Proof.* At every prescribed root of a rooted-tree feedback coloring, traverse the hub first and then monochromatically traverse the components obtained by cutting inactive parent links. Ordering those components by color gives a full path with at most one switch. The root in \(C\) admits neither orientation by Theorem 54, excluding this structure.

A strongly connected dependency graph with at most one branching target is a directed cycle or an outward rooted tree with additional arrows entering its root. Every nonhub color function then has one active predecessor, hence the required affine one-bit form. The rootwise theorem applies, giving the contradiction. \(\square\)

This sharpens the earlier requirement of one branching direction whenever the defect factor is strongly connected. For a factor with several strongly connected components, coupling their root-specific orientations remains an additional obligation. The tree-face counterexample in note \(\texttt{note_0ef014a49eca70c6785725e2}\) has several branching targets and is consistent with this stronger restriction.


## A causal obstruction to transporting the prescribed empty root

The strong-connectivity qualification in Corollary 55 has a dimension-uniform obstruction. For every \(r\ge2\), use cycle bits \(y_0,\ldots,y_{r-1}\) and two more directions \(u,v\), and color
\[
f_i=y_{i-1}\quad(0\le i<r,\ \text{indices modulo }r),\qquad
f_u=(1-v)\left(1-\prod_i y_i\right),\qquad f_v=1-u.
\]
Its directed dependency graph has a source cycle on the \(y\)-directions, a terminal two-cycle \(u\leftrightarrow v\), and arrows from the source into \(u\). The sole branching target of the whole graph is \(u\). Every individual feedback component is covered by the cyclic-core or rooted-tree theorem.

At the prescribed root \((\mathbf0,0,0)\), every full path has both a rise and a descent. The cycle subsequence supplies a rise. If \(v\) precedes \(u\), their colors are one and zero. If \(u\) precedes \(v\), the latter color is zero; either \(u\) is one, supplying a descent, or all cycle bits were already one at \(u\), and an earlier one-colored cycle edge precedes this zero. Yet reverse cyclic order followed by \(u,v\) has word
\[
\boxed{0^{r-1}100,}
\]
with one strictly internal exceptional edge. Its antipodal endpoint also admits neither orientation.

The full root profile is
\[
A_0=\{(y,u,v):y\ne\mathbf1,\ (u,v)\ne(0,0)\},\qquad
A_1=\{(y,u,v):y\ne\mathbf0,\ (u,v)\ne(1,1)\},
\]
so
\[
\boxed{|P|=2^{r+1}-4.}
\]
The proof and complete profile are recorded in note \(\texttt{note_0868fc3b9c03299a5e19a9b8}\). This family proves that a single-defect path at an empty prescribed root can traverse a dependency system whose components are all globally reducible, with only one branching target in their union.

**Implication for closure.** Restoring the defect produces a zero path between the required corners, while component reductions supply paired roots at other locations. Any closure argument using these reductions must preserve compatibility with the outside one-colored arms during the change of root. The additional quadrilateral arm conditions remain available: the family above establishes the local transport obstruction, and does not assert that it extends to a paired-root-free full coloring.


## Audit and a path toward closure

The hub-first rooted-tree theorem, the affected-face endpoint exclusion, and the causal obstruction family remain valid in their stated scopes. Two graph-lemma hypotheses have been corrected in the companion interaction-reduction Subsection: the unique-predecessor forest conclusion requires a nonempty set of branching targets, and a singleton strongly connected graph needs its own case. A directed cycle supplies the counterexample to the forest assertion when that set is empty. The two-hub compression applications already satisfy the required nonempty-set hypothesis.

The following limits are part of the mathematical status:
- Corollary 55 requires strong connectivity of the surviving defect factor. The causal family proves the corresponding weak-connectivity extension false.
- A paired root in a repaired coloring supplies no established antipodal quadrilateral certificate. Certificate availability remains an additional unproved assertion.
- The causal family is a counterexample to prescribed-root transport from the stated local hypotheses; its paired-root count is positive. Extension to a critical full quadrilateral with compatible outside arms is unproved.

**Written closure route.** Start with an ordinary coloring without paired roots minimizing its one-edge count. Every nonempty restoration of one-edges creates a paired root. The singleton repair classification splits the witness into a repaired zero full path or a newly repaired orientation paired with an old opposite orientation. The first remaining task is to obtain antipodally aligned seams, or to run the exchange argument directly on both orientation paths without such alignment.

When a repair supplies a nondegenerate quadrilateral, fix its other three monochromatic arms. In the affected face consider all full corner-to-corner paths with one one-colored edge. Every such path produces the same type of marked quadrilateral after repairing its exceptional edge, because all other arms lie outside this affected face. An endpoint exception contradicts original paired-root absence. Minimize the defect's rank, or maximize it, among these paths. The next lemma gives forced square constraints at both extremes.

The proposed finishing step is to combine these constraints with the opposite zero arm and the two one arms: produce an endpoint exception, reduce the affected zero block, or create an original paired root. Each successful alternative contradicts a minimum marked obstruction. This finishing step and initial seam alignment remain unproved; the local root-transport counterexamples show why all four arms must participate.

**Lemma 56 (incoming and outgoing fans at extremal defect positions).** Let \(g\) color a cube face \(H\), with opposite roots \(z,w\). Suppose no full \(z\)-to-\(w\) path has a monotone color word, and some full path has precisely one one-colored edge. Let \(\mathcal E\) be all such one-defect paths.

For a path in \(\mathcal E\) whose defect rank is smallest possible, write its two steps immediately before and through the defect as
\[
a\xrightarrow[\ 0\ ]{i}b\xrightarrow[\ 1\ ]{j}v.
\]
Then the alternative square edge
\[
\boxed{a\oplus e_j\xrightarrow[\ 1\ ]{i}v}
\]
has color one. More generally, keep the defect \(b\to v\) and its zero suffix fixed. For every direction \(i\) which can be last on a zero geodesic from \(z\) to \(b\), the edge into \(v\) in direction \(i\) has color one. Together with the defect itself these form an incoming one-colored fan of size at least two.

For a path whose defect rank is largest possible, write the defect and its next step as
\[
b\xrightarrow[\ 1\ ]{j}v\xrightarrow[\ 0\ ]{i}c.
\]
Then
\[
\boxed{b\xrightarrow[\ 1\ ]{i}b\oplus e_i}
\]
has color one. Keeping the zero prefix and defect fixed, every possible first direction of a zero suffix from \(v\) gives such a one-colored edge out of \(b\), again forming a fan of size at least two.

*Proof.* An exceptional edge cannot be first or last, since its path would have a monotone word.

In the first square suppose the alternative final edge had color zero. If the alternative first edge were zero, the swapped full path would be monochromatic zero. If it were one, the swapped full path would still have one defect, one rank earlier. Both conclusions contradict the hypotheses. Thus the alternative final edge is one. Any other zero prefix ending at \(b\) can replace the original prefix while retaining its defect rank and zero suffix, proving the full fan assertion.

In the second square suppose the alternative first edge had color zero. If its following edge were zero, the swapped path would be monochromatic zero. If it were one, the defect would move one rank later. Both are excluded. Replacement by any zero suffix proves the outgoing fan assertion. \(\square\)

**Application to critical quadrilaterals.** The affected corners admit neither monotone orientation by the empty-face corollary. The family \(\mathcal E\) is nonempty by restoration, so Lemma 56 applies there. It constrains edges outside the selected witness, while allowing the repaired defect edge to vary. The earliest and latest fans can occur on different paths; no common path attaining both extremes is asserted.

The square constraints were additionally checked on all one-defect paths in the causal obstruction family for cycle lengths two through five. The proof is dimension-independent.


**Proposition 57 (complete local defect immobility in the causal family).** In the causal obstruction family with \(r\) cycle directions and additional directions \(u,v\), every full one-defect path from \((\mathbf0,0,0)\) has word
\[
\boxed{0^{r-1}100.}
\]
There are precisely \(r\) such dimension orders. Thus the earliest and latest defect ranks both equal \(r\), and no exchange sequence retaining one defect within this face can move it to an endpoint.

*Proof.* Every full cycle traversal from its all-zero root has at least one one-colored step. A full one-defect path must therefore have zero-colored \(u\) and \(v\) steps. The zero \(v\) step requires \(u\) to precede \(v\). At that earlier \(u\) step the bit \(v\) is still zero, so a zero \(u\) step requires all cycle bits to be one. Consequently all cycle steps precede \(u\), which precedes \(v\).

For a cycle traversal to have only one one-colored step, all other directions must precede their cycle predecessors. Choosing the exceptional direction breaks the cyclic precedence system into a total chain. Its unique order is reverse cyclic order, ending at the exceptional direction. There is one such order for each of the \(r\) choices. Appending \(u,v\) proves the word and count. \(\square\)

The causal family still has paired roots elsewhere. Proposition 57 proves that the affected-face hypotheses alone cannot support an endpoint-mobility theorem. Lemma 56 supplies necessary fans; obtaining a contradiction requires the additional full-coloring hypothesis and its exterior arm geometry.


## Coupling opposite zero arms through transverse geodesic cuts

The unaffected zero arm constrains entire transverse fibers, rather than only the chosen exceptional path.

Use the marked quadrilateral notation of the endpoint restoration theorem. The original coloring \(f\) has no paired root. Its affected arm \(P:z\to w\) uses the direction block \(U\), has one one-colored edge, and otherwise is zero. Its opposite arm \(Q:\bar w\to\bar z\) is zero. Put \(V=U^c\), \(k=|U|\), and \(m=|V|\ge1\).

A subset \(T\subseteq U\) is **compatible** when it is a prefix direction set both of \(P\) and of \(Q\). More generally, allow \(P\) to vary over all one-defect full paths in its face and \(Q\) over all zero full paths in the opposite face. Write \(\mathcal C\) for the union of compatible subsets. For \(T\in\mathcal C\), let
\[
p_T=z\oplus\mathbf1_T,\qquad
q_T=\bar w\oplus\mathbf1_T.
\]
These vertices differ precisely in \(V\), and determine a transverse \(V\)-face.

**Theorem 58 (transverse zero-path exclusion).** No transverse face indexed by \(T\in\mathcal C\) contains a zero-colored full \(p_T\)-to-\(q_T\) geodesic. Its one-colored edges contain a directed geodesic cut separating those two vertices.

*Proof.* Choose the corresponding arm orders, and let the exceptional edge of \(P\) have rank \(r\). Put \(t=|T|\). If \(t<r\), concatenate the zero prefix of \(P\), a supposed zero transverse geodesic, and the zero suffix of \(Q\). This is a zero-colored full geodesic from \(z\) to \(\bar z\).

If \(t\ge r\), concatenate the reverse of the zero suffix of \(P\), the transverse geodesic, and the reverse of the zero prefix of \(Q\). This gives a zero-colored full geodesic from \(w\) to \(\bar w\). Both contradict paired-root absence. Prefix-set compatibility ensures that the two \(U\)-arms use complementary direction sets.

Orient the transverse face away from \(p_T\), and let \(Z_T\) be its vertices reachable from \(p_T\) along zero-colored directed paths. Then \(p_T\in Z_T\), \(q_T\notin Z_T\), and every directed edge leaving \(Z_T\) has color one. Every full directed geodesic crosses this cut. \(\square\)

**Lemma 59 (smallest rooted geodesic blockers).** In \(Q_m\), a set of edges meeting every full geodesic between one prescribed antipodal pair has size at least \(m\). For \(m\ge3\), equality requires the set to consist of all \(m\) edges incident with one of the prescribed endpoints.

*Proof.* Give a uniformly chosen full direction order to the prescribed starting root. A directed edge from rank \(s\) to rank \(s+1\) is traversed with probability
\[
\frac{s!(m-s-1)!}{m!}
=\frac1{m\binom{m-1}{s}}\le\frac1m.
\]
A blocker has expected intersection size at least one, yielding the lower bound.

For \(m\ge3\), every interior edge has probability strictly below \(1/m\). A blocker of size \(m\) must therefore use only first or last edges. Let \(I\) be its first-edge directions and \(J\) its last-edge directions. Every possible pair of distinct first and last directions must be covered: for all \(i\ne j\), either \(i\in I\) or \(j\in J\).

If \(I\ne[m]\), each missing \(i\) forces all \(j\ne i\) into \(J\). Two missing first directions would force \(J=[m]\), so a mixed blocker could omit only one first direction. It would then have at least \(m-1\) first edges and \(m-1\) last edges, exceeding \(m\) when \(m\ge3\). Thus all edges are first, or all are last. \(\square\)

**Corollary 60 (disjoint transverse cuts and endpoint fans).** Each compatible transverse fiber contains at least \(m\) one-colored edges. Distinct compatible subsets give edge-disjoint fibers. If one has precisely \(m\) one-colored edges and \(m\ge3\), they form a full one-colored endpoint star. When \(m=1\), its single transverse bridge is one.

If the two arm orders agree, all \(k+1\) prefix subsets are compatible, so the transverse fibers contribute at least \(m(k+1)\) distinct one-colored edges. The exceptional edge lies in a \(U\)-direction and contributes an additional edge. The structural conclusion is the family of directed one-colored cuts; the count records their disjointness.

The theorem uses both opposite zero arms and the full-coloring obstruction. It does not require their orders to agree. It converts the other arm into constraints on edges beyond the selected witness and the internal square fans.

## Critical direction exchanges force incompatible bridge selectors

The bridge-independent repair theorem also provides a coupling which does not assume a quadrilateral certificate.

For an ordinary cube coloring \(f\), let \(A_0(f)\) be its favorable-root set. Let \(\mathcal B(f)\) consist of all antipodally odd bridge functions \(h\) for which the odd extension \(C(f,h)\) is bad. Equivalently, its zero-bridge selector avoids \(A_0(f)\). When \(P(f)=\varnothing\), the set \(\mathcal B(f)\) is a nonempty Boolean subcube: a favorable root fixes the bridge choice in its antipodal pair, and a pair with neither favorable member leaves that bit free.

**Theorem 61 (selector incompatibility under a directional exchange).** Suppose \(P(f)=\varnothing\), and changing one one-colored edge \(e\) to zero produces a coloring with a paired root. Let \(g\) differ from \(f\) only on edges in the direction of \(e\), including the change at \(e\). The other edges in that direction may change either way.

Then
\[
\boxed{\mathcal B(f)\cap\mathcal B(g)=\varnothing.}
\]
Consequently either \(g\) has a paired root, or there is a root \(x\) with
\[
\boxed{x\in A_0(f)\cap A_1(g).}
\]

*Proof.* Fix \(h\in\mathcal B(f)\). The original odd extension \(C(f,h)\) is bad, while \(C(f_e,h)\) is good by bridge-independent repair. Thus the antipodal edge-pair flip corresponding to \(e\) is a healing flip in its direction. The restoration fan theorem says that any collection of pair flips in that direction containing this flip remains good. The extension \(C(g,h)\) therefore is good, proving disjointness.

If \(g\) has no paired root, both bad-selector subcubes are nonempty. Two Boolean subcubes are disjoint only when some bit is fixed to opposite values. Here that bit indexes an antipodal root pair. Hence one of its members \(x\) lies in \(A_0(f)\), while \(\bar x\) lies in \(A_0(g)\). Reversal gives \(x\in A_1(g)\). \(\square\)

**Corollary 62 (a separating root for balanced minimum-obstruction exchanges).** In the minimum-one-edge obstruction of the bridge-independent repair theorem, any same-direction exchange which turns at least one original one edge to zero either creates a paired root or yields the crossed witnesses of Theorem 61. In particular this applies to a balanced swap of a one edge and a zero edge.

Two distinct minimum-one-edge obstructions which differ only in one direction have disjoint bad-selector subcubes. Equal one-edge counts force their difference to contain a one-to-zero change, so Theorem 61 applies.

**Quantifier qualification.** Paired-root absence means that some bridge assignments are bad. It does not mean that every bridge assignment is bad. Theorem 61 therefore proves disjoint bad-selector sets and crossed witnesses, rather than unconditional paired-root persistence under arbitrary same-direction additions.

**Progress toward the written closure route.** The transverse cut theorem forces exterior constraints using the unaffected zero arm. The selector theorem produces a common root carrying opposite favorable orientations in two directionally related colorings. The remaining task is to couple the cut or crossed witnesses to an original paired certificate while preserving all direction uses. This has not been proved. The crossed-witness alternative avoids assuming initial quadrilateral availability and provides a second route for that missing alignment step.

## Two-lift induction and edge-pair avoidance across an unread direction

Let \(n\ge3\) and let \(c\) be a legal antipodally odd coloring of the undirected edges of \(Q_n=Q_{n-1}\times\{0,1\}\). Denote the last direction by \(j\), and suppose every edge color in the other \(n-1\) directions is independent of the \(j\)-bit. Let \(g\) denote that common horizontal coloring. Antipodal oddness of \(c\) implies that \(g\) itself is antipodally odd. Write \(h(y)\) for the color of the vertical edge above \(y\); then \(h(\bar y)=1-h(y)\). Let \(F_d\) count unoriented monochromatic-zero full antipodal geodesics.

**Theorem (two-lift monochromatic induction).** Every unoriented monochromatic-zero full geodesic \(P\) of \(g\), between roots \(y,\bar y\), gives two distinct monochromatic-zero full geodesics of \(c\). Choose the unique endpoint \(z\in\{y,\bar y\}\) with \(h(z)=0\). Orient \(P\) from \(z\) to \(\bar z\). The two lifts start at \((z,0)\) and \((z,1)\), respectively, traverse the zero-colored vertical edge at \(z\), and then traverse \(P\) in the opposite horizontal layers. Thus
\[
\boxed{F_n(c)\ge2F_{n-1}(g).}
\tag{LI1}
\]

*Proof.* Since the horizontal colors are independent of the layer, the described paths use each cube direction once and have every edge color zero. Their horizontal edges lie in different layers, so the unoriented full paths are distinct. Removing the unique vertical edge from either lift recovers \(P\); hence paths derived from distinct lower geodesics do not coincide, proving the inequality. \(\square\)

**Theorem (pair-avoidance lifting).** Assume \(g\) has at least one monochromatic-zero antipodal full geodesic. For every *horizontal* antipodal edge orbit \(q\) of \(Q_n\), at least one monochromatic-zero full geodesic of \(c\) avoids \(q\). If \(g\) has monochromatic-zero full geodesics with at least two different antipodal endpoint pairs, then the same avoidance holds for *every* antipodal edge orbit, including vertical ones. In particular, any single legal antipodal-pair recoloring of \(c\) preserves a monochromatic full antipodal geodesic.

*Proof.* Fix a monochromatic-zero lower geodesic \(P\) and its two lifts from the preceding theorem. A horizontal orbit of \(Q_n\) consists of an edge \(e\) in one horizontal layer and the antipodal edge \(\bar e\) in the other. The lower coloring \(g\) assigns opposite colors to \(e,\bar e\). Thus the zero-colored path \(P\) cannot contain both. Since its two lifts traverse the same lower horizontal edge sequence in different layers, at most one lift can encounter the given horizontal orbit. The other avoids it.

For a vertical orbit, each lifted path derived from \(P\) uses the vertical edge above \(z\), where \(z\) is the unique endpoint of \(P\) satisfying \(h(z)=0\). If two lower geodesics have different antipodal endpoint pairs, their selected vertical edges belong to different antipodal orbits. Consequently one of their lifts avoids any prescribed vertical orbit. A path avoiding a recolored orbit is unaffected by its flip and remains monochromatic. \(\square\)

**Restoration consequence.** A critical good coloring in the pair-restoration lemma cannot possess an unread direction whose induced facet has two monochromatic-zero endpoint pairs: the lifting theorem produces a monochromatic full geodesic avoiding the purported compulsory internal pivot, no matter which direction contains that pivot. The functional-reader root census supplies the required two endpoint pairs whenever its lower facet has dimension at least three; this gives an alternate route to the dimension-four one-pair robustness theorem without requiring the exceptional vertical color function itself to have the one-reader form.

**Scope.** This is a nontrivial all-dimensional closure transfer for every legal odd coloring with an unread direction, provided the lower-dimensional odd coloring has a monochromatic full geodesic. It does not settle the minimum-dimensional case in which every direction influences at least one other direction.

## Three exceptional directions, the two-hub bridge, and facetwise obstruction rigidity

The recent computer-assisted two-hub paired-root theorem combines with the unrestricted bridge criterion to close a further all-dimensional class of odd cube-edge colorings. It also forces a simultaneous structural obstruction in every facet of a minimum-dimensional counterexample.

Call a direction \(i\) of a legal antipodally odd cube coloring *simple* if its edge colors have the form \(c_i(x)=a_i+x_{r(i)}\), where \(r(i)\ne i\). A nonsimple direction is *exceptional*. Every legal edge-color function depending on at most one other bit is simple: global antipodal oddness excludes constant functions, and a nonconstant Boolean function of one bit is a signed reader.

For an arbitrary edge coloring \(g\) of \(Q_m\), its directed influence graph has an arc \(j\to i\) when changing bit \(j\) can change the color of a direction-\(i\) edge. A direction function that is constant or reads only one bit has indegree at most one. Thus a coloring with at most \(k\) other direction functions has at most \(k\) vertices of indegree at least two, both globally and within any strongly connected component.

**Lemma (two-exception paired-root bound, from the two-hub SCC theorem).** If an arbitrary edge coloring \(g\) of \(Q_m\) has at most two direction functions that are neither constant nor signed one-bit readers, then
\[
\boxed{|P(g)|\ge\max\{2,\;2^{\lceil m/2\rceil-2}\}.}
\tag{TE1}
\]
Here \(P(g)\) consists of roots admitting both monotone color-word orientations. This lemma uses the computer-assisted two-hub favorable-root theorem published in “A coupled-hub obstruction to independent leaf elimination.”

*Proof.* Every dependency SCC has at most two vertices with internal indegree greater than one. The two-hub SCC gluing theorem gives a paired-root multiplicative factor at least \(2^{b-1}\) for any nontrivial component of size \(b\) with at most one branching target, and at least \(2^{b-3}\) if it has two; a singleton gives factor \(2\). Let \(t\) count nontrivial SCCs and let \(\delta=1\) if a component with two branching targets occurs, zero otherwise. Since only two exceptional functions exist, at most one SCC can have two branching targets. Multiplying the factors gives
\[
|P(g)|\ge2^{m-t-2\delta}
\ge2^{m-\lfloor m/2\rfloor-2}
=2^{\lceil m/2\rceil-2}.
\]
The paired-root set is antipodally symmetric and nonempty, so it also has at least two vertices. \(\square\)

**Theorem (NORI1 with at most three exceptional directions).** Every legal antipodally odd edge coloring \(c\) of \(Q_n\), \(n\ge2\), with at most three exceptional direction functions admits a monochromatic full antipodal geodesic. Its number \(F_n(c)\) of unoriented monochromatic-zero full antipodal geodesics satisfies the all-dimensional estimate
\[
\boxed{F_n(c)\ge\max\{1,\;2^{\lceil(n-1)/2\rceil-3}\}.}
\tag{TE2}
\]

*Proof.* If there is an exceptional direction \(h\), choose it. Otherwise choose any direction. Restrict the other direction-edge color functions to the lower \(h\)-facet, obtaining an arbitrary coloring \(g\) of \(Q_{n-1}\). Every globally simple direction restricts to either a constant function, if it reads \(h\), or a signed one-bit reader. Of the exceptional directions, at most two remain after deleting \(h\). Thus \(g\) meets the lemma's hypotheses, and \(P(g)\) has the bound (TE1). For each antipodal vertex pair contained in \(P(g)\), the odd colors on its two \(h\)-bridges select a color-zero crossing above one favorable root. The universal bridge-splice bijection turns this into a monochromatic-zero full geodesic. Crossings from distinct root pairs are different, so
\[
F_n(c)\ge |P(g)|/2
\ge\max\{1,2^{\lceil(n-1)/2\rceil-3}\}.
\]
\(\square\)

**Corollary (four exceptional directions are necessary).** In any hypothetical legal odd coloring without a monochromatic antipodal full geodesic, at least four distinct direction functions are nonsimple. In Walsh language, at least four direction spins have nonzero Fourier mass on odd levels at least three. This strengthens the earlier two-direction support obstruction using the computer-assisted two-hub theorem.

**Theorem (facetwise three-branching obstruction at minimum dimension).** Assume \(c\) is a bad legal coloring of \(Q_n\) with minimum possible \(n\). For every direction \(h\), let \(g_h\) denote its coloring induced on the facet \(x_h=0\). Then \(P(g_h)=\varnothing\), and **every terminal strongly connected component** of the directed influence graph of \(g_h\) has at least three distinct vertices with internal indegree at least two. In particular it contains at least four directions and is not a directed simple cycle.

*Proof.* If some \(g_h\) had a paired root, the universal bridge criterion would give a monochromatic full geodesic for \(c\), a contradiction. By the converse half of the same criterion, a paired-root-free arbitrary coloring of \(Q_d\) has an odd extension without a monochromatic full geodesic on \(Q_{d+1}\). Since \(c\) is minimum-dimensional, no coloring of a cube of dimension less than \(n-1\) is paired-root-free.

Let \(B\) be any terminal SCC of the influence graph of \(g_h\). If it has at most two branching targets, the established fiberwise two-hub gluing theorem removes \(B\) and shows
\[
|P(g_h)|\ge \rho_B\,|P(g_h|_{Q_{[n]\setminus(\{h\}\cup B)}})|,
\quad \rho_B>0.
\]
The left side is zero, so the smaller induced coloring would have no paired root. Its odd bridge extension would be a bad legal cube coloring of dimension \(n-|B|<n\), contradicting minimality. Thus every terminal SCC has at least three branching targets. Every SCC on at most three directions is reducible by the published small-SCC theorem, so the component has size at least four. \(\square\)

**Closure target.** If a minimum-dimensional bad coloring has only four exceptional directions, the theorem forces a coupled feedback configuration in every facet: deleting any one exceptional direction must leave a terminal SCC containing the other three, each still internally dependent on at least two direction bits. The constraint is imposed simultaneously for all deletion choices, rather than merely on the original influence digraph. A closing proof could attempt to show that these four facetwise feedback structures cannot coexist with antipodal oddness and the square-exchange identities. The present argument does not exclude their coexistence.

## The apex two-hub criterion and vertex-deletion feedback rigidity

For a legal odd edge coloring \(c\) of \(Q_n\), let \(D(c)\) be its directed influence graph on the dimension set: \(j\to i\) means that the direction-\(i\) edge color can change when bit \(j\) is toggled. For an induced digraph \(H\), call an SCC *two-hub reducible* when at most two of its vertices have internal indegree at least two.

**Theorem (apex two-hub NORI1 closure).** Suppose there is a direction \(h\) such that every strongly connected component of the graph \(D(c)-h\) is two-hub reducible. Then \(c\) has a monochromatic antipodal full geodesic. This conclusion allows arbitrarily many nonlinear direction functions and does not bound the ambient dimension.

*Proof.* Let \(g_h\) be the edge coloring induced on the facet \(x_h=0\). Its directed influence graph \(D(g_h)\) is a subgraph of \(D(c)-h\): fixing one bit cannot introduce a dependence on another bit that did not occur in the full coloring. Every SCC of a subgraph lies inside some SCC of the original digraph, and its internal indegree cannot increase. Hence every SCC of \(D(g_h)\) is two-hub reducible. The published two-hub SCC paired-root theorem, whose central nine-sixteenths estimate is computer-assisted, gives \(P(g_h)\ne\varnothing\). The universal antipodal bridge criterion then gives a monochromatic antipodal full geodesic in \(c\), independently of the direction-\(h\) edge colors. \(\square\)

**Corollary (vertex-deletion resilient feedback is necessary).** In every hypothetical bad legal coloring and for every direction \(h\), the induced graph \(D(c)-h\) must contain a strongly connected component with at least three vertices of internal indegree at least two. This is an all-direction graph condition imposed before examining the detailed color values on a facet. A bad coloring cannot have a dimension whose deletion separates all internally branching feedback into one- or two-target SCCs.

**Corollary (four-exception persistence).** Suppose a bad legal coloring has precisely four exceptional direction functions, and write \(H\) for their set. Then for every \(h\in H\), all three vertices of \(H\setminus\{h\}\) belong to a single SCC of \(D(c)-h\), and each has internal indegree at least two within that SCC. The corresponding three functions must also retain at least two active internal bit-dependencies when restricted to the facet \(x_h=0\).

*Proof.* All globally simple direction functions have indegree one. After deleting \(h\), only the three remaining exceptional directions can have internal indegree at least two. The preceding corollary therefore forces all three to be in one SCC with internal indegree at least two. Since \(P(g_h)=\varnothing\), the contrapositive of the two-hub SCC paired-root theorem gives some SCC of \(D(g_h)\) containing at least three branching vertices. Only the three remaining exceptional directions can have such indegrees; hence all three occur in this one SCC and retain the specified internal dependencies. The SCC need not be terminal unless the bad coloring has minimum possible dimension. \(\square\)

**Toward proof closure.** The first unresolved bad configuration must be robust under deletion of every individual dimension: three branching targets must remain strongly feedback-connected somewhere after each deletion. When there are four exceptional directions this demands a common three-target feedback skeleton in every exceptional facet. This offers a global structural alternative to direct path enumeration: analyze the compatibility of the resulting vertex-deletion-resistant influence digraphs with antipodal oddness and with the square-derivative relations of their Boolean edge-color functions. No contradiction for the general skeleton is claimed here.

## Terminal-component elimination and global strong connectivity of minimal obstructions

For a legal antipodally odd coloring \(c\) of the undirected edges of \(Q_n\), let \(D(c)\) be its directed influence graph: \(j\to i\) if the color of a direction-\(i\) edge depends on bit \(j\). Edges point from a bit toward a function reading that bit.

**Theorem (inductive terminal-component elimination).** Suppose NORI1 holds in every dimension below \(n\). If \(D(c)\) is not strongly connected, then \(c\) has a monochromatic antipodal full geodesic. Consequently every counterexample of minimum dimension has a strongly connected influence digraph.

*Proof.* Choose a proper terminal SCC \(B\) of \(D(c)\), and put \(A=[n]\setminus B\ne\varnothing\). No influence arc leaves \(B\) toward \(A\), so all \(A\)-direction edge colors are independent of the \(B\)-bits. Their common restriction \(c_A\) is odd under antipodal inversion of \(Q_A\):
\[
c_{A,i}(\bar x_A)=c_i(\bar x_A,\bar z_B)
=1-c_i(x_A,z_B)=1-c_{A,i}(x_A).
\]
Thus \(|A|\ge2\), since a one-dimensional cube admits no legal antipodally odd undirected-edge coloring: its only edge is fixed by inversion.

By lower-dimensional NORI1, \(c_A\) has a monochromatic-zero full antipodal geodesic \(P_A:x_A\to\bar x_A\). Fix the \(A\)-bits at \(\bar x_A\), giving an arbitrary coloring \(g_B\) of \(Q_B\). Since \(|B|\le n-2\), the dimension \(|B|+1\) falls under the induction hypothesis. The universal paired-root bridge equivalence therefore guarantees \(P(g_B)\ne\varnothing\), and in particular a full geodesic \(P_B:z_B\to\bar z_B\) with word \(0^*1^*\).

Traverse \(P_A\) at fixed \(B\)-bits \(z_B\), then \(P_B\) at fixed \(A\)-bits \(\bar x_A\). This is a complete antipodal geodesic, because the two paths use disjoint direction sets and together use all directions. The first block is all zero, since its edge colors are independent of \(B\)-bits; the second block has word \(0^*1^*\). The concatenation therefore has at most one color change. The established one-change root-slide surgery for legal odd colorings produces a monochromatic full antipodal geodesic. \(\square\)

**Corollary (global and deletion-level rigidity).** In a minimum-dimensional bad legal odd coloring, (i) the entire directed influence graph is strongly connected; (ii) for every removed direction \(h\), the unrestricted coloring on the lower \(h\)-facet has no paired root; (iii) every terminal SCC of each such facet influence graph contains at least three internal branching targets, by the published computer-assisted two-hub theorem and minimum-dimensionality. These conditions are simultaneous, imposed by the same legal coloring.

**Limitation of graph-only closure.** A fully connected feedback graph can satisfy all of the corresponding indegree and deletion-survival requirements. For instance \(c_i(x)=\sum_{j\ne i}x_j\pmod2\) in dimension four is legal and has a complete bidirected influence graph. Every three-direction facet restriction retains a complete feedback triangle with internal indegree two, while the coloring is good by the affine full-rank theorem. An eventual contradiction must use numerical color or path-incidence relations, not strong graph connectivity alone.

The theorem gives an unrestricted-dimensional induction step: any first obstruction is a single strongly connected influence core, rather than a collection of terminal components. It sharpens the earlier connected-interaction-graph reduction.

## Minimal obstruction is a canonical hub-star kernel

Let \(c\) be a legal antipodally odd edge coloring of \(Q_n\). A direction is *simple* if its color is \(a_i+x_{p(i)}\), with \(p(i)\ne i\); let \(H\) contain the other directions, and put \(k=|H|\). Antipodal oddness forces every edge-color function to read at least one bit, and any odd Boolean function reading at most two bits is a signed one-bit reader.

**Compression lemma.** If the directed influence graph is strongly connected, all simple vertices lie in outward rooted trees whose parents eventually reach \(H\). For each branch \(B\) beginning at a child of hub \(h(B)\), let \(a(B)\) be the offset in its leading-edge color \(a(B)+x_{h(B)}\). Group branches by the pair \((h(B),a(B))\), giving \(r\le2k\) nonempty classes \(S_j\) partitioning the simple vertices. For each coset representative \(y\) of the span of their indicator vectors, the compressed coloring \(c_y\) on \(Q_{k+r}\) has hub-edge colors
\[
(c_y)_h(u,s)=c_h\left(u,y+\sum_js_j\mathbf1_{S_j}\right)
\]
and macro-leaf colors \((c_y)_j(u,s)=a(S_j)+u_{h(S_j)}\). This coloring is legal odd, and every monochromatic full antipodal geodesic in it lifts to one in \(c\).

*Proof.* A directed cycle of simple vertices cannot have an incoming arrow from a hub or another vertex, because every simple vertex has only one incoming arrow. Strong connectivity excludes such a cycle, so the unique-predecessor simple graph consists of hub-rooted trees. The compressed antipode complements every represented original bit because the type classes partition all simple bits; hence all compressed colors satisfy oddness. To expand a macro-leaf step of color \(t\), traverse each branch in its class without changing the controlling hub bit. Every leading edge has color \(t\). For descendant \(i\), the requirement \(a_i+x_{p(i)}=t\) prescribes one parent-child precedence relation. An orientation of a tree is acyclic, so these comparisons have a total-order extension, giving a complete all-\(t\) traversal of the branch. After every branch is traversed, the macro class has been flipped, and the next hub step reads the represented original state. Expansion uses every original direction once, respects all colors, and joins antipodes. \(\square\)

**Theorem (minimal hub-star kernel).** If \(c\) is a counterexample of minimum dimension \(n\), then the directed influence graph is strongly connected and every simple direction reads a hub directly. For each hub there is at most one simple leaf colored \(x_h\) and at most one colored \(1+x_h\). Hence
\[
\boxed{n\le3k,\qquad k\ge\max\{4,\lceil n/3\rceil\}.}
\]
*Proof.* Strong connectivity follows from the terminal-SCC induction theorem. If any type class \(S_j\) contained more than one simple direction, then its compressed legal odd coloring would have dimension \(k+r<n\). Minimality makes the compressed coloring good, and the compression lemma lifts its monochromatic full antipodal geodesic to \(c\), a contradiction. Hence every class contains one simple direction, and all branches have size one. There are at most two classes per hub, yielding \(n-k\le2k\). The previously published three-exception closure establishes \(k\ge4\). \(\square\)

Thus a first obstruction with four hubs must occur in a legal odd canonical star with at most twelve directions. This is a proven inductive reduction; it leaves the four-hub kernel existence question open.

## Favorable roots in every bit facet: the simple-bridge induction target

Let \(g\) be an arbitrary binary coloring of the undirected edges of \(Q_m\). Write
\[
A(g)=\{x:\exists\text{ a full antipodal geodesic rooted at }x
\text{ with word }0^*1^*\}.
\]
Define the *facet-hitting property* \(\mathrm{FH}_m\): for every \(g\), every bit position \(j\), and each \(b\in\mathbb F_2\),
\[
\boxed{A(g)\cap\{x:x_j=b\}\ne\varnothing.}
\tag{FH1}
\]
This remains conjectural in unrestricted dimension.

**Theorem (equivalence to odd colorings with a simple bridge).** For every \(m\ge1\), \(\mathrm{FH}_m\) is equivalent to the statement that every legal antipodally odd coloring of \(Q_{m+1}\) whose edge color in at least one direction \(h\) is a signed single-bit reader \(c_h(y)=a+y_j\), \(j\ne h\), admits a monochromatic antipodal geodesic.

*Proof.* Cut the odd colored \((m+1)\)-cube across \(h\). The lower horizontal facet has an unrestricted coloring \(g\), and the upper facet is its antipodally complemented image. The zero-colored bridge selector is the bit facet \(S=\{y:y_j=a\}\). The established bridge-splice bijection says that a monochromatic antipodal geodesic exists if and only if \(S\cap A(g)\ne\varnothing\). Thus (FH1) proves the stated one-reader-bridge closure.

Conversely, for any \(g,j,b\), give a larger cube its lower horizontal coloring \(g\), its upper horizontal coloring the antipodally complemented image of \(g\), and bridge color \(y_j+b\). This is legal odd and has a simple bridge direction. If it is good, the bridge-splice criterion gives a favorable root of \(g\) in the bit facet \(y_j=b\). This is (FH1). \(\square\)

**Theorem (induction reduces the facet-hitting conjecture to strongly connected influence cores).** Suppose \(\mathrm{FH}_d\) holds for all \(d<m\). If the directed influence graph of an arbitrary coloring \(g\) of \(Q_m\) is not strongly connected, then \(g\) satisfies (FH1) for every \(j,b\).

*Proof.* Choose a proper source SCC \(U\) in the influence graph, and put \(V=[m]\setminus U\). No influence arrow enters \(U\) from \(V\), so all \(U\)-direction edge colors are independent of the \(V\)-bits. Their induced coloring \(g_U\) is arbitrary. Fix a desired starting bit \(x_j=b\).

If \(j\in U\), the induction hypothesis supplies a favorable full \(U\)-geodesic from a root with \(j\)-bit \(b\). If \(j\in V\), it supplies any favorable full \(U\)-geodesic. Let \(y\) be the vertex of \(Q_U\) at the zero-to-one division of that path. Fix the \(U\)-bits at \(y\), giving an arbitrary colored \(V\)-cube \(g_{V,y}\). The induction hypothesis supplies a favorable full \(V\)-geodesic, with starting \(j\)-bit \(b\) if \(j\in V\), or any starting root otherwise.

Insert the \(V\)-geodesic at the color-change division of the \(U\)-geodesic. All \(U\)-direction colors remain unchanged because they are independent of \(V\)-bits, while the \(V\)-geodesic is evaluated at fixed \(U\)-bits \(y\). The concatenated word remains \(0^*1^*\), and the full geodesic begins with \(j\)-bit \(b\). Thus (FH1) holds. \(\square\)

**Corollary (conditional closure improvement).** If \(\mathrm{FH}_m\) holds in every dimension, then no bad legal odd coloring has a simple direction. In combination with the canonical hub-star theorem above, a minimum bad coloring would have **every direction exceptional** (no simple leaves). If (FH1) ever fails, the bridge construction furnishes a bad odd coloring with a simple direction in the next dimension. The theorem does not decide which possibility occurs.

**Finite checks and proof status.** A binary integer feasibility formulation can test failure of (FH1): introduce one edge-color bit for each undirected cube edge and, for every dimension order rooted in the selected bit facet, require at least one adjacent color descent \(1\to0\). Auxiliary binary bits mark candidate descents and are constrained above by the color of the first edge and by the complement of the second. Infeasibility is equivalent to (FH1). This formulation was solved as infeasible in dimensions four and five using SciPy/HiGHS; these are computational checks, not a general proof or a published independently checkable certificate. The cross-facet seam geometry for strongly connected unrestricted colorings remains the missing step.


## Empty corridors, component polarization, and localization of paired repairs

The empty-corridor rule must retain the source of the root's failure. An empty full root can arise from incompatible one-sided orientations in independent components, even though every component root supports an orientation. A one-edge paired repair imposes a stronger local condition.

Let \(f=\prod_{\nu=1}^r f_\nu\) be the Cartesian factorization by weak components of its direction-interaction graph. At a root \(x=(x_\nu)\), define its component profile by membership in \(A_0(f_\nu),A_1(f_\nu)\). Paired-root and favorable-root factorization give
\[
A_t(f)=\prod_\nu A_t(f_\nu),\qquad
P(f)=\prod_\nu P(f_\nu).
\]
Call a root *locally empty* in component \(\nu\) when \(x_\nu\) admits neither orientation there. When every component root admits an orientation, the full root is empty precisely when one component is favorable only nondecreasingly and another only nonincreasingly.

**Theorem (an empty antipodal corridor in a reader coloring).** In every dimension \(n\ge6\), there is a legal odd one-reader coloring having a full antipodal geodesic all of whose vertices admit neither monotone orientation.

*Proof.* Use three independent two-direction blocks, with reciprocal readers
\[
f_{2j}=x_{2j+1},\qquad f_{2j+1}=x_{2j}\quad(j=0,1,2).
\]
A block root, encoded by its first bit plus twice its second, has profiles
\[
A_0=\{0,1,2\},\qquad A_1=\{1,2,3\}.
\]
Thus root zero is upward-only, root three downward-only, and roots one and two paired.

Start at full root \(60\), whose three block roots are \((0,3,3)\), and traverse order
\[
\boxed{(2,3,0,1,4,5).}
\tag{EC1}
\]
Its vertex sequence is
\[
\boxed{60,56,48,49,51,35,3.}
\]
First the second block moves \(3\to2\to0\), while the first remains upward-only and the third downward-only. Then the first moves \(0\to1\to3\), while the second is upward-only and the third downward-only. Finally the third moves \(3\to2\to0\), while the first is downward-only and the second upward-only. Every vertex therefore has both one-sided profile types among its factors and is empty. The order flips every direction once and \(3=60\oplus63\).

For larger dimensions add leaf directions \(i\ge6\) with color \(x_0\), leaving every old direction independent of the new bits. The one-way leaf insertion lemma gives
\[
A_t(f^+)=A_t(f)\times\mathbb F_2\quad(t=0,1):
\]
insertion at the appropriate monotone seam proves inclusion, and deleting the added step from a favorable path proves the reverse inclusion because old edge colors remain unchanged. Hence the empty-root set is the old empty-root set times the new bit cube. Traverse all added directions at the initial empty old root and then follow (EC1). This is an empty-root full antipodal geodesic, and every edge-color function remains a legal signed reader. \(\square\)

This shows that empty-corridor exclusion requires more information than reader structure or componentwise paired-root existence. The gate geometry and critical repair ports supply the additional constraints.

**Proposition (two covered components cannot support an empty antipodal path).** Suppose \(f\) has at most two Cartesian factors, and every root of each factor admits at least one orientation. Then no cube path lying entirely in empty roots can join antipodal vertices.

*Proof.* With one factor no root is empty. With two factors an empty root has profiles upward-only/downward-only or downward-only/upward-only. A cube edge changes bits in only one factor, so it cannot connect the two profile combinations while retaining emptiness. Antipodal inversion exchanges upward and downward profiles in each factor by path reversal. Therefore antipodal empty roots lie in different components of the induced empty-root graph. \(\square\)

### A repaired empty root has an empty component

**Lemma (two new orientations through one edge splice monochromatically).** Suppose an ordinary coloring \(f'\) differs from \(f\) on one edge \(e\). If a root \(x\) is empty in \(f\) and paired in \(f'\), then \(f'\) has a monochromatic full geodesic from \(x\) through \(e\).

*Proof.* Both new monotone witnesses must traverse \(e\); a witness avoiding it would already give an orientation in \(f\). Their traversal direction on \(e\) is the same, because the starting bit of its direction is fixed and is flipped only once. Their prefixes ending at its far endpoint use the same direction set, determined by the displacement from \(x\) to that endpoint.

If the repaired edge has color zero, splice the nondecreasing witness's zero prefix through \(e\) to the nonincreasing witness's zero suffix after \(e\). If it has color one, splice the nonincreasing one's one prefix to the nondecreasing one's one suffix. The shared prefix-direction set ensures no direction is repeated or omitted. \(\square\)

**Theorem (localization of a one-edge paired repair at an empty root).** Let \(B\) be the original Cartesian component containing the direction of \(e\). Under the preceding lemma's hypotheses,
\[
\boxed{x_B\notin A_0(f_B)\cup A_1(f_B).}
\tag{EC2}
\]
For some color \(t\), every other component supports a monochromatic full color-\(t\) geodesic from its starting root \(x_\nu\).

*Proof.* In \(f\), the spliced path has all edges of one color \(t\) except \(e\). Its projection to every component other than \(B\) is a monochromatic full geodesic in the original coloring. Its projection to \(B\) contains the sole exception.

If \(x_B\) admitted either monotone orientation in \(f_B\), use that full \(B\)-path and insert every unaffected monochromatic component path at its color-change division, in the phase matching \(t\). Original component independence preserves all edge colors. This gives a full monotone path in \(f\) from \(x\), contrary to emptiness. Hence (EC2) holds. \(\square\)

The repaired coloring may acquire new dependencies on other components; the theorem uses only the original factorization and the original colors along the spliced path.

**Corollary (polarization-only empty roots resist a one-edge paired repair).** When every original component root admits at least one orientation, changing one arbitrary edge cannot turn an empty full root into a paired root. In particular no vertex of (EC1) can be healed in this way.

**Coupling to Article XIV.** A separately certified gate forces the neighboring face root to be empty. A monochromatic codimension-two face path certifies gates at its two endpoints; the former inference of gates at every interior vertex has been withdrawn in the corrected folding and transverse-strip subsections. Thus the following coupling applies at certified gate sites, without assuming a gate throughout the corridor. If a critical one-edge repair produces paired witnesses at one of those roots, (EC2) locates a component that is itself empty there, and every unaffected factor must provide a common-color monochromatic path. The repair therefore resolves a local feedback obstruction at that prescribed root. Independent components with opposing one-sided orientations can supply an empty corridor, but cannot supply such a paired repair.

This separates two structural sources of the corridor and narrows the missing induction: transport the critical witness into its locally empty component, preserving its seam and direction set, and then apply the rooted feedback exclusions or cross-profile stripe rule. The original causal transport obstruction still prevents an automatic passage to a different favorable root.

**Independent checks.** The block profiles and all seven vertices of (EC1) were directly evaluated. The repair-splice theorem follows from the shared displacement direction set and does not use enumeration.

## Zero/one crossing gates for a prescribed root facet

Let \(f_0,f_1\) be arbitrary binary colorings on two horizontal copies of \(Q_m\), and let \(h(z)\) color the joining edge above \(z\in Q_m\). Define \(Z\) as the sites above which a full geodesic from some lower-layer root can cross with an all-zero lower horizontal prefix and a \(0^*1^*\) upper horizontal suffix. Define \(O\) as the sites permitting a lower \(0^*1^*\) prefix and an all-one upper suffix. The two segments together traverse each horizontal direction once; empty segments are allowed. The gate sets depend on \(f_0,f_1\) only.

**Theorem (crossing-gate completion face).** The assembled coloring has no \(0^*1^*\) full antipodal geodesic starting in its lower root facet precisely when
\[
\boxed{h(z)=1\ (z\in Z),\qquad h(z)=0\ (z\in O).}
\tag{BG1}
\]
These bridge assignments exist precisely if \(Z\cap O=\varnothing\); their number is then \(2^{2^m-|Z\cup O|}\).

*Proof.* With a zero bridge, a favorable word must have only zeros before the bridge and a nondecreasing word afterward. With a one bridge, it must have a nondecreasing prefix and only ones afterward. Thus favorable paths are present at the indicated gate sites precisely for the respective bridge bit. Avoiding every such path forces the opposite bit. Conflict occurs at an intersection site; otherwise one independent bridge bit is fixed per site of the union. \(\square\)

**Lemma (endpoint gates).** If \(A(f)\) denotes roots of full \(0^*1^*\) geodesics, then
\[
\boxed{A(f_1)\subseteq Z,\qquad\overline{A(f_0)}\subseteq O.}
\tag{BG2}
\]
Hence a coloring with no favorable root in the lower facet must have
\[
\boxed{A(f_1)\cap\overline{A(f_0)}=\varnothing,\qquad
|A(f_0)|+|A(f_1)|\le2^m.}
\tag{BG3}
\]
*Proof.* A favorable upper full geodesic rooted at \(z\) may follow a zero bridge first. A favorable lower full geodesic rooted at \(\bar z\) may precede a one bridge last. These yield the inclusions, and the gate theorem gives the separation. \(\square\)

**Corollary (both root facets covered for every bridge assignment).** If
\[
\boxed{A(f_1)\cap\overline{A(f_0)}\ne\varnothing,}
\tag{BG4}
\]
then each of the two root facets has a favorable full antipodal geodesic, whatever \(h\) is. This holds, in particular, when \(|A(f_0)|+|A(f_1)|>2^m\).

*Proof.* A vertex in the intersection supplies both gate colors; hence a favorable path from the lower layer exists for either choice of its bridge bit. Interchanging layers sends the intersection into its antipodal image \(\overline{A(f_1)}\cap A(f_0)\), proving the upper-layer claim. The cardinality condition forces intersection by inclusion-exclusion. \(\square\)

**Corollary (two independent two-hub facet colorings).** If each horizontal coloring is a two-hub star with arbitrary nonlinear hub functions and signed one-bit leaf readers, then the published computer-assisted theorem gives \(|A(f_b)|\ge(9/16)2^m\) in each layer. Their combined favorable-root counts exceed \(2^m\). Therefore both root facets remain favorable for every vertical edge-color assignment, even if the two layers have unrelated hub functions, offsets, and reader patterns.

This gives the crossing-site interpretation of the general one-direction completion Boolean-face theorem published separately. The bit-facet hitting conjecture is equivalent to demanding \(Z\cap O\ne\varnothing\) for every pair of unrestricted horizontal colorings. Any obstruction has the cross-facet separation (BG3); a closing argument must then force internally crossing gate witnesses. Formula (BG1) was checked on 100 randomly generated four-cube horizontal interfaces and 45 vertical assignments per interface.

## Cross-coloring condensation and apex facet coverage

Let \(f,g\) be arbitrary binary edge colorings of \(Q_m\). Assume a common directed influence supergraph \(D\) contains every arc \(j\to i\) along which either color of direction \(i\) depends on bit \(j\). Suppose each strongly connected component of \(D\) has at most two vertices with internal indegree greater than one.

**Theorem (opposed favorable roots of distinct colorings).** The favorable root sets for \(0^*1^*\) complete geodesics satisfy
\[
\boxed{A(f)\cap\overline{A(g)}\ne\varnothing.}
\tag{CC1}
\]

*Proof.* Induct on the dimension. Choose a terminal strongly connected component \(B\) of \(D\), and write \(U=[m]\setminus B\). Because no arc goes from \(B\) to \(U\), the colors of \(U\)-direction edges in both colorings are independent of \(B\)-bits. Their restrictions \(f_U,g_U\) share influence supergraph \(D[U]\); by induction choose favorable full \(U\)-paths from antipodal starting roots \(x,\bar x\).

Let \(u,v\) be the zero-to-one seam vertices of these two paths. The induced \(B\)-fiber colorings \(f_{B,u},g_{B,v}\) have their internal dependency arcs contained in \(D[B]\). The existing component theorems give a strict favorable-root majority in *each* fiber, uniformly over all outside bit assignments: density one for a singleton SCC; at least \(1-2^{-|B|}\) for a simple reader cycle and its inactive-edge subgraphs; at least \(3/4\) for a one-branching-target rooted feedback component; and at least \(9/16\) for a two-branching-target component, by the computer-assisted two-hub theorem and its inactive-parent extension. In every case both fiber favorable sets exceed half the cube, so
\[
A(f_{B,u})\cap\overline{A(g_{B,v})}\ne\varnothing.
\]
Choose a root \(z\) in this intersection. Insert the favorable \(f\)-fiber path rooted at \(z\) into the \(f_U\)-seam \(u\), and the favorable \(g\)-fiber path rooted at \(\bar z\) into the independent \(g_U\)-seam \(v\). The outer edge colors do not depend on \(B\)-bits, so both insertions preserve their respective \(0^*1^*\) words and traverse each direction once. The resulting favorable paths begin at antipodal roots \((x,z)\) and \((\bar x,\bar z)\). \(\square\)

**Theorem (two-hub apex facet coverage without oddness).** Let \(F\) be an unrestricted edge coloring of \(Q_{m+1}\), and suppose a direction \(j\) can be deleted from its influence graph so that every remaining SCC has at most two vertices of internal indegree greater than one. Then **each** of the two bit facets \(x_j=0\) and \(x_j=1\) contains a starting root of a full \(0^*1^*\) geodesic, independently of how the direction-\(j\) edges are colored.

*Proof.* The horizontal colorings \(f_0,f_1\) of the two \(j\)-facets share the common influence supergraph \(D(F)-j\). The preceding theorem gives \(A(f_1)\cap\overline{A(f_0)}\ne\varnothing\). The crossing-gate theorem (BG4) then yields favorable complete paths from both starting facets for every assignment to the joining edges. \(\square\)

**Corollary (three exceptional directions).** An arbitrary cube coloring with at most three edge-direction functions other than constants or signed one-bit readers has favorable roots in both bit facets of **every exceptional direction**. For any such direction \(j\), deletion leaves at most two potentially branching vertices in the common influence graph. This applies in unbounded dimension and does not assume antipodal oddness.

**Necessary obstruction.** A counterexample to bit-facet hitting at a particular direction \(j\) must have some SCC in the influence graph after deleting \(j\) with at least three distinct vertices of internal indegree at least two. This is a condition on the horizontal dependencies alone, stronger than requiring global influence connectivity.

The new proof is the cross-coloring seam induction: the computer-assisted ingredient is the published \(9/16\) two-hub favorable-root bound, not the induction itself. Independent direct path enumeration verified the cross-favorable conclusion on 100 randomly sampled pairs of independent two-hub colorings in each of dimensions four, five and six.

## Opposed-root multiplicity and flat square derivatives

For a directed influence graph \(D\) whose SCCs each have at most two vertices of internal indegree greater than one, assign a factor
\[
\lambda(B)=
\begin{cases}
2,&|B|=1,\\
2^{|B|}-2,&B\text{ is a directed cycle},\\
2^{|B|-1},&B\text{ has one branching target},\\
2^{|B|-3},&B\text{ has two branching targets}.
\end{cases}
\]
The terminal-component induction proving opposed favorable-root existence also proves the quantitative bound
\[
\boxed{|A(f)\cap\overline{A(g)}|
\ge\prod_{B\in\operatorname{SCC}(D)}\lambda(B)>0.}
\tag{CD1}
\]
Indeed each opposed favorable root of the outer coloring has at least \(\lambda(B)\) inner choices: the respective fiber favorable sets have densities one, at least \(1-2^{-|B|}\), at least \(3/4\), or at least \(9/16\) in these four component classes. Inclusion-exclusion yields the factors. The two-hub factor depends on the previously published computer-assisted theorem.

Now fix a legal antipodally odd coloring \(c\) of \(Q_n\), with distinct directions \(h,j\). Restrict to the facet \(x_h=0\), and then cut across \(j\), yielding arbitrary colorings \(f_{00},f_{01}\) of \(Q_{n-2}\). Put
\[
L_{h,j}=A(f_{01})\cap\overline{A(f_{00})},
\qquad
\partial_hc_j(z)=c_j(z,h=0)+c_j(z,h=1)\pmod2.
\]

**Theorem (cross-witness derivative vanishing).** If \(c\) has no monochromatic full antipodal geodesic, then
\[
\boxed{L_{h,j}\subseteq\{z:\partial_hc_j(z)=0\}.}
\tag{CD2}
\]
Moreover \(\partial_hc_j(\bar z)=\partial_hc_j(z)\), so it also vanishes on the antipodal image of \(L_{h,j}\).

*Proof.* The bridge equivalence makes the facet coloring at \(h=0\) paired-root-free. Take \(z\in L_{h,j}\). If its two vertical direction-\(j\) edges above \(z,\bar z\) within that facet had equal colors, the endpoint construction yields paired favorable roots. When both edges are zero, cross them first from the antipodal roots \((z,0)\) and \((\bar z,1)\), then follow the favorable upper and lower paths rooted at \(z,\bar z\). When both are one, use the favorable horizontal paths first from antipodal roots \((\bar z,0)\) and \((z,1)\), then cross the edges last. Both cases contradict paired-root-freeness. Therefore
\(c_j(z,h=0)+c_j(\bar z,h=0)=1\).
Global antipodal oddness gives
\(c_j(\bar z,h=0)=1+c_j(z,h=1)\), so \(\partial_hc_j(z)=0\). Complementing all remaining input bits shows the derivative is antipodally even. \(\square\)

**Corollary (four-hub uniform-coupling exclusion).** Suppose a legal odd coloring has at most four nonsimple direction functions. If two distinct nonsimple directions \(h,j\) satisfy \(\partial_hc_j\equiv1\), then the coloring has a monochromatic full antipodal geodesic.

*Proof.* If it were bad, deleting \(h,j\) would leave at most two branching direction functions, so the common-influence root bound (CD1) would give \(L_{h,j}\ne\varnothing\). The preceding theorem would then force \(\partial_hc_j=0\) at a member of this set, a contradiction. \(\square\)

In particular, a hypothetical four-hub minimal obstruction has, for every ordered pair of different hubs \(h,j\), the quantitative restriction
\[
\boxed{
|\{z:\partial_hc_j(z)=0\}|
\ge\prod_{B\in\operatorname{SCC}(D(c)-\{h,j\})}\lambda(B)>0.
}
\tag{CD3}
\]
Every present hub-to-hub dependency must therefore switch its activity with other input bits; no such edge can be a uniform affine coupling. A closure argument should force a nonzero square derivative at one of the opposed favorable-root sites, contradicting (CD2).

### A five-cube warning: active derivatives can avoid every cross-witness site

The preceding square-flatness theorem is a necessary condition for a **bad** coloring. Its converse cannot be obtained from antipodal oddness alone: an active derivative need not intersect the opposed favorable-root witness set. The following small construction makes this precise.

Use directions \((h,j,a,b,t)\) of \(Q_5\), and let \(p=x_a+x_b+x_t\pmod2\). Define
\[
\boxed{
\begin{aligned}
c_h(x)&=x_a,\\
c_j(x)&=p+\mathbf1_{\{x_a=x_b=x_t=1-x_h\}}\pmod2,\\
c_a(x)&=1+x_b,\qquad c_b(x)=1+x_a,\qquad c_t(x)=x_h.
\end{aligned}}
\tag{W1}
\]
Each edge-color function is independent of its own direction bit. The three-bit parity \(p\) changes under antipodal inversion, while the indicator in \(c_j\) remains invariant; all other functions are signed readers. Thus \(c\) is legal antipodally odd.

On the facet \(h=0\), the two subfacets \(j=0\) and \(j=1\) have the same horizontal three-cube coloring
\[
f_a=1+x_b,\qquad f_b=1+x_a,\qquad f_t=0.
\]
With the three-bit root encoding \(z=x_a+2x_b+4x_t\), its favorable-root set is
\[
A(f)=\{1,2,3,5,6,7\}.
\]
Consequently the opposed witness set is
\[
\boxed{L_{h,j}=A(f)\cap\overline{A(f)}=\{1,2,5,6\}.}
\tag{W2}
\]
On the other hand
\[
\boxed{\{z:\partial_hc_j(z)=1\}=\{0,7\}.}
\tag{W3}
\]
The derivative is nonzero but its active sites avoid the entire opposed witness set. Nonetheless this coloring is good: starting from the cube vertex \(x=4\) (only \(x_a=1\)), the direction order \(h,j,a,b,t\) has color word \(11111\).

The favorable-root sets, derivative support, legal oddness, and displayed monochromatic path were independently checked by finite enumeration. This example rules out the unconditional statement that every active square derivative must meet the opposed favorable-root set. A closing argument based on (CD2) must exploit counterexample minimality, gauge criticality, or additional simultaneous constraints across hub pairs; square oddness and active influence alone are insufficient.

## Leaf-root surjectivity and a nonlinear hub-coupling closure class

**Lemma (prescribed constant-block roots).** Let \(f,g\) be binary edge colorings of the same \(Q_m\), with a common directed influence supergraph \(D\) whose strongly connected components each contain at most two vertices of internal indegree greater than one. Let \(S\) be a set of directions whose edge colors are constant in each of the two colorings, possibly with different constants. Then for every starting assignment \(u\in\mathbb F_2^S\) there is a root
\[
\boxed{x\in A(f)\cap\overline{A(g)},\quad x_S=u.}
\tag{LS1}
\]
The number of such roots is at least \(\prod_{B\in\operatorname{SCC}(D[[m]\setminus S])}\lambda(B)\), with the component factors established in (CD1).

*Proof.* The constant-colored \(S\)-directions admit a full \(0^*1^*\) geodesic from *every* root, obtained by listing all zero directions before all one directions. In \(f\) choose such a path from \(u\), and in \(g\) choose one from \(\bar u\). Let their zero-to-one seams occur at \(S\)-vertices \(v_f,v_g\). The induced colorings on \(T=[m]\setminus S\) at these two seam assignments share the influence supergraph \(D[T]\), hence by the quantitative cross-coloring condensation theorem have at least the displayed number of opposed favorable-root choices \(z,\bar z\). Insert the two \(T\)-geodesics at their respective \(S\)-seams. Since the \(S\)-edge colors are constant, the resulting complete paths preserve the nondecreasing color words and start at antipodal roots \((u,z),(\bar u,\bar z)\). \(\square\)

**Theorem (closure for leaf-supported hub derivatives).** Suppose a legal odd coloring \(c\) of \(Q_n\) has at most four nonsimple direction functions. Choose two distinct nonsimple directions \(h,j\). Let \(S_{h,j}\) consist of simple directions whose edge colors read only \(h\) or only \(j\):
\[
c_s(x)=a_s+x_h\quad\text{or}\quad c_s(x)=a_s+x_j.
\]
Assume the Boolean square derivative
\[
\partial_h c_j(z)=c_j(z,h=0)+c_j(z,h=1)
\]
depends only on the bits of \(S_{h,j}\). If \(\partial_hc_j\) is nonzero at any input, then
\[
\boxed{c\text{ possesses a monochromatic antipodal full geodesic}.}
\tag{LS2}
\]

*Proof.* Suppose \(c\) were bad. Delete direction \(h\), fix its bit to zero, then split the resulting facet along \(j\) into colorings \(f_{00},f_{01}\) on the remaining \(n-2\) directions. Every direction of \(S_{h,j}\) becomes constant-colored in both horizontal colorings, because its only reader is a fixed deleted bit. At most two nonsimple direction functions remain, so the common influence graph after deleting \(h,j\) has no SCC with more than two branching vertices.

Apply (LS1) to \(f=f_{01}\), \(g=f_{00}\). For every assignment \(u\) of the bits in \(S_{h,j}\), the opposed favorable-root set
\(L_{h,j}=A(f_{01})\cap\overline{A(f_{00})}\)
contains a root with that assignment. The previously proved square-flatness theorem (CD2) says \(\partial_hc_j\) vanishes at every such root whenever \(c\) is bad. Because its value depends only on \(u\), it must vanish for all assignments, contradicting the hypothesis that it is nonzero somewhere. \(\square\)

This strengthens the uniform active-coupling exclusion: a four-hub obstruction cannot have a nonzero hub-to-hub interaction whose activity is controlled solely by simple leaf bits attached to the two participating hubs, even when that control function is nonlinear. In a canonical minimal hub-star kernel, any present feedback arc between distinct hubs must have activity depending on a bit outside those two hubs' simple leaf sets. The result is dimension-uniform but does not rule out interactions controlled by other hubs or their leaf bits.
\n\n## Finite hub kernel certification\n\nThe four-hub canonical stars in dimensions seven through ten were tested with exhaustive Boolean solvers. All nine leaf-pattern instances were unsatisfiable. Thus the first bad four-hub kernel, if any, occurs in dimension eleven or twelve. Complete generators and checks are preserved in the local research artifacts.\n
Reproduction: sat_hub_slots.py checks hub-step orders with leaf slots; sat_hub_kernel.py checks full direction orders. The n=7 and n=8 results agree in both constructions. Further n=9 and n=10 runs each return unsatisfiable.


## Arc-disjoint feedback necessary in every odd cube obstruction

For a binary edge coloring \(f\) of a cube, let \(D(f)\) have an arrow \(i\to j\) if direction-\(j\) edge colors may depend on bit \(i\).

**Lemma (acyclic root saturation).** If \(D(f)\) is acyclic, every starting root has a full antipodal geodesic with color word \(0^*1^*\). Traverse unused zero-colored edges until none remain. All remaining colors are then one. Repeatedly traverse a sink in the induced influence graph on unused directions: its bit is not read by any other unused direction, so their colors remain one. This gives the desired full path from the arbitrary starting root.

**Theorem (arc-complement cycle condition).** If a legal antipodally odd coloring \(c\) of \(Q_n\) is bad, then for every influence arc \(h\to j\) in \(D(c)\), the digraph \(D(c)-\{h,j\}\) contains a directed cycle.

*Proof.* Suppose the complement of an arc is acyclic. Fix the \(h\)-bit zero, and split this facet into its two \(j\)-layers. Each resulting horizontal edge coloring has acyclic influence graph and therefore has a favorable full path from every root. Hence their opposed favorable-root witness set is the entire remaining vertex cube. The square-flatness theorem previously proved in this Subsection says that badness forces \(\partial_hc_j\) to vanish at every such root. Thus \(\partial_hc_j\equiv0\), contradicting the assumed influence arc. \(\square\)

**Corollary (arc endpoint sets do not meet every cycle).** In a bad legal odd coloring, the endpoints of any influence arc fail to form a directed feedback vertex set: at least one directed cycle survives their deletion.

*Proof.* This is the preceding arc-complement cycle condition. A surviving cycle avoids the two endpoints; its vertices may meet other vertices of a cycle containing the selected arc. A conclusion about vertex-disjoint cycle packing requires an additional argument.

## Two-vertex feedback elimination by a monochromatic hub connector

Let \(D(c)\) be the directed influence graph of a legal antipodally odd undirected-edge coloring of \(Q_n\). A *feedback vertex set* \(H\) is a set of dimensions whose deletion makes the induced digraph acyclic.

**Theorem (two-vertex feedback closure).** If \(D(c)\) has a feedback vertex set of size at most two, then \(c\) has a monochromatic full antipodal geodesic. Consequently every minimum-dimensional bad legal coloring has directed feedback vertex number at least three.

*Proof.* If \(D(c)\) is acyclic, the all-root acyclic greedy theorem gives a full \(0^*1^*\) geodesic, converted to monochromatic by root-slide surgery. If a feedback vertex set is a singleton \(h\), choose any influence arc incident with \(h\). Removing that arc's endpoints also removes \(h\), leaving an acyclic digraph; the arc-complement cycle theorem immediately gives a monochromatic geodesic.

Now let \(H=\{h,j\}\) be a feedback vertex set, with nonempty acyclic complement \(S\). If an influence arc joins \(h\) and \(j\) in either direction, deleting these two endpoints leaves an acyclic graph, and the arc-complement theorem applies.

Suppose neither hub reads the other. Their edge-color functions therefore depend only on the \(S\)-bits, say \(b_h(z),b_j(z)\), and satisfy \(b_h(\bar z)=1+b_h(z)\) and similarly for \(b_j\).

If they agree at some \(z\), they also agree with the opposite color at \(\bar z\). Hence choose a site where both hub edges are zero. Traverse \(h,j\) first at that site; the two edges have color zero and do not affect one another's colors. In the resulting fixed hub layer, the \(S\)-direction influence graph is acyclic. Its all-root theorem provides a favorable full \(S\)-geodesic starting at \(z\). Concatenation has word \(0^*1^*\).

It remains to suppose \(b_j(z)=1+b_h(z)\) for every \(z\). The odd function \(b=b_h\) is nonconstant on \(S\); choose a direction \(s\in S\) and a site \(z\) where \(b(z\oplus e_s)=1+b(z)\). Put \(t=b(z)\). Fix the other \(S\)-bits at \(z\). If the direction-\(s\) edge color takes the value \(t\) at some choice of the two hub bits, choose the initial hub bits so that, after traversing \(h\), its value is \(t\). Then the three-step block
\[
\boxed{h,\ s,\ j}
\]
is monochromatic of color \(t\): the first hub edge has color \(t\), the middle edge was chosen color \(t\), and the final hub edge has color \(1+b(z\oplus e_s)=t\). If no hub-bit choice gives color \(t\) on the \(s\)-edge at this fixed \(S\)-site, its color is identically \(1+t\) on all four hub-bit assignments. In this case the three-step block
\[
\boxed{j,\ s,\ h}
\]
is monochromatic of color \(1+t\). The first edge has color \(1+t\), the middle edge has that fixed color, and the last edge has color \(b(z\oplus e_s)=1+t\).

Thus some complete traversal of the three directions \(C=\{h,j,s\}\), at the fixed other \(S\)-bits, is monochromatic of a color \(q\). Put \(T=S\setminus\{s\}\), whose induced influence graph is acyclic. If \(q=0\), traverse this block first and then, at the resulting fixed \(C\)-state, use the all-root acyclic theorem to traverse every direction of \(T\) with word \(0^*1^*\). If \(q=1\), first traverse all \(T\)-directions with a favorable full geodesic ending at the prescribed \(T\)-site \(z_T\), with the \(C\)-bits fixed at the block's starting values, and then traverse the monochromatic-one block. Either concatenation traverses every direction once and has word \(0^*1^*\). Root-slide surgery finishes the proof. \(\square\)

**Inductive significance.** A hypothetical minimal counterexample must have directed feedback vertex number at least three, even if many nonhub directions have arbitrary nonlinear functions and high internal indegrees. The two-hub argument uses only the acyclic greedy lemma, antipodal oddness, and a three-step monochromatic connector; it does not invoke the finite two-hub certificate. A natural next target is to construct analogous bounded-length connectors from three feedback directions and an acyclic exterior.


## Prescribed roots on acyclic source blocks and feedback-dependent activity

Write \(A_0(f)\) for roots admitting a full path with word \(0^*1^*\), and \(A_1(f)\) for roots admitting a full path with word \(1^*0^*\).

**Lemma (source-block cross gluing).** Let \(f,g\) be ordinary binary edge colorings on \(Q_{S\cup T}\). Suppose their common influence supergraph has no arrow from \(T\) into \(S\), and its restriction to \(S\) is acyclic. For each pair of assignments \(v,w\in\mathbb F_2^S\), suppose the two induced \(T\)-colorings satisfy
\[
|A_0(f_{T,v})\cap A_1(g_{T,w})|\ge \kappa>0.
\]
Then, for every prescribed assignment \(u\in\mathbb F_2^S\),
\[
\boxed{|\{x\in A_0(f)\cap A_1(g):x_S=u\}|\ge\kappa.}
\tag{AS1}
\]

*Proof.* The acyclic root-saturation lemma, applied also after interchanging the colors, gives an increasing full \(S\)-path for \(f\) and a decreasing full \(S\)-path for \(g\), both starting at \(u\). Let \(v,w\) be their respective change-of-color seams. Choose any cross root \(z\) for \(f_{T,v},g_{T,w}\). Insert the increasing and decreasing \(T\)-paths at the corresponding seams. The \(S\)-edge colors do not depend on the \(T\)-bits, so both inserted paths preserve the required color words. They start at the same full root \((u,z)\). Distinct choices of \(z\) give distinct roots. Empty blocks and paths with a single color are included by allowing endpoint seams. \(\square\)

The hypothesis on the \(T\)-fibers is available from each of the following established modules: the common directed influence theorem with at most two internal branching targets per strongly connected component; the universal cross-favorability theorem for a common linear-forest interaction graph; or the Hall theorem for two independently functional colorings. The last module does not require the two fiber colorings to have the same reader map. This source-block statement prescribes exterior source bits, and therefore does not assert the endpoint prescription that fails for general path-local pairs.

**Theorem (acyclic-source activity exclusion).** Let \(c\) be a legal antipodally odd coloring, and choose distinct directions \(h,j\). In the residual influence digraph \(D(c)-\{h,j\}\), let \(S\) be a source-closed acyclic set and put \(T=[n]\setminus(\{h,j\}\cup S)\). Assume that every pair of \(T\)-fibers of the two horizontal colorings \(f_{01},f_{00}\) satisfies one of the cross-favorability modules above. If the nonzero Boolean derivative \(\partial_hc_j\) depends only on bits in \(S\), then \(c\) has a monochromatic full antipodal geodesic.

*Proof.* If \(c\) were bad, square flatness (CD2) would force \(\partial_hc_j=0\) on
\[
L_{h,j}=A_0(f_{01})\cap A_1(f_{00}).
\]
By (AS1), this set contains a root over every assignment of the \(S\)-bits. A derivative depending only on those bits must consequently vanish everywhere, contrary to the hypothesis. \(\square\)

More generally, badness forces at least \(\kappa\) zeros of the derivative in every prescribed \(S\)-fiber. This replaces the constant-block conclusion (LS1) by an arbitrarily large acyclic source block, including directed source trees with nonlinear direction functions.

**Corollary (activity must use surviving feedback descendants).** Let \(S\) comprise all vertices of \(D(c)-\{h,j\}\) which are not reachable from a directed cycle. This set is source-closed and acyclic: an arrow into it from a cycle descendant would make its target a cycle descendant, and a cycle inside it would contradict its definition. Under the same fiber hypotheses, if \(c\) is bad and \(h\to j\) is an influence arc, then some \(v\in T\) satisfies
\[
\boxed{\partial_v\partial_hc_j\not\equiv0.}
\tag{AS2}
\]
Indeed, the influence arc makes \(\partial_hc_j\) nonzero. If all its derivatives in \(T\) vanished, it would depend only on \(S\), contradicting the preceding theorem. The bit \(v\) need only be downstream of a surviving directed cycle; it need not lie on the cycle itself.

In particular, the fiber hypothesis holds when \(c\) has at most four nonsimple direction functions and \(h,j\) are two of them. Deleting these two directions leaves at most two possible branching targets, and restriction to \(T\) cannot add others. Thus every active hub-to-hub derivative in a bad four-hub coloring must have a nonzero mixed derivative with a bit downstream of residual feedback.

**Path toward closure.** The arc-complement condition supplies surviving feedback; (AS2) now requires that feedback to control the activity of each participating coupling. A closing argument must show that these mixed-derivative requirements either expose a square at a cross-favorable root or admit a feedback-reducing monochromatic connector. Neither conclusion follows from the projection lemma alone. In particular, it does not supply arbitrary prescribed roots in the residual feedback block, and it does not upgrade cycle survival to vertex-disjoint cycle packing.


## Simultaneous prescribed roots outside all directed cycles

Let \(f,g\) be arbitrary binary edge colorings on \(Q_d\), and let \(D\) be a common directed influence supergraph. An arc \(i\to j\) permits the direction-\(j\) edge color in either coloring to depend on bit \(i\). Let \(B_1,\ldots,B_t\) be the strongly connected components in a topological order, and put \(R_\nu=B_1\cup\cdots\cup B_{\nu-1}\). Define
\[
\rho_\nu=\min_{v,w\in Q_{R_\nu}}
\left|A_0(f^{(\nu)}_v)\cap A_1(g^{(\nu)}_w)\right|,
\]
where \(f^{(\nu)}_v,g^{(\nu)}_w\) are the induced \(B_\nu\)-colorings at the stated earlier-bit assignments. Later bits cannot affect these colorings.

Let \(S\) be the set of vertices of \(D\) belonging to no directed cycle. Since influence graphs have no loops, these are precisely the singleton strongly connected components. Put \(T=[d]\setminus S\).

**Theorem (simultaneous prescription on all singleton components).** If \(\rho_\nu>0\) for every nonsingleton component, then every prescribed assignment \(u\in Q_S\) satisfies
\[
\boxed{
\left|\{x\in A_0(f)\cap A_1(g):x_S=u\}\right|
\ge\prod_{\nu:\,|B_\nu|\ge2}\rho_\nu>0.
}
\tag{SPC1}
\]
No restriction on arrows between \(S\) and \(T\) is imposed.

*Proof.* Process the components in their topological order. Maintain roots on the processed dimensions admitting both an \(f\)-path with word \(0^*1^*\) and a \(g\)-path with word \(1^*0^*\), while satisfying all prescriptions in the processed singleton components.

At a nonsingleton component \(B_\nu\), choose one witness of each orientation at a retained root, and let \(v,w\) be their respective phase seams. There are at least \(\rho_\nu\) common roots for the two induced \(B_\nu\)-colorings. Insert their two full monotone paths at the corresponding seams. Earlier edge colors are independent of the \(B_\nu\)-bits, so the enlarged paths retain their monotone words. Each old root therefore has at least \(\rho_\nu\) extensions.

At a singleton component \(\{i\}\), use its prescribed starting bit \(u_i\). Its induced edge has a constant color in each of the two seam fibers, and its one-step path has both monotone orientations. Inserting it at each seam preserves both full words. This extends every old root with the prescribed bit and imposes no further restriction.

Starting from the empty root and multiplying the nonsingleton extension counts proves (SPC1). \(\square\)

Thus one can prescribe source singletons, singletons between feedback components, and terminal singletons simultaneously. The cross-root choices in the nonsingleton components can depend on all prescriptions; the theorem asserts projection surjectivity and a lower bound in every prescribed fiber.

For the known cross-favorability modules it suffices that every conditional pair in each nonsingleton component lies in the relevant class. In particular, the hypothesis holds if every component of \(D\) has at most two vertices of internal indegree greater than one, by the established two-target theorem, including its stated computer-assisted ingredient.

**Corollary (square-derivative activity must involve a surviving cycle vertex).** Let \(c\) be an antipodally odd coloring, fix distinct directions \(h,j\), and set \(D'=D(c)-\{h,j\}\). Suppose every nonsingleton component of \(D'\) satisfies the preceding conditional cross-favorability hypothesis for the two horizontal colorings \(f_{01},f_{00}\). If \(c\) is bad and \(h\to j\) is an influence arc, then some vertex \(v\) lying on a directed cycle of \(D'\) satisfies
\[
\boxed{\partial_v\partial_hc_j\not\equiv0.}
\tag{SPC2}
\]

*Proof.* Let \(S\) consist of the vertices lying on no directed cycle of \(D'\), and let \(T\) be its complement. The theorem supplies a cross root in
\[
L_{h,j}=A_0(f_{01})\cap A_1(f_{00})
\]
over every assignment of the \(S\)-bits. Badness forces \(\partial_hc_j=0\) at all these cross roots by square flatness. If \(\partial_v\partial_hc_j\) vanished for every \(v\in T\), then \(\partial_hc_j\) would depend only on \(S\). Its vanishing at a cross root over every \(S\)-assignment would make it identically zero, contradicting \(h\to j\). Thus a vertex \(v\in T\) satisfies (SPC2), and every member of \(T\) lies on a directed cycle. \(\square\)

**Corollary (four exceptional directions).** If \(c\) has at most four direction-edge functions that are not signed one-bit readers, and \(h,j\) are two of them, then every bad coloring with \(h\to j\) obeys (SPC2).

*Proof.* After deleting \(h,j\), at most two direction functions can have more than one essential input. Restriction to any earlier-state fiber cannot create an essential input. Every nonsingleton component therefore has at most two internally branching targets, so the established cross-favorability theorem supplies the hypothesis of (SPC1). \(\square\)

This strengthens the earlier descendant condition: the mixed derivative in (SPC2) uses a bit on a surviving directed cycle. The argument retains separate seams for the two witnesses and makes no prescription on the cyclic bits. Obtaining compatible cross roots across different omitted direction pairs remains necessary for a general closure proof.

An independent subset-reachability calculation tested 300 unrelated coloring pairs on six dimensions with component order \(2,1,2,1\), allowing arbitrary dependencies from earlier to later blocks. All 1200 assignments of the interstitial and terminal singleton bits had at least four cross roots, as predicted by the two square-component factors. The theorem follows from the component induction above.


## Switch-component intersection lemma

Let \(f:Q_m\to\mathbb F_2\) be antipodally odd. Let \(\Gamma_f\) be the subgraph of cube edges across which \(f\) changes.

**Theorem.** Every other antipodally odd function \(g\) changes on some edge of \(\Gamma_f\) if and only if \(\Gamma_f\) contains a connected component preserved by antipodal complementation.

*Proof.* If a component contains \(z\) and \(\bar z\), every odd \(g\) takes opposite values there. Along a connecting path in that component, \(g\) must change, giving a common switch. Conversely, if no component is antipodally invariant, pair up the components as \(C,\bar C\) and make \(g\) constant zero on one and constant one on its mate. This defines an odd \(g\) with no switches along any edge of \(\Gamma_f\). \(\square\)

If \(z,\bar z\) belong to one component \(C\), every odd \(g\) has at least \(\lambda_C(z,\bar z)\) common-switch edges with \(f\), where \(\lambda_C\) is the minimum edge-cut size between the two vertices. Each path between them must cross a \(g\)-switch edge, and all edges of \(C\) are already \(f\)-switches.


## Synchronized feedback switch closes NORI1

Let \(H\sqcup S\) partition directions of a legal odd cube-edge coloring. Assume the induced influence graph on \(S\) is acyclic, and no hub direction reads another hub's bit. Thus its hub-edge color functions \(b_h(z)\) depend only on \(z\in Q_S\).

**Theorem.** If some edge \(z,z\oplus e_s\) in \(Q_S\) switches every hub color,
\[
\boxed{b_h(z\oplus e_s)=1+b_h(z)\quad(h\in H),}
\]
the full coloring has a monochromatic antipodal geodesic.

*Proof.* Choose a desired bit \(t\). Traverse before direction \(s\) all hubs colored \(t\) at \(z\), and after \(s\) the hubs colored \(1+t\) at \(z\). Their colors at their respective steps are all \(t\), because every hub flips its color across \(s\) and none reads another hub bit. Varying the starting hub bits can realize any hub-bit assignment when step \(s\) is taken. If its edge color can equal \(t\), the entire hub-and-\(s\) block is monochromatic \(t\). Otherwise that edge color is identically \(1+t\) for all hub assignments at \(z\); choose the opposite desired bit and repeat to obtain a monochromatic block of color \(1+t\).

The remaining directions \(T=S\setminus\{s\}\) have acyclic influence graph. For a zero-colored block, traverse the block first and follow it by an all-root favorable full \(T\)-geodesic. For a one-colored block, take an all-root favorable \(T\)-geodesic ending at the selected \(T\)-site, then append the block. Both constructions yield a complete path with word \(0^*1^*\). The odd root-slide lemma makes it monochromatic. \(\square\)

**Corollary.** If every hub except perhaps one reads either an odd Boolean function \(f:Q_S\to\mathbb F_2\) or its complement, and the switch graph of \(f\) has a component containing antipodal vertices, the full coloring is good. Indeed the remaining odd hub function must switch with \(f\) on some edge by the preceding switch-component theorem. On that edge all hub colors switch together, and the theorem applies. This is an all-dimensional closure class with any number of feedback directions.


### Parity limitation of switch-component transport

**Lemma.** Let \(m\) be even and \(f:Q_m\to\mathbb F_2\) be antipodally odd. Then no connected component of its switch graph contains antipodal vertices.

*Proof.* Each edge of the switch graph changes \(f\), so any switch-only path from \(z\) to \(\bar z\) must have odd length, since \(f(\bar z)=1+f(z)\). But every cube path between antipodes has length congruent to \(m\) modulo two, and \(m\) is even. Contradiction. \(\square\)

This also has a constructive dual proof. Let \(p(z)=\sum_{s=1}^m z_s\pmod2\), which is antipodally even for even \(m\). Given any odd \(f\), put \(g=f+p\). Then \(g\) is also odd, while every cube edge changes \(p\), so
\[
\partial_sg(z)=1+\partial_sf(z).
\]
Consequently no edge changes both \(f\) and \(g\). Thus the switch-component criterion can enforce a common switch only in odd dimension.

Dependence on all input bits does not replace the missing parity condition. For instance, in dimension five take \(f(x)=x_1+p(x_2,x_3,x_4,x_5)\), where \(p\) indicates the antipodal pair \(0000,1111\) in its four-bit input. The function \(f\) is odd and depends on every input bit, yet its switch-edge components occur in disjoint antipodal pairs. Therefore the robust closing property is antipodal connectivity of the switch graph, not merely full bit sensitivity.

## Global switch-packing rigidity and antipodal component duality

Fix \(m\ge2\). For an antipodally odd Boolean function \(f:Q_m\to\mathbb F_2\), let \(E(f)\) contain those cube edges across which \(f\) changes.

**Lemma (odd switch isoperimetry).** For \(\phi=(-1)^f\), with normalized Walsh coefficients \(\widehat\phi(T)\),
\[
\boxed{|E(f)|=2^{m-1}\sum_{|T|\ {\rm odd}}|T|\widehat\phi(T)^2\ge2^{m-1}.}
\tag{SP1}
\]
Equality holds precisely for a signed one-bit reader \(f(x)=a+x_j\).

*Proof.* Sum the switching probabilities across all \(m\) bit directions, each having \(2^{m-1}\) undirected cube edges. Parseval and the absence of even Walsh levels give the lower bound. Equality forces Fourier support solely at singleton sets. If \(\phi=\sum_j a_j\chi_j\) is Boolean, comparing the degree-two coefficients of \(\phi^2=1\) gives \(a_ja_l=0\) for all \(j\ne l\); Parseval leaves just one coefficient of magnitude one. \(\square\)

For odd functions \(f_1,\ldots,f_k\), put \(r_e=|\{i:e\in E(f_i)\}|\), \(R=\sum_e(r_e-1)_+\), and \(U=|\{e:r_e=0\}|\). Let
\(\Delta_i=\sum_{|T|\ge3}(|T|-1)\widehat\phi_i(T)^2\), where \(\phi_i=(-1)^{f_i}\).

**Theorem (switch-incidence budget).**
\[
\boxed{R-U=2^{m-1}\left(k-m+\sum_{i=1}^k\Delta_i\right).}
\tag{SP2}
\]
On every full antipodal geodesic \(P\), if the \(i\)-th odd function switches \(1+2a_i(P)\) times, and \(R(P),U(P)\) denote repeated-switch and no-switch edge counts along \(P\), then
\[
\boxed{R(P)-U(P)=k-m+2\sum_i a_i(P).}
\tag{SP3}
\]
*Proof.* Count all switch incidences first by odd functions, then by cube edges. Each function contributes \(2^{m-1}(1+\Delta_i)\) from (SP1), while the edge sum is \(|E(Q_m)|-U+R=m2^{m-1}-U+R\). The same count on a full path proves (SP3), because every odd function switches an odd positive number of times between antipodal endpoints. \(\square\)

**Theorem (near-capacity rigidity).** Suppose the switch sets \(E(f_i)\) are pairwise disjoint, and \(k\ge m-1\). Then \(k\le m\), and all \(f_i\) are signed one-bit readers with *different* reader bits. If \(k=m-1\), the family extends to size \(m\) by adjoining the unique unused bit reader, with either sign.

*Proof.* On a full antipodal path, the disjoint switch sets each require one edge, forcing \(k\le m\). For \(k\ge m-1\), if any \(f_i\) switched three times on a full path, the other \(k-1\) functions would require at least \(k+2>m\) distinct edges, impossible. Thus each \(f_i\) switches once along **every** full antipodal path. Under the uniform distribution on rooted full geodesics, every cube edge occurs with probability \(2^{-(m-1)}\); hence \(|E(f_i)|=2^{m-1}\). The isoperimetric lemma makes each a signed reader. Their switch sets are disjoint only when their reader bits differ. \(\square\)

**Corollary (gap for maximal disjoint switch families).** A family maximal under adding further odd functions has either at most \(m-2\) members or \(m\) members: there is no maximal family of size \(m-1\). This gap is sharp for \(m\ge3\). Take the odd triple-parity function \(f_1=x_1+x_2+x_3\) and the independent one-bit readers \(f_2=x_4,\ldots,f_{m-2}=x_m\). Their switch supports partition all cube edges, so no further odd function can avoid their union.

**Theorem (common-switch avoidance dichotomy).** For any family of odd functions, let \(\Gamma\) retain every cube edge belonging to at least one \(E(f_i)\), keeping isolated vertices. There exists another odd function \(g\) with no switches in \(\Gamma\) if and only if \(\Gamma\) has no antipodally invariant connected component. If the components of \(\Gamma\) form \(p\) pairs under antipodal inversion, precisely \(2^p\) such functions \(g\) exist.

*Proof.* Avoiding every retained edge means \(g\) is constant on every connected component of \(\Gamma\). Oddness requires its constant values on antipodal components to be opposite. This is possible precisely when no component contains an antipodal vertex pair, leaving one binary choice per pair. \(\square\)

These theorems apply to arbitrary dimensions and arbitrary numbers of odd switch functions, without a finite-case search. The budget makes nonlinear dependence consume additional switch capacity, while the component theorem identifies when any further independent odd switch channel is impossible. A NORI1 closing step would have to turn unavoidable common-switch edges into dimension-simple path exchanges; no such general exchange is yet established.

## Full antipodal switch-geodesics at deficiency two

Let \(m\ge3\), and take \(k=m-2\) antipodally odd Boolean functions \(f_1,\ldots,f_k:Q_m\to\mathbb F_2\), with pairwise disjoint edge-switch sets. Let \(\Gamma\) be the union of their switch-edge graphs.

**Theorem (dimension-simple saturation dichotomy).** The following are equivalent: (a) at least one \(f_i\) is not a signed one-bit reader; (b) \(\Gamma\) contains a full antipodal geodesic of length \(m\); (c) \(\Gamma\) contains a connected component preserved by antipodal inversion; (d) no further odd Boolean function can be added while preserving pairwise disjointness of switch sets. If all functions are readers, their reader bits are different, and the family instead extends to the full set of \(m\) bit readers.

*Proof.* If all functions are signed readers, the disjointness assumption makes their reader bits distinct. Two bit directions remain absent from the union switch graph. Every component therefore fixes those two bits and is disjoint from its antipodal image; the missing bit readers can be adjoined.

If some \(f_i\) is nonlinear, odd-switch isoperimetry gives \(|E(f_i)|>2^{m-1}\). A uniformly random rooted antipodal full geodesic contains each edge with probability \(2^{-(m-1)}\); hence the expected number of \(f_i\)-switches exceeds one. Every antipodal path has an odd number of \(f_i\)-switches, so some full antipodal geodesic \(P\) has at least three such switches. All other \(k-1=m-3\) odd functions switch on \(P\) at least once. Their switch sets are pairwise disjoint. Therefore at least \(3+(m-3)=m\) different edges of this length-\(m\) geodesic lie in \(\Gamma\). All its edges must lie in \(\Gamma\), with three switches of one function and one of every other function. This proves (b), implying (c). A switch-union component containing antipodes forbids any further odd function with disjoint switch support by the previously proved antipodal component duality, proving (d). All implications and the reader alternative follow. \(\square\)

For normalized Walsh spin coefficients \(\widehat\phi_i(T)\), \(\phi_i=(-1)^{f_i}\), write
\[
\Delta_i=\sum_{\substack{|T|\ge3\\|T|\ {\rm odd}}}(|T|-1)\widehat\phi_i(T)^2.
\]

**Theorem (saturation frequency identity).** For a uniformly chosen rooted full antipodal geodesic \(P\),
\[
\boxed{\Pr[E(P)\subseteq E(\Gamma)]=\frac12\sum_{i=1}^{m-2}\Delta_i.}
\tag{SG1}
\]

*Proof.* Every odd function switches an odd positive number of times on \(P\), and disjointness limits the total to \(m\). With \(m-2\) functions, either all switch once and two path edges have no switch, or one function switches three times, the others once, and every path edge belongs to the union. Thus the switch-incidence excess above \(m-2\) equals two times the indicator of full path saturation. The expected number of switches of function \(i\) is \(|E(f_i)|/2^{m-1}=1+\Delta_i\). Taking expectations proves (SG1). \(\square\)

**Sharp examples.** Odd parity in three bit directions, together with individual readers of every remaining bit, forms a maximal disjoint family of \(m-2\) functions with saturation probability one. Replacing the triple-parity function by odd majority on those three bits gives probability \(1/4\), since its Walsh weight at degree three is \(1/4\).

This is a global passage from switch-graph connectivity to a *dimension-simple full antipodal geodesic*, retaining the requirement that no dimension repeat. It makes no assumption that the auxiliary odd functions are original cube-edge colors: a further structural exchange theorem is needed to turn their switch path into a monochromatic NORI1 path.


## Global influence-congestion law for unrestricted NORI1 colorings

Let \(c\) be any legal antipodally odd binary coloring of the undirected edges of \(Q_n\), \(n\ge2\). Extend each direction-\(i\) edge-color function to a Boolean vertex function
\[
f_i(x)=c(\{x,x\oplus e_i\}),
\]
which is independent of \(x_i\) and antipodally odd on \(Q_n\). For a vertex-cube edge \(e=\{x,x\oplus e_j\}\), let
\[
\boxed{r(e)=|\{i\ne j:f_i(x)\ne f_i(x\oplus e_j)\}|.}
\tag{IC1}
\]
This counts how many other direction-edge colors change when the vertex bit \(j\) is toggled. Call an edge *silent* if \(r(e)=0\), and count its excess simultaneous switch incidences by \((r(e)-1)_+\). Write
\[
U(c)=|\{e:r(e)=0\}|,\qquad
R(c)=\sum_{e\in E(Q_n)}(r(e)-1)_+.
\]

**Theorem (unrestricted influence-congestion identity).** With normalized Walsh coefficients of \(\phi_i=(-1)^{f_i}\),
\[
\boxed{
R(c)-U(c)=2^{n-1}
\sum_{i=1}^n
\sum_{\substack{T\subseteq[n]\setminus\{i\}\\|T|\ge3,\ |T|\ {\rm odd}}}
(|T|-1)\widehat\phi_i(T)^2
\ge0.
}
\tag{IC2}
\]
Equality holds precisely when **all** direction-edge functions are signed one-bit readers, \(c_i(x)=a_i+x_{p(i)}\). If any direction function is nonlinear, then \(R(c)>U(c)\).

*Proof.* Apply the global switch-incidence budget (SP2) to the family \(f_1,\ldots,f_n\) on \(Q_n\), with the number of odd functions equal to the dimension \(k=m=n\). Their cube-edge switch multiplicity is (IC1), because \(f_j\) does not read bit \(j\). The budget gives (IC2). Every summand is nonnegative. Vanishing forces every \(\phi_i\) to have Walsh support only on singleton sets, and Booleanity forces a single signed singleton character. \(\square\)

**Theorem (pathwise influence curvature).** On every full antipodal geodesic \(P\), let \(U(P)\) count silent edges and \(R(P)\) the excess simultaneous switch incidences. Then
\[
\boxed{
R(P)-U(P)=2\sum_{i=1}^n a_i(P)\ge0,
}
\tag{IC3}
\]
where the number of changes of \(f_i\) along \(P\) is \(1+2a_i(P)\). In particular, the surplus is even on every path, and a direction-edge color function changing three or more times forces at least two more excess switch incidences than silent edges on that path.

*Proof.* Each \(f_i\) is odd at the antipodal endpoints, so it changes an odd positive number of times along \(P\). Specialize the pathwise switch budget (SP3) to \(k=m=n\). \(\square\)

**Corollary (all-dimensional no-congestion closure).** If no cube edge changes the colors of two different direction-edge functions simultaneously, then \(c\) has a monochromatic antipodal full geodesic.

*Proof.* The no-congestion assumption gives \(r(e)\le1\) everywhere, hence \(R(c)=0\). Formula (IC2) forces \(U(c)=0\) and all nonlinear Walsh masses to vanish. Therefore each direction-edge function is a signed one-bit reader. The all-dimensional functional-reader root theorem already proved in Article XIV then produces a monochromatic antipodal geodesic. \(\square\)

**Closure target without hub-count induction.** A bad legal coloring must have strictly more repeated than silent switch incidences, with a nonnegative even surplus on each full antipodal geodesic. Thus the first global missing step can be expressed as a *congestion-to-exchange principle*: exploit an overloaded edge along a minimum-switch Petrie geodesic to perform a dimension-simple square exchange that lowers the number of color changes, or identify an antipodal topological obstruction to doing so. Unlike proving one extra bounded hub case, this target involves every direction simultaneously and makes no fixed-dimensional reduction.

## Canonical saturation of disjoint odd switch channels

Let \(F=\{f_1,\ldots,f_k\}\) be antipodally odd Boolean functions on \(Q_m\) with pairwise disjoint switching-edge sets.

**Lemma (reader peeling).** If \(f_i=a+x_j\), then every other \(f_l\) is independent of bit \(j\); after removing this function and bit, the remaining odd functions have pairwise disjoint switch sets on \(Q_{m-1}\).

*Proof.* A signed reader changes across every edge in direction \(j\), so no other member can change along such an edge. Thus the other members ignore bit \(j\), and their oddness and switch disjointness descend to the remaining cube. \(\square\)

**Theorem (global switch-channel saturation).** Every pairwise-disjoint family can be extended to a maximal such family \(F^*\), through at most \(m-k\) additions. Every maximal family falls into one of two disjoint classes:

1. A complete collection of \(m\) signed bit readers, with all reader bits different.
2. At most \(m-2\) functions, whose switch-union graph has a connected component containing antipodal vertices and whose residual family after reader peeling is nonempty and nonlinear.

*Proof.* Every odd function switches on each full antipodal geodesic at least once, so disjointness bounds the family size by \(m\). Whenever the union switch graph has no antipodally invariant component, the earlier switch-component duality constructs another odd function avoiding all retained switch edges; adjoin it. The procedure terminates within \(m-k\) steps. At termination the union graph has a component containing antipodal vertices. The near-capacity rigidity theorem forces an \(m\)-member family to be the full signed reader basis and excludes a maximal \((m-1)\)-member family. Every smaller maximal family therefore has at most \(m-2\) members. It cannot consist entirely of readers, since one missing reader could be added. Reader peeling leaves a nonempty nonlinear residual family. \(\square\)

**Corollary (full geodesics at the near-capacity boundary).** When the second alternative has \(m-2\) members, its union switch graph already contains a full dimension-simple antipodal geodesic, by the earlier switch-saturation theorem.

This construction terminates for all dimensions without separate case checks. The two remaining mechanisms are the rigid basis at high switch capacity and antipodal component connectivity at low capacity. Passing from an antipodally connected component at arbitrary switch density to a dimension-simple path, and then to a monochromatic path in the original edge coloring, remains a proof target rather than an established implication.

## Opposed-root cylinders through terminal acyclic blocks

Let \(f,g\) be arbitrary edge colorings of the same \(Q_m\). Let \(A(f)\) denote the roots admitting full antipodal geodesics with edge-color word \(0^*1^*\). Let \(D\) be a common directed influence supergraph: an arrow \(p\to q\) means bit \(p\) may influence the color of a direction-\(q\) edge in either coloring.

**Theorem (acyclic block cylinder).** Partition the dimensions into \(S\sqcup T\), where \(D[S]\) is acyclic and no arrow leads from \(S\) into \(T\). The \(T\)-edge colors are therefore independent of the \(S\)-bits and induce colorings \(f_T,g_T\). Then
\[
\boxed{
Q_S\times \bigl(A(f_T)\cap\overline{A(g_T)}\bigr)
\subseteq A(f)\cap\overline{A(g)}.
}
\tag{RC1}
\]

*Proof.* Choose \(z\in A(f_T)\cap\overline{A(g_T)}\). Select favorable complete \(T\)-geodesics in \(f_T,g_T\), rooted respectively at \(z,\bar z\). Let \(v,w\) be their possibly different zero-to-one seam vertices. Fix any \(u\in Q_S\). The \(S\)-fiber colorings of \(f\) at \(T\)-state \(v\) and of \(g\) at \(T\)-state \(w\) have acyclic influence graphs, because all their influence arrows belong to \(D[S]\). By the previously established acyclic all-root theorem, each has a favorable full \(S\)-geodesic rooted at \(u\) and \(\bar u\), respectively. Insert these \(S\)-geodesics at the corresponding \(T\)-seams. Every \(T\)-edge color is independent of the \(S\)-bits, so both original \(T\)-words are unchanged. Inserting \(0^*1^*\) at a zero-to-one seam preserves nondecreasing color words. The resulting complete paths use each direction once and are rooted at the antipodal vertices \((u,z),(\bar u,\bar z)\). Since \(u\) was arbitrary and \(z\) was fixed, the claimed whole cylinder belongs to the opposed favorable-root set. \(\square\)

**Corollary (multiplicity).** If the common influence digraph on \(T\) has at most two vertices with internal indegree greater than one in each SCC, then
\[
\bigl|A(f)\cap\overline{A(g)}\bigr|
\ge 2^{|S|}
\prod_{B\in\operatorname{SCC}(D[T])}\lambda(B),
\tag{RC2}
\]
where the component factors \(\lambda(B)>0\) are those of the published quantitative cross-coloring condensation theorem. Each opposed favorable \(T\)-root supplies a full parallel \(S\)-subcube of favorable roots.

This result extends the previously published prescribed constant-leaf lemma: direction colors within \(S\) may depend nonlinearly on \(T\) and may have arbitrary acyclic internal dependencies. It is an unrestricted-dimensional transport theorem, not a fixed-order calculation.

## Flat subcubes in square derivatives of hypothetical four-hub obstructions

Let \(c\) be a legal antipodally odd coloring of the undirected edges of \(Q_n\). Call a direction *simple* if its color is a signed one-bit reader \(c_i(x)=a_i+x_{r(i)}\), and otherwise *exceptional*. Fix distinct directions \(h,j\), both exceptional, and assume that there are at most four exceptional directions overall.

Set \(D'=D(c)-\{h,j\}\). Choose any partition of the remaining dimensions into \(S\sqcup T\) such that \(D'[S]\) is acyclic and no influence arrow goes from \(S\) into \(T\). Define the square derivative of the direction-\(j\) edge-color function by
\[
\partial_h c_j(u,z)=c_j(h=0,u,z)+c_j(h=1,u,z)\pmod2,
\]
where \(u\in Q_S,z\in Q_T\).

**Theorem (flat square-derivative cylinders).** If \(c\) is a NORI1 counterexample, then there exists a set \(K\subseteq Q_T\) with
\[
\boxed{|K|\ge\prod_{B\in\operatorname{SCC}(D'[T])}\lambda(B)>0}
\tag{FC1}
\]
such that
\[
\boxed{\partial_h c_j(u,z)=0\quad\text{for every }u\in Q_S,\ z\in K.}
\tag{FC2}
\]
Thus the zero set of the derivative contains at least \(|K|\) disjoint parallel full \(S\)-subcubes. Here the factors \(\lambda(B)\) are those in the previously proved quantitative two-hub opposed-root theorem; the corresponding estimate relies on its published computer-assisted component bound.

*Proof.* Restrict the coloring first to \(h=0\), then split its directions by \(j=0,1\), obtaining arbitrary horizontal colorings \(f_{00},f_{01}\) on \(Q_{S\cup T}\). Their common influence supergraph is \(D'\). On the induced \(T\)-direction colorings, at most two original exceptional direction functions remain; all others are constants or signed readers after restriction. Hence each SCC of \(D'[T]\) has at most two vertices with internal indegree greater than one. The quantitative cross-coloring theorem produces
\[
K=A((f_{01})_T)\cap\overline{A((f_{00})_T)}
\]
of cardinality at least the product in (FC1). The acyclic-block cylinder theorem (RC1) gives
\[
Q_S\times K\ \subseteq\
A(f_{01})\cap\overline{A(f_{00})}=L_{h,j}.
\]
The previously proved cross-witness square-flatness theorem states that badness of \(c\) forces \(\partial_hc_j\) to vanish at all \(L_{h,j}\). This proves (FC2). \(\square\)

**Corollary (uniform higher-derivative exclusion).** Under the same hypotheses, if for some nonempty \(R\subseteq S\) the iterated Boolean derivative \(\partial_R\partial_h c_j\) is identically one, then \(c\) has a monochromatic full antipodal geodesic. Indeed, if \(c\) were bad, (FC2) would force every derivative in nonempty directions \(R\subseteq S\) to vanish throughout each full \(S\)-subcube in its zero set, contrary to the stipulated uniform value.

**Corollary (acyclic external control).** Suppose additionally that \(\partial_hc_j\) depends only on the bits of \(S\). If it is nonzero at any input, then \(c\) is good: the cylinder (FC2) ranges over all \(u\in Q_S\), so under badness the derivative would be identically zero.

The theorem generalizes the earlier leaf-supported derivative exclusion to all terminal acyclic blocks, with arbitrary nonlinear dependence on other directions. It imposes all-dimensional flatness conditions on the overlap of cross-facet favorable paths, but it does not close unrestricted NORI1 or all four-hub configurations.



## Maximal influence congestion and unbounded exchange plateaus

For every even \(n=2m\ge6\), color direction-\(i\) cube edges by
\[
c_i(x)=\sum_{j\ne i}x_j\pmod 2. \tag{EP1}
\]
This coloring is well-defined because \(c_i\) ignores \(x_i\), and it is antipodally odd because \(n-1\) is odd. By an *adjacent-direction exchange* we mean swapping successive dimensions of a rooted full antipodal geodesic while preserving its root. A *Petrie rotation* shifts the starting point along the cycle consisting of a geodesic followed by its antipodal image.

**Theorem (maximal-congestion strict-descent obstruction).** In (EP1), every cube edge has influence multiplicity \(r(e)=n-1\). There is a rooted full antipodal geodesic \(P\) with color word
\[
\boxed{w(P)=0\,1^{n-2}\,0.}\tag{EP2}
\]
No adjacent-direction exchange or Petrie rotation strictly reduces its two color changes. Nevertheless a monochromatic full antipodal geodesic exists from the same root, and the minimum number of adjacent-direction exchanges between \(P\) and such a geodesic is \(m-1\).

*Proof.* Flipping bit \(j\) changes every function \(c_i\) with \(i\ne j\). Hence all cube edges have \(r(e)=n-1\); in the influence-congestion notation, \(U=0\) and \(R=n(n-2)2^{n-1}\).

Fix a dimension order \(\pi_0,\ldots,\pi_{n-1}\), indexed from zero, and root \(x\). Define \(T=\sum_i x_i\) and \(b_k=T+x_{\pi_k}\) in \(\mathbb F_2\). The color of step \(k\) is
\[
w_k=b_k+k\pmod2. \tag{EP3}
\]
Conversely every word \(w\) is obtained by putting \(b_k=w_k+k\), \(T=\sum_kb_k\), and \(x_{\pi_k}=b_k+T\): as \(n\) is even, \(\sum_i x_i=T\). Thus a root giving (EP2) exists.

An adjacent exchange at positions \(k,k+1\) replaces the two color bits by
\[
\boxed{(w_k,w_{k+1})\longmapsto(1-w_{k+1},1-w_k).}\tag{EP4}
\]
Pairs \(01,10\) remain unchanged; \(11\) becomes \(00\) and \(00\) becomes \(11\). In (EP2) the only equal adjacent pair is \(11\), within a central block of at least four ones. Replacing any such pair by \(00\) leaves at least two changes, while each boundary exchange preserves the word. Hence no adjacent exchange improves \(P\).

The antipodal Petrie cycle has color word \(w\bar w\). Its length-\(n\) window starting after \(1\le k<n\) steps reads \(w_k\cdots w_{n-1}\bar w_0\cdots\bar w_{k-1}\). Because \(w_0=w_{n-1}=0\), it has \(3-\mathbf1_{\{w_{k-1}\ne w_k\}}\), hence two or three, switches. The windows beginning at offsets \(0,n\) also have two. Thus no Petrie rotation improves \(P\).

Under adjacent exchanges, the binary entries \(b_k\), each attached to its direction, merely undergo adjacent transpositions. In (EP2) the one-positions of \(b\) are \(2,4,\ldots,2m-2,2m-1\). A constant-zero word requires one-positions \(1,3,\ldots,2m-1\); a constant-one word requires \(0,2,\ldots,2m-2\). For binary strings containing equally many ones, the minimum adjacent-transposition distance equals the sum of absolute differences between corresponding ordered one-positions. These distances are \(m-1\) and \(2m-1\), respectively. Repeatedly exchanging the first pair of ones remaining in the central block of (EP2) attains the former bound: the two-switch word remains two-switch until the final exchange makes it constant zero. \(\square\)

Consequently maximum simultaneous switching of direction-color functions does not imply an immediately improving square exchange, even allowing Petrie rotations. An exchange-based NORI1 proof must accommodate nondecreasing steps or use a global invariant detecting improving sequences whose length grows with dimension.


## Parity completion and the sizes of maximal disjoint odd switch families

Let \(m\ge1\), and let \(f_1,\ldots,f_k:Q_m\to\mathbb F_2\) be antipodally odd Boolean functions with pairwise disjoint switch sets \(E(f_i)\). Constants differing by one give the same switch set. Write
\[
p(x)=\sum_{j=1}^m x_j,\qquad
h(x)=p(x)+\sum_{i=1}^k f_i(x).
\tag{PC1}
\]
All sums of Boolean functions in this subsection are in \(\mathbb F_2\).

**Theorem (completion by the unused edges).** The residual function \(h\) satisfies
\[
\boxed{
E(h)=E(Q_m)\setminus\bigcup_{i=1}^kE(f_i),\qquad
h(\bar x)+h(x)=m+k\pmod2.
}
\tag{PC2}
\]
In particular, whenever \(m-k\) is odd, \(h\) is an odd function that can be adjoined to the family. The enlarged switch sets partition all cube edges, so the enlarged family is maximal under adjoining further odd functions.

*Proof.* Across a cube edge, \(p\) changes once. At most one retained function changes, by disjointness. Consequently \(h\) changes precisely when none of the retained functions changes. This proves the switch-set formula. Complementing all bits changes \(p\) by \(m\) and each \(f_i\) by one, proving the antipodal formula. If \(m-k\) is odd, this makes \(h\) odd; its switch set is disjoint from every retained set and fills their complement. An odd function is nonconstant and has a nonempty switch set. Thus an additional odd function cannot have switch set disjoint from this edge partition. \(\square\)

**Corollary (complete classification of maximal family sizes).** For \(m\ge1\), the possible cardinalities \(k\) of maximal pairwise-disjoint odd switch families on \(Q_m\) are precisely
\[
\boxed{1\le k\le m,\qquad k\equiv m\pmod2.}
\tag{PC3}
\]

*Proof.* Every odd function changes an odd positive number of times on each full antipodal geodesic. Disjointness therefore gives \(k\le m\). An empty family is extendible by a bit reader. If \(m-k\) were odd, the completion theorem would extend the family, contradicting maximality.

Conversely, fix a positive \(k\le m\) of the same parity as \(m\). Partition the dimensions into \(k\) nonempty odd-sized blocks: one block of size \(m-k+1\) and \(k-1\) singleton blocks suffice. For each block \(B\), take \(f_B(x)=\sum_{j\in B}x_j\). Each function is odd, and its switch set consists of all edges in the dimensions of \(B\). These sets partition \(E(Q_m)\), proving maximality. \(\square\)

Thus the previously proved exclusion of maximal families of size \(m-1\) extends to every odd deficiency. Every positive even deficiency is attained. The examples can include a function that is not a signed one-bit reader: parity on an odd-sized block of size at least three has this property.

**Proposition (residual level-set criterion at even deficiency).** Suppose \(m-k\) is even, and let \(\Gamma\) be the graph formed by the union of the retained switch sets. Then \(h\) is antipodally even and
\[
\boxed{\Gamma=Q_m[h^{-1}(0)]\ \sqcup\ Q_m[h^{-1}(1)].}
\tag{PC4}
\]
The family is maximal if and only if at least one of these two induced graphs has a connected component preserved by antipodal complementation.

*Proof.* Formula (PC2) makes \(h\) even and says that a cube edge belongs to \(\Gamma\) precisely when its endpoints have the same \(h\)-value, proving (PC4). A further odd function can be adjoined precisely when it is constant on every connected component of \(\Gamma\). If some component contains \(x,\bar x\), such constancy contradicts oddness. If no component is antipodally invariant, pair each component with its distinct antipodal mate and assign the values zero and one to the two members of every pair. The resulting function is odd and has no switch edge in \(\Gamma\), so it extends the family. \(\square\)

**Scope for the feedback argument.** The residual \(h\) is an auxiliary Boolean function. It need not be one of the direction-edge color functions, and adjoining it does not recolor a NORI1 instance or preserve an assigned direction for the new function. The theorem completes the switch-channel saturation analysis: odd deficiency is settled by an explicit formula, while even deficiency is governed by antipodal components inside an even Boolean level set. Converting that component information into a monochromatic direction-simple path in the original coloring remains an additional requirement.

An independent enumeration of all switch sets of odd Boolean functions in dimensions one through four found maximal family sizes respectively \(\{1\},\{2\},\{1,3\},\{2,4\}\). It also checked (PC2) for every disjoint family of odd deficiency in those dimensions. These calculations verify the formulas on finite instances; the proofs above apply in every dimension.


## Facet-imbalance extremality and weighted-majority closure

Let \(n\ge2\), let \(c\) be any legal antipodally odd coloring of \(E(Q_n)\), and write \(\sigma_i(x)=(-1)^{c_i(x)}\). Define the signed color imbalance of the facet \(x_j=0\) by
\[
B_j=\sum_{i\ne j}\ \sum_{\substack{x_i=0\\x_j=0}}\sigma_i(x),\qquad
\mathcal E(c)=\sum_{j=1}^n B_j^2.
\tag{FE1}
\]
The opposite facet has imbalance \(-B_j\). Index antipodal edge pairs by \(p\). For a representative direction-\(i\) edge with sign \(s_p\), choose an incident vertex \(x\) and set \(v_{p,i}=0\), \(v_{p,j}=(-1)^{x_j}\) for \(j\ne i\). Then \(B=\sum_p s_pv_p\), and
\[
\boxed{\mathcal E(c^{[p]})-\mathcal E(c)
=4\left((n-1)-s_p\langle B,v_p\rangle\right).}
\tag{FE2}
\]

**Lemma (weighted-majority path).** Let \(a_1,\ldots,a_n\ge0\), with at least two positive weights, and assume \(\sum_{j\ne i}a_j(-1)^{x_j}\ne0\) for every direction \(i\) and vertex \(x\). The direction-\(i\) edge-sign coloring
\[
\sigma_i(x)=\operatorname{sgn}\sum_{j\ne i}a_j(-1)^{x_j}
\tag{FE3}
\]
has a monochromatic full antipodal geodesic.

*Proof.* Partition the positive weights into \(P,N\) minimizing \(D=|a(P)-a(N)|\), with \(a(P)\ge a(N)\). Transferring an \(i\in P\) to \(N\) would reduce the discrepancy if \(a_i<D\). Equality \(a_i=D\) would give a zero sum in (FE3), by choosing positive signs on \(N\) and negative signs on \(P\setminus\{i\}\). Hence \(a_i>D\) for every \(i\in P\). If zero-weight dimensions exist, then \(D>0\), since otherwise their field can vanish.

Choose a root with bit-sign \(+1\) on \(P\) and \(-1\) on \(N\), and traverse the \(N\) dimensions first, the zero-weight dimensions next, and the \(P\) dimensions last, in arbitrary order within each group. At an \(N\)-step the field excluding its negative current weight is at least \(D+a_i>0\). At a zero-weight step the field is \(a(P)+a(N)>0\). At a \(P\)-step the field is at least \(a_i-D>0\), the lower bound occurring if \(i\) is last in \(P\). All edges have sign \(+1\). \(\square\)

**Theorem (all facet-energy local maxima are good).** If no legal single-antipodal-edge-pair flip raises \(\mathcal E(c)\), then \(c\) has a monochromatic full antipodal geodesic.

*Proof.* Formula (FE2) gives \(s_p\langle B,v_p\rangle\ge n-1>0\) on every edge pair. Thus every direction-\(i\) edge sign equals the sign of the nonvanishing field \(\sum_{j\ne i}B_j(-1)^{x_j}\). At least two \(B_j\) are nonzero. Changing the initial-bit conventions to absorb the signs of \(B_j\) transforms the field to (FE3) with \(a_j=|B_j|\). Apply the lemma. \(\square\)

**Corollary (extremal counterexample and critical repairs).** If NORI1 fails in dimension \(n\), choose a bad legal coloring maximizing \(\mathcal E\) among all bad legal colorings. It has at least one \(\mathcal E\)-increasing antipodal edge-pair flip; every increasing flip heals the coloring. Every monochromatic full geodesic in any repaired coloring passes through the flipped pair strictly internally, by the critical-restoration theorem proved earlier in this Subsection.

This reduces a possible energy-extremal closure proof to reconciling the repaired internal pivots with the positive energy gradient. The result has no bounded-hub or affine hypothesis, but does not yet transfer the monochromatic repaired path back to the bad coloring.


**Corollary (uniform energy gain at frustrated pairs).** With the notation (FE1)--(FE2), call an antipodal edge pair \(p\) *frustrated* when \(h_p=s_p\langle B,v_p\rangle\le0\). Every bad legal coloring has at least one frustrated pair, and flipping any frustrated pair increases the facet energy by at least \(4(n-1)\):
\[
\boxed{h_p\le0\implies \mathcal E(c^{[p]})-\mathcal E(c)\ge4(n-1).}
\tag{FE4}
\]
In a bad coloring maximizing \(\mathcal E\) among bad colorings, **all** frustrated pairs are healing; every monochromatic antipodal geodesic after any such repair traverses that pair strictly internally.

*Proof.* If there were no frustrated pairs, then \(h_p>0\) everywhere, so every edge sign agrees with the nonzero field \(\sum_{j\ne i}B_j(-1)^{x_j}\). The weighted-majority lemma supplies a monochromatic geodesic. The gain follows from (FE2). Maximality over bad colorings makes every improving flip healing, and the internal-pivot theorem applies. \(\square\)

This identifies the distinguished repairs using only facet imbalances and edge colors, and quantifies their gain independently of dimension-specific classification. Repeatedly flipping any frustrated pair strictly raises \(\mathcal E\); the process terminates at a weighted-majority coloring with a monochromatic full geodesic. Pulling a witness back through the flips remains the closure problem.




### Weak threshold agreement and positive spanning in every obstruction

The weighted-majority argument extends to arbitrary tie colors. This removes the nonvanishing-field assumption and gives a necessary geometric condition on every unrestricted bad coloring.

For \(a\in\mathbb R^n\), define the field of a direction-\(i\) edge by
\[
H_a(x,i)=\sum_{j\ne i}a_j(-1)^{x_j}.
\tag{WT1}
\]
It is independent of the chosen endpoint and changes sign under antipodal complementation.

**Theorem (weak threshold closure, including all ties).** Let \(n\ge2\), and let \(c\) be any antipodally odd edge coloring. If there is a nonzero vector \(a\) such that
\[
\boxed{(-1)^{c_i(x)}H_a(x,i)\ge0
\quad\text{on every edge},}
\tag{WT2}
\]
then \(c\) has a monochromatic full antipodal geodesic. The colors on all zero-field edges are arbitrary, subject only to antipodal oddness.

*Proof.* Choose a root \(x\) with \((-1)^{x_j}a_j=|a_j|\), assigning the zero-weight bits arbitrarily. Traverse all zero-weight directions first, followed by the positive-weight directions in any order. During the first block every field is \(\sum_j|a_j|>0\), so every edge has color zero.

Write the positive weights in their chosen order as \(b_1,\ldots,b_r\). At the \(t\)-th step of this second block the field is
\[
M_t=\sum_{k>t}b_k-\sum_{k<t}b_k.
\]
For \(1\le t<r\), \(M_t-M_{t+1}=b_t+b_{t+1}>0\). Thus these fields strictly decrease, with at most one zero. By (WT2), the corresponding color word consists of zeros, at most one arbitrary tie bit, and then ones. It has the form \(0^*1^*\). This also covers \(r=1\), when the single positive-weight step has zero field. The full path uses every direction once. The established antipodal root-slide surgery turns it into a monochromatic full antipodal geodesic. \(\square\)

This proof also strengthens Article XIV's type-B threshold theorem. Genericity of the weight vector is unnecessary. The order restriction placing zero-weight directions first matters: it prevents a block of independently colored zero-field observations.

Choose one representative \(e_p\) of each antipodal edge pair, with direction \(i\), sign \(s_p=(-1)^{c(e_p)}\), and vector \(v_p\) as in (FE1): its \(i\)-th entry is zero and its other entries are \((-1)^{x_j}\). Put \(w_p=s_pv_p\). Replacing \(e_p\) by its antipode changes both \(s_p\) and \(v_p\) by a minus sign, so \(w_p\) is intrinsic to the pair.

**Corollary (positive spanning is necessary for badness).** Every bad legal coloring satisfies
\[
\boxed{0\in\operatorname{int}\operatorname{conv}\{w_p:p\text{ an antipodal edge pair}\}.}
\tag{WT3}
\]
Equivalently, for every nonzero \(a\in\mathbb R^n\), there are pairs \(p,q\) with
\[
\langle a,w_p\rangle<0<\langle a,w_q\rangle.
\tag{WT4}
\]

*Proof.* If zero is not in the interior of this finite convex hull, finite-dimensional separation provides a nonzero \(a\) with \(\langle a,w_p\rangle\ge0\) for every \(p\), after reversing \(a\) if necessary. This is (WT2), contradicting badness. Conversely, failure of either strict inequality in (WT4) gives such a separator, and the usual supporting-hyperplane criterion makes (WT3) and (WT4) equivalent. \(\square\)

**Corollary (strictly frustrated repairs, with the zero-energy case separated).** Let \(n\ge3\), and choose a bad coloring maximizing \(\mathcal E=\sum_jB_j^2\) among bad colorings. If \(B\ne0\), some pair satisfies
\[
h_p=s_p\langle B,v_p\rangle<0.
\]
Every such pair is healing, and
\[
\boxed{\mathcal E(c^{[p]})-\mathcal E(c)\ge4(n+1).}
\tag{WT5}
\]
If instead \(B=0\), every single-pair flip is healing, and every facet has no empty roots: its two disjoint orientation-root sets partition its vertex set.

*Proof.* For \(B\ne0\), apply (WT4) with \(a=B\). Each facet contains \((n-1)2^{n-2}\) edges, an even number, so each \(B_j\), and hence each \(h_p\), is even. Strict negativity gives \(h_p\le-2\). Formula (FE2) proves (WT5), and maximality over bad colorings makes the flip healing.

For \(B=0\), (FE2) gives energy gain \(4(n-1)>0\) at every pair. Thus every flip heals. In any direction, an empty bridge-root pair would permit a nonhealing flip by the restoration-fan theorem. There are therefore no empty roots in any facet. Paired roots are already excluded by badness, giving the asserted partition. \(\square\)

The positive-spanning condition is necessary, not sufficient, for a bad coloring. It does not establish that an energy-extremal obstruction has a separating vector. The remaining task is to use the original path witnesses attached to the forced healing pairs to contradict (WT3), or to obtain an original paired root directly. In particular, the case \(B=0\) cannot be discarded by applying the threshold theorem with the zero vector.

An independent path evaluator checked the constructive weak-threshold proof and the resulting monochromatic root-slide on 1400 colorings in dimensions two through eight, using signed integer weights, zero weights, and independently assigned legal tie colors. The argument above is dimension-uniform and does not depend on these checks.


## Global extremal imbalance and antipodal-path transversal stability

For an arbitrary coloring of cube edges, with no locality or symmetry assumptions, let \(q=2^{n-1}\) and \(M_i\) be the set of all direction-\(i\) edges. Call \(E\) a transversal if it meets every full antipodal geodesic.

**Theorem (sharp minimum).** A transversal has at least \(q\) edges, with equality if and only if \(E=M_i\) for some \(i\).

*Proof.* Given a direction ordering, the \(q\) full geodesics beginning at even-parity roots partition all edges, one from each direction at each root. A fixed direction edge is produced from two possible roots of opposite parity, so appears once. Thus a transversal has size at least \(q\). At equality every full geodesic, for every order and starting root, meets \(E\) once. On an arbitrary square write edge indicators \(a,b,c,d\) so the two routes from its first corner have sums \(a+c,b+d\). Exchanging their first two directions gives \(a+c=b+d\). Starting from an adjacent corner gives \(a+b=c+d\). Thus \(a=d,b=c\), showing that opposite square edges agree. Every direction matching is connected by these square comparisons, so \(E\) is a union of complete direction matchings. Size \(q\) forces a single matching. \(\square\)

**Theorem (quantitative stability).** If \(E\) is a transversal of size \(q+t\), put \(\epsilon=t/q\). Some direction \(i\) satisfies
\[
\boxed{|E\triangle M_i|
\le t\left(1+\frac{n(n-1)}{1+\epsilon}\right)
\le [1+n(n-1)]t.}\tag{BI1}
\]

*Proof.* Let \(r_i(x)\) be the membership indicator of the direction-\(i\) edge at \(x\), and \(p_i=\mathbb E_xr_i(x)\), so \(\sum_i p_i=1+\epsilon\). For uniform starting root and direction order, let \(K\) count the traversed edges in \(E\). As \(E\) is a transversal,
\[
K\ge1,\qquad\mathbb EK=1+\epsilon.
\]
Swapping a random consecutive direction pair \(i,j\) inside its square changes the path count from \(K\) to \(K'\). Both are at least one. Thus \(|K-K'|\le(K-1)+(K'-1)\), and the expectation of the absolute square-route difference \(a+c-b-d\) is at most \(2\epsilon\). Exchanging from the adjacent square corner gives the same bound for \(a+b-c-d\). Since the sum of these two signed differences is \(2(a-d)\), uniformly averaging over square locations and ordered directions yields
\[
\frac1{n(n-1)}\sum_i\sum_{j\ne i}
\Pr_x[r_i(x)\ne r_i(x^j)]\le2\epsilon.
\]
The Boolean-cube Poincare inequality therefore gives
\[
\sum_i p_i(1-p_i)
\le\frac14\sum_i\sum_{j\ne i}
\Pr_x[r_i(x)\ne r_i(x^j)]
\le\tfrac12n(n-1)\epsilon.
\]
Consequently
\[
\max_i p_i
\ge\frac{\sum_i p_i^2}{\sum_i p_i}
\ge1-\frac{n(n-1)\epsilon}{2(1+\epsilon)}.
\]
For such an \(i\), the mismatch count satisfies
\[
|E\triangle M_i|/q
=(1-p_i)+\sum_{j\ne i}p_j
=2+\epsilon-2p_i,
\]
which proves (BI1). \(\square\)

**Theorem (global counterexample imbalance gap).** If a binary edge coloring of \(Q_n\), \(n\ge2\), has no paired root, then
\[
\boxed{
\min(|E_0|,|E_1|)
\ge 2^{n-1}+
\left\lceil\frac{2^{n-2}}{1+n(n-1)}\right\rceil.}
\tag{BI2}
\]

*Proof.* Either color class \(E\) is a transversal, otherwise the opposite color supplies a monochromatic full geodesic and hence a paired root. Write \(|E|=q+t\). By (BI1), a matching \(M_i\) differs from \(E\) in at most \(D=[1+n(n-1)]t\) edges. Color the matching with the color of \(E\), and all other directions oppositely. From any common root this reference coloring has opposite monotone geodesics, one traversing \(i\) first and the other last, with the remaining directions in a fixed order. For uniformly random roots the expected combined encounters of both paths with changed edges is \(2|E\triangle M_i|/q\). If \(D<q/2\), some root supports both reference paths without traversing changed edges, so also supports both in the given coloring. Therefore \(D\ge q/2\); integrality gives (BI2). \(\square\)

**Implication for unrestricted NORI1.** In any antipodally odd coloring of \(Q_{n+1}\) with no monochromatic antipodal geodesic, **every** \(n\)-dimensional facet coloring has no paired root by the established bridge equivalence. Therefore its two color classes satisfy (BI2) on every facet. This supplies a dimension-uniform necessary condition on any putative minimal counterexample. It does not prove closure: a further argument must couple imbalance restrictions on intersecting facets.


## One-facet extremality produces exponentially many critical repairs

Let \(n\ge3\). In any hypothetical bad legal coloring of \(Q_n\), write \(B_j\) for the signed imbalance of the facet \(F_{j,0}=\{x_j=0\}\), as in (FE1), and put
\[
M(c)=\max_{1\le j\le n}|B_j(c)|.
\]

**Theorem (extremal minority-edge saturation).** Suppose NORI1 fails in \(Q_n\). Choose a bad legal coloring \(c\) maximizing \(M(c)\) over all bad colorings, and a facet \(F=F_{j,s}\) having maximum absolute imbalance. Designate its more frequent color by \(b\), choosing either one in a tie. Then for **every** edge \(e\subset F\) of minority color \(1-b\), the legal antipodal-pair flip \(c^{[e]}\) is good. Every color-\(b\) monochromatic full geodesic in \(c^{[e]}\) uses \(e\) strictly internally. Furthermore, the minority edges give at least \(2^{n-2}+1\) distinct healing antipodal edge pairs in this single facet. The sharper quantitative blocker gap previously established in this Subsection raises this to
\[
\boxed{
2^{n-2}+\left\lceil
\frac{2^{n-3}}{1+(n-1)(n-2)}
\right\rceil .
}
\tag{FE5}
\]

*Proof.* Antipodal complementation sends \(F\) to the opposite facet and reverses its edge colors. Flipping the antipodal pair of any minority edge \(e\subset F\) changes that edge in \(F\) from \(1-b\) to \(b\), increasing the absolute imbalance of \(F\) by two (also if the imbalance was zero). Therefore \(M(c^{[e]})\ge M(c)+2\). By maximality of \(c\) among bad colorings, \(c^{[e]}\) is good. The universal internal-pivot theorem applies to each healing pair; a color-\(b\) monochromatic full geodesic in the repaired coloring can only use \(e\) from the changed antipodal pair, so \(e\) occurs internally.

Let \(m=n-1\). The induced coloring of \(F\cong Q_m\) contains no monochromatic full antipodal geodesic: otherwise its two antipodal endpoints would be paired favorable roots, and the bridge selector theorem would already make the original \(c\) good. Thus each of its color classes hits every full antipodal \(m\)-geodesic. The minimum geodesic-blocker theorem gives each class at least \(2^{m-1}\) edges, with equality only for one complete direction class. Equality would give monotone paired roots by putting that direction first or last, again making \(c\) good. Hence each class has at least \(2^{m-1}+1\) edges, and the previously proved quantitative blocker gap (BI2) yields the displayed stronger bound. Distinct edges of \(F\) belong to distinct antipodal edge pairs, since the mates lie in the opposite facet. \(\square\)

**Closure target.** An imbalance-extremal hypothetical counterexample has exponentially many distinct *minority-to-majority healing pairs concentrated in one facet*, each carrying a strictly internal universal monochromatic pivot in its repaired coloring. A closing lemma must use the simultaneous location and routing constraints of these repair witnesses to construct a monochromatic geodesic before any recoloring. This extremality makes no structural assumption on the coloring.



### Extremizing squared facet imbalance in a hypothetical bad coloring

Let \(N\ge3\), let \(c\) be antipodally odd on undirected edges of \(Q_N\), and encode colors as signs \(s(e)\in\{-1,1\}\), with \(s(\bar e)=-s(e)\). Set
\[
B(F)=\sum_{e\subset F}s(e),\qquad
\Phi(c)=\sum_{F\ {\rm facet}}B(F)^2.
\]
For an antipodal edge orbit \([e]\) put
\[
T_e=s(e)\sum_{F\ {\rm facet}:\ e\subset F}B(F).
\]
Antipodal replacement of the representative reverses both signs, leaving \(T_e\) unchanged.

**Theorem (imbalance drift and random baseline).** If \(c^{[e]}\) is obtained by flipping the two edges of \([e]\), then
\[
\boxed{\Phi(c^{[e]})-\Phi(c)=8(N-1-T_e).}\tag{IE1}
\]
Summing over all \(N2^{N-2}\) edge orbits gives
\[
\boxed{\sum_{[e]}[\Phi(c^{[e]})-\Phi(c)]
=4\bigl(N(N-1)2^{N-1}-\Phi(c)\bigr).}\tag{IE2}
\]
The quantity \(N(N-1)2^{N-1}\) is also the expectation of \(\Phi\) for a uniformly random antipodally odd edge coloring.

*Proof.* Each edge \(e\) lies in \(N-1\) facets, and no proper facet contains both \(e\) and its antipode. On each facet containing \(e\), the flip changes \(B\) to \(B-2s(e)\), changing its square by \(4-4s(e)B\). Its antipodal facet contributes the same change. This gives (IE1). Also
\[
\sum_{[e]}T_e
=\tfrac12\sum_{\rm all\ edges\ e}s(e)\sum_{F\ni e}B(F)
=\tfrac12\sum_FB(F)^2=\Phi(c)/2.
\]
Summation proves (IE2). Every facet has \((N-1)2^{N-2}\) edges, independently and symmetrically signed under a random legal coloring, so the expectation of its squared imbalance is that edge count. There are \(2N\) facets. \(\square\)

**Corollary (extremal bad-coloring pivot condition).** Assume a bad legal coloring exists, and choose one maximizing \(\Phi\) among all bad legal colorings. Every orbit with \(T_e<N-1\) must be healing: flipping it produces a monochromatic full antipodal geodesic. In the original coloring, its changed edge occurs strictly inside a full geodesic and is the sole edge with the opposite color, so the original path has two adjacent switches. If instead a bad coloring minimizes \(\Phi\), the same statement holds for every orbit with \(T_e>N-1\).

*Proof.* The indicated flip strictly improves the chosen potential by (IE1), so it cannot stay bad. Apply the existing universal internal-pivot theorem to the repaired monochromatic geodesic: if its changed edge were absent or terminal, the original would have a path with at most one switch, which already forces a monochromatic antipodal geodesic. \(\square\)

In particular a maximum-energy bad coloring below the random baseline must have a healing positive-drift orbit, and a minimum-energy bad coloring above the baseline has a healing negative-drift orbit. This is a global criticality condition with no restricted-interaction hypothesis. To obtain closure it must be combined with the overlap structure of the forced internal two-switch paths.

## Free bridge variations force root coverage at small facet energy

Retain the facet imbalances \(B_j\) and energy \(\mathcal E(c)=\sum_jB_j^2\) from (FE1). Suppose bad colorings exist in dimension \(n\ge2\), and choose a bad coloring \(c\) maximizing this energy among all bad colorings in that dimension. Dimension minimality may be imposed before this maximization.

For each direction \(j\), let \(f_j\) be the ordinary coloring of the facet \(x_j=0\), and let
\[
U_j=V(Q_{n-1})\setminus\bigl(A_0(f_j)\cup A_1(f_j)\bigr),
\qquad K_j=\tfrac12|U_j|.
\tag{FB1}
\]
Thus \(U_j\) consists of roots admitting neither monotone orientation. It is antipodally invariant by reversal. Badness gives \(P(f_j)=\varnothing\), so
\[
|A_0(f_j)|=|A_1(f_j)|=2^{n-2}-K_j.
\tag{FB2}
\]

**Lemma (joint variations through empty bridge pairs).** Fix \(j\). Arbitrary simultaneous flips of the direction-\(j\) antipodal edge pairs indexed by \(U_j/\{u,\bar u\}\) preserve badness. For every subcollection \(F\) of these pairs, the vectors and signs of (FE1)--(FE2) satisfy
\[
\boxed{
\sum_{p\in F}s_p\langle B,v_p\rangle
\ge
\left\|\sum_{p\in F}s_pv_p\right\|_2^2.
}
\tag{FB3}
\]
In particular, at every empty bridge root \(u\),
\[
\boxed{
(-1)^{c_j(u)}
\sum_{h\ne j}B_h(-1)^{u_h}\ge n-1.
}
\tag{FB4}
\]

*Proof.* The horizontal coloring \(f_j\) is unchanged by any direction-\(j\) recoloring. At an empty root, neither bridge color has a monotone certificate. Thus changing any number of these bridge pairs cannot create a monochromatic full geodesic; the bridge correspondence makes all these changes jointly bad.

Flipping a subcollection \(F\) changes the imbalance vector to
\[
B-2\sum_{p\in F}s_pv_p.
\]
Its squared norm cannot exceed \(\mathcal E(c)\), by the selected maximality over bad colorings. Expanding the squared norm proves (FB3). A singleton has \(\|v_p\|_2^2=n-1\), giving (FB4). \(\square\)

Thus every root with
\[
\left|\sum_{h\ne j}B_h(-1)^{u_h}\right|<n-1
\]
admits one monotone orientation in \(f_j\). More generally this is true whenever the left side of (FB4), with its sign, is less than \(n-1\). Its available orientation is \(1-c_j(u)\), since the other orientation would already give a monochromatic full path in \(c\).

**Theorem (quantitative root-coverage bound).** For every direction \(j\),
\[
\boxed{
K_j^2\le\mathcal E(c)-B_j^2,\qquad
(n-1)K_j\le\mathcal E(c)-B_j^2.
}
\tag{FB5}
\]
Consequently, putting \(R_j=(\mathcal E(c)-B_j^2)^{1/2}\),
\[
\boxed{
|A_0(f_j)|=|A_1(f_j)|
\ge
2^{n-2}-\min\left\{R_j,\frac{R_j^2}{n-1}\right\}.
}
\tag{FB6}
\]

*Proof.* Fix the signs on all edge pairs other than the \(K_j\) empty direction-\(j\) pairs. Their contributions to the facet imbalance vector have the form
\[
B(t)=A+\sum_{p=1}^{K_j}t_pv_p,\qquad t_p\in\{-1,1\},
\tag{FB7}
\]
where \(v_{p,j}=0\), every other entry of \(v_p\) is \(1\) or \(-1\), and \(A_j=B_j\). Every choice of \(t\) remains bad by the lemma.

Average \(\|B(t)\|_2^2\) over independent fair signs. The mixed terms cancel, giving
\[
\mathbb E_t\|B(t)\|_2^2
=\|A\|_2^2+(n-1)K_j
\ge B_j^2+(n-1)K_j.
\]
Each value of this norm is at most \(\mathcal E(c)\), proving the second inequality in (FB5).

Choose any \(h\ne j\). The \(h\)-th component in (FB7) is \(A_h+\sum_pt_pv_{p,h}\). Its maximum absolute value over the free signs is \(|A_h|+K_j\ge K_j\). At such a choice, the \(j\)-th component is still \(B_j\). Hence the energy is at least \(B_j^2+K_j^2\), proving the first inequality. Formula (FB6) follows from (FB2). \(\square\)

**Corollary (imbalance versus empty-root density).** Let \(M=2^{n-2}\). If every facet imbalance satisfies \(|B_h|\le b\), then every facet of this energy-maximizing bad coloring obeys
\[
\boxed{
\frac{|U_j|}{2^{n-1}}
=\frac{K_j}{M}
\le \frac{\sqrt{n-1}\,b}{M}.
}
\tag{FB8}
\]
Conversely, if some facet has empty-root fraction at least \(\delta>0\), then a different facet has imbalance at least \(\delta M/\sqrt{n-1}\).

*Proof.* Formula (FB5) gives \(K_j^2\le\sum_{h\ne j}B_h^2\le(n-1)b^2\). The converse follows by taking the largest absolute term among the same \(n-1\) imbalances. \(\square\)

These conditions apply to an unrestricted energy-maximizing hypothetical counterexample. Small facet imbalance forces nearly complete coverage by the two disjoint monotone-root sets. Large empty-root sets force a quantitatively imbalanced facet. The joint variation inequalities (FB3) retain the compatibility of every collection of free bridge changes in one direction. Neither conclusion establishes paired-root existence: the two orientations can occupy different roots, and a closing argument must use their retained full paths.

The single-pair energy identity was independently checked on 1000 flips in random legal odd colorings of dimensions three through seven. The two norm bounds and the singleton condition were also checked on 500 independently generated free-sign optimization problems of the form (FB7), with all free assignments enumerated. The latter verify the variational calculation; they are auxiliary optimization systems rather than bad-coloring examples.



**Corollary (isolated-defect geodesic abundance).** With \(c,F,b\) as in the preceding one-facet extremality theorem, for each minority edge \(e\subset F\) there is a full antipodal geodesic \(P_e\) whose color word is \(b^{a_e}(1-b)b^{n-a_e-1}\), with \(1\le a_e\le n-2\), and with \(e\) as the unique wrong-color edge. Hence the original bad coloring contains at least the bound (FE5) distinct undirected full antipodal geodesics having a single strictly internal wrong-color edge in \(F\).

*Proof.* Take a color-\(b\) monochromatic full antipodal geodesic in \(c^{[e]}\). By internal restoration criticality it uses \(e\) strictly internally. Undoing that flip changes only the color at \(e\) along this path. The path for each \(e\) is distinct because its unique wrong-color edge identifies \(e\). \(\square\)

These geodesics are simultaneous witnesses in the unchanged extremal bad coloring, not merely in its separate repairs. Their interaction remains a closure question.


**Corollary (lexicographic facet-and-energy extremality).** Assume a bad legal coloring exists in \(Q_n\). Choose one maximizing the pair \((M(c),\mathcal E(c))\) lexicographically, where \(M(c)\) is the largest absolute facet imbalance and \(\mathcal E\) is (FE1). Let \(F\) be a maximizing facet, free in all dimensions except \(j\), and let \(g\) be its induced ordinary coloring. Then:

(i) Every minority edge in \(F\) is a healing pair, yielding all the isolated-defect witnesses of (FE6).

(ii) Every antipodal pair \(p\) of direction-\(j\) edges for which \(s_p\langle B,v_p\rangle<n-1\) is healing.

(iii) Let \(A(g)\) be the set of roots admitting a nondecreasing full facet path, with the bridge selector oriented as in the previously established restoration-fan theorem. For every direction-\(j\) pair disjoint from the antipodal root pairs represented in \(A(g)\), one has
\[
\boxed{s_p\langle B,v_p\rangle\ge n-1.}
\tag{FE7}
\]

*Proof.* Claim (i) follows from the maximizing-facet theorem: its flip raises \(M\). Flipping a direction-\(j\) edge pair leaves the colors of all edges in \(F\) unchanged, so it leaves the chosen facet imbalance unchanged and hence cannot lower \(M\). If such a flip raises \(\mathcal E\) by (FE2), lexicographic maximality forces goodness, proving (ii). By the restoration-fan theorem, a direction-\(j\) pair disjoint from \(A(g)\) and its antipodal image is not a healing pair. Thus its flip stays bad and cannot raise \(\mathcal E\), yielding (iii). \(\square\)

This simultaneously places exponentially many critical pivots in one facet and forces all nonhealing bridge pairs to align, with margin, with a weighted-majority field determined by the entire coloring. A closing argument must exploit the incompatibility, if any, between these routing constraints and the paired-root geometry of \(A(g)\).
## Simultaneous facet repairs and interval certificates

Assume a bad antipodally odd coloring c of Q_n exists and choose one maximizing the largest absolute signed facet imbalance among bad colorings. Let F be a maximizing facet, b its majority color, and D its minority-colored edge set.

**Theorem (simultaneous repair saturation).** Every nonempty S subset D gives a good coloring c^[S] after flipping all antipodal edge pairs indexed by S.

*Proof.* Each flipped minority edge increases the absolute signed imbalance of F by two. Thus the imbalance after all flips is |B_F(c)|+2|S|, exceeding the extremal maximum among bad colorings. QED.

There is an intrinsic description of the resulting paths. Fix a rooted full antipodal geodesic P. Define A_P={e in D:e belongs to P} and C_P={e in D:bar e belongs to P}. Call P eligible when every edge of color 1-b in the original coloring lies in D. For eligible P, it is monochromatic of color b after flips S precisely when A_P subset S and C_P intersect S is empty. A_P is nonempty by badness of c, and A_P,C_P are disjoint because P uses every dimension once.

**Corollary (Boolean interval covering).** With [A,T] denoting all sets S such that A subset S subset T,
[
2^D\setminus\{\varnothing\}=
\bigcup_{P\text{ eligible}}[A_P,D\setminus C_P].
\tag{BR1}
]
*Proof.* Every nonempty S produces a monochromatic full path by the theorem. Its antipodal image has the opposite color, hence some monochromatic full path has color b. Such a path is eligible and fulfills the stated incidence conditions. Conversely each listed interval supplies a color-b monochromatic full path after those flips, and its members are nonempty. QED.

**Corollary (path-certificate mass).** For independent Bernoulli-p selection of S subset D and each 0<=p<=1,
[
1-(1-p)^{|D|}\le\sum_{P\text{ eligible}}p^{|A_P|}(1-p)^{|C_P|}.
\tag{BR2}
]
*Proof.* Take the union bound on the interval cover. QED.

This furnishes dimension-uniform simultaneous repair constraints without a structural hypothesis on the direction functions. Whether such an interval covering can be excluded using dimension-simple path intersections remains open.

### A common extremizer for paired-root criticality and bridge energy

The one-facet and squared-energy arguments can be coupled to the bridge-independent minimum obstruction, with their quantifiers retained.

Suppose bad legal colorings exist in dimension \(n=d+1\). Let
\[
m_d=\min\{|E_1(f)|: f\text{ colors }Q_d,\ P(f)=\varnothing\},
\qquad L_d=d2^{d-1}.
\]
The minimum exists by the odd bridge equivalence. Global color complementation preserves paired-root absence, so \(m_d\le L_d/2\). Let \(M_*=\max_{c\ {\rm bad}}\max_j|B_j(c)|\).

**Theorem (identification of the two extremal problems).**
\[
\boxed{M_*=L_d-2m_d.}
\tag{CE1}
\]
Every facet attaining \(M_*\), with its minority color called one, is a minimum-one-edge paired-root obstruction. Consequently, repairing any nonempty subset of its minority edges creates a paired root in the facet itself. Every legal bridge assignment over the repaired facet is good.

*Proof.* Every facet of every bad legal coloring is paired-root-free. Its minority class has at least \(m_d\) edges, so its absolute imbalance is at most \(L_d-2m_d\). This proves the upper bound in (CE1). Conversely choose a minimizer \(f\). The bridge equivalence supplies a bad extension \(C(f,q)\), whose lower facet has imbalance \(L_d-2m_d\). This proves equality. An attaining facet therefore has \(m_d\) minority edges. Any nonempty minority repair lowers this count and must have a paired root by the definition of \(m_d\). The universal bridge criterion gives the final statement. \(\square\)

**Corollary (simultaneous criticality and free-bridge bounds).** Choose \(c\) maximizing \((M(c),\mathcal E(c))\) lexicographically among bad legal colorings, and let \(F=\{x_j=0\}\) be an attaining facet, after a cube symmetry. Its ordinary coloring \(f\), with colors normalized as above, has all the bridge-independent repairs in the theorem. At the same time, all joint free-bridge inequalities (FB3)--(FB8) hold for its empty-root pair count \(K_j\). In particular,
\[
\boxed{K_j^2\le\mathcal E(c)-B_j^2,\qquad
dK_j\le\mathcal E(c)-B_j^2.}
\tag{CE2}
\]

*Proof.* Any simultaneous change of the direction-\(j\) bridge bits at empty roots stays bad and leaves \(F\) unchanged. Its value of \(M\) is at least \(M_*\), because \(F\) still attains that value, and at most \(M_*\), by the definition of the global maximum. Thus \(M\) remains equal to \(M_*\). Lexicographic maximality now makes \(\mathcal E\) maximal over this entire free-bridge cube. The proofs of (FB3)--(FB8) apply verbatim to direction \(j\). \(\square\)

This common extremizer combines two previously separate sources of information: every nonempty minority repair gives opposite monotone paths at a common root, independently of the bridge; every empty root supplies a jointly free bridge bit subject to the quadratic bounds. The assertion about (FB3)--(FB8) is for the chosen maximizing facet. Lexicographic maximality alone does not justify those inequalities for every other direction.

**Closure attempt and remaining lemma.** The most direct continuation is to apply the singleton repair normal form (Propositions 22--23) simultaneously to this facet's minority edges. Each repair either joins two original zero arms through its single changed edge, or creates one orientation at a root already carrying the opposite original orientation. To close the argument, these witnesses must force compatible original arms at one root. The energy bounds constrain how many roots can be empty, while the weak-threshold theorem constrains signs of the full coloring's facet vectors; neither currently aligns the direction supports or interior seams of the repair witnesses. The common extremizer removes the incompatibility of the extremization choices, but this path-compatibility lemma remains unproved.


## Free-bridge twisting and root-activation congestion

Let \(n\ge3\), and suppose there exists a bad antipodally odd coloring \(c\) of \(Q_n\). Choose \(c\) maximizing its largest absolute facet imbalance among all bad colorings, and fix a maximizing facet \(F=\{x_j=0\}\). Complement both color labels if needed so that color zero is more frequent in \(F\). Let \(D\) denote its color-one edges, \(g=c|_F\), and \(A=A_0(g)\) the roots admitting a full \(0^*1^*\) facet path. Put \(m=n-1\) and
\[
q=2^{m-1},\quad
U=Q_m\setminus(A\cup\bar A),\quad K=|U|/2=q-|A|.
\]
The sets \(A,\bar A\) are disjoint by badness and the bridge equivalence. Let \(S\) be the zero-colored bridge selector; hence \(S\cap A=\varnothing\). Let \(\Omega=S\setminus U\), the fixed selected roots on the occupied antipodal root pairs. Then \(|\Omega|=|A|=q-K\).

**Lemma (free-selector dichotomy).** For every nonempty \(H\subseteq D\), let \(g^H\) be obtained from \(g\) by recoloring all edges of \(H\) zero and put \(A_H=A_0(g^H)\). At least one of the following holds:
\[
\boxed{
\Omega\cap A_H\ne\varnothing,\qquad
\exists u\in U:\ u,\bar u\in A_H.
}
\tag{FR1}
\]

*Proof.* After flipping \(H\) and the corresponding antipodal edge mates, the imbalance of \(F\) strictly exceeds its maximum in \(c\). The resulting legal coloring is good for **every** choice of colors on bridge pairs indexed by \(U/\{u,\bar u\}\), since bridge changes leave the facet unchanged. Keep all other bridge choices fixed as in \(c\). By the bridge equivalence, each of these selectors must meet \(A_H\). If \(\Omega\cap A_H\) were empty and no pair \(u,\bar u\subset U\) belonged to \(A_H\), choose in every free bridge pair the member outside \(A_H\). The resulting selector would avoid \(A_H\), contradiction. \(\square\)

**Lemma (a paired-root gain from one edge creates a monochromatic facet path).** Let \(h\) be any binary edge coloring of \(Q_m\), and let \(e\) be one edge. Suppose \(u,\bar u\notin A_0(h)\) but \(u,\bar u\in A_0(h^e)\), where \(h^e\) reverses the color of \(e\). Then \(h^e\) admits a monochromatic full geodesic from \(u\) to \(\bar u\) traversing \(e\). The corresponding geodesic in \(h\) has the color of every edge except \(e\) constant; the edge \(e\) is strictly internal.

*Proof.* The two \(0^*1^*\) paths from \(u\) and \(\bar u\) in \(h^e\) both traverse \(e\), since neither exists in \(h\). Reverse the latter, giving a \(1^*0^*\) path from \(u\) to \(\bar u\) through \(e\). Both paths traverse \(e\) in the same orientation and at the same rank, because the rank of each vertex from \(u\) equals its Hamming distance from \(u\). If the new color of \(e\) is zero, splice the zero prefix of the first path through \(e\) to the zero suffix of the reversed second path. If it is one, splice the one prefix of the second path to the one suffix of the first. The meeting vertex determines the set of previously used dimensions, so the splice is a full geodesic. Returning to \(h\) changes only \(e\). If \(e\) were terminal, reversing this nearly monochromatic path if necessary would produce a \(0^*1^*\) full path from \(u\) or \(\bar u\) in \(h\), contrary to the hypothesis. \(\square\)

**Theorem (activation congestion in a maximizing facet).** Write
\[
\delta_m=\left\lceil\frac{2^{m-2}}{1+m(m-1)}\right\rceil,
\qquad |D|\ge q+\delta_m,
\]
where the lower bound is the previously established geodesic-blocker gap. For each \(e\in D\) for which \(A_0(g^e)\) contains an antipodal pair lying in \(U\), designate \(e\) a *paired activation*; let \(r\) be their number. Every paired activation produces a monochromatic full geodesic in \(g^e\) with \(e\) as its unique strictly internal defect in \(g\).

Assign each remaining \(e\in D\) to a root \(y(e)\in\Omega\cap A_0(g^e)\), whose existence follows from (FR1). For \(y\in\Omega\), put \(d_y=|\{e:y(e)=y\}|\). Then
\[
\boxed{\sum_{y\in\Omega}(d_y-1)_+\ge\delta_m+K-r.}
\tag{FR2}
\]
In particular, either at least \(\delta_m+K\) minority-edge repairs create paired roots on formerly empty root pairs, or two distinct minority-edge repairs activate the same previously unfavorable bridge root.

*Proof.* There are \(|D|-r\) assigned edges and at most \(|\Omega|=q-K\) occupied targets. Therefore
\[
\sum_y(d_y-1)_+\ge |D|-r-|\Omega|
\ge (q+\delta_m)-r-(q-K)=\delta_m+K-r.
\]
The monochromatic facet-path assertion follows from the preceding shared-edge splicing lemma. \(\square\)

This reduction uses the full dimension-simple bridge correspondence and has no restriction on direction interactions. To complete NORI1 through this route, one must show that paired activations or collisions of restored monotone paths cannot persist in an imbalance-maximal bad coloring. Mere collisions do not automatically yield a monotone path: two different edge recolorings can each repair the same root while neither path exists before recoloring.



## Same-facet pivot injection into three-switch projective cycles

**Lemma.** In an antipodally odd coloring of \(Q_N\), fix a facet \(F\) and a color \(b\). A projective dimension-simple Petrie cycle with three switched comparisons supports at most one interior pivot \(e\subset F\) of color \(1-b\) whose removal from a full geodesic leaves a monochromatic word of color \(b\).

*Proof.* Such a geodesic has color word \(b^a(1-b)b^{N-a-1}\), \(1\le a\le N-2\). Its projective completion has two switches adjacent to the unique wrong-color observation and the third switch at the twisted closing seam. In a cyclic sequence with three switches, at most two observations can each be incident to two switches; if two exist they are adjacent across a switched comparison (the triangle case has the same property).

If two different pivots in \(F\) existed on one such cycle, their quotient observations would therefore be adjacent across a switch. Any incident lift between two horizontal edges in \(F\) and their antipodal partners connects either both edges in \(F\) or both antipodes in the opposite facet: mixing these is impossible because the fixed facet bits differ. Both valid lifts have equal edge colors, since the given pivots both have color \(1-b\) and antipodal reversal changes both. Their quotient comparison therefore cannot switch, a contradiction. \(\square\)

**Theorem.** Suppose a bad antipodally odd coloring of \(Q_N\), \(N\ge4\), maximizes the largest absolute facet imbalance among bad colorings. Let \(F\) be a maximizing facet and \(R\) its minority-color edges. If \(Z_1(c)\) counts projective Petrie cycles with three switches, then
\[
\boxed{Z_1(c)\ge |R|\ge2^{N-2}+
\left\lceil\frac{2^{N-3}}{1+(N-1)(N-2)}\right\rceil.}
\]
*Proof.* The maximal-facet healing theorem supplies, for each \(e\in R\), a full geodesic with \(e\) its only wrong-color edge and lying internally. Its projective completion has three switches. Choose one such cycle for each \(e\). The preceding lemma says distinct edges of \(R\) cannot yield the same cycle. The final inequality is the already proved unrestricted imbalance gap applied to the facet's induced coloring. \(\square\)

This doubles the previous generic grade-one witness bound in the extremal same-facet setting. It is a necessary condition on every possible unrestricted counterexample, not a new locality hypothesis. The lower bound by itself does not establish closure.


Corollary: In a bad coloring maximizing facet imbalance, there are more minority edges in the maximizing facet than majority-colored bridges perpendicular to that facet. Each minority edge has a full antipodal repair witness of the majority color, whose unique perpendicular bridge was unchanged. Pigeonhole therefore forces distinct minority pivots whose repair paths cross the same bridge edge. Their projective three-switch completions are distinct by the preceding pivot-injection theorem. This is an unavoidable global two-cycle configuration in any hypothetical counterexample, and is a precise target for a further exchange argument.

## Minority-repair dependency digraphs and shared-bridge obstructions

The simultaneous repair theorem above covers every nonempty set of minority edges in a maximizing facet. The next lemmas identify which subsets already have witnesses coming from the singleton repairs, and show why a collision of bridges alone is not enough for closure.

Fix a legal coloring c and a facet F with preferred color b. Let D be a set of edges of color 1-b in F. Assume for each e in D there is a full antipodal geodesic P_e whose only edge of color 1-b is e, strictly internally. (An imbalance-maximizing bad coloring has this property for its entire minority set.)

Define a directed graph T on D by
\[
e\longrightarrow f \quad\Longleftrightarrow\quad f\ne e\ \text{and}\ \bar f\in P_e.
\tag{RD1}
\]
Its outgoing degree is at most n-2, because a full geodesic P_e uses e, one edge perpendicular to F, and at most n-2 edges in the opposite facet.

**Theorem (dependency-sink repair certificate).** If a nonempty set S subset D has some e in S without an outgoing neighbor in S, then the simultaneous antipodal pair flip at S has a monochromatic full geodesic, witnessed by P_e. Hence every set S for which the induced directed graph T[S] is acyclic is automatically repaired by one of the chosen singleton witnesses.

*Proof.* Originally P_e consists entirely of color b edges except e. Flipping all pairs indexed by S changes e to b. It does not change any other edge of P_e: no other member of D occurs on P_e, and the only other potentially changed edges are antipodal mates bar f with f in S. By the sink hypothesis P_e avoids all such edges. Thus P_e is entirely color b after the simultaneous recoloring. QED.

**Corollary (large independent repair subcubes).** There is a subset I of D of size at least \(|D|/(2n-3)\) such that every nonempty subset S of I is repaired by the already chosen singleton witnesses. In particular, the simultaneous repair condition on 2^D contains a Boolean subcube of dimension at least \(|D|/(2n-3)\) that imposes no additional witness condition beyond singleton healing.

*Proof.* The underlying undirected graph of T has average degree at most 2(n-2). The standard greedy/random-order independent-set bound gives an independent set I of size at least |D|/(2n-3). Any nonempty S subset I has a sink. QED.

**Proposition (exponentially many same-bridge pivots at an empty facet-root pair).** Fix integers \(m\ge4\) and \(a,b,c\ge1\) with \(a+b+c+1=m\). On Q_m color the edges between Hamming layers of ranks k and k+1 by 1 when k<a or k=a+b, and by 0 otherwise. Every full path from 0^m to 1^m then has color word
\[
1^a0^b1\,0^c,
\]
and every reverse path has \(0^c1\,0^b1^a\). Hence neither pole belongs to the nondecreasing favorable-root set A_0.

Embed this coloring as the lower facet F of Q_{m+1}, define its antipodal extension in the upper facet, and color the bridge at y=1^m by zero (therefore the bridge at 0^m has color one). Then for each edge e in the rank-(a+b) layer of F there is a full antipodal geodesic P_e traversing the SAME color-zero bridge at y, whose only color-one edge is e and for which e is strictly internal. There are
\[
\boxed{(m-a-b)\binom{m}{a+b}}
\tag{RD2}
\]
different such edges and witnesses, of order \(\sqrt m\,2^m\) when the defect layer is central.

*Proof.* Choose any monotone facet path from 0^m to 1^m through e, and write its vertices after the first a dimensions as x. From (x,0), follow the remainder of that path to (y,0), cross the fixed bridge, then in the upper facet traverse the antipodal image of the first a edges, from (y,1) to (bar x,1). In the lower segment the word is \(0^b1\,0^c\). The bridge and all upper edges have color zero, by construction and antipodal oddness. Hence the only nonzero edge is e and it occurs internally. There are \((m-a-b)\binom{m}{a+b}\) rank-(a+b) edges, and different e give different paths. QED.

The proposition is a counterexample to any claim that two, or even exponentially many, distinct internal defect paths passing through one bridge whose antipodal facet roots are both unfavorable must splice into a favorable facet path. The global bad-coloring hypothesis and its constraints across all bridges cannot be discarded. The dependency digraph also shows that only subsets whose chosen witnesses all inhibit each other (which necessarily contain a directed cycle) have a chance to add information beyond singleton repairs.


## Bridge-distance holonomy and sharp two-cycle separation

**Theorem (bridge-distance holonomy).** Fix a facet F of Q_n and let P_e be full antipodal geodesics oriented from F to its opposite facet, each crossing a bridge at y_e and having a single strictly internal minority pivot e in F. Define e->f if P_e traverses bar f in the opposite facet. For any edge e of direction i in F put R_y(e)={l!=i:e_l!=y_l}, and d_y(e)=|R_y(e)|, the distance from y to edge e. If e->f then R_{y_e}(e) union {i} is a subset of R_{y_e}(f), hence d_{y_e}(f)>=d_{y_e}(e)+1. Proof: dir f=k has not flipped before the bridge, so k is not in R_{y_e}(e). Any l in R_{y_e}(e) flips after e but before the bridge, hence bar f_l=y_e_l and f_l!=y_e_l. Direction i flips at e and cannot flip again, so bar f_i=y_e_i and f_i!=y_e_i. Thus the inclusion. For a directed cycle e_1->...->e_t->e_1, sum the inequalities and reindex to obtain t<=sum_s[d_{y_(s-1)}(e_s)-d_{y_s}(e_s)]<=sum_s d_H(y_(s-1),y_s), using the 1-Lipschitz property of edge-distance. No cycle can occur when all bridge positions coincide. Moreover, if e->f and f->e, y=y_e,z=y_f, i=dir e,k=dir f, then y_i!=z_i and y_k!=z_k. For any l outside i,k with y_l=z_l, the two inclusion relations show e_l=f_l. If this common bit disagrees with y_l, l must be traversed after e and before the bridge on P_e; if it agrees, l must be traversed after the bridge and before bar f. Therefore every step before e or after bar f occurs in a direction where y,z disagree, outside i,k. If a_e counts the steps before e and b_e those after bar f, d_H(y,z)>=2+a_e+b_e>=3. The two bridges have the same color, hence are not antipodal; d_H(y,z)<=m-1 with m=n-1. Sharpness: in Q5, bit4 facet direction, prescribe colors (0,1,0,0,0) on the rooted full geodesics (root,order)=(1,(2,0,4,3,1)) and (5,(2,1,4,3,0)). These prescriptions occupy seven compatible antipodal edge-pair orbits and can be completed arbitrarily. The minority pivots e=(0,4),f=(1,1) are internal; P_e contains bar f=(1,28), P_f contains bar e=(0,26). Their bridge positions 4 and3 in Q4 have Hamming distance3. This is a legal coloring but not claimed bad. The metric obstruction localizes any cyclic critical-repair interactions to differing bridge positions, beyond fixed-bridge collisions.

### Full rank-growth identity and reinforced bridge-cycle holonomy

With the bridge dependency notation of (BH1), let \(P_e\) traverse \(e\) in the lower facet, cross the bridge at \(y=y_e\), and later traverse \(\bar f\) in the upper facet. Let \(a_e\) count steps before \(e\), and \(b_e\) steps after \(\bar f\). Then
\[
\boxed{d_y(f)-d_y(e)=1+a_e+b_e.}\tag{BH6}
\]

*Proof.* Distinct dimensions on a full path fall into the five groups: before \(e\), at \(e\), between \(e\) and the bridge, between the bridge and \(\bar f\), at \(\bar f\), and after \(\bar f\). Each dimension before \(e\) or after \(\bar f\) has the fixed bit of \(e\) equal to \(y\), and that of \(f\) opposite \(y\); so it contributes one to \(d_y(f)-d_y(e)\). The direction of \(e\) contributes one as well. Each dimension strictly between \(e\) and the bridge disagrees with \(y\) at both \(e\) and \(f\), contributing zero to the difference. Each dimension strictly between the bridge and \(\bar f\) agrees with \(y\) at both, also contributing zero. Finally, the direction of \(f\) contributes zero by definition. Summing gives (BH6). \(\square\)

**Theorem (reinforced cycle-perimeter bound).** A dependency cycle \(e_1\to\cdots\to e_t\to e_1\), with bridges \(y_s=y_{e_s}\), prefix lengths \(a_s\) before each \(e_s\), and suffix lengths \(b_s\) after each \(\bar e_{s+1}\), satisfies
\[
\boxed{\sum_{s=1}^t d_H(y_s,y_{s+1})
\ge\sum_{s=1}^t(1+a_s+b_s)\ge2t.}
\tag{BH7}
\]
*Proof.* Sum (BH6) over the cycle, cyclically reindex and apply the 1-Lipschitz inequality for \(y\mapsto d_y(e)\), as in the proof of (BH2). Each minority pivot is strictly internal, hence \(a_s\ge1\). \(\square\)

This strengthens the previously published perimeter bound from \(t\) to \(2t\), with additional penalties for long witness arms. The rank-growth identity was independently checked for every admissible pivot/upper-mate position and direction order in Q3, Q4, Q5 (8, 192, 3840 instances); the argument above holds for all dimensions.


Rooted reachability repair lemma. For arbitrary edge coloring, a root initially lacking nondecreasing geodesics becomes favorable after changing one edge from one to zero precisely when the edge tail is reachable from the root through zero edges and its head admits a nondecreasing completion to the antipode. This follows by splitting the repaired path at its changed zero edge. The two endpoint sets are disjoint before repair.

**Two-phase rooted restoration theorem.** For arbitrary edge coloring f and root r not admitting a nondecreasing full geodesic, orient the cube from r by subsets. Write Z for zero-only reachable states, V for nondecreasing-prefix reachable states, U for states permitting nondecreasing completion to the top, and O for states permitting all-one completion. Then Z intersect U and V intersect O are both empty. Changing a one edge u-v to zero restores r precisely when u lies in Z and v lies in U. Changing a zero edge u-v to one restores r precisely when u lies in V and v lies in O. Necessity follows by splitting a newly favorable path at the recolored edge, and sufficiency by concatenating its specified prefix and suffix.

**Transverse facet synchronization theorem.** In a bad odd cube coloring, any antipodal edge pair whose reversal makes the coloring good gives a rooted edge repair in every facet transverse to its direction. To see this, take a monochromatic zero antipodal geodesic after reversal. Its bridge in each other direction remains zero, so the bridge correspondence identifies a favorable root in the repaired lower facet. The same root was not favorable before reversal, or the original cube coloring would have been good. All these root repairs are synchronized by one geodesic.

## Facet energy as first-level Walsh mass

Let c be any antipodally odd binary coloring of E(Q_n), n>=3. Put \(\sigma_i(x)=(-1)^{c_i(x)}\), independent of bit i, \(d(x)=\sum_i\sigma_i(x)\), and let B_j be the signed color sum of edges internal to facet x_j=0. Write \(\widehat d(S)=2^{-n}\sum_xd(x)(-1)^{\sum_{i\in S}x_i}\).

**Theorem.** For all j,
\[
\boxed{B_j=\tfrac14\sum_x(-1)^{x_j}d(x)
=2^{n-2}\widehat d(\{j\}),\quad
\mathcal E(c)=2^{2n-4}\sum_j\widehat d(\{j\})^2.}
\tag{FW1}
\]
The Walsh spectrum of d is supported on odd subsets S other than the full set [n].

*Proof.* Since \(\sigma_j\) ignores bit j and is odd when the other bits are complemented, its sum over the facet x_j=0 is zero. Summing d over that facet counts each horizontal edge twice and each vertical edge with total zero; hence \(\sum_{x_j=0}d(x)=2B_j\). Antipodal oddness gives \(\sum_{x_j=1}d(x)=-2B_j\), proving (FW1). The function d is antipodally odd, so all even Walsh levels vanish. For every i, \(\sigma_i\) ignores x_i, so its Fourier coefficient on [n] vanishes; the same holds for d. \(\square\)

**Corollary (unrestricted spectral sufficiency, including equality).** Every legal coloring satisfying
\[
\boxed{\mathcal E(c)\ge2^{2n-4}(n^2-6n+6)}
\tag{FW2}
\]
admits a monochromatic full antipodal geodesic. The same conclusion holds if \(\sum_S\widehat d(S)^2\ge n^2-6(n-1)\).

*Proof.* Let \(r(x)\) be the number of incident edges of color one. Then \(d(x)=n-2r(x)\) and \(r(x)(n-r(x))=(n^2-d(x)^2)/4\). Thus the projective-vertex bichromatic-turn count is
\[
N_c=\tfrac18\sum_x(n^2-d(x)^2)
=2^{n-3}\left(n^2-\sum_S\widehat d(S)^2\right).
\tag{FW3}
\]
The mixed exchange variance theorem in “Global Petrie switch moment and local-turn counting” proves that a constant Petrie grade must equal one. Therefore every bad coloring has mean Petrie grade strictly greater than three, so \(N_c>3\cdot2^{n-2}(n-1)\). It follows that \(\sum_S\widehat d(S)^2<n^2-6(n-1)\). Parseval and (FW1) give \(\mathcal E(c)<2^{2n-4}(n^2-6n+6)\). The contrapositives prove both assertions. \(\square\)

The same mixed exchange theorem supplies a positive quantitative gap below these bad-coloring bounds in dimensions at least six. In dimension five, the pointwise inequality \(d(x)^2\ge1\) already reaches the equality threshold, giving an analytic NORI1 proof; the accompanying multiplicity argument gives at least three monochromatic-zero unoriented full antipodal geodesics.

The identity gives a direct relation between the facet-energy extremal argument and the global Petrie turn moments, without restricting the coloring class. It measures only first-order spatial imbalance, so its sufficient condition need not hold for well-distributed colorings.


Bridge-root metric theorem. Bridge-root metric selection theorem (unrestricted, n>=3). Let P be a full dimension-simple antipodal geodesic, and for each direction j let w_j be the lower endpoint of its unique direction-j edge, represented by bits outside j. Define D_ij=1+d_H(w_i restricted away from i,j, w_j restricted away from i,j). Then D_ij=|rank_P(i)-rank_P(j)|. Indeed, a bit k outside i,j differs at the two bridge endpoints precisely when direction k occurs strictly between i,j along P. Conversely, suppose a family of candidate bridge endpoints has D_ij=|rank(i)-rank(j)| for some permutation of the n directions. Adjacent directions in that permutation have D=1, so their endpoint labels agree at every bit other than their two direction bits. Hence for any fixed k, the kth bits of the other endpoints are constant on each side of k in the proposed order. If k is internal, the two endpoints adjacent to k have D=2; every shared bit other than k agrees by the adjacent-pair equalities, so their kth bits differ. Choose initial root bit r_k as the common kth bit of all earlier endpoints if there are earlier ones; if k is first, set r_k to the complement of the common kth bit of all later endpoints. Then w_j(k)=r_k XOR [k precedes j] for all j different from k. The path starting at r and traversing the proposed order has precisely the given bridge endpoints. The line metric recovers the direction order up to reversal and then determines the unoriented geodesic uniquely. This was exhaustively audited over all candidate bridge endpoint assignments: 24 valid families in Q3 and 192 in Q4, matching their numbers of unoriented antipodal geodesics. NORI1 therefore has a complete unrestricted metric-selection reformulation: For an odd cube-edge coloring c, in each direction j let Z_j be the lower endpoints of its zero edges (one choice from every antipodal edge pair). A monochromatic-zero antipodal geodesic exists if and only if one can select w_j in Z_j for every j so that D is a consecutive-integer line metric. A healing antipodal edge orbit produces an otherwise zero-colored line-metric selection with its unique wrong-color chosen edge in the healed direction.


**Corollary (enumeration and the random baseline).** In \(Q_n\), \(n\ge3\), the number of valid bridge-root line-metric selections equals
\[
\boxed{2^{n-1}n!}.
\]
For a uniformly random antipodally odd coloring of cube edges, the expected number of monochromatic-zero full antipodal geodesics is
\[
\boxed{\mathbb E N_0=\frac{n!}{2}}.
\]
*Proof.* Every unoriented full geodesic has two oriented descriptions, obtained by choosing its first endpoint and an ordering of all \(n\) directions. There are \(2^n n!\) oriented descriptions, and the bridge-root characterization is a bijection on unoriented geodesics. This gives \(2^{n-1}n!\) signatures. For a fixed full geodesic, its \(n\) edges belong to distinct antipodal edge orbits because the directions are distinct. Their colors are therefore independent fair bits under a uniformly random odd coloring, so the chance all edges are zero is \(2^{-n}\). Sum over geodesics by linearity of expectation. \(\square\)

The factorial random baseline supports the proposed distribution-versus-extremal viewpoint, but it does not establish existence for every coloring; a deterministic transversality or path-exchange argument is still needed.



**Lemma (one-direction overlap rigidity).** Let \(P,Q\) be dimension-simple full antipodal geodesics in \(Q_n\), \(n\ge3\), that use the same undirected edge in every direction except possibly direction \(i\). Either they coincide up to reversal, or their differing direction-\(i\) edges form an antipodal pair and both are terminal edges of their respective paths.

*Proof.* Delete the direction-\(i\) edge of \(P\). If it was internal, the remaining edge set forms two nonempty paths. Among their four candidate endpoint pairs, only the original joining pair differs in one bit: every other pair differs in at least two, since the removed direction is distinct from every remaining path direction. Thus the deleted edge is the unique reconnection. If the removed edge was terminal, the remaining edges form one path of length \(n-1\). Completing it by a direction-\(i\) edge requires extending one endpoint or the other; these two edges are antipodal because the remaining chain traverses every other direction once. \(\square\)

**Corollary (distinct defects force two changed directions).** In an antipodally odd coloring, two full geodesics with distinct unique wrong-color edges of the same minority color and every other edge of the opposite majority color must differ in their selected undirected edges in at least two direction classes. Otherwise the unique wrong-color edges would be identical or antipodal, contrary to their distinctness and common color.

This supplies a two-direction separation condition on the full bridge signatures of the different critical repair geodesics forced by extremal facet imbalance.



## Universal triangle-compatible selectors and tournament closure

Let \(n\ge3\). For every direction \(i\), let \(\chi_i\) color its lower-edge endpoints \(w\in\mathbb F_2^{[n]\setminus\{i\}}\), with antipodal oddness \(\chi_i(\bar w)=1+\chi_i(w)\). A bridge-row family \(W=(w_1,\ldots,w_n)\) has symmetric pair labels \(\tau_{ij}=w_i(j)+w_j(i)\). Define **triangle compatibility** by
\[
\boxed{\tau_{ij}+\tau_{jk}+\tau_{ki}=1\quad(i,j,k\text{ distinct}).}\tag{TC1}
\]

**Theorem (tournament representation).** Equation (TC1) is equivalent to the existence of a vertex \(r\in\mathbb F_2^n\) and a tournament \(T\) on the direction set for which
\[
\boxed{w_i(j)=r_j+[j\prec_T i]\quad(i\ne j).}\tag{TC2}
\]
The two representations are \((r,T)\) and \((\bar r,T^{\rm rev})\). The family represents a full antipodal dimension-simple geodesic precisely when the tournament is transitive.

*Proof.* Equation (TC2) implies \(\tau_{ij}=1+r_i+r_j\), giving (TC1). Conversely, the triangle equations imply the symmetric pair values \(1+\tau_{ij}\) form a coboundary on \(K_n\); choose \(r_1=0\) and \(r_j=1+\tau_{1j}\). Then \(1+\tau_{ij}=r_i+r_j\). Define the indicator of \(j\prec_T i\) to be \(w_i(j)+r_j\). Opposite indicators sum to \(\tau_{ij}+r_i+r_j=1\); hence these prescribe a tournament. The coboundary potential \(r\) is unique up to global complementation, which reverses \(T\). A tournament describes a direction order if and only if it is transitive. \(\square\)

**Theorem (equipartition of compatible monochromatic rows).** For every antipodally odd edge coloring, the number of triangle-compatible families with all chosen direction edges color zero is independent of the coloring:
\[
\boxed{|\{W:\text{(TC1)},\ \chi_i(w_i)=0\ \forall i\}|=2^{\binom n2-1}.}\tag{TC3}
\]

*Proof.* The \(\binom n2\) pair labels have \(2^{n-1}\) feasible assignments, determined by \(\tau_{1j}\) for \(j>1\). For each prescribed pair bit \(\tau_{ij}\), there are two assignments to its two directed entries \(w_i(j),w_j(i)\). Thus \(2^{\binom n2+n-1}\) families satisfy (TC1).

Complementing a row \(w_i\) toggles both of its contributions in each triangle containing \(i\), leaving (TC1) unchanged. These independent row flips act freely with orbit size \(2^n\). Antipodal oddness guarantees that complementing row \(i\) toggles precisely the selected color \(\chi_i(w_i)\), with all other colors unaffected. Therefore each orbit contains one member with all selected colors zero. Division by \(2^n\) proves (TC3). \(\square\)

**Unrestricted NORI1 reformulation.** The conjecture holds if and only if at least one of the \(2^{\binom n2-1}\) guaranteed all-zero triangle-compatible families has a transitive tournament. Thus the pairwise and triangle consistency constraints never obstruct selection; the remaining problem is global tournament acyclicity.

**Obstruction to closing by local compatibility alone.** For even \(n\), take the valid antipodally odd coloring \(\chi_i(w)=\sum_{j\ne i}w_j\). Fix any tournament \(T\), including a tournament with directed triangles, and let \(d_i\) be its indegrees. Put \(R=\binom n2\bmod2\), \(r_i=R+d_i\bmod2\). Since \(n\) is even, \(\sum_i r_i=R\), and the compatible rows (TC2) have
\[
\chi_i(w_i)=\sum_{j\ne i}r_j+d_i=R+r_i+d_i=0.
\]
Thus directed triangles do occur among all-zero compatible families. A proof of NORI1 needs a mechanism selecting a transitive member, not just a nonempty compatible family.

Exhaustive checks in dimensions three and four confirmed the respective constant numbers four and 32 of all-zero compatible families for every odd coloring. The theorem is dimension-uniform and does not rely on these checks.



### Self-switching tournament normalization and its local-descent obstruction

For a tournament \(T\) on \([n]\), let \(b_i(T)\) denote the Boolean vector of its in-neighbors at \(i\): \(b_i(j)=[j\prec_T i]\). Given an arbitrary antipodally odd cube-edge coloring with local functions \(\chi_i\), put
\[
s_i(T)=\chi_i(b_i(T)),\qquad
F_\chi(T)=\operatorname{Switch}_{s(T)}(T),
\tag{TN1}
\]
where switching reverses an arc \(i,j\) precisely when \(s_i+s_j=1\).

**Theorem (canonical all-zero normalization).** For every tournament \(T\), the bridge rows
\[
w_i=b_i(T)+s_i(T)\mathbf1_{[n]\setminus\{i\}}
\tag{TN2}
\]
are triangle-compatible and all have color zero. The starting root associated with the tournament representation of these rows is \(r=s(T)\), and its tournament is \(F_\chi(T)\). Moreover, the map \(T\mapsto(w_i)\) has fibers precisely \(\{T,T^{\rm rev}\}\). Consequently it parametrizes the \(2^{\binom n2-1}\) all-zero compatible families by tournaments modulo reversal.

*Proof.* Since each \(\chi_i\) is antipodally odd, \(\chi_i(w_i)=\chi_i(b_i)+s_i=0\). The rows are obtained from tournament rows by independent complementation, which preserves triangle compatibility. Relative to root \(s\), their pair directions are
\[
w_i(j)+s_j=b_i(j)+s_i+s_j,
\]
namely the tournament obtained by the indicated star switches.

If \(T\) and \(S\) give the same rows, their input in-neighbor vectors are equal or complementary at each vertex, according to their differences in correction bits \(s_i\). Antisymmetry of tournament arcs forces these differences to agree for all vertices. They are therefore either all zero, giving \(T=S\), or all one, giving \(S=T^{\rm rev}\). Conversely reversal complements every \(b_i\) and toggles every \(s_i\), leaving (TN2) unchanged. \(\square\)

**Single-arc response.** Let \(T^{ij}\) reverse just the arc \(i,j\). Only \(s_i,s_j\) can change. Write
\(\delta_i=s_i(T^{ij})+s_i(T)\), \(\delta_j=s_j(T^{ij})+s_j(T)\). Then
\[
\boxed{
F_\chi(T^{ij})
=\operatorname{Switch}_{\delta_i e_i+\delta_j e_j}
\bigl(F_\chi(T)^{ij}\bigr).
}
\tag{TN3}
\]
The derivatives \(\delta_i,\delta_j\) are the Boolean sensitivities of the two incident direction functions at their present input vectors.

**Contrast with ordinary tournaments.** If \(D(T)\) is the number of directed triangles, then
\[
D(T)=\binom n3-\sum_v\binom{d_v^+(T)}2.
\]
Reversing an arc \(a\to b\) changes this count by \(d_a^+(T)-d_b^+(T)-1\). Every nontransitive tournament contains a directed triangle, along which at least one arc has \(d_a^+\le d_b^+\); reversing that arc strictly lowers \(D\). Thus ordinary triangle count has no nontransitive single-arc local minima. Equation (TN3) shows why this descent does not automatically extend to all-zero normalized tournaments: the incident star responses can undo the improvement.

**Finite obstruction to a naive descent proof.** In \(Q_4\), number antipodal edge-orbit variables by direction \(i=0,1,2,3\), with canonical lower endpoints respectively \(0,2,4,6\) for direction 0; \(0,1,4,5\) for direction 1; and \(0,1,2,3\) for each of directions 2,3. Set their color bits to the 16-bit mask \(\texttt{0x5af1}\), and give the antipodal edge the opposite color. Encode a tournament by six bits for pairs \((01),(02),(03),(12),(13),(23)\), bit one meaning the first vertex precedes the second. Direct substitution into (TN1) yields
\[
F_\chi(14)=36,\qquad D(36)=1,
\]
whereas for single-arc input neighbors \(14\oplus2^k\), \(k=0,\ldots,5\), the respective outputs are
\[
34,\ 12,\ 19,\ 44,\ 45,\ 4,
\]
all of which have two directed triangles. Thus a cyclic normalized output can be a strict local minimum under every input single-arc change, despite the same coloring admitting monochromatic antipodal geodesics elsewhere.

**Global closure formulation.** NORI1 is equivalent to requiring a transitive tournament in the image of \(F_\chi\) for every antipodally odd coloring. A proof must use more than simple triangle-count descent on the single-arc exchange graph.



### Zero bridge-row extension and pairwise uniformity

Fix \(I\subseteq[n]\), \(1\le k=|I|\le n\), and prescribe one zero-colored bridge row \(w_i\) for every \(i\in I\). Assume these rows satisfy the triangle equations (TC1) on triples internal to \(I\). Then the number of completions to triangle-compatible all-zero bridge families is
\[
\boxed{2^{\binom{n-k}{2}}.}\tag{TE1}
\]
A violation of an internal triangle equation prevents completion.

*Proof.* Put \(h=n-k\). The tournament-potential representation (TC2) gives a potential on \(I\) unique up to common complementation, since all its internal triangle equations hold. Choose potential values on the other \(h\) directions freely and choose one directed entry for every pair among those directions freely. Entries in the opposite orientations and across \(I\) are then determined. After identifying the global complementary potentials, there are \(2^{h+\binom h2}\) triangle-compatible extensions with arbitrary colors in the unknown rows. Independently complementing any unknown row preserves all triangle equations and flips only that row's chosen edge color by antipodal oddness. Every free row-flip orbit of size \(2^h\) has one member with all unknown colors zero. Division proves (TE1). \(\square\)

**Consequences.** Any two zero-colored bridge edges in distinct directions extend to such a family, regardless of their positions. Under the uniform distribution on all-zero triangle-compatible families, any two selected rows are independent and uniform over their respective sets of zero edges. Any \(n-1\) prescribed zero rows satisfying their internal triple equations have a unique final zero-row completion.

The first compatibility obstruction occurs at triples of directions, not pairs. Selecting a *transitive* tournament still requires an additional global condition.



### Sequential extension and a universal branching law

Let \(W\) range over all-zero triangle-compatible bridge families of a legal odd coloring of \(Q_n\), \(n\ge3\). Fix any order of the directions and suppose \(k\ge1\) bridge rows have been prescribed with zero color and all internal triangle equations holding.

**Theorem (regular next-row branching).** The next unselected direction has precisely
\[
\boxed{2^{n-k-1}}
\tag{SE1}
\]
possible zero-colored bridge rows that preserve the triangle equations. Every such choice has the same number of subsequent all-zero completions, namely \(2^{\binom{n-k-1}{2}}\). Consequently, uniformly sampling one of the admissible next rows at every stage produces the uniform distribution on all \(2^{\binom n2-1}\) compatible all-zero families.

*Proof.* Let \(j\) be the next direction and choose one prior direction \(i_0\). For every other previously selected \(i\), its triangle equation with \(j,i_0\) prescribes the parity \(w_j(i)+w_j(i_0)\). These \(k-1\) independent affine equations on the \(n-1\) bits of \(w_j\) are consistent because the previous rows satisfy their internal triangle equations. Their solution set is an affine subspace of dimension \(n-k\), stable under complementing every bit of \(w_j\). Antipodal oddness selects precisely one zero-colored row from each complementary pair, leaving \(2^{n-k-1}\) possibilities. The constant remaining completion count follows from (TE1); multiplication of branching factors gives the stated total. \(\square\)

In particular, the first two selected bridge rows are independent and uniform over their respective zero-edge sets; the first restrictions arise when selecting a third direction. The final row is uniquely determined.


Fix k directions of an odd coloring of Q_n. The law of their selected bridge rows under a uniformly random all-zero triangle-compatible family is a convex mixture of the corresponding laws for odd Q_k colorings. For each partial row u, let a_i(u) count zero full rows restricting to u. Antipodal oddness gives a_i(u)+a_i(complement u)=2^(n-k). The extension theorem counts full completions of any compatible k-row tuple as 2^binomial(n-k,2) times the product of its a_i values. Normalize these counts into independent probabilities for random odd Q_k edge colors. Since every such Q_k coloring has the same number of compatible zero-row families, averaging its uniform distribution recovers the projected law. This transfers all local tournament-event probability bounds across dimensions.


### Star-critical tournament classification

For a nontransitive tournament \(T\), call \(i\) a star-critical center if reversing every incident arc makes \(T\) transitive. In dimension \(n\ge4\), there are at most two such centers. If \(i,j\) are both centers, every third vertex \(h\) has opposite relations with \(i,j\):
\[
[h\to i]\ne[h\to j].
\tag{SC1}
\]
Indeed, choose transitive \(L=S_iT\). Another center \(j\) requires \(S_{\{i,j\}}L\) transitive. Switching a subset of a transitive tournament preserves transitivity precisely when the subset is an initial or terminal segment in its linear order. Since \(i\) must be internal in \(L\), the two-set \(\{i,j\}\) is its first two or final two members. Consequently every \(\{i,j,h\}\) is cyclic in \(T\), and at most one additional center exists.

Counting pairs \((L,i)\) with \(L\) transitive and \(i\) internal gives \(n!(n-2)\). Of these, \(2n!\) have \(i\) second or penultimate, each arising twice from a two-center tournament. Therefore the number of tournaments with two, one, or zero centers is respectively
\[
n!,\quad (n-4)n!,\quad 2^{\binom n2}-(n-2)n!.
\]
These assertions were also exhaustively checked for \(n=4,5,6\).


Same-facet healing-pair exclusion. In any bad legal odd coloring, a single zero-compatible bridge family cannot certify two distinct healing edge pairs whose newly zero members belong to the same facet F. Indeed, changing a direction-i antipodal edge pair acts on the compatible ensemble by complementing row i, and thus switches the induced tournament star at i. Two certified repairs in directions i,j would make them two star-critical centers of one nontransitive tournament. By the previously proved two-center theorem, the two chosen rows have opposite bits in every other direction. Yet the original chosen zero edges are antipodes of both healing edges in F, so lie together in the opposed facet and agree at its normal bit, contradiction. The row-extension theorem also shows that each antipodal pair flip acts on a block of 2^binomial(n-1,2) compatible families, leaving all others unchanged. Consequently the certification families of distinct minority-edge repairs in any imbalance-maximizing facet are disjoint.


### Global repair-budget identity

Let \(c\) be a bad antipodally odd coloring of \(Q_n\), \(n\ge4\), let \(\mathcal W(c)\) be its \(2^{\binom n2-1}\) compatible all-zero bridge families, and let \(N_0(d)\) count monochromatic-zero full antipodal geodesics of a legal coloring \(d\). For the associated tournament \(T_W\), put
\[
\kappa(T_W)=|\{i:S_iT_W\text{ is transitive}\}|.
\]

**Theorem (critical-neighbor identity).**
\[
\boxed{
\sum_{\text{antipodal edge pairs }[e]}N_0(c^{[e]})
=\sum_{W\in\mathcal W(c)}\kappa(T_W)
\le 2^{\binom n2}.}
\tag{RB1}
\]
For every fixed facet \(F\), let \(D_F\) be its edges of color one. Then
\[
\boxed{\sum_{e\in D_F}N_0(c^{[e]})
\le 2^{\binom n2-1}.}
\tag{RB2}
\]

*Proof.* The one-pair surgery bijection complements the direction-\(i\) selected row in precisely those old compatible families selecting the old zero member of \([e]\). An all-zero transitive family of the changed coloring must arise in this block, since \(c\) is bad; its old tournament has star-critical center \(i\). Conversely each star-critical center \(i\) of an old family specifies a unique affected antipodal edge pair whose reversal makes its row-complement family transitive. This gives equality in (RB1). The two-center theorem bounds \(\kappa\le2\).

For (RB2), the same-facet disjointness theorem shows that each old compatible family can certify at most one changed pair having its one-colored member in \(F\). Sum the corresponding incidence counts. \(\square\)

These are dimension-uniform upper bounds on *total monochromatic path multiplicity produced by single-pair repairs of a bad coloring*. Combined with facet-imbalance extremality they turn the proof target into finding a sufficient lower bound on the repair multiplicities; mere existence of one geodesic per repaired edge does not exhaust the available budget.



## Uniform switching-class fiber theorem

Let \(\mathcal W(c)\) be the all-zero triangle-compatible bridge families for an arbitrary antipodally odd coloring of \(Q_n\), \(n\ge3\). Partition tournaments on \([n]\) by star switching: two tournaments are equivalent if one is obtained from the other by reversing all arcs crossing a vertex subset. Reverse all arcs to pair each switching class \(C\) with a distinct class \(C^{\rm rev}\).

**Theorem.** Every reversal-pair of tournament switching classes accounts for precisely
\[
\boxed{2^{n-1}}
\tag{EQ1}
\]
different all-zero compatible bridge families, independent of the coloring. There are \(2^{\binom n2-n}\) such class-pairs.

*Proof.* Vertex-star switches form a free group of size \(2^{n-1}\) modulo simultaneous switching of all vertices. Thus every switching class contains \(2^{n-1}\) tournaments. Global arc reversal cannot be achieved by a star switch when \(n\ge3\): it would require \(s_i+s_j=1\) for all pairs, impossible on any triple. Therefore each reversal-pair contains \(2^n\) tournaments.

The proved map \(T\mapsto W(T)\) obtained by independently complementing its reader rows according to their colors identifies precisely \(T\) and its global reversal, and no other pair. The normalized tournament of \(W(T)\) is star-switching-equivalent to \(T\), so it belongs to the same reversal-pair. Divide \(2^n\) by two to get (EQ1), and divide the total \(2^{\binom n2}\) tournaments by \(2^n\) to count class-pairs. \(\square\)

**Corollary.** Reversal-paired switching classes that contain a transitive tournament are indexed by unoriented cyclic orders of directions, numbering \((n-1)!/2\). Every such cyclic-order fiber contains \(2^{n-1}\) all-zero compatible families regardless of coloring.

*Proof.* Switching a transitive tournament preserves transitivity precisely when the switched subset is a prefix or suffix of its linear order. The resulting transitive tournaments are its cyclic rotations. Global reversal identifies reversal orientations of the same unoriented cyclic order. Apply (EQ1). \(\square\)

**Fixed-order Boolean normalization.** Choose an ordered direction sequence \(L=(i_1,\ldots,i_n)\), and let \(b_i(L)\) be the predecessor bit vector at site \(i\). Every tournament in its switching class has the form \(S_vL\) for a vertex switch vector \(v\in\mathbb F_2^n/\langle\mathbf1\rangle\). Define
\[
p_i(v)=\chi_i(b_i(L)+v|_{[n]\setminus\{i\}}).
\]
Then \(p_i\) is independent of bit \(v_i\) and satisfies \(p_i(\bar v)=1+p_i(v)\). The all-zero normalized tournament is
\[
\boxed{F_\chi(S_vL)=S_{p(v)}L.}\tag{EQ2}
\]
The bit \(p_i(v)\) is also the color at direction \(i\) along the full geodesic with root \(v\) and direction order \(L\). Consequently the normalized tournament is transitive if and only if this path's color word has at most one change.

*Proof.* In the switched input tournament \(S_vL\), the in-neighbor vector at site \(i\) is \(b_i(L)+v_i\mathbf1+v_{-i}\). Antipodal oddness gives its color \(s_i=v_i+p_i(v)\). Normalizing by the star vector \(s\) therefore produces \(S_{s+v}L=S_{p(v)}L\). The other assertions follow from the usual cube path bit update and the prefix/suffix characterization of transitivity after switching a linear order. \(\square\)

The fiber theorem shows the compatibility ensemble is uniformly distributed among *reversal-paired switching classes*, including many classes without transitive representatives. It does not assert that each transitive-eligible class contains a transitive all-zero family. NORI1 requires at least one of the \((n-1)!/2\) eligible fibers to contain such a family.



### Sharp Q4 multiplicity and global four-direction majority

**Theorem.** Every antipodally odd edge coloring of \(Q_4\) has at least four monochromatic-zero full antipodal geodesics. Equality holds precisely when every vertex has two edges of each color.

*Proof.* There are 24 projective Petrie cycles of order four, each with one or three switched comparisons. If \(Z\) have one switch, the total switch count is \(72-2Z\). Each antipodal incidence-turn comparison belongs to two Petrie cycles. Therefore, with \(r(v)\) the number of color-one edges incident to \(v\),
\[
72-2Z=\sum_{v\in Q_4}r(v)(4-r(v))\le16\cdot4=64.
\]
Hence \(Z\ge4\). Equality forces \(r(v)=2\) at every vertex, and this condition also suffices. Each one-switch cycle corresponds to a zero monochromatic full antipodal geodesic. \(\square\)

Sharpness: \(c_0=1+x_3,\ c_1=1+x_2,\ c_2=x_3,\ c_3=x_2\). Each of the pairs \((c_0,c_2)\), \((c_1,c_3)\) is complementary at every vertex, giving degree balance and four zero geodesics.

**Corollary (four-direction transitivity).** For any antipodally odd coloring of \(Q_n\), \(n\ge4\), any fixed four directions form a transitive subtournament with probability at least \(1/8\) in a uniformly sampled all-zero triangle-compatible bridge family.

*Proof.* The projective mixture theorem expresses this marginal as a mixture of uniform compatible-family distributions from odd colorings of \(Q_4\). Every such coloring has 32 compatible zero-row families and at least four transitive members. Therefore the probability is at least \(4/32\). The displayed coloring attains equality in dimension four. \(\square\)


## Simultaneous ascent from a facet-energy extremizer

Let n>=3 and c be an antipodally odd binary edge coloring. Index antipodal edge pairs by p, choose one direction-i edge from p with sign s_p=(-1)^{c(e)}, and let v_p have entry zero at i and entry (-1)^{x_j} at j!=i, where x is either endpoint of the chosen edge. Set w_p=s_pv_p; it is independent of which antipodal representative is chosen. Define
\[
B=\sum_pw_p,\qquad \mathcal E(c)=\|B\|^2,\qquad h_p=\langle B,w_p\rangle.
\]

**Theorem (multi-pair energy identity).** For every set S of antipodal edge pairs,
\[
\boxed{\mathcal E(c^{[S]})-\mathcal E(c)
=4\left(\left\|\sum_{p\in S}w_p\right\|^2-\sum_{p\in S}h_p\right).}
\tag{MA1}
\]
*Proof.* Flipping p changes its contribution to B from w_p to -w_p. Thus \(B(c^{[S]})=B(c)-2\sum_{p\in S}w_p\). Expanding its squared norm proves (MA1). \(\square\)

**Corollary (Boolean saturation of strict frustration).** Suppose c is bad and maximizes \(\mathcal E\) over all bad legal colorings of Q_n. Put
\[
F_-=\{p:h_p<0\},\qquad F_0=\{p:h_p=0\}.
\]
Every nonempty S subset F_- union F_0 which intersects F_- produces a good coloring c^[S]. In particular, every nonempty subset of F_- heals c. For n>=3, all h_p are even integers, so
\[
\boxed{\mathcal E(c^{[S]})-\mathcal E(c)\ge8|S\cap F_-|>0.}
\tag{MA2}
\]
The previously proved weak-threshold/positive-spanning theorem guarantees \(F_-\ne\varnothing\) whenever \(B\ne0\).

*Proof.* For p in F_- each h_p<=-2, and for p in F_0 each h_p=0. The squared norm in (MA1) is nonnegative, so the displayed gain follows. Maximality among bad colorings forces c^[S] to be good. The integrality and parity of h_p follow because each signed facet sum B_j contains \((n-1)2^{n-2}\) signs, an even number for n>=3. \(\square\)

**Corollary (zero-imbalance isolation and direction parity).** Suppose instead the same extremal bad coloring has B=0, and let S be a nonempty set of antipodal edge pairs. Any S with \(\sum_{p\in S}w_p\ne0\) heals c. If \(\sum_{p\in S}w_p=0\), writing \(m_i(S)\) for the number of S-pairs in direction i gives
\[
\boxed{m_i(S)\equiv |S|\pmod2\qquad\text{for every i}.}
\tag{MA3}
\]
Moreover, no nonempty S of size one or two has zero vector sum. Consequently:
- for all n>=4, every nonempty S of size at most three heals;
- for even n, every odd-cardinality S heals, regardless of its size;
- for odd n, every odd-cardinality S of size less than n heals.

*Proof.* With B=0, (MA1) equals \(4\|\sum_{p\in S}w_p\|^2\). For each fixed dimension i, the ith entry of w_p is zero when p has direction i and is +1 or -1 otherwise. Its sum has parity \(|S|-m_i(S)\), proving (MA3). A zero sum of two vectors would require \(w_p=-w_q\). Different directions have zeros in different entries; in one direction \(v_p=\pm v_q\) means the chosen edges are antipodal, hence p=q, excluded by S being a set. Thus no two distinct vectors cancel. A singleton is nonzero as well. For odd |S|, (MA3) demands m_i(S) odd for all i; this is impossible if n is even, and implies |S|>=n if n is odd. These observations prove all three statements. \(\square\)

The multi-pair identity applies to every coloring. Its two corollaries are global necessary constraints on an energy-maximizing counterexample, with no assumption on the edge-direction functions. The zero-imbalance case, in particular, would be isolated from other bad colorings throughout its radius-three orbit-flip Hamming ball in dimensions at least four. No incompatibility with the simultaneous-restoration path witnesses is presently established.



### Low-dimensional imbalance and switch identities

Let \(r(v)\) count color-one edges incident to vertex \(v\); let \(Z_s\) count projective Petrie cycles with \(s\) switched comparisons. As established, \(Z_1=N_0(c)\).

**Four-dimensional theorem.** For any antipodally odd coloring of \(Q_4\),
\[
\boxed{N_0(c)=4+\tfrac12\sum_{v\in Q_4}(r(v)-2)^2.}\tag{VI4}
\]
*Proof.* There are 24 projective Petrie cycles, with one or three switches each. The total switched-comparison count is \(72-2Z_1\). Every antipodal turn pair occurs twice among these cycles, so it is also
\(\sum_vr(v)(4-r(v))=64-\sum_v(r(v)-2)^2\). Equate and solve. \(\square\)

**Five-dimensional theorem.** For any antipodally odd coloring of \(Q_5\),
\[
\boxed{N_0(c)=Z_5+\tfrac32\sum_{v\in Q_5}
[6-r(v)(5-r(v))].}\tag{VI5}
\]
*Proof.* There are 192 projective Petrie cycles, with odd switch counts one, three, or five. The total is \(576-2Z_1+2Z_5\). Each antipodal turn pair occurs six times, so the same total is \(3\sum_vr(v)(5-r(v))\). Equating these yields (VI5). \(\square\)

**Consequences.** In dimension four, vertex-perfect balance minimizes \(N_0\) at four; imbalance strictly increases it. In dimension five, a hypothetical bad coloring must be balanced at every vertex, have no five-switch Petrie cycles, and hence have three switches on every Petrie cycle. These are global identities for all legal colorings, not locality statements.


## Edge extension and fault tolerance for weak weighted-majority colors

**Theorem (every weak-majority edge extends).** Let n>=3 and a_i>=0 not all zero. Put Phi(x)=sum_i a_i(-1)^(x_i), and give a direction-i edge e the color zero when its midpoint potential H(e)=(Phi(u)+Phi(v))/2 is positive, color one when H(e) is negative, and any antipodally odd tie color when H(e)=0. Then every zero edge lies on a monochromatic-zero full antipodal geodesic; likewise every one edge lies on a monochromatic-one full antipodal geodesic.

*Proof.* Start from a zero edge e of direction i, whose midpoint potential is nonnegative, and regard it as a path with used dimensions S={i}. Its endpoints u,v agree on all unused bits. Define H_S=(Phi(u)+Phi(v))/2=sum_(j notin S)a_j epsilon_j, where epsilon_j is their common bit sign. For any unused j, adding its edge at u or v gives midpoint potentials Phi(u)-a_j epsilon_j and Phi(v)-a_j epsilon_j, whose maximum is at least H_S-a_j epsilon_j. After the extension the new endpoint-average potential is H_S-a_j epsilon_j.

Choose a reserved unused dimension for the last extension: one with positive a_j epsilon_j if possible, otherwise one of weight zero if possible, otherwise any. Extend all other unused dimensions in this order: negative a_j epsilon_j, zero a_j, then positive a_j epsilon_j. During negative steps H_S>=0 and the maximal candidate midpoint exceeds H_S; removing negative signed weights makes H_S increase. During zero steps the maximal candidate midpoint is at least H_S, which is positive unless all unprocessed signed weights are zero. In the latter case H_S=0 implies all weights other than a_i were zero from the start; as the weights are not all zero, a_i>0 and the two endpoint potentials are +a_i and -a_i, so one zero-step candidate still has positive midpoint. During positive steps before the reserved final direction, H_S is the sum of remaining positive weights, including at least one other positive weight, and the best midpoint is strictly positive. Thus all nonfinal edges can be chosen color zero. When only one direction j remains, the two candidate j-edges at the path endpoints are antipodal mates, and one is color zero. Adding it yields a zero full geodesic through e. Antipodal complementation proves the color-one statement. QED.

**Corollary (single-direction tolerance).** Flipping any fewer than 2^(n-2) antipodal edge pairs contained in one direction preserves a monochromatic full antipodal geodesic: choose one of the 2^(n-2) unflipped zero edges in that direction, extend it as above, and note that the resulting path uses that direction only once.

**Corollary (unrestricted necessary frustration).** In any hypothetical bad odd coloring c with nonzero signed facet-imbalance vector B, let h_p=s_p sum_(j ne dir p)B_j(-1)^(x_j) be the alignment of each antipodal edge-pair sign with its B-weighted field, and put F={p:h_p<0}. Then F meets at least two directions, or |F|>=2^(n-2). In particular |F|>=2. Proof: reverse all strictly misaligned pairs to obtain an antipodally odd weak weighted-majority coloring with weights |B_j| and the same tie colors. If the reversal set lay within one direction with size less than 2^(n-2), the tolerance corollary would make the original c good, contradiction. The previously proved positive-spanning lemma guarantees F nonempty whenever c is bad and B!=0. QED.

The edge-extension property covers all edges of both colors, not merely one constructed full geodesic. The final corollary imposes an unrestricted necessary condition on every counterexample with B!=0; no restricted coloring hypothesis is imposed on c.


## Turn-moment edge-flip gradient and classification of stationary odd colorings

Let \(n\ge3\) and \(c\) be any antipodally odd coloring of \(Q_n\). Put \(s_i(x)=(-1)^{c_i(x)}\), independent of bit \(i\), \(r(x)=|\{i:s_i(x)=-1\}|\), and \(d(x)=\sum_i s_i(x)=n-2r(x)\). Let \(M=2^{n-2}(n-1)!\) be the number of projective Petrie cycles and \(S(c)\) their aggregate switched-comparison count. From the universal first-turn incidence identity,
\[
S(c)=\frac{(n-2)!}{2}\sum_{x\in Q_n}r(x)(n-r(x)).
\tag{TG1}
\]

**Theorem (one-pair turn-moment gradient).** Let \([e]\) be an antipodal edge pair in direction \(i\), represented by \(e=xx^i\), and put \(s=s_i(x)\). Then
\[
\boxed{S(c^{[e]})-S(c)
=2(n-2)![s(n-r(x)-r(x^i))-1]
=(n-2)![s(d(x)+d(x^i))-2].}
\tag{TG2}
\]
Moreover,
\[
\boxed{\sum_{[e]}[S(c^{[e]})-S(c)]
=2nM-4S(c).}
\tag{TG3}
\]

*Proof.* Inverting \([e]\) changes \(r(x),r(x^i)\) by \(s\) and changes the degrees at their antipodes by \(-s\). Antipodal oddness gives \(r(\bar x)=n-r(x)\). For \(q(t)=t(n-t)\), the difference \(q(t+s)-q(t)=s(n-2t)-1\). Therefore the change in \(\sum q(r)\) is \(4[s(n-r(x)-r(x^i))-1]\), proving (TG2).

Every switched comparison in a projective Petrie cycle compares two edge observations in distinct directions, hence depends on two different antipodal edge-pair variables. Flipping either one toggles that comparison. Summing the changes over all pair flips contributes \(2(1-2X)\) for each old switch indicator \(X\in\{0,1\}\). There are \(nM\) comparisons altogether, proving (TG3). \(\square\)

**Theorem (all locally stationary colorings).** Every pair-flip gradient in (TG2) vanishes if and only if \(n\) is even and
\[
\boxed{s_i(x)=\varepsilon_i(-1)^{\sum_{j\ne i}x_j}
\quad\text{for each }i,\qquad \varepsilon_i\in\{\pm1\}.}
\tag{TG4}
\]
For any coloring (TG4) and every permutation \(\pi=(i_1,\ldots,i_n)\), there is precisely one starting vertex whose full geodesic in order \(\pi\) has color zero throughout. Consequently
\[
\boxed{N_0(c)=n!/2}
\tag{TG5}
\]
for all stationary colorings. In odd dimension, no legal odd coloring has all pair-flip gradients zero.

*Proof.* If all gradients vanish, then for every \(x,i\),
\[
d(x)+d(x^i)=2s_i(x).
\tag{TG6}
\]
Summing over directions gives \(\sum_i d(x^i)=(2-n)d(x)\): the cube adjacency operator acts on \(d\) with eigenvalue \(2-n\). Its Walsh characters \(\chi_A(x)=(-1)^{\sum_{j\in A}x_j}\) have eigenvalues \(n-2|A|\), hence \(d\) has Walsh support entirely in degree \(n-1\). Formula (TG6) states \(s_i=\frac12(I+\mathrm{flip}_i)d\). This projection kills every character containing \(i\), retaining from degree \(n-1\) only the single character missing \(i\). As \(s_i\) is sign-valued, its surviving coefficient is \(\varepsilon_i\in\{\pm1\}\), proving (TG4). Antipodal oddness of (TG4) requires \(n-1\) odd, hence \(n\) even. Conversely for even \(n\), every displayed coloring satisfies (TG6), and all gradients vanish.

Write \(\varepsilon_i=(-1)^{b_i}\). Given a direction permutation \(\pi\), define \(R=\sum_i b_i+\binom n2\pmod2\) and the starting bits
\[
x_{i_k}=b_{i_k}+R+k-1\pmod2.
\]
Since \(n\) is even, \(\sum_i x_i=R\). The sign at the direction-\(i_k\) edge of the resulting geodesic is
\[
(-1)^{b_{i_k}+\sum_{j\ne i_k}x_j+(k-1)}=1.
\]
Conversely demanding all signs equal one forces these same starting bits, proving uniqueness. Every undirected geodesic has two orientations, so \(n!\) oriented zero geodesics give \(N_0=n!/2\). \(\square\)

**Interpretation.** The signed Hamming-weight-parity family suggested by the user is the entire stationary locus of the global Petrie first moment. It is not bad: each direction ordering supports a zero monochromatic geodesic. Thus any hypothetical bad coloring has at least one nonzero first-moment pair-flip gradient. The averaged drift (TG3) measures how far its turn moment lies above or below the random-color baseline \(nM/2\), providing a global extremal pivot criterion independent of special coloring subclasses.



## Middle-layer path design and spectral isolation of the parity stationary locus

Continue the preceding turn-moment stationary classification. Write \(n=2m\ge4\), and let \(\mathcal P\) be the family
\[
s_i(x)=\varepsilon_i(-1)^{\sum_{j\ne i}x_j},\qquad
\varepsilon_i=(-1)^{b_i}.
\]
There is one color-zero full antipodal geodesic for each direction order, giving \(n!/2\) unoriented geodesics.

**Theorem (middle-layer incidence design).** Fix \(c\in\mathcal P\), and put
\[
R_0=\sum_i b_i+\binom n2\pmod2,\qquad K_n=\binom{n-1}{m}.
\]
For each direction \(i\), the zero-colored direction-\(i\) edges appearing on any monochromatic-zero full geodesic have lower endpoints \(w_i\) characterized by
\[
\boxed{\left|\{j\ne i:w_i(j)+b_j+R_0=1\}\right|=m.}
\tag{PD1}
\]
All \(K_n\) such edges occur, and each lies on precisely \(n!/(2K_n)\) unoriented color-zero full antipodal geodesics.

*Proof.* Let \(\pi\) be a direction order, and let \(p_j\in\{1,\ldots,n\}\) be the position of direction \(j\). By the stationary classification, its unique all-zero starting root has bit \(x_j=b_j+R_0+p_j-1\). At the direction-\(i\) bridge, the other bits are
\[
w_i(j)=b_j+R_0+p_j-1+[p_j<p_i]\pmod2.
\]
Thus the adjusted bit in (PD1) is one if and only if \(p_j\) is odd and precedes \(p_i\), or is even and follows \(p_i\). If \(p_i=k\), these contribute \(\lfloor k/2\rfloor\) and \(m-\lfloor k/2\rfloor\) directions, totaling \(m\).

Conversely every \(m\)-subset of the remaining directions occurs as the adjusted one-set: put \(i\) first, assign those \(m\) labels to the even positions, and the remaining labels to the other odd positions. Permuting the remaining direction labels acts transitively on the \(K_n\) adjusted middle-layer vectors and preserves the number of orders yielding each vector. Since there are \(n!\) direction orders and every order has a unique zero starting root, each edge is used by \(n!/K_n\) oriented geodesics or \(n!/(2K_n)\) unoriented ones. \(\square\)

**Corollary (exponential perturbation tolerance in arbitrary directions).** If \(c\in\mathcal P\), and \(c'\) differs from \(c\) on fewer than
\[
\boxed{K_n=\binom{n-1}{n/2}}
\tag{PD2}
\]
antipodal edge pairs, then \(c'\) has a monochromatic-zero full antipodal geodesic. The edge-orbit transversal number of the original color-zero geodesic family of \(c\) is \(K_n\).

*Proof.* The \(n!\) oriented zero paths from the theorem each use \(n\) distinct edge orbits. Every orbit lies on at most \(n!/K_n\) of them. Recoloring fewer than \(K_n\) orbits cannot meet all \(n!\) paths by the union bound; an untouched path stays monochromatic zero. Conversely, all \(K_n\) supported zero edge orbits in any fixed direction meet every original zero path, proving the transversal number. This converse concerns destruction of the **original** path family, not necessarily all zero paths appearing after recoloring. \(\square\)

The theorem quantifies the user's parity-of-Hamming-weight example. Despite rapid color oscillations along some prescribed pole-to-pole paths, these colorings support an evenly spread middle-layer design of monochromatic full paths, robust against exponentially many arbitrary edge-orbit perturbations.

**Theorem (spectral rigidity of near-stationary turn gradients).** For any odd coloring \(c\) write
\[
h_i(x)=\frac{d(x)+d(x^i)}2-s_i(x),\qquad
\mathcal R(c)=\sum_{x,i}h_i(x)^2.
\tag{PD3}
\]
With \(\Delta_e S=S(c^{[e]})-S(c)\), one has
\[
\boxed{\sum_{[e]}(\Delta_e S)^2=(n-2)!^2\mathcal R(c).}
\tag{PD4}
\]
When \(n\) is even, some stationary parity coloring \(p\in\mathcal P\) differs from \(c\) on at most \(\mathcal R(c)/8\) antipodal edge pairs. Therefore every hypothetical bad coloring in even dimension obeys
\[
\boxed{\mathcal R(c)\ge8\binom{n-1}{n/2},
\qquad
\sum_{[e]}(\Delta_e S)^2
\ge8(n-2)!^2\binom{n-1}{n/2}.}
\tag{PD5}
\]
For odd \(n\), every legal coloring satisfies
\[
\boxed{\mathcal R(c)\ge n2^n.}
\tag{PD6}
\]

*Proof.* The flip formula (TG2) gives \(\Delta_eS=2(n-2)!\,s_i(x)h_i(x)\). Each antipodal edge orbit accounts for four \((x,i)\) instances with equal squared residual, proving (PD4).

For the Fourier bound, write the Walsh coefficient of \(s_i\) on \(A\subseteq[n]\) as \(a_{i,A}\), zero when \(i\in A\), and set \(A_A=\sum_{i\notin A}a_{i,A}\). For \(\ell=n-|A|\) missing directions, the residual's squared Fourier coefficients obey
\[
\sum_{i\notin A}(A_A-a_{i,A})^2
=\sum_{i\notin A}a_{i,A}^2+(\ell-2)A_A^2.
\tag{PD7}
\]
All \(s_i\) are antipodally odd, so \(A\) must have odd cardinality. For even \(n\), the top permissible degree is \(n-1\); its sole coefficient for direction \(i\) is
\(\alpha_i=\widehat{s_i}([n]\setminus\{i\})\), and its contribution to (PD7) vanishes. All other permissible \(A\) have \(\ell\ge3\). Parseval and (PD7) give
\[
\mathcal R(c)\ge2^n\sum_i(1-\alpha_i^2).
\]
Choose the parity signs \(\varepsilon_i\) to match \(\operatorname{sgn}\alpha_i\). The number of differing antipodal edge pairs is
\[
D=2^{n-3}\sum_i(1-|\alpha_i|)
\le 2^{n-3}\sum_i(1-\alpha_i^2)
\le\mathcal R(c)/8.
\]
The perturbation-tolerance corollary makes \(D\ge K_n\) for every bad coloring, proving (PD5).

For odd \(n\), degree \(n-1\) is even and hence forbidden by oddness. Every possible \(A\) has \(\ell\ge2\); (PD7) bounds the total residual energy below by \(2^n\sum_i\|s_i\|_2^2= n2^n\), proving (PD6). \(\square\)

These are unconditional, dimension-uniform structural inequalities for all hypothetical NORI1 counterexamples, obtained without specializing their edge colorings. They make the well-distributed stationary example a quantitatively isolated region of guaranteed-good colorings. Closure still requires controlling colorings far from every parity stationary state.



## General first-moment inversion and compulsory high-switch budget

For any antipodally odd coloring \(c\) of \(Q_n\), \(n\ge3\), let \(Z_{2j+1}\) count projective Petrie cycles having \(2j+1\) switched comparisons; only odd switch counts occur. Write
\[
M=2^{n-2}(n-1)!,\qquad
I(c)=\sum_{x\in Q_n}\left(r(x)-\frac n2\right)^2.
\]
Recall the universal turn-incidence identity \(S=\frac{(n-2)!}{2}\sum_x r(x)(n-r(x))\).

**Theorem (all-dimensional imbalance/high-switch identity).**
\[
\boxed{
N_0(c)=
2^{n-4}(n-2)!\,[6(n-1)-n^2]
+\frac{(n-2)!}{4}I(c)
+\sum_{\substack{j\ge2\\2j+1\le n}}(j-1)Z_{2j+1}.
}
\tag{HI1}
\]

*Proof.* Since every projective Petrie cycle has an odd number of switches,
\[
M=Z_1+Z_3+\sum_{j\ge2}Z_{2j+1},
\quad
S=Z_1+3Z_3+\sum_{j\ge2}(2j+1)Z_{2j+1}.
\]
Eliminating \(Z_3\) gives \(Z_1=(3M-S)/2+\sum_{j\ge2}(j-1)Z_{2j+1}\). By the one-switch/Petrie correspondence \(Z_1=N_0(c)\). Finally,
\[
\sum_xr(x)(n-r(x))=2^n\frac{n^2}{4}-I(c),
\]
and substitution yields (HI1). \(\square\)

**Corollary (high-switch necessity in any bad coloring).** If \(N_0(c)=0\), then
\[
\boxed{
\sum_{j\ge2}(j-1)Z_{2j+1}
=2^{n-4}(n-2)!\,[n^2-6(n-1)]
-\frac{(n-2)!}{4}I(c).
}
\tag{HI2}
\]
Thus every hypothetical counterexample must simultaneously obey an upper bound on vertex degree-imbalance energy and a prescribed positive amount of five-or-more-switch Petrie activity. The Q4 and Q5 formulas (VI4)--(VI5) are the first two instances of (HI1).

For a minimum-dimensional bad coloring the two sources of nonexistence must be combined: forcing extra color imbalance increases the positive term in (HI1), while suppressing high-switch cycles decreases its last term. The identity alone does not bound those competing terms sufficiently in large dimensions. Unlike a small-order enumeration, (HI1) applies uniformly in every dimension and is available for any future second-moment or extremal argument.

### Multiplicity of simultaneous critical repairs

Let c be an antipodally odd edge coloring of Q_n, and let F be a facet. Suppose D is a set of one-colored edges in F and for every e in D there exists a full dimension-simple antipodal geodesic P_e with e its unique one-colored edge, occurring strictly internally. Define a directed graph T on D by e->f if f differs from e and P_e traverses the antipodal mate of f. Since P_e contains its pivot e, a bridge perpendicular to F and at most n-2 edges in the opposite facet, the outdegree is at most n-2.

**Theorem (quantitative simultaneous repair).** Let c^S swap the colors of the antipodal edge pairs indexed by S subset D, and let Z(c^S) count unoriented all-zero full antipodal geodesics. Then
\[
\boxed{Z(c^S)\ge
|\{e\in S:N_T^+(e)\cap S=\varnothing\}|.}\tag{QR1}
\]
Consequently there is an independent set I in the undirected graph underlying T such that
\[
\boxed{|I|\ge\left\lceil\frac{|D|}{2n-3}\right\rceil,\qquad
Z(c^S)\ge|S|\text{ for every }S\subseteq I.}\tag{QR2}
\]
Thus all nonempty vertices of the Boolean recoloring face supported on I admit monochromatic full geodesics. A vertex corresponding to a k-element subset S has at least k distinct all-zero geodesics.

*Proof.* If e belongs to S and has no outgoing neighbor in S, its path P_e becomes all zero when the edge pair indexed by e is swapped: e is the unique initially one-colored edge on P_e, and P_e avoids the antipodal mate of every other swapped member f in S. Two such paths P_e are distinct, since the unique one-colored pivot in the original coloring is different. Counting them proves (QR1).

The underlying undirected graph has at most (n-2)|D| edges by summing the directed outdegrees. The elementary Turan or Caro--Wei bound gives an independent set of size at least |D|^2/(2(n-2)|D|+|D|)=|D|/(2n-3). Every e in any subset S of this independent set has no neighbor in S, so (QR1) yields (QR2). QED.

**Corollary (robustness in a neighboring Boolean face).** If S is a random subset of I obtained by including each element independently with probability 1/2, then
\[
\boxed{\mathbb E Z(c^S)\ge|I|/2,\qquad
\Pr[Z(c^S)\ge|I|/3]\ge1-e^{-|I|/36}.}\tag{QR3}
\]
Indeed Z(c^S)>=|S| and |S| has a binomial distribution. Applying the multiplicative Chernoff inequality with relative deficit one-third yields the displayed probability.

In particular, if c were a bad coloring selected to maximize facet imbalance, the established private internal repair theorem supplies D on a maximizing facet with
\[
|D|\ge 2^{n-2}+
\left\lceil\frac{2^{n-3}}{1+(n-1)(n-2)}\right\rceil.
\]
Thus the dimension of its neighboring Boolean face satisfies
\[
\boxed{|I|\ge\left\lceil
\frac{2^{n-2}+\lceil2^{n-3}/[1+(n-1)(n-2)]\rceil}{2n-3}
\right\rceil.}\tag{QR4}
\]
This multiplicity result strengthens the previously established independent-repair-face existence theorem: all selected private witnesses survive simultaneously, not just one. It is a necessary neighborhood condition on a hypothetical counterexample, not a proof that one cannot exist.


Parity stationary geodesic transversal theorem. In even dimension n=2m, each direction-i supported zero edge is indexed by an m-subset A of the other directions; for a direction permutation pi, A comprises labels in odd positions before i and even positions after i. Any two supported zero edges from different directions coexist on some zero antipodal geodesic. Construct the permutation for rows A at i and B at j: if i belongs to B, put i first, fill even positions by A, place j at position 2(m-|A intersect B|) if j in A or one later otherwise, then assign remaining labels to slots before/after j according to B. If i does not belong to B, choose h in A intersect B, put h first and i second, fill remaining even positions by A excluding h, and perform the same construction with intersection count reduced by one. All counts fit because both subsets have size m. Consequently every minimum path transversal of size K=binomial(n-1,m) is precisely the entire supported set of edges in one direction. Proof: each supported edge appears on the same number of paths, so a size-K hitting set must meet each path once; two chosen edges in different directions would occur together on a path. Any arbitrary recoloring restricted to one direction of a stationary parity coloring remains good, because the unaffected normal facet is antipodally even and has a paired nondecreasing favorable root; whichever antipodal bridge is zero gives a zero geodesic. Hence any hypothetical bad legal coloring has distance at least K+1 from every stationary parity coloring, strengthening the spectral residual necessary condition to R>=8(K+1).

Global parity foliation theorem. Let n be even and P range over all unoriented full antipodal geodesics of Q_n. For each sign vector epsilon in {+-1}^n, let p_epsilon be the legal stationary parity coloring s_i(x)=epsilon_i times (-1) to the sum of bits outside direction i. Every full geodesic P is monochromatic zero in one and only one p_epsilon: it traverses one edge in each direction, so each edge's zero requirement uniquely determines the sign epsilon_i. Therefore the 2^n stationary parity zero-path families partition all 2^(n-1) n! unoriented full geodesics into equal classes of n!/2 paths. For any legal odd coloring c define the discrepancy set F_epsilon of antipodal edge orbits where c differs from p_epsilon. Then the number N0(c) of zero geodesics equals the sum over epsilon of the number of p_epsilon-zero geodesics avoiding F_epsilon. Thus badness is equivalent to F_epsilon meeting every zero geodesic in every parity family simultaneously. These transversals are strongly coupled: toggling one parity sign epsilon_i complements all direction-i orbit memberships and leaves every other direction untouched, so F_epsilon xor F_epsilon-flipped-i equals the full set M_i of 2^(n-2) direction-i orbits. The previous minimum-transversal rigidity makes every individual discrepancy set of a bad coloring have size at least binomial(n-1,n/2)+1. The remaining all-dimensional closure task is to prove that this correlated Boolean cube of discrepancy transversals cannot exist, rather than trying to bound a single transversal independently.

## Complementary monochromatic arms and locally obstructed critical flips

Let \(c\) be a legal antipodally odd edge coloring of \(Q_n\), \(n\ge3\), with no monochromatic full antipodal geodesic. For a vertex \(u\), color \(b\), and a direction \(i\), define \(\mathcal R_b(u;i)\) to be the family of subsets \(S\subseteq[n]\setminus\{i\}\) for which there is a monochromatic color-\(b\) geodesic starting at \(u\) and traversing precisely the directions in \(S\) once each.

**Theorem (critical-pair complementary-arm criterion).** Let \(e=uv\) have direction \(i\) and original color \(1-b\). Flipping its antipodal pair \(\{e,\bar e\}\) produces a monochromatic full antipodal geodesic if and only if there is a nonempty proper subset \(S\subset[n]\setminus\{i\}\) such that
\[
\boxed{S\in\mathcal R_b(u;i),\qquad
([n]\setminus(\{i\}\cup S))\in\mathcal R_b(v;i).}
\tag{CA1}
\]

*Proof.* Since \(c\) is bad, any monochromatic full geodesic after the flip must traverse one of \(e,\bar e\). If it uses \(\bar e\), apply antipodal complementation: the resulting geodesic traverses \(e\) and has color \(b\), since the post-flip coloring remains antipodally odd. Thus it suffices to consider a monochromatic color-\(b\) full path through \(e\). Split at \(e\). The two remaining arms are monochromatic color \(b\) already in \(c\), have disjoint sets of traversed directions, and together use every direction other than \(i\), proving (CA1). Their direction sets are both nonempty: if either arm were empty, the original coloring would have a full antipodal geodesic with at most one switch, contradicting badness by the established root-slide lemma.

Conversely, take the two arms asserted by (CA1), reverse the first one, traverse \(e\), and follow the second. Since the arms use complementary direction sets and both avoid \(i\), the concatenated path traverses all \(n\) directions once. Its endpoints are antipodal. After flipping \(e,\bar e\), every edge on this path has color \(b\). \(\square\)

For a direction-\(i\) edge \(e=uv\) of color \(1-b\), let \(D_b(u;e)\subseteq[n]\setminus\{i\}\) be the directions of color-\(b\) edges incident with \(u\), and similarly at \(v\).

**Corollary (two-sided local Hall obstruction).** If
\[
\boxed{\nexists\ j\in D_b(u;e),\ k\in D_b(v;e)\quad\text{with }j\ne k,}
\tag{CA2}
\]
then the antipodal pair of \(e\) is nonhealing. In particular, every edge incident to a monochromatic vertex is nonhealing; the same holds when the opposite-colored neighbors at both endpoints occur in a common single direction and no other opposite-colored neighbors exist.

*Proof.* Under (CA1), the first edge of the \(u\)-arm and the first edge of the \(v\)-arm have distinct directions, since their direction sets are disjoint and nonempty. They belong to the respective sets in (CA2). \(\square\)

**Corollary (monochromatic vertices force nonhealing pairs).** Let \(M(c)\) be the set of cube vertices whose incident \(n\) edges all have the same color. Then the number of nonhealing antipodal edge pairs is at least
\[
\boxed{\left\lceil\frac{n|M(c)|}{4}\right\rceil.}
\tag{CA3}
\]
Whenever \(M(c)\) is nonempty, there are at least \(n\) such pairs.

*Proof.* The set \(M(c)\) is closed under antipodal complementation. Every edge incident with any vertex in \(M(c)\) is nonhealing by (CA2). In the projective vertex/edge-orbit incidence graph, each antipodal vertex pair represented by \(M(c)\) contributes \(n\) incidences, and an antipodal edge pair has at most two projective endpoints. Thus there are at least \(n(|M(c)|/2)/2\) nonhealing edge-pair orbits. A fixed monochromatic vertex itself contributes \(n\) distinct incident edge-pair orbits. \(\square\)

**Corollary (unrestricted energy-extremal obstruction).** Choose any bad coloring maximizing the facet-imbalance energy \(\mathcal E=\sum_jB_j^2\) among bad colorings, and put \(h_p=\langle B,w_p\rangle\) as previously. Every pair failing (CA2)'s local Hall condition must obey
\[
\boxed{h_p\ge n-1.}
\tag{CA4}
\]
If \(B=0\), then no pair fails (CA2), and every vertex sees both colors.

*Proof.* Such a pair is nonhealing, hence its flip remains bad. Energy maximality gives \(\mathcal E(c^{[p]})-\mathcal E(c)\le0\). Apply the proved flip identity \(4[(n-1)-h_p]\). For \(B=0\), all h_p vanish, contradicting (CA4) at a locally obstructed pair. \(\square\)

The criterion (CA1) is a restatement of restoration criticality in complementary direction-set geometry, and (CA2)--(CA4) sharpen the necessary local structure of an unrestricted extremal bad coloring. They do **not** exclude balanced mixed-vertex colorings and do not settle NORI1. The closure issue is to show that the complementary-arm constraints for **all** antipodal edge pairs cannot hold simultaneously when every full geodesic is bichromatic.


Bridge-selector invariance. Under antipodally even lower-facet coloring, favorable-root weights agree at antipodal roots. Hence the bridge sum for monochromatic full paths is unchanged by every legal bridge flip. For a stationary parity coloring in even dimension, recoloring any number of edge pairs in one direction preserves its full zero path count n factorial divided by two.

Fourier geodesic multiplicity. Sharp unrestricted Fourier lower bound on monochromatic path multiplicity. Let n even, K=binomial(n-1,n/2), and c any legal odd coloring. For each direction i let alpha_i be the Walsh coefficient of its signed edge-color function on the full set of other n-1 directions. For stationary parity sign vector epsilon in plus-minus-one to the n, its antipodal edge-pair distance D(epsilon) from c equals 2^(n-3) times (n minus sum_i epsilon_i alpha_i). Each stationary coloring has n!/2 zero full paths, and each supported edge orbit belongs to n!/(2K) of them. The elementary union bound leaves at least n!/2 times positive-part(1-D(epsilon)/K) stationary zero paths surviving all discrepancies. The parity foliation theorem makes these surviving paths disjoint as epsilon varies. Thus N0(c) is at least n!/2 times the sum over all epsilon of positive-part(1-D(epsilon)/K). Equality holds at every stationary parity coloring: its own term is one, all other terms vanish since changing a parity sign differs on 2^(n-2)>K edge-pair orbits. This quantitative lower bound applies to every legal coloring and is sharper than using only the nearest stationary parity reference.


### Two-scale robustness and distributed Fourier obstruction

Let \(n=2m\ge4\), \(K=\binom{n-1}{m}\), and \(p\) a stationary parity coloring. Fix one direction \(i\). Let \(q\) be obtained from \(p\) by arbitrary recolorings of antipodal edge pairs in direction \(i\), with no changes to other directions. Let \(M=n!/2\).

**Theorem (uniform incidence envelope).** The coloring \(q\) has \(N_0(q)=M\). For any antipodal edge orbit \([e]\) in a different direction \(j\ne i\), at most \(2M/K\) of these zero geodesics traverse \([e]\).

*Proof.* The count is conserved by the preceding antipodally-even facet bridge-selector theorem. Let \(p^{(i)}\) be the stationary parity coloring obtained by reversing *all* direction-\(i\) edge pairs of \(p\). The horizontal facet colorings of \(p,q,p^{(i)}\) are the same. For any lower-facet antipodal bridge-root pair, the selector of \(q\) chooses either the zero bridge of \(p\) or that of \(p^{(i)}\). The corresponding fan of zero full geodesics therefore agrees with the fan in one of those two stationary colorings. Consequently
\[
\mathcal G_0(q)\subseteq\mathcal G_0(p)\cup\mathcal G_0(p^{(i)}).
\]
Each stationary family has \(M\) paths and each orbit in direction \(j\) lies on at most \(M/K\) of them, by the proved middle-layer design theorem. The bound \(2M/K\) follows. \(\square\)

**Corollary (large arbitrary changes in one direction).** After the arbitrary direction-\(i\) recolorings above, change an additional \(t\) antipodal edge pairs in *any other directions*. The resulting coloring \(c\) satisfies
\[
\boxed{N_0(c)\ge M\left(1-\frac{2t}{K}\right)_+.}
\tag{DR1}
\]
In particular it is good whenever \(t<K/2\), regardless of how many direction-\(i\) pairs were changed.

*Proof.* Each additional orbit flip can destroy at most \(2M/K\) paths of the zero family of \(q\). Apply the union bound to all \(t\) changes. \(\square\)

**Corollary (unrestricted distributed nonstationarity).** If \(c\) is a hypothetical bad legal coloring of even-dimensional \(Q_n\), let
\(\alpha_j=\widehat{s_j}([n]\setminus\{j\})\) be its highest admissible Walsh coefficients. Then for **every** direction \(i\),
\[
\boxed{
\sum_{j\ne i}(1-|\alpha_j|)
\ \ge\ \frac{K}{2^{n-2}}.
}
\tag{DR2}
\]

*Proof.* For any stationary parity reference \(p\), write \(D_j(p,c)\) for the number of mismatching direction-\(j\) antipodal edge pairs. If \(\sum_{j\ne i}D_j(p,c)<K/2\), the two-scale robustness theorem makes \(c\) good, contradiction. Choose the reference sign in every direction to minimize its mismatches, giving \(D_j=2^{n-3}(1-|\alpha_j|)\). Substitution yields (DR2). \(\square\)

This applies to all hypothetical NORI1 counterexamples, not a restricted coloring class: the only use of the stationary reference is to quantify the distribution of the arbitrary coloring's parity discrepancy across directions. It complements the total residual gap (PD5) by preventing the highest-order spectral defect from concentrating in any single direction. The constant factor two is an incidence envelope, not a claim of invariance of individual path signatures.


## Even-dimensional equivariant parity-transversal reduction

Write \(Q_{n+1}=Q_n\times Q_1\). A bad antipodally odd coloring c of Q_n extends to a bad coloring c' of Q_(n+1): use c unchanged in each horizontal facet, and color the new-direction edges by any bit function b(x) satisfying b(bar x)=1-b(x). Every monochromatic full geodesic of c' would project, after deleting its one new-direction step, to a monochromatic full geodesic of c. Thus proving NORI1 in all even dimensions suffices for every dimension.

**Theorem (even-dimensional parity-transversal equivalence).** Let n be even and let O be the antipodal edge-pair orbits. Let M_i subset O be the orbits in direction i, and let p_0 be the stationary parity coloring with
\[
p_{0,i}(x)=\sum_{j\ne i}x_j\pmod2.
\]
For each a in F_2^n put \(p_{a,i}=p_{0,i}+a_i\), and let P_a be the set of its monochromatic-zero full antipodal geodesics. For every a define
\[
\boxed{t_i(a)=a_i+\sum_j a_j\pmod2.}\tag{ET1}
\]
Then \(P_a=t(a)+P_0\). Given any legal coloring c, define its difference-orbit set \(F=\{[e]:c(e)\ne p_0(e)\}\). Then c is bad if and only if every set
\[
\boxed{F_a=F\mathbin{\triangle}\bigcup_{i:a_i=1}M_i}\tag{ET2}
\]
meets every full geodesic in \(t(a)+P_0\). Consequently NORI1 in all dimensions is equivalent to excluding such a simultaneous family of transversals F_a for all even n.

*Proof.* Since n is even, the linear map \(t\mapsto(\sum_{j\ne i}t_j)_i\) is invertible: if its output is a, summing a gives \(\sum_jt_j\), so inversion gives (ET1). Translating a direction-i edge by t changes its parity coloring by \(\sum_{j\ne i}t_j=a_i\). Thus t translates the full zero-geodesic family P_0 onto P_a. Replacing p_0 by p_a complements the edge signs precisely on M_i for directions with a_i=1, giving (ET2). A full geodesic zero under p_a remains zero under c if and only if none of its edges lies in the corresponding mismatch-orbit set F_a. This proves the equivalence in even dimensions. The lifting construction in the opening paragraph proves the equivalence with unrestricted NORI1. QED.

The reduction preserves dimension-simplicity and the antipodal involution. It isolates a global combinatorial closure target: the 2^n coupled discrepancy transversals, linked by whole-direction complementation and hypercube translation, must be incompatible. Individual transversal-size bounds do not by themselves rule them out.



## Sharp incidence envelope after arbitrary one-direction parity recoloring

Let \(n=2m\ge4\), \(K=\binom{n-1}{m}\), \(M=n!/2\), and let \(p\) be any stationary parity coloring of \(Q_n\). Fix a direction \(i\). Let \(q\) be obtained from \(p\) by changing an arbitrary collection of antipodal edge pairs of direction \(i\) and none in other directions.

**Theorem (sharp exterior edge-orbit incidence).** Every antipodal edge orbit \([e]\) in direction \(j\ne i\) belongs to at most
\[
\boxed{\left(\frac32-\frac1n\right)\frac{M}{K}}
\tag{SE1}
\]
monochromatic-zero antipodal full geodesics of \(q\). The bound is attained, for each distinct \(i,j\), by some choice of changed direction-\(i\) pairs and of the exterior orbit \([e]\). All such \(q\) have \(N_0(q)=M\).

*Proof.* The path-count conservation law gives \(N_0(q)=M\). Let \(p^{(i)}\) be the stationary coloring obtained by changing every pair in direction \(i\). In each antipodal direction-\(i\) bridge pair the zero selector of \(q\) chooses independently the selector of \(p\) or that of \(p^{(i)}\). If a direction-\(j\) edge orbit lies in the support of only one of these stationary zero-path families, it occurs on at most \(M/K\) zero paths of \(q\); if in neither, on none. We calculate the maximum when it belongs to both.

Use the stationary middle-layer labeling: for each direction permutation \(\pi\) let \(A_\ell(\pi)\subset[n]\setminus\{\ell\}\) be the \(m\)-set of directions in odd positions preceding \(\ell\) or even positions following \(\ell\). The zero full geodesic determined by \(\pi\) traverses the direction-\(\ell\) orbit labeled by \(A_\ell(\pi)\), and every unoriented path has two direction-permutation descriptions.

An external \(j\)-orbit common to both supports is represented in \(p\) by an \(m\)-set \(A=\{i\}\cup U\), \(|U|=m-1\), and in \(p^{(i)}\) (via facet antipodal reflection to the \(p\) family) by \(B=\{i\}\cup V\), where \(U,V\) partition the other \(n-2\) directions and both have size \(m-1\). The \(K\) supported \(i\)-orbits are labeled by \(m\)-sets \(C\subset[n]\setminus\{i\}\), the same orbits for both stationary colorings.

Let \(G(A,C)\) count permutations with \(A_j(\pi)=A\) and \(A_i(\pi)=C\). Put \(\delta=[j\in C]\), \(a=|C\cap U|\). The directions strictly between \(i,j\) along such a permutation form the set
\[
H=U\mathbin{\triangle}(C\setminus\{j\}),
\quad
k=|H|=2m-1-\delta-2a.
\tag{SE2}
\]
Among these \(k\) labels, \(\lfloor k/2\rfloor\) belong to \(U\), and \(\lceil k/2\rceil\) to \(V\). Conversely, any ordering with this interval set and the parity conditions yields the requested two labels. Counting possible positions of \(i,j\) and then permutations within the four membership/interval groups gives
\[
\begin{aligned}
g(2t)&=2(m-t)(t!)^2((m-1-t)!)^2,\\
g(2t+1)&=2(t+1)(t!)^2((m-1-t)!)^2,
\end{aligned}
\tag{SE3}
\]
where \(G(A,C)=g(k)\). Indeed, for even \(k=2t\) the allowed ordered position pairs number \(2(m-t)\) and the four groups have sizes \(t,t,m-1-t,m-1-t\); for odd \(k=2t+1\) the allowed position pairs number \(2(m-t-1)\) and the groups have sizes \(t,t+1,m-1-t,m-2-t\).

For the partner label \(B\), the intervening set is complementary to \(H\) within the \(n-2\) remaining directions, hence \(G(B,C)=g(n-2-k)\). To maximize the number of selected zero paths through \([e]\), independently choose for each \(i\)-orbit \(C\) the bridge selector contributing the larger of these two counts. Thus the maximal *oriented* incidence is
\[
\sum_C \max(G(A,C),G(B,C)).
\]
If \(j\in C\), then \(a\in\{0,\ldots,m-1\}\), with
\(\binom{m-1}a^2\) possibilities for \(C\). Substitution into (SE3) makes this group's contribution
\(2((m-1)!)^2\max(a+1,m-a)\).
If \(j\notin C\), then \(a\in\{1,\ldots,m-1\}\), with
\(\binom{m-1}a\binom{m-1}{a-1}\) possibilities, contributing
\(2((m-1)!)^2\max(a,m-a)\).
Summing gives
\[
\begin{split}
&2((m-1)!)^2\left[
\sum_{a=0}^{m-1}\max(a+1,m-a)
+\sum_{a=1}^{m-1}\max(a,m-a)\right]\\
&\hspace{10mm}=(3m^2-m)((m-1)!)^2.
\end{split}
\]
Every supported external orbit occurs on \(n!/K=2m^2((m-1)!)^2\) oriented paths in its stationary family. Their ratio is
\((3m-1)/(2m)=3/2-1/n\).
Passing to unoriented paths divides numerator and denominator by two and proves (SE1). Choosing each bridge selector to maximize its local contribution gives equality. \(\square\)

**Corollary (improved two-scale robustness).** After arbitrary direction-\(i\) pair recolorings of a stationary parity coloring, reverse an additional \(t\) pairs in other directions. The final legal coloring \(c\) satisfies
\[
\boxed{N_0(c)\ge\frac{n!}{2}
\left(1-\frac{(3/2-1/n)t}{K}\right)_+.}
\tag{SE4}
\]
Consequently a hypothetical bad coloring must have, outside each chosen direction, at least
\(K/(3/2-1/n)\) discrepant edge pairs relative to every stationary reference.

**Corollary (strengthened unrestricted distributed spectral obstruction).**
For any hypothetical bad coloring in even dimension,
\[
\boxed{
\sum_{j\ne i}(1-|\alpha_j|)
\ge
\frac{4n}{3n-2}\,
\frac{\binom{n-1}{n/2}}{2^{n-2}}
\quad\text{for every }i.}
\tag{SE5}
\]
*Proof of corollaries.* At most \((3/2-1/n)M/K\) zero paths are destroyed by each additional edge-pair reversal; apply the union bound. For the spectral statement choose stationary signs minimizing the number
\(2^{n-3}(1-|\alpha_j|)\) of mismatching edge orbits in direction \(j\), and rearrange the necessary edge-count inequality. \(\square\)

The coefficient in the exterior-edge incidence theorem is sharp for each even dimension, and improves the previous factor two. No locality or special-form hypothesis is placed on a hypothetical bad coloring; the stationary family is used only as a universal comparison.

## Counterexample-preserving balance and finite-order pseudorandom padding

Write an antipodally odd cube-edge coloring as functions c_i(x) in {0,1}, independent of bit x_i, satisfying c_i(bar x)=1-c_i(x). A coloring is *bad* if no monochromatic dimension-simple geodesic joins antipodal vertices.

**Theorem (perfect-balance lift).** Every legal coloring c of Q_n has a legal lift B(c) on Q_(2n), given by
\[
\boxed{B(c)_i(x,y)=c_i(x),\qquad B(c)_{n+i}(x,y)=1-c_i(x).}\tag{BL1}
\]
At each vertex the two incident-color degrees both equal n. A monochromatic full geodesic of B(c) projects, by deleting its y-direction steps, to a monochromatic full geodesic of c. Consequently c bad implies B(c) bad, and unrestricted NORI1 is equivalent to its restriction to legal edge colorings of even-dimensional cubes which are perfectly balanced at every vertex.

*Proof.* Each rule ignores its own direction bit. Under full antipodal complementation both types of colors reverse, as c is odd. Each pair of directions i,n+i has complementary incident colors. Projecting a full lifted geodesic onto the first n bits deletes each y step and leaves each old direction once; the remaining colors agree with those in c. Hence a monochromatic lifted path would produce one in c. QED.

### Defect-preserving perfect-balance lift and simultaneous first-excess reduction

Recall the perfect-balance lift \(B(c)\) of (BL1): for \(c\) on \(Q_n\), \(B(c)_i(x,y)=c_i(x)\) and \(B(c)_{n+i}(x,y)=1-c_i(x)\). For each legal antipodally odd coloring \(c\), let \(r(c)\) be the minimum number of color-one edges on a full antipodal geodesic. Write \(g_k(c;x)\) for the number of oriented full antipodal geodesics starting at \(x\) and having \(k\) color-one edges, and set \(d(x)=|\{i:c_i(x)=1\}|\).

**Theorem (defect-preserving balanced doubling).** For all legal \(c\) and all \(0\le k\le n\),
\[
\boxed{r(B(c))=r(c),}\tag{BL5}
\]
\[
\boxed{g_k(B(c))\ge 2^n\sum_{x\in Q_n}d(x)!(n-d(x))!g_k(c;x).}\tag{BL6}
\]
In particular, every full antipodal geodesic of \(c\) extends to a full antipodal geodesic of \(B(c)\) with the same number of color-one edges.

*Proof.* Let \(P\) be any full antipodal geodesic in \(c\), starting at \(x\) and ending at \(\bar x\), and put \(J=\{i:c_i(x)=1\}\). Start at any \((x,y)\) in \(Q_{2n}\). First traverse all auxiliary directions \(n+i\) with \(i\in J\), in arbitrary order. Their colors are zero because \(B(c)_{n+i}(x,y')=1-c_i(x)=0\). Next traverse all old directions following \(P\), with no auxiliary changes. Their colors reproduce those of \(P\). Finally traverse auxiliary directions \(n+i\) for \(i\notin J\), in arbitrary order. Their colors are zero since \(B(c)_{n+i}(\bar x,y')=1-c_i(\bar x)=c_i(x)=0\). This traverses every direction once and joins \((x,y)\) to \((\bar x,\bar y)\), without introducing color-one edges. Each root \(y\) and pair of auxiliary-block orderings give distinct oriented extensions. There are \(2^n |J|!(n-|J|)!\) such extensions per original rooted geodesic; distinct old geodesics have distinct projections. Summing over \(x\) gives (BL6).

Conversely, project any full antipodal geodesic of \(B(c)\) to the \(x\)-bits and delete its auxiliary steps. The result is a full antipodal geodesic in \(c\), and all its color-one edges remain color one in the lifted path. Therefore \(r(B(c))\ge r(c)\). The constructed extension of a minimizing old path gives the opposite inequality, proving (BL5). \(\square\)

**Corollary (balanced first-excess branch is universally sufficient).** Unrestricted NORI1 is equivalent to the following assertion: every vertex-balanced antipodally odd coloring of any even-dimensional cube that has a full antipodal geodesic with precisely one color-one edge also has a monochromatic full antipodal geodesic.

Indeed, a hypothetical unrestricted counterexample yields, by the established first-excess reduction, a bad legal \(c\) with \(r(c)=1\). The coloring \(B(c)\) is vertex-balanced by (BL1), and (BL5) gives \(r(B(c))=1\), hence it is a balanced bad coloring retaining a one-defect full geodesic. The converse is immediate. This also establishes equivalence when the balanced class is restricted to lifts of form (BL1), provided the one-defect condition is imposed.

**Corollary (noise-trace endpoint multiplicity survives balancing).** For the established deformation \(F_c(t)=\operatorname{tr}(P_n((A_n+t(2R_c-A_n))/2)^n)\), the noise-trace distance theorem gives
\[
\boxed{\operatorname{ord}_{t=1}F_{B(c)}(t)=\operatorname{ord}_{t=1}F_c(t)=r(c).}\tag{BL7}
\]
Thus the established perfect-balance reduction simultaneously preserves the number of defects required to make a full antipodal geodesic monochromatic. It places the balanced Boolean matrix constraints and first-excess obstruction on one hypothetical counterexample; excluding the latter configuration remains open.

**Theorem (balanced lift with arbitrarily high fixed-order marginal independence).** Fix n>=2, t>=1, and any legal coloring c on Q_n. For every k>=2 define a coloring C_k(c) on Q_N, N=2n+2k, with bits (x_1,...,x_n,y_1,...,y_n,a_1,...,a_k,b_1,...,b_k): use (BL1) in the first 2n directions and, cyclically for j=1,...,k, set
\[
\boxed{C_{a_j}(x,y,a,b)=a_{j+1},\qquad C_{b_j}(x,y,a,b)=1-a_{j+1}.}\tag{BL2}
\]
The notation a_(k+1)=a_1 is used. Then C_k(c) is legal, balanced at every vertex, and preserves badness by projection onto x. Moreover, at least
\[
\boxed{\frac{2^t\binom kt}{\binom{2n+2k}t}}\tag{BL3}
\]
of all t-element subsets of directions have *mutually independent fair* incident edge colors when the cube vertex is chosen uniformly. The fraction tends to 1 for fixed n,t as k grows. All direction pairs except the k complementary gadget pairs and the at most binom(2n,2) pairs within the old/compensator block have normalized Hamming distance 1/2.

*Proof.* The gadget rule in direction a_j reads only bit a_(j+1), distinct from a_j because k>=2; the rule in direction b_j ignores b_j. Every gadget function changes color under antipodal complementation. Each gadget pair has opposite incident colors, giving perfect local balance together with (BL1). Projecting a monochromatic full path onto the x directions would make a monochromatic full path in c, proving badness preservation.

The common color source of gadget pair j is the uniform bit a_(j+1). Distinct gadget pairs read different source bits, which are independent. Thus choosing one of two directions from each of t distinct gadget pairs gives independent uniform incident colors. There are 2^t binom(k,t) such choices out of binom(N,t) choices. Every gadget color is also independent of the old and compensator colors, which are functions only of x, giving the pairwise statement. QED.

**Corollary (equivalent balanced pseudorandom closure branch).** For every fixed t and every epsilon>0, NORI1 for all legal colorings with equal incident degrees at every vertex and at least a proportion 1-epsilon of t-subsets of directions showing independent fair incident colors would imply unrestricted NORI1. Indeed, a bad coloring could be lifted by (BL2) into this class for all sufficiently large k. The converse is immediate.

For an arbitrary perfectly balanced coloring of Q_N, let s_i(v)=(-1)^{c_i(v)}. Since sum_i s_i(v)=0 pointwise,
\[
\boxed{\sum_{i<j}\mathbb E_v[s_i(v)s_j(v)]=-N/2.}\tag{BL4}
\]
Every correlation is at least -1; therefore no balanced coloring can have fewer than N/2 direction pairs with nonzero correlation. The lifted C_k(c) has at most N/2+O(n^2) potentially correlated pairs, asymptotically attaining this necessary number as k tends to infinity for fixed n.

By the unrestricted mean-switch identity, every balanced lift has expected switch count N/2, its maximal value. Thus neither maximal mean switching nor independence on almost every fixed-size family of incident directions, in isolation, distinguishes universally good colorings from possible balanced bad extensions. The conjecture still requires geometric compatibility of complete dimension-simple paths.



### Sparse exterior support and localized obstruction for arbitrary counterexamples

Retain even \(n=2m\ge4\), \(K=\binom{n-1}{m}\), a stationary parity coloring \(p\), and a distinguished direction \(i\). Let \(p^{(i)}\) reverse all its direction-\(i\) edge pairs. For \(j\ne i\), let \(\mathcal L_j(p)\) and \(\mathcal L_j(p^{(i)})\) be their supported direction-\(j\) antipodal edge orbits in monochromatic-zero full paths. Put
\[
\mathcal U_{i,j}(p)=\mathcal L_j(p)\cup\mathcal L_j(p^{(i)}).
\]

**Theorem (support intersection count).** For every \(j\ne i\),
\[
\boxed{
|\mathcal L_j(p)\cap\mathcal L_j(p^{(i)})|
=\binom{n-2}{m-1},
\qquad
|\mathcal U_{i,j}(p)|
=2K-\binom{n-2}{m-1}.}
\tag{SU1}
\]
In particular,
\[
\boxed{
2^{n-2}-2K+\binom{n-2}{m-1}
}
\]
direction-\(j\) edge orbits are absent from *every* zero geodesic of every legal coloring obtained by arbitrary changes to \(p\) confined to direction \(i\).

*Proof.* The middle-layer representation of the stationary path design assigns every supported orbit in direction \(j\) a unique \(m\)-subset \(A\subset[n]\setminus\{j\}\). Translating from \(p\) to \(p^{(i)}\) reflects all bits outside \(i\); modulo antipodal edge identification, this toggles the \(i\)-th bit of the direction-\(j\) orbit. The toggled row has adjusted weight \(m-1\), whose complement represents a supported orbit, precisely when \(i\in A\). Thus the common supported orbits correspond to the \(m\)-subsets containing \(i\), numbering \(\binom{n-2}{m-1}\). Inclusion-exclusion proves (SU1). Every zero path after a direction-\(i\) selector change belongs to one of the two stationary zero-path families by the bridge-fan decomposition, so outside their union no orbit can be traversed. \(\square\)

**Corollary (localized sharp robustness).** Let \(c\) be any legal antipodally odd coloring, and let \(q\) be the coloring obtained from the stationary reference \(p\) by giving it precisely \(c\)'s direction-\(i\) edge colors while retaining \(p\) elsewhere. Define
\[
t_{\mathrm{active}}(c;p,i)=
\sum_{j\ne i}
|\{[e]\in\mathcal U_{i,j}(p):c(e)\ne p(e)\}|.
\]
Then
\[
\boxed{
N_0(c)\ge\frac{n!}{2}
\left(1-\frac{(3/2-1/n)t_{\mathrm{active}}(c;p,i)}K\right)_+.
}
\tag{SU2}
\]
Consequently a hypothetical bad coloring must satisfy
\[
\boxed{
t_{\mathrm{active}}(c;p,i)\ge
\left\lceil\frac{K}{3/2-1/n}\right\rceil
\quad\text{for every stationary }p\text{ and every }i.}
\tag{SU3}
\]

*Proof.* The path family of \(q\) has size \(n!/2\), and every path's exterior edges lie in the indicated union of supports. Recoloring orbits outside that union leaves these paths unchanged. Every recoloring inside the union destroys at most the sharp exterior incidence maximum from (SE1). The union bound proves (SU2); setting \(N_0(c)=0\) yields (SU3). \(\square\)

Thus each hypothetical counterexample must be misaligned with *every* stationary comparison state on a sizable number of orbits belonging to sparse, explicitly known exterior middle-layer windows. This is stronger than a bound on its total parity discrepancy alone, yet it still does not exclude globally distributed colorings.


### Connected balanced padding with independent marginals and sparse square curvature

**Theorem (counterexample-preserving connected lift).** Every bad antipodally odd coloring in dimension n has bad lifts in all dimensions 2n+2k, k>=max(2,n-1), which are perfectly balanced at every vertex and have connected undirected direction-influence graph. For every fixed t, almost all t-subsets of directions exhibit mutually independent uniform incident-edge colors; moreover almost every pair of directions has zero cubical square curvature. Thus the corresponding class is sufficient to settle unrestricted NORI1.

*Construction and proof.* Let c be an odd undirected Q_n edge coloring, n>=2. For k>=max(2,n-1), on Q_(2n+2k) with bits (x,y,a,b), set C_i=c_i(x), C_(y_i)=1-c_i(x), C_(a_j)=a_(j+1)+x_1+x_(r(j)), C_(b_j)=1+C_(a_j) mod2, where cyclic j and r(j)=2+((j-1) mod(n-1)). This is antipodally odd and pointwise degree-balanced; projecting any monochromatic full geodesic to the first n directions gives one in c. The undirected influence graph is connected: gadget a_j form a cycle, each b_j attaches to it, every x_i occurs in some gadget rule, and each y_i reads a nonconstant odd c_i. Conditional on x, the gadget source bits a_(j+1) are independent and uniform; hence 2^t binom(k,t)/binom(2n+2k,t) of all t-subsets of directions have independent fair incident colors. At most binom(2n,2)+6k direction pairs have nonzero square curvature: at most 4k gadget-old interactions, 2k adjacent-gadget interactions, and all old-old pairs. Thus this exceptional fraction approaches zero as k grows. If a bad coloring exists, it has connected perfectly balanced bad lifts with arbitrary fixed-order local color independence and locally flat squares on all but a vanishing proportion of direction sets. Hence proving NORI1 in this class implies NORI1 unrestricted. Independently audited at all vertices of Q14 for n=3,k=4; script nori_balanced_connected_padding_audit.py, SHA256 d67ebb15ce17e24a60a27663cec56a86d7e8e64e2257914579f8ba7d6607a809.
### Middle-rank support crossing in balanced cubes

For a balanced antipodally odd coloring of Q_(2m), define R_b^k(r) to be the k-element direction sets S which support some color-b dimension-simple path from root r to r xor 1_S.

**Theorem (universal halfpath expansion).** For every root r, color b, and 0<=k<=m,
\[
\boxed{|R_b^k(r)|\ge\binom mk.}\tag{HC1}
\]
*Proof.* For S in R_b^k, the reached vertex has m incident b-edges, at most k of which use directions in S. Hence at least m-k b-edges extend to distinct (k+1)-direction supports. Every support T of size k+1 has at most k+1 predecessors. Thus \((k+1)|R_b^{k+1}(r)|\ge(m-k)|R_b^k(r)|\); induction from |R_b^0|=1 proves (HC1). QED.

**Theorem (complementary halfpath criterion).** A legal coloring of Q_(2m) has a monochromatic full antipodal geodesic if and only if there are a root r and an m-set S such that
\[
\boxed{S\in R_0^m(r)\quad\text{and}\quad [2m]\setminus S\in R_1^m(r).}\tag{HC2}
\]
*Proof.* Choose a zero m-step path from r to v=r xor 1_S and a one m-step path from r using the complementary direction set. Antipodal translation converts the latter path to a zero path from bar r to v. Reverse and concatenate with the first half; their direction sets partition [2m], giving a zero full geodesic. Conversely split any zero full geodesic after m steps. Reverse and antipodally translate its second half to get the complementary one path from r. A one full geodesic becomes zero under antipodal translation. QED.

**Corollary (closure-equivalent middle-rank intersection).** Combining (HC2) with the badness-preserving perfect-balance lift, unrestricted NORI1 is equivalent to the statement that for every balanced legal coloring in every even dimension there exists a root r for which
\[
R_0^m(r)\cap\{[2m]\setminus T:T\in R_1^m(r)\}\ne\varnothing.
\tag{HC3}
\]
Each family is nonempty at every root by (HC1), but demanding (HC3) root by root is false. On Q_6 set c_i(x,y)=x_((i+1) mod3) and c_(3+i)(x,y)=1-x_((i+1) mod3), i=0,1,2. At r=0, the reachable zero halfpath supports are represented by bit masks \(\{11,14,21,22,35,37\}\), whereas the one halfpath supports comprise only mask 56. The complement of mask 56 is 7, absent from the zero set. The coloring is nevertheless good. Thus a closure argument must couple different roots, not merely demand complementary midpoint supports at each root.


## Directional affinity of full-geodesic counts

Let \(c\) be an antipodally odd binary edge coloring of \(Q_n\), and let \(Z(c)\) count its monochromatic-zero unoriented full antipodal geodesics. Write \(M_i\) for the antipodal edge-pair orbits in direction \(i\), and \(c^{[S]}\) for simultaneous reversal of the orbits in \(S\).

**Theorem (directional modularity).** For every \(S\subseteq M_i\),
\[
Z(c^{[S]})=Z(c)+\sum_{p\in S}(Z(c^{[\{p\}]})-Z(c)).\tag{DM1}
\]
*Proof.* Every full geodesic uses one edge in direction \(i\). Its monochromatic-zero indicator changes under \(S\) only through the reversal of that edge's orbit, so its change is the sum of its changes under the singleton reversals in \(S\). Sum over geodesics. \(\square\)

**Corollary (simultaneous repair).** If \(c\) is bad, then
\[
Z(c^{[S]})=\sum_{p\in S}Z(c^{[\{p\}]}).\tag{DM2}
\]
Therefore a same-direction recoloring heals \(c\) if and only if it includes a healing singleton. If every member of \(S\) is healing, then \(Z(c^{[S]})\ge|S|\).

**Theorem (Boolean fibers of bad completions).** Fix the colors of all edge orbits outside direction \(i\). For each orbit \(p=\{e_p,\bar e_p\}\in M_i\), let \(L_p^+\), respectively \(L_p^-\), be the number of full geodesics through \(e_p\), respectively \(\bar e_p\), whose other \(n-1\) edges are zero. If the zero member of \(p\) is chosen by \(\eta_p\in\{+,-\}\), then
\[
Z(\eta)=\sum_{p\in M_i}L_p^{\eta_p},\qquad
\min_\eta Z(\eta)=\sum_{p\in M_i}\min(L_p^+,L_p^-).\tag{DM3}
\]
In particular, bad completions form either the empty set or a Boolean subcube of the direction-\(i\) orbit assignments.

*Proof.* Each zero full geodesic is counted by the summand corresponding to its unique direction-\(i\) orbit. Since all summands are nonnegative, \(Z(\eta)=0\) precisely when every selected \(L_p^{\eta_p}\) vanishes. The choices at different orbits are independent. \(\square\)

**Corollary (zero-energy extremal rigidity).** If a bad coloring \(c\) maximizes the facet-imbalance energy among bad colorings and its imbalance vector \(B\) vanishes, then each singleton flip raises its energy by \(4(n-1)\) and therefore heals. Consequently, for each direction \(i\), \(c\)'s orbit assignment is the unique bad completion with all other directions held fixed; moreover \(Z(c^{[S]})\ge|S|\) for every nonempty \(S\subseteq M_i\).

The theorem applies to unrestricted colorings. It constrains the bad set on each direction fiber, without imposing consistency of those fibers across distinct directions.


## Facet balance and sharp opposite face extremes under counterexample-preserving lifts

For an antipodally odd edge coloring C of Q_N, let s_i(v)=(-1)^{C_i(v)}. Call C *vertex-balanced* when \(\sum_i s_i(v)=0\) for every vertex v. This requires even N.

**Theorem (balanced facets).** Every vertex-balanced antipodally odd coloring has equally many edges of the two colors in every facet.

*Proof.* Fix a facet F by setting bit i to b. Double-counting its internal signed edges gives
\[
2\sum_{e\subset F}s(e)
=\sum_{v\in F}\sum_{j\ne i}s_j(v)
=-\sum_{v\in F}s_i(v).
\]
The direction-i edge function s_i ignores bit i and is odd under complementing all other bits. Its sum over the remaining \(N-1\) freely varying bits is zero. Thus the facet signed-edge sum vanishes. \(\square\)

In particular, in a vertex-balanced legal coloring the vertex and facet edge-count imbalances both attain their minimum, zero. The unrestricted mean-switch identity gives the maximum possible mean switch count, \(N/2\). This does not require the colors to be evenly distributed on smaller-dimensional faces.

**Theorem (near-extremal monochromatic faces and approximate independent local colors).** Let c be any antipodally odd coloring of Q_n, n>=3. For every integer k>=3 there is an antipodally odd coloring C of Q_N, N=2n+2k, such that:

1. C is vertex-balanced, and its undirected direction-influence graph is connected.
2. Any monochromatic full antipodal geodesic of C projects onto a monochromatic full antipodal geodesic of c.
3. C contains a monochromatic k-dimensional face, and \(k=N/2-n\). Every monochromatic face of any vertex-balanced coloring of Q_N has dimension at most N/2, so this approaches the upper bound with additive deficit n.
4. Fix t. At least the proportion
\[
\boxed{\frac{2^t\binom{k}{t}}{\binom{2n+2k}{t}}}\tag{BE1}
\]
of all t-element direction sets have a joint distribution of incident colors at a uniformly chosen vertex whose total-variation distance from t independent fair bits is at most \(k\,2^{2-k}\). For n,t fixed, the proportion tends to one and the total-variation bound tends to zero as k grows.

*Construction.* Let \(\beta:\{0,1\}^n\to\{0,1\}\) be antipodally odd and sensitive to every input bit. Such a function exists for n>=3: for odd n use the parity of all n bits; for even n>=4 use majority, breaking ties by the first bit. Use old bits x_i, compensator bits y_i, and k pairs of new bits u_j,v_j, with indices j interpreted cyclically. Define
\[
H_j(v)=\mathbf1_{\{v_\ell:\ell\ne j\text{ are all equal}\}},\qquad
g_j(x,u,v)=
\begin{cases}
\beta(x),&H_j(v)=1,\\
u_{j+1},&H_j(v)=0,
\end{cases}\tag{BE2}
\]
and put
\[
\boxed{C_{x_i}=c_i(x),\quad C_{y_i}=1-c_i(x),\quad
C_{u_j}=g_j,\quad C_{v_j}=1-g_j.}\tag{BE3}
\]

*Proof.* Every old rule ignores its own direction bit. The rule g_j does not read u_j since k>=3; it also does not read v_j, since H_j omits v_j. The test H_j is unchanged when all v bits are complemented. Both beta(x) and u_(j+1) change their bits under full antipodal complementation, so g_j does too. All rules therefore satisfy the undirected-edge and antipodal-odd requirements. Each old/compensator pair and each new pair contribute opposite incident colors, proving vertex balance.

Deleting all non-x steps from a full monochromatic geodesic of C yields a full monochromatic geodesic of c, proving the projection assertion. The undirected influence graph is connected: each new u_j reads u_(j+1) when H_j=0, yielding a cycle; each v_j rule reads u_(j+1), attaching v_j; each g_j depends on beta(x) when H_j=1, and beta is sensitive to every x_i; each compensator y_i reads an old x-bit since the odd Boolean function c_i is nonconstant.

Fix all old, compensator, and v bits, with v_1=...=v_k=0, and allow the k bits u_1,...,u_k to vary freely. Then H_j=1 for every j, so the induced k-face has every edge of color beta(x), proving the monochromatic-face assertion. Conversely, if an r-face is monochromatic with color b, each of its vertices has at least r incident edges of color b. Vertex balance implies r<=N/2.

For the distributional assertion, let E be the event that H_j(v)=1 for some j. Each H_j depends on k-1 independent v-bits and satisfies
\[
\Pr(H_j=1)=2^{2-k},\qquad
\Pr(E)\le k2^{2-k}.\tag{BE4}
\]
Conditional on the complementary event, all g_j are the mutually independent fair bits u_(j+1). Event E depends only on v and is independent of all u bits. Thus any t incident colors chosen from distinct new pairs, taking either u_j or v_j in each pair, are within total-variation distance at most Pr(E) of t independent fair bits. There are \(2^t\binom{k}{t}\) such selections, proving (BE1). \(\square\)

**Corollary (joint extremization does not force the conjecture).** For every fixed t and epsilon>0, unrestricted NORI1 is equivalent to NORI1 for even-dimensional legal colorings which are vertex-balanced and interaction-connected, contain a monochromatic face of dimension at least \((1/2-\epsilon)N\), and have incident-color distributions within epsilon of independent fair bits on at least a fraction \(1-\epsilon\) of t-direction subsets.

Indeed, if a bad coloring c existed then (BE3), for large k, would give bad colorings satisfying all four restrictions. This exhibits the coexistence of perfect vertex and facet balance, almost maximal monochromatic-face dimension, and asymptotically independent local color samples. The residual closure question is global compatibility of full dimension-simple geodesics, not either local extremum separately.

An independent enumeration of Q_14, taking n=3 and k=4, verified undirectedness, antipodal oddness, vertex balance, interaction connectivity, and the monochromatic-face condition at every vertex. It also checked the two-gadget color distribution and the guard-event probability. Reproducible script nori_self_guarded_extremes_audit.py.



## Two freely recolored directions: terminal-path conservation and exterior robustness

Let \(n=2m\ge4\), \(p_k(x)=b_k+\sum_{\ell\ne k}x_\ell\bmod2\) be a stationary parity coloring, and \(i\ne j\) be directions. Let \(q\) be any antipodally odd coloring agreeing with \(p\) outside directions \(i,j\). Write \(T=(n-1)!\) and \(H=\binom{n-2}{m-1}\).

**Theorem (terminal geodesic conservation).** The number of unoriented monochromatic-zero full antipodal geodesics of \(q\) with direction \(i\) terminal is \(T\); likewise for \(j\).

*Proof.* Fix an order \(\pi\) beginning with \(i\), and initial vertex \(x\), with \(R=\sum_kx_k\bmod2\). Requiring the edges in each unchanged direction \(k\notin\{i,j\}\) to be zero gives \(x_k=R+b_k+\pi^{-1}(k)-1\bmod2\). The \(n-2\) equations leave four roots, parametrized by \(x_i,x_j\). Holding \(x_j\) fixed and toggling \(x_i\) complements all bits of the root other than \(x_j\), so the observed direction-\(j\) edge changes to its antipodal mate and its color toggles. Thus two of the four roots have zero color in every step after the initial \(i\)-step.

When the initial step is one, delete it and append its antipodal mate to the far end; this root-slide gives a zero full geodesic with \(i\) terminal. Each target unoriented zero path with \(i\) terminal has two source representations: its zero orientation starting with \(i\), and the path starting with the antipodal \(i\)-edge (color one), followed by the original remaining zero chain backwards. Both sources use the same edges in all directions except \(i\). Therefore \(2(n-1)!\) candidates produce \(T\) targets. \(\square\)

**Theorem (exterior incidence).** Every antipodal edge orbit in a direction \(k\notin\{i,j\}\) belongs to at most \(T/H\) of the conserved terminal zero geodesics.

*Proof.* The four roots satisfying the unchanged direction constraints, for a fixed order starting with \(i\), are precisely the zero roots for four stationary parity references obtained by independently toggling their \(i,j\) sign offsets. Within the \(i\)-terminal zero family of each reference, every supported exterior orbit appears \(T/H\) times and the support is a middle layer of \(H\) projective orbits. Toggling the \(i\) sign preserves each exterior middle-layer support by complementing the remaining \(n-2\) bits; toggling the \(j\) sign sends it to a disjoint support by toggling one adjusted bit. Hence a fixed exterior orbit occurs in zero or two reference families. It appears in at most \(2T/H\) source paths, and each target has two sources with the same exterior edges, yielding \(T/H\). \(\square\)

**Consequences.** The two terminal families each have \(T\) members; their intersection has at most \(2(n-2)!\), by fixing both terminal directions and an order of the other \(n-2\), so
\[
\boxed{N_0(q)\ge 2(n-2)!(n-2).}\tag{TD1}
\]
If \(c\) further differs from \(q\) on \(t\) antipodal edge pairs outside \(i,j\), then
\[
\boxed{N_0(c)\ge T(1-t/H)_+.}\tag{TD2}
\]
This follows by charging at most \(T/H\) terminal paths to every additional changed orbit. In particular every hypothetical bad odd coloring \(c\) in even dimension has, outside **every** pair of directions \(i,j\), at least \(H\) edge-pair discrepancies relative to every stationary parity reference. If \(\alpha_k=\widehat{s_k}([n]\setminus\{k\})\) are its top admissible Walsh coefficients, choosing the reference signs independently to minimize directionwise discrepancies yields
\[
\boxed{\sum_{k\notin\{i,j\}}(1-|\alpha_k|)\ge
\binom{n-2}{m-1}/2^{n-3}.}\tag{TD3}
\]
These conclusions are restrictions on unrestricted hypothetical counterexamples, not a special-coloring assumption. The terminal count and exterior incidences were separately audited in dimensions four and six.



## Bounded-Fourier-degree balanced lifts: a barrier to spectral-only closure

**Theorem (counterexample-preserving low-degree lift).** Let \(n\ge3\), and let \(c\) be any antipodally odd binary edge coloring of \(Q_n\). For every \(k\ge0\), there exists a vertex-balanced antipodally odd coloring \(C\) of \(Q_N\), \(N=2n+2k\), satisfying:

(i) every monochromatic full antipodal geodesic in \(C\) projects to a monochromatic full antipodal geodesic in \(c\);

(ii) each signed direction-edge function of \(C\) has Walsh degree at most \(n-1\), regardless of \(k\);

(iii) every vertex and facet has zero color imbalance, and every highest-permitted Walsh coefficient
\(\widehat{s^{C}_a}([N]\setminus\{a\})\) vanishes.

*Proof.* Write the axes as original \(x_1,\ldots,x_n\), compensators \(y_1,\ldots,y_n\), and new pairs \(u_1,v_1,\ldots,u_k,v_k\). Choose an antipodally odd Boolean function \(\beta(x)\), for instance \(x_1\). Set
\[
\boxed{
C_{x_i}(x,y,u,v)=c_i(x),\quad
C_{y_i}(x,y,u,v)=1-c_i(x),\quad
C_{u_j}=\beta(x),\quad C_{v_j}=1-\beta(x).}
\tag{BL1}
\]
All direction rules ignore their own direction bits. Under global antipodal complementation, every displayed bit changes because each \(c_i\) and \(\beta\) is antipodally odd. Thus \(C\) is legal.

At each vertex, each compensator pair \(x_i,y_i\) contributes one edge of each color, as does each new pair \(u_j,v_j\), proving vertex balance. Facet balance then follows by the established balanced-facet theorem. In signed form, every rule depends only on the original \(n\) bits. The \(c_i\) rule ignores \(x_i\), so its Walsh degree is at most \(n-1\); the companion has the same spectrum up to sign, while the new rules \(\beta(x)=x_1\) have degree one. For \(N>n\), no direction rule has Fourier mass at degree \(N-1\); this proves (ii),(iii).

A full dimension-simple geodesic in \(Q_N\) traverses each original \(x_i\)-direction once. Deleting all other steps produces a full antipodal geodesic in the \(x\)-cube. Its \(x_i\)-edge colors are unchanged from \(c_i(x)\), so if the full path is monochromatic then so is the projected path. \(\square\)

**Corollary (spectral-barrier implication).** If NORI1 fails in any dimension, it fails in infinitely many arbitrarily large even dimensions with vertex and facet imbalance identically zero, and with all direction-color Fourier spectra supported in degrees at most a constant depending only on the original counterexample. In particular the top Walsh coefficients \(\alpha_i\) of all these counterexamples vanish, as does the entire vertex-degree field \(d(v)\). Their high-parity spectral discrepancy from stationary states is maximal in every direction.

Consequently neither the positive first-level facet-energy condition nor proximity to the top-degree stationary parity characters, nor any criterion based only on those two regimes, can settle unrestricted NORI1 without an additional global compatibility invariant. This corollary concerns a hypothetical counterexample and does not construct one.


## Counterexample-preserving one-source padding and imbalanced extremal reduction

Let \(c=(c_1,\ldots,c_n)\) be an antipodally odd binary edge coloring of \(Q_n\), represented by functions \(c_i(x)\) independent of bit \(i\). Fix an original direction \(j\), let \(k\ge1\), and put \(N=n+k\). On \(Q_N\) with vertex bits \((x,z)\in Q_n\times Q_k\), define
\[
\boxed{
C_i(x,z)=c_i(x)\ (1\le i\le n),\qquad
C_{n+t}(x,z)=x_j\ (1\le t\le k).
}
\tag{IP1}
\]

**Theorem (badness-preserving imbalanced padding).** The coloring \(C\) is antipodally odd. If \(c\) is bad, then every coloring obtained from \(C\) by independently reversing any subset of the antipodal edge pairs in its \(k\) added directions is bad. These are
\[
\boxed{2^{k2^{N-2}}}
\tag{IP2}
\]
distinct bad legal colorings in dimension \(N\).

*Proof.* An old direction rule ignores every new bit and remains odd under full complementation. A new rule \(x_j\) ignores its new direction and reverses under complementing all vertex bits. Thus \(C\) is legal. Every full dimension-simple antipodal geodesic in the lifted cube projects, on deleting the new-direction steps, to a full dimension-simple antipodal geodesic of \(Q_n\): it traverses each old direction once, and the old edge colors are those of \(c\). Therefore a monochromatic full path in any stated recoloring would project to one in \(c\), contrary to badness. There are \(2^{N-2}\) antipodal edge pairs per added direction, giving (IP2). \(\square\)

Let \(F_j=\{x:x_j=0\}\) in the original cube, and let \(t_j\) be its number of one-colored internal edges. Write \(F'_j\) for the corresponding facet of \(Q_N\).

**Theorem (arbitrarily polarized facets).** In the lifted coloring (IP1), the number of one-colored edges within \(F'_j\) is \(2^k t_j\), while the total number of edges in that facet is \((N-1)2^{N-2}\). Consequently
\[
\boxed{
\frac{\#\{\text{one-colored edges in }F'_j\}}
{\#E(F'_j)}
=\frac{t_j}{(N-1)2^{n-2}}
\le\frac{n-1}{N-1}\longrightarrow0
\quad(k\to\infty).
}
\tag{IP3}
\]
Writing \(B_j(c)\) for the signed imbalance of \(F_j\), the imbalances satisfy
\[
\boxed{B'_j=2^k B_j(c)+k\,2^{N-2}.}
\tag{IP4}
\]
In particular \(\lim_{k\to\infty}B'_j/[(N-1)2^{N-2}]=1\).

*Proof.* Each old internal edge of \(F_j\) occurs in \(2^k\) copies, and every added-direction edge inside \(F'_j\) has color zero because \(x_j=0\). Each added direction contributes \(2^{N-2}\) such zero edges. Counting the old and new edges proves both assertions. The original facet has \((n-1)2^{n-2}\) edges, giving the upper bound. \(\square\)

**Corollary (the nonzero-energy extremal branch suffices for closure).** If a bad legal coloring exists in some dimension \(n\), then in dimension \(n+1\) there is a bad coloring with a nonzero signed facet-imbalance vector. Consequently that dimension admits an energy-maximizing bad coloring with nonzero imbalance, where \(\mathcal E=\sum_iB_i^2\).

*Proof.* Use \(k=1\) and choose the new rule to be either \(x_j\) or \(1-x_j\). Both preserve badness by projection. Their distinguished facet imbalances are \(2B_j(c)+2^{n-1}\) and \(2B_j(c)-2^{n-1}\), which cannot both vanish. Therefore at least one bad extension has positive energy. An energy maximum over the finite bad-coloring space of \(Q_{n+1}\) has energy no smaller, and its imbalance vector is nonzero. \(\square\)

This removes the \(B=0\) case from a strategy that seeks to contradict the existence of energy-maximizing bad colorings in arbitrary dimensions, since any lower-dimensional counterexample may first be lifted once. Conversely, (IP3) shows that a dimension-independent positive upper bound on the fraction of monochromatic edges within a single facet cannot by itself prove the conjecture: conditional on any bad coloring, there are bad lifts with a facet arbitrarily close to monochromatic. The fixed-dimensional extremality and simultaneous-restoration restrictions remain meaningful.



### Two-way balanced lift and factorial geodesic-count transfer

Let \(c\) color \(Q_n\) antipodally oddly, \(n\ge2\). Take its balanced low-degree lift \(C\) to \(Q_{2n+2k}\) as defined in (BL1), with \(D=n+2k\) auxiliary directions. Then
\[
\boxed{N_0(C)>0\iff N_0(c)>0,}\tag{BL2}
\]
and
\[
\boxed{N_0(C)\ge
2^{D}(\lfloor n/2\rfloor+k)!(\lceil n/2\rceil+k)!\,N_0(c).}
\tag{BL3}
\]

*Proof.* A zero full geodesic in \(C\) projects to a zero full geodesic in \(c\), by deleting every auxiliary step. For the converse, orient a zero full geodesic \(P\) of \(c\) from vertex \(x\) to \(\bar x\). Each original direction function \(c_i\) has opposite values at these endpoints. Insert the auxiliary \(y_i\)-step, whose color is \(1-c_i\), before \(P\) when \(c_i(x)=1\) and after \(P\) otherwise. For each extra auxiliary pair \(u_j,v_j\), whose colors are \(\beta(x)\) and \(1-\beta(x)\), insert one step before and the other after \(P\), where each has color zero. Since all auxiliary colors depend only on the original \(x\)-bits, these insertions do not affect one another.

If \(a\) of the values \(c_i(x)\) equal one, there are \(a+k\) auxiliary steps before \(P\) and \(n-a+k\) after. Their orders can be chosen freely, as can the \(2^D\) starting auxiliary bit strings. This yields \(2^D(a+k)!(n-a+k)!\) lifts per oriented original zero path. The opposite orientation exchanges \(a\) and \(n-a\) and reverses the lifts; hence the same expression counts unoriented lifted paths per unoriented original path. Factorial log-convexity makes the product smallest for \(a\) nearest \(n/2\), proving (BL3). \(\square\)

**Full gap-allocation count.** Choose one orientation \(P=(x_0,\ldots,x_n)\) per unoriented zero path of \(c\), and write \(h_d(x)\) for the edge color of auxiliary direction \(d\) at original vertex \(x\). Assign each auxiliary direction a gap \(\sigma(d)\in\{0,\ldots,n\}\) in which \(h_d(x_{\sigma(d)})=0\), and order the directions within each gap. Then
\[
\boxed{N_0(C)=2^D\sum_{P\in\mathcal G_0(c)}
\ \sum_{\sigma:\ h_d(x_{\sigma(d)})=0\ \forall d}
\prod_{t=0}^n|\sigma^{-1}(t)|!.}
\tag{BL4}
\]
This follows by bijectively encoding each lifted unoriented path by the orientation projecting to the chosen \(P\), the admissible gap assignment, orders inside gaps, and starting auxiliary bits.

The lift therefore transfers geodesic existence in both directions, while increasing path multiplicity at least factorially, despite perfect balance and bounded Fourier degree.



### Co-singleton Fourier coupling of vertex imbalance and high parity

Let \(c\) be an antipodally odd coloring of \(Q_N\), \(N\ge3\). Put \(s_i(x)=(-1)^{c_i(x)}\), \(d(x)=\sum_i s_i(x)=N-2r(x)\), and \(\alpha_i=\widehat{s_i}([N]\setminus\{i\})\).

**Theorem.** For each \(i\),
\[
\boxed{\alpha_i=\widehat d([N]\setminus\{i\}),}\tag{VB1}
\]
and
\[
\boxed{\sum_i\alpha_i^2
\le 2^{-N}\sum_x d(x)^2
=\frac4{2^N}\sum_x(r(x)-N/2)^2.}\tag{VB2}
\]
In particular, **vertex-balanced colorings have \(\alpha_i=0\) in every direction**.

*Proof.* The signed direction rule \(s_j\) ignores its own bit \(x_j\). If \(j\ne i\), the Walsh character of the set \([N]\setminus\{i\}\) depends on \(x_j\), so \(\widehat{s_j}([N]\setminus\{i\})=0\). Taking this Walsh coefficient in \(d=\sum_j s_j\) therefore leaves only \(\widehat{s_i}([N]\setminus\{i\})\). Orthogonality of the co-singleton Walsh characters and Bessel's inequality imply the squared-energy bound. The final equality uses \(d=N-2r\). \(\square\)

**Interpretation.** High-parity spectral concentration forces a lower bound on squared vertex imbalance. Conversely a perfectly vertex-balanced coloring has no high-parity direction coefficient, regardless of how its remaining Fourier spectrum is distributed. Since counterexample-preserving balanced lifts exist, parity-neighborhood and facet-imbalance conditions alone cannot eliminate hypothetical unrestricted counterexamples: a global path-compatibility constraint is necessary.


### Closure-equivalent dominant-reader reduction

Let \(g:\mathbb N\to\mathbb N\) be any function satisfying \(g(N)\to\infty\) as \(N\to\infty\). Consider the class of antipodally odd edge colorings of \(Q_N\) for which some direction \(j\) satisfies
\[
\boxed{c_i(x)=x_j\quad\text{for all but at most }g(N)\text{ directions }i.}
\tag{DR1}
\]
In particular all the indicated directions are distinct from \(j\); the remaining direction functions are unrestricted.

**Theorem (dominant-reader equivalence).** NORI1 holds for every antipodally odd edge coloring in every dimension if and only if it holds for every coloring in (DR1), for any fixed unbounded function \(g\).

*Proof.* One implication is immediate. Conversely, suppose an arbitrary bad coloring \(c\) of \(Q_n\) exists. Choose \(N>n\) so large that \(g(N)\ge n\), and apply the imbalanced padding construction (IP1) with \(k=N-n\), choosing any original direction \(j\). The resulting legal coloring \(C\) is bad by projection, while its \(N-n\) added directions all have rule \(C_i=x_j\). Only the \(n\) original directions may violate (DR1), and \(n\le g(N)\). Thus the restricted assertion would fail as well. \(\square\)

The equivalence holds, for example, with \(g(N)=\max(1,\lfloor\log\log N\rfloor)\), or with \(g(N)=\lfloor\epsilon N\rfloor\) for any fixed \(\epsilon>0\). The latter form states that restricting to colorings with a common signed reader on at least a \((1-\epsilon)\)-fraction of directions leaves NORI1 unchanged.

**Caveat.** The exceptional direction functions in (DR1) may represent an arbitrary \(Q_n\) coloring and retain the entire obstruction under projection. The theorem is a counterexample-preserving reduction, not an independent proof of compatibility for a bounded-hub reader class. A proof exploiting the dominant reader must control an exceptional core whose size is unbounded, albeit arbitrarily slowly growing.



### Balanced NORI1 as a reversible Eulerian alternating-rainbow path problem

Let \(n=2m\), and orient every edge of \(Q_n\) from its even-parity endpoint to its odd-parity endpoint when its color is zero, and in the opposite direction when its color is one. Denote the resulting digraph by \(D_c\).

**Theorem (Eulerian correspondence).** The coloring \(c\) is vertex-balanced if and only if \(D_c\) is Eulerian, meaning indegree equals outdegree \(m\) at each vertex. Moreover, when \(c\) is antipodally odd, the antipodal map \(\tau\) reverses every directed arc of \(D_c\). Conversely, every Eulerian orientation of \(Q_{2m}\) for which \(\tau\) reverses all arcs defines a vertex-balanced antipodally odd coloring by making even-to-odd arcs color zero and odd-to-even arcs color one.

*Proof.* At an even vertex, a zero edge points outward and a one edge inward; at an odd vertex the roles reverse. Equal color degrees \(m,m\) are therefore equivalent to equal directed in/out degrees at each vertex. For even \(n\), antipodal complementation preserves vertex parity. If the coloring is odd, the antipodal edge has the opposite color, hence the orientation prescribed by the rule reverses under \(\tau\). The converse follows by reversing these implications. \(\square\)

**Geodesic equivalence.** In this digraph, a monochromatic-zero antipodal full geodesic is a path traversing each direction once whose arc traversal signs alternate forward/backward/forward/backward, starting with forward at an even initial vertex and backward at an odd initial vertex. The antipodal image supplies the complementary monochromatic-one geodesic, so zero suffices. Combined with the established counterexample-preserving balanced lift, unrestricted NORI1 is equivalent to the following dimension-uniform statement:

> Every Eulerian orientation of an even-dimensional hypercube for which antipodal complementation reverses all arcs contains a full antipodal direction-rainbow path whose traversal alternates with the bipartite parity.

**Halfpath guarantee and remaining obstruction.** From every root of such an orientation, there is a monochromatic-zero direction-simple path of length \(m\) and a monochromatic-one such path of length \(m\): at stage \(t<m\), at least \(m-t>0\) of the \(m\) incident edges of either color have as-yet-unused directions. Grand-theorem closure demands a root and a pair of these opposite-color halfpaths with complementary used direction sets, as in the existing halfpath criterion; this rootwise condition is not automatic, and examples in Article XV show it may fail at specified roots.

The Eulerian correspondence is a structural equivalence, not a claim that an arbitrary Eulerian graph satisfies the desired rainbow-path property. It isolates the crucial global obstruction beyond first-order vertex balance.




### Antipodal alternating-cycle switch connectivity and monochromatic two-path rigidity

Let \(n=2m\ge4\), and let \(c,d\) be antipodally odd vertex-balanced undirected binary edge colorings of \(Q_n\). Write \(\tau x=\bar x\). Call a *paired alternating-cycle switch* the operation of reversing colors on the edge-disjoint union of two distinct antipodal images \(C,\tau C\), where \(C\) is an even simple cycle with colors alternating around it. Such a switch preserves antipodal oddness and all vertex color degrees.

**Theorem (balanced odd configuration space is connected under paired alternating-cycle switches).** Every pair \(c,d\) as above is related by a sequence of paired alternating-cycle switches. The cycles of each switch can be chosen edge-disjoint from those of every other switch, all alternating with respect to the initial coloring \(c\). The intermediate colorings remain vertex-balanced and antipodally odd. If \(D=\{e:c(e)\ne d(e)\}\), the number of switches is at most \(|D|/8\).

*Proof.* Antipodal oddness of \(c,d\) implies \(\tau D=D\). At every vertex, the number of incident \(D\)-edges colored zero by \(c\) equals the number colored one: each change from zero to one is compensated by a change from one to zero because \(c,d\) have the same zero degree \(m\). Orient the \(D\)-edges from even to odd vertices when colored zero by \(c\), and from odd to even vertices when colored one. The resulting digraph \(H\) is Eulerian, and \(\tau\) reverses every arc.

Choose, at one representative \(v\) of each antipodal vertex pair, an arbitrary bijection \(f_v\) from the incoming arcs at \(v\) to the outgoing arcs at \(v\). At \(\tau v\), transport its inverse: the incoming arc \(\tau b\), corresponding to an outgoing arc \(b\) at \(v\), is followed by the outgoing arc \(\tau f_v^{-1}(b)\). These transition bijections first partition the directed edges of \(H\) into closed directed trails, and \(\tau\) maps each trail to another trail with reversed cyclic order. No trail can be invariant under this action: a reflection of the cyclic list of vertices that preserves their alternating parity classes fixes a vertex position, contradicting the fixed-point-free antipodal map. To obtain simple cycles, whenever a trail visits a vertex \(v\) more than once, exchange the outgoing successors of two of its incoming arcs at \(v\), and simultaneously perform the antipodally corresponding inverse exchange at \(\tau v\). The trail and its distinct antipodal partner each split into two shorter closed trails. Repeating this operation strictly increases the number of trails and ultimately yields simple directed cycles. These cycles still occur in distinct antipodal pairs \(C,\tau C\), and the paired cycles have disjoint edges, although they may share vertices. They alternate zero and one because the digraph orientation follows zero edges even-to-odd and one edges odd-to-even.

Switch the colors on each pair \(C\cup\tau C\). At each vertex, each switched cycle contributes the same number of incident zero and one edges, so vertex balance is preserved. The switched edge set is \(\tau\)-invariant, so oddness is preserved. The paired cycles partition \(D\); switching all pairs therefore changes \(c\) into \(d\). Every cycle has at least four edges, and distinct antipodal partners contribute at least eight, proving the switch bound. \(\square\)

**Theorem (monochromatic component two-connectivity).** Let \(f\) be any vertex-balanced binary coloring of \(Q_{2m}\), without an antipodal hypothesis, with \(m\ge2\). Each connected component of either monochromatic graph is two-vertex-connected.

*Proof.* Let \(K\) be an \(m\)-regular connected bipartite component with classes \(A,B\), and suppose \(v\in A\) were a cut vertex. For every component \(U\) of \(K-v\), put \(A_U=A\cap U\), \(B_U=B\cap U\). Counting incident edges from the two sides gives
\[
m|A_U|+d(v,U)=m|B_U|,
\]
hence \(d(v,U)=m(|B_U|-|A_U|)\) is a positive multiple of \(m\). Summing over the components gives \(\sum_Ud(v,U)=m\), so there can be only one component, a contradiction. The case \(v\in B\) is symmetric. \(\square\)

**Corollary (two disjoint monochromatic antipodal paths).** In every vertex-balanced antipodally odd \(Q_{2m}\) coloring, \(m\ge2\), both colors have a component containing an antipodal pair, and within each such component any antipodal pair is joined by two internally vertex-disjoint monochromatic paths. Their union is a simple monochromatic cycle of length at least \(2n\). Indeed the established monochromatic antipodal-path theorem supplies one such component; antipodal complementation supplies the opposite color, and the preceding two-connectivity theorem and Menger's theorem give the paths.

The paired switches supply dimension-uniform exchanges within the balanced legal class. A switch can change the presence of monochromatic antipodal geodesics, and the two-path theorem does not control repeated directions; imposing a potential compatible with these cycle switches remains the global closure problem.



### Commuting antipodal square flips in the closure-equivalent paired-flat class

Fix \(N=2m\ge4\) and a partition of its dimensions into pairs \(P_i=\{i,i'\}\), \(1\le i\le m\). A *paired-flat coloring* is determined by functions
\[
f_i:\mathbb F_2^{[N]\setminus P_i}\longrightarrow\mathbb F_2,
\qquad f_i(\bar z)=1+f_i(z),
\]
with undirected edge rules \(c_i(z)=f_i(z|_{[N]\setminus P_i})\) and \(c_{i'}(z)=1+f_i(z|_{[N]\setminus P_i})\). Each rule disregards both bits in its pair. All these colorings are vertex-balanced and antipodally odd.

**Theorem (paired-square Boolean configuration cube).** For a fixed direction pairing, the class of paired-flat colorings is a Boolean cube of
\[
\boxed{K=m\,2^{N-3}}
\tag{EC1}
\]
independent parameters. Its elementary parameter flips have the following graph-theoretic description: choose a square face supported on some \(P_i\) and simultaneously reverse the four colors on that face and on its distinct antipodal image. Every such operation preserves the paired-flat class. The operations commute, are independent, and connect all \(2^K\) paired-flat colorings. In every one of these colorings the cube edges partition into \(m2^{N-2}\) alternating squares supported on the direction pairs, arranged into \(K\) antipodal square pairs.

*Proof.* For a fixed \(i\), the two incident edge colors in the directions \(i,i'\) are complementary, independently of their own two bits. Thus each square with free directions \(P_i\) has its \(i\)-edges of color \(f_i\) and its \(i'\)-edges of the opposite color. The four edges alternate colors cyclically. As the other \(N-2\) bits vary, these faces partition all edges in directions \(P_i\); varying \(i\) partitions the edge set of \(Q_N\). Their antipodal images are distinct for \(N\ge4\).

The \(2^{N-2}\) values of the outside bits for \(f_i\) form \(2^{N-3}\) antipodal pairs, and \(f_i(\bar z)=1+f_i(z)\) leaves one independent bit for each pair. Different \(i\) have independent rules. Hence there are \(K=m2^{N-3}\) independent bits and \(2^K\) colorings. Flipping a pair of antipodal \(P_i\)-squares toggles the corresponding value of \(f_i\) and its antipodal companion, without changing any other parameter. The square edge sets are pairwise disjoint, so these flips commute and every intermediate coloring retains the alternating-square partition. \(\square\)

**Corollary (unrestricted closure reduction to commuting square flips).** Every legal antipodally odd coloring \(b\) of \(Q_m\) admits a paired-flat lift on \(Q_{2m}\) with rules
\[
c_i(x,y)=b_i(x),\qquad c_{i'}(x,y)=1+b_i(x).
\tag{EC2}
\]
The lift has a monochromatic full antipodal geodesic if and only if \(b\) does. Thus unrestricted NORI1 is equivalent to monochromatic full-geodesic existence for every paired-flat coloring in every even dimension. In particular any hypothetical counterexample has a paired-flat representative lying in a \(K\)-dimensional commuting-square exchange cube, where every edge of the ambient cube belongs to one of the alternating square faces.

*Proof.* The functions \(b_i\) ignore their own bits, so (EC2) lies in the paired-flat class. A monochromatic full geodesic in the lift projects, after omission of the primed steps, to a monochromatic full geodesic in \(b\). Conversely, given one in \(b\), each primed step has the desired color at one of its two old endpoints because its rule is antipodally odd, so place it before or after the old geodesic accordingly. The primed steps do not affect other edge colors. \(\square\)

This parametrization identifies a large family of legal local exchanges inside a class sufficient for unrestricted theorem closure. Local square abundance and commuting connectivity can coexist with a hypothetical counterexample; an extremal proof must control how geodesic reachability changes under these flips.




### Covering radius of the successful paired-flat exchange region

Let \(N=2m\ge4\), and let \(\mathscr C_N\cong Q_K\), \(K=m2^{N-3}\), be the Boolean parameter cube of all paired-flat legal colorings for a fixed pairing of the \(N\) directions. Adjacency means switching one antipodal pair of alternating squares. Write \(\mathscr G_N\) for configurations admitting a monochromatic full antipodal geodesic. Antipodal oddness ensures that every such coloring also has a color-zero full antipodal geodesic.

For a full geodesic \(P\), let \(O(P)\subseteq[K]\) record the square-pair parameter orbits traversed by its edges, and let \(S_P\) be the set of configurations making every edge of \(P\) color zero. Whenever \(S_P\) is nonempty, it is a subcube of codimension \(|O(P)|\le N\). We have \(\mathscr G_N=\bigcup_{P}S_P\).

**Theorem (covering radius, neighborhood, and density).**
Every configuration of \(\mathscr C_N\) is within at most \(m=N/2\) square-pair switches of a successful configuration. Every \(g\in\mathscr G_N\) has at least \(K-N\) successful neighbors, and
\[
\boxed{|\mathscr G_N|\ge2^{K-N+1}.}\tag{EC5}
\]

*Proof.* Fix a root \(x\) and take the full direction order \(P=(1,\ldots,m,1',\ldots,m')\). Between its two steps of pair \(i\), precisely \(m-1\) directions outside that pair are used. Since \(0<m-1<N-2\), their assignments outside pair \(i\) are neither equal nor complementary. Hence the two edges lie in distinct antipodal square-pair parameter orbits. Different pairs have disjoint parameter sets, so \(|O(P)|=N\).

The subcube \(S_P\) prescribes \(N\) independent parameter bits. Its antipodal path \(\tau P\) encounters the same parameter orbits with opposite edge colors, so \(S_{\tau P}\) prescribes the complementary \(N\) bits. Their distance requirements from any configuration sum to \(N\); consequently at least one lies at distance at most \(m\). The two subcubes are disjoint and each has \(2^{K-N}\) vertices, proving the density bound.

Given \(g\in\mathscr G_N\), fix one all-zero full geodesic \(Q\). Any parameter switch outside \(O(Q)\) leaves all its edges unchanged. There are at least \(K-N\) such switches. \(\square\)


**Theorem (high connectivity of successful square-switch configurations).** For every even \(N\ge10\), the induced graph \(\mathscr G_N\) is connected, has diameter at most \(K+N\), and has vertex connectivity
\[
\boxed{\kappa(\mathscr G_N)\ge K-N.}\tag{EC6}
\]

*Proof.* Choose any two successful configurations \(g,h\) and zero full geodesics \(P,Q\) in them. Each full geodesic traverses two edges of each direction pair, so \(O(P)\cup O(Q)\) contains at most four square-pair orbits of any fixed direction pair.

For a uniformly random root \(x\), take the repeated-sweep full geodesic \(R_x\) with order \(1,\ldots,m,1',\ldots,m'\). At each of its two edges in pair \(i\), the outside-bit assignment modulo antipodal complementation is uniformly distributed among the \(2^{N-3}\) square-pair orbits of type \(i\). Thus the union bound gives
\[
\Pr\bigl(O(R_x)\cap(O(P)\cup O(Q))\ne\varnothing\bigr)
\le\frac{8m}{2^{N-3}}<1\qquad(N\ge10).
\tag{EC7}
\]
Choose a path \(R\) for which these orbit sets are disjoint. By the preceding theorem, \(S_R\) is a nonempty parameter subcube of codimension \(N\). The intersections \(S_P\cap S_R\) and \(S_Q\cap S_R\) are nonempty: the two families of prescribed parameter bits are disjoint in each intersection. Starting from \(g\), change at most \(N\) parameters in \(O(R)\) to reach \(S_P\cap S_R\), retaining the successful path \(P\). Do the same from \(h\) to reach \(S_Q\cap S_R\). The resulting configurations can be connected inside \(S_R\) by at most \(K-N\) more switches. All intermediate configurations remain successful, proving the diameter claim.

For vertex connectivity, remove any set \(U\) of fewer than \(K-N\) successful configurations. The subcubes \(S_P,S_Q,S_R\) have dimension at least \(K-N\), so each remains connected after the removal by the vertex connectivity theorem for ordinary hypercubes. Each of \(S_P\cap S_R\), \(S_Q\cap S_R\) has at least \(2^{K-2N}>K-N>|U|\) vertices, so both intersections retain vertices. Connect surviving \(g,h\) through the three surviving subcubes. This proves (EC6). \(\square\)

The bounds hold for arbitrary nonlinear rules in the counterexample-preserving paired-flat class. In a hypothetical counterexample dimension \(N\ge10\), the unsuccessful configurations constitute holes in a highly vertex-connected region of successful configurations; they cannot separate that region under legal paired-square switches.


### One-Lipschitz minority defect and trapped paired turns

For a paired-flat legal coloring \(c\) of \(Q_N\), let
\[
m(c)=\min_{P\ {\rm full\ geodesic}}\min\{N_0(P),N_1(P)\}
\]
be its global minority count. Antipodal complementation of a full geodesic reverses all colors, so \(m(c)\) equals the minimum number of color-one edges on a full geodesic.

**Theorem (one-Lipschitz minority defect).** If paired-flat legal colorings \(c,d\) differ by one antipodal pair of alternating square switches, then
\[
\boxed{|m(c)-m(d)|\le1.}\tag{EC8}
\]
Consequently, with the successful configuration region \(\mathscr G_N\) of (EC5),
\[
\boxed{m(c)\le\operatorname{dist}_{\mathscr C_N}(c,\mathscr G_N)
\le N/2.}\tag{EC9}
\]

*Proof.* Choose a full geodesic \(P\) with precisely \(k=m(c)\) color-one edges. Its first and last edges are color zero: if either endpoint edge had color one, orient \(P\) to put it first and cyclically transfer that first edge to the end. Its antipodal translate has color zero, reducing the color-one count, a contradiction.

Let \(F,\tau F\) be the switched faces. The geodesic uses at most two edges of \(F\cup\tau F\), because only the two paired directions are free. If it uses two edges of the same face, these are consecutive and have opposite colors; switching both preserves the number \(k\) of color-one edges. If it uses one edge, the count changes by at most one. If it uses one edge of each face, those edges are the first and last steps: traversing both complementary outside-bit assignments forces the path to start in the first face and end in the second, with the two paired directions exhausted at those steps. Both affected edges therefore have color zero by the first paragraph. After switching them, there are \(k+2\) color-one edges, at the first and last steps. Cyclically moving the first edge to the end complements its color under antipodal oddness and leaves all other colors unchanged; the rotated full geodesic has \(k+1\) color-one edges. Thus in every case \(m(d)\le m(c)+1\). Interchanging \(c,d\) proves (EC8). Along a shortest switch path from \(c\) to \(\mathscr G_N\), the minority defect falls from \(m(c)\) to zero and changes by at most one per step, giving the lower bound in (EC9). The upper bound is (EC5). \(\square\)

**Corollary (exposed-defect descent and a necessary local trap condition).** Let \(P\) attain \(m(c)=k>0\). If some color-one edge of \(P\) is the only edge of \(P\) belonging to its antipodal square-pair parameter orbit, switching that orbit produces \(d\) with
\[
\boxed{m(d)=k-1.}\tag{EC10}
\]
Consequently, at any configuration \(c\) that is a local minimum of the function \(m\) under antipodal paired-square switches, every color-one edge of every minimizing geodesic is immediately adjacent along that geodesic to a color-zero edge in the other direction of the same paired square.

*Proof.* The prescribed switch changes just the exposed color-one edge of \(P\) to color zero, so \(m(d)\le k-1\); (EC8) gives the reverse inequality. If no reducing switch exists, every minority edge of every minimizing path must share its square-pair parameter orbit with another traversed edge. Two traversed edges in antipodal companion squares would occupy the first and last steps, which are color zero for a minimizing path. Thus the minority edge shares an individual square with its paired direction step. Those two steps are consecutive and have opposite colors, as claimed. \(\square\)

This provides a dimension-uniform integer-valued potential for the complete paired-flat configuration cube. Local minima away from the successful region, if present, must be supported entirely by adjacent opposite-color paired turns. No assertion is made that such local minima exist or that all paired-turn traps can be eliminated.




### Unary-spectator single-square critical normal form

Call a coloring \(C\) a *unary-spectator pair extension* of a paired-flat coloring \(b\) on \(Q_N\) if it is defined on \(Q_{N+2}\) by keeping all old direction rules independent of the new pair, and adjoining complementary rules \(h(x)=x_t\) and \(1+h(x)\) for one old direction \(t\).

**Theorem (single-spike obstruction to unrestricted NORI1).** If unrestricted NORI1 fails, there exist an even \(N\), a bad paired-flat legal coloring \(b\) of \(Q_N\), a unary-spectator pair extension \(C\) of \(b\), and an antipodal square-pair orbit \(E\) supported on an old direction pair, such that:

1. \(C\) is bad, and has a full geodesic with one one-edge, belonging to \(E\), and all remaining edges zero. The witness has no adjacent paired-direction turns.
2. The coloring \(G\) obtained by flipping the eight edges of \(E\) in \(C\) is paired-flat, balanced, odd, and successful.
3. Every monochromatic-zero full geodesic of \(G\) uses at least one edge of \(E\).

Thus a counterexample forces the existence of a successful coloring differing from a one-way unary-spectator extension by one antipodal pair of squares, with a mandatory square orbit for all its zero full geodesics.

*Proof.* For an arbitrary bad odd coloring \(c\) of \(Q_d\), let \(W(c)\subseteq\mathbb F_2^d\) be its full-geodesic direction-color profile support. It is nonempty, closed under complementation, and misses both constant words. Choose a missing profile \(u\) adjacent in the profile cube to some attained \(w\). Direction-wise recoloring by \(u\) produces another legal coloring whose profile support is \(W(c)+u\). Both constants remain absent, since \(u,\bar u\notin W(c)\), while \(w+u\) has Hamming weight one. Thus a bad one-defect coloring exists in dimension \(d\).

Apply the complementary paired lift to obtain a bad paired-flat coloring \(b\) on \(Q_{2d}\). The profile-cylinder identity ensures that it retains a full geodesic \(P\) with one one-edge. Since \(m(b)=1\), the endpoints of \(P\) are zero, by cyclic root rotation. Each adjacent paired turn contains one one-edge, so \(P\) has at most one paired turn.

If such a turn occurs, add one unary spectator pair with reader \(h(x)=x_t\), choosing \(t\) as the second direction in the turn. Place one red spectator step between the turn's two old steps, and its other red step after the old path. Their colors are red because \(h\) flips between these two old vertices. If the path is already turn-free, add the spectator pair with any old-bit reader; place one red step before the old path and the other after it. In either case the new full geodesic \(R\) has one one-edge and no paired turns. Projection onto the old dimensions proves that the extension \(C\) remains bad.

By the turn-free square-orbit criterion, the unique one-edge of \(R\) lies in a square-pair orbit \(E\) containing no zero-edge of \(R\). Flip \(E\). All edges of \(R\) become zero in the resulting legal paired-flat coloring \(G\), proving its success. If \(G\) possessed a zero full geodesic avoiding \(E\), that geodesic would remain zero in \(C\), contradicting badness. This proves (1)--(3). \(\square\)

**Equivalent local closure target.** NORI1 holds if and only if every unary-spectator pair extension \(C\) of every paired-flat legal core, whenever \(C\) has a one-defect full geodesic, remains successful whenever any one old-pair square-orbit flip makes it successful. Necessity follows from NORI1, and sufficiency from the theorem. A stronger sufficient statement would require a zero geodesic in the switched successful coloring avoiding the flipped orbit. This formulation retains arbitrary nonlinear rules in the old core while confining the new cross-pair dependence to one unary reader and one changed square orbit.

### Counterexample-preserving spectator-pair defect stabilization

Let \(c\) be paired-flat and antipodally odd on \(Q_N\), \(N\ge4\) even. Let \(P\) be a full geodesic with \(k=m(c)\) one-edges and \(r\) adjacent turns whose directions belong to the same prescribed pair. Each turn has opposite edge colors, so \(r\le k\).

**Theorem.** There is a paired-flat odd coloring \(C\) on \(Q_{N+2\lceil r/2\rceil}\) such that \(C\) is successful if and only if \(c\) is,
\[
\boxed{m(C)=m(c)=D(C)=k,}\tag{EC15}
\]
and \(C\) has a turn-free minority-minimizing full geodesic. In fact \(k\) successive antipodal square-pair flips produce \(C=C_0,\ldots,C_k\) with \(m(C_t)=k-t\).

*Proof.* Group the paired turns into pairs, leaving one singleton if necessary. For a group of two turns at intermediate old-path vertices \(u,v\), choose an old direction \(t\) traversed between \(u,v\). Adjoin a fresh spectator direction pair with complementary color rules \(h(z)=z_t\) and \(1+h(z)\). Since \(h(u)\ne h(v)\), its two distinct red directions can be traversed at \(u\) and \(v\), separating both old paired turns. For a singleton turn at vertex \(u\), choose an old direction \(t\) still unused at \(u\). Then \(h(u)\ne h(\bar x)\), where \(x\) is the old root; traverse one red spectator step at \(u\) and the complementary red step after the old path, at \(\bar x\). All spectator rules ignore spectator bits, and old rules ignore them too, so the insertions preserve every old edge color. They create a full geodesic \(R\) with \(k\) one-edges and no adjacent paired turns.

Every full path of \(C\) projects to an old full path with unchanged old colors, so \(m(C)\ge k\), and \(R\) gives equality. A red full path of \(c\) extends to one of \(C\) by using the red member of each spectator pair before the old path and the other after it, since each reader \(h\) reverses under the old antipode. Thus failure and success are both preserved.

Two edges of a turn-free full path can share a square-pair parameter orbit only when they lie in its first and last positions; the endpoint edges of \(R\) are red because \(R\) minimizes its minority count. Therefore the \(k\) one-edges of \(R\) lie in distinct parameter orbits containing no red edge of \(R\). Switch those orbits successively. After \(t\) switches, \(R\) has \(k-t\) one-edges, while the established one-Lipschitz bound for square switches gives minority count at least \(k-t\). Hence every switch strictly lowers the defect and the last coloring is successful. The switch distance equals \(k\). \(\square\)

The witness removes all paired-turn traps by adding at most \(2\lceil m(c)/2\rceil\) directions, preserving arbitrarily nonlinear old rules and preserving counterexamples.

### Cartesian stabilization of square-switch defect descent

Let \(c\) be a paired-flat antipodally odd coloring of \(Q_{2m}\). Write \(k=m(c)\) for its minority defect, \(D(c)\) for its square-switch distance to the successful region, and \(\rho(c)\) for the minimum number of adjacent paired-direction turns on a full geodesic with \(k\) one-colored edges, as defined in (EC11). Let \(g\) be any successful paired-flat coloring of \(Q_b\), \(b\ge4\) even.

**Theorem (stabilized equality and monotone defect descent).** If \(b\ge\rho(c)\), then
\[
\boxed{D(c\boxtimes g)=m(c\boxtimes g)=m(c)=k.}\tag{EC13}
\]
There are \(k\) distinct antipodal square-pair parameters \(E_1,\ldots,E_k\) in the product configuration such that switching them successively produces legal colorings \(C_0=c\boxtimes g,C_1,\ldots,C_k\) with
\[
\boxed{m(C_t)=k-t\quad(0\le t\le k).}\tag{EC14}
\]

*Proof.* Choose a full geodesic \(P\) of \(c\) with \(k\) one-edges and \(\rho(c)\) paired turns. Its first and last edges are zero by cyclic root rotation. Every paired turn contains one edge of each color, so \(\rho(c)\le k\). Choose a zero full geodesic \(Q\) in \(g\). Interleave one successive edge of \(Q\) between the two edges of each paired turn of \(P\), and place any remaining edges of \(Q\) after all \(P\)-steps. Since the product factors are independent, the resulting full geodesic \(R\) has \(k\) one-edges.

Consider the two \(c\)-factor steps of any direction pair. Their exterior assignments in \(c\) are equal precisely when they are consecutive in the projected \(P\)-order, or antipodal precisely when they are its first and last steps. In the former case the inserted \(Q\)-step changes one \(g\)-bit between the two steps. Their exterior assignments in the product are therefore distinct modulo full antipodal complementation (as \(b\ge4\)), so they lie in different square-pair parameter orbits. In the latter case both steps are zero, being the first and last edges of the minimizing \(P\). Other pairs have disjoint parameter sets. Consequently every one-edge of \(R\) belongs to a parameter orbit containing no zero-edge of \(R\), and the \(k\) one-edges represent distinct parameter orbits.

Switch these \(k\) orbits in any order. After \(t\) switches, \(R\) has \(k-t\) one-edges, so \(m(C_t)\le k-t\). By minority additivity (FM3), \(m(C_0)=m(c)+m(g)=k\); the one-Lipschitz switch theorem (EC8) gives \(m(C_t)\ge k-t\). Thus equality holds throughout and \(C_k\) is successful. The same lower bound yields \(D(C_0)\ge k\), proving (EC13). \(\square\)

This rules out persistence of positive local minima of the minority-defect potential under sufficiently large independent successful padding. The initial product may remain bad: the switches alter its coloring, so the theorem is a legal-edit statement.

### Cartesian-product square avoidance and interaction components

Let \(a,b\ge4\) be even and let \(c,d\) be successful paired-flat legal colorings on \(Q_a,Q_b\). In their independent Cartesian product, a *square-pair orbit* is an antipodal pair of squares whose free directions form one prescribed pair.

**Theorem (square avoidance in successful products).** For every square-pair orbit \(E\) of \(c\boxtimes d\), a color-zero full antipodal geodesic avoids \(E\). More generally, if \(E_1,\ldots,E_t\) are square-pair orbits all supported on direction pairs of \(c\), and \(b+1>2t\), there exists a zero full product geodesic avoiding them simultaneously. The symmetric assertion holds for orbits supported on \(d\).

*Proof.* Choose zero full geodesics \(P,Q\) in \(c,d\). If \(E_j\) is supported on a \(c\)-pair, its external bits in the \(d\)-factor specify a vertex \(y_j\in Q_b\), and its antipodal companion specifies \(\bar y_j\). Along \(Q\), the \(b+1\) vertices are distinct. Thus if \(b+1>2t\), some vertex \(y\) of \(Q\) avoids all pairs \(\{y_j,\bar y_j\}\). Traverse \(Q\) to \(y\), perform the entire \(P\) while keeping the \(d\)-bits fixed at \(y\), then finish \(Q\). Factor independence makes this a zero full antipodal geodesic. Its steps in \(c\) have \(d\)-bits equal to \(y\), hence avoid every \(E_j\), and its steps in \(d\) have directions outside the \(E_j\). The single-orbit case uses \(b\ge4\). Interchanging factors covers an orbit supported in \(d\). \(\square\)

**Corollary (connected pair-interaction obstruction).** Define the undirected interaction graph on direction pairs by joining \(i,j\) when the paired rule \(f_i\) reads some bit of pair \(j\), or conversely. If a successful paired-flat coloring fails square avoidance for some orbit, this interaction graph is connected.

*Proof.* If the graph is disconnected, each rule depends only on bits belonging to its own connected component. The coloring is an independent Cartesian product of at least two paired-flat legal colorings. A zero full geodesic of the product projects to zero full geodesics in every factor, making each factor successful. Group one factor against the product of the remaining factors and apply the preceding theorem. \(\square\)

These results hold with arbitrarily many nonlinear direction rules. The stabilization theorem concerns successful legal edits; the avoidance theorem concerns monochromatic paths in the original successful coloring. A potential failure of universal square avoidance must be supported by interaction-connected pairs rather than by independent successful factors.

### Antipodally twisted perfect-matching involutions and double-occurrence words

Continue with a paired-flat coloring of \(Q_{2m}\), whose paired dimensions are \(P_i=\{i,i'\}\). Write \(S_i\) for the translation that flips both bits in \(P_i\), and put \(\tau=S_1\cdots S_m\), the full antipodal translation. For each \(i\) define a map \(T_i:Q_{2m}\to Q_{2m}\) by traversing the unique color-zero edge among the two incident edges in \(P_i\).

**Theorem (paired-flat permutation representation).** The maps \(T_i\) are fixed-point-free involutions with the following properties:
\[
\boxed{\quad
T_i(x)\text{ differs from }x\text{ in one bit of }P_i,\qquad
\tau T_i\tau=S_iT_i,\qquad
(\tau T_i)^2=S_i.
\quad}\tag{EC3}
\]
They commute with \(S_i\), and the red graph is the edge-disjoint union of the \(m\) perfect matchings defined by the \(T_i\). The blue matching in \(P_i\) is \(S_iT_i\).

Conversely, any family of involutions \(T_i\) satisfying the first two conditions in (EC3), for a fixed pairing of the bits, determines a unique paired-flat antipodally odd vertex-balanced coloring by declaring the \(T_i\)-edges red and the remaining pair edges blue.

*Proof.* On every square with free dimensions \(P_i\), the unique red neighbor of each vertex lies in the same one of the two directions, since the two parallel edges have a common color and the other pair has the complementary color. Hence \(T_i\) is a perfect matching, \(T_i^2=1\), and it commutes with \(S_i\). The antipodal image of its red edge is the blue edge in the same pair; the blue neighbor map is \(S_iT_i\), so \(\tau T_i\tau=S_iT_i\). Multiplication by \(T_i\) gives \((\tau T_i)^2=S_i\).

For the converse, an involution that changes just one of the two bits in \(P_i\) restricts, with all other bits fixed, to a perfect matching of a square. Every perfect matching consisting of square edges selects one of the two parallel edge pairs. Hence the selection is independent of both bits within \(P_i\). The relation \(\tau T_i\tau=S_iT_i\) makes the chosen red direction switch to the complementary member of \(P_i\) at the antipodal outside assignment. The resulting pair rule is antipodally odd, flat on its paired square, and contributes one red and one blue edge at each vertex. Applying this independently for all \(i\) proves the assertion. \(\square\)

**Corollary (unrestricted double-occurrence-word reformulation).** NORI1 is equivalent to the following permutation theorem.

For every \(m\ge2\) and every family \(T_1,\ldots,T_m\) satisfying (EC3), there exist a vertex \(x\in Q_{2m}\) and a word \(w=(i_1,\ldots,i_{2m})\) in which each symbol \(i\in[m]\) occurs twice, such that
\[
\boxed{\qquad T_{i_{2m}}\cdots T_{i_1}(x)=\tau x.\qquad}\tag{EC4}
\]
Indeed each step is a red edge, and its symbol identifies the pair in which a bit flips. If each pair is used twice and the endpoint is antipodal, the two different bits in every pair must each have flipped once, so the path is a full antipodal geodesic. Conversely a red full antipodal geodesic uses both dimensions in every pair once and gives (EC4). The paired-flat closure equivalence (EC2) completes the reduction.

The relations in (EC3) encode antipodal color reversal entirely within permutations, while (EC4) isolates the remaining dimension-simple word problem. A fixed repeated sweep \(w=(1,\ldots,m,1,\ldots,m)\) need not work; the existence quantifier over double-occurrence words is essential.

**Witness for failure of a prescribed double sweep.** For \(m=3\), pair dimensions \((0,3),(1,4),(2,5)\), and take \(f_0=x_1,\ f_1=x_0,\ f_2=x_1\). The word \((0,1,2,0,1,2)\) does not carry any vertex to its antipode. Indeed, to use both directions of pair \(0\), the two visits to \(T_0\) must see distinct values of \(x_1\). Between these visits, only the first \(T_1\) can modify \(x_1\), so that visit must flip \(x_1\). Likewise, to use both directions of pair \(2\), its two visits must see distinct values of \(x_1\); between them only the second \(T_1\) can modify \(x_1\), so it must also flip \(x_1\). Thus the two visits to pair \(1\) both flip the same bit, precluding an antipodal endpoint. Yet the order \((0,2,1,0,1,2)\), from a suitable root, does succeed. This exhibits the distinction between one chosen word and the existential assertion (EC4).




### One-paired-square boundary reduction for hypothetical counterexamples

**Theorem (square-adjacent critical counterexample).** If unrestricted NORI1 fails, there are two paired-flat antipodally odd vertex-balanced colorings \(b,g\) of the same \(Q_{2m}\), \(m\ge2\), and an antipodal pair of square faces \(F,\tau F\) supported on one paired direction set \(P_i=\{i,i'\}\), with the following properties:

1. \(b\) admits no monochromatic full antipodal geodesic, while \(g\) admits one.
2. \(b\) and \(g\) differ only on the eight edges of \(F\cup\tau F\); on these edges their colors are complementary.
3. The bad coloring \(b\) has a full antipodal geodesic with precisely one color-one edge, in a direction of \(P_i\). This exceptional edge belongs to \(F\cup\tau F\).

*Proof.* By the paired-flat lift equivalence, a bad paired-flat coloring exists. A good paired-flat coloring exists as well: begin with any legal odd coloring admitting a monochromatic full geodesic, for example one with all noninitial direction rules equal to the initial vertex bit and the remaining rule reading another bit, and apply the paired lift. By the Boolean parameter theorem (EC1), the configuration graph of paired-flat colorings for the fixed pairing is connected by single antipodal square-pair flips. Follow a path in that graph from a bad coloring to a good one and select adjacent vertices \(b,g\) at a bad-to-good transition. This proves (1)--(2).

Antipodal oddness implies that a monochromatic geodesic in \(g\) may be chosen to have color zero. Let \(P\) be such a geodesic. In each of the squares \(F,\tau F\), its edges alternate zero and one. A full geodesic can use at most two edges of one two-dimensional face, and if it uses two, they must be consecutive along the face: once it leaves the face in an outside dimension, it cannot return without repeating that dimension. Thus a zero geodesic traverses at most one edge of each alternating square. It therefore encounters at most two switched edges, both of them zero in \(g\) and one in \(b\), and all other steps remain zero. Because \(b\) is bad, at least one switched edge occurs. If both occur, the corresponding directions are \(i,i'\). We show that the two exceptional edges are the first and last steps of \(P\). The fixed outside-bit assignments of \(F\) and \(\tau F\) are complementary. Since every outside dimension is traversed just once, encountering both faces forces the path to begin in the first face met and finish in the other. It cannot use either paired dimension before the first exceptional edge: such an earlier step would lie in the same alternating square, and the two steps would have different colors, contrary to the monochromaticity of \(P\) in \(g\). Similarly no paired step can follow the last exceptional edge. Hence the affected edges occupy positions one and \(2m\). Under the cyclic root rotation that moves the first edge of \(P\) to its end, the transferred first edge becomes its antipodal mate and reverses color in \(b\), while all other edge colors are unchanged. The resulting full geodesic has just one color-one edge, coming from the former final edge and belonging to \(F\cup\tau F\). If \(P\) meets only one switched edge, it already has just one color-one edge in \(b\). As \(b\) is bad, the zero-defect case cannot occur. This proves (3). \(\square\)

**Closure consequence.** To establish unrestricted NORI1 it is sufficient to exclude a bad paired-flat coloring which is a single antipodal paired-square flip away from a successful paired-flat coloring. The theorem places a single defect on an antipodal square carrier while retaining vertex balance and the paired-flat constraints. This is a legal-coloring extremal reduction, rather than a restriction to colorings with finitely many nonlinear direction rules.


### Midpoint halfpath convolution identity

Let \(n=2m\ge2\), and let \(c\) be any antipodally odd binary edge coloring of \(Q_n\), not necessarily balanced. For each root \(r\), \(m\)-subset \(S\subset[n]\), and color \(b\in\{0,1\}\), let \(A_b(r,S)\) count ordered length-\(m\) dimension-simple geodesics from \(r\) using the direction set \(S\) with all edges color \(b\). Let \(N_0(c)\) count unoriented monochromatic-zero full antipodal geodesics.

**Theorem (midpoint convolution).**
\[
\boxed{
2N_0(c)=
\sum_{r\in Q_{2m}}\ 
\sum_{\substack{S\subset[2m]\\ |S|=m}}
A_0(r,S)\,A_1(r,S^c).}
\tag{MC1}
\]
Using antipodal oddness, equivalently
\[
\boxed{
2N_0(c)=\sum_{r,S:\,|S|=m}
A_0(r,S)\,A_0(\bar r,S^c).}
\tag{MC2}
\]

*Proof.* An ordered pair of halfpaths counted by one summand in (MC1) consists of a zero path \(P\) from \(r\) to \(u=r\oplus S\) and a one path \(Q\) from \(r\) to \(v=r\oplus S^c\). Antipodal complementation of \(Q\) is a zero path from \(\bar r\) to \(\bar v=u\), since \(\bar r\oplus S^c=r\oplus S\). Reverse that latter halfpath and concatenate it with \(P\); the result is a zero full antipodal geodesic from \(r\) to \(\bar r\) through its middle vertex \(u\). Conversely, every *oriented* zero full antipodal geodesic uniquely splits at its middle vertex into the two halfpaths just described, the second recovered by reversing and antipodally complementing the terminal half. Thus the right side of (MC1) counts oriented zero full geodesics. Each unoriented path has two orientations, proving the factor two. Antipodal complementation sends a one path from \(r\) with direction set \(S^c\) to a zero path from \(\bar r\) with the same direction set, proving (MC2). \(\square\)

**Balanced closure interpretation.** In a vertex-balanced legal coloring of \(Q_{2m}\), the greedy unused-direction argument shows \(A_0(r,\cdot)\) and \(A_1(r,\cdot)\) each have total weight at least \(m!\) at every root. The positive quantities in (MC1) can nevertheless have disjoint support at specified roots, as documented in Article XV. The unrestricted grand theorem is equivalent, via the balanced lift, to asserting that the total bilinear midpoint convolution cannot vanish in a balanced coloring. Equation (MC1) is a quantitative global formulation of the previously established halfpath-overlap criterion, not a solution of that assertion.




## Entropy amplification of hypothetical counterexamples and global counting closure

The freedom in added directions has a strong counting consequence. It persists under perfect balance, using many choices of balanced ordinary colorings in the added fibers. Throughout, logarithms in this subsection are to base two.

For \(N\ge2\), put
\[
L_N=N2^{N-2}.
\]
There are \(L_N\) antipodal edge orbits in \(Q_N\), so the total number of legal odd colorings is \(2^{L_N}\). Let \(B_N\) count those having no monochromatic full antipodal geodesic, and let \(B_N^{\rm bal}\) count the vertex-balanced members. Write \(T_N^{\rm bal}\) for the total number of balanced legal colorings in even dimension.

**Theorem (unrestricted counting amplification).** If a bad legal coloring exists in dimension \(d\), then for every \(N>d\),
\[
\boxed{B_N\ge2^{(N-d)2^{N-2}},\qquad
\frac{B_N}{2^{L_N}}\ge2^{-d2^{N-2}}.}\tag{EA1}
\]

*Proof.* Keep the old \(d\) direction rules independent of the added bits, and color every antipodal edge orbit in every added direction freely. There are \((N-d)2^{N-2}\) independent free bits. Any monochromatic full geodesic in an extension would project onto a monochromatic full geodesic in the old cube, contrary to badness. Distinct free assignments give distinct legal colorings. This is the earlier free-direction extension count, stated in normalized counting form. \(\square\)

### A pairing count for balanced ordinary cube colorings

Let \(a_k\) be the number of ordinary binary edge colorings of \(Q_k\) in which each vertex has \(k/2\) incident edges of each color; antipodal oddness is not imposed here. We use even \(k\ge2\).

**Lemma (elementary Eulerian-orientation count).** For any finite simple \(2r\)-regular graph with \(v\) vertices, its number of Eulerian orientations is at least
\[
\left(\frac{\binom{2r}{r}}{2^r}\right)^v.
\]
Consequently,
\[
\boxed{
a_k\ge
\left(\frac{\binom{k}{k/2}}{2^{k/2}}\right)^{2^k}.
}\tag{EA2}
\]

*Proof.* Pair the \(2r\) incident edges at each vertex. There are
\[
(2r-1)!!=\frac{(2r)!}{2^r r!}
\]
local choices. Any resulting transition system decomposes the undirected edges into closed trails; orient each trail to obtain an Eulerian orientation compatible with those pairings. Thus every transition system admits at least one compatible Eulerian orientation.

For a fixed Eulerian orientation, each vertex has \(r\) incoming and \(r\) outgoing edges. A compatible pairing must pair incoming to outgoing, giving precisely \(r!\) choices per vertex. Counting compatible pairs of a transition system and an Eulerian orientation therefore gives
\[
\#\operatorname{EO}(G)\,(r!)^v
\ge ((2r-1)!!)^v,
\]
which is the asserted bound.

For \(Q_k\), orient a zero edge from the even endpoint to the odd endpoint and a one edge in the reverse direction. Having \(k/2\) edges of each color at every vertex is equivalent to an Eulerian orientation. This is a bijection, proving (EA2). \(\square\)

### Balanced extensions retain full ambient entropy

**Theorem (balanced counting amplification).** Suppose a balanced bad legal coloring exists on \(Q_d\), with \(d\) even. For every even \(k\ge2\), put \(N=d+k\). Then
\[
\boxed{
B_N^{\rm bal}\ge a_k^{\,2^{d-1}}
\ge
2^{\,2^{N-1}\left(\log\binom{k}{k/2}-k/2\right)}.
}\tag{EA3}
\]
In particular,
\[
\boxed{
\log B_N^{\rm bal}
\ge
\bigl(N-d-2\log(N-d+1)\bigr)\,2^{N-2}.
}\tag{EA4}
\]

*Proof.* Write vertices as \((x,z)\in Q_d\times Q_k\), and keep every old direction rule equal to its original rule, independent of \(z\).

For each antipodal pair \(\{x,\bar x\}\) of old vertices, choose an arbitrary balanced ordinary coloring \(g_x\) of the new-direction fiber \(\{x\}\times Q_k\). On the opposite old fiber define
\[
g_{\bar x}(e)=1-g_x(\bar e),
\]
where the antipode on the right is taken in the added \(Q_k\). This gives global antipodal oddness. Both auxiliary fibers are balanced. The old edges supply \(d/2\) zeros at every vertex and the new edges supply \(k/2\), so the full coloring is balanced.

All such extensions are bad by projection to the fixed old directions. The \(2^{d-1}\) old antipodal vertex pairs have independent choices, giving the first bound in (EA3). Substitute (EA2) for the second. Finally
\(\binom{k}{k/2}\ge2^k/(k+1)\), since the largest of the \(k+1\) binomial coefficients is at least their average. This proves (EA4). \(\square\)

The same fiber construction applied to a fixed successful balanced legal four-cube proves, without a counterexample hypothesis,
\[
\log T_N^{\rm bal}=(1-o(1))L_N
\qquad(N\longrightarrow\infty,\ N\text{ even}).
\tag{EA5}
\]
One such four-cube has
\(c_0=x_1,\ c_1=x_0,\ c_2=1-x_1,\ c_3=1-x_0\).
Use this as the old block in the proof and retain the same count of balanced extensions; projection-based badness is unnecessary for counting admissible extensions.

**Corollary (zero-or-full entropy dichotomy).** Define
\[
s_N=\frac{\log(1+B_N)}{L_N},\qquad
s_N^{\rm bal}=\frac{\log(1+B_N^{\rm bal})}{L_N}.
\]
Then
\[
\boxed{
\begin{array}{ll}
\text{NORI1 holds in every dimension}
&\Longrightarrow s_N=s_N^{\rm bal}=0,\\
\text{NORI1 fails in some dimension}
&\Longrightarrow
\displaystyle\lim_{N\to\infty}s_N
=\displaystyle\lim_{\substack{N\to\infty\\N\ {\rm even}}}s_N^{\rm bal}=1.
\end{array}}
\tag{EA6}
\]
In the first line the balanced expression is read in even dimensions.

*Proof.* Universal NORI1 makes both bad counts zero. Any failure supplies a bad coloring for (EA1), forcing \(s_N\to1\). The established balanced counterexample-preserving reduction supplies a fixed even-dimensional balanced bad coloring; (EA4) forces \(s_N^{\rm bal}\to1\). Both expressions have limsup at most one from the total count \(2^{L_N}\). \(\square\)

**Global counting closure criterion.** Each of the following would prove unrestricted NORI1:

1. For some fixed \(\eta>0\) and arbitrarily large even \(N\),
   \[
   B_N^{\rm bal}\le2^{(1-\eta)L_N}.
   \tag{EA7}
   \]
2. Under the uniform distribution on all legal odd colorings,
   \[
   \Pr(\text{bad})\le2^{-a_N2^{N-2}}
   \tag{EA8}
   \]
   along an unbounded sequence, where \(a_N\to\infty\).
3. Under the uniform distribution on balanced legal colorings,
   the same bound (EA8) holds along an unbounded even sequence with
   \(a_N/\log N\to\infty\).

The first follows from (EA6); the second contradicts (EA1). For the third, (EA4) and \(T_N^{\rm bal}\le2^{L_N}\) give the necessary lower bound
\[
\Pr_{\rm bal}(\text{bad})
\ge2^{-[d+2\log(N-d+1)]2^{N-2}}
\tag{EA9}
\]
whenever a fixed balanced bad old block exists.

These are uniform entropy or probability targets. No such upper bound is established here.

### Counterexample amplification inside a single gauge orbit

There is also an orbitwise consequence directly relevant to the recent uniform-gauge second-moment bounds.

**Theorem (positive-entropy bad gauge flats).** If a balanced bad coloring exists in fixed even dimension \(d\), then for arbitrarily large even \(N=d+k\) there is a gauge orbit \(\mathcal O_N\), with a balanced representative, containing at least
\[
\boxed{
2^{\,2^{k-1}-1}=2^{\,2^{-d}M_N-1}
\quad\text{bad colorings},\qquad M_N=2^{N-1}.
}\tag{EA10}
\]
They arise from a linear family of invariant vertex gauges.

*Proof.* Take any balanced bad extension from (EA3). Apply gauges
\[
h(x,z)=a(z),\qquad a(\bar z)=a(z).
\]
All old-direction edge colors remain fixed because their endpoints have the same \(z\). Every resulting coloring is consequently bad by projection. There are \(2^{k-1}\) independent values of \(a\). Two such gauges have the same edge coboundary precisely when their difference is constant, since the full cube is connected. Their distinct resulting colorings therefore number \(2^{2^{k-1}-1}\). The starting representative is balanced; the other gauges are required only to be legal odd colorings. \(\square\)

Hence a uniform bound
\[
\boxed{
\sup_{\substack{\mathcal O\text{ has a}\\\text{balanced representative}}}
\log(1+\#\{\text{bad members of }\mathcal O\})
=o(2^{N-1})
}\tag{EA11}
\]
would also prove NORI1. The known \(O(2^{-N})\) bound on the bad *fraction* of each orbit leaves its permitted bad count at nearly the full orbit entropy. A hypothetical failure supplies the structured large families in (EA10), so the count distinction matters.

**Relation to parity-peeling independence.** Let a parity-peelable family contain \(r\) projective Petrie cycles. Reading a peeling order backward, its first cycle contributes \(N\) vertices and every later one contributes at least \(N-2\) new projective vertices. Thus
\[
r\le\frac{M_N-2}{N-2}.
\tag{EA12}
\]
The common individual success probability is \(p=N/M_N\). Even a largest family certified independent by that criterion has \(rp\le N/(N-2)\). Its joint-failure estimate \((1-p)^r\) alone therefore stays on a constant scale as \(N\) grows. Higher-moment or compression arguments need information from the non-peelable incidence clusters identified in the curvature manuscript.

**Research consequence.** Counterexample-preserving extremization produces a precise global entropy target: save any fixed positive fraction of the \(L_N\) edge-orbit bits when encoding balanced bad colorings. Entropy compression permits repairs that temporarily raise grade, which is compatible with the strict exchange islands proved in the cyclic-variation manuscript. A closing argument still requires an injective encoding, a decoder, and the strict record-count bound (EA7); these objects remain to be constructed.

**Face-network compression milestone.** The subsequent odd-face-network theorem in *Curvature realization, gauge phases and rooted square-defect transport* proves a bad fraction at most \(\exp(-2^{N-O(\sqrt N)})\) inside every invariant gauge orbit, using a preferred face-parity lemma, a block root slide that corrects the seam parity, and entropy covering over all translations. Its disjoint-network construction includes an explicit decoder. The translated edge-noise networks in *Sharp rootwise random cube geodesics by singleton-block second moments* prove the unconditional uniform-random bound \(\Pr(\mathrm{bad})\le\exp(-2^{N-O(N^{1/3})})\), together with a decoder saving \(2^{N-O(N^{1/3})}\) edge-orbit bits. These are proved partial compression bounds. Their guaranteed savings have vanishing normalized size relative to \(L_N\), so the fixed entropy deficit in (EA7) remains open.

The elementary pairing bound was checked by direct balanced-factor enumeration on \(Q_2,Q_4\): the counts are \(2,2970\), exceeding the respective lower bounds \(1,(3/2)^{16}\). The extension and entropy arguments are dimension-uniform proofs independent of these checks.


## Pathwise pseudorandom padding and Gaussian bulk with a retained obstruction

The balance and independent-marginal reductions admit a stronger probabilistic form. Their local independence persists for samples taken at distinct positions of a random full geodesic, including positions far apart along the path. Nevertheless the probability of a monochromatic full path retains a factor determined by the original coloring.

Fix an antipodally odd coloring \(c\) of \(Q_n\), and let \(B(c)\) be its balanced lift on the \(x,y\) directions. For \(k\ge2\), append the independent cyclic gadget
\[
C_{a_j}=a_{j+1},\qquad C_{b_j}=1-a_{j+1}\quad(j\bmod k).
\tag{PP1}
\]
Together with \(C_{x_i}=c_i(x)\), \(C_{y_i}=1-c_i(x)\), this defines \(C_k\) on \(Q_N\), \(N=2n+2k\). Sample a starting vertex uniformly and a full direction order uniformly and independently. Let \(W\) be its binary edge-color word and \(X\) its number of ones.

**Theorem (growing-order path sampling).** For any prescribed \(t\) distinct positions of \(W\), with \(t\le k\), the joint color distribution has total-variation distance at most
\[
1-\frac{2^t(k)_t}{(N)_t}
\ \le\ \frac{2nt}{N}+\binom t2\frac{2k}{N(N-1)}
\tag{PP2}
\]
from \(t\) independent fair bits. Here \((q)_t=q(q-1)\cdots(q-t+1)\). In particular, for fixed \(n\) this distance tends to zero whenever \(t=o(\sqrt N)\).

*Proof.* Call the sampled directions admissible when they are gadget directions drawn from distinct pairs \(\{a_j,b_j\}\). Their probability is \(2^t(k)_t/(N)_t\). Condition on a complete direction order with this property. The color at a sampled occurrence from pair \(j\) is its starting bit \(a_{j+1}\), plus a bit determined by the order and by which member of the pair was chosen. Distinct pairs use distinct independent starting bits. Thus the conditional law is the uniform product law for every admissible order. The total-variation bound follows by coupling. Failure of admissibility requires an old/compensator direction at some sampled position, or both members of one gadget pair at two sampled positions. A union bound gives the second inequality. \(\square\)

**Theorem (full count distribution and Gaussian limit).** Let \(X_B\) be the color-one count on a uniform rooted full geodesic of \(B(c)\). For a uniform order of the \(2k\) gadget directions, let
\[
R=\#\{j:\operatorname{pos}(a_{j+1})\text{ lies strictly between }
\operatorname{pos}(a_j)\text{ and }\operatorname{pos}(b_j)\}.
\tag{PP3}
\]
Then \(X_B\) is independent of the gadget count, and
\[
X\ \stackrel{\mathrm{law}}=\ X_B+k-R+2\operatorname{Bin}(R,1/2),
\tag{PP4}
\]
where the binomial variable has the displayed conditional distribution given the gadget order. For fixed \(c\), as \(k\to\infty\),
\[
\frac{X-N/2}{\sqrt{N/6}}\ \Longrightarrow\ \mathcal N(0,1).
\tag{PP5}
\]

*Proof.* The restrictions of a uniform direction permutation to the two disjoint blocks are independent uniform permutations; their relative interleaving does not alter either block's colors. The starting bits in the two blocks are independent as well.

In gadget pair \(j\), the two sampled colors are complementary unless the direction \(a_{j+1}\) occurs between its two members. In that exceptional case they agree and contribute either zero or two ones with equal probability. Distinct pairs read distinct initial \(a\)-bits, so these choices are conditionally independent. This proves (PP4).

Generate the gadget order by assigning independent continuous uniform priorities to its directions. Each event in (PP3) has probability \(1/3\), whence \(\mathbb ER=k/3\). Its indicator depends only on the priorities of \(a_j,b_j,a_{j+1}\). For \(k\ge4\), nonadjacent indicators on the cyclic index set are independent. Thus \(\operatorname{Var}R=O(k)\), and \(R/k\to1/3\) in probability. Conditional on the order, the centered gadget count is a sum of \(R\) independent fair signs. Its characteristic function after division by \(\sqrt{k/3}\) is
\[
\mathbb E\left[\cos\!\left(t/\sqrt{k/3}\right)^R\right]
\longrightarrow e^{-t^2/2}.
\]
Indeed, the logarithm of the quantity inside the expectation is \(-3t^2R/(2k)+O(R/k^2)\); convergence in probability and boundedness give the limit. The bounded term \(X_B-n\) disappears after normalization, and \(N/6=(n+k)/3\). This proves (PP5). \(\square\)

**Proposition (the rare-event factor is retained).** Define the probability generating functions \(H_C(z)=\mathbb E z^X\) and \(H_B(z)=\mathbb E z^{X_B}\). Then
\[
H_C(z)=H_B(z)\,
\mathbb E\left[z^{k-R}\left(\frac{1+z^2}{2}\right)^R\right],
\qquad
\Pr(X=0)=\Pr(X_B=0)\,2^{-k}\Pr(R=k).
\tag{PP6}
\]
Moreover \(\Pr(R=k)>0\).

*Proof.* The generating-function identity follows from (PP4), with the expression interpreted as a polynomial. A zero gadget count requires \(R=k\) and the zero outcome in every pair, giving the second identity. To see positivity, assign distinct priorities in \((0,1)\) to the \(a_j\). If \(a_{j+1}\) is later than \(a_j\), place \(b_j\) later than \(a_{j+1}\); otherwise place \(b_j\) earlier than \(a_{j+1}\). All these inequalities hold on a nonempty open set of priorities. \(\square\)

Consequently this padding preserves monochromatic full-geodesic existence in both directions. Projection gives one implication. Conversely, any zero full path in \(c\) lifts to \(B(c)\) by placing each \(y_i\) before or after the old path where its color is zero; the gadget has a zero full path by the positivity just proved. Concatenation yields a zero full path in \(C_k\).

**Theorem (connected version with almost maximal monochromatic faces).** Replace the gadget in (PP1) by the guarded gadget from the face-extremization theorem:
\[
g_j=
\begin{cases}
\beta(x),&\text{all }b_\ell,\ \ell\ne j,\text{ are equal},\\
a_{j+1},&\text{otherwise},
\end{cases}
\qquad C_{a_j}=g_j,\quad C_{b_j}=1-g_j.
\tag{PP7}
\]
Here \(k\ge3\), and \(\beta\) is odd and sensitive to every old bit, as in that theorem. Its random full color word is within total-variation distance
\[
\epsilon_k\le (N+1)k2^{2-k}
\tag{PP8}
\]
of the word for (PP1). Hence (PP2) holds with the additional error \(\epsilon_k\), and the Gaussian limit (PP5) remains valid. These colorings are perfectly balanced, have connected undirected influence graph, contain a monochromatic \(k\)-face, and preserve badness by projection.

*Proof.* Couple the two colorings using the same starting vertex and direction order. At each of the \(N+1\) visited vertices, each guard has probability \(2^{2-k}\): conditional on the direction order, its starting \(b\)-bits remain independent and uniform after the deterministic prefix flips. A union bound over vertices and guards proves (PP8). If no guard is active, the full words agree. The other properties are those established for the guarded construction. \(\square\)

**Closure consequence and scope.** If NORI1 fails, it has counterexample sequences satisfying all the preceding balance, connectivity, large-face and growing-order path-sampling properties, whose full-path color counts converge to the Gaussian law (PP5). Thus a bulk central-limit argument, even combined with these properties, leaves the essential rare-event positivity question unresolved. Formula (PP6) identifies what remains: complete-path compatibility is retained as a multiplicative factor from the fixed original block. A useful probabilistic closure argument must establish positivity at this scale, or supply a structural estimate that rules out a vanishing original factor. These are conditional consequences of a hypothetical counterexample, not constructions of counterexamples.

An independent enumeration verified (PP4) and its generating-function coefficients on all 384 rooted full paths of the four-direction gadget and all 46,080 rooted full paths of the six-direction gadget. The arguments above are dimension-uniform.


## Balanced second-turn discrepancy forces beyond-half geodesics

Let \(N=2m\ge4\), and let \(c\) be a vertex-balanced antipodally odd edge coloring of \(Q_N\). For each vertex \(v\), put
\[
D(v)=\{j:c_j(v)=0\},\qquad |D(v)|=m.
\]
Define the total Boolean influence of the direction functions by
\[
\mathcal I(c)=\sum_{i,j=1}^N
\Pr_v[c_j(v)\ne c_j(v\oplus e_i)].
\tag{BH1}
\]
Let \(M_{m+1}^0(c)\) count unoriented zero-colored direction-simple paths of length \(m+1\).

**Theorem (quantitative beyond-half guarantee).**
\[
\boxed{
M_{m+1}^0(c)\ge
2^{N-3}(m-2)!\,\mathcal I(c)
\ge N2^{N-3}(m-2)!.
}
\tag{BH2}
\]
The same bound holds for color one. In particular every balanced odd coloring has a monochromatic geodesic strictly longer than half the dimension. The bound is attained in dimension four.

*Proof.* Count rooted ordered two-step zero paths \((u,u^i,u^{ij})\) for which direction \(j\) is one-colored at \(u\). Their number is
\[
T_0=\sum_{u,i:\,c_i(u)=0}|D(u^i)\setminus D(u)|.
\tag{BH3}
\]
The directions are automatically distinct, since a direction-\(i\) edge has the same color at its two ends. Define \(T_1\) by the same sum restricted to one-colored direction-\(i\) edges. Equal cardinalities of \(D(u)\) and \(D(u^i)\) give
\[
|D(u^i)\setminus D(u)|
=|D(u)\setminus D(u^i)|
=\tfrac12|D(u^i)\mathbin{\triangle}D(u)|.
\]
Antipodal complementation exchanges zero and one edges and replaces each \(D(v)\) by its complement. Therefore \(T_0=T_1\), and summing the last display over \(u,i\) yields
\[
\boxed{T_0=T_1=2^{N-2}\mathcal I(c).}
\tag{BH4}
\]

Extend each two-step zero path counted by \(T_0\) to an ordered zero path of length \(m\). After \(t<m\) steps at least \(m-t\) zero directions remain unused, so there are at least \((m-2)!\) extensions. Let \(S\) be the \(m\) directions of such an extension. Its second direction \(j\) lies outside \(D(u)\); hence the two \(m\)-sets \(S,D(u)\) differ. Choose, by a fixed deterministic rule, some \(a\in D(u)\setminus S\). Prepend the zero edge \(u^a u\). The resulting path has \(m+1\) distinct directions and is all zero.

This map from extended ordered paths to ordered \((m+1)\)-paths is injective: delete the first edge of the output to recover the extension, including its distinguished initial two-step path. Thus there are at least \(T_0(m-2)!\) ordered zero paths of length \(m+1\). Dividing by two proves the first inequality in (BH2).

For each \(j\), antipodal oddness implies
\[
\sum_i\Pr_v[c_j(v)\ne c_j(v^i)]\ge1.
\]
Indeed, follow any fixed full direction order from \(v\) to \(\bar v\). The value of \(c_j\) changes at least once, and averaging the number of changes over the uniform starting vertex gives the displayed sum. Summing over \(j\) yields \(\mathcal I(c)\ge N\). Antipodal translation supplies the color-one assertion. \(\square\)

**Sharpness audit in dimension four.** Enumeration of all 65,536 antipodally odd colorings found 48 vertex-balanced colorings. Their minimum zero-path count at length three is eight, equal to (BH2), and their minimum count \(T_0\) is sixteen, equal to (BH4) with \(\mathcal I=4\). The proof does not rely on this enumeration.

**Relation to averaging and to padding.** The usual minimum-degree argument reaches \(m\) from every root. The extra step in (BH2) uses a globally forced discrepancy between the direction sets available at neighboring vertices. Balance turns that discrepancy into the symmetric count (BH4), and oddness gives its positive lower bound. This retains information absent from a count of incident zero degrees alone.

For the unguarded balanced cyclic padding \(C_k\) of a fixed \(c\) on \(Q_n\), direct summation of influences gives
\[
\mathcal I(C_k)=2\mathcal I(c)+2k,\qquad
\mathcal I(C_k)-N=2(\mathcal I(c)-n).
\tag{BH5}
\]
Thus arbitrary padding preserves the total excess influence above its balanced minimum. A dimension-uniform theorem forcing that excess to diverge along every sequence of balanced counterexamples would close NORI1, by (BH5). Such a theorem is presently unproved; (BH2) establishes the first extension beyond the halfpath threshold, without asserting iteration to full length.


## Weighted Leader--Long surplus and polarized-product invariance

Leader and Long prove that, for any fixed order of the cube directions, the average length of a longest increasing geodesic ending at a vertex of a cube subgraph is at least its average degree. See I. Leader and E. Long, *Long geodesics in subgraphs of the cube*, Discrete Mathematics 326 (2014), 29--33, Theorem 2.1, doi:10.1016/j.disc.2014.02.013. Here increasing refers to the direction order. The update proof gives the following weighted refinement, which identifies the surplus retained by this averaging argument.

**Theorem (weighted surplus identity).** Let \(G\) be a spanning subgraph of \(Q_d\); isolated vertices are allowed. Give direction \(i\) weight \(w_i\ge0\), and process the directions in a fixed order. Let \(L_{<i}(v)\) be the maximum weight of an increasing path ending at \(v\) using only earlier directions, and let \(L(v)\) be the final maximum. Then
\[
\boxed{
\sum_v L(v)=
2\sum_{uv\in E(G)}w_{\operatorname{dir}(uv)}
+\sum_i\ \sum_{\substack{uv\in E(G)\\\operatorname{dir}(uv)=i}}
\bigl(|L_{<i}(u)-L_{<i}(v)|-w_i\bigr)_+.
}
\tag{LLS1}
\]

*Proof.* Direction-\(i\) edges form a matching. Across one such edge, if the previous maxima are \(a,b\), the new maxima are
\(\max(a,b+w_i)\) and \(\max(b,a+w_i)\).
A newly appended direction cannot repeat an earlier direction, so these are the path maxima. Their total increase is
\(2w_i+(|a-b|-w_i)_+\).
Unmatched vertices keep their previous values. Summing all updates proves (LLS1). \(\square\)

**Theorem (product invariance).** Form \(G'=G\square Q_k\), retain the old direction weights, and give the new directions arbitrary nonnegative weights \(u_1,\ldots,u_k\). For any interleaving of the new directions with a fixed old order,
\[
L_{G'}(v,z)=L_G(v)+\sum_{a=1}^ku_a.
\tag{LLS2}
\]
Consequently the normalized difference between the two sides of the weighted Leader--Long lower bound is unchanged:
\[
\frac{\sum_{v,z}L_{G'}(v,z)-2\sum_{e\in E(G')}w_e}{2^{d+k}}
=
\frac{\sum_vL_G(v)-2\sum_{e\in E(G)}w_e}{2^d}.
\tag{LLS3}
\]

*Proof.* Projection of an increasing path to \(G\) bounds its old weight by \(L_G(v)\); its new weight is at most \(\sum_a u_a\). Conversely, take a maximizing old path ending at \(v\) and insert every new direction in its designated position in the full direction order, choosing its starting bits to end at \(z\). All new edges are present, so this realizes the upper bound. The average weighted degree also increases by \(\sum_a u_a\), proving (LLS3). \(\square\)

**Application to the polarized-facet reduction.** In the one-source padding \(C_{n+a}=x_j\), the zero-edge graph of the facet \(x_j=0\) is precisely \(G\square Q_k\), where \(G\) is the old zero-edge graph of that facet. Hence the facet becoming almost monochromatic introduces no additional normalized surplus in this averaging argument, even with arbitrary nonnegative direction weights. The old deficit remains after the auxiliary contribution is subtracted. A closing refinement must control the endpoint direction sets or another compatibility quantity beyond this longest-increasing-path average. The beyond-half theorem above supplies one such additional quantity, the change of available zero directions across an edge.



## Rooted halfpath-support rigidity and maximal monochromatic-face packing

Let \(n=2m\ge4\), and let \(c\) be a vertex-balanced antipodally odd coloring of \(Q_n\). For a root \(u\), color \(b\), and \(m\)-subset \(S\subset[n]\), let \(A_b(u,S)\) count ordered monochromatic-\(b\) geodesics using the directions \(S\). Put \(\mathcal F_b(u)=\{S:A_b(u,S)>0\}\).

**Theorem (singleton support iff monochromatic half-dimensional face).** The family \(\mathcal F_b(u)\) contains just one \(m\)-set if and only if the \(m\)-face through \(u\) whose free directions are \(D_b(u)=\{i:c_i(u)=b\}\) is monochromatic color \(b\). In this case
\[
\boxed{\mathcal F_b(u)=\{D_b(u)\},\quad A_b(u,D_b(u))=m!.}\tag{RF1}
\]
This face is an isolated connected component of the color-\(b\) edge graph.

*Proof.* At each vertex the color-\(b\) degree is \(m\), so any monochromatic color-\(b\) direction-simple path of length \(t<m\) can be extended: at least \(m-t>0\) incident directions remain unused. Every initial direction \(i\in D_b(u)\) therefore belongs to the support of an \(m\)-path. If this support is a singleton \(\{S\}\), then \(D_b(u)\subseteq S\), so \(S=D_b(u)\).

Inductively all vertices \(v=u\oplus\mathbf1_T\) of the face, \(T\subseteq S\), can be reached by zero-or-one monochromatic paths using only directions in \(T\). At a reached vertex with \(|T|<m\), if any color-\(b\) edge had direction \(j\notin S\), taking it and extending to \(m\) steps would yield a root-\(u\) halfpath with a direction set other than \(S\). Hence all \(m\) color-\(b\) edges at \(v\) have directions in \(S\), making every internal edge of the face color \(b\) and every boundary edge the other color. The face is an isolated component. Conversely, if this face is monochromatic, vertex balance forces all boundary edges to have the other color. All color-\(b\) halfpaths are confined to the face and may traverse its \(m\) free directions in all \(m!\) orders. \(\square\)

**Theorem (maximal-face packing under badness).** If \(N_0(c)=0\), no monochromatic-zero \(m\)-face intersects a monochromatic-one \(m\)-face. Writing \(H_b\) for the number of color-\(b\) monochromatic \(m\)-faces, one has
\[
\boxed{H_0=H_1\le2^{m-1}.}\tag{RF2}
\]
At least \(2^{2m-1}\) vertices have \(|\mathcal F_b(u)|\ge2\), for each \(b\).

*Proof.* At any common vertex \(u\) of opposite-color \(m\)-faces, their free directions are the complementary sets \(D_0(u),D_1(u)\). Their monochromatic halfpaths therefore combine, by the midpoint gluing lemma, to form a zero full antipodal geodesic.

Distinct monochromatic \(m\)-faces of the same color are disjoint: intersecting faces would need the same free directions at a shared vertex, then would be identical. Opposite-color faces must also be disjoint in a bad coloring. Antipodal oddness bijects the two types, so \(H_0=H_1=H\). Their \(2H\) disjoint sets of \(2^m\) vertices fit inside \(2^{2m}\), proving the bound. By (RF1), vertices with singleton halfpath support are precisely the vertices in such faces, yielding the final conclusion. \(\square\)

**Same-color midpoint convolution.** Reversing both halfpaths in the preceding midpoint identity yields
\[
\boxed{2N_0(c)=\sum_{u\in Q_{2m}}\sum_{|S|=m}A_0(u,S)A_0(u,S^c).}\tag{RF3}
\]
Both factors count zero halfpaths from a common midpoint whose direction sets are complementary. This holds even without vertex balance, and shows that every root's zero halfpath-support family must be complement-free in a hypothetical bad coloring.

These global assertions do not assume any special construction for an unrestricted hypothetical counterexample. They link maximal monochromatic faces, concentrated midpoint supports, and the sought complementary-halfpath overlap.


Maximal half-face separation. In vertex-balanced Q_(2m), every color-b monochromatic m-face uses all m available b incident edges at each vertex, so every boundary edge has the opposite color. A monochromatic zero m-face F and monochromatic one m-face G, if disjoint, cannot have adjacent vertices: their joining boundary edge would be forced to have both colors. For a hypothetical bad coloring, F and the antipode of every other zero m-face Fprime are disjoint, and therefore separated by Hamming distance at least two. Let S,T be the free direction sets of F,Fprime and let a,a-prime be their fixed bit assignments. The distance equals the number of jointly fixed directions h outside S union T on which a_h equals a-prime_h. Thus there are at least two such directions. In particular abs(S intersect T) >= 2 for every pair of zero maximal faces. Their free direction sets form a pairwise two-intersecting family, and their fixed bit labels satisfy a stronger agreement condition. This global obstruction holds for any hypothetical balanced counterexample.


### Kleitman anticode bound for all maximal monochromatic half-faces

Let \(c\) be a hypothetical bad vertex-balanced antipodally odd coloring of \(Q_{2m}\), \(m\ge2\). Let \(A\subseteq Q_{2m}\) be the union of all monochromatic-zero \(m\)-faces, and \(H\) their number.

**Theorem (diameter obstruction).** Every two vertices in \(A\) have Hamming distance at most \(2m-2\), and therefore
\[
\boxed{
H\le \left\lfloor 2^{-m}
\sum_{j=0}^{m-1}\binom{2m}{j}\right\rfloor
=\left\lfloor2^{m-1}-2^{-m-1}\binom{2m}{m}\right\rfloor.}
\tag{KA1}
\]
In particular the respective upper bounds on \(H\) for \(m=2,3,4,5\) are \(1,2,5,12\), strengthening the elementary \(2^{m-1}\) bound.

*Proof.* Let \(\bar A\) be the vertexwise antipode of \(A\), which is precisely the union of the monochromatic-one \(m\)-faces. The earlier maximal-face theorems show that in a bad coloring \(A\cap\bar A=\varnothing\) and, more strongly, no cube edge joins \(A\) to \(\bar A\). If some \(u,v\in A\) had Hamming distance \(2m\), then \(u=\bar v\in\bar A\), contradiction. If their distance were \(2m-1\), then \(u\) would be adjacent to \(\bar v\in\bar A\), another contradiction. Thus the diameter of \(A\) is at most \(2m-2\).

By the Kleitman diameter theorem (D. J. Kleitman, *On a combinatorial conjecture of Erdős*, 1966), any subset of the binary \(2m\)-cube with diameter at most \(2m-2=2(m-1)\) has at most the volume of a Hamming ball of radius \(m-1\), equal to \(\sum_{j=0}^{m-1}\binom{2m}{j}\). The \(H\) monochromatic-zero maximal faces are vertex-disjoint and each contains \(2^m\) vertices. Consequently \(H2^m=|A|\) satisfies the displayed bound. The binomial identity follows by symmetry. \(\square\)

The theorem is an all-dimensional necessary condition on hypothetical balanced counterexamples, not a reduction to colorings that happen to have a maximal monochromatic face. It quantifies the previously identified antipodal separation of all maximal-face vertices. Because known counterexample-preserving lifts need not create an \(m\)-face, this face-count obstruction alone does not settle NORI1.



### Backward extension of halfpaths and rootwise escape

Let \(n=2m\ge4\) and let \(c\) be a vertex-balanced antipodally odd coloring. For \(b\in\{0,1\}\) let \(D_b(u)=\{i:c_i(u)=b\}\), let \(A_b(u,S)\) count ordered length-\(m\) color-\(b\) geodesics rooted at \(u\) using the \(m\)-set \(S\), and let \(L_b^{m+1}\) count ordered color-\(b\) \((m+1)\)-geodesics.

**Theorem (backward-extension count).**
\[
\boxed{L_b^{m+1}=\sum_{u\in Q_{2m}}\sum_{|S|=m}
|D_b(u)\setminus S|A_b(u,S).}\tag{BE1}
\]
A vertex \(u\) is the second vertex of a monochromatic color-\(b\) path of length \(m+1\) if and only if its color-\(b\) halfpath support \(\mathcal F_b(u)=\{S:A_b(u,S)>0\}\) is not a singleton, equivalently \(u\) is outside every monochromatic color-\(b\) \(m\)-face.

*Proof.* Every unused color-\(b\) direction \(j\in D_b(u)\setminus S\) supplies a zero-or-one colored edge \(u^j\to u\) of color \(b\). Prepending that edge to the ordered \(m\)-path yields an \((m+1)\)-geodesic. Every such oriented longer path has a unique decomposition given by its first edge and its remaining \(m\)-path. This proves the count. Since \(D_b(u)\) has size \(m\) and the halfpath-support theorem gives nonempty support, the sum at \(u\) is zero only when every supported \(S\) equals \(D_b(u)\), which the singleton-face rigidity theorem characterizes. \(\square\)

**Corollary (rootwise escape obstruction).** In any hypothetical bad balanced coloring, for **every** vertex \(u\) at least one color \(b\) admits a monochromatic \((m+1)\)-geodesic with \(u\) its second vertex:
\[
\boxed{|\mathcal F_0(u)|\ge2\quad\text{or}\quad|\mathcal F_1(u)|\ge2.}\tag{BE2}
\]
Indeed simultaneous singleton supports would be the complementary sets \(D_0(u),D_1(u)\), producing a full zero antipodal geodesic by midpoint gluing.

For each color separately, the number of vertices in the second position of some monochromatic \((m+1)\)-geodesic is at least
\[
\boxed{2^{2m}-2^m\left\lfloor2^{-m}
\sum_{j=0}^{m-1}\binom{2m}{j}\right\rfloor.}\tag{BE3}
\]
This follows because the exceptional vertices with singleton support are precisely those in maximal monochromatic faces, whose number is bounded by the preceding Kleitman anticode theorem. Thus in a hypothetical counterexample, both colors have spatially widespread beyond-half paths; the rootwise distribution, rather than length-increment iteration, is the remaining global compatibility target.



### Double-escape population and a local non-gluing example

Let \(n=2m\ge4\), let \(c\) be a hypothetical bad vertex-balanced antipodally odd coloring, and call \(u\) *\(b\)-escaping* if it is the second vertex of a monochromatic color-\(b\) geodesic of length \(m+1\). Equivalently, \(|\mathcal F_b(u)|\ge2\), by the backward-extension and singleton-face theorems.

**Theorem.** The number of vertices escaping in both colors is
\[
\boxed{2^{2m}-2^{m+1}H\ge\binom{2m}{m},}\tag{DE1}
\]
where \(H\) is the number of monochromatic-zero \(m\)-faces.

*Proof.* Vertices not escaping in color zero are precisely the union \(A\) of those \(H\) disjoint zero faces, so \(|A|=2^mH\). Antipodal oddness identifies the vertices not escaping in color one with \(\bar A\). The two collections are disjoint in a bad coloring because complementary singleton supports at the same root give a monochromatic full antipodal geodesic. Thus both-color escape occurs precisely outside \(A\cup\bar A\). The previous Kleitman diameter theorem bounds \(|A|\) by
\(\sum_{j=0}^{m-1}\binom{2m}j=2^{2m-1}-\frac12\binom{2m}m\), proving (DE1). \(\square\)

**Double escape alone does not force rootwise midpoint overlap.** A reproducible \(Q_6\) example is obtained from three sign-opposed direction pairs \((x_i,y_i)\), \(i=0,1,2\). For each \(i\), list the four remaining direction bits in increasing order as a number \(z\) from 0 to 15. Define an odd Boolean function \(f_i\) by reading the bit at index \(z\) from the respective mask \((33,232,59)\) for \(z<8\), and setting \(f_i(z)=1-f_i(15-z)\) for \(z\ge8\). Color the paired directions by \(c_{x_i}=f_i,\ c_{y_i}=1-f_i\). The coloring is undirected, antipodally odd, and vertex-balanced.

At root \(u=3\), enumeration of all ordered monochromatic three-geodesics gives support masks
\[
\mathcal F_0(3)=\{7,11,26,35,42,44,56\},
\quad
\mathcal F_1(3)=\{11,14,41,42,44,49\}.
\]
Both colors escape, but these families contain no complementary pair of six-bit supports. Thus the midpoint convolution at this root is zero even though both escaping paths exist. This is a rootwise obstruction, not a NORI1 counterexample; the global overlap must be established by coupling different roots.


## Walk potentials, derivative-run erasure, and extremal-lift invariance

The toolkit's Minty argument optimizes an additive walk score and erases nonprofitable excursions. The graph construction in *Odd girth and frustration of switch component quotients* realizes a cube analogue: for an antipodal walk \(W\), its length \(L(W)\) plus completed turn count
\[
g(W)=\sum_{t<L}[w_t\ne w_{t+1}]+[w_L=w_1]
\tag{ME1}
\]
is the length of an odd closed walk in the graph consisting of the zero cube edges and all antipodal matching edges. For even dimension, its minimum is the odd girth of that graph. Under vertex balance the graph is regular. This retains ordinary graph distances and allows local Bellman inequalities.

Here we identify the cost of erasing a repeated direction, and show that the extremal lifts preserve the full tradeoff between walk length and completed turn count.

**Lemma (twisted subsequence monotonicity).** If \(v\) is a nonempty subsequence of a binary word \(w\), then \(g(v)\le g(w)\).

*Proof.* Extend \(w\) by the rule \(w_{t+L}=1-w_t\). Its adjacent comparisons have period \(L\), and their sum in one period is \(g(w)\). For the chosen subsequence positions \(s_1<\cdots<s_r\), compare successively \(w_{s_1},\ldots,w_{s_r},w_{s_1+L}\). Each comparison is bounded by the sum of adjacent comparisons on the corresponding interval. The intervals partition a period. Their sum is \(g(v)\), proving the claim. \(\square\)

Fix an integer \(\lambda\ge1\), and minimize
\[
\Phi_\lambda(W)=\lambda L(W)+g(W)
\tag{ME2}
\]
over all cube walks joining any root to its antipode, with minimum length used to break ties.

**Proposition (finite walk optimization and ordinary erasure).** A minimizer exists. It repeats no cube vertex, and no two of its vertices belong to the same antipodal pair except its two endpoints.

*Proof.* A full geodesic is a candidate of finite value, while \(\Phi_\lambda\ge\lambda L+1\). Thus only finitely many bounded-length walks need be considered. If a vertex repeats, delete the intervening closed subwalk. The color word becomes a subsequence, so \(g\) does not increase and length decreases, contradicting minimality.

If a proper subwalk joins two antipodal vertices, its ordinary variation is at most that of the whole walk. Its completed turn count is the least odd integer at least its ordinary variation. The whole completed count is also odd and is at least that variation, so the subwalk has no greater completed count. Choosing the subwalk as the new antipodal walk reduces length, again a contradiction. \(\square\)

**Theorem (direction-folding derivative-run bound).** Suppose a walk has direction word \(A\,i\,U\,i\,B\), with no occurrence of \(i\) in \(U\). Remove the two displayed \(i\)-steps and translate the intervening segment across direction \(i\), obtaining a legal walk \(W'\) with the same endpoints and length \(L-2\). Along the old middle segment, let
\[
h_t=\partial_i c_{j_t}(v_t)
\]
be the color change caused by this translation. Let \(r(h)\) be the number of nonempty runs of ones in this derivative word. Then
\[
\boxed{g(W')-g(W)\le2r(h).}
\tag{ME3}
\]
Consequently, in a minimizer of (ME2), every such repeated-direction interval satisfies
\[
\boxed{r(h)\ge\lambda+1.}
\tag{ME4}
\]
In particular, minimizing length plus completed turn count forces at least two separated active-derivative runs inside every repeated-direction interval.

*Proof.* First delete the colors of the two displayed \(i\)-edges from the word of \(W\), giving a virtual word \(v\); subsequence monotonicity gives \(g(v)\le g(W)\). The legal folded word differs from \(v\) by XOR with the derivative word \(h\) on the middle segment and zero elsewhere. There is at least one edge outside that segment: otherwise the two displayed \(i\)-steps would give even \(i\)-parity for an antipodal walk. The padded derivative word has \(2r(h)\) cyclic changes. Only at those comparisons can the completed turn word change, proving (ME3).

For a minimizing walk, the shorter folded walk cannot have equal or smaller \(\Phi_\lambda\). Hence \(g(W')-g(W)>2\lambda\). Both grades are odd, so their difference is at least \(2\lambda+2\). Combine with (ME3). \(\square\)

Thus the direction-erasure condition is measured by ordered runs of square derivatives along the intervening walk. Ordinary loop erasure is automatic; dimension erasure requires this further transport control.

### The full length--turn frontier survives balanced extremization

For an odd coloring \(c\) of \(Q_n\), define
\[
\ell_c(r)=
\min\{L(W):W\text{ joins some }x\text{ to }\bar x,\ g(W)\le r\},
\tag{ME5}
\]
with value \(+\infty\) for an empty family. The root is variable. Let \(B(c)\) be the balanced lift on \(Q_{2n}\):
\(B_{x_i}=c_i(x)\), \(B_{y_i}=1-c_i(x)\).

**Theorem (frontier preservation).** For every \(r\ge1\),
\[
\boxed{\ell_{B(c)}(r)=\ell_c(r)+n.}
\tag{ME6}
\]
For the independent cyclic-gadget extension \(C_k\) on \(N=2n+2k\) directions,
\[
\boxed{\ell_{C_k}(r)-N=\ell_c(r)-n.}
\tag{ME7}
\]
Consequently, for every \(\lambda\ge1\), the normalized minimum walk potential is preserved:
\[
\boxed{
\min_W[\lambda(L(W)-N)+g(W)-1]\text{ on }C_k
=
\min_W[\lambda(L(W)-n)+g(W)-1]\text{ on }c.
}
\tag{ME8}
\]

*Proof.* Project any lifted antipodal walk to its original directions. It remains an antipodal walk with the same old colors. Its completed grade does not increase, by subsequence monotonicity. Each auxiliary direction occurs an odd positive number of times, so projection removes at least the number of auxiliary directions. This gives the lower bounds in (ME6),(ME7).

For the converse, take an old antipodal walk \(W\). Root sliding along the concatenation of \(W\) and its antipodal image cyclically rotates its completed comparison word, preserving length and grade. Cut immediately after a changed comparison, and use antipodal complementation if needed. The resulting walk starts and ends with color zero, has ordinary variation \(g(W)-1\), and retains its original length and grade.

For each \(y_i\), its edge color \(1-c_i(x)\) has opposite values at the two old endpoints. Insert the \(y_i\)-step before or after \(W\), wherever that color is zero. Auxiliary steps affect none of the old rules or one another. The lifted word has zero prefixes and suffixes around the old word and hence the same completed grade. Its length increases by \(n\).

The independent cyclic gadget has a zero full geodesic, as established by the between-position construction in the pathwise padding theorem. Insert one such gadget geodesic among the zero prefix steps. This adds \(2k\) steps and no grade. The upper bounds follow. Equality of the normalized minima follows either from the two walk maps or by minimizing the frontier formulas. \(\square\)

**Connected guarded version.** For fixed \(c\) on \(Q_n\), \(n\ge3\), the connected guarded balanced lift also satisfies (ME7) for all sufficiently large \(k\), simultaneously for every \(r\).

*Proof.* The projection lower bound still holds. Choose one minimizing old walk for each finite frontier value needed: there are finitely many such values, since a full geodesic has grade at most \(n\), and \(\ell_c(r)=n\) for every \(r\ge n\). For one selected old walk of length \(L\), use the preceding construction with a fixed zero gadget geodesic and fixed direction order. Its \(b\)-starting bits are free: the unguarded gadget rules ignore them. At every visited vertex they are still uniform after fixed prefix flips. The probability that any guard is active anywhere along this lifted walk is at most
\[
(L+n+2k+1)\,k\,2^{2-k}.
\]
For sufficiently large \(k\) this is less than one. Choose starting \(b\)-bits avoiding every guard. The guarded walk then has the same colors, length and grade as its unguarded version. Apply this separately to the finite collection of frontier witnesses. Infinite frontier values remain infinite by projection. \(\square\)

**Closure plan.** A bound forcing the normalized minimum in (ME8) to vanish for balanced colorings would prove NORI1: vanishing forces both \(L=N\) and \(g=1\), and root sliding gives a monochromatic full geodesic. The extremal reductions preserve this entire optimization problem, including the connected guarded version. The new local obstruction (ME4) identifies what an erasure proof must overcome: separated derivative runs on every repeated-direction interval. A proof coupling these runs across the minimizing walk, using balance and the complementary antipodal edge rules, remains open.

An independent evaluator verified (ME3) on 5,000 direction-fold configurations in dimensions three through seven. The proofs apply to all stated dimensions.


Universal double-escape equivalence. Universal two-way balanced double-escape lift. In Q6 use paired direction bits a_i,b_i for i modulo 3. Let g_(a_i)=a_(i+1)+a_(i+2)+b_(i+1) modulo 2 and g_(b_i)=1-g_(a_i). Each pair is oppositely colored at every vertex; the rules ignore their own bits and depend on three other bits, so g is legal antipodally odd and vertex balanced. Starting at zero and traversing (a0,b1,b0,a2,a1,b2) gives a zero full antipodal geodesic. The gadget has no monochromatic three-face: a hypothetical such face must have one free direction in each a_i,b_i pair; changing either free bit of pair i toggles g_(a_(i-1)), hence changes the color of the selected free edge of pair i-1, contradiction. For any original legal odd coloring c of Q_n and integer k>=0, take the already-proved two-way vertex-balanced bounded-Fourier lift ctilde_k on Q_(2n+2k) and form independent-block product C_k=ctilde_k box g on Q_(2n+2k+6). A zero full geodesic in the product projects to one in c. Conversely a zero full geodesic in c lifts to one in ctilde_k, and concatenating with the exhibited zero geodesic in g gives one in the product. Thus C_k has a zero full geodesic if and only if c does. The product is vertex-balanced and odd. Its monochromatic maximal half-face would need all n+k free directions of the corresponding color in the first block and all three in the gadget block, forcing a monochromatic three-face of g; impossible. By the previously proved singleton halfpath support and backward extension theorems, at every vertex both colors admit multiple halfpath direction sets and geodesics of length N/2+1 with that vertex second. Every direction rule has Fourier degree <=max(n-1,3), independent of k; balance kills all top permissible Walsh coefficients. Consequently unrestricted NORI1 is equivalent to its restriction to balanced even-dimensional colorings having no monochromatic half-dimensional face, equivalently double escape at every vertex. The reduction preserves badness in arbitrarily high dimensions and is not a proof of NORI1.


### Independent-block product geodesic count and irreducible minimal counterexamples

Let \(c\) and \(g\) be arbitrary binary edge colorings of \(Q_a\) and \(Q_b\). Form their independent-block product \(C=c\Box g\), meaning a direction in either factor retains its original edge-color rule and ignores the other block.

**Theorem (product path multiplicativity).**
\[
\boxed{N_0(C)=2\binom{a+b}{a}N_0(c)N_0(g).}\tag{PG1}
\]
In particular \(N_0(C)>0\) if and only if both factors have a zero monochromatic full antipodal geodesic.

*Proof.* An oriented full zero geodesic of \(C\) projects to an oriented full zero geodesic of each factor. Conversely, any two such factor paths combine into a full zero product geodesic in any of the \(\binom{a+b}{a}\) interleavings of their two fixed direction orders. These operations are inverse, so the number of oriented zero product geodesics is
\[
\binom{a+b}{a}\,[2N_0(c)]\,[2N_0(g)].
\]
Every unoriented full geodesic has two orientations, proving (PG1). \(\square\)

If the two factors are legal antipodally odd colorings, so is their product. Thus any hypothetical bad independent-block product must have a bad factor. Consequently a **minimum-dimensional bad odd coloring** is indecomposable as a nontrivial independent-block product of legal odd colorings. This makes precise the distinction between an irreducible proof obstruction and arbitrary balanced or double-escape padding.

For the six-direction gadget (DG1), an enumeration of its \(2^6\cdot6!\) oriented full paths gives \(N_0(g)=216\). Consequently for a legal coloring \(d\) of \(Q_a\),
\[
\boxed{N_0(d\Box g)=432\binom{a+6}{6}N_0(d).}\tag{PG2}
\]
This quantitative identity strengthens the two-way product argument: when the base is bad, the product is bad; when it is good, the number of zero antipodal geodesics is amplified by the displayed combinatorial factor. The statement applies in all dimensions and does not require Fourier or balance hypotheses.



## A sharp gap above the minimum size of balanced monochromatic components

**Theorem (cube minimum-degree size gap).** Let \(X\ne\varnothing\) be a vertex subset of \(Q_d\) (or \(Q_D\) with \(D\ge d\)) whose induced cube subgraph has minimum degree at least \(d\). Then either \(X\) is a \(d\)-dimensional face and \(|X|=2^d\), or
\[
\boxed{|X|\ge 3\cdot2^{d-1}.}\tag{CG1}
\]
For \(d\ge2\) the second bound is attained by the Cartesian product of the six-cycle on \(Q_3\setminus\{000,111\}\) with \(Q_{d-2}\); for \(d=1\), a three-vertex path attains the bound.

*Proof.* Induct on \(d\), with a secondary induction on the ambient dimension to discard fixed directions. For \(d=0\), a singleton is a zero-face, and every larger set has at least two vertices. For \(d\ge1\), choose a direction in which \(X\) meets both opposite facets; if no such direction remains after discarding fixed directions, the set is a singleton, contrary to its positive minimum degree. Let \(X_0,X_1\) be the two sections of \(X\) in that direction, identified with subsets of \(Q_{D-1}\). Each has minimum internal degree at least \(d-1\), because at most one neighbor of each vertex lies in the other section. By induction each section is either a \((d-1)\)-face of \(2^{d-1}\) vertices or has at least \(3\cdot2^{d-2}\) vertices.

If neither is minimal, their total has at least \(3\cdot2^{d-1}\) vertices. Otherwise suppose \(X_0=F\) is a \((d-1)\)-face. Every vertex of \(F\) has internal degree \(d-1\), so minimum degree \(d\) forces its crossing neighbor into \(X_1\); thus \(F\subseteq X_1\) under the section identification. If \(X_1=F\), then \(X\) is a \(d\)-face. Otherwise let \(Y=X_1\setminus F\). Every vertex of \(Y\) has no crossing neighbor in \(X_0=F\), and has at most one neighbor in \(F\), since any vertex outside a cube face has at most one neighbor in that face. Thus the induced graph of \(Y\) has minimum degree at least \(d-1\). The usual cube minimum-degree lower bound, proved by the same induction, gives \(|Y|\ge2^{d-1}\). Hence \(|X|\ge|X_0|+|F|+|Y|\ge3\cdot2^{d-1}\). \(\square\)

**Corollary (monochromatic component gap).** In any vertex-balanced binary edge coloring of \(Q_{2m}\), each connected component of either monochromatic edge graph has either \(2^m\) vertices and is an isolated monochromatic \(m\)-face, or at least
\[
\boxed{3\cdot2^{m-1}}
\tag{CG2}
\]
vertices. In particular, in the counterexample-preserving double-escape reduction (DG2), neither color has a minimal face component, and each has at most \(\lfloor 2^{m+1}/3\rfloor\) components.

*Proof.* Every vertex has degree \(m\) in each monochromatic edge graph. Its component vertex set has minimum induced-cube degree at least \(m\), so (CG1) applies. If the component has \(2^m\) vertices its set is a face; the component already contains all \(m\) internal edges at each vertex, making it an isolated monochromatic face. Conversely such a face is a component. If no such component exists, divide the total \(2^{2m}\) cube vertices by the lower bound (CG2). \(\square\)

This global expansion gap applies to all balanced colorings, with no assumption on local readers, Fourier spectra, or dimensions of hypothetical counterexamples. It quantifies how far a component must grow once its rooted halfpath support escapes a single maximal face. The bound alone does not force complementary halfpaths, since the component vertex sets may be large while their geodesic midpoint supports remain separated.



### Attribution and proof-status clarification for the minimum-degree gap

The cube minimum-degree gap (CG1), though given above with a self-contained induction, is a previously established theorem of **Andris Ambainis and Jevgenijs Vihrovs**, *Size of Sets with Small Sensitivity: A Generalization of Simon's Lemma*, Theory and Applications of Models of Computation (TAMC 2015), Lecture Notes in Computer Science **9076**, pp. 122–133, DOI **10.1007/978-3-319-17142-5_12**; available also as ECCC report TR14-077 (2014). In their language, a subset of \(Q_D\) with sensitivity at most \(D-d\) has cardinality either \(2^d\) or at least \(3\cdot2^{d-1}\). The sensitivity bound is equivalent to minimum induced degree at least \(d\). Thus (CG1) is **the Ambainis–Vihrovs first gap theorem**, not a new theorem.

The NORI1-specific **corollary** derived here remains: each color component in a vertex-balanced \(Q_{2m}\) is either an isolated monochromatic \(m\)-face of size \(2^m\), or contains at least \(3\cdot2^{m-1}\) vertices; in the double-escape reduction, there are no components of the first type. The interpretation and interaction with the earlier halfpath-support and universal-lift results are the contribution to Article XV. Any later presentation should explicitly credit Ambainis and Vihrovs for the gap itself.


Wu and Yang, arXiv:2607.19276v1 (2026), proved the ordinary monochromatic antipodal path conjecture but explicitly left the geodesic strengthening open. Their rook-label construction uses ordinary monochromatic graph connectivity, which is transitive. Our legal odd Q3 coloring c0=x2, c1=1+x0, c2=1+x1 shows that monochromatic geodesic reachability is not transitive: zero geodesics join 000 to 110 and 110 to 011, but no zero geodesic joins 000 to 011. Thus no direct replacement of ordinary components by geodesic-reachability classes is possible. The path theorem makes the minimum monochromatic antipodal walk length finite, of the form n+2e with integer e>=0. NORI1 requires e=0, and any counterexample would have e>=1.

Shortest-walk square-derivative budget. The 2026 Wu-Yang monochromatic antipodal path theorem ensures that a shortest monochromatic antipodal walk P exists for every legal odd coloring. Let its length be L=n+2e. For each direction i appearing 2k_i+1 times, consider the 2k_i intervals between successive occurrences. Every interval contains an active square derivative delta_i c_j(v)=c_j(v) xor c_j(v^i)=1 on one of its traversed j edges. Indeed, write P=A i B i C and remove the two displayed i steps while translating B in bit i; this yields a shorter antipodal walk. If all i-derivatives along B vanish, the shorter walk remains monochromatic, contradicting shortest length. Intervals for each i are disjoint, hence summing derivative incidences over each path-edge occurrence and each direction i gives at least sum_i 2k_i = L-n=2e. This is a uniform walk-erasure obstruction, not proof of e=0. Example Q4 coloring c0=x1, c1=x0+x2+x3, c2=x0+x1+x3, c3=x0+x1+x2 has all-zero antipodal path rooted at vertex 1 of direction word 0,2,0,3,0,1 but no zero geodesic at that root. Each of the two successive direction-zero intervals contains a nonzero square derivative. The repeated-direction budget complements the Minty-style fold potential in Article XV.


## Global root-changing near-antipodal shortcuts

Let \(n\ge3\), and let \(c\) be any antipodally odd coloring. By Wu--Yang's path theorem choose a shortest monochromatic-zero antipodal path
\(P=(v_0,\ldots,v_L)\), \(v_L=\bar v_0\), minimizing length over **all endpoint roots**. Write \(L=n+2e\).

**Theorem (root-changing shortcut).** For \(0\le i<j\le L\),
\[
\boxed{d_H(v_i,v_j)=n\ \Longrightarrow\ j-i=L,}\tag{SC1}
\]
and
\[
\boxed{d_H(v_i,v_j)=n-1\ \Longrightarrow\ j-i\ge L-1.}\tag{SC2}
\]

*Proof.* If \(v_j=\bar v_i\), the zero subpath from \(v_i\) to \(v_j\) would be a shorter antipodal path unless \(i=0,j=L\).

If \(d_H(v_i,v_j)=n-1\), the vertices \(v_j,\bar v_i\) are adjacent. If the joining edge is zero, append it to the zero segment \(v_i\to\cdots\to v_j\), producing a zero antipodal walk of length \(j-i+1\). If the joining edge is one, its antipodal mate from \(v_i\) to \(\bar v_j\) is zero. Append that mate to the reversed zero segment \(v_j\to\cdots\to v_i\), giving a zero antipodal walk of the same length. In both cases shortest-length minimality forces \(j-i+1\ge L\). Any closed subwalk can be erased. \(\square\)

**Corollary (rainbow-window extraction).** Any monochromatic antipodal path containing a contiguous block of \(n-1\) pairwise distinct directions implies the existence of a monochromatic *full antipodal geodesic*, possibly from a different root. In particular, if \(e\ge1\), every block of \(n-1\) successive steps along a globally shortest monochromatic antipodal path must repeat some direction.

*Proof.* The endpoints of the block differ in \(n-1\) directions. The unique edge from one to the antipode of the other, or its antipodal mate, has the desired color. Adding it to the block or its reversal gives a monochromatic \(n\)-step antipodal geodesic. \(\square\)

**Corollary (buried central repetition for one detour).** If \(L=n+2\), a unique direction appears three times and all others once. Write the three occurrence positions \(1\le a<b<c\le n+2\). Each of the four length-\((n-1)\) windows must contain at least two of these appearances. Their median \(b\) therefore belongs to the intersection of the four windows, giving
\[
\boxed{4\le b\le n-1.}\tag{SC3}
\]
In particular this shortest-walk configuration requires \(n\ge5\). This global restriction is stronger than mere active square derivatives and uses the freedom to change antipodal roots, which fixed-root shortening lacks.

The theorem is a dimension-uniform necessary condition on shortest monochromatic antipodal paths; it does not yet force \(e=0\) in arbitrary dimension.



### Systolic anticode of a shortest monochromatic antipodal path

Let \(n\ge3\), and let \(P=(v_0,\ldots,v_L)\) be a globally shortest monochromatic antipodal path for an antipodally odd coloring. By the root-changing shortcut theorem (SC1)--(SC2),
\[
\boxed{\operatorname{diam}_H\{v_1,\ldots,v_{L-1}\}\le n-2.}\tag{SA1}
\]
Indeed any two of these vertices have index difference at most \(L-2\), hence cannot be antipodal or nearly antipodal. In particular their projected classes in the folded cube form a simple essential cycle whose inner vertices are a Hamming anticode.

**Theorem (topological shortest-path length bound).** Write \(n=2m\) or \(n=2m+1\). Then
\[
\boxed{
L\le
\begin{cases}
1+\displaystyle\sum_{j=0}^{m-1}\binom{2m}{j},& n=2m,\\[2mm]
1+\displaystyle2\sum_{j=0}^{m-1}\binom{2m}{j},& n=2m+1.
\end{cases}
}\tag{SA2}
\]
Together with \(L\equiv n\pmod2\), this bounds the minimum detour excess of any legal coloring.

*Proof.* The interior set contains \(L-1\) distinct vertices (the chosen path is shortest), and has Hamming diameter at most \(n-2\) by (SA1). The classical Kleitman diameter/anticode theorem bounds a subset of \(Q_{2m}\) of diameter at most \(2m-2\) by the Hamming-ball volume \(\sum_{j=0}^{m-1}\binom{2m}{j}\). In \(Q_{2m+1}\), the diameter threshold \(2m-1\) gives the sharp maximum \(2\sum_{j=0}^{m-1}\binom{2m}{j}\), the size of two adjacent radius-\((m-1)\) balls with overlapping centers handled in their union description. Apply those established inequalities to the interior set. \(\square\)

**Corollary (geodesic closure for \(Q_4\) from the ordinary-path theorem).** For \(n=4\), (SA2) gives \(L\le6\). Parity forces \(L=4\) or \(6\). If \(L=6\), the path uses one direction three times and each other direction once. The median repeated occurrence would have to lie in \([4,n-1]=[4,3]\) by (SC3), impossible. Therefore \(L=4\): every legal odd \(Q_4\) coloring has a monochromatic antipodal geodesic.

The preceding is an alternative proof of this known finite-dimensional case. The all-dimensional anticode consequence (SA1) is a new application to our shortest-path extremization, not a claim to have discovered Kleitman's established diameter theorem. It remains far from proving \(L=n\) for unrestricted dimension \(n\).



### Balance and global path minimality give a one-third volume bound

The codimension-one extension lemma is already established in earlier NORI research. The contribution here is its combination with a **monochromatic induced-path boundary count** and perfect vertex balance.

Let \(n=2m\ge4\), and let \(c\) be a vertex-balanced antipodally odd coloring of \(Q_n\). Choose a globally shortest monochromatic-zero antipodal path \(P=(v_0,\ldots,v_L)\); its existence follows from Wu--Yang, and antipodal symmetry makes both colors equivalent. Put \(X=\{v_1,\ldots,v_{L-1}\}\), \(Y=\bar X\), and \(Z=Q_n\setminus(X\cup Y)\).

**Theorem (balanced shortest-walk cut bound).**
\[
\boxed{L-1\le
\left\lfloor\frac{m2^{2m}-2}{3m-2}\right\rfloor.}\tag{BC1}
\]
Thus \(L\le(1/3+O(1/m))2^{2m}\) in the balanced regime.

*Proof.* By the known root-changing near-antipodal completion lemma, \(X\cap Y=\varnothing\) and no cube edge connects \(X\) to \(Y\). Indeed an internal antipodal pair would give a shorter zero antipodal subpath, and an internal near-antipodal pair could be completed at one of its two roots to a shorter zero antipodal walk.

The color-zero induced subgraph on \(X\) has only the \(L-2\) internal successive edges of \(P\). Any other color-zero chord would replace a longer subpath and shorten \(P\).

All vertices have color-zero degree \(m\). Consequently the number of zero edges crossing from \(X\) to its complement is
\[
m|X|-2(L-2)=(m-2)|X|+2.\tag{BC2}
\]
None reaches \(Y\), so all reach \(Z\). Each vertex in \(Z\) has zero degree \(m\), hence can receive at most \(m\) crossing zero edges from \(X\). Thus
\[
(m-2)|X|+2\le m|Z|=m(2^{2m}-2|X|).
\]
Rearrangement proves (BC1). \(\square\)

**Corollary (combined anticode/cut bound).** The previously proved anticode constraint gives
\[
\boxed{
L-1\le\min\left\{
\sum_{j=0}^{m-1}\binom{2m}{j},
\left\lfloor\frac{m2^{2m}-2}{3m-2}\right\rfloor
\right\}.}\tag{BC3}
\]
The cut bound improves the Kleitman volume bound starting in dimension \(n=12\). The asymptotic fractions are respectively \(1/3\) and \(1/2\).

**Status.** This is an unconditional dimension-uniform upper bound on the length of a shortest monochromatic antipodal path in a balanced coloring; it does not prove NORI1, and does not automatically furnish an equivalent bound in an original coloring before balanced lifting. The new counting ingredient is that a minimal monochromatic antipodal path is an induced path **in its own color graph**, and its interior is separated from its antipodal image.



### Stronger shortest-path expansion from cubical two-step bypass rigidity

Retain a vertex-balanced antipodally odd coloring of \(Q_n\), \(n=2m\ge4\), and a globally shortest monochromatic-zero antipodal path \(P=(v_0,\ldots,v_L)\). Put \(X=\{v_1,\ldots,v_{L-1}\}\), \(Y=\bar X\), \(Z=Q_n\setminus(X\cup Y)\), and \(t=|X|=L-1\).

**Lemma (external two-neighbor rigidity).** Every \(z\in Z\) has at most two color-zero neighbors on \(X\). If there are two, they are vertices \(v_i,v_{i+2}\) two steps apart on \(P\), and \(z\) is the other corner of their unique dimension-two square. Consequently, at most \(L-3=t-2\) vertices of \(Z\) have two color-zero neighbors in \(X\).

*Proof.* If \(z\) were joined by zero edges to \(v_i\) and \(v_j\) with \(j-i>2\), replacing the color-zero subpath of \(P\) between them by \(v_i,z,v_j\) would shorten the antipodal zero walk by at least two steps, contradicting global minimality. Distinct neighbors of \(z\) lie in the same cube bipartition class, hence their path indices have the same parity. Therefore any two such indices differ by two. Three indices would include a pair differing by at least four, impossible. For each consecutive two-step subpath \(v_i,v_{i+1},v_{i+2}\), the endpoints differ in two directions (as \(P\) is vertex-simple), so there is only one other common cube neighbor besides \(v_{i+1}\). Thus there is at most one possible double-neighbor vertex for each of the \(L-3\) internal two-step subpaths. \(\square\)

**Theorem (improved antipoidal shortest-path volume bound).**
\[
\boxed{
L-1\le\left\lfloor\frac{2^n-4}{m-1}\right\rfloor
\quad (n=2m\ge4).}\tag{BP1}
\]
In particular \(L=O(2^n/n)\), a factor of order \(n\) below the ambient cube size, with a stronger exponent-independent prefactor than the preceding one-third bound.

*Proof.* As in the preceding theorem, established near-antipodal root-changing completion gives \(X\cap Y=\varnothing\) and no cube edge from \(X\) to \(Y\). The color-zero induced graph on \(X\) contains only its \(L-2\) successive path edges. Therefore the number of zero edges leaving \(X\) into \(Z\) is
\[
B=m|X|-2(L-2)=(m-2)t+2.
\]
Let \(N\) be the number of vertices \(z\in Z\) incident to at least one such edge, and let \(D\) count vertices with two. The lemma gives \(B=N+D\) and \(D\le t-2\), hence
\[
N\ge (m-2)t+2-(t-2)=(m-3)t+4.
\]
But \(N\le |Z|=2^n-2t\), so
\[
(m-1)t\le2^n-4,
\]
proving (BP1). \(\square\)

**Corollary (best combined geometric bounds).** With the classical Kleitman anticode bound, the previous simple cut bound, and (BP1), one has
\[
L-1\le
\min\left\{
\sum_{j=0}^{m-1}\binom{2m}{j},\
\left\lfloor\frac{m2^n-2}{3m-2}\right\rfloor,\
\left\lfloor\frac{2^n-4}{m-1}\right\rfloor
\right\}.
\tag{BP2}
\]
The square-bypass bound improves the Kleitman bound from dimension eight onward. It uses only the **existing** codimension-one shortcut, the induced-path property of shortest monochromatic walks, balance, and the two-common-neighbor geometry of cube squares. This is a global length bound and not yet a proof that the minimum length equals \(n\).

**Generalization.** If the color-zero degree is at least \(d\ge2\) at every vertex of the path, the same argument gives
\[
(d-1)(L-1)\le2^n-4,
\]
without needing vertex balance elsewhere. In a legal antipodally odd coloring, the balanced case \(d=n/2\) gives the displayed strongest uniform version.



### Antipodally separated color neighborhoods of globally shortest monochromatic paths

Let \(c\) be a vertex-balanced antipodally odd coloring of \(Q_n\), \(n=2m\ge6\). Let \(P=(v_0,\ldots,v_L)\) be a globally shortest monochromatic-zero antipodal path, over all roots; the shortest color-one length equals \(L\) by antipodal complementation. Put \(X=\{v_1,\ldots,v_{L-1}\}\), \(Y=\bar X\), and \(Z=Q_n\setminus(X\cup Y)\). Let
\[
N=\{z\in Z:\ c(v_i z)=0\text{ for some }1\le i<L\}
\]
denote the exterior color-zero neighborhood of \(X\).

**Theorem (four-vertex antipodal neighborhood overlap).**
\[
\boxed{|N\cap\bar N|\le4.}\tag{AN1}
\]
The overlap can occur only at the two endpoints \(v_0,\bar v_0\) and at the other two corners of the squares associated with the first and last directions of \(P\).

*Proof.* Suppose \(z\in N\cap\bar N\). Choose \(i,j\in\{1,\ldots,L-1\}\) with red edges \(zv_i\) and \(\bar z v_j\). By antipodal oddness, the edge from \(z\) to \(\bar v_j\) is blue. From \(z\), traverse this blue edge to \(\bar v_j\), follow the blue antipodal image of the subpath of \(P\) from \(v_j\) to \(v_i\), and finish with the antipodal blue mate of the red edge \(v_i z\), joining \(\bar v_i\) to \(\bar z\). The result is a monochromatic-blue antipodal walk from \(z\) to \(\bar z\) of length
\[
\boxed{|i-j|+2.}\tag{AN2}
\]
Its length cannot be less than the global shortest \(L\). But \(|i-j|\le L-2\) for internal indices, so necessarily \(|i-j|=L-2\) and \(\{i,j\}=\{1,L-1\}\).

Write \(a,b\) for the first and last path directions. They are distinct: otherwise \(v_1=\bar v_{L-1}\), an internal antipodal pair contradicting shortestness. The two internal vertices \(v_1,\bar v_{L-1}\) equal \(v_0^a,v_0^b\), so they have only the common cube neighbors \(v_0,v_0^{a,b}\). The reversed extreme pair similarly has common neighbors \(\bar v_0,\bar v_0^{a,b}\). This gives at most four candidates for \(z\), proving (AN1). \(\square\)

**Theorem (improved shortest-path volume bound).**
\[
\boxed{
L-1\le\left\lfloor\frac{2^n-4}{n-4}\right\rfloor
\qquad (n=2m\ge6).}\tag{AN3}
\]
Thus \(L=O(2^n/n)\), with half the leading coefficient of the previous square-bypass bound (BP1).

*Proof.* Put \(t=|X|=L-1\). As previously established, \(X\cap\bar X=\varnothing\) with no cube edge joining these sets; the color-zero edges inside \(X\) are only its \(t-1\) successive path edges. Vertex balance therefore gives \((m-2)t+2\) red edges from \(X\) to \(Z\). The square-bypass lemma says each \(z\in Z\) has at most two red neighbors in \(X\), and at most \(t-2\) vertices have two; hence
\[
|N|\ge(m-3)t+4.
\]
Antipodal complementation preserves \(Z\), and (AN1) gives
\[
2|N|-4\le |N\cup\bar N|\le |Z|=2^n-2t.
\]
Combining yields
\(2(m-3)t+8-4\le2^n-2t\), or
\[
2(m-2)t\le2^n-4.
\]
Since \(2(m-2)=n-4\), this is (AN3). \(\square\)

**Combined bound and provenance.** The best of the Kleitman anticode, initial balanced boundary and two-neighbor bound, and (AN3) applies. The antipodal neighborhood bound improves the anticode bound already from \(n=8\), and the asymptotic upper fraction is now \(1/n\), rather than \(1/3\) or \(2/n\). The **codimension-one completion lemma is old**; what is added here is a color-sensitive antipodal separation of an entire *neighborhood* of a globally extremized path, followed by a balanced expansion count. It is not yet a proof that the shortest path has no repeated directions.



### Layered antipodal separation for every shortest monochromatic path

Let \(c\) be an antipodally odd coloring of \(Q_n\), and let \(P=(v_0,\ldots,v_L)\) be a globally shortest zero antipodal path. Put \(X=\{v_1,\ldots,v_{L-1}\}\), \(Z=Q_n\setminus(X\cup\bar X)\). For an integer \(r\ge1\), let
\[
U_r=\{z\in Z:\text{there is a zero path of length at most }r\text{ from }z\text{ to }X\}.
\]
For \(z\in U_r\cap\overline{U_s}\), choose zero paths of lengths \(a\le r,b\le s\) from \(z\) to \(v_i\), and from \(\bar z\) to \(v_j\), with \(1\le i,j<L\).

**Theorem (antipodal attachment separation).** Any such attachments satisfy
\[
\boxed{a+b+|i-j|\ge L.}\tag{LA1}
\]
If \(r+s<L\), their anchor indices obey
\[
\boxed{|i-j|\ge L-r-s,\qquad
\min(i,j)\le r+s-1,\quad
\max(i,j)\ge L-(r+s-1).}\tag{LA2}
\]
Thus antipodal overlap of \(r\)- and \(s\)-step monochromatic neighborhoods of the interior of a shortest antipodal path can only arise from attachments at the first or last \(r+s-1\) interior positions.

*Proof.* Concatenate the zero path from \(z\) to \(v_i\), the zero segment of \(P\) from \(v_i\) to \(v_j\), and the zero path from \(v_j\) to \(\bar z\). This is a zero antipodal walk from \(z\) to \(\bar z\) of length \(a+|i-j|+b\). Global shortestness implies this length is at least \(L\), proving (LA1). Since internal indices range between \(1,L-1\), rearranging yields (LA2). Neither the argument nor its inequality requires antipodal color reversal once the shortest color-zero antipodal path is available.

**Corollary (bounded Hamming endpoint collars).** If \(r+s<L\) and \(z\in U_r\cap\overline{U_s}\), then
\[
\boxed{z\in B_H(v_0,r+s+\min(r,s)-1)
\ \cup\ B_H(\bar v_0,r+s+\min(r,s)-1).}\tag{LA3}
\]
*Proof.* If \(i<j\), (LA2) gives \(i\le r+s-1\) and \(L-j\le r+s-1\). Hence
\(d_H(z,v_0)\le a+i\le2r+s-1\).
Also \(d_H(z,\bar v_j)\le b\le s\) and
\(d_H(\bar v_j,v_0)\le L-j\le r+s-1\),
so \(d_H(z,v_0)\le r+2s-1\). Take the smaller bound. If \(i>j\), the analogous argument centers the Hamming ball at \(\bar v_0\). \(\square\)

For \(r=s=1\), (LA2) forces \(\{i,j\}=\{1,L-1\}\); cube common-neighbor geometry gives the sharper earlier bound \(|U_1\cap\overline{U_1}|\le4\). This proof also corrects an unnecessary attribution in the earlier AN1 argument: the overlap constraint itself is a shortest-*red*-path fact, while antipodal oddness is used in the earlier result to exclude arbitrary cube edges between the path interior and its antipode.

**Role in closure.** The inequalities apply in any dimension and at every neighborhood depth, providing a precise obstruction to placing monochromatic reachability layers on both sides of the antipodal involution. They do not alone imply geodesic existence, because arbitrary balanced counterexample-preserving lifts can have detour excess independent of ambient dimension, making pure volume bounds too weak.



## Square-pattern budget in perfectly balanced antipodally odd cubes

Let \(n=2m\ge4\), and let \(c\) be any vertex-balanced antipodally odd binary edge coloring of \(Q_n\). Classify every undirected square by the number of its color-one edges. Put \(H_k\) for the number of squares with \(k\) color-one edges. Further split the two-one-edge count \(H_2=H_2^{\mathrm{opp}}+H_2^{\mathrm{adj}}\), according to whether the two color-one edges are opposite (parallel) or adjacent.

**Theorem (opposite-edge-square identity).**
\[
\boxed{
H_0=H_4,\qquad H_1=H_3,\qquad
H_2^{\mathrm{opp}}=m2^{n-2}+2H_4,
\qquad
H_2^{\mathrm{adj}}=2^n\binom m2-4H_4-2H_3.
}
\tag{SQ1}
\]
In particular **every** vertex-balanced odd \(Q_{2m}\) contains at least
\[
\boxed{m\,2^{n-2}}\tag{SQ2}
\]
squares whose edges alternate in pairs of opposite colors around the boundary (the two color-one edges are parallel, as are the two color-zero edges).

*Proof.* The cube has \(Q=2^{n-2}\binom n2\) squares. Antipodal complementation maps a square with \(k\) one-edges to a different square with \(4-k\), proving \(H_k=H_{4-k}\). At every vertex there are \(m\) incident one-edges, so the total number of unordered one-colored incident edge pairs (one-colored wedges) is \(W=2^n\binom m2\). Each one-color wedge determines one square. A square with four one-edges contributes four such wedges; a square with three contributes two; a square with two adjacent one-edges contributes one; all remaining patterns contribute none. Therefore
\[
W=4H_4+2H_3+H_2^{\mathrm{adj}}.
\]
Likewise
\(Q=2H_4+2H_3+H_2^{\mathrm{adj}}+H_2^{\mathrm{opp}}\).
Eliminating the latter unknown gives
\[
H_2^{\mathrm{opp}}=Q-W+2H_4.
\]
Because \(n=2m\),
\(Q-W=2^{n-2}[\binom{2m}{2}-4\binom m2]=m2^{n-2}\).
This proves all identities. \(\square\)

**Defect transport interpretation.** When a color-one edge in direction \(i\) belongs to such a two-and-two opposite-edge square and both adjacent transverse edges are zero, its parallel direction-\(i\) partner is also one. The two zero transverse edges transport the nonzero direction-\(i\) defect to a parallel edge without changing color. If the parallel \(i\)-edge is zero instead, the three zero edges provide a length-three monochromatic bypass of the original defect. This distinction gives a global supply of transport squares but does not ensure that the transport chain reaches a zero \(i\)-edge; closed trapped components remain possible.

**Audits.** The square identity was checked across all 48 vertex-balanced odd colorings of \(Q_4\), where the square counts are \(H_0=H_4=1\), \(H_1=H_3=4\), \(H_2^{\mathrm{adj}}=4\), \(H_2^{\mathrm{opp}}=10\), and in random balanced odd colorings of \(Q_6\) and \(Q_8\). The theorem is dimension-uniform; these checks are not used in the proof.

The identity establishes a rigid local-square budget for every balanced counterexample, a candidate global constraint for the repeated-direction/defect-transport problem rather than another restricted-class NORI1 proof.



### A balanced odd obstruction to single-direction defect transport closure

The abundant opposite-colored-square count (SQ1) does **not** imply that transporting a one-colored direction-\(i\) edge defect along two zero-colored transverse edges eventually reaches a zero-colored direction-\(i\) edge. A legal balanced \(Q_4\) counterexample is
\[
\boxed{
c_0=x_2,\quad c_1=1-x_2,\quad
c_2=x_0,\quad c_3=1-x_0
\qquad(\bmod2).}\tag{ST1}
\]
Every rule ignores its own bit, flips under antipodal complementation, and each direction pair \((0,1)\), \((2,3)\) contributes one zero and one one edge at every vertex. Thus the coloring is vertex-balanced and antipodally odd; as known, it has monochromatic full antipodal geodesics.

Consider a direction-zero one-colored edge \(e\), where \(x_2=1\). At both its endpoints, the perpendicular direction 1 is zero-colored. Directions 2 and 3 have opposite colors at the two endpoints (their rules depend on \(x_0\)), so neither can provide a pair of zero transverse edges. Thus its only permitted all-zero transverse transport is across direction 1, to the parallel direction-zero edge \(e^1\). But \(c_0=x_2\), so \(e^1\) is still color one. Transporting again returns to \(e\). Each direction-zero defect is therefore trapped in a two-edge transport component containing no zero direction-zero edge.

**Interpretation.** Balance guarantees, by a pigeonhole argument, at least one common zero transverse direction across any one-colored edge: each endpoint has \(m\) zero lateral directions among \(2m-1\). The transport graph may nevertheless be a closed component containing no zero edge of the defective direction, even with the legal antipodal symmetry. The all-dimensional square budget forces many such transport squares but not a successful fixed-direction repair. A possible grand-theorem closure proof must combine *different defective directions*, different paths, or the global topological parity obstruction rather than iterating a single color-preserving square move to termination.



### Four endpoint-square exchanges for minimal antipodal paths

Let \(c\) be an antipodally odd binary coloring of \(Q_n\). Choose a globally shortest monochromatic-zero antipodal path \(P=(v_0,\ldots,v_L)\). Write \(u=v_0\), let \(a,b\) be its first and last directions, and put \(z=u^{a,b}\). The established internal-antipodal shortcut shows \(a\ne b\). Write \(A=c_b(u^a)\), \(B=c_a(u^b)\). Then \(c_a(u)=0\) and \(c_b(u)=1\), using antipodal oddness on the last edge.

**Endpoint-square exchange lemma.** If \((A,B)\ne(1,0)\), the following is a second monochromatic-zero antipodal path with the same length \(L\):
\[
\begin{array}{c|l}
(A,B)&\text{new vertex sequence}\\
(0,0)&u^b,z,v_1,v_2,\ldots,v_{L-1}\\
(1,1)&v_1,v_2,\ldots,v_{L-1},\bar z,\bar v_1\\
(0,1)&z,v_1,v_2,\ldots,v_{L-1},\bar z.
\end{array}
\]
The pattern \((1,0)\) gives no exchange by these three operations.

*Proof.* In the first construction, the new initial edges have colors \(c_a(u^b)=B=0\) and \(c_b(u^a)=A=0\), and its terminal vertex is \(\overline{u^b}=v_{L-1}\). In the second, the new terminal edges have colors \(1-B=0\) and \(1-A=0\) by antipodal oddness, and the last vertex is \(\bar v_1\). In the third the new initial and final edge colors are \(A=0\) and \(1-B=0\), with antipodal endpoints \(z,\bar z\). Retained internal edges remain zero. Any repeated vertex in a constructed walk would permit a shorter zero antipodal walk, violating the global choice of \(L\); thus the walks are paths. \(\square\)

**Neighborhood implication.** Let \(X=\{v_1,\ldots,v_{L-1}\}\), and let \(N\) be its exterior zero neighborhood in the complement of \(X\cup\bar X\). The prior antipodal-overlap theorem shows \(N\cap\bar N\subseteq\{u,\bar u,z,\bar z\}\). The pair \(\{u,\bar u\}\) is always present, while \(\{z,\bar z\}\) is present precisely when \((A,B)=(0,1)\). Hence \(|N\cap\bar N|\) is two or four, and the extra overlap encodes a length-preserving root exchange.

**No forced blocked square.** The legal odd \(Q_4\) coloring \(c_0=x_1\), \(c_1=c_2=c_3=x_0\) has 24 unoriented zero antipodal geodesics. For each oriented zero geodesic its endpoint-square pattern belongs to \(\{(0,0),(0,1),(1,1)\}\), never \((1,0)\). Indeed direction 0 must be first or last: if it were internal, the first and last other-direction edge colors would impose opposing values of \(x_0\). If direction 0 is first, \(A=0\); if last, \(B=1\). Thus minimizing path length alone cannot force a blocked endpoint square.

This exchange lemma should be compared with the prior endpoint-rotation arguments in Article X before treating it as a distinct proof mechanism. It gives a finite move graph on globally minimal witnesses, not a demonstration that any move reduces the detour excess.


### Probabilistic closure status: exponential smoothing and a marginal-counting barrier

The random-cube geodesics Subsection now proves independent-round amplification, (SR1)--(SR5). Uniformly over every legal baseline, fixed-root prescribed-word failure under antipodal edge-orbit noise has order at most \(\exp[-c n\rho]\), for an absolute \(c>0\). A root-star obstruction gives the matching exponential order for monochromatic prescriptions. Under uniform legal coloring, the global bad fraction is at most \(\exp[-2^{n-O(\log n)}]\); the associated failure-list encoding saves \(2^{n-O(\log n)}\) bits.

The same Subsection proves a dimension-uniform obstruction to closing (EA7) by refining marginal network counts alone. If a test subgraph \(K\) contains at most one edge from each antipodal orbit, its local no-zero-full-geodesic failure list has entropy deficit at most \(|E(K)|/n\). Set all edges of a least frequent direction in \(K\) to one to obtain this bound. Consequently disjoint-support coding, and weighted Shearer estimates using only those marginal failure lists, can save at most \(L_n/n\), where \(L_n=n2^{n-2}\).

Thus the quantitative improvement and the limitation have complementary roles. The fixed entropy-deficit closure criterion remains a viable unrestricted target, but reaching it requires joint compatibility beyond marginal failure-list counting, or test supports containing antipodal partner edges. This barrier applies to all orbit-simple test subgraphs, with no restriction to a particular face partition or network shape.


### Complete classification of rooted profile parity obstructions

The full-geodesic profile Subsection now proves (RA1)--(RA8). Let \(V\) be the span of all binary square-exchange profile changes. At every root \(x\), the affine profile hull is \(x+a+V\). Its annihilator has a canonical basis consisting of indicators of disjoint autonomous flat direction blocks of positive even size. These are all rooted profile parity restrictions; direction rules outside a block may read its bits.

Balance supplies an additional inequality. Every such flat odd block has signed degree imbalance at least two somewhere. Its rules read only its own bits, so the positive imbalances of different blocks can be attained simultaneously. If there are \(t\) blocks and \(p\) other directions, then \(2t\le p\), and the blocks themselves contain at least \(2t\) directions. Therefore
\[
t\le\lfloor n/4\rfloor,\qquad
\dim\operatorname{aff}\mathcal W_x=n-t\ge\lceil3n/4\rceil.
\]
Explicit balanced legal examples attain equality in every even dimension \(n\ge4\).

Under the standard complementary lift, \(V_{L(c)}=V_c\oplus\mathbb F_2^n\), so the number of parity restrictions remains unchanged. The known rootwise support factorization preserves forbidden old profiles at the same time. Thus the remaining obstruction lies in attainment within these affine cosets, and persists even in balanced lifts whose rooted affine ranks approach their full dimensions. This specifies the higher-order exchange compatibility required by profile-based closure arguments.


### Balanced two-nonlinear switching closure and sign audit

The paired-direction manuscript now closes the full balanced two-nonunary branch. Its switching proof has two independent transport formulations: common four-pivot transport, and transport restricted to the mixed distinguished-reader locus \(X=-Y\).

The remaining incompatible mutual-reader case has two sign configurations, \(s_u=\mu Y,\ s_v=\mu X\). For \(\mu=1\), a zero \(u,v\)-path passes through \(X=Y=1\); both exceptional steps can be inserted there, independently of the selector and all exterior bits. The uniform frozen-core absorption argument handles the unary exterior. For \(\mu=-1\), balance pairs every remaining unary rule into an opposite same-reader pair. Their transport graph, restricted at the exceptional steps to \(X=-Y\), has a strongly connected set containing an antipodal pair. On that locus \(s_a,s_b\) are complementary, and an odd sign transition on an arc supplies both zero exceptional edges. Paired-leaf extension and autonomous-component products give the SCC in arbitrary dimension.

The sign distinction is included explicitly in the manuscript's four-pivot proof as well. Together with the complementary closure and the one-exception theorem, this proves NORI1 for every balanced legal coloring with at most two nonunary direction rules. The result places no bound on their nonlinear reader supports. The restricted transport construction was checked on all eight elementary \(Q_6\) interfaces and twelve \(Q_8\) interfaces including an autonomous paired-reader cycle; the proof is independent of those checks.


### Antipodal exposure: a nonlinear transport extension invariant

The paired-direction Subsection proves (OE1)--(OE6). For a strongly connected transport set \(C\), let \(\mathcal E(C)\) consist of all full cube states encountered between exceptional steps in witnesses with endpoints in \(C\). Adjoin a direction whose rule is any odd Boolean function \(g\) of the old bits, with old nonexceptional rules ignoring the new bit.

The full lifted set \(C\times\mathbb F_2\) is strongly connected precisely when \(g\) vanishes somewhere in \(\mathcal E(C)\). Consequently this lift works for every odd \(g\) precisely when \(\mathcal E(C)\) contains an antipodal pair. Moreover \(\mathcal E(C\times\mathbb F_2)\) contains \(\mathcal E(C)\times\mathbb F_2\). This proves a reusable induction invariant under arbitrary nonlinear odd feedforward extensions. Adding complementary rule pairs preserves balance, and yields closure modules with arbitrarily many nonlinear rules around complementary exceptional cores or the solved negative mutual-reader switching core.

The proof inserts a new zero edge outside an old witness to lift it without changing the new state bit, and inserts it at an exposed zero of \(g\) to toggle that bit within the strongly connected set. Oddness provides complementary values at the full witness endpoints and on exposed antipodal states.

A legal balanced successful \(Q_6\) example shows that requiring loops for every exceptional-bit assignment is too strong for general cyclic interfaces: its universally looped states all have one fixed bit. Its transport SCC nevertheless exposes all cube states, satisfying the weaker invariant. Thus the closing target is cyclic-block transport with antipodal exposure. Existence of an antipodal transport SCC for arbitrary fixed-complementary-pair interfaces would settle unrestricted NORI1 via the established balanced paired lift.
\n\n**Cartesian amplification of minimum monochromatic antipodal path length.** For a legal coloring c of Q_n let L(c) be the shortest red antipodal path length (finite by Wu--Yang, 2026), and e(c)=(L(c)-n)/2. The antipodal map exchanges colors, so the red minimum equals the overall monochromatic minimum. For legal block-product colorings c and d, both conditions remain legal, and L(c boxplus d)=L(c)+L(d). Indeed every red antipodal product path projects to red antipodal walks in both factors, whose lengths sum to at least L(c)+L(d); concatenating shortest red paths attains equality. Hence e(c boxplus d)=e(c)+e(d). If a uniform bound L(c)<=n+o(n) held in every sufficiently large dimension, any putative counterexample c with e(c)>0 would yield tensor powers of dimensions kn with linearly growing excess ke(c), a contradiction. Likewise E(n)=max_c e(c) obeys E(n+m)>=E(n)+E(m) for n,m>=2. If E(n0)>=a>0, tensor floor((n-2)/n0) copies with an arbitrary legal remainder of dimension at least two to give liminf E(n)/n>=a/n0. Thus NORI1 is equivalent to a uniform sublinear additive detour upper bound, and failure of NORI1 forces a linear detour gap in all sufficiently large dimensions. This is an all-dimensional forcing implication, with the sublinear estimate itself open. Independent proof recorded in note_98b1e0fc35badd4e7eb3124d.\n

### Two-hit temporal-word transport across one antipodal alternating-square switch

Let \(c\) be any legal antipodally odd coloring of \(Q_N\), \(N\ge3\). Fix an alternating square \(F\) with free directions \(i,j\), its antipodal square \(\tau F\), and the legal coloring \(c'=T_Fc\) obtained by complementing their eight edges. For a rooted full geodesic \(P\), let \(h_F(P)\in\{0,1,2\}\) be the number of its traversed edges belonging to \(F\cup\tau F\); let \(w_c(P)\in\{0,1\}^N\) be its *temporal* edge-color word.

**Theorem (two-hit full-word involution).** There exists an explicit involutive bijection \(\Phi\) from the \(h_F=2\) rooted full geodesics of \(c\) onto those of \(c'\), satisfying
\[
\boxed{w_c(P)=w_{c'}(\Phi P)\quad\text{in every temporal position}.}\tag{EC14}
\]

*Proof.* If both hits lie in the same switched square, the hits must be consecutive, because each direction outside its free pair is traversed only once. Swap the two consecutive directions \(i,j\) in \(P\), keeping its root. The alternate two-step route follows the other two edges of the same alternating square. Its two colors before switching are the complements of the original colors in corresponding temporal positions, so after switching they match. Every other path edge is unchanged. Swapping back gives the inverse.

If the two hits lie in opposite squares, their outside-bit assignments are complements. All \(N-2\) outside directions are therefore traversed between the hits, so the two hits occur as the first and last edges. Up to interchanging \(i,j\), let \(P\) have root \(x\) and direction order \((i,\rho,j)\), with \(\rho\) the other \(N-2\) directions. Put \(u=x\oplus e_i\), \(v=\bar x\oplus e_j\), \(x'=x\oplus e_i\oplus e_j\), and construct
\[
x'\xrightarrow{j}u\xrightarrow{\rho}v\xrightarrow{i}\bar{x'}.
\]
The interior edges agree with those of \(P\); the first and last edges are the alternate edges on \(F,\tau F\). The alternating pattern and switch make their new colors agree positionwise with the old endpoint colors. Applying this transformation again returns \((x,(i,\rho,j))\). Interchanging the directions and the order of the two opposite faces covers the remaining orientations. Both cases exhaust \(h_F=2\). \(\square\)

**Corollary (all full-word changes are carried by one-hit paths).** For each temporal word \(w\), the number of \(h_F=0\) paths with word \(w\) and the number of \(h_F=2\) paths with word \(w\) are separately invariant under \(T_F\). Consequently the difference of the full temporal-word enumerators of \(c,c'\) is supported entirely on the \(h_F=1\) sector.

**Corollary (strictly internal square carrier at a good-to-bad boundary).** If \(c\) admits an all-zero full geodesic and \(T_Fc\) admits no monochromatic full geodesic, then **every** all-zero full geodesic of \(c\) meets \(F\cup\tau F\) in precisely one edge, strictly internally. A zero-hit red path would survive unchanged, and a two-hit red path would survive through the involution. A one-hit red path produces a one-blue path after switching. Were its single blue edge first or last, the cyclic root rotation would replace it with its red antipodal mate, producing a red full geodesic after the switch. All cases except the single internal hit are excluded. \(\square\)

In particular, the already proved paired-flat balanced square-adjacent counterexample normalization of this Subsection improves: if NORI1 fails, there is a balanced good/bad paired-flat square-switch boundary for which every red witness on the good side crosses the switched square pair in one strictly internal red edge; the bad side has a corresponding full path with one strictly internal blue edge. The two-opposite-endpoint hit case permitted by the earlier reduction is eliminated by a joint root/endpoint-order exchange. This is an unrestricted geometric strengthening and leaves the remaining one-internal-hit configuration unresolved.

Reproducible verification: research note \`note_nori_double_square_temporal_word_transport_r11510\`, session \`session_nori_r11510_3\`; 440,576 two-hit path tests in dimensions three through five, including involution tests. The argument above proves the theorem for all dimensions.


### Two-pair seam forcing and mutual-reader traps

Let N=2m>=6 and c be any paired-flat antipodally odd coloring. Each prescribed direction pair P={i,i'} has red/blue gate f_P independent of both bits in P, with colors f_P and 1+f_P, and f_P(bar x)=1+f_P(x).

**Theorem (four-direction seam forcing).** Fix two pairs P,Q, let J be the remaining N-4 directions, and suppose a zero full J-geodesic H goes from (u,y) to (u,bar y), freezing the four P,Q bits at u. Rename them 0,1 in P and 2,3 in Q. At J-root y write the two gates a(x2,x3), b(x0,x1). Then H extends to an all-zero full antipodal geodesic unless a=x_r+alpha, r in {2,3}, b=x_s+beta, s in {0,1}, and
  a(u)=1_{s=0}, b(u)=1_{r=2}. (SC1)
If a,b are such mutual unary readers, the exceptional seam positions form a four-vertex affine subcube.

**Four-bit proof.** Let A be the ordinary Q4 coloring with rules a,1+a,b,1+b. The colors of the four missing directions after H are A^+_i(v)=1+A_i(bar v), by antipodal oddness. A completion is an order pi of 0,1,2,3 and a cut k in {0,...,4}; start at u xor the first k directions of pi, use A-red edges for the first k steps, traverse H, and use A^+-red edges for the last 4-k steps. Translate u to 0000, write a,b as four-bit truth-table integers. The following 24 pairs (pi,k) cover 252 of the 256 table pairs:
(0213,0),(0213,4),(0231,2),
(0312,0),(0312,2),(0312,3),
(1203,1),(1203,3),(1230,2),
(1302,1),(1302,2),(1302,3),
(2013,2),(2031,1),(2031,3),
(2103,2),(2130,0),(2130,4),
(3021,1),(3021,2),(3021,4),
(3120,0),(3120,2),(3120,4).
Each is verified by evaluating the four traversed edge bits with A before the cut and A^+ afterward. The four uncovered table pairs are (3,10),(5,5),(10,3),(12,12), precisely (SC1) at u=0. Translation gives the displayed criterion for any u. Conversely, under (SC1), A^+=A because both gates are complement-odd on Q4. At u, each pair's zero edge toggles the bit not read by the other gate. Both reader bits stay fixed, hence the entire red component of u is a four-cycle using those two unread directions. No red full antipodal Q4 path contains u. Thus the four exceptions cannot be completed. This proves both directions of the local lemma. The insertion described above lifts the lemma to the original Q_N. QED.

**Global support confinement.** In a hypothetical bad paired-flat c, fix any P,Q and J-root y. Let U_y be the set of all u in F_2^4 supporting an all-zero full J-geodesic rooted at (u,y), allowing any order. If U_y is nonempty, the two outer gate restrictions at y must be mutual unary readers, and U_y lies in the four-vertex exceptional affine subcube (SC1). Thus |U_y|<=4. Either a single J-witness at a non-unary interface, or five J-witnesses from distinct u at a common J-root y, forces a full red antipodal geodesic. The hypotheses are tested within one arbitrary paired-flat coloring; they impose no global Boolean degree or feedback restriction.

**Endpoint-pair factorization.** Fix one pair P={i,j}, and the four faces F_u with its bits frozen to u. Every rooted full face path with temporal color word w has two full-path completions with the pair directions at its first and last steps in opposite orders, of words 0w0 and 1w1. For the (i,H,j) completion the endpoint colors are f_P(y) and 1+f_P(bar y)=f_P(y); swapping i,j complements both. Therefore the temporal blue-count polynomial for all rooted full paths whose first and last directions are the members of P is
 F_{c;P}^{end}(z)=(1+z^2) sum_{u in F_2^2} F_{c|F_u}(z).
This full temporal-word multiset is invariant under arbitrary changes to the odd pair gate f_P, with other pair gates fixed. The identity holds for all paired-flat legal Q_N, N>=4.

**Scope and verification.** The four-bit calculation is an all-dimensional conditional forcing mechanism, with a finite Boolean certificate. It does not guarantee a red J-geodesic in every coloring, so NORI1 remains open. The self-contained checker nori_two_pair_seam_certificate.py verified all 4096 (a,b,u) instances against all 120 order/cut possibilities, checked the 24-route certificate, and verified 20 nonlinear Q8 lifts. Full proof nori_two_pair_seam_forcing.md.

### Paired rank-two sensitivity forcing and irreducible all-pair circuits

**Proved.** Full proof at /mnt/data/nori_pair_sensitivity_circuit.md and checker at /mnt/data/nori_pair_circuit_activation.py. The first assertion is positive and constructive. The second explains the limit of induction from smaller paired faces. NORI1 remains open.

**THEOREM 1 (rank-two product identity).** On an ordinary, possibly non-antipodal-odd paired-flat Q4, split directions into A={a0,a1} and B={b0,b1}. Let edge colors be c_(a_i)(p,q)=a(q)+i and c_(b_j)(p,q)=b(p)+j, over F2, for arbitrary gates a,b:F2^2->F2. Denote by E(a), E(b) the numbers of undirected input-square edges where the respective gate changes. The number of rooted all-red full geodesics is
   R=2 E(a) E(b).
The number of rooted all-blue full geodesics obeys the same identity. In particular R>0 iff both gates are nonconstant, and then R>=8.

**Proof.** Two red consecutive edges cannot lie in the same direction pair, because traversing its chosen red direction leaves that pair gate unchanged and the other direction blue. Thus every red full path has pair word ABAB or BABA. For ABAB choose a sensitivity edge of a in B-input direction beta and a sensitivity edge of b in A-input direction gamma. Put alpha=1-gamma. On the first edge choose the endpoint q where a(q)=alpha, and on the second choose t where b(t)=beta. Set initial A-bit pair p=t+e_alpha. Then directions (a_alpha,b_beta,a_gamma,b_(1-beta)) from root (p,q) are all red: first gate values select alpha,beta, and the chosen sensitivities flip them to gamma,1-beta for the last two steps. Every red ABAB witness uniquely specifies those two input sensitivity edges, so there are E(a)E(b). Swapping A and B gives the same number for BABA. Complementing both gates preserves their edge-boundary sizes, proving the blue statement. QED.

**DIMENSION-UNIFORM FACE COUNT.** For any legal paired-flat Q_(2m), fix two paired groups A,B and freeze all remaining direction bits at y. Write a_y,b_y for the induced four-face gates. Then the total number of rooted red four-face geodesics, summed over all frozen y, is
  2 sum_y E(a_y) E(b_y).
This measures simultaneously active reciprocal influences using the SAME frozen assignment. Separate influence counts do not determine it.

**THEOREM 2 (globally essential cyclic-reader witness).** For every m>=2, define paired directions P_i={a_i,b_i}={2i,2i+1}, indices cyclic modulo m, with legal gates c_(a_i)(x)=x_(a_(i-1)), c_(b_i)(x)=1+x_(a_(i-1)). Every vertex has one red and one blue edge from each pair, and the group-influence graph is a directed m-cycle. This coloring has a full all-red antipodal geodesic but NO proper nonempty paired-direction face has a monochromatic full geodesic relative to that face.

**Proof.** From root x_(a0)=1, all other bits 0, traverse
  b1, a0, a_(m-1), a_(m-2), ..., a1, b0, b2, ..., b_(m-1).
The first b1 reads a0=1 and is red; a0 and the descending a_i read predecessors still zero and are red; a1 reads a0 after its flip to zero and is red; b0 and the remaining b_i read predecessors now one and are red. Each direction is used once and the endpoint is antipodal. For any proper nonempty subset S of paired groups, there is i in S with predecessor i-1 outside S. Throughout every face freezing all other groups, group i's gate is constant, so its two directions have opposite constant colors. A full spanning S-face geodesic uses both; hence no such path is monochromatic. QED.

**RESEARCH SCOPE.** The positive local mechanism is simultaneous reciprocal gate sensitivity. The reader-cycle example proves that even a successful coloring may have no monochromatic full geodesic in any proper pair-face, including all codimension-four faces tested by the preceding seam theorem. Thus a universal proof must also construct global irreducible all-pair witnesses. The example does not rule out counterexample-specific hereditary forcing.

**TESTS.** Independent complete-root/order checking of all 256 four-bit gate-pairs confirms R=2 E(a)E(b), with 196 positive cases and 60 constant-gate cases. The full reader-cycle construction and the proper-pair-subset criterion were checked for m=2,...,12, with dimension-uniform proofs above.

### Even sweep parity and operator-level Cartesian transfer (October 2026)

In the paired-flat red matching model, write fiber bits \(t_i=x_{2i}\) and base pair parities \(p_i=x_{2i}\oplus x_{2i+1}\). Each red pair gate \(U_i\) is a fiber shear \(t_i\mapsto t_i\oplus h_i(p_{-i},t_{-i})\), with all other fiber bits unchanged. Antipodal oddness yields \(h_i(p_{-i},t_{-i}+\mathbf1)=1+h_i(p_{-i},t_{-i})\). Thus, on every fixed-base fiber of cardinality \(2^m\), the induced shear permutation has \(2^{m-2}\) disjoint transpositions. A complete order of the \(m\) red gates therefore has permutation sign \((-1)^{m2^{m-2}}=+1\) for every \(m\ge2\). All complete-sweep comparison holonomies \(\Phi_\rho^{-1}\Phi_\pi\) consequently lie in the alternating group \(A_{2^m}\), without any linearity hypothesis on the selectors.

Combined with the established full-sweep holonomy generation theorem, this excludes a red covering with precisely one two-sheet component and every other component single-sheeted. Indeed, transitivity on that two-point component forces an odd transposition of the entire fiber, contradicting even holonomy. Unlike the earlier antipodal two-sheet exclusion, this new statement does not require the two-sheet component to contain antipodes.

For independent paired-flat colorings on \(m,k\) direction pairs, let \(B^c_p(t,s)\) count full red sweeps with given input/output fiber states. All interleavings of two fixed factor orders have identical endpoints, and there are \(\binom{m+k}m\) such interleavings. Thus the full matrices satisfy
\[
B^{c\boxplus d}_{(p,q)}=\binom{m+k}m\,B^c_p\otimes B^d_q.
\]
Writing \(P=B/m!\) and \(K=PP^\top\), one obtains \(P_{\rm product}=P_c\otimes P_d\), \(K_{\rm product}=K_c\otimes K_d\). The comparison holonomy group similarly factors as a direct product, and the product collision spectrum consists of products of factor eigenvalues. For connected component fibers, the spectral gap is the lesser of the two factor gaps. This operator law strengthens the earlier scalar midpoint-count tensor identity.

These are necessary structural constraints, not a proof of a one-step antipodal collision. The proofs and standalone verification are preserved in research note \`note_fdf278eae230ca4aac3ec185\`, version 2, with local files \`nori_even_holonomy_tensor_theorem.md\` and \`nori_even_sweep_holonomy_verify.py\`.


**Antipodal endcap intertwining for complete red sweeps.** Write \(J(t)=t+\mathbf1\) on fiber states and \(T_i(t)=t+e_i\). Antipodal oddness yields \(U_iJ=T_iJU_i\), equivalently \(U_i J U_i^{-1}=T_iJ\), interpreting the gate on its appropriate source and target parity fibers. Therefore for every pair order \(\pi=(i_1,\ldots,i_m)\) and every fiber root \(t\),
\[
[\Phi_\pi(t)+\Phi_\pi(t+\mathbf1)]_{i_1}=0.
\]
Indeed the two initial complementary roots have opposite gate-control values for the first pair, so their \(i_1\)-bits agree after that red move; subsequent moves in other pairs preserve that bit. Applying the same reasoning to the reverse gate order proves the dual constraint
\[
[\Phi_\pi^{-1}(s)+\Phi_\pi^{-1}(s+\mathbf1)]_{i_m}=0.
\]
Equivalently \(\Phi_\pi J\Phi_\pi^{-1}\) preserves both first-label fiber-bit hyperplanes, and \(\Phi_\pi^{-1}J\Phi_\pi\) preserves last-label hyperplanes. These hold for arbitrary nonlinear legal paired-flat gates and are directly path-realizable, unlike abstract support-matching constraints. The complete proofs and finite Q4/Q6/Q8 checks are in research note \`note_fdf278eae230ca4aac3ec185\`, v3. Neither identity alone proves the unrestricted two-different-order antipodal midpoint collision.


### Rank-two parity-peeling square closure
Every static odd-row zero-diagonal rank-two paired-flat reader with arbitrary nonlinear parity phases admits a red antipodal geodesic in each parity fiber. Partition its rows into two types u,v, choose mutually reading labels a,b, and let s list all other rows of the first type followed by those of the second. The word s a b a b reverse(s) has 2^(m-2) successful fiber roots per base. The outer prefix sends the all-one displacement to e_a+e_b; the central four-gate square has invertible active displacement matrix [[1,1],[1,0]]. The outer suffix inverts the prefix because the paired occurrences read the same parity-phase keys. The theorem and the more general even-predecessor certificate are proved in note_c8f556bc515815b03a2f2f9a and nori_rank_two_parity_shell_forcing.md.


**Proof of the general parity-peeling certificate.** Suppose \(A_{ab}=A_{ba}=1\) and the remaining labels \(s_1,\ldots,s_{m-2}\) obey \(\sum_{\ell<k}A_{s_k,s_\ell}=0\) modulo two. For the prefix red sweep \(H\), let \(E_i=I+e_iA_{i,*}\) be its linear gate. Start with difference vector \(\mathbf1\). At step \(s_k\), previously visited difference bits are zero and all unvisited bits are one. Oddness of the row then makes the new bit \(1+\sum_jA_{s_kj}d_j=\sum_{\ell<k}A_{s_k,s_\ell}=0\). Thus \(H_{\mathrm{lin}}\mathbf1=e_a+e_b\).

Each outer label is visited again after the central square and later outer labels have returned. Its two phase keys differ only in its own parity bit, which its phase function ignores. Consequently the full word \(s\,a b a b\,s^{\mathrm{rev}}\) acts affinely as \(H^{-1}CH\), where \(C\) is the central four-step return. To produce global displacement \(\mathbf1\), it suffices that \(C(y)=y+e_a+e_b\). Since \(A_{ab}=A_{ba}=1\), the active two-dimensional linear parts of the red gates are \(E_a=\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}\) and \(E_b=\begin{psmallmatrix}1&0\\1&1\end{psmallmatrix}\). Their four-step return has displacement matrix \((E_bE_a)^2+I=\begin{psmallmatrix}1&1\\1&0\end{psmallmatrix}\), invertible. For every assignment to the other \(m-2\) fiber bits, precisely one active two-bit assignment gives the desired shift, for any affine phase values. There are therefore \(2^{m-2}\) successful roots per starting parity fiber. A red antipodal path of length \(2m\) is a full geodesic.


**Why rank two always peels.** For \(A\) of rank two with all rows odd, the two-dimensional row space has precisely two nonzero vectors of odd weight, \(u,v\); their sum has even weight. Each matrix row is \(u\) or \(v\). Let \(I,J\) denote the nonempty row classes of \(u,v\). As \(A_{ii}=0\), \(\operatorname{supp}u\subseteq J\) and \(\operatorname{supp}v\subseteq I\). Choose \(a\in I\cap\operatorname{supp}v\) and \(b\in J\cap\operatorname{supp}u\), both nonempty because \(u,v\) are odd. Then \(A_{ab}=A_{ba}=1\). Order the other labels by listing \(I\setminus\{a\}\) first, then \(J\setminus\{b\}\). An \(I\)-row reads only \(J\) and sees no prior reader. A \(J\)-row reads \(v\), supported in \(I\), and sees parity \(\sum_{i\in I\setminus\{a\}}v_i=(\sum_iv_i)+v_a=1+1=0\). Thus the even-predecessor condition is satisfied at every step. The preceding proof supplies a full red geodesic for each of \(2^{m-2}\) fiber roots in each prescribed base parity, independent of the nonlinear phase values.

The construction applies to arbitrary rank whenever a mutually reading pair and an even-predecessor order exist. Related archive work separately handles the full-rank case by the Gauss--Seidel determinant identity. In the singular case, the common reader kernel satisfies \(\ker A\subseteq\ker(L_w+I)\). Combined with the archived phase-interlacement corank theorem, any phase-immune doubled word for rank \(r\) has at most \(r\) nonisolated interlacement chords. At rank two a successful word needs precisely one crossing pair: a zero-crossing word cancels through adjacent equal-label involutions and cannot reach the antipode. This gives a structural reason to seek a transported square rather than an unrestricted word.


## Translation-orbit avoidance of paired-square switches

Let \(c\) be a paired-flat legal coloring of \(Q_{2m}\), with paired direction sets \(P_i\), and suppose \(c\) has a red full antipodal geodesic. Let \(H\le\mathbb F_2^{2m}\) be a group of translations preserving every colored edge, and let \(S\) be an antipodal square-pair orbit supported on \(P_i\). Translation acts on square-pair orbits supported on \(P_i\). Write \(M=|H\cdot S|\).

**Theorem (translation-orbit avoidance and simultaneous restoration).** If \(M>2t\), then for any collection \(\mathcal T\) of at most \(t\) square-pair orbits in \(H\cdot S\), there is a red full antipodal geodesic avoiding their union. In particular \(M\ge3\) guarantees that switching the colors on \(S\) preserves the existence of a monochromatic full antipodal geodesic.

*Proof.* Choose a red full geodesic \(P\). It uses the two directions in \(P_i\) once each, so its two \(P_i\)-edges meet at most two distinct square-pair orbits. For uniformly chosen \(h\in H\), the translated path \(P+h\) remains a red full antipodal geodesic, since \(h\) preserves all edge colors and bit differences. The \(H\)-translates of any fixed square-pair orbit in \(H\cdot S\) are uniformly distributed over this orbit. Consequently for each \(T\in\mathcal T\), the probability that either of the two \(P_i\)-edges of \(P+h\) belongs to \(T\) is at most \(2/M\). The union bound gives
\[
\Pr_h[(P+h)\cap\bigcup_{T\in\mathcal T}T\ne\varnothing]\le 2t/M<1.
\]
Some translate therefore avoids every member of \(\mathcal T\). Any prescribed color switches on these square-pair orbits leave that red geodesic unchanged. QED.

**Corollary (unread-direction obstruction at a strict critical boundary).** Suppose \(2m\ge6\), and the two directions of \(P_i\) have at least two exterior directions whose bits are not read by any paired gate. If \(c\) has a red full geodesic, one avoids every prescribed square-pair orbit supported on \(P_i\). Thus at a hypothetical good-to-bad paired-square boundary, at most one direction outside the switched pair can be globally unread.

*Proof.* Translation in a globally unread direction preserves every edge color: no gate reads this bit, and each gate ignores its own paired directions. Let \(j,k\notin P_i\) be two such directions. Their translations generate a four-element group. Since there are at least four exterior directions, no nonzero translation supported on \(\{j,k\}\) complements all exterior bits. Hence the orbit of a square-pair parameter under this group has cardinality four. Apply the theorem with \(t=1\). QED.

**Sharpness.** The threshold \(M>2\) cannot be reduced to \(M=2\). On \(Q_4\) use direction pairs \(A=\{0,1\}\), \(B=\{2,3\}\), with paired-flat gates \(f_A(x)=x_2\), \(f_B(x)=x_0\). Translation in direction \(3\) preserves the coloring. It acts with a two-element orbit on the antipodal \(A\)-square pairs, yet every red full antipodal geodesic meets both such square-pair orbits. Indeed the paired-direction word of a red full geodesic must alternate \(ABAB\) or \(BABA\); otherwise consecutive steps in one pair have opposite colors. In each alternating word the two \(A\)-steps differ by one exterior bit and hence meet different square-pair orbits. Thus no red full geodesic avoids either \(A\)-square-pair orbit.

**Scope.** This is an all-dimensional restoration theorem with a color-preserving translation hypothesis. A hypothetical critical successful coloring must have square-orbit size at most two under its full color-preserving translation group. The statement does not impose such symmetry on arbitrary nonlinear paired-flat gates and therefore does not settle unrestricted NORI1. An exhaustive six-dimensional strengthening without any translation hypothesis is documented in the related research note \`note_nori_q6_square_orbit_avoidance_20261018_r11755\`; lifting that finite statement requires compatible paths across exterior fibers.


## Critical pair-word sparsity and nonlinear perturbation survival

Fix \(m\ge2\) and a paired-flat legal coloring \(c\) on \(Q_{2m}\), with direction pairs \((a_i,b_i)\). The red edges in pair \(i\) form a perfect matching; let \(T_i\) be its involution on vertices. A *pair word* \(w=(w_1,\ldots,w_{2m})\) uses each pair label twice. Let \(X_c(w)\) be the starting vertices of red walks along \(w\) whose terminal vertex is the antipode, and let \(r_i(w)\in\{0,1,2\}\) count occurrences of \(i\) at strictly internal positions. Every walk counted by \(X_c(w)\) is a full geodesic: in \(2m\) steps, an antipodal endpoint requires every original direction once.

**Theorem 1 (critical rooted-word bound).** Suppose \(c'\) is obtained by flipping the eight edges of an alternating square in directions \(a_i,b_i\) and its antipodal square, and suppose \(c'\) has no monochromatic full geodesic. Then for *every* pair word \(w\),
\[
\boxed{|X_c(w)|\le 8r_i(w).}\tag{KR1}
\]
In particular, no red full geodesic of \(c\) begins and ends in pair \(i\); and at most eight red rooted full geodesics share any word with one occurrence of \(i\) at an endpoint. This applies to nonlinear gates.

*Proof.* Of the eight switched edges, four are red in \(c\). Under the badness hypothesis every red full geodesic of \(c\) has precisely one switched edge, in an internal position. To see this, a path avoiding the switch survives. For two switched edges in one square, exchange the consecutive square directions; for one edge in each of the two antipodal squares, exchange the first and last square directions while translating the root by their sum. Either operation yields a red full geodesic of \(c'\). A one-hit path with a terminal hit becomes a one-blue-edge path in \(c'\), and cyclic rotation across that endpoint edge replaces it by its red antipodal mate, giving a red full geodesic. Thus only a single internal hit is possible.

For a fixed red switched edge, one of its two orientations, and an internal position \(t\) with \(w_t=i\), the red \(w\)-walk traversing that oriented edge at \(t\) has at most one starting vertex: invert the red matching bijections forming its prefix. There are four red edges, two orientations, and \(r_i(w)\) internal positions. Counting every root by its compulsory hit gives (KR1). \(\square\)

**Corollary 2 (square-boundary forcing).** If \(|X_c(w)|>8r_i(w)\) for some word \(w\), every paired alternating-square switch in pair \(i\) preserves the existence of a monochromatic full geodesic. Nine red rooted geodesics sharing a word with one endpoint occurrence of \(i\) suffice.

**Theorem 3 (full-rank affine class survives one nonlinear switch).** Let the paired gates of \(c\) be
\[
f_i(p,q)=\sum_{j\ne i}a_{ij}q_j+\theta_i(p_{-i})\pmod2,
\]
where \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\); the matrix \(A=(a_{ij})\) has zero diagonal, \(A\mathbf1=\mathbf1\), and \(\det A=1\); and the phase functions \(\theta_i\) are arbitrary. For every \(m\ge4\), one antipodal alternating-square switch in any direction pair preserves a monochromatic full geodesic, including when it generates a nonlinear gate.

*Proof.* If the switched pair is \(i\), choose a permutation \(\pi\) with \(i\) first, and put \(w=\pi\pi\); then \(r_i(w)=1\). For a fixed initial parity \(p\), the first sweep is an affine map of \(q\) with linear part \(F_\pi\). Relabel by \(\pi\), let \(L\) be the strictly lower triangular part of \(A\), and write the sequential equations to obtain \(F_\pi+I=(I+L)^{-1}A\). The second sweep has the same linear part; its phase offset may differ. The complete antipodal return equation is affine with coefficient
\[
F_\pi^2+I=(F_\pi+I)^2,
\]
which is invertible because \(\det A=1\). Hence in *each* of the \(2^m\) initial parity fibers there is one root producing a red full geodesic with word \(w\). Thus \(|X_c(w)|=2^m\ge16>8r_i(w)\); Corollary 2 applies. \(\square\)

**Theorem 4 (multiple sparse nonlinear switches).** Under Theorem 3's hypotheses, flip any union of \(t\) antipodally paired alternating squares lying in direction pairs, with the final coloring legal. If
\[
\boxed{16t<2^m,}\tag{KR2}
\]
the final coloring retains a red full geodesic.

*Proof.* Fix any \(\pi\), and set \(w=\pi\pi\). Theorem 3's linear calculation produces \(2^m\) red full geodesics of \(c\) with that word. Each square pair contains four red edges of \(c\). For each of those edges, either orientation, and either of the two positions of its pair label in \(w\), there is at most one starting root, by invertibility of the preceding matching product. Thus at most \(16t\) of the witnesses use any of the changed edges. Under (KR2), one witness remains untouched and stays red. \(\square\)

Theorem 1 gives a necessary restriction on *arbitrary* nonlinear paired-flat critical good colorings, within a common fixed pair word and shared edge assignment. Theorems 3–4 give a dimension-uniform positive transfer to one or several nonlinear square perturbations of the full-rank affine-slope class. They do not prove that an arbitrary hypothetical critical good coloring has the required common-word root multiplicity, or give the vertex-simple boundary-tournament implication. This root-multiplicity production is the remaining gap.


### Root-support robustness for arbitrary paired-flat gate systems

**Theorem 5 (common-word square-fault budget).** Let \(c\) be *any* paired-flat legal coloring on \(Q_{2m}\), possibly with nonlinear gates. Suppose a pair word \(w\) has \(N=|X_c(w)|\) red antipodal roots. Let \(c^\star\) be a legal coloring obtained by switching a union of \(t\) antipodally paired alternating squares, in arbitrary direction pairs. If
\[
16t<N,
\]
then \(c^\star\) has a red full geodesic. For a *single* square pair \(S\) in pair \(i\), the sharper hypothesis \(\lvert X_c(w)\rvert>8r_i(w)\) suffices to preserve a monochromatic full geodesic, as in Theorem 1.

*Proof.* Fix a switched square pair in label \(i\). There are four originally red edges in its eight-edge support. For each such edge, its two orientations, and either occurrence position of label \(i\) in \(w\), at most one initial root follows the red word \(w\) through that edge; the prefix is a bijection. Thus at most sixteen of the \(N\) witnesses meet this square pair. The union of \(t\) square pairs meets at most \(16t\) witnesses. One untouched witness survives when the inequality holds. No linearity is used. \(\square\)

**Corollary 6 (nested-core nonlinear fault tolerance).** Consider paired-flat gates \(f_i(p,q)=\sum_{j\ne i}a_{ij}q_j+\theta_i(p_{-i})\), with parity-independent zero-diagonal slope matrix \(A\), odd row sums, and arbitrary phase functions. Suppose \(i_1,\ldots,i_k\) are distinct outer labels, with remaining set \(R\) of size at least two, such that \(\det A[R,R]=1\) and \(\sum_{s<t}a_{i_t,i_s}=0\) for each \(t\). For any permutation \(\pi\) of \(R\), the established nested-core forcing theorem supplies
\[
w=i_1\cdots i_k\,\pi\pi\,i_k\cdots i_1,\qquad |X_c(w)|=2^{m+k}.
\]
Consequently any union of \(t\) legal paired-square switches with \(16t<2^{m+k}\) preserves a red full geodesic. If \(m\ge4\) and \(k\ge1\), *every single* legal antipodal paired-square switch preserves a monochromatic full geodesic, because \(2^{m+k}\ge32>16\ge8r_i(w)\) for every pair \(i\). The case \(k=0\), equivalent to nonsingular \(A\), is covered by Theorem 3 by selecting \(\pi\) to start with the switched pair. Hence **every static affine-slope coloring admitting a legal nested-core peel in dimension \(2m\ge8\) remains successful under one legal square switch**, with unrestricted nonlinear phase truth tables and nonlinear output gates.

*Proof.* The nested-core theorem solves the red antipodal return equation for precisely \(2^k\) starting \(q\)-states in each of the \(2^m\) parity fibers. The common-word budget of Theorem 5 gives the multi-switch result. The critical bound of Theorem 1 gives the one-switch result. \(\square\)

The nested-core existence hypothesis is established for every odd-row zero-diagonal slope matrix only through the recorded finite classifications, with an arbitrary-size peeling conjecture still unresolved. The corollary is dimension-uniform **conditional on an explicit algebraic peel**, and does not imply the existence of such a peel for all matrices, nor the required nonlinear-gate transfer at arbitrary hypothetical good/bad critical boundaries.


## Nonlinear outer gates and nonsingular inner returns

All additions below are in \(\mathbb F_2\). Partition the \(2m\) cube dimensions into pairs \((a_i,b_i)\), and write \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\). A paired-flat coloring assigns the two direction colors \(f_i(p,q)\), \(1+f_i(p,q)\), where \(f_i\) ignores \(p_i,q_i\) and satisfies \(f_i(p,q+\mathbf1)=1+f_i(p,q)\). The unique red move in pair \(i\) is the involution
\[
T_i:(p,q)\longmapsto(p+e_i,\ q+(1+f_i(p,q))e_i).
\tag{NO1}
\]
Here red denotes color zero. Antipodal complementation fixes \(p\) and sends \(q\) to \(q+\mathbf1\).

**Theorem (nonlinear extension of nested-core forcing).** Let \(S=(i_1,\ldots,i_k)\) be ordered distinct pair labels, and let \(R\) be the complementary set, with \(|R|\ge2\). Suppose:

1. For every \(t\), every \(p,q\), and \(D_t=R\cup\{i_{t+1},\ldots,i_k\}\),
\[
f_{i_t}(p,q+\mathbf1_{D_t})=1+f_{i_t}(p,q).
\tag{NO2}
\]
2. For \(j\in R\), the gate has the form
\[
f_j(p,q)=\sum_{\ell\in R}B_{j\ell}(p_S,q_S)q_\ell+
\theta_j(p_{\ne j},q_S),
\tag{NO3}
\]
where every matrix \(B(p_S,q_S)\) has zero diagonal and is nonsingular. The phase functions are arbitrary subject to the stated paired-flat coloring law.

For any fixed permutation \(\pi\) of \(R\), the pair word
\[
w=i_1\cdots i_k\,\pi\pi\,i_k\cdots i_1
\tag{NO4}
\]
has precisely \(2^k\) red antipodal starting roots in every prescribed initial parity fiber \(p=p^0\). Each resulting \(2m\)-step walk is a full geodesic in the original cube.

The matrices in (NO3) may depend nonlinearly on the outer bits. No row-sum condition is imposed on these inner matrices.

*Proof.* Execute the first \(k\) moves. This prefix is a bijection from the initial parity fiber to the fiber \(p'=p^0+\mathbf1_S\). Choose the \(k\) outer bits \(z=q_S\) arbitrarily just after the prefix. During the central word \(\pi\pi\), these bits and \(p_S\) are fixed, so the inner slope matrix is one fixed nonsingular matrix \(B=B(p'_S,z)\).

Relabel the inner labels in the order \(\pi\), and write \(B=L+U\) with \(L,U\) strictly lower and upper triangular. A single inner sweep has homogeneous matrix
\[
F=(I+L)^{-1}(I+U),\qquad F+I=(I+L)^{-1}B.
\tag{NO5}
\]
Indeed, the sequential update at an inner label reads the new values at earlier labels and the old values at later labels. Its phase reads a specified parity state and the fixed outer bits, so it is independent of the inner \(q\)-variables. The two sweeps therefore have affine forms \(q_R\mapsto Fq_R+\alpha\) and \(q_R\mapsto Fq_R+\beta\), with potentially different offsets. The equation making their combined return complement every inner bit is
\[
(F^2+I)q_R=\mathbf1_R+F\alpha+\beta.
\tag{NO6}
\]
Since \(F^2+I=(F+I)^2\) and \(F+I\) is nonsingular by (NO5), this equation has one solution for each chosen \(z\).

Return through the outer labels in reverse order. At the two visits to \(i_t\), every other pair parity has the same value: deeper labels have each occurred twice, while earlier outer labels have occurred once at both visits. The gate ignores its own parity. By reverse induction, the deeper \(q\)-bits have all been complemented, while earlier outer bits have stayed fixed. Thus the two gate values differ by one, by (NO2). Their two red moves traverse opposite members of pair \(i_t\), complementing its \(q\)-bit and restoring its parity.

Consequently every choice of \(z\) gives a red antipodal return. The prefix bijection gives \(2^k\) distinct initial roots. Conversely, any successful return along (NO4) complements the inner bits during the central word, since the outer moves leave them unchanged. Its inner starting state must therefore be the unique solution of (NO6) for its \(z\). This proves the root count.

Each pair occurs twice. A pair's restored parity and complemented \(q\)-bit mean that its two original dimensions were traversed once each. Hence the entire walk uses all \(2m\) original dimensions once, and is a vertex-simple full antipodal geodesic. \(\square\)

### Whole-gate replacement and square-switch tolerance

By global oddness, (NO2) is equivalent to
\[
f_{i_t}(p,q+\mathbf1_{\{i_1,\ldots,i_{t-1}\}})
=f_{i_t}(p,q).
\tag{NO7}
\]
For \(t=1\), this is automatic. Later outer gates may depend nonlinearly on earlier bits through functions invariant under their simultaneous complementation.

**Corollary (whole-gate replacement).** Under the theorem's hypotheses with \(k\ge1\), replace \(f_{i_1}\) by any function defining a legal paired-flat gate, leaving all other gates fixed. The same word (NO4) still has \(2^k\) successful roots in every parity fiber. More generally, all outer gates may be replaced simultaneously by arbitrary functions satisfying (NO7) and global oddness.

*Proof.* Condition (NO7) for the first gate is vacuous. Conditions (NO3) for the other gates are unchanged. For the simultaneous statement, every hypothesis remains valid. Apply the theorem. \(\square\)

This allows changes to an entire gate truth table. In particular, any collection of antipodally paired alternating-square switches supported on the first outer pair preserves a red full geodesic, without a bound on the collection's size.

**Corollary (additional faults in arbitrary pairs).** Starting with any coloring satisfying the theorem, switch any union of \(t\) antipodally paired alternating squares in arbitrary direction pairs. If either
\[
4t<2^m\qquad\text{or}\qquad16t<2^{m+k},
\tag{NO8}
\]
the resulting coloring has a red full geodesic. Every single such switch preserves success for \(m\ge3\).

*Proof.* Word (NO4) has \(2^{m+k}\) successful roots, counting all parity fibers. One square pair contains four originally red edges. For each edge, orientation, and either occurrence of its pair label in the word, at most one starting root traverses that oriented edge there: invert the preceding matching involutions. Thus at most sixteen of these rooted paths meet one square pair, and at most \(16t\) meet the changed union. One untouched red geodesic survives when \(16t<2^{m+k}\).

For the other inequality, a fixed square pair in label \(i\) has one fixed exterior pair-parity pattern \(\sigma\): its antipodal companion has the same pattern. At a specified occurrence of \(i\) in (NO4), the initial outside parity is therefore determined by \(\sigma\) and the known prefix of pair labels; only the initial bit \(p_i\) is free. Each occurrence can affect at most two initial parity fibers, so a square pair affects at most four. The theorem supplies a successful root in all \(2^m\) fibers. If \(4t<2^m\), some fiber's successful paths avoid every changed square pair. For \(t=1\) this inequality holds whenever \(m\ge3\). \(\square\)

The earlier static affine nested-core theorem is recovered by taking \(B=A[R,R]\). For an outer affine gate, (NO7) becomes \(\sum_{s<t}a_{i_t,i_s}=0\). The present theorem also permits nonlinear dependence in every gate and nonlinear variation of the inner slope matrix with outer states.

### An unbounded strongly connected family with every gate nonlinear

Let \(k\ge3\), \(m=k+3\), with outer bits \(z_0,\ldots,z_{k-1}\) and inner bits \(u,v,w\). Define
\[
H(z)=\prod_{j=1}^{k-1}(z_0+z_j),\qquad
M(u,v,w)=uv+uw+vw.
\]
Use gates independent of all pair parities:
\[
f_{z_i}=M(u,v,w)\ (0\le i<k),\qquad
f_u=v+H(z),\quad
f_v=w+H(z),\quad
f_w=u+v+z_0+H(z).
\tag{NO9}
\]
Each gate ignores its own bit. The function \(H\) is invariant under simultaneous complementation of all outer bits, whereas \(M\) changes value under simultaneous complementation of the three inner bits. These identities verify global oddness of every displayed gate.

Choose outer order \(z_0,\ldots,z_{k-1}\). Each outer gate satisfies (NO2), since it depends only on the three inner bits. The inner slope matrix is
\[
B=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad \det B=1.
\]
The theorem therefore gives \(2^k\) successful \(q\)-roots in every parity fiber for
\[
z_0\cdots z_{k-1}\,u v w\,u v w\,z_{k-1}\cdots z_0.
\tag{NO10}
\]
Every gate is nonlinear: \(M\) has degree two and \(H\) has degree \(k-1\). Every outer bit influences every inner gate through \(H\), and every inner bit influences every outer gate through \(M\). The directed influence graph is consequently strongly connected. Thus the theorem applies with arbitrarily many nonlinear gates and with feedback in both directions between the inner and outer sets.

Because (NO9) is independent of \(p\), it also defines a legal odd edge coloring of the smaller cube \(Q_m\), with direction-\(i\) rule \(f_i(q)\). The paired coloring is its complementary lift. Project a red geodesic supplied above onto the \(a_i\)-dimensions: an \(a_i\)-step occurs precisely when \(f_i(q)=0\), each such dimension occurs once, and the \(b_i\)-steps leave \(q\) unchanged. The projection is a red full antipodal geodesic of \(Q_m\). In particular this smaller-cube family has at least \(2^k\) distinct red starting roots.

### Scope

The theorem establishes a dimension-uniform nonlinear forcing class and supplies the root multiplicity needed by a square-fault forcing argument. Its assumptions retain the partial-complement symmetries (NO2) and an inner block affine in its own bits with a uniformly nonsingular slope. Arbitrary nonlinear paired-flat colorings need not satisfy these assumptions. Producing such an ordered decomposition at every hypothetical strict square boundary remains open, as does the arbitrary-rank odd-matrix peeling conjecture. No boundary-tournament specialization preserving distinct original vertices is established here; unrestricted NORI1 and the grand conjecture remain open.


## Odd singular parity cores and four-word nonlinear forcing

The following argument replaces nonsingularity of an inner slope block by a four-word certificate. The argument uses shared phase values and a reduction that removes two pair labels at a time.

### An odd parity core with arbitrary phase functions

Let \(r\ge3\) be odd. On \(Q_{2r}\), use direction pairs \((a_i,b_i)\), pair parities \(p_i=x_{a_i}+x_{b_i}\), and bits \(q_i=x_{a_i}\). Assign pair colors \(g_i,1+g_i\), where
\[
g_i(p,q)=\sum_{j\ne i}q_j+\theta_i(p_{\ne i}).
\tag{OPC1}
\]
The functions \(\theta_i\) are arbitrary. This coloring is antipodally even; the conclusion below permits either monochromatic color.

Choose three pair labels, call them \(0,1,2\), and partition all remaining labels into ordered pairs \((a,b)\). Let \(H\) concatenate the words \(abab\) for these pairs, in any fixed order. Set
\[
\begin{array}{ll}
v_A=010212,&v_B=012012,\\
v_C=012021,&v_D=102012,
\end{array}
\qquad
\mathcal V=\{Hv_A,Hv_B,Hv_C,Hv_D\}.
\tag{OPC2}
\]
Each word contains every pair label twice.

**Theorem (odd singular core).** For every prescribed initial parity \(p\), at least one word in \(\mathcal V\) has a monochromatic antipodal root. More precisely, the number of triples \((v,\varepsilon,q)\), where \(v\in\mathcal V\), \(\varepsilon\in\{0,1\}\), and the color-\(\varepsilon\) pair walk from \((p,q)\) ends at its antipode, is either four or twelve. Every counted walk is a full geodesic.

*Proof.* Put \(y_*=\sum_iq_i\) and \(y_i=q_i\). For a color-\(\varepsilon\) move in pair \(i\), the augmented bits undergo
\[
(y_*,y_i)\longmapsto(y_i+c,\ y_*+c),
\qquad c=1+\varepsilon+\theta_i(p_{\ne i}),
\tag{OPC3}
\]
with all other bits unchanged, while \(p_i\) toggles. Thus each move is an affine swap. The condition that augmented bits represent original bits is
\[
y_*+\sum_i y_i=0.
\tag{OPC4}
\]
Every affine swap preserves this parity.

First take \(r=3\), temporarily allowing all four augmented bits to be independent. Normalize the prescribed initial parity to zero by translating the phase tables. Write \(\theta_i[d]\), \(0\le d<4\), for the value of \(\theta_i\) at the outside parity packed in increasing label order, with the first outside label as the low bit.

For each word in (OPC2), the unsigned permutation of the four augmented bits has two cycles. The respective cycle partitions and conditions for a red augmented return \(y\mapsto y+\mathbf1\) are:

| Word | Cycle supports | Required equation |
|---|---|---|
| \(v_A\) | \(\{*\},\{0,1,2\}\) | \(\theta_0[0]+\theta_0[1]+\theta_2[0]+\theta_2[2]=1\) |
| \(v_B\) | \(\{*,1\},\{0,2\}\) | \(\theta_0[0]+\theta_0[3]+\theta_1[1]+\theta_1[2]+\theta_2[0]+\theta_2[3]=0\) |
| \(v_C\) | \(\{*,0,2\},\{1\}\) | \(\theta_1[0]+\theta_1[1]+\theta_2[2]+\theta_2[3]=1\) |
| \(v_D\) | \(\{*,0,2\},\{1\}\) | \(\theta_0[1]+\theta_0[3]+\theta_1[0]+\theta_1[2]=1\) |

Here is the algebra behind the table. Compose the six swaps (OPC3) with \(\varepsilon=0\), obtaining \(y\mapsto Py+d\). The equation \((P+I)y=\mathbf1+d\) is solvable if and only if the sum of \(d\) on each permutation cycle equals the length of that cycle modulo two. Since every swap adds its offset in two positions, \(\sum d=0\), and the two cycle equations are equivalent. Substitution of the six visited phase keys gives the displayed equations. When an equation holds, two permutation cycles give four augmented solutions.

The sum of the four left sides is zero, whereas the sum of their right sides is one. Consequently an odd number of the four equations holds: one or three. This is an identity on one shared collection of twelve phase values.

Let \(K\) toggle only \(y_*\). Conjugating a red affine swap by \(K\) gives the corresponding blue affine swap. Hence, if \(y\) is a red augmented antipodal root, \(Ky\) is a blue augmented antipodal root for the same word. Their parities differ. For either prescribed augmented parity \(\gamma\), each red augmented root therefore determines one colored root of parity \(\gamma\): keep \(y\) in red if its parity is \(\gamma\), and use \(Ky\) in blue otherwise. This correspondence is bijective. Each feasible word supplies four colored roots of prescribed augmented parity. Taking \(\gamma=0\) proves the three-pair claim.

Now remove one ordered pair \((a,b)\) using \(abab\). Let \(s,A,B\) be its initial augmented bits \(y_*,y_a,y_b\), and let \(c_1,c_2,c_3,c_4\) be the four offsets in (OPC3). The choice
\[
A=s+c_1+c_2+c_4,\qquad
B=s+c_1+c_3+c_4+1
\tag{OPC5}
\]
is the unique choice with prescribed center \(s\) for which this word fixes \(y_*\) and complements \(y_a,y_b\). Direct substitution into the four swaps proves the assertion. Moreover
\[
A+B=1+c_2+c_3
\tag{OPC6}
\]
is independent of \(s\) and of the common color \(\varepsilon\). The two appearances of \(1+\varepsilon\) cancel in this sum.

Every completed \(abab\) block restores its two parities and fixes the augmented center. Thus all offsets needed for later blocks are independent of the initial bits chosen in earlier blocks. Apply (OPC5) to every pair outside the distinguished triple. Let \(\Gamma\) be the sum of their values (OPC6). It depends on the phase tables and the prescribed parities, and is independent of the common color and the center bit.

The remaining three-pair problem must have augmented parity \(\Gamma\), by (OPC4). The three-pair argument supplies four colored roots for each feasible distinguished word with this prescribed parity. For every such root, (OPC5) determines the earlier pair bits uniquely in the same color. Conversely every full antipodal return along a word \(Hv\) must fix the center during each completed \(abab\) block, since complementing two original \(q\)-bits preserves their sum; its initial pair bits are therefore forced by (OPC5). The three-pair correspondence gives all roots. There are four or twelve in total.

Finally, restoring \(p_i\) and complementing \(q_i\) in a pair means traversing each of its two original dimensions once. Every counted walk therefore uses all \(2r\) original dimensions once. \(\square\)

### Nonlinear outer gates around the singular core

Return to a legal odd paired-flat coloring on \(Q_{2m}\), with gates \(f_i(p,q)\) ignoring \(p_i,q_i\). Order \(k\ge1\) outer labels \(S=(i_1,\ldots,i_k)\), and let the remaining set \(R\) have odd size \(r\ge3\). Assume the outer gates satisfy
\[
f_{i_t}(p,q+\mathbf1_{R\cup\{i_{t+1},\ldots,i_k\}})
=1+f_{i_t}(p,q)
\quad\text{for every }p,q,t,
\tag{OPC7}
\]
and assume the inner gates have the form
\[
f_j(p,q)=\sum_{\ell\in R\setminus\{j\}}q_\ell+
\theta_j(p_{\ne j},q_S),\qquad j\in R.
\tag{OPC8}
\]
All phase functions are arbitrary subject to legality of the whole coloring. In particular global oddness makes each \(\theta_j\) odd under simultaneous complementation of \(q_S\). The inner slope block \(J_r+I_r\) is singular, of rank \(r-1\).

**Theorem (four-word nonlinear forcing with a singular core).** Form the four words
\[
w_\nu=i_1\cdots i_k\,H v_\nu\,i_k\cdots i_1,
\qquad \nu\in\{A,B,C,D\},
\tag{OPC9}
\]
with \(H,v_\nu\) as in (OPC2) on \(R\). In every prescribed initial parity fiber, at least one of these four words has a red antipodal root. The total number of red root-word pairs in that fiber is at least \(2^{k+1}\).

*Proof.* Fix the initial parity \(p^0\). For either chosen color, the outer prefix is a bijection onto parity \(p'=p^0+\mathbf1_S\). Assign its postprefix outer bits \(z=q_S\) arbitrarily. During the inner word, \(p_S,z\) stay fixed. The inner gates are (OPC1) with arbitrary phase tables, so the odd-core theorem supplies four or twelve colored root-word pairs for this \(z\).

Return through the outer labels in reverse. At the two visits to \(i_t\), other pair parities agree, earlier outer bits are unchanged, and deeper bits have been complemented. Equation (OPC7) makes the two gate values complementary. In either common color, the two moves consequently traverse opposite members of pair \(i_t\). Thus every inner colored return extends to a full monochromatic antipodal geodesic.

Conversely, every successful full return along (OPC9) restricts to an inner colored antipodal return, and its initial state is recovered by inverting the prefix in that color. Summing over \(2^k\) choices of \(z\) gives at least \(4\cdot2^k\) colored root-word pairs. Global oddness maps red roots to blue roots in the same initial parity fiber and with the same pair word. Half the colored pairs are red, proving the lower bound. \(\square\)

The first outer gate can be replaced by any legal odd gate without changing this conclusion. More generally all outer gates may be replaced while retaining (OPC7). This follows from the proof and the equivalence between (OPC7) and invariance under simultaneous complementation of the earlier outer bits.

The class permits nonlinear dependence in every gate and arbitrary parity-dependent phase tables. For example let \(k\ge3\), let \(M\) be majority on three distinguished inner bits, and set
\[
G(z)=z_0+\prod_{j=1}^{k-1}(z_0+z_j).
\]
Take every outer gate to be \(M+\phi_i(p_{\ne i})\), and every inner phase to be \(G(z)+\psi_j(p_{\ne j})\), with arbitrary \(\phi_i,\psi_j\). Both \(M\) and \(G\) are odd and nonlinear, and \(G\) depends on every outer bit. All hypotheses hold. Every gate is nonlinear, and the directed \(q\)-influence graph is strongly connected: each outer bit influences all inner gates, the inner complete dependence graph is strongly connected, and its distinguished triple influences every outer gate.

### Parity transport for a family of words

Let \(\mathcal W\) be any finite family of full pair words in an arbitrary legal paired-flat coloring \(c\). Suppose their red antipodal root sets jointly meet every initial parity fiber; a different word may witness each fiber. For each label \(i\), define
\[
\Sigma_i(\mathcal W)=
\{(\eta_t)_{\ne i}:w\in\mathcal W,\ w_t=i,\ 
\eta_t=\sum_{s<t}e_{w_s}\}.
\tag{OPC10}
\]
Suppose gates are rewritten arbitrarily on exterior parity sets \(E_i\subseteq\mathbb F_2^{[m]\setminus\{i\}}\), and are unchanged elsewhere. The rewritten gates must define a coloring; their dependence on \(q\) inside those sets is unrestricted.

**Lemma (joint word-family transport).** Every initial fiber outside
\[
\bigcup_i\{p:p_{\ne i}\in E_i+\Sigma_i(\mathcal W)\}
\tag{OPC11}
\]
retains a red full geodesic. Consequently the rewrite preserves success whenever
\[
2\sum_i |E_i|\,|\Sigma_i(\mathcal W)|<2^m.
\tag{OPC12}
\]

*Proof.* Before step \(t\), pair parity is \(p+\eta_t\), independent of the selectors. A word can consult a changed gate \(i\) only when \(p_{\ne i}\in E_i+(\eta_t)_{\ne i}\). Outside (OPC11), every red walk in every word of the family encounters unchanged selectors, so it follows the same states after the rewrite. Choose its existing red witness in that fiber. Each exterior parity assignment leaves two possibilities for \(p_i\), giving the bound (OPC12). No single word is assumed to cover all fibers. \(\square\)

**Corollary (arbitrary nonlinear slab rewrites).** For the four words (OPC9), the cardinalities in (OPC10) are one on an outer label, two on a label in an \(abab\) block, and three on a distinguished triple label. Thus arbitrary nonlinear rewrites on \(s_O,s_P,s_T\) exterior parity slabs in those respective groups preserve success if
\[
2s_O+4s_P+6s_T<2^m.
\tag{OPC13}
\]
In particular any single exterior parity slab in any pair may be rewritten, since \(m=k+r\ge4\). This includes any one antipodally paired alternating-square switch.

*Proof.* An outer label's two occurrences enclose complete returns of all deeper labels, so their exterior prefix parities agree. An \(abab\) label has two exterior signatures, common to all four words. For the distinguished triple, suppressing the fixed outside prefix, the signature sets at labels \(0,1,2\) are respectively \(\{0,1,3\}\), \(\{0,1,2\}\), and \(\{0,2,3\}\), with the other two triple bits packed as above. Hence their cardinalities are three. Apply (OPC12). \(\square\)

The transport lemma applies to arbitrary paired-flat colorings with a witnessed fiber-covering word family. The odd-core theorem supplies this hypothesis for (OPC7)–(OPC8) through a four-word shared-phase identity. A single common word covering all fibers is unnecessary.

### Scope

These theorems establish a nonlinear forcing class with a singular inner slope block and a dimension-uniform nonlinear transfer across an entire parity slab. A hypothetical strict good/bad square boundary cannot have the displayed outer decomposition and inner parity rules on its good side. The proof supplies the root and word choices and verifies simplicity in the original cube.

A general nonlinear coloring need not satisfy (OPC7) or (OPC8). Deriving an appropriate decomposition, or another fiber-covering family with small sets (OPC10), at every hypothetical boundary remains open. The arbitrary-rank matrix-peeling problem is also unresolved. No reduction to vertex-simple boundary-tournament paths is asserted, and unrestricted NORI1 and grand closure remain open.


## Paired-midpoint collision tensorization and the two-pair base (session session_nori_r11755_1)

This section extends the paired-midpoint construction of note_dd297b14828b049d0221340b, with the two-part obstruction analysis in note_nori_xvi_midpoint_tensor_product_and_scarcity_barrier_20261018_r11755, version 2. For a paired-flat legal coloring on Q_(2m), let T_i be the unique red matching involution for direction pair i. For every order pi of the pair labels, write T_pi for their full sweep. Define W(c) as the number of triples (x,pi,rho) with T_pi(x)=T_rho(bar x), all roots and both orders counted. Such a collision yields a full red antipodal geodesic.

**Theorem (disjoint-block tensor product).** If c and d are paired-flat legal colorings on Q_(2m) and Q_(2k), then for their disjoint-block product c box d,

W(c box d)=binom(m+k,m)^2 W(c)W(d).

In particular w(c)=W(c)/(m!)^2 obeys w(c box d)=w(c)w(d).

**Proof.** The matching actions from the two blocks commute, since each acts only within its own block. Thus a full pair order on m+k labels has endpoint determined solely by its two restricted orders. For each prescribed ordered pair of restrictions there are binom(m+k,m) interleavings. Each equality of two full-sweep endpoints in the product splits into one such equality per block. The two independent interleavings contribute the squared binomial factor. QED.

**Theorem (two-pair normalization).** Every paired-flat legal coloring on Q4 has W=8, independently of its two arbitrary legal gates.

**Proof.** In F2 put p_i=x_(2i)+x_(2i+1), t_i=x_(2i). The gate outside pair 0 is t_1+a(p_1) and the gate outside pair 1 is t_0+b(p_0), because complementing both bits of the other pair must change the gate. The red pair matchings T_0,T_1 flip their corresponding parity bits and have linear parts, in t=(t_0,t_1),

L_0=[[1,1],[0,1]], L_1=[[1,0],[1,1]].

The resulting complete sweeps 01 and 10 have linear parts A=L_1 L_0=[[1,1],[1,0]] and B=L_0 L_1=[[0,1],[1,1]], satisfying A+B=I. Their affine constants depend on the initial p only. The antipodal map fixes p and adds (1,1) to t. For a given p, collisions with equal orders cannot happen since a sweep is a bijection. For each opposite-order choice, the equation comparing its two endpoints has coefficient matrix A+B=I on t and hence has one solution. There are four choices of p and two ordered opposite-order choices, giving W=8. QED.

Consequently, for any r, a product of r paired-flat Q4 blocks has normalized count w=2^r. In Q8 the two-block product has W=binom(4,2)^2*8^2=2304 and w=4. This falls below the known first good-to-bad square-switch scarcity bound w<=12, so unconditional lower bounds on w stronger than that threshold are unavailable. The linked note records the stronger all-dimensional obstruction to combining tensor amplification with a telescoped one-switch Lipschitz estimate.

**Scope.** Both the tensor identity and the two-pair computation are proved. The product argument retains arbitrary nonlinear gates. These results quantify midpoint witness multiplicity and rule out an unqualified counting shortcut; the strict one-internal-hit nonlinear square-boundary remains unresolved.

### Exterior pair-parity localization and nonlinear switch distance

Let \(c\) be a legal paired-flat coloring of \(Q_{2m}\), \(m\ge2\), with direction pairs \(\{a_i,b_i\}\), and use \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\) over \(\mathbb F_2\). A red pair step \(T_i\) toggles \(p_i\) and is a bijection. For a pair word \(w=(w_1,\ldots,w_{2m})\) containing each label twice, let \(X_c(w)\) be the roots of red full antipodal geodesics with that pair word and put
\[
\mathcal P_c(w)=\{p(x):x\in X_c(w)\}.
\]
For \(t\in[2m]\) set \(\eta_t=\sum_{s<t}e_{w_s}\in\mathbb F_2^m\). At step \(t\), a red \(w\)-walk starting in fiber \(p\) has pair-parity \(p+\eta_t\), independent of every gate.

**Lemma 7 (exterior parity of a paired-square hit).** Fix an alternating square \(F\) in the two directions of pair \(i\), together with its antipodal square \(\bar F\), and write \(S=E(F)\cup E(\bar F)\). There is a unique \(\sigma\in\mathbb F_2^{[m]\setminus\{i\}}\) such that all vertices of \(F\cup\bar F\) have outside pair-parity \(\sigma\). If a red pair-word walk meets \(S\) at position \(t\), then \(w_t=i\) and its starting parity satisfies
\[
p_{-i}=\sigma+(\eta_t)_{-i}.\tag{PL1}
\]
Thus for a fixed occurrence position \(t\) of label \(i\), red walks hitting \(S\) start in at most two pair-parity fibers, independent of their gate functions and initial \(q\)-values.

*Proof.* The exterior bits of \(F\) are fixed. Those of \(\bar F\) are their complements; simultaneous complementation of the two bits of an outside pair leaves that pair's parity unchanged. Therefore all eight square vertices have the same outside pair-parity \(\sigma\). Every pair step toggles just its own pair-parity bit. Hence the outside parity at step \(t\) is \(p_{-i}+(\eta_t)_{-i}\), which must equal \(\sigma\) when the traversed edge belongs to \(S\). This leaves just the unrestricted initial bit \(p_i\), giving two fibers. \(\square\)

**Theorem 8 (fiber-support critical sparsity).** Suppose \(c'=T_Sc\) has no monochromatic full antipodal geodesic. Then, for every pair word \(w\),
\[
\mathcal P_c(w)\subseteq
\bigcup_{\substack{2\le t\le2m-1\\ w_t=i}}
\{p:p_{-i}=\sigma+(\eta_t)_{-i}\},\qquad
|\mathcal P_c(w)|\le 2r_i(w),\tag{PL2}
\]
where \(r_i(w)\) is the number of internal occurrences of label \(i\). When both occurrences are internal, the right-hand union has only two fibers if pair \(i\) is isolated in the chord-interlacement graph of \(w\), and four otherwise.

*Proof.* The established two-hit exchange and cyclic endpoint repair show that, under the stated badness hypothesis, every red full geodesic of \(c\) meets \(S\) in a single strictly internal edge. Apply Lemma 7 at that position to every root in \(X_c(w)\). For two internal occurrences \(s<t\), the two parity signatures coincide precisely when each other label appears an even number of times between \(s\) and \(t\). Since each label occurs twice in \(w\), this is equivalent to the absence of a chord interlacing label \(i\). Otherwise their signatures differ and the two two-fiber sets are disjoint. \(\square\)

**Corollary 9 (fiber-spread preservation).** If some pair word \(w\) has red antipodal roots in more than \(2r_i(w)\) initial pair-parity fibers, *every* alternating-square switch in pair \(i\) preserves the existence of a monochromatic full geodesic. In particular, roots in all \(2^m\) fibers for one pair word guarantee preservation in every pair for \(m\ge3\), and for \(m=2\) whenever \(r_i(w)=1\).

**Theorem 10 (multi-square fiber-support budget).** Let \(c^\star\) be formed by flipping a union of \(t\) antipodally paired alternating squares, each involving the two directions of one pair, with a legal final coloring. For any pair word \(w\),
\[
|\mathcal P_c(w)|>4t\quad\Longrightarrow\quad
c^\star\text{ has a red full antipodal geodesic}.\tag{PL3}
\]
More precisely, there are at least \(|\mathcal P_c(w)|-4t\) initial pair-parity fibers in which *every* red full antipodal \(w\)-geodesic survives unchanged.

*Proof.* In each switched square pair and for either of the two positions occupied by its direction-pair label in \(w\), Lemma 7 excludes every initial parity except two possibilities. Therefore each square pair can affect red \(w\)-walks in at most four initial pair-parity fibers. The union of \(t\) supports affects at most \(4t\) fibers. All red \(w\)-walks in remaining fibers traverse no switched edge, hence survive the union of flips. \(\square\)

**Theorem 11 (nonlinear standard-lift and parity-static robustness).** Assume the paired-flat gates of \(c\) are independent of \(p\), but may be arbitrary nonlinear antipodally odd functions of \(q\). If \(c\) admits any red full antipodal geodesic, then the same pair word admits one in *every* initial parity fiber. Consequently:

1. For \(m\ge3\), **every single legal antipodal paired-square switch preserves success**, without any affine assumption on the gates.
2. For \(m\ge2\), any union of fewer than \(2^{m-2}\) legal paired-square switches preserves a red full antipodal geodesic.
3. For \(m=2\), every single legal paired-square switch also preserves success.

In particular these conclusions hold for every successful standard paired-flat lift \(c_{a_i}(x,y)=b_i(x)\), \(c_{b_i}(x,y)=1+b_i(x)\) of an antipodally odd coloring \(b\), regardless of the algebraic degree of its edge rules.

*Proof.* With \(p\)-independent gates, each red pair-step updates \(q\) by a function of \(q\) alone. Therefore the \(q\)-return condition for any fixed pair word is independent of the initial parity \(p\). A successful root \(q\) works for all \(2^m\) initial parity fibers, proving \(\mathcal P_c(w)=\mathbb F_2^m\). For \(m\ge3\), \(2^m>4\ge2r_i(w)\), so Corollary 9 applies to any switch. If \(4t<2^m\), Theorem 10 supplies the multiple-switch assertion. Finally, for \(m=2\), a successful pair word must alternate its two labels: two consecutive occurrences of one label cancel as the same red involution and cannot yield an antipodal endpoint. In an alternating word each pair has precisely one strictly internal occurrence, hence \(r_i(w)=1\) for both \(i\), and \(2^m=4>2\); Corollary 9 applies. \(\square\)

**Corollary 12 (improved affine and nested-core transfer).** Every parity-independent affine-slope paired-flat coloring with nonsingular slope matrix survives one paired-square switch already for \(m\ge2\). More generally, every parity-independent affine-slope paired-flat coloring admitting a valid nested-core peeling word survives one paired-square switch for \(m\ge3\), regardless of the rank or of the nonlinear parity-phase terms, because the established nested-core theorem supplies the *same* word and at least one antipodal red root in every starting parity fiber. For \(m=2\) the nonsingular core case gives the assertion.

These results are dimension-uniform and permit nonlinear switched gates. The ordinary lift class is a strict subclass of unrestricted paired-flat colorings; iterated switches leave that class, and the theorem grants survival through a bounded number of switches from one successful parity-static seed. Unrestricted NORI1 still requires a forcing mechanism for arbitrary parity-dependent nonlinear gates. A hypothetical critical good coloring must instead concentrate all roots for every fixed word into at most four parity fibers, and at most two for words with one internal hit of the switched pair. The boundary-tournament simple-path obligation remains separate.


### Parity-cylinder transport: arbitrary nonlinear gate rewrites on sparse slabs

Let \(c,c^\star\) be two legal paired-flat colorings on \(Q_{2m}\) with the same direction-pair partition. For each gate \(i\), define its *exceptional exterior parity set*
\[
E_i=\{u\in\mathbb F_2^{[m]\setminus\{i\}}:\exists q,\ f_i^c(u,q)\ne f_i^{c^\star}(u,q)\}.
\]
The gates may differ arbitrarily as functions of \(q\) inside an exceptional parity slab, subject only to the legality and paired-flat axioms. Let \(E=(E_1,\ldots,E_m)\). For any pair word \(w=(w_1,\ldots,w_{2m})\) put \(\eta_t=\sum_{s<t}e_{w_s}\) and
\[
H_w(E)=
\bigcup_{t=1}^{2m}
\{p\in\mathbb F_2^m:
(p+\eta_t)_{-w_t}\in E_{w_t}\}.\tag{PC1}
\]

**Theorem 13 (parity-cylinder avoidance).** Every red full antipodal \(w\)-geodesic of \(c\) whose initial parity \(p\notin H_w(E)\) remains a red full antipodal geodesic of \(c^\star\), with the same root and the same pair word. Moreover
\[
|H_w(E)|\le 4\sum_{i=1}^m |E_i|.\tag{PC2}
\]
Consequently,
\[
\boxed{|\mathcal P_c(w)|>4\sum_i|E_i|
\implies c^\star\text{ has a red full antipodal geodesic}.}\tag{PC3}
\]
These assertions are unrestricted in the algebraic degrees of the original and modified Boolean gates.

*Proof.* At step \(t\) of a red pair-word walk, the pair parity is \(p+\eta_t\). If \(p\notin H_w(E)\), the current exterior parity lies outside \(E_{w_t}\) for every step, so the two gate functions agree there at *all* states \(q\). Induction over the red pair-word walk gives identical successive vertices in the two colorings, and hence the same red geodesic. Each set in the union (PC1) contains \(2|E_{w_t}|\) initial parity vectors, because its \(w_t\)-th bit is unrestricted. Every pair label occurs twice, yielding (PC2). A successful \(p\in\mathcal P_c(w)\setminus H_w(E)\) establishes (PC3). \(\square\)

**Corollary 14 (nonlinear slab robustness).** If \(c\) admits a red full antipodal geodesic with pair word \(w\) in every initial pair-parity fiber, then *any* legal paired-flat modification affecting at most \(s\) distinct exterior parity slabs, counted across pair labels, preserves a red geodesic when \(4s<2^m\). In particular, for \(m\ge3\), **one whole slab may be rewritten by an arbitrary nonlinear antipodally odd gate function**, without losing a monochromatic full geodesic. For parity-independent gates, a single successful red full geodesic supplies the required full fiber support by Theorem 11.

Theorem 13 improves the earlier square-count budget when many square switches share exterior parity signatures. An exceptional slab contains up to \(2^{m-2}\) antipodally paired square-switch sites, yet its entire influence on a prescribed pair word is confined to four starting parity fibers. The geometry responsible is the projection of red pair steps to the parity cube; no independence assumption is imposed on the changed \(q\)-truth-table entries.

**Finite illustration.** On \(Q_8\), generate self-dual, parity-independent red gate functions, one for each of four direction pairs. For the word \(w=(2,3,1,0,2,0,1,3)\), an instance has 32 red antipodal roots, occupying all 16 initial parity fibers. Complementing the entire gate-0 truth table on exterior parity \(p_{-0}=000\), while preserving legal self-duality, changes the full-red-root membership at precisely the four initial parity fibers \(\{10,11,14,15\}\). Twenty-four of the original 32 red roots remain, including every root in the other twelve parity fibers. This finite test checks the exceptional-fiber projection, while the theorem follows from the symbolic parity argument for all dimensions.

**Limitation.** Arbitrary paired-flat colorings may have exceptional exterior parity sets covering most slabs relative to every successful parity-independent seed. Theorem 13 supplies a dimension-uniform nonlinear transfer from *fiber-spread* witnesses through sparse exterior-parity changes. Establishing such witness support at an arbitrary good/bad critical boundary is the unresolved hypothesis-production problem; the simple-path boundary-tournament conclusion remains independently open.


### Four-root square-switch support and affine midpoint-rank stability

Let \(c\) be a legal paired-flat coloring of \(Q_{2m}\) with direction pairs \(P_i=\{a_i,b_i\}\). Put \(p_i=x_{a_i}+x_{b_i}\) and \(t_i=x_{a_i}\), all in \(\mathbb F_2\). Write the pair colors as \(f_i(p_{-i},t_{-i})\) and \(1+f_i(p_{-i},t_{-i})\). The red pair-matching involution \(T_i\) flips \(p_i\) and changes \(t_i\) by \(1+f_i\). A red sweep using every pair once in order \(\pi\) induces a permutation \(F_\pi^p\) from the initial \(t\)-fiber at parity \(p\) to the terminal \(t\)-fiber at parity \(p+\mathbf1\). Define
\[
C_{p,\pi,\rho}(c)=\{t:F_\pi^p(t)=F_\rho^p(t+\mathbf1)\}.
\tag{SS1}
\]
Every element of this set supplies a red full antipodal geodesic: the two half-sweeps meet and jointly use both directions in every pair.

Let \(c'=T_Sc\) be a legal switch of an antipodal pair of alternating squares within pair \(i\). The switched gate values occur at two exterior assignments with common exterior parity \(u\) and complementary exterior fiber bits \(z,z+\mathbf1\). Let \(\alpha_{p,\pi}\) equal one when the exterior parity immediately before \(i\) is traversed in order \(\pi\) equals \(u\), and zero otherwise. This depends only on \(p,\pi,u\).

**Theorem (four-root support and robust midpoint collisions).** Let
\[
A_{p,\pi}=\{t:F_\pi^p(t)\ne F_\pi^{\prime p}(t)\}.
\]
Then
\[
|A_{p,\pi}|=4\alpha_{p,\pi},\qquad
|C_{p,\pi,\rho}(c')|\ge
|C_{p,\pi,\rho}(c)|-4(\alpha_{p,\pi}+\alpha_{p,\rho}).
\tag{SS2}
\]
In particular, a collision set of size greater than the subtraction budget supplies a full red antipodal geodesic in \(c'\).

*Proof.* Every matching before pair \(i\) is unchanged. Their composition bijectively maps starting fiber bits to the state just before \(i\). If the exterior parity there differs from \(u\), no input is affected. If it equals \(u\), the changed inputs are the two prescribed exterior fiber-bit vectors, each with either value of \(t_i\): four states. At each changed state the other member of pair \(i\) becomes red, and the two outputs differ. All later red matchings are unchanged and compose to a bijection, so the half-sweep endpoints differ on four starting roots. A former collision persists whenever its first root is outside \(A_{p,\pi}\) and its antipodal second root is outside \(A_{p,\rho}\). The two excluded sets together contain at most \(4(\alpha_{p,\pi}+\alpha_{p,\rho})\) roots. \(\square\)

**Corollary (affine collision-rank forcing).** Suppose for some \(p,\pi,\rho\) the two complete half-sweep endpoint maps are affine:
\[
F_\pi^p(t)=M_\pi t+b_\pi,\qquad
F_\rho^p(t)=M_\rho t+b_\rho.
\]
Let \(r=\operatorname{rank}(M_\pi+M_\rho)\). Their collision set is empty or is an affine subspace with \(2^{m-r}\) elements, since its defining equation is
\[
(M_\pi+M_\rho)t=M_\rho\mathbf1+b_\pi+b_\rho.
\tag{SS3}
\]
If the equation is consistent and
\[
2^{m-r}>4(\alpha_{p,\pi}+\alpha_{p,\rho}),
\tag{SS4}
\]
the switched coloring \(c'\) contains a red full antipodal geodesic. The switched gate may be nonlinear, and the other initial parity fibers may contain nonlinear gates.

**Corollary (adjacent interchange gives rank at most two).** Suppose the original gates \(f_i\) are affine in the fiber bits on each fixed pair-parity fiber; their slope matrices and affine offsets may depend arbitrarily on pair parity. If \(\pi,\rho\) differ by interchanging two consecutive pair labels, then
\[
\operatorname{rank}(M_\pi+M_\rho)\le2.
\tag{SS5}
\]
Consequently, for \(m\ge6\), an antipodal midpoint collision between such orders in any parity fiber certifies preservation of a red full antipodal geodesic across **every one** paired-square switch. If only one order can read the switched parity slab, \(m\ge5\) suffices. If neither order can read that slab, one collision suffices in any dimension.

*Proof.* The two affine sweeps have common initial and final segments. The exchanged two-step segments leave all fiber bits other than those of the exchanged pairs unchanged and finish in the same pair-parity fiber. Their difference therefore has image contained in a two-dimensional vector space. Left and right composition with the common invertible affine segments preserves the rank bound. A nonempty collision set has at least \(2^{m-2}\) roots by (SS3). This exceeds eight for \(m\ge6\) and exceeds four for \(m\ge5\), giving the claims by (SS2). \(\square\)

For a hypothetical good-to-bad switch, every collision set in the good coloring must be covered by its two four-root exceptional sets. In an affine starting fiber, every consistent collision equation must therefore have rank large enough that \(2^{m-r}\le4(\alpha_{p,\pi}+\alpha_{p,\rho})\). The theorem combines paired-square criticality and witness multiplicity on the same coloring. It complements parity-cylinder transport, which controls the distribution of one full-path word across starting parity fibers; here multiplicity is measured within a fixed parity fiber for two independently ordered half-sweeps.

This criterion is dimension-uniform and allows nonlinear gates after switching, but obtaining the necessary low-rank collision on an arbitrary critical good coloring remains open. It implies no boundary-tournament transfer without an additional reduction. A standalone checker sampled 200 legal paired-flat \(Q_6\) colorings, eight starting parity fibers, and all 15 order pairs, confirming four-root perturbation, affine collision cardinality, and rank at most two for adjacent swaps.


## Endpoint repeated-pair-word scarcity in all even dimensions at least eight

Let c be paired-flat on Q_(2m), with pairs P_i={2i,2i+1} and red matching involutions T_i. For a permutation pi, let X_c(pi pi) be the set of roots of red antipodal paths following the pair labels pi twice.

**Theorem.** For every m>=4 there is a successful paired-flat legal coloring c and a pair P_0 such that X_c(pi pi) is empty whenever pi begins or ends with 0.

**Seed (m=4).** Let E_i=255 xor (3<<(2i)), u=x&E_i, r=min(u,u xor E_i), and k=32i+rank_i(r), where rank_i orders the 32 canonical exterior masks increasingly starting from zero. Define f_i(x)=b_k xor [u!=r] and color directions 2i and 2i+1 respectively by f_i and 1 xor f_i. The low and high 64-bit words of b are f2f0669117119177 and 0fe04996433cc73c (hexadecimal). Since f_i ignores its pair bits and is complemented by global antipodality, this is a paired-flat legal coloring. The exhaustive standalone verifier nori_q8_endpoint_pairword_obstruction.cpp checks every edge identity and all 24 pair orders times 256 roots. All twelve words pi pi with pair 0 first or last have zero antipodal roots. The other twelve have 250 such roots. A red full geodesic has root 0 and original dimension order (1,2,4,7,0,3,6,5).

**Extension lemma and proof.** Extend any successful paired-flat coloring c by one pair P_m, retaining all old gates and choosing f_m(x)=x_(2j) for one old pair j. This gate is independent of the new pair and is antipodally odd. Given a red full old geodesic, use one new-pair red edge, then the old geodesic, then the other new-pair red edge. The old path flips x_(2j), so the two new red moves use opposite dimensions and the full path is red and antipodal. Conversely a red repeated-pair geodesic pi pi in the enlarged coloring projects onto the old bits as a red geodesic pi_old pi_old: old gates ignore the new pair. If 0 is first or last in pi it is first or last in pi_old. Thus the absence of such roots is preserved. Iterate from the Q8 seed. QED.

**Scope.** A positive lower bound for endpoint-prescribed X_c(pi pi) fails even among successful nonlinear paired-flat colorings and in arbitrarily high even dimension. In particular the critical square-boundary hypothesis |X_c(pi pi)|>8 cannot follow from success alone for these words. The obstruction does not exclude different pair words or additional critical-boundary hypotheses.

### Midpoint bottleneck in the opposite exterior parity fibers

Retain the setting of Theorem 8: a paired-flat legal coloring \(c\) on \(Q_{2m}\), a switched antipodal pair \(S\) of alternating squares in direction pair \(i\), common outside pair parity \(\sigma\), and a switched coloring \(c'=T_Sc\) having no monochromatic full geodesic. Put \(\omega=\sigma+\mathbf1\) in the \((m-1)\)-bit outside parity space. The set of starting pair-parity vectors \(p\) with \(p_{-i}=\omega\) consists of two fibers.

**Theorem 15 (opposite-fiber midpoint restriction).** Every red full antipodal geodesic of \(c\) whose starting parity satisfies \(p_{-i}=\omega\) crosses \(S\) at step \(m\) or step \(m+1\). In its pair word, each label \(j\ne i\) occurs once before the switched step and once afterward. Consequently the word belongs to one of the two families
\[
w=\pi\,i\,v,\qquad |v|=m,\quad v\text{ a permutation of }[m]\setminus\{i\}\text{ together with }i,\tag{MB1}
\]
or
\[
w=u\,i\,\rho,\qquad |u|=m,\quad u\text{ a permutation of }[m]\setminus\{i\}\text{ together with }i,\tag{MB2}
\]
where \(\pi,\rho\) permute the outside labels, and the displayed central \(i\) is respectively at position \(m\) or \(m+1\). The occurrence of \(i\) in \(u\) or \(v\) is the other occurrence. In particular, no red full geodesic rooted in either opposite exterior parity fiber can have a pair word with neither central position occupied by \(i\).

*Proof.* By the strict critical-boundary theorem, every red full geodesic must hit \(S\) once and internally. Its projection to the pair-parity cube is a closed walk of length \(2m\) using every label twice. The starting outside parity \(\omega\) differs from the outside parity \(\sigma\) of \(S\) in all \(m-1\) positions. A visit to \(S\) at step \(t\) therefore requires at least \(m-1\) outside-label steps before it, and at least \(m-1\) outside-label steps after it to restore the original outside parity. Thus
\[
t-1\ge m-1,\qquad 2m-t\ge m-1,
\]
so \(t\in\{m,m+1\}\). Each of the \(m-1\) outside labels must occur an odd number of times on each side of the hit; because it occurs twice in the full word, it occurs once on each side. The remaining step besides the hit and the \(2(m-1)\) outside steps is the other occurrence of \(i\), lying after the hit when \(t=m\) and before it when \(t=m+1\). This gives (MB1) and (MB2). \(\square\)

**Corollary 16 (distance-dependent temporal sector).** More generally, if a red critical geodesic starts in a pair-parity fiber at outside Hamming distance \(d\) from \(\sigma\), then its unique internal switched hit occurs at a time \(t\) satisfying
\[
d+1\le t\le2m-d.\tag{MB3}
\]
This temporal restriction is independent of the within-fiber bits, nonlinear gate values and chosen path order.

These are unrestricted necessary conditions on a hypothetical paired-flat square-critical boundary. When a separate theorem supplies red geodesics rooted in the opposite exterior parity fibers, Theorem 15 constrains those geodesics to two explicit midpoint-sweep families. The existence of such rooted geodesics in arbitrary dimensions, or a contradiction among their shared gate values, remains open. Neither the midpoint restriction nor the earlier fiber-cylinder transfer asserts a new universal forcing theorem.


**Corollary (bounded-block affine exchange and switch stability).** Under the affine-fiber hypotheses above, suppose pair orders \(\pi,\rho\) have a common prefix and suffix and differ only in the order of the same \(k\) consecutive pair labels. Then
\[
\operatorname{rank}(M_\pi+M_\rho)\le k.
\tag{SS6}
\]
If \(C_{p,\pi,\rho}(c)\ne\varnothing\) and \(m-k\ge4\), every one-square switch of \(c\) preserves a red full antipodal geodesic. If at most one of the orders reads the switched exterior parity slab, \(m-k\ge3\) suffices.

*Proof.* The two middle sweeps change only the \(k\) fiber bits in their common set of pair labels. The endpoint difference is supported on those \(k\) bits. Their common invertible affine prefix and suffix preserve the difference rank, proving (SS6). Any nonempty affine collision set has at least \(2^{m-k}\) elements. This exceeds eight if \(m-k\ge4\) and exceeds four if \(m-k\ge3\); the result follows from (SS2). \(\square\)

**Sharper adjacent-order case.** If the two exchanged adjacent labels include pair \(i\), the pair containing the switched square, the orders reach \(i\) with opposite values of the other exchanged pair parity. At most one order can read the modified exterior parity assignment. Thus \(\alpha_{p,\pi}+\alpha_{p,\rho}\le1\), and an affine-fiber adjacent-order collision survives any such switch whenever \(m\ge5\). If the two exchanged labels exclude \(i\), the orders have the same exterior parity before \(i\), so either neither or both are affected.

The local-exchange hypothesis cannot be deduced from the existence of a red full geodesic alone. The product of \(r\) paired-flat \(Q_4\) colorings has midpoint collisions, but every collision must reverse the order of both pair labels in each factor. Hence no two orders differing only in a proper consecutive middle block can collide. This all-dimensional obstruction is proved in note_nori_global_midpoint_exchange_product_barrier_20261018_r11785. Deriving local-exchange witnesses therefore requires additional interaction hypotheses.


### One-way gate decoupling and unrestricted nonlinear gate replacement

Let \(c\) be any paired-flat legal coloring on \(Q_{2m}\) with \(m\ge2\), and let \(T_i\) be the red matching associated to pair \(i\). Write the gate selector \(f_j(p,q)\) for pair \(j\), independent of its own bits \(p_j,q_j\) and satisfying \(f_j(p,q+\mathbf1)=1+f_j(p,q)\). Say pair \(i\) is *unread by the other gates* when, for every \(j\ne i\), the selector \(f_j\) is independent of both \(p_i\) and \(q_i\). This is a one-way condition: \(f_i\) may depend arbitrarily on all other pair bits.

**Theorem 17 (nonlinear unread-pair extension).** Suppose pair \(i\) is unread by the other gates. The following are equivalent:

(a) \(c\) has a red full antipodal geodesic.

(b) On the \(2m-2\) original directions outside pair \(i\), the inherited red pair-matching rules admit a red full antipodal geodesic, with the bits of pair \(i\) held fixed.

(c) \(c\) has a red full antipodal geodesic whose pair word begins and ends with \(i\).

Moreover (b) is independent of the fixed values of the two bits belonging to pair \(i\).

*Proof.* In (a), delete the two steps belonging to pair \(i\) from a red full antipodal geodesic. The remaining \(2m-2\) original directions each occur once. The selectors of all remaining pair labels are independent of the bits of pair \(i\), so their red transitions depend only on the outside state. The projected trajectory is therefore a red antipodal full geodesic on the outside pairs, proving (b).

For (b), choose an outside red geodesic from exterior state \(y\) to its complement \(\bar y\), with pair word \(v\), and choose any of the four possible states \(z\) of pair \(i\). In the full coloring, let \(Z=(z,y)\), and let \(X=T_i(Z)\). The first red \(i\)-step from \(X\) reaches \(Z\) because \(T_i\) is an involution. Follow the red outside geodesic to \(Z'=(z,\bar y)\); it remains red because outside gates do not read pair \(i\). Finally take the red \(i\)-step from \(Z'\).

At \(Z\) and \(Z'\), the outside pair parities agree and every outside first-member bit is complemented. Antipodal oddness of the gate \(f_i\) therefore exchanges the red choice between directions \(a_i\) and \(b_i\). The first and last red \(i\)-steps traverse the two different original directions of pair \(i\). Along the middle segment every outside original direction occurs once. Thus the concatenated red path has length \(2m\) and ends at the antipode of \(X\), proving (c). Condition (c) implies (a). The outside rules are independent of the fixed state of pair \(i\), proving the final assertion. \(\square\)

**Theorem 18 (arbitrary full-gate nonlinear replacement).** Suppose \(c\) is successful and pair \(i\) is unread by the other gates. Replace *the entire selector function* \(f_i(p_{-i},q_{-i})\) by any other selector \(g_i(p_{-i},q_{-i})\) obeying the paired-flat legality and antipodal oddness conditions; leave every gate \(j\ne i\) unchanged. The resulting coloring \(c^\star\) has a red full antipodal geodesic, with pair \(i\) occupying both endpoint positions. Thus any legal antipodally paired square switch in pair \(i\), and any sequence of such switches, preserves success in this class.

*Proof.* By Theorem 17, the success of \(c\) supplies a red outside full geodesic using only the gates \(f_j\), \(j\ne i\). Those gates are unchanged and do not read pair \(i\). The construction (b) to (c) of Theorem 17 applies with the new legal self-dual selector \(g_i\); its two cap steps again traverse opposite original directions. Hence \(c^\star\) is successful. The number and support of changes to gate \(i\) are unrestricted. \(\square\)

**Corollary 19 (dependency condition on a critical good side).** If \(c\) is successful and switching one antipodally paired alternating square in pair \(i\) produces a bad coloring, then *some other pair-gate must depend on either \(p_i\) or \(q_i\)*. Thus a hypothetical nonlinear critical boundary requires outward sensitivity from the switched pair to the remaining red matching rules. This restriction and the parity-fiber support restrictions of Theorem 8 hold on the same hypothetical coloring.

Theorem 18 is a dimension-uniform nonlinear transfer mechanism with an explicit shared-coloring hypothesis; it allows arbitrary Boolean truth-table changes across **all** exterior parity slabs of one gate. It is independent of affine slopes and of the exceptional-slab budget. It does not prove that a general critical coloring possesses an unread pair. At the unrestricted boundary, proving the necessary dependence and the severe fiber localization incompatible is a separate open obligation.


### Sink deletion as a counterexample-preserving reduction

Retain Theorem 17's hypothesis: pair \(i\) is unread by every gate \(j\ne i\).

**Theorem 20 (legal sink reduction and root-count factorization).** Removing pair \(i\) from \(c\) defines a legal paired-flat coloring \(c^{-i}\) on \(Q_{2(m-1)}\), whose red pair matchings are the restrictions of the \(T_j\), \(j\ne i\). For every outside pair word \(v\), containing each remaining pair twice,
\[
\boxed{|X_c(i\,v\,i)|=4\,|X_{c^{-i}}(v)|},\tag{SR1}
\]
and
\[
\boxed{\mathcal P_c(i\,v\,i)=\mathcal P_{c^{-i}}(v)\times\mathbb F_2},\tag{SR2}
\]
where the final bit corresponds to the deleted pair parity. Consequently, \(c\) has a monochromatic full antipodal geodesic if and only if \(c^{-i}\) does.

*Proof.* For \(j\ne i\), the selector \(f_j\) is independent of both bits of pair \(i\), so its restriction to the remaining pair bits is well-defined. The original self-duality relation \(f_j(p,q+\mathbf1)=1+f_j(p,q)\) becomes the same relation under complementation of the remaining \(m-1\) first-member bits, since \(f_j\) ignores \(q_i\). The own-pair independence of \(f_j\) also persists. Thus the restricted rules define a legal paired-flat coloring.

Fix an outside starting vertex \(y\) and any one of the four values \(z\) of the removed pair. For the full word \(i\,v\,i\), its first red step maps \(X=T_i(z,y)\) to \((z,y)\). The exterior \(v\)-walk then follows precisely the red \(v\)-walk of \(c^{-i}\), independently of \(z\). It reaches the complemented exterior vertex precisely when \(y\in X_{c^{-i}}(v)\). In that case the final red \(i\)-step uses the opposite original direction from the first, by the gate's antipodal oddness; the full endpoint is the antipode of \(X\). Conversely, if the full word reaches the antipode, its outside projection reaches the outside antipode. The map \((z,y)\mapsto X=T_i(z,y)\) is bijective and preserves the outside starting state; it gives four full starting roots for each outside successful root \(y\), proving (SR1). The four roots attain both values of the initial pair parity \(p_i\), proving (SR2).

The equivalence of success follows in one direction from this construction and in the other by deleting the two \(i\)-steps of any red full antipodal geodesic, as in Theorem 17. Since any monochromatic full geodesic of a legal coloring can be globally complemented to a red one, the equivalence holds for monochromatic success. \(\square\)

**Corollary 21 (dependency-core necessity).** Define a directed dependency graph on pair labels by placing \(i\to j\) whenever \(f_j\) depends on either \(p_i\) or \(q_i\). A paired-flat counterexample of least possible pair count has no vertex of outdegree zero. More generally, repeated deletion of outdegree-zero labels preserves the existence or absence of a monochromatic full antipodal geodesic, and produces a reduced legal paired-flat instance whose dependency graph has minimum outdegree at least one. Deleting such pairs also preserves nonlinear within-fiber dependencies among all remaining gates.

*Proof.* An outdegree-zero label is unread by every other gate. Apply Theorem 20 to delete it, retaining a legal paired-flat instance with the same success status. Repeating terminates in the stated dependency core. A minimal counterexample cannot admit a deletion because it would produce a smaller counterexample. \(\square\)

A critical square switch in pair \(i\) leaves all other gate functions unchanged, so when \(i\) is a dependency sink the reduction also proves preservation under *any entire-gate rewrite* of \(f_i\), as in Theorem 18. The sink condition itself need not hold for an arbitrary critical coloring. This result is a counterexample-preserving dimension reduction, rather than a proof that the remaining cyclic dependency core is always successful.


## Simultaneous scarcity for all repeated pair words in Q8

For any permutation pi of four pair labels, let X_c(pi pi) be the red antipodal roots for the repeated pair word. For any label i, let r_i(pi pi) count the occurrences of i in strictly internal positions.

**Proposition (exhaustively verified).** There exists a successful paired-flat legal coloring c of Q8 with |X_c(pi pi)|<=8 for every pi. Hence |X_c(pi pi)|<=8r_i(pi pi) for every pi and every switched pair label i. Thus no single repeated pair word meets the known sufficient root-multiplicity criterion for a critical square switch.

**Proof certificate.** In the preceding canonical Q8 gate indexing, let low 64 bits b2f0741136139912 and high 64 bits 07ec0d14623c8779 (hexadecimal). The verifier nori_q8_allpair_root_scarcity.cpp checks undirectedness, antipodal oddness, and all 24 pair permutations at all 256 roots. Every root count is between 5 and 8; their sum is 176. A red antipodal geodesic has root zero and dimension order (0,2,5,6,1,4,3,7). This finite exhaustive check proves the statement.

**Scope.** Mere success fails to produce a repeated-word forcing witness, even when all possible switched pairs are considered jointly. The proposition does not impose the additional strict internal-hit conditions of a hypothetical critical good/bad boundary, and it does not address multiple pair words used together.

### Global low-rank midpoint exchange in a cyclic reader system

For \(m\ge3\), consider the legal paired-flat coloring \(c^{\mathrm{cyc}}\) with gates
\[
f_i(p,t)=t_{i+1}\quad(i\pmod m).
\]
Antipodal complementation changes each gate value, and each gate ignores both bits of its own pair. Its red pair matching updates \(t_i\mapsto t_i+1+t_{i+1}\), with all other fiber bits fixed. This gives a strongly connected directed cycle of dependencies.

**Theorem (full-width exchange with rank two).** For
\[
\pi=(0,1,\ldots,m-1),\qquad \rho=(1,\ldots,m-1,0),
\]
in every initial pair-parity fiber \(p\),
\[
C_{p,\pi,\rho}(c^{\mathrm{cyc}})
=\{t:t_1=1,\ t_2=0\}.
\tag{CY1}
\]
Consequently this collision set has \(2^{m-2}\) roots, and
\[
\operatorname{rank}(M_\pi+M_\rho)=2.
\tag{CY2}
\]
For \(m\ge6\), any single legal paired-square switch of \(c^{\mathrm{cyc}}\) retains at least \(2^{m-2}-8>0\) collisions in each initial parity fiber for these two orders.

*Proof.* In order \(\pi\), pair \(i\) is read before pair \(i+1\) for \(0\le i\le m-2\), whereas pair \(m-1\) reads the already updated bit \(t_0\). Thus the output \(y=F_\pi^p(t)\) is
\[
y_i=t_i+1+t_{i+1}\quad(0\le i\le m-2),
\qquad y_{m-1}=t_{m-1}+t_0+t_1.
\]
For order \(\rho\), the output \(z=F_\rho^p(s)\) is
\[
z_i=s_i+1+s_{i+1}\quad(1\le i\le m-2),
\qquad z_{m-1}=s_{m-1}+1+s_0,
\qquad z_0=s_0+s_1+s_2.
\]
Set \(s=t+\mathbf1\). Then the components \(1,\ldots,m-2\) agree automatically. Component \(m-1\) agrees precisely when \(t_1=1\), and component \(0\) agrees precisely when \(t_2=0\). This proves (CY1). The two nontrivial independent linear conditions give (CY2), and the switch-survival conclusion follows from (SS2). \(\square\)

An important limitation accompanies this construction. No midpoint collision in \(c^{\mathrm{cyc}}\) comes from two orders with a common prefix and suffix that merely reorder a proper middle set of pair labels. The proof uses a label in that set whose unique reader lies outside it; this forces a surviving bit discrepancy. It is recorded, along with the product-block obstruction, in note_nori_global_midpoint_exchange_product_barrier_20261018_r11785 v2.

This example exhibits a long exchange whose endpoint-map difference nevertheless has bounded rank. Thus controlling *rank* can give switch stability beyond the bounded-exchange-width regime. Producing such a low-rank compatible pair of sweeps in arbitrary nonlinear critical colorings remains the missing forcing step.


### Terminal one- and two-pair seams force square-switch preservation

Let \(c\) be a legal paired-flat coloring of \(Q_{2m}\), with direction pairs \(P_i=\{a_i,b_i\}\) and gate rules \(c_{a_i}=f_i,\ c_{b_i}=1+f_i\). Each \(f_i\) ignores its own pair and satisfies \(f_i(\bar x)=1+f_i(x)\). Put an arc \(j\to i\) in the pair-dependency digraph when \(f_i\) reads either bit of pair \(P_j\). A *terminal component* is a strongly connected component with no outgoing arcs. If \(B\) is such a component, put \(R=[m]\setminus B\). Every \(R\)-gate ignores all bits in \(B\).

**Lemma (flexible terminal seam).** Suppose the \(R\)-rules have a red full antipodal geodesic \(H\), with \(R\)-root \(y\). One can complete \(H\) by inserting all \(B\)-directions before and after it, keeping its \(B\)-state \(u\) constant during \(H\), for all four \(u\in\mathbb F_2^2\) if \(|B|=1\), and for at least twelve \(u\in\mathbb F_2^4\) if \(|B|=2\). Here the \(B\)-rules may depend arbitrarily and nonlinearly on the \(R\)-bits.

*Proof.* The \(R\)-edge colors are independent of \(B\), so the middle segment stays red. Let \(A\) be the ordinary paired-flat \(B\)-edge coloring in the exterior state \(y\). At \(\bar y\), antipodal oddness gives \(A^+_d(v)=1+A_d(\bar v)\). In a single pair, use at \(y\) the unique red member before \(H\) and the other member at \(\bar y\) after \(H\). The gate ignores both bits of its pair, so every prescribed middle state \(u\) is possible.

For two pairs, label their dimensions \(0,1,2,3\). Write \(A_0=a(v_2,v_3), A_1=1+a(v_2,v_3), A_2=b(v_0,v_1), A_3=1+b(v_0,v_1)\), for arbitrary two-bit Boolean tables \(a,b\). For a permutation \(\pi\in S_4\), cut \(0\le h\le4\), and frozen state \(u\), take initial \(B\)-root \(u+\sum_{j\le h}e_{\pi_j}\); use the first \(h\) steps with rules \(A\), traverse \(H\), and take the remaining steps with \(A^+\). The finite four-direction seam calculation checks all \(16^2\) gate-table pairs, all sixteen middle states and all \(24\cdot5\) order/cut possibilities. For 240 table pairs all sixteen middle states work; for the other sixteen, twelve work. More intrinsically, failure occurs only for mutual unary readers \(a(v)=v_r+\alpha\), \(b(v)=v_s+\beta\), with \(r\in\{2,3\}\), \(s\in\{0,1\}\), and then only at the four \(u\) satisfying \(a(u)=\mathbf1_{\{s=0\}}\), \(b(u)=\mathbf1_{\{r=2\}}\). This proves the bound. \(\square\)

**Theorem (small terminal component preserves every single square switch).** Suppose \(c\) has a red full antipodal geodesic and its pair-dependency digraph has a terminal component \(B\) of one or two pair labels. For *every* antipodal pair \(S\) of alternating squares supported in one direction pair, the switched legal coloring \(T_Sc\) has a red full antipodal geodesic.

*Proof.* Delete the \(B\)-steps of an existing red full antipodal geodesic of \(c\). The other edge colors ignore \(B\), hence the remaining full \(R\)-geodesic \(H\) is red.

If the switched pair lies in \(B\), the switch alters only one \(B\)-gate; the \(R\)-rules and \(H\) remain unchanged. The switched coloring still obeys the paired-flat and oddness laws, so the flexible terminal-seam lemma applied to its new \(B\)-rules completes \(H\) to a red full geodesic.

Suppose the switched pair lies in \(R\). The switched set \(S\) projects onto just two complementary \(B\)-states \(u_S,\bar u_S\), corresponding to its square and antipodal square. By the lemma, choose a successful middle state \(u\) outside these two states: four choices are successful if \(|B|=1\), and at least twelve if \(|B|=2\). During the embedded middle geodesic \(H\), the state in \(B\) is \(u\), so no \(R\)-edge of \(H\) lies in \(S\). The other path edges move in \(B\)-directions and cannot lie in \(S\). The resulting red full geodesic avoids \(S\) and remains red after the switch. \(\square\)

**Simultaneous avoidance corollary.** If \(|B|=2\), the same construction avoids any five prescribed antipodal square-pair orbits supported in \(R\), simultaneously: at most ten of the sixteen frozen \(B\)-states are excluded, while at least twelve support seam completion. If \(|B|=1\), it avoids one prescribed such orbit.

**Critical-boundary corollary.** In any hypothetical neighboring good/bad paired-flat colorings differing by a single legal antipodal alternating-square switch, *every terminal strongly connected component of the pair-dependency digraph on the good side contains at least three pair labels*. This necessary condition coexists with the established balanced good/bad normalization and strict one-internal-hit witness restriction, and holds for nonlinear gates of unrestricted dependence elsewhere.

**Small-component forcing corollary.** If every strongly connected pair-dependency component contains at most two pair labels, then the coloring has a red full antipodal geodesic. To prove this, delete a terminal component \(B\). Its removal leaves a legal paired-flat coloring on the remaining pairs, since those rules ignore \(B\) and retain the antipodal identity on their remaining inputs. Apply induction to obtain a red \(R\)-geodesic and then the flexible terminal-seam lemma. This yields arbitrarily high-dimensional nonlinear forcing. The more useful critical-boundary theorem needs only one small terminal component; it imposes no bound on the other components.

**Remaining problem.** A critical good coloring may have terminal dependency components of three or more pairs. The finite six-dimensional square-avoidance theorem concerns gates odd under the six-dimensional antipode, whereas the three-pair seam at a frozen exterior state has arbitrary Boolean gate tables. Transferring six-dimensional avoidance through these two exterior layers is a separate unresolved requirement.


**Corollary (whole-gate replacement of a small terminal block).** Under the preceding theorem, replace *all* gates with labels in \(B\) by arbitrary new legal paired-flat gates satisfying global antipodal oddness, while leaving every gate outside \(B\) unchanged. The resulting coloring has a red full antipodal geodesic. More generally, alongside these whole-gate replacements one may switch one antipodal square-pair orbit outside \(B\) when \(|B|=1\), or any set of at most five such orbits when \(|B|=2\), and retain a red full geodesic.

*Proof.* The old red geodesic projects to a red full path \(H\) on the outside labels, and the outside gates are unaffected by the whole-gate replacement. Apply the flexible terminal-seam lemma to the *new* \(B\)-rules. When outside square orbits are also switched, choose a successful frozen \(B\)-state outside the at most two forbidden projections for each orbit. The middle segment then avoids every changed outside edge, while both cap segments move only in \(B\)-directions and use the new red gates. The bounds four and twelve on successful frozen states prove both assertions. \(\square\)

This extends the earlier single unread-pair arbitrary-gate replacement theorem to *two mutually dependent pair gates*, with nonlinear dependence on the remaining pairs. The terminal-block hypothesis is imposed only on the unchanged outside rules; the replacement gates may introduce new incoming dependencies and need not preserve the old condensation digraph.


### Three-pair terminal seams: nonlinear completion, exclusion, and dependency-core reduction

Write \(P_i=\{a_i,b_i\}\), \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\), over \(\mathbb F_2\). A legal paired-flat coloring has red selector \(f_i(p_{-i},q_{-i})\), with \(f_i(p,q+\mathbf1)=1+f_i(p,q)\). A set \(S\) of pair labels is *outgoing-closed* when every gate labeled outside \(S\) ignores every bit belonging to \(S\). Deleting an outgoing-closed set produces a legal paired-flat coloring \(c^{-S}\), since the remaining gates inherit own-pair independence and the antipodal identity.

**Finite three-pair seam lemma.** Fix three internal pair labels \(0,1,2\), and two exterior states \(y,\bar y\) connected by a red full geodesic using all exterior directions once. At \(y\), the three internal selectors \(h_i(p_{-i},q_{-i})\) are arbitrary Boolean functions of four bits. At \(\bar y\), legal antipodal oddness forces
\[
h_i^{+}(p_{-i},q_{-i})=1+h_i(p_{-i},q_{-i}+\mathbf1).
\tag{TS1}
\]
Use the symbol \(E\) to denote the exterior red geodesic, which leaves the internal state fixed. Let a *completion word* contain each internal label twice and \(E\) once, with red matching steps at the current exterior stage.

(a) For every triple of the \(2^{16}\)-choice internal gate tables and every prescribed initial internal parity \(p\in\mathbb F_2^3\), some completion word and some initial \(q\in\mathbb F_2^3\) give the internal antipode.

(b) For any two antipodal pairs of frozen internal vertices, there are a completion word and a starting internal vertex such that the completed red path reaches the internal antipode and the frozen internal vertex at the \(E\)-step avoids both forbidden antipodal pairs. The starting parity may depend on the forbidden pairs.

*Finite proof.* Write the six original internal bits in the order \(a_0,b_0,a_1,b_1,a_2,b_2\), and write the pre-\(E\) gate bit of label \(i\) as \(z_{i,4P+Q}\), where \(P,Q\in\mathbb F_2^2\) encode the parity and first-member bits of the other two labels in increasing order. There are 48 independent Boolean variables. For a proposed original-direction path, with \(s=0\) before \(E\) and \(s=1\) after \(E\), traversal of member \(\epsilon\in\{0,1\}\) in pair \(i\) requires the gate equation
\[
z_{i,\,4P+(Q+s\mathbf1)}=\epsilon+s.\tag{TS2}
\]
Enumerate the 630 words in the multiset \(\{0,0,1,1,2,2,E\}\), the starting internal vertices, and the two possible assignments of the first/second member order in each pair. If any candidate path demands contradictory values of one gate variable, discard it. Otherwise form the disjunctive clause saying at least one of its demanded values fails. The conjunction of all clauses is satisfiable precisely when some triple of gate tables blocks every admissible completion.

For (a), fix initial parity \(000\). The 630 words, eight initial \(q\)-states and eight member-order choices give 13,440 distinct consistent blocking clauses of lengths five and six. A complete Boolean DPLL refutation visits 2,799 recursion nodes and returns UNSAT. Translation of the original six internal bits takes any prescribed parity to \(000\) and preserves (TS1), so (a) follows.

For (b), translate the first forbidden antipodal middle-state pair to \(\{0,63\}\), and write the second as \(\{v,63+v\}\) with \(1\le v\le31\), using six-bit XOR for addition. For each of the 31 possibilities, enumerate all 64 starting internal vertices and retain only paths whose frozen middle state avoids these four forbidden vertices. The 31 resulting blocking CNFs are UNSAT. A direct complete DPLL refutation visits between 183 and 263 recursion nodes in each case. The clause generator and DPLL checker use integer bit operations with no SAT-library dependency. The independent earlier parity-gate and original-bit generators agree on all 13,440 clauses of (a), and the original-bit and parity-gate avoidance generators agree on sampled normalized cases. These finite, exhaustively certified lemmas impose no affine condition on the gates. \(\square\)

**Theorem (three-pair outgoing-closed deletion).** Let \(c\) be an arbitrary legal paired-flat coloring of \(Q_{2m}\). If \(S\subseteq[m]\) is outgoing-closed with \(|S|=3\), then
\[
c\text{ has a red full antipodal geodesic}
\quad\Longleftrightarrow\quad
c^{-S}\text{ has one}.\tag{TS3}
\]
This equivalence holds separately in every prescribed starting pair-parity fiber.

*Proof.* For the forward implication, project a red full geodesic onto the directions outside \(S\). Their gate functions ignore all internal bits, so projection retains the colors, uses every remaining original direction once, and reaches the outside antipode. It also preserves the starting outside pair parity. Conversely, let \(E\) be any exterior red full geodesic from \(y\) to \(\bar y\), rooted in any prescribed exterior parity fiber. It remains red regardless of the internal state because all exterior gates ignore \(S\). Freeze the internal state during \(E\); the selectors before and after \(E\) satisfy (TS1). Apply finite lemma (a) for any prescribed internal starting parity. The resulting full path is red, uses each of the six internal original directions once, and uses each exterior original direction once in \(E\). It therefore connects antipodes and proves the fiberwise assertion. \(\square\)

**Theorem (two-orbit nonlinear square-switch stability).** Under the hypotheses of (TS3), suppose \(c\) is successful. Replace *all three internal gates* in \(S\) by arbitrary other legal paired-flat gates, retaining the exterior gates. In addition, switch at most two antipodally paired alternating-square orbits, each supported in a direction pair outside \(S\). The resulting legal coloring still has a red full antipodal geodesic.

*Proof.* Project an original red full geodesic to an exterior red full geodesic \(E\). Each switched outside-square orbit has its two constituent squares at an antipodal pair of fixed internal vertices. By finite lemma (b), choose a completion of \(E\) under the *new* internal gates whose internal middle state avoids these at most two antipodal pairs. Throughout the exterior segment, the internal state is frozen at that middle vertex, so none of its edges belongs to any switched outside-square orbit; all exterior edges remain red. The two red internal cap segments traverse only directions in \(S\), and therefore cannot meet the switched outside edges. Their selectors are those of the new legal gates and obey (TS1). The completed geodesic remains red. \(\square\)

**Corollary (dependency-core obstruction).** For the dependency digraph with an arc \(i\to j\) when gate \(j\) reads some bit of pair \(i\):

1. If all strongly connected components have at most three vertices, every legal paired-flat coloring is successful, and it has a red full antipodal geodesic in every starting pair-parity fiber. Delete sink components of sizes one, two, and three successively, then reinsert them using the corresponding fiberwise seam completion lemmas.
2. In any good-to-bad critical boundary differing by one legal antipodally paired square switch, *every terminal strongly connected component of the good-side dependency digraph has at least four vertices.* Indeed, if a terminal component has size at most three, the archived one- and two-pair terminal-seam theorems, or the three-pair theorem above, preserve red success across the switch whether it lies inside or outside the terminal component.
3. If the switched label belongs to any outgoing-closed subset of at most three pair labels, the switch cannot destroy success. Thus a hypothetical critical switched label has a forward dependency-reachability set containing at least four labels.

These results apply to arbitrary nonlinear within-pair gate truth tables. They produce a dimension-uniform *dependency-structure restriction*, not unrestricted NORI1 closure. The surviving hypothetical counterexamples have large terminal feedback components. The separate boundary-tournament simple-path conclusion remains open.


### Unrestricted square-safe antipodal permutation rank theorem

Fix any legal paired-flat coloring of \(Q_{2m}\). In a prescribed starting pair-parity fiber \(p\), every red half-sweep pair order \(\pi\) induces a permutation \(F_\pi^p\) of the \(N=2^m\) fiber states. Let \(P_\pi\) be its permutation matrix, \(J\) the complement permutation on fiber states, and
\[
B(A,D)=\operatorname{tr}(A^{\mathsf T}DJ).
\tag{AR1}
\]
The quantity \(B(P_\pi,P_\rho)\) counts roots whose red \(\pi\)-sweep meets the red \(\rho\)-sweep from the antipodal root. Each collision produces a red full antipodal geodesic.

**Theorem (unrestricted rank forcing).** If a nonempty family \(\mathcal H\) of pair orders has no such collisions, then
\[
\dim_{\mathbb R}\operatorname{span}
\{P_\pi-P_{\pi_0}:\pi\in\mathcal H\}
\le\frac{(N-1)(N-2)}2.
\tag{AR2}
\]
*Proof.* Write \(U=\mathbf1\mathbf1^{\mathsf T}/N\) and \(Q_\pi=P_\pi-U\). On the space of doubly centered matrices, \(B\) has positive index \((N-1)(N/2-1)\) and negative index \((N-1)N/2\): on the column zero-sum space, \(J\) has positive and negative eigenspace dimensions \(N/2-1,N/2\), and the row zero-sum space has dimension \(N-1\). Since \(B(P_\pi,U)=B(U,P_\rho)=B(U,U)=1\), absence of collisions implies \(B(Q_\pi,Q_\rho)=-1\) for all orders. Fix \(Q_0\), whose squared \(B\)-norm is \(-1\). All differences \(Q_\pi-Q_0\) lie in the \(B\)-orthogonal complement of \(Q_0\) and are mutually \(B\)-isotropic. Their dimension is therefore bounded by the positive index, giving (AR2). \(\square\)

**Critical-square corollary.** Let a paired-square switch \(S\), supported in pair \(i\) at exterior parity \(u\), transform a successful coloring into a bad one. Let \(\mathcal H(p,S)\) be the pair orders for which the exterior parity immediately before \(i\) differs from \(u\). Their complete endpoint maps are unaffected by switching \(S\). Therefore (AR2) holds for the original coloring restricted to \(\mathcal H(p,S)\), for every \(p\). If the forbidden predecessor subset has size \(k\), precisely \(k!(m-1-k)!\) orders are excluded; hence
\[
|\mathcal H(p,S)|\ge (m-1)(m-1)!.
\tag{AR3}
\]
For \(m\ge8\), affine independence of these square-safe sweep maps forces survival of a red full geodesic, because the family is larger than the rank ceiling plus one. No affine or bounded-dependency hypothesis is imposed on the coloring itself.

**Bidirectional support law.** Because each red matching is an involution,
\[
F_{\operatorname{rev}\pi}^{p+\mathbf1}
=(F_\pi^p)^{-1}.
\tag{AR4}
\]
Reversal preserves square safety when starting parity changes from \(p\) to \(p+\mathbf1\). Accordingly, at any hypothetical critical square, the union of all square-safe permutation graphs has no complementary pair of sources sharing one endpoint, and no complementary pair of endpoints sharing one source. Every vertex in this bipartite incidence graph has degree at most \(N/2\).

The theorem gives a dimension-uniform sufficient forcing condition and an unrestricted necessary condition for criticality. Producing the required large rank or contradictory support geometry in arbitrary critical colorings is unresolved. The full proof record and finite checks appear in note_d0da03890cda4141501176d0 and nori_unrestricted_square_safe_geometry.md.



### Acyclic-orientation ceiling for square-safe permutation ranks

Let \(H\) be the undirected interaction graph of a legal paired-flat coloring: two pair labels \(i,j\) are adjacent if either gate \(f_i\) depends on \(p_j,q_j\), or \(f_j\) depends on \(p_i,q_i\). Let \(a(H)\) be the number of acyclic orientations of \(H\).

**Theorem (order factorization).** For every prescribed starting parity \(p\), the red half-sweep endpoint permutation \(F_\pi^p\) depends only on the acyclic orientation of \(H\) induced by \(\pi\). Consequently, for any nonempty family \(\mathcal H\) of pair orders,
\[
\dim_{\mathbb R}\operatorname{span}\{P_\pi-P_{\pi_0}:\pi\in\mathcal H\}
\le a(H)-1.
\tag{AO1}
\]

*Proof.* The red pair-step involution is \(T_i(p,q)=(p+e_i,q+(1+f_i(p,q))e_i)\). If \(ij\notin E(H)\), each gate ignores both bits of the other pair, so \(T_iT_j=T_jT_i\) in every state. Swapping adjacent noninteracting labels leaves the endpoint permutation unchanged. Every linear order induces an acyclic orientation of \(H\); orders inducing the same orientation are related by swaps of adjacent incomparable labels in its topological ordering. Each such pair is nonadjacent in \(H\), so the corresponding endpoint permutations agree. At most \(a(H)\) distinct permutation matrices occur, proving (AO1). \(\square\)

**Corollary (dimension-uniform limit on the rank-forcing criterion).** Put \(N=2^m\), \(D=(N-1)(N-2)/2\). The preceding criterion (AR2) can certify a monochromatic antipodal geodesic from a family of half-sweep orders only if
\[
a(H)\ge D+2.
\tag{AO2}
\]
If \(m\ge3\) and \(H\) has at most \(2m-2\) edges, then \(a(H)\le2^{2m-2}\le D\), and no such family, including any square-safe family, can exceed the forcing rank. The statement concerns the sufficiency of the rank certificate; it makes no assertion that the coloring lacks red geodesics.

Even a strongly connected pair-dependency digraph need not supply the necessary rank. Take \(f_i(p,q)=q_{i-1\pmod m}\). Its directed dependency graph is an \(m\)-cycle and \(H=C_m\), with
\[
a(C_m)=2^m-2,\qquad
\dim\operatorname{span}\{P_\pi-P_{\pi_0}\}\le2^m-3.
\tag{AO3}
\]
The rank ceiling in (AR2) grows on the order of \(4^m\), while (AO3) grows on the order of \(2^m\). The cyclic example is a successful coloring; it establishes a limit of the rank method under arbitrarily large strongly connected dependency blocks.

The restriction is sharp enough to matter for the smallest dimension in which the safe-order count can exceed (AR2). At \(m=8\), \(N=256\) and \(D=32385\). When \(H=K_8\) with one missing edge, \(a(H)=8!-7!=35280\), leaving room for the rank criterion. With two missing edges, \(a(H)\le8!-2\cdot7!+6!=30960\); if they share a vertex, \(a(H)=8!-2\cdot7!=30240\). Indeed, the chromatic polynomials for the two missing-edge configurations are respectively \((t)_8+2(t)_7+(t)_6\) and \((t)_8+2(t)_7\), and the number of acyclic orientations is \((-1)^8\chi_H(-1)\). Deleting further edges cannot increase this number. Thus any paired-flat \(Q_{16}\) coloring with at least two missing undirected pair interactions falls below the forcing-rank threshold for every half-sweep family.


**Corollary (nonlinear strong-feedback systems can have low half-sweep rank).** Let \(m=2k\), \(k\ge3\), and let \(H=C_k\square K_2\) be the cubic prism graph. For every label \(i\) with neighbors \(a,b,c\), prescribe
\[
f_i(p,q)=q_aq_b+q_aq_c+q_bq_c .
\tag{AO4}
\]
Each gate is a quadratic Boolean function of its three neighbors, ignores its own pair bits, and is antipodally odd because three-variable majority complements under \(q\mapsto q+\mathbf1\). Every neighboring influence is essential, so the directed dependency graph contains both orientations of each edge of \(H\), is strongly connected, and has directed feedback vertex number equal to the vertex-cover number \(\tau(H)\). Every edge is a directed two-cycle, so a feedback set meets every edge; conversely a vertex cover leaves an independent set and hence an acyclic residual. Since \(H\) has \(3m/2\) edges and maximum degree three, \(\tau(H)\ge m/2\).

Nevertheless \(|E(H)|=3m/2\le2m-2\), so (AO1) bounds the span of **every** half-sweep family below the rank-forcing threshold (AR2). Thus even full nonlinear dependence at every gate, strong connectivity, and linear directed feedback number together do not produce the rank hypothesis required by (AR2). The colorings are legal instances; no NORI1 counterexample is claimed.

An independent verifier enumerates the gates, influence relations, vertex covers and acyclic orientations for \(m=6,8,10\). The triples \((m,\tau(H),a(H))\) are \((6,4,204)\), \((8,4,1862)\), \((10,6,14700)\), while the rank thresholds are \(1953,32385,522753\), respectively. The all-dimensional argument follows from the preceding proof. The verifier is \`nori_cubic_rank_barrier_verify.py\`, with the full record in \`note_nori_permutation_sweep_acyclic_orientation_rank_barrier_r11755\`.

**Remaining task.** A rank-based unrestricted proof must simultaneously establish sufficiently many interaction-order classes and a lower bound on the linear independence of their endpoint maps, or supply a different forcing theorem when (AO1) makes the rank certificate unavailable. The theorem applies to arbitrary nonlinear gates, with no affine slope assumption. Its proof and calculations are retained in note \`note_nori_permutation_sweep_acyclic_orientation_rank_barrier_r11755\`.


### Complete complementary-halfword expansion beyond balanced midpoint orders

A red full antipodal geodesic need not traverse every pair once before the midpoint. The preceding rank criterion therefore tests only one class of witness. The following decomposition captures all red full antipodal geodesics without any gate restrictions.

For any pair word \(\alpha=(i_1,\ldots,i_m)\) of length \(m\), let \(n_i(\alpha)\) be the occurrence count of label \(i\), and let \(F_\alpha^p\) be the fiber permutation induced by the successive red matchings. Let \(\alpha\sim\beta\) denote *complementary multiplicity*, meaning \(n_i(\alpha)+n_i(\beta)=2\) for every pair \(i\). Then \(\alpha,\beta\) have the same parity of label occurrences and their red halfwalks terminate in the same pair-parity fiber.

**Theorem (all-full-path midpoint identity).** The number \(Z(c)\) of rooted red full antipodal geodesics equals
\[
\boxed{Z(c)=
\sum_{p\in\mathbb F_2^m}
\ \sum_{\substack{|\alpha|=|\beta|=m\\ \alpha\sim\beta}}
\operatorname{tr}\bigl((P_\alpha^p)^{\mathsf T}P_\beta^pJ\bigr).}
\tag{AR5}
\]
Every summand is a nonnegative integer. Hence red full antipodal geodesics are absent precisely when *every compatible halfword pairing* has zero antipodal-root midpoint incidence.

*Proof.* A midpoint collision from antipodal roots joins two red halfwalks of length \(m\). Their concatenation uses each pair twice by \(\alpha\sim\beta\). The endpoints are antipodal, so the two selected original dimensions of each pair must be different, establishing a full antipodal geodesic. Conversely, split any rooted red full antipodal geodesic after \(m\) edges, let \(\alpha\) be the first-half pair word, and \(\beta\) the reverse of the second-half pair word. They are complementary, and their red halfwalks from the two antipodal roots meet at the split vertex. The constructions are inverse. \(\square\)

**Corollary (cross-type rank forcing).** Choose nonempty classes \(A,B\) of length-\(m\) halfwords such that every \(\alpha\in A\) is multiplicity-complementary to every \(\beta\in B\). In one fixed starting parity fiber, let \(U_A\) and \(U_B\) be the respective real spans of differences of their red endpoint permutation matrices from a fixed representative of the same class. If no red full antipodal geodesic exists, then
\[
\boxed{\dim U_A+\dim U_B\le(N-1)^2.}
\tag{AR6}
\]
*Proof.* As in (AR2), center every permutation matrix by subtracting the uniform doubly stochastic matrix. Zero cross midpoint incidence gives bilinear pairing \(-1\) for every centered cross pair. Subtracting the two fixed representatives makes the difference subspaces orthogonal under the nondegenerate pairing \(B\) on doubly centered matrices, of dimension \((N-1)^2\). \(\square\)

The same result certifies square-switch survival when both selected halfword families never visit the switched exterior parity at any occurrence of the switched pair. In particular, (AR5) avoids assuming that every red full geodesic has a one-visit-per-pair midpoint split.

An independent direct enumeration checks (AR5) against all red pair words and original starting vertices for legal nonlinear colorings in \(Q_6\) and \(Q_8\). In one \(Q_8\) instance the full count is \(16{,}724\), of which only \(8{,}606\) arise from halfwords using every pair once. The exhaustive checker is nori_complete_midpoint_verifier.py. No conclusion that the cross-type rank bounds are universally exceeded is claimed.


### Unavoidable square-safe exchange curvature in every nonlinear paired-flat coloring

Let \(m\ge3\). In a legal paired-flat coloring of \(Q_{2m}\), label direction pairs by \([m]\), write \(p_i=x_{a_i}+x_{b_i}\) and \(q_i=x_{a_i}\), and put
\[
T_i(p,q)=(p+e_i,\ q+e_i(1+f_i(p,q))),
\]
where \(f_i\) ignores its own pair and satisfies \(f_i(p,q+\mathbf1)=1+f_i(p,q)\). Each \(T_i\) is an involutive bijection. For an order \(\pi\in S_m\), write \(F_\pi^p(q)\) for the within-fiber endpoint of the red half-sweep executing \(T_{\pi_1},\ldots,T_{\pi_m}\) from \((p,q)\).

Fix a pair label \(i\) and an exterior parity signature \(\sigma\in\mathbb F_2^{[m]\setminus\{i\}}\). These are the outside pair parities of an antipodal pair of alternating squares in the original directions \(a_i,b_i\). For a starting fiber \(p\), put \(D=\{j\ne i:p_j\ne\sigma_j\}\). An order \(\pi\) is *safe* when the labels preceding \(i\) form a set different from \(D\). Every red half-sweep with a safe order avoids the switched squares, regardless of its starting within-fiber bits \(q\). Let \(\mathcal H_i(p,\sigma)\) denote the safe orders.

**Lemma 1 (connected safe order graph).** If \(D\ne\varnothing\), then \(\mathcal H_i(p,\sigma)\), with edges given by adjacent exchanges of two labels, is connected; moreover every label \(j\in[m]\) begins some order in \(\mathcal H_i(p,\sigma)\).

*Proof.* For the first-label property, label \(i\) may come first because \(D\ne\varnothing\). For \(j\ne i\), choose a third label \(k\ne i,j\). There are orders beginning \(j,i\) with predecessor set \(\{j\}\), and orders beginning \(j,k,i\) with predecessor set \(\{j,k\}\). At most one of those sets equals \(D\); hence one order is safe.

For connectivity, fix a safe permutation and let \(B\ne D\) be the set preceding \(i\). If \(D\not\subseteq B\), repeatedly exchange \(i\) leftward with the immediately preceding label. Every intermediate predecessor set is a subset of \(B\), and therefore differs from \(D\). If \(D\subsetneq B\), rearrange the labels of \(B\) using swaps not involving \(i\) until some label \(j\in D\) immediately precedes \(i\). Exchange \(i\) with \(j\). The new predecessor set \(B\setminus\{j\}\) omits \(j\in D\), so the preceding case applies and \(i\) can move left to the first position. Finally, all orders beginning with \(i\) are connected by adjacent swaps among the remaining labels, and are safe. \(\square\)

**Theorem 2 (pointwise antipodal square-safe curvature).** Fix any legal paired-flat coloring, any \(i,\sigma\), and any initial parity \(p\) with \(p_{-i}\ne\sigma\). Define
\[
\mathcal C_p=
\{q\in\mathbb F_2^m:\exists\pi,\pi'\in\mathcal H_i(p,\sigma)
\text{ differing by one adjacent exchange, }
F_\pi^p(q)\ne F_{\pi'}^p(q)\}.
\]
Then
\[
\boxed{\mathcal C_p\cup(\mathcal C_p+\mathbf1)=\mathbb F_2^m,
\qquad |\mathcal C_p|\ge2^{m-1}.}\tag{SC1}
\]
For every \(q\in\mathcal C_p\), the differing half-sweep endpoints arise from a noncommuting pair of red matchings \(T_j,T_k\) reached after a red prefix; the two red half-sweeps and their exchanged pair steps avoid the designated switched squares. All assertions allow arbitrary nonlinear truth tables.

*Proof.* Suppose some antipodal source pair \(q,q+\mathbf1\) lies outside \(\mathcal C_p\). By Lemma 1, the safe order graph is connected, and the maps \(\pi\mapsto F_\pi^p(q)\) and \(\pi\mapsto F_\pi^p(q+\mathbf1)\) are constant on it; write their endpoints as \(z,z'\).

For each label \(j\), choose by Lemma 1 a safe order beginning with \(j\). Its first red pair step changes bit \(q_j\) to
\[
q_j+1+f_j(p,q),
\]
and none of the later pair steps changes that bit. Starting instead from \(q+\mathbf1\) gives the same \(j\)-th endpoint bit, since
\[
(q_j+1)+1+f_j(p,q+\mathbf1)
=q_j+1+f_j(p,q).
\]
Hence \(z_j=z'_j\) for every \(j\), and therefore \(z=z'\). But each red half-sweep is a composition of bijections, so it cannot send the distinct inputs \(q,q+\mathbf1\) to the same output. This contradiction proves the first assertion, and the cardinality bound follows by pairing the \(2^m\) inputs antipodally.

If two safe orders differ by exchanging adjacent \(j,k\), their common red prefix and suffix induce bijections, and different final endpoints imply the intermediate red paths \(T_jT_k\) and \(T_kT_j\) have different endpoints at the same intermediate vertex. Their difference is a nontrivial square commutator in the pair-parity quotient. Both complete orders are safe, so their red steps avoid the switched support. \(\square\)

**Corollary 3 (simultaneous good/bad curvature).** Let two legal paired-flat colorings differ by one antipodally paired alternating-square switch in pair \(i\) with exterior signature \(\sigma\). For each \(p\) with \(p_{-i}\ne\sigma\), their safe half-sweep endpoint maps are identical for every order in \(\mathcal H_i(p,\sigma)\). Thus they share the set \(\mathcal C_p\), and that set has at least \(2^{m-1}\) within-fiber sources. The conclusion applies, in particular, at any hypothetical balanced good-to-bad critical boundary.

*Proof.* A safe half-sweep uses pair \(i\) at outside pair-parity different from \(\sigma\), so it meets no changed edge. Its entire red trajectory and endpoint are identical in both colorings. Apply Theorem 2. \(\square\)

**Scope and forcing obligation.** The theorem produces nontrivial adjacent-exchange holonomy outside a prescribed critical square for at least half the sources in each of \(2^m-2\) starting pair-parity fibers. It does not itself produce an antipodal midpoint collision or a full monochromatic geodesic. A closure argument would have to couple these unavoidable safe exchanges with the strict one-internal-hit full-geodesic witnesses in the *same* hypothetical critical coloring. The rank bounds for square-safe permutation matrices previously recorded in this Subsection give a complementary obstruction; (SC1) supplies a nonzero, rootwise curvature source without affine assumptions.

**Finite verification.** An independent bit-level checker enumerates safe orders and red half-sweep endpoints for random legal nonlinear gate tables in \(Q_6\) and \(Q_8\), and checks the pointwise antipodal covering law. A separate enumerator verifies connectivity of the safe adjacent-transposition graph for every switched pair and exterior signature for \(3\le m\le6\). The proof above is dimension-uniform.


### Why first-label symmetry and square-safe curvature alone do not force midpoint collisions

The preceding curvature theorem uses first-label output constraints and bijectivity; its proof does not yet use the full prefix-causal consistency of the matchings \(T_i\). The following abstract permutation model separates those hypotheses.

**Proposition (parity-preserving abstract endpoint obstruction).** On \(V=\mathbb F_2^3\), define invertible linear maps \(L_0,L_1\) by
\[
L_0(q_0,q_1,q_2)=(q_0+q_1,q_1,q_1+q_2),\quad
L_1(q_0,q_1,q_2)=(q_0,q_0+q_1,q_0+q_2).
\]
For each \(\pi\in S_3\), put \(G_\pi=L_1\) if \(\pi_1=1\), and \(G_\pi=L_0\) otherwise. Then

1. Every \(G_\pi\) is a bijection, and its first-label output bit \(G_\pi(q)_{\pi_1}\) is invariant under \(q\mapsto q+\mathbf1\). This is the pointwise antipodal identity supplied by the first red matching of a legal paired-flat coloring.
2. For any connected subfamily of orders containing an order beginning with every label, at least one member of each antipodal source pair \(q,q+\mathbf1\) has an endpoint depending on the order. Thus the first-label covering proof of Theorem 2 applies to this abstract family.
3. Nevertheless
\[
G_\pi(q)\ne G_\rho(q+\mathbf1)
\]
for *every* \(q,\pi,\rho\): the family has no complementary-root midpoint collisions.

*Proof.* Both matrices are invertible, since \(L_0\) reconstructs \(q_1\), then \(q_0,q_2\), and \(L_1\) reconstructs \(q_0\), then \(q_1,q_2\). The first-label output bit is \(q_0+q_1\) for labels \(0,1\), and \(q_1+q_2\) for label \(2\); these expressions have even parity in the input bits and hence are invariant under complementing all three input bits. The argument proving the pointwise square-safe curvature theorem uses only this first-label identity, bijectivity, and connectivity, so it proves (2). Finally, each \(L_i\) preserves input bit parity:
\[
\sum_{j=0}^{2}(L_iq)_j=\sum_{j=0}^{2}q_j\pmod2.
\]
In odd dimension, \(q\) and \(q+\mathbf1\) have opposite parity. Thus their images under any \(G_\pi,G_\rho\) cannot coincide. \(\square\)

This is an *abstract permutation-family counterexample*, not a legal paired-flat coloring. It shows that the first-label antipodal law, square-safe connectedness, and even pointwise endpoint variation are insufficient by themselves to force a midpoint collision. A closing argument must use further compatibility that the actual red half-sweep permutations satisfy.

That compatibility is explicit. For an adjacent exchange of two pair labels \(j,k\) after a common prefix \(\alpha\) and before a common suffix \(\beta\), the endpoint difference factors through
\[
T_\beta\,T_kT_j\,T_\alpha\quad\text{versus}\quad
T_\beta\,T_jT_k\,T_\alpha.
\]
After cancelling the bijective common prefix and suffix, the discrepancy is a square commutator of two matchings, affecting only the two within-fiber bits \(q_j,q_k\) at the intermediate state. On each fixed assignment of other bits, the two relevant gates are affine in their single active outside bit; thus this commutator is a permutation of the four local states arising from two affine Boolean shears. An abstract first-label permutation system need not admit any such common-gate factorization.

The precise outstanding implication is therefore a *prefix-causal holonomy-to-collision principle*: show that the common nonlinear gate data and the resulting two-bit local commutators prevent all complementary halfword midpoint incidences from vanishing. The first-label curvature theorem supplies mandatory commutators even outside any selected critical square, but the parity-preserving model proves that this alone cannot complete the argument.


### Complete-dependency nonlinear colorings with unavoidable safe curvature but no safe midpoint collision

For every \(m\ge3\) there is a *successful* legal paired-flat coloring of \(Q_{2m}\) with a complete directed gate-dependency graph, whose square-safe red half-sweeps in one parity fiber have no antipodal-root midpoint collision, despite having nontrivial safe adjacent-exchange curvature on three quarters of the within-fiber roots. For \(m\ge4\), every gate can be chosen nonlinear in the within-pair \(q\)-variables. This refutes the transfer from the preceding square-safe curvature theorem to square-safe collisions even for shared nonlinear gates with dense dependencies.

**Construction.** Use \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\), and red matching steps \(T_i(p,q)=(p+e_i,q+e_i(1+f_i(p,q)))\). Let \(s(0)=1\), \(s(i)=0\) for \(i>0\). Define an outside-parity row \(\alpha_i\) by \((\alpha_i)_j=1\) for every \(j>0,j\ne i\), and \((\alpha_i)_0=0\) for \(i>0\). Write \(\delta_i(p)=\mathbf1_{\{p_{-i}=\alpha_i\}}\). Choose a Boolean function \(h_i(q_{-i})\) satisfying \(h_i(0)=1\) and \(h_i(q+\mathbf1)=h_i(q)\). One may take \(h_i=1\) when \(m=3\); when \(m\ge4\), choose three distinct outside labels \(a,b,c\) and take \(h_i=1+(q_a+q_b)(q_a+q_c)\). Put
\[
f_i(p,q)=q_{s(i)}+\delta_i(p)h_i(q).
\tag{DH1}
\]

The gates ignore their own pair. The first term changes by one under \(q\mapsto q+\mathbf1\), and the second is invariant, so the coloring is legal and antipodally odd. Toggling any other parity bit \(p_j\) at \(p_{-i}=\alpha_i,q=0\) changes \(f_i\), because \(h_i(0)=1\). Thus every directed dependency \(j\to i\), \(i\ne j\), is present. For \(m\ge4\), the displayed \(h_i\) has nonzero quadratic degree in \(q\), proving within-fiber nonlinearity.

**A red full antipodal geodesic.** Start at \(p=(1,1,0,\ldots,0)\), \(q=(0,1,0,\ldots,0)\) and use pair word \(w=(0,1,\ldots,m-1,0,1,\ldots,m-1)\). None of the \(2m\) pair steps visits a row \(\alpha_i\): on the first sweep, gate \(0\) sees \(p_1=1\) and \(p_j=0\) for \(j\ge2\); gate \(1\) sees all later parities zero; every gate \(i\ge2\) sees \(p_1=0\). On the second sweep, gate \(0\) sees \(p_1=0\), and all other gates see \(p_0=1\). Hence the full word uses only the simpler reader gates \(g_0=q_1\), \(g_i=q_0\) for \(i>0\). The first \(0\)-step leaves \(q_0=0\), the first passage through every positive label flips that label's \(q\)-bit, the second \(0\)-step flips \(q_0\) to one, and the second passage through the positive labels leaves their bits fixed. Every \(q_i\) has therefore changed once, so the full red path ends at the antipode and traverses every original direction once.

**Safe half-sweeps.** Now fix starting parity \(p=0\), switched label \(0\), and a switched square pair whose outside parity is all ones. A half-sweep order \(\pi\) avoids this square set independently of \(q\) whenever \(0\) is not its last label. These are precisely the safe orders. None reads an exceptional parity row: gate \(0\) would need to be last to read \(\alpha_0\); another gate \(i>0\) would need every other positive label before it and label \(0\) afterward, again forcing \(0\) last. Thus every safe half-sweep uses the reader gates \(g_i\).

Write \(r=q_0,s=q_1\). For a safe order of type \(A\), in which label \(1\) precedes \(0\), the endpoint bits \(0,1\) are \((s,s+r+1)\). For type \(B\), in which label \(1\) follows \(0\), they are \((r+s+1,r)\). Starting from \(q+\mathbf1\), the corresponding output pairs are \((s+1,s+r+1)\) and \((r+s+1,r+1)\). Equal-type outputs from complementary roots cannot coincide. A cross-type output \(A(q)=B(q+\mathbf1)\) in the first two bits requires \((r,s)=(1,0)\). In this case a label \(j\ge2\) that follows \(0\) in the \(A\)-order has output \(q_j+1\), whereas its output in the \(B\)-order from \(q+\mathbf1\) is \(q_j\), irrespective of the latter order. Equality would force every \(j\ge2\), as well as label \(1\), to precede \(0\) in the \(A\)-order, contradicting safety. In the other cross-type case \(B(q)=A(q+\mathbf1)\), the first-two-bit condition requires \((r,s)=(0,1)\), and equality on the remaining bits would force every \(j\ge2\) to precede \(0\) in the \(A\)-order from \(q+\mathbf1\), the same contradiction. Therefore
\[
\boxed{F_\pi^{\,0}(q)\ne F_\rho^{\,0}(q+\mathbf1)
\quad\text{for every }q\text{ and every two safe orders }\pi,\rho.}
\tag{DH2}
\]

Both types of safe order exist for \(m\ge3\). Their first-two-bit outputs differ whenever \((r,s)\ne(1,1)\). When \((r,s)=(1,1)\), both types give identical first two bits and every other output bit equals its input bit, independently of the order. Thus precisely \(3\cdot2^{m-2}\) sources have order-dependent safe endpoints. Connectivity of the safe adjacent-exchange graph produces a nontrivial safe square commutator for every such source.

**Consequence.** A *single legal, successful*, dense-dependency, nonlinear paired-flat coloring can possess strong safe exchange curvature and still lack *every* safe one-per-pair midpoint collision in a chosen starting parity fiber. This is a dimension-uniform obstruction to the inference that shared-gate causality plus local safe holonomy forces a safe midpoint witness. It does not refute NORI1 or the possibility of a collision using unsafe orders, other parity fibers, or complementary-multiplicity halfwords.

The mechanism is a general visibility principle: any gate truth-table row at an exterior parity never encountered by the selected pair words may be changed by an antipodally even perturbation without changing those words' red endpoints. The exceptional rows \(\alpha_i\) make every dependency essential and allow nonlinear gates without affecting the safe half-sweep data. Syntactic dependency density consequently cannot replace a theorem controlling the parity rows actually traversed by the witnesses. Exhaustive finite verification for \(3\le m\le6\) accompanies the symbolic proof in nori_dense_safe_holonomy_verifier.py.


### Tensor obstruction for midpoint rank amplification

Let \(P_\pi(c,p)\) denote complete red half-sweep permutations on the \(N=2^m\) fiber states of a paired-flat coloring \(c\), starting at parity \(p\). Set \(r(c,p)=\dim_{\mathbb R}\operatorname{span}\{P_\pi\}\), \(d(c,p)=r(c,p)-1\), and \(K(c,p)=\frac1{m!}\sum_\pi P_\pi\).

**Theorem.** For any independent paired-flat factors \(c,h\),
\[
r(c\boxtimes h,(p,q))=r(c,p)r(h,q),\qquad
K(c\boxtimes h,(p,q))=K(c,p)\otimes K(h,q).
\tag{TN1}
\]
*Proof.* Pair updates in distinct factors commute, so a combined sweep has endpoint matrix \(P_{\pi_c}(c,p)\otimes P_{\pi_h}(h,q)\). Every factor-order pair arises, and each arises in the same number \(\binom{m+k}{m}\) of interleavings. This proves both identities. The difference span has dimension \(d=r-1\), because all permutation matrices have the same sum of entries. \(\square\)

Put \(T(N)=(N-1)(N-2)/2\). If \(d(c,p)\le T(N)\), then \(d(c\boxtimes h,(p,q))\le T(NM)\) for every independent factor \(h\) with \(M=2^k\) fiber states. Indeed \(r(h,q)\le(M-1)^2+1\), and
\[
T(NM)+1-(T(N)+1)((M-1)^2+1)
=\tfrac12(M-1)(2N^2+3NM-6N-4M+4)>0.
\tag{TN2}
\]
Moreover, \(\|K(c\boxtimes h)\|_F^2=\|K(c)\|_F^2\|K(h)\|_F^2\), with \(\|K(h)\|_F^2\ge1\). Hence independent padding cannot turn a failed rank-forcing or Frobenius-mixing certificate into a successful one.


**Multigraded halfword theorem.** For \(a\in\{0,1,2\}^m\), let \(V_a(c,p)\) be the span of red endpoint permutation matrices for pair words in which label \(i\) occurs \(a_i\) times. For all count vectors \(a,b\) and independent paired-flat factors \(c,h\),
\[
\boxed{V_{(a,b)}(c\boxtimes h,(p,q))
=V_a(c,p)\otimes V_b(h,q).}
\tag{TN3}
\]
*Proof.* Every word with count vector \((a,b)\) restricts to words of count vectors \(a,b\), and its factor updates commute. Conversely every pair of factor words admits a shuffle producing the prescribed full count vector. Thus the endpoint matrices and their spans are the stated tensor products. \(\square\)

For a fixed total length \(L\) and pair-count parity signature \(\sigma\), the endpoint span is a *sum* of the \(V_a\) with \(\sum_i a_i=L\), \(a\bmod2=\sigma\). It can have larger dimension than the read-once sweep span. In the Cartesian product of two paired-flat \(Q_4\) blocks with gates \(f_0=t_1,f_1=t_0,f_2=t_3,f_3=t_2\), the read-once \(Q_8\) half-sweep span has dimension four, whereas the length-four halfwords with all pair-label multiplicities even have span dimension five. The independent checker nori_halfword_graded_tensor_verify.py confirms (TN3) for all four-step count vectors in this product, and verifies the ranks.

The complete midpoint identity pairs halfwords with count vector \(a\) only against halfwords with vector \(2-a\). Consequently the extra span of a coarser parity sector cannot be inserted directly into the complementary-halfword rank criterion. A closure mechanism requires relations *between distinct count-vector sectors*, arising from shared nonlinear gates or admissible exchanges between paths. These tensor identities show why independent padding of read-once orders cannot supply those relations.


### Faithful global sweep tomography and sharp square-safe information kernel

Let \(m\ge2\), \(p_i=x_{a_i}+x_{b_i}\), \(q_i=x_{a_i}\). For an arbitrary legal paired-flat coloring let
\[
T_i(p,q)=(p+e_i,q+e_i(1+f_i(p_{-i},q_{-i}))),\qquad
f_i(u,v+\mathbf1)=1+f_i(u,v).
\]
Fix an order \(\pi=(i_1,\ldots,i_m)\) and let \(H_\pi=T_{i_m}\cdots T_{i_1}\). Its terminal within-fiber function is \(F_\pi^p(q)\), while its terminal parity is \(p+\mathbf1\).

**Theorem 1 (one-order global reconstruction).** Knowledge of \(H_\pi\) for every starting vertex \((p,q)\) uniquely determines every gate \(f_i\), with no affine or bounded-dependency condition.

*Proof.* The first terminal bit \(i_1\) is its value just after the first pair step. Hence \(f_{i_1}=1+q_{i_1}+(F_\pi^p(q))_{i_1}\), recovering the first gate globally. If the first \(k-1\) gates are known, their prefix bijectively transports all starting vertices to all intermediate vertices. At each intermediate vertex \(z=(p^{(k)},q^{(k)})\), the next gate satisfies \(f_{i_k}(z)=1+q^{(k)}_{i_k}+(F_\pi^p(q))_{i_k}\), because later steps never change that bit. By varying the source one recovers its entire truth table. Continue inductively. \(\square\)

**Theorem 2 (maximal square-safe one-order reconstruction).** Fix a pair \(i\) and an exterior pair-parity signature \(\sigma\in\mathbb F_2^{[m]\setminus\{i\}}\). Fix any order \(\pi\) beginning with \(i\). Suppose \(F_\pi^p(q)\) is known for every within-fiber source \(q\) and every starting parity \(p\) with \(p_{-i}\ne\sigma\). These observations determine *every gate value* except those of \(f_i\) on the exterior parity row \(p_{-i}=\sigma\). Conversely, arbitrary legal changes on that single row leave all these endpoint observations unchanged.

*Proof.* The first step uses gate \(i\) at initial exterior parity \(p_{-i}\). By the first-bit formula its entire table is recovered outside \(\sigma\). Process the remaining labels in order. To recover the gate of label \(j\ne i\) at an arbitrary prescribed intermediate outside parity \(u\), choose the initial bit \(p_j=1+\sigma_j\). Since \(j\) has not yet been updated, its own bit is absent from its exterior parity \(u\); the other initial parity bits may therefore be chosen to realize \(u\). But the choice of \(p_j\) ensures \(p_{-i}\ne\sigma\), so the initial \(i\)-step is safe. The known prefix is bijective on the within-fiber variables \(q\), and thus every intermediate \(q\) occurs. Its terminal \(q_j\) bit recovers the whole \(u\)-row of gate \(j\). Induct on the position of \(j\). Conversely, an \(i\)-first sweep started with \(p_{-i}\ne\sigma\) never evaluates the changed row of \(f_i\), and every other gate is identical, proving invariance of the observed endpoints. \(\square\)

**Corollary 3 (sharp hidden Boolean hypercube).** The legal colorings consistent with the safe observations of Theorem 2 form a Boolean hypercube of dimension \(2^{m-2}\), hence number \(2^{2^{m-2}}\). The free bits are the values of \(f_i(\sigma,q_{-i})\) on one representative of each complementary pair \(\{q_{-i},q_{-i}+\mathbf1\}\). Toggling one free bit is precisely an antipodally paired alternating-square switch with exterior parity \(\sigma\). All other nonlinear gate values and dependencies are identified by the single safe order.

**Theorem 4 (minimum eight-root distance).** For any fixed order \(\pi\) and any two distinct legal paired-flat colorings \(c,d\), their global endpoint maps \(H_\pi^c,H_\pi^d\) disagree at at least eight starting vertices. Every elementary legal antipodally paired alternating-square switch changes the endpoint map on precisely eight starting vertices.

*Proof.* Let \(j\) be the first gate along \(\pi\) where the two colorings differ. All earlier gates agree, so the common prefix bijectively maps starting vertices onto all intermediate states. Choose an outside state \((p_{-j},q_{-j})\) where their \(j\)-gates differ. The gate difference is invariant under complementing the outside \(q\)-bits, so it also differs at \((p_{-j},q_{-j}+\mathbf1)\). Since the gates ignore their own \(p_j,q_j\), each outside state admits four independent own-pair choices. These eight states have distinct starting preimages. Their terminal \(q_j\) output bits differ because no later gate changes coordinate \(j\). This proves the bound. For a single square switch, exactly eight intermediate states undergo a changed red matching, and the common prefix and suffix are bijective, so the resulting endpoint maps differ on precisely eight starting vertices. \(\square\)

### Optimal fixed-parity tomography as a Boolean-lattice chain-cover theorem

Fix just one initial pair parity \(p\), while observing terminal endpoints from every initial \(q\) for selected pair orders. Each pair order visits gate \(i\) at the exterior parity \(p_{-i}\) toggled on the set \(S\) of labels preceding \(i\). This observation corresponds to the oriented Boolean-lattice edge \(S\to S\cup\{i\}\). A collection of orders determines every gate table precisely when its maximal chains cover every such directed edge: sufficiency follows by recovering rows in increasing cardinality of \(S\) with the known prefix gates; necessity follows by toggling an unobserved antipodally odd row, which changes no observed sweep endpoint.

**Theorem 5 (optimal fixed-parity portfolio).** The minimum number of half-sweep orders whose complete terminal maps from a single starting parity fiber identify an arbitrary legal paired-flat coloring is
\[
\boxed{M(m)=\max_{0\le k<m}(m-k)\binom mk
=m\binom{m-1}{\lfloor(m-1)/2\rfloor}.}
\]

*Proof.* There are \(E_k=(m-k)\binom mk=m\binom{m-1}{k}\) directed Boolean-lattice edges from rank \(k\) to \(k+1\). Every maximal chain covers one such edge, giving the lower bound \(M=\max_kE_k\). For the upper bound, put fractional flow \(M/E_k\ge1\) on each rank-\(k\) edge. At a rank-\(k\) vertex incoming and outgoing flows equal \(M/\binom mk\); the source and sink carry total flow \(M\). Therefore the directed network has a feasible flow of value \(M\) subject to integer lower bound one on every edge. Total unimodularity of the directed incidence matrix yields an integral feasible flow of the same value, with each edge carrying at least one unit. Decompose this acyclic integral flow into \(M\) maximal source-to-sink chains. They cover every lattice edge, giving a portfolio of \(M\) pair orders and completing the proof. \(\square\)

The values begin \(M(2)=2\), \(M(3)=6\), \(M(4)=12\), \(M(5)=30\), \(M(6)=60\), \(M(7)=140\), \(M(8)=280\). Constructive verifiers are nori_sweep_tomography_flow.py, nori_square_safe_tomography.py, and nori_sweep_code_distance.py.

**NORI1 scope.** These reconstruction and metric theorems apply to arbitrary legal nonlinear paired-flat gates and supply a full-class mechanism rather than another finite gate classification. A single globally observed sweep encodes every gate; one globally observed safe sweep encodes everything outside the unique switched exterior-parity row. A critical paired-square boundary changes one free bit in the invisible Boolean hypercube and changes the complete sweep permutation on the minimum eight-root support. This identifies the missing bridge as a relation between safe transport and paths visiting that exceptional row. It does not itself prove a monochromatic antipodal full geodesic or settle the distinct boundary-tournament problem.


### Quadratic dependence of unrestricted red full-geodesic counts on one complete pair gate

Fix \(m\ge2\) and a legal paired-flat coloring on \(Q_{2m}\). Fix every gate \(f_j\), \(j\ne i\), and allow the entire nonlinear gate \(f_i\) to vary subject to own-pair independence and the antipodal oddness law. Index its independent Boolean truth-table values by \(t=(u,[v])\), where \(u\in\mathbb F_2^{m-1}\) is outside pair parity and \([v]=\{v,v+\mathbf1\}\) is a complementary orbit of outside first-member bits. There are \(B=2^{m-1}2^{m-2}=2^{2m-3}\) independent gate bits \(h_t\).

For a fixed geometric rooted full antipodal geodesic \(P\), meaning a root together with a permutation of all \(2m\) original direction indices, let \(I_P(h)\) be one if every edge of \(P\) is red and zero otherwise. Set
\[
Z(h)=\sum_P I_P(h),
\]
the number of rooted red full antipodal geodesics.

**Theorem 6 (full-gate quadratic witness law).** For arbitrary fixed values of all other gates,
\[
\boxed{\deg Z(h)\le2}
\tag{QR1}
\]
when \(Z\) is represented as the unique multilinear real polynomial in the \(B\) independent Boolean bits \(h_t\). More precisely, \(Z\) is a nonnegative sum of products of at most two literals \(h_t\) or \(1-h_t\). Therefore every third mixed Boolean derivative in distinct gate bits vanishes identically.

*Proof.* A geometric full antipodal geodesic uses each original direction once, so it traverses only two edges of pair \(i\): one in direction \(a_i\) and the other in direction \(b_i\). Every other path-edge color is fixed. If any such fixed color is blue, \(I_P(h)\) vanishes. Otherwise the two pair-\(i\) red conditions prescribe at most two independent gate-table literals: the first must choose its prescribed original pair member, and the second must choose its other prescribed member. The oddness relation on the complementary \(q\)-arguments translates each condition into \(h_t=0\) or \(h_t=1\). Repeated compatible literals reduce to one; incompatible literals make the indicator zero. Consequently every nonzero \(I_P(h)\) is a product of at most two literals. Summation proves (QR1). \(\square\)

**Corollary 7 (pairwise switch inclusion-exclusion).** Fix a baseline legal coloring \(c\), and select arbitrary distinct legal antipodally paired alternating-square switches \(S_1,\ldots,S_t\), all supported in the *same direction pair* \(i\), with arbitrary exterior parity and outside-bit locations. For \(A\subseteq[t]\), let \(c^A\) be the coloring obtained by applying switches with indices in \(A\); the switches commute as truth-table bit flips. Then
\[
\boxed{Z(c^A)=Z(c)+
\sum_{a\in A}\bigl[Z(c^{\{a\}})-Z(c)\bigr]
+\sum_{\{a,b\}\subseteq A}
\bigl[Z(c^{\{a,b\}})-Z(c^{\{a\}})-Z(c^{\{b\}})+Z(c)\bigr].}
\tag{QR2}
\]
Thus the total red full-geodesic count across *all* combinations of same-pair switches is determined by its values at the baseline, all single switches, and all pairs of switches. There is no independent third- or higher-order switch interaction in this count.

*Proof.* Apply Theorem 6 after parametrizing the selected independent gate bits by their flip indicators relative to \(c\). The resulting multilinear polynomial has degree at most two. Its constant, linear and quadratic coefficients are respectively the baseline value, first differences and mixed second differences displayed in (QR2). \(\square\)

**Corollary 8 (robustness under random full-gate replacement).** If \(c\) possesses a red full antipodal geodesic, at least one quarter of all legal replacements of the *entire* gate \(f_i\), with all other gates fixed, preserve a red full antipodal geodesic. Indeed, a chosen successful geometric red path constrains at most two independent bits of the replacement gate, and each remaining truth-table bit may be assigned arbitrarily. More generally, replacing simultaneously the entire gates of \(r\) prescribed direction pairs preserves some red full antipodal geodesic for at least a \(2^{-2r}\) fraction of all their legal replacements, witnessed by any one fixed successful path.

**Corollary 9 (2-CNF obstruction on the full nonlinear gate cube).** For fixed other gates, the assignments of gate \(i\) with *no* red full antipodal geodesic form the solution set of a Boolean 2-CNF formula: for every geometric full path whose fixed-gate edges are all red, forbid the conjunction of its at most two required \(f_i\)-literals. The empty conjunction contributes an impossible clause, a single literal contributes a unit clause, and two literals contribute a binary clause. The formula may have arbitrarily many clauses; this is a full-class reduction with \(2^{2m-3}\) Boolean variables, not a bounded certificate or a proof that the formula is inconsistent.

The polynomial and 2-CNF formulations give a dimension-uniform compatibility calculus for varying arbitrary nonlinear truth tables of a pair gate. They complement the earlier two-direction seam clauses in Article XVI, but do not supply the missing universal unsatisfiability theorem. The lower bound in Corollary 8 concerns the survival of a *specified* successful path under random gate replacements; it is not an assertion of deterministic survival under every replacement. The independent original-direction-path checker nori_one_gate_quadratic_verifier.py enumerates all relevant red-path terms in \(Q_6\), verifies every third mixed difference vanishes across all 256 assignments of a gate, and checks nonnegativity and degree.


### Complementary-halfword influence and the critical-square curvature barrier

Complete-halfword midpoint collisions require odd finite differences of the shared pair gates. A midpoint profile without singly used pairs requires two vertex-disjoint directed dependency cycles.

THEOREM A. Let w contain each pair label twice and v_k be its red matching trajectory. With visits r_i<s_i, reaching the antipode is equivalent to f_i(v_(r_i-1))+f_i(v_(s_i-1))=1 for all i. This equals the sum of finite differences f_i(v_(k-1))+f_i(v_k) over r_i<k<s_i. Every nonzero term involving a step in pair j supplies a dependency arc i->j. Proof: each pair parity returns to its start; its first-member fiber bit must flip once, meaning the two selected red directions in the pair differ. Gate i ignores its own pair, and its values telescope between the visits.

THEOREM B. Split the word after m steps. Define D as pairs occurring twice in first half, Z as pairs occurring zero times, and S as pairs occurring once. Then |D|=|Z|. Any successful full geodesic forces an outgoing dependency arc from every i in D into D union S, and from every i in Z into Z union S. If G[D] is acyclic, every vertex of D has a directed path to S; likewise for Z. Proof: the odd temporal derivative for each repeated pair contains a nonzero increment caused by a pair in its own half. A finite walk following these arcs either enters S or creates a directed cycle.

COROLLARY C. When S is empty and D is nonempty, the directed dependency graph contains a cycle inside D and another inside Z. These cycles are vertex disjoint. Thus if the graph has no pair of vertex-disjoint directed cycles, every complementary-halfword midpoint incidence with multiplicities only 0 or 2 vanishes: tr(P_alpha^T P_beta J)=0 for every alpha,beta with complementary all-even pair counts and every starting parity fiber. This is a shared-gate zero-incidence theorem, not a proof of unrestricted NORI1.
CRITICAL-SQUARE CURVATURE: If a legal paired-square switch turns a successful coloring into a bad one, every red full geodesic on the good side hits the switch once internally. The switched pair step cannot commute with either neighboring red step from another pair. Otherwise swapping that adjacent pair of red moves keeps the two-step endpoint and all original directions, but moves the unique switched edge outside the switched square orbit, producing a red full geodesic surviving the switch. For adjacent pair labels i,j, local red commutation holds precisely when both finite derivatives f_i(v)+f_i(T_j v) and f_j(v)+f_j(T_i v) vanish. This adds two necessary nonzero-curvature conditions to every strict one-hit witness, but does not force such a witness to be repairable.
