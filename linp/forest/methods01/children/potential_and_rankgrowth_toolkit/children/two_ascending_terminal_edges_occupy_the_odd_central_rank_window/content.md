# At most two ascending terminal edges occupy the odd central rank window

## Statement

Let q≥3 be an integer, H a finite linear 3-graph, and v a vertex with φ(v)≥2q-3. Then at most two ascending nonspecial edges e containing v have v terminal at e and φ(e)≤q. No comparison with their opposite terminal vertex ranks is required. More precisely the respective upper bounds are 2, 1, and 0 when φ(v)=2q-3, φ(v)=2q-2, and φ(v)≥2q-1. In particular, if φ(v)=5, at most two rank-four ascending edges are terminal at v, even without potential charging.

## Body

The certified terminal-rank inequality a7b7670e955a says that an ascending nonspecial edge of rank s terminal at v satisfies φ(v)≤2s-2. Thus under φ(v)≥2q-3, every edge counted in the statement has rank exactly q, and none exists if φ(v)≥2q-1.

We first prove the bound two, using only a path P=(g_1,...,g_r) of length r=2q-3 ending at v. Such a path exists by truncating a longer v-ending path at its beginning.

For each counted edge e={x,v,u}, x is its unique entrance and φ(x)=q-1. Choose a witness on P: choose x when x∈V(P), and otherwise choose u. We justify existence and locate the witness.

If x is private to g_j, the two path segments ending at x give φ(x)≥max{j,r-j+1}. Therefore j=q-1. If x is the joint g_j∩g_{j+1}, they give φ(x)≥max{j,r-j}, so j∈{q-2,q-1}. These are exactly the private vertex and two joints of g_{q-1}.

If x is absent, e cannot be the last edge of P. Indeed r≥q; if e is last then r=q and nonspeciality requires x on the penultimate edge. The certified terminal-tail lemma b5ba2ebc7a66 now places u in g_{r-q+2}∪...∪g_{r-1}. Let j be the first path-edge index containing u. The prefix (g_1,...,g_j,e) is a linear path entering e through u: x is absent, and v occurs only in g_r, later than j. Since u is not the unique entrance and e has rank q, this path has at most q-1 edges. Thus j≤q-2. If u were private, tail membership would give j≥r-q+2=q-1, impossible. If u is a joint, tail membership gives j≥r-q+1=q-2. Therefore u must be a=g_{q-2}∩g_{q-1}.

Consequently all witnesses belong to the three vertices of g_{q-1}, and only its left joint a may be a terminal witness. Distinct edges through v have disjoint pairs {x,u}, by linearity, so their witnesses are distinct.

If three counted edges existed, their witnesses would occupy all three vertices. In particular c=g_{q-1}∩g_q would be an entrance witness, so φ(c)=q-1, and another counted edge f would contain a and v. Apply a570c0ad0001 to P with p=2q-3 and i=q-2. It gives φ(c)≥min{q,q}=q, a contradiction. This proves the bound two.

For φ(v)=2q-2, instead take a path of length r=2q-2 ending at v. The same segment bounds force every visible entrance x of rank q-1 to be the single joint g_{q-1}∩g_q: no private position is possible. If x is absent, terminal-tail membership gives the first u-index j≥q-1, whereas the wrong-entrance prefix above gives j≤q-2, a contradiction. Hence every counted edge contains that same entrance joint and v. Linearity permits at most one.

The φ(v)≥2q-1 case was already excluded by the terminal-rank inequality. This proves all claims. The q=3 endpoint is consistent with the existing stronger rank-three incoming bound ccdf649da5bf. The new statement extends the bound two to arbitrary q in the odd central window.