# Every proper R435 cycle is already a closed movable-break family of maximum three-forests

**Workspace:** D17
**State:** established
**Key:** `r435-proper-cycle-movable-break-closed-family`

**Summary:** In a hypothetical smallest counterexample, any vertex-simple proper tight cycle C produced by R435 is automatically a current closed representative orbit. Every cyclic break K_e of C is a literal tight path on the same support. Since a Hamilton complement would pair with any K_e to two-cover H, the fixed complement W=H-V(C) is non-Hamiltonian; accepted R4 gives one literal exact two-cover T_1|T_2 of W. The same T_1|T_2 therefore works for every cyclic break, so K_e|T_1|T_2 is an actual maximum spanning three-forest for every rim edge e of C. Consecutive states differ only by moving the break of one physical tight cycle, while the complement rails remain literally fixed. Thus the proper-cycle output of neighboring-support Reverse Ear geometry is not terminal cycle debt: it canonically exports CBCA into a closed movable-break family in the global maximum-three-forest exchange graph. No escape or augmentation is asserted.

### 1. Setup\nLet H be a hypothetical smallest Strong Level-(1) counterexample and suppose an application of accepted R435 produces a vertex-simple proper tight cycle\n\n  C=(c_0,c_1,...,c_{r-1},c_0),\n\nwith r>=3 and V(C) a proper subset of V(H). Retain the physical cyclic order and the exact R435 ancestry that produced C.\n\n### 2. Every cyclic break is an actual tight path\nBecause C is a tight cycle, for every i the cyclic break\n\n  K_i=(c_{i+1},c_{i+2},...,c_i)\n\nis a literal vertex-simple tight Hamilton path on the support V(C). No path reversal is used; K_i is simply the inherited cyclic order with one rim state omitted.\n\nPut\n\n  W=H-V(C).\n\nIf W were Hamiltonian, then any K_i together with a Hamilton path on W would form a spanning two-cover of H, contradiction. Hence W is non-Hamiltonian.\n\n### 3. One fixed exact complement two-cover serves every break\nApply accepted R4/P601 to any one proper tight path K_i. Since H is a smallest counterexample and K_i is proper, W has path-cover number exactly two. Choose and retain one literal exact two-cover\n\n  T=T_1|T_2\n\nof W.\n\nThe support W is independent of i. Therefore the very same literal T works for every cyclic break K_i, and\n\n  F_i=K_i|T_1|T_2\n\nis an actual spanning three-path cover of H for every i. Since H has no spanning two-cover, each F_i is a maximum compatible spanning forest.\n\n### 4. Closed movable-break representative orbit\nThe family\n\n  F_0,F_1,...,F_{r-1}\n\nis cyclic in the literal representative space. Consecutive members change only the break location on the same physical tight cycle C; both complementary rails T_1,T_2 remain fixed with identical orders and selected states. After r break moves the literal state returns to F_0.\n\nThus a proper-cycle output of R435 canonically determines a CLOSED CURRENT REPRESENTATIVE WALK in the maximum-three-forest exchange space, with exact physical holonomy equal to one full circuit of the break around C. No arbitrary choice of fresh complement representatives is required after the first R4 application.\n\n### 5. CBCA / closed-class interface\nIn particular, whenever a neighboring-support R435 comparison inside a fixed-complement critical-block family takes its proper-cycle branch, the CBCA investigation may leave the static Reverse-Ear description immediately. The cycle itself supplies the carrier of a closed maximum-three-forest family, and the fixed exact cover T of H-V(C) supplies the two other rails for every break.\n\nThis is not an augmentation theorem and does not prove Global Three-Forest Escape. It is a currentization theorem: proper R435 cycle debt is already an explicit closed exchange-class object. The remaining consumer is to show that its break orbit escapes, contracts to a shorter comparison holonomy, or emits a universally one-extendable four-set.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    }
]
```
