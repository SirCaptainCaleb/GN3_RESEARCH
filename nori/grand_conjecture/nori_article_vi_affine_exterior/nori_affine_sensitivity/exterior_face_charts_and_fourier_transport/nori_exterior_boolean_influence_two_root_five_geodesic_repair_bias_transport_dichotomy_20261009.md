# Exterior Boolean influence forces real two-root five-geodesic repairs; six-support bias-or-transport dichotomy

# Exterior Fourier influence forces genuine rooted five-geodesic repair: an exact bias–transport dichotomy

**Definitions.** Let n>=6 and c be an active binary NORI coloring of actual physical ordered-three-faces of Q_n, c(bar F,rev pi)=1-c(F,pi). For any ordered triple pi=(a,b,c) of DISTINCT directions with unordered free set T, put E=[n]\T and define the face-sign function f_pi(z)=(-1)^{c(F_z(T),pi)} for uniform z∈F2^E. Let its global bias be m_pi=E_z f_pi(z) and its exterior-direction influence be
  Inf_e(pi)=Pr_z[f_pi(z) != f_pi(z xor e_e)], e∈E.
This is a literal PHYSICAL face change across an exterior coordinate, not a change of starting corner within one face.

**THEOREM 1 (exact exterior derivative to TWO-ROOT repair).** For EVERY five pairwise distinct directions (a,b,c,d,e), fix the FULL five-edge direction word p=(a,b,c,d,e), and let G_p(x) be the event that the three ACTUAL ordered-three-face windows of the rooted five-edge geodesic P(x,p) change color at most once. Then
    Pr_(x uniform in Q_n) G_p(x) >= (1/2)*Inf_e(a,b,c).
The coloring need not satisfy active antipodal oddness for this individual inequality; only physical ordered-face locality matters.

**Proof.** Fix an arbitrary actual cube vertex z and compare the two GENUINE five-edge paths of identical direction word p rooted at
  x0=z xor {a,b,c},    x1=x0 xor e_e.
Their three REAL ordered-window faces, in order, are
  U0=F_z({a,b,c}) with orientation (a,b,c),
  V0=F_z({b,c,d}) with orientation (b,c,d),
  M=F_z({c,d,e}) with orientation (c,d,e),
and
  U1=F_(z xor e)({a,b,c}) with orientation (a,b,c),
  V1=F_(z xor e)({b,c,d}) with orientation (b,c,d),
  M=F_(z xor e)({c,d,e}) with orientation (c,d,e).
The last face M is literally IDENTICAL in both paths because e is FREE inside it, whereas U0,U1 differ in the physical exterior e-bit. If their first colors differ, c(U0)!=c(U1), both three-bit words (c(U0),c(V0),c(M)) and (c(U1),c(V1),c(M)) cannot be strictly alternating: strict alternation of both would require the first color of each to equal the SAME last color c(M). Hence
   1{c(U0)!=c(U1)} <= 1{G_p(x0)} + 1{G_p(x1)}
for EVERY physical z, and all colors of the intermediate V windows are arbitrary. Under uniform z, x0 and x1 are separately uniform roots and the left event has probability exactly Inf_e(a,b,c). Taking expectations proves the inequality. All paths are genuine distinct-direction geodesics; no virtual stitching occurs. QED.

**THEOREM 2 (Fourier Poincare root-shuttle supply).** For every fixed ordered triple pi=(a,b,c) and for EACH exterior e∈E choose any direction d(e)∈E\{e} (available since n>=6). Let p_e=(a,b,c,d(e),e). Then
    sum_(e∈E) Pr_x G_(p_e)(x)
       >= (1/2)*sum_(e∈E) Inf_e(pi)
       >= (1-m_pi²)/2.
In particular if |m_pi|<=1/3, the sum of honest rooted five-geodesic good-probabilities across these distinct exterior-last-direction words is >=4/9. Also some e has
    Pr_x G_(p_e)(x) >= (1-m_pi²)/(2(n-3)).
For |m_pi|<=1/3 this fixed-word probability is >=4/[9(n-3)].

**Proof.** The first inequality is Theorem1 summed over e. For the second, expand the ±1 face-sign function in Walsh characters f_pi(z)=sum_(S⊆E) fhat_pi(S) chi_S(z), with chi_S(z)=(-1)^{sum_(j∈S)z_j}. Orthogonality gives
    Inf_e(pi)=sum_(S containing e) fhat_pi(S)^2,
    sum_e Inf_e(pi)=sum_(nonempty S) |S| fhat_pi(S)^2
         >=sum_(nonempty S) fhat_pi(S)^2=1-m_pi².
