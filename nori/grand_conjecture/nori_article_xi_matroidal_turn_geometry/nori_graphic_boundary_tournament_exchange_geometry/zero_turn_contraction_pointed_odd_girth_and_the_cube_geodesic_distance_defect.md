# Zero-turn contraction, pointed odd girth, and the cube geodesic distance defect

# Zero-turn contraction, pointed odd girth, and the cube geodesic distance defect

Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover, with induced connected turn cover over \(H=L(G)\). Let \(a\in C^1(H;\mathbb F_2)\) represent the covering-monodromy class. The pointed lift dual from Article XI is
\[
D=M\begin{pmatrix}B_H&0\\ a&1\end{pmatrix}^{*},
\tag{1}
\]
with distinguished port \(p\). Any deck-odd coloring gives \(d=a+\delta f\); its associated port-containing binary cycle is \(X_d=\operatorname{supp}(d)\cup\{p\}\).

The dependence on the coloring can be consolidated into a smaller **signed contraction graph**. This gives a full characterization of *unrestricted* port-cocircuit intersection and, in the cube, a metric distance defect whose vanishing is equivalent to NORI1.

## 1. Zero-turn contraction and pointed odd girth

Define \(H_0(d)=(V(H),\{e:d(e)=0\})\), with all original vertices and only zero-turn edges. Contract each connected component of \(H_0(d)\) to one vertex; retain all edges \(e\) with \(d(e)=1\), including parallel edges and loops. Denote the resulting multigraph by \(K_d\). A loop has odd-girth contribution one. Let \(\operatorname{og}(K_d)\) denote the minimum edge count of an odd cycle, with \(+\infty\) if none exists.

**Theorem 1 (zero-turn odd-girth normal form).** For any deck-odd coloring and its pointed cycle \(X_d\),
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\p\in Y}}
|X_d\cap Y|
=1+\operatorname{og}(K_d).
}
\tag{2}
\]
The contracted graph \(K_d\) is nonbipartite (where loops count as odd cycles), so its odd girth is finite. More precisely, the contraction of the *primal* pointed matroid (1) by all zero-turn elements is represented, after elementary row operations, by
\[
\boxed{
\widehat M/H_0(d)\cong
M\begin{pmatrix}B_{K_d}&0\\ \mathbf1&1\end{pmatrix},
}
\tag{3}
\]
where \(\widehat M=D^*\), \(B_{K_d}\) is the incidence matrix of the contracted multigraph, and \(\mathbf1\) assigns one to each retained graph edge. The dual statement is deletion of the zero-turn elements from \(D\).

*Proof.* Replace the bottom row \(a\) in (1) by \(d=a+\delta f\) using vertex-incidence row operations. The columns corresponding to \(d=0\) then have bottom entry zero; contracting them identifies precisely the vertices in each connected component of \(H_0(d)\). The remaining columns represent \(B_{K_d}\) with bottom entry one, and the port still has bottom entry one, proving (3).

By the pointed covering representation, a port-containing cocircuit of \(D\) has the form \(Y_C=C\cup\{p\}\) for a simple cycle \(C\subseteq H\) with monodromy one, and
\[
|X_d\cap Y_C|=1+w_d(C),\qquad
w_d(C)=\sum_{e\in C}d(e),
\tag{4}
\]
where \(w_d\) is an integer. Since \(d\) represents monodromy, \(w_d(C)\) is odd.

Under the component contraction, \(C\) becomes a closed walk in \(K_d\) having \(w_d(C)\) edges: all zero turns have been contracted. Every odd closed walk contains an odd simple cycle, possibly a loop. Consequently
\(\operatorname{og}(K_d)\le w_d(C)\).

Conversely, take a shortest odd cycle of \(K_d\), of length \(g=\operatorname{og}(K_d)\). For each pair of its consecutive retained edges meeting at a contracted vertex, join their original endpoints by a path of zero turns inside the corresponding component of \(H_0(d)\). These zero paths and the \(g\) retained edges assemble a closed walk of \(H\) with odd monodromy and total integer turn weight \(g\). Split this closed walk into simple cycles, discarding paired traversals. Its mod-two turn sum is one, so at least one simple component has odd monodromy and weight at most \(g\). This gives a port cocircuit intersecting \(X_d\) in at most \(1+g\), proving (2).

Finally, if \(K_d\) were bipartite, its constant-one edge cochain would be a cut. Pulling that cut back through the zero-turn components would make \(d\) a cut of \(H\), contradicting the nonzero covering-monodromy class \(a\). Thus \(K_d\) has an odd cycle. \(\square\)

**Corollary 2 (single-disagreement loops).** A port cocircuit \(Y\) with \(|X_d\cap Y|=2\) exists if and only if \(K_d\) has a loop; equivalently, some positive-turn edge \(e=uv\) has both endpoints in the **same** connected component of \(H_0(d)\).

For the folded cube, the established nongeodesic monochromatic-antipodal-path theorem supplies this loop for every antipodally odd coloring. The open geodesic conjecture asks for a loop with a much stronger distance property.

## 2. The cube zero-turn metric

Let \(n\ge4\), \(G_n=Q_n/\langle\tau\rangle\), \(H_n=L(G_n)\), and \(d\) be any deck-odd cube-edge coloring signature. Let
\[
\mathcal L_d=
\{\,e=uv\in E(H_n): d(e)=1,\ 
u,v\text{ lie in one component of }H_0(d)\,\}.
\tag{5}
\]
These are precisely the positive-turn edges that become loops of \(K_d\). For \(e=uv\in\mathcal L_d\), let \(\operatorname{dist}_{H_0(d)}(u,v)\) be their ordinary shortest-path distance using only zero-turn edges, and put
\[
\boxed{\ell_1(d)=
1+\min_{uv\in\mathcal L_d}
\operatorname{dist}_{H_0(d)}(u,v),}
\tag{6}
\]
taking \(+\infty\) when \(\mathcal L_d\) is empty.

**Theorem 3 (quantized geodesic distance defect).** When \(\mathcal L_d\ne\varnothing\), there exists an integer \(q_d\ge0\) such that
\[
\boxed{\ell_1(d)=n+2q_d.}
\tag{7}
\]
Moreover,
\[
\boxed{
\text{A full monochromatic antipodal geodesic exists}
\iff \ell_1(d)=n
\iff \min_{uv\in\mathcal L_d}\operatorname{dist}_{H_0(d)}(u,v)=n-1.
}
\tag{8}
\]
In particular, a hypothetical coloring refuting NORI1 must satisfy
\[
\boxed{
\operatorname{dist}_{H_0(d)}(u,v)\ge n+1
\quad\text{for EVERY }uv\in\mathcal L_d.
}
\tag{9}
\]

*Proof.* Every \(e=uv\in\mathcal L_d\), together with a shortest zero-turn path from \(u\) to \(v\), forms a simple turn cycle \(C_e\) with \(w_d(C_e)=1\). Thus \(\ell_1(d)\) is the minimum length of a simple odd-monodromy turn cycle containing precisely one positive-turn edge. Every odd-monodromy simple turn cycle in \(H_n\) has length at least \(n\), by the antipodal displacement bound of Article XI.

Choose such a cycle of minimum length, \(C\). If it contains a stationary edge state, the star-triangle shortening theorem permits deleting that state while retaining simplicity and odd monodromy. Its two incident turn labels are binary, and the shortcut label is their XOR. Since \(C\) contains only one positive-turn label, the integer turn cost of the shortened cycle is still one (it cannot be zero, by odd monodromy). This contradicts the minimum choice. Consequently \(C\) has no stationary contacts.

Its lifted edge-state sequence therefore represents a moving cube walk from \(x\) to \(x^*\), of length \(|C|=\ell_1(d)\). Each of the \(n\) coordinate directions appears an **odd positive** number of times in such a walk. Hence the length is \(n+2q_d\) for a nonnegative integer \(q_d\), proving (7).

If \(\ell_1(d)=n\), the lifted walk uses each coordinate once, so it is a full antipodal geodesic. Its cyclic turn word has one nonzero label; choose the root immediately after that turn, making all \(n-1\) internal turns zero. Conversely, a monochromatic full antipodal geodesic has precisely one cyclic nonzero turn (its closing seam, by reversal oddness); its turn cycle has length \(n\), showing \(\ell_1(d)\le n\). The antipodal lower bound forces equality. Formula (6) gives the remaining equivalence, and (7) gives (9) under the negation. \(\square\)

**Corollary 4 (explicit graph algorithm).** For a supplied cube coloring, the existence of a full monochromatic antipodal geodesic can be decided without enumerating \(n!\) coordinate permutations. Form \(H_0(d)\), find its connected components, and for every positive-turn edge \(uv\) internal to a zero component run a shortest-path search from \(u\) to \(v\) in \(H_0(d)\). A shortest path with \(n-1\) edges together with \(uv\) certifies a monochromatic antipodal geodesic. A direct implementation takes
\[
O\bigl(|E(H_n)|(|V(H_n)|+|E(H_n)|)\bigr)
\]
time and linear working space in the explicit turn graph. The method does not decide the all-dimensional conjecture uniformly; it decides the instance given by its complete edge coloring.

## 3. What the contraction preserves and what it loses

Theorem 1 settles the **unrestricted minimum port-cocircuit intersection** as an odd-girth calculation after zero-turn contraction. But contraction discards both the number of zero turns used between positive turns and the moving-coordinate resources of the lift. A loop of \(K_d\) is therefore not necessarily a geodesic cocircuit: its shortest zero path can contain repeated moving directions, forcing a cycle of length \(n+2q_d\) with \(q_d>0\).

The distinction is now measured by the intrinsic nonnegative integer \(q_d\). Existing unrestricted port-two intersection results guarantee that \(q_d\) is finite for the cube. NORI1 is equivalent to \(q_d=0\). Any general matroid theorem proving that a point-loop of the zero-turn contraction can be **shortened to the covering-displacement distance** under the folded-cube exchange axioms would establish NORI1. The star-triangle shortening theorem removes stationary contacts but preserves moving-direction multiplicities; balanced hexagon exchanges alter the coordinate order but need not reduce the repeated-direction excess. Thus the remaining obstruction is a metric/resource defect, not a deficit of pointed-matroid parity.

## 4. Intrinsic binary-matroid port-parallelism formulation

The graph contraction above is a special case of a matroid identity that does not assume a graph-cover representation.

**Lemma 5 (port-cocircuit intersection as a dual-minor circuit girth).** Let \(D\) be a finite matroid, \(p\in E(D)\), and \(X\subseteq E(D)\) with \(p\in X\). Put \(S=E(D)\setminus X\) and \(N=D^*/S\). Then
\[
\boxed{
\min_{\substack{Y\in\mathcal C^*(D)\\p\in Y}}
|X\cap Y|
=\min_{\substack{C\in\mathcal C(N)\\p\in C}}|C|.
}
\tag{10}
\]
Either minimum may be infinite if there is no relevant circuit or cocircuit.

