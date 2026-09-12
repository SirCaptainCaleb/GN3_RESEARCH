# R628 is R24-independent: three-terminal parity routing is finite sign bookkeeping

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r628-three-terminal-parity-routing`

**Summary:** R628, `Three Terminal Parity Routing`, is independent of R24. Starting from three terminal witnesses on one tested dimer, assign the binary parity bit used in the theorem to each witness. Equal parity among two witnesses is immediate by pigeonhole and routes to the equal-parity branch; if the theorem's local seam test flips parity after a bad turn, R3 supplies the exact reversed turn and the bit update. The only mixed pattern has one witness in one class and two in the other, already giving the required routed pair. Thus the result is combinatorial bookkeeping on explicit witness turns and does not depend on singleton-deletion rail orders or short complements.

### 1. Input
Retain the R628 three-terminal packet on one tested oriented dimer D with witnesses

  w_1,w_2,w_3.

For each witness the theorem defines one binary parity/sign class from an explicit ordered-turn test. Call it

  chi(w_i) in {0,1}.                                     (R628.1)

### 2. Pigeonhole routing
Among three binary values, at least two are equal. Choose i!=j with

  chi(w_i)=chi(w_j).                                     (R628.2)

This is exactly the equal-parity pair needed for the routed branch of R628. If the chosen class corresponds to a bad seam, accepted R3 converts the bad tested turn into its complete-reversal tight turn, so the physical routed packet remains explicit.

The remaining third witness is retained as the spare terminal certificate required by the alternate branch bookkeeping.

### 3. No global order input
Every step uses only the three physical witnesses, one tested dimer, binary seam outcomes, and R3 reversal. No path-cover theorem, singleton deletion, complement length, or R24 consequence occurs.

Therefore R628 has a direct R24-independent proof.