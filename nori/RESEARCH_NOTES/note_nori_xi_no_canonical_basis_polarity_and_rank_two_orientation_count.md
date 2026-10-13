# Canonical basis polarity and rank-two orientation count obstructions

- Stable ID: note_nori_xi_no_canonical_basis_polarity_and_rank_two_orientation_count
- Author: Astra
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: exchange-flags, polarization, oriented-matroid, structural-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_1
- Updated session: session_nori_r7130_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let \(M_1=\bigoplus_{i=1}^nU_{1,2}\), \(M_2=U_{2,n}\), and \(n\ge5\).

**Theorem 1 (polarization is at different levels).** Complementation \(B\mapsto E(M_1)\setminus B\) is a free automorphism-natural involution of \(\Gamma(M_1)=Q_n\). Every \(S_n\)-equivariant map \(\binom{[n]}2\to\binom{[n]}2\) is the identity; thus \(\Gamma(M_2)=J(n,2)\) has no nonidentity relabeling-natural involution on bases. On the oriented-exchange flags of \(M_2\), however, \((\{a,b\},\{b,c\})\mapsto(\{b,c\},\{a,b\})\), or \((a,b,c)\mapsto(c,b,a)\), is a free canonical involution, and its odd bit assignments are the ordinary reversal-odd boundary colorings.

*Proof.* Complementation swaps one selected element in each two-element rank-one summand, preserves bases, and commutes with ground-set permutations. For \(M_2\), the stabilizer of \(B=\{1,2\}\) in \(S_n\) is \(S_{\{1,2\}}\times S_{\{3,\ldots,n\}}\). For \(n\ge5\) the only two-subset invariant under this stabilizer is \(B\), so every equivariant map fixes \(B\). Transitivity forces it to fix all bases. On oriented exchange flags, reversing the ordered pair of adjacent bases exchanges removed and inserted elements, preserving the common element, and is the stated reversal. \(\square\)

**Theorem 2 (rank-two orientation-count obstruction).** Ordinary rank-two oriented-matroid orientations on the labeled ground set of \(U_{2,n}\) cannot encode all reversal-odd boundary colorings injectively for \(n\ge5\). There are \(2^{n\binom{n-1}{2}}\) legal boundary colorings, but at most \((2n)!\) labeled orientations of \(U_{2,n}\).

*Proof.* At each of the \(n\) middle vertices, one freely specifies the bits on \(\binom{n-1}{2}\) reversal pairs. Every rank-two uniform oriented matroid is representable by nonparallel nonzero vectors in \(\mathbb R^2\). The circular ordering of their \(2n\) signed rays \(\pm v_i\) determines every pair determinant sign and hence the oriented matroid, giving the factorial upper bound. For \(n=5\), \(2^{30}>10!\). The coloring exponent increases by \(3n(n-1)/2\) as \(n\) increases, while the factorial multiplier is only \((2n+1)(2n+2)<2^{3n(n-1)/2}\) for every \(n\ge5\). \(\square\)

**Scope.** These are intrinsic obstructions to an undecorated ordinary-matroid or rank-two oriented-matroid identification. A class containing the unrestricted cube and boundary models must permit polarization on oriented exchange flags, with an independent comparison field and coherent resource-simple path language. Neither theorem implies a path selector.
