# Every isolated singleton has two curvature-free one-sided local resolutions — preserved pre-item development

## Every isolated singleton has two curvature-free one-sided local resolutions

Let five consecutive coordinates be
\[
(a,b,c,d,e)
\]
with ternary status word
\[
u,v,u,\qquad v=1-u.
\]
No flatness or curvature hypothesis is imposed.

### Left endpoint swap

Swap only the first pair:
\[
(b,a,c,d,e).
\]
Its three internal statuses are
\[
\alpha(b,a,c)=v,\qquad
z:=\alpha(a,c,d),\qquad
\alpha(c,d,e)=u.
\]
Since \(z\in\{u,v\}\), the word
\[
v,z,u
\]
has at most one change: it is either \(vvu\) or \(vuu\).

This move leaves the ordered right boundary pair \((d,e)\) unchanged. Hence every ambient ternary window on the right boundary and farther right is unchanged. All reconnection risk is exported to the left.

### Right endpoint swap

Swap only the last pair:
\[
(a,b,c,e,d).
\]
Its internal statuses are
\[
\alpha(a,b,c)=u,\qquad
z':=\alpha(b,c,e),\qquad
\alpha(c,e,d)=v.
\]
Again \(z'\in\{u,v\}\), so
\[
u,z',v
\]
is either \(uuv\) or \(uvv\), hence has at most one change.

This move leaves the ordered left boundary pair \((a,b)\) unchanged. Thus every ambient window on the left boundary and farther left is unchanged; all reconnection risk is exported to the right.

### Theorem

Every five-coordinate isolated-singleton packet admits two explicit one-sided local one-change resolutions, one preserving each chosen exterior side. This uses only reversal oddness of the ternary orientation and the binary status alphabet.

In particular, no flat/full classification, five-set holonomy, or coboundary identity is required to leave the isolated-singleton interior.

### Article III consequence

By §§241–242, every state supporting a first five-position equality/convex-zero event for the consecutive-change carrier is a global isolated-singleton witness. Apply either endpoint swap above toward a chosen protected side. The whole packet becomes locally one-change and the opposite ordered boundary pair is preserved exactly.

In the coboundary-flat transport branch, choose the one-change target determined by the preserved side and pass to its maximal threshold-compatible interval. The only remaining mismatches lie on the exported side. Repeated nearest-boundary flat repairs strictly enlarge the threshold band (§40); therefore they terminate in a spanning one-change order or at a fully-curved protected-root barrier.

Thus the first five-position carrier failure has no irreducible interior obstruction. Its only remaining content is the already-existing exported fully-curved boundary root.
