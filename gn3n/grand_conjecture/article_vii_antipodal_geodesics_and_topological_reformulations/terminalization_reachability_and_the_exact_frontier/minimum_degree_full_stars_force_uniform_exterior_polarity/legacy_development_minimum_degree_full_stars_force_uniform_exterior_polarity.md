# Minimum-degree full stars force uniform exterior polarity — preserved pre-item development

## Development

## Minimum source degree forces uniform polarity across every exterior coordinate

Let C be a nonempty pure source-sink cubical 1-cocycle arising from the surviving one-hole deletion-cover core of a minimum counterexample.

Choose a source vertex of minimum positive outdegree, and apply the full-star descent theorem to its active coordinate set. We obtain a full-star source D such that
d=|D|
is the minimum positive outdegree of any source in C.

Put B=V-D. Then:
- D is non-Hamiltonian;
- D-x is Hamiltonian for every x in D;
- B is Hamiltonian;
- B+x is non-Hamiltonian for every x in D.

Fix y in B. The edge D+y -> D is not in C, because D is already a source and purity forbids an incoming C-edge.

For x in D, the square on x,y contains the selected edge D -> D-x. Since D-x is a sink, its outgoing y-edge is absent. Cocycle parity therefore says that exactly one of
D+y -> D-x+y,
D-x+y -> D-x
lies in C.

Define
X_y={x in D : D+y -> D-x+y lies in C}.

If X_y is nonempty, D+y is a source. Its only possible outgoing coordinates are the x in D, because the y-edge to D is absent. Hence its outdegree is exactly |X_y|. By minimality of d,
|X_y|>=d.
Since X_y subseteq D and |D|=d, X_y=D.

Therefore for every y in B there are exactly two possibilities.

### Type I: upper polarity
X_y=D.
Then for every x in D,
D+y -> D-x+y
is selected.
Thus D+y is a source of outdegree d, B-y is Hamiltonian, and D-x+y is Hamiltonian for every x in D. The y-edge D+y -> D is absent.

### Type II: lower polarity
X_y=empty.
Then cocycle parity forces, for every x in D,
D-x+y -> D-x
to be selected.
Hence every D-x+y is a source. Since it has at least the outgoing y-edge and d is the minimum positive source outdegree, while |D-x+y|=d, it must have outdegree exactly d and therefore is itself a full-star source.

Thus an exterior vertex either:
- has uniform upper polarity simultaneously for all x in D; or
- has uniform lower polarity simultaneously for all x in D, in which case replacing any x in D by y produces another full-star source of the same minimum degree.

No mixed x-by-x polarity is possible.

This converts the cubical core into a two-coloring of the exterior labels relative to a minimum-degree full-star source. Type II labels generate Johnson exchanges among full-star sources; Type I labels generate a coherent family of Hamiltonian cross-exchanges D-x+y together with Hamiltonian B-y.

The next closure question is whether both polarities can coexist, or whether either uniform regime already forces a spanning two-cover.
