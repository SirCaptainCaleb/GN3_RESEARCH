# Extremal compatibility density peels to a seven-cycle complement

## Statement

Let G be a graph on m>=7 vertices such that every edge lies in at most two triangles and every triangle contains an edge lying in no other triangle. If e(G)=floor(m^2/4)+2, then there is an ordering v_m,v_{m-1},...,v_8 of m-7 vertices such that, for each k=m,m-1,...,8, the vertex v_k has degree floor(k/2) in the induced k-vertex graph remaining at that stage, and the final induced seven-vertex graph is isomorphic to the complement of C_7.

## Body

# Proof

The two triangle properties are inherited by induced subgraphs. The density lemma underlying compatdensityplus2 proves that every such graph J of order k>=8 has a vertex of degree at most floor(k/2), and that every graph of order r>=7 with the two properties has at most floor(r^2/4)+2 edges.

Suppose G has m>=8 vertices and equality e(G)=floor(m^2/4)+2. Choose v with d_G(v)<=floor(m/2). Then

e(G-v)=e(G)-d_G(v)
       >= floor(m^2/4)+2-floor(m/2)
       = floor((m-1)^2/4)+2.

The general upper bound applied to G-v gives the reverse inequality. Hence equality holds throughout:
d_G(v)=floor(m/2)
and
e(G-v)=floor((m-1)^2/4)+2.

Iterating yields vertices v_m,...,v_8 with the asserted stage degrees and leaves a seven-vertex graph J with e(J)=14. It remains to identify J.

Since J has 14 edges, its average degree is four, so Delta(J)>=4.

First Delta(J) cannot be six. If v is universal, then for every neighbor x, the common-neighbor count t(vx)=d(x)-1 is at most two, so d(x)<=3. Thus
2e(J)<=6+6*3=24,
contrary to e(J)=14.

Next Delta(J) cannot be five. Let v have degree five, let u be its unique nonneighbor, and put S=N(v), |S|=5. Write s=|N(u) intersect S|. For x in S, every neighbor of x inside S is a common neighbor of v and x, so d_S(x)<=2. Hence
e(J)=5+s+e(J[S]).
If s=4, equality e(J)=14 forces e(J[S])=5, and therefore J[S] is a 5-cycle. For any cycle edge xy, the triangle vxy has t(vx)=t(vy)=2. Since u is adjacent to four of the five cycle vertices, some cycle edge xy has both ends adjacent to u; then t(xy)>=2 as well. Thus the triangle vxy has no edge lying in exactly one triangle, contradiction.
If s=5, equality forces e(J[S])=4. Here u and v are both adjacent to every vertex of S. For every edge xy of J[S], t(xy)>=2, so in each triangle vxy one of vx,vy must lie in no other triangle. But t(vx)=d_S(x), so every edge xy of J[S] has an endpoint of S-degree one. Since d_S<=2, every nontrivial component of J[S] is a path of order at most three; on five vertices such a graph has at most three edges, contradiction.
Thus Delta(J)=4. Since the average degree is four, J is 4-regular, and its complement is 2-regular on seven vertices. Hence the complement is either C_7 or C_3 disjoint-union C_4. The latter is impossible: the two opposite vertices of the C_4 are adjacent in J and have all three C_3 vertices as common neighbors, giving edge codegree at least three. Therefore the complement of J is C_7, as claimed.

For a deletion-cover compatibility graph saturating the bound floor(m^2/4)+2, the final seven labels therefore have incompatibility graph exactly C_7. This converts extremal compatibility density into an explicit cyclic incompatibility pattern.
