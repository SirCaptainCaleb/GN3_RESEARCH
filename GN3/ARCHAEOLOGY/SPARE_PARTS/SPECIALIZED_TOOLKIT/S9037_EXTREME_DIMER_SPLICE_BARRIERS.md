# S9037 — Extreme Dimers Turn Failed Cooperative Splices into Barrier Corridors

## Theorem

Let G be a finite edge-ordered complete graph with pc_inc(G)>2. MINIMUM-DIMER CORRIDOR: suppose G has a spanning increasing three-cover D|A|B where D is the dimer on vertices x,y and xy is the globally minimum edge. Orient A,B increasingly. Let p->v be any selected edge of A and let s be the source of B. If L_A(p)<lambda(ps)<U_B(s), then lambda(xv)>=U_A(v) and lambda(yv)>=U_A(v). MAXIMUM-DIMER CORRIDOR: suppose instead D is the dimer on vertices X,Y and XY is the globally maximum edge. Let p->v be any selected edge of A and t the terminal of B. If L_B(t)<lambda(tv)<U_A(v), then lambda(pX)<=L_A(p) and lambda(pY)<=L_A(p). Thus failure of all `S9015` cooperative splices with an extreme dimer produces simultaneous two-end successor barriers in the minimum case and simultaneous two-end predecessor barriers in the maximum case.

## Proof

MINIMUM-DIMER CORRIDOR. Let D have physical vertices x,y and globally minimum edge xy. Fix selected p->v of A and source s of B with L_A(p)<lambda(ps)<U_B(s). First orient D as (x,y), so its terminal is y and L_D(y)=lambda(xy). Since xy is globally minimum and yv is a different physical edge, lambda(xy)<lambda(yv). If lambda(yv)<U_A(v), then both `S9015` inequalities hold: L_D(y)<lambda(yv)<U_A(v) and L_A(p)<lambda(ps)<U_B(s). `S9015` would then reduce the displayed three-cover to two increasing paths, contradicting pc_inc(G)>2. Hence lambda(yv)>=U_A(v). Reverse the vacuous dimer orientation to (y,x). The same three-cover remains increasing, now with terminal x and L_D(x)=lambda(xy). Again global minimality gives lambda(xy)<lambda(xv). The same `S9015` application shows lambda(xv)>=U_A(v). This proves the minimum case. MAXIMUM-DIMER CORRIDOR. Let D have physical vertices X,Y and globally maximum edge XY. Fix selected p->v of A and terminal t of B with L_B(t)<lambda(tv)<U_A(v). Orient D as (X,Y), so its source is X and U_D(X)=lambda(XY). Since XY is globally maximum and pX is different, lambda(pX)<lambda(XY)=U_D(X). If L_A(p)<lambda(pX), then `S9015` applied with terminal t of B, source X of D, and selected edge p->v of A has both seam inequalities: L_B(t)<lambda(tv)<U_A(v) and L_A(p)<lambda(pX)<U_D(X). This would two-cover G, contradiction. Therefore lambda(pX)<=L_A(p). Reversing D to (Y,X) gives identically lambda(pY)<=L_A(p). No other property is used.

## Why this is reusable

Combining an extreme dimer with the three-component splice `S9015` converts every failed cooperative splice into simultaneous two-end edge-order barriers. This is a clean local obstruction for minimum- or maximum-edge dimers.

## Scope and nonclaims

The theorem assumes an explicit spanning three-cover with an extreme dimer rail and one compatible splice inequality on the other two rails. It does not assert such a cover exists.

## Provenance

Rescued from accepted archived result `R1004`.
