# The stationary two-cross cell cannot leave p isolated

**Workspace:** D17
**State:** working
**Key:** `stationary-isolated-p-consumer`

**Summary:** In the corrected quiet c=2 stationary normal form, the d=0 case is impossible. Then A,B,Z are full blocks and p is a singleton rail. Outside explicit same-support R435 disagreement, those full block orders equal the retained petal orders, while A+p and B+p have the exact quiet final-gap puncture orders. If the three-block rail has an A-B adjacency, puncturing the downstream petal Hamiltonizes M=A+B+p and yields the forbidden subthreshold singleton cover M|(u+Z). If it has no A-B adjacency, its word is A-Z-B or B-Z-A; puncturing the terminal petal Hamiltonizes W, and W together with the omitted dimer two-covers H. Thus every surviving quiet c=2 cover has at least one p-A or p-B incidence.

### Setup
Retain the corrected quiet c(T)=2 stationary normal form from `stationary-common-cross-multiplicity`. Put

  A=X-{u_X},  B=Y-{u_Y},

with |A|=|B|=k-1, |Z|=k, and W=A disjoint-union B disjoint-union Z disjoint-union {p}. Assume d(T)=0, so p has no selected p-A or p-B incidence. The corrected block identity then gives

  b_A=b_B=b_Z=1.

Since p-Z is impossible, p is an isolated T rail and the other rail P is a Hamilton path on A union B union Z with exactly three full class blocks and exactly two class transitions.

Branch explicitly if any full A-,B-, or Z-block order in P has R435 geometry relative to the retained Hamilton order on that same support. Outside that order-valued branch, R435 monotonicity on equal supports forces each full block order to be exactly its retained order. Likewise `terminal-puncture-last-gap`, together with the accepted source-anchored puncture packet, gives quiet Hamilton punctures

  K_A=(a_1,...,a_{k-2},p,a_{k-1}),
  K_B=(b_1,...,b_{k-2},p,b_{k-1})

for the retained orders A=(a_1,...,a_{k-1}) and B=(b_1,...,b_{k-1}), up to the exact common dual orientation. In particular K_A and K_B preserve the first two vertices of their petal orders.

### If the three-block rail has an A-B seam, M is Hamiltonian
Suppose P contains an adjacent A-B pair. Orient the occurrence as A followed by B; the B-followed-by-A case is dual. The literal P seam certifies the two junction turns from the terminal end of A into the first two vertices b_1,b_2 of B. Replace the full B block by K_B. Because K_B has the same first two vertices b_1,b_2, every A-to-B junction turn remains certified, while the rest of K_B is tight by construction. Therefore

  A followed by K_B

is a Hamilton path on

  M=A union B union {p}.

The historical stationary seam gives a Hamilton path on u_X+Z. Hence

  H-u_Y : M | (u_X+Z)

is an exact singleton cover with rail sizes

  2k-1  and  k+1,

both strictly below a=2k. This contradicts `subminimum-source-saturation`.

### If there is no A-B seam, W itself becomes Hamiltonian
A three-block path on A,B,Z with two transitions and no A-B adjacency must have class word

  A-Z-B

or its A/B dual, in its actual path orientation. Suppose it is A-Z-B. The terminal B block is traversed in the retained B order. Replace that terminal block by K_B. The incoming Z-to-B seam uses only the first two B vertices b_1,b_2, so it is unchanged. No outgoing seam exists at the terminal end. Thus

  A-Z-K_B

is a Hamilton path on all of W. The omitted pair {u_X,u_Y} is a vacuous tight dimer, so this Hamilton W path together with (u_X,u_Y) is a spanning two-cover of H, contradiction. The B-Z-A word is dual using K_A.

### Conclusion
Therefore the quiet stationary c=2 residue cannot have d=0. Every surviving quiet c=2 cover satisfies

  d=m_A+m_B>=1.

Equivalently p must be physically incident with A or B in every surviving minimum-two-cross representative. The next case d=1 has exactly one fragmented petal and should be treated by recombining that split petal with its full quiet puncture path while retaining the two outer seams.

Status: complete conditional consumer inside the corrected stationary c=2 quiet cell. Explicit same-support R435 disagreement remains a separate live output and is not claimed to close the branch.
