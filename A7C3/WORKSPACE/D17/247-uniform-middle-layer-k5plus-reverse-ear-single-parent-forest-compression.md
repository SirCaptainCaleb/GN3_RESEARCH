# For k at least five, Arm M has a direct one-parent entrance into maximum-three-forest dynamics

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-k5plus-reverse-ear-single-parent-forest-compression`

**Summary:** Combine the global Reverse-Ear forcing SV37965 with exact currentization of its three R435 outputs. Inspection of the SV37965 proof shows that the forced nonquiet R435 comparison is always between two actual Hamilton paths on one common support X of order k or k-1. In Arm M, H-X is non-Hamiltonian: if |X|=k its order is k+1 and Hamiltonicity is forbidden directly; if |X|=k-1 its order is k+2 and a Hamilton path would contain a forbidden contiguous Hamilton (k+1)-subpath. Thus R4 gives one exact two-cover U|V of H-X, making both compared Hamilton words literal maximum three-forest rails with U,V fixed. An adjacent selected reversal therefore enters the finite two-spectator transport SV36339, reaching R561 support escape/closure or a named current wrap shield. A reverse trimer is itself a proper tight path and R4 currentizes it immediately. A proper cycle enters the closed movable-break maximum-forest family SV25652. Consequently every Arm-M system with k>=5 has a direct parent-scale entrance into actual/closed maximum-three-forest dynamics. This strictly improves the earlier k>=8 Johnson/spindle compression as an entrance theorem, while leaving the global forest extinction problem open.

### 1. Global R435 activity occurs on one common support
Retain accepted R927 Arm M:

  |V(H)|=2k+1,
  every k-set is Hamiltonian,
  no (k+1)-set is Hamiltonian,

and assume k>=5.

The current exact working unit SV37965 proves that at least one of the R435 comparisons in its Hall-circuit argument is nonquiet. Crucially, inspecting that proof rather than using only its headline shows that every comparison capable of firing is a SAME-SUPPORT comparison:

* two Hamilton words P,Q on one k-support S;
* two trimmed Hamilton core words K_x,K_y on one (k-1)-support R; or
* the terminal insertion-clash paths T_a,T_b on one (k-1)-support M+c.

Hence we may retain two actual Hamilton tight paths

  P,Q

on one common physical support X with

  |X| in {k-1,k},                                      (RF.1)

such that accepted R435 emits an adjacent selected-state reversal, a reverse tight trimer, or a proper tight cycle. All physical vertices and the exact R435 ancestry are retained.

### 2. The complement of the active support is necessarily non-Hamiltonian
Put

  C=V(H)-X.

If |X|=k, then |C|=k+1, and C is non-Hamiltonian by the defining Arm-M hypothesis.

If |X|=k-1, then |C|=k+2. Were C Hamiltonian, any contiguous block of k+1 vertices in a Hamilton order of C would itself be a tight Hamilton path on a (k+1)-set, again contradicting Arm M.

Thus in both cases C is non-Hamiltonian. Accepted smallest-counterexample minimality R4 therefore gives a literal exact two-cover

  U | V                                                     (RF.2)

of C. In particular U and V are nonempty. Consequently

  P | U | V,
  Q | U | V                                                (RF.3)

are literal spanning three-path covers of H and hence maximum three-forests. The SAME spectator path words U,V serve both representatives.

### 3. Adjacent selected reversal enters support-changing forest transport
Suppose the nonquiet R435 output is the adjacent-reversal case. Then one physical dimer {u,v} is selected as u->v in one of P,Q and v->u in the other. The pair (RF.3) therefore satisfies exactly the hypotheses of the current two-spectator reversal transport SV36339.

That transport freezes U,V and the named physical reversed dimer while a strict boundary-distance discrepancy decreases. It terminates in one of two exact species:

  R561 boundary reversal,
  named reverse-wrap shield.                              (RF.4)

At R561, absorbing an endpoint of U or V either closes H by a spanning two-cover or gives a literal support-changing maximum three-forest. A wrap shield is a proper graph-intrinsic tight trimer; by R4 its complement has an exact two-cover, so the shield is already current as a rail of a maximum three-forest.

Thus the selected-reversal R435 branch enters genuine support-changing/current maximum-three-forest dynamics with both original complement rails retained throughout the finite transport.

### 4. Reverse trimer is immediately current
Suppose R435 emits a reverse tight trimer T. The trimer is a proper graph-intrinsic tight path in H. By R4 the complement H-V(T) has an exact two-cover

  U_T | V_T.

Therefore

  T | U_T | V_T                                          (RF.5)

is a literal maximum spanning three-forest. No representative synchronization or inherited selection claim is needed: the trimer itself is the retained physical output.

### 5. Proper cycle is a closed current family
Suppose R435 emits a proper vertex-simple tight cycle C_0. Apply the exact current unit SV25652. One exact two-cover of H-V(C_0) serves every cyclic break of C_0, producing a closed movable-break family of literal maximum three-forest representatives with the two complement rails fixed.

Hence the cycle branch is already an explicit closed object in the global maximum-forest exchange space.

### 6. Direct single-parent compression for the uniform arm
All three possible nonquiet outputs of SV37965 therefore have parent destination

  ACTUAL / CLOSED MAXIMUM-THREE-FOREST DYNAMICS.          (RF.6)

Consequently, for every hypothetical R927 Arm-M system with k>=5,

  ARM M  -->  R435-ACTIVE SAME-SUPPORT PACKET
         -->  MAXIMUM-THREE-FOREST DYNAMICS.              (RF.7)

This is a stronger entrance theorem than the earlier k>=8 compression SV37494: it does not require first finding a degree-three Johnson completion core, a universal one-extension four-core, a pair-core triangle, or a three-port spindle. Those local systems remain useful exact models inside the forest program, especially the two-square spindle disk SV38434, but they are no longer necessary parent gates for Arm M.

For k=5 the uniform arm is independently eliminated by the accepted small-order theorem R957; (RF.7) is still formally valid as a parent reduction. Its new range of interest begins at k=6.

### 7. Scope and remaining obstruction
This section does NOT prove that every maximum-three-forest component escapes to a two-cover, that every closed movable-break orbit contracts, or that every history-bearing marked holonomy is trivial. It proves only the exact parent compression (RF.7). The surviving grand consumer is now sharply global: extinguish support-changing maximum-three-forest recurrence / component-recompletion / marked holonomy.

In particular, further Arm-M work should not reopen Johnson overlap, universal-core, C4, or spindle as independent terminal programs unless needed as local cells inside that global exchange problem.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```