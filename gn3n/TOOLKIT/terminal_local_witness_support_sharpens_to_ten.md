# Terminal dual-polarity local-witness support is bounded by ten vertices

**Summary:** In the nearest dual-polarity local-witness reduction, every terminal configuration is centered or overlapping and is supported on at most ten actual vertices.

## Statement

Assume the nearest dual-polarity local-witness reduction reaches a terminal configuration. The disjoint single-sided alternating branch is impossible, and the disjoint single-sided span-two branch is impossible. Therefore any terminal configuration is centered or overlapping; by the dual-polarity reflected-witness bound, its determining support has order at most ten.

## Body

Use the nearest-witness ordering for all six local patterns 001,011,0101,110,100,1010. By [[terminal_alternating_witness_branch_is_impossible]], no disjoint single-sided terminal configuration of alternating type 0101 or 1010 exists. By [[dual_polarity_terminal_span_two_branch_is_impossible]], no disjoint single-sided terminal configuration of span-two type 001,011,110,100 exists. Hence every terminal dual-polarity configuration is centered or has overlapping reflected determining windows. The dual-polarity reduction [[dual_polarity_witness_reduction]] bounds the reflected start separation by at most three for a span-two witness and at most four for an alternating witness. The union of the two determining windows therefore uses at most eight actual vertices in the span-two case and at most ten in the alternating case. Thus every terminal configuration has actual support at most ten. This version deliberately does not use the separate one-polarity two-vertex toggle normal form.

## Metadata

- ID: terminal_local_witness_support_sharpens_to_ten
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
