# The mixed p=4 charged obstruction is impossible

## Statement

If phi(v)=4, four potential-charged ascending nonspecial edges through v cannot have ordered ranks (3,4,4,4).

## Body

Assume for contradiction that e={x,v,u} has rank 3 and f_1,f_2,f_3 are the three rank-4 charged edges through v.

By 2dbfe112a0fe, phi(x)=2 and x is the middle joint of every maximum four-edge path ending at v with v as a last vertex. For each i choose a longest path
P_i=(A_i,B_i,C_i,f_i)
ending in f_i with last vertex v. Then
x=B_i∩C_i.
Since f_i is nonspecial of rank four, C_i∩f_i={a_i}, where a_i is the unique entrance of f_i. In particular a_i≠v. Also x∉f_i: otherwise f_i and e would share both x and v.

We claim that for every ordered pair i≠j, f_i meets C_j.

Suppose f_i∩C_j=∅. The three edges
f_i,f_j,C_j
then form a linear path. The first two meet exactly at v because distinct edges through v are linear. The last two meet at the entrance a_j. The nonconsecutive pair f_i,C_j is disjoint by assumption, and v≠a_j. The last edge C_j contains x, while x∉f_j, so this three-edge path can end at x with x as a last vertex. Hence phi(x)>=3, contradicting phi(x)=2.

Thus every f_i meets every C_j.

Now consider the three edges C_1,C_2,C_3, all containing x.

If they are pairwise distinct, then any two meet exactly at x. Fix f_1. It meets each C_j. None of these intersections is x, because x∉f_1. Moreover the three intersection vertices are distinct: if f_1 met two distinct C_j,C_k in the same vertex w, then C_j and C_k would share both x and w, violating linearity. Therefore f_1 has three distinct vertices away from v, impossible for a 3-uniform edge, which has only two vertices besides v.

Hence two of the C_j coincide; say C_2=C_3=C. Since f_2 and f_3 both share v, their entrance contacts
a_2=C∩f_2,  a_3=C∩f_3
are distinct, else f_2,f_3 would share both v and that entrance. Therefore
C={x,a_2,a_3}.

But f_1 must meet C. It cannot contain x, so it contains a_2 or a_3. If it contains a_2, then f_1 and f_2 share both v and a_2; if it contains a_3, then f_1 and f_3 share both v and a_3. Either violates linearity.

This contradiction excludes the rank pattern (3,4,4,4).