# Every two deep-central deletions force three crossings or explicit order disagreement

## Statement


Let H be a minimum counterexample with lexicographically maximal spanning three-cover A|B|C, decreasing component orders a>=b>=c>=2, gap g=a-(b+c), and deep-central interval J={i:max(g,2)<=i<=min(a-g-1,a-3)}. Every block-faithful exact cover of H-a_i with i in J is automatically clean: after naming {P,Q}={B,C}, it has block order L_i P | Q R_i. Hence adjacent indices in J cannot both be block-faithful. Consequently every two consecutive indices in J contain an index i such that every exact two-cover of H-a_i has either at least three ordinary edges joining distinct members of L_i|R_i|B|C, or relative-order disagreement on an inherited support, yielding a reversed common edge, reversing tight triple, or vertex-simple tight cycle.


## Body


# Every two deep-central deletions force three crossings or explicit order disagreement

Let
A=(a_0,...,a_{a-1}) | B | C
be a lexicographically maximal spanning three-cover of a minimum counterexample H, with decreasing component orders a>=b>=c>=2. Put
g=a-(b+c),
L_i=A[0,i-1],
R_i=A[i+1,a-1],
and define the deep-central interval
J={i : max(g,2)<=i<=min(a-g-1,a-3)}.

The strict-majority/maximal-path theorem makes A a globally longest tight path.

Fix i in J and suppose H-a_i has a block-faithful exact two-cover: each of L_i,R_i,B,C remains one contiguous block in its displayed order. The central block-faithful theorem forces a cross-pairing. After naming {P,Q}={B,C}, the component supports are
L_i union P
and
R_i union Q.

We now determine their block directions. Since i>=2, L_i begins with a_0,a_1. If the first component had order P L_i and p were the terminal vertex of P, tightness would give
(p,a_0,a_1)
tight. Then
(p,a_0,a_1,...,a_{a-1})
would be a tight path of order a+1, contradicting global maximality of A. Therefore the first component has block order
L_i P.

Similarly i<=a-3, so R_i contains a_{a-2},a_{a-1}. If the second component had order R_i Q and q were the initial vertex of Q, tightness would give
(a_{a-2},a_{a-1},q)
tight, extending A to order a+1. Hence the second component has block order
Q R_i.

Thus every deep-central block-faithful state is clean. The clean-deletion sparsity theorem says adjacent clean positions are impossible, so no two adjacent indices in J are both block-faithful.

Take two consecutive indices in J. At least one, say i, is not block-faithful. Consider any exact two-cover T of H-a_i. For each inherited support
X in {L_i,R_i,B,C},
let b_X be the number of T-blocks contained in X, and let t be the number of ordinary T-edges joining different inherited supports.

Cutting all such crossing edges from the two-component forest leaves exactly
sum_X b_X
blocks, so
t=sum_X b_X-2.

If some inherited support is split, then some b_X>=2. Since all four supports are nonempty, sum_X b_X>=5 and therefore
t>=3.

Otherwise every b_X=1: each inherited support is one contiguous Hamilton block of T. Since i is not block-faithful, at least one block has a different relative order from its displayed inherited path. Path restriction/intersection calculus then yields an explicit order-disagreement witness: a reversed common edge, a reversing tight triple, or a vertex-simple tight cycle.

Therefore every pair of consecutive deep-central positions contains an index i for which every exact deletion cover of H-a_i has either at least three four-part crossing edges or explicit inherited-order disagreement.
