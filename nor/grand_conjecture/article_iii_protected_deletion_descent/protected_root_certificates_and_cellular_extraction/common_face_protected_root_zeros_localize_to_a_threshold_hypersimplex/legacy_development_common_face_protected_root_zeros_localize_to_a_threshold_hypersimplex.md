# Common-face protected-root zeros localize to a threshold hypersimplex — preserved pre-item development

## Composition

(none yet)

## Development

Let F=B_1|...|B_s be a proper permutahedron face and suppose a family of protected roots carried by refinements of F has a positive physical dependence. Fix the normalized p-cut. Let B=B_j be the unique face block containing the cut boundary, with K=B_1 union ... union B_{j-1} and r=p-|K|, so 1<=r<=|B|-1 unless the cut lies exactly between blocks.

Pair every carried root with the inward face-normal functional used in root 42. A root whose endpoints lie in different face blocks has strictly positive face-normal value, while a root internal to one block has value zero. A positive dependence summing to zero has zero total pairing, so no cross-block root can occur. Since every protected root crosses the physical p-cut, an internal root can only lie in the boundary block B. If the cut lies exactly between blocks, every protected crossing root is cross-block, so no positive dependence exists at all.

Thus every common-face positive protected-root dependence localizes to the unique threshold block B.

For a chamber refining F, its protected cut has the form C=K union T with T a subset of B of size r. After projection to the zero-sum coordinate space W_B on B, the centered global cut vector z_C becomes
1_T-(r/|B|)1_B,
the centered vertex of the hypersimplex Delta(B,r). A protected root rho=e_a-e_c in the dependence has a in T and c in B minus T, so -rho is exactly the edge direction from T to T-a+c in that hypersimplex.

Therefore the faithful common-face extraction problem is a hypersimplex problem: vertices are the realized threshold cuts T, protected roots are oriented Johnson/hypersimplex edges, and the quadratic full-cut moment of root 53 projects to a nonzero scalar multiple of the centered hypersimplex vertex.

This gives a natural fixed-point arena. Any continuous common-face protected-state carrier can be projected from the permutahedral threshold block to Delta(B,r). A root zero becomes a positive circulation of hypersimplex edges. The full-cut perturbation adds a radial hypersimplex-vertex term carrying side provenance. Root 50 proves complete extraction when |B|=4, while root 42 shows that a zero of the all-refinements ternary averaged carrier requires some face block of size at least six. Hence the unresolved topological extraction problem can be stated entirely on hypersimplices Delta(m,r) with m>=6.

This is the appropriate setting for a Sperner/Brouwer attack: prove that the protected edge assignment on the realized chamber refinement of Delta(B,r) either has a boundary-compatible fixed point yielding a realizable Johnson exchange, or forces an edge circulation whose cut defect can be reduced.
