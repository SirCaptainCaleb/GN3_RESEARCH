# Candidate unified conjecture on reversal-coherent odd-face colorings

- Stable ID: note_reversal_coherent_odd_face_grand_conjecture_candidate
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: conjecture, unification, topological-approach
- Lifecycle: active
- Epistemic status: proposed
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r0_3
- Updated session: session_nori_r0_3
- Disposition: none
- Successor: none

## Related references

- article:nori_article_i_conjecture
- article:nori_article_vii_seven_coordinate
- article:nori_article_viii_edges
- note:note_tetrahedral_parity_boundary_no_spanning_tight_path
- note:note_joint_realizability_selection_for_nori1_and_boundary_tournaments

## Research note

# Candidate grand conjecture: reversal-coherent odd-face colorings

**Status:** proposed, unproved and not selected as a definitive grand conjecture pending counterexample tests, notably arity at least five and exterior-dependent arity three. The purpose is to put unrestricted NORI1 and all ordinary boundary 3-tournaments under one non-disjunctive symmetry law and one quantitative witness assertion.

## One intrinsic graded class

For odd \(k\ge1\), \(n>k\), let \(Q_n\) be the Boolean \(n\)-cube. A member of \(\mathcal C_{n,k}\) colors each \(k\)-dimensional coordinate face \(F\) together with an ordering \(\pi=(i_1,\ldots,i_k)\) of its free directions by \(c(F,\pi)\in\mathbb F_2\). The value depends on the face and ordered free directions, not the corner from which the face is traversed.

Require simultaneously
\[
\tag{A}c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi),
\]
\[
\tag{R}c(F,\operatorname{rev}\pi)=c(F,\pi)+\binom{k}{2}\pmod2.
\]
Here \(\bar F\) is the antipodal face (all fixed coordinates complemented), and all additions are over \(\mathbb F_2\). These are uniform intrinsic identities for *every odd arity*. Their combination is
\[
c(\bar F,\pi)=c(F,\pi)+1+\binom{k}{2}.
\]
Thus the antipodal degree changes with the parity of reversal in the symmetric group. One may include \(n=k\) where consistent (notably \(k=3\)); the restriction \(n>k\) avoids vacuous cases at certain arities.

For a full antipodal cube geodesic \(P\) of length \(n\), let \(w_k(P)\) be the binary word of the \(n-k+1\) consecutive ordered \(k\)-face windows along \(P\). Define the common quantitative witness predicate
\[
W_k(P):\quad P\text{ is }((k-1)/2)\text{-splice}.
\]

**Proposed single conjecture U (reversal-coherent geodesics).** For every odd \(k\ge1\), every \(n>k\), and every \(c\in\mathcal C_{n,k}\), there exists a full antipodal geodesic \(P\) satisfying \(W_k(P)\).

The uniform arity parameter is part of one graded notion of orientation-reversal coherence; the witness predicate and axioms have identical definitions across arities. The \(k\ge5\) range is an additional substantive conjectural assertion; it is not needed for the two principal deductions and must be independently tested before adopting U.

## precise specialization to NORI1

At \(k=1\), reversal of the one-element direction order is trivial, so (R) is automatic. Identity (A) is precisely the antipodal-odd law for a underlying undirected cube-edge coloring. Thus \(\mathcal C_{n,1}\) comprises **all** unrestricted legal NORI1 instances, including nonlinear ones. The uniform splice bound is \((1-1)/2=0\), so U yields a fully monochromatic antipodal geodesic, which is precisely unrestricted NORI1. The geodesic itself is the decoded witness.

## precise specialization to every ordinary boundary 3-tournament

Let \(b(a,v,c)\in\mathbb F_2\) on ordered triples of distinct vertices in \([n]\) be **any** ordinary boundary 3-tournament, satisfying only \(b(c,v,a)=1+b(a,v,c)\). In particular the local comparison tournaments may have directed cycles and no global edge order need exist.

For \(k=3\), define on every underlying 3-face \(F\) with free ordered directions \((a,v,c)\)
\[
C_b(F;(a,v,c)):=b(a,v,c),
\]
independently of all fixed exterior bits. The reversal parity is \(\binom32=3\equiv1\), hence (R) follows from boundary reversal. Antipodal invariance of \(C_b\) with order fixed together with (R) gives (A). Therefore \(C_b\in\mathcal C_{n,3}\) for \(n>3\).

If U holds, there is a permutation \(p_1,\ldots,p_n\) of the **original tournament vertices**, and a cube root, whose ordered-triple word
\[
b(p_1,p_2,p_3),\ldots,b(p_{n-2},p_{n-1},p_n)
\]
is 1-splice. A longest monochromatic block has at least \(\lceil(n-2)/2\rceil\) consecutive triples, corresponding to a **vertex-simple tight path on at least**
\[
\boxed{\,2+\lceil(n-2)/2\rceil\,}
\]
original vertices. If the block has color \(1\), reverse its order; the boundary reversal law turns all its triples into color \(0\). Thus U proves a **linear positive tight-path lower bound** for every ordinary boundary 3-tournament, including non-edge-orderable instances. For \(n=3\), any single ordered triple can be reversed to be positive, giving the trivial missing case.

This supplies precise instance encoding and decoding theorems for both full classes, conditional solely on the **same** U. A counterexample to U at \(k=1\) would refute NORI1; one at \(k=3\) in the direction-only subfamily would refute the proposed one-splice strengthening for boundary tournaments; a counterexample with exterior dependence or \(k\ge5\) would refute U without automatically refuting either original target.

## Known obstruction screening and limits of topology

The published \(Q_9\) NORI3 sentinel obstruction does not satisfy (R) for \(k=3\): on triples avoiding its sentinel, its reversal-even class rule conflicts with the required reversal-odd identity. Therefore it is excluded by an intrinsic symmetry property rather than by an arbitrary subclass label. The unconditional positive \(Q_5,Q_6\) theorems are consistent with U. The separate four-vertex tetrahedral parity boundary tournament has no positive spanning tight path, yet its two-window color word is 1-splice, so it also is consistent with U.

This is **not evidence that all** exterior-dependent \(k=3\) cases or higher arities satisfy U. No comprehensive counterexample search has been carried out for those ranges.

For \(k=1\), define \(R(a)\) as the set reachable from \(a\) by some monochromatic geodesic, of either color. An intersection \(R(a)\cap R(\bar a)\) yields a 1-splice antipodal geodesic: both geodesics concatenate at the common vertex because their Hamming distances sum to \(n\). No color-matching condition is necessary. This only yields a 1-splice witness; the unrestricted NORI1 target remains 0-splice. For \(k=3\), an analogous join must additionally verify both newly introduced ordered-three-face windows across the junction, with a common cube root and valid face evaluations. In the direction-only tournament specialization it must retain distinct original vertices. Standard Tucker/Sperner/Borsuk--Ulam label coincidence alone establishes none of these extra properties; a jointly witnessed high-index carrier or stronger discrete selection theorem would be needed.

**Research decision:** retain this as a candidate to falsify or sharpen. A complete proof of U has not been obtained. Its higher-arity demand may be stronger than necessary to unify the two target specializations. Do not promote to a manuscript or describe it as an established grand conjecture.
