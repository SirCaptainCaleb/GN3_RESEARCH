# Type-A index gap and irreducibility obstruct linear dimension reduction

- Stable ID: note_93be7dcfcd553b4713e9f5bb
- Author: unspecified; session provenance retained
- Primary home: section:nori_type_a_rook_gallery_topology
- Labels: type-a, equivariant-topology, dimension-gap, standard-representation
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7547_3
- Updated session: session_nori_r7547_3
- Disposition: none
- Successor: none

## Related references

- subsection:local_exchange_axioms_reconstruct_the_two_coloring_classes

## Research note

**Proposition (the type-A chamber complex alone has no Borsuk–Ulam dimension gap).** Let \(n\ge3\), \(W=\{z\in\mathbb R^n:\sum_i z_i=0\}\), and let \(\mathcal C_A\) denote the spherical Coxeter chamber complex of type \(A_{n-1}\). Under the antipodal action, \(|\mathcal C_A|\) is \(S(W)\cong S^{n-2}\). Hence an antipodally equivariant map \(|\mathcal C_A|\to S(W)\) exists: the identity. In particular the impossibility of equivariant maps \(S^{d+1}\to S^d\), used by Wu and Yang, cannot be invoked with the unmodified type-A chamber sphere as source and the type-A root sphere as target.

**Proposition (no natural linear equivariant dimension drop).** Let \(S_n\) act on \(W\) by relabeling the standard basis. For any real \(S_n\)-representation \(U\) with \(\dim U<n-1\), every \(S_n\)-equivariant linear map \(L:W\to U\) is zero.

*Proof.* The real standard representation \(W\) is irreducible. If \(V\subseteq W\) is a nonzero invariant subspace, choose \(v\in V\setminus\{0\}\). Since \(\sum_i v_i=0\), some \(v_i\ne v_j\). For the transposition \((ij)\), the vector \(v-(ij)v=(v_i-v_j)(e_i-e_j)\) lies in \(V\), so \(e_i-e_j\in V\). Applying all permutations produces all differences \(e_a-e_b\), which span \(W\). Thus \(V=W\). The kernel of an equivariant linear map is invariant, so any nonzero map out of \(W\) is injective. An injection into \(U\) is impossible when \(\dim U<n-1\). \(\square\)

Consequently an \(S_n\)-symmetric Borsuk–Ulam strategy for boundary tournaments cannot obtain a lower-dimensional root-sphere target by a linear equivariant quotient of the usual type-A root representation. It must instead obtain an additional dimension in the source, use nonlinear color-sensitive data, or employ a target not produced by such a quotient. For NORI1, the type-B chamber sphere has dimension \(n-1\), one greater than the type-A root sphere \(S(W)\), but color-induced construction of a suitable equivariant map remains unproved.
