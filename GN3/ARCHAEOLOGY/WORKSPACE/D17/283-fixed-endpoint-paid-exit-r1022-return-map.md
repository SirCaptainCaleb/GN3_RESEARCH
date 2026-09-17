# Paid pair exits return nonincreasingly to the old endpoint clock; R1022 supplies a new admissible middle

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-paid-exit-r1022-return-map`

**Summary:** Fix an old physical endpoint pair E and the middle-independent completed-anchor ledger A_E of SV56855. Any explicit exit that lawfully pays to an ancestry-bearing both-singleton floor can be returned to the old E without increasing the candidate endpoint clock Psi_E=(2-|A_E|,M-2,delta_E): pay to a floor, steer that floor to E by R432, and use the entrance construction inside accepted R1022 with target pair E to obtain an exact H-E frame with an internal new middle b' and a proper turn on the same physical pair. Historical A_E certificates survive because they are graph-intrinsic anchor facts; middle rebasing is then governed by SV56855. At the returned checkpoint Psi_E=(2-|A_E|,0,0), so the macro is strict whenever A_E grew, the old mass exceeded two, or the old mass-two floor was not already E-aligned. Equality is possible only at an already E-aligned mass-two checkpoint with unchanged A_E; there the new middle does not reset the budget, and any ensuing selected-incidence episode either completes a fresh endpoint and strictly lowers epsilon_E or is immediately nonquiet. SV50987 enters through accepted R514. The R920 all-internal component-drop branch also enters lawfully: accepted R159 is proved by an R176 selected-cross-state birth, and R415 explicitly accepts an R176 pair as certificate-bearing payment input. Thus neither test object loses the old endpoint ledger; the surviving obstruction is only the explicit nonquiet portal at the rank-flat aligned stratum.

### 1. Old endpoint-pair checkpoint
Let H be a hypothetical smallest Strong Level-(1) counterexample. Fix an OLD physical endpoint pair

  E={a,c}

and retain the middle-independent endpoint ledger A_E of SV56855. Thus every e in A_E carries a historical graph-intrinsic signed-singleton certificate from a completed quiet selected-incidence return, possibly born at a middle different from the one currently displayed.

For an active ancestry-bearing balanced pair of mass M, define

  Psi_E=(2-|A_E|, M-2, delta_E),

where delta_E=0 for M>2, while at a mass-two floor with singleton set S,

  delta_E=2-|S intersect E|.

This section analyzes an explicit exit that has a lawful certificate-retaining route to a genuine ancestry-bearing both-singleton floor. It does not assume that the exit supports, witnesses, or current representative use E.

### 2. Historical endpoint data survive unrelated pair payment
The certificates defining A_E are graph-intrinsic historical signed-anchor facts. A later payment excursion can change active representatives and pair supports but cannot make those earlier path/sign facts false. We therefore retain A_E as a side ledger throughout the exit. If the exit itself completes another protected endpoint episode, enlarge A_E accordingly; write A_E^+ for the ledger after the exit and A_E^- for the old ledger. Always

  A_E^- subseteq A_E^+.

For the mass-four route this persistence is explicit in accepted R514: separately certified graph-intrinsic static configurations remain valid historical data throughout the chosen R427/R428 continuation. For an R176/R415 route, R415 preserves the pair-birth/refund ancestry, while the pre-existing A_E certificates remain separately retained graph-intrinsic history. No simultaneous currentness of old representatives is asserted.

### 3. Pay to a genuine floor and steer back to the OLD pair E
Assume the exit does not close H. By hypothesis its certificate-retaining payment reaches an ancestry-bearing both-singleton floor. Let S be its two physical singleton supports. Apply accepted R432 with the prescribed target pair E. Outside a spanning two-cover, R432 reaches a genuine ancestry-bearing floor whose active singleton set is exactly E.

At this returned floor,

  M_ret=2,
  delta_E,ret=0,
  A_E,ret=A_E^+.

Therefore

  Psi_E,ret=(2-|A_E^+|,0,0).                         (ER.1)

Compare with the old checkpoint

  Psi_E,old=(2-|A_E^-|, M_old-2, delta_E,old).        (ER.2)

Lexicographically, (ER.1) never exceeds (ER.2). More precisely it is STRICTLY smaller if at least one of the following holds:

1. A_E grew during the exit/return macro;
2. M_old>2;
3. M_old=2 but the old floor was not E-aligned, equivalently delta_E,old>0.

Equality can occur only when

  A_E^+=A_E^-,  M_old=2,  S_old=E.                    (ER.3)

Thus payment and steering themselves already give the desired endpoint-clock descent everywhere except the old aligned-floor stratum.

### 4. The R1022 entrance construction supplies a new middle without changing the clock
Now start from the returned ancestry-bearing floor on E. Use the entrance construction in accepted R1022 with its freely chosen physical target pair set equal to the OLD E. Accepted R429 supplies an exact two-cover

  H-E=U_0|V_0

with both rails nontrivial. The order bound used inside R1022 guarantees an internal rail vertex b'. Boundary antisymmetry orients the three physical vertices E union {b'} into a proper tight turn whose outer pair is exactly E. Denote it locally by

  J'=(a,b',c),

allowing the displayed names a,c to be interchanged if the tight outer orientation is reversed. The physical set E and the endpoint ledger are unchanged.

Stop at this R1022 entrance checkpoint before its later R445 forest-currentization compiler. We have recovered exactly the data needed for phase-0 continuation:

- the same physical endpoint pair E;
- the same historical A_E^+;
- an E-aligned ancestry-bearing floor;
- an exact H-E frame;
- a proper turn with an internal new middle b'.

No coordinate of Psi_E changes when b' is chosen. By SV56855 the middle switch does not reset the endpoint budget. Hence the paid exit has a finite SAME-E macro-return whose rank is (ER.1).

### 5. What happens in the equality stratum
Assume the only rank-flat possibility (ER.3). At the new middle b', run a selected-incidence channel when needed. SV56855 gives an exact dichotomy on its anchored endpoint e.

- If e is already in A_E, the old historical signed singleton at e and the genuinely later endpoint-anchored dimer trigger accepted R436, so the episode is immediately nonquiet.
- If e is fresh, the R434/R42 protected arm either exits explicitly, or completes an E-aligned return with e retained and adjoins e to A_E, strictly lowering the first coordinate 2-|A_E|.

Therefore a middle change can create a rank-flat checkpoint but cannot create a quiet rank-flat selected-incidence recurrence. The remaining equality-case obstruction is an EXPLICIT NONQUIET PORTAL, not loss of the endpoint ledger. In particular when A_E=E, every selected-incidence channel at every rebased middle is nonquiet.

### 6. Mandatory test I: SV50987 transverse-cap mass-four pair
SV50987 supplies a direct mass-four balanced pair from two transverse Arm-M cap walls. Accepted R514 gives exactly a certificate-retaining continuation to a spanning two-cover or an ancestry-bearing both-singleton floor. R514 also explicitly preserves every separately certified graph-intrinsic static configuration as historical data, so the old A_E certificates survive without qualification.

Hence the route

  old E-checkpoint -> SV50987 pair -> R514 floor -> R432(E) -> R1022 entrance at E

has endpoint-clock comparison (ER.1)-(ER.3). Wall dimers and other cap facts may remain historical side certificates, but no old cap representative is claimed current. The only possible failure of strict descent is the already-aligned rank-flat stratum, where SV56855 converts any endpoint reuse at the new middle into explicit nonquiet contact.

### 7. Mandatory test II: R920 all-internal component-drop pair
In the all-internal branch of accepted R920, deleting the middle x from an H-E return produces a literal three-cover of the proper residue H-J, while the source U|V is a two-cover. R159 supplies the balanced pair. For payment provenance, inspect the accepted proof of R159: it first finds a selected cross-state joining two components and then invokes accepted R176 on that exact state. R176 retains the selected cross-state witness, the crossed source component and its old neighbor when nontrivial, plus a chosen spare vertex; this is an explicit physical pair-birth certificate.

Accepted R415 states in its applicability that an R176 cross-state pair is a lawful ancestry-bearing input to certificate-retaining descent. Therefore the R920/R159 pair is NOT a bare anonymous pair for payment purposes. Apply R415 to reach a genuine floor unless H closes, then R432 to the OLD E and the R1022 entrance construction as above. The four R920 reverse shields remain graph-intrinsic historical side facts; they need not remain simultaneously current.

Thus the cross-pole R920 packet has exactly the same endpoint-clock return map as SV50987. No additional datum is lost at the payment entrance.

### 8. Parent theorem and remaining obstruction
The reusable parent statement is:

> Any explicit phase-0 exit carrying a certificate-bearing balanced pair with a lawful finite descent to an ancestry-bearing both-singleton floor admits a finite return to the OLD physical endpoint pair E with a new admissible internal middle and with Psi_E nonincreasing. The return is strict unless the source checkpoint was already an E-aligned mass-two floor and no new endpoint was completed. Middle rebasing never enlarges the clock and never resets A_E. At equality, the next selected-incidence event is either strict in epsilon_E or explicitly nonquiet.

This closes the precise G21 ancestry question for the two requested G20 test objects. It does NOT consume the explicit nonquiet growth/cycle/reversal/contact portal at the equality stratum. That is the surviving fully-anchored/nonquiet curvature problem, not a return-map or middle-rebasing failure.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R415"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    },
    {
        "relation": "dependency",
        "revision_id": "R920"
    },
    {
        "relation": "dependency",
        "revision_id": "R1022"
    }
]
```