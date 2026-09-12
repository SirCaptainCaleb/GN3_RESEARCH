# With one internal fixed-E frame, both trimer-return regimes produce a payable same-E exit

**Workspace:** D17
**State:** established
**Key:** `fixed-endpoint-trimer-return-always-payable`

**Summary:** Let an ancestry-bearing phase-0 floor be aligned to E={a,c}, retain a proper tight trimer J=(a,b,c), and retain one exact H-E cover C_int in which b is internal. Then the R920 endpoint/all-internal dichotomy has no independent mate-clause residue. If every exact H-E cover keeps b internal, R920 gives a component-drop R159 pair on H-J; accepted R159 is proved by an explicit R176 cross-state, so R415 lawfully pays it. If some exact H-E cover C_end exposes b at a rail endpoint, compare C_end with C_int: accepted R408 gives an endpoint/internal component-drop pair; its proof invokes R159, whose P555 route again retains an R176 cross-state certificate, so R415 lawfully pays this pair as well. In either regime the resulting certificate-bearing pair enters SV57138/SV57422: pay to a floor, steer back to the same old E, re-enter by R1022. Thus every such trimer has a finite same-E continuation to TWO-COVER, strict Psi_E decrease, or an explicit nonquiet portal. Endpoint mate clauses are not a new terminal species once an internal base frame is already present. This does not consume the final explicit nonquiet portal in the fully anchored equality stratum.


### 1. Aligned phase-zero input with one internal base frame
Let H be a hypothetical smallest Strong Level-(1) counterexample. Fix a physical endpoint pair

  E={a,c}                                                   (TP.1)

and retain an ancestry-bearing both-singleton floor aligned to E. Let

  J=(a,b,c)                                                 (TP.2)

be a proper tight trimer whose outer pair is E. Retain one literal exact two-cover

  C_int=U|V   of H-E                                       (TP.3)

in which the middle b is INTERNAL on its displayed rail.

This is exactly the entrance geometry supplied by R1022 and the bilateral common-center frame used in SV70372. The point is that one internal exact H-E representative is retained before the trimer-return analysis begins.

### 2. If every return keeps b internal, R920 gives a certificate-bearing pair
Apply accepted R920 to J. Suppose first that every exact two-cover of H-E places b internally. This is R920 regime (II).

Choose any exact return P|Q of H-E, with

  P=(...,ell,b,r,...).                                     (TP.4)

Deleting b produces the literal three-cover

  P_L | P_R | Q                                            (TP.5)

of H-J. R920 compares this with an exact two-cover of H-J and invokes accepted R159.

The accepted proof P555 of R159 is explicit: the smaller cover selects a physical cross-state joining two components of the larger cover, and fully reconstructible R176 is then applied to that retained state. Hence the resulting balanced pair is equipped with the exact R176 cross-state birth certificate required by the certificate-retaining payment theorem R415.

Therefore the all-INTERNAL R920 pair has a lawful finite continuation to

  TWO-COVER,
  or an ancestry-bearing both-singleton floor.             (TP.6)

### 3. If some return exposes b, the retained internal frame turns it into R408 component drop
Suppose instead that R920 is in regime (I): some exact two-cover

  C_end=P'|Q'  of H-E                                     (TP.7)

places b at a physical rail endpoint.

Now use the already-retained internal cover C_int from (TP.3). The two covers C_end and C_int are exact covers of the SAME proper residue H-E, and the same physical vertex b is an endpoint in C_end but internal in C_int. Accepted R408 therefore applies.

Its proof deletes b. Trimming b from C_end leaves an at-most-two-cover of H-J, whereas deleting internal b from C_int gives a literal three-cover of H-J. R408 invokes R159 on this component drop.

Again inspect accepted R159/P555: the proof chooses a selected state of the smaller cover crossing two components of the three-cover and invokes R176 on that exact state. Retain this cross-state and its source-component ancestry rather than only the anonymous balanced-pair conclusion.

Thus the R408 pair is also a certificate-bearing R176 pair and accepted R415 applies. Hence the endpoint-return regime likewise gives (TP.6).

In particular, the R919/R173 mate certificate that R920 also supplies in regime (I) is auxiliary geometry here. It is not the only usable output and need not be treated as an independent terminal phase-zero species.

### 4. Return every such paid exit to the same old endpoint pair
In either Section 2 or Section 3, take the certificate-bearing balanced pair and run R415 to a genuine ancestry-bearing floor unless H closes. Apply R432 with prescribed target pair equal to the OLD E. Then use the R1022 entrance construction at E.

This is precisely the paid-exit return map of SV57138 and the completed fixed-E macro of SV57422. Therefore the entire trimer-return macro has one of only three outcomes:

  TWO-COVER;
  strict decrease of the fixed-E clock Psi_E;
  explicit nonquiet growth/cycle/reversal/contact geometry. (TP.8)

At a rank-flat returned E-aligned floor, SV57422 appends the first incidence episode rather than ending the macro. A fresh endpoint completion decreases epsilon_E; a spent endpoint gives the explicit nonquiet alternative in (TP.8).

### 5. Phase-zero trimer-return compression
> At an aligned phase-zero floor on E, once one exact H-E frame with the trimer middle internal is retained, every proper outer-pair trimer J=(a,b,c) has a lawful certificate-bearing paid-pair exit. R920's endpoint-return and all-internal regimes both enter the same SV57422 fixed-E macro. Endpoint mate clauses are therefore not a separate irreducible phase-zero obstruction in this setting.

This applies directly to the internal-middle entrance frames of SV70372. It also applies after any later explicit R445 output supplies a proper trimer whose outer pair is the retained E and whose middle is internal in the fixed frame.

### 6. Scope fence
The theorem does not claim strict Psi_E descent in the fully anchored equality stratum. There the completed paid macro may return rank-flat and terminate only by exposing another explicit nonquiet portal. Consuming that portal remains the hard phase-zero problem.

Nor does the theorem apply to an arbitrary trimer whose outer pair differs from E unless an internal exact frame for that new outer pair is separately retained. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R415"
    },
    {
        "relation": "dependency",
        "revision_id": "R920"
    }
]
```