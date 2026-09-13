# D4 — Gate-phase exact-cover geometry: common fibers, first-depth clauses, and consumers

Full-library gate-phase development containing the current ALIGNED/CROSSED interfaces, repair genealogies, first-step zipper archaeology and fences, fixed-core renormalizations, finite cap saturation, and deep endpoint-rotation packets.

## ALIGNED: common residue and forced first-inward stars


Assume the long ALIGNED phase and write Q=(q_0,...,q_m), L=q_0, u=q_1, v=q_2, t=q_3, r=q_{m-3}, d=q_{m-2}, s=q_{m-1}, R=q_m. Accepted R619 gives the two enlarged H-z covers and the two enlarged H-b covers. Deleting the other terminal root from each short rail yields four literal exact covers of the same residue H-{b,z}:

T_L^a=(u,L,a,c) sqcup Q[2,m],
T_L^c=(u,L,c,a) sqcup Q[2,m],
T_R^c=Q[0,m-2] sqcup (a,c,R,s),
T_R^a=Q[0,m-2] sqcup (c,a,R,s).

This is accepted R899. The representatives coexist graph-intrinsically and none is chosen canonically. Their support comparisons are equally literal. Relative to either right support partition Q[0,m-2] | {a,c,R,s}, T_L^a crosses exactly at La and ds, while T_L^c crosses exactly at Lc and ds. Relative to either left support partition {u,L,a,c} | Q[2,m], T_R^c crosses exactly at uv and cR, while T_R^a crosses exactly at uv and aR. Thus the common fiber carries the fixed physical cross-state rectangle {La,Lc,ds,uv,cR,aR}.

There is a stronger source-level consequence that should be used before gluing the pair-deletion representatives. The original R619 enlarged singleton-deletion covers force all four first-inward reverse stars by literal one-turn root reinsertion.

For root z, R619 gives
H-z=(u,L,a,c,b) sqcup Q[2,m].
If (z,v,t) were tight, then
(u,L,a,c,b) sqcup (z,v,t,q_4,...,q_m)
would be a spanning two-cover of H. Since pc(H)>2, (z,v,t) is bad; boundary antisymmetry R3 therefore forces (t,v,z) tight. The same argument from
H-b=(u,L,c,a,z) sqcup Q[2,m]
forces (t,v,b) tight.

At the right end, R619 gives
H-z=Q[0,m-2] sqcup (b,a,c,R,s).
If (r,d,z) were tight, then
(q_0,...,r,d,z) sqcup (b,a,c,R,s)
would be a spanning two-cover, so R3 forces (z,d,r) tight. Likewise the right enlarged H-b cover
H-b=Q[0,m-2] sqcup (z,c,a,R,s)
forces (b,d,r) tight.

Hence, throughout the ALIGNED phase,
(t,v,b), (t,v,z), (b,d,r), (z,d,r)
are simultaneous graph-intrinsic tight turns. No R899 same-residue comparison, R879 splice fan, capture, payment, or computation is used. These are exactly four accepted R703 inputs, two at the first inward left Q dimer and two at the first inward right Q dimer.

The two inputs on each side share the same R703 no-P4 residue. On the left, applying R703 to x=b,z gives for each x either a Hamilton P4 on {u,v,t,x}, or the common all-Q reverse trimer (v,t,u) together with the extra turn (u,x,v). Equivalently, one may split directly on the R3 reversal pair (u,t,v)/(v,t,u): if (u,t,v) is tight, then both literal P4s (u,t,v,b) and (u,t,v,z) are tight; if (v,t,u) is tight, the common reverse-Q trimer is already present and R435 applies. Dually, on the right, either both literal P4s (b,d,r,s),(z,d,r,s) occur when (d,r,s) is tight, or the common reverse-Q trimer (s,r,d) is present and R435 applies. Thus the ALIGNED branch has a synchronized first-depth normal form rather than four unrelated local events.

This strictly dominates the old strategic reading of the pending R918 recut. In a hypothetical counterexample the four R703 source triggers are already present before the R918 FIRST-DEPTH-EAR clauses are consulted. Consequently the 'outside all displayed R703 outputs' corridor used to reach the R918 ears and crossing signed-dimer packet is not a live counterexample branch. The live ALIGNED frontier is now the synchronized pair of first-depth alternatives just described: common reverse-Q geometry versus two simultaneous labelled P4s at each end.


## ALIGNED: pending R918 gluing is dominated by forced first-depth stars


R918/P989 remains pending and is not used as an established premise. Its GLUE step is structurally interesting: the R899 representatives sharing ac concatenate to K_ac=(u,L,a,c,R,s), those sharing ca concatenate to K_ca=(u,L,c,a,R,s), and with N=Q[2,m-2] one gets H-{b,z}=K_ac sqcup N=K_ca sqcup N. Thus the inner subsystem B=H[N union {b,z}] has pc(B)=2 and is nonHamiltonian, since a Hamilton path of B together with either glued P6 would two-cover H.

The later R918 route starts from the spanning three-cover K sqcup (b,z) sqcup N. R879 gives the clauses
(v,z,b) OR (t,v,z),
(b,d,r) OR (z,b,d),
(v,b,z) OR (t,v,b),
(z,d,r) OR (b,z,d).
R918 then says that outside the R703 outputs triggered by the four inward turns, both ears E_bz=(v,b,z,d) and E_zb=(v,z,b,d) occur; recutting those ears yields either old-Q reversals or the crossing two-witness chord packet on (v,r) and (t,d). This conditional mathematics is retained in R918/P989.

However, the current ALIGNED development no longer treats that quiet corridor as live. The preceding established `aligned-fiber` section proves directly from the original accepted R619 enlarged singleton-deletion covers and R3 that all four inward turns
(t,v,b), (t,v,z), (b,d,r), (z,d,r)
are already tight in every hypothetical ALIGNED counterexample. Each is an accepted R703 input. Therefore a source-labelled R703 P4/Reverse-Ear output occurs before the R879 ear alternatives can be entered. In particular the assumption 'outside the displayed R703 outputs' that is needed to obtain both ears is incompatible with the counterexample frame.

Two earlier conditional observations remain mathematically correct but are strategically dominated. First, if one formally follows the quiet R918 recut at m=6, the final packet would make (z,v,t,d,b) a Hamilton path of B, contradicting the nonHamiltonicity of B. Second, for m>=7 the formal final packet can be rotated by R700/R542 into labelled P4s or source-local capture/contact through Q-skipping carrier states. Neither should now be used as the main ALIGNED consumer, because the route reaches R703 earlier using accepted inputs only.

Accordingly, preserve R918 as an optional structural strengthening of R899 and as a record of the gluing/inner-obstruction geometry, but do not spend research effort on its ears, crossing dimers, payment, or deep-contact descendants unless a later argument specifically needs those graph-intrinsic facts. The live ALIGNED frontier is the synchronized first-depth normal form in `aligned-fiber`: at the left, either the common reverse-Q trimer (v,t,u) is tight or both P4s (u,t,v,b),(u,t,v,z) are tight; dually at the right, either (s,r,d) is tight or both P4s (b,d,r,s),(z,d,r,s) are tight. The next consumer should exploit the coexistence of the two end decisions and the original exact deletion covers.


## CROSSED: exact singleton-deletion source geometry

Assume the CROSSED phase of R619, with X={a,b,c,z}, Q=(q_0,...,q_m), L=q_0,u=q_1,v=q_2,d=q_{m-2},s=q_{m-1},R=q_m. The left middle gate {a,c} is outgoing from L and its complement {b,z} incoming to L, while the right roles are swapped. R621 retains the four deep root-labelled exact covers:

H-z=(u,L,a,c,b) sqcup Q[2,m],
H-b=(u,L,c,a,z) sqcup Q[2,m],
H-c=Q[0,m-2] sqcup (a,b,z,R,s),
H-a=Q[0,m-2] sqcup (c,z,b,R,s).

