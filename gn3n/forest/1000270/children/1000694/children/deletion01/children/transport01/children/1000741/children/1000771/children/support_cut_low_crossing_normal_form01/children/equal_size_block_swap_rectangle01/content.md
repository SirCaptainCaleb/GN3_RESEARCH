# Equal-size low-cut support swaps are switch rectangles or have three reverse cuts

## Statement

Let F=P|Q and G=A|B be support-incompatible two-covers of the same vertex set, with |P|=|Q|=p, and suppose Phi(G)=Phi(F) and the support-cut count of G along the displayed paths P,Q is less than three. Then support_cut_low_crossing_normal_form01 implies that their support partitions differ by exchanging equal-order terminal blocks.

Apply the support-cut count in the reverse direction, along the displayed paths A,B with respect to the F-support partition. Then either this reverse count is at least three, or it equals two with one cut on each of A,B. In the latter case, if the displayed orders of F and G have no order disagreement on any common block, there are nonempty tight subpaths L,X,Y,R such that
P=(L,X),  Q=(Y,R),
the G-supports are L union Y and X union R,
|L|=|R|,  |X|=|Y|,
and the displayed G-orders are one of (L,Y),(Y,L) on the first support and independently one of (X,R),(R,X) on the second, with every block carrying its inherited F-order.

The same support swap can be described by exchanging X,Y or by exchanging L,R. Choose the description with exchanged-block order s=min(|X|,|L|)<=p/2. If s=1, the swap is a terminal singleton swap. If s>=2, all four blocks have order at least two, and each displayed G-order splices with the adjacent displayed F-join to give a tight path on three of the four blocks: the first G-component yields either (L,Y,R) or (Y,L,X), and the second yields either (L,X,R) or (Y,R,X).

Consequently, in a minimum counterexample, if F|D and G|D occur as spanning three-covers with the same unchanged third path D, every non-singleton low-cut equal-size equal-Phi swap with fewer than three reverse cuts and no order disagreement produces two positioned Hamiltonian supports on three blocks, each having non-Hamiltonian path-cover-two complement. Thus the equal-size low-cut equal-Phi swap residue reduces to three reverse support cuts, order disagreement, a terminal singleton swap, or two explicit three-block Hamiltonian-support outputs.

## Body

Because |P|=|Q|=p, F and G have the same quadratic contribution whenever G also has component orders p,p. The hypothesis that G is support-incompatible with F and has fewer than three support cuts along P,Q lets us apply support_cut_low_crossing_normal_form01. In the equal-size case its low-cut classification has only one possibility: an exchange of equal-order terminal blocks. Hence, after choosing the two cut positions and naming the four nonempty contiguous F-blocks,
P=(L,X),  Q=(Y,R),
the unordered G-support partition is
{L union Y, X union R},
and necessarily |L|=|R| and |X|=|Y|.

Now count support cuts in the reverse direction: color the vertices along the displayed G-paths A,B by their F-support P or Q. If the reverse count is at least three, we are done. Suppose it is less than three. Since each G-support L union Y and X union R meets both F-supports, neither A nor B is monochromatic in this coloring. Thus each of A,B has at least one reverse support cut, so the total reverse count is exactly two and there is one cut on each path.

Equivalently, each displayed G-path consists of its two F-intersection blocks consecutively. If one of those blocks appears in an order different from its inherited order in P or Q, the two displayed paths exhibit order disagreement on common vertices. Excluding that outcome, the G-orders are exactly
(L,Y) or (Y,L)
and
(X,R) or (R,X),
with the inherited block orders.

There are two equivalent descriptions of the same support switch. The displayed partition
{L union X, Y union R} -> {L union Y, X union R}
may be viewed as exchanging X and Y, of common order t=|X|=|Y|, or as exchanging L and R, of common order p-t. Relabel the four blocks using the description with
s=min(t,p-t)<=p/2.
If s=1, this is a terminal singleton swap. Assume s>=2. Then both the exchanged blocks and their complementary blocks have order at least two, so all four blocks L,X,Y,R have order at least two.

Consider the first G-path. If its order is (L,Y), then the join L->Y is certified by G while the join Y->R is certified by Q=(Y,R). Because the middle block Y has at least two vertices, every consecutive triple of (L,Y,R) is inherited from one of those two tight paths; hence (L,Y,R) is tight. If instead the first G-order is (Y,L), combine its join Y->L with the F-join L->X from P=(L,X). Since |L|>=2, (Y,L,X) is tight.

The second G-path is identical. If it is (X,R), combine L->X from F with X->R from G to obtain the tight path (L,X,R), using |X|>=2. If it is (R,X), combine Y->R from F with R->X from G to obtain (Y,R,X), using |R|>=2.

Thus the two displayed G-components independently generate two tight three-block paths, each omitting exactly one of the four blocks.

For the minimum-counterexample corollary, suppose F|D and G|D are spanning three-covers of H. Let T be either generated three-block path and let Z be the omitted block. Then H-T is covered by the two tight paths Z and D, so pc(H-T)<=2. The support T is nonempty and proper. If H-T were Hamiltonian, a Hamilton path on T together with one on H-T would two-cover H, impossible. Hence H-T is non-Hamiltonian with path-cover number exactly two. This applies to both generated three-block paths.
