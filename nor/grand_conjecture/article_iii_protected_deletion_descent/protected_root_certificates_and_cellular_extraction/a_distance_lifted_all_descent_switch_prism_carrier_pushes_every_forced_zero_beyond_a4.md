# A distance-lifted all-descent switch-prism carrier pushes every forced zero beyond A4

## Composition

(none yet)

## Development

## A distance-lifted all-descent switch-prism carrier pushes every forced zero beyond A4

Work in ternary arity under counterexamplehood, so every full coordinate order has at least two color changes. Hence every binary status word has at least one 10 transition.

Let the ternary windows of an order pi be indexed 1,...,m, where m=n-2. For every 10 transition between window i and i+1 attach its physical slide root

rho_i=e_{v_i}-e_{v_{i+3}} in W.

For a switch-prism state (pi,k), where k is the proposed cut between window k and k+1, lift this occurrence by the SIGNED TRANSITION DISTANCE

d_i=i-k.

Thus the occurrence label is

Lambda_i(pi,k)=(rho_i,d_i) in W direct-sum R.

Average uniformly over all 10 occurrences of the state:

A(pi,k)=average_{i:10 at i} (rho_i,i-k).

This is defined at every state because counterexamplehood guarantees at least one 10.

### Exact reversal oddness

Under coordinate reversal,

pi -> pi^rev,
k -> m-k,
i -> m-i.

A 10 transition remains a 10 transition, its slide root reverses,

rho_i -> -rho_i,

and its signed distance satisfies

(m-i)-(m-k)=-(i-k).

Therefore

A(pi^rev,m-k)=-A(pi,k).

So A is an honest odd W direct-sum R label on switch-prism state vertices.

### Degree zero

Let X=P_V x I be the switch prism. It is an n-ball and dim(W direct-sum R)=n. On a centrally symmetric refinement, extend the state labels equivariantly over the boundary and affinely over cells/simplices, using the same all-refinements averaging convention as the actual-root face carrier.

If the resulting map F:X->W direct-sum R were zero-free, normalization would extend an antipodal map S^{n-1}->S^{n-1} across the n-ball, impossible because the boundary map has odd degree.

Hence F has a zero.

At a zero one obtains simultaneously a positive physical dependence among actual 10 slide roots and vanishing weighted signed transition distance from the proposed switch.

### Small-block exclusion

The physical W-component of A(pi,k) is independent of k: it is exactly the average of all actual 10 slide roots of pi.

Consequently, after averaging over refinements of a permutahedron face, the physical component is the all-refinements actual-root carrier from the local rotation theorem. For ternary arity, on every proper face whose Coxeter blocks all have size at most five, that carrier has strictly positive pairing with the inward normal of the largest face.

The extra scalar coordinate cannot cancel a nonzero physical component. Therefore F has no zero over the subcomplex of switch-prism states whose permutahedron face has every block of size at most five.

### Theorem

Every forced zero of the distance-lifted all-descent switch-prism carrier in ternary arity projects to a Coxeter face containing a block of at least SIX physical coordinates.

Thus this fixed-point carrier bypasses A2, A3, and A4 zero analysis entirely. The previously established A2/A3 extraction results remain useful for selected-violation/Tucker carriers, but they are not needed to localize zeros of this averaged all-descent carrier.

### Interpretation of the scalar equation

The last coordinate is not an arbitrary provenance tag. It is the signed displacement of each actual 10 transition from the proposed threshold cut. A zero satisfies

sum lambda_j (i_j-k_j)=0.

Thus the physical root circulation has zero first moment in the switch direction: its 10 descents balance on the two sides of the proposed switch, with a transition sitting exactly at the cut contributing zero.

This is a genuine transverse condition unavailable to any perturbation confined to W.

### Remaining gap

Localization to a block of size at least six is not closure. The next problem is to extract a witness improvement from a support-minimal large-block zero with balanced transition distance. In particular one should seek either:
- an actual 10 transition at distance zero, giving a switch-crossing obstruction directly at the proposed cut;
- two opposite-side descents that can be joined by the Tucker/repair dynamics;
- or a face reduction contradicting support-minimality.

No claim is made here that the large-block zero already preserves deletion-witness provenance.
