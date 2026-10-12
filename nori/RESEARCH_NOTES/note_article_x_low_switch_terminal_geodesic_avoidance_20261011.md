# Low-switch terminal sets need not meet antipodal geodesics

- Stable ID: note_article_x_low_switch_terminal_geodesic_avoidance_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_x_switch_induction
- Labels: obstruction, endpoint_geometry, construction
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6298_1
- Updated session: session_nori_r6298_1
- Disposition: none
- Successor: none

## Related references

- article:nori_article_x_switch_induction, exact version 1

## Research note

# A low-switch terminal set can avoid an antipodal geodesic

For an arbitrary undirected-edge coloring \(d\) of \(Q_m\), let \(E_t(d)\) be the set of terminals of spanning geodesics with at most \(t\) color changes.

**Proposition.** For every integer \(t\ge0\) and every \(m\ge2(t+2)\), some edge coloring \(d\) of \(Q_m\) has a spanning antipodal geodesic \(R\) such that
\[
V(R)\cap E_t(d)=\varnothing. \tag{1}
\]

*Proof.* Put \(\ell=t+2\), and partition the coordinate set into disjoint blocks \(A,B,C\), where \(|A|=|B|=\ell\) and \(C\) contains the remaining \(m-2\ell\) coordinates. For \(i\in A\) set
\[
d_i(x)=\bigoplus_{j\in A\setminus\{i\}}x_j,
\]
and for \(i\in B\) use the analogous formula with \(B\). Color each direction in \(C\) constantly zero. The color of an edge is independent of the bit in its own direction, hence this defines an undirected-edge coloring.

Consider a vertex \(x\) whose bits on \(A\) are all zero. In every spanning geodesic starting at \(x\), take the subsequence consisting of its \(\ell\) edges in directions from \(A\). These edges have color word \(0,1,0,1,\ldots\), because just before the \(k\)-th direction of \(A\) is flipped, precisely \(k-1\) other \(A\)-bits are one. Thus this subsequence has \(\ell-1=t+1\) color changes. The same conclusion holds when \(x|_A=1^\ell\): the colors alternate in reverse parity order. It also holds, by symmetry, when \(x|_B\) is either constant word. Deleting symbols from a binary color word cannot increase its number of changes. Therefore every spanning geodesic starting at such an \(x\) has at least \(t+1\) changes. Reversal gives the identical assertion for spanning geodesics ending at \(x\), so \(x\notin E_t(d)\).

Now take the spanning geodesic \(R\) beginning at \(0^m\) and flipping first all coordinates in \(A\), then all in \(B\), then all in \(C\). Until the \(B\)-phase begins, the \(B\)-bits are all zero; thereafter, the \(A\)-bits are all one. Every vertex of \(R\) therefore has a constant \(A\)-block or \(B\)-block, so every vertex lies outside \(E_t(d)\). \(\square\)

**Scope.** Although \(E_t(d)\) is invariant under complementation (by path reversal), it need not intersect every spanning antipodal geodesic. This rules out any endpoint-coincidence argument that assumes such geodesic-blocking merely from being a low-switch terminal set. It does not rule out intersection between \(E_2(d)\) and \(E_3(e)\) for two arbitrary colorings, nor the possibility of choosing another pair of exterior directions in the ambient NORI1 cube.

**Strengthening to antipodally odd colorings.** The same avoidance phenomenon occurs within NORI1. Fix any \(t\ge0\), let \(\ell\) be an even integer satisfying \(\ell\ge t+2\), and take \(m\ge2\ell\). Keep the displayed formulas on \(A\) and \(B\), and, when \(C\ne\varnothing\), color each \(i\in C\) edge by \(x_{a_0}\) for one fixed \(a_0\in A\). The colors are independent of each edge's own coordinate. Since \(\ell-1\) is odd, complementing all bits flips each internal \(A\)- and \(B\)-edge color; it also flips each \(C\)-edge color. Hence \(d\) is antipodally odd, and the same geodesic \(R\) avoids \(E_t(d)\). In particular, for \(t=2\) and \(m\ge8\), an antipodally odd coloring of \(Q_m\) has a spanning antipodal geodesic containing no terminal of any spanning geodesic with at most two switches.
