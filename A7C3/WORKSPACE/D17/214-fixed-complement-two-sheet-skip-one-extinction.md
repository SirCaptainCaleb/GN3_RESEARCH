# Skip-one comparison extinguishes the endpoint two-sheet CBCA residue

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-two-sheet-skip-one-extinction`

**Summary:** In the even alternating endpoint-return residue SV28285, compare P_i on Omega-y_i with P_{i+2} on Omega-y_{i+2}. Their common cycle endpoint y_{i+1} occurs at opposite ends because matched roles alternate, while at least one other common cycle label exists; hence their common contacts cannot be R435-monotone and an explicit neighboring-support R435 output is forced. The exchanged labels y_{i+2} in P_i and y_i in P_{i+2} are both internal, so the adjacent-selected-reversal output cannot recycle into the endpoint-endpoint residue: SV27136 forces a fresh pair-deletion maximum-three-forest portal. The reverse-trimer output gives a universal one-extension four-set or a fresh maximum forest by SV26759, and the proper-cycle output gives the closed movable-break orbit SV25652. Thus the two-sheet endpoint holonomy cannot remain a CBCA-local obstruction. It necessarily exports in one skip-one comparison to the universal-core or actual maximum-three-forest holonomy programs. This completes the local CBCA routing but does not itself absorb those global destinations or close O4.

### 1. Two-sheet setup
Retain the even endpoint-return residue of `fixed-complement-endpoint-reversal-two-sheet-parity` SV28285 inside a hypothetical smallest Strong Level-(1) counterexample:

  V(H)=Omega disjoint_union V(Q),

with Q a fixed literal Hamilton path and

  y_0 -> y_1 -> ... -> y_{ell-1} -> y_0,

ell even and ell>=4, be the physical endpoint-return cycle. For each i retain the actual Hamilton puncture path P_i on Omega-y_i. SV28285 gives

  End(P_i)={y_{i-1},y_{i+1}},                            (SE.1)

and if epsilon_i denotes the role HEAD/TAIL of the matched successor y_{i+1} in P_i, then

  epsilon_{i+1}=opposite(epsilon_i).                    (SE.2)

All indices are modulo ell.

### 2. Skip-one puncture paths force a Reverse-Ear event
Fix i and compare the actual Hamilton paths

  P_i      on Omega-y_i,
  P_{i+2}  on Omega-y_{i+2}.                            (SE.3)

Their common support is

  S=Omega-{y_i,y_{i+2}}.                                (SE.4)

The physical vertex y_{i+1} belongs to S. In P_i it is the matched successor and has role epsilon_i. In P_{i+2}, the same physical vertex y_{i+1} is the predecessor endpoint, so its role is the opposite of epsilon_{i+2}. By two-step alternation epsilon_{i+2}=epsilon_i, hence y_{i+1} occurs at opposite ends of the two displayed Hamilton words.

There is at least one other common cycle label. For ell>4 one may take any cycle label distinct from y_i,y_{i+1},y_{i+2}; for ell=4 the opposite label y_{i-1}=y_{i+3} is common. Thus some common vertex w lies after y_{i+1} in one path and before y_{i+1} in the other. The common S-contacts therefore cannot occur in one monotone order.

Apply accepted R435 to P_i and P_{i+2}. A reverse-order pair of contacts has a consecutive reverse-order subpair, so R435 necessarily emits one of its explicit outputs:

  selected-state reversal,
  reverse seam trimer,
  proper tight cycle.                                   (SE.5)

The two supports in (SE.3) differ by exactly one exchanged vertex, so the one-foreign localization SV24806 applies to this neighboring-support comparison.

### 3. The selected-reversal output cannot return to endpoint-endpoint holonomy
For the comparison (SE.3), the exchanged label present in P_i but absent from P_{i+2} is y_{i+2}. By (SE.1), the only endpoints of P_i are y_{i-1},y_{i+1}; since ell>=4,

  y_{i+2} is internal in P_i.                            (SE.6)

Dually the exchanged label y_i is internal in P_{i+2}, whose endpoints are y_{i+1},y_{i+3}:

  y_i is internal in P_{i+2}.                            (SE.7)

Therefore if (SE.5) is the adjacent selected-state reversal branch, the endpoint-endpoint case of SV27136 is impossible. Both exchanged labels are internal, so SV27136 supplies one exact two-cover T of

  H-{y_i,y_{i+2}}

which crosses the explicit trims of both puncture paths. Lifting T with the deleted dimer {y_i,y_{i+2}} gives an actual maximum spanning three-forest of H. Thus selected reversal exits directly to current representative dynamics.

### 4. The other R435 outputs are already global destinations
If (SE.5) is a reverse seam trimer, SV26759 gives either

1. a physical four-set X satisfying X+d Hamiltonian for every exterior d, or
2. a fresh actual maximum spanning three-forest obtained by one cut of the reference puncture path and attachment of the foreign exchanged label.

If (SE.5) is a proper tight cycle, SV25652 gives the closed movable-break family of actual maximum spanning three-forests, with one fixed exact two-cover of the cycle complement serving every cyclic break.

Hence every possible R435 output of the skip-one comparison has already left the endpoint-endpoint local residue.

### 5. Local two-sheet extinction
Consequently the even two-sheet holonomy of SV28285 cannot be closed under its own CBCA-local endpoint-endpoint reversal species. One skip-one comparison P_i versus P_{i+2} necessarily produces

  UNIVERSAL ONE-EXTENSION FOUR-SET,
  or FRESH MAXIMUM THREE-FOREST,
  or CLOSED MOVABLE-BREAK MAXIMUM-FOREST ORBIT.          (SE.8)

In particular, the third destination of the parent CBCA reduction SV27898 is not a terminal local obstruction. It immediately exports to the same two parent programs as the other CBCA branches: universal-core holonomy or actual maximum-three-forest exchange dynamics.

This completes the local routing of the fixed-complement critical-block program. It does NOT prove that the universal one-extension core is absorbable, does NOT prove Global Three-Forest Escape, and therefore does not by itself close Full Critical-Block Complement Absorption or O4. The gain is exact elimination of the last independent CBCA-local residue.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
