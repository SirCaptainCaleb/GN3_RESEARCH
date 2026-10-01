# The pure tight-cycle residue reduces to local reversal, a small complement, or the standard five-window/cross-triple frontier

## Statement

Let H be a minimum counterexample and let C be the proper vertex-simple tight cycle arising in the pure-cycle branch of aa6c87f1e473. Put K=H-V(C). Then at least one of the following holds:

(1) some cycle edge uv has a genuine nontrivial reversal: a tight triple contains the consecutive pair (v,u);

(2) |V(K)|<=6;

(3) H contains a proper Hamiltonian five-vertex set W whose complement is non-Hamiltonian of path-cover number two;

(4) there is a displayed two-cover A|B of K, a component R=(r_0,...,r_m) of order at least four, and a cycle vertex u such that the tight endpoint cross triple (r_m,u,r_0) holds.

Thus, outside a bounded complement of order at most six, the pure-cycle outcome of path-intersection disagreement is completely reduced to the same local reversal / Hamiltonian-five-window / endpoint-cross-triple interface already used by endpoint transport.

## Body

The cycle C is proper: if it spanned H, opening it at any cyclic cut would give a Hamilton path of H, contradicting pc(H)=3. By minimum-counterexample calculus, K is non-Hamiltonian with path-cover number two. Choose any displayed two-cover A|B of K.

If some cycle edge u_i u_{i+1} has a tight triple containing (u_{i+1},u_i) consecutively, outcome (1) holds. Hence suppose no cycle edge has such a nontrivial reversed-pair witness.

Fix any cycle vertex u_i. Apply the universal-edge argument to the cycle edge u_i u_{i+1}: absence of a reversed-pair triple implies that for every exterior vertex w,
(w,u_i,u_{i+1}) and (u_i,u_{i+1},w)
are tight. If R=(r_0,...,r_m) is a non-singleton component of A|B, opening C at u_i and attempting to append it after R shows, exactly as in 2d06838dc40e, that
(u_i,r_m,r_{m-1})
is tight.                                                   (A)

Now use the preceding cycle edge u_{i-1}u_i. It too has no reversed-pair witness, hence is universally two-sided extendable. Open C at u_{i+1}, so its Hamilton order ends
...,u_{i-1},u_i.
Attempt to concatenate this opened cycle before R. The join triple
(u_{i-1},u_i,r_0)
is tight by universal extension. If the next join
(u_i,r_0,r_1)
were tight, the opened cycle followed by R, together with the other component of A|B, would be a spanning two-cover of H. Therefore (u_i,r_0,r_1) is non-tight, and boundary reversal antisymmetry gives
(r_1,r_0,u_i)
tight.                                                   (B)

Thus every cycle vertex u_i gives opposite reverse hooks (B) and (A) at the two ends of every nontrivial complement component R.

If |K|<=6, outcome (2) holds. Otherwise |K|>=7, so in the two-cover A|B at least one component R has order at least four. Fix such R and any cycle vertex u=u_i. Boundary reversal antisymmetry gives exactly one of
(r_0,u,r_m), (r_m,u,r_0)
as tight.

If (r_0,u,r_m) is tight, then using (B), this central triple, and (A),
(r_1,r_0,u,r_m,r_{m-1})
is a tight Hamilton path on the five-set
W={r_0,r_1,u,r_{m-1},r_m}.
The five vertices are distinct because |R|>=4 and u lies outside K. Since a minimum counterexample has order greater than ten, W is proper. If H-W were Hamiltonian, W and H-W would two-cover H; hence H-W is non-Hamiltonian and minimum-counterexample calculus gives path-cover number two. This is outcome (3).

If (r_0,u,r_m) is non-tight, reversal antisymmetry gives (r_m,u,r_0) tight, which is outcome (4).

No cyclic rotation of an ordered tight triple is used.
