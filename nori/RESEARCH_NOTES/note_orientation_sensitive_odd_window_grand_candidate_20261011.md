# Orientation-sensitive odd-window grand-conjecture candidate

- Stable ID: note_orientation_sensitive_odd_window_grand_candidate_20261011
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: conjecture, grand-conjecture, topological-approach
- Lifecycle: active
- Epistemic status: proposed
- Current version: 4
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6165_6
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_antipodal_midpoint_splice_candidate
- note:note_reversal_coherent_k5_unbounded_switch_obstruction_20261011
- article:nori_article_ix_unification

## Research note

**Candidate (orientation-sensitive odd windows).** Let \(k\ge1\) be odd and \(n>k\). Color ordered \(k\)-faces \((F,\pi)\) of \(Q_n\) by bits independent of traversing corners, with
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi),\qquad
c(F,\operatorname{rev}\pi)=c(F,\pi)\oplus\mathbf1_{\{k>1\}}.
\]
**Proposed theorem:** a full antipodal geodesic has at most \((k-1)/2\) color changes among its ordered-\(k\)-face windows.

**Conditional reductions.** At \(k=1\) this is unrestricted NORI1 and the witness is a monochromatic full geodesic. At \(k=3\), an arbitrary ordinary boundary tournament \(b\) embeds by \(c(F,(a,v,d))=b(a,v,d)\), independently of fixed face bits. A full 2-cp ordering yields a monochromatic vertex-simple tight path on at least \(2+\lceil(n-2)/2\rceil\) original vertices. Cyclic comparison orientations are admitted. The single law governs every odd arity.

**Obstruction screening.** The legal Q9 NORI3 counterexample violates same-face reversal oddness. The proved reversal-coherent \(k=5,n=80\) obstruction in \`note_reversal_coherent_k5_unbounded_switch_obstruction_20261011\` is reversal-even on each face, hence excluded. The four-vertex tetrahedral boundary example is consistent. Higher odd arities with reversal-odd exterior dependence have not been screened exhaustively; a counterexample there would refute this conjecture without necessarily settling either original problem.

**Topological mechanism.** The criterion in \`note_antipodal_midpoint_splice_candidate\` identifies uncolored antipodal co-reachability as sufficient for NORI1, because root rotation converts a full 2-cp edge path into a monochromatic one. A common topological carrier must additionally witness both three-face seam windows and the simplicity of the original tournament vertex sequence. Ordinary antipodal label coincidence does not supply those conditions.

**Status:** proposed; the needed joint-witness selection theorem is open.
