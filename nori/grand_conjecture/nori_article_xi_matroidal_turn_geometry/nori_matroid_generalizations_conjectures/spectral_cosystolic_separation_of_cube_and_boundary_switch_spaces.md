# Spectral cosystolic separation of cube and boundary switch spaces

### Spectral lower bound for unrestricted boundary switches

The signed adjacency spectrum of the reversal quotient, established in the preceding spectral Subsection, gives a lower as well as an upper bound on switched turns. Let \(N=n(n-1)(n-2)/2\), \(E=N(n-3)\), and \(S_b\) be the switch support of any reversal-odd triple coloring.

**Theorem 1 (two-sided hereditary density).** For every \(n\ge6\),
\[
\boxed{\frac{n-4}{4(n-3)}\le \frac{|S_b|}{E}\le\frac{3n-8}{4(n-3)}.}
\]
The same inequalities apply on every \(m\)-symbol restriction for \(m\ge6\).

*Proof.* The self-adjoint signed adjacency matrix \(A\) obeys \(-(n-2)I\preceq A\preceq(n-2)I\), by the previously established annihilating polynomial. For a reversal-odd sign vector \(x\in\{\pm1\}^{N}\),
\[
\tfrac12x^\top Ax=E-2|S_b|,\qquad x^\top x=N.
\]
The two Rayleigh bounds give \(E/2-(n-2)N/4\le |S_b|\le E/2+(n-2)N/4\). Substitute \(E=(n-3)N\). Restriction retains reversal oddness. QED.

**Theorem 2 (cyclic-orientation construction).** For every \(n\ge5\), there is a reversal-odd boundary coloring with switched-turn fraction \(1/3\).

*Proof.* Fix a cyclic ordering of the symbols, and color an ordered triple by its clockwise orientation. Reversing the two outside entries complements its color. Two overlapping triples \(abc\) and \(bcd\) disagree precisely when the distinct exterior symbols \(a,d\) lie on opposite arcs of the circle from \(b\) to \(c\). Among the relative circular configurations of four distinct labeled points this occurs with probability \(1/3\). Uniformity of the directed overlapping turns therefore gives switched fraction \(1/3\). QED.

**Theorem 3 (sharp cube comparison).** The minimum switch fraction over all legal antipodally odd cube-edge colorings is \(1/n\), whereas the minimum boundary fraction belongs to \([\, (n-4)/(4(n-3)),\,1/3\,]\) for \(n\ge6\).

*Proof.* Every projective dimension-simple Petrie cycle has an odd, hence positive, number of switches. All such cycles have \(n\) turns and all quotient turns occur with equal multiplicity, so cube switch fraction is at least \(1/n\). To attain this, choose distinct directions \(a,b\) and set \(c_a(x)=x_b\), \(c_d(x)=x_a\) for every \(d\ne a\). This coloring is well-defined on undirected edges and is antipodally odd. At a projective cube vertex, the number of bichromatic turns is \(n-1\) when \(x_a\ne x_b\), and zero otherwise. Half of the projective vertices satisfy the inequality, so the switch support has size \((n-1)2^{n-2}\), while the entire quotient turn graph has \(n(n-1)2^{n-2}\) edges. Their ratio is \(1/n\). The boundary inequalities are Theorems 1-2. QED.

**Corollary (first-moment barrier).** A uniformly random Hamilton order of any reversal-odd boundary tournament has expected switch count at least \((n-4)/4\), since it contains \(n-3\) overlap transitions sampled uniformly across quotient turns. This applies even to globally support-minimizing odd colorings, and grows linearly with \(n\). Thus a proof of the one-switch conjecture must exploit favorable-path structure beyond the global first moment or cographic support minimization.

The contrast is intrinsic to the different covering incidence graphs: their common odd cohomology description does not imply comparable minimum representative densities.
