# Proper regular row–column graphs obstruct full-length one-switch rainbow paths

- Stable ID: note_proper_regular_row_column_involution_obstruction
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xiii_binary_involutive_rainbow_paths
- Labels: obstruction, counterexample, proper-edge-coloring, regularity, involution
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7438_1
- Updated session: session_nori_r7438_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

**Proper, regular row–column obstruction.** For each integer \(d\ge2\), put \(q=2^d\) and choose a set \(I\) of \(q+1\) indices. Let \(G\) have vertices \((i,j)\in I^2\) with \(i\ne j\); join two vertices when they share a first coordinate (a row edge) or a second coordinate (a column edge). Each vertex has \(q-1\) edges of each type, so \(G\) is \(2(q-1)\)-regular and connected.

For each \(i\), choose a bijection \(f_i:I\setminus\{i\}\to\mathbb F_2^d\). Assign to row edges \((i,j)(i,j')\), and to their transposed column edges \((j,i)(j',i)\), the ordinary color
\[
\lambda=(i,f_i(j)+f_i(j')).
\]
Give all row edges binary label \(0\) and all column edges label \(1\); put \(\tau(i,j)=(j,i)\). Then \(\tau\) is an involutive vertex automorphism, \(\lambda(\tau e)=\lambda(e)\), and \(\chi(\tau e)=1-\chi(e)\). At \((i,j)\), its \(q-1\) row colors have first coordinate \(i\), its \(q-1\) column colors first coordinate \(j\), and each family is pairwise distinct. Hence the coloring is proper and both the degree and the color degree equal \(2q-2\) at every vertex.

Any rainbow path entirely within a row has length at most \(q-2\): a path of \(q-1\) edges would exhaust all \(q-1\) nonzero differences in \(\mathbb F_2^d\), whose sum is zero (as \(d\ge2\)), whereas the telescope of those differences is the nonzero difference between its distinct endpoints. The same holds for columns. Every rainbow path with at most one binary switch is one row segment followed by one column segment, or vice versa, hence has at most \(2q-4=\hat\delta-2\) edges. In particular a monochromatic-bit rainbow path has at most \(q-2\) edges.

This excludes even properness, regularity, color-degree regularity and the two involution identities, alone or together, as sufficient hypotheses for the original full-color-degree one-switch conjecture. It does not exclude a positive linear-fraction bound. See Article XIII's detailed transfer theorem for the broader generalization.
