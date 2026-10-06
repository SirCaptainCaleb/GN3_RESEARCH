# Article VII — exact deficiency, antipodal roots, and terminal carriers

## Composition status

- Composition version: 9
- Stale: False
- Composed through revision: 1916

## Composition

# Article VII — exact deficiency, antipodal roots, and the minimum-counterexample frontier

For a spanning order \(\pi\), let \(p(\pi)\) be the first non-tight status and \(q(\pi)\) the last tight status, and put
\[
c(\pi)=m+1-q(\pi),\qquad d_2(\pi)=\max\{0,q-p-1\}.
\]
The basic exactness theorem identifies
\[
\kappa_2(H)=\min_\pi d_2(\pi),
\]
so the order statistic is exactly the deletion distance to a spanning two-path cover. The corresponding exact inversion root
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}
\]
is odd under reversal. Thus antipodal topology can be applied directly to the genuine two-cover deficiency rather than to an auxiliary surrogate.

The convex-root construction produces positively balanced carrier faces. When all roots on such a carrier are nonzero, face geometry compresses sharply: the varying root data lie in one central block of order at most four, with only bounded exterior freedom. For \(\kappa_2(H)\ge2\), the dimension surplus already forces a zero exact root. The only potentially exceptional nonzero recurrence is therefore the deletion-distance-one case.

Now let \(H\) be a minimum-order counterexample. Every proper induced subtournament satisfies the conjecture, so for every vertex \(x\), \(H-x\) has a spanning two-cover. Hence
\[
\kappa_2(H)=1.
\]
At deletion distance one, three surplus antipodal dimensions may be spent on three actual-vertex role coordinates. For any prescribed triple, Borsuk--Ulam yields a positively balanced exact-root carrier with zero average in those three roles. If this carrier had no zero root, the exact-root compression theorem forces the unique possible geometry: a freely permuted four-vertex central block with equal left and right sides, and all four central role averages zero.

That four-block cannot occur. Boundary antisymmetry among five selected permutations of the block forces incompatible central status words. Consequently the entire nonzero exact-root branch is empty in a minimum counterexample.

Thus every minimum-order counterexample contains a chamber with
\[
p(\pi)=c(\pi).
\]
This is the present exact-root frontier. It is important not to mistake it for a two-cover: zero root is a symmetric exact-deficiency state, not closure by itself.

The deletion-cover topology independently constrains any residue that survives equivariant leaf collapse. Cubical parity propagates partial critical stars to full stars; minimum-degree full stars saturate Johnson blocks; and minimum-counterexample heredity then forces any nonempty antipodally invariant closed deletion residue to be the complete odd middle layer:
\[
n=2r+1,
\]
every \(r\)-set is Hamiltonian, and every \((r+1)\)-set is non-Hamiltonian. Hamiltonian prefix chains further show that any nonempty closed cocycle of actual deletion edges is then the whole middle deletion interface.

This odd uniform state has strong path consequences. Every exterior vertex reverses both exposed end-edges of every maximum \(r\)-path. Separated or adjacent insertion gaps give genuine path augmentation, while arbitrary compatible insertion orders need not exist. What survives is therefore not a support-only obstruction but an endpoint-order obstruction.

Two newer local mechanisms sharpen that obstruction. First, deleting the root vertex from an actual Hamiltonian one-vertex extension leaves at most two adjacent status defects; if both bridge triples fail, boundary reversal exposes a tight reversed four-vertex seam. Second, two maximum paths sharing an endpoint cannot have mutually exterior next vertices in the same endpoint role. More generally, an odd cycle of rooted Hamiltonian supports with pairwise consecutive intersection exactly at the common root forces a path one vertex longer. Hence, in the odd uniform residue, every explicit odd support cycle must contain a support on which the root is internal in every Hamiltonian order.

Article VII therefore leaves a single scale-independent closure problem. Starting from a zero exact-root chamber in a minimum counterexample, exploit the adjacent two-defect seam and the forced endpoint-role structure to obtain either a spanning two-cover or a contradiction to minimum counterexamplehood. The old nonzero-root recurrence, bounded-support terminalization, and small-order cutoff branches are no longer active frontiers.

## Contained Sections

- 1. [Spanning orders and defect Helly theory](../SECTIONS/spanning_orders_and_defect_helly.md) (`spanning_orders_and_defect_helly`; composition v2; stale=False)
- 2. [From antipodal labels to cellular root topology](../SECTIONS/antipodal_labels_and_cellular_root_topology.md) (`antipodal_labels_and_cellular_root_topology`; composition v3; stale=False)
- 3. [Convex root balance and Bourgin–Yang multiplicity](../SECTIONS/convex_root_balance_and_bourgin_yang.md) (`convex_root_balance_and_bourgin_yang`; composition v2; stale=False)
- 4. [Exact-root compression and bounded central structure](../SECTIONS/exact_root_compression_and_bounded_central_structure.md) (`exact_root_compression_and_bounded_central_structure`; composition v2; stale=False)
- 5. [Deletion distance one: role-balanced four-blocks and Ky Fan alternation](../SECTIONS/kappa_one_role_balance_and_ky_fan.md) (`kappa_one_role_balance_and_ky_fan`; composition v2; stale=False)
- 6. [Local-witness topology and the finite terminal theorem](../SECTIONS/local_witness_topology_and_the_finite_terminal_theorem.md) (`local_witness_topology_and_the_finite_terminal_theorem`; composition v2; stale=False)
- 7. [Terminalization, reachability, and the exact frontier](../SECTIONS/terminalization_reachability_and_the_exact_frontier.md) (`terminalization_reachability_and_the_exact_frontier`; composition v9; stale=True)
- 8. [Synthesis and the exact topological frontier](../SECTIONS/article_vii_synthesis_and_exact_frontier.md) (`article_vii_synthesis_and_exact_frontier`; composition v2; stale=False)