*Proof.* Every circuit \(C\) of the contraction \(D^*/S\) lifts to a circuit \(Y\) of \(D^*\) with \(Y\setminus S=C\); this is the circuit description of matroid contraction. Hence the left-hand minimum is at most the right-hand minimum. Conversely, if \(Y\) is a circuit of \(D^*\) containing \(p\), then \(p\) lies in the closure of \(Y\setminus\{p\}\). After contracting \(S\), it still lies in the closure of \((Y\cap X)\setminus\{p\}\) in \(N\). Therefore a circuit \(C\) of \(N\) containing \(p\) exists inside \(Y\cap X\), and \(|C|\le|Y\cap X|\). This proves the reverse inequality. \(\square\)

**Corollary 6 (unrestricted two-intersection is parallelism).** If \(D\) is binary and \(X\in Z(D)\) contains \(p\), then \(p\) is **not a loop** of the contracted dual minor \(N=D^*/(E(D)\setminus X)\). Moreover
\[
\boxed{
\exists Y\in\mathcal C^*(D)\ (p\in Y,\ |X\cap Y|=2)
\iff
p\text{ belongs to a two-element parallel circuit of }N.
}
\tag{11}
\]
In the signed-cover representation, the parallel element is a positive-turn loop of \(K_d\): both its column and the port column of the contracted primal matrix (3) are \((0,\ldots,0,1)^\mathsf T\).

*Proof.* Binary cycle–cocircuit orthogonality forbids any one-element intersection of \(X\) with a cocircuit containing \(p\). Lemma 5 thus forbids a port loop in \(N\) and identifies intersection two with a two-element port circuit of \(N\). In (3), a positive graph loop has zero incidence column and bottom entry one, as does the port, proving the claimed correspondence. \(\square\)

This provides a fully matroid-intrinsic unrestricted two-intersection criterion, independent of shortest-cocircuit size. The remaining cube conjecture additionally asks that a corresponding lifted port cocircuit have size \(n+1\). The contraction minor forgets the lengths of its contracted zero-turn paths; Theorem 3 measures precisely that lost resource-length information by \(q_d\).

## 5. Graphic-matroid fundamental circuits and a basis-selection form of NORI1

The distance defect of Theorem 3 can also be expressed using **basis exchange inside a graphic matroid**, without referencing a selected path. Let \(M_0=M(H_0(d))\), the cycle matroid of the zero-turn graph, and let \(\mathcal B_0\) be its set of spanning-forest bases. For \(T\in\mathcal B_0\) and a positive edge \(e=uv\in\mathcal L_d\), let \(C_T(e)\) be the unique fundamental circuit of \(e\) relative to \(T\) in the full graphic cycle matroid \(M(H_n)\). Equivalently, \(C_T(e)\) is \(e\) together with the unique tree path connecting its ends.

**Proposition 7 (basis-choice formula for the defect).** For any antipodally odd cube-edge coloring with \(\mathcal L_d\ne\varnothing\),
\[
\boxed{
\ell_1(d)=\min_{\substack{T\in\mathcal B_0\\e\in\mathcal L_d}}
|C_T(e)|,\qquad
q_d=\frac12\left(
\min_{\substack{T\in\mathcal B_0\\e\in\mathcal L_d}}|C_T(e)|-n
\right).
}
\tag{12}
\]
Consequently,
\[
\boxed{\text{NORI1 for this coloring}\iff
\exists\,T\in\mathcal B_0,\ e\in\mathcal L_d:\ |C_T(e)|=n.}
\tag{13}
\]

*Proof.* Every \(T\in\mathcal B_0\) joins the endpoints of every \(e\in\mathcal L_d\) by a zero-turn tree path, so \(|C_T(e)|-1\ge\operatorname{dist}_{H_0(d)}(u,v)\). Conversely, a shortest zero-turn path \(P\) from \(u\) to \(v\) is an independent set of the graphic matroid \(M_0\) and can be extended to a spanning-forest basis \(T\). Because \(T\) contains \(P\), its unique tree path between \(u,v\) is \(P\); thus \(|C_T(e)|=1+|P|\). Minimize over \(e\) and invoke Theorem 3. \(\square\)

This separates the proposed general matroid argument into two logically distinct steps. The unrestricted port intersection theorem supplies **parallelism after contracting all zero turns**, i.e. a positive \(e\) closing inside a zero component. The missing step is a compatible **basis selection** of that zero-turn component in which the mate \(e\) has a fundamental circuit of the covering-displacement length \(n\).

The latter property is stronger than ordinary matroid exchange or binary orthogonality: it compares a fundamental-circuit cardinality with the geometric displacement of the two-cover. Once that cardinality is \(n\), the cube's antipodal parity automatically forces each coordinate resource to occur once, so no further resource-independence hypothesis is needed in the cube model. For boundary tournaments, by contrast, a short port circuit need not use many original vertices, and the independent-resource path language must still be supplied separately.

## 6. Chordless minimizers and simple moving cycles

The minimum-length one-disagreement cycle has a stronger structural property than the absence of stationary contacts.

**Theorem 8 (one-disagreement chord elimination).** Let \(H\) be a finite simple graph with a binary edge cochain \(d\). Among all simple cycles with integer turn weight
\[
w_d(C)=\sum_{e\in C}d(e)=1,
\]
choose a cycle \(C\) of minimum length. Then \(C\) is an **induced cycle of \(H\)**: there is no edge of \(H\) joining nonconsecutive vertices of \(C\). More generally, every one-disagreement simple cycle admits a sequence of strictly length-decreasing chord eliminations ending at an induced one-disagreement cycle.

*Proof.* Let \(h\) be a chord of a simple cycle \(C\) with \(w_d(C)=1\). The chord splits \(C\) into two strictly shorter simple cycles, using its two complementary arcs. Of the arcs, precisely one contains the unique positive-turn edge of \(C\). If \(d(h)=0\), choose the arc containing that edge; the resulting shorter cycle still has weight one. If \(d(h)=1\), choose the other arc, whose original edges all have cost zero; the chord contributes its unique positive edge. In both cases there is a shorter one-disagreement cycle. Iteration terminates and establishes the result. \(\square\)

**Corollary 9 (simple folded-cube core).** For the cube \(n\ge4\), a minimum-length monodromy-one cycle with one changed turn projects from \(H_n=L(G_n)\) to a **simple odd-monodromy cycle in \(G_n=Q_n/\tau\)**, whose lift is a self-avoiding path between antipodal vertices of \(Q_n\), with no two interior vertices related by the antipodal map. Its length is \(n+2q_d\).

*Proof.* Theorem 8 makes the turn cycle an induced cycle of \(L(G_n)\), of length at least \(n\ge4\). Any induced line-graph cycle of length at least four arises from a simple cycle of the base graph: consecutive edge-state vertices must meet at different endpoints of each base edge, else the preceding and following states are adjacent and create a chord. Moreover the contact vertices cannot repeat, since three or more selected edge states would then lie in the same base-vertex star clique, producing a chord of the induced cycle. Thus the moving walk is a simple base-graph cycle. Its monodromy is one, so its lifted path begins and ends at antipodal vertices, and no two distinct interior vertices project to the same base vertex. The direction-parity argument of Theorem 3 gives its length \(n+2q_d\). \(\square\)

**Example (why chordlessness alone does not close NORI1).** In every dimension \(n\ge4\), the following cube-vertex sequence, written as subsets of \([n]\), is a path from \(\varnothing\) to \([n]\):
\[
\varnothing,\ \{1\},\ \{1,2\},\ \{2\},\ \{2,3\},\
\{1,2,3\},\ \{1,2,3,4\},\ldots,[n].
\tag{14}
\]
Its direction sequence is \(1,2,1,3,1,4,5,\ldots,n\), of length \(n+2\). Its intermediate vertices have pairwise distinct antipodal orbits, so its projection is a simple monodromy-one cycle of length \(n+2\) in \(G_n\), corresponding to an induced turn cycle in \(H_n\). This is a geometric example, not an alleged NORI1 counterexample: prescribing one changed turn on this longer cycle does not rule out a monochromatic geodesic elsewhere.

Thus Theorem 8 removes all chord and stationary-contact defects from the shortest one-positive cocircuit, leaving **simple odd-voltage cycles of excess \(2q_d\)** as the sole geometric obstruction. A successful closure argument must exploit the cube's coordinate-square exchange structure to eliminate that positive excess; graph-theoretic chord shortening by itself is insufficient.

## 7. Antipodal component-contact graph and port-parallel bundles

Let \(\widetilde G\to G\) be a connected regular two-sheeted graph cover with deck transformation \(\tau\), and let \(c:E(\widetilde G)\to\mathbb F_2\) be deck-odd, so \(c(\tau e)=1+c(e)\). Let \(R\) be the subgraph of color-zero covering edges, omitting isolated vertices; write \(R_1,\ldots,R_s\) for its edge-containing connected components. For a lifted vertex \(x\) incident with a red edge define \(\rho(x)=i\) by \(x\in R_i\), and put \(a_x=\deg_R(x)\), including \(a_x=0\) when no red edge is incident.

Construct the **antipodal component-contact multigraph** \(A_c\) with vertices \(R_1,\ldots,R_s\). For each pair \(\{x,\tau x\}\) with \(a_xa_{\tau x}>0\), place \(a_xa_{\tau x}\) parallel edges between \(R_{\rho(x)}\) and \(R_{\rho(\tau x)}\), allowing loops.

**Theorem 10 (component-contact realization).** Let \(K_d\) be the zero-turn contraction of the quotient line graph \(H=L(G)\) from Theorem 1. There is a canonical multigraph isomorphism
\[
\boxed{K_d\cong A_c.}\tag{15}
\]
In particular \(K_d\) is connected and nonbipartite. The entire contribution of a lifted vertex orbit is a single parallel edge bundle of cardinality
\[
\boxed{a_xa_{\tau x}=a_x(\deg_{\widetilde G}(x)-a_x).}\tag{16}
\]

*Proof.* Lift the zero-turn graph to \(L(\widetilde G)\). Its edges join incident covering edges of the same color, so its connected components are the line graphs of the monochromatic edge components. The deck transformation exchanges colors and pairs \(R_i\) with the color-one component \(\tau R_i\); the quotient zero-turn components are therefore indexed by red components \(R_i\). A positive turn at \(x\) joins a red covering edge at \(x\) to a blue covering edge at \(x\). The latter is the deck image of a red covering edge at \(\tau x\). Its two quotient components are \(R_{\rho(x)}\) and \(R_{\rho(\tau x)}\). Every choice of one red edge at each antipodal endpoint specifies one positive-turn orbit, and no orbit is counted twice since \(x,\tau x\) are one base vertex. This gives \(a_xa_{\tau x}\) parallel edges and exhausts the positive turns. Theorem 1 gives connectedness and nonbipartiteness. Deck oddness implies \(a_{\tau x}=\deg_{\widetilde G}(x)-a_x\). \(\square\)

