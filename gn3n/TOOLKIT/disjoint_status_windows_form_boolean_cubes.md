# Disjoint internal status windows form Boolean cubes

**Summary:** Pairwise disjoint internal triple windows inside permutahedron blocks can have their status bits prescribed independently.

## Statement

If pairwise disjoint three-position windows all lie wholly inside blocks of a permutahedron face, then their chamber-status projection is the full Boolean cube, with every pattern occurring equally often.

## Body

Let
[
F=B_1|cdots|B_k
]
be a permutahedron face and let (I) be a set of status positions such that the windows
[
W_i={i,i+1,i+2},qquad iin I,
]
are pairwise disjoint and each lies wholly in one block.

For each (i), swap the vertices in positions (i) and (i+2). This preserves the face and flips exactly the selected status (epsilon_i). Because the windows are disjoint, these involutions commute and do not affect the other selected coordinates. Hence the generated ((mathbb Z/2)^{I})-action realizes every vector in ({0,1}^{I}) exactly once on each orbit.

Thus the selected status bits are jointly independent under the uniform chamber distribution.

## Metadata

- ID: disjoint_status_windows_form_boolean_cubes
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
