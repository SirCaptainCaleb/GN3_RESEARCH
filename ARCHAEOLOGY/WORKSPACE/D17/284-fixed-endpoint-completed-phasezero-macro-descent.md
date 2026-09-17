# Quiet steps and paid pair excursions form one strict fixed-endpoint phase-zero macro descent

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-completed-phasezero-macro-descent`

**Summary:** Combine the fixed-endpoint quiet clock SV56573 with the paid-exit return map SV57138. Fix E and Psi_E=(2-|A_E|,M-2,delta_E). Define a completed phase-zero macro to be either one ordinary quiet nonclosing nonexit fixed-E macro, or a certificate-bearing balanced-pair excursion followed through payment, R432 steering to the old E, and the R1022 entrance return. If that paid return is already strict in Psi_E, stop. If it is rank-flat, do not declare a macro boundary there: append the first selected-incidence episode at the rebased middle. By the middle-independent endpoint ledger, that appended episode either hits a spent endpoint and terminates in explicit R436 nonquiet geometry, or uses a fresh endpoint and any quiet completed return strictly decreases epsilon_E. Consequently every completed macro avoiding closure and explicit nonquiet geometry strictly lowers Psi_E. Hence the entire quiet-plus-paid-pair phase-zero sector is well founded on the fixed endpoint pair without adding any new rank coordinate; the only surviving phase-zero obstruction is explicit nonquiet portal geometry. This includes the SV50987 mass-four and R920/R159 cross-state excursions via SV57138.

### 1. Fix the endpoint-pair state space
Fix a physical endpoint pair

  E={a,c}

in a hypothetical smallest Strong Level-(1) counterexample. Retain the physical completed-endpoint ledger A_E of the fixed-endpoint quiet theorem SV56573. For an active ancestry-bearing balanced pair of mass M, and singleton floor S when M=2, put

  epsilon_E=2-|A_E|,
  delta_E=0                    if M>2,
  delta_E=2-|S intersect E|    if M=2,

  Psi_E=(epsilon_E,M-2,delta_E).                         (CM.1)

We consider only phase-zero motion that preserves the physical pair E as the target coordinate. Middle vertices are gauge choices at aligned checkpoints.

### 2. Two primitive kinds of phase-zero motion
There are two already-established classes.

**QUIET primitive.** SV56573 proves that every quiet, nonclosing, nonexit fixed-E continuation macro, allowing arbitrary middle rebasing at aligned checkpoints, strictly decreases Psi_E.

**PAID-PAIR primitive.** SV57138 proves that any explicit exit carrying a certificate-bearing balanced pair with a lawful finite descent to a genuine both-singleton floor has a finite same-old-E return:

  pair birth / exit
  -> certificate-retaining payment to a floor
  -> R432 steering to E
  -> R1022 entrance checkpoint at E with some internal middle b'.

At the returned checkpoint

  Psi_E,ret <= Psi_E,old.                                 (CM.2)

The inequality is strict unless the old checkpoint was already an E-aligned mass-two floor, A_E did not grow during the excursion, and therefore all three coordinates return unchanged. This is the unique equality stratum.

### 3. Do not place a macro boundary at a rank-flat paid return
The equality in (CM.2) is not a recurrence mechanism. It is an artifact of stopping the excursion one elementary episode too early.

Accordingly define a COMPLETED PAID MACRO as follows. Run the paid-pair primitive through its same-E R1022 return.

- If H closes, stop.
- If Psi_E has strictly decreased, end the macro at that returned checkpoint.
- If Psi_E is unchanged, do NOT declare a macro boundary. At the returned aligned floor choose any admissible middle b' supplied by the R1022 entrance and append the first selected-incidence episode at b'.

The physical endpoint ledger has not reset under this rebase. Hence the appended episode has only two possibilities.

1. Its anchored endpoint e already lies in A_E. Then the old historical singleton anchor and the genuinely later endpoint-anchored dimer trigger accepted R436, so the macro terminates at an explicit nonquiet growth/cycle/reversal/contact portal.
2. The anchored endpoint e is fresh. Then the protected R434 continuation either emits explicit nonquiet geometry/closure or completes a quiet E-aligned return with e adjoined to A_E. In the latter case epsilon_E decreases by one, while it is the first lexicographic coordinate. Therefore Psi_E strictly decreases.

Thus a rank-flat paid return is only an internal plateau of one larger macro; it cannot be the endpoint of a quiet completed macro.

### 4. Completed phase-zero macro theorem
Call a COMPLETED PHASE-ZERO MACRO either:

- one quiet primitive from SV56573; or
- one completed paid macro of Section 3.

Then every such macro has exactly one of the following outcomes:

  TWO-COVER;
  EXPLICIT NONQUIET PORTAL;
  STRICT DECREASE OF Psi_E.                               (CM.3)

In particular, along any chosen continuation that avoids closure and all explicit nonquiet portals, every completed macro strictly lowers the nonnegative lexicographic triple Psi_E. Therefore the quiet-plus-paid-pair phase-zero sector is well founded. There is no need to append a return-bit, middle index, or representative identifier to the rank.

This is stronger than saying paid excursions are merely nonincreasing: after choosing the correct macro granularity, every portal-free completed excursion is strictly decreasing.

### 5. The two G21 test excursions are included
The transverse-cap SV50987 pair is mass four and enters the paid primitive through accepted R514, so its same-E excursion is a completed paid macro.

The R920 all-internal component-drop pair is born through the R159 proof's selected cross-state and accepted R176; accepted R415 lawfully pays that certificate-bearing pair. Hence it is also a completed paid macro.

For both test objects the only way to avoid strict fixed-E descent is to arrive at the rank-flat aligned stratum and immediately expose explicit nonquiet geometry at the appended incidence episode. Neither object can create a silent phase-zero reset.

### 6. Relation to the phased global Morse program
SV41376 used the phase-zero fixed-turn clock only on quiet nonexit continuations and therefore left PRODUCTIVE-EXIT REENTRY as the exact global obligation. SV56573 quotients the quiet clock by the middle, and SV57138 handles certificate-bearing pair exits. The present section says these two pieces compose without a new coordinate: pair exits that can be genuinely paid belong inside the same fixed-E descending macro calculus.

Thus PRODUCTIVE-EXIT REENTRY has been reduced further. Among phase-zero exits, every certificate-bearing balanced-pair excursion is now consumed into strict same-E descent unless it exposes an explicit nonquiet portal. The remaining global obstruction is no longer payment, floor steering, R1022 reentry, or middle mismatch. It is the consumption of the explicit nonquiet geometry itself, especially in the fully anchored stratum A_E=E.

### 7. Scope fence
This theorem does NOT say an arbitrary trimer, proper cycle, R435 event, or universal four-core automatically carries a payable pair. It does not consume an R436 portal after that portal appears. It applies exactly to ordinary quiet fixed-E macros and to explicit exits whose balanced-pair birth has the certificate provenance required by R415/R514 or an equivalent lawful payment theorem.

Current versus historical data remain separated throughout: old endpoint certificates persist as graph-intrinsic ancestry, but old exact covers or representatives are not asserted simultaneously current after payment/steering. Frozen quarantined roots are not used.