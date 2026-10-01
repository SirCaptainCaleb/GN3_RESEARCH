# Equality-layer induction reconciles Turan and critical-core minimality

## Statement

Fix ell>=4 and d=floor(2ell/3). Consider the strengthened equality-layer assertion S_ell: every P_ell-free linear 3-graph H with |E(H)|>=d|V(H)| that contains a nonspecial edge has a vertex of degree at most d. If S_ell holds, then ex_L(n,P_ell^(3))<=dn. Moreover, whenever H is an edge-minimal counterexample to S_ell with |E(H)|>=d|V(H)|+1, then for every nonspecial edge e with witness path P, every edge f outside P contains a vertex of degree exactly d+1 in H.

## Body

Write n=|V(H)| and m=|E(H)|.

If S_ell holds and a P_ell-free H violated m<=dn, take a vertex-minimal counterexample. Then delta(H)>=d+1. If every edge were special, the certified snake bound gives
3m<=(2ell-3)n<=3dn,
contradiction. Thus H contains a nonspecial edge, and S_ell gives a vertex of degree at most d, again a contradiction.

Now let H be edge-minimal among counterexamples to S_ell, assume m>=dn+1, and fix a nonspecial edge e with witness path P. Let f be any edge outside P. Deleting f preserves P_ell-freeness and preserves nonspeciality of e with the same rank and unique entrance: the witness P survives, edge deletion cannot create a longer path ending in e, and cannot create a new entrance label.

Moreover
|E(H-f)|=m-1>=dn.
Since H-f has fewer edges than H, edge-minimality says H-f satisfies S_ell. Hence H-f has a vertex v with d_{H-f}(v)<=d.

All vertices outside f have unchanged degree at least d+1, because H itself is a counterexample to S_ell. Therefore v lies in f. Its degree in H is at most d+1, and the minimum-degree condition in H gives d_H(v)>=d+1. Hence d_H(v)=d+1.

Thus every off-witness edge meets the exact-threshold set
D={v:d_H(v)=d+1}.

The equality layer is essential: when m=dn+1, deletion of f lands exactly at m=dn, so the threshold-cover conclusion uses S_ell at equality. This is why a proof of the Turan bound by this route naturally becomes a simultaneous strict/equality induction rather than a strict-excess induction alone.
