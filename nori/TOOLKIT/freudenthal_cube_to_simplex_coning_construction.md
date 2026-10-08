# Freudenthal cube-to-simplex coning construction

**Summary:** Freudenthal-triangulate Q_n, cone each positive facet to a new coordinate vertex, and the result is exactly a triangulated n-simplex. Each permutation sector is cut in two at the midpoint of the edge from the distinguished vertex 0 to its first coordinate vertex.

## Statement

The Freudenthal triangulation of Q_n, after adjoining one vertex a_i beyond each positive facet P_i and coning P_i to a_i, admits an explicit geometric realization as a triangulation of the n-simplex. Each coordinate permutation sector of the simplex is split into exactly two top simplices: one Freudenthal cube chamber and one positive-facet cone chamber.

## Body


## Exact simplex realization

Let Delta^n have vertices e_0,e_1,...,e_n. Start with the Freudenthal triangulation of Q_n, whose vertices are subsets S of [n]. Adjoin a new vertex a_i for each coordinate i and cone the positive cube facet P_i={S:i in S} to a_i.

Define a realization Phi on vertices by

- Phi(emptyset)=e_0;
- Phi({i})=(e_0+e_i)/2;
- for |S|>=2, Phi(S)=|S|^{-1} sum_{i in S} e_i, the barycenter of the simplex face spanned by S;
- Phi(a_i)=e_i.

### Theorem
Phi realizes the completed Freudenthal complex as a simplicial triangulation of Delta^n.

### Proof by permutation sectors

Fix a permutation pi=(pi_1,...,pi_n) of [n]. Let

b_k=(1/k) sum_{j=1}^k e_{pi_j}  for k>=2,
m=(e_0+e_{pi_1})/2.

The Freudenthal cube simplex for pi maps to

conv(e_0,m,b_2,...,b_n).

The cone simplex obtained from the positive pi_1-facet maps to

conv(e_{pi_1},m,b_2,...,b_n).

Their union is the simplex

C_pi=conv(e_0,e_{pi_1},b_2,...,b_n),

split into two simplices by the point m on the edge e_0 e_{pi_1}.

But C_pi is exactly the standard permutation sector

{lambda in Delta^n : lambda_{pi_1} >= lambda_{pi_2} >= ... >= lambda_{pi_n}}.

Indeed the extreme points of that order cone in the simplex are e_0 and the successive barycenters e_{pi_1}, b_2,...,b_n.

The n! permutation sectors C_pi have disjoint interiors and cover Delta^n. Their common faces agree on equalities among barycentric coordinates, and the displayed midpoint split agrees on shared faces because every vertex image depends only on its subset S. Hence all 2 n! top simplices fit face-to-face and triangulate Delta^n.

### Boundary face dictionary

This realization also explains the simplex-face structure.

- The distinguished simplex vertex e_0 is the negative cube corner emptyset.
- The new cone vertex a_i is the simplex vertex e_i.
- A cube singleton {i} is the midpoint of edge e_0 e_i.
- A cube vertex S with |S|>=2 is the barycenter of the simplex face spanned by {e_i:i in S}.

The macroface opposite e_0 is exactly the barycentric subdivision of the (n-1)-simplex on e_1,...,e_n: its vertices are a_i for singleton faces and cube vertices S for faces of size at least two.

For i>=1, the macroface opposite e_i is recursively the same completed construction on the negative cube facet x_i=0.

### NOR relevance

A maximal cube Freudenthal chamber still records a coordinate order pi. Its consecutive ordered-window faces therefore sit inside an honest simplex triangulation. This provides a direct route for importing simplex-topology tools such as Sperner/KKM, degree, connectivity, and chain arguments without first replacing the cube geometry by an abstract PL model.

The next question is not whether the cube completion is a simplex: it is. The next question is which labeling or cochain induced by a hypothetical NOR counterexample satisfies a simplex boundary condition strong enough for one of these theorems to force a low-variation chamber.


## Metadata

- ID: freudenthal_cube_to_simplex_coning_construction
- Kind: toolkit
- Version: 2
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
