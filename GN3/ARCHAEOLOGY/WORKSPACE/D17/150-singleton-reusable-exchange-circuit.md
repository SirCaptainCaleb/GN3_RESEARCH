# Reusable exchange circuits reduce to an endpoint-role-locked odd two-sheet circuit

**Workspace:** D17
**State:** established
**Key:** `singleton-reusable-exchange-circuit`

**Summary:** Open repair chains reduce to an odd two-sheet support orbit. Fully order-quiet circuits of physical length at least five are impossible by the two-step endpoint-role recurrence; the only quiet survivor has three physical labels and paired HHH/TTT common-core form. Corrected integration contract: R926 consumes only an induced distinct-label compatibility circuit (apart from its spanning odd exception); opposite-sheet trims create exact same-residue component drops whose selected cross-states pass through R176/P540 before any payment. In HHH the cross-state birth is already an ancestry-bearing both-singleton floor; in TTT R428 legitimately pays the nontrivial side while preserving the pivot. After R432 steering, the original T_U,T_V covers remain separately available exact targets; each physical pivot gives an internal-middle R442 interface in one cover and the current R919/P992 endpoint-return interface in the other, including core order two. Thus the three-label residue is a same-residue doubled fixed-turn discrepancy source, not a new terminal packet.

### 1. Open repair chains are re-realizable
Retain a hypothetical smallest counterexample and a complete chosen singleton-deletion cover family. Use the exact support partitions and deleted-label substitution notation of `codimension-one-coherence`.

Fix distinct deletion labels a_0,...,a_t and freeze the current actual row at a_t. Work backward for i=t-1,...,0. Once the row at a_{i+1} has been finalized, compare the current actual row at a_i with that ACTUAL source row. There are exactly three possibilities supplied by `codimension-one-coherence`.

(1) kappa(a_i<-a_{i+1})=0. Then the two rows are already overlap-compatible; keep the a_i row.

(2) The a_i row selects a direct adjacency between the two source-rail supports of the a_{i+1} row away from the exchanged labels. Retain this literal source-rail crossing as a current defect exit.

(3) No such direct source-rail crossing occurs. Then the positive defect is the R511 unique-transition bridge cell, and the seam-free repair gives an ACTUAL exact replacement of the a_i row with support partition equal to the deleted-label transport of the finalized a_{i+1} support partition. Hence a_i and a_{i+1} become compatible.

Changing row a_i does not alter any already-finalized row a_j with j>i. Therefore, unless a direct crossing is emitted, after the backward pass the compatibility graph of the resulting actual family contains the whole path
  a_0-a_1-...-a_t.
No assumption that the original repair candidates remain valid after upstream rows change is needed: each comparison is rerun against the then-current actual source row. This is the exact open-chain reusability statement.

### 2. One support copy acts on every third-row target by a transposition
Now isolate one seam-free support transport a<-b. Let sigma_b be the source partition on V-b and let
  sigma_prime_a=T_{a<-b}(sigma_b)
be the transported partition on V-a: the source label a is removed from its sigma_b block and b is inserted in that same block. Fix a third deletion label c distinct from a,b.

Let tau_{c<-b}(sigma_b) be the old target partition on V-c, and let tau_prime_{c<-a}(sigma_prime_a) be the target induced by the transported row. Then tau_prime_{c<-a}(sigma_prime_a) is obtained from tau_{c<-b}(sigma_b) by transposing the physical labels a and b and changing no other block membership.

Proof. Orient the two blocks of sigma_b temporarily and write s(v) for the block bit. The old target has a in block s(a) and b in block s(c). The transported source sigma_prime_a has b in block s(a), while c retains s(c); after forming the c<-a target, a is inserted in block s(c). Thus the new target exchanges exactly the old block values of a and b. The statement is independent of the temporary orientation.

Consequently, for the fixed selected-edge forest E(C_c) of the unchanged c-row,
  kappa_new(c<-a)-kappa_old(c<-b)
is exactly the change in cut size when the two vertices a,b are transposed across the old target cut. Call this local correction
  delta_c(a,b; tau_{c<-b}).
Only selected adjacencies incident with exactly one of a,b can contribute. In particular the correction is completely local to the two circuit labels; since C_c is a two-path cover, its absolute value is at most deg_{C_c}(a)+deg_{C_c}(b)<=4. No claim on its sign is made.

### 3. Cyclic incoming collateral telescopes
Let I={a_0,...,a_{t-1}} and suppose one simultaneously installs actual transported supports
  sigma_prime_{a_i}=T_{a_i<-a_{i+1}}(sigma_{a_{i+1}})
with indices modulo t. These replacements are individually realizable support choices; this subsection only computes the incoming comparisons from rows c outside I.

