# Cellular Tucker forces an opposite label Coxeter carrier without triangulation diagonals — preserved pre-item development

## Composition

(none yet)

## Development

## Cellular Tucker forces an opposite-label Coxeter carrier without triangulation diagonals

Work in ternary arity with the switch-prism state space. Let P_V be the type-A permutohedron on the n physical coordinates and subdivide the switch interval I at the genuine cut levels. The product
[
X=P_V	imes I
]
is an n-dimensional ball with its centrally symmetric boundary involution
[
(pi,k)longmapsto(pi^{m rev},m-k).
]

Assume counterexamplehood, so every genuine switch-state vertex is bad. Label each state vertex by the signed physical middle coordinate of a selected nearest violating ternary window:
[
lambda(v)in{pm1,ldots,pm n}.
]
Use a reversal-compatible tie rule, so on boundary-antipodal state vertices
[
lambda(-v)=-lambda(v).
]

### Cellular Tucker theorem

Some product cell of X contains two state vertices labeled
[
+b,qquad -b
]
for the same physical coordinate b.

### Proof

Suppose not. Then for every product cell C, its vertex-label set contains no complementary pair.

Send a vertex labeled +i to the crosspolytope vertex +e_i and a vertex labeled -i to -e_i. If a finite signed coordinate set contains no complementary pair, its convex hull is a face of the n-dimensional crosspolytope, hence lies in the boundary sphere
[
partialDiamond^ncong S^{n-1}.
]

We extend the vertex map over X cell-by-cell. Induct on cell dimension. For a cell C, all maps already defined on proper faces land in the crosspolytope face spanned by the labels of vertices of C, because every proper face uses a subset of those labels. That target face is convex, so the boundary map extends continuously over C while remaining in the same crosspolytope face.

On paired boundary cells choose the extension on one member and define the extension on its antipodal mate by
[
F(-x)=-F(x).
]
The boundary involution is free, so this yields a continuous antipodal map
[
F|_{partial X}:S^{n-1}	o S^{n-1}.
]
The interior cell-by-cell extensions give an extension
[
F:X	o S^{n-1}.
]

But an antipodal self-map of (S^{n-1}) has odd degree, while any map extending over the n-ball has degree zero. Contradiction.

Therefore some genuine product cell contains complementary labels +b and -b. QED.

### Significance

This avoids the main triangulation problem in the signed-middle Tucker program. No diagonal edge of an arbitrary triangulation is interpreted as a repair. The topological conclusion is instead an honest **Coxeter product carrier** whose genuine state vertices include opposite obstruction labels for the same physical middle coordinate.

By the local theorem on signed-middle labels:
- a one-dimensional horizontal carrier is already a switch-crossing endpoint repair;
- a vertical carrier cannot be complementary.

Thus any unresolved minimal complementary carrier has genuine permutohedral dimension at least two. For ternary arity its first possible residue is an A2 braid face, exactly where directed-triangle and tetrahedral-curvature obstructions live.

The remaining extraction lemma is now sharply cellular: prove that a minimal Coxeter cell containing +b and -b either contains a horizontal complementary edge, or its chamber graph yields a controlled A2/higher-block residue from which one can extract a compatible repair path.
