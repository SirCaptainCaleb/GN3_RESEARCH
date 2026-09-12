# Every fixed-complement critical block exports completely to small-core or maximum-forest holonomy

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-critical-block-local-routing-complete`

**Summary:** SV27898 reduced every smallest-counterexample fixed-complement critical block to three destinations: universal one-extension four-set, current/closed maximum-three-forest dynamics, or endpoint-endpoint fixed-complement reversal. SV29667 eliminates the third as an independent local residue: in the even two-sheet normal form, comparing skip-one puncture paths forces neighboring-support R435 activity with both exchanged labels internal, so every R435 output exports to a universal one-extension four-set, a fresh maximum three-forest, or a closed movable-break orbit. Therefore every fixed-complement critical block now has only the two global destinations SMALL EXTENSION CORE or ACTUAL/CLOSED MAXIMUM-THREE-FOREST HOLONOMY. This completes the local CBCA routing program but does not absorb either global destination and does not prove Full CBCA or O4.

### 1. Parent reduction
Retain the fixed-complement critical-block setup of SV27898 in a hypothetical smallest Strong Level-(1) counterexample:

  V(H)=Omega disjoint_union V(Q),

where Q is a literal Hamilton path and Omega is non-Hamiltonian deletion-Hamiltonian.

SV27898 proves that every such configuration reaches at least one of the three parent-scale destinations

1. a four-set S such that S+d is Hamiltonian for every exterior d;
2. a fresh actual maximum spanning three-forest or a closed movable-break family of maximum three-forests;
3. an endpoint-endpoint fixed-complement selected-reversal residue on one pair deletion.          (LR.1)

### 2. The third destination is no longer local
Assume destination 3. SV28285 compresses any closed survival of these endpoint-endpoint reversals to an even two-sheet endpoint-return cycle with actual Hamilton puncture paths P_i on Omega-y_i and

  End(P_i)={y_{i-1},y_{i+1}},

with alternating endpoint roles.

SV29667 then compares P_i with the skip-one path P_{i+2}. The shared endpoint y_{i+1} occurs at opposite ends of the two actual Hamilton words, so R435 activity is forced. The exchanged labels y_{i+2} in P_i and y_i in P_{i+2} are both internal. Consequently the adjacent-selected-reversal output cannot return to endpoint-endpoint residue; SV27136 sends it to a fresh pair-deletion maximum-three-forest portal. The reverse-trimer and proper-cycle outputs are already sent by SV26759 and SV25652 respectively to a universal one-extension four-set / fresh maximum forest or a closed movable-break orbit.

Hence destination 3 of (LR.1) itself reaches destination 1 or 2 after one skip-one comparison.                                  (LR.2)

### 3. Complete local CBCA routing
Combining (LR.1) and (LR.2), every fixed-complement critical block in a hypothetical smallest counterexample exports to

  SMALL EXTENSION CORE,
  or ACTUAL/CLOSED MAXIMUM-THREE-FOREST HOLONOMY.         (LR.3)

There is no remaining independent fixed-complement local packet, blocker family, Reverse-Ear species, or endpoint two-sheet residue requiring a separate CBCA-local consumer.

### 4. Scope
This is a routing theorem, not Full Critical-Block Complement Absorption. The universal one-extension four-set is now itself a holonomy generator via SV26947 and later pair-core work; maximum-three-forest dynamics are governed by the G10 minimal closed-holonomy program. Neither global destination is yet proved impossible in general.

The significance is organizational and mathematical: any future proof of the global small-core / closed-representative extinction theorem automatically consumes the entire fixed-complement critical-block branch without further CBCA case analysis. Conversely, future CBCA work should use the retained fixed-complement ancestry only to strengthen those global holonomy destinations, not restart local packet classification.

