# Equivalence of directed tuples and translation-invariant windows

## Metadata

- ID: translation_invariant_repair_and_the_tuple_conjecture_t_k
- Parent Section: higher_memory_norine_geodesics
- Position: 4
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


A full ordered cube-window coloring is translation-invariant when
\[
\chi(X_0\triangle S,\ldots,X_k\triangle S)
=
\chi(X_0,\ldots,X_k)
\]
for every \(S\subseteq V\).

For a geodesic segment with successive flipped coordinates
\[
v_1,\ldots,v_k,
\]
translation by \(X_0\) sends it to the canonical monotone segment beginning at \(\varnothing\). Hence every translation-invariant window coloring has a unique representation
\[
\chi(X_0,\ldots,X_k)=h(v_1,\ldots,v_k).
\]

Conversely every directed tuple coloring \(h\) defines such a translation-invariant window coloring.

Under complement-plus-reversal, the flip order reverses, so the cube antisymmetry condition is precisely
\[
h(v_k,\ldots,v_1)=1-h(v_1,\ldots,v_k).
\]

Thus the directed tuple Grand Conjecture \(N_k\) and the translation-invariant ordered-window formulation are the same problem. “Translation invariance” is not an added repair hypothesis relative to directed tuples; it is simply the cube-coordinate expression of the directed tuple model itself.

For \(r=2\), \(N_2\) follows from the Hamilton-path theorem for tournaments.


## Frontier

- Development version when composed: None
- Development version now: 3
