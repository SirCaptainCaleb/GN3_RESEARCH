# Every anchored four-window either descends, yields a bounded six-window, or has order at most fourteen

## Statement

Let H be a minimum counterexample, let W be a Hamiltonian four-vertex set, and let H-W=P|Q be a two-cover, with displayed endpoint sets E_P={p_0,p_m} and E_Q={q_0,q_s}. Then at least one of the following holds.

(1) Bounded six-window: there is a six-vertex set U containing three vertices of W and three displayed complement endpoints such that either H[U] is Hamiltonian, or H[U] is non-Hamiltonian and Hamilton paths on its Hamiltonian one-vertex deletions exhibit order disagreement.

(2) Strict quadratic descent: the spanning three-cover W|P|Q admits an endpoint transfer to another spanning three-cover with strictly smaller Phi=sum |C|^2.

(3) |V(H)|<=14.

Consequently, for order at least fifteen, every anchored Hamiltonian four-window with two-cover complement yields either a bounded Hamiltonian/order-disagreement six-window or an explicit strict Phi descent.

## Body

For each cross pair (e,f) in E_P x E_Q, apply the certified theorem twofourhamdeletions01 to the disjoint two-set {e,f} and four-set W. At least two labels w in W make (W-{w}) union {e,f} Hamiltonian. Thus the 4 by 4 incidence relation between labels w and cross pairs has at least eight good incidences.

If some fixed w is good for two cross pairs sharing an endpoint, say (e,q_0) and (e,q_s), put D=W-{w} and U=D union {e,q_0,q_s}. Then U-q_s and U-q_0 are Hamiltonian. If U is Hamiltonian, outcome (1) holds. If U is non-Hamiltonian, the certified four-of-six theorem says at least four vertex deletions of U are Hamiltonian; applying astra004fourgooddisagree to arbitrary Hamilton orders on four good deletions forces order disagreement. Again outcome (1) holds.

Assume now no fixed w is good for two cross pairs sharing an endpoint. For each w its good-pair set is therefore a matching in K_{2,2}, so has size at most two. Since the total good-incidence count is at least eight and there are four labels w, equality holds: every w is good for exactly two cross pairs, and every cross pair is good for exactly two labels. A two-edge matching in K_{2,2} is one of the two perfect matchings, so the four labels split into two pairs according to the two checkerboard matching types.

Fix any cross pair (e,f) and set V=W union {e,f}. Exactly two deletions V-w, w in W, are Hamiltonian. By four-of-six, at least four of the six vertex deletions of V are Hamiltonian. Hence the two remaining deletions V-e=W union {f} and V-f=W union {e} are both Hamiltonian. Varying the cross pair shows that W enlarged by each displayed endpoint of P or Q is Hamiltonian.

If |P|=m>=6, choose either endpoint e of P. Replacing W|P by a Hamilton path on W union {e} and the inherited path P-e changes the two component orders from (4,m) to (5,m-1), so the quadratic-potential change is 25+(m-1)^2-16-m^2=10-2m<0. This gives outcome (2). The same applies when |Q|>=6. If neither path has order at least six, then |P|,|Q|<=5 and |V(H)|=4+|P|+|Q|<=14, outcome (3).
