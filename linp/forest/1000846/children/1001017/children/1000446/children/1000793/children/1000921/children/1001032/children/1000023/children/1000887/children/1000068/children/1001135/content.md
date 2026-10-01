# At density-plus-one equality every maximum endpoint path has a special last edge

## Statement

Assume equality in c77c818cf1e9. Then for every vertex v with p=phi(v), every maximum p-edge path ending at v has a special last edge.

Moreover, relative to every such maximum path P=(g_1,...,g_p) with special last edge h=g_p:
- all 2p-4 nonspecial terminal edges through v are single-blockers on P and their blocker witnesses biject exactly onto
  (V(g_2 union ... union g_{p-1}))\V(h);
- the two special edges through v other than h meet P outside v exactly at the two free vertices of g_1, one each.

## Body

Equality in c77c818cf1e9 gives for every v
  b(v)=(2p-1)-d_D^-(v)=0
and
  t_ns(v)=2p-4.

Fix an arbitrary maximum p-edge path P ending at v. Let B_v be the chosen-path double-blocker count from 3a0d8866aba9. Since
  d_D^-(v)+B_v<=2p-1
and d_D^-(v)=2p-1, we must have B_v=0. In particular the nonspecial-terminal double-blocker count D(v) of 672725540541 is zero.

If the last edge h were nonspecial with v terminal, then the stronger h-in-F conclusion in 672725540541 would give
  t_ns(v)-D(v)<=2p-5.
But here t_ns(v)=2p-4 and D(v)=0, contradiction. Thus h cannot be nonspecial terminal.

Every maximum endpoint path has a snake-incoming last edge at v by definition, and a nonspecial incoming edge at v would make v one of its terminals. Hence h must be special.

Now apply the special-last case of 1080210bcf37. Since h is special, all 2p-4 nonspecial terminal edges inject bijectively into the tail set, while the two remaining special edges through v occupy the two far free vertices. Because B_v=0, every nonspecial terminal edge is a single-blocker, proving the refined statement.
