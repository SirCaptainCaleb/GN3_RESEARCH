# The aligned G32 exception is a same-support maximum-forest reversal and transports to R561 or a wrap shield

**Workspace:** D17
**State:** established
**Key:** `g32-aligned-exception-selected-reversal-forest-transport`

**Summary:** In the sole aligned no-B-active-omission residue, let {v,s} be the common endpoint-gate M_S edge and {t,u} the complementary B-active spoke edge. Universal spectator stars and the aligned gates give two Hamilton P6s on one support, (b1,b0,v,s,bm,b_{m-1}) and (b1,b0,s,v,bm,b_{m-1}), selecting {v,s} oppositely. Since |H|>10, the spectator middle B[2,m-2] is nonempty; SV89302 gives a Hamilton P4 on the complementary outer four-set {A,C,t,u}. Pairing either P6 with that same outer P4 and the same spectator-middle path yields two literal maximum spanning three-forests with identical support partition and frozen complementary rails. SV36339 therefore transports the physical {v,s} reversal finitely to R561 support escape/two-cover or an exact current reverse-wrap trimer. Thus the aligned rigid middle-matching cell is not a terminal static G32 obstruction; after the crossed cell is eliminated by SV101535, every no-active-omission exception exports to established maximum-forest reversal transport. This is an export theorem, not direct three-spoke absorption.

### 1. Sole aligned rigid input
Retain the G32 transitive singleton-star spectator frame after SV101535. Work in the only surviving no-B-active-omission branch from SV100744/SV101932. Write the source anchors as A,C, the spectator rail as

  B=(b_0,b_1,...,b_{m-1},b_m),

and the transitive four-cell as

  X={v,s,t,u}.

Here s is the unique B-inactive source spoke, {v,s} is the common aligned endpoint-gate M_S edge, and {t,u} is the complementary M_S edge consisting of the two B-active source spokes. The three source turns

  (A,s,C), (A,t,C), (A,u,C)

are retained. By SV99565 the universal endpoint stars hold:

  (b_1,b_0,x) and (x,b_m,b_{m-1})

are tight for every x in X. The aligned gate on {v,s} gives both orders

  (b_0,v,s), (b_0,s,v), (v,s,b_m), (s,v,b_m)

tight.

### 2. Two opposite-order boundary P6s
Concatenating the displayed turns gives two literal Hamilton P6s on the same six-vertex support

  Y={b_1,b_0,v,s,b_m,b_{m-1}}:

  Q^+=(b_1,b_0,v,s,b_m,b_{m-1}),
  Q^-=(b_1,b_0,s,v,b_m,b_{m-1}).

Indeed their four consecutive turns are supplied respectively by the left universal star, the aligned L-gate, the aligned R-gate, and the right universal star. The two paths select the same physical dimer {v,s} in opposite orders.

### 3. Freeze the two complementary rails
Because H is a hypothetical smallest counterexample, accepted R533 gives |H|>10. Since V(H) is the disjoint union of {A,C}, X, and V(B),

  |B|=|H|-6 >=5.

Hence m>=4 and the literal middle spectator path

  M=B[2,m-2]=(b_2,...,b_{m-2})

is nonempty (possibly a singleton when |B|=5).

The two B-active source spokes t,u have the same outer orientation through A,C. Exact unit SV89302 therefore gives a literal Hamilton P4 P_O on the complementary four-set

  O={A,C,t,u}.

The supports Y,O,V(M) are pairwise disjoint and partition V(H). Thus

  F^+=Q^+ | P_O | M,
  F^-=Q^- | P_O | M

are literal spanning three-path covers. Since H is a counterexample with pc(H)=3, both are maximum spanning three-forests. They have identical three support sets and the complementary rails P_O,M are literally frozen. Their active Hamilton rails Q^+,Q^- select the physical dimer {v,s} oppositely.

### 4. Apply same-support reversal transport
This is exactly the hypothesis of established SV36339 `compatible-forest-selected-reversal-two-rail-transport`, with active support Y, frozen spectators P_O,M, and reversed dimer {v,s}. Therefore the finite R548 transport has only the accepted terminal alternatives:

1. R561 boundary-reversed Hamilton-dimer geometry on Y. Then every exterior vertex Hamilton-extends Y; absorbing an endpoint of P_O or M gives either a spanning two-cover when that spectator rail is a singleton, or a genuine support-changing maximum three-forest.
2. A failed transport wrap produces one of the exact named reverse-wrap shield trimers, and SV36339/R4 currentizes that proper trimer as a rail of an actual maximum spanning three-forest.

No spectator support or order is changed during the selected-reversal transport before one of these terminal alternatives occurs.

### 5. Consequence for G32
SV101535 already removes the crossed rigid middle-matching exception. The present section removes the aligned rigid exception as a terminal STATIC spectator-frame cell: if R582 cannot omit a B-active source spoke, the aligned packet itself creates a same-support maximum-forest reversal and immediately enters the established R561/support-escape or wrap-shield interface.

Thus the only branch still requiring the G32 trimerized full-H endpoint-cut construction inside the static spectator-frame program is the branch where an endpoint-favorable K_s actually omits a B-active source spoke and carries its retained old source incidence into B.

This theorem is an export/reduction, not a spanning-two-cover proof and not a claim that wrap-shield geometry is already absorbed. It does not invoke payment, R24, or R5.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R533"
    }
]
```
