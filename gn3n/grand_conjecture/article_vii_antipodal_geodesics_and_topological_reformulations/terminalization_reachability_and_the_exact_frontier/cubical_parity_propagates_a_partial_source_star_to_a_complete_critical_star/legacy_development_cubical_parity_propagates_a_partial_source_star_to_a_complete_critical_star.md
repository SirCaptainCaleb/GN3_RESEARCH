# Cubical parity propagates a partial source star to a complete critical star — preserved pre-item development

## Development

## Cubical parity propagates every partial source star to a full source star

Let C be a nonempty cubical 1-cocycle in the naturally oriented Boolean cube on V. Assume every vertex incident with C is pure: all its incident C-edges are either outgoing or all incoming.

For a source vertex S subseteq V, define its active coordinate set
D(S)={x in S : the edge S -> S-{x} lies in C}.
This set is nonempty.

### Propagation lemma

If x is in D(S) and y is in S-D(S), then
the edge
S-{y} -> S-{x,y}
also lies in C.

Proof. Consider the square on coordinates x,y with vertices
S,
S-{x},
S-{y},
S-{x,y}.

The top x-edge S -> S-{x} is in C. The top y-edge is not, by y notin D(S). Since S-{x} is a sink (it is the head of a C-edge), purity forbids its outgoing y-edge
S-{x} -> S-{x,y}
from lying in C.

A cubical 1-cocycle has even parity on every square. Therefore the remaining x-edge
S-{y} -> S-{x,y}
must lie in C. Its tail S-{y} is consequently a source. QED.

### Full-star descent

Let D=D(S). Repeatedly delete the coordinates in S-D. The propagation lemma shows inductively that after deleting any subset E subseteq S-D, the vertex S-E is a source and every coordinate x in D remains active.

At the terminal vertex D itself, every coordinate belongs to D, so
D(D)=D.
Thus every edge
D -> D-{x}, x in D,
lies in C.

Therefore every nonempty pure source-sink cubical cocycle contains a full-star source. By reversing signs, it also contains the antipodal full-star sink.

### Consequence in a minimum counterexample

Apply this to the surviving deletion-edge cocycle of a minimum-order counterexample H.

At a full-star source D, put
B=V(H)-D.
For every x in D, the outgoing edge
D -> D-{x}
is a one-hole deletion-cover facet, hence
D-{x} and B are Hamiltonian.

Because H has no spanning two-cover, D itself is non-Hamiltonian. Also B union {x} is non-Hamiltonian for every x in D; otherwise
(D-{x}) | (B union {x})
would span H.

Hence every nonempty cubical core forces a genuine complete paired obstruction:
- D is non-Hamiltonian;
- D-{x} is Hamiltonian for every x in D;
- B is Hamiltonian;
- B union {x} is non-Hamiltonian for every x in D.

This recovers the critical-set/opposite-extension-desert reduction from the audited source-sink theorem without assuming any global monotonicity of the Boolean potential.

The remaining closure target is therefore exactly to rule out such a partition D sqcup B under minimum-counterexample hypotheses.
