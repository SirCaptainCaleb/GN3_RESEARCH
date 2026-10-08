# NORI exact two-window connector criterion and false bare-vertex transfer

# Exact two-window splice criterion for NORI ordered-three-face colors

Let n>=6. Let P be a geodesic from x to z of length a>=3, and Q a geodesic from z to bar x of length b>=3, with a+b=n, so their coordinate supports are disjoint and complementary. Orient the concatenation H=P*Q from x to bar x. Assume every ordered-three-face window wholly inside P has color q and every one wholly inside Q has color r, where q,r are in {0,1}. Write the final two directions of P as (s,t) and the first two directions of Q as (u,v). Define the two actual ordered-three-face seam colors
A=c(F_H(s,t,u),(s,t,u)),
B=c(F_H(t,u,v),(t,u,v)).
Here each face F_H is the unique three-dimensional face traversed by the corresponding consecutive three edges; its exterior assignment is inherited from H.

**Theorem (exact splice extraction).** H has at most one ordered-three-face color change if and only if
(i) q=r and (A,B)=(q,q); or
(ii) q!=r and (A,B) belongs to {(q,q),(q,r),(r,r)}.
In particular, if q!=r the sole forbidden seam pair is (r,q), whereas if q=r both seam colors must equal q.

*Proof.* The full length-(n-2) color word of H is exactly
q repeated (a-2) times, followed by A,B, followed by r repeated (b-2) times.
All three displayed blocks have their claimed lengths because a,b>=3. If q=r, the binary word begins and ends in q. A word with at most one change and equal endpoint colors must be constant; hence A=B=q. If q!=r, a binary word with one change from q to r must be nondecreasing in the two-color order q<r, so its two intervening seam entries are qq,qr,or rr, with rq excluded. This establishes necessity and sufficiency.

**Independent counterexample to naive common-vertex extraction.** For n=6 take H from 000000 in direction order 1,2,3,4,5,6 and split after direction 3. Assign the colors of its ordered windows (1,2,3),(2,3,4),(3,4,5),(4,5,6) to 0,1,0,1 respectively, with the appropriate traversed exterior bits. These are four distinct ordered-face objects, none paired to another by face-antipodality plus reversal. Consequently the partial assignment extends to a valid antipodal-reversal-odd coloring of all ordered three-faces. The first three-edge leg is monochromatic 0, and the last three-edge leg is monochromatic 1, yet their concatenation has color word 0101 (three changes). Thus the edge-case implication 'two monochromatic antipodal-origin geodesic branches meeting at a vertex guarantee a one-change full geodesic' DOES NOT hold for ordered-three-face NORI without a two-window seam certificate. No assertion is made that this coloring defeats the full NORI grand conjecture, or that alternative choices of connector paths fail.

**Topology-ready extraction target.** A root-coupled reachability label for NORI must record enough memory to identify the last two directions of the first leg, the first two of the second leg, their monochromatic window colors, and the two bridge-face exterior assignments. When a topological coincidence yields disjoint complementary supports together with one of the allowed seam pairs, a full one-change antipodal geodesic follows immediately. A coincidence in bare reachable vertex names or bare complementary supports has no such implication. For legs of length 0,1,2 the analogous certification uses the actual concatenated windows directly (since a purported pure window block may be empty).
