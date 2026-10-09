# Dead-edge rigidity and extension constraints

# Dead-edge rigidity, monochromatic hubs, and facet lifting

Fix a binary coloring of ordered physical three-faces of Q_n. A physical cube edge is certified when some genuine monochromatic four-edge geodesic traverses it. Call an edge dead if no such geodesic exists. The following rigidity holds even without antipodal oddness.

## Rigidity around a dead edge

Let e={z,z xor e_i} be dead. The dead-edge rigidity theorem forces a color q for all ordered physical three-faces through either endpoint whose three free directions avoid i, independently of their ordering. Consequently, any directed path of length 3<=k<=min(n-1,6) through one endpoint that uses k distinct directions avoiding i is monochromatic whenever that endpoint occurs at a vertex position j satisfying k−3<=j<=3 (with the usual endpoint truncations). Indeed every consecutive three-face window along the path contains that vertex and has its free directions outside i, so each has color q. In particular for n>=7, arbitrary six-direction orders avoiding i can be rooted to pass through a dead-edge endpoint and yield genuine monochromatic six-edge geodesics.

This exhibits the tradeoff: failure of a local four-edge connector forces extensive monochromatic rigidity on transverse faces. The conclusion concerns actual physical faces; exterior bits are fixed by the chosen common hub.

## Facet-local amplification

Suppose n>=8 and e is dead. Let H be any coordinate 8-face containing e. The restriction of the coloring to H still has e dead: every four-edge witness in H would also be a witness in Q_n. Applying the established dimension-eight dead-edge polarity bootstrap inside H gives a full antipodal 8-geodesic with at most one window-color change. Its six windows are physical windows of the ambient coloring.

Order the remaining n−8 unused directions after this eight-edge path. The extension remains a full ambient geodesic and introduces at most n−8 additional windows, hence at most n−8 additional color changes. The resulting global switch count is at most 1+(n−8)=n−7. This is a conditional all-dimensional quantitative consequence of a single dead edge, rather than full one-switch closure.

The general hub-extension results further constrain how a collection of certified middle edges may be lifted across facets. Each extension must keep the actual fixed exterior coordinates and evaluate the new ordered windows; a local monochromatic hub need not persist as a globally monochromatic full path without this boundary control.

## Exact role in the global argument

Dead-edge rigidity and certified-edge density split the problem into two regimes: a dead edge yields transverse monochromatic paths and an eight-face good seed; the complementary live-edge regime supplies abundant certified local four-geodesics. The outstanding step is to synchronize these seeds or certificates across complementary supports with compatible root and terminal windows. The present theorems give physical local forcing and a global switch bound, while preserving the distinction between a long monochromatic partial path and a full antipodal one-switch geodesic.
