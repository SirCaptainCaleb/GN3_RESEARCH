# Long deletion components reduce to reversal, one-label replacement, or strict quadratic descent

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion cover with P of order at least six. Then at least one of the following occurs: (1) H contains a genuine reversing tight triple on a displayed edge of P or on a proper bounded tight cycle or a complementary two-cover path arising inside V(P) union {x}; (2) for some internal vertex p of P, H-p has a deletion cover P'|Q obtained by replacing p with x in the inherited order of P while leaving Q unchanged; (3) H has a spanning three-cover admitting an explicit strict quadratic-potential decrease.

## Body

For each i=0,...,m-5 let W_i=(p_i,p_{i+1},p_{i+2},p_{i+3},p_{i+4}). The omitted vertex x cannot be inserted into the full displayed order P, since then the resulting Hamilton path together with Q would two-cover H.

If x is noninsertable into some W_i, acdec36ae3ca gives a tight triple reversing a displayed edge of W_i, hence of P, and outcome (1) holds. Thus assume x is insertable into every W_i. A successful insertion in one of the two middle gaps of W_i would also insert x at the same position in the full path P, impossible. Hence each W_i admits a successful insertion only in a left gap or a right gap. The first window cannot use a left gap and the last cannot use a right gap, so for some consecutive windows W_i,W_{i+1}, the first has a right insertion and the second a left insertion. On their common four-path B=(p_{i+1},p_{i+2},p_{i+3},p_{i+4}), 0d2a8a61c45a gives either a short tight cross (p_j,x,p_k) with 1<=k-j<=3, or a vertex-simple tight cycle consisting of x and the inherited interval from p_j to p_k.

In the cycle case, the cycle is proper because Q is nonempty and disjoint from it. Applying f21cfb4840ff gives a tight triple reversing either a displayed cycle edge or an edge of a complementary two-cover path, so outcome (1) holds.

In the short-cross case, apply f05c3c78500c. A neighboring displayed-edge reversal gives outcome (1). If k=j+2 and both boundary joins are tight, deleting p_{j+1} and replacing it by x in inherited order gives a deletion cover P'|Q of H-p_{j+1}, which is outcome (2). If k=j+3 and both boundary joins are tight, deleting the consecutive pair p_{j+1},p_{j+2} gives a two-cover P'|Q after replacing that pair by x, and restoring the deleted pair as its own two-vertex path yields a spanning three-cover P'|Q|(p_{j+1},p_{j+2}). Since |P|>=6, |P'|>=5; twosidedescent4 applied to the two-vertex side and P' gives a legal pairwise repartition with strict quadratic-potential decrease, which is outcome (3). For k=j+1 only the reversal alternative can occur.

These cases exhaust all possibilities.