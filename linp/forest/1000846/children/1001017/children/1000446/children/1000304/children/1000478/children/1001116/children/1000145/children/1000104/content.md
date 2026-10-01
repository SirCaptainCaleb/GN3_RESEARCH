# Cross-blocker reduction for four-edge spacing

## Statement

Let e_1,e_2,e_4 be ascending nonspecial edges with common last vertex v and q_1<=q_2<=q_4. Let Q=(g_1,...,g_M) be the precursor of a q_4-edge path ending with e_4 at v, where M=q_4-1. Let x_i be the entrance of e_i. Suppose e_2∩V(Q)={x_2}; let b be the last index of an edge of Q containing x_2. Suppose also that e_1 is disjoint from V(g_b∪...∪g_M), and that there exists a (q_1-1)-edge path R with last vertex x_1, not using e_1, such that V(R)∩e_1={x_1}, and R is disjoint from e_4 and from V(g_b∪...∪g_M). Then 2q_2>=q_1+q_4+2.

## Body

Because e_2∩V(Q)={x_2}, the edges of Q containing x_2 form one block of size at most two. If its first index is a, then the prefix g_1,...,g_a can be ordered with last vertex x_2, so a<=phi(x_2)=q_2-1. Hence b<=q_2. Now concatenate R,e_1,e_4,g_M,g_{M-1},...,g_b. This is a linear path: R ends at x_1 and by hypothesis meets e_1 only at x_1; e_1∩e_4={v}; e_4 meets Q only in g_M; and the stated disjointness assumptions exclude every other intersection with the reversed tail. The path ends with g_b, and x_2 occurs there but not in g_{b+1}, so it can be chosen as a last vertex. Its length is (q_1-1)+2+(M-b+1)=q_1+q_4-b+1. Therefore q_1+q_4-b+1<=phi(x_2)=q_2-1. Thus q_1+q_4+2<=q_2+b<=2q_2.