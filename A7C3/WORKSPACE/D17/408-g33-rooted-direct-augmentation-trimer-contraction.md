# The G33 bad seam reduces to strict descent or one source-rooted trimer

**Workspace:** D17
**State:** established
**Key:** `g33-rooted-direct-augmentation-trimer-contraction`

**Summary:** The explicit endpoint-favorable words used in SV103129 have only five L/R position patterns. Choosing the literal R540 cut by position gives a proposal with one hole such that, if the hole is bad, cutting one specified hole edge produces a tight spanning three-forest J with tau_X|B(J)=1 and with the omitted B-active source spoke s on a singleton or X-dimer component. This permits a direct rooted augmentation, bypassing the support-incidence case split. If s is singleton, add an old F-incidence at s. If s lies on a dimer, use the F-edge at the free matching copy of s; if that edge is the reverse dimer, reverse the dimer and simultaneously install the other old F-incidence at s. The operation has net matching excess one and joins the short s-component to another J-component. Any far-end copy competition or new bad turn yields, by R3, an exact tight trimer on a support containing s and the physical support of the relevant old F-incidence, but the tight trimer may reverse that incidence. If no such local blocker occurs, the result is an exact two-cover T with tau(T)<=2<3<=tau(F), a strict old-source descent. Hence every direct G33 packet reaches strict transition descent or one explicit source-rooted trimer support packet arising from an old F-incidence and a J-local state. The C4/repeated-crossing/R435 support-incidence outputs are no longer required to obtain a bounded obstruction, though they remain valid supplementary geometry.


### 1. Input
Retain the direct G33 packet. Thus

  G=H-{A,C}=X union V(B),
  X={v,p,q,r},

and F=F_1|F_2 is the actual old exact source two-cover with

  tau(F)>=3.                                               (RA.1)

The endpoint-favorable Hamilton P5 K_s omits a B-active source spoke s, and one actual old selected incidence s-h with h in B is retained. The literal R540 endpoint-cut construction has one uncertified turn. If that turn is tight, SV103129 already gives an exact two-cover of G with at most two transitions, hence strict descent. We therefore work only when the chosen one-hole turn is bad.

The purpose of this section is to choose the one-hole cut more sharply than merely tau<=2 and then augment the resulting three-forest directly at s.

### 2. The explicit forcing words admit a cut forest with exactly one transition
Read the literal candidate lists in Sections 3-4 of SV103129. Ignoring the names of the three X-vertices, every candidate used by those forcing chains places (L,R) in exactly one of the following five position pairs:

  (0,1), (4,0), (2,1), (3,2), (3,4).                      (RA.2)

No other endpoint pattern is used in the proof of existence of K_s. We choose a one-hole endpoint cut separately in these five patterns.

#### Pattern (0,1)
Write

  K_s=(L,R,x,y,z).

Use the left cut at L. Its proposal is

  (L,b_1,...,b_{m-1}) | (s,R,x,y,z),

with unique hole

  eta=(s,R,x).

The proposal has exactly the two transitions sR and Rx. If eta is tight we already have strict descent. If eta is bad, cut the selected edge sR. The result is a literal tight three-forest J with

  D_s=(s),   tau(J)=1.                                    (RA.3)

#### Pattern (4,0)
Write

  K_s=(R,x,y,z,L).

Use the right cut at R. The proposal is

  (s) | (b_1,...,b_{m-1},R,x,y,z,L),

with unique hole

  eta=(b_{m-1},R,x).

Its two transitions are Rx and zL. In the bad-hole branch cut Rx. Then again

  D_s=(s),   tau(J)=1.                                    (RA.4)

#### Pattern (2,1)
Write

  K_s=(x,R,L,y,z).

Use the right cut at R. The proposal begins with the literal dimer (x,s), while its other rail is

  (b_1,...,b_{m-1},R,L,y,z).

The unique hole is (b_{m-1},R,L), entirely inside B. The proposal already has exactly one transition, namely Ly. Cutting either edge of the bad hole therefore gives a literal tight three-forest with

  D_s=(x,s),   tau(J)=1.                                  (RA.5)

#### Pattern (3,2)
Write

  K_s=(x,y,R,L,z).

Use the left cut at L. The partner rail is the literal dimer (s,z), the unique hole is (R,L,b_1), and the proposal has exactly one transition yR. Cutting either edge of the bad hole gives

  D_s=(s,z),   tau(J)=1.                                  (RA.6)

#### Pattern (3,4)
Write

  K_s=(x,y,z,L,R).

Use the right cut at R. The proposal is

  (x,y,z,L,s) | (b_1,...,b_{m-1},R),

with unique hole

  eta=(z,L,s).

Its two transitions are zL and Ls. In the bad-hole branch cut Ls. Thus

  D_s=(s),   tau(J)=1.                                    (RA.7)

Combining the five literal forms, every nonexported direct packet has the following stronger canonical choice:

  J is a spanning tight three-path forest of G,
  tau(J)=1,
  and D_s is either (s) or a dimer on two X-vertices.       (RA.8)

This is a direct reading of the same human forcing words used in SV103129; no finite-search assertion is introduced.

