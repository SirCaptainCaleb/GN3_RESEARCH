# Four-side cross-endpoint exchanges are adjacent or form a checkerboard equality shell

## Statement

Let H be a minimum counterexample, let W be a Hamiltonian four-set, and let H-W=P|Q be a two-cover with endpoint sets E_P={p_0,p_m}, E_Q={q_0,q_s}. For w in W let G_w be the set of cross pairs (e,f) in E_P x E_Q for which (W-{w}) union {e,f} is Hamiltonian.

Then exactly one of the following structural alternatives holds.

(A) Shared-endpoint branch: for some w, G_w contains two distinct cross pairs sharing one endpoint of P or Q.

(B) Checkerboard equality branch: after partitioning W=W_0 disjoint-union W_1 with |W_0|=|W_1|=2, the only good cross pairs are
G_w={(p_0,q_0),(p_m,q_s)} for every w in W_0,
G_w={(p_0,q_s),(p_m,q_0)} for every w in W_1.
In particular every G_w has size exactly two and every cross pair is good for exactly two labels w.

Thus failure of a common-endpoint double extension forces a 2+2 diagonal checkerboard on the four labels of W.

## Body

By twofourhamdeletions01, each of the four cross pairs (e,f) is good for at least two labels w in W. Hence there are at least 8 good incidences (w,(e,f)).

Assume (A) fails. Then for each fixed w, G_w contains no two edges of the 4-cycle K_{2,2} sharing a vertex. Therefore |G_w|<=2, and if |G_w|=2 those two edges form one of the two perfect matchings
M_0={(p_0,q_0),(p_m,q_s)},
M_1={(p_0,q_s),(p_m,q_0)}.
The total incidence count is at most 4*2=8, while the pairwise lower bound gives at least 8. Hence equality holds throughout: every |G_w|=2 and every cross pair has exactly two incident labels.

Let W_i={w:G_w=M_i}. Each edge of M_i is good exactly for the labels in W_i, so |W_i|=2 because every cross pair has incidence exactly two. Since the two matchings partition the four cross pairs and every w has one matching type, W=W_0 disjoint-union W_1. This is exactly (B).