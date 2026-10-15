# Homotopy-constant prefix carriers and unrestricted degree transport

### Nested prefix carriers are homotopically constant; top degrees remain movable

Use the notation of the preceding Subsection. For every ordered partition \(\mathcal P\) into at least two nonempty blocks, put
\[
K_{\mathcal P}=\{v\in W:\langle v,T_{A_j}\rangle>0
\text{ for each proper cumulative first-block union }A_j\},
\]
and
\[
\mathcal C_{\mathcal P}
=\{\Pi\in\widetilde{\mathrm{Gr}}_2(W):
\Pi\cap K_{\mathcal P}\ne\varnothing\}.
\]
A refinement \(\mathcal Q\) of \(\mathcal P\) yields inclusions \(K_{\mathcal Q}\subseteq K_{\mathcal P}\) and \(\mathcal C_{\mathcal Q}\subseteq\mathcal C_{\mathcal P}\).

**Theorem 1 (all refinement inclusions are homotopy equivalences).** For every refinement \(\mathcal Q\) of \(\mathcal P\), the inclusion
\[
\boxed{\mathcal C_{\mathcal Q}\hookrightarrow\mathcal C_{\mathcal P}}
\tag{1}
\]
is a homotopy equivalence, inducing multiplication by \(\pm1\) on \(\pi_{n-3}\cong\mathbb Z\).

*Proof.* Let \(B_{\mathcal R}=K_{\mathcal R}\cap S(W)\), for \(\mathcal R=\mathcal P,\mathcal Q\). Both are nonempty contractible spherical convex sets, and \(B_{\mathcal Q}\subseteq B_{\mathcal P}\). Define incidence spaces
\[
E_{\mathcal R}
=\{(\Pi,v):\Pi\in\mathcal C_{\mathcal R},
\ v\in B_{\mathcal R}\cap\Pi\}.
\]
Projection \(E_{\mathcal R}\to B_{\mathcal R}\) is the \(S^{n-3}\)-bundle of oriented orthogonal companions of \(v\). Fix any \(v_0\in B_{\mathcal Q}\), and identify its fiber with \(S(v_0^\perp)\). Since each base is contractible, inclusion of this fiber is a homotopy equivalence for both \(E_{\mathcal Q}\) and \(E_{\mathcal P}\). The inclusion \(E_{\mathcal Q}\hookrightarrow E_{\mathcal P}\) is the identity on that common fiber, so is also a homotopy equivalence.

The projection \(E_{\mathcal R}\to\mathcal C_{\mathcal R}\) is a homotopy equivalence by the feasible-plane selection and contractible-fiber proof in the preceding Subsection; these projections commute with the refinement inclusions. The two-out-of-three property therefore implies (1) is a homotopy equivalence. QED.

**Theorem 2 (degree transport within the positive-carrier system).** Let \(F\) be any reversal-equivariant positive-carrier filling of the \((n-3)\)-skeleton, as constructed previously, with \(n\ge4\). Fix a three-block cell
\[
D_{A|B|C},\qquad A,B,C\ne\varnothing.
\]
It lies in precisely the two top cells
\[
D_{A|(B\cup C)}\quad\text{and}\quad
D_{(A\cup B)|C}.
\]
One can modify \(F\) inside the relative interior of this three-block cell, leaving its entire boundary and all other lower-dimensional cells fixed, and preserving all positive carriers, so that the two adjacent integral top-cell obstruction degrees each change by \(+1\) or \(-1\). No other top-cell degree changes. The modification on the reversal partner cell is uniquely prescribed by odd equivariance.

*Proof.* The three-block cell is an \((n-3)\)-ball, whose carrier has \(\pi_{n-3}(\mathcal C_{A|B|C})\cong\mathbb Z\). Replace its interior filling, relative to its fixed boundary, by the connected sum with any representative of a generator supported on a small interior ball. This changes its relative homotopy class by one and remains inside its carrier. The boundary of each adjacent top cell includes this three-block facet once. Under its inclusion into either two-block carrier, the added homotopy class maps to a generator by Theorem 1, changing that top attaching degree by \(\pm1\). No other top cell is incident with this three-block cell. Transport the modification to its reversed partner to retain global equivariance. QED.

**Corollary 3 (no fixed distribution of top-degree parity).** The graph on reversal-orbits of two-block cells, joining two vertices whenever they share a three-block facet orbit, is connected. Consequently, the changes allowed by Theorem 2 span all even-sum changes of the modulo-two top-degree vector. In particular, carrier preservation alone cannot determine which two-block cells have odd obstruction degree: it can move the odd degrees between different top-cell orbits.

*Proof.* Two-block cells are indexed by bipartitions \(\{A,V\setminus A\}\). Refining one side or the other gives a three-block incidence, and inclusions of proper nonempty subsets connect the bipartitions; more explicitly any proper subset can be reduced to a singleton by successive deletion, and singleton bipartitions connect through two-element unions. Hence the incidence graph is connected. Each three-block modification toggles the parity at its two endpoints. In a connected graph, endpoint-toggle vectors of edges span the even-sum subspace over \(\mathbb F_2\). QED.

**Interpretation and limitation.** The nested cone carriers solve the problem of constructing compatible fillings through the entire lower skeleton, but their facewise inclusions retain the full top-dimensional homotopy group: no natural degree is lost when a cell is refined. Thus the higher obstruction is a universal characteristic-class obstruction rather than an invariant of the particular color words. A proof of either original conjecture requires a further **color-sensitive restriction on allowed fillings or top-cell degrees**; positivity, reversal symmetry, and the nested-carrier condition alone do not provide one.
