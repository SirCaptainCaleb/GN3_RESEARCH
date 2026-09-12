# Five virtual root branches compress to four literal anchor types or force collision/core geometry

**Workspace:** D17
**State:** established
**Key:** `virtual-five-root-anchor-link-tournament-compression`

**Summary:** Refine the SV58856 virtual five-root common-center packet at the exact R434 birth level. For each nonclosing root branch {d,xi}, run one xi-anchored selected-incidence channel only through the birth of its concrete signed dimer and retain that graph-intrinsic certificate before following any alternative descendant. A head birth (xi,u) with witness w is encoded by the link-tournament arc w->u at xi; a tail birth (u,xi) with witness w is encoded by u->w. Among five births, three share one polarity. In one polarity, if the same secondary u occurs with two distinct witnesses, accepted R523 gives an immediate same-oriented-dimer collision. Otherwise each secondary has one witness. For distinct secondaries u,v, the unique link orientation between them would provide a second same-polarity witness on the loser dimer unless the winner is exactly that loser's retained witness. Hence, outside R523 collision, every secondary has indegree at most one in the tournament induced by the secondaries. Such a tournament has at most three vertices; with three it is a directed 3-cycle, so the four-set consisting of xi and the three secondaries contains a directed comparison triangle and is universally one-vertex Hamilton-extendable by R902. Therefore outside collision/universal-core geometry each polarity uses at most two exact xi-anchored dimer+witness certificates. Both polarities together use at most four literal certificate types, so the five distinct SV58856 root lineages force two roots to share one identical concrete xi-anchored birth certificate. This upgrades virtual saturation to a bounded literal ancestor packet without asserting simultaneous current descendants. It does not itself extinguish the bottom family.


### 1. Input: the virtual five-root common-center packet
Retain the source packet of `global-completed-anchor-five-root-saturation` SV58856. Thus one common parent produces five alternative rooted continuations indexed by the five physical vertices d of one Hamilton P5 K. After the common R176 birth and payment/steering, each branch reaches an ancestry-bearing floor

  {d,xi},   d in V(K),

with one common physical center xi and the common upstream K / component-drop / cross-state ancestry retained.

Work in a nonclosing reconstruction-closed family at a stratum minimizing the global completed-anchor budget of SV58856. For each of the five root branches, choose one exact H-{d,xi} frame and one internal middle. Run the R434 selected-incidence channel anchored at xi, but stop immediately after its endpoint-anchored signed-dimer birth. If H closes during actualization, stop. Otherwise retain the born dimer, its exact witness, its tested orientation, the root d, the chosen frame and middle, and the common SV58856 ancestry. These five descendants need not be simultaneously current. The five signed-dimer certificates are graph-intrinsic and therefore may be compared in the common parent record.

The point is to upgrade VIRTUAL zero-quietness to a finite literal ancestor packet before any paid return is followed.

### 2. The link tournament at the common anchor
Fix xi. On V(H)-{xi}, define the physical link tournament L_xi by

  x -> y  iff  (x,xi,y) is tight.                          (VA.1)

Boundary antisymmetry R3 says exactly one of x->y or y->x holds for every distinct x,y outside xi.

Unpack one R434 birth.

- If the xi-channel is a HEAD birth, it has an oriented dimer

    D=(xi,u)

  head-signed by an exact witness w, so

    (w,xi,u) is tight.                                    (VA.2)

  In L_xi this is the arc w->u. Call u the SECONDARY of the birth.

- If the xi-channel is a TAIL birth, it has an oriented dimer

    D=(u,xi)

  tail-signed by an exact witness w, so

    (u,xi,w) is tight.                                    (VA.3)

  In L_xi this is the arc u->w, again with secondary u.

Thus every concrete xi-birth is one directed link edge together with the information of whether the secondary is the head-end or tail-end of that link edge.

### 3. Three same-polarity births: repeated secondary means collision or exact replay
Among five births, at least three have the same polarity. Treat HEAD; TAIL is the exact link-dual.

Retain a same-polarity family

  (xi,u_i) head-signed by w_i,
  equivalently w_i -> u_i in L_xi.                         (VA.4)

If u_i=u_j for two births but w_i!=w_j, then the same tested oriented dimer (xi,u_i) has two distinct head witnesses. Accepted R523 gives the explicit same-support two-head collision packet.

