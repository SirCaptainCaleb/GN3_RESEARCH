# Parity coloring makes both completions bad at every root-slide ridge of a fixed block

# Parity coloring defeats every bounded one-ridge local BU extraction at a root pair

Fix even \(n\ge6\), choose \(a\in Q_n\), and define the valid reversal-odd ordered-three-face coloring
\[
c_a(F,\pi)=\bigoplus_{j\in[n]\setminus \operatorname{free}(F)}(y_j\oplus a_j).
\]
This is the pre-existing exterior-disagreement parity construction.

**Theorem (both root-slide completions can be bad at every ridge).** Fix the antipodal root pair \(e=\{a,\bar a\}\). For EVERY \((n-1)\)-edge root-slide ridge \(R\) incident to the rooted block \(K_e\), both full antipodal-geodesic completions of \(R\) have at least two ordered-three-face color changes. Nevertheless, for EVERY odd labeling \(\ell:Q_n\to\mathbb R^{n-1}\), some such ridge has \(0\) in the convex hull of its vertex labels.

**Proof.** The two full completions of \(R\) have antipodal endpoint pairs \(e\) and \(e'=\{a\oplus e_j,\bar a\oplus e_j\}\) for a unique coordinate \(j\). Write a directed path's root-difference bits in its direction order as \(d_i=y_{p_i}\oplus a_{p_i}\). Its adjacent window-change indicators are
\[
\delta_i=1\oplus d_i\oplus d_{i+3},\qquad 1\le i\le n-3.
\]
For roots \(a\) or \(\bar a\), all \(d_i\) agree and every \(\delta_i=1\), so the number of changes is \(n-3\ge3\). For roots \(a\oplus e_j\) and \(\bar a\oplus e_j\), precisely one \(d_k\) disagrees with the others. At most two of the \(n-3\) comparisons contain \(k\). For \(n\ge8\) this leaves at least \(n-5\ge3\) switches; for \(n=6\), the three comparison pairs are \((1,4),(2,5),(3,6)\), disjoint, so exactly two switches remain. Every possible full completion is therefore bad. Finally, the root-slide ridge Borsuk–Ulam theorem supplies a balanced ridge incident to \(e\) for every odd \(\ell\). \(\square\)

**Consequence.** There is no universal extraction theorem of the form 'every zero-balanced root-slide ridge for an arbitrary odd vertex labeling has a one-change completion,' even if the labeling is chosen based on the coloring. There is also no *per-root* forcing rule requiring that a balanced ridge supply a good completion at either of its two neighboring root pairs: the parity coloring makes all such completions bad simultaneously. A successful topological NORI proof must instead use global propagation across multiple root slides, nonlocal reachability labels, a contradiction from a pattern of zeros, or an additional topological constraint not already forced at each root. This is a guardrail for the earlier balanced-ridge and odd-degree connector theorems.