For each unchanged c notin I, the transposition identity gives
  sum_i kappa_new(c<-a_i)
   = sum_i kappa_old(c<-a_{i+1})
     + sum_i delta_c(a_i,a_{i+1}; tau_{c<-a_{i+1}}).
The first sum is just a cyclic permutation of the old source indices, hence
  sum_i [kappa_new(c<-a_i)-kappa_old(c<-a_i)]
   = sum_i delta_c(a_i,a_{i+1}; tau_{c<-a_{i+1}}).
Thus a closed support transport has no diffuse incoming collateral from an unchanged row: after the source-index permutation cancels, every residual term is supported on selected incidences of C_c at adjacent circuit labels. Summing over c outside I gives the exact external incoming-cut contribution to the multirow ledger. Outgoing row costs and comparisons internal to I remain separate and must still be evaluated/reoptimized as in `singleton-multirow-energy-ledger`; this identity does not assert total-K descent.

### 4. If an induced closing circuit persists, support topology already consumes it
Suppose distinct repair labels a_0,...,a_{m-1}, with m>=4, are simultaneously realized in one actual singleton-cover family so that on these labels the compatibility graph is exactly the induced cycle
  a_0-a_1-...-a_{m-1}-a_0.
Accepted R926 applies to that final family. Its precise forbidden-cycle corollary is for an INDUCED compatibility cycle of length at least four: under pc(H)>2 such a cycle can only be the unique odd cycle containing every physical vertex. Therefore a simultaneously realized induced repair circuit that is even, or that omits even one physical vertex, already yields a spanning two-cover through R926.

The inducedness hypothesis is essential. In the forest-root alternative G=L(R), several root edges may meet one port and form a compatibility clique, so a non-induced simple cycle in G can occur with chords and is not ruled out by R926. No triangle in G is forbidden either. Thus Section 5 correctly keeps the sharper object: an induced compatibility path on distinct physical labels with one missing closing edge. The support-level obstruction is CLOSING-EDGE PERSISTENCE for that induced path: after re-realizing all but one obligation, can the last compatibility be created without destroying an earlier one?

### 5. A seam-free closing slide either rotates an odd gap or folds and shortens an even one
Start from one actual family whose compatibility graph contains an induced path
  a_0-a_1-...-a_{m-1}
with m>=3 distinct labels, and suppose a_0 and a_{m-1} are not compatible. Compare the current a_0 row against the actual source row C_{a_{m-1}}. Assume no direct source-rail crossing occurs, so the R511 seam-free repair replaces the a_0 row by the deleted-label transport of the a_{m-1} support partition.

Temporarily orient the unordered two-block partitions along the OPEN compatible path. Choose an orientation of the a_0 row arbitrarily, then orient each successive row so that it agrees with its predecessor on their common residue. For every internal circuit label a_j, 1<=j<=m-2, its block bit is constant in rows before a_j and constant in rows after a_j; call these values L_j and R_j. Inducedness forces
  R_j=1-L_j.
Indeed, if L_j=R_j then the distance-two rows a_{j-1} and a_{j+1} agree on their whole common residue and would be compatible, contradicting that the displayed path is induced.

Write R_0 for the bit of a_0 in all rows after a_0, and L_{m-1} for the bit of a_{m-1} in all rows before a_{m-1}. The R926 rail-incidence root of the induced path is a simple root path. Coloring its ports by membership of the physical label a_0 gives the exact endpoint parity
  R_0=L_{m-1}          when m is even,
  R_0=1-L_{m-1}        when m is odd.
This is the valid part of the former port-coloring audit; no triangle in the compatibility graph is forbidden.

Let sigma'_0 be the transported support partition after the seam-free closing copy. Every internal a_j now has bit R_j instead of L_j, while the inserted label a_{m-1} has bit R_0. Comparing sigma'_0 with the unchanged old path rows gives an exact compatibility list.

If m is ODD, sigma'_0 is compatible among the displayed path labels only with a_{m-1}. For every 1<=j<=m-2, the common residue of sigma'_0 and sigma_j still contains a_{m-1}, on which they have opposite bits; for earlier j there are further mismatches a_{j+1},...,a_{m-2}. Thus the old edge a_0-a_1 is lost and the missing closing gap has simply rotated:
  a_1-a_2-...-a_{m-1}-a_0
is again an induced compatibility path.

If m is EVEN, sigma'_0 is compatible among the displayed path labels exactly with a_{m-2} and a_{m-1}. For sigma_j with j<=m-3, the common residue still contains at least a_{j+1},...,a_{m-2} with opposite bits, while for j=m-2 or m-1 no mismatch survives. Hence the old edge a_0-a_1 is lost, the labels a_0,a_{m-2},a_{m-1} form a LEGAL compatibility triangle corresponding to a folded root port, and
  a_1-a_2-...-a_{m-2}-a_0
