# One mixed bad-singleton row pays four good roots to one globally spent anchor

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-bad-row-common-center-anchor-star`

**Summary:** In a smallest-counterexample fixed-complement shell V(H)=Omega disjoint_union Q with Q Hamiltonian, let D subset Omega be good labels with Omega-d Hamiltonian and let y be bad. Fix one actual exact bad row C_y of H-y and one selected Omega|Q state a->b in that row, with Omega endpoint o. For every good d != o, delete d from C_y and y from the good row C_d=P_d|Q. The same state a->b survives in C_y-d and its endpoints lie in distinct components of C_d-y. R176 with spare d therefore gives singleton d opposite a singleton/dimer signed at the same physical anchor a. Accepted R428 followed, if needed, by one-coordinate R432 steering pays this to the ancestry-bearing floor {a,d}. Hence one mixed bad row yields a common-center floor star on D-{o}, so at least four roots when |D|>=5. Combining with the global completed-anchor ledger of SV58856: from each floor {a,d}, pair-deletion rigidity and an internal middle give an R434 channel anchored at a. If a is already globally completed, R436 makes the channel nonquiet; if fresh, the protected continuation either closes/exits nonquietly or completes a once, strictly lowering epsilon_*=|V|-|A_*|. Thus one bad singleton row is directly coupled to the global anchor budget, not merely to anonymous current portals. In a lex-minimal epsilon_* stratum all its good-root branches are forced nonquiet at the same physical center a. No consumer of that common-center nonquiet packet is claimed.

### 1. One bad singleton row and one retained mixed state
Let H be a hypothetical smallest Strong Level-(1) counterexample and retain

  V(H)=Omega disjoint_union V(Q),

where Q is one literal Hamilton path and Omega is non-Hamiltonian. Let D subset Omega be a set of GOOD labels such that Omega-d is Hamiltonian for every d in D. Fix a BAD label

  y in Omega-D,   Omega-y non-Hamiltonian.                  (BA.1)

For each d in D choose an actual Hamilton puncture path P_d on Omega-d and retain the exact good row

  C_d=P_d|Q  on H-d.                                       (BA.2)

Choose one literal exact bad row

  C_y=A|B  on H-y.                                         (BA.3)

Because Omega-y is non-Hamiltonian while Q is Hamiltonian, C_y cannot have support partition (Omega-y)|Q. Hence some selected state of C_y crosses the fixed support cut Omega|Q. This also follows from SV65492 for every ordered good comparison. Fix ONE such selected directed state

  a -> b,                                                   (BA.4)

with one endpoint in Omega-y and the other in Q. Let o denote the physical Omega-endpoint of {a,b}. The directed first endpoint a may lie on either side of the cut; no orientation case split will be needed.

### 2. The same mixed state pays every good root except possibly o
Fix

  d in D-{o}.                                               (BA.5)

Put W=V(H)-{y,d}. Delete d from the bad row C_y, splitting its rail if d was internal. Since d is different from both endpoints of (BA.4), the selected directed state a->b survives literally in the resulting path cover

  T_d := C_y-d   of H[W].                                  (BA.6)

Delete y from the good row C_d. The fixed complement Q survives as one entire path component, while P_d-y is one or two nonempty Omega-side intervals, possibly with an empty interval discarded. Thus

  R_d := C_d-y                                               (BA.7)

is a literal path cover of H[W] in which every component is contained entirely in Omega or entirely in Q.

The endpoints a,b of (BA.4) lie on opposite sides Omega|Q, so they lie in two distinct components of R_d. Therefore accepted R176 applies to the CURRENT selected state a->b of T_d, with the spare vertex chosen to be d outside W.

Inspecting the accepted R176/P540 construction, its support on the R_d side containing the directed first endpoint a is either:

- the singleton (a), if that R_d-component is singleton; or
- an oriented dimer containing a, signed at the physical anchor a, if the component is nontrivial.

In both cases singleton (d) receives the opposite polarity from the same cross-state witness. Thus the one retained state (BA.4) gives, for every d in D-{o}, a graph-intrinsic balanced pair

  singleton (d) + opposite support S_d of order at most two,
  with signed physical anchor a in S_d.                     (BA.8)

The exact old neighbor used inside S_d may vary with d when a lies in Omega. The physical signed anchor a and the source selected state (BA.4) do not vary.

### 3. Pay and steer to one common-center floor
If S_d is already singleton, (BA.8) is the ancestry-bearing floor {a,d}. Otherwise apply accepted R428 with singleton d fixed. Outside closure this reaches an ancestry-bearing both-singleton floor while preserving d. If the surviving opposite singleton is not a, apply accepted R432 with target pair {a,d}, using the one-coordinate replacement branch that preserves d. Consequently every root d in D-{o} has a finite certificate-retaining continuation

  TWO-COVER
  or ancestry-bearing floor {a,d}.                          (BA.9)

Retain as ancestry the one common bad row C_y, the one selected mixed state a->b, the good row C_d, the punctured comparison R_d,T_d, the R176 birth, and the payment/steering certificates.

Therefore one actual mixed singleton row yields a COMMON-CENTER paid star

  {a,d},   d in D-{o}.                                     (BA.10)

If |D|>=5, this star has at least four distinct good roots. In the rigid order-seven residue with five good P5 roots, a single mixed edge of either bad row therefore produces a four- or five-leaf ancestry-bearing star centered at one physical endpoint of that actual selected edge.

### 4. Couple the common center to the global completed-anchor ledger
Use the global completed-anchor notion A_* of SV58856: a physical vertex belongs to A_* once some earlier R434 selected-incidence episode has completed its protected return to an aligned both-singleton floor retaining that vertex as the signed singleton coordinate. The proof of SV58856 via accepted R436 makes this completion physical rather than endpoint-pair-relative.

Fix one nonclosing floor {a,d} from (BA.9). Accepted R429 supplies an exact pair-deletion frame

  H-{a,d}=U|V                                                (BA.11)

with both rails nontrivial. Accepted R533 gives |V(H)|>10. Hence U and V cannot both be dimers: their total order is |V(H)|-2>8. Choose an internal rail vertex m. By boundary antisymmetry one of the two complete-reversal outer-pair turns on {a,m,d} is tight; call it J. In either orientation a is one outer endpoint of J. Since m is internal, its selected predecessor and successor both exist, so accepted R434 supplies the selected-incidence channel anchored at a.

Now exactly the global-spend alternatives of SV58856 apply.

- If a is already in A_*, the new nontrivial a-anchored dimer meets the historical signed singleton (a). Accepted R436 makes the episode explicitly nonquiet; changing d or m cannot reset this.
- If a is not in A_*, run the ordinary R434 protected continuation. It either closes H, exits through explicit nonquiet geometry, or completes quietly back to an aligned floor retaining singleton a. In the last case append a to A_*.

Thus every branch of the common-center star has a finite continuation

  TWO-COVER,
  or explicit a-anchored nonquiet geometry,
  or strict global progress |A_*| -> |A_*|+1.               (BA.12)

Equivalently, with epsilon_*=|V(H)|-|A_*|,

  epsilon_* -> epsilon_*-1                                 (BA.13)

in every quiet fresh-center completion.

### 5. Lex-minimal family consequence
In a reconstruction-closed nonclosing family chosen with epsilon_* minimal, the third alternative in (BA.12) is forbidden. Hence one retained bad singleton mixed state forces, simultaneously at the family level, an a-anchored nonquiet continuation for every good root in D-{o}. When |D|>=5 this is a common-center packet of at least four root alternatives, all carrying the SAME bad row and SAME selected mixed state as upstream ancestry.

This is the direct global-budget interface missing from a support-only analysis of the order-seven necklace. The local certificate SV64875 does not encode C_y, the selected Omega|Q state, or the globally completed-anchor ledger, so it does not test BA.12.

### 6. Scope fence
BA.12 is genuine strict epsilon_* progress when the center a is fresh and the protected continuation remains quiet. It is not a proof that the alternative common-center nonquiet packet closes H. The root descendants in (BA.10) remain alternative certificate-retaining continuations, not simultaneous current floors. No strict Phi improvement is claimed. R24 and R5 are not used.

## References

```json
[
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
        "revision_id": "R432"
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
        "revision_id": "R533"
    }
]
```