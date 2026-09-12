# Alternating hard runs force a skip-middle P4 pivot ladder with disjoint adjacent destinations

**Workspace:** D17
**State:** established
**Key:** `alternating-hard-run-skip-middle-p4-pivot-ladder`

**Summary:** In any growth-free alternating hard run on one fixed endpoint pair, every interior R542 packet is forced into the both-bad branch of SV73681, because the two SV73681 tests are complete reversals of the already-tight neighbor turns. Hence each interior center has a source-visible P4 on the old endpoints plus its two neighboring rail middles, omitting the center itself. Via SV73682 this P4 has a canonical middle-pair return. For adjacent interior centers these canonical destination pairs are physically disjoint, independent of the R584 branch choice. Thus R542 recycling cannot erase the hard-run event: before payment the run already carries a static ladder of pair-to-pair ancestor pivots. This does not yet contradict a bottom family, and the distinct paid descendants are alternatives, not simultaneous current states.


### 1. Input: one growth-free alternating hard run
Fix one ancestry-bearing floor aligned to a physical endpoint pair

  E={a,c},

and one literal exact pair-deletion frame H-E=U|V. On one displayed rail let

  v_1 -> v_2 -> ... -> v_m,  m>=3,

be a consecutive run of internal middles in the hard no-growth regime of `fixed-endpoint-hard-run-bilateral-r542-chain` SV73346. Thus the proper outer turns alternate. For an interior index i, normalize

  J_{i-1}=(a,v_{i-1},c),
  J_i=(c,v_i,a),
  J_{i+1}=(a,v_{i+1},c)                         (SP.1)

as tight. The endpoint-dual case is obtained by interchanging a and c in the displayed formulas, without changing any physical ancestor orientation.

SV73346 says that the reverse initial boundary dimer of the central carrier J_i,

  D_i=(v_i,c),

is tail-signed by the two distinct physical witnesses v_{i-1},v_{i+1}; simultaneously its reverse terminal boundary is R542-ready as well. Only D_i is needed below.

### 2. The SV73681 tests are forced bad
Apply `r542-collision-p4-payment-conversion` SV73681 to the R542 packet on D_i, with carrier

  K=J_i=(c,v_i,a)

and witness pair {v_{i-1},v_{i+1}}. In the notation of SV73681 its two test trimers are exactly

  X_-=(c,v_{i-1},a),
  X_+=(c,v_{i+1},a).                              (SP.2)

But the two neighbor turns in (SP.1) are tight. Boundary antisymmetry R3 therefore makes both complete reversals in (SP.2) bad. Consequently neither one-test-tight branch of SV73681 is available. Its BOTH-BAD branch is forced.

Hence one of the two literal tight P4s

  (a,v_{i-1},c,v_{i+1}),
  (a,v_{i+1},c,v_{i-1})                           (SP.3)

exists. In particular the center v_i has disappeared. This P4 is a graph-intrinsic consequence of the source hard-run packet and exists before any R542 payment descendant is chosen.

For the endpoint-dual central orientation

  J_i=(a,v_i,c),

with neighboring turns (c,v_{i-1},a) and (c,v_{i+1},a), the same calculation gives one of

  (c,v_{i-1},a,v_{i+1}),
  (c,v_{i+1},a,v_{i-1}).                           (SP.4)

Call the resulting source-visible object the skip-middle P4 at center i.

### 3. Canonical middle-pair pivot
By `phasezero-p4-middle-pair-bilateral-return` SV73682, every P4 in (SP.3) has a lawful nonclosing return to its literal middle pair, retaining the P4 boundary dimers as a bilateral ancestor packet. Thus when J_i=(c,v_i,a), its canonical destination has the form

  F_i={c,z_i},  z_i in {v_{i-1},v_{i+1}}.          (SP.5)

When J_i=(a,v_i,c), the endpoint-dual destination is

  F_i={a,z_i},  z_i in {v_{i-1},v_{i+1}}.          (SP.6)

This is a pair-to-pair ancestry pivot, not a claimed rank decrease.

### 4. Adjacent interior pivots have disjoint physical destinations
Assume m>=4 and take adjacent interior centers i and i+1. Their outer orientations are opposite. Normalize the first as in (SP.1). Then

  F_i={c,z_i},          z_i in {v_{i-1},v_{i+1}},
  F_{i+1}={a,z_{i+1}}, z_{i+1} in {v_i,v_{i+2}}.  (SP.7)

The two rail-choice sets in (SP.7) are disjoint because all displayed rail vertices are distinct, and neither contains a or c. Since a!=c,

  F_i cap F_{i+1} = emptyset.                      (SP.8)

This disjointness is independent of which of the two R584 P4 orders occurs at either center. Therefore every growth-free hard run of length at least four carries, already in the common parent graph, two adjacent skip-middle P4s whose canonical SV73682 floor destinations are physically disjoint.

### 5. Family-level consequence and fence
The alternating bilateral R542 chain of SV73346 is therefore not merely a sequence of payable collision packets. Before payment it contains a static skip-middle P4 ladder. R542 recycling cannot erase this parent geometry, because the P4 at each interior center is forced before a payment choice is made.

For a reconstruction-closed G26 bottom family, every legal continuation must therefore be compatible with these P4-born pair-to-pair ancestry pivots. In a run of length at least four the family must in particular absorb pivot types toward two disjoint physical middle pairs arising at adjacent centers.

This section does NOT claim that the two paid SV73682 descendants are simultaneously current. They are alternative legal continuations from graph-intrinsic parent P4s. It also does NOT claim that disjoint destination pairs alone contradict bottom-family closure. A tempting next move is to use the opposite-polarity P4 boundary dimers meeting at the old endpoints, but an R547 hinge output is not automatically a paid floor outside an actual signed-payment lineage. Any such consumer must preserve that provenance explicitly.

R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```