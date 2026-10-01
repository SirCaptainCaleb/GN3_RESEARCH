# Separated anchor neighbors force a long interval of order reversals

## Statement

Let F_d=P|Q be an anchor deletion cover with P=(p_1,...,p_m). Let y=p_i and z=p_j, i<j, be two labels whose deletion covers F_y,F_z are each compatible with F_d. Then in F_y the restored label d is inserted into P-y at the reinsertion slot of y or one adjacent slot, and similarly for z. Consequently, for every index t with i+2<=t<=j-2, d precedes p_t in the P-class of F_y while p_t precedes d in the P-class of F_z. In particular, if j-i>=4, F_y and F_z are incompatible and their relative-order disagreement contains the entire interval {p_{i+2},...,p_{j-2}} against the common label d.

## Body

# Proof

Apply the compatible-pair normal form from d43a7c9e2f61 to F_d and F_y. On the common P-support with y removed, the restored labels y and d use equal or adjacent insertion slots.

In the anchor order P, deleting y=p_i creates the reinsertion gap between p_{i-1} and p_{i+1}, with the evident endpoint interpretation. The slot equal to this gap, and its two adjacent slots, all lie between the prefix through p_{i-2} and the suffix beginning at p_{i+2}. Therefore every anchor vertex p_t with t>=i+2 occurs after d in the P-class of F_y. Equivalently d precedes every such p_t.

Likewise, compatibility of F_d and F_z implies that d is restored into P-z at the reinsertion slot of z=p_j or an adjacent slot. All three possible slots lie after every anchor vertex p_t with t<=j-2. Hence every such p_t precedes d in the P-class of F_z.

Thus for each t satisfying i+2<=t<=j-2, the common pair {d,p_t} has opposite relative order in F_y and F_z: d precedes p_t in F_y, while p_t precedes d in F_z.

If j-i>=4, this index interval is nonempty, so F_y,F_z are incompatible. More strongly, the disagreement is not confined to one local triple: it reverses d against every anchor vertex in the displayed interval from p_{i+2} through p_{j-2}.
