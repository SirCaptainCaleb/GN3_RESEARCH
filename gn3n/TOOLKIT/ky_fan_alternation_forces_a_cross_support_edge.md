# Ky Fan alternation forces a cross-support edge

**Summary:** For an equal-side one-hole deletion cover, an alternating-role Ky Fan output for the block order P then Q must contain a genuine cross-support path edge away from the old hole.

## Statement

Assume H-x=P|Q with |P|=|Q|=r>=3 and an alternating-role deletion-cover conclusion is available for every prescribed ordering. Prescribing all vertices of P before all vertices of Q forces both new supports to meet both P and Q; hence some new path edge joins P to Q away from x.

## Body

Let
[
H-x=Pmid Q,qquad |P|=|Q|=rge3,
]
and suppose an alternating-role deletion-cover conclusion is available for every prescribed ordering.

Prescribe all vertices of (P) first and all vertices of (Q) second. After removing the new hole label (y), the left/right support roles alternate along the induced order.

Among the (r) consecutive (P)-labels, at most one is removed, so at least (r-1ge2) remain consecutively. Hence both alternating roles occur on (P). The same argument applies to (Q). Therefore each of the two new supports contains vertices from both old supports.

If (y=x), neither new path contains (x), so each mixed path has an ordinary path edge crossing from (P) to (Q). If (y
e x), exactly one new path contains (x); the other still contains vertices from both (P) and (Q), so some consecutive pair on that path crosses between the two old supports and is not incident with (x).

Thus the abstract alternating-role conclusion forces a genuine cross-support path edge away from the old hole.

## Metadata

- ID: ky_fan_alternation_forces_a_cross_support_edge
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
