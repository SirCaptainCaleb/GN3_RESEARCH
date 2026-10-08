#  — preserved pre-item development

## Composition

(none yet)

## Development

Choose for every vertex \(v\) a maximum path
\[
P_v=(g_1,\ldots,g_p),\qquad p=\phi(v),
\]
with last vertex \(v\). Assign each ascending edge
\[
e=\{x,u,v\}
\]
to a terminal of smaller vertex rank, breaking ties arbitrarily. Thus, if \(e\) is assigned to \(v\),
\[
\phi(u)\ge\phi(v)=p. \tag{5}
\]

Except when \(e\) is the last edge of \(P_v\), every maximum \(p\)-edge path ending at \(v\) contains \(x\) or \(u\). Indeed, otherwise \(e\) can be appended after \(P_v\), contradicting maximality. Thus every assigned edge falls into one of the following three classes:
\[
\begin{array}{ll}
D:& x,u\in V(P_v),\\[2mm]
X:& x\in V(P_v),\ u\notin V(P_v),\\[2mm]
U:& u\in V(P_v),\ x\notin V(P_v).
\end{array}
\tag{6}
\]

The class \(D\) is controlled by double intersections with the chosen paths. The other two classes have more useful structure.
