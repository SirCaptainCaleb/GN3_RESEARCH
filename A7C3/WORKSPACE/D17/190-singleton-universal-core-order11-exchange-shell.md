# Universal four-cores force a donor floor and a closed order-eleven 5+5 exchange circuit

**Workspace:** D17
**State:** established
**Key:** `singleton-universal-core-order11-exchange-shell`

**Summary:** A Hamilton core X that Hamilton-extends by every exterior vertex forces its complement Y and every puncture Y-z to be non-Hamiltonian. In the short G1 cell this applies to each of the four audited SV16347 cycle-edge cores: the two deleted labels give SV16094 Hamilton punctures and every b in B preserves an explicit comparison 3-cycle, so R887/R902 Hamiltonizes X+b. Orders |B|<=2 are impossible by R3, |B|=3 by R522, and |B|=4 by R195, hence |B|>=5. At |B|=5, R195 yields a donor-good graph on seven labels and a fixed core puncture supporting a shortest closed same-residue exact 5+5 support-exchange circuit. Outside an explicit R408 endpoint/internal event all circuit covers share one physical endpoint 4-set, forcing exactly three endpoint regimes: two fixed core endpoints and no circuit endpoints; one core endpoint with alternating circuit endpoints on an even cycle; or no core endpoint with every circuit label an endpoint, possible only for cycle length at most four. The fifth SV16734 comparison-cyclic core is not asserted Hamiltonian. SV7318 transfers only at support-circuit level until endpoint exposure is reconstructed.

### 1. Universal-core complement shell
Let H be a Strong Level-(1) boundary tournament with pc(H)>2 and let

  V(H)=X disjoint-union Y,

where X is Hamiltonian and X+z is Hamiltonian for every z in Y. Then

  Y is non-Hamiltonian,
  Y-z is non-Hamiltonian for every z in Y.                    (UC.1)

Indeed a Hamilton Y together with X would two-cover H. If Y-z were Hamiltonian, then the two disjoint Hamilton paths on Y-z and X+z would two-cover H. No minimal-counterexample hypothesis is needed for this shell.

### 2. Four audited universal four-cores in the short G1 cell
Retain accepted exact SV16094 and the current pair-support unit SV16347. Thus

  U={s,q,t,p,u,v},

all punctures U-z are Hamiltonian, B is a literal Hamilton complement, and the four cycle-edge deletions

  D in {{s,q},{s,u},{q,t},{t,p}}

leave explicit Hamilton four-sets X=U-D. The same four X carry the explicit comparison star cycles recorded in SV16347. Consequently for every physical b in B, not merely the endpoints of one chosen B-order, X+b still contains that directed comparison cycle. By accepted R887 it is non-edge-orderable; by accepted R902 every non-Hamiltonian five-set would be edge-orderable. Hence

  X+b is Hamiltonian for every b in B.                         (UC.2)

If D={r,s}, then X+r=U-s and X+s=U-r are Hamiltonian by accepted SV16094. Therefore each of these four fibers satisfies the universal-core shell with

  Y=B union D.                                                  (UC.3)

The fifth cycle edge {p,u} is deliberately not included here: SV16734 proves its four-set {s,q,t,v} comparison-cyclic and proves all one-vertex extensions Hamiltonian, but does not prove that the bare four-set itself is Hamiltonian. The present audited shell does not silently upgrade that statement.

### 3. The donor floor improves to |B|>=5
Fix any one of the four audited fibers D={r,s}.

If |B|<=2, then the shell says Y-r=B+s is non-Hamiltonian, but B+s has order at most three and is Hamiltonian: singletons and dimers are vacuous tight paths, while every three-set has a Hamilton tight order by R3. Contradiction.

If |B|=3, orient B as a tight trimer. By (UC.1), both four-sets B+r and B+s are non-Hamiltonian. Accepted R522 applied to the common tight trimer B and the two exterior labels r,s then Hamiltonizes B+{r,s}=Y, contradicting (UC.1).

If |B|=4, then |Y|=6 and (UC.1) says Y-z is non-Hamiltonian for every one of its six vertices. Accepted R195 says every six-set has at least four Hamiltonian five-punctures, contradiction.

Hence every audited surviving donor fiber has

  |B|>=5.                                                       (UC.4)

This subsumes the old order-four donor taxonomy on these four fibers without asserting that the older local statements were false.

### 4. Order eleven produces one closed same-residue 5+5 support-exchange circuit
Now assume |B|=5. Then |X|=4 and |Y|=7. Define a graph G_Y on Y by

  ab in E(G_Y)  iff  Y-{a,b} is Hamiltonian.                    (UC.5)

