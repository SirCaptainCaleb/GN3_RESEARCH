# A flat transfer cycle has no clean second-private ear and forces a target-preserving maximum rotation

## Statement


In an entrance-joint equal-rank flat-transfer q-cycle C=(h_1,...,h_{q-2},e,f), let x=f∩h_1 be the unique entrance of target f and let p be the private vertex of h_2. No noncycle edge through p is clean relative to C. In minimum degree q, p therefore has a one-contact ear; relative to P=(h_2,...,h_{q-2},e,f), it in fact has at least two single blockers, one with blocker different from x. Such a blocker gives a nontrivial (q-1)-edge maximum x-ending rotation that still ends with f.


## Body


If an edge a through p met C only at p, then
  a,h_2,h_3,...,h_{q-2},e,f
would be a q-edge path ending in f through y=e∩f. But y is terminal for the nonspecial rank-q target f, contradicting its unique entrance. Hence there is no clean ear through p. The q-cycle mobile-ear inequality then forces a noncycle edge with exactly one additional cycle contact.

More directly relative to P=(h_2,...,h_{q-2},e,f), no edge through p can be clean: the same concatenation would again enter f through forbidden terminal y. Let S,D count single- and double-blocking edges through p other than h_2. Minimum degree gives S+D>=q-1, while their blocker vertices are disjoint inside V(P) minus h_2, which has size 2q-4; hence S+2D<=2q-4 and therefore S>=2. By linearity at most one single blocker uses x. Choose one with blocker w≠x. The endpoint-preserving single-blocker rotation produces another (q-1)-edge path P' ending at x. Because the new blocker edge avoids x, the only path edge containing x remains f, so f is still the last edge. Since phi(x)=q-1, P' is another maximum x-ending witness. Thus every entrance-joint flat transfer has internal rotational mobility while preserving its target edge.
