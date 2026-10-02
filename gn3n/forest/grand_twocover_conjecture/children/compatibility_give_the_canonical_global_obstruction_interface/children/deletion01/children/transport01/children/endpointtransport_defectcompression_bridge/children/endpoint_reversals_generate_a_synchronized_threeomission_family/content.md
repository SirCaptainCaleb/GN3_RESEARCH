# Two neutral endpoint reversals generate a synchronized three-omission family

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, where P=(p_0,...,p_m). Suppose H[P] has a Hamilton order R_L containing the reversed initial edge (p_1,p_0) and a Hamilton order R_R containing the reversed terminal edge (p_m,p_{m-1}). Then at least one of the following holds.

(1) H has a spanning two-cover.

(2) The singleton lift P|Q|{x} admits a legal pairwise repartition with strictly smaller quadratic potential.

(3) Two Hamilton paths on one common support have order disagreement.

(4) There are two distinct vertices a,b in V(P) such that, with X=V(P) union {x}, the three deletion covers F_x=P|Q, F_a=(X-{a})|Q, F_b=(X-{b})|Q form a pairwise support-compatible localized family with fixed complement Q. Consequently the synchronized endpoint-family theorem applies: after choosing deletion covers at the two endpoints of a Hamilton order of Q, some family member is support-incompatible with both endpoint covers, each endpoint cover has at least two crossings of the associated three-part partition, and either one has at least three crossings, one has a direct mixed-support crossing, or the endpoint probes force order disagreement.

Thus simultaneous reversed displayed end-edges cannot remain merely local: unless they already give a two-cover, descent, or order disagreement, they amplify to a synchronized three-omission disturbance family.

## Body

Apply ac7bd525291b separately to R_R and R_L.

For the reversed terminal edge, ac7bd525291b gives a spanning two-cover, a strict quadratic-potential decrease, or the neutral boundary case. In that neutral case the prefix before the reversed edge has one vertex, so for some a in V(P),
R_R=(a,p_m,p_{m-1},B),
and
F_a=(x,p_m,p_{m-1},B)|Q
is a deletion two-cover of H-a.

For the reversed initial edge, the symmetric part of ac7bd525291b gives the same first two outcomes, or its neutral boundary case. In the neutral case the suffix after the reversed edge has one vertex, so for some b in V(P),
R_L=(A,p_1,p_0,b),
and
F_b=(A,p_1,p_0,x)|Q
is a deletion two-cover of H-b.

Assume neither a spanning two-cover nor a strict potential decrease occurred, so both neutral descriptions hold.

If a=b=z, then F_a and F_b have the same variable support X-{z}, where X=V(P) union {x}. Their displayed Hamilton paths put x first in F_a and last in F_b. The neutral case requires |P|>=3, so X-{z} contains a vertex other than x. Hence these two Hamilton paths order x and such a common vertex differently, giving order disagreement. This is outcome (3).

Now assume a!=b. Put D={x,a,b}. The original deletion cover is
F_x=(X-{x})|Q.
Together with F_a and F_b, this gives
F_t=(X-{t})|Q
for every t in D.
All three support partitions are pairwise support-compatible on common two-deletion domains because the Q-side is fixed and every remaining X-vertex lies on the other side.

Moreover H[X] is non-Hamiltonian: if X were Hamiltonian, a Hamilton path on X together with Q would be a spanning two-cover of H. Thus the hypotheses of e92b0f47c1a6 hold for the three-label family D. Its synchronized endpoint conclusion is exactly outcome (4).