# Across successful defect pivots only the fixed far-end reverse star can persist

**Workspace:** D17
**State:** established
**Key:** `g35-successful-pivot-far-star-persistence`

**Summary:** Let two consecutive G35 prefix states M_q,M_{q+1} be literal tight three-forests, related by one successful zipper pivot, and assume neither shortcut is the unique loop coincidence. The q-th closing shortcut g_q=a_q->b_m has only a near seam at a_q and a far-boundary obstruction at b_m. Any near-seam blocker uses g_q and disappears when the defect advances because g_q is no longer selected. By SV113367 an ordinary shortcut-cycle blocker also cannot persist across the successful pivot. Since a_{q+1}!=b_m, the pivot does not remove the selected outgoing edge of b_m, so its physical successor c is unchanged. If c!=a_q, the far boundary is the genuine three-vertex seam (a_q,b_m,c), and a bad seam reverses by R3 to (c,b_m,a_q). If c=a_q, there is no three-vertex seam: the selected edge b_m->a_q and shortcut a_q->b_m form an explicit reverse-dimer/backtrack branch. A successful pivot changes the moving terminal, so this same-rail coincidence cannot occur at both consecutive states. Hence R3 is used only on distinct-vertex triples, the reverse-dimer branch is one-step debt, and the only blocker that can genuinely recur at the next shortcut is the fixed far reverse star. Along any run of successful physical pivots, genuinely persistent seam debt is therefore one growing reverse star at the fixed far boundary; near blockers, reverse-dimer debt, and cycle debt are one-step phenomena.

### 1. Consecutive physical defect states
Retain the G35 zipper corridor and suppose two consecutive prefix matchings

  M_q, M_{q+1}

are both realized as literal spanning tight three-path forests. They are related by the successful pivot

  f_{q+1}=a_{q+1}->b_{q+1}
  replaced by
  e_{q+1}=a_q->b_{q+1}.                                (SP.1)

The moving unmatched OUT copy is a_q,out in M_q and a_{q+1},out in M_{q+1}; a successful pivot advances the physical moving terminal, so

  a_q != a_{q+1}.                                       (SP.1a)

The fixed far unmatched IN copy is b_m,in in both states. Assume

  a_q != b_m,   a_{q+1} != b_m,                          (SP.2)

so neither closure is the unique singleton-loop coincidence.

For the q-th state put

  g_q=a_q->b_m.                                           (SP.3)

Because a_q is a rail terminal and b_m a rail source, adding g_q creates at most a near seam plus one far-boundary obstruction. The NEAR seam is

  alpha_q=(p_q,a_q,b_m)                                  (SP.4)

when a_q has predecessor p_q. If b_m has selected successor c, then there are two far-boundary cases.

If c!=a_q, the FAR seam is the genuine distinct-vertex turn

  beta_q=(a_q,b_m,c).                                    (SP.5)

Here b_m!=c because b_m->c is a selected path edge, and a_q!=b_m by (SP.2), so all three vertices in beta_q are distinct.

If c=a_q, there is no three-vertex far seam. Instead the selected suffix is the order-two dimer

  b_m->a_q,

and the closing shortcut g_q=a_q->b_m is its exact reverse. Thus the closure contains the explicit two-edge backtrack

  b_m->a_q->b_m.                                         (SP.5b)

No invocation of R3 is made in this branch. All other turns are inherited from M_q.

### 2. Near-seam debt is one-step debt
If alpha_q is bad, R3 gives its exact reverse

  (b_m,a_q,p_q) tight.                                   (SP.6)

But the selected edge g_q is not present in the next closure M_{q+1}+g_{q+1}; its tail changes from a_q to a_{q+1}. Therefore the exact selected turn alpha_q is absent after the defect advances. A near-seam blocker can be newly replaced by another near-seam blocker at q+1, but the physical blocker at q itself does not persist.

This is literal support transport, not a novelty claim.

