# D3 — R24 reconstruction: from short deletion rails to the long-core gate problem

Full-library R24 development containing the modern reconstruction, native historical gate mathematics, seam/zipper archaeology, finite-base repair history, cross-end residue renormalization, and explicit rejected/abandoned route fences.

## R24, O6, and the global target

In a smallest counterexample, R4 supplies pc(H)=3 and says that every nonempty proper induced subsystem has path-cover number at most two. R4 gives an exact two-cover in the more specific situation where one removes the vertices of a proper graph-intrinsic tight path and considers its complement; it does not assert exact path-cover number two for every proper induced subsystem. R24 is the legacy singleton-deletion order floor. Its role is foundational because the modern proof of R5 uses R24, but a proof of R24 alone does not eliminate every smallest counterexample. The document therefore separates the R24 reconstruction problem from the global closure problem rather than treating the former as the latter.

## Noncircular reduction to the synchronized order-three frame

Assume R24 fails through an exact singleton-deletion cover H-z=P sqcup Q with |P|<=3. We prove the accepted R594 reduction without using R24 or R5.

If |P|=1, adjoining z to P gives a tight dimer, which together with Q two-covers H. If |P|=2, R3 gives a tight trimer on V(P) union {z}, again leaving Q as the second rail. Thus every survivor has |P|=3.

Now exclude short Q. If |Q|=1, adjoining z to Q gives a dimer and P remains the other rail. If |Q|=2, R3 gives a tight trimer on V(Q) union {z}. If |Q| is 3 or 4, then |H| is 7 or 8. Choose any six vertices. R193 gives a tight P5 on five of them. The vertices outside that P5 form respectively a dimer or a three-set; in the latter case R3 supplies a tight trimer. Either way H has a spanning two-cover. Therefore |Q|>=5. Write Q=(q_0,...,q_m) with m>=4.

Put X=V(P) union {z}. A Hamilton P4 on X together with Q would two-cover H, so X is P4-free. For every x in X, R3 supplies a tight trimer on X-{x}. Together with Q this gives a literal two-cover of H-x. It is exact: R4 gives pc(H-x)<=2, while a Hamilton path of H-x together with singleton x would two-cover H. Thus all four roots share the same exact Q rail and exact trimer complements.

Neither X union {q_0} nor X union {q_m} can contain a Hamilton P5, since such a P5 together with the untouched Q suffix or prefix would two-cover H. Also, for every x in X, (x,q_0,q_1) must be bad: otherwise (x,q_0,...,q_m) together with the trimer on X-{x} would two-cover H. By R3, (q_1,q_0,x) is tight for every x. Dually, (x,q_m,q_{m-1}) is tight for every x. These are simultaneous graph-intrinsic endpoint reverse stars.

The accepted four-cell classification R518 leaves, for the P4-free X, the transitive matching-height signatures and the cyclic 00 signature. R590 proves that every fifth vertex Hamilton-extends the cyclic 00 cell. Taking q_0 would contradict the established P5-freeness of X union {q_0}. Hence X is transitive. Relabel its opposite-edge matching heights M(ab)=M_R>M(ac)=M_S>M(bc)=M_L. This is precisely the synchronized transitive order-three frame.

This proof is P677, the selected fully reconstructible route for R594. The only imported mechanisms are the finite six-set P5 lemma R193 and the four-cell classification R518; neither depends on R24.

## Finite base m=4: aligned phase

Write Q=(L,u,v,s,R). We use one elementary principle throughout the finite-base analysis. If two vertex-disjoint proposed paths span V(H), every required turn except one turn tau is already certified, and tau were tight, those two paths would be a spanning two-cover of H. Hence tau is bad, and boundary antisymmetry R3 forces rev(tau) tight.

In ALIGNED, consider (z,v,u,b) sqcup (L,a,c,R,s). Its sole uncertified turn is (v,u,b): (z,v,u) is the aligned right-inward turn from R536; (L,a,c) and (a,c,R) are aligned gate turns from R619; and (c,R,s) is an endpoint star from R594. The one-hole principle therefore forces (b,u,v) tight.

Now consider (L,c,a,z) sqcup (b,u,v,s,R). Its sole uncertified turn is (b,u,v): (L,c,a) is the aligned gate turn, (c,a,z) is the matching-height X-turn supplied by R594, and (u,v,s),(v,s,R) are Q turns. Thus (v,u,b) is tight. The two forced turns are exact reversals, contradicting R3. This is the complete aligned m=4 branch historically isolated inside R877.

## Finite base m=4: crossed phase

Assume CROSSED and retain Q=(L,u,v,s,R). R723 gives (v,u,x) and (x,s,v) tight for every x in X, and R536 supplies the relevant inward complement turns. Apply the one-hole principle from the preceding section to the following six literal spanning proposals, in order:

1. (L,c,a,z) sqcup (v,u,b,R,s), hole (u,b,R), forces Rbu=(R,b,u).
2. (u,v,s,R) sqcup (b,z,L,a,c), hole (z,L,a), forces aLz=(a,L,z).
3. (L,u,v,s) sqcup (b,R,c,a,z), hole (b,R,c), forces cRb=(c,R,b).
4. (c,z,b,R) sqcup (u,L,a,s,v), hole (L,a,s), forces saL=(s,a,L).
5. (c,R,b,u) sqcup (a,s,v,z,L), hole (v,z,L), forces Lzv=(L,z,v).
6. (c,R,b,u) sqcup (s,a,L,z,v), hole (L,z,v), forces vzL=(v,z,L).

Every non-hole turn in these proposals is supplied by Q, the crossed R619 gate data, the R594 endpoint stars and X-turns, R723 first-inward stars, R536 inward turns, or an earlier forced literal in this list. The final literals Lzv and vzL are exact reversals, contradicting R3. Thus m=4 is impossible in the crossed phase as well. This is the complete crossed branch historically packaged as R877.

## Finite base m=5: aligned phase

Write Q=(L,u,v,d,s,R). R594 gives endpoint stars (u,L,a) and (c,R,s), while the aligned R619 gate gives (L,a,c) and (a,c,R), so P6=(u,L,a,c,R,s) is tight. R536 gives (b,d,v) and (d,v,z), so P4=(b,d,v,z) is tight. The supports are disjoint and span H. This is the complete local argument historically isolated as R876.

## Finite base m=5: crossed phase

