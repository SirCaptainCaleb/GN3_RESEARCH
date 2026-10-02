# Full-label 3|5|5 plateaus have at least one hundred forty-five three-side supports

## Statement

Let D be the family of three-side supports in a trapped order-thirteen 3|5|5 Astra-003 component and let G be its two-shadow. Then every vertex lies in G, every vertex of G has degree at least 8, and every edge of G has at least 7 common neighbors. Consequently the complement F of G has at most 16 edges. Hence |E(G)|>=62 and |D|>=145. If |E(F)|=16, then F is exactly K_{4,4} plus five isolated vertices.

## Body

# A 145-support lower bound from the full-label shadow

Let D be the three-uniform family of reachable three-side supports in a trapped order-thirteen 3|5|5 connected component of the Astra-003 move graph, and let G be its two-shadow.

The Johnson-projection lemma gives the following coordinate-wise exchange property: for every X in D and every x in X, at least six vertices y outside X satisfy X-x+y in D.

As observed in the support-expansion argument, every edge uv of G therefore has D-codegree at least seven. In particular uv has at least seven common neighbors in G. Also every nonisolated vertex of G has degree at least eight. The full-label reachability theorem says every vertex occurs in D, so G has no isolated vertices. Thus

minimum degree of G >= 8.

Let F be the complement of G in K_13. Then maximum degree of F <=4.

For any edge uv of G, the common neighbors of u,v in G are precisely the vertices among the other eleven that lie in neither N_F(u) nor N_F(v). Since there are at least seven such common neighbors,

|N_F(u) union N_F(v)| <=4.   (*)

We bound |E(F)|.

## If Delta(F)=4

Choose u with d_F(u)=4 and put A=N_F(u), |A|=4. Let

B=V(H)-({u} union A),

so |B|=8.

For every v in B, uv is an edge of G. Applying (*) gives

N_F(v) subseteq A,

because N_F(u)=A already has four vertices. Hence there are no F-edges inside B and none from u to B. Every F-edge is incident with A.

Therefore

|E(F)| = sum_{a in A} d_F(a) - |E(F[A])| <= 16.

Suppose equality holds. Then F[A] is empty and every a in A has degree four. Each a is adjacent to u and therefore has exactly three neighbors in B.

Now take b in B. We know N_F(b) subseteq A. If b has positive F-degree but is not adjacent to some a in A, then ab is an edge of G. Since d_F(a)=4 and N_F(a) lies in {u} union B whereas N_F(b) lies in A, the two F-neighborhoods are disjoint. Thus

|N_F(a) union N_F(b)| = 4+d_F(b)>4,

contradicting (*). Hence every positive-degree b is adjacent to all four vertices of A and has degree four.

The A--B edge count is 4*3=12, so exactly three vertices of B have positive degree. Together with u they form a four-vertex class C, and F[A union C]=K_{4,4}; the other five vertices are isolated. Thus equality |E(F)|=16 has the unique form K_{4,4} plus five isolated vertices.

## If Delta(F)<=3

If Delta(F)<=2 then trivially |E(F)|<=13. Assume Delta(F)=3 and choose u with N_F(u)=A of order three. Let B be the remaining nine vertices.

For v in B, uv is an edge of G, so (*) gives

|A union N_F(v)|<=4.

Thus v has at most one F-neighbor outside A. Therefore F[B] has maximum degree at most one and

|E(F[B])|<=4.

The sum of degrees over A is at most nine. Since the three edges from u to A contribute three to that sum and edges inside A contribute twice,

|E_F(A,B)| <= 6-2|E(F[A])|.

Hence

|E(F)| = 3+|E(F[A])|+|E_F(A,B)|+|E(F[B])|
<= 3+|E(F[A])|+6-2|E(F[A])|+4
<=13.

So in all cases |E(F)|<=16. Consequently

|E(G)| >= C(13,2)-16 = 62.

Finally count pair--triple incidences in D. Every edge of G has D-codegree at least seven, so

3|D| = sum_{e in E(G)} d_D(e) >= 7|E(G)| >= 434.

Therefore

|D| >= ceil(434/3)=145.

Thus a trapped order-thirteen 3|5|5 plateau has at least 145 distinct reachable three-side supports. The sparsest possible two-shadow is the complement of a K_{4,4} missing-edge block.