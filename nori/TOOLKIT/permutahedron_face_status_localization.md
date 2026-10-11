# Permutahedron face-status averaging and disjoint-window independence

**Summary:** For any ordered-partition face, internal triple-window statuses average to zero; only coordinates adjacent to block boundaries can survive.

## Statement

Let F=B_1|...|B_k be a permutahedron face. If positions i,i+1,i+2 lie in one block, then the average sign status λ_i over all chambers of F is zero. Hence the face-average status vector is supported on at most two coordinates per block boundary.

## Body

# Face-status localization and Boolean independence

Let b(a,b,c) be an arbitrary reversal-odd direction-only boundary 3-tournament label, and put λ_i(π)=+1 for a tight ordered triple in positions (i,i+1,i+2), and -1 otherwise. Let F=B_1|⋯|B_k be a permutahedron face; chambers of F freely permute the elements inside each ordered block.

**Face-average localization.** Whenever three consecutive positions i,i+1,i+2 all lie in one block, the involution swapping the entries at positions i and i+2 stays in F and reverses the sign λ_i. Hence its uniform chamber average is zero. Only windows crossing block boundaries may have nonzero averages, at most two per boundary.

**Joint Boolean independence.** Let I be a family of positions whose length-three position windows W_i={i,i+1,i+2} are pairwise disjoint and each contained entirely within a single block of F. Independently swap the entries at the first and third positions of each W_i. These involutions commute, preserve F, and flip the selected λ_i without changing any other selected λ_j. Consequently the action of (Z/2Z)^I is free on its orbits and realizes each sign pattern exactly once per orbit. The selected status vector is uniform on {−1,+1}^I when chambers of F are uniformly sampled.

**Scope.** These facts require reversal-odd labels of ORDERED COORDINATE TRIPLES, as in ordinary boundary tournaments. They do not assume a global edge order, nor independently establish comparable averaging for arbitrary root-dependent physical-face colorings. Convex balanced packets still require a genuine path-extraction argument.

**Consolidation provenance.** Includes the full flip argument of disjoint_status_windows_form_boolean_cubes; its former record remains archived.

## Metadata

- ID: permutahedron_face_status_localization
- Kind: toolkit
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
