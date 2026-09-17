# Every arbitrary three-forest recompletion factors through at most two one-edge transfers or leaves a bounded overlap nucleus

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-arbitrary-recompletion-two-edge-or-bounded-nucleus`

**Summary:** Let F=C1|C2|C3 and G=D1|D2|D3 be literal maximum spanning three-forests in a hypothetical smallest counterexample. Form the 3-by-3 support-incidence graph I(F,G), with one edge for every nonempty cell C_i intersect D_j. If I contains a cycle, a shortest cycle is C4 or C6 and choosing one physical vertex from each cyclic cell gives a bounded support-overlap nucleus on at most six vertices. Assume I is acyclic. If any intersection cell occurs in more than one interval along one of its two rail words, one obtains a bounded repeated-crossing certificate from the two successive cross-cell seams surrounding a return to that cell. Otherwise every cell is a contiguous tight subpath in both F and G. Compare the two Hamilton words on each cell by accepted R435; unless an adjacent reversal, reverse trimer, or proper cycle is emitted, the two cell words are literally identical. Let e be the number of nonempty cells. A support-changing acyclic incidence graph has e=4 or 5. With synchronized cell words, F and G share every internal cell edge; F has exactly e-3 old cross-cell seams and G exactly e-3 new seams, and no seam is common. If e=4 they differ by one selected edge and are directly a support-changing one-edge transfer. If e=5, write old seams o1,o2 and new seams n1,n2 and test H=(common internal edges)+{o2,n1}. The seam-incidence union is a tree. If o2,n1 compete for a vertex copy, R3 gives a proper current trimer. If their only genuinely mixed physical turn is bad, R3 again gives a proper current reverse trimer. Otherwise H is an acyclic locally tight matching with n-3 edges, hence a literal maximum three-forest, and F->H->G consists of two reversible support-changing one-edge transfers. Thus every non-one-edge recompletion is absorbed into the already simply-connected one-edge sector unless it exposes one of four explicit nuclei: C4/C6 support incidence, repeated rail crossing, same-cell R435 geometry, or a current mixed-seam trimer. In particular the generic component-recompletion portal has no unbounded hidden combinatorial type.

### 1. Two maximum forests and their support-incidence graph
Let H be a hypothetical smallest counterexample and retain two literal maximum spanning three-forests

  F=C_1|C_2|C_3,
  G=D_1|D_2|D_3.                                         (RF.1)

The displayed C_i,D_j are actual oriented tight paths, and their physical supports partition V(H).

Form the bipartite SUPPORT-INCIDENCE graph I=I(F,G) on left vertices C_1,C_2,C_3 and right vertices D_1,D_2,D_3. Join C_i to D_j exactly when the physical intersection

  S_{ij}=V(C_i) intersect V(D_j)                         (RF.2)

is nonempty. Call every nonempty S_{ij} a CELL. Since both triples are partitions into nonempty supports, I has no isolated vertices.

If the two unordered support partitions are equal, I is a perfect matching and the transition lies in the fixed-support fiber already compressed by SV35882. Hence below assume the support partition changes.

### 2. Any incidence cycle is already a bounded physical overlap nucleus
Suppose I contains a cycle. Since I is a simple bipartite graph with only three vertices on each shore, a shortest cycle has length four or six. Retain that shortest cyclic list of cells and choose one physical vertex from each cell. Different cells are disjoint, so these are four or six distinct physical vertices.

This gives a bounded COMPONENT-OVERLAP NUCLEUS: an alternating C_4 or C_6 in old/new component ancestry with one named physical representative in every incidence cell. No tight-path adjacency is asserted between those chosen vertices; this is a support-ancestry certificate, not a graph-intrinsic tight cycle.

Thus every recompletion with cyclic support incidence has already reduced to a physical nucleus of order at most six. The remaining argument assumes I is acyclic.

### 3. Acyclic support change has only four or five nonempty cells
Let e=|E(I)| be the number of nonempty cells and c the number of connected components of I. Because I is a forest on six nonisolated vertices,

  e=6-c <=5.                                             (RF.3)

Also e>=3. If e=3, no isolated vertices force I to be a perfect matching, so the support partitions are equal up to relabeling. Since we assumed genuine support change,

  e in {4,5}.                                             (RF.4)

This already removes arbitrary large component-incidence patterns from the non-one-edge problem.

### 4. Noncontiguous cells give a bounded repeated-crossing certificate
Fix one literal rail, say C_i, and color each of its vertices by the new component D_j containing it. If some cell S_{ij} is not one contiguous interval of the C_i word, then the color word returns to j after visiting another color. Choose the first such return. At the two block boundaries retain the selected cross-cell states

  u -> v,
  w -> z,                                                 (RF.5)

where u,z lie in S_{ij} and v,w lie outside it; if the middle block is a singleton then v=w, otherwise all four displayed boundary vertices are distinct. These are actual selected states of the one literal rail C_i.

Thus a noncontiguous cell yields a REPEATED-CROSSING NUCLEUS on at most four named seam vertices, together with their two cell ancestries and the retained rail order. The dual statement applies to every D_j rail.

Henceforth assume EVERY nonempty incidence cell is contiguous in each of the two literal rails in which it occurs.

### 5. Outside R435, every cell has one common literal path word
For a nonempty cell S=C_i intersect D_j, contiguity gives two actual tight Hamilton paths on S: the restriction P_S of the C_i word and the restriction Q_S of the D_j word.

Compare P_S and Q_S using accepted Reverse Ear R435. If the words differ, then some consecutive Q_S pair occurs in decreasing P_S order. The exact same-support specialization of R435 gives one of its explicit outputs: an adjacent selected reversal, a reverse tight trimer, or a proper tight cycle. Retain that exact physical output and its cell ancestry.

If no R435 output occurs on any cell, monotonicity forces

  P_S = Q_S                                               (RF.6)

as literal oriented vertex words for EVERY cell S. Singleton cells satisfy this trivially.

Thus outside the R435 portal branch, F and G have identical selected edges INTERNAL to every incidence cell. All remaining difference lies in the seams joining consecutive cells along the three old and three new rails.

### 6. The old/new seam union is itself a forest
At an old component C_i of incidence degree d_i, its d_i nonempty cells occur as contiguous blocks along the literal C_i path. Exactly d_i-1 selected edges of F cross between consecutive cells. Summing over the three old rails gives

  |O|=sum_i(d_i-1)=e-3,                                  (RF.7)

where O is the set of OLD cross-cell seams. Likewise the new forest has a set N of NEW cross-cell seams with

  |N|=e-3.                                               (RF.8)

No seam belongs to both O and N. Indeed an old seam joins two distinct cells sharing one old component; if the same physical seam were new as well, those two cells would also share one new component, contradicting that they are distinct cells.

Contract every common cell path to one atom and draw an abstract edge for every seam in O union N. Call this seam graph Lambda. Inside each connected component of the incidence forest I, the cell-atoms are connected by the old/new seam paths around the incident old/new component vertices. Hence Lambda has exactly c connected components. It has e atom vertices and

  |E(Lambda)|=2(e-3)=2e-6=e-c                       (by RF.3). (RF.9)

Therefore Lambda is a FOREST. This is the order-sensitive version of acyclic component ancestry: once the cell words synchronize, the complete old/new seam interaction contains no hidden support cycle.

### 7. Four cells give one literal one-edge transfer
If e=4, equations (RF.7)-(RF.8) give one old seam o and one new seam n. All internal cell edges agree, so

  M(G)=(M(F)-{o}) union {n}.                              (RF.10)

Both endpoints are literal maximum forests. Hence F<->G is itself one exact reversible one-edge transfer. Since the support partitions differ, it is support-changing.

Thus an acyclic four-cell recompletion is already inside the completed one-edge sector.

### 8. Five cells factor through two one-edge transfers unless one mixed seam emits a trimer
Now e=5. Write

  O={o_1,o_2},
  N={n_1,n_2}.                                            (RF.11)

The seam graph Lambda is a tree on the five cell-atoms. Form the mixed selected-edge set

  M_* = (all common internal cell edges) union {o_2,n_1}. (RF.12)

Equivalently, M_* is obtained from F by deleting o_1 and adding n_1. It has exactly |V(H)|-3 selected edges.

Each of o_2 and n_1 is separately compatible with every internal cell edge, because o_2 occurs in F, n_1 occurs in G, and the internal cell words are common. Therefore the only possible bipartite-matching failure in M_* is direct vertex-copy competition between o_2 and n_1. If they share one out-copy, write them v->x and v->y with x!=y; if they share one in-copy, write them x->v and y->v. Boundary antisymmetry R3 makes one of the two complete-reversal trimers on x,v,y tight. This proper trimer is graph-intrinsic and accepted R4 currentizes it.

Assume no such competition, so M_* is a matching. Every physical turn using at most one of {o_2,n_1} is inherited from F or G. The only genuinely mixed turn can occur where the two seams meet at one cell endpoint. The outside vertices then lie in two distinct incidence cells, hence are physically distinct. If that mixed turn is bad, R3 gives the exact reverse tight trimer, again current by R4.

Assume the mixed turn is tight as well. Then every selected turn of M_* is tight. A physical directed cycle is impossible: after contracting the common cell paths it would project to a cycle in the two-edge subgraph {o_2,n_1} of the seam forest Lambda. Thus M_* is a spanning tight path forest. With n-3 selected edges it has exactly three components, so it is a literal maximum spanning three-forest; call it F_*.

Now

  F  <->  F_*  <->  G                                   (RF.13)

consists of two exact reversible one-edge transfers:

  F -> F_* deletes o_1 and adds n_1,
  F_* -> G deletes o_2 and adds n_2.                      (RF.14)

Both transfers are support-changing. The first contains a new seam n_1 joining cells from different old components, so its support partition cannot equal F's; dually F_* retains an old seam o_2 joining cells from different new components, so its support partition cannot equal G's.

Hence every acyclic five-cell recompletion either emits one current trimer in the single mixed-seam test or factors into TWO support-changing one-edge transfers.

### 9. Universal recompletion factorization theorem
Combining the preceding sections, EVERY transition between literal maximum spanning three-forests satisfies one of the following parent outcomes.

- FIXED SUPPORT: the unordered support partition is unchanged and the transition lies in the exact FIBER-REORDER compression of SV35882.
- INCIDENCE NUCLEUS: I(F,G) has a physical C_4 or C_6 support-overlap certificate on at most six named vertices.
- REPEATED-CROSSING NUCLEUS: one incidence cell reappears along a literal rail, giving two named opposite cell-crossing seams on at most four boundary vertices.
- R435 CELL PORTAL: two contiguous realizations of one common cell disagree in order and emit an adjacent reversal, reverse trimer, or proper cycle.
- MIXED-SEAM TRIMER: after cell-word synchronization, the sole candidate mixed-seam intermediate fails by copy competition or one bad mixed turn, giving a current R3/R4 trimer.
- ONE-EDGE FACTORIZATION: the recompletion is one support-changing one-edge transfer when e=4, or factors through two such transfers when e=5.

The first item is fiber-compressed. The last item lies entirely in the portal-relative triangle-square simply connected sector of SV39912. The R435 same-support birth ancestry is already edge-generated in SV39669. Therefore an arbitrary non-one-edge COMPONENT RECOMPLETION has no unbounded residual combinatorial species. Outside already-named R435/trimer portals it either collapses to at most two one-edge exchanges or leaves one of TWO bounded physical overlap nuclei: a C_4/C_6 component-incidence circuit or a repeated-crossing seam pair.

This is the desired parent contraction for the G15 exchange-structure lane. It does not yet consume those two bounded overlap nuclei, nor does it assert that arbitrary portal-conversion ancestry is flat. But any surviving nontrivial monodromy must now pass through one of those bounded nuclei or through a named trimer/cycle/reversal portal; arbitrary large 3-to-2 recompletion is no longer a primitive obstruction.
