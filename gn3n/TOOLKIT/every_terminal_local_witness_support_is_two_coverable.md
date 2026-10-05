# Every terminal local-witness support is two-coverable

**Summary:** Every finite terminal support arising from the nearest dual-polarity local-witness reduction has path-cover number at most two.

## Statement

Assume the nearest dual-polarity local-witness reduction has reached any terminal finite support. Then the induced boundary tournament on that support has path-cover number at most two.

## Body

Centered span-two and centered alternating witnesses use at most five and six actual vertices, respectively; partition into subsets of order at most three to obtain a two-cover. By [[dual_polarity_witness_reduction]], reflected double span-two supports have order at most eight and reflected alternating supports have order at most ten. The former are two-coverable by [[eight_vertex_boundary_tournaments_have_two_cover]], and the latter by [[ten_vertex_boundary_tournaments_have_two_cover]]. In the disjoint single-sided branch, [[terminal_alternating_witness_branch_is_impossible]] removes alternating type, [[terminal_local_block_sharpens_to_four]] and [[terminal_span_two_blocks_three_and_four_are_impossible]] reduce span-two type to the two-vertex bridging toggle, and [[terminal_two_vertex_toggle_forces_two_cover]] gives an explicit two-cover. Hence every terminal support in the local-witness reduction is two-coverable.

## Metadata

- ID: every_terminal_local_witness_support_is_two_coverable
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
