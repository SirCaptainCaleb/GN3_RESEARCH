# Signed-support retraction of geodesic endpoint posets and sharp equivariant index

Let \(Q_n\) have vertex set \(\{0,1\}^n\) and let \(c\) be an arbitrary binary coloring of its undirected edges. Fix a color \(a\). Denote by \(P_a(c)\) the poset of ordered distinct vertex pairs \((u,v)\) joined by a monochromatic color-\(a\) geodesic, with
\[
(u,v)\preceq(u',v')
\]
when there are color-\(a\) geodesics \(u'\to u\) and \(v\to v'\) such that
\[
d(u',v')=d(u',u)+d(u,v)+d(v,v').
\tag{1}
\]
This order and its endpoint-reversal involution \(J(u,v)=(v,u)\) were established earlier in this Article. The distance condition ensures that all concatenated subpaths traverse distinct cube dimensions.

Let \(\mathcal B_n\) be the poset of nonempty *signed dimension sets* \((S^+,S^-)\), where \(S^+,S^-\subseteq[n]\) are disjoint, ordered by inclusion in each part. Its order complex is the barycentric subdivision of the boundary of the \(n\)-crosspolytope:
\[
|\Delta\mathcal B_n|\cong S^{n-1}.
\]
The involution \(j(S^+,S^-)=(S^-,S^+)\) acts antipodally on this sphere.

**Theorem 1 (intrinsic signed-support map).** For every cube-edge coloring and either color, the assignment
\[
\boxed{\rho(u,v)=
\bigl(\{i:u_i=0,\ v_i=1\},\ \{i:u_i=1,\ v_i=0\}\bigr)}
\tag{2}
\]
is an order-preserving map \(P_a(c)\to\mathcal B_n\) satisfying
\[
\boxed{\rho(Jp)=j\rho(p).}
\tag{3}
\]
It induces a simplicial equivariant map
\[
\boxed{\Delta P_a(c)\longrightarrow\operatorname{sd}\partial\mathcal O_n.}
\tag{4}
\]
If the longest color-\(a\) geodesic has length \(L\), its image lies in the barycentric subdivision of the \((L-1)\)-skeleton of \(\partial\mathcal O_n\).

*Proof.* Suppose \(p=(u,v)\preceq p'=(u',v')\). By (1) the concatenated monochromatic paths \(u'\to u\to v\to v'\) form a cube geodesic. Every dimension in which \(u,v\) differ is consequently traversed once on this concatenation, and in the same direction as between \(u',v'\). Thus both signed parts of \(\rho(p)\) are subsets of the corresponding signed parts of \(\rho(p')\). Reversing the ordered endpoints exchanges the two signed parts, giving (3). Passing to chains gives (4). The cardinality of the support of \(\rho(u,v)\) equals \(d(u,v)\); thus the bound \(d(u,v)\le L\) places its image in the stated skeleton. \(\square\)

**Theorem 2 (equivariant retraction on a monochromatic face).** Suppose a cubical \(m\)-face \(F\subseteq Q_n\), with free dimension set \(I\) and \(m\ge1\), has all its edges colored \(a\). Let \(P_a(F)\) denote the induced endpoint poset with both endpoints in \(F\). There is an equivariant order embedding
\[
\boxed{\iota:\mathcal B_I\hookrightarrow P_a(F)}
\tag{5}
\]
such that \(\rho\circ\iota=\operatorname{id}_{\mathcal B_I}\). Consequently
\[
\boxed{S^{m-1}\cong|\Delta\mathcal B_I|
\quad\text{is a \(\mathbb Z_2\)-equivariant retract of }
|\Delta P_a(F)|.}
\tag{6}
\]
In particular, the antipodal characteristic class on the quotient of \(\Delta P_a(F)\) has nonzero \((m-1)\)-st power. Its \(\mathbb Z_2\)-index, defined as the least \(d\) admitting an equivariant map to \(S^d\), is \(m-1\).