Assume m=5 and CROSSED, with Q=(L,u,v,d,s,R). First apply the one-hole principle to ten literal spanning caps. Every non-hole turn below is a Q turn, an R594 endpoint star or matching-height X-turn, a crossed R619/R621 gate turn, an R723 first-inward star, or an R536 inward turn. The caps force:

1. (u,L,c,a,z) sqcup (d,v,b,R,s), hole (v,b,R), forces Rbv=(R,b,v).
2. (u,L,a,c,b) sqcup (d,v,z,R,s), hole (v,z,R), forces Rzv=(R,z,v).
3. (u,v,d,s,R) sqcup (c,z,b,L,a), hole (b,L,a), forces aLb=(a,L,b).
4. (u,v,d,s,R) sqcup (b,z,L,a,c), hole (z,L,a), forces aLz=(a,L,z).
5. (L,u,v,d,s) sqcup (c,z,b,R,a), hole (b,R,a), forces aRb=(a,R,b).
6. (u,v,d,s,R) sqcup (a,b,z,L,c), hole (z,L,c), forces cLz=(c,L,z).
7. (L,u,v,d,s) sqcup (b,R,c,a,z), hole (b,R,c), forces cRb=(c,R,b).
8. (L,u,v,d,s) sqcup (a,b,z,R,c), hole (z,R,c), forces cRz=(c,R,z).
9. (u,L,a,d,v) sqcup (c,z,b,R,s), hole (L,a,d), forces daL=(d,a,L).
10. (u,L,c,d,v) sqcup (a,b,z,R,s), hole (L,c,d), forces dcL=(d,c,L).

Here the turns adv, cdv, dvb, and dvz are exactly the m=5 inward turns supplied by R536.

Now use the physical Mate-Cycle/Mate-Fork rule R173. In each pair below, the two displayed proposals have hole sets {h,t} and {h,rev(t)}; the r=1 Mate-Fork specialization therefore forces rev(h). All unlisted turns are already certified or were forced above.

F1. (a,d,c,L,z) sqcup (v,u,b,R,s), holes {adc,ubR}, and (c,d,a,L,z) sqcup (v,u,b,R,s), holes {cda,ubR}; force Rbu=(R,b,u).
F2. (u,L,a,s,d) sqcup (c,R,b,v,z), holes {Las,bvz}, and (u,L,a,s,d) sqcup (c,R,z,v,b), holes {Las,zvb}; force saL=(s,a,L).
F3. (c,d,v,z,L) sqcup (s,a,R,b,u), holes {vzL,saR}, and (d,c,L,z,v) sqcup (s,a,R,b,u), holes {Lzv,saR}; force Ras=(R,a,s).
F4. (u,s,a,L,b) sqcup (R,c,d,v,z), holes {usa,Rcd}, and (u,s,a,L,b) sqcup (d,c,R,z,v), holes {usa,dcR}; force asu=(a,s,u).
F5. (a,d,v,z,L) sqcup (c,R,b,u,s), holes {vzL,bus}, and (d,a,L,z,v) sqcup (c,R,b,u,s), holes {Lzv,bus}; force sub=(s,u,b).
F6. (s,a,L,b,u) sqcup (d,c,R,z,v), holes {Lbu,dcR}, and (s,a,L,b,u) sqcup (R,c,d,v,z), holes {Lbu,Rcd}; force ubL=(u,b,L).

Consequently Ras, asu, sub, ubL make P6=(R,a,s,u,b,L) a tight path. R536 supplies cdv and dvz, so P4=(c,d,v,z) is tight. The two paths are disjoint and span V(H), contradicting pc(H)>2. Thus m=5 is impossible in the crossed phase. The historical R878/P954 certificate remains an exact standalone interface, and pending P990 contains the same calculation as a local part of the direct R880 proof.

## The finite branches combine into the substantial m>=6 conclusion

R594 gives m>=4 and R619 is exhaustive. The four preceding local sections eliminate both gate phases at m=4 and both at m=5, proving exactly the R880 conclusion m>=6. Pending route P990 stores this as one sectioned proof with direct external dependencies; until fresh review accepts P990, the existing accepted R880 route and R876/R877/R878 proof leaves remain canonical. R881 then combines R594, R880, and R810 to obtain the eight-vertex pc=2 core G8 plus nonempty Hamilton middle rail N.

## The exhaustive internal gate split

R619 synchronizes all four enlarged singleton-deletion roots and shows that the left and right M_S gate roles have exactly two possibilities. ALIGNED uses the same M_S pair at both ends; CROSSED swaps the two pairs. Because this split is proved exhaustive, a proof that follows this reduction must discharge both phases. The later exact-cover developments may reorganize their internal analysis without changing that logical fact.

## Cross-end turns have a direct current-interface consumer

When a tight turn (L,e,R) is available, R884 constructs a Hamilton P5 through the endpoints, two exact residue covers, and four simultaneous seam alternatives. This is a supporting interface inside the long frame. It neither chooses a gate phase nor by itself proves a spanning two-cover.

## Why the long-core reduction is not already finite closure

R829 shows that boundary antisymmetry alone permits longest tight paths of only asymptotic half order. R835 shows the aligned inward-star data do not force the relevant five-set Hamiltonian. R904 gives all-order Hamiltonian examples with the listed crossed local eight-core data but no two-cover preserving the designated middle rail intact. These results fence specific endgames without contradicting the long-core reduction itself.

## Remaining closure requirement after the reduction

No accepted theorem cited in this development closes every ALIGNED and CROSSED long frame. The next mathematical layer is therefore exact-cover interaction inside those phases. That layer is developed separately so the reduction theorem is not burdened with local packet inventories.

## Finite base: every six-set contains a tight five-path

R193 is a short but genuine finite-base result. Let W be any six vertices. Partition W into a three-set P and complementary vertices {x,y,z}. R8 gives a tight trimer ordering of P. Apply R146, the three-exterior pair-extension lemma, to that fixed trimer and x,y,z. One of P union {x,y}, P union {x,z}, or P union {y,z} supports a tight P5. Hence every six-set contains a tight five-path.

The result is currently superseded as a standalone claim but remains valid and fully reconstructible through P193. In the R594 reduction it is used only as a finite-order engine: when the hypothetical order-three root has |Q|=3 or 4, a P5 on five of six chosen vertices leaves a dimer or trimer as the second spanning rail. R146 is indexed in D22 as the exact three-exterior pair-extension theorem, but D22 explicitly leaves its SAT certificate P602 unreconstructed in prose; the exact proof remains P602. It is cited here only at this finite-base use.

