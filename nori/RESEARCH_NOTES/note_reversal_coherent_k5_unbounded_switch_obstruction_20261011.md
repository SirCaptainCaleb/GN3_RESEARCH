# Unbounded switches in reversal-coherent higher odd faces

- Stable ID: note_reversal_coherent_k5_unbounded_switch_obstruction_20261011
- Author: Independent NORI researcher
- Primary home: article:nori_article_ix_unification
- Labels: proved, obstruction, conjecture
- Lifecycle: active
- Epistemic status: proved
- Current version: 6
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6165_3
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- note:note_reversal_coherent_odd_face_grand_conjecture_candidate
- subsection:unbounded_mandatory_color_changes_from_multilevel_local_minima
- article:nori_article_ix_unification

## Research note

# Unbounded switches under reversal coherence in arity \(k\equiv1\pmod4\)

**Theorem.** Fix \(k\ge5\) with \(k\equiv1\pmod4\), \(r\ge2\), and an even integer \(n\ge k+1\) satisfying \(n-1\ge r(2r+1)\). There is a coloring of ordered \(k\)-faces of \(Q_n\) satisfying
\[
c(F,\operatorname{rev}\pi)=c(F,\pi),\qquad c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)
\]
for which every antipodal geodesic has at least \(2r-2k+1\) color changes. In particular, the all-odd-arities reversal-coherent \((k-1)/2\)-switch proposal is false in arity \(k=5\): take \(r=6,n=80\), yielding at least three changes. For each fixed \(k\equiv1\pmod4\), the bound grows as \(\sqrt{2n}-O(k)\) over even \(n\).

**Proof.** Put \(m=n-1\). Partition \(m\) directions into \(r\) classes of size at least \(2r+1\), with class map \(\tau\), and designate the remaining direction \(s\). Set \(h(a,b,c)=\mathbf1_{\{b>\min(a,c)\}}\); then \(h(a,b,c)=h(c,b,a)\). The multilevel word lemma proved in Article I shows that for every ordering \(q_1,\ldots,q_m\) of the ordinary directions, the word \(H_j=h(\tau(q_j),\tau(q_{j+1}),\tau(q_{j+2}))\), \(1\le j\le m-2\), has at least \(2r-2\) changes. Its proof counts at most two occurrences of each class as centers in any run of ones, forces each class to occur in a zero-run, and observes that consecutive zero-centers have the same class.

Write \(k=2t+3\). For an ordered \(k\)-face \((F,(a_1,\ldots,a_k))\), where \(z_i(F)\) denotes its exterior bit in direction \(i\), define
\[
c(F,(a_1,\ldots,a_k))=
\begin{cases}
z_s(F)\oplus h(\tau(a_{t+1}),\tau(a_{t+2}),\tau(a_{t+3})),&s\notin\{a_1,\ldots,a_k\},\\
\bigoplus_{i\notin\{a_1,\ldots,a_k\}}z_i(F),&s\in\{a_1,\ldots,a_k\}.
\end{cases}
\]
Reversal preserves the middle triple's \(h\)-value and the exterior parity. Antipodal complementation flips \(z_s\) in the first case, and flips the exterior parity in the second because \(n-k\) is odd. These verify both identities.

Fix any root and full direction permutation \(p\), and let \(q\) be \(p\) with \(s\) removed. Of the associated \(H\)-word, the five-or-more-direction windows avoiding \(s\) retain two consecutive subwords, each with constant XOR offset determined by the starting \(s\)-bit. At most \(t\) entries are dropped at each end of \(H\), and at most \(k-1\) consecutive entries are omitted around the position of \(s\). Thus at most \(2t+k=2k-3\) changing adjacencies of \(H\) are lost; every other change survives. The windows containing \(s\) do not alter these retained adjacencies. Therefore
\[
\sigma(c(p))\ge\sigma(H)-(2k-3)\ge2r-2k+1.
\]
The bound is uniform in the root and permutation. \(\square\)

**Scope.** This refutes the graded conjecture proposed in \`note_reversal_coherent_odd_face_grand_conjecture_candidate\`, while preserving its unresolved NORI1 (\(k=1\)) and boundary-tournament (\(k=3\)) specializations. It uses the established reversal-even local-minimum lemma from the Article I Subsection \`unbounded_mandatory_color_changes_from_multilevel_local_minima\` and a new higher-face central-triple embedding with controlled erasure loss.