The bounds follow by averaging over the n-3 exterior directions. This Fourier identity is finite Boolean-cube algebra and does not invoke an external theorem. QED.

**THEOREM 3 (universal six-support bias-or-physical-transport dichotomy).** Fix any six distinct coordinate directions V⊆[n]. At least ONE of the following alternatives holds:
(A) An ACTUAL monochromatic five-edge cube geodesic exists with five direction names from V.
(B) There is some ordered triple pi=(a,b,c) using V with |m_pi|<=1/3. Consequently it has sum_(e exterior to pi) Inf_e(pi)>=8/9, and there is a literal five-direction word p=(a,b,c,d,e), with e exterior to pi and d another exterior direction, for which a uniformly random actual root gives a <=1-switch five-geodesic with probability >=4/[9(n-3)].

Proof. Assume (A) fails. Suppose contrary to (B) that EVERY ordered triple pi using V has |m_pi|>1/3. Then its unique majority color q(pi) over ALL physical exterior bit assignments has probability >2/3. Active NORI gives m_(rev pi)=-m_pi by complementing the entire exterior cube, so q(rev pi)=1-q(pi), i.e. q is a bona fide coordinate-only reversal-odd ordered-triple coloring on V. The proved six-direction monotone-facet transfer theorem (Item nori_six_direction_monochromatic_facet_transfer_20261008) supplies five distinct directions p1,...,p5∈V for which
  q(p1,p2,p3)=q(p2,p3,p4)=q(p3,p4,p5)=q0.
For a UNIFORMLY random full cube root x, each of the three REAL ordered windows along this five-edge direction word has a uniformly distributed exterior-bit string. Therefore its probability of disagrement with q0 is <1/3, for each of the three windows individually. The union bound shows a POSITIVE probability that all three ACTUAL windows equal q0, contradicting failure of (A). Hence some |m_pi|<=1/3, and Theorem2 supplies (B). QED.

**Consequences for hypothetical grand failure.** For n=6, a monochromatic five-edge geodesic extends by the one remaining direction to a FULL antipodal one-switch six-edge geodesic. Thus if a six-dimensional counterexample existed, alternative (A) would be impossible, and it would have a real ordered-three-face orientation with exterior influence sum >=8/9, hence many forced two-root repair witnesses. In arbitrary n>6, a monochromatic five-edge geodesic is only a useful local seed; Theorem3 remains an unconditional dichotomy, not full grand closure.

**Relation to NORI topological forcing.** The rooted hexagon transport Item nori_exterior_root_transport_hexagon_exact_good_triangles_rigidity_dichotomy_20261009 showed structurally that a color-sensitive exterior one-bit shuttle forces one of two genuine five-path repair triangles. Theorem1 turns this exact HEXAGON INCIDENCE into an INFLUENCE-TO-WITNESS COUNT, and Theorem2 relates its density to the full exterior Fourier spectrum. Together with the multibit projection theorem (Item nori_multibit_exterior_chart_fourier_intersection_compression_mono_five_threshold_20261009), the result precisely separates two modes: low nonconstant Fourier energy provides a coordinate-only majority profile and mono5 extraction; high exterior energy supplies many actual cross-root repair paths. The remaining global obstruction is synchronizing these shorter certified paths into the SAME ROOT and complementary REVERSED TWO-TAIL supports needed for full one-switch antipodal extraction.

## Elevation: uniformity-r universal two-root nonalternation lemma

The exact influence-to-good-path bound extends with NO change of constant to every ordered-r-face coloring, every r>=2, n>=r+2, with no antipodal condition. Fix distinct directions p1,...,p_(r+2) and put e=p_(r+2). For an actual physical ordered r-face of free tuple (p1,...,pr), define its exterior influence Inf_e by toggling the exterior bit e. Then for a UNIFORM actual cube root x, the (r+2)-edge genuine direction-distinct geodesic of that full direction word has three consecutive ordered-r-face windows, and
  Pr_x(its 3-window word has <=1 switch) >= Inf_e(p1,...,pr)/2.