is an induced compatibility path on only m-1 labels.

Therefore an inclusion-minimal pure seam-free closing dependency cannot have even cardinality: an even closing slide strictly shortens it. The minimal pure survivor is odd, where a seam-free slide moves the unique support gap without shortening. This replaces the invalid DR17.141 claim that a compatibility triangle itself was contradictory. The even branch is a PORT-FOLD / DEFECT-SLIDE, not closure.

### 6. Hall comparison: exact reusability exists there
Accepted R946 supplies the model reusability property on the uniform-middle-layer endpoint-Hall side. For one minimal Hall circuit, choose one common base matching M of F-{S} onto N. Every actual endpoint incidence S-R_i is currentized by replacing one matched edge T_i-R_i with S-R_i, and any pair of rooted matchings differs on the exact alternating path
  T_i-R_i-S-R_j-T_j.
Thus deleting one Hall obligation leaves all remaining obligations simultaneously represented relative to one common base matching M. This is precisely what the singleton K-support circuit does not yet possess on odd closing circuits.

The parent theorem suggested by these two systems is therefore a reusable cover-exchange circuit theorem: either a closed support-repair dependency set admits a common realization in which the intended distinct-label compatibility circuit is induced (so the exact R926 forbidden-cycle corollary consumes it unless it is the spanning odd exception), or failure of such an induced common realization produces a direct labelled defect/escape that strictly enlarges or reroutes the dependency set. The present section proves open-chain realization, cyclic incoming telescoping, and the exact parity of a seam-free closing slide: an even slide folds a root port and strictly shortens an inclusion-minimal dependency, while an odd slide rotates the support gap. It does not yet consume the resulting odd orbit or prove the final circuit-absorption theorem.

### 7. Odd seam-free closing has exact period-two support monodromy
Retain the induced compatibility path
  a_0-a_1-...-a_{m-1}
from Section 5, now with m odd, and suppose the circuit label set I={a_0,...,a_{m-1}} is proper in V(H). Choose one outside physical label c in V(H)-I. Orient every two-block support partition of the path rows by declaring the block containing c to have bit 0. Because consecutive compatible rows agree on their common residue and c survives every circuit row, this orientation is coherent along the whole path.

For each internal circuit label a_j, 1<=j<=m-2, its block bit is constant in rows a_0,...,a_{j-1} and constant in rows a_{j+1},...,a_{m-1}. Call these values L_j and R_j. They are opposite. Indeed the two distance-two rows a_{j-1} and a_{j+1} already agree on every common vertex except possibly a_j; if L_j=R_j they would be compatible, contradicting inducedness. Thus
  R_j=1-L_j.                                           (7.1)
The endpoint labels have analogous single-side values: write R_0 for the bit of a_0 in rows a_1,...,a_{m-1}, and L_{m-1} for the bit of a_{m-1} in rows a_0,...,a_{m-2}. The R926 port coloring used in Section 5 gives, for odd m,
  R_0=1-L_{m-1}.                                       (7.2)

Now perform the seam-free closing copy a_0<-a_{m-1}. For every internal a_j the repaired row a_0 inherits the a_{m-1} bit R_j, whereas the old a_0 row had L_j, so every internal circuit label flips by (7.1). The inserted label a_{m-1} receives the old source bit of a_0, namely R_0, which is the opposite of its old a_0-row bit L_{m-1} by (7.2). Every label outside I keeps its source-row bit. Therefore the repaired row a_0 is obtained from the old row a_0 by flipping the block membership of every surviving circuit label and fixing every outside label.

The same statement propagates around the gap. After the first slide the induced compatibility path is
  a_1-a_2-...-a_{m-1}-a_0
unless H already closes or a direct crossing is emitted. Suppose rows a_0',...,a_{i-1}' have been updated in sequence and each updated row equals its original support partition with every surviving I-label flipped and every outside label fixed. The next seam-free copy a_i<-a_{i-1} inherits all common vertices from a_{i-1}'. For any v outside {a_i,a_{i-1}}, compatibility of the original rows a_{i-1},a_i says their old bits agree, so v is again flipped exactly when v lies in I and fixed otherwise. For the inserted label a_{i-1}, the forced deleted-label placement on the original compatibility edge gives
  bit_{a_i}(a_{i-1}) = bit_{a_{i-1}}(a_i).
The updated source has the opposite bit on a_i, so the inserted a_{i-1} also flips. Induction completes one full gap rotation.

Hence after m successive seam-free closing slides, one at each newly exposed gap, every circuit row has undergone the SAME involution:
  every surviving label of I changes block,
  every label outside I stays in its old block.          (7.3)
