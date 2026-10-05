# Two-tail split routing is an exact Hall problem

## Metadata

- ID: two_tail_split_routing_is_an_exact_hall_problem
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 46
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Split routing of the two hole labels is an exact Hall problem

Let \(X=\{x,y\}\) be a minimum deletion pair and fix
\[
H-X=P\mid Q,
\]
with terminal pieces
\[
(\ldots,u,a,b)=P,\qquad (\ldots,v,d,c)=Q.
\]
Put
\[
P^-=(p_1,\ldots,u,a),\qquad Q^-=(q_1,\ldots,v,d).
\]

For a hole label \(z\in\{x,y\}\), say that \(z\) is **P-attachable** when
\[
h(u,a,z)=1,\qquad h(a,z,b)=1,
\]
so that
\[
P^-,z,b
\]
is tight. Likewise say that \(z\) is **Q-attachable** when
\[
h(v,d,z)=1,\qquad h(d,z,c)=1,
\]
so that
\[
Q^-,z,c
\]
is tight.

Form the bipartite graph with left class \(\{x,y\}\), right class \(\{P,Q\}\), and these attachment edges.

If this graph has a perfect matching, say \(x\) is P-attachable and \(y\) is Q-attachable, then
\[
(p_1,\ldots,u,a,x,b)
\qquad\text{and}\qquad
(q_1,\ldots,v,d,y,c)
\]
are disjoint tight paths covering every vertex of \(H\). Thus \(H\) has a spanning two-cover. The swapped matching is identical.

Therefore every genuine deletion-distance-two obstruction has a Hall failure. Since both sides have order two, one of the following holds:

1. **blocked tail:** one of \(P,Q\) accepts neither \(x\) nor \(y\);
2. **blocked hole:** one of \(x,y\) is accepted by neither \(P\) nor \(Q\).

Each missing attachment has an explicit two-triple reason. For example failure of P-attachment of \(z\) means
\[
h(u,a,z)=0
\quad\text{or}\quad
h(a,z,b)=0,
\]
equivalently by boundary antisymmetry
\[
h(z,a,u)=1
\quad\text{or}\quad
h(b,z,a)=1.
\]
Thus a blocked P-tail assigns to each hole one of two concrete reverse-junction types across the adjacent anchor layers \((u,a,b)\); the Q-side has the mirror pair
\[
h(z,d,v)=1
\quad\text{or}\quad
h(c,z,d)=1.
\]

Minimum-hole synchronization already fixes
\[
h(z,b,a)=1,\qquad h(z,c,d)=1
\]
for both \(z=x,y\). Hence Hall failure does not leave an arbitrary four-label routing residue: it leaves one of finitely many adjacent reverse-junction patterns superimposed on the forced first-edge reversals.

This is the exact split-routing specialization of the older two-extender Hall calculus. It sits strictly between the general four-middle-label routing formulation and the stronger one-sided six-path criterion.
