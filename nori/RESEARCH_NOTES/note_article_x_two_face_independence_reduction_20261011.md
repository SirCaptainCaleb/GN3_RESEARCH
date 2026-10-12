# Adjacent-face universality and simultaneous endpoint intersection

- Stable ID: note_article_x_two_face_independence_reduction_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_x_switch_induction
- Labels: reduction, obstruction, endpoint_geometry
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6298_1
- Updated session: session_nori_r6298_1
- Disposition: none
- Successor: none

## Related references

- article:nori_article_viii_edges, exact version 22
- article:nori_article_x_switch_induction, exact version 1

## Research note

# Adjacent codimension-two faces realize two independent arbitrary colorings

Let \(m\ge1\). For an arbitrary binary coloring \(d\) of the undirected edges of \(Q_m\), define
\[
E_t(d)=\{x\in Q_m:\text{some spanning geodesic ending at }x\text{ has at most }t\text{ color changes}\}.
\]
Reversing a spanning geodesic gives \(E_t(d)=\overline{E_t(d)}\).

**Proposition (two-face realization).** Fix exterior directions \(a,b\) of \(Q_{m+2}=Q_m\times Q_2\). Given arbitrary edge colorings \(d,e\) of \(Q_m\), there is an antipodally odd edge coloring \(c\) of \(Q_{m+2}\) whose restrictions to the interior edges of faces with exterior bits \(00,10\) are respectively \(d,e\). The terminal sets projected onto \(Q_m\) in exterior-bit order \(00,10,01,11\) are
\[
E_t(d),\ E_t(e),\ E_t(e),\ E_t(d).
\]
Consequently, for any *fixed* exterior coordinate pair, universal existence of adjacent codimension-two faces with corresponding terminals of spanning paths with at most \(t\) changes is equivalent to
\[
E_t(d)\cap E_t(e)\ne\varnothing\qquad
\text{for every pair of arbitrary edge colorings }d,e\text{ of }Q_m. \tag{1}
\]

*Proof.* For each interior edge direction \(i\), define
\[
\begin{aligned}
c_i(u,00)&=d_i(u),&c_i(u,10)&=e_i(u),\\
c_i(u,01)&=1-e_i(\bar u),&c_i(u,11)&=1-d_i(\bar u).
\end{aligned}
\]
These are well-defined undirected edge colors and satisfy \(c_i(\bar u,\bar z)=1-c_i(u,z)\). Choose \(j\) among the interior directions and color each \(a\)-edge and \(b\)-edge by \(u_j\). These colors are constant on each exterior-direction edge and flip upon antipodal complementation. Thus \(c\) is antipodally odd. Conversely, the displayed relations between opposite interior faces hold for any antipodally odd coloring. Applying global antipodality to a spanning path and reversing the resulting path preserves the projected terminal and the number of switches. Therefore opposite faces have identical projected endpoint sets, and adjacent faces have corresponding endpoints precisely when \(E_t(d)\cap E_t(e)\ne\varnothing\). \(\square\)

**Relaxed criterion.** Article VIII, Theorem 10, and the evenness of the minimum switch count among full antipodal geodesics show that corresponding endpoints of paths with at most \(2\) and at most \(3\) switches in adjacent faces (in either order) already imply \(\mu(c)\le2\): the theorem gives \(\mu(c)\le3\), and evenness gives \(\mu(c)\le2\). A sufficient arbitrary-pair condition for each fixed exterior pair is therefore
\[
E_2(d)\cap E_3(e)\ne\varnothing
\quad\text{or}\quad
E_3(d)\cap E_2(e)\ne\varnothing
\qquad\text{for all }d,e. \tag{2}
\]

**Consequence.** The ambient antipodal law places no restriction coupling the internal edges of adjacent codimension-two faces. A fixed-exterior-pair proof must establish a simultaneous arbitrary-coloring endpoint principle such as (1) or (2). A proof allowed to select the exterior directions may use compatibility across different choices instead. Neither (1) nor (2) is asserted here.
