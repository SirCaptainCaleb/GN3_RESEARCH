# Terminal local-witness obstructions have support at most twelve

**Summary:** Every terminal obstruction in the nearest local-witness reduction is determined by at most twelve actual vertices.

## Statement

After selecting the nearest local witness in both color directions, centered cases use at most six vertices, reflected double cases at most ten, and a terminal single-sided bridging-block case at most twelve actual vertices.

## Body

Centered witnesses are themselves supported on one determining window, of size five or six. By [[dual_polarity_witness_reduction]], a reflected double occurrence has start separation at most three for a three-bit witness and at most four for a four-bit witness, so the union of its two determining windows has at most eight or ten vertices. In the single-sided terminal case, let the bridging block contribute alpha and beta positions to the two determining windows. [[terminal_local_block_bound]] gives block size at most alpha+beta. Adding the outside portions of two size-five windows gives at most ten vertices; for two size-six windows, at most twelve. Thus every terminal local-witness configuration has actual support at most twelve.

## Metadata

- ID: terminal_local_witnesses_have_twelve_vertex_support
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
