# Ordered windows remove the distinguished-pole restriction

## Metadata

- ID: ordered_windows_remove_the_distinguished_pole_restriction
- Parent Section: port_cube_geodesics_and_ordered_windows
- Position: 2
- Row version: 3
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition


Ordered local windows are read directly from the coordinate order of an antipodal geodesic, so arbitrary antipodal endpoints and arbitrary Boolean-rank oscillation are harmless. By contrast, a bare rank-oriented reading naturally handles the one-turn subfamily: \(+^*-^*\) passes through \(V\), and \(-^*+^*\) passes through \(\varnothing\). Local normalization depending on the current window can alter a global one-change word and therefore is not an innocent replacement for ordered windows.


## Development


Let an ordered \(r\)-window coloring depend on the ordered cube vertices
\[
(X_i,\ldots,X_{i+r}),
\]
or equivalently on the ordered list of its \(r\) distinct flipped coordinates together with any additional allowed local data.

Along an arbitrary antipodal geodesic, consecutive windows are read in the coordinate order supplied by the geodesic itself. No distinguished start pole is needed. In particular, for the GN3 subclass of \(N_4\),
\[
\chi(X_i,X_{i+1},X_{i+2},X_{i+3})=h(v_{i+1},v_{i+2},v_{i+3})
\]
reproduces the ordinary GN3 status word for every antipodal geodesic, regardless of its Boolean-rank profile.

The bare rank-oriented picture is different. If the up/down sign word of an antipodal geodesic changes direction at most once, then the path necessarily passes through one Boolean pole: \(+^*-^*\) passes through \(V\), while \(-^*+^*\) passes through \(\varnothing\). Its two arms then use complementary coordinate sets.

This yields a useful separation of models:

- ordered windows support arbitrary antipodal geodesics;
- bare rank-oriented local data naturally support only the one-turn pole-crossing subfamily unless additional structure is supplied.

The failed local XOR normalizations from the GN3 investigation illustrate the danger: a correction that varies from window to window can destroy a global one-change property even when it repairs local orientation.


## Frontier

- Development version when composed: 1
- Development version now: 2
