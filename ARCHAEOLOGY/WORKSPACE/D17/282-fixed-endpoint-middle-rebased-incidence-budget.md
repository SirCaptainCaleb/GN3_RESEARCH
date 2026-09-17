# Completed endpoint history survives middle rebasing at one fixed outer pair

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-middle-rebased-incidence-budget`

**Summary:** Fix one physical endpoint pair E={a,c}. Record A_E as the endpoints whose earlier quiet selected-incidence episodes, possibly at different middle vertices, completed a protected return to an E-aligned floor with that endpoint retained as a historically signed singleton. This ledger is genuinely middle-independent. At any later proper turn with the same outer pair E, the R434 selected-incidence mechanism produces a new nontrivial endpoint-anchored dimer unless H closes. If its anchor e already lies in A_E, the old historical signed singleton at e and the new dimer meet at the old signed anchor, so accepted R436 forces explicit growth/cycle/reversal/contact geometry; the episode cannot be quiet, regardless of the new middle. If e is fresh, the R434/R42 protected-return proof runs with the new middle and either exits explicitly or completes a new E-aligned floor with e retained, thereby adjoining e to A_E. Hence across all admissible middles for one fixed physical pair E there are at most two completed quiet endpoint episodes total, not two per middle. This is the local middle-quotient compiler needed by G21; it does not by itself consume the resulting nonquiet portals.

### 1. Fixed physical endpoint pair and a middle-free ledger
Let H be a hypothetical smallest Strong Level-(1) counterexample and fix two distinct physical vertices

  E={a,c}.

We define a historical endpoint ledger A_E subseteq E as follows. An endpoint e belongs to A_E when, at some earlier stage, there was a proper tight turn with outer pair E,

  J_i=(a,b_i,c)

(or the reversed displayed outer orientation), together with an E-aligned ancestry-bearing both-singleton floor and an exact H-E frame, such that one selected-incidence episode anchored at e completed its designated R42 protected continuation all the way back to an E-aligned floor with e retained as a historically signed singleton coordinate. Retain the complete physical certificate of that episode, in particular the historical signed singleton at the physical endpoint e.

This definition deliberately forgets the old middle b_i but not the physical endpoint or its sign/capture ancestry. The question is whether a later middle may quietly reuse e.

### 2. Rebase to an arbitrary later middle
Let b' be any vertex for which one outer orientation of E gives a proper tight turn J' with middle b'. Work at an E-aligned ancestry-bearing floor and an exact pair-deletion frame

  H-E=U|V

from which the selected-incidence mechanism at b' is available. The physical names a,c may be interchanged locally if R3 makes the reversed outer orientation tight; E itself and the ledger A_E are unchanged.

Reconstruct the R434 incidence calculation for J'. A selected predecessor of b' yields, unless H closes during actualization, a graph-intrinsic nontrivial signed dimer whose signed physical endpoint is one outer vertex of E; a selected successor gives the dual dimer anchored at the other endpoint. Write e for the resulting anchored endpoint and D_e for this genuinely later dimer. The construction of D_e uses J' and the current selected incidence, but the next step uses only the physical anchor e.

### 3. A spent endpoint cannot be quietly spent at a new middle
Assume e is already in A_E. By definition we retain an older graph-intrinsic signed singleton support P=(e), together with its completed protected-return certificate. The new D_e is a proper tight path of order two containing e. It is not the vacuous stationary replay of the old singleton certificate.

Apply accepted R436, General Tight-Path Contact and Historical Anchor Protection, to the old signed singleton P and the genuinely later proper path D_e. This is exactly the at-anchor case of R436. Therefore one obtains explicit strict path growth, strict growth of the later path, a vertex-simple tight cycle, or a reverse contact/reversal cell. In every case the new episode is nonquiet.

Crucially, R436 never refers to the middle vertex that created the old singleton certificate. The proof sees only the old graph-intrinsic signed anchor e and the later path containing e. Hence replacing b_i by b' does not reset the spent-endpoint status.

### 4. A fresh endpoint can be credited exactly once
Now assume e is not in A_E. Run the same protected-return arm used in accepted R434, but with the current turn J'. Immediately designate the descendant continuation protected by R42 toward singleton e. Along that continuation either H closes, or the first later event touching e is exposed and the episode is explicitly nonquiet, or certificate-retaining pair descent reaches a both-singleton floor with e itself retained. Accepted R433/R432 steering then restores the other outer endpoint while preserving e, producing a new E-aligned floor. In this quiet return branch append e to A_E and retain the new completed endpoint certificate.

Nothing in this completion argument needs the previous middle. The fixed data are the physical pair E, the fresh endpoint e, the current J' incidence certificate, and the designated protected continuation.

### 5. Middle-quotient endpoint budget
Therefore, for one fixed physical endpoint pair E, every selected-incidence episode at every admissible middle has the following common ledger behavior:

1. if its anchored endpoint e is already in A_E, the episode is immediately nonquiet by R436;
2. if e is fresh, then either the episode closes/exits explicitly or a completed quiet return enlarges A_E by e.

Consequently at most two completed quiet endpoint episodes can occur over the entire family of middle vertices sharing E. The budget is two per endpoint pair, not two per literal turn.

Equivalently, the first coordinate

  epsilon_E = 2-|A_E|

is well-defined on the middle-quotiented historical lineage. A middle switch does not increase epsilon_E. A completed quiet episode strictly lowers it; reuse of a spent endpoint is an explicit nonquiet portal.

### 6. Scope and fence
This section does not claim that every nonquiet growth/cycle/reversal/contact output is already consumed, nor that arbitrary current representatives coexist. It proves only the missing bookkeeping statement: completed endpoint history is a physical historical-anchor fact and lawfully survives b -> b' rebasing at fixed E. It uses the exact R434 selected-incidence mechanism for the new birth and the graph-intrinsic R436 contact theorem for cross-middle reuse. No frozen root is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R42"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    },
    {
        "relation": "dependency",
        "revision_id": "R433"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R436"
    }
]
```