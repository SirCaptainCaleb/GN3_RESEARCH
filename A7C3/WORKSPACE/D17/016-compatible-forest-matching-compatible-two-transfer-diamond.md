# Two matching-compatible one-edge transfers either fill an exchange square or expose a shared current portal

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-matching-compatible-two-transfer-diamond`

**Summary:** Let F be a literal maximum spanning three-forest and let F1,F2 be two distinct literal maximum forests obtained from F by one-edge exchanges tau_i: delete one selected directed edge a_i and add one directed edge b_i. Assume the two exchanges are simultaneously matching-compatible: a_1!=a_2 and the double replacement M*=(M(F)-{a1,a2})+{b1,b2} is still a bipartite matching on V_out union V_in. Then exactly one of three parent outcomes occurs. If a genuinely mixed predecessor-successor turn in M* is bad, R3 reverses it to a graph-intrinsic tight trimer, which R4 currentizes. If all mixed turns are tight but M* contains a physical directed cycle, that cycle is proper and unique and must contain both added edges (neither one-edge transfer alone has a cycle); hence it is explicit shared cycle debt and enters the movable-break/CYCLE-ROTATE current family. Otherwise M* is a spanning tight path forest with n-3 edges, hence a literal maximum three-forest F12, and F-F1-F12-F2-F is a verified exchange square whose four sides are reversible one-edge exchanges. Thus matching-compatible one-edge generators satisfy a diamond relation unless their interaction itself exposes current reverse-trimer or shared cycle debt. The only one-edge-pair obstruction not covered is vertex-copy competition, where the simultaneous replacement is not a matching.

### 1. Two literal one-edge transfers from one maximum forest
Let H be a hypothetical smallest counterexample and let

  F=P_1|P_2|P_3

be a literal maximum spanning three-forest. Write M for its directed bipartite matching in V_out disjoint_union V_in. Thus |M|=|V(H)|-3.

Retain two DISTINCT reversible one-edge transfers from F. For i=1,2 let

  tau_i : a_i -> b_i

mean that a_i is one selected directed edge of F, b_i is one directed edge not selected by F, and

  M_i=(M-{a_i}) union {b_i}                              (DG.1)

is the selected matching of a literal maximum three-forest F_i. This includes every SLIDE of SV22098, but the statement does not require the moves to have arisen from the SLIDE construction.

Assume

  a_1 != a_2                                              (DG.2)

and that the simultaneous replacement

  M_*=(M-{a_1,a_2}) union {b_1,b_2}                      (DG.3)

is still a bipartite matching. Call this MATCHING-COMPATIBILITY. It says precisely that after the two old selected edges are removed, the two new edges do not compete for one out-copy or one in-copy.

The question is whether tau_1 and tau_2 commute through a fourth literal maximum forest.

### 2. Only genuinely mixed turns can newly fail
Because M_* is a matching, every physical vertex has indegree and outdegree at most one. Consider a selected predecessor-successor pair

  x -> v -> y

in M_*.

If both selected states at v are inherited from F, the turn is tight because F is a literal forest. If the local pair is exactly the pair selected in F_1 or exactly the pair selected in F_2, it is tight because F_1,F_2 are literal forests. Therefore a new compatibility question occurs only when one side of v comes from tau_1 and the other side from tau_2.

If x=y, then M_* contains the directed physical 2-cycle

  x -> v -> x,                                           (DG.4)

which belongs to the cycle-debt branch below. Assume x,v,y are distinct. If the mixed turn (x,v,y) is bad, accepted boundary antisymmetry R3 gives the exact reverse trimer

  (y,v,x) tight.                                         (DG.5)

This trimer is proper. By accepted R4 its complement has an exact two-cover, so (DG.5) is immediately current as one rail of a literal maximum spanning three-forest.

Thus any failed mixed compatibility relation is not anonymous noncommutation: it emits a named graph-intrinsic current reverse-trimer portal.

### 3. If every mixed turn is tight, the double replacement is a tight pseudoforest
Assume now that every mixed turn on three distinct vertices is tight. Then every physical predecessor-successor triple selected by M_* is tight. Since M_* is a matching, its physical components are directed tight paths, singleton vertices, or directed tight cycles.

If there is no directed cycle, M_* is a spanning tight path forest. It has

  |M_*|=|M|=|V(H)|-3,

so it has exactly three path components. Hence it is a literal maximum spanning three-forest; call it F_12.

Moreover

  F_1 <-> F_12

differs by exactly the second edge replacement a_2 -> b_2, while

  F_2 <-> F_12

differs by exactly a_1 -> b_1. Since both endpoints of each displayed transition are literal maximum forests, all four sides are exactly reversible one-edge exchanges. Therefore

  F - F_1 - F_12 - F_2 - F                             (DG.6)

is a verified exchange square.

No appeal to abstract commutativity is being made: F_12 itself is the literal fourth representative.

### 4. Any cycle debt is shared by the two transfers
It remains to suppose every mixed turn is tight but M_* contains a directed physical cycle C.

The cycle C cannot occur already in F, because F is a forest. It cannot use b_1 but avoid b_2: if it did, the same cycle would occur in M_1, since M_1 differs from M only by a_1 -> b_1 and the second replacement is absent. But F_1 is a forest. Symmetrically C cannot use b_2 while avoiding b_1. Therefore every directed cycle of M_* contains BOTH added edges b_1 and b_2.

In particular there can be at most one directed cycle: two disjoint directed cycles cannot both contain the same two selected edges. Hence the double replacement has one UNIQUE physical cycle-debt component C, and C records the interaction of the two transfers rather than debt belonging to either transfer separately.

The cycle is proper. Indeed M_* has only |V(H)|-3 selected edges, so it cannot be one spanning directed cycle. Every cyclic turn is tight by the preceding section. Thus C is a proper vertex-simple tight cycle. Accepted R4 gives an exact two-cover of H-V(C), and the current movable-break/CYCLE-ROTATE mechanism supplies literal maximum-three-forest representatives for every cyclic break of C with one fixed complement two-cover.

Hence the only cycle obstruction to the square is an explicit SHARED CURRENT CYCLE PORTAL.

### 5. Diamond-or-portal relation
We have proved the exact trichotomy for any two matching-compatible one-edge transfers from one literal maximum three-forest:

  (SQUARE) the simultaneous replacement is a literal maximum forest F_12 and the two moves bound the verified square (DG.6);

  (TRIMER PORTAL) some genuinely mixed turn is bad and R3 emits a named current reverse trimer;

  (SHARED CYCLE) all mixed turns are tight but the simultaneous replacement carries one unique proper tight cycle containing both new edges, already current through its movable-break family.            (DG.7)

This is a genuine relation theorem for the exchange-complex program. In particular, after quotienting local reverse-trimer/cycle portals to their existing global consumers, any two matching-compatible one-edge generators commute through an actual fourth representative.

The spindle two-square disk SV38434 is an explicit structured instance of (SQUARE): its one-edge transfers fill two adjacent diamonds, while the two omitted formal cube states correspond to applying the tail reversal before the prerequisite edge removal and hence fall outside matching/path-forest compatibility through visible 2-cycle debt.

### 6. Exact remaining local obstruction
The theorem deliberately leaves one sharply defined one-edge interaction untreated: VERTEX-COPY COMPETITION, when (DG.3) is not a bipartite matching because b_1 and b_2 demand the same physical out-copy or the same physical in-copy after the two deletions.

Thus the broad G14 diamond target may be split cleanly:

  matching-compatible pairs -> square or current portal, PROVED here;
  vertex-copy competing pairs -> remaining overlap theorem.          (DG.8)

No assertion is made that an arbitrary history-bearing mark transports coherently around every verified square. The present theorem contracts the BASE representative loop. Marked-holonomy extinction still requires the source transition rules to certify that the retained ancestry/mark agrees under the two square routes, or else to use the discrepancy itself as a strict shortening/output.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R4"}
]
```
