# Direction-deleted port-cocircuit reassembly and root-phase duality

# Direction-deleted cocircuit reassembly and rooted phase duality

Let \(m\ge2\), and let \(D_{m+1}\) be the pointed matroid built from the antipodal line-graph cover of \(Q_{m+1}\). Write
\[
I(X)=\min\{|X\cap Y|:Y\in\mathcal C^*(D_{m+1}),\ p\in Y,\ |Y|=m+2\}
\tag{1}
\]
for every port-containing binary cycle \(X\). Every such \(X\) is the turn support of an antipodally odd coloring of the edges of \(Q_{m+1}\), together with the port; the full-geodesic switch minimum is \(I(X)-2\).

Fix one coordinate direction \(s\), identify its zero facet with \(Q_m\), and write \(x^*\) for the antipode within that facet. An arbitrary undirected-edge coloring \(d_i(x)\), \(i\in[m]\), and a function \(h:Q_m\to\mathbb F_2\) satisfying
\[
h(x^*)=1+h(x)
\tag{2}
\]
determine the following antipodally odd coloring of \(Q_{m+1}\):
\[
c_i(x,0)=d_i(x),\qquad
c_i(x,1)=1+d_i(x^*),\quad (i\in[m]),
\qquad c_s(x,z)=h(x).
\tag{3}
\]
Conversely, every antipodally odd cube-edge coloring has this description relative to the selected coordinate. Denote its port-containing cycle by \(X(d,h)\). Geometrically, the direction-deleted turn subgraph is \(L(Q_m)\), a connected subgraph on which the covering monodromy vanishes. The function \(h\) specifies the remaining joining-edge phases.

For each full \(d\)-geodesic \(R\) within \(Q_m\), write \(r(R)\) for its number of color changes and \(s(R)\) for the color of its initial edge.

**Theorem 1 (reassembly formula for minimum port intersections).** For every \(d,h\) satisfying (2),
\[
\boxed{\begin{aligned}
I(X(d,h))=2+\min_{x\in Q_m}\ \min_{R:x\to x^*}\ \Theta(R,h(x)),\\
\Theta(R,p)=
\begin{cases}
r(R),&r(R)\text{ even},\\
r(R)-1+2[s(R)\ne p],&r(R)\text{ odd}.
\end{cases}
\end{aligned}}
\tag{4}
\]
Here every \(R\) spans all \(m\) directions, and both minimizations run over finite sets. The formula is independent of the other joining-edge colors \(h(y)\).

*Proof.* Any full geodesic of \(Q_{m+1}\) traverses the joining direction \(s\) once. Reverse it if needed so this step goes from facet zero to facet one, crossing at the lower-facet vertex \(x\). Reverse the lower portion of the geodesic and reverse the within-facet antipodal image of its upper portion. These two paths concatenate into a full \(d\)-geodesic \(R:x\to x^*\), uniquely split as \(R=UV\). Conversely, any such \(R\), split at any of its vertices, gives a full geodesic of (3), with color word
\[
\operatorname{rev}(w(U)),\quad p,\quad
\overline{\operatorname{rev}(w(V))},
\qquad p=h(x).
\tag{5}
\]
All directions appear once. Thus optimizing over full geodesics is equivalent to optimizing the two seams in (5) over \(R\), its split, and its root \(x\).

Put \(r=r(R)\), \(s=s(R)\), and \(q\) equal to the final color of \(R\). We have \(q=s+(r\bmod2)\) over \(\mathbb F_2\). If the split is interior, write \(j=1\) when it cuts a color change of \(R\), and \(j=0\) otherwise. The number of changes in (5) is
\[
r-j+[s\ne p]+[1+q\ne p].
\tag{6}
\]
If \(r\) is positive and even, the two seam indicators sum to one. Splitting at one of the \(r\) changes attains cost \(r\). If \(r=0\), an endpoint split places all \(m\) facet edges on whichever side gives their constant color agreement with \(p\), attaining cost zero. If \(r\) is odd, the seam indicators are equal and sum to \(2[s\ne p]\); splitting at a change attains \(r-1+2[s\ne p]\). An endpoint split has cost \(r+[s\ne p]\), never smaller. These are the values of \(\Theta\). Finally, the intersection identity \(I=\mu+2\) proves (4). \(\square\)

