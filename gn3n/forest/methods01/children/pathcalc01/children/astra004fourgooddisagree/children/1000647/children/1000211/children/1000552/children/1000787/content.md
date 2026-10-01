# A tight-cycle support with pc-two complement forces a reverse obstruction at every cyclic cut

## Statement

Let H be a boundary tournament with pc(H)>2. Let C=(c_0,...,c_{k-1}) be a vertex-simple tight cycle, indices modulo k, and suppose the proper complement H-V(C) has a displayed two-cover A|B. Write A=(a_0,...,a_m), m>=1. Then for every i the terminal endpoint a_m satisfies at least one of
(c_i,a_m,a_{m-1}) tight,
(c_{i+1},c_i,a_m) tight.
Dually, for every i the initial endpoint a_0 satisfies at least one of
(a_0,c_i,c_{i-1}) tight,
(a_1,a_0,c_i) tight.
The same two cut-by-cut dichotomies hold for both endpoints of B. Thus failure to splice the cyclic support to its complement is witnessed at every cut by a bounded reverse triple, and for each fixed complementary endpoint at least ceil(k/2) cyclic cuts realize one of its two obstruction types.

## Body

Fix i. Open the tight cycle at the cut c_{i-1}|c_i, obtaining the tight Hamilton path
C_i=(c_i,c_{i+1},...,c_{i-1})
on V(C).

First try to concatenate A followed by C_i. All consecutive triples are already tight except possibly
(a_{m-1},a_m,c_i)
and
(a_m,c_i,c_{i+1}).
If both were tight, A followed by C_i would be a Hamilton path on V(A) union V(C), and together with the unchanged path B would form a spanning two-cover of H, contradicting pc(H)>2. Hence at least one of the two triples is non-tight. Boundary antisymmetry gives respectively
(c_i,a_m,a_{m-1})
or
(c_{i+1},c_i,a_m)
tight. This proves the terminal-end dichotomy.

Now open the cycle at c_i|c_{i+1}, so that
C'_i=(c_{i+1},...,c_i)
ends at c_i, and try to concatenate C'_i followed by A. The only possibly new triples are
(c_{i-1},c_i,a_0)
and
(c_i,a_0,a_1).
Again they cannot both be tight, or C'_i followed by A together with B would two-cover H. Reversing whichever fails yields respectively
(a_0,c_i,c_{i-1})
or
(a_1,a_0,c_i)
tight.

The proof for B is identical. Finally, for a fixed endpoint and its k cuts, each cut belongs to at least one of two obstruction classes; therefore one class occurs on at least ceil(k/2) cuts.