**Corollary 11 (large parallel bundles).** If the covering graph has minimum degree \(m\ge3\), every edge of \(K_d\) belongs to a parallel bundle containing at least \(m-1\) elements. Every nonloop edge lies in a two-edge cycle; hence \(K_d\) has no bridges.

*Proof.* Both factors in a nonempty bundle are positive integers summing to a degree at least \(m\), so their product is at least \(m-1\). Each bundle consists of edges with the same two endpoints. \(\square\)

**Corollary 12 (loop characterization and port-parallel amplification).** The graph \(K_d\) has a loop if and only if some color-zero edge component \(R_i\) contains an antipodal pair \(x,\tau x\). More precisely, an edge contributed by the vertex orbit \(\{x,\tau x\}\) is a loop if and only if \(\rho(x)=\rho(\tau x)\). Such a vertex orbit contributes at least \(m-1\) distinct loops when the minimum degree is \(m\ge3\). In the primal pointed contraction of Theorem 1, these loop columns are all identical to the port column, so the port has at least \(m-1\) parallel mates.

*Proof.* The edge corresponding to \(\{x,\tau x\}\) is a loop if and only if \(\rho(x)=\rho(\tau x)\). In the contracted incidence-plus-monodromy matrix, a graph loop has zero incidence column and bottom entry one, as does the distinguished port. Apply Corollary 11. \(\square\)

**Lemma 13 (monochromatic antipodal metric).** In the cube cover,
\[
\boxed{
\ell_1(d)=
\min_{\substack{x\in Q_n,\ \varepsilon\in\{0,1\}\\
x,\tau x\text{ joined by an }\varepsilon\text{-colored path}}}
\operatorname{dist}_{G_\varepsilon}(x,\tau x),
}\tag{17}
\]
where \(G_\varepsilon\) is the spanning subgraph of cube edges of color \(\varepsilon\), and the distance is measured inside that monochromatic subgraph.

*Proof.* Any monochromatic antipodal path gives a turn walk of zero internal cost and one positive closing turn, hence an odd-monodromy turn walk of no larger length. Splitting it into simple cycles yields a one-positive simple cycle and proves \(\ell_1(d)\) is no larger than the monochromatic distance. Conversely, Theorem 3 shortens a minimum one-positive turn cycle to a moving stationary-free cycle, which lifts to a monochromatic cube path between antipodal vertices of length \(\ell_1(d)\). \(\square\)

**Proposition 14 (uniform near-short circuits within one loop bundle).** Suppose \(x,\tau x\) belong to the same color-zero component \(R_i\), and put \(L_x=\operatorname{dist}_{R_i}(x,\tau x)\). Every one of the \(a_xa_{\tau x}\) loop elements from the orbit \(\{x,\tau x\}\) belongs to a port cocircuit \(Y\) such that
\[
\boxed{|Y|\le L_x+3,\qquad |X_d\cap Y|=2.}\tag{18}
\]
These cocircuits are distinct for distinct loop edges. Consequently, for a cube coloring whose minimum monochromatic antipodal distance is \(\ell_1(d)=n+2q_d\), at least \(n-1\) distinct port cocircuits have intersection two and size at most \(n+2q_d+3\).

*Proof.* Let \(P\) be a shortest red \(x\)-to-\(\tau x\) path of length \(L_x\). Its edge states form a zero-turn path of length \(L_x-1\). Replace its initial edge by any other red edge incident at \(x\), and its terminal edge by any other red edge incident at \(\tau x\); these replacements add at most one zero turn each. Thus every pair of red incident edges at \(x,\tau x\) is joined by a zero-turn walk of length at most \(L_x+1\) in the quotient state graph. Close it by its associated positive-turn element (one of the loop bundle), and shorten the zero walk to a simple zero path. The result is a simple odd-monodromy cycle of length at most \(L_x+2\) with one positive turn. Adding the port gives (18); its positive-turn element identifies it uniquely. Take an antipodal pair attaining Lemma 13 and apply the cube degree \(m=n\) to obtain the multiplicity assertion. \(\square\)

The contact-graph structure is significantly more restrictive than an arbitrary nonbipartite multigraph: each edge belongs to a large parallel bundle, and a self-contact component yields many port-parallel elements with uniformly bounded circuit-length spread. Nevertheless, a loop is a certificate of monochromatic antipodal **connectivity**, not necessarily of a geodesic. The unresolved geometric condition is \(L_x=n\) for some self-contact, which would force zero directional excess and close NORI1.

## 8. Eulerian conservation in the antipodal contact minor

Regularity of the covering graph imposes a second global constraint on \(K_d\), beyond the large parallel bundles in Corollary 11.

**Theorem 15 (Eulerian contact conservation).** Suppose \(\widetilde G\to G\) is a connected regular two-cover, \(\widetilde G\) is \(m\)-regular, and \(c(\tau e)=1-c(e)\). Then the contracted antipodal component-contact multigraph \(K_d\) of Theorem 10 is **Eulerian**:
\[
\boxed{\deg_{K_d}(R_i)\equiv0\pmod2\qquad
\text{for every color-zero edge component }R_i.}
\tag{19}
\]
More precisely,
\[
\boxed{
\deg_{K_d}(R_i)
=\sum_{x\in V(R_i)}a_x(m-a_x),\qquad
a_x=\deg_{R_i}(x).
}
\tag{20}
\]
Loops contribute two to the graph degree.

If \(m\) is odd, every *individual local parallel bundle* has even cardinality. If \(m\) is even, a local bundle has odd cardinality precisely when \(a_x\) is odd; the collection of odd-cardinality bundles, considered modulo two on the contact graph, forms an Eulerian subgraph.

*Proof.* A base vertex orbit \(\{x,\tau x\}\) contributes \(a_xa_{\tau x}\) edges between the red components containing \(x\) and \(\tau x\), by Theorem 10. Its contribution to the degree of a red component is \(a_xa_{\tau x}\) for each endpoint \(x\) of that orbit lying in the component; if both antipodal endpoints belong to it, the bundle is a loop and the contribution is counted twice. Summing the contributions over all vertices of \(R_i\) gives (20), since deck oddness and \(m\)-regularity yield \(a_{\tau x}=m-a_x\).

Working modulo two, \(a_x(m-a_x)\equiv(m-1)a_x\), because \(a_x^2\equiv a_x\pmod2\). The degree-sum identity inside \(R_i\) gives \(\sum_{x\in V(R_i)}a_x=2|E(R_i)|\equiv0\pmod2\). Therefore (20) is even, proving (19). For odd \(m\), the positive integers \(a_x\) and \(m-a_x\) have opposite parity and their product is even. For even \(m\), the product has the parity of \(a_x\); the already-proved even-degree condition says the odd-bundle edge set has even degree at every contact-graph vertex. \(\square\)

**Corollary 16 (common Eulerian-port-minor axiom).** The cube cover \(Q_n\to Q_n/\tau\) is \(n\)-regular. The ordered-pair cover used for ordinary boundary 3-tournaments, \(S(K_n)\to L(K_n)\), is \(2(n-2)\)-regular. Thus **both** canonical Article XI signed turn models yield Eulerian zero-turn contractions for every reversal-odd coloring. The cube additionally has even local parallel multiplicities in odd dimensions; the boundary model always lies in the even-degree branch.

In matroid language, the entire positive-turn edge multiset of \(K_d\) is a cycle of its graphic matroid \(M(K_d)\). The parity reduction of local parallel bundles is itself an Eulerian cycle. Consequently a proposed abstract common class may require an Eulerian contact minor, quantitative parallel bundles, and a distinguished port-parallel loop whose lifted fundamental circuit has covering-displacement length. The first two properties are theorems for all regular two-covers; the last is the unresolved NORI1 selector.

**Limitation.** A connected nonbipartite Eulerian multigraph with all nonloop edges in large parallel classes need not have any loops: an odd cycle with each edge replaced by two parallel edges is a counterexample to that implication. Therefore regularity and Eulerian parity alone cannot replace the cube-specific antipodal connectivity theorem, much less guarantee a length-\(n\) loop lift. These restrictions nevertheless exclude most arbitrary pointed binary matroids and supply a useful common structural hypothesis for future matroid generalizations.

## 9. Global contact-edge parity as a covering-cohomology evaluation

The Eulerian conservation law has a global counterpart. Let \(\beta\in H^1(G;\mathbb F_2)\) denote the monodromy class of a connected regular two-cover \(\widetilde G\to G\), where \(G\) is \(m\)-regular. The number of nonzero-turn edges is
\[
|E(K_d)|=\sum_{v\in V(G)}a_v(m-a_v),
\tag{21}
\]
with \(a_v\) the number of red covering edges incident with either selected lift of \(v\).

**Theorem 17 (covering-cohomology edge-parity identity).** If \(m\) is odd, then \(|E(K_d)|\) is even for every deck-odd coloring. If \(m\) is even, the all-edge set \(E(G)\) is a binary cycle of \(G\), and
\[
\boxed{
|E(K_d)|\equiv
\left\langle\beta,\ E(G)\right\rangle
\pmod2.
}
\tag{22}
\]
Thus for an even-regular quotient, the parity of the total changed-turn set depends only on the covering, **not** on the deck-odd coloring.

*Proof.* Fix one reference lift \(s(v)\) of every base vertex, and represent the covering by a binary edge-voltage cochain \(\alpha\): it is one on a base edge \(uv\) precisely when its lift from \(s(u)\) meets \(\tau s(v)\). Let \(a_v\) count red edges incident with \(s(v)\). Modulo two, \(a_v(m-a_v)\equiv(m-1)a_v\).

For each base edge \(uv\), the deck-odd coloring chooses one of its two covering-edge lifts to be red. If \(\alpha(uv)=0\), this chosen red lift is incident with either both reference endpoints \(s(u),s(v)\) or neither, and contributes zero modulo two to \(\sum_v a_v\). If \(\alpha(uv)=1\), it is incident with precisely one reference endpoint and contributes one, independently of which lift is red. Summing over all base edges gives
\[
\sum_{v\in V(G)}a_v\equiv\sum_{e\in E(G)}\alpha(e)\pmod2.
\]
If \(m\) is odd, the coefficient \(m-1\) vanishes modulo two. If \(m\) is even, the all-edge set is Eulerian; the right-hand sum is the well-defined pairing of covering cohomology with the all-edge cycle, proving (22). \(\square\)

**Corollary 18 (even contact-edge count for both canonical models).** For every antipodally odd \(n\)-cube edge coloring with \(n\ge3\), and for every ordinary reversal-odd boundary 3-tournament on \(n\ge4\) vertices,
\[
\boxed{|E(K_d)|\equiv0\pmod2.}
\tag{23}
\]

