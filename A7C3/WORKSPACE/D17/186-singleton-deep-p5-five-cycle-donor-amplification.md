# Five-cycle donor restoration forces closure, indexed P4s, or two-ended inward stars

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-five-cycle-donor-amplification`

**Summary:** In the accepted short G1 universe, the four SV16347 deleted-pair choices extend to all five edges of the tight cycle C5=(u,s,q,t,p,u): the fifth pair {p,u} is legal because its active complement {s,q,t,v} plus either B-endpoint contains the q-centered comparison cycle qv->qs->qt->qv and is Hamiltonian by R887/R902. For each cycle edge and the source deletion b0, R700 on the corresponding cyclic trimer with probes b1,b2 gives either a labelled P4, or the first donor seam; if the second seam fails, R3 forces the first-inward star (b2,b1,a_i). The terminal deletion is dual and forces (a_i,b_{k-1},b_{k-2}). Hence if no donor closes H, every one of the ten endpoint/edge tests is certified blocked by a specifically supported R700 P4 or a named inward-star turn. If no such P4 occurs, all five cycle labels simultaneously satisfy both first-inward star families. For |B|=4 the two star supports coincide on the dimer (b2,b1); for |B|>=5 any four labels instantiate accepted R974. This is an exhaustive donor obstruction ledger, not a claim that a local P4 itself closes H.


### 1. Setup and the missing fifth donor pair
Retain accepted `singleton-deep-p5-short-r961-currentization` SV16094 and current `singleton-deep-p5-short-pair-support-transfer` SV16347. Write

  U={s,q,t,p,u,v},
  B=(b_0,b_1,...,b_k),

with B literal Hamiltonian and B+z non-Hamiltonian for every z in U. Retain the tight cycle

  C_5=(a_0,a_1,a_2,a_3,a_4)=(u,s,q,t,p)

cyclically, so

  (a_i,a_{i+1},a_{i+2})

is tight for every i modulo 5. The four deleted pairs in SV16347 are four of the five cycle edges. The omitted edge is

  D_4={p,u}={a_4,a_0}.

Its active complement in U is

  X_4={s,q,t,v}.

The turns

  (v,q,s), (s,q,t), (t,q,v)

are retained from SV16094 and give the directed comparison cycle

  qv -> qs -> qt -> qv

inside X_4. Therefore for either physical endpoint b in {b_0,b_k}, the five-set X_4+{b} still contains this directed comparison cycle. Accepted R887/R902 implies X_4+{b} is Hamiltonian. Thus the support-transfer menu extends from the four SV16347 pairs to all five cycle edges

  D_i={a_i,a_{i+1}}, i in Z/5Z.                    (FD.1)

For every i and either endpoint b of B, the active support (U-D_i)+b is Hamiltonian. Consequently, if the donor support

  (B-b) union D_i

is Hamiltonian for any i,b, the two Hamilton paths are disjoint and span H, contradiction. The hard branch may therefore assume every one of these ten donor supports is non-Hamiltonian.

By `singleton-deep-p5-short-donor-order-floor` SV16604, every surviving short-cell branch has |B|>=4, so b_2 and b_{k-2} below exist.

### 2. Source-end donor tests
Fix i modulo 5 and delete b_0 from B. Apply accepted R700 to the tight cyclic trimer

  K_i=(a_i,a_{i+1},a_{i+2})

with the two distinct probes b_1,b_2.

If R700 takes its P4 branch, retain the exact statement

  K_i union {b_j} supports a Hamilton P4 for some j in {1,2}.  (FD.L-P4_i)

No closure is inferred from this local P4.

Otherwise R700 is in DUAL-CP. Its reverse-initial-dimer conclusion gives in particular

  (a_{i+1},a_i,b_1) tight.                            (FD.2)

Now test the complete literal donor word

  L_i=(a_{i+1},a_i,b_1,b_2,...,b_k).                 (FD.3)

Every turn after the first two displayed seams is inherited from B. The first seam is FD.2. Hence the only uncertified turn is

  (a_i,b_1,b_2).                                      (FD.4)

If FD.4 is tight, L_i Hamiltonizes (B-b_0) union D_i and closes H with the already Hamiltonian active support (U-D_i)+b_0. Therefore in a counterexample FD.4 is bad, and R3 forces

  (b_2,b_1,a_i) tight.                                (FD.L_i)

Thus for each i, source-end donor failure is certified by exactly one of:

  (a) labelled P4 FD.L-P4_i, or
  (b) first-inward star FD.L_i.

In particular, if none of the five source R700 tests takes its P4 branch, then

  (b_2,b_1,z) tight for every z in {u,s,q,t,p}.       (FD.L*)

### 3. Terminal-end donor tests
Fix i modulo 5 and delete b_k. Apply R700 to the tight cyclic trimer

  K'_i=(a_{i-1},a_i,a_{i+1})

with probes b_{k-2},b_{k-1}.

If R700 takes P4, retain

  K'_i union {b_j} supports a Hamilton P4

for some j in {k-2,k-1}.                              (FD.R-P4_i)

Otherwise DUAL-CP gives the reverse-terminal-dimer contact, using probe b_{k-1},

  (b_{k-1},a_{i+1},a_i) tight.                        (FD.5)

Test the donor word

  R_i=(b_0,...,b_{k-2},b_{k-1},a_{i+1},a_i).         (FD.6)

All turns are inherited except the two terminal seams. FD.5 certifies the second; the only uncertified turn is

  (b_{k-2},b_{k-1},a_{i+1}).                          (FD.7)

If FD.7 is tight, R_i Hamiltonizes (B-b_k) union D_i and closes H with the Hamiltonian active support (U-D_i)+b_k. Hence in the hard branch FD.7 is bad, so R3 gives

  (a_{i+1},b_{k-1},b_{k-2}) tight.                    (FD.R_i)

As i runs around the cycle, a_{i+1} runs through all five labels. Therefore, absent every terminal R700 P4,

  (z,b_{k-1},b_{k-2}) tight for every z in {u,s,q,t,p}.  (FD.R*)

### 4. Exhaustive ten-test obstruction ledger
Assume no donor restoration closes H. For each of the five cycle edges at each of the two endpoints of B, the corresponding test is then blocked in one of two graph-intrinsic ways:

- a specifically supported R700 P4 on one cyclic trimer plus one of the two exposed B probes; or
- the named first-inward star turn FD.L_i or FD.R_i.

Thus all ten available endpoint/cycle-edge donor choices are covered by a finite labelled obstruction ledger. No P4 is treated as closure and no generic R542/R435 payment is taken.

If the ledger contains no P4 entry at all, then the five cycle labels satisfy both simultaneous universal first-inward families FD.L* and FD.R*.

### 5. Long and order-four all-no-P4 forms
If |B|>=5, choose any four labels X from {u,s,q,t,p}. With Q=B, the turns FD.L* and FD.R* are exactly the universal first-inward hypotheses

  (q_2,q_1,x), (x,q_{m-1},q_{m-2})

of accepted R974 for every x in X. Therefore the all-no-P4 donor obstruction enters the accepted R974 two-ended path/static-sign/capture compiler. This statement only currentizes that compiler; it does not claim its later alternatives close H.

If |B|=4, write B=(b_0,b_1,b_2,b_3). Then q_2=b_2=q_{m-1} and q_1=b_1=q_{m-2}; the two inward star families collapse onto the same oriented physical dimer:

  (b_2,b_1,z) and (z,b_2,b_1) tight

for every z in {u,s,q,t,p}.                           (FD.8)

Thus the unique short all-no-P4 obstruction is a single reverse middle dimer of B simultaneously tail- and head-signed by all five cycle labels. R974 is not invoked at this order.

### 6. Consequence and fence
The v45 donor-restoration target has the following exact finite reduction. Either:

1. some donor (B-b) union D_i is Hamiltonian, giving a spanning two-cover of H;
2. the ten-test ledger contains at least one labelled R700 P4, whose exact cyclic-trimer/B-probe support is retained; or
3. no ledger P4 occurs, in which case all five cycle labels form simultaneous first-inward stars at both ends of B, entering R974 when |B|>=5 and collapsing to the coincident five-witness dimer FD.8 when |B|=4.

The unresolved work is specifically to consume the labelled R700-P4 ledger entries and the |B|=4 coincident-dimer obstruction. Neither is silently promoted to closure.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R700"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R974"
    }
]
```
