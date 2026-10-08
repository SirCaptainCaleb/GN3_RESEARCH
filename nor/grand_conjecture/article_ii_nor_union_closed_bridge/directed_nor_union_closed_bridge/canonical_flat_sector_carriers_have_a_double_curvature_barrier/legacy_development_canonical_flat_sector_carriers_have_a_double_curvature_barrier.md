# Canonical flat sector carriers have a double curvature barrier — preserved pre-item development

## Development

## Canonical flat-sector carriers have a double curvature barrier

Work in the coboundary-flat pure-orientation sector. Let C be a four-change cyclic order maximizing
[
Phi=sum_{i=1}^4 r_i^2
]
among all four-change orders in a counterexample. Suppose its cyclic run profile is
[
1,p,q,2
]
and
[
p,qge2.
]

The established singleton-trap theorem already implies that the transition
[
qmid 2
]
entering the final length-two run is fully curved.

### Theorem

The preceding transition
[
pmid q
]
is also fully curved.

### Proof

Assume for contradiction that the transition between the p-run and q-run is flat. Then both endpoint repairs are available, and by minimum variation every repair must preserve q(C)=4 rather than lower it to 2.

We split according to p and q.

#### Case 1: p,q>=4

This is excluded by convex run extremality: a flat transition cannot separate two runs both of length at least 4.

#### Case 2: p=3

Use the leftward repair, which moves the transition into the p-run by distance d in {2,3}. If d=3, the target is exactly the preceding transition, so variation drops by two, impossible. Hence d=2.

Because the move stays inside the p-run, the two incident lengths change from
[
(3,q)mapsto(1,q+2).
]
Thus
[
DeltaPhi
=
1+(q+2)^2-9-q^2
=
4(q-1)>0
]
since q>=2, contradicting maximality.

The case q=3 is symmetric, using the rightward repair.

#### Case 3: p=2

Again use the leftward repair. Distance 2 lands exactly on the preceding transition. Distance 3 passes across the p-run of length 2 and then across the preceding singleton run of length 1, landing exactly on the next transition beyond it. Thus either possible transport distance targets an occupied switch, so the repair would lower variation to 2. Contradiction.

#### Case 4: q=2

Use the rightward repair. Distance 2 lands on the already-known transition q|2 and lowers variation, impossible. Therefore the only possible transport distance is 3. It crosses the q-run and lands one slot inside the following run of length 2.

For a right repair across a length-two run, the local run transformation is
[
(p,2,2)mapsto(p+2,1,1).
]
Hence
[
DeltaPhi
=
(p+2)^2+1+1-p^2-4-4
=
4p-2>0,
]
contradicting maximality.

These cases cover all p,q>=2. Therefore p|q is fully curved. QED.

### Corollary

In the perfect-blocker range p,q>=2, a Phi-maximal canonical carrier has two consecutive curvature barriers around the entire q-run:
[
p oxed{	ext{full}} q oxed{	ext{full}} 2.
]

Thus the flat-sector escape problem reduces further. The two remaining transitions lie on the complementary corridor with run lengths
[
2,1,p,
]
while the q-run is trapped between universal-switch barriers. Any closed repair component must explain how the mobile switches in the short corridor avoid either colliding, creating a singleton insertion escape, or changing one of the two barrier tetrahedra under the induced coordinate swaps.
