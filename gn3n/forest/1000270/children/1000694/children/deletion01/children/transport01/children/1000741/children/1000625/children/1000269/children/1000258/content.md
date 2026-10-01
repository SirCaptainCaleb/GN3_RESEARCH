# Persistent noninsertability has a label-independent canonical tail index

## Statement

In the order-four endpoint-triangle configuration of the persistent-noninsertability lemma, write R=(r0,...,r_{h-1}). For each q in Q, apply the canonical choice used in the proof of the failed-insertion normal form to each of the three paths (a,R),(b,R),(c,R). The resulting obstruction index t(q) is identical for all three prefixed labels. If t(q)>=3, the entire first- or second-type obstruction is supported only on q and consecutive vertices of R and is literally the same for all three paths. If t(q)=1 or 2, all label dependence is confined to the initial edge joining the prefix label to r0.

## Body

Fix q in Q and a prefix label w in {a,b,c}. Write the path (w,R) in the indexing of the failed-insertion theorem as
B_w=(b1,...,bm)=(w,r0,r1,...,r_{h-1}),
so m=h+1. Put e_i={b_i,b_{i+1}} and f_i={q,b_i}.

In the proof of the failed-insertion normal form, the obstruction index is chosen canonically as follows: if some t<=m-2 satisfies
f_{t+1} -> e_{t+1},
take the least such t; otherwise take t=m-1.

For every candidate t<=m-2, the two comparison vertices in this test are
f_{t+1}={q,b_{t+1}}, e_{t+1}={b_{t+1},b_{t+2}}.
Since t+1>=2, both b_{t+1} and b_{t+2} lie in the common tail R. Hence the truth value of f_{t+1}->e_{t+1} is independent of the prefix w. The fallback condition that no such t exists is likewise independent of w. Therefore the canonical index t(q) is the same for (a,R),(b,R),(c,R).

Now inspect the two obstruction alternatives at this common index. When t>=3, every path vertex appearing in e_{t-1},e_t,e_{t+1},f_t,f_{t+1} has index at least 2 in B_w and therefore belongs to R. Thus every displayed comparison arc in either obstruction alternative involves only q and vertices of R; the obstruction is identical for all three prefixed paths.

When t=2, the only comparison vertex that can involve w is e_1={w,r0}; all of e_2,e_3,f_2,f_3 are supported on q and R. When t=1, the only prefix-dependent comparison vertices are e_1={w,r0} and f_1={q,w}; the right-feasibility arc f_2->e_2 and all later data are common. Hence all dependence on the choice of a,b,c is confined to the first edge w-r0.

Thus the four vertices of Q do not generate twelve unrelated failed insertions. Each q carries one canonical obstruction location along the shared tail R; except at the first two gaps, its complete bounded obstruction is common to all three label-prefix paths.
