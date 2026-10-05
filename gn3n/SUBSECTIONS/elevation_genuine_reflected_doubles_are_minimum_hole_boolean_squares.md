# Elevation: genuine reflected doubles are minimum-hole Boolean squares

## Metadata

- ID: elevation_genuine_reflected_doubles_are_minimum_hole_boolean_squares
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 14
- Row version: 2
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

### Genuine doubles are two-element minimum holes

Let \(J=C\sqcup\{x,y\}\) be a reflected double span with corridor cover \(C=P\mid Q\) and
\[
\kappa_2(H[J])=2.
\]
Then \(\{x,y\}\) is a minimum deletion set. Minimum-hole heredity gives the Boolean square
\[
\kappa_2(H[J])=2,\quad
\kappa_2(H[J]-x)=\kappa_2(H[J]-y)=1,\quad
\kappa_2(H[C])=0.
\]
Absolute nonaugmentability implies that each of \(x,y\) reverses all four exposed end edges of \(P\mid Q\), and no assignment of either nonempty subset of \(\{x,y\}\) to the two corridor paths can make both enlarged sides Hamiltonian. Thus the four-end reversal and internal nonabsorbability of a genuine reflected double are consequences of the general minimum-hole theorem, not separate terminal phenomena.

## Development

## A genuine reflected double is a minimum-hole Boolean square

Let
[
J=Csqcup{x,y},qquad C=Pmid Q,
]
be the determining span of a positive reflected double, where (P,Q) are the corridor two-cover. Assume
[
kappa_2(H[J])=2.
]
Then (X={x,y}) is a minimum two-cover deletion set of (H[J]).

Apply the hereditary exactness theorem for minimum holes from [[spanning_orders_and_defect_helly]]. For every (Ysubseteq X),
[
kappa_2!left(H[J]-(Xsetminus Y)ight)=|Y|.
]
Hence the four induced states form the exact Boolean square
[
egin{array}{c|c}
	ext{induced span} & kappa_2\ hline
H[J] & 2\
H[J-x] & 1\
H[J-y] & 1\
H[C] & 0.
end{array}
]

This recovers, from the first exact-deletion section alone, the later fact that each one-endpoint deletion is a genuine distance-one instance.

There is more. Write
[
P=(p_1,ldots,p_s),qquad Q=(q_1,ldots,q_t)
]
in their tight orientations. Absolute nonaugmentability of a minimum hole says that for every nonempty (Ysubseteq{x,y}),

- (Pcup Y) is non-Hamiltonian;
- (Qcup Y) is non-Hamiltonian;
- no partition (Y=Y_Psqcup Y_Q) makes both (Pcup Y_P) and (Qcup Y_Q) Hamiltonian.

For each (ein{x,y}), if
[
h(e,p_1,p_2)=1,
]
then ((e,P)) would be a Hamilton path on (Pcup{e}), contradicting the singleton case of absolute nonaugmentability. Therefore
[
h(p_2,p_1,e)=1.
]
The same argument at the other end of (P) gives
[
h(e,p_s,p_{s-1})=1.
]
Applying the identical argument to (Q) yields
[
h(q_2,q_1,e)=1,qquad h(e,q_t,q_{t-1})=1.
]

Thus both deleted vertices reverse all four exposed corridor end-edges:
[
oxed{
egin{aligned}
h(p_2,p_1,x)&=h(p_2,p_1,y)=1,\
h(q_2,q_1,x)&=h(q_2,q_1,y)=1,\
h(x,p_s,p_{s-1})&=h(y,p_s,p_{s-1})=1,\
h(x,q_t,q_{t-1})&=h(y,q_t,q_{t-1})=1.
end{aligned}}
]

So [[genuine_two_deletion_doubles_reverse_all_four_corridor_ends]] is not an isolated endpoint calculation: it is a direct manifestation of the minimum-hole Boolean-cube theorem.

Likewise every attempted internal assignment of (x,y) to the two corridor sides is already covered by absolute nonaugmentability. In particular, any surgery supported entirely on (J) that would turn the corridor plus (x,y) into two Hamilton paths contradicts the minimum-hole property. Combined with [[outward_repair_inside_a_double_span_is_equivalent_to_a_two_cover]], this recovers the no-internal-outward-repair theorem.

### Elevation consequence

The genuine reflected-double residue should be introduced as soon as the exact deletion-distance theory is available:

[
oxed{
	ext{positive reflected double with }kappa_2=2
=
	ext{a two-element minimum exact hole with a fixed corridor cover}.
}
]

The later corridor classification remains necessary to identify when the local-witness route reaches this state, but once it does, the distance-one deletions, four-end reversals, and internal nonabsorbability are inherited from the general minimum-hole theory and need not be reproved as separate structural facts.
