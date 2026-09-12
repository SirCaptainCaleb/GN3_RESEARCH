# A closed P5 capture family either currentizes outside K or is strongly current on all five roots

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-exterior-current-or-strong-current-k5`

**Summary:** Refine SV63649 using the all-choice graph and proper-sink extinction. Let C_K contain every nonclosing K-side capture arc d->k arising from every selected K-d|E crossing. If any such crossing has its exterior endpoint e internal in the source H-d row, SV63332 gives an exterior-coordinate current portal H-{d,e} and floor {d,e}. Otherwise every exterior crossing endpoint is END. Since the two marker endpoints cannot both be END, every K-side endpoint k of every crossing is INTERNAL, so every arc d->k of C_K is itself a current 3-to-2 component-drop portal on H-{d,k}. SV61245 rules out every proper sink SCC of C_K in a reconstruction-closed nonclosing family. A finite digraph has a sink SCC, hence the unique sink is all five vertices K and C_K is strongly connected. Therefore the only no-exterior-current residue is a strongly connected directed graph on all five P5 roots in which EVERY capture arc is currentized on its K-K deleted pair. Its underlying current-pair graph is connected and has at least four distinct rim pairs. This is a stronger normal form for the remaining G23 consumer problem.

### 1. All-choice capture graph with both marker endpoints retained
Retain the Hamilton P5 K and exterior E=V(H)-V(K). Let C_K be the ALL-CHOICE nonclosing K-side capture digraph of SV60654: an arc

  d -> k

exists whenever some exact H-d row T_d selects a K-d|E crossing

  k e,   k in K-{d}, e in E,                              (SC.1)

and the lawful K-side capture continuation is nonclosing. Work in a reconstruction-closed nonclosing family.

SV63332 says the same crossing also admits exterior capture at e, and at least one of k,e is INTERNAL in the source row T_d. We now branch on whether exterior INTERNALity occurs anywhere in the full all-choice family.

### 2. Exterior-current branch
Suppose some crossing SC.1 has e internal on its T_d rail. Then puncturing e leaves a literal three-cover of H-{d,e}; an exact two-cover of the same residue supplies the R159 current component-drop interface. Simultaneously the dual capture/payment branch gives

  TWO-COVER or floor {d,e}.                                (SC.2)

Thus the legal reconstruction family has a current deleted pair involving a coordinate e outside the original P5 K. This is the EXTERIOR-CURRENT branch. No further K-only wheel analysis is legitimate without retaining this escape.

### 3. No exterior current forces every K-side arc current
Assume instead that NO exterior endpoint e of ANY selected root crossing in the all-choice family is internal in its source row. Then every such e is a rail endpoint. By SV63332 the two crossing endpoints k,e cannot both be endpoints. Therefore for every crossing SC.1,

  k is INTERNAL in T_d.                                    (SC.3)

Puncturing k from T_d gives a literal three-cover of H-{d,k}; exact pair-deletion recompletion gives the current component-drop interface. Hence

  EVERY arc d->k of C_K is currentized on H-{d,k}.          (SC.4)

This is simultaneous as a graph-intrinsic family of source certificates; later paid descendants remain alternative.

### 4. Proper-sink extinction upgrades currentness to strong connectivity
Every finite digraph has a sink strongly connected component S. SV61245 proves that in the all-choice P5 capture graph no proper sink S subsetneq K can survive reconstruction closure: deleting the other S-roots from one singleton row and recompleting H-S forces a paid return through K-S.

Therefore the sink SCC of C_K must be all of K. A strongly connected component equal to the whole vertex set means

  C_K is strongly connected on the five roots of K.         (SC.5)

Combining SC.4 and SC.5, the no-exterior-current branch has an exact finite normal form:

  a strongly connected directed graph on five physical roots,
  and every directed capture arc is a literal current
  3-to-2 component-drop portal on its own K-K pair deletion.  (SC.6)

The underlying undirected current-pair graph is connected, hence contains at least four distinct physical K-K pairs. In particular the lower bound of three distinct current fibers from SV63649 improves to four in this branch.

### 5. G23 dichotomy
Every reconstruction-closed nonclosing P5 capture family therefore satisfies exactly the strategic alternative

  EXTERIOR CURRENT: some H-{d,e}, e outside K, is current and pays to {d,e};

  OR

  STRONGLY CURRENT K5: C_K is strongly connected on all five roots and every arc is current on H-{d,k}.  (SC.7)

The old mixed END/INTERNAL rim taxonomy has disappeared. If END survives on the K side, the same crossing lies in the exterior-current branch. If no exterior current branch exists, all K-side capture choices are INTERNAL/current.

### 6. Scope fence
Strong connectivity does not by itself lower Phi or epsilon_*. The four-or-more current rim fibers can have different exact recompletions, and their paid returns are not simultaneous current floors. SC.7 is therefore the final bounded currentization normal form, not a proof of portal-wheel extinction. Its value is that any next consumer may assume either an actual coordinate escape outside K or a completely current strongly connected five-root system; no static coherent wheel residue remains to classify.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    }
]
```