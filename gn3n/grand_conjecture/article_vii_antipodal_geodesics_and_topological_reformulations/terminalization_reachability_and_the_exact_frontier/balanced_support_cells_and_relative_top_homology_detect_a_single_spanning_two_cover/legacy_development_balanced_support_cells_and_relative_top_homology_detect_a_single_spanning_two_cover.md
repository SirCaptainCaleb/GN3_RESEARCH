# Balanced support cells and relative top homology detect a single spanning two-cover — preserved pre-item development

## Development

This supplies an exact relative target after the missing-point audit 275. It is a reformulation, not a proof of the required nonvanishing.

BALANCED DOWNWARD-CLOSURE COMPLEX.
For n>=3 let
Z_n={x in R^n: sum x_i=0, ||x||_1=1},
with its sign cells C_(A,B) from 275 for disjoint nonempty A,B.
Define
Z_H=|E(H)| intersect Z_n.
Equivalently C_(A,B) belongs to Z_H exactly when there are disjoint Hamiltonian supports A' superset A, B' superset B. Thus Z_H is a polytopal subcomplex of Z_n. Its partial sign supports need not themselves be Hamiltonian; extendability by the same witness makes the cell structure hereditary.

It is also the order-complex realization of the poset of mixed faces of E(H), up to barycentric subdivision.
More geometrically, the mixed-sign locus of |E(H)| retracts equivariantly onto Z_H: if a=sum x_i^+>0 and b=sum x_i^->0, replace positive coordinates by x_i/(2a) and negative coordinates by x_i/(2b). Linear homotopy to this normalization preserves sign support and hence stays in the same simplex of E(H).

EXACT DIMENSION.
dim Z_H = n-kappa_2(H)-2.
Indeed a maximum support pair has total size n-kappa_2(H), and its balanced cell has dimension total size minus two. Conversely every balanced cell lies in such a witnessing support-pair cell.
For the actual-pair order complex Khat, equality in the same dimension formula follows by choosing Hamilton orders on a maximum pair and successively adding prefix vertices from a starting singleton|singleton pair.

TOP CELLS ARE EXACTLY SPANNING COVERS.
Put d=n-2.
The d-cells of Z_n correspond to ordered nontrivial bipartitions A|B of V. Such a cell belongs to Z_H if and only if A and B themselves are Hamiltonian: disjoint extending witnesses have no unused label and hence must equal A,B.
Let N(H) be the number of unordered nontrivial support bipartitions A|B with Hamiltonian sides. Path orders are not counted.
Then cellular relative homology gives
H_d(Z_H, Z_H^(d-1); F_2) = F_2^(2 N(H)).
After the free sign-swap quotient,
H_d(Z_H/T, Z_H^(d-1)/T; F_2) = F_2^(N(H)).
Proof: the relative cellular chain group has one basis element per allowed d-cell, its boundary lands in the lower skeleton, and there are no (d+1)-cells. Antipodality pairs the two ordered versions of each support partition.

Consequently
pc(H)<=2
if and only if
this relative top homology is nonzero.
By contrast maximal ABSOLUTE equivariant index of Z_H is n-2 if and only if Z_H=Z_n, equivalently every proper nonempty subset is Hamiltonian (275). This distinction is essential: one full-support cell versus every full-support cell.

A LOCAL RELATIVE-DEGREE CRITERION.
A map of pairs
F:(B^d, boundary B^d) -> (Z_H, Z_H^(d-1))
with F_*[B^d,boundary B^d] nonzero produces an actual spanning support partition. It is enough that the mod-two local degree be nonzero in one allowed d-cell.
Equivariance can be imposed by adjoining a disjoint antipodal copy of the source ball and defining the second map by sign swap. This does not require a map from the entire antipodal d-sphere, and does not demand that every full-support target cell be present.
A proposed construction must prove both the lower-skeleton boundary condition and the nonzero local degree. Merely extending a source face, or supplying pointwise deletion covers, proves neither.

RELATION TO THE ODD UNIFORM CASE.
If n=2r+1 and the uniform middle-layer profile holds, E(H) is an antipodal S^(n-2), but Z_H has dimension n-3: its largest allowed balanced cells have support sizes r|r and omit one vertex. Therefore the relative group above is zero, as it must be when no spanning cover exists. The large absolute index of E(H) comes from its monochromatic parts and cannot be transferred to Z_H without an additional avoidance argument.

Limits. No nonzero relative class or local degree is constructed here. This target records exactly the existential conclusion we want and avoids the universally false maximal-index demand. Any future coherence proof must derive its relative nonvanishing from identifiable tournament or minimum-counterexample constraints.
