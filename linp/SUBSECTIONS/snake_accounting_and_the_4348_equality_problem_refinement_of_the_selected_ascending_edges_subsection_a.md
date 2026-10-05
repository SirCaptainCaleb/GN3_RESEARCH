# snake_accounting_and_the_4348_equality_problem_refinement_of_the_selected_ascending_edges_subsection_a

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_refinement_of_the_selected_ascending_edges_subsection_a
- Parent Section: snake_accounting_and_the_4348_equality_problem_refinement_of_the_selected_ascending_edges
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

The identity also controls the intersections at the unique entrance and at the two terminals.

By (20), \(A-C=o(S)\). Hence, after deleting \(o(S)\) ascending edges, if
\[
e=\{x,u,v\}
\]
has unique entrance \(x\), the chosen maximum path ending at \(x\) contains neither \(u\) nor \(v\). Likewise \(D=o(S)\), and every maximum path chosen at a terminal of an ascending edge must contain at least one of the other two vertices; after deleting \(o(S)\) terminal incidences, it contains exactly one.

It remains to remove terminal incidences \((e,w)\) for which
\[
\phi(e)=\phi(w). \tag{31}
\]
Such an incidence makes \(w\) terminal at an ascending edge whose edge rank equals \(\phi(w)\). Hence
\[
q(w)=\phi(w).
\]
By (21), vertices with this equality have total vertex rank \(o(S)\). Corollary 2 gives
\[
t(w)\le \gamma(\phi(w))=O(\phi(w)),
\]
so the total number of incidences satisfying (31) is also \(o(S)\).

Consequently one may choose families \(G_v\subseteq T(v)\) such that
\[
\sum_v\left(\frac{\phi(v)}8-|G_v|\right)_+=o(S), \tag{32}
\]
and every edge \(e=\{x,u,v\}\in G_v\) satisfies

\[
V(P_x)\cap\{u,v\}=\varnothing, \tag{33}
\]
for the chosen maximum path \(P_x\) ending at its unique entrance, and
\[
|(e\setminus\{w\})\cap V(P_w)|=1 \tag{34}
\]
for each terminal \(w\in\{u,v\}\), together with
\[
\phi(e)<\min\{\phi(u),\phi(v)\}. \tag{35}
\]

The point of (32)–(35) is that they retain the \(1/8\)-scale family while removing the exceptional entrance and terminal incidences measured by the four terms of (13).
