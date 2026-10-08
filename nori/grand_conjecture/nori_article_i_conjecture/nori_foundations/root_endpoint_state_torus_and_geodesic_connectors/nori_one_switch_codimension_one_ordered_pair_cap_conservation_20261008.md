# NORI codimension-one one-switch facet geodesics conserve first and reversed-last ordered-pair cap colors

# Active NORI: codimension-one ONE-SWITCH facet cores preserve a canonical ordered-pair cap color

Let n>=5, fix a coordinate direction g and U=[n]\{g}, and fix any physical U-facet (its g-bit is fixed). Let x lie in that facet, y=x xor U, and let P be a directed U-spanning (n-1)-edge cube geodesic from x to y whose successive ordered-three-face colors have AT MOST ONE change. Write its order
  p=(p_1,...,p_(n-1))
and, when it has exactly one switch, its window word as q^s (1-q)^t with s,t>=1.

For each ordered pair (i,j) of distinct directions from U define the ACTUAL physical cap color
  A_(i,j)(x;g) := c(F(x;{g,i,j}),(g,i,j)).
This is a physical ordered face color, independent of the exterior g-facet bit of x. It generally DOES depend on x's bits outside {g,i,j} and must NOT be considered a globally coordinate-only quantity.

**THEOREM (codimension-one ordered-pair cap conservation).** If the ACTIVE NORI grand conjecture FAILS, every such good U-spanning facet geodesic has EXACTLY one color change (no monochromatic U-spanning facet path can exist), and its ordered-pair cap colors satisfy
   A_(p1,p2)(x;g) = A_(p_(n-1),p_(n-2))(x;g) = 1-q.
In particular the cap labels at the initial ordered two directions and the REVERSE of the terminal ordered two directions are EQUAL, and they both determine the first block color of P. If these cap values differ for any single good facet geodesic, grand NORI closure follows.

**Proof.**
1. If P is monochromatic, appending the missing g direction produces a full n-edge antipodal geodesic whose old n-3 ordered three-face windows have the same color and whose single new final window may differ; the full word changes at most once. Hence any P existing under no closure has exactly one change q→1-q, with both blocks nonempty.
2. Prepend the unused direction g to P. The full antipodal path begins with a NEW three-face window of color
  alpha=c(F(x;{g,p1,p2}),(g,p1,p2))=A_(p1,p2)(x;g),
followed by q^s (1-q)^t. If alpha=q, its total number of changes remains one, contradicting grand failure. Therefore alpha=1-q.
3. Append the unused direction g to P. The full antipodal path ends with a NEW window
  gamma=c(F(y;{p_(n-2),p_(n-1),g}),(p_(n-2),p_(n-1),g))
following q^s (1-q)^t. If gamma=1-q, the total number of changes is one, contrary to failure. Therefore gamma=q.
4. The faces F(y;{g,p_(n-2),p_(n-1)}) and F(x;{g,p_(n-2),p_(n-1)}) are global antipodal images: on every exterior coordinate in U\{p_(n-2),p_(n-1)} the vertices y and x differ, and the g-coordinate lies in the free set. The triples (p_(n-2),p_(n-1),g) and (g,p_(n-1),p_(n-2)) are reverse. Thus active NORI oddness gives
  gamma = 1 - A_(p_(n-1),p_(n-2))(x;g).
Since gamma=q, the final reversed cap equals 1-q=alpha. QED.

**Four-facet/physical facet coupling.** For fixed projected U-root x_U, there are two parallel g-facets. The cap A_(i,j)(x;g) is INDEPENDENT of the root's g-bit, because g is among the free face axes. Therefore one may make a graph on ordered distinct coordinate pairs (i,j)∈U² with an edge (p1,p2)--(p_(n-1),p_(n-2)) for EVERY GOOD U-spanning directed geodesic rooted at x in EITHER g-facet; under grand failure this entire combined graph has a canonical vertex two-coloring A, and EVERY such edge must be MONOCHROMATIC in A (its ends equal, rather than differ as for the older rank-(n-2) monochromatic core first–last graph). Any cross-cap edge with distinct A forces grand closure.

**Rooted polarity synchronization.** Suppose two good U-spanning paths P and Q have the SAME root projected onto U (possibly different g-facets), and the same first two directions, or one path's first ordered pair is the reverse of the other's last ordered pair. Under grand failure their FIRST block colors must coincide. This follows immediately from the displayed canonical A label. Consequently any pair with differing first block colors and either compatibility is already a full one-switch antipodal closure certificate.

**Limits.** The graph may be empty or partitioned into A-mono components; this theorem is a conditional extraction and synchronization tool. The grand question is to force a forbidden cap-mixing edge or odd signed cycle by coupling MANY good codimension-one facet paths, potentially using the known n-1 dimensional closure theorem inductively. No such forcing statement has been established. This result uses the actual physical ordered-face involution and does NOT treat NORI coloring as an edge-coloring.
