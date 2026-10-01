# Failed high-low terminal pair forces both other high vertices onto the low mate

## Statement

Let R be a 9-vertex 7-edge linear triple system with degree multiset (3,3,3,2,2,2,2,2,2). Let t have degree 3 and o have degree 2, and suppose no edge of R contains {t,o}. If R contains no three-edge linear path ending physically at t and avoiding o, then o is adjacent in R to both of the other degree-three vertices.

## Body

Let C_1,C_2,C_3 be the three edges through t. By linearity their six off-t vertices are distinct. Thus V(R) consists of t, those six vertices, and exactly two nonneighbors o,r of t.

Since d_R(o)=2, exactly two of the four edges not through t contain o. Call the other two edges A,B. Any three-edge path ending at t while avoiding o must use A and B followed by one C_i: two distinct edges through t cannot both occur because they would meet nonconsecutively at t.

If A and B intersect, then absence of such a path implies that A and B meet exactly the same C_i's. Indeed, if B met C_i and A did not, then A,B,C_i would be a three-edge path ending at t; the reverse implication is symmetric. Each of A,B meets a given C_i in at most one vertex.

If A∩B is a t-neighbor, say a vertex of C_1, equality of their C_i-contact sets forces both A and B to meet all three C_i. A common contact set of size one is impossible because each edge needs two more vertices, and size two is impossible because the only vertex outside the six t-neighbors besides o is r, which cannot belong to both A and B. Hence the common contact set has size three, so neither A nor B contains r. Then the only remaining edges that could give r its required degree at least two are the two o-edges; both would have to contain r, repeating the pair {o,r}, contradiction. Therefore, if A and B intersect, their common vertex is r. In that case they meet exactly two of C_1,C_2,C_3, and on each of those two t-edges they use complementary off-t vertices.

It remains to read the degrees in the two possible cases.

First suppose A and B are disjoint. They cover six of the seven vertices consisting of the six t-neighbors and r. They must cover r, because otherwise r would again have to lie in both o-edges. Hence the unique vertex missed by A∪B is a t-neighbor s. The two o-edges have four distinct off-o vertices. They must include s, to raise d(s) from one to at least two, and r, to raise d(r) from one to at least two. Their other two off-o vertices are t-neighbors already used once by A∪B. Exactly those two vertices therefore receive degree three. Since t is already one degree-three vertex and the prescribed degree multiset has exactly three such vertices, these two are precisely the other degree-three vertices. Both are adjacent to o.

Now suppose A∩B={r}. As above, A and B use all four off-t vertices of two C_i's and avoid the third C_k. The two off-t vertices of C_k currently have degree one, so both must occur in the two o-edges. The remaining two off-o slots either consist of r and one vertex already used by A∪B, or of two vertices already used by A∪B. In the first case r and that latter vertex become the two additional degree-three vertices; in the second case the two latter vertices do. Again both degree-three vertices are adjacent to o.

Thus in every possible no-path configuration, o is adjacent in R to both degree-three vertices other than t.
