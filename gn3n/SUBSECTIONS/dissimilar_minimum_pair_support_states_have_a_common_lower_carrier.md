# Dissimilar minimum-pair support states have a common lower carrier

## Metadata

- ID: dissimilar_minimum_pair_support_states_have_a_common_lower_carrier
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 239
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Dissimilar minimum-pair support states have an order-free common lower bound

Let kappa_2(H)=2. Fix x,y,z with xy and xz edges of the minimum-pair graph, and choose arbitrary two-covers
H-{x,y}=A|B and H-{x,z}=C|D.
Work on W=V(H)-{x,y,z}.

Form the 2x2 intersection matrix of A∩W,B∩W against C∩W,D∩W. If all four displayed components A,B,C,D have order at least 4, every row and column sum is at least 3.

Elementary 2x2 lemma: if every row and column sum of a nonnegative integer 2x2 matrix is at least 3, then either both main-diagonal entries are at least 2 or both off-diagonal entries are at least 2. Otherwise one can choose an entry at most 1 from each diagonal pair; the two chosen small entries share a row or column, forcing that row or column sum at most 2.

Hence, after possibly swapping C,D, there are disjoint two-sets
U subset (A∩C∩W), V subset (B∩D∩W).
Every two-set is Hamiltonian vacuously, so (U,V) is a support-pair vertex satisfying
(U,V)<=(A,B) and (U,V)<=(C,D).

Therefore arbitrary neighboring minimum-pair support states have a common lower bound in the Hamiltonian support-pair poset whenever all four components have order at least 4. Their Hamilton orders may be completely unrelated.

Topologically, the two top-rank vertices are joined by the length-two path
(A,B) > (U,V) < (C,D)
after the harmless side swap. Thus dissimilar deletion-cover orders are not even a connectivity obstruction in the support-pair complex.

Generalization: if every row and column sum is at least 2t-1, one alignment has both diagonal cells of size at least t. Taking t=3, if all four original components have order at least 6, neighboring top-rank states have a common lower bound (U,V) with |U|=|V|=3; every three-set is Hamiltonian.

This moves the dissimilar-cover frontier upward: pairwise connectivity is automatic in the large-component regime. The remaining obstruction for the Smith approach is higher-dimensional cycle filling, not order agreement.
