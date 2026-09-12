# Ordered-cover recombination has an exact directed-cycle cost

**Workspace:** D17
**State:** established
**Key:** `cycle-cost-cover-recombination`

**Summary:** A self-contained compiler for two equal-size ordered tight-path covers: locally admissible symmetric-difference flips form preorder upper sets, and cutting every resulting directed cycle yields b-Delta+c paths. Delta>c is a genuine improvement; unlike edge orders, general boundary systems can have bidirectional collision constraints and directed cycles. A shared isolated vertex cannot be absorbed by union-only recombination.

### Statement: recombination with explicit cycle cost
Let F_0,F_1 be two spanning ordered tight-path covers of the same finite vertex set V, each with b components. This lemma requires only a specified predicate on ordered triples of distinct vertices; neither edge-orderability nor boundary antisymmetry is needed. Retain the actual orders.

Encode each adjacency u followed by v as u_out v_in in a bipartite matching M_i. Let C range over the connected components of M_0 symmetric-difference M_1, and set delta(C)=|M_1 intersect C|-|M_0 intersect C|. Then delta(C) is -1,0,1 and their sum is zero.

Choose a bit e_C for every C, selecting the M_1 edges when e_C=1 and the M_0 edges otherwise, and retain common edges. Impose the following local implications. At a physical vertex v with changed incoming and outgoing copies in distinct components I,J, test both mixed predecessor/successor choices. If the incoming-1/outgoing-0 choice gives a bad distinct-vertex turn, impose I<=J. If incoming-0/outgoing-1 gives a bad distinct-vertex turn, impose J<=I. Both implications may occur. Missing predecessor or successor needs no turn test. A choice with predecessor equal to successor is provisionally permitted as a directed 2-cycle and is handled by the cycle cost below.

Let W be an upper set of the generated preorder, let Delta(W)=sum_{C in W} delta(C), and let c(W) count the directed cycles in the physical selected graph, including 2-cycles. Deleting one selected arc from each cycle produces an ACTUAL spanning tight-path cover with exactly
  b - Delta(W) + c(W)
components. Thus Delta(W)>c(W) strictly improves the original cover. For spanning three-covers it gives a spanning cover by at most two paths.

### Complete proof
A union of two matchings has alternating path and even-cycle symmetric-difference components. Each component can independently take either matching, so all bit choices remain matchings and the selected arc count is |V|-b+Delta(W).

At v, if either copy is unchanged, each possible local pair is already present in one original cover and is safe. If both copies belong to the same alternating component, they receive the same bit and again reproduce an original local pair. For distinct components, equal bits are safe and the two mixed choices are precisely those tested. The generating implications forbid exactly the bad mixed choices. Therefore upper sets are exactly the assignments with no bad distinct-vertex turn.

The physical graph has indegree and outdegree at most one and no loops. Its components are directed paths, isolated vertices or directed cycles. In cycles of length at least three all consecutive distinct-vertex turns are tight by the local test. A 2-cycle has no distinct-vertex turn to test. Removing one arc from each cycle gives vertex-simple directed paths: all their consecutive triples were already certified, and a broken 2-cycle is a vacuously tight dimer. Removing arcs creates no new adjacency and hence requires no new junction assumption.

After the c(W) removals the graph is a spanning directed linear forest with |V|-b+Delta(W)-c(W) arcs. Its number of components is |V| minus its arc count, proving the formula. In particular all output orders are reconstructed simply by traversing the selected paths and the cycles from just after their chosen deleted arc.

For a fixed locally admissible selected graph, c(W) deletions are also necessary if the only permitted repair is arc deletion: every vertex-disjoint directed cycle must lose an arc. Thus the stated cost is exact for this compiler, not a lower bound on arbitrary repairs using new arcs.

### Why the edge-ordered specialization is stronger
For increasing paths, two mixed local inequalities cannot both fail, and strict increase of edge labels rules out every directed cycle, including a 2-cycle using the same underlying edge twice. Hence c(W)=0 and the criterion reduces to the pending R980 positive-upper-set criterion. In a general tight-turn system neither simplification may be assumed. The present proof is self-contained and does not use R980 as a premise.

### Exact obstruction and fixed-fiber fence
If the minimum tight-path-cover number on V is b, then EVERY upper set in EVERY such comparison satisfies Delta(W)<=c(W), since otherwise the constructed cover contradicts minimality. This is a necessary nonimprovement inequality, not a contradiction or a gain-existence theorem.

The construction introduces no arc outside M_0 union M_1. In particular a vertex isolated in both inputs remains isolated in every output, including after cycle cuts. Therefore comparing two covers of the same singleton-deletion residue and adjoining the same omitted singleton cannot absorb that singleton by this compiler alone. For the full theorem, compare spanning three-covers from different deleted labels, or explicitly supply new arcs by a separate construction. Same-fiber comparisons remain useful for reordering and redistribution but do not evade this fence.

Status: complete new internal proof, unreviewed exposition. No existence of an upper set with surplus Delta-c>0 is claimed. The physical cycle list and actual output paths are part of the interface; a positive edge gain alone is insufficient.

## References

```json
[
    {
        "relation": "related",
        "revision_id": "R980"
    }
]
```
