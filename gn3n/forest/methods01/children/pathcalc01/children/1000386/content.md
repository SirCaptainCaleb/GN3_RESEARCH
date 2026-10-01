# Two same-end extenders force Hamiltonicity or two reverse endpoint triples

## Statement

Let H be a boundary tournament and let R=(r_1,...,r_m), m>=2, be a tight path. Let a,b,c be distinct vertices outside R. Suppose both (a,R) and (b,R) are tight and (R,c) is tight. Then either H[V(R) union {a,b,c}] is Hamiltonian, or both (r_1,b,a) and (r_1,a,b) are tight. Symmetrically, if (R,a) and (R,b) are tight and (c,R) is tight, then either the same union is Hamiltonian, or both (b,a,r_m) and (a,b,r_m) are tight.

## Body

Suppose first that (a,R) and (b,R) are tight and that (R,c) is tight.

If (a,b,r_1) is tight, then
(a,b,r_1,r_2,...,r_m,c)
is a Hamilton tight path on V(R) union {a,b,c}: the first triple is tight by assumption, the next triple (b,r_1,r_2) is inherited from (b,R), all interior triples are inherited from R, and the final triple (r_{m-1},r_m,c) is inherited from (R,c).

Likewise, if (b,a,r_1) is tight, then
(b,a,r_1,r_2,...,r_m,c)
is a Hamilton tight path.

Therefore, if the full support is non-Hamiltonian, both displayed first triples are non-tight. Boundary antisymmetry applied separately to their reversal pairs gives
(r_1,b,a)
and
(r_1,a,b)
tight.

For the symmetric statement, if either (r_m,a,b) or (r_m,b,a) is tight, append the corresponding ordered pair to the tight path (c,R) to obtain a Hamilton path. If neither is tight, boundary antisymmetry gives both (b,a,r_m) and (a,b,r_m) tight.

Thus two exterior vertices extending the same end cannot in general be freely ordered before or after the path. Failure of both possible orders is exactly witnessed by two reverse endpoint triples.