## The cyclic no-P4 cell is impossible, with a stronger near-end variant

Let X={a,b,c,z} be the cyclic 00 no-P4 cell of R516, with its fixed twelve tight representatives. Let d be a fifth vertex. R590 proves that X union {d} always has a Hamilton P5 by an explicit implication certificate.

Assume for contradiction that X union {d} is P5-free. Write xyz for the turn (x,y,z) being tight. If dab is tight, successive one-hole Hamilton candidates force

dab => adz => czd => bdz => dba => bdc => dbz => bda => cad => zda => bad.

The candidates, in order, are (z,d,a,b,c), (a,d,z,c,b), (a,c,z,d,b), (c,a,b,d,z), (c,d,b,a,z), (a,z,b,d,c), (a,d,b,z,c), (b,d,a,c,z), (b,c,a,d,z), and again (z,d,a,b,c). Each implication uses two already-certified turns of the candidate; P5-freeness makes the third bad and R3 makes its complete reversal tight. Thus dab forces its reverse bad.

If instead bad is tight, the same procedure gives

bad => cda => dcz => cdb => abd => zdb => cbd => adb => daz.

Here the candidates are (z,b,a,d,c), (b,z,c,d,a), (b,d,c,z,a), (c,d,b,a,z), (c,a,b,d,z), (z,d,b,c,a), (z,c,b,d,a), and (c,z,a,d,b). The final two forced turns cda and daz, together with the fixed 00 turn azb, make (c,d,a,z,b) a Hamilton P5, contradiction. Hence bad cannot be tight. R3 then forces dab tight, and the first chain forces bad tight, another contradiction. This proves R590.

R593 preserves the theorem and adds a useful coordinate: d can be placed in position 1 or 3 of a Hamilton order. Its proof uses only candidate orders having d in one of those positions. Under the contrary assumption, the two explicit implication chains are

dab => adz => czd => bdz => dba => bdc => dbz => bda => cad => zda => bad,

bad => cda => dcz => cdb => abd => zdb => cbd => adb => daz => adc => dab.

The corresponding compact candidate names are zdabc, adzcb, aczdb, cabdz, cdbaz, azbdc, adbzc, bdacz, bcadz, zdabc for the first chain, and zbadc, bzcda, bdcza, cdbaz, cabdz, zdbca, zcbda, czadb, cdazb, zbadc for the second. Every one places d one step from an end. Since dab and bad are complete reversals, either initial orientation forces the other, contradiction. Thus R593 is a genuine stronger-hypothesis-free strengthening of R590, not merely a duplicate proof.

For the R24 reduction, R590 alone suffices: take d=q_0 and combine the Hamilton P5 on X union {q_0} with Q[1,m]. The abandoned R594 route P672 used the stronger R593 coordinate; P677 intentionally uses the weaker sufficient R590 theorem.

## Two-witness no-P4 stars renormalize to matching-height geometry

R537 gives a direct native classification that is useful independently of the original R24 root. Suppose ABc and ABd are tight and Z={A,B,c,d} has no Hamilton P4.

Candidate (A,B,c,d) forces dcB; (A,B,d,c) forces cdB. Then (A,c,d,B) forces dcA and (A,d,c,B) forces cdA. Finally (c,A,B,d) forces BAc and (d,A,B,c) forces BAd. Thus the eight turns

ABc, ABd, BAc, BAd, cdA, dcA, cdB, dcB

are simultaneously tight.

One remaining cross-comparison bit, AcB versus BcA, determines every other reversal pair. If AcB is tight, repeated no-P4 tests force the unique matching-height completion

{{A,B},{c,d}} > {{A,c},{B,d}} > {{A,d},{B,c}}.

If BcA is tight, the unique completion is

{{A,B},{c,d}} > {{A,d},{B,c}} > {{A,c},{B,d}}.

Uniqueness is literal: after the common eight turns and the chosen cross bit are fixed, each remaining reversal pair occurs as the sole uncertified turn in a Hamilton P4 candidate whose other turn is already tight. Conversely both displayed matching-height assignments are P4-free, since a Hamilton P4 would require a strict matching descent M_i>M_j>M_i. Therefore these are exactly the two completions. In both, the star dimer {A,B} and witness dimer {c,d} form the top matching.

## A P5-free fifth vertex has alternating full middle gates

Let X be a transitive matching-height four-cell with
M_R={{t,r},{l,s}}, M_S={{t,s},{l,r}}, M_L={{t,l},{r,s}},
ordered M_R>M_S>M_L, and suppose X union {d} is P5-free. Put
A=[dts], B=[dst], C=[drl], D=[dlr].
The matching-height rule supplies trl,lrs,tsr,rts,lst,stl,slr,rlt.

We first prove A=B. Suppose A holds and B fails, so tsd is tight. If sdl were tight then (r,t,s,d,l) would be a P5, so lds is tight. If rld were tight then (t,r,l,d,s) would be a P5, so D=dlr is tight. If tdl were tight then (t,d,l,r,s) would be a P5, so ldt is tight. But then (l,d,t,s,r) is a P5 using ldt,A,tsr, contradiction. Thus A=>B.

Conversely suppose B holds and A fails, so std is tight. If tdr were tight then (l,s,t,d,r) would be a P5, so rdt is tight. If lrd were tight then (s,l,r,d,t) would be a P5, so C=drl is tight. If sdr were tight then (s,d,r,l,t) would be a P5, so rds is tight. But then (r,d,s,t,l) is a P5 using rds,B,stl. Hence B=>A.

The same complementary candidate calculation gives C=D. Explicitly, if C holds and D fails then rld is tight; P5-freeness successively forces rds, tsd, and lds, after which (t,r,l,d,s) is a P5. If D holds and C fails then lrd is tight; P5-freeness successively forces ldt, std, and rdt, after which (s,l,r,d,t) is a P5.

Finally A and C have opposite values. If A=C=0, then std and lrd are tight. P5-freeness of (l,s,t,d,r) forces tdr bad and therefore rdt tight, making (s,l,r,d,t) a P5. If A=C=1, then B=D=1. P5-freeness of (r,d,s,t,l) forces rds bad and hence sdr tight, making (s,d,r,l,t) a P5. Thus A!=C. Since A=B and C=D, exactly one M_S edge is fully outgoing from d and the complementary M_S edge is fully incoming. This is the stronger direct proof P625 of R534.

