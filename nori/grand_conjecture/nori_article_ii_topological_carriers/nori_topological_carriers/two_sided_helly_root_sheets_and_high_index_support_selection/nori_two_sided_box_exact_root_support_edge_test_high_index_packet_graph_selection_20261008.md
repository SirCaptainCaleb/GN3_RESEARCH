# Topology-first closure reduces to a Helly flag-graph selection with exact root/support compatibility tests

# EXACT EDGE TEST FOR TWO-SIDED PHYSICAL ROOT SHEETS AND A TOPOLOGY-FIRST, GRAPH-LEVEL GRAND CLOSURE CRITERION

Inputs, all proved in NORI:
- nori_two_sided_root_sheet_helly_equivariant_exact_grand_fixedpoint_index_four_ceiling_20261008: the genuine two-sided physical path box nerve E is a Θ-equivariant FLAG complex, GRAND iff a Θ-fixed point, and under hypothetical no-grand 3<=ind_Z2(E)<=4.
- nori_multiroot_permutohedral_endpoint_zero_synchronized_face_packets_high_index_20261008: for any t distinct physical root representatives with 1<=t<=n−2, the actual endpoint-opposed permutohedral packet complex K_X is free under simultaneous full-order reversal and carries nonzero w^(n−2−t).

For any admitted <=1-switch partial directed ordered-three-face path P of length k>=3, let root x(P)∈F2^n, used direction set W(P), unused D(P)=[n]\W(P), and middle-window common free directions
  M(P)=intersection of free-direction sets of all its ordered three-face windows,
with |M(P)|=max(6−k,0). Its complete physical-face-invariant root sheet fixes every coordinate OUTSIDE M(P) to x(P). Its Θ-reversed image has invariant root sheet fixing coordinates outside M(P) to x(P) XOR D(P). Let B(P)=S(P)×S(ΘP) be the exact two-sided coordinate box.

**THEOREM 1 (combinatorial EDGE-INTERSECTION EQUALITY, iff).** For ANY two actually admitted paths P,Q, their two-sided boxes intersect iff BOTH conditions hold:
  supp(x(P) XOR x(Q)) ⊆ M(P)∪M(Q),
  W(P) △ W(Q) ⊆ M(P)∪M(Q).
Equivalently
  supp(x(P) XOR x(Q)) ∪ (W(P) △ W(Q)) ⊆ M(P)∪M(Q).
When this condition holds, the intersection B(P)∩B(Q) is a literal coordinate product subcube with at least one Boolean source-root pair, so every component witness is physically genuine; no convexification or arbitrary facial-color interpolation occurs.

PROOF. At any coordinate i outside M(P)∪M(Q), BOTH original sheets have fixed bits x_i(P),x_i(Q), so they intersect in that coordinate iff x_i(P)=x_i(Q). Both Θ-sheets have fixed bits x_i(P) XOR 1_(i∈D(P)) and x_i(Q) XOR 1_(i∈D(Q)), so (given equality of original bits) their fixed bits match iff 1_(i∈D(P))=1_(i∈D(Q)), equivalently i notin W(P)△W(Q). At coordinates in M(P)∪M(Q), at least one of the two original sheets and at least one of the two Θ-sheets are free, so no disagreement is possible. Coordinatewise independence gives necessity and sufficiency simultaneously. QED.

**COROLLARY 2 (physically certified local repair graph).** Make a finite graph H_c whose vertices are ALL actual <=1-switch partial directed path states P (length >=3), with P--Q iff the criterion of Theorem1 holds. Then E is EXACTLY the clique/flag complex Cl(H_c). Physical antipodal path reversal Θ acts as a graph involution, because the actual boxes are exchanged by factor swap, and the vertex η(P)=bar(endpoint P)−root P is a genuine odd sign-vector label. Every graph clique is realized by ONE simultaneously valid Boolean source root and ONE simultaneously valid Boolean Θ-root, due coordinate-cube Helly2.

**THEOREM 3 (HIGH-INDEX PACKET GRAPH LIFT IMPLIES GRAND NORI).** Fix an integer t with 1<=t<=n−7, and ANY t distinct cube roots X=(x1,...,xt). Let K_X be the team's ACTUAL multiroot endpoint-opposed full-geodesic permutohedral packet nerve; its known index satisfies
   ind_Z2(K_X) >= n−2−t >=5.
