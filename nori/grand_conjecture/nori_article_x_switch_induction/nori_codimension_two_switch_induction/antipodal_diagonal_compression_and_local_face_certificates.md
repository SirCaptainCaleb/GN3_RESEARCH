# Antipodal diagonal compression and local face certificates

# Antipodal diagonal compression and local face certificates

Let \(n\ge3\), let \(c:E(Q_n)\to\mathbb F_2\) satisfy \(c(\bar e)=1+c(e)\), and fix distinct directions \(a,b\). Put \(D=[n]\setminus\{a,b\}\), with \(|D|=m\). After translating coordinates, let \(F\) fix \(a=b=0\). Identify \(F\) with \(Q_D\), and write \(x^*=x^D\) for complementation within \(F\). For \(x\in F\), label its exterior square by
\[
A(x)=c(xx^a),\quad B(x)=c(xx^b),\quad
C(x)=c(x^ax^{ab}),\quad E(x)=c(x^bx^{ab}).
\tag{1}
\]
Thus the routes from \(x\) to its corresponding vertex \(x^{ab}\) have color words \(A(x)C(x)\) and \(B(x)E(x)\). Antipodal oddness gives
\[
A(x^*)=1+E(x),\quad B(x^*)=1+C(x),\quad
C(x^*)=1+B(x),\quad E(x^*)=1+A(x).
\tag{2}
\]

### Odd compressed cubes

Keep the edges of \(F\) and \(F^{ab}\), and join every pair \(x,x^{ab}\) by a new edge of color \(h(x)\). The resulting graph is \(Q_D\times Q_1\). If \(d\) denotes the restriction to \(F\), its two facet colorings are
\[
g_i(x,0)=d_i(x),\qquad g_i(x,1)=1+d_i(x^*),\qquad i\in D.
\tag{3}
\]
The joining-direction edge has color \(g_t(x,z)=h(x)\). This coloring is antipodally odd if and only if
\[
h(x^*)=1+h(x).
\tag{4}
\]

For compression using original \(a\)-edges, choose one edge from each antipodal pair: the edge chosen at \(x\) is incident with \(F\), and its antipodal mate at \(x^*\) is incident with \(F^{ab}\), or conversely. Its joining color satisfies
\[
h_a(x)\in\{A(x),E(x)\},\qquad h_a(x^*)=1+h_a(x).
\tag{5}
\]
Equation (2) shows that such choices always exist and can be made independently on the antipodal pairs of vertices of \(F\). The corresponding \(b\)-compression has
\[
h_b(x)\in\{B(x),C(x)\},\qquad h_b(x^*)=1+h_b(x).
\tag{6}
\]
Both compressed cubes therefore belong to NORI1 in dimension \(n-1\). They have the same facet colorings (3) and differ only in their joining edges.

A long geodesic in a compressed cube crosses its joining direction once. Reverse it if necessary so that it goes from the lower to the upper facet, and write its word as
\[
\alpha\,h(x)\,\beta.
\tag{7}
\]
Its two lifts to \(Q_n\) have words
\[
\alpha\,A(x)C(x)\,\beta,\qquad
\alpha\,B(x)E(x)\,\beta.
\tag{8}
\]
The direction sets used before and after the crossing partition \(D\). Thus each lift uses every direction of \(Q_n\) once and has antipodal endpoints.

If \(h(x)\) is chosen from any of the four square edges, one route in (8) retains that edge color and inserts one additional letter beside it. Inserting a binary letter increases the switch count by at most two. Consequently a compressed path with at most two switches lifts to at most four switches. A compressed path with at most one switch lifts to at most three; odd-change rotation in \(Q_n\) then gives \(\mu(c)\le2\).

### Reassembly at the joining position

The following formula describes all paths through a prescribed joining edge. It depends only on the coloring \(d\) in one face.

For an arbitrary edge coloring \(d\) of \(Q_m\), a vertex \(x\in Q_m\), and \(p\in\mathbb F_2\), let \(\tau_d(x;p)\) be the least switch count of a long geodesic in the two-facet cube (3) which crosses the joining edge at \(x\), when that edge has color \(p\). Its value does not depend on the other joining-edge colors.

For a nonempty long \(d\)-geodesic \(R\) rooted at \(x\), let \(r(R)\) be its switch count and \(s(R)\) its initial edge color.

