# Withdrawn proposal: balanced antipodal reachability

- Stable ID: note_orientation_sensitive_balanced_antipodal_reachability_candidate_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: conjecture, grand-conjecture, topological-approach, unification, withdrawn
- Lifecycle: active
- Epistemic status: proposed
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6176_1
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_antipodal_midpoint_splice_candidate
- note:note_orientation_sensitive_odd_window_grand_candidate_20261011
- note:note_boundary_tournament_fixed_block_eight_seam_obstruction_20261011

## Research note

# Withdrawn as grand conjecture candidate (2026-10-11)

**Editorial assessment.** The proposed reversal condition distinguishes \(k=1\) from all larger odd arities solely to combine NORI1 and ordinary boundary tournaments. No independently motivated axiom produces that switch. The natural permutation-parity condition gives the desired behavior for \(k=1,3\), but the previously proved \(k=5\) obstruction rules out its full-arity conclusion. Thus the proposal below remains a mathematically open assertion with two valid conditional implications, but it is no longer endorsed as the next grand conjecture. A shared intrinsic structure is needed.

## Former candidate: balanced antipodal reachability

Let \(k\ge1\) be odd, \(n\ge2k\), and color the ordered \(k\)-faces \((F,\pi)\) of \(Q_n\) by bits satisfying
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi),\qquad
c(F,\operatorname{rev}\pi)=c(F,\pi)\oplus\mathbf1_{\{k>1\}}. \tag{1}
\]
For \(k=1\) the second identity is automatic. For \(k\ge3\), (1) implies \(c(\bar F,\pi)=c(F,\pi)\).

Let \(R_j(a)\) be endpoints of monochromatic length-\(j\) geodesics from \(a\), of either color, where monochromaticity concerns all consecutive ordered-\(k\)-face windows. Write \(m=\lfloor n/2\rfloor\).

**Former conjecture.**
\[
\exists a,v:\qquad v\in R_m(a),\quad\bar v\in R_{n-m}(a). \tag{2}
\]

**Proved geometric decoding lemma.** Let \(P:a\to v\) and \(T:a\to\bar v\) be monochromatic geodesics of respective lengths \(m,n-m\). Translate \(T\) antipodally, then reverse it, giving a monochromatic path \(v\to\bar a\). Both transformations change the color uniformly along a path, by (1). The direction supports of \(P,T\) are complementary, so concatenation yields a full antipodal geodesic with monochromatic internal windows on each of the two constituent direction blocks. The cross-seam windows are unrestricted.

**Conditional NORI1 implication.** For \(k=1\), (1) admits all antipodally odd edge colorings. The resulting full geodesic has at most one color change. The cyclic root/order move
\[
(a;\pi_1,\ldots,\pi_n)\mapsto(a^{\pi_1};\pi_2,\ldots,\pi_n,\pi_1)
\]
transforms the color word \((w_1,\ldots,w_n)\) to \((w_2,\ldots,w_n,1-w_1)\). Moving the initial constant run to the end converts an at-most-one-change word into a constant word; hence (2) implies unrestricted NORI1.

**Conditional boundary-tournament implication.** Any ordinary reversal-odd \(h(a,b,d)\) on distinct triples embeds at \(k=3\) by \(c(F,(a,b,d))=h(a,b,d)\), independently of the fixed coordinates of \(F\). This obeys (1). For \(n\ge6\), the two blocks from the decoding lemma give vertex-simple monochromatic tight paths of respective orders \(m,n-m\) on the original tournament vertices, one of order at least \(\lceil n/2\rceil\).

**Open problem.** The existence predicate (2) has no proved topological forcing theorem. A usable equivariant carrier must preserve a common root and compatible geodesic witnesses. Reconsider the color-system axioms before further proof attempts.
