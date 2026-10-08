# Audit: the cubical core gives partial critical stars, not a monotone separator — preserved pre-item development

## Audit correction: pure source-sink cubical cocycles need not be monotone

The previous version incorrectly claimed that a surviving source-sink cubical cocycle C=delta f can be normalized so that f is monotone in the natural cube orientation.

This is false. Purity says only that, at each vertex incident with C, all incident C-edges are oriented either all outward or all inward. It does not force all source vertices to have the same f-value globally, because different source-sink components can be connected through non-C edges in a way that reverses the local f polarity.

A concrete 3-cube counterexample is the Boolean function with value 0 at 000 and 111 and value 1 at the other six vertices. Its cut consists of the six edges incident with the two antipodal extrema. At 111 all cut edges are outgoing; at 000 all cut edges are incoming; every other incident vertex is pure as well. The cut is antipodally invariant, but f is neither monotone nor antimonotone.

Therefore the claimed global source upset, self-dual monotone separator, inclusion-minimal source, and complete critical-set/extension-desert conclusion are withdrawn.

### Valid residue

Let A be any source vertex of the surviving deletion-edge graph, with B=V(H)-A, and let D(A) be the set of coordinates x in A for which the outgoing cube edge A -> A-{x} survives.

For every x in D(A), that edge represents the one-hole support pair
(A-{x}, B).
Hence A-{x} and B are Hamiltonian.

Since H has no spanning two-cover, A is non-Hamiltonian. Also B union {x} is non-Hamiltonian for every x in D(A), because otherwise
(A-{x}) | (B union {x})
would span H.

Thus every source gives a partial critical star:
B Hamiltonian;
A non-Hamiltonian;
A-x Hamiltonian and B+x non-Hamiltonian for all surviving coordinates x in D(A).

The closure problem is therefore to control the size and interaction of these partial critical stars, or to show that the cubical cocycle necessarily contains a source with sufficiently rich outgoing star. No global monotonicity is presently established.