Therefore, outside R523 collision, every physical secondary u occurring in the family has one uniquely determined retained witness w(u). Multiple root branches using the same secondary must replay the identical graph-intrinsic dimer+witness certificate.

### 4. Distinct secondaries have link indegree at most one
Assume now that u and v are two distinct secondaries in the same HEAD family. Exactly one of

  u -> v,   v -> u                                        (VA.5)

holds in L_xi.

Suppose u->v. Then

  (u,xi,v) is tight,                                      (VA.6)

so u is a head witness on the tested dimer (xi,v). That dimer already has retained head witness w(v). If u!=w(v), accepted R523 again gives the two-head collision packet on (xi,v). Hence outside collision,

  u->v  implies  w(v)=u.                                  (VA.7)

Similarly,

  v->u  implies  w(u)=v.                                  (VA.8)

Consequently each secondary v can have at most one incoming edge from the set U of distinct secondaries: every such predecessor would have to equal the single physical vertex w(v).

But a tournament on m=|U| vertices has exactly m(m-1)/2 directed edges, while indegree at most one at every vertex would give at most m edges. Hence m<=3.

### 5. The three-secondary case is a universal four-core
If |U|=3, the three indegrees sum to three, so every secondary has indegree exactly one. Therefore L_xi[U] is a directed 3-cycle. Write it

  u_1 -> u_2 -> u_3 -> u_1.                              (VA.9)

The three certified tight turns

  (u_1,xi,u_2),
  (u_2,xi,u_3),
  (u_3,xi,u_1)                                            (VA.10)

form a directed comparison triangle on the three ordinary edges xi-u_1, xi-u_2, xi-u_3.

Put

  X={xi,u_1,u_2,u_3}.                                     (VA.11)

For every exterior z, the five-set X+z still contains this directed comparison triangle, hence is nonintegrable. Accepted R902 therefore makes X+z Hamiltonian. Thus X is a universally one-vertex Hamilton-extendable four-set.

No Hamiltonicity of X itself is asserted or needed.

The TAIL case is identical after reversing every link edge: three tail births with distinct secondaries and no collision again force a directed link triangle and the same universal-four-core conclusion.

### 6. Four literal ancestor types suffice outside explicit geometry
Therefore, for one fixed polarity, outside

  R523 SAME-SUPPORT COLLISION
  or UNIVERSAL ONE-EXTENSION FOUR-CORE,                    (VA.12)

there are at most two distinct secondary vertices, and Section 3 says each secondary carries at most one witness. Hence that polarity contributes at most two exact concrete xi-anchored birth certificates.

There are only two polarities. Therefore all five root-indexed R434 births together use at most four literal certificate types unless (VA.12) already occurs.

By pigeonhole, outside (VA.12) there exist two distinct roots d!=e in V(K) whose alternative xi-channels produce the IDENTICAL graph-intrinsic birth certificate:

  same tested oriented dimer,
  same polarity,
  same witness,
  same physical anchor xi.                                (VA.13)

The two root labels, source floors {d,xi},{e,xi}, exact source frames/middles, and the common SV58856 K/cross-state ancestry are retained as distinct historical provenance attached to this one literal ancestor certificate.

### 7. G26 meaning and fences
This is the desired VIRTUAL-TO-LITERAL bridge. SV58856 by itself says that five alternative roots are forced nonquiet at one virtual common center in a minimal global-anchor stratum. The present theorem says that before those nonquiet continuations separate, their first R434 births already form a bounded physical object:

  collision/core geometry,
  or at most four literal xi-anchored dimer+witness types shared by five roots.  (VA.14)

Thus failure of quiet completion does not leave an untyped cloud of five unrelated descendants. At least two distinct roots carry one identical concrete ancestor certificate.

This is NOT bottom-family extinction. An R523 collision or universal four-core is explicit geometry, not automatically closure at phase zero. Likewise exact replay of one xi-ancestor by two roots is a compression, not a contradiction. The next consumer should exploit the two distinct root ancestries attached to the same physical certificate, ideally by comparing their exact H-{d,xi} and H-{e,xi} source frames before payment/steering erases the distinction.

No simultaneous currentness of the five root descendants is asserted. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R434"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```