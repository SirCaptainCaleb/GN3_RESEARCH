# Correct terminal-blocker localization in Class III

## Statement

In the Class-III maximum-rank setup P=(g_1,g_2,g_3,g_4,e), e={x,y,z}, put W=V(P)\e and E=W∩V(g_1∪g_2). For any edge h≠e through a terminal y or z, either h has a contact in E, or h is the unique single blocker using the outside vertex o and its sole W-contact lies in g_4\e. In particular no terminal edge can have its first precursor contact in g_3, and a terminal with four double blockers has no L-L blocker pair except possibly a pair whose earlier contact is already in E; the only completely late exceptional contact is the penultimate single blocker.

## Body

Fix a terminal v∈{y,z} and an edge h≠e through v.

If h avoids g_1 and g_2 but meets g_3, then
g_1,g_2,g_3,h,e
is a five-edge linear path ending in e through v: h is disjoint from g_1,g_2 by assumption, g_3 is disjoint from e because it is nonconsecutive to e in P, and h∩e={v}. This contradicts nonspecialness of e, whose unique longest-path entrance is x. Therefore a terminal edge with no contact in g_1∪g_2 cannot meet g_3.

Every terminal edge must meet the longest path P in a second vertex besides v. Otherwise it would meet P only at the last vertex v and could be appended after e, producing a six-edge linear path. Hence an edge h with no contact in g_1∪g_2 must meet g_4.

Because it avoids g_1,g_2,g_3 and meets g_4 in only one vertex by linearity, its other non-v vertex cannot lie on P. There is only one vertex o outside P. Thus such an edge has the form
h={v,o,s}
with s∈g_4\e.

It is the unique single blocker through v, since two v-edges using o would share the pair {v,o}.

Therefore every terminal edge either has an early contact in
E=W∩V(g_1∪g_2),
or is this unique penultimate single blocker {v,o,s} with s∈g_4\e.

This is the correct path-relative localization. It deliberately retains the genuine j=p-1 exception from the certified two-contact competitor lemma 0a5cb0d55cbd; no claim is made that the exceptional blocker can be rotated into a second entrance for e without additional hypotheses.