# NORI snake fan: exact Johnson hypersimplex of two-step merging roots and independent merge-bit obstruction

# Universal maximal-path snake fan: Johnson root hypersimplex and independent physical first-window obstruction

Active NORI physical 3-face binary coloring c satisfying c(bar F,rev pi)=1−c(F,pi), n>=5. Source for snake motivation: user-provided Devine–Milans linear-path manuscript; no web or outside literature. The previous exact snake fan theorem is nori_snake_digraph_maximal_path_dual_terminal_fan_and_two_step_cap_20261009. The new theorem works at ARBITRARY MONOCHROMATIC PATH LENGTH k, not only near spanning.

Let P be a q-monochromatic genuine k-edge geodesic x→y of direction word (u_1,...,u_(k−2),a,b), k>=3, direction support S, unused set T=[n]\S of cardinal m=n−k >=2. Suppose P is unextendable at its end as a monochromatic q path (e.g. it is a globally longest mono q geodesic). Then for every d∈T its attempted extension window (a,b,d) at F_y({a,b,d}) has color 1−q, and by antipodal reversal the real path B_d of directions (d,b,a) ending at bar y has all one three-face-window color q. Each B_d begins at
 r_d = bar y xor {a,b,d} = x xor (T\{d}) xor {a,b}.
These m roots form a Hamming radius-one star centered at h=bar y xor {a,b}, with pairwise Hamming distance two.

**THEOREM (JOHNSON ROOT LAYER FOR PAIRWISE FAN MERGES).** For each unordered pair {d,e}⊂T define
 s_{d,e} = h xor {d,e} = x xor {a,b} xor (T\{d,e}).
There are exactly TWO genuine four-edge geodesics from s_{d,e} to bar y with last two directions (b,a):
 Q_de=(d,e,b,a), Q_ed=(e,d,b,a).
Their SECOND ordered-three-face windows are the corresponding q-colored B_e and B_d fan windows respectively. Their FIRST windows are orientations (d,e,b),(e,d,b) of the SAME actual physical face F_h({b,d,e}). Hence Q_de is q-monochromatic iff c(F_h({b,d,e});(d,e,b))=q, and Q_ed is q-monochromatic iff c(F_h({b,d,e});(e,d,b))=q.

The root set {s_{d,e}:{d,e∈T} has binomial(m,2) distinct vertices. Hamming distance between s_{d,e} and s_{d',e'} equals |{d,e}△{d',e'}|∈{0,2,4}; therefore adjacency under Hamming distance TWO is the JOHNSON GRAPH J(m,2), the vertex-edge graph of the second hypersimplex Δ(m,2). This gives an honest root-coupled combinatorial carrier for two-step snake merging, entirely based on literal cube vertices and certified 4-edge paths (no invented lift).

**SHARP INDEPENDENCE/NEGATIVE RESULT.** For a single fixed q-monochromatic terminal-unextendable path P, the 2*binomial(m,2) first-window color bits
 c(F_h({b,d,e});(d,e,b)), c(F_h({b,d,e});(e,d,b))
may be arbitrarily specified independently, while simultaneously preserving (i) all windows of P color q, (ii) all blocked extension windows (a,b,d) color 1−q, and (iii) global active antipodal-reversal oddness. Proof: choose the required physical ordered faces on P, its extension caps, and the indicated face F_h({b,d,e}) for every distinct unordered {d,e}; their three-free-coordinate sets are respectively contained in S, {a,b,d}, and {b,d,e}. These types are disjoint, except that two opposite candidate orientations share F_h({b,d,e}) but are not reversed orderings of one another ((d,e,b) reverses to (b,e,d), NOT to (e,d,b)). The antipodal partner of any prescribed colored ordered face has complement color, and for n>3 the antipodal physical face is distinct. Therefore each independent prescribed bit extends to a globally valid NORI coloring by selecting one representative per remaining reversal orbit. Taking ALL these first-window bits equal 1−q produces a valid coloring with P q-monochromatic and END-UNEXTENDABLE in color q but NO q-monochromatic four-edge merge anywhere in the entire associated Johnson root layer. No global-maximality claim is made for P in that constructed coloring: only terminal unextendability. Thus the geometry supplies no unconditional snake-edge density.

**SPECIAL CASE m=2.** The Johnson layer has a single vertex s=x xor {a,b}, exactly the two-tail root square of Item nori_snake_nearspanning_root_square_merge_and_parallel_cap_dichotomy_20261009 v2. That Item proves, under hypothetical grand failure, a nonzero exterior a-derivative on one of the two near-spanning cap orientations forces a corresponding earlier two-bit (a,b)-exterior color-change fault along the root-slid P. For m>2, additional unused directions enter the pair root s_de via their COMPLEMENT T\{d,e}; no same-root complementary-support grand certificate follows from P alone.

**OPEN TARGET.** What is needed is a GLOBAL selector or a topological interaction between the Johnson layers attached to DIFFERENT maximal monochromatic paths, rather than an ungrounded degree/edge assumption for a single fan. The physical 3-face antipodal involution couples each arbitrary first-window bit to a different antipodal face, not to another arc of the same fan.
