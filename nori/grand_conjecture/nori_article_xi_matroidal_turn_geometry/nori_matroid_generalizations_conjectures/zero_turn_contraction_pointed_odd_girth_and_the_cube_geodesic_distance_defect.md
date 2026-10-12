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
