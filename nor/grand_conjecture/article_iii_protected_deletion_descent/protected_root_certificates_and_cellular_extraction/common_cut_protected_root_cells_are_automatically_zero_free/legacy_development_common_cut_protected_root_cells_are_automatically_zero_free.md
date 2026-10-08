# Common-cut protected root cells are automatically zero-free — preserved pre-item development

## Composition

(none yet)

## Development

## Common-cut cells are automatically zero-free

Let (Csubsetneq V) be a nontrivial cut and write
[
u_C=mathbf 1_C-	frac12mathbf 1.
]
Consider any finite collection of oriented coordinate roots
[
ho_i=e_{a_i}-e_{b_i}
]
such that every root crosses the same oriented cut:
[
a_iin C,qquad b_i
otin C.
]

Then for every (i),
[
langle u_C,ho_iangle=1.
]
Consequently every convex combination
[
x=sum_ilambda_iho_i,
qquad
lambda_ige0,quad sum_ilambda_i=1,
]
satisfies
[
langle u_C,xangle=1.
]
Therefore
[
0
otinoperatorname{conv}{ho_i}.
]

### Cellular form

Let (P) be any polytope or regular cell whose vertices are labeled by roots crossing the same oriented cut (C). Extend the vertex labeling affinely over any triangulation of (P), or affinely on (P) itself when the labels respect its affine relations. The image of every point of (P) remains in
[
{x:langle u_C,xangle=1},
]
so the extension is zero-free.

No special feature of a square is required.

Thus:

> Any commuting square, braid polygon, or higher carrier face whose root labels all cross one common oriented central cut is automatically a safe zero-free cell.

Under reversal,
[
Cmapsto C^c,qquad
u_Cmapsto-u_C,qquad
ho_imapsto-ho_i,
]
so the statement is equivariant.

### Consequence for Article III topology

The local coherence problem should be split sharply into two classes.

1. **Cut-preserving residues.**  
   If all competing protected labels in the residue retain the same central cut and orientation, the residue may be filled immediately. Convexity cannot create a zero.

2. **Cut-changing residues.**  
   Only these can contribute a nontrivial zero or obstruction. Here no single cut normal separates all labels, and genuine compatibility information is required.

The fully-curved (K_{2,2}) barrier square is the first concrete instance of class 1. The same argument applies verbatim to any higher Coxeter residue once common-cut provenance is verified.

This substantially narrows the compatible-equivariant-complex frontier: one need not solve arbitrary square/hexagon coherence. One only needs to classify the rank-two residues in which the protected central cut actually changes, and show that such a cut change either gives a legal improvement or enters a separately controlled cell.
