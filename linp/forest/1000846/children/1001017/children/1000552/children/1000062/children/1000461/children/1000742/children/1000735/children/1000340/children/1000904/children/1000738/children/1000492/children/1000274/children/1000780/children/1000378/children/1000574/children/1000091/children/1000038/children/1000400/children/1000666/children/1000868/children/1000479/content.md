# Terminal blockers on a flat-cycle entrance rail are pushed early by their cycle distance

## Statement

Let C=(e_0,...,e_{c-1}) be a flat rank-(p-1) terminal cycle with private entrances x_i, and let R_i=(r_1,...,r_{p-2}) be a maximum entrance rail ending at x_i. Assume R_i has no entrance-label contact with the relevant short cycle arc. Suppose a terminal vertex y of e_{i+d}, d in {1,2}, lies on R_i and the short forward arc e_{i+d},e_{i+d-1},...,e_i meets R_i only at y and x_i. If a is the first rail-edge index containing y, then a<=p-d-3. The symmetric backward statement holds for d in {1,2}. Thus an adjacent terminal blocker has first occurrence at most p-4, while a distance-two terminal blocker has first occurrence at most p-5.

## Body

Take the prefix r_1,...,r_a ending at y. By the clean-short-arc hypothesis, append the cycle edges e_{i+d},e_{i+d-1},...,e_i in that order. Consecutive cycle edges meet in their terminal joints, the first appended edge meets the rail prefix only at y, and e_i meets the omitted rail suffix only at x_i, which is now available as the last vertex. Hence this is a linear path ending at x_i of length a+(d+1). Since phi(x_i)=p-2, maximality gives a+d+1<=p-2, i.e. a<=p-d-3. Reversing the cycle orientation proves the backward version.
