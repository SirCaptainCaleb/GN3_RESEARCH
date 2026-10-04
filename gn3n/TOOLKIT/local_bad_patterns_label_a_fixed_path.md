# Local bad patterns label a fixed path

**Summary:** The forbidden patterns 001, 011, and 0101 admit a reverse-complement-equivariant labeling by oriented edges of one fixed path; any positive zero balance is edgewise.

## Statement

For bad binary status words of length m, the local witnesses 001, 011, and 0101 can be encoded by oriented edges of a fixed path T_m so that reverse-complement reverses the chosen edge. The edge-incidence vectors are nonzero and linearly independent up to orientation, so any positive convex zero requires both orientations of each used edge.

## Body

Let w be a bad binary status word of length m. By [[two_cover_words_avoid_three_local_patterns]], w contains 001, 011, or 0101. A length-three witness starting at i is associated with the pair i and m-1-i; a 0101 witness starting at i is associated with i and m-2-i. Reverse-complement keeps the same unordered pair and reverses the orientation. Ignoring centered self-pairs, the edges from the two reflections i -> m-1-i and i -> m-2-i form one path on start-position coordinates: each coordinate has degree at most two, and composing the reflections moves i to i+1 wherever both are defined. The unique centered self-reflecting witness lies at an endpoint. Replace it by one pendant edge to a new vertex. For odd m, centered 001 and 011 orient that pendant oppositely; for even m, centered 0101 is oriented using any antipodal sign g. Fix an ordering of the path edges. For each bad word choose the first represented edge. If both orientations of that edge occur in the same word, use g to break the tie. This gives a nonzero oriented edge label ell(w) with ell(reverse-complement(w))=-ell(w). Since the incidence vectors of the edges of a tree are linearly independent, any positive relation sum lambda_w ell(w)=0 balances each edge separately. Therefore every used edge occurs in both orientations.

## Metadata

- ID: local_bad_patterns_label_a_fixed_path
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
