# A matched-endpoint reverse trimer either makes a cap dip, a universal four-core, or diagonalizes to same-support curvature

**Workspace:** D17
**State:** established
**Key:** `uniform-middle-layer-matched-endpoint-trimer-diagonalization`

**Summary:** In the fixed-cap SV46809 cylinder, take three consecutive labels a->b->c on the extremal endpoint-return cycle and an actual puncture path P_a on Omega-a exposing b. If the R435 comparison with P_b emits a one-foreign reverse trimer immediately at the matched endpoint b, then either the opposite seam closes a directed comparison triangle and hence a universally one-extendable four-set, or antisymmetry replaces b by a in exactly the same ordered residual core, producing a Hamilton path P'_b on Omega-b. Comparing P'_b with the actual matched puncture path P_b is now a same-support comparison. If it is R435-active, neighboring-support curvature has strictly diagonalized to same-support curvature. If it is R435-quiet, the two words coincide; since P_b exposes c, the original P_a also exposes c. In the no-prior-dip regime the matched edges a->b and b->c flip cross-cap parity, so chi_C(a)=chi_C(c), and this skip-one endpoint incidence gives the equal-parity SV46809 P4/P5 cap-dip forest. The TAIL role is dual. Thus the reciprocal-root/common-core equality cell is not terminal: outside the small-core or local cap-dip outputs it reduces support-discrepancy depth from one to zero. This is a local curvature reduction, not yet genuine phased-Morse reentry; a bare k to k-1 dip is still only an excursion until its canonical return checkpoint is compared.


### 1. Fixed-cap endpoint-return coordinates
Work in accepted R927(M) in the live range k>=6. Fix a literal Hamilton k-cap

  C=(c_0,...,c_{k-1})

and put Omega=V(H)-V(C). Retain the extremal R945 endpoint-return matching used in SV46809 and three consecutive labels

  a -> b -> c.                                             (MD.1)

Let P_a be the actual Hamilton puncture path on Omega-a which exposes the matched endpoint b, and let P_b be the actual Hamilton puncture path on Omega-b which exposes c. Both singleton-deletion rows use the SAME literal complement C.

If either matched edge a->b or b->c has equal cross-cap parity, the explicit equal-parity splice of SV46809 already gives a spanning maximum three-forest whose largest rail has order k-1. Hence, in the branch with no such local cap dip,

  chi_C(a) != chi_C(b),
  chi_C(b) != chi_C(c),

and therefore

  chi_C(a)=chi_C(c).                                      (MD.2)

We now consume the reverse-trimer curvature cell which is adjacent to the matched endpoint b of P_a.

### 2. HEAD role: root swap on one fixed ordered core
Suppose b is the HEAD of P_a. Write

  P_a=(b,r_0,r_1,...,r_t).                                (MD.3)

Assume the neighboring-support R435 comparison emits the first-seam one-foreign reverse trimer

  (a,r_0,b) tight.                                        (MD.4)

This is exactly the i=1 endpoint-adjacent instance of the reverse-trimer currentization mechanism SV26759.

Test the opposite turn

  (r_1,r_0,a).                                            (MD.5)

If (MD.5) is tight, then (MD.4), the inherited tight turn

  (b,r_0,r_1),

and (MD.5) form the directed comparison triangle at middle r_0 used in SV26759. Consequently

  X={a,b,r_0,r_1}                                         (MD.6)

is universally one-extendable by accepted R902. This is the SMALL-CORE output.

Assume instead that (MD.5) is bad. Boundary antisymmetry R3 gives

  (a,r_0,r_1) tight.                                      (MD.7)

All later turns are inherited from P_a, so

  P'_b=(a,r_0,r_1,...,r_t)                                (MD.8)

is a literal Hamilton path on Omega-b. Thus the endpoint-adjacent reverse trimer has not merely produced an anonymous fresh forest: it has exchanged the puncture root b for a while preserving the entire ordered residual core

  R=(r_0,r_1,...,r_t)                                     (MD.9)

and the literal cap C.

### 3. The reciprocal-root equality cell either dips or becomes same-support curvature
Compare the new Hamilton path P'_b with the actual matched puncture path P_b. They have exactly the same support Omega-b.

