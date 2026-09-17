# Completed endpoint dimers break singleton replay at every fixed-E reentry middle

**Workspace:** D17
**State:** established
**Key:** `fully-anchored-pre-singleton-replay-breaker`

**Summary:** At a fully anchored fixed endpoint pair E={a,c}, the completed signed singleton coordinates alone do NOT obstruct coherent replay: for any later proper reentry turn J=(a,b,c), accepted R436 may simply regard J as strict growth of both singleton supports. The useful retained data are the original nontrivial R434 endpoint-anchored dimers from the two completed episodes. Write L=(p,a), tail-signed, and R=(c,q), head-signed. For every later same-E proper turn J=(a,b,c), independently at each endpoint either the old secondary vertex equals the new middle, giving an adjacent reversal against J, or one seam test gives a literal P4 through J and the old secondary vertex, while failure gives by R3 a labelled reverse trimer at the old endpoint dimer. Thus every same-E reentry carries a bilateral ancestor-contact packet: P4 / reverse trimer / adjacent reversal at BOTH completed endpoints. If p,q,b are pairwise distinct and both extension seams pass, they concatenate to the literal P5 (p,a,b,c,q). This is middle-independent and therefore survives arbitrary R1022 return to the old endpoint pair. It applies after paid SV50987, R920, or SV50536 exits once the existing fixed-E return map has restored E. It does not yet prove closure or strict Psi_E descent at the bottom rank; the remaining obstruction is bilateral pre-singleton ancestor curvature absorption.

### 1. Singleton double replay is genuinely possible
Let H be a hypothetical smallest Strong Level-(1) counterexample and fix a fully anchored physical endpoint pair

  E={a,c},  A_E=E.

Retain the two completed historical signed singleton coordinates (a) and (c). Let

  J_b=(a,b,c)

be any later proper tight turn on the same endpoint pair, in particular a turn supplied by an R1022 return with a new middle b.

There is an important fence. The two historical SINGLETONS by themselves do not make coherent replay difficult. In the proof of accepted R436, when the old signed support has order one, any later nontrivial tight path containing its anchor is already strict growth of that singleton. Therefore applying R436 to (a) versus J_b may output J_b itself as strict growth, and the dual application at (c) may output the same J_b. Both endpoint contacts can replay one common source trimer.

So a theorem of the form `two completed singleton anchors make double source-trimer replay impossible' is false at the level of the singleton supports alone. Any fully-anchored collapse proof must spend stronger retained ancestry.

### 2. Completed R434 episodes retain stronger endpoint dimers
Use the persistence clause of accepted R434, not merely its final singleton coordinates. The completed a-episode retains an original nontrivial endpoint-anchored signed dimer; after orienting with the R434 predecessor convention write it

  L=(p,a),

with L tail-signed and p notin E. The completed c-episode similarly retains

  R=(c,q),

with R head-signed and q notin E.

The old witnesses and the old middle vertices are retained historically but are not needed for the local calculation below. What matters is that L and R are graph-intrinsic proper tight dimers, physically different from the singleton supports to which their protected descendants were eventually paid.

Now let J_b=(a,b,c) be ANY later proper turn on E. No assumption is made that b equals either middle used when L or R was created.

### 3. Left completed dimer versus an arbitrary new middle
First compare L=(p,a) with the new first state a b of J_b.

If p=b, then L is the directed dimer (b,a), while J_b selects the opposite directed state (a,b). Hence the parent frame already contains a labelled adjacent selected-state reversal on the physical dimer {a,b}.

Assume p!=b. Test the single ordered seam

  (p,a,b).

If it is tight, it concatenates with the retained turn (a,b,c) to the literal vertex-simple tight P4

  (p,a,b,c).

If it is bad, boundary antisymmetry R3 gives its exact reversal

  (b,a,p) tight.

This is a labelled reverse trimer through the old a-dimer L. In the language of R436 it is an explicit reverse-contact/reversal cell rather than a stationary replay.

Therefore the completed a-episode has, against every later same-E middle b, one of exactly three explicit source-visible forms:

  LEFT-P4:       (p,a,b,c),
  LEFT-REVERSE:  (b,a,p),
  LEFT-ADJ:      p=b and (b,a) opposes the J-state (a,b).

### 4. Right completed dimer versus an arbitrary new middle
The terminal calculation is exact and is written explicitly to avoid informal reversal. Compare R=(c,q) with the new final state b c of J_b.

If q=b, then R is the directed dimer (c,b), opposite the J_b state (b,c), so there is a labelled adjacent reversal on {b,c}.

Assume q!=b. Test

  (b,c,q).

If it is tight, it concatenates with J_b to the literal P4

  (a,b,c,q).

If it is bad, R3 gives

  (q,c,b) tight,

a labelled reverse trimer through the old c-dimer R.

Thus the completed c-episode independently gives

  RIGHT-P4:       (a,b,c,q),
  RIGHT-REVERSE:  (q,c,b),
  RIGHT-ADJ:      q=b and (c,b) opposes the J-state (b,c).

### 5. Bilateral replay-breaking normal form
Combining Sections 3 and 4 gives a middle-independent bilateral packet. For EVERY later proper turn J_b on the same fully anchored endpoint pair E, each completed endpoint contributes a literal P4, a labelled reverse trimer, or an adjacent reversal.

In particular, the only replay available from the bare singleton contacts disappears once the retained pre-singleton R434 ancestors are consulted. One does not merely recover the new source trimer J_b twice: one gets explicit geometry involving the old secondary vertex p at a and the old secondary vertex q at c.

There is one useful simultaneous strengthening. If

  p,q,b

are pairwise distinct and both extension seams are tight, then the consecutive tight turns

  (p,a,b), (a,b,c), (b,c,q)

concatenate to the literal vertex-simple tight P5

  (p,a,b,c,q).

If p=q, no P5 claim is made because the displayed five-word repeats a vertex; the two certified P4s are retained separately.

### 6. Fixed-endpoint return consequence
The theorem is insensitive to the old middle vertices. Hence it composes directly with the current fixed-endpoint return machinery. After any certificate-bearing productive exit has been paid to a floor, steered back to the OLD endpoint pair E, and currentized by accepted R1022 through some new proper trimer J_b=(a,b,c), the fully anchored lineage immediately acquires the bilateral packet above.

Consequently the same statement applies to the G21 mandatory returned objects once their already-established paid return is invoked:

- a transverse-cap exit from SV50987/R514;
- an R920 cross-pole pair packet;
- any chosen R514 payment descendant of the SV50536 bilateral cap-wall rectangle;
- a generic R1022 reentry at the old endpoint pair.

No frozen root is used.

### 7. Remaining obstruction
This is not yet FULLY-ANCHORED COLLAPSE. At A_E=E and an E-aligned mass-two checkpoint the candidate endpoint rank is already at the bottom

  Psi_E=(0,0,0).

A P4, reverse trimer, or adjacent reversal born from this phase-0 checkpoint cannot simply be sent to phase 1 and counted as progress; it must close H or return to the same E-lineage productively. The theorem therefore identifies the correct surviving parent problem:

  BILATERAL PRE-SINGLETON ANCESTOR CURVATURE ABSORPTION.

The important correction is that the hard cell is not `double singleton replay'. That replay is automatic. The hard cell is whether the two retained nontrivial completion ancestors, now forced to interact with every new middle through the bilateral P4/reverse/reversal packet, can be consumed jointly into closure or a lawful strict return.

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
        "revision_id": "R436"
    },
    {
        "relation": "dependency",
        "revision_id": "R1022"
    }
]
```