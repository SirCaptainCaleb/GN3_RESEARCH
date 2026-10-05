# Terminalization, reachability, and the exact frontier

**Summary:** The finite line is closed; the grand conjecture now hinges on one global terminalization theorem for balanced local-witness carriers.

## Statement

All finite terminal local-witness configurations are two-coverable. The remaining unresolved step is global terminalization: promote local removal of the innermost witness edge in a balanced carrier to a new balanced carrier supported farther outward, or directly to a spanning two-cover.

## Cold composition

## Terminalization, relative index, and the exact remaining coherence theorem

The finite local-witness line is closed by [[local_witness_topology_and_the_finite_terminal_theorem]]: every terminal centered/overlapping determining support has order at most ten and path-cover number at most two. The remaining issue is global terminalization.

Order the fixed witness-path edges from the center outward:
[
e_1,ldots,e_d,qquad d=m-2,qquad m=n-2.
]
For a bad chamber (pi), write (ho(pi)) for the depth of its selected witness edge. Reversal preserves depth and reverses its oriented label.

### The relative-index mechanism

At depth (r), a protected face is one in which every chamber avoids witness edges (e_1,ldots,e_{r-1}). On the barycentric face poset of the protected region define
[
s_r(F)=
egin{cases}
+1,&F	ext{ contains }+e_r	ext{ and not }-e_r,\
-1,&F	ext{ contains }-e_r	ext{ and not }+e_r,\
0,&	ext{otherwise}.
end{cases}
]
No chain contains both a positive and a negative vertex, so the affine zero set (S_r) is an invariant separator. The standard separator/genus argument gives
[
gamma(S_r)ge gamma(X_r)-1.
]
Thus an equivariant map
[
S_rlongrightarrow X_{r+1}
]
(or to the corresponding existential next-depth face space (Y_{r+1})) is enough to obtain
[
gamma(X_{r+1})gegamma(X_r)-1.
]
Iterating this inequality from (gamma(S^m)=m+1), with only (d=m-2) witness depths, would leave positive genus at the witness-free level and therefore force a spanning two-cover.

So the relative-(mathbb Z_2)-index strategy is sound. The unresolved point is exactly the construction of the separator-to-next-depth map.

### What the finite classification already gives

For a protected mixed face carrying both orientations of (e_r), the audited paired-witness analysis has two branches.

If a face-block boundary separates the determining windows, blockwise splicing stays in the face and produces a chamber whose selected witness is strictly farther outward.

If such splicing is impossible, the dual-polarity terminal classification removes every disjoint single-sided branch. Only centered or overlapping reflected configurations remain, on a determining interval of at most ten actual vertices. The induced boundary tournament on that interval has a two-cover. Reordering the full positional span by such a local two-cover removes every witness (e_j) with (jle r); boundary effects can create only strictly farther-out witnesses. Hence terminal surgery always produces an actual outward spanning order.

This is enough for pointwise escape, but not for literal same-face inclusion.

### The same-face shortcut is false

The terminal branch can genuinely leave the original face. On six vertices, take
[
F={0}mid{1}mid{2,3}mid{4}mid{5},
]
whose chambers are (012345) and (013245). The boundary orientations can be chosen so their status words are respectively
[
0101,qquad 1010.
]
Using the relative order of (2,3) as the antipodal gauge, these are opposite orientations of the centered pendant witness. Thus (F) is a pure balanced one-edge face with no outward chamber in (F). The six-vertex tournament is globally two-coverable, so this is not a counterexample to the grand conjecture; it is a local obstruction to the proposed implication
[
F	ext{ mixed}Longrightarrow F	ext{ itself contains an outward chamber}.
]
Accordingly the earlier cold argument asserting (Sigma_rsubseteq Y_{r+1}) in the terminal branch was too strong.

### Coordinatewise pruning

Because every local-witness label is a signed basis vector, balance is coordinatewise. If
[
sum_{piinmathcal V(F)}lambda_piell(pi)=0
]
and (e_r) is innermost, then the subcollection of chambers of depth (>r) is itself balanced whenever it is nonempty. Thus the only face-level obstruction to even algebraic outward balance is a **pure one-edge carrier**, in which every chamber label is (pm e_r).

This does not by itself create a new positive carrier face: closing the outward subconfiguration under the permutahedron face structure can reintroduce (e_r). But it shows that the genuinely topological part of terminalization is concentrated on pure one-edge behavior.

### Minimal separator faces

A minimal separator face is either an outward chamber or a mixed Coxeter edge.

