# Defect span

## Composition

For an ordering \(\pi=(v_1,\ldots ,v_n)\), an index \(i\), \(2\le i\le n-1\), is a defect center if
\[
(v_{i-1},v_i,v_{i+1})
\]
is non-tight. The defect span of \(\pi\) is \(0\) when there is no defect center and otherwise is
\[
\max D-\min D+1,
\]
where \(D\) is the set of defect centers.

**Lemma 1.** \(H\) has a two-cover if and only if it has a spanning ordering of defect span at most \(2\).

**Proof.** If \(P=(v_1,\ldots ,v_j)\) and \(Q=(v_{j+1},\ldots ,v_n)\) form a two-cover, then all defect centers of the concatenated ordering lie among \(j,j+1\). Conversely, if all defect centers lie among two consecutive indices \(j,j+1\), then
\[
(v_1,\ldots ,v_j)\quad\text{and}\quad (v_{j+1},\ldots ,v_n)
\]
are tight paths and form a two-cover. \(\square\)

Let \(H-x=P\mid Q\), where
\[
P=(p_1,\ldots ,p_r),\qquad Q=(q_1,\ldots ,q_s).
\]
The ordering
\[
(p_1,\ldots ,p_r,x,q_1,\ldots ,q_s)
\]
has possible defect centers only at the three positions adjacent to the join. The two outer join triples are necessarily non-tight: if \((p_{r-1},p_r,x)\) were tight, then \((P,x)\mid Q\) would be a two-cover of \(H\), and the other side is symmetric. Hence every deletion cover gives a spanning ordering of defect span \(3\).

If the middle triple \((p_r,x,q_1)\) is also non-tight, boundary reversal gives
\[
(x,p_r,p_{r-1}),\qquad (q_1,x,p_r),\qquad (q_2,q_1,x)
\]
tight whenever the displayed vertices exist. Thus
\[
(q_2,q_1,x,p_r,p_{r-1})
\]
is a tight path. The problem is therefore to reduce a spanning ordering of defect span \(3\) to one of defect span at most \(2\).

## Metadata

- ID: deletion_covers_and_the_support_graph_defect_span
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/deletion_covers_and_the_support_graph_defect_span_subsection_a.md) (`deletion_covers_and_the_support_graph_defect_span_subsection_a`; development v1; composition vNone; stale=False)
