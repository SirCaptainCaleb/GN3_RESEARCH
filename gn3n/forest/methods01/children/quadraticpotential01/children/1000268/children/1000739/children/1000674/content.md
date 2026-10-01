# All unique-crossing endpoint-probe branches on an equal three-cover force order disagreement

## Statement

Let H be a minimum counterexample and A|B|C an all-equal spanning three-cover. If the deletion covers chosen for both endpoints a_1,a_r of A each have exactly one crossing relative to (A-{d})|B|C, then the resulting deletion-cover data contain explicit relative-order disagreement. Consequently, for the two endpoint probes, either at least one probe has at least two crossings or relative-order disagreement is already present.

## Body

By e30f76549e23, each unique-crossing endpoint probe isolates B or C and its other component is a near-merge Hamilton path. If both probes isolate the same opposite block, the same-isolate lemma forces relative-order disagreement. If they isolate different opposite blocks, the crossed-splice lemma already proved that simultaneous inherited-order preservation would splice to a spanning two-cover, so relative-order disagreement is forced there as well. These exhaust the unique-crossing possibilities.
