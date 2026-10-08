# Wu--Yang chain-level Borsuk--Ulam proof of Norine's conjecture

**Summary:** Norine's original non-geodesic antipodal-coloring conjecture is proved by reducing to rook labels and excluding them with a Freudenthal/chain-level Borsuk--Ulam obstruction.

## Statement

Hehui Wu and Ningyuan Yang prove Norine's conjecture: every antipodal red-blue edge-coloring of Q_n, n>=2, contains a monochromatic path joining a vertex to its antipode. Their proof reduces a hypothetical counterexample to an antipodally symmetric rook labeling and rules that labeling out via a Freudenthal-based equivariant chain map into a root sphere together with a purely algebraic chain-level Borsuk--Ulam obstruction.

## Body


### Literature theorem

Hehui Wu and Ningyuan Yang, *A Chain-Level Borsuk--Ulam Obstruction Proof of Norine's Antipodal-Coloring Conjecture* (arXiv:2607.19276, 2026), prove:

> For every \(n\ge2\), every red--blue edge-coloring of \(Q_n\) in which antipodal edges receive opposite colors contains a monochromatic path joining some vertex to its antipode.

The theorem is non-geodesic. The authors explicitly leave geodesic strengthenings open.

### Proof architecture

The proof is best remembered as a sequence of reusable transformations rather than as one long topological argument.

#### 1. Counterexample \(\Rightarrow\) rook labeling

Assume no monochromatic antipodal path exists. Let
\[
C_1,\ldots,C_r
\]
be the connected components of the red spanning subgraph, and let \(p(x)\) denote the red component containing \(x\).

Define
\[
q_0(x)=\bigl(p(x),p(Ax)\bigr),
\]
where \(A\) is cube antipodality.

The two coordinates are distinct, since equality would place \(x\) and \(Ax\) in one red component. Also
\[
q_0(Ax)=\tau q_0(x),
\qquad
\tau(a,b)=(b,a).
\]

