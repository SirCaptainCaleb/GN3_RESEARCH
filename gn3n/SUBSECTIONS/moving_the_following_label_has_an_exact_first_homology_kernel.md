# Moving the following label has an exact first-homology kernel

## Metadata

- ID: moving_the_following_label_has_an_exact_first_homology_kernel
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 150
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Exact first-homology kernel for moving the following label

The four-cycle obstruction extends to an arbitrary terminal-pair relation.

Let B be finite of order at least two, z outside B, and T=B union {z}. Fix exit values delta:T->{0,1} with delta(z)=1. Let D be the chamber-defined subcomplex of P(T) in which a chamber is allowed exactly when its final label w has delta(w)=0 or its last ordered triple is tight. Put F=P(B)|{z}, D_0=D intersect F.

Define
E={(u,v):u,v in B, u!=v, h(u,v,z)=1}.
Let G be the mutual-pair graph on V_E={v:some (u,v) belongs to E}. Let K be its clique complex. Write S={v in V_E:delta(v)=0}, and K_S for the induced clique subcomplex on S. Homology below has coefficients in any fixed field; an empty subcomplex has zero first homology.

The terminal-pair classification identifies H_1(D_0) with H_1(K).

**Theorem.** Under this identification,
ker[H_1(D_0) -> H_1(D)]
=
im[H_1(K_S) -> H_1(K)].

Thus moving the following label kills precisely the old first-homology classes coming from the subcomplex on labels with zero exit status.

**Proof, first inclusion.** Let A be the subcomplex of D_0 consisting of faces whose terminal label before z always belongs to S. Its terminal-label cover consists of the usual contractible sectors C_v for v in S, together with the suffix-clique faces Q_U for cliques U subset S. The same intersection calculation as in [[terminal_ordered_pair_loci_have_the_homotopy_type_of_mutual_pair_clique_complexes]] identifies A with K_S up to homotopy, naturally with respect to the inclusions into D_0 and K. Singleton sectors remain whole: their permitted predecessor may lie outside S.

If S is empty there is nothing to prove. Otherwise the subcomplex C of P(T) whose terminal label always belongs to S lies in D and is contractible by the endpoint-subset theorem.

For an outward face G' in A, its last relevant blocks are U|{z}, with nonempty U subset S. Merge these blocks to obtain M(G'). Every chamber ending in z was already in G'; every other chamber ends in U and has zero exit status. Therefore M(G') is a convex face contained in D. These merges are order preserving. The intersections M(G') intersect C are nonempty, contractible and nested. Contractible-carrier induction maps A into C, with a straight-line homotopy to its original inclusion carried inside the faces M(G'). Therefore A -> D is null-homotopic. Its first-homology image in D_0 lies in the displayed kernel.

**Proof, reverse inclusion.** Suppose c in H_1(K) does not lie in the image of H_1(K_S). Finite-dimensional linear algebra gives a linear functional lambda on H_1(K) that vanishes on that image and has lambda(c)!=0.

Represent lambda by a simplicial 1-cocycle eta on K. Its restriction to K_S is cohomologically zero. Subtract the coboundary of a vertex function extending a primitive on K_S, so that eta actually vanishes on every edge of K_S. In characteristic two the signs below can simply be omitted.

Define a cellular 1-cochain omega on D. Give it value zero except on edges which keep final label z and swap the last two labels u,v immediately before z. Such an edge belongs to D exactly when uv is mutual. Assign its value eta(u,v) when the terminal label before z changes from u to v, with the opposite sign for the reverse orientation.

Check the two-faces:
- A square incident with such an edge has two opposite supported edges with cancelling contributions.
- A hexagon permuting three consecutive labels immediately before the fixed final z can belong to D only when those labels form a clique in G. Its supported edges project to the boundary of that triangle, on which eta sums to zero.
- A hexagon permuting the final three labels {u,v,z} and incident with a supported uv edge belongs to D exactly when delta(u)=delta(v)=0. Necessity follows from h(z,v,u)=1-h(u,v,z)=0 and its u,v interchange. Sufficiency holds because its chambers ending in z use the mutual pair, and its other chambers end in a label with zero exit status. Thus uv is an edge of K_S, and eta(u,v)=0.
No other two-face contains a supported edge. Hence omega is a cocycle on D.

Its restriction to D_0 represents eta under the terminal-pair equivalence. Explicitly, collapsing each contractible terminal-label sector sends a change of terminal label u->v to the edge uv. Faces whose last free block is a clique map into that clique simplex. The supported-edge cochain is exactly the pullback on these one-dimensional changes, and the square and triangle checks give consistency on two-faces. This is also the natural correspondence from the cover proof of the terminal-pair theorem.

Consequently omega evaluates as lambda on H_1(D_0), and evaluates nontrivially on c. Since a cocycle evaluates to zero on boundaries, c cannot map to zero in H_1(D). This proves the reverse inclusion and the formula. QED.

### Scope

The formula determines the kernel, not all of H_1(D), its fundamental group, or its higher homotopy. Vanishing of the old homology image does not by itself prove a null-homotopy.

For a chordless four-cycle, every proper induced subgraph has zero first homology. Therefore any nonzero exit value makes the old H_1 inject into the enlarged locus. When every exit value on B is zero, the stronger endpoint-enlargement theorem makes the entire D contractible.

For a larger graph this gives a precise filter for proposed repairs: cycles supported on labels with zero exit status can be filled by the explicit enlargement, while any old homology class outside their span survives regardless of unspecified tight triples. Further enlargements must address those surviving classes.
