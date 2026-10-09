# Every ordered-k-face 2-coloring has monochromatic (k+1)-edge seeds through every root via an odd cyclic window

# Universal odd-cycle monochromatic two-window seed for ordered k-face colorings

Let k>=1 and let Q_n have an ARBITRARY binary coloring of ordered physical k-dimensional coordinate faces: c(F,pi) in {0,1}, with no parity, reversal, or antipodality assumptions. Assume n contains an ODD number m>=k+1 of distinct directions. Thus we may take m=k+1 when k is even and m=k+2 when k is odd (provided n>=m).

**THEOREM (odd cyclic window seed).** For EVERY cube vertex r and EVERY cyclically ordered list p=(p_0,...,p_{m-1}) of m distinct coordinate directions, there exists i mod m such that the (k+1)-edge geodesic with root r⊕e_{p_i} and direction word
\[
(p_i,p_{i+1},\ldots,p_{i+k})
\]
(indices cyclically mod m) has MONOCHROMATIC ordered-k-face window word (exactly two windows). Its first edge arrives at r, and the remaining k coordinate changes depart from r. In particular, for k=3 and n>=5, every binary ordered-three-face coloring admits a monochromatic FOUR-edge geodesic, locally through ANY prescribed cube vertex r and ANY prescribed 5-set of coordinates.

**PROOF.** For each cyclic index i, put
\[
W_i=(p_i,p_{i+1},\ldots,p_{i+k-1}),
\quad
b_i=c(F(r;\operatorname{set} W_i),W_i).
\]
Here F(r;W) is the unique W-free physical k-face containing r. Because m is odd, the cyclic binary word b_0,...,b_{m-1} has two cyclically adjacent equal values: otherwise it would alternate around an odd cycle and return to the complement of its initial bit.

Choose i with b_i=b_{i+1}. Start at x=r⊕e_{p_i} and traverse the distinct directions (p_i,...,p_{i+k}); the condition m>=k+1 guarantees they are all distinct, so the resulting path is geodesic. Its FIRST k-edge window has ordered directions W_i and passes through r (after its first edge), hence its physical face is F(r;set W_i), with color b_i. Its SECOND k-edge window has ordered directions W_{i+1}, begins at r, and hence lies in F(r;set W_{i+1}), with color b_{i+1}. These are the only two windows; both colors agree. QED.

**Quantitative density.** Fix r and an m-set D of free coordinates. Every cyclic ordering of D produces at least one incident monochromatic two-window path whose first edge enters r. In the k=3,m=5 case, the five ordered triple colors through r form a cyclic 5-word, and at least one of the five adjacent pairs is equal. Consequently each 5-coordinate face through r contains a monochromatic 4-edge geodesic whose first edge reaches r. This gives a local seed at EVERY r and any prescribed 5-set, without NORI oddness.

**Application to terminal-tail color-FREE NORI reachability.** For k=3, choose i as above; the monochromatic four-edge path from x=r⊕e_{p_i} uses word (p_i,p_{i+1},p_{i+2},p_{i+3}). Thus the set U={p_i,p_{i+1}} belongs to the color-free terminal-two-tail reachability family R_(p_{i+2},p_{i+3})(x). It guarantees a supply of rank-2 reachable support labels. The outstanding grand-closure problem is to force complementary rank-(n-4) labels in the reversed-tail family at the SAME root, as required by the exact complementary-tail theorem.

**Scope.** The theorem proves a local monochromatic path SEED and DOES NOT give a full antipodal one-switch geodesic in arbitrary n. It is a dimension-independent five-coordinate gadget, not Q7 subclass analysis.
