# Every pair of support-changing one-edge generators gives a square, an augmentation, or a current trimer/cycle portal

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-support-changing-one-edge-complete-diamond`

**Summary:** Complete the G14 one-edge diamond target. Let F be a literal maximum three-forest and let tau_1,tau_2 be two distinct reversible one-edge exchanges from F whose unordered support partitions genuinely change. First, distinct support-changing exchanges cannot have the same added directed edge b: matching forces a unique deleted edge whenever one endpoint copy of b is occupied; if both are free, b joins a terminal to a source, and either the two rails are distinct, where the one-bad-seam SLIDE mechanism gives a unique deletion, or they are the same rail, where deleting a rim edge only rebreaks one cycle and preserves the support partition. Hence b_1!=b_2. If the deletions are distinct and the simultaneous replacement is a matching, SV38699 gives a verified exchange square or a current reverse-trimer/shared-cycle portal. If the simultaneous replacement is not a matching, the two distinct added edges share one out-copy or one in-copy, so on their three physical endpoints R3 gives one of the two complete-reversal trimers; R4 currentizes it. If the two generators delete the same old edge, applying both additions after that one deletion has one more selected edge than F. A matching-compatible, locally tight, acyclic double addition is therefore a spanning two-cover. Any bad mixed turn again gives a current reverse trimer; any physical cycle must contain both added edges, hence is unique and proper and gives a current movable-break cycle portal. Thus every pair of genuine support-changing one-edge generators satisfies exactly the desired local relation: SQUARE, TWO-COVER AUGMENTATION, CURRENT TRIMER, or UNIQUE SHARED CURRENT CYCLE. After quotienting same-support fiber/cycle reorders, there is no remaining pairwise one-edge base obstruction. Marked holonomy is correspondingly reduced to transport coherence around verified squares and to the existing trimer/cycle portal consumers.

### 1. Genuine one-edge generators
Let H be a hypothetical smallest counterexample and let

  F=P_1|P_2|P_3

be a literal maximum spanning three-forest with directed bipartite selected matching M. Thus

  |M|=|V(H)|-3.

A ONE-EDGE TRANSFER from F is a literal maximum three-forest F' whose matching has the form

  M'=(M-{a}) union {b},                                (CD.1)

where a is one selected directed edge of F and b is one directed edge not selected by F. The transfer is SUPPORT-CHANGING when the unordered three-set support partition of F' differs from that of F.

Retain two distinct reversible support-changing one-edge transfers

  tau_i=(a_i -> b_i),   i=1,2,                         (CD.2)

with endpoint forests F_i. All physical directed edges and literal path words are retained.

The purpose is to classify the interaction of these two generators completely.

### 2. A support-changing generator is determined by its added edge
Fix one directed edge

  b=u->v

not selected by F, and suppose (CD.1) is a literal maximum forest. In the matching M, if u_out is already matched by an old edge c, then matching compatibility forces a=c. Likewise, if v_in is already matched by an old edge d, then a=d. In particular both endpoint copies cannot be occupied by two distinct old edges, because one deletion would not free both.

Thus nonuniqueness of the deleted edge for a fixed b can occur only when both u_out and v_in are unmatched in F: u is a terminal of one F-rail and v is a source of one F-rail.

If u and v lie on the SAME F-rail, adding b closes that rail to a directed cycle. Any one-edge deletion which restores a path forest must break that same cycle. The vertex support of the rail is unchanged and the other two rails are untouched. Hence every resulting transfer is same-support CYCLE-ROTATE / rebreak geometry, not a support-changing generator.

If u and v lie on DISTINCT F-rails, b is exactly a physical terminal-to-source merge seed. The root-gate mechanism of SV22098 applies. If both merge turns are tight, adding b without deleting anything gives a spanning two-cover, impossible. If both are bad, one deletion cannot remove both bad root states, so no one-edge transfer exists. If exactly one is bad, the unique valid deletion is the unique old boundary edge responsible for that bad turn. This is precisely the reversible SLIDE of SV22098.

Therefore a fixed added edge supports AT MOST ONE support-changing one-edge transfer. Since tau_1,tau_2 are distinct,

  b_1 != b_2.                                           (CD.3)

This is the only place where same-added-edge ambiguity occurs: it belongs entirely to the same-support cyclic-break fiber already quotiented by the current marked-holonomy normal form.

### 3. Distinct deletions: matching-compatible pairs satisfy the existing diamond theorem
First suppose

  a_1 != a_2.                                           (CD.4)

If the simultaneous replacement

  M_*=(M-{a_1,a_2}) union {b_1,b_2}                    (CD.5)

is a bipartite matching, apply the exact current unit SV38699. It proves one of:

  (i) M_* is a literal maximum three-forest F_12 and
      F-F_1-F_12-F_2-F is a verified exchange square;

  (ii) one genuinely mixed turn is bad, so R3 gives a named graph-intrinsic reverse trimer and R4 currentizes it;

  (iii) all mixed turns are tight but M_* has one unique proper directed tight cycle containing both added edges, hence a current shared movable-break cycle portal.          (CD.6)

Thus nothing remains in the matching-compatible distinct-deletion case.

### 4. Distinct deletions: vertex-copy competition is itself a trimer portal
Assume (CD.4), but M_* is NOT a matching. Each M_i is separately a matching, and all old conflicts involving b_i are removed by its own deletion a_i. Because both old deletions are performed in (CD.5), the only possible remaining matching failure is mutual competition of b_1 and b_2. By (CD.3) the two added edges are distinct.

Hence either they share one out-copy,

  b_1=v->x,   b_2=v->y,   x!=y,                        (CD.7)

or they share one in-copy,

  b_1=x->v,   b_2=y->v,   x!=y.                        (CD.8)

In both cases the three physical vertices x,v,y are distinct. Boundary antisymmetry R3 applied to the complete-reversal pair

  (x,v,y),   (y,v,x)                                    (CD.9)

makes exactly one of them tight. Therefore every vertex-copy competition emits a literal graph-intrinsic tight trimer on the two competing destinations/sources and their shared physical endpoint.

The trimer is proper in a smallest counterexample. Accepted R4 gives an exact two-cover of its complement, so it is immediately current as one rail of a literal maximum spanning three-forest.

Thus the sole residue left open by SV38699 is not a new generator relation at all: it is a CURRENT TRIMER PORTAL.

### 5. Common deletion: the clean double addition augments to two paths
It remains to suppose

  a_1=a_2=a.                                             (CD.10)

By (CD.3), b_1 and b_2 are distinct. Form the simultaneous double addition after the one common deletion:

  M^+=(M-{a}) union {b_1,b_2}.                          (CD.11)

This has

  |M^+|=|M|+1=|V(H)|-2.                                (CD.12)

If M^+ is not a bipartite matching, the failure is again mutual competition of b_1,b_2, and Section 4 gives the current trimer portal.

Assume M^+ is a matching. Every local predecessor-successor turn selected by M^+ is inherited from F_1 or F_2 except a genuinely mixed turn using one side from each added edge. If such a three-distinct-vertex mixed turn is bad, R3 reverses it to a named tight trimer and R4 currentizes it. A mixed physical backtrack is already a directed 2-cycle and belongs to the cycle branch below.

Assume all mixed turns are tight. Then M^+ is a directed tight pseudoforest. If it has NO directed cycle, it is a spanning tight path forest with |V(H)|-2 selected edges, hence EXACTLY TWO path components. This is a spanning two-cover of H, contradicting counterexamplehood. Thus a clean common-deletion pair would close O4 immediately.

### 6. Common deletion cycle debt is unique and shared
Suppose instead that M^+ contains a directed physical cycle C. The cycle cannot avoid b_1, because then it would already occur in

  M_2=(M-{a}) union {b_2},

which is the forest F_2. Likewise C cannot avoid b_2. Hence every directed cycle of M^+ contains BOTH b_1 and b_2. There can therefore be at most one cycle.

The cycle is proper: a spanning directed cycle on n vertices has n selected edges, while M^+ has only n-2. Every cyclic turn is tight by the preceding section. Thus C is one unique proper tight cycle recording the interaction of the two alternative gains.

Accepted R4 gives an exact two-cover of H-V(C), and the current movable-break/CYCLE-ROTATE mechanism turns every cyclic break of C into a literal maximum three-forest with one fixed complement two-cover. Therefore the nonaugmenting common-deletion residue is again exactly one SHARED CURRENT CYCLE PORTAL.

### 7. Complete pairwise one-edge relation theorem
Combining Sections 3-6, every pair of distinct reversible SUPPORT-CHANGING one-edge generators from one literal maximum three-forest has one of exactly four parent outcomes:

  SQUARE:
    a verified fourth maximum forest completes the exchange diamond;

  AUGMENTATION:
    the common-deletion double addition is an acyclic tight matching of size n-2 and therefore a spanning two-cover;

  TRIMER PORTAL:
    a mixed-turn failure or vertex-copy competition gives a named proper tight trimer currentized by R4;

  SHARED CYCLE PORTAL:
    the simultaneous interaction contains one unique proper tight cycle carrying both added edges, currentized as a movable-break family.          (CD.13)

There is NO fifth pairwise base obstruction after same-support fiber/cyclic reorders are quotiented away.

This is the desired one-edge DIAMOND / SQUARE-COMPLETION principle of G14 at the level of literal representatives. The spindle disk SV38434 is one explicit two-cell packet inside the SQUARE branch. The collision-preorder cycle debt of SV20847 is exactly the phenomenon isolated by the SHARED CYCLE branch.

### 8. Marked-holonomy consequence and exact remaining global work
Let a shortest marked loop be fiber-compressed as in SV35882. At any literal representative F, reverse the incoming one-edge support-changing transition and compare it with the outgoing one-edge support-changing transition. The base interaction now always has one of the four forms (CD.13).

Thus pairwise BASE noncommutation is completely generated by verified exchange squares and current trimer/cycle portals, with augmentation as an immediate exit. The genuinely global marked problem is correspondingly smaller: certify transport coherence of the retained history-bearing mark around verified squares, and consume any trimer/cycle portal that lies on a shortest marked loop. A discrepancy between the two square routes is itself a length-four history-bearing marked holonomy and should be treated as the atomic marked 2-cell obstruction.

No claim is made here that arbitrary ancestry marks automatically agree around a square, nor that every current trimer/cycle portal is extinct. The theorem removes the pairwise BASE geometry; the surviving obstruction is mark transport and portal consumption, not another local one-edge shape.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R4"}
]
```
