# NORI no-closure implies exact complementary-rank density bounds for color-free reversed-tail reachability

# Complementary-rank reachability density inequalities for active NORI

Assume the ACTIVE antipodal-reversal-odd ordered-three-face NORI coloring of Q_n, n>=4. Fix a root x and an ordered pair J=(a,b). Let D=[n]\{a,b}, d=|D|=n-2, and let \(\mathcal R_J(x)\) be the COLOR-FREE monochromatic terminal-two-direction reachability family defined in the exact complementary-tail equivalence theorem. For s=1,...,d-1 write
\[
\mathcal R_J^{(s)}(x)=\{U\in\mathcal R_J(x):|U|=s\}.
\]

**Theorem (sharp rankwise necessary inequalities).** If the grand NORI conjecture has NO good full antipodal geodesic, then for EVERY x,J,s,
\[
\boxed{|\mathcal R_J^{(s)}(x)|
+|\mathcal R_{\operatorname{rev}J}^{(d-s)}(x)|
\le\binom ds.}
\]
This statement contains NO color-indexed reachability sets and requires no numerical or small-dimension classification.

**Proof.** Taking complements inside D is a bijection from \(\binom D{d-s}\) to \(\binom Ds\). By the exact complementary-tail extraction theorem, a member U of \(\mathcal R_J^{(s)}(x)\) and its complement D\U in \(\mathcal R_{\operatorname{rev}J}^{(d-s)}(x)\) would give a good full antipodal geodesic. Thus under no closure these two families, after complementing the second, are disjoint subsets of the same \(\binom Ds\). The cardinality inequality follows. QED.

**Immediate consequences.**
1. Every singleton {i}⊆D belongs to BOTH \(\mathcal R_J(x)\) and \(\mathcal R_{\operatorname{rev}J}(x)\): the three-edge direction words (i,a,b) and (i,b,a) each have only one ordered-three-face window and therefore are automatically monochromatic. Hence under a hypothetical counterexample, the inequality at s=1 forces
\[
\mathcal R_J^{(d-1)}(x)=\varnothing
\quad\text{for all roots and ordered tails J}.
\]
Equivalently there is NO monochromatic (n-1)-edge geodesic, since appending its unique unused coordinate would create at most one new ordered-three-face window and yield grand closure.
2. If d=2r is even, s=r yields
\[
|\mathcal R_J^{(r)}(x)|+
|\mathcal R_{\operatorname{rev}J}^{(r)}(x)|
\le\binom{2r}r.
\]
In other words, between two opposite terminal-tail polarities at a fixed root, AT MOST HALF of the \(2\binom{2r}r\) possible middle-rank support labels can be monochromatically reachable in any counterexample.
3. Summing the displayed inequality over every cube root x and ordered pair J gives a global complementary-rank tradeoff
\[
A_s+A_{d-s}\le 2^n n(n-1)\binom ds,
\quad A_s=\sum_{x,J}|\mathcal R_J^{(s)}(x)|.
\]
For the middle rank in even d, this is \(A_{d/2}\le2^{n-1}n(n-1)\binom d{d/2}\).

**Topological/couting target.** Obtain a dimension-independent lower bound on one or more ranks of the true monochromatic terminal-memory reachability families that violates these exact complementary-rank inequalities. Unlike abstract equal-label coincidences, any violation extracts an actual full one-switch antipodal geodesic with no uncontrolled seam windows. The forcing lower bound remains open.