Call the resulting support family Sigma^*. Repeating the same odd gap rotation a second time applies the involution again and returns exactly to the original support family Sigma. Thus pure odd support transport is not an unbounded collateral process; it is a period-two support orbit.

If I=V(H), there is no outside anchor. In that case (7.3) flips every surviving vertex in every row, which is merely a global exchange of the two UNORDERED blocks. Therefore Sigma^*=Sigma after one rotation. This is exactly the spanning odd-cycle monodromy exception in accepted R926. For proper I the outside anchor c prevents the flip from being a block swap, so Sigma^* is genuinely distinct from Sigma and the second rotation is necessary.

This identifies the remaining parent obstruction more sharply. A minimal pure R511 collateral circuit is an odd gap-transport orbit of length at most 2|I| at the support level. Scalar K need not decrease on one slide: the three-label fixed-hub HHH/TTT transport is the smallest neutral example. Any successful global theorem must now consume endpoint roles, path orders, or the exact cut-transposition ledger over this finite period-two orbit, rather than control arbitrary collateral propagation.

### 8. Two rotations currentize one circuit endpoint in every original support fiber
The period-two statement records only support partitions, but the actual R511 repair retains more. In the unique-transition bridge normal form for a seam-free copy a<-b, the replacement rail on the transported side is the contiguous source-side block followed by b (or its reversal). Hence the inserted source deletion label b is a PHYSICAL ENDPOINT of that Hamilton replacement rail.

During one odd gap rotation every row a_i is replaced once from its predecessor a_{i-1} in the cyclic order (indices modulo m). Therefore the first-sheet cover C_i^1 on the toggled support state exposes a_{i-1} as a physical endpoint. During the second rotation the row a_i is again replaced from a_{i-1}; Section 7 says its support partition has now returned exactly to the original state sigma_i^0. Thus there is an ACTUAL exact two-cover \hat C_i^0 of H-a_i with the original support partition sigma_i^0 in which a_{i-1} is a physical endpoint.

Consequently both support sheets may be represented by actual covers C_i^0,C_i^1 in which the predecessor a_{i-1} is an endpoint. If one wishes to retain the original pre-orbit representative as well and it had a_{i-1} internal, accepted R408 applies to the two exact covers of the same proper residue H-a_i and gives its graph-intrinsic balanced-pair output. The stronger reusable-circuit analysis may therefore continue after reselecting the endpoint-currentized representative without changing the support state.

### 9. The two support sheets form one exact even compatibility cycle
For each i let sigma_i^0 be the original support state and sigma_i^1 the state after one full odd gap rotation. Thus sigma_i^1 is obtained from sigma_i^0 by flipping every surviving label of I and fixing every outside label, under the outside-anchor orientation of Section 7.

The compatibility relation among these 2m actual support alternatives is exact. For i<j, the original rows sigma_i^0 and sigma_j^0 differ, on their common residue, exactly at the circuit labels a_k with i<k<j and nowhere outside I. This follows directly from the one-jump description (7.1): labels before i are seen on their R side by both rows, labels after j on their L side by both rows, and precisely the labels strictly between i and j are seen on opposite sides.

Hence two SAME-SHEET alternatives sigma_i^epsilon,sigma_j^epsilon are compatible exactly when j=i+1, because the original path is induced. Two OPPOSITE-SHEET alternatives flip every surviving I-label on one side, so they are compatible exactly when the original rows disagreed at every surviving I-label. That happens only for the endpoint pair {i,j}={0,m-1}. Therefore the full alternative-state compatibility graph on
  {a_i^0,a_i^1 : 0<=i<m}
is the single even cycle
  a_0^0-a_1^0-...-a_{m-1}^0-a_0^1-a_1^1-...-a_{m-1}^1-a_0^0.     (9.1)
Every vertex of this state cycle is an ACTUAL singleton-deletion cover choice, not a formal partition.

This is the precise K-side analogue of a reusable Hall circuit, with one important twist: each physical deletion label occurs twice. Selecting one state for each physical label is a Z_2-frustrated transversal. Along the path edges compatibility requires equal sheet bits, while the closing physical pair requires opposite sheet bits. No one-state-per-label selection realizes the whole cycle; changing the sheet choice merely moves the unique support-level gap. The period-two monodromy is therefore a literal two-sheet compatibility lift rather than indefinite collateral propagation.

### 10. Outside component-drop, the two-sheet circuit is endpoint-current; opposite-role states admit R933 and same-role states are rigid
Retain the endpoint-currentized representatives from Section 8. Fix one state-cycle vertex a_i^epsilon. Its predecessor in the state cycle has physical label a_{i-1}, and a_{i-1} is already a physical endpoint of C_i^epsilon.

