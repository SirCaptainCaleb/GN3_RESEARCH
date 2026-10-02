# Every deletion singleton state descends in two moves to a three-vertex central state

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, with p=|P|>=q=|Q|. Then the singleton lift P|Q|{x} reaches in two legal pairwise repartitions a spanning three-cover P^-|C|Q^+ with |C|=3 and component-order multiset {p-1,q-1,3}. Both moves strictly decrease the quadratic potential Phi: the first by 2q-4 and the second by 2p-6, so the net decrease is 2|V(H)|-12. Here C is supported on the two facing endpoints of P,Q together with x, using whichever of the two reverse orders is tight. Consequently the earlier three-versus-five central-path split is unnecessary for no-trapping: every deletion state has a monotone two-move route to a three-vertex central state. If |V(H)|>=14, the resulting state has a component of order at least six and therefore admits a further strict one-move descent by threesidedescent6.

## Body

Write
P=(p_0,...,p_{p-1}),  Q=(q_0,...,q_{q-1}),
with p>=q. By the deletion-cover bounds, p,q>=3. Since H is a minimum counterexample, |V(H)|>10, so p+q=|V(H)|-1>=10 and therefore p>=5.

Start from the singleton lift
S_0=P|Q|(x).

First repartition Q|(x). The two-vertex order
(x,q_0)
is a tight path, and
Q^+=(q_1,...,q_{q-1})
is an inherited contiguous tight path. Thus
S_1=P|(x,q_0)|Q^+
is reached by one legal pairwise repartition.

For the changed pair, the old component orders are q,1 and the new orders are q-1,2. Hence
Phi(S_0)-Phi(S_1)
=q^2+1-[(q-1)^2+2^2]
=2q-4>0.                                             (1)

Now inspect the three vertices
{p_{p-1},x,q_0}.
Boundary antisymmetry says exactly one of
(p_{p-1},x,q_0)
and
(q_0,x,p_{p-1})
is tight. Let C denote the resulting tight three-vertex path in whichever of those two orders is tight.

Repartition the pair P|(x,q_0). Its union has the two-path cover
P^-|C,
where
P^-=(p_0,...,p_{p-2})
is inherited from P. Hence a second legal move reaches
S_2=P^-|C|Q^+.

For this move the old pair orders are p,2 and the new pair orders are p-1,3. Therefore
Phi(S_1)-Phi(S_2)
=p^2+2^2-[(p-1)^2+3^2]
=2p-6>0,                                             (2)
because p>=5.

Adding (1) and (2),
Phi(S_0)-Phi(S_2)
=2p+2q-10
=2(|V(H)|-1)-10
=2|V(H)|-12.                                        (3)

Thus every deletion singleton lift reaches, by two consecutive strict quadratic descents, a spanning three-cover with component orders
p-1,q-1,3.
No case split on the orientation of the facing middle triple is needed: that orientation only determines which order of the same three-vertex support is used for C.

This strictly strengthens the central-path reachability picture. The five-vertex path from centralbridge35 remains valid additional structure when all three join triples reverse coherently, but it is not needed to obtain a central three-vertex path or to enter the quadratic-descent route.

Finally, if n=|V(H)|>=14, then
p>=ceil((n-1)/2)>=7,
so |P^-|=p-1>=6. Applying threesidedescent6 to C|P^- yields a third strict one-move quadratic descent. ∎