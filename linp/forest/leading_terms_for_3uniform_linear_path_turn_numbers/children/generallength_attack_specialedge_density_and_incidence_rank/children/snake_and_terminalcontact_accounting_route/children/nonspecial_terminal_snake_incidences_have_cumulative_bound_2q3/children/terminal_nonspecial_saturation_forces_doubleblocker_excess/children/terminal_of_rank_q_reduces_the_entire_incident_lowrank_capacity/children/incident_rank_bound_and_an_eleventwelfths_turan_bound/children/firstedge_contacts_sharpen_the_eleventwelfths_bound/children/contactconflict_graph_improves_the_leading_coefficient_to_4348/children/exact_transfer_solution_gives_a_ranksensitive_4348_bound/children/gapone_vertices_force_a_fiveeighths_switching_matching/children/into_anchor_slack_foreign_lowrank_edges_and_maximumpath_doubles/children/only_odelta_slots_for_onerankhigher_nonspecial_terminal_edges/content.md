# Near saturation leaves only O(delta) slots for one-rank-higher nonspecial terminal edges

## Statement

Let v lie in the gap-one shell phi(v)=q+1 with q(v)=q>=4. Choose a maximum-rank ascending nonspecial anchor
      e={x,v,u}
    of rank q terminal at v, and let R be a canonical (q-1)-edge source rail ending physically at x, so R,e is a q-edge longest path and R avoids v,u. Put
      W=V(R) minus {x},
    so |W|=2q-2.

Let
      J=J_q(v)={f: v in f and phi(f)<=q},
      M=gamma(q)=floor((11q-5)/8),
      r=M-|J|,
    and let U_R be the set of vertices of W unused by all contacts (f minus {v}) intersect W for f in J minus {e}.

Let H_+(v) be the family of nonspecial edges h through v such that v is a terminal of h and phi(h)=q+1. Then
      |H_+(v)| <= |U_R| <= 2r+1.

In the near-dangerous gap-one notation of f6c9ded0ae63, r<=delta, and therefore
      |H_+(v)| <= 2delta+1.
In particular, at exact local saturation delta=0 there is at most one nonspecial rank-(q+1) edge terminal at v.

## Body

By the fixed-entrance contact system for the anchor e, every edge f in J minus {e} meets W in one or two vertices, and the contact sets are pairwise disjoint. The periodic near-equality identity 88db9b4e8337 gives
      |U_R|<=2r+1.

Now let h be in H_+(v). Since h is nonspecial, has rank q+1, and v is a terminal of h, downward-completeness of the canonical source rail (1c8aac8aa4dd) forces h to meet V(R). Because h and e are distinct edges through v, linearity gives h intersect e={v}; in particular h contains neither x nor u. Hence every R-contact of h lies in W.

We claim that every such R-contact lies in U_R. Indeed, if y in W also belonged to the contact set of some f in J minus {e}, then h and f would both contain v and y, contradicting linearity. Thus h must use at least one vertex of U_R.

Distinct edges h,h' in H_+(v) already share v, so linearity forbids them from sharing any second vertex. Choosing one R-contact for each h therefore injects H_+(v) into U_R. Hence
      |H_+(v)|<=|U_R|<=2r+1.

Finally f6c9ded0ae63 gives
      r=M-|J|<=delta
in the gap-one local-slack notation, proving
      |H_+(v)|<=2delta+1.