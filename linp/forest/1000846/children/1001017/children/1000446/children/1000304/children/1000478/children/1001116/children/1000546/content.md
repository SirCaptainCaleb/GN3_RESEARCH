# Geometric spacing for clean ascending attachments to one path

## Statement

Let H be a linear 3-graph and P=(g_1,...,g_M) a linear path with last vertex v. Let f_1,...,f_r be distinct ascending nonspecial edges not in P, all having v as a last vertex. Suppose that for each i there is a vertex x_i in f_i\{v} and an index j_i<M such that (a) x_i lies in exactly one edge of P, namely g_{j_i}; (b) f_i∩V(P)={v,x_i}; (c) x_i is the unique entrance of f_i; and (d) φ(x_i)=j_i and φ(f_i)=j_i+1. Write j_1<...<j_r. Then any subfamily whose attachment indices have pairwise gaps at least two satisfies, for consecutive selected indices i-1<i below the last selected attachment j_r, the recurrence j_r-j_{i-1} >= 2(j_r-j_i)+3. Consequently the size of such a subfamily is O(log M), and hence r=O(log M).

## Body

Proof. It is enough to prove the recurrence for attachment indices j_{i-1}<j_i<j_r with j_i-j_{i-1}>=2. Consider the sequence

g_1,...,g_{j_{i-1}}, f_{i-1}, f_r, g_{j_r}, g_{j_r-1},...,g_{j_i}.

This is a linear path. Indeed, the prefix and the reversed suffix are separated in P by at least one omitted edge, so no edge of the prefix meets an edge of the suffix. By the hypotheses f_{i-1} meets P only at x_{i-1} and v, while f_r meets P only at x_r and v; hence the only consecutive intersections introduced are g_{j_{i-1}}∩f_{i-1}={x_{i-1}}, f_{i-1}∩f_r={v}, and f_r∩g_{j_r}={x_r}. All other nonconsecutive intersections are absent by linearity and the single-contact hypotheses. The path ends in g_{j_i}, and because x_i lies only in g_{j_i}, its final edge may be ordered with last vertex x_i.

Its length is j_{i-1}+2+(j_r-j_i+1)=j_{i-1}+j_r-j_i+3. Since φ(x_i)=j_i, this length is at most j_i. Therefore

2j_i >= j_{i-1}+j_r+3,

or equivalently

j_r-j_{i-1} >= 2(j_r-j_i)+3.

Let D_i=j_r-j_i. Repeatedly applying the recurrence gives geometric growth of the deficits when moving leftward: D_{i-1}>=2D_i+3. Thus a selected subfamily of size s has j_r>=c 2^s for an absolute c>0, and so s=O(log M). Finally, among the original attachment indices j_1,...,j_r, one parity class contains at least ceil(r/2) indices; those indices differ by at least two, so applying the preceding bound to that parity subfamily yields r=O(log M).

The path-plus-clique family d5e0ab668a51 essentially attains equality in the recurrence D_{i-1}=2D_i+3, showing that the geometric mechanism is sharp in this clean single-contact setting.
