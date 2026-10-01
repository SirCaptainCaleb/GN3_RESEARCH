# A Type-A saturated rank-minus-one fan has at least p minus five genuine early private rotations

## Statement

In the setting of 4c0a0105c825, let v be Type A with p=phi(v)>=5, choose a rank-(p-1) nonspecial terminal edge h through v, and let
  P=(g_1,...,g_{p-1}=h)
be a longest path ending in h at physical terminal v. Put
  W=V(P)\h,
  C=g_{p-3}\g_{p-4}.

Among the other 2p-6 nonspecial terminal edges through v, at least p-4 are single-blocking on P whose unique W\C contact is a private/free vertex of its path edge. At most one of these has that contact on g_{p-2}; consequently at least
  p-5
have a private/free unique precursor contact on one of
  g_1,...,g_{p-4}.

For each such early private-contact edge f, f meets P in exactly two path edges: its contact edge g_j and the last edge h, so the certified two-contact Posa rotation applies.

## Body

By 4c0a0105c825, the 2p-6 edges f!=h have distinct singleton designated contacts that partition W\C; at most two of these edges have an additional contact in C.

We count the types of vertices in W\C. For the (p-1)-edge 3-uniform linear path P, after deleting the final edge h, W consists of:
- p-1 private/free vertices: the two free vertices of g_1 and one private vertex from each g_2,...,g_{p-2};
- p-3 path joints not belonging to h.
The excluded two-vertex cell
  C=g_{p-3}\g_{p-4}
consists of the private vertex of g_{p-3} and the joint g_{p-3}∩g_{p-2}.
Hence W\C contains exactly
  p-2 private/free vertices
and
  p-4 joints.

Each of the p-2 private/free vertices is the designated W\C contact of a distinct edge f. At most two f in the entire fan have an additional C-contact. Therefore at least
  (p-2)-2=p-4
of the edges assigned to private/free vertices have no additional contact: they are genuinely single-blocking, and because their contact vertex is private/free they meet exactly one precursor path edge.

Among the private/free vertices of W\C, only one lies on g_{p-2}, namely the private vertex of g_{p-2}; none lies on g_{p-3}, whose private vertex was removed in C. Thus at most one of these p-4 genuine private single blockers is penultimate, leaving at least
  p-5
with contact edge g_j for j<=p-4.

For such an edge f, its unique precursor contact is private/free on g_j and it also meets the last edge h at the common terminal v. It has no other P-contact. Hence f meets P exactly in g_j and h, and the hypotheses of the certified two-contact rotation lemma a51a7f9cff95 apply.
