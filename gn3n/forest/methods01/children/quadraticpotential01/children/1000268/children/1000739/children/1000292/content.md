# All-equal three-cover endpoint probes always expose scale-free disturbance

## Statement

Let H be a minimum counterexample and let A|B|C be a spanning three-cover with |A|=|B|=|C|. Probe the two displayed endpoints of A by arbitrary two-covers of their vertex deletions, and count crossings relative to the inherited three-part partitions as in e30f76549e23. Then at least one of the following holds: (1) one endpoint-deletion cover has at least two ordinary three-part crossings; (2) the two endpoints of A are both noninsertable into the same displayed opposite block, so the universal paired-noninsertion theorem a8c9883902b1 supplies its fixed five-way local structural alternative; (3) one of the sparse endpoint-deletion Hamilton orders has explicit relative-order disagreement with an inherited displayed block. Thus the all-equal quadratic plateau has no order-neutral sparse residue.

## Body

Apply e30f76549e23. If one endpoint probe has at least two crossings, outcome (1) holds. Otherwise both probes have exactly one crossing. If they isolate the same opposite block, e30f76549e23 makes both endpoints noninsertable into that block and a8c9883902b1 gives outcome (2). If they isolate different opposite blocks, e30f76549e23 gives the crossed unique-crossing near-merge configuration. The crossed-splice lemma then forces relative-order disagreement in one of the two sparse Hamilton orders, giving outcome (3). These alternatives are independent of the common component order.