It also gives the opposite-end shallow covers
H-z=Q[0,m-1] sqcup (R,a,c,b),
H-b=Q[0,m-1] sqcup (R,c,a,z),
H-c=(a,b,z,L) sqcup Q[1,m],
H-a=(c,z,b,L) sqcup Q[1,m].
Thus every deletion root has two physical representatives with opposite-end absorption; their root labels and Q cuts are retained.

R723 symmetrizes this source geometry. For every x in X there are shallow covers H-x=A_x^L sqcup Q[1,m] and H-x=Q[0,m-1] sqcup A_x^R, with
x=z: A_z^L=(L,a,c,b), A_z^R=(R,a,c,b);
x=b: A_b^L=(L,c,a,z), A_b^R=(R,c,a,z);
x=c: A_c^L=(a,b,z,L), A_c^R=(a,b,z,R);
x=a: A_a^L=(c,z,b,L), A_a^R=(c,z,b,R).
Testing the first inward seams against the impossibility of a spanning two-cover forces, simultaneously for every x in X,
(v,u,x) tight and (x,s,d) tight.
These are graph-intrinsic universal reverse stars. The source cover representatives remain distinct physical certificates; no selected-state information is borrowed between them.

## CROSSED: pair-deletion clauses and BI-ANCHOR compression

The first-depth CROSSED argument starts by deleting a common gate pair from the R621 singleton representatives. Deleting b from the H-z left cover and z from the H-b left cover gives exact covers of H-{b,z}:
(u,L,a,c) sqcup Q[2,m],
(u,L,c,a) sqcup Q[2,m].
Write t=q_3. Concatenating the two rails of the first cover has exactly the seam holes (a,c,v),(c,v,t); since H-{b,z} is not Hamiltonian, R3 gives
(v,c,a) OR (t,v,c).
The second cover similarly gives
(v,a,c) OR (t,v,a).

Dually, deleting c and a from the two right R621 covers gives exact covers of H-{a,c}:
Q[0,m-2] sqcup (b,z,R,s),
Q[0,m-2] sqcup (z,b,R,s).
Write r=q_{m-3}. Their concatenations give
(b,d,r) OR (z,b,d),
(z,d,r) OR (b,z,d).
These are the four exact R911 first-depth clauses. R911 retains more information in a dimer branch: if both left clauses choose inward-dimer literals, the tested dimer (t,v) becomes two-sided by the R873/R523 mechanism and the resulting bidirectional P4 pair enters R843, yielding either block count greater than two or a source-visible reverse seam in every exact H-{t,v} cover; the right side is dual. Thus R911 should be used when exact cover and block provenance matters.

R914 is the coarser producer compression. Each inward-dimer literal (t,v,x) is exactly a left R703 input at i=2, and each right dimer literal (x,d,r) is the dual R703 input at i=m-3. Therefore any dimer choice immediately yields a labelled P4 or explicit R435 Reverse-Ear geometry. Outside those outputs, the four clauses must all choose their anchor literals, so the following four turns coexist:
(v,a,c), (v,c,a), (b,z,d), (z,b,d).
This is the BI-ANCHORS branch.

The logic is a trichotomy, not a closure theorem: BI-ANCHORS, a labelled P4, or Reverse-Ear geometry. The P4 and Reverse-Ear outputs remain visibly unconsumed here.

## Reverse-Ear activity is a baseline geometry, not closure

R910 proves a stronger baseline fact: every exact deletion cover of either crossed middle-gate pair is already Reverse-Ear active. For G_3={a,c}, fix either orientation S=(s_0,s_1). Accepted source geometry head-signs S by both endpoints, in particular (R,s_0,s_1) is tight. Let T=T_1 sqcup T_2 be any exact cover of H-S and let K be the T-rail containing R.

If R is terminal on K, with predecessor y, the HEAD-END seam rule gives (s_0,R,y) tight. This contains the adjacent state R y in the reverse order from K, so R435 gives explicit adjacent-state reversal geometry. If R is not terminal, let y be its successor. If y=q_i lies on Q, K encounters R=q_m and then q_i with i<m, a decreasing Q contact, so R435 applies. If y lies in the opposite gate pair G_4, choose its mate y'. The crossed right gate supplies (y',y,R) tight, whose state yR reverses the selected K state Ry; again R435 applies. These cases exhaust the cover.

For deletion of G_4 the proof is the exact left/right dual, using that either orientation of G_4 is tail-signed by L. A rail containing L either begins at L and receives the reverse outer seam, or has a predecessor lying on Q (decreasing contact) or in G_3 (a crossed-gate reverse state). Thus R435 is triggered in every case.

R483 supplies the necessary fence on interpretation: Reverse-Ear output existence is ubiquitous around path triples. Consequently R910 is useful source-labelled geometry but not a completed consumer. No P4/Reverse-Ear occurrence in this development is silently counted as branch closure.

## BI-ANCHORS: pending opposite-gate saturation

This section records the exact pending R917/P988 continuation of BI-ANCHORS and does not treat it as established. Suppose first that X union {v} is nonHamiltonian. R902 then gives an edge order realizing the five-vertex boundary tournament. The matching-height order on X yields
ab<ac<az, ab<bz<bc, cz<ac<bc, cz<bz<az,
and the BI-ANCHORS turns (v,a,c),(v,c,a) give av<ac and cv<ac.

To force (z,b,v), equivalently bz<bv, suppose bv<bz. If bv<cv then the edge sequence of (b,v,c,a,z) is bv<cv<ac<az; if cv<bv then (c,v,b,z,a) has cv<bv<bz<az. Either order is a tight Hamilton P5, contradiction. Hence bz<bv. To force (b,z,v), equivalently bz<vz, suppose vz<bz. If vz<av then (z,v,a,c,b) has vz<av<ac<bc; if av<vz then (a,v,z,b,c) has av<vz<bz<bc. Again either is Hamilton. Thus bz<vz. So, conditional on nonHamiltonicity of X+v, v tail-signs both orientations of the opposite gate pair {b,z}.

The right argument is dual but equally explicit. If X union {d} is nonHamiltonian, BI-ANCHORS gives bz<zd and bz<bd. If ac<ad, comparison of bd and ad produces Hamilton path (c,z,b,d,a) or (z,c,a,d,b), so ad<ac and (d,a,c) is tight. If ac<cd, comparison of zd and cd produces (a,b,z,d,c) or (b,a,c,d,z), so cd<ac and (d,c,a) is tight. Hence d head-signs both orientations of {a,c}.

Therefore the pending route says: on each side, either the inward five-set is Hamiltonian or the missing opposite-gate signs are forced; if both five-sets are nonHamiltonian, all eight inward gate-sign turns coexist. Neither alternative is asserted to close H, and R917 remains unusable until fresh review accepts it.

## The crossed m=6 packet is one finite argument

At m=6 write Q=(L,u,v,w,d,s,R), X={a,b,c,z}, and N=(v,w,d). We give the complete R875 packet argument at its natural scale. Pending P991 is the sectioned proof route carrying exactly this consolidation; accepted P951 remains canonical until P991 receives fresh review.

First, a local cover fact used below. If D is a tight physical dimer and T=T_1 sqcup T_2 is an exact two-cover of H-D supplied by R4, then H-D is not Hamiltonian, since a Hamilton path together with D would two-cover H. Neither T rail can be singleton: if T_1={r}, then R3 supplies a tight trimer on V(D) union {r}, and that trimer together with T_2 would two-cover H. Thus every exact dimer-deletion cover below has two nontrivial rails.

Apply the reusable R583 insertion-obstruction array at the unique internal gap w|d. If it yields two reverse-middle blockers, R584 produces a labelled tight reverse P4. This is outcome RM and is not by itself a closure theorem.

If R583 instead gives distinct right-terminal witnesses x,y with (s,d,x),(s,d,y), R723 supplies (x,s,d),(y,s,d). Hence both (x,s,d,y) and (y,s,d,x) are tight P4s on common middle dimer (s,d). In any exact H-{s,d} cover the rails are nontrivial by the preceding fact, so R843 gives HIGH (block count >2) or a source-visible reverse seam. This is RT.