### 3. A rooted repair operation
Encode J and F by their directed bipartite matchings M_J and M_F. Since s is internal in F and D_s has order at most two, at least one old F-incidence at s leaves D_s.

We construct a size-|G|-2 matching candidate using only the short component D_s and the old incidences at s.

#### 3a. Singleton root
If D_s=(s), both matching copies of s are free in M_J. Choose either old F-incidence e at s; in particular the retained old s-B incidence may be used. Its other endpoint lies in another J-component.

If the corresponding matching copy at the other endpoint is already occupied by a J-edge f, then e and f compete for one copy. R3 on their three physical endpoints gives one of the complete-reversal tight trimers. Retain that exact trimer. Its support contains s and the physical support of the named old incidence e, but its tight orientation need not select e in the old F direction.

Assume instead that the far copy is free. Then M_J+e is a matching with |G|-2 edges. Since e joins two different J-components, it cannot create a directed cycle and it merges the three J paths into two directed components.

#### 3b. Dimer root
Now D_s is a literal X-dimer. Let e_0 be the F-edge incident with the matching copy of s that is free in J.

If e_0 leaves D_s, use the one-edge augmentation M_J+e_0 exactly as in the singleton case.

The only alternative is that e_0 stays inside D_s. Because D_s has only two vertices, e_0 is then the exact reverse orientation of the J-dimer d. The other old F-incidence e_1 at s must leave D_s. Moreover the retained old s-B incidence is e_1, because both vertices of D_s lie in X. Form the repair

  M^* = M_J - d + e_0 + e_1.                              (RA.9)

At s the two installed edges e_0,e_1 are exactly the two old F-incidences and use opposite matching copies. At the other dimer vertex the reverse edge e_0 uses the copy that was free in J. Thus the only possible matching competition is at the far endpoint of e_1. If that copy is occupied by a J-edge, R3 again gives an exact tight trimer on the three-vertex collision support. That support contains s and the physical support of e_1, but the certified tight orientation may reverse e_1.

If no competition occurs, (RA.9) is a matching with |G|-2 edges. Removing d first splits the dimer into two singleton components; e_0 rejoins them in the reverse direction and e_1 attaches that reversed dimer to another old J-component. Hence the resulting directed graph has exactly two components and no directed cycle.

### 4. Every physical failure is a source-rooted R3 trimer
Assume the repair matching from Section 3 is compatible. Every unchanged consecutive turn is inherited from the tight forest J.

For a one-edge augmentation, the only new turns are the turns incident with the added old edge e. Hence each new turn contains s. If one is bad, R3 gives its complete reversal as a tight trimer on the same three-vertex support containing s. The trimer is tied to the physical support of e, but its tight orientation may reverse e.

For the reverse-dimer repair (RA.9), the turn through s is exactly the old F-turn determined by e_0 and e_1 and is therefore tight. The reverse-dimer endpoint is terminal. The only other possible new turn is at the far endpoint of e_1, so any bad turn there again has a complete-reversal tight trimer on a support containing s; again, the old e_1 orientation need not survive in the tight trimer.

Thus the repair has exactly two outcomes:

1. one explicit R3 trimer whose support contains s and whose construction retains the physical support of an actual old F-incidence at s together with the competing or adjacent J-state, without asserting retention of that F-incidence orientation; or
2. a literal exact two-cover T of G.                         (RA.10)

### 5. A successful repair is automatically a strict transition descent
In the singleton or one-edge dimer repair,

  tau(T)=tau(J)+chi(e_0)<=1+1=2.                           (RA.11)

In the reverse-dimer repair, d and e_0 both join two X-vertices and contribute no X|B transition, while e_1 contributes at most one. Therefore

  tau(T)=tau(J)-chi(d)+chi(e_0)+chi(e_1)<=2.               (RA.12)

Combining with (RA.1), every successful repair satisfies

  tau(T)<=2<3<=tau(F).                                     (RA.13)

So T is a strict old-source transition descent on the same top fiber and the same physical partition X|B.

### 6. G33 contraction
Every nonexported direct G33 packet therefore yields, without payment or replay and without a global support-incidence case split,

- an exact two-cover of G with strict old-source transition descent; or
- one exact tight R3 trimer on a three-vertex support containing the omitted B-active source spoke s, arising from a collision or bad mixed turn involving the physical support of an actual old F-incidence at s and one literal J-local competitor or neighbor.

The support-incidence theorem SV105952 and the rooted four-cell contraction SV106767 remain valid supplementary descriptions of the same defect-one packet, but they are no longer required merely to obtain a bounded physical obstruction. The surviving non-descent object is now one source-rooted three-vertex turn packet.

### 7. Scope
This theorem does not yet consume the final rooted trimer and therefore does not by itself close G33 or H. It preserves exactly the coordinates needed by the next consumer: s, its historical source trimer (A,s,C), the physical support and old orientation of an actual source-cover incidence at s, the chosen K_s/cut, and the J-local witness that blocked augmentation. The blocker trimer itself is retained in its exact certified orientation, which may reverse the old incidence. R24, R5, payment, and historical replay are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R540"
    }
]
```