Consider the state-cycle compatibility edge from a_i^epsilon to the successor state with physical label a_{i+1}. The successor cover has a_i as its predecessor endpoint. Deleting that endpoint from the successor cover therefore leaves a literal exact two-cover of
  W=H-{a_i,a_{i+1}}.
If a_{i+1} were internal in C_i^epsilon, deleting it from C_i^epsilon would split its rail and give a literal three-cover of the SAME proper residue W. Accepted R159, equivalently the R408 endpoint/internal comparison mechanism, then gives a graph-intrinsic balanced opposite-sign pair. Thus outside this explicit component-drop output, a_{i+1} is also a physical endpoint of C_i^epsilon.

Moreover a_{i-1} and a_{i+1} lie on OPPOSITE rails of C_i^epsilon. Choose one complete singleton family containing the three actual state alternatives from the two incident edges of (9.1), and arbitrary actual states for the remaining deletion labels. Both neighbors are compatible with a_i in that family, while the two neighbor states are not compatible because (9.1) has no triangle. In the R926 rail-incidence root, the two neighbor root edges therefore meet the two different ports of the center edge e_{a_i}; these ports are exactly the two rail supports of C_i^epsilon.

Now retain the SOURCE/TERMINAL role of each neighbor endpoint on its own rail. This is distinct from the preceding opposite-RAIL conclusion.

If the two neighbor endpoints have OPPOSITE roles, one is a source and the other a terminal. Put x=a_{i-1}, y=a_{i+1}, z=a_i. There is then exactly one role-correct Hamilton order on the singleton absorber {z} with endpoints x,y: it runs from the terminal endpoint through z to the source endpoint. This is one of the reversal pair
  (x,z,y), (y,z,x).
If that role-correct orientation is tight, accepted R933 applies with X={z}; because pc(H)>2, both residual attachment seams exist and both are bad, so both exact reversed attachment turns are simultaneously tight. If the role-correct orientation is bad, R3 supplies its exact reverse middle-z connector as a labelled tight trimer.

If instead the two neighbor endpoints have the SAME role, both sources or both terminals, R933 is NOT applicable to these two endpoints: a single Hamilton absorber path cannot simultaneously attach to two residual rails on the same side. Retain this as a SAME-ROLE RIGID state. No connector absorption is claimed from R933 in this branch.

Finally compare the two sheets for one physical deletion label a_i. If either sheet is same-role, the physical label already lies in the same-role rigid residue. Suppose BOTH sheets are opposite-role and both avoid the R933 branch. The graph-intrinsic tight orientation among (x,z,y),(y,z,x) is the same on both sheets. Each sheet's role-correct orientation must therefore be the unique bad one. Hence the two sheets require the SAME role-correct orientation: the same neighbor is terminal and the same neighbor is source on both sheets. Equivalently, the ordered endpoint-role pair agrees sheet-to-sheet, and R3 supplies the same graph-intrinsic reverse connector orientation. Call this the OPPOSITE-ROLE CONNECTOR LOCK.

Thus every state-cycle vertex yields
  R408/R159 component-drop currency,
  OR an opposite-role R933 simultaneous two-seam packet,
  OR a same-role rigid endpoint state,
  OR, when both sheets are opposite-role and avoid R933, an opposite-role connector lock shared by the two sheets.

This is the endpoint-role cover-exchange circuit exposed by the two-sheet support monodromy. The remaining theorem must consume a finite 2m-cycle in which same-role states and opposite-role connector locks coexist, by R561, profitable K* recombination, or a spanning two-cover. In particular one may not assume that every two-ended state admits an R933 test merely because its two neighbors lie on different rails. No final circuit consumer is claimed here.

### 11. A fully order-quiet two-sheet circuit has physical length three
Retain Sections 7-10 and exclude the already explicit R408/R159 component-drop output. Index the exact state cycle (9.1) cyclically as
  v_0,v_1,...,v_{2m-1},
where the physical deletion label of v_j is a_{j mod m}. Let C_j be the retained actual cover at v_j. Its two state-cycle neighbor labels are physical endpoints on opposite rails.

Fix one state-cycle edge C_j--C_{j+1}. Write x for the physical label of v_j and y for that of v_{j+1}. Trim the endpoint y from C_j and the endpoint x from C_{j+1}. This gives two literal exact two-covers F_j,F_{j+1} of the same proper residue H-{x,y}. Compatibility of the two state alternatives means that their unordered rail supports are exactly the same.

Call K the common support containing the exchanged labels before trimming, and L the opposite common support. On K the two trimmed Hamilton paths may a priori have different orders. If they do, accepted R435 applied to those two Hamilton paths gives its explicit reverse-state / reverse-trimer / proper-cycle output. Hence in the R435-quiet branch the literal K order is the same in F_j and F_{j+1}.