The m=6 core-middle seam calculation is local to this proof. R817 supplies the four canonical core rails
A_1=(u,L,a,c), A_2=(u,L,c,a), B_1=(b,z,R,s), B_2=(z,b,R,s),
with every A_i disjoint from every B_k and A_i sqcup B_k an exact two-cover of the order-eight core. Hence N together with any chosen A_i,B_k partitions V(H). In each of the following concatenations the untouched core rail is the second path of a literal spanning two-path proposal. All internal turns away from the displayed seam are already certified. If both seam turns were tight, the proposal would two-cover H; therefore at least one seam turn is bad and R3 makes its reversal tight.

1. Append A_i after N: (v,w,d,u,L,...) has new turns (w,d,u),(d,u,L). Therefore E_A is (u,d,w) OR (L,u,d).
2. Prepend A_1 before N: (u,L,a,c,v,w,d) has new turns (a,c,v),(c,v,w). Therefore A_1 is (v,c,a) OR (w,v,c).
3. Prepend A_2 before N: (u,L,c,a,v,w,d) has new turns (c,a,v),(a,v,w). Therefore A_2 is (v,a,c) OR (w,v,a).
4. Append B_1 after N: (v,w,d,b,z,R,s) has new turns (w,d,b),(d,b,z). Therefore B_1 is (b,d,w) OR (z,b,d).
5. Append B_2 after N: (v,w,d,z,b,R,s) has new turns (w,d,z),(d,z,b). Therefore B_2 is (z,d,w) OR (b,z,d).
6. Prepend either B_k before N. The seam is (...,R,s,v,w,d), whose new turns are (R,s,v),(s,v,w). Therefore E_B is (v,s,R) OR (w,v,s).

These six clauses are simultaneous physical facts in the fixed frame. The hole lists are complete because each displayed support decomposition is a literal disjoint spanning partition. This is the full local calculation historically isolated as R839.

Now consider a left-terminal R583 packet: distinct x,y satisfy (x,w,v),(y,w,v) on D_L=(w,v). If {x,y}={b,z}, R849 tail-signs the same D_L by b,z, so (b,w,v,z) and (z,w,v,b) are both tight; R843 gives HIGH or reverse seam in any exact H-D_L cover. If {x,y}={a,c}, R849 tail-signs D_L by b,z and produces the full 2x2 head/tail signed rectangle; R846 gives HIGH, SEAM, CLOSE, or WEAVE.

If the head-witness pair is mixed, write {h,k} with h in {a,c}, k in {b,z}. For h=a use local clause A_2: either the literal core seam (v,a,c) is retained, or (w,v,a) makes a an additional tail witness. R849 already tail-signs k, and a,k are both head witnesses, so (a,w,v,k) and (k,w,v,a) form a bidirectional same-dimer P4 pair and R843 gives HIGH or reverse seam. For h=c use A_1 identically, producing either (v,c,a) or the paired-P4/R843 branch. This exhausts the left-terminal packet types.

It remains to normalize the quiet WEAVE branch. Let T=T_1 sqcup T_2 be a WEAVE cover of H-{w,v} from R846. Its rail starts are exactly a,c, its rail ends exactly b,z, and each rail is h -> E_h -> t for a nonempty exterior block E_h; the two blocks partition E={L,u,d,s,R}. Compare each T rail with Q using R435. If an old-state reversal, reverse trimer/contact, or vertex-simple tight cycle appears, retain that explicit R435 output. Otherwise the Q contacts on each T rail are increasing.

Under this monotonicity three same-rail pairs are forbidden. R594 gives (u,L,h) for h in {a,c}, so R3 makes (h,L,u) bad and L,u cannot share a weave rail. R594 gives (t,R,s) for t in {b,z}, so (s,R,t) is bad and s,R cannot share a rail. R723 gives (t,s,d), so (d,s,t) is bad and d,s cannot share a rail. Both exterior blocks are nonempty and partition five vertices. A 1+4 split is impossible because the four-block necessarily contains one of the forbidden pairs. Thus the block sizes are 2 and 3. Among d,s,R, two share a rail; since d,s and s,R are forbidden, that pair is exactly {d,R}, while s lies on the other rail. Finally L and u split. Up to exchanging the two rails, the only possible increasing contact partitions are
{L,d,R}|{u,s}  or  {u,d,R}|{L,s}.
This is the complete quiet-WEAVE normalization historically isolated as R847.

Therefore the R583 packet is exhausted exactly as R875 states: reverse-middle gives a labelled P4; right-terminal and the {b,z} left-terminal case give HIGH/SEAM through R843; the {a,c} case gives R846 HIGH/SEAM/CLOSE or WEAVE, with WEAVE reduced to explicit R435 geometry or the two monotone contact partitions; and the mixed case gives a literal core seam or HIGH/SEAM. This is a normal form, not a proof that the crossed phase closes. In particular the surviving P4, Reverse-Ear/R435, HIGH/SEAM, and monotone-WEAVE outputs remain consumers to be discharged elsewhere.

## Common inward-anchor recompletion

R862 introduces the exact cover of W=H-{q_2,q_{m-2}} and the five source cells used by the later recompletion theory. It is the bridge from first-depth gate information to arbitrary exact recompletions. The detailed five-cell classification and the block-preserving finite reconstruction interface are kept in separate developments because they answer different mathematical questions.

## What is still missing from the gate-phase interfaces

R904 rules out an intact-middle-only endgame from the listed crossed local core data. R483 rules out treating generic Reverse-Ear occurrence as closure. The ALIGNED and CROSSED branches therefore still need exact-cover consumers that convert their physical representative data into a literal two-cover or contradiction. This statement records the mathematical gap without choosing a tactical priority.

## Crossed gate saturation: the twelve source packets survive the failed payment conclusion

R648 is an instructive partial failure. Its table of twelve R542-ready packets in the crossed frame is correct; its final claim that every distinguished vertex becomes a universally preserved floor coordinate is not available noncircularly there, because that continuation invoked R224, whose reconstructible lineage runs through R169/R5/R24. The review therefore marked R648 needs_more_work rather than false.

R649/P728 is the repaired theorem and keeps exactly the valid native content. For S=(a,c), use carriers (z,c,a),(L,c,a),(R,c,a) with complementary singletons z,L,R and witness pairs {L,R},{b,R},{b,L}. For S=(c,a), use (b,a,c),(L,a,c),(R,a,c) with singletons b,L,R and witnesses {L,R},{z,R},{z,L}. For S=(b,z), use (z,b,c),(z,b,L),(z,b,R) with singletons c,L,R and witnesses {L,R},{a,R},{a,L}. For S=(z,b), use (b,z,a),(b,z,L),(b,z,R) with singletons a,L,R and witnesses {L,R},{c,R},{c,L}.

Every carrier is a tight trimer, the displayed S is exactly its reverse boundary dimer, and the two witnesses have the same required polarity and lie outside the carrier. Thus the twelve source packets coexist simultaneously in the fixed crossed frame. R649’s theorem is the simultaneous twelve-packet source saturation. R542/payment continuations are developed in D16 and are cited only when used.

## Native crossed-frame fences and path-shape constraints

Three results constrain how the long crossed phase can look without claiming closure.

R718/P795 is a finite non-propagation fence. It gives two complete six-vertex Strong orientations on X+{L,u}, both with transitive matching-height X, P5-free X+L and X+u, P6-free X+{L,u}, and the full star uLx for every x in X. In one model the outgoing M_S gate at u is the same physical edge as at L; in the other it is the complementary edge. Matching-height automorphisms realize all ordered gate-bit pairs. Hence the endpoint star and local P5/P6-freeness do not determine a one-step gate-bit propagation law.

