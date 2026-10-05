# Blocked exterior vertices either extend the opposite tail or force root advance

## Metadata

- ID: blocked_exterior_vertices_either_extend_the_opposite_tail_or_force_root_advance
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 119
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Elevation of the blocked endpoint: direct opposite-tail extension or root advance

Retain a genuine mixed reflected double
\[
J=C\sqcup\{x,y\},\qquad C=P\mid Q,
\]
with
\[
P=(p_1,p_2,\ldots),\qquad Q=(q_1,q_2,\ldots),
\qquad \kappa_2(H[J])=2.
\]
By [[genuine_two_deletion_doubles_reverse_all_four_corridor_ends]],
\[
h(p_2,p_1,x)=h(p_2,p_1,y)=1,
\qquad
h(q_2,q_1,x)=h(q_2,q_1,y)=1.
\]

Let \(z\) be an exterior vertex on a completely blocked left buffer side. Then the blocked-buffer relation gives
\[
h(p_2,p_1,z)=1.
\]

There are now exactly two possibilities at the other initial corridor edge.

### Alternative A: \(z\) directly extends the opposite tail

If
\[
h(q_2,q_1,z)=0,
\]
then boundary antisymmetry gives
\[
h(z,q_1,q_2)=1.
\]
Since \(Q\) is a tight path,
\[
(z,q_1,q_2,\ldots)
\]
is itself a tight path. Thus every blocked exterior vertex which is not a common reverser of both initial corridor edges is an immediate one-vertex extension of the opposite corridor component.

### Alternative B: \(z\) is a common reverser

If
\[
h(q_2,q_1,z)=1,
\]
then
\[
x,y,z
\]
are three common initial reversers of both \(P\) and \(Q\). Apply [[three_common_initial_reversers_force_a_root_advancing_five_path]]. Two of these three labels, say \(u,v\), give a tight five-path of one of the forms
\[
(p_2,p_1,u,q_1,v),\qquad
(p_2,p_1,v,q_1,u),
\]
or the left-right symmetric forms rooted at \(q_2\).

Hence:

> **Blocked-vertex transport dichotomy.** Every vertex on a completely blocked exterior side either extends the opposite corridor path directly, or together with the two deleted endpoint vertices forces a bounded five-path that advances one corridor root across the other component.

This uses only the genuine \(\kappa_2=2\) four-end reversal theorem, boundary antisymmetry, and the three-common-reverser lemma.

### Elevation consequence

The uniformly blocked reservoir is therefore not merely a family of failed buffer tests. Every reservoir label has a **positive transport role**:
\[
\boxed{\text{opposite-tail extender}\quad\text{or}\quad\text{root-advance witness}.}
\]

This sharpens the endpoint-repartition target. A remaining obstruction must simultaneously prevent:

1. all opposite-tail extenders from yielding an enlarged-window two-cover or usable carrier; and
2. all root-advancing five-paths from handing off to the untouched tails.

Thus the next local theorem should be stated in terms of these two transport outputs rather than in terms of arbitrary Hamiltonian endpoint packets.
