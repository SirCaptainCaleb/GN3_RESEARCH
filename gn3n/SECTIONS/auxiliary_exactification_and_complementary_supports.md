# Auxiliary exactification and complementary path supports

**Summary:** The auxiliary vertex removes the gap between the stronger one-change target and the actual two-cover conjecture.

## Statement

Adding one special vertex makes the directed one-change geodesic property exactly equivalent to a two-cover, and the exactified state admits complementary-tail, common-endpoint, and positive-factorization descriptions.

## Composition

## Exactification before support-family development

### One-change orders and opposite-edge supports

Before exactifying the theorem, it is useful to record the support meaning of a one-change order.

For an ordered pair \(u,v\), let \(\mathcal F_{uv}\) consist of the sets
\[
X\subseteq V\setminus\{u,v\}
\]
for which some ordering of \(X\), followed by \(u,v\), is a tight path.

A spanning order with status word
\[
1^a0^b
\]
exists if and only if for some \(u\ne v\) there are
\[
X\in\mathcal F_{uv},
\qquad
Y\in\mathcal F_{vu}
\]
with
\[
X\sqcup Y=V\setminus\{u,v\}.
\]
Indeed, the tight prefix ends in \(u,v\), while reversing the non-tight suffix turns it into a tight path ending in \(v,u\). Conversely the two tight paths splice to a one-change order.

Equivalently, one may use two tight paths having one common terminal vertex. If
\[
P=(p_1,\ldots,p_\ell,v),
\qquad
Q=(q_1,\ldots,q_m,v),
\]
then
\[
(p_1,\ldots,p_\ell,v,q_m,\ldots,q_1)
\]
has at most one change. Conversely splitting a one-change order and reversing the non-tight side gives such a common-terminal pair.

These formulations concern the directed word \(1^a0^b\). The other direction uses opposite initial edges or a common initial vertex. Either common-terminal path may be a singleton.

One useful quantitative consequence is retained from [[antipodal_geodesics_and_complementary_path_supports]]: a one-change order on \(N\geq2\) vertices yields two tight paths sharing an edge, so their orders sum to \(N+2\). Hence at least one has
\[
\left\lceil\frac{N+2}{2}\right\rceil
\]
vertices. This helps explain why the one-change target on the original vertices may be stronger than a two-cover.

We now exactify the original theorem before developing these support formulations further.

### Auxiliary-vertex exactification

Adjoin a new vertex \(r\) to \(H\). Retain every old triple and impose
\[
h(u,v,r)=1,
\qquad
h(r,v,u)=0
\]
for distinct \(u,v\in V(H)\). Values of
\[
h(u,r,v)
\]
may be chosen arbitrarily subject to boundary reversal.

Every spanning order of the extension is uniquely
\[
(L,r,R).
\]

**Theorem 3 (exact one-change extension).**
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
H^+\text{ has a spanning order of directed form }1^a0^b.
}
\]

Assume \(V(H)\ne\varnothing\). More precisely, directed one-change orders of \(H^+\) occur in reversal pairs and map two-to-one onto two-covers of \(H\). A cover is an unordered collection of individually ordered paths.

**Proof.** Suppose
\[
(L,r,R)
\]
has directed form \(1^a0^b\). If \(|L|\ge2\), the last two vertices of \(L\) followed by \(r\) form a tight triple by construction. Hence every earlier triple on the left belongs to the initial tight run, so \(L\) is a tight path. Likewise a triple beginning at \(r\) is non-tight, forcing the entire right side into the non-tight run; therefore \(R^{\rm rev}\) is a tight path. Removing \(r\) gives
\[
L\mid R^{\rm rev}.
\]

Conversely, from a two-cover
\[
P\mid Q
\]
the two orders
\[
(P,r,Q^{\rm rev}),
\qquad
(Q,r,P^{\rm rev})
\]
have directed form \(1^a0^b\). The possible triple with \(r\) in the middle may have either value without creating a second switch. For a one-path cover \(P\), the two orders are \((P,r)\) and \((r,P^{\rm rev})\); when deleting \(r\), discard an empty side. The two side orders are recoverable from the spanning order, proving the two-to-one assertion. \(\square\)

This theorem is the conceptual pivot of the article. From here onward the geodesic and support formulations model the **actual conjecture**, not merely a stronger surrogate.

### Exact geodesic form

Apply the memory lift to \(H^+\) and keep the copy with source color \(1\). Its pole-geodesic words begin in \(1\) and end in \(0\). Therefore
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
\Gamma(H^+)\text{ has a directed one-change pole geodesic}.
}
\]

The switch is normalized near \(r\). If
\[
P=(p_1,\ldots,p_k),
\qquad
Q=(q_1,\ldots,q_\ell),
\]
then the order
\[
(P,r,Q^{\rm rev})
\]
changes in the junction containing \(r\). There is no separate search for the switch position.

Similarly, in the opposite-edge support formulation for \(H^+\), the shared oppositely directed edge necessarily contains \(r\). In the common-terminal formulation, the endpoint-moving involution has a unique representative whose common endpoint is \(r\). Deleting \(r\) from that normalized state recovers the two-cover.

### Complementary tails in the exactified problem

The support-family language can now be read without ambiguity.

