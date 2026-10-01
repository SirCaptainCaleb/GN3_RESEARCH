# Every deletion-cover component in a minimum counterexample has order at least three

## Statement

Let H be a minimum counterexample. Then every component of every one-vertex deletion two-cover H-x=P|Q has order at least three.

## Body

Minimum-counterexample calculus already excludes singleton components. Suppose, for contradiction, that one component P has order two. Then V(P) union {x} has order three. Every boundary tournament on three vertices has a Hamilton tight path: choose any middle vertex; boundary antisymmetry selects one of the two orders of the remaining vertices. Hence H[V(P) union {x}] is Hamiltonian. A Hamilton path on V(P) union {x} together with the other deletion-cover component Q forms a spanning two-cover of H, contradicting that H is a counterexample. Therefore both deletion-cover components have order at least three.