R726/P803 goes in the opposite direction: despite that non-propagation, every x in X lies in some Hamilton P4 containing both physical endpoints L,R. Let r,s,l be the M_R,M_S,M_L neighbors of x. R3 chooses one of (R,x,L),(L,x,R). In either case, assume both r- and s-probe four-sets are P4-free. R518 supplies reverse contacts; four explicit P5-freeness deductions in X+L and X+R then produce a forbidden Hamilton P5. Thus one of {L,R,x,r} or {L,R,x,s} is Hamiltonian. The theorem is useful geometry, but bare P4 support remains too weak to close the branch.

R837/P911 is a path-shape theorem for the crossed gate dimers G_3={a,c}, G_4={b,z}. If an oriented G_3 occurs consecutively inside a tight path and has a successor y, the path gives a tail sign on that tested dimer while R649 supplies a fixed distinct head witness; R518 forces a labelled P4. Therefore absent that P4, G_3 can occur only as a terminal block. Dually, absent a labelled P4, G_4 can occur only as an initial block. This is graph-intrinsic endcap geometry, not a claim that such P4 output is itself closure.

## The crossed 4+4 core gives a direct deep-gap trichotomy

R820 is a durable crossed-core theorem with an important proof-history correction. The four core P4s are A_1=(u,L,a,c), A_2=(u,L,c,a), B_1=(b,z,R,s), B_2=(z,b,R,s). Fix a deep gap q_j|q_{j+1} of N=Q[2,m-2]. Insert A_1 and A_2 directly at that gap. For A_1 the complete new seam window is (q_{j-1},q_j,u), (q_j,u,L), (a,c,q_{j+1}), and, when present, (c,q_{j+1},q_{j+2}); A_2 has the same first two seams and replaces the last two by the a/c-swapped versions. Since a successful insertion together with a complementary B_k would two-cover H, each insertion must have a bad new turn. Reversing the holes with R3 yields exactly U_j OR G_AC(j) OR T_AC(j), with the terminal T term absent at j=m-3. Inserting B_1,B_2 gives the dual V_j OR G_BZ(j) OR T_BZ(j).

This direct proof is P919 and uses only R3 and the crossed core geometry R621. The older alternate proof P895 was once accepted but is now invalid because it delegated the seam window to R811, whose exterior-position formula omitted a second junction turn. That defect does not invalidate R820: P919 rederives the full internal windows literally and is the selected fully reconstructible route. The history is preserved because it is a canonical example of a theorem surviving the failure of one proof route.

## Signed rectangles and the m=6 packet: exact repair genealogy

Two repair chains are central to the present crossed m=6 argument.

R658/P736 correctly constructed synchronized inward signed rectangles, but its m=6 interpretation was false: when S_L=(q_3,q_2) and S_R=(q_4,q_3) hinge at q_3, R547 produces only a static opposite-sign singleton pair unless the ancestor dimers already belong to a certified payment lineage. R658 incorrectly called that raw hinge a floor. R849/P924 repairs exactly this point. The rectangle construction is unchanged: b,z tail-sign both (L,u) and (q_3,q_2); a,c head-sign both (s,R) and (q_{m-2},q_{m-3}). At m=6 the conclusion is only the graph-intrinsic hinged singleton pair. For m>=7 the dimers are physically disjoint and their mass-four balanced pair legitimately enters the external payment theorem R514.

R845/P920 then attempted the full crossed m=6 packet normal form. Its main case decomposition was useful, but the route had two audit defects: it inherited an incorrect seven-shape count from R825, and applications of R833 silently required exact dimer-deletion covers to have both rails nontrivial. It also still cited invalid R658. R875/P951 repairs all three. It first proves dimer-deletion rail nontriviality directly: a singleton rail plus the deleted dimer spans a tight trimer, which together with the other rail would two-cover H. It replaces the repeated R833 compatibility argument by R843, uses corrected R849, and uses R846/R847 for the full signed-rectangle WEAVE branch. This is the accepted normal form expanded in the m6 section above.

R860 and R861 are later abandoned editorial duplicates of accepted R843 and R846 respectively. They changed only stale application references from R658 to R849; their theorem statements/proofs are mathematically the same. They therefore receive explicit duplicate disposition rather than parallel exposition.

## First-depth compression history: preserve source clauses, retire unnecessary corridors

Several successive attempts compressed crossed pair-deletion geometry before the current R911/R914 interface. Their valid mathematics is worth retaining even though the standalone layers were retired.

R720/P797 specializes the general END branch of an R696 short-carrier deletion cover. In the one-hole orientation the forced reverse literally reverses the selected singleton-exterior state. In the two-hole orientation, one reverse either reverses a selected boundary state on the pure exterior rail or gives opposite polarity on the exact tested middle-gate dimer; combining that opposite sign with one of the fixed R649 endpoint witnesses via R523 yields a labelled P4. Thus a crossed END clause is never merely an anonymous mate clause: it is selected-state reversal geometry or a labelled P4. This remains a correct superseded interface.

R912/P983 proposed a stronger global corridor: first-depth clauses, followed by R873 propagation, either yielded anchors/P4 or an all-X signature-00 corridor. The mathematics was coherent, but the layer was abandoned because R911 already exposes the exact first-depth clauses and a first inward dimer witness can be consumed directly. R913/P984 removed the 00 corridor from the conclusion but still carried unnecessary propagation. R914/P985 is the final clean parent: derive the four two-hole first-depth clauses directly; every dimer literal is already an R703 hypothesis, hence yields P4 or Reverse-Ear geometry; outside those outputs all four BI-ANCHOR turns are forced simultaneously.

R916/P987 is a separate pending pre-split corollary. R596 gives the distinguished left inward turn (q_3,q_2,x_L), exactly R703 form (L) at i=2, so R703 yields a first-depth P4 on {q_1,q_2,q_3,x_L} or Reverse-Ear geometry; the right side is dual. The proof is short and dependency-complete, but the revision is still pending and this document does not promote it.

## R714 is a theorem with a broken only proof, not an established Hamiltonicity fact

R714 is deliberately preserved as an integrity warning. Its statement says that for every x in X, both {q_1} union (X-{x}) and {q_{m-1}} union (X-{x}) are Hamiltonian P4-supports. The only proof P791 first asserts that X+q_1 is P5-free because a Hamilton P5 there together with Q[2,m] would two-cover H. But those supports cover only V(H)-{q_0}; q_0 is omitted. Dually, (X+q_{m-1}) together with Q[0,m-2] omits q_m. Therefore neither displayed pair contradicts pc(H)>2.

The proof consequently does not establish the needed inward-five-set P5-freeness, and its subsequent use of the two-no-P4 extension theorem cannot prove the claimed P4s. The claim revision remains marked mathematically valid rather than disproved, but with its only proof invalid it is currently unusable. No result in this migration may silently use R714 as established. A genuinely independent replacement proof could still repair the theorem later.

## Before the first-step zipper, crossed endpoint stars already forced P4 and support-coupling geometry

The crossed program first tried to turn signed inward dimers directly into local P4s. R704 is historically important but currently unusable: its only proof P781 depended on the invalid R658 rectangle revision. R858/P933 is the dependency-migrated version using corrected R849. Its local mathematics is valid, but the result was abandoned because it still ends only in P4 manufacture and no live theorem requires it. The migration therefore preserves R704 as an invalidly-supported predecessor and R858 as its valid-abandoned repair.

A cleaner endpoint route appeared as R709/R710. R709 was a valid first version and was abandoned when R710/P787 removed unnecessary hypotheses. In the synchronized crossed frame, the high-side roots and the generic trimer/contact theorem R518 give, independently at each end, either a Hamilton P4 immediately or an exact reverse contact that concatenates with the root turn to a canonical P4 such as (q_3,q_2,x_L,q_0), with the right-side dual. R710 is accepted but retired because later source interfaces expose stronger cover-valued data.

R715/P792 couples the first inward vertices before any zipper selection. On X union {q_1,q_{m-1}}, the two five-sets containing one inward coordinate cannot be Hamiltonian for literal two-cover reasons. The four-of-six theorem R195 then forces the four remaining root-omission five-sets to be Hamiltonian. This is support geometry, not a closure theorem.

