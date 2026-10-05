# A five-set or an end-edge reversal

## Cold composition

For \(y\in U\), the first and third triples of
\[
(a_1,a_0,y,a_{\lambda-1},a_{\lambda-2})
\]
are tight by Lemma 3. If
\[
(a_0,y,a_{\lambda-1})
\]
is tight, these five vertices form a Hamilton path.

Suppose instead that this middle triple is non-tight for every \(y\in U\). Then
\[
(a_{\lambda-1},y,a_0)
\]
is tight for every \(y\in U\). Define a tournament on \(U\) by
\[
p\to q
\quad\Longleftrightarrow\quad
(p,a_{\lambda-1},q)\text{ is tight}.
\]
Since \(|U|\ge4\), some \(y\) has an in-neighbor \(w\) and an out-neighbor \(z\). Then
\[
(y,a_{\lambda-1},z,a_0)
\]
is a tight four-path, while
\[
(w,a_{\lambda-1},y)
\]
reverses its first edge \((y,a_{\lambda-1})\). Indeed, the first triple comes from \(y\to z\), the second consecutive triple is the difficult-orientation relation \((a_{\lambda-1},z,a_0)\), and \(w\to y\) gives the displayed reversing triple.

Thus:

**Lemma 4.** Either some
\[
(a_1,a_0,y,a_{\lambda-1},a_{\lambda-2})
\]
is a Hamilton path, or a four-vertex tight path has an explicitly reversed end edge.

In the second case the four-set supporting the displayed tight path is Hamiltonian, and the reversing triple uses one additional exterior vertex. In a minimum counterexample its complement is therefore non-Hamiltonian and has path-cover number two.

## Metadata

- ID: longest_paths_and_reversal_structure_a_five_set_or_an_end_edge_reversal
- Kind: section
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/longest_paths_and_reversal_structure_a_five_set_or_an_end_edge_reversal_subsection_a.md) (`longest_paths_and_reversal_structure_a_five_set_or_an_end_edge_reversal_subsection_a`; development v1; composition vNone; stale=False)
