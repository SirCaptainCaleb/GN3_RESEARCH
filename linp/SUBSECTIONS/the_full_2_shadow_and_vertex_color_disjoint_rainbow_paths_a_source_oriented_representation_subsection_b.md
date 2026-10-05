# Lemma 5

## Metadata

- ID: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation_subsection_b
- Parent Section: the_full_2_shadow_and_vertex_color_disjoint_rainbow_paths_a_source_oriented_representation
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

For every vertex \(v\),
\[
\frac12 d_D^+(v)+d_D^-(v)=d_H(v). \tag{10}
\]

#### Proof
Every hyperedge through \(v\) places \(v\) in exactly one of two roles. If \(v\) is the source, it contributes one to \(s(v)\); otherwise it contributes one to \(h(v)\). Hence
\[
s(v)+h(v)=d_H(v).
\]
Each source hyperedge contributes two distinct outgoing arcs, so
\[
d_D^+(v)=2s(v).
\]
Each nonsource occurrence corresponds to exactly one incoming arc, so
\[
d_D^-(v)=h(v).
\]
Substitution gives (10). ∎

Longest directed paths force complementary degree information at their ends.

## Development

For every vertex \(v\),
\[
\frac12 d_D^+(v)+d_D^-(v)=d_H(v). \tag{10}
\]

#### Proof
Every hyperedge through \(v\) places \(v\) in exactly one of two roles. If \(v\) is the source, it contributes one to \(s(v)\); otherwise it contributes one to \(h(v)\). Hence
\[
s(v)+h(v)=d_H(v).
\]
Each source hyperedge contributes two distinct outgoing arcs, so
\[
d_D^+(v)=2s(v).
\]
Each nonsource occurrence corresponds to exactly one incoming arc, so
\[
d_D^-(v)=h(v).
\]
Substitution gives (10). ∎

Longest directed paths force complementary degree information at their ends.
