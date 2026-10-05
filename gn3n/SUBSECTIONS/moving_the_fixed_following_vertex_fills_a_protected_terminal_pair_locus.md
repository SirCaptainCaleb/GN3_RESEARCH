# Moving the fixed following vertex fills a protected terminal-pair locus

## Metadata

- ID: moving_the_fixed_following_vertex_fills_a_protected_terminal_pair_locus
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 136
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Moving the fixed following vertex fills the outward locus

Let B be nonempty, let z not belong to B, and let F be an ordered-partition face with consecutive blocks B|{z}, followed and preceded by fixed source blocks. Let H be obtained by merging B|{z} into the single block B union {z}. Assume:
1. H is protected at depth r;
2. every face of H all of whose chambers end the merged block in a label of B is outward at depth r;
3. D(F)=F intersect X_{r+1} is nonempty.

Here “end” refers to the last position of the merged block, not necessarily the final position of the spanning order. Let C be the subcomplex of H on which that last label belongs to B in every chamber. By (2), C subset X_{r+1}. The endpoint-subset theorem makes C contractible, including the neutral factors of H.

**Theorem.** The inclusion
\[
D(F)\longrightarrow D(H)=H\cap X_{r+1}
\]
is null-homotopic. In particular it extends over the cone on D(F). This fills every component and loop obstruction of the old outward locus at once, with no new vertex labels.

**Proof.** For an outward subface G of F, write its last two relevant blocks as A|{z}, where A is the final block refining B. Let M(G) be obtained by merging A|{z}. Equivalently delete the cut at the fixed position immediately preceding z.

Every chamber of M(G) is outward. If its last merged-block label is z, its order is a chamber of G. Otherwise that label belongs to A subset B, so assumption (2) applies. Thus M(G) is a convex face entirely contained in D(H).

Moreover M is order preserving: if G is a refinement of G', deleting the same positional cut from both leaves a refinement. Define
\[
C(G)=M(G)\cap C.
\]
Within the merged last block A union {z}, this is the prescribed-last-label locus for A. It is nonempty and contractible, times neutral factors. The carriers C(G) are nested.

Consequently a map f from the barycentric subdivision of D(F) into C exists by contractible-carrier induction, carried on a face chain by C(G_max). Let j be the inclusion of that subdivision into D(H). Both j and f map each simplex into the convex face M(G_max), so the straight-line homotopy joins them inside D(H). The map f is null-homotopic because C is contractible. Therefore j, and hence the original inclusion, is null-homotopic. ∎

## Concrete positive-word conditions

One sufficient model retains the terminal-pair window at start a=k-1, where |B|=k, B occupies the first k positions, z occupies position k+1, and the following fixed labels are z_1,z_2,... . Take n>=2k+9 so the reflected determining window is separated.

Assume
\[
h(z,z_1,z_2)=1,\qquad
h(u,z_1,z_2)=0\quad(u\in B),
\]
and all consecutive suffix statuses beginning with (z_1,z_2,z_3) are 0. No condition on h(u,v,z_1) is required.

After merging B and z, the left determining word is
\[
t,\alpha,\delta,\qquad
\delta=1\ \hbox{if the final label is }z,\quad \delta=0\ \hbox{otherwise}.
\]
The next status is 0 and every later status is 0. Hence inward three-status words have form alpha,delta,0 or delta,0,0; none is 001 or 011. Inward four-status words likewise do not equal 0101. The reflected selected-depth occurrence is absent because its statuses are all 0. Thus H is protected. If the merged block ends in B, delta=0 and the selected span-two occurrence is absent. These verify (1) and (2).

Inside F, the selected occurrence is absent exactly when its terminal ordered pair (u,v) satisfies h(u,v,z)=1. The theorem therefore fills any terminal-pair locus C_E, including the chordless four-cycle, under the displayed exit-status conditions. The middle status alpha can vary freely.

## Scope and compatibility

The filling contains the entire old outward locus as its boundary data; it does not discard previously chosen outward chambers. It also does not reverse a tight path. The deformation is carried by explicitly protected convex faces M(G).

This is a local relative extension. Across distinct source faces one still needs compatible enlarged ambient faces H. Fixed positional cut deletion provides an order-preserving construction when the same enlargement positions apply, but existence of the required exit statuses is a combinatorial hypothesis. Boundary antisymmetry alone does not force those statuses.
