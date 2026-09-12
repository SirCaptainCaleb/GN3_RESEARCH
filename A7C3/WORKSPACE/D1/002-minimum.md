# The complete sigma=0 classification and restoration argument

**Workspace:** D1
**State:** established
**Key:** `minimum`

**Summary:** The contracted forest has six typed shapes; Internal-X shapes force P4, and the surviving A/C/D geometries are handled by explicit anchor restoration, including the m=6 seam repairs.

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
