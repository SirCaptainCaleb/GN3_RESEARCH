# Genuine deletion distance two forces a fully protected four-label middle face

## Metadata

- ID: genuine_deletion_distance_two_forces_a_fully_protected_four_label_middle_face
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 39
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Genuine deletion distance two forces a fully protected four-label middle face

Let H satisfy kappa_2(H)=2. Let X={x,y} be a minimum deletion pair and fix a displayed two-cover
H-X=P|Q,
with
P=(p_1,...,p_r), Q=(q_1,...,q_s),
where r,s>=3.

Consider the minimum-hole order
pi=(P,x,y,Q^rev).
By minimum-hole exactness its deficiency is two. Write
u=p_{r-2}, a=p_{r-1}, b=p_r,
c=q_s, d=q_{s-1}, v=q_{s-2}.
Thus the relevant eight-position band is
(u,a,b,x,y,c,d,v).

Freeze u,a in the first two positions of this band and d,v in the last two positions, and allow the four middle labels
M={b,x,y,c}
to occur in an arbitrary order sigma. Let pi_sigma be the resulting global spanning order, with all vertices outside the band left in their inherited positions.

Every status strictly to the left of the band is 1 and every status strictly to the right is 0. Because the first two and last two band positions are fixed, the two statuses crossing the exterior boundaries are also the inherited monotone statuses. Hence every status that can differ among the 24 orders pi_sigma is supported entirely in the eight-position band.

Since kappa_2(H)=2, every spanning order has exact deficiency at least two. Therefore no pi_sigma can satisfy the two-cover threshold q<=p+1, nor can it have deficiency one. By the positive local-witness criterion, every one of the 24 middle permutations contains a witness from
W_+={001,011,0101}
whose determining interval is contained in the eight-position band.

Consequently a genuine minimum two-hole state determines a four-label permutahedral face with the following properties:

1. all 24 chambers are positively obstructed;
2. every obstruction is supported inside one fixed eight-vertex band;
3. the two hole labels x,y satisfy the minimum-hole four-end reversal relations against the inherited path edges;
4. the original two hole orders (b,x,y,c) and (b,y,x,c) are minimum-deficiency chambers with the central form 0ab1.

Thus, after kappa_2=2 has been reached, the combinatorial frontier is equivalent to excluding a fully protected anchored S_4 middle face subject to the minimum-hole reversal constraints. No unbounded corridor remains.

This formulation also identifies the overlap with the carrier-localization route: protected commuting-square and minimal commuting-cube failures are already known to be eight-position local. The combinatorial endpoint obstruction and the topological protection obstruction therefore live on the same bounded positional scale. The missing theorem can be sought as a structural impossibility theorem for this anchored four-label face rather than as a global corridor-surgery theorem.