*Proof.* If the cube dimension \(n\) is odd, Theorem 17 applies immediately. If \(n\ge4\) is even, choose the sheet of the folded-cube covering whose first coordinate is zero. The voltage is one precisely on quotient edges of direction one; their number is \(2^{n-2}\), which is even. Thus the cohomology pairing in (22) vanishes.

For boundary tournaments the ordered-pair cover \(S(K_n)\to L(K_n)\) has degree \(m=2(n-2)\), and its covering class is the canonical contact-curvature class \(\kappa_{K_n}\), established in the monodromy-tower Subsection. Orient \(K_n\) transitively with vertices \(0,1,\ldots,n-1\). At vertex \(v\) there are \(v\) incoming and \(n-1-v\) outgoing edges, and curvature one occurs on pairs with the same incidence sense. Summing the curvature over all edges of \(L(K_n)\) therefore gives
\[
\sum_{v=0}^{n-1}\left[
\binom v2+\binom{n-1-v}2
\right]
=2\binom n3\equiv0\pmod2.
\]
Apply Theorem 17. \(\square\)

Theorems 15 and 17 identify a pair of common matroidal constraints: the entire positive-turn edge multiset is an Eulerian cycle in the graphic matroid of the contact graph, and it has even cardinality. Equivalently, its evaluation under the constant-one edge functional is zero. These conditions survive arbitrary deck-odd recoloring in both canonical systems. They do not force a length-\(n\) lift of a port-parallel loop; that additional metric selection is the remaining obstruction to NORI1.

## 10. Endpoint-star tree certificate and rank amplification

The preceding results measure a hypothetical defect \(q_d>0\) by the length of a monochromatic antipodal path. The regular cubical endpoint stars force that metric defect to appear as **graphic rank** in the corresponding monochromatic component.

**Theorem 19 (endpoint-star independent-tree bound).** Let \(c\) be any antipodally odd two-coloring of \(E(Q_n)\), \(n\ge3\), and suppose \(x\) and \(x^*\) belong to one monochromatic component \(R\). Let \(P=(v_0=x,v_1,\ldots,v_L=x^*)\) be a *shortest* monochromatic path between these two endpoints, where \(L\ge n\). Then the union of \(P\) with **all monochromatic edges incident to either endpoint** is a tree having
\[
\boxed{L+n-2\text{ edges and }L+n-1\text{ vertices}.}
\tag{24}
\]
In particular, writing \(M(R)\) for the graphic cycle matroid of the monochromatic component,
\[
\boxed{\operatorname{rank}M(R)=|V(R)|-1\ge L+n-2.}
\tag{25}
\]

*Proof.* If a monochromatic edge joined \(v_0\) to a later path vertex \(v_j\) with \(j\ge2\), replacing the initial \(j\) path edges by this edge would shorten the monochromatic path from \(x\) to \(x^*\), contradicting minimality. The same argument at \(v_L\) shows that its only monochromatic neighbor on \(P\) is \(v_{L-1}\). By deck oddness, the monochromatic endpoint degrees satisfy
\[
\deg_c(x)+\deg_c(x^*)=n,
\]
because each coordinate-direction edge at \(x\) is paired with the oppositely colored edge at \(x^*\). The \(n\) endpoint-neighbor vertices are all distinct for \(n\ge3\): the neighbors of \(x\) and \(x^*\) belong to Hamming layers one and \(n-1\), respectively. Among those \(n\) monochromatic endpoint-neighbor vertices, only \(v_1\) and \(v_{L-1}\) belong to \(P\). Every other endpoint red edge therefore attaches a new leaf to \(P\), and there are \(n-2\) such edges. The resulting union is a tree with the asserted sizes. It is a graphic independent set in \(M(R)\), so the rank inequality follows. \(\square\)

**Corollary 20 (rank cost of cubical geodesic defect).** Let \(\ell_1(c)=n+2q_d\) be the shortest monochromatic antipodal-path length from Theorem 3, and let \(R\) be a monochromatic component containing a pair achieving this length. Then
\[
\boxed{
|V(R)|\ge 2n+2q_d-1,\qquad
\operatorname{rank}M(R)\ge2n+2q_d-2.
}
\tag{26}
\]
Consequently, **if every monochromatic component containing an antipodal pair has fewer than \(2n+1\) vertices, then NORI1 holds for that coloring.** Conversely, a hypothetical counterexample to NORI1 must have every such component of order at least \(2n+1\).

*Proof.* Substitute \(L=n+2q_d\) into Theorem 19; if \(q_d>0\), integrality makes \(q_d\ge1\), giving the threshold. For another self-contact component the same argument uses its own shortest antipodal distance, which is no smaller than \(\ell_1(c)\). \(\square\)

Theorem 19 is a useful graphic-matroid rank constraint on any port-parallel bundle: a self-contact loop with shortest lift of length \(n+2q\) can occur only in a monochromatic component carrying an independent tree of rank at least \(2n+2q-2\). The proof uses the combination of shortest-path chordlessness and complementary antipodal endpoint stars, not binary parity alone.

**Scope.** The rank bound by itself does not force \(q=0\). A partial monochromatic subgraph can contain a length-\(n+2\) antipodal path, both complementary endpoint stars, and no shorter path between its chosen endpoints, with \(2n+1\) vertices. Extending such a partial subgraph to a full deck-odd coloring may create additional monochromatic antipodal geodesics elsewhere. Thus Theorem 19 supplies a rigorous rank barrier for a hypothetical counterexample but not its exclusion.

### Cartesian metric amplification and cross-antipodal chords

For a legal antipodally odd binary edge coloring \(c\) of \(Q_n\), \(n\ge2\), let \(L(c)=\ell_1(c)\) denote the shortest length of a monochromatic antipodal path. The antipodal-path existence theorem ensures finiteness. Put \(\delta(c)=(L(c)-n)/2\). Every antipodal path has length congruent to \(n\) modulo two; consequently \(\delta(c)\) is a nonnegative integer, vanishing precisely when there is a monochromatic full geodesic.

For legal \(c\) on \(Q_n\) and \(d\) on \(Q_m\), define the *independent Cartesian product* \(c\Box d\) on \(Q_{n+m}\): first-factor edges receive their colors from \(c\), second-factor edges from \(d\), independent of the vertex in the other factor. This coloring is legal.

**Theorem 21 (product additivity of shortest monochromatic antipodal distance).** For legal colorings \(c,d\) with dimensions at least two,
\[
\boxed{L(c\Box d)=L(c)+L(d),\qquad\delta(c\Box d)=\delta(c)+\delta(d).}
\]

*Proof.* Antipodal reflection maps monochromatic antipodal paths of color zero bijectively to those of color one, so the shortest antipodal length for either specified color is \(L\). Project any monochromatic antipodal path in the product onto both factors. The projections are monochromatic antipodal walks; deleting closed subwalks shows their lengths are at least \(L(c)\) and \(L(d)\). Their lengths add up to the length of the original product path. Conversely, choose shortest monochromatic antipodal paths of one common color in the factors, and concatenate their lifts in the product. This gives a monochromatic antipodal path of length \(L(c)+L(d)\). Subtracting \(n+m\) and dividing by two yields the second equality. \(\square\)

**Corollary 22 (sublinear-detour equivalence for unrestricted NORI1).** Define
\[
\Delta(N)=\max\{\delta(c):c\text{ is a legal coloring of }Q_N\},\quad N\ge2.
\]
Then \(\Delta(n+m)\ge\Delta(n)+\Delta(m)\) for \(n,m\ge2\). The following assertions are equivalent:

(i) Every legal cube coloring in every dimension admits a monochromatic full geodesic.

(ii) \(\Delta(N)=o(N)\) as \(N\to\infty\).

(iii) There is an unbounded sequence \(N_k\) for which \(\Delta(N_k)=o(N_k)\).

Indeed, if a counterexample \(c\) exists in dimension \(m\) with \(\delta(c)=q\ge1\), then
\[
\boxed{\Delta(N)\ge q\left\lfloor\frac{N-2}{m}\right\rfloor\ (N\ge m+2),
\qquad \liminf_{N\to\infty}\frac{\Delta(N)}N\ge\frac qm.}
\]

*Proof.* Superadditivity follows from Theorem 21. For \(N\ge m+2\), set \(h=\lfloor(N-2)/m\rfloor\) and \(r=N-hm\), so \(2\le r\le m+1\). Combine \(h\) independent copies of \(c\) with an arbitrary legal coloring \(d\) of \(Q_r\), which exists for every \(r\ge2\). Product additivity gives detour \(hq+\delta(d)\ge hq\). The displayed bound contradicts (iii), showing (iii) implies (i); (i) implies (ii) implies (iii) immediately. \(\square\)

In particular, a bound \(L(c)\le N+o(N)\) **uniform over all legal colorings** would prove unrestricted NORI1. Conversely, any counterexample yields legal colorings in every sufficiently large dimension with monochromatic antipodal distance \(N+\Omega(N)\).

**Theorem 23 (cross-antipodal chord exclusion).** Let \(P=(v_0,\ldots,v_L)\) be a monochromatic antipodal path of minimum length \(L=L(c)\), so \(v_L=\bar v_0\). If \(0\le i<j\le L\) and \(j-i\le L-2\), then
\[
\boxed{d_H(v_i,v_j)\le n-2.}
\]
In addition, \(L\le 2^{n-1}\).

*Proof.* If \(d_H(v_i,v_j)=n\), their monochromatic subpath is a shorter antipodal path. If \(d_H(v_i,v_j)=n-1\), the cube edge \(e=\{v_i,\bar v_j\}\) exists and its antipodal edge \(\bar e=\{\bar v_i,v_j\}\) has the complementary color. One of \(e,\bar e\) therefore has the color of \(P\). When \(e\) does, append \(e\) to the subpath \(v_j,\ldots,v_i\), obtaining a monochromatic antipodal walk from \(v_j\) to \(\bar v_j\). When \(\bar e\) does, append it to the subpath \(v_i,\ldots,v_j\), obtaining such a walk from \(v_i\) to \(\bar v_i\). Both walks have length \(j-i+1\le L-1\); deletion of closed subwalks contradicts minimality of \(L\). This proves the Hamming-distance bound.

A shortest path contains no repeated vertices. Nor can it contain another antipodal pair, since that pair would be joined by a shorter monochromatic subpath. Hence the \(L+1\) vertices of \(P\) occupy \(L\) antipodal vertex orbits: its endpoints share one orbit, and its other vertices occupy different orbits. There are \(2^{n-1}\) antipodal vertex orbits, proving \(L\le 2^{n-1}\). \(\square\)

The product formula translates any failure of geodesic existence into a linear asymptotic obstruction; the chord theorem constrains shortest witnesses to avoid near-antipodal internal pairs. Both conclusions apply to colorings with unrestricted nonlinear dependence. The missing step remains a uniform sublinear upper bound on \(L(c)-n\).


