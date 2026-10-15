# Paired-dimension colorings give a low-index global endpoint quotient

- Stable ID: note_cfb2ea26b51b2a8827e349cd
- Author: unspecified; session provenance retained
- Primary home: subsection:monochromatic_geodesic_endpoint_posets_and_a_global_rank_bounded_target
- Labels: endpoint-poset, equivariant-index, method-limitation
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7742_1
- Updated session: session_nori_r7742_1
- Disposition: none
- Successor: none

## Related references

- subsection:monochromatic_geodesic_endpoint_posets_and_a_global_rank_bounded_target, exact version 1

## Research note

**Theorem.** For every \(m\ge1\), there is a NORI1 coloring of \(Q_{2m}\) such that, for the red geodesic endpoint poset \(\mathcal P_0(c)\) and its endpoint-reversal involution \(J\), the covering class on its quotient satisfies
\[
w^{m-1}\ne0,\qquad w^m=0.
\]
The coloring has monochromatic full antipodal geodesics of length \(2m\).

**Construction.** Group the dimensions into pairs \(\{2j-1,2j\}\), and put
\[
c_{2j-1}(x)=x_{2j},\qquad c_{2j}(x)=x_{2j-1}.
\]
Each edge color ignores its own dimension bit and changes under full complementation. In each pair, the red graph is the path \(10-00-01\), together with the isolated vertex \(11\). Consequently every red component of the full cube is a Cartesian product of some of these three-vertex paths and isolated factors.

**Upper bound.** Define
\[
t_j(x)=x_{2j-1}-x_{2j}.
\]
For every red-geodesic endpoint pair \((u,v)\), the vector \(t(v)-t(u)\in\mathbb R^m\) is nonzero. Within a red component, \(t_j\) orders its three-vertex path as \(-1,0,1\). The distance-additivity condition defining the endpoint poset requires each factor to move monotonically along this path. Thus, on every poset chain, all endpoint-difference vectors have compatible signs in each entry. A nonnegative nonzero combination of those vectors cannot vanish. Normalized barycentric interpolation therefore gives a continuous \(J\)-equivariant map
\[
\Delta\mathcal P_0(c)\longrightarrow S^{m-1},
\qquad (u,v)\longmapsto
\frac{t(v)-t(u)}{\|t(v)-t(u)\|}.
\]
Naturality of the covering class gives \(w^m=0\).

**Lower bound.** Fix all even-numbered bits to zero. The remaining \(m\)-cube is entirely red. Its endpoint poset contains an antipodal copy of \(S^{m-1}\): map a nonempty signed face of the \(m\)-crosspolytope, with negative support \(A\) and positive support \(B\), to the endpoint pair \((\mathbf1_A,\mathbf1_B)\) in this red subcube. Signed-face inclusion gives the metric-additive poset order, and sign reversal swaps the endpoints. The order complex of the signed-face poset is \(S^{m-1}\), so pulling back the covering class proves \(w^{m-1}\ne0\).

Finally, a full red geodesic starts with state \(10\) in every dimension pair, flips each odd-numbered dimension to reach all \(00\), and then flips each even-numbered dimension to reach all \(01\). Its terminal vertex is the antipode of its initial vertex.

**Scope.** Antipodal oddness alone therefore does not force the endpoint quotient to have nonzero covering-class powers near the ambient cube dimension. Its highest nonzero power can be only \(m-1\) in dimension \(2m\), even when full monochromatic geodesics exist. A proposed equivariant source assignment into this target must use consequences of the absence of favorable complete paths; those consequences cannot be replaced by a universal high-index assertion for every NORI1 coloring.
