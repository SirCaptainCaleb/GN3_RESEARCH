# A mutually admissible exterior vertex fills the terminal-pair carrier — preserved pre-item development

## Composition

(none yet)

## Development

## One exterior vertex fills a terminal-pair carrier

Let B be a finite set with |B|>=2, E a loopless directed relation on B, and g not in B. Let E^+ on B^+=B union {g} restrict to E on B and satisfy
\[
(u,g),(g,u)\in E^+\qquad(u\in B).
\]

**Lemma.** The terminal-pair locus C_{E^+} in P(B^+) is nonempty and contractible. Moreover the inclusion of C_E in the facet {g}|B extends over the cone on C_E. Any map from a sphere into this copy of C_E is null-homotopic in C_{E^+}.

**Proof.** Every vertex of B^+ is an active terminal label, and g is adjacent to every other vertex of the mutual-pair graph. Its clique complex is therefore a cone with apex g. The exact terminal-pair locus theorem [[terminal_ordered_pair_loci_have_the_homotopy_type_of_mutual_pair_clique_complexes]] gives contractibility.

Embedding P(B) in the facet {g}|B preserves the final ordered pair, so the embedded C_E is a subcomplex of C_{E^+}. Compose its inclusion with a contraction of C_{E^+}; this defines the required cone extension. The assertion for sphere maps follows. ∎

This lemma simultaneously joins previously disconnected terminal-label components and fills all their loops. It is stronger than choosing a single successful chamber.

## A protected-window version

Suppose a determining window has variable first two labels u,v from a source block B and three fixed labels z,z_1,z_2. Assume its status word is
\[
h(u,v,z),1,1,
\]
so its positive span-two occurrence is absent exactly when h(u,v,z)=1.

Let a singleton exterior vertex g be immediately before B, and let H be the ordered-partition face obtained by merging {g}|B into B^+. Assume:

1. h(g,z,z_1)=1, so the second determining status remains 1 for every new last label;
2. for every u in B,
\[
h(u,g,z)=h(g,u,z)=1;
\]
3. all determining statuses for smaller witness depths remain equal to their protected source values on H;
4. the reflected depth-r occurrence is absent throughout H, and no other depth-r condition remains except this terminal-pair test.

Then H is protected, and its outward locus D(H)=H intersect X_{r+1} is C_{E^+} times the neutral factors, where E consists of the pairs with h(u,v,z)=1. It is therefore a contractible protected target containing D(F) in the original facet {g}|B.

**Proof.** Conditions (1) and the fixed third status make the selected word t11 for every chamber of H. Hence the selected occurrence is absent precisely for terminal pairs in E^+. Conditions (2) give the mutual universal vertex g in its allowed-pair graph. Conditions (3) and (4) establish the claimed protectedness and rule out additional inward or selected-depth tests. The factor identification and the first lemma complete the proof. ∎

Condition (3) is an explicit protection obligation, not an inference from the pair graph. In the model of [[arbitrary_terminal_pair_relations_occur_on_protected_zero_faces]], all inward statuses after the variable pair are 1,1,0,...,0. When the enlarged block continues to occupy only the first two window positions, condition (1) and the fixed suffix preserve that inward status pattern; earlier block-internal changes lie farther outward.

The right-end/initial-pair version follows by reversing orders and complementing boundary statuses.

## Relative carrier use

For a chosen ambient protected face H satisfying the hypotheses, all source subfaces whose outward images lie in D(F) also lie in D(H). Taking this same D(H) as their enlarged target fills their entire local face-poset cone, including the forced cycle of [[saturated_natural_carriers_force_their_outward_loci_to_be_contractible]]. This directly addresses the missing point and loop extensions.

For a global construction, if chosen ambient faces H(F) satisfy H(G) subset H(F) for G subset F, then the enlarged carriers D(H(F)) are naturally nested. Contractibility then supplies all simplex extensions. Choosing g independently on neighboring source faces does not establish this nesting; that compatibility remains a separate theorem.

No existence of such an exterior vertex is claimed from boundary antisymmetry alone. The new conclusion is a precise sufficient local mechanism: a vertex satisfying the two ordered-pair tests and the protection test removes every topological obstruction of that pair factor.
