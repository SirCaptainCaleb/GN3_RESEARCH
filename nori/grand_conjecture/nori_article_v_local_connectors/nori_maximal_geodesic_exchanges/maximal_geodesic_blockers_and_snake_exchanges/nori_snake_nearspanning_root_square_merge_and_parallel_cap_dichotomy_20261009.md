# Snake-fan two-root-square synchronization and parallel-cap versus root-slide defect dichotomy

# Two-missing-direction snake synchronization: exact two-root-square grand-extraction and failure dichotomy

Active NORI: binary coloring c of ACTUAL ordered physical 3-faces, c(bar F,rev pi)=1-c(F,pi). No outside web/literature used. This work is a genuine lift of the user-provided Devine–Milans linear-hypergraph snake method, and extends Item nori_snake_digraph_maximal_path_dual_terminal_fan_and_two_step_cap_20261009. The grand conjecture remains open.

Let n>=5. Suppose P is a MONOCHROMATIC direction-distinct (n−2)-edge geodesic starting at x, with ordered direction word
   p=(u_1,...,u_(n-4),a,b)
of window color q, and missing coordinates {d,e}. Put U={u_1,...,u_(n-4)}, y=x xor U xor {a,b}, t=x xor U=y xor {a,b} (the point immediately BEFORE the last a,b edges of P), and define
   s=x xor {a,b},   h=bar y xor {a,b}.
Because the full coordinates are U sqcup {a,b,d,e}, one has bar y = x xor {d,e}; hence
   h=s xor {d,e},  s=h xor {d,e}.
Use notation F_z(A) for the genuine physical cube face through z with free coordinate set A. For a face F with specified ordered free directions pi, write c(F;pi).

**Lemma 1 (exact paired cap under hypothetical grand failure).** Assume no full at-most-one-switch antipodal geodesic exists. Appending the two missing directions to P in either order yields
 c(F_y({a,b,d});(a,b,d)) = c(F_y({a,b,e});(a,b,e)) = 1−q,
 c(F_y({b,d,e});(b,d,e)) = c(F_y({b,d,e});(b,e,d)) = q.
The two last orientations belong to the SAME ACTUAL FACE F_y({b,d,e}), because the two paths reach that face with roots y xor d or y xor e, and d,e are free. Proof: first new window must have 1−q or a full path with at most one switch; second new window must revert to q or again there is a full path with at most one switch. This is the existing two-step-cap lemma, included for full context.

**Lemma 2 (fan merging has a SINGLE exact root).** The two reversed-antipodal windows guaranteed by blocked extension have
 c(F_bar_y({a,b,d});(d,b,a))=c(F_bar_y({a,b,e});(e,b,a))=q.
For the full genuine 4-edge geodesics
   Q_de: root s, order (d,e,b,a), endpoint bar y,
   Q_ed: root s, order (e,d,b,a), endpoint bar y,
their SECOND three-coordinate windows are exactly the known q fan windows. Their FIRST windows lie in the SAME physical face F_h({b,d,e}), with respective orders (d,e,b) and (e,d,b). Therefore each Q is monochromatic q if and only if its first window is q. No unspecified seam windows occur.

**MAIN THEOREM (EXACT CONDITIONAL GRAND-EXTRACTION AT TWO-TAIL ROOT SLIDE).** Suppose either Q_de or Q_ed is monochromatic q AND the ORIGINAL (n−2)-letter direction word p, traversed from the TWO-BIT-SLID ROOT s=x xor a xor b, is monochromatic of EITHER color. Then grand NORI closure holds. Indeed both monochromatic paths start at s, the shifted P has terminal ordered pair (a,b) and support U before that pair, and Q has terminal ordered pair (b,a) and support {d,e} before it. Their supports U and {d,e} are complementary in [n]\{a,b}. Apply the already proved exact same-root reversed-two-tail splice criterion Item nori_exact_color_free_reversed_two_tail_complement_reachability_grand_equivalence_20261008. No requirement that the two branch colors agree.

**EXACT FAILURE DICHOTOMY, one per cap orientation.** Continue assuming the GRAND CONJECTURE FAILS, and set C=F_h({b,d,e}), B=F_t({b,d,e}), A=F_y({b,d,e}). Note B=bar C since t=bar h, and A and B are two PARALLEL PHYSICAL 3-faces differing only in the single fixed outside coordinate a (because t=y xor a xor b and b is free). Lemma1 says BOTH orientations (b,d,e) and (b,e,d) on face A have color q.

For each ordered pair (d,e)/(e,d), one of the following MUST hold:
 (i) its 4-edge snake-merged Q is monochromatic q, and the original p started from s is NONMONOCHROMATIC (otherwise MAIN THEOREM closes NORI);
 (ii) its 4-edge snake-merged Q has first window color 1−q; the antipodal-reversal law then forces the corresponding reversed order on face B to be q:
   if c(C;(d,e,b))=1−q then c(B;(b,e,d))=q;
   if c(C;(e,d,b))=1−q then c(B;(b,d,e))=q.
 In case (ii), this ordered orientation is q on BOTH parallel faces A and B, a literal a-direction 3-face square-prism agreement.

