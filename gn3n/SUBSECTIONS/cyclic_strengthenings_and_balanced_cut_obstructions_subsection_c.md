# The exact cyclic defect-graph formulation

## Metadata

- ID: cyclic_strengthenings_and_balanced_cut_obstructions_subsection_c
- Parent Section: cyclic_strengthenings_and_balanced_cut_obstructions
- Position: 3
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

For an oriented Hamilton cycle \(Z=(v_1,\ldots,v_n,v_1)\), let \(e_i=\{v_i,v_{i+1}\}\). Define the blue-transition defect graph \(D_Z\) on the cycle-edge positions \(e_i\) by adding \(\{e_{i-1},e_i\}\) exactly when \((v_{i-1},v_i,v_{i+1})\) is non-tight.

Cutting a nonempty set \(S\) of cycle edges leaves \(|S|\) inherited path components. Every resulting component is tight exactly when \(S\) meets every edge of \(D_Z\), i.e. exactly when \(S\) is a vertex cover of \(D_Z\). Hence
\[
\operatorname{pc}(H)
=
\min_Z \max\{1,\tau(D_Z)\}.
\]
In particular,
\[
\operatorname{pc}(H)\le2
\iff
\text{some cyclic order }Z\text{ has }\tau(D_Z)\le2.
\]

This is the correct cyclic reformulation. It allows several separated blue runs provided two cut positions hit them all, which is exactly the information lost by counting monochromatic components alone.
