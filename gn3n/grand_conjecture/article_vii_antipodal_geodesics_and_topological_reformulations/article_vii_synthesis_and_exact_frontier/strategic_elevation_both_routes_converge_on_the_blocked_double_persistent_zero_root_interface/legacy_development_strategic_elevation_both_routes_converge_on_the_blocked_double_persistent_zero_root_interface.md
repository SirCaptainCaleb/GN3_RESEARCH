# Strategic elevation: both routes converge on the blocked double-persistent zero-root interface — preserved pre-item development

## Strategic elevation: the two Article VII routes now meet at one blocked zero-root interface

Recent developments materially change where effort should be spent.

### 1. The exact-root route has eliminated high-distance nonzero recurrence

By [[elevation_four_vertex_exact_root_compression_sharpens_the_surplus_bound_to_two]], augmenting the exact-root map by \(k+2\) role coordinates and using the four-vertex central-block theorem shows:

> if a positive augmented exact-root carrier has no zero root, then
> \[
> \kappa_2(H)\le2.
> \]

Thus no hypothetical obstruction of deletion distance at least three can remain indefinitely in the nonzero-root recurrence branch. At high deletion distance the topology is forced onto the diagonal
\[
p=c,
\]
the symmetric zero-root geometry.

### 2. The positive-witness separator has isolated the unbounded part of that same diagonal

By [[persistent_face_labels_isolate_the_double_persistent_zero_root_locus]], a long protected reflected span-two zero face has only two possibilities:

- it already contains an outward chamber; or
- both reflected positive occurrences persist in every chamber.

Every chamber in the second case is a symmetric zero-root chamber on its full reflected determining span. Hence the unbounded obstruction surviving the positive-witness separator is exactly a **double-persistent zero-root locus**.

This is the same geometric layer onto which the exact-root route is forced.

### 3. Most of the face geometry of the double-persistent locus is already harmless

The persistent-window footprint theorem and its correction show that:

- every interior face block has bounded width;
- an endpoint reservoir can meet a determining window in at most two positions;
- arbitrarily many neutral interior factors may be collapsed by frozen-window carriers;
- a one-slot endpoint reservoir has a contractible successful-buffer locus by [[frozen_interiors_make_buffer_success_sectors_contractible]];
- a two-slot endpoint reservoir is not an arbitrary ordered-pair problem: [[two_slot_persistent_boundary_reservoirs_are_uniformly_blocked_and_rooted]] shows persistence forces it to be uniformly blocked and supplies rooted Hamilton four-paths.

Thus the remaining unboundedness is not corridor length, Coxeter rank, or arbitrary endpoint tuple complexity.

### 4. The actual remaining seam

After these reductions, the only genuinely new local combinatorics is the following.

Take a double-persistent mixed reflected span-two face. Freeze its neutral interior. At each endpoint either:

1. a buffer-success sector exists, in which case that whole sector has a natural contractible outward carrier; or
2. the endpoint reservoir is uniformly blocked, so all permitted labels satisfy the same reverse-root relations.

If both ends lie in the blocked alternative, persistence additionally supplies fixed inward tight triples from the endpoint words
\[
011\qquad\text{and}\qquad001.
\]
The blocked reservoirs therefore meet the corridor through a bounded rooted interface with genuine endpoint control.

This is now the strategically preferred attack:

\[
\boxed{
\text{double-persistent zero root}
+
\text{uniformly blocked endpoint reservoirs}
\Longrightarrow
\begin{cases}
\text{two-cover},\\
\text{enlarged-window outward repair},\\
\text{or a separator reduction to already contractible sectors.}
\end{cases}}
\]

The point is not merely that this statement is narrower than the old reflected-double packet theorem. It sits at the intersection of the two strongest Article VII reductions. Closing it would simultaneously remove the unbounded positive-witness zero locus and the symmetric zero-root branch of the exact-root route.

### 5. What should not receive primary effort now

The following are downstream or have been structurally bypassed:

- arbitrary packet-by-packet surgery for a single reflected double;
- a bounded-rank Coxeter quotient for large boundary blocks;
- an external or universal gauge;
- arbitrary same-face outward-locus acyclicity;
- higher odd moments of the exact root;
- large-radius auxiliary nearest-violation cancellation caused only by moving the auxiliary vertex.

The auxiliary-center fiber calculation [[auxiliary_center_fibers_are_two_status_deletion_fibers]] explains the last item: sliding the auxiliary vertex is a one-dimensional thickening over one fixed original order, not new GN3 geometry. Low-radius auxiliary neighborhoods remain useful because the balanced \(3|3,4|4,5|5\) theorems give center-preserving exact repairs, but the large-radius fiber itself should not be the main closure target.

### 6. Immediate technical target

At a two-slot blocked left reservoir \(B\), persistence of \(011\) gives, for every \(v\in B\),
\[
h(v,c_2,c_3)=1,
\]
in addition to the uniform polarization
\[
h(u,v,c_2)=0,\qquad h(c_2,v,u)=1
\quad(u\ne v\in B).
\]
Therefore every reservoir label \(v\) already forms the tight rooted path
\[
(v,c_2,c_3,c_4)
\]
with the fixed first inward corridor segment.

The analogous right-hand statement follows from persistent \(001\).

So the next lemma should not ask merely for a Hamiltonian bounded packet; that has already been obtained. It should ask for a **rooted handoff theorem**: use these universal one-label inward extensions at the two blocked ends, together with connector-path exclusion in the genuine \(\kappa_2=2\) layer, to either join the corridor cover after moving bounded endpoint labels, or force one of the enlarged-buffer success conditions.

This is the shortest currently visible path from Article VII development to the grand theorem.
