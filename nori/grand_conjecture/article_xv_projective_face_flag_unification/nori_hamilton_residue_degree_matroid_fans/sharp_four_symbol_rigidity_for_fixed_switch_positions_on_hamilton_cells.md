# Sharp four-symbol rigidity for fixed switch positions on Hamilton cells

### The four-symbol threshold for uniformly fixed switches

Let \(b(x,y,z)\in\mathbb F_2\) color ordered distinct triples, with \(b(z,y,x)=1-b(x,y,z)\). For a Hamilton order \(\pi\), the consecutive triple-color word has switches at the comparisons of successive triples. For a two-block cell \(D(A|B)\), all permutations within \(A\) and within \(B\) are present.

**Lemma 1 (no universal homogeneous comparison on five symbols).** If \(U\) has at least five elements, there is no reversal-odd triple coloring such that
\[
b(x,y,z)+b(y,z,w)=\varepsilon\pmod2
\]
for every ordered quadruple of distinct symbols from \(U\), for either fixed \(\varepsilon\in\{0,1\}\).

*Proof.* Fix distinct \(y,z\). For any distinct \(x,x'\notin\{y,z\}\), choose \(w\) distinct from all four; applying the identity with \(x\) and \(x'\), and the same \(y,z,w\), gives \(b(x,y,z)=b(x',y,z)\). Therefore \(b(x,y,z)=f(y,z)\) is independent of \(x\). Reversal oddness gives \(f(y,x)=1-f(y,z)\) for every distinct \(x,z\ne y\). Three distinct choices of \(x,z\) make these pairwise complement equations inconsistent. QED.

**Lemma 2 (mixed seam rigidity).** Let \(|A|\ge4\). It is impossible that, for every order of \(A|B\), the last all-\(A\) triple and the following \(AAB\) triple have opposite colors. Dually, if \(|B|\ge4\), the first \(ABB\) triple and following all-\(B\) triple cannot have opposite colors for every order.

*Proof.* The first alleged condition says \(b(x,y,z)=1-b(y,z,d)\) for every distinct \(x,y,z\in A\), \(d\in B\). Holding \(y,z,d\) fixed shows \(b(x,y,z)=f(y,z)\), independent of \(x\). Reversal oddness then gives \(f(y,x)=1-f(y,z)\) for all distinct \(x,z\ne y\). As \(|A|\ge4\), there are at least three such symbols, contradiction. The second statement follows by the symmetric final-block argument. QED.

**Theorem 3 (global fixed-switch cutoff).** Suppose every flag of \(D(A|B)\) has a first switch and the index of this first switch is the same for all flags. Then \(|A|\le4\). If every flag has a last switch at a common index, then \(|B|\le4\). In particular, for \(n\ge9\), no two-block cell of the type-A Hamilton Coxeter complex supports a reversal-odd coloring for which all flags have the same first and last switch positions.

*Proof.* Put \(a=|A|\ge5\). If the common first switch occurs among the successive all-\(A\) triple windows (indices \(j\le a-3\)), all ordered quadruples of \(A\) would give an opposite-color comparison, contrary to Lemma 1 with \(\varepsilon=1\). If it occurs between the last all-\(A\) and first \(AAB\) windows (\(j=a-2\)), Lemma 2 applies. If it occurs later (\(j\ge a-1\)), the first two all-\(A\) windows would have equal colors for every order, contrary to Lemma 1 with \(\varepsilon=0\). The last-switch argument reverses the roles of initial and final blocks: a common last switch within \(BBB\) windows contradicts Lemma 1, one on the \(ABB/BBB\) seam contradicts Lemma 2, and an earlier last switch forces equality throughout \(BBB\). At least one block has size at least five when \(n\ge9\). QED.

**Theorem 4 (sharpness; color-realizable degree-one cells in dimensions 6, 7, 8).** For every pair \(a,b\in\{3,4\}\) there exists an unrestricted reversal-odd triple coloring on \(A\sqcup B\), with \(|A|=a,|B|=b\), such that every Hamilton order in \(D(A|B)\) has first switch at position \(1\) and last switch at position \(n-3\). Consequently every one of its \(a!b!\) complete orders has at least two switches, and its extreme-switch bivectors induce a degree-\(\pm1\) map on the boundary of \(D\) after contraction against the centered block vector.

*Proof.* On a four-element block \(U\), define the color of the ordered triple \((x,y,z)\) to be the parity of the unique permutation \((x,y,z,w)\) of \(U\), where \(w\) is the omitted symbol and a reference orientation of \(U\) is fixed. This is reversal odd, and shifting the four-symbol order cyclically from \((x,y,z,w)\) to \((y,z,w,x)\) changes permutation parity. Hence the two consecutive triple colors in every four-symbol order are opposite.

For an initial three-element block \(A\), prescribe \(b(y,z,d)=1-b(x,y,z)\), where \(x\) is the third member of \(A\), \(y,z\) are its two final members, and \(d\in B\) is the first member of \(B\). This forces the first switch for every order; this assignment concerns only \(AAB\) triples. For an initial four-element block, the parity construction already forces the first switch between its first two \(AAA\) windows.

For a final three-element block \(B\), prescribe \(b(c,d,e)=1-b(d,e,f)\), where \(d,e\) are its first two members, \(f\) is its third, and \(c\in A\) is the preceding last member of \(A\). This forces the last switch and concerns only \(ABB\) triples. For a final four-element block, the parity construction forces the last switch between its final two \(BBB\) windows. The assigned triple types are disjoint and their reverses either match the required oddness within a single block or lie in unassigned types. Thus extend arbitrarily on remaining reversal pairs. The first and last switch prefix ranks are \(2\) and \(n-2\), strictly inside their respective blocks for \(a,b\in\{3,4\}\). Apply the product-degree theorem for centered permutahedral prefix maps to obtain degree \(\pm1\). QED.

**Scope.** This sharp cutoff is specific to *uniformly fixed first and last switch indices across an entire two-block cell*. It does not limit top-cell obstruction degrees for arbitrary colorings with variable switch ranks.
