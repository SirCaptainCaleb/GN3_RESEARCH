# S9028 — P5-Free Fifth-Vertex Gates over a Transitive Four-Cell

## Theorem A — Extreme gate existence

Let X={t,l,r,s} be a transitive matching-height no-P4 four-cell in a Strong Level-(1) boundary tournament, with opposite-edge perfect matchings M_R={{t,r},{l,s}}>M_S={{t,s},{l,r}}>M_L={{t,l},{r,s}}. Let d be a fifth vertex such that X union {d} has no tight Hamilton P5. Then at least one M_L edge is fully outgoing from d, and at least one M_R edge is fully incoming to d. Equivalently, for at least one uv in M_L both duv and dvu are tight, and for at least one xy in M_R both xyd and yxd are tight.

### Proof

Write M_R={{t,r},{l,s}}, M_S={{t,s},{l,r}}, M_L={{t,l},{r,s}}. The matching-height rule supplies every X-only turn used below.

BOTTOM. Suppose neither M_L edge is fully outgoing from d. Since {t,l} is not fully outgoing, at least one of dtl,dlt is bad; by boundary antisymmetry at least one of ltd,tld is tight. Since {r,s} is not fully outgoing, at least one of drs,dsr is bad; hence at least one of srd,rsd is tight. There are four cases.
(1) ltd and srd tight. If rdt were tight, then (l,s,r,d,t) would be a P5 because lsr is tight; hence rdt is bad and tdr is tight. Then (s,l,t,d,r) is a P5, using slt,ltd,tdr.
(2) ltd and rsd tight. If sdt were tight, then (l,r,s,d,t) would be a P5 because lrs is tight; hence sdt is bad and tds is tight. Then (r,l,t,d,s) is a P5, using rlt,ltd,tds.
(3) tld and srd tight. If rdl were tight, then (t,s,r,d,l) would be a P5 because tsr is tight; hence rdl is bad and ldr is tight. Then (s,t,l,d,r) is a P5, using stl,tld,ldr.
(4) tld and rsd tight. If sdl were tight, then (t,r,s,d,l) would be a P5 because trs is tight; hence sdl is bad and lds is tight. Then (r,t,l,d,s) is a P5, using rtl,tld,lds.
All four cases contradict P5-freeness, so some M_L edge is fully outgoing.

TOP. Suppose neither M_R edge is fully incoming to d. Since {t,r} is not fully incoming, at least one of trd,rtd is bad; hence at least one of drt,dtr is tight. Since {l,s} is not fully incoming, at least one of lsd,sld is bad; hence at least one of dsl,dls is tight. Again there are four cases.
(1) drt and dsl tight. If rds were tight, then (r,d,s,l,t) would be a P5 because slt is tight; hence rds is bad and sdr is tight. Then (s,d,r,t,l) is a P5, using sdr,drt,rtl.
(2) drt and dls tight. If ldr were tight, then (l,d,r,t,s) would be a P5 because rts is tight; hence ldr is bad and rdl is tight. Then (r,d,l,s,t) is a P5, using rdl,dls,lst.
(3) dtr and dsl tight. If tds were tight, then (t,d,s,l,r) would be a P5 because slr is tight; hence tds is bad and sdt is tight. Then (s,d,t,r,l) is a P5, using sdt,dtr,trl.
(4) dtr and dls tight. If tdl were tight, then (t,d,l,s,r) would be a P5 because lsr is tight; hence tdl is bad and ldt is tight. Then (l,d,t,r,s) is a P5, using ldt,dtr,trs.
Thus some M_R edge is fully incoming. This proves both extreme-gate existence clauses using only boundary antisymmetry and the transitive matching-height orientation of X.

## Theorem B — Wrong-polarity extreme gates are forbidden