The abandoned alternative P610 is mathematically distinct and remains historically retrievable. It assumes named extreme gates dtl,dlt and trd,rtd, then proves the same A=B, C=D and A!=C using complementary P5 candidates. Its dependence on the older four-cell classification R516 and its redundant extreme-gate hypotheses made it inferior to P625; abandonment does not make its valid local deductions false.

## Two-ended native gate geometry gives the exhaustive ALIGNED/CROSSED split

Retain the transitive frame X,Q and the endpoint reverse stars. R534 gives at q_0 one fully outgoing M_S edge e_L and its fully incoming complement f_L. Let e_L={a,b}, f_L={c,d}, and relabel c,d so that bd and ac are M_L edges. The matching-height rule gives abd and bac. Together with q_1q_0a and q_1q_0b, this yields the two tight absorber P5s

(q_1,q_0,a,b,d),  (q_1,q_0,b,a,c).

Their complementary vertex sets are {c} union V(Q[2,m]) and {d} union V(Q[2,m]). By the generic complementary-absorber lemma R538, neither induced complement is Hamiltonian.

At q_m, let e_R={u,v} be the fully incoming M_S edge and f_R={r,s} its complement. Relabel so ru and sv are M_R edges. Then ruv and svu are tight because M_R>M_S. With the fully incoming gate turns uvq_m, vuq_m and the endpoint stars xq_mq_{m-1}, we obtain

(r,u,v,q_m,q_{m-1}),  (s,v,u,q_m,q_{m-1}).

R538 gives the dual non-Hamiltonian one-witness prefixes {s} union V(Q[0,m-2]) and {r} union V(Q[0,m-2]).

Now M_S has exactly two complementary edges. Therefore e_L and e_R are either the same edge or the two distinct complementary edges. In the first case their witness complements are also the same: this is ALIGNED. In the second, each selected gate is the other's complement: this is CROSSED. No third phase exists. This is the complete R541 proof.