The singleton-deletion rail floor is at least three: an order-one rail closes with the deleted vertex as a dimer, and an order-two rail closes because the deleted vertex together with that dimer has some tight Hamilton trimer. Therefore after trimming the exchanged endpoint, K has order at least two. If y attaches to the K order at one end in C_j while x attaches at the opposite end in C_{j+1}, the two certified endpoint extensions concatenate with that literal common K order to a Hamilton path on K+{x,y}. The literal common L rail is its disjoint Hamilton complement, giving a spanning two-cover of H. Thus outside closure and R435 output the exchanged endpoint has the SAME source/terminal role on the two sides of every state-cycle edge. Define s_j in {0,1} to be this common role on edge C_j--C_{j+1}.

Now assume m>=5. The two outer physical labels v_{j-1} and v_{j+2} are then distinct. In F_j, the label v_{j-1} is an endpoint of the L rail. In F_{j+1}, the label v_{j+2} is an endpoint of the L rail. If either outer label were internal in the other cover, accepted R408 on the common residue H-{x,y} would give the explicit endpoint/internal component-drop output. Hence outside R408 both outer labels are endpoints in both F_j and F_{j+1}. Since they are distinct, they are exactly the two endpoints of the Hamilton L rail.

Again compare the two Hamilton orders on L. If they differ, accepted R435 gives explicit order geometry. In the R435-quiet branch they are literally the same ordered path, so its two physical endpoints v_{j-1},v_{j+2} have opposite source/terminal roles. Their roles in C_j,C_{j+1} are exactly s_{j-1},s_{j+1}. Therefore
  s_{j+1}=1-s_{j-1},
for every j, equivalently
  s_{j+2}=1-s_j.                                      (11.1)

But the state cycle has length 2m and m is odd. Iterating (11.1) exactly m times advances by 2m and returns to the same state edge while flipping its role m times, hence
  s_j = 1-s_j,
a contradiction.

Consequently a proper endpoint-current two-sheet circuit of physical length m>=5 cannot remain simultaneously R408-quiet and R435-quiet. It either closes H, produces the explicit R408/R159 component-drop currency, or contains a circuit-current R435 reverse-state / reverse-trimer / proper-cycle event. The only possible fully order-quiet physical length is m=3, where the two outer state-cycle labels in the preceding argument are the same physical vertex and the role recurrence degenerates.

### 12. The m=3 quiet survivor is a paired constant-role HHH/TTT hexagon
Let the three physical circuit labels be 0,1,2 and put O=V(H)-{0,1,2}. Use the outside-anchor orientation from Section 7. The restrictions of all six state supports to O are identical, so write the two fixed outside blocks as U|V. After possibly exchanging U,V and cyclically relabelling 0,1,2, the exact two-sheet support hexagon is
  C_0^0 : (U+1) | (V+2),
  C_1^0 : (U+0) | (V+2),
  C_2^0 : (U+0) | (V+1),
  C_0^1 : (U+2) | (V+1),
  C_1^1 : (U+2) | (V+0),
  C_2^1 : (U+1) | (V+0).                              (12.1)
Every displayed support carries an actual Hamilton path. The circuit labels are physical endpoints on their displayed one-label extension rails.

Assume first that no R435 order event occurs anywhere among the Hamilton paths on the same fixed support. For each i, trim i from any Hamilton path on U+i occurring in (12.1); this gives a Hamilton path on U. Comparing the resulting U orders for different i by R435 shows that they must all be one literal order P_U. The same holds on V, with one literal order P_V. Likewise the two occurrences of U+i expose i at the same end outside R435 endpoint-inversion output; write u_i for that source/terminal role. Define v_i dually on V+i.

The state-cycle edge C_0^0--C_1^0 exchanges labels 1 and 0 on the U side, so Section 11 gives u_1=u_0. The next U-side exchange and its sheet dual give u_0=u_2=u_1. Thus
  u_0=u_1=u_2=:u.
Similarly the three V-side exchanges give
  v_0=v_1=v_2=:v.                                    (12.2)
Hence every U+i extension exposes i in one common role u, and every V+i extension exposes i in one common role v.

If u and v are opposite roles, then every one of the six state covers has opposite-role circuit endpoints. Consider the two sheet states deleting the same physical label, say 0. In C_0^0 the ordered predecessor/successor role pair is (v,u), while in C_0^1 the two surviving labels have exchanged U/V sides, so the ordered role pair is (u,v). These are opposite ordered pairs. Exactly one of the middle-0 orientations on {2,0,1} is tight. Therefore one of the two sheets demands the tight role-correct connector and accepted R933 fires there. Consequently, in the branch avoiding R933 one must have
  u=v.                                                (12.3)

