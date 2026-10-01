# Uniform order incompatibility localizes to three transport intervals

## Statement

In the common-core-order branch of compattripletransport13, let L=(r_1,...,r_m) be the common order on R=X-{a,b,c}. For each special label x in {a,b,c}, let i_x<j_x be its two distinct insertion gaps in the two deletion paths that contain x. Then the set of core vertices whose relative order with x differs between those two paths is exactly I_x={r_{i_x+1},...,r_{j_x}}, a nonempty interval of L. Consequently every pairwise order incompatibility in the triple is carried by one special label against one contiguous core interval, and the three-cover residue is encoded by three nonempty transport intervals I_a,I_b,I_c on the same linearly ordered core.

## Body

# Proof

Use the notation of compattripletransport13. The three deletion paths P_a,P_b,P_c restrict to one common linear order
L=(r_1,...,r_m)
on R.

Fix a special label x. Exactly two of the three deletion paths contain x; call them P and P'. By the common-core-order branch, P is obtained from L by inserting x in some gap i_x, while P' is obtained from L by inserting x in a different gap j_x. Relabel the two paths so i_x<j_x.

For a core vertex r_t, its relative order with x in an insertion at gap i is determined solely by whether t<=i or t>i: vertices at positions at most i precede x, and vertices after i follow x.

Therefore r_t has opposite relative order with x in the two paths exactly when
i_x < t <= j_x.
These are precisely the consecutive core vertices
r_{i_x+1},...,r_{j_x}.

Because the two insertion gaps are distinct, this interval is nonempty.

No pair of core vertices changes relative order, since all three paths restrict to L. And in the common domain of the two covers containing x, the only special label present outside R is x itself. Hence this interval accounts for the entire order incompatibility of that pair.

Applying the same argument to a,b,c gives three nonempty transport intervals on the same ordered core.