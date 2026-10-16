# Paired square trades alter good roots and antipodal geodesic counts

- Stable ID: note_nori_balanced_paired_square_trades_root_and_count_variability_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:odd_girth_and_frustration_of_switch_component_quotients
- Labels: balanced-cube, alternating-trades, negative-certificate
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_3
- Updated session: session_nori_r9962_3
- Disposition: none
- Successor: none

## Related references

- subsection:odd_girth_and_frustration_of_switch_component_quotients

## Research note

Let \(n=2m\in\{4,6\}\), and index bits from zero. Set \(c_{2j}(x)=x_{2j+2\bmod n}\), \(c_{2j+1}(x)=1-x_{2j+2\bmod n}\). This is an antipodally odd vertex-balanced coloring. Let \(C\) be the square in directions \(0,1\) with all other bits zero; its four edge colors alternate. Let \(c'\) be obtained by reversing the colors of \(C\cup\bar C\). The two squares are disjoint; this is one legal balanced alternating-trail trade.

For \(n=4\), the roots of zero-colored full antipodal geodesics are, respectively,
\[
A_0(c)=\{1,3,4,6,9,11,12,14\},\qquad
A_0(c')=\{1,3,5,7,8,10,12,14\},
\]
where vertices are identified with binary integers. Each listed root has one such oriented geodesic. Thus a single paired square trade can delete the geodesic rooted at \(4\), and a root-preserving exchange lemma is false.

For \(n=6\), the corresponding counts of oriented zero full antipodal geodesics are \(144\) and \(168\). Hence even a paired alternating-square trade need not preserve \(\operatorname{tr}(PR^n)\).

Both statements admit a direct finite verification. For each root \(x\), let \(d_x(\varnothing)=1\); for each proper \(S\subseteq[n]\) and \(i\notin S\), update
\[
d_x(S\cup\{i\})\mathrel{+}=d_x(S)[c_i(x\oplus\mathbf1_S)=0].
\]
Then \(d_x([n])\) counts the corresponding full paths and \(\sum_xd_x([n])=\operatorname{tr}(PR^n)\). Applying the same recurrence to \(c'\) yields the displayed root sets and counts.

These examples disprove the root-fixed and trace-invariance strengthenings of paired-trail preservation. They leave open preservation of the *existence* of some zero full antipodal geodesic after each trade.