**Proposition 24 (linear-detour paths satisfy cross-antipodal chord exclusion).** For every \(n\ge5\), there is a simple antipodal path \(P=(v_0,\ldots,v_L)\) in the uncolored cube \(Q_n\), of length
\[
\boxed{L=n+2\left\lfloor\frac{n-3}{2}\right\rfloor,}
\]
such that
\[
d_H(v_i,v_j)\le n-2
\quad\text{whenever }0\le i<j\le L,\ j-i\le L-2.
\]
Thus the Hamming-distance conclusion of Theorem 23, considered as a condition on the vertex sequence alone, permits detour growing linearly with dimension.

*Proof.* Let \(s=2\lfloor(n-1)/2\rfloor\), which is even, put \(z=s+1\), and let \(\varepsilon=n-s-1\in\{0,1\}\). Starting at the all-zero vertex, traverse the direction word
\[
W=(1,z,2,z,\ldots,s-1,z,s)
\]
and, when \(\varepsilon=1\), append direction \(t=s+2=n\). Each of the ordinary directions \(1,\ldots,s\) occurs once, direction \(z\) occurs \(s-1\) times (an odd number), and direction \(t\), if present, occurs once. Hence the endpoint is antipodal to the starting vertex. The ordinary-bit configurations never recur except at the two consecutive vertices surrounding a single occurrence of \(z\); those two vertices differ in their \(z\)-bit. Thus the path is simple. Its length is \(2s-1+\varepsilon=n+2\lfloor(n-3)/2\rfloor\).

Consider a contiguous proper subword \(I\) of \(W\) of length at most \(L-2\). Its Hamming displacement equals the number of directions occurring an odd number of times in \(I\). If \(I\) includes at most \(s-2\) ordinary directions, its displacement is at most
\[
(s-2)+1+\varepsilon=n-2.
\]
If \(I\) includes all \(s\) ordinary directions, it contains the entire alternating word through its final ordinary direction; its length is at least \(2s-1=L-\varepsilon\ge L-1\), impossible.

It remains that \(I\) includes \(s-1\) ordinary directions. Since these directions appear in increasing order, \(I\) contains either \(1,\ldots,s-1\) or \(2,\ldots,s\). If \(\varepsilon=0\), the only subwords of these kinds with odd \(z\)-parity extend from the first ordinary direction through the following \(z\) just before \(s\), or from the \(z\) just before \(2\) through the last ordinary direction. Both have length \(L-1\). Every allowed subword therefore has zero \(z\)-parity, and its Hamming displacement equals \(s-1=n-2\).

If \(\varepsilon=1\), the Hamming displacement of a subword with \(s-1\) ordinary directions is at most \(s+1=n-1\). To attain \(n-1\), both special directions \(z\) and \(t\) must have odd parity, so \(I\) must include the terminal \(t\). It must therefore omit the first ordinary direction while containing \(2,\ldots,s\). Its \(z\)-parity is odd only if \(I\) begins with the \(z\) immediately before direction \(2\), in which case \(I\) has length \(L-1\). Thus every allowed \(I\) has Hamming displacement at most \(n-2\). This completes both parity cases. \(\square\)

**Scope.** The constructed paths carry no prescribed coloring and need not arise as globally shortest monochromatic antipodal paths in any legal coloring. They establish a dimension-uniform obstruction to an argument using only the Hamming-distance conclusion of Theorem 23; any deduction of NORI1 from shortest paths must use additional coloring constraints.


### Reflection sensitivity and near-antipodal face shortcuts

For an undirected cube-edge coloring \(c\), define \(\partial_i c_j(z)=c_j(z)\oplus c_j(z\oplus e_i)\) for different dimensions \(i,j\). Let \(P=(v_0,\ldots,v_L)\) be a shortest color-zero path joining some antipodal pair, and write \(j_t\) for its \(t\)-th edge direction and \(k_i=|\{t:j_t=i\}|\).

**Theorem 25 (reflection sensitivity charge).** For every \(i\), each interval strictly between two consecutive occurrences of direction \(i\) in \(P\) contains a traversed edge in some direction \(j\ne i\), initially at \(z\), with \(\partial_i c_j(z)=1\). In particular,
\[
\boxed{\sum_{\substack{t=1\\j_t\ne i}}^L\partial_i c_{j_t}(v_{t-1})\ge k_i-1,\qquad
\sum_{t=1}^L\sum_{i\ne j_t}\partial_i c_{j_t}(v_{t-1})\ge L-n.}\tag{25}
\]
The assertion holds for arbitrary undirected binary edge colorings whenever a color-zero antipodal path exists.

*Proof.* Two consecutive direction-\(i\) traversals enclose a color-zero walk \(Q\) that uses no edge in direction \(i\). If every edge of \(Q\) had zero derivative \(\partial_i c_j\), translating the full walk \(Q\) by \(e_i\) would leave its edge colors zero. Since the two flanking direction-\(i\) steps are both flips by \(e_i\), replacing the flanked segment by this translate would preserve its endpoints and shorten the total color-zero antipodal walk by two. Loop-erasure would supply a shorter antipodal path, contradicting minimality. Hence each intervening interval has a derivative-one edge. These intervals are disjoint for each fixed \(i\), proving the first inequality. Every antipodal path traverses every direction an odd positive number of times, so \(\sum_i(k_i-1)=L-n\); summing the first inequalities proves the second. \(\square\)

**Corollary (unique influence successor).** If direction \(i\) has just one outgoing neighbor \(j\) in the directed influence graph and \(k_i\ge3\), then \(k_j\ge k_i\).

*Proof.* All derivative-one edges charged by the \(k_i-1\) intervening intervals are in direction \(j\). Hence \(k_j\ge k_i-1\). Both multiplicities are odd; therefore \(k_j\ge k_i\). \(\square\)

**Theorem 26 (cross-antipodal face obstruction).** Now suppose \(c\) is antipodally odd. Choose \(0\le a<b\le L\), and put \(u=v_a\), \(v=v_b\), and \(k=d_H(u,\bar v)=n-d_H(u,v)\). If
\[
\boxed{b-a+k<L,}\tag{26}
\]
then neither color admits a \(k\)-edge geodesic from \(u\) to \(\bar v\) in their common \(k\)-face.

*Proof.* If a color-zero geodesic \(Q\) runs from \(u\) to \(\bar v\), concatenate the reversed red segment of \(P\) from \(v\) to \(u\) with \(Q\). This is a color-zero antipodal walk from \(v\) to \(\bar v\), of length \(b-a+k<L\). If \(Q\) has color one, its antipodal image is a color-zero path from \(\bar u\) to \(v\). Concatenate the red segment of \(P\) from \(u\) to \(v\) with the reversal of this image, obtaining a color-zero antipodal walk from \(u\) to \(\bar u\), of the same length. Each case contradicts shortestness, after loop-erasure if required. \(\square\)

**Corollary (two-face curvature forced to vanish).** If \(d_H(u,v)=n-2\) and \(b-a\le L-3\), then each of the two length-two routes from \(u\) to \(\bar v\) uses one edge of each color. Consequently the four edge colors of the intervening square \(F\) satisfy
\[
\boxed{\bigoplus_{e\in E(F)}c(e)=0.}\tag{27}
\]

*Proof.* Apply Theorem 26 with \(k=2\). Both routes are bichromatic, so their mod-two color sums are one. XORing their sums yields zero. \(\square\)

The reflection operation charges every repeated traversal in a shortest monochromatic antipodal path to transverse influence witnessed on the path. The face obstruction extends the cross-antipodal chord argument from Hamming distance \(n-1\) to every distance \(n-k\), retaining the actual coloring information in the intervening \(k\)-face. These necessary constraints apply to hypothetical counterexamples with arbitrarily many nonlinear rules; a dimension-uniform upper bound forcing \(L=n\) remains unresolved.


### Spectator-extension isometry for monochromatic antipodal detours

Let \(m\ge2\), \(k\ge1\), and let \(c\) be an antipodally odd binary edge coloring of \(Q_m\). Choose Boolean functions \(g_1,\ldots,g_k\) on \(Q_m\) with \(g_j(\bar x)=1\oplus g_j(x)\), and define the spectator extension \(C\) on \(Q_{m+k}\) by
\[
C_i(x,y)=c_i(x)\quad(1\le i\le m),\qquad
C_{m+j}(x,y)=g_j(x)\quad(1\le j\le k).
\tag{29}
\]
The added edge colors are independent of the added vertex bits. Write \(\ell(c)\) for the length of the shortest monochromatic path joining antipodal vertices, and \(\delta(c)=(\ell(c)-m)/2\) for its detour. The shortest length is finite for antipodally odd cube colorings by the established antipodal-path theorem.

**Theorem 28 (spectator metric identity).** Every extension (29) is antipodally odd, and
\[
\boxed{\ell(C)=\ell(c)+k,\qquad \delta(C)=\delta(c).}
\tag{30}
\]
More precisely, the shortest color-zero and color-one antipodal lengths both increase by \(k\).

*Proof.* Edge consistency follows from the independence of the new rules from \(y\); deck oddness follows from the hypotheses on \(c\) and the \(g_j\). For any monochromatic antipodal walk in the extension, projection onto the first \(m\) bits is a monochromatic antipodal walk of \(c\), since its old-direction edges retain their old colors. Removing closed subwalks shows that the number of old-direction steps is at least \(\ell(c)\). Every new dimension must be traversed an odd positive number of times, so there are at least \(k\) new-direction steps. Thus \(\ell(C)\ge\ell(c)+k\).

Conversely, take a shortest color-zero antipodal path \(P\) of \(c\), from \(x\) to \(\bar x\). Antipodal translation exchanges the two colors, so its length is also the shortest possible for either color. For every new dimension \(m+j\), place its step before \(P\) if \(g_j(x)=0\), and after \(P\) if \(g_j(x)=1\). The latter step has color \(g_j(\bar x)=0\). Flipping new bits changes none of the edge colors in (29), so all these steps have color zero. They traverse every added dimension once, and their combination with \(P\) is an antipodal monochromatic walk of length \(\ell(c)+k\). This proves equality. Repeat the argument with colors exchanged for the color-specific statement. Subtracting \(m+k\) from (30) gives detour invariance. \(\square\)

**Corollary 29 (balanced lift towers at bounded distance from geodesicity).** Let \(L(c)\) denote the standard complementary paired lift of \(c\) to dimension \(2m\). For all integers \(r\ge1\), with \(N=2^r m\),
\[
\boxed{\ell(L^r(c))=N+2\delta(c),\qquad
\delta(L^r(c))=\delta(c).}
\tag{31}
\]
The lifts are legal and vertex-balanced. In particular, if a legal counterexample exists with detour \(q\ge1\), there are vertex-balanced counterexamples in arbitrarily large dimensions with shortest monochromatic antipodal length \(N+2q\), and relative excess \(2q/N\to0\).

