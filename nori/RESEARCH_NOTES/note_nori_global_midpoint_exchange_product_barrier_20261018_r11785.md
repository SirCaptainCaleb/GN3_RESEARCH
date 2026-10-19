# Product and cyclic paired-flat colorings require global midpoint order exchanges

- Stable ID: note_nori_global_midpoint_exchange_product_barrier_20261018_r11785
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, midpoint-collision, tensor-product, order-exchange, method-obstruction, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11785_1
- Updated session: session_nori_r11785_1
- Disposition: none
- Successor: none

## Related references

- note:note_nori_xvi_midpoint_tensor_product_and_scarcity_barrier_20261018_r11755

## Research note

# Product of paired-flat four-cubes requires globally distributed midpoint exchanges

Let \(r\ge2\) and let \(c=c^{(1)}\boxdot\cdots\boxdot c^{(r)}\) be the disjoint-block product of arbitrary legal paired-flat colorings \(c^{(j)}\) of \(Q_4\). Each factor has two direction pairs \(a_j,b_j\), so the product has \(m=2r\) pairs. For a full pair ordering \(\pi\), the endpoint of its red half-sweep in factor \(j\) is the endpoint of the two-pair sweep with induced order \(\pi|_{\{a_j,b_j\}}\).

**Theorem.** If \(F_\pi(x)=F_\rho(\bar x)\), the orders \(\pi\) and \(\rho\) induce opposite relative orders on \(a_j,b_j\) for **every** factor \(j\). Consequently, there is no such midpoint collision between orders differing only by a permutation of a proper contiguous block of fewer than \(m\) pair labels, with a common initial and final word outside that block.

**Proof.** The two red pair matchings in each factor are involutions. Their composition in either of the two possible pair orders is therefore a permutation of that factor's vertex set. If \(\pi,\rho\) have the same restriction to some factor, their projected collision equality would assert \(F(x_j)=F(\bar x_j)\) for that permutation \(F\), contradicting \(x_j\ne\bar x_j\). Thus both labels in every two-pair factor must reverse relative order.

Now suppose \(\pi,\rho\) agree outside a contiguous word block whose pair-label set is \(K\subsetneq\{1,\dots,m\}\), and reorder only the labels of \(K\). Since \(K\) omits some label from some factor, at least one factor has at most one label in \(K\). The relative order of that factor's two labels is unchanged: the omitted label stays in the common prefix or suffix, and the other label either stays fixed or moves inside the same middle block. This contradicts the first assertion. \(\square\)

Each \(Q_4\) factor has \(W=8\) midpoint collisions, and the established tensor formula gives \(W(c)=\binom{2r}{2,\ldots,2}^{\,2}8^r>0\). Thus these colorings are good while all their midpoint collisions require exchanges reaching every pair block.

**Scope.** This disproves any universal hypothesis asserting a midpoint collision for two orders differing inside at most \(m-1\) consecutive pair labels, even for legal balanced paired-flat colorings that have many full red antipodal geodesics. It does not concern exchanges in nonlinear interaction-prime colorings or exclude square-switch preservation. It delimits the use of the small-rank local-exchange stability criterion in the same Subsection.

## Interaction-prime cyclic gates give the same nonlocal-exchange obstruction

For any \(m\ge3\), identify each pair's fiber bit with \(t_i\), with indices modulo \(m\), and define the paired-flat gate \(f_i(p,t)=t_{i+1}\). It is independent of pair \(i\), and \(f_i(p,t+\mathbf1)=1+f_i(p,t)\), so the coloring is legal. The reader graph is the directed \(m\)-cycle and therefore has no nontrivial independent-factor partition.

**Theorem.** If two complete pair orders \(\pi,\rho\) agree on a common prefix and suffix, differing only by reordering the same proper middle set \(K\subsetneq[m]\), then
\[
F_\pi^p(t)\ne F_\rho^p(t+\mathbf1)
\]
for every parity fiber \(p\) and every root \(t\). The set \(K\) need not be small or an interval in cyclic label order.

**Proof.** Apply the common prefix to the two antipodal starts, obtaining fiber states \(y,y'\). Since no prefix pair lies in \(K\), \(y_i'=y_i+1\) for each \(i\in K\). If the complete sweep endpoints were equal, applying the inverse of their common suffix would make the two middle-sweep endpoints equal. The middle sweeps never change bits outside \(K\); hence \(y_j'=y_j\) for all \(j\notin K\). Because the directed reader graph is a single cycle and \(K\) is a proper nonempty set, some \(i\in K\) has \(i+1\notin K\). Throughout each middle sweep the reader bit \(t_{i+1}\) is fixed, with the same value on both sides. The unique occurrence of pair \(i\) therefore makes the same change \(1+t_{i+1}\) to each \(t_i\). Their values still differ by one at the end of the middle sweeps, contrary to equality. If \(K\) is empty, the orders coincide and the bijection property excludes antipodal collision. \(\square\)

**Compensating global low-rank collision.** Despite the nonlocal requirement, take \(\pi=(0,1,\ldots,m-1)\), \(\rho=(1,\ldots,m-1,0)\). The equations for \(F_\pi^p(t)=F_\rho^p(t+\mathbf1)\) reduce to \(t_1=1\) and \(t_2=0\); all other bits are free. Thus these two globally differing orders meet at \(2^{m-2}\) roots per parity fiber. Their affine linear endpoint-map difference has rank two. In particular, in dimensions \(m\ge6\), the four-root square-switch theorem certifies survival of a red full antipodal geodesic after any single paired-square switch by this one pair of orders.

**Scope.** Products of Q4 factors are disconnected reader systems; cyclic gates have a strongly connected reader graph. Both classes disprove universal midpoint-witness locality. Therefore neither goodness nor interaction-primality alone supplies a short changed-order block. The positive rank-two global collision shows that bounding the rank of an endpoint-map difference need not require a short exchange.
