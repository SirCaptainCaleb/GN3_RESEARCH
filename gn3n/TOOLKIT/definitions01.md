# Boundary tournaments and tight-path conventions

**Summary:** Core definitions and path-construction hygiene for boundary tournaments, tight paths, path covers, Hamiltonicity, and induced subtournaments.

## Body

# Boundary tournaments and tight paths

A **boundary tournament** is a finite vertex set (V) together with, for every three distinct vertices (x,y,z), exactly one tight member of the reversal pair
[
(x,y,z),qquad (z,y,x).
]

A **tight path** is a vertex-simple ordered sequence
[
(v_0,ldots,v_k)
]
such that every consecutive triple ((v_{i-1},v_i,v_{i+1})) is tight. Paths of order one or two are tight vacuously.

A **tight path cover** partitions the vertex set into supports carrying tight paths. Write (operatorname{pc}(H)) for the minimum number of components in such a cover. A tight path containing every vertex is **Hamiltonian**. A **tight cycle** is a cyclic order whose cyclically consecutive triples are tight.

For (Ssubseteq V(H)), (H[S]) denotes the induced boundary tournament and (H-S=H[V(H)setminus S]).

## Path-construction hygiene

Tightness is local to displayed consecutive triples.

- Contiguous subpaths inherit tightness.
- Arbitrary reversal of a tight path is not valid.
- A cyclic rotation is valid only when its new wrap triple is checked.
- Concatenating tight pieces requires checking every new join triple.
- Insertion or endpoint replacement requires checking every newly created consecutive triple.

Boundary antisymmetry reverses a **single failed triple**: if ((x,y,z)) is not tight, then ((z,y,x)) is tight. It does not reverse an entire path.

## Metadata

- ID: definitions01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
