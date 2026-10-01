# Clean-retained switchers gain a one-sixth quadratic source term

## Statement

Let v be an active misaligned vertex with p=phi(v)>=8, let P_v be the chosen maximum p-edge path, and let F_v be a switching family from b032348c1a8a. Split
  F_v = X_v disjoint_union U_v,
where X_v consists of switchers whose unique retained off-v contact on P_v is their entrance, and U_v consists of switchers whose retained contact is the opposite terminal. Put
  a=|X_v|, k=|U_v|, s=a+k.

Order the ranks of X_v as
  rho_1<=...<=rho_a.
Then for every i,
  rho_i >= p/2 + (i+1)/3,
and therefore
  sum_{f in X_v} phi(x_f) >= (p/2)a + (a^2-a)/6.

Every f in U_v has
  phi(x_f) >= (p+1)/2.
Consequently
  sum_{f in F_v} phi(x_f)
  >= (p/2)s + (a^2-a)/6 + k/2.                 (*)

Combining (*) with the all-switcher central-window bound a5066873364f gives
  sum_{f in F_v} phi(x_f)
  >= max{
       (p/2)s+s^2/8-s/8,
       (p/2)s+(a^2-a)/6+k/2
     }.

In particular, if eta_v=o(p), then s=(5/8-o(1))p. Hence either |U_v|=Omega(p), or, whenever |U_v|=o(p),
  sum_{f in F_v}phi(x_f) >= (145/384-o(1))p^2.
Thus a low-defect center either carries a linear terminal-retained switching family or pays the stronger 145/384 clean-retained source-mass coefficient.

## Body

Fix an integer R<p and let X_{\le R} be the members of X_v of edge rank at most R. Every member of X_{\le R} is an ascending terminal edge that is single on P_v and whose unique P_v-contact is its entrance.

The central-window localization 49080cbf1371 says that an entrance contact of rank at most R can occur only in the common central window. More explicitly, writing P_v=(g_1,...,g_p), the eligible joint entrances are
  g_j intersect g_{j+1},
  p-R+1 <= j <= R-1,
so there are
  J=2R-p-1
eligible joints; the eligible private entrances lie on
  g_j,
  p-R+2 <= j <= R-1,
so there are
  m=2R-p-2
eligible private indices. If X_{\le R} is nonempty then p<=2R-2, hence m>=0.

Distinct switchers have distinct entrance vertices by linearity. Thus at most J members of X_{\le R} use joints.

For private entrances, c265aa8ded39 says that two occupied private indices differing by two are incompatible. On the m consecutive eligible indices, the graph joining indices at distance two is the disjoint union of two paths. Its independence number is at most m/2+1. Hence
  |X_{\le R}|
  <= J + m/2 +1
  = 3R - (3/2)p -1.                              (1)

Now order the X_v-ranks rho_1<=...<=rho_a. Taking R=rho_i in (1) gives
  i <= 3rho_i-(3/2)p-1,
and hence
  rho_i >= p/2+(i+1)/3.                           (2)

If x_i is the unique entrance of the corresponding ascending edge, then phi(x_i)=rho_i-1. Summing (2),
  sum_{i=1}^a phi(x_i)
   >= sum_{i=1}^a [p/2+(i+1)/3-1]
   = (p/2)a + a(a+1)/6 -2a/3
   = (p/2)a +(a^2-a)/6.                           (3)

Now let f={x,v,u} lie in U_v and have rank r. It is terminal-only single on P_v: u is the unique off-v contact and x is absent. The sharper terminal-only singleton localization 028c2c3f7167 gives
  r>=ceil((p+3)/2).
Since f is ascending, phi(x)=r-1>=(p+1)/2. Therefore
  sum_{f in U_v}phi(x_f)>=k(p+1)/2.               (4)

Adding (3) and (4) yields (*). The maximum with the all-switcher estimate is exactly a5066873364f.

Finally b032348c1a8a gives s>=(5/8)p-eta_v-O(1), so eta_v=o(p) implies s=(at least 5/8-o(1))p. If k=o(p), then a=s-o(p)=(at least 5/8-o(1))p, and (*) gives
  sum_{F_v}phi(x_f)
  >= (p/2)(5p/8)+(1/6)(25p^2/64)-o(p^2)
  = [5/16+25/384-o(1)]p^2
  = (145/384-o(1))p^2.
Otherwise k=Omega(p), giving the asserted terminal-retained branch.
