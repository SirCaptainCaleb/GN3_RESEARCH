# Near-saturated gap-one states have linear symmetric difference and a dense switching matching

## Statement

In a near-saturated gap-one state p=q+1, the anchor-to-maximum switching matching has size s=(5/8)q-O(1)-delta and forces linear two-sided symmetric difference between the q-edge anchor Q and the maximum (q+1)-edge path P: each has at least s-O(1) vertices absent from the other. The s switching hyperedges form a matching through v pairing retained and omitted anchor vertices. Thus the hard shell is an ordered two-rail matching problem of density asymptotically 5/16 on the anchor precursor.

## Body


Let v be in the gap-one shell:
  p=phi(v)=q+1,
and suppose q(v)=q. Choose:
- a q-edge anchor path Q ending physically at v in a rank-q ascending terminal edge;
- a maximum p-edge path P ending physically at v.

Use the switching matching of fecba48a3ffd. Let s be its size:
  s >= gamma(q)-ceil((3q-4)/4)-delta
    = (5/8)q-O(1)-delta.

Each switching edge f={v,a,b} has both a,b in the anchor precursor
  R=V(Q)\h,
and exactly one of {a,b} lies in V(P)\last(P), while the other lies outside V(P).

Let
  I=R intersect V(P),
  O=R minus V(P).
Since switching pairs are disjoint,
  |I|>=s and |O|>=s.                                (1)

Because |R|=2q-2,
  |R intersect V(P)|<=2q-2-s.                       (2)

Now P has 2(q+1)+1=2q+3 vertices, while the last edge of P contributes at most three vertices not counted in its precursor. More directly its precursor vertex set has size 2q. Hence
  |(V(P)\last(P)) minus R|
   >=2q-|I|
   >=2q-(2q-2-s)
   =s+2.                                            (3)

Thus both directions of the symmetric difference are linear:
  |V(Q) minus V(P)|>=s-O(1),
  |V(P) minus V(Q)|>=s+O(1).                        (4)

Moreover the switching hyperedges themselves pair s distinct O-vertices to s distinct I-vertices, all through the common terminal v. Thus near saturation produces not just large symmetric difference but a concrete matching of hyperedges crossing the membership cut R∩V(P) versus R\V(P).

Order the 2q-2 vertices of R by their first occurrence along Q. Every switching edge determines an ordered pair
  (i_f,o_f)
of Q-positions, one retained and one omitted.
The residual gap-one problem is therefore a two-rail ordered matching problem: show that a matching of density 5/16 on the Q-vertex sequence, together with P being only one edge longer than Q, forces an alternating splice/cycle that either:
- creates a path longer than P,
- turns a switching edge double on P,
- or produces a second maximum endpoint state with strictly more anchor-double transfer.

Any linear loss in the possible switching density improves the 43/48 global coefficient.
