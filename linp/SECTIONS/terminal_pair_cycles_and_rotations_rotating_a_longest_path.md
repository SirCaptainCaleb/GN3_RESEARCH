# Rotating a longest path

## Composition

The forced second intersections of Lemma 5 can change the last vertex of a longest path.

## Lemma 6

Let
\[
P=(g_1,\ldots,g_L)
\]
be a linear path with last vertex \(z\in g_L\). Let \(f\notin E(P)\) contain \(z\), and suppose that
\[
(f\setminus\{z\})\cap V(P)=\{w\}.
\]
Let \(j\) be the first index for which \(w\in g_j\). If \(j\le L-2\), then
\[
g_1,\ldots,g_j,f,g_L,g_{L-1},\ldots,g_{j+2}
\]
is an \(L\)-edge linear path.

#### Proof
The new sequence uses the initial segment \(g_1,\ldots,g_j\), crosses to \(f\), then traverses the old final segment in reverse. Consecutive edges meet at the prescribed vertices. Since \(f\) has no other vertex on \(P\), it has no nonconsecutive intersection with the old path. The original path is linear, so reversing the final segment creates no new intersection. ∎

Thus every single additional intersection at a suitable position creates another longest path with a different last vertex. Iterating such rotations is the natural mechanism for turning the \(\beta(T)\) fundamental-cycle intersections into many reachable last vertices.

## Metadata

- ID: terminal_pair_cycles_and_rotations_rotating_a_longest_path
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/terminal_pair_cycles_and_rotations_rotating_a_longest_path_subsection_a.md) (`terminal_pair_cycles_and_rotations_rotating_a_longest_path_subsection_a`; development v1; composition v1; stale=False)
- [Subsection 2 — Lemma 6](../SUBSECTIONS/terminal_pair_cycles_and_rotations_rotating_a_longest_path_subsection_b.md) (`terminal_pair_cycles_and_rotations_rotating_a_longest_path_subsection_b`; development v1; composition vNone; stale=False)
