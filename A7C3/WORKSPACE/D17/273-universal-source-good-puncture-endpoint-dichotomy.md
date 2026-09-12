# Every Arm-U good puncture either produces same-complement R435 curvature or exposes a bad endpoint with wall-bearing pair-deletion curvature

**Workspace:** D17
**State:** established
**Key:** `universal-source-good-puncture-endpoint-dichotomy`

**Summary:** In the Arm-U fixed-universe setup V(H)=Omega disjoint B, let q be good and P_q=(p0,...,pm) any actual Hamilton puncture path on Omega-q. For either endpoint r of P_q, (P_q-r)|B is an exact two-cover of H-{q,r}. The good source label q tail-signs the reverse initial boundary dimer and head-signs the reverse terminal boundary dimer of the fixed Hamilton complement B. If an endpoint r is bad, then the literal word obtained by replacing r with q would Hamiltonize Omega-r except for its unique new boundary turn; since Omega-r is non-Hamiltonian, that turn is bad and R3 makes q witness the reverse boundary dimer one step inward in P_q-r. Thus a bad endpoint produces an exact pair-deletion frame with fixed rail B and a named q-signed reverse boundary dimer on the other rail. If both endpoints of P_q are good, their Hamilton puncture paths supply the two endpoint replacements in accepted R966 for base P_q and exterior q, while Omega itself is non-Hamiltonian; hence P_q and the two endpoint-replacement puncture paths emit explicit R435 geometry, all as singleton rows with the same literal complement B. Consequently, in any R435-quiet Arm-U fixed universe, EVERY actual Hamilton puncture path for EVERY good q has at least one bad endpoint. Arm U is therefore reduced to same-complement R435 curvature or a good-to-bad endpoint boundary cell on an exact pair-deletion residue. Working/unreviewed exposition only.


### 1. Fixed-universe coordinates
Let H be a hypothetical smallest counterexample and retain the Arm-U fixed-universe setup

  V(H)=Omega disjoint_union V(B),
  B=(b_0,b_1,...,b_t),

where B is a literal Hamilton tight path and Omega is non-Hamiltonian. Put

  G(Omega)={q in Omega : Omega-q is Hamiltonian},
  D(Omega)={z in Omega : Omega-z is non-Hamiltonian}.

Fix q in G(Omega) and choose ANY actual Hamilton puncture path

  P_q=(p_0,p_1,...,p_m)                                  (EP.1)

on Omega-q. Then

  P_q | B                                                 (EP.2)

is an exact singleton-deletion two-cover of H-q. Exactness is forced by counterexamplehood: if H-q were Hamiltonian, its Hamilton path together with singleton q would two-cover H. We need only the following R24-free source floor: |P_q|,|B|>=3. Indeed, in any exact singleton-deletion row H-q=A|B, if A={a} then (q,a)|B is a spanning two-cover of H. If A=(a_0,a_1), boundary antisymmetry R3 makes exactly one of the reversed turns (q,a_0,a_1) and (a_1,a_0,q) tight, so that tight trimer together with the untouched rail B is again a spanning two-cover of H. Hence |A|>=3, and symmetrically |B|>=3. Applied to P_q|B, this defines every boundary turn below and gives the order-at-least-three hypothesis required by R966.

The good label q already gives the fixed-complement two-ended wall. If (q,b_0,b_1) were tight, then (q,B)|P_q would two-cover H; hence R3 gives

  (b_1,b_0,q) tight.                                      (EP.3)

Dually

  (q,b_t,b_{t-1}) tight.                                  (EP.4)

Thus q tail-signs the reverse initial B-dimer and head-signs the reverse terminal B-dimer.

### 2. Every puncture endpoint gives an exact pair-deletion frame
Let r be either endpoint of P_q. Delete q and r. Trimming r from the literal puncture path gives

  (P_q-r) | B                                             (EP.5)

as a two-path cover of H-{q,r}. It is exact. If H-{q,r} were Hamiltonian, that Hamilton path together with the vacuous tight dimer (q,r) would be a spanning two-cover of H.

Hence every physical endpoint of every chosen good puncture word determines one actual exact pair-deletion row with the SAME literal complement B.

### 3. A bad endpoint puts curvature directly on the pair-deletion boundary
Suppose first that the left endpoint r=p_0 lies in D(Omega). Then Omega-p_0 is non-Hamiltonian. Consider the literal replacement word

  (q,p_1,p_2,...,p_m)                                    (EP.6)

on Omega-p_0. All consecutive turns except the first are inherited from P_q. If the first turn (q,p_1,p_2) were tight, (EP.6) would be a Hamilton path on Omega-p_0, contradiction. Therefore R3 gives

  (p_2,p_1,q) tight.                                      (EP.7)