A directed one-change order of \(H^+\) is equivalent to two tight paths
\[
P=(X,u,v),
\qquad
Q=(Y,v,u)
\]
whose union is \(V(H^+)\), whose intersection is the ordinary edge \(uv\), and whose remaining supports are complementary.

Because the exactification forces
\[
r\in\{u,v\},
\]
this is an exact support encoding of a two-cover of \(H\).

Equivalently, normalize the paired common-terminal state so that both paths end at \(r\):
\[
P=(P_H,r),
\qquad
Q=(Q_H,r).
\]
Then
\[
P_H\mid Q_H
\]
is a two-cover of \(H\).

Thus the unresolved support problem may be stated as a complementary-tail problem **with a distinguished root** rather than as an arbitrary opposite-endpoint problem. This positional normalization is important: many topological arguments naturally produce support abundance, but the theorem needs the correct root and the correct endpoint order.

### The endpoint-moving involution

For completeness, common-terminal pairs on a fixed support carry a fixed-point-free involution.

Suppose
\[
P=(A,u,v),
\qquad
Q=(B,w,v).
\]
Exactly one of
\[
(u,v,w),
\qquad
(w,v,u)
\]
is tight. If the first is tight, replace the pair by
\[
(A,u,v,w),
\qquad
(B,w).
\]
The common endpoint moves from \(v\) to \(w\). If \(B\) is nonempty with last vertex \(z\), tightness of the old second path gives \((z,w,v)\) tight, so the same rule returns to \(v\). The other orientation is symmetric.

If one path is the singleton \((v)\), write the other as \((A,u,v)\) and replace the pair by \((A,u)\) and \((v,u)\). These are tight, and the preceding rule returns to the old pair when \(A\) is nonempty; when \(A\) is empty the singleton rule itself returns. Thus the involution is defined on every common-terminal pair whose union has at least two vertices.

The involution explains why common-terminal states naturally occur in pairs. In \(H^+\), exactly one member of such a pair has common endpoint \(r\), which is another form of the exactification.

### The common-terminal counting identity

One useful identity from the earlier positive enumeration has a direct combinatorial proof. For a boundary tournament \(J\) on at least two vertices, let \(A(J)\) count spanning orders of directed form \(1^a0^b\), and let \(h(J)\) count ordered tight Hamilton paths. Let \(b(J)\) count a choice of vertex \(v\) and an unordered pair of nonempty tight paths partitioning \(V(J)\setminus\{v\}\), such that appending \(v\) to either path remains tight. Then
\[
\boxed{A(J)=h(J)+b(J).}
\]

**Proof.** Common-terminal pairs with a singleton member correspond to the \(h(J)\) Hamilton paths; pairs with both members nontrivial correspond to the \(b(J)\) certificates. The endpoint-moving involution groups all these pairs into two-element orbits, one for each unordered opposite-terminal-edge pair. Such an edge pair also gives exactly two directed one-change orders, exchanged by reversal. Conversely a directed word has a uniquely specified shared edge: if it contains \(a\) tight triples, use its vertices in positions \(a+1,a+2\). Thus both sides count twice the number of opposite-terminal-edge pairs. \(\square\)

This identity retains the earlier square-zero calculation's positive combinatorial content without requiring its transfer matrices. It concerns the directed one-change target on \(J\); it does not assert that an arbitrary two-cover of \(J\) gives such an order.

### Positive factorization

Work in the square-zero algebra
\[
\mathcal A
=
\mathbb Q[x_v:v\in V]/(x_v^2:v\in V).
\]
Let
\[
F_H
=
\sum_{P\text{ nonempty tight in }H}x_{V(P)},
\]
counting distinct path orders separately.

For \(S\subseteq V\), let \(m_r(S)\) be the number of directed one-change orders on \(S\cup\{r\}\). Applying the exact extension to every induced subtournament gives
\[
\boxed{
\sum_{S\subseteq V}m_r(S)x_S
=
(1+F_H)^2.
}
\]

The constant term is the singleton order \(r\); the term \(2F_H\) places one nonempty tight path on either side of \(r\); and \(F_H^2\) records two disjoint nonempty tight paths. Square-zero multiplication removes intersecting supports with no cancellation.

In particular
\[
m_r(V)
=
2[x_V]\left(F_H+\frac12F_H^2\right).
\]

This factorization does not itself prove positivity. Its value is conceptual: it confirms that the auxiliary one-change model counts exactly the original one- and two-path covers.

The first half of Article VII is therefore exact:
\[
\text{two-cover}
\longleftrightarrow
\text{rooted one-change order}
\longleftrightarrow
\text{rooted one-change geodesic}
\longleftrightarrow
\text{rooted complementary supports}.
\]
The second half asks what antipodal topology can force inside these exact models.


## Further developments



## Metadata

- ID: auxiliary_exactification_and_complementary_supports
- Kind: section
- Version: 4
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False
- Subsections existing when composed: 2
- Subsections now: 2

## Development tree

- [Subsection 1 — Exactification before support-family development](../SUBSECTIONS/auxiliary_exactification_and_complementary_supports_subsection_a.md) (`auxiliary_exactification_and_complementary_supports_subsection_a`; development v4; composition v1; stale=False)
- [Subsection 2 — Further developments](../SUBSECTIONS/auxiliary_exactification_and_complementary_supports_subsection_b.md) (`auxiliary_exactification_and_complementary_supports_subsection_b`; development v1; composition vNone; stale=False)
