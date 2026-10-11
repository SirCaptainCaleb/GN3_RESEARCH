# Refuted reversal-coherent odd-face conjecture

- Stable ID: note_reversal_coherent_odd_face_grand_conjecture_candidate
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: conjecture, refuted, unification, obstruction
- Lifecycle: active
- Epistemic status: refuted
- Current version: 8
- Retention: current and at most one previous snapshot
- Created session: session_nori_r0_3
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_reversal_coherent_k5_unbounded_switch_obstruction_20261011
- note:note_antipodal_midpoint_splice_candidate
- article:nori_article_ix_unification

## Research note

**Status: refuted.** The all-odd-arities reversal-coherent conjecture below fails for \(k=5\), by the proved construction in \`note_reversal_coherent_k5_unbounded_switch_obstruction_20261011\`. Its arity-one and arity-three specializations remain open.

**Former proposal.** For every odd \(k\ge1\), \(n>k\), color ordered \(k\)-faces of \(Q_n\) by \(c(F,\pi)\in\mathbb F_2\), subject to
\[
c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi),\qquad
c(F,\operatorname{rev}\pi)=c(F,\pi)+\binom{k}{2}\pmod2.
\]
The proposed conclusion was a full antipodal geodesic with at most \((k-1)/2\) color changes among its consecutive ordered-face windows.

**Conditional specialization at \(k=1\).** Reversal is trivial and the first relation is the unrestricted NORI1 antipodal-odd edge law. The proposed bound is zero, hence gives a monochromatic antipodal geodesic. The equivalent, weaker-looking target of a single full 2-cp edge geodesic also implies NORI1 by cyclically rotating its initial monochromatic edge block; see \`note_antipodal_midpoint_splice_candidate\`.

**Conditional specialization at \(k=3\).** Every ordinary boundary 3-tournament \(b\), including cyclic non-edge-orderable ones, yields \(c(F,(a,v,d))=b(a,v,d)\), independent of fixed cube bits. The two axioms follow from \(b(d,v,a)=1-b(a,v,d)\). A full 2-cp ordered-triple geodesic has a monochromatic block of at least \(\lceil(n-2)/2\rceil\) triples, decoding to a vertex-simple monochromatic tight path on at least \(2+\lceil(n-2)/2\rceil\) original tournament vertices. Reversal makes its color positive if desired.

**Refutation.** For \(k=5\) and \(n=80\), an explicit coloring satisfies both defining identities while every full geodesic has at least three color changes. This contradicts the proposed allowance \((5-1)/2=2\). The construction uses reversal-even central-triple local minima and an antipodally odd exterior-parity rule when the sentinel direction is free. For fixed \(k\equiv1\pmod4\), the same mechanism forces unbounded changes as \(n\) grows.

**Scope.** Restricting \(k\) to 1 and 3 would leave a pair of unresolved specializations, not an intrinsic resolution of the common-structure problem. A replacement conjecture must preserve unrestricted NORI1 and all ordinary boundary tournaments, while supplying one substantive shared mechanism. Mere antipodal coincidence for ordered three-faces also needs the two junction windows to have compatible colors.
