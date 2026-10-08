# General outer-splice bridge and branch-length forcing — preserved pre-item development

## General outer-splice bridge

Fix coordinate arity r>=2. Let
P=A,S and Q=B,S^rev
be a color-sigma converging tight fork covering V\{x}, with |A|=p>=1, |B|=q>=1, and |S|=r-1. Assume x is blocked at both outer fronts:
h(x,F_P)=h(x,F_Q)=1-sigma.

Form the cyclic coordinate order
C=(P^rev,x,B).
Write bar(sigma)=1-sigma. Its cyclic status word is

bar(sigma)^p, sigma, e_1,...,e_{r-2}, bar(sigma), sigma^q.   (1)

Indeed the first p windows are the reversals of the windows of P; the next window is (F_P^rev,x), of color sigma; the next r-2 windows are the remaining windows through x; the next is (x,F_Q), of color bar(sigma); and the final q windows are the windows of Q.

Normalize sigma=0 and call the length-r bridge
G=(g_0,...,g_{r-1})=(0,e_1,...,e_{r-2},1).
Let
K={k in {1,...,r-1}: g_{k-1} != g_k},
k_- = min K,  k_+ = max K.
The set K is nonempty because the bridge endpoints differ.

### Branch-length forcing

In a counterexample,
p >= r-k_+,
q >= k_-.

Proof. The full cyclic status word is
1^p, G, 0^q.
A linear cut omits exactly r consecutive cyclic transition edges.

Suppose p+k_+ <= r-1. Start an omitted r-edge arc at the cyclic transition 0^q -> 1^p. Before reaching the last internal bridge transition k_+, the arc uses
1 +(p-1)+1+k_+ = p+k_+ +1 <= r
edges. It has already captured the cyclic transition, the transition 1^p -> g_0=0, and every internal transition of G. Extend the arc to exactly r edges through the zero-transition tail after k_+; this can be done without reaching the remaining transition g_{r-1}=1 -> 0^q. Hence all cyclic changes except at most that one are omitted. The complementary linear order has at most one change, contradiction. Therefore p+k_+ >= r.

Symmetrically, if q <= k_- -1, an r-edge arc beginning at the first internal bridge transition k_- and running through the bridge end, the 0^q run, and the cyclic return captures every transition except 1^p -> g_0. Again a good linear cut results. Hence q>=k_-.

### One-change bridge specialization

If the bridge itself changes exactly once, at position k, then
p>=r-k and q>=k,
so p+q>=r and therefore n>=2r.

For r=3 the bridge is (0,beta,1), which always has exactly one change. If beta=0 then q>=2; if beta=1 then p>=2. This recovers the ternary outer-splice forcing rule.

### Significance

The missing vertex is confined to an r-status bridge. In a minimum counterexample, the first and last transitions of that bridge must be protected from the two ends by branch lengths at least r-k_+ and k_-, respectively. Thus short branches force the bridge transition pattern away from the corresponding end.