Three nearby results are strategy fences. R719/P796 observes that feeding a cross-end trimer into Reverse Ear merely reproduces already-known endpoint stars, so that move creates no new currency. R721/P798 gives an explicit eight-vertex Level-(1) orientation satisfying a full left crossed/high-side packet, the historical rectangle turns, and an explicit labelled P4, yet with no Hamilton P8. Thus even substantial one-sided local path abundance does not close the frame. R724/P801 is a valid orientation-specific cross-end-trimer-to-P4 theorem, retired because the stronger accepted R726 subsumes it. Together these results explain why the program moved from raw P4 generation toward exact-cover zipper states.

## The crossed first-step zipper is an exact root-switch mechanism, not a terminal progress measure

R725/P802 is the native first-step producer. From the universal R723 reverse stars, each physical side yields either an exact root-switch ADV cover or an outer-matching saturation packet. On the left, for example, one ADV representative has a short rail beginning (v,u,a,...) after deleting c, with the dual root a case; the right side is symmetric. If the ADV alternative fails, the matching-labelled turns (b,a,u),(z,c,u) or their duals are forced. R727/P804 consumes precisely that saturation alternative through the no-P4 signature theorem and turns it into a labelled P4. Hence each side is ADV-or-P4.

R729/P806 explored iterating ADV as a literal zipper. The first advance creates a three-boundary root ladder, but antisymmetry blocks naive repetition with the same root. This valid observation was abandoned as a global route. R730/P807 gives the sharper interpretation that survived: an ADV is a same-root reversal between two exact deletion-cover representatives, together with a shield at the next physical Q boundary. R731/P808 compares those same two representatives and identifies two support-crossing states in opposite comparison directions. R176 is the separate cross-state birth theorem; this section retains the exact representative pair and its cross states.

R734/P811 shows that an ADV also self-mints a two-witness short-carrier packet. For a left ADV with deleted root r, the advanced trimer K=(v,u,x) has reversed boundary dimer (u,v). The original Q vertex w=q_3 is one witness. Reinserting r at the same rail end would two-cover H, so R3 supplies r as a second witness of the same polarity. Thus the exact hypotheses of R696 hold; the right construction is dual. This compiles ADV directly into the external END/FREE/SANDWICH consumer without generic payment.

Several later P4 compressions were mathematically sound but strategically retired. R735/P812 turned ADV-or-P4 into P4-on-each-side; it was abandoned after R829 made clear that local P4 production is not a closure engine. R738/P815 obtained the same conclusion even more directly from R723 plus the generic two-probe trimer amplifier R700 and same-support sign interaction R523. R745/P822 further showed every exterior vertex can be absorbed into a first-inward P4, but was likewise abandoned as pure local path abundance. R736/P813 is the matching explicit fence: a fully specified seven-vertex Level-(1) orientation satisfies the crossed endpoint/gate/star packet and contains both R727 P4s, yet no six-set obtained by deleting an X-root has a Hamilton P6. The certificate proves that the P4 branch cannot simply be extended locally into a cover-valued root advance.

The durable lesson is therefore exact rather than heuristic: ADV carries representative reversal, next-boundary shielding, cross-state provenance, and a source-localized two-witness packet. Bare P4 abundance, even universal abundance, is not counted as progress.

## Every long crossed frame contains one fixed pc=2 order-ten core coupled to the middle rail

R806/P882 is the clean elevator theorem for the long crossed phase. For m>=6 put G=H[X union {L,u,v,d,s,R}] and M=Q[3,m-3]. The six named Q vertices are distinct and X is disjoint from Q, so |G|=10 and V(H)=V(G) disjoint-union V(M). The interval M is a nonempty tight path. Minimality gives pc(G)<=2. If G were Hamiltonian, its Hamilton path together with M would two-cover H, so pc(G)=2. Therefore every exact two-cover G=A sqcup B gives the literal minimum three-cover A sqcup B sqcup M of H.

This representation is especially useful because all bounded punctures used by the deep-crossing theorem R803, namely D_L={d,v,u}, D_R={s,d,v}, and D_F={u,v,d,s}, lie inside the same fixed G while M is untouched. Thus the variable-order problem can be viewed as a fixed pc=2 ten-core interacting with one long Hamilton rail. This does not make G a smallest counterexample and does not license applying the global order-ten counterexample theorem to G.

R807/P883 supplies a small but important endpoint interface for those punctures. In C_L=X union {L,s,R}, probe the crossed gate trimer (L,c,a) with s using R518. The P4 branch pairs with (b,z,R); the no-P4 branch yields the reverse contact (c,L,s), which pairs with (a,b,z,R). Either way C_L has an exact two-cover exposing R as a rail endpoint. The dual construction on C_R=X union {L,u,R} exposes L. These are literal endpoint-exposing covers, not uniqueness statements.

## Crossed endcaps normalize to physical endpoints, while m=6 forces a twenty-turn outer fan

R840/P913 turns the one-way endcap theorem R837 into a bounded attachment statement. If an oriented G_4={b,z} block occurs at the beginning of a tight rail, its next Q vertex is a sign witness on that tested X dimer; if the neighbor is interior to Q, the generic inward-witness theorem R682 immediately yields its nonlocal capture/cross-end output. Thus outside that output the neighbor must be L or R. Dually an intact terminal G_3={a,c} block has only L/R as its safe preceding Q contact. If both blocks lie on one rail and Reverse Ear R435 is also absent, their Q contacts must respect increasing Q order, so only (L,L),(L,R),(R,R) remain. The forbidden pair (R,L) is itself reverse-order geometry. This is a fixed three-state endpoint normalization independent of m.

At m=6, R841/P915 produces much more explicit native data. Twelve first-layer one-hole spanning proposals force c s R, a s R, L u b, L u z, c R z, c R b, a R z, a R b, c L z, c L b, a L z, a L b. Eight second-layer proposals, each using one newly certified turn plus the original matching/gate/star data, force c z R, R c b, a b R, R a z, c z L, L c b, a b L, L a z. Every item is the exact reversal of the sole uncertified turn in a literal spanning two-path proposal. Hence all twenty turns coexist graph-intrinsically.

R841 is not itself the m=6 closure. Its value is that it turns the finite cap geometry into a simultaneous exact outer fan that later Mate-Fork, endpoint, or gap-clause consumers may use without rediscovering the one-hole ledger.

## Endpoint rotations force a genuinely deep two-witness packet on both sides

R905/P976 is a current native consequence of the crossed singleton-deletion representatives and is stronger than a bounded-core-only observation because its certificates reach the first deep rail coordinates. Let t=q_3,h=q_4 on the left and r=q_{m-3}, ell=q_{m-4} on the right.

For H-z and H-b, rotate the first vertex v=q_2 of the long deletion rail to its end. The two resulting Hamilton-candidate orders have exactly the three possible holes (c,b,t)/(b,t,h)/(s,R,v) and (a,z,t)/(z,t,h)/(s,R,v). Since either Hamilton path plus the deleted singleton would two-cover H, each candidate has a bad hole; R3 yields the simultaneous clauses
(t,b,c) OR (h,t,b) OR (v,R,s),
(t,z,a) OR (h,t,z) OR (v,R,s).
Case analysis on those two clauses produces one of four genuine same-polarity two-witness packets: a cross-end packet on reverse dimer (R,s), a matching-labelled packet on (b,c) or (z,a) with deep witness t, or the deep Q packet on (h,t) with witnesses b,z.

The exact dual rotation in H-c and H-a gives
(u,L,d) OR (a,r,ell) OR (b,a,r),
(u,L,d) OR (c,r,ell) OR (z,c,r),
and therefore one of four right-side packets, again either cross-end, matching-labelled with deep witness r, or on the deep Q dimer (r,ell). The left and right conclusions coexist in the fixed frame.

Each packet is exactly an input type for the generic two-witness short-carrier theorem R696, but the proof of R905 itself uses only the literal R621 covers and boundary antisymmetry. It therefore records a genuine smallest-counterexample obstruction to local witness models such as R904 without claiming that any particular R696 descendant closes the crossed phase.

