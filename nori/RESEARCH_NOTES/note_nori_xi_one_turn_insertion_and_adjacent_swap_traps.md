# One-turn paths need not admit monotone insertion or adjacent-swap rerouting

- Stable ID: note_nori_xi_one_turn_insertion_and_adjacent_swap_traps
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: boundary-tournaments, obstruction, one-turn, insertion, phase-rigidity, block-reversal, induction
- Lifecycle: active
- Epistemic status: proved
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_2
- Updated session: session_nori_r6430_2
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Research obstruction to monotone Hamilton one-turn insertion and adjacent-swap induction.

Let V={0,1,2,3,4,5,6}; represent the 105 reversal-orbits of ordered triples (a,b,c) by increasing middle entry b and increasing outer pair a<c, both different from b. Color each representative by the corresponding bit of M=0x1ac7021fa38c061f59fbd55e375, and color (c,b,a) by the complementary bit. This is a legal ordinary reversal-odd boundary 3-tournament.

The six-vertex word W=(0,6,4,2,5,1), omitting vertex z=3, has one color change among its four triple colors. Nevertheless, inserting z at any of the seven positions produces color-change counts [2,2,3,3,2,2,2], and swapping any of the five adjacent positions of W produces counts [2,2,3,2,2]. Thus W is an isolated vertex of the adjacent-swap graph of one-turn orders on its six-vertex resource set, and none of its seven direct z-insertions is a one-turn order.

This does not refute the spanning one-turn conjecture: other six-vertex one-turn orders and full seven-vertex one-turn orders exist for this b. It refutes the auxiliary inductive lemma that EVERY one-turn (n−1)-path can be made spanning by insertion, and the variant allowing a sequence of adjacent swaps remaining in the one-turn class before insertion.

Reproducibility: for each ordered triple (a,b,c), compute representative (min(a,c),b,max(a,c)), read the bit at its index, xor 1 if a>c. For W and its seven insertions and five swaps, count consecutive inequalities among the triple colors; the arrays above are the output of local enumeration.

A weaker obstruction: for V={0,1,2,3,4}, mask 0x2542ad73, the one-turn word (0,2,4,3) omitting vertex 1 has every insertion yielding two color changes. Thus plain monotone insertion fails already in order five.

Research implication: try two-arm endpoint packing with rerouting via multi-vertex exchanges that temporarily permit two turns or change the terminal pair; do not assume the one-turn permutation flip graph is connected or that local optimality implies global one-turn extendability.

A broader local-search obstruction holds even when full interval reversals are allowed: on seven vertices use mask M=0x18d19f9846ecc3863983eb2c2d7 (same indexing), and W=(5,3,0,2,4,1,6). Its three-letter color word has two changes. For all 21 nontrivial interval reversals W[i:j+1] (0≤i<j≤6), the switch histogram is 14 reversals of cost 2 and seven of cost 3; none reduces the cost to one. This was computed by enumerating the 21 reversed permutations with the bit-mask coloring rule. Therefore descent using arbitrary consecutive-block reversals, even though these operations preserve resources and complement/reverse all fully internal triple colors, also has a nonoptimal local minimum in order seven.

A positive endpoint constraint: if a vertex-simple monochromatic tight path uses n−1 of n vertices, appending the last vertex adds only one triple color, so the result is necessarily a spanning path with at most one turn. Every counterexample to the spanning one-turn conjecture must therefore lack any monochromatic path of order n−1. For a one-turn path on n−1 vertices with first and last triple colors epsilon and 1−epsilon, nonextendability by prepending or appending the missing vertex z forces boundary colors b(z,w1,w2)=1−epsilon and b(w_(n−2),w_(n−1),z)=epsilon. Such endpoint locks are possible for individual words, as the insertion trap demonstrates; any use in a proof must compare a family of paths.

All-dimensional terminal-phase rigidity in a hypothetical counterexample. Let b on n≥5 vertices have NO spanning path with at most one color change. Fix omitted vertex z and any spanning one-turn word W=(w1,...,w_(n−1)) on V\{z}. Because a monochromatic (n−1)-word can always be extended by appending the missing vertex with at most one change, W must have one change, not zero. Let epsilon denote its initial triple color, and 1−epsilon its last triple color. Prepending z would preserve at most one change if b(z,w1,w2)=epsilon; appending z would preserve at most one if b(w_(n−2),w_(n−1),z)=1−epsilon. Therefore a counterexample forces
  b(z,w1,w2)=1−epsilon,
  b(w_(n−2),w_(n−1),z)=epsilon
for EVERY such W.

In particular, if two spanning one-turn words of the (n−1)-vertex induced tournament have the SAME ordered first pair (u,v) but opposite initial colors, then, for any missing z, one can prepend z to the word whose first color equals b(z,u,v), giving a spanning one-turn word on all n vertices. Thus a counterexample would require a phase-rigid near-spanning family at every deletion: for fixed omitted z and ordered first pair (u,v), all good (n−1)-vertex words beginning (u,v) must start in the same color, prescribed by the external triple b(z,u,v). This is a stringent all-dimensional necessary condition and a possible strengthened induction invariant.

CORRECTION (refuted): Universal terminal-phase flexibility is false already on six vertices. The mask 0x7f9ed7b30020000 has 84 spanning one-turn words, but no ordered starting pair supports both initial phases. A seven-vertex extension with mask 0x3ff0ecd1d98f0021004000 blocks BOTH endpoint insertions for all 84 six-vertex one-turn words while allowing internal insertions; see the separate verified obstruction note. The extension lemma remains true but terminal-phase flexibility cannot serve as a universal induction hypothesis.
