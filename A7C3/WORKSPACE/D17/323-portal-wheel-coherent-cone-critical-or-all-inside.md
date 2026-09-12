# A phase-minimal coherent wheel is a full critical block unless all six wheel vertices lie in the non-Hamiltonian side

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-coherent-cone-critical-or-all-inside`

**Summary:** Combine the phase extinction of every CURRENT-INCOHERENT wheel with the coherent cone shell SV62430 and bad-row prepayment lift SV67792. In the coherent shell V(H)=Omega disjoint Q, Q is Hamiltonian, Omega non-Hamiltonian, and Q is independent on the six-vertex cone W={x} union K. If x lies in Q, all five roots K lie in Omega and every Omega-d, d in K, is Hamiltonian, so one good root exists. If x lies in Omega but Q meets K, connectedness of the capture graph and independence of Q∩K force a cross capture edge uv with u in Omega, v in Q; its coherent pair-deletion cover gives Omega-u Hamiltonian, again producing a good singleton. Once one good singleton exists, any bad y in Omega has an exact bad row mixing Omega|Q, and SV67792 phase-lifts it at the good source forest to TWO-COVER or strict phased-rank descent. Hence in a nonclosing phase-rank-minimal family no bad y exists: Omega is deletion-Hamiltonian at every vertex, so the cone has promoted to a full fixed-complement critical block. The only coherent cone not covered by this argument has x in Omega and Q∩K empty, i.e. all six distinguished wheel vertices lie in Omega. In that residual all five spokes and every capture edge are Omega-monochromatic, so their coherent pair-deletion covers certify Omega-{x,d} and Omega-{d,e} Hamiltonian. This is the unique surviving wheel geometry, not closure.


### 1. Input: only the support-coherent wheel remains
Work in a hypothetical smallest counterexample H inside a nonclosing reconstruction-closed family chosen minimal for the legitimate SV41376 phased rank. By `portal-wheel-current-branch-phase-extinction` SV68111, every CURRENT-INCOHERENT branch of the full-root wheel is already TWO-COVER / strict phased-rank descent. Hence retain only the SUPPORT-COHERENT shell of SV62430.

Thus there is one global bipartition

  V(H)=Omega disjoint_union Q,                              (CC.1)

with Q carrying a literal Hamilton path and Omega non-Hamiltonian. Let K be the retained Hamilton P5 and x the common hub. Let G_K be the connected underlying all-choice capture graph on the five roots K, and let

  W = {x} union V(K).                                      (CC.2)

SV62430 says Q intersect W is an independent set of the cone over G_K. Every spoke x-d and every retained capture edge de has an exact pair-deletion cover whose support partition is the restriction of Omega|Q. In particular:

- for every cross cone edge uv with u in Omega and v in Q,

    (Omega-u) | (Q-v)                                     (CC.3)

  is an exact pair-deletion support partition, so both Omega-u and Q-v are Hamiltonian;

- for every Omega-monochromatic cone edge uv,

    (Omega-{u,v}) | Q                                     (CC.4)

  is an exact pair-deletion support partition, so Omega-{u,v} is Hamiltonian while Q remains the fixed Hamilton complement.

Call u GOOD when Omega-u is Hamiltonian and BAD when Omega-u is non-Hamiltonian.

### 2. Hub in Q immediately supplies five good roots
Suppose x in Q. Since every spoke x-d belongs to the cone and Q intersect W is independent, no root d in K lies in Q. Hence

  K subset Omega.                                         (CC.5)

Every spoke is a cross edge. Applying (CC.3) to x-d gives

  Omega-d Hamiltonian for every d in K.                   (CC.6)

Thus the coherent cone contains five GOOD singleton labels with one common fixed Hamilton complement Q.

### 3. Hub in Omega with any Q-colored root still supplies a good root
Now suppose x in Omega and

  S := Q intersect K != empty.                            (CC.7)

Because S is independent in the connected graph G_K, S cannot be all five roots: G_K has an edge, while an all-Q root set would contain that Q-monochromatic edge. Hence S is a nonempty proper subset of V(K).

Connectedness of G_K therefore supplies a capture edge

  u v in E(G_K),   u in K-S subset Omega,   v in S subset Q.   (CC.8)

This is a cross cone edge. By (CC.3),

  Omega-u is Hamiltonian.                                 (CC.9)

So again the coherent cone contains at least one GOOD singleton u in Omega.

### 4. One good singleton eliminates every bad singleton by phase lift
Assume either Section 2 or Section 3, and fix one GOOD label g in Omega. Suppose for contradiction that some y in Omega is BAD. Necessarily y != g.

Choose any exact singleton-deletion row C_y of H-y. Since Omega-y is non-Hamiltonian while Q is Hamiltonian, C_y cannot be cut-pure for Omega|Q: if it selected no Omega|Q adjacency, its two nonempty rails would have supports Omega-y and Q, Hamiltonizing Omega-y. Hence C_y contains an actual selected mixed Omega|Q state.

The hypotheses of `fixed-complement-bad-mixed-edge-prepayment-phase-lift` SV67792 now hold with good root g, bad root y, and the same literal Hamilton complement Q. SV67792 produces, before R176/payment, a cross-rail proper tight trimer born at the phase-1 good source forest

  {g} | P_g | Q,                                          (CC.10)

and SV52939 gives TWO-COVER or phased rank strictly below that source checkpoint.

Both alternatives contradict the assumed nonclosing phase-rank-minimal family. Therefore no BAD singleton exists:

  Omega-y is Hamiltonian for every y in Omega.            (CC.11)

Together with Omega itself non-Hamiltonian and Q Hamiltonian, (CC.11) is exactly the full fixed-complement deletion-Hamiltonian critical-block hypothesis.

Hence:

> If a phase-minimal coherent wheel has x in Q, or has x in Omega with Q intersect K nonempty, then its non-Hamiltonian color Omega is already a FULL deletion-Hamiltonian critical block with fixed Hamilton complement Q.

The wheel has ceased to be an independent obstruction and enters the existing fixed-complement critical-block architecture.

### 5. The unique coherent wheel residue is all-inside
The only case not covered by Sections 2-4 is

  x in Omega,
  Q intersect K = empty.                                  (CC.12)

Equivalently,

  W={x} union K subset Omega.                             (CC.13)

Then every wheel spoke x-d and every capture edge de is Omega-monochromatic. The coherent pair-deletion covers therefore give, from (CC.4),

  Omega-{x,d} Hamiltonian for every d in K,                (CC.14)

and

  Omega-{d,e} Hamiltonian for every capture edge de of G_K. (CC.15)

The complement Q is literally Hamiltonian in every one of these pair-deletion fibers.

Thus after the G25 phase-lift wave, the full portal-wheel program has only one genuinely wheel-specific coherent residue: a six-vertex cone lying entirely inside one non-Hamiltonian fixed-complement block, with Hamiltonian pair punctures along all five spokes and the connected capture graph.

### 6. Scope fence
This section does NOT prove a good singleton exists in the all-inside residue (CC.12), and therefore does not silently promote that case to a full deletion-Hamiltonian critical block. Pair-puncture Hamiltonicity (CC.14)-(CC.15) is strictly weaker than singleton-puncture Hamiltonicity.

Likewise, the conclusion is phased-rank relative. SV67792 gives source-relative strict rank descent, so the elimination of BAD labels is asserted inside a nonclosing reconstruction-closed family minimal for the legitimate phased rank, exactly as in G25/SV68111. No R24 or R5 is used.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```