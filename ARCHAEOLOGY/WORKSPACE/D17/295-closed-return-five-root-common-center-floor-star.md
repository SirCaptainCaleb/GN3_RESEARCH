# The five-root return fan pays to one common-center floor star

**Workspace:** D17
**State:** established
**Key:** `closed-return-five-root-common-center-floor-star`

**Summary:** Refine SV58280 at proof level. Fix its one component-drop cross-state x->y in T_K relative to the source cover R_K of H-K. R176 uses the same crossed R_K-component for every spare d in the Hamilton P5 K. If that component is singleton {x}, R176 directly gives the floor {x,d}. If it is nontrivial, fix one literal R_K-neighbor p of x. The single R3 bit on {p,x,y} determines once and for all a signed dimer D: either (x,p) head-signed by y or (p,x) tail-signed by y. For every d in K, the automatic d-y dimer gives singleton d the opposite polarity, so all five R176 births share the identical nontrivial support D, witness y, and signed anchor x; only the spare singleton d changes. Applying R428 while preserving d to this order-two opposite support has only one nonclosing outcome: the unsigned endpoint p is clipped and the signed endpoint x survives. Hence every nonclosing rooted branch lands at the ancestry-bearing floor {x,d}. Therefore one pair-deletion frame supplies a five-leaf paid-floor star with common center x and roots exactly the five vertices of K, together with the same K, source frame, cross-state x->y, and common birth ancestor D (when nontrivial). The paid descendants remain alternatives. This strengthens the G22 family object but does not rule out a rank-flat sink.

### 1. Fix the common component-drop cross-state
Retain SV58280. Thus one exact pair-deletion frame produces a Hamilton P5 K on five physical vertices and, after deleting the three selected internal middles used to build K, a literal cover R_K of W=H-K with at least three components. Let T_K be an at-most-two-path cover of W and fix one selected directed cross-state

  x -> y

whose endpoints lie in distinct R_K-components. This cross-state is chosen once. Every rooted pair birth below uses this same x,y and differs only in the spare vertex d in K.

### 2. R176 has one fixed opposite support for all five spares
Let C_x be the R_K-component containing x.

If C_x is the singleton path (x), the singleton case of accepted R176 gives, for every spare d in K, a balanced opposite-sign pair whose supports are literally (x) and (d). Hence the claimed common-center floor already exists.

Assume C_x is nontrivial. Choose once and for all a literal R_K-neighbor p of x. Accepted R176/P540 applies R3 to the fixed triple {p,x,y}. Exactly one of

  (y,x,p),   (p,x,y)

is tight. This choice is independent of d.

- If (y,x,p) is tight, the fixed dimer D=(x,p) is head-signed by y. For every d in K, the automatic path (d,y) makes singleton (d) tail-signed by the same witness y.
- If (p,x,y) is tight, the fixed dimer D=(p,x) is tail-signed by y. For every d in K, the automatic path (y,d) makes singleton (d) head-signed by y.

Thus all five R176 births have the form

  fixed signed dimer D with signed physical anchor x
  + opposite singleton (d),   d in K.

The support D, its tested orientation, the common witness y, the old neighbor p, and the selected cross-state x->y are identical in all five births. Only the spare singleton varies. All five birth certificates are graph-intrinsic consequences of the one common parent frame; no paid descendants are asserted simultaneous.

### 3. Paying a root preserves d and leaves exactly x
Fix d in K and take the corresponding R176 birth. Apply accepted R428 with the singleton (d) as the fixed coordinate and D as the nontrivial opposite support. Because D has order two, every nonclosing first refund removes its unsigned endpoint and leaves its signed endpoint. This can be read directly from the R175 step inside the reconstructed proof of R428: the one-rail refund clips the unsigned end of the signed dimer and Signed-Interval Rebirth preserves the signed endpoint. If the outside reservoir has size zero or one, the order-two special cases in R428 close H rather than produce a different singleton.

In both R176 orientations above the signed endpoint of D is x. Therefore the chosen continuation yields exactly

  TWO-COVER, or the ancestry-bearing floor {(d),(x)}.

No second possible center occurs. The x-sign retains the common R176/R428 ancestry through D and y.

### 4. Five-root common-center floor star
Consequently SV58280 sharpens to the following bounded family certificate. One physical pair-deletion frame supplies a Hamilton P5 K and one exterior physical vertex x such that for every d in V(K) there is a lawful certificate-retaining continuation

  common parent -> root d birth -> TWO-COVER or floor {x,d}.

If no branch closes, the five alternative floors form the exact star

  {x,d},  d in V(K).

They share not only x but also the source pair-deletion frame, K, the punctured source cover R_K, the selected cross-state x->y, and, in the nontrivial-component case, the same signed dimer ancestor D and witness y.

This is strictly stronger than five arbitrary rooted floors. Any G22 normalized sink-family quotient that absorbs SV58280 must be liftable for this common-center five-root star and must retain enough physical ancestry to distinguish its common D/x/y origin.

### 5. Scope fence
The five paid descendants are alternatives, not simultaneous current floors. Singleton signs are formally cheap, so the star alone is not a contradiction. No fixed-E rank decrease is claimed. The gain is the collapse of five apparently independent payment branches to one bounded common-support/common-center family object, suitable for a closed-family recurrence argument.

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
    }
]
```