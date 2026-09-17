# Every mutual-internal two-root capture sink emits a third-root paid return

**Workspace:** D17
**State:** established
**Key:** `closed-return-two-root-sink-third-root-escape`

**Summary:** Consume the only two-root sink left by SV60654. If S={a,b} is a sink SCC of the all-choice P5 capture graph, then b is internal in every exact H-a cover and a internal in every exact H-b cover. Puncturing b from any H-a cover gives a literal three-cover R of H-{a,b}. Because every original K-a|E crossing was forced through b, every component of R is pure for (K-{a,b})|E. Pair-deletion rigidity gives an exact two-cover F of the same residue, while R508 applied to the Hamilton P5 K forces F to select a crossing ce with c in K-{a,b}, e in E. This state crosses two R-components. Running the R176 seam proof at the K-side endpoint c with spare a gives singleton a opposite an order-at-most-two signed support anchored at c; the order-two R428 refund used in SV58568 either closes H or leaves exactly c, hence pays to floor {a,c}. Thus a reconstruction-closed family cannot remain supported on the two roots {a,b}: the mutual-internal residue necessarily returns through a third P5 root. Consequently the smallest closed wheel kernel has at least three rim roots. This is a genuine G23 rim-shortening/extinction result for length two, not yet extinction of 3-,4-,5-root kernels.

### 1. Input: the only possible two-root all-choice sink
Retain the all-choice capture graph C_K of SV60654 on the Hamilton P5 K, with E=V(H)-V(K), and assume no branch closes H. Suppose a sink strongly connected component has order two,

  S={a,b}.

SV60654 then gives the universal mutual-internal conclusion

  b is internal in every exact H-a two-cover,
  a is internal in every exact H-b two-cover.                    (TE.1)

Moreover every selected K-a|E crossing in every H-a row has K-endpoint b, and dually every selected K-b|E crossing has K-endpoint a.

We now show that this two-root set is not closed under the full legal reconstruction family.

### 2. Puncturing the opposite root leaves a cut-pure three-cover
Fix any exact two-cover

  T=P|Q

of H-a. By TE.1, b is internal on its T-rail. Delete b. That rail splits into two nonempty intervals and the other rail stays nonempty, so

  R:=T-b

is a literal three-cover of

  W=H-{a,b}.                                                (TE.2)

Put

  C=V(K)-{a,b}.

Thus |C|=3 and W=C disjoint_union E. Every component of R is C/E-pure. Indeed, if a surviving component contained vertices of both C and E, one of its selected adjacencies would be a C|E crossing. That adjacency already occurred in T and avoids b, hence would be a selected K-a|E crossing of T whose K-endpoint lies in C rather than at b, contradicting the sink property from SV60654. Therefore

  every R-component is contained wholly in C or wholly in E.  (TE.3)

### 3. Exact rim recompletion forces a third-root cross-state
Accepted pair-deletion rigidity R429 gives an exact two-cover

  F=F_1|F_2

of the same residue W=H-{a,b}. Apply accepted R508 with deleted set D={a,b}, absorbable block C=K-{a,b}, and carrier path Q_K=K. Since K is Hamilton on D union C, F must select a physical crossing

  ce,    c in C, e in E                                    (TE.4)

between C and E. By TE.3, c and e lie in distinct components of the three-cover R. Hence TE.4 is simultaneously a current R176 cross-state for the pair R,F.

Crucially c is one of the THREE remaining P5 roots:

  c in K-{a,b}.                                             (TE.5)

### 4. The third-root cross-state pays to {a,c}
Choose the spare vertex a outside W. We now run the seam calculation of accepted R176/P540 at the K-side endpoint c of the selected dimer {c,e}. The proof is endpoint-symmetric after dualizing head/tail polarity: if the R-component containing c is singleton, the automatic selected dimer orientation gives singleton c one sign with the other crossing endpoint as witness, while the automatic dimer through spare a gives singleton a the opposite sign. If the R-component containing c is nontrivial, choose its literal neighbor p. Boundary antisymmetry R3 on {p,c,e} gives exactly one of the two orientations that makes (c,p) head-signed by e or (p,c) tail-signed by e; the spare singleton (a) receives the opposite polarity from the automatic two-vertex path through e.

Thus TE.4 gives a graph-intrinsic balanced opposite-sign pair of the form

  singleton (a) + a signed support D_c of order 1 or 2

whose signed physical anchor is c.                              (TE.6)

If D_c is singleton we already have the floor {a,c}. If D_c is order two, apply accepted R428 preserving singleton a. The exact order-two refund calculation is the same one used in SV58568: outside closure the unsigned endpoint is removed and the signed endpoint c survives. Hence the continuation yields

  TWO-COVER, or the ancestry-bearing floor {a,c}.            (TE.7)

The retained ancestry includes the original H-a row T, its internal occurrence of b, the punctured three-cover R, the exact rim recompletion F, and the selected third-root crossing ce.

### 5. Two-root closed-kernel extinction
The new floor in TE.7 uses c notin {a,b}. Therefore a family closed under the legal component-drop/cross-state/payment reconstruction cannot remain supported on the two-root set {a,b}. Combining with SV60654 gives the exact two-root dichotomy:

  END occurrence => TWO-COVER or an immediate third-root capture choice;
  all INTERNAL => TWO-COVER or a third-root component-drop paid return.   (TE.8)

Hence NO nonclosing reconstruction-closed G23 wheel kernel can have only two P5 rim roots. Any minimal closed root kernel has order at least three.

This is stronger than saying an arbitrary chosen directed 2-cycle is impossible. A chosen 2-cycle may exist inside the five-root graph, but it cannot be a sink after all legal reconstructions are included.

### 6. Scope fence
No claim is made that the resulting three-root kernel closes. The third-root floor TE.7 is a later ancestry-bearing checkpoint, not a simultaneous current representative with T or F. The theorem also does not identify a decrease of global Phi by itself. The next G23 target is therefore the genuine three-root Johnson-triangle kernel, where every rim deletion pair and all three hub spokes must be compared on their common triple-deletion shadows.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R176"
    },
    {
        "relation": "dependency",
        "revision_id": "R428"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    }
]
```