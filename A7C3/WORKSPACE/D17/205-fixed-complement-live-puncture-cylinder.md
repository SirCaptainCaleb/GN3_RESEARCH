# Live puncture cylinders are preserved by simultaneous fixed-boundary prefix push

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-live-puncture-cylinder`

**Summary:** Define a live puncture cylinder in a hypothetical counterexample by a partition V(H)=A disjoint-union Q with Q a literal Hamilton path, a live set L subset A, and for every a in L one retained Hamilton path P_a on A-a, so P_a|Q is an exact H-a two-cover. No Hamilton-deletion condition is imposed on A-L. Every live label still satisfies the full reverse Q-boundary wall. Hence if C subset L and for every a in C a retained HEAD representative P_a=(b_a,r_a,...) has b_a in L and successful transfer turn (q0,b_a,r_a), then the live wall at b_a supplies (q1,q0,b_a), so (q1,q0,P_a)|Q[2,t] is exact on H-a. With Aplus=A+{q0,q1}, Qplus=Q[2,t], Lplus=C, these rows form another live puncture cylinder. TAIL is dual. Thus the one-step CBCA prefix contraction is genuinely closed in a weaker partial-family state class even though the enlarged active support need not be deletion-Hamiltonian at the newly absorbed vertices. Neighboring-support R435 comparisons remain fully current inside the class because both rows share the same literal complement.

### 1. Live puncture cylinder
Let H be a hypothetical smallest Strong Level-(1) counterexample. A LIVE PUNCTURE CYLINDER is data

  V(H)=A disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),
  L subseteq A,

where Q is a literal Hamilton tight path, L is nonempty, and for every live label a in L one retains an actual Hamilton path P_a on exactly A-a. Hence

  P_a | Q

is a literal spanning two-cover of H-a. It is exact: if H-a itself were Hamiltonian, that Hamilton path together with the singleton {a} would two-cover H.

No deletion-Hamiltonicity is required for labels of A-L. The active universe A itself is non-Hamiltonian, since a Hamilton path on A together with Q would two-cover H.

The original fixed-complement critical-block family is the special case A=Omega and L=Omega.

### 2. Every live label still has the full outer boundary wall
Assume |Q|>=2. Fix a in L. If

  (a,q_0,q_1)

were tight, then (a,q_0,q_1,...,q_t) would Hamiltonize {a}+Q and pair with P_a on A-a to two-cover H. Therefore that turn is bad, and R3 gives

  (q_1,q_0,a) tight.                                      (LC.1)

Dually,

  (a,q_t,q_{t-1}) tight.                                  (LC.2)

Thus the full critical-block boundary-wall proof only needs the puncture row at the tested label; it does not need A to be deletion-Hamiltonian everywhere.

### 3. Simultaneous HEAD prefix push preserves the class
Assume |Q|>=3 and let C be a nonempty subset of L. For every a in C choose a retained live representative

  P_a=(b_a,r_a,...)

with b_a in L, and suppose the HEAD transfer turn

  (q_0,b_a,r_a)                                            (LC.3)

is tight.

Because b_a is itself live, (LC.1) applied to b_a gives

  (q_1,q_0,b_a) tight.                                    (LC.4)

Combining (LC.4), (LC.3), and the inherited turns of P_a shows that

  P_a^+=(q_1,q_0,b_a,r_a,...)

is Hamiltonian on

  A^+-a,   where A^+=A union {q_0,q_1}.

Put

  Q^+=(q_2,q_3,...,q_t),   L^+=C.

Then

  P_a^+ | Q^+

is a literal exact two-cover of H-a for every a in C. Again A^+ is non-Hamiltonian, because otherwise A^+|Q^+ would two-cover H. Therefore

  (A^+,L^+;Q^+)

is another live puncture cylinder.

Crucially, no claim is made that A^+-q_0 or A^+-q_1 is Hamiltonian. The newly absorbed labels may be dead roots. Likewise labels in L-C may be dropped from the live domain. This is exactly why the class is preserved when full deletion-Hamiltonicity is not.

### 4. TAIL dual
If retained representatives expose live terminal labels and the terminal transfer turn succeeds, the same argument with the reverse terminal wall absorbs q_t,q_{t-1}, replaces Q by Q[0,t-2], and preserves a live puncture cylinder on the transferred live labels. No whole-path reversal is invoked.

### 5. Neighboring-support comparisons remain current
For a,b in L, P_a and P_b are Hamilton paths on neighboring supports A-a and A-b and both occur in exact singleton rows with the same literal complement Q. Therefore any accepted R435 comparison between them is source-current in the live cylinder. Replacing P_a or P_b by any other actual Hamilton representative on the same puncture support leaves the cylinder contract unchanged. An R435-active output is retained with its physical ancestry; an R435-quiet comparison retains the common order.

In particular the class is deliberately weaker than a critical block but strong enough to support the next neighboring-support comparison after a simultaneous prefix push. Proper-cycle output may be exported to the movable-break maximum-three-forest family of the sibling section r435-proper-cycle-movable-break-closed-family.

### 6. Scope
This repairs only the closure-under-transition objection to treating SV24412 as a one-step family move. It does NOT show that the new cylinder contains another endpoint-return Hall cycle, because its newly absorbed labels need not be live and transferred paths may expose them as endpoints. It therefore does not justify naive iteration of the same Hall argument. The repeatable state is the live puncture cylinder; the next legal move must be supplied by an actual live-endpoint transfer, a neighboring-support R435 comparison, or an exit to the maximum-three-forest closed-family parent.

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
    }
]
```