For an arbitrary coloring \(d\), define its allowable joining phases at \(x\) by
\[
\mathscr H_2(d,x)=
\{p\in\mathbb F_2:\min_{R:x\to x^*}\Theta(R,p)\le2\}.
\tag{7}
\]

**Lemma 2 (phase duality and an antipodal selection principle).** For every arbitrary \(d\),
\[
\boxed{\mathscr H_2(d,x^*)=1+\mathscr H_2(d,x).}
\tag{8}
\]
Furthermore, the following are equivalent:

(i) Every joining phase function \(h\) satisfying (2) gives \(I(X(d,h))\le4\).

(ii) Some \(x\in Q_m\) has \(\mathscr H_2(d,x)=\mathbb F_2\).

*Proof.* Reverse a rooted full \(d\)-geodesic \(R:x\to x^*\). The reversal has the same switch count; its first color is \(s(R)\) for even \(r(R)\), and \(1+s(R)\) for odd \(r(R)\). In either case (4) shows that replacing the root by \(x^*\) and the joining phase \(p\) by \(1+p\) preserves \(\Theta\). This proves (8).

If (ii) holds, every \(h\) assigns at that \(x\) a phase admitted by (7), and (4) supplies a port-cocircuit intersection at most four. Conversely, if no \(x\) admits both phases, choose one representative of each antipodal pair \(\{x,x^*\}\), select \(h(x)\) outside \(\mathscr H_2(d,x)\), and set \(h(x^*)=1+h(x)\). Equation (8) guarantees that both choices lie outside their respective allowable sets. The resulting \(h\) is antipodally odd and (4) gives \(I(X(d,h))>4\), contradicting (i). \(\square\)

**Theorem 3 (rooted criterion for universal short port-cocircuit intersections).** The following assertions are equivalent for every \(m\ge2\):

(a) Every binary cycle \(X\) of \(D_{m+1}\) containing the port satisfies \(I(X)\le4\).

(b) For every arbitrary undirected-edge coloring \(d\) of \(Q_m\), some vertex \(x\in Q_m\) has one of these properties: there is a full \(d\)-geodesic rooted at \(x\) with at most two changes; or there are two full \(d\)-geodesics rooted at \(x\), each with three changes, whose initial edge colors differ.

*Proof.* Formula (4) gives \(\mathscr H_2(d,x)=\mathbb F_2\) whenever a rooted geodesic has zero or two changes. When a rooted geodesic has one change, its two choices of \(p\) give costs zero and two; both are also allowable. If all rooted geodesics have at least three changes, then only those with precisely three changes and matching initial and joining colors have \(\Theta\le2\). Consequently \(\mathscr H_2(d,x)=\mathbb F_2\) holds precisely under the alternatives in (b). Every admissible port cycle is \(X(d,h)\) for some lower-facet coloring and joining function. Apply Lemma 2 and quantify over \(d\). \(\square\)

**Corollary 4 (facet obstructions in a putative high-intersection cycle).** If \(X=X(d,h)\) satisfies \(I(X)\ge6\), then for every choice of the deleted direction and corresponding facet coloring \(d\):

1. No vertex of the facet starts a full \(d\)-geodesic with at most two changes.
2. Whenever a vertex \(x\) starts a full three-change \(d\)-geodesic, all such geodesics have the same initial color, necessarily \(1+h(x)\).
3. No vertex starts three-change \(d\)-geodesics with both initial colors.

*Proof.* If a path as in (1) existed, both joining phases at its root would produce an intersection at most four by (4). If a three-change path had initial color \(h(x)\), formula (4) would again produce an intersection four. Opposite initial phases among two such paths would include \(h(x)\), establishing (2)--(3). The deleted direction was arbitrary. \(\square\)

This characterization transfers the codimension-one reassembly theorem from Article X into the pointed matroid of Article XI. It couples a direction-deleted graphic restriction, an antipodally odd selection of joining phases, and minimum port-cocircuit intersections. The rooted criterion is unrestricted in the dimension, color dependence and choice of the deleted direction.
