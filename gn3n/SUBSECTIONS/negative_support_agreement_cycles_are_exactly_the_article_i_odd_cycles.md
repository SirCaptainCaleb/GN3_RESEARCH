# Negative support-agreement cycles are exactly the Article I odd cycles

## Metadata

- ID: negative_support_agreement_cycles_are_exactly_the_article_i_odd_cycles
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 215
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A negative spanning support-agreement cycle is exactly the old odd support-cycle geometry

Let \(H\) be a minimum counterexample, choose one deletion cover \(F_x\) for every hole \(x\), and let \(G\) be the support-agreement graph of [[two_connected_support_agreement_closes_except_for_a_negatively_signed_spanning_cycle]].

Assume the exceptional case:
\[
G=x_0x_1\cdots x_{n-1}x_0
\]
is exactly one spanning cycle with negative sign product.

### Neighbor labels must be separated

Fix \(i\). Suppose the two cycle-neighbor labels
\[
x_{i-1},x_{i+1}
\]
lie in the same support of \(F_{x_i}\).

The agreement edge \(x_{i-1}x_i\) identifies the restricted support partition of \(F_{x_{i-1}}\) with that of \(F_{x_i}\), and the compatible insertion lemma puts the omitted labels \(x_{i-1},x_i\) into the same common support. Likewise the edge \(x_ix_{i+1}\) puts \(x_i,x_{i+1}\) into the same corresponding common support.

Since \(x_{i-1}\) and \(x_{i+1}\) lie on the same side in \(F_{x_i}\), these two identifications agree on the placement of \(x_i\). Hence \(F_{x_{i-1}}\) and \(F_{x_{i+1}}\) induce the same unordered support partition on
\[
V(H)-\{x_{i-1},x_{i+1}\}.
\]
Thus \(x_{i-1}x_{i+1}\) is an agreement edge, a chord of \(G\), contradicting that \(G\) is exactly the displayed cycle.

Therefore
\[
\boxed{x_{i-1}\text{ and }x_{i+1}\text{ lie in opposite supports of }F_{x_i}}
\]
for every \(i\).

### Alternation propagates

Fix \(i\) and name the two supports of \(F_{x_i}\) temporarily \(+\) and \(-\), with
\[
x_{i+1}\in +.
\]
Use the agreement edges successively to transport these names along the path
\[
x_i,x_{i+1},\ldots,x_{i-1}
\]
obtained by cutting the agreement cycle at \(x_i\).

Across the edge \(x_jx_{j+1}\), the compatible insertion lemma says that \(x_j\) in \(F_{x_{j+1}}\) lies in the same transported support class as \(x_{j+1}\) in \(F_{x_j}\). In \(F_{x_{j+1}}\), the preceding and following cycle labels \(x_j,x_{j+2}\) are opposite by the preceding paragraph. Transporting back across the agreement edge therefore shows that \(x_{j+1}\) and \(x_{j+2}\) occupy opposite classes in \(F_{x_i}\).

Inductively, the labels
\[
x_{i+1},x_{i+2},\ldots,x_{i-1}
\]
alternate between the two supports of \(F_{x_i}\).

The two ends \(x_{i+1},x_{i-1}\) are required to be opposite. Along the displayed path there are \(n-2\) adjacency steps, so this is possible only when
\[
n-2\text{ is odd},
\]
equivalently
\[
\boxed{n\text{ is odd}.}
\]

Write \(n=2k+1\). Then each support of every \(F_{x_i}\) has order \(k\), and, after choosing the cyclic indexing consistently,
\[
S_i=\{x_{i+1},x_{i+3},\ldots,x_{i+2k-1}\},
\]
\[
S_{i+1}=\{x_{i+2},x_{i+4},\ldots,x_{i+2k}\},
\]
with
\[
F_{x_i}=S_i\mid S_{i+1}.
\]

Thus the support vertices \(S_0,\ldots,S_{2k}\) and deletion edges
\[
S_iS_{i+1}\quad\text{labelled }x_i
\]
form exactly the spanning odd support cycle of Article I.

### Consequence

The negatively signed spanning cycle is therefore not a new support-agreement obstruction. It is canonically the old odd-cycle normal form already treated in [[deletion_covers_and_the_support_graph_the_odd_cycle_case]], which returns to the bounded-support / reversal-disturbance interface.

Hence support-agreement connectivity adds no additional global terminal geometry beyond the existing Article I dichotomy.

## Frontier

- Development version when composed: None
- Development version now: 1
