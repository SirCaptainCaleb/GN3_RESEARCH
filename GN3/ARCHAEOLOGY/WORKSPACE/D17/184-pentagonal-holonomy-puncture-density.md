# The short-G1 3-of-6 certificate is a pentagonal-holonomy phenomenon

**Workspace:** D17
**State:** established
**Key:** `pentagonal-holonomy-puncture-density`

**Summary:** The seven-vertex 3-of-6 replacement-density phenomenon used in SV20367 needs only a tight directed five-cycle C=(c0,...,c4) inside a non-Hamiltonian six-set U=C+v, not the remaining short-G1 turns. For every exterior b, at least three of the six supports U-x+b are Hamiltonian. Exact MILP verification of the three rotational four-bad orbit types remains the present certificate. The theorem is genuinely cyclic: replacing C5 by a Hamilton P5 makes all three orbit types feasible, and deleting any one of the five cyclic turns also makes them feasible. Structurally, non-Hamiltonicity of C+v forces at every rim vertex the comparison triangle E_{i-1}->E_i->V_i->E_{i-1}; if C+b is also non-Hamiltonian, a second spoke B_i occupies the same interval and in fact every mixed support (C-c_i)+{v,b} is Hamiltonian. Thus the sharp 3-of-6 residue occurs only when C+b is Hamiltonian. A complete computer-free proof of the two-sheet pentagonal-wheel implication and the remaining Hamilton-apex branch is still open; this section records the stronger reusable formulation and the identified holonomy mechanism without upgrading computational evidence to canonical proof.

### 1. Minimal local hypothesis behind the order-eleven certificate
Let C=(c_0,c_1,c_2,c_3,c_4) be five distinct vertices with all five cyclic turns

  (c_{i-1},c_i,c_{i+1})

tight, indices modulo five. Let v be a sixth vertex and assume

  U=C union {v}

is non-Hamiltonian. Let b be any seventh vertex outside U.

A fresh exact-reversal computation shows the following stronger form of the local lemma used in `singleton-deep-p5-order11-reciprocal-exchange-closure` SV20367:

  #{x in U : U-{x}+{b} is Hamiltonian} >= 3.             (PH.1)

No other short-G1 turn is required. Up to rotation of C, a hypothetical four-bad set has only three forms: four cycle punctures; v plus three cycle punctures whose omitted cycle pair is adjacent; or v plus three cycle punctures whose omitted cycle pair is at cyclic distance two. Each of the three exact-reversal feasibility systems is infeasible.

This is computational/certificate evidence at present, not a computer-free proof.

### 2. One bad apex creates a directed pentagonal wheel
The non-Hamiltonicity assumption already has a clean human consequence. Put

  E_i={c_i,c_{i+1}},   V_i={c_i,v}.

If (v,c_i,c_{i+1}) were tight, then v followed by the cyclic order c_i,c_{i+1},...,c_{i-1} would Hamiltonize U. Hence that turn is bad and R3 gives

  (c_{i+1},c_i,v) tight.                                  (PH.2)

Dually, if (c_{i-1},c_i,v) were tight, the cyclic C-order ending at c_i followed by v would Hamiltonize U, so

  (v,c_i,c_{i-1}) tight.                                  (PH.3)

In the comparison orientation at c_i, the rim turn gives E_{i-1}->E_i, while (PH.2)-(PH.3) give

  E_i -> V_i -> E_{i-1}.                                 (PH.4)

Thus every rim vertex carries the directed local triangle

  E_{i-1} -> E_i -> V_i -> E_{i-1}.                      (PH.5)

The five triangles form one closed pentagonal wheel. This is the first structural layer hidden by the SAT encoding.

As a useful consequence, every cycle puncture U-c_i is Hamiltonian. Choose a remaining rim vertex c_j whose two cyclic neighbors also remain after deleting c_i. The corresponding directed star triangle (PH.5) survives in the five-set U-c_i, so its comparison orientation is cyclic. Accepted R902 therefore makes U-c_i Hamiltonian. Together with C=U-v, the bad-apex six-set U is automatically deletion-Hamiltonian.

### 3. Two bad apexes form a two-sheet wheel and force every mixed puncture computationally
Suppose in addition that C+b is non-Hamiltonian. Repeating (PH.2)-(PH.5) with b gives spokes B_i={c_i,b} satisfying

  E_i -> B_i -> E_{i-1}                                  (PH.6)

at every rim vertex. Thus V_i and B_i occupy the same comparison interval between the two adjacent rim edges. The geometry is a two-sheet pentagonal wheel over the common C5.

A separate exact-reversal check gives the stronger conclusion

  (C-{c_i}) union {v,b} is Hamiltonian for every i.       (PH.7)

Hence if the second apex puncture U-v+b=C+b is bad, all five cycle punctures are good. The 3-of-6 bound is therefore far from sharp in this branch.

The desired human lemma is now sharply isolated:

  TWO-SHEET PENTAGONAL-WHEEL LEMMA (target).
  Two non-Hamiltonian one-apex extensions of one tight C5 force every mixed one-hole six-set to be Hamiltonian.

The present proof of (PH.7) is computational. Its reconstruction should use the five simultaneous local triangles (PH.5)-(PH.6), not a generic density argument.

### 4. The cyclic closure is load-bearing
Two negative controls identify what the finite proof is spending.

First, if the five cyclic turns are replaced by only the three turns of an ordinary Hamilton P5, all three four-bad orbit types become feasible. Second, starting from the full C5, deleting any one of its five cyclic turns again makes all three orbit types feasible.

Therefore (PH.1) is not a consequence of a Hamilton five-support, deletion-Hamiltonicity alone, or a bounded collection of local seams. The complete closed odd cycle is load-bearing. The likely invariant is comparison holonomy around the whole rim: the five local spoke triangles cannot be opened into a path without losing the density conclusion.

### 5. Sharp branch and higher-order target
The 3-of-6 bound itself is sharp. When C+b is Hamiltonian, exact models exist with any prescribed three cycle punctures non-Hamiltonian; then C+b together with the two remaining good cycle punctures gives exactly three good U-puncture extensions. Thus no stronger unconditional local density can be extracted from the minimal hypothesis above.

The human proof naturally splits into two tasks: prove the two-sheet wheel lemma (PH.7), then prove that a Hamilton second apex cannot coexist with four bad mixed punctures. More importantly, the wheel formulation suggests a higher-order analogue: a non-Hamiltonian apex over a tight odd cycle creates one spoke trapped in the reverse rim interval at every vertex. The research question is whether two such sheets, or one sheet plus a Hamilton competing apex, force a positive fraction of mixed puncture Hamiltonicity on longer odd cycles. No higher-order theorem is claimed here.

### 6. Status
The stronger minimal-hypothesis statement (PH.1), the two-bad-apex strengthening (PH.7), sharpness, and the missing-rim-turn/path negative controls have been verified by exact-reversal integer feasibility calculations. The wheel identities (PH.2)-(PH.6) and deletion-Hamiltonicity consequence are symbolic deductions from R3 and R902. A complete human proof of (PH.1) has not yet been obtained. The computational evidence must remain distinct from canonical theorem status.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
