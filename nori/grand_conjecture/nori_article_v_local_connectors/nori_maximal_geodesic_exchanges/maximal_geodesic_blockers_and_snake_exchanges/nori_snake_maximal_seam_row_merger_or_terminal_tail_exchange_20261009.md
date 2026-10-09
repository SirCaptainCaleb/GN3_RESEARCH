# Maximal monochromatic snake: seam admissibility forces a full Johnson merge row or tail-swap/blocker descent

# Snake-type maximal terminal rerouting: q-seam directions force a complete row of opposite-corner four-geodesic merges

Sources: active NORI physical ordered-three-face coloring; prior snake fan Item nori_snake_maximal_fan_johnson_root_hypersimplex_and_independent_merge_bits_20261009; inspiration from attached Devine–Milans *Linear Hypergraph Turan Numbers of Paths*. No web/literature search.

Fix n>=6. Let P be a GLOBAL maximum-length monochromatic geodesic of SOME FIXED color q, with k>=4 edges, direction word
    P = (u_1,...,u_(k−2),a,b),
starting at x and ending y, and let T be its set of m=n−k>=2 unused directions. Global q-maximality suffices; grand conjecture failure is NOT assumed. As P cannot be extended in color q, all attempted terminal ordered-three-face windows (a,b,d) for d∈T have color 1−q, and their antipodal reversed windows (d,b,a) at the opposite physical faces have color q. Put t=x xor {u_1,...,u_(k−2)}=y xor {a,b} and h=bar t; note h=bar y xor {a,b}.

Write v=u_(k−2), w=u_(k−3) (the final two distinct prefix directions). Define the ACTUAL root-matched seam bits
 alpha = color of ordered window (w,v,b) in the (k−1)-edge prefix U,b from root x;
 beta_d = color of ordered window (v,b,d) in the k-edge path U,b,d from root x;
 gamma_de = c(F_t({b,d,e});(b,d,e)) for distinct d,e∈T.

**LEMMA (SNAKE SEAM IMPLIES COMPLETE MERGE ROW).** If alpha=q AND beta_d=q for some d∈T, then gamma_de=1−q for EVERY e∈T\{d}. Hence every four-edge geodesic
   Q_ed: root s_de=x xor {a,b} xor (T\{d,e}), direction (e,d,b,a), endpoint bar y
is MONOCHROMATIC q, for all e !=d. In particular one admissible seam direction d forces m−1 genuine q four-geodesic branches, lying at m−1 distinct vertices of the Johnson layer of two-unused-direction roots.

**Proof.** For any e!=d, the (k+1)-edge literal geodesic from x whose order is
  (u_1,...,u_(k−2),b,d,e)
has the first k−4 ordered three-face windows equal to P's original first k−4 windows (all color q), followed by EXACTLY the three windows (w,v,b), (v,b,d), (b,d,e). The first two have color q by alpha=beta_d=q. If gamma_de=q, the entire (k+1)-edge geodesic is q-monochromatic, contradicting global k maximality. Thus gamma_de=1−q for every e. Antipodal reversal pairs F_t({b,d,e});(b,d,e) with F_h({b,d,e});(e,d,b), so each such first merge window has color q. The second window of Q_ed is (d,b,a), already q by the antipodal reversal of the blocked terminal extension (a,b,d). Hence both windows of each Q_ed are q, and Q_ed is a real four-edge geodesic rooted at s_de and ending bar y. QED.

**Corollary (exact terminal-blocker/merge-density dichotomy).** If alpha=q then, for each d∈T, either beta_d=1−q (a blocked seam) or the ENTIRE row {Q_ed:e≠d} comprises q-monochromatic four-edge paths. The latter provides m−1 certifications. Define D={d∈T:beta_d=q}. The number of ordered certified q four-edge paths forced by this lemma is at least |D|(m−1); for each distinct {d,e} at most two orders are counted and both are genuinely distinct physical paths. If alpha!=q, no conclusion about beta or merge rows follows from this argument.

**Corollary (old path's tail can be swapped, or a shorter fully blocked fan is born).** Suppose alpha=q and beta_d=1−q for ALL d∈T (the fully blocked seam alternative). Consider beta_a, the next ordered triple (v,b,a) after the mono (k−1)-edge prefix U,b. If beta_a=q, then
    P_swap=(u_1,...,u_(k−2),b,a)
is a distinct q-monochromatic k-edge path from SAME root x to SAME endpoint y with REVERSED final ordered pair (b,a). If beta_a=1−q, then the q-monochromatic (k−1)-edge geodesic U,b is terminal-UNEXTENDABLE IN COLOR q by every unused direction {a}∪T, yielding a NEW fan with m+1 roots via the previous snake lemma. These are the only cases. This is a literal path exchange/rank-drop step, not the original loose-hypergraph 'free reorder terminal r−1 vertices' assumption.

**Guardrails and challenge.** An m−1 row of monochromatic Q paths has distinct starting roots s_de as e varies; there is still no direct same-root complementary support certificate. A fan root s_de should be coupled to another monochromatic (n−2)-edge reversed-two-tail branch at THAT root, a genuine topological or global exchange obligation. If beta_d=1−q for all d, the shorter terminal fan is not necessarily a globally maximum q path, so the row lemma cannot simply be iterated downward without a new monotone potential. The lemma does NOT establish universal positive |D| nor grand closure.

**Conjectural next tactic.** Select a maximum q path P with extremal secondary statistic over terminal memories, then exclude indefinite tail-swap and blocked-prefix descent, leaving at least one free beta_d and hence a positive Johnson row. Prove that the root-Johnson families attached to P, P_swap and globally antipodal partner intersect at a root with reversed complementary support. None of these last implications is established.
