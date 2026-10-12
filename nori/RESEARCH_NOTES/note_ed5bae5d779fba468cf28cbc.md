# Boundary tight-window incidence Smith forms and conjectured length torsion

- Stable ID: note_ed5bae5d779fba468cf28cbc
- Author: unspecified; session provenance retained
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: computation, smith-normal-form, lattice, conjecture
- Lifecycle: active
- Epistemic status: open
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6379_4
- Updated session: session_nori_r6379_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Integral incidence of boundary-tournament tight windows: finite Smith forms

**Status: finite computations and an all-order divisibility observation. The extrapolated lattice identity remains open.**

For \(n\ge4\), index columns by reversal orbits of ordered triples of distinct labels, \((a,b,c)\sim(c,b,a)\). There are \(N=n(n-1)(n-2)/2\) columns. For each permutation \(\pi=(v_1,\ldots,v_n)\), define its unsigned Hamiltonian tight-window incidence vector
\[
h_\pi=\sum_{j=1}^{n-2}e_{[(v_j,v_{j+1},v_{j+2})]}
\in\mathbb Z^N.
\]
Let \(A_n\) be the integral matrix with these \(n!\) rows.

**Universal divisibility:** Every row has coordinate sum \(n-2\). Thus the integral row lattice \(\Lambda_n^{BT}\) is contained in the sublattice
\[
L_n=\{z\in\mathbb Z^N:\sum_{t=1}^{N}z_t\equiv0\pmod{n-2}\}.
\]
In characteristic \(\ell\mid(n-2)\), the all-one column vector annihilates all incidence rows. This is a characteristic-specific obstruction absent from the cube's saturated geodesic-incidence lattice.

**Integer Smith computations:**
\[
\begin{array}{c|r|r|r|l}
n&N&n!&\operatorname{rank}_{\mathbb Q}A_n&\text{nonunit invariant factors}\\
4&12&24&9&\text{none}\\
5&30&120&30&3\\
6&60&720&60&4\\
7&105&5040&105&5
\end{array}
\]
The zero invariant factors in order four account for rational rank deficiency; all other omitted nonzero factors are units. Thus for \(n=5,6,7\), \(\mathbb Z^N/\Lambda_n^{BT}\) is cyclic of order \(n-2\).

**Order-eight modular check:** For \(n=8\), the matrix has 40,320 rows and 168 columns; modular elimination gives rank 168 in characteristic five, and rank 167 in characteristics two and three. This matches but does not prove the prediction of one Smith factor six.

**Conjecture (tight-window integral lattice).** For all \(n\ge5\),
\[
\boxed{\Lambda_n^{BT}=L_n.}
\]
Equivalently the Smith diagonal contains \(N-1\) units and one nonunit entry \(n-2\). This has not been proved for arbitrary \(n\). Verification uses all permutations, lexicographically canonicalized triple reversal orbits, and integer Smith normal form using SymPy, rather than approximate floating-point rank.

**Unification warning:** Cube geodesic unsigned turn incidence has a saturated integer lattice in every \(n\ge5\) by the Fourier theorem in Article XI Subsection 21. Boundary Hamiltonian tight-window incidence has nontrivial torsion in the displayed orders. Therefore integral lattice saturation is not a common hypothesis for *these two incidence models*. The tournament object here records triple resources, not the full signed two-port cocircuit representation, and these should not be equated. The underlying graph-cover and resource-gallery conjecture remains open.
