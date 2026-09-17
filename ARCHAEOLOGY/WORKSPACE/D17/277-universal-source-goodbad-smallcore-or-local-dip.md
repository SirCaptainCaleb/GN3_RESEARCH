# A large Arm-U puncture is fixed-complement R435-active, universally four-core, or strictly locally cap-dipping

**Workspace:** D17
**State:** established
**Key:** `universal-source-goodbad-smallcore-or-local-dip`

**Summary:** In an Arm-U fixed universe V(H)=Omega disjoint B, fix a good label q and an actual Hamilton puncture path P_q on Omega-q. Put a=|P_q|, b=|B| and M=max(a,b). If both endpoints of P_q are good, SV48242/R966 already gives explicit R435 geometry among common-B puncture rows. Otherwise choose a bad endpoint r. For a left endpoint write P_q=(r,p,s,...). Badness of r gives (s,p,q) tight while (r,p,s) is inherited. Test (q,p,r). If tight, the three turns form a directed comparison star-triangle at p on X={q,r,p,s}; every five-set X+y is then nonintegrable and hence Hamiltonian by accepted R902, so X is universally one-vertex Hamilton-extendable. If the test is bad, R3 gives the bridge trimer T=(r,p,q). Apply SV49328 to T plus the two endpoints of B. Either one endpoint completes T to a Hamilton P4, or both endpoints together give a Hamilton P5. In the P4 case the complement is exactly the two literal paths P_q-{r,p} and B minus that endpoint, with rail orders a-2 and b-1; in the P5 case the complement is exactly P_q-{r,p} and B with both endpoints removed, of orders a-2 and b-2. Therefore when M>=6 the resulting spanning three-forest has largest rail at most M-1. The bad right-endpoint case is the exact ordered dual. Thus every Arm-U puncture in the large range M>=6 exports fixed-complement R435 curvature, a universal one-extension four-core, or an explicit strict local largest-rail dip. The dip is not claimed to be global phased-Morse reentry.

### 1. Setup and the good-good exit
Let H be a hypothetical smallest counterexample and retain one Arm-U fixed universe

  V(H)=Omega disjoint_union V(B),
  B=(b_0,b_1,...,b_t),                                   (AU.1)

with B a literal Hamilton tight path and Omega non-Hamiltonian. Fix a GOOD deletion label q and an ACTUAL Hamilton puncture path

  P_q=(p_0,p_1,...,p_m)                                  (AU.2)

on Omega-q. Write

  a=|P_q|=m+1,
  b=|B|=t+1,
  M=max(a,b).                                             (AU.3)

The R24-free singleton-source floor proved directly in SV51259 gives a,b>=3.

Apply the endpoint router SV51259. If both physical endpoints of P_q are good, accepted R966 supplies explicit R435 Reverse-Ear geometry among three actual Hamilton puncture rows, all with the SAME literal complement B. Retain that FIXED-COMPLEMENT R435 output and stop.

Hence only the case of a BAD physical endpoint remains.

### 2. Left bad endpoint: one three-turn test
After naming the left endpoint bad, write

  P_q=(r,p,s,p_3,...,p_m),                               (AU.4)

where r lies in D(Omega). The inherited source turn

  (r,p,s) tight                                           (AU.5)

is graph-intrinsic.

Because r is bad, Omega-r is non-Hamiltonian. Replacing r by q in the displayed puncture order gives the candidate word

  (q,p,s,p_3,...,p_m).                                   (AU.6)

Every turn after the first is inherited from P_q. Therefore its first turn (q,p,s) must be bad, and R3 gives

  (s,p,q) tight.                                         (AU.7)

Now test the single remaining middle-p turn

  sigma=(q,p,r).                                         (AU.8)

This test is the entire local branch.

### 3. Tight sigma gives a universal one-extension four-core
Suppose sigma is tight. At the common middle vertex p, equations (AU.5), (AU.7), and (AU.8) give the directed comparison cycle

  pr -> ps -> pq -> pr                                   (AU.9)

in the line-graph comparison orientation. Hence the four-set

  X={q,r,p,s}                                             (AU.10)

is nonintegrable: its comparison orientation already contains a directed star triangle.

Let y be ANY vertex outside X. The induced five-set X+y still contains the directed cycle (AU.9), so its comparison orientation is nonintegrable. Accepted R902 says every nonHamilton five-vertex boundary tournament is edge-orderable. Contrapositively, every nonintegrable five-set is Hamiltonian. Therefore

  X+y is Hamiltonian for every y outside X.               (AU.11)

Thus X is a UNIVERSALLY ONE-VERTEX HAMILTON-EXTENDABLE FOUR-CORE. No representative currentization is needed; the certificate is the literal directed comparison triangle (AU.9).

### 4. Bad sigma gives one bridge trimer
Suppose instead sigma is bad. Boundary antisymmetry R3 gives

  (r,p,q) tight.                                         (AU.12)

Put

  T=(r,p,q).                                              (AU.13)

This is a graph-intrinsic tight trimer. It contains the bad endpoint r, its inward source neighbor p, and the omitted good source label q. We now spend the two physical endpoints of the fixed complementary rail B against this one trimer.

### 5. The order-free five-cell compiler forces P4 or P5
Consider the two four-sets

  V(T)+b_0,
  V(T)+b_t.                                               (AU.14)

If either supports a Hamilton P4, retain one such P4 Q_4. Otherwise both four-sets are P4-free and the order-free common-triangle theorem SV49328 applies with shared triangle V(T). It gives a Hamilton P5 Q_5 on

  V(T)+{b_0,b_t}.                                        (AU.15)

