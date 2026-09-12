# The order-four all-star donor obstruction closes by a two-P4 pivot

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-order4-coincident-dimer-closure`

**Summary:** In the |B|=4 specialization of SV16734, if all five source and terminal cyclic R700 tests avoid their P4 branches, then every cycle label z both head- and tail-signs the same reverse middle dimer (b2,b1). For any cycle edge {x,y}, this gives the two tight P4s (x,b2,b1,y) and (y,b2,b1,x). Non-Hamiltonicity of the source donor support {b1,b2,b3,x,y} then forces, by the four prepend/append tests, (b2,x,b3),(b2,y,b3),(b3,x,b1),(b3,y,b1). R3 on {x,b3,y} makes one of (x,b3,y),(y,b3,x) tight, so one of (b2,x,b3,y,b1),(b2,y,b3,x,b1) is a Hamilton P5 on that donor support, closing H with the already Hamiltonian active five-core. Hence the |B|=4 all-no-R700-P4 obstruction is impossible; any surviving order-four donor terminal must contain a specifically supported indexed R700 P4 from the SV16734 ledger.


### 1. Setup
Retain `singleton-deep-p5-five-cycle-donor-amplification` SV16734 and specialize to

  B=(b_0,b_1,b_2,b_3).

Assume first that none of the cyclic R700 tests in SV16734 takes its P4 branch. Then FD.8 gives, for every cycle label z in

  C={u,s,q,t,p},

both

  (b_2,b_1,z) tight,   (z,b_2,b_1) tight.             (O4.1)

Fix any cycle edge D={x,y}. By FD.1 the complementary active support (U-D)+b_0 is Hamiltonian. Therefore the donor support

  W_D={b_1,b_2,b_3,x,y}=(B-b_0) union D

must be non-Hamiltonian, else the two Hamilton paths span H.

### 2. Two opposite endpoint P4s through the coincident inward dimer
From O4.1 for x and y, the words

  P_xy=(x,b_2,b_1,y),
  P_yx=(y,b_2,b_1,x)                                  (O4.2)

are both literal tight P4s.

Test b_3 at both ends of both P4s. If

  (b_1,y,b_3)

were tight, then (x,b_2,b_1,y,b_3) would Hamiltonize W_D. Hence it is bad and R3 gives

  (b_3,y,b_1) tight.                                  (O4.3)

Applying the same append test to P_yx gives

  (b_3,x,b_1) tight.                                  (O4.4)

Likewise, if (b_3,x,b_2) were tight, then

  (b_3,x,b_2,b_1,y)

would Hamiltonize W_D. Therefore R3 gives

  (b_2,x,b_3) tight.                                  (O4.5)

The prepend test on P_yx gives

  (b_2,y,b_3) tight.                                  (O4.6)

All four turns O4.3-O4.6 are forced solely by the assumed donor non-Hamiltonicity.

### 3. One R3 pivot Hamiltonizes the donor
Apply R3 to the three distinct vertices x,b_3,y. Exactly one of

  (x,b_3,y),   (y,b_3,x)

is tight.

If (x,b_3,y) is tight, then O4.5, that turn, and O4.3 certify the Hamilton donor

  (b_2,x,b_3,y,b_1).

If instead (y,b_3,x) is tight, O4.6, that turn, and O4.4 certify

  (b_2,y,b_3,x,b_1).

Either way W_D is Hamiltonian, contradiction. Together with the Hamilton active support (U-D)+b_0 this would be a spanning two-cover of H.

### 4. Consequence
Therefore the |B|=4 all-no-P4 alternative of SV16734 is impossible. In every surviving order-four donor terminal, at least one of the specifically indexed cyclic R700 applications from the ten-test ledger must take its labelled P4 branch.

This does not consume that local R700 P4. It removes the coincident-five-witness dimer as an independent terminal and isolates the indexed P4 branch as the only surviving order-four obstruction.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
