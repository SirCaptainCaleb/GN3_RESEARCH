# A pure-cycle residue without direct reversal has a complete cycle-edge by complement-endpoint four-window grid

## Statement

Let H be a minimum counterexample, let C=(u_0,...,u_{r-1}) be a proper vertex-simple tight cycle, and let A|B be a displayed two-cover of H-V(C). Fix a cycle edge u_i u_{i+1}. If no tight triple contains the reversed consecutive pair (u_{i+1},u_i), then for every non-singleton complementary component R=(r_0,...,r_m), the four-set {u_i,u_{i+1},r_m,r_{m-1}} is Hamiltonian, witnessed by the tight path (r_m,u_i,u_{i+1},r_{m-1}). Consequently, if both A and B are non-singleton, every cycle edge lies simultaneously in two Hamiltonian four-windows, one using the final two vertices of A and one using the final two vertices of B; each such four-window has non-Hamiltonian path-cover-two complement.

## Body

Fix the cycle edge u_i u_{i+1} and assume no tight triple contains the reversed consecutive pair (u_{i+1},u_i).

As in the proof of 2d06838dc40e, this makes the fixed cycle edge universally two-sided extendable. For every vertex w outside {u_i,u_{i+1}}, both
(w,u_i,u_{i+1}) and (u_i,u_{i+1},w)
are tight: otherwise their reverses would contain (u_{i+1},u_i) consecutively.

Let R=(r_0,...,r_m), m>=1, be any non-singleton displayed component of the complement cover A|B. Apply universal two-sided extension first with w=r_m and then with w=r_{m-1}. The two triples
(r_m,u_i,u_{i+1}) and (u_i,u_{i+1},r_{m-1})
are tight. Hence
(r_m,u_i,u_{i+1},r_{m-1})
is a tight Hamilton path on the four-set W={u_i,u_{i+1},r_m,r_{m-1}}.

If both displayed complement components are non-singleton, apply the same argument independently to each, giving one Hamiltonian four-set for each component and the same chosen cycle edge.

Since H is a minimum counterexample of order greater than ten, every such W is proper. If H-W were Hamiltonian, a Hamilton path on W together with one on H-W would two-cover H. Therefore H-W is non-Hamiltonian, and minimum-counterexample calculus gives path-cover number two.

Thus every cycle edge with no direct reversed-pair witness lies in a Hamiltonian four-window with the final two vertices of each nontrivial complement component. No adjacency or orientation of the complement terminal edge inside that Hamilton path is asserted.
