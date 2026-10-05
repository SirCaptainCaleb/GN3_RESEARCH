# The defect-line identity

## Cold composition

**Lemma 1.**
\[
c(\pi)=1+\tau(L_\pi)=1+\nu(L_\pi).
\]

**Proof.** A set \(C\) of cuts partitions \(\pi\) into tight paths exactly when, for every defect center \(i\), at least one of the adjacent cuts \(i-1,i\) belongs to \(C\). Thus \(C\) is a vertex cover of \(L_\pi\), and
\[
c(\pi)=1+\tau(L_\pi).
\]
The graph \(L_\pi\) is a subgraph of a path and is therefore bipartite, so \(\tau(L_\pi)=\nu(L_\pi)\). \(\square\)

Hence \(H\) has a two-cover if and only if some spanning ordering satisfies
\[
\nu(L_\pi)\le1.
\]

If the defect centers occur in maximal consecutive runs of lengths \(r_1,\ldots ,r_s\), then
\[
\nu(L_\pi)=\sum_{j=1}^s\left\lceil\frac{r_j}{2}\right\rceil.
\]
In particular, \(c(\pi)=3\) exactly when there is one run of length three or four, or two separated runs, each of length one or two.

## Metadata

- ID: defect_lines_and_spanning_order_compression_the_defect_line_identity
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/defect_lines_and_spanning_order_compression_the_defect_line_identity_subsection_a.md) (\`defect_lines_and_spanning_order_compression_the_defect_line_identity_subsection_a\`; development v1; composition vNone; stale=True)
