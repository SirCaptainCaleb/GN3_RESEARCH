# The retained three-spoke genealogy makes every reciprocal P5 remint immediately two-coverable

**Workspace:** D17
**State:** established
**Key:** `three-spoke-reciprocal-p5-outer-p4-two-cover-collapse`

**Summary:** In the actual G27/G28 source genealogy, the P5 K=(u,a,m,c,v) is not an arbitrary P5: SV58280/SV83487 retain three same-orientation source turns (a,u,c),(a,m,c),(a,v,c). If the history-neutral branch of SV87107 reaches even one reciprocal cover H-{u,a}=(c,v)|Q, then Q is a Hamilton path on exactly V(H)-{u,a,c,v}. Apply R3 to the triple {u,c,v} with middle c. Either (u,c,v) is tight, giving the Hamilton P4 (a,u,c,v) from the retained turn (a,u,c), or (v,c,u) is tight, giving the Hamilton P4 (a,v,c,u) from (a,v,c). In either case this P4 has support exactly {u,a,c,v}, is disjoint from Q, and together with Q spans H as two tight paths. Hence the reciprocal-remint branch is impossible in the retained three-spoke application. No Q=Qprime synchronization, outgoing R176 test, R844 shield, or repeated-payment argument is needed. SV87107 remains a valid abstract arbitrary-P5 reduction; this section consumes its actual three-spoke descendant branch.

### 1. Restore the source genealogy suppressed by the P5 shorthand
The G27/G28 source packet is the three-spoke packet of SV58280 retained explicitly by SV83487. Before the later shorthand K=(u,a,m,c,v) is introduced, SV83487 records three distinct same-orientation source middles b_0,b_1,b_2 with

  J_i=(a,b_i,c) tight,  i=0,1,2,

and a Hamilton source order

  K=(x,a,y,c,z),  with {x,y,z}={b_0,b_1,b_2}.             (TG.1)

In the later firewall/remint notation x=u, y=m, z=v. Therefore the retained graph-intrinsic source packet contains, in addition to the consecutive turns of K, the three turns

  (a,u,c),  (a,m,c),  (a,v,c) tight.                     (TG.2)

The two outer turns in (TG.2) are the data that were hidden when the source packet was abbreviated to the literal P5 K alone. They remain historical graph facts through every later payment.

### 2. One reciprocal cover has the exact complementary support
Assume the maximally history-neutral branch reaches the reciprocal-cover conclusion of SV87107. It is enough to retain the first displayed reciprocal cover

  H-{u,a}=(c,v) | Q.                                     (TG.3)

Because (TG.3) is a literal exact two-cover of H-{u,a}, the tight path Q has vertex set

  V(Q)=V(H)-{u,a,c,v}.                                   (TG.4)

No information about the order of Q, the position of m in Q, or the second reciprocal cover is needed below.

### 3. The two unused source spokes Hamiltonize the deleted four-set
Apply boundary antisymmetry R3 to the three distinct vertices u,c,v with middle c. Exactly one of

  (u,c,v),  (v,c,u)                                      (TG.5)

is tight.

If (u,c,v) is tight, combine it with the retained source turn (a,u,c) from (TG.2). The consecutive turns

  (a,u,c), (u,c,v)

show that

  P=(a,u,c,v)                                             (TG.6)

is a literal tight Hamilton P4 on {a,u,c,v}.

If instead (v,c,u) is tight, combine it with the other retained source turn (a,v,c). Then

  P=(a,v,c,u)                                             (TG.7)

is a literal tight Hamilton P4 on the same four-set.

Thus, independently of the R3 branch, the physical four-set

  S={u,a,c,v}                                             (TG.8)

has a tight Hamilton P4 P.

### 4. The reciprocal remint closes immediately
By (TG.4), P and Q are vertex-disjoint and their supports partition V(H). Both are tight paths. Therefore

  H = P | Q                                               (TG.9)

is a spanning two-cover, contradicting the assumption that H is a counterexample.

Consequently the reciprocal-cover alternative of SV87107 cannot occur when K carries its actual SV58280/SV83487 three-spoke genealogy. In particular the common-rail reciprocal P5 remint cell targeted by G28 is empty before residual-rail synchronization, outgoing/incoming R176 choices, R844 insertion shields, or another PAYABLE-FOUR payment are considered.

### 5. Scope fence
The conclusion deliberately uses the two extra source turns (a,u,c) and (a,v,c). It does not claim that an arbitrary literal P5 K=(u,a,m,c,v) by itself forces the outer four-set {u,a,c,v} Hamiltonian. Thus SV87107 remains a legitimate abstract reduction for an arbitrary P5 carrying only its displayed P5 turns. The present theorem consumes the branch in the actual G27/G28 lineage, where SV83487 explicitly retains the full three-spoke source packet from SV58280.

No payment descendants are braided, no current representative is identified with a historical one, and R24/R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```