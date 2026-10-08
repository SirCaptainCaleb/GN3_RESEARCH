# Alternating feasible-support peeling and uniform future polarization — preserved pre-item development

## Development

## Alternating feasible-support peeling and uniform future polarization

Work in arbitrary coordinate arity (rge2). Let (P) be an inclusion-maximal (sigma)-tight path in a directed NOR counterexample, let (F_0) be its exposed first ordered ((r-1))-state, and let
[
Y_0=Vsetminus V(P).
]
Put
[
c_1=1-sigma.
]

By maximality of (P),
[
h(y,F_0)=c_1qquad(yin Y_0),
]
so every singleton of (Y_0) is feasible in (mathcal F_{c_1,F_0}).

We now define an alternating peeling recursively.

At stage (j), assume:
- (Y_{j-1}
earnothing);
- every singleton ({y}), (yin Y_{j-1}), is feasible in (mathcal F_{c_j,F_{j-1}}).

Choose an inclusion-maximal feasible support
[
M_jsubseteq Y_{j-1},
qquad
M_jinmathcal F_{c_j,F_{j-1}}.
]
Since all singletons are feasible, (M_j
earnothing). Choose a (c_j)-tight witness
[
Q_j=(	ext{an ordering of }M_j,F_{j-1}),
]
and let (F_j) be its exposed first ordered ((r-1))-state.

Set
[
Y_j=Y_{j-1}setminus M_j.
]

If (Y_j=arnothing), stop. Otherwise set
[
c_{j+1}=1-c_j.
]

### Theorem 1: every future vertex is uniformly polarized at the new front

For every (yin Y_j),
[
h(y,F_j)=c_{j+1}.
]

#### Proof
If instead (h(y,F_j)=c_j), then prepending (y) to the chosen (c_j)-tight witness (Q_j) would give a (c_j)-tight witness for
[
M_jcup{y}
]
ending at (F_{j-1}), contradicting inclusion-maximality of (M_j). Since the label is binary,
[
h(y,F_j)=1-c_j=c_{j+1}.
]
(square)

Thus every singleton of the remaining set (Y_j) is feasible in the opposite-color family
[
mathcal F_{c_{j+1},F_j},
]
so the construction continues.

Because each (M_j) is nonempty, the process terminates after finitely many stages, say (k), with a partition
[
Y_0=M_1dotcup M_2dotcupcdotsdotcup M_k.
]

### Theorem 2: the peeling produces a spanning (k)-change order

The witnesses splice in reverse stage order:
[
Q_k,Q_{k-1},ldots,Q_1,P.
]
Their successive colors are
[
c_k,c_{k-1},ldots,c_1,sigma,
]
and adjacent colors are opposite. Each block contributes at least one status window because (M_j
earnothing).

Hence the resulting spanning coordinate order has exactly (k) color changes.

In particular:
- (k=0) means (P) was already spanning monochromatic;
- (k=1) gives the directed NOR conclusion;
- a counterexample forces (kge2) for every such maximal-support peeling.

### Corollary 3: triangular future polarization

For every stage (j<k) and every later-layer vertex
[
yin M_{j+1}cupcdotscup M_k,
]
one has the uniform identity
[
h(y,F_j)=c_{j+1}.
]

Thus the exposed states
[
F_0,F_1,ldots,F_{k-1}
]
see all future layers with a deterministic alternating polarity. The obstruction is therefore layered, not arbitrary.

### Corollary 4: every nonfinal layer witnesses failure of union closure

At stage (j<k), all singletons of (Y_{j-1}) are (c_j)-feasible at (F_{j-1}), but the maximal feasible support (M_j) does not contain all of (Y_{j-1}). If the restricted family on (Y_{j-1}) were union-closed, the union of its feasible singleton supports would be all of (Y_{j-1}), contradicting maximality.

Hence every nonfinal layer carries a union-closure defect. Choosing a minimal infeasible support inside the current remainder recovers a punctured-Boolean circuit.

### Significance

This gives a finite depth parameter for Article II: the **alternating peeling depth** of a maximal monochromatic path. It measures how many successive witness-synchronization failures are required before all omitted coordinates can be absorbed.

Unlike a single front circuit, the peeling records global compatibility data:
- each layer is maximal feasible at its terminal state;
- every later vertex is uniformly blocked in the current color;
- that same blocking automatically makes every later singleton feasible in the next color;
- the layers concatenate to an actual spanning order.

The closure problem can now be attacked by minimizing peeling depth and showing that depth at least two is unstable under reversal, interval reversal, or recentering. Depth two already gives a spanning two-change order and therefore lands on the minimum four-change cyclic frontier in ternary arity.