Indeed the two paths from x and x xor e have DIFFERENT first-window colors whenever the exterior derivative is nonzero, while their LAST window is the SAME physical ordered r-face because e belongs to its free coordinate set. If both 3-window words strictly alternated, their first colors would have to equal that common last color, contradiction. Average the pointwise two-root inequality. There are no additional seam windows: an (r+2)-edge path has exactly THREE r-face windows.

For any ordered r-tuple pi, the identical Fourier/Poincare calculation gives
 sum_(e exterior) Inf_e(pi) >=1-(E f_pi)².
Choosing a distinct direction d for each e gives a sum of actual rooted (r+2)-geodesic good probabilities at least [1-(E f_pi)²]/2. This reveals the two-root repair mechanism as a general finite-cubical phenomenon independent of uniformity three. In the active r=3 problem, the strengthened lemma remains a local witness supply, not the missing full-n root-compatible reachability intersection.


## Elevation: exterior sensitivity controls the expected switch count of FULL antipodal paths

**THEOREM 4 (unrestricted influence-refined full-geodesic switch bound).** Let n>=5 and c be ANY binary coloring of ACTUAL physical ordered three-faces, with or without antipodal NORI oddness. Define the GLOBAL normalized exterior-bit influence
  I_avg = [1/(n(n-1)(n-2)(n-3))] *
          sum_(ordered distinct a,b,c) sum_(e outside {a,b,c})
             Inf_e(a,b,c)
          ∈[0,1].
For a uniformly chosen cube root X and uniformly random full direction permutation P, let D(X,P) count ACTUAL consecutive ordered-three-face color changes on the genuine full n-edge antipodal geodesic. Then
  E[D(X,P)] <= (n-3)*(1-max{1/5,I_avg/4}).
Consequently some FULL actual antipodal n-edge geodesic has at most
  floor((n-3)*(1-max{1/5,I_avg/4}))
switches. In particular, whenever I_avg>4/5, this STRICTLY improves the previously proved universal 4(n-3)/5 expectation and path bound. When I_avg=1 the bound becomes 3(n-3)/4 (the stronger exact eight-monochromatic-roots parity theorem applies in that extreme situation).

**Proof.** For a random ACTUAL ordered five-edge geodesic, sample its direction order (a,b,c,d,e) uniformly from all five-tuples of distinct directions and sample a full cube root X uniformly. Let G be the event that its three ordered-three-face windows have <=1 switch. Theorem1 for each five-tuple gives
  Pr_X(G|a,b,c,d,e) >= (1/2)Inf_e(a,b,c).
Conditioned on ordered triple (a,b,c), the final direction e in a uniformly random ordered pair (d,e) of other distinct coordinates is itself UNIFORM in E=[n]\{a,b,c}. Averaging hence yields
  Pr(G)>=I_avg/2.
Write Q for the probability that TWO successive genuine ordered-three-face windows have EQUAL colors under a uniform ordered four-tuple of distinct directions and a uniform root. Along a uniform ordered five-tuple, its two adjacent comparisons have this same marginal Q. Because a three-bit word has <=1 switch exactly when at least one of its two adjacent comparisons is equal, the union bound gives
  Pr(G)<=2Q.
Thus Q>=I_avg/4.

Independently the proved physical odd-five-cycle pentagon inequality yields Q>=1/5 for every such coloring: under uniformly random physical hub and five cyclic direction order, at least one of its five cyclic adjacent window comparisons is equal. The distribution of a random cyclic consecutive ordered four-tuple is exactly uniform among all ordered distinct four-tuples, so the comparison equality probability Q is at least1/5. Combine to obtain Q>=max{1/5,I_avg/4}.

Finally, in a uniformly random FULL rooted n-geodesic every one of its n-3 adjacent ordered-window comparisons is distributed as exactly the same uniform physical ordered-four-tuple comparison: the four direction names are uniform and the physical root at that subpath is uniform, because the global root X is uniform. Therefore each switch indicator has expectation 1-Q. Summing without any independence assumption gives E D=(n-3)(1-Q), proving the bound. QED.

**Method limitation.** The exterior-sentinel fully sharp eight-support obstruction has I_avg potentially high on some orientations and very low on others; the present global theorem requires averaging over ALL ordered triple supports and exterior directions, not just a fixed selected rank-eight chamber. Its bound is a genuine all-n analytic improvement for high-influence physical colorings, but for low/medium normalized influence it reduces to the existing 4/5 estimate and cannot force <=1 switches for unbounded n.
