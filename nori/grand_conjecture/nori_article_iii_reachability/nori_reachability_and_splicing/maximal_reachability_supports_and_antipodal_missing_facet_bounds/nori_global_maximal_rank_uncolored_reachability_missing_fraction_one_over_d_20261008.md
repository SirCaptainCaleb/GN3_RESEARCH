# Hypothetical edge-geodesic counterexamples miss at least 1/d of all maximum-rank reachability pairs

# Global missing-reachability density at the maximum monochromatic rank

Assume a hypothetical counterexample to the antipodally odd UNDIRECTED edge-colored hypercube monochromatic-geodesic conjecture. Let m be its global maximum monochromatic-geodesic length, let d=n-m>=2, and let
\[
\mathcal U_m=\{(x,S):x\in Q_n,\ |S|=m,\ x\oplus S\notin R(x)\}
\]
be the missing color-free reachable endpoint states at rank m.

**Theorem (at least a 1/d fraction of rank-m pairs are missing).**
\[
\boxed{|\mathcal U_m|\ge\frac1d\,2^n\binom nm.}
\]
Equivalently, at least \(1/d\) of all unordered Hamming-distance-m vertex pairs are NOT joined by any monochromatic geodesic. Consequently some root x has at least \(\binom nm/d\) missing rank-m supports.

**Proof.** Fix a set U of m coordinate directions. The remaining d coordinates index 2^d parallel U-facets. Within a U-facet there are 2^{m-1} unordered antipodal projected endpoint pairs \(\{r,r\oplus U\}\). For each fixed U and projected pair, the exterior occupancy C(U,r) consists of the facet assignments at which that pair is joined by a monochromatic U-spanning geodesic. Under the counterexample assumption, each C(U,r) is either empty or invariant under antipodality with no occupied component containing an antipodal exterior pair. The antipodal-geodesic incidence separator theorem gives at least \(2^d/d\) missing facet assignments in EITHER case (the empty case misses all 2^d).

Thus for each U and projected pair, at least a 1/d fraction of the exterior copies of that vertex pair are monochromatically unreachable. Summing over the \(\binom nm\) direction sets U and \(2^{m-1}\) projected antipodal pairs and 2^d exterior assignments shows that at least
\[
\frac1d \binom nm 2^{m-1}2^d=\frac1d\,2^{n-1}\binom nm
\]
unordered Hamming-distance-m pairs are missing. Each missing unordered pair gives two oriented root–support states (x,S), so |\mathcal U_m|≥2^n\binom nm/d. Averaging over the 2^n roots yields the final assertion. \(\square\)

**Geometric perspective.** The bound concerns ALL globally maximal-rank monochromatic-reachability pairs, not a fixed root or a selected subset of witnesses. It is independent of how many witness direction permutations yield each pair. In the especially interesting deficit d=2, at least half of all rank-(n-2) pairs must be unreachable in any counterexample. This is a concrete global combinatorial deficit. To close the edge conjecture by contradiction one needs a complementary lower bound on rank-m monochromatic reachability derived from the color-incidence constraints; no such matching lower bound is established here.
