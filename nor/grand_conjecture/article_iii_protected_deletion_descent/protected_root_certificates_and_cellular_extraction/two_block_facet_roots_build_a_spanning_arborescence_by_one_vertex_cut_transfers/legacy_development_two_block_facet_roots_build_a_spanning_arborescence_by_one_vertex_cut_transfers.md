# Two-block facet roots build a spanning arborescence by one-vertex cut transfers — preserved pre-item development

## Composition

(none yet)

## Development

## Two-block facet roots build a spanning arborescence by one-vertex cut transfers

Fix the canonical good-order selector (g(S)) on every proper nonempty coordinate subset, and use the two-block facet roots of §294.

Choose an arbitrary root coordinate (t).

### Growing-cut construction

Start with
[
S_1={t}.
]
For every nonempty proper set (S), the canonical two-block witness
[
pi_S=g(S),g(S^c)
]
is bad and has outermost root
[
a_S	o b_S
]
with
[
a_Sin S,qquad b_S
otin S.
]

Given (S_j), choose this canonical root and set
[
S_{j+1}=S_jcup{b_{S_j}}.
]

Exactly one new coordinate is added at each step. Hence after (n-1) stages,
[
S_n=V.
]

Record the directed edge
[
a_{S_j}	o b_{S_j}
]
when (b_{S_j}) is added.

### The selected roots form a spanning out-arborescence

Every new vertex (b_{S_j}) has one selected incoming edge from the already constructed set (S_j). The initial vertex (t) has none.

Therefore the selected edges form a directed spanning tree oriented away from (t).

In particular, for every coordinate (s), there is a unique selected directed path
[
t=x_0	o x_1	ocdots	o x_m=s.
]

Every edge on this path is the outermost root of an actual canonical two-block witness.

### Return path for any protected root

Given any actual protected root
[
s	o t,
]
build the arborescence rooted at (t). Its unique tree path (tleadsto s), together with (s	o t), gives a witnessed directed root cycle.

Thus a return path for a protected root requires neither degree theory nor a search through arbitrary flags.

### One-coordinate transfer provenance

Suppose vertex (v=b_{S_j}) is added, and write
[
R=Vsetminus(S_jcup{v}).
]
The consecutive cuts are
[
S_jmid({v}cup R)
]
and
[
(S_jcup{v})mid R.
]

Both are coarsenings of the same three-block ordered partition
[
oxed{S_jmid{v}mid R.}
]

Hence each arborescence step is mediated by one canonical three-block transfer cell. Its three relevant canonical witnesses are
[
g(S_j),v,g(R),
]
[
g(S_j),g({v}cup R),
]
and
[
g(S_jcup{v}),g(R).
]

All blocks are proper until the final stage.

### Consequence

The protected-root realization problem may be reduced to a particularly rigid return architecture:

- one backward protected root (s	o t);
- one outward tree path (tleadsto s);
- nested growing cuts (S_1subset S_2subsetcdots);
- every change of cut is a single-coordinate transfer through a three-block canonical cell.

This is stronger provenance than generic strong connectivity. The remaining gluing theorem only needs to understand one vertex crossing a two-block boundary at a time.
