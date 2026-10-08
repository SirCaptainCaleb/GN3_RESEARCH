# Full deletion connector orders glue from four coherent witnesses or two nonadjacent-gap witnesses — preserved pre-item development

## Composition

(none yet)

## Development

## Coherence of full deletion connectors gives spanning closure directly

Work in the flat split B→z→A→x, with z→x and the fixed tournament t. Set U=A∪{x,z}. A compatible connector is a linear order of its coordinates with α=0 on all consecutive triples and forward first and last ordered pairs. Each deletion connector below contains BOTH special coordinates x,z. Order agreement means agreement of every relative comparison on the full common coordinate domain, including x,z.

THEOREM 1 (four coherent full deletion connectors). Let D⊆A have at least four labels. For every d∈D choose a compatible connector C_d on U\{d}. If the C_d agree pairwise on the relative order of every common coordinate pair, then U has a spanning compatible connector, and any NOR-good order on B gives full NOR closure.

PROOF. For each pair u,v choose a d∈D outside {u,v} and take its comparison in C_d. Agreement makes this independent of the chosen d. For each triple u,v,w choose a d outside it; C_d establishes transitivity of its three comparisons. Thus they define one total order C on U, restricting to C_d on U\{d}. Every consecutive triple of C survives one deletion avoiding it, remains consecutive there, and has color zero. Its first and last pairs similarly survive a deletion avoiding each pair, remain endpoint pairs, and are forward. Apply the homogeneous-cut connector theorem. QED.

This argument uses tuple locality and endpoint-pair conditions, so it includes deletion connectors with three shore blocks and independently placed special coordinates. For r-ary constant-window orders with the same binary endpoint-port property, max(4,r+1) coherent deletions suffice by the same proof. In the ternary case the witnesses are supplied individually by minimal connector obstructionhood; coherence is the additional obligation. There is no need to first select two-path shore covers to apply Theorem 1.

THEOREM 2 (two-order gluing and its single-triple obstruction). Let d,e∈A be distinct, and let C_d on U\{d} and C_e on U\{e} be compatible connectors agreeing on the order of W=U\{d,e}. Write that common order as O. The order C_e inserts d in one gap of O, and C_d inserts e in another; end gaps are included. Number a gap by the number of common coordinates preceding it, and let the two indices be i,j.

(a) If |i−j|≥2, inserting both labels in their inherited gaps gives a spanning compatible connector.

(b) If i=j, one of the two orders of d,e in that gap gives a spanning compatible connector.

(c) If |i−j|=1, simultaneous insertion has just one possibly nonzero triple, consisting of d, the intervening common coordinate w, and e, in their inherited order. All other triples are zero, and both endpoint pairs are forward. Thus color zero on this triple closes. Color one leaves a precisely witnessed spanning order with one 1-colored triple and all other triples zero.

PROOF OF (a) AND (c). For distinct gaps, preserve their inherited order in O. Every consecutive triple containing at most one restored label survives deleting the other restored label, remains consecutive, and appears in its compatible deletion connector. If at least two common coordinates separate d,e, every triple is of this type. If just w separates them, the only exception is (d,w,e), up to interchanging d,e. Every endpoint pair contains at most one restored label and is an inherited endpoint pair of the other deletion connector, hence is forward.

PROOF OF (b), INTERNAL GAP. Let L,R be the common coordinates bracketing the gap. The two deletion connectors give α(L,d,R)=α(L,e,R)=0. The alternating tournament cocycle identity gives
α(L,d,e)+α(d,e,R)=α(L,d,R)+α(L,e,R)=0 (mod 2).
The two new internal statuses are therefore equal. Interchanging d,e complements both statuses, since α is alternating in a tournament representative. Choose their order making both zero. Every other triple, including the left exterior collar with the first restored label and the right exterior collar with the last, is inherited from an appropriate deletion connector. The full endpoint pairs are inherited unless this is an end gap.

PROOF OF (b), END GAPS. At the initial gap, both d→R and e→R are forward initial pairs of their deletion connectors. Orient the pair {d,e} forward. Their order then forms a forward transitive triple with R, so its color is zero and the new first port is forward; later windows and the last port are inherited. At the terminal gap, the last common coordinate L dominates both restored labels by the deletion ports. Orient {d,e} forward and use the same transitive-triple argument. The common order contains x,z and has size at least two, so the two end-gap conventions cover all boundary cases. QED.

COROLLARY (necessary obstruction pattern). In a minimal shore obstruction, EVERY pair of order-compatible deletion connectors has distinct adjacent insertion gaps and its sole newly exposed triple has color one. Four pairwise order-compatible deletion connectors cannot exist. This conclusion quantifies over actual full deletion connectors, including their special-coordinate positions and endpoint ports.

The same-gap argument specifically uses the tournament-derived alternating cocycle. The four-witness theorem and separated-gap argument require only locality. The adjacent-gap color-one state is a certificate of failure of the simultaneous insertion move; its conversion to a compatible zero connector or a full one-change NOR order remains an augmentation obligation. A finite graph or complex of actual deletion connector orders may use pairwise common-order agreement as compatibility. A simplex carrying four distinct omitted labels would have a complete closure extraction by Theorem 1. Any topological use still needs its domain, boundary realization, and proof that the required simplex is forced.