## ALIGNED: common-fiber concatenation forces gate anchors or universal inward stars


Retain the established ALIGNED frame and notation of `aligned-fiber`: X={a,b,c,z}, Q=(q_0,...,q_m), m>=6, L=q_0,u=q_1,v=q_2,t=q_3,r=q_{m-3},d=q_{m-2},s=q_{m-1},R=q_m. Accepted R899 gives four exact two-covers of the common residue H-{b,z}. Because (b,z) is itself a vacuous tight dimer, H-{b,z} cannot be Hamiltonian: a Hamilton path of that residue together with (b,z) would be a spanning two-cover of H.

Concatenate the two rails of the first left representative
T_L^a=(u,L,a,c) sqcup Q[2,m]
in the displayed order. The Hamilton candidate
(u,L,a,c,v,t,q_4,...,R)
has exactly two uncertified turns, (a,c,v) and (c,v,t). They cannot both be tight, so R3 gives the physical clause
(v,c,a) OR (t,v,c).
The second left representative gives, identically,
(v,a,c) OR (t,v,a).

The two right representatives give the dual pair of clauses on the same surviving gate pair. Concatenating
T_R^c=Q[0,m-2] sqcup (a,c,R,s)
yields the Hamilton candidate
(L,u,...,r,d,a,c,R,s),
whose only holes are (r,d,a) and (d,a,c). Hence
(a,d,r) OR (c,a,d).
Likewise T_R^a=Q[0,m-2] sqcup (c,a,R,s) gives
(c,d,r) OR (a,c,d).
All four clauses are graph-intrinsic consequences of the one common exact H-{b,z} fiber; no representative synchronization beyond R899 is asserted.

Now combine them with the four inward stars already established in `aligned-fiber`:
(t,v,b), (t,v,z), (b,d,r), (z,d,r).
At the left there is an exact dichotomy:

* **LEFT-GATE.** At least one of (v,c,a),(v,a,c) is tight. Thus v is a head witness on at least one tested orientation of the surviving M_S gate {a,c}.
* **LEFT-UNIVERSAL.** Neither gate-anchor literal is tight. Then the two clauses force (t,v,c) and (t,v,a). Together with (t,v,b),(t,v,z), the reverse Q dimer D_L=(t,v) is tail-signed by every x in X.

Dually, at the right:

* **RIGHT-GATE.** At least one of (c,a,d),(a,c,d) is tight. Thus d is a tail witness on at least one tested orientation of {a,c}.
* **RIGHT-UNIVERSAL.** Neither gate-tail literal is tight. Then the clauses force (a,d,r),(c,d,r), and together with (b,d,r),(z,d,r), the reverse Q dimer D_R=(d,r) is head-signed by every x in X.

Hence every ALIGNED counterexample lies in one of four global regimes LEFT-GATE/LEFT-UNIVERSAL crossed with RIGHT-GATE/RIGHT-UNIVERSAL. This is a cover-valued refinement of the synchronized R703 normal form: the dimer alternative does not merely exhibit Reverse-Ear geometry, but saturates the corresponding inward reverse Q dimer by all four physical X witnesses.

Two immediate consequences should be retained without overinterpreting them. If both universal branches occur and m>=7, D_L and D_R are physically disjoint opposite-polarity dimers, with every x in X available as a common source witness. Accepted R514 therefore supplies a genuine mass-four balanced-pair continuation to closure or an ancestry-bearing both-singleton floor, while the four-witness source geometry remains historical certificate data. At m=6 the two supports hinge at t=r, so accepted R547 instead gives the raw opposite-sign singleton pair on the nonhinge vertices v,d; this is not automatically a paid floor. If both gate branches choose the same tested orientation of {a,c}, they concatenate to a literal inward P4, either (v,a,c,d) or (v,c,a,d). Mixed tested orientations require a separate consumer.


### Literal cut shift and the immediately blocked next seam

Here LEFT-UNIVERSAL denotes the no-gate branch defined above, not merely the weaker assertion that all four reverse-dimer signs happen to hold. Its two absent gate turns reverse by R3 to (a,c,v) and (c,a,v). Consequently it gives two literal exact covers of the SAME residue:
  (u,L,a,c,v) sqcup Q[3,m],
  (u,L,c,a,v) sqcup Q[3,m].
Only one turn was added to each short rail; the suffix remains a tight subpath of Q. Exactness follows because H-{b,z} is nonHamiltonian, as proved above.

This advance cannot be repeated by appending the next Q vertex while preserving the displayed orders. The already forced turns (t,v,c) and (t,v,a) make (c,v,t) and (a,v,t) bad, respectively. These are precisely the new turns required to append t=q_3 to the two shifted rails. Thus the no-gate branch supplies an advance AND an immediate obstruction to the next unchanged-order advance.

Dually, RIGHT-UNIVERSAL reverses the absent turns (c,a,d),(a,c,d) to (d,a,c),(d,c,a), yielding the exact covers
  Q[0,m-3] sqcup (d,a,c,R,s),
  Q[0,m-3] sqcup (d,c,a,R,s).
The forced turns (a,d,r),(c,d,r) make (r,d,a),(r,d,c) bad, so prepending r=q_{m-3} to the displayed short rails is impossible. All these assertions hold at m=6 as well; no disjointness of the two inward dimers is used.

The left shifted covers retain a useful restoration test. For h=c use the first shifted rail, and for h=a use the second. Appending (b,z) to its end gives a literal spanning two-path proposal with untouched Q[3,m], having exactly the two new turns (h,v,b),(v,b,z). Appending (z,b) instead has exactly (h,v,z),(v,z,b). Antisymmetry and pc(H)>2 therefore give simultaneously
  (b,v,h) OR (z,b,v),
  (z,v,h) OR (b,z,v),  for h=a,c.
Hence either v tail-signs at least one tested orientation of the deleted pair {b,z}, or all four turns (b,v,a),(z,v,a),(b,v,c),(z,v,c) are tight. This is a disjunction of physical certificates, not a Hamiltonicity conclusion.

The underlying two-hole mechanism is independent of the labels. In any nonHamiltonian residue with a tight two-cover A sqcup (v,t,...), where A ends (...,a,c), the candidate concatenation has holes (a,c,v),(c,v,t). If (v,c,a) is bad, the first hole is tight, so the second must be bad. Moving v to A is legal and its next direct extension by t is blocked. The ALIGNED calculation applies this elementary mechanism simultaneously to two representatives of one fiber.

Scope and status: these are direct internal reconstructions from R3, R4, R619 and R899, not a newly accepted standalone theorem. They do not exclude advances that reorder a rail, change its terminal ordered pair, exchange vertices between rails, or change deletion residue. They do not assert that two independently available left/right advances compose. The analogous shield after crossed ADV is developed separately in first-step-zipper-archaeology; that argument is a comparison, not a dependency here.

The unresolved ALIGNED task has therefore narrowed: consume these four global regimes together with the original R619/R899 deletion representatives. Generic payment or bare P4 production alone is not counted as closure.


## Phase-free inward-pair floor and internal-middle interaction front door

Assume the surviving long R24-failure frame supplied by the accepted reconstruction entrance, so X has four vertices, Q=(q_0,...,q_m) with m>=6, and write L=q_0,u=q_1,v=q_2,t=q_3,r=q_{m-3},d=q_{m-2},s=q_{m-1},R=q_m. The following argument does not use the ALIGNED/CROSSED gate orientation.

Put D={v,d} and W=H-D. Partition the four exterior vertices X into any two physical pairs E_3,E_4; each pair, in either orientation, is a vacuous tight dimer. Together with
G_0=Q[0,1],  G_1=Q[3,m-3],  G_2=Q[m-1,m],  G_3=E_3,  G_4=E_4,
these give five nonempty pairwise disjoint tight paths whose supports partition W. At m=6 the middle cell G_1 is a singleton, which causes no degeneracy.

