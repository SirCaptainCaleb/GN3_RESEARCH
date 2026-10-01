# Deletion-cover compatibility satisfies the exact Mantel density bound

## Statement

Let H be a boundary tournament with pc(H)>2, let D be any set of m>=7 deletion labels, choose one two-cover F_d of H-d for each d in D, and let G be their full pair-state compatibility graph. Then e(G)<=floor(m^2/4). Consequently at least binom(m,2)-floor(m^2/4) chosen pairs are incompatible, and some chosen deletion cover is incompatible with at least floor((m-1)/2) of the others.

## Body

# Proof

We use three certified inputs.

First, d1572b057d93 gives
e(G)<=floor(m^2/4)+1
for every m>=7.

Second, 47d4a615286a says that for every compatibility vertex v, the graph induced by its compatibility neighborhood N(v) is a linear forest: relative to the two displayed paths of F_v, every edge inside N(v) joins consecutive labels on one of those two orders.

Third, f7c79b595b2e gives the separator rule: if an edge ab has exactly two common compatibility neighbors c,d and c,d are incompatible, then every compatibility path from c to d meets {a,b}.

We first prove a graph lemma.

## Degree lemma

Let J be any graph on n>=8 vertices whose every vertex-neighborhood induces a linear forest. Then J has a vertex of degree at most floor(n/2).

Suppose instead that the minimum degree is delta>floor(n/2). Fix any vertex v, put A=N(v), d=|A|, and B=V(J)-(A union {v}), so |B|=n-1-d. Since J[A] is a linear forest,
e(A)<=d-1.
Let e(A,B) denote the number of cross edges. Summing the degrees of vertices in A gives
d delta <= d + 2e(A)+e(A,B),
hence
e(A,B)>=d(delta-3)+2.                 (1)
But trivially
e(A,B)<=d(n-1-d).                     (2)

If n=2k is even, then delta>=k+1 and d>=k+1, so n-1-d<=k-2 while delta-3>=k-2. Equations (1),(2) are incompatible because of the extra +2.

Now let n=2k+1. If d>=k+2, again n-1-d<=k-2 and delta-3>=k-2, contradicting (1),(2). Since v was arbitrary and delta>=k+1, every vertex has degree exactly k+1. Thus J is (k+1)-regular. For n>=9, parity immediately rules this out when k is even; so suppose k is odd, necessarily k>=5.

Fix v again. Now |A|=k+1, |B|=k-1. Let M be the number of missing A-B edges. Regularity gives
e(A,B)=(k+1)k-2e(A),
and therefore
M=(k+1)(k-1)-e(A,B)=2e(A)-(k+1)<=k-1.       (3)

Every edge of J has at most two common neighbors, because if xy is an edge then the common neighbors of x,y are precisely the neighbors of y inside J[N(x)], and that linear forest has maximum degree two.

If B is independent, regularity forces every b in B to be adjacent to all k+1 vertices of A. Then every edge xy of J[A], if one exists, has v together with all k-1 vertices of B as common neighbors. Such an edge must exist: from M=0 in (3), e(A)=(k+1)/2>0. This gives at least k>=5 common neighbors, contradiction.

Hence B contains an edge bc. Let m_b,m_c be the numbers of A-vertices missed by b,c. Since bc has at most two common neighbors,
(k+1)-m_b-m_c<=2,
so m_b+m_c>=k-1.
By (3), M<=k-1, hence equality holds throughout:
M=k-1 and m_b+m_c=k-1,
and all missing A-B edges are incident with b or c. Equation (3) gives e(A)=k. A linear forest on k+1 vertices with k edges is one path.

Every other vertex r in B-{b,c} is adjacent to all of A. Since r already has k+1 neighbors there and J is (k+1)-regular, r has no neighbor in B. Thus bc is the only B-edge incident with b or c. Regularity now gives
m_b=m_c=1,
so k-1=m_b+m_c=2, i.e. k=3, contradicting k>=5. The degree lemma follows.

## The seven-vertex base

We show that a seven-vertex compatibility graph cannot have 13 edges. The previous bound d1572b057d93 already gives e(G)<=13, so this is the only equality case to exclude.

Assume e(G)=13. Every neighborhood is a linear forest.

A vertex of degree six is impossible: deleting it leaves its six-vertex neighborhood, which has at most five edges, so the whole graph would have at most 6+5=11 edges. Hence Delta(G)<=5.

