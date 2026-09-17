# Every phase-zero P4 pays to its middle-pair floor carrying its boundary dimers as bilateral ancestors

**Workspace:** D17
**State:** established
**Key:** `phasezero-p4-middle-pair-bilateral-return`

**Summary:** Let K=(x,p,q,y) be any proper tight P4 in a hypothetical smallest counterexample. Its first turn makes the boundary dimer L=(x,p) tail-signed by q; its second makes R=(q,y) head-signed by p. L and R are physically disjoint opposite-polarity dimers of total mass four. R514 therefore gives TWO-COVER or an ancestry-bearing both-singleton floor, and R432 can steer the nonclosing floor to the prescribed middle pair E_K={p,q}. At that returned E_K-floor, the graph-intrinsic P4 boundary dimers persist exactly as a bilateral ancestor packet L=(x,p) tail and R=(q,y) head. Hence the local SV57993 replay-breaker calculation applies to every later proper turn on E_K, without any quiet-completion assumption. Thus every phase-zero P4 has a canonical family-level destination: closure or a middle-pair floor carrying typed nontrivial endpoint ancestors. This turns the R542→P4 output into pair-to-pair ancestor transport rather than anonymous payment.

### 1. A P4 contains a direct mass-four pair
Let H be a hypothetical smallest Strong Level-(1) counterexample and let

  K=(x,p,q,y)                                           (PM.1)

be any proper vertex-simple tight P4. Its two defining turns are

  (x,p,q),   (p,q,y) tight.                             (PM.2)

Read the first turn as a tail sign on the initial boundary dimer

  L=(x,p):   (x,p,q) tight,

so L is tail-signed by witness q with signed endpoint p. Read the second as a head sign on the terminal boundary dimer

  R=(q,y):   (p,q,y) tight,

so R is head-signed by witness p with signed endpoint q. Since K is vertex-simple, V(L) and V(R) are disjoint. Therefore L,R are physically disjoint opposite-polarity signed dimers of total support mass four.

Accepted R514 applies directly. It gives a finite chosen certificate-retaining continuation to

  TWO-COVER,
  or an ancestry-bearing both-singleton floor.            (PM.3)

The P4 K, both boundary dimers, their tested orientations, and witnesses p,q remain graph-intrinsic historical data.

### 2. Steer to the physical middle pair
In the nonclosing branch of (PM.3), prescribe

  E_K={p,q}.                                              (PM.4)

Apply accepted R432. We obtain TWO-COVER or an ancestry-bearing floor aligned exactly to E_K. R432 changes active singleton coordinates but does not invalidate the separately retained graph-intrinsic turns (PM.2).

Thus at the returned E_K-floor we possess the typed bilateral historical packet

  L=(x,p) tail-signed by q,
  R=(q,y) head-signed by p.                              (PM.5)

The two signed anchors are precisely the two coordinates of the returned pair E_K.

### 3. Immediate replay-breaker interface
Let

  J'=(p,b,q)                                             (PM.6)

be any later proper tight turn on the same physical pair E_K. The local seam calculation in `fully-anchored-pre-singleton-replay-breaker` SV57993 requires only a tail-signed historical dimer ending at the first endpoint and a head-signed historical dimer beginning at the second endpoint. It does not use the old quiet-completion middles. Therefore (PM.5) satisfies its exact local hypotheses.

Consequently every later same-E_K turn carries, independently at p and q, a literal P4, labelled reverse trimer, or adjacent reversal against the retained P4 boundary ancestors. If x,y,b are pairwise distinct and both extension seams pass, the turns concatenate to the P5

  (x,p,b,q,y).                                           (PM.7)

If a vertex coincidence prevents that P5, retain the exact two local outputs and make no unlicensed cycle claim.

### 4. Pair-to-pair transport interpretation
A phase-zero P4 is therefore not merely a proper path that can be currentized into phase one. It has a completely phase-zero family-level normalization:

  P4 K=(x,p,q,y)
    -> direct R514 mass-four pair on its boundary dimers
    -> R432 return to the middle pair {p,q}
    -> same-pair bilateral ancestor packet (x,p),(q,y).  (PM.8)

Combining with `r542-two-witness-packet-already-p4`, every R542-ready packet likewise has such a canonical middle-pair return after choosing the source-visible P4 supplied there. This converts the former R542 recycling gap from anonymous payment into typed pair-to-pair ancestor transport.

### 5. Scope fence
This section does not prove that the middle pair differs from a previous floor pair, that the resulting family transport is acyclic, or that the returned floor has lower numerical rank. It does not assert paid descendants of different P4s coexist as current states. The durable simultaneous data are the graph-intrinsic P4 and its two boundary signed dimers. The remaining G26 problem is to show that a finite reconstruction-closed orbit of such typed pair returns cannot absorb all accumulated ancestor packets.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R514"
    },
    {
        "relation": "dependency",
        "revision_id": "R432"
    }
]
```