Thus the fully R408/R435/R933-quiet three-label residue is constant-role on BOTH cores. If u=v is SOURCE, write
  P_U=(u_1,...,u_r),  P_V=(v_1,...,v_s).
Then for every circuit label i there are literal Hamilton paths
  (i,P_U) on U+i,     (i,P_V) on V+i.                 (12.4-H)
If u=v is TERMINAL, the exact dual holds:
  (P_U,i) on U+i,     (P_V,i) on V+i.                 (12.4-T)
Call these the paired HHH and paired TTT hexagons respectively.

There is one further exact blocker packet. For distinct circuit labels i,j let k be the third label. The support U+{i,j} cannot be Hamiltonian, because V+k is Hamiltonian and the two would span H. In the HHH case, (j,P_U) certifies every turn of the proposal (i,j,P_U) except (i,j,u_1); therefore that turn is bad and R3 gives
  (u_1,j,i) tight.
Swapping i,j gives (u_1,i,j) tight. The same argument with V gives both
  (v_1,j,i), (v_1,i,j) tight.                         (12.5-H)
In the TTT case the exact terminal dual gives, with u_r,v_s the terminal core vertices,
  (i,j,u_r), (j,i,u_r), (i,j,v_s), (j,i,v_s) tight.  (12.5-T)
for every unordered pair {i,j}. Thus the quiet m=3 residue is not anonymous same-role behavior: it is a six-cover common-core hexagon carrying two simultaneous same-polarity three-label collision fans. No spanning two-cover, R561 state, or K* descent is claimed from this final packet.

### 13. The paired constant-role hexagon has an exact one-sided reverse-boundary shield
Retain the HHH branch (12.4-H), with P_U=(u_1,...,u_r) and P_V=(v_1,...,v_s). Fix distinct circuit labels i,j and let k be the third label. The support U+{i,j} is non-Hamiltonian: otherwise its Hamilton path together with the actual Hamilton complement (k,P_V) would be a spanning two-cover of H.

Now test the literal proposal
  (i,P_U,j).
Every turn before the final junction is certified by the actual source extension (i,P_U). Hence if (u_{r-1},u_r,j) were tight, this proposal would Hamiltonize U+{i,j}, impossible. Boundary antisymmetry therefore gives
  (j,u_r,u_{r-1}) tight
for every circuit label j. The same argument on V gives
  (j,v_s,v_{s-1}) tight.                         (13.1-H)
Thus every circuit label is simultaneously a source-extension label for the whole core and a reverse-terminal-trimer witness on the literal terminal core dimer.

The TTT branch is the exact dual. If (P_U,i) and (P_V,i) are the three terminal extensions, then non-Hamiltonicity of U+{i,j} tested by the proposal (j,P_U,i) forces
  (u_2,u_1,j) tight,
and dually
  (v_2,v_1,j) tight                                (13.1-T)
for every circuit label j. These are graph-intrinsic reverse-boundary trimers; no full boundary-reversed Hamilton order, R561 conclusion, or closure is asserted.

### 14. Opposite-sheet trims give two exact pair-deletion covers with a double endpoint/internal swap
Still in the HHH branch; the TTT proof is the exact head/tail dual. Fix an unordered circuit pair {j,k} and let i be the third label. Among the six actual covers in (12.1), trim the displayed endpoint k from an appropriate j-deletion state carrying (i,P_U)|(k,P_V), and trim the displayed endpoint j from the corresponding k-deletion state carrying (j,P_U)|(i,P_V). This gives two literal exact covers of the SAME pair-deletion residue H-{j,k}:
  T_U=(i,P_U) | P_V,
  T_V=P_U | (i,P_V).                               (14.1)
The singleton-deletion rail floor from Section 11 ensures |U|,|V|>=2. Hence u_1 is internal in T_U and an endpoint in T_V, while v_1 is an endpoint in T_U and internal in T_V. Thus the paired hexagon contains TWO simultaneous accepted R408 endpoint/internal disagreements on one pair-deletion residue.

More is available without treating the R408 pair as a bare floor. Puncture u_1. Then (14.1) gives on
  W=H-{j,k,u_1}
the literal three-cover
  (i) | U[2,r] | P_V
and the literal two-cover
  U[2,r] | (i,P_V).
