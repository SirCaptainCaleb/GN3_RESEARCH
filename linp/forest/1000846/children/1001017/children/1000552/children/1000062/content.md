# Nonspecial terminal snake incidences have cumulative bound 2q-3

## Statement

Let H be a finite linear 3-graph, let v be a vertex, and let 2<=q<=phi(v). Among nonspecial edges e for which v is a terminal snake vertex and phi(e)<=q, there are at most 2q-3. In particular, the total number t(v) of nonspecial edges for which v is a terminal satisfies t(v)<=max{0,2phi(v)-3}.

## Body

Fix v and put p=phi(v). Choose a maximum p-edge path
  P=(g_1,...,g_p)
ending at v; thus v is private to the last edge h=g_p.

Let F be the family of nonspecial edges e such that v is a terminal vertex of e and phi(e)<=q. There is at most one member of F equal to h. We show that every e in F\{h} can be assigned a distinct vertex from a set of size 2q-4.

Take e in F\{h}, and write r=phi(e)<=q. Since v is terminal for e, r<=phi(v)=p. The path P does not use e, because e contains v while v appears only in the final edge h. Also e must meet P at some vertex other than v: if not, e could be appended to P through v, giving a (p+1)-edge path ending in e and hence phi(e)>=p+1>r.

Among the vertices of e\{v} occurring on P, choose the one whose last occurrence before v is latest, and call it w_e. Let i be the last path-edge index containing w_e. By choice of w_e, no vertex of e occurs on the intervening path segment from after i until the final occurrence of v in g_p. The successive-contact lemma e7315cdd5c63 applies to the nonspecial rank-r edge e. Since the later contact v is a terminal vertex of e,
  p-i <= r-2 <= q-2.
Thus i>=p-q+2, so w_e lies in the final q-2 precursor edges
  g_{p-q+2},...,g_{p-1}.
Moreover w_e is not in h, because e and h already share v and H is linear.

The vertices in those q-2 precursor edges that lie outside h form a set of size exactly 2q-4: the segment
  g_{p-q+2},...,g_{p-1},h
has q-1 edges and therefore 2q-1 vertices, of which the three vertices of h are excluded. Distinct edges e,e' in F\{h} receive distinct witnesses w_e,w_e', because both contain v and sharing the witness would violate linearity.

Hence
  |F\{h}|<=2q-4,
and adding the possible last edge h gives
  |F|<=2q-3.

Taking q=phi(v) proves
  t(v)<=2phi(v)-3
when phi(v)>=2. If phi(v)<=1 then no nonspecial edge can have v as a terminal, since rank-one edges are special, giving the max{0,.} formulation.