# Minimum-counterexample closure is a one-rank support-pair extension problem

## Metadata

- ID: minimum_counterexample_closure_is_a_one_rank_support_pair_extension_problem
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 242
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Minimum-counterexample closure is a one-rank support-pair extension problem

Let \(H\) be a minimum-order counterexample to the spanning two-cover theorem. Then every proper induced subtournament satisfies the theorem. In particular, for every vertex \(x\),
\[
H-x=P_x\mid Q_x
\]
for some spanning two-cover.

Therefore
\[
\kappa_2(H)\le1.
\]
Since \(H\) itself is assumed to have no spanning two-cover,
\[
\boxed{\kappa_2(H)=1.}
\]

Using [[support_pair_rank_is_exactly_two_cover_deletion_distance]], if
\[
\mathcal P(H)=\{(A,B): A,B\text{ disjoint Hamiltonian supports},\ |A|,|B|\ge2\},
\]
then
\[
\kappa_2(H)=n-\max_{(A,B)\in\mathcal P(H)}(|A|+|B|).
\]
Hence in a minimum counterexample
\[
\boxed{\max(|A|+|B|)=n-1.}
\]

Thus every minimum counterexample already has top-rank support pairs omitting exactly one vertex, and the grand theorem asks for only one additional rank:
\[
n-1\longrightarrow n.
\]

Equivalently, closure is the following single extension problem.

> **One-rank extension target.** Given the family of one-hole support pairs
> \[
> (A_x,B_x),\qquad A_x\sqcup B_x=V(H)-\{x\},
> \]
> prove that some Hamiltonian support pair spans all of \(V(H)\).

### Consequence for Article VII strategy

All machinery whose sole purpose is to reduce a general state to
\[
\kappa_2=2
\]
is bypassed once minimum-order counterexample analysis is allowed. Genuine two-deletion states, minimum-pair graphs, five-component two-hole cores, reflected-double Boolean squares, and the associated two-hole endpoint handoffs may remain useful as auxiliary lemmas, but they are no longer the closure frontier.

The closure-relevant later results are instead those that can be moved upward to the \(\kappa_2=1\) layer:

1. fixed-hole Ky Fan and balanced deletion-state results;
2. the ordinary link tournament \(T_x\);
3. support-pair rank and Smith-chain topology;
4. common-core / support-pair carrier results;
5. four-/five-support extension results when they fill a support-pair cycle rather than merely produce a bounded support;
6. carrier-loop results if they can be interpreted as obstructions to extending the one-hole support-pair family by the final rank.

This also changes the role of deletion-cover disagreement. Path-order agreement is not a primary coordinate of the one-rank problem. A one-hole deletion state is already a top-rank vertex of \(\mathcal P(H)\), regardless of which Hamilton orders certify its two supports. Order disagreement matters only insofar as it changes the topology of the fibers or supplies a mixed support-pair filling.

### Topological restatement

If \(H\) has no spanning two-cover, then
\[
\dim K(H)\le n-5,
\qquad K(H)=\Delta\mathcal P(H).
\]
The universal support-pair source has equivariant height \(n-4\). Thus minimum counterexamplehood leaves a codimension-one topological deficit. Algebraically, after lower Smith-chain equations have been constructed, only the final rank extension is genuinely tournament-specific.

This is the natural place to seek closure: not by descending further to a two-hole state, but by proving that the one-hole top-rank support-pair family cannot support the final equivariant obstruction.

No small-order cutoff is used.

## Frontier

- Development version when composed: None
- Development version now: 1
