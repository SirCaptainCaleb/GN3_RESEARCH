# Root advance plus four-of-six leaves one wrong-root exception

## Metadata

- ID: root_advance_plus_four_of_six_leaves_one_wrong_root_exception
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 122
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Root advance plus four-of-six reduces to one wrong-root exception

Retain the common-reverser branch of [[blocked_exterior_vertices_either_extend_the_opposite_tail_or_force_root_advance]]. Thus
\[
P=(p_1,p_2,p_3,\ldots),\qquad
Q=(q_1,q_2,q_3,\ldots)
\]
are disjoint tight corridor paths and \(u,v,w\) are three common initial reversers. Suppose the root-advance lemma yields, after relabelling \(u,v\),
\[
X=(p_2,p_1,u,q_1,v)
\]
as a tight five-path. Let
\[
S=\{p_2,p_1,q_1,u,v,w\}.
\]

**Lemma (six-support / favorable root deletion / wrong-root exception).**
At least one of the following holds.

1. \(H[S]\) is Hamiltonian.
2. The five-set
   \[
   S-\{p_2\}
   \]
   is Hamiltonian.
3. The five-set
   \[
   S-\{q_1\}
   \]
   is Hamiltonian.
4. The five-set
   \[
   S-\{p_1\}
   \]
   is Hamiltonian.

Moreover, outcomes 1--3 each produce a spanning three-cover of the enlarged local configuration consisting of \(S\) together with the untouched corridor tails.

**Proof.**
If \(S\) is Hamiltonian, outcome 1 holds. Otherwise apply the established four-of-six theorem: at least four of the six vertex-deleted five-subsets of \(S\) are Hamiltonian.

One of them is already known:
\[
S-\{w\}=X
\]
is Hamiltonian. There are only three deletions of common-reverser labels,
\[
S-\{u\},\qquad S-\{v\},\qquad S-\{w\}.
\]
Since at least four deletions are Hamiltonian, at least one Hamiltonian five-subset deletes a corridor-root label in
\[
\{p_2,p_1,q_1\}.
\]
This gives outcomes 2, 3, or 4. \(\square\)

For the three-cover statements:

- In outcome 1, use the Hamiltonian six-support \(S\), together with the untouched tight tails
  \[
  (p_3,p_4,\ldots),\qquad(q_2,q_3,\ldots).
  \]
- In outcome 2, the Hamiltonian five-support \(S-\{p_2\}\) is disjoint from the tight tails
  \[
  (p_2,p_3,\ldots),\qquad(q_2,q_3,\ldots).
  \]
- In outcome 3, the Hamiltonian five-support \(S-\{q_1\}\) is disjoint from
  \[
  (p_3,p_4,\ldots),\qquad(q_1,q_2,\ldots).
  \]

Thus every common-reverser root advance either immediately enters the existing three-cover repartition theory with a Hamiltonian support of order five or six, or falls into the single exceptional deletion
\[
\boxed{S-\{p_1\}\text{ Hamiltonian}}
\]
for the displayed \(p_2\)-rooted orientation. In the left-right symmetric root-advance orientation, the unique analogous exception is deletion of \(q_1\).

This is useful because the handoff problem is no longer “make the displayed five-path concatenate to its old tail.” The four-of-six theorem allows the packet to change its Hamiltonian support. Except for the wrong-root deletion, that support releases exactly the corridor vertex needed to restore a contiguous tight tail.

The next local target is therefore the wrong-root exception: show that a Hamiltonian support
\[
\{p_2,q_1,u,v,w\}
\]
with \(u,v,w\) common reversers either admits a Hamilton order releasing \(p_2\) or \(q_1\) in the required direction, or forces an opposite-tail extension / farther witness.

## Frontier

- Development version when composed: None
- Development version now: 1
