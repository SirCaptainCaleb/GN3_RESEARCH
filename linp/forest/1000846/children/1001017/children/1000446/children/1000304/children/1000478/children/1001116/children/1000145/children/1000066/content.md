# Slack-corrected spacing for clean entrance contacts

## Statement

Let e_1,e_2,e_4 be ascending nonspecial edges with common last vertex v and q_i=φ(e_i), where q_1<=q_2<=q_4. Let Q=(g_1,...,g_M) be the precursor of a q_4-edge path ending with e_4 at v, so M=q_4-1 and e_4 meets Q only at its entrance in g_M. Suppose for i=1,2 that e_i meets Q only at its entrance x_i, that x_i lies in exactly one edge g_{j_i}, and j_1+2<=j_2. Put s_i=(q_i-1)-j_i. Then 2q_2>=q_1+q_4+3+s_2-s_1.

## Body

Consider the sequence g_1,...,g_{j_1},e_1,e_4,g_M,g_{M-1},...,g_{j_2}. It is a linear path: the prefix and reversed suffix are separated by at least the omitted edge g_{j_1+1}; e_1 meets Q only in g_{j_1}, e_4 meets Q only in g_M, and e_1∩e_4={v}. Its last edge is g_{j_2}, and x_2 occurs only in that edge, so the path can be ordered with last vertex x_2. Its length is j_1+M-j_2+3 and therefore is at most φ(x_2)=q_2-1, because e_2 is ascending. Substituting M=q_4-1 and j_i=q_i-1-s_i gives the stated inequality.