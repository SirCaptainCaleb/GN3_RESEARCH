# Two fixed-hole one-contact chords give an exact bridge splice

## Statement

Let P=(p_1,...,p_s) be a linear 3-uniform path ending at x, and let b notin V(P). Let f_1,f_2 be distinct edges through b such that f_r meets V(P) in exactly one vertex w_r, and its third vertex lies outside V(P)∪{b}. Assume w_2≠x. Let j be the first index of a path edge containing w_1, and let k be the last index of a path edge containing w_2. If j+2<=k, then (p_1,...,p_j,f_1,f_2,p_k,...,p_s) is a linear path ending at x of length s+3-(k-j). In particular, if s=q-2 and k-j=2, this produces a (q-1)-edge path ending at x.

## Body

Because f_1 meets V(P) only in w_1 and j is the first path-edge index containing w_1, no retained prefix edge before p_j contains w_1. If w_1 is also contained in the consecutive edge p_{j+1}, that edge lies in the omitted middle segment. Hence f_1 meets the retained prefix only in p_j and is disjoint from the retained suffix. Similarly, because k is the last path-edge index containing w_2, if w_2 is also contained in p_{k-1}, that edge lies in the omitted middle segment; thus f_2 meets the retained suffix only in p_k and is disjoint from the retained prefix. The two bridge edges f_1,f_2 intersect exactly in b by linearity. Since k>=j+2, p_j and p_k were nonconsecutive in P and are therefore disjoint. All remaining nonconsecutive intersections are absent by the one-contact hypotheses or inherited from P. Thus the displayed sequence is linear. Because w_2≠x and f_2 meets P only at w_2, the terminal vertex x of P is not used by f_2; hence x remains a last vertex of the final edge p_s, so the new path ends at x. Its edge count is j+2+(s-k+1)=s+3-(k-j). For s=q-2 and k-j=2 this equals q-1.
