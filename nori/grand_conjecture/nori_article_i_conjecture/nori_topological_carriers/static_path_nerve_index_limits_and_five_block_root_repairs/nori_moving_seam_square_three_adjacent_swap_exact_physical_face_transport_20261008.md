# Moving-seam permutohedral adjacent swaps preserve both or one literal crossing ordered three-face(s)

# Moving-seam cubical transport through central permutohedral adjacent swaps: both genuine face objects preserved by the crossing swap

Let n>=6 and let c be ANY binary coloring of physical ordered three-faces on Q_n. Take a full rooted cube-geodesic direction order p=(p1,...,pn), choose any cut rank ell with 2<=ell<=n−2, and denote four consecutive direction names
  c0=p_(ell−1), a=p_ell, b=p_(ell+1), d=p_(ell+2),
which are pairwise distinct. Let S be the first ell used directions and y=x XOR S the true physical cut vertex of the path from root x. Its TWO actual crossing three-face window objects are
  L=(F(y;{c0,a,b}),(c0,a,b)),
  R=(F(y;{a,b,d}),(a,b,d)).
The two underlying physical faces are flat across the root square spanned by a,b.

**THEOREM 1 (cross-cut central transposition preserves BOTH physical seam face objects).** Let p' be obtained from p by interchanging only the adjacent positions ell,ell+1, replacing (c0,a | b,d) by (c0,b | a,d). The NEW used prefix set is S'=S symmetric-difference {a,b}, so the new cut vertex is y'=y XOR a XOR b, the OPPOSITE corner of the physical seam square. Its two crossing ordered face windows are
  L'=(F(y';{c0,b,a}),(c0,b,a)),
  R'=(F(y';{b,a,d}),(b,a,d)).
Since a,b are free directions of BOTH old physical faces,
  F(y';{c0,a,b})=F(y;{c0,a,b}),
  F(y';{a,b,d})=F(y;{a,b,d}).
Thus the old/new pairs L,L' are DIFFERENT ORIENTATIONS of exactly the SAME actual physical three-face, and likewise R,R' are different orientations of exactly the SAME actual second physical three-face. The four actual seam-window colors are
  c(F_L,(c0,a,b)), c(F_L,(c0,b,a)),
  c(F_R,(a,b,d)),  c(F_R,(b,a,d)),
with two fixed physical faces F_L,F_R. Every one of these four values remains unchanged when the STARTING ROOT is independently flipped in a, b, or both. This gives a literal 2-by-4 physically grounded seam-color table, unlike an interpolated Tucker label.

**THEOREM 2 (adjacent moves on either side transport one physical seam face).**
(a) Swap the two last directions of the prefix, positions ell−1,ell: (c0,a | b,d) becomes (a,c0 | b,d). The cut USED support S and physical cut vertex y do not change. The new LEFT crossing window has triple (a,c0,b) and uses the SAME underlying physical face F_L=F(y;{c0,a,b}), while the new RIGHT window has triple (c0,b,d) on a generally different physical face. The seam-square axes change from {a,b} to {c0,b}, two squares sharing direction b.
(b) Swap the first two suffix directions, positions ell+1,ell+2: (c0,a | b,d) becomes (c0,a | d,b). The cut support and y again do not change. The new RIGHT crossing window has triple (a,d,b) on the SAME underlying physical face F_R=F(y;{a,b,d}), while the new LEFT window has triple (c0,a,d) on a generally different face. The seam-square axes change from {a,b} to {a,d}, two squares sharing direction a.

**PROOF.** For Theorem1 the transposition crosses the cut, so S' replaces a by b, changing the cut vertex by a XOR b. Each crossing face's free triple includes both a and b, so changing the reference vertex y on those two coordinates leaves the physical face literally unchanged. The ordered triples transform exactly as stated. Flipping starting root in any subset of {a,b} changes the cut vertex only on the same free directions, establishing the four-root square invariance. For Theorem2 the transpositions lie wholly inside S or its complement, so the cut endpoint y is unchanged. The left seam free 3-set {c0,a,b} is unchanged by the left transposition, and the right free set {a,b,d} is unchanged by the right transposition, whereas the other seam free set generally changes. The resulting direction words determine the displayed orientations. QED.

**PHYSICAL ORDER-EXCHANGE FRAMEWORK.** These three elementary adjacent permutation moves give genuine transport rules for a root-coupled moving seam-square label:
- crossing swap: the physical root cut moves by a XOR b, the pair {a,b} stays fixed, and BOTH physical seam faces are preserved;
- left-neighbor swap: cut root fixed, seam pair changes {a,b}->{c0,b}, LEFT physical face preserved;
- right-neighbor swap: cut root fixed, seam pair changes {a,b}->{a,d}, RIGHT physical face preserved.

The central root-square label pair {a,b} cannot be fixed globally without killing antipodal index, by Item nori_fixed_pair_separating_permutohedron_facets_antipodal_index_zero_square_alignment_nogo_20261008. The present theorem identifies the precise COLOR-INDEPENDENT GEOMETRIC transport operations for a MOVING pair, requiring only genuine physical faces and adjacent-coordinate exchanges. Color memory remains attached to these actual ordered faces. These operations are promising 1-cells for an enriched equivariant root-square / permutohedral repair complex.

**LIMITATION.** The active NORI antipodal-reversal law relates colors on antipodal faces with reversed entire direction triples; it does NOT relate two different orders of the SAME physical face. Thus the four crossing-swap seam bits above can be arbitrarily assigned locally, and none of the three elementary moves is automatically defect-decreasing. The missing forcing step is a parity/holonomy or fixed-point principle applied to the WHOLE system of these actual ordered-face transport moves, using all-root antipodal compatibility and genuine path-window color incidence. This theorem is a rigorous geometric toolkit item, NOT an unrestricted grand proof.
