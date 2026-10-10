# Article VII — Seven-coordinate structural and tournament methods

All-dimensional boundary-tournament altitude transfer: any direction-only boundary 3-tournament with an acyclic line-graph comparison orientation has a monochromatic cube geodesic using n/2^{O(sqrt(log n loglog n))} distinct coordinates, via a global edge order and the Bucić et al. 2020 nearly-linear increasing-path theorem. The transfer exactly preserves original-vertex simplicity and physical face colors. Directed comparison cycles are therefore necessary for shorter-path obstructions in this subclass. See the new Section Subsection; exterior dependence remains unresolved.

# Seven-direction endpoint factorization

Let c color physical ordered three-faces of Q_n. For a direction-distinct path (p_1,...,p_k) rooted at x, let w_j be the color of the actual ordered three-face traversed by (p_j,p_(j+1),p_(j+2)). Exterior-coordinate bits determine the root dependence of these colors.

## Shared-pivot formula

For seven distinct directions (a,b,c,d,e,f,g), fix the initial root bits other than x_d=t. The five window colors have the form

(A(t),M_1,M_2,M_3,E(t)).

Indeed the three interior free triples (b,c,d),(c,d,e),(d,e,f) contain d, so their physical faces and colors do not depend on t. The first triple (a,b,c) and last triple (e,f,g) omit d and may depend on t. Thus a single pivot controls the two endpoint windows while the interior color word remains fixed.

For six moves (a,b,c,d,e,f), choosing the two middle root bits x_d and x_c gives the independent endpoint formula (A(u),B,C,D(v)). Both central windows contain c and d as free directions, hence B,C are fixed. If B≠C and both endpoint maps are nonconstant, select A=B and D=C, obtaining one change. If B=C then matching either endpoint to that common middle color also suffices.

## A seven-direction conditional criterion

Let the three fixed middle bits be (M_1,M_2,M_3), and let A,E be the endpoint maps. Every possible resulting word is (A(t),M_1,M_2,M_3,E(t)). If the middle triple has two changes, both endpoint choices leave at least two changes. If the middle triple has exactly one change, a good word occurs precisely when the chosen first endpoint equals M_1 and the chosen last endpoint equals M_3, because any extra change would raise the total to two. If the middle triple is constant q, a good word occurs precisely when at least one of the two endpoint values is q. These alternatives follow by directly counting the four boundaries between consecutive colors. They give an exact one-bit rooted solvability test in any ambient dimension, provided the other exterior bits are held fixed.

## Wing factorization and closure classes

The endpoint maps are functions of the same pivot, so their attainable value pairs are correlated. The seven-coordinate wing-factorization results exploit this correlation together with changes of direction order, complemented faces and alternative pivots. Under the established crossed-sensitivity and flat-bridge hypotheses, a good antipodal seven-geodesic is forced. These structural criteria expose what a general proof would need: a coordinated pivot change or interchangeable wing that removes an endpoint obstruction while preserving the genuine middle ordered-face colors.

This article gives exact endpoint-root formulas and provable closure tests, with seven-coordinate special families providing further forced configurations. The general-dimension conjecture remains a separate global compatibility question.

**New polynomial structural lower bound.** When a boundary-compatible physical ordered-three-face coloring has at most d influential exterior coordinates *per unordered triple* (with arbitrary triple-specific supports), a 4-uniform dependency-hypergraph extraction yields a flat direction subset of size Omega((n/d)^(1/3)). The Devine-Milans snake lower bound on the induced genuine boundary tournament produces an Omega((n/d)^(1/6))-edge monochromatic geodesic. For one common support set of size t, the stronger sqrt(n-t) bound holds directly. The proof requires same-face reversal oddness and correct physical-root consistency; it does not require a common comparison order or a global exterior support. See Article VII's new sparse triplewise exterior-dependence Subsection.


**Improved robust-snake theorem (current strongest per-triple exterior support bound).** The boundary-compatible sparse exterior-dependence result of the preceding paragraph has been sharpened from \(\Omega((n/d)^{1/6})\) to \(\Omega((n/d)^{1/4})\) without changing its hypotheses. A quantitative partial-boundary-tournament lemma shows that if \(B\) unordered triples are unavailable on \(N\) vertices, then its longest positive vertex-simple tight path of order \(L\) satisfies \((N-1)/4\le(L-1)^2+(L-1)\sqrt{24B/N}\). Choosing a random \(p=1/\sqrt{dn}\) fraction of original directions retains \(\Omega(\sqrt{n/d})\) directions while making only \(O(N^2)\) triples unusable due to exterior dependencies, so the snake lemma forces \(\Omega(\sqrt N)=\Omega((n/d)^{1/4})\) directions in a genuine monochromatic cube geodesic. This is the best proved rate in that manuscript; the original \(1/6\) estimate is valid but superseded. The fully unrestricted boundary-compatible case remains open.

**New quantitative frontier: exponent \(1/3\) under sparse triple-specific exterior support.** The strongest current transfer for physical boundary-compatible NORI3 with at most \(d\) exterior dependencies PER unordered triple is \(\Omega((n/d)^{1/3})\) monochromatic geodesic length, not the superseded exponents \(1/6\) and \(1/4\). The key new robust snake lemma retains a dense subgraph of terminal pairs having \(O(\sqrt N)\) missing triple extensions, and forces \(\Omega(\sqrt N)\) positive vertex-simple tight paths even though roughly \(N^{5/2}\) unordered triples may be unavailable. Sampling \(N\asymp(n/d)^{2/3}\) directions eliminates all dependencies on those coordinates for the remaining available triples. The resulting path is realized on physical cube faces from a common fixed root. Stronger \(\Omega(\sqrt{n-t})\) bounds hold for one common exterior support of size \(t\). The unrestricted boundary-compatible case still lacks a universal polynomial guarantee.