*Proof.* Identify the free directions of \(F\) with an \(m\)-cube and use the face vertex \(0^I\) as reference. Given \(S=(S^+,S^-)\in\mathcal B_I\), define endpoints \(u(S),v(S)\) in \(F\) by
\[
\begin{array}{c|ccc}
& i\in S^+&i\in S^-&i\in I\setminus(S^+\cup S^-)\\ \hline
u(S)_i&0&1&0\\
v(S)_i&1&0&0 .
\end{array}
\tag{7}
\]
All edges of \(F\) have color \(a\), so \(\iota(S)=(u(S),v(S))\) belongs to \(P_a(F)\). If \(S\subseteq T\) as signed sets, the geodesic from \(u(T)\) to \(u(S)\) traverses the newly added negative directions, and the geodesic from \(v(S)\) to \(v(T)\) traverses the newly added positive directions. Their supports are disjoint from one another and from the support of \(\iota(S)\), proving \(\iota(S)\preceq\iota(T)\). Conversely, containment of these endpoint intervals forces signed-support inclusion by Theorem 1; thus \(\iota\) is an order embedding.

Equation (7) gives \(\iota(jS)=J\iota(S)\) and \(\rho\iota(S)=S\). Therefore \(\Delta\iota\) and \(\Delta\rho\) exhibit the required equivariant retraction. The classifying map for the free involution on \(\Delta P_a(F)\) restricts along the embedded sphere quotient to that of \(\mathbb{RP}^{m-1}\), where the \((m-1)\)-st power of the degree-one class is nonzero. Hence the same power is nonzero on \(\Delta P_a(F)/J\). The map \(\rho\) supplies an equivariant map to \(S^{m-1}\), establishing the index claim. \(\square\)

**Theorem 3 (translation components of lower fibers).** In the setting of Theorem 2, fix a signed set \(S\in\mathcal B_I\) of cardinality \(k\). The lower fiber
\[
\boxed{\rho^{-1}(\mathcal B_{I,\le S})\subseteq P_a(F)}
\tag{8}
\]
is a disjoint union of \(2^{m-k}\) subposets, each possessing a greatest element. Therefore its order complex has the homotopy type of \(2^{m-k}\) discrete points.

*Proof.* An ordered endpoint pair in the fiber can differ only in the dimensions of \(S\), and every such difference must follow the corresponding orientation sign. The common bits outside \(\operatorname{supp}S\) are constant along comparisons in the fiber; hence the fiber splits into \(2^{m-k}\) subposets, indexed by these bits. In each such \(k\)-face, let \(p_{S,z}\) be the oriented pair differing in all \(k\) directions according to \(S\). It is monochromatically joined because the whole face is color \(a\). Every other interval in that subposet is contained in this full interval as in (1): first traverse the directions whose fixed endpoint bit equals the ending bit of \(p_{S,z}\), then the shorter interval, and finally the remaining directions. Thus \(p_{S,z}\) is a greatest element and each component is a cone. \(\square\)

**Consequences for the equivariant-chain program.** The signed-support map is defined for the unrestricted coloring class and records precisely the orientation and set of dimensions traversed by every monochromatic geodesic. Under a hypothetical NORI1 counterexample, the length-\((n-1)\) extension lemma proved earlier excludes every color-\(a\) geodesic of length \(n-1\) or \(n\), so (4) lands in an \((n-3)\)-dimensional complex. The desired contradiction would follow from an antipodally equivariant chain map from the cubical boundary sphere into \(\Delta P_a(c)\), as explained in the endpoint-poset construction.

Theorems 2–3 identify two constraints on such a construction. A monochromatic \(m\)-face already forces equivariant index \(m-1\) inside the target; consequently the elementary support bound is topologically sharp on these faces. Further, lower fibers of \(\rho\) can be disconnected even for an entirely monochromatic cube. Thus a carrier argument cannot replace the endpoint poset by the signed-face poset through a claim that all lower fibers are contractible. The different translates of a signed subface must be retained in the chain assignments.
