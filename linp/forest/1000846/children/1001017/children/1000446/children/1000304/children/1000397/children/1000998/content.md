# Rank-gap forces the terminal blocker for ascending edges

## Statement

Let e={x,v,y} be an ascending nonspecial edge of rank q, with unique entrance x, so a(x)=q-1 and v,y are terminal vertices. Let f be a snake-incoming edge at v of rank p>=q-1. For any longest path ending in f at v, the terminal tail-blocker lemma forces e to meet the final q-2 precursor edges. If p>=2q-1, that forced intersection cannot occur at x; hence it must occur at y.

## Body

By the terminal tail-blocker lemma, e meets one of the q-2 precursor edges immediately before f in every longest p-edge path P ending in f at v. Suppose one such forced intersection occurs at x. The earliest of those q-2 precursor edges has index p-q+2 in P. If x lies in that edge but is its entrance from the preceding edge, then the prefix through the preceding edge has length p-q+1 and can end at x; otherwise the prefix through the current edge is even longer and can end at x. Thus in all cases a(x)>=p-q+1. Since e is ascending, a(x)=q-1, so p-q+1<=q-1, i.e. p<=2q-2. Therefore if p>=2q-1, x cannot serve as the required blocker. As e meets P through one of e\{v}={x,y}, the blocker must be y. This gives a useful dichotomy: competitors of an ascending rank-q edge are either of rank at most 2q-2 or, when higher, are all forced through its other terminal vertex.