# The parallel double bridge enters each terminal R696 frame by one direct turn test

**Workspace:** D17
**State:** established
**Key:** `singleton-cover-union-endpoint-return-currentization`

**Summary:** The hard parallel double bridge does not need cross-fiber p-C/q-C returns to currentize its terminal R696 packets. For each bridge label r=p,q, the single left test (r,c2,c3) either gives the exact H-{c0,c1} cover (r,c2,...,ct)|D_r, where R696 is automatically FREE, or R3 gives the r-labelled reversed old C-state (c3,c2,r), an immediate R435 adjacent-reversal output. The right end is dual. Thus each endpoint is FREE-or-labelled-reversal; simultaneous failure for p,q puts both labels on one reversed C-state. Cross-fiber returns remain useful only for K defect/replacement accounting. The next target is to consume the four terminal tests into R561, legal support transfer/K descent, or closure.

### Direct left packet entry

Retain the established parallel double bridge

  C_p=(A-q-B)|C,
  C_q=(A-p-B)|C,

with a fixed Hamilton order

  C=(c_0,c_1,...,c_t),

where the accepted double-bridge section gives t>=3. Put

  D_p=A-q-B,   D_q=A-p-B.

The left terminal packet has carrier K_L=(c_0,c_1,c_2), reverse initial dimer S_L=(c_1,c_0), complementary singleton e_L=c_2, and witness pair {p,q}.

Fix r in {p,q}. Test the single turn

  L_r=(r,c_2,c_3).

If L_r is tight, then

  T_L(r)=(r,c_2,c_3,...,c_t) | D_r

is a literal two-cover of H-{c_0,c_1}, where D_p=A-q-B and D_q=A-p-B. In a hypothetical counterexample the pair-deletion residue cannot itself be Hamiltonian, since a Hamilton H-{c_0,c_1} together with the vacuous dimer {c_0,c_1} would already give a spanning two-cover of H. Hence T_L(r) is an exact two-cover in the R696 frame.

In T_L(r), the complementary singleton c_2 has literal neighbors r and c_3. Since c_3 is outside {p,q}, R696 is automatically in its FREE branch. The selected carrier/exterior state c_2-c_3 avoids both witnesses, so the packet is genuinely current in the exact support-deletion residue. No state from another singleton fiber has been imported.

If L_r is not tight, boundary antisymmetry R3 gives

  (c_3,c_2,r) tight.

This trimer already contains the reversed old C-state c_3 c_2 of the selected C-state c_2 c_3. Equivalently, comparing the trimer (c_3,c_2,r) with C lands immediately in the adjacent-reversal branch of R435. The output is source-labelled by the distinguished bridge label r.

Therefore, for each r in {p,q}, the left endpoint has the exact dichotomy

  R696-FREE in H-{c_0,c_1}   OR   an r-labelled R435 adjacent reversal of c_2 c_3.

In particular, if either L_p or L_q is tight, the left R696 packet is currentized. If both are bad, both (c_3,c_2,p) and (c_3,c_2,q) are tight, so the same reversed old C-state carries both distinguished bridge labels.

### Direct right packet entry

The terminal-end dual is equally literal. The right packet has carrier K_R=(c_{t-2},c_{t-1},c_t), reverse terminal dimer S_R=(c_t,c_{t-1}), complementary singleton e_R=c_{t-2}, and the same witness pair {p,q}.

For r in {p,q}, test

  R_r=(c_{t-3},c_{t-2},r).

If R_r is tight, then

  T_R(r)=D_r | (c_0,...,c_{t-3},c_{t-2},r)

is an exact two-cover of H-{c_{t-1},c_t}. The complementary singleton c_{t-2} has neighbors c_{t-3},r, with c_{t-3} outside {p,q}, so R696 is again automatically FREE.

If R_r is bad, R3 gives

  (r,c_{t-2},c_{t-3}) tight,

which contains the reversal c_{t-2}c_{t-3} of the old C-state c_{t-3}c_{t-2}; this is the corresponding r-labelled adjacent-reversal output of R435. Thus the right endpoint has the same FREE-or-labelled-reversal dichotomy, and simultaneous failure for p,q puts both labels on the same reversed old state.

### Consequence for cross-fiber return currentization

The currentization problem is therefore stronger and simpler than the cross-fiber formulation suggested by `singleton-cover-union-minimal-equality-incidence`. Once the parallel double bridge and its fixed Hamilton complement are present, the terminal R696 packets can be entered directly by one boundary turn test per bridge label. The actual p-C and q-C states guaranteed in other singleton fibers are not needed to establish common-residue currentness.

Those cross-fiber returns remain valuable for the independent codimension-one defect/replacement program: `singleton-cover-union-return-defect-or-replacement` still turns each into either a positive current defect or a Hamilton replacement. But they are no longer the scarce ingredient for the terminal packet.

Hence the parallel double-bridge residue itself yields, at each end, either a genuine same-residue R696 FREE packet or source-labelled R435 reversal geometry; if both bridge-label tests fail at one end, the failure is a dual-labelled reversal on one fixed old C-state. This fully resolves CROSS-FIBER RETURN CURRENTIZATION as an entry problem without mixing deletion fibers.

### Remaining consumer

R696 FREE is current but is not by itself closure, and a source-labelled R435 reversal is also not by itself closure. The next bounded target is therefore a FOUR-TEST TERMINAL ABSORPTION theorem: combine the two left tests and two right tests, preserving the fixed bridge rails D_p,D_q and the common witness pair {p,q}, to force fixed-support R561, a legal singleton-support transfer / profitable K repair, or a spanning two-cover. In the all-bad branch retain the dual-labelled reversed C-states at both ends; in every good branch retain the exact FREE frame rather than spending it into anonymous payment.

Status: complete deduction from the established parallel double-bridge section plus accepted R3, R435, and R696; not independently canonically reviewed as an exact section unit.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R696"
    }
]
```
