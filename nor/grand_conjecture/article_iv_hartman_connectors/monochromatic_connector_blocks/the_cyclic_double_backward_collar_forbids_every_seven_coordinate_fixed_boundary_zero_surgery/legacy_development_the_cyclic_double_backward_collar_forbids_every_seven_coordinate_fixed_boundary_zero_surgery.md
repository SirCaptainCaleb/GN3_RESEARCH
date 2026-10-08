# The cyclic double-backward collar forbids every seven-coordinate fixed-boundary zero surgery — preserved pre-item development

## Fixed-collar obstruction at the coherent triple

Consider the normalized flat switching tournament on the seven labels
{p,q,a,b,c,x,z}. Assume that z dominates all five shore labels, all five shore labels dominate x, z→x, that a→b→c→a is a directed triangle, and that each of a,b,c dominates p while q dominates each of a,b,c. The edge p↔q is unrestricted.

THEOREM. No permutation
(p, w_1,w_2,w_3,w_4,w_5, q), {w_1,...,w_5}={a,b,c,x,z},
has every consecutive ternary color α=0. In particular, the residual double-backward collar of the three-deletion cyclic packet cannot be repaired by a permutation supported on {a,b,c,x,z} that keeps p and q as the two boundary vertices.

PROOF. Work with α(u,v,w)=t(u,v)+t(v,w)+t(w,u) modulo 2, where t(u,v)=1 iff u→v. For the directed triangle T={a,b,c}, any order (u,v,w) of T has t(u,v)=t(v,w)=ε. Its triple color is α(u,v,w)=1−ε: the cyclic direction has ε=1, α=1, and its reverse has ε=0, α=0.

The following identities hold whenever u,v∈T:
α(p,u,x)=α(p,u,z)=1;
α(z,u,q)=α(x,u,q)=1;
α(x,u,z)=α(u,z,x)=α(z,x,u)=1;
α(p,z,u)=α(p,x,u)=0;
α(u,x,q)=α(u,z,q)=0;
α(z,u,v)=α(x,u,v)=α(u,v,x)=α(u,v,z)=1−t(u,v);
α(u,x,v)=α(u,z,v)=t(u,v);
α(z,u,x)=0.
They follow immediately from the displayed dominance relations and are independent of t(p,q).

If x and z are adjacent, their order must be x,z: a neighboring shore vertex gives color 1 for either orientation z,x. For the order x,z, splitting the three T labels to its two sides gives four possibilities. One T label on its left forces the forbidden prefix p,u,x; one on its right forces the forbidden suffix z,u,q. Thus only all three T labels on one side remain. In either case the two neighboring T edges must be forward for their crossing triples to be zero; then the internal triple of T has color 1. Hence adjacent specials are impossible.

If x and z are separated and x occurs first, write the internal sequence as T^i,x,T^j,z,T^k with i+j+k=3 and j≥1 (each power denotes some order of distinct T labels). For j=1 the middle triple x,u,z has color 1. For j=2, the remaining T label lies either before x or after z; the former produces p,u,x and the latter z,u,q, each color 1. For j=3, the required zero of x,u,v forces t(u,v)=1, while the zero of the internal T triple forces t(u,v)=0. Thus this order is impossible.

It remains to consider z occurring before x, with sequence T^i,z,T^j,x,T^k and i+j+k=3, j≥1. If j=3, the zero of z,u,v requires t(u,v)=1, contradicting the zero of the internal T triple. If j=2, the single remaining T coordinate before z produces p,u,z of color 1; if it follows x, the zero of z,u,v requires t(u,v)=1 while the zero of v,x,w requires t(v,w)=0, contradicting equality of consecutive T-edge orientations. Finally, if j=1: i=k=1 produces p,u,z of color 1; (i,k)=(0,2) requires t(u,v)=0 from u,x,v and t(v,w)=1 from x,v,w; (i,k)=(2,0) requires t(u,v)=1 from p,u,v and t(v,w)=0 from v,z,w. Both contradict the same equality. Every permutation is excluded. QED.

INTERPRETATION. This is an impossibility theorem for a specified local *relative* surgery. It is consistent with universal seven-coordinate connector existence, because a connector may move p or q, change both exterior collars, or use further shore support. Consequently, a proof based on three-deletion coherent packets must handle the double-backward state with a genuinely nonlocal exchange or boundary release. The seven-vertex test is algebraic, not a small-order cutoff for the grand conjecture.
