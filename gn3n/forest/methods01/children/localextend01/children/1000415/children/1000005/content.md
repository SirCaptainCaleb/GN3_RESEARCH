# Parallel middles contain a linear complete alternating fan

## Statement

Let H be a boundary tournament, let a,b be distinct vertices, and let W be a set of n>=5 vertices disjoint from {a,b}. Suppose (a,w,b) is tight for every w in W. Put t=floor((n+1)/4). Then there exist x in W and subsets Y,Z of W-{x} with |Y|>=t and |Z|>=t such that for every y in Y and z in Z with y!=z, (y,a,x,b,z) is a tight path. In particular there are at least t(t-1) ordered endpoint pairs (y,z) producing this same controlled five-path pattern through the fixed center x and anchors a,b.

## Body

Define two ordinary tournaments A and B on W by y ->_A x iff (y,a,x) is tight, and x ->_B z iff (x,b,z) is tight. For an integer t>=1, in any tournament the set of vertices of indegree < t has order at most 2t-1: if S is that set, then the induced tournament on S has |S|(|S|-1)/2 edges, while the sum over S of full indegrees is < t|S|, so |S|(|S|-1)/2 < t|S| and hence |S|<=2t-1. The same bound holds for the set of vertices of outdegree < t.

Take t=floor((n+1)/4). Then 4t-2<n. Therefore the union of the vertices with A-indegree < t and the vertices with B-outdegree < t has order at most 4t-2<n. Choose x outside this union. Let Y=N_A^-(x) and Z=N_B^+(x). Then |Y|,|Z|>=t.

For y in Y and z in Z with y!=z, the definitions give (y,a,x) and (x,b,z) tight, while the hypothesis gives (a,x,b) tight. These are exactly the three consecutive triples of (y,a,x,b,z), so it is a tight path. Among the |Y||Z| ordered pairs, only pairs with y=z are excluded; there are at most min{|Y|,|Z|} such pairs. Hence there are at least |Y||Z|-min{|Y|,|Z|}>=t(t-1) valid ordered pairs.
