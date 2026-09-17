# Every fixed singleton hub side has a direct endpoint crossing or a common-complement R966 packet

**Workspace:** D17
**State:** established
**Key:** `singleton-fixed-hub-endpoint-r966`

**Summary:** Every rail in every exact singleton-deletion two-cover of a smallest boundary-tournament counterexample has order at least three. For a fixed hub row H-b=P|Q, if neither endpoint deletion fiber of P has a direct selected P|Q crossing, the fixed-hub support-copy theorem supplies both endpoint replacements by b and R966 forces explicit R435 geometry among the source path and the two replacements. All three compared paths occur in singleton fibers with the same literal complement Q. Thus each hub side is END-DIRECT or a cover-current fixed-complement R966 packet.

### Elementary singleton-deletion rail floor three
Let H be a hypothetical smallest boundary-tournament counterexample and let

  H-b=P|Q

be any exact two-nonempty-path cover. Neither rail can have order one by `codimension-one-coherence`. In fact neither can have order two. If P=(u,v) is a dimer, then on the three-set {b,u,v} at least one of the complete-reversal pair (b,u,v),(v,u,b) is tight by boundary antisymmetry. Hence {b,u,v} has a tight Hamilton trimer. Together with the disjoint Hamilton rail Q this gives a spanning two-cover of H, contradiction. Therefore every rail in every exact singleton-deletion two-cover of a smallest counterexample has order at least three. This is the general boundary-tournament analogue of the edge-ordered rail-floor-three fact, proved here directly.

### Endpoint-currentization on one hub side
Fix one actual singleton source row

  C_b=P|Q,
  P=(p_0,p_1,...,p_r),

so r>=2 by the preceding floor. Test only the two endpoint deletion fibers p_0 and p_r against source row b.

If C_{p_0} contains a selected adjacency directly crossing (P-p_0)|Q, retain that literal current defect. The same applies at p_r. Suppose instead that neither endpoint fiber contains such a direct source-rail crossing. Then `singleton-fixed-hub-critical-dichotomy` supplies actual Hamilton replacement paths

  L on (P-p_0)+b,
  R on (P-p_r)+b.

The full support P+b is non-Hamiltonian, because any Hamilton path on P+b together with the disjoint literal Q rail would two-cover H. Thus accepted R966 applies to the literal Hamilton path P, exterior vertex b, and the two actual endpoint-replacement paths L,R. It yields explicit R435 Reverse-Ear geometry in at least one of the three comparisons

  (P,L), (P,R), (L,R).

Crucially this R435 output is cover-current across one fixed complement. The three paths occur in the literal singleton fibers

  H-b     = P | Q,
  H-p_0   = L | Q,
  H-p_r   = R | Q,

where the same literal oriented path Q may be retained in all three covers. No selected state is transported between unrelated fibers and no path is reversed.

Hence every source side P of every singleton row has the exact alternative:

(END-DIRECT) at least one endpoint deletion fiber has a selected source-rail crossing between P-endpoint and Q sides; or

(END-R966) the two endpoint replacement fibers and the source fiber form a three-row, fixed-complement R966 packet with an explicit source-relative R435 reversal, reverse trimer/contact, or vertex-simple tight cycle.

The exact dual holds with P,Q exchanged.

### Relation to the full fixed-hub critical dichotomy
If an entire P-side has no direct defects, the earlier fixed-hub theorem gives the full deletion-Hamiltonian block Omega_P=P+b with Q as a fixed complement for every puncture. The present theorem is a strict compression of what is needed to force explicit order geometry: only the two endpoint punctures of the retained P order are needed. Thus the no-direct branch can never remain a featureless support-level critical block; already at the source endpoints it emits cover-current one-hole R435 geometry.

If both source sides P and Q have no endpoint-direct defect, one obtains two simultaneous fixed-complement R966 packets sharing the same physical hub b: the P-side packet has literal complement Q, while the Q-side packet has literal complement P. This paired packet is the next consumer target.

### Scope
This theorem does not consume the R435 output. Bare Reverse-Ear existence remains cheap. Its value is exact currentization: the R435 event is attached to three named singleton fibers and one unchanged complementary Hamilton rail. The next theorem must either use both hub-side packets jointly, convert one localized endpoint event into a strict K/support repair, or derive a spanning two-cover. Generic R435/P4 production alone is not closure.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```