Accepted Pair-Deletion Rigidity R429 supplies an exact two-cover T of W. Apply the intrinsic partition-cover deficit identity R7 to the five source cells and T. If t_G(T) is the number of T-selected states crossing between distinct G_i, then
t_G(T)=5-2+sigma_G(T)=3+sigma_G(T)>=3.
Choose any one selected intercell state xy. Relative to the literal five-cover G_0 sqcup ... sqcup G_4, xy joins two distinct source components. Since W is proper, accepted R176 applies. Choose v (or, symmetrically, d) as the spare vertex outside W. The fully reconstructible R176 construction yields a graph-intrinsic balanced opposite-sign pair with singleton support (v) and with the opposite support of order at most two: if the source component containing x is nontrivial, R176 uses one literal source neighbor of x and produces a signed dimer; if it is singleton, the opposite support is singleton already. Therefore, in a hypothetical smallest counterexample, either we already have a both-singleton ancestry-bearing pair or accepted R428, with (v) fixed, pays the opposite nontrivial support to singleton width unless a spanning two-cover occurs. Thus every long synchronized R24 failure has a genuine ancestry-bearing mass-two floor, obtained without gate classification, capture, five-cell shape analysis, or a raw R547 hinge.

Accepted R432 may now steer this genuine floor to the prescribed physical inward pair {v,d}, unless H is already two-covered. After steering, choose a fresh exact two-cover T* of H-{v,d} by R429. Its residue has |W|=m+3>=9 vertices and the two rails are nontrivial. A two-path forest has only four rail endpoints. Among the m-1>=5 surviving Q vertices Q\{v,d}, at least one, call it x, is therefore internal on a T* rail. By boundary antisymmetry R3 exactly one of (v,x,d) and (d,x,v) is a proper tight turn J with outer pair {v,d}. The active floor is already aligned to the outer pair of J, and x has both a selected predecessor and selected successor in the same literal T* frame. Accepted R442 therefore applies immediately: the predecessor and successor selected-incidence birth channels coexist in that one frame, and unless a spanning two-cover occurs their two nontrivial balanced-pair births enter accepted R441 cross-generation interaction. Hence every long synchronized R24 failure yields either a spanning two-cover or a role-bearing R441 output whose fixed turn has middle x on the original physical long rail Q and outer pair exactly {q_2,q_{m-2}}.

This gives a phase-free parent reduction:
R24 failure -> inward-pair cross-state -> genuine paid floor -> floor {q_2,q_{m-2}} -> old-Q internal middle -> R442/R441 interaction.
The ALIGNED/CROSSED split is unnecessary for reaching this interface. In ALIGNED there is an even shorter redundant entrance: the accepted R899 left and right exact covers of H-{b,z} have visibly different rail-support partitions, so accepted R410/R176 already births a small balanced pair before any gate clause or zipper analysis; R428 again pays it to a floor.

The reduction does NOT close R24. R441 deliberately ends in strict support descent/contact, fused or strict signed growth, a vertex-simple tight cycle, bounded reverse/contact or signed-BB geometry, or bounded-small output. None is automatically a contradiction. The sharpened common target is therefore the following stretch theorem: in the synchronized four-exterior frame, an R442 two-birth interaction whose fixed-turn outer pair is {q_2,q_{m-2}} and whose middle is a surviving old-Q vertex cannot terminate in a nonclosing R441 output. Proving that inward-pair two-birth absorption theorem would close the long R24 case in both ALIGNED and CROSSED phases at once. It should be attacked by consuming the two R441 source mechanisms, overlap via R436 and disjoint checkerboard via R440, with the retained original-Q role of the fixed middle and the four-exterior frame still graph-intrinsic.

### Fixed-frame bilateral absorber strengthening

Retain the phase-free inward-pair setting above: D={v,d}={q_2,q_{m-2}} and fix one literal exact two-cover F of H-D. Let b be any internal vertex of one F-rail, with literal consecutive host neighbors l,b,s, so (l,b,s) is tight. Boundary antisymmetry gives exactly one proper tight turn J_b on {v,b,d}; orient notation so J_b=(v,b,d), with the reverse case obtained by swapping v,d.

Apply accepted R700 (equivalently source-preserving R768) to J_b with the two literal probes l,s. If either probe is in the P4 branch, retain that role-labelled P4 on J_b plus one actual host neighbor. If both probes are no-P4, then simultaneously the reverse initial dimer S_L=(b,v) is tail-signed by both l,s and the reverse terminal dimer S_R=(d,b) is head-signed by both l,s. These two packet facts coexist graph-intrinsically and use the actual selected neighbors of b from F. R768 additionally retains a Hamilton P5 on {l,v,b,d,s}, but no currentization of that P5 is asserted.

Refine either boundary packet by accepted R696 in an arbitrary exact support-deletion cover. END is not terminal: accepted R785 compiles every two-witness END packet to either a selected-state reversal or a literal P4. SANDWICH is also eliminated in this bilateral source-labelled setting. For S_L=(b,v), complementary singleton d and witnesses {l,s}, SANDWICH gives either (l,d,s) or (s,d,l). But the opposite R700 packet S_R=(d,b) already has graph-intrinsic certificates (l,d,b) and (s,d,b). If SANDWICH is (l,d,s), its state d->s is exactly reversed by s->d inside (s,d,b). If SANDWICH is (s,d,l), its state d->l is exactly reversed by l->d inside (l,d,b). Thus every S_L-SANDWICH output is an explicit source-labelled selected-state reversal/R435 geometry. The exact dual eliminates S_R-SANDWICH using the S_L certificates.

Therefore, after excluding explicit P4/reversal geometry, BOTH boundary packets are forced into R696 FREE. Concretely there exist alternative exact pair-deletion covers T_L of H-{b,v} and T_R of H-{d,b} such that d has in T_L a selected crossing {d,x_L} with x_L outside {l,s}, and v has in T_R a selected crossing {v,x_R} with x_R outside {l,s}. Each physical crossing avoids both literal host witnesses l,s, so accepted R527 may capture the complementary singleton using either witness in its own side fiber. No coexistence of the two capture descendants is asserted, and neither crossing is transported back into F.

Hence one fixed inward-pair host F and one internal b satisfy the sharper normal form

    role-labelled P4 / selected-state reversal geometry
    OR
    bilateral FREE side-fiber crossings avoiding both literal host neighbors.

This is strictly narrower than generic R441/R445 output and preserves the physical triple {v,b,d}, the same original host rail, and both host-neighbor identities l,s. It also explains why bare R523/R285 spoke interaction is insufficient: the useful datum is the simultaneous two-boundary packet on the SAME trimer J_b with the SAME literal witness pair {l,s}.

Fences: R542 is used only on the exact reverse tested orientations (b,v) and (d,b); the two R696 descendants live in different deletion fibers and need not coexist; the R768 P5 is graph-intrinsic but is not automatically a current replacement of l-b-s; this argument does not address coherent pair-deletion selection or global Phi repair.

The remaining local stretch target is a Bilateral-FREE Absorption Theorem: in the synchronized inward-pair frame, the two side-fiber FREE crossings forced from one internal host vertex cannot both persist without an actual spanning two-cover or a source-order reversal that currentizes against F. Proving it would consume both protected-return and generic geometric-output branches of the phase-free O6 entrance without an ALIGNED/CROSSED split.

### Common-triple residue and saturated terminal shields

Retain the fixed-frame bilateral-FREE branch above, and now exclude the already-separated role-labelled P4/selected-state-reversal outputs. The R696 conclusion is then universal, not merely existential. For S_L=(b,v), every exact two-cover of H-{b,v} must lie in FREE: END would trigger accepted R785, and SANDWICH would be an explicit source-labelled reversal by the opposite S_R packet. Hence d is internal in EVERY exact H-{b,v} two-cover. Dually, v is internal in EVERY exact H-{b,d} two-cover.