In the exact pair-deletion row

  (p_1,p_2,...,p_m) | B                                  (EP.8)

this says that the deleted good label q TAIL-signs the reverse initial boundary dimer

  (p_2,p_1)                                               (EP.9)

of the active puncture core.

The right endpoint is the exact dual. If r=p_m is bad, then the candidate

  (p_0,...,p_{m-2},p_{m-1},q)

cannot be Hamiltonian on Omega-p_m, so

  (q,p_{m-1},p_{m-2}) tight.                              (EP.10)

Thus q HEAD-signs the reverse terminal boundary dimer (p_{m-1},p_{m-2}) of the exact pair-deletion core P_q-p_m.

Combining (EP.3)-(EP.4) with (EP.7) or (EP.10), a bad endpoint therefore yields a WALL-BEARING PAIR-DELETION CURVATURE CELL:

- one exact H-{q,r} row (P_q-r)|B;
- the fixed Hamilton rail B with q witnessing both reverse boundary dimers;
- one named reverse boundary dimer on the other rail, also witnessed by q;
- the physical good/bad labels q,r and the exact source word P_q retained.

No representative transport is used.

### 4. Two good endpoints force same-complement R435 curvature
Now suppose BOTH endpoints p_0,p_m lie in G(Omega). Choose actual Hamilton puncture paths

  P_0 on Omega-p_0,
  P_m on Omega-p_m.                                      (EP.11)

Apply accepted R966 with

  Q=P_q,
  X=Omega-q,
  y=q.                                                    (EP.12)

The full extension X+y=Omega is non-Hamiltonian. The two endpoint-replacement supports are

  (X-{p_0})+q = Omega-p_0,
  (X-{p_m})+q = Omega-p_m,                                (EP.13)

and are Hamiltonian by (EP.11). Therefore R966 forces explicit R435 Reverse-Ear geometry among the three ACTUAL Hamilton paths

  P_q, P_0, P_m:                                         (EP.14)

an adjacent selected reversal, a reverse tight trimer, or a proper tight cycle.

Moreover each puncture path occurs in an exact singleton-deletion row with the SAME literal complement B:

  H-q   : P_q | B,
  H-p_0 : P_0 | B,
  H-p_m : P_m | B.                                       (EP.15)

Thus the curvature in (EP.14) is literally fixed-complement curvature of the same kind demanded by G18, without first currentizing to an anonymous forest.

### 5. Arm-U endpoint router
For every good q and every actual Hamilton puncture word P_q, exactly one of the following usable alternatives holds:

GOOD-GOOD ENDPOINTS:
  both endpoints of P_q are good, and accepted R966 gives explicit R435 curvature among three puncture rows sharing literal complement B;

GOOD-BAD BOUNDARY:
  at least one endpoint r of P_q is bad, and H-{q,r} has the exact wall-bearing pair-deletion curvature cell of Section 3.     (EP.16)

In particular, if a fixed Arm-U universe is R435-quiet throughout its common-B puncture family, then EVERY Hamilton puncture path P_q for EVERY q in G(Omega) has at least one endpoint in D(Omega). Equivalently, the bad-deletion set is an endpoint transversal of the entire retained good-puncture family.

This is substantially stronger than the raw curvature fan. The defect is not merely somewhere within distance two of a bad deletion: outside same-complement R435 activity, a bad deletion must occur at an actual puncture boundary, where its curvature lives on a named exact pair-deletion representative.

### 6. G18 interface and remaining gap
The natural cross-arm object suggested by (EP.16) is a WALL-BEARING PAIR-DELETION CURVATURE CELL rather than a bare current trimer. Arm M supplies the strong form: two deleted labels belong to a deletion-Hamiltonian complement of a fixed cap, with the full universal cap wall and R945/R966 ancestry. Arm U supplies either the same-complement R966 form directly, or the mixed good-bad boundary form above.

The present theorem does not consume the good-bad boundary cell. It does not prove that the q-signed inward reverse dimer reenters the phased Morse process below an earlier checkpoint, and it does not manufacture a second deleted-label wall witness when r is bad. That distinction is exactly what the Arm-U stress test is meant to expose.

The next parent-cancellation theorem should therefore ask whether ONE two-ended fixed-rail wall witness q plus one q-signed boundary dimer on the opposite rail of an exact pair-deletion row is sufficient for two-cover / strict canonical reentry, or whether Arm-M cancellation genuinely needs the second wall witness supplied by deletion-Hamiltonicity. Either resolution sharply identifies the load-bearing hypothesis.

Status: complete internal working mathematics, unreviewed exposition. No canonical certification or O4 closure is claimed.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```