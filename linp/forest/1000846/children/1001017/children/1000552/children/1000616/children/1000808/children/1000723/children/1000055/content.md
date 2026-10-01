# Canonical-entrance cross-blocker reduction for charged four-edge spacing

## Statement

Let e_1,e_2,e_4 be ascending nonspecial edges with common terminal v and ranks q_1<=q_2<=q_4. Let Q=(g_1,...,g_M), M=q_4-1, be the precursor of a longest q_4-edge path Q,e_4 ending at v, and let x_i be the unique entrance of e_i. Assume e_2∩V(Q)={x_2}, and let b be the last index of a Q-edge containing x_2. Assume e_1 is disjoint from V(g_b∪...∪g_M). Let R be a canonical (q_1-1)-edge entrance path for e_1 ending at x_1 and avoiding the two terminal vertices of e_1. If R is disjoint from e_4 and from V(g_b∪...∪g_M), then 2q_2>=q_1+q_4+2.

## Body

Because e_2 is ascending, phi(x_2)=q_2-1. Since e_2∩V(Q)={x_2}, the Q-edges containing x_2 form one block of size at most two. If a is its first index, the prefix g_1,...,g_a can end at x_2, so a<=q_2-1; hence the last index b satisfies b<=q_2. Since e_1 is ascending, deleting e_1 from a longest q_1-edge path ending in e_1 through its unique entrance x_1 gives the canonical R of length q_1-1 ending at x_1 and avoiding both terminal vertices of e_1. Under the stated disjointness assumptions, R,e_1,e_4,g_M,g_{M-1},...,g_b is a linear path: R meets e_1 only at x_1 and avoids its terminals; e_1∩e_4={v}; e_4 meets Q only in g_M; and R and e_1 avoid the reversed tail. The displayed path ends with g_b, and x_2 lies in g_b but not in the preceding edge g_{b+1}, so x_2 can be chosen as its last vertex. Its length is (q_1-1)+2+(M-b+1)=q_1+q_4-b+1. Therefore q_1+q_4-b+1<=phi(x_2)=q_2-1, whence q_1+q_4+2<=q_2+b<=2q_2. The canonical entrance path R avoids both terminal vertices of e_1, which is exactly the source-clean condition needed for the splice above.
