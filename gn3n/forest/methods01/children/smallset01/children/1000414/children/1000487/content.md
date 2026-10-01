# Dense complementary blocker family

## Statement

Let H be edge-orderable. Let A|B be a spanning two-cover with mandatory ordered triple T consecutive on A. Let u,v be the endpoints of A and C=A-{u,v}. Put an edge xy on B when H[{u,v,x,y}] is Hamiltonian. Then this graph has independence number at most two. For each such xy, with S=B-{x,y}, if T meets {u,v} then H[C union S] is non-Hamiltonian; if T is contained in C, then H[C union S] is either non-Hamiltonian or every Hamilton path on it contains T consecutively. If m=|B|, this applies to at least binom(m,2)-floor(m^2/4) pairs.

## Body

The independence bound is 83629aa6b00e. For an edge xy, Q={u,v,x,y} is Hamiltonian and its complementary support is P=C union (B-{x,y}). Apply 03f207e2f951 to P,Q. This gives the stated blocker alternative. Since the complement of the auxiliary graph is triangle-free, Mantel's theorem gives at most floor(m^2/4) missing edges, proving the pair count. ∎
