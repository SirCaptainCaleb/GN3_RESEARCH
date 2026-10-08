# Every minimal protected exchange has a root descent certificate after at most one codimension drop — preserved pre-item development

## Composition

(none yet)

## Development

## Every minimal protected exchange has a root descent certificate after at most one codimension drop

Let (h) be a reversal-odd binary label on ordered (r)-tuples. Work at a one-change deletion witness in a minimum coordinate counterexample chosen with first run (p) minimal, and consider the protected replacement bridge
[
B=b_1cdots b_r
]
from subsection 193.

For adjacent bridge windows (i,i+1), let (a_i) be the physical coordinate dropped and (c_i) the physical coordinate entering when the window slides one step to the right. Define the descent-root vector
[
R(B)
=
sum_{substack{1le i<r\ b_i=1, b_{i+1}=0}}
(e_{a_i}-e_{c_i})
in W_V.
]

### Noncancellation

In the protected replacement packet, the dropped coordinates are the (r-1) coordinates immediately to the left of the replacement position, while the entering coordinates are the (r-1) coordinates immediately to its right. These two sets are disjoint.

Therefore every coordinate occurring with positive coefficient in (R(B)) is distinct from every coordinate occurring with negative coefficient. Consequently
[
R(B)=0
quadLongleftrightarrowquad
B	ext{ contains no }10	ext{ descent}.
]

At a first-run-minimal witness, subsection 193 excludes every nontrivial monotone bridge (0^a1^{r-a}) with (a<r). Hence
[
R(B)=0
quadLongleftrightarrowquad
B=0^r.
]
Thus the zero set of the protected descent-root certificate is exactly the inert-exchange locus.

### Reversal equivariance

Under reversal of the full ordered configuration, the bridge transforms as
[
Blongmapsto overline{B^{m rev}}.
]
A descent (10) in (B) at adjacent windows (T_i,T_{i+1}) becomes a descent (10) between
[
T_{i+1}^{m rev},T_i^{m rev}.
]
The old entering coordinate becomes the new dropped coordinate and the old dropped coordinate becomes the new entering coordinate. Hence each root
[
e_{a_i}-e_{c_i}
]
is sent to its negative. Therefore
[
R(overline{B^{m rev}})=-R(B).
]

So (R) is a canonical odd root certificate on the noninert protected locus.

### Codimension-one repair of the zero locus

If (R(B)=0), then (B=0^r), so the protected exchange is inert. By subsection 195, the omitted coordinate (x) and replaced coordinate (y) become mutual blockers over a common codimension-two core.

Insert both consecutively in the order (x,y). Its local insertion packet has length (r), its final bit is forced to be (0), and counterexamplehood forces at least one of its first (r-1) bits to be (1). Hence that pair-insertion packet necessarily contains a (10) descent.

Applying the same descent-root construction to that pair packet gives a nonzero root certificate at codimension two. The same holds for the pair order (y,x).

### Strategic consequence

Every first-run-minimal protected exchange has a local root obstruction after at most one codimension drop:
1. a noninert replacement bridge has (R(B)
e0);
2. an inert replacement bridge has (R(B)=0), but canonically exposes a mutual-blocker pair whose full pair-insertion packet has a nonzero descent-root certificate.

This gives a two-level replacement for arbitrary signed-middle carrier extraction. The remaining topological problem is no longer to find a legal path inside an arbitrary permutohedron face. It is to package these level-1 and level-2 root certificates into one equivariant carrier on the protected deletion-fiber complex, with the codimension-two certificate filling the zero locus of the level-1 map.
