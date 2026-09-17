# A fixed-complement critical block reduces to a small extension core, current maximum-forest dynamics, or endpoint-endpoint reversal

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-critical-block-core-exchange-or-endpoint-reversal`

**Summary:** Apply accepted R961 to any smallest-counterexample fixed-complement critical block. In the R961 quiet constant-role triangle, a blocker gives the universal Hamilton four-core of SV24585, hence a universally one-extendable four-set, while the all-transfer case is exported by SV27515 in one step to a universally one-extendable four-set or actual maximum-three-forest representative dynamics. In the explicit R435 branch, neighboring puncture supports differ by one deleted label. A proper-cycle output gives the closed movable-break family SV25652; a reverse trimer gives the small core or fresh maximum forest of SV26759; an adjacent selected reversal gives SV27136, hence either a fresh pair-deletion maximum-forest portal when at least one exchanged label is internal, or two exact same-residue covers with identical support partition and fixed complement selecting one common dimer oppositely when both exchanged labels are endpoints. Therefore every fixed-complement critical block has only three parent-scale destinations: a universally one-extendable four-set, current/closed maximum-three-forest dynamics, or the single residual endpoint-endpoint fixed-complement reversal. Full CBCA is reduced to consuming that last reversal together with the global exchange/core absorbers; no closure is claimed.

### 1. Full fixed-complement critical-block setup
Let H be a hypothetical smallest Strong Level-(1) counterexample with

  V(H)=Omega disjoint_union V(Q),

where Q is a literal Hamilton tight path and Omega is non-Hamiltonian but deletion-Hamiltonian. Retain the complete family of actual Hamilton puncture paths on Omega-y, each paired with Q in an exact singleton-deletion row.

Apply accepted R961 proof-aware to an extremal endpoint-return matching and its actual puncture representatives.

### 2. Quiet R961 branch has no independent local terminal
Suppose R961 enters its R435-quiet constant-role triangle.

If at least one matched endpoint incidence takes the BLOCKER branch of the fixed-boundary transfer compiler, SV24585 produces a Hamilton four-set which Hamilton-extends by every exterior vertex. In particular it is a universally one-extendable four-set in the stronger current G9 sense.

If all three matched incidences transfer, SV27515 shows that no second critical-block induction is required. After the one common prefix/suffix push, either the resulting neighboring-support comparison produces a universally one-extendable four-set, a fresh actual maximum spanning three-forest, or a closed movable-break maximum-forest family; if all pushed comparisons remain quiet, the directed triangle itself plus one absorbed complement endpoint is a universally one-extendable four-set.

Thus the quiet R961 triangle has only

  SMALL EXTENSION CORE
  or CURRENT MAXIMUM-FOREST DYNAMICS.                     (CR.1)

### 3. Explicit R435 branch routes by its physical output species
Suppose instead R961 produces explicit R435 geometry between two actual neighboring puncture paths P_a on Omega-a and P_b on Omega-b. Both occur with the same literal Hamilton complement Q.

PROPER CYCLE. SV25652 turns the proper tight cycle into a cyclic family of actual maximum three-forests obtained by moving the break of the same physical cycle while retaining one fixed exact two-cover of its complement.

REVERSE TRIMER. SV26759 tests the opposite turn at the same physical middle. The result is either a directed comparison triangle on a four-set, hence a universally one-extendable four-set by R902, or a literal fresh maximum three-forest obtained by cutting the old puncture path once and attaching the foreign deleted label to the new boundary.

ADJACENT SELECTED REVERSAL. SV27136 deletes the exchanged pair {a,b}. If at least one exchanged label is internal in the opposite puncture path, the corresponding trim is a three-cover of H-{a,b}; an exact two-cover of that same residue must cross its components, and lifting it with the deleted dimer gives an actual maximum three-forest. If both exchanged labels are endpoints, the two trims are exact two-covers of the same pair-deletion residue with identical support partition

  (Omega-{a,b}) | Q

and select one common physical dimer in opposite directions. Retain this as the ENDPOINT-ENDPOINT FIXED-COMPLEMENT REVERSAL residue.                            (CR.2)

### 4. Parent reduction
Combining Sections 2 and 3, every fixed-complement critical block in a hypothetical smallest counterexample produces at least one of:

1. SMALL CORE: a four-set S satisfying S+d Hamiltonian for every exterior d;
2. REPRESENTATIVE DYNAMICS: a fresh actual maximum spanning three-forest or a closed movable-break family of such forests, with physical ancestry retained;
3. ENDPOINT-ENDPOINT REVERSAL: two exact covers of one pair-deletion residue with identical support partition and literal complement Q, selecting one common dimer oppositely.                       (CR.3)

No other static R435 species survives this reduction.

### 5. What remains for full CBCA
This is not Full Critical-Block Complement Absorption. Destination (1) is delegated to the universal one-extension four-set absorber; destination (2) enters the global closed-exchange-class escape parent; destination (3) is the one genuinely CBCA-local residue still requiring a consumer.

The existing selected-reversal transport SV7559 can move the discrepancy toward an R561 boundary state or named wrap shields, but this section does not assume those shields close. The next local CBCA target is therefore sharply isolated: use the ancestral fact that a and b were actual endpoints of the two puncture paths to consume the endpoint-endpoint same-residue reversal, preferably into destination (1) or (2).

All SV dependencies used here remain expository/unreviewed unless independently certified; accepted R961 and R902 are the canonical engines.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R961"
    }
]
```
