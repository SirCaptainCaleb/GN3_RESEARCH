# Maximum-path characterization of ascending and nonascending edges

## Statement

Let f={x,y,z} be a nonspecial edge with unique entrance x and q=φ(f). Then f is ascending if and only if there exists a path of length φ(x) with last vertex x that contains neither y nor z. If f is nonascending, every path of length φ(x) with last vertex x contains at least one of y,z. If moreover φ(x)>2(q-1), then every such path contains both y and z.

## Body

Because f is nonspecial with unique entrance x, a longest q-edge path ending with f enters f through x. Deleting f gives a (q-1)-edge path with last vertex x and avoiding y,z, so φ(x)>=q-1. If f is ascending, φ(x)=q-1 and this deleted path is a longest path ending at x, proving the forward implication. Conversely, suppose some path P of length φ(x) with last vertex x avoids y,z. Then P followed by f is a linear path of length φ(x)+1 ending with f, so q>=φ(x)+1. Together with φ(x)>=q-1 this gives φ(x)=q-1, hence f is ascending. Therefore if f is nonascending, no longest path ending at x can avoid both y and z, so every such path contains at least one of them. Finally, if φ(x)>2(q-1), apply the consecutive-contact distortion lemma to any longest path ending at x. That lemma forces all three vertices of f to occur on the path; since x is its last vertex, both y and z occur earlier.
