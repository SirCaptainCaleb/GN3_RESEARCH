# Color-blind antipodal reachability criterion for NORI1

- Stable ID: note_antipodal_midpoint_splice_candidate
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: proved, reachability, topological-approach, grand-conjecture
- Lifecycle: active
- Epistemic status: proved
- Current version: 7
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6150_1
- Updated session: session_nori_r6202_2
- Disposition: none
- Successor: none

## Related references

- article:nori_article_ix_unification

## Research note

**Theorem (color-blind antipodal reachability criterion).** Let \(c\) be a binary coloring of the undirected edges of \(Q_n\), \(n\ge2\), satisfying \(c(\bar e)=1-c(e)\). Let \(R(a)\) be the endpoints of monochromatic geodesics rooted at \(a\), with either color admitted. The following are equivalent:
\[
\text{(i) \(c\) has a monochromatic full antipodal geodesic;}
\quad\text{(ii) }\exists a,\ R(a)\cap R(\bar a)\ne\varnothing;
\quad\text{(iii) }\exists a,\ R(a)\cap\overline{R(a)}\ne\varnothing.
\]
For every integer \(0\le r\le n\), condition (i) is equivalent to \(\exists a,\ R^r(a)\cap R^{n-r}(\bar a)\ne\varnothing\). In particular, for even \(n=2m\), balanced midpoint co-reachability \(R^m(a)\cap R^m(\bar a)\ne\varnothing\) for some \(a\) is both necessary and sufficient.

**Proof.** Given \(x\in R(a)\cap R(\bar a)\), choose monochromatic geodesics \(P:a\to x\) and \(Q:\bar a\to x\). Their coordinate supports are disjoint: the first consists of directions on which \(a\) and \(x\) differ, while the second consists of the complementary directions. Therefore \(P\) followed by the reverse of \(Q\) is a full antipodal geodesic whose edge-color word has at most one change. If its word is \(\alpha^r(1-\alpha)^{n-r}\), cyclically rotate its first \(r\) directions to the end, moving the root along those \(r\) initial edges. Each rotated edge becomes the antipodal copy of its old edge and changes color; all other edges remain unchanged. The resulting full geodesic is monochromatic of color \(1-\alpha\). The all-one-color case is immediate. Thus (ii) implies (i). Conversely, the endpoints of any monochromatic full antipodal geodesic supply (ii). Antipodal complementation maps monochromatic geodesics rooted at \(a\) bijectively to monochromatic geodesics rooted at \(\bar a\) with complementary colors. Hence \(R(\bar a)=\overline{R(a)}\), establishing (ii)\(\Leftrightarrow\)(iii). The midpoint assertion is a special case. \(\square\)

**Topological implication.** A topological principle forcing a root \(a\) for which \(R(a)\) contains an antipodal pair would *resolve unrestricted NORI1*, without color-specific reachability labels. The needed intersection must be witnessed by monochromatic geodesics in the original cube; symmetry of abstract carriers alone is insufficient. For ordered-three-face colorings, additional junction windows prevent the same argument from transferring automatically to boundary tournaments.

**Level refinement proof.** If a monochromatic full geodesic starts at \(a\), its vertex after \(r\) moves is reached from \(a\) by a monochromatic length-\(r\) prefix and from \(\bar a\) by reversing its monochromatic length-\((n-r)\) suffix. Conversely, the intersection supplies two monochromatic geodesics from antipodal endpoints of complementary lengths. Their supports are disjoint, so their concatenation is an antipodal 2-cp geodesic, which root rotation makes monochromatic. This holds for every \(0\le r\le n\).
