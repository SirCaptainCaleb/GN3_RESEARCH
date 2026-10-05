# longest_paths_and_reversal_structure_a_common_four_vertex_core_subsection_a

## Metadata

- ID: longest_paths_and_reversal_structure_a_common_four_vertex_core_subsection_a
- Parent Section: longest_paths_and_reversal_structure_a_common_four_vertex_core
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Put
\[
D=\{a_1,a_0,a_{\lambda-1},a_{\lambda-2}\}.
\]
Call \(y\in U\) good when \(D\cup\{y\}\) is Hamiltonian in the displayed order. If three vertices of \(U\) are not good, the tournament argument above produces the end-edge reversal of Lemma 4. Therefore:

**Lemma 5.** Unless the end-edge-reversal four-path occurs, all but at most two vertices of \(U\) are good.

When \(|U|\ge6\), at least four such labels exist.

**Lemma 6.** If \(|U|\ge6\) and the end-edge-reversal four-path does not occur, then either
1. \(H\) contains a Hamiltonian six-set with two-coverable complement; or
2. there is a four-set \(C\) and three distinct vertices \(r_1,r_2,r_3\notin C\) such that each \(C\cup\{r_i\}\) is Hamiltonian and has two-coverable complement.

**Proof.** By Lemma 5, at least \(|U|-2\ge4\) vertices of \(U\) are good. Choose three distinct such vertices \(r_1,r_2,r_3\), and set \(C=D\). For each \(i\), the order
\[
(a_1,a_0,r_i,a_{\lambda-1},a_{\lambda-2})
\]
is a Hamilton path on \(C\cup\{r_i\}\).

Put \(S_i=C\cup\{r_i\}\). The set \(V(H)-S_i\) is nonempty, since it contains \(U-\{r_i\}\), and is a proper subset of \(V(H)\). Minimality gives \(\operatorname{pc}(H-S_i)\le2\). If \(H-S_i\) were Hamiltonian, its Hamilton path together with the displayed path on \(S_i\) would give a two-cover of \(H\), a contradiction. Hence \(\operatorname{pc}(H-S_i)=2\) for each \(i\). Alternative (2) follows with the original core \(C=D\). \(\square\)

Choose Hamilton orders on the three five-sets. If two induce different orders on \(C\), there is an order disagreement. Otherwise each root is inserted into one gap of a common order on \(C\). Separated gaps give a Hamiltonian six-set; adjacent gaps give either a Hamiltonian six-set or a reverse tight triple through the intervening core vertex; a common internal gap gives a Hamiltonian four-set. If all three roots use one endpoint gap, boundary reversal among the roots gives a Hamiltonian four-set. Thus the common-core case always carries additional ordered information.
