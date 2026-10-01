# Reduce the cocycle route to omitted-label gap transport

## Statement

Proposal: use the common-core branch of compattripletransport13 as the first genuinely nontrivial deletion-cover transport datum. For a pairwise support-compatible, pairwise order-incompatible triple F_a,F_b,F_c whose restrictions to R=X-{a,b,c} have one common order, record for each x in {a,b,c} the two insertion gaps occupied by x in the two paths that contain it. The immediate proof target is a boundary-tournament constraint on these three two-gap transports strong enough to force either common-core order disagreement, full compatibility of a pair, or a spanning two-cover.

## Body

Established input: support-only transport has trivial monodromy, and fixed surviving-pair order parity telescopes. The certified theorem compattripletransport13 shows what survives those fences: after deleting a,b,c, either order disagreement remains on the common core R, or every one of a,b,c moves between two distinct gaps of one fixed R-order across the two paths containing it. Thus the cocycle route no longer needs an abstract intermediate datum; it can study the six concrete gap positions. Proposed next step: encode each label by the interval between its two gaps and derive a three-label compatibility law from tightness at the two insertion neighborhoods. A useful theorem would show that a configuration of three such transports cannot persist without producing a pair of compatible deletion covers or a checked splice. No claim about that final law is asserted here.