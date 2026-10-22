# Coupled reachability cuts and two-endpoint path-set squares

- Stable ID: note_nori_coupled_reachability_cuts_endpoint_squares_r12002_5
- Author: session_nori_r12002_5
- Primary home: subsection:boolean_reachability_posets_and_complementary_geodesic_gluing
- Labels: NORI1, reachability, topology, endpoint-extension
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12002_5
- Updated session: session_nori_r12002_5
- Disposition: none
- Successor: none

## Related references

- subsection:monochromatic_geodesic_endpoint_posets_and_a_global_rank_bounded_target

## Research note

Let c be an arbitrary binary coloring of Q_n, with red color 0. Let D(u,v)={k:u_k differs from v_k}, and let P(u,v) be the finite set of red geodesics from u to v, including the empty path when u=v. Put r(u,v)=1_{P(u,v) nonempty} and N(u,v)=|P(u,v)|. All paths retain their vertex sequences and traverse each direction at most once.

## Reachability cuts and reversal

For root x, put r_x(S)=r(x,x xor 1_S). Path reversal gives r(u,v)=r(v,u), hence r_x(S)=r_{x xor 1_S}(S). If i is outside D(u,v), a terminal extension has crossing value r(u,v^i)-r(u,v). Reversal changes it to r(v^i,u)-r(v,u), the crossing value of the corresponding initial extension. These values are equal. Thus reversal preserves exit and entry signs; it does not directly pair an exit with an entry.

For a red terminal edge vv^i, concatenation gives r(u,v)<=r(u,v^i). For a red initial edge uu^i, it gives r(u,v)<=r(u^i,v). Consequently an exit from rooted red reachability along an increasing Boolean edge crosses a blue original edge. Along a full Boolean chain under absence of a red antipodal geodesic, the sum of crossing values is -1. Re-entries prevent this telescoping identity alone from becoming a positive count of exits.

If c is antipodally odd and has no monochromatic full antipodal geodesic, then r_x(S)r_x(S^c)=0 for every x,S: reverse a red arm with support S and concatenate a red arm with support S^c to obtain a red full geodesic. Also r(u,v)=0 for d(u,v)>=n-1. For length n-1, the two unused-direction endpoint edges are antipodal, so one extends the path in red. These are global restrictions to retain alongside the local identities below.

## Two endpoint extensions

Fix u,v, put S=D(u,v), and choose distinct i,j outside S. Assume the two original edges uu^i and vv^j are red. Consider the four path sets
P_00=P(u,v), P_10=P(u^i,v), P_01=P(u,v^j), P_11=P(u^i,v^j).
Their direction sets are S, S union {i}, S union {j}, S union {i,j}, respectively.

There are canonical injections P_10 -> P_11 by appending vv^j and P_01 -> P_11 by prepending u^i u. Their images consist, respectively, of top paths whose last direction is j and whose first direction is i. Their intersection consists of paths beginning with i and ending with j; removing those two edges identifies this intersection with P_00. The two injections from P_00 commute.

It follows that
N(u^i,v^j)-N(u^i,v)-N(u,v^j)+N(u,v)
= #{P in P_11 : first direction is not i and last direction is not j} >= 0.
This is a set-theoretic inclusion-exclusion identity with individual path provenance. It uses no antipodal assumption. The positivity does not by itself yield nonvanishing of a full-rank path set.

The Boolean second difference
Delta r = r(u^i,v^j)-r(u^i,v)-r(u,v^j)+r(u,v)
belongs to {-1,0,1}, by the red-extension inclusions. Its nonzero cases are:
Delta r=1 iff only P_11 is nonempty;
Delta r=-1 iff P_10,P_01,P_11 are nonempty and P_00 is empty.
Here 'only' refers to the four path sets. These assertions follow by listing the upward-closed zero/one patterns of this square.

## Disjointness in the negative Boolean case

More generally, if P_00 is empty, every path in P_10 is vertex-disjoint from every path in P_01.

Proof. Suppose paths L:u^i -> v and R:u -> v^j share a vertex z. The whole path L has bit j equal to u_j, and the whole path R has bit i equal to u_i. Hence z lies in the face interval [u,v]. The prefix of R from u to z uses the dimensions where u and z differ, all in S. The suffix of L from z to v uses the complementary dimensions of S. Concatenating these two red paths gives a red geodesic from u to v, contrary to P_00 being empty.

In the positive Boolean case, every top path avoids the prescribed first-i and last-j positions. A witness with i preceding j has at least one S-direction before i and at least one S-direction after j. A witness with j preceding i can pass through the opposite i,j layer. Both orders must remain available in any further argument.

## Continuation question

The reachability indicators discard the intersection information in the commuting square of path sets. The nonnegative path-count identity restores that information at the level of individual witnesses. A potential relative-chain construction should retain these prefix/suffix embeddings and their intersection P_00, together with endpoint reversal and antipodal color exchange. Its unresolved obligation is a nonvanishing or obstruction statement that forces a full direction set. No relative homology class, global cancellation theorem, or NORI1 proof is established here.

Endpoint reversal alone preserves crossing signs. Ordinary scalar telescoping and unweighted path counting therefore leave the main forcing problem open. The next investigation is whether compatible exchange cells among the retained paths supply a global relative obstruction while respecting the common original coloring.

## A relative complex retaining the endpoint inclusions

For each ordered pair u,v with S=D(u,v), let K(u,v) be the following finite polyhedral subcomplex of the permutahedron on S. Its vertices are the red geodesic orders in P(u,v). Include a permutahedral face precisely when all its vertex orders give red geodesics. This defines a subcomplex because every subface has a subset of those vertices. Use a point for S empty. The empty path set gives the empty complex. An edge is an adjacent transposition for which both resulting paths are red. Higher faces retain the corresponding compatible order exchanges.

Under the red-edge assumptions above, prepending i embeds K(u,v^j) as the intersection of K(u^i,v^j) with the permutahedral facet having first direction i; appending j similarly embeds K(u^i,v) in the facet having last direction j. For the two-dimensional-support case these facets are vertices. Their intersection is the embedded K(u,v), because imposing both endpoint positions leaves precisely the red orders on S. These assertions hold face by face, by removing the fixed red endpoint edges.

Writing K_ab for the four complexes and B for the union of the two embedded lower complexes, one therefore has
B = K_10 union K_01, K_10 intersect K_01 = K_00.
The relative cellular zero-chain group C_0(K_11,B) has dimension
N_11-N_10-N_01+N_00,
the nonnegative quantity above. Its higher boundary maps record the red-preserving exchanges. Consequently this positive zero-chain dimension alone implies no homology nonvanishing.

There is a precise relative-homology interpretation of a negative Boolean square. If K_00 is empty and a path component of K_11 meets both K_10 and K_01, choose vertices a,b in those two intersections and an edge path gamma between them in K_11. Then gamma is a relative one-cycle in (K_11,B), and its connecting image in H_0(B;F_2) is [a]+[b], which is nonzero because the two lower subcomplexes are disjoint. Thus its relative H_1 class is nonzero. The relative homology sequence expresses this as a kernel element of H_0(B)->H_0(K_11). Existence of the required component has not been proved in general.

Endpoint reversal reverses all dimension orders and exchanges prefix and suffix inclusions. Antipodality sends the red complexes to the blue complexes with complemented endpoints. Both operations preserve the facewise constructions. The unresolved global step is to use these symmetries and the simultaneous no-full-path restrictions to force an incompatible relative class or a full-rank witness. The complexes by themselves provide no such theorem.
