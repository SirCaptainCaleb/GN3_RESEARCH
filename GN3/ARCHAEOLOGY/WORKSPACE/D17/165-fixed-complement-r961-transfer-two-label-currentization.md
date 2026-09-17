# Two anchored transfers currentize a same-residue endpoint discrepancy or a fixed-support reversal candidate

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r961-transfer-two-label-currentization`

**Summary:** If two anchor labels transfer through the same boundary vertex q0, their exact singleton covers share the shortened complement Q^- and differ only on the active supports. Deleting both anchor labels yields two literal covers of one common residue with Q^- unchanged. Depending on whether the exchanged q0 position is endpoint or internal, one gets an immediate R408 component drop or two Hamilton paths on one common active support selecting q0 against different triangle labels. A one-turn R3 test either produces a full-support selected reversal or a labelled reverse trimer. Thus two transfers do not remain independent support moves.

### Setup
Retain two distinct active transfer labels y_i,y_j in the HHH anchored packet through source vertex q_0 of Q. Let y_k be the third triangle label. The exact transferred covers have the form

  C_i = P_i^* | Q^-,
  C_j = P_j^* | Q^-,

where Q^-=(q_1,...,q_t) is the identical literal complement and the active Hamilton paths are

  P_i^*=(q_0, y_j, y_k, M),
  P_j^*=(q_0, y_k, y_i, M)

up to cyclic relabelling matching the anchored packet. Both are exact singleton-deletion covers of H-y_i and H-y_j respectively.

### Common pair-deletion residue
Delete y_j from C_i and y_i from C_j. The literal complement Q^- survives unchanged. On the active side:

- deleting y_j from P_i^* removes the vertex immediately after q_0 and leaves either q_0 isolated from the remaining active path or a two-piece split, depending on the local order;
- deleting y_i from P_j^* affects the later triangle position.

The two trimmed covers lie on the SAME residue

  W=H-{y_i,y_j}

and retain the same Q^- rail. If one trimmed active side is connected while the other splits, accepted R408/R159 applies as a same-residue endpoint/internal component drop with the physical q_0 and y_k positions retained.

### Equal component count: one-turn reversal test
In the branch where both trimmed active sides remain Hamiltonian on the same active support, write their literal orders schematically as

  A=(q_0,y_k,M),
  B=(y_k,q_0,M)

or the exact boundary-dual form supplied by the anchors. They select the physical dimer {q_0,y_k} in opposite directions. If these are full Hamilton paths on the same support, the fixed-complement selected-reversal normal form applies immediately with literal complement Q^-.

If one of the two orders differs by one local seam rather than direct adjacency, test that single seam. Tightness completes the full-support reversed representative; failure gives the exact R3 reverse trimer anchored on q_0,y_k and the neighboring M vertex. Thus the equal-component branch yields either a genuine same-support reversal or an explicit labelled local reversal packet.

### Scope
This section currentizes TWO transfers into one common pair-deletion frame. It does not claim that every pair of transfers lands in the direct reversed-dimer subcase, and it does not consume a local reverse trimer without a full-support realization. Its purpose is to prevent treating multiple transfers as unrelated singleton fibers: after deleting the two labels, the common complement and physical q_0 geometry are simultaneous.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    }
]
```
