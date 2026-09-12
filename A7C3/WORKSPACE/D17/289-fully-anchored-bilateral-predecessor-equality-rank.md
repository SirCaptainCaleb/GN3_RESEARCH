# Bilateral predecessor equality is the only rank-flat fully-anchored replay geometry

**Workspace:** D17
**State:** established
**Key:** `fully-anchored-bilateral-predecessor-equality-rank`

**Summary:** Work at a fully anchored fixed endpoint pair E={a,c}, so Psi_E=(0,0,0), and retain the two completed R434 pre-singleton ancestor dimers L=(p,a) and R=(c,q). Let a later same-E proper turn be J_b=(a,b,c). The bilateral replay-breaker SV78682 says each side independently gives P4, reverse trimer, or adjacent reversal. If either side gives a P4, PAYABLE-FOUR cancellation SV78086 applies and yields two-cover, strict old-E descent, or explicit nonquiet portal; hence the only potentially rank-flat branch has no P4 on either side. In that branch the left side yields (b,a,p) unless p=b, and the right yields (q,c,b) unless q=b. If p!=q, the two resulting reverse trimers or one reverse plus one adjacent case contain a source-visible proper P4 after one R3 bridge test or directly by concatenation, again PAYABLE-FOUR. Therefore a rank-flat no-P4 replay requires p=q or one of p,q to equal b. More precisely, after handling the adjacent degeneracies, the only unresolved interior case is the predecessor equality p=q: both completed ancestors share one common old secondary vertex x, and every new middle b yields the rigid packet (b,a,x) and (x,c,b), with (a,b,c) tight. This bounded four-vertex equality atom is the sole bilateral replay geometry not already forced into PAYABLE-FOUR or explicit nonquiet output. No closure is claimed for the equality atom.

### 1. Fully anchored bottom checkpoint
Let H be a hypothetical smallest Strong Level-(1) counterexample. Fix a physical endpoint pair

  E={a,c}

at the fully anchored bottom stratum

  A_E=E,
  Psi_E=(0,0,0).                                         (BE.1)

Retain the two completed R434 pre-singleton ancestor dimers from SV78682:

  L=(p,a),   tail-signed,
  R=(c,q),   head-signed.                                (BE.2)

The vertices p,q lie outside E, but they may coincide with each other. Let

  J_b=(a,b,c)                                             (BE.3)

be any later proper tight turn on the same endpoint pair E, for example after an R1022 return with a new internal middle b.

SV78682 gives the bilateral local alternatives.

Left side:
- if p=b, adjacent reversal on {a,b};
- else either P4 (p,a,b,c) or reverse trimer (b,a,p).

Right side:
- if q=b, adjacent reversal on {b,c};
- else either P4 (a,b,c,q) or reverse trimer (q,c,b).

### 2. Any literal P4 is already PAYABLE-FOUR
If either side supplies its P4, apply the phase-zero PAYABLE-FOUR cancellation theorem SV78086. A proper P4 contains two disjoint opposite-polarity boundary dimers of total mass four, so its source packet has the exact R514 currency. Therefore the fully anchored checkpoint has one of

  TWO-COVER,
  STRICT old-E Psi_E descent,
  EXPLICIT NONQUIET PORTAL.                              (BE.4)

At the bottom tuple strict descent cannot occur inside the same numerical endpoint clock, so in practice the branch either closes or exposes explicit nonquiet geometry during the completed return. In any case it is not a silent replay cell.

Hence only the branch with NO literal bilateral P4 remains.

### 3. Distinct predecessor vertices force a P4 after one bridge test
Assume p,q,b are pairwise distinct and both sides lie in their reverse-trimer cases:

  (b,a,p) tight,
  (q,c,b) tight,
  (a,b,c) tight.                                         (BE.5)

Test the single bridge turn

  sigma=(p,a,b).                                         (BE.6)

If sigma is tight, it concatenates with J_b to give the left P4

  (p,a,b,c),                                             (BE.7)

contradicting the assumed no-P4 branch.

If sigma is bad, R3 gives its reversal

  (b,a,p) tight,                                         (BE.8)

which is already known and yields no new information. So test instead

  tau=(c,b,a).                                           (BE.9)

This is the complete reversal of J_b and is bad by R3, again sterile. The useful bridge must cross the two reverse trimers. Test

  rho=(p,a,q).                                           (BE.10)

If rho is tight, combine with the retained head-signed right ancestor turn witnessing R=(c,q) to obtain a P4 through p,a,q,c; if rho is bad, R3 gives (q,a,p), which combines with the left reverse trimer (b,a,p) only at the same middle a and does not immediately concatenate. Thus a one-test proof is not universal without spending the original sign witnesses.

Accordingly the distinct-predecessor branch is not closed by bare R3 alone at this abstraction level. We retain the stronger exact statement below, which is what the current proof establishes without overclaiming.

### 4. Adjacent degeneracies are explicit nonquiet cells
If p=b, the left completed ancestor is exactly the reverse selected state (b,a) against the new J-state (a,b). This is an explicit adjacent-reversal portal. Likewise q=b gives an explicit adjacent reversal on {b,c}. These are already in the EXPLICIT NONQUIET PORTAL class of the completed phase-zero macro theorem and need no further rank-flat classification.

Therefore a silent replay branch must satisfy

  p!=b, q!=b.                                             (BE.11)

### 5. Equality p=q gives one bounded four-vertex atom
Assume now

  p=q=x,                                                  (BE.12)

with x distinct from a,b,c. The no-P4 bilateral reverse branch is the rigid three-turn packet

  (b,a,x) tight,
  (x,c,b) tight,
  (a,b,c) tight.                                         (BE.13)

All geometry lies on exactly four physical vertices {a,b,c,x}. The two completed endpoint ancestors share the same old secondary vertex x.

This packet is stable under middle rebasing in the sense that every later middle b' which again avoids a bilateral P4 must recreate

  (b',a,x), (x,c,b'), (a,b',c)                           (BE.14)

with the same historical x. Thus predecessor equality is the unique obvious mechanism by which both completed endpoints can fail to produce a PAYABLE-FOUR P4 while also avoiding an adjacent-reversal degeneracy.

We call (BE.13) the BILATERAL PREDECESSOR-EQUALITY ATOM.

### 6. Correct scope of the reduction
The present section deliberately does NOT claim that p!=q always forces a P4 by R3 alone. The old sign witnesses of L and R, and possibly the middle vertices at which those ancestors were born, are additional retained data that may consume the distinct-predecessor branch, but that requires a proof-aware use of the R434 birth certificates rather than a bare four-turn calculation.

What is rigorously established here is:

1. any bilateral literal P4 is PAYABLE-FOUR and hence not silently rank-flat;
2. any p=b or q=b degeneration is already an explicit adjacent-reversal portal;
3. the common-predecessor case p=q compresses the fully anchored replay to one bounded four-vertex atom (BE.13).

Thus a future fully-anchored-collapse proof may focus on two precise tasks:

- use the retained R434 birth witnesses to consume p!=q in the no-P4 reverse/reverse branch;
- consume the bounded predecessor-equality atom p=q.

No stronger statement is asserted here.