# Two blocked endpoint truncations force a displayed-edge reversal

## Statement

Let H be a boundary tournament, let R=(r_0,\ldots,r_m), m>=2, be a displayed tight path, and let x lie outside V(R). If both induced supports
(V(R)-{r_0}) union {x}
and
(V(R)-{r_m}) union {x}
are non-Hamiltonian, then x is noninsertable into every position of the displayed order of R. Consequently H contains a tight triple reversing a displayed edge of R.

## Body

Suppose first that x could be inserted into the displayed order of R. If x is inserted before r_0, deleting the opposite endpoint r_m from the resulting tight path gives a Hamilton path on (V(R)-{r_m}) union {x}, contradiction. If x is inserted after r_m, deleting r_0 gives a Hamilton path on (V(R)-{r_0}) union {x}, contradiction. For an insertion at any internal gap, both original endpoints remain endpoints of the enlarged tight path, so deleting either one gives one of the two forbidden Hamiltonian endpoint truncations. Hence x is globally noninsertable in the displayed order R. Apply acdec36ae3ca to obtain a tight triple reversing some displayed edge of R.
