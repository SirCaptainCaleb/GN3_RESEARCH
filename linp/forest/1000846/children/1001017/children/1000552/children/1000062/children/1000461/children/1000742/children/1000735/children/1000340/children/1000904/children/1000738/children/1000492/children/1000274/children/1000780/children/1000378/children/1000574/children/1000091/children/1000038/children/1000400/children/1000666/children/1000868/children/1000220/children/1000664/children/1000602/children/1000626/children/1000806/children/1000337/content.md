# Every aligned joint in a lens-free flat cycle lies in the late half

## Statement

In the entrance-rail lens-free flat gap-one terminal cycle of 315871ed0c8b, let k_i be the aligned joint level of R_i and R_{i+1}. Then for every i,
  k_i >= ceil((p-2)/2).

## Body

Apply the dichotomy b6043206d165 with L=p-2. Suppose the common-early-joint alternative holds. Then there is a vertex y such that every two distinct entrance rails meet exactly in {y}.

On the other hand, the distance-three intersection lemma 8777d2ccd614 gives, for every i,
  V(R_i) intersect V(R_{i+3})={t_{i+2}}.
Hence y=t_{i+2} for every i. Applying this for consecutive values of i gives t_{i+2}=t_{i+3}, impossible because these are the two distinct terminal vertices of the cycle edge e_{i+2}.

Therefore the common-early-joint alternative is impossible. The late-jointed alternative of b6043206d165 remains, giving k_i>=ceil((p-2)/2) for every i.
