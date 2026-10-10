# Arbitrary Q7 exact two-root exterior derivative and g-third closure test

# Exact two-root derivative extraction for arbitrary physical Q7 NORI

Let c be ANY legal ordered-three-face NORI coloring of Q_7, and fix a direction g, a residual root y∈Q_6, and residual order (a,b,c,d,e,f). Consider the two genuine full geodesics with direction order (a,b,g,c,d,e,f) and starting vertices differing only in the g-bit. Their first three window colors are identical, since their ordered faces all contain g as a free direction; call this triple G=(G_1,G_2,G_3). Let U=(u_1,u_2) be the last two window colors for initial g-bit 0 and let Δ=(δ_1,δ_2) be their physical g-exterior sensitivity vector:
δ_i=c(F_i with g=0,π_i)+c(F_i with g=1,π_i) in F_2.
The last two window colors for initial g-bit 1 are U+Δ. (Any fixed parity from traversing g can be absorbed into the definition of U.) Crucially the two δ_i need not agree for a general legal coloring.

**Theorem (complete two-root certificate).** At least one of these two full geodesics has at most one window-color change if and only if one of the following holds:

(1) G is constant with value t, and either U≠(1−t,t) or Δ≠(0,0).

(2) G has exactly one change, ends in t, and (t,t)∈{U,U+Δ}.

If G alternates, both full geodesics are bad.

**Proof.** A constant triple ttt can only accumulate two changes from a trailing pair when that pair equals (1−t,t). Consequently both initial g choices are bad precisely if their trailing pairs are both that forbidden pair, equivalently U=(1−t,t) and Δ=00. A triple with exactly one switch has already spent its switch; both trailing bits must equal its last color t. An alternating triple already has two switches. This exhausts all cases. QED.

**Flipper specialization.** If g is universal exterior flipper, Δ=11. The certificate simplifies to: G constant, or G one-switch with u_1=u_2. The exact 480-vertex odd-cycle reduction and computer-assisted Q7 closure are Items nori_q7_flipper_odd_cycle_bipartite_reduction_20261009 and nori_q7_universal_exterior_flipper_computer_verified_full_closure_20261009.

**Grand-conjecture frontier.** For arbitrary c, the physical two-bit sensitivity Δ is complement-reversal even across opposite six-dimensional charts. A full proof must combine odd antipodal h-colors on the g-containing windows with residual roots/order changes to force (1) or (2) for some g. In case G constant, every packet with at least one sensitive trailing face certifies immediate closure. The only root-pair obstruction is a pair of g-insensitive trailing faces colored (1−t,t).
