# A Hamiltonian enlargement of a noninsertable path forces order disagreement

## Statement

Let P=(p_1,...,p_m) be a displayed tight path in a boundary tournament H and let x lie outside V(P). Suppose x is noninsertable into every position of the displayed order P, but H[V(P) union {x}] is Hamiltonian. Then every Hamilton tight path R on V(P) union {x} has order disagreement with P on two vertices of V(P).

## Body

Suppose some Hamilton path R on V(P) union {x} preserves the relative order of every pair of vertices of P. Since R contains all vertices of P and only one additional vertex x, deleting x from the word R leaves exactly the displayed order P. Therefore R is obtained from P by inserting x into one of its m+1 positions. This contradicts noninsertability.

Hence every Hamilton order on the enlarged support reverses the relative order of at least one common vertex pair. The general path-intersection calculus may then be applied to P and R to produce its standard local disagreement witnesses.

This is the line-independent final step of astra003fiveonepath; no quadratic potential, repartition, component-size, or five-side hypothesis is used.