*Proof.* The paired lift is (29), taking \(k=m\) and \(g_i=1\oplus c_i\). The old and new edge colors of each pair are complementary, so the lift is balanced. Apply Theorem 28 repeatedly, noting that each lift doubles the dimension and preserves \(\delta\). A full monochromatic antipodal geodesic exists precisely when \(\delta=0\). \(\square\)

Unlike independent Cartesian products, whose detours add by Theorem 21, spectator extensions preserve absolute detour. Thus a near-geodesic bound only along balanced lifts of a fixed coloring is compatible with an unrestricted NORI1 counterexample. A dimension-uniform bound over all balanced legal colorings must also control independent products of the interacting cores.


### Rootwise metric fibration under spectator and feedback-core deletion

Refining the preceding global spectator metric identity, fix a color \(\varepsilon\in\mathbb F_2\) and define \(D_\varepsilon(c;x)\) as the minimum length of a color-\(\varepsilon\) path from \(x\) to \(\bar x\), with value \(+\infty\) if none exists. Reversal of an antipodally translated path gives \(D_0(c;x)=D_1(c;x)\), including the infinite case.

**Theorem 30 (rootwise spectator identity).** For the legal spectator extension (29), with \(C_i(x,y)=c_i(x)\) on the \(m\) original directions and \(C_{m+j}(x,y)=g_j(x)\) on the \(k\) added directions, where every \(g_j(\bar x)=1\oplus g_j(x)\), one has
\[
\boxed{D_\varepsilon(C;(x,y))=D_\varepsilon(c;x)+k}
\tag{32}
\]
for every root \((x,y)\) and either prescribed color. Thus the sets of roots admitting monochromatic antipodal paths in the two cubes are related by
\[
\boxed{S(C)=S(c)\times Q_k.}\tag{33}
\]
The same factorization holds for roots admitting monochromatic full geodesics.

*Proof.* Any prescribed-color antipodal path of \(C\) projects to a prescribed-color antipodal walk in \(c\), with at least \(D_\varepsilon(c;x)\) old-direction steps. At least one step is needed in each added direction. Conversely, take a prescribed-color shortest antipodal path \(P\) from \(x\) to \(\bar x\). For each added direction \(m+j\), the available step at the initial old vertex has color \(g_j(x)\), and the corresponding step at the terminal old vertex has the complementary color \(g_j(\bar x)\). Place the added step before \(P\) if \(g_j(x)=\varepsilon\), and after \(P\) otherwise. All added bits are ignored by every edge-color rule, so these insertions do not change the prescribed colors of other steps. This gives length \(D_\varepsilon(c;x)+k\) from every lift root. If \(D_\varepsilon(c;x)=+\infty\), projection rules out any monochromatic antipodal path in \(C\). This proves (32)--(33). The same proof, with \(P\) a full geodesic, proves the last claim. \(\square\)

**Corollary 31 (rootwise isometry of the directed-feedback core).** In a legal coloring \(c\) of \(Q_n\), write \(j\to i\) in its directed influence graph when changing vertex bit \(j\) changes direction rule \(c_i\) somewhere. Repeatedly delete directions with no outgoing influence within the surviving vertex set. Let \(K\) be the canonical nonempty surviving feedback core, and let \(c_K\) be the restricted legal coloring. Then
\[
\boxed{D_\varepsilon(c;x)=D_\varepsilon(c_K;x_K)+n-|K|,
\quad S(c)=S(c_K)\times Q_{[n]\setminus K},
\quad\delta(c)=\delta(c_K).}
\tag{34}
\]

*Proof.* At each sink deletion, the other retained rules ignore its bit. The deleted direction's edge color is an odd Boolean function on the surviving bits, since it ignores its own bit and the coloring is antipodally odd. Thus the deleted dimension is a spectator direction as in Theorem 30. Apply (32) once per deletion; the order-independent feedback core was established in the paired-direction Subsection. Minimizing over roots and subtracting dimensions yields the detour equation. \(\square\)

**Balanced specialization.** For the paired lift \(B(c)\) on \(Q_n\times Q_n\) whose colors are \(c_i(x)\) on original directions and \(1\oplus c_i(x)\) on dummy directions, all dummy directions are sinks. Formula (32) gives
\[
D_\varepsilon(B(c);(x,y))=D_\varepsilon(c;x)+n,\qquad S(B(c))=S(c)\times Q_n.
\tag{35}
\]
This refines (31) by preserving every root's antipodal distance, including roots with no monochromatic antipodal path. All conclusions hold for arbitrary legal direction functions, including unrestricted nonlinear dependence.


### Rootwise detour polynomials and tensorization

For a legal coloring \(c\) on \(Q_n\), let \(D(c;x)=D_0(c;x)=D_1(c;x)\), as established above, and define
\[
d_c(x)=\begin{cases}(D(c;x)-n)/2,&D(c;x)<+\infty,\\+\infty,&D(c;x)=+\infty.\end{cases}
\]
All finite values are nonnegative integers. Define the **rootwise detour polynomial**
\[
\boxed{P_c(t)=\sum_{\substack{x\in Q_n\\d_c(x)<+\infty}}t^{d_c(x)}\in\mathbb Z_{\ge0}[t].}
\tag{36}
\]
The coefficient \([t^q]P_c(t)\) counts roots admitting a monochromatic antipodal path of shortest length \(n+2q\); thus \(P_c(0)\) counts roots admitting monochromatic full geodesics. The antipodal-path existence theorem guarantees \(P_c\ne0\).

**Theorem 32 (rootwise Cartesian tensorization).** If \(c\) and \(d\) are legal on \(Q_n,Q_m\), and \(c\Box d\) is their independent Cartesian product, then, for every root \((x,y)\),
\[
\boxed{D(c\Box d;(x,y))=D(c;x)+D(d;y),\qquad
d_{c\Box d}(x,y)=d_c(x)+d_d(y),}
\tag{37}
\]
with the usual convention for \(+\infty\). Consequently
\[
\boxed{P_{c\Box d}(t)=P_c(t)P_d(t).}\tag{38}
\]
Under the spectator extension (29), and in particular under its complementary balanced paired lift \(B(c)\),
\[
\boxed{P_C(t)=2^kP_c(t),\qquad P_{B(c)}(t)=2^nP_c(t).}\tag{39}
\]
If \(K\) is the directed-feedback core, then \(P_c(t)=2^{n-|K|}P_{c_K}(t)\). In particular,
\[
\delta(c)=\operatorname{ord}_{t=0}P_c(t).
\tag{40}
\]

*Proof.* For a prescribed color, a product antipodal path projects to prescribed-color antipodal walks in each factor. After loop deletion, the factor lengths are at least \(D_\varepsilon(c;x)\) and \(D_\varepsilon(d;y)\). Conversely, concatenating shortest antipodal paths of the same prescribed color in the two factors gives a product antipodal path attaining their sum. The fixed-root red and blue minima agree by antipodal reflection and reversal. The identities (37) hold, including the infinite case. Subtract the sum of dimensions and divide by two; summing \(t\)-powers over the independent root pairs proves (38). By (32), spectator extension adds \(k\) to every finite antipodal length, and each original root has \(2^k\) lifted roots, giving the first part of (39). The balanced case and repeated sink-deletion identity follow. Finally the least exponent of a nonzero polynomial \(P_c\) is the minimum finite root detour, which is \(\delta(c)\). \(\square\)

This single polynomial simultaneously retains the support of antipodally reachable roots \(P_c(1)\), the geodesic-root count \(P_c(0)\), and the globally minimal detour \(\operatorname{ord}_{0}P_c\). The exact product and balanced-lift identities distinguish absolute detour amplification from root-density dilution. All formulas hold for arbitrary legal nonlinear rules.


### Connected balanced metric-amplification criterion for unrestricted NORI1

Call a legal coloring \(C\) on \(Q_N\), \(N\) even, *paired balanced* if its directions admit a partition into pairs whose two incident edge colors are complementary at every vertex. This guarantees vertex balance and remains true in every subcube retaining whole direction pairs. Its undirected interaction graph has an edge \(i-j\) if some derivative \(\partial_i C_j\) or \(\partial_j C_i\) is nonzero.

**Theorem 33 (connected balanced sublinear-detour equivalence).** Let \(\mathcal B_N\) be the class of paired-balanced legal colorings on \(Q_N\) with connected undirected interaction graph. Unrestricted NORI1 in every dimension is equivalent to
\[
\boxed{
\sup_{C\in\mathcal B_N}\bigl(L(C)-N\bigr)=o(N)
\quad\text{as }N\to\infty\text{ through even dimensions }N\ge4.
}
\tag{41}
\]
Indeed, if a counterexample \(c\) on \(Q_m\) has detour \(q=\delta(c)\ge1\), then for each integer \(h\ge2\) there exists \(C_h\in\mathcal B_{2(hm+1)}\) with
\[
\boxed{L(C_h)=2(hm+1)+2hq.}\tag{42}
\]
Thus even the balanced, paired-face-balanced, interaction-connected class contains counterexamples of linear relative antipodal detour whenever the unrestricted conjecture fails.

*Proof.* Put \(d=hm\) and form the independent \(h\)-fold product \(f=c^{\Box h}\) on \(Q_d\). By Theorem 21, \(L(f)=d+2hq\).

For \(d\ge3\), the Boolean function
\[
g(x)=x_1\oplus\prod_{j=2}^{d}(x_1\oplus x_j)
\tag{43}
\]
satisfies \(g(\bar x)=1\oplus g(x)\), because every factor \(x_1\oplus x_j\) is antipodally invariant. It depends essentially on every input bit: for \(j\ge2\), choose all other factors equal to one to witness \(\partial_jg=1\); for \(j=1\), choose \(x_2=x_1\) and \(x_3=1\oplus x_1\), so the product vanishes both before and after flipping \(x_1\), witnessing \(\partial_1g=1\).

Append one spectator direction \(s\) of color \(g(x)\). This yields a legal coloring \(f^+\) of dimension \(d+1\). Its interaction graph has a star centered at \(s\) spanning all original directions because every \(\partial_jg\) is nonzero. Hence the undirected interaction graph is connected, regardless of the factorization of \(f\). By Theorem 28, \(L(f^+)=L(f)+1=d+1+2hq\).

Take the complementary paired lift \(C_h=B(f^+)\) on \(Q_{2(d+1)}\): for each original direction \(i\), its paired directions have the color rules \((f^+)_i(x)\) and \(1\oplus(f^+)_i(x)\). This coloring is legal, paired balanced, and therefore balanced on every face retaining whole pairs. Its original-direction interaction subgraph is that of \(f^+\), hence connected. Each dummy direction interacts with at least one original direction, because an antipodally odd direction rule \((f^+)_i\) must depend on some other input bit. Consequently the full undirected interaction graph of \(C_h\) is connected. The paired-lift metric identity gives
\[
L(C_h)=L(f^+)+(d+1)=2(d+1)+2hq.
\]
This is (42), with \(N_h=2(hm+1)\). Along these even dimensions,
\[
\frac{L(C_h)-N_h}{N_h}
=\frac{hq}{hm+1}\longrightarrow\frac qm>0,
\]
contradicting (41). Conversely, if unrestricted NORI1 holds, \(L(C)=N\) for every legal coloring, so (41) follows. \(\square\)