**Theorem 1 (reassembly formula).**
\[
\boxed{\tau_d(x;p)=
\min_{R:x\to x^*}
\begin{cases}
r(R),&r(R)\text{ even},\\
r(R)-1+2[s(R)\ne p],&r(R)\text{ odd}.
\end{cases}}
\tag{9}
\]

*Proof.* Split \(R=UV\) at any vertex \(u\). In the compressed cube, traverse \(U\) in reverse from \(u\) to \(x\) in the lower facet, cross the joining edge to \(x\) in the upper facet, and then traverse the reversed antipodal image of \(V\). This last segment starts at \(x\) in the upper facet and ends at \(u^*\) there. The resulting path is long.

Conversely, a compressed path crossing at \(x\) can be reassembled in the lower face: reverse its lower portion to obtain \(U\), and antipodally reverse its upper portion to obtain \(V\). The two segments concatenate into a long \(d\)-geodesic from \(x\) to \(x^*\). Thus all such compressed paths arise from the construction.

Let \(w\) be the word of \(R\), with initial color \(s\), final color \(q\), and \(r\) switches. Its compressed word is
\[
\operatorname{rev}(w(U))\,p\,
       \overline{\operatorname{rev}(w(V))}.
\tag{10}
\]
For an interior split, let \(j\in\{0,1\}\) indicate whether the cut lies at a switch. Its switch count is
\[
r-j+[s\ne p]+[1+q\ne p].
\tag{11}
\]
If \(r\) is even, \(q=s\), so the last two terms sum to one. For \(r>0\), splitting at a switch realizes the minimum \(r\). Splitting at either endpoint yields \(r+[s\ne p]\) or \(r+[1+q\ne p]\); these endpoint choices also give minimum \(r\), including \(r=0\).

If \(r\) is odd, \(q=1+s\), and the last two terms in (11) sum to \(2[s\ne p]\). A split at a switch yields \(r-1+2[s\ne p]\). Endpoint splits yield \(r+[s\ne p]\), which give no smaller value. Minimizing over \(R\) proves (9). \(\square\)

Define
\[
H_2(d,x)=\{p\in\mathbb F_2:\tau_d(x;p)\le2\}.
\tag{12}
\]

**Corollary 2 (two-switch face alternatives).** If some long \(d\)-geodesic rooted at \(x\) has at most two switches, then \(H_2(d,x)=\mathbb F_2\). Otherwise
\[
H_2(d,x)=
\{p:\text{a long }d\text{-geodesic rooted at }x
       \text{ has three switches and initial color }p\}.
\tag{13}
\]
Furthermore \(H_2(d,x^*)=1+H_2(d,x)\).

*Proof.* A path with zero or two switches gives both joining colors by (9). A one-switch path gives costs zero and two. If every face path has at least three switches, only a three-switch path whose initial color is the joining color can contribute a value at most two. Reversing a face path preserves its switch count, preserves its initial color when that count is even, and complements it when the count is odd. Applying (9) proves the final equality. \(\square\)

### Varying all antipodal selections

**Lemma 3 (selection criterion).** Suppose nonempty sets \(S(x)\subseteq\mathbb F_2\) satisfy \(S(x^*)=1+S(x)\). The following are equivalent:

(i) Every joining coloring \(h\) satisfying (4) and \(h(x)\in S(x)\) gives a compressed cube with a long geodesic having at most two switches.

(ii) Some \(x\) satisfies \(S(x)\subseteq H_2(d,x)\).

*Proof.* If (ii) holds, every admissible selection assigns a color to the joining edge at \(x\) for which a two-switch path exists. Conversely, suppose (ii) fails. At one representative \(x\) of each antipodal pair, choose a color in \(S(x)\setminus H_2(d,x)\), and give the opposite vertex its complementary color. Corollary 2 ensures that this color also belongs to \(S(x^*)\setminus H_2(d,x^*)\). No joining position now supports a two-switch long path. Every long compressed path uses one joining edge, contradicting (i). \(\square\)

For the \(a\)-compression use \(S(x)=\{A(x),E(x)\}\), and for the \(b\)-compression use \(S(x)=\{B(x),C(x)\}\). Therefore, if the universal two-switch assertion holds in dimension \(n-1\), each family has a vertex at which every available joining color supports a two-switch path. The vertices supplied by the two families may differ.

Allowing all odd joining colorings yields a full-class equivalence.

