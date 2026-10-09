# Two-ended exterior sensitivities force monochromatic five-paths; global influence threshold 1/2

# Two-ended exterior sensitivity forces a genuine monochromatic five-geodesic

Let n>=5, and let c assign bits to actual ordered physical three-faces of Q_n; no antipodal axiom is required. For any ordered triple pi of distinct directions, define Inf_j(pi) as the probability over uniformly random exterior bits that toggling exterior direction j changes the color of (F,pi).

THEOREM (complementary-pivot five-window forcing). For every ordered five-tuple p=(a,b,c,d,e) of distinct directions, write M_p for the event that the genuine five-edge geodesic of direction order p from uniform cube root X has all THREE ordered three-face colors identical. Then

 Pr_X(M_p) >= (1/4) E_t[ alpha_p(t) beta_p(t) ]
              >= (1/4) max(0, Inf_d(a,b,c)+Inf_b(c,d,e)-1),

where t ranges uniformly over the root bits on [n]\{a,b,c,d,e}; alpha_p(t) is the influence in direction d of the first ordered face (a,b,c) conditional on t (averaging its other exterior bit e), and beta_p(t) is the influence in direction b of the final ordered face (c,d,e) conditional on t (averaging its other exterior bit a).

In particular, Inf_d(a,b,c)+Inf_b(c,d,e)>1 guarantees a genuine MONOCHROMATIC 5-edge geodesic of the prescribed direction order p. If a physical coloring has NO monochromatic five-edge geodesic anywhere, then for EVERY ordered five-tuple p and every fixed outside-five chart t, either alpha_p(t)=0 or beta_p(t)=0; hence necessarily Inf_d(a,b,c)+Inf_b(c,d,e)<=1.

PROOF. Fix t and write A,B,D,E for the four independent initial root-bit variables associated respectively with a,b,d,e, absorbing the deterministic flips of a,b in the later windows into the definitions of A,B. The unused initial bit c has no effect on any of the three physical windows. Their actual colors have the exact dependency pattern
  U=U(D,E) for the ordered face (a,b,c);
  V=V(A,E) for the ordered face (b,c,d);
  W=W(A,B) for the ordered face (c,d,e).
These are precisely the physical exterior coordinates at the first, second and third windows; all remaining bits are t.

Define delta_U(E)=U(0,E) XOR U(1,E) and delta_W(A)=W(A,0) XOR W(A,1). For each fixed pair (A,E) with delta_U(E)=delta_W(A)=1, the middle bit V(A,E) is fixed. There is a UNIQUE value of D with U(D,E)=V(A,E), and INDEPENDENTLY a UNIQUE value of B with W(A,B)=V(A,E). Therefore at least 1/4 of the (D,B) choices make all three colors equal, conditional on any such (A,E). The event delta_U(E)=1 depends only on E, and delta_W(A)=1 depends only on A; A and E are independent under the uniform root. Thus
  Pr(M_p | t) >= (1/4) Pr_E(delta_U(E)=1) Pr_A(delta_W(A)=1)
              = alpha_p(t) beta_p(t)/4.
Average t. Since alpha,beta∈[0,1], alpha beta >=alpha+beta−1 pointwise, while E_t alpha=Inf_d(a,b,c) and E_t beta=Inf_b(c,d,e). Nonnegativity gives the displayed bound. If M_p is impossible, E_t alpha beta=0; each nonnegative product is then zero, proving the chartwise alternative. QED.

COROLLARY (global influence threshold and counting). Define
 I_avg= 1/[n(n−1)(n−2)(n−3)] sum_(ordered distinct a,b,c) sum_(j outside {a,b,c}) Inf_j(a,b,c).
Choose a uniformly random full cube root and a uniformly random ordered five-tuple of distinct coordinate directions. Both oriented endpoint-pivot incidences (abc,d) and (cde,b) are uniform among the ordered-triple/exterior-direction incidences. The positive-part function is convex, so averaging the theorem gives
 Pr_(X,p)(the five-edge geodesic is MONOCHROMATIC)
      >= max(0,2 I_avg−1)/4.
