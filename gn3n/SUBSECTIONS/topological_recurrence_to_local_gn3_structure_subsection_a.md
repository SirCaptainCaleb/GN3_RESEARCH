# From balanced recurrence to local reversal structure

## Metadata

- ID: topological_recurrence_to_local_gn3_structure_subsection_a
- Parent Section: topological_recurrence_to_local_gn3_structure
- Position: 1
- Row version: 5
- Development version: 5
- Composition version: 1
- Composition stale: False

## Cold composition

### Determining positions and positive face balance

Let \(F=B_1|\cdots|B_k\) be a proper permutahedral face, with its blocks occupying consecutive positions. Assume its chamber roots admit a circulation strictly positive on every occurring root, as provided by [[convex_root_balance_and_bourgin_yang]]. Then every coordinate occurring as a first switch also occurs as a reflected last switch in the same face. Every chamber belongs to a directed root cycle, unless it has a zero root and is already an exact diagonal.

This is stronger than choosing just one cycle. The following deductions explain what can be extracted without assuming that convex balance is already a two-cover.

### Block separation with explicit determining windows

A first switch at \(x\) is determined by the first \(x+1\) statuses and hence by vertex positions
\[
1,\ldots,x+3.
\]
A reflected last switch at \(x\) is determined by the last \(x+1\) statuses and hence by positions
\[
n-x-2,\ldots,n.
\]

**Lemma 7.1.** Suppose \(F\) has a chamber with first switch \(x\), a chamber with reflected last switch \(x\), and a block boundary after position \(j\) such that
\[
x+3\leq j\leq n-x-3.
\]
Then \(F\) contains a chamber with root zero.

**Proof.** Use the block orders from the first witness in every block up to the boundary, and those from the second witness after it. Both determining windows remain unchanged. The resulting chamber has \(a=\bar b=x\). \(\square\)

Consequently, if \(F\) contains no diagonal and the displayed interval of possible boundaries is nonempty, all positions
\[
x+3,\ldots,n-x-2
\]
lie in a single block. Its size is at least \(n-2x-4\).

**Corollary 7.2.** Under strictly positive face balance and absence of a diagonal, let \(r\) be the least switch coordinate occurring in any chamber root of \(F\). If \(n\geq2r+6\), one block contains positions \(r+3,\ldots,n-r-2\). It also contains every nonempty corridor of this form for any larger occurring coordinate.

**Proof.** Positive balance supplies both kinds of witness for \(r\), so Lemma 7.1 excludes all boundaries in its corridor. Corridors for larger coordinates are nested inside it. \(\square\)

This gives a single block for all occurring root coordinates, not only those of a selected cycle. If \(n<2r+6\), this separation lemma gives no block conclusion. Near-central coordinates must be treated by a separate argument; their numerical location alone does not prove a bounded-support descent.

### Cross-intersecting determining families

Fix the orders of all blocks other than a chosen block \(B\), and fix a coordinate \(x\) whose two determining windows are disjoint. Let \(\mathcal L_x\) consist of the sets of labels of \(B\) occupying its positions in the left window in some chamber with first switch \(x\). Define \(\mathcal R_x\) analogously for reflected last switch \(x\). Witness orders of these sets inside the corresponding positions are retained when combining them.

**Lemma 7.3.** If no chamber with these fixed outside orders has root zero, then every \(L\in\mathcal L_x\) intersects every \(R\in\mathcal R_x\).

**Proof.** If the sets were disjoint, place each in its own determining positions using its witness order, and fill the remaining positions of \(B\) arbitrarily. The disjoint windows and the fixed outside orders preserve both witnesses. This produces a diagonal. \(\square\)

The qualification about outside orders is essential: face balance supplies witnesses somewhere in \(F\), not automatically witnesses with every prescribed choice of outside block orders.

