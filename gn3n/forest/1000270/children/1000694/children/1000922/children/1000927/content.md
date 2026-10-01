# Every deletion-cover anchor forces near-total support crossings or anchor-centered order disagreement

## Statement

Let H be a boundary tournament with pc(H)>2. Let D be a set of m>=4 deletion labels, choose one two-cover F_d of H-d for each d in D, and fix an anchor x in D with F_x=P|Q.

Let C be the full-compatibility graph on D. The neighbors of x split canonically into two classes N_P,N_Q according to the common support class into which x is inserted in the neighboring cover; write p=|N_P| and q=|N_Q|.

For each S in {N_P,N_Q}, every pair of labels in S is support-compatible. The full-compatibility graph induced by S is triangle-free. Hence S contains at least floor((|S|-1)^2/4) support-compatible but order-incompatible pairs. Moreover every such order disagreement is centered at x: the two covers agree on the relative order of every common pair not involving x, so some common vertex t is ordered on opposite sides of x in the two path orders.

Consequently the anchor x satisfies the quantitative tradeoff
number of support-incompatible covers relative to F_x = m-1-p-q,
while the two compatible side-classes contain at least
floor((p-1)^2/4)+floor((q-1)^2/4)
anchor-centered order-incompatible pairs.

In particular, for every prescribed anchor x, either at least m-5 other covers are support-incompatible with F_x and therefore have the fixed-cut crossing witness of 1000922, or there exist two covers, both fully compatible with F_x and assigned to the same anchor side, that are support-compatible but order-incompatible with disagreement necessarily involving x.

## Body

Fix x and write F_x=P|Q. Let y be fully compatible with x. By the compatible-pair localization in 1000694, when F_x and F_y are compared on H-{x,y}, the omitted vertices x and y restore into the same common support class; restoring them into different classes would give a spanning two-cover of H. Thus each neighbor y of x is assigned canonically to the P-side or Q-side. Let these classes be N_P and N_Q.

Take distinct y,z in N_P. Because F_y is fully compatible with F_x, on the common vertex set V(H)-{x,y} it has the same support partition and relative orders as F_x. Since y lies on the P-side, the support of F_y containing x is the P-side with y omitted and x restored, while Q is the other support. The same is true for F_z. Therefore, on V(H)-{y,z}, the two covers F_y and F_z induce the same two support classes:
((P-{y,z}) union {x}) | Q.
Hence F_y and F_z are support-compatible. The same argument applies inside N_Q.

Now consider the full-compatibility graph induced by N_P. It is triangle-free. Indeed, if y,z,w in N_P were pairwise fully compatible, then x,y,z,w would be four pairwise fully compatible deletion covers. The four-cover gluing theorem in 1000694 would then produce a spanning two-cover of H, contradicting pc(H)>2. Thus Mantel's theorem gives at most floor(p^2/4) full-compatibility edges inside N_P. Every remaining pair in N_P is already known to be support-compatible, so it is support-compatible but order-incompatible. Therefore N_P contains at least
binom(p,2)-floor(p^2/4)=floor((p-1)^2/4)
order-incompatible pairs. Likewise N_Q contains at least floor((q-1)^2/4).

These disagreements are positioned at x. Take y,z in N_P that are support-compatible but order-incompatible. On Q, both covers agree in relative order with F_x, because Q survives both pairwise comparisons with the anchor. On the common vertices P-{y,z}, both covers also agree in relative order with F_x: full compatibility of F_y with F_x fixes every pair not involving x or y, and full compatibility of F_z with F_x fixes every pair not involving x or z. Hence F_y and F_z agree on every common pair not involving x. Since they are order-incompatible, some common vertex t must therefore satisfy opposite relative orders with x in the two anchor-side path orders. Equivalently, the two neighboring covers place x at different insertion cuts of the inherited anchor-side order. The same reasoning applies inside N_Q.

Finally, x has exactly m-1-p-q nonneighbors in the full-compatibility graph. A nonneighbor is either support-incompatible or support-compatible but order-incompatible. But if p+q<=4, then x has at least m-5 nonneighbors; any nonneighbor that is support-incompatible has the fixed-cut crossing witness of 1000922, while any support-compatible nonneighbor already gives order disagreement. If p+q>=5, one of p,q is at least three, and the preceding triangle-free argument gives an anchor-centered support-compatible order-incompatible pair among neighbors of x. Thus for every prescribed anchor, either at least m-5 support-incompatible crossing covers occur, or an anchor-centered order-disagreement pair occurs among covers individually fully compatible with the anchor. The quantitative count above records both phenomena simultaneously.