Put T={b,v,d}. Since J=(v,b,d) is tight, H-T cannot be Hamiltonian: a Hamilton path on H-T together with J would two-cover H. Smallest-counterexample minimality R4 gives pc(H-T)<=2, so pc(H-T)=2. Fix one exact common-residue cover C=U sqcup V of H-T. Neither rail can be a singleton. Indeed, if U=(u), then the dimer (d,u) together with V is an exact H-{b,v} two-cover exposing d, contradicting universal d-internality; the v-dual gives the same contradiction. Thus both U,V have order at least two, without R24,R5,or R168.

Write U=(u_1,...,u_r), r>=2. Universal d-internality forbids attaching d at either end of U: (d,u_1,u_2) and (u_{r-1},u_r,d) are bad. R3 therefore gives the reverse shields (u_2,u_1,d) and (d,u_r,u_{r-1}) tight. Universal v-internality gives simultaneously (u_2,u_1,v) and (v,u_r,u_{r-1}) tight. The same holds at both ends of V. The third trimer vertex b has, at each physical rail end, an exact CAP-or-SHIELD alternative by R3: either b attaches there, producing an actual exact H-{v,d} cover with b exposed, or b joins v,d as a third same-polarity reverse shield on that terminal dimer.

A useful pure amplification explains the fully shielded subcase. Let a tested oriented dimer (p,q) carry three distinct tail witnesses x,y,z, so (p,q,x),(p,q,y),(p,q,z) are tight. If every four-set {p,q,x,y},{p,q,x,z},{p,q,y,z} were P4-free, apply accepted R518/R516 to the trimer (p,q,x) with probe y: its no-P4 reverse contact gives (y,x,q) tight. Swapping x,y gives (x,y,q) tight, and repeating over all witness pairs gives (alpha,beta,q) tight for every ordered distinct alpha,beta in {x,y,z}. R3 on {x,y,z} gives either (x,y,z) or (z,y,x); in the first case (x,y,z,q) is a P4, and in the second (z,y,x,q) is a P4, contradiction. Thus three same-tail witnesses force a P4 on the three witnesses plus q. The head-signed dual is exact.

Applied at a fully shielded left end of U, the three witnesses are {b,v,d} on (u_2,u_1), so {u_1,b,v,d} has a Hamilton P4 ending at u_1. This does NOT yet close: appending the old suffix u_2,u_3,... leaves one new seam whose bad reverse is exactly the pre-existing shield of the final witness. Thus the terminal P4 is a saturated obstruction, not fresh augmentation. This identifies the precise quiet species: either a b-CAP produces a same-fiber endpoint/internal comparison against the fixed host F, or every end is triply shielded and the forced P4s are blocked tautologically by the same shields that created them.

This common-source formulation is noncircular and uses only R3,R4,R518/R516 plus the already-established bilateral packet reduction. It reconstructs the useful multi-internal terminal-shield geometry without importing historical R168-dependent triple-return routes. The next absorption step must break the tautological shield by moving the obstruction to an adjacent physical dimer, or consume the b-CAP same-fiber endpoint/internal comparison into an actual cover exchange. Generic payment or bare R435 output does not suffice.

### Actual-neighbor FREE exchange and signature incompatibility

The bilateral FREE side fibers admit a stronger source-cover consumer than generic capture. Retain J=(v,b,d), and consider any exact cover T_L of H-{b,v}. In the geometry-quiet FREE regime d is internal, so orient its rail locally as (...,p,d,q,...). Replacing the selected singleton d by the missing tight trimer in its source order gives the literal spanning-cover proposal (...,p,v,b,d,q,...), with the other T_L rail unchanged. Every old turn survives; the only new turns are (p,v,b) and (b,d,q). Hence pc(H)>2 forces the exact physical mate clause

    (b,v,p) tight  OR  (q,d,b) tight.

This clause lives on the two reverse boundary dimers of the SAME J. In particular, if one of p,q is outside the old witness pair {l,s}, the only way to avoid a genuinely new boundary witness is for the old-neighbor side of the clause to win; then the opposite seam is actually tight and the proposed insertion fails at exactly the old R700 witness seam. The exact v-side dual holds for every exact T_R of H-{d,b}: if (...,p,v,q,...) is selected, the same replacement (...,p,v,b,d,q,...) yields the same mate clause (b,v,p) OR (q,d,b).

Now probe J by the two ACTUAL neighbors p,q of the internal side vertex. If either four-set J+p or J+q has a Hamilton P4, retain that P4 with its actual selected-neighbor role. Suppose both are no-P4. Accepted R522 says their R516 signatures agree and gives an explicit P5. Compare that P5 with the actual side-cover rail by accepted R435.

For the d-side turn p,d,q, signatures 00 and 10 give R522 order d,p,v,q,b or d,q,v,p,b; signature 11 gives d,p,b,q,v or d,q,b,p,v. In every one of these cases the P5 encounters the T_L contacts p,d,q out of their selected order, so R435 yields an exact selected-state reversal, reverse trimer, or proper-cycle output. The ONLY no-P4 signature that can remain order-quiet is 01. Since p,d,q itself is tight, R522 then chooses the unique order

    K_d=(b,p,d,q,v),

whose internal trimer is literally the selected FREE segment.

For the v-side turn p,v,q the calculation is complementary. Signatures 00 and 10 use the R522 comparison at middle v, so the selected turn forces the quiet P5

    K_v=(d,p,v,q,b).

Signatures 01 and 11 encounter p,v,q out of selected order and therefore trigger R435. Thus a no-P4/order-quiet d-side FREE cover requires common signature 01, while a no-P4/order-quiet v-side FREE cover requires common signature 00 or 10.

But the no-P4 signature is graph-intrinsic to the fixed core J: R522 proves that any two no-P4 probes of J have the same R516 signature. The original host probes l,s are already joint no-P4 probes in the bilateral-FREE branch, so they fix one signature sigma_J for all later no-P4 probes. Consequently the two side fibers CANNOT both remain in their no-P4/order-quiet cells. At least one side necessarily yields either

  * a Hamilton P4 on J plus an ACTUAL selected neighbor of d or v, or
  * an R435 source-order change relative to the ACTUAL exact side cover.

No selected state is transported between fibers in this argument. The coupling is entirely graph-intrinsic through the single four-cell signature of J, while each R435 comparison is made against the cover in which its p-middle-q turn is genuinely selected. This strictly sharpens the Bilateral-FREE residue: the earlier two FREE crossings cannot coexist as two anonymous capture packets. The remaining local consumer is now source-specific actual-neighbor P4 absorption (with exact seam bookkeeping), together with consumption of the resulting side-cover order-change output.


### Common-residue endpoint currentization fork

Choose b to be the second vertex of a host rail F=(l,b,s,...) sqcup Q_F. Then F-b is the literal three-cover (l) sqcup (s,...) sqcup Q_F of the common residue H-{b,v,d}. Fix any exact common-residue cover C. The previous universal-internality argument shows both C rails are nontrivial, so l has at least one selected C-neighbor and is physically absorbed from its singleton source component.

If l is a C-rail endpoint with selected neighbor y, there is an exact one-test currentization fork. If the rail begins (l,y,...), test (b,l,y). If it is tight, prepend b: (b,l,y,...) together with the other C rail is an exact H-{v,d} two-cover exposing b as an endpoint; moreover it selects the exact reverse b->l of the old host state l->b. If (b,l,y) is bad, R3 forces (y,l,b) tight, and the original host turn (l,b,s) then gives the literal source-labelled P4 (y,l,b,s).

If instead the C rail ends (...,y,l), test (y,l,b). If it is tight, append b and obtain an exact H-{v,d} two-cover exposing b as an endpoint. If it is bad, R3 forces (b,l,y) tight, which contains the exact reversed old host state b->l against F's selected l->b.

Thus whenever the old host singleton l is exposed at an end of the common-residue cover, the singleton-source absorption is already consumed into either an ACTUAL same-residue endpoint-role change for b, an exact old-host-state reversal, or a P4 tied simultaneously to the selected common-residue neighbor y and the old host successor s. No selected state is transported between covers. The unresolved subcase is precisely l INTERNAL in C, where both selected incidences at l must be used and complete insertion windows (e.g. R844) are required; one-sided endpoint logic is insufficient.