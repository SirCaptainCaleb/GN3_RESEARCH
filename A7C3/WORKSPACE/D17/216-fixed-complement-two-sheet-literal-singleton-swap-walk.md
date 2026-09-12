# The endpoint two-sheet cycle lifts to a literal singleton-swap closed walk of maximum three-forests

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-two-sheet-literal-singleton-swap-walk`

**Summary:** In the SV28285 two-sheet endpoint cycle, each puncture row gives a singleton-rooted maximum forest S_i={y_i}|P_i|Q. Because P_i has endpoints y_{i-1},y_{i+1}, each adjacent cycle edge e_i={y_i,y_{i+1}} has two pair-deletion lifts F_i^- = e_i | (P_i-y_{i+1}) | Q and F_i^+ = e_i | (P_{i+1}-y_i) | Q. S_i<->F_i^- and F_i^+<->S_{i+1} are reversible one-edge endpoint swaps. F_i^- and F_i^+ have identical support partition and fixed complement Q; declaring the exact reversible RAIL-REORDER edge between their two actual Hamilton words yields a 3ell-step closed walk S_0,F_0^-,F_0^+,S_1,...,S_0 of literal maximum three-forest representatives. In the endpoint-endpoint selected-reversal residue, each middle RAIL-REORDER retains the named oppositely selected physical dimer from SV27136. The forward and reverse endpoint-core matchings are therefore the two orientations of one explicit closed representative walk, not merely an abstract matching holonomy. No extinction or two-cover is claimed.

### 1. Two-sheet endpoint cycle
Retain the endpoint-endpoint two-sheet residue SV28285 in a hypothetical smallest Strong Level-(1) counterexample:

  V(H)=Omega disjoint_union V(Q),

with Q a fixed literal Hamilton path and

  y_0 -> y_1 -> ... -> y_{ell-1} -> y_0,

ell even, an endpoint-return cycle. For each i retain the actual Hamilton puncture path P_i on Omega-y_i. The two-sheet theorem gives

  End(P_i)={y_{i-1},y_{i+1}}.                            (LW.1)

Indices are modulo ell.

### 2. Singleton-rooted maximum representatives
For every i put

  S_i={y_i} | P_i | Q.                                  (LW.2)

This is a literal spanning three-path cover of H. Since H is a smallest counterexample and therefore pc(H)=3 by accepted R4, every S_i is a maximum compatible spanning three-forest.

These S_i are the natural literal states associated with the endpoint-return labels. Unlike the endpoint-core matching itself, they live directly in maximum-three-forest representative space.

### 3. The common pair-deletion bridge on every cycle edge
Fix the physical cycle edge

  e_i={y_i,y_{i+1}}.

Because y_{i+1} is an endpoint of P_i, deleting it leaves one Hamilton path

  A_i=P_i-y_{i+1}

on

  C_i=Omega-{y_i,y_{i+1}}.                              (LW.3)

Likewise y_i is an endpoint of P_{i+1}, so

  B_i=P_{i+1}-y_i                                       (LW.4)

is another Hamilton path on the same support C_i.

Orient the order-two rail e_i arbitrarily when it is displayed as a path. Then

  F_i^- = e_i | A_i | Q,
  F_i^+ = e_i | B_i | Q                                 (LW.5)

are literal spanning three-path covers of H, hence maximum three-forests.

In the endpoint-endpoint selected-reversal residue of SV27136, A_i and B_i additionally retain one named common physical dimer selected in opposite directions. That selected reversal is not needed for existence of (LW.5), but it is the nontrivial physical datum carried by the middle transition below.

### 4. Endpoint swap is a reversible one-edge transition
The passage

  S_i <-> F_i^-                                         (LW.6)

is a literal one-edge endpoint exchange.

For example, if P_i begins

  P_i=(y_{i+1},a_0,a_1,...),

then S_i selects the edge y_{i+1}a_0 while F_i^- selects y_i y_{i+1}; every other selected edge is unchanged. Replacing y_{i+1}a_0 by y_i y_{i+1} leaves the inherited path A_i and the dimer e_i, so the resulting forest is literal and compatible. Reversing the replacement restores the certified initial segment of P_i. If y_{i+1} is the tail of P_i, the identical argument uses the last selected edge of P_i instead.

Call (LW.6) ENDPOINT-SWAP. It is reversible and changes exactly one selected ordinary edge.

The same argument on P_{i+1} gives the second reversible endpoint swap

  F_i^+ <-> S_{i+1}.                                    (LW.7)

### 5. Same-support rail reorder is an exact reversible representative edge
The two middle states F_i^- and F_i^+ have identical unordered support partition

  e_i | C_i | V(Q)                                      (LW.8)

and the same literal complement rail Q. Their only difference is that the C_i rail uses the actual Hamilton word A_i in one state and the actual Hamilton word B_i in the other.

Declare the following narrow exact transition in the augmented literal representative graph:

  RAIL-REORDER: if two maximum three-forests have identical support partition and two literal rails are unchanged, while the third support carries two retained actual Hamilton words, one may replace the first word by the second.                         (LW.9)

This is reversible because both endpoint states are already literal maximum three-forests; no unproved intermediate compatibility is asserted. Applied to (LW.5), it gives

  F_i^- <-> F_i^+.                                      (LW.10)

In the present endpoint-reversal residue, (LW.10) retains the full two Hamilton words and the named common dimer that they select oppositely. Thus RAIL-REORDER does not quotient away the selected-edge holonomy.

### 6. Explicit closed representative walk
Combining (LW.6), (LW.10), and (LW.7) for every i gives the literal closed walk

  S_0,
  F_0^-, F_0^+,
  S_1,
  F_1^-, F_1^+,
  ...,
  S_{ell-1},
  F_{ell-1}^-, F_{ell-1}^+,
  S_0.                                                   (LW.11)

Every vertex of (LW.11) is an actual maximum spanning three-forest. Every ENDPOINT-SWAP edge is a one-selected-edge reversible move. Every RAIL-REORDER edge preserves all three supports and the fixed complement Q while retaining the two competing Hamilton words. In the SV28285 endpoint-reversal case, each RAIL-REORDER carries an explicit selected-state reversal inherited from SV27136.

The reverse endpoint-core matching of SV28285 traverses the same physical macrocycle in the opposite direction. Hence the two matching sheets are exactly the two orientations of one closed current representative walk after the declared factorization (LW.11).

### 7. Scope
This theorem supplies the finite recurrence object requested by the G10 minimal-holonomy program. It does not prove that the walk (LW.11) is shortest, does not prove that its selected-edge holonomy is nontrivial after one full circuit under every possible notion of transport, and does not itself produce a two-cover.

The exchange graph has been explicitly enlarged by the narrowly defined RAIL-REORDER edge (LW.9); shortest-walk claims in any later argument must state whether this edge type is included. The value here is currentness: the endpoint two-sheet residue is now a closed walk of literal maximum representatives with all supports, words, endpoint swaps, fixed complement, and selected reversal data retained.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    }
]
```
