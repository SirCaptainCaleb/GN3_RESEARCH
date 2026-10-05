# Connector-path exclusion for genuine two-deletion packets

## Metadata

- ID: connector_path_exclusion_for_genuine_two_deletion_packets
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 87
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

### Connector exclusion at deletion distance two

Let \(H[J]\) be a genuine two-deletion span. If a nonempty bounded packet fragment could join the two corridor tails as a tight path while the unused packet remainder were Hamiltonian, then the resulting decomposition would lower the two-cover deletion distance. In particular, every packet fragment of order at most seven is excluded from serving as such a connector. The shared-connector configurations occurring in the distance-one analysis therefore disappear from the genuine two-deletion layer.

## Development

## Connector-path exclusion in a genuine two-deletion residue

Let \(H\) be a boundary tournament with \(\kappa_2(H)\ge 2\). Suppose
\[
V(H)=S\sqcup V(T)\sqcup V(U),
\]
where \(T,U\) are vertex-disjoint tight paths. Let
\[
R=(r_1,\ldots,r_k)
\]
be a nonempty tight path whose support \(A=\{r_1,\ldots,r_k\}\) is contained in \(S\). Assume the displayed concatenation
\[
L=(T,R,U)
\]
(or symmetrically \((U,R,T)\)) is a tight path.

**Lemma.** If \(|S\setminus A|\le 6\), then \(\kappa_2(H)\le1\). If \(|S\setminus A|\le3\), then \(H\) already has a two-cover.

**Proof.** The path \(L\) covers every vertex outside \(S\) and all vertices of \(A\). Its complement is
\[
E=S\setminus A.
\]
When \(|E|\le6\), the small-set Hamiltonicity facts used in [[genuine_two_deletion_obstructions_have_no_small_packet_tail_connectors]] show that \(E\) becomes Hamiltonian after deleting at most one vertex \(d\): for \(|E|\le3\) it is Hamiltonian outright; for \(|E|=4\) delete one vertex; for \(|E|=5\) use a Hamiltonian four-deletion if needed; for \(|E|=6\) use a Hamiltonian five-deletion supplied by four-of-six. Hence \(H-d\) is covered by the two tight paths \(L\) and a Hamilton path of \(E-d\), proving \(\kappa_2(H)\le1\). If \(|E|\le3\), no deletion is needed and \(L\mid E\) is a two-cover. \(\square\)

**Six-/seven-packet consequence.** If \(|S|\le7\) and \(\kappa_2(H)\ge2\), then there is no nonempty packet path \(R\subseteq S\) that joins the two complementary tails into one tight path. Thus the connector exclusion from [[genuine_two_deletion_obstructions_have_no_small_packet_tail_connectors]] holds not only for one packet vertex but for every nonempty ordered packet fragment.

This gives a useful rooted forcing rule. Suppose a proposed packet fragment \(R\) has all its internal tight triples and all but one of the boundary join triples already forced by inherited corridor structure. In a genuine two-deletion residue the remaining join triple must be non-tight; boundary antisymmetry therefore forces its exact reverse triple. A family of overlapping candidate connector paths can consequently be converted into a family of forced reverse triples without any minimum-counterexample or disturbance argument.

Applied to the canonical six-packets in the monotone and rigid reflected-double branches, this also removes all "shared bridge" subcases from the genuinely \(\kappa_2=2\) layer: a shared bridge is already a one-vertex connector and hence would force \(\kappa_2\le1\). The neighboring-shared-bridge lemmas remain useful for the distance-one layer and for proving an outright two-cover, but they are not part of the residual two-deletion obstruction.

The remaining packet theorem should therefore be stated against a **connector-free rooted packet**: every nonempty packet fragment that would join the two tails is forbidden. The objective is to show that the resulting forced reverse triples either (i) make the packet complement Hamiltonian in a compatible way and hence give a two-cover, (ii) permit an enlarged-window repair using an exterior vertex, or (iii) create a strictly farther positive witness.
