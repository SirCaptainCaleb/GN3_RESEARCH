# Compatibility density is within two edges of the bipartite bound

## Statement

Let H be a boundary tournament with pc(H)>2, let D be a set of m>=7 deletion labels, and choose one deletion cover F_d of H-d for each d in D. Let G be the compatibility graph on D. Then e(G) <= floor(m^2/4)+2. Consequently at least binom(m,2)-floor(m^2/4)-2 pairs of chosen deletion covers are incompatible, and some chosen cover is incompatible with at least ceil(2(binomial(m,2)-floor(m^2/4)-2)/m) others.

## Body

# Compatibility density is within two edges of the bipartite bound

Let G be the compatibility graph of chosen deletion covers. We use only the certified conclusions of compatdensity01:

1. every edge of G lies in at most two triangles;
2. every triangle of G contains an edge lying in no other triangle.

The second assertion follows because a cyclic-precedence triangle has all three edges triangle-isolated, while a transitive-precedence triangle has its source-sink edge triangle-isolated.

We first prove an abstract graph lemma.

## Lemma

Let G be a graph on m>=7 vertices such that every edge lies in at most two triangles and every triangle contains an edge lying in no other triangle. Then

e(G) <= floor(m^2/4)+2.

### High-minimum-degree cores of order at least eight are impossible

Suppose k>=8 and a k-vertex graph J has the two stated triangle properties and minimum degree

delta(J) > floor(k/2).

Then e(J)>floor(k^2/4), so Mantel's theorem gives a triangle abc.

For an edge xy write t(xy)=|N(x) intersect N(y)|. For the triangle abc,

t(ab)+t(bc)+t(ca) >= d(a)+d(b)+d(c)-k.

Indeed, for each vertex v let r(v) be the number of its neighbors among {a,b,c}. Its contribution to the left side is binom(r(v),2), and binom(r,2)>=r-1 whenever r>=1. Summing and using that at most k vertices have r(v)>=1 gives the displayed inequality.

On the other hand, each of the three edge codegrees is at most two, and at least one is at most one because every triangle has an edge lying in no other triangle. Hence

t(ab)+t(bc)+t(ca) <= 5.

But delta(J)>floor(k/2) gives

d(a)+d(b)+d(c)-k >= 3(floor(k/2)+1)-k.

For even k>=8 this lower bound is k/2+3>=7; for odd k>=9 it is (k+3)/2>=6. In either case it exceeds 5, contradiction.

Thus every graph with the two triangle properties and order k>=8 has a vertex of degree at most floor(k/2).

### The seven-vertex base

Let J have seven vertices. We claim e(J)<=14.

Assume for contradiction that e(J)>=15, and choose a vertex v of maximum degree Delta. Since the average degree is greater than four, Delta>=5.

If Delta=6, then v is adjacent to every other vertex. For each neighbor x of v,

t(vx)=d(x)-1,

because every neighbor of x other than v is also adjacent to v. Since every edge has codegree at most two, d(x)<=3 for all six neighbors x. Hence

2e(J)=d(v)+sum_{x in N(v)}d(x) <= 6+6*3=24,

so e(J)<=12, contradiction.

Therefore Delta=5. Let u be the unique nonneighbor of v, and let S=N(v), so |S|=5. Put s=|N(u) intersect S|=d(u).

For x in S, every neighbor of x inside S is a common neighbor of v and x. Hence d_S(x)<=2. Also x may be adjacent to u, so

d(x)<=3+1_{xu}.

Summing degrees gives

2e(J) <= 5+s + 4s + 3(5-s)=20+2s.

If s<=4, then e(J)<=14, contradiction. Hence s=5: u is adjacent to every vertex of S.

Now J contains all ten edges between {u,v} and S. Since e(J)>=15, the induced graph J[S] has at least five edges. But every vertex of J[S] has degree at most two, so e(J[S])<=5. Therefore e(J[S])=5 and J[S] is a 2-regular graph on five vertices, hence a 5-cycle.

Take any edge xy of this 5-cycle. The edge vx lies in exactly the two triangles vxy and vxz, where y,z are the two cycle-neighbors of x; similarly every edge ux lies in exactly two triangles. The cycle edge xy lies in the two triangles vxy and uxy. Thus every edge of the triangle vxy lies in two triangles, contradicting the hypothesis that every triangle contains an edge lying in no other triangle.

Hence e(J)<=14.

### Induction

We now induct on m>=7. The case m=7 is proved.

For m>=8, choose a vertex v with d(v)<=floor(m/2), whose existence was proved above. The induced graph G-v inherits both triangle properties, so by induction

e(G-v) <= floor((m-1)^2/4)+2.

Therefore

e(G) <= floor((m-1)^2/4)+2+floor(m/2)
     = floor(m^2/4)+2,

using the standard recurrence for the balanced complete bipartite edge count.

This proves the abstract lemma and hence the compatibility-graph bound.

Finally the number of incompatible pairs is binom(m,2)-e(G), giving

binom(m,2)-floor(m^2/4)-2

as a lower bound. Averaging incompatible degrees gives a vertex with at least

ceil(2(binomial(m,2)-floor(m^2/4)-2)/m)

incompatible partners.

The argument is arbitrary-order and uses only compatibility-triangle geometry; no finite boundary-tournament classification or computation is involved.