For a red edge \(xy\), the first coordinate is constant; for a blue edge, the antipodal edge is red, so the second coordinate is constant. Thus adjacent cube vertices move like a rook:
\[
(a,b)\to(a',b)
\quad\text{or}\quad
(a,b)\to(a,b').
\]

This reduction is strikingly general: a global connectivity failure is encoded by a local coordinate-pair rule.

#### 2. Dimension padding

If the number \(r\) of red components exceeds \(n\), enlarge the cube to
\[
Q_K=Q_n\times Q_{K-n},
\qquad
K\ge\max\{n,r\},
\]
and keep the rook label constant in the added coordinates after injecting \([r]\) into \([K]\).

This matches cube dimension and label set size without changing the obstruction. The resulting task is purely combinatorial:

\[
\text{there is no rook labeling }Q_K\to\Omega_K,
\qquad
\Omega_K=\{(a,b):a\ne b\}.
\]

#### 3. Rook labels \(\Rightarrow\) type-\(A\) roots

Associate
\[
(a,b)\longmapsto e_a-e_b
\]
in
\[
W_K=\left\{z\in\mathbb R^K:\sum_i z_i=0\right\}.
\]

Swapping the rook coordinates negates the root:
\[
e_b-e_a=-(e_a-e_b).
\]

Thus the antipodal rook symmetry becomes ordinary antipodal symmetry on
\[
S(W_K)\cong S^{K-2}.
\]

This root encoding is useful whenever an ordered pair has coordinate-swap antipodality.

#### 4. Freudenthal subdivision as a chain map

The cubical boundary
\[
\partial I^K\cong S^{K-1}
\]
is subdivided by the standard Freudenthal triangulation.

For each cubical face \(F\), take the mod-2 sum of its maximal Freudenthal simplices. Internal facets appear twice and cancel, so this assignment is itself a chain map from cubical cellular chains to simplicial chains.

The vertices of every maximal Freudenthal simplex form a monotone cube path. Therefore their rook labels form a rook gallery. This is the key place where local rook behavior becomes coherent along a simplex.

#### 5. Gallery roots \(\Rightarrow\) spherical polyhedral chains

For a simplex carrying root labels
\[
v_0,\ldots,v_j,
\]
take the intersection of the positive cone
\[
\operatorname{cone}_{\ge0}\{v_0,\ldots,v_j\}
\]
with the unit sphere when the roots are linearly independent; assign zero when they are dependent.

These spherical polytopes need not form a face-to-face complex globally. Wu--Yang therefore introduce a subdivision-invariant polyhedral chain group: a polytope is identified with the mod-2 sum of the pieces in any subdivision.

This is an important technical device. It permits chain-level geometry even when naturally produced cells overlap badly or require repeated refinement.

#### 6. Degenerate radial cancellation

To prove the radial assignment is a chain map, degenerate simplices must disappear correctly. A mod-2 radial cancellation identity, together with a rank bound specific to rook galleries, handles the dependent cases.

Reusable lesson: if a local labeling produces positive cones rather than a genuine simplicial map, one can sometimes work directly with chain-valued cone sections and prove cancellation algebraically.

#### 7. Chain-level Borsuk--Ulam obstruction

The composite has the form
\[
C_*^{\mathrm{cell}}(\partial I^K;\mathbb F_2)
\longrightarrow
C_*^{\mathrm{simp}}(\text{Freudenthal subdivision};\mathbb F_2)
\longrightarrow
C_*^{\mathrm{poly}}(S(W_K);\mathbb F_2).
\]

It is antipodally equivariant and augmentation-preserving.

The source is the chain complex of \(S^{K-1}\); the target has no chains above dimension \(K-2\). On the target, with antipodal involution \(U\), the norm operator
\[
\nu=\mathrm{id}+U
\]
satisfies
\[
\ker\nu=\operatorname{im}\nu
\]
in every relevant degree.

Wu--Yang prove a purely algebraic obstruction: under the source exactness assumptions, target dimension bound, and the displayed kernel-image identity, no equivariant augmentation-preserving chain map can exist.

This is a chain-level version of the \(\mathbb Z_2\) Dold/Borsuk--Ulam obstruction. Crucially, the constructed chain map need not come from any continuous map.

### Techniques especially reusable for NOR

1. **Component-pair compression.** Encode a failed connectivity conclusion by a pair of component indices at \(x\) and \(Ax\).
2. **Rook locality.** Arrange that each local move preserves one coordinate.
3. **Dimension padding.** Add dummy cube directions until combinatorial dimension matches label dimension.
4. **Rootification.** Send a swap-antipodal pair \((a,b)\) to \(e_a-e_b\).
5. **Freudenthal coherence.** Convert local edge behavior into gallery behavior on monotone simplices.
6. **Subdivision-invariant chain targets.** Work with chains modulo arbitrary subdivisions when natural geometric images fail to form a clean complex.
7. **Chain-valued maps instead of point maps.** A continuous equivariant map is not necessary if one can build a coherent equivariant chain map.
8. **Algebraic Borsuk--Ulam.** The contradiction can be driven by exactness, dimension, augmentation, equivariance, and the norm-operator identity alone.
9. **Degeneracy by cancellation.** Dependent root configurations can be sent to zero provided boundary terms cancel mod 2.
10. **Separation of geodesic content.** The proof uses Freudenthal monotone galleries internally but proves only existence of an arbitrary monochromatic antipodal path. Recovering a geodesic conclusion requires an additional mechanism; it does not follow merely from the chain obstruction.

### NOR relevance

The most promising transfer is not to imitate the theorem statement directly, but to imitate the architecture:

\[
\text{failure of one-change geodesic}
\to
\text{structured directed labels}
\to
\text{Freudenthal/Coxeter gallery chains}
\to
\text{root or cone chains}
\to
\text{equivariant chain obstruction}.
\]

For ordered-tuple NOR, a major advantage is that arbitrary antipodal geodesics already carry the directed local data natively. Thus one can ask whether a counterexample yields a rook-like or higher-rank label system on directed windows whose gallery chains admit the same kind of chain-level obstruction.


## Metadata

- ID: literature_wu_yang_norine_chain_level_borsuk_ulam
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
