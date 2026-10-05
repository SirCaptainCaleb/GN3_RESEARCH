# Auxiliary-center fibers are exact inversion windows

## Metadata

- ID: auxiliary_center_fibers_are_exact_inversion_windows
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 11
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Auxiliary-center fibers are exact inversion windows

Fix a spanning order of the original tournament
\[
\rho=(v_1,\ldots,v_n)
\]
with status word
\[
\epsilon_1,\ldots,\epsilon_{n-2}.
\]
Let
\[
p=\min\{i:\epsilon_i=0\},\qquad
q=\max\{i:\epsilon_i=1\},
\]
with the usual conventions when one color is absent. For \(1\le j\le n-1\), let
\[
\pi_j=(v_1,\ldots,v_j,r,v_{j+1},\ldots,v_n)
\]
be the chamber obtained by inserting the auxiliary vertex \(r\) at cut \(j\).

This one-dimensional insertion family is the correct model for motion of \(r\) inside a non-singleton face block.

**Proposition (fiber formula).**
For the chamber \(\pi_j\):

1. there is no left violation if and only if \(j\le p+1\);
2. there is no right violation if and only if \(j\ge q\);
3. hence \(\pi_j\) is violation-free if and only if
   \[
   q\le j\le p+1.
   \]
   Such an insertion exists exactly when
   \[
   q\le p+1,
   \]
   which is the exact inversion-window criterion for a two-cover.

If \(q\ge p+2\), put
\[
\delta=q-p-1>0.
\]
For every cut in the interior inversion interval
\[
p+2\le j\le q-1,
\]
the nearest left and right violation radii are
\[
d_L(j)=j-p-1,\qquad
d_R(j)=q-j,
\]
and therefore
\[
\boxed{d_L(j)+d_R(j)=\delta.}
\]

**Proof.**
All original statuses strictly to the left of the inserted \(r\) survive unchanged up to position \(j-2\). Thus a left violation exists exactly when some zero occurs among \(\epsilon_1,\ldots,\epsilon_{j-2}\), equivalently \(p\le j-2\), i.e.
\[
j\ge p+2.
\]
This proves (1).

On the right, after the forced auxiliary junction, the original statuses \(\epsilon_{j+1},\ldots,\epsilon_{n-2}\) survive and are required to be \(0\). Hence a right violation exists exactly when some \(1\) occurs there, equivalently \(q\ge j+1\), i.e.
\[
j\le q-1.
\]
This proves (2), and (3) follows.

When both sides violate, the first zero at \(p\) is exactly \(j-p-1\) radius steps to the left of the auxiliary junction, while the last one at \(q\) is exactly \(q-j\) radius steps to the right. Their sum is
\[
(j-p-1)+(q-j)=q-p-1=\delta.
\]
\(\square\)

### Consequences

The large-radius moving-center phenomenon is now completely identified. Along one insertion fiber, moving \(r\) one step changes
\[
(d_L,d_R)\longmapsto(d_L+1,d_R-1)
\]
until one side disappears. The nearest-violation sign changes when the moving cut passes the midpoint of one **fixed** exact inversion window \([p,q]\). A double-nearest state is simply a midpoint of that interval.

Thus the example in [[moving_the_auxiliary_center_can_reverse_arbitrary_large_nearest_radii_without_same_face_escape]] is not an independent unbounded local obstruction. It is the one-dimensional geometry of the exact deficiency
\[
\delta=q-p-1.
\]

Equivalently:
\[
\boxed{
\text{quotienting pure motion of }r\text{ collapses the violation-radius data back to }(p,q).
}
\]

This explains why the exact violation map and the exact-root map behave differently only when actual original-vertex order changes. Along a pure \(r\)-motion fiber, the violation map is a resolved, cut-position-dependent encoding of the exact inversion root.

Strategically this removes one false target. There is no reason to repair arbitrarily large nearest radii created solely by moving \(r\). They should be collapsed or quotiented as insertion-fiber motion. The genuinely new data occur only when a Coxeter move changes the underlying original order, hence changes the exact inversion window itself. Those moves are local in the original status word and are the natural place to combine the exact-root structure with the positive-witness separator machinery.

The remaining closure problem may therefore be phrased as a fiberwise one:

> construct an antipodally compatible collapse of auxiliary insertion fibers to exact inversion-window data, and prove that the residual sign-changing cells—those in which the underlying original order changes—either admit the bounded center-preserving replacement at radius at most three or the fixed-position persistent-witness / outward-square alternative.

This is a sharper target than global reflected-double repair and isolates the moving-center pathology exactly.
