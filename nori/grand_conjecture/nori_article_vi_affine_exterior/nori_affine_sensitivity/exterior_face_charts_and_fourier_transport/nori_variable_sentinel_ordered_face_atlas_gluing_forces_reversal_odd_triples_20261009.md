# Distinct exterior sentinels on a shared physical triple force reversal oddness and six-support monochromatic surplus

# Complete variable-sentinel chart gluing: changing the exterior bit forces literal reversal oddness on every shared triple

**Setting.** Active NORI concerns actual physical ordered three-faces of Q_n, n>=5, colored in F2 with c(bar F,rev pi)=1+c(F,pi) mod2. Take a finite or arbitrary family of local charts indexed by i, each consisting of a direction support S_i⊆[n], |S_i|>=3, a distinguished **sentinel** t_i∈[n]\S_i, and an arbitrary function h_i on all ordered triples of DISTINCT directions in S_i. The chart requires that at EVERY physical hub z and every ordered triple pi∈S_i,

    c(F_z(supp pi),pi) =
       h_i(pi)                if z_(t_i)=0,
       1+h_i(rev pi)          if z_(t_i)=1,   (F2).

This is an ACTUAL face-local formula: each t_i is outside the free triple, so its bit is a constant exterior face bit. Each individual chart already respects the physical antipodal-reversal law.

**THEOREM (necessary and sufficient atlas compatibility).** These local chart formulas extend simultaneously to ONE genuine global active NORI physical coloring if and only if, for every ordered triple pi belonging to at least two chart supports, the following hold:

(A) **Same orientation agreement.** All charts containing pi assign the SAME base value h_i(pi), denoted h(pi).

(B) **Distinct-sentinel reversal constraint.** If the set of sentinels {t_i : supp(pi)⊆S_i} has cardinality >=2, then the common base function is REVERSAL ODD on that triple:
         h(pi)+h(rev pi)=1 in F2.

No other condition involving chart-intersection cycles or higher-dimensional faces is necessary for mere face-COLOR assignment.

**Necessity.** Let i,j both contain pi and choose an actual physical three-face F with supp pi as free directions. Both t_i,t_j are exterior. If t_i=t_j, take its exterior bit zero, so the single physical face color gives h_i(pi)=h_j(pi), for every pi. If t_i!=t_j, the two exterior bits are INDEPENDENTLY assignable (because the free face fixes both); varying the four possibilities (0,0),(0,1),(1,0),(1,1) yields

     h_i(pi)=h_j(pi)=1+h_i(rev pi)=1+h_j(rev pi).

Thus same-orientation agreement AND h_i(pi)+h_i(rev pi)=1. Repeating for all intersecting charts gives (A),(B). This argument uses literal physical faces, not imaginary based windows.

**Sufficiency.** For a fixed unordered direction triple T covered by at least one chart, (A) gives a unique base h(pi) for every orientation pi of T, including rev pi. If all charts containing T use ONE common sentinel t, assign c(F,pi)=h(pi) for exterior t-bit0 and 1+h(rev pi) for t-bit1. This simultaneously realizes all such charts and is NORI reversal-odd by flipping t under antipodality. If the charts containing T have TWO OR MORE distinct sentinels, (B) gives h(rev pi)=1+h(pi), so EVERY chart formula simplifies to c(F,pi)=h(pi) INDEPENDENTLY OF ALL EXTERIOR FACE BITS. This is again active reversal odd, since c(bar F,rev pi)=h(rev pi)=1+h(pi). Different unordered triples T occupy disjoint antipodal-reversal orbits and impose no cross-T assignment constraints. Complete all uncovered triple supports by arbitrary choices on each remaining antipodal-reversal orbit. This constructs the claimed global coloring. QED.

**COROLLARY (exact sentinel-diversity rigidity).** Suppose a chart (S,t) with |S|>=6 is accompanied by other charts such that EVERY unordered triple T⊂S is also contained in a chart whose sentinel differs from t. If all charts simultaneously realize their stipulated exterior-sentinel normal forms on genuine physical cube faces, then h_S is reversal odd on ALL ordered triples of S. In particular, choose any 6-element subset V⊂S. The team's proved six-direction monochromatic-facet theorem (Item nori_six_direction_monochromatic_facet_transfer_20261008) yields a FIVE-DIRECTION ORDER in V whose three ordered-window colors are ALL IDENTICAL. This is an actual monochromatic physical five-edge geodesic at EVERY starting root because the chart becomes independent of exterior face bits on those six directions.

Within any such 6-element V, the prior cyclic pentagon count now forces at least 52 of 120 five-direction orders to be <=1-switch from EVERY root: baseline48, plus 4 guaranteed by the rich cyclic class and its distinct reversed partner. Therefore a fully saturated 2/5 local five-path density on V is IMPOSSIBLE in a sentinel-diverse complete triple cover.

**Interpretation and exact frontier.** One common sentinel allows arbitrary locally sharp five-window profiles across complicated overlap complexes, as proved by Item nori_common_sentinel_exact_local_ordered_face_atlas_gluing_20261009; no higher face-color gluing obstruction exists there. The present theorem identifies a genuine PHYSICAL obstruction when distinct sentinels occur on overlapping triple supports: the same fixed exterior face must obey two independent Boolean coordinate descriptions, and consequently the color loses all exterior dependence on the shared triple and becomes reversal odd. If sentinel diversity covers every triple of a 6-support, it forces a genuinely monochromatic five-geodesic and strict local surplus.

This is a dimension-independent forcing lemma for a PRECISE SENTINEL-NORMAL-FORM SUBCLASS. An arbitrary active NORI coloring need NOT admit such charts (its three-face exterior dependence may involve arbitrarily many bits), so this does not close the unrestricted grand conjecture. A topological proof would need to extract these normal-form charts, or a more flexible finite-memory analogue, from arbitrary actual physical reachability/terminal-two-tail data without assuming them.
