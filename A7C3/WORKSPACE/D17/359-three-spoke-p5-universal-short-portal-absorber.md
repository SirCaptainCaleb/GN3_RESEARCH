# The retained three-spoke P5 absorbs every later proper trimer, hence every G27 short portal, into PAYABLE-FOUR

**Workspace:** D17
**State:** established
**Key:** `three-spoke-p5-universal-short-portal-absorber`

**Summary:** Retain one three-spoke source packet with distinct x,a,y,c,z, tight P5 K=(x,a,y,c,z), and three same-orientation source turns J_i=(a,b_i,c). Their boundary dimers (a,b_i) tail and (b_i,c) head form a permanent signed fossil fan. For any later proper trimer Q, if its tail dimer misses one source head dimer or its head dimer misses one source tail dimer, there is an immediate direct opposite-sign 2+2 birth. Avoiding all such births forces the tail dimer of Q to contain c and the head dimer to contain a, leaving only Q=(c,a,u),(u,c,a),(c,u,a). The extra P5 signs (a,y) head-signed by x and (y,c) tail-signed by z consume these three cases: for u!=y they give a direct disjoint 2+2 pair; for Q=(c,a,y) or (y,c,a) they give R523 collisions with distinct witnesses; Q=(c,y,a) is forbidden by R3 as the complete reversal of J_y=(a,y,c). Hence every later proper trimer yields a direct mass-four pair or raw R523 collision, and SV76748/SV79137 compile the collision to PAYABLE-FOUR. A bare adjacent selected-state reversal also enters the theorem: choose any third vertex w; R3 makes either (w,u,v) or (v,u,w) tight, carrying one of the two reversed selected states, so the resulting portal-linked trimer is absorbed. Thus the explicit R435/R436 short-portal alphabet is not an independent bottom species once the P5 fossil is retained; the remaining G27 obstruction is repeated flat payment ancestry, not portal type.


### 1. Permanent source fossil from the three-spoke P5
Fix a hypothetical smallest counterexample and one old endpoint pair

  E={a,c}.

Retain one exact H-E frame and the three same-orientation internal middles supplied by SV58280. Write them b_0,b_1,b_2, so

  J_i=(a,b_i,c) tight,  i=0,1,2.                         (UA.1)

Retain also the Hamilton order produced by the three-spoke lemma, relabelled

  K=(x,a,y,c,z),                                          (UA.2)

where {x,y,z}={b_0,b_1,b_2}. Thus

  (x,a,y), (a,y,c), (y,c,z) tight.                       (UA.3)

For every source middle b_i, (UA.1) gives the signed boundary dimers

  T_i=(a,b_i), tail-signed by c,
  H_i=(b_i,c), head-signed by a.                         (UA.4)

The P5 order supplies two additional signs on the central source dimers:

  H_*=(a,y), head-signed by x,
  T_*=(y,c), tail-signed by z.                           (UA.5)

All certificates in (UA.4)-(UA.5) are graph-intrinsic historical facts. They need not remain current through later payments.

### 2. Any later trimer either pairs directly with the source fan or is forced through E
Let

  Q=(q_0,q_1,q_2)                                        (UA.6)

be any later proper tight trimer. Its initial and terminal signed dimers are

  A_Q=(q_0,q_1), tail-signed by q_2,
  B_Q=(q_1,q_2), head-signed by q_0.                     (UA.7)

If A_Q is disjoint from one source head support H_i=(b_i,c), then A_Q|H_i is immediately a direct opposite-sign mass-four pair. If B_Q is disjoint from one source tail support T_i=(a,b_i), then T_i|B_Q is likewise a direct mass-four pair. In either case Q is already linked to a source-visible PAYABLE-FOUR birth by R514.

Assume therefore that neither direct pairing occurs. Then the two-set V(A_Q) meets all three distinct two-sets {b_i,c}. A two-set cannot meet all three through the three distinct b_i, so

  c in V(A_Q).                                           (UA.8)

Dually V(B_Q) meets all three {a,b_i}, hence

  a in V(B_Q).                                           (UA.9)

Because Q is vertex-simple, (UA.8)-(UA.9) leave exactly three ordered forms, with u distinct from a,c:

  Q=(c,a,u),  or  Q=(u,c,a),  or  Q=(c,u,a).             (UA.10)

