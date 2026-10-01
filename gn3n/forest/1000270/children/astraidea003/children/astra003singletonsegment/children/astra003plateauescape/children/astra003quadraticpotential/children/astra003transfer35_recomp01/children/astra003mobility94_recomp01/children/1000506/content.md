# Ten active vertices force at least one hundred four three-side supports

## Statement

Let D be a family of three-subsets satisfying the coordinate-wise Astra exchange property: for every X in D and x in X, at least six y outside X have X-{x}+{y} in D. If the two-shadow of D uses exactly ten vertices, then it is either K_10 or K_10 minus one edge. In the first case |D|>=107; in the second |D|>=104. Hence any trapped order-thirteen 3|5|5 Astra-003 component whose three-side shadow uses ten vertices has at least 104 distinct three-side supports.

## Body

# The ten-vertex shadow is almost complete

Let W be the ten vertices appearing in the two-shadow G of D. As before, every shadow edge uv has codegree d_D(uv)>=7, and every vertex of G has degree at least eight. Hence the complement of G in K_10 has maximum degree at most one: its edges form a matching.

There cannot be two missing shadow edges uv and ab. They would be disjoint. Then ua is a shadow edge, but any triple of D containing ua can use neither v nor b as its third vertex. Among the eight possible third vertices in W-{u,a}, at most six remain, contradicting d_D(ua)>=7. Therefore G is either K_10 or K_10 minus one edge.

## Complete shadow

Suppose G=K_10. For every pair uv there are eight possible third vertices, while d_D(uv)>=7. Thus each pair is contained in at most one missing triple. Equivalently, the complement C(W,3)-D is a linear three-uniform hypergraph.

In a linear triple system on ten vertices, the missing triples through a fixed vertex use disjoint pairs among the other nine vertices, so every vertex lies in at most floor(9/2)=4 missing triples. If q triples are missing, then

3q <= 10*4=40,

so q<=13. Therefore

|D| >= C(10,3)-13 = 107.

## One missing shadow edge

Now suppose uv is the unique missing shadow edge. Then all eight triples containing uv are absent.

Take w outside {u,v}. The pair uw is a shadow edge. A D-triple containing uw cannot have v as third vertex because uv is missing. There are exactly seven other possible third vertices, and d_D(uw)>=7, so all seven occur. Thus every triple containing u but not v is present. The same holds with u,v interchanged.

Let R=W-{u,v}, so |R|=8. For a pair ab in R, the triples abu and abv are both present. Since d_D(ab)>=7, among the six possible third vertices in R-{a,b} at most one can give a missing triple. Hence the missing triples contained entirely in R form a linear triple system.

In a linear triple system on eight vertices, each vertex lies in at most floor(7/2)=3 triples. Thus if q_R triples of R are missing,

3q_R <= 8*3=24,

so q_R<=8.

The only missing triples are the eight containing uv and these at most eight triples inside R. Hence at most sixteen of the C(10,3)=120 triples are absent, and

|D|>=104.

Therefore ten active shadow vertices already force at least 104 reachable three-side supports.
