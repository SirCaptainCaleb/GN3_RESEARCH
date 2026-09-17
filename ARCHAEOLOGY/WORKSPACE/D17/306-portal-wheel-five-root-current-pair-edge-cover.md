# Every P5 wheel carries a five-root current pair-deletion edge cover

**Workspace:** D17
**State:** established
**Key:** `portal-wheel-five-root-current-pair-edge-cover`

**Summary:** Combine the rootwise R508 crossing of SV60333 with the dual-capture forced-current fork SV63332. For each of the five P5 roots d choose one exact H-d row and one selected K-d|E crossing k_d e_d. At least one crossing endpoint c_d in {k_d,e_d} is internal in that same row, so H-{d,c_d} carries a literal 3-to-2 component-drop interface; simultaneously the same crossing lawfully pays to floor {d,c_d}. Thus the five roots index five current deleted-pair portals D_d={d,c_d}. Their underlying pairs cover all five K roots. A pair involving an exterior endpoint can occur for only one root; a K-K pair can be indexed by at most its two endpoints. Hence at least ceil(5/2)=3 distinct current pair-deletion fibers coexist as graph-intrinsic source certificates. Equivalently, every portal wheel has a current pair-edge cover of K of size at least three. If any chosen current pair leaves K, the legal reconstruction family already escapes to an exterior coordinate; if all remain inside K, choosing one current K-neighbor per root gives a fixed-point-free current map K->K and hence a directed current cycle. This reduces the full G23 wheel to simultaneous consumption of a bounded current-pair edge cover; the static coherent shell is not terminal. No Phi descent is claimed.

### 1. Five root rows and their forced current choices
Retain the Hamilton P5 K of the G23 family and put E=V(H)-V(K). Assume no branch closes H. For every root d in K choose one actual exact two-cover

  T_d of H-d.

Accepted R508 forces T_d to select a physical crossing

  k_d e_d,   k_d in K-{d}, e_d in E.                      (CE.1)

Apply the dual-capture forced-current theorem SV63332 to this very crossing. The two marker endpoints k_d,e_d are both lawful capture anchors, and they cannot both be rail endpoints of T_d. Hence choose one endpoint

  c_d in {k_d,e_d}

which is INTERNAL on its T_d rail. Puncturing c_d from T_d is a literal three-cover of H-{d,c_d}; accepted pair-deletion exactness supplies an exact two-cover of the same residue, so the SV63332/R159 mechanism gives a current 3-to-2 component-drop interface there. At the same time the dual-capture payment branch gives

  TWO-COVER or ancestry-bearing floor {d,c_d}.              (CE.2)

Thus each root d supplies a deleted pair

  D_d={d,c_d}                                               (CE.3)

which simultaneously carries a literal current pair-deletion portal and a lawful root-preserving paid return.

### 2. The five current pairs cover all five P5 roots
By construction every root d belongs to D_d. Therefore the family of physical pairs

  E_cur={D_d : d in K}                                     (CE.4)

covers the five-element set K.

Distinct roots can produce the same unordered pair only in the K-K case. Indeed if D_d={d,e} with e in E, no other root d' in K can produce the same unordered pair because its K member would have to be d. If D_d={d,k} subset K, the same unordered pair may also be indexed by root k, but by no third root. Consequently every distinct current pair accounts for at most two of the five root indices. Hence

  |E_cur| >= ceil(5/2)=3.                                  (CE.5)

So one Hamilton P5 wheel carries at least THREE distinct current pair-deletion fibers, source-visible before any payment reset, and these fibers collectively touch every P5 root.

### 3. Interior-versus-exterior currentization dichotomy
There are two family-level possibilities.

EXTERIOR CURRENT ESCAPE. Some D_d={d,e} with e in E. Then the same root row already supplies both an exterior-coordinate floor {d,e} and a literal current component-drop portal on H-{d,e}. Thus the legal reconstruction family is not closed on the five P5 coordinates.

ALL-K CURRENTIZATION. Every chosen D_d is contained in K. Then choose the directed arc d->c_d. This is a fixed-point-free map K->K. Hence its functional digraph contains a directed cycle of length 2,3,4,or5, and EVERY arc of that chosen cycle is already INTERNAL/current on its own pair deletion. This is stronger than the original SV60333 rim extraction, where END arcs were allowed.

Thus every wheel satisfies

  exterior current escape,
  OR a completely current K-rim cycle,                       (CE.6)

and in either case at least three distinct current pair-deletion fibers cover all five roots.

### 4. Relation to the coherent shell
SV61535/SV63042 show that if the selected spoke/rim pair partitions avoid their own Johnson-triangle crossing outputs, they glue to a global support partition and collapse to the fixed-complement 5+1/6+0 shell. CE.5 shows that this shell is not a geometry-free terminal object once the FULL legal capture choice is retained: independent of support coherence, the five root rows already carry a bounded current-pair edge cover. In particular every END-type K-side rim edge has the exterior current portal of SV63332, while every INTERNAL K-side edge is itself current.

Therefore the remaining G23 problem is no longer wheel extraction or support-shell classification. It is the simultaneous consumer problem:

  consume a bounded current pair-edge cover touching all five K roots,
  with each edge retaining its root row, physical crossing, dual capture choice, and paid-return ancestry.

This is exactly the scale at which a Phi/epsilon descent theorem must operate.

### 5. Scope fence
Three current pair-deletion portals do not automatically lower the global partition-disagreement objective Phi. Their exact two-cover recompletions can be different and their paid descendants are alternatives. CE.5 is therefore a family-level currentization/compression theorem, not portal-wheel closure. No anonymous payment is counted as progress, and no R24/R5 input is used.

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
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    }
]
```