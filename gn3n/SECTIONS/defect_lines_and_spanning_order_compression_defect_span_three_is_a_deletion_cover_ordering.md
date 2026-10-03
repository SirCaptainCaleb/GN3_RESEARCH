# Defect span three is a deletion-cover ordering

## Body

The defect span of \(\pi\) is \(0\) if there is no defect center and otherwise is
\[
\max D(\pi)-\min D(\pi)+1.
\]

A deletion cover
\[
H-x=P\mid Q
\]
gives the spanning ordering \(P,x,Q\), whose possible defect centers are the three positions adjacent to the join. The two outer join triples are non-tight, since otherwise \(x\) could be appended to one of the two paths and \(H\) would have a two-cover.

Conversely:

**Lemma 2.** If \(\pi=(v_1,\ldots ,v_n)\) has defect span \(3\), and \(i\) is its leftmost defect center, then with
\[
x=v_{i+1},\qquad
P=(v_1,\ldots ,v_i),\qquad
Q=(v_{i+2},\ldots ,v_n)
\]
the paths \(P,Q\) form a deletion cover of \(H-x\), and \(\pi=P,x,Q\).

**Proof.** No defect center occurs before \(i\) or after \(i+2\). Hence every internal triple of \(P\) and \(Q\) is tight. \(\square\)

There are two cases. If the middle join triple
\[
(v_i,x,v_{i+2})
\]
is tight, the central three vertices form a tight path. If it is non-tight, then all three join triples are non-tight, and boundary reversal gives the tight five-vertex path
\[
(v_{i+3},v_{i+2},x,v_i,v_{i-1})
\]
whenever the displayed vertices exist.

Thus every minimum-span ordering is a deletion-cover ordering whose central part is a Hamiltonian three-set or a Hamiltonian five-set.

## Metadata

- ID: defect_lines_and_spanning_order_compression_defect_span_three_is_a_deletion_cover_ordering
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — HOT, version 1: (untitled)
