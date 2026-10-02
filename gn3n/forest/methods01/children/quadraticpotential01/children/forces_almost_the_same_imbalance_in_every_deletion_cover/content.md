# A global quadratic minimum with a four-vertex component forces almost the same imbalance in every deletion cover

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover minimizing Phi=sum |C_i|^2 among all spanning three-covers, with |X|=4, |P|=m, |Q|=r. Put d=|m-r|. For any vertex v and any deletion cover H-v=U|W, write p=|U|>=q=|W| and D=p-q. Then D>=d-1. More precisely, each initial- or terminal-end four-vertex endpoint construction from U|W produces a spanning three-cover whose two non-four component orders have sum m+r and imbalance either |D-1| or D+1; global Phi-minimality forces the realized imbalance to be at least d. Consequently, if d>=2 and D=d-1, both end constructions are forced to use the D+1 orientation, both have the same component-order multiset {4,m,r} as the original global minimum, and their cross triples are (w_0,v,u_0) and (u_{p-1},v,w_{q-1}) for displayed orders U=(u_0,...,u_{p-1}), W=(w_0,...,w_{q-1}).

## Body

Let X|P|Q be globally Phi-minimal with |X|=4, |P|=m, |Q|=r, and put d=|m-r|. Thus
Phi_0=16+m^2+r^2.

Fix v and a deletion cover
H-v=U|W,
with displayed orders
U=(u_0,...,u_{p-1}), W=(w_0,...,w_{q-1}),
where p>=q. In a minimum counterexample every deletion-cover component has order at least three, so the residual paths below are nonempty.

The endpoint-extension obstruction gives
(u_1,u_0,v), (w_1,w_0,v),
(v,u_{p-1},u_{p-2}), (v,w_{q-1},w_{q-2})
tight.

At the initial ends exactly one of
(u_0,v,w_0), (w_0,v,u_0)
is tight.

If (u_0,v,w_0) is tight, then
(u_1,u_0,v,w_0) | (u_2,...,u_{p-1}) | (w_1,...,w_{q-1})
is a spanning three-cover, with component orders
4, p-2, q-1.
If instead (w_0,v,u_0) is tight, then
(w_1,w_0,v,u_0) | (u_1,...,u_{p-1}) | (w_2,...,w_{q-1})
is a spanning three-cover, with component orders
4, p-1, q-2.

The same construction at the terminal ends gives another spanning three-cover, again with one of these two order multisets.

Since
p+q=|V(H)|-1=m+r+3,
the two non-four components in either construction have total order m+r. Their imbalance is respectively
|(p-2)-(q-1)|=|D-1|
or
|(p-1)-(q-2)|=D+1,
where D=p-q.

For fixed total m+r, quadratic potential on the two non-four components is strictly ordered by absolute imbalance. Because X|P|Q is globally Phi-minimal, every spanning three-cover just constructed must have two-component imbalance at least d. Hence whichever orientation occurs,
d <= max{|D-1|,D+1}=D+1.
Therefore
D>=d-1.

Now assume d>=2 and D=d-1. Then D>=1. The first orientation would have residual imbalance
|D-1|=d-2<d,
contradicting global Phi-minimality. Hence the second orientation is forced at the initial ends, so
(w_0,v,u_0)
is tight. The identical argument at the terminal ends forces the second orientation there as well, giving
(u_{p-1},v,w_{q-1})
tight.

In each forced construction the two residual component orders have total m+r and imbalance
D+1=d.
Therefore their unordered size pair is exactly {m,r}. Each resulting three-cover has component-order multiset {4,m,r}, hence exactly the same Phi as the original global minimum.

Thus every deletion cover lies at imbalance at least d-1; attaining the floor for d>=2 creates two endpoint-locked equal-Phi transitions among the globally Phi-minimal three-covers. ∎