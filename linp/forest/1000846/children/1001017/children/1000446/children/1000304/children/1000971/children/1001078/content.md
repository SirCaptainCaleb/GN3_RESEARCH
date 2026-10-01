# Entrance-value distortion with consecutive-contact correction

## Statement

Let f be a nonspecial edge with φ(f)=q and unique entrance x. Let P be a path of length φ(x) with last vertex x. If r vertices of f occur on P, then φ(x)<=r(q-1)<=3(q-1). If f is not ascending, then r>=2; if φ(x)>2(q-1), then r=3.

## Body

For each u∈f, the set of edges of P containing u is an interval of size at most two, since nonconsecutive path edges are disjoint. The block containing x consists only of the last edge of P. Order the nonempty vertex blocks of f along P. For each block before the last, the path segment from the end of the preceding block to the first edge of the current block, followed by f, ends with f and enters f through a snake vertex; therefore its length is at most q-1. The final analogous segment enters f through x and has length at most q. Accounting for the possible one-edge overlap inside each earlier block shows that each block contributes at most q-1 edges of P. Hence φ(x)<=r(q-1). If f is not ascending then φ(x)>=q, so r≠1. If φ(x)>2(q-1), then r=3.