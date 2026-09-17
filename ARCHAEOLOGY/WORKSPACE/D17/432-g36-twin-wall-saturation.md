# A P5-free G36 twin wall saturates both anchor turns at d

**Workspace:** D17
**State:** established
**Key:** `g36-twin-wall-saturation`

**Summary:** Once D17.430 reaches the twin-anchor wall residue, absence of a Hamilton P5 forces two additional turns at the far wall vertex `d`. In the OUT packet, `(b,d,A)` and `(b,d,C)` are both tight. In the IN packet, `(A,d,b)` and `(C,d,b)` are both tight. The proof is two one-line R3 contradictions in each polarity. This sharpening is independent of R902 after the twin wall itself has been obtained.

## 1. OUT twin wall
Assume the P5-free OUT twin-wall residue from D17.430. Thus

`(d,b,t)`, `(b,t,A)`, `(b,t,C)`

are tight.

We claim both

`(b,d,A)` and `(b,d,C)`

are tight.

If `(b,d,A)` were bad, boundary antisymmetry R3 would give `(A,d,b)` tight. Then

`(A,d,b,t,C)`

is a tight Hamilton P5, using consecutively

`(A,d,b)`, `(d,b,t)`, `(b,t,C)`,

contrary to the P5-free assumption. Hence `(b,d,A)` is tight.

Similarly, if `(b,d,C)` were bad, R3 would give `(C,d,b)` tight, and

`(C,d,b,t,A)`

would be a tight Hamilton P5. Hence `(b,d,C)` is tight.

Therefore a P5-free OUT twin wall carries two forced tail witnesses on the ordered wall edge `(b,d)`:

`(b,d,A)`, `(b,d,C)`.

## 2. IN twin wall
Assume the P5-free IN twin-wall residue from D17.430. Thus

`(t,b,d)`, `(A,t,b)`, `(C,t,b)`

are tight.

We claim both

`(A,d,b)` and `(C,d,b)`

are tight.

If `(A,d,b)` were bad, R3 gives `(b,d,A)` tight. Then

`(C,t,b,d,A)`

is a tight Hamilton P5, using

`(C,t,b)`, `(t,b,d)`, `(b,d,A)`.

Thus `(A,d,b)` is tight.

Likewise, if `(C,d,b)` were bad, R3 gives `(b,d,C)` tight, and

`(A,t,b,d,C)`

is a tight Hamilton P5. Thus `(C,d,b)` is tight.

Therefore a P5-free IN twin wall carries two forced head witnesses on the ordered wall edge `(d,b)`:

`(A,d,b)`, `(C,d,b)`.

## 3. Consequence and scope
The P5-free twin-anchor residue is strictly more rigid than the raw pair of shared-wall P4s: both source anchors are forced to interact with the far wall edge in the same polarity.

This is only a local saturation theorem. It does not itself produce a two-cover, a transition descent, or an endpoint-controlled Hamilton P5. In particular, D17.431 shows that nearby retained seams alone do not license arbitrary endpoint control.

After D17.430 has supplied the twin-wall packet, the present proof uses only boundary antisymmetry R3. No use is made of R902, R24, R5, payment/replay machinery, or the quarantined reflection route.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```