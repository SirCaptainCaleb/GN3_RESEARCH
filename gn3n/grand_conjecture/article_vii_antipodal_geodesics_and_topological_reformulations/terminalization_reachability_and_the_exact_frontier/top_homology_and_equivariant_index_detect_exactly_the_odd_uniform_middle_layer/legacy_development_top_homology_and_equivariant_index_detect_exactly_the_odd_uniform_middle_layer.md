# Top homology and equivariant index detect exactly the odd uniform middle layer — preserved pre-item development

## Composition

(none yet)

## Development

Let H be a minimum-order counterexample on n vertices, E(H) its signed support-pair downward-closure complex, and D its full cubical deletion interface. Then dim E(H)=n-2.

The following conditions are equivalent:
(i) H_(n-2)(E(H); F_2) is nonzero;
(ii) the cube graph after removing D is disconnected;
(iii) D is a nonempty cubical 1-cocycle;
(iv) n=2r+1, every r-set is Hamiltonian, and every (r+1)-set is non-Hamiltonian;
(v) E(H) is the full signed complex of disjoint A,B with |A|,|B|<=r;
(vi) the Z_2-index of E(H) is n-2, where index means the minimum d admitting an equivariant map to the antipodal d-sphere.

Proof of (i)-(v).
A nonzero top mod-two cycle is a nonempty set of top deletion facets with even incidence at every codimension-one face. In the dual cube it is a nonempty cocycle C contained in D. The prefix-chain theorem 272 forces C=D; complement connectivity and 269 give (ii)-(iv).
Under (iv), a Hamiltonian support has order at most r, by the contiguous-subpath argument. Any disjoint A,B with sizes at most r can be enlarged disjointly to r-sets, both Hamiltonian. Hence (v). Conversely (v) includes all actual middle-layer facets and gives their nonzero top cycle.

An explicit equivariant sphere realization, avoiding a separate appeal to the Bier sphere theorem.
Let W={x in R^n:sum x_i=0} and take its unit Euclidean sphere S(W), of dimension n-2.
For x in S(W), let m(x) be the median of its 2r+1 coordinates. Put
F(x)=(x-m(x)1)/||x-m(x)1||_1.
The median leaves at most r positive and r negative coordinates, so F(x) belongs to |E(H)| in its standard l_1 realization. The denominator is nonzero: otherwise x would be constant, contradicting sum x_i=0 and ||x||_2=1.
The median is continuous and m(-x)=-m(x), so F is continuous and equivariant.
For y in |E(H)|, its median is zero. The inverse is
G(y)=(y-mean(y)1)/||y-mean(y)1||_2.
Both denominators are nonzero and direct substitution verifies F G=identity and G F=identity. Thus E(H) is equivariantly homeomorphic to the standard antipodal S^(n-2). In particular its index is n-2.

If (i) fails, 272 shows every nonempty top collection has a unique-incidence face. Paired antipodal elementary collapses remove every top facet and yield an equivariant deformation retraction onto a free complex of dimension at most n-3. Any finite free k-dimensional Z_2-complex admits an equivariant map to S^k (extend over cells, choosing opposite cells equivariantly). Hence index E(H)<=n-3. This proves the equivalence with (vi).

Interpretation.
For a minimum counterexample, a universal lower bound index E(H)>=n-2 would FORCE the odd uniform family. It would not yet force a spanning two-cover: that family already realizes the whole antipodal sphere in precisely that dimension.
The stronger bound index E(H)>=n-1 is the genuine closure target, as in 243. Alternatively a separate tournament argument excluding the uniform family, together with the n-2 lower bound, would close.
Top-dimensional homology, complement separation, and maximal possible index are therefore the SAME obstruction in this setting, rather than three independent ways to eliminate it.

Limits. Neither the n-2 lower bound nor the Hamiltonian unrealizability of the odd middle layer is proved here. The explicit median homeomorphism explains why an unqualified appeal to stronger generic topology cannot by itself eliminate the surviving middle sphere.
