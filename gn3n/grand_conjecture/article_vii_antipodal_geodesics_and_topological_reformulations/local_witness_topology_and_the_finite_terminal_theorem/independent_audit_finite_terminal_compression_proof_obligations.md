# Independent audit: finite-terminal compression proof obligations

## Composition

(none yet)

## Development

## Independent audit: finite-terminal compression needs explicit proofs

The finite endpoint theorems used at the end of this Section are sound: the eight-vertex and ten-vertex two-cover results follow from the audited four-of-six theorem by short counting arguments.

What is not presently independently auditable is the reduction from an arbitrary protected balanced witness carrier to the listed centered/overlapping supports of order at most ten.

Several load-bearing steps are asserted in the current composition and its sole development Subsection without a proof or a traceable proved dependency:

1. the “stronger finite argument” that five protected consecutive vertex positions cannot lie in one face block;
2. the ordered-tuple disjointness-graph implication
   \[
   |B|\le \alpha+\beta;
   \]
3. the subsequent boundary-antisymmetry deduction
   \[
   \alpha,\beta\le2;
   \]
4. the claim that the disjoint alternating \(0101/1010\) branch is impossible because the terminal indicators reduce to unary endpoint functions and “exactly one side occurs” forces them constant;
5. the dual-polarity elimination of every disjoint span-two terminal branch.

The local forbidden-word theorem itself checks out, as does the elementary statement that a length-at-least-four binary interval avoiding all six patterns
\[
001,011,0101,110,100,1010
\]
must be monochromatic. But those observations alone do not establish the terminal block compression above.

I did not find a separate canonical Toolkit/Section proof of these exact implications; the searchable project record currently points back to this same Section/Subsection. Therefore the finite terminal theorem should be treated as **not independently verified**, rather than as failed: the missing material may exist in prior research history, but it is not present in a form sufficient for audit.

Because [[terminalization_reachability_and_the_exact_frontier]] uses the finite terminal classification as a premise, a publication-quality closure requires these compression lemmas either to be proved explicitly here or to cite exact audited dependencies containing their proofs.