### 3. Cycle and reverse-dimer debt are one-step debt after a successful pivot
If both genuine shortcut seams at q are tight but g_q closes an ordinary directed cycle, SV113367 applies. Since the pivot (SP.1) is physically successful, the cut edge f_{q+1} must lie on a different M_q rail from the b_m-to-a_q cycle rail. Consequently b_m and the new terminal a_{q+1} lie on different M_{q+1} rails. Thus the next closure g_{q+1}=a_{q+1}->b_m cannot create the same directed cycle.

The order-two coincidence c=a_q is even more explicit. By (SP.1a), c=a_q implies c!=a_{q+1}. Hence the backtrack (SP.5b) cannot recur at the next closure. Conversely, if c=a_{q+1}, then c!=a_q, so the q-th far boundary was a genuine three-vertex seam. Therefore the same-rail order-two suffix can occur at at most one of two consecutive successful states.

Hence neither ordinary shortcut-cycle debt nor reverse-dimer debt persists across two consecutive physical corridor states.

### 4. The far boundary itself is fixed
Assume b_m has a selected successor c in M_q. The only selected edge leaving b_m could be changed by the pivot (SP.1) if its tail were b_m, i.e. if

  a_{q+1}=b_m.

This is excluded by (SP.2). The new edge e_{q+1} has tail a_q, not b_m. Therefore the selected outgoing edge b_m->c survives literally into M_{q+1}.

If c!=a_{q+1}, the far seam of the next closure is the genuine distinct-vertex turn

  beta_{q+1}=(a_{q+1},b_m,c).                            (SP.7)

If c=a_{q+1}, the next closure instead lies in the explicit reverse-dimer branch of Section 1. By Section 3 this cannot happen simultaneously with c=a_q.

If b_m is a singleton rail, no far seam or far reverse dimer exists at either state and this section is vacuous.

### 5. Persistent failure is exactly a reverse star
Suppose the same physical far-seam obstruction is bad at both consecutive states. Then neither state can be in the reverse-dimer branch, because that branch is an order-two backtrack rather than a three-vertex seam and cannot occur at both consecutive states. Thus

  c!=a_q,   c!=a_{q+1},

so beta_q and beta_{q+1} are genuine distinct-vertex triples. R3 is therefore legal and gives

  (c,b_m,a_q) tight,
  (c,b_m,a_{q+1}) tight.                                 (SP.8)

Thus repeated far-end shortcut failure does not produce unrelated trimers: it grows one graph-intrinsic reverse star at the fixed physical dimer (c,b_m), with the successive moving defect terminals as witnesses.

Iterating the same argument along any run

  M_q,M_{q+1},...,M_s

of successful physical pivots (omitting the at-most-one loop index), every blocker that genuinely persists from one closure to the next is represented by the single fixed-boundary family

  (c,b_m,a_i) tight                                      (SP.9)

at every pair of consecutive indices where the far boundary is a genuine seam. A same-rail order-two coincidence, if encountered, is an explicit transient backtrack and breaks rather than extends this seam-debt chain. Near blockers use the current g_i and disappear when i advances; ordinary cycle debt disappears after one successful pivot by Section 3.

### 6. G35 consequence and scope
The moving-defect corridor therefore has only one mechanism for carrying the SAME physical shortcut obstruction forward through successful pivots: a reverse star anchored at the fixed far endpoint. The same-rail order-two suffix is not a hidden exception to R3; it is a separate reverse-dimer/backtrack branch and is one-step debt.

This is a transport normal form, not a seam taxonomy. It does not claim that successive closures must all fail at the far seam, nor does it yet consume the reverse star when a source-spoke terminal enters it. Its purpose is to turn persistent mixed-turn debt into one common-parent object whose witness set is ordered by the zipper traversal. In particular the G36 consumer, which starts only from genuinely persistent fixed-wall debt, is unchanged: the transient reverse-dimer branch cannot supply a persistent wall, while every persistent genuine far seam supplies the same reverse-star certificate as before.

No R24, R5, payment, replay, MILP, or SAT is used.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
