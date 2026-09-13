# D1 — Five-cell recompletion, fragmentation, and exact-cover interfaces

Complete connected development of the crossed inward-anchor five-cell recompletion theory. It gives the minimum-layer classification and physical restoration arguments, the unfragmented and fragmented excess geometry, the separator conservation law, source-labelled consumer interfaces, and a status-separated historical archive of the interior-switch and 43-configuration routes.

## The five-cell residue and its exact transition tax

Put D={q_2,q_{m-2}} and W=H-D. In the crossed inward-anchor frame the five pairwise disjoint tight source paths are
G_0=Q[0,1], G_1=Q[3,m-3], G_2=Q[m-1,m], G_3=(a,c), G_4=(b,z).
They partition W. For an exact two-cover T of W let b_i be the number of maximal nonempty T-blocks lying in G_i, B=sum_i b_i, let t_G(T) be the number of T-edges joining different cells, and define sigma_G(T)=B-5.

Because each G_i is itself one path, the intrinsic partition-cover deficit identity R7 gives
 t_G(T)=sum_i pc(G_i)-2+sigma_G(T)=5-2+sigma_G(T)=3+sigma_G(T).
Hence t_G>=3. Equality holds exactly when sigma_G=0, equivalently b_i=1 for all five i, so every source cell occurs as one contiguous T-block. This is R862. Every intercell transition is a physical transition in the residue W; R176 may therefore use either deleted anchor as its separate spare coordinate when a downstream cross-state upgrade is invoked. Nothing in this count asserts a paid floor or synchronizes different exact covers.

## The complete sigma=0 classification and restoration argument

Assume sigma_G(T)=0. Contract each source cell to a labelled vertex. Since T has two path components, the contracted object F_T is a two-component path forest on five vertices with three edges. The two X cells cannot be adjacent: an edge G_3G_4 would concatenate the two tight X dimers into a Hamilton P4 on X, forbidden in the crossed no-P4 cell. At least one Q-X transition occurs. Writing c_X for the number of Q-X edges, degree and edge counting gives c_X in {1,2,3}.

For c_X=1 the old unique-transition analysis applies: the forest is P4 plus an isolated X cell, and the three-hole/one-transition compiler produces the previously named dimer refinements. The new residue is c_X in {2,3}. Up to the Q/X type quotient there are exactly six forests:
 A: X-Q-Q-X plus isolated Q;
 B: Q-Q-X-Q plus isolated X;
 C: Q-Q-X plus Q-X;
 D: Q-Q plus X-Q-X;
 E: X-Q-X-Q plus isolated Q;
 F: Q-X-Q plus Q-X.
This is R866.

Apply Reverse Ear R435 to the Q contacts. Outside its explicit reverse-state, reverse-contact/trimer, or tight-cycle outputs, the Q contacts on each T-rail occur in increasing Q order, and every unfragmented Q source cell is read in the literal Q order. Thus the only possible Q-Q transitions are the physical skips G_0G_1 through q_1,q_3, G_1G_2 through q_{m-3},q_{m-1}, and G_0G_2 through q_1,q_{m-1}. This is R867.

If an X cell has degree two in F_T, its two Q neighbours put it internally on a rail. R649 fixes the head polarity of G_3=(a,c) and the tail polarity of G_4=(b,z). At an internal X block, the selected Q adjacency supplies the opposite natural endpoint polarity; R518 then gives a labelled Hamilton P4. Therefore shapes B,E,F are P4-producing. In the P4-free branch G_4 is initial and G_3 terminal. Only A,C,D survive. This is R868.

Shape A. One rail is E_L-G_i-G_j-E_R with the two X blocks at its ends and i<j; the third Q cell is isolated. If the adjacent Q pair is G_0,G_1, restore v=q_2 between them and put d=q_{m-2} with G_2 on the other rail. The resulting long rail is Q[0,m-2]; the other case G_1,G_2 is dual. If the Q pair is G_0,G_2, the second rail v,G_1,d is Q[2,m-2]. For m>=7 all new turns are inherited Q turns. At m=6, G_1={q_3}. The nonadjacent case gives the tight trimer q_2,q_3,q_4. In the left adjacent case the only new seam is (q_2,q_3,x). If it is bad, R3 reverses it to (x,q_3,q_2); the static R849 tail-sign on D_L=(q_3,q_2), using the other appropriate gate witness, and R523/R518 yield a labelled P4. The right adjacent case is the dual seam (x,q_3,q_4), using the R849 head-sign on D_R. Hence every A configuration either restores the two anchors to a spanning two-cover or emits the stated P4 obstruction. This is R855.

