# Double-hole endpoint certificates always contain a hole-preserving core — preserved pre-item development

## Double-hole endpoint certificates always contain a hole-preserving core

Let \(Y\) be a Hamiltonian five-set with distinguished labels \(x,y\), and put
\[
N=Y-\{x,y\},\qquad |N|=3.
\]
Let \(e\notin Y\). Suppose both
\[
(Y-\{x\})\cup\{e\}
\qquad\text{and}\qquad
(Y-\{y\})\cup\{e\}
\]
are Hamiltonian.

Then there exists \(r\in N\) such that
\[
\boxed{(Y-\{r\})\cup\{e\}\text{ is Hamiltonian}.}
\]

Indeed, consider the six-set
\[
U=Y\cup\{e\}.
\]
Among its six vertex-deleted five-subsets, three are already Hamiltonian:
deleting \(x\), deleting \(y\), and deleting \(e\) (which leaves \(Y\)).
The four-of-six theorem says at least four of the six deletions are Hamiltonian.
The three remaining deletion labels are precisely the ordinary labels in \(N\), so at least one of them is also good.

Consequently the double-hole endpoint alternative in [[rooted_five_components_synchronize_through_a_nonhole_or_double_hole_endpoint]] is not disjoint from the hole-preserving-core alternative at that endpoint. Every endpoint carrying both hole-deletion certificates also carries a four-label core \(Y-\{r\}\) which still contains both holes and accepts the endpoint.

For a long tail with endpoints \(e_1,e_2\), the only genuine obstruction to a single hole-preserving four-core working at both ends is therefore a **change of ordinary deletion label**:
\[
r_1\ne r_2,\qquad
(Y-\{r_i\})\cup\{e_i\}\text{ Hamiltonian}.
\]
Thus the rooted five-component handoff reduces further from a hole/nonhole dichotomy to synchronization of at most three ordinary deletion labels across the exposed tail endpoints.