Indeed, if a minimal separator face contains both (+e_r) and (-e_r) and no outward chamber, every chamber is labeled (pm e_r). The chamber graph of a permutahedron face is connected, so a path from a positive chamber to a negative chamber contains an adjacent sign-flip pair. Their one-dimensional Coxeter face is already mixed; minimality forces the original face to be that edge.

Hence all genuinely terminal separator pathology lives on adjacent-transposition edges. Such an edge is necessarily one of the bounded centered/overlapping terminal transitions, and terminal-support surgery assigns it an outward chamber outside the edge.

Higher separator cells contain no new local terminal types. Their only role is to impose compatibility among these edge surgeries.

### Exact remaining theorem: terminal edge-surgery coherence

The type-(A) Coxeter complex is generated by the rank-two relations
[
s_i s_j=s_j s_iquad(|i-j|>1),
qquad
s_i s_{i+1}s_i=s_{i+1}s_i s_{i+1}.
]
Therefore it is enough to make the outward surgeries on terminal sign-flip edges extend coherently across the square and braid-hexagon residues of the separator.

Swaps supported disjointly from the terminal interval are harmless: they commute with terminal replacement and can change only farther-out witness windows. The only nontrivial residues meet the interior or an endpoint of the bounded centered/overlapping interval.

Thus the grand-conjecture frontier has been reduced to the following finite local statement.

**Terminal edge-surgery coherence lemma.** For every protected terminal sign-flip edge at depth (r), choose an outward replacement chamber equivariantly under reversal. These choices can be made so that on every separator square or braid hexagon the selected outward chambers lie in a contractible next-depth carrier. Equivalently, the edge assignments extend to an equivariant map
[
S_rlongrightarrow Y_{r+1}.
]

Once this lemma is proved, the relative-index inequality iterates through all (m-2) witness depths and forces a witness-free chamber, hence
[
operatorname{pc}(H)le2.
]

No minimum-counterexample or disturbance argument is involved. The remaining work is a bounded Coxeter-coherence analysis around the at-most-ten-vertex terminal support.

## Metadata

- ID: terminalization_reachability_and_the_exact_frontier
- Kind: section
- Version: 5
- Math version: 3
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 3
- Composition stale: False

## Development tree

- [Subsection 1 — Current closure frontier](../SUBSECTIONS/terminalization_reachability_and_the_exact_frontier_subsection_a.md) (`terminalization_reachability_and_the_exact_frontier_subsection_a`; development v3; composition vNone; stale=False)
- [Subsection 2 — Relative-index filtration proves terminalization](../SUBSECTIONS/relative_index_filtration_and_the_mixed_face_outward_push_lemma.md) (`relative_index_filtration_and_the_mixed_face_outward_push_lemma`; development v2; composition vNone; stale=False)
- [Subsection 3 — Global separator filtration and bounded mixed-cell completion](../SUBSECTIONS/global_separator_filtration_and_bounded_mixed_cell_completion.md) (`global_separator_filtration_and_bounded_mixed_cell_completion`; development v1; composition vNone; stale=False)
- [Subsection 4 — Terminal support surgery gives a genuine outward escape](../SUBSECTIONS/terminal_support_surgery_gives_a_genuine_outward_escape.md) (`terminal_support_surgery_gives_a_genuine_outward_escape`; development v1; composition vNone; stale=False)
- [Subsection 5 — Audit of the depth filtration: the remaining same-face gap](../SUBSECTIONS/audit_of_the_depth_filtration_the_remaining_same_face_gap.md) (`audit_of_the_depth_filtration_the_remaining_same_face_gap`; development v1; composition vNone; stale=False)
- [Subsection 6 — Protected-carrier separator and the acyclic-carrier reduction](../SUBSECTIONS/protected_carrier_separator_and_the_acyclic_carrier_reduction.md) (`protected_carrier_separator_and_the_acyclic_carrier_reduction`; development v1; composition vNone; stale=False)
- [Subsection 7 — Coordinatewise pruning and the pure terminal core](../SUBSECTIONS/coordinatewise_pruning_and_the_pure_terminal_core.md) (`coordinatewise_pruning_and_the_pure_terminal_core`; development v1; composition vNone; stale=False)
- [Subsection 8 — A local pure carrier shows same-face escape is false](../SUBSECTIONS/a_local_pure_carrier_shows_same_face_escape_is_false.md) (`a_local_pure_carrier_shows_same_face_escape_is_false`; development v1; composition vNone; stale=False)
- [Subsection 9 — Minimal separator faces and terminal edge-surgery coherence](../SUBSECTIONS/minimal_separator_faces_and_terminal_edge_surgery_coherence.md) (`minimal_separator_faces_and_terminal_edge_surgery_coherence`; development v1; composition vNone; stale=False)
