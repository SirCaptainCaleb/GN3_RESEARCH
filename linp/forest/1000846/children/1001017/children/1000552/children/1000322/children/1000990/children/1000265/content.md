# The sharp Turan bound reduces to the exact-density equality layer

## Statement

Fix ell>=5, put d=floor(2ell/3) and k=d+1. Assume the following equality-layer assertion E_ell:

Every P_ell-free linear 3-graph J with |E(J)|=d|V(J)| that contains a nonspecial edge has a vertex of degree at most d.

Then
ex_L(n,P_ell^(3))<=dn
for every n.

More strongly, under E_ell there is no edge-minimal strict counterexample, because its DXX color graph simultaneously has more than k(k-3/2)|X| edges and fewer than ((9ell+5)/7)|X| edges.

## Body

Assume E_ell and suppose, for contradiction, that H is P_ell-free with
m:=|E(H)|>dn.
Choose H edge-minimal among such strict Turan counterexamples after first passing to a vertex-minimal counterexample if desired. The standard peeling reduction gives delta(H)>=d+1=k.

If every edge of H were special, the certified special-edge/snake bound would give
3m<=(2ell-3)n.
Since (2ell-3)/3<floor(2ell/3)=d for ell>=5, this contradicts m>dn. Thus H contains a nonspecial edge e. Fix a longest witness path P ending in e.

Let f be any edge outside P. Deleting f preserves P_ell-freeness and preserves nonspeciality of e with the same rank and unique entrance. Since H is edge-minimal for strict excess,
m-1<=dn.
Because m and dn are integers and m>dn, necessarily m=dn+1 and hence
|E(H-f)|=dn.

By E_ell, H-f has a vertex v of degree at most d. Only vertices of f lost degree. Since delta(H)>=d+1 and deletion lowers a surviving degree by at most one in a linear hypergraph, v lies in f and
d_H(v)=d+1=k.
Thus the threshold set
D={v:d_H(v)=k}
meets every edge outside P. The argument of 7de985881169 and 324fa959c567 now applies verbatim: with X=V(H)\D, the induced hypergraph H[X] is a linear path forest, so
m_0:=|E(H[X])|<=|X|/2.

Let m_i denote the number of edges of H containing exactly i vertices of D, i=1,2,3, and put
s=m_2+2m_3.
Counting D-incidences gives
k|D|=m_1+2m_2+3m_3,
while the number of edges meeting D is
m_D=m_1+m_2+m_3=k|D|-s.

Since m=dn+1=(k-1)(|D|+|X|)+1,
m_0+k|D|-s>(k-1)(|D|+|X|).
Therefore
|D|-s>(k-1)|X|-m_0
          >=(k-3/2)|X|.

Also
m_1=k|D|-2m_2-3m_3
   >=k|D|-2s
   =(k-2)|D|+2(|D|-s)
   >k(k-3/2)|X|,
because s>=0 implies |D|>|D|-s>(k-3/2)|X|.

Now form the simple graph G on X from the m_1 edges of type DXX, coloring xy by the unique d∈D with {d,x,y}∈E(H). Linearity makes this a proper edge-coloring. Any rainbow graph P_ell in G lifts directly to a linear hypergraph P_ell in H, because graph vertices lie in X and color vertices lie in disjoint set D. Hence G is rainbow-P_ell-free.

By the certified Ergemlidze-Gyori-Methuku bound e4fb292edb26,
m_1<((9ell+5)/7)|X|.

For ell>=5 one has
k(k-3/2)>(9ell+5)/7.
Indeed this is immediate in the three residue classes ell mod 3, and the smallest case ell=5 already reads 10>50/7; thereafter the left side grows quadratically in ell while the right side grows linearly.

This contradicts the two bounds on m_1. Therefore no strict Turan counterexample exists, proving
ex_L(n,P_ell^(3))<=dn.

Thus the entire strict-density problem is reduced to E_ell, the exact-density nonspecial low-degree assertion.
