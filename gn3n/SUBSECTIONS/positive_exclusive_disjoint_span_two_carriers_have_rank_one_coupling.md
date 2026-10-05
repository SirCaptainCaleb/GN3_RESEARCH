# Positive exclusive disjoint span-two carriers have rank-one coupling

## Metadata

- ID: positive_exclusive_disjoint_span_two_carriers_have_rank_one_coupling
- Parent Section: local_witness_topology_and_the_finite_terminal_theorem
- Position: 12
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False
- Provisional declared dependencies: ["exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity", "verified_five_position_obstruction_and_ordered_tuple_compression", "positive_protection_eliminates_exclusive_disjoint_alternating_carriers", "balanced_ten_position_repairs_have_explicit_protected_endpoint_orbits"]

## Cold composition

(none yet)

## Development

## The surviving exclusive disjoint span-two carrier has a two-vertex coupling block

This strengthens the positive-word adjacency compression. The span-two branch need not be eliminated; its entire sign-changing freedom has rank one.

**Theorem.** Suppose a protected face has exactly one of two reflected, disjoint positive span-two occurrences in every chamber, and both orientations occur somewhere. Then the determining windows are adjacent, their full span has ten vertices, and the unique common block has exactly two vertices, one in each window. All other face-block factors are sign-neutral.

**Proof.** Adjacency and a unique common block \(B\) follow from [[exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity]]. Each determining window has five vertices.

The footprint bound applies also to the grouped predicate \(\{001,011\}\): it prescribes the first status zero and the last status one. If a left footprint had at least three vertices, choose a support partition with left indicator one and flip the first and third vertices of its final triple. Exclusivity makes the indicator constant under support-preserving reordering, but the flip changes the required final status one to zero. The right argument flips its required first status zero. Thus
\[
|B|=\alpha+\beta,\qquad 1\le\alpha,\beta\le2.
\]

Fix left and right exterior block orders from positive chambers as in the adjacency proof. Translate the ten vertex positions to \(1,\ldots,10\), with eight statuses \(s_1,\ldots,s_8\). Because the footprints have at most two vertices, the exterior statuses satisfy
\[
s_1=0,\qquad s_8=1
\]
throughout this fixed context. The left indicator is \(L=s_3\); the right indicator is \(R=1-s_6\). Exclusivity implies
\[
s_3=s_6=:C.
\]

Strict inward positive protection excludes span-two witnesses at starts \(2,\ldots,5\) and alternating witnesses at starts \(1,\ldots,5\). These exclusions imply
\[
s_3=s_4=s_5=s_6=C.
\]
Indeed, if \(C=1\), exclusion at starts 4 and 2 gives \(s_4=s_2=1\). If \(s_5=0\), then \(s_7=1\) gives a forbidden span-two word at start 5, whereas \(s_7=0\) gives \(0101\) at start 5. Hence \(s_5=1\).

If \(C=0\), exclusion at starts 3 and 5 gives \(s_5=s_7=0\). If \(s_4=1\), then \(s_2=0\) gives \(001\) at start 2, whereas \(s_2=1\) gives \(0101\) at start 1. Hence \(s_4=0\).

If \(|B|=3\) and \((\alpha,\beta)=(1,2)\), let the block order be \((x,y,z)\) in positions \(5,6,7\). Then
\[
h(x,y,z)=C=L(x),
\]
where \(L\) depends only on the first block vertex. Boundary antisymmetry gives \(L(z)=1-L(x)\) for every distinct \(x,z\). This is impossible on three vertices. For \((\alpha,\beta)=(2,1)\), the same argument uses the last block vertex and the internal triple on positions \(4,5,6\).

If \(|B|=4\), its positions are \(4,5,6,7\). For an order \((x,y,z,w)\),
\[
h(x,y,z)=h(y,z,w)=C=L(x,y).
\]
Rotate the block order. The shared triple forces \(L(x,y)=L(y,z)\) for all distinct \(x,y,z\). As in [[positive_protection_eliminates_exclusive_disjoint_alternating_carriers]], this makes \(L\) constant, contradicting the occurrence of both orientations.

Therefore \(|B|=2\), with \(\alpha=\beta=1\). It occupies the two central positions 5 and 6.

Finally fix either ordering of \(B\). All other determining variables on the left and right belong to disjoint collections of blocks. Since \(L+R=1\) on every independent pair of exterior choices, \(L\) is constant over all left exterior choices and \(R\) over all right exterior choices. Thus the sign depends only on the order of the two central block vertices. Since both signs occur, those two orders have opposite signs. Every other block factor is sign-neutral. \(\square\)

This rank-one statement applies only to the exclusive disjoint span-two branch. It supplies no rank bound for overlapping or reflected-double faces. It is compatible with [[positive_protection_allows_a_disjoint_single_sided_span_two_carrier]], whose two-vertex block attains the bound.

The theorem permits collapsing the entire two-vertex interaction while freezing the ten-position repair. It does not justify endpoint transport: that target-side issue remains exactly the exception identified in [[balanced_ten_position_repairs_have_explicit_protected_endpoint_orbits]]. A globally compatible choice of the frozen repair is still required.
