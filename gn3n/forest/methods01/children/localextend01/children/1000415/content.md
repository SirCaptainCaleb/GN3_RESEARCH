# Five parallel middle vertices force an explicitly alternating five-path

## Statement

Let H be a boundary tournament, let a,b be distinct vertices, and let W be a set of at least five vertices disjoint from {a,b}. Suppose (a,w,b) is tight for every w in W. Then there exist distinct y,x,z in W such that (y,a,x,b,z) is a tight path.

## Body

Define two ordinary tournaments A and B on W by y→_A x exactly when (y,a,x) is tight, and x→_B z exactly when (x,b,z) is tight. Suppose for contradiction that there are no distinct y,x,z with y→_A x and x→_B z. If a vertex x has indegree at least two in A, then x must have outdegree zero in B: otherwise choose a B-out-neighbor z of x and then choose an A-in-neighbor y of x distinct from z. Thus every vertex of A with indegree at least two is a sink of B. A tournament has at most one sink, so A has at most one vertex of indegree at least two. But if |W|=n>=5, this is impossible, since then the total indegree of A would be at most (n-1)+(n-1)=2n-2, while every n-vertex tournament has total indegree n(n-1)/2>2n-2. Therefore distinct y,x,z exist with (y,a,x) and (x,b,z) tight. By hypothesis (a,x,b) is tight. These are exactly the three consecutive triples of (y,a,x,b,z), so that sequence is a tight path.
