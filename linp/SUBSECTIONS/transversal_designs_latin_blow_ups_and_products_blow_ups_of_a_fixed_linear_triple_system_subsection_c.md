# Corollary 4

## Metadata

- ID: transversal_designs_latin_blow_ups_and_products_blow_ups_of_a_fixed_linear_triple_system_subsection_c
- Parent Section: transversal_designs_latin_blow_ups_and_products_blow_ups_of_a_fixed_linear_triple_system
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

Let \(s(T)\) be the maximum number of edges in a linear cycle of \(T\). Then every arbitrary Latin blow-up of \(T\) has normalized density at most
\[
\frac{m}{v\,s(T)}+o(1). \tag{4}
\]

#### Proof
By Theorem 3, the maximum path length of \(T(q)\) is at least
\[
s(T)q-o(q).
\]
Using (2),
\[
\frac{|E(T(q))|/|V(T(q))|}{s(T)q-o(q)}
=
\frac{mq/v}{s(T)q-o(q)}
=
\frac{m}{v\,s(T)}+o(1).
\]
∎

Therefore an arbitrary Latin blow-up can exceed the one-third scale only if its base hypergraph satisfies
\[
s(T)<\frac{3m}{v}. \tag{5}
\]

This converts the amplification problem into a finite structural problem about the density and circumference of the base hypergraph.
