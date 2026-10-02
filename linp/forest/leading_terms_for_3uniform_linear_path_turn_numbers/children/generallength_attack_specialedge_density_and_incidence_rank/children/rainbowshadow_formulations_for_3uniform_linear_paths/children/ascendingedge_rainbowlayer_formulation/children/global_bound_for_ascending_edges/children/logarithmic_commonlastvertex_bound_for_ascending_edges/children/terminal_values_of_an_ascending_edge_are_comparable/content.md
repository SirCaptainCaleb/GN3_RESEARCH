# Terminal φ-values of an ascending edge are comparable

## Statement

Let e={x,u,v} be an ascending nonspecial edge of a linear 3-graph, with unique entrance x and q=φ(e). Then |φ(u)-φ(v)|<=q-1. In particular max{φ(u),φ(v)}<2 min{φ(u),φ(v)}.

## Body

Since u and v are snake vertices of e, φ(u),φ(v)>=q. Assume φ(u)>=φ(v) and put p=φ(u). If p<=2q-2, then p-φ(v)<=2q-2-q=q-2. Now suppose p>=2q-1. Choose an edge f and a longest p-edge path P ending with f and last vertex u, so φ(f,u)=φ(f)=p. Apply the rank-gap blocker lemma to the ascending edge e at the common last vertex u. Because p>=2q-1, the required intersection of e with the final q-2 precursor edges of P cannot occur at x; it occurs at v. Hence v lies in some precursor edge of index at least p-q+2. If v is the intersection with the preceding edge, the prefix through that preceding edge has length at least p-q+1 and can be ordered with last vertex v; otherwise the prefix through the current edge is at least as long. Thus φ(v)>=p-q+1, so p-φ(v)<=q-1. This proves the difference bound. Since min{φ(u),φ(v)}>=q, the ratio bound follows.