# Gamma ancestry makes one-row reconstruction P4-valued and conditionally forbids a P4-free paired tau-one terminal

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-gamma-tau1-p4-refinement`

**Summary:** The failed sibling in an exactly-one-gamma q2 reconstruction is useful current data: probing the common trimer (c0,c,t) by d,y through R700 either directly gives a P4 or tail-signs (c,c0), while the failed sibling gamma head-signs the same tested dimer; R523 therefore gives a labelled P4. Thus a one-gamma H-t row always carries a P4 in addition to the exact reconstruction. For paired gamma rows there is no unconditional transport to tau=1. While the rows remain synchronized, a common successful tail rotation sends (lambda,tau) to (lambda-1,tau+1), a common B+s source transfer sends it to (lambda-1,tau), and a common terminal shave through Hamiltonian B+q sends it to (lambda,tau-1). These moves are well-founded in lambda-first lexicographic order but may terminate at tau>=2, and a one-row move may destroy synchronization. Conditional on actually reaching a synchronized tau=1 state with lambda>0, all common T+ support transfers unavailable, both row-specific tail wraps blocked, and no earlier opposite-wrap P4 output, the SV14742 boundary argument applies to both rows. If either boundary four-cell is Hamiltonian, retain that cover-aware P4. If both are P4-free, signature 11 in both produces P4s (d,t,q,y) and (y,t,q,d); R833 applied to the latter exact middle-dimer deletion cover forces (t,y,c), contradicting the original P4-free lower-lift cell via (d,t,y,c). Thus the tau-one conclusion is valid as a conditional laboratory, not as a guaranteed normal form.

### 1. Exactly one gamma gives an H-t row carrying a labelled P4
Retain the lower q2 insertion branch of `singleton-deep-q2-local-insertion` SV12272. Thus c has actual predecessor c_0, the common seam

  alpha=(c_0,c,t)

is tight, the four-set X_0={t,d,y,c} is P4-free, and the only lower H-t seams are

  gamma_d=(c_0,c,d),   gamma_y=(c_0,c,y).

Suppose exactly gamma_d is tight. Then G_d together with the untouched other rail is an actual exact H-t two-cover selecting d->y, while gamma_y is bad and R3 gives

  (y,c,c_0) tight.

The common alpha seam makes

  K_0=(c_0,c,t)

a tight trimer. Probe K_0 by d and y using accepted R700. If either probe yields the R700 P4 alternative, retain that labelled P4 together with the exact H-t row G_d. Otherwise the DUAL-CP branch tail-signs the reverse initial tested dimer (c,c_0) by both probes, in particular

  (c,c_0,d) tight.

The failed sibling gamma already makes the same tested dimer head-signed by y through (y,c,c_0). Accepted R523 on the fixed tested orientation (c,c_0), with distinct witnesses y and d of opposite polarities, therefore gives the literal tight P4

  (y,c,c_0,d).

Thus the exactly-one-gamma d-row is not merely an H-t reconstruction: it always carries a labelled P4 whose support and failed-sibling ancestry are retained. The case gamma_y tight and gamma_d bad is exact dual and gives either an R700 P4 or

  (d,c,c_0,y).

This strengthens, but does not replace, the exact H-t reconstruction. The source-distance transport may still be applied to that row; the P4 is additional current data and is not itself called closure.

### 2. Paired gamma transport is synchronized but does not force tau=1
Now suppose both gamma turns are tight. At their birth the two exact H-t rows have the same active support, the same literal complement B, and opposite d/y orders:

  R_d=(L,c,d,y,S) | B,
  R_y=(L,c,y,d,S) | B,

where L denotes the possibly empty prefix before c and S the common suffix after the d/y block. The physical vertex c is the immediate predecessor of the block in both rows. Let lambda be the common source distance of the selected d/y state and let

  tau=|S|

be the common number of active vertices strictly after the selected state.

There are three synchronization-preserving moves relevant here, and their coordinate changes must be kept explicit.

COMMON WRAP. While tau>=2, the final two active vertices lie in the common suffix S and the current source is the same in both rows. Hence the tail-wrap seam of `singleton-deep-single-row-source-transport` SV12703 is literally the same test in the two representatives. If it is tight, rotate both rows simultaneously. This preserves the common support and complement and sends

  (lambda,tau) -> (lambda-1,tau+1).

In particular this move decreases lambda but moves tau AWAY from one; it is not a tau-reduction.

COMMON SOURCE TRANSFER. If B+s is Hamiltonian for the common current source s, choose one Hamilton path B_s on B+s and move s from both active rails to that same complement. Since lambda>0, s lies before the selected d/y state in both rows. The paired state remains synchronized and

  (lambda,tau) -> (lambda-1,tau).

TERMINAL SHAVE. If tau>0, the common terminal q lies strictly after the selected d/y state. If B+q is Hamiltonian, choose one Hamilton path B_q and delete q from both active rails. The paired state remains synchronized and

  (lambda,tau) -> (lambda,tau-1).

These moves are strictly decreasing for the lambda-first lexicographic coordinate whenever they are used: the wrap and source transfer decrease lambda, while the shave decreases tau at fixed lambda. Therefore any process using only displayed legal moves is finite. But it need NOT reach tau=1. It may stop with tau>=2 because the common wrap is bad and neither common support transfer is available. Moreover, once the two wrap tests cease to be literally identical, or if only one row has a successful row-specific move, advancing that row loses paired synchronization even though it may still be valid one-row progress.

The predecessor c remains immediately before the d/y block in every synchronized positive-lambda state produced by the moves above. A move from lambda=1 that removes the current source instead reaches lambda=0 and belongs to the closing one-row endgame.

Thus the remainder of this section is CONDITIONAL: assume a synchronized paired state has actually been reached with

  tau=1,  lambda>0,

so the rows have the form

  R_d=(A,c,d,y,q) | B,
  R_y=(A,c,y,d,q) | B,

with common current source s, common terminal q, and the same literal complement B.

Before entering the hard tau-one cell, apply the available support-transfer exits. If B+s is Hamiltonian, the common source transfer is strict paired lambda progress. If B+q is Hamiltonian, the common terminal shave is strict paired tau progress. If B+{s,q} is Hamiltonian, the two-end transfer from SV14742 gives its displayed strict support-transfer progress. Therefore the hard conditional tau-one cell assumes all three supports B+s, B+q, B+{s,q} are non-Hamiltonian.

At tau=1 the two tail-wrap tests are now distinct because their penultimate vertices are y and d respectively. If either row-specific wrap succeeds, that sibling makes strict lambda progress by SV12703, but paired synchronization may be lost. Hence the hard PAIRED tau-one terminal assumes both wraps are bad. R3 then gives

  (s,q,y),   (s,q,d) tight.

Likewise appending omitted t to either row would close H, so

  (t,q,y),   (t,q,d) tight.

These hypotheses place each sibling in the true positive-tail terminal regime used by SV14742, except that SV14742 first separates its opposite-wrap P4 alternative. If that alternative occurs for either row, retain the resulting labelled P4 with its exact complement data and stop. Otherwise the opposite head-wrap needed by the P4-free boundary analysis is retained in each row, and the signature argument below is licensed.

### 3. A P4-free conditional paired tau-one terminal would force two middle-dimer P4s
Under the full conditional hypotheses of Section 2, apply `singleton-deep-tplus-anti-extension-cell` SV14742 separately to the two tau-one rows after excluding its already-successful opposite-wrap P4 output. For R_d the active boundary four-set is

  F_y={s,q,y,t};

for R_y it is

  F_d={s,q,d,t}.

If either F_y or F_d has a Hamilton P4, retain its exact order and stop in labelled P4 output. Its complement is cover-aware: deleting the four-set leaves the untouched B rail and one contiguous active prefix.

Assume both cells are P4-free. SV14742 proves that the only P4-free boundary signature is R516 signature 11. In F_y this gives

  (y,t,q) tight,

while the append obstruction already gives (t,q,y). In F_d signature 11 gives

  (d,t,q) tight,

while the append obstruction gives (t,q,d). Consequently the graph contains both literal P4s

  K_d=(d,t,q,y),
  K_y=(y,t,q,d).

These share the same physical middle dimer {t,q} and exchange d,y as endpoints.

### 4. R833 contradicts the original lower-lift P4-free cell
Use K_y=(y,t,q,d). Delete its middle dimer D={t,q}. From the exact H-t row R_y, deleting terminal q gives the literal exact two-cover of H-{t,q}

  T=(A,c,y,d) | B.

Exactness is automatic: a Hamilton path on H-{t,q} together with the vacuous dimer (t,q) would two-cover H. Both T rails are nontrivial; the true T+ hypotheses give |B|>=4, and the active rail contains c,y,d.

In R833 notation, the P4 endpoints are x=y and y_R=d. Deleting these two endpoints from T leaves exactly two maximal complementary blocks: the contiguous prefix (A,c) and the untouched rail B. Hence b_T(x,y_R)=2 and accepted R833/P907 applies.

The T-active rail selects the endpoint chord y->d, so REVERSE-CHORD, which requires d->y in this R833 orientation, is impossible. The endpoints are adjacent, so ANTI-ENDS is impossible. The terminal vertex d has no selected d->C incidence, so the Y-REVERSE alternative is impossible. Therefore X-REVERSE is forced. Its actual complementary predecessor is c, because c immediately precedes y in R_y. R833 gives

  (t,y,c) tight.

But the original q2 lower-lift branch retained

  (d,t,y) tight

and assumed X_0={t,d,y,c} P4-free. The two consecutive tight turns (d,t,y) and (t,y,c) form the literal P4

  (d,t,y,c),

contradiction.

The exact dual R833 application to K_d and (A,c,d,y)|B forces (t,d,c); it is retained symmetrically but is not needed for the contradiction above.

### 5. Consequence
There is no theorem here that paired gamma transport always reaches tau=1. The synchronized transport is only a finite legal representative process and may terminate at larger tau; a one-row success may also destroy synchronization.

Conditionally, however, if a synchronized paired state reaches tau=1 and all common support-transfer exits are blocked, then a hard paired failed-wrap terminal cannot remain P4-free. A row-specific wrap success is strict one-row lambda progress. An opposite-wrap alternative from SV14742 is already a labelled P4 output. Otherwise, if either boundary four-cell is Hamiltonian, retain that cover-aware P4; and if both are provisionally P4-free, the R833 middle-dimer consumer forces a contradiction to the original q2 P4-free lower-lift cell.

The surviving output is deliberately only P4-valued, not closure: whenever a labelled P4 occurs, retain its exact order, the sibling H-t row(s) that still exist, and the literal residual path fragments. Those cover-aware P4 outputs remain inputs for the next restoration consumer.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R523"
    },
    {
        "relation": "dependency",
        "revision_id": "R700"
    },
    {
        "relation": "dependency",
        "revision_id": "R833"
    }
]
```
