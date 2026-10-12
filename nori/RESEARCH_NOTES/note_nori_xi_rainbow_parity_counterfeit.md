# Rainbow-cycle parity does not certify edge-color turn cochains

- Stable ID: note_nori_xi_rainbow_parity_counterfeit
- Author: session_nori_r6430_1
- Primary home: article:nori_article_xi_matroidal_turn_geometry
- Labels: proof, obstruction, rainbow-cycle, matroid
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6430_1
- Updated session: session_nori_r6430_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Rainbow-cycle parity alone does not certify turn cochains

Fix \(n\ge3\). Let \(H_n=L(Q_n)/\langle\tau\rangle\), and let \(a:E(H_n)\to\mathbb F_2\) be any admissible antipodally odd turn cochain. Every cyclic turn cycle \(C\) of a full antipodal geodesic has \(n\) turns and \(a(C)=1\). Every star triangle \(T\) has \(a(T)=0\).

**Universal parity obstruction.** Define \(q=1+(1+n\bmod2)a\), with all arithmetic in \(\mathbb F_2\). If \(n\) is odd, this means \(q=1\); if \(n\) is even, \(q=1+a\). Every geodesic turn cycle satisfies
\[
q(C)\equiv n+(1+n\bmod2)\cdot 1\equiv0\pmod2,
\]
whereas every star triangle satisfies \(q(T)=1\). Thus the \(\mathbb F_2\)-span of all geodesic cycles is a proper subspace of the cycle space \(Z_1(H_n;\mathbb F_2)\) in every dimension \(n\ge3\). In particular, prescribing parity on all geodesic cycles does not determine the covering-monodromy functional, even though every such cycle has nonzero monodromy.

**High-weight counterfeit cochains.** For each \(n\ge5\), there exists a binary labeling \(d\) of turns such that every cyclic antipodal-geodesic turn cycle has odd sum and integer weight at least \(n-1\), while \(d\) violates the star-triangle identity and hence is not induced by any antipodally odd edge coloring.

If \(n\) is odd, let \(d=1\). Every geodesic turn cycle then has weight \(n\), which is odd, and every star triangle has odd parity.

If \(n\) is even, fix a coordinate \(s\). Define an admissible cube-edge coloring by
\[
c_i(x)=x_s\quad(i\ne s),\qquad
c_s(x)=\sum_{j\ne s}x_j\pmod2,
\]
where \(c_i(x)\) is the color of the edge in direction \(i\) based at \(x\), and \(x_i\) is ignored when evaluating the respective edge color. Because \(n-1\) is odd, complementing every coordinate complements \(c_s\); it also complements each \(c_i\), \(i\ne s\). Thus this coloring is antipodally odd.

Let \(a\) be its turn cochain. All turns between two non-\(s\) directions have \(a=0\), since their incident edges share the same \(s\)-coordinate. Every rainbow geodesic cycle has two turns incident with its direction-\(s\) edge. Their \(a\)-values differ: their sum over \(\mathbb F_2\) is the covering monodromy 1, and all other turns have value 0. Consequently, the integer \(a\)-weight of every geodesic cycle is precisely 1. Set \(d=1+a\). Every geodesic cycle has integer \(d\)-weight \(n-1\), which is odd. On a star triangle the parity of \(d\) is \(1+a(T)=1\), so it violates the required vanishing. This works for every even \(n\ge6\).

The two constructions show why the rainbow-cycle parity constraints alone cannot support any uniform three-turn bound. The local star/square identities from Article XI are essential hypotheses in the full cochain formulation; a relaxation retaining only nontrivial-monodromy rainbow cycles admits spurious assignments of unbounded turn weight. This is a scoped obstruction to a parity-relaxed approach, rather than a counterexample to the unrestricted NORI1 or two-switch conjectures.
