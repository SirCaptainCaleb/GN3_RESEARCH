# Full-label 3|5|5 plateaus have at least one hundred forty-eight three-side supports

## Statement

Let D be the family of three-side supports in a trapped order-thirteen 3|5|5 Astra-003 component, let G be its two-shadow, and let F be the complement of G in K_13. Then |D|>=148. More precisely, either |E(F)|<=14, in which case |D|>=150, or F is exactly K_{4,4} plus five isolated vertices, in which case at least 148 supports are forced.

## Body


# Sharpening the full-label shadow bound

Use the full-label shadow theorem 47fd923c847c. Thus every vertex lies in the two-shadow G, every shadow edge has D-codegree at least seven, and for every edge uv of G,

|N_F(u) union N_F(v)| <= 4,

where F is the complement of G. Also Delta(F)<=4.

The previous argument already gives |E(F)|<=16, with equality only for K_{4,4} plus five isolated vertices. We sharpen the near-extremal case.

Assume |E(F)|=15. Since the Delta(F)<=3 branch has at most thirteen edges, choose u with d_F(u)=4. Put A=N_F(u), |A|=4, and let B be the other eight vertices. For every v in B, uv is a G-edge, so the neighborhood-union bound forces N_F(v) subseteq A. Hence B is independent in F and every F-edge is incident with A.

Write e=|E(F[A])| and m=|E_F(A,B)|. Since the sum of F-degrees over A is at most 16,

4 + 2e + m <= 16,

while

15 = |E(F)| = 4 + e + m.

Therefore e<=1.

If e=1, then m=10 and every vertex of A has F-degree four. Let a3,a4 be the two vertices of A not incident with the unique edge of F[A]. For any positive-degree b in B, if a3b were a G-edge then, because d_F(a3)=4, the neighborhood-union bound would force N_F(b) subseteq N_F(a3). But N_F(b) is a nonempty subset of A, whereas N_F(a3) contains no vertex of A, impossible. Thus every positive-degree b is adjacent in F to both a3 and a4. Since each of a3,a4 has exactly three neighbors in B, all positive-degree vertices of B lie in one common three-set C. Now take either endpoint a1 of the unique edge in F[A]. It has exactly two neighbors in B. Hence some b in C is not adjacent to a1. Then a1b is a G-edge. Again d_F(a1)=4, so the neighborhood-union bound requires N_F(b) subseteq N_F(a1). But N_F(b) contains a3 and a4, neither of which lies in N_F(a1), contradiction. Hence e=1 is impossible.

Thus e=0. Then m=11. The four A-to-B degrees sum to eleven and are each at most three, so after relabeling they are 3,3,3,2. Let a1,a2,a3 be the three vertices of A of F-degree four, and a4 the remaining one. If b in B has positive F-degree, then for each i=1,2,3 the edge a_i b cannot lie in G: otherwise d_F(a_i)=4 and the neighborhood-union bound would force the nonempty set N_F(b) subseteq A into N_F(a_i), which contains no vertex of A. Hence every positive-degree b is adjacent to all of a1,a2,a3. Since each a_i has exactly three B-neighbors, there are exactly three positive-degree vertices C subseteq B, each joined to a1,a2,a3. The remaining two A-B edges join a4 to two vertices of C. Consequently F is K_{4,4} minus one edge, on bipartition A and {u} union C, together with five isolated vertices.

But this is impossible. Let a4c be the unique missing edge of that K_{4,4}; then a4c is an edge of G. Its common neighbors in G are exactly the five isolated vertices, so it lies in at most five G-triangles. Every D-triple containing a4c must be a G-triangle, hence d_D(a4c)<=5, contradicting d_D(a4c)>=7.

Therefore |E(F)| is never fifteen. Hence either |E(F)|<=14 or |E(F)|=16.

If |E(F)|<=14, then |E(G)|>=78-14=64. Since every edge of G has D-codegree at least seven,

3|D| = sum_{e in E(G)} d_D(e) >= 7*64 = 448,

so |D|>=150.

It remains to treat |E(F)|=16. By the equality classification in 47fd923c847c, F is K_{4,4} plus five isolated vertices. Let the K_{4,4} sides be A and C, and let R be the five isolated vertices. Any G-edge with at least one endpoint in A has exactly seven common neighbors in G: the other vertices of A together with R. Since its D-codegree is at least seven, every G-triangle containing such an edge lies in D. The same holds for C.

Thus every G-triangle not wholly contained in R belongs to D. The shadow G is the union of the two cliques A union R and C union R, each of order nine, intersecting in R. The number of G-triangles with at least one vertex in A or C is

2*C(9,3) - 2*C(5,3) = 168 - 20 = 148.

Therefore |D|>=148 in the equality case.

Combining the two cases gives |D|>=148.
