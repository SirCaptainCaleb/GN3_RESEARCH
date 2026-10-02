# Two truncated terminal stars force many bounded-reuse linear triangles

## Statement

Let e={x,u,v} be an ascending nonspecial edge of edge rank q, and let R be a canonical source rail ending at its unique entrance x. For w in {u,v}, restrict to ascending edges terminal at w of edge rank at most q, including e, let t_w be their number, and write delta_w=gamma(q)-t_w>=0. Put Delta=delta_u+delta_v. Then the two truncated terminal stars around the common source rail force at least q/8-3Delta-O(1) distinct linear 3-cycles. More exactly, with alpha(q)=ceil((3q-8)/4), kappa_q=alpha(q)-2gamma(q)+2q in {0,1}, the number is at least one half of 3alpha(q)-2q+2-6kappa_q-6Delta. The resulting triangles have multiplicity at most three when counted over choices of the base edge e.

## Body

Let W be the vertex set of the source-rail precursor, so |W|=2q-2. For w in {u,v}, let T_w be the ascending edges f!=e terminal at w with edge rank at most q. Apply the source-rail coupling theorem 1000259 to T_w. Write S_w for the number of vertices of W used as singleton contacts by T_w, U_w for the number unused by T_w, B_w for the number of two-vertex contact sets, and M_w for the matching of those two-vertex contact pairs. Let
  t_w=1+|T_w|.
The fixed-entrance terminal bound used in 1000285 gives t_w<=gamma(q); define
  delta_w=gamma(q)-t_w>=0.
The exact source-rail identity from 1000259 gives
  2t_w=2q+S_w-U_w,
hence
  S_w-U_w=2gamma(q)-2q-2delta_w.                 (1)

As in 1000285, the fixed-entrance transfer theorem gives
  S_w<=alpha(q),  alpha(q)=ceil((3q-8)/4).
With
  kappa_q=alpha(q)-2gamma(q)+2q in {0,1},
equation (1) yields
  S_w>=alpha(q)-kappa_q-2delta_w,                (2)
  U_w<=kappa_q+2delta_w.                         (3)
No maximum-rank hypothesis at u or v is needed: truncating the terminal stars at edge rank q is enough for the source-rail argument.

Now compare M_u and M_v. Let I be the number of vertices that are singleton contacts for both terminal stars. Put
  A_w=S_w union U_w
as a vertex subset of W; the endpoints of M_w are exactly W\A_w. In G=M_u union M_v let n_1,n_2 be the numbers of degree-one and degree-two vertices. Since the two matchings are edge-disjoint, every nontrivial component is an alternating path or even cycle. The number of nontrivial path components is n_1/2, and every path component having at least two edges contains a degree-two vertex. Hence the number L_1 of one-edge components satisfies
  L_1>=n_1/2-n_2.
Writing J=|A_u intersect A_v|,
  n_1=|A_u triangle A_v|,
  n_2=|W|-|A_u union A_v|,
so
  L_1>=3/2(|A_u|+|A_v|)-|W|-2J.
Every element of A_u intersect A_v not counted by I lies in U_u union U_v, hence
  J<=I+U_u+U_v.
Therefore
  L_1>=3/2(S_u+S_v)-|W|-2I-1/2(U_u+U_v).       (4)

Call a one-edge component usable if, when its edge belongs to M_u, both endpoints are singleton contacts for the v-star, and symmetrically for an edge of M_v. Every unusable one-edge component contains a vertex in U_u union U_v. Distinct components are vertex-disjoint, so at most U_u+U_v one-edge components are unusable. If L is the number of usable one-edge components, (4) gives
  L>=3/2(S_u+S_v)-|W|-2I-3/2(U_u+U_v).          (5)
Substitute |W|=2q-2 and (2),(3), with Delta=delta_u+delta_v:
  L>=3alpha(q)-2q+2-6kappa_q-6Delta-2I.         (6)
Let
  C=3alpha(q)-2q+2-6kappa_q-6Delta.

Each common singleton-contact vertex a counted by I gives a linear 3-cycle consisting of e and the two singleton-contact edges through u and v at a. Distinct a give distinct such cycles.

Each usable one-edge component also gives a linear 3-cycle. For example, if {a,b} is an edge of M_u, the corresponding hyperedge f={u,a,b} is accompanied by distinct singleton-contact edges through v meeting W at a and b. These three hyperedges meet pairwise in a,b,v and, by linearity, in no further vertices. Distinct one-edge components give pairwise edge-disjoint cycles. These cycles do not contain e, so they are distinct from the cycles arising from common singleton contacts.

Consequently the number T of distinct cycles produced satisfies
  T>=I+L.
Together with L>=C-2I and L>=0, a two-case check gives
  T>=C/2
   =[3alpha(q)-2q+2-6kappa_q-6Delta]/2.           (7)
Since alpha(q)=3q/4+O(1) and kappa_q in {0,1},
  T>=q/8-3Delta-O(1).
Moreover one of the two mechanisms alone has size at least C/3, namely q/12-2Delta-O(1).

Finally these outputs have bounded reuse over choices of e. A cycle arising from a common singleton-contact vertex contains its base edge e, so the same 3-cycle can arise from at most its three constituent edges as base edges. For a cycle arising from a usable one-edge component, fix which constituent edge is the two-vertex-contact edge. The cycle then determines its third vertex u and the intersection v of the other two edges; a base edge must contain u and v, and linearity allows at most one such hyperedge. There are at most three choices for the distinguished two-vertex-contact edge. Thus every produced triangle has multiplicity at most three over base-edge choices.