R536 sharpens the same geometry locally. If e={a,b} is a fully outgoing M_S gate from d and e'={c,d'} its complement, relabel so {a,c},{b,d'} are M_L. From dab,dba and the matching descents abd',bac we get the two exposed P4s (d,a,b,d') and (d,b,a,c). At q_0, prepend q_1 by the endpoint star. If the complementary tail with the omitted witness were Hamiltonian it would join this P5 to two-cover H; hence the tail is non-Hamiltonian, forcing the reverse inward turns q_3q_2x for both omitted witnesses. The right statement is the complete reversal. These inward turns are the native source of the finite and crossed certificates later in the document.

## Historical order-three routes: weaker predecessor and stronger-coordinate alternative

The current R594 statement has two important historical predecessors/routes whose valid mathematics should remain visible.

R592 with P670 was a correct but weaker first revision. It already closed |P|=1,2, proved the short rail had order three, established X P4-free, four common exact deletion roots, endpoint P5-freeness, endpoint reverse stars, and transitive normalization. Its finite argument closed only |Q|<=3, giving |Q|>=4 and m>=3. It used R193 for the seven-vertex |Q|=3 case. This was abandoned because the same finite-base idea also closes |Q|=4 and therefore yields the stronger m>=4 statement now recorded as R594.

Within R594, abandoned route P672 does prove the full m>=4 conclusion. It closes |Q|=3,4 by R193 exactly as P677 does, but excludes the cyclic four-cell using the stronger near-end theorem R593. P677 instead uses the weaker sufficient R590 extension theorem. The two routes therefore differ only at the cyclic-cell exclusion interface. P677 was selected because it has the cleaner dependency set, not because P672 contains a mathematical error.

The review distinctions remain exact: R592/P670 is valid but abandoned and not canonically usable; P672 is a valid abandoned alternative proof of accepted R594; P677 is the accepted selected fully reconstructible route.

## Historical finite-base deposits and their repaired certificates

The finite m=4 and m=5 conclusions were first deposited as R830, R831, and R832. All three revisions are marked mathematically valid, but each received `needs_more_work` review because its attached proof object was empty and dependency-free. Their statements anticipated the later correct closures but were not auditable as deposited.

R831 stated the aligned m=5 6+4 cover. Its proof object P905 contained no derivation. R876/P952 later verified every turn of P6=(u,L,a,c,R,s) and P4=(b,d,v,z) from R594, R619, and R536.

R832 stated the m=4 closure in both gate phases. P906 was empty. R877/P953 later supplied the two aligned one-hole caps and six crossed caps explicitly, ending in exact reversal collisions.

R830 stated the crossed m=5 Mate-Fork certificate. P904 was empty despite citing substantial ingredients. R878/P954 later supplied all ten one-hole cap proposals, all six physical Mate-Fork pairs, and the final P6 sqcup P4 cover. The present m=4/m=5 sections reproduce those later complete certificates.

Thus the old revisions are not discarded. Their substantive mathematical content is the same finite closure idea, now realized by their repaired successor revisions. Their review status also remains meaningful historical information: they show where the theorem statements were discovered before the proof objects caught up.

## External mathematical interfaces used by the R24 development

The long-core argument uses several generic mechanisms whose hypotheses are not specific to the R24 frame. Complete insertion and split-splice windows are developed in D14, including R583. Payment and floor steering are developed in D16, including R542 and the ancestry rules needed to spend signed supports. Capture and protected-contact machinery is developed in D15. Arbitrary-cover absorber crossing and unique-transition rigidity are developed in D13. When one of those theorems is used here, the R24 section retains the additional gate labels and exact cover representative required for the specialization; it does not reproduce the generic proof.

## Extreme gates and the universal-bridge obstruction

Let X be a transitive matching-height four-cell with M_R>M_S>M_L and let d be a fifth vertex for which X+d is P5-free. Three native facts were proved before the later middle-gate compression and remain useful on their own.

First, R546/P622 excludes the wrong extreme polarities. No M_L edge can be fully incoming to d, and no M_R edge can be fully outgoing. For a representative bottom edge bc, assume bcd and cbd. Five one-hole P5 tests force successively zdc, dzb, zda, adb, dac (after normalizing M_R={ab,cz}, M_S={ac,bz}, M_L={bc,az}); then (z,d,a,c,b) is a P5. The other bottom edge follows by the matching-height automorphism. The top argument is dual: a fully outgoing ab forces bdc, acd, zdc, dzb, zda and then the P5 (z,d,a,b,c).

Second, R549/P626 proves existence of correctly polarized extreme gates using only R3 and P5-freeness. If neither bottom M_L edge is fully outgoing, each bottom edge supplies one tight reversed incoming turn. The four possible choices are exhausted explicitly; in each case one P5 test reverses one mixed turn and a second displayed order becomes a P5. Hence some M_L edge is fully outgoing. The exact four-case dual shows some M_R edge is fully incoming. Together R546 and R549 say a P5-free fifth vertex necessarily has at least one correctly polarized extreme gate and cannot have an extreme gate with the opposite polarity.

Third, R553/P630 is a six-vertex bridge obstruction. Suppose u,v lie outside X and both (x,u,v) and (u,v,x) are tight for every x in X. If X+u were P5-free and X+{u,v} P6-free, two P6 tests force uca and ubz, then a P5 test forces cub, and (c,u,b,z,a) becomes a Hamilton P5 on X+u. Thus a dimer that is bidirectionally universal across X forces a P5 on X+u or a P6 on X+u+v. This is pure native gate geometry, independent of deletion-cover payment machinery.

## Two-ended gate polarity already forces an endpoint-favorable P5

R582/P660 predates the final R619 formulation but gives a useful two-ended native theorem. Let X be transitive matching-height, and let L,R be exterior vertices whose M_S gates have the required alternating full polarities: at L one M_S edge is fully outgoing and its complement fully incoming; at R one M_S edge is fully incoming and its complement fully outgoing. Normalize the L-outgoing edge as {b,z}. A Hamilton P5 on {L,R}+X-{x} is called endpoint-favorable when L is not confined to positions 1,2 or R is not confined to positions 2,3.

Assume no such P5 exists. There are only two possibilities for the R-incoming M_S edge. In the CROSSED case it is {a,c}. Four successive favorable candidates force zRL, czR, aLR, after which (z,c,a,L,R) is a favorable P5. In the ALIGNED case it is {b,z}. Eleven explicit one-hole candidates force, in sequence, cRz, bLc, cRL, RLa, aRL, RLc, zaL, azR, abL, baR, and then (b,a,R,L,c) is a favorable P5. Every forcing step uses two already-certified turns and R3 to reverse the unique missing turn. Thus one endpoint-favorable P5 exists in either gate phase.

This theorem is not itself a branch closure. Its enduring content is that two-ended gate polarity already produces a five-vertex path with a useful endpoint position before any selected-cover, payment, or capture mechanism is invoked.

## The retired exactly-two-bad seam branch was a complete native subtheory

An older route singled out the unique transitive seam cell with exactly two bad normalized seams. Although this route is no longer the preferred global organization, its native geometry is fully reconstructible and should not disappear.

R574/P650 begins with the aligned M_S gate {b,z}. The path S=(q_1,q_0,b,z,q_m,q_{m-1}) is a tight P6. Its complement is M={a,c} union V(Q[2,m-2]). R536 supplies the inward stars q_3q_2a,q_3q_2c and a q_{m-2}q_{m-3}, c q_{m-2}q_{m-3}. Consequently the branch closes for m=3,4,5: M is respectively a dimer, a three-set (hence Hamilton by R3), or has the explicit Hamilton P4 (a,q_3,q_2,c). Any surviving exactly-two-bad cell therefore has m>=6.

R589/P667 then uses eight one-hole Hamilton-P6 tests on X union {L,R}, where L=q_0 and R=q_m, to force the complete aligned cross-end reverse fan: aRz,cRz,aRb,cRb and bLc,zLc,bLa,zLa. Each hypothetical missing reverse would complete a P6 disjoint from the nonempty interior Q[1,m-1]. R591/P669 adds the cross-end anchor trimer LbR: if RbL were tight, (c,R,b,L,a,z) would be a P6, so R3 forces LbR.

The original R601 statement recorded the resulting short-trimer bridge pattern; R607/P686 is the fuller second revision. Six P5 obstructions force aLc, zcL, baL, Rcb, Raz, aRc; two P6 obstructions force RcL and RaL. Together with LbR, the original short trimer (a,b,c) has the rigid cross-end middle pattern RaL, LbR, RcL. Thus a and c point from R toward L while b points from L toward R; the analogous z-middle bridge is intentionally left undetermined.

These results are retained as a coherent retired branch, not as prerequisites for the modern R594/R619 route. They remain useful finite identities and show exactly how much rigidity was present in the old minimum-seam normalization.

## Historical high-side roots already produced same-residue exact-cover geometry

The pre-R619 route also discovered exact-cover geometry that survives independently of its old seam-count framing.

R598/P676 says a side-maximal high-side root absorbs exactly two physical vertices from one end of Q. On the left, R596 supplies A_L=(q_1,q_0,a,c,b), and A_L together with Q[2,m] is an exact two-cover of H-x_L. The right dual is Q[0,m-2] together with (b,a,c,q_m,q_{m-1}). Exactness is elementary: if the deletion residue were Hamiltonian, its Hamilton path plus the deleted singleton would two-cover H.

Inside the historical exactly-two-bad cell, R599/P678 identifies the left and right sibling roots as c and a. Deleting the exposed terminal root from each enlarged cover gives two exact covers of the same pair deletion W=H-{a,c}: T_L=(q_1,q_0,b,z) sqcup Q[2,m] and T_R=Q[0,m-2] sqcup (z,b,q_m,q_{m-1}). Four selected states cross the opposite support partition: q_0b and q_{m-2}q_{m-1} from T_L, and bq_m and q_1q_2 from T_R. The durable statement here is the common-residue four-cross-state weave. R599 then feeds those crossings into the separate reusable cross-state birth theorem R176.

R616/P695 obtains a closely related left-side synchronization without assuming the exactly-two-bad branch. With L=q_0,u=q_1,v=q_2,w=q_3, the two exact enlarged roots H-z=(u,L,a,c,b) sqcup Q[2,m] and H-b=(u,L,c,a,z) sqcup Q[2,m] coexist. R536 gives wvb,wvz. Two P6 exclusions also force Lub,Luz, so the same witness pair {b,z} tail-signs both tested reverse boundary dimers (L,u) and (w,v). This 2-by-2 inward witness rectangle is a direct ancestor of the later crossed signed-rectangle geometry.

## Historical finite fences explain why local badness, wrapping, and one-sided EAR data stalled

Three historical results are important chiefly because they prevent the migration from resurrecting failed local strategies.

R597/P675 gives a complete six-vertex orientation on X union {L,R}. Both endpoint five-cells are P5-free, the entire six-cell is P6-free, and every one of the four normalized roots has exactly five bad seams. The proof lists one tight representative from every reversal pair and verifies the endpoint and six-vertex path exclusions literally. Therefore even perfectly synchronized endpoint-local badness multiset {5,5,5,5} does not force local discharge of the R24 frame. Seam-count pressure needs genuinely nonlocal information.

R609/P688 shows something positive but limited in the historical exactly-two-bad cell: at least one of the two wrap seams alpha=(R,L,q_1) and beta=(q_{m-1},R,L) is bad. Three explicit five-vertex absorbers K_a,K_b,K_c guarantee that one of the endpoint cuts is available, and the general endpoint-cut recompletion theorem R540 turns it into alpha-bad or beta-bad. This excludes the double-wrap branch, but it does not close either single-wrap residue by itself.

R613/P692 is a stronger finite insufficiency certificate. It gives an explicit eight-vertex Strong orientation with the left high-side seed, the inward anchor, and a genuine gap-1 reverse-middle EAR packet, while X+L is P5-free and all one-sided prefix-compatible extensions through q_3 fail. Moreover none of the four proposed root-switched advanced states exists. Its complete middle-vertex table and finite path lists are stored in P692. Hence one-sided gap-1 EAR data, even with all local prefix obstructions, cannot force the first zipper switch. Any valid continuation must use a second end, a selected-cover coupling, or another genuinely nonlocal invariant.

## The old global order-greater-than-ten theorem remains partly legacy-dependent

R533/P598 is the accepted historical order-greater-than-ten gate. Its exact current dependency ledger is now clearer than the older DR3.8 wording suggested. R169/P168 has a full proof text: if a proper tight path K left at most four exterior vertices, deleting exactly those vertices would contradict R5 because the remainder is the Hamilton path K. R191/P191 likewise has a full proof text for the order-ten contradiction, using the minimum-overlap framework and the Johnson-neighbor count. Thus neither theorem survives merely as an opaque compressed certificate.

However, the exact proof-route status still matters. The current route service marks both R169/P168 and R191/P191 as not fully reconstructible end to end because some of their dependencies remain legacy/nonreconstructible. Consequently R533/P598 is accepted and usable, and its own proof text is explicit, but the whole dependency closure is not yet fully reconstructible. This is the correct provenance statement.

This remains distinct from the modern finite-base work in this document. R574 closes the historical exactly-two-bad cell through order ten; R876-R878 close the synchronized m=4 and m=5 gate phases. Those local reconstructions do not replace the separate global dependency chain of R533.

## The minimum cell saturates terminal edges and, after one wrap failure, saturates the surviving wrap phase

R608/P687 strengthens the historical exactly-two-bad cell at the two physical terminal edges of the short trimer J=(a,b,c). The bad minimum seams give Lbc and abR; matching-height X gives abz,baz,zbc,zcb; R607 gives baL and Rcb. Hence the identical tested orientations carry simultaneous signs: (a,b) is tail-signed by z,R; (b,a) is tail-signed by z,L; (b,c) is head-signed by z,L; and (c,b) is head-signed by z,R. Thus each physical terminal edge {a,b} and {b,c} is saturated in both tested orientations with one common polarity, with z a common witness. P687 further checks that each packet satisfies the reusable R542 carrier hypotheses. The theorem proved here is the simultaneous sign saturation itself.

R610/P689 continues the wrap analysis after R609 excludes double-wrap. In the double-fail branch R579 gives the reverse P4 (q_1,L,R,q_{m-1}). In single-wrap SW1, the cyclic rotation (R,L,q_1,...,q_{m-1}) is again globally longest. Longestness forces LRx for every x in X. Four explicit forbidden P6s then force RLx for every x. Therefore both tested wrap orientations (L,R) and (R,L) are tail-signed by all of X. In the dual SW2 rotation, longestness first forces xLR for all x, and four reflected P6s force xRL for all x; both wrap orientations are head-signed by all of X.

Thus the wrap tetrachotomy sharpens inside the minimum cell to: double-fail gives a labelled reverse P4, while either single-wrap branch gives universal bidirectional same-polarity saturation of the physical wrap dimer by all four X vertices. R610 observes that this creates an eight-channel R542 payment fan. D16 supplies the generic payment continuation; the wrap theorem itself is the bidirectional saturation statement proved here.

## The old order-three seam program isolated a sharp two-bad trap before the modern gate split

Before R619 became the preferred phase interface, the order-three frame was attacked by classifying its six normalized endpoint seams. R543/P619 is the clean parent of that branch. A bad seam paired with the z-extension produces a same-polarity two-witness collision on the relevant tested dimer. If all six seams are tight, the extreme- and middle-gate theorems force the aligned two-ended trap, with the literal shell path (q_1,q_0,b,z,q_m,q_{m-1}). R542 is the generic payment consumer developed in D16; the seam/gate dichotomy itself is proved here.

R544/P620 closes that aligned trap by a pure six-vertex forcing calculation. Five reverse-forcing tests end with a Hamilton P6 on the six-cell, so the all-six-good seam branch cannot survive. R554/P631 records a different physical consequence of the seam normalization: the left and right bad seams create opposite-polarity collisions hinged at b, and R547 can singletonize them only as a graph-intrinsic balanced pair unless genuine payment ancestry is separately available.

R555/P632 then identifies the unique minimal exactly-two-bad status word: (good,bad,good | good,good,bad), with cbq_0 and q_mba the bad seams in the normalized labels. R556/P633 feeds that exact word into the native middle/extreme gate geometry and recovers the aligned gate packet with precisely those two turns missing. These results are retired as a global route, not false. Their value is the exact finite seam geometry they isolate.

## Synchronized enlarged roots exposed the first zipper obstruction and its finite countermodel

R614/P693 is a short but decisive incompatibility in the synchronized-root route. The enlarged-root seed R598 concatenates to the tight turns q_2q_1x_L and aq_0x_L, so the displayed one-sided prefix used by the old R613 strategy is not induced in an actual smallest-counterexample R24 frame. This explains why the finite R613 witness was a genuine local fence but not an embeddable model of the full synchronized root data.

The first attempt to prove that even the synchronized left packet did not force a zipper switch was R617/P696. Its proposed local countermodel was wrong: the alleged P5-free five-sets F-z and F-b actually are Hamiltonian. The revision is therefore needs_more_work and its proof abandoned. R626/P705 repaired the idea with an explicit eight-vertex orientation. That certificate satisfies the synchronized two-root left prefix, the exact-cover/one-hole blocker data, and the required local non-Hamiltonicity, yet still has no cover-valued first inward switch. Hence left-local synchronization alone is insufficient; a right coordinate or another genuinely nonlocal coupling is necessary.

R618/P697 records the positive same-residue geometry that survives the failed one-sided strategy. When the right root coincides appropriately with the synchronized left pair, two exact singleton-deletion representatives descend to the same residue and expose four opposite support-crossing states. R176 is the separate cross-state birth theorem. This section retains the coexistence of the exact representatives and their four physical cross states.

## The first synchronized deep-cut splice theorem was rejected for an exact two-junction error

R816/P891 must remain visible precisely because it is not valid. It tried to turn each deep cut q_j|q_{j+1} of the synchronized enlarged-root frame into binary clauses such as A_j(z) OR (q,b,c). The proposed spanning split-splices, however, have two new junction windows, not one. For example the rail ending ...q_{j-1},q_j,z,R,s introduces both (q_{j-1},q_j,z) and (q_j,z,R); the companion rail can simultaneously introduce both (c,b,q_{j+1}) and, when present, (b,q_{j+1},q_{j+2}). The proof ledger suppressed the second hole and therefore could not reverse a unique missing turn.

Review correctly rejected R816 and P891. The later accepted R818 is the repaired complete-window interface and retains all four possible hole types at each splice. R818 belongs to the generic split-splice development rather than being re-proved here. This section therefore records a useful negative lesson: synchronized root covers do constrain every deep cut, but a two-junction splice cannot be compressed to a binary clause without separately certifying the second junction.

## A cross-end P5 led to deep-residue renormalization before the current R884 compiler

Fix e in X with (L,e,R) tight in the synchronized transitive frame. R749/P826 lets gamma be the M_R-partner of e and {alpha,beta} the other top-matching edge. Endpoint stars make J=(u,L,e,R,s) a tight P5. Its complement W=(X-{e}) union Q[2,m-2] cannot be Hamiltonian, or J plus that Hamilton path would two-cover H. The two matching-height trimers (beta,alpha,gamma) and (alpha,beta,gamma) can then be tested against the left and right ends of the deep Q interval. A failed concatenation reverses to either a deep Q witness or a two-witness star, and R537 converts the latter into a labelled P4 or a new transitive four-cell whose top matching pairs the deep coordinate with gamma. For m=4 the residue itself is the four-cell, so the renormalization is forced with no witness escape.

R750/P827 tried to saturate this deleted-P5 residue further. Its seam-closure calculation was sound in shape, but the proof depended on the invalid old rectangle revision R658 and was therefore unusable. R859/P934 is the exact dependency-migrated repair: it replaces R658 by accepted R849 and proves the left trimer seam, right trimer seam, and two Q-rail seam alternatives from literal impossibility of splicing either exact residue rail onto J. R859 is accepted but already superseded as an interface.

The active compression is R884, already cited in the main cross-end section. It packages the same cross-end orientation directly into the two canonical residue covers and simultaneous two-ended seam packet. The older R749/R750/R859 chain remains useful because it exposes the renormalization mechanism and the precise dependency repair rather than presenting R884 as an unexplained black box.

## Order-ten crossed survivors had two additional finite normal forms before direct closure

Two order-ten ideas were discovered around the crossed m=5 finite base and should remain distinguishable from the final direct certificate.

R819/P894 is valid and fully reconstructible. Any R725 first-step ADV cover at m=5 consists of one tight P6 and one tight trimer after deleting its root. Regard the trimer together with the deleted root as the new four-cell and the P6 as the new long rail. The hypotheses of R594 are literally met again in the same hypothetical counterexample, so the entire synchronized transitive package reappears on a rotated 4+6 partition. For example the left root-c case has S_c=(q_2,q_1,a,b,z,q_0) and new cell {c,q_3,q_4,q_5}, with endpoint stars (q_1,q_2,y) and (y,q_0,z) for every new root y. The other three root cases are exact dual/label variants. Thus ADV at order ten is a self-renormalization, not merely cut motion.

R824/P899 proposed a different central-cap compression: the crossed 4+4 caps should force q_3 fully outgoing on {a,c}, {b,z} fully incoming to q_2, plus one residual binary saying either both q_2,q_3 are outgoing on {a,c} or {b,z} is incoming to both. The claim revision is marked valid, but its only proof object is empty and dependency-free despite relying on R3/R536/R817. It therefore remains needs_more_work and unusable. It is also superseded by the direct accepted crossed m=5 closure R878, so migration preserves the proposal without asking the current proof to depend on it.

## High-side seam roots force explicit inward singleton anchors

Retain the common transitive order-three frame on X and Q=(q_0,...,q_m), m>=3. For each physical M_L edge e at L=q_0, the two deletion roots whose trimers contain e use the two incoming orientations uvL and vuL as their bottom seams. R546 says at least one of these is bad for every M_L edge. R549 supplies an M_L edge e_L fully outgoing from L, so R3 makes both incoming seam orientations on e_L bad. Let F_L be the M_S edge fully outgoing from L, supplied by R534 together with the extreme-gate information. The root-pair belonging to e_L and the root-pair belonging to F_L are pairs from distinct perfect matchings of K_4, hence meet in a unique root x_L.

Normalize X-{x_L}=(a,b,c) so bc=e_L and ac=F_L. Then bcL and cbL are bad because e_L is fully outgoing, and acL is bad because F_L is fully outgoing. Thus ell_{x_L}=3. Full outgoing polarity of F_L gives Lac and Lca tight. The matching-height rule gives acb tight because M(ac)=M_S>M(cb)=M_L. Hence K_L=(L,a,c,b) is a tight Hamilton P4 on {L} union (X-{x_L}). The standing endpoint reverse star q_1La extends it to the tight P5 A_L=(q_1,L,a,c,b).

Its complementary set is W_L={x_L} union {q_2,...,q_m}. If H[W_L] were Hamiltonian, its Hamilton path together with A_L would two-cover H, impossible. The literal order (x_L,q_2,q_3,...,q_m) differs from the tight Q suffix only in the first turn x_L q_2 q_3. That turn must therefore be bad, and R3 gives the graph-intrinsic inward anchor q_3 q_2 x_L tight.

The right endpoint is dual. Put R=q_m. R549 supplies an M_R edge e_R fully incoming to R; R3 makes both outgoing seam orientations on e_R bad. Let F_R be the M_S edge fully incoming to R. Their root-pairs meet in a unique root x_R. Normalize X-{x_R} so ab=e_R and ac=F_R. The two top seams and the middle seam are bad, so r_{x_R}=3. Full incoming polarity gives acR tight, while matching height gives bac tight. Thus (b,a,c,R) is a tight P4, and the endpoint reverse star extends it to (b,a,c,R,q_{m-1}), a tight P5. Its complement cannot be Hamiltonian; consequently the only new terminal turn q_{m-3}q_{m-2}x_R is bad and R3 yields x_R q_{m-2} q_{m-3} tight.

In the equality case of R576 with badness multiset {2,4,5,5}, the root sharing only the M_R pair with the unique two-bad root is x_L, while the root sharing only its M_L pair is x_R. They are distinct and are exactly the two five-bad siblings. This last identification is an equality-case refinement; outside that case R596 does not assert x_L=x_R or x_L!=x_R.

This is the complete R596/P674 construction. R596 remains an active standalone spine interface because its named roots, endpoint P5s, and inward turns are independently consumed later; this section is its connected R24 home, not an absorption or replacement of the claim.

## Four simultaneous deletion roots and the 2/4/5/5 seam law

For every deleted vertex x in X, the three-set X-{x} supports a tight trimer by R3, so together with Q it is a literal two-path cover of H-x. It is exact: if H-x were Hamiltonian, that Hamilton path together with the singleton (x) would be a spanning two-cover of H, contrary to pc(H)>2 from R4. Thus all four normalized deletion roots are legitimate simultaneously on the same physical X,Q frame.\n\nLEFT END. Fix one of the two physical M_L edges e={u,v}. In each of the two deletion roots whose trimer contains e, the two bottom seams are precisely uvq_0 and vuq_0, merely listed in opposite order. Let b_e be the number of these two turns that are bad. R546 says no M_L edge is fully incoming to q_0, so b_e>=1 for each of the two M_L edges. R549 says some M_L edge is fully outgoing from q_0. For that edge q_0uv and q_0vu are tight, so R3 makes vuq_0 and uvq_0 both bad; hence b_e=2 for at least one M_L edge. Since each bad orientation of e is counted in both roots containing e, the four roots contain 2(b_{e_1}+b_{e_2})>=6 bad bottom-seam occurrences.\n\nNow inspect the middle seams. For a physical M_S edge f, the two deletion roots whose trimers contain f use exactly the two orientations of f into q_0 as their middle seams. R534 says exactly one M_S edge is fully outgoing from q_0 and the complementary M_S edge is fully incoming. On the outgoing edge both orientations f->q_0 are bad by R3, while on the incoming edge both are tight. Hence among the four middle-seam occurrences exactly two are bad. Therefore the total number of bad left seams over all four roots is at least 6+2=8.\n\nRIGHT END. The same count is dual with M_R. For each physical M_R edge e let c_e be the number of bad orientations q_muv,q_mvu. R546 says no M_R edge is fully outgoing from q_m, so c_e>=1 for both top edges. R549 says some M_R edge is fully incoming to q_m, whose two outgoing reverses are therefore both bad, so c_e=2 for at least one edge. Each orientation is counted in both roots containing that edge, giving at least 6 bad top-seam occurrences. The four right middle seams are the two outgoing orientations q_muv,q_mvu on each M_S edge; R534 makes one M_S edge fully incoming and the other fully outgoing, so exactly two of these four middle seams are bad. Thus the right total is at least 8, and the total six-seam badness over all four roots is at least 16.\n\nIt remains to sharpen the equality-two case. The two physical edges in each perfect matching induce a partition of the four deleted-vertex roots into two pairs: a root lies in the pair for edge e exactly when its trimer contains e. The three matchings M_L,M_S,M_R give the three distinct pair partitions of a four-element set. A root has total badness two only if it has exactly one bad left seam and exactly one bad right seam. Thus its M_L edge must be the edge with exactly one bad incoming orientation, its left M_S middle seam must lie on the fully-incoming (good) M_S edge, its M_R edge must be the top edge with exactly one bad outgoing orientation, and its right M_S middle seam must lie on the fully-outgoing (good) M_S edge. In particular the left-good and right-good M_S edge must be the same physical edge, since the two M_S root-pairs are disjoint. Such a root therefore lies simultaneously in one prescribed pair from each of the M_L,M_S,M_R pair partitions. Any two distinct root labels lie together in exactly one of these three pair partitions, so the intersection of one prescribed pair from all three partitions has size at most one. Hence at most one root has total badness two.\n\nFinally suppose such a root r exists. Its M_L pair is the unique one-bad extreme pair and the opposite M_L pair is fully bad; similarly for M_R. Its M_S pair is the good-middle pair at both ends and the opposite M_S pair contributes a bad middle seam at both ends. The other three root labels each share exactly one of the three selected pairs M_L,M_S,M_R with r. The root sharing only the selected M_L pair has left count 1+1=2 and right count 2+1=3, hence total 5. The root sharing only selected M_R is symmetric and also has total 5. The root sharing only selected M_S has left count 2+0=2 and right count 2+0=2, hence total 4. Thus the four-root multiset is exactly {2,4,5,5}.

## R24 four-complement gap pressure: capture/payment or a reverse P4 ear

Fix a gap i. For 1<=i<=m-2, R583 gives one of three alternatives. In its left alternative there are distinct x,y in X with (x,q_i,q_{i-1}) and (y,q_i,q_{i-1}) tight. Since (q_{i-1},q_i,q_{i+1}) is a tight trimer inherited from Q, (q_i,q_{i-1}) is exactly its left reverse boundary dimer in the notation of R542. The witnesses x,y lie outside that trimer, so R542 applies and forces its capture/payment continuation. In the right alternative, use the tight trimer (q_i,q_{i+1},q_{i+2}); its right reverse boundary dimer is (q_{i+2},q_{i+1}), carrying the two R583 witnesses, so R542 again applies. In the third R583 alternative, two distinct reverse-middle turns (q_{i+1},x,q_i),(q_{i+1},y,q_i) are tight; accepted R584 gives the displayed P4 ear. At i=0, R583 has only the right terminal packet and the reverse-middle alternative. The right packet is on (q_2,q_1), the reverse terminal dimer of (q_0,q_1,q_2), hence R542-ready; if absent, at least three reverse-middle turns occur and any two invoke R584. The right endpoint is symmetric. These cases exhaust every gap.