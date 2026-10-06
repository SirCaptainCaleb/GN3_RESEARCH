# Status averages localize at permutahedron face boundaries

**Summary:** For any ordered-partition face, internal triple-window statuses average to zero; only coordinates adjacent to block boundaries can survive.

## Statement

Let F=B_1|...|B_k be a permutahedron face. If positions i,i+1,i+2 lie in one block, then the average sign status λ_i over all chambers of F is zero. Hence the face-average status vector is supported on at most two coordinates per block boundary.

## Body

Let (H) be a boundary (3)-tournament and
[
F=B_1|cdots|B_k
]
a face of the permutahedron. Its chambers are obtained by ordering vertices arbitrarily inside each block.

For a chamber (pi), let (lambda_i(pi)=+1) when the triple in positions (i,i+1,i+2) is tight and (-1) otherwise. If those three positions lie in one block, pair (pi) with the chamber obtained by swapping the vertices in positions (i) and (i+2). The swap stays inside the face and boundary antisymmetry flips (lambda_i). Thus the average of (lambda_i) over the chambers of (F) is zero.

Therefore the face-average status vector can be supported only at windows meeting block boundaries, at most two status coordinates per boundary.

## Metadata

- ID: permutahedron_face_status_localization
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
