# Corrected fixed-hole two-chord bridge

## Statement

Let P=(p_1,...,p_s) be a linear 3-graph path with last vertex x, and let b notin V(P). Let f_1,f_2 be distinct edges through b such that each f_r meets V(P) in exactly one vertex w_r and its third vertex lies outside V(P) union {b}. Let j be the first index of a path edge containing w_1 and k the last index of a path edge containing w_2. Assume j+2<=k and w_2!=x. Then (p_1,...,p_j,f_1,f_2,p_k,...,p_s) is a linear path with last vertex x and length s+3-(k-j). In particular, if s=q-2 and k-j=2, this is a (q-1)-edge path ending at x.

## Body

The linearity verification is the same as in the failed predecessor f762f44ddb18. The first-contact choice of j ensures that f_1 meets the retained prefix only in p_j; any second occurrence of w_1 can only be in p_{j+1}, which is omitted. The last-contact choice of k gives the symmetric statement for f_2 and the retained suffix. The two bridge edges meet exactly in b, their external third vertices are distinct by linearity, and p_j,p_k are disjoint because k>=j+2. Thus the displayed edge sequence is linear. Its length is j+2+(s-k+1)=s+3-(k-j). Finally w_2!=x guarantees that x is not the joint f_2 cap p_k. Since x was a last vertex of P, it occurs only in p_s; the retained suffix still ends with p_s and x remains a last vertex. The omitted hypothesis w_2!=x is exactly the defect identified in the audit failure of f762f44ddb18.