Shape C. One rail contains an increasing Q-Q pair and endpoint X_A; the other contains X_B and the remaining Q cell. Use v=q_2,w=q_3,d=q_{m-2},r=q_{m-3},s=q_{m-1}. The boundary dimers D_0=(v,q_1) and D_2=(s,d) carry the fixed R616/R621 tail/head signs; G_3 has fixed head sign and G_4 fixed tail sign. If the Q pair is G_0,G_1, try the physical insertion X_B,d,G_2. The only two new holes are (y_1,y_2,d) and (y_2,d,s). If the latter reverses, it is opposite D_2 and gives P4. If the former reverses, then reversing X_B gives either the same-head R542 packet on G_3 or P4 on G_4. The G_1,G_2 case is dual through G_0,v,X_B and D_0. If the Q pair is G_0,G_2, leave that jump rail and absorb v,d on the G_1 rail: use K=(v,y_1,y_2,G_1,d) when X_B precedes G_1 and K=(v,G_1,y_1,y_2,d) in the other order. For m>=7 there is one new local hole, whose reverse is consumed by R542/P4 exactly as above. For m=6 the four possible seams are (v,q_3,x),(x,q_3,d),(y_2,q_3,d),(v,q_3,y_1); any bad seam reverses to an inward R849-labelled sign conflict and hence a P4. Thus C has no unnamed quiet residue. This is R856.

Shape D. One rail is a Q-Q pair and the other is X_L-G_1-X_R. For Q pair G_0,G_1, restore v and append d to obtain Q[0,m-2]; the G_1,G_2 case is dual. For G_0,G_2 leave the jump rail and put
 K=(v,x_1,x_2,G_1,y_1,y_2,d),
where X_L=(x_1,x_2), X_R=(y_1,y_2) are their actual T orientations. Even at m=6 the only new holes are h_L=(v,x_1,x_2) and h_R=(y_1,y_2,d). If both are tight, restoration closes. Otherwise R3 gives A=(x_2,x_1,v) or B=(d,y_2,y_1). If X_L=G_3,X_R=G_4, the reversal is opposite the corresponding fixed R649 sign and yields P4. If X_L=G_4,X_R=G_3, it agrees with the fixed sign and supplies the new witness needed for an R542 two-witness packet. This is R882, a current-interface rebase of historical R680.

Consequently R883 is exhaustive: in sigma=0, c_X=1 is the old unique-transition family; for c_X=2,3 the six typed forests exhaust the contracted possibilities, B/E/F emit P4, and A/C/D are handled by the explicit restoration/P4/packet routes above. There is no unnamed minimum five-cell species.

## Unfragmented excess geometry

Assume both X cells G_3,G_4 are contiguous T-blocks, but allow sigma>0. The fixed endpoint signs plus R518 force G_4 to be initial on its T-rail and G_3 terminal unless a labelled P4 already occurs. Outside the explicit R435 outputs, Q contacts on each rail are strictly increasing. Since each G_i for i=0,1,2 is a contiguous interval of Q, a given Q cell can occur at most once on each rail. Each X cell contributes exactly one T-block. Therefore any excess over the five baseline blocks comes only from a Q cell appearing on both rails. If k of the three Q source cells are represented on both rails, B=5+k and sigma=B-5=k. Thus sigma is exactly the number of doubled Q cells and lies in {0,1,2,3}; R862 gives t_G=3+sigma. This is R870. The conclusion is geometric: it records which physical Q cells are duplicated and retains the endcap roles. It is not merely the f=0 numerical specialization of R901.

## One conservation law controls the fragmented excess budget

General counting reference: D13/selected-forest-counting proves c(F-K)=k+|K|-e_F(K)-delta_F(K) for any selected k-path forest. Taking F=T, k=2, and K=X with |X|=4 gives the conservation identity below. The geometric LOW/MAX deductions remain specific to this section.

Let X=G_3 union G_4 and Y=G_0 union G_1 union G_2. For an arbitrary exact two-cover T put p=e_T(X), q=e_T(X,Y), r_Y=c(T[Y]), and delta_X=sum_{x in X}(2-d_T(x)). Because T is a spanning forest of exactly two paths, it has |W|-2 edges. The induced Y-forest has |Y|-r_Y edges, so counting the remaining selected edges gives p+q=r_Y+2. Summing selected degrees over the four X vertices gives 2p+q, hence delta_X=8-(2p+q). Eliminating q yields the unconditional identity
 r_Y+p+delta_X=6.
The total endpoint deficiency of a two-path forest is four, so delta_X is literally the number of its four rail-end slots occupied by X, with an isolated X vertex occupying two.

Now assume the BOUNDED branch of R885, and let f be the number of fragmented X cells. Every unfragmented X cell contributes its internal selected edge, so p>=2-f, and its forced initial/terminal placement contributes an X endpoint slot, so delta_X>=2-f. Define
 s=(p-(2-f))+(delta_X-(2-f))>=0.
Substitution into the conservation identity gives
 r_Y=2+2f-s.
Thus MAX is exactly s=0, namely p=2-f, delta_X=2-f, r_Y=2+2f, and q=2+3f. Each fragmented marker then has d_Y=2 and c=1+2f; in each unfragmented cell the inner vertex has d_Y=1,c=2+2f and the outer endpoint has d_Y=0,c=3+2f. The three specializations are f=0: (p,q,r_Y)=(2,2,2), c multiset {2,2,3,3}; f=1: (1,5,4), d_Y multiset {2,2,1,0}, c={3,3,4,5}; f=2: (0,8,6), all c=5.

