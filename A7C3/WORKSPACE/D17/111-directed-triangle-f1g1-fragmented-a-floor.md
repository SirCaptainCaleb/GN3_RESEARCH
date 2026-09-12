# The F1G1 fragmented-A floor reduces to one no-A|B split-rail topology

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-f1g1-fragmented-a-floor`

**Summary:** For a transition-minimal F1G1 exact pair-deletion representative with A={a,b} fragmented and t=3, P,Q,B are whole blocks. The 1+4 rail shape is consumed; if both A-singletons lie on one rail, A-Q-A contradicts t-minimality, A-B-A enters the exact mu-transfer unit outside R435 order activity, and A-P-A forces a two-ended R548 wrap-shield pair. If A lies on both rails, any actual A|B boundary gives a one-seam current-boundary reversal, while the no-A|B case has only two support types; one collapses to t=2 via the locked A+Q path, leaving only (A-P)|(A-Q-B). This is a conditional reduction, not closure.

### 1. Fragmentation identity and the t=3 floor
Retain the F1G1 first-bad cell of SV11804 with coarse blocks

  A={a,b}, P={j0,j1,m}, Q={c,x}, B,

literal J=(j0,j1,m,x,c) on P union Q and locked L=(a,b,c,x) on A union Q. For an exact H-{u,v} cover T let b_X(T) be the number of maximal coarse X-blocks along its two rails. If t(T) is the number of selected edges joining distinct coarse cells, splitting the two rails at all such transitions gives

  t=b_A+b_P+b_Q+b_B-2.

Assume T is transition-minimal in F1G1, A is fragmented, and t=3. Then b_A=2 and necessarily

  b_P=b_Q=b_B=1.

Thus there are exactly five coarse blocks A,A,P,Q,B.

### 2. The 1+4 rail shape is consumed
A 1+4 coarse split isolates one whole block. An isolated A is a singleton target rail; the other rail is Hamiltonian, while the singleton together with deleted u,v forms a tight trimer in some order, giving a spanning two-cover of H. Isolated B is the B-quiet codimension-two currentization already proved in SV11804. Isolated Q is the {c,x} dimer-to-codimension-one branch there. If P is isolated, test P+u and P+v. A Hamilton P4 gives codimension-one reconstruction; if both are P4-free, accepted R522/P537 Hamiltonizes P+{u,v}, closing H with the other rail. Hence every genuinely hard t=3 fragmented-A representative has a 2+3 coarse split.

### 3. Both A-singletons on one rail
Then the three-block rail is A-X-A for X in {P,Q,B}.

If X=Q, its support is A union Q. Replacing that entire rail by the retained locked Hamilton path L=(a,b,c,x) changes A-Q-A to one A-Q transition while leaving the other rail unchanged, giving t=2, contrary to transition minimality.

If X=B, the other rail has support P union Q and may be normalized to literal J. If the current Hamilton order on the whole B-block differs from the literal ancestral B order, retain the explicit R435 order activity. Outside R435, the A-B-A rail together with literal J is exactly the mu=2 endpoint-only cell of `directed-triangle-f1g1-endpoint-mu-transfer`; apply that bounded consumer and retain its terminal output.

If X=P, consider the two cyclic rotations of the actual A-P-A rail that move one endpoint A-label across the rail and make the two A-labels contiguous. Either successful R548 wrap would reduce the number of A-blocks by one and hence produce t=2, contradicting transition minimality. Therefore both relevant wrap turns fail. R3 yields a two-ended named wrap-shield pair on the actual P-block endpoints and the two A labels. This pair is retained; no generic packet payment is taken.

### 4. A-singletons on different rails: conditional A|B currentization
Now each target rail contains one A-singleton. Suppose one of them, h, is actually adjacent to the whole B-block, and let e be the other A-label. If the current boundary is h|B with B beginning b0, replace the P union Q support by literal J and move e next to h on the B-side. The existing h|B turn certifies the second junction, so the sole new seam is

  kappa=(e,h,b0).

If kappa were tight the resulting exact cover would have t=2. Therefore kappa is bad and R3 gives

  (b0,h,e) tight,

an exact reversal of the current selected h->b0 boundary with e as witness. Dually, for B|h with B ending bL, the sole seam (bL,h,e) is bad and R3 gives (e,h,bL). If |B|=1, either orientation of this trimer Hamiltonizes A union B and together with literal J gives the forbidden t=2 exit. Thus any surviving conditional A|B shield has |B|>=2.

### 5. The no-A|B split has one unresolved topology
Assume instead that no A-singleton is adjacent to B. Up to reversing rails and exchanging a,b, there are only two coarse support types:

  (A-P) | (A-Q-B),
  (A-Q) | (A-P-B).

Indeed in a 2+3 split the two blocks adjacent to the two A-singletons must be P and Q, leaving B as the far block of the three-block rail.

The second type cannot survive transition minimality. Its A-Q rail has support exactly A union Q, so replace it by L=(a,b,c,x); leave the existing contiguous P-B rail untouched. The result has exactly the two coarse transitions A-Q and P-B, hence t=2.

Therefore the only no-A|B t=3 fragmented-A topology not consumed above is

  (A-P) | (A-Q-B),

up to the stated symmetries. This section does not claim to consume that final topology. In particular R933 is not invoked merely from the deleted pair {u,v}; its endpoint-controlled Hamilton-path hypothesis is not supplied by the retained four-support paths.

### 6. Exact scope
At the minimum fragmented-A floor t=3, every branch leaves by codimension improvement/closure, the exact mu consumer, a named two-ended wrap shield, a current A|B reversal, or the single no-A|B support type (A-P)|(A-Q-B). For t>=4 at least one of P,Q,B fragments in addition to A, but no further taxonomy is asserted here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    },
    {
        "relation": "dependency",
        "revision_id": "R548"
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