If both families are nonempty, any member of \(\mathcal L_x\) is a transversal of \(\mathcal R_x\). An inclusion-minimal transversal \(T\) contained in it has, for each \(v\in T\), a member of \(\mathcal R_x\) meeting \(T\) exactly at \(v\); otherwise \(v\) could be removed. This preserves the private-witness mechanism without asserting an absolute bound on \(|T|\). Such a bound would require a bound on the number of determining positions inside \(B\).

### Front motion with the witness hypotheses retained

**Lemma 7.4.** Fix all outside block orders. Suppose a permutation of \(B\) realizes first switch \(x\), another realizes reflected last switch \(x\), and no permutation of \(B\) realizes a diagonal. Then an adjacent transposition within \(B\) changes the first switch coordinate.

**Proof.** In the second witness, the first switch cannot equal \(x\). The adjacent-transposition graph of the permutations of \(B\) is connected. Along a path between the two witnesses, at least one swap changes the first switch. \(\square\)

If positions \(j,j+1\) are swapped, only triple positions \(j-2,\ldots,j+1\) can change, clipped to \(1,\ldots,m\). Consequently only switch positions \(j-3,\ldots,j+1\) can change. If two resulting first-switch coordinates \(a<a'\) differ, the earlier coordinate \(a\) lies in this five-position interval; the word with first switch \(a'\) is constant through position \(a'\). Thus a long displacement has a monochromatic interval, while the cause of the displacement is local. The same statement holds for last switches by reversal.

### The conversion problem after face recurrence

Boundary antisymmetry turns each specified non-tight triple into its reversed tight triple. By itself, however, the preceding face geometry does not yet synchronize arbitrary left and right witnesses: a moved front need not already be one exterior vertex reversing two required end edges, and witnesses with different outside block orders need not have disjoint exposed edges.

The next subsection resolves precisely this issue without trying to synchronize two arbitrary chambers. Instead one minimizes switch span inside the carrier face and transports the **same physical carrier** to the two extreme fronts of a single chamber. The common-block conclusion above keeps both tests inside the face, while minimality prevents inward front motion. This produces the required local reversal structure and removes the formerly global synchronization problem.

The local path-cover mechanisms used after that compression are recorded in [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], [[endpoint_transport_and_small_support_gluing_the_remaining_lemma]], and [[defect_lines_and_spanning_order_compression_the_remaining_lemma]].


## Development

### Determining positions and positive face balance

Let \(F=B_1|\cdots|B_k\) be a proper permutahedral face, with its blocks occupying consecutive positions. Assume its chamber roots admit a circulation strictly positive on every occurring root, as provided by [[convex_root_balance_and_bourgin_yang]]. Then every coordinate occurring as a first switch also occurs as a reflected last switch in the same face. Every chamber belongs to a directed root cycle, unless it has a zero root and is already an exact diagonal.

This is stronger than choosing just one cycle. The following deductions explain what can be extracted without assuming that convex balance is already a two-cover.

### Block separation with explicit determining windows

A first switch at \(x\) is determined by the first \(x+1\) statuses and hence by vertex positions
\[
1,\ldots,x+3.
\]
A reflected last switch at \(x\) is determined by the last \(x+1\) statuses and hence by positions
\[
n-x-2,\ldots,n.
\]

**Lemma 7.1.** Suppose \(F\) has a chamber with first switch \(x\), a chamber with reflected last switch \(x\), and a block boundary after position \(j\) such that
\[
x+3\leq j\leq n-x-3.
\]
Then \(F\) contains a chamber with root zero.

**Proof.** Use the block orders from the first witness in every block up to the boundary, and those from the second witness after it. Both determining windows remain unchanged. The resulting chamber has \(a=\bar b=x\). \(\square\)

Consequently, if \(F\) contains no diagonal and the displayed interval of possible boundaries is nonempty, all positions
\[
x+3,\ldots,n-x-2
\]
lie in a single block. Its size is at least \(n-2x-4\).

**Corollary 7.2.** Under strictly positive face balance and absence of a diagonal, let \(r\) be the least switch coordinate occurring in any chamber root of \(F\). If \(n\geq2r+6\), one block contains positions \(r+3,\ldots,n-r-2\). It also contains every nonempty corridor of this form for any larger occurring coordinate.

**Proof.** Positive balance supplies both kinds of witness for \(r\), so Lemma 7.1 excludes all boundaries in its corridor. Corridors for larger coordinates are nested inside it. \(\square\)

This gives a single block for all occurring root coordinates, not only those of a selected cycle. If \(n<2r+6\), this separation lemma gives no block conclusion. Near-central coordinates must be treated by a separate argument; their numerical location alone does not prove a bounded-support descent.

### Cross-intersecting determining families

Fix the orders of all blocks other than a chosen block \(B\), and fix a coordinate \(x\) whose two determining windows are disjoint. Let \(\mathcal L_x\) consist of the sets of labels of \(B\) occupying its positions in the left window in some chamber with first switch \(x\). Define \(\mathcal R_x\) analogously for reflected last switch \(x\). Witness orders of these sets inside the corresponding positions are retained when combining them.

**Lemma 7.3.** If no chamber with these fixed outside orders has root zero, then every \(L\in\mathcal L_x\) intersects every \(R\in\mathcal R_x\).

**Proof.** If the sets were disjoint, place each in its own determining positions using its witness order, and fill the remaining positions of \(B\) arbitrarily. The disjoint windows and the fixed outside orders preserve both witnesses. This produces a diagonal. \(\square\)

The qualification about outside orders is essential: face balance supplies witnesses somewhere in \(F\), not automatically witnesses with every prescribed choice of outside block orders.

If both families are nonempty, any member of \(\mathcal L_x\) is a transversal of \(\mathcal R_x\). An inclusion-minimal transversal \(T\) contained in it has, for each \(v\in T\), a member of \(\mathcal R_x\) meeting \(T\) exactly at \(v\); otherwise \(v\) could be removed. This preserves the private-witness mechanism without asserting an absolute bound on \(|T|\). Such a bound would require a bound on the number of determining positions inside \(B\).

### Front motion with the witness hypotheses retained

**Lemma 7.4.** Fix all outside block orders. Suppose a permutation of \(B\) realizes first switch \(x\), another realizes reflected last switch \(x\), and no permutation of \(B\) realizes a diagonal. Then an adjacent transposition within \(B\) changes the first switch coordinate.

**Proof.** In the second witness, the first switch cannot equal \(x\). The adjacent-transposition graph of the permutations of \(B\) is connected. Along a path between the two witnesses, at least one swap changes the first switch. \(\square\)

If positions \(j,j+1\) are swapped, only triple positions \(j-2,\ldots,j+1\) can change, clipped to \(1,\ldots,m\). Consequently only switch positions \(j-3,\ldots,j+1\) can change. If two resulting first-switch coordinates \(a<a'\) differ, the earlier coordinate \(a\) lies in this five-position interval; the word with first switch \(a'\) is constant through position \(a'\). Thus a long displacement has a monochromatic interval, while the cause of the displacement is local. The same statement holds for last switches by reversal.

### The conversion problem after face recurrence

Boundary antisymmetry turns each specified non-tight triple into its reversed tight triple. By itself, however, the preceding face geometry does not yet synchronize arbitrary left and right witnesses: a moved front need not already be one exterior vertex reversing two required end edges, and witnesses with different outside block orders need not have disjoint exposed edges.

The next subsection resolves precisely this issue without trying to synchronize two arbitrary chambers. Instead one minimizes switch span inside the carrier face and transports the **same physical carrier** to the two extreme fronts of a single chamber. The common-block conclusion above keeps both tests inside the face, while minimality prevents inward front motion. This produces the required local reversal structure and removes the formerly global synchronization problem.

The local path-cover mechanisms used after that compression are recorded in [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], [[endpoint_transport_and_small_support_gluing_the_remaining_lemma]], and [[defect_lines_and_spanning_order_compression_the_remaining_lemma]].
