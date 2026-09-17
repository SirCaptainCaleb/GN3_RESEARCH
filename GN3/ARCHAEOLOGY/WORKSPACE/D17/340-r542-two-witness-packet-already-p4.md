# Every R542-ready reverse-boundary packet already contains a literal P4

**Workspace:** D17
**State:** established
**Key:** `r542-two-witness-packet-already-p4`

**Summary:** Let K=(a,b,c) be a tight trimer and let one reverse boundary dimer be signed by two distinct same-polarity witnesses outside K, exactly the R542 hypothesis. Then a literal P4 already exists before any capture/payment. For the reverse initial dimer (b,a) tail-signed by w1,w2, test (a,w_i,c). If one is tight, (b,a,w_i,c) is a P4. If both are bad, R3 gives (c,w_i,a) for i=1,2 and R584 forces one of (c,w1,a,w2),(c,w2,a,w1). The reverse-terminal head-signed case is dual: a tight (a,w_i,c) gives (a,w_i,c,b), while two failures give the same R584 pair. Thus R542 is useful for ancestry-bearing payment but is not an independent geometric species in a bottom-family alphabet: every R542-ready packet carries source-visible P4 geometry.

### 1. Reverse-initial packet
Let H be a Strong Level-(1) boundary tournament, let

  K=(a,b,c)

be a vertex-simple tight trimer, and let w_1,w_2 be distinct vertices outside K. Suppose the reverse initial dimer

  D_L=(b,a)

is tail-signed by both witnesses:

  (b,a,w_1), (b,a,w_2) tight.                    (RP.1)

This is exactly the local signed geometry required by R542 on the initial side.

For i=1,2 test

  X_i=(a,w_i,c).                                  (RP.2)

If some X_i is tight, then the consecutive turns

  (b,a,w_i), (a,w_i,c)

make the literal vertex-simple tight P4

  (b,a,w_i,c).                                    (RP.3)

Assume both X_1,X_2 are bad. By R3 their complete reversals are tight:

  (c,w_1,a), (c,w_2,a).                           (RP.4)

Apply accepted R584 with common poles A=c and C=a and probes w_1,w_2. It yields one of

  (c,w_1,a,w_2),
  (c,w_2,a,w_1),                                  (RP.5)

as a literal tight P4. All four vertices are distinct because w_1,w_2 lie outside K.

Hence every reverse-initial R542-ready packet already contains a P4.

### 2. Reverse-terminal packet
Now suppose instead that the reverse terminal dimer

  D_R=(c,b)

is head-signed by w_1,w_2:

  (w_1,c,b), (w_2,c,b) tight.                     (RP.6)

Test the same turns X_i=(a,w_i,c). If some X_i is tight, then

  (a,w_i,c,b)                                      (RP.7)

is a literal P4. If both X_i are bad, R3 again gives (RP.4), and R584 again gives one of the P4s in (RP.5).

Thus the terminal-head case is exact without invoking informal path reversal.

### 3. Consequence for R542 recycling
Every packet satisfying accepted R542 therefore has TWO simultaneous interfaces:

- the certificate-retaining capture/payment continuation supplied by R542;
- a graph-intrinsic literal P4 already present in the source packet.

The P4 conclusion uses only R3 and R584 and is independent of which R542 capture crossing or paid descendant is later chosen. Consequently a reconstruction-closed phase-zero family cannot treat R542 as an anonymous payment-only symbol: it must also absorb explicit P4 geometry with the exact carrier boundary, two witness identities, and tested orientation retained.

### 4. Scope fence
A P4 born at phase zero is not numerical progress in the exhausted fixed-E clock. This section does not claim that R542 closes H, that its paid descendant coexists with the P4 as a current representative, or that repeated R542 use is monotone. It only removes R542 as a distinct geometric residue.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R584"
    }
]
```