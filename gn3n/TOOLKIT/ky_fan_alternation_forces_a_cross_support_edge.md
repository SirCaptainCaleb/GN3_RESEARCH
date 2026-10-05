# Ky Fan alternation forces a cross-support edge

**Summary:** For an equal-side one-hole deletion cover with side orders at least three, the Ky Fan alternating-role cover for the order P followed by Q contains a path edge joining the old supports away from the old hole.

## Statement

Assume H-x=P|Q with |P|=|Q|=r>=3 and assume the Ky Fan alternating-role alternative holds for every prescribed ordering. Prescribe all vertices of P first and all vertices of Q second. In the resulting one-hole deletion cover G_y, both new path supports meet both P and Q. Consequently at least one path edge of G_y joins P to Q and is not incident with x.

## Body

After removing the new hole label y from the prescribed order, the left/right support roles alternate. Among the r consecutive P-labels, at most one is removed, so at least r-1>=2 remain consecutively in the induced ordering; therefore both role signs occur on P. The same holds on Q. Hence each of the two supports of G_y contains at least one old-P vertex and at least one old-Q vertex. If y=x, neither new path contains x, so each mixed path has a direct ordinary path edge between P and Q. If y is not x, exactly one new path contains x. The other path still contains vertices from both P and Q, and along its path order some consecutive pair crosses from one old support to the other; that edge is not incident with x. Thus a genuine P-Q path edge away from x is forced.

## Metadata

- ID: ky_fan_alternation_forces_a_cross_support_edge
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