Consequently any coloring with I_avg>1/2 contains an actual monochromatic five-edge geodesic. Conversely a coloring without such a path necessarily has I_avg<=1/2. This gives a structural high-exterior-influence-to-MONOCHROMATIC-PATH theorem, complementing the previously established one-ended influence-to-ONE-SWITCH five-path inequality.

SHARPNESS. For every n>=5 let c(F,pi)=parity(number of exterior 1-bits of F) XOR h(pi), with h(pi)=0 if n is even and h(a,b,c)=1[a>c] if n is odd. This is a legal active NORI coloring: the exterior parity changes under complementation by (n−3) mod 2, and h(rev pi) XOR h(pi) is 0 for even n, 1 for odd n. Every exterior-coordinate influence equals 1, so I_avg=1. For every five-direction order, equality of its consecutive three window colors is equivalent to two independent binary linear equations, one supported on the pair {a,d} and one on the disjoint pair {b,e}. Thus exactly one quarter of the 2^n roots produce a monochromatic five-geodesic. The coefficient 1/4 and the global lower bound at I_avg=1 are sharp even within active NORI.

SCOPE. A monochromatic five-edge path closes full NORI immediately for n=5 and, by appending the single unused direction, gives a full one-switch geodesic when n=6. For n>6 it is a certified physical seed; the global complementary-support, root-coupled terminal-memory splice remains to be established. The inequality improves the frontier by upgrading sufficiently combined opposite-end exterior sensitivity to a MONOCHROMATIC rather than merely one-switch length-five certificate, with a quantitative rooted count.

## Elevation: arbitrary uniformity r, with the same optimal threshold

The entire theorem extends unchanged from ordered three-faces to ordered r-faces for every integer r>=2 and every ambient dimension n>=r+2, without an antipodal axiom. Given an ordered (r+2)-tuple p=(a_1,...,a_(r+2)), its THREE successive genuine ordered r-face window colors have the SAME dependence pattern
 U(D,E), V(A,E), W(A,B)
on the independent initial bits A=a_1 (with a fixed prefix flip absorbed), B=a_2 (also with prefix flip absorbed), D=a_(r+1), and E=a_(r+2); the other r−2 interior direction bits are FREE in all three physical r-faces. Consequently
 Pr(rooted monochromatic (r+2)-edge path of prescribed p)
  >= (1/4) max(0, Inf_(a_(r+1))(a_1,...,a_r)
                     + Inf_(a_2)(a_3,...,a_(r+2)) −1).
The chartwise product inequality and the exact same proof apply. Averaging over uniform ordered (r+2)-tuples yields the global arbitrary-uniformity threshold
 Pr_(X,p)(monochromatic (r+2)-edge ordered-r-window geodesic)
  >= max(0, 2 I_avg^(r)−1)/4,
where I_avg^(r) is the uniform mean exterior-bit influence among all ordered r-face/oriented-exterior-direction incidences. Thus I_avg^(r)>1/2 forces a physical monochromatic (r+2)-edge geodesic for every r>=2.

The numerical factor 1/4 is sharp even under antipodal-reversal oddness: choose exterior-parity coloring with orientation offset h satisfying h(rev pi) XOR h(pi)=1 XOR((n−r) mod 2); take h identically0 when n−r odd, and h(pi)=1[pi_1>pi_r] when n−r even. For every fixed full (r+2)-tuple, equality of its three window colors imposes two independent parity equations on the disjoint root-bit pairs {a_1,a_(r+1)} and {a_2,a_(r+2)}, giving monochromatic probability exactly 1/4. This extension demonstrates that the two-ended mechanism is genuinely general finite-cubical topology/Boolean analysis, while the full-spanning NORI extraction problem remains separate.