If this comparison is R435-nonquiet, retain its adjacent reversal, reverse trimer, or proper cycle. This is now SAME-SUPPORT R435 curvature. Relative to the original neighboring puncture comparison, the support-discrepancy depth has strictly decreased from one exchanged label to zero.

Suppose instead the comparison P'_b versus P_b is R435-quiet. Since every vertex is common, R435 contact monotonicity forces the two oriented Hamilton words to be identical:

  P_b=P'_b.                                               (MD.10)

The actual matched path P_b exposes c as a physical endpoint. The endpoints of P'_b are a and r_t. The cycle labels are distinct, so c!=a and therefore

  c=r_t.                                                  (MD.11)

But then the ORIGINAL path P_a in (MD.3) has endpoint set {b,c}. In particular it is also an actual Hamilton puncture path on Omega-a exposing c. Hence the endpoint core

  Omega-{a,c}                                             (MD.12)

is a genuine endpoint incidence for the left label a, witnessed by P_a itself. Matchedness of this skip-one incidence is irrelevant to the equal-parity splice: deleting the exposed endpoint c from P_a gives a Hamilton path

  D_ac=P_a-c

on Omega-{a,c}, so

  H-{a,c}=C | D_ac                                        (MD.13)

is the literal pair-deletion frame needed in the proof of SV46809.

By (MD.2), chi_C(a)=chi_C(c). If both bits are one, accepted R584 plus the fixed two-ended wall of C gives the same P5 splice as SV46809; if both bits are zero, R3 and R584 give the same P4 splice. In either case one obtains the explicit spanning maximum three-forest with largest rail of order k-1.

Thus quietness of the reciprocal-root comparison forces the LOCAL CAP-DIP output.

### 4. TAIL role is exact dual
Suppose b is instead the TAIL of the matched puncture path. Write

  P_a=(r_t,...,r_1,r_0,b).                                (MD.14)

The endpoint-adjacent second-seam reverse trimer is

  (b,r_0,a) tight.                                        (MD.15)

Test (a,r_0,r_1). If it is tight, (MD.15), the inherited turn (r_1,r_0,b), and the test form the same directed comparison triangle and yield the universal four-core {a,b,r_0,r_1}. If the test is bad, R3 gives

  (r_1,r_0,a) tight,

so

  P'_b=(r_t,...,r_1,r_0,a)                                (MD.16)

is Hamilton on Omega-b with the identical ordered residual core. Compare P'_b with P_b. A nonquiet comparison is same-support R435 curvature. A quiet comparison forces literal identity, hence the matched endpoint c of P_b is the opposite endpoint r_t. Therefore P_a also exposes c, and the equal-parity skip-one splice again gives the cap-dip forest.

### 5. Diagonalization theorem and Morse interpretation
We have proved the following exact local statement.

> MATCHED-ENDPOINT TRIMER DIAGONALIZATION. In the fixed-cap SV46809 endpoint-return cylinder, let a->b->c be consecutive matched labels. If the neighboring-support R435 comparison at a->b emits a one-foreign reverse trimer immediately at the matched endpoint b of P_a, then at least one of the following occurs:
>
> 1. a physical four-set is universally one-extendable;
> 2. an explicit equal-parity P4/P5 splice gives a spanning maximum three-forest whose largest rail has order k-1;
> 3. the curvature reduces to an R435-active comparison of two Hamilton paths on the SAME support Omega-b, with the same fixed cap C.

The important equality mechanism is therefore narrower than it first appears. The literal reciprocal-root cell

  (a) | (b,R) | C   <->   (b) | (a,R) | C                 (MD.17)

cannot remain a terminal neighboring-support flat sector: if the second word agrees with the actual b-puncture representative, it creates the equal-parity skip-one incidence a->c and the cap dip; if it disagrees, all remaining curvature has been diagonalized to one support.

This supplies a genuine local auxiliary coordinate: support-discrepancy depth rho, with rho=1 for neighboring puncture supports and rho=0 for same-support curvature. The present theorem strictly lowers rho outside SMALL-CORE or CAP-DIP.

It does NOT promote CAP-DIP to completed SV41376 descent. Guidance G18's warning remains in force: after a k->k-1 excursion, canonical A-growth may return to cap height k. The surviving cancellation problem is now concentrated on same-support R435 curvature and on proving that the cap-dip excursion returns below the old global checkpoint.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R584"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R945"
    }
]
```