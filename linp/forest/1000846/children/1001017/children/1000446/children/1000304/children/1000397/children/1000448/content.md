# High-rank competitor captures all vertices of a lower ascending edge

## Statement

Let e={x,v,y} be an ascending nonspecial edge of rank q, with unique entrance x and terminals v,y. Let f be a snake-incoming edge at v of rank p>=2q-1, and let P be any longest p-edge path ending in f at v. Then P contains both x and y in its precursor before f; together with v in f, the path P meets all three vertices of e.

## Body

By the rank-gap blocker lemma, because p>=2q-1 the required intersection of e with the final q-2 precursor edges of P cannot occur at x, so it occurs at y. From the occurrence of y on P there is a prefix R of P ending at y of length at least p-q+1>=q: if y lies internally in the earliest allowed tail edge, use the prefix through that edge; if y is the entrance of that edge from its predecessor, use the prefix through the predecessor, still of length at least p-q+1. Take the final q-1 edges of R, obtaining a (q-1)-edge linear path S ending at y. The terminal vertex v of P occurs only in the final edge f, hence v is not in S. If x were also absent from S, then S could be followed by e through y, producing a q-edge linear path ending in e and entering e through y. Since phi(e)=q and e is nonspecial with unique entrance x, this would make e special, a contradiction. Therefore x lies in S. Thus x and y both lie in the precursor of P, while v lies in f. In particular every high-rank competitor path captures all three vertices of the lower ascending edge.
