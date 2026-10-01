# PG(3,2) gives a 7/3 lower bound for P7

## Statement

The binary projective Steiner triple system PG(3,2) on 15 vertices and 35 edges contains no linear path with 7 edges. Consequently ex_L(n,P_7^(3)) >= 35 floor(n/15) = (7/3)n-O(1), with equality to (7/3)n for 15|n.

## Body

Let V=F_2^4\setminus\{0\}, and let H be the 3-graph on V whose edges are the triples \{u,v,u+v\} with u and v distinct. Every pair of vertices lies in exactly one edge, so H is linear and has \binom{15}{2}/3=35 edges.

Suppose for a contradiction that H contains a linear path P=e_1,\ldots,e_7. Since a 7-edge linear 3-uniform path has 15 vertices, P is spanning. For 1\le i\le 6 let j_i be the joint e_i\cap e_{i+1}.

The sum of all vectors in V is 0, and the three vertices of every edge of H sum to 0. Summing the seven edge equations, every joint is counted twice and every nonjoint vertex once. Hence the nonjoint vertices have sum 0, and therefore
\[
j_1+\cdots+j_6=0.
\]
The six distinct joints lie in the 4-dimensional space F_2^4, so their six column vectors have a relation space of dimension at least two. Besides the all-six relation above, choose a nonzero proper relation and, if necessary, replace its support by its complement. Its support has size at most three. A zero-sum set of distinct nonzero vectors cannot have size one or two, so it has size three. Thus the joints split as
\[
J=U^*\sqcup W^*,
\]
where U^*=U\setminus\{0\} and W^*=W\setminus\{0\} are the nonzero points of two 2-dimensional subspaces U,W. Since the six joints are distinct, U\cap W=\{0\}; hence F_2^4=U\oplus W.

Two consecutive joints cannot both lie in U^* (and similarly cannot both lie in W^*). Indeed, if two consecutive joints of an edge e_i were distinct points u,u' of U^*, then the third vertex of e_i would be u+u', the third point of U^*. That vertex is another joint of P, contradicting the path intersection pattern. Therefore
\[
j_1,j_2,\ldots,j_6
\]
alternates between U^* and W^*. Regard the complete bipartite graph K_{3,3} with parts U^* and W^*. The joint sequence is then a Hamilton path T in K_{3,3}.

Every vector outside U^*\cup W^* has a unique form u+w with u\in U^* and w\in W^*. Identify this vector with the edge uw of K_{3,3}. For 2\le i\le 6, the edge e_i has consecutive joints j_{i-1},j_i, so its third vertex is j_{i-1}+j_i. Consequently the five internal nonjoint vertices of P correspond exactly to the five edges of T. The four nonjoint vertices not used by e_2,\ldots,e_6 therefore correspond exactly to the complement
\[
F=E(K_{3,3})\setminus E(T).
\]

Assume, after interchanging U and W if necessary, that j_1\in U^*; then j_6\in W^*. The first path edge e_1 contains j_1 and two of the four remaining nonjoint vertices. Write these vertices as
\[
x=u+w,\qquad y=u'+w'
\]
with u,u'\in U^* and w,w'\in W^*. Since x+y=j_1\in U, uniqueness in U\oplus W gives w=w' and u+u'=j_1. Thus the two corresponding edges of F share the vertex w, and their U-endpoints are precisely the two points of U^* other than j_1. In particular, d_F(w)\ge2.

But T is a Hamilton path in the cubic graph K_{3,3}. Hence
\[
d_F(v)=3-d_T(v),
\]
so the only vertices of F of degree two are the two endpoints j_1 and j_6 of T; every internal vertex has F-degree one. Since w\in W^* while j_1\in U^*, it follows that w=j_6. The two U-points other than j_1 include j_5, because T alternates and ends j_5j_6. Therefore one of the two edges of F required by e_1 is j_5j_6. This is impossible, since j_5j_6 is the last edge of T.

Thus H contains no linear path with seven edges. Taking disjoint copies gives
\[
\operatorname{ex}_L(n,P_7^{(3)})\ge 35\left\lfloor\frac n{15}\right\rfloor
=\frac73 n-O(1),
\]
and the construction has exactly (7/3)n edges when 15 divides n.