Let X={a,b,c,z} be a transitive matching-height no-P4 four-cell with perfect matchings M_R>M_S>M_L, normalized by M_R={ab,cz}, M_S={ac,bz}, M_L={bc,az}. Let d be a fifth vertex and suppose X∪{d} is P5-free. Then no M_L-edge can be fully incoming to d: for every uv∈M_L, the two turns (u,v,d),(v,u,d) cannot both be tight. Dually, no M_R-edge can be fully outgoing from d: for every rs∈M_R, the two turns (d,r,s),(d,s,r) cannot both be tight. Equivalently, every bottom matching edge has at least one bad incoming orientation and every top matching edge has at least one bad outgoing orientation.

### Proof

In the matching-height cell the following X-turns are tight whenever used below: abc, acb, abz, zbc, zcb, zca and their matching-height equivalents.

BOTTOM. Suppose for contradiction that the bottom edge bc is fully incoming to d, so bcd and cbd are tight. Because X+d is P5-free, each displayed candidate below must fail at its sole not-yet-certified turn; boundary antisymmetry then certifies the complete reversal of that turn.
(1) (a,b,c,d,z) forces zdc.
(2) (a,b,z,d,c) forces dzb.
(3) (a,d,z,b,c) forces zda.
(4) (z,c,b,d,a) forces adb.
(5) (z,c,a,d,b) forces dac.
Now (z,d,a,c,b) is a tight P5, using zda,dac,acb, contradiction. Hence bcd and cbd cannot both be tight. Swapping simultaneously a↔c and b↔z preserves the matching-height structure and exchanges the two M_L edges, so the same holds for az.

TOP. Suppose for contradiction that the top edge ab is fully outgoing from d, so dab and dba are tight. Again use P5-freeness and boundary antisymmetry:
(1) (c,d,b,a,z) forces bdc.
(2) (b,d,c,a,z) forces acd.
(3) (b,a,c,d,z) forces zdc.
(4) (a,b,z,d,c) forces dzb.
(5) (a,d,z,b,c) forces zda.
Then (z,d,a,b,c) is a tight P5, using zda,dab,abc, contradiction. Swapping the two M_R edges gives the statement for cz. Therefore no bottom edge is fully incoming and no top edge fully outgoing.

## Theorem C — Middle matching gates alternate

Let X be a transitive no-P4 Strong Level-(1) four-cell. Write its three opposite-edge perfect matchings as M_R>M_S>M_L so that for distinct u,v,w in X, uvw is tight iff M(uv)>M(vw). Let d be a fifth vertex such that X union {d} has no tight Hamilton P5. Suppose an M_L-edge {t,l} is fully outgoing from d, meaning dtl and dlt are tight, and an M_R-edge {t,r} is fully incoming to d, meaning trd and rtd are tight. Let s be the fourth vertex of X. Then among the two M_S-edges {t,s} and {l,r}, exactly one is fully outgoing from d and the other is fully incoming to d. Equivalently, with A=[dts], B=[dst], C=[drl], D=[dlr], one has A=B, C=D, and A is not equal to C. In particular every P5-free fifth vertex over a transitive four-cell has a full gate in each matching class, with the middle-class gate orientation opposite on its two edges.

### Proof

Write M_R={{t,r},{l,s}}, M_S={{t,s},{l,r}}, M_L={{t,l},{r,s}}. The matching-height rule makes trl,lrs,tsr,rts,lst,stl,slr,rlt tight. Put A=[dts], B=[dst], C=[drl], D=[dlr]. We use only P5-freeness and boundary antisymmetry.

A implies B. Suppose A holds and B fails, so tsd is tight. If sdl were tight then (r,t,s,d,l) would be a P5, since rts is tight; hence lds is tight. If rld were tight then (t,r,l,d,s) would be a P5, since trl and lds are tight; hence D=dlr is tight. If tdl were tight then (t,d,l,r,s) would be a P5, since D and lrs are tight; hence ldt is tight. But then (l,d,t,s,r) is a P5 using ldt, A=dts, and tsr, contradiction. Thus A implies B.

B implies A. Suppose B holds and A fails, so std is tight. If tdr were tight then (l,s,t,d,r) would be a P5 using lst and std; hence rdt is tight. If lrd were tight then (s,l,r,d,t) would be a P5 using slr and rdt; hence C=drl is tight. If sdr were tight then (s,d,r,l,t) would be a P5 using C and rlt; hence rds is tight. But then (r,d,s,t,l) is a P5 using rds, B=dst, and stl, contradiction. Hence A=B.

