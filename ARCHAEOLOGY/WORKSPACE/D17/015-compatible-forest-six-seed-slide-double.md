# Each physical merge seed is a reversible one-edge slide or a double-root reverse-P4 portal

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-six-seed-slide-double`

**Summary:** For a physical merge seed e=t->s between two components of a maximum three-forest, the only immediate collision gates are the two native merge turns at t and s. If exactly one existing merge turn is bad, adding e and deleting the unique boundary edge responsible for that bad turn gives the unique closest edge-containing maximum forest at symmetric-difference distance two. Its charged collision preorder is exactly one gain E pointing to one loss L, with no zero corridor or cycle debt. This one-vertex transfer is exactly reversible from the new forest, so all such SLIDE moves form an undirected exchange graph on maximum three-forests. If both merge turns are bad, every edge-containing representative must change both adjacent old boundary edges, distance two is impossible, and R3 reverses the two failures into the literal reverse P4 (q,s,t,p). R4 currentizes this P4 with an exact two-covered complement. Thus each of the six ordered terminal-source seeds is either a reversible SLIDE or a genuinely global DOUBLE root carrying two physical implications plus a reverse-P4 restoration portal. Only DOUBLE seeds can support nontrivial long charged transport or cycle debt after quotienting the SLIDE graph.

### 1. Root-gate localization
Let H be a hypothetical smallest counterexample and let

  F=A|B|C

be any spanning compatible three-forest. Fix two distinct oriented rails

  A=(a_0,...,p,t),   B=(s,q,...),

using the intrinsic one-hole interpretation when either rail has order one. Put e=t->s. The matching of F leaves t_out and s_in unmatched, so adding e alone is the isolated +1 seed for this physical merge.

The only physical local states changed by the singleton seed flip are at t and s. When the displayed neighbors exist, its two merge turns are

  alpha=(p,t,s),     beta=(t,s,q).                       (SD.1)

If alpha is bad, any edge-containing recombinant which flips e while retaining the F-incoming edge p->t realizes the unsafe mixed state alpha. Hence the seed has the collision implication

  E <= C_t,                                            (SD.2)

where C_t is the symmetric-difference component carrying the changed incoming copy t_in. In particular every compatible edge-containing representative must change the old incoming edge at t. Dually, if beta is bad then

  E <= C_s,                                            (SD.3)

where C_s carries the changed outgoing copy s_out, and every compatible edge-containing representative must change the old outgoing edge at s.

There are no other immediate physical collision gates out of E. Thus the two holes of the native R879 merge proposal are exactly the two root gates of the global collision-preorder obstruction.

### 2. One bad hole gives the unique distance-two edge-containing representative
Because H has no spanning two-cover, the complete merge window cannot be entirely tight. Suppose it has exactly one bad existing hole.

If alpha is tight and beta is bad, delete the selected edge s->q and add e=t->s. The resulting paths are

  (A,s) | (B-s) | C,                                    (SD.4)

with the evident singleton interpretation when B is a dimer. Every new turn is tight: alpha is the only new turn on A,s, and B-s,C are inherited. Thus (SD.4) is another maximum three-forest containing e.

If beta is tight and alpha is bad, delete p->t and add e. The result is

  (A-t) | (t,B) | C.                                    (SD.5)

Again this is a maximum compatible three-forest containing e. If only one merge seam physically exists, the same construction deletes the boundary edge responsible for that sole bad seam.

These representatives differ from F by exactly one deleted and one added selected edge. No edge-containing maximum forest can be closer, since F itself does not contain e and both matchings have the same cardinality. Moreover the distance-two representative is UNIQUE: any size-preserving matching at distance two which contains e deletes only one F-edge; to destroy the unique bad root state that deleted edge must be precisely s->q in (SD.4), or p->t in (SD.5).

Its collision system has exactly two noncommon singleton components:

  E={e}, delta(E)=+1,
  L={deleted boundary edge}, delta(L)=-1,

and the unique bad merge turn gives E<=L. There are no zero corridors and no cycle debt. Hence a singly blocked physical merge is already the smallest possible charged obstruction.

### 3. The distance-two move is exactly reversible
The move (SD.4) is reversible inside the maximum-forest family. In the new forest the deleted edge s->q joins the terminal s of A,s to the source q of B-s. Its merge window has the old bad turn beta=(t,s,q) on one side, while the other side is the next inherited B-turn (or is absent in the short case). Restoring s->q and deleting t->s therefore recovers F by the dual one-hole slide.

Likewise (SD.5) is reversed by restoring p->t: the old bad alpha remains the sole obstructing side while the other side is inherited from A. Consequently the graph whose vertices are maximum compatible three-forests and whose edges are these distance-two one-vertex transfers is UNDIRECTED.

Call such a seed a SLIDE.

### 4. Two bad holes force two root gates and a literal reverse P4
Now suppose both alpha and beta exist and are bad. Then both old boundary edges p->t and s->q must change in every compatible representative containing e, by (SD.2)-(SD.3). In particular no edge-containing maximum forest can lie at distance two from F: one deleted selected edge can destroy at most one of the two bad endpoint states.

Boundary antisymmetry R3 gives simultaneously

  (s,t,p) tight,       (q,s,t) tight,

so the physical word

  K=(q,s,t,p)                                           (SD.6)

is a literal tight P4. This is the complete reverse of the three-edge boundary chain p-t-s-q: it reverses the B source edge, the attempted merge edge, and the A terminal edge. By accepted R4, because K is proper, H-K has exact path-cover number two. Thus every DOUBLE root carries both its two explicit collision gates and a fresh reverse-P4 restoration portal K|T with T an exact two-cover of H-K.

Call this a DOUBLE seed. The reverse P4 and the exact complement are part of its retained physical ancestry; they are not to be projected immediately to generic mate/payment currency.

### 5. Six-seed quotient
Every ordered terminal-to-source pair of the three rails is therefore exactly one of:

  SLIDE: one bad merge hole, unique reversible distance-two edge-containing maximum forest, charged preorder E<L;

  DOUBLE: both merge holes bad, no distance-two edge-containing representative, two physical root implications, and the reverse P4 restoration portal (SD.6).

There are six such ordered seeds. The SLIDE moves generate an undirected exchange graph on maximum three-forests. Passing to one connected component of this graph removes all purely one-edge neutral wandering from the hard global question. The only seeds which can carry nontrivial long charged transport or cycle debt are DOUBLE seeds; any proof of Simultaneous Physical Merge Escape may therefore organize itself around how DOUBLE portals attach to or connect different SLIDE components.

This is a representation theorem, not closure. In particular it does not assert that every SLIDE component contains a DOUBLE seed, nor that a DOUBLE reverse P4 is absorbable without using its exact restored complement.

## References

```json
[
    {"relation":"dependency","revision_id":"R3"},
    {"relation":"dependency","revision_id":"R4"}
]
```
