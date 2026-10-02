# Terminal nonspecial saturation forces double-blocker excess

## Statement

Let H be a finite linear 3-graph, let v have p=phi(v), and choose a maximum p-edge path P=(g_1,...,g_p) with last vertex v and last edge h=g_p. Let t(v) be the number of nonspecial edges for which v is a terminal. Let D(v) count those such edges e!=h for which both vertices of e\\{v} lie in V(P)\\h. If p>=3, then t(v)-D(v)<=2p-4. (For p=2 one has t(v)<=1.)

## Body

For p=3 the conclusion follows immediately from the certified localized rank-3 special-edge lemma da65f29a0916, which gives t(v)<=2=2p-4. Assume henceforth p>=4.

Let F be the family of nonspecial edges for which v is terminal. As in 0e550ff0eadd, every e in F\{h} has a distinct latest blocker w_e in the set
  S=(V(g_2 union ... union g_{p-1}))\h,
and |S|=2p-4.

If h is not in F, this injection already gives
  t(v)<=2p-4,
hence t(v)-D(v)<=2p-4.

Now suppose h is in F. Since P has length p and ends in h at the terminal v, phi(h)=p. Let x=g_{p-1} intersect h be the unique entrance of the nonspecial edge h.

Inside S consider the two vertices
  C = g_{p-2}\g_{p-3}
that are last vertices of the prefix g_1,...,g_{p-2}: namely the private vertex of g_{p-2} and the forward joint g_{p-2} intersect g_{p-1}. Thus |C|=2.

We claim that whenever w_e lies in C, the edge e must be double-blocking on P, i.e. counted by D(v). Suppose instead that e has only the single blocker w_e on P outside h. Because w_e is a last vertex of the prefix g_1,...,g_{p-2}, the sequence
  g_1,...,g_{p-2}, e, h
is a linear p-edge path: e meets the prefix only at w_e, e meets h only at v by linearity, and h is disjoint from g_1,...,g_{p-2}. This p-edge path ends in h but enters h through v. The original path P enters h through x!=v. Thus h has two distinct longest-path entrance labels and is special, contradicting h in F. Hence every assignment into C is double-blocking.

There are t(v)-1 injected blockers w_e in S, and S\C has size 2p-6. Therefore at least
  max(0,t(v)-1-(2p-6)) = max(0,t(v)-2p+5)
of the corresponding edges are counted by D(v). Hence
  D(v)>=max(0,t(v)-2p+5).
If t(v)<=2p-5 then trivially t(v)-D(v)<=2p-5<2p-4. If t(v)>=2p-4, the displayed bound gives
  t(v)-D(v)<=2p-5.
Thus in fact the h in F case satisfies the slightly stronger t(v)-D(v)<=2p-5, and the universal p>=4 bound is
  t(v)-D(v)<=2p-4.

For p=2, the cumulative terminal bound 0e550ff0eadd gives t(v)<=1.