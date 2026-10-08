# Three coherent deletion covers localize to one forced cyclic defect, with a double-gap repair — preserved pre-item development

## Theorem: three coherent ported deletions have one forced cyclic defect

Fix the flat ternary split and the representing tournament t, writing t(u,v)=1 when u→v and
α(u,v,w)=t(u,v)+t(v,w)+t(w,u) (mod 2).
Let A have at least four shore labels. Choose three distinct labels D={a,b,c}. For each d∈D, suppose A\{d} is covered by at most two disjoint fully ported zero paths. Assume the three covers agree pairwise, after restricting to A\{d,e}, both on same-path membership and on relative order within a common path.

Then A partitions into at most two classes. Each class has a total order with forward first and final pairs. One class, at most, may contain a consecutive block formed by the three deleted labels a,b,c on which α=1; every other consecutive triple in both classes has α=0. Consequently, if no such block exists, the two paths close the whole split by the adjacent-xz connector theorem.

In the exceptional case, the pair-comparison relation within the exceptional class has one directed 3-cycle, precisely D. Its three labels form a module for that relation: every other member precedes all three or succeeds all three. Cyclically rotating the block produces three near-zero ordered classes, each having the same unique 1-colored triple.

### Proof: gluing the supports

For u≠v, choose d∈D\{u,v} and define u~v when they occur in the same zero path of the d-cover. Pairwise consistency makes this independent of d. Any triple other than D lies in one of the deletion covers, giving transitivity. If a~b, b~c but a not~c, choose w∈A\D. In the b-cover, w is equivalent to a or c because this cover has at most two classes. If w~a, transitivity in the c-cover gives w~b, and in the a-cover gives w~c, contradicting a not~c in the b-cover. The alternative w~c is symmetric. Thus ~ is an equivalence relation. Three distinct classes would admit three representatives that must be D, since every other triple survives one deletion. An outside w would have to share a class with one of the three in two of the covers; equivalence then contradicts the third cover's two-class bound. Hence there are at most two global classes.

For each class, orient a pair u,v according to their relative order in any deletion witness containing both. The resulting comparison tournament is well-defined. Every three-set other than D survives some deletion, so is transitively ordered. If this tournament is transitive, its unique order restricts to all three zero-path witnesses. If it has a 3-cycle, that cycle must be D and lies in one class. Every external vertex of this class compares uniformly with D: otherwise a cyclic edge of D runs from a vertex preceded by the external vertex to one succeeding it, creating a second comparison triangle. Contracting D gives a transitive tournament, since any surviving cyclic triangle would differ from D. Thus D is a consecutive module, and we may expand it in one of its three cyclic orders, say a,b,c with a before b, b before c, and c before a in the comparison tournament.

After deleting c or deleting a, the expanded global class order agrees with the corresponding original witness order. Every consecutive triple outside (a,b,c), and every extreme ordered pair, avoids at least one of {a,c}. It therefore survives, in the same relative position, one of those two witnesses. All such triples have color 0 and both endpoint pairs are forward. The same is true of the other global class, if present.

If p is the immediate predecessor of the cyclic block, the three deletion witnesses give α(p,a,b)=α(p,b,c)=α(p,c,a)=0. The tournament coboundary identity
α(p,a,b)+α(p,b,c)+α(p,c,a)=1+α(a,b,c) (mod 2)
forces α(a,b,c)=1. If there is no predecessor, each of (a,b), (b,c), and (c,a) is the first, forward pair of one deletion path. Therefore t(a,b)=t(b,c)=t(c,a)=1 and again α(a,b,c)=1. Cyclic rotations leave α unchanged. This proves the normal form.

### Exact collar compatibility and a single-class closure

Suppose the exceptional block lies strictly inside its global class, with immediate predecessor p and successor q. For u∈D set e_u=t(p,u), f_u=t(u,q). The three zero left collars and three zero right collars yield, for the cyclic pairs (a,b),(b,c),(c,a),
t(u,v)=1+e_u+e_v=1+f_u+f_v (mod 2).
Hence e_u+f_u is independent of u∈D. In particular f=e or f=1−e coordinatewise.

Assume moreover the reconstructed partition has only ONE class. If D begins or ends that class, its two surviving-label edges are forward in every deletion witness; splitting the class inside D yields two fully ported zero paths, hence a spanning connector.

If p and q both exist, every incidence pattern except e_a=e_b=e_c=f_a=f_b=f_c=0 has one of two explicit repairs:

* A ported split: for a cyclic order (u,v,w), split the near-zero class as (L,u) and (v,w,R) when e_u=1 and t(v,w)=1; or as (L,u,v) and (w,R) when t(u,v)=1 and f_w=1. The two resulting classes are fully ported zero paths.
* A double-gap repair: for a cyclic order (u,v,w) with e_u=f_w=1 and t(u,v)=t(v,w)=0, replace L,u,v,w,R by L,u,z,v,x,w,R. The five changed consecutive triples at the two junctions are zero, using α(p,u,z)=0, α(u,z,v)=0, α(z,v,x)=0, α(v,x,w)=0, α(x,w,q)=0. The external endpoint ports are unchanged. This is a spanning compatible zero connector.

To verify exhaustiveness, if e has three or one entries equal to 1, the first split applies. If e has two 1s, the second split applies when the minority coordinate has f=1; otherwise f=e and the double-gap repair uses its two majority coordinates at the ends. If e has no 1s and f has three, the second split applies. The only remaining vector is e=f=(0,0,0).

Thus three coherent fully ported *single-path* deletion witnesses already close the NOR split unless their unique cyclic block is internal and has a uniform double-backward exterior collar, p←D←q. This exceptional collar, and the possible second reconstructed class in the general two-path theorem, are genuine remaining obligations. The result does not assume that support-exchange connectivity or a local repair automatically preserves an additional path's ports.