Thus the bad-sigma branch has exactly the useful alternative

  P4 on T plus one B-endpoint,
  OR
  P5 on T plus both B-endpoints.                          (AU.16)

No edge-orderability hypothesis is present: SV49328 already combines the R902 nonintegrable branch with accepted edge-ordered R963.

### 6. Literal complement bookkeeping: both outputs are current maximum forests
First suppose Q_4 is supported on T+b_0; the b_t case is identical. Removing its four physical vertices q,r,p,b_0 from H leaves exactly

  (s,p_3,...,p_m) | (b_1,b_2,...,b_t).                   (AU.17)

Both displayed words are literal tight paths inherited from P_q and B. Their orders are

  a-2,  b-1.                                             (AU.18)

Hence

  Q_4 | P_q-{r,p} | B-b_0                               (AU.19)

is a literal spanning three-path forest of H with rail-order multiset

  {4,a-2,b-1}.                                           (AU.20)

Now suppose Q_5 is the five-path from (AU.15). Removing q,r,p,b_0,b_t leaves exactly

  (s,p_3,...,p_m) | (b_1,b_2,...,b_{t-1}),              (AU.21)

again two literal tight paths, of orders a-2 and b-2. Thus

  Q_5 | P_q-{r,p} | B-{b_0,b_t}                          (AU.22)

is a literal spanning three-path forest with rail-order multiset

  {5,a-2,b-2}.                                           (AU.23)

Because a,b>=3, no hidden empty-component issue occurs in either construction.

### 7. Large source range gives a strict local largest-rail dip
Assume

  M=max(a,b)>=6.                                          (AU.24)

The original restored source forest

  P_q | B | {q}                                          (AU.25)

has largest rail order M.

In the P4 branch,

  max{4,a-2,b-1} <= M-1.                                 (AU.26)

In the P5 branch,

  max{5,a-2,b-2} <= M-1.                                 (AU.27)

Therefore every non-small-core bad-endpoint branch produces an explicit CURRENT maximum three-forest whose largest rail is strictly smaller than the largest rail of the source forest.

Call this a LOCAL CAP DIP. It is a real representative-level improvement, not a metaphor: all three new path words are displayed and their supports partition V(H).

It is deliberately NOT promoted to completed phased-Morse descent. Guidance G18's fence remains essential: after entering the canonical largest-rail rewrite system, a later A-growth normalization may recover the old height. Equations (AU.26)-(AU.27) establish only a strict local excursion in the current forest coordinate.

### 8. Right bad endpoint is the exact ordered dual
Suppose instead the bad endpoint is the right endpoint. Write

  P_q=(p_0,...,s,p,r).                                    (AU.28)

The inherited turn is

  (s,p,r) tight,                                          (AU.29)

while non-Hamiltonicity of Omega-r makes the terminal replacement turn (s,p,q) bad, hence

  (q,p,s) tight.                                          (AU.30)

Test

  (r,p,q).                                                (AU.31)

If it is tight, then at middle p

  ps -> pr -> pq -> ps                                   (AU.32)

is a directed comparison star triangle and X={q,r,p,s} is universally one-extendable by the same R902 argument.

If (AU.31) is bad, R3 gives the bridge trimer

  (q,p,r) tight.                                          (AU.33)

Apply SV49328 with the two B endpoints exactly as in Sections 5-7. The P4/P5 supports remove q,p,r and one/two B endpoints; the untouched prefix of P_q and the untouched B segment are literal complementary rails of orders a-2 and b-1/b-2. Hence the same local cap dip follows when M>=6.

No reversal of P_q is used.

### 9. Arm-U large-range compression
For EVERY good q and EVERY retained actual Hamilton puncture path P_q in an Arm-U fixed universe, if M=max(|P_q|,|B|)>=6, one of the following occurs:

1. FIXED-COMPLEMENT R435 CURVATURE: both puncture endpoints are good, so SV51259/R966 gives explicit R435 geometry among common-B singleton rows;
2. UNIVERSAL FOUR-CORE: a bad endpoint has the tight middle test of Section 3 or 8;
3. STRICT LOCAL CAP DIP: a bad endpoint has the bad middle test, and the P4/P5 compiler yields a literal maximum forest whose largest rail is at most M-1.   (AU.34)

Thus the bidirectional two-probe wall and parity-leakage structures of SV48512/SV48783 are not terminal in the large Arm-U range. They are useful intermediate certificates, but the endpoint source order itself already collapses the whole good-bad branch to SMALL CORE or LOCAL DIP.

The only numerical residue not covered by the strict-dip conclusion is M<=5. In particular, when M=5 the P5 branch has rail profile {5,a-2,b-2}, so the largest rail need not drop. No secondary global rank is asserted here.

### 10. G18 synthesis
This brings Arm U to the same theorem-scale interface as the current Arm-M fixed-cap work, including SV49051:

  R435 curvature,
  OR universal one-extension four-core,
  OR explicit local cap dip.                              (AU.35)

The two arms reach this interface by different physical mechanisms: Arm M uses endpoint-return parity and reciprocal-root diagonalization, while Arm U uses one bad endpoint, one middle-p comparison triangle test, and the order-free five-cell compiler.

What remains common is exactly the G18 obligation: consume same-/fixed-complement R435 curvature and local cap-dip excursions into TWO-COVER or genuine reentry below the pre-curvature phased-Morse checkpoint. The present theorem sharply removes the Arm-U two-probe wall as an additional large-range parent obstruction.

Status: complete internal working mathematics, unreviewed exposition. No canonical certification or global phased-Morse cancellation is claimed.

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
        "revision_id": "R902"
    }
]
```