**Scope.** Connectivity is required for the undirected interaction graph, not strong connectivity of directed influence. The added spectator and the dummy directions have no outgoing influence into the original-direction block. This theorem strengthens the unrestricted sublinear-detour criterion by allowing its hypotheses to be confined simultaneously to vertex balance, complementary direction pairs, and undirected interaction connectedness; it does not establish the required sublinear bound.


### Rigidity and multiplicities of shortest antipodal paths

Fix a legal antipodally odd coloring \(c\) of \(Q_n\). For a vertex \(x\) and a prescribed color \(\varepsilon\), let \(\mathcal S_\varepsilon(c;x)\) denote the set of directed shortest monochromatic paths from \(x\) to \(\bar x\), and let \(M_\varepsilon(c;x)=|\mathcal S_\varepsilon(c;x)|\); declare both empty and zero if \(D_\varepsilon(c;x)=+\infty\). Directed paths are counted by their ordered edge sequence. Antipodal reflection followed by reversal induces a bijection \(\mathcal S_0(c;x)\leftrightarrow\mathcal S_1(c;x)\), so their cardinalities agree.

**Theorem 34 (shortest-path factorization).** For legal colorings \(c\) of \(Q_n\) and \(d\) of \(Q_m\), every shortest prescribed-color antipodal path of the independent product \(c\Box d\) is a shuffle of a shortest prescribed-color antipodal path from \(x\) to \(\bar x\) in the first factor and one from \(y\) to \(\bar y\) in the second factor. Conversely every such shuffle is a shortest product path. In particular, when both factor distances \(a=D_\varepsilon(c;x)\), \(b=D_\varepsilon(d;y)\) are finite,
\[
\boxed{M_\varepsilon(c\Box d;(x,y))=\binom{a+b}{a}M_\varepsilon(c;x)M_\varepsilon(d;y).}
\tag{SP1}
\]
If either distance is infinite, the count is zero.

*Proof.* The two projections of an antipodal product path are prescribed-color antipodal walks, requiring at least \(a\) and \(b\) steps respectively. The rootwise metric product identity (37) gives a shortest product-path length \(a+b\), hence the two projections of each shortest path have lengths \(a\) and \(b\). Every shortest walk joining prescribed endpoints is a simple shortest path: removing any repeated-vertex closed segment would strictly shorten it. Therefore both projections belong to the corresponding sets of shortest factor paths. Conversely, interleave a pair of factor shortest paths according to any shuffle of their \(a+b\) steps. The resulting product path has prescribed color, joins antipodes, and has minimum length \(a+b\). There are \(\binom{a+b}{a}\) choices of interleaving. Projections and their interleaving recover the product path, giving a bijection and (SP1). \(\square\)

