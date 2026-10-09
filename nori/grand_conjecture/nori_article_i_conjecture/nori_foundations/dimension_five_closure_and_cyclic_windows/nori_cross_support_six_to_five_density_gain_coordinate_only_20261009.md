# Six-to-five transfer forces 73/180 five-path density and 143/180 full switch expectation for direction-only NORI

# Cross-support density gain from six-direction monochromatic facet transfer

**Scope.** Direction-only active NORI colorings: a Boolean function h on ordered triples of distinct elements of [n] satisfying h(c,b,a)=1+h(a,b,c) mod 2, used identically on every physical three-face of those directions. Assume n>=6. The claims below quantify genuine ordered-geodesic color words; physical roots are arbitrary because h is independent of all exterior bits.

**Theorem A (rich five-support from a monochromatic five-order).** Fix any five-set S. Its 120 linear direction orders partition into 24 directed cyclic orders with five rotations each. Write w_0,...,w_4 for the five cyclic triple-window colors of one directed cycle, let E count cyclic equal adjacent pairs, and let G count rotations whose three consecutive colors have <=1 switch.

By the odd cycle parity, E is odd and hence E>=1. If E=1, exactly two of the five rotations are good, hence G=2. If E=3, exactly two of the five cyclic comparison edges switch, and at most one adjacent pair of these switches can occur; therefore G>=4. If E=5, G=5. Thus every cyclic class supplies G>=2. If SOME five-letter order has a MONOCHROMATIC triple-window word, that cyclic class has two adjacent equality comparisons and hence E>=3. The reversed directed cyclic class is distinct (length five on five distinct letters) and has the same E, by reversal-oddness of h. These TWO cyclic classes each supply >=4 good rotations. The other 22 contribute >=2 each. Thus at least 52 of the 120 orders supported on S are good. Moreover the number of cyclic equal-adjacent comparisons among all 24 cyclic classes is at least 24+2+2=28, versus the baseline 24, giving >=28/120=7/30 equality density on random ordered four distinct directions within S.

For every S without the monochromatic five-order certificate, the universal pentagon inequality still gives at least 48/120=2/5 good five-orders, and at least 24/120=1/5 equal four-window comparisons.

**Theorem B (at least 1/6 of the five-supports are rich).** The team's proved theorem nori_six_direction_monochromatic_facet_transfer_20261008 says every reversal-odd coordinate-only coloring restricted to any six-set T has a monochromatic ordered-five-window geodesic on SOME five-subset S⊂T. Let M be the number of five-subsets possessing such a monochromatic five-order. Count pairs (S,T) with |S|=5, |T|=6 and S⊂T. Every T contributes at least one pair, each rich S belongs to exactly n-5 supersets T, and therefore
  M*(n-5)>=binom(n,6),
so M>=binom(n,5)/6.

**Theorem C (strict, dimension-independent improvements).** Select a uniformly random five-subset S and a uniformly random permutation of S. By Theorems A,B, the probability of <=1 ordered-three-face color switch is at least
 (48/120) +(1/6)*(4/120)= 73/180.
The random physical root x may be chosen independently: the assertion remains true at EVERY root.

Select instead four uniformly random distinct directions, which are equivalently the first four of a uniformly random ordered five-tuple, or four consecutive directions of a uniformly random full permutation. The equality indicator of the two consecutive actual three-face window colors has expectation at least
 (24/120)+(1/6)*(4/120)=37/180.
Indeed in a uniformly random ordered five-tuple, choosing the first four is the same distribution of cyclic four-letter windows as choosing a uniformly random cyclic rotation, and hence the 24x5 counting above applies exactly.

Consequently, for a uniformly random FULL antipodal n-geodesic rooted at ANY fixed x, each of its n-3 consecutive ordered-three-face color comparisons switches with probability at most 143/180. By linearity,
 E[#switches]<= (143/180)(n-3).
There exists an ACTUAL FULL antipodal n-geodesic from EACH fixed root x (coordinate-only assumption) with at most floor(143(n-3)/180) switches. This improves the general 4(n-3)/5 expectation and 2/5 rank-five density bounds by exactly the certified positive margins 1/180 in their respective normalized probabilities. It does not reduce the bound to one switch in arbitrary n.

**Sharpness and limitation.** Item nori_active_reversal_odd_five_pentagon_density_fully_sharp_20261009 constructs a five-support with exactly 48/120 good orders and just one equal cyclic edge in EVERY pentagon, simultaneously across all roots, so single-support/root-averaging improvements are impossible. The present improvement uses INCOMPATIBILITY of such saturated five-supports across every six-direction subsystem. The argument crucially invokes reversal oddness ON THE SAME physical ordered triple type across roots (direction-only h); in general active NORI, c(F,rev pi) is unconstrained at a fixed F, so the six-direction monochromatic five-subset theorem cannot be applied at one hub. Neither unrestricted NORI nor edge-geodesic closure is claimed.

**Near-term bridge question.** Replace the coordinate-only six-support monochromatic-transfer input by a genuinely physical cross-root theorem showing a positive fraction of five-supports with >24/120 cyclic good connector counts *after averaging over real cube hubs*. Even a tiny uniform gain would improve the universal unrestricted NORI 4/5 switch coefficient. To force one-switch closure, still require a coupled, root-compatible two-tail reachability overlap rather than a local density bound.