The latter selects the directed state i v_1, whose endpoints lie in the singleton-i and P_V components of the former. Since W is proper, choose the actual spare vertex d=u_1. Accepted R176/P540 now applies with x=i, y=v_1, d=u_1. Here the R-component of x is already the singleton (i), so the singleton-source branch of P540 directly births an ancestry-bearing balanced opposite-sign pair with singleton supports (i) and (u_1), retaining the selected cross-state i v_1 and common witness v_1. Thus in the HHH orientation the paid both-singleton floor is obtained immediately; R428 is neither needed nor applicable after this particular birth because the opposite support is already singleton. Puncturing v_1 and using the selected directed cross-state i u_1 gives the exact dual ancestry-bearing floor with singleton supports (i),(v_1).

For the TTT hexagon, write the dual core paths as (P_U,i) and (P_V,i). The pair-deletion covers dual to (14.1) are
  T_U=(P_U,i) | P_V,
  T_V=P_U | (P_V,i).
The physical pivots are now u_r and v_s. Puncturing u_r gives a three-cover U[1,r-1] | (i) | P_V and a two-cover U[1,r-1] | (P_V,i), whose selected directed cross-state is v_s i. Apply R176/P540 with spare d=u_r. Since the R-component containing x=v_s is the nontrivial P_V rail, P540 births a balanced pair with fixed singleton support (u_r) and a nontrivial signed dimer supported at the terminal P_V neighbor; accepted R428 then either closes H or pays that nontrivial side to singleton width while preserving u_r and the birth ancestry. The v_s puncture is the exact dual. The minimum case |U|=|V|=2 is included: the surviving core fragment is a singleton and the P540 terminal neighbor required in the TTT branch still exists.

Consequently a surviving paired HHH/TTT hexagon canonically enters the genuine ancestry-bearing paid-floor regime. The route is literal common-residue component drop -> selected cross-state -> R176/P540, followed by R428 only in the TTT nontrivial-support branch; no bare balanced pair is reminted as a paid floor.

### 15. Every circuit pair carries two doubled fixed-turn interfaces on the same exact residue
Retain {j,k}, third label i, and one genuine ancestry-bearing paid floor supplied by Section 14. Accepted R432 may steer that floor to the prescribed outer singleton pair {j,k}, unless H closes during steering. R432 explicitly need not preserve the old source representative or its rails as current. This causes no provenance gap here: the two covers T_U,T_V from Section 14 remain separately retained literal exact covers of H-{j,k}, while R432 supplies only the active ancestry-bearing floor aligned to the same outer pair. The consumers below require those two ingredients, not their coexistence in one representative.

In the HHH branch apply boundary antisymmetry to the middle-u_1 reversal pair on {j,u_1,k}. Exactly one of
  (j,u_1,k), (k,u_1,j)
is tight. Call it J_U=(a,u_1,c), where {a,c}={j,k}. The exact pair-deletion covers (14.1) expose BOTH fixed-turn roles in the same residue H-{a,c}:

* in T_U=(i,P_U)|P_V, the middle u_1 is internal, with literal predecessor i and successor u_2. The active R432-steered ancestry-bearing floor is aligned to {a,c}, so accepted fully reconstructible R442 applies to J_U together with this exact cover;
* in T_V=P_U|(i,P_V), the same middle u_1 is an endpoint of the literal P_U rail. Apply the current endpoint-return compiler R919/P992 to J_U and this exact cover. If |P_U|=2 its explicit order-two clause gives the unique reverse mate; if |P_U|>=3 it gives the exact two-hole mate disjunction. No rail-floor-three assumption is needed.

Dually, boundary antisymmetry chooses a tight turn J_V=(a',v_1,c') with outer pair {j,k}; T_V makes v_1 internal while T_U exposes v_1 as an endpoint. Hence the same R442/R919 doubled interface occurs on the V core.

For the TTT hexagon the exact head/tail dual uses the physical middles u_r and v_s, the pair-deletion covers (P_U,i)|P_V and P_U|(P_V,i), the right-end clause of R919, and R442 with predecessor/successor (u_{r-1},i) or (v_{s-1},i). The minimum core order two is again covered explicitly by R919 and still leaves the one neighbor needed for the internal R442 frame.

In the beyond-order-ten range, accepted R446 may be used as the historical consumer of the internal-middle R442 packet, reducing it to a spanning two-cover, an explicit mate clause, or a source-localized ancestry-bearing floor. R446 is not fully reconstructible and is not needed for the exact doubled-interface statement above.

Therefore the m=3 constant-role hexagon is not a wholly new terminal species: on every circuit-pair deletion residue it retains two physical middles, two exact covers with opposite endpoint/internal roles, a steered ancestry-bearing floor on the same outer pair, and the reverse-boundary shields (13.1). This still does not prove O4: the R919 mate clauses and R442/R446 interaction outputs require a final consumer. The sharpened residual is a SAME-RESIDUE doubled fixed-turn discrepancy problem, not an unconstrained six-cover role packet.
