# One-slack critical cores have at most one forest joint

## Statement

Assume the extremal |D|=k color-complete critical-core normal form with one unit of slack,
m+2c=2k-1.
Let j=m-c be the number of forest joints. Then
j(k-2)<=k.
In particular, for k>=5 one has j<=1. Hence H-D consists of single-edge components, with at most one two-edge path component. More precisely 3c+j=2k-1 with j∈{0,1}.

## Body

Put r=m+2c=2k-1, the number of forest-degree-one vertices.

By 1663a127e081, for each color d∈D the d-colored matching has exactly k edges, all of them DXX. It saturates the 2k-1 private vertices and has exactly one remaining X-endpoint. Therefore exactly one d-colored edge has a forest-joint endpoint, and every other d-colored edge pairs two forest-private vertices.

Summing over all k colors, the total number of incidences
(d-colored edge, forest joint endpoint)
is exactly k.

On the other hand, by 6aa954fe903a every forest joint x has DXX color-graph degree at least k-2. Therefore the same total joint incidence count is at least
j(k-2).

Hence
j(k-2)<=k.

If k>=5, then 2(k-2)>k, so j cannot be at least two. Thus j<=1.

Since a path forest with m edges and c nonempty components has exactly
j=m-c
joint vertices, j=0 means every component has length one; j=1 means exactly one component has length two and all others have length one.

Finally
m+2c=(c+j)+2c=3c+j=2k-1,
which gives the displayed arithmetic normal form.
