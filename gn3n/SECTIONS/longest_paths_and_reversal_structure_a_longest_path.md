# A longest path

## Body

Choose a longest tight path
\[
A=(a_0,\ldots ,a_{\lambda-1})
\]
and put
\[
U=V(H)-V(A).
\]

**Lemma 3.**
1. \(H[U]\) is non-Hamiltonian and has path-cover number two.
2. For every \(y\in U\),
\[
(a_1,a_0,y),\qquad
(y,a_{\lambda-1},a_{\lambda-2})
\]
are tight.
3. The complement of every nonempty proper contiguous subpath of \(A\) is non-Hamiltonian and has path-cover number two.

**Proof.** If \(H[U]\) were Hamiltonian, Hamilton paths on \(A\) and \(U\) would two-cover \(H\). Minimality gives a two-cover of every proper induced subtournament, proving (1).

If \((y,a_0,a_1)\) were tight, prepending \(y\) would give a longer tight path. Hence \((y,a_0,a_1)\) is non-tight and boundary reversal gives \((a_1,a_0,y)\) tight. The other end is symmetric.

Let \(I\) be a nonempty proper contiguous subpath of \(A\). If \(H-I\) were Hamiltonian, Hamilton paths on \(I\) and \(H-I\) would two-cover \(H\). Minimality again gives path-cover number two. \(\square\)

No two-cover of \(U\cup\{a_0,a_1\}\) can have a component ending with \((a_0,a_1)\), since the inherited suffix of \(A\) could then be appended. The symmetric statement holds at the other end. Thus the two reversed endpoint families coexist but cannot be joined directly.

## Metadata

- ID: longest_paths_and_reversal_structure_a_longest_path
- Kind: section
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 1: (untitled)