For each a in Y, apply R195 to the six-set Y-a. At least four of its five-punctures are Hamiltonian, so

  deg_GY(a)>=4,
  |E(G_Y)|>=14.                                                 (UC.6)

Fix a donor-good edge ab. The six-set X+{a,b} is non-Hamiltonian, because otherwise its Hamilton path together with the Hamilton complement Y-{a,b} would two-cover H. Apply R195 to X+{a,b}. Deleting a gives X+b, Hamiltonian by hypothesis, and deleting b gives X+a. Since at least four of the six punctures are Hamiltonian, at least two distinct x in X satisfy

  (X-x)+{a,b} is Hamiltonian.                                  (UC.7)

Thus there are at least 2|E(G_Y)|>=28 incidences (x,ab) with x in X and ab donor-good satisfying (UC.7). Some fixed x occurs on at least seven donor-good edges. Let G_x be the graph formed by those edges. Since G_x has seven vertices and at least seven edges, it contains a cycle. Choose a shortest cycle

  C=(v_0,v_1,...,v_{m-1},v_0).                                 (UC.8)

Put A=X-x. For every cycle edge e_i={v_i,v_{i+1}}, choose actual Hamilton orders on both five-sets and retain the literal cover

  C_i : (A+{v_i,v_{i+1}}) | (Y-{v_i,v_{i+1}}).                 (UC.9)

All C_i cover the same proper residue H-x. They are exact: H-x cannot be Hamiltonian, since a Hamilton path on H-x together with singleton x would two-cover H. Consecutive covers exchange exactly the two physical labels v_{i-1} and v_{i+1} across the common pivot v_i while retaining the physical three-core A.

By shortestness, any G_x chord of C is already a strictly shorter support-exchange circuit and is immediate progress. No claim is made that arbitrary Hamilton orders on the displayed supports expose the exchanged labels as endpoints.

### 5. Endpoint-status synchronization or an explicit R408 event
Compare the actual exact covers C_i on the common residue H-x. If a physical vertex is an endpoint in one C_i and internal in another, retain the two named covers, the physical vertex, and the endpoint/internal discrepancy as an explicit R408 event. This is circuit-current geometry; it is not paid here.

Outside every such event, accepted R408 implies that all covers C_i have the same physical endpoint set E. Since each cover consists of two Hamilton P5s,

  |E|=4.                                                        (UC.10)

Write

  alpha=|E cap A|.

For every cycle edge {v_i,v_{i+1}}, the active rail A+{v_i,v_{i+1}} has exactly two endpoints. Therefore

  alpha + 1_E(v_i)+1_E(v_{i+1}) = 2                            (UC.11)

for all i. The right side is independent of i, so exactly three regimes are possible.

(A-INTERNAL-CIRCUIT) alpha=2 and 1_E(v_i)=0 for every circuit label. Two fixed vertices of the three-core A are the endpoints of every active P5, and every circuit label is internal in every cover in which it appears.

(ALTERNATING) alpha=1 and every cycle edge has exactly one endpoint label. Hence C is even and endpoint membership alternates around C. In particular, for each pivot v_i the exchanged labels v_{i-1},v_{i+1} have the same endpoint status: both endpoint at one parity of pivots and both internal at the other.

(ALL-ENDPOINT) alpha=0 and both ends of every cycle edge belong to E. Thus every circuit label lies in E. Since |E|=4, this regime forces m<=4. Here all exchanged labels are endpoint-currentized simultaneously.

No other R408-quiet endpoint pattern exists. In particular every odd shortest cycle of length at least five is forced into A-INTERNAL-CIRCUIT: all of its circuit labels are internal in every selected 5+5 cover. This is the exact systematic failure mode of endpoint currentization.

### 6. Transfer fence from SV7318
The role-recurrence mechanism of `singleton-reusable-exchange-circuit` may only be imported after exchanged endpoints have actually been currentized and the trimmed common Hamilton orders have been compared. Its singleton-deletion/R511 mechanism for manufacturing endpoint-current representatives does not transfer automatically to (UC.9). Moreover all covers (UC.9) live on H-x, so the old SV7318 step in which opposite attachment roles immediately span H must be re-proved using the universal core rather than copied verbatim.

The next consumer should therefore attack the three exact regimes above. ALL-ENDPOINT is the direct role-recurrence entrance; ALTERNATING offers endpoint-currentization on every other pivot; A-INTERNAL-CIRCUIT is the genuine systematic failure theorem and should be attacked through its fixed two-ended core orders or an explicit order-discrepancy event, not by generic payment.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R195"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
