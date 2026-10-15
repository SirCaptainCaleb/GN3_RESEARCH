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

**Coupling to Article XIV.** A gate corridor forces neighboring face roots to be empty. If a critical one-edge repair produces paired witnesses at one of those roots, (EC2) locates a component that is itself empty there, and every unaffected factor must provide a common-color monochromatic path. The repair therefore resolves a local feedback obstruction at that prescribed root. Independent components with opposing one-sided orientations can supply an empty corridor, but cannot supply such a paired repair.

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
