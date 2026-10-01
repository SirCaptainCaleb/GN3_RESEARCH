# In minimum-potential equality, every special edge lies strictly below all three endpoint potentials

## Statement

Assume the minimum-potential equality setting of 148ebd1d1809. Then for every vertex v with p=phi(v), every maximum p-edge path ending at v has a nonspecial last edge for which v is a terminal.

Consequently, if e is special and v∈e, then
  phi(e)<=phi(v)-1.
Thus every special edge e={a,b,c} satisfies
  phi(a),phi(b),phi(c)>=phi(e)+1.

## Body

Fix v and put p=phi(v). From 148ebd1d1809,
  t_ns(v)=2p-3.
Choose an arbitrary maximum p-edge path P ending at v and let h be its last edge.

In the proof of the certified cumulative terminal bound 0e550ff0eadd with q=p, every nonspecial terminal edge through v other than a possible h is injected into a set of exactly 2p-4 precursor vertices. If h were not one of the nonspecial terminal edges counted by t_ns(v), then all 2p-3 such edges would have to inject into those 2p-4 vertices, impossible. Therefore h is nonspecial and v is a terminal for h.

Since P was arbitrary, every maximum endpoint path ending at v has nonspecial last edge.

Now let e be special and contain v. Specialness implies v is a snake terminal for e, so there exists a phi(e)-edge path ending with e and last vertex v. If phi(e)=p, that path would be a maximum p-edge endpoint path ending at v with special last edge e, contradicting the preceding conclusion. Since always phi(e)<=phi(v)=p at a special incidence, one must have phi(e)<=p-1.

Apply this to all three vertices of e.
