# The remaining G32 bad seam is a one-defect matching exchange against the old source cover

**Workspace:** D17
**State:** established
**Key:** `g33-defect-one-source-cover-exchange-normal-form`

**Summary:** From SV103129, a bad low-transition endpoint cut gives a spanning two-word proposal P on the top fiber G with exactly one bad consecutive turn eta and at most two selected X|B transitions, beside the actual old exact two-cover F with at least three transitions. Cutting either of the two word-edges inside eta yields a literal spanning tight three-path forest J with tau(J)<=2. Encoding oriented path forests as bipartite matchings gives |M_F|=|G|-2 and |M_J|=|G|-3; their symmetric difference is a disjoint union of alternating paths/cycles with total F-minus-J edge excess one, hence contains an F-heavy augmenting component. Every such cut forest omits at least one old X|B transition; for the retained active incidence s-h, either s-h itself is omitted or, if it survives, some other old transition is omitted. Flipping an F-heavy alternating component into J therefore gives a canonical size-|G|-2 matching candidate. If it is acyclic and all mixed turns are tight, it is an exact two-cover; otherwise the only defects are explicit directed-cycle debt or mixed bad-turn windows. Thus the remaining direct G32 problem is naturally a static defect-one matching/forest exchange with a transition-gap constraint, not temporal payment/replay. This section is a normal form, not a claim that some flip already lowers tau or closes H.

### 1. Input
Retain the direct G32 packet of exact unit SV103129. Thus

  G=H-{A,C}=X union V(B),
  X={v,p,q,r},

and F=U|V is the actual old exact source two-cover of G. On the fixed physical partition X|B,

  tau(F)>=3.                                                    (DX.1)

There is a B-active omitted source spoke s, an actual old selected source incidence s-h with h in B, an endpoint-favorable Hamilton P5 K_s, and one chosen LOW R540-style endpoint cut. The cut produces two vertex-disjoint spanning words

  P=P_1|P_2

whose complete uncertified-turn set is the singleton {eta}. Its selected X|B adjacency count is at most two. In the branch considered here eta is bad; SV103129 also retains its exact R3 reverse, but that reverse is not needed for the first reduction below.

### 2. Cutting the unique bad turn gives two literal three-forests
Write the unique bad consecutive turn as

  eta=(u,v,w),

so u-v-w occurs consecutively in one of the two words P_i. Cut that word at uv. Every consecutive triple that survives on either side of the cut was already a consecutive triple of P different from eta, hence is tight. No new consecutive triple is created by cutting. Together with the untouched other P-rail, the result is therefore a literal spanning tight three-path forest; call it J^- .

Cutting instead at vw gives a second literal spanning tight three-path forest J^+ by the same argument. Singleton or dimer pieces are allowed and create no turn obligation. Thus the bad one-hole proposal canonically determines two exact three-forests on the SAME top fiber G.

Deleting one selected adjacency cannot create a new X|B transition, so

  tau(J^-), tau(J^+) <= tau(P) <= 2.                         (DX.2)

Comparing (DX.1) and (DX.2), each J in {J^-,J^+} omits at least one selected X|B adjacency of the old cover F. In particular the retained old active incidence s-h is a concrete coordinate: either s-h is absent from J, or it survives in J and at least one OTHER old X|B transition is absent because J carries at most two transitions while F carries at least three. No anonymous birth history is needed to witness the discrepancy.

### 3. Exact matching-exchange representation
Orient every rail in its displayed tight order and encode a path forest J by the bipartite matching M_J in V(G)_out disjoint_union V(G)_in, selecting x_out y_in exactly when x->y is a consecutive directed adjacency of a rail. Do the same for F.

Because F is a spanning two-path forest and J a spanning three-path forest,

  |M_F|=|V(G)|-2,
  |M_J|=|V(G)|-3.                                            (DX.3)

The symmetric difference M_F triangle M_J is therefore the ordinary symmetric difference of two bipartite matchings. Its connected components are alternating paths and alternating cycles. On each component the F-edge count minus the J-edge count lies in {-1,0,1}, and summing over components gives +1 by (DX.3). Hence at least one alternating path component C is F-heavy: it contains one more F-edge than J-edge.

Flip C into J, replacing the J-edges of C by its F-edges. The result M_C is again a bipartite matching and has exactly |V(G)|-2 edges. It is consequently a canonical two-component DIRECTED-LINEAR-FOREST CANDIDATE unless physical directed cycles occur. If M_C is acyclic and every mixed predecessor-successor turn created at the exchange boundary is tight, its directed components are two literal tight paths and M_C is an exact two-cover of G. If not, the failure is completely static and local: either M_C contains explicit directed-cycle debt, or a mixed consecutive turn is bad.

This is the same matching language used elsewhere for compatible-forest exchange, but no same-component-count theorem is imported here: the present pair has matching sizes differing by exactly one.

### 4. The remaining theorem target
The direct G32 problem can therefore be posed without payment or replay clocks. Starting from either J^- or J^+, choose an F-heavy alternating component and control three quantities simultaneously:

1. physical acyclicity of the flipped matching;
2. tightness of its mixed boundary turns; and
3. the X|B transition count after the flip.

A flip that is acyclic, tight, and has transition count at most two gives a strict old-source descent immediately. More generally any exact flipped two-cover with transition count <tau(F) is sufficient. If every F-heavy component is blocked, the blocking directed cycle or mixed bad-turn window is an explicit finite static obstruction attached to the old source cover and the chosen low cut; it should be consumed before any generic payment machinery is invoked.

The source-mate full-H theorem SV102728 remains a separate strong consumer when the low-cut word has the required source-mate endpoint form. The present normal form does not claim that every F-heavy flip is legal, that the retained s-h edge lies on every augmenting component, or that cycle/bad-turn debt already closes H.

### 5. Scope
This section uses the exact physical output of SV103129 and elementary path-cut/matching facts only. It does not use R24, R5, a payment generation, or a historical novelty argument. It is a static representation of the sole direct G32 residue, intended to replace the larger generic trimerized-R540 target.
