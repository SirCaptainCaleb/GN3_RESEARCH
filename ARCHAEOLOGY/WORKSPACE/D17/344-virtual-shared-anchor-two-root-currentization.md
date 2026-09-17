# Two roots sharing one virtual anchor certificate currentize on the common triple deletion

**Workspace:** D17
**State:** established
**Key:** `virtual-shared-anchor-two-root-currentization`

**Summary:** Consume the repeated-certificate branch of SV73012. Let distinct roots d,e at common center xi have exact source frames T_d on H-{d,xi} and T_e on H-{e,xi}, and suppose their xi-anchored R434 births are the identical tested dimer+polarity+witness certificate. That certificate determines one common physical source state {u,w}; each frame selects one of its two directions. Since u,w occur in both frames, they avoid d,e,xi. Puncture e from T_d and d from T_e. If either exchanged root is internal, the puncture is a literal three-cover of W=H-{d,e,xi}; smallest-counterexample minimality supplies an at-most-two cover and R159/R176 gives common-residue component-drop geometry. Hence only END/END is quiet. Then both punctures are exact two-covers of W preserving the common selected state. R410/R471 says different support partitions or different literal path orders already give a balanced-pair/R435 output; in particular opposite orientations of {u,w} are an explicit selected reversal. Thus the fully quiet residue has one identical exact cover F of W and the same source-state direction in both root frames. Relative to the common R434 certificate this direction is either INSERTABLE, in which case replacing the selected state by its certified xi-trimer gives a literal exact two-cover of H-{d,e}, or REVERSE, in which case the certificate itself is a source-pinned reverse trimer across the selected state of F. Therefore repeated virtual anchor types cannot remain an untyped two-root replay: they currentize to component drop, same-residue disagreement/reversal, a named pair-deletion cover, or a pinned reverse trimer.


### 1. Two distinct roots with one identical anchor certificate
Retain the repeated-certificate output of `virtual-five-root-anchor-link-tournament-compression` SV73012. Thus d and e are distinct root labels in the five-root source family, xi is the common physical center, and there are actual exact pair-deletion frames

  T_d = P_d|Q_d   of H-{d,xi},
  T_e = P_e|Q_e   of H-{e,xi}.                            (VR.1)

From one internal middle in each source frame, the xi-anchored R434 channel produces the IDENTICAL graph-intrinsic birth certificate: same tested oriented dimer, same polarity, same exact witness, and same physical anchor xi.

Treat HEAD polarity first. Write the common certificate as

  D=(xi,u) head-signed by w,
  so (w,xi,u) is tight.                                  (VR.2)

The TAIL case is the exact order-dual and is recorded in Section 5.

Unpack accepted R434 in either source frame. A head birth anchored at xi comes from a selected successor incidence at an internal middle. There are only two possibilities compatible with the fixed certificate (VR.2):

  DIRECT:  middle=w, successor=u, so the source frame selects w->u;
  REVERSE: middle=u, successor=w, so the source frame selects u->w. (VR.3)

In the REVERSE case the failed direct insertion turn is (u,xi,w), whose complete reversal is exactly the retained certificate (w,xi,u).

Thus each source frame selects the same physical state {u,w}, with one of the two directions in (VR.3).

Because u and w are vertices of both exact frames T_d and T_e, while d is absent from T_d and e is absent from T_e,

  {u,w} is disjoint from {d,e,xi}.                        (VR.4)

Hence the selected state survives every puncture below.

### 2. Puncture the opposite roots
Put

  W=H-{d,e,xi}.                                           (VR.5)

Puncture e from T_d and d from T_e.

If e is internal on its T_d rail, deleting e splits that nontrivial rail into two nonempty path pieces, while the other rail survives. Therefore T_d-e is a literal three-cover of W. Smallest-counterexample minimality R4 gives an at-most-two-path cover of the proper induced subsystem W. Accepted R159 then supplies a selected component-crossing and its R176 balanced-pair certificate. The same conclusion holds if d is internal in T_e.

Hence any branch in which at least one exchanged root is INTERNAL is already common-residue component-drop geometry. No comparison of the two paid descendants is needed.

The only potentially quiet branch is therefore

  e is an endpoint in T_d,
  d is an endpoint in T_e.                               (VR.6)

