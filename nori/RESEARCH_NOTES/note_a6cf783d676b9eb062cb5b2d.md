# Switch-filtered complementary-support gluing for boundary tournaments

- Stable ID: note_a6cf783d676b9eb062cb5b2d
- Author: unspecified; session provenance retained
- Primary home: section:nori_type_a_rook_gallery_topology
- Labels: boundary-tournaments, full-rank, switch-filtration, wu-yang
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7547_3
- Updated session: session_nori_r7547_3
- Disposition: none
- Successor: none

## Related references

- subsection:square_carrier_obstructions_and_switch_filtration
- subsection:boundary_overlap_cocycles_and_the_shared_antipodal_covering_class

## Research note

**Theorem (switch-budget gluing for boundary 3-tournaments).** Let \(b(a,h,c)\) be any reversal-odd coloring of ordered distinct triples on an \(n\)-element set \(V\). For an ordered pair \((h,c)\) of distinct vertices and \(r\ge0\), let \(\mathcal F_{h,c}^{[r]}\) be the family of sets \(S\subseteq V\setminus\{h,c\}\) for which there is a vertex-simple tight path using \(S\cup\{h,c\}\), ending with \((h,c)\), whose consecutive triple-color word has at most \(r\) switches. A length-two path has the empty color word and belongs to the family for every \(r\).

Then a Hamilton tight path with at most \(r+s+1\) switches exists if and only if there are \(h\ne c\) and \(S\subseteq V\setminus\{h,c\}\) with
\[
\boxed{S\in\mathcal F_{h,c}^{[r]},\qquad
(V\setminus\{h,c\})\setminus S\in\mathcal F_{c,h}^{[s]}.}
\]

*Proof.* Choose witnessing paths \(P=(p_1,\ldots,p_k,h,c)\), \(Q=(q_1,\ldots,q_\ell,c,h)\), with complementary outside-vertex sets. Reverse \(Q\), obtaining \((h,c,q_\ell,\ldots,q_1)\). Reversal oddness complements its triple-word bits while reversing their order, but preserves the number of switches. Concatenation along the shared pair \((h,c)\) is a Hamilton ordering because the two outside-vertex sets are disjoint and exhaustive. Its switch count is at most \(r+s+1\), including a possible change between the last triple of \(P\) and first triple of the reversed \(Q\).

Conversely suppose a Hamilton ordering has \(t\le r+s+1\) switches. If \(t=0\), split anywhere, permitting a length-two empty-word path at an endpoint. If \(t\ge1\), choose an integer \(j\) with
\[
\max(0,t-1-s)\le j\le\min(r,t-1)
\]
and split between the consecutive triple colors at the \((j+1)\)-st switch. The two portions share the two original vertices at that boundary and otherwise have disjoint vertex sets; the initial portion has \(j\) switches, and the terminal portion has \(t-j-1\le s\). Reverse the terminal portion to obtain a path ending at the reversed boundary ordered pair. This yields the required complementary support families. \(\square\)

**Unified interpretation.** The cube theorem in the preceding subsection expresses the same inequality through intersection of rooted geodesic-prefix complexes at antipodal roots. The boundary theorem expresses it through complementary used-vertex sets and reversed terminal pairs. Both carry the same additive switch budget \(r+s+1\) and enforce full matroid rank during concatenation. At \((r,s)=(0,0)\), both recover precisely the unrestricted one-switch existence problem. No arbitrary state-graph or restricted coloring hypotheses have been added.

**Proof obligation.** A topological chain argument for a common conjecture must force the complementary-support intersection specifically at budget \((0,0)\); unrestricted passage to the level-one carriers proves only weaker higher-switch conclusions.
