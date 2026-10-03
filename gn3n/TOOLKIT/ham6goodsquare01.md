# Every Hamiltonian six-set with two-coverable complement contains a full two-label square

**Summary:** Every Hamiltonian six-set with two-coverable complement contains a full two-label square.

## Statement

Let H be a minimum counterexample, let U be a proper Hamiltonian six-vertex set, and put K=H-U. Assume H[K] is non-Hamiltonian, hence has path-cover number two. Then there exist distinct d,e in U such that all four induced subtournaments H[K], H[K+d], H[K+e], and H[K+d+e] are non-Hamiltonian with path-cover number two, while U-d, U-e, and U-{d,e} are Hamiltonian.

## Body

# Proof

Choose a Hamilton tight path

U=(u_0,u_1,u_2,u_3,u_4,u_5).

Set d=u_0 and e=u_5. Deleting d leaves the inherited Hamilton path (u_1,u_2,u_3,u_4,u_5), deleting e leaves (u_0,u_1,u_2,u_3,u_4), and deleting both leaves (u_1,u_2,u_3,u_4). Hence U-d, U-e, and U-{d,e} are Hamiltonian.

By hypothesis K is non-Hamiltonian with path-cover number two. If K+d were Hamiltonian, a Hamilton path on K+d together with a Hamilton path on U-d would give a spanning two-cover of H, contradiction. Hence K+d is non-Hamiltonian; as a proper induced subtournament of the minimum counterexample, it has path-cover number two. The same argument applies to K+e.

Finally, if K+d+e were Hamiltonian, its Hamilton path together with the inherited Hamilton path on U-{d,e} would two-cover H. Thus K+d+e is non-Hamiltonian and has path-cover number two. ∎

## Metadata

- ID: ham6goodsquare01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Promoted