Pair-deletion rigidity makes every rail of T_d,T_e nontrivial. Deleting one endpoint from such a rail leaves a nonempty path. Thus

  F_d:=T_d-e,
  F_e:=T_e-d                                               (VR.7)

are literal exact two-covers of the SAME residue W, and the selected physical state {u,w} survives in each with its source direction.

### 3. Exact-cover rigidity on W
Apply accepted R410/R471 to F_d and F_e.

If their unordered rail-support partitions differ, R410 gives an actual selected cross-state and a graph-intrinsic balanced opposite-sign pair.

Assume their support partitions agree. If their literal Hamilton orders differ on a common support, R471/R435 gives an exact adjacent-state reversal, a reverse trimer, or a proper tight cycle. In particular, if the two source frames realize opposite directions in (VR.3), then F_d and F_e select the common physical dimer {u,w} oppositely, so the same-support order comparison is already explicit R435 geometry.

Therefore outside R410/R435 geometry the two punctured covers are literally identical up to rail exchange:

  F_d = F_e =: F,                                        (VR.8)

and they select the SAME direction of {u,w}. The two root frames consequently realize the same DIRECT/REVERSE role in (VR.3).

This is the only fully quiet repeated-certificate residue.

### 4. DIRECT role inserts xi and currentizes on H-{d,e}
Suppose the common role is DIRECT. Then the literal common cover F selects

  w -> u,                                                  (VR.9)

and the shared certificate gives

  (w,xi,u) tight.                                         (VR.10)

Replace the selected state w->u in its F-rail by the two-state segment

  w -> xi -> u.                                           (VR.11)

Only one new turn is required, namely (VR.10), so the modified rail remains tight. The other F-rail is untouched. Since F spans W, the two resulting rails span

  W union {xi}=H-{d,e}.                                   (VR.12)

Thus the repeated virtual anchor certificate has produced a NAMED literal exact two-cover of the pair-deletion residue H-{d,e}, with the whole common W-cover and the exact insertion site retained.

This is a genuine currentization of the two-root replay onto its own deleted root pair. No payment descendant is used.

### 5. REVERSE role is a pinned reverse trimer
Suppose instead the common role is REVERSE. Then F selects

  u -> w,                                                  (VR.13)

while the retained certificate is

  (w,xi,u) tight.                                         (VR.14)

The direct insertion turn (u,xi,w) is the complete reversal of (VR.14) and is bad. Hence (VR.14) is an explicit source-pinned reverse trimer across the selected F-state u->w, with the common exact cover F, roots d,e, center xi, and tested certificate orientation all retained.

The TAIL case is the exact dual. If the common certificate is

  D=(u,xi) tail-signed by w,
  so (u,xi,w) is tight,

then DIRECT means the source frames select u->w and xi inserts between them to give an exact H-{d,e} cover; REVERSE means they select w->u and the tight trimer (u,xi,w) is the pinned reverse cell.

### 6. Two-root currentization theorem
Combining the cases:

> Two distinct virtual roots sharing one identical xi-anchored R434 birth certificate cannot remain an untyped replay. Before any further payment they yield at least one of:
> 1. common-triple-deletion component-drop/R176 geometry because an exchanged root is internal;
> 2. R410 support-partition disagreement on the common triple deletion;
> 3. R435 selected reversal/reverse-trimer/cycle because the two endpoint punctures differ in order, including opposite directions of the certificate state;
> 4. one literal common exact cover F of H-{d,e,xi} in the DIRECT role, where the certificate inserts xi and gives a named exact two-cover of H-{d,e};
> 5. one literal common exact cover F of H-{d,e,xi} in the REVERSE role, where the certificate is a pinned reverse trimer across F's selected certificate state.

Thus the repeated-certificate output of SV73012 has an explicit codimension-three/codimension-two current interface. The two distinct root ancestries remain visible all the way to that interface.

### 7. Scope fence
This is not bottom-family extinction. The R159/R176, R410, R435 and reverse-trimer outputs are typed geometry, not automatically a global decrease. The DIRECT pair-deletion cover is a current representative, not by itself progress from a phase-zero source. No claim is made that later paid descendants coexist with the source frames.

The theorem only removes one ambiguity demanded by G26: two virtual root branches sharing one literal ancestor certificate cannot disappear into indistinguishable payment histories. Their difference is currentized on the common deleted roots or exposed as a source-pinned reversal cell before payment.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R410"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R471"
    }
]
```