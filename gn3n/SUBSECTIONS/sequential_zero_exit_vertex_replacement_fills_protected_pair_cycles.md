# Sequential zero-exit vertex replacement fills protected pair cycles

## Metadata

- ID: sequential_zero_exit_vertex_replacement_fills_protected_pair_cycles
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 154
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Sequential zero-exit vertex replacement fills a protected terminal-pair cycle

Work in the terminal-pair clique-complex model before a fixed following label \(z\). Let
\[
C_0=(v_1,v_2,\ldots,v_m,v_1)
\]
be a cycle in the mutual-pair graph, representing a loop in the fixed-\(z\) outward locus. Each movable label \(w\) has an exit value
\[
\delta(w)\in\{0,1\}.
\]

Suppose the labels of \(C_0\) having nonzero exit can be eliminated by the following finite replacement process.

At stage \(i\), let
\[
\ell_i-v_i-r_i
\]
be the two cycle edges incident with a current cycle vertex \(v_i\) satisfying \(\delta(v_i)=1\). Choose a fresh movable label \(y_i\) with
\[
\delta(y_i)=0
\]
such that \(y_i\) is mutually admissible before \(z\) with all three labels
\[
\ell_i,\quad v_i,\quad r_i.
\]
Replace the segment
\[
\ell_i-v_i-r_i
\]
of the current cycle by
\[
\ell_i-y_i-r_i.
\]
Assume the process terminates with a cycle \(C_N\) all of whose labels have zero exit status.

Then the original loop represented by \(C_0\) is null-homotopic in the enlarged outward locus.

### Proof

At one replacement step, mutual admissibility of \(y_i\) with
\[
\ell_i,v_i,r_i
\]
puts the two triangles
\[
\{\ell_i,v_i,y_i\},
\qquad
\{v_i,r_i,y_i\}
\]
in the terminal-pair clique complex. Their union gives a homotopy replacing the old two-edge segment
\[
\ell_i-v_i-r_i
\]
by
\[
\ell_i-y_i-r_i.
\]
Thus \(C_{i-1}\) and \(C_i\) represent homotopic loops in the fixed-\(z\) pair locus.

Iterating, the original loop \(C_0\) is homotopic to the final cycle \(C_N\).

Every terminal label occurring on \(C_N\) has zero exit status. Therefore the subcomplex carried by those terminal labels maps null-homotopically into the enlarged outward locus by merging its final free block with \(z\), exactly as in the zero-exit inclusion of [[moving_the_following_label_has_an_exact_first_homology_kernel]] and the endpoint-enlargement contraction.

Hence \(C_N\), and therefore \(C_0\), is null-homotopic.

### Consequences

1. Case (3) of [[a_four_cycle_has_an_exact_six_label_repair_classification_with_one_exterior_label]] is the one-step instance of this theorem.

2. [[two_opposite_nonzero_exits_admit_independent_two_label_repair]] is the two-step commuting instance in which the two bad vertices are nonadjacent, so the two replacements do not need any mutual edge between the new labels.

3. Adjacent bad vertices can also be repaired: after replacing the first one, the exterior replacement label becomes a current neighbor of the second. The second replacement therefore requires mutual admissibility to that first exterior label in addition to the remaining old neighbor.

The protected-loop frontier can thus be stated purely combinatorially:

> produce a sequence of zero-exit exterior labels that successively replaces every nonzero-exit vertex of the terminal-pair cycle.

A universal exterior cone is sufficient but no longer necessary. The required adjacency pattern adapts locally as the cycle is repaired.
