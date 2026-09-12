# Every endpoint-return edge is a complementary transfer or a named fixed-boundary reverse trimer

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-endpoint-return-transfer-compiler`

**Summary:** In a fixed-complement critical block V(H)=Omega disjoint-union Q, combine the full all-Omega boundary wall with any actual endpoint incidence a->b from the accepted R945/R961 endpoint-return system. If b is the HEAD of a Hamilton puncture path P_a=(b,r1,...) on Omega-a, test (q0,b,r1). Failure gives the named reverse trimer (r1,b,q0). Success transfers q0 into Omega-a, giving an exact H-a row (q0,P_a)|Q[1,t]; the reciprocal support a+Q[1,t] is non-Hamiltonian and forces the first-inward star (q2,q1,a). The universal outer wall at b then pulls q1 as well, yielding a second pushed row and, when it survives, the second-inward star (q3,q2,a). The TAIL role is the exact terminal dual. Thus every matched endpoint-return arc is a literal support-transfer-or-blocker cell on one fixed complement boundary, with the deleted label gaining inward stars when transfer succeeds.

### 1. Fixed-complement endpoint-return coordinates
Retain a hypothetical smallest counterexample with

  V(H)=Omega disjoint_union V(Q),
  Q=(q_0,q_1,...,q_t),

where Omega is non-Hamiltonian deletion-Hamiltonian and Q is a literal Hamilton path. Retain the full two-ended critical-block wall SV23225.

Let a,b be distinct vertices of Omega and let P_a be an ACTUAL Hamilton path on Omega-a having b as a physical endpoint. This is exactly the data carried by an endpoint-core incidence a->b in accepted R945/R961. No R435 quietness is assumed.

### 2. HEAD endpoint: one test gives transfer or a named blocker
Assume first that b is the head of P_a and write

  P_a=(b,r_1,r_2,...,r_k).

SV23225 gives

  (q_1,q_0,b) tight.                                    (ET.1)

Test the single attachment turn

  gamma_a=(q_0,b,r_1).                                  (ET.2)

If gamma_a is bad, R3 gives the exact reverse trimer

  (r_1,b,q_0) tight.                                    (ET.3)

This blocker retains the matched endpoint b, its first inward puncture neighbor r_1, the deleted label a, and the fixed complement boundary q_0.

Assume gamma_a is tight. Then

  P_a^0=(q_0,b,r_1,...,r_k)                             (ET.4)

is a literal Hamilton path on (Omega-a) union {q_0}. Together with

  Q^1=(q_1,q_2,...,q_t)

it gives an exact two-cover of H-a.

The reciprocal support {a} union V(Q^1) is non-Hamiltonian, since a Hamilton path on it together with P_a^0 would two-cover H. If |Q|>=3 and (a,q_1,q_2) were tight, the literal order (a,q_1,q_2,...,q_t) would Hamiltonize that reciprocal support. Therefore

  (q_2,q_1,a) tight.                                    (ET.5)

So one successful endpoint transfer forces the deleted label a onto the first-inward reverse source dimer.

### 3. The same successful test automatically pulls q_1 too
Still in the successful HEAD branch, prepend q_1 to (ET.4). The sole new turn is (q_1,q_0,b), already tight by (ET.1). Thus

  P_a^1=(q_1,q_0,b,r_1,...,r_k)                         (ET.6)

is Hamiltonian on (Omega-a) union {q_0,q_1}, with literal complement

  Q^2=(q_2,q_3,...,q_t).

Hence {a} union V(Q^2) is non-Hamiltonian. If |Q|<=4, that reciprocal support has order at most three and is Hamiltonian (vacuously for order at most two, and by R8/R3 for order three), contradiction. Therefore a surviving successful endpoint transfer forces |Q|>=5. For |Q|>=5, the turn (a,q_2,q_3) must be bad, so R3 gives

  (q_3,q_2,a) tight.                                    (ET.7)

Thus a successful HEAD endpoint edge exports two exact pushed singleton rows and places its deleted label a on two consecutive inward reverse source dimers.

### 4. TAIL endpoint dual
If b is instead the tail of P_a, write

  P_a=(r_0,...,r_{k-1},b).

The full wall gives (b,q_t,q_{t-1}) tight. Test

  gamma_a^R=(r_{k-1},b,q_t).

If it is bad, R3 gives the named blocker

  (q_t,b,r_{k-1}) tight.                                (ET.8)

If it is tight, first append q_t and then, using the full wall, q_{t-1}. These give exact pushed H-a rows with complements Q[0,t-1] and Q[0,t-2]. Reciprocal non-Hamiltonicity forces, in the surviving range |Q|>=5,

  (a,q_{t-1},q_{t-2}) tight,
  (a,q_{t-2},q_{t-3}) tight.                            (ET.9)

This is the exact terminal dual of (ET.5)-(ET.7).

### 5. Endpoint-return functional graph interpretation
Apply the compiler to every matched arc a->f(a) of any accepted R945 endpoint-return matching, retaining the actual matched puncture path and its certified HEAD/TAIL role. Every arc has exactly one of two outputs:

  TRANSFER: a literal one- and two-vertex complementary support push, with the deleted label a forced onto the first two inward reverse Q dimers on the role-correct side;

  BLOCKER: one named reverse trimer at the corresponding fixed Q boundary, using the matched endpoint and its adjacent puncture-path neighbor.

This statement uses no R435 quietness and therefore applies on both sides of the R961 dichotomy. It upgrades the endpoint-return functional graph from a bookkeeping object to a support-transfer-or-blocker system. No assertion is made that one transfer closes H, that blockers on different arcs synchronize automatically, or that the pushed active block is deletion-Hamiltonian.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R945"
    }
]
```