**Theorem 35 (spectator rigidity and insertion enumerator).** Suppose \(C\) is the legal \(k\)-spectator extension (29) of \(c\) on \(Q_m\), with new-direction rules \(g_j(x)\), independent of every new bit. Every shortest prescribed-color antipodal path from \((x,y)\) to \((\bar x,\bar y)\) uses each spectator direction once, and its projection onto the original cube is a shortest prescribed-color antipodal path. Conversely, fix \(P=(x_0,\ldots,x_a)\in\mathcal S_\varepsilon(c;x)\), \(x_0=x\), \(x_a=\bar x\). Place each spectator direction \(j\) at a slot \(t_j\in\{0,\ldots,a\}\) satisfying \(g_j(x_{t_j})=\varepsilon\); at a slot with \(r_t\) placed spectator directions, choose any of their \(r_t!\) orders. All resulting paths are shortest prescribed-color antipodal paths, and every such path occurs once. Thus
\[
\boxed{
M_\varepsilon(C;(x,y))
=\sum_{P\in\mathcal S_\varepsilon(c;x)}
\sum_{\substack{t_1,\ldots,t_k\in\{0,\ldots,a\}\\
g_j(x_{t_j})=\varepsilon\ \forall j}}
\prod_{t=0}^{a}\bigl|\{j:t_j=t\}\bigr|!.
}
\tag{SP2}
\]
The right-hand side is independent of \(y\). For one spectator direction,
\[
\boxed{M_\varepsilon(C;(x,y))
=\sum_{P=(x_0,\ldots,x_a)\in\mathcal S_\varepsilon(c;x)}
\#\{0\le t\le a:g_1(x_t)=\varepsilon\}.}
\tag{SP3}
\]

*Proof.* A path in the extension has at least \(D_\varepsilon(c;x)\) original-direction steps by projection and at least one step in each new direction by antipodality. The rooted spectator identity (32) attains their sum. Equality forces the original projection to be a shortest path and every spectator direction to occur once. Each spectator step leaves the original vertex fixed, and its prescribed color is equivalent to \(g_j(x_{t_j})=\varepsilon\), independently of the other spectator coordinates. Consequently the slot data and within-slot permutations reconstruct exactly all shortest paths. The root \((x,y)\) merely fixes the spectator bits at each step and imposes no further condition. Counting gives (SP2) and its specialization (SP3). \(\square\)

**Corollary 36 (shortest-path support is confined to the feedback core).** Let \(K\) be the directed-feedback core of a legal coloring \(c\). On every globally shortest monochromatic antipodal path, every direction outside \(K\) appears once. The directions traversed more than once all belong to \(K\), and deleting all directions outside \(K\) from the path leaves a shortest monochromatic antipodal path of \(c_K\). Thus if its total length is \(n+2q\), then
\[
q=\sum_{i\in K}\frac{N_i(P)-1}{2},
\]
where \(N_i(P)\) is the number of traversals in direction \(i\).

*Proof.* Apply Theorem 35 with \(k=1\) successively in reverse order along the canonical sink-deletion process. Each shortest path uses each deleted direction once and projects to a shortest path at the next stage. This does not require direction-simplicity of its feedback-core projection. \(\square\)

The factorization identifies the complete shortest-path family, strengthening the metric product law. The insertion enumerator retains color-sensitive information along shortest paths and can distinguish spectator lifts sharing identical antipodal-distance polynomials. Both apply to unrestricted nonlinear direction rules.


### Repeat-support defect: exact product and spectator laws

A monochromatic antipodal walk \(P\) in \(Q_n\) traverses each direction \(i\) an odd positive number \(N_i(P)\) of times. Define its *repeat support* and its cardinality by
\[
T(P)=\{i:N_i(P)\ge3\},\qquad r(P)=|T(P)|.
\]
Set \(r_\varepsilon(c;x)=\min r(P)\), over color-\(\varepsilon\) antipodal walks from \(x\) to \(\bar x\), taking \(+\infty\) if none exist, and put \(r(c)=\min_{x,\varepsilon}r_\varepsilon(c;x)\). Removing any closed subwalk deletes an even number of traversals in each direction and cannot increase the repeat support; hence the same minima are obtained over simple paths. Antipodal translation followed by reversal gives \(r_0(c;x)=r_1(c;x)\). The antipodal-path existence theorem makes \(r(c)\) finite, and
\[
\boxed{r(c)=0\quad\Longleftrightarrow\quad
c\text{ contains a monochromatic full antipodal geodesic}.}\tag{RS1}
\]
For each monochromatic antipodal path of length \(n+2q\),
\[
r(P)\le q=\sum_i\frac{N_i(P)-1}{2};
\]
therefore \(0\le r(c)\le\delta(c)\).

**Theorem 37 (rootwise repeat-support product and spectator laws).** For legal colorings \(c\) on \(Q_n\), \(d\) on \(Q_m\),
\[
\boxed{r_\varepsilon(c\Box d;(x,y))=
r_\varepsilon(c;x)+r_\varepsilon(d;y),\qquad
r(c\Box d)=r(c)+r(d).}\tag{RS2}
\]
The identities hold with the convention \(a+\infty=\infty\). For every legal spectator extension \(C\) of \(c\), with \(k\) added directions whose rules depend only on the original bits,
\[
\boxed{r_\varepsilon(C;(x,y))=r_\varepsilon(c;x),\qquad r(C)=r(c).}\tag{RS3}
\]
In particular \(r(B(c))=r(c)\) under the balanced paired lift, and \(r(c)=r(c_K)\) for the canonical directed-feedback core \(K\).

*Proof.* The two projections of a monochromatic antipodal walk in an independent Cartesian product are monochromatic antipodal walks in its factors. Since factor direction sets are disjoint, the repeat-support cardinality of the product walk equals the sum of those of the factor projections. This gives the lower bound in (RS2); the upper bound follows by concatenating two minimum-repeat-support paths of the same prescribed color in the respective factors. Color-specific minima agree by antipodal translation and reversal, permitting compatible choices when minimizing globally.

For a spectator extension, projection onto the original block gives the lower bound in (RS3). Conversely, take a monochromatic antipodal path attaining the original minimum. Each added direction has complementary edge colors at the original starting and terminal vertices. Traverse that added direction once at the endpoint giving the prescribed color, putting all the suitable added steps before the original path and the remaining steps afterward. Added bits are not read by any direction rule; the resulting path has the same repeated-direction set and is antipodal. This proves (RS3). Repeated sink deletion and the paired-lift definition give the final assertions. \(\square\)

**Corollary 38 (repeat-support asymptotic equivalence).** Let
\[
R(N)=\max\{r(c):c\text{ legal on }Q_N\},\qquad N\ge2.
\]
Then \(R(n+m)\ge R(n)+R(m)\). Unrestricted NORI1 is equivalent to each of the following:
\[
\boxed{R(N)=o(N)\text{ as }N\to\infty,}
\tag{RS4}
\]
or the existence of an unbounded sequence \(N_j\) for which \(R(N_j)=o(N_j)\). More precisely, a counterexample \(c\) in dimension \(m\) with \(r(c)=s\ge1\) gives
\[
\boxed{R(N)\ge s\left\lfloor\frac{N-2}{m}\right\rfloor
\quad (N\ge m+2).}\tag{RS5}
\]

*Proof.* Superadditivity is (RS2). For \(N\ge m+2\), use \(h=\lfloor(N-2)/m\rfloor\) copies of \(c\) and one arbitrary legal coloring in the residual dimension \(N-hm\in[2,m+1]\); equation (RS2) yields \(R(N)\ge hs\). This contradicts (RS4), or any unbounded sequence with \(R(N_j)=o(N_j)\). Conversely, if NORI1 holds, all values \(r(c)\) vanish. \(\square\)

**Corollary 39 (balanced-connected repeat-support closure criterion).** Let \(\mathcal B_N\) be the paired-balanced legal \(Q_N\) colorings with connected undirected direction-interaction graph, as in Theorem 33. Then unrestricted NORI1 is equivalent to
\[
\boxed{\sup_{C\in\mathcal B_N}r(C)=o(N)
\quad\text{as }N\to\infty\text{ through even dimensions}.}\tag{RS6}
\]

*Proof.* The forward direction follows from (RS1). Conversely, if a counterexample \(c\) of dimension \(m\) has \(r(c)=s\ge1\), take \(h\) independent copies \(f=c^{\Box h}\). Then \(r(f)=hs\). Append one legal spectator direction with an odd Boolean rule depending essentially on every original bit, as in equation (43) above, so the undirected interaction graph becomes connected; (RS3) preserves \(r\). Take the complementary paired lift \(C_h\) to dimension \(N_h=2(hm+1)\), preserving repeat support and ensuring paired balance. Each dummy direction is incident in the undirected interaction graph to at least one old direction, so the graph stays connected. Hence \(r(C_h)=hs\) and \(r(C_h)/N_h\to s/(2m)>0\), contradicting (RS6). \(\square\)

This repeat-support criterion is weaker as a quantitative requirement than the shortest-length criterion (41), because \(r(c)\le\delta(c)\). It requires control only of the number of distinct repeated directions in some monochromatic antipodal path and allows arbitrarily many additional traversals of those directions. It is a global target for dimension-simple path arguments with unrestricted nonlinear rules; the sublinear bound itself remains open.


### Monochromatic geodesic correction distance: the color-space metric invariant

For a legal antipodally odd coloring \(c\) on \(Q_n\), let \(\mathcal W(c)\subseteq\mathbb F_2^n\) be its realized full-geodesic color profiles indexed by direction. Define the **geodesic correction number**
\[
\boxed{\eta(c)=\min_{w\in\mathcal W(c)}|w|.}\tag{CD1}
\]
Equivalently, \(\eta(c)\) is the minimum number of blue edges along any full antipodal geodesic. Antipodal translation complements its color profile, so the same minimum is obtained by counting red edges. Hence \(\eta(c)\) is the least number of edges of the minority color on a full geodesic, allowing the chosen path, color and root to vary. In particular
\[
0\le\eta(c)\le\lfloor n/2\rfloor,\qquad
\eta(c)=0\quad\Longleftrightarrow\quad\text{\(c\) has a monochromatic full antipodal geodesic}.
\tag{CD2}
\]

Let \(\mathcal G_n\) be the set of successful legal colorings on \(Q_n\). The legal coloring space is a Boolean cube of dimension \(M_n=n2^{n-2}\), with one binary variable per antipodal edge orbit. Write \(d_{\rm orb}\) for its ordinary Hamming metric.

**Theorem 40 (geodesic correction = coloring-space distance).** For every legal coloring \(c\),
\[
\boxed{\eta(c)=\min_{g\in\mathcal G_n}d_{\rm orb}(c,g).}\tag{CD3}
\]
In particular, if \(\eta(c)=q>0\), then *every* legal coloring obtained from \(c\) by changing fewer than \(q\) antipodal edge-pair variables is also unsuccessful, and some coloring obtained by changing exactly \(q\) such variables is successful. The function \(\eta\) is 1-Lipschitz in \(d_{\rm orb}\).

*Proof.* Choose a full antipodal geodesic \(P\) for \(c\) with exactly \(q=\eta(c)\) blue edges. Its \(n\) edges have pairwise distinct directions, hence lie in distinct antipodal edge orbits. Flip the \(q\) orbits meeting those blue edges. This produces a legal coloring \(g\) in which \(P\) is entirely red, at orbit-Hamming distance \(q\) from \(c\). Thus the right side of (CD3) is at most \(q\). Conversely, if \(g\in\mathcal G_n\) has a monochromatic full geodesic \(P\), each orbit variable on which \(c\) and \(g\) disagree alters the color of at most one edge of \(P\). Hence the number of edges of \(P\) differing from its constant \(g\)-color in \(c\) is at most \(d_{\rm orb}(c,g)\). By definition and antipodal color symmetry, \(\eta(c)\le d_{\rm orb}(c,g)\). Minimize over \(g\). The stability ball and 1-Lipschitz assertions are standard consequences of the identity with distance to the nonempty subset \(\mathcal G_n\). \(\square\)

**Theorem 41 (exact product, spectator and feedback-core laws).** For arbitrary legal colorings \(c,d\),
\[
\boxed{\eta(c\Box d)=\eta(c)+\eta(d).}\tag{CD4}
\]
If \(C\) is a legal extension of \(c\) by \(k\) spectator directions with antipodally odd rules depending only on the original bits, then
\[
\boxed{\eta(C)=\eta(c).}\tag{CD5}
\]
In particular \(\eta(B(c))=\eta(c)\) under the complementary paired balanced lift, and \(\eta(c)=\eta(c_K)\) for the canonical directed-feedback core \(K\).

*Proof.* Every full antipodal product geodesic projects to a full antipodal geodesic in each factor, and its blue-edge count equals the sum of the two factor blue-edge counts. This is at least \(\eta(c)+\eta(d)\). Conversely concatenate two full geodesics attaining these two minima (using blue as the common counted color) to attain the sum. For a spectator extension, projection of any full geodesic produces a base full geodesic with at most as many blue edges; hence \(\eta(C)\ge\eta(c)\). For the reverse bound, take a base full geodesic attaining \(\eta(c)\), from \(x\) to \(\bar x\). Every spectator direction \(j\) has color \(g_j(x)\) at the initial base root and color \(g_j(\bar x)=1\oplus g_j(x)\) at the terminal base root. Insert each spectator edge at the endpoint where its color is red; all spectator steps are red, and no original edge color is changed because the original rules ignore spectator bits. This gives a full geodesic in the extension with the same blue count. Iterated spectator deletion proves the feedback-core statement. \(\square\)

**Corollary 42 (counterexample robustness amplification).** If a legal coloring \(c\) on \(Q_m\) is an unsuccessful instance, then \(q=\eta(c)\ge1\). For every \(h\ge1\), its independent Cartesian product \(c^{\Box h}\) on \(Q_{hm}\) is unsuccessful and remains unsuccessful after **any** fewer than \(hq\) antipodal edge-pair flips. Moreover its vertex-balanced paired lift \(B(c^{\Box h})\) on \(Q_{2hm}\) remains unsuccessful under the same arbitrary \(hq-1\) edge-pair flips.

One can also require *connected undirected interaction*. Append one spectator direction with an antipodally odd Boolean rule essentially dependent on each original bit (the explicit star-connecting rule of Theorem 33), then take the complementary paired lift. The resulting paired-balanced, interaction-connected legal coloring \(C_h\) has dimension \(N_h=2(hm+1)\), satisfies \(\eta(C_h)=hq\), and every legal coloring at orbit-Hamming distance less than \(hq\) from \(C_h\) remains unsuccessful. Consequently
\[
\boxed{\frac{\eta(C_h)}{N_h}\longrightarrow \frac{q}{2m}>0.}\tag{CD6}
\]

*Proof.* (CD4) gives \(\eta(c^{\Box h})=hq\). Equation (CD3) gives its robustness radius. Balanced lifting preserves \(\eta\) by (CD5), and appending a connecting spectator also preserves \(\eta\). The interaction-connectivity and pairing assertions are those proved in Theorem 33. \(\square\)

**Corollary 43 (sublinear geodesic correction equivalence).** Put
\[
E(n)=\max_{\text{legal }c\text{ on }Q_n}\eta(c).
\]
Then \(E(n+m)\ge E(n)+E(m)\). Unrestricted NORI1 is equivalent to
\[
\boxed{E(n)=o(n),}\tag{CD7}
\]
equivalently to \(E(n_j)=o(n_j)\) along any unbounded sequence \(n_j\), and also equivalent to the uniform \(o(n)\) bound restricted to paired-balanced legal colorings with connected undirected interaction graphs.

*Proof.* If NORI1 holds, \(E(n)=0\). Otherwise take one unsuccessful \(c\) in dimension \(m\) with \(\eta(c)=q\ge1\); (CD4) and arbitrary legal residual factors of dimension at least two imply \(E(n)\ge q\lfloor(n-2)/m\rfloor\) for every sufficiently large \(n\). For paired-balanced connected colorings use the explicit family \(C_h\) of Corollary 42. \(\square\)

**Corollary 44 (profile-code covering radius and directional recoloring).** For \(u\in\mathbb F_2^n\), let \(c^{(u)}\) be the legal recoloring obtained by reversing the edge colors in direction \(i\) when \(u_i=1\). Then
\[
\boxed{\eta(c^{(u)})=\min_{w\in\mathcal W(c)}d_H(u,w).}\tag{CD8}
\]
Thus the Hamming covering radius \(R_{\rm cov}(\mathcal W(c))\) is precisely
\[
\boxed{R_{\rm cov}(\mathcal W(c))=\max_{u\in\mathbb F_2^n}\eta(c^{(u)}),}\tag{CD9}
\]
and obeys the tensorization law
\[
\boxed{R_{\rm cov}(\mathcal W(c\Box d))
=R_{\rm cov}(\mathcal W(c))+R_{\rm cov}(\mathcal W(d)).}\tag{CD10}
\]
The proof is immediate from \(\mathcal W(c^{(u)})=\mathcal W(c)\oplus u\) and the established Cartesian profile product \(\mathcal W(c\Box d)=\mathcal W(c)\times\mathcal W(d)\).

**Interpretation.** The potential \(\eta(c)\) is simultaneously a geodesic color-error invariant and an ambient Hamming distance to the successful-coloring set. Its exact product law converts a hypothetical unsuccessful coloring into arbitrarily large instances with *linear* resistance to arbitrary individual legal edge-pair recolorings, even after imposing perfect balance and connected undirected interaction. This does not contradict the separate sparse-noise completion theorem: at noise rate \(A/n\), the expected number of flipped orbit variables is \(A2^{n-2}\), exponentially larger than the linear robustness radius exhibited here. The equivalence (CD7) is a new closure target on near-monochromatic **full geodesics**, separate from the repeat-support potential on arbitrary monochromatic paths; the required sublinear upper bound is not proved.
PROVENANCE CORRECTION. In the geodesic-correction Section, eta(c) is identical to Article VIII's previously defined minority-count m(c). The product rule CD4 is prior Theorem FM3, the spectator rule CD5 is prior Theorem SM2, and direction-recoloring formula CD8 is prior Theorem GD3. The Fourier second-moment formula and ballot corridor are also already proved in Article VIII. The distinctive new result here is the ambient edge-orbit Hamming metric identity CD3, which identifies the correction number with distance to the SUCCESSFUL coloring set, and its consequence that any hypothetical counterexample can be amplified into balanced interaction-connected bad colorings whose entire Hamming balls of radius linear in dimension remain bad. This paragraph clarifies priority and supersedes any interpretation of the prior formulas as newly discovered.