No cyclic rereading of a certified turn is used here; these are the literal three possible positions of a,c under (UA.8)-(UA.9).

### 3. The P5 cross-signs consume all three residual orders
First let

  Q=(c,a,u).

Then B_Q=(a,u) is head-signed. If u!=y, B_Q is physically disjoint from the source tail dimer T_*=(y,c), so T_*|B_Q is a direct mass-four pair. If u=y, tightness of Q gives

  (c,a,y) tight,

while (UA.3) gives (x,a,y) tight. Thus the same tested oriented dimer (a,y) has two distinct HEAD witnesses c and x. Accepted R523 gives a same-oriented two-head collision.

Next let

  Q=(u,c,a).

Then A_Q=(u,c) is tail-signed. If u!=y, A_Q is physically disjoint from H_*=(a,y), giving the direct mass-four pair A_Q|H_*. If u=y, tightness gives (y,c,a), while (UA.3) gives (y,c,z). Hence the tested dimer (y,c) has two distinct TAIL witnesses a and z, an R523 two-tail collision.

Finally let

  Q=(c,u,a).

If u!=y, the initial tail dimer (c,u) is disjoint from H_*=(a,y), again giving a direct mass-four pair. If u=y, Q=(c,y,a) is the complete reversal of the retained tight source turn (a,y,c), so R3 says Q is bad. This contradicts the assumption that Q is tight.

Therefore every later proper trimer Q produces, using the retained source P5 packet, either

  DIRECT OPPOSITE-SIGN MASS-FOUR PAIR,
  or RAW R523 SAME-ORIENTED COLLISION.                    (UA.11)

The first output is PAYABLE-FOUR by R514. The second parent-compiles through SV76748 to P4/P5, a direct mass-four pair, or R407; SV78086 and SV79137 make every such output PAYABLE-FOUR. Thus every proper trimer is absorbed into the PAYABLE-FOUR interface with explicit source-P5/portal ancestry.

### 4. Bare adjacent reversal is trimerizable without losing portal ancestry
Suppose an R435/R436 portal is only an adjacent selected-state reversal on the physical dimer {u,v}: one retained state uses u->v and the other uses v->u, with no proper trimer yet named. Choose any physical w outside {u,v}. By R3 exactly one of

  (w,u,v),  (v,u,w)                                      (UA.12)

is tight. The first tight turn contains the selected state u->v as its terminal dimer; the second contains the reversed selected state v->u as its initial dimer. Hence (UA.12) supplies a proper trimer whose ancestry contains one of the two literal reversal states. Section 3 absorbs that trimer into PAYABLE-FOUR.

Likewise, any short R436 output already carrying a nontrivial signed dimer has its retained sign witness and therefore already sits inside a proper tight trimer. Reverse-trimer outputs are covered directly. Proper paths of order at least four and proper cycles of order at least four have already crossed the PAYABLE-FOUR boundary by SV78086. A proper tight 3-cycle contains a proper tight trimer as any three consecutive cyclic vertices; apply Sections 2--3 to that trimer.

Consequently, after the source packet (UA.1)-(UA.5) has been retained, the entire explicit short R435/R436 portal alphabet has a portal-linked route back to PAYABLE-FOUR.

### 5. G27 consequence and fence
The surviving bottom obstruction is therefore no longer a choice among adjacent reversal, reverse trimer, changed-outer-pair trimer, or short signed-contact species. All of them can be contracted to the same PAYABLE-FOUR interface while retaining the physical portal certificate and the fixed source P5 fossil.

This is not yet portal-stack extinction. A portal-linked PAYABLE-FOUR birth may be paid and may return rank-flat to E again. The theorem removes the PORTAL-TYPE coordinate from a reconstruction-closed bottom SCC; it does not prove that the remaining repeated-payment ancestry stack terminates. In particular no new numerical rank below Psi_E=(0,0,0) is claimed.

Alternative paid descendants are never treated as simultaneously current. Only the source P5 signs and the later portal/trimer are combined as graph-intrinsic historical certificates at the moment the new direct pair or collision is formed. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R514"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    }
]
```