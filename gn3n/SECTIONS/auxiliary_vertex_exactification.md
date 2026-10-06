# Auxiliary-vertex exactification

**Summary:** Adding one special vertex turns the stronger-looking one-change target into an exact reformulation of the two-cover conjecture.

## Statement

After adjoining a vertex r with h(u,v,r)=1 for all distinct u,v, directed one-change spanning orders in the extension are in two-to-one correspondence with two-covers of the original tournament. The switch is automatically forced adjacent to r, and the resulting geodesic target is exactly equivalent to the grand conjecture.

## Composition

## The exact one-change extension

Let \(H\) have nonempty vertex set \(V\). Adjoin \(r\), retain all triples of \(H\), and impose
\[
h(u,v,r)=1,\qquad h(r,v,u)=0
\]
for distinct \(u,v\in V\). The values \(h(u,r,v)\) may be chosen arbitrarily subject only to boundary reversal.

Every spanning order of the extension is uniquely
\[
(L,r,R).
\]
If its status word has the directed form \(1^a0^b\), then \(L\) is a tight path: whenever \(|L|\ge2\), its last two vertices followed by \(r\) form a tight triple, so every earlier triple lies in the initial tight run. Likewise \(R^{\rm rev}\) is a tight path because a triple beginning at \(r\) is non-tight, forcing the entire right side into the non-tight run. Deleting \(r\) therefore produces the two-cover
\[
L\mid R^{\rm rev}.
\]

Conversely, from a two-cover \(P\mid Q\), the orders
\[
(P,r,Q^{\rm rev})\qquad\text{and}\qquad(Q,r,P^{\rm rev})
\]
both have status word \(1^a0^b\). The possible triple with \(r\) in the middle can have either status without destroying the one-change form. These two orders are reverses, and no other cover maps to either order.

Hence directed one-change spanning orders of \(H^+\) map two-to-one onto two-covers of \(H\), independently of the local tournament at \(r\).

## The switch and common endpoint normalize to r

The extension does more than create a correspondence: it normalizes the geometry.

For nonempty \(P,Q\), let \(p=|P|\) and
\[
\epsilon=h(\operatorname{last}(P),r,\operatorname{last}(Q)).
\]
In the order \((P,r,Q^{\rm rev})\), the number of initial tight triple positions is
\[
a=p-1+\epsilon.
\]
Thus the ordinary edge straddling the change contains \(r\). The switch location is forced by the extension.

Likewise, every tight path containing \(r\) has at most one vertex after \(r\), because any triple beginning at \(r\) is non-tight. Therefore any pair of tight paths sharing an oppositely directed terminal edge and covering \(V\cup\{r\}\) must share an edge containing \(r\). Under the endpoint-moving involution, exactly one of its two common-terminal states ends at \(r\). Removing \(r\) from that normalized state gives a two-cover of \(H\).

So neither the switch position nor the common endpoint needs to be found by a separate search once the extension is made.

## Exact positive factorization

Let
\[
F_H=\sum_{P\text{ nonempty tight in }H}x_{V(P)}
\]
in the square-zero algebra, with path orders counted separately. For \(S\subseteq V\), let \(m_r(S)\) be the number of orders of \(S\cup\{r\}\) having directed one-change word \(1^a0^b\). Applying the exact extension to every induced subtournament yields
\[
\boxed{\sum_{S\subseteq V}m_r(S)x_S=(1+F_H)^2.}
\]
The constant term is the singleton order \(r\); \(2F_H\) corresponds to a single path placed on either side of \(r\); and \(F_H^2\) corresponds to two disjoint nonempty paths on opposite sides. There is no cancellation.

In particular,
\[
m_r(V)=2[x_V]\left(F_H+\frac12F_H^2\right).
\]
The left side is positive exactly when \(H\) has a one- or two-path cover. The factorization therefore identifies the count exactly, although it does not itself prove positivity.

## The exact geodesic form of the grand conjecture

Apply the \(\Gamma\)-construction to \(H^+\) and keep only the copy \(\sigma=1\). Its pole geodesics have color words
\[
1,\ h(w_1,w_2,w_3),\ldots,h(w_{n-1},w_n,w_{n+1}),\ 0.
\]
Such a word changes color exactly once if and only if its internal word has directed form \(1^a0^b\).

Therefore the grand two-cover conjecture is equivalent to the following single-copy antipodal-geodesic statement:

> For every boundary tournament \(H\), after adjoining \(r\) with \(h(u,v,r)=1\), the \(\sigma=1\) memory-lift graph of \(H^+\) contains a one-change geodesic from its distinguished source pole to its distinguished target pole.

The local tournament at \(r\) may be chosen arbitrarily, for example transitively. This is the key exactification: topology is no longer being asked to prove the potentially stronger one-change assertion on \(H\) itself.

## Metadata

- ID: auxiliary_vertex_exactification
- Kind: section
- Version: 12
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False
- Subsections existing when composed: 4
- Subsections now: 4

## Development tree

- [Subsection 1 — The exact one-change extension](../SUBSECTIONS/auxiliary_vertex_exactification_subsection_a.md) (`auxiliary_vertex_exactification_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — The switch and common endpoint normalize to r](../SUBSECTIONS/auxiliary_vertex_exactification_subsection_b.md) (`auxiliary_vertex_exactification_subsection_b`; development v4; composition v1; stale=False)
- [Subsection 3 — Exact positive factorization](../SUBSECTIONS/auxiliary_vertex_exactification_subsection_c.md) (`auxiliary_vertex_exactification_subsection_c`; development v4; composition v1; stale=False)
- [Subsection 4 — The exact geodesic form of the grand conjecture](../SUBSECTIONS/auxiliary_vertex_exactification_subsection_d.md) (`auxiliary_vertex_exactification_subsection_d`; development v3; composition vNone; stale=False)
