# A three-cover collision system has at most three gains, and a blocked merge seed reaches a loss surplus

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-three-gain-root-pressure`

**Summary:** For two maximum compatible spanning three-forests, symmetric-difference gain components use distinct unmatched terminal/source copies of the base forest, so there are equally many gains and losses and at most three of each. Gains therefore form a partial physical matching between the three base terminals and three base sources. Using the corrected SV20847 minimizing class, a prescribed merge edge t->s is an isolated +1 component even when it is not a separate dimer rail. Project the collision preorder to the charged components P union N by inherited reachability through arbitrary zero-weight corridors. Full upper sets project to charged upper sets without changing weight, and the full upward closure of any charged upper set contains exactly those charged components, so positive-weight upper-set existence is exactly an at-most-six-node charged-preorder question. In the acyclic branch, for a closest edge-containing representative, the charged closure of the seed either has strictly more losses than gains or contains every charged component; in the latter case corrected CP.8 forces its full closure to be the entire symmetric-difference system. Thus zero-corridor length is not the remaining weighted obstruction. The live target is physical: show that the six ordered terminal-to-source merge seeds of one base three-cover cannot all induce nonaugmenting charged preorders compatible with their actual collision witnesses. In the cyclic branch cycle supports and break data remain essential because charged projection does not preserve cycle debt.

### 1. Gain and loss count in a spanning three-cover comparison
Retain the corrected matching/collision-preorder setup of `compatible-forest-collision-preorder` SV20847 for two spanning compatible three-forests F_0,F_1. Their directed bipartite matchings M_0,M_1 both have size n-3.

A +1 connected component C of M_0 triangle M_1 is an alternating path with one more M_1-edge than M_0-edge. Hence both ends of C are incident to M_1 but not M_0. One endpoint is an M_0-unmatched out-copy and the other an M_0-unmatched in-copy. Distinct alternating components have disjoint endpoints.

A spanning three-path forest F_0 has exactly three unmatched out-copies, its three physical terminals, and exactly three unmatched in-copies, its three physical sources. Therefore the numbers g_+,g_- of +1 and -1 components satisfy

  g_+=g_-=:g<=3.                                        (TG.1)

The equality follows from total alternating weight zero. Thus every comparison of maximum three-forests has at most six charged alternating components in total. Zero-weight components may still be arbitrarily numerous.

### 2. Physical endpoint ancestry of gains
Each +1 alternating component C has a unique endpoint pair

  (t_C)_out, (s_C)_in,

where t_C is a terminal of F_0 and s_C a source of F_0. The gain components therefore form a partial matching from the three F_0 terminals to the three F_0 sources.

For the canonical merge setup of SV20847, fix a terminal t and a source s of different F_0 rails, put e=t_out s_in, and choose F_1 closest to F_0 among ALL maximum three-forests containing the directed edge e. The edge e is an isolated +1 component E and occupies exactly the endpoint slots (t,s). Any other gain must use one of the remaining terminal slots and one of the remaining source slots. No assertion that e remains a separate dimer rail is made.

### 3. Exact charged-preorder projection
Let C be the full set of alternating components and let

  C^*=P union N

be the charged components, where P has weight +1 and N weight -1. Restrict the full collision reachability relation to C^*: for charged A,B write A<=_*B exactly when A<=B in the full preorder, allowing the witnessing implication route to pass through zero-weight components.

Then weighted upper-set existence depends ONLY on this at-most-six-node charged preorder.

First let U be any upper set of the full preorder. If A is charged and A in U, and A<=_*B with B charged, then B in U. Hence U cap C^* is an upper set of <=_*. Since all omitted components have weight zero,

  delta(U)=delta(U cap C^*).                             (TG.2)

Conversely let S be an upper set of <=_* and form its full upward closure

  U=Up_C(S).

If a charged B lies in U, some A in S satisfies A<=B, hence A<=_*B and charged-upperness forces B in S. Thus

  U cap C^*=S,                                           (TG.3)

and therefore

  delta(U)=delta(S).                                     (TG.4)

Consequently a positive-weight full upper set exists if and only if the charged preorder has a positive-weight upper set. Zero corridors are mathematically relevant as physical provenance of the relations A<=_*B, but their lengths and number are irrelevant to the existence of a positive-weight upper set.

### 4. Corrected rooted pressure in the acyclic branch
Assume Gamma(H) is acyclic and retain the closest edge-containing representative F_1 from Section 2. Then every full upper-set recombination has zero directed-cycle debt.

Let

  S_E=C^* cap Up_C(E)

be the charged components reachable upward from the isolated gain seed E. This is exactly the upward closure of E in the charged preorder.

If S_E is a proper subset of C^*, then Up_C(E) is a proper full upper set: if it were the whole component system it would contain every charged component. Corrected CP.8 from SV20847 therefore gives

  delta(S_E)=delta(Up_C(E))<0.                           (TG.5)

Equivalently,

  |N cap S_E|>|P cap S_E|.                              (TG.6)

Since E is one of the reachable gains, S_E contains at least two losses.

If S_E=C^*, then delta(S_E)=0. In this case Up_C(E) cannot be proper, because corrected CP.8 would give 0<0. Hence

  S_E=C^*  =>  Up_C(E)=C.                               (TG.7)

Thus a closest blocked merge in the acyclic branch has an exact charged dichotomy:

  either the seed reaches EVERY charged component and in fact every alternating component,
  or its charged closure has strictly more reachable losses than gains.               (TG.8)

This replaces the earlier zero-corridor-shortcut target. The charged obstruction has at most six nodes, but an arbitrary such weighted preorder can certainly block every positive upper set. The unresolved issue is the PHYSICAL origin of its reachability relations and their compatibility across the six different terminal-to-source seeds rooted in the same base forest.

### 5. Simultaneous-merge target
For a fixed maximum three-cover F_0=A|B|C, there are six ordered cross-rail merge edges t_X->s_Y with X!=Y. For each, choose a corrected closest maximum forest containing that directed edge and retain its charged preorder together with the actual physical collision vertices and implication routes realizing each charged reachability relation.

The next theorem target is SIMULTANEOUS PHYSICAL MERGE ESCAPE: these six rooted charged-preorder obstructions cannot all be nonaugmenting. In the acyclic branch it suffices to force one positive-weight charged upper set. In the cyclic branch the charged projection alone is insufficient because zero-weight components can alter physical cycle debt c(U); full cycle supports, break edges, and attachment data must be retained there.

No simultaneous escape theorem is claimed here.

## References

```json
[
    {"relation":"dependency","revision_id":"R887"}
]
```
