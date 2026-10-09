# Opposite-color NORI root diamonds impose exact same-face adjacent-transposition extension blockers

# Actual physical-face transposition blockers for opposite-color same-root reversed-tail diamonds

Let n>=5 and let c be ANY binary coloring of physical ordered 3-faces (antipodal oddness not needed). Suppose two GENUINE length-four MONOCHROMATIC geodesics begin at SAME ROOT x, end at SAME PHYSICAL ENDPOINT y, have four pairwise distinct used directions a,b,c,d and specifically direction orders
  P0=(c,a,b,d), color 0 in BOTH windows,
  P1=(a,c,d,b), color 1 in BOTH windows.
These are exactly the two-color diamonds constructed in NORI's item nori_bichromatic_hub_same_root_reverse_tail_opposite_color_diamond_20261008 at a bichromatic hub when opposite-color common-edge certificates are absent. The common midpoint hub is z=x xor {a,c}, and y=x xor {a,b,c,d}. The first TWO and last TWO directions are swapped between the two paths.

Fix ANY fresh unused coordinate e∉{a,b,c,d}.

**Theorem 1 (exact append blocker).** Appending e to P0 and P1 gives two ACTUAL length-five geodesics with window-color words respectively
  (0,0, A_e),  where A_e = c(F(y;{b,d,e}),(b,d,e)),
  (1,1, B_e),  where B_e = c(F(y;{b,d,e}),(d,b,e)).
Crucially, A_e and B_e refer to two ORDERS OF THE SAME PHYSICAL THREE-FACE through their COMMON endpoint y. If neither length-five extension is monochromatic, then
  (A_e,B_e)=(1,0).
If the two order colors are equal, at least ONE extension is monochromatic; if (A_e,B_e)=(0,1), BOTH are monochromatic.

**Theorem 2 (exact prepend blocker).** Prepending e to P0 and P1 gives two ACTUAL length-five geodesics with window-color words respectively
  (C_e,0,0), where C_e=c(F(x;{a,c,e}),(e,c,a)),
  (D_e,1,1), where D_e=c(F(x;{a,c,e}),(e,a,c)).
Again C_e,D_e are two ordered colors on the SAME PHYSICAL three-face, now through common root x. If neither prepended length-five path is monochromatic, then
  (C_e,D_e)=(1,0).
Equal order colors guarantee at least one monochromatic extension; (0,1) guarantees both.

**Proof.** For append, the only new color window consists of the last two directions of P0/P1 followed by e, respectively (b,d,e) and (d,b,e), whose physical free-face has common endpoint y. The first two window colors are 0,0 and1,1 by hypothesis. Appended path monochromatic iff A_e=0 for P0 and iff B_e=1 for P1; simultaneous failure iff (1,0). For prepend, the new window has e followed by first two directions of each path, respectively (e,c,a) and (e,a,c), and through same root x. Prepend P0 stays monochromatic iff C_e=0 and prepend P1 stays monochromatic iff D_e=1; simultaneous failure iff (1,0). QED.

**Corollary 3 (active NORI no-grand constraints in dimension n=6).** In Q_6 a length-five monochromatic directed geodesic can be extended via its only unused coordinate to a FULL one-switch antipodal geodesic, irrespective of the last window color. Hence if the ACTIVE grand conjecture hypothetically fails in Q_6 and a two-color four-edge diamond as above exists, for BOTH unused coordinates e,f it is NECESSARY that at the relevant physical faces:
  c(F(y;{b,d,e}),(b,d,e))=1,
  c(F(y;{b,d,e}),(d,b,e))=0,
  c(F(x;{a,c,e}),(e,c,a))=1,
  c(F(x;{a,c,e}),(e,a,c))=0,
and likewise substituting f for e. These are four precise ordered-face transposition defects per unused direction. They are compatible with the active antipodal reversal law locally; no false contradiction is claimed.

**Corollary 4 (higher-dimensional conditional extension).** If n>6 and an opposite-color rank-(n−2) geodesic diamond can be constructed with two distinct final ordered directions swapped between its colors, then an equal-color pair on EITHER shared physical extension face (root or endpoint) produces a MONOCHROMATIC (n−1)-edge path. Extending by the final unused direction gives grand closure. The theorem therefore identifies an exact physical three-face adjacent-transposition obstruction to lifting a color-flexible diamond across its remaining coordinates. A general existence theorem for such near-spanning diamonds is NOT known.

**Research strategy.** The present color-free reachability diamond provides same-root SAME-SUPPORT reversed tails. To upgrade it into a complementary-support grand witness, attempt a sequence of actual root/terminal-order exchanges that either (i) extends one of the mono colors by a fresh coordinate (eliminating a terminal tail), or (ii) accumulates transposition defects whose antipodal sign product around a closed compatible memory cycle is odd. The local blockers alone do not close grand NORI.