Moreover if (i) holds, a *root-slide defect* is certified: the final window of shifted p has color q because toggling a,b preserves the same physical 3-face of that window (both are its free coordinates), yet p from s is nonmono. Hence some EARLIER triple window (u_j,u_(j+1),u_(j+2)) with j<=n−5 has changed color q ->1−q between the physical face based at x and the face based at s; these two faces differ by simultaneous toggling of the OUTSIDE coordinates a,b. Such a genuine two-bit exterior root-slide defect can be factored through an intermediate one-bit root translate, showing at least one of the a- or b-exterior face edges carries a color change for this orientation.

Thus under grand failure, a near-spanning mono path necessarily yields an EXPLICIT CHOICE: either a two-bit root-slide color defect OR (for each snake-matching orientation failing) a monochromatic parallel two-layer cap. If both Q orders fail, BOTH orientations (b,d,e),(b,e,d) are q on BOTH A and B. If at least one Q succeeds, the first part certifies a root-slide defect. This is a LOCAL DISJUNCTION, NOT a proof that one alternative globally contradicts grand failure.

**Important exact identities/guardrails.** F_h({b,d,e}) and F_y({b,d,e}) are generally NOT THE SAME FACE (their other outside bits differ); antipodal pairing takes F_h to F_t, not necessarily F_y. The fact that s=x xor a xor b depends on there being EXACTLY TWO unused directions d,e, i.e. P length n−2. Such mono (n−2)-paths may not exist on a chosen coordinate support/root for a valid NORI coloring; this is conditional. Do not treat global failure as proving their existence.

**Next step.** Develop a lexicographic descent over longest monochromatic paths which charges (i) an earlier-index two-bit root-slide defect, while (ii) builds a connected monochromatic prism face-sheet through cap copies. A global topological mechanism must rule out all defects/prisms without assuming arbitrary physical face colors can be reordered for free.

**ELEVATION: EXACT DISCRETE-EXTERIOR DERIVATIVE PROPAGATION.** In the GRAND-FAILURE setting, define A=F_y({b,d,e}) and B=F_t({b,d,e}), where t=y xor a xor b. Since b is free in both, B and A are adjacent physical 3-faces separated by the single *exterior* direction a. Let
 Delta_a^pi = c(A;pi) XOR c(B;pi)
for pi in {(b,d,e),(b,e,d)}. The forced cap guarantees c(A;pi)=q for BOTH pi.
By the exact antipodal pairing C=bar B,
  c(C;(e,d,b))=1−c(B;(b,d,e)), 
  c(C;(d,e,b))=1−c(B;(b,e,d)).
Therefore:
   Q_ed is monochromatic q  IFF  Delta_a^(b,d,e)=1;
   Q_de is monochromatic q  IFF  Delta_a^(b,e,d)=1.
Thus successful SNAKE FAN MERGING is EXACTLY a nonzero one-coordinate EXTERIOR derivative at the cap, rather than some unidentified 'first window' constraint. Together with the conditional grand-extraction theorem, no grand closure implies the rigorously FORCED DERIVATIVE TRANSFER:
   [Delta_a^(b,d,e)=1 OR Delta_a^(b,e,d)=1]
   => there exists j<=n−5 such that 
       c(F_{x,j};(u_j,u_(j+1),u_(j+2)))
         XOR
       c(F_{s,j};(u_j,u_(j+1),u_(j+2))) = 1.
Here F_{x,j} is the actual j-th ordered three-face window of P from root x, and F_{s,j} is that of the SAME direction order P rooted at s=x xor a xor b. The two physical faces differ precisely in the TWO EXTERIOR DIRECTIONS a,b because both occur only as the last two directions, and j<n−4. The final window j=n−4 is literally unchanged under this slide because both a,b are free. In terms of discrete derivatives of face colors this is a propagation law
    exterior a-derivative at the TERMINAL {b,d,e} cap
       => exterior (a xor b)-derivative at an EARLIER core window.
The earlier two-bit derivative necessarily factors as a XOR of two one-bit derivatives along the a,b root square; hence one of its one-bit edges differs. No theorem currently turns this earlier face derivative into a NEW monochromatic near-spanning witness of smaller rank, so the iteration/descent remains open.

**DIRECTION-ONLY SANITY CHECK.** For coloring independent of physical exterior bits, both Delta_a^pi=0 identically and the two-bit slide of P is automatically monochromatic. Thus the conditional theorem correctly cannot produce a fan-merged path under hypothetical failure; the persistent two-layer cap is consistent with same-face reversal-oddness. The transfer is genuinely exploiting EXTERIOR dependence, not claiming to solve the boundary (3,3)-tournament subclass by itself.
