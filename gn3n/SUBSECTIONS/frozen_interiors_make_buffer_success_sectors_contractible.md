# Frozen interiors make buffer-success sectors contractible

## Metadata

- ID: frozen_interiors_make_buffer_success_sectors_contractible
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 109
- Row version: 3
- Development version: 2
- Composition version: 1
- Composition stale: False

## Cold composition

### Contractible one-boundary sectors

Freeze the interior of a double-persistent corridor and vary one boundary reservoir. For any prescribed nonempty set of endpoint labels that give a successful outward buffer, the corresponding chambers form a contractible subcomplex of the boundary permutahedron. Hence one-boundary success sectors require no further topological obstruction theory; difficulty remains only when the boundary reservoir is uniformly blocked.

## Development

## After freezing the interior, buffer-success sectors have natural contractible carriers

Retain a double-persistent protected face (Fsubset X_r) and its full reflected determining span (J). By [[double_persistent_faces_have_bounded_block_width_and_rank_one_span_boundaries]], every block wholly inside the long inward corridor has bounded order, while a block straddling an outer boundary of (J) may be large but occupies at most two determining-window positions.

Collapse every source-face block meeting the interior of (J), and fix one reference ordering of the vertices occupying the interior determining positions. At the left endpoint, retain only the freedom of the boundary block (B) that determines which label occupies the single outer buffer position (z) immediately outside the frozen span. In particular the first two corridor vertices
[
c_1,c_2
]
are fixed.

Define
[
S={vin B:h(v,c_1,c_2)=1}.
]

Whenever (zin S), the left buffer replacement of [[outward_buffer_vertices_bypass_the_internal_two_deletion_obstruction]] gives an outward repair while the frozen interior order is unchanged.

**Lemma (contractible successful-buffer sector).** The subcomplex of the (B)-permutahedron on which every chamber has its boundary vertex in (S) is empty if (S=arnothing), and contractible if (S
earnothing).

**Proof.** Depending on whether the retained buffer position is the first or last position of the block, this is exactly the prescribed-first-vertex or prescribed-last-vertex locus of [[prescribed_endpoint_subsets_of_a_permutahedron_give_contractible_outward_loci]]. (square)

Taking the product with every retained exterior neutral factor preserves contractibility. Since the interior determining span is frozen, every chamber in this target carrier uses the same successful buffer mechanism and hence lies in (X_{r+1}). Using the inherited-mask convention of [[frozen_window_carriers_and_separator_relabeling_require_precise_invariants]] makes these carriers nested on subfaces of the chosen ambient face.

The right boundary is symmetric.

### Consequence

For the double-persistent zero-root locus, one-variable endpoint variation separates into two qualitatively different sectors.

1. **Successful-buffer sector.** At least one allowed boundary label belongs to (S). The entire family of successful choices has a natural contractible protected carrier; no packet gluing is needed there.

2. **Uniformly blocked sector.** (S=arnothing). Then
   [
   h(z,c_1,c_2)=0
   ]
   for every allowed boundary label (z), hence
   [
   h(c_2,c_1,z)=1
   ]
   for all of them. This is exactly the common-reverser structure of [[a_blocked_outward_buffer_creates_a_boundary_straddling_common_core_packet]] and, when enough labels are available, activates the local parallel-middle and packet-extension lemmas.

Thus the carrier problem need not mix successful and failed choices at a one-variable endpoint. The successful part is topologically automatic after freezing the interior; all genuinely new combinatorics is concentrated in the uniformly blocked endpoint sector.

This statement deliberately does **not** say that the full boundary block has rank one. The block may contain arbitrarily many labels; only one determining slot is being retained as variable in this sector. If two determining slots from the same boundary block must remain variable simultaneously, a separate ordered-pair locus theorem is needed.

Nor does this prove that every double-persistent face has a successful buffer. If both endpoints are uniformly blocked, the remaining theorem is the bounded rooted packet/endpoint-control problem on top of the frozen long corridor.
