# Independent port-preserving contractions and fundamental-cocircuit repair

# Independent port-preserving contractions and fundamental-cocircuit repair

Let \(M\) be a finite binary matroid with a distinguished nonloop \(p\), and let \(T\subseteq E(M)\setminus\{p\}\), with \(S=E(M)\setminus T\). Denote the binary cycle space by \(Z(M)\) and its dual cocycle space by \(Z^*(M)\).

**Theorem 1 (intrinsic faithful-contraction criterion).** Restriction induces a surjective linear map
\[
\pi_T:Z(M)\longrightarrow Z(M/T),\qquad X\longmapsto X\cap S.
\tag{1}
\]
The map is an isomorphism if and only if \(T\) is independent in \(M\). Moreover,
\[
\boxed{T\cup\{p\}\text{ is independent in }M}
\tag{2}
\]
if and only if (1) is an isomorphism and \(p\) remains a nonloop of \(M/T\).

*Proof.* Choose a binary representation \(A\) of \(M\). A cycle of \(M/T\) is a binary dependence of the columns indexed by \(S\) modulo the span of the columns indexed by \(T\). Every such dependence lifts to a cycle of \(M\), proving surjectivity. The kernel comprises cycles of \(M\) supported in \(T\); it is zero precisely when \(T\) contains no circuit, equivalently when \(T\) is independent. Finally \(p\) becomes a loop in \(M/T\) precisely when its representing column lies in the span of the columns of \(T\). In conjunction with independence of \(T\), this is equivalent to dependence of \(T\cup\{p\}\). \(\square\)

**Theorem 2 (port-avoiding fundamental cocircuit certificates).** Assume (2). There is a basis \(B\) of \(M\) containing \(T\cup\{p\}\). For every \(e\in T\), its fundamental cocircuit \(K_e^*\) with respect to \(B\) obeys
\[
\boxed{K_e^*\cap(T\cup\{p\})=\{e\}.}
\tag{3}
\]
Consequently each deleted cycle coordinate is reconstructed by
\[
\boxed{\mathbf1_X(e)=
\sum_{f\in K_e^*\setminus\{e\}}\mathbf1_X(f)\pmod2}
\tag{4}
\]
for every \(X\in Z(M)\). Conversely, if \(p\) is a nonloop and the cocircuits (3) exist for all \(e\in T\), then (2) holds.

*Proof.* Extend the independent set \(T\cup\{p\}\) to a basis \(B\). By definition, \(K_e^*\cap B=\{e\}\), giving (3). Binary cycle–cocircuit orthogonality gives (4). Conversely, if a circuit lies inside \(T\cup\{p\}\), it cannot be \(\{p\}\) because \(p\) is a nonloop. It contains some \(e\in T\), and then its intersection with \(K_e^*\) has size one, contrary to binary orthogonality. Therefore \(T\cup\{p\}\) is independent. \(\square\)

The criterion is an intrinsic property of the pointed matroid and the selected contraction set; it involves neither a graph representation nor a covering. The local-port-diameter theorem of the previous Subsection supplies the stronger **bounded-size** certificates (3) in the two canonical graph-cover models.

