# A dimer-root three-cover gives bounded fresh-edge responses on four of its six merge seeds

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-dimer-root-local-double`

**Summary:** Choose any oriented physical dimer D=(x,y). R4 gives an exact two-covered complement U|V, so D|U|V is a maximum three-cover; R3 shows neither U nor V can be a singleton. For a DOUBLE seed y->u0 from D into U, the two bad endpoint turns reverse to the tight P4 (u1,u0,y,x). If U is a dimer this P4 together with V already closes H. Otherwise the P4, the literal residual suffix U[2,r], and V form another maximum three-cover differing from the dimer-root cover in exactly three deleted and three fresh selected edges. The U->D DOUBLE is the terminal dual, and the same holds for V. Combined with the unique distance-two SLIDE response from SV22098, every one of the four seeds touching the dimer has a bounded local alternative: distance two for SLIDE or a fresh reverse-P4 distance-six rebuild for DOUBLE. Only the U<->V pair lacks this special dimer-local response. The DOUBLE rebuild intentionally uses fresh reversed edges, so it is outside the R989 fixed-selected-union fence. This is a normalization/escape interface, not an augmentation theorem.

### 1. Canonical dimer-root base
Let H be a hypothetical smallest counterexample and choose any two distinct physical vertices x,y. The oriented dimer

  D=(x,y)

is vacuously tight. By accepted R4 its complement has exact path-cover number two; retain one literal exact cover

  H-{x,y}=U|V.

Thus

  F=D|U|V                                             (DB.1)

is a maximum spanning compatible three-forest. Neither U nor V can be a singleton. Indeed, if U={u}, the three-set {x,y,u} has a Hamilton tight trimer by R3, and that trimer together with V would two-cover H. Hence

  |U|,|V|>=2.                                         (DB.2)

The orientation of D may be chosen freely at the outset; no tight turn is used inside a dimer.

### 2. A DOUBLE seed from the dimer has an exact local reverse-P4 rebuild
Write

  U=(u_0,u_1,...,u_r),   r>=1.

First use the ordered seed from D into U, namely y->u_0. If it is DOUBLE in the sense of SV22098, the two bad turns are

  (x,y,u_0),   (y,u_0,u_1).

R3 gives the literal reverse P4

  K^+_U=(u_1,u_0,y,x).                                 (DB.3)

If |U|=2 then K^+_U spans D union U, so K^+_U|V is already a spanning two-cover, impossible. Therefore a surviving DOUBLE has |U|>=3. In that case

  K^+_U | (u_2,...,u_r) | V                           (DB.4)

is itself a spanning maximum three-cover. No arbitrary recompletion of H-K^+_U is required. Relative to F it deletes exactly

  x->y,  u_0->u_1,  u_1->u_2

and adds exactly

  u_1->u_0,  u_0->y,  y->x,

so it is a six-edge symmetric-difference move. For |U|=3 the residual U-rail is the singleton u_2, with the same count.

The seed from U into D is the exact terminal dual. If u_r->x is DOUBLE, then

  K^-_U=(y,x,u_r,u_{r-1})                              (DB.5)

is tight; |U|=2 would close with V, while for |U|>=3

  (u_0,...,u_{r-2}) | K^-_U | V                       (DB.6)

is a local maximum three-cover at symmetric-difference distance six.

Exactly the same statements hold with V in place of U.

### 3. Dimer-incident seeds are bounded local cells
By SV22098, a singly blocked dimer-incident seed is a SLIDE and has its unique distance-two response. Section 2 shows that a DOUBLE dimer-incident seed, although its closest representative CONTAINING the attempted directed seed edge may still require a global collision reconstruction, always has a different explicit fresh-edge maximum representative at distance six, obtained by reversing the seed edge together with the adjacent dimer and rail-boundary edges.

Thus the four ordered seeds between D and U,V have the bounded alternative

  SLIDE at distance 2,
  or reverse-P4 rebuild at distance 6.                 (DB.7)

The only two ordered seeds of the dimer-root base for which no such dimer-local bounded response is supplied are the pair U->V and V->U.

This is precisely outside the R989 fixed-union fence: the DOUBLE response deliberately introduces the reversed seed and reversed boundary edges, which need not belong to any previously selected-edge union.

### 4. Short-rail consequence
A DOUBLE seed can never join two dimer rails in a counterexample, because its reverse P4 spans both rails and the untouched third rail completes a spanning two-cover. More generally, whenever one participating rail is the distinguished dimer D, the opposite rail of a surviving DOUBLE has order at least three and the response (DB.4) or (DB.6) is completely local.

Hence any attempt to prove Simultaneous Physical Merge Escape may normalize first to a dimer-root forest (DB.1). Four of the six physical merge seeds then have explicit bounded fresh-edge alternatives; genuinely unbounded charged transport need only be invoked after these local representatives have been consumed, or directly on the U<->V pair.

No theorem is claimed that the distance-six reverse-P4 response itself augments H, nor that iterating these bounded moves is monotone.
