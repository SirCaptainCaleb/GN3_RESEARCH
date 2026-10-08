# A shared bridge at neighboring cuts exposes four new repair labels — preserved pre-item development

## Development

Lemma. Let A be a four-vertex set, r,v,s three further vertices, and T,U disjoint tight paths of order at least two, with all these vertex sets disjoint. Suppose (T,r) and (U,s) are tight. Consider the two six-packets
S_s=A union {r,v}, with complement T | (U,s),
S_r=A union {v,s}, with complement (T,r) | U.
Assume v is a bridge between the two displayed tails in each test.

Either one of those two bridge tests gives a two-cover, or there is an explicit third packet
S_v=A union {r,s},
with a two-path complement, such that every deletion S_v-w, w in A, is Hamiltonian.

Proof. If S_s-v=A+r is Hamiltonian, the first bridge test gives a two-cover. If S_r-v=A+s is Hamiltonian, the second does so. Otherwise both five-sets A+r and A+s are non-Hamiltonian. Four-of-six on S_v then makes all four five-deletions S_v-w, w in A, Hamiltonian, as in [[successive_bad_five_packets_force_four_cross_endpoint_repairs]].

The third complement is obtained from the first bridge. If (T,v,U,s) is tight, use (T,v)|U. If (U,s,v,T) is tight, use (v,T)|U. In the first case T,v is an inherited tight subpath and in the second v,T is an inherited tight subpath. U itself is tight after deleting its displayed terminal endpoint s. These two paths partition the complement of S_v. No internal deletion or reversal of a tight path is used. QED.

Consequently, in the residual case, any w in A that bridges the two paths of this constructed third cover gives a two-cover: its five-deletion S_v-w is already known Hamiltonian. The permissible repair labels have expanded from the common exceptional bridge v to four good deletions. Failure requires that all four A vertices fail the joining test for the third cover.

Application to neighboring monotone cuts j and j+1. Use
A={x,y,c_1,c_2},
r=c_{j+1}, v=c_{j+2}, s=c_{j+3},
T=(c_3,...,c_j), U=(c_N,...,c_{j+4}).
These have the asserted orientations and endpoint extensions because the two legal corridor cuts give tight covers. When j is u or u+1 and u,v_status>=4, T and U each have at least two vertices. The shared vertex c_{j+2} can be tested as a bridge in both neighboring packets. If both tests fail their Hamiltonian deletion tests, transferring that shared vertex to T as above makes the third cover available automatically.

This is a two-stage sufficient repair certificate. It uses the failure of neighboring tests to force four good deletion supports and creates the compatible tail cover needed to consume them. It does not assume that the shared vertex bridges both tests or that a good deletion label must bridge the new tails. Their simultaneous failure remains a stated structural residue, rather than a completed finite reduction.

A resulting two-cover order on the full reflected span is outward in the positive witness filtration. Equivariance and compatibility of the choices of neighboring cuts, transfers, and carriers across ambient faces remain separate.
