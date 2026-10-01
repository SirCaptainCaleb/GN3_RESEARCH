# Dual excess equals deletion-cover slack

## Statement

Let H be an n-vertex boundary tournament such that H-v has a two-cover for every v. Let w>=0 satisfy w(V(P))<=1 for every tight path P, and let w(V(H))=2+eta. Then w(v)>=eta for every v. Writing delta(v)=w(v)-eta, for every deletion cover P|Q of H-v one has
(1-w(V(P)))+(1-w(V(Q)))=delta(v).
Consequently sum_v delta(v)=2-(n-1)eta, so eta<=2/(n-1), and each path in every v-deletion cover has weight at least 1-delta(v).

## Body

Let H be a finite boundary tournament on n vertices such that H-v has a two-cover for every vertex v. Let w:V(H)->R_{>=0} satisfy w(V(P))<=1 for every tight path P, and suppose

W:=w(V(H))=2+eta.

Fix v and write w(v)=eta+delta(v). For any deletion cover P|Q of H-v,

w(V(P))+w(V(Q))=W-w(v)=2-delta(v).

Since each of P and Q is a tight path, dual feasibility gives w(V(P))<=1 and w(V(Q))<=1. Hence

delta(v)=[1-w(V(P))]+[1-w(V(Q))]>=0.

Thus w(v)>=eta for every v, and the displayed identity is independent of the chosen deletion cover of H-v. In particular each component of every deletion cover of H-v has weight at least 1-delta(v).

Summing w(v)=eta+delta(v) over all vertices gives

2+eta=n eta+sum_v delta(v),

so

sum_v delta(v)=2-(n-1)eta.

Therefore eta<=2/(n-1). Equality holds if and only if delta(v)=0 for every v, in which case every vertex has weight eta and every component of every deletion cover has weight exactly 1.

The argument uses only the existence of a two-cover after each one-vertex deletion; minimum-counterexample status is not otherwise needed.
