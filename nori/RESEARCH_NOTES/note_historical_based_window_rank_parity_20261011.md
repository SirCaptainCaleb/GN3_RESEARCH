# Historical based-window rank-parity obstruction and start-only classification

- Stable ID: note_historical_based_window_rank_parity_20261011
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: obstruction, historical_scope, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r5005_1
- Updated session: session_nori_r5005_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Historical model only: the directed based-window J-odd class permits different colors at different starting corners of the same ordered physical face. Rank parity is a valid counterexample to that superseded conjecture and ILLEGAL in the active physical ordered-face NORI class. The start-only parity classification is likewise limited to that broader model. Original Toolkit versions are retained as archived records. This note preserves the proofs verbatim.

## Original Toolkit source: nori_rank_parity_counterexample_even_dimensions

Let n be even and n≥6. For each directed length-three geodesic P=(x0,x1,x2,x3), set c(P)=|x0| mod 2. For the antipodal reversal J(P)=(bar x3,bar x2,bar x1,bar x0), the parity of |bar x3| is opposite to that of |x0|, so c(J(P))=1−c(P). Along any full antipodal geodesic, consecutive length-three windows begin at adjacent vertices; hence their colors strictly alternate, giving n−3≥3 changes. This rigorously refutes the historical unrestricted based-window statement. It does not refute active NORI: two length-three paths traversing the same ordered three-face from different corners can have distinct starting-vertex parities, violating the defining requirement that the color depend only on the face and ordered free directions.

## Original Toolkit source: nori_start_only_coloring_classification

Suppose n≥4 and c(X0,X1,X2,X3)=f(X0) for all directed length-three geodesics of Q_n. Under antipodal reversal the new initial vertex is bar X3=bar X0△D, where D is the set of the three flipped coordinates. Thus c(JP)=1−c(P) iff f(X△S)=1−f(X) for every X⊆V and every S⊆V of size n−3. If 1≤n−3≤n−1, comparison of two such S differing by one coordinate yields invariance under all double-coordinate flips, so f is constant on each Hamming-parity class. The required equation is possible iff n−3 is odd, that is, iff n is even. In that case f(X)=|X| mod 2 or its complement. Thus the rank-parity counterexample is essentially the only 'start-only' odd coloring in this range. Adapted from NOR Article I classification_of_start_only_antipodal_colorings, with the three-edge length used explicitly.