**Theorem 3 (intrinsic quantitative port-cocircuit transfer).** Under (2), suppose that cocircuit certificates \(K_e^*\) can be chosen for all \(e\in T\) satisfying (3) and \(|K_e^*|\le L+1\), for an integer \(L\ge1\). For any binary cycle \(X\in Z(M)\) containing \(p\), and any cocircuit \(Y\in\mathcal C^*(M)\) containing \(p\), let \(t=|Y\cap T|\) and put \(X'=\pi_T(X)\). Then there exists a port cocircuit \(Y'\in\mathcal C^*(M/T)\) such that
\[
\boxed{|Y'|\le |Y|+(L-1)t,}
\tag{5}
\]
and
\[
\boxed{|X'\cap Y'|\le
|X\cap Y|+2\left\lfloor\frac L2\right\rfloor t.}
\tag{6}
\]
No graph-cover realization is required for this theorem.

*Proof.* Cocycle vectors form a binary vector space, so take
\[
Z=Y\mathbin{\triangle}
\mathop{\triangle}_{e\in Y\cap T}K_e^*.
\tag{7}
\]
Every \(K_e^*\) meets \(T\) solely in \(e\) and avoids \(p\). Hence \(Z\) is a cocycle avoiding \(T\) and containing \(p\). A binary cocycle decomposes into a disjoint union of cocircuits; at least one constituent \(Y'\) contains \(p\). Since \(Y'\subseteq S\), it is a cocircuit of \(M/T\). Formula (7) replaces \(t\) deleted elements with at most \(Lt\) surviving elements, proving (5).

For the weight bound, put \(v_e=\mathbf1_X(e)\) and \(R_e=K_e^*\setminus\{e\}\). Since \(K_e^*\) is a cocircuit, binary orthogonality gives
\[
|X\cap R_e|\equiv v_e\pmod2.
\tag{8}
\]
Also \(|R_e|\le L\). Consequently
\[
|X\cap R_e|-v_e\le2\lfloor L/2\rfloor.
\tag{9}
\]
Using symmetric-difference subadditivity for the integer overlap weight and summing (9) over the replaced elements gives
\[
|X\cap Z|
\le |X\cap Y|+2\lfloor L/2\rfloor t.
\]
Since \(Y'\subseteq Z\cap S\), and \(X'\) is the restriction of \(X\), (6) follows. \(\square\)

**Corollary 4 (the signed-cover cases).** For the cube all turns are admissible, so take \(T=\varnothing\). For the boundary graph cover, delete inadmissible turns; the local-port completion theorem supplies certificates \(K_e^*\) of size at most four, avoiding \(p\) and meeting \(T\) only at \(e\). Thus \(T\cup\{p\}\) is independent, and (5)–(6) recover the boundary transfer bounds
\[
|Y'|\le |Y|+2t,\qquad
|X'\cap Y'|\le|X\cap Y|+2t.
\]

**Generalization hypothesis.** The combination of (i) a binary pointed matroid, (ii) a port-preserving independent contraction \(T\), (iii) uniformly short fundamental cocircuit certificates, and (iv) a directed resource-independent path language gives an intrinsic matroidal starting point for a common path-selector conjecture. Parts (i)–(iii) provide faithful passage from unrestricted to admissible turns and quantitative control of port cocircuit intersection. Part (iv) is essential for converting the resulting cocircuits to forward, resource-simple witnesses.

## 4. Bipointed sector cohesion: the missing condition

Theorem 3 transfers cocircuits containing a **single** distinguished port. For two ports \(p,q\), it need not transfer a cocircuit containing both ports, even if \(T\cup\{p,q\}\) is independent: the repaired cocycle can split into cocircuits that separate \(p\) and \(q\). A four-vertex diamond-graph counterexample is retained in the linked research notes.

**Theorem 5 (cocycle-support port-cohesion criterion).** Let \(M\) be any matroid, and let \(Z\in Z^*(M)\) be a nonempty cocycle containing distinct designated elements \(p,q\). There exists a cocircuit \(Y\subseteq Z\) containing both \(p\) and \(q\) if and only if \(p,q\) lie in the same connected component of the restricted dual matroid
\[
\boxed{M^*|Z.}\tag{10}
\]

*Proof.* The cocircuits of \(M\) contained in \(Z\) are precisely the circuits of \(M^*|Z\). In any matroid, two different elements lie in a common connected component if and only if some circuit contains both. Substituting the dual circuits proves the assertion. \(\square\)

**Corollary 6 (conditional two-port quantitative transfer).** Assume \(T\cup\{p,q\}\) is independent and every \(e\in T\) admits a fundamental cocircuit certificate of size at most \(L+1\) meeting \(T\cup\{p,q\}\) solely in \(e\). Let \(Y\) be a cocircuit containing both \(p,q\), and form the repaired cocycle \(Z\) by (7), with \(t=|Y\cap T|\). If \(p,q\) remain in the same connected component of \(M^*|Z\), then there exists a cocircuit \(Y'\) of \(M/T\) containing both \(p,q\) and obeying the same length and integer-overlap bounds (5)–(6).

*Proof.* The fundamental cocircuits avoid both ports, so \(Z\) contains \(p,q\) and avoids \(T\); its size and overlap satisfy the estimates already proved for Theorem 3. Theorem 5 supplies a cocircuit \(Y'\subseteq Z\) containing both ports. It is also a cocircuit of \(M/T\) because it avoids \(T\), and restricting the overlap to \(Y'\) cannot increase it. \(\square\)

Thus a bipointed extension requires **cocycle-support port cohesion**, not merely survival and independence of two ports. This is a natural dual-matroid connectivity condition, and it pinpoints the obstruction to preserving the orientation-curvature cocircuit sector of Article XI under contraction.
