# Calderbank--Chung--Sturtevant monotone-path suppression

## Statement

There are edge orderings of K_n for which every increasing simple path has length at most (1/2+o(1))n. For n=2^k the construction is algebraic over F_2^k and converts simple increasing paths into increasing vector sequences with no zero consecutive block sum.

## Body

Source: A. R. Calderbank, F. R. K. Chung, D. G. Sturtevant, "Increasing sequences with nonzero block sums and increasing paths in edge-ordered graphs", Discrete Mathematics 50 (1984), 15--28.
Primary source: https://fanchung.ucsd.edu/mypaps/fanpap/63iswnbsaipieog.PDF

Definitions. Let alpha(n) be the minimum, over total orders of E(K_n), of the maximum number of edges in an increasing simple path. For n=2^k identify V(K_n) with F_2^k. Label xy by x+y and order labels lexicographically; ties are ordered arbitrarily. If v_0,...,v_t is a path and a_i=v_{i-1}+v_i, then
  a_r+...+a_s = v_{r-1}+v_s.
Hence a consecutive block sum is zero exactly when two path vertices repeat. Thus a simple increasing path gives a lexicographically increasing sequence with every consecutive block sum nonzero. Conversely such a sequence reconstructs a simple path after choosing v_0.

The paper introduces f(k), the maximum length of such a sequence, and a relaxed bipartite quantity g(k) in which only even-length consecutive block sums are required nonzero. The basic decomposition by the first coordinate gives
  f(k) <= f(k-1)+g(k-1),   g(k) <= 2g(k-1).

Projection lemma. Project an extremal increasing path in the recursively ordered bipartite graph G(k) to its first t coordinates. The resulting increasing pseudo-path gamma(t) records multiplicities with which projected edges are used. If, for fixed t,d, every full t-projection contains a vertex of degree at least d, then
  limsup_{k->infinity} 2^{-k} g(k) <= 2/d.
The counting reason is that a projected edge can represent at most g(k-t) original edges, whereas d projected edges incident with one projected vertex together can represent only 2*2^{k-t} original path edges because the original path is simple.

Finite local input. The appendix proves that every full 8-projection has a vertex of degree at least 4. This is a lengthy parity/case analysis of how projected edges split under one-coordinate refinement. With d=4 the projection lemma gives limsup 2^{-k}g(k)<=1/2, and hence f(k)<=(1/2+o(1))2^k.

General n. Section 4 recursively orders K_{n,n} and K_n by splitting each part approximately in half, ordering the first F_2-coordinate first and recursing on ties. The same 8-coordinate projection argument yields r(n)<=s(n)<=(1/2+o(1))n and therefore
  alpha(n) <= (1/2+o(1))n.

Proof-import decision. The algebraic reduction, recurrences, and projection lemma are recorded here because they are clean and reusable. The appendix establishing the finite t=8,d=4 local claim is intentionally not recopied; it is a long configuration analysis and is best consulted in the linked source, pp. 20--28.

LINP relevance. This is a template for a dense construction with a global path cap: assign algebraic labels to permitted transitions, make path simplicity equivalent to a nonvanishing interval-sum condition, then prove a finite projection must branch enough to force an asymptotic cap. A useful port would replace "increasing" by a canonical orientation/order on intersections of hyperedges or on states in a blow-up component.