Suppose one can choose, for EACH vertex v of K_X, an actual admissible <=1-switch PARTIAL path state P(v) of length >=3 such that:
 (a) EQUIVARIANCE: P(Θv)=ΘP(v);
 (b) EDGE LOCAL COMPATIBILITY: for EVERY edge {v,w} of K_X, the roots/used sets of P(v),P(w) satisfy the exact inclusion
     supp(x(P(v)) XOR x(P(w))) ∪ (W(P(v))△W(P(w)))
       ⊆ M(P(v))∪M(P(w)).
Then the FULL unrestricted active NORI GRAND CONCLUSION HOLDS.

PROOF BY TOPOLOGICAL INDEX CONTRADICTION. If no grand path existed, the physically certified E would be free and have ind(E)<=4 by the exact index-four ceiling theorem. By (b) and Theorem1, the vertex assignment sends every EDGE of K_X to an E edge (or collapses its two ends to one E vertex), and because E is FLAG, it sends EVERY higher-dimensional simplex of K_X to a valid simplex of E. By (a) it therefore extends to a continuous Θ-equivariant simplicial map
   |K_X| -> |E|.
The first Stiefel–Whitney class of K_X is the pullback of that on E. Since w_E^5=0 but w_(K_X)^5≠0 (its higher nonzero w power implies every lower power nonzero), this is impossible. Consequently the assumption of grand failure is false and there is an actual full antipodal <=1-switch path. QED.

**STRONG CONTRAPOSITIVE / PRACTICAL SEARCH TARGET.** Under any hypothetical grand failure in dimension n>=8, EVERY equivariant selection of physically actual good PARTIAL path states P(v) at all vertices of the single-root permutohedral endpoint-opposed complex K_x MUST contain some K_x edge v--w violating Theorem1's purely root/support/middle-coordinates criterion. For t roots, the same is true whenever n>=t+7. Thus the FULL topological obstruction is reducible to a finite, root-and-used-set-compatible GRAPH SELECTION LEMMA. The combinatorial work is inside the topological frame: choose witnesses that are automatically Θ-equivariant and prove the exact TWO-SET inclusion along each packet edge. Once that edge lemma is established, higher simplex filling is FREE, thanks to genuine cubical Helly2, and the index contradiction is immediate.

**LIMITATION AND NO-GO TEST.** This sufficient selection theorem is CONDITIONAL. It cannot be obtained merely by choosing arbitrary three-edge subpaths: these are always monochromatic but may fail the root/support compatibility criterion even for two vertices lying in one common permutohedron face. The even-dimensional exterior-parity bad-root example has high-index endpoint packet carriers but no good FULL path from that root, so any proposed universal local selection rule must genuinely use cross-root physical-face structure. The graph selection lemma has NOT been proved. This is a rigorous reformulation, not a solution of grand NORI.

**COROLLARY 4 (for n>=8, the graph-selection condition is actually EQUIVALENT to GRAND closure).** Take t=1 and the genuine fixed-root endpoint-opposed high-index permutohedral face nerve K_x for ANY chosen root x, in any dimension n>=8. Its vertex set has the fixed-point-free reversal involution. The following are equivalent:
 (i) NORI admits some full antipodal geodesic with at most one ordered-3-face color change, from an arbitrary root (not necessarily x);
 (ii) one can assign one ACTUAL <=1-switch partial path state P(v) to each vertex v of K_x, equivariantly under physical reversal, satisfying the exact root/support middle-set compatibility on every K_x edge.

The implication (ii)->(i) is Theorem3. Conversely suppose (i) with full good path P0. The physical ΘP0 is also full good and has SAME root as P0. Its exact root-invariant sheet equals S(P0), so B(P0)=B(ΘP0), and these two vertices in E have a common box. For each Θ-orbit {v,Θv} of K_x choose one representative v, assign P(v)=P0 and P(Θv)=ΘP0. Because ALL assigned boxes equal the SAME actual root-sheet product box B(P0), every edge satisfies the intersection condition and equivariance is literal. Hence (i)->(ii). 

This makes an EXACT finite *graph-lifting version* of grand NORI for n>=8. The TRUE missing mathematical work is proving the graph selection without assuming the already desired full witness; the conditional theorem alone is not grand closure. It eliminates all higher-simplex bookkeeping, because genuine coordinate-box 2-Helly automatically fills every selected clique.