C implies D. Suppose C holds and D fails, so rld is tight. If sdr were tight then (s,d,r,l,t) would be a P5 using C and rlt; hence rds is tight. If dst were tight then (r,d,s,t,l) would be a P5 using rds and stl; hence tsd is tight. If sdl were tight then (r,t,s,d,l) would be a P5 using rts and tsd; hence lds is tight. But then (t,r,l,d,s) is a P5 using trl, rld, and lds, contradiction. Thus C implies D.

D implies C. Suppose D holds and C fails, so lrd is tight. If tdl were tight then (t,d,l,r,s) would be a P5 using D and lrs; hence ldt is tight. If dts were tight then (l,d,t,s,r) would be a P5 using ldt and tsr; hence std is tight. If tdr were tight then (l,s,t,d,r) would be a P5 using lst and std; hence rdt is tight. But then (s,l,r,d,t) is a P5 using slr, lrd, and rdt, contradiction. Hence C=D.

It remains to show the two full M_S gates have opposite polarities. If A=C=0, then std and lrd are tight. P5-freeness of (l,s,t,d,r) forces tdr bad and hence rdt tight; then (s,l,r,d,t) is a P5, contradiction. If A=C=1, then B=D=1 by the equalities. P5-freeness of (r,d,s,t,l) forces rds bad and hence sdr tight; then (s,d,r,l,t) is a P5 using C and rlt, contradiction. Therefore A is not equal to C. Since A=B and C=D, exactly one M_S edge is fully outgoing from d and the complementary M_S edge is fully incoming. This proves the alternating middle-gate conclusion.

## Theorem D — A bidirectionally universal bridge dimer forces P5 or P6

Let X={a,b,c,z} be a transitive matching-height no-P4 four-cell normalized by M_R={ab,cz}>M_S={ac,bz}>M_L={bc,az}. Let u,v be distinct vertices outside X. Suppose (x,u,v) and (u,v,x) are tight for every x∈X. Then at least one of the following holds: X∪{u} supports a Hamilton P5, or X∪{u,v} supports a Hamilton P6. Equivalently, if X+u is P5-free and the six-set X+u+v is P6-free, a physical dimer uv cannot carry both universal polarities X→uv and uv→X.

### Proof

The matching-height rule gives the X-turns bac, czb, caz, bza tight. Since (c,u,v),(u,v,z) are tight, the candidate (b,a,c,u,v,z) would be a P6 if (a,c,u) were tight. Hence (a,c,u) is bad and boundary antisymmetry gives (u,c,a) tight. Since (b,u,v),(u,v,a) are tight, the candidate (c,z,b,u,v,a) would be a P6 if (z,b,u) were tight. Hence (z,b,u) is bad and boundary antisymmetry gives (u,b,z) tight. Now consider the five-set X+u. The candidate (b,u,c,a,z) has its last two turns (u,c,a) and (c,a,z) tight. P5-freeness therefore forces (b,u,c) bad, so boundary antisymmetry gives (c,u,b) tight. But then (c,u,b,z,a) is a Hamilton P5 on X+u: its turns are (c,u,b), (u,b,z), and the matching-height turn (b,z,a), all tight. Contradiction. Thus at least one of the claimed Hamilton paths exists.

## Why this is reusable

A P5-free fifth vertex over a transitive matching-height four-cell is forced into a rigid gate pattern: correctly polarized full gates exist on the extreme matching classes, wrong extreme polarities are forbidden, the middle gates alternate, and a universally bidirectional bridge dimer cannot persist without producing a Hamilton P5 or P6.

## Scope and nonclaims

This package is local to transitive matching-height no-P4 four-cells. It does not cover the cyclic four-cell, which is handled separately by `S9027`.

## Provenance

Rescued from accepted archived results `R549`, `R546`, `R534`, `R553`.
