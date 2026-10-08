# A two-root Radon zero in one carrier cell contains the needed Coxeter swap direction

## Metadata

- ID: a_two_root_radon_zero_in_one_carrier_cell_contains_the_needed_coxeter_swap_direction
- Parent Section: directed_nor_union_closed_bridge
- Position: 228
- Row version: 2
- Development version: 2
- Composition version: 2
- Composition stale: False

## Composition

Opposite physical window-slide roots in one ordered-partition cell force their endpoints into a common tied block. Locality strengthens this to a block containing the full r+1-coordinate packet. Refinement making the endpoints adjacent cannot preserve the same r-window-slide root for r≥2. The valid extraction interface is a packet-sized move with its descent certificate and crossing collars retained; explicit packet reversal reverses the root while preserving 10.

## Development

Common-cell extraction for a two-root protected Radon zero. Assume the protected root map is realized on a permutohedral/switch-prism cell complex in which each cell is indexed by an ordered partition of the physical coordinates and its chamber vertices are linear extensions of that partition. Suppose an affine zero in one cell is supported by exactly two opposite window-slide roots rho=e_a-e_c and -rho=e_c-e_a, attached to two chamber states of that same cell. The first root certifies a protected descent whose dropped coordinate a lies on the left side of its local cut and entering coordinate c on the right; the opposite root arises at a chamber where the physical relative order of a and c is reversed. Since both chambers refine the same ordered partition, a and c must belong to one common tied block: coordinates in distinct ordered blocks have fixed relative order throughout the cell. Hence the carrier face contains the Coxeter direction which interchanges a and c. After fixing an ordering of all other coordinates in the tied block with a and c adjacent, that direction is represented by an actual adjacent-swap chamber edge. Therefore the only missing ingredient for extracting a legal protected path from a two-root Radon zero is certificate persistence under refinement of the other tied coordinates. If the 10 descent labels of the two endpoint chambers restrict to that adjacent-swap edge, the two-cycle immediately becomes a genuine complementary/protected edge. This isolates the base-case compatibility problem: not topology of the face, but preservation of the local descent certificate while freezing unrelated tied coordinates.

Unification audit: actual r-window slide endpoints are r positions apart. Their common tied block therefore contains the entire r+1-coordinate packet. Refining to a chamber edge with those endpoints adjacent destroys the same physical root certificate for r≥2. The tied-block direction is valid geometry; extraction should retain a packet-sized block. The new packet-reversal theorem gives an explicit full-support move that reverses the root and preserves its actual 10 descent, with an exposed r−1-window collar on each side.
