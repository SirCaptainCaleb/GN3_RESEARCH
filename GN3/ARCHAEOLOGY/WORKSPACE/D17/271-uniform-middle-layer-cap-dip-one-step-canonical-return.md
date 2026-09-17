# Every fixed-cap parity dip has a zero-or-one-step canonical return, and any returned cap is transverse to the source cap

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-cap-dip-one-step-canonical-return`

**Summary:** Take either explicit equal-parity cap-dip forest produced in SV46809 and mark its Hamilton core D_uv on Omega-{u,v}, of order k-1. For k>=6 this is a largest rail (at k=6 in the P5 branch it may tie the order-five splice rail, and we choose D_uv). Every marked A-growth SLIDE increases D_uv by exactly one vertex, so one successful move reaches order k and a second would create a forbidden tight (k+1)-path in R927(M). Hence any A-growth history has length at most one. Moreover, outside augmentation/trimer/cycle portals there cannot be two distinct first growth moves: SV41625 makes same-end competition a trimer portal, while two opposite-end portal-free moves would complete to an A-growth square whose common endpoint has marked rail order k+1, impossible. Thus the portal-free canonical A-growth normal form is either the dip forest itself or one unique one-SLIDE terminal cap forest. In the latter case the returned cap is D_uv plus one donor vertex from C union {u,v}; it therefore contains at least k-1 Omega vertices and at most one vertex of the original cap C, so it is never C. This answers the regrowth part of G18 sharply: the cap dip is not by itself global Morse descent, but its canonical return has depth at most one and cannot erase the excursion by returning to the source cap. Working/unreviewed exposition only.


### 1. Start from the explicit equal-parity dip forest
Assume accepted R927(M) in the live range k>=6 and fix the same literal cap

  C=(c_0,...,c_{k-1}),
  Omega=V(H)-V(C)

as in SV46809. Let u->v be any actual endpoint incidence in Omega with

  chi_C(u)=chi_C(v).                                      (CR.1)

Retain the actual puncture path P_u exposing v and put

  D_{uv}=P_u-v.                                           (CR.2)

Then D_{uv} is a literal Hamilton path on Omega-{u,v}, of order k-1, and

  H-{u,v}=C | D_{uv}.                                     (CR.3)

The equal-parity construction in SV46809 gives one of two explicit maximum three-forests.

If both bits are one, the R584/wall splice produces a P5 S_5 and

  F_dip = S_5 | C[2,k-2] | D_{uv},                        (CR.4)

with rail orders

  5, k-3, k-1.                                            (CR.5)

If both bits are zero, the splice produces a P4 S_4 and

  F_dip = S_4 | C[1,k-2] | D_{uv},                        (CR.6)

with rail orders

  4, k-2, k-1.                                            (CR.7)

In both cases D_{uv} is a largest rail. In the only tie relevant here, k=6 in (CR.5), both S_5 and D_{uv} have order five; choose D_{uv} as the marked largest rail. Denote it by A.

### 2. Marked A-growth has length at most one
Every A-GROWTH rewrite of SV41625 is an inward endpoint SLIDE which transfers exactly one endpoint vertex of another rail into the marked physical descendant of A. Therefore

  |A|=k-1 -> k                                             (CR.8)

after one successful rewrite.

A second A-growth rewrite would make the marked descendant have order k+1. But accepted R927(M) says no (k+1)-set supports a Hamilton tight path. Hence no second rewrite exists.

Thus every marked A-growth history beginning at F_dip has length zero or one. In particular the apparently dangerous regrowth after the cap dip is not a long process.

### 3. Two competing first growth moves already expose a portal
There is a stronger local-confluence consequence. Suppose two distinct A-growth rewrites are both available from F_dip.

If they enter the same end of A, Section 2 of SV41625 applies: the two added edges compete for the same endpoint copy, and R3 gives a current proper trimer portal.

Suppose they enter opposite ends. SV41625 applies the complete one-edge interaction theorem. Outside augmentation, current-trimer, and current-cycle outputs, the two moves complete to an exact A-growth square. The common lower corner of that square performs BOTH endpoint additions to the same marked descendant of A and therefore has marked rail order

  (k-1)+2=k+1.                                            (CR.9)

Such a literal tight rail is forbidden by R927(M). Consequently the square branch cannot occur.

Therefore:

> Outside an immediate augmentation/trimer/cycle portal, F_dip has at most ONE available A-growth rewrite.                 (CR.10)

Combined with termination, this means the portal-free canonical normal form N_A(F_dip) of SV41625 is literal and choice-free in the strongest possible sense: it is either F_dip itself or the endpoint of one unique A-growth SLIDE.

### 4. Any one-step returned cap is transverse to the old cap
Assume the unique growth move exists. Let x be the transferred donor endpoint and let

  K = V(D_{uv}) union {x}                                 (CR.11)

be the support of the resulting marked k-rail.

Because the other two rails of F_dip partition the complement of D_{uv}, their union is exactly

  V(C) union {u,v}.                                       (CR.12)

Hence

  x in V(C) union {u,v}.                                  (CR.13)

But

  V(D_{uv})=Omega-{u,v}                                   (CR.14)

already contains k-1 vertices of Omega. Therefore the returned cap K satisfies

  |K intersect Omega| >= k-1,
  |K intersect V(C)| <= 1.                                (CR.15)

Since k>=6,

  K != V(C).                                              (CR.16)

Indeed the returned cap is nearly complementary to C: it consists of all but at most two vertices of Omega plus at most one old-cap vertex. No canonical A-growth return from the parity dip can silently restore the source cap.

The one-step state is terminal for marked A-growth, because another growth would again create order k+1.

### 5. Canonical-return theorem and the remaining Morse comparison
We have proved:

> ONE-STEP CAP-DIP RETURN. Every explicit equal-parity dip forest of SV46809, marked on its k-1 puncture core D_{uv}, has exactly one of the following outcomes:
>
> 1. an immediate augmentation/current-trimer/current-cycle portal appears in the A-growth critical-pair analysis;
> 2. no A-growth move exists, so the dip forest itself is the canonical terminal marked forest;
> 3. exactly one portal-free A-growth move exists, and its endpoint is the canonical terminal forest with a k-cap K satisfying |K intersect C|<=1.
>
> In particular portal-free canonical regrowth has length at most one and never returns to the source cap C.

This resolves the REGROWTH part of Guidance G18's warning but not the full checkpoint comparison. The temporary k-1 dip still cannot simply be declared a decrease of the phased rank: after the zero-or-one-step forest normalization one must compare the resulting fixed-turn/payment checkpoint with the pre-curvature checkpoint. What is now eliminated is arbitrary regrowth ambiguity. The remaining equality problem is concentrated in one terminal dip state, one transverse cap state, or an explicit trimer/cycle portal.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    }
]
```