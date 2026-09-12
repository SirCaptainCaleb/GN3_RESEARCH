# Either R582 omits a source-to-spectator spoke or the source incidences are one middle-matching edge

**Workspace:** D17
**State:** established
**Key:** `g32-source-active-r582-middle-matching-reduction`

**Summary:** In the G32 transitive singleton-star spectator frame, call a source spoke B-active when the retained source cover U|V selects an edge from it into the spectator rail B. At least two of p,q,r are B-active: if two spokes were B-inactive, both would have selected degree two entirely inside X={v,p,q,r}, forcing the selected X-subgraph to be a spanning P4, contrary to X being P4-free. The prescribed-avoidance proof of SV99957 sharpens pairwise. After normalizing the L-outgoing M_S edge to {b,z}, in the ALIGNED gate each of b,z is individually favorable-omittable, so every target pair except the complementary M_S edge {a,c} contains a forceable omission. In the CROSSED gate every target pair meeting both M_S edges admits a favorable omission in that pair, by four explicit short P660-style forcing chains; only the two M_S edges themselves remain exceptional. Hence either some endpoint-favorable K_s omits a B-active source spoke s, retaining an actual old selected s-B incidence, or exactly two source spokes are B-active and they are the two vertices of one exceptional M_S edge; the complementary M_S edge consists of the singleton center v and the unique B-inactive source spoke. This is a coordinate reduction for the full-H splice, not extinction.


### 1. Source-active spokes
Retain the G32 transitive singleton-star spectator frame and the source crossing floor of SV100350. Thus

  X={v,p,q,r},
  B=(b_0,...,b_m),
  H-{a,c}=U|V,

X is P4-free, p,q,r are internal in the literal source cover U|V, and U|V has at least three selected X|B transitions.

Call a source spoke s in {p,q,r} B-ACTIVE if at least one of its two selected source-cover neighbors lies in B.

At least two source spokes are B-active. Indeed, suppose two distinct spokes s,t were B-inactive. Because both are internal in U|V, each has selected degree two, and both incident selected edges lie inside X. The selected-edge graph induced on X is a subgraph of the two-path forest U|V, hence is itself a forest of maximum degree two. A forest on four vertices containing two distinct degree-two vertices must be the spanning four-vertex path: the two degree-two vertices lie in one path component, and that component needs at least four vertices. Therefore X would contain a literal selected Hamilton P4, contradicting the G32 P4-free cell. Thus

  at least two of p,q,r are B-active.                    (SA.1)

This strengthens the anonymous transition count by attaching the source crossings to physical source spokes.

### 2. Pair-target refinement of prescribed-avoidance R582
Use the pure R582 notation temporarily. Let the transitive matching-height cell be

  {a,b,c,z},
  M_R={ab,cz} > M_S={ac,bz} > M_L={bc,az},

and normalize the L-outgoing M_S edge to {b,z}, exactly as in P660 and SV99957.

#### 2a. Aligned gates
When the R-incoming M_S edge is also {b,z}, the proof of SV99957 gives more than prescribed-singleton avoidance.

The chain

  L R c a z,
  z c a L R,
  z c R L a,
  R c z a L,
  c R L a z

uses only Hamilton P5s omitting b. Assuming no endpoint-favorable P5 omits b, the first four candidates successively force cRL, RLa, Rcz, Laz, and the fifth is then a forbidden endpoint-favorable P5. Hence b itself is favorable-omittable.

The dual chain

  L R a c b,
  b a c L R,
  b a R L c,
  R a b c L,
  a R L c b

uses only P5s omitting z and proves that z itself is favorable-omittable.

Consequently every two-element target set other than the complementary M_S edge {a,c} contains a vertex that can be omitted by an endpoint-favorable R582 path. The only pair not controlled by this argument is {a,c} itself.

#### 2b. Crossed gates
Now the R-incoming M_S edge is {a,c}; the two exceptional same-matching pairs are therefore {a,c} and {b,z}. Every cross pair admits a target-preserving forcing chain. In each row, assume no endpoint-favorable P5 omits either member of the displayed target pair. Every listed candidate omits a member of that pair, has two already-tight consecutive turns, and is endpoint-favorable; its remaining turn is therefore bad and R3 supplies the displayed reverse. The final candidate is then tight and gives the contradiction.

Target {a,b}:

  R z c a L   -> czR,
  z c a L R   -> RLa,
  c z R L a   -> LRz,
  L R z b c   tight.

Target {a,z}:

  L R z b c   -> zRL,
  b a c L R   -> RLc,
  R z b c L   -> Lcb,
  z R L c b   tight.

Target {b,c}:

  L R b z a   -> bRL,
  R b z a L   -> Laz,
  b R L a z   -> aLR,
  z c a L R   tight.

Target {c,z}:

  R b a c L   -> abR,
  b a c L R   -> RLc,
  a b R L c   -> LRb,
  L R b z a   tight.

Thus in the crossed gate every pair meeting both M_S edges contains an endpoint-favorably omittable vertex. Only the two M_S edges themselves are left exceptional by this pair-target theorem.

### 3. Apply the pair theorem to the actual B-active source spokes
Return to X={v,p,q,r}. The pure gate labels above are only temporary coordinates; transport the pair-target conclusion through the matching-height automorphism used to normalize the live R582 packet.

Let A be the set of B-active source spokes. By (SA.1), |A|>=2.

If the live gate is ALIGNED and A is not exactly the exceptional complementary M_S edge, then A contains a target pair controlled by Section 2a, so some endpoint-favorable K_s omits a B-active source spoke s. Retain one actual selected old source edge s-h with h in B.

If the live gate is CROSSED and A meets both M_S edges, choose one active spoke from each. Section 2b forces an endpoint-favorable K_s omitting one of those two active spokes, again retaining its actual old s-B incidence.

Therefore, if NO endpoint-favorable R582 path omits a B-active source spoke, the source incidence pattern is rigid:

  * exactly two source spokes are B-active;
  * those two spokes are the two vertices of one exceptional M_S edge;
  * the complementary M_S edge consists of the singleton center v and the unique B-inactive source spoke.                 (SA.2)

For an aligned gate the active edge is specifically the M_S edge complementary to the common L-outgoing/R-incoming edge. For a crossed gate either M_S edge may be the active pair.

### 4. Full-H splice interface
The easy branch now retains more than the G32 prescribed-avoidance theorem: the omitted source spoke s comes with

  * its source trimer (a,s,c),
  * an endpoint-favorable cross-end P5 K_s,
  * and an actual selected old source incidence s-h with h in B.

These three pieces coexist in the same graph and the s-h edge belongs to the retained old source representative. Any full-H endpoint-cut proof may therefore use a real source-to-spectator seam at the omitted spoke rather than an anonymous source-crossing count.

The only branch where this source seam cannot be attached to the omitted spoke by the present forcing theorem is the rigid middle-matching residue (SA.2). There the exact active M_S edge, complementary center/inactive-spoke M_S edge, and all actual source X|B incidences are retained for a separate finite splice.

### 5. Scope
This theorem is a coordinate-preserving reduction, not frame absorption. It does not claim that a B-active omitted spoke already yields a spanning two-cover, and it does not count an R159/R523/PAYABLE-FOUR output as progress. The pair-target forcing chains use only R3 and the live R582 gate data. The source activity statement uses only the literal old source cover and P4-freeness of X. No finite search is used as proof. R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
