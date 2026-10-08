# Every binary ordered-three-face coloring has a one-switch antipodal Q5 geodesic, without oddness

# Unconditional one-switch dimension-five closure, and global maximal-rank floor

Let c be ANY binary ordered-three-face coloring of Q_n, n>=5, with the colors attached to physical ordered three-faces. No antipodal/reversal oddness is assumed.

**Theorem 1 (unconditional 5-edge one-switch geodesic).** Every 5-dimensional coordinate facet of Q_n contains a full 5-edge antipodal geodesic whose three ordered-three-face window colors change at most once. Consequently, in EVERY such coloring of Q_n, there exists a one-switch cube geodesic of length 5, and the global maximum length m of one-switch geodesics satisfies m>=5.

**Proof.** Fix any five-dimensional facet F, any reference vertex r of F, and its five free coordinate directions in an arbitrary cyclic order. By the universal odd-cyclic ordered-three-face seed theorem, F contains a monochromatic four-edge geodesic P, with color word (q,q) on its two ordered-three-face windows. Exactly one coordinate i of F is not used by P. Append i at P's terminal endpoint (or prepend it at the initial endpoint). The resulting direction word uses all five distinct coordinates, so it is a full antipodal geodesic of F. Its three window colors have form (q,q,t) (or (t,q,q)), and therefore change at most once, regardless of the value of t. QED.

**Theorem 2 (global root-slide sharpening).** If n>=6 and c has no full n-edge one-switch antipodal geodesic, let m<n be the largest length of any one-switch geodesic. Then m>=5, and every cyclic 2m-root-slide orbit consisting entirely of good length-m paths would force m=6. Thus for all m≠6 there is at least one bad path on EVERY orbit; for m>=7 the proved quantitative lower bound of max{2,ceil((2m-12)/3)} bad arcs per orbit applies.

**Proof.** The first claim is Theorem 1. The earlier cyclic period theorem allows a uniformly good maximal orbit only at m=4 or m=6. The rank floor m>=5 excludes m=4. The quantitative estimate was independently proved for m>=7. QED.

**Relation to active NORI.** For n=5 the ordered-three-face grand conclusion holds for ALL binary face-local colorings, a stronger claim than the active antipodal-reversal-odd hypothesis. In arbitrary n>=5, the theorem supplies a dimension-independent one-switch length-five seed inside every 5-facet. This does NOT prove a full n-edge one-switch path for n>=6.
