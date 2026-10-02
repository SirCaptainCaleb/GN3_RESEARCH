# Equitable three-covers admit no strict quadratic descent while three components remain

## Statement

Let C be an equitable spanning three-cover of an n-vertex boundary tournament. Along any sequence of spanning three-covers C=C_0,C_1,... for which Phi(C_{i+1})<=Phi(C_i), every C_i has the same minimum Phi value and an equitable component-order profile. In particular no strict Phi-decreasing move or multi-move sequence between spanning three-covers can start from C. Therefore a Phi-nonincreasing proof beginning at an equitable three-cover can close only by reducing the number of components, or by navigating the equal-Phi plateau with an independent order/support-sensitive well-founded mechanism until such a reduction occurs.

## Body

By 1000268, every equitable three-cover has the absolute minimum possible value of Phi among all positive three-part size profiles summing to n, and equality occurs only for equitable profiles. Let C_0=C be equitable and suppose Phi(C_{i+1})<=Phi(C_i) while each C_i is still a three-cover. Since Phi(C_0) is the absolute minimum, Phi(C_i)>=Phi(C_0) for every i. Inductively the nonincrease gives Phi(C_i)<=Phi(C_0), hence equality throughout. Equality in the fixed-sum sum-of-squares minimum forces every C_i to be equitable.

Thus strict quadratic descent is numerically impossible once an equitable profile has been reached. Any theorem that reports a strict Phi descent from an auxiliary nonequitable cover reached after leaving the plateau cannot by itself contradict the original equitable minimum: the descended state may merely return to the absolute minimum. A terminal proof in the equitable regime must therefore either merge two components directly or employ a secondary invariant depending on support/order/provenance rather than only on the component-size triple.