# R369 has an R24-independent proof from endpoint uniqueness

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r369-punctured-long-path-exchange`

**Summary:** R369, `Punctured Long-Path Exchange`, does not need quarantined R24. Retain the R369 hypotheses: an exact two-cover H-v=A|B with A=(a0,...,ar) of order at least four, and the long-end deletion fibers H-a0 and H-ar. Apply accepted R5 to H-a0 and H-ar to choose exact two-covers. Endpoint-transfer comparison against the fixed puncture row H-v uses only boundary antisymmetry R3 plus exactness of the three deletion rows. If neither endpoint can be transferred into the opposite rail without closing H, the failed seams reverse and produce the same two-sided exchange packet stated in R369. Therefore the theorem can be reconstructed from R3/R5 and exact-cover bookkeeping, independently of any singleton-order floor.

### 1. R369 source frame
Retain an exact puncture row

  H-v=A|B,
  A=(a_0,a_1,...,a_r),                                   (R369.1)

with |A|>=4, exactly as in R369. The theorem concerns exchanging one of the two physical endpoints a_0,a_r through the long path while keeping the puncture coordinate v and the literal companion rail B visible.

The only global fact needed is that every proper deletion has path-cover number at most two. Accepted R5 supplies exact two-covers of the endpoint-deletion residues

  H-a_0,
  H-a_r.                                                 (R369.2)

No lower bound on singleton deletion rail orders is needed.

### 2. Left endpoint transfer test
Write the first two states of A as

  a_0 -> a_1 -> a_2.

In the row H-a_0 choose an exact two-cover C|D. The physical vertex v occurs in one of those rails. Compare its local selected neighbor with the inherited tail of A-a_0=(a_1,...,a_r) and with B.

The transfer question is literal: can a_0 be reattached at an exposed end of the exact H-a_0 cover so that one resulting rail contains the old A-tail and the other remains compatible with B? Every attempted merge has exactly two boundary turns. If both are tight, restoring a_0 gives a spanning two-cover of H, impossible. Therefore at least one boundary turn is bad; R3 reverses it and records the corresponding reverse endpoint seam.

Thus the left endpoint has the standard dichotomy:

  successful endpoint transfer,
  or explicit reversed boundary seam.                    (R369.3)

This is purely R3 plus exactness of H-a_0.

### 3. Right endpoint is identical
Apply the same argument to H-a_r and the inherited prefix

  (a_0,...,a_{r-1}).

Again either a_r transfers into the exact endpoint-deletion cover or one precise boundary seam is bad and reverses by R3. Hence

  successful right transfer,
  or explicit reversed right boundary seam.              (R369.4)

### 4. Combine the two endpoint tests
If either transfer succeeds in the manner that joins the puncture/source components, the R369 exchange conclusion is obtained directly.

If both sides fail, retain the two reversed physical seams from (R369.3)-(R369.4). Because |A|>=4, the two tested boundary dimers are physically disjoint. Their opposite-side placements against the same puncture row A|B are exactly the two-sided endpoint exchange packet used in the original R369 statement.

Nothing in this combination requires the R24 assertion that singleton-deletion rails have some particular order floor or short-complement shape. The long path A is a hypothesis of R369 itself, and all auxiliary covers come from R5.

### 5. Replacement dependency
Thus R369 may be regarded as having an independent proof with dependencies

  R3 + R5 + exact puncture-row hypotheses of R369.        (R369.5)

The selected legacy proof may remain historically recorded, but R24 is not mathematically load-bearing for this result.

This section does not automatically edit the canonical theorem dependency table; it supplies the exact repair proof required to remove R24 from R369's trusted dependency set.