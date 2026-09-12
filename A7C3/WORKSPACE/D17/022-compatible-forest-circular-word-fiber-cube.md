# A fixed circular-word SLIDE sheet is a three-cut cube or already reaches a portal

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-circular-word-fiber-cube`

**Summary:** Fix persistent ancestry labels on the three rails of a maximum spanning three-forest and choose one cyclic rail order. Their concatenation is an oriented circular physical word W. A forest on this same sheet is exactly three cut gaps of W covering every cyclic center whose consecutive triple is bad. For a nonsingleton cut, its two merge seams are the two cyclic turn bits at the endpoints of that gap: 11 gives a spanning two-cover, 00 is exactly the SV22098 DOUBLE portal, and 10/01 is the unique reversible SLIDE, which simply pivots the cut across its unique bad endpoint while leaving W fixed. A singleton rail is itself an immediate two-cover or R3/R4 trimer exit. Therefore, in a W-horizontal closure avoiding two-cover, trimer, and DOUBLE, each of the three cuts covers exactly one bad center and every bad center is covered; singleton exclusion forces exactly three bad centers. Adjacent bad centers yield a reachable DOUBLE, and distance-two bad centers yield a reachable singleton exit. Otherwise the three bad centers are separated and each independently chooses its left or right incident cut gap, so the entire W-horizontal fiber is literally the 3-cube Q_3. Filling its commuting square faces makes the fiber contractible. Hence no nontrivial square-coherent history can live inside one fixed ancestry-oriented circular-word SLIDE sheet: genuine holonomy must switch the two circular sheets or traverse an already named portal.

### 1. Framed circular-word sheets
Let H be a hypothetical smallest counterexample and let

  F=A|B|C

be a literal maximum spanning three-forest. Give the three rails persistent ancestry labels A,B,C and choose one of their two cyclic orders. Concatenating the three literal path words in that cyclic order gives one oriented circular word

  W=(w_0,w_1,...,w_{n-1})                               (CW.1)

read modulo cyclic rotation. Call this choice a CIRCULAR-WORD SHEET.

A W-STATE is a literal maximum three-forest whose three ancestry-labelled rails occur as the three nonempty arcs obtained by cutting this same physical circular word W at three labelled gaps, in the chosen cyclic rail order. Thus changing a cut may move physical vertices from one ancestral rail to the next, but the circular physical word W itself is fixed.

For every cyclic center i put

  c_i=1  iff  (w_{i-1},w_i,w_{i+1}) is tight,
  c_i=0  otherwise,                                      (CW.2)

and let D(W)={i:c_i=0}. These bits are graph-intrinsic and do not change anywhere in the W-sheet.

### 2. W-states are exactly three-cut covers of the bad centers
Let e_i be the gap between w_i and w_{i+1}. A cyclic center w_i is internal to one of the three path arcs exactly when neither e_{i-1} nor e_i is a cut. Therefore the three arcs are all tight exactly when

  for every i in D(W), at least one of e_{i-1},e_i is a cut.    (CW.3)

Equivalently, regarding the gaps e_i as the edges of the cycle C_n on the cyclic positions, the three cuts form a three-edge cover of the bad-center set D(W).

This is a literal representation, not an analogy: a framed W-state is precisely a set of three distinct labelled cut gaps satisfying (CW.3), with the cuts occurring in the prescribed cyclic rail order.

### 3. A sheet-preserving SLIDE is one cut pivot around one bad center
Assume first that the two rails incident with a cut e_i both have order at least two. The two physical merge seams across that cut are exactly

  (w_{i-1},w_i,w_{i+1})  and
  (w_i,w_{i+1},w_{i+2}),                                 (CW.4)

so their tightness bits are c_i,c_{i+1}.

If c_i=c_{i+1}=1, deleting the cut merges those two arcs into one tight path and gives a spanning two-cover.

If c_i=c_{i+1}=0, the physical merge has two bad holes and is exactly the DOUBLE branch of SV22098, retaining its reverse-P4 restoration portal.

If (c_i,c_{i+1})=(1,0), SV22098 gives the unique SLIDE which transfers the source w_{i+1} across the cut. On W this simply replaces cut e_i by e_{i+1}. Dually, pattern (0,1) replaces e_i by e_{i-1}. Hence every sheet-preserving SLIDE is exactly the pivot

  one incident edge of a bad center  <->  its other incident edge.   (CW.5)

The circular word W is literally unchanged.

### 4. Singleton rails are already exits
If one rail is the singleton {x}, attempt to merge it with either neighbouring non-singleton rail in the chosen sheet. There is only one physical seam turn. If it is tight, the singleton merges and H has a spanning two-cover. If it is bad, R3 gives the reverse tight trimer on the same three physical vertices; in the present large-counterexample setting it is proper, and R4 currentizes it with an exact two-covered complement.

If two rails are singletons, joining the two singleton vertices makes a dimer and immediately gives a spanning two-cover.

Thus a W-horizontal class which avoids TWO-COVER and CURRENT TRIMER exits contains no singleton rail. In particular all seam bits in Section 3 are genuine physical merge seams throughout such a class.

### 5. Portal-free W-sheets have exactly three bad centers
Now suppose the W-horizontal SLIDE closure under consideration reaches none of

  TWO-COVER,
  CURRENT TRIMER,
  DOUBLE.                                                 (CW.6)

At every cut e_i, Section 3 then forbids both endpoint bits 11 and 00. Hence each of the three cut edges has exactly one bad endpoint.

By (CW.3), every bad center is incident with at least one cut. The three cuts therefore contribute exactly three cut-bad incidences and cover all of D(W), so |D(W)|<=3.

On the other hand |D(W)| cannot be 0 or 1, since then some cut would have no bad endpoint and would be a 11 two-cover cut. It cannot be 2 either: three cut-bad incidences covering only two bad centers force one bad center to be incident with both of its cut gaps, making that physical vertex a singleton rail, contrary to Section 4. Therefore

  |D(W)|=3,                                               (CW.7)

and each cut is incident with a distinct bad center.

### 6. Nearby bad centers force an exit; otherwise the whole fiber is Q_3
Let the three bad centers be d_1,d_2,d_3 around W.

If two bad centers are cyclically adjacent, pivoting the cut which covers either one toward their common gap reaches a cut whose two endpoint seam bits are 00. This is a DOUBLE portal.

If two bad centers are at cyclic distance two, independently pivoting their covering cuts toward the unique center between them reaches two adjacent cut gaps. The intervening physical vertex is then a singleton rail, so Section 4 gives a two-cover or current trimer exit.

Consequently, if the entire W-horizontal closure remains inside the portal-free sector (CW.6), the three bad centers have pairwise cyclic distance at least three. Their two incident gap-pairs are then disjoint and no choice of one incident gap at each bad center creates adjacent cuts.

Every bad center therefore supplies one independent binary choice of which incident gap carries its labelled cut. By (CW.5) toggling that choice is exactly one reversible sheet-preserving SLIDE. Hence the full W-horizontal closure is literally

  {left,right}^{ {d_1,d_2,d_3} } = Q_3.                  (CW.8)

The six square faces are the commuting cut-pivot relations. After filling those verified square faces, the W-fiber is a 3-cube and is contractible. In particular it supports no nontrivial history-bearing holonomy for any transport mark which is coherent on the elementary cut-pivot squares.

### 7. Moonshot consequence: holonomy must change sheet or use a portal
Thus a maximum-three-forest recurrence cannot hide arbitrarily complicated topology inside one ancestry-oriented circular-word SLIDE sheet. Starting from any framed forest and holding its circular word W fixed, either horizontal SLIDE motion reaches a two-cover, a current trimer, or a DOUBLE reverse-P4 portal, or the entire horizontal fiber is the explicit cube (CW.8).

Accordingly, after the one-edge token-flatness SV39182, the remaining G15 monodromy target sharpens again: any genuinely nontrivial closed transport must either

  (i) SWITCH between the two circular concatenation sheets of the three ancestral rails, or
  (ii) traverse a named non-SLIDE portal (trimer, DOUBLE, proper-cycle/rebreak, component recompletion, or another genuinely non-one-edge transition).   (CW.9)

This identifies sheet-switching, rather than square coherence inside one sheet, as the first new global curvature candidate. No claim is made here that sheet-switching is itself impossible or that Arm-M Hall deficiency already forces a nonzero sheet-switch class.
