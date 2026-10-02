# Higher-terminal certificate anchors reintersect the lower-terminal maximum path

## Statement

Let e={x,v,u} be an ascending nonspecial edge with unique entrance x and terminals v,u. Suppose a selected common-anchor certificate at u supplies a distinct ascending nonspecial anchor h={y,u,w} and a canonical maximum source precursor A ending at y such that A,h is a longest h-path ending at u, A avoids u, and x,v belong to V(A).

Let P_v be any maximum endpoint path ending at v, and let g be its last edge. Then
  |V(A) intersect V(P_v)| >= 2,
and at least one of the following holds:
(C) A union P_v contains a linear cycle;
(E) g belongs to E(A).

If moreover phi(e)<phi(v) and e is terminal-single on P_v, then exactly one of x,u occurs on the precursor of P_v. In the X-type case x lies on P_v, so A and P_v have the explicit two common vertices v,x. In the U-type case u lies on P_v and x does not; since A avoids u, every common vertex of A and P_v besides v is outside V(e).

In particular, every uphill-certified edge assigned to its lower-rank terminal carries a repeated-intersection certificate between the fixed lower-terminal maximum path and the higher-terminal certificate-anchor precursor, sharpened to a linear cycle or containment of the fixed lower-terminal last edge.

## Body

The precursor A is a maximum endpoint path ending at y. Since v belongs to A, first note that v is not the last vertex y of A. Indeed h is distinct from e in the common-anchor switching construction; if y=v, then h and e would both contain u and v, contradicting linearity.

Let P_v be any maximum endpoint path ending at v. If A and P_v had v as their unique common vertex, the unique-intersection theorem 5854d853a44b for maximum endpoint paths would force v to be an internal joint of both paths. This is impossible because v is the last vertex of P_v. Hence A and P_v have at least two common vertices.

Now apply 41100a9882dd with P=P_v and comparison path A. Its hypotheses hold because the last vertex v of P_v lies on A and there is a second common vertex. Therefore either A union P_v contains a linear cycle, or the last edge g of P_v is also an edge of A. This proves the cycle-or-common-edge dichotomy.

Finally assume phi(e)<phi(v) and e is terminal-single on P_v. Since e cannot be the last edge of P_v, terminal-singleness and linearity imply that exactly one of x,u occurs on the precursor of P_v. If x occurs, then v and x are two explicit common vertices of A and P_v. If u occurs, then x is absent from P_v; on the other hand u is absent from A by the common-anchor precursor geometry. Thus every common vertex of A and P_v besides v lies outside {x,u,v}=V(e).

Strengthening pass: the strict uphill inequality phi(v)<phi(u), source-cleanliness, fundamental-cycle data, and near-extremal hypotheses are not used. Only the common-anchor precursor geometry is needed for the repeated-intersection and cycle-or-common-edge conclusions, while phi(e)<phi(v) plus terminal-singleness is needed for the X/U refinement.