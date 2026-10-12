# Odd girth of the monochromatic component quotient and antipodal walk duality

Let \(n\ge3\), and retain the folded-cube line graph \(H=H_n=L(Q_n)/\langle\tau\rangle\), its antipodal monodromy \(\alpha\), and the admissible turn cochain \(d=a+\delta f\). For an edge set or closed walk \(W\) of \(H\), write
\[
w_d(W)=\sum_{\text{traversed turns }t} d(t)
\tag{1}
\]
with integer multiplicity. The parity identity is
\[
w_d(W)\equiv\alpha(W)\pmod2
\tag{2}
\]
for every closed walk \(W\).

Put
\[
H_0(d)=(V(H),\{t:d(t)=0\}).
\]
Let its connected components be \(K_1,\ldots,K_r\). Define the **monochromatic-component quotient** \(J_d\) by contracting every \(K_i\) to one vertex, retaining one edge for each turn \(t\) with \(d(t)=1\). Loops and parallel edges are permitted. Let \(g_{\rm odd}(J_d)\) denote the minimum length of an odd cycle of this multigraph, with a loop counted as a cycle of length one.

**Theorem 1 (odd-girth identity).** For every admissible antipodally odd coloring, in every dimension,
\[
\boxed{\displaystyle
g_{\rm odd}(J_d)=
\min_{\substack{C\subseteq H\text{ a simple cycle}\\
\alpha(C)=1}} w_d(C).}
\tag{3}
\]
In particular, \(J_d\) is nonbipartite and its odd girth is finite and odd.

*Proof.* If \(C\) is a simple cycle with \(\alpha(C)=1\), contract the portions of \(C\) lying in \(H_0(d)\). The result is a closed walk of \(J_d\) of length \(w_d(C)\), which is odd by (2). Any odd closed walk in a multigraph contains an odd cycle of length at most its length. Thus
\[
g_{\rm odd}(J_d)\le w_d(C).
\]

For the reverse inequality, take a shortest odd cycle \(Z\) of \(J_d\). Each of its edges arises from a turn of \(H\) with \(d=1\). At each intervening contracted vertex \(K_i\), join the endpoints of consecutive turns by a path of zero-turn edges inside \(K_i\). This produces a closed walk \(W\) of \(H\) satisfying \(w_d(W)=|Z|\). By (2), \(\alpha(W)=1\). Splitting \(W\) at repeated vertices, and discarding any immediate backtracking, decomposes it into closed subwalks of total weight at most \(|Z|\), at least one of which has nonzero monodromy. Repeating this splitting yields a simple cycle \(C\) with \(\alpha(C)=1\) and \(w_d(C)\le|Z|\). The two inequalities prove (3). The monodromy class is nonzero because an antipodal-geodesic turn cycle has monodromy one, so some such cycle exists; therefore \(J_d\) is not bipartite. \(\square\)

Let \(\mu_{\rm path}(c)\) denote the minimum number of color changes among **arbitrary** paths of \(Q_n\) joining a vertex to its antipode, with no geodesicity requirement. Repeated vertices or edges may be allowed during an intermediate walk: removing a closed detour cannot increase the number of changes of a binary color word, by the triangle inequality for the discrete metric on \(\{0,1\}\).

**Theorem 2 (full antipodal-path duality).** For every antipodally odd coloring,
\[
\boxed{\displaystyle
\mu_{\rm path}(c)=g_{\rm odd}(J_d)-1.}
\tag{4}
\]
In particular, the minimum number of switches on an unrestricted antipodal path is even.

