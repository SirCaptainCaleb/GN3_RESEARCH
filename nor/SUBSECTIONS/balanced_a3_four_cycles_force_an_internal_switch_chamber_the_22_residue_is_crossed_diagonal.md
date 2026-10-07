# Balanced A3 four-cycles force an internal switch chamber; the 2+2 residue is crossed-diagonal

## Metadata

- ID: balanced_a3_four_cycles_force_an_internal_switch_chamber_the_22_residue_is_crossed_diagonal
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 101
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A3 terminalization: balanced four-cycles force an internal switch chamber

Normalize the switch target to 0 on the pre-switch side and 1 on the post-switch side. Thus a pre-switch violation has actual ternary color 1, while a post-switch violation has actual color 0.

Work in one exact A3 Coxeter block on four coordinates.

### Lemma 1: absence of an internal switch chamber forces a transitive tetrahedral face pattern

Assume there is no ordering (x1,x2,x3,x4) whose two consecutive internal ternary windows have colors 0,1.

Fix any ordering (x1,x2,x3,x4). Consider the cyclic four-word
alpha(x1,x2,x3), alpha(x2,x3,x4), alpha(x3,x4,x1), alpha(x4,x1,x2).
If this cyclic word contained a transition 0->1, the corresponding cyclic rotation of the coordinate order would be an internal switch chamber. Hence it has no 0->1. A cyclic binary word with no 0->1 is constant.

Therefore for every coordinate order the four cyclic facet values are equal. In particular, relative to any chosen total order v1<v2<v3<v4, there is a bit t such that
alpha(v1,v2,v3)=alpha(v1,v2,v4)=alpha(v1,v3,v4)=alpha(v2,v3,v4)=t.
So the only A3 face pattern with no internal switch chamber is the transitive tetrahedral orientation induced by a total order, up to global color complementation.

### Lemma 2: every directed Hamilton four-cycle is monochromatic under the transitive pattern

Let x1->x2->x3->x4->x1 be any directed Hamilton cycle in the physical root graph. By Lemma 1, for this cyclic order the four cyclic windows
(x1,x2,x3), (x2,x3,x4), (x3,x4,x1), (x4,x1,x2)
all have one color t_C.

For the root e_xi-e_x(i+1), the middle coordinate of a ternary window can be either of the two remaining block coordinates. In either choice the ordered triple is obtained from one of the above cyclic triples by one transposition. Hence every window in the block having that physical root has color 1-t_C.

Thus all four roots of the directed Hamilton cycle, regardless of their chosen middle coordinates, lie on the same violation side.

### Theorem: a side-balanced A3 four-cycle forces a controlled internal repair

Suppose an honest lifted zero contains one simple directed physical four-cycle and that cycle itself is side-balanced. Then two cycle roots are pre-switch violations and two are post-switch violations.

If no internal switch chamber existed, Lemma 2 would put all four roots on the same violation side, contradiction. Therefore some order of the four block coordinates has internal color word 0,1.

Equivalently, every side-balanced simple A3 four-cycle determines a switch-compatible internal chamber. It is therefore nonterminal for the local extraction problem: the remaining verification is only the already-isolated boundary-pair/full-window splice compatibility.

This removes the balanced-four-cycle branch from the genuinely new A3 lifted-zero frontier.

### Residual two-cycle geometry under no internal chamber

Still assume the transitive pattern and fix v1<v2<v3<v4.

A same-side physical reversal pair e_u-e_v, e_v-e_u cannot use the same middle coordinate, since reversal complements the ternary color. Using the two different possible middles gives the same color exactly when one middle lies strictly between u,v in the total order and the other lies outside that interval.

On four coordinates this happens exactly for the two crossing rank-two diagonals {v1,v3} and {v2,v4}. Adjacent endpoint pairs and the extreme pair {v1,v4} cannot support a same-side reversal two-cycle.

Consequently, if a support-minimal lifted zero is the union of two oppositely side-imbalanced two-cycles and no internal switch chamber exists, the two physical two-cycles must lie on the two distinct crossing diagonals. They cannot lie on the same diagonal: choosing one root from each opposite-side pair would already give a two-term lifted zero, contradicting support minimality.

So the terminal 2+2 residue has one canonical form: two same-side reversal pairs on the crossing diagonals of the transitive A3 order, with opposite sides.

### Frontier consequence

After the already-proved two-term extraction and the theorem above, a support-minimal honest lifted A3 zero can fail immediate internal extraction only through:
1. the canonical crossed-diagonal 2+2 packet just described; or
2. a pair of oppositely imbalanced simple cycles in which at least one constituent is a triangle.

This is a strict reduction of the A3 extraction frontier and identifies the crossed-diagonal packet as the first genuinely terminal local configuration to test against boundary provenance or the cellular Tucker event.

## Frontier

- Development version when composed: None
- Development version now: 1
