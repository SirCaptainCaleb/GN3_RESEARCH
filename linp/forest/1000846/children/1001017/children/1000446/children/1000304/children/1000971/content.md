# Entrance-rank distortion by blockers

## Statement

Let H be a linear 3-graph. Let e={x,y,z} be a nonspecial edge of rank t=phi(e) with unique entrance x, and let a(x) be the maximum length of a linear path ending physically at x. For any a(x)-edge path P ending at x, let r be the number of edges of P that meet e. Then 1<=r<=3 and a(x)<=r(t-1). In particular a(x)<=3(t-1). If e is nonascending, then r>=2; if a(x)>2(t-1), then r=3, so both terminal vertices y,z occur on P as blockers.

## Body

Proof. Let P=(f_1,...,f_a), where a=a(x), end physically at x. Since x is a terminal vertex of P, x belongs to the last edge f_a and to no earlier edge of P. Thus e meets f_a at x. By linearity, each vertex of e can lie in at most one edge of P, so the set of indices of P-edges meeting e is p_1<...<p_r=a with 1<=r<=3. Put p_0=0. For each j, the contiguous segment f_{p_{j-1}+1},...,f_{p_j} meets e only in its last edge f_{p_j}; hence appending e gives a linear path ending in e of length p_j-p_{j-1}+1. Since phi(e)=t, each gap satisfies p_j-p_{j-1}+1<=t, i.e. p_j-p_{j-1}<=t-1. Summing over j gives a=sum_j(p_j-p_{j-1})<=r(t-1)<=3(t-1). If e is nonascending then a(x)>=t, so r=1 would give a<=t-1, impossible; hence r>=2. If a>2(t-1), then r cannot be at most 2, so r=3. The intersections with P then use all three vertices of e; besides x at f_a, both terminal vertices y and z appear on earlier P-edges, giving two blockers.