# Maximal supports are absolutely nonaugmentable by exposed endpoints

## Metadata

- ID: maximal_supports_are_absolutely_nonaugmentable_by_exposed_endpoints
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 143
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Maximality forbids every exposed-endpoint enlargement

Retain the setting of [[maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs]]:
\[
S=(s_1,\ldots,s_k),\qquad H-S=P\mid Q,
\]
where \(S\) has maximum cardinality among Hamiltonian supports whose complement is two-coverable. Write
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t).
\]

Let
\[
E_P\subseteq\{p_1,p_m\},\qquad E_Q\subseteq\{q_1,q_t\},
\]
and put
\[
E=E_P\cup E_Q.
\]
Assume \(E\ne\varnothing\).

Deleting any chosen subset of the two displayed endpoints of a tight path leaves either the whole path, a one-sided truncation, or its interior interval, all of which are tight. Therefore
\[
H-(S\cup E)
\]
is covered by the two inherited residual intervals
\[
P-E_P\mid Q-E_Q,
\]
with empty intervals omitted. Hence
\[
pc\bigl(H-(S\cup E)\bigr)\le2.
\]

If \(S\cup E\) were Hamiltonian and proper, it would be a Hamiltonian support strictly larger than \(S\) with two-coverable complement, contradicting maximality. If \(S\cup E=V(H)\), its Hamiltonicity would itself give a spanning Hamilton path and hence a two-cover. Thus in the no-two-cover setting this case is impossible as well.

Consequently
\[
\boxed{H[S\cup E]\text{ is non-Hamiltonian for every nonempty }E
\subseteq\{p_1,p_m,q_1,q_t\}.}
\]

In particular:

- no one exposed endpoint extends \(S\);
- no two exposed endpoints jointly extend \(S\), whether they come from the same complementary path or opposite paths;
- no three or four exposed endpoints jointly extend \(S\).

This strengthens endpoint noninsertability from a one-label statement to an **exposed-endpoint absolute nonaugmentability** statement.

### Order-preserving coupled absorption consequence

Fix two exposed endpoints \(u,v\). They are individually noninsertable into the displayed order of \(S\). If there were a Hamilton order of \(S\cup\{u,v\}\) preserving the relative order of all vertices of \(S\), [[minimum_pair_coupled_insertions_have_range_at_most_two]] would place \(u,v\) adjacent or with one \(S\)-vertex between them. But maximality has just shown that \(S\cup\{u,v\}\) is non-Hamiltonian. Therefore no such order exists.

Thus every attempted two-endpoint enlargement either fails already in the local adjacent/one-separator tests, or any Hamilton comparison order on a related bounded support must change the inherited order on \(S\), producing exactly the order-disagreement interface used by the transport machinery.

The maximal-support branch is therefore more rigid than the original endpoint statement: all four exposed complementary endpoints form a jointly nonaugmenting reservoir around the same Hamiltonian support.

## Frontier

- Development version when composed: None
- Development version now: 1
