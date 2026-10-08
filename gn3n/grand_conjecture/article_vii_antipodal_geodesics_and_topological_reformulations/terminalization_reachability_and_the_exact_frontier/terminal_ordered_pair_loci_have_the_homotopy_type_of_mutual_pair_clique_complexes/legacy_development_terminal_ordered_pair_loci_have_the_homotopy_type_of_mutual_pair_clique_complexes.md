# Terminal ordered-pair loci have the homotopy type of mutual-pair clique complexes — preserved pre-item development

## Exact topology of a prescribed terminal ordered-pair locus

Let B be finite with |B|>=2, and let E be a set of ordered pairs (u,v) of distinct elements of B. Let C_E be the permutahedral subcomplex consisting of those faces every chamber of which has its last ordered pair in E.

Put A_v={u:(u,v) in E}, and V_E={v:A_v is nonempty}. Define the simple graph G_E on V_E by
\[
uv\in E(G_E)\quad\Longleftrightarrow\quad (u,v)\in E\ \hbox{and}\ (v,u)\in E.
\]
Let K(G_E) be its clique complex.

**Theorem.** If E is empty, C_E is empty. Otherwise
\[
C_E\simeq K(G_E).
\]
The first-two-position analogue follows by reversing orders and reversing the ordered-pair relation.

**Proof.** For each v in V_E, let C_v be the part of C_E in the facet with last block {v}. The remaining prefix is P(B-{v}), with its last vertex restricted to A_v. Therefore C_v is a nonempty contractible subcomplex by [[prescribed_endpoint_subsets_of_a_permutahedron_give_contractible_outward_loci]].

For each clique T of G_E with |T|>=2, let Q_T be the face (B-T)|T, omitting the empty first block when T=B. This face lies in C_E because every distinct ordered pair from T is allowed.

These C_v and Q_T cover C_E as subcomplexes. Indeed, a face with singleton last block {v} belongs to C_v. If its last block is T with |T|>=2, every ordered pair from T occurs as the terminal pair of some chamber. Thus T is a clique and the face belongs to Q_T.

We verify every nonempty finite intersection is contractible and determine exactly when it is nonempty.
1. C_v and C_w are disjoint for v!=w, because they prescribe different last labels.
2. An intersection of Q_T's is nonempty exactly when the sets T form a chain under inclusion. Each Q_T prescribes T as a suffix set of a chamber order; two suffix sets must be nested. Conversely a nested chain is realized by ordering its successive set differences. Its intersection is a convex face.
3. C_v intersects a chain of Q_T's exactly when v belongs to its smallest T. Necessity follows because the terminal label must lie in every suffix set. For sufficiency, refine the common ordered-partition face by splitting its last block T into (T-{v})|{v}. Every possible predecessor of v is now in T-{v}, and all of these belong to A_v because T is a clique. Consequently this refinement is exactly the intersection with C_v; it is a nonempty convex face.

The case consisting only of one C_v is contractible by the endpoint-subset theorem. Thus the cover is a finite cover by subcomplexes with contractible nonempty intersections. Apply the subcomplex nerve lemma. Its nerve has one vertex for each singleton {v}, represented by C_v, and one for each clique T of size >=2, represented by Q_T. Its simplices are exactly inclusion chains of nonempty cliques. The nerve is therefore the barycentric subdivision of K(G_E). This proves the theorem. ∎

The precise topological citation is Allen Hatcher, Algebraic Topology, §4G, Corollary 4G.3 and Exercise 4 (the extension to covers by subcomplexes), https://pi.math.cornell.edu/~hatcher/AT/ATch4.4.pdf, printed pp. 459–460. All cover and intersection checks above are supplied explicitly; the cover sets C_v need not be convex.

## Consequences

The locus C_E is connected exactly when G_E is connected, and it is contractible exactly when K(G_E) is contractible. In particular:
- A vertex adjacent to every other vertex of G_E makes its clique complex a cone, hence C_E contractible.
- A connected tree G_E gives a contractible locus.
- A bidirected chordless four-cycle, with no other allowed pairs, gives C_E homotopy equivalent to a circle.
- If there are no mutual pairs, C_E has |V_E| contractible connected components. One-way arcs can enlarge each terminal-label sector but cannot join different terminal-label sectors.

This is an exact classification, not a claim that every nonempty ordered-pair locus is acyclic.

## Protected determining windows

Suppose a free block meets a determining window in exactly two terminal (or initial) slots, all other determining positions are fixed, and absence of the occurrence is exactly the condition that the corresponding ordered pair belongs to E. The protected outward locus in this factor is C_E. Neutral factors do not change its homotopy type. If two determining windows depend on separate factors, their simultaneous absence locus is the product of the respective loci.

For an invariant sector of protected separator faces, if every such factor has a nonempty contractible clique complex (and every one-vertex factor has a nonempty allowed subset), the natural carriers D(F)=F intersect X_{r+1} are contractible. They remain nested under face inclusion. The inductive equivariant extension argument of [[natural_outward_carriers_close_the_one_boundary_vertex_sector]] therefore extends to this sector verbatim. A genus-loss assertion for the full separator still requires these conditions on every relevant face, not just on a chosen sector.

This theorem complements [[two_slot_persistent_boundary_reservoirs_are_uniformly_blocked_and_rooted]]. On a double-persistent two-slot endpoint reservoir the first/third fixed status makes the same-face absence relation empty: that branch needs an outward replacement or attachment theorem. The clique-complex classification applies instead to variable-persistence and outward-choice sectors, where a nonempty relation genuinely occurs.
