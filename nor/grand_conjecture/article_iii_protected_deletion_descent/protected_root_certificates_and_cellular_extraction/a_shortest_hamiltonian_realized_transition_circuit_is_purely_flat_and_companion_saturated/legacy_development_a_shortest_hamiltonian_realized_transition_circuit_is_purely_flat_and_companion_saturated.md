# A shortest Hamiltonian realized-transition circuit is purely flat and companion-saturated — preserved pre-item development

## Shortest Hamiltonian transition-root cycles are forced entirely flat

Let (mathcal R) be the directed graph on coordinates whose edge (u	o v) is present whenever some full coordinate order realizes a genuine ternary transition on four consecutive coordinates with dropped coordinate (u) and entering coordinate (v).

Let
[
C:x_0	o x_1	ocdots	o x_{k-1}	o x_0
]
be a shortest directed cycle in (mathcal R), and assume (C) is Hamiltonian on the ambient coordinate set.

Take any cycle edge
[
a	o d
]
and any transition carrier ((a,b,c,d)) realizing it.

### Fully-curved carriers are impossible

Suppose this carrier is fully curved. By the complete (K_{2,2}) barrier-square theorem, the same tetrahedron also realizes the transition root
[
a	o c.
]
The four carrier coordinates are distinct, so (c
eq d).

Because (C) is Hamiltonian, (c) is a vertex of (C). Since (a	o d) is the unique outgoing cycle edge from (a), the root (a	o c) is not a cycle edge. It is therefore a directed chord. The chord (a	o c) followed by the old directed segment of (C) from (c) back to (a) gives a strictly shorter directed cycle in (mathcal R), contradicting minimality.

Hence **no carrier of any edge of a shortest Hamiltonian transition-root cycle can be fully curved**.

### Every carrier is flat and its disjoint companion is a cycle edge

Therefore every transition carrier of every edge of (C) is flat.

For a flat carrier ((a,b,c,d)), the disjoint-companion theorem realizes
[
b	o c
]
on the double endpoint swap ((b,a,d,c)).

Again Hamiltonicity puts (b,c) on (C). If (b	o c) were not already an edge of (C), it would be a directed chord and give a shorter cycle. Thus
[
b	o cin E(C).
]

So every carrier of a cycle edge pairs it with a **nonadjacent disjoint cycle edge**, and the carrier is necessarily flat. For each such incidence, the two transition orientations are opposite, as in the audited companion-root theorem.

### Consequence

A shortest Hamiltonian cycle in the full realized transition-root graph has an extremely rigid form:

- every transition carrier of every cycle edge is flat;
- every carrier's disjoint companion root is another edge of the same cycle;
- no fully-curved tetrahedron can realize any cycle edge;
- the resulting carrier-companion graph on (E(C)) has minimum degree at least one and no adjacency incidences.

Thus the fully-curved part of the Article III root system cannot support a shortest Hamiltonian positive circuit once all realized transition roots are admitted. The only Hamiltonian circuit obstruction in this enlarged physical-root graph is a purely flat companion-saturated cycle.

### Scope for the protected-root program

The theorem is unconditional for the enlarged graph (mathcal R). To transfer the contradiction directly to a cycle minimized inside a narrower provenance class, one still needs closure of that class under the same local side/companion realizations.

Nevertheless this gives a precise closure target: **prove that a minimum protected positive circuit may be minimized in the enlarged realized-transition graph without losing the extraction data.** Once that provenance-minimization bridge is established, every Hamiltonian mixed circuit containing a terminal full barrier disappears, and the remaining Hamiltonian case is purely flat.
