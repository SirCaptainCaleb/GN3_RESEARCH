# A fixed-witness defect fan contains an unavoidable odd crossing segment

**Workspace:** D17
**State:** established
**Key:** `singleton-disagreement-fan-parity`

**Summary:** If a fixed witness pair {u,v} lies on one rail of C_a, then for every opposite-status deletion label b, the literal u-to-v rail segment crosses tau_{a<-b} an odd number of times. Thus the complete defect fan concentrates a parity-bearing row segment, though total-K descent remains open.

Retain the complete fixed-witness fan and the row weights. Choose a deletion label a for which u and v lie on the same actual C_a rail, and let R_uv be the literal contiguous u-to-v subpath. Define O_a to be the set of deletion labels b in the opposite witness-status class. For every b in O_a, u and v lie in different blocks of tau_{a<-b}, because they survive both deletions and tau preserves their sigma_b same-block status. Along R_uv, every selected edge crossing tau_{a<-b} toggles target block and every noncrossing edge preserves it. Since the endpoints are in opposite target blocks, the number of crossing selected edges is odd. Hence sum_{e in E(R_uv)} chi_b(e)=1 mod 2 for every b in O_a. Equivalently, the XOR of the target-cut incidence vectors of the selected edges on this one physical segment is the all-ones vector over O_a. Summing integrally gives sum_{e in E(R_uv)} w_a(e) >= |O_a|. This is a concentration/parity lemma, not a K-descent theorem: different b may be witnessed by different edges, and support-changing replacements still alter incoming targets. The next parent is a coordinated two-row or whole-class deleted-label exchange with exact collateral accounting.
