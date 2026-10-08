# Antipodal-geodesic incidence forces at least 2^d/d missing facets per maximal-reachability label

# Antipodal-geodesic incidence gives a 2^d/d missing-facet bound

Let C⊆Q_d be a nonempty subset invariant under complement t↦\bar t. Assume NO connected component of the induced cube graph Q_d[C] contains an antipodal pair. Write Z=Q_d\C and z=|Z|. Such a C arises as every occupied maximal-reachability parallel-facet fiber in a hypothetical counterexample to the antipodally odd UNDIRECTED edge-geodesic conjecture, by the terminal-fiber theorem.

**Theorem (geodesic incidence separator inequality).**
\[
\boxed{|Z|\ge \frac{2^d}{d}} \qquad(d\ge2).
\]
Since Z is antipodally invariant, its cardinality is even and the bound may be rounded up to the next even integer. More precisely, for each t∈C,
\[
\sum_{z\in Z}\binom{d}{d_H(t,z)}^{-1}\ge1.
\]

**Proof.** Fix t∈C. Since \bar t∈C but lies in another component, EVERY antipodal geodesic from t to \bar t meets Z in an internal vertex. Choose the geodesic uniformly among its d! possible direction orders. A vertex z at Hamming distance k from t belongs to this random geodesic with probability
\[
\frac{k!(d-k)!}{d!}=\binom dk^{-1}.
\]
Apply the union bound to the event that the random geodesic meets Z. This proves the displayed inequality for t.

Sum the inequality over all t∈C:
\[
|C|\le\sum_{z\in Z}\sum_{t\in C}\binom{d}{d_H(t,z)}^{-1}.
\]
For fixed z∈Z, both z and \bar z belong to Z, by antipodal invariance. Thus every t∈C lies at Hamming rank 1,...,d-1 from z. For each rank k there are exactly \binom dk possible t, contributing total at most 1 after multiplication by \binom dk^{-1}. Hence
\[
\sum_{t\in C}\binom{d}{d_H(t,z)}^{-1}\le d-1.
\]
It follows that |C|≤(d-1)|Z|. Since |C|+|Z|=2^d, we obtain 2^d≤d|Z|, proving the bound. \(\square\)

**Application to NORI's edge proving ground.** Let m<n be the largest monochromatic-geodesic length, d=n-m≥2, and U any size-m support with a projected antipodal endpoint-pair label. If that label is realized in at least one U-parallel facet, then it is absent from at least 2^d/d of the 2^d parallel facets. This strengthens the previous edge-isoperimetric 2^d/(2d+1) bound, and it is proved directly by counting *actual antipodal geodesics* through absent labels. It says in particular that a no-closure coloring cannot have a maximal reachability label supported on all but o(2^d/d) exterior roots.

**Future closure link.** Combine this universal separator deficit with an independently proved lower bound on the number or distribution of maximal reachable pairs. In contrast with a pointwise Borsuk–Ulam zero, the incidence inequality is automatically root-mobile and does not require a balanced ridge itself to carry any monochromatic witness.