*Proof.* Let \(C\) attain the minimum in (3), with odd weight \(w=w_d(C)\). Lift its cyclic turn sequence to a sequence \(e_1,\ldots,e_m,e_{m+1}=\tau e_1\) of cube edges. If at some cube edge the contact vertices with its predecessor and successor coincide, remove that stationary edge from the turn sequence, replacing two turns in one vertex star by the third side of the corresponding star triangle. The triangle inequality
\[
(c(e_-)\oplus c(e))+(c(e)\oplus c(e_+))
\ge c(e_-)\oplus c(e_+)
\]
shows that each removal does not increase turn weight, and the star triangle has zero monodromy. As established by the stationary-contact contraction theorem earlier in Article XI, repetition ends with a cyclic sequence whose contacts traverse a cube-edge walk from a vertex to its antipode. Its new cyclic turn weight \(w'\) is odd and at most \(w\).

The cyclic sequence of edge colors is antipodally complementary after one traversal. By moving the cut in this cyclic sequence, each comparison in its cyclic turn count can be chosen as the terminal seam of an antipodal walk. As \(w'\) is positive and odd, some turn has weight one. Choosing that turn as the seam yields an antipodal walk with \(w'-1\le w-1\) changes. Erasing self-intersections does not increase the switch count. Thus \(\mu_{\rm path}(c)\le g_{\rm odd}(J_d)-1\).

Conversely, let \(P\) be an antipodal cube-edge path with \(k\) switches. Follow its edge sequence in \(L(Q_n)\). Its last edge is incident with the antipode of the initial vertex, as is the antipode of its first edge; adjoining the latter creates a closed turn walk in \(H\) with monodromy one. If the last edge is already the antipode of the first, no additional turn is needed. The resulting walk has at most \(k+1\) turns of weight one: the original \(k\) switches, plus possibly the terminal seam. Applying the first part of Theorem 1 to this closed walk gives \(g_{\rm odd}(J_d)\le k+1\). Taking a minimizing path proves the reverse inequality. Equation (4) follows; parity of the odd girth makes the minimum even. \(\square\)

**Corollary 3 (monochromatic antipodal paths as quotient loops).** The following statements are equivalent:
1. \(J_d\) has a loop;
2. \(\mu_{\rm path}(c)=0\);
3. some connected monochromatic cube-edge component contains a vertex and its antipode;
4. for some monochromatic cube-edge component \(A\), the vertex sets of \(A\) and its antipodal image \(\tau A\) intersect.

Thus the original, nongeodesic Norine antipodal monochromatic-path statement is equivalent to the assertion that every admissible coloring has a loop in its monochromatic-component quotient. Wu and Yang proved that statement in 2026; the geodesic strengthening remains open.

*Proof.* A loop means \(g_{\rm odd}(J_d)=1\), which is equivalent to (2) by Theorem 2. A monochromatic path between antipodal vertices lies within one monochromatic edge-component, proving equivalence of (2) and (3). Finally, if \(v\in A\cap\tau A\), then both \(v\) and \(\tau v\) lie in \(A\), and conversely any antipodal vertex pair lying in \(A\) yields such an intersection. \(\square\)

Let \(\mu_{\rm geo}(c)\) be the minimum number of switches among full antipodal *geodesics*. By the pointed-matroid theorem of the preceding Subsection,
\[
\mu_{\rm geo}(c)=
\min_{\substack{Y\in\mathcal C^*(D_n)\\
p\in Y,\ |Y|=n+1}} |X_d\cap Y|-2.
\tag{5}
\]

**Corollary 4 (geodesicity penalty).** The difference
\[
\boxed{\displaystyle
\Gamma(c)=\mu_{\rm geo}(c)-\mu_{\rm path}(c)
=\min_{\substack{\alpha(C)=1\\|C|=n}}w_d(C)
-\min_{\alpha(C)=1}w_d(C)
}
\tag{6}
\]
is a nonnegative even integer. An unrestricted two-switch counterexample, if one exists, must exhibit one of two phenomena: either \(g_{\rm odd}(J_d)\ge5\), which would also violate the unrestricted nongeodesic two-switch bound, or \(g_{\rm odd}(J_d)\le3\) but \(\Gamma(c)\ge2\). In the latter case, every low-weight odd-monodromy cycle of weight at most three has positive repeated-coordinate excess \(q(C)\ge1\), by the preceding stationary-contact contraction theorem.

*Proof.* The equality follows from Theorem 2 and the cyclic turn formula (5), and parity gives evenness. If the minimum among length-\(n\) odd cycles is at least five, then either the unrestricted odd girth is at least five or there is an odd cycle of weight at most three. Such a cycle cannot have \(q(C)=0\), since the stationary-contact contraction theorem would then produce a length-\(n\) odd cycle of no greater weight, contradicting the assumed geodesic minimum. \(\square\)

Theorem 2 identifies the shortest odd-cycle problem in the pointed binary matroid with the classical unrestricted antipodal-path problem. Equation (6) isolates the additional geodesicity difficulty as a measurable, even-valued defect. In particular, general matroid circuit-cocircuit principles can guarantee small intersections for unrestricted port cocircuits only insofar as they address the nongeodesic problem; the fixed length condition \(|Y|=n+1\) demands further cube geometry. The component-quotient reduction is valid without assuming any degree balance, sparse curvature, or special coloring structure.

**Theorem 5 (maximum-cut extraction of a dual-circuit core).** Let \(D=\operatorname{supp}(d)\), and let \(J=J_d\) be its connected component quotient, retaining loops. Write \(\operatorname{mc}(J)\) for its maximum cut cardinality, with multiplicities. Among admissible cochains \(d'=d+\delta g\) satisfying \(\operatorname{supp}(d')\subseteq D\),
\[
\boxed{\min |\operatorname{supp}(d')|=|D|-\operatorname{mc}(J).}\tag{7}
\]
Every minimizer has connected zero-turn graph \(H_0(d')\); in particular \(X_{d'}=\operatorname{supp}(d')\cup\{p\}\) is a circuit of the pointed dual matroid. If \(S\) is any maximum cut of \(J\), and \(b_S\) its pullback to \(H\), then
\[
\boxed{\operatorname{supp}(d)=\operatorname{supp}(d')\ \dot\cup\ \operatorname{supp}(b_S)}
\tag{8}
\]
for \(d'=d+b_S\) over \(\mathbb F_2\), and every closed walk \(W\) satisfies
\[
\boxed{w_d(W)=w_{d'}(W)+|\operatorname{supp}(b_S)\cap W|,\quad
|\operatorname{supp}(b_S)\cap W|\equiv0\pmod2.}\tag{9}
\]

*Proof.* The support inclusion \( \operatorname{supp}(d+\delta g)\subseteq D\) holds if and only if \(\delta g\) vanishes on every zero-turn edge. Thus \(g\) is constant on each connected component of \(H_0(d)\), and induces a vertex bipartition of \(J\). Precisely the edges crossing that bipartition are deleted from \(D\). This proves (7) and (8).

We claim that the crossing-edge subgraph of every maximum cut in a connected multigraph \(J\) is connected and spans \(V(J)\). Otherwise take one connected component \(U\) of this crossing-edge subgraph. Every edge between \(U\) and its complement is noncrossing, and at least one exists because \(J\) is connected. Reversing the bipartition on all vertices of \(U\) preserves its previously crossing edges and makes each edge from \(U\) to its complement crossing, increasing the cut size. This is impossible. When \(J\) has one vertex the claim is immediate. Consequently, \(H_0(d')\) contains all original zero-turn components and the edges of a connected spanning crossing subgraph, so it is connected. The dual-circuit connectivity theorem identifies \(X_{d'}\) as a dual circuit. Disjointness in (8) gives the weight identity in (9), and cut-cycle orthogonality gives its evenness. \(\square\)

**Proposition 6 (minimal odd-cycle transversals).** For an admissible turn cochain \(d\) on \(H\), the following are equivalent:

(i) \(X_d=D\cup\{p\}\) is a circuit of the pointed dual;

(ii) \(H_0(d)\) is connected;

(iii) \(D\) is an inclusion-minimal edge set meeting every monodromy-one simple cycle of \(H\);

(iv) each turn \(e\in D\) has a monodromy-one simple-cycle witness \(C_e\) satisfying \(C_e\cap D=\{e\}\).

*Proof.* The dual-circuit criterion gives (i) if and only if (ii). If (ii) holds, join the endpoints of any \(e\in D\) by a simple zero-turn path. Adding \(e\) gives a simple cycle of weight one, hence odd monodromy. This proves (iv), which implies (iii) because each \(C_e\) loses its sole intersection when \(e\) is removed.

If (ii) fails, connectivity of \(H\) supplies \(e\in D\) connecting different zero-turn components. A monodromy-one cycle containing \(e\) cannot contain only one edge of \(D\), since the other edges would then connect the distinct zero-turn components. By parity, it contains at least three edges of \(D\). Thus removing \(e\) from \(D\) leaves every monodromy-one cycle intersected, contradicting (iii). Therefore (iii) implies (ii). \(\square\)

The maximum-cut representative is a minimum-cardinality signature among representatives whose support is contained in \(D\). The decomposition (9) exhibits the nonnegative even crossing penalty on every geodesic cycle. Controlling this penalty simultaneously with the core circuit intersection remains necessary for a universal two-switch proof.

**Corollary 7 (Wu–Yang's theorem gives an unconditional two-intersection cocircuit).** The theorem of Hehui Wu and Ningyuan Yang, *A Chain-Level Borsuk--Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture*, arXiv:2607.19276 (July 2026), states that every antipodally odd edge coloring of \(Q_n\), \(n\ge2\), has a monochromatic antipodal path, without a geodesicity requirement. Combining that theorem with Theorems 1 and 2 gives, for every \(n\ge3\) and every admissible turn signature \(d\),
\[
\boxed{g_{\rm odd}(J_d)=1,\qquad \mu_{\rm path}(c)=0.}\tag{10}
\]
Equivalently, every \(H_0(d)\) has a connected component containing both endpoints of some turn with \(d=1\). In the pointed binary dual matroid \(D_n\),
\[
\boxed{\displaystyle
\forall X\in Z(D_n)\ (p\in X),\quad
\exists Y\in\mathcal C^*(D_n)\ (p\in Y):
\ |X\cap Y|=2.}
\tag{11}
\]
There is no bound on \(|Y|\) in (11). The two-switch *geodesic* conjecture is the strengthening that requires \(|Y|=n+1\) and allows the intersection to be at most four.

*Proof.* Apply the Wu--Yang monochromatic antipodal-path theorem, so \(\mu_{\rm path}(c)=0\). Equation (4) gives \(g_{\rm odd}(J_d)=1\). A loop in \(J_d\) is a turn \(e\) with \(d(e)=1\) whose endpoints are joined by a zero-turn path in \(H_0(d)\). Their union contains a simple monodromy-one cycle \(C\) with \(w_d(C)=1\). Theorem 1 of the preceding pointed-lift Subsection makes \(C\cup\{p\}\) a cocircuit \(Y\) of \(D_n\), and its intersection with \(X_d\) has cardinality \(1+w_d(C)=2\). Every port-containing dual cycle equals \(X_d\) for some admissible signature, so the quantifiers follow. \(\square\)

**Corollary 8 (only geodesicity can obstruct the conjecture).** For every admissible coloring,
\[
\boxed{\Gamma(c)=\mu_{\rm geo}(c),}
\tag{12}
\]
and an obstruction to \(\mu_{\rm geo}(c)\le2\), if one exists, must force every monodromy-one turn cycle of weight one to have positive repeated-direction excess \(q(C)\), or it would contract to a length-\(n\) geodesic turn cycle of weight one. More generally, every odd-monodromy cycle of weight at most three in such an obstruction must have \(q(C)\ge1\). These are unrestricted necessary conditions, and the existence of the weight-one cycles is unconditional by Wu--Yang.

The topological theorem in the cited paper does not constrain the lengths of its monochromatic paths. Consequently (11) does not imply the desired minimum-size cocircuit intersection; that restriction is the remaining issue of Article XI.
