# Pairwise-complete root triples force a seven-support or mixed four-support

## Metadata

- ID: pairwise_complete_root_triples_force_a_seven_support_or_mixed_four_support
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 97
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Finite seven-label lemma: a pairwise-complete root triple cannot stay quiet

Let \(C\) be a Hamiltonian four-set and let \(x,y,z\notin C\) be distinct. Assume

\[
C\cup\{r\}\text{ is Hamiltonian}\qquad(r\in\{x,y,z\}),
\]
and
\[
C\cup\{r,s\}\text{ is Hamiltonian}
\qquad(\{r,s\}\subset\{x,y,z\}).
\]

A direct binary MILP feasibility check on the seven labels gives the following dichotomy:

> Either \(C\cup\{x,y,z\}\) is Hamiltonian, or there exist distinct roots \(r,s\in\{x,y,z\}\) and distinct core labels \(c_i,c_j\in C\) such that
> \[
> \{r,s,c_i,c_j\}
> \]
> is Hamiltonian.

### Exact finite model

Use one binary variable for each boundary-reversal orbit
\[
h(u,m,v),\qquad h(v,m,u)=1-h(u,m,v),
\]
on seven labelled vertices. By relabelling the Hamiltonian core, fix one Hamilton order
\[
C=(0,1,2,3).
\]

Hamiltonicity of each required five- and six-set is encoded by a binary selector for every vertex permutation, with the selector implying tightness of every consecutive triple and with at least one selector active for each support.

To test the negation of the dichotomy, impose simultaneously:

1. every one-root support \(C+r\) is Hamiltonian;
2. every two-root support \(C+r+s\) is Hamiltonian;
3. the full seven-set is non-Hamiltonian, by requiring every one of its \(7!\) vertex orders to contain a non-tight consecutive triple;
4. every four-set consisting of two roots and two vertices of \(C\) is non-Hamiltonian.

This \(0\)-\(1\) feasibility system has 2625 binary variables before the final mixed-four constraints and 15200 linear constraints after them. HiGHS reports the system infeasible.

As a sanity check, removing condition 4 makes the system feasible: pairwise Hamiltonicity alone does **not** force the seven-set Hamiltonian. Thus the mixed Hamiltonian four-support is essential and is not an artifact of an already-impossible premise.

### Application to the quiet six-root residue

In [[quiet_six_root_states_grow_to_seven_supports_or_are_exactly_order_seventeen]], the only no-degree-three graph allowed by
\[
\alpha(\Gamma)\le2,\qquad |E|\ge6
\]
was
\[
\Gamma=K_3\sqcup K_3.
\]

Take either triangle \(\{x,y,z\}\). By definition of \(\Gamma\),

- \(C+x,C+y,C+z\) are Hamiltonian;
- \(C+x+y,C+x+z,C+y+z\) are Hamiltonian.

The seven-label lemma now says either:

- \(C+x+y+z\) is a Hamiltonian seven-support; or
- a mixed Hamiltonian four-support occurs.

The second output is one of the bounded Hamiltonian disturbances excluded in the quiet branch. Therefore the \(K_3\sqcup K_3\) case cannot remain quiet.

Consequently the quiet carrier residue has no order-seventeen two-triangle exception: it always grows to a Hamiltonian seven-support unless a bounded disturbance or maximal-support entry has already occurred.

This is a finite computational lemma. The MILP formulation is exact over the binary boundary-tournament variables; an analytic proof would still be desirable, but no heuristic or relaxation is used.

## Frontier

- Development version when composed: None
- Development version now: 1
