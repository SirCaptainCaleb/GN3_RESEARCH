# Cochain viewpoint on color changes

## Metadata

- ID: cochain_viewpoint_on_color_changes
- Parent Section: port_cube_geodesics_and_ordered_windows
- Position: 3
- Row version: 3
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition


The ordinary edge problem and ordered-window NOR can be viewed as a degree-shifted pair: colors are local data on directed windows, while color changes compare adjacent overlapping windows. The one-change target asks that this change process have support of size at most one along some antipodal geodesic. In the GN3 \(k=3\) subclass the local datum is additionally translation-invariant in the Boolean base set.


## Development


The Article VII notes also identified a useful degree-shifted analogy.

For an ordinary edge coloring of the cube, regard the binary color as a degree-one local datum. Along a path, the change indicator between consecutive edge colors is the corresponding discrete coboundary-type quantity.

For an ordered \(r\)-tuple coloring, the local datum lives on length-\(r\) directed windows. Consecutive windows overlap in \(r-1\) edges, and the switch indicator compares the two adjacent window values. Thus the one-change problem can be viewed as controlling the support of a one-step coboundary of the ordered-window coloring along a geodesic.

In the GN3 \(r=3\) subclass this specializes to a translation-invariant rank-three local datum
\[
\alpha(S;u,v,w)=\alpha(u,v,w),
\]
and the change between adjacent triple windows compares
\[
\alpha(u,v,w),\qquad \alpha(v,w,z).
\]

The point is conceptual rather than formal cohomology: the ordinary Norine edge problem and higher-window NOR problems differ in the degree of the local datum, while the target remains sparse support of its change process along an antipodal geodesic.


## Frontier

- Development version when composed: 1
- Development version now: 2
