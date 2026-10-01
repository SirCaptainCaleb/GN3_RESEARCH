# Single ascending terminal contacts on a maximum path lie in one central rank window

## Statement

Let H be a finite linear 3-graph. Let v have p=phi(v), and let P=(g_1,...,g_p) be any maximum p-edge path with last vertex v, with last edge g_p. Let e={x,v,u} be an ascending nonspecial edge of rank q<p, with unique entrance x, and suppose e has contact multiplicity one on P:
|(e minus {v}) intersect (V(P) minus g_p)|=1.
Let c be that unique contact, and let a,b be the first and last indices of path edges containing c.

Then
a<=q-1 and b>=p-q+2.
If c=u is the opposite terminal, the stronger a<=q-2 holds.

Consequently p<=2q-2. More precisely all possible singleton-contact vertices for ascending terminal edges of rank at most q lie in a common central window of exactly
max(0,4q-2p-3)
vertices. Hence if s_q(v;P) is the number of ascending edges terminal at v, of rank at most q, that are single on P, then
s_q(v;P)<=max(0,4q-2p-3).
In particular, if p>=2q-1, every ascending terminal edge of rank at most q is double on every maximum path with last vertex v.

## Body

Let c be the unique contact of e with W=V(P) minus g_p. Since e and g_p both contain v, linearity implies neither of the other two vertices of e lies in g_p.

First prove the left bound. If c=x, then the prefix g_1,...,g_a is a linear path with last vertex x: by definition of a, x occurs in no earlier edge. Hence a<=phi(x)=q-1.

If c=u, then x is absent from all of P. Indeed u is the unique contact in W and x cannot lie in g_p because e and g_p already meet at v. Therefore
g_1,...,g_a,e
is a linear path of length a+1 with last vertex x. It enters e through u, a terminal of the nonspecial edge e. If a+1>=q, then at equality this is a longest e-ending path with wrong entrance u, while if a+1>q it exceeds the rank q. Both are impossible. Thus a+1<=q-1, so a<=q-2.

Now prove the right bound without any assumption on the last edge g_p. Suppose b<=p-q+1. Then the final q-1 path edges
g_{p-q+2},...,g_p
avoid c. Since c is the only contact of e outside g_p, and e meets g_p only at v, the sequence
g_{p-q+2},...,g_p,e
is a linear q-edge path ending in e and entering e through v. But v is a terminal of the nonspecial edge e, whereas its unique entrance is x. This is a longest e-ending path with a wrong entrance, contradiction. Therefore b>=p-q+2.

Every path vertex outside g_p has occurrence interval either {i} for a private vertex of g_i or {i,i+1} for the joint g_i intersect g_{i+1}. Thus a singleton contact of rank at most q must have first occurrence at most U=q-1 and last occurrence at least L=p-q+2. Since q<p, the eligible private vertices are precisely those of g_i with L<=i<=U, numbering max(0,U-L+1)=max(0,2q-p-2), and the eligible joints are precisely g_i intersect g_{i+1} with L-1<=i<=U, numbering max(0,U-L+2)=max(0,2q-p-1). Their total is max(0,4q-2p-3).

Distinct edges through v have distinct non-v contact vertices by linearity. Therefore the number of single-contact ascending terminal edges of rank at most q is at most the number of eligible vertices, proving the result.
