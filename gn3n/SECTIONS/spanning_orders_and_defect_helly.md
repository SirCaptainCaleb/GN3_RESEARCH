# Spanning orders and defect Helly theory

**Summary:** The original two-cover problem is an exact interval-Helly problem on the defect line of a spanning order.

## Statement

For a spanning order, the two-cover condition is exactly the existence of one cut meeting every non-tight defect interval; failure is witnessed by two disjoint defects, and the extreme defects provide canonical coordinates for later topology.

## Composition

## Inversion windows, positive witnesses, and minimum holes

For a spanning order \(\pi\), let \(p(\pi)\) be the first non-tight status and \(q(\pi)\) the last tight status. The two-cover problem is equivalent to the single inequality
\[
q(\pi)\le p(\pi)+1.
\]
Thus
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\quad q(\pi)\le p(\pi)+1.
\]
The corresponding order-level deficiency
\[
d_2(\pi)=\max\{0,q(\pi)-p(\pi)-1\}
\]
has the global interpretation
\[
\boxed{\kappa_2(H)=\min_\pi d_2(\pi)}.
\]

Failure is local: an order has positive deficiency if and only if its status word contains one of
\[
\mathcal W_+=\{001,011,0101\}.
\]
These witnesses use at most six consecutive vertices and are closed under reverse-complement.

Minimum deletion sets carry substantially more structure. If \(|X|=\kappa_2(H)\) and \(H-X=P\mid Q\), then every \(Y\subseteq X\) satisfies
\[
\kappa_2(H-(X\setminus Y))=|Y|.
\]
In particular no nonempty subfamily of \(X\) can be absorbed into \(P\) and \(Q\), even after splitting that subfamily between the two sides. This hereditary exactness is the deletion-theoretic invariant used throughout the remainder of the article.

## Metadata

- ID: spanning_orders_and_defect_helly
- Kind: section
- Version: 14
- Math version: 11
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 2
- Composition stale: False
- Subsections existing when composed: 3
- Subsections now: 3

## Development tree

- [Subsection 1 — Defect intervals and the exact Helly criterion](../SUBSECTIONS/spanning_orders_and_defect_helly_subsection_a.md) (`spanning_orders_and_defect_helly_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — Exact inversion-window criterion](../SUBSECTIONS/spanning_orders_and_defect_helly_subsection_b.md) (`spanning_orders_and_defect_helly_subsection_b`; development v8; composition v2; stale=False)
- [Subsection 3 — Local forbidden patterns and witness handoff](../SUBSECTIONS/spanning_orders_and_defect_helly_subsection_c.md) (`spanning_orders_and_defect_helly_subsection_c`; development v3; composition v1; stale=False)