**Theorem 4 (rooted face characterization).** For every \(m\ge1\), the following statements are equivalent:

(a) Every antipodally odd edge coloring of \(Q_{m+1}\) has a long geodesic with at most two switches.

(b) Every arbitrary edge coloring \(d\) of \(Q_m\) has a vertex \(x\) satisfying one of:
- a long geodesic rooted at \(x\) has at most two switches;
- two long geodesics rooted at \(x\) each have three switches and have different initial edge colors.

*Proof.* Every antipodally odd coloring of \(Q_{m+1}\) has the form (3), with an arbitrary lower-facet coloring \(d\) and an odd joining coloring \(h\). For fixed \(d\), Lemma 3 with \(S(x)=\mathbb F_2\) says that every such \(h\) admits a two-switch path if and only if some \(x\) has \(H_2(d,x)=\mathbb F_2\). By Corollary 2, this is precisely the alternative in (b). Quantifying over \(d\) proves the equivalence. \(\square\)

### Monochromatic square routes and a hypothetical four-switch obstruction

**Corollary 5 (monochromatic diagonal completion).** Suppose a long geodesic \(R\subset F\), rooted at \(x\), has \(r\) switches and initial color \(s\). If the exterior square at \(x\) has a monochromatic route from \(x\) to \(x^{ab}\) of color \(p\), then \(Q_n\) has a long geodesic with at most
\[
\begin{cases}
r,&r\text{ even},\\
r-1+2[s\ne p],&r\text{ odd}
\end{cases}
\tag{14}
\]
switches.

*Proof.* Use the split realizing (9), with joining color \(p\), and replace the joining edge by the monochromatic square route. Duplicating its color preserves the switch count in (10). The result is a long geodesic of \(Q_n\). \(\square\)

In particular, a two-switch face path together with a monochromatic diagonal square route of either color gives \(\mu(c)\le2\). A three-switch face path rooted at \(x\) gives the same conclusion when the route color equals its initial color.

**Theorem 6 (constraints obtained from compressed induction).** Suppose the universal two-switch assertion holds in dimension \(n-1\), and \(c\) is an antipodally odd coloring of \(Q_n\) with \(\mu(c)\ge4\). For every opposing codimension-two face pair \(F,F^{ab}\), there is \(x\in F\) such that
\[
A(x)\ne C(x),\qquad B(x)\ne E(x),
\tag{15}
\]
and one of the following holds:
- \(F\) has a long two-switch geodesic rooted at \(x\);
- \(F\) has long three-switch geodesics rooted at \(x\) with both initial colors.

In the first case, if \(s\) is the initial color of the two-switch face path, then
\[
A(x)=B(x)=1+s,\qquad C(x)=E(x)=s.
\tag{16}
\]

*Proof.* Let \(M(x)\) be the set of colors of monochromatic diagonal routes in the exterior square. Equation (2) implies \(M(x^*)=1+M(x)\). Set \(S(x)=M(x)\) when this set is nonempty, and \(S(x)=\mathbb F_2\) otherwise. Every allowed color can be chosen from an original square edge; the antipodal selections give odd compressed cubes. Induction and Lemma 3 supply \(x\) with \(S(x)\subseteq H_2(d,x)\).

If \(M(x)\) were nonempty, choose \(p\in M(x)\subseteq H_2(d,x)\). A compressed two-switch path crossing there lifts along the monochromatic route without changing its switch count, contradicting \(\mu(c)\ge4\). Thus \(M(x)=\varnothing\), which is (15), and \(H_2(d,x)=\mathbb F_2\). Corollary 2 gives the asserted alternatives. A face path with at most one switch would extend by the two exterior directions to a full path with at most three switches; odd-change rotation would give \(\mu(c)\le2\). Hence the first alternative has two switches.

Finally, reverse that face path so it terminates at \(x\). Its final color remains \(s\), since its switch count is even. Appending either square route introduces at most two switches. If either route introduced fewer than two, a full path would have at most three and imply \(\mu(c)\le2\). Both new comparisons must therefore switch on both routes, giving (16). \(\square\)

The induction conclusion is a local certificate in an arbitrary face coloring, obtained by varying the antipodal selections. The remaining configurations in (15)–(16) specify where the two-edge lift can introduce its additional switches. Excluding those configurations globally, or finding a compressed witness whose square lift has at most three switches, would complete the proposed two-switch induction.
