# Minimum holes reduce to genuine two-deletion states with a five-component — preserved pre-item development

## Composition

(none yet)

## Development

## Minimum holes reduce canonically to a genuine two-deletion five-component state

Retain the setup of [[minimum_deletion_holes_of_order_at_least_three_force_canonical_root_advance_three_covers]]. Let
\[
X
\]
be a minimum two-cover deletion set of order \(k\ge3\), let
\[
H-X=P\mid Q,
\]
and choose a good pair \(x,y\in X\) supplied by the root-advance lemma. Put
\[
G=H-(X-\{x,y\}).
\]

Then
\[
\boxed{\kappa_2(G)=2.}
\]

Indeed, deleting \(x,y\) from \(G\) leaves \(H-X=P\mid Q\), so \(\kappa_2(G)\le2\). If \(\kappa_2(G)\le1\), deleting at most one further vertex from \(G\) would give a two-cover. In \(H\) this would delete at most
\[
(k-2)+1=k-1
\]
vertices, contradicting minimality of \(|X|=k\).

At the same time the root-advance pair gives an actual spanning three-cover of \(G\). If
\[
|P|=|Q|=s+1
\]
(as in the symmetric zero-root situation), then, up to left-right symmetry, the cover has exact profile
\[
\boxed{5\mid(s-1)\mid s.}
\]

Thus every symmetric minimum deletion hole of order at least three canonically produces a **genuine \(\kappa_2=2\) graph carrying a distinguished Hamiltonian five-component**.

This is a useful elevation because the high-deletion-distance zero-root problem no longer needs to be attacked at its original scale. Any theorem of the form

> every genuine \(\kappa_2=2\) boundary tournament with a three-cover containing a five-component has a two-cover, or reduces to a bounded endpoint-core configuration,

would immediately rule out all symmetric zero-root minimum holes of order at least three.

More modestly, all five-side / long-neighbor pairwise-repartition lemmas may now be applied inside \(G\) without carrying the other \(k-2\) hole vertices. The large hole has been compressed to the first nontrivial deletion layer before any further analysis.
