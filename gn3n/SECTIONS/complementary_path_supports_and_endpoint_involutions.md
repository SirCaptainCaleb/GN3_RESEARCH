# Complementary path supports and endpoint involutions

**Summary:** The geodesic switch can be translated exactly into complementary tight-path supports, exposing a rigid endpoint involution and a positive support-counting formulation.

## Statement

A one-change spanning order is equivalent to two tight paths with complementary supports meeting along an oppositely directed terminal edge, or equivalently to two tight paths with one common terminal vertex. The latter states carry a fixed-point-free endpoint-moving involution.

## Composition

## Opposite terminal edges and complementary supports

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets \(X\subseteq V\setminus\{u,v\}\) for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word \(1^a0^b\) exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},\qquad Y\in\mathcal F_{vu}
\]
that partition \(V\setminus\{u,v\}\). Indeed, the tight prefix ends with \(u,v\), while reversing the non-tight suffix turns it into a tight path ending with \(v,u\). Conversely, two such paths splice into a spanning order whose first block is tight and second block non-tight.

Thus a one-change order is the same object as two tight paths sharing exactly one ordinary edge, traversed in opposite terminal directions, with complementary remaining supports. The \(0^a1^b\) case is the corresponding initial-edge formulation.

## The common-terminal formulation

Equivalently, on a vertex set \(W\), a spanning order with word \(1^a0^b\) exists if and only if there are two tight paths whose union is \(W\), whose intersection is one vertex \(v\), and which both end at \(v\). Either path may be the singleton \(v\).

From paths
\[
P=(p_1,\ldots,p_\ell,v),\qquad
Q=(q_1,\ldots,q_m,v)
\]
one obtains
\[
(p_1,\ldots,p_\ell,v,q_m,\ldots,q_1).
\]
All triples on the first side are tight and all triples on the reversed second side are non-tight; the single central triple may have either status without creating a second change. Conversely, split a one-change order at the change point and reverse its non-tight side.

This common-terminal picture removes the shared edge from the notation and is better adapted to endpoint transport.

## The endpoint-moving involution

Common-terminal pairs on a fixed support carry a fixed-point-free involution. Suppose
\[
P=(A,u,v),\qquad Q=(B,w,v).
\]
Exactly one of \((u,v,w)\) and \((w,v,u)\) is tight. If the first is tight, move \(w\) across the common endpoint:
\[
(A,u,v,w),\qquad(B,w).
\]
The new pair has common terminal vertex \(w\), and applying the same rule there returns to \(v\). The other orientation is symmetric. If one member is the singleton \(v\), the move truncates the other path at its final edge and creates the two-vertex path \((v,u)\); this is again inverted by the same rule.

The two paired common-terminal states are precisely the two truncations of one pair of tight paths that share an oppositely directed terminal edge and are otherwise disjoint. Hence endpoint motion by itself produces matched pairs rather than a longer orbit. Any augmentation argument needs an additional operation beyond this involution.

## Positive support enumeration

In the square-zero algebra
\[
\mathcal A=\mathbb Q[x_v:v\in V]/(x_v^2:v\in V),
\]
define
\[
F_{uv}=\sum_{P\text{ tight ending }u,v}
x_{V(P)\setminus\{u,v\}}.
\]
Then
\[
Z_{\rm end}(H)=\sum_{u<v}x_ux_vF_{uv}F_{vu}
\]
has nonnegative coefficients, and \([x_V]Z_{\rm end}(H)>0\) exactly when there is a spanning order of type \(1^a0^b\). Intersecting tails vanish because of the square-zero variables; complementary tails survive positively. An analogous polynomial \(Z_{\rm start}\) records the \(0^a1^b\) case.

This formulation isolates the unresolved combinatorics as a disjointness problem between opposite endpoint-support families. It is the support-theoretic shadow of the one-change geodesic problem.

## Metadata

- ID: complementary_path_supports_and_endpoint_involutions
- Kind: section
- Version: 12
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — Opposite terminal edges and complementary supports](../SUBSECTIONS/complementary_path_supports_and_endpoint_involutions_subsection_a.md) (`complementary_path_supports_and_endpoint_involutions_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — The common-terminal formulation](../SUBSECTIONS/complementary_path_supports_and_endpoint_involutions_subsection_b.md) (`complementary_path_supports_and_endpoint_involutions_subsection_b`; development v4; composition v1; stale=False)
- [Subsection 3 — The endpoint-moving involution](../SUBSECTIONS/complementary_path_supports_and_endpoint_involutions_subsection_c.md) (`complementary_path_supports_and_endpoint_involutions_subsection_c`; development v4; composition v1; stale=False)
- [Subsection 4 — Positive support enumeration](../SUBSECTIONS/complementary_path_supports_and_endpoint_involutions_subsection_d.md) (`complementary_path_supports_and_endpoint_involutions_subsection_d`; development v3; composition vNone; stale=False)
