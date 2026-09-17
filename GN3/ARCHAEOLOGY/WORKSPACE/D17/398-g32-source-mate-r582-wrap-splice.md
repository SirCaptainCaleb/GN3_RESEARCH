# A source-mate R582 path reduces the full-H splice to one pure spectator wrap seam

**Workspace:** D17
**State:** established
**Key:** `g32-source-mate-r582-wrap-splice`

**Summary:** Let A,C be the source anchors, let s,t be distinct source spokes with retained turns (A,s,C),(A,t,C), and write L=b0,R=bm for the spectator endpoints. If an R582 Hamilton P5 omitting s has the literal form (t,R,L,x,y), then the four-set {A,C,s,t} has a tight Hamilton P4 by one R3 test, while (b1,...,b_{m-1},R,L,x,y) is a spanning complementary path with exactly one uncertified turn, the pure spectator wrap seam (b_{m-1},R,L). Thus in a counterexample that seam is bad and its exact reverse (L,R,b_{m-1}) is tight. Dually, a path (x,y,R,L,t) omitting s leaves only the wrap seam (R,L,b1), whose reverse (b1,L,R) is tight. If both source-mate forms occur, the two spectator wrap seams are simultaneously bad; for |B|>=4 their reversals concatenate to the boundary P4 (b1,L,R,b_{m-1}), while for |B|=3 they give the corresponding tight three-cycle. This is a full-H one-hole reduction, not closure in the both-bad branch.

### 1. Setup
Retain the G32 spectator frame with global source anchors A,C, source spokes p,q,r, transitive cell X={v,p,q,r}, and spectator path

  B=(b_0,b_1,...,b_{m-1},b_m).

Write L=b_0 and R=b_m. Let s,t be two distinct source spokes. The retained source packet contains

  (A,s,C) and (A,t,C) tight.                         (WS.1)

Let x,y be the two remaining vertices of X-{s,t}. Suppose an R582 Hamilton P5 K_s on {L,R} union (X-{s}) omits s and has one of the two source-mate forms below.

### 2. The source four-set is Hamilton
Test the ordered triple (t,A,s). If it is tight, then

  (t,A,s,C)

is a tight P4 by (WS.1). If it is bad, R3 gives (s,A,t) tight, and then

  (s,A,t,C)

is a tight P4. Hence in either case the four-set

  {A,C,s,t}                                             (WS.2)

has a literal Hamilton P4 Q_{s,t}. This uses the actual source turns and fixes all anchor bookkeeping at once.

### 3. Right-cut source-mate form
Assume

  K_s=(t,R,L,x,y).                                      (WS.R)

Consider

  P_R=(b_1,b_2,...,b_{m-1},R,L,x,y).

Its support is V(B) union (X-{s,t}), disjoint from Q_{s,t}, and the two supports together are V(H). Every consecutive turn of P_R is inherited either from B or from K_s except exactly

  beta=(b_{m-1},R,L).                                   (WS.3)

Indeed the final inherited B turn reaches b_{m-1}, the next K_s turns are (R,L,x) and (L,x,y), and no anchor or source-spoke seam remains. Therefore if beta is tight,

  P_R | Q_{s,t}

is a spanning two-path cover of H. In a hypothetical counterexample beta must consequently be bad, and R3 gives the graph-intrinsic reverse seam

  (L,R,b_{m-1}) tight.                                  (WS.4)

This is the full-H analogue of the right R540 cut, but no R540 bad-hole inference is imported: badness follows directly from the explicit full-H two-path proposal.

### 4. Left-cut source-mate form
Dually assume

  K_s=(x,y,R,L,t).                                      (WS.L)

Then

  P_L=(x,y,R,L,b_1,b_2,...,b_{m-1})

again has support complementary to Q_{s,t}. Every turn is inherited from K_s or B except exactly

  alpha=(R,L,b_1).                                      (WS.5)

If alpha were tight, P_L|Q_{s,t} would two-cover H. Thus alpha is bad and R3 gives

  (b_1,L,R) tight.                                      (WS.6)

### 5. Simultaneous two-ended residue
If source-mate paths of both forms (WS.R) and (WS.L) are available, possibly with different ordered source pairs (s,t), then both pure spectator wrap seams alpha and beta are bad. Their exact reversals (WS.4),(WS.6) coexist. If b_1 and b_{m-1} are distinct, they concatenate to the literal tight boundary P4

  (b_1,L,R,b_{m-1}).                                   (WS.7)

If b_1=b_{m-1}, the two reverse turns instead give the corresponding tight three-cycle on {b_1,L,R}; no four-vertex claim is made in that short degeneracy.

### 6. Scope
This is a conditional full-H splice theorem. It identifies a particularly strong R582 placement: once the omitted source spoke s is paired on the cut-off side with another source spoke t, the anchors are absorbed by the source P4 and the entire failure is pushed onto one pure B wrap seam. The theorem does not assert that every G32 packet supplies one or both source-mate forms, and the simultaneous reverse boundary P4/cycle is retained as geometry rather than declared closure. No R159, R407, R523, PAYABLE-FOUR, R24, or R5 is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