LOW is exactly s>=1, so it has a physical meaning: either an extra selected X-X edge beyond the forced internal edges of unfragmented cells, or an extra X rail-end slot beyond the forced outer endpoints. At f=2 there is no forced contribution, so LOW4 iff p+delta_X>=1. Any selected X-X edge must then be cross-cell, one of ab,az,cb,cz, because both native dimers are fragmented; the other alternative is an X rail endpoint. Moreover 5-r_Y=p+delta_X-1. This is the complete R901 conservation proof and physical LOW4 normal form. It unifies the numerical faces, but does not imply the M/N skeletons or endpoint labels proved separately.

## Exactly one fragmented X cell: LOW2/MAX3 and its consumers

Assume the BOUNDED branch of R885 and f=1. Let F={x,x'} be the fragmented X cell and I the intact X dimer. R837 forces I to an endcap. Delete I from the selected two-path forest and then inspect either fragmented marker. The component identity gives c_x=k+deg_{T'}(x')-1 with k<=2 and deg_{T'}(x')<=2, hence both fragmented markers satisfy c<=3. Therefore exactly one of two regimes occurs.

LOW2: some fragmented marker has c<=2, equivalently r_Y<=3. Choose such x. With v=q_2,d=q_{m-2}, set D_x={v,d} union (X-{x}) and R_x=Y union {x}. The three vertices X-{x} form a tight trimer C by the no-P4 crossed X geometry. Probe C by v and d using R522. Either a labelled P4 occurs, or D_x has a Hamilton P5. If D_x has a P5 and c_x=1, that P5 together with the Hamilton R_x rail gives a spanning two-cover of H, impossible. Thus the surviving absorber case has c_x=2 and yields an exact spanning three-cover P5 union U union V. No assertion is made that U,V are both nontrivial; R879 is available only when that extra condition holds. This is R897.

MAX3: both fragmented markers have c=3, equivalently r_Y=4. The forest equations force p=1,q=5; the fragmented markers have d_Y=2, while the two intact-cell vertices have d_Y=1 and 0. Hence d_Y={2,2,1,0} and c={3,3,4,5}. Contract each maximal Y-run to Y, retain the intact endcap as II, and retain the two fragmented markers as individual F symbols. Up to swapping/reversing rails, interchanging fragmented labels, and reversing II, the skeleton is exactly
 M0: II-Y | Y-F-Y-F-Y,
 M1: II-Y-F-Y | Y-F-Y,
 M2: II-Y-F-Y-F-Y | Y.
The number t=0,1,2 of fragmented markers on the intact-endcap rail determines the skeleton. This proves the R886 MAX3 list. Source-cell placement is not discarded in actual use. R896 restores it: R840 says the Q cell adjacent to the intact endcap is either NONLOCAL or a physical endpoint Q cell; in M1/M2 the crossed endpoint signs force G_4-initial to attach on the left and G_3-terminal on the right, while M0 retains the stated left/right flexibility. Thus the M-skeleton is a quotient only; the current exact cover retains actual X labels, rail assignment, and endpoint source labels.

## Both X cells fragmented: LOW4/MAX5, N-skeletons, and simultaneous packets

Assume the BOUNDED branch and f=2. The forest equations give LOW4 iff some x has c_x<=4 iff r_Y<=5. The complement is MAX5: r_Y=6. Then p=0,q=8, every X vertex has d_Y=2 and c_x=5, and every X vertex is an internal separator between two Y-runs. Contracting the six Y-runs gives, up to rail symmetries and X relabelling, exactly
 N0: Y | Y-X-Y-X-Y-X-Y-X-Y,
 N1: Y-X-Y | Y-X-Y-X-Y-X-Y,
 N2: Y-X-Y-X-Y | Y-X-Y-X-Y.
This is R894. R901 sharpens LOW4 physically: because f=2 has no forced X edge or endpoint, LOW4 is exactly the presence of a selected cross-cell X-X edge among ab,az,cb,cz or an X rail endpoint, possibly both.

For a general fragmented marker, R900 converts actual local placement into a source-labelled interface. If x has a Y neighbour, one obtains either a P4-END output or a TWO-WITNESS packet typed by x and by the opposite endpoint role; the packet carries an all-X short carrier and is ready for R542. If x has no Y neighbour, retain the X-PURE alternative: its selected degree is one or two and its neighbours lie in the other X cell, giving an endpoint or literal X-only three-segment. In f=2 LOW4, a chosen low marker that is X-PURE forces r_Y<=3. Universal X-PURE is impossible in the P4-free crossed X cell because then the rails split X from Y and the X-only rail would Hamiltonize X. Hence at least one physical P4-END or two-witness packet exists.

MAX5 is stronger. Every X vertex has two distinct Y neighbours, so the X-PURE alternative disappears. R898 shows that, unless an endpoint-labelled P4 already occurs, four packets coexist simultaneously, with both head orientations on G_3 and both tail orientations on G_4. The all-X carriers are respectively (z,c,a) for the (a,c)-head packet, (b,a,c) for the (c,a)-head packet, (b,z,a) for the (z,b)-tail packet, and (z,b,c) for the (b,z)-tail packet. These carriers are R542-ready. Their simultaneity is additional geometry not contained in the conservation identity or N-skeleton count.

## Physical seam, witness, endpoint, and absorber interfaces

The useful outputs of the five-cell theory are physical objects on a retained exact cover, not generic statements that some short path exists. The LOW2 consumer R897 retains the chosen fragmented marker x, the five-vertex absorber support D_x, and the complementary exact cover of R_x. MAX3 retains the actual M-skeleton, actual rail, and source endpoint labels from R896. LOW4 retains a specific cross-cell selected edge or a specific X endpoint by R901 and a specific marker output by R900. MAX5 retains all four current-neighbour packets simultaneously by R898.

A separate seam amplifier R869 applies to nontrivial local seam trimers created by the preferred R176 construction in the inward-anchor residue. Such a seam lies wholly in W=H-{q_2,q_{m-2}} and therefore avoids both deleted anchors. Probe the same retained seam independently by q_2 and q_{m-2}. Each probe produces either a labelled inward P4 or the corresponding dual two-witness reverse-boundary packet. Thus the older branch in which the seam was supposed to meet q_{m-2} is empty. The seam itself and both probe identities must be retained. A P4 or packet is an interface, not a contradiction, until a proved exact-cover consumer uses it.

## Historical Internal-X restoration: valid m>=7 route, failed m=6 seam, repaired all-order route

The Internal-X subfamily has a useful historical alternative proof that should not be erased by the later A/C/D compiler.

Original R672/P750 claimed the all-order restoration. Its structural argument is sound through the monotone reduction: a c_X=2 Internal-X cover has one nontrivial rail containing all three Q cells and one internal X block, hence outside the explicit R435 outputs it is either G_0-X_i-G_1-G_2 or G_0-G_1-X_i-G_2. Removing X_i and restoring the corresponding deleted anchor constructs a jumped Q rail K_R on V(Q)-{q_{m-2}} or K_L on V(Q)-{q_2}. But P750 silently treated the newly exposed m=6 seam as an old Q turn. Therefore the all-m proof is invalid at m=6; its m>=7 portion survives.

R674/P752 states that surviving portion correctly. For m>=7, in the left-gap order remove X_i and insert q_2 between q_1 and q_3. Since q_4 lies in G_1, every newly exposed turn is consecutive in Q and the later G_1-G_2 seam is inherited from T. Thus
 K_R=(q_0,q_1,q_2,q_3,...,q_{m-3},q_{m-1},q_m)
is tight on V(Q)-{q_{m-2}}. Put d=q_{m-2}. If X union {d} had a Hamilton P5, it and K_R would be a spanning two-cover, so X union {d} is P5-free. R549 gives an outgoing extreme gate and incoming opposite extreme gate; R534 supplies complementary alternating gates; R536 and its terminal dual give four Hamilton P4s A_x on ({d} union X)-{x}, one for each x in X. Hence A_x union K_R is an exact two-cover of H-x for every x. The right-gap case is dual: remove X_i, restore q_{m-2}, obtain K_L on V(Q)-{q_2}, put d=q_2, and repeat the same P5-free gate construction. This m>=7 theorem is valid but abandoned as superseded; it remains a useful weaker-hypothesis route.

R675/P753 attempted to repair m=6. It correctly isolates the only new seam. In the left-gap case with G_1={q_3}, K_R=(q_0,q_1,q_2,q_3,q_5,q_6) needs only q_2 q_3 q_5 beyond inherited/old turns. If that seam is bad, R3 gives (q_5,q_3,q_2). The right-gap case similarly isolates q_1 q_3 q_4, whose bad orientation reverses to (q_4,q_3,q_1). However P753 cited old R658 to sign D_L=(q_3,q_2) and D_R=(q_4,q_3) as though a paid-floor conclusion were available. R658 was later invalidated for that overclaim. Therefore P753 is not a valid all-order proof even though its seam isolation is correct.

R852/P927 is the dependency-clean repair. It repeats the m>=7 construction unchanged. At m=6, for a bad left seam (q_5,q_3,q_2), accepted R849 gives the static tail signs of D_L by both b,z; the trimer itself supplies the opposite natural head polarity through q_5, so R518 gives labelled P4s on {q_5,q_3,q_2,b} and {q_5,q_3,q_2,z}. For a bad right seam (q_4,q_3,q_1), R849 gives the static head signs of D_R by a,c while the trimer supplies the opposite natural tail polarity through q_1, yielding P4s on {q_4,q_3,q_1,a} and {q_4,q_3,q_1,c}. If the seam is tight, K_R or K_L exists and the same P5-free R549/R534/R536 argument gives the four exact deletion covers. Thus R852 contains a valid all-order repaired Internal-X proof. It was abandoned because the later parent compilation subsumed its live use, not because this mathematical route is false.

## Exact 43-configuration audit of the monotone minimum residue

R871/P947 is a valid abandoned audit, not a realizability theorem. In the monotone sigma=0 residue with c_X in {2,3}, assign the physical labels G_0,G_1,G_2 to the Q roles and G_3,G_4 to the X roles of the six R866 shapes. The complete labelled list is:

A (6): [G0 | G3-G1-G2-G4], [G0 | G4-G1-G2-G3], [G1 | G3-G0-G2-G4], [G1 | G4-G0-G2-G3], [G2 | G3-G0-G1-G4], [G2 | G4-G0-G1-G3].
B (4): [G0-G1-G3-G2 | G4], [G0-G1-G4-G2 | G3], [G0-G3-G1-G2 | G4], [G0-G4-G1-G2 | G3].
C (12): [G0-G1-G3 | G2-G4], [G0-G1-G4 | G2-G3], [G0-G2-G3 | G1-G4], [G0-G2-G4 | G1-G3], [G0-G3 | G1-G2-G4], [G0-G3 | G4-G1-G2], [G0-G4 | G1-G2-G3], [G0-G4 | G3-G1-G2], [G1-G3 | G4-G0-G2], [G1-G4 | G3-G0-G2], [G2-G3 | G4-G0-G1], [G2-G4 | G3-G0-G1].
D (3): [G0-G1 | G3-G2-G4], [G0-G2 | G3-G1-G4], [G1-G2 | G3-G0-G4].
E (12): [G0 | G1-G3-G2-G4], [G0 | G1-G4-G2-G3], [G0 | G3-G1-G4-G2], [G0 | G4-G1-G3-G2], [G0-G3-G1-G4 | G2], [G0-G3-G2-G4 | G1], [G0-G4-G1-G3 | G2], [G0-G4-G2-G3 | G1], [G1 | G3-G0-G4-G2], [G1 | G4-G0-G3-G2], [G2 | G3-G0-G4-G1], [G2 | G4-G0-G3-G1].
F (6): [G0-G3 | G1-G4-G2], [G0-G3-G1 | G2-G4], [G0-G3-G2 | G1-G4], [G0-G4 | G1-G3-G2], [G0-G4-G1 | G2-G3], [G0-G4-G2 | G1-G3].

Completeness is not a brute-force assertion. Shape A: choose the isolated Q in 3 ways and order the two X endpoints in 2, giving 6. B: choose the isolated X in 2 and the internal-X gap G0|G1 or G1|G2 in 2, giving 4. C: choose the Q on the two-block rail in 3, its X label in 2, and the endpoint side in 2, giving 12. D: choose the Q used in X-Q-X in 3; reversing that rail adds no unoriented configuration, giving 3. E: choose the isolated Q in 3, the internal X in 2, and the endpoint side in 2, giving 12. F: choose the internal X in 2 and the Q on the separate Q-X rail in 3, giving 6. Hence c_X=2 has 6+4+12+3=25 configurations and c_X=3 has 12+6=18, total 43.

R867 forces the internal order of every Q block. Only the two orientations of G_3 and the two of G_4 remain, so there are at most 43*4=172 ordered rail pairs. Every turn internal to a Q block is already a Q turn; only block-boundary seams need checking. These involve only q_0,q_1,q_3,q_4,q_{m-4},q_{m-3},q_{m-1},q_m,a,b,c,z. For m>=9 the twelve roles are distinct; m=6,7,8 only identify some of them. This proves the finite-locality certificate. It makes no claim that all 43 configurations occur.

## What this theory does not prove

The five-cell classification is a recompletion interface. It does not close the crossed branch. A labelled P4 may be plentiful without yielding a spanning path or two-cover. A Reverse-Ear output is similarly weak in isolation. A two-witness packet is useful only when a theorem such as R542 consumes its precise support and polarity. LOW2 produces a three-cover absorber alternative, not automatically a two-cover. M0-M2 and N0-N2 are quotient skeletons; actual source labels and rail assignments must be retained when a downstream argument needs them. R901 unifies numerical budgets only and cannot replace R870, R886, R894, R896, R898, or R900.

Most importantly, all statements here are attached to one chosen exact cover T. Data produced on different exact covers of the same residue cannot be combined merely because their source cells have the same names. A separate common-fiber or exchange theorem is required to synchronize them.

## Remaining cover-valued recompletion gap

After the minimum and excess classifications, every retained exact inward-anchor recompletion lies in a named physical regime. The live gap is a cover-valued consumer. In LOW2 one must exploit the actual absorber and complementary rails. In MAX3 one must use the physically labelled M-skeleton and endpoint role. In LOW4 one must consume the named cross-cell X edge or X rail endpoint together with its marker packet. In MAX5 one has four simultaneous two-witness packets and an N-skeleton but still needs a theorem that acts on that same cover. The all-order bounded-reconstruction obstruction developed separately in D2 shows why preserving a prescribed middle block cannot be assumed from local eight-core data alone. Thus further progress should change or strengthen the consumer interface, not merely refine the already finite descriptive list.

## Extremal recompletion: low fragmentation or four universally internal separated markers

Fix a hypothetical smallest counterexample H to the two-path-cover conjecture. Let D={v,d} be two distinct vertices and X be a disjoint four-set; put W=V(H)-D and Y=W-X. For each ordered exact two-cover T of H-D define
  r(T)=c(T[Y]),
  s(T)=e_T(X)+delta_T(X),
  delta_T(X)=sum_{x in X}(2-deg_T(x)).
These are selected-forest quantities. Pair-deletion exactness follows directly from minimality: a Hamilton path on H-D plus the dimer D would two-cover H. Thus the finite collection of exact T is nonempty.

D13/selected-forest-counting gives, without gate or monotonicity hypotheses,
  r(T)=6-s(T).
Choose T_* maximizing s(T), equivalently minimizing r(T), over ALL exact two-covers of this one pair-deletion residue.

There is an exhaustive extremal dichotomy.
(LOW) s(T_*)>=1, hence r(T_*)<=5.
(PERSISTENT) s(T_*)=0, hence in EVERY exact two-cover T of H-D all four vertices of X have selected degree two and no selected edge joins two vertices of X.

Proof. Each summand in s(T) is nonnegative for a path forest. If the maximum is zero, both e_T(X) and delta_T(X) vanish for every T; this says precisely that every X vertex is internal and all its selected neighbors are in Y. The converse is immediate. In that case deleting X leaves exactly six nonempty Y-blocks. Contracting them gives the three N0/N1/N2 rail shapes according to the distribution 0+4, 1+3, or 2+2 of X markers between rails. These are T-ordered blocks; native-Q monotonicity is not asserted.

Fix x in X and orient J_x on {v,x,d} with middle x, using R3. The graded deletion theorem in D1/persistent-marker-deletion-lattice, applied with B=X and S={x}, gives an exact two-cover U sqcup V of H-J_x and proves that every such cover has both rails of order at least three. That section contains the general proof, directly from R3/R4 and universal internality; no R24-dependent rail floor is invoked.

For every such source cover, all four direct attachments of x to the ends of U,V are bad. Any tight attachment would again yield an exact H-D cover exposing x. For U=(u_0,...,u_t), this forces the tight reverse shields
  (u_1,u_0,x), (x,u_t,u_{t-1}),
and likewise at both ends of V. These conclusions hold for each x and every corresponding source cover. They require no R24, R5, R168, payment, or Reverse-Ear premise.

The quantifiers matter. A single selected MAX5 cover does not establish persistent internality. Persistence follows only when MAX5 survives minimization over the entire fixed pair-deletion fiber. Conversely finding one endpoint exposure of any x in X, or one selected X-X adjacency in any exact cover, eliminates the persistent branch.

In the crossed application D={q_2,q_{m-2}} and X={a,b,c,z}, this reorganizes the choice of recompletion before applying the existing five-cell classification. LOW here means r<=5 unconditionally; its refinement into the existing LOW2/MAX3/LOW4 branches still depends on the additional hypotheses used in those classifications.

This is a proved selection principle and shield consequence, not a closure theorem. It does not prove r(T_*)<=5, eliminate the persistent branch, synchronize the four different triple-deletion source covers, or guarantee D2 recognizer acceptance in the low-fragmentation branch. It is internal exposition pending independent mathematical review.

### Persistent internality is already a component-drop/payment branch

Keep the chosen x, J_x, and exact source cover U sqcup V. The source-rail floor and terminal shields are as above.

Now choose any exact two-cover P sqcup Q of H-D. In the persistent branch x is internal in every such cover, so after relabelling P=(...,ell,x,r,...) with both sides nonempty. Deleting x from P gives a literal three-cover P_L sqcup P_R sqcup Q of the proper residue H-J_x, while U sqcup V is a literal two-cover of exactly the same residue. The fully reconstructible component-drop theorem R159 therefore gives a graph-intrinsic balanced opposite-sign pair. This recovers the useful pair-birth part of the historical universal-return theorem R359 without invoking R168 or any R24/R5 lineage.

The four direct attachments of x to the two ends of U and V are bad by persistent internality, so R3 gives the four reverse terminal shields already displayed above. The two left reverse terminal dimers of U and V have the same polarity with common witness x, while the two right reverse terminal dimers have the opposite polarity. Consequently each cross-rail diagonal, left(U) with right(V) and left(V) with right(U), is a disjoint mass-four balanced opposite-sign pair. This is the signed rectangle historically isolated in R373, but here it is rederived directly inside the persistent branch.

Apply the fully reconstructible terminal-reversal payment theorem R532 to either diagonal. Its conclusion is an alternative certificate-retaining continuation: either a spanning two-cover occurs, or the chosen diagonal has a strict balanced-pair descendant of mass less than four, with the named terminal dimer and chosen endpoint-survival certificate retained as ancestry. In the hypothetical counterexample the spanning-two-cover alternative is unavailable. The two diagonal descendants are alternative lineages and are not asserted to coexist.

Thus PERSISTENT is not a quiet descriptive residue. For every x in X and every chosen source exact two-cover of H-J_x it supplies (i) a noncircular R159 component-drop pair, (ii) four graph-intrinsic terminal shields, and (iii) two explicit R532 payment channels. What remains open is to consume one of these ancestry-bearing descendants into the desired spanning two-cover or to couple it back to the selected pair-deletion fiber. No claim is made that payment alone closes the branch.

### Consequence for the selected-cover compression side

In the LOW alternative, r(T_*)<=5. Therefore the fixed-cover boundary accounting used in D2 improves immediately for this extremal representative: with K=X and |D|=2 there are at most r+6<=11 movable pieces, and the original-vertex boundary budget 6+4r is at most 26 rather than the generic 30. This is only a sharpening of the pending D2 selected-cover compression interface; it does not imply that its exact recognizer accepts.

The extremal dichotomy therefore exposes a cleaner parent interface: either one has a selected exact pair-deletion cover with a <=26-vertex block-preserving boundary instance, or one has universal X-internality together with the reconstructible component-drop/shield/payment outputs above. Neither branch is yet a closure theorem.

### A noncircular partner-splice collision and a genuine paid-floor lineage

Keep the same source state; the already established order-three rail floor makes both terminal trimer carriers available.

Write U=(u_0,...,u_r) and V=(v_0,...,v_s), now with r,s>=2. Consider the literal spanning proposal obtained by concatenating U to V and keeping J_x as the other rail. Its only new turns are
  h_1=(u_{r-1},u_r,v_0),
  h_2=(u_r,v_0,v_1).
They cannot both be tight, since then (U,V) sqcup J_x would be a spanning two-cover of H.

If h_1 is bad, R3 gives A=(v_0,u_r,u_{r-1}) tight. The persistent right shield (x,u_r,u_{r-1}) is also tight. Hence the tested reverse terminal dimer S_U=(u_r,u_{r-1}) has two distinct same-polarity witnesses x and v_0. Since r>=2, S_U is the reverse terminal dimer of the tight carrier trimer K_U=(u_{r-2},u_{r-1},u_r), and both witnesses lie outside K_U. Therefore accepted fully reconstructible R542 applies.

If h_2 is bad, R3 gives B=(v_1,v_0,u_r) tight. The persistent left shield (v_1,v_0,x) is tight, so S_V=(v_1,v_0) has the two distinct same-polarity witnesses u_r and x. Since s>=2, S_V is the reverse boundary dimer of K_V=(v_0,v_1,v_2), again exactly in the scope of R542. Thus the U-to-V splice forces at least one R542-ready terminal collision. Reversing the roles of U and V gives a second directional collision certificate. This reconstructs the partner-only core of historical R455 directly from persistence, without R359, R389, or R168.

R542 converts whichever winning collision is chosen into a certificate-retaining continuation to either a spanning two-cover or a balanced opposite-sign descendant with one singleton support. In the hypothetical counterexample only the latter remains. If the opposite support is already singleton, this is a genuine ancestry-bearing mass-two floor; otherwise fully reconstructible R428 pays the opposite support down to singleton width while preserving the installed singleton. Consequently every persistent source state has a completely reconstructible route to a genuine paid floor carrying the R542 carrier/dimer/two-witness/crossing/capture ancestry.

This is stronger than mere existence of a floor, which is globally ubiquitous by later coordinate theorems. Its potential value is the retained source provenance: the floor descends from a specific terminal dimer of U or V and from the literal U-to-V (or V-to-U) splice. The present argument does not show that a prescribed source coordinate is the singleton produced by R542, does not keep the old source cover current through R428, and does not yet convert that ancestry into closure. Those are the remaining consumer questions.

### Crossed PERSISTENT face: the fully internal MAX5 residue is entirely geometric

Specialize to the crossed inward-anchor frame D={q_2,q_{m-2}}, X={a,b,c,z}, with Y=G_0 union G_1 union G_2, G_0={L,u}, G_1=Q[3,m-3], G_2={s,R}. In PERSISTENT every exact H-D cover has e_T(X)=0 and delta_T(X)=0. Thus all four X vertices have selected degree two, all eight selected X-incidences go to Y, and both middle-gate cells are fragmented.

Fix such an exact cover T. Apply accepted R885/R894/R898. Any R885 P4/Reverse-Ear output or R898 P4-END output is already retained geometry. Otherwise T is MAX5 and R898 gives four simultaneous tested middle-gate witness packets. Each physical middle gate has an inward witness outside {L,R}: if both vertices of one gate had neighbour set {L,R}, the selected forest would contain a 4-cycle. Moreover some X-Y incidence lands in the genuine middle cell G_1. Otherwise all eight incidences land in B={L,u,s,R}, forcing every vertex of X union B to have degree two in the induced selected subgraph and hence forcing a cycle. Therefore choose a tested middle-gate orientation S with a deep witness y=q_i, 3<=i<=m-3.

Pending R921/P993 now consumes this witness completely. Apply accepted R682 to S,y in a fresh exact H-V(S) cover. No selected state of T is transported.

In XET, one obtains (R,y,L) or (L,y,R). The first is immediately R435-active because Q is encountered in reverse order. For (L,y,R), probe by q_{i-1} using R518. A Hamilton P4 is already geometry; otherwise R518 forces (y,L,q_{i-1}), whose consecutive Q contacts y then L run backward, so R435 fires.

In CAP, retain the actual selected endpoint crossing {e,t} avoiding y and orient R527 to capture e. The underlying R526 actualization certificate itself contains exactly one tight turn from the reversal pair (t,e,y),(y,e,t), centered at the physical endpoint e. If that turn encounters Q in reverse order, R435 fires immediately. In the only monotone orientation, choose one of q_{i-1},q_{i+1} different from t and probe the capture turn by R518. Its no-P4 signature forces a trimer with consecutive Q contacts e/y in reverse order, so R435 fires; otherwise a labelled P4 occurs. The right endpoint is the exact dual.

Thus, pending review of R921/P993, the crossed PERSISTENT/MAX5 face has **no payment, protected-contact, or fixed-turn residue**. It terminates entirely in a labelled P4 or explicit Reverse-Ear/reversal/cycle certificate with source Q-coordinates retained. This is stronger than the earlier paid-floor and protected-contact continuations and makes them unnecessary for this face. R921/P993 remain pending independent review and are not canonical inputs until accepted.


## Persistent markers force graded deletion exactness and common-source constraints

Let H be a hypothetical smallest counterexample, let D be a pair, and put W=V(H)-D. Let B be a nonempty set of vertices that are internal in EVERY exact two-cover of H[W]. The PERSISTENT alternative of extremal-recompletion supplies B=X, but the first assertion below needs no selected B-B separation and no four-set hypothesis.

Graded deletion exactness. For any S subset W with 1<=|S|<=3 and S intersect B nonempty, provided W-S is nonempty,
  pc(H[W-S])=2.
Moreover, in every exact two-cover of H[W-S], each rail has order at least 4-|S|.

Proof. Choose b in S intersect B. Every set of at most three vertices containing b has a Hamilton path with b as an endpoint: singletons and dimers are immediate; for {b,y,z}, one of (b,y,z) and (z,y,b) is tight by R3. If H[W-S] were Hamiltonian, its Hamilton path together with this path on S would be an exact two-cover of H[W] exposing b, a contradiction. Minimality supplies the upper bound two. Now suppose a source rail A has |A|<=3-|S|. The set A union S has at most three vertices and contains b, so it has a Hamilton path exposing b. Replace A by that path and keep the other source rail literally. This again two-covers W with an exposed b, a contradiction. This proves the rail floor. No R24, R5, R168, pair payment, or trimer-return theorem is used.

In particular, for distinct x,y in B, H[W-{x,y}] has an exact two-cover with both rails nontrivial. This is one common source residue for the two markers, not an identification of independently chosen covers of W-x and W-y. Singleton deletion at a persistent marker has both rails of order at least three, recovering the direct source-rail floor in extremal-recompletion. Triple deletion meeting B is still exact, even though singleton source rails are then allowed.

A simultaneous insertion constraint on the common source is immediate. Fix a two-cover A disjoint-union C of W-{x,y}. Form the bipartite graph with left vertices x,y and right vertices A,C, putting an edge when that marker can be attached at either end of the indicated source rail while leaving its order unchanged. This graph has no matching of size two: the two matched attachments would yield a W two-cover exposing the markers. If both markers have an available rail, all their available rails must consequently be the same single rail. Even on that rail, attachments at opposite ends cannot be jointly available: the rail has order at least two, so the two new endpoint turns are separate certified turns, and placing x and y at opposite ends would again yield a forbidden W cover. Same-end attachments are not asserted composable. This is a common-residue compatibility constraint, not a closure argument.

There is also a complementary Hamilton-support constraint using the full PERSISTENT hypothesis. Assume every W two-cover keeps B internal and selects no B-B edge. Let Z be a nonempty proper subset of W whose complement is Hamiltonian. Every Hamilton path on Z, if any, must have both endpoints outside B and no adjacent B vertices. Hence
  |Z-B| >= |Z intersect B|+1
is necessary for Z to be Hamiltonian. Indeed j internal separated markers on one path require at least j+1 other vertices. If this inequality fails, H[Z] is non-Hamiltonian, and minimality makes its path-cover number exactly two. In particular, a four-set Z containing at least two persistent markers and having Hamiltonian complement must itself be non-Hamiltonian. This gives an exact point at which non-Hamiltonian four-cell structure can enter the persistent branch.

Scope. These are consequences of universal internality over the entire fixed W-cover fiber, not of a single selected MAX5 representative. Exactness after deletion here is conditional on persistence and is not the unrestricted small-deletion theorem R168. The simultaneous insertion condition is necessary; absence of a matching does not rule out insertions requiring cuts or rearrangement. No identification of historical paid-floor ancestry with the present source cover is made. Full internal proof supplied; pending independent mathematical review.
