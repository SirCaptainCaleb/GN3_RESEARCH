# An irrational two-moment perturbation forces Hamiltonian regular cut designs

## Composition

(none yet)

## Development

## An irrational two-moment perturbation forces a Hamiltonian regular cut design

There are now two antipodally even provenance moments in the physical root space W.

For a protected p-cut C and crossing root rho=e_a-e_c, define the side moment from root §47
\[
M(C,\rho)=\Pi_W(z_C\odot\rho),
\qquad
z_C=\mathbf 1_C-\frac pn\mathbf 1,
\]
and the full-cut moment from root §53
\[
Q(C,\rho)=q(C,\rho)z_C,
\qquad
q(C,\rho)=1-\frac{2p}{n}.
\]
In normalized ternary deletion states p<n/2, so q>0.

Fix any irrational number theta, for example sqrt(2), and put
\[
E_\theta(C,\rho)
=
M(C,\rho)+\theta Q(C,\rho).
\]
Both M and Q are antipodally even under (rho,C)->(-rho,C^c), so for a side sign s the perturbed label
\[
\Xi_\varepsilon(\rho,C,s)
=
\rho+\varepsilon s E_\theta(C,\rho)
\]
is antipodally odd and remains in W.

### Rational separation

For the discrete protected states considered here, M and Q have rational coordinates. Therefore if a rational linear combination of the E_theta labels vanishes, the M and Q parts vanish separately: coordinatewise an equality A+theta B=0 with A,B rational forces A=B=0.

In particular, on a simple physical root cycle every positive physical dependence has one common coefficient. Hence if the corresponding Xi_epsilon labels form a positive zero, then
\[
\sum_i s_iM(C_i,\rho_i)=0
\qquad\text{and}\qquad
\sum_i s_iQ(C_i,\rho_i)=0
\]
separately.

### Side-moment classification of a simple cycle

Write the simple cycle as
\[
\rho_i=e_{v_{i+1}}-e_{v_i},
\]
with k distinct cycle coordinates. Let
\[
S=\sum_i s_i,
\qquad t=p/n<1/2.
\]
For the side moment, every coordinate outside the root endpoints of one edge has value -1/n. At the cycle vertex v_i, summing the cycle moments gives
\[
s_i(1-t)+s_{i-1}t-\frac Sn=0.
\]

If k<n, choose a coordinate outside the entire cycle support. Its moment equation gives S=0. The vertex equation then becomes
\[
s_i(1-t)+s_{i-1}t=0.
\]
Since s_i,s_{i-1} are +/-1, this requires opposite signs and t=1/2, contradicting p<n/2. Therefore:

> No simple perturbed cycle can have proper coordinate support.

Now let k=n. If two consecutive side signs are equal, the left side of the vertex equation before the -S/n term is +/-1. This forces S=+/-n, hence all signs are equal. If no consecutive signs are equal, the signs alternate, so S=0, and the equation again forces t=1/2. Thus:

> Every surviving simple perturbed cycle uses all n coordinates and has one uniform barrier side.

This strengthens the A3-local exclusions to an arbitrary-length statement for a single physical cycle.

### Full-cut moment then forces regular incidence

For the surviving Hamiltonian cycle all side signs have a common value s. The Q equation, after dividing by the nonzero common scalar sq, is
\[
\sum_{i=1}^n z_{C_i}=0.
\]
Equivalently,
\[
\sum_{i=1}^n \mathbf 1_{C_i}=p\mathbf 1.
\]
Hence every physical coordinate belongs to exactly p of the n protected cuts.

Thus the cut-incidence matrix
\[
A_{ij}=\mathbf 1_{v_j\in C_i}
\]
has every row sum and every column sum equal to p. The root-crossing condition also imposes
\[
A_{i,i}=0,
\qquad
A_{i,i+1}=1
\]
cyclically, after orienting rho_i from v_i to v_{i+1}.

Therefore a single-cycle zero of the two-moment perturbation is not an arbitrary protected circulation. It is a Hamiltonian directed coordinate cycle, all terminal barriers occur on the same side, and the associated protected cuts form a p-regular bipartite incidence design containing the successor matching and avoiding the diagonal matching.

### Closure significance

Common-face A3 dependences already extract locally. The two-moment perturbation shows that any genuinely new single-cycle topological obstruction must be global in the strongest possible sense: full coordinate support plus a regular cut design.

The next useful reduction is to study this regular design together with the canonical Johnson-edge defect of root §52. If the design is the cyclic interval design, the desired Johnson exchanges compose directly. More generally the p-regular incidence graph decomposes into perfect matchings, one of which is the forced successor matching. A closure argument should exploit the remaining p-1 regular factor to find either a zero cut-defect edge, a shorter defect circulation, or a threshold-band improvement.

This theorem concerns a single simple physical cycle. A support-minimal zero whose physical circulation decomposes into two oppositely imbalanced cycles can still couple their moment equations and remains a separate case.
