# Any singleton row produced by a repeated five-root anchor has an internal original root and re-enters component-drop geometry

**Workspace:** D17
**State:** established
**Key:** `virtual-five-root-singleton-row-internal-root-recycle`

**Summary:** Retain the singleton-row currentization branch of SV74357: an exact two-cover C_xi of H-xi produced from two roots of the original SV58280 five-root Hamilton P5 K. Since xi lies outside K, all five K vertices survive in C_xi. Two path rails have at most four distinct physical endpoints, so some root f in K is internal on its C_xi rail. Puncturing f produces a literal three-cover of H-{xi,f}. Pair-deletion rigidity supplies an exact two-cover of the same residue, and R159 gives an R176-selected component-crossing balanced-pair birth with the singleton-row decomposition retained as source ancestry. Hence the H-xi row is not a new quiet bottom-family representative species. Any reconstruction-closed family that accepts it must immediately accept a source-visible component-drop portal rooted at one of the same five P5 vertices. This is structural recycling, not phase-zero descent.


### 1. Input: the five-root singleton row
Retain the SINGLETON-ROW CURRENTIZATION outcome of `virtual-shared-anchor-two-root-common-residue-diamond` SV74357. Thus the five-root construction of SV58280 supplies one fixed Hamilton P5

  K on five physical vertices,                              (SR.1)

one common center xi outside K, and two distinct roots d,e in K whose repeated literal xi-ancestor has been merged into a literal exact two-cover

  C_xi=P|Q  of H-xi.                                       (SR.2)

The common selected incidence and tight xi-birth trimer retained by SV74357 remain historical side data. Only the exact row (SR.2) is needed for the present argument.

### 2. One of the five original roots is internal
All five vertices of K belong to H-xi because xi lies outside K in the SV58280/SV58856 source construction.

A two-path cover has at most four distinct physical rail endpoints: two on P and two on Q, with singleton rails contributing fewer rather than more. Therefore among the five K vertices at least one

  f in V(K)                                                (SR.3)

is internal on its C_xi rail.

Write that rail locally as

  (...,r,f,s,...).                                         (SR.4)

Deleting f splits it into two nonempty tight intervals. The other C_xi rail survives. Hence

  R_f=C_xi-f                                               (SR.5)

is a literal three-cover of the common pair-deletion residue

  W_f=H-{xi,f}.                                            (SR.6)

### 3. Pair-deletion rigidity gives the smaller cover
Accepted R429 supplies a literal exact two-cover

  T_f=T_1|T_2  of W_f,                                    (SR.7)

with both rails nontrivial.

Now R_f has three nonempty components while T_f has two. Accepted R159 applies. Its fully reconstructed proof selects an actual T_f-state crossing two distinct R_f-components and invokes accepted R176 on that exact cross-state. Thus the output is not an anonymous balanced pair: retain

- the exact singleton row C_xi,
- the internal root f and its predecessor/successor cut,
- the three-component puncture R_f,
- the exact pair-deletion cover T_f,
- one selected T_f component-crossing,
- the resulting R176 pair-birth certificate.              (SR.8)

### 4. Consequence for the G26 bottom-family alphabet
Therefore an exact H-xi row produced from the repeated five-root ancestor packet cannot be a terminal quiet current representative. Before any unrelated payment or return it exposes a source-visible component-drop portal on one of the SAME five root coordinates that generated the virtual packet.

Equivalently,

  FIVE-ROOT REPEATED ANCESTOR
  -> exact H-xi row
  -> rooted R159/R176 component drop.                      (SR.9)

This removes the singleton-row currentization from the independent G26 bottom-family alphabet. It does NOT declare the R159/R176 payment strict progress at phase zero: its paid descendant may still return flat. The gain is exact ancestry recycling onto the original finite root set.

R24 and R5 are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    }
]
```