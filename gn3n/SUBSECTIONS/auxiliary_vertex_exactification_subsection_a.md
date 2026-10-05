# The exact one-change extension

## Metadata

- ID: auxiliary_vertex_exactification_subsection_a
- Parent Section: auxiliary_vertex_exactification
- Position: 1
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

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

## Development

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
