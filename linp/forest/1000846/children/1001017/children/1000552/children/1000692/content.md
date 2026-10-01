# Ascending-edge defect reduces to near-top clean chords and high-potential rotation endpoints

## Statement

Let H be a P_ell^(3)-free linear 3-graph with m edges and n vertices. Let A be the number of ascending edges. For every nonspecial nonascending edge f with unique entrance x define
  r(f)=ceil(phi(x)/(phi(f)-1))-2,
and let R=sum_f r(f). Then
  3m-A+R <= sum_v(2phi(v)-1) <= (2ell-3)n.

Choose for every vertex v a maximum p=phi(v) path P_v ending at v and assign every ascending nonspecial edge e={x,v,u} to a terminal v of minimum terminal potential. Apart from at most one assigned last edge per vertex, every assigned edge is of type D (both x,u on P_v), X (x on P_v,u off P_v), or U (u on P_v,x off P_v). If B is the chosen-path double-blocker compensation and S_X,S_U are the X,U counts, then
  A<=B+S_X+S_U+n
and, with N=(2ell-3)n,
  5m+s+R <= 2N+S_X+S_U+n.
For every fixed epsilon>0, the X-edges with phi(e)<=(1-epsilon)phi(v) contribute only O_epsilon(n).

Moreover, for a fixed charged pair (P_v,v), the U-edges expand with multiplicity at most two into distinct canonical Pósa endpoints w of potential at least phi(v): if W(P_v,v) is the set of resulting endpoints then
  |U(P_v,v)| <= 2|W(P_v,v)|+1.
Thus the leading ascending-edge obstruction is localized to near-top-rank clean entrance chords and large sets of nondecreasing-potential rotation endpoints.

## Body

Fix a vertex x. Let I(x) be the incident edges e with phi(e,x)=phi(e), let C(x) be the ascending edges with unique entrance x, and let B^-(x) be the nonspecial nonascending edges with unique entrance x. These classes partition the incident edges. For f in B^-(x), the joint snake-incidence/blocker budget gives
  w_x(f)=ceil(phi(x)/(phi(f)-1))-1
and
  |I(x)|+sum_{f in B^-(x)}w_x(f)<=2phi(x)-1.
Because f is nonascending, w_x(f)>=1. Hence
  d_H(x)<=2phi(x)-1+|C(x)|
           -sum_{f in B^-(x)}(w_x(f)-1).
Summing over x counts every ascending edge once through its unique entrance and every nonascending compensation once. With
  r(f)=w_x(f)-1=ceil(phi(x)/(phi(f)-1))-2
and R=sum_f r(f), this gives
  3m-A+R<=sum_x(2phi(x)-1).
P_ell-freeness implies phi(x)<=ell-1, so the right side is at most (2ell-3)n.

Now for each vertex v choose a maximum p=phi(v) path P_v ending at v. Assign each ascending nonspecial edge e={x,v,u} to a terminal v having minimum terminal potential; then phi(u)>=p, so e is potential-charged at v. Except when e itself is the last edge of P_v, the charged two-point transversal property forces P_v to contain x or u. This yields the exhaustive trichotomy:
  D: x,u both lie on P_v;
  X: x lies on P_v and u does not;
  U: u lies on P_v and x does not.
A D-edge is counted by the chosen-path double-blocker term B_v. Thus globally
  A<=B+S_X+S_U+n.
Combining this with the compensated ascending inequality
  3m<=N+A-R
and the chosen-path blocker inequality
  2m+s+B<=N
gives
  5m+s+R<=2N+S_X+S_U+n.

For type X, the charged edge meets P_v exactly in {x,v}, so it is a clean entrance chord. The clean-entrance deficit-spacing lemma implies that for fixed epsilon>0 the edges satisfying
  phi(e)<=(1-epsilon)p
number only O_epsilon(1) at each v, hence O_epsilon(n) in total. Therefore only near-top-rank X-edges can contribute to the leading residual.

It remains to understand the U-edges. For e in U(P_v,v), let j(e) be the first index of P_v containing u. The canonical terminal-only rotation gives j(e)<=p-2 and an endpoint
  w(e)=g_{j(e)+1} cap g_{j(e)+2}
with phi(w(e))>=p. Different first-contact indices give different endpoints. By linearity, distinct charged edges through v have distinct opposite terminals u. In an oriented linear path, at most two vertices have first occurrence at any edge g_j for j>=2, while at most three have first occurrence at g_1. Hence at most two U-edges have a fixed j>=2 and at most three have j=1. If W(P_v,v) is the set of distinct canonical endpoints, then
  |U(P_v,v)|<=2|W(P_v,v)|+1,
so
  |W(P_v,v)|>=(|U(P_v,v)|-1)/2,
and every w in W has phi(w)>=phi(v).

Consequently the original global ascending-edge error has been reduced to two structured leading-order phenomena: entrance-only chords whose rank is asymptotically at the charged terminal potential, and terminal-only rotations which force comparably large sets of distinct reachable endpoints of nondecreasing potential.
