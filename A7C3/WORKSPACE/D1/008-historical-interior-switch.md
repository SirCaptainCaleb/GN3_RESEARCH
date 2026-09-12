# Historical Internal-X restoration: valid m>=7 route, failed m=6 seam, repaired all-order route

**Workspace:** D1
**State:** working
**Key:** `historical-interior-switch`

**Summary:** R674 is a valid weaker-hypothesis restoration theorem for m>=7; R675 exposed the m=6 seam but depended on invalid R658; R852 repairs exactly that dependency with R849.

The Internal-X subfamily has a useful historical alternative proof that should not be erased by the later A/C/D compiler.

Original R672/P750 claimed the all-order restoration. Its structural argument is sound through the monotone reduction: a c_X=2 Internal-X cover has one nontrivial rail containing all three Q cells and one internal X block, hence outside the explicit R435 outputs it is either G_0-X_i-G_1-G_2 or G_0-G_1-X_i-G_2. Removing X_i and restoring the corresponding deleted anchor constructs a jumped Q rail K_R on V(Q)-{q_{m-2}} or K_L on V(Q)-{q_2}. But P750 silently treated the newly exposed m=6 seam as an old Q turn. Therefore the all-m proof is invalid at m=6; its m>=7 portion survives.

R674/P752 states that surviving portion correctly. For m>=7, in the left-gap order remove X_i and insert q_2 between q_1 and q_3. Since q_4 lies in G_1, every newly exposed turn is consecutive in Q and the later G_1-G_2 seam is inherited from T. Thus
 K_R=(q_0,q_1,q_2,q_3,...,q_{m-3},q_{m-1},q_m)
is tight on V(Q)-{q_{m-2}}. Put d=q_{m-2}. If X union {d} had a Hamilton P5, it and K_R would be a spanning two-cover, so X union {d} is P5-free. R549 gives an outgoing extreme gate and incoming opposite extreme gate; R534 supplies complementary alternating gates; R536 and its terminal dual give four Hamilton P4s A_x on ({d} union X)-{x}, one for each x in X. Hence A_x union K_R is an exact two-cover of H-x for every x. The right-gap case is dual: remove X_i, restore q_{m-2}, obtain K_L on V(Q)-{q_2}, put d=q_2, and repeat the same P5-free gate construction. This m>=7 theorem is valid but abandoned as superseded; it remains a useful weaker-hypothesis route.

R675/P753 attempted to repair m=6. It correctly isolates the only new seam. In the left-gap case with G_1={q_3}, K_R=(q_0,q_1,q_2,q_3,q_5,q_6) needs only q_2 q_3 q_5 beyond inherited/old turns. If that seam is bad, R3 gives (q_5,q_3,q_2). The right-gap case similarly isolates q_1 q_3 q_4, whose bad orientation reverses to (q_4,q_3,q_1). However P753 cited old R658 to sign D_L=(q_3,q_2) and D_R=(q_4,q_3) as though a paid-floor conclusion were available. R658 was later invalidated for that overclaim. Therefore P753 is not a valid all-order proof even though its seam isolation is correct.

R852/P927 is the dependency-clean repair. It repeats the m>=7 construction unchanged. At m=6, for a bad left seam (q_5,q_3,q_2), accepted R849 gives the static tail signs of D_L by both b,z; the trimer itself supplies the opposite natural head polarity through q_5, so R518 gives labelled P4s on {q_5,q_3,q_2,b} and {q_5,q_3,q_2,z}. For a bad right seam (q_4,q_3,q_1), R849 gives the static head signs of D_R by a,c while the trimer supplies the opposite natural tail polarity through q_1, yielding P4s on {q_4,q_3,q_1,a} and {q_4,q_3,q_1,c}. If the seam is tight, K_R or K_L exists and the same P5-free R549/R534/R536 argument gives the four exact deletion covers. Thus R852 contains a valid all-order repaired Internal-X proof. It was abandoned because the later parent compilation subsumed its live use, not because this mathematical route is false.
