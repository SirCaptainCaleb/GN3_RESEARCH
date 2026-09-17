# Shortest-rim and native DOUBLE data alone do not force escape

**Workspace:** D17
**State:** limitation
**Key:** `compatible-forest-shortest-rim-native-trap-diagnostic`

**Summary:** Computational exact-reversal diagnostics fence an overstrong minimal-holonomy strategy. A shortest ordinary C6 can coexist with a Hamilton four-rail whose source is globally LOW, terminal globally HIGH, all rim/source and rim/terminal endpoint seeds DOUBLE, and every whole-rim insertion across every rail cut blocked, with no MID spoke at all. More strongly, a 14-vertex system with shortest C6 and two Hamilton four-rails simultaneously realizes all Q-U and Q-V cyclic-break DOUBLE families and both remaining ordered U-V DOUBLE seeds. That full native all-six-DOUBLE pattern is feasible and the witness is Hamiltonian. Therefore shortestness plus native six-seed gate data is insufficient; fresh representatives forced by smallest-counterexample minimality are logically necessary. Computational diagnostic only, not canonical theorem evidence.

### 1. Diagnostic purpose
This section records finite exact-reversal tests of an overstrong version of the G7 minimal-holonomy program. It is a strategy fence, not canonically reviewed mathematics. The solver assignments are not promoted as standalone exact certificates.

### 2. One-rail C6 trap
Take Q={0,1,2,3,4,5} and U={6,7,8,9}. Use one binary variable for each exact boundary-reversal pair, 360 variables total. Impose: no star comparison triangle; no ordinary directed comparison cycle of lengths 3,4,5; Q is a directed comparison C6; U=(6,7,8,9) is tight; source 6 is globally LOW and all source-side rim merge seeds are DOUBLE; terminal 9 is globally HIGH and all terminal-side rim merge seeds are DOUBLE; and for every cut of U and every cyclic break of Q, the complete whole-rim insertion word has at least one bad new turn.

SciPy/HiGHS reports the 4676-constraint system feasible. The returned spoke-state words are

  6: L L L L L L,
  7: L L L L L L,
  8: L H H L L L,
  9: H H H H H H.

Thus no U-vertex need have any MID spoke. The three-site MID interval theorem, even combined with all endpoint DOUBLE walls, does not force one-rail rim insertion.

### 3. Full native all-six-DOUBLE pattern
Take Q={0,1,2,3,4,5}, U={6,7,8,9}, V={10,11,12,13}. The exact-reversal model has 1092 binary variables. Impose: no star comparison triangles; no ordinary directed cycles of lengths 3,4,5; Q is the shortest directed C6; U and V are tight Hamilton four-paths; for each R in {U,V}, every cyclic break of Q has the Q-to-R source family DOUBLE with the R-source globally LOW and the R-to-Q terminal family DOUBLE with the R-terminal globally HIGH; and the remaining ordered seeds U_terminal->V_source and V_terminal->U_source are DOUBLE.

The resulting 31,481-constraint MILP is feasible. A direct Hamilton-path dynamic program on the returned boundary system finds the spanning tight Hamilton order

  (9,11,8,10,7,6,12,0,1,2,3,4,5,13).

So even the entire native all-six-DOUBLE pattern can occur in a Hamiltonian boundary system.

### 4. Consequence
The following purely local parent formulation is false:

  shortest ordinary rim + SOURCE/SINK chord rigidity + all six native DOUBLE root gates => contradiction.

The missing force must use additional smallest-counterexample structure, in particular fresh exact representatives created from the reverse-P4 complements. The section `compatible-forest-rim-double-crossing-fan` records the corresponding family-level crossing portals. No inference against Global Three-Forest Escape is made.
