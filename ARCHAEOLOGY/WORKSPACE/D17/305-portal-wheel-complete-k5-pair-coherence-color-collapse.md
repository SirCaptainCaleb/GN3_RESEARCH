# Quiet full-wheel coherence propagates to all ten K-pairs and leaves only 5-0 or 4-1 root colorings

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-complete-k5-pair-coherence-color-collapse`

**Summary:** Strengthen SV62139's coherent full-wheel branch. Once all five spoke partitions glue to P*=A|B and a connected rim skeleton has one constant hub-side bit, take any missing pair {d,e} of P5 roots. The Johnson triangle {x,d,e} either exposes current common-residue crossing/component-drop geometry, or its pair-deletion cover trims to the same spoke partition. Comparing that cover with any already coherent rim-skeleton edge incident to d pins its hub-side bit; otherwise the adjacent-pair common-shadow argument of SV61535 again gives a current crossing. Therefore outside current geometry every one of the ten pair-deletion fibers H-{d,e}, d,e in K, has an exact representative whose support partition is P* restricted. With x in A, if K contains at least one A-root then its spoke makes B Hamiltonian; if K contains at least two B-roots, deleting that B-B pair makes A Hamiltonian. Thus any coloring with 1<=|K cap A|<=3 closes H. If |K cap A|=0, A is Hamiltonian and B is the unique non-Hamiltonian block, with B-d Hamiltonian for all five d in K. If |K cap A|=4, B is Hamiltonian and A is the unique non-Hamiltonian block, with A-x and A-d Hamiltonian for every A-colored root d, so {x} plus the four A-roots are five Hamilton-deletable vertices. If |K cap A|=5, B is Hamiltonian and A is the only non-Hamiltonian block, with every A-{x,d} and every A-{d,e} (d,e in K) Hamiltonian. Hence the coherent full-wheel residue has only the 5-0/4-1 extreme color patterns, a much smaller critical-block target.

### 1. Setup: coherent full five-root wheel
Retain the quiet coherent full-root branch of SV62139. Thus K is the physical Hamilton P5, x is the common hub, every one of the five spoke pairs {x,d}, d in K, has a chosen exact pair-deletion cover, and a connected spanning rim skeleton G_R on K has chosen exact covers. Outside current common-residue crossing/component-drop geometry, SV61535/SV62139 glue these covers to one global bipartition

  P*=A|B,   x in A.                                       (KC.1)

Every chosen spoke and rim-skeleton cover has support partition equal to the restriction of P*.

### 2. Every missing K-chord inherits the same global partition
Fix any distinct d,e in K, whether or not {d,e} is an edge of the chosen rim skeleton. Accepted R429 supplies an exact cover

  F_de of H-{d,e}.

Apply the Johnson-triangle compiler of SV61535 to the three pair fibers

  {x,d}, {x,e}, {d,e}.                                    (KC.2)

If the surviving third vertex is internal in one cover, or if the three endpoint trims disagree on the common triple-deletion residue, we obtain the CURRENT crossing/component-drop branch and stop. Hence assume the triangle support-commutes. Then trimming x from F_de gives exactly P* restricted to H-{x,d,e}; the only remaining freedom is which P*-side receives x in F_de.

Choose any rim-skeleton edge {d,f} incident with d; if d is a leaf of the tree skeleton it still has such an edge, and when e=f the desired pair is already coherent. Otherwise compare F_de and the coherent cover F_df on their common triple-deletion shadow H-{d,e,f}. If e or f is internal in its respective cover, deleting it gives the current component-drop branch. If both are endpoints, their trims are exact two-covers. All nonhub vertices have the same P*-side, so opposite choices for x would make the two trimmed support partitions differ; accepted R410 then gives a current selected crossing.

Therefore outside current geometry the hub-side bit of F_de equals the already fixed coherent bit. Hence

  every pair {d,e} subset K has an exact H-{d,e} cover
  whose support partition is P* restricted to V(H)-{d,e}.   (KC.3)

Thus quiet coherence propagates from a connected rim skeleton to the complete K5 of root-pair deletion fibers.

### 3. Same-color root pairs certify the opposite full block
Write

  K_A=K cap A,   K_B=K cap B.                              (KC.4)

For every d in K_A, the spoke deletion {x,d} removes two A-vertices, so its coherent exact cover has rails

  A-{x,d}  |  B.

Therefore

  K_A nonempty  =>  B is Hamiltonian.                     (KC.5)

For every distinct d,e in K_B, KC.3 supplies an exact cover with rails

  A  |  B-{d,e}.

Therefore

  |K_B|>=2  =>  A is Hamiltonian.                          (KC.6)

If both KC.5 and KC.6 hold, A|B is a spanning two-cover of H. Since |K|=5, every coloring with

  1 <= |K_A| <= 3                                         (KC.7)

has |K_B|>=2 and therefore closes H.

The only quiet nonclosing color counts are

  |K_A| in {0,4,5}.                                       (KC.8)

This is independent of the particular spanning rim skeleton.

### 4. The three extreme critical residues
CASE 0: |K_A|=0. Then K subset B. Any K-pair deletion makes A an intact Hamilton rail, so A is Hamiltonian. Counterexamplehood forces B non-Hamiltonian. Every spoke {x,d}, d in K, has rails

  A-x | B-d,

so

  A-x Hamiltonian and B-d Hamiltonian for all five d in K. (KC.9)

Thus B is a non-Hamiltonian block with FIVE distinguished Hamilton-deletable roots forming the Hamilton P5 K.

CASE 4: |K_A|=4 and K_B={b}. Since K_A is nonempty, B is Hamiltonian. A must be non-Hamiltonian. The spoke {x,b} gives A-x Hamiltonian. For every a in K_A, the complete K5 pair coherence KC.3 applied to {a,b} gives rails

  A-a | B-b,

so A-a is Hamiltonian. Therefore

  A is non-Hamiltonian but A-v is Hamiltonian for every
  v in {x} union K_A, a five-vertex distinguished set.      (KC.10)

Additionally every A-A root pair deletion gives A-{a,a'} Hamiltonian with B intact.

CASE 5: |K_A|=5. Again B is Hamiltonian and A is non-Hamiltonian. Every spoke gives

  A-{x,d} Hamiltonian, d in K,                            (KC.11)

and every K-pair deletion gives

  A-{d,e} Hamiltonian, distinct d,e in K.                 (KC.12)

This is a highly overdetermined two-deletion Hamilton shell on the six distinguished vertices K union {x}.

### 5. The original SV58280 source pair also becomes coherent or noisy
Let {a_0,c_0} be the original deleted pair whose exact source cover U|V produced K in SV58280. Both labels lie in K. KC.3 supplies an exact H-{a_0,c_0} cover with support partition P* restricted. Compare it with the original source cover U|V. If their support partitions differ, accepted R410 gives a current same-residue crossing. Hence in the fully quiet branch the ORIGINAL source frame itself has the P* partition. In particular the three internal vertices b_1,b_2,b_3 used to build K retain their actual rail locations inside the appropriate global blocks. This keeps the source-frame ancestry available for the next critical-block consumer.

### 6. Remaining target
The full coherent wheel is therefore no longer an arbitrary one-Hamilton-block configuration. Outside current crossing/component-drop geometry it lies in exactly one of the three extreme root-color residues KC.9-KC.12. The mixed colorings 1-3 close immediately.

No claim is made here that Cases 0,4,5 close. Case 0 is a five-root partial hypohamiltonian block; Case 4 has five named one-vertex Hamilton deletions; Case 5 has a complete distinguished two-deletion Hamilton shell. These are the next theorem-scale targets. The R195 conclusion from SV62139 that at least three K-d+x five-sets are Hamiltonian remains simultaneously available in all three cases.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```