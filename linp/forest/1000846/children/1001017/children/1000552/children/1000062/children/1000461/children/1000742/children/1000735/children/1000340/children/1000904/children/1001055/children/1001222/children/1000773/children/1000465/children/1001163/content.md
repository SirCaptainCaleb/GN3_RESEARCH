# A clean intersection of crossing balanced endpoint lenses yields two new maximum host-endpoint paths

## Statement

Let P be a maximum p-edge path ending at v. Let two balanced endpoint lenses have crossing host intervals [a,c] and [b,d] with a<b<c<d, and off-host sides A_1 from a to c and A_2 from b to d. Suppose w is a common vertex of A_1,A_2 such that, in each of the two displayed cross-splices, the chosen A_1- and A_2-subsegments meet only at w and are otherwise disjoint from the host pieces they are joined to. Then the two cross-splices
P[start,a] + A_1[a,w] + A_2[w,d] + P[d,v]
and
P[start,b] + A_2[b,w] + A_1[w,c] + P[c,v]
are both maximum p-edge paths ending at v.

## Body

Write alpha=|A_1[a,w]| and beta=|A_2[b,w]|. Since the lenses are balanced, |A_1|=|P[a,c]| and |A_2|=|P[b,d]|. By the stated cleanliness and unique-crossing hypotheses, both displayed cross-splices are linear paths ending at v.

The first cross-splice has length L_1=|P[start,a]|+alpha+(|A_2|-beta)+|P[d,v]|. The second has length L_2=|P[start,b]|+beta+(|A_1|-alpha)+|P[c,v]|. Adding and substituting the balanced lens lengths, all intermediate terms telescope and give L_1+L_2=2p. Maximality of P gives L_1<=p and L_2<=p. Since their sum is 2p, equality holds in both: L_1=L_2=p. Thus every auxiliary intersection satisfying these clean cross-splice conditions generates two new maximum endpoint states.