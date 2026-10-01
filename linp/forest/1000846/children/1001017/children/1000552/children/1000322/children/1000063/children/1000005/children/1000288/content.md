# Lexicographic path-state induction for the grand two-thirds conjecture

## Statement

A proposed induction for 3delta<=2L+2 tracks a nonspecial target edge together with an entrance path. Order states by increasing target rank, then decreasing path loss, then the span of the unique loss-one fixed-hole obstruction. Certified rotation, transfer, and sink lemmas show that all persistent recurrence is forced into two atoms: flat equal-rank transfer cycles and canonical loss-one fixed-hole/theta states. Closing those two atoms at the 3q/2 scale would prove the boundary step and plausibly the grand conjecture.

## Body


Goal: prove the grand nonspecial-edge inequality
  3 delta(H) <= 2L+2
whenever H contains a nonspecial edge, where L is the global maximum path length.

The proposed induction does not run on |V(H)|. It runs on a path state.

STATE.
A state consists of:
(1) a nonspecial target edge e={x,y,z} of rank q, with unique entrance x and terminals y,z;
(2) an x-ending entrance path Q avoiding y,z, normally of length q-1 when e is ascending, or a shorter path obtained by a controlled blocker splice;
(3) if Q has lost one edge from the canonical q-1 length, the distinguished omitted path vertex ("fixed hole") and the minimal interval containing its one-contact external chords.

Order states lexicographically by:
(A) larger target rank q is better;
(B) at fixed q, larger entrance-path length is better;
(C) in the unique loss-one regime, smaller hole/contact span is better.

The certified machinery gives the following monotone alternatives.

I. BELOW THE BOUNDARY q<=delta-1.
Every canonical ascending entrance state has a safe single-blocker rotation, and in fact the fixed-entrance rotation graph has degree at least 4(delta-q)-2. Thus such a state cannot be a local sink. The induction does not need to classify it locally; it moves within a large finite rotation class until a terminal switch, clean branch, repeated blocker, or transfer is exposed.

II. AT THE BOUNDARY q=delta.
Far-end deletion plus the deficiency-two classification gives:
- a safe clean move;
- a safe single-blocker rotation;
- a terminal-clean branch f which is special or has rank at least q.
If rank(f)>q, coordinate (A) improves.
If rank(f)=q and f is nonspecial ascending, the move is a flat terminal transfer and closes a q-cycle.
If a double-blocker splice is used, any loss >=2 cannot be a sink (585acf12de9a). Thus recurrence can persist only at loss one.

III. THE LOSS-ONE STATE.
Every loss-one sink is one of the exact saturated Type A/Type B forms. Its double blockers form a degree-at-most-two cell-index graph. If no lossless rotation exists, a nonlocal double blocker is forced (74a355123ba8). The exact splice-loss formula implies that a minimal-span recurrent nonlocal blocker must be the distance-two/private pattern, producing the canonical two-cycle (0501d7730fd2). The two-cycle has a fixed omitted vertex with external attachment surplus (99598d2f3043). The Type-B alternate break either produces a further nonlocal blocker of smaller/equally controlled span or a terminal theta with branch lengths q-2,1,2 (58e8229b49ca). Thus the only possible non-improving recurrence at fixed q and loss one is a finite fixed-hole/window system.

IV. FLAT TRANSFER RECURRENCE.
A q-step walk of flat equal-rank ascending transfers contains a labeled linear cycle of length c<=q (1ab61678f414). Each flat transfer carries one-edge blocker memory into the next longest witness. A cycle of length c has, at every private vertex, mobile-ear surplus
  2C_0+C_1 >= 2q-2c+1
under minimum degree q (64823c8c54de).
Hence short recurrent cycles have increasingly many mobile ears; only cycles with c close to q can have near-minimal mobility. This is the same saturation phenomenon seen in the order-11 equality example.

V. TOP-RANK / MAXIMUM-RANK STATES.
At q=L, terminal double blockers form alternating path-cycle systems with exact defect accounting. The identity
  U_v-S_v=2(L-d(v))
measures deviation from full saturation. The zero-defect case is the closed alternating-cycle geometry realized at equality; one-defect states are the punctured-Steiner one/two-chain topology. More generally outside/single-blocker deficiency controls the number of open chains.

Therefore a proof by induction would be complete after two local closure lemmas:

(A) BOUNDARY CYCLE CLOSURE.
In minimum degree q, every recurrent flat rank-q transfer/rotation cycle either yields a nonspecial state of larger rank or produces a linear path of length at least ceil((3q-2)/2).

(B) FIXED-HOLE CLOSURE.
Every canonical loss-one fixed-hole/window state either returns losslessly to a canonical q-1 entrance path, yields a special/higher-rank terminal branch, or produces a path of length at least ceil((3q-2)/2).

If (A) and (B) hold, then the boundary rank q=delta cannot exist whenever 3delta>2L+2. Below the boundary, the rotation-rich induction feeds into the boundary/higher-rank regime; at maximum rank, defect-stability supplies the same two recurrent geometries. The remaining nonascending issue can be incorporated by taking entrance potential as a secondary rank coordinate: equal-rank nonascending transfers strictly increase entrance potential relative to an ascending source, while any closed flat transfer chain is necessarily ascending.

This is intended as an inductive proof architecture, not yet a proof of (A) or (B).