Suppose first that some vertex v has degree five. Let u be its unique nonneighbor and A=N(v), |A|=5. Since G[A] is a linear forest, e(A)<=4, while
13=5+e(A)+d_A(u).
Thus either
(e(A),d_A(u))=(3,5) or (4,4).

In the first case choose any edge ab of G[A]. In the second case G[A] is a five-vertex path; since u misses only one A-vertex, choose an edge ab of that path avoiding the missed vertex. In either case a,b are both adjacent to u, and u has a further neighbor c in A-{a,b}. Because G[A] is a forest, ab has no common neighbor inside A; and because every edge has at most two common neighbors, its common-neighbor pair is exactly {v,u}. Yet v and u are incompatible while
v-c-u
is a compatibility path avoiding a,b, contradicting the separator rule f7c79b595b2e.

Therefore Delta(G)<=4. Since the degree sum is 26, the degree sequence is
4,4,4,4,4,3,3.

Fix a degree-four vertex v, put A=N(v), |A|=4, and let B={r,s} be its two nonneighbors.

Suppose rs is an edge. Since
13=4+e(A)+e(A,B)+1
and
e(A,B)=d(r)+d(s)-2,
we have
e(A)=10-d(r)-d(s).
The pair d(r),d(s) cannot be (3,3), because then e(A)=4 although a four-vertex linear forest has at most three edges.

If the degrees are 4 and 3, then G[A] is a four-vertex path and the degree-four member b of B has three neighbors in A. Any three vertices of P4 contain an edge xy. The edge xy then has common neighbors v,b; the third A-neighbor c of b gives a path v-c-b avoiding x,y, contradicting the separator.

If both r,s have degree four, then e(A)=2 and each of r,s has three A-neighbors. If either three-set contains an A-edge, the same separator contradiction applies. Otherwise both are independent three-sets in the two-edge linear forest G[A]. The only two-edge linear forest on four vertices admitting an independent three-set is P3 plus an isolated vertex, and its independent three-set is unique. Hence r and s have the same three A-neighbors. Since rs is an edge, it then has at least three common neighbors, impossible.

Thus for every degree-four vertex v, its two nonneighbors are themselves nonadjacent.

Pass to the complement L of G. The five degree-four vertices of G have degree two in L, the two degree-three vertices have degree three, and L has eight edges. The preceding paragraph says that every degree-two vertex of L has adjacent neighbors, hence lies in a triangle.

Let p,q be the two degree-three vertices of L. They lie in the same connected component, since every component has an even number of odd-degree vertices. A shortest p-q path cannot have an internal degree-two vertex: that vertex's two path-neighbors would be adjacent, shortening the path. Hence pq is an edge.

A degree-two neighbor x of p that is not adjacent to q must have a second neighbor y adjacent to p, so x,y form a pendant triangle with p. If p had such a pendant triangle, its three incident edges would already be pq,px,py; the same degree accounting on q and the remaining degree-two vertices leaves one degree-two vertex with nowhere to lie in a triangle. Therefore p and q instead have two common degree-two neighbors. They induce the diamond K4 minus the edge between those two degree-two tips. The remaining three degree-two vertices form a separate triangle. Thus L is exactly a diamond disjoint union a triangle.

But then in G the two diamond tips are adjacent, and each is adjacent to all three vertices of the complementary triangle component. In the neighborhood of one tip, the other tip has degree at least three, contradicting that every compatibility neighborhood is a linear forest. This excludes e(G)=13.

Therefore every seven-vertex compatibility graph has at most 12=floor(49/4) edges.

## Induction

We now induct on m>=7. The base m=7 was just proved. For m>=8, the degree lemma gives a vertex v with
d(v)<=floor(m/2).
If e(G)>=floor(m^2/4)+1, then
e(G-v)>=floor(m^2/4)+1-floor(m/2)
       =floor((m-1)^2/4)+1.
The induced graph G-v is itself the compatibility graph of the corresponding subfamily of deletion covers, so the induction hypothesis applies and gives a contradiction.

Hence
e(G)<=floor(m^2/4)
for every m>=7.

The incompatible-pair count follows by subtraction. Averaging incompatible degrees gives a vertex with at least
ceil(2[binom(m,2)-floor(m^2/4)]/m)
=floor((m-1)/2)
